# G1 — Paquete ORILLA listo para composición UI

4 de octubre de 2026 · G1, único PM · Recepción y contraste documental acotados. No revisión independiente G4 ni aprobación global de M1.

## Fuente común y estado por oficio

| Oficio / fuente | Versión exacta | Resultado recibido / límite |
| --- | --- | --- |
| G2.04 / #39 | CASE/COPY **1.1 juntos en `4b382bebe5d5c6cad21a7edcaffab053c433a0e9`**; evidencia d9ef8c9 | [Caso](../../../docs/design/orilla-case.md), [copy](../../../docs/design/m1-storefront-content-and-copy.md) y [R01–R08 editoriales](../../g2-04-storefront/seo-consolidation-1.1/resolutions.md) consolidados. No nueva reescritura requerida por la relectura. |
| G2.02 / [#42](https://github.com/yaboula/valiris-restaurants/pull/42) | IA **v0.4 en `70512d7a3d1afcd7f3aa0c9823a4d6e7b08dde8c`** | [Arquitectura/paquete UI](../../../docs/design/m1-storefront-information-architecture.md) y [adopción explícita](../../g2-02-storefront/content-1-1-adoption.md) del mismo par 1.1. Conserva destinos/mapas/recorridos; CR05–CR07 parciales y XR03/XR04 pendientes por aplicaciones. |
| SEO/GEO / [#43](https://github.com/yaboula/valiris-restaurants/pull/43) | `7c233f1b5b94257312ab92ca8c9c859c7a6c2c64` | [Relectura](../../seo-storefront/rereview-1.1/review.md) de contenido 1.1 e IA **v0.3/ba44c68**, no v0.4. R01–R08 suficientes en usos examinados y R02/R04/R05/R09 compatibles, sin correcciones editoriales obligatorias. [Nota posterior #42](../../seo-storefront/rereview-1.1/later-architecture-return.md) identifica el límite y supera los encargos de adopción anteriores. |
| G1 / este traspaso | Propia rama `docs/m1-g1-orilla-ui-ready` | Reúne #42 y #43, contrasta el delta v0.3→v0.4 y permite componer **par completo 1.1 + IA v0.4**, con aplicaciones y técnica pendientes. No atribuye a SEO revisión/aceptación de v0.4. |

**Siguiente responsable: G2.07 — UI adaptativa**, con G2.03 para comportamiento aplicado a las composiciones. La preparación editorial, su relectura acotada y la adopción de la versión están recibidas. No se exige otra ronda genérica de arquitectura/copy/SEO para empezar UI. Si surge una divergencia nueva, vuelve por ID/versión al propietario pertinente; solo ese uso necesita resolución. No se presume que G2.07 o G2.03 estén activos por preparar sus mensajes.

## Qué comprobó G1

Leídos relectura, doce contrastes, entrega y nota posterior de SEO; inspeccionado completo su verificador. Reutilizadas las lecturas recientes de par 1.1, resoluciones y adopción v0.4, incluidos sus diez contrastes y el diff acotado. No se repite investigación competitiva ni se cambia una regla técnica; las fuentes primarias históricas conservan su fecha y alcance.

Reproducidos **21 controles SEO** en el checkout limpio del autor, desviando únicamente las tres escrituras de resultados a caché G1. Checks y manifiesto coinciden byte a byte con los publicados; fuente, archivos y rama del autor quedan intactos. El anterior control de G1 sobre #42 reprodujo el verificador de v0.4, con 79 enlaces/fragmentos, 46 fuentes, seis IDs revisados/11 nuevos, mapas y evidencia histórica preservados; los dos JSON también coincidieron con los del autor. Son controles documentales, no acciones ejecutadas de producto, SEO en una web real o validación con comensales.

CASE/COPY conserva 94 IDs (83 heredados), 30 estados y el mismo negocio ficticio. Se mantienen historias/personas/platos/recetas/importes/horarios/contextos; SCENARIO-06 revisión 2 fecha explícitamente la misma excepción. La arquitectura conserva siete destinos semánticos y seis recorridos; estos no equivalen a siete páginas independientes ni a pantallas aprobadas. Las 72 capacidades/36-30-6 y fuentes/ADRs/criterios permanecen intactos.

### Delta IA v0.3 → v0.4 y cruce con el dictamen SEO

| Uso | Cambio v0.4 comprobado frente a ba44c68 | Relación con la relectura / límite |
| --- | --- | --- |
| Fuentes y categorías | Pin del par 1.1 y mapeo C01–C04/M01-03; identidades/miembros y mapa sin cambio. | La relectura consideró suficiente ese mismo mapeo en 1.1 y compatible con v0.3. No nueva clasificación. |
| Historia y entradas | H03-09/E01 y E01–E03 referenciados explícitamente; enlace aislado versus heading contextual; entradas directas sin Home obligatorio. | Mismos textos y relaciones que SEO examinó. Composición/expansión/foco y lectura de avisos requieren aplicación. |
| Producto/variante | H02-07/E03 conservan nombre actual, formato/unidad/condición, oferta y retorno; incertidumbre no sustituye V02 por V01. | No cambio de receta/precio ni nueva literal editorial. Accesibilidad y selección deben comprobarse en composición/interacción. |
| Horarios/recuperación | S10/SCENARIO-06 revisión 2 con fecha completa; S11/S14/S18 referencian Horarios y visita, condicionado a destino conocido. | Mismo uso fechado evaluado por SEO; horarios local/cocina no cambian. No reloj/publicación/cache implementados. |
| Metadatos | META-01–07 se adoptan como relaciones condicionales a destinos existentes, no como siete páginas/configuraciones. | Literales son los de 1.1 examinados. v0.4 aclara que un fragmento no garantiza preview individual; granularidad de entrega sigue en G3/SEO. No promesa nueva de indexación o preview. |
| Registro | Adopción 1.1 explícita, CR/XR/paquete actualizado, documentos 1.0 preservados como evidencia. | El pedido de adoptar 1.1 ya está atendido; no volver a encargarlo por leer un informe histórico. |

No se reproduce contradicción material bloqueante en este delta documental. **Este es el contraste de G1, distinto del dictamen SEO congelado en v0.3.** No exige otra auditoría completa ni amplía retrospectivamente la revisión. Si cambia en el futuro un texto/target/comportamiento que afecte a descubrimiento, solicitar el contraste especializado pertinente en aquella versión.

## Paquete, Git y siguiente encargo

Rama propia de reunión sobre #43/7c233f1: merge local de #42/70512d7 sin conflicto ni rutas solapadas; commit `063edf041ee88d12b8c499c23c1188f59e73e558`. Los 15 archivos de ambas entregas se conservan exactamente. No se cambia main, fuentes/ramas ajenas ni se fusiona una PR. La PR de este traspaso se apila sobre #43 y declara #42 como dependencia paralela; ambas deben conservarse al integrar después de los antecedentes.

**Baseline para nueva composición:** HEAD publicado de `docs/m1-g1-orilla-ui-ready`, congelado antes de editar. Contiene par 1.1, IA v0.4, ambos retornos y encargo vigente. Propia rama/worktree y PR draft sobre esa rama; propiedad UI en `docs/design/m1-storefront-ui-adaptive.md` y `research-evidence/g2-07-storefront/`. Fuentes editables, exportaciones, recursos disponibles, procedencia y evidencia en Git; temporales en caché. No introducir este descendiente en #42/#43 ni cambiar otro checkout. Si UI ya trabaja sobre un baseline acordado, consumir los SHAs exactos por lectura, registrar diferencias y acordar integración con G1 sin reinicio/rebase automático.

[Mensaje vigente G2.07](../../../coordination/valiris-restaurants/G2_07_UI_Storefront_Adaptativo_Prompt.md) preparado; [complemento G2.03](../../../coordination/valiris-restaurants/G2_Product_Designer_Prompt.md) conserva su propiedad y revisión de interacción. No se enviaron mensajes entre chats, no se crearon especialistas ni nuevas pantallas/prototipos aquí. G1 no asume dirección de arte, composición o recursos de los especialistas.

Resultado esperado UI: Storefront coherente completo, más allá de portada, usando preguntas/destinos como fuentes de diseño y conservando libertad de composición. PC propio primero; después adaptación deliberada a teléfono, con posibilidad de ajustar PC. Dos intensidades: presentación expresiva y consulta clara; en este encargo Storefront y sus puentes a Carta/Detalle, sin reconstruir todo Menu Digital/manager. Seis checkpoints R10, referencias/estados/retornos pertinentes y recursos situados; no biblioteca previa ni 72 elementos de navegación. Recursos e interacción acompañan las primeras composiciones; no esperar una ronda global de aprobaciones.

## Pendientes reales, sin nuevos encargos de corrección genéricos

- G2.07/G2.03: composiciones PC/teléfono y comportamiento/foco/origen/expansión/variantes/estados demostrables; los medios y límites se declaran, una imagen estática no prueba interacción.
- G2.05: idiomas y significado de strings completos/fallback; datos alimentarios del caso siguen sin verificar.
- G2.08/G2.06: recursos situados, correspondencia con plato/variante y dirección, fuente/productividad/derechos pendientes; personajes no fijados ni roles narrativos obligatorios. Original ORILLA y tres referencias conservados.
- G1/G3 y colaboradores: R11/R12/T01–T08 permanecen en M2/#4. No ruta/stack/política/robots/schema/cache/preview seleccionados o configurados por esta recepción.
- G4: revisión independiente de las aplicaciones cuando existan; #30 conserva su revisión conceptual. Participantes/dispositivos/uso real siguen pendientes; no inventar validación o resultados comerciales.

#42/#43 OPEN/draft sobre #41; #5/#4/#15 OPEN al readback. Linear no se volvió a consultar ni modificar. M0 cerrado y M1 abierto. Sin fecha comprometida, coste supuesto, compra, publicación web, código o configuración. No nueva pregunta material al fundador. [Comprobaciones y límites](checks.json).
