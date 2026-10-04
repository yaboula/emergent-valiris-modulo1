# G1 — Recepción conjunta de contenido 1.1 y arquitectura v0.3

4 de octubre de 2026 · G1, único PM · Lectura documental y coordinación; no revisión independiente G4.

## Fuentes exactas y resultado

| Fuente / autor | Versión congelada | Estado real y uso |
| --- | --- | --- |
| G2.04 / [#39](https://github.com/yaboula/valiris-restaurants/pull/39) | CASE/COPY **1.1 juntos en `4b382bebe5d5c6cad21a7edcaffab053c433a0e9`**; HEAD de evidencia `d9ef8c9bc90f77de8d38dd14b1664d8384d4dea4` | [Caso](../../../docs/design/orilla-case.md), [copy](../../../docs/design/m1-storefront-content-and-copy.md), [resoluciones](../../g2-04-storefront/seo-consolidation-1.1/resolutions.md) y [entrega](../../g2-04-storefront/seo-consolidation-1.1/delivery.md). R01–R08 aceptadas editorialmente por su propietario, no aprobación conjunta. |
| G2.02 / [#40](https://github.com/yaboula/valiris-restaurants/pull/40) | IA **v0.3 en `ba44c6809516d8d078d192f5f6a423b12cd8b673`** | [Arquitectura](../../../docs/design/m1-storefront-information-architecture.md), [adopción](../../g2-02-storefront/adoption.md) y [CR/XR](../../g2-02-storefront/content-requests.md). Adopta CASE/COPY **1.0**, no 1.1, y SEO #37. |
| SEO/GEO / #37 | `0c17480bdc2b6ff8037022228ebc4599a704e702` | [Revisión aplicada](../../../docs/design/m1-storefront-discovery-content.md). Respuestas XR02/Q01–Q05 y R/T sobre 1.0; relectura de nuevas versiones pendiente. |
| G1 / #38 | `b30dada1ac8fa5be01d07092ec6c7dbfe80a0439` | Baseline común de ambas continuaciones; no integración en main. |

**Dictamen:** ambas entregas son utilizables para composición representativa. No se reprodujo contradicción material bloqueante en el cruce de los cambios editoriales con las relaciones y destinos de IA v0.3. Hay una diferencia explícita de versión consumida: G2.02 adoptó 1.0 mientras G2.04 ya entregó 1.1. Se resuelve mediante adopción/relectura acotadas, sin rehacer el caso o la arquitectura.

Paquete operativo para UI: **CASE/COPY 1.1 como única fuente vigente de contenido + IA v0.3 como estructura**, con el contraste G1 por IDs de este registro. Este permiso de composición preliminar no afirma que G2.02 haya adoptado 1.1 ni que SEO haya releído las nuevas versiones. Las notas de 1.0 y enlaces relativos de los documentos de autor conservan su procedencia; en este checkout los enlaces a contenido abren 1.1. Para reproducir la lectura del autor, usar su SHA congelado; para componer ahora, usar el par completo 1.1, sin mezclar textos de 1.0.

## Comprobaciones y conservación

Leídos los cambios completos de CASE/COPY, resoluciones y diez contrastes 1.1, así como IA v0.3, adopción/CR-XR y 18 contrastes nuevos; reutilizadas las lecturas de fuentes previas intactas. Inspeccionados ambos verificadores y ejecutados en sus respectivos checkouts limpios, desviando solo sus dos escrituras de resultados a caché G1. Los cuatro JSON reproducidos coinciden byte a byte con sus publicados. Los checkouts y ramas de los autores no se modificaron.

Contenido: 61 registros fuente y seis evidencias 1.0 preservados; 83 IDs de copy conservados, seis revisados y 11 nuevos (94 total), 30 estados y 11 entradas de escenario. Se conserva historia/personas/platos/recetas/precios/horarios; SCENARIO-06 pasa a revisión 2 por fecha explícita en su texto, sin cambiar el servicio. 32 enlaces/fragmentos y 31 tablas comprobados por el autor y reproducidos.

Arquitectura: 42 registros de fuente, 60 enlaces/fragmentos, siete destinos y seis recorridos; 26 contrastes históricos preservados y 18 nuevos. CR01–CR04 aceptados, CR05–CR07 parciales; XR01 ajustado/aceptado, XR02 recibido/adoptado dentro de IA, XR03/XR04 pendientes. Sus doce resoluciones SEO son resultados arquitectónicos, no aceptación global; R01/R10/R11/R12 mantienen aspectos pendientes. Las 72 capacidades y decisiones originales siguen intactas.

Las PRs #39 y #40 permanecen OPEN/draft sobre #38. HEAD #39 avanza del par 4b382be a d9ef8c9 únicamente por evidencia; sus dos blobs coinciden. #35/#33 siguen preservadas. #5/#4/#15 OPEN al readback de esta recepción; Linear no se ha vuelto a consultar ni modificar. [Comprobaciones y límites](checks.json).

G1 reúne ambas ramas en **su propia** `docs/m1-g1-orilla-joint-handoff`: merge local de ba44c68 sobre d9ef8c9, sin conflictos ni rutas de entrega solapadas, preservando los 17 archivos de ambas contribuciones exactamente. Commit de reunión `6064648a08a15f7604d099b406e7dd8439aeb333`. No merge de PR/main ni modificación de ramas ajenas. La PR de este traspaso se apila sobre #39 y declara #40 como dependencia paralela que debe conservarse al integrar; no se presume ninguna PR fusionada.

## Contraste de versiones para uso situado

| Cambio 1.0 → 1.1 | Cruce con IA v0.3 / resultado documental | Incorporación pendiente |
| --- | --- | --- |
| C01–C04 / M01-03: título completo y salto compacto aceptados | Coinciden exactamente con los cuatro mapeos IA §2; arroz sigue C02, espresso C04. No página, categoría o identidad nueva. | G2.02 registra fuente 1.1; UI comprueba orientación/lectura. |
| H03-09: La historia de ORILLA en enlace aislado | IA ya distingue ese enlace de Nuestra mesa con introducción. Mismo H03, relato completo y omisión de salto si falta el bloque. | Añadir referencia al nuevo ID en adopción/paquete UI; G2.03 aplica expansión/foco/retorno. |
| H02-07 y E03: enlace con nombre actual de producto/variante | IA conserva variante/formato, nombre completo, oferta y origen; no sustitución por V01 ni un precio desnudo. | UI aplica asociación visible/accesible con G2.03; SEO relee R03/R07/R08. |
| S10 / SCENARIO-06 revisión 2: domingo 4 de octubre de 2026 | Compatible con IA-J02/CA09: cocina 13:30–15:30, local sin cambio; ya exige fecha/alcance. No nuevo horario ni estado. | G2.02 adopta revisión 2; UI mantiene fecha en PC/teléfono/entrada directa. |
| S11/S14/S18: Horarios y visita en recuperación | Coincide con H04/retornos de IA; destino solo si conocido y válido. Incertidumbre no equivale a cerrado/retirado. | Referencias de copy actualizado y comportamiento aplicado. |
| E01–E03: contexto visible de entradas directas | IA exige identidad/ficción y tarea directa sin pasar antes por Home; Menu/Detalle mantienen límites alimentarios. | UI compone cada entrada y retorno, con fuentes y estados identificados. |
| META-01–07: ficción literal por destino/estado | Cumplen la distinción editorial de ficción/idioma/retirada/desconocido. No precio/stock actual en los resúmenes por defecto, ni datos privados. IA deja los literales a G2.04. | Relectura SEO; entrega técnica/preview T03/T04/T08 aún en M2. No metadatos implementados. |

Este contraste no sustituye revisión SEO, lingüística, visual o de comportamiento. No exige otra investigación de mercado, menú más grande, nuevos destinos o un reinicio. Los textos heredados no revisados siguen en su fuente; los seis cambios y 11 IDs nuevos se consumen siempre del par 1.1 completo.

## Próximos retornos y baseline

- **SEO/GEO:** relectura acotada de 1.1 (R01–R08, seis IDs revisados/11 nuevos, categorías y excepción) y de las adopciones R02/R04/R05/R09 de IA v0.3. Registrar fuente/localización/resultado y corrección si procede. No repetir auditoría general ni afirmar ranking/rastreo/usuarios.
- **G2.02:** adoptar explícitamente el par 1.1 comparando esta matriz y revisar las referencias/paquete UI/CR-XR afectados. Mantener destinos/recorridos donde no haya razón de cambio; registrar cualquier discrepancia. Su v0.3/ba44c68 queda como fuente de esta recepción.
- **G2.07 con G2.03:** puede empezar o continuar la composición con este paquete, **PC primero y adaptación deliberada a teléfono**. Seis checkpoints R10 con contenido actual, entradas/retornos/variantes/fecha/notices; recursos situados, no biblioteca genérica previa. Las relecturas pendientes acotan los usos afectados, no obligan a esperar todo M2.
- **G2.04:** primera consolidación cumplida y recibida. No otra reescritura ahora; corregir solo retornos reales y conservar versión/IDs/evidencia.
- **G1/G3:** R11/R12 y T01–T08 mantienen decisiones técnicas en #4; ninguna ruta, stack, política o configuración elegida por esta recepción.

Mensajes vigentes en los contratos existentes de [SEO/GEO](../../../coordination/valiris-restaurants/SEO_Estrategia_Contenido_Prompt.md), [G2.02](../../../coordination/valiris-restaurants/G2_02_Arquitectura_Storefront_ORILLA_Prompt.md), [G2.07](../../../coordination/valiris-restaurants/G2_07_UI_Storefront_Adaptativo_Prompt.md) y [G2.04](../../../coordination/valiris-restaurants/G2_04_Contenido_Storefront_ORILLA_Prompt.md). **Preparados, no enviados; no nueva activación de agentes aquí.**

Para continuación nueva: HEAD publicado de `docs/m1-g1-orilla-joint-handoff`, congelado antes de editar, rama/worktree propia y PR draft sobre esa rama; conservar #39/#40 y sus entregas congeladas. Fuentes de revisión distintas del baseline operativo. Trabajo ya iniciado conserva su checkout y puede leer los SHAs exactos; G1 coordina adopción/integración sin rebase/reinicio automático. No importar este traspaso descendiente en las ramas fuente para crear dependencias circulares.

G2.05, recursos/fuente/derechos, composición/interacción aplicadas, G4 aplicaciones y participantes siguen pendientes. G4 #30 solo revisó selección conceptual. Ningún hallazgo documental acredita accesibilidad, comprensión o software. M0 cerrado; M1/#5, M2/#4 y #15 abiertos. Sin prototipo nuevo, implementación, configuración, publicación web o cierre. Dirección elegida, ORILLA original y decisiones aprobadas conservadas.
