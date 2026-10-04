// Original G2.06 editorial specimens. No UI library, implementation or tokens.
// Inject LETTERING_A and LETTERING_B as SVG source strings before execution.
if(figma.root.children.some(p=>p.name.startsWith('G2.06 · Proposals v2')))throw new Error('v2 already exists; inspect before retry');
const old=figma.root.children.find(p=>p.id==='0:1');
old.name='G2.06 · Proposals v1 · Rejected by founder';
const page=figma.createPage();page.name='G2.06 · Proposals v2 · Kitchen family · Not approved';
await figma.setCurrentPageAsync(page);
const fonts=[{family:'Gabarito',style:'Black'},{family:'Gabarito',style:'Bold'},{family:'Source Sans 3',style:'Regular'},{family:'Source Sans 3',style:'Bold'}];
const available=await figma.listAvailableFontsAsync();
for(const f of fonts)if(!available.some(a=>a.fontName.family===f.family&&a.fontName.style===f.style))throw new Error('Missing font '+JSON.stringify(f));
await Promise.all(fonts.map(f=>figma.loadFontAsync(f)));
const INK='#251E2E',CREAM='#FFFDF8',YELLOW='#FFD33E',RED='#F83E49',VIOLET='#6C55FF',TURQ='#24DCC5',ORANGE='#FF6B35';
const ids=[page.id],mutated=[old.id],boards=[],uploads=[];
const solid=h=>[{type:'SOLID',color:{r:parseInt(h.slice(1,3),16)/255,g:parseInt(h.slice(3,5),16)/255,b:parseInt(h.slice(5,7),16)/255}}];
function col(parent,name,w,bg=null,pad=0,gap=24){const n=figma.createAutoLayout('VERTICAL');n.name=name;n.fills=bg?solid(bg):[];n.itemSpacing=gap;n.paddingLeft=pad;n.paddingRight=pad;n.paddingTop=pad;n.paddingBottom=pad;parent.appendChild(n);n.resize(w,100);n.primaryAxisSizingMode='AUTO';n.counterAxisSizingMode='FIXED';ids.push(n.id);return n;}
function row(parent,name,w,gap=32){const n=figma.createAutoLayout('HORIZONTAL');n.name=name;n.fills=[];n.itemSpacing=gap;n.counterAxisAlignItems='MIN';parent.appendChild(n);n.resize(w,100);n.primaryAxisSizingMode='FIXED';n.counterAxisSizingMode='AUTO';ids.push(n.id);return n;}
function text(parent,name,s,w,size=26,color=INK,font=fonts[2],lh=1.2){const n=figma.createText();n.name=name;n.fontName=font;n.fontSize=size;n.lineHeight={unit:'PERCENT',value:lh*100};n.fills=solid(color);n.characters=s;n.textAutoResize='HEIGHT';parent.appendChild(n);n.resize(w,n.height);ids.push(n.id);return n;}
function art(parent,name,path,w,h){const n=figma.createRectangle();n.name=name;n.fills=solid(CREAM);n.resize(w,h);parent.appendChild(n);ids.push(n.id);uploads.push({nodeId:n.id,path});return n;}
function svg(parent,name,source,w,h){const n=figma.createNodeFromSvg(source);n.name=name;parent.appendChild(n);n.resize(w,h);ids.push(n.id,...n.findAll().map(n=>n.id));return n;}
function board(number,title,bg=CREAM){const n=col(page,String(number).padStart(2,'0')+' · '+title,1920,bg,72,32);n.x=100+((number-1)%3)*2120;n.y=100+Math.floor((number-1)/3)*3100;n.placeholder=true;text(n,'Sheet and status',String(number).padStart(2,'0')+' / '+title+'   ·   PROPUESTA G2.06 / v2',1776,24,INK,fonts[3]);boards.push(n);return n;}
function finish(n,s='03.10.2026 · Identidad en propuesta. Ilustraciones conceptuales generadas; texto y composición editables.'){text(n,'Evidence boundary',s,1776,22);n.placeholder=false;}
function note(parent,title,body,w=868,bg=null){const c=col(parent,title,w,bg,bg?28:0,12);const tw=w-(bg?56:0);text(c,'Heading',title,tw,32,INK,fonts[1]);text(c,'Body',body,tw,26);return c;}
function lockup(parent,route,w=540){const c=col(parent,'Full line lockup — '+route,w,CREAM,0,0);svg(c,'Valiris custom lettering — '+route,route==='A'?LETTERING_A:LETTERING_B,w,w*190/650);text(c,'Restaurants — unchanged product name','Restaurants',w,58,INK,fonts[0],1.05);return c;}
function entry(parent,w,ink=INK,bg=YELLOW,label='Ver carta'){const c=col(parent,'Direct menu entry — static',w,bg,18,0);text(c,'Direct menu label',label,w-36,30,ink,fonts[3]);return c;}
function fact(parent,w,ink=INK){text(parent,'Fixture item','Café con leche',w,34,ink,fonts[3]);text(parent,'Fixture context and price','Carta general · 1,90 €',w,32,ink);text(parent,'Declared positive','Contiene leche declarada.',w,28,ink,fonts[3]);text(parent,'Unknown is not absence','Resto de información alimentaria pendiente. Consulta al personal antes de elegir.',w,28,ink);}

// 01. Reference analysis: large image excerpts, concise mechanisms.
{
const b=board(1,'APRENDER SIN COPIAR');text(b,'Title','La vida nace\nde una regla.',1776,98,INK,fonts[0],1.0);
const refs=row(b,'Three static references',1776,36);
for(const r of [
['Eat Curious','reference-evidence/eat-curious-1.png','Color a escala de lugar. La comida ancla el relato; la ilustración añade actitud.'],
['Duolingo','reference-evidence/duolingo-1.png','Personajes que actúan. Silueta, pose y mirada explican una idea.'],
['Gorilla','reference-evidence/gorilla-user-reference.png','Una anatomía estable, muchas acciones. Autoría y derechos sin identificar.']]){
const c=col(refs,r[0],568,null,0,18);text(c,'Reference',r[0],568,36,INK,fonts[0]);art(c,'Supplied reference — not our asset',r[1],568,640);text(c,'Mechanism',r[2],568,26);}
const vid=row(b,'Two observed recordings',1776,40);
for(const r of [['Marshmallow / Ragged Edge','reference-evidence/marshmallow-frame-approx-18-5s.png','La elasticidad tiene resolución. Una gramática conecta letras, familia y objetos. Secuencias ampliadas: 4,7–6,3 s y 12,1–14,8 s.'],['Headspace','reference-evidence/headspace-frame-approx-20s.png','Una escena completa crea ambiente. Pequeñas expresiones y aparición del paisaje. Secuencias: 7–9 s y 19,7–23,3 s.']]){const c=col(vid,r[0],868,null,0,18);text(c,'Reference',r[0],868,36,INK,fonts[0]);art(c,'Observed frame — approximate time',r[1],868,488);text(c,'Mechanism',r[2],868,26);}
finish(b,'7 páginas completas · dos vídeos: muestreo de toda la duración + cuatro ampliaciones. No demuestra interacción, conversión ni accesibilidad. Análisis completo y procedencia en Git.');}

// 02. Recommended territory, incorporating founder's kitchen-object direction.
{
const b=board(2,'A / CARÁCTER A LA MESA',YELLOW);
const r=row(b,'Named line and authored scene',1776,40);const l=col(r,'Line identity',600,null,0,30);
lockup(l,'A',550);text(l,'Display proposition','La cocina\ntiene carácter.',600,88,INK,fonts[0],1.02);
text(l,'Draft copy','Un lenguaje propio para presentar cada restaurante y su oferta.',600,32);
art(r,'Kitchen family — selected conceptual scene','assets/a-kitchen-scene.png',1136,757);
const evalr=row(b,'Recommendation reasons',1776,40);
note(evalr,'Una familia de cocina','Pera, berenjena, plato y taza: contornos distintos, el mismo lenguaje de ojos, manos y gestos.');
note(evalr,'Recomendada para decidir','Conexión gastronómica inmediata, escenas sin fotografías y formas que pueden pasar a letras y encuadres. Requiere controlar anatomía y variaciones.');
finish(b,'Territorio creativo interno, sin cambio de nombre. Familia de prueba: no repertorio final ni identidad aprobada. La recomendación v1 queda retirada.');}

// 03. Social alternative: equal finished scene, different semantic construction.
{
const b=board(3,'B / SALA VIVA',TURQ);const r=row(b,'Line identity and social scene',1776,40);const l=col(r,'Line identity',600,null,0,30);
lockup(l,'B',550);text(l,'Display proposition','La mesa\ncobra vida.',600,88,INK,fonts[0],1.02);text(l,'Draft copy','El carácter nace del encuentro: recibir, conversar, compartir espacio.',600,32);
art(r,'Social family — alternative scene','assets/b-sala-viva-scene.png',1136,757);
const evalr=row(b,'Alternative evaluation',1776,40);note(evalr,'Hospitalidad entre personas','Figuras sociales, perfiles y brazos gestuales. Naranja y turquesa; letras con una cadencia más conversada.');note(evalr,'Más dibujo por situación','Aporta cercanía adulta. Depende más de la ilustración de escenas y conecta menos directamente con cocina y alimentos que A. No se mezcla con la familia A.');finish(b);}

// 04. Family construction: images are conceptual art; labels native.
{
const b=board(4,'UNA FAMILIA, CUATRO SILUETAS');text(b,'Title','Distintos cuerpos.\nEl mismo carácter.',1776,90,INK,fonts[0],1.03);
art(b,'Four silhouettes and acting study','assets/a-kitchen-study.png',1776,1184);
const names=row(b,'Silhouette keys',1776,24);
for(const [name,s]of [['PLATO','Recibe / contorno circular con profundidad de borde'],['PERA','Se aproxima / cintura y tallo reconocibles'],['BERENJENA','Escucha / curva continua y cáliz pequeño'],['TAZA','Se incorpora / asa como rasgo propio']])note(names,name,s,426);
const rr=row(b,'Family rules',1776,40);note(rr,'Se comparte','Una pareja de ojos, cejas breves, boca asimétrica; manos crema, miembros tinta y pies apoyados. Escala de manos y colocación facial consistentes.');note(rr,'Se permite variar','Silueta del objeto, inclinación, gesto, mirada y expresión. Estudio inferior: anticipación / bienvenida del plato; curiosidad / reposo de la berenjena.');
finish(b,'La exploración sensorial anterior se conserva en Git. Los personajes no son iconos de dieta, disponibilidad o alérgenos. G2.08 define el repertorio y normaliza los recursos de producción.');}

// 05. Lettering and colour: intentional cuts, full name and readable fonts.
{
const b=board(5,'DE LOS CONTORNOS A LAS LETRAS');text(b,'Title','Curva, corte\ny conversación.',1776,92,INK,fonts[0],1.03);
const rr=row(b,'Logo studies',1776,40);const a=col(rr,'A custom lettering study',868,CREAM,24,20);lockup(a,'A',760);text(a,'Construction','A / curvas tensas, terminales interrumpidos y puntos oblicuos. Dibujo SVG propio, sin exclusividad ni acabado óptico final acreditados.',820,27);
const bb=col(rr,'B custom lettering study',868,CREAM,24,20);lockup(bb,'B',760);text(bb,'Construction','B / trazo gestual e inclinaciones variables. Mismo nombre completo; otra relación entre cuerpo y letra.',820,27);
const sw=row(b,'Palette and text pairs',1776,24);
for(const [name,c,fg]of [['Sandía',RED,INK],['Solar',YELLOW,INK],['Violeta',VIOLET,CREAM],['Tinta',INK,CREAM],['Crema',CREAM,INK]]){const n=col(sw,name,336,c,24,16);text(n,'Color name',name,288,32,fg,fonts[0]);text(n,'Screen reference',c,288,26,fg,fonts[3]);}
const type=row(b,'Display and reading',1776,40);const dl=col(type,'Display',868,null,0,16);text(dl,'Font role','Gabarito Black',868,52,INK,fonts[0]);text(dl,'Display specimen','Buen carácter.\nBuen apetito.',868,82,INK,fonts[0],1.02);
const dr=col(type,'Reading',868,null,0,16);text(dr,'Font role','Source Sans 3 / Regular + Bold',868,36,INK,fonts[3]);text(dr,'Reading specimen','Ñáéüß · Café con leche · 1,90 €\nLos nombres, precios y estados siguen siendo texto. La expresividad se concentra en presentación.',868,32);
text(b,'Pairing rule','Tinta sobre rojo, amarillo, crema y turquesa. Crema sobre violeta y tinta. Evitar crema sobre rojo/amarillo y tinta pequeña sobre violeta. Un campo dominante, acentos subordinados.',1776,28);
finish(b,'OFL de Gabarito y Source Sans 3 conservadas. Binarios de Figma no identificados. Favicon y variantes ópticas requieren producción posterior; no se reduce el nombre completo a 16 px.');}

// 06. Two bounded fragments, identical maintained information.
{
const b=board(6,'DOS INTENSIDADES. LOS MISMOS HECHOS');text(b,'Title','Expresar.\nDejar leer.',1776,96,INK,fonts[0],1.02);
const r=row(b,'Two identity fragments — not full UI',1776,40);
const expressive=col(r,'Expressive presentation fragment',868,YELLOW,36,24);
text(expressive,'Label','PRESENTACIÓN / MUESTRA OPCIONAL',796,24,INK,fonts[3]);text(expressive,'Restaurant identity','Casa del Patio\ny de la Huerta',796,64,INK,fonts[0],1.03);art(expressive,'Selective conceptual kitchen illustration','assets/a-kitchen-scene.png',796,531);entry(expressive,796);fact(expressive,796);text(expressive,'Attribution','Powered by Valiris Restaurants',796,24);
const clear=col(r,'Clear consultation fragment',868,CREAM,36,30);
text(clear,'Label','CONSULTA / SIN PERSONAJES',796,24,INK,fonts[3]);text(clear,'Restaurant identity','Casa del Patio\ny de la Huerta',796,64,INK,fonts[0],1.03);entry(clear,796);text(clear,'Consultation context','Carta general',796,48,INK,fonts[0]);fact(clear,796);text(clear,'Attribution','Powered by Valiris Restaurants',796,24);text(clear,'Identity when character absent','Se conservan nombre, ritmo de letras, curva y acento de color. Los hechos tienen espacio propio.',796,28);
text(b,'Maintenance contrast','1,90 € → 2,00 € se cambia como texto mantenido; no se redibuja un personaje ni se encarga otra composición. La muestra no verifica un editor de contenido.',1776,28,INK,fonts[3]);finish(b,'Fixture híbrido: local ficticio + fragmento factual C1. Ilustración no representa platos reales. No Home completa, navegación, componentes ni interacción implementada.');}

// 07. One conceptual render plus three authored acting keyframes.
{
const b=board(7,'UN MUNDO EN VOLUMEN. UN GESTO CON SENTIDO');text(b,'Title','El mismo mundo,\notra materia.',1776,92,INK,fonts[0],1.02);art(b,'One conceptual 3D hospitality scene','assets/a-kitchen-3d.png',1776,1184);
text(b,'Material boundary','Render conceptual generado. Misma familia; material mate, luz cálida y sombras. No restaurante real, fotografía de oferta ni modelo 3D editable.',1776,28);
art(b,'Three plate acting keyframes','assets/a-plate-storyboard.png',1776,888);
const rr=row(b,'Motion purpose',1776,36);note(rr,'01 / ANTICIPACIÓN','El plato orienta la mirada y recoge el brazo. Prepara la bienvenida.',568);note(rr,'02 / GESTO','Abre la mano y hace espacio. La acción expresa hospitalidad.',568);note(rr,'03 / REPOSO','Baja el brazo y permanece atento. La escena quieta sigue funcionando.',568);
finish(b,'Brief para G2.09: una acción y resolución, sin bucle obligatorio. Alternativa quieta completa; no animar precios, estados alimentarios ni acceso a carta. Tiempos/easing y pruebas quedan pendientes.');}

// 08. Hierarchy, content autonomy, long name and preserved ORILLA.
{
const b=board(8,'EL LOCAL SIGUE SIENDO EL LOCAL');text(b,'Title','Firma del estudio.\nIdentidad del restaurante.',1776,90,INK,fonts[0],1.03);
const hierarchy=row(b,'Three relationships',1776,36);
for(const [title,body]of [['R1 / RECOMENDADA','Restaurante protagonista. Valiris Restaurants firma en segundo plano. Menos exposición del proveedor; más espacio para la identidad local.'],['R2 / CO-MARCAS','Pesos comparables entre local y línea. Más presencia del estudio; más conflicto y trabajo de convivencia, especialmente con nombres largos.'],['R3 / LÍNEA PRIMERO','La línea domina y el local queda subordinado. Más uniformidad; menor identificación del negocio. No recomendada para este encargo.']])note(hierarchy,title,body,568,title.startsWith('R1')?YELLOW:null);
const br=row(b,'Base and bespoke identities — maintained facts',1776,40);
for(const [title,bg,display]of [['BASE / GRAMÁTICA CURADA',CREAM,fonts[0]],['A MEDIDA / EXPRESIÓN PROPIA',TURQ,fonts[1]]]){const c=col(br,title,868,bg,32,20);text(c,'Route',title,804,24,INK,fonts[3]);text(c,'Long fictional restaurant name','Casa del Patio y de la Huerta Mediterránea de San Sebastián',804,58,INK,display,1.05);entry(c,804);fact(c,804);text(c,'Exact attribution','Powered by Valiris Restaurants',804,24);}
text(b,'Localisation contrast','ES: Ver carta / Información alimentaria pendiente.\nDE: Speisekarte ansehen / Weitere Allergeninformationen stehen noch aus.\nÑ · á · ü · ß · 1,90 € · 26,00 € — muestra ilustrativa, no traducción aprobada.',1776,30);
text(b,'Model and maintenance boundary','Dos o tres modelos base, más diseño realmente personalizado. Número, familias y controles iniciales pendientes. El restaurante mantiene contenido cotidiano; el estudio define diseño. Personajes y paleta de la línea no son obligatorios para clientes.',1776,28,INK,fonts[3]);
const oo=row(b,'Preserved ORILLA and coexistence',1776,40);art(oo,'ORILLA v0.2 — untouched source','../../g2-06-art-direction-2026-10-03/storefront-v0.2/02-cartel-revisado-v0.2.png',868,675);note(oo,'ORILLA conserva su voz','Original v0.2 / nodo 9:15. Se muestra sin recolorear ni rediseñar. Comparar jerarquía local, exactitud de atribución, claridad y posibles conflictos. Cualquier adaptación se propone después de selección y revisión por sus responsables.');
finish(b,'Selección de Yahya pendiente. G1 consolida impactos; G4 conserva revisión independiente. G6 / G2.04 / G2.05: checkpoints pendientes, sin consultas inventadas. No cierra #15 ni M1.');}

return {createdNodeIds:ids,mutatedNodeIds:mutated,pageId:page.id,boards:boards.map(b=>({id:b.id,name:b.name,width:b.width,height:b.height})),uploads,fonts,nativeTextCount:boards.reduce((n,b)=>n+b.findAllWithCriteria({types:['TEXT']}).length,0),discovery:{codeConnect:'No source mappings; branding specimens, not application implementation',existingInstances:0,publishedSystem:'N/A: no UI library being built or adopted'}};
