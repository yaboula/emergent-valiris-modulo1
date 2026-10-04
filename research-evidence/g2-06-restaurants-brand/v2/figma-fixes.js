// Consolidated record of two sequential fixes, originally executed separately.
// Delivered IDs only. Inspect first; do not rerun creation in v2.
const page = await figma.getNodeByIdAsync('20:2');
await figma.setCurrentPageAsync(page);
const fonts = [{family:'Gabarito',style:'Black'}, {family:'Source Sans 3',style:'Bold'}, {family:'Source Sans 3',style:'Regular'}];
await Promise.all(fonts.map(f => figma.loadFontAsync(f)));
const family = await figma.getNodeByIdAsync('20:84');
const keys = family.children.find(n => n.name === 'Silhouette keys');
family.insertChild(2, keys);
const label = await figma.getNodeByIdAsync('20:144');
const swatch = label.parent;
const paint = h => [{type:'SOLID',color:{r:parseInt(h.slice(1,3),16)/255,g:parseInt(h.slice(3,5),16)/255,b:parseInt(h.slice(5,7),16)/255}}];
swatch.fills = paint('#FFFDF8');
let band = swatch.children.find(n => n.name === 'Red graphic band — label has cream reading surface');
const created = [];
if (!band) {
  band = figma.createRectangle();
  band.name = 'Red graphic band — label has cream reading surface';
  band.fills = paint('#F83E49'); band.resize(288,60);
  swatch.insertChild(0,band); created.push(band.id);
}
const board5 = await figma.getNodeByIdAsync('20:109');
const rule = board5.findAllWithCriteria({types:['TEXT']}).find(n => n.name === 'Pairing rule');
rule.characters = 'Tinta sobre amarillo, crema y turquesa. Crema sobre violeta y tinta. Rojo: campo gráfico; etiquetas pequeñas sobre crema. Evitar crema sobre rojo/amarillo y tinta pequeña sobre violeta.';
return {createdNodeIds:created,mutatedNodeIds:[family.id,keys.id,swatch.id,rule.id,board5.id],boards:[family,board5].map(b=>({id:b.id,width:b.width,height:b.height}))};
