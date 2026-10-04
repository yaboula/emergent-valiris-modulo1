**Later source update, 4 October 2026:** the original transfer below is frozen at #46/ffadd70 and includes the older #45/f84c549 Part 1 supplement. G2.07 subsequently published [a complete PC reading set](../../../research-evidence/g2-07-storefront/imagegen/README.md) at #45/298643b. Use that current proposal for a new visual contrast; Part 1 and the frozen dossier are historical snapshots, not the complete current UI state. ImageGen sections/bridges remain proposals with no editable UI, phone or G4 approval. [Integration register](../../../research-evidence/reviews/main-integration-2026-10-04/README.md) retains source boundaries. No Relume upload/generation is implied.

# ORILLA — paquete de prueba para Relume

4 de octubre de 2026 · G1, único PM · Encargo del fundador: trasladar el trabajo de G2 a una prueba externa en Relume. Preparado para uso manual; no acredita proyecto creado, información enviada, generación, compra o publicación en Relume.

## Empezar aquí

1. Crea un proyecto de prueba llamado **ORILLA — exploración Relume** y selecciona español para el contenido.
2. Pega [el prompt inicial](01-prompt-inicial.txt) en el campo de descripción del proyecto. Es la entrada breve; el dossier completo es material de consulta, no un prompt único para ese campo.
3. Revisa el sitemap antes de generar wireframes: **Presentación de ORILLA** y **Carta de ORILLA** son los dos destinos principales. Cocina, historia y visita son bloques de la presentación; categorías son secciones de la carta. Detalle y recuperación son destinos/estados contextuales, no páginas principales añadidas automáticamente.
4. Usa [las instrucciones por página, sección y dirección](02-paginas-secciones-y-direccion.md). Empieza revisando la presentación en PC; si Relume genera otras vistas, mantenlas como exploraciones. La carta y los estados se transfieren como contexto funcional completo, sin certificar su ejecución por aparecer en una maqueta.
5. Sustituye el contenido generado por los textos y datos del [dossier de G2](../../../research-evidence/relume-orilla/dossier-g2.md), conservando IDs, variante, formato, importe, condición y estado. Relume permite editar texto; generar copy no garantiza respetar nuestros literales. Si propone otro texto, registra la propuesta para G2.04.
6. Consulta las cuatro referencias visuales identificadas en las instrucciones. La propuesta publicada de G2.07 es una quinta imagen opcional, **no aprobada**. Si tu interfaz permite incorporar imágenes, usa esos archivos; esta preparación no confirma importación de imágenes, Markdown, PDF o ZIP como contexto de su AI. Si no la permite, usa las referencias como guía durante edición y revisión.
7. Guarda el proyecto/enlace de revisión y exportaciones que ofrezca tu interfaz. Devuélvelos al repositorio con fecha, prompts usados, versión, capturas y límites. Un enlace solo no sustituye los archivos exportables. G1 coordina la revisión con los propietarios y G4; la generación no cierra M1.

No hace falta activar nuevos chats para probar la herramienta. El contexto, contratos y trabajo recibido están disponibles; Relume aporta una exploración revisable, no reemplaza las responsabilidades de G2 ni decide alcance, identidad o arquitectura técnica.

## Qué recibe y qué estado tiene

| Fuente | Versión congelada | Estado que debe conservarse |
| --- | --- | --- |
| Recepción conjunta G1 | `4893d501b750efd1bb9149ff695564f0d2df227b`, [PR #44](https://github.com/yaboula/valiris-restaurants/pull/44) | Base documental de este paquete; aún no integrada en main. |
| Caso y copy G2.04 | ORI-CASE-1.1 + ORI-COPY-1.1, juntos en `4b382bebe5d5c6cad21a7edcaffab053c433a0e9` / #39 | Única realidad compartida de ORILLA; datos de restaurante ficticios, información alimentaria sin verificar. 94 IDs, 30 estados, 11 platos y 13 ofertas. |
| Arquitectura G2.02 | IA v0.4, `70512d7a3d1afcd7f3aa0c9823a4d6e7b08dde8c` / #42 | Adopta explícitamente el par 1.1. Siete destinos semánticos y seis recorridos no significan siete páginas. |
| SEO/GEO | `7c233f1b5b94257312ab92ca8c9c859c7a6c2c64` / #43 | Relectura de 1.1 con IA v0.3. G1 contrastó el delta posterior v0.4 por separado; no aprobación SEO general de v0.4. |
| G2.06 | Tres referencias elegidas, #28 / `e7065aaa92acdf223628f9d7099301d766810ad3` | Dirección elegida, no branding definitivo ni tres modelos. ORILLA original se conserva. |
| G2.07, lectura complementaria | `f84c549ddaf3e775fd8fff808bbd2391c5ca5a21`, [PR #45](https://github.com/yaboula/valiris-restaurants/pull/45) | Exploración ImageGen publicada: **Part 1 PC v0.2**, raster con texto incrustado, no modelo completo, teléfono o aprobación. Cinco archivos del commit se incluyen en el archivo exportado, con procedencia. Trabajo local no publicado queda fuera de esta transferencia. |
| G2.03 y cobertura | Documentos de `docs/design/`, criterios, matriz y ADRs en #44 | Contratos funcionales y evidencia documental recibida. No producto implementado, prototipo validado ni diseño visual completo. |

El dossier abre con el estado actual para resolver referencias históricas de las fuentes que aún dicen «relectura/adopción pendiente». Esas tareas ya recibidas no se vuelven a encargar. Sus textos originales se reproducen intactos como evidencia; composición, comportamiento aplicado, idiomas, recursos y revisión independiente siguen pendientes.

## Exportación completa y trazabilidad

[Generador y verificador](../../../research-evidence/relume-orilla/export_bundle.py) produce el dossier y dos ZIP reproducibles dentro de `.cache/relume-orilla/`:

- `ORILLA-Relume-paquete.zip`: entrada, instrucciones, dossier, manifiesto, referencias visuales y los cinco archivos publicados de G2.07. Es cómodo para guardar/compartir el paquete; **no se afirma que Relume importe ese ZIP**.
- `ORILLA-G2-fuentes-completas.zip`: árbol original de documentación, coordinación, investigaciones/evidencias y antecedentes de #44, más la entrada de este paquete y el complemento publicado de #45. Conserva estructura y enlaces originales, fuentes, ADRs y revisiones; no es material para pegar entero al prompt inicial.

Las fuentes, entrada, dossier, manifiesto, generador y comprobaciones se versionan en esta rama. Los ZIP son exportaciones derivadas regenerables, sin crear una fuente de verdad paralela. El [manifiesto](../../../research-evidence/relume-orilla/source-manifest.json) identifica rutas, commits, hashes y estados; el [informe](../../../research-evidence/relume-orilla/checks.json) limita expresamente lo comprobado. No se cambia el trabajo de otros agentes.

## Cómo evaluar lo generado

| Revisión | Pregunta concreta |
| --- | --- |
| Fidelidad al caso | ¿Todos los nombres, recetas, variantes, precios y horarios provienen del par 1.1? ¿Se conserva ficción visible, Alcoy y ausencia de contactos reales? |
| Estructura | ¿Hay acceso directo a carta, cuatro bloques conectados de presentación y retorno al origen? ¿Se evitó convertir categorías, metadatos y estados en páginas superfluas? |
| Dirección | ¿La propuesta tiene personalidad culinaria, luz, tipografía gráfica y ritmo? ¿La presentación es expresiva y la consulta clara? No basta elegir colores de una plantilla. |
| Lectura y estados | ¿El arroz conserva 16,00 € / persona y mínimo 2? ¿Berenjena distingue formato/variante? ¿Flan agotado temporalmente sigue visible? ¿Pendiente, retirada y fallo se distinguen? |
| Adaptación | ¿PC se compone primero y teléfono se adapta deliberadamente manteniendo hechos y tareas? Ver ambos dispositivos en la herramienta no acredita adaptación deliberada o accesibilidad. |
| Evidencia | ¿Qué se ha observado realmente: sitemap, wireframe, imagen, enlaces conectados, exportación? Registrar lo no demostrado; no atribuir validación UX, G4, SEO técnico o software. |

Cambios editoriales vuelven a G2.04; arquitectura a G2.02; interacción a G2.03; composición a G2.07; dirección a G2.06 y recursos a G2.08. SEO/GEO contrasta usos afectados; G3 mantiene las decisiones técnicas de M2/#4 y G4 su revisión independiente. No se presume participación de ninguno por nombrarlo.

## Capacidades de Relume contrastadas en fuentes oficiales

Consultadas el 4 de octubre de 2026; documentación del proveedor, no prueba de nuestra cuenta/interfaz:

- [Sitemap y prompts](https://www.relume.ai/resources/docs/building-a-sitemap-with-ai): recomienda descripción inicial breve; admite prompts por página y sección y selección de idioma. Revisar estructura antes de wireframes.
- [Edición de wireframes](https://www.relume.ai/resources/docs/how-to-create-and-edit-wireframes-in-the-relume-site-builder): sección vinculada a sitemap, edición de copy, dispositivos y exportación. No documenta que pegue una carpeta de Git como contexto de AI.
- [Style Guide](https://resources.relume.io/resources/docs/concept-creation-using-the-relume-style-guide-builder): conceptos de colores, tipografía y UI después de sitemap/wireframes. Su generación no acredita reproducción de recursos custom, motion o tipografía licenciada.
- [Importación de sitio](https://resources.relume.io/resources/docs/import-an-existing-site-into-the-relume-site-builder): importación de sitemap desde un sitio; no equivale a importar este repositorio y ORILLA no tiene un sitio publicado que usar aquí.

Sin fechas comprometidas ni costes supuestos. No se elige stack, rutas definitivas, alojamiento, políticas de indexación, schema, licencias o plan de pago. M0 se conserva cerrado; M1/#5, M2/#4 y la línea comercial #15 siguen su flujo existente.
