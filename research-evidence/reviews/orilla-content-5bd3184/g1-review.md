# G1 — Recepción de ORILLA CASE/COPY 1.0 y traspaso

4 de octubre de 2026 · G1, único PM · Revisión acotada documental; no revisión independiente G4.

## Fuente exacta y dictamen

[PR #35](https://github.com/yaboula/valiris-restaurants/pull/35), OPEN/draft sobre #34. Fuente común congelada: **`5bd3184ca48be8d579e3f82d3361dbf5de0ed228`**, ORI-CASE-1.0 y ORI-COPY-1.0 juntos. HEAD de evidencia consultado: `6ce8634e98da3d975a376a265de77b940ed22f37`.

| Documento | Git blob en ambos commits | Uso |
| --- | --- | --- |
| `docs/design/orilla-case.md` | `bade7126a2d4222227095a1f8e9fa6ae85c5c687` | Única realidad ficticia del restaurante. |
| `docs/design/m1-storefront-content-and-copy.md` | `bfc11eba8d86c2192e0c4fef766bf2728d7d15cf` | Copy situado derivado, no otra fuente de precios/horarios. |

El par está disponible para revisión SEO/GEO, adopción de arquitectura y composición PC temprana. La lectura no reprodujo una contradicción material que bloquee esos trabajos. Es contenido preliminar útil, parcial en el checkpoint conjunto; no aprobación final de copy, arquitectura, UI, marca, recursos o M1. G2.04 conserva consolidación de caso/copy y resuelve propuestas; G1 no reescribe su entrega.

## Comprobaciones y lectura

Leídos completos caso, copy, README, entrega y 18 contrastes del autor; inspeccionados verificador y checks. Se contrastaron historia/personas/ambiente con carta, categorías y ofertas; unidades/precios/minimum, variantes/positivos alimentarios/pendientes, local frente a cocina, indisponibilidad/restauración/desconocido/retirada, borrador privado, lenguaje/retorno y recursos conceptuales. Es lectura documental, sin UI compuesta ni revisión gastronómica/alimentaria real; no reaudita todos los recorridos anteriores.

G1 reprodujo el verificador en el checkout limpio del autor, desviando solo sus escrituras JSON a caché propia. Checks y manifiesto coinciden byte a byte con los publicados; el checkout del autor quedó limpio. Confirma 44 registros originales preservados, 18 enlaces locales/fragmentos, 28 tablas, 83 IDs únicos de copy, 11 platos, 13 ofertas, cuatro categorías, 12 registros alimentarios y 11 escenarios. Los 30 estados son propuestas de texto/relaciones, no 30 interacciones probadas. Los contrastes de reloj no demuestran cálculo real de un indicador de apertura.

Se verificó la igualdad de los dos blobs entre 5bd3184 y 6ce8634; los commits posteriores solo cambiaron README/checks/entrega del autor. Arquitectura ff8fc06 y CR/XR siguen intactos. #35 OPEN/draft, sin reviews/comentarios/checks en la respuesta GitHub consultada; #5/#4/#15 OPEN. Sin nueva comprobación ni sincronización de Linear.

## Qué está recibido y qué sigue pendiente

- CR01–CR07: respuestas **producidas por G2.04**, revisables. No se marcan adoptadas ni resueltas en el registro de G2.02 por esta recepción.
- XR01: recomendaciones argumentadas, especialmente Nuestra mesa, Horarios y visita y variantes de etiquetas de categorías. G2.02 adopta/rechaza/ajusta con motivo, sin duplicar identidades.
- XR02 y ORI-SEO-Q01–Q05: revisión aplicada SEO/GEO pendiente sobre este mismo par. No hay tráfico, ranking, indexación, datos estructurados o rastreo comprobados.
- XR03/compatibilidad de comportamiento: aplicado a composición sigue pendiente de G2.03; los contratos previos continúan vigentes.
- XR04: composición PC y posterior adaptación deliberada a teléfono pendientes; las longitudes propuestas no acreditan ajuste visual, foco, lectura o interacción.
- G2.05, fuentes/licencias, G2.08/G2.06 y G4 aplicaciones/participantes: mantienen sus revisiones pendientes. La selección conceptual y G4 #30 no aprueban estos nuevos usos.

## Reparto del siguiente trabajo

| Chat / responsable | Encargo concreto / límite |
| --- | --- |
| SEO/GEO | Revisar estructura ff8fc06 y CASE/COPY 5bd3184; responder XR02/Q01–Q05, recomendaciones editoriales y preguntas técnicas concretas a G3/M2. Solo sus rutas; no otra carta/historia/copy. |
| G2.02 | Adoptar explícitamente el par e identificar qué CR/XR resuelve; ajustar su arquitectura/etiquetas y retornar pendientes con efecto. Nueva rama/worktree de continuación; #33 permanece congelada. |
| G2.07 | Primer modelo coherente de Storefront con contenido real del caso, PC primero y después adaptación teléfono. Entrada Ver carta y puentes con consulta separada; no reconstrucción completa del Menu Digital/gestión. Pedir recursos situados, conservar fuentes editables/exportaciones en Git. |
| G2.04 | Recibir y consolidar recomendaciones sobre nuevos commits identificados; no cambia ahora por suponer revisiones recibidas. Una nueva versión afectará solo los IDs/usos pertinentes y sus revisiones. |
| G1 | Coordinar baseline, propiedad, discrepancias y secuencia de integración; no activar perfiles ni enviar mensajes por guardar el paquete. |

**Baseline operativo del siguiente ciclo:** HEAD publicado de `docs/m1-g1-orilla-content-handoff`, dependiente de #35. G1 y cada especialista congelan su SHA antes de editar. **Fuente de contenido revisada:** 5bd3184; **arquitectura de entrada:** ff8fc06. Son referencias distintas y deliberadas. El baseline contiene esos mismos blobs y los mensajes situados de este traspaso.

SEO/GEO y G2.07 son chats separados con ramas/worktrees propias. G2.02 continúa su oficio en nueva rama/worktree desde el traspaso publicado, conservando su #33: no adelantar aquella rama para introducirle dependencias descendientes ni reabrir/reiniciar lo ya entregado. Las tres contribuciones parten del mismo baseline y sus PRs apuntan a la rama del traspaso G1; G1 integra retornos por commits identificados. UI puede explorar etiquetas aún propuestas, con su estado visible, sin esperar revisión global de SEO/arquitectura; cambios recibidos afectan solo las composiciones correspondientes.

Los contratos existentes contienen los mensajes preparados y propiedad exacta. No se enviaron a otros chats ni se crearon/activaron especialistas aquí. Tampoco se fusionó, publicó sitio, compró, implementó o cerró resultado. Ninguna decisión aprobada cambia; 72 capacidades/36-30-6, público sin cuenta, personalización autenticada, solo audio independiente/3D pospuestos, dirección seleccionada y original ORILLA conservados. [Checks y límites](checks.json).
