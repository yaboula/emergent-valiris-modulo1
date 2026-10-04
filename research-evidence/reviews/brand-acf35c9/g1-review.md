# G1 — revisión y consolidación de la exploración de marca

3 de octubre de 2026 · Fuente congelada `acf35c9a2d89646ce1222ec10c9435578748205c`, [PR #26](https://github.com/yaboula/valiris-restaurants/pull/26), OPEN/draft sobre #25/27861fd. Revisión PM documental/visual estática; no dictamen independiente G4 ni aceptación de branding definitivo.

## Dictamen

La entrega cumple el resultado acotado de exploración revisada y traspaso: guía, dos rutas contrastables, ocho láminas, recursos conceptuales, fuentes, límites y retornos por oficio existen en Git. No se reprodujo una contradicción material que obligue a rehacer la exploración antes de continuar su refinamiento. La idea culinaria general tiene valoración positiva del fundador, transmitida en este chat y coherente con el registro del autor; se conserva como base de desarrollo. A / Carácter a la mesa es la recomendación de G2.06, B / Sala viva es alternativa. Esto no convierte A en identidad definitiva aprobada ni decide R1/R2/R3.

El repertorio permanece abierto a comida, cocina y restaurante. Plato, pera, berenjena y taza son cuatro muestras, no el elenco final ni un compromiso numérico de servicio. Paleta, lettering, anatomía, composición y recursos siguen exploratorios. No solicitar de nuevo aprobación de M0 ni una nueva exploración genérica; el siguiente ciclo resuelve dudas concretas sobre esta entrega.

## Lectura y evidencia

Leídos completos: [guía](../../../docs/design/valiris-restaurants-brand-direction.md), [retorno v2](../../g2-06-restaurants-brand/v2/RETORNO_G1.es.md), [aclaración del fundador](../../g2-06-restaurants-brand/v2/founder-clarification.md), README, análisis de referencias, revisión del autor y código del verificador. Consultados manifest y registro de comprobaciones. G1 inspeccionó las ocho exportaciones PNG locales, no el lienzo Figma en vivo ni todos los originales de referencia.

| Láminas | Observación de G1 y límite |
| --- | --- |
| 01 | Explicita mecanismos distintos de las referencias y separa aprendizaje de copia. No demuestra originalidad jurídica ni resultados de terceros. |
| 02–03 | A conecta objetos culinarios mediante actuación/escena; B explora hospitalidad social y un lenguaje distinto. Son propuestas reconocibles entre sí, no estudios de reconocimiento con usuarios. |
| 04 | Siluetas, gestos y elementos compartidos hacen evaluable la familia abierta. Las reglas iniciales y continuidad anatómica aún necesitan refinamiento/producción. |
| 05 | Lettering, paleta y lectura son visibles y marcados como exploratorios. No hay logo óptico final, variantes compactas ni tokens aprobados. |
| 06 | Dos intensidades preservan café/1,90 €, declaración de leche, resto pendiente y atribución; consulta no necesita personajes. El acceso Ver carta y los datos son fragmentos, no un recorrido o editor probado. |
| 07 | Render volumétrico raster y tres poses ilustran materia/gesto. No hay modelo 3D, reproducción temporal, reposo animado o alternativa reducida comprobados. |
| 08 | Muestra nombre largo, idioma ilustrativo, relaciones de marca y ORILLA intacto. Base/a medida son contrastes de identidad, no demostración de modelos completos o personalización entregada. |

Se inspeccionó el código y se reejecutó el verificador **sin escritura** en el checkout del autor, después de confirmar HEAD exacto acf35c9 y estado limpio, comprobados también al terminar. Resultado reproducido: PASS, 56 activos v2, 19 registros de fuentes congeladas, 93 destinos locales, paridad factual y preservación v1/ORILLA. El script exige la rama del autor; no se cambió de rama ningún checkout para ejecutarlo. Se conserva [registro de reproducción](author-check-reproduced.json).

El [verificador G1 de solo lectura](verify.py) y [resultado](consolidation-checks.json) comprueban 116 archivos de la entrega del autor sin cambios y destinos locales del dictamen/encargos. [Comprobación de almacenamiento](storage-checks.json): 475 originales conservados, 487 registros, 83 documentos operativos/producto y 2.289 destinos locales, fuentes protegidas intactas. No se modifican manifests del autor; hashes actuales de copias operativas G1 se actualizan sin cambiar origen/historia.

Los 129 textos, 12 imágenes, ausencia de desbordamiento del padre inmediato y mínimo 4,72:1 proceden del **audit Figma archivado del autor**; el script verifica consistencia y recalcula cinco pares sólidos. No se rehízo un audit nativo en vivo, ni se verifican con ello texto raster, contraste con imágenes, accesibilidad integral o responsive. Licencias presentes no equivalen a nueva comprobación de binarios, exclusividad o derechos comerciales de todo el repertorio. No se consultaron fuentes externas nuevas para recomendar fuentes o rendimiento.

## Consecuencias operativas pendientes

1. **BR01 — jerarquía y modelos.** R1/restaurante protagonista sigue recomendación. Las instrucciones de la guía a UI sobre predominio local y no imponer paleta/personajes son condicionales a la relación que se seleccione; no nuevas reglas de configuración aprobadas. R2/R3 permanecen alternativas. El próximo encargo debe mostrar convivencia con restaurante/ORILLA y devolver la decisión al fundador sobre evidencia concreta.
2. **BR02 — dirección y producción.** Refinar paleta/lettering/gramática corresponde a G2.06 en colaboración; G2.08 puede realizar un piloto acotado de fuentes editables y variantes sobre una versión identificada, sin fabricar el repertorio entero o declarar branding final. Sujeto abierto no significa producción ilimitada incluida en un paquete.
3. **BR03 — 3D/motion.** La muestra raster con aspecto volumétrico no reabre la capacidad 3D de producto pospuesta en ADR-0008. G2.09 desarrolla motion solo ante aplicación/gesto concretos; la estética de profundidad no decide tecnología.
4. **BR04 — aplicaciones y copy.** IA, hechos y preguntas de contenido/SEO pueden avanzar sobre reglas auditadas. Textos de marca de la muestra siguen propuestas con G2.04/G6/SEO y localización pendientes. No imponer la composición de la lámina 06 ni convertir sus personajes en información alimentaria o de estado.
5. **BR05 — revisión independiente.** G4 tiene pendiente su lectura acotada de esta exploración y después de las aplicaciones. Esta revisión G1 no la sustituye; el [encargo preparado](../../../coordination/valiris-restaurants/G4_Brand_Exploration_Review_Prompt.md) no acredita activación o mensaje enviado.

Estos son límites y próximos checkpoints, no fallos ocultos declarados resueltos ni una petición de rehacer lo ya recibido. G1 actualiza solo coordinación/fuentes propias; conserva la guía y todos los archivos originales del autor sin modificar sus manifests.

## Estado y continuidad

#15 y #5 abiertos comprobados en este turno; PR #26 abierta en acf35c9, no integrada. No se ha sincronizado Linear, fusionado la pila, construido una aplicación, cambiado configuración, contactado especialistas o comprado recursos. M0 cerrado y alcance/ADRs aceptados intactos.

G1 prepara el siguiente refinamiento G2.06, un piloto condicionado G2.08 y revisión independiente G4. Cada uno conserva rama/worktree y archivos propios. G2.02/G2.03/G2.04/SEO continúan en lo independiente; identidad final y despliegue amplio esperan decisiones y evidencia. #15/M1 no se cierran por recibir esta exploración.
