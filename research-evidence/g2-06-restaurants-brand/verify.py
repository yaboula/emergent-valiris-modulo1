"""Verify this static delivery. Run from any directory with Python 3; no dependencies.

Use --write-checks to refresh checks.json after a deliberate evidence change.
This checks artifact integrity and source preservation, not an implemented product.
"""
import argparse
import hashlib
import json
import re
import struct
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BASE = "27861fd94dafd51889e2f223000320d66fd39dae"
BRANCH = "docs/m1-g2-06-restaurants-brand"
OWN = ("docs/design/valiris-restaurants-brand-direction.md",
       "research-evidence/g2-06-restaurants-brand/")


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def sha(data):
    return hashlib.sha256(data).hexdigest()


def owned(path):
    return path == OWN[0] or path.startswith(OWN[1])


def contrast(fg, bg):
    def lum(hex_color):
        rgb = [int(hex_color[i:i+2], 16)/255 for i in (1, 3, 5)]
        linear = [c/12.92 if c <= .04045 else ((c+.055)/1.055)**2.4 for c in rgb]
        return sum(c*w for c, w in zip(linear, (.2126, .7152, .0722)))
    lo, hi = sorted((lum(fg), lum(bg)))
    return round((hi+.05)/(lo+.05), 2)


def verify():
    errors = []
    def check(condition, detail):
        if not condition:
            errors.append(detail)
    manifest = json.loads((HERE/"manifest.json").read_text(encoding="utf-8"))
    check(Path(git("rev-parse", "--show-toplevel").decode().strip()).resolve() == ROOT,
          "Unexpected repository root")
    check(git("branch", "--show-current").decode().strip() == BRANCH,
          "Unexpected working branch")
    check(subprocess.run(["git", "-C", str(ROOT), "merge-base", "--is-ancestor",
                          BASE, "HEAD"], capture_output=True).returncode == 0,
          "Agreed baseline is not an ancestor")
    changed = git("diff", "--name-only", BASE).decode().splitlines()
    untracked = git("ls-files", "--others", "--exclude-standard").decode().splitlines()
    check(all(owned(p) for p in changed+untracked), "Changes outside reserved paths")
    for source in manifest["repositorySources"]:
        blob = git("show", source["commit"]+":"+source["path"])
        check(sha(blob) == source["sha256"], "Frozen source hash: "+source["path"])
        # The source guide uses an earlier commit; its current version is preserved separately.
        if source["commit"] == BASE:
            check((ROOT/source["path"]).read_bytes() == blob,
                  "Baseline source changed: "+source["path"])
    check(not git("diff", "--name-only", BASE, "--", "docs", "coordination",
                  "AGENTS.md", "CONTRIBUTING.md", "HANDOFF.md", "CHANGELOG.md",
                  "research-evidence/g2-06-art-direction-2026-10-03",
                  "research-evidence/reviews").decode().splitlines()
          or all(owned(p) for p in git("diff", "--name-only", BASE).decode().splitlines()),
          "Protected project sources changed")
    asset_count = 0
    png_dimensions = {}
    svg_count = 0
    for asset in manifest["assets"]:
        path = ROOT/asset["path"]
        data = path.read_bytes()
        asset_count += 1
        exact = len(data) == asset["bytes"] and sha(data) == asset["sha256"]
        normalized = data.replace(b"\r\n", b"\n")
        text_equivalent = ("lfSha256" in asset
                           and len(normalized) == asset["lfBytes"]
                           and sha(normalized) == asset["lfSha256"])
        check(exact or text_equivalent,
              "Asset integrity: "+asset["path"])
        if path.suffix == ".png":
            check(data[:8] == b"\x89PNG\r\n\x1a\n", "PNG header: "+path.name)
            dims = list(struct.unpack(">II", data[16:24]))
            check(dims == asset["dimensions"], "PNG dimensions: "+path.name)
            png_dimensions[path.name] = dims
        if path.suffix == ".svg":
            svg = ET.fromstring(data)
            svg_count += 1
            check(svg.tag.endswith("svg"), "SVG root: "+path.name)
            if "dimensions" in asset:
                dims = [float(svg.attrib[k].removesuffix("px")) for k in ("width", "height")]
                check(dims == asset["dimensions"], "SVG dimensions: "+path.name)
                check(not any(el.tag.endswith("}text") for el in svg.iter()),
                      "Board has unoutlined text: "+path.name)
            for el in svg.iter():
                for key, value in el.attrib.items():
                    if key.endswith("href"):
                        check(not value.startswith(("http:", "https:", "file:")),
                              "SVG external resource: "+path.name)
        if asset["kind"] == "font-license":
            check(b"SIL OPEN FONT LICENSE Version 1.1" in data,
                  "OFL notice missing: "+path.name)
    png_source = (ROOT/manifest["orilla"]["sourcePath"]).read_bytes()
    check(sha(png_source) == manifest["orilla"]["sha256"], "Selected ORILLA changed")
    audit = json.loads((HERE/"figma-validation.json").read_text(encoding="utf-8"))
    check(len(audit["checks"]) == 7, "Expected seven Figma sheets")
    text_count = sum(c["textCount"] for c in audit["checks"])
    check(text_count == 144, "Expected 144 authored native text nodes")
    for c in audit["checks"]:
        check(not c["failures"] and c["minimumTextContrast"] >= 4.5,
              "Figma bounds/contrast failure: "+c["id"])
    for pair in audit["pairs"]:
        check(contrast(pair["foreground"], pair["background"]) == pair["ratio"],
              "Contrast arithmetic disagrees: "+str(pair))
    link_count = 0
    md_paths = [ROOT/OWN[0], *HERE.glob("*.md")]
    for path in md_paths:
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", content):
            if target.startswith(("https://", "http://", "#", "mailto:")):
                continue
            link = unquote(target.split("#", 1)[0])
            check((path.parent/link).exists(), "Broken local link: "+path.name+" -> "+link)
            link_count += 1
    doc = (ROOT/OWN[0]).read_text(encoding="utf-8")
    check("Recommend A" in doc and "R1" in doc and "Hacer sitio" in doc,
          "Recommendation missing")
    check("Powered by Valiris Restaurants" in doc, "Exact attribution missing")
    check("not approved" in doc and "two or three base models" in doc,
          "Approval/model boundary missing")
    return {
        "edition": "2026-10-03 / v1.0",
        "baseline": BASE,
        "expectedBranch": BRANCH,
        "result": "PASS" if not errors else "FAIL",
        "checks": {
            "ownedPathsOnly": all(owned(p) for p in changed+untracked),
            "frozenRepositorySources": len(manifest["repositorySources"]),
            "assetHashesAndBytes": asset_count,
            "pngDimensions": png_dimensions,
            "svgDocuments": svg_count,
            "localMarkdownLinks": link_count,
            "orillaUnchanged": sha(png_source) == manifest["orilla"]["sha256"],
            "nativeFigmaSheets": len(audit["checks"]),
            "nativeTextNodes": text_count,
            "minimumAuthoredTextContrast": min(c["minimumTextContrast"] for c in audit["checks"]),
            "contrastPairsRecomputed": audit["pairs"],
        },
        "limits": [
            "Opaque solid colors and immediate-parent bounds; ORILLA raster text excluded.",
            "No functional UI, full accessibility, translation, user or independent review.",
            "Binary hashes are exact; text may use recorded LF-equivalent hashes across Git newline conversion.",
            "Hashes do not establish legal clearance or successful reproduction in Figma.",
            "Font source notices pinned; exact Figma binaries unidentified and not distributed.",
            "Git author, remote publication and PR recorded separately in publication.json."
        ],
        "errors": errors,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-checks", action="store_true")
    args = parser.parse_args()
    report = verify()
    if args.write_checks:
        (HERE/"checks.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n",
                                       encoding="utf-8", newline="\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["result"] == "PASS" else 1)
