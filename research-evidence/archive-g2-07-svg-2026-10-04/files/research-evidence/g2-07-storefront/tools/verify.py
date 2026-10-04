"""Evidence checks for static design sources and content invariants, not UI tests."""
from pathlib import Path
from collections import Counter
import hashlib,json,re,sys,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research-evidence/g2-07-storefront'
manifest=json.loads((OUT/'manifest.json').read_text(encoding='utf-8'))
exports=json.loads((OUT/'checks/exports.json').read_text(encoding='utf-8'))
exportmap={r['frame']:r for r in exports['results']}
errors=[];reports=[]
def check(value,message):
    if not value:errors.append(message)
def normalized(s):return ' '.join(s.replace('\u00a0',' ').split())
for source in manifest['sources'].values():
    check(hashlib.sha256((ROOT/source['path']).read_bytes()).hexdigest()==source['sha256'],'Source hash changed: '+source['path'])
for frame in manifest['frames']:
    path=ROOT/frame['svg'];raw=path.read_bytes();s=raw.decode('utf-8',errors='strict');root=ET.fromstring(s)
    ids=[n.attrib['id'] for n in root.iter() if 'id' in n.attrib];duplicates=[k for k,n in Counter(ids).items() if n>1]
    refs=re.findall(r'url\(#([^\)]+)\)',s)+re.findall(r'href="#([^"]+)"',s)
    broken=[r for r in refs if r not in ids]
    check(not duplicates,frame['frame']+': duplicate IDs')
    check(not broken,frame['frame']+': broken references')
    check(s.startswith('<?xml version="1.0" encoding="UTF-8"?>'),frame['frame']+': missing UTF-8 declaration')
    check(root.attrib.get('viewBox')==f"0 0 {frame['width']} {frame['height']}",frame['frame']+': viewBox mismatch')
    forbidden=[n.tag for n in root.iter() if n.tag.split('}')[-1] in ['script','foreignObject','image','animate','animateTransform']]
    check(not forbidden,frame['frame']+': unexpected runtime/media')
    check(not re.search(r'd="\s*"|TODO|sodipodi:|inkscape:',s),frame['frame']+': SVG skill hygiene')
    textnodes=[n for n in root.iter() if n.tag.endswith('}text')]
    check(len(textnodes)==len(frame['text']),frame['frame']+': text inventory mismatch')
    overflow=[t['id'] for t in frame['text'] if t['max_line_width']>t['width']+1 or t['x']+t['max_line_width']>frame['width']+1 or t['y']+t['height']>frame['height']+1]
    check(not overflow,frame['frame']+': text overflow '+','.join(overflow))
    small=[a['label'] for a in frame['controls'] if a['width']<44 or a['height']<44]
    check(not small,frame['frame']+': drawn target smaller than proposed 44x44 '+','.join(small))
    check(all(not a['connected'] for a in frame['controls']),frame['frame']+': false interaction claim')
    er=exportmap[frame['frame']]
    check((er['width'],er['height'])==(frame['width'],frame['height']),frame['frame']+': PNG dimensions')
    check(hashlib.sha256(raw).hexdigest()==er['svg_sha256'],frame['frame']+': stale SVG export evidence')
    check(hashlib.sha256((ROOT/frame['png']).read_bytes()).hexdigest()==er['png_sha256'],frame['frame']+': stale PNG export')
    flat=normalized(' '.join(t['text'] for t in frame['text']))
    if 'C1' not in frame['frame'] and 'C2' not in frame['frame'] and 'C3' not in frame['frame']:
        check('ORILLA es un restaurante ficticio creado para esta demostración.' in flat,frame['frame']+': fiction missing')
    if frame['scope']=='complete Storefront':
        for required in ['Ver carta','Mínimo 2 personas.','16,00 € / persona','Media ración · 9,50 €','Ración · 15,00 €','Horario del local','Horario de cocina']:
            check(required in flat,frame['frame']+': missing '+required)
        if '-NOSTORY' in frame['frame']:check('La historia de ORILLA' not in flat and 'Inés Vidal' not in flat,frame['frame']+': missing-story link/person retained')
        if '-WITHDRAWN' in frame['frame']:check('Flan de café' not in flat and not re.search(r'(?<!\d)6,00 €',flat),frame['frame']+': withdrawn preview retained')
    if '-S17' in frame['frame'] or '-S18' in frame['frame'] or '-S16' in frame['frame']:
        check('6,00 €' not in flat,frame['frame']+': unconfirmed/withdrawn price exposed')
    if '-V02' in frame['frame']:
        for required in ['Berenjena asada con aceite de limón, miel y avellanas tostadas','no se ha confirmado la ausencia de leche','9,50 €','15,00 €']:
            check(required in flat,frame['frame']+': variant mismatch '+required)
        check('Berenjena asada con yogur' not in flat,frame['frame']+': stale variant name')
    if '-VISIT-MENU' in frame['frame']:
        check('domingo 4 de octubre de 2026, 13:30–15:30.' in flat,frame['frame']+': incomplete dated exception')
        check('Volver a la carta' in flat,frame['frame']+': lost menu return')
    reports.append({'frame':frame['frame'],'text_blocks':len(textnodes),'unique_ids':len(ids),'local_references':len(refs),'overflow':overflow,'small_drawn_targets':small,'png_dimensions':[er['width'],er['height']]})
def luminance(h):
    a=[int(h[i:i+2],16)/255 for i in [1,3,5]]
    a=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in a]
    return sum(x*y for x,y in zip(a,[.2126,.7152,.0722]))
palette={'paper':'#FFF8EC','ink':'#20251E','muted':'#53594C','blue':'#243EB8','mint':'#DDEBBE','yellow':'#F3DE8A','pink':'#F7CADD','white':'#FFFFFF'}
pairs=[('ink',b) for b in ['paper','mint','yellow','pink']]+[('muted','paper'),('white','blue')]
contrast=[]
for fg,bg in pairs:
    a,b=sorted([luminance(palette[fg]),luminance(palette[bg])]);ratio=(b+.05)/(a+.05)
    check(ratio>=4.5,fg+'/'+bg+': contrast below 4.5')
    contrast.append({'foreground':fg,'background':bg,'ratio':round(ratio,2),'normal_text_threshold':4.5})
result={'method':'Windows Python UTF-8/XML, static measured text/target bounds, source and export hashes, critical content invariants; not browser reflow/keyboard/AT tests',
        'frames':len(reports),'errors':errors,'results':reports,'contrast':contrast}
(OUT/'checks/static-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'frames':len(reports),'errors':errors,'contrast':contrast},ensure_ascii=False))
sys.exit(bool(errors))
