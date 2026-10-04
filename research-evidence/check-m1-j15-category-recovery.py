from pathlib import Path
from collections import Counter
import re, subprocess

root = Path(r'D:\the next level\valiris-restaurants')
paths = [
 'docs/design/m1-service-and-maintenance.md',
 'docs/design/m1-connected-journey.md', 'docs/design/m1-content-preparation.md',
 'docs/design/m1-extended-journeys.md',
 'docs/adr/0012-confirm-delegated-updates-per-assignment.md',
 'docs/adr/0011-shared-menu-content-and-contextual-maintenance.md',
 'docs/adr/0010-diner-account-and-display-recovery.md',
 'docs/adr/README.md', 'docs/README.md', 'CHANGELOG.md',
 'docs/product/m1-design-briefs.md', 'docs/product/m0-journeys-and-criteria.md',
 'docs/project/roadmap.md', 'docs/project/m0-closeout.md',
]
def anchors(s):
 return [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in re.findall(r'^#{1,6} (.+)$', s, re.M)]
links=0
for name in paths:
 p=root/name
 s=p.read_text(encoding='utf-8')
 assert s.count('```')%2==0, ('fences',name)
 a=anchors(s)
 assert len(a)==len(set(a)), ('headings',name)
 assert not re.search(r'^(<<<<<<<|=======|>>>>>>>)',s,re.M),name
 width=None
 for line in s.splitlines():
  if line.startswith('|'):
   current=len(line.split('|'))
   if width is None: width=current
   assert current==width,('table',name,line)
  else: width=None
 for link in re.findall(r'\]\(([^)]+)\)',s):
  if link.startswith(('https://','http://','mailto:')): continue
  dest,_,frag=link.partition('#')
  target=p.parent/dest if dest else p
  assert target.exists(),(name,link)
  if frag: assert frag in anchors(target.read_text(encoding='utf-8')),(name,link)
  links+=1

baseline='f2ba724'
def original(name):
 return subprocess.check_output(['git','show',f'{baseline}:{name}'],cwd=root).decode('utf-8')
def text(name): return (root/name).read_text(encoding='utf-8')
name='docs/design/m1-extended-journeys.md'
s=text(name);old=original(name)
cards=lambda d: dict(re.findall(r'^### (J\d{2}-[POAC]\d{2}):[^\n]*\n(.*?)(?=^### |^## |\Z)',d,re.M|re.S))
a,b=cards(old),cards(s)
assert set(a)==set(b) and len(b)==38
modified=[k for k in a if a[k]!=b[k]]
assert set(modified)=={'J15-A06','J15-P02','J15-P03'},modified
assert set(re.findall(r'J\d{2}-[POAC]\d{2}',s))<=set(b),'undefined state'
for key in modified:
 for field in ['Actor /','Composition','Actions','Failure' if key!='J15-P03' else 'Error']:
  assert re.search(field,b[key],re.I),(key,field)
assert re.findall(r'^\| (LC\d{2}) ',s,re.M)==[f'LC{i:02}' for i in range(1,7)]
for row in re.findall(r'^\| LC\d{2} .*$',s,re.M):
 assert 'FP' in row and 'FC' in row and 'J15-' in row,row
 assert any(k in row.lower() for k in ['unknown','uncertain','current source cannot','uncertainty']),row
q=lambda d:dict(re.findall(r'^(\| Q\d{2}) (.*)$',d,re.M))
qo,qn=q(old),q(s)
assert set(qo)==set(qn) and len(qn)==20
assert [k for k in qo if qo[k]!=qn[k]]==['| Q17']
for tag in ['V','PC','DS','SC']:
 filename={'V':'docs/design/m1-connected-journey.md','PC':'docs/design/m1-content-preparation.md','DS':'docs/design/m1-content-preparation.md','SC':'docs/design/m1-service-and-maintenance.md'}[tag]
 pattern=r'^\| '+tag+r'\d{2} .*$'
 assert re.findall(pattern,text(filename),re.M)==re.findall(pattern,original(filename),re.M),tag
for tag in ['E','W','XF']:
 pattern=r'^\| '+tag+r'\d{2} .*$'
 assert re.findall(pattern,s,re.M)==re.findall(pattern,old,re.M),tag
mapping=lambda d:dict(re.findall(r'^(\| J1[0-5]\.\d) (.*)$',d,re.M))
m1,m2=mapping(old),mapping(s)
assert len(m2)==20 and set(m1)==set(m2)
assert set(k for k in m1 if m1[k]!=m2[k])=={'| J15.3','| J15.4'}
for filename in ['docs/design/m1-content-preparation.md','docs/design/m1-service-and-maintenance.md']:
 states=lambda d:dict(re.findall(r'^### ((?:CP|J[89])-[A-Z]\d{2}):[^\n]*\n(.*?)(?=^### |^## |\Z)',d,re.M|re.S))
 assert states(text(filename))==states(original(filename)),filename
source='docs/product/m0-journeys-and-criteria.md'
rows=lambda d:re.findall(r'^- \*\*J\d+\.\d:.*$',d,re.M)
assert rows(text(source))==rows(original(source))
for filename in ['docs/product/m0-capability-matrix.md','docs/research/storefront-digital-menu/functional-definition/functional-definition.es.md']+[f'docs/adr/{n}' for n in ['0008-first-launch-capability-commitment.md','0009-studio-design-and-registered-diner-personalisation.md','0010-diner-account-and-display-recovery.md','0011-shared-menu-content-and-contextual-maintenance.md','0012-confirm-delegated-updates-per-assignment.md']]:
 assert text(filename)==original(filename),filename
assert '72' in text('docs/design/m1-connected-journey.md')
# Confirm meaningful recovery boundaries appear in the actual states, alongside six manual contrasts.
for marker in ['same-identity','meaning','unresolved reference','Sin preferencia','late','unknown','FP2','independent recheck pending','M2/#4']:
 assert marker.lower() in s.lower(),marker
print(f'PASS: {links} local/internal links in 14 docs; fragments/headings/fences/tables; 38 states with only J15-A06/P02/P03 changed; six LC contrasts; only Q17 and J15.3/J15.4 mappings refined.')
print('PASS: other 63 prior V/Q/PC/DS and 26 SC rows, all E/W/XF rows, CP/J8-J9 state cards, source criteria/matrix/definition/ADR-0008-0012 unchanged from f2ba724. Independent recheck remains pending. Documentary check only.')
