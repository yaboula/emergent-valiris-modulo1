from pathlib import Path
import re, subprocess

root = Path(r'D:\the next level\valiris-restaurants')
baseline = '9cfe77b'
new = 'docs/design/m1-scheduling-and-service-continuity.md'
paths = [new, 'docs/design/m1-public-presence-and-discovery.md',
 'docs/design/m1-service-and-maintenance.md', 'docs/design/m1-connected-journey.md',
 'docs/design/m1-content-preparation.md', 'docs/design/m1-extended-journeys.md',
 'docs/adr/0012-confirm-delegated-updates-per-assignment.md',
 'docs/adr/0011-shared-menu-content-and-contextual-maintenance.md',
 'docs/adr/0010-diner-account-and-display-recovery.md', 'docs/adr/README.md',
 'docs/README.md', 'CHANGELOG.md', 'docs/product/m1-design-briefs.md',
 'docs/product/m0-journeys-and-criteria.md', 'docs/project/roadmap.md',
 'docs/project/m0-closeout.md']
def doc(name): return (root/name).read_text(encoding='utf-8')
def original(name): return subprocess.check_output(['git','show',f'{baseline}:{name}'],cwd=root).decode('utf-8')
def anchors(s): return [re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in re.findall(r'^#{1,6} (.+)$',s,re.M)]
links=0
errors=[]
for name in paths:
 s=doc(name); p=root/name
 assert s.count('```')%2==0, ('fences',name)
 a=anchors(s); assert len(a)==len(set(a)), ('headings',name)
 assert not re.search(r'^(<<<<<<<|=======|>>>>>>>)',s,re.M),name
 width=None
 for line in s.splitlines():
  if line.startswith('|'):
   current=len(line.split('|'))
   if width is None: width=current
   assert current==width,('table',name,line)
  else: width=None
 for link in re.findall(r'\]\(([^)]+)\)',s):
  if link.startswith(('https://','http://','mailto:')):continue
  dest,_,frag=link.partition('#');target=p.parent/dest if dest else p
  if not target.exists() or (frag and frag not in anchors(target.read_text(encoding='utf-8'))):errors.append((name,link))
  links+=1
assert not errors,errors
s=doc(new)
pattern=r'^### (JT-[OPX]\d{2}):[^\n]*\n(.*?)(?=^### |^## |\Z)'
cards=dict(re.findall(pattern,s,re.M|re.S))
expected=[f'JT-O{i:02}' for i in range(1,16)]+['JT-P01','JT-P02']+[f'JT-X{i:02}' for i in range(1,5)]
assert list(cards)==expected and len(cards)==21,list(cards)
assert set(re.findall(r'JT-[OPX]\d{2}',s))<=set(cards)
for key,body in cards.items():
 for field in ['**Actor / objective / entry / version:', '**Composition / copy:', '**Actions / effect:', '**Errors / recovery / check:']: assert field in body,(key,field)
 assert '→' in body,('destination',key)
criteria=re.findall(r'^\| (J[45]\.\d) \|',s,re.M)
assert criteria==[f'J{j}.{i}' for j in [4,5] for i in range(1,5)],criteria
source=doc('docs/product/m0-journeys-and-criteria.md')
assert set(criteria)<=set(re.findall(r'^- \*\*(J\d+\.\d):',source,re.M))
caps=re.findall(r'^\| (B\d\.\d{2}) \|',s,re.M)
assert caps==['B1.02']+[f'B2.{i:02}' for i in range(1,10)]+[f'B4.{i:02}' for i in range(3,10)]+['B4.11','B5.04','B7.07'],caps
for tag,count in [('TC',30),('TW',6)]:
 found=re.findall(r'^\| ('+tag+r'\d{2}) ',s,re.M)
 assert found==[f'{tag}{i:02}' for i in range(1,count+1)],found
prior=0
for filename,tag,count in [('docs/design/m1-connected-journey.md','V',16),('docs/design/m1-extended-journeys.md','Q',20),('docs/design/m1-content-preparation.md','PC',24),('docs/design/m1-content-preparation.md','DS',4),('docs/design/m1-service-and-maintenance.md','SC',26),('docs/design/m1-extended-journeys.md','LC',6),('docs/design/m1-public-presence-and-discovery.md','VC',26)]:
 pat=r'^\| '+tag+r'\d{2} .*$';old,current=re.findall(pat,original(filename),re.M),re.findall(pat,doc(filename),re.M)
 assert old==current and len(current)==count,(filename,tag);prior+=count
assert prior==122
defined=set(cards)
defined.update(re.findall(r'^\| ([OPX]\d{2}) \|',doc('docs/design/m1-connected-journey.md'),re.M))
for filename,pat in [('docs/design/m1-connected-journey.md',r'^### ([OPX]\d{2}):'),('docs/design/m1-extended-journeys.md',r'^### (J\d{2}-[POAC]\d{2}):'),('docs/design/m1-content-preparation.md',r'^### (CP-[A-Z]\d{2}):'),('docs/design/m1-service-and-maintenance.md',r'^### (J[89]-[A-Z]\d{2}):'),('docs/design/m1-public-presence-and-discovery.md',r'^### (PV-[POX]\d{2}):')]:
 def states(d):return dict(re.findall(pat+r'[^\n]*\n(.*?)(?=^### |^## |\Z)',d,re.M|re.S))
 assert states(doc(filename))==states(original(filename)),('old state changed',filename)
 defined.update(states(doc(filename)))
references=set(re.findall(r'(?<![\w-])(?:J\d{1,2}-[A-Z]\d{2}|CP-[A-Z]\d{2}|PV-[POX]\d{2}|JT-[POX]\d{2}|[OPX]\d{2})(?![\w-])',s))
assert references<=defined,('undefined destination',references-defined)
rows=lambda d:re.findall(r'^- \*\*J\d+\.\d:.*$',d,re.M)
assert rows(source)==rows(original('docs/product/m0-journeys-and-criteria.md'))
for filename in ['docs/product/m0-capability-matrix.md','docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md']+[f'docs/adr/{n}' for n in ['0005-repository-and-product-language.md','0008-first-launch-capability-commitment.md','0009-studio-design-and-registered-diner-personalisation.md','0010-diner-account-and-display-recovery.md','0011-shared-menu-content-and-contextual-maintenance.md','0012-confirm-delegated-updates-per-assignment.md']]:assert doc(filename)==original(filename),filename
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
print(f'PASS: {links} local/internal links across {len(paths)} docs; headings/fragments/fences/tables; 21 JT cards/all fields/destinations; eight exact criteria, 20 capabilities, six TW/30 TC.')
print('PASS: 122 prior contrast rows and all earlier state cards preserved at 9cfe77b; original criteria/definition/matrix/ADR-0005,0008–0012 unchanged; 72 parents exactly once/S1,S2 separate. Author documentary integrity only.')
