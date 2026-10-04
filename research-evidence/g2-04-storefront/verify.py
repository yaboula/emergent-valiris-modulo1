"""Check documentary source integrity and critical ORILLA fixture relationships.

No application, food-safety, accessibility or independent review is performed.
Writes only checks.json/source-manifest.json in this owned evidence directory.
"""

import collections
import datetime as dt
import hashlib
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
BASE = "6046327ee9216e26ed56aeac81c346f7299735d8"
BRANCH = "docs/m1-g2-04-orilla-content"
CASE = "docs/design/orilla-case.md"
COPY = "docs/design/m1-storefront-content-and-copy.md"
OWN = "research-evidence/g2-04-storefront/"
IA_SHA = "ff8fc061dfb4e63461ee2b77b5a18f02108edb6b"
G4_SHA = "2b2a4a3bf5506c94b95d9b177f6006946200df24"
G4_PATH = "research-evidence/reviews/g4-selected-e7065aa/g4-review.md"
SOURCES = [
    "AGENTS.md", "CONTRIBUTING.md", "HANDOFF.md", "coordination/README.md",
    "coordination/valiris-restaurants/workspace-working-agreement-2026-10-01.md",
    "coordination/valiris-restaurants/Valiris_G2_Brief_Arranque_Diseno.md",
    "coordination/valiris-restaurants/Valiris_Contexto_Comun_Agentes.md",
    "coordination/valiris-restaurants/Valiris_Organizacion_Protocolo_Agentes.md",
    "coordination/valiris-restaurants/G2_04_Contenido_Storefront_ORILLA_Prompt.md",
    "coordination/valiris-restaurants/SEO_Estrategia_Contenido_Prompt.md",
    "docs/project/roadmap.md", "docs/product/m1-design-briefs.md",
    "docs/product/m0-journeys-and-criteria.md", "docs/product/m0-capability-matrix.md",
    "docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md",
    "docs/design/m1-public-presence-and-discovery.md",
    "docs/design/m1-connected-journey.md", "docs/design/m1-coverage-and-evidence.md",
    "docs/design/m1-storefront-information-architecture.md",
    "research-evidence/g2-02-storefront/content-requests.md",
    "research-evidence/reviews/orilla-architecture-ff8fc06/g1-review.md",
    "research-evidence/reviews/coverage-d71d3de/review-result.md",
    "docs/project/valiris-restaurants-brand-foundation-brief.md",
    "docs/design/valiris-restaurants-brand-refinement.md",
    "research-evidence/g2-06-restaurants-brand/refinement/selected-three-references-2026-10-03.es.md",
]
ASSETS = [
    "research-evidence/g2-06-art-direction-2026-10-03/storefront-v0.2/02-cartel-revisado-v0.2.png",
    "research-evidence/g2-06-restaurants-brand/refinement/signature-and-first-model/03-orilla-contraste-propuesto.png",
    "research-evidence/g2-06-restaurants-brand/refinement/signature-and-first-model/02-expresion-sin-personajes.png",
    "research-evidence/g2-06-restaurants-brand/refinement/polish-v2/01-cafeteria-refinada-v2.png",
    "research-evidence/g2-06-restaurants-brand/refinement/polish-v2/02-campana-refinada-v2.png",
]
SKILLS = [
    Path("C:/Users/aboul/.codex/skills/ux-writing-content-design/SKILL.md"),
    Path("C:/Users/aboul/.codex/skills/rampstack-content-and-copy/SKILL.md"),
]


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def slug(text):
    text = re.sub(r"[*`]|<[^>]*>", "", text.strip().lower())
    return re.sub(r"\s", "-", re.sub(r"[^\w\- ]", "", text))


def anchors(path):
    found, count = set(), collections.Counter()
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if m := re.match(r"^#{1,6} (.+)$", line):
            key = slug(m[1])
            found.add(key if not count[key] else f"{key}-{count[key]}")
            count[key] += 1
    return found


def table_records(text, prefix):
    result = {}
    for line in text.splitlines():
        if line.startswith("| " + prefix):
            row = [x.strip() for x in line.strip().strip("|").split("|")]
            key = row[0].split(" / ")[0]
            if key.startswith(prefix):
                assert key not in result, f"Duplicate record: {key}"
                result[key] = row
    return result


def own(path):
    return path in (CASE, COPY) or path.startswith(OWN)


def main():
    assert Path(git("rev-parse", "--show-toplevel").decode().strip()).resolve() == ROOT
    assert git("branch", "--show-current").decode().strip() == BRANCH
    assert git("merge-base", "--is-ancestor", BASE, "HEAD") == b""
    changed = set(git("diff", "--name-only", BASE).decode().splitlines())
    untracked = set(git("ls-files", "--others", "--exclude-standard").decode().splitlines())
    assert all(own(p) for p in changed | untracked), "Foreign paths changed/untracked"
    git("diff", "--check", BASE)

    sources = []
    # Preserve every source/ADR/graphic blob; this is not a claim to re-audit it.
    preserved = SOURCES + ASSETS + git("ls-tree", "-r", "--name-only", BASE, "docs/adr").decode().splitlines()
    for path in preserved:
        baseline = git("show", f"{BASE}:{path}")
        blob = git("rev-parse", f"{BASE}:{path}").decode().strip()
        current = (ROOT / path).read_bytes()
        # git hash-object honours checkout line-ending policy.
        assert git("hash-object", "--path", path, path).decode().strip() == blob, path
        sources.append({"path": path, "baseline_git_blob": blob,
                        "baseline_sha256": sha256(baseline), "checkout_sha256": sha256(current)})
    for path in ("docs/design/m1-storefront-information-architecture.md",
                 "research-evidence/g2-02-storefront/content-requests.md"):
        assert git("rev-parse", f"{BASE}:{path}") == git("rev-parse", f"{IA_SHA}:{path}")

    case = (ROOT / CASE).read_text(encoding="utf-8-sig")
    copy = (ROOT / COPY).read_text(encoding="utf-8-sig")
    dishes = table_records(case, "ORI-DISH-0")
    dishes.update(table_records(case, "ORI-DISH-1"))
    # Variant rows are separate records, not separate dish identities.
    dish_rows = {k: v for k, v in dishes.items() if re.fullmatch(r"ORI-DISH-\d{2}", k)}
    offers = table_records(case, "ORI-MENU-P")
    categories = table_records(case, "ORI-MENU-C")
    food = table_records(case, "ORI-FOOD-0")
    food.update(table_records(case, "ORI-FOOD-1"))
    scenarios = table_records(case, "ORI-SCENARIO-")
    assert len(dish_rows) == 11 and len(offers) == 13 and len(categories) == 4
    assert set(scenarios) == {f"ORI-SCENARIO-{n:02d}" for n in range(11)}
    for offer in offers.values():
        assert re.search(r"ORI-DISH-\d{2}", offer[1])[0] in dish_rows
        assert re.search(r"\d+,\d{2} €", offer[3]) and offer[2] and offer[4]
    for dish in dish_rows.values():
        assert re.search(r"ORI-FOOD-\d{2}", dish[3])[0] in food
    assert len(dish_rows["ORI-DISH-02"][1]) >= 60, "No representative long name"
    assert offers["ORI-MENU-P05"][3] + " · " + offers["ORI-MENU-P05"][4] in copy
    assert f"{offers['ORI-MENU-P02'][2]} · {offers['ORI-MENU-P02'][3]} / {offers['ORI-MENU-P03'][2]} · {offers['ORI-MENU-P03'][3]}" in copy
    assert set(re.findall(r"\d+,\d{2} €", copy)) <= set(re.findall(r"\d+,\d{2} €", case)), "Copy invented an amount"
    assert "V01 or V02" in offers["ORI-MENU-P02"][1] and "V01 or V02" in offers["ORI-MENU-P03"][1]
    assert "Leche" in food["ORI-FOOD-02"][2] and "avellanas" in food["ORI-FOOD-02"][2]
    assert "Avellanas" in food["ORI-FOOD-02-V02"][2] and "Milk absence NOT established" in food["ORI-FOOD-02-V02"][3]
    assert "Leche; huevo" == food["ORI-FOOD-08"][2]
    assert all(row[3] for row in food.values()), "Pending food fields omitted"
    assert all("P09" in " ".join(scenarios[f"ORI-SCENARIO-{n:02d}"]) for n in (0, 1, 2))
    assert "H02" in scenarios["ORI-SCENARIO-01"][2]
    assert "not confirmed" in scenarios["ORI-SCENARIO-03"][1]
    assert "private" in case[case.index("### ORI-FOOD-CHANGE-01"):case.index("## 7.")].lower()

    sunday, tuesday = dt.date(2026, 10, 4), dt.date(2026, 10, 6)
    assert sunday.weekday() == 6 and tuesday.weekday() == 1
    def minutes(text):
        hour, minute = map(int, text.split(":"))
        return hour * 60 + minute
    def is_open(clock, start, end):
        return minutes(start) <= minutes(clock) < minutes(end)
    clock_states = {clock: [is_open(clock, "12:30", "17:00"), is_open(clock, "13:00", "15:30")]
                    for clock in ("10:30", "12:45", "14:00", "15:30", "17:00")}
    assert list(clock_states.values()) == [[False, False], [True, False], [True, True], [True, False], [False, False]]
    assert not is_open("13:15", "13:30", "15:30")

    docs = [ROOT / CASE, ROOT / COPY] + sorted(HERE.glob("*.md"))
    generated_reports = {HERE / "checks.json", HERE / "source-manifest.json"}
    links, tables, copy_ids = 0, 0, []
    heading_cache = {}
    for path in docs:
        body = path.read_text(encoding="utf-8-sig")
        assert not re.search(r"^(<<<<<<<|=======|>>>>>>>)", body, re.M), path
        assert body.count("```") % 2 == 0, path
        width = None
        for line in body.splitlines():
            if line.startswith("|"):
                cells = len(line.strip().strip("|").split("|"))
                if width is None:
                    tables += 1
                    width = cells
                assert cells == width, f"Table width {path}: {line}"
                if path.name == Path(COPY).name and re.match(r"\| ORI-COPY-", line):
                    copy_ids.append(line.split("|")[1].strip().split(" / ")[0])
            else:
                width = None
        for target in re.findall(r"\[[^\]]+\]\(([^\)]+)\)", body):
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("//"):
                continue
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            assert dest.is_relative_to(ROOT) and (dest.exists() or (dest in generated_reports and not parsed.fragment)), f"Missing local link: {path}: {target}"
            if parsed.fragment:
                heading_cache.setdefault(dest, anchors(dest))
                assert unquote(parsed.fragment) in heading_cache[dest], f"Missing anchor: {target}"
            links += 1
    assert len(copy_ids) == len(set(copy_ids)), "Duplicate copy ID"
    assert {f"ORI-COPY-S{n:02d}" for n in range(1, 31)} <= set(copy_ids)
    for request in [f"CR{n:02d}" for n in range(1, 8)] + ["XR01"]:
        assert f"| {request} |" in (HERE / "README.md").read_text(encoding="utf-8-sig")
    assert "partial" in copy.lower() and "Not received" in (HERE / "README.md").read_text(encoding="utf-8-sig")
    skills = [{"path": str(path), "sha256": sha256(path.read_bytes()), "status": "read and adapted, unchanged"} for path in SKILLS]
    manifest = {"operating_baseline": BASE, "architecture_source": IA_SHA,
                "sources": sources, "conceptual_g4_source": {"sha": G4_SHA, "path": G4_PATH,
                "sha256": sha256(git("show", f"{G4_SHA}:{G4_PATH}"))}, "skills": skills,
                "reading_scope": "See README; integrity preservation is broader than fresh semantic review.",
                "deliverables": [{"path": p, "sha256": sha256((ROOT / p).read_bytes())} for p in (CASE, COPY)]}
    checks = {"status": "passed", "scope": "author documentary integrity/relationships, no product tests",
              "operating_baseline": BASE, "branch": BRANCH, "source_records_preserved": len(sources),
              "local_links": links, "tables": tables, "unique_copy_ids": len(copy_ids),
              "dishes": len(dish_rows), "offers": len(offers), "categories": len(categories),
              "food_records": len(food), "scenarios": len(scenarios), "long_dish_name_characters": len(dish_rows["ORI-DISH-02"][1]),
              "clock_states_local_kitchen": clock_states, "fictional_date_weekdays": "4 October Sunday; 6 October Tuesday",
              "unchanged_architecture_requests": True, "owned_paths_only": True,
              "not_checked": ["real food", "translations", "SEO/GEO applied review", "UI/render/accessibility",
                              "participants", "runtime/stock/publication", "rights", "independent application review"]}
    for name, data in (("checks.json", checks), ("source-manifest.json", manifest)):
        (HERE / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    assert all(path.exists() for path in generated_reports)
    print(json.dumps(checks, ensure_ascii=False))


if __name__ == "__main__":
    main()
