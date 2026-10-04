from pathlib import Path
import subprocess,json,re,hashlib

workspace=Path(r'D:\the next level')
root=workspace/'valiris-restaurants'
evidence=workspace/'research-evidence'
def run(args):return subprocess.check_output(args,cwd=root).decode('utf-8').strip()
head=run(['git','rev-parse','HEAD'])
assert head=='120903f138a798e957b26498f2a3efb5d5e6521a',head
assert not run(['git','status','--porcelain'])
assert head==run(['git','rev-parse','@{upstream}'])
assert run(['git','log','-1','--format=%an <%ae>'])=='Yahya <yaboula@epsa.upv.es>'
assert not run(['git','log','-1','--format=%(trailers)'])
pr=json.loads(run(['gh','pr','view','21','--json','headRefOid,title,isDraft,state,url,body']))
issue=json.loads(run(['gh','issue','view','5','--json','state,url']))
assert pr['headRefOid']==head and pr['isDraft'] and pr['state']=='OPEN'
assert issue['state']=='OPEN'
body=(evidence/'pr21-scheduling-body.md').read_text(encoding='utf-8')
assert pr['body'].strip()==body.strip(),'PR body mismatch'
assert 'Closes #' not in pr['body']
subprocess.run(['git','diff','--check'],cwd=root,check=True)

handoff=workspace/'HANDOFF.md'
before=handoff.read_bytes();s=before.decode('utf-8')
marker='### Revisión paralela G1 y G4 de C1–C3'
assert s.count(marker)==1
prefix,tail=s.split(marker,1)
already_inserted='Entrega J4–J5, 2 de octubre, 120903f' in prefix
entry='''**Entrega J4–J5, 2 de octubre, 120903f:** [m1-scheduling-and-service-continuity.md](valiris-restaurants/docs/design/m1-scheduling-and-service-continuity.md) entrega 21 fichas JT, ocho criterios J4.1–J4.4/J5.1–J5.4, 20 capacidades afectadas, seis TW y 30 TC. Distingue horarios local/cocina/oferta, excepción y vigencia, contenido guardado/programado/ejecutado/público, revisión de cambios y carreras al cancelar/sustituir, disponibilidad urgente por grupo, revisión del próximo servicio e historial/corrección acotada. La publicación de contenido conserva disponibilidad urgente aplicable más reciente; nunca confirma existencias al iniciar otro servicio. Mantiene borradores del croissant/D11, datos alimentarios conocidos/pendientes y salidas físicas separadas. Elección de programación privada hasta ejecución confirmada frente a publicación futura expresa sigue propuesta X06, pendiente G1/G3; ningún ADR aceptado cambia.

**Comprobación y continuidad vigente tras J4–J5:** autor G2: 431 enlaces en 16 documentos, fragmentos/tablas/IDs/campos/destinos/versiones, ocho criterios exactos y cobertura única de 72/S1/S2; 122 contrastes anteriores y cuerpos de todas las fichas/fuentes/ADR conservados frente a 9cfe77b. Checker JT y regresión PV/C1–C3/extendido/J15 pasan; TF01–TF03 corrigen fragmentos, disponibilidad nueva frente a snapshot programado y referencias ambiguas. Diff/staged/autor EPSA sin trailers/commit/push/cuerpo-HEAD de [PR #21](https://github.com/yaboula/valiris-restaurants/pull/21) OPEN/draft/#5 OPEN/checkout limpio y sincronizado confirmados; HEAD actual `120903f138a798e957b26498f2a3efb5d5e6521a`. [Registro del autor y encargo de relectura](research-evidence/m1-scheduling-review-2026-10-02.md), [checker](research-evidence/check-m1-scheduling.py) y readback JSON fuera de Git. Sin suites de software, Figma, implementación, mensajes a otros chats, merge ni cierre M1.

**Orden actual:** J4–J5 diseñado y comprobado documentalmente por G2; revisión independiente JT pendiente. El dictamen G1/G4 J8–J9 sobre 9cfe77b, recibido durante esta entrega, no requiere correcciones documentales acotadas y queda registrado en mapa/briefs/roadmap/PR. PV/J1–J2 conserva revisión independiente pendiente hasta un retorno real. Los estados anteriores de siguiente bloque/revisión quedan como historia fechada. Siguiente bloque descriptivo G2: J6–J7 registro alimentario mantenido/personal y salidas carta/papel/QR; dirección visual, interacción, accesibilidad, participantes, contratos M2/#4, material real y revisión independiente siguen en sus checkpoints. G1 coordina revisiones G4 y aportaciones concretas G3/G5/G6 sin suponer disponibilidad o pruebas realizadas; M1/#5 abierto y 72 capacidades/S1/S2 intactas.

'''
out=s if already_inserted else prefix+entry+marker+tail
assert out.split(marker,1)[1]==tail,'history changed'
for dest in re.findall(r'\]\(([^)]+)\)',entry):
 if dest.startswith('https://'):continue
 assert (workspace/dest.split('#')[0]).exists(),dest
assert handoff.read_bytes()==before,'HANDOFF changed during preparation'
handoff.write_bytes(out.encode('utf-8'))
assert handoff.read_bytes().decode('utf-8').split(marker,1)[1]==tail

result={k:pr[k] for k in ['headRefOid','title','isDraft','state','url']}
result.update({'m1Issue':issue,'clean':True,'synchronised':True,'author':'Yahya <yaboula@epsa.upv.es>','trailers':[], 'bodyMatches':True,'handoffHistoryPreserved':True,'documentaryOnly':True,'links':431,'states':21,'criteria':8,'capabilityRows':20,'contrasts':30,'priorContrastsPreserved':122})
(evidence/'m1-scheduling-final-readback.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
record=evidence/'m1-scheduling-review-2026-10-02.md'
with record.open('a',encoding='utf-8') as f:
 f.write('\nCompleted: commit `'+head+'` (seven canonical files, 414 additions/seven removals), author Yahya/EPSA, empty trailers. Normal/staged whitespace checks pass. Push confirmed; PR #21 exact current HEAD/body/title OPEN/draft and #5 OPEN; checkout clean/equal upstream. Current HANDOFF adds delivery/current next order while preserving all independent-review/history text. Final readback JSON records these checks. No merge, software suite, independent JT acceptance or M1 closure.\n')
print('PASS: exact PR HEAD/body OPEN/draft, #5 OPEN, author/trailers, clean/upstream, HANDOFF review/history preserved. '+head)
