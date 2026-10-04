# M1 J4–J5 — scheduling, exceptions and service continuity

2 October 2026 · G2 Product Design · Descriptive continuation under [M1 #5](https://github.com/yaboula/valiris-restaurants/issues/5), draft PR #21.

**Status:** complete descriptive proposal, checked documentarily by the author; independent review pending. English documentation and Spanish interface copy; fictional examples are not a working calendar, stock system or usability evidence. No software, Figma, provider, time executor or permission implementation. Technical contracts remain in [M2 #4](https://github.com/yaboula/valiris-restaurants/issues/4); M1 stays open.

## 1. Assignment, sources and review boundary

The owner authorised the next J4/J5 block while G4 reviews J8/J9 and J1/J2 separately. G2 consolidates scheduling/calendar/manual exceptions, controlled publication, urgent mobile/bulk availability and scoped history/recovery. This supplies the remaining descriptions behind all eight [J4.1–J4.4/J5.1–J5.4 criteria](../product/m0-journeys-and-criteria.md#j4--operator-publishes-or-schedules), without replacing previously reviewed states or removing launch scope.

Reuse [C1–C3 and publication/urgent recovery](m1-connected-journey.md), [content preparation](m1-content-preparation.md), [public presence/discovery](m1-public-presence-and-discovery.md), [J10–J15](m1-extended-journeys.md), [service/maintenance](m1-service-and-maintenance.md), [briefs](../product/m1-design-briefs.md), [roadmap](../project/roadmap.md), [capability matrix](../product/m0-capability-matrix.md), [functional definition](../research/storefront-digital-menu/functional-definition/functional-definition.es.md) and ADRs [0005](../adr/0005-repository-and-product-language.md), [0008](../adr/0008-first-launch-capability-commitment.md), [0009](../adr/0009-studio-design-and-registered-diner-personalisation.md), [0010](../adr/0010-diner-account-and-display-recovery.md), [0011](../adr/0011-shared-menu-content-and-contextual-maintenance.md), [0012](../adr/0012-confirm-delegated-updates-per-assignment.md). Accepted decisions and all earlier card/contrast bodies remain intact.

Independent continuity: bounded G1/G4 reviews resolved G4-01 on c4f219c and G4-J15-01 on 2eb8e86; the separate CP review on 2eb8e86 requested no documentary correction. During JT authoring, the separate consolidated G1/G4 J8/J9 report on 9cfe77b also arrived without required documentary correction; it was read with its stated limits. Those returns do not review this JT delivery. PV review remains pending until an actual return, not inferred from the ongoing review. No reviewer is activated or messaged by this document. G1 coordinates actual G3/G4/G5 contributions; their contracts/materials/results remain pending at the affected checkpoint.

**Value and cost hypothesis:** diners can distinguish readable planned content, current service and communicated availability; operators can prepare future work and correct the selected live scope; Valiris must support meaningful status checks, conflicts and service training. None establishes saved time, reliability, sales or reduced support cost. C1 keeps direct content/service controls without mandatory calendar configuration; C2/C3 reveal relevant dates/zones/formats only.

## 2. Proposed shared behavior and fixture branches

**Time and scope:** separate local opening, kitchen service, offering validity and publication time. Scope identifies restaurant/location, menu, zone, service/date, item/format and relevant field; languages share prices/status/validity rather than separate copies. Show venue-local date/time and timezone; viewer/device time does not silently change them. C3 uses Europe/Madrid, publication at 2 October 2026 12:15 and ordinary service validity [13:00, 15:30). At an end boundary the service is over; a readable historical offer is not current. No UTC offset, clock accuracy or time execution guarantee is invented.

**Calendar composition:** explicit applicable regular periods and published exceptions generate an inspectable date/service preview. A kitchen exception does not close the local; a terrace exception does not alter General. A declared one-date end does not overwrite next-day normal hours. Conflicting applicable periods, services, zones or same-target publication intents are shown before authorisation; no hidden priority among conflicting exceptions or duplicate schedules. Resolve the affected group or deliberately exclude it and review the remaining group. A manual exception's explicit reviewed precedence over normal hours follows existing X06; withdrawing it re-evaluates current underlying rules, not an old whole-menu snapshot.

**Scheduling policy, proposed rather than a new founder decision:** retain [X06](m1-connected-journey.md#x06-scheduling-and-manual-exception): a schedule authorises a specific confirmed saved revision and coherent scope at a stated future time; it leaves content private until a confirmed execution. A separately reviewed immediate publication of future-valid content enables advance consultation. These are distinct intents; publishing early does not silently leave a second replacement active. Changes to target/dependencies require fresh review/re-authorisation or cancellation. G1/G3 must settle authority, consistency, execution races and lifecycle contracts before affected closure. No new ADR or retrospective accepted decision is introduced here.

**Recurring periods versus content:** a regular weekly service describes when an offering can apply, not permission to reuse yesterday's daily menu or publish the latest draft. Optional repeated publication authorisation must show the exact reviewed revision, occurrences, timezone and explicit applicable end/stop policy. It cannot select a new revision automatically. A missing daily target remains missing. Unknown end/time/scope blocks the affected intent; no invented recurrence limit or implicit endless exception. Overlapping overnight intervals are checked by their actual start/end dates, not truncated at midnight.

**Different visible statuses:** local proposal; last confirmed saved revision; latest authorised current revision; authorised schedule; execution result; current public publication and present validity are separate. Schedule lifecycle labels are **Programado · no publicado / En ejecución · resultado pendiente / Bloqueado por revisión / Cancelado / Sustituido / Fallido / Publicado / Resultado desconocido** only when evidence supports them. Elapsed time or an equal public amount cannot prove execution. A successful past action may be superseded by a later publication; keep both facts, not a false current success.

**Late result and recovery:** responses carry the original intent/scope/source/result conceptually; a response from a prior date/context, source revision, actor or venue cannot replace the current view. Check original outcome before retry/cancel/undo. Known failure preserves earlier history and allowed work, while respecting expiry/absence of any prior publication. Uncertain execution stays uncertain; do not claim a pause, cancellation or no effect merely because the requester lost access. A missed publication is not silently backdated or executed after its validity; review an applicable current intent or prepare another service explicitly.

**Temporary availability:** C1/C3 use explicit review at the next applicable service. Marking sold out names item/context and service end, not a private editorial version. Restoring in the current service is a new scoped action. A continuing exception must be deliberately reviewed with its actual end/stop rule; an old service's status is history. No automatic restock or inferred available stock from time, scheduled menu, exception expiry or copy. Editorial/scheduled publication in the same current service must reconcile and preserve the latest applicable live availability unless a separate deliberate current availability correction is authorised; its saved content snapshot cannot restore an older available flag. A missing/withdrawn/private target cannot receive a live availability action. Status is supplied by the restaurant or actual authorised source; it is not measured stock or an order promise.

**Dependent output and food:** any selected factual/common change uses CP shared-group rules, current positive declarations plus pending remainder, nutrition/diet review and affected language fallback/withholding. Unknown food never becomes zero/absence/suitability. A schedule cannot revive an old claim when its recipe, format or relationship changed. Current highlights/directed pairings/personal choices follow current published applicability; unrelated private drafts remain private. New paper generation is not physical replacement, owned success is not external distribution, and unattended display freshness differs from loaded diner offline content.

### Reset fixtures, not one cumulative timeline

| Branch | Fictional starting point and explicit contrast |
| --- | --- |
| T-C1 | Existing C1: 1 October 10:00 Europe/Madrid; Monday–Saturday local 08:00–17:00, breakfast 08:00–12:00. Coffee remains 1,90 € unless its separate 2,00 € publication is confirmed. Croissant 2,20 €, pending food, independent description draft stays private. Its live sold-out scope is today's breakfast, not all future days. |
| T-C2 | Existing confirmed cheese formats/context and independent shared/copy identities; terrace media 26,00 €, complete 36,00 €, extra bread 2,20 €; General media 24,00 €, complete 34,00 €, extra 2,00 €. Conditional service-bound bulk availability uses a supplied selected current service/end; C2 has no invented hours. CP's distinct 27,00 €/2,30 € editorial proposal branch is not an already published update. |
| T-C3-S | Reset L10 published 1 October lunch 16,50 €/person and private D11r1 for 2 October 17,50 €. Schedule D11r1 at 2 October 12:15; validity 13:00–15:30. Confirmed execution alone creates L11. Target edit D11r2 is a new private revision, not silently bound to the schedule. |
| T-C3-E | Separate X06 kitchen exception: 2 October 13:30–15:30, end 15:30; local remains 12:30–17:00. Review/reschedule matching offering validity, or explicitly revise/cancel exception. No new recurring weekday pattern is invented for C3. |
| T-C3-U | Reset current L10, flan milk/egg declared with remaining pending, private D11. Sold out creates L10a only for 1 October lunch; no-conflict current-service correction creates L10b. Next-service availability unconfirmed; D11 is not published by restoration. |
| T-C3-F | Separate L10c ingredient branch: crema with supplied milk, remaining food pending and EN fallback. Historical/scheduled recovery must not restore old EN or erase declared milk; no numerical nutrition, diet attribute or authorised media is fabricated. |

Publication/version names remain those of the original fixtures. Additional schedule/exception/result references below are descriptive labels, not generated production records. Real regular hours, exceptions, sources, recurring policies and contact destinations remain to obtain from each restaurant.

### Entry and inherited destinations

| Task boundary | Existing continuation |
| --- | --- |
| Enter/edit/preview/select/publish/result | [O01](m1-connected-journey.md#o01-venue-and-task-entry), [O02](m1-connected-journey.md#o02-content-editor), [O03/O04](m1-connected-journey.md#o03-review-and-preview), [O05](m1-connected-journey.md#o05-selected-publication), [O06](m1-connected-journey.md#o06-publication-result) |
| Current urgent/undo/next service | [O07](m1-connected-journey.md#o07-urgent-availability), [O08](m1-connected-journey.md#o08-undo-and-current-state-review), [X07](m1-connected-journey.md#x07-next-service-availability-review) |
| Shared facts/bulk/history/save uncertainty/access | [CP-S02](m1-content-preparation.md#cp-s02-review-a-shared-change), [CP-B01–CP-B04](m1-content-preparation.md#cp-b01-choose-bulk-mode-and-scope), [CP-X01–CP-X03](m1-content-preparation.md#cp-x01-conflicting-revisions) |
| Current public presence/detail/changed target | [PV-P02/PV-P03](m1-public-presence-and-discovery.md#pv-p02-visit-information-and-declared-attributes), [PV-P06](m1-public-presence-and-discovery.md#pv-p06-detail-and-return-to-the-choice), [PV-P11](m1-public-presence-and-discovery.md#pv-p11-unavailable-changed-or-unconfirmed-public-target) |
| Maintenance and output consequence | [J9-M01](m1-service-and-maintenance.md#j9-m01-inspect-actionable-maintenance), [J9-M04](m1-service-and-maintenance.md#j9-m04-check-affected-outputs-and-physical-actions), [J10-P04/J10-P05](m1-extended-journeys.md#j10-p04-loaded-public-snapshot), [J12-O02](m1-extended-journeys.md#j12-o02-observe-refresh-and-reconcile) |

Links navigate descriptions, not executed product actions. The structural check must verify their exact fragments rather than assume the wording above.

## 3. Operator states — calendar and controlled publication

### JT-O01: Service and programming overview

**Actor / objective / entry / version:** permitted venue operator enters Servicio or Programación from O01/J9-M01; locate current offering and authorised future work. Identify venue/location, current service/time source, confirmed public revision, private drafts and known schedule/exception references separately.

**Composition / copy:** venue/current context → **Servicio actual / Próximas publicaciones / Horarios y excepciones / Historial**. C1 first shows today's breakfast and croissant status; calendar is optional. C3 shows L10/current or expired validity, D11 private and known schedule state. **“No hay menú del día publicado para este servicio”** differs from **“No podemos confirmar el estado actual”**; empty schedules are not failures.

**Actions / effect:** **Cambiar disponibilidad** → JT-O10; **Revisar próximo servicio** → JT-O14; **Preparar publicación** → JT-O04; **Horarios y excepciones** → JT-O02/JT-O03; **Ver historial** → JT-O15. Viewing/navigation does not publish or restore stock. Only relevant permitted actions appear, with readable denial if authority changes.

**Errors / recovery / check:** missing current scope/time → JT-X04, inaccessible venue → JT-X03, unresolved action → JT-X02. Check J4/J5: old menu/private target never presented as today's live menu and C1 requires no advanced setup.

### JT-O02: Maintain distinct regular periods

**Actor / objective / entry / version:** authorised content editor from JT-O01/PV-O01 maintains supplied local opening, kitchen and offering service periods. Local proposal and confirmed saved calendar revision are private; read the latest authorised current source before review.

**Composition / copy:** three labelled groups **Horario del local / Horario de cocina / Vigencia de la oferta**, relevant days/date range, local start/end, timezone and target location/zone. Optional **Añadir otro tramo** handles split periods; explicit next-day end handles overnight. C1 existing hours/breakfast are readable without requiring a new service definition; C3 has no unsupplied regular weekdays selected. **“Estos horarios aún no están publicados”**.

**Actions / effect:** **Guardar borrador** → existing O02 save reconciliation then JT-O04; **Vista previa por fecha y servicio** → JT-O04; **Añadir excepción** → JT-O03; cancel returns JT-O01 retaining only authorised confirmed/explicitly kept work. Changing timezone requires reviewing affected local dates/occurrences, not an invisible shift.

**Errors / recovery / check:** missing/end-before-start/timezone ambiguity or overlapping incompatible periods identifies fields and keeps inputs; do not auto-fix a date or infer closed from blank. Relevant changed source → JT-X01; unknown save → JT-X02; permission → JT-X03. Check J4.2/R03: local/kitchen/offer dates remain independently comprehensible before publication.

### JT-O03: Prepare scoped exceptions and conflicts

**Actor / objective / entry / version:** permitted editor from JT-O02/JT-O01 prepares a closure, changed kitchen period, zone restriction or temporary withdrawal. Source target, proposed start/end/stop rule and current applicable normal/published rules are explicit; a draft exception has no public precedence yet.

**Composition / copy:** **Qué cambia / Dónde y cuándo / Qué verá el comensal** → current versus exception → affected offering/schedules/languages/outputs. T-C3-E: **“Cocina: 2 octubre, 13:30–15:30. Local: 12:30–17:00, sin cambios”**; flag schedule's 13:00 validity. A whole-local closure and a kitchen-only change show different scope. Multiple conflicting exceptions are listed, without a silent winner.

**Actions / effect:** **Revisar efectos** → JT-O04/JT-O09; **Resolver conflicto** → JT-X01 with affected normal/exception/schedule choices; **Volver a editar** → JT-O02 or remain. Clearing/removing an exception proposes only that exception change; unrelated source content and future drafts remain unchanged.

**Errors / recovery / check:** unknown end or contradictory zone/date/service blocks that affected proposal, retaining others privately. Unknown save → JT-X02; denied access → JT-X03. Check J4.2: user can see and resolve exact precedence and end without mutating next day's normal hours or claiming a draft closure public.

### JT-O04: Review coherent selection and publication intent

**Actor / objective / entry / version:** authorised reviewer from JT-O01/JT-O03/CP-R03/JT-O02/JT-O03/JT-O15 compares chosen confirmed saved source against current public source, date/context/format and dependencies. A local unsaved/unconfirmed proposal can be inspected with its label but cannot masquerade as a saved reviewed target.

**Composition / copy:** chosen changes/current → proposed, local date/time/zone/service, preview **“Vista previa · no pública”**, food/language/relation/output effects and **“Seguirán privados”** list. Intent choices **Publicar ahora / Programar publicación**; **Publicar ahora para consulta futura** explicitly explains future validity and no stock assurance. C3 selection D11 alone excludes E10/other drafts; C1 coffee selection excludes croissant draft.

**Actions / effect:** immediate reviewed selection → original O05 then O06 or JT-X02; future schedule → JT-O05. Any known active same-target schedule is resolved explicitly in the reviewed intent before early publication; cancellation uncertainty cannot claim no second action. Change scope/dependencies → O03/CP-S02 then fresh preview. No incidental preview/save publishes.

**Errors / recovery / check:** changed revision/recipe/format/exception or overlapping authorisations → JT-X01; ambiguous amount/translation/food assertion returns its source review, not a fabricated value; denied publication → JT-X03. Check J4.1/J4.4: one coherent selected group, unrelated drafts intact and exact known public result required.

### JT-O05: Authorise a specific timed publication

**Actor / objective / entry / version:** actor with scheduling/publication authority from JT-O04 selects confirmed saved target revision, exact coherent group and venue-local publication time, distinct from offering validity. Authority is not inferred from content editing, availability or a diner account.

**Composition / copy:** T-C3-S **“Publicar D11r1 el 2 octubre a las 12:15 · Europe/Madrid. Menú: 13:00–15:30 · 17,50 €/persona”**; **“Seguirá privado hasta una publicación confirmada”**. Review affected ES/EN facts, conditions and exception. Optional repeat shows actual authorised occurrences/end/stop policy; each needs applicable reviewed content. One-time remains C3's fixture; no mandatory recurrence in C1.

**Actions / effect:** **Confirmar programación** → JT-O07 on known schedule-creation result; **Volver a revisión** → JT-O04. Creation confirms the authorisation, not L11. Changed target after authorisation → JT-O06; cancel/change plan → JT-O08. Subsequent execution must reconcile reviewed source/applicability and authority, not adopt latest draft.

**Errors / recovery / check:** time already passed, non-unique/nonexistent local moment or unsupported scope → JT-X04; current conflict → JT-X01; failed/unknown creation → JT-X02 before retry; permission → JT-X03. Check J4.2/J4.3: confirmed schedule binds intended saved revision; no blind duplicate scheduling or early public content.

### JT-O06: Review changed scheduled target

**Actor / objective / entry / version:** editor/reviewer sees a schedule whose saved target, common fact, format, translation or calendar applicability changed. Show authorised D11r1, local/saved D11r2 as actually known, latest source and original schedule's real outcome; permitted edit alone cannot silently re-authorise.

**Composition / copy:** **“El contenido programado cambió. Revisa la programación”**; per-field/relation/calendar differences, formerly authorised target and affected group. **“Bloqueado por revisión”** is a required proposed execution gate only if its state is confirmed; if race/paused outcome unknown, say **“No podemos confirmar si la publicación se detuvo”**. A common ingredient change carries food/nutrition/diet/translation dependencies across its uses.

**Actions / effect:** **Revisar nueva versión** → JT-O04/JT-O05 for explicit replacement authorisation; **Cancelar programación** → JT-O08; **Comprobar ejecución anterior** → JT-X02/JT-O07. A deliberate choice to retain r1 is possible only after a new coherent review establishes it still valid; it cannot bypass known changed food facts. Unrelated drafts stay private.

**Errors / recovery / check:** execution already confirmed → JT-O07 and current corrective review, not retroactive unpublish; inaccessible revision → JT-X03; current conflict → JT-X01. Check J4.2/J4.4: no undocumented old-to-new revision rebinding or claimed pause without evidence. G3 must validate the required consistency gate in M2.

### JT-O07: Inspect schedule lifecycle and actual execution

**Actor / objective / entry / version:** authorised schedule/history viewer from JT-O05/JT-O01/JT-X02 sees each original authorisation and execution result. Scheduled target, known result publication/time and current latest offering are distinct references.

**Composition / copy:** target/time/scope first → lifecycle label → original result → current validity/newer publication → pending recovery. Confirmed T-C3-S at 12:15: **“Publicado: L11 · menú del 2 octubre · 17,50 €/persona”**, still planned before 13:00. Failure: **“No se ha publicado este menú. Revisa el motivo”**; L10 is historical/expired on 2 October. No prior publication means no published menu, not a fallback success. Time passed with missing result uses **“Resultado desconocido”**.

**Actions / effect:** confirmed public source → JT-P01 and original O06; blocked target → JT-O06; known failure → JT-O04 with applicable time/scope checks; original unknown → JT-X02; scheduled cancellation → JT-O08. A successful result later superseded remains history, with **Ver publicación actual**, not old live preview. Reconcile any newer applicable live availability at execution; a current-service content publication preserves sold-out scope, while a new service uses JT-O14 without implicit available stock.

**Errors / recovery / check:** delayed/missed execution cannot backdate or auto-publish an expired menu; review current intent explicitly through JT-O04/JT-X04. Unverified original receipt/current source remains uncertain. Check J4.3: scheduled/failed/cancelled/superseded/live facts distinguishable and retry does not duplicate a conflicting publication.

### JT-O08: Cancel, replace or stop future occurrences

**Actor / objective / entry / version:** permitted schedule actor from JT-O05/JT-O06/JT-O07 reviews the original authorisation, actual outcome and exact future occurrences to cancel/replace. Cancellation is separate from withdrawing already public content.

**Composition / copy:** selected reference/date/target and consequences; **“Cancelar esta publicación programada”** or explicitly **“Detener las próximas publicaciones”**, retained past history and private source. Replacement shows old/new target/time/group. **“Esta publicación ya ocurrió; cancelarla no retira el contenido publicado”** when known.

**Actions / effect:** **Confirmar cancelación** → JT-O07 only when recorded cancelled; if original already published, inspect JT-P01 and use JT-O04 for an authorised corrective/withdrawal publication. Replacement requires known cancelled/superseded old intent and confirmed new authorisation via JT-O05, or an explicitly verified coherent replacement result; do not create the new conflicting schedule while the old outcome is unknown. Stop future recurrence does not erase completed occurrences.

**Errors / recovery / check:** cancellation/replace race, response lost or partial independent occurrence results → JT-X02; preserve each known outcome. Permission → JT-X03; changed reviewed plan → JT-X01. Check J4.3: no false cancelled label, retroactive history rewrite or implied deletion of the saved draft/public menu.

### JT-O09: Activate, end or correct a manual exception

**Actor / objective / entry / version:** authorised publisher reviews JT-O03 exception against current rules/offering/schedules. A service member's live availability permission does not imply permission to alter local/kitchen hours. Immediate urgent exception publication is explicitly selected through O05, separate from other editorial drafts.

**Composition / copy:** current rule → exception/effect/end → dependent offering/translation/schedule → public preview. T-C3-E confirms **“Horario especial · cocina de 13:30 a 15:30”**, local still 12:30–17:00; resolve matching validity. Temporary withdrawal distinguishes omitted current target from readable sold-out target. **“Al terminar, se revisarán las reglas vigentes; no se confirmarán existencias”**.

**Actions / effect:** **Publicar esta excepción** → original O05/result then JT-P01/JT-P02; **Finalizar o corregir excepción** → JT-O04 with current underlying rules and dependent selection, then known result. End/expiry re-evaluates applicable current normal/other exceptions; next-service stock → JT-O14. Expired old offer cannot reappear merely because exception ended. Unknown active rule → JT-X04/JT-X02.

**Errors / recovery / check:** overlap/current schedule dependency → JT-X01; failed/unknown publication/end → JT-X02; revoked access → JT-X03. Check J4.2/J5.3: explicit precedence/end/current-source recovery without silently opening another area, publishing D11 or restoring expired availability.

## 4. Operator states — urgent availability and recovery

### JT-O10: Scoped availability on mobile

**Actor / objective / entry / version:** actor authorised for current live availability enters from JT-O01/original O07 on a confirmed published item/context/service. Read current public revision and status; unrelated editorial drafts are outside the action.

**Composition / copy:** single-column venue/item/current service → current amount/format/status → **Marcar agotado / Confirmar disponible** → exact selected scope/end/review policy. C1: **“Croissant · Desayunos de hoy · hasta las 12:00”**; C3: **“Flan · comidas del 1 octubre · hasta las 15:30”**. **“Solo cambia la disponibilidad. D11 y los demás borradores seguirán privados”**. No required calendar wizard or photos for C1.

**Actions / effect:** **Confirmar este cambio** → JT-O12; **Cambiar varios elementos** → JT-O11; **Ver oferta publicada** → JT-P02. No available target → JT-O14/JT-O03 for preparation only. Result rechecks current service, item/format and permission; scope cannot silently expand between preview/confirm.

**Errors / recovery / check:** newer relevant status/removal → JT-X01; expiry → JT-X04/JT-O14; failed/unknown original operation → JT-X02; permission → JT-X03. Check J5.1/J5.2: current live scope only, pending food remains pending and no draft price/text publication.

### JT-O11: Review selected bulk availability groups

**Actor / objective / entry / version:** availability actor from JT-O10/CP-B01 selects current published items/context/format/services; use existing CP-B01–CP-B03 result groups, not a second bulk mechanism.

**Composition / copy:** explicit selected names/count, off-screen selections, context/date/format/current status/end, coherent groups and permission/conflict exclusions. T-C2 **“Agotar queso y vino · Terraza · servicio seleccionado”** only after actual service/end supplied; General unaffected unless expressly selected. Editorial CP price/order proposals stay private. Full common factual group cannot be split into inconsistent public uses.

**Actions / effect:** **Revisar cambios** → CP-B02 then **Confirmar disponibilidad** → CP-B03/JT-O12. Removing denied/conflicted groups generates a new preview; remaining unknown results are not retried with known successes. Switch to editorial editing → CP-B01 with separate review, no mixed action. Return JT-O10 retains deliberate selections only within permitted current scope.

**Errors / recovery / check:** no selection/unknown C2 scope/end blocks live confirmation, not guessed service; conflict → JT-X01; failed/partial/unknown → JT-X02 per group. Check J5.2/J4.1: no “Todo actualizado” with any unresolved group, no overlooked selected formats/areas or accidental public draft.

### JT-O12: Confirm availability result and current public effect

**Actor / objective / entry / version:** actor inspects original availability action and per-group result from JT-O10/JT-O11/JT-X02. Recorded success, current public source and later changes remain separately visible.

**Composition / copy:** confirmed T-C3-U **“Flan agotado · comidas del 1 octubre”**, L10a unchanged 16,50 €, D11 private; **Ver carta publicada / Revisar corrección**. Known failure **“No se ha cambiado la disponibilidad”** only if original no-effect confirmed. Partial groups show applied/not-applied/conflict/unknown counts and names, without invented operation outcome.

**Actions / effect:** original known result → JT-P02; **Revisar corrección** → JT-O13; uncertain → JT-X02; known not-applied → JT-O10/JT-O11 with fresh scope. Successful original action followed by another actor's status is history; display latest confirmed status and JT-X01 rather than advertising old sold-out as current.

**Errors / recovery / check:** public fetch unavailable after known action does not erase known success or verify current view; distinguish result from **“No podemos confirmar la carta actual”**. Permission/read loss → JT-X03. Check J5.1/J5.2: result routes by urgent action, never editorial publication; D11/croissant drafts unchanged.

### JT-O13: Review a scoped correction without losing later work

**Actor / objective / entry / version:** permitted availability corrector from JT-O12/history compares the selected known earlier action with latest current field/context/service. Read-only history is insufficient to correct.

**Composition / copy:** original before/after → latest status → proposed current correction and later unrelated changes. **“Se restaurará solo la disponibilidad de este elemento en este servicio”**. C3 no relevant conflict yields L10b; C2 later terrace price/translation changes stay untouched. Newer relevant availability/end/exception requires fresh review; no automatic winner.

**Actions / effect:** **Confirmar corrección** → JT-O12 after current permission/scope check; **Mantener estado actual** → JT-O01; relevant change → JT-X01; ended service/item withdrawn/private → JT-O14, not an old-snapshot restore. Editorial/history restoration instead uses JT-O15/JT-O04.

**Errors / recovery / check:** original result unknown → JT-X02 before deciding reversal; failed/unknown correction uses its own original operation, not assume rollback; permission → JT-X03. Check J5.4: preserve later authorised work, no expired target reactivation or collateral recipe/price/translation restoration.

### JT-O14: Review availability at the next applicable service

**Actor / objective / entry / version:** current-service actor from JT-O01/JT-O13/J9-M01 sees old temporary states/history and the current published applicable service. This is original X07 expansion, not an automatic daily stock reset.

**Composition / copy:** **Servicio anterior / Este servicio**, prior scope/end/chosen review policy and current targets. C3 **“Disponibilidad por confirmar”** for an applicable flan until deliberate action; future L11 may be readable planned without stock assurance. Private D11/no current publication → **“No hay una oferta publicada sobre la que cambiar disponibilidad”**. Removed identity/copy/format is not matched by name.

**Actions / effect:** deliberate **Confirmar disponible para este servicio / Marcar agotado para este servicio** → JT-O10/JT-O12. To keep an exception, explicitly select current applicable scope and review actual end/stop policy → JT-O03/JT-O09; prior exception is history, not new authorisation. Missing target → O03/JT-O04 preparation; return ordinary consultation → JT-P01.

**Errors / recovery / check:** unknown current source/time → JT-X04; relevant newer status → JT-X01; unknown result → JT-X02; authority loss → JT-X03. Check J5.3: availability, future publication and ending an exception are different facts; no service opening/restock or draft publication inferred.

### JT-O15: History and reviewed restoration of selected content

**Actor / objective / entry / version:** authorised history viewer from JT-O01/CP-B04 sees actual known actor/responsibility, action/field/scope/time/source/base/result; creates corrections only with proper edit/publication or availability authority. Fictional actor roles are not invented named employees.

**Composition / copy:** separate **Guardado de borrador / Publicación / Programación / Excepción / Disponibilidad**, known/unknown outcomes, supersession and current source comparison. **“Preparar corrección desde esta versión”**, not unconditional restore. Old L10/old translation remain historical; compare current recipe/format, food/nutrition/diet, language/relations, validity and output obligations.

**Actions / effect:** selected editorial restore → new private proposal via O02/CP-R02 → JT-O04/JT-O05, with dependent facts reviewed; urgent correction → JT-O13. Expired-menu reuse prepares a new dated reviewed proposal, never live old content. View result → JT-O07/JT-O12; reconcile uncertainty → JT-X02. History itself cannot rewrite measured digital events, transfer preferences or publish other drafts.

**Errors / recovery / check:** incomplete/inaccessible history explicitly pending/restricted, no assumed author or reconstructive equal-value success; source conflict → JT-X01; access → JT-X03. Check J5.4/J4.4: relevant field/responsibility traceable, allowed recovery preserves later work and reviewed coherent public source.

## 5. Public and exception states

### JT-P01: Read planned, current, closed or past offering

**Actor / objective / entry / version:** anonymous diner via presence/direct menu/PV-P03/JT-O07 reads actual published venue/context/date/service/language. Public offering/source and time/exception confirmation are distinct from private target and stock status.

**Composition / copy:** identity/context → published local/kitchen hours/exception → offering validity → applicable amount/inclusions/format/conditions → declared/pending food. Confirmed L11 at 12:30: **“Menú previsto para el 2 octubre · comidas de 13:00 a 15:30 · disponibilidad por confirmar”**, 17,50 €/person. T-C3-E at 13:15: local open/kitchen special 13:30–15:30, planned only. At 15:30 label service over; absent/failed L11 cannot show L10 current. Truly published general offering stays readable, never fabricated.

**Actions / effect:** **Ver otra carta o servicio** → PV-P04; detail → PV-P06; expired/removed target → PV-P11; contact staff via supplied destination only. These actions do not reserve, order, confirm availability or access private D11. Direct C1 entry remains short/account-free.

**Errors / recovery / check:** unconfirmed time/rule → JT-X04 with honest notice; offline → J10-P04 loaded coverage/time warning, unloaded absent; language → PV-P10 current source fallback; no prior publication → explicit absent offer. Check J4.2/J5.3/J1: readable planned/current/historical distinctions, no stock or fresh-status guarantee.

### JT-P02: Read a live change, withdrawal or recovery

**Actor / objective / entry / version:** diner already consulting detail/highlight/pairing/saved option receives confirmed newer public publication or current-state fetch failure. Reconcile actual selected context/service/format, retain reading intent and latest authorised public source.

**Composition / copy:** T-C3-U **“Flan · agotado en este servicio”**, same menu 16,50 € and milk/egg plus remaining pending; fruit stays a listed choice. Confirmed temporary removal omits target from current highlights/pairings and explains changed deep link. Restored status only for known current correction, not old service. **“La oferta de este servicio ha cambiado. Revisa las opciones actuales”** identifies actual changed values/status.

**Actions / effect:** applicable detail/return → PV-P06; relevant current menu → PV-P11/PV-P04; saved reconciliation → J10-P05. Directed pairing removal does not create inverse/substitute format; personal results → J15-P02/J15-P03 current checks without changing saved preferences. No local reading interaction writes restaurant drafts or private profiles.

**Errors / recovery / check:** old response/date/zone ignored as current and rechecked via PV-P11; offline → J10-P04, absent content absent; unattended display → J12-P02 withdrawing unconfirmed prices/availability. Generated paper/remote channel can remain stale; J9-M04/J14-O02 tracks them separately. Check J5.1/J5.4: availability and current food/context coherent across outputs, no fake universal refresh.

### JT-X01: Relevant source, schedule or live-status conflict

**Actor / objective / entry / version:** permitted actor encounters changed saved/current source, overlapping schedule/exception, or newer availability after preview. Separate local proposal, last confirmed saved revision, latest authorised current source and original operation result. Read only permitted data.

**Composition / copy:** **“Estos datos cambiaron después de tu revisión”**, specific before/current/proposed values, date/zone/format/field and affected uses; unrelated draft summary. C1 local coffee 2,00 € versus current saved 2,10 € follows original O02/CP-X01; C3 D11r1 versus r2/time exception requires new coherent selection. A later unrelated price is preserved, not a reason to overwrite everything.

**Actions / effect:** **Mantener estado actual** → JT-O01; **Revisar mi propuesta** → source O02/CP-X01 then JT-O04; schedule dependency → JT-O06; live correction → JT-O10/JT-O13 after current review. Known successful original operation remains history; exclude independent blocked groups only with fresh explicit remaining-scope preview.

**Errors / recovery / check:** unresolved common factual group blocks that group, not automatically all site content; missing current source → JT-X02/JT-X04; authority → JT-X03. Check J4.4/J5.2: no silent overwrite, automatic newest-draft win, guessed identities or loss of unrelated work.

### JT-X02: Failed or unknown original operation

**Actor / objective / entry / version:** authorised actor checks original save/schedule/execution/cancel/exception/availability/correction intent and per-group scope/base/result. Current visible field alone does not establish the original outcome; source access/result-read authority are independently checked.

**Composition / copy:** **“No hemos podido confirmar esta operación. Comprueba su estado antes de repetirla”**, exact action/reference/time/group and known result versus current public source/validity. Save unknown retains allowed local proposal distinct from confirmed draft. Known not-applied preserves prior known history and its actual expired/absent state; no “sigue vigente” by default. Partial groups are named without assumed global rollback.

**Actions / effect:** **Comprobar estado** → original CP-X02 result check, then confirmed save → O03/JT-O04; schedule creation/execution/cancel → JT-O07/JT-O08; exception → JT-O09; urgent/correction → JT-O12/JT-O13. Confirmed no-effect permits refreshed review/retry of only that group. Unknown stays here with authorised help/access-recovery route; never resubmit entire original action blindly. Latest changed source → JT-X01.

**Errors / recovery / check:** original result unreadable after revocation → JT-X03 with uncertainty retained, protected work hidden as required; late prior intent cannot replace current state. Check J4.3/J5.2 and G4-01 preservation: applied/lost acknowledgement, confirmed no-effect, concurrent newer revision and access loss remain distinct; no duplicate schedule/publication or collateral draft exposure.

### JT-X03: Denied or revoked action and source access

**Actor / objective / entry / version:** member lacks/loses action-specific edit/publish/schedule/availability/history/status-read or venue access before confirmation/recovery/execution. Prior opened view or delegated request never confers current authority.

**Composition / copy:** **“No tienes permiso para esta acción”** names allowed scope/action; permitted read-only current content is distinct from denied editing. Revoked venue access hides its private proposals/sources; **“Solicita acceso a la persona responsable del restaurante”** only suggests user action, not a sent message or available colleague. Original unknown cannot become known failure through access denial.

**Actions / effect:** permitted source read/status check → JT-X02; allowed content edit → O02 without publishing; availability-only member → JT-O10, not hours/D11; otherwise O01 authorised workspace/access recovery. Restore access requires latest-source/authority/intent review, not replay of an old pending confirmation. Retention/clearing of local work follows future authorised G3 contract; no promise to keep reading revoked content.

**Errors / recovery / check:** revoked schedule authority before execution is a required review/authority gate; if execution race/outcome cannot be established, remain unknown through JT-X02. Delegated per-assignment confirmation from J8-S07/ADR-0012 does not bypass publication permission or authorise changed scope. Check J4.1/J5.2: no staff access from guest session, restricted data export or false “nothing changed”.

### JT-X04: Uncertain time, expired scope or unavailable rules

**Actor / objective / entry / version:** actor/diner cannot establish current local time/applicable published rules or selected service expired/disappeared. Historical known result, current source and freshness are distinct.

**Composition / copy:** operator **“Revisa la fecha, la hora y la zona horaria”** with retained fields for past/non-unique/nonexistent local moment; **“Este servicio ya terminó; elige un servicio vigente”** when confirmed. Public **“No podemos confirmar el estado de este servicio. Consulta al personal”**; readable known published content labelled with scope/limits. A closed known service is different from unknown time/rules. No missing input becomes closed/open.

**Actions / effect:** permitted time/calendar correction → JT-O02/JT-O04/JT-O05; actual current availability → JT-O14; public current-target choice → PV-P11/PV-P04. Offline loaded reading → J10-P04 without current-stock assurance; screen unconfirmed → J12-P02. Missed expired schedule remains history; explicitly prepare new current/future target rather than replay late.

**Errors / recovery / check:** unresolved timezone change/overnight overlap/conflicting exceptions blocks affected confirmation, not hide current unaffected offering; no device-clock fallback or invented DST date/offset. Check J4.2/J4.3/J5.3: boundaries are explicit, expired service not reactivated and unknown rules never imply safe/current availability. G3 supplies actual time/freshness/execution proof.

## 6. Criterion and capability traceability

### Eight unchanged source criteria

| Criterion | Concrete states / transition and documentary check |
| --- | --- |
| J4.1 | JT-O04 → original O05/O06; JT-O09/JT-O11 coherent selected scope, excluded drafts and current authority; JT-X01/JT-X03 denial/review. TC01/TC02/TC13/TC22. |
| J4.2 | JT-O02/JT-O03/JT-O04 → JT-O05; JT-O06 changed target; JT-O09 exception → JT-P01; JT-X04 time/date/zone and conflict. TC03–TC08/TC14/TC28. |
| J4.3 | JT-O05 → JT-O07; JT-O08 cancellation/replacement; JT-X02 original known/unknown; JT-X04 expired/missed target. TC09–TC12/TC15/TC29. |
| J4.4 | JT-X01/JT-O06 compare local/confirmed/latest sources → JT-O04 new review; JT-O15 selected correction; CP original save/bulk retained. TC06/TC16/TC21/TC30. |
| J5.1 | JT-O10 → JT-O12 → JT-P02 and JT-O13; T-C3-U L10a only, D11 stays private. TC17/TC18. |
| J5.2 | JT-O10/JT-O11/JT-O12 → JT-X01/JT-X02/JT-X03 per action/group, not global success; original CP bulk/status routes. TC19–TC22/TC30. |
| J5.3 | JT-O14 review prior/end policy → JT-O10 current deliberate action; JT-O09 current-rule exception end → JT-P01; missing/private target stays absent. TC23/TC24/TC27. |
| J5.4 | JT-O15 new reviewed editorial proposal → JT-O04; JT-O13 scoped current correction preserves newer fields/dependencies; expired recovery → JT-O14/JT-X04. TC18/TC21/TC25/TC26. |

### Individual affected capabilities

These 20 contributions are not 20 finished software capabilities. The [single 72-parent map](m1-connected-journey.md#7-compact-coverage-and-remaining-work) keeps 36 included/30 configurable/six connection-dependent and S1/S2 separate; nothing is silently deferred.

| Capability | Contribution / remaining boundary |
| --- | --- |
| B1.02 | JT-O02/JT-O03/JT-O09/JT-P01 separate local/kitchen/exception visit facts; real source/time proof pending |
| B2.01 | JT-O04/JT-O10/JT-O14 preserve actual item/menu identity; no name-based substituted target |
| B2.02 | JT-O04/JT-O10/JT-O11 exact scoped formats, current amounts; inherited CP ambiguity unchanged |
| B2.03 | JT-O04/JT-P01/JT-P02 supplements/minima/units beside exact amount, not erased by timed change |
| B2.04 | JT-O05/JT-O07/JT-P01 composed menu price/inclusions/choices/validity; no order or stock guarantee |
| B2.05 | JT-O01/JT-P01 actual multiple offerings/fallback; C1 no compulsory extra menu setup |
| B2.06 | JT-O02/JT-O04/JT-O05/JT-O07/JT-X04 periods/publication time/zone/recurrence/current validity; executor contract pending |
| B2.07 | JT-O03/JT-O10/JT-O11 scoped location/zone, General versus terrace unchanged unless selected |
| B2.08 | JT-O10–JT-O14/JT-P02 urgent scoped status/undo/next-service review, real availability proof pending |
| B2.09 | JT-O03/JT-O09/JT-P01 exception scope/precedence/end/current-rule re-evaluation; technical proof pending |
| B4.03 | JT-O01/JT-O10/JT-O13 direct mobile service controls; rendered touch/focus/interaction pending |
| B4.04 | JT-O11/JT-X02 existing coherent bulk outcomes/retry, CP reuse/identity retained |
| B4.05 | JT-O02–JT-O06 private proposal/saved/current revisions and contextual labelled preview |
| B4.06 | JT-O04/JT-O09/JT-O12/JT-X02 exact authorised publication/result, no private draft side effect |
| B4.07 | JT-O05–JT-O08/JT-X01/JT-X02 scheduled/changed/cancelled/failed/superseded/live outcome, no blind duplicate |
| B4.08 | JT-O13/JT-O15 scoped history/current reviewed correction, no expired recipe/menu revival |
| B4.09 | JT-X03 action/source/status access independent, delegated assignment not permission |
| B4.11 | JT-O04/JT-O06/JT-O15 food/translation/diet/nutrition/relation dependency review, unchanged incomplete facts |
| B5.04 | JT-O04/JT-O09/JT-P01/JT-P02 prices/status/validity common across languages, not language copies |
| B7.07 | JT-O01/JT-O06/JT-O14/JT-X02 → J9-M01 actionable schedule/temporary/output work regardless of traffic |

Other affected public/food/output/offline/screen/connection/personalisation paths reuse PV/CP/J10–J15/J8–J9 coverage, not extra counted parents. Full maintained register/print/QR and visual expression remain separate next work.

### Connected reader walkthroughs

| Walkthrough | Reset branch / ordered path and consequence |
| --- | --- |
| TW01 | T-C1 JT-O01 → JT-O10 → JT-O12 → JT-P02 → JT-O13. No calendar configuration; croissant draft private; breakfast expiry then JT-O14, not old undo. |
| TW02 | T-C3-S O02/O03 → JT-O04/JT-O05 → JT-O07 → JT-P01. Private target before execution, confirmed L11 planned/current by time, no stock assurance; failure/unknown branch JT-X02. |
| TW03 | T-C3-S edit r2 or T-C3-E exception → JT-O06/JT-O03 → JT-X01 → JT-O04/JT-O05 or JT-O08 → JT-O07. Confirm actual old/new authorisation outcome, no silent rebinding or double publication. |
| TW04 | T-C2 JT-O11 → CP-B02/CP-B03 → JT-O12/JT-X02 per coherent group → JT-O13. Newer price/private drafts unchanged; known failure versus unknown/conflict explicit; no invented C2 service/end. |
| TW05 | T-C3-U end/current-next service JT-O14 → JT-O10/JT-O12; T-C3-F selected history JT-O15 → O02/O03 → JT-O04. New scope/action and food/language dependencies reviewed; no old availability/EN restoration. |
| TW06 | JT-O07/JT-O12 known public effect → JT-P01/JT-P02 → PV detail/deep-link/J10 reconnect/J12 display/J9-M04 outputs. One current coherent source, loaded snapshot labelled, paper/external/device status independent. |

## 7. Author contrasts and affected regression

All cases are readings of the descriptive transitions, not executed scheduling/stock/provider/participant tests. Reset the named fixture; unknown sources/declarations/destinations remain unknown.

| Case | Contrast | Required documentary result / actual proof still needed |
| --- | --- | --- |
| TC01 | C1 immediate coffee 2,00 € with croissant draft | JT-O04/JT-O05 selected coffee only; croissant draft and published pending food unchanged. Actual publication/permission pending. |
| TC02 | C2 ambiguous 24 / 34 or unresolved required common group | Original CP review blocks affected structure; JT-O04 can select independent reviewed scope only after new preview, no guessed formats. |
| TC03 | C3 12:15 publication versus 13:00 service/local12:30 | JT-O05/JT-O07/JT-P01 distinguish private schedule, published planned offering, current service and stock. Actual time executor pending. |
| TC04 | C3 local open/kitchen closed, 13:30 exception, end15:30 | JT-O03/JT-O09/JT-P01 explicit scope; 13:15 planned, 15:30 expired; local not closed by kitchen rule. |
| TC05 | Recurring service with no tomorrow's target/version | JT-O02/JT-O05/JT-O14 no daily content inheritance, new draft not authorised by weekly hours. Actual recurrence/authority pending. |
| TC06 | D11r1 authorised, local/saved D11r2 or shared ingredient change | JT-O06/JT-X01 original/latest/local/dependencies distinct; review gate proposed, not assumed pause; re-authorise coherent source explicitly. |
| TC07 | Competing normal/exception/zone and two conflicting schedules | JT-O03/JT-O04/JT-X01 list affected groups, resolve or explicitly exclude before confirmation; no hidden priority or new duplicate. |
| TC08 | Overnight/split periods and timezone edit | JT-O02/JT-X04 exact start/end days, independent periods/shift review; unknown/non-unique moment not auto-corrected. Real timezone evidence pending. |
| TC09 | Creation confirmed versus response lost | JT-O05/JT-O07/JT-X02 original action check before retry; confirmed schedule not public L11; no duplicate receipt inferred from equal time. |
| TC10 | Execution confirmed but later newer publication; urgent status newer than scheduled source | JT-O07 retains original outcome/history and latest current source; old success not current menu. Same-service content publication preserves latest applicable sold-out scope; new-service stock requires JT-O14. |
| TC11 | Execution confirmed not applied; L10 expired or no prior offer | JT-O07/JT-X02 preserve historical/absent publication, honest no-current daily menu; retry revalidates actual applicable intent. |
| TC12 | Cancel or replace racing execution | JT-O08/JT-X02 original cancelled/published/unknown distinct; cannot unpublish by cancel or authorise competing replacement blindly. |
| TC13 | Early explicit future-publication plus existing schedule | JT-O04/JT-O08 resolve old authorisation, known outcome before coherent new intent; early publication no stock guarantee or hidden second replacement. |
| TC14 | Exception remove/end after normal rules changed | JT-O09 re-evaluates latest normal/other applicable rules and dependencies; no old schedule/expired menu revival. |
| TC15 | Missed executor/late response beyond15:30 | JT-O07/JT-X04 no backdated expired publication; known history distinct, current/future authorised review required. |
| TC16 | Local proposal/current saved2,10 € versus uncertain save2,00 € | Original O02/CP-X01/CP-X02 retained through JT-X01/JT-X02; saved/result/public sources distinct, no quiet overwrite. |
| TC17 | C3 flan urgent with D11 price/text draft | JT-O10/JT-O12/JT-P02 L10a 16,50 €, declared milk/egg and pending remainder, D11 17,50 € private. |
| TC18 | No relevant undo conflict versus service expired/item withdrawn | JT-O13 scoped L10b only while current; expiry/withdrawal → JT-O14, never old whole-menu restore. |
| TC19 | Bulk terrace/current formats with General or off-screen selection | JT-O11/CP preview exact actual identities/scope/end, independent context unchanged; no guessed C2 service or selected format. |
| TC20 | Known partial bulk result versus unknown group | JT-O12/JT-X02 per coherent group, known success kept, only known no-effect re-reviewed; no aggregate success/blind repeat/assumed rollback. |
| TC21 | Newer relevant stock status versus unrelated later terrace price | JT-O13/JT-X01 status conflict explicitly reviewed; later price/translation preserved, no forced old snapshot. |
| TC22 | Availability-only member/editor/publisher; revoked source/status access | JT-X03 distinct authorities, private sources hidden, unknown action stays unknown; no false no-effect or diner→staff privilege. |
| TC23 | Old sold-out at new service versus explicitly retained exception | JT-O14 names previous/current/end/policy; operator reviews current exception/action; no automatic available/old status transfer. |
| TC24 | Next service private D11/absent format/withdrawn/copied same name | JT-O14 no live target, original identities preserved; preparation separate, no side-effect publication or name-based stock carry. |
| TC25 | Selected historical recipe/translation/content restore | JT-O15/JT-O04 current food/diet/nutrition/translation dependency review, T-C3-F milk retained; no stale old EN/absence claim. |
| TC26 | Old paper/new generated file/unknown screen/external channel | JT-P02 → J9-M04/J12-O02/J14-O02 distinct evidence; unconfirmed screen hides prices/status, no universal output update. |
| TC27 | Diner offline loaded planned/sold-out versus unloaded future menu | J10-P04 warning/age/coverage, private D11 absent; reconnect coherent current scope; no private preferences offline. |
| TC28 | Viewer clock/venue timezone or applicable rules unknown | JT-X04 unknown distinct from closed/open; retained labelled source, no local-device inference or fabricated current price/stock. |
| TC29 | Recurring stop with completed/pending/unknown occurrences | JT-O08 per occurrence history preserved and actual stopped state checked; past live content not deleted or future work silently assumed cancelled. |
| TC30 | Late result after context/service/actor/source or permission changes | JT-X01/JT-X02/JT-X03 current intent gate; old operation history separate, no view overwrite, restricted data disclosure or retry with old authority. |

**Regression reading:** re-read all 122 unchanged earlier V01–V16, Q01–Q20, PC01–PC24, DS01–DS04, SC01–SC26, LC01–LC06 and VC01–VC26 against affected JT paths. Preserve every row and card body at baseline 9cfe77b. V temporal/private/urgent/food/print rules and DS original-save recovery remain; Q/LC preference identity/diet/privacy, loaded snapshot/display/connection/measurement limits remain; PC shared/copy/bulk/glossary source review remains; SC actual authority/support/export/maintenance/history/outcomes and VC public intent/context/food/directed relationship/late-response constraints remain. Reading is author evidence only, not retroactive independent approval.

### Author refinements before handover

| Refinement | Actual first-draft gap / correction and evidence |
| --- | --- |
| TF01 | First structural check found five paraphrased CP/PV/J9 heading fragments. Replace them with actual source headings and rerun the complete linked-document check. |
| TF02 | Schedule/current-source rules did not explicitly state the effect of an urgent status newer than a scheduled content snapshot. Add same-service availability preservation and deliberate new-service review in section 2/JT-O07/TC10; no scheduled restock. |
| TF03 | Destination checking found ambiguous shorthand state references. Qualify JT/CP/PV/J10 destinations throughout and name actual display/connection states in TC26. The original O04 preview remains a defined annotated source state, not a new JT card. |

These are author drafting corrections, not independent findings or executed time/stock tests. The dated external record retains initial failures and subsequent bounded verification.

## 8. Dependencies, completion boundary and next order

| Responsible contribution | Pending input / effect on closure |
| --- | --- |
| G1 with G3 | Settle proposed scheduling/private-versus-planned intent, reviewed exact targets/groups, recurring occurrences/end, exception precedence and new-source/timezone review; no accepted ADR changed. |
| G3 under #4 | Actual saved/current/operation correlation, consistent authorisation/execution/cancellation/supersession, simultaneous dependency/status changes, per-group atomicity, current authority/revocation, time/DST/overnight/freshness and missed-execution behavior. These are required observable design contracts, not implemented guarantees or APIs. |
| G5 with G2 | Actual regular local/kitchen/offering periods, one-date exceptions/end/restoration policy, responsible action/source and real content; train short C1/current-service path and escalation. No media/rights, legal compliance or staff availability is invented. |
| G4 independent | Bounded immutable-commit review of JT-O02–JT-O09/JT-O10–JT-O15/JT-X01–JT-X04 and TC01–TC30; separate from ongoing J8/J9 and PV review, incorporating actual returned findings later. |
| G2/G4 with authorised real operators/diners/devices | Rendered mobile date/scope/errors, keyboard/focus/reflow/read order, actual time boundary/parallel-edit/recovery comprehension, screen and placed-paper behavior. Fictional reading cannot prove these. |

**Descriptive completion:** 21 state cards, eight exact-source criterion mappings, 20 individual affected capability rows, six walkthroughs and 30 documentary contrasts, connected to previous source/public/output recovery. Author verification covers identifiers/fields/links/destinations/versions/coverage and 122 prior contrasts with limits; no software suites. G2 corrects actual findings and supplies an immutable commit for independent review. Completion of documents does not close #5, M1, technical contracts or original interaction/visual/real-input obligations.

**Executed author checks:** 431 local/internal link occurrences in 16 linked documents, valid fragments/unique headings/balanced fences/table widths, 21 unique JT cards with required fields/defined inherited destinations, eight exact-source criteria, 20 capability rows and six TW/30 TC. Preserve all 122 previous contrast rows and previous state cards at 9cfe77b; original criteria/matrix/definition/ADR-0005 and 0008–0012 unchanged, 72 parents once/S1/S2 separate. Prior PV, C1–C3, extended and scoped J15 integrity checkers also pass. Their dated pending-review text is historical; actual bounded independent returns above establish current review status. TF01–TF03 corrections are author findings only. Final whitespace/staged/author/commit/push/PR readback evidence is recorded outside Git after success, not inferred here. No software suites or actual time/stock/device/participant test.

**Next descriptive block:** J6–J7 maintained food register/staff and menu/print/QR outputs, preserving actual declared/pending source and generated-versus-placed state. Template/bespoke visual expression, accessibility rendering, interaction/participants and independent/technical/material evidence accompany all blocks; the unique 72-capability map/S1/S2 remains the governing inventory. Continue existing branch/draft PR #21; no merge or milestone closure authorised.
