from pathlib import Path
import re,subprocess

root=Path(r'D:\the next level\valiris-restaurants')
baseline='120903f'
new='docs/design/m1-food-register-and-outputs.md'
paths=[new,'docs/design/m1-scheduling-and-service-continuity.md',
 'docs/design/m1-public-presence-and-discovery.md','docs/design/m1-service-and-maintenance.md',
 'docs/design/m1-connected-journey.md','docs/design/m1-content-preparation.md',
 'docs/design/m1-extended-journeys.md','docs/adr/0012-confirm-delegated-updates-per-assignment.md',
 'docs/adr/0011-shared-menu-content-and-contextual-maintenance.md','docs/adr/0010-diner-account-and-display-recovery.md',
 'docs/adr/README.md','docs/README.md','CHANGELOG.md','docs/product/m1-design-briefs.md',
 'docs/product/m0-journeys-and-criteria.md','docs/project/roadmap.md','docs/project/m0-closeout.md']
def doc(name):return (root/name).read_text(encoding='utf-8')
def original(name):return subprocess.check_output(['git','show',f'{baseline}:{name}'],cwd=root).decode('utf-8')
def anchors(s):return [re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in re.findall(r'^#{1,6} (.+)$',s,re.M)]
links=0;errors=[]
for name in paths:
 s=doc(name);p=root/name;a=anchors(s)
 assert s.count('```')%2==0,('fences',name)
 assert len(a)==len(set(a)),('headings',name)
 assert not re.search(r'^(<<<<<<<|=======|>>>>>>>)',s,re.M),name
 width=None
 for line in s.splitlines():
  if line.startswith('|'):
   current=len(line.split('|'))
   if width is None:width=current
   assert current==width,('table',name,line)
  else:width=None
 for link in re.findall(r'\]\(([^)]+)\)',s):
  if link.startswith(('https://','http://','mailto:')):continue
  dest,_,frag=link.partition('#');target=p.parent/dest if dest else p
  if not target.exists() or (frag and frag not in anchors(target.read_text(encoding='utf-8'))):errors.append((name,link))
  links+=1
assert not errors,errors
s=doc(new)
pat=r'^### (FO-[FOQX]\d{2}):[^\n]*\n(.*?)(?=^### |^## |\Z)'
cards=dict(re.findall(pat,s,re.M|re.S))
expected=[f'FO-{prefix}{i:02}' for prefix,count in [('F',6),('O',6),('Q',3),('X',3)] for i in range(1,count+1)]
assert list(cards)==expected and len(cards)==18,list(cards)
assert set(re.findall(r'FO-[FOQX]\d{2}',s))<=set(cards)
for key,body in cards.items():
 for field in ['**Actor / objective / entry / version:','**Composition / copy:','**Actions / effect:','**Errors / recovery / check:']:assert field in body,(key,field)
 assert '→' in body,('destination',key)
criteria=re.findall(r'^\| (J[67]\.\d) \|',s,re.M)
assert criteria==[f'J6.{i}' for i in range(1,4)]+[f'J7.{i}' for i in range(1,5)],criteria
source=doc('docs/product/m0-journeys-and-criteria.md')
assert set(criteria)<=set(re.findall(r'^- \*\*(J\d+\.\d):',source,re.M))
caps=re.findall(r'^\| (B\d\.\d{2}) \|',s,re.M)
assert caps==['B4.05','B4.06','B4.08','B4.09','B4.11']+[f'B5.{i:02}' for i in range(1,10)]+[f'B6.{i:02}' for i in range(1,7)]+['B6.10','B7.07'],caps
for tag,count in [('FC',24),('FW',5)]:
 found=re.findall(r'^\| ('+tag+r'\d{2}) ',s,re.M)
 assert found==[f'{tag}{i:02}' for i in range(1,count+1)],found
prior=0
for filename,tag,count in [('docs/design/m1-connected-journey.md','V',16),('docs/design/m1-extended-journeys.md','Q',20),('docs/design/m1-content-preparation.md','PC',24),('docs/design/m1-content-preparation.md','DS',4),('docs/design/m1-service-and-maintenance.md','SC',26),('docs/design/m1-extended-journeys.md','LC',6),('docs/design/m1-public-presence-and-discovery.md','VC',26),('docs/design/m1-scheduling-and-service-continuity.md','TC',30)]:
 pattern=r'^\| '+tag+r'\d{2} .*$';old,current=re.findall(pattern,original(filename),re.M),re.findall(pattern,doc(filename),re.M)
 assert old==current and len(current)==count,(filename,tag);prior+=count
assert prior==152
defined=set(cards)
defined.update(re.findall(r'^\| ([OPX]\d{2}) \|',doc('docs/design/m1-connected-journey.md'),re.M))
for filename,pattern in [('docs/design/m1-connected-journey.md',r'^### ([OPX]\d{2}):'),('docs/design/m1-extended-journeys.md',r'^### (J\d{2}-[POAC]\d{2}):'),('docs/design/m1-content-preparation.md',r'^### (CP-[A-Z]\d{2}):'),('docs/design/m1-service-and-maintenance.md',r'^### (J[89]-[A-Z]\d{2}):'),('docs/design/m1-public-presence-and-discovery.md',r'^### (PV-[POX]\d{2}):'),('docs/design/m1-scheduling-and-service-continuity.md',r'^### (JT-[POX]\d{2}):')]:
 def states(d):return dict(re.findall(pattern+r'[^\n]*\n(.*?)(?=^### |^## |\Z)',d,re.M|re.S))
 assert states(doc(filename))==states(original(filename)),('old card changed',filename)
 defined.update(states(doc(filename)))
refs=set(re.findall(r'(?<![\w-])(?:FO-[FOQX]\d{2}|J\d{1,2}-[A-Z]\d{2}|CP-[A-Z]\d{2}|PV-[POX]\d{2}|JT-[POX]\d{2}|[OPX]\d{2})(?![\w-])',s))
assert refs<=defined,('undefined destination',refs-defined)
rows=lambda d:re.findall(r'^- \*\*J\d+\.\d:.*$',d,re.M)
assert rows(source)==rows(original('docs/product/m0-journeys-and-criteria.md'))
for filename in ['docs/product/m0-capability-matrix.md','docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md']+[p.relative_to(root).as_posix() for p in (root/'docs/adr').glob('*.md')]:assert doc(filename)==original(filename),filename
coverage=doc('docs/design/m1-connected-journey.md').split('## 7.',1)[1].split('## 8.',1)[0]
expanded=[]
for line in coverage.splitlines():
 if not line.startswith('| B'):continue
 field=line.split('|')[1]
 def expand(m):
  a,b,c,d=m.groups();assert a==c;expanded.extend(f'{a}.{i:02}' for i in range(int(b),int(d)+1));return ''
 remaining=re.sub(r'(B\d)\.(\d{2})–(B\d)\.(\d{2})',expand,field);expanded.extend(re.findall(r'B\d\.\d{2}',remaining))
assert len(expanded)==len(set(expanded))==72
assert set(expanded)==set(re.findall(r'B\d\.\d{2}',doc('docs/product/m0-capability-matrix.md')))
assert 'Separate S1:' in coverage and 'Separate S2:' in coverage
print(f'PASS: {links} local/internal links across {len(paths)} docs; fragments/headings/fences/tables; 18 FO required-field cards/defined destinations; seven exact criteria,22 capability rows,five FW/24 FC.')
print('PASS: all152 previous contrasts and all earlier card bodies preserved at120903f; original criteria/matrix/definition/all ADRs unchanged;72 parents once,S1/S2 separate. Documentary integrity only.')
