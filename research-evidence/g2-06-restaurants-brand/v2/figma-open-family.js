const page=await figma.getNodeByIdAsync('20:2');
await figma.setCurrentPageAsync(page);
const changes=[
['20:30','02 / A / CARÁCTER A LA MESA · DIRECCIÓN CONCEPTUAL / v2'],
['20:52','Plato, pera, berenjena y taza son cuatro ejemplos. Repertorio abierto a comida, cocina y restaurante, con un lenguaje visual compartido.'],
['20:56','Idea de dirección, no branding definitivo. Personajes, colores y detalles exploratorios; el repertorio no se limita a estos cuatro ejemplos.'],
['20:85','04 / UNA FAMILIA ABIERTA · DIRECCIÓN CONCEPTUAL / v2'],
['20:86','Una gramática.\nMuchas posibilidades.'],
['20:106','Libertad de repertorio'],
['20:107','Cualquier elemento de comida, cocina o restaurante puede entrar en la familia. Estos cuatro son muestras; silueta, gesto y expresión conservan parentesco.'],
['20:108','Idea de dirección, no familia final. Anatomía y detalles se ajustarán después. Los personajes no indican dieta, disponibilidad ni alérgenos. G2.08 desarrolla producción.'],
['20:110','05 / LETRAS Y COLOR · EXPLORACIÓN DE DIRECCIÓN / v2'],
['20:166','Paleta, lettering y fuentes exploratorios: no branding definitivo. OFL conservadas; binarios de Figma no identificados. Producción y ajuste óptico posteriores.']
];
const targets=await Promise.all(changes.map(async([id,characters])=>({node:await figma.getNodeByIdAsync(id),characters})));
const fonts=new Map();
for(const {node} of targets){if(node.type!=='TEXT')throw new Error('Expected text: '+node.id);for(const segment of node.getStyledTextSegments(['fontName']))fonts.set(JSON.stringify(segment.fontName),segment.fontName);}
await Promise.all([...fonts.values()].map(font=>figma.loadFontAsync(font)));
for(const {node,characters} of targets)node.characters=characters;
page.name='G2.06 · Proposals v2 · Open kitchen family · Not final branding';
const family=await figma.getNodeByIdAsync('20:84');family.name='04 · UNA FAMILIA ABIERTA';
const ids=['20:29','20:84','20:109'];
const names=['02-a-caracter-a-la-mesa.png','04-kitchen-family.png','05-lettering-color.png'];
const boards=await Promise.all(ids.map(id=>figma.getNodeByIdAsync(id)));
for(let i=0;i<boards.length;i++)figma.io.write(names[i],await boards[i].exportAsync({format:'PNG',constraint:{type:'SCALE',value:1}}));
return {mutatedNodeIds:[page.id,family.id,...targets.map(t=>t.node.id)],boards:boards.map(b=>({id:b.id,name:b.name,width:b.width,height:b.height})),changes:targets.map(({node})=>({id:node.id,name:node.name,characters:node.characters})),status:'Direction idea, not definitive branding; four examples, open culinary repertoire; colors and details exploratory'};
