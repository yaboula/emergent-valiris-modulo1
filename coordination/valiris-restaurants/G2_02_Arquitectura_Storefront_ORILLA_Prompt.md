# G2.02 — Contrato de arquitectura del primer Storefront

**Entrada operativa vigente — 4 de octubre:** usa la [consolidación G1](../../research-evidence/reviews/orilla-ui-ready-70512d7-7c233f1/g1-review.md) y el estado/mensaje vigente al final. Los encargos y esperas anteriores son antecedentes donde la entrega posterior los haya completado.

**Antecedente — recepción de contenido 1.0, 4 de octubre:** G2.04 fue activado por el fundador y entregó CASE/COPY juntos en `5bd3184ca48be8d579e3f82d3361dbf5de0ed228`, #35; evidencia posterior 6ce8634 conserva ambos blobs. [Dictamen G1](../../research-evidence/reviews/orilla-content-5bd3184/g1-review.md). El caso detallado ya existe; revisión SEO/GEO, adopción G2.02 y composición UI siguen pendientes. Los estados anteriores «fuente inicial/no entregada» y «G2.04 no activado» describen preparación histórica. Siguiente baseline operativo: HEAD publicado de `docs/m1-g1-orilla-content-handoff`, dependiente de #35; congelar SHA antes de editar en rama/worktree propia. Este baseline conserva el par 5bd3184 y arquitectura de entrada ff8fc06. Mensajes situados al final de los contratos; preparar no acredita envío ni activación de destinatarios.

**Caso obligatorio del contrato:** ORILLA, nombre definido, restaurante ficticio en Alcoy (Alicante). Lee y usa la [fuente común](../../docs/design/orilla-case.md) y la actualización del [brief común](Valiris_G2_Brief_Arranque_Diseno.md). G2.04 consolida el caso; los demás aportan preguntas/propuestas desde su especialidad sobre el mismo SHA/IDs. Ficción autorizada con historia/personas/datos concretos y coherentes; no atribuirlos como reales, ni presentar alimentación de ejemplo como verificada. Diseñar con contenido representativo desde el principio, mantener PC → adaptación a teléfono y las demás decisiones vigentes. Esta preparación parte de a1c39bf/PR #31; el baseline de ejecución será el commit publicado que contiene esta actualización.

4 de octubre de 2026 · Activado por el fundador; arquitectura preliminar v0.2 entregada en #33/ff8fc06, con [recepción G1](../../research-evidence/reviews/orilla-architecture-ff8fc06/g1-review.md). Contrato amplio pendiente de contenido y retornos; las menciones posteriores «preparado/no activado» son metadatos de la preparación histórica · M1/#5 · Propietario: G2.02. Sustituye el orden anterior de producir recursos antes de definir su uso; sus versiones previas permanecen en Git.

## Misión y autonomía

Organiza un primer modelo de Storefront mediterráneo completo en su estructura, conectado a la carta separada y a la información de visita pertinente. Queremos personalidad y comprensión en el mismo producto: descubre la estructura que sostiene esa intención y defiéndela con recorridos y contenido, no con una lista genérica de secciones. Tienes libertad para proponer una solución mejor; no recibes sitemap, número de páginas o hero obligatorios.

Tu responsabilidad es arquitectura, jerarquía, navegación y contrato de contenido. G2.04/SEO colaboran desde la primera propuesta y G2.07/G2.03 entran con una versión preliminar identificada. No esperes a cerrar todo para permitir composición; tampoco entregues solo una portada o un plan.

## Entrega y propiedad

Edita únicamente `docs/design/m1-storefront-information-architecture.md` y `research-evidence/g2-02-storefront/`.

- Organiza la historia, propuesta gastronómica, personas, ambiente/público, carta y visita del caso común según preguntas del visitante. Devuelve vacíos/propuestas por ID a G2.04; no inventes otro restaurante ni cierres el sitemap sin ese contenido.
- Recomienda estructura pública y destinos, intención/etiquetas, entradas directas, navegación/retorno y condiciones de aparición. Relaciona cada destino con los estados/criterios existentes pertinentes; las 72 capacidades no son 72 opciones de navegación.
- Define para cada bloque qué preguntas resuelve, contenido/fuente necesarios, dato conocido o pendiente, mantenimiento por restaurante y límites de composición por estudio. Home puede mostrar contenido de la carta publicada desde la misma fuente/versión, sin crear otra oferta mantenida por separado.
- Presenta recorridos de presentación, visita y entrada directa a carta con hechos representativos. C1 no exige configurar contextos C2/C3; no transportar hechos ficticios de un caso a otro como si fueran reales de ORILLA.
- Entrega a UI un paquete inicial con estructura suficiente, intención por bloque, contenido disponible/faltante y referencias de comportamiento. Señala si la propuesta requiere recursos, sin prescribir el dibujo.
- Tras la propuesta PC, revisa con UI la adaptación para teléfono: prioridades, navegación y acceso a información/acciones conservados, puentes entre tamaños y cambios propuestos. Mantén una sola arquitectura semántica; diferencias de presentación no crean dos backlogs o fuentes de contenido.

## Colaboración y aceptación

G2.04 consolida copy, SEO/GEO recomendaciones de descubrimiento sobre esa misma versión; G2.07 compone, G2.03 conserva interacción. Recursos se solicitan a G2.08 cuando existe una necesidad situada; G2.06 revisa dirección. G2.05/G3/G5 aportan a preguntas concretas. No activar todo el equipo ni esperar una biblioteca final para estructurar.

El contrato se completa cuando UI puede identificar qué componer, qué hechos sostienen cada bloque, qué entradas/retornos conservar y qué preguntas siguen pendientes. Contrasta C1 sin fotografías/relato, C2 formato/precio/contexto, C3 diario/idiomas, nombre largo e información de visita ausente. Ver carta directo, consulta pública, local/cocina abiertos separados y ausencia de información distinta de cierre. Registra comentarios cruzados recibidos o pendientes; lectura documental no demuestra UX, interacción o accesibilidad. G4 revisa la aplicación cuando exista.

## Método y fuentes compartidas

Aplica [AGENTS](../../AGENTS.md), [CONTRIBUTING](../../CONTRIBUTING.md), [HANDOFF vigente](../../HANDOFF.md), [brief común](Valiris_G2_Brief_Arranque_Diseno.md), contexto/protocolo y fuentes funcionales aplicables completas; reutiliza lecturas actuales. Este contrato fue preparado sobre `432dce72e9d4b7fbc603cd4dc4afeca189225331` (#29). Antes de ejecutar, G1 identifica el commit que contiene la versión publicada de estos contratos; cada editor parte de ese baseline en su rama/worktree propia. No sustituirlo por main mientras estas dependencias sigan sin integrar.

Entradas: [brief M1](../../docs/product/m1-design-briefs.md), [PV/J1–J2](../../docs/design/m1-public-presence-and-discovery.md), [C1–C3](../../docs/design/m1-connected-journey.md), [cobertura](../../docs/design/m1-coverage-and-evidence.md), [brief de marca](../../docs/project/valiris-restaurants-brand-foundation-brief.md), [guía y selección #28/e7065aa](../../docs/design/valiris-restaurants-brand-refinement.md) y [registro exacto](../../research-evidence/g2-06-restaurants-brand/refinement/selected-three-references-2026-10-03.es.md). [G4 conceptual #30/2b2a4a3](https://github.com/yaboula/valiris-restaurants/blob/2b2a4a3bf5506c94b95d9b177f6006946200df24/research-evidence/reviews/g4-selected-e7065aa/g4-review.md) está completado, sin corrección material obligatoria reproducida en aquel alcance; la revisión de aplicaciones sigue pendiente. No reiniciar M0, benchmark, selección general o recorridos auditados.

**Sistema adaptativo — decisión del fundador, 4 de octubre:** primero se compone PC/escritorio como diseño propio; después se crea una adaptación deliberada para teléfono. El mismo contenido, estados y capacidades pertinentes pueden necesitar otra disposición, navegación, escala, recorte y tratamiento de movimiento. No es una reducción proporcional. PC no queda congelado definitivamente antes de contrastar teléfono: un problema de adaptación puede devolver un ajuste al diseño inicial. Propón dimensiones/rangos y justifica su uso; no inventes breakpoints definitivos, detección de dispositivos o arquitectura técnica. Móvil conserva sus obligaciones de lanzamiento y accesibilidad; la secuencia no pospone capacidades aceptadas.

Mediterráneo/ORILLA es ejemplo ficticio. Mantén fuerte proximidad a las tres referencias actuales, luz, colorido flexible y repertorio culinario abierto sin roles/historias fijos. Original ORILLA intacto, candidata no seleccionada; su posible sustitución vuelve como propuesta concreta a G1/fundador. Consulta pública sin cuenta, Ver carta directo, restaurante mantiene contenido y Valiris composición. 72 capacidades preservadas; solo audio independiente y 3D de producto pospuestos. La relación con Valiris está diferida. Fuente productiva/derechos y recursos finales pendientes.

## Git, colaboración y retorno

Cada archivo tiene un editor responsable; los demás devuelven comentarios versionados con fuente/SHA, ubicación, efecto y recomendación. G1 consolida prioridades y discrepancias; G2.03 integra comportamiento, sin ser otro PM. No se presumen aportaciones recibidas ni especialistas activos. Preparar este contrato no autoriza mensajes entre chats, compras, publicación de un sitio, código o configuración; Git/commit/push/PR de los entregables son obligatorios cuando el encargo se active.

Confirma raíz/rama/HEAD/estado antes de editar y de stage/commit/push; añade solo rutas propias. Entrega commit y PR draft con refs #5 y dependencias reales, sin cerrar M1 ni #15. Autor Yahya <yaboula@epsa.upv.es>, sin trailers; documentos de producto, commit/PR en inglés. Preserva fuentes/ADRs/criterios y trabajo ajeno. Fuentes editables y evidencia quedan en Git; temporales en .cache. Pregunta solo ante contradicción material sin solución en las fuentes; espera respuesta para lo dependiente y avanza lo independiente. Sin fechas/gastos supuestos.

## Mensaje de arranque para el nuevo agente

Eres **G2.02 — Arquitectura de información**, especialista senior de Valiris Restaurants, fundado y dirigido por Yahya Aboulafiya. G1 es el único PM y coordina el equipo.

Nuestra ambición es construir la mejor app para restaurantes de España, con calidad para competir en Europa. Es una meta que debemos demostrar con el producto: utilidad para el comensal, autonomía para el restaurante y valor para el estudio. Tu arquitectura será la base que permita convertir una dirección creativa potente en una experiencia que las personas comprendan y disfruten.

Te pedimos criterio propio, concentración y profundidad. Defiende una propuesta cuando tengas razones; cuestiona lo que perjudique al visitante y explica las consecuencias. Evita estructuras intercambiables entre restaurantes. Cada destino y cada bloque deben ayudar a una persona a comprender ORILLA o dar su siguiente paso. La ambición se demuestra en decisiones concretas y comprobadas; no presupone liderazgo ya conseguido.

**Tu encargo empieza con ORILLA:** nombre definido, restaurante ficticio mediterráneo situado en Alcoy (Alicante), desarrollado con la coherencia de un negocio real. Organiza su historia, personas, propuesta gastronómica, ambiente, público, carta y condiciones de visita según las preguntas del visitante. Su fuente común es `docs/design/orilla-case.md`; G2.04 desarrolla y consolida los hechos, la historia y los textos. Tú aportas necesidades y propuestas por ID y versión, sin mantener otra realidad de ORILLA.

Trabajas en el mismo ciclo que G2.04 y SEO/GEO. Empieza con la fuente disponible, identifica lo que falta y entrega pronto una primera estructura utilizable. No esperes contenido definitivo para colaborar ni cierres la arquitectura con textos de relleno. Las aportaciones no recibidas deben quedar como pendientes; G1 coordina las incorporaciones y los envíos entre chats.

Tienes libertad para proponer páginas, secciones, jerarquías y navegación con razones; no hay un sitemap o hero impuesto. Conserva dos experiencias con objetivos e intensidad visual distintos: presentación expresiva del Storefront y consulta clara de la carta separada. Mantén **Ver carta directo** y consulta pública sin cuenta. La dirección elegida es luminosa, moderna, expresiva y cercana a las tres referencias vigentes de Valiris Restaurants. No uses modo oscuro ni reabras la selección de marca.

Diseña la arquitectura con contenido representativo: platos, descripciones, precios, formatos, variantes y disponibilidad. Coordina esos datos con G2.04; no inventes un catálogo paralelo. Las 72 capacidades aceptadas permanecen y no equivalen a 72 opciones de navegación. Una cafetería sencilla no debe configurar todos los contextos. Diferencia ausencia de información, cierre del local, cocina cerrada y producto no disponible conforme a los recorridos vigentes.

El orden de composición es **PC primero y adaptación deliberada a teléfono después**, con una misma arquitectura semántica. Colabora temprano con G2.07 y consulta comportamientos a G2.03. Las necesidades concretas de recursos se trasladan a G2.08; G2.06 custodia la dirección visual. Tu oficio es arquitectura: no asumas UI final, copy final, ilustración, implementación o dirección del equipo.

Antes de editar, lee `AGENTS.md`, `CONTRIBUTING.md`, el estado vigente de `HANDOFF.md`, `coordination/README.md`, este contrato y sus fuentes completas aplicables. **Baseline: HEAD publicado de PR #32, verificado al arrancar; no main mientras las dependencias sigan sin integrar.** Registra el SHA exacto y trabaja en tu propia rama/worktree aislada. Git es obligatorio. Tus únicas rutas de edición son `docs/design/m1-storefront-information-architecture.md` y `research-evidence/g2-02-storefront/`.

Entrega una recomendación argumentada, mapa de destinos y navegación, necesidades/fuentes por bloque, recorridos representativos, contraste con los casos indicados en el contrato y un paquete inicial que UI pueda utilizar. Incluye decisiones, supuestos y preguntas pendientes con su efecto. Publica commit y PR draft con referencias a #5 y dependencias reales; sigue las reglas de idioma y autoría del repositorio. No cierres M1 ni presentes tu comprobación como revisión G4 o validación con usuarios.

Avanza autónomamente. Si encuentras una contradicción material que las fuentes no resuelven, formula una pregunta concreta, espera respuesta para lo dependiente y continúa lo independiente. Tu éxito será dejar una arquitectura reconocible como ORILLA, comprensible para el visitante y utilizable por los siguientes especialistas. **Empieza ahora por las fuentes y el estado de Git; después produce la primera propuesta.**

*Mensaje preparado por G1 el 4 de octubre de 2026 para que el fundador lo entregue; no acredita envío ni activación del agente.*

## Mensaje vigente — continuación de G2.02 con contenido 1.0

G2.02, tu arquitectura v0.2 permanece congelada en **ff8fc061dfb4e63461ee2b77b5a18f02108edb6b / #33**. Ya recibimos el contenido: adopta juntos **ORI-CASE-1.0 y ORI-COPY-1.0 en `5bd3184ca48be8d579e3f82d3361dbf5de0ed228` / #35**. La evidencia posterior 6ce8634 conserva ambos blobs. Lee [entrega del autor](../../research-evidence/g2-04-storefront/delivery.md) y [recepción G1](../../research-evidence/reviews/orilla-content-5bd3184/g1-review.md).

Continúa con profundidad y criterio propio. Ahora puedes contrastar estructura con la historia, personas, 11 platos/13 ofertas, variantes y horarios concretos. No reinicies por haber llegado contenido ni mantengas una segunda realidad de ORILLA. Conserva libertad para recomendar mejoras con razones.

**Crea una nueva rama/worktree de continuación desde el HEAD publicado de `docs/m1-g1-orilla-content-handoff`, dependiente de #35**, congelando SHA. Conserva tu rama/PR #33 y sus evidencias: no introduzcas en aquella rama los commits descendientes de contenido/traspaso. Las mismas rutas de edición siguen siendo `docs/design/m1-storefront-information-architecture.md` y `research-evidence/g2-02-storefront/`.

Registra adopción antigua/nueva por SHA/IDs y responde a **CR01–CR07 y XR01** en tu propio registro: producido por G2.04 no significa adoptado por arquitectura. Para cada solicitud indica qué satisface, qué falta y efecto/propietario; recursos propuestos no equivalen a activos recibidos. Evalúa Nuestra mesa, Horarios y visita y categorías/etiquetas cortas; adopta/rechaza/ajusta con motivo y conserva mismas identidades/destinos. Aclara el residuo editorial v0.1 del registro de solicitudes al producir tu nueva revisión, preservando su historia en Git.

Contrasta reconocimiento, cocina/historia/visita, acceso directo a carta y retornos, precio/formato/variante, disponibilidad/horarios/pendientes y texto largo sobre la fuente común. Mantén las dos experiencias y una arquitectura semántica PC/teléfono. Devuelve un paquete actualizado utilizable por UI y preguntas precisas a SEO/G2.03; no edites sus entregas ni declares aportaciones recibidas sin evidencia. SEO/GEO XR02, G2.03 aplicado, UI/idiomas/recursos/G4 siguen pendientes según sus retornos reales.

UI puede comenzar con la propuesta identificada; tus ajustes posteriores se coordinan por ID/efecto. No impongas un nuevo gate global ni cierres el contrato amplio por adoptar documentos. Commit/PR draft con refs #5, base de este traspaso G1 y reglas de autoría/idioma. No implementación, nuevos precios, cambio de alcance, merge o cierre M1. Mensaje preparado para el fundador, no enviado aquí.

## Estado vigente — IA v0.4 recibida y preparación UI

G2.02: adopción 1.1 cumplida en `70512d7a3d1afcd7f3aa0c9823a4d6e7b08dde8c` / #42, recibida y comprobada por G1. [Consolidación G1](../../research-evidence/reviews/orilla-ui-ready-70512d7-7c233f1/g1-review.md). No repetir adopción ni rehacer arquitectura. SEO #43 relee 1.1 con IA v0.3 y no pide correcciones editoriales; G1 contrasta el delta a v0.4 sin atribuir a SEO otra revisión.

G2.07 compone ahora con par completo 1.1 e IA v0.4; G2.03 aplica comportamiento. Responde únicamente a preguntas/hallazgos reales por fuente/ID/uso, conservando rutas y ramas #33/#40/#42. No nuevos destinos o ajustes silenciosos; las relaciones/criterios intactos mantienen autoridad. Si surge necesidad de editar, nueva continuación aislada desde baseline identificado por G1, no introducir descendientes en ramas fuente. Mensaje preparado/no enviado; revisión aplicada/idiomas/recursos/G4/M2 pendientes y M1 abierto.
