from pathlib import Path
import hashlib, json, re, subprocess, difflib

root = Path(r'D:\the next level')
repo = root / 'valiris-restaurants'
folder = root / 'research-evidence/reviews/j6-j7-a0583e0'
prelim = root / 'research-evidence/reviews/j6-j7-preliminary-b63b454'
commit = 'a0583e0ec04e310f6736f1d763ca4d7a78191973'
sha = 'e268d5276cb735f945783ef2f114dc03ff8221c077ac7e8cd2bd09eeeb3e7507'

def command(*args):
    return subprocess.check_output(args, cwd=repo).decode('utf-8').strip()

assert command('git', 'rev-parse', 'HEAD') == commit
assert command('git', 'rev-parse', '@{upstream}') == commit
assert not command('git', 'status', '--porcelain')
pr = json.loads(command('gh', 'pr', 'view', '21', '--json', 'number,state,isDraft,headRefOid,url'))
issues = [json.loads(command('gh', 'issue', 'view', str(n), '--json', 'number,state,url')) for n in (5, 4)]
assert pr['state'] == 'OPEN' and pr['isDraft'] and pr['headRefOid'] == commit
assert all(i['state'] == 'OPEN' for i in issues)
source_bytes = subprocess.check_output(['git', 'show', commit + ':docs/design/m1-food-register-and-outputs.md'], cwd=repo)
assert hashlib.sha256(source_bytes).hexdigest() == sha
assert (folder / 'm1-food-register-and-outputs.snapshot.md').read_bytes() == source_bytes
g4 = (folder / 'g4-review.md').read_text(encoding='utf-8')
assert commit in g4 and sha in g4 and 'no required documentary correction' in g4
old_evidence = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in prelim.iterdir() if p.is_file()}

original = (prelim / 'g1-review.md').read_text(encoding='utf-8')
semantic = original[original.index('Read the complete'):original.index('[Integrity checks]')]
semantic = semantic.replace('complete354-line proposal:18FO cards,24FC contrasts,fiveFW paths,22affected', 'complete 354-line proposal: 18 FO cards, 24 FC contrasts, five FW paths, 22 affected')
semantic = semantic.replace('C1without', 'C1 without').replace('C2long', 'C2 long').replace('C3choices', 'C3 choices')
g1 = f'''# G1 final documentary review — J6–J7 food register and outputs

2 October 2026 · G1 Direction + Product, sole PM consolidator.

**No required documentary correction found in the described branches at `{commit}`.** This final checkpoint supersedes the preliminary verdict for this delivery; it does not close M1 or establish an error-free product.

Frozen [FO snapshot](m1-food-register-and-outputs.snapshot.md), SHA-256 `{sha}`. Full preliminary reading and criterion/case assessment are retained in [the preliminary review](../j6-j7-preliminary-b63b454/g1-review.md). G1 compared the final exact Git bytes with that snapshot and read the final differences and affected operational references. All 18 state bodies, criteria/capability/FC/FW rows and shared behavioral/fixture/composition sections remain identical after newline normalisation. Final changes record author checking, actual JT return, completed author regression/refinement and fully qualified FO scope. The stale administrative JT-pending statement is corrected; no behavioral change required a new whole-block review. G4 independently returned its [final exact-commit review](g4-review.md).

{semantic}
[Integrity checks](document-checks.json): 38 local/internal FO link occurrences resolve against the frozen Git tree; 18 unique cards with required fields, seven original criterion mappings, 22 affected-capability rows, 24 FC and five FW. All 152 earlier contrast rows and earlier card bodies remain preserved, as do original criteria, matrix, functional definition and protected ADRs. The matrix retains 72 parents: 36 included, 30 configurable and six connection-dependent. Whitespace checking passes. [Preliminary-to-final checks](preliminary-to-final-checks.json) and [exact diff](preliminary-to-final.diff) record the unchanged behavior and final bookkeeping changes. These are documentary integrity checks, not software or runtime tests. G2's recorded semantic re-reading of all 152 earlier cases remains author evidence; G1/G4 did not repeat a full independent semantic regression of every earlier block.

No new scope/strategy decision or founder answer is needed for this bounded result. Final G2 delivery is committed/pushed, PR #21 remains OPEN/draft at this exact HEAD, #5 and #4 OPEN, checkout clean/upstream equal. Reviewers preserve repository sources and state. Reports and HANDOFF continuity stay outside Git; no implementation, configuration, merge, tracker closure or external message is performed.

Next G2 work under M1/#5: cross-package coverage of the 72 capabilities/S1/S2 and original criteria, real gaps rather than inferred completion percentages, and a concrete plan for visual direction, templates/bespoke composition, public/mobile/staff/paper/display interaction and evidence. G1 consolidates priorities/behavior and G4 remains independent; visual design collaborates with representative journeys/content. G3/G1 retains technical source/variant/review/permission/group/result/manifest/retention/hosting contracts in M2/#4; G5/G2 supplies actual food/process/adaptation/nutrition/translation/source responsibility, served-recipe confirmation, authorised URLs and material-placement evidence. No specialist consultation is invented.

Product Design guidance informs this documentary review; the agreed deliverable is Markdown description, not a screenshot-based visual audit. Actual interaction, rendered accessibility, food facts/review, generated files, pagination, printing, QR encoding/scanning, devices and participant evidence remain unproved. The approved 72-capability scope and decisions remain intact; only independent audio and 3D are deferred. M1 remains open.
'''

result = f'''# J6–J7 — consolidated final documentary review

2 October 2026 · G1 consolidator and sole PM; G4 independent reviewer.

**No required documentary correction found in the described J6/J7 branches at `{commit}`.** G1 and G4 completed the bounded review of this final delivery. It is not a declaration of zero product defects, UX validation or M1 completion.

[G1 review](g1-review.md), [G4 independent review](g4-review.md), [integrity checks](document-checks.json), [final FO snapshot](m1-food-register-and-outputs.snapshot.md), [original criteria snapshot](m0-journeys-and-criteria.snapshot.md), [matrix snapshot](m0-capability-matrix.snapshot.md) and [final-state checks](final-state-checks.json) are evidence outside Git. The canonical operational source remains [m1-food-register-and-outputs.md](../../../valiris-restaurants/docs/design/m1-food-register-and-outputs.md), linked into the existing coverage map, briefs and roadmap. Snapshot SHA-256: `{sha}`.

Read scope: 354 lines, 18 states, seven original criteria, 22 capability contributions, five FW paths and 24 FC contrasts. Facts known positive and still unknown remain distinct; format/process/adaptation/diet/nutrition are separately scoped. Future private recipe differs from a known actual-service discrepancy; staff-only review/source evidence and faithful current-language fallback are explicit. Output preview/generation uses one coherent source/context/language; known generated file, retrieved file and paper actually placed remain different facts. Partial replacement/newer-source review is bounded. QR requires an actual configured owned public destination and separates content updates from destination/host changes. Recovery keeps original operation, authority and known/unknown result distinct.

The [preliminary checkpoint](../j6-j7-preliminary-b63b454/review-result.md) remains unchanged as history. Final-vs-preliminary comparison preserves all 18 cards, mapped rows and shared behavioral text; five final FO edits record author evidence, actual prior JT return and explicit FO identifiers. The preliminary stale JT-pending administrative entry is resolved. [Comparison record](preliminary-to-final-checks.json) and [diff](preliminary-to-final.diff) preserve this transition. No behavior defect was reproduced; no corrective G2 return is required for this checkpoint.

Structural evidence: 38 local/internal FO links valid against the frozen tree; 152 prior contrast rows/card bodies and protected sources preserved; 72 parents retain 36 included, 30 configurable and six connection-dependent, with S1/S2 separate. Author and independent evidence remain identified separately. Counts/preserved bodies do not prove all accepted capabilities or all M1 criteria are satisfied.

Next G2 responsibility under [M1/#5](https://github.com/yaboula/valiris-restaurants/issues/5): cross-package capability/criterion/gap consolidation and a concrete visual/interaction/evidence plan. Keep the existing single coverage map and backlog; organise journeys by risk within the complete accepted scope. G1 consolidates; visual design collaborates early; G4 retains independent checks. G3/G1 technical contracts stay under [M2/#4](https://github.com/yaboula/valiris-restaurants/issues/4). G5/G2 real sources/food/translation/procedure/destinations/materials and G2/visual/G4 actual rendering, interaction, accessibility, devices, printing, scans and participant evidence remain pending. Consultations require actual availability and concrete questions; none were invented here.

At final readback local HEAD/upstream/PR #21 HEAD match this commit, checkout clean, PR OPEN/draft and #5/#4 OPEN. Reports and current [HANDOFF](../../../HANDOFF.md) are personal continuity outside Git; previous evidence/history and G2 work preserved. No source/configuration change, prototype, implementation, software suite, food/compliance certification, physical test, tracker mutation, merge, closure or external message was performed. No new approved decision changes.
'''
for name, text in [('g1-review.md', g1), ('review-result.md', result)]:
    path = folder / name
    assert not path.exists(), f'Preserve existing report: {path}'
    path.write_text(text, encoding='utf-8', newline='\n')

handoff_path = root / 'HANDOFF.md'
before_bytes = handoff_path.read_bytes()
before = before_bytes.decode('utf-8')
text = before
def replace_once(old, new):
    global text
    assert text.count(old) == 1, (old, text.count(old))
    text = text.replace(old, new, 1)

replace_once('J6–J7 ya entregado por G2 en a0583e0, comprobado documentalmente por su autor; revisión independiente FO y evidencia real pendientes.', 'J6–J7 revisado documentalmente por G1/G4 en a0583e0, sin corrección requerida en las ramas descritas; evidencia visual, interacción y uso real pendientes.')
replace_once('J6–J7 y demás evidencias pendientes antes del cierre de M1;', 'J6–J7 revisado documentalmente por G1/G4 en a0583e0, sin corrección requerida; evidencias reales y revisiones posteriores pendientes antes del cierre de M1;')
replace_once('HEAD 120903f138a798e957b26498f2a3efb5d5e6521a, subida y limpia/sincronizada', f'HEAD {commit}, subida y limpia/sincronizada')
replace_once('ahora revisado documentalmente por G1/G4, sin corrección requerida. #5 sigue OPEN;', 'ahora revisado documentalmente por G1/G4, sin corrección requerida. G2 entregó J6–J7 en a0583e0 y G1/G4 completaron su revisión documental acotada, sin corrección requerida; retorno final enlazado debajo. #5 sigue OPEN;')
replace_once('**Continuidad tras J1–J2:**', '**Continuidad histórica tras J1–J2 — sustituida por el dictamen FO y orden vigente debajo:**')
replace_once('siguen pendientes J6–J7, contratos y evidencias en los checkpoints existentes.', 'J4–J5 y J6–J7 también están revisados documentalmente por G1/G4; contratos y evidencias visuales, de interacción y reales siguen en los checkpoints existentes.')
replace_once('PV/J1–J2 y J4–J5 documentalmente.', 'PV/J1–J2, J4–J5 y J6–J7 documentalmente.')
replace_once('**Comprobación y continuidad vigente tras J4–J5:**', '**Comprobación histórica de entrega J4–J5:**')
replace_once('HEAD actual `120903f138a798e957b26498f2a3efb5d5e6521a`.', 'HEAD en aquella entrega `120903f138a798e957b26498f2a3efb5d5e6521a`.')
replace_once('**Orden actual:**', '**Orden histórico tras J4–J5 — sustituido por entrega y revisión FO debajo:**')
replace_once('### Entrega vigente G2 J6–J7 — 2 de octubre de 2026', '### Entrega G2 J6–J7 — 2 de octubre de 2026; revisión final recibida debajo')
replace_once('G1 coordina revisión independiente G4 sobre este commit cuando haya disponibilidad, contratos G3 y fuentes/procedimientos/idiomas/URLs/materiales G5; contribuciones pendientes, no mensajes enviados ni revisiones inventadas.', 'En el momento de la entrega FO, su revisión independiente estaba pendiente. El dictamen G1/G4 sobre este commit, enlazado debajo, la completa en su alcance documental. Contratos G3 y fuentes/procedimientos/idiomas/URLs/materiales G5 siguen pendientes; no se inventan consultas, mensajes ni pruebas.')
replace_once('Revisión independiente FO, materiales/fuentes/destinos autorizados, contratos técnicos y pruebas reales siguen separados.', 'Revisión independiente FO completada documentalmente según dictamen debajo; materiales/fuentes/destinos autorizados, contratos técnicos y pruebas reales siguen pendientes y separados.')
replace_once('**Siguiente bloque descriptivo y posterior revisión independiente: J6–J7,', '**Siguiente bloque en el momento del dictamen JT — completado y revisado posteriormente debajo: J6–J7,')

section = f'''### Revisión final paralela G1/G4 de J6–J7 — 2 de octubre de 2026

**J6–J7 revisado documentalmente en {commit}, sin corrección requerida en las ramas descritas.** G1, único PM y Dirección/Producto unidos, consolida con G4 independiente. Documento completo de 354 líneas, 18 fichas, siete criterios originales, 22 contribuciones, cinco FW y 24 FC. Positivos alimentarios/pendientes, receta privada/discrepancia real, fuentes/glosario/idiomas, acceso del personal y salidas mantienen sus diferencias. Fuente revisada/archivo generado/recuperado/papel colocado y contenido público/destino QR se contrastaron con recuperación, permisos, concurrencia y cambios posteriores.

Evidencia fuera de Git: [dictamen consolidado](research-evidence/reviews/j6-j7-a0583e0/review-result.md), [G1](research-evidence/reviews/j6-j7-a0583e0/g1-review.md), [G4 independiente](research-evidence/reviews/j6-j7-a0583e0/g4-review.md), [integridad](research-evidence/reviews/j6-j7-a0583e0/document-checks.json), [comparación preliminar/final](research-evidence/reviews/j6-j7-a0583e0/preliminary-to-final-checks.json) y [estado final](research-evidence/reviews/j6-j7-a0583e0/final-state-checks.json); snapshots/diff en esa carpeta. Hash FO {sha}. Los 18 cuerpos, filas y comportamiento compartido permanecen idénticos al [checkpoint preliminar conservado](research-evidence/reviews/j6-j7-preliminary-b63b454/review-result.md); cambios finales registran comprobaciones del autor y retorno JT ya realizado, sin cambiar reglas. 38 enlaces FO válidos; 152 filas previas y fichas/fuentes/criterios/ADRs protegidos preservados; 72 padres/36–30–6 y S1/S2 intactos. La regresión semántica completa de los 152 casos registrada por G2 sigue siendo evidencia del autor, no una suite independiente ejecutada por G4/G1.

**Orden vigente y siguiente encargo G2 bajo #5:** consolidar transversalmente cobertura de las 72 capacidades/S1/S2 y criterios, identificar huecos reales y preparar un plan concreto de dirección visual, composición de plantillas/diseño propio, interacción pública/móvil/personal/papel/pantalla, accesibilidad y evidencias. Reutilizar mapa y backlog existentes; ordenar por recorridos/riesgos no pospone capacidades ni convierte las 72 referencias en navegación obligatoria. G1 consolida decisiones y prioridades; diseñador visual colabora con recorridos y contenido representativo, G4 conserva revisión independiente. No se vuelve a pedir el cierre de M0 ni se exige corregir un hallazgo FO inexistente.

M1/#5 y PR #21 OPEN/draft; M2/#4 OPEN para contratos de fuentes/variantes/revisión/grupos/permisos/resultados/manifiestos/retención/hosting. Checkout limpio y HEAD local/upstream/PR coincidentes al readback. G5/G2 aporta hechos alimentarios, fuentes/idiomas/procedimientos, destinos y colocación reales; G2/visual/G4 aporta expresión, interacción, accesibilidad renderizada, dispositivos, impresión/escaneo y participantes. Esas aportaciones no están comprobadas por documentación. No hay declaración de cero errores globales, validación UX/software/alimentaria/cumplimiento, implementación, configuración, merge, cierre, cambio de decisiones aprobadas ni mensaje a otro chat. Historial, evidencia preliminar y trabajo G2 conservados; informes y continuidad personal permanecen fuera de Git.

'''
replace_once('## Historial conservado — sin autoridad operativa', section + '## Historial conservado — sin autoridad operativa')
assert text.split('## Historial conservado — sin autoridad operativa', 1)[1] == before.split('## Historial conservado — sin autoridad operativa', 1)[1]
assert handoff_path.read_bytes() == before_bytes, 'Concurrent HANDOFF edit; reread before updating'
handoff_path.write_bytes(text.encode('utf-8'))
(folder / 'handoff-continuity.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True), text.splitlines(True), fromfile='HANDOFF-before-FO-return', tofile='HANDOFF-after-FO-return')), encoding='utf-8')

broken = []
for path in [folder / 'g1-review.md', folder / 'g4-review.md', folder / 'review-result.md', handoff_path]:
    for match in re.finditer(r'\[[^\]]*\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
        target = match.group(1).strip('<>').split('#', 1)[0]
        if not target or re.match(r'^[a-z]+://', target):
            continue
        resolved = path.parent / target
        if target.endswith('final-state-checks.json') and resolved.resolve() == (folder / 'final-state-checks.json').resolve():
            continue
        if not resolved.exists():
            broken.append({'source': str(path), 'target': target})
assert not broken, broken
assert old_evidence == {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in prelim.iterdir() if p.is_file()}
assert command('git', 'rev-parse', 'HEAD') == commit
assert not command('git', 'status', '--porcelain')
checks = {'date': '2026-10-02', 'baseline': commit, 'head_upstream_match': True, 'pr': pr, 'issues': issues, 'checkout_clean_before_after': True, 'fo_git_snapshot_sha256': sha, 'local_report_handoff_links_valid': True, 'preliminary_evidence_unchanged': True, 'historical_handoff_section_unchanged': True, 'handoff_before_sha256': hashlib.sha256(before_bytes).hexdigest(), 'handoff_after_sha256': hashlib.sha256(handoff_path.read_bytes()).hexdigest(), 'outcome': 'No required documentary correction in described final FO branches; M1 open; actual UX/food/files/print/QR/software evidence pending', 'tracker_mutations_or_external_messages': False}
(folder / 'final-state-checks.json').write_text(json.dumps(checks, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'reports': ['g1-review.md', 'g4-review.md', 'review-result.md'], 'handoff': str(handoff_path), 'baseline': commit, 'local_links_valid': True, 'preliminary_preserved': True, 'checkout_clean': True}, ensure_ascii=False))
