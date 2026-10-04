# G1 — revisión del traspaso acotado de dirección ORILLA

3 de octubre de 2026 · Responsable: G1, Dirección + Producto. Fuente congelada: `4f97693bbdb207e910146be74330ea852d5b6861`, [PR #22](https://github.com/yaboula/valiris-restaurants/pull/22), base `b28ee63`. Revisión documental del encargo y su traspaso, distinta de una revisión G4 nueva.

**Dictamen G1: el encargo acotado de guía y traspaso G2.06 está cumplido y sirve como entrada para los siguientes especialistas. No se reproduce una corrección material obligatoria en ese alcance.** La dirección seleccionada no cambia. Fuentes candidatas, aplicaciones y contrastes pendientes conservan su estado; no se aprueba el sistema visual completo ni se cierra M1. El cierre del encargo de especialidad no equivale a merge de su PR.

## Fuentes y correspondencia con el encargo

Lecturas completas: [encargo corregido](../../../coordination/valiris-restaurants/G2_06_Continuacion_Storefront_ORILLA.md), [guía en su commit exacto](https://github.com/yaboula/valiris-restaurants/blob/4f97693bbdb207e910146be74330ea852d5b6861/docs/design/m1-storefront-visual-direction.md#direction-handoff--g206-v10), [retorno preparado del autor](../../g2-06-art-direction-2026-10-03/storefront-v0.3/RETORNO_PM-direccion-v1.es.md), manifests v0.2/v0.3 y [dictamen estático anterior G4](../orilla-v0.3-2026-10-03/g4-review.md). Se reutilizan contexto, protocolo, roadmap, definición funcional y recorridos/criterios ya leídos; se consultaron los contratos públicos PV y los prompts SEO pertinentes.

| Resultado solicitado | Evidencia de cumplimiento y límite |
| --- | --- |
| Referencia y lenguaje transferibles | Mantiene Cartel abierto revisado, nodo 9:15 y su hash. Describe nombre/alimentos/campo compartido/planos luminosos/luz-sombra; permite variar escala, orden y alineación por contenido. No impone una arquitectura o hero obligatorio. |
| Dirección tipográfica | Propone Archivo Black y Source Sans 3, sin confundir candidatos con fuentes del raster o una selección final. UI/localización contrastan silueta, nombres, lectura y glyphs; sistema consolida aplicaciones probadas. |
| Brief de recursos para G2.08 | Distingue fotografía real y propuesta ilustrada, fidelidad, derechos, producción y coste pendiente. No atribuye datos alimentarios a imágenes ni entrega un repertorio ficticio. Contempla una aplicación tipográfica cuando no haya recursos. |
| Criterios de coherencia | Preserva identidad y lectura al reducir intensidad; nombres, unidades, condiciones y hechos conocidos/pendientes no se sacrifican a la expresión. Expone riesgos de nombre largo, fuentes, ilustración y falta de recursos. |
| Retornos por especialidad | Arquitectura, contenido/SEO, interacción, UI, localización, recursos, motion y sistema conservan sus oficios. G2.06 revisa coherencia, G1 coordina y G4 mantiene independencia. Papel/servicio participan ante consecuencias concretas. |

La guía mantiene Storefront y Digital Menu separados, entrada Ver carta directa, autonomía de contenido y composición a cargo del estudio, hechos C1–C3 y las obligaciones vigentes. No reduce 36/30/6 ni exige representar las 72 referencias como navegación. El diff fuente solo añade 46 líneas de guía y dos líneas de changelog; las definiciones, estados, criterios y ADRs no se modifican.

## Comprobaciones y observaciones

- [Comprobaciones locales](document-checks.json): siete activos de manifests v0.2/v0.3 coinciden en bytes/SHA-256; dimensiones PNG leídas y registradas. No se alteraron los originales ni sus flags de revisión.
- Fuentes primarias consultadas el 3 de octubre: las licencias oficiales de [Archivo Black](https://github.com/google/fonts/blob/main/ofl/archivoblack/OFL.txt) y [Source Sans 3](https://github.com/google/fonts/blob/main/ofl/sourcesans3/OFL.txt) indican OFL 1.1 y conservación de avisos/licencia al distribuir. Esto respalda la referencia documental, no una comprobación de fuentes instaladas, glyphs o adecuación visual por G1.
- PR #22 observada OPEN/draft con SHA 4f97693, apilada sobre #21; PR #23 OPEN/draft contiene migración Git. No se han fusionado estas PRs mediante esta revisión ni cerrado #5.
- Carpeta local v0.4 y rama local del encargo retirado ausentes en la comprobación. Eliminación de objetos/historial activo Figma y originales de herramientas: declaración del autor, confirmada mediante retorno del fundador; G1 no inspeccionó el lienzo en vivo ni acredita borrado del historial interno.

**Ajuste operativo G1, sin devolución material a G2.06:** el párrafo inicial de 4f97693 todavía sitúa activos fuera del repositorio y el retorno conserva enlaces relativos a su ubicación anterior. La migración #23 ya aporta las rutas versionadas. G1 conservará la guía y esas referencias al integrar; no se modifica el retorno original para ocultar su contexto histórico. No reencargar dirección creativa ni generar otra muestra para resolver un cambio de ubicación.

## Continuación y límites de aceptación

G1 prepara [G2.02 arquitectura](../../../coordination/valiris-restaurants/G2_02_Arquitectura_Storefront_ORILLA_Prompt.md) y [G2.04 contenido](../../../coordination/valiris-restaurants/G2_04_Contenido_Storefront_ORILLA_Prompt.md), junto al [SEO de estrategia/contenido](../../../coordination/valiris-restaurants/SEO_Estrategia_Contenido_Prompt.md) ya preparado. Estructura y contenido se contrastan entre sí sobre versiones identificadas; G2.03 conserva comportamiento. UI/G2.07 entra con sus primeros recorridos y contenido representativo, sin esperar un sistema cerrado; G2.05/G2.08 aportan antes de congelar textos/recursos. G2.09 participa ante momentos concretos de movimiento y G2.10 consolida patrones demostrados. G2.06 custodia coherencia sobre aplicaciones identificadas.

Los nuevos prompts están preparados, no enviados ni ejecutados; no se presupone disponibilidad de esos agentes. No se ha realizado una revisión G4 nueva del texto de la guía, validación UX, accesibilidad integral, prototipo interactivo o software. Los pendientes reales son continuidad/contenido/visita autorizados, nombres e idiomas, tipografía aplicada, estados C1–C3, recursos/procedencia, interacción/motion y sus alternativas, dispositivos/salidas/uso real y contratos M2. No tienen fechas ni gastos supuestos. M1/#5 sigue abierto.

Flujo Git: esta revisión parte de #23/920ddf6 y no incorpora ni duplica el commit de #22. Tras la integración revisada de #21, G1 conserva guía #22 y migración #23, resuelve sus solapamientos en registro visual/changelog y retargetea las dependencias antes de integrar este dictamen y los prompts. Ninguna protección o rama ajena se cambia.
