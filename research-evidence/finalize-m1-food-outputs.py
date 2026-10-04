from pathlib import Path
import subprocess,json,hashlib

root=Path(r'D:\the next level\valiris-restaurants')
evidence=Path(r'D:\the next level\research-evidence')
def run(*args):
    return subprocess.check_output(args,cwd=root).decode('utf-8').strip()
commit=run('git','rev-parse','HEAD')
assert run('git','branch','--show-current')=='docs/m1-connected-journey'
assert not run('git','status','--porcelain')
assert commit==run('git','rev-parse','@{upstream}')
assert run('git','log','-1','--format=%an <%ae>')=='Yahya <yaboula@epsa.upv.es>'
assert not run('git','log','-1','--format=%(trailers:only)')
pr=json.loads(run('gh','pr','view','21','--json','body,headRefOid,isDraft,state,url,title'))
expected=(evidence/'pr21-food-register-and-outputs-body.md').read_text(encoding='utf-8').strip()
assert pr['headRefOid']==commit and pr['isDraft'] and pr['state']=='OPEN'
assert pr['body'].strip()==expected
assert pr['title']=='docs(product): describe M1 public, management and service journeys'
issue=json.loads(run('gh','issue','view','5','--json','state,url'))
assert issue['state']=='OPEN'
source=root/'docs/design/m1-food-register-and-outputs.md'
result={'commit':commit,'branch':'docs/m1-connected-journey','clean':True,'upstreamMatch':True,
 'author':'Yahya <yaboula@epsa.upv.es>','trailers':[],
 'pr':{k:pr[k] for k in ['url','headRefOid','title','state','isDraft']},'bodyMatches':True,
 'M1':issue,'FO_SHA256':hashlib.sha256(source.read_bytes()).hexdigest()}
(evidence/'m1-food-register-and-outputs-final-state.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
record=evidence/'m1-food-register-and-outputs-review-2026-10-02.md'
report=record.read_text(encoding='utf-8')
report+='\n## Final observed delivery\n\nCommit `'+commit+'` pushed to existing `docs/m1-connected-journey`; local tree clean and upstream identical. Staged whitespace check passed; seven canonical files,380 insertions/13 deletions. Local author Yahya <yaboula@epsa.upv.es>, no trailers. PR #21 OPEN/draft with exact HEAD and prepared body read back; M1 #5 OPEN. No merge/closure. FO raw-file SHA256 `'+result['FO_SHA256']+'`. Structured readback: [final-state JSON](m1-food-register-and-outputs-final-state.json).\n'
record.write_text(report,encoding='utf-8',newline='\n')

handoff=Path(r'D:\the next level\HANDOFF.md')
before=handoff.read_bytes()
text=before.decode('utf-8')
marker='### Revisión paralela G1 y G4 de C1–C3'
assert text.count(marker)==1
head,tail=text.split(marker,1)
old='Siguiente bloque pendiente: J6–J7, tras entrega de G2.'
assert head.count(old)==1
head=head.replace(old,'J6–J7 ya entregado por G2 en '+commit[:7]+', comprobado documentalmente por su autor; revisión independiente FO y evidencia real pendientes. Siguiente trabajo: consolidar cobertura/huecos y preparar el plan concreto de expresión visual, interacción y evidencias.',1)
section='''### Entrega vigente G2 J6–J7 — 2 de octubre de 2026

Continúa exactamente el encargo M1/#5 en la rama y PR existentes. [Registro alimentario y salidas](valiris-restaurants/docs/design/m1-food-register-and-outputs.md): 18 fichas FO-F01–F06/FO-O01–O06/FO-Q01–Q03/FO-X01–X03, siete criterios J6.1–J6.3/J7.1–J7.4, 22 filas afectadas, cinco recorridos FW y 24 contrastes FC. Documentación inglesa/copy español, C1–C3 ficticios. Registro contextual del personal, positivos/pendientes y fuente revisada, receta futura privada frente a discrepancia conocida de lo servido, glosario/idiomas, tres usos de salida, archivo generado/recuperado/papel colocado y destino público/QR mantienen sus diferencias.

Comprobación documental del autor: 478 enlaces locales/internos en17 documentos;18 fichas/campos/destinos/siete criterios/22 filas/cinco FW/24 FC, tablas/fragmentos/headings/fences. Todos los152 casos anteriores y fichas preservados contra120903f; criterios originales/matriz/definición/todos los ADR intactos,72 padres una vez/S1,S2 separados. Checks relevantes previos pasan:JT440/PV404/extended264/J15 372 enlaces y C1–C3 42locales/55acciones. El texto histórico del checker J15 no cambia la relectura G4/G1 ya resuelta. Evidencia: [registro del autor](research-evidence/m1-food-register-and-outputs-review-2026-10-02.md), checker FO y JSON de estado final fuera de Git. Sin suites de software ni archivos/QR/impresión/escaneo/registro alimentario real/pruebas con usuarios.

G2 leyó los retornos consolidados PV/9cfe77b y JT/120903f: sin corrección documental requerida en sus alcances; fuentes/snapshots e informes independientes intactos. Ninguno revisa FO ni demuestra implementación, UX real, seguridad, información alimentaria o conformidad. G1 coordina revisión independiente G4 sobre este commit cuando haya disponibilidad, contratos G3 y fuentes/procedimientos/idiomas/URLs/materiales G5; contribuciones pendientes, no mensajes enviados ni revisiones inventadas.

Commit COMMIT, subido; PR #21 OPEN/draft, cuerpo/HEAD exactos verificados; árbol limpio/upstream idéntico, autor Yahya <yaboula@epsa.upv.es> sin trailers. Índices, mapa, briefs, roadmap, evidencia de criterios y changelog actualizados. M1/#5 OPEN; M2/#4 mantiene contratos; sin merge/cierre.

Siguiente acción G2: auditoría transversal de cobertura de las72 capacidades/S1,S2 y criterios, identificar huecos reales y preparar un plan concreto de dirección visual/plantillas-bespoke/público/móvil/personal/papel/pantalla/accesibilidad/interacción/evidencias. No declarar100%M1 por completar descripciones. Revisión independiente FO, materiales/fuentes/destinos autorizados, contratos técnicos y pruebas reales siguen separados.

'''.replace('COMMIT',commit)
assert '### Entrega vigente G2 J6–J7' not in head
new=head+section+marker+tail
assert new.split(marker,1)[1]==tail
assert handoff.read_bytes()==before,'HANDOFF changed concurrently; reread before applying'
handoff.write_bytes(new.encode('utf-8'))
assert handoff.read_bytes().decode('utf-8').split(marker,1)[1]==tail
print(json.dumps(result,ensure_ascii=False,indent=2))
print('HANDOFF current FO continuity added; independent-review history preserved byte-for-byte.')
