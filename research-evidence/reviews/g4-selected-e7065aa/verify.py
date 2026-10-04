"""Read-only source integrity and local-target checks for G4's bounded review.

Run from any directory with Python 3; output is confined to this review folder.
No source, asset, author manifest or operating instruction is rewritten.
"""
from pathlib import Path
import hashlib
import json
import re
import struct
import subprocess
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
SOURCE = "e7065aaa92acdf223628f9d7099301d766810ad3"
BASE = "617ec16956e64c590d27930e91979f89e8399070"
REF = "research-evidence/g2-06-restaurants-brand/refinement"

def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])

def digest(data):
    return hashlib.sha256(data).hexdigest()

failures = []
preserved = []
for p in git("ls-tree", "-r", "--name-only", SOURCE, "--", REF).decode().splitlines():
    frozen = git("show", f"{SOURCE}:{p}")
    current = git("show", f"HEAD:{p}")
    passed = frozen == current
    preserved.append({"path": p, "source_blob_sha256": digest(frozen), "current_git_blob_matches": passed})
    if not passed:
        failures.append(f"Changed frozen source: {p}")

assets = []
for folder, filenames in [
    ("signature-and-first-model", ["02-expresion-sin-personajes.png", "03-orilla-contraste-propuesto.png"]),
    ("polish-v2", ["01-cafeteria-refinada-v2.png", "02-campana-refinada-v2.png"]),
]:
    manifest_path = ROOT / REF / folder / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for filename in filenames:
        item = next(a for a in manifest["assets"] if a["file"] == filename)
        p = manifest_path.parent / filename
        raw = p.read_bytes()
        dimensions = list(struct.unpack(">II", raw[16:24])) if raw[:8] == b"\x89PNG\r\n\x1a\n" else None
        checks = {"hash": digest(raw) == item["sha256"], "bytes": len(raw) == item["bytes"], "dimensions": dimensions == item["dimensions"], "frozen_blob": raw == git("show", f"{SOURCE}:{p.relative_to(ROOT).as_posix()}")}
        assets.append({"path": p.relative_to(ROOT).as_posix(), "sha256": digest(raw), "bytes": len(raw), "dimensions": dimensions, "checks": checks})
        if not all(checks.values()):
            failures.append(f"Asset integrity mismatch: {filename}")

original_path = "research-evidence/g2-06-art-direction-2026-10-03/storefront-v0.2/02-cartel-revisado-v0.2.png"
raw = (ROOT / original_path).read_bytes()
original = {"path": original_path, "sha256": digest(raw), "bytes": len(raw), "dimensions": list(struct.unpack(">II", raw[16:24])), "matches_selected_hash": digest(raw) == "4f576dd2156f9361abee8338df13704cfd4dc70a4e5e2a47d11de8fbf567f989", "matches_frozen_blob": raw == git("show", f"{SOURCE}:{original_path}")}
if not original["matches_selected_hash"] or not original["matches_frozen_blob"]:
    failures.append("Original ORILLA not preserved")

source_docs = [ROOT / "docs/design/valiris-restaurants-brand-refinement.md", ROOT / REF / "selected-three-references-2026-10-03.es.md", ROOT / REF / "founder-clarification-2026-10-03.es.md"]
# Materialise the owned output before checking report links to that output.
# The final result below replaces this provisional record in the same run.
(OUT / "checks.json").write_text("{\"status\": \"checking local targets\"}\n", encoding="utf-8", newline="\n")
docs = source_docs + sorted(OUT.glob("*.md"))
links = []
for doc in docs:
    for target in re.findall(r"\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
        target = target.strip().strip("<>").split("#", 1)[0]
        if not target or re.match(r"^[a-zA-Z]+:", target):
            continue
        dest = (doc.parent / unquote(target)).resolve()
        passed = dest.exists() and dest.is_relative_to(ROOT)
        links.append({"document": doc.relative_to(ROOT).as_posix(), "target": target, "exists_inside_repository": passed})
        if not passed:
            failures.append(f"Missing/local target outside root: {target}")

result = {"review_source_sha": SOURCE, "operating_baseline_sha": BASE, "source_files": preserved, "assets": assets, "preserved_original": original, "local_targets": links, "limits": ["PNG header dimensions and file integrity only; no responsive or accessibility certification", "Git blobs compared to frozen source; no author output rewritten", "Remote links and Markdown fragment validity not checked", "Attachment equality is not reverified here; founder selection and author records are attributed sources", "Manual visual observations are in g4-review.md, not inferred from this script"], "failures": failures}
(OUT / "checks.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"source_files_preserved": len(preserved), "assets_checked": len(assets), "original_preserved": original["matches_selected_hash"] and original["matches_frozen_blob"], "local_targets_checked": len(links), "failures": failures}, ensure_ascii=False))
raise SystemExit(bool(failures))
