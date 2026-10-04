const page=await figma.getNodeByIdAsync("0:1");
await figma.setCurrentPageAsync(page);
page.name="G2.06 · Proposals v1 · Not approved";
const available=await figma.listAvailableFontsAsync();
const fonts=[{family:"Bricolage Grotesque",style:"ExtraBold"},{family:"Fraunces",style:"Black"},{family:"Space Grotesk",style:"Bold"},{family:"Source Sans 3",style:"Regular"},{family:"Source Sans 3",style:"Bold"}];
for(const f of fonts){if(!available.some(a=>a.fontName.family===f.family&&a.fontName.style===f.style))throw new Error("Font unavailable "+JSON.stringify(f));}
await Promise.all(fonts.map(f=>figma.loadFontAsync(f)));
const ids=[page.id];const frames=[];
function paint(h){return [{type:"SOLID",color:{r:parseInt(h.slice(1,3),16)/255,g:parseInt(h.slice(3,5),16)/255,b:parseInt(h.slice(5,7),16)/255}}];}
function col(parent,name,width,bg,pad=0,gap=20){const n=figma.createAutoLayout("VERTICAL");n.name=name;n.fills=bg?paint(bg):[];n.itemSpacing=gap;n.paddingLeft=pad;n.paddingRight=pad;n.paddingTop=pad;n.paddingBottom=pad;parent.appendChild(n);n.resize(width,100);n.primaryAxisSizingMode="AUTO";n.counterAxisSizingMode="FIXED";ids.push(n.id);return n;}
function row(parent,name,width,gap=24){const n=figma.createAutoLayout("HORIZONTAL");n.name=name;n.fills=[];n.itemSpacing=gap;parent.appendChild(n);n.resize(width,100);n.primaryAxisSizingMode="FIXED";n.counterAxisSizingMode="AUTO";n.counterAxisAlignItems="CENTER";ids.push(n.id);return n;}
function txt(parent,name,s,width,size,color,font=fonts[3],lh=1.16){const n=figma.createText();n.name=name;n.fontName=font;n.fontSize=size;n.lineHeight={unit:"PERCENT",value:lh*100};n.fills=paint(color);n.characters=s;n.textAutoResize="HEIGHT";parent.appendChild(n);n.resize(width,n.height);ids.push(n.id);return n;}
function line(parent,w,c){const n=figma.createRectangle();n.name="Divider";n.fills=paint(c);n.resize(w,2);parent.appendChild(n);ids.push(n.id);return n;}
function svg(parent,name,data,w,h){const n=figma.createNodeFromSvg(data);n.name=name;parent.appendChild(n);n.resize(w,h);ids.push(n.id,...n.findAll().map(v=>v.id));return n;}
const A='<svg xmlns="http://www.w3.org/2000/svg" width="240" height="250" viewBox="0 0 240 250"><path d="M36 36L168 16L210 152L82 192Z" fill="#164B3B"/><path d="M36 36L118 110L168 16Z" fill="#E6F07A"/><path d="M118 110L210 152L168 16Z" fill="#CBD7F1"/><path d="M82 192L86 224M174 172L176 213M30 116L8 100M214 98L230 64" fill="none" stroke="#164B3B" stroke-width="10" stroke-linecap="round"/><ellipse cx="111" cy="137" rx="6" ry="9" fill="#F7F4E8"/><ellipse cx="142" cy="131" rx="6" ry="9" fill="#F7F4E8"/><path d="M116 161Q132 173 148 151" fill="none" stroke="#F7F4E8" stroke-width="6" stroke-linecap="round"/></svg>';
const B='<svg xmlns="http://www.w3.org/2000/svg" width="240" height="250" viewBox="0 0 240 250"><path d="M28 120C28 40 58 20 122 20C193 20 214 74 205 143C198 203 166 214 108 210C50 206 28 179 28 120Z" fill="#B53C26"/><path d="M82 110C82 75 99 65 120 65C148 65 157 85 153 119C149 151 130 160 112 157C91 155 82 138 82 110Z" fill="#FFF0C8"/><path d="M57 184L33 222M176 191L200 220M19 106L6 87M219 130L235 109" fill="none" stroke="#B53C26" stroke-width="10" stroke-linecap="round"/><ellipse cx="71" cy="85" rx="6" ry="8" fill="#FFF0C8"/><ellipse cx="170" cy="85" rx="6" ry="8" fill="#FFF0C8"/><path d="M160 163Q174 165 179 153" fill="none" stroke="#FFF0C8" stroke-width="6" stroke-linecap="round"/></svg>';
const C='<svg xmlns="http://www.w3.org/2000/svg" width="240" height="250" viewBox="0 0 240 250"><path d="M43 20L62 30L81 20L100 30L119 20L138 30L157 20L176 30L195 20L195 198L176 188L157 198L138 188L119 198L100 188L81 198L62 188L43 198Z" fill="#244BDD"/><path d="M75 62H161M75 83H125" stroke="#F5F7FF" stroke-width="8"/><path d="M108 171L148 133L109 133M148 133V173" stroke="#ECA593" stroke-width="12" fill="none"/><ellipse cx="90" cy="111" rx="6" ry="7" fill="#F5F7FF"/><ellipse cx="136" cy="111" rx="6" ry="7" fill="#F5F7FF"/><path d="M74 198L64 229M166 198L181 223M35 146L8 132M203 70L230 58" fill="none" stroke="#244BDD" stroke-width="9" stroke-linecap="round"/></svg>';
const symbols=[
'<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96" viewBox="0 0 96 96"><path d="M10 20H33L45 48L64 10L87 26L59 84H34Z" fill="#164B3B"/></svg>',
'<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96" viewBox="0 0 96 96"><path d="M10 48C10 18 22 9 48 9C76 9 88 27 85 54C82 78 65 88 42 85C20 82 10 70 10 48ZM34 48C34 32 40 29 49 29C61 29 64 39 62 52C60 64 54 66 47 65C38 64 34 57 34 48Z" fill="#B53C26" fill-rule="evenodd"/></svg>',
'<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96" viewBox="0 0 96 96"><path d="M8 14H36L48 45L60 14H88L60 82H36Z" fill="#244BDD"/><path d="M67 58H88V82H67Z" fill="#244BDD"/></svg>'];

if(page.children.some(n=>n.name==="07 · Base and bespoke identity"))throw new Error("Already built");
const root=col(page,"07 · Base and bespoke identity",1440,"#F7F4E8",64,28);root.x=4780;root.y=1500;root.placeholder=true;
txt(root,"Topic","07 / MISMO LOCAL · DOS VÍAS DE EXPRESIÓN · PROPUESTAS",1312,24,"#164B3B",fonts[4]);
txt(root,"Title","Un oficio. Identidades propias.",1312,67,"#164B3B",fonts[0]);
txt(root,"Scope","La dirección de la línea no es una plantilla obligatoria de color, logo o personaje para los clientes.",1312,26,"#164B3B");
const rr=row(root,"Same facts two identities",1312,36);rr.counterAxisAlignItems="MIN";
for(const [name,bg,ink,font] of [["BASE / MUESTRA DE GRAMÁTICA","#FFFFFF","#164B3B",fonts[0]],["A MEDIDA / VOZ DEL RESTAURANTE","#F1E4DB","#583D52",fonts[1]]]){
const r=col(rr,name,638,bg,32,20);
txt(r,"Route",name,574,19,ink,fonts[4]);
txt(r,"Restaurant name","Casa del Patio\ny de la Huerta",574,55,ink,font,1.05);
line(r,574,ink);
txt(r,"Direct entry","Ver carta",574,28,ink,fonts[4]);
txt(r,"Same name","Café con leche",574,28,ink,fonts[4]);
txt(r,"Same amount","Carta general · 1,90 €",574,27,ink);
txt(r,"Same food fact","Contiene leche declarada. Resto de información pendiente.",574,25,ink);
txt(r,"Exact attribution","Powered by Valiris Restaurants",574,18,ink);
txt(r,"Expression limit",name.startsWith("BASE")?"Composición y pareja tipográfica predefinidas por el estudio; controles iniciales por decidir.":"Tipografía, color y ritmo pueden cambiar por encargo. Su coste de diseño y revisión queda separado del contenido.",574,24,ink);}
line(root,1312,"#164B3B");
txt(root,"Shared","Se conserva: nombre del local, hechos mantenidos, consulta directa, distinción declarado/pendiente y atribución exacta.",1312,27,"#164B3B",fonts[4]);
txt(root,"Maintenance","La edición cotidiana del restaurante conserva las mismas responsabilidades en ambas vías. Esta muestra no verifica una herramienta de gestión.",1312,26,"#164B3B");
txt(root,"Status","Fixture híbrido explícito: nombre ficticio nuevo + fragmento factual C1. No cliente real, Home, carta completa ni familia de modelos elegida.",1312,18,"#164B3B");
root.placeholder=false;
return {createdNodeIds:ids,frames:[{id:root.id,name:root.name,width:root.width,height:root.height}]};
