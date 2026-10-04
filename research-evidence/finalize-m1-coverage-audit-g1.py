from pathlib import Path
import subprocess, json, hashlib, re, difflib

root = Path(r'D:\the next level')
repo = root / 'valiris-restaurants'
folder = root / 'research-evidence/reviews/coverage-d71d3de'
base = 'd71d3de81d611b76d2d80aab86ead119b34b0a0d'
def command(*args):
    return subprocess.check_output(args, cwd=repo).decode('utf-8').strip()
assert command('git', 'rev-parse', 'HEAD') == base
assert command('git', 'rev-parse', '@{upstream}') == base
assert not command('git', 'status', '--porcelain')
pr = json.loads(command('gh', 'pr', 'view', '21', '--json', 'state,isDraft,headRefOid,url'))
issues = [json.loads(command('gh', 'issue', 'view', str(n), '--json', 'number,state,url')) for n in (5, 4)]
assert pr['headRefOid'] == base and pr['state'] == 'OPEN' and pr['isDraft']
assert all(i['state'] == 'OPEN' for i in issues)
for file in ('g1-review.md', 'g4-review.md', 'review-result.md'):
    s = (folder / file).read_text(encoding='utf-8')
    assert base in s and 'No required documentary correction' in s or base in s and 'no required documentary correction' in s
old_folders = [root / 'research-evidence/reviews/j6-j7-a0583e0', root / 'research-evidence/reviews/j6-j7-preliminary-b63b454']
old_hashes = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for f in old_folders for p in f.iterdir() if p.is_file()}
handoff = root / 'HANDOFF.md'
before_bytes = handoff.read_bytes()
before = before_bytes.decode('utf-8')
s = before
def replace_once(old, new):
    global s
    assert s.count(old) == 1, (old, s.count(old))
    s = s.replace(old, new, 1)
replace_once('La consolidación nueva aún requiere revisión independiente;', 'La consolidación nueva fue auditada documentalmente por G1/G4 en ese commit, sin correcciones obligatorias reproducidas; CG11 completa solo esa lectura agregada y conserva sus obligaciones de cierre/evidencia;')
replace_once('Siguiente trabajo: consolidar cobertura/huecos y preparar el plan concreto de expresión visual, interacción y evidencias.', 'Consolidación de cobertura/huecos y plan auditados documentalmente por G1/G4 en d71d3de. Siguiente trabajo G2: identidad, plantillas/diseño propio y composiciones públicas/de gestión C1–C3 con guiones de interacción y evidencia, conservando las dependencias pendientes.')
replace_once('HEAD a0583e0ec04e310f6736f1d763ca4d7a78191973, subida y limpia/sincronizada', 'HEAD d71d3de81d611b76d2d80aab86ead119b34b0a0d, subida y limpia/sincronizada')
replace_once('Revisión de la consolidación nueva pendiente CG11; autor y calidad independientes siguen separados.', 'Estado en la entrega: revisión de la consolidación nueva pendiente CG11. Estado posterior: G1/G4 completaron la auditoría documental del agregado d71d3de según el dictamen enlazado debajo, sin corrección obligatoria; sus evidencias de cierre M1 siguen pendientes. Autor y calidad independientes conservan sus registros separados.')
replace_once('**Orden vigente y siguiente encargo G2 bajo #5:** consolidar transversalmente', '**Orden tras el dictamen FO — sustituido por la consolidación y su auditoría debajo — bajo #5:** consolidar transversalmente')
section = '''### Auditoría profunda G1/G4 de consolidación M1 — 2 de octubre de 2026

**Dictamen: sin correcciones documentales obligatorias reproducidas en d71d3de81d611b76d2d80aab86ead119b34b0a0d.** G1, único PM y Dirección/Producto unidos, consolida; G4 aporta auditoría independiente. Leídos mapa individual de72 padres,59 criterios/correspondencias, RV01–RV07,17 entradas CG y encargo siguiente, contra fuentes aceptadas y cuerpos pertinentes. La distinción69 recorridos escritos suficientes/tres contribuciones visuales parciales es sostenible solo como juicio documental limitado: no son69 capacidades entregadas ni quedan solo tres tareas. B1.05 identidad/B1.06 plantillas/B1.07 diseño propio mantienen CG01–CG03 pendientes. Precios/contexto, publicación/borradores/urgencias, fuente compartida/permisos/recuperación, alimentación/idiomas/nutrición, papel/QR/hosting, cuentas/offline y eventos/resultados fueron contrastados transversalmente sin reproducir contradicción obligatoria.

Evidencia fuera de Git: [retorno consolidado](research-evidence/reviews/coverage-d71d3de/review-result.md), [G1](research-evidence/reviews/coverage-d71d3de/g1-review.md), [G4 independiente](research-evidence/reviews/coverage-d71d3de/g4-review.md), [integridad G1](research-evidence/reviews/coverage-d71d3de/document-checks.json), [comprobación propia G4](research-evidence/reviews/coverage-d71d3de/g4-structural-checks.json) y [estado final](research-evidence/reviews/coverage-d71d3de/final-state-checks.json); snapshots exactos/manifest de referencias en la misma carpeta.1.809 enlaces en18 docs Git congelados;357 enlaces de etiquetas de contraste comprobados contra casos únicos reales del destino, además del fragmento;161 cuerpos de fichas/176 filas anteriores preservados;72 nombres/tratamientos36–30–6,59 criterios y fuentes/ADRs intactos. Esto no es ejecución independiente nueva de los176 casos ni prueba de producto. Historial/evidencia autor y retornos previos conservados.

**Orden vigente G2 / M1 #5:** continuar el encargo existente de composición e interacción representativas: CG01–CG03 con C1 sin fotos y C2/C3, identidad/plantilla/diseño propio, mantenimiento autónomo y controles de contenido/marca separados de composición Valiris; composiciones públicas/de gestión y guiones con inicio/reset/fuente/acción/resultado/error/recuperación/evidencia requerida. Después aplicar esa dirección a A4/diario/personal/pantalla/QR, locales/accesibilidad y las capacidades aceptadas de cuenta/comparación/vídeo/nutrición/conexiones/medición/mantenimiento. Static/interactivo y lo no probado deben quedar identificados. Reutilizar mapa/backlog; orden por riesgos no pospone capacidades.

La lectura agregada independiente de CG11 queda completada a este commit; CG11 conserva evidencias de cierre y todos los requisitos CG05/CG07/CG08 y demás entradas no cumplidas. G1 consolida; diseño visual colabora con recorridos/contenido; G4 mantiene revisión independiente posterior. G3/G1 conserva contratos bajo M2/#4, G5/G2 fuentes/materiales/idiomas/alimentos/URLs/dispositivos/participantes autorizados y G6 preguntas concretas de descubrimiento/servicio/D3. Responsabilidades no acreditan disponibilidad ni consultas realizadas. No hay pregunta nueva material para el fundador.

PR #21 OPEN/draft, M1/#5 y M2/#4 OPEN; HEAD local/upstream/PR coincidentes y checkout limpio. Sin modificar fuente/configuración/decisiones aprobadas/Git/trackers, merge/cierre, implementación/prototipo o mensajes externos. Markdown continúa como medio acordado; no se declara auditoría de pantalla, UX/accesibilidad renderizada, fuente alimentaria, conexión funcionando, impresión/escaneo ni uso real. Esas evidencias siguen pendientes; M0 no se reabre y M1 permanece abierto.

'''
replace_once('## Historial conservado — sin autoridad operativa', section + '## Historial conservado — sin autoridad operativa')
assert s.split('## Historial conservado — sin autoridad operativa', 1)[1] == before.split('## Historial conservado — sin autoridad operativa', 1)[1]
assert handoff.read_bytes() == before_bytes, 'HANDOFF edited concurrently; reread first'
handoff.write_bytes(s.encode('utf-8'))
(folder / 'handoff-continuity.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True), s.splitlines(True), fromfile='HANDOFF-before-aggregate-return', tofile='HANDOFF-after-aggregate-return')), encoding='utf-8')

broken = []
targets = [folder / f for f in ('g1-review.md', 'g4-review.md', 'review-result.md')] + [handoff]
for path in targets:
    for ref in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
        ref = ref.strip('<>').split('#')[0]
        if not ref or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', ref):
            continue
        dest = (path.parent / ref).resolve()
        if dest == (folder / 'final-state-checks.json').resolve():
            continue
        if not dest.exists():
            broken.append({'source': str(path), 'target': ref})
assert not broken, broken
assert old_hashes == {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for f in old_folders for p in f.iterdir() if p.is_file()}
assert command('git', 'rev-parse', 'HEAD') == base and not command('git', 'status', '--porcelain')
checks = {'date': '2026-10-02', 'baseline': base, 'head_upstream_pr_match': True, 'checkout_clean_before_after': True, 'pr': pr, 'issues': issues, 'local_report_handoff_links_valid': True, 'old_fo_final_and_preliminary_evidence_unchanged': True, 'historical_handoff_section_unchanged': True, 'handoff_before_sha256': hashlib.sha256(before_bytes).hexdigest(), 'handoff_after_sha256': hashlib.sha256(handoff.read_bytes()).hexdigest(), 'report_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in targets if p != handoff}, 'disposition': 'No required documentary correction reproduced; new aggregate reading complete; original M1 actual evidence and closure remain pending', 'tracker_mutations_or_external_messages': False}
(folder / 'final-state-checks.json').write_text(json.dumps(checks, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: v for k,v in checks.items() if 'sha256' not in k}, ensure_ascii=False))
