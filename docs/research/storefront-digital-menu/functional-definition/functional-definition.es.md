# Valiris — Definición funcional de Storefront + Digital Menu

**Fecha:** 30 de septiembre de 2026. **Estado:** propuesta de producto para discutir; no especificación de software ni compromiso de entrega.

## 1. Dirección acordada y cambio de enfoque

El módulo representa públicamente al restaurante y permite entender su oferta antes y durante la visita. El QR es una forma de entrada, junto al enlace, la web del restaurante y sus canales públicos. La carta y la presencia comparten información, pero sus entradas responden a intenciones distintas: conocer el local y consultar qué tomar.

El usuario ha aceptado desarrollar siete direcciones: identidad, contexto de la oferta, consulta, automatización, idiomas y confianza, distribución y medición. Ha precisado un modelo comercial de **plantillas base y diseño propio realizado por el estudio, también de pago**. Tiene capacidad para abordar funciones ambiciosas y no quiere que se descarten por su dificultad técnica.

Esta propuesta sustituye las restricciones de amplitud del cierre anterior. Importación, búsqueda, filtros, programación y formatos múltiples forman parte de la definición cuando resuelven una situación concreta. El documento anterior se conserva como razonamiento histórico, no como techo funcional.

La aprobación de estas direcciones no significa que se hayan aprobado todos los detalles siguientes. Las capacidades y comportamientos que aquí se concretan son recomendaciones del diseñador. Sus beneficios son esperados; no proceden de pruebas de Valiris con clientes.

**Propuesta central:** una presencia con personalidad, una oferta comprensible y actualizada, y herramientas que permitan al restaurante sostener ambas sin trabajo duplicado.

## 2. Qué significa completo

Completo significa cubrir el recorrido de principio a fin: preparar contenido, revisarlo, publicarlo, consultarlo, actualizarlo, distribuirlo, corregir errores y conservarlo al terminar el servicio. La amplitud se adapta a cada negocio; no exige mostrarle todas las opciones a cada comensal ni configurar todas las capacidades a cada operador.

Una cafetería con una carta estable puede utilizar el mismo producto que un restaurante con menú diario y terraza, con una experiencia de gestión más corta. No estamos definiendo dos productos ni una versión de calidad inferior para el primero.

| Tratamiento | Qué significa en esta propuesta |
|---|---|
| Recomendada | Capacidad que considero parte de la oferta funcional del módulo. Su diseño concreto sigue abierto. |
| Configurable | Capacidad disponible que se activa cuando la oferta o el funcionamiento del establecimiento lo requieren. |
| Oportunidad | Idea con una utilidad plausible que todavía requiere un caso convincente antes de incorporarse como compromiso. |
| Conectada | Capacidad que necesita una relación efectiva con otro módulo, proveedor o canal, además de autorización y datos adecuados. |
| Otro módulo | Trabajo cuya ejecución pertenece a reservas, pedidos, pagos, TPV, reparto, facturación u otra área de Valiris. |

Estos tratamientos no son fases de ingeniería ni equivalen a «ahora / nunca». Permiten decidir con claridad sin convertir una lista extensa en una interfaz extensa.

## 3. Bloque 1 — Presencia, identidad y personalización

### Trabajo que debe resolver

El visitante debe reconocer el restaurante, entender su propuesta y preparar una visita. El comprador debe poder elegir cómo quiere estar representado y cuánto trabajo quiere delegar en el estudio.

| Capacidad | Utilidad y comportamiento propuesto | Tratamiento |
|---|---|---|
| Página pública del local | Nombre, concepto, presentación y acceso claro a la oferta y a la información de visita. | Recomendada |
| Información para visitar | Dirección, mapa, contacto, horarios del local y de cocina, cierres excepcionales y condiciones relevantes. | Recomendada |
| Atributos del establecimiento | Terraza, acceso, opciones para grupos u otras condiciones declaradas por el negocio; información concreta cuando la etiqueta resulte ambigua. | Configurable |
| Historia y contenido editorial | Equipo, origen, producto, proveedores, noticias o eventos informativos cuando expresen una propuesta real. | Configurable |
| Identidad visual | Marca, tipografía, composición, tono, fotografías y recursos propios en presencia y carta. | Recomendada |
| Plantillas base | Composiciones cuidadas, utilizables con materiales modestos y con fotografías selectivas o sin fotografías. | Recomendada |
| Diseño propio por el estudio | Experiencia y dirección visual contratadas, con alcance y revisiones definidos; gestión cotidiana independiente del diseñador. | Configurable |
| Dominio, vista al compartir y contenido descubrible | Dirección reconocible, títulos, información pública y presentación de enlaces coherentes. Favorecer descubrimiento sin garantizar posiciones en buscadores. | Recomendada; dominio propio según oferta |
| Conexión con reservas | Acceso contextual a la experiencia de reserva, conservando la identidad del local. | Conectada |

### Decisión de producto que recomiendo

La personalización debe cambiar la expresión del restaurante y puede cambiar la composición de su experiencia. El catálogo, la publicación, las traducciones y los cambios habituales deberían seguir utilizándose de manera común. Un restaurante con diseño propio debe poder corregir un precio por sí mismo.

No se ha acordado un editor libre para que el dueño diseñe cada pantalla. Es una posibilidad distinta del servicio de diseño del estudio y necesitaría una demanda específica. Recomiendo ofrecer al operador controles útiles de contenido y marca, mientras el estudio realiza la composición a medida.

La lectura, los precios comprensibles y el acceso al contenido son calidad básica en ambas vías. El servicio propio cobra trabajo de diseño y representación singular, no la eliminación de fricciones que perjudicarían a los clientes de las plantillas.

La portada puede tener riqueza editorial. Una entrada destinada a consultar la carta debe respetar esa intención y evitar una portada o promoción obligatorias. Este principio conserva lo útil de las referencias estudiadas sin copiar sus interrupciones.

## 4. Bloque 2 — Oferta, formatos y contexto

### Trabajo que debe resolver

El restaurante debe expresar lo que realmente sirve y sus condiciones. El comensal debe distinguir entre la oferta general, la prevista para una visita y la declarada disponible en el momento.

| Capacidad | Utilidad y comportamiento propuesto | Tratamiento |
|---|---|---|
| Catálogo de productos y categorías | Nombres, descripciones, ingredientes declarados, fotografías opcionales, orden y pertenencia a diferentes cartas. | Recomendada |
| Formatos y variantes | Tapa, media ración, ración, tamaño, copa/botella o alternativa; cada formato identificado junto a su precio. | Configurable |
| Complementos y condiciones | Suplementos, mínimos de personas, unidades, precio por peso o condiciones que afecten a la elección. | Configurable |
| Menús compuestos | Menú diario, degustación o combinado: precio, inclusiones, elecciones, suplementos y vigencia. | Configurable |
| Varias cartas | Desayunos, principal, bebidas, vinos, infantil, temporada u otros conjuntos pertinentes. | Configurable |
| Programación por servicio y fechas | Preparar cambios, indicar periodos de validez y publicar una oferta al comenzar su periodo. | Configurable |
| Oferta por zona o sede | Diferencias reales de producto, formato, precio o servicio; contexto visible y posibilidad de cambiarlo. | Configurable |
| Disponibilidad durante el servicio | Marcar agotado, ocultar lo retirado, recuperar disponibilidad y deshacer acciones accidentales. | Recomendada |
| Excepción manual | Un cierre, cambio de servicio o retirada temporal puede prevalecer sobre la programación habitual, con vigencia clara. | Recomendada |
| Datos recibidos de sistemas operativos | Reutilizar catálogo o disponibilidad donde evite trabajo duplicado y el origen sea fiable. | Conectada |

### Reglas de coherencia

Reutilizar un plato no debería obligar a mantener varias copias. Cuando su precio cambie en terraza, esa diferencia debe mostrarse como condición del contexto; cuando sea un plato distinto, no debe ocultarse esa diferencia bajo una supuesta reutilización.

La elección de contexto debe ser comprensible: «Carta de terraza» o «Desayunos, hasta las 12:00». Un QR puede resolver parte del contexto, pero el comensal debe poder comprobarlo y corregirlo. No necesitamos un QR por mesa si la mesa no cambia la oferta ni una tarea útil del módulo.

Antes de visitar, debe ser posible consultar una oferta aunque ese servicio esté cerrado. La programación orienta sobre lo previsto; no garantiza existencias al llegar. Durante el servicio se muestra el estado que el restaurante o su fuente autorizada comunique.

Al iniciar una jornada conviene revisar los agotados anteriores; no volver a declarar disponible un producto silenciosamente sin una regla elegida por el negocio. Las excepciones deben tener final comprensible para evitar que una retirada de hoy siga afectando la semana siguiente.

Cuando dos reglas se contradigan, el operador debe ver el conflicto antes de publicar: por ejemplo, menú de lunes a viernes y cierre excepcional del miércoles. Debe poder previsualizar qué verá el visitante para una fecha, servicio y zona concretos. Es un problema de comprensión y control, independientemente de cómo se resuelva técnicamente.

## 5. Bloque 3 — Encontrar, entender y elegir

### Trabajo que debe resolver

El comensal necesita orientarse a su ritmo: recorrer una carta corta, encontrar algo concreto, entender un plato desconocido o reducir una oferta extensa. La identidad debe acompañar esas tareas.

| Capacidad | Utilidad y comportamiento propuesto | Tratamiento |
|---|---|---|
| Navegación por categorías | Orientación clara, acceso a secciones y retorno sin perder el punto de lectura. | Recomendada |
| Búsqueda | Encontrar productos por nombre y descripción, con términos pertinentes al idioma mostrado. | Configurable según carta |
| Filtros útiles | Preferencias declaradas, nivel de picante, formatos u otras dimensiones reales de la oferta; estados activos y limpieza fáciles. | Configurable |
| Consulta de alérgenos | Leer información declarada; distinguir información pendiente y facilitar conversación con el personal. | Recomendada |
| Detalle gradual | Información breve para comparar y más contexto para quien lo necesite, sin esconder condiciones esenciales. | Recomendada |
| Explicación de platos | Nombres originales acompañados de explicación, preparación, tamaño o forma de consumo cuando ayuden a entender. | Configurable |
| Destacados del restaurante | Especialidades, novedades o recomendaciones identificadas y gestionadas por el negocio. | Configurable |
| Enlaces a platos y cartas | Compartir o regresar directamente a un contenido; mostrar su vigencia si ha cambiado. | Recomendada |
| Lista personal para comparar | Guardar temporalmente opciones sin cuenta ni confundirlas con un pedido. | Oportunidad |
| Maridajes o relaciones entre productos | Recomendaciones explícitas del local que ayuden a elegir, sin fingir personalización individual. | Configurable |
| Vídeo, explicación sonora o presentación 3D | Utilidad específica para explicar preparación, porciones o una propuesta singular. | Oportunidad |

### Decisión de experiencia que recomiendo

Buscar y filtrar son capacidades disponibles, no elementos obligatorios en todas las cartas. En una carta de diez referencias quizá baste recorrer categorías; en una carta extensa de vinos puede tener sentido filtrar y buscar. El diseño debe activarlas según contenido y tarea, no según el deseo de enseñar funciones.

Recomiendo empezar la consulta alimentaria por información declarada comprensible. Si ofrecemos un filtro para excluir ingredientes o alérgenos, los productos sin información suficiente deben quedar claramente separados; no entrar silenciosamente en resultados que parezcan seguros. Tampoco conviene que desaparezcan sin explicar que falta información.

Las preferencias como «vegetariano» y los alérgenos responden a preguntas diferentes. No deben confluir en un indicador de aptitud universal. Una modificación posible bajo petición requiere confirmación del establecimiento, no una garantía automática de Valiris.

Los destacados son una oportunidad comercial útil para el restaurante, pero deben conservar precio, condiciones y navegación claros. No llamaremos «más vendido» a algo sin datos que sostengan esa afirmación. Un sistema de recomendación individual es una oportunidad distinta, cuya ventaja frente a una selección del propio local tendría que demostrarse.

## 6. Bloque 4 — Preparar, actualizar y publicar

### Trabajo que debe resolver

El restaurante debe pasar de los materiales que ya posee a una oferta revisada, mantenerla durante el servicio y corregir errores con confianza. La automatización aporta valor si reduce trabajo total, incluido el tiempo de revisión.

| Capacidad | Utilidad y comportamiento propuesto | Tratamiento |
|---|---|---|
| Importar cartas | PDF, fotografía, hoja de datos o fuente estructurada; propuesta editable junto al material original. | Recomendada |
| Revisión de importación | Señalar dudas, omisiones y formatos ambiguos; comprobar especialmente precios y contenido alimentario. | Recomendada |
| Edición desde móvil | Cambios habituales sin rehacer el diseño ni recorrer configuración irrelevante. | Recomendada |
| Edición conjunta y duplicación | Reordenar, reutilizar menús y cambiar conjuntos de productos con vista previa del alcance. | Recomendada |
| Borradores y previsualización | Ver carta pública, contextos y traducciones antes de hacerlos visibles. | Recomendada |
| Publicación controlada | Publicar cambios seleccionados; separar un agotado urgente de otros borradores pendientes. | Recomendada |
| Publicación programada | Preparar precios, temporada o menú próximo; comprobar el momento y el contenido previstos. | Configurable |
| Historial y recuperación | Saber qué se cambió, por quién, y corregir o recuperar una versión sin perder toda la carta. | Recomendada |
| Responsabilidades del equipo | Diferenciar quien modifica disponibilidad, edita contenido y publica, cuando el equipo lo necesita. | Configurable |
| Asistencia de texto e imágenes | Preparar descripciones, traducciones o mejoras de material; revisar fidelidad antes de publicar. | Configurable |
| Revisión del contenido afectado | Un cambio de ingrediente puede afectar descripción, etiquetas, alérgenos y traducciones. | Recomendada |
| Fuente externa como origen de cambios | Definir qué información se mantiene allí y qué puede editarse en Valiris; comunicar conflictos y fallos. | Conectada |

### Automatización con valor concreto

Importar debe ahorrar transcripción, no transferir al dueño una carta aparentemente terminada llena de errores difíciles de detectar. Propongo conservar la referencia al original durante la revisión y agrupar las incertidumbres por producto y tipo de dato.

Una fotografía con «24 / 34» puede sugerir dos formatos, pero no demuestra sus nombres. El sistema puede proponer una estructura pendiente; el responsable confirma qué significa cada importe. La ausencia de una mención de alérgenos no demuestra ausencia de alérgenos.

La asistencia puede reescribir información suministrada y mejorar la lectura. No debería inventar ingredientes, procedencia, denominaciones, certificaciones o imágenes que representen falsamente el plato servido. Una fotografía generada puede resultar atractiva y aun así ser una mala representación del restaurante.

Los cambios urgentes y los editoriales son tareas distintas. Marcar un producto agotado debe ser rápido y recuperable; no publicar a la vez una descripción que otro empleado está redactando. El historial debe permitir entender lo ocurrido, sin obligar a un pequeño negocio a adoptar un proceso de aprobación complejo.

Los permisos de las personas y de la empresa pertenecen al sistema común de Valiris; aquí definimos qué acciones del módulo se distinguen. El flujo de carta no debe duplicar toda la administración de usuarios.

## 7. Bloque 5 — Idiomas, información y confianza

### Trabajo que debe resolver

Comprender la misma oferta en diferentes idiomas, con precios y condiciones coherentes, y reconocer qué información está confirmada. Confianza también significa no presentar una conclusión que los datos no permiten.

| Capacidad | Utilidad y comportamiento propuesto | Tratamiento |
|---|---|---|
| Idiomas de presencia y carta | Elegir idioma y conservarlo durante la consulta; también traducir horarios, avisos y condiciones. | Configurable |
| Traducción asistida y revisión | Preparar versiones, comprobarlas y publicar con un responsable identificado internamente. | Recomendada si se ofrecen idiomas |
| Glosario del restaurante | Conservar nombres propios y unificar términos, ingredientes y tono. | Configurable |
| Coherencia de datos comunes | Precio, disponibilidad, formato y vigencia no se mantienen por separado en cada traducción. | Recomendada |
| Traducción pendiente de actualización | Identificar contenido afectado; mostrar alternativa explícita o retirar la versión afectada según relevancia. | Recomendada |
| Ingredientes y alérgenos por variante | Registrar lo declarado y sus diferencias por formato, con estado de revisión. | Recomendada; detalle según oferta |
| Indicaciones del establecimiento | Separar ingredientes declarados, advertencias sobre elaboración y adaptaciones bajo petición. | Recomendada |
| Registro y salida para el personal | Facilitar consulta interna y generación de información revisada, sin reducirla a iconos públicos. | Recomendada |
| Información nutricional | Publicar valores aportados con origen y alcance adecuados cuando el negocio pueda sostenerlos. | Oportunidad |

### Reglas que recomiendo sostener

Una traducción no es otra carta independiente. Si el plato cambia de precio, el importe debe cambiar en todos los idiomas. Si cambia de ingredientes, no debe seguir apareciendo silenciosamente una descripción anterior en inglés como si estuviera vigente. Las advertencias afectan al contenido concreto; no todo cambio requiere detener el sitio entero.

La detección del idioma puede sugerir una versión, pero el visitante debe poder elegir. Los nombres locales pueden conservarse acompañados de explicación; traducir literalmente puede quitar información en vez de añadirla.

Para los alérgenos, recomendamos estados explícitos de información declarada y de revisión pendiente. El restaurante sigue siendo la fuente de sus ingredientes y procesos. No se infiere seguridad desde el nombre de un plato ni se publica una afirmación de ausencia cuando falta el dato.

**Base verificable:** el artículo 6.5 del Real Decreto 126/2015 contempla comunicación oral bajo condiciones, entre ellas un registro escrito o electrónico accesible y la indicación de dónde obtener la información cuando corresponde. Esto fundamenta prestar atención al proceso del establecimiento además de la carta pública; no acredita cumplimiento automático por usar Valiris. [S1]

## 8. Bloque 6 — Acceso, impresión y distribución

### Trabajo que debe resolver

La oferta debe estar al alcance del comensal donde la encuentra y del equipo donde la necesita. Una presentación digital no elimina la necesidad de alternativas o materiales físicos.

| Capacidad | Utilidad y comportamiento propuesto | Tratamiento |
|---|---|---|
| Enlace y QR estables | Cambiar contenidos sin sustituir el material que enlaza a la misma dirección. | Recomendada |
| Entradas con intención | Portada para conocer el local; carta directa para consultar; contexto cuando cambia la oferta. | Recomendada |
| Acceso sin cuenta ni instalación | Consulta pública sin barreras que no aportan a esa tarea. | Recomendada |
| Material para compartir | Enlaces, QR descargables y composición de soportes físicos con identidad legible. | Recomendada |
| Formatos imprimibles | Generar cartas, menú diario y hojas pertinentes con composición específica para papel. | Recomendada |
| Versiones por idioma y uso | Misma información revisada en diferentes salidas, incluidas hojas para el personal. | Configurable |
| Presencia en una web existente | Enlazar o integrar la consulta donde el restaurante ya tiene una presencia útil. | Configurable / conectada |
| Canales externos | Compartir enlaces y, cuando la conexión lo permita, distribuir datos y comprobar resultados. | Conectada para sincronización |
| Pantallas y soportes de sala | Reutilizar oferta para pizarra digital u otros soportes cuando reduzca trabajo real. | Configurable / conectada |
| Consulta con conexión interrumpida | Recuperar contenido previamente cargado, indicando su antigüedad y limitaciones de actualización. | Oportunidad |
| Exportación y continuidad | Recuperar contenido del restaurante y entender dominio, materiales y acceso al terminar el contrato. | Recomendada |

### Una fuente mantenida, distintas presentaciones

La versión en papel merece una composición propia: jerarquía, saltos de página, densidad y contenido pertinentes a su uso. No basta imprimir una captura de la pantalla móvil. Generarla desde la carta vigente reduce duplicación, pero no modifica automáticamente las hojas ya impresas.

El operador debe poder distinguir una salida recién generada de otra que ha quedado antigua. También debe decidir qué cambios exigen reimprimir. Podemos facilitar fechas y avisos; no controlar por software qué documento físico sigue en una mesa.

Compartir el enlace en Instagram o Google es distinto de actualizar automáticamente sus datos. La sincronización requiere una capacidad real del destino y un alcance comprobado. La ayuda oficial de Google indica que los cambios en su editor de menú pueden tardar entre 24 y 48 horas en aparecer. Por eso una promesa de actualización simultánea en todos los canales sería excesiva. [S2]

Una conexión debe explicar destino, contenido enviado, última actualización y problemas pendientes. Si falla un canal externo, la carta propia puede seguir funcionando y el operador necesita saber qué ha quedado desactualizado.

## 9. Bloque 7 — Medición y oferta comercial

### Trabajo que debe resolver

El dueño necesita señales que le ayuden a mantener y presentar mejor su oferta. Valiris necesita vender una prestación concreta y entender cuánto trabajo cuesta entregarla.

| Capacidad | Decisión que puede apoyar | Tratamiento |
|---|---|---|
| Consultas de presencia y carta | Entender qué recorridos digitales se utilizan; distinguirlos de clientes físicos. | Recomendada |
| Origen del acceso | Comparar enlace compartido, campañas y soportes QR identificados, dentro de lo que pueda medirse. | Configurable |
| Uso de categorías, búsqueda y filtros | Detectar dificultad de localización, términos sin resultado o información que falta. | Configurable |
| Interés en platos | Observar consultas y combinarlas con contexto antes de cambiar el orden o los destacados. | Configurable |
| Acciones hacia la visita | Medir clics en mapa, teléfono o reserva como acciones digitales, sin llamarlos visitas o reservas confirmadas. | Recomendada |
| Resultados de otros módulos | Relacionar reservas u otros resultados reales cuando exista la conexión y un alcance de atribución definido. | Conectada |
| Calidad y mantenimiento | Localizar traducciones pendientes, importaciones sin revisar, estados temporales antiguos y salidas desactualizadas. | Recomendada |
| Comparación de cambios | Comprobar una mejora con una pregunta concreta y suficiente actividad; evitar conclusiones de muestras mínimas. | Oportunidad |
| Servicio de alta y diseño | Comercializar preparación de contenido, implantación y representación visual con entregables claros. | Recomendada |
| Actualizaciones delegadas | Ofrecer atención del estudio con volumen, tiempos y tipos de cambios pactados. | Configurable |

### Cómo convertir señales en utilidad

Si se consulta mucho la categoría de desayunos, eso puede justificar comprobar su visibilidad y comprensión; no demuestra ventas de desayunos. Si la búsqueda contiene términos sin resultado, puede faltar contenido o haber una denominación que el visitante no entiende. Si aparecen muchas consultas de alérgenos, puede existir interés o dificultad; no prueba que el producto sea fiable.

La información de mantenimiento es accionable incluso con poco tráfico: «esta traducción requiere revisión» ayuda a corregir una situación. La analítica comercial necesita más cuidado y contexto. El panel debe mostrar decisiones posibles, periodo y limitaciones, en vez de inventar un retorno económico.

La consulta pública no necesita identificar individualmente al comensal. Recomiendo medir lo necesario para las tareas elegidas, con transparencia y las condiciones aplicables a la solución de medición que después se seleccione. No se define aquí una tecnología de seguimiento ni se asume autorización para cualquier recogida de datos.

## 10. Modelo de entrega del estudio

El usuario ha acordado las dos vías de diseño. La separación económica siguiente es una recomendación pendiente de concretar, no una tarifa aprobada.

| Componente | Qué compra el restaurante | Qué debe quedar definido |
|---|---|---|
| Servicio de producto | Presencia publicada, carta gestionable y capacidades contratadas. | Servicio continuo, soporte y condiciones de acceso. |
| Puesta en marcha | Preparación/importación, revisión con el local y entrega lista para uso. | Material recibido, volumen de contenido, revisiones y responsable de validar. |
| Aplicación de plantilla | Representación cuidada a partir de una composición existente. | Opciones de marca y contenido incluidas. |
| Diseño propio | Trabajo del estudio para una identidad y experiencia particulares. | Alcance, entregables, revisiones, conservación de gestión autónoma y mantenimiento posterior. |
| Actualización delegada | El estudio realiza cambios por encargo del negocio. | Tipos de cambios, frecuencia, plazo y atención durante servicio. |
| Evolución del diseño | Nueva composición o ampliación del encargo ya entregado. | Qué es cambio cotidiano y qué es un nuevo trabajo de diseño. |

La viabilidad no se demuestra porque todos reciban algo valioso. Debemos comprobar trabajo real de alta, revisiones, soporte, permanencia y adquisición. La hipótesis de beneficio mutuo es razonable si el restaurante recibe valor que entiende y el estudio cobra el trabajo que efectivamente realiza.

El diseño propio puede elevar el ingreso y la diferenciación. También puede consumir margen si se vende sin límites claros de revisión o si cada actualización necesita al diseñador. Eso es una decisión de servicio comercial, no una razón para renunciar al diseño propio.

## 11. Límites del módulo y conexiones

| Situación | Qué resuelve Storefront + Digital Menu | Dónde continúa |
|---|---|---|
| Quiero reservar tras ver la carta | Información pertinente y acceso a la reserva. | Módulo de reservas; disponibilidad y confirmación de mesa. |
| He elegido lo que quiero tomar | Consulta, comparación y explicación de la oferta. | Personal o módulo de pedidos; una lista personal no es un pedido. |
| Quiero pagar | Mantener clara la oferta y sus precios. | Módulo de pagos y operación. |
| El TPV ya tiene el catálogo | Presentación y datos que realmente se puedan reutilizar. | Conexión autorizada; no convertir este módulo en TPV. |
| El restaurante tiene varias sedes | Identificar sede y mostrar la oferta adecuada. | Administración común del negocio para sedes y equipos. |
| Quiero conocer reseñas o fidelización | Punto de conexión contextual si aporta al recorrido. | Sus módulos; evitar un panel de funciones ajenas dentro de la carta. |

El carácter modular preserva recorridos completos dentro de cada responsabilidad y permite conexiones claras. No justifica omitir el mantenimiento o la corrección de errores, que sí pertenecen a este módulo.

## 12. Calidad transversal

La calidad se evalúa con contenido real: carta corta, carta extensa, texto largo, fotografías parciales, varios idiomas, precios por formatos, avisos y contexto cambiante.

- Lectura móvil, ampliación de texto, contraste, foco, controles comprensibles y navegación con teclado y tecnologías de asistencia son requisitos de diseño y comprobación. Este documento no acredita accesibilidad ya conseguida.
- La información esencial debe entenderse con texto, no solo iconos o color. La identidad no debe dificultar precio, formato, condición o retorno al recorrido.
- La consulta debe seguir siendo útil sin fotografías; fotografías selectivas no deben parecer errores de contenido.
- Los avisos se muestran según relevancia; una promoción no debe impedir consultar la carta.
- El trabajo cotidiano del operador debe poder completarse con controles pertinentes, resultados visibles y recuperación de errores.
- La disponibilidad, la vigencia y el idioma deben expresar lo conocido sin transmitir una certeza mayor.

## 13. Escenarios para comprobar la propuesta

Son escenarios de diseño, **no pruebas ya realizadas**. Permiten juzgar si las capacidades forman un producto coherente.

| Escenario | Qué debería ocurrir | Qué nos haría revisar la propuesta |
|---|---|---|
| Cafetería con diez productos y sin fotos | Carta cuidada y cambios directos; opciones avanzadas fuera del recorrido habitual. | Configurar servicios y filtros para poder publicar una carta sencilla. |
| Restaurante con carta extensa de vinos | Búsqueda y filtros ayudan a reducir opciones sin perder precios por copa/botella. | Más trabajo para usar filtros que para recorrer la carta. |
| Enlace antes de visitar | Conocer local, condiciones y oferta; poder consultar otro servicio previsto. | Solo ver «cerrado» y no acceder a la información de planificación. |
| QR de terraza | Contexto visible, precios pertinentes y posibilidad de volver a la oferta general. | Cambiar de precio sin indicar por qué. |
| Menú diario preparado el día anterior | Publicación en su periodo y distinción de inclusiones, elecciones y suplementos. | Quedar publicado fuera de vigencia o exigir duplicar precios. |
| Se agota un producto durante el servicio | Cambiar ese estado con rapidez, ver el resultado y deshacer. | Publicar también borradores ajenos o mantener agotado indefinidamente. |
| Importar una carta con formatos ambiguos | La duda queda localizada y el responsable confirma antes de publicar. | Inventar nombres de formatos y aparentar revisión completa. |
| Cambiar ingrediente | Revisar información alimentaria y traducciones afectadas. | Precio correcto pero descripción anterior silenciosa en otro idioma. |
| Consultar alérgenos con información pendiente | Comprender la falta y cómo consultar al personal. | Interpretar ausencia de dato como aptitud o garantía de seguridad. |
| Usar diseño propio del estudio | Mantener precios, fotos, avisos y carta sin una intervención de diseño cotidiana. | Tener que contratarnos para cualquier cambio de contenido. |
| Imprimir tras cambiar precios | Generar una salida nueva y reconocer qué materiales anteriores requieren revisión. | Creer que la carta de mesa ya impresa se ha actualizado. |
| Falla la actualización externa | Carta propia vigente y destino externo pendiente claramente identificado. | Prometer que todos los canales están actualizados. |
| Ver muchas consultas de un plato | Interpretarlas como interés digital y contrastar antes de concluir ventas. | Panel que presenta visitas o ingresos sin datos que los acrediten. |
| Finalizar contrato | Recuperar contenido y entender dominio, enlaces y servicios que terminan. | Condiciones de continuidad desconocidas hasta la salida. |

## 14. Qué aprovechamos de la investigación

Se conserva la investigación maestra y la comparación enfocada. No se realiza en este documento una nueva auditoría competitiva. Las observaciones de páginas públicas y las capacidades publicadas por proveedores no demuestran usabilidad de sus paneles ni beneficios comerciales para Valiris.

| Referencia conservada | Principio aprovechable | Desarrollo propuesto para Valiris |
|---|---|---|
| BentoBox / Union Square Cafe | Identidad consistente y carta textual con carácter. | Plantillas y diseño propio con precios y formatos explícitos y entrada directa. |
| Sociavore / PAI | Explicación de platos, variantes y relación entre presencia y oferta. | Detalle gradual, condiciones fuera de títulos excesivos y contexto comprensible. |
| BuonMenu | Facilidad de acceso e importación de contenido. | Preparación asistida con revisión clara del material original. |
| Menutech | Idiomas y formatos impresos/digitales. | Traducciones mantenidas, registro revisado y composición adecuada para cada salida. |
| MustHaveMenus | Contenido reutilizado en varias presentaciones. | Distinción entre publicación propia, salidas generadas y sincronización externa. |
| Zenchef | Continuidad de presencia hacia reserva. | Conexión con reservas conservando su responsabilidad modular. |

Popmenu no es una referencia seleccionada para esta dirección. La investigación histórica se conserva sin convertir cada competidor en un patrón que debamos copiar.

Las modificaciones propuestas son hipótesis de mejora de tareas concretas, no una prueba de que Valiris supere a estos productos o sea el mejor de España.

## 15. Discusión recomendada y siguiente trabajo

Recomiendo discutir el conjunto antes de fragmentarlo en pantallas o tickets. No necesitamos elegir todas las opciones de cada restaurante ahora. Sí necesitamos detectar si falta un trabajo importante, si una regla contradice el funcionamiento de un negocio real o si una capacidad no tiene una utilidad suficiente.

Mi recomendación concreta es sostener tres compromisos: **personalización con gestión autónoma; contexto y actualización sin contradicciones; automatización que conserva revisión y control de lo publicado**. Con ellos podemos explorar una experiencia ambiciosa sin convertir la amplitud en carga para el usuario.

Las primeras comprobaciones pueden usar tres cartas reales como contraste: cafetería sencilla; restaurante con variantes y zonas; restaurante con menú diario e idiomas. Esos contenidos ayudarán a corregir esta definición y después a prototipar sin código los recorridos públicos y del operador. No se propone otra ronda general de exploración competitiva.

## 16. Evidencia y continuidad

### Fuentes puntuales verificadas para esta definición

- **S1.** [BOE — Real Decreto 126/2015, artículo 6.5](https://www.boe.es/buscar/act.php?id=BOE-A-2015-2293): condiciones de disponibilidad y comunicación de información alimentaria. Consulta: 30/09/2026. El registro propuesto no constituye una certificación de cumplimiento.
- **S2.** [Google — Acerca del editor de menú](https://support.google.com/business/answer/9455840?hl=es): contenido del perfil y plazo declarado de 24–48 horas para cambios. Consulta: 30/09/2026. No prueba que una futura conexión de Valiris esté disponible ni autorizada.

### Documentos previos preservados

- Investigación maestra de Storefront + Digital Menu: muestra competitiva y fuentes por regiones.
- Fase 2D: síntesis y decisiones de enfoque históricas.
- Informe BentoBox / Sociavore: observaciones y capturas públicas.
- Cierre de investigación y propuesta integral: razonamiento previo, con restricciones de amplitud ahora sustituidas por esta dirección.

### Estado de decisiones

**Acordado por el usuario:** siete direcciones, capacidad para desarrollar funciones de valor, enfoque modular, plantillas base y diseño propio de pago por el estudio; equilibrio de comensal, restaurante y Valiris; QR como entrada; investigación competitiva cerrada.

**Recomendado en este documento:** capacidades, tratamientos, reglas, calidad y estructura comercial detalladas. Pendiente de discusión y ajustes.

**Todavía no demostrado:** comprensión por comensales, facilidad de mantenimiento, ahorro neto de tiempo, disposición a pagar, márgenes o ventaja competitiva global.

**No realizado:** implementación, prototipos de producto, pruebas con usuarios, integración con canales externos, tarifas definitivas ni contacto con terceros.
