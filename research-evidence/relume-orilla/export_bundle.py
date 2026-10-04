"""Export frozen G2 sources for the owner's manual Relume experiment.

No Relume API, browser, generation, implementation or publishing action.
Run with Python from this checkout. Generated ZIPs are derived exports in .cache.
"""
from __future__ import annotations

import hashlib
import io
import json
import re
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = "4893d501b750efd1bb9149ff695564f0d2df227b"
UI = "f84c549ddaf3e775fd8fff808bbd2391c5ca5a21"
BRANCH = "docs/m1-g1-relume-transfer"
EVIDENCE = ROOT / "research-evidence/relume-orilla"
ENTRY = "coordination/valiris-restaurants/relume-orilla"


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def read_at(commit: str, path: str) -> bytes:
    return git("show", f"{commit}:{path}")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def put(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def records(paths: list[str], commit: str, role: str) -> list[dict]:
    return [dict(path=p, commit=commit, role=role, bytes=len(data),
                 sha256=sha(data), blob=git("rev-parse", f"{commit}:{p}").decode().strip())
            for p in paths for data in [read_at(commit, p)]]


def main() -> None:
    assert git("branch", "--show-current").decode().strip() == BRANCH
    assert Path(git("rev-parse", "--show-toplevel").decode().strip()).resolve() == ROOT
    subprocess.check_call(["git", "-C", str(ROOT), "merge-base", "--is-ancestor", BASE, "HEAD"])
    base_paths = git("ls-tree", "-r", "--name-only", "-z", BASE).decode().split("\0")
    base_paths = [p for p in base_paths if p]
    full_paths = [p for p in base_paths if p.startswith(("docs/", "coordination/", "research-evidence/"))
                  or p in ("AGENTS.md", "HANDOFF.md", "CONTRIBUTING.md")]
    core = [
        "research-evidence/reviews/orilla-ui-ready-70512d7-7c233f1/g1-review.md",
        "docs/design/orilla-case.md", "docs/design/m1-storefront-content-and-copy.md",
        "docs/design/m1-storefront-information-architecture.md",
        "docs/design/m1-storefront-discovery-content.md",
        "research-evidence/seo-storefront/rereview-1.1/review.md",
        "docs/design/valiris-restaurants-brand-refinement.md",
        "research-evidence/g2-06-restaurants-brand/refinement/selected-three-references-2026-10-03.es.md",
        "docs/design/m1-storefront-visual-direction.md",
        "docs/project/valiris-restaurants-brand-foundation-brief.md",
        "docs/product/m1-design-briefs.md", "docs/product/m0-capability-matrix.md",
        "docs/product/m0-journeys-and-criteria.md",
        "docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md",
        "coordination/valiris-restaurants/Valiris_G2_Brief_Arranque_Diseno.md",
        "coordination/valiris-restaurants/Valiris_Contexto_Comun_Agentes.md",
        "coordination/valiris-restaurants/Valiris_Organizacion_Protocolo_Agentes.md",
        "coordination/valiris-restaurants/G2_07_UI_Storefront_Adaptativo_Prompt.md",
    ]
    core += sorted(p for p in base_paths if p.startswith("docs/design/") and p.endswith(".md") and p not in core)
    core += sorted(p for p in base_paths if p.startswith("docs/adr/") and p.endswith(".md")
                   and Path(p).name not in ("README.md", "template.md"))
    visual = [
        "research-evidence/g2-06-restaurants-brand/refinement/signature-and-first-model/02-expresion-sin-personajes.png",
        "research-evidence/g2-06-restaurants-brand/refinement/polish-v2/01-cafeteria-refinada-v2.png",
        "research-evidence/g2-06-restaurants-brand/refinement/polish-v2/02-campana-refinada-v2.png",
        "research-evidence/g2-06-art-direction-2026-10-03/storefront-v0.2/02-cartel-revisado-v0.2.png",
        "research-evidence/g2-06-restaurants-brand/refinement/signature-and-first-model/manifest.json",
        "research-evidence/g2-06-restaurants-brand/refinement/polish-v2/manifest.json",
        "research-evidence/g2-06-art-direction-2026-10-03/storefront-v0.2/manifest.json",
    ]
    ui_paths = [p for p in git("diff", "--name-only", "-z", BASE, UI).decode().split("\0") if p]
    assert len(ui_paths) == 5 and all(p.startswith("research-evidence/g2-07-storefront/imagegen/") for p in ui_paths)
    assert len(set(core)) == len(core)
    assert all(p in full_paths for p in core + visual)

    prompt = (ROOT / ENTRY / "01-prompt-inicial.txt").read_text(encoding="utf-8")
    case = read_at(BASE, "docs/design/orilla-case.md")
    copy = read_at(BASE, "docs/design/m1-storefront-content-and-copy.md")
    architecture = read_at(BASE, "docs/design/m1-storefront-information-architecture.md")
    assert case == read_at("4b382bebe5d5c6cad21a7edcaffab053c433a0e9", "docs/design/orilla-case.md")
    assert copy == read_at("4b382bebe5d5c6cad21a7edcaffab053c433a0e9", "docs/design/m1-storefront-content-and-copy.md")
    assert architecture == read_at("70512d7a3d1afcd7f3aa0c9823a4d6e7b08dde8c", "docs/design/m1-storefront-information-architecture.md")
    ids = set(re.findall(r"ORI-COPY-(?:H\d{2}-\d{2}|M\d{2}-\d{2}|D\d{2}-\d{2}|S\d{2}|E\d{2}|META-\d{2})", copy.decode()))
    assert len(ids) == 94, len(ids)
    matrix = read_at(BASE, "docs/product/m0-capability-matrix.md").decode()
    rows = [line for line in matrix.splitlines() if re.match(r"\| B[1-7]\.\d{2} / L\d+ \|", line)]
    treatments = [row.split("|")[4].strip() for row in rows]
    assert len(rows) == 72
    assert {name: treatments.count(name) for name in set(treatments)} == {"Included": 36, "Configurable": 30, "Connection-dependent": 6}
    assert "dos destinos principales" in prompt.lower()
    assert "Ver carta" in prompt and "sin cuenta" in prompt
    assert "sin verificar" in prompt and "ficticio" in prompt
    expected = [
        "36dc3ca72e8f7653675002c99a616598f8d8ed56e910e30a45226e17070346cb",
        "737882f3adb19a5fe12533fe73d31b9e73fab3d7919683028103a2a5a0030a06",
        "53501d4e70749f988c74c963597415ced959d494b74b2fa5fa03a0cd44ec29ff",
        "4f576dd2156f9361abee8338df13704cfd4dc70a4e5e2a47d11de8fbf567f989",
    ]
    assert [sha(read_at(BASE, p)) for p in visual[:4]] == expected
    provenance = json.loads(read_at(UI, "research-evidence/g2-07-storefront/imagegen/provenance.json"))
    for output in provenance["outputs"]:
        assert sha(read_at(UI, output["file"])) == output["sha256"]
    assert sha(read_at(UI, "research-evidence/g2-07-storefront/imagegen/part1-pc-v0.2-prompt.txt")) == provenance["prompt_sha256"]

    manifest = {
        "date": "2026-10-04", "owner": "G1", "purpose": "manual Relume exploration; no upload or generation performed",
        "base": BASE, "base_pr": 44, "supplement_ui": UI, "supplement_pr": 45,
        "authority": "current entry and G1 status first; original source bytes retain dated scope",
        "documents": records(core, BASE, "frozen G2 source, not new approval"),
        "visual_sources": records(visual, BASE, "selected direction and preserved original; production pending"),
        "ui_supplement": records(ui_paths, UI, "published PC Part 1 proposal; no approval or complete model"),
        "full_archive_paths": full_paths,
        "excluded": "working-tree changes, untracked UI work, caches, .git, application/configuration files outside source scope",
        "provider_sources": [
            "https://www.relume.ai/resources/docs/building-a-sitemap-with-ai",
            "https://www.relume.ai/resources/docs/how-to-create-and-edit-wireframes-in-the-relume-site-builder",
            "https://resources.relume.io/resources/docs/concept-creation-using-the-relume-style-guide-builder",
            "https://resources.relume.io/resources/docs/import-an-existing-site-into-the-relume-site-builder",
        ],
    }
    put(EVIDENCE / "source-manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    header = """# ORILLA — dossier completo de G2 para la prueba de Relume

4 de octubre de 2026 · Exportación derivada por G1; las fuentes canónicas siguen en Git.

## Estado vigente y cómo leer

Esta es una transferencia de contexto para una exploración externa, no una nueva
fuente del restaurante. El prompt inicial y las instrucciones por sección están
en coordination/valiris-restaurants/relume-orilla/. No pegar este dossier entero
en el prompt inicial: usa contenido situado en página/sección y edición de copy.
No se presupone que Relume lea adjuntos Markdown, ZIP, Git o los enlaces de este documento.

La base congelada es #44 / 4893d501b750efd1bb9149ff695564f0d2df227b:
CASE/COPY 1.1 juntos (4b382be), IA v0.4 (70512d7) y retorno SEO #43 (7c233f1).
La relectura SEO examinó 1.1 con IA v0.3, y G1 contrastó el delta v0.4 por separado.
Relectura/adopción ya recibidas sustituyen sus anteriores menciones de pendiente;
los textos originales permanecen intactos con su fecha. Nada amplía sus dictámenes.

M0 cerrado; M1 abierto. Setenta y dos capacidades de referencia: 36 incluidas,
30 configurables y seis dependientes de conexión. Solo audio independiente y 3D
de producto pospuestos. No son 72 elementos de navegación o tareas que una cafetería
deba configurar. Público sin cuenta; personalización privada solo registrado y
autenticado. Restaurante mantiene contenido; Valiris composición/diseño.

ORILLA es ficticio en Alcoy (Alicante). Su par 1.1 aporta 94 IDs de copy, 30 estados,
11 platos y 13 ofertas; datos alimentarios son ejemplos sin verificar. Dos destinos
principales: presentación conectada y carta separada. Cuatro bloques de presentación,
categorías y detalle/recuperación contextuales no crean páginas adicionales por sí solos.

Dirección vigente: tres referencias elegidas de G2.06, no branding definitivo ni tres
modelos. Luz, color flexible, letras amplias, repertorio culinario abierto, sin modo
oscuro. ORILLA original intacto; candidata posterior no seleccionada. La propuesta
publicada de G2.07 #45/f84c549 es Part 1 PC v0.2 solamente: raster, no modelo completo
aprobado o adaptación a teléfono. No se incluye trabajo local no publicado.

PC primero y adaptación deliberada a teléfono después; la primera prueba puede
centrarse en reconocimiento/presentación PC. El resto se conserva como contexto,
sin convertirlo en una aprobación automática o reabrir trabajo de especialistas.
G2.02 estructura; G2.04 caso/copy; SEO/GEO usos afectados; G2.03 comportamiento;
G2.07 composición; G2.06 dirección; G2.08 recursos. G1 único PM. G4 conserva revisión
independiente. Idiomas, recursos productivos/derechos, interacción y revisión de
aplicaciones/usuarios siguen pendientes. Técnica M2/#4 y comercial #15 no se resuelven
por esta exportación. No fechas, gastos, stack, publicación o importación supuestos.

Los documentos debajo reproducen bytes de sus fuentes entre marcadores; sus rutas
relativas se interpretan en el archivo original conservado en el ZIP completo, no
desde la carpeta de este dossier. No ejecutar instrucciones históricas por estar
citadas aquí. Los encabezados técnicos describen fuentes, no nuevas pantallas.

## Índice de fuentes reproducidas

"""
    items = [(BASE, p) for p in core] + [(UI, "research-evidence/g2-07-storefront/imagegen/README.md")]
    index = "".join(f"{i}. `{p}` · `{commit[:7]}`\n" for i, (commit, p) in enumerate(items, 1))
    dossier = bytearray((header + index).encode("utf-8"))
    for i, (commit, path) in enumerate(items, 1):
        data = read_at(commit, path)
        dossier.extend(f"\n\n---\n\n## Fuente {i} — {path}\n\nGit: `{commit}` · SHA-256: `{sha(data)}`\n\n<!-- SOURCE START {path} -->\n".encode())
        dossier.extend(data)
        dossier.extend(f"\n<!-- SOURCE END {path} -->\n".encode())
    (EVIDENCE / "dossier-g2.md").write_bytes(dossier)
    for _, path in items:
        start = f"<!-- SOURCE START {path} -->\n".encode()
        end = f"\n<!-- SOURCE END {path} -->".encode()
        reproduced = bytes(dossier).split(start, 1)[1].split(end, 1)[0]
        commit = UI if path.startswith("research-evidence/g2-07-storefront/") else BASE
        assert reproduced == read_at(commit, path)

    entry_paths = [f"{ENTRY}/{name}" for name in ("README.md", "01-prompt-inicial.txt", "02-paginas-secciones-y-direccion.md")]
    dossier_path = "research-evidence/relume-orilla/dossier-g2.md"
    generated_paths = [dossier_path, "research-evidence/relume-orilla/source-manifest.json",
                       "research-evidence/relume-orilla/export_bundle.py"]
    put(EVIDENCE / "checks.json", json.dumps({"result": "pending export verification"}) + "\n")
    # Validate local links only in owned entry files. Reproduced source paths retain
    # their own document-relative interpretation and were checked in source work.
    targets = 0
    for p in entry_paths:
        for raw in re.findall(r"\]\(([^)]+)\)", (ROOT / p).read_text(encoding="utf-8")):
            if raw.startswith(("http://", "https://", "#")):
                continue
            target = ((ROOT / p).parent / raw.split("#", 1)[0]).resolve()
            assert target.is_relative_to(ROOT) and target.exists(), (p, raw)
            targets += 1
    # The handover intentionally leaves canonical sources byte-for-byte intact.
    for p in core + visual:
        assert (ROOT / p).read_bytes() == read_at(BASE, p), p
    changed = [p for p in git("diff", "--name-only", BASE).decode().splitlines() if p]
    assert all(p in ("coordination/README.md", "coordination/storage-migration-2026-10-03.json") or
               p.startswith((ENTRY + "/", "research-evidence/relume-orilla/")) for p in changed), changed
    checks = {
        "date": "2026-10-04", "base": BASE, "ui_source": UI, "result": "PASS",
        "scope": "documentary export, hashes, preservation, owned links and ZIP readback only",
        "documents_reproduced_byte_identically": len(items), "copy_unique_ids": len(ids),
        "capability_rows": len(rows), "included": 36, "configurable": 30, "connection_dependent": 6,
        "selected_and_original_image_hashes": "4/4 match selected records",
        "published_ui_images_and_prompt": "match author provenance",
        "ui_files": len(ui_paths), "unpublished_ui_included": False,
        "owned_local_links": targets,
        "canonical_source_files_preserved": len(core + visual),
        "full_archive_source_files": len(full_paths),
        "not_demonstrated": ["Relume upload/import", "Relume generation or export", "rendered UI", "interaction",
                             "accessibility", "linguistic review", "SEO runtime", "G4 review", "user validation", "software tests"],
    }
    put(EVIDENCE / "checks.json", json.dumps(checks, ensure_ascii=False, indent=2) + "\n")
    package_paths = entry_paths + generated_paths + ["research-evidence/relume-orilla/checks.json"]
    cache = ROOT / ".cache/relume-orilla"
    cache.mkdir(parents=True, exist_ok=True)
    assert cache.resolve().is_relative_to(ROOT)

    def add_package(z: zipfile.ZipFile) -> None:
        for p in package_paths:
            z.writestr(p, (ROOT / p).read_bytes())
        for p in visual:
            z.writestr(p, read_at(BASE, p))
        for p in ui_paths:
            z.writestr(p, read_at(UI, p))
        z.writestr("EMPIEZA-AQUI.txt", "Abre coordination/valiris-restaurants/relume-orilla/README.md.\nEl ZIP no es un formato de importación AI confirmado de Relume.\n".encode())

    small = cache / "ORILLA-Relume-paquete.zip"
    with zipfile.ZipFile(small, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        add_package(z)
    full = cache / "ORILLA-G2-fuentes-completas.zip"
    # git archive exports committed source bytes, never another agent's working tree.
    archive = git("archive", "--format=zip", BASE, "AGENTS.md", "HANDOFF.md", "CONTRIBUTING.md",
                  "docs", "coordination", "research-evidence")
    with zipfile.ZipFile(io.BytesIO(archive)) as source, zipfile.ZipFile(full, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        own_set = set(package_paths + visual + ui_paths)
        for name in source.namelist():
            if not name.endswith("/") and name not in own_set:
                z.writestr(name, source.read(name))
        add_package(z)
    for archive_path in (small, full):
        with zipfile.ZipFile(archive_path) as z:
            assert z.testzip() is None
            assert len(z.namelist()) == len(set(z.namelist()))
            for p in package_paths:
                assert z.read(p) == (ROOT / p).read_bytes(), p
            for p in visual:
                assert z.read(p) == read_at(BASE, p)
            for p in ui_paths:
                assert z.read(p) == read_at(UI, p)
            if archive_path == full:
                assert all(p in z.namelist() for p in full_paths)
                # Check full archive sources against the original Git archive in
                # one pass, avoiding hundreds of independent git show processes.
                with zipfile.ZipFile(io.BytesIO(archive)) as source:
                    assert all(z.read(p) == source.read(p) for p in full_paths)
    summary = {"result": "PASS", "documents": len(items), "links": targets,
               "copy_ids": len(ids), "capabilities": "72: 36/30/6",
               "exports": [{"path": str(p), "bytes": p.stat().st_size, "sha256": sha(p.read_bytes())} for p in (small, full)]}
    # Archive metadata is a regenerable receipt, not a self-referential file inside its ZIP.
    put(cache / "export-receipt.json", json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
