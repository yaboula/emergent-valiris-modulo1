from pathlib import Path
import hashlib

p = Path(r'D:\the next level\HANDOFF.md')
raw = p.read_bytes()
s = raw.decode('utf-8')
marker = '### Revisión paralela G1 y G4 de C1–C3'
active, history = s.split(marker,1)
replacements = {
    'Siguiente revisión independiente: PV/J1–J2.': 'PV/J1–J2 revisado documentalmente por G1/G4 en 9cfe77b, sin corrección requerida. Siguiente revisión independiente: J4–J5 en 120903f.',
    'PV/J1–J2 y demás evidencias pendientes antes del cierre de M1': 'PV/J1–J2 revisado documentalmente por G1/G4 en 9cfe77b, sin corrección requerida; J4–J5 y demás evidencias pendientes antes del cierre de M1',
    'HEAD 9cfe77ba652d8b22b412f69a93d24987a9201098, subida y limpia/sincronizada': 'HEAD 120903f138a798e957b26498f2a3efb5d5e6521a, subida y limpia/sincronizada al último readback de esta revisión',
    'PV sigue pendiente de revisión independiente.': 'PV revisado documentalmente por G1/G4 en 9cfe77b, sin corrección requerida. Durante esa revisión G2 entregó J4–J5 en 120903f; queda pendiente su revisión independiente.',
    'PV sigue pendiente de revisión independiente/contratos/entradas y pruebas reales;': 'PV revisado documentalmente por G1/G4 en 9cfe77b, sin corrección requerida; contratos/entradas y pruebas reales siguen pendientes;',
    'Siguiente revisión independiente pendiente: PV/J1–J2;': 'PV/J1–J2 ya revisado documentalmente por G1/G4 en 9cfe77b, sin corrección requerida. Siguiente revisión independiente pendiente: J4–J5 en 120903f;',
    'descubrimiento/destinos/fuentes, revisión PV y expresión/interacción': 'descubrimiento/destinos/fuentes y expresión/interacción',
    'Siguiente bloque descriptivo: J4–J5 programación/excepciones/continuidad, después J6–J7 registro alimentario/personal/salidas;': 'J4–J5 programación/excepciones/continuidad entregado por G2 en 120903f y pendiente de revisión independiente. Siguiente bloque descriptivo: J6–J7 registro alimentario/personal/salidas;',
    'G1 coordina la siguiente revisión independiente de PV/J1–J2': 'G1 coordina la siguiente revisión independiente de J4–J5',
    'CP y J8–J9 están revisados documentalmente por G1/G4; siguen pendientes la revisión independiente de PV/J1–J2 y contratos/evidencias': 'CP, J8–J9 y PV/J1–J2 están revisados documentalmente por G1/G4; siguen pendientes la revisión independiente de J4–J5 y contratos/evidencias',
    'G4 revisó C1–C3, J10–J15, CP y J8–J9 documentalmente.': 'G4 revisó C1–C3, J10–J15, CP, J8–J9 y PV/J1–J2 documentalmente.',
}
for old,new in replacements.items():
    assert active.count(old) == 1, (old,active.count(old))
    active = active.replace(old,new,1)
s = active + marker + history
s = s.replace('**Siguiente revisión independiente: PV/J1–J2, presencia pública, consulta, destacados y maridajes dirigidos, ya entregado por G2.**', '**Siguiente revisión en el momento del dictamen J8–J9: PV/J1–J2, presencia pública, consulta, destacados y maridajes dirigidos, ya entregado por G2.** El dictamen posterior PV figura debajo.',1)
section = '''### Revisión paralela G1/G4 de PV/J1–J2 — 2 de octubre de 2026

**PV/J1–J2 revisado documentalmente en 9cfe77ba652d8b22b412f69a93d24987a9201098, sin corrección requerida en las ramas escritas contrastadas.** G1 —único PM y Dirección/Producto unidos— consolida con revisión independiente G4. Leídos los 17 estados completos, 11 criterios originales, 23 capacidades afectadas, seis recorridos y 26 contrastes. Coherentes entrada anónima, horarios local/cocina y oferta publicada prevista, precios/contextos/formatos/condiciones, búsqueda/filtros e información incompleta, detalle/retorno, destacados y maridajes dirigidos, idiomas/fallback, enlaces cambiados/preview externo, lectura offline y publicación/recuperación autorizada. No se reproduce regresión documental de G4-01 ni G4-J15-01; ninguna nueva decisión del fundador es necesaria para continuar.

Evidencia fuera de Git: [dictamen consolidado](research-evidence/reviews/j1-j2-9cfe77b/review-result.md), [G1](research-evidence/reviews/j1-j2-9cfe77b/g1-review.md), [G4 independiente](research-evidence/reviews/j1-j2-9cfe77b/g4-review.md), [comprobaciones](research-evidence/reviews/j1-j2-9cfe77b/document-checks.json), checker y snapshots PV/criterios/matriz en esa carpeta. 32 ocurrencias locales/internas PV verificadas contra Git congelado; 17 fichas únicas/11 mapeos/23 filas/26 VC/seis VW/cuatro VF. Fichas idénticas a c5e0a5b; criterios originales/matriz/definición/ADR aceptados preservados. Se conservan 72 padres y 36/30/6. Hash PV db1a922be8bb42150e9089fe2adf152a17e4d7937100732d554150e7dea01ece.

Durante esta revisión G2 añadió y subió J4–J5 y referencias en 120903f138a798e957b26498f2a3efb5d5e6521a. Trabajo concurrente conservado; PV no cambia. Último readback: checkout limpio, HEAD local y PR #21 coincidentes en 120903f, PR OPEN/draft y #5/#4 OPEN. El JSON conserva el estado intermedio con cambios ajenos, sin convertirlo retroactivamente en limpio. G1/G4 no editaron ni integraron esos documentos.

**Siguiente revisión independiente pendiente: J4–J5, programación y continuidad de servicio, entregado en 120903f.** G1 consolida y G4 revisa independientemente; este dictamen no acepta el nuevo bloque. La secuencia de G2 continúa J6–J7 registro/personal/impresión/QR. G3/G1 conserva contratos M2/#4 de identidades/contextos/fuentes/horarios/excepciones/grupos/resultados/permisos/resolución pública; G5/G2 material real/destinos/derechos/traducciones; G6 aportaciones concretas de descubrimiento; G2/diseñador visual/G4 interacción, accesibilidad renderizada, dispositivos y participantes. No hay validación UX/software/servicio/seguridad/SEO, cambio de alcance, configuración, merge, cierre M1 ni mensaje a otro chat. Historial, decisiones aceptadas e informes anteriores permanecen disponibles.

'''
history_marker = '## Historial conservado — sin autoridad operativa'
assert s.count(history_marker) == 1
s = s.replace(history_marker,section+history_marker,1)
assert p.read_bytes() == raw, 'Concurrent HANDOFF edit; retry from current source'
p.write_bytes(s.encode('utf-8'))
print('HANDOFF updated; original SHA256 '+hashlib.sha256(raw).hexdigest())
