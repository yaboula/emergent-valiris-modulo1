from pathlib import Path
import subprocess,json,hashlib

r=Path(r'D:\the next level\valiris-restaurants')
e=Path(r'D:\the next level\research-evidence')
def run(*args):return subprocess.check_output(args,cwd=r).decode('utf-8').strip()
commit=run('git','rev-parse','HEAD')
assert run('git','log','-1','--format=%s')=='docs(product): consolidate M1 capability coverage and evidence'
assert run('git','branch','--show-current')=='docs/m1-connected-journey'
assert not run('git','status','--porcelain')
assert commit==run('git','rev-parse','@{upstream}')
assert run('git','log','-1','--format=%an <%ae>')=='Yahya <yaboula@epsa.upv.es>'
assert not run('git','log','-1','--format=%(trailers:only)')
pr=json.loads(run('gh','pr','view','21','--json','body,headRefOid,isDraft,state,title,url'))
assert pr['headRefOid']==commit and pr['state']=='OPEN' and pr['isDraft']
assert pr['title']=='docs(product): describe M1 public, management and service journeys'
assert pr['body'].strip()==(e/'pr21-coverage-consolidation-body.md').read_text(encoding='utf-8').strip()
issue=json.loads(run('gh','issue','view','5','--json','state,url'))
assert issue['state']=='OPEN'
hashes={str(p.relative_to(r)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [r/'docs/design/m1-connected-journey.md',r/'docs/design/m1-coverage-and-evidence.md']}
result={'commit':commit,'branch':'docs/m1-connected-journey','clean':True,'upstreamMatch':True,
 'author':'Yahya <yaboula@epsa.upv.es>','trailers':[],
 'PR':{k:pr[k] for k in ['url','title','headRefOid','state','isDraft']},'bodyMatch':True,
 'M1':issue,'sourceSHA256':hashes}
(e/'m1-coverage-consolidation-final-state.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=e/'m1-coverage-consolidation-review-2026-10-02.md'
record=p.read_text(encoding='utf-8')
record+='\n## Final observed delivery\n\nCommit `'+commit+'` pushed to existing docs/m1-connected-journey. Normal/staged whitespace PASS; seven canonical files,307 insertions/30 deletions. Local tree clean/upstream identical; author Yahya <yaboula@epsa.upv.es>,no trailers. PR #21 OPEN/draft with exact prepared body and HEAD read back; M1 #5 OPEN. No merge/closure or external messaging. Structured readback: [final-state JSON](m1-coverage-consolidation-final-state.json).\n'
p.write_text(record,encoding='utf-8',newline='\n')

h=Path(r'D:\the next level\HANDOFF.md')
before=h.read_bytes();s=before.decode('utf-8')
marker='### Revisión paralela G1 y G4 de C1–C3'
assert s.count(marker)==1
head,tail=s.split(marker,1)
intro='''**Actualización G2 vigente — consolidación de cobertura:** commit COMMIT subido a PR #21 OPEN/draft. El mapa existente contiene72 filas individuales;59 criterios localizados; juicio documental del autor69 recorridos escritos suficientes/tres contribuciones visuales parciales, sin equivaler a capacidades terminadas ni porcentaje de M1. J6–J7 tiene retorno final G1/G4 sobre a0583e0 sin corrección documental requerida. La consolidación nueva aún requiere revisión independiente; siguiente encargo G2: identidad/plantillas/diseño propio y composición pública/gestión C1–C3 con guiones de interacción/evidencias. M1/#5 permanece OPEN. Esta actualización supersede los pendientes de consolidación de las notas anteriores, sin cambiar su historia ni sus límites.

'''.replace('COMMIT',commit)
heading='## Estado vigente — 2 de octubre de 2026'
assert heading in head
head=head.replace(heading+'\r\n\r\n',heading+'\r\n\r\n'+intro,1) if heading+'\r\n\r\n' in head else head.replace(heading+'\n\n',heading+'\n\n'+intro,1)
section='''### Consolidación vigente de72 capacidades — G2, 2 de octubre de 2026

Entregado [mapa individual](valiris-restaurants/docs/design/m1-connected-journey.md#7-compact-coverage-and-remaining-work) y [informe de criterios/revisiones/huecos/evidencias](valiris-restaurants/docs/design/m1-coverage-and-evidence.md). Mapa único:72 padres una vez,36 incluidos/30 configurables/seis dependientes de conexión;S1/S2 y audio-3D separados. Cada fila contiene estado concreto, criterio/contraste, revisión acotada y pendiente/checkpoint. Informe complementario:59 criterios, RV01–RV07,17 entradas CG con seis conexiones individuales, alcance/evidencia/responsable/efecto de cierre y siguiente encargo concreto. No duplica inventario/backlog.

Juicio del autor:69 recorridos escritos suficientes para continuar diseño;B1.05 identidad/B1.06 plantillas/B1.07 diseño propio parciales por faltar contribución visual esencial. Ningún recorrido escrito ausente o contradicción sustantiva nueva fue reproducido en este contraste. Esto no declara69 capacidades completadas, aceptación independiente global,100%M1 o validación real. Todos176 casos y cuerpos de fichas conservados contraa0583e0;criterios originales/matriz/definición/ADRs intactos. Retorno final FO/G1/G4 a0583e0 incorporado, sin corrección requerida al nivel documental acotado; fuentes e informes independientes históricos intactos. Revisión de la consolidación nueva pendiente CG11; autor y calidad independientes siguen separados.

Comprobación:1.809 enlaces locales/internos en18 documentos,filas/treatments/59criterios/referencias de estados/casos/RV/CG/fragmentos/tablas/headings/fences. Checkers anteriores relevantes pasan (FO1.235/JT1.197/PV1.161/C1–C3 794locales+55acciones/extended1.021/J15 1.129). Sin suites de software, prototipo/Figma, assets/salidas/escaneo/dispositivo, fuente alimentaria/usuario real, APIs/contratos o activación/mensajes a especialistas. Evidencia externa: [registro del autor](research-evidence/m1-coverage-consolidation-review-2026-10-02.md),check-m1-consolidation.py y estado JSON; helper/datos fuera de Git.

Commit COMMIT, subido y limpio/upstream idéntico;autor Yahya <yaboula@epsa.upv.es> sin trailers;PR #21 OPEN/draft,cuerpo/HEAD exactos verificados;M1/#5 OPEN,sin merge/cierre. Índice/changelog/briefs/roadmap/evidencia de criterios/continuidad actualizados. M2/#4 mantiene contratos;D3 y comercial/#15 mantienen sus checkpoints.

Siguiente G2: [encargo visual/interacción](valiris-restaurants/docs/design/m1-coverage-and-evidence.md#6-next-g2-visual-and-interaction-assignment). Resolver identidad/template/bespoke con C1 sin fotos y C2/C3 contexto/formatos/alimentación;composición pública y gestión y guiones críticos;después A4/personal/pantalla/QR/locales y evidencia de accesibilidad/interacción. Las59 correspondencias son trazabilidad,no criterios pasados. G1 coordina aportaciones reales de G3/G4/G5/G6;materiales/participantes/destinos/acceso/revisiones siguen explícitos. No repetir benchmark ni reconstruir secuencia aleatoria;el informe conserva alcance completo y siguiente resultado.

'''.replace('COMMIT',commit)
assert '### Consolidación vigente de72 capacidades' not in head
new=head+section+marker+tail
assert h.read_bytes()==before,'HANDOFF changed concurrently; reread before applying'
h.write_bytes(new.encode('utf-8'))
assert h.read_bytes().decode('utf-8').split(marker,1)[1]==tail
print(json.dumps(result,ensure_ascii=False,indent=2))
print('HANDOFF current consolidation inserted; independent review history preserved byte-for-byte.')
