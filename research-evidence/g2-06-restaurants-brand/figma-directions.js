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
const ds=[
{id:"A",name:"HACER SITIO",subtitle:"Recomendada · acogida con criterio",bg:"#F7F4E8",ink:"#164B3B",accent:"#E6F07A",soft:"#CBD7F1",font:fonts[0],display:"Valiris\nRestaurants",phrase:"Cada local tiene su sitio.",body:"Un pliegue abre espacio. La línea firma el oficio; el restaurante ocupa la escena.",character:A,form:"Pliegues asimétricos / gesto abierto",benefit:"Personaje separable de datos. Funciona sin fotos.",limit:"El símbolo necesita su nombre. No sustituye la marca del local."},
{id:"B",name:"SOBREMESA TIPOGRÁFICA",subtitle:"Alternativa · conversación editorial",bg:"#FFF0C8",ink:"#B53C26",accent:"#ECA593",soft:"#2C2A49",font:fonts[1],display:"Valiris\nRestaurants",phrase:"Una carta con conversación.",body:"Las letras toman asiento. Serifa carnosa, contraformas y personajes que nacen del tipo.",character:B,form:"Letras / curvas / ritmo de conversación",benefit:"Gran personalidad con pocos recursos.",limit:"Mayor ajuste tipográfico. Riesgo de nostalgia y voz demasiado dominante."},
{id:"C",name:"COMPÁS DE SALA",subtitle:"Alternativa · orientación gráfica",bg:"#F5F7FF",ink:"#244BDD",accent:"#ECA593",soft:"#17224C",font:fonts[2],display:"VALIRIS\nRESTAURANTS",phrase:"Buen ritmo. Carta clara.",body:"La energía de sala se convierte en bandas y señales. El carácter nace del ritmo y la dirección.",character:C,form:"Bandas / recortes / alineación",benefit:"Orden legible y variación por composición.",limit:"Puede parecer señalética genérica o sistema de pedidos."}
];
for(let i=0;i<ds.length;i++){
const d=ds[i];if(page.children.some(n=>n.name==="0"+(i+1)+" · "+d.id+" · "+d.name))throw new Error("Already built");
const root=col(page,"0"+(i+1)+" · "+d.id+" · "+d.name,1440,d.bg,64,28);root.x=100+i*1560;root.y=100;root.placeholder=true;
txt(root,"Direction",d.id+" / "+d.name+"       "+d.subtitle,1312,24,d.ink,fonts[4]);
const hero=row(root,"Wordmark and character — concept only",1312,40);
const words=col(hero,"Line brand — type-set proposal",872,null,0,18);
txt(words,"Line name",d.display,872,d.id==="C"?83:100,d.ink,d.font,1.02);
txt(words,"Draft line copy",d.phrase,872,32,d.ink,fonts[4]);
svg(hero,"Character — conceptual, not a family",d.character,400,417);
line(root,1312,d.ink);
const spec=row(root,"Language",1312,32);
const left=col(spec,"Type and graphic grammar",650,null,0,12);
txt(left,"Type",d.font.family+" + Source Sans 3",650,26,d.ink,fonts[4]);
txt(left,"Grammar",d.form,650,24,d.ink);
txt(left,"Reason",d.body,650,26,d.ink);
const sw=col(spec,"Palette and mark",630,null,0,16);
const swrow=row(sw,"Palette",630,12);
for(const c of [d.ink,d.bg,d.accent,d.soft]){const s=col(swrow,"Swatch "+c,148,c,12,8);s.minHeight=70;txt(s,"Hex",c,124,18,c===d.ink||c===d.soft?d.bg:d.ink,fonts[4]);}
const mr=row(sw,"Symbol and name",630,20);svg(mr,"Symbol — not standalone attribution",symbols[i],64,64);txt(mr,"Naming boundary","Valiris Restaurants\nNombre conservado · sin renombrar",540,24,d.ink,fonts[4]);
line(root,1312,d.ink);
const proof=col(root,"Restaurant-led bounded specimen",1312,"#FFFFFF",28,12);
txt(proof,"Specimen label","FRAGMENTO DE IDENTIDAD · LOCAL FICTICIO · SIN FOTOGRAFÍA",1256,18,d.ink,fonts[4]);
txt(proof,"Restaurant name","Casa del Patio y de la Huerta",1256,48,d.ink,d.font);
txt(proof,"Direct menu label","Ver carta",1256,26,d.ink,fonts[4]);
txt(proof,"Attribution","Powered by Valiris Restaurants",1256,18,d.ink);
const pros=row(root,"Evaluation",1312,36);
txt(pros,"Gain","Aporta: "+d.benefit,638,22,d.ink,fonts[4]);
txt(pros,"Trade-off","Límite: "+d.limit,638,22,d.ink);
txt(root,"Approval status","G2.06 / v1 / 03.10.2026 · Propuesta estática. Tipos reales; dibujos conceptuales vectoriales. No UI ni identidad aprobada.",1312,18,d.ink);
root.placeholder=false;frames.push({id:root.id,name:root.name,width:root.width,height:root.height});
}
return {createdNodeIds:ids,frames,fontNames:fonts,characters:[A,B,C],symbols};
