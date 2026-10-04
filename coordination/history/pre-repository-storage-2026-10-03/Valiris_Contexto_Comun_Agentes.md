# Valiris — Contexto común para agentes

Versión 0.1 · 1 de octubre de 2026 · Responsable del proyecto: fundador de Valiris.

Documento de incorporación preparado a partir de la definición funcional y las decisiones posteriores de la conversación. Sus reglas operativas son propuestas para utilizar como base de trabajo; no acreditan que los agentes, integraciones o servicios ya estén activos.

## 1. Lectura y uso

Lee este documento completo al incorporarte. Después lee la definición funcional vigente y la ficha de tu responsabilidad en `Valiris_Organizacion_Protocolo_Agentes.md`. Consulta la investigación detallada cuando un encargo requiera evidencia o trazabilidad de una decisión.

La lectura termina en trabajo: identifica el resultado solicitado, las decisiones que ya existen y el siguiente entregable. No vuelvas a preguntar por información resuelta en los documentos. Si falta algo importante, explica qué decisión depende de ello y formula una pregunta concreta mientras avanzas en lo independiente.

Este contexto no sustituye el encargo actual del fundador. Las instrucciones posteriores y las decisiones registradas pueden modificarlo. Trabaja siempre con la versión disponible más reciente y deja señaladas las contradicciones que afecten a tu tarea.

## 2. Proyecto y objetivo

Valiris Restaurants es un proyecto de producto para restaurantes independientes y cafeterías, con España como mercado inicial. Nació con un propósito de portfolio trabajado con rigor profesional y una posible evolución comercial. La dirección actual busca construir y comercializar una oferta real, apoyada en una organización de agentes especializados.

El fundador tiene capacidad de desarrollo, sensibilidad por UI/UX y experiencia trabajando con agentes de IA. Está dispuesto a aprender y a abordar trabajo exigente. No se deben descartar capacidades útiles simplemente porque su implementación sea compleja.

La ambición es competir con referentes de España y, progresivamente, Europa. Ser el mejor es una aspiración que orienta el esfuerzo; no es una ventaja demostrada ni una frase que deba publicarse sin evidencia. La superioridad debe concretarse en tareas, calidad, servicio y resultados comprobables.

El objetivo combina utilidad para el comensal, utilidad para el restaurante y viabilidad para Valiris. No exigimos que cada capacidad beneficie directamente a los tres actores. Sí examinamos su contribución y los costes o efectos que impone a los demás.

## 3. Primer producto y dos líneas de trabajo

El primer módulo prioritario es **Storefront + Digital Menu**: presencia pública del restaurante y carta digital que se puede consultar mediante enlace, QR u otras entradas pertinentes.

El QR es una vía de acceso, no el módulo. La web comercial de Valiris es otra experiencia: representa nuestra marca, explica nuestra oferta y permite que restaurantes interesados nos conozcan.

| Línea | Resultado buscado | Relación con la otra línea |
|---|---|---|
| Producto común | Módulo completo, comprensible, gestionable y mantenible | Proporciona demostración, capacidades y límites reales |
| Marca y presentación comercial | Identidad de Valiris y web que explica la oferta | Posicionamiento y oferta orientan su contenido; promesas corresponden a lo entregable |
| Servicios del estudio | Alta, diseño propio y actualización delegada según contrato | Utilizan el producto común; costes y encargos se identifican por separado |

El producto tiene prioridad. Marca y web pueden avanzar en paralelo con decisiones y materiales suficientemente definidos. No es necesario esperar a completar todo el software para preparar identidad y estructura comercial. La demostración y las condiciones finales requieren correspondencia con la entrega real.

## 4. Personas y situaciones

| Actor | Trabajos relevantes | Fricciones que debemos comprender |
|---|---|---|
| Comensal antes de visitar | Reconocer el local, entender propuesta y precios, preparar la visita | Información dispersa, oferta desactualizada, horarios o condiciones ambiguos |
| Comensal durante la visita | Llegar a la carta, encontrar opciones, entender formatos y condiciones | Interrupciones, títulos confusos, navegación pesada, información incompleta |
| Personal del restaurante | Preparar contenido, revisar, publicar y actualizar durante el servicio | Trabajo duplicado, ediciones difíciles, incertidumbre sobre qué se ha publicado |
| Dueño o comprador | Representar su negocio, delegar cuando lo necesita y entender qué compra | Oferta comercial opaca, dependencia del proveedor y soporte poco definido |
| Valiris | Entregar un producto útil y servicios con costes sostenibles | Personalización que consume margen, promesas excesivas y operaciones difíciles de mantener |

Estos son trabajos y problemas de referencia. La intensidad y frecuencia en un restaurante específico necesitan investigación real; no se inventan respuestas para completar una persona o un journey.

## 5. Alcance y límites

Storefront + Digital Menu cubre preparación, revisión, publicación, consulta, actualización, distribución, corrección de errores y continuidad del contenido.

Pedidos, pagos, TPV, reparto y facturación tienen responsabilidades fuera de este módulo. Reservas, opiniones, fidelización y atención por WhatsApp pertenecen a sus áreas correspondientes; se puede diseñar una conexión cuando aporta al recorrido. Una conexión no autoriza a absorber la ejecución del otro módulo.

Core concentra responsabilidades compartidas como establecimientos, miembros, permisos y datos comunes. El alcance concreto de esa relación se determinará al planificar; no se reconstruye silenciosamente todo Core dentro de la carta.

### Las siete áreas funcionales

| Área | Contenido de referencia |
|---|---|
| Presencia e identidad | Información del local, visita, contenido editorial, marca, plantillas y diseño propio |
| Oferta y contexto | Categorías, formatos, variantes, suplementos, menús compuestos, servicios, zonas, vigencia y disponibilidad |
| Consulta | Navegación, búsqueda, filtros, explicación, detalle gradual, destacados y enlaces directos |
| Gestión y publicación | Importación, revisión, edición móvil y conjunta, borradores, programación, historial y recuperación |
| Idiomas y confianza | Traducciones mantenidas, glosario, datos comunes, información alimentaria declarada y revisión pendiente |
| Acceso y distribución | Enlace, QR, entrada contextual, impresión, web existente, canales externos y exportación |
| Medición y oferta comercial | Uso digital, acciones, mantenimiento pendiente, servicios del estudio y resultados conectados cuando existan |

El detalle está en `Valiris_Definicion_Funcional_Storefront_Digital_Menu.md`. No reemplaces sus comportamientos por esta tabla abreviada.

Las etiquetas Recomendada, Configurable, Oportunidad y Conectada representan tratamientos de propuesta. No son pruebas de demanda, plazos de entrega ni un compromiso automático de construir cada oportunidad.

## 6. Identidad, plantillas y diseño propio

Se ha acordado ofrecer plantillas base y diseño propio realizado por el estudio, también de pago. El diseño propio es un encargo profesional con alcance y revisiones definidos, no un editor libre que el comprador deba aprender a utilizar.

La autonomía de mantenimiento debe conservarse en ambas vías. Modificar un precio, un agotado o un texto cotidiano no debería obligar al restaurante a contratar un nuevo trabajo de diseño.

La expresión visual puede cambiar; información, publicación y gestión comunes deben conservar coherencia. La calidad de lectura, acceso y comprensión es parte del producto, no un extra reservado al cliente con mayor presupuesto.

Servicios posibles: puesta en marcha, aplicación de plantilla, diseño propio, actualizaciones delegadas y evolución del diseño. No hay tarifas, paquetes definitivos, compromisos de soporte ilimitado ni economía unitaria demostrada.

## 7. Filosofía de trabajo

### Ambición y utilidad

Explora posibilidades ambiciosas cuando exista una razón convincente. Valora capacidades pequeñas con la misma seriedad. Explica qué situación mejoran, a quién ayudan y qué mantenimiento necesitan. La complejidad técnica es una consideración de planificación; por sí sola no invalida una idea.

### Profundidad con cierre

Desmonta el problema hasta poder tomar una decisión y producir un resultado. La investigación debe responder una duda concreta. Una vez suficiente para decidir, registra el límite y avanza. Evita ciclos de análisis que generan más documentos sin cambiar el trabajo.

### Completo y manejable

Un producto completo cubre el trabajo y sus excepciones relevantes. La configuración y la consulta se adaptan al negocio. Una cafetería sencilla no necesita activar todas las opciones que usa un restaurante con zonas y menús diarios.

No reduzcas la propuesta automáticamente a un MVP genérico por una preferencia personal por simplicidad. Tampoco conviertas cada posibilidad en una función comprometida. Propón una decisión fundada y respeta el alcance acordado.

### Criterio y autonomía

Actúa como un especialista que cuestiona supuestos y propone alternativas. No te limites a asentir. Continúa las tareas autorizadas y necesarias; pide aclaración cuando una ausencia o contradicción cambie sustancialmente el resultado. Las decisiones rutinarias dentro del encargo se resuelven con criterio y se dejan visibles cuando importa.

### Honestidad

Distingue observación, declaración de proveedor, inferencia, hipótesis y resultado de prueba. No inventes datos de usuarios, costes, tiempos, conversiones, contactos, entrevistas ni capacidades de herramientas. Una simulación entre agentes puede preparar una prueba; no cuenta como investigación con comensales o restaurantes reales.

### Revisión y continuidad

Quien produce comprueba su trabajo; cuando corresponde, otro agente revisa de manera independiente. Un resultado entregado no equivale a un resultado validado. Registra lo que se hizo, lo que falta, la evidencia y el siguiente paso para que el equipo continúe sin reconstruir la conversación.

## 8. Compromisos de coherencia del producto

Los siguientes son principios de diseño conservados en la propuesta, que deberán concretarse y comprobarse:

- Consultar sin cuenta ni instalación obligatorias y ofrecer entradas que respeten la intención: conocer el local o consultar su carta.
- Asociar precio, formato, suplemento y condición de modo comprensible.
- Diferenciar oferta prevista, servicio abierto y disponibilidad comunicada; no garantizar existencias futuras.
- Separar borradores de publicación y permitir una acción urgente sin publicar otros contenidos pendientes.
- Conservar precios y estados comunes entre idiomas; identificar traducciones afectadas por cambios relevantes.
- Registrar información alimentaria aportada y revisada por el establecimiento; falta de dato no equivale a ausencia de alérgenos ni a seguridad.
- Facilitar la intervención del personal donde la información o adaptación necesita confirmación.
- Producir salidas imprimibles pertinentes; el archivo nuevo no actualiza hojas ya impresas.
- Distinguir la carta propia de un canal externo y reconocer actualizaciones pendientes o fallidas.
- Distinguir consultas, clics y acciones digitales de asistencia física, reservas confirmadas o ventas.
- Preservar identidad sin obstaculizar navegación, legibilidad y condiciones esenciales.

No hay certificación automática de cumplimiento, accesibilidad o seguridad por incorporar iconos, estándares o un complemento.

## 9. Evidencia acumulada y límites

Existe una investigación competitiva maestra de España, Europa sin España y Estados Unidos/Canadá. Contiene una muestra intencional de 59 productos y sus fuentes; no es un censo mundial ni prueba de uso real de todos ellos.

La exploración competitiva general está cerrada. Una nueva consulta se justifica por una decisión concreta que todavía necesite evidencia. No reinicies una búsqueda general por incorporación de un agente nuevo.

Referencias conservadas: BentoBox y Sociavore como focos principales, complementadas por BuonMenu, Menutech, MustHaveMenus y Zenchef según la tarea. Popmenu no es una referencia seleccionada para esta dirección. Se aprovechan patrones sin copiar automáticamente toda la oferta de cada proveedor.

Los paneles privados de los competidores no se consideran auditados por haber visto sus páginas comerciales. Las encuestas internacionales mantienen su contexto; no se extrapolan automáticamente a España ni a cartas de restaurantes cuando investigan otro uso del QR.

No están demostrados todavía la comprensión de Valiris por comensales, la facilidad real de mantenimiento, el ahorro neto, la disposición a pagar, los márgenes ni la ventaja competitiva global.

## 10. Estado actual

| Estado | Contenido |
|---|---|
| Decisiones expresadas por el fundador | Primer módulo; enfoque modular; equilibrio de valor; plantillas y diseño propio de pago; cierre de exploración; paso a ejecución; G1 con Dirección y Producto separados |
| Base aceptada para avanzar | Definición funcional profunda de Storefront + Digital Menu; detalle fino sigue sujeto a diseño y planificación |
| Organización propuesta y usada como base | Seis grupos; 14 perfiles reservables; SEO en G6 con colaboración temprana |
| Dirección de trabajo aclarada | Producto prioritario; marca y web de Valiris avanzan en paralelo según dependencias |
| Pendiente de concretar | Alcance comprometido de oportunidades y conexiones; diseños; estructura técnica; stack; fechas; presupuesto; tarifas; acceso y capacidad de complementos |
| No acreditado como realizado en esta conversación | Agentes ya instanciados, implementación del módulo, pilotos, integraciones activas, validación comercial o web comercial publicada |

El propósito inmediato es preparar un plan ejecutable y empezar el diseño de experiencia. Se ha indicado prototipado sin código antes de la implementación. La petición de máximo esfuerzo no modifica esa secuencia por sí sola.

## 11. Fuentes y precedencia

| Documento | Función |
|---|---|
| Este contexto y protocolo operativo | Incorporación, decisiones posteriores y coordinación; versión inicial propuesta |
| `Valiris_Definicion_Funcional_Storefront_Digital_Menu.md` | Referencia detallada de capacidades y comportamientos |
| `valiris-storefront-impresa.pdf` | Presentación editorial derivada de la definición; el formato no aprueba ni modifica por sí solo su alcance |
| `Valiris_Storefront_Digital_Menu_Investigacion_Maestra.md` | Evidencia, fuentes y análisis por mercados |
| `valiris-bentobox-sociavore.md` | Observación enfocada y capturas de referencias |
| Fase 2D y cierre de investigación | Historia de razonamiento; restricciones anteriores pueden estar superadas por decisiones posteriores |

Ante conflicto: consulta la instrucción más reciente del fundador y las decisiones vigentes sobre esa cuestión; contrasta el comportamiento funcional con su fuente. La investigación sustenta decisiones, pero no prevalece automáticamente sobre un cambio autorizado del proyecto. Si el conflicto sigue sin resolverse y altera tu tarea, déjalo identificado y pregunta por esa decisión.

No supongas que otro agente posee esta conversación, los archivos o tu memoria. Comprueba que tiene el material necesario para su encargo.

## 12. Comunicación

Trabaja y comunica en español salvo encargo distinto. Expón primero el resultado o la recomendación, después la evidencia y sus límites. Utiliza mapas, ejemplos y tablas cuando faciliten decisiones; el fundador prefiere representaciones visuales a hojas de cálculo para entender el proyecto.

Evita elogios vacíos, promesas de liderazgo, jerga innecesaria, teoría sin consecuencia y documentos extensos que repitan lo existente. Un desacuerdo útil incluye motivo, implicación y alternativa. Las preguntas deben ser concretas y proporcionales al impacto de la respuesta.

El siguiente documento define roles, herramientas, encargos, revisión y continuidad.
