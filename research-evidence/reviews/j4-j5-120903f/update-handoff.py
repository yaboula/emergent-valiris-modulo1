from pathlib import Path
p=Path(r'D:\the next level\HANDOFF.md')
raw=p.read_bytes();s=raw.decode('utf-8')
marker='### Revisión paralela G1 y G4 de C1–C3'
active,history=s.split(marker,1)
changes={
 'Siguiente revisión independiente: J4–J5 en 120903f.':'J4–J5 revisado documentalmente por G1/G4 en 120903f, sin corrección requerida. Siguiente bloque pendiente: J6–J7, tras entrega de G2.',
 'J4–J5 y demás evidencias pendientes antes del cierre de M1':'J4–J5 revisado documentalmente por G1/G4 en 120903f, sin corrección requerida; J6–J7 y demás evidencias pendientes antes del cierre de M1',
 'Durante esa revisión G2 entregó J4–J5 en 120903f; queda pendiente su revisión independiente.':'Durante esa revisión G2 entregó J4–J5 en 120903f; ahora revisado documentalmente por G1/G4, sin corrección requerida.',
 'Siguiente revisión independiente pendiente: J4–J5 en 120903f;':'J4–J5 también revisado documentalmente por G1/G4 en 120903f, sin corrección requerida;',
 'J4–J5 programación/excepciones/continuidad entregado por G2 en 120903f y pendiente de revisión independiente.':'J4–J5 programación/excepciones/continuidad entregado por G2 y revisado documentalmente por G1/G4 en 120903f, sin corrección requerida.',
 'G1 coordina la siguiente revisión independiente de J4–J5':'G1 coordina la revisión independiente de J6–J7 cuando G2 entregue un commit revisable',
 'siguen pendientes la revisión independiente de J4–J5 y contratos/evidencias':'siguen pendientes J6–J7, contratos y evidencias',
 'G4 revisó C1–C3, J10–J15, CP, J8–J9 y PV/J1–J2 documentalmente.':'G4 revisó C1–C3, J10–J15, CP, J8–J9, PV/J1–J2 y J4–J5 documentalmente.',
 'J4–J5 diseñado y comprobado documentalmente por G2; revisión independiente JT pendiente.':'J4–J5 diseñado por G2 y revisado documentalmente por G1/G4 en 120903f, sin corrección requerida.',
 'PV/J1–J2 conserva revisión independiente pendiente hasta un retorno real.':'PV/J1–J2 revisado documentalmente por G1/G4 en 9cfe77b, sin corrección requerida; dictamen disponible debajo y en research-evidence/reviews/j1-j2-9cfe77b.',
}
for old,new in changes.items():
    assert active.count(old)==1,(old,active.count(old))
    active=active.replace(old,new,1)
s=active+marker+history
old='**Siguiente revisión independiente pendiente: J4–J5, programación y continuidad de servicio, entregado en 120903f.**'
assert s.count(old)==1
s=s.replace(old,'**Siguiente revisión en el momento del dictamen PV: J4–J5, programación y continuidad de servicio, entregado en 120903f.** El dictamen posterior JT figura debajo.',1)
section='''### Revisión paralela G1/G4 de J4–J5 — 2 de octubre de 2026

**J4–J5 revisado documentalmente en 120903f138a798e957b26498f2a3efb5d5e6521a, sin corrección requerida en las ramas escritas contrastadas.** G1 —único PM y Dirección/Producto unidos— consolida con revisión independiente G4. Leídos documento completo de 394 líneas,21 estados,ocho criterios originales,20 contribuciones de capacidades,seis TW y30 TC. Guardado/programación/ejecución/publicación/vigencia separados; revisión de fuente/dependencias cambiadas; cancelación/sustitución conocida frente a incierta; excepción con ámbito/final y reglas actuales; agotado reciente conservado ante publicación del mismo servicio; revisión del siguiente servicio; urgencia/corrección por grupo e historial alimentario/idiomas sin restauraciones colaterales. No aparece contradicción material ni regresión reproducible en contratos previos afectados. No se necesita decisión nueva del fundador para este dictamen.

Evidencia fuera de Git: [dictamen consolidado](research-evidence/reviews/j4-j5-120903f/review-result.md), [G1](research-evidence/reviews/j4-j5-120903f/g1-review.md), [G4 independiente](research-evidence/reviews/j4-j5-120903f/g4-review.md), [comprobaciones](research-evidence/reviews/j4-j5-120903f/document-checks.json), checker y snapshots JT/criterios/matriz en esa carpeta.36 enlaces locales/internos JT contra Git congelado;21 fichas únicas/ocho mapeos/20 filas/30 TC/seis TW/tres TF.122 filas previas de contraste,criterios originales/matriz/definición/ADR-0005/0008–0012 preservados frente a9cfe77b.72 padres/36–30–6 intactos; whitespace limpio. Hash JT66903175d2a9b370369bbb45fa77f77ef892bc5659a03ced62b63132bc04fb22.

**Siguiente bloque descriptivo y posterior revisión independiente: J6–J7, registro alimentario mantenido/personal y salidas carta/impresión/QR, cuando G2 entregue versión revisable.** No se da por entregado ni revisado. Política X06 de programación privada hasta ejecución confirmada frente a publicación futura expresa sigue propuesta para G1/G3; G1 recomienda conservar esa distinción al especificar, sin nuevo ADR aceptado. Contratos en M2/#4: identidades/grupos/fuentes/resultados,permisos/revocación,concurrencia de disponibilidad/dependencias,ejecución/cancelación/recurrencias/finales,zona horaria/DST/noche/frescura y ejecución perdida. G5/G2 aporta periodos/excepciones/políticas/materiales/fuentes y formación reales; G2/diseñador visual/G4 interacción,accesibilidad renderizada,dispositivos/usuarios,límites de servicio,pantallas y papel colocado. Descripciones no validan estos resultados.

M1/#5 y PR#21 OPEN/draft; #4 conserva contratos. Sin modificación de fuentes/Git/trackers/configuración,implementación,merge,cierre M1 o mensaje a otro chat por G1/G4. HANDOFF e informes personales actualizados fuera de Git; historial,fuentes y decisiones aprobadas conservados. Conteo de documentos/estados no implica porcentaje global de producto completado.

'''
hm='## Historial conservado — sin autoridad operativa'
assert s.count(hm)==1
s=s.replace(hm,section+hm,1)
assert p.read_bytes()==raw,'Concurrent HANDOFF edit; retry current version'
p.write_bytes(s.encode('utf-8'))
print('HANDOFF updated')
