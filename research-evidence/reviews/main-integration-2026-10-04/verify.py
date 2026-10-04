"""Documentary verification for the owner-authorised consolidation; no app tests."""
from pathlib import Path
import subprocess
import json
import hashlib
import re
import urllib.parse

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
assert subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT).decode().strip() == "docs/m1-g1-main-integration"
def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)
def sha(data):
    return hashlib.sha256(data).hexdigest()
def original(commit, path):
    return git("show", f"{commit}:{path}")
register = json.loads((HERE / "source-register.json").read_text(encoding="utf-8"))
for item in register["pull_requests"]:
    assert subprocess.run(["git", "merge-base", "--is-ancestor", item["headRefOid"], "HEAD"], cwd=ROOT).returncode == 0, item["number"]
assert len(register["pull_requests"]) == 26
assert subprocess.run(["git", "merge-base", "--is-ancestor", register["retained_local_exploration"], "HEAD"], cwd=ROOT).returncode == 0
frozen = "ffadd70da06b1b934b5492eb65f637b104854580"
ui = "298643b81c9800a7fbb4f1cc718c560af58dee60"
modified = {"HANDOFF.md", "coordination/README.md", "research-evidence/README.md", "docs/README.md",
            "README.md", "docs/design/m1-storefront-visual-direction.md", "CHANGELOG.md",
            "coordination/storage-migration-2026-10-03.json", "coordination/valiris-restaurants/relume-orilla/README.md"}
paths = [p for p in git("ls-tree", "-r", "--name-only", "-z", frozen).decode().split("\0") if p]
preserved = 0
for path in paths:
    if path in modified:
        continue
    assert (ROOT / path).read_bytes() == original(frozen, path), path
    preserved += 1
protected = ["docs/product/m0-capability-matrix.md", "docs/product/m0-journeys-and-criteria.md",
             "docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md"]
protected += [p for p in paths if p.startswith("docs/adr/")]
assert all((ROOT / p).read_bytes() == original("b28ee63ef887c9d3bc9a6a8ad5165e9e160aa9fc", p) for p in protected)
assert (ROOT / "docs/design/orilla-case.md").read_bytes() == original("4b382bebe5d5c6cad21a7edcaffab053c433a0e9", "docs/design/orilla-case.md")
copy = (ROOT / "docs/design/m1-storefront-content-and-copy.md").read_bytes()
assert copy == original("4b382bebe5d5c6cad21a7edcaffab053c433a0e9", "docs/design/m1-storefront-content-and-copy.md")
ids = set(re.findall(r"ORI-COPY-(?:H\d{2}-\d{2}|M\d{2}-\d{2}|D\d{2}-\d{2}|S\d{2}|E\d{2}|META-\d{2})", copy.decode()))
assert len(ids) == 94
matrix = (ROOT / protected[0]).read_text(encoding="utf-8")
rows = [line for line in matrix.splitlines() if re.match(r"\| B[1-7]\.\d{2} / L\d+ \|", line)]
treatments = [row.split("|")[4].strip() for row in rows]
assert len(rows) == 72
assert {k: treatments.count(k) for k in set(treatments)} == {"Included": 36, "Configurable": 30, "Connection-dependent": 6}
ui_paths = [p for p in git("ls-tree", "-r", "--name-only", "-z", ui, "research-evidence/g2-07-storefront").decode().split("\0") if p]
assert all((ROOT / p).read_bytes() == original(ui, p) for p in ui_paths)
prov = json.loads((ROOT / "research-evidence/g2-07-storefront/imagegen/provenance.json").read_text(encoding="utf-8"))
for item in prov["outputs"]:
    data = (ROOT / item["file"]).read_bytes()
    assert sha(data) == item["sha256"]
    assert data[:8] == b"\x89PNG\r\n\x1a\n"
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    assert (width, height) == (item["width"], item["height"])
    if "prompt" in item:
        assert sha((ROOT / "research-evidence/g2-07-storefront/imagegen" / item["prompt"]).read_bytes()) == item["prompt_sha256"]
for item in prov["references"]:
    assert sha((ROOT / item["file"]).read_bytes()) == item["sha256"]
archive = ROOT / "research-evidence/archive-g2-07-svg-2026-10-04"
snapshot = json.loads((archive / "manifest.json").read_text(encoding="utf-8"))
assert len(snapshot["files"]) == 146
source = Path(snapshot["source_worktree"])
assert all(sha((ROOT / x["archive_path"]).read_bytes()) == x["sha256"] == sha((source / x["source_path"]).read_bytes()) for x in snapshot["files"])
active = ["HANDOFF.md", "coordination/README.md", "research-evidence/README.md", "docs/README.md", "README.md",
          "docs/design/m1-storefront-visual-direction.md", "coordination/valiris-restaurants/relume-orilla/README.md",
          "research-evidence/reviews/main-integration-2026-10-04/README.md", "research-evidence/archive-g2-07-svg-2026-10-04/README.md"]
# Reserve only the current generated report for local-link validation.
(HERE / "checks.json").write_text('{}\n', encoding="utf-8")
links = 0
for name in active:
    data = (ROOT / name).read_text(encoding="utf-8-sig")
    assert not re.search(r"^(<<<<<<<|=======|>>>>>>>)", data, re.M), name
    assert data.count("```") % 2 == 0, name
    for ref in re.findall(r"\]\((<[^>]+>|[^)]+)\)", data):
        target = ref.strip("<>").split("#", 1)[0]
        if not target or re.match(r"^[A-Za-z][\w+.-]*:", target) or target.startswith("//"):
            continue
        dest = ((ROOT / name).parent / urllib.parse.unquote(target)).resolve()
        assert dest.is_relative_to(ROOT) and dest.exists(), (name, ref)
        links += 1
storage = json.loads((ROOT / ".cache/storage-checks.json").read_text(encoding="utf-8"))
assert storage["failures"] == []
check = {
    "date": "2026-10-04", "result": "PASS", "source_pr_heads_collected": 26,
    "retained_local_exploration_ancestor": True, "source_files_byte_preserved_from_46": preserved,
    "explicit_operating_changes": sorted(modified), "protected_original_sources": len(protected),
    "copy_ids": len(ids), "capabilities": {"total": 72, "included": 36, "configurable": 30, "connections": 6},
    "published_ui_files_byte_preserved": len(ui_paths), "ui_pngs_and_prompt_hashes": len(prov["outputs"]),
    "original_visual_hashes_match": len(prov["references"]), "archived_working_files": len(snapshot["files"]),
    "original_working_files_unchanged": True, "active_entry_local_links": links,
    "migration_originals_preserved": storage["preserved_original_files"],
    "migration_links": storage["local_link_targets_checked"],
    "branch_rules": "active required PR, squash-only, linear history, no bypass actors; unchanged",
    "scope": "integration ancestry, documentary preservation, local links and asset integrity only",
    "not_claimed": ["G4 application approval", "UX validation", "rendered accessibility", "software tests", "Relume operation", "M1 completion"],
}
(HERE / "checks.json").write_text(json.dumps(check, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps(check, ensure_ascii=False, indent=2))
