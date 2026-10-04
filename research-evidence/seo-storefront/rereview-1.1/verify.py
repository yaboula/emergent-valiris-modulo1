"""Check this bounded documentary continuation; write only its new evidence.

No old or other-owner verifier is run. Python 3.10+; no dependencies/network.
"""

import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
BASE = "56306793d54bb8df74305134ec6284c6d647eebf"
OLD_REVIEW = "0c17480bdc2b6ff8037022228ebc4599a704e702"
OLD_CONTENT = "5bd3184ca48be8d579e3f82d3361dbf5de0ed228"
CONTENT = "4b382bebe5d5c6cad21a7edcaffab053c433a0e9"
EVIDENCE = "d9ef8c9bc90f77de8d38dd14b1664d8384d4dea4"
ARCH = "ba44c6809516d8d078d192f5f6a423b12cd8b673"
LATER = "70512d7a3d1afcd7f3aa0c9823a4d6e7b08dde8c"
LATER_PATH = "research-evidence/g2-02-storefront/content-1-1-adoption.md"
BRANCH = "docs/m1-seo-orilla-1-1-review"
DOC = "docs/design/m1-storefront-discovery-content.md"
CASE = "docs/design/orilla-case.md"
COPY = "docs/design/m1-storefront-content-and-copy.md"
IA = "docs/design/m1-storefront-information-architecture.md"
REVISED = {"ORI-COPY-H02-07", "ORI-COPY-M01-03", "ORI-COPY-S10", "ORI-COPY-S11", "ORI-COPY-S14", "ORI-COPY-S18"}
ADDED = {"ORI-COPY-H03-09", *[f"ORI-COPY-E{n:02}" for n in range(1, 4)],
         *[f"ORI-COPY-META-{n:02}" for n in range(1, 8)]}
FROZEN = {
    CASE: (CONTENT, "ad0f42fc461396e1d28191c667b077c060195a38"),
    COPY: (CONTENT, "d570c699455169c4d27c2fe8fc384250ce47fbd7"),
    IA: (ARCH, "297d25f2869970b268bc1e8671bd0cbe74c477fd"),
}


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT).decode("utf-8").replace("\r\n", "\n")


def blob(ref, path):
    return git("rev-parse", f"{ref}:{path}").strip()


def source(ref, path):
    return git("show", f"{ref}:{path}")


def rows(text):
    return {m.group(1): m.group(0) for m in re.finditer(r"^\|\s*(ORI-[A-Z0-9-]+)\s*[/|][^\n]*$", text, re.M)}


def cells(row):
    return [cell.strip() for cell in row.strip("|").split("|")]


def owned(path):
    return path == DOC or path.startswith("research-evidence/seo-storefront/rereview-1.1/")


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


checks = []


def check(name, valid, detail):
    checks.append({"check": name, "status": "pass" if valid else "fail", "detail": detail})


check("isolated_assignment", git("branch", "--show-current").strip() == BRANCH,
      {"branch": git("branch", "--show-current").strip(), "root": git("rev-parse", "--show-toplevel").strip()})
source_records = []
for path, (ref, expected) in FROZEN.items():
    refs = [ref, BASE, "HEAD"] + ([EVIDENCE] if ref == CONTENT else [])
    actual = {revision: blob(revision, path) for revision in dict.fromkeys(refs)}
    valid = all(value == expected for value in actual.values()) and not git("diff", "--name-only", "HEAD", "--", path).strip()
    check(f"frozen_source:{path}", valid, actual)
    source_records.append({"path": path, "reviewed_sha": ref, "blob": expected, "verified_at": actual})

old_evidence = git("ls-tree", "-r", "--name-only", OLD_REVIEW, "--", "research-evidence/seo-storefront/").splitlines()
preserved = {path: blob(OLD_REVIEW, path) for path in old_evidence}
check("six_historical_evidence_files", len(old_evidence) == 6 and all(
    blob(BASE, path) == expected == blob("HEAD", path)
    and not git("diff", "--name-only", "HEAD", "--", path).strip()
    for path, expected in preserved.items()), preserved)

current_doc = (ROOT / DOC).read_text(encoding="utf-8")
old_doc = source(OLD_REVIEW, DOC)
historical_body = current_doc.split("## Historical review 1.0\n\n", 1)[1].split(
    "\n## Scoped outcomes — CASE/COPY 1.1 and IA v0.3\n", 1)[0]
check("original_review_body", historical_body == old_doc.split("\n\n", 1)[1],
      "Original 1.0 body retained; separate current pointer/outcomes added.")

old_copy = {key: row for key, row in rows(source(OLD_CONTENT, COPY)).items() if key.startswith("ORI-COPY-")}
new_copy = {key: row for key, row in rows(source(CONTENT, COPY)).items() if key.startswith("ORI-COPY-")}
changed_ids = {key for key in old_copy.keys() & new_copy.keys() if old_copy[key] != new_copy[key]}
added_ids, removed_ids = set(new_copy) - set(old_copy), set(old_copy) - set(new_copy)
check("exact_affected_copy_rows", len(old_copy) == 83 and len(new_copy) == 94
      and changed_ids == REVISED and added_ids == ADDED and not removed_ids,
      {"old_count": len(old_copy), "new_count": len(new_copy), "revised": sorted(changed_ids),
       "added": sorted(added_ids), "removed": sorted(removed_ids)})

old_case, new_case = rows(source(OLD_CONTENT, CASE)), rows(source(CONTENT, CASE))
category_errors = []
for n, jump in enumerate(("Para compartir", "Platos", "Postres", "Bebidas"), 1):
    key = f"ORI-MENU-C{n:02}"
    before, after = cells(old_case[key]), cells(new_case[key])
    if after[1] != before[1] or after[2] != jump or after[-1] != before[-1]:
        category_errors.append(key)
check("category_mapping_and_membership", not category_errors, category_errors or "Same four IDs/full headings/memberships; mapped compact jumps.")
before, after = cells(old_case["ORI-SCENARIO-06"]), cells(new_case["ORI-SCENARIO-06"])
check("exception_revision_and_same_input", after[0].endswith("/ 2") and before[1] == after[1]
      and "domingo 4 de octubre de 2026, 13:30–15:30" in after[2],
      "Revision 2 dates the same kitchen-service input; no local-hours change.")
retained = [key for key in old_case if key.startswith(("ORI-DISH-", "ORI-MENU-P", "ORI-FOOD-", "ORI-VISIT-"))]
check("retained_offer_recipe_visit_rows", all(new_case[key] == old_case[key] for key in retained),
      {"rows_compared": len(retained), "scope": "Mechanical preservation of relevant retained records, not a new factual audit."})
metadata_ids = [f"ORI-COPY-META-{n:02}" for n in range(1, 8)]
check("independent_fiction_in_metadata", all("ficticio" in cells(new_copy[key])[1].lower()
      and "ficticio" in cells(new_copy[key])[2].lower() for key in metadata_ids), metadata_ids)

read_records = {}
for path in (
    "HANDOFF.md", "coordination/README.md", "coordination/valiris-restaurants/SEO_Estrategia_Contenido_Prompt.md",
    "research-evidence/reviews/orilla-joint-4b382be-ba44c68/g1-review.md",
    "research-evidence/g2-04-storefront/seo-consolidation-1.1/resolutions.md",
    "research-evidence/g2-04-storefront/seo-consolidation-1.1/author-review.md",
    "research-evidence/g2-04-storefront/seo-consolidation-1.1/delivery.md",
    "research-evidence/g2-02-storefront/adoption.md", "research-evidence/g2-02-storefront/content-requests.md",
    "research-evidence/g2-02-storefront/content-adoption-contrasts.md",
):
    read_records[path] = {"sha": BASE, "blob": blob(BASE, path),
                          "scope": "Current operating changes or complete received resolution/return; affected IA destination/relations sections."}
old_manifest = json.loads(source(OLD_REVIEW, "research-evidence/seo-storefront/source-manifest.json"))
reused = {}
for record in old_manifest["sources"]:
    path = record["path"]
    if path.startswith(("AGENTS", "CONTRIBUTING", "coordination/valiris-restaurants/Valiris_", "docs/product/", "docs/project/", "docs/adr/", "docs/research/")) or path in (
        "docs/design/m1-public-presence-and-discovery.md", "docs/design/m1-connected-journey.md",
        "docs/design/m1-coverage-and-evidence.md", "docs/design/valiris-restaurants-brand-refinement.md",
        "research-evidence/g2-06-restaurants-brand/refinement/selected-three-references-2026-10-03.es.md",
    ):
        reused[path] = {"original_blob": blob(OLD_REVIEW, path), "baseline_blob": blob(BASE, path),
                        "read_scope_reused": record.get("read_scope", record.get("scope"))}
check("unchanged_common_readings", all(row["original_blob"] == row["baseline_blob"] for row in reused.values()),
      {"reused_records": len(reused), "not_refreshed": "Historical reads reused only where their blobs match."})
later_return = source(LATER, LATER_PATH)
check("later_owner_return_provenance", CONTENT in later_return and "IA v0.4" in later_return,
      {"sha": LATER, "path": LATER_PATH, "blob": blob(LATER, LATER_PATH),
       "scope": "Owner adoption declaration only; not a new IA v0.4 SEO comparison or verifier reproduction."})
write_json(OUT / "source-manifest.json", {
    "checked_on": "2026-10-04", "baseline": BASE, "base_branch": "docs/m1-g1-orilla-joint-handoff", "base_pr": 41,
    "branch": BRANCH, "original_review_sha": OLD_REVIEW, "content_pair_sha": CONTENT,
    "architecture_sha": ARCH, "architecture_consumed_pair_sha": OLD_CONTENT,
    "frozen_sources": source_records, "historical_evidence_blobs": preserved,
    "original_review_blob": blob(OLD_REVIEW, DOC), "read_records": read_records, "reused_common_readings": reused,
    "affected_copy_rows": {"revised": sorted(changed_ids), "added": sorted(added_ids)},
    "later_parallel_return": {"pr": 42, "sha": LATER, "path": LATER_PATH, "blob": blob(LATER, LATER_PATH),
                              "read_scope": "Full adoption declaration; applied SEO findings remain frozen on IA v0.3."},
    "source_evidence_reuse": "Eight official primary pages retained byte-for-byte from #37; no new technical rule or external retrieval claimed.",
    "limits": "Scoped documentary comparison on IA v0.3; later G2.02 v0.4 adoption declared separately. G1 consolidation and composition, behaviour, linguistic/technical and independent review remain pending.",
})
write_json(OUT / "checks.json", {})

md_files = [ROOT / DOC, *sorted(OUT.glob("*.md"))]
texts = {path: path.read_text(encoding="utf-8") for path in md_files}
review = texts[OUT / "review.md"]
recs = re.findall(r"^\| (SEO-R\d{2}) /", review, re.M)
check("per_recommendation_results", recs == [f"SEO-R{n:02}" for n in range(1, 10)], recs)
contrast_ids = re.findall(r"^\| (RR11-C\d{2}) /", review, re.M)
check("twelve_affected_use_contrasts", contrast_ids == [f"RR11-C{n:02}" for n in range(1, 13)], contrast_ids)
check("every_affected_id_cited", REVISED | ADDED <= set(re.findall(r"ORI-COPY-[A-Z0-9-]+", review)),
      {"revised": 6, "new": 11})
id_pattern = r"\b(?:ORI|IA)-[A-Z0-9]+(?:-[A-Z0-9]+)*\b"
valid_ids = set(re.findall(id_pattern, source(CONTENT, CASE) + source(CONTENT, COPY) + source(ARCH, IA)
                           + source(OLD_CONTENT, CASE) + source(OLD_CONTENT, COPY)))
used_ids = set(re.findall(id_pattern, "\n".join(texts.values())))
check("valid_frozen_source_ids", used_ids <= valid_ids,
      {"unique_cited": len(used_ids), "unmatched": sorted(used_ids - valid_ids)})


def heading_slugs(text):
    result, counts, in_fence = set(), {}, False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match and not in_fence:
            slug = re.sub(r"[^\w\- ]", "", re.sub(r"[`*_]", "", match.group(1)).lower()).replace(" ", "-")
            index = counts.get(slug, 0)
            counts[slug] = index + 1
            result.add(slug if not index else f"{slug}-{index}")
    return result


link_errors, link_count, table_errors, table_count = [], 0, [], 0
for path, text in texts.items():
    for target in re.findall(r"(?<!!)\[[^\]\n]+\]\(([^)]+)\)", text):
        parts = urlsplit(target)
        if parts.scheme or target.startswith("//"):
            continue
        link_count += 1
        destination = (path.parent / unquote(parts.path)).resolve() if parts.path else path
        if not destination.is_relative_to(ROOT) or not destination.is_file():
            link_errors.append(f"{path.relative_to(ROOT)} -> {target}")
        elif parts.fragment and unquote(parts.fragment) not in heading_slugs(destination.read_text(encoding="utf-8")):
            link_errors.append(f"{path.relative_to(ROOT)} -> missing #{parts.fragment}")
    width = None
    for number, line in enumerate(text.splitlines(), 1):
        if line.startswith("|"):
            current_width = len(re.split(r"(?<!\\)\|", line)) - 2
            if width is None:
                width = current_width
                table_count += 1
            if current_width != width:
                table_errors.append(f"{path.relative_to(ROOT)}:{number}")
        else:
            width = None
check("local_links_and_fragments", not link_errors, {"checked": link_count, "errors": link_errors})
check("markdown_tables", not table_errors, {"tables": table_count, "errors": table_errors})
changed_paths = set(git("diff", "--name-only", BASE).splitlines()) | set(git("ls-files", "--others", "--exclude-standard").splitlines())
check("owned_new_paths_only", all(owned(path) for path in changed_paths), sorted(changed_paths))
diff = subprocess.run(["git", "diff", "--check", BASE], cwd=ROOT, text=True, capture_output=True)
check("git_diff_check", diff.returncode == 0, diff.stdout + diff.stderr or "clean")
report = {"checked_on": "2026-10-04", "baseline": BASE, "status": "pass" if all(row["status"] == "pass" for row in checks) else "fail",
          "scope": "Author documentary checks; twelve manual affected-use contrasts in review.md; no rendered/runtime/G4/participant validation.",
          "checks": checks, "pending": ["G1 receipt/consolidation of the parallel returns", "Any further IA v0.4 comparison assigned by G1", "Applied PC/phone and behaviour review", "Linguistic/technical and independent G4 application review"]}
write_json(OUT / "checks.json", report)
print(json.dumps({"status": report["status"], "checks": len(checks),
                  "failed": [row for row in checks if row["status"] == "fail"]}, ensure_ascii=False, indent=2))
raise SystemExit(0 if report["status"] == "pass" else 1)
