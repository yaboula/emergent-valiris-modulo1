from pathlib import Path
import re,subprocess,json,collections

r=Path(r'D:\the next level\valiris-restaurants')
baseline='a0583e0'
def text(p):return (r/p).read_text(encoding='utf-8')
def old(p):return subprocess.check_output(['git','show',baseline+':'+p],cwd=r).decode('utf-8')
def anchors(s):return [re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in re.findall(r'^#{1,6} (.+)$',s,re.M)]
paths=[p.relative_to(r).as_posix() for p in (r/'docs/design').glob('*.md')]+[
 'docs/README.md','CHANGELOG.md','docs/product/m1-design-briefs.md',
 'docs/product/m0-journeys-and-criteria.md','docs/project/roadmap.md',
 'docs/project/m0-closeout.md','docs/adr/README.md',
 'docs/adr/0010-diner-account-and-display-recovery.md',
 'docs/adr/0011-shared-menu-content-and-contextual-maintenance.md',
 'docs/adr/0012-confirm-delegated-updates-per-assignment.md']
count=0;errors=[]
for name in paths:
 s=text(name);a=anchors(s);assert len(a)==len(set(a)),('headings',name)
 assert s.count('```')%2==0,('fences',name)
 assert not re.search(r'^(<<<<<<<|=======|>>>>>>>)',s,re.M)
 width=None
 for line in s.splitlines():
  if line.startswith('|') and line.endswith('|'):
   w=len(re.split(r'(?<!\\)\|',line))
   if width is None:width=w
   assert width==w,('table',name,line)
  else:width=None
 for ref in re.findall(r'\]\(([^)]+)\)',s):
  if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',ref):continue
  ref=ref.strip('<>');filename,_,frag=ref.partition('#')
  target=(r/name).parent/filename if filename else r/name
  if not target.exists():errors.append((name,ref,'missing file'));continue
  if frag and frag not in anchors(target.read_text(encoding='utf-8')):errors.append((name,ref,'fragment'))
  count+=1
assert not errors,errors
connected=text('docs/design/m1-connected-journey.md')
maptext=connected.split('## 7.',1)[1].split('## 8.',1)[0]
rows=[line.split('|')[1:-1] for line in maptext.splitlines() if re.match(r'^\| B\d\.\d{2} ',line)]
matrix={}
for line in text('docs/product/m0-capability-matrix.md').splitlines():
 if re.match(r'^\| B\d\.\d{2} /',line):
  cols=[x.strip() for x in line.split('|')[1:-1]];matrix[cols[0].split(' /')[0]]=(cols[1],cols[3])
assert len(rows)==len(matrix)==72
assert [row[0].strip().split(' ')[0] for row in rows]==list(matrix)
for row in rows:
 key=row[0].strip().split(' ')[0]
 assert row[0].strip()==key+' · '+matrix[key][0]+' / '+matrix[key][1],key
 assert all(cell.strip() for cell in row),key
 assert re.search(r'\[(?:FO|PV|CP|JT|J\d+|[OPX])',row[2]),key
 assert re.search(r'J\d+\.\d',row[3]) and re.search(r'\[(?:V|Q|PC|DS|SC|LC|VC|TC|FC)\d{2}\]',row[3]),key
 assert re.search(r'\[RV0[1-7]\]',row[4]) and '[CG' in row[5],key
assert collections.Counter(t for n,t in matrix.values())=={'Included':36,'Configurable':30,'Connection-dependent':6}
assert sum('Sufficient written path' in row[1] for row in rows)==69
assert [row[0].strip().split(' ')[0] for row in rows if 'Partial:' in row[1]]==['B1.05','B1.06','B1.07']
assert 'Separate S1:' in maptext and 'Separate S2:' in maptext
report=text('docs/design/m1-coverage-and-evidence.md')
source=text('docs/product/m0-journeys-and-criteria.md')
criteria=re.findall(r'^- \*\*(J\d+\.\d):',source,re.M)
found=re.findall(r'^\| (J\d+\.\d) \|',report,re.M)
assert found==criteria and len(found)==59,(found,criteria)
state_ids=set()
for p in (r/'docs/design').glob('*.md'):
 state_ids.update(re.findall(r'^### ((?:FO|PV|CP|JT|J\d+)-[A-Z]\d{2}|[OPX]\d{2}):',p.read_text(encoding='utf-8'),re.M))
for doc in [report,maptext]:
 refs=set(re.findall(r'(?<![\w-])((?:FO|PV|CP|JT|J\d+)-[A-Z]\d{2})(?![\w-])',doc))
 assert refs<=state_ids,('state',refs-state_ids)
 reviews=set(re.findall(r'(?<!\w)RV\d{2}(?!\w)',doc));assert reviews<=set(f'RV{i:02}' for i in range(1,8))
 gaps=set(re.findall(r'(?<!\w)CG\d{2}(?:\.\d)?(?!\w)',doc))
 defined=set(re.findall(r'^### (CG\d{2}(?:\.\d)?)$',report,re.M));assert gaps<=defined,('gap',gaps-defined)
 assert set(re.findall(r'(?<!\w)J\d+\.\d(?!\w)',doc))<=set(criteria)
prior=0
for filename,tags in [('m1-connected-journey.md',[('V',16)]),('m1-extended-journeys.md',[('Q',20),('LC',6)]),('m1-content-preparation.md',[('PC',24),('DS',4)]),('m1-service-and-maintenance.md',[('SC',26)]),('m1-public-presence-and-discovery.md',[('VC',26)]),('m1-scheduling-and-service-continuity.md',[('TC',30)]),('m1-food-register-and-outputs.md',[('FC',24)])]:
 name='docs/design/'+filename
 def bodies(s):return dict(re.findall(r'^### ((?:FO|PV|CP|JT|J\d+)-[A-Z]\d{2}|[OPX]\d{2}):[^\n]*\n(.*?)(?=^### |^## |\Z)',s,re.M|re.S))
 assert bodies(text(name))==bodies(old(name)),('old card body',name)
 for tag,n in tags:
  regex=r'^\| '+tag+r'\d{2}(?:\s|\|).*$'
  now,before=re.findall(regex,text(name),re.M),re.findall(regex,old(name),re.M)
  assert now==before and len(now)==n,(filename,tag);prior+=n
assert prior==176
original_lines=lambda s:re.findall(r'^- \*\*J\d+\.\d:.*$',s,re.M)
assert original_lines(source)==original_lines(old('docs/product/m0-journeys-and-criteria.md'))
for p in ['docs/product/m0-capability-matrix.md','docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md']+[p.relative_to(r).as_posix() for p in (r/'docs/adr').glob('*.md')]:assert text(p)==old(p),p
print(f'PASS: {count} local/internal links across{len(paths)}docs; fragments/headings/fences/tables;72 individual rows faithful to36/30/6 treatments,69 written/3 partial;59 exact source criteria with paths/contrasts; RV/CG/state references valid.')
print('PASS: all176 previous contrasts and existing state bodies preserved ata0583e0; original59 criteria/matrix/definition/all ADRs unchanged;S1/S2 separate. Author documentary integrity; no independent/runtime/M1 closure claim.')
