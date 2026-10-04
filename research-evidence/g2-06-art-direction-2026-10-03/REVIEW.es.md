# G2.06 - Direccion mediterranea: alternativas v0.1

3 de octubre de 2026. Propietario: G2.06, identidad y direccion de arte. Estado actualizado: las tres alternativas fueron rechazadas por Yahya. Se retienen como evidencia historica, no como candidatas de desarrollo.

La recomendacion original de Patio abierto queda retirada. El autor reconoce que las tres composiciones son variantes convencionales de una web de restaurante y no demuestran la direccion acordada. Yahya solicita empezar exclusivamente por Storefront y cambiar tambien el restaurante ficticio. Continuidad: [Storefront v0.2](storefront-v0.2/REVIEW.es.md). El cuerpo siguiente conserva el retorno original para trazabilidad; sus recomendaciones no estan vigentes.

## Resultado y acceso

Tres alternativas independientes para la Home de Mesa del Patio, caso ficticio C2 existente. No representan un cliente, platos fotografiados de un restaurante real ni informacion revisada por ese restaurante. G2.03 conserva comportamiento e integracion; G1 consolida consecuencias y Yahya selecciona direccion.

[Figma: archivo G2.06](https://www.figma.com/design/miM4ul2l4Q6ZwJNfAJeN38?node-id=3-2)

Equipo Valiris: asiento Full y rol admin confirmados por whoami. Se comprobaron en este archivo creacion, lectura, edicion de nodos/textos, disponibilidad y carga de fuentes, subida/colocacion de tres imagenes y captura/render. Esto acredita esas operaciones, no permisos universales sobre cualquier archivo ni todas las capacidades del plugin.

Pagina: 0:1. Tablero: 3:2. Imagenes: 3:10 / 3:15 / 3:20. Tablero 4592 x 1526; captura de inspeccion 3600 x 1197. Las imagenes se pidieron para 1440 x 1024, pero ImageGen devolvio 1487 x 1058. Se conserva esa resolucion real y relacion de aspecto; no se estiraron para afirmar las dimensiones solicitadas.

Las imagenes de Home son raster: su UI no esta compuesta en capas editables. Titulos y observaciones en Figma son textos editables con las fuentes reales comprobadas. Las familias solicitadas en los prompts son orientacion; el raster no acredita fidelidad tipografica exacta.

## Intencion de marca

El visitante debe reconocer un restaurante mediterraneo acogedor y contemporaneo, comprender su oferta para compartir y llegar a la carta. La expresion pertenece al restaurante. Studio Valiris conserva su papel de proveedor; este encargo no cambia su identidad comercial.

Hipotesis: el nombre, las alineaciones y el ritmo de composicion deben conservar reconocimiento al retirar la fotografia. Este principio aun no esta demostrado en estas tres muestras.

Se reutiliza Mesa del Patio para mantener nombres, precios y contexto comparables. No se ha creado otra carta ni se modifican los recorridos auditados. La composicion baja de intensidad al pasar de presentacion a consulta.

## Alternativas y recomendacion

| Orden visible / artefacto | Decision que permite comparar | Fortalezas observadas | Debilidades y comprobacion siguiente |
| --- | --- | --- | --- |
| 1 - [Patio abierto](01-patio-abierto-v0.1.png) | Nombre grafico a gran escala, composicion asimetrica y mesa cenital; comienzo de carta mas sereno. | Nombre protagonista, entrada Ver carta clara, precios/formato/contexto juntos en el fragmento, largo nombre envuelto. | Gran parte del caracter viene de la fotografia. Falta Home sin fotos, composicion movil y alimentacion/idiomas. |
| 2 - [Cuaderno de cocina](02-cuaderno-de-cocina-v0.1.png) | Portada editorial centrada y carta tabular vertical en continuidad con la serif. | Nombre legible, entrada clara, filas completas con formatos/precios y condicion del arroz. | Mas convencional y dependiente de la escena fotografica; varias piezas usan serif donde se habia previsto sans. Falta revisar legibilidad y amplitud del bloque de formatos en movil. |
| 3 - [Mercado al mediodia](03-mercado-al-mediodia-v0.1.png) | Nombre de rotulacion en una linea, entrada en franja y carta en filas con columna de formatos/precios. | Mas estructura de consulta visible, etiquetas de formato separadas, suplemento y estados alimentarios explicitos. | El raster anadio miniaturas, aumentando dependencia de fotos. Los avisos secundarios necesitan contraste medido; titulo ancho y tres columnas no se trasladan directamente a movil. |

**Recomendada: Patio abierto.** La combinacion de nombre, mesa compartida y carta calmada ofrece el punto de partida mas convincente para la personalidad buscada. Mercado aporta una referencia util de columna de formatos/precios, sin aprobar una mezcla automaticamente. Cuaderno ofrece mayor continuidad editorial, con menor singularidad observada.

Esta recomendacion es juicio del autor sobre las imagenes; no evidencia de preferencia de clientes, uso, superioridad comercial ni aprobacion del fundador.

## Referencias inspeccionadas y adaptacion

| Referencia | Material efectivamente inspeccionado | Rasgo aprovechable / adaptacion |
| --- | --- | --- |
| [Gastrometro 2024](https://www.just-eat.es/gastrometro/2024/) | Fotogramas locales 01, 02, 06 y 08; contenido publico de su pagina. | Aire, cambio de escala y alimento reconocible. Adaptar al nombre del restaurante y entrada a carta; no copiar el informe, exigir foto ni imponer su navegacion/scroll. |
| [Eat Curious / Fiasco](https://fiasco.design/work/plant-based-brand-eat-curious/) | eat-curious-overview.png y caso publicado. | Coherencia de producto/tipografia/color. Adaptar intensidad y densidad a consulta; no copiar su tono, mascotas, paleta ni afirmar motion observado. |
| [Marshmallow / Ragged Edge](https://raggededge.com/partnerships/marshmallow) | marshmallow.png y fotogramas scroll-03/scroll-11; pagina del caso. | Ritmo editorial entre formatos. Conservar modo claro y contenido pertinente; no reproducir mascota, bloques oscuros ni llenar Home con manifiestos. |

Los fotogramas son evidencia estatica. No se ha ejecutado una auditoria de interaccion ni observado una tecnica concreta de scroll. Las referencias adjuntas al generador fueron archivos reales; los prompts identifican su papel de inspiracion.

## Comprobacion del autor realizada

- Lectura de fuentes iniciales y estados publicos pertinentes sobre el baseline local d71d3de; coincidente con el retorno documental G1/G4. No se reinicia M0 ni el benchmark.
- Inspeccion visual de las tres salidas a su tamano mostrado: nombres, jerarquia, acceso a carta, precios, formatos, minimo de dos personas, corte del contenido y paso a consulta.
- Las tres muestran Carta general; quesos media 24,00 EUR/completa 34,00 EUR y arroz 18,00 EUR por persona/minimo dos. Mercado incorpora extra de pan +2,00 EUR general.
- Mercado mantiene leche y trigo/gluten declarados junto a informacion restante pendiente. Ninguna muestra acredita revision alimentaria real. Patio/Cuaderno no desarrollan estos avisos en su fragmento.
- Resolucion y SHA-256 comprobados tras copiar los PNG; originales de ImageGen conservados. Todos los activos tienen menos de 10 MB.
- Tres subidas a Figma devolvieron success y el nodo previsto. Lectura posterior encontro tres IMAGE fills con hash y modo FIT.
- La primera composicion habia asignado 1488 x 1056 a los marcos. Se corrigieron a 1487 x 1058 antes de subir los activos para conservar su proporcion.
- Los 13 bloques de texto nativo del tablero tienen ancho dentro del padre. Se obtuvo e inspecciono [captura de Figma](figma-board-v0.1.png): imagenes visibles, notas separadas, sin solapamientos observados.
- Fuentes reales disponibles/cargadas para anotaciones: Source Sans 3 Regular/SemiBold, Bricolage Grotesque Bold, Fraunces Bold y Archivo Black Regular. No se deduce de ello la tipografia exacta del raster.

No se ha medido contraste pixel a pixel del raster, ni probado reflow/zoom/teclado, movil, lectores de pantalla, mantenimiento, motion, rendimiento, dispositivos reales o comprension con participantes. Autoinspeccion no equivale a revision independiente de G4.

## Aportaciones tempranas y traspaso preparado

Estas aportaciones quedan preparadas; no han sido enviadas ni respondidas por otros especialistas. Su disponibilidad no se presume.

| Destinatario | Aportacion / pregunta concreta | Consecuencia pendiente |
| --- | --- | --- |
| G2.04 - Contenido | Mantener nombre y concepto literal. Cocina mediterranea para compartir es copy propuesto del caso ficticio, no una promesa validada. No inventar origen local, km0, premios, chef ni atributos de visita. Definir el minimo de informacion alimentaria en destacados y fragmentos de carta. | Confirmar copy y coherencia factual antes de consolidar la muestra seleccionada. |
| SEO estrategia/contenido | Identidad, oferta y condiciones deben estar disponibles como contenido publico textual en el desarrollo siguiente, con entrada directa a carta. Se propone historia solo si hay contenido significativo; no Home rellena con texto SEO generico. | Revisar significado, estructura y relacion presentacion/carta. No hay posiciones, trafico ni rastreo comprobados. |
| SEO tecnico / G3 | El texto del raster no es entrega de contenido web. Revisar en la fase pertinente entrega del contenido, titulos, activos e idiomas/rutas con el stack real. | No se selecciona tecnica, proveedor, estructura URL ni regla de indexacion ahora. |
| G2.07 - UI y G2.03 - Interaccion | Conservar nombre, entrada, alineaciones y asociaciones formato/precio/condicion al bajar intensidad. No trasladar el hero de escritorio a movil por simple recorte. | Componer muestras sobre la direccion elegida manteniendo PV-P01/P04/P06/P10 y C1-C3. |
| G2.08 - Recursos | Las tres fotografias son generadas y conceptuales. No publicarlas como representacion fiel de platos reales. Preparar opcion sin fotografia y reglas para fotos parciales sin huecos. | Verificar material, derechos y fidelidad cuando exista restaurante real. |
| G2.09 - Motion | Propuesta posterior: un cambio breve de intensidad puede comunicar pasar a carta; precio, estado y acceso no deben depender de animacion. Estas imagenes no demuestran movimiento. | Entregar muestra observable y alternativa reducida tras seleccion, coordinada con G2.03. |
| G2.05 - Localizacion | Usar los avisos EN/FR/DE existentes; mantener valores comunes y nombrar fallback. No atribuir revision real a traducciones simuladas. | Comprobar longitudes y significado de muestras C3 seleccionadas. |
| G2.11 - Impreso | Evaluar si nombre y jerarquia sobreviven sin hero; formatos/precio/condicion deben permanecer unidos. | Composicion especifica de papel posterior, no impresion de una captura ni prueba fisica afirmada. |
| G1 / G4 | G1 recibe consecuencias de alcance/mantenimiento; G4 conserva revision independiente posterior de muestras concretas. | Esta entrega no resuelve CG01-CG03 completos ni cierra M1. |

Para el comensal se propone reconocimiento y continuidad hacia consulta; para el restaurante, expresion propia con mantenimiento de datos separado de composicion; para Valiris, trabajo inicial de recursos y direccion con posibilidad de reutilizar patrones. Costes, ahorro, facilidad de mantenimiento y margen no estan medidos.

## Continuacion dependiente de seleccion

Yahya elige una direccion o solicita un ajuste/mezcla. Si combina elementos, producir una nueva referencia coherente antes de desarrollar las muestras. No inferir seleccion por la recomendacion del autor.

La siguiente version v0.2 mantendra este archivo de Figma y contrastara nueve composiciones: Home escritorio/movil/sin fotos; C1 carta movil sin fotos; C2 General/Terraza/detalle; C3 EN/fallback DE. C1 conserva diez productos y acceso directo sin configuracion avanzada. C2 conserva sus importes contextualizados, minimo, unidad de peso y suplementos. C3 conserva las fechas ficticias 1-2 octubre, la distincion publicado/borrador y positiva+pendiente, sin exponer D11.

Corregir defectos observados y registrar su alcance. La aceptacion de una muestra no completa UI/sistema/motion ni M1. El retorno de producto docs/design/m1-art-direction.md se integrara por el flujo vigente de #5/PR #21 cuando exista la direccion y sus muestras contrastadas. Esta evidencia local no sustituye ninguna fuente funcional.

## Archivos y continuidad

- PNG 01-03: imagenes conceptuales originales de esta tanda, ordenadas por aparicion real en el chat.
- prompts.txt: prompts completos y referencias adjuntas; herramienta integrada ImageGen, sin CLI/API alternativa.
- manifest.json: origen, hashes, tamanos, archivo/nodos y estado.
- figma-board-v0.1.png: captura descargada e inspeccionada, no una cuarta alternativa.
- Este retorno: propietario G2.06 y version v0.1; no modifica inventario funcional ni entregables G2.03.

Fuentes de continuidad: [brief comun](../../coordination/valiris-restaurants/Valiris_G2_Brief_Arranque_Diseno.md), [protocolo G2.06](../../coordination/valiris-restaurants/Valiris_Organizacion_Protocolo_Agentes.md), [C1-C3 existentes](../../valiris-restaurants/docs/design/m1-connected-journey.md), [presencia publica](../../valiris-restaurants/docs/design/m1-public-presence-and-discovery.md), [cobertura](../../valiris-restaurants/docs/design/m1-coverage-and-evidence.md), [retorno G1/G4](../reviews/coverage-d71d3de/review-result.md).

Siguiente accion y responsable: Yahya selecciona 1, 2 o 3, o concreta el ajuste; G2.06 produce v0.2 sobre esa decision.
