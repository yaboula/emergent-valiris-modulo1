"""Reproducible static SVG design boards; this is not a product application.

Only reads the frozen project inputs and writes G2.07 evidence. Fonts are local
exploratory substitutes; no font files are copied. Every text block stays text.
"""
from pathlib import Path
from xml.sax.saxutils import escape
from PIL import ImageFont
import argparse, hashlib, json, re

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'research-evidence/g2-07-storefront'
BASE = '4893d501b750efd1bb9149ff695564f0d2df227b'
COPY_SHA = '4b382bebe5d5c6cad21a7edcaffab053c433a0e9'
IA_SHA = '70512d7a3d1afcd7f3aa0c9823a4d6e7b08dde8c'
SEO_SHA = '7c233f1b5b94257312ab92ca8c9c859c7a6c2c64'
C = {'paper':'#FFF8EC','ink':'#20251E','muted':'#53594C',
     'coral':'#FA735A','blue':'#243EB8','pink':'#F7CADD',
     'mint':'#DDEBBE','yellow':'#F3DE8A','line':'#CCC6B8','white':'#FFFFFF'}
FILES = {'copy':'docs/design/m1-storefront-content-and-copy.md',
         'case':'docs/design/orilla-case.md',
         'ia':'docs/design/m1-storefront-information-architecture.md',
         'journey':'docs/design/m1-connected-journey.md',
         'brand_guide':'docs/design/valiris-restaurants-brand-refinement.md',
         'reference_register':'research-evidence/g2-06-restaurants-brand/refinement/selected-three-references-2026-10-03.es.md',
         'selected_triptych':'research-evidence/g2-06-restaurants-brand/refinement/signature-and-first-model/02-expresion-sin-personajes.png'}

def table(path, prefix):
    rows = {}
    for line in (ROOT / path).read_text(encoding='utf-8').splitlines():
        if not line.startswith('| ' + prefix): continue
        cells = [x.strip().replace('**','') for x in line.strip('|').split('|')]
        key = cells[0].split(' / ')[0]
        if key not in rows: rows[key] = cells[1:]
    return rows

COPY = table(FILES['copy'], 'ORI-COPY-')
CASE = table(FILES['case'], 'ORI-')
FONTS = {'body':('Segoe UI','C:/Windows/Fonts/segoeui.ttf'),
         'bold':('Segoe UI','C:/Windows/Fonts/segoeuib.ttf'),
         'display':('Arial Black','C:/Windows/Fonts/ariblk.ttf')}

def copy(code, phone=False):
    row = COPY['ORI-COPY-'+code]
    value = row[1] if phone and code.startswith('H') else row[0]
    return row[0] if value == 'Same' or value.startswith('Same,') else value

def clean(s): return s.replace('**','').replace('`','')

def wrap(s, width, font):
    # Keep decimal amount + euro and quantity + unit together when possible.
    s = re.sub(r'(\d(?:[\d,.]*)?) (€/ persona|€ / persona|€|ml)', lambda m:m[1]+'\u00a0'+m[2], s)
    lines=[]
    for para in s.split('\n'):
        line=''
        for word in para.split(' '):
            candidate = line+' '+word if line else word
            # Reserve 4% for observed PIL/librsvg/browser font-metric variance.
            if line and font.getlength(candidate)>width*.96:
                lines.append(line); line=word
            else: line=candidate
        lines.append(line)
    return lines

class Board:
    def __init__(self, key, width, scope, state='SCENARIO-01', scale=1, version='0.1'):
        self.key,self.w,self.scope,self.state,self.scale,self.version=key,width,scope,state,scale,version
        self.p=24 if width<600 else 48 if width<1100 else 72
        self.inner=width-2*self.p
        self.phone=width<600
        self.wide=width>=1100 and scale==1
        self.parts=[]; self.boxes=[]; self.controls=[]; self.count=0; self.y=0
        self.group('composition-'+key)

    def group(self, name, source=''):
        self.parts.append(f'<g id="{escape(name)}" data-source="{escape(source)}">')
    def end(self): self.parts.append('</g>')
    def uid(self):
        self.count+=1; return f'{self.key}-e{self.count}'
    def rect(self,x,y,w,h,fill='paper',radius=0,stroke=None):
        self.parts.append(f'<rect id="{self.uid()}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{C.get(fill,fill)}"'+(f' stroke="{C.get(stroke,stroke)}"' if stroke else '')+'/>')
    def rule(self,y): self.rect(self.p,y,self.inner,1,'line')
    def text(self,s,x,y,width,size=20,style='body',color='ink',source='',leading=1.45):
        s=clean(s); size=round(size*self.scale,2)
        font=ImageFont.truetype(FONTS[style][1],round(size))
        lines=wrap(s,width,font); height=len(lines)*size*leading
        ident=self.uid(); weight='900' if style=='display' else '700' if style=='bold' else '400'
        self.parts.append(f'<text id="{ident}" data-source="{escape(source)}" x="{x}" y="{round(y+size,2)}" font-family="{FONTS[style][0]}" font-size="{size}" font-weight="{weight}" fill="{C[color]}">')
        for i,line in enumerate(lines):
            self.parts.append(f'<tspan x="{x}" y="{round(y+size+i*size*leading,2)}">{escape(line)}</tspan>')
        self.parts.append('</text>')
        self.boxes.append({'id':ident,'text':s,'source':source,'x':x,'y':y,'width':width,'height':round(height,2),'size':size,'color':C[color],
                           'lines':lines,'max_line_width':round(max(font.getlength(l) for l in lines),2)})
        return y+height
    def cp(self,code,x,y,width,**kw):
        return self.text(copy(code,self.phone),x,y,width,source='ORI-COPY-'+code,**kw)
    def button(self,label,x,y,width=None,primary=False,source='',target=''):
        size=18*self.scale
        font=ImageFont.truetype(FONTS['bold'][1],round(size))
        width=width or min(self.inner,max(124,font.getlength(label)+44))
        lines=wrap(label,width-40,font); h=max(48, len(lines)*size*1.4+24)
        self.group(self.uid()+'-action',source)
        self.rect(x,y,width,h,'blue' if primary else 'paper',h/2 if h<80 else 16, None if primary else 'ink')
        self.text(label,x+20,y+10,width-40,18,'bold','white' if primary else 'ink',source,1.4)
        self.end()
        self.controls.append({'label':label,'source':source,'target':target,'x':x,'y':y,'width':round(width,2),'height':round(h,2),'connected':False})
        return y+h
    def link(self,label,x,y,width,source='',target=''):
        start=len(self.boxes)
        end=self.text(label,x,y+10,width,18,'bold',source=source,leading=1.4)
        h=max(48,end-y+8); box=self.boxes[start]
        self.parts.append(f'<path id="{self.uid()}" d="M{x} {round(end+1,2)} H{x+min(width,box["max_line_width"])}" stroke="{C["ink"]}"/>')
        self.controls.append({'label':label,'source':source,'target':target,'x':x,'y':y,'width':width,'height':round(h,2),'connected':False})
        return y+h
    def notice(self,s,y,source,fill='mint'):
        font=ImageFont.truetype(FONTS['body'][1],round(18*self.scale))
        h=len(wrap(s,self.inner-32,font))*18*self.scale*1.45+32
        self.rect(self.p,y,self.inner,h,fill,12)
        self.text(s,self.p+16,y+14,self.inner-32,18,source=source)
        return y+h
    def header(self,nav=True,story=True):
        self.group('H01-recognition','ORI-COPY-H01-01/05/06')
        p=self.p; y=24
        # 200% text is deliberately recomposed, not clipped in a fixed header.
        if self.scale>1:
            y=self.cp('H01-01',p,y,self.inner,size=32,style='display',leading=1.1)+16
            y=self.button(copy('H01-05'),p,y,self.inner,True,'ORI-COPY-H01-05','M01')+18
        else:
            self.cp('H01-01',p,y,self.inner,size=32 if self.phone else 42,style='display',leading=1.1)
            bw=132 if self.phone else 180
            self.button(copy('H01-05'),self.w-p-bw,y,bw,True,'ORI-COPY-H01-05','M01')
            y+=68
        y=self.cp('H01-06',p,y,self.inner,size=16,color='muted')+16
        self.end()
        if nav:y=self.navigation(y,story)
        self.rule(y); return y+40
    def navigation(self,y,story=True):
        self.group('navigation-secondary')
        labels=[('H02-01','H02'),('H03-09','H03'),('H04-01','H04')]
        if not story:labels=[r for r in labels if r[1]!='H03']
        if self.inner>=850 and self.scale==1:
            for code,x in zip(labels,[self.p,self.p+240,self.p+560]):self.link(copy(code[0]),x,y,230 if code[0]!='H03-09' else 300,'ORI-COPY-'+code[0],code[1])
            y+=56
        elif self.scale==1:
            font=ImageFont.truetype(FONTS['bold'][1],18);x=self.p;rowend=y
            for code,target in labels:
                width=min(self.inner,font.getlength(copy(code))+12)
                if x+width>self.w-self.p:y=rowend+8;x=self.p
                rowend=max(rowend,self.link(copy(code),x,y,width,'ORI-COPY-'+code,target));x+=width+24
            y=rowend+8
        else:
            for code,target in labels:y=self.link(copy(code),self.p,y,self.inner,'ORI-COPY-'+code,target)+8
        self.end();return y
    def asset(self,asset,x,y,w,h,caption):
        """Explicit placement/crop study, not delivered illustration or dish imagery."""
        self.group(asset+'-'+self.uid(),'Resource brief '+asset)
        self.rect(x,y,w,h,'pink' if asset=='ORI-ASSET-01' else 'yellow',20)
        # Geometry is solely a scale/crop marker, never a dish or room depiction.
        if asset=='ORI-ASSET-03':
            self.parts.append('<g aria-hidden="true" filter="url(#soft-depth)">')
            self.rect(x+w*.16,y+h*.15,w*.68,h*.43,'coral',18)
            self.rect(x+w*.24,y+h*.19,w*.2,h*.34,'blue',6)
            self.parts.append(f'<circle id="{self.uid()}" cx="{x+w*.62}" cy="{y+h*.37}" r="{min(w,h)*.1}" fill="{C["paper"]}"/>')
            self.parts.append('</g>')
        else:
            cx=x+w*.56; cy=y+h*.40; r=min(w*.34,h*.29)
            self.parts.append(f'<g aria-hidden="true" filter="url(#soft-depth)"><circle id="{self.uid()}" cx="{cx}" cy="{cy}" r="{r}" fill="{C["coral"]}"/><circle id="{self.uid()}" cx="{cx}" cy="{cy}" r="{r*.66}" fill="{C["paper"]}"/></g>')
            self.parts.append(f'<g aria-hidden="true" transform="rotate(-22 {x+w*.2} {y+h*.38})"><ellipse id="{self.uid()}" cx="{x+w*.2}" cy="{y+h*.25}" rx="{w*.055}" ry="{h*.085}" fill="{C["blue"]}"/><rect id="{self.uid()}" x="{x+w*.18}" y="{y+h*.3}" width="{w*.04}" height="{h*.3}" rx="{w*.02}" fill="{C["blue"]}"/></g>')
        self.text(caption,x+20,y+h-100,w-40,16,'body',source=asset)
        self.end(); return y+h
    def dish(self,num,y,variant='V01',status=None,detail=False):
        dish='ORI-DISH-'+num; row=CASE[dish]
        source=dish; name,desc=row[:2]
        if num=='02':
            vr=CASE[dish+'-'+variant]; name=vr[0].split(' / ')[1]; desc=vr[1]
            if variant=='V01': desc=row[1]
            source=dish+'-'+variant
        self.group('offer-'+num+'-'+variant+'-'+self.uid(),source)
        self.rule(y); y+=28
        left=self.p; width=min(self.inner,860) if detail else self.inner
        if self.wide and not detail:
            nw=round(self.inner*.56); ox=left+nw+64; ow=self.inner-nw-64
            titleend=self.text(name,left,y,nw,32,'display',source=source,leading=1.2)
            if status and num=='08':titleend=self.text(copy(status).split(' / ')[0],left,titleend+12,nw,20,'bold',source='ORI-COPY-'+status)+8
            descriptionend=self.text(desc,left,titleend+18,nw,20,source=dish if num!='02' else source)
            oy=y
        else:
            nw=width; ox=left; ow=width
            titleend=self.text(name,left,y,nw,30 if detail else 26,'display',source=source,leading=1.2)
            if status and num=='08':titleend=self.text(copy(status).split(' / ')[0],left,titleend+12,nw,20,'bold',source='ORI-COPY-'+status)+8
            descriptionend=self.text(desc,left,titleend+16,nw,20 if not self.phone else 18,source=dish if num!='02' else source)
            oy=descriptionend+24
        if num=='02':
            oy=self.text(CASE[dish+'-'+variant][0].split(' / ')[0],ox,oy,ow,18,'bold',source=source)+12
        offers=[(k,v) for k,v in CASE.items() if k.startswith('ORI-MENU-P') and v[0].startswith(dish)]
        for key,offer in offers:
            oy=self.text(offer[1]+' · '+offer[2],ox,oy,ow,22,'bold',source=key,leading=1.3)+14
        condition=offers[0][1][3]
        oy=self.text(condition,ox,oy,ow,18,source=offers[0][0])+16
        y=max(oy,descriptionend)+12
        if status and num=='08':
            if status=='S06':
                y=self.text(copy('S07').split(' / ')[0],left,y,width,18,source='ORI-COPY-S07')+8
                y=self.link('Ver postres',left,y,width,'ORI-COPY-S07','M01/C03')+12
        food = 'D01-03' if num=='02' and variant=='V01' else 'D01-04' if num=='02' else 'D01-06' if num=='08' else 'D01-05'
        if food=='D01-03': foodtext=copy(food).replace('D02/V01: ','')
        elif food=='D01-04': foodtext=copy(food).replace('D02/V02: ','')
        else: foodtext=copy(food)
        if num=='10': foodtext='Declarado en el ejemplo: sulfitos. El resto de alérgenos y la elaboración están pendientes.'
        y=self.text(foodtext,left,y,width if not self.wide else min(width,920),18,color='muted',source='ORI-COPY-'+food if num!='10' else 'ORI-FOOD-10')+8
        if detail and num=='02':
            y+=20; y=self.text(copy('M01-05'),left,y,width,18,'bold',source='ORI-COPY-M01-05')+12
            for v in ['V01','V02']:
                label=CASE[dish+'-'+v][0].split(' / ')[0]
                y=self.button(('✓ ' if v==variant else '')+label,left,y,width,False,dish+'-'+v,'D01/'+v)+12
            y+=8; y=self.text(copy('M01-06'),left,y,width,18,'bold',source='ORI-COPY-M01-06')+12
            for key,offer in offers:y=self.button(('✓ ' if key=='ORI-MENU-P02' else '')+offer[1]+' · '+offer[2],left,y,width,False,key,'D01/'+variant+'/'+key)+12
        if not detail:y=self.link('Ver detalle',left,y,min(width,300),'ORI-COPY-H02-07; '+source,'D01/'+source)+16
        self.end(); return y+24
    def story(self,y,asset=True):
        self.group('H03-story','ORI-COPY-H03-01–09')
        y=self.cp('H03-01',self.p,y,self.inner,size=48 if not self.phone else 36,style='display',leading=1.14)+20
        y=self.cp('H03-02',self.p,y,self.inner,size=28,style='bold',leading=1.25)+28
        x=self.p; width=min(self.inner,740)
        if self.wide:
            width=650; x=self.w-self.p-width
            if asset:self.asset('ORI-ASSET-03',self.p,y,440,380,'ORI-ASSET-03\nEscena del lugar pendiente.\nSin fotografía de un local real.')
        # Always the full canonical story, including phone. No fake expansion.
        paragraphs=copy('H03-03').split('Dani reparó',1)
        end=self.text(paragraphs[0].strip(),x,y,width,20 if not self.phone else 18,source='ORI-COPY-H03-03')+20
        end=self.text('Dani reparó'+paragraphs[1],x,end,width,20 if not self.phone else 18,source='ORI-COPY-H03-03')+28
        py=y+410 if self.wide and asset else end
        for code in ['H03-05','H03-06']:
            py=self.cp(code,self.p if self.wide else x,py,440 if self.wide else width,size=18 if self.phone else 20,style='bold')+24
        if not self.wide:end=py
        end=self.cp('H03-07',x,end,width,size=18 if self.phone else 20)+24
        end=self.link(copy('H03-08'),x,end,width,'ORI-COPY-H03-08','H04')+32
        self.end(); return max(end,py)
    def visit(self,y,pending=False,exception=False,origin=False):
        start=y; p=self.p
        # Insert the tinted full block underneath its actual content bounds.
        pos=len(self.parts); self.group('H04-visit','ORI-COPY-H04-01–11; ORI-VISIT-01–03')
        y+=44
        y=self.cp('H04-01',p,y,self.inner,size=48 if not self.phone else 36,style='display',leading=1.15)+20
        y=self.cp('H04-02',p,y,self.inner,size=24,style='bold')+8
        y=self.cp('H04-03',p,y,self.inner,size=18)+28
        if exception: y=self.notice(copy('S10'),y,'ORI-COPY-S10','paper')+24
        if pending:
            for label in ['Horario del local pendiente.','Horario de cocina pendiente.']:y=self.text(label,p,y,self.inner,22,'bold',source='ORI-COPY-S12')+14
        else:
            if self.wide:
                widths=[round(self.inner*.35),round(self.inner*.3),round(self.inner*.35)-32]
                xs=[p,p+widths[0],p+widths[0]+widths[1]+32]
                self.text('Días',xs[0],y,widths[0],18,'bold',source='ORI-VISIT-01')
                self.text('Horario del local',xs[1],y,widths[1],18,'bold',source='ORI-COPY-H04-04')
                self.text('Horario de cocina',xs[2],y,widths[2],18,'bold',source='ORI-COPY-H04-04'); y+=52
            for days,local,kitchen in [('Lunes','Cerrado','Cerrada'),('Martes a jueves y domingo','12:30–17:00','13:00–15:30'),('Viernes y sábado','12:30–17:00 y 19:30–23:00','13:00–15:30 y 20:00–22:00')]:
                self.rule(y); y+=20
                if self.wide:
                    ends=[self.text(t,x,y,w,20,'bold' if i==0 else 'body',source='ORI-VISIT-01') for i,(t,x,w) in enumerate(zip([days,local,kitchen],xs,widths))]
                    y=max(ends)+20
                else:
                    y=self.text(days,p,y,self.inner,22,'bold',source='ORI-VISIT-01')+12
                    for label,value in [('Horario del local',local),('Horario de cocina',kitchen)]:
                        y=self.text(label,p,y,self.inner,16,'bold',source='ORI-COPY-H04-04')+4
                        y=self.text(value,p,y,self.inner,20,source='ORI-VISIT-01')+16
                    y+=8
        y+=20
        y=self.cp('H04-06',p,y,min(self.inner,820),size=18 if self.phone else 20)+32
        def fact(code,x,fy,width):
            value=copy(code,self.phone); first,rest=value.split('. ',1) if '. ' in value else (value,'')
            fy=self.text(first+'.' if rest else first,x,fy,width,18 if self.phone else 20,'bold',source='ORI-COPY-'+code)+8
            if rest:fy=self.text(rest,x,fy,width,18 if self.phone else 20,source='ORI-COPY-'+code)+12
            return fy+16
        if self.wide:
            fw=round((self.inner-72)/2); rx=p+fw+72
            ly=fact('H04-07',p,y,fw); ry=fact('H04-08',rx,y,fw); ry=fact('H04-09',rx,ry,fw)
            for code in ['ORI-VISIT-03C','ORI-VISIT-03E']:ly=self.text(CASE[code][0],p,ly,fw,18,source=code)+16
            y=max(ly,ry)+24
        else:
            for code in ['H04-07','H04-08','H04-09']:y=fact(code,p,y,self.inner)
            for code in ['ORI-VISIT-03C','ORI-VISIT-03E']:y=self.text(CASE[code][0],p,y,self.inner,18,source=code)+16
            y+=16
        y=self.cp('H04-10',p,y,min(self.inner,820),size=18 if self.phone else 20)+20
        y=self.button('Volver a la carta' if origin else 'Ver carta',p,y+12,min(self.inner,(240 if origin else 180)*self.scale),True,'ORI-COPY-H04-11','M01/origin' if origin else 'M01')+44
        self.end(); self.parts.insert(pos,f'<rect id="{self.uid()}" x="0" y="{start}" width="{self.w}" height="{y-start}" fill="{C["yellow"]}"/>')
        return y
    def footer(self,y):
        y+=36; self.rule(y); y+=24
        y=self.text('ORILLA',self.p,y,self.inner,26,'display',source='ORI-COPY-H01-01')+14
        y=self.text('Powered by Valiris Restaurants',self.p,y,self.inner,16,color='muted',source='ADR-0003; attribution only')+36
        return y
    def save(self,y):
        h=int(y+20); self.end()
        defs='<defs><filter id="soft-depth" x="-35%" y="-35%" width="170%" height="190%"><feDropShadow dx="0" dy="10" stdDeviation="10" flood-color="#20251E" flood-opacity="0.12"/></filter></defs>'
        title=f'{self.key} · ORILLA · static editable {self.scope} · v{self.version}'
        svg=f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {h}" width="{self.w}" height="{h}" role="img" aria-labelledby="board-title board-desc">\n<title id="board-title">{escape(title)}</title>\n<desc id="board-desc">Fictional ORILLA demonstration. Static design source; drawn controls are not connected. {escape(self.state)}. Essential content is editable text; resource panels are labelled crop studies.</desc>\n{defs}\n<rect width="{self.w}" height="{h}" fill="{C["paper"]}"/>\n'+ '\n'.join(self.parts)+'\n</svg>\n'
        target=OUT/'sources'/f'{self.key}.svg'; target.parent.mkdir(parents=True,exist_ok=True); target.write_text(svg,encoding='utf-8')
        info={'frame':self.key,'version':self.version,'width':self.w,'height':h,'scope':self.scope,'scenario':self.state,'text_scale':self.scale,'svg':str(target.relative_to(ROOT)).replace('\\','/'),'png':f'research-evidence/g2-07-storefront/exports/{self.key}.png','text':self.boxes,'controls':self.controls}
        return info

def storefront(key,w,scale=1,assets=True,story=True,withdrawn=False,version='0.1'):
    b=Board(key,w,'complete Storefront','SCENARIO-07; flan withdrawn from current preview' if withdrawn else 'SCENARIO-01; scoped unavailable flan, no live clock',scale,version)
    y=b.header(nav=not b.phone,story=story); b.group('H01-presentation','ORI-COPY-H01-02–04')
    width=round(b.inner*.57) if b.wide and assets else min(b.inner,900)
    y=b.cp('H01-02',b.p,y,width,size=20,style='bold')+20
    hero=y
    y=b.cp('H01-03',b.p,y,width,size=80 if b.wide else 58 if not b.phone else 46,style='display',leading=1.10)+24
    y=b.cp('H01-04',b.p,y,width,size=22 if not b.phone else 18)+24
    y=b.button(copy('H01-05'),b.p,y, min(b.inner,180*b.scale),True,'ORI-COPY-H01-05','M01')+32
    if assets:
        if b.wide:
            x=b.p+width+48; ah=max(430,y-hero); b.asset('ORI-ASSET-01',x,hero,b.w-b.p-x,ah,'ORI-ASSET-01\nIlustración de marca pendiente.\nEstudio de espacio y recorte.'); y=max(y,hero+ah)
        else:
            y=b.asset('ORI-ASSET-01',b.p,y,b.inner,290 if b.phone else 350,'ORI-ASSET-01\nIlustración de marca pendiente.\nEstudio de espacio y recorte.')+16
    b.end()
    if b.phone:y=b.navigation(y+8,story)
    y+=64 if not b.phone else 44
    b.group('H02-kitchen','ORI-COPY-H02-01–07; ORI-MENU-H01')
    b.rule(y); y+=36
    y=b.cp('H02-01',b.p,y,b.inner,size=48 if not b.phone else 36,style='display',leading=1.15)+22
    y=b.cp('H02-02',b.p,y,min(b.inner,820),size=30 if not b.phone else 26,style='bold',leading=1.25)+18
    y=b.cp('H02-03',b.p,y,min(b.inner,820),size=20 if not b.phone else 18)+28
    y=b.notice(copy('M01-10'),y,'ORI-COPY-M01-10')+36
    y=b.cp('H02-04',b.p,y,b.inner,size=24,style='bold')+24
    for n in (['02','04'] if withdrawn else ['02','04','08']):y=b.dish(n,y,status='S06' if n=='08' else None)
    y=b.button(copy('H02-06'),b.p,y,min(b.inner,250*b.scale),True,'ORI-COPY-H02-06','M01')+56
    b.end()
    if story:y=b.story(y,assets)+64
    y=b.visit(y)+16
    return b.save(b.footer(y))

def bridge(key,w,kind,variant='V01',origin='direct',state=None,version='0.2'):
    b=Board(key,w,'partial '+kind+' bridge; not complete Digital Menu',state or 'SCENARIO-01',version=version)
    y=b.header(False)
    y=b.cp('H01-02',b.p,y,b.inner,size=18)+20
    if kind=='visit':return b.save(b.footer(b.visit(y,pending=state=='S12',exception=state=='S10',origin=origin=='menu')))
    if kind=='detail':
        label='Volver a La cocina' if origin=='kitchen' else 'Volver a la carta' if origin=='menu' else 'Ver carta'
        y=b.link(label,b.p,y,b.inner,'ORI-COPY-D01-10' if origin=='kitchen' else 'ORI-COPY-D01-09' if origin=='menu' else 'ORI-COPY-E03', 'H02/D02' if origin=='kitchen' else 'M01/C01/D02/'+variant if origin=='menu' else 'M01')+24
        y=b.notice(copy('M01-10'),y,'ORI-COPY-M01-10')+24
        y=b.dish('02',y,variant,detail=True)
        return b.save(b.footer(y))
    y=b.cp('M01-01',b.p,y,b.inner,size=48 if not b.phone else 36,style='display',leading=1.12)+18
    y=b.cp('M01-02',b.p,y,b.inner,size=20,style='bold')
    y+=20; y=b.notice(copy('M01-10'),y,'ORI-COPY-M01-10')+16
    y=b.notice(copy('S05'),y,'ORI-COPY-S05','yellow')+20
    for code in ['M01-09','M01-08']:y=b.link(copy(code),b.p,y,b.inner,'ORI-COPY-'+code,'H01' if code=='M01-09' else 'H04')+8
    y+=20
    # These are four source category labels, not a reconstructed full Menu.
    y=b.text('Para compartir · Platos · Postres · Bebidas',b.p,y,b.inner,18,'bold',source='ORI-MENU-C01–04')+24
    for title,items in [('Para el centro',['02']),('Del horno y la cuchara',['04']),('Un final y sobremesa',['08']),('Para beber',['10'])]:
        y=b.text(title,b.p,y,b.inner,30 if not b.phone else 26,'display',source='ORI-COPY-M01-03',leading=1.2)+18
        for n in items:y=b.dish(n,y,status='S06' if n=='08' else None)
    return b.save(b.footer(y))

def stateboard(key,w,state,version='0.2'):
    scenario={'available':'SCENARIO-00 at 14:00','S06':'SCENARIO-01 at 14:15','S08':'SCENARIO-02 at 14:30; confirmed restoration','S09':'SCENARIO-03; 6 October next service','S17':'SCENARIO-07; confirmed withdrawal','S24':'SCENARIO-08; Spanish source fallback'}.get(state,state)
    b=Board(key,w,'situated state study; entry and recovery',scenario,version=version)
    y=b.header(False); y=b.notice(copy('M01-10'),y,'ORI-COPY-M01-10')+28
    if state in ['S06','S08','S09','available']:
        y=b.dish('08',y,status=state if state!='available' else None,detail=True)
        if state=='available': y=b.text(copy('S01'),b.p,y,b.inner,20,'bold',source='ORI-COPY-S01')+20
        y=b.link('Volver a la carta',b.p,y,b.inner,'ORI-COPY-D01-09','M01/C03/D08')+24
    else:
        heading=CASE['ORI-DISH-02-V02'][0].split(' / ')[1] if state=='S23' else 'Flan de café' if state in ['S17','S18','S16'] else 'Carta de ORILLA'
        hsource='ORI-DISH-02-V02; intended target only' if state=='S23' else 'ORI-DISH-08' if state in ['S17','S18','S16'] else 'ORI-COPY-M01-01'
        y=b.text(heading,b.p,y,b.inner,36 if not b.phone else 28,'display',source=hsource,leading=1.2)+24
        y=b.notice(copy(state).split(' / ')[0],y,'ORI-COPY-'+state,'yellow')+24
        actions={'S17':['Ver carta'],'S18':['Reintentar','Horarios y visita'],'S16':['Volver a la carta'],'S14':['Reintentar','Horarios y visita'],'S24':['Ver carta'],'S25':['Ver carta en español'],'S19':['Ver Postres'],'S23':['Ver opciones'],'S13':[]}
        if state=='S19':
            # Substitute only the actually known current category in the editorial action.
            pass
        for label in actions[state]:y=b.button(label,b.p,y,b.inner if b.phone else 320,False,'ORI-COPY-'+state, 'D01/ORI-DISH-02' if state=='S23' else 'H04' if label=='Horarios y visita' else 'M01/C03' if state=='S19' else 'M01')+14
        if state=='S24':y=b.dish('02',y,'V02',detail=True)
    return b.save(b.footer(y))

def contrast(key,w,fixture):
    """Separate audited journey fixtures. Never ORILLA restaurant content."""
    b=Board(key,w,'separate '+fixture+' content contrast',fixture+' separate reset',version='0.2')
    p=b.p; width=min(b.inner,900); y=28
    src='m1-connected-journey.md#'+fixture.lower()
    y=b.text('Caso ficticio de contraste '+fixture+'. No es contenido de ORILLA.',p,y,width,16,color='muted',source=src)+28
    title={'C1':'Café Linde','C2':'Mesa del Patio','C3':'Casa del Mediodía'}[fixture]
    y=b.text(title,p,y,width,38 if b.phone else 52,'display',source=src,leading=1.12)+24
    y=b.notice('Ingredientes y alérgenos de ejemplo. Los datos declarados no confirman la ausencia de otros alérgenos.',y,src)+28
    if fixture=='C1':
        y=b.text('Carta · consulta sin fotografías ni relato',p,y,width,24,'bold',source=src)+20
        y=b.text('Local: lunes a sábado, 08:00–17:00. Desayunos: 08:00–12:00. Caso fijado: 1 de octubre de 2026, 10:00.',p,y,width,18,source=src)+20
        for heading,items in [('Cafés',[('Espresso','1,60 €'),('Café con leche','1,90 €'),('Café con hielo','1,80 €')]),('Desayunos',[('Tostada de tomate','2,80 €'),('Tostada de mantequilla','2,60 €'),('Croissant','2,20 €')]),('Bebidas',[('Zumo de naranja','3,00 €'),('Té','1,80 €'),('Agua','1,50 €'),('Chocolate caliente','2,80 €')])]:
            y=b.text(heading,p,y,width,28,'display',source=src)+16
            for name,amount in items:
                b.rule(y);y=b.text(name+' · '+amount,p,y+16,width,22,'bold',source=src)+12
                positive='leche' if name in ['Café con leche','Chocolate caliente'] else 'trigo (gluten) y leche' if name=='Tostada de mantequilla' else 'trigo (gluten)' if name=='Tostada de tomate' else None
                y=b.text('Declarado en el ejemplo: '+positive+'. Resto de información pendiente.' if positive else 'Información alimentaria pendiente.',p,y,width,18,source=src)+24
    elif fixture=='C2':
        terrace=b.phone
        y=b.text('Carta de terraza' if terrace else 'Carta general',p,y,width,24,'bold',source=src)+12
        y=b.button('Cambiar carta',p,y,min(width,250),False,src,'C2/context-chooser')+28
        rows=[('Tabla de quesos artesanos de leche cruda, membrillo y pan de masa madre',
               'Media tabla · '+('26,00 €' if terrace else '24,00 €')+'\nTabla completa · '+('36,00 €' if terrace else '34,00 €'),
               'Pan adicional · +'+('2,20 €' if terrace else '2,00 €')+'. Declarado en el ejemplo: leche y trigo (gluten). Resto de información pendiente.'),
              ('Arroz de verduras',('19,50 €' if terrace else '18,00 €')+' / persona','Mínimo 2 personas. Información alimentaria pendiente.'),
              ('Pescado del mercado',('7,00 €' if terrace else '6,50 €')+' / 100 g','Peso y total por confirmar con el personal. Declarado en el ejemplo: pescado. Resto de información pendiente.'),
              ('Vino de la casa','Copa · '+('3,80 €' if terrace else '3,50 €')+'\nBotella · '+('21,00 €' if terrace else '19,00 €'),'Declarado en el ejemplo: sulfitos. Resto de información pendiente.')]
        for name,amount,condition in rows:
            b.rule(y);y=b.text(name,p,y+22,width,26,'display',source=src,leading=1.2)+16
            y=b.text(amount,p,y,width,22,'bold',source=src)+16
            y=b.text(condition,p,y,width,18,source=src)+30
    else:
        y=b.text('Menú del día · 1 de octubre de 2026 · comidas',p,y,width,26,'display',source=src,leading=1.2)+18
        y=b.text('16,50 € / persona',p,y,width,24,'bold',source=src)+14
        y=b.text('Un primero, un segundo y un postre. Pan y agua incluidos. Café +1,50 €.',p,y,width,18,source=src)+22
        y=b.text('Horario del local · 12:30–17:00\nHorario de cocina · 13:00–15:30',p,y,width,20,source=src)+20
        y=b.notice('Este contenido se muestra en español mientras revisamos la traducción.',y,src+' / L10c fallback')+24
        for heading,items in [('Primeros',['Crema de calabaza con yogur','Ensalada']),('Segundos',['Pollo al horno','Arroz de verduras']),('Postres',['Flan','Fruta'])]:
            y=b.text(heading,p,y,width,28,'display',source=src)+16
            for name in items:
                y=b.text(name,p,y,width,22,'bold',source=src)+8
                msg='Contiene leche declarada. Traducción afectada pendiente; resto de información alimentaria pendiente.' if name=='Crema de calabaza con yogur' else 'Declarado en el ejemplo: leche y huevo. Resto de información pendiente.' if name=='Flan' else 'Información alimentaria pendiente.'
                y=b.text(msg,p,y,width,18,source=src+' / L10c')+24
        y=b.text('Referencia L10c · fuente publicada del 1 de octubre.',p,y,width,16,color='muted',source=src+' / L10c')+24
    return b.save(y+30)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--phase',choices=['pc','pc-stress','all'],default='pc'); args=ap.parse_args()
    frames=[storefront('UI-P01',1440,version='0.1' if args.phase=='pc' else '0.2')]
    if args.phase=='all':
        frames += [storefront('UI-T01',390,version='0.2')]
        for w in [360,430,768,1024,1280]:frames.append(storefront('UI-W'+str(w),w,version='0.2'))
        frames.append(storefront('UI-L844',844,version='0.2'))
        frames.append(storefront('UI-Z390',390,scale=2,assets=False,version='0.2'))
    if args.phase in ['all','pc-stress']:
        for w,tag in ([(1440,'P'),(390,'T')] if args.phase=='all' else [(1440,'P')]):
            frames.append(storefront('UI-'+tag+'-NOART',w,assets=False,version='0.2'))
            frames.append(storefront('UI-'+tag+'-NOSTORY',w,assets=False,story=False,version='0.2'))
            frames.append(storefront('UI-'+tag+'-WITHDRAWN',w,withdrawn=True,version='0.2'))
            frames.append(bridge('UI-'+tag+'-MENU',w,'menu'))
            frames.append(bridge('UI-'+tag+'-V01-H02',w,'detail',origin='kitchen'))
            frames.append(bridge('UI-'+tag+'-V02-DIRECT',w,'detail',variant='V02'))
            frames.append(bridge('UI-'+tag+'-V02-MENU',w,'detail',variant='V02',origin='menu'))
            frames.append(bridge('UI-'+tag+'-VISIT-DIRECT',w,'visit'))
            frames.append(bridge('UI-'+tag+'-VISIT-MENU',w,'visit',origin='menu',state='S10'))
            frames.append(bridge('UI-'+tag+'-VISIT-PENDING',w,'visit',state='S12'))
            for state in ['available','S06','S08','S09','S17','S18','S16','S14','S24','S25','S19','S23','S13']:
                frames.append(stateboard('UI-'+tag+'-'+state,w,state))
    if args.phase=='all':
        for fixture in ['C1','C2','C3']:
            for w,tag in [(1440,'P'),(390,'T')]:frames.append(contrast('UI-'+tag+'-'+fixture,w,fixture))
    OUT.mkdir(parents=True,exist_ok=True)
    manifest={'baseline':BASE,'case_copy_sha':COPY_SHA,'ia_sha':IA_SHA,'seo_sha':SEO_SHA,
              'sources':{k:{'path':v,'sha256':hashlib.sha256((ROOT/v).read_bytes()).hexdigest()} for k,v in FILES.items()},
              'static':True,'fonts':'Arial Black + Segoe UI; local exploratory substitutes; no font binaries', 'frames':frames}
    (OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'phase':args.phase,'frames':len(frames),'dimensions':[(f['frame'],f['width'],f['height']) for f in frames]},ensure_ascii=False))

if __name__=='__main__':main()
