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

if(page.children.some(n=>n.name==="04 · Brand hierarchy"))throw new Error("Already built");
const ink="#164B3B",paper="#F7F4E8";
const h=col(page,"04 · Brand hierarchy",1440,paper,64,30);h.x=100;h.y=1500;h.placeholder=true;
txt(h,"Topic","04 / RELACIÓN ENTRE MARCAS · PROPUESTAS",1312,24,ink,fonts[4]);
txt(h,"Title","Quién firma. Quién recibe.",1312,72,ink,fonts[0]);
txt(h,"Roles","Valiris: estudio paraguas  →  Valiris Restaurants: línea  →  Restaurante: negocio que recibe al comensal",1312,26,ink);
const hr=row(h,"Three viable relationships",1312,26);hr.counterAxisAlignItems="MIN";
const choices=[
{label:"R1 / RESTAURANTE PROTAGONISTA",line:"Firma de oficio discreta",localSize:43,lineSize:18,reco:true,text:"Recomendada. La línea se reconoce en su firma y sus reglas, con menor presencia en el cliente."},
{label:"R2 / MARCAS COMPARTIDAS",line:"Dos identidades visibles",localSize:34,lineSize:34,reco:false,text:"Más recuerdo de Valiris; más competencia entre nombres y más acuerdos de convivencia."},
{label:"R3 / LÍNEA PROTAGONISTA",line:"Valiris toma el primer plano",localSize:25,lineSize:48,reco:false,text:"Coherencia del proveedor; el local se parece a un miembro de plataforma. No recomendada."}];
for(const c of choices){const card=col(hr,c.label,420,"#FFFFFF",24,20);
txt(card,"Relationship label",c.label,372,18,ink,fonts[4]);
if(c.reco){txt(card,"Restaurant","Casa del Patio\ny de la Huerta",372,c.localSize,ink,fonts[0]);txt(card,"Menu entry","Ver carta",372,26,ink,fonts[4]);txt(card,"Signature","Powered by Valiris Restaurants",372,c.lineSize,ink);}
else{txt(card,"Line","Valiris Restaurants",372,c.lineSize,ink,fonts[0]);line(card,372,ink);txt(card,"Restaurant","Casa del Patio y de la Huerta",372,c.localSize,ink,fonts[0]);txt(card,"Menu entry","Ver carta",372,26,ink,fonts[4]);txt(card,"Signature","Powered by Valiris Restaurants",372,18,ink);}
txt(card,"Consequences",c.text,372,24,ink);}
line(h,1312,ink);
const br=row(h,"Design routes",1312,36);br.counterAxisAlignItems="MIN";
for(const [name,body] of [
["MODELOS BASE","Se comparte gramática, lectura y firma; el nombre, hechos y recursos son del local. Dos o tres modelos es intención: no son estas tres alternativas."],
["DISEÑO A MEDIDA","Puede cambiar composición, tipo, color y carácter del restaurante. Mantiene acceso, datos y actualización autónoma. No exige encargos por cada precio."]]){const x=col(br,name,638,null,0,14);txt(x,"Route",name,638,24,ink,fonts[4]);txt(x,"Route detail",body,638,27,ink);}
txt(h,"Umbrella limit","No hay marca visual paraguas aprobada en estas fuentes. No se exporta el personaje de Restaurants a todo Valiris.",1312,24,ink);
txt(h,"Status","Locales ficticios · fragmentos de identidad · jerarquía pendiente de selección · sin navegación ni UI completa",1312,18,ink);h.placeholder=false;frames.push({id:h.id,name:h.name,width:h.width,height:h.height});
const s=col(page,"05 · Bounded stress specimens",1440,paper,64,26);s.x=1660;s.y=1500;s.placeholder=true;
txt(s,"Topic","05 / HACER SITIO · CONTRASTES ACOTADOS",1312,24,ink,fonts[4]);
txt(s,"Title","El carácter deja leer.",1312,72,ink,fonts[0]);
txt(s,"Scope","Muestras estáticas de identidad: no carta completa, controles, responsive, traducciones revisadas ni prueba de uso.",1312,25,ink);
const r1=row(s,"Long name and locale",1312,36);r1.counterAxisAlignItems="MIN";
const sn=col(r1,"Long name without photos",638,"#FFFFFF",26,14);
txt(sn,"Label","NOMBRE LARGO / SIN FOTO",586,18,ink,fonts[4]);
txt(sn,"Venue","Restaurante Casa del Patio y de la Huerta del Mercado",586,44,ink,fonts[0],1.08);
txt(sn,"Entry","Ver carta",586,26,ink,fonts[4]);
txt(sn,"Footer","Powered by Valiris Restaurants",586,18,ink);
txt(sn,"Limit","Nombre ficticio. Reparte líneas y altura; no comprime ni abrevia el negocio.",586,22,ink);
const loc=col(r1,"Language representative",638,"#FFFFFF",26,14);
txt(loc,"Label","ES / DE · PRUEBA DE LONGITUD Y GLIFOS",586,18,ink,fonts[4]);
txt(loc,"Glyphs","Ñáéüß · 1,90 € · 26,00 €",586,36,ink,fonts[0]);
txt(loc,"ES","Ver carta",364,30,ink,fonts[4]);
txt(loc,"DE","Die Speisekarte ansehen",364,30,ink,fonts[4]);
txt(loc,"Language limit","Alemán ilustrativo, no traducción aprobada. El nombre propio permanece. Otros idiomas y RTL pendientes.",586,23,ink);
const r2=row(s,"Facts without characters",1312,36);r2.counterAxisAlignItems="MIN";
const p=col(r2,"C2 amount context",638,"#FFFFFF",26,12);
txt(p,"Label","C2 / FRAGMENTO FICTICIO / DATOS LEGIBLES",586,18,ink,fonts[4]);
txt(p,"Item","Tabla de quesos artesanos de leche cruda, membrillo y pan de masa madre",586,28,ink,fonts[4]);
txt(p,"Context price","Terraza · media tabla · 26,00 €",586,28,ink,fonts[4]);
txt(p,"Supplement","Pan extra · +2,20 €",586,25,ink);
txt(p,"Declared","Leche y gluten declarados en el ejemplo.",586,24,ink);
txt(p,"Boundary","Sin personaje, sin foto, sin color como único significado. Solo este formato/contexto; no es la carta completa.",586,22,ink);
const f=col(r2,"C3 known versus pending",638,"#FFFFFF",26,12);
txt(f,"Label","C3 / L10c HISTÓRICO / NO MENÚ ACTUAL",586,18,ink,fonts[4]);
txt(f,"Current ES","Crema de calabaza con yogur",586,28,ink,fonts[4]);
txt(f,"Known","Contiene leche declarada.",586,26,ink,fonts[4]);
txt(f,"Pending","Resto de información alimentaria pendiente. Consulta al personal antes de elegir.",586,24,ink);
txt(f,"EN fallback","Description available in Spanish. Translation being updated.",586,23,ink);
txt(f,"Boundary","Fixture fechado 1 octubre. No se infiere seguridad ni se presenta la receta EN antigua.",586,22,ink);
line(s,1312,ink);
const mini=row(s,"Small monochrome mark",1312,22);
for(const size of [16,24,48]){svg(mini,"A symbol "+size+"px",symbols[0],size,size);txt(mini,"Size "+size,size+" px",100,20,ink);}
txt(mini,"Small mark limit","Símbolo a una tinta. El nombre acompaña la atribución; reconocimiento y favicon final pendientes.",680,21,ink);
txt(s,"Content autonomy","C1: 1,90 € → 2,00 € usa la misma voz de datos. Cambiar un importe no obliga a rehacer el pliegue.",1312,24,ink,fonts[4]);
txt(s,"Status","G2.06 / v1 · autoevaluación estática, sin revisión G4, interacción, accesibilidad integral ni datos reales.",1312,18,ink);s.placeholder=false;frames.push({id:s.id,name:s.name,width:s.width,height:s.height});
const o=col(page,"06 · ORILLA coexistence comparison",1440,paper,64,28);o.x=3220;o.y=1500;o.placeholder=true;
txt(o,"Topic","06 / ORILLA · ORIGINAL PRESERVADO + FIRMA PROPUESTA",1312,24,ink,fonts[4]);
txt(o,"Title","Coexistir con ORILLA.",1312,72,ink,fonts[0]);
txt(o,"Scope","Comparación por separado. No se recolorea, redibuja ni superpone la nueva identidad al original seleccionado.",1312,26,ink);
const orow=row(o,"Original beside line signature",1312,36);orow.counterAxisAlignItems="MIN";
const original=col(orow,"Selected source and caption",824,null,0,16);
const image=figma.createRectangle();image.name="ORILLA source raster — unchanged";image.resize(824,641);image.fills=paint("#FFFFFF");original.appendChild(image);ids.push(image.id);
txt(original,"Source label","ORILLA / v0.2 / nodo 9:15\nImagen conceptual generada; platos ficticios. Fuente local verificada.",824,23,ink,fonts[4]);
const os=col(orow,"Proposed line signature — separate",452,"#FFFFFF",26,22);
txt(os,"Proposal label","PROPUESTA R1 / FIRMA SEPARADA",400,19,ink,fonts[4]);
svg(os,"A mark",symbols[0],48,48);
txt(os,"Exact attribution","Powered by Valiris Restaurants",400,22,ink);
line(os,400,ink);
txt(os,"Principle","ORILLA conserva nombre, menta, frambuesa y peso culinario.",400,29,ink,fonts[4]);
txt(os,"Restriction","No añadir el personaje junto al plato. No convertir ORILLA en una variante verde de la línea.",400,25,ink);
txt(os,"Next contrast","Tras seleccionar: comparar firma tipográfica neutra frente a símbolo discreto, en copia identificada. G1 coordina; G4 revisa aplicación.",400,24,ink);
txt(o,"Risk","La firma cromática de la línea puede competir con ORILLA. En clientes se propone versión a una tinta adaptada al contraste del local.",1312,26,ink,fonts[4]);
txt(o,"Status","No adaptación aprobada ni prueba funcional. Original seleccionado intacto. Guía fuente: 4f97693 / PR #22.",1312,18,ink);
o.placeholder=false;frames.push({id:o.id,name:o.name,width:o.width,height:o.height});
return {createdNodeIds:ids,frames,sourceImageTarget:image.id};
