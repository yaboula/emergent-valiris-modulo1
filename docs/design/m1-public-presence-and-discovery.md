# M1 public presence and discovery — J1–J2

2 October 2026 · G2 Product Design · Accountable consolidator: Product Designer · [M1 #5](https://github.com/yaboula/valiris-restaurants/issues/5) · Draft PR #21.

**Status: complete reviewable descriptive proposal, with author documentary checks recorded below; independent acceptance, rendered interaction and real inputs remain pending.** Document links navigate descriptions, not working product actions. This package adds 17 PV state cards to [C1–C3](m1-connected-journey.md), [content preparation](m1-content-preparation.md), [J10–J15](m1-extended-journeys.md) and [J8/J9](m1-service-and-maintenance.md). No software, live restaurant, QR, destination, mail, measurement, media rights or participant operation is supplied.

## 1. Authority, choices and fictional branches

Use the [roadmap](../project/roadmap.md), [briefs](../product/m1-design-briefs.md), [criteria](../product/m0-journeys-and-criteria.md), [matrix](../product/m0-capability-matrix.md), [original functional definition](../research/storefront-digital-menu/functional-definition/functional-definition.es.md), [closeout](../project/m0-closeout.md) and accepted [language decision](../adr/0005-repository-and-product-language.md), [launch commitment](../adr/0008-first-launch-capability-commitment.md) and [studio/account direction](../adr/0009-studio-design-and-registered-diner-personalisation.md). Common context/protocol/instructions were read previously and reused; relevant public/editorial/consultation source sections were inspected for this delivery. Baseline `2eb8e86` was clean/synchronised; PR #21 OPEN/draft and #5 OPEN were checked before editing.

| Decision / status | Visible consequence |
| --- | --- |
| Owner-selected Markdown; no active Figma work | Describe composition, copy, actions and recovery. Links do not prove interaction. |
| Owner-selected directed pairings, confirmed during this block's planning | A dish → wine relation does not imply wine → dish. A reverse relation needs an explicit separate edit/review/publication. |
| Accepted venue content autonomy and studio-controlled composition | Operators maintain visit/editorial/highlight/relation content in both template and bespoke designs; no page builder or new design purchase for routine edits. |
| Accepted anonymous consultation; venue editorial recommendations separate from J15 | No registration, profile, taste inference or personal diet matching is required for highlights/pairings. |
| Proposed operational contracts in this document | Coherent source/relationship/context, translation effects and original-action recovery need G3/G1 review in M2/#4; no API or storage choice is made. |

The directed-pairing choice is recorded here as an explicit founder input. Existing accepted ADRs are preserved; the operational descriptions do not retrospectively rewrite their decisions.

**Independent review continuity:** the external immutable G4/G1 result under `research-evidence/reviews/j15-recheck-2eb8e86` resolves documentary G4-J15-01 on `2eb8e86831c4c00315078b5442e20fc5273150c9`. The earlier G4-01 save-recovery finding remains separately resolved. Read the consolidated result and focused G4 evidence; neither reviews this new PV package, whole CP or J8/J9. Reports/snapshots and their dated limits are now versioned in root `research-evidence/` byte-for-byte (3 October storage migration). No specialist or external thread communication is activated here.

**Review received during final delivery:** the separate external consolidated G1/G4 result under `research-evidence/reviews/cp-2eb8e86` now records CP preparation/maintenance reviewed documentarily on 2eb8e86 without required correction in the bounded written branches. This supersedes its former pending-review status in the block map, not the old author/history records. CP technical/real/visual/interaction evidence remains pending; this review covers neither PV nor J8/J9. Its reports/snapshots are preserved.

**Fixture reuse:** all examples are fictional C1 Café Linde, C2 Mesa del Patio and C3 Casa del Mediodía. Reuse their exact prices, food facts and frozen 1–2 October Europe/Madrid dates. C1 coffee starts at 1,90 €; its separately reviewed 2,00 € branch never exposes the croissant draft. C2 terrace cheese media/completa 26,00 €/36,00 €, extra bread +2,20 €; general 24,00 €/34,00 €, extra +2,00 €. Rice is 19,50 €/18,00 € per person, minimum two; fish 7,00 €/6,50 € per 100 g, actual weight/total unconfirmed. House wine copa/botella is 3,80 €/21,00 € terrace or 3,50 €/19,00 € general, sulphites declared, remaining food information pending. Cheese retains declared milk/wheat. Do not infer dietary suitability from a name or editorial relationship.

C3 local 12:30–17:00 and kitchen 13:00–15:30 are separate. A 12:45 branch shows local open/kitchen not yet serving; a pre-12:30 branch shows local closed with the actually published L10 planned for that date's lunch. L10 is 16,50 € per person, inclusions and coffee +1,50 € unchanged; D11 17,50 € stays private except its independently authorised existing branch. An exception branch is explicitly conditional **[reviewed published exception, scope/end]**, not an invented actual closure. A conflicting/unconfirmed exception cannot produce a confident open/closed claim.

Additional labels are hypothetical design references, not asserted stored revisions: `VP1` means a confirmed public venue-information snapshot with supplied facts and missing fields visible; `VE1` a separately reviewed optional editorial proposal; `VR1` the proposed directed C2 cheese → house-wine **bottle** relation, with supplied fictional text **“El restaurante propone acompañar la tabla con su vino de la casa”**; `VR2` its deliberate revised proposal. In VR1 the hypothetical editor deliberately selects both general and terrace placements and both cheese formats, each pointing to the corresponding published wine bottle; none is inherited merely by sharing a product identity. No wine expertise or real restaurant endorsement is claimed. Reset branches before each walkthrough/case; do not combine contradictory histories.

Address/contact/owned URL/external destination, actual venue attributes, story, logo/photos/rights and other-language editorial material remain **[pending authorised input]**. Bracketed fields describe required input, never fake actionable production values. Empty materials do not require fabricated history/photos or block C1 menu reading. A hypothetical real configured destination must be supplied before testing its action.

## 2. Shared interface and composition contracts

PV-P IDs are public, PV-O operator, PV-X recovery. Bare O/P/X destinations refer to the original connected package; extended J IDs and CP IDs remain fully qualified. Every card states actor/objective/entry/version, composition/copy, actions/effect and errors/recovery/check. Physical QR/print composition is continued in J7, not generated here.

| Conceptual interface | Meaning to preserve / technical review |
| --- | --- |
| Venue-information snapshot | Correct venue/location, published address/contact, distinct local/kitchen hours and applicable exception scope/end, declarations/limits, language review and coherent reference. Unknown is distinct from closed or absent. |
| Published offering and reading intent | Venue, menu/item identity, placement, area, service/date/validity, format/unit/conditions, food state, language/fallback and publication reference; retain appropriate category/query/filter/detail return position. |
| Editorial highlight or directed relation | Published source identity and target identity within the venue, applicable contexts/formats, reviewed text/language, order and reference; current amounts/status come from the matching offer, not copied editorial values. |
| Shared-link representation | Public target/intent/context/language, published title/summary and permitted image if supplied; public preview distinct from external cached copy and from actual target resolution. No private account/preferences/token/draft data. |
| Content operation | Actor authority, original action, permitted scope, confirmed base/current revision, local proposal and known/failed/unknown outcome. Equal displayed values alone do not prove the original action saved. |

Do not imply that all content shares one storage version. Confirm the compatible published venue/offer/editorial references needed by the view; never mix draft/new context prices with old relationship text as though one current result. G3 specifies version/identity/freshness/enforcement in #4. No TTL, schema, URL syntax, search algorithm, ranking model or crawler policy is selected.

**Late public response:** resolve the currently intended venue, entry/target, area/service/date, format, language and compatible published references before replacing a public view. A response for the previous area/language or a retired target cannot overwrite the newer selection, even when names match. Unknown currency keeps the uncertainty/historical state, not falsely current cards. Public target resolution never restores signed-out/other-user private state; J15's restrictions remain in force independently.

Public composition: venue identity accompanies both entry routes; essential price/format/condition remains readable before expanded detail. Editorial sections do not interpose before direct menu entry. Mobile order is identity/context → essential task → optional detail; long names wrap and text/colour-independent state labels remain visible. Label language controls, search/filter state, external exits and back destinations; describe focus return to the opening control/list item, announcements after context/results changes, and recoverable field errors. ES/EN/FR/DE interface intentions and reviewed source-language fallback follow ADR-0005; Arabic/RTL is preparation, not a supplied translated or tested interface. Rendered accessibility, typography, reflow and device checks remain pending.

## 3. Public states before and during the visit

### PV-P01: Recognise the venue and choose the task

**Actor / objective / entry / version:** anonymous visitor from a venue/discovery/shared presence entry, correct venue/location and confirmed VP1; recognise the business and choose visit information or menu. Direct-menu intent enters PV-P04 instead.

**Composition / copy:** name **“Café Linde”**, supplied public concept if available, **Ver carta**, **Información para visitar**, then optional reviewed story/highlights. No hero image, gallery, story or account is required. Missing logo uses readable venue name, not an invented brand asset.

**Actions / effect:** **Ver carta** → [PV-P04](#pv-p04-direct-menu-and-context-entry); visit → PV-P02; optional editorial reading stays here with explicit return to the task; highlights → PV-P07. All use public sources; no private profile or write.

**Errors / recovery / check:** venue mismatch/unconfirmed identity → PV-P11, not another restaurant's familiar name. Missing optional material is omitted, missing essential information labelled. Check J1.1/J2.1: C1 menu remains reachable without promotion, sign-in or elaborate setup.

### PV-P02: Visit information and declared attributes

**Actor / objective / entry / version:** visitor from PV-P01 or menu's venue-information link; VP1 for the same location, confirmed publication/language. Decide whether/how to contact or visit.

**Composition / copy:** readable supplied address → separate **“Horario del local”** / **“Horario de cocina”** → applicable published exceptions/conditions → contact/map/reservation destination → optional declared attributes with exact detail. Unknown fields say **“Información pendiente. Consulta al local”**; a generic accessibility/terrace label does not establish an accessible route or current seating availability. Missing input is not a negative facility claim.

**Actions / effect:** **Ver carta** → PV-P04; opening/closed interpretation → PV-P03. **Abrir mapa**, **Llamar al local**, configured **Ir al sitio de reservas** each explain the actual supplied external destination/system action before exit; booking follows [J14-C01](m1-extended-journeys.md#j14-c01-booking-destination), without a confirmed reservation. A supplied phone/address can remain readable when device handoff fails; no external result is observed from a click alone.

**Errors / recovery / check:** missing/malformed/unconfirmed destination has a labelled unavailable action and PV-P11 recovery, no fabricated number/link/map pin. Return preserves venue/context/language. Check J1.1/J1.4: local and kitchen hours/unknowns, conditions and link outcome remain distinguishable.

### PV-P03: Closed venue kitchen and planned consultation

**Actor / objective / entry / version:** visitor needs offering before service, or PV-P02/PV-P04 detects a boundary. Confirm venue-local time, published hours/exception and relevant offer validity; use labelled fictional clock, not the reader's current date.

**Composition / copy:** separate **“Local abierto · Cocina abre a las 13:00”** for C3 12:45, or **“Local cerrado ahora”** when established, beside **“Oferta publicada para comidas del 1 de octubre · 13:00–15:30”** and stock unconfirmed. Published exception displays its exact scope/end and overrides ordinary hours only within that scope. Distinguish **“Todavía no hay menú del día publicado”** from an expired published menu and from unknown status.

**Actions / effect:** **Ver oferta publicada** → PV-P04 for actual general/planned offering; **Información para visitar** → PV-P02; absent daily menu offers any actually published general menu. No D11 entry, service booking or stock assurance follows.

**Errors / recovery / check:** conflicting references, uncertain local time/exception or unavailable refresh → PV-P11 **“No podemos confirmar el servicio actual”**; historical loaded content follows J10, never a fabricated live state. Check J1.2: useful consultation while closed/planned; scheduling controls remain [X06](m1-connected-journey.md#x06-scheduling-and-manual-exception) for the later calendar block.

### PV-P04: Direct menu and context entry

**Actor / objective / entry / version:** anonymous direct link/QR/menu visitor or PV-P01 action. Resolve public venue, menu identity, context/date and coherent offer; no physical QR is produced or scanned in this design.

**Composition / copy:** identity then C1 short sections; C2 generic entry **“Elige la carta: General / Terraza”**, context-specific entry **“Carta de terraza · Cambiar”**. C3 shows full date/service/16,50 € per-person price, choices, bread/water inclusion and coffee +1,50 €. Photos, accounts and optional editorial content are not gates.

**Actions / effect:** current menu → PV-P05, detail → PV-P06, venue info → PV-P02. Context change reviews actual formats/prices/conditions and retains selected item only if applicable; missing format asks explicit reselection, never silently adopts another size. J10 comparison follows its existing reconciliation.

**Errors / recovery / check:** wrong/unavailable/expired context → PV-P11 with named alternatives, not assumed seating; source not loaded → J10-P04. Planned/closed → PV-P03. Check J2.1/J2.2: valid context-specific entry and simple C1 without unnecessary chooser/configuration.

### PV-P05: Browse search and explicitly scoped filters

**Actor / objective / entry / version:** diner in confirmed PV-P04 context; choose through current reviewed visible categories/names/descriptions. Reading state records public category/query/filter/position, not diner identity/preferences.

**Composition / copy:** category navigation and sections; C1's short menu may omit search/filter. C2 **“Buscar en esta carta”**, active criteria/result state and **Restablecer filtros**. Query **vino** matches six supplied wine entries; **Merlot** has no fixture match and says **“No encontramos resultados para «Merlot»”** with revise/reset. Use actually displayed reviewed/fallback language text, not invisible stale translations.

**Actions / effect:** detail → PV-P06; highlights → PV-P07; change query/clear filters stays here, preserving same context/language. Explicit venue-declared dimensions may be selected, without inventing spice/format attributes. **Excluir productos con leche declarada** excludes known milk, then separately labels the insufficient-information group **“Información incompleta: consulta al personal”** within the filtered result; never calls it safe. **Ver carta completa** restores ordinary reading.

**Errors / recovery / check:** changed category/query result reconciles current offering and explains loss of a reading anchor; only a same confirmed category identity retains navigation, not a similarly named replacement. Unknown source/loading → PV-P11/J10-P04, not empty-results fiction. Check J2.3/J2.4 and [X05](m1-connected-journey.md#x05-context-search-and-food-filter); this public filter never edits J15 saved tastes.

### PV-P06: Detail and return to the choice

**Actor / objective / entry / version:** diner opens exact published item/format from PV-P05/PV-P07/PV-P08 or resolved deep link. Context/offer reference travels with the detail; preserve originating view and public reading position.

**Composition / copy:** full wrapping name → actual format/amount/unit → supplements/minimum/weight condition → concise supplied explanation → known food declarations and remaining pending information → optional reviewed media/nutrition/editorial relation. Rice remains per person/minimum two; fish per 100 g cannot become an invented final price. Cheese shows milk/wheat; wine sulphites plus remaining pending, independently of pairing.

**Actions / effect:** **Volver a la carta** returns to PV-P05 or the actual named origin PV-P07/PV-P08; if origin anchor vanished, explain and offer the nearest relevant current section without showing old content as current. **Recomendación del restaurante** → PV-P08; share → PV-P09; nutrition/video → existing J11-P01/J10-P03 when corresponding content exists; anonymous comparison → J10-P01.

**Errors / recovery / check:** sold-out retains known scope **“Agotado en este servicio”** and readable current essentials, not an order action. Removed/expired item/format → PV-P11. Context/language change → PV-P04/PV-P10 with coherent new facts. Check J1.3/J2.5: essential conditions are never hidden behind explanation/media, and return orientation remains explicit.

### PV-P07: Venue-selected highlights

**Actor / objective / entry / version:** anonymous diner sees reviewed current-venue highlights from PV-P01/PV-P05; published editorial selection and corresponding offer/context references, not traffic scores or a private preference profile.

**Composition / copy:** **“Recomendaciones del restaurante”**, supplied editorial labels/explanation, exact relevant format/price/conditions and declared/pending food state, venue-chosen order. No **más vendido**, scarcity or dietary/safety assertion is inferred. Empty configuration omits this section while keeping the full menu.

**Actions / effect:** **Ver detalle** → PV-P06; **Ver toda la carta** → PV-P05 same context. No mandatory promotion or automatic reordered catalogue. Choosing a highlight neither registers a diner nor adds an order.

**Errors / recovery / check:** sold-out selected item is visibly unavailable and ceases to be presented as an available choice; readable detail may remain in its published scope. Withdrawn/incompatible item is excluded from current highlight destinations, with labelled empty/change notice if the section has no current entries. Refresh uncertainty → PV-P11/J10 snapshot rules. Check B3.07/J2.1: editorial value without blocked consultation or fabricated popularity.

### PV-P08: Directed pairings with current contextual targets

**Actor / objective / entry / version:** anonymous diner from a valid source detail, published VR1 and compatible current source/target placements in the same venue. Inspect an explicit venue recommendation, not an individual profile or combined deal.

**Composition / copy:** **“Recomendación del restaurante”**, supplied relation explanation, exact target wine **botella** and its current price/food/conditions. Terrace VR1 shows cheese's own media/completa 26,00 €/36,00 € and wine bottle 21,00 € separately; general, if explicitly applicable, uses 24,00 €/34,00 € and 19,00 €. No summed bundle price, cup assumption, included wine or dietary classification. Unreviewed relation language uses marked reviewed-source fallback only when faithful.

**Actions / effect:** **Ver vino recomendado** → PV-P06 for the exact target format/context; return → PV-P08/source detail with source anchor. Opening wine does not show an inverse cheese relation unless separately created/reviewed/published. **Ver toda la carta** → PV-P05. No account, automatic saved choice, order or price/status mutation.

**Errors / recovery / check:** sold-out target is labelled **“El vino recomendado está agotado en este servicio”**, not an available choice; current readable detail can be inspected. Withdrawn target/format or incompatible context is removed from current destinations with **“Esta recomendación ya no está disponible en esta carta”** and menu/source recovery. Source retirement → PV-P11. Relevant changed recipe/text/translation cannot retain a misleading old explanation: use reviewed fallback or withhold that affected relation; unaffected recommendations stay usable. Unknown freshness → PV-P11/J10-P04 with historical limit. Check B3.10/J1.3/J2.5: direction, identity, current facts and independent food limits.

### PV-P09: Share and resolve a public target

**Actor / objective / entry / version:** visitor shares presence/menu/item from PV-P01/PV-P04/PV-P06; public target identity/intent, explicit context/language and compatible published representation. Real owned destination remains pending input.

**Composition / copy:** target summary/title, public context and **“Compartir enlace”** / **“Copiar enlace”** only when an actual configured public URL exists. Optional permitted image has source/rights; otherwise readable title/summary suffices. Never include private profile, draft reference, credential or staff-session data in public preview.

**Actions / effect:** share/copy hands off the supplied public link; a known clipboard result may say **“Enlace copiado”**, not after failure/uncertainty. Recipient resolution goes to PV-P01/PV-P04/PV-P06 according to intent; invalid/withdrawn target → PV-P11, never compulsory homepage redirection. Closing/cancelling device sharing returns to origin; it is not a booking/visit confirmation.

**Errors / recovery / check:** unsupported share uses readable/copyable actual URL; denied clipboard explains **“No hemos podido copiar el enlace”** and manual copy. Missing configured URL says **“Enlace público pendiente de configurar”**, not fake success. External cached title/image may remain stale; opening the link checks current public source and never resurrects cached withdrawn offer/price. Check J1.5/B1.08/B3.08/B6.01: stable target intent across edits, not guaranteed external-cache refresh.

### PV-P10: Language and factual fallback

**Actor / objective / entry / version:** public visitor changes interface/content language from any public PV card; preserve venue/context/service/item/query/filter intent and reconcile actual reviewed language coverage.

**Composition / copy:** labelled ES/EN/FR/DE controls, actual content language and notice **“Este contenido se muestra en español mientras revisamos la traducción”** when applicable. Changed ingredient/condition/venue-hours facts cannot leave an old factual translation appearing current. Names remain faithful; price/status/validity are common sources, not edited language copies.

**Actions / effect:** change returns to the same valid originating PV card, reruns search against displayed reviewed/fallback text and announces resulting context/result changes. No counterpart → readable reviewed source plus notice, or withhold the affected assertion/relation when that fallback would mislead; **Ver carta** → PV-P04. It never silently changes area or resets saved private preferences.

**Errors / recovery / check:** failed language fetch keeps labelled known content, not a fabricated translation; partial offline coverage → [J10-P04](m1-extended-journeys.md#j10-p04-loaded-public-snapshot). Unknown current reference → PV-P11. Check J1.4/J2.3: context, food limits, essential amounts/conditions and navigation persist; no actual translator or four-language content completion is claimed.

### PV-P11: Unavailable changed or unconfirmed public target

**Actor / objective / entry / version:** anonymous visitor encounters retired/expired/wrong-context target, unconfirmed venue/offer/exception, empty published daily menu or failure. Identify the reason using known public evidence; unknown result/source is not absence.

**Composition / copy:** correct known venue/context → specific reason: **“Esta carta ya no está vigente”**, **“Este producto ya no está publicado en esta carta”**, **“Todavía no hay menú del día publicado”** or **“No podemos confirmar la información actual”**. Do not display withdrawn/expired price as current. Missing input is labelled without publishing bracketed fake destinations.

**Actions / effect:** **Ver carta actual** → PV-P04 only if a current appropriate menu is known; **Ver información del local** → PV-P02; **Cambiar carta** → valid named contexts in PV-P04; **Reintentar** checks the same target/current references, not guessed replacements. Preserve public intent, no private/admin recovery link.

**Errors / recovery / check:** no loaded content → [J10-P04](m1-extended-journeys.md#j10-p04-loaded-public-snapshot) honest unavailable state; loaded snapshot remains historical with coverage/time and food limits. Known coherent reconnect follows J10-P05 then the relevant PV card; connectivity alone does not certify currency. Unknown/unavailable external destination retains applicable readable supplied info and a return, no false provider failure/success. Check J1.5/J2.5/J2.6 and [X04](m1-connected-journey.md#x04-expired-target-and-language-recovery).

## 4. Maintain the public experience without a page builder

### PV-O01: Maintain visit facts and declared attributes

**Actor / objective / entry / version:** editor with venue/location content authority from [O02](m1-connected-journey.md#o02-content-editor), confirmed VP1 versus local proposal. Maintain address/contact/local and kitchen hours and supplied facility detail in both presentation routes.

**Composition / copy:** **“Información para visitar”**, separate source fields, missing/declared states, actual external targets, ordinary published hours and exception summary. Attributes require restaurant-supplied explanation; do not offer a certified-accessibility badge from a generic checkbox. Relevant factual language/shared-field effects and dependent link/preview/output uses appear before review.

**Actions / effect:** **Guardar borrador** → PV-O05, **Cancelar** retains known saved/published state; examine public visit preview → PV-P02/PV-P03 explicitly labelled private preview. Edit calendar/exception through existing X06, without implementing the later full calendar flow here. Save does not publish or reset stock.

**Errors / recovery / check:** ambiguous address/phone/destination is an explicit review issue, not guessed correction. Changed factual translation needs review/fallback. Conflict/save unknown/access loss → PV-X01. Check J1.1/J1.4: no duplicate public fact source or automatic push to external channels from a side action.

### PV-O02: Maintain optional editorial text and authorised media

**Actor / objective / entry / version:** authorised venue content editor from O02, published editorial base versus VE1 local/private proposal; maintain authentic supplied presentation/story/team/product/news/event information.

**Composition / copy:** **“Presentación e historia”**, factual text, optional appropriate content sections, source/rights/review fields for supplied media, language/validity where relevant and original versus proposal. Missing materials say **“Añade contenido cuando dispongas de material autorizado”**; no fabricated story, provider, team, photo or event/date. No independent publishing platform, compulsory article taxonomy or free layout editor.

**Actions / effect:** save → PV-O05; optional description/translation/faithful-image assistance → existing CP-A01–CP-A03 with accept/edit/reject and draft-only effect; remove proposal/review public removal → PV-O05. Public/readable preview PV-P01/PV-P10 remains clearly **“Vista previa · no publicada”**. Template/bespoke share maintenance controls.

**Errors / recovery / check:** absent image authorisation blocks the affected media use, not text/menu; unsupported assistance preserves original/manual path. Factual changes flag affected translations/preview. PV-X01 handles denied/conflicting/unknown save. Check B1.04/B1.05: useful no-photo expression without fabricated assets or claimed visual execution.

### PV-O03: Maintain highlights and directed relations

**Actor / objective / entry / version:** authorised content editor from item/menu O02 or existing CP source review, current published highlight/relation base versus private VR1/VR2. Same restaurant only, actual source/target identities and placements; shared versus independent copy remains explicit.

**Composition / copy:** **“Destacados y recomendaciones”**, choose source/destination identity, applicable context/format/service, reviewed explanation/language, manual order and **“Esta relación se muestra desde el plato. No crea la relación inversa”**. Show shared uses and separate contextual amounts/status. A relation does not inherit placement/context, allergen/diet facts, stock or publication rights. If a specific format is mentioned, select that exact format; otherwise an explicit product-level relation displays applicable published formats without guessing a preferred size.

**Actions / effect:** **Guardar recomendación en borrador** → PV-O05; **Crear relación inversa** prepares a separate explicitly reviewed proposal with its own text/applicability, never instant reciprocal publication. Reorder/remove highlight/relation → private proposal then PV-O05. Inspect affected shared uses → [CP-S02](m1-content-preparation.md#cp-s02-review-a-shared-change); independent-copy target is a different identity, never remapped by name.

**Errors / recovery / check:** missing/retired/private target or incompatible/ambiguous context blocks claiming a current publishable recommendation; revise target/scope or explicitly select a coherent group including required reviewed item publication. No secondary save publishes a target draft. Price change alone reads the new contextual amount on coherent refresh; changed meaning/recipe/format/explanation flags factual text, food/diet/nutrition/translation/output dependencies for their own review, never infers new declarations. Unknown currency or permission/conflict → PV-X01. Check B3.07/B3.10: both directions and affected contexts are deliberate; current unreviewed misleading relation is withheld through existing dependency policy, not silently rewritten.

### PV-O04: Maintain the published representation of shared links

**Actor / objective / entry / version:** authorised venue content editor from O02, actual configured owned URL/target if supplied, public title/summary/media base versus a private proposal. Domain/control setup remains J8-S11, not a new DNS workflow.

**Composition / copy:** **“Vista al compartir”**, published presence/menu/item target, title/summary, optional rights-cleared image, interface/content language, context and side-by-side proposed/public representation. **“Los servicios externos pueden conservar una vista anterior”**. Draft preview is local/documentary, not a request to make private content crawlable.

**Actions / effect:** save representation proposal → PV-O05; inspect known public target → PV-P09; verify owned domain/control → [J8-S11](m1-service-and-maintenance.md#j8-s11-inspect-domain-and-access-continuity). Do not expose draft data by fetching an external preview service. Publication adopts coherent reviewed public representation; URL ownership/redirect/cache/search mechanics stay technical/source dependencies.

**Errors / recovery / check:** missing owned target/rights leaves affected field/action pending, with no fake preview asset/link; changing restaurant facts/price does not overwrite an external provider's cached copy. Device/crawler/access result unknown is labelled unconfirmed, never proof of indexability. Save/review conflict → PV-X01. Check B1.08/B3.08: price-bearing snippet, if supplied, is tied to current published context/validity and cannot promise timely external refresh.

### PV-O05: Review public changes and publish a coherent selection

**Actor / objective / entry / version:** permitted editor/publisher from PV-O01–PV-O04; local proposal, last confirmed saved draft, current public references, dependency group and operation result remain distinct. Reuse [O03](m1-connected-journey.md#o03-review-and-preview), [O05](m1-connected-journey.md#o05-selected-publication) and [O06](m1-connected-journey.md#o06-publication-result).

**Composition / copy:** **“Revisar cambios públicos”**, current versus proposed venue/editorial/relationship/representation facts → affected placements/languages/outputs → explicit selected coherent group → preview PV public destinations labelled private → permissions/result. C1 coffee/croissant and C3 L10/D11 retain their independent histories.

**Actions / effect:** known draft save allows review; **Publicar estos cambios** submits only reviewed authorised group through O05; known publication result → O06 and corresponding PV view. **Volver a editar** → originating PV-O card; **Cancelar** retains private draft/known public source. Required private target item publication must be explicitly included/reviewed with its dependencies or the relation waits; it never sweeps all drafts into scope.

**Errors / recovery / check:** review outdated after source/context/meaning change → PV-X01/current versus proposal review; unreviewed factual translation uses established fallback/withholding, not false reviewed status. Unknown save cannot be reviewed as a confirmed revision; unknown publication cannot be declared live. Check directed/publication invariants and original G4-01 recovery; no new automatic publish or urgency shortcut.

### PV-X01: Recover permission conflict and uncertain results

**Actor / objective / entry / version:** operator from PV-O01–PV-O05 with a denied action, conflicting base/current revision or original save/publication response unconfirmed. Recheck actual edit/publish/status access, not job-title assumptions.

**Composition / copy:** original action/scope, permitted local proposal, last confirmed saved draft/current public source and observed result. **“No hemos podido confirmar el guardado. Comprueba el resultado antes de continuar”**, **“Estos datos cambiaron después de tu revisión”**, or denied-action copy specific to edit/publish/status access. Revoked venue access hides restricted source and local private work per existing recovery contract; no claim of no-effect follows merely from revocation.

**Actions / effect:** **Comprobar estado** → [X02](m1-connected-journey.md#x02-failed-or-unknown-result) / [CP-X02](m1-content-preparation.md#cp-x02-result-register-and-unknown-operation), bound to original action/venue/revision. Known saved result → PV-O05; confirmed no-effect permits revalidated save; conflict → [CP-X01](m1-content-preparation.md#cp-x01-conflicting-revisions) and origin with fresh deliberate review; publication/status denial → [X01](m1-connected-journey.md#x01-publication-permission) / [CP-X03](m1-content-preparation.md#cp-x03-permission-and-access-boundary). Support when permitted follows J8-S08; no invented recipient/contact.

**Errors / recovery / check:** uncertainty remains pending with authorised check/manual support, not unlimited retry or forced overwrite. Equal text/price alone is insufficient operation evidence. No reset/undo can publish unrelated drafts, revive expired offerings or remap a copied item/profile. Check save-applied/lost response, not-applied, changed-underfoot and revoked access; offline public reading does not grant offline editor mutation.

## 5. Criteria capabilities and connected walkthroughs

| Criterion | Concrete states / transitions | Documentary check / remaining evidence |
| --- | --- | --- |
| J1.1 | PV-P01 → PV-P02/PV-P03; PV-O01 → PV-O05 | Correct identity/local-kitchen hours/exception/declarations, unknown fields and maintained sources; actual facts absent. |
| J1.2 | PV-P03 → PV-P04/PV-P11 | Closed/planned/general/empty/expired distinct; no D11 or future stock guarantee; calendar implementation pending. |
| J1.3 | PV-P04/PV-P06/PV-P08 | Actual price/format/unit/minimum/supplements and independent food limits; real review absent. |
| J1.4 | PV-P02/PV-P10/PV-P09 → J14-C01 or retained public task | Language context/fallback and external exits; real targets/translation/device handoff pending. |
| J1.5 | PV-P09 → PV-P11 → PV-P04/PV-P06 | Withdrawn/expired/context-changed target recovery; owned URL/routing/cache evidence pending. |
| J2.1 | PV-P04 → PV-P05/PV-P06; optional PV-P01/PV-P07 | Direct C1 entry without registration/photo/promotional gate; rendered reading remains untested. |
| J2.2 | PV-P04 ↔ PV-P06/PV-P08 | Terrace/general exact applicability and reselection; no guessed context/format or mixed price. |
| J2.3 | PV-P05 ↔ PV-P06/PV-P10 | Reviewed visible language query, active dimensions/no-result/reset and retained position; real search absent. |
| J2.4 | PV-P05/PV-P06 | Incomplete food group inside exclusion result, positives excluded, no safety/personal-profile implication. |
| J2.5 | PV-P06/PV-P07/PV-P08/PV-P11 | Sold-out/removed/expired distinctions and relevant return; relation/editorial maintenance behind each public assertion. |
| J2.6 | PV-P11/PV-P10 → J10-P04/J10-P05 → current appropriate PV state | Loaded coverage/time/food limits, absent target and coherent reconnect; no private offline state. |

### Individual affected capability record

These 23 rows identify this block's contribution, not 23 completed software capabilities. Reuse B2.01–B2.09 offer/context rules and J10/J11/J14/J15 without duplicating their coverage ledger. The [72-parent map](m1-connected-journey.md#7-compact-coverage-and-remaining-work) stays unique, with 36/30/6 treatment and S1/S2 separate.

| Capability | PV contribution and remaining boundary |
| --- | --- |
| B1.01 | PV-P01/PV-O02/PV-O05 public presence and maintained content; rendered layout pending |
| B1.02 | PV-P02/PV-P03/PV-O01 visit facts/hours/exceptions; actual input/complete calendar contract pending |
| B1.03 | PV-P02/PV-O01 explicit declared detail/unknown attributes, no certification inferred |
| B1.04 | PV-P01/PV-O02 optional authentic editorial sections; material/review pending |
| B1.05 | PV-P01/PV-P04/PV-O02 coherent no-photo name/content hierarchy; visual identity/tokens/rendering pending |
| B1.08 | PV-P09/PV-O04 published representation/discovery; actual owned domain/URL/SEO/cache evidence pending |
| B1.09 | PV-P02 → J14-C01, link/confirmed booking boundary; actual supported destination pending |
| B3.01 | PV-P05/PV-P06 category/return/context orientation |
| B3.02 | PV-P05/PV-P10 reviewed visible-language search/no-result/reset |
| B3.03 | PV-P05 explicit declared dimensions/active filter/reset |
| B3.04 | PV-P05/PV-P06 positive/pending food facts and distinct exclusion-result groups |
| B3.05 | PV-P06 gradual explanation without hidden price/condition |
| B3.06 | PV-P06/PV-O02 supplied faithful explanations, translation/source dependencies |
| B3.07 | PV-P07/PV-O03/PV-O05 venue-selected ordered highlights, no invented bestseller/stock claim |
| B3.08 | PV-P09/PV-P11/PV-O04 correct public target/intent/context/language and changed-target recovery |
| B3.10 | PV-P08/PV-O03/PV-O05 directed editorial relation, applicability/current food/price/translation/source review |
| B5.01 | PV-P10/PV-O01/PV-O02 reviewed content language and preserved task; four-language real content not supplied |
| B5.04 | PV-P04/PV-P06/PV-P08/PV-P10 common price/status/validity source, not language copies |
| B5.05 | PV-P10/PV-O05 affected factual translation/fallback/withholding |
| B5.07 | PV-P02/PV-P06/PV-P08 declarations/preparation/adaptations distinct and pending limits |
| B6.01 | PV-P09/PV-P11 stable owned target intent; actual destination/QR evidence pending |
| B6.02 | PV-P01/PV-P04 presence versus direct-menu intent without compulsory gateway |
| B6.03 | All public PV states anonymous and readable without installation or private profile |

### Reader-led walkthroughs

| Walkthrough | Reset fictional branch / ordered states and consequence |
| --- | --- |
| VW01 | C1 direct menu → PV-P04/PV-P05/PV-P06 → return. No photos/account/story/search setup required; coffee amount is the selected confirmed branch and croissant draft private. |
| VW02 | C3 pre-12:30 versus 12:45 → PV-P01/PV-P02/PV-P03/PV-P04. Local/kitchen distinct, L10 published planned with conditions; D11 hidden. Conditional exception unknown uses PV-P11, not fabricated closure. |
| VW03 | C2 terrace → PV-P04/PV-P05 query vino or Merlot/filter → PV-P06 → PV-P10 → retained applicable origin. Known milk exclusion and incomplete group stay distinct. |
| VW04 | C2 operator PV-O03 private VR1 bottle relation → PV-O05 → original O05/O06 known result → PV-P06/PV-P08 → wine detail → return. General/terrace facts rechecked; reverse absent until separately authored and published. |
| VW05 | Shared item → PV-O03/CP-S02 relevant recipe/format change → PV-O05 language/dependency review → PV-P08/PV-P10 or affected relation withheld. Price update reads current context; copy/name does not inherit relation. |
| VW06 | PV-P09 hypothetical configured share → recipient target retired → PV-P11/current menu; repeat offline loaded/unloaded then J10-P04/PV-P05. External cached preview cannot make price current; no real URL/clipboard/provider operation claimed. |

## 6. Author contrasts and regression

All rows are bounded readings of the described transitions, not passed product tests. Reset each fictional branch; conditional materials/destinations/declarations remain pending.

| Case | Contrast | Documentary result / remaining proof |
| --- | --- | --- |
| VC01 | C1 direct link, no photos/story/account/search | PV-P04/PV-P05 immediate short menu; no required onboarding or editorial gateway. Rendered use pending. |
| VC02 | Presence entry with missing identity versus missing logo | Missing logo permits readable name; uncertain venue identity uses PV-P11, never substitutes venue. |
| VC03 | C3 local closed versus local open/kitchen not open | PV-P02/PV-P03 separate facts and planned L10; no stock promise/D11. Real time/hours pending. |
| VC04 | Published exception known versus conflict/time uncertainty | Exact applicable scope/end only when established; otherwise PV-P11, no invented closure/open. |
| VC05 | No daily publication versus expired known daily menu | Different copy/recovery; actually published general offering allowed, old amount not current. |
| VC06 | Missing address/phone/booking target and failed device handoff | PV-P02/PV-P11 readable supplied facts, unavailable missing action; click not outcome. Actual configured destination pending. |
| VC07 | Attributes absent, generic access label, unverified adaptation | Detail/declaration/pending state, no negative assumption/certification/suitability. |
| VC08 | Terrace → general with matching versus absent format | PV-P04/PV-P06 updates exact values/conditions or requires reselection, no silent size/area change. |
| VC09 | Rice/fish/cheese comparison | Per-person minimum/100 g unknown total/supplements adjacent to amount, not hidden by detail/image. |
| VC10 | Vino match versus Merlot no results, reset | PV-P05 reviewed visible names/categories only; reset preserves context/language, service failure not zero results. |
| VC11 | Declared milk exclusion versus incomplete records | Cheese excluded even with other pending facts; unknown group separately inside filtered result, no safety inference. |
| VC12 | Changed/removed category or detail origin during reading | Confirm identity/intent, explain lost anchor, relevant current section; no similarly named replacement/private taste edit. |
| VC13 | ES → reviewed EN versus pending FR/DE/failed language fetch | PV-P10 labelled actual source/fallback/withheld misleading claim, common prices and current facts; no fabricated translation. |
| VC14 | Highlight absent, sold-out, withdrawn or claims popularity | Empty section optional; unavailable labelled, withdrawn destination omitted; no bestseller claim or compulsory placement. |
| VC15 | Directed cheese → wine versus deliberate reverse | PV-P08 only created direction; PV-O03 inverse is a separate proposal/review/result, no implicit reciprocity. |
| VC16 | VR1 bottle general versus terrace; extra/cup/food facts | Exact bottle 19,00 €/21,00 €, cheese conditions separate; no cup substitution/bundle sum/diet guarantee; sulphites and milk/wheat independent. |
| VC17 | Pairing target sold-out versus removed/format incompatible | Visible unavailable status and readable current detail only when published; missing target removed from current recommendation with relevant recovery. |
| VC18 | Pairing source withdrawn or stale response after offer change | PV-P11/source recovery or current compatible refresh; cannot show old contextual relation/price as current. |
| VC19 | Shared source recipe/text change versus independent copy | PV-O03/CP-S02 affected relation/language/food dependencies; no guessed new declaration or name-based remap. |
| VC20 | Draft target or ambiguous applicability during relation publication | PV-O05 blocks current relation assertion or reviews explicitly selected coherent target group; unrelated croissant/D11 remain private. |
| VC21 | Optional editorial/faithful-image assistance missing authorisation or failure | PV-O02 retains text/original/manual route; affected media blocked, no invented rights/history/photos. |
| VC22 | Configured public share, cancellation, denied clipboard versus missing URL | PV-P09 known copy success only; manual actual URL when supplied; missing URL pending, no invented operation. |
| VC23 | External stale preview after withdrawal/changed price | Current resolver PV-P09/PV-P11 wins; cache/history not current guarantee. No crawler/index/cache test claimed. |
| VC24 | Save applied with response lost, confirmed no-effect, concurrent proposal | PV-O05/PV-X01/CP-X02 distinguish local/confirmed/current/original outcome; revise/retry only after authorised check, no equal-value inference. |
| VC25 | Publish/venue access revoked during review/result recovery | PV-X01 original result remains known/unknown as evidence permits, restricted content hidden; edit permission not publish permission, no silent overwrite. |
| VC26 | Offline loaded versus absent relation/language/target, reconnect/account switch | J10 coverage/time/food limits; absent content absent, current coherent references rechecked; no private preference cache/A data in B or staff route. |

**Regression reading:** all 96 prior V01–V16/Q01–Q20/PC01–PC24/DS01–DS04/SC01–SC26/LC01–LC06 rows were read against the affected PV paths. Preserve their wording and review limits; no retroactive rewrite or new independent credit. V price/context/urgent/private/exception/output invariants remain; Q video/nutrition/display/measurement/connection/session/diet boundaries remain; PC import/shared-copy/glossary/bulk and DS original-save distinctions remain; SC authority/export/maintenance/outcome/privacy remains. LC category loss cannot become empty tastes just because public categories changed. Public filtering/reading anchor/highlights/relation edits never write a private preference profile. G4-J15-01 is independently resolved only at its reviewed documentary scope, not implementation.

### Author refinements before handover

| Refinement | Initial gap found / correction supplied |
| --- | --- |
| VF01 | VR1's initial fixture left general applicability conditional while contrasting both prices. State the editor's deliberate general/terrace and source-format selection; no inherited relationship placement. |
| VF02 | Coherent refresh alone left a late prior-area/language response's visible consequence implicit. Add the current public intent/reference gate in section 2; old result cannot replace new choice or restore private state. |
| VF03 | First structural check found paraphrased J10-P04 and J8-S11 fragment names. Replace them with actual destination headings and recheck all links. |
| VF04 | Destination inventory found shorthand public/operator IDs in VC/VW/capability rows that could be mistaken for original storyboard states. Fully qualify those PV destinations and recheck the inherited-state inventory. |

These are author corrections during drafting/checking, not new independent findings or runtime tests.

## 7. Dependencies and accountable continuity

| Contribution / checkpoint | Concrete pending input and effect |
| --- | --- |
| G5 with G2: venue facts and editorial sources | Supplied identity/address/contact/hours/exception/attributes, authentic text/media/rights, factual explanation/relation and translations before claiming real venue delivery; pending fields are not production actions. |
| G3 with G1: M2/#4 | Identity/placement/applicability, hours/exception/time/source consistency, publication/dependency groups, action/result correlation, access isolation and public target/context/language resolution. No API/storage/search/URL scheme selected here. |
| G6 with G1/G3/G2: focused discovery | Actual supported public titles/preview/language/owned domain, indexability/cache/redirect requirements from current primary guidance and verified hosting/provider access. No SEO, structured-data compliance, traffic or instant cache-refresh proof supplied. |
| G4 independent | Review PV public/operator paths, VC01–VC26 and affected regression on this delivery's immutable commit; source/current/privacy/food/context and recovery. No reviewer availability or acceptance claimed. |
| G2/G4 with actual authorised participants/devices | Rendered visual hierarchy/template/bespoke, long text/keyboard/focus/reflow/assistive reading, device share/clipboard/QR and real task comprehension. Description/fictional cases cannot prove these. |

**Block completion boundary:** all 17 PV cards, 11 unchanged-source criterion mappings, 23 affected capability rows, six walkthroughs and 26 contrasts supply a coherent descriptive proposal. Author structural/cross-document checks and any refinements are recorded with reproducible evidence now versioned in root `research-evidence/` (3 October storage migration). No software suites or live data/provider/media/crawler/clipboard/QR operation; no independent PV review or M1 closure follows.

**Executed documentary verification:** 387 local/internal links across 15 linked documents, actual fragments/headings/fences/table widths, 17 PV cards with required fields and defined inherited destinations, 11 unchanged-source criteria, 23 capability rows, six VW/26 VC and four VF refinements. All 96 prior contrast rows and original state cards, source criteria/matrix/functional definition/ADR-0005 and ADR-0008–0012 match baseline 2eb8e86; 72 parents appear exactly once and S1/S2 remain separate. C1–C3, extended and scoped J15 checks also pass with their current link counts; dated prior results are preserved. Diff/staged/author/push/PR readback were recorded only after they succeeded; those original records are now versioned in root `research-evidence/` (3 October storage migration). No suite or real/independent/rendered test is represented.

**Remaining M1 order:** public/editorial/consultation/pairing behavior is now described, with its actual/technical/independent/visual obligations retained. Next descriptive block consolidates remaining J4/J5 programming, exceptions and service continuity; then complete J6/J7 maintained food register/staff/print/QR output behavior; visual expression/rendering and full M1 review/interaction/real evidence remain required throughout. Preserve the single 72-capability ledger, all accepted treatments and S1/S2; document counts do not establish a measured completion percentage. G1 coordinates actual contributions and remaining reviews; G2 incorporates verified returns. Continue draft PR #21/#5, with no merge or issue/milestone closure.
