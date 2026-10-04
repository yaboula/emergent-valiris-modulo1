"""Bounded documentary checks; no product, food, SEO or accessibility tests.

Preserves all 1.0 evidence. Writes only this revision's two JSON reports.
"""

import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[3]
BASE = "b30dada1ac8fa5be01d07092ec6c7dbfe80a0439"
ORIGINAL = "5bd3184ca48be8d579e3f82d3361dbf5de0ed228"
SEO = "0c17480bdc2b6ff8037022228ebc4599a704e702"
IA = "ff8fc061dfb4e63461ee2b77b5a18f02108edb6b"
BRANCH = "docs/m1-g2-04-orilla-seo-consolidation"
CASE = "docs/design/orilla-case.md"
COPY = "docs/design/m1-storefront-content-and-copy.md"
OWN = "research-evidence/g2-04-storefront/seo-consolidation-1.1/"
LEGACY = "research-evidence/g2-04-storefront/"

# Reuse immutable documentary parsing/source lists, never its main() or writes.
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("orilla_legacy_evidence", HERE.parent / "verify.py")
legacy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(legacy)


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def source(sha, path):
    return git("show", f"{sha}:{path}").decode("utf-8-sig")


def records(body, prefix):
    return legacy.table_records(body, prefix)


def between(body, start, end):
    return body[body.index(start):body.index(end)]


def tree(prefix):
    return git("ls-tree", "-r", "--name-only", BASE, prefix).decode().splitlines()


def main():
    assert Path(git("rev-parse", "--show-toplevel").decode().strip()).resolve() == ROOT
    assert git("branch", "--show-current").decode().strip() == BRANCH
    git("merge-base", "--is-ancestor", BASE, "HEAD")
    changed = set(git("diff", "--name-only", BASE).decode().splitlines())
    untracked = set(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
    assert all(p in (CASE, COPY) or p.startswith(OWN) for p in changed | untracked), "Foreign or legacy evidence changed"
    git("diff", "--check", BASE)

    old_case, old_copy = source(ORIGINAL, CASE), source(ORIGINAL, COPY)
    case = (ROOT / CASE).read_text(encoding="utf-8-sig")
    copy = (ROOT / COPY).read_text(encoding="utf-8-sig")
    for path in (CASE, COPY):
        assert git("rev-parse", f"{BASE}:{path}") == git("rev-parse", f"{ORIGINAL}:{path}"), "Baseline lost original pair"
    for path, sha in (("docs/design/m1-storefront-discovery-content.md", SEO),
                      ("docs/design/m1-storefront-information-architecture.md", IA),
                      ("research-evidence/g2-02-storefront/content-requests.md", IA)):
        assert git("rev-parse", f"{BASE}:{path}") == git("rev-parse", f"{sha}:{path}")
    assert "**ORI-CASE-1.1**" in case and "**ORI-COPY-1.1**" in copy and "**ORI-CASE-1.1**" in copy
    for start, end in (("\n## 2.", "\n## 4."),
                       ("\n### Dish source strings", "\n## 5."),
                       ("\n## 5.", "\n## 7.")):
        assert between(case, start, end) == between(old_case, start, end), f"Factual region changed: {start}"
    assert records(case, "ORI-ASSET-") == records(old_case, "ORI-ASSET-")

    old_categories, categories = records(old_case, "ORI-MENU-C"), records(case, "ORI-MENU-C")
    jumps = ["Para compartir", "Platos", "Postres", "Bebidas"]
    assert len(categories) == 4
    for n, jump in enumerate(jumps, 1):
        key = f"ORI-MENU-C{n:02d}"
        row = categories[key]
        assert row[2] == jump and row[:2] + row[3:] == old_categories[key], "Category facts/identity changed"
        assert f"{row[1]} → {jump}" in copy

    old_scenarios, scenarios = records(old_case, "ORI-SCENARIO-"), records(case, "ORI-SCENARIO-")
    assert set(scenarios) == set(old_scenarios) and len(scenarios) == 11
    for key, row in scenarios.items():
        old = old_scenarios[key]
        assert row[1] == old[1], f"Scenario input changed: {key}"
        if key != "ORI-SCENARIO-06":
            assert row == old, f"Unrelated scenario changed: {key}"
    assert scenarios["ORI-SCENARIO-06"][0].endswith("/ 2")
    full_date = "domingo 4 de octubre de 2026, 13:30–15:30."
    assert full_date in scenarios["ORI-SCENARIO-06"][2] and full_date in copy

    old_ids, copy_ids = records(old_copy, "ORI-COPY-"), records(copy, "ORI-COPY-")
    assert len(old_ids) == 83 and set(old_ids) <= set(copy_ids)
    revised_ids = {k for k in old_ids if old_ids[k] != copy_ids[k]}
    expected_revised = {"ORI-COPY-H02-07", "ORI-COPY-M01-03", "ORI-COPY-S10",
                        "ORI-COPY-S11", "ORI-COPY-S14", "ORI-COPY-S18"}
    assert revised_ids == expected_revised, f"Unexpected changed strings: {revised_ids}"
    new_ids = set(copy_ids) - set(old_ids)
    expected_new = {"ORI-COPY-H03-09"} | {f"ORI-COPY-E{n:02d}" for n in range(1, 4)} | {f"ORI-COPY-META-{n:02d}" for n in range(1, 8)}
    assert new_ids == expected_new and len(copy_ids) == 94
    assert len([key for key in copy_ids if re.fullmatch(r"ORI-COPY-S\d{2}", key)]) == 30
    assert copy_ids["ORI-COPY-H03-01"] == old_ids["ORI-COPY-H03-01"]
    assert "La historia de ORILLA" in copy_ids["ORI-COPY-H03-09"][1]
    for n in range(1, 8):
        row = copy_ids[f"ORI-COPY-META-{n:02d}"]
        assert "ficticio" in row[1].lower() and "ficticio" in row[2].lower(), "Standalone metadata lost fiction"
        assert not re.search(r"\d+,\d{2} €", row[1] + row[2]), "Default metadata introduced price claim"
    assert "{nombre_actual_del_plato_o_variante}" in copy_ids["ORI-COPY-META-03"][1]
    assert "ORI-FICTION" in copy_ids["ORI-COPY-E03"][1] and "ORI-FOOD-NOTICE" in copy_ids["ORI-COPY-E03"][1]
    assert "ORI-COPY-S27" not in " ".join(sum(records(copy, "ORI-COPY-META-").values(), []))
    assert "ORILLA · Cocina mediterránea en Alcoy | Demo" not in copy
    assert set(re.findall(r"\d+,\d{2} €", copy)) <= set(re.findall(r"\d+,\d{2} €", case))
    assert "16,00 € / persona · Mínimo 2 personas." in copy
    assert "Media ración · 9,50 € / Ración · 15,00 €" in copy

    resolution = (HERE / "resolutions.md").read_text(encoding="utf-8-sig")
    outcomes = records(between(resolution, "\n## R01–R08", "\n## Preserved requests"), "SEO-R")
    assert len(outcomes) == 8 and all(row[1] == "Accepted" for row in outcomes.values())
    assert set(outcomes) == {f"SEO-R{n:02d}" for n in range(1, 9)}
    assert "pending" in copy.lower() and "re-reading" in copy.lower()

    preserved = sorted(set(legacy.SOURCES + legacy.ASSETS + tree("docs/adr") + tree(LEGACY)
                           + tree("research-evidence/seo-storefront")
                           + tree("research-evidence/reviews/orilla-seo-0c17480")
                           + tree("research-evidence/reviews/orilla-content-5bd3184")
                           + ["docs/design/m1-storefront-discovery-content.md"]))
    manifest_sources = []
    for path in preserved:
        blob = git("rev-parse", f"{BASE}:{path}").decode().strip()
        assert git("hash-object", "--path", path, path).decode().strip() == blob, f"Source/legacy changed: {path}"
        manifest_sources.append({"path": path, "baseline_git_blob": blob,
                                 "baseline_sha256": legacy.sha256(git("show", f"{BASE}:{path}"))})

    docs = [ROOT / CASE, ROOT / COPY] + sorted(HERE.glob("*.md"))
    generated = {HERE / "checks.json", HERE / "source-manifest.json"}
    local_links, tables = 0, 0
    for path in docs:
        body = path.read_text(encoding="utf-8-sig")
        assert not re.search(r"^(<<<<<<<|=======|>>>>>>>)", body, re.M)
        assert body.count("```") % 2 == 0
        width = None
        for line in body.splitlines():
            if line.startswith("|"):
                cells = len(line.strip().strip("|").split("|"))
                if width is None:
                    width, tables = cells, tables + 1
                assert cells == width, f"Table width: {path}: {line}"
            else:
                width = None
        for target in re.findall(r"\[[^\]]+\]\(([^\)]+)\)", body):
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("//"):
                continue
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            assert dest.is_relative_to(ROOT) and (dest.exists() or (dest in generated and not parsed.fragment)), f"Missing local link: {path}: {target}"
            if parsed.fragment:
                assert unquote(parsed.fragment) in legacy.anchors(dest), f"Missing anchor: {target}"
            local_links += 1

    manifest = {"operating_baseline": BASE, "reviewed_pair_1_0": ORIGINAL, "received_seo": SEO,
                "frozen_architecture": IA, "preserved_sources": manifest_sources,
                "skills": [{"path": str(p), "sha256": legacy.sha256(p.read_bytes()), "status": "same main skill reused"} for p in legacy.SKILLS],
                "reading_scope": "New full review/receipts/index; reuse previous complete readings plus changed operating text, as README records.",
                "deliverables_1_1": [{"path": p, "sha256": legacy.sha256((ROOT / p).read_bytes()),
                                      "working_git_blob": git("hash-object", "--path", p, p).decode().strip()} for p in (CASE, COPY)]}
    checks = {"status": "passed", "scope": "author documentary preservation/coherence, no product tests",
              "operating_baseline": BASE, "branch": BRANCH, "received_seo": SEO,
              "source_records_preserved": len(preserved), "original_evidence_files_preserved": len(tree(LEGACY)),
              "original_copy_ids_preserved": len(old_ids), "copy_ids_1_1": len(copy_ids),
              "revised_copy_ids": sorted(revised_ids), "new_copy_ids": sorted(new_ids),
              "state_ids": 30, "scenarios": 11, "scenario_wording_revision": "ORI-SCENARIO-06 / 2; input facts unchanged",
              "unchanged": ["story/people/place", "dishes/offers/variants/prices", "visit/food", "asset rows", "scenario inputs", "foreign/1.0 evidence"],
              "recommendations_resolved_by_author": sorted(outcomes), "local_links": local_links, "tables": tables,
              "not_checked": ["SEO re-reading of 1.1", "architecture adoption", "UI/phone/accessibility", "translations/food", "runtime/metadata/preview/indexing/policies", "G4/participants"]}
    for name, data in (("checks.json", checks), ("source-manifest.json", manifest)):
        (HERE / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    assert all(path.exists() for path in generated)
    print(json.dumps(checks, ensure_ascii=False))


if __name__ == "__main__":
    main()
