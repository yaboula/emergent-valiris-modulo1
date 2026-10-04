# Retorno preparado para G1/PM · Dirección ORILLA

3 octubre 2026 · Propietario G2.06 · Versión de traspaso 1.0.
Estado: preparado, no enviado a otro chat. Guía propuesta para revisión/consolidación; no cierre M1.

## Resultado

He completado el encargo corregido de dirección y traspaso, no el desarrollo completo del Storefront. La guía está en la sección **Direction handoff — G2.06 v1.0** del [registro existente de M1](../../../valiris-restaurants/docs/design/m1-storefront-visual-direction.md). Este retorno no duplica una definición funcional ni crea otro sistema de diseño.

La autoridad creativa sigue siendo **Cartel abierto revisado**, [original v0.2](../storefront-v0.2/02-cartel-revisado-v0.2.png), [nodo 9:15](https://www.figma.com/design/miM4ul2l4Q6ZwJNfAJeN38?node-id=9-15). Móvil e ilustración v0.3 continúan propuestas. No he generado nuevas muestras para este encargo acotado ni recuperado las descartadas.

## Criterio Que Se Transfiere

Lo reconocible es la relación entre nombre de gran peso gráfico, producto sobre un campo compartido, planos luminosos menta/frambuesa y profundidad por luz/sombra. No un hero obligatorio, una cuadrícula o una sucesión fija de secciones. La información precisa debe sobrevivir al bajar la intensidad en consulta. ORILLA expresa al restaurante; no sustituye la identidad comercial de Studio Valiris.

La página puede ser más corta si el restaurante no tiene una historia o recursos que sostengan otra sección. Prefiero ese límite visible a inventar procedencia, fotografías o texto editorial. La falta de fotografías no impide dirección; tampoco demuestra por sí sola que exista un repertorio ilustrado.

Propongo probar Archivo Black Regular para expresión y Source Sans 3 Regular/SemiBold para lectura. Disponibilidad Figma y licencias OFL 1.1 comprobadas; son candidatas, no identificación del raster ni selección final. UI debe contrastar especialmente la silueta del nombre y localización sus textos/glyphs. Fuentes primarias y consecuencias constan en la guía.

## Retornos Y Propietarios

- G2.02: estructura/navegación. El cartel no decide la arquitectura pública.
- G2.04 + contenido/SEO: revisar significado culinario, promesas y hechos de visita; no duplicar precios/recetas en otra fuente ni llenar Home con texto genérico. G3 SEO revisa consecuencias técnicas.
- G2.03/G2.07: integrar comportamiento auditado, componer continuidad y responsive; entrada Ver carta directa. Contrastar nombre largo, información pendiente y los hechos/reglas C1–C3 en su superficie, sin declararlos resueltos.
- G2.05: idiomas públicos y fallback vigente; ninguna traducción de restaurante real ha sido revisada aquí.
- G2.08: brief fotográfico/ilustrado, repertorio, fidelidad, procedencia/derechos y producción. Ni foto conceptual ni dibujo acreditan datos alimentarios. G1 decide consecuencias materiales de coste.
- G2.09: movimiento motivado y alternativa reducida si lo propone, con evidencia observable. No prescribo animación ni produzco motion.
- G2.10: patrones demostrados, no extracción automática de un sistema desde el raster. G2.11/G2.12 participan ante consecuencias para papel/servicio.
- G2.06: revisar coherencia de aplicaciones versionadas. G1 coordina disponibilidad y revisión de contenido/SEO antes de consolidar; G4 mantiene independencia. El reparto no acredita especialistas activos ni consultas recibidas.

## Comprobación Y Límite

El original conserva su SHA256 `4F576DD2156F9361ABEE8338DF13704CFD4DC70A4E5E2A47D11DE8FBF567F989` y su IMAGE hash/nodo en Figma. Se conservan REVIEW y manifests v0.2/v0.3, sin cambiar sus flags históricos. El [dictamen G4](../../reviews/orilla-v0.3-2026-10-03/g4-review.md) existe: sin corrección material obligatoria en su alcance estático, no aprobación de las aplicaciones ni comprobación de continuidad, idiomas, reflow, interacción, accesibilidad integral, recursos o motion.

Riesgos que pueden debilitar la dirección: nombre largo que pierda protagonismo/legibilidad, candidato tipográfico que cambie demasiado la silueta elegida, ilustración que pierda presencia culinaria y aplicación sin recursos que quede genérica. Son preguntas acotadas para sus responsables y revisión G2.06; no una nueva elección creativa.

## Retirada Del Encargo Anulado

Por instrucción explícita del fundador se eliminaron la carpeta storefront-v0.4 con sus 19 archivos, sus dos originales generados, los seis elementos raíz nuevos de Figma con descendientes, el componente/estilo y la colección de 15 variables. Se retiró la rama local docs/m1-orilla-editorial-continuation. No hubo commits míos ni PR de ese trabajo. No se ha borrado la conversación ni se controla el historial interno de versiones de Figma; las muestras retiradas ya no están en su lienzo activo.

Original seleccionado, v0.1 histórica, v0.2/v0.3, fuentes de G1/G4 y trabajo ajeno preservados. El commit b28ee63 de G1 estaba en la rama retirada y en origin/docs/m1-connected-journey: se conservó mediante avance fast-forward, no se descartó.

Siguiente acción: G1 revisa este traspaso y coordina arquitectura/contenido/SEO y UI con G2.03. No se necesita otra confirmación de la dirección elegida.

## Registro Git De Esta Entrega

Commit `4f97693` en `docs/m1-orilla-direction-handoff`, publicado con [PR #22 en borrador](https://github.com/yaboula/valiris-restaurants/pull/22), apilada sobre la PR #21 abierta, base b28ee63. Solo añade la guía al registro existente y una entrada de CHANGELOG; no modifica entregas de G2.03 ni la selección. Refs #5, no cierre del issue. Revisión/merge de #21 primero; después trasladar únicamente el commit dependiente, retarget y revisar diff. No se ha fusionado ninguna PR. `git diff --check` correcto; siete activos históricos con bytes/SHA y dimensiones concordantes. Sin tests de software por no haber implementación.
