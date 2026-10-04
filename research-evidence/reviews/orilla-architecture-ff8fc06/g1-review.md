# G1 — Recepción y revisión acotada de arquitectura ORILLA v0.2

4 de octubre de 2026 · Fuente congelada: `ff8fc061dfb4e63461ee2b77b5a18f02108edb6b`, [PR #33](https://github.com/yaboula/valiris-restaurants/pull/33), OPEN/draft sobre #32. G1 es el PM; este registro no es revisión independiente G4.

## Dictamen operativo

La arquitectura preliminar es una entrada utilizable para desarrollar contenido y explorar composición. En la lectura acotada no se reprodujo una contradicción material que obligue a detener ese avance. No se acepta como arquitectura final, caso completo, aplicación aprobada ni cierre del contrato amplio/M1. La estructura y sus etiquetas permanecen propuestas revisables con contenido real del caso y aportaciones especializadas.

Se conservan dos destinos principales, presentación expresiva y carta separada; Ver carta directo y consulta sin cuenta. Los bloques de cocina, personas/lugar y visita son destinos enlazables dentro de la presentación, no páginas obligatorias. Detalle y recuperación mantienen su intención contextual. Las 72 capacidades no se convierten en 72 opciones de navegación; los controles dependen del contenido y configuración pertinentes.

## Lectura y comprobaciones

Leídos completos la arquitectura, README del autor, CR/XR, contrastes y adaptación metodológica; inspeccionados el verificador y resultados/manifiesto publicados. Se contrastaron con el caso común inicial y los contratos vigentes: fuente única, dueño de datos, ficción autorizada, PC/adaptación teléfono, dirección seleccionada y límites de estado/comprobación. Se revisaron entradas/retornos, formato/precio/contexto, falta de información frente a cierre y declaraciones alimentarias positivas junto a pendientes. No se repitió una auditoría exhaustiva de todos los recorridos ni una revisión visual de las referencias.

G1 reprodujo el verificador del autor sobre su checkout limpio en la fuente congelada, desviando únicamente sus dos escrituras JSON a la caché del checkout de G1. Los resultados coinciden byte a byte con la evidencia publicada; el checkout del autor quedó limpio. Resultado: 78 enlaces locales/fragmentos, 17 tablas, siete destinos, seis recorridos, siete solicitudes y cuatro retornos; 33 registros de fuentes y cuatro archivos originales del método contrastados. Se conservaron las primeras 22 filas de contraste; ahora son 26 contrastes documentales, no 26 pruebas con usuarios. Ledger intacto: 72 padres únicos, 36 incluidas, 30 configurables y seis dependientes de conexión.

GitHub leído el 4 de octubre: #33 OPEN/draft en ff8fc06, sin reviews/comentarios/checks en la respuesta consultada; #5, #4 y #15 OPEN. No se sincronizó Linear ni se infirió disponibilidad de especialistas de estos estados.

## Observaciones y adopción

- El título de `content-requests.md` conserva «IA v0.1» aunque la entrega es v0.2. Sus IDs y baseline son coherentes; es un residuo editorial sin bloqueo. G2.02 puede aclararlo en su siguiente revisión propia; G1 conserva la fuente congelada sin editar sus entregables.
- Las expresiones «no fake portraits» y «no fabricated specials/bestsellers» se entienden bajo la autorización vigente: se permite crear personas y platos de ficción coherente y representaciones conceptuales identificadas; no se permite atribuirlos como reales ni fingir evidencia de ventas, popularidad o experiencia observada. No se impone una prohibición nueva al desarrollo del caso.
- Rampstack es un método adaptado declarado por el autor, no una aprobación de plantilla, sitemap, umbral de clics o calidad UX. Se conservó la primera propuesta; no hay motivo para reiniciar por adoptar el método.
- 1440/390 son lienzos de contraste propuestos; no breakpoints comprometidos. Rutas/anchors ilustrativos tampoco son configuración o decisiones canónicas aceptadas.

## Próximo ciclo y responsables

| Responsable | Trabajo y efecto pendiente |
| --- | --- |
| G2.04 | Desarrollar una primera versión coherente del caso y copy situado, responder CR01–CR07 y XR01 por ID/SHA. Historia/personas, gastronomía/ambiente, carta/precios/variantes, visita y escenarios siguen sin producir; no basta un esquema de campos. |
| SEO/GEO | Trabajar en ese ciclo sobre la misma fuente: XR02, preguntas/etiquetas, contenido enlazable y recomendaciones editoriales. Consecuencias de rutas/idiomas/canonical/entrega se devuelven a G3/M2; no configurar ni prometer ranking. Aportación pendiente, no enviada/activada por este registro. |
| G2.02 | Adoptar explícitamente el nuevo SHA de caso/copy, resolver solicitudes recibidas y ajustar estructura/etiquetas. Conserva sus archivos; no se cierra su contrato amplio con esta recepción. |
| G2.07 / G2.03 | Explorar ya estructura conocida con vacíos visibles. La composición representativa depende del caso/copy; XR03 y XR04 siguen pendientes. PC primero y adaptación deliberada a teléfono. No se presume activación por esta revisión. |
| G2.08 / G2.06 | Recursos desde necesidades situadas de composición y contenido; revisión de coherencia. Ninguna biblioteca completa ni nueva selección visual exigida ahora. |
| G1 / G4 | G1 coordina discrepancias e integración; G4 conserva revisión independiente de aplicaciones. No se recibió dictamen G4 de #33 y #30 solo cubre la selección conceptual previa. |

Los mensajes de arranque de G2.04 y SEO/GEO se preparan en sus contratos existentes; no se envían a otros chats ni se activan por guardarlos. La referencia inicial de arquitectura se congela en ff8fc06. La futura ejecución adopta el HEAD publicado del traspaso de G1 que contiene esta actualización, en ramas/worktrees propios, y congela ese SHA antes de editar. Dependencia directa #33; no main mientras siga sin integrar.

No se fusionó ninguna PR, se cerró ningún resultado ni se cambió una decisión del fundador. No se acredita comprensión, accesibilidad renderizada, interacción, validación con usuarios, alimento verificado, descubrimiento en vivo, derechos de recursos o software probado. [Comprobaciones reproducidas y alcance](checks.json).
