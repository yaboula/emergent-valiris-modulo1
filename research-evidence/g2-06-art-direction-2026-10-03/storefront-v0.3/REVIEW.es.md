# G2.06 - ORILLA: direccion elegida y contrastes v0.3

Propietario: G2.06, identidad y direccion de arte. Fecha: 2026-10-03. Alcance: Storefront, no implementacion. Estado: seleccion creativa confirmada; muestras de aplicacion producidas y autoinspeccionadas. No cierre del ciclo completo.

## Decision

Yahya elige Cartel abierto revisado como direccion, la muestra central 9:15 del tablero v0.2. El archivo de referencia vinculante es ../storefront-v0.2/02-cartel-revisado-v0.2.png. No es el cartel inicial ni una de las propuestas descartadas v0.1. La seleccion no aprueba tipografia exacta, sistema completo, comportamiento, accesibilidad, rendimiento o resultados comerciales.

## Invariantes De La Direccion

- Nombre con presencia grafica y alimento protagonista sobre un campo compartido, no una foto pegada a una plantilla.
- Fondo luminoso menta, plano frambuesa, tinta muy oscura; comida como objeto recortado y profundidad por luz/sombra coherentes.
- Nombre, propuesta culinaria y entrada Ver carta legibles antes de desplazarse. UI contenida, no tarjetas decorativas.
- Ritmo editorial posterior que cambie escala sin pegar una carta al hero.
- No reconstruir UX, no imponer esta estetica a todas las cocinas, no atribuir platos reales a las imagenes.

## Contrastes De Este Turno

Se produjo una composicion movil del Storefront elegido y una variante sin fotografias. Son pruebas de aplicacion, no otra ronda de tres alternativas ni reinterpretaciones de la direccion. Las nuevas muestras quedan propuestas hasta revision; solo el original central esta seleccionado por Yahya.

Sin fotos no significa inventar fotografias fieles: la variante explorara recursos ilustrados conceptuales reutilizables por categoria, cuya procedencia y coste de preparacion deben quedar explicitos. No se supone que todos los restaurantes aportaran fotos. Tampoco una ilustracion implica fidelidad a la receta.

## Resultado Y Acceso

[Figma: muestras Storefront v0.3](https://www.figma.com/design/miM4ul2l4Q6ZwJNfAJeN38?node-id=15-2). Pagina 0:1, tablero 15:2, movil 15:10, sin fotos 15:15. Mismo archivo Valiris; no se altera la imagen seleccionada 9:15. Se actualizan solamente las anotaciones de su seleccion.

| Artefacto | Decision visible | Limite observado |
| --- | --- | --- |
| 01-storefront-mobile-v0.3.png | Nombre en una linea, descriptor en dos, Ver carta antes del producto; alimentos recompuestos sobre los planos menta/frambuesa; comienzo de La cocina. | Nombre cercano a los margenes y suficiente para ORILLA, no evidencia para nombres largos. Menu e idioma son controles dibujados, no operables. |
| 02-no-photo-illustrated-v0.3.png | Misma gramatica sin fotos del restaurante: alimentos dibujados por categoria, campos cromaticos y jerarquia permanecen. | Sigue necesitando recursos ilustrados del estudio. No demuestra cero activos; profundidad mas grafica y tono menos sensorial que la fotografia. |
| 02-no-photo-failed-v0.3.png | Intento inicial retenido como evidencia de correccion. | No cumple: apariencia fotografica/CGI demasiado realista. No usar como variante sin fotos. |

La variante ilustrada es una propuesta de repertorio reutilizable del estudio, no un pack entregado ni un encargo por cada plato. Evita exigir fotos del restaurante, pero no elimina el trabajo de recursos, revision de formas y derechos/procedencia. Su coste no se ha estimado. Los dibujos no se utilizan como evidencia de ingredientes, dieta, alergenos, cantidad o receta.

## Comprobacion Del Autor

- Los prompts adjuntan el PNG realmente elegido. La correccion ilustrada utiliza el intento fallido como referencia editable. Prompts completos y procedencia en prompts.txt y manifest.json.
- Movil solicitado a 390 x 844; ImageGen devuelve 853 x 1844. Se coloca en Figma con FIT a 390 x 843, relacion conservada con redondeo inferior a 1 px. Captura especifica mobile-at-390px-v0.3.png inspeccionada a 390 x 843, no solo a resolucion ampliada.
- En esa captura: ORILLA completo, descriptor legible en dos lineas, Ver carta visible, plato central completo y comienzo de la siguiente seccion. No solapamientos observados entre esos bloques. Es una observacion estatica del autor, no prueba con usuarios.
- Sin fotos solicitado 1440 x 1120, salida 1422 x 1106; Figma usa esa resolucion con FIT. El primer intento presentaba comida realista. Se corrigio a ilustracion claramente grafica y se confirmo visualmente la diferencia.
- Dos subidas a Figma confirmaron success y nodo esperado. Lectura posterior de IMAGE fills confirma hashes y FIT. Diez anotaciones con altura automatica HEIGHT y ancho dentro del padre. Tablero 2050 x 1534, captura figma-board-v0.3.png inspeccionada; notas completas y sin solapamiento observado.
- Originales de ImageGen preservados; copias locales con SHA-256 en manifest.json. Las muestras son raster, no UI editable ni activos ilustrados aislados. Las anotaciones si son editables.
- No se ha validado contraste integral, reflow/zoom, orden de foco, menu desplegado, traducciones, motion, rendimiento o mantenimiento. No se ejecutan tests de software: no se implemento software.

## Traspaso Y Siguiente Accion

G2.06: desarrollar la continuidad editorial del Storefront sin repetir el hero, con significado culinario y visita, y contrastar nombre largo, idiomas/estado pendiente y recursos limitados. No insertar una lista de carta para llenar la pagina. Conservar ORILLA y Cartel abierto revisado como referencia seleccionada.

UI/G2.03: muestras de estructura y escala, no conducta aprobada nueva. Registrar dimensiones y diferencias entre presentacion y consulta; mantener la entrada directa a carta. Precisar fuentes reales antes de construir, sin inferir una familia del raster.

Contenido/SEO: descriptor culinario propuesto y ficticio. Visita requiere hechos suministrados antes de mostrar ubicacion u horarios. No llenar huecos con supuestas promesas del restaurante. Las imagenes no son texto web rastreable; la estrategia publica auditada sigue vigente.

Recursos: mantener fotografia/ilustracion como vias separadas dentro de la composicion, sin mezclarlas por defecto. Preparar recursos por categoria, comprobando platos reales cuando se suministren. Una pagina ilustrada no demuestra fidelidad a una carta.

Motion: sigue pendiente una muestra observable con un momento motivado y alternativa reducida. No animar por defecto cada alimento ni demorar Ver carta. Ninguna imagen acredita movimiento.

Traspasos preparados, no enviados; especialistas y revision G4 no se presumen activos. G1 consolida consecuencias cuando corresponda. Yahya ya selecciono direccion; futuras composiciones y recursos siguen sujetos a revision, no se solicita elegir direccion otra vez.

## Limites

Menu Digital sigue separado. Casos C1-C3 y sus reglas se conservan; no se rehacen sus recorridos en este turno. Estado alimentario/traducciones, contexto/precio/formato y carta diaria se desarrollaran visualmente en su superficie correspondiente. No se acredita motion con imagenes ni se cierra el primer ciclo completo o M1.
