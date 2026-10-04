"""Reproduce bounded document/source integrity checks; never tests application UX."""

import collections
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
BASE = "56306793d54bb8df74305134ec6284c6d647eebf"
BRANCH = "docs/m1-g2-02-orilla-content-1-1-adoption"
OLD_ARCH = "ff8fc061dfb4e63461ee2b77b5a18f02108edb6b"
OLD_BRANCH = "docs/m1-g2-02-storefront-architecture"
PREVIOUS_ARCH = "ba44c6809516d8d078d192f5f6a423b12cd8b673"
PREVIOUS_BRANCH = "docs/m1-g2-02-orilla-content-adoption"
OLD_CONTENT_SHA = "5bd3184ca48be8d579e3f82d3361dbf5de0ed228"
CONTENT_SHA = "4b382bebe5d5c6cad21a7edcaffab053c433a0e9"
SEO_SHA = "0c17480bdc2b6ff8037022228ebc4599a704e702"
FIRST_DELIVERY = "c2faedff9209571d793f21a8df3200b8f1a93077"
METHOD_SHA = "3d4510a94a76ead80122c691b5c480f92f3fbe40"
MAIN = "docs/design/m1-storefront-information-architecture.md"
OWN = "research-evidence/g2-02-storefront/"
DOCS = [MAIN] + [OWN + name for name in (
    "README.md", "content-requests.md", "documentary-contrasts.md", "rampstack-adaptation.md",
    "adoption.md", "content-adoption-contrasts.md", "content-1-1-adoption.md",
    "content-1-1-contrasts.md")]
PINNED = {
    "docs/design/orilla-case.md": (CONTENT_SHA, "ad0f42fc461396e1d28191c667b077c060195a38", "ORI-CASE-1.1"),
    "docs/design/m1-storefront-content-and-copy.md": (CONTENT_SHA, "d570c699455169c4d27c2fe8fc384250ce47fbd7", "ORI-COPY-1.1"),
    "docs/design/m1-storefront-discovery-content.md": (SEO_SHA, "57345211d68b3d67be7bfe5ff726ba718b041e78", "SEO/GEO 1.0"),
}
METHOD_FILES = [
    ("skills/information-architecture/SKILL.md", "6334299eb89142e856dcb7dd7619112edfcc9320", 10456),
    ("skills/information-architecture/references/ia-document-template.md", "4f7ad123579e32d18aab625b480c44b8b8b01503", 7519),
    ("skills/information-architecture/references/url-pattern-library.md", "75bf05273c1ffb1d7c81fd0cb72934f3e97df4a6", 8047),
    ("LICENSE", "9d5acfd7a3ad1c3c164a15834a06ff101197cae4", 1070),
]
SOURCES = [
    "AGENTS.md", "CONTRIBUTING.md", "HANDOFF.md", "coordination/README.md",
    "coordination/valiris-restaurants/G2_02_Arquitectura_Storefront_ORILLA_Prompt.md",
    "coordination/valiris-restaurants/Valiris_G2_Brief_Arranque_Diseno.md",
    "coordination/valiris-restaurants/Valiris_Contexto_Comun_Agentes.md",
    "coordination/valiris-restaurants/Valiris_Organizacion_Protocolo_Agentes.md",
    "coordination/valiris-restaurants/G2_04_Contenido_Storefront_ORILLA_Prompt.md",
    "coordination/valiris-restaurants/SEO_Estrategia_Contenido_Prompt.md",
    "coordination/valiris-restaurants/G2_07_UI_Storefront_Adaptativo_Prompt.md",
    "docs/design/orilla-case.md", "docs/project/roadmap.md",
    "docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md",
    "docs/product/m1-design-briefs.md", "docs/product/m0-capability-matrix.md",
    "docs/product/m0-journeys-and-criteria.md",
    "docs/design/m1-public-presence-and-discovery.md",
    "docs/design/m1-connected-journey.md", "docs/design/m1-coverage-and-evidence.md",
    "docs/design/m1-extended-journeys.md",
    "docs/project/valiris-restaurants-brand-foundation-brief.md",
    "docs/design/valiris-restaurants-brand-refinement.md",
    "research-evidence/g2-06-restaurants-brand/refinement/selected-three-references-2026-10-03.es.md",
] + ["docs/adr/" + x for x in (
    "0005-repository-and-product-language.md",
    "0008-first-launch-capability-commitment.md",
    "0009-studio-design-and-registered-diner-personalisation.md",
    "0010-diner-account-and-display-recovery.md",
    "0011-shared-menu-content-and-contextual-maintenance.md",
)] + ["research-evidence/g2-06-restaurants-brand/refinement/" + x for x in (
    "signature-and-first-model/02-expresion-sin-personajes.png",
    "polish-v2/01-cafeteria-refinada-v2.png",
    "polish-v2/02-campana-refinada-v2.png",
)]
SOURCES += [
    "docs/design/m1-storefront-content-and-copy.md",
    "docs/design/m1-storefront-discovery-content.md",
    "research-evidence/g2-04-storefront/README.md",
    "research-evidence/g2-04-storefront/delivery.md",
    "research-evidence/reviews/orilla-architecture-ff8fc06/g1-review.md",
    "research-evidence/reviews/orilla-content-5bd3184/g1-review.md",
    "research-evidence/reviews/orilla-seo-0c17480/g1-review.md",
    "research-evidence/seo-storefront/delivery.md",
    "research-evidence/seo-storefront/primary-sources.md",
    "research-evidence/reviews/orilla-joint-4b382be-ba44c68/g1-review.md",
    "research-evidence/g2-04-storefront/seo-consolidation-1.1/resolutions.md",
    "research-evidence/g2-04-storefront/seo-consolidation-1.1/delivery.md",
    "research-evidence/g2-04-storefront/seo-consolidation-1.1/author-review.md",
]
G4_SHA = "2b2a4a3bf5506c94b95d9b177f6006946200df24"
G4_PATH = "research-evidence/reviews/g4-selected-e7065aa/g4-review.md"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def slug(title):
    title = re.sub(r"[*`]|<[^>]*>", "", title.strip().lower())
    return re.sub(r"\s", "-", re.sub(r"[^\w\- ]", "", title))


def headings(path):
    found, counts = set(), collections.Counter()
    fenced = False
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("```"):
            fenced = not fenced
        if not fenced and (m := re.match(r"^#{1,6}\s+(.+)$", line)):
            key = slug(m[1])
            found.add(key if not counts[key] else f"{key}-{counts[key]}")
            counts[key] += 1
    return found


errors = []


def require(condition, message):
    if not condition:
        errors.append(message)


branch = git("branch", "--show-current").decode().strip()
require(branch == BRANCH, "Wrong assignment branch")
require(Path(git("rev-parse", "--show-toplevel").decode().strip()).resolve() == ROOT,
        "Wrong repository root")
require(subprocess.run(["git", "merge-base", "--is-ancestor", BASE, "HEAD"],
                       cwd=ROOT, capture_output=True).returncode == 0,
        "Baseline is not an ancestor of HEAD")
require(subprocess.run(["git", "merge-base", "--is-ancestor", FIRST_DELIVERY, "HEAD"],
                       cwd=ROOT, capture_output=True).returncode == 0,
        "First published proposal is not retained in branch history")
old_branch_frozen = git("rev-parse", "refs/heads/" + OLD_BRANCH).decode().strip() == OLD_ARCH
require(old_branch_frozen, "Original architecture branch advanced beyond frozen #33 source")
previous_branch_frozen = git("rev-parse", "refs/heads/" + PREVIOUS_BRANCH).decode().strip() == PREVIOUS_ARCH
require(previous_branch_frozen, "Previous architecture branch advanced beyond frozen #40 source")
changed = set(git("diff", BASE, "--name-only").decode().splitlines())
untracked = set(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
require(all(p == MAIN or p.startswith(OWN) for p in changed | untracked),
        "A changed/untracked delivery file is outside owned paths")

records = []
for path in SOURCES:
    data = git("show", f"{BASE}:{path}")
    require((ROOT / path).read_bytes() == data, f"Baseline source changed: {path}")
    records.append({"path": path, "source_commit": BASE,
                    "git_blob": git("rev-parse", f"{BASE}:{path}").decode().strip(),
                    "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})
    if path in PINNED:
        sha, expected, version = PINNED[path]
        require(git("rev-parse", f"{sha}:{path}").decode().strip() == expected,
                f"Unexpected adopted source identity: {path}")
        require(git("show", f"{sha}:{path}") == data,
                f"Operating baseline changed the adopted source: {path}")
        records[-1].update({"authority_commit": sha, "adopted_version": version})
data = git("show", f"{G4_SHA}:{G4_PATH}")
records.append({"path": G4_PATH, "source_commit": G4_SHA,
                "git_blob": git("rev-parse", f"{G4_SHA}:{G4_PATH}").decode().strip(),
                "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data),
                "scope": "separate frozen conceptual review, not IA/application approval"})

external_records = []
external_valid = True
for path, expected_blob, expected_bytes in METHOD_FILES:
    archived_path = OWN + "method/rampstack/upstream/" + path
    data = (ROOT / archived_path).read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    valid = blob == expected_blob and len(data) == expected_bytes
    external_valid = external_valid and valid
    require(valid, f"Pinned method archive altered: {archived_path}")
    external_records.append({"repository": "rampstackco/claude-skills",
                             "source_commit": METHOD_SHA, "upstream_path": path,
                             "archive_path": archived_path,
                             "source_url": f"https://github.com/rampstackco/claude-skills/blob/{METHOD_SHA}/{path}",
                             "git_blob": blob, "sha256": hashlib.sha256(data).hexdigest(),
                             "bytes": len(data), "license": "MIT; original notice archived in bundle"})

links = tables = fences = 0
doc_text = {}
for name in DOCS:
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    doc_text[name] = text
    require(not re.search(r"^(<<<<<<<|=======|>>>>>>>)", text, re.M),
            f"Conflict marker: {name}")
    require(text.endswith("\n"), f"Missing final newline: {name}")
    table_width = None
    in_fence = False
    for n, line in enumerate(text.splitlines(), 1):
        require(line == line.rstrip(), f"Trailing whitespace: {name}:{n}")
        if line.startswith("```"):
            fences += 1
            in_fence = not in_fence
        if in_fence:
            continue
        if line.startswith("|"):
            width = len(re.split(r"(?<!\\)\|", line)) - 2
            if table_width is None:
                tables += 1
                table_width = width
            require(width == table_width, f"Table width: {name}:{n}")
        else:
            table_width = None
    require(not in_fence, f"Unbalanced fences: {name}")
    for target in re.findall(r"!?\[[^\]]*\]\(([^)\n]+)\)", text):
        target = target.strip().strip("<>")
        if urlsplit(target).scheme:
            continue
        base, _, fragment = unquote(target).partition("#")
        resolved = (path.parent / base).resolve() if base else path
        require(resolved.is_relative_to(ROOT), f"External local link: {name}: {target}")
        require(resolved.exists(), f"Missing link: {name}: {target}")
        if resolved.exists() and fragment:
            require(fragment in headings(resolved), f"Missing fragment: {name}: {target}")
        links += 1

main = doc_text[MAIN]
dest = re.findall(r"^\| (IA-(?:H0[1-4]|M01|D01|R01)) —", main, re.M)
require(set(dest) == {"IA-H01", "IA-H02", "IA-H03", "IA-H04", "IA-M01", "IA-D01", "IA-R01"}
        and len(dest) == 7, "Destination table IDs missing/duplicated")
journeys = re.findall(r"^\| (IA-J\d{2}) —", main, re.M)
require(journeys == [f"IA-J{x:02}" for x in range(1, 7)], "Journey IDs missing/duplicated")
previous_main = git("show", f"{PREVIOUS_ARCH}:{MAIN}").decode("utf-8-sig")
maps_preserved = re.findall(r"```mermaid\n.*?```", main, re.S) == re.findall(
    r"```mermaid\n.*?```", previous_main, re.S)
require(maps_preserved, "Existing structural/entry-return maps changed without cause")
unaffected_journeys_preserved = [r for r in main.splitlines() if r.startswith("| IA-J")
                                and not r.startswith("| IA-J02")] == [
    r for r in previous_main.splitlines() if r.startswith("| IA-J") and not r.startswith("| IA-J02")]
require(unaffected_journeys_preserved, "Unaffected v0.3 journeys changed")
requests = doc_text[OWN + "content-requests.md"]
cr = re.findall(r"^\| (CR\d{2}) —", requests, re.M)
xr = re.findall(r"^\| (XR\d{2}) —", requests, re.M)
require(cr == [f"CR{x:02}" for x in range(1, 8)], "Content request IDs missing/duplicated")
require(xr == [f"XR{x:02}" for x in range(1, 5)], "Cross-return IDs missing/duplicated")
contrasts = re.findall(r"^\| (IA-C\d{2}) \|", doc_text[OWN + "documentary-contrasts.md"], re.M)
require(contrasts == [f"IA-C{x:02}" for x in range(1, 27)], "Contrast IDs missing/duplicated")
first_contrasts = git("show", f"{FIRST_DELIVERY}:{OWN}documentary-contrasts.md").decode("utf-8")
old_rows = re.findall(r"^\| IA-C\d{2} \|.*$", first_contrasts, re.M)
new_rows = re.findall(r"^\| IA-C\d{2} \|.*$", doc_text[OWN + "documentary-contrasts.md"], re.M)
preserved = len(old_rows) == 22 and old_rows == new_rows[:22]
require(preserved, "The original 22 documentary contrast rows were changed")
historical_evidence_preserved = all(
    (ROOT / (OWN + p)).read_bytes() == git("show", f"{OLD_ARCH}:{OWN}{p}")
    for p in ("documentary-contrasts.md", "rampstack-adaptation.md"))
require(historical_evidence_preserved, "Frozen v0.2 contrasts or method adaptation changed")
previous_adoption_preserved = all(
    (ROOT / (OWN + p)).read_bytes() == git("show", f"{PREVIOUS_ARCH}:{OWN}{p}")
    for p in ("adoption.md", "content-adoption-contrasts.md"))
require(previous_adoption_preserved, "Frozen v0.3 adoption or contrasts changed")
new_contrasts = re.findall(r"^\| (IA-CA\d{2}) \|",
                          doc_text[OWN + "content-adoption-contrasts.md"], re.M)
require(new_contrasts == [f"IA-CA{x:02}" for x in range(1, 19)],
        "Adoption contrast IDs missing/duplicated")
adoption = doc_text[OWN + "adoption.md"]
seo_outcomes = re.findall(r"^\| (SEO-R\d{2}) \|", adoption, re.M)
require(seo_outcomes == [f"SEO-R{x:02}" for x in range(1, 13)],
        "SEO recommendation outcome IDs missing/duplicated")

case = (ROOT / "docs/design/orilla-case.md").read_text(encoding="utf-8-sig")
copy = (ROOT / "docs/design/m1-storefront-content-and-copy.md").read_text(encoding="utf-8-sig")
scoped_adoption = doc_text[OWN + "content-1-1-adoption.md"]
scoped_contrasts = doc_text[OWN + "content-1-1-contrasts.md"]
scoped_ids = re.findall(r"^\| (IA-CB\d{2}) \|", scoped_contrasts, re.M)
require(scoped_ids == [f"IA-CB{x:02}" for x in range(1, 11)],
        "Scoped 1.1 contrast IDs missing/duplicated")
current_docs = main + requests + scoped_adoption + scoped_contrasts
source_tokens = set(re.findall(r"\bORI-[A-Z0-9]+(?:-[A-Z0-9]+)*\b", case + copy))
for token in set(re.findall(r"\bORI-[A-Z0-9]+(?:-[A-Z0-9]+)*\b", current_docs)):
    # Bare families are valid prefixes; detailed IDs must be exact source tokens.
    require(token in source_tokens or (not re.search(r"\d", token) and token in case + copy),
            f"Unknown adopted case/copy ID: {token}")

# Compare source rows, not declared counts, to detect silent old/new string mixing.
def copy_rows(body):
    return {m[1]: m[0] for m in re.finditer(r"^\| (ORI-COPY-[A-Z0-9-]+) /.*$", body, re.M)}

old_copy = git("show", f"{OLD_CONTENT_SHA}:docs/design/m1-storefront-content-and-copy.md").decode("utf-8-sig")
old_case = git("show", f"{OLD_CONTENT_SHA}:docs/design/orilla-case.md").decode("utf-8-sig")
old_copy_rows, new_copy_rows = copy_rows(old_copy), copy_rows(copy)
revised_copy_ids = sorted(k for k in old_copy_rows.keys() & new_copy_rows.keys()
                          if old_copy_rows[k] != new_copy_rows[k])
added_copy_ids = sorted(new_copy_rows.keys() - old_copy_rows.keys())
expected_revised = sorted("ORI-COPY-" + k for k in ("H02-07", "M01-03", "S10", "S11", "S14", "S18"))
expected_added = sorted(["ORI-COPY-H03-09"] + [f"ORI-COPY-E{x:02}" for x in range(1, 4)]
                        + [f"ORI-COPY-META-{x:02}" for x in range(1, 8)])
require(len(old_copy_rows) == 83 and len(new_copy_rows) == 94
        and old_copy_rows.keys() <= new_copy_rows.keys(), "Historical copy identities lost")
require(revised_copy_ids == expected_revised and added_copy_ids == expected_added,
        "Source diff exceeds six revised/eleven new copy IDs")
for identity in expected_revised + expected_added:
    require(identity in scoped_adoption, f"Affected 1.1 ID not registered: {identity}")

def region(body, start, end):
    return body.split(start, 1)[1].split(end, 1)[0]

factual_regions_preserved = all(region(old_case, a, b) == region(case, a, b) for a, b in (
    ("## 2. Origin and people", "## 4. One representative menu"),
    ("### Dish source strings", "## 7. Frozen scenarios using the same records")))
require(factual_regions_preserved, "Restaurant/story/offer/price/visit/food facts changed")
old_scenarios = [line for line in old_case.splitlines() if line.startswith("| ORI-SCENARIO-")]
new_scenarios = [line for line in case.splitlines() if line.startswith("| ORI-SCENARIO-")]
require(len(old_scenarios) == len(new_scenarios) == 11, "Scenario identity count changed")
scenario_inputs_preserved = all(a.split("|")[2] == b.split("|")[2]
                               for a, b in zip(old_scenarios, new_scenarios))
require(scenario_inputs_preserved, "Scenario factual inputs changed")
require("| ORI-SCENARIO-06 / 2 |" in case
        and "domingo 4 de octubre de 2026, 13:30–15:30" in main,
        "Fully dated exception revision missing")
metadata_relations = re.findall(r"^\| (ORI-COPY-META-\d{2}) \|", scoped_adoption, re.M)
require(metadata_relations == [f"ORI-COPY-META-{x:02}" for x in range(1, 8)],
        "Conditional metadata relation coverage missing/duplicated")
category_map = [
    ("ORI-MENU-C01", "Para el centro", "Para compartir"),
    ("ORI-MENU-C02", "Del horno y la cuchara", "Platos"),
    ("ORI-MENU-C03", "Un final y sobremesa", "Postres"),
    ("ORI-MENU-C04", "Para beber", "Bebidas"),
]
for identity, title, jump in category_map:
    require(f"| {identity} | {title} | {jump} |" in main,
            f"Category jump/source identity mapping lost: {identity}")
for identity, name, amount in (
    ("ORI-MENU-P02", "Media ración", "9,50 €"),
    ("ORI-MENU-P03", "Ración", "15,00 €"),
    ("ORI-MENU-P05", "Por persona", "16,00 € / persona"),
    ("ORI-MENU-P09", "Ración", "6,00 €"),
    ("ORI-MENU-P11", "Copa · 125 ml", "3,50 €"),
    ("ORI-MENU-P12", "Botella · 750 ml", "17,50 €"),
):
    offer = next((line for line in case.splitlines() if line.startswith(f"| {identity} |")), "")
    require(name in offer and amount in offer, f"Referenced offer changed: {identity}")
    require(amount in main, f"Representative offer amount absent in IA: {identity}")

matrix = (ROOT / "docs/product/m0-capability-matrix.md").read_text(encoding="utf-8-sig")
rows = [line for line in matrix.splitlines() if re.match(r"^\| B\d\.\d{2} / L", line)]
treatments = collections.Counter(line.split("|")[4].strip() for line in rows)
require(len(rows) == 72 and len({line.split("|")[1].split("/")[0].strip() for line in rows}) == 72,
        "Baseline capability ledger is not 72 unique parents")
require(dict(treatments) == {"Included": 36, "Configurable": 30, "Connection-dependent": 6},
        "Baseline treatment counts changed")
whitespace = subprocess.run(["git", "diff", "--check", BASE], cwd=ROOT,
                            capture_output=True, text=True)
require(whitespace.returncode == 0, "git diff --check failed: " + whitespace.stdout)

manifest = {"baseline": BASE, "delivery_date": "2026-10-04", "sources": records,
            "original_architecture": OLD_ARCH, "previous_architecture": PREVIOUS_ARCH,
            "previous_content_pair": OLD_CONTENT_SHA, "adopted_content_pair": CONTENT_SHA,
            "received_seo_review": SEO_SHA,
            "external_method_sources": external_records}
checks = {"baseline": BASE, "branch": branch, "result": "pass" if not errors else "fail",
          "scope": "author document/source integrity only; no UX, G4 or runtime proof",
          "owned_paths_only": not any(p != MAIN and not p.startswith(OWN) for p in changed | untracked),
          "baseline_sources_unchanged": all((ROOT / p).read_bytes() == git("show", f"{BASE}:{p}")
                                           for p in SOURCES),
          "source_records": len(records), "markdown_documents": len(DOCS),
          "external_method_records": len(external_records),
          "external_method_archives_unchanged": external_valid,
          "first_delivery": FIRST_DELIVERY, "original_contrast_rows_preserved": preserved,
          "original_architecture_branch_frozen": old_branch_frozen,
          "previous_architecture_branch_frozen": previous_branch_frozen,
          "v0_3_adoption_and_contrasts_preserved": previous_adoption_preserved,
          "historical_contrasts_and_method_preserved": historical_evidence_preserved,
          "adopted_content_pair": CONTENT_SHA, "received_seo_review": SEO_SHA,
          "local_links_and_fragments": links, "tables": tables, "fence_lines": fences,
          "destination_ids": len(dest), "journey_ids": len(journeys),
          "structural_and_entry_return_maps_preserved": maps_preserved,
          "unaffected_journeys_preserved": unaffected_journeys_preserved,
          "content_request_ids": len(cr), "cross_return_ids": len(xr),
          "historical_documentary_contrasts": len(contrasts),
          "adoption_documentary_contrasts": len(new_contrasts),
          "scoped_1_1_documentary_contrasts": len(scoped_ids),
          "revised_copy_ids": revised_copy_ids, "new_copy_ids": added_copy_ids,
          "factual_regions_preserved": factual_regions_preserved,
          "scenario_inputs_preserved": scenario_inputs_preserved,
          "metadata_relations": len(metadata_relations),
          "seo_recommendation_outcomes": len(seo_outcomes),
          "category_jump_mappings": len(category_map), "capability_parent_rows": len(rows),
          "treatments": dict(treatments), "git_diff_check": whitespace.returncode == 0,
          "errors": errors}
for name, value in (("sources.json", manifest), ("checks.json", checks)):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8", newline="\n")
print(json.dumps(checks, ensure_ascii=False, indent=2))
sys.exit(bool(errors))
