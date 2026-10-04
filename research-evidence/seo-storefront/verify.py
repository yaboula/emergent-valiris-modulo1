"""Verify documentary integrity; do not run or simulate product behaviour.

Run from any directory with Python 3. Writes only this owner's manifest/report.
Uses frozen Git sources, not a moving branch or another owner's verifier.
"""

import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research-evidence/seo-storefront"
BASE = "81f72e68aac5b6fd92a3511ac684edc288f739cc"
CONTENT = "5bd3184ca48be8d579e3f82d3361dbf5de0ed228"
EVIDENCE = "6ce8634e98da3d975a376a265de77b940ed22f37"
ARCH = "ff8fc061dfb4e63461ee2b77b5a18f02108edb6b"
BRANCH = "docs/m1-seo-orilla-content-review"
REVIEW = "docs/design/m1-storefront-discovery-content.md"
EXPECTED = {
    "docs/design/orilla-case.md": (CONTENT, "bade7126a2d4222227095a1f8e9fa6ae85c5c687"),
    "docs/design/m1-storefront-content-and-copy.md": (CONTENT, "bfc11eba8d86c2192e0c4fef766bf2728d7d15cf"),
    "docs/design/m1-storefront-information-architecture.md": (ARCH, "8c8a56aa5ce22def06f659398ad9900bce7a78bf"),
}
READ_SCOPES = {
    "AGENTS.md": "Full common instructions; own-checkout authority.",
    "CONTRIBUTING.md": "Full workflow; stacked dependency and author rules.",
    "HANDOFF.md": "Current operating entry, dependencies and checkpoints; historical handoffs retained, not re-audited.",
    "coordination/README.md": "Current operating index and SEO handoff.",
    "coordination/valiris-restaurants/SEO_Estrategia_Contenido_Prompt.md": "Full current specialty contract, including later ORILLA CASE/COPY handoff.",
    "coordination/valiris-restaurants/Valiris_G2_Brief_Arranque_Diseno.md": "Common current brief and adaptive/content decisions.",
    "coordination/valiris-restaurants/Valiris_Contexto_Comun_Agentes.md": "Full shared context.",
    "coordination/valiris-restaurants/Valiris_Organizacion_Protocolo_Agentes.md": "Shared protocol and responsibilities; current later decisions override historical preparation.",
    "docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md": "Full functional definition; later launch decisions preserved.",
    "docs/project/roadmap.md": "Full roadmap; M1 design versus M2 preparation and later implementation.",
    "docs/product/m1-design-briefs.md": "Both M1 briefs; accepted capabilities and factual/public/private/language criteria.",
    "docs/adr/0005-repository-and-product-language.md": "Full language ADR; English repository documents, Spanish-first UI, guest-language and RTL preparation obligations preserved.",
    "docs/design/m1-public-presence-and-discovery.md": "Public structure, PV-P tasks, walkthroughs and contrasts; applicable operator-maintenance links.",
    "docs/design/m1-connected-journey.md": "Applicable shared public C1-C3 rules, direct/menu/detail entries and public change/recovery contrasts; operator history not re-audited.",
    "docs/design/m1-coverage-and-evidence.md": "Coverage purpose, CG01-CG12 gaps and next-assignment checkpoints; no repeated audit of all capability rows.",
    "docs/project/valiris-restaurants-brand-foundation-brief.md": "Current scoped brand direction and ownership; no new visual selection.",
    "docs/design/valiris-restaurants-brand-refinement.md": "Current selected direction and application constraints; no rendered visual audit.",
    "research-evidence/g2-06-restaurants-brand/refinement/selected-three-references-2026-10-03.es.md": "Exact selected-reference record; existing image assets not re-audited.",
    "research-evidence/reviews/orilla-content-5bd3184/g1-review.md": "Full content receipt and limits.",
    "research-evidence/g2-04-storefront/delivery.md": "Full author delivery and source pair.",
    "research-evidence/g2-04-storefront/author-review.md": "Author contrasts and pending cross-specialist review; specialty questions remain in K section 7.",
    "research-evidence/g2-02-storefront/content-requests.md": "Architecture requests including full XR02.",
}


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT).decode("utf-8").strip()


def blob(ref, path):
    return git("rev-parse", f"{ref}:{path}")


def permitted(path):
    return path == REVIEW or path.startswith("research-evidence/seo-storefront/")


def slugs(text):
    result, counts = set(), {}
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match and not in_fence:
            label = re.sub(r"[`*_]", "", match.group(1)).lower()
            slug = re.sub(r"[^\w\- ]", "", label).replace(" ", "-")
            index = counts.get(slug, 0)
            counts[slug] = index + 1
            result.add(slug if not index else f"{slug}-{index}")
    return result


checks = []


def check(name, valid, detail):
    checks.append({"check": name, "status": "pass" if valid else "fail", "detail": detail})


check("isolated_branch", git("branch", "--show-current") == BRANCH,
      {"expected": BRANCH, "actual": git("branch", "--show-current")})
source_records, source_texts = [], []
for path, (ref, expected) in EXPECTED.items():
    refs = [ref, BASE, "HEAD"] + ([EVIDENCE] if ref == CONTENT else [])
    found = {revision: blob(revision, path) for revision in dict.fromkeys(refs)}
    check(f"preserved_blob:{path}", all(value == expected for value in found.values()), found)
    # Comparing the working file through Git catches edits despite checkout EOL conversion.
    changed = git("diff", "--name-only", "HEAD", "--", path)
    check(f"unchanged_working_source:{path}", not changed, changed or "unchanged")
    source_records.append({"path": path, "reviewed_sha": ref, "expected_blob": expected,
                           "verified_at": found, "scope": "Full paired case/copy or architecture review."})
    source_texts.append(git("show", f"{ref}:{path}"))

for path, scope in READ_SCOPES.items():
    source_records.append({"path": path, "baseline_sha": BASE,
                           "baseline_blob": blob(BASE, path), "read_scope": scope})

manifest = {
    "consulted_on": "2026-10-04", "operating_baseline": BASE,
    "published_base_branch": "docs/m1-g1-orilla-content-handoff", "base_pr": 36,
    "own_branch": BRANCH,
    "base_remote_check": "Matched 81f72e68aac5b6fd92a3511ac684edc288f739cc before creation and editing; manually observed with git ls-remote.",
    "sources": source_records,
    "official_source_method": "Web tool reads of official pages on 2026-10-04; URLs/excerpts/scope in primary-sources.md, no site crawl or raw-page reproduction.",
    "review_limits": "Author documentary review, not acceptance, rendered inspection, implementation testing or independent review.",
}
(OUT / "source-manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
# Ensure the report target exists for local-link verification on the first run.
report_path = OUT / "checks.json"
report_path.write_text("{}\n", encoding="utf-8", newline="\n")

md_files = [ROOT / REVIEW, *sorted(OUT.glob("*.md"))]
texts = {path: path.read_text(encoding="utf-8") for path in md_files}
review = texts[ROOT / REVIEW]
expected_requests = ["XR02", *[f"ORI-SEO-Q{n:02}" for n in range(1, 6)]]
check("six_request_answers", all(f"| {request} |" in review for request in expected_requests), expected_requests)
rec_ids = re.findall(r"^### (SEO-R\d{2})$", review, re.M)
check("recommendation_records", rec_ids == [f"SEO-R{n:02}" for n in range(1, 13)], rec_ids)
field_errors = []
for section in re.split(r"^### SEO-R\d{2}\s*$", review, flags=re.M)[1:]:
    section = section.split("\n## ", 1)[0]
    for required in ("**Location/source:**", "**Objective/reason:**", "**Editorial proposal:**",
                     "**Evidence/certainty:**", "**Technical effect/owner/resolution:**",
                     "5bd3184", "ff8fc061", "Pending"):
        if required not in section:
            field_errors.append(required)
check("recommendation_fields_and_pending_status", not field_errors, field_errors)
tech_ids = re.findall(r"^\| (SEO-T\d{2}) \|", review, re.M)
check("technical_questions", tech_ids == [f"SEO-T{n:02}" for n in range(1, 9)], tech_ids)
contrasts = texts[OUT / "documentary-contrasts.md"]
contrast_ids = re.findall(r"^\| (DC\d{2}) —", contrasts, re.M)
check("documentary_contrasts", contrast_ids == [f"DC{n:02}" for n in range(1, 15)], contrast_ids)

id_pattern = r"\b(?:ORI|IA)-[A-Z0-9]+(?:-[A-Z0-9]+)*\b"
valid_ids = set(re.findall(id_pattern, "\n".join(source_texts)))
cited_ids = set(re.findall(id_pattern, "\n".join(texts.values())))
check("exact_frozen_source_ids", cited_ids <= valid_ids,
      {"cited_unique": len(cited_ids), "unmatched": sorted(cited_ids - valid_ids)})

link_errors, links_checked, table_errors, tables_checked = [], 0, [], 0
for path, text in texts.items():
    for target in re.findall(r"(?<!!)\[[^\]\n]+\]\(([^)]+)\)", text):
        parts = urlsplit(target)
        if parts.scheme or target.startswith("//"):
            continue
        links_checked += 1
        destination = (path.parent / unquote(parts.path)).resolve() if parts.path else path
        if not destination.is_relative_to(ROOT) or not destination.is_file():
            link_errors.append(f"{path.relative_to(ROOT)} -> {target}")
        elif parts.fragment and unquote(parts.fragment) not in slugs(destination.read_text(encoding="utf-8")):
            link_errors.append(f"{path.relative_to(ROOT)} -> missing #{parts.fragment}")
    expected_width = None
    for number, line in enumerate(text.splitlines(), 1):
        if line.startswith("|"):
            width = len(re.split(r"(?<!\\)\|", line)) - 2
            if expected_width is None:
                expected_width = width
                tables_checked += 1
            if width != expected_width:
                table_errors.append(f"{path.relative_to(ROOT)}:{number}")
        else:
            expected_width = None
check("local_files_and_fragments", not link_errors, {"checked": links_checked, "errors": link_errors})
check("markdown_table_widths", not table_errors, {"tables": tables_checked, "errors": table_errors})

changed_paths = set(git("diff", "--name-only", BASE).splitlines())
changed_paths.update(git("ls-files", "--others", "--exclude-standard").splitlines())
outside_scope = sorted(path for path in changed_paths if path and not permitted(path))
check("only_owned_routes", not outside_scope,
      {"changed_paths": sorted(changed_paths), "outside_scope": outside_scope})
diff = subprocess.run(["git", "diff", "--check", BASE], cwd=ROOT, capture_output=True, text=True)
check("git_diff_check", diff.returncode == 0, diff.stdout + diff.stderr or "clean")
report = {
    "checked_on": "2026-10-04", "scope": "Author documentary integrity before delivery commit; semantic source comparison in DC01-DC14; no rendered or runtime test.",
    "operating_baseline": BASE, "reviewed_content_sha": CONTENT, "reviewed_architecture_sha": ARCH,
    "status": "pass" if all(item["status"] == "pass" for item in checks) else "fail",
    "checks": checks,
    "pending": ["Consolidator acceptance and receipt", "PC/phone compositions and applied behaviour", "Linguistic review", "G3/M2 technical and access policies", "Independent G4 application review"],
}
report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"status": report["status"], "checks": len(checks),
                  "failed": [item for item in checks if item["status"] == "fail"]}, ensure_ascii=False, indent=2))
raise SystemExit(0 if report["status"] == "pass" else 1)
