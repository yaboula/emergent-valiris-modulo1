# M1 content preparation and maintenance

Updated 2 October 2026 · G2 Product Design · [M1 #5](https://github.com/yaboula/valiris-restaurants/issues/5) · draft [PR #21](https://github.com/yaboula/valiris-restaurants/pull/21).

**Status: complete descriptive proposal for this block, subject to the author checks recorded below; not implementation, independent review or M1 completion.** The owner selected Markdown and authorised this delivery. Links navigate descriptions, not working product actions. No PDF parser, image processor, assistance provider, persistence service, real venue or participant is represented.

## 1. Sources, mandate and decisions

Continue the [C1–C3 storyboard](m1-connected-journey.md) and [J10–J15 journeys](m1-extended-journeys.md), using the [functional definition](../research/storefront-digital-menu/functional-definition/functional-definition.es.md), [capability matrix](../product/m0-capability-matrix.md), [source criteria](../product/m0-journeys-and-criteria.md), [M1 briefs](../product/m1-design-briefs.md) and [roadmap](../project/roadmap.md). Common context/protocol and these sources were read previously and reused; this increment inspects their relevant import, assistance, sharing, publication and maintenance sections. The baseline is `60d76ad`, with a clean working tree on `docs/m1-connected-journey`; #5 and draft #21 were checked open before editing.

**Owner-selected:** shared item content is the principal reuse option; independent copies remain available. The owner answered the specific shared-versus-copy question and then authorised this plan. [ADR-0011](../adr/0011-shared-menu-content-and-contextual-maintenance.md) records that choice separately from proposed field ownership, scope/recovery and M2 contracts. ADR-0008/0009 remain accepted and unchanged; ADR-0010 retains its proposed status. The 72 parent capabilities remain 36 included, 30 configurable at launch and six connection-dependent, with S1/S2 separate. This block does not close the remaining J8/J9, pairing, visual, interaction or independent-evidence work.

**Responsibility:** G2 Product Designer consolidates and corrects this document. G1 coordinates actual G3/G4 review and G5 materials at the checkpoints in section 10. Named groups are responsibilities, not a claim that specialists are available or were consulted. No general competitive research is reopened.

| Affected party | Intended value and cost to evaluate |
| --- | --- |
| Diner | Consistent contextual prices and explicit food/translation limits; factual safety cannot be inferred from import or assistance. Mixed-language fallback may impose reading effort. |
| Restaurant, staff and buyer | Less repeated maintenance through shared facts and reviewed intake; source checking, resolving ambiguity and replacing paper still require work. No measured time saving is claimed. |
| Valiris | One explainable maintenance path for template and bespoke presentation; source provenance, context ownership, coherent publication, conflict handling and media review add engineering/service obligations. No margin or superior performance is established. |

## 2. Fixtures and version boundaries

All following inputs are **fictional source transcripts and simulated states**, not supplied files, extraction results, authorised media or content review by a restaurant. Keep the original C1–C3 prices, times and declared/pending facts unless the named branch explicitly changes them. Dated C3 stays 1–2 October even when read later. Reset between branches; they are not one cumulative history.

| Fixture | Inspectable source and review contrast |
| --- | --- |
| F-PDF · C1 | Simulated two-page PDF transcript: page 1 lists Espresso 1,60 €, Café con leche 1,90 €, Café con hielo 1,80 €, Tostada de tomate 2,80 €, Tostada de mantequilla 2,60 €, Croissant 2,20 €. Page 2 lists Zumo de naranja 3,00 €, Té 1,80 €, Agua 1,50 €, Chocolate caliente 2,80 €. No photos or food claims occur in the transcript. Complete branch recognises ten source entries; partial branch recognises six/page 1 and leaves four/page 2 unprocessed, not absent. Existing wheat/milk declarations stay intact during update. |
| F-PHOTO · C2 | Simulated photo-region transcript: “Tabla de quesos de leche cruda con membrillo y pan de masa madre · 24 / 34”; another region “Pan extra · 2”. No portion labels, terrace amounts or complete food record are supplied by these regions. Separate manual confirmation supplies media/general 24,00 €, completa/general 34,00 €, media/terraza 26,00 €, completa/terraza 36,00 €, pan extra/terraza 2,20 €. These are operator-supplied fictional facts, not inferred photo results. |
| F-DATA · C3 | Simulated structured rows with columns `date`, `service`, `menu_amount`, `item`, `choice_group`: `2026-10-01; comidas; 16,50; sopa; primero`, `2026-10-01; comidas; 16,50; flan; postre`, `2026-10-02; comidas; 17,50; arroz; segundo`. The last row maps to separate D11, not the current menu. Other choices/inclusions from C3 remain supplied separately; this excerpt is not a complete daily menu. Failure branch has an unreadable amount `16,5?` and reversed validity 15:30–13:00. Map menu price once, never as a per-dish amount. |
| F-SHARED · C2 | Added fictional reuse branch: one cheese source ficha CS1 used by general and terrace presentations, each with its own confirmed format/amounts above. Published contexts CS1/g1 and CS1/t1 refer to the same recipe revision r1; CP-S01 creates a private reuse proposal, not a publication. Recipe branch r2 adds operator-declared walnuts, retaining declared milk/wheat and remaining information pending. Nutrition is pending; EN factual text, if present in this branch, is simulated reviewed r1 and affected by r2. No real translation or recipe review is claimed. |
| F-COPY · C2 | Reset CS1/r1; private independent copy CC1 for a separately maintained offering, with copied facts labelled for restaurant confirmation. No origin/date/food/stock review is inferred from duplication. It does not receive subsequent CS1 changes. |
| F-BULK · C1/C2 | C1 ordinary coffee edit 1,90 € → 2,00 € with separate croissant-description draft retained. Separate C2 bulk proposal changes only terrace cheese media 26,00 € → 27,00 € and terrace pan extra 2,20 € → 2,30 €; general values remain 24,00 €/2,00 €. Independent urgent branch selects current terrace cheese and wine; only availability changes. Existing future/editorial drafts stay private. |

Source addressing is proposed UX: page/region/row and original text beside each proposal, plus an unprocessed-source checklist. “Ten recognised entries” means only the simulated parse inventory, not ten correct or complete reviewed entries. Source completeness must be checked against the actual material; no confidence percentages, nutrition numbers, file-size limits or provider success rates are invented.

Private version vocabulary: **batch IB1** is an intake operation; **proposal IP1** its staged revision; **draft ED1** is incorporated editable content. None is a public revision. Updating an already edited/published item must record its reviewed base and compare current values before incorporation/publication. ED1 does not overwrite existing E10/D11 drafts by assumption. The public menu remains its last known coherent publication with its actual validity, not an expired menu relabelled current. An authorised withdrawal remains possible through existing publication controls if facts cannot be maintained safely.

## 3. Shared interface and publication rules

- Entry lives under **Contenido** in the existing operator workspace. Header order: venue → task → source/destination → **“Borrador · no publicado”** and saved status. C1 needs no contexts, languages, glossary, assistance or sharing setup. A template and a studio-designed public route use these same content controls; there is no restaurant page builder.
- Desktop review pairs source and proposal; mobile uses an explicit **“Original / Propuesta”** switch preserving the same item/region and entered work, with source access beside the affected field. Lists identify selected elements/contexts in text, not colour alone. Field errors, focus return and announcements are design intentions, not rendered accessibility evidence. No secret/private diner inputs enter these tasks.
- New proposals never delete missing rows, convert blank values to zero or overwrite declarations automatically. Matching by name proposes candidates, not identity. Updates, shared reuse, independent copy and leaving unresolved are deliberate alternatives. A source that explicitly contradicts a fact marks a conflict for review; ignoring the contradiction does not make that fact current. Unsupported material remains visibly unprocessed.
- Shared source facts cover identity, recipe/ingredients and their food/diet/nutrition/translation dependencies. A placement owns its menu section/order, format/context amounts, supplements/conditions, validity and availability; format/portion changes still affect relevant food/nutrition facts. Prices/status are not language-specific copies. Shared content is bounded to the selected restaurant, not cross-restaurant reuse.
- Publication of a common factual change is one coherent reviewed group containing all affected published uses of that shared recipe/variant and the necessary factual fallback/pending states. If an affected use cannot be reviewed or the actor cannot publish it, the shared factual publication is blocked; retain the private proposal or take an explicitly authorised withdrawal/review route. Do not detach/copy to evade a permission or known food fact. Inapplicable expired uses are recorded for later review, never reactivated. Unrelated draft changes are not included; dependent unsaved/conflicting drafts require reconciliation, not silent inclusion. G3 must evaluate enforcement and atomicity in M2.
- Editorial bulk actions save proposals and enter selected publication. Urgent bulk actions affect only current published availability for the explicitly selected item/context/service. Group outcome can be confirmed, not applied, conflicted, denied or unknown. An unknown operation must be checked by its original action/scope/revision reference before retry; matching current values alone do not prove success.
- Assistance is optional at every entry. Accepting a suggestion or glossary term creates a draft, never reviewed translation or public content by itself. Price-format/food/diet/nutrition/source assertions remain restaurant-confirmed facts. Accepted image improvement needs supplied permitted material and faithful review; without those inputs only its workflow is described. No generated image stands in for the served dish.
- After confirmed publication, affected translation, staff, paper, comparison/offline and display outputs follow their existing version rules. A generated/regenerated file does not replace paper already placed. Public offline snapshots keep version/age/warning; unattended screens withdraw unconfirmed price/availability. A new nutrition/diet statement has its own evidence and review state.

The following cards all specify the actor, entry/version, composition/copy, action destinations, public/private effect, errors/recovery and author-check expectation. Bare O/P/X destinations refer to C1–C3 only; J11/J14/J15 destinations are qualified. CP identifiers are local to this package.

## 4. Import and source review

### CP-I01: Choose source and destination

**Actor / objective / entry / version:** authorised content editor from [O02](m1-connected-journey.md#o02-content-editor), correct venue, no batch yet; prepare new content or proposed changes to a chosen existing menu. A revoked venue access enters [CP-X03](#cp-x03-permission-and-access-boundary).

**Composition / copy:** venue/task heading, **“Importar carta · se preparará un borrador”**, source choices **PDF / Fotografía / Hoja o datos**, destination **Nueva carta / Proponer cambios en una carta existente**. Show current destination/public/draft version if existing. No file present: **“Selecciona material o escribe la carta manualmente”**. Existing-menu update is additive review, not replacement.

**Actions / effect:** choose source and destination → [CP-I02](#cp-i02-check-source-and-map-fields); **Introducir manualmente** → [CP-M01](#cp-m01-routine-mobile-maintenance); return → O02 unchanged. All intake remains private. Wrong restaurant/destination requires correction before starting, without applying content.

**Errors / recovery / check:** no source, absent menu or unavailable access explains the missing entry and keeps allowed choices; never import into a guessed destination. Check J3.1/J3.2: C1 reaches a manual or single-menu import path without advanced setup.

### CP-I02: Check source and map fields

**Actor / objective / entry / version:** editor from CP-I01 with selected source and destination; stage IB1, retain source address, no ED1/public update. Source access is for authorised venue actors; filenames do not certify rights.

**Composition / copy:** source preview/transcript reference first, page/region/row inventory, supported/unreadable sections, proposed column-to-field mapping. F-DATA maps `menu_amount` to the composed-menu price and `choice_group` to menu choice structure, not dish price. **“Comprueba qué representa cada columna”**; **“Esta parte no se puede interpretar; revísala manualmente”**. Date/service/locale and units need explicit confirmation where ambiguous.

**Actions / effect:** **Preparar propuesta** → [CP-I03](#cp-i03-processing-and-cancellation); correct mapping stays here; replace file → CP-I01; manual entry from source → CP-M01 with retained reference. No publication or merge. Unsupported source cannot start a falsely complete parse; protected/unreadable file offers a readable authorised source or manual work.

**Errors / recovery / check:** missing fields, mixed formats, blank or negative amount and invalid validity keep raw input and field-linked explanations; no zero, guessed portion or silent date correction. Replacing material creates a new source revision and requires mapping again; do not combine obsolete regions. Check J3.2/J3.3 against F-DATA and F-PHOTO.

### CP-I03: Processing and cancellation

**Actor / objective / entry / version:** editor starts IB1 on confirmed source/mapping; no published result. The saved operation reference identifies source, destination and base revision; this is a proposed service contract, not an implemented job API.

**Composition / copy:** **“Preparando propuesta · todavía no incorporada”**, source coverage known so far, work remaining if observable, not invented percentage/ETA. **Cancelar preparación** identifies the batch. Closing the view does not claim cancellation; returning reads IB1 status.

**Actions / effect:** known completion → [CP-I04](#cp-i04-result-and-source-coverage); known failure/partial → CP-I04 or [CP-I07](#cp-i07-failed-unknown-and-resumed-intake); confirmed cancellation → CP-I07 with **“Preparación cancelada”**, source retained. Cancellation race/lost response → CP-I07 **“Resultado pendiente de comprobar”**. **Volver a Contenido** → O02; work is still private.

**Errors / recovery / check:** no connection does not mean stopped or complete; resume checks the same IB1. If preparation finishes before cancellation, show actual prepared proposals and let the editor explicitly discard or review them; none is incorporated automatically. Check J3.2: processing, failure and cancellation are distinct and no retry creates a second batch unknowingly.

### CP-I04: Result and source coverage

**Actor / objective / entry / version:** editor checks known IB1/IP1 result; understand what was interpreted before choosing incorporation. “Prepared” is not “reviewed” or “published”.

**Composition / copy:** coverage summary → source checklist → proposed rows → unresolved issues. F-PDF complete: **“10 entradas propuestas · revisión pendiente”**; partial: **“6 entradas propuestas. La página 2 está pendiente de interpretar”** with its four transcript entries retained as source, not parsed rows. F-DATA excerpt: **“Material parcial: faltan opciones y condiciones del menú”**. Unreadable regions appear even when no item could be created.

**Actions / effect:** **Revisar propuestas** → [CP-I05](#cp-i05-identity-matches-and-duplicates); review individual source fact → [CP-R01](#cp-r01-field-and-source-comparison); retry unprocessed portion → CP-I07; manual correction → CP-R01; explicitly discard selected staged proposals → CP-I07. Only authorised private staging changes; missing source rows never remove existing menu entries.

**Errors / recovery / check:** completion with omissions cannot claim a complete menu. Reviewer must resolve each source segment as incorporated, deliberately excluded with reason, or unprocessed; excluded is not fabricated successful extraction. Parsed entries can proceed individually if independently complete; missing mandatory composed-menu choices block that group, not every unrelated item. Check J3.2/J3.4 and explicit completeness limits.

### CP-I05: Identity matches and duplicates

**Actor / objective / entry / version:** editor from CP-I04 with IP1 and the destination's current source/draft/public identities; reconcile each proposed row without overwriting by name.

**Composition / copy:** source row → candidate existing item(s), where used, changed fields and current/private conflicts → choices **Actualizar esta ficha / Reutilizar ficha compartida / Crear copia independiente / Dejar pendiente / Excluir propuesta**. **“Un nombre parecido no confirma que sea el mismo producto”**. Reuse is principal when adding an existing confirmed item to another menu, not an automatically selected match.

**Actions / effect:** confirmed update → CP-R01; reuse → [CP-S01](#cp-s01-reuse-a-shared-item); independent copy → [CP-S03](#cp-s03-create-or-detach-an-independent-copy); new item → CP-R01. Leave pending remains in IP1; exclusion records source/reason, not deletion of the existing item. Review incorporation → [CP-I06](#cp-i06-incorporate-selected-reviewed-proposals).

**Errors / recovery / check:** two identical names, changed source identity or relevant draft conflict prevents assumed merge; [CP-X01](#cp-x01-conflicting-revisions) shows current/private/proposed fields. Confirmed incorporation records proposal identity; repeats show **“Ya incorporada a este borrador”** and link its result, not append another copy. Check J3.3 and preservation of restaurant/context boundaries.

### CP-I06: Incorporate selected reviewed proposals

**Actor / objective / entry / version:** authorised editor selects resolved IP1 changes against recorded current/private bases; create or update ED1 only. Price-format ambiguity, missing composed-menu essentials and conflicting identity stay outside applicable incorporation until resolved; food data may remain explicitly pending.

**Composition / copy:** selected rows/fields and source references → destination menu/context → required dependent group → existing draft conflicts → staged rows remaining unresolved/private. **“Incorporar al borrador · no publicar”**. F-DATA current rows and D11 future row have distinct destinations; it is not one present-day menu.

**Actions / effect:** confirmed incorporation → [CP-R02](#cp-r02-review-dependent-facts-and-languages); return → CP-I05 retaining selection; save denied → CP-X03; failure/unknown → [CP-X02](#cp-x02-result-register-and-unknown-operation). Existing live publication stays unchanged. A source segment needing factual review cannot acquire a reviewed label through incorporation.

**Errors / recovery / check:** compare bases again before applying; no silent replacement of the croissant draft or D11. A known saved ED1 result links incorporated rows, unresolved remainder and original IB1/IP1. Unknown save checks original operation before retry, not new content equality. Check J4.1/J4.4: incorporation and public publication are different actions.

### CP-I07: Failed unknown and resumed intake

**Actor / objective / entry / version:** editor returns to IB1/IP1 after parse failure, partial work, cancellation, discard or lost result; preserve inspectable original and known staged work.

**Composition / copy:** original operation status/source coverage; **“No se pudo interpretar esta parte”**, **“Resultado pendiente de comprobar”** or **“Preparación cancelada”**, each with actual known proposal inventory. Explicit discard lists staged proposals and impact; it never discards ED1 or deletes public content already created elsewhere.

**Actions / effect:** **Comprobar preparación** resolves IB1 → CP-I04; known not processed **Reintentar parte pendiente** creates an identified continuation tied to IB1 → CP-I03; **Corregir manualmente** → CP-R01; **Usar otro material** → CP-I02 with new source mapping; return → O02. Explicit discard confirmation leaves source/operation record as permitted by future retention contract and returns CP-I01. No publication.

**Errors / recovery / check:** inaccessible source/status → CP-X03; remain unknown and offer authorised help, not blind retry. Resumed rows reconcile source addresses and already incorporated identities; a replaced source cannot reuse old reviewed mappings by assumption. Check J3.2 and CP-I05 duplicate handling; actual operation identity, retention/deletion and retry enforcement remain G3 work.

### CP-R01: Field and source comparison

**Actor / objective / entry / version:** editor opens an import row, manual entry or assisted proposal with source reference and current/public/private bases. Review field meaning, not just spelling.

**Composition / copy:** source beside proposed name/description, format/amount/unit, supplements, menu/date/context and food facts. F-PHOTO says **“24 / 34 · formatos sin identificar”**; inputs **Formato / Importe / Contexto** await confirmation. F-DATA says **“Precio del menú completo”**, with choices/inclusions separately pending. Missing food: **“Información pendiente. Consulta al personal”**, retaining known milk/wheat where supplied in the existing record.

**Actions / effect:** manual correction saves an authorised draft through CP-I06 or CP-M01; source mapping correction → CP-I02; dependent review → CP-R02; inspect original returns to same field, preserving input. Explicit deletion/correction of a declared fact requires actual supplied reason and review; empty imported cells do not request deletion. Update amounts only for the confirmed context.

**Errors / recovery / check:** ambiguity blocks affected price group; raw `16,5?`, missing unit and inverted validity retain input with O02 field errors. Source-derived claims need supplied evidence, not unchecked certification/diet icons. Contradictory facts route CP-X01. Check J3.3/J3.4: correct format/context before publication, pending stays pending without losing positive declarations.

### CP-R02: Review dependent facts and languages

**Actor / objective / entry / version:** editor reviews saved ED1, imported/manual/assisted/shared changes and each affected recipe/portion revision; no new publication yet.

**Composition / copy:** current versus proposed facts, all shared uses, food declarations and remaining unknowns, diet attributes, nutrition basis, text/translation/glossary dependencies and affected outputs. CS1/r2 shows **“Nueces declaradas; leche y trigo declarados; información restante pendiente”**. Diet requires [J15-O01](m1-extended-journeys.md#j15-o01-maintain-explicit-venue-diet-attributes); nutrition source/portion/variant requires [J11-O01](m1-extended-journeys.md#j11-o01-source-portion-and-variant-draft). Unsupported values stay pending, not zero. Factual EN r1 becomes affected; common price/status has no separate language edit.

**Actions / effect:** resolve fact → CP-R01; language assistance → CP-A01; glossary → CP-G01; nutrition → J11-O01; diet → J15-O01; inspect full shared scope → CP-S02; **Previsualizar** → [CP-R03](#cp-r03-contextual-preview-and-selected-publication). All saves remain private. An unchanged positive declaration is retained while the rest is incomplete.

**Errors / recovery / check:** blocked dependent use or incompatible language must be resolved or use explicit current-source fallback/authorised withholding through existing review. Do not publish an old factual translation or independently infer vegetarian/vegan from text. Portion changes affect nutrition even if recipe ingredients stay unchanged. Check J3.4/J6.1–J6.3 and connections to J11/J15.

### CP-R03: Contextual preview and selected publication

**Actor / objective / entry / version:** editor/publisher inspects reviewed ED1 against current publication and chosen coherent scope. Preview permission does not imply publication authority.

**Composition / copy:** **“Vista previa · no pública”**, venue/menu/context/date/service/language and source revision; public price, units, supplements, declarations/pending notices and language fallback. F-DATA previews 1 October current E10 and 2 October D11 separately; includes C3 manual validity exception if selected in its independent branch. Source omissions are still listed in private review, not hidden by polished preview.

**Actions / effect:** return → CP-R02; **Revisar publicación** → [O05](m1-connected-journey.md#o05-selected-publication), with CP-S02 common-fact dependencies or selected contextual prices; confirmed result → [O06](m1-connected-journey.md#o06-publication-result). Only that existing authorised publication changes public content. Unresolved unrelated proposals and croissant/D11 drafts remain private. Output review → [O09](m1-connected-journey.md#o09-version-linked-paper-composition), [J11-O03](m1-extended-journeys.md#j11-o03-check-nutrition-across-outputs) or [J12-O02](m1-extended-journeys.md#j12-o02-observe-refresh-and-reconcile).

**Errors / recovery / check:** latest-base conflict → CP-X01; permission → CP-X03; unknown publish → CP-X02 routed by original action, not assumed success. Outdated schedules require [X06](m1-connected-journey.md#x06-scheduling-and-manual-exception) re-review, never automatic incorporation into a scheduled target. Check J3.6/J4.1/J4.4/J7.3: preview never publishes or replaces physical paper.

## 5. Optional assistance and venue glossary

### CP-A01: Request a bounded suggestion

**Actor / objective / entry / version:** authorised editor from O02/CP-R02 on a saved source revision; request text, translation or image improvement without making assistance compulsory. Venue terms and supplied facts accompany the requested task, never private diner profiles.

**Composition / copy:** original content → **Descripción / Traducción / Mejorar imagen** → task limits and proposed destination; **“La propuesta necesitará tu revisión; no se publicará”**. Text example uses the C2 cheese name already supplied, not a new provenance claim. Translation preserves supplied proper names/terms. Image task requires an original, permission basis and intended use; current fixtures have no such asset: **“Añade una imagen que tengas autorización para usar”**.

**Actions / effect:** known provider/task availability and authorised supplied material **Solicitar propuesta** → [CP-A02](#cp-a02-compare-accept-edit-or-reject); **Editar manualmente** → CP-M01; missing/unavailable service → [CP-A03](#cp-a03-assistance-failure-and-outdated-source). Image without material remains here/manual source selection, not a fictitious improved asset. Service access/provider/cost/data processing are pending G3/G1 decisions, not a promise of free generation.

**Errors / recovery / check:** unsupported task or missing rights keeps original and explains what is needed. Do not send material merely because importing it was allowed; permitted processing/distribution and necessary source metadata need checking. Check J3.5: assistance can be skipped, and no ingredient/certification/media authority is invented.

### CP-A02: Compare accept edit or reject

**Actor / objective / entry / version:** editor reviews a proposal tied to its source revision, task and language/asset; assistant output is unreviewed. This card describes simulated suggestions, not provider execution.

**Composition / copy:** original/proposal side by side or mobile toggle, differences and supplied fact references, **“Propuesta · pendiente de revisión”**. C2 faithful text candidate: **“Tabla de quesos de leche cruda, acompañada de membrillo y pan de masa madre.”** Unsupported contrast **“quesos ecológicos certificados”** is rejected because certification was not supplied. EN candidate **“Raw-milk cheese selection with quince paste and sourdough bread.”** is a fictional translation proposal; names/meaning and food notices still require review. Image comparison requires an actual permitted original and result, checking dish identity, portion and presentation; fixtures supply neither.

**Actions / effect:** **Aceptar en borrador** or **Editar propuesta** → CP-R01/CP-R02 retaining source and review need; **Rechazar** returns CP-A01 with original unchanged; **Revisar glosario** → CP-G01. Accepted image remains a draft asset until faithful/rights review and O05 selected publication. No acceptance substitutes for actual translation, food or recipe confirmation.

**Errors / recovery / check:** changed source → CP-A03 before acceptance; failed save/unknown → CP-X02; permission revoked → CP-X03. Rejecting an unaccepted proposal does not discard an already saved user edit. No artificial dietary match, nutrition value or review badge is added. Check J3.5/J6.3: acceptance, edit and rejection have different retained results.

### CP-A03: Assistance failure and outdated source

**Actor / objective / entry / version:** editor on known request/source after unavailable provider, processing failure, lost response or newer source. Original and permitted entered edits stay available; no public change.

**Composition / copy:** **“No se pudo preparar la propuesta. Puedes seguir editando”**; unknown **“La respuesta está pendiente de comprobar”**; changed source **“El contenido cambió desde la solicitud; compara la propuesta con la versión actual”**. Original and any returned proposal show their actual revisions, not a silently refreshed label.

**Actions / effect:** manual work → CP-M01; known failure **Solicitar de nuevo sobre la versión actual** → CP-A01; check original request → CP-A02 only when known returned; compare current versus old suggestion → CP-X01 then a newly reviewed proposal. Return → CP-R02. A lost response does not authorise repeated provider calls/costs without knowing the original result.

**Errors / recovery / check:** inaccessible request status stays unknown; discard stale suggestion deliberately, not user's newer draft. If the original image permission/source is no longer valid, do not reuse the old result for publication. Check J3.5/J4.4: provider failure never blocks manual editing or overwrites a newer source.

### CP-G01: Maintain a venue glossary proposal

**Actor / objective / entry / version:** authorised editor from CP-R02/CP-A02, current restaurant glossary and proposed revision GT1; maintain consistent names/terms/tone without another restaurant's data.

**Composition / copy:** term/source language, preserve-name flag, supplied meaning, target-language proposed term, affected occurrences and current/proposed review state. Fictional example preserves **“Casa del Mediodía”** as a venue name; **“membrillo” → “quince paste”** is a candidate for C2 accompaniment, not a reviewed universal substitution. **“Propuesta de término · comprobar significado”**; C1 has no mandatory glossary task.

**Actions / effect:** save term proposal → [CP-G02](#cp-g02-review-glossary-impact); manual edit/reject preserves prior term; request wording → CP-A01. No mass replacement/publication or automatic approval. Common prices/status are outside the glossary. Refer to the restaurant glossary here; do not confuse it with the repository's domain glossary.

**Errors / recovery / check:** conflicting meaning, missing context, reused name or newer glossary base → CP-X01; failed/unknown save → CP-X02. Keep supplied text, distinguish a missing term from an empty approved translation. Check J6.3: a reusable glossary supports maintenance but does not claim a translation review.

### CP-G02: Review glossary impact

**Actor / objective / entry / version:** editor/translator reviews GT1 against actual maintained content versions. A term may affect source or target text differently; only relevant occurrences are included.

**Composition / copy:** current/proposed term → occurrence list by item/menu/language → contextual meaning and public/private state → selection and retained terms. **“Este cambio afecta a 2 textos de ejemplo; revísalos antes de publicar”** uses a simulated two-occurrence fixture, not a counted production inventory. Proper names remain supplied; dietary/food claims require their own confirmation.

**Actions / effect:** accept selected contextual wording into drafts → CP-R02; reject occurrence keeps original where still factually valid; edit term → CP-G01. Current meaning changes invalidate relevant factual translations even if an occurrence was not selected; unreviewed factual EN follows explicit source fallback/withholding in CP-R03. Updating glossary alone does not rewrite or republish a live menu.

**Errors / recovery / check:** changed occurrence → CP-X01; inaccessible affected common-fact use blocks relevant factual publication through CP-S02; failed save → CP-X02. Staff output retains the same food facts and pending labels regardless of terminology. Check J6.2/J6.3: vocabulary consistency never conceals stale facts or substitutes for review.

## 6. Shared item and independent copy

### CP-S01: Reuse a shared item

**Actor / objective / entry / version:** editor adds an existing confirmed item to a second menu in the same restaurant from CP-I05 or O02; CS1/r1 source, target placement proposal private. This is not a cross-restaurant catalogue.

**Composition / copy:** **“Reutilizar ficha compartida”** principal action; common name/recipe/facts → existing uses → new menu placement/context → contextual price/formats/conditions/validity needing confirmation. **“Los datos comunes se mantendrán juntos. Revisa el precio y las condiciones de esta carta”**. Alternative **Crear copia independiente** remains directly available.

**Actions / effect:** confirm common identity and target context → CP-R01/CP-R02 private placement; inspect uses → [CP-S02](#cp-s02-review-a-shared-change); copy → [CP-S03](#cp-s03-create-or-detach-an-independent-copy); cancel → CP-I05/O02 retaining original. Reuse does not inherit a general amount as terrace price, current stock as future stock or copy publication authority.

**Errors / recovery / check:** wrong restaurant, incompatible recipe or inaccessible common source blocks reuse; choose the correct permitted source or prepare genuinely separate content, without cloning protected data. Unknown save → CP-X02; ambiguity stays pending. Check J3.3/B4.04: operator can explain common data versus contextual placement before saving.

### CP-S02: Review a shared change

**Actor / objective / entry / version:** editor/publisher reviews CS1 proposed r2 against all affected published/private/expired uses and current recipe revisions. Source and placement identifiers remain visible.

**Composition / copy:** **“Ficha compartida · usada en carta general y terraza”**; changed common fields → affected uses and bases → dependent ingredient/food/diet/nutrition/EN and outputs → scope. Recipe branch r2 adds declared walnuts while preserving milk/wheat/remaining pending. **“Este cambio factual se revisará para ambos usos publicados”**. Separate price branch **“Solo terraza · media: 26,00 € → 27,00 €”** leaves general 24,00 € and common recipe untouched.

**Actions / effect:** common factual review → CP-R02, then CP-R03/O05 with all affected published uses as one group; contextual edit → CP-B01 or CP-M01, confined to selected placement. Review expired/private uses remains private and does not activate them. An affected scheduled draft needs X06 re-review. Return → CP-S01/O02.

**Errors / recovery / check:** missing publish permission on one affected use → CP-X03 and block that common factual group; conflict or hidden dependent draft → CP-X01; unknown common-group publication → CP-X02 with all uses unconfirmed until checked. If safe current facts cannot be maintained, an authorised publisher must explicitly review withdrawal; detaching is not a workaround. Check J3.4/J4.1/J6.1/J6.2: no incompatible shared recipe claims or uncontrolled draft inclusion.

### CP-S03: Create or detach an independent copy

**Actor / objective / entry / version:** editor chooses copy from CP-I05/CP-S01 or explicitly detaches a permitted placement from CS1/r1; creates private CC1 with new identity. The original and other placements retain their relationship.

**Composition / copy:** source version, copied fields, target placement, independence consequences and facts needing confirmation. **“Esta copia no recibirá los cambios posteriores de la ficha original”**. Explicit detach also says **“Esta carta dejará de usar la ficha compartida al publicar el cambio revisado”**; until then its public placement still references CS1.

**Actions / effect:** **Crear copia en borrador** → CP-R02; detach membership proposal → CP-R03/O05, showing old/new identity and dependencies; cancel → CP-S01/CP-S02 unchanged. Default does not copy confirmed stock, temporary availability, future validity, schedule or reviewer certification. Copied supplied declarations remain visible with their source, requiring applicability review, not erased or called newly verified. Paper/media rights are not transferable merely by copying.

**Errors / recovery / check:** source changed mid-copy → CP-X01; denied protected data/access → CP-X03; unknown creation/detach → CP-X02 before retry. Detach during a known common-recipe change must carry the actual applicable recipe/dependencies; no permissions/food-fact bypass. Check J3.3/J5.4: CC1 can diverge only through authorised factual maintenance, not old-state reactivation.

### CP-S04: Duplicate a menu and review placement order

**Actor / objective / entry / version:** editor duplicates a permitted menu structure for another menu in the same restaurant, from O02/CP-S01; source menu revision and new private target are distinct. Duplication is content maintenance, not a new page-layout editor.

**Composition / copy:** source sections/items and order → new name/context/service → relationship choices. **“Nueva carta en borrador”**; principal **Reutilizar fichas compartidas**, alternative **Copias independientes** with CP-S03 consequences, both requiring explicit selection. Review per-item exceptions and contextual amount/condition mappings; source amounts can be proposed only when applicable, never assumed confirmed in a new area. New menu has no confirmed stock, schedule, live validity or publication.

**Actions / effect:** **Preparar nueva carta** → CP-R02 with reused source identities or new copy identities and target placements listed; contextual review → CP-R01; **Reordenar secciones o productos** → CP-B01 editorial order operation. Preview → CP-R03 for a separately reviewed publication. Cancel returns O02 without changing the source menu. A composed menu must retain and review choice/inclusion constraints; it cannot become independent flat dish-price rows.

**Errors / recovery / check:** changed source/membership/order → CP-X01; inaccessible item remains an explicit blocked entry, not a silently omitted clone; failed/unknown creation → CP-X02 before retry. Detachment/copy never bypasses a known recipe change or permission. Check B4.04/J3.3/J5.4: whole-menu reuse and reordering conserve identities, contextual meaning and public/private boundaries.

## 7. Mobile and bulk maintenance

### CP-M01: Routine mobile maintenance

**Actor / objective / entry / version:** editor from O02/CP-I01/CP-A03 on a selected item/private revision; make an ordinary price, text or photo edit without a new design commission. Availability authority has a separate live task.

**Composition / copy:** one-column venue/item/header **“Borrador · no publicado”**, current versus proposed amount/text, retained input, fact/dependency and source controls. C1 café con leche **1,90 € → 2,00 €** requires no area/glossary/assistance; croissant description stays its own draft. Photo selection permits an authorised original, alt-text/faithful-crop review and explicit **Quitar foto**; no fixture photo is fabricated. A no-photo public menu remains valid.

**Actions / effect:** **Guardar borrador** → CP-R02, then CP-R03; replace/remove photo proposes that selected asset change only; **Disponibilidad del servicio actual** → [O07](m1-connected-journey.md#o07-urgent-availability) or CP-B01 urgent mode if permitted. Leaving unsaved input offers save or explicit discard; failed save retains inputs for CP-X02/manual retry. The same controls serve template and bespoke presentation.

**Errors / recovery / check:** bad amount/unit, failed image upload, lost save result, permission and concurrent edit use field explanations/CP-X01–CP-X03 without clearing unrelated work. Image removal does not assert source-file deletion or rights revocation. Check J3.1/J4.4/B4.03: price/text/photo/availability routes are inspectable, while actual touch targets, focus and persistence remain untested.

### CP-B01: Choose bulk mode and scope

**Actor / objective / entry / version:** editor chooses multiple contextual content changes, or authorised service actor selects current published availability. Modes are explicit and cannot silently change mid-operation.

**Composition / copy:** **Editar borradores / Disponibilidad actual** → venue/menu/context/service → item selections by identity → selection count and names. Editorial operation choices are **Importes / Campos de contenido / Orden**; common factual edits require CP-S02 dependencies. F-BULK editorial targets two terrace amounts; urgent targets terrace cheese and wine in the current scope. **“Solo elementos seleccionados”**. A filter/search change shows retained selections outside view; it does not silently include all results or hide their effect.

**Actions / effect:** **Revisar alcance** → [CP-B02](#cp-b02-preview-bulk-change-groups); clear selection remains here; a shared factual selection → CP-S02 full affected uses. Order uses **Subir / Bajar** for sections/items as well as any future drag interaction, preserving identity and amount/conditions together; no mouse-only reordering. Switching mode requires a new preview and confirmation, preserving or explicitly discarding entered editorial work, never executing it. No selection gives **“Selecciona al menos un elemento”**.

**Errors / recovery / check:** absent context, expired service or withdrawn target cannot enter live urgent scope; show current target through existing X04/X07 recovery. Missing action permission → CP-X03. Check J5.2/B4.04: visible counts/names are scoped to actual selected identities, including off-screen selections.

### CP-B02: Preview bulk change groups

**Actor / objective / entry / version:** actor from CP-B01 with selected mode/items and per-group current bases. Exact changes are proposed explicitly, not an invented global price multiplier.

**Composition / copy:** selected items/context/service with current → proposed values → coherent groups/dependencies → permissions/conflicts → exclusions. Editorial: **“Guardar 2 cambios en borrador: terraza, media 26,00 € → 27,00 €; pan extra 2,20 € → 2,30 €. General sin cambios”**. Order branch changes C1 **Cafés → Desayunos → Bebidas** to **Desayunos → Cafés → Bebidas** in the chosen menu only; show both complete ordered lists and preserve item identity/prices. Urgent: **“Marcar agotados: queso y vino · terraza · servicio actual”** and **“Los borradores de precio y texto seguirán sin publicar”**.

**Actions / effect:** editorial **Guardar estos borradores** → [CP-B03](#cp-b03-apply-and-inspect-bulk-results), then CP-R02/CP-R03/O05; urgent **Confirmar disponibilidad de estos elementos** → CP-B03 under live availability permission only. Revise selection → CP-B01; inspect common facts → CP-S02. Any choice to exclude denied/conflicted groups generates a new explicit preview of the remaining scope before execution.

**Errors / recovery / check:** no empty/unsupported input becomes zero; format/unit/portion changes bring dependent facts. A known pre-action conflict/denial blocks confirmation until reviewed or explicitly excluded; do not report already-applied exclusions. Expired target routes X07. Check J4.1/J5.2/J6.1: editorial versus urgent effects cannot be combined by one secondary action.

### CP-B03: Apply and inspect bulk results

**Actor / objective / entry / version:** permitted actor confirms reviewed operation BO1, exact action/scope and per-group bases. Bases and permissions must be rechecked at application; actual contracts remain M2.

**Composition / copy:** per-group result and revision/reference → aggregate known outcomes → pending/failed actions and private drafts. Simulated partial contrast: terrace media price saved to ED1, pan-extra group conflicted at a newer 2,40 €, no public price change. **“1 cambio guardado en borrador; 1 conflicto sin aplicar”**. Unknown response: **“No se ha podido confirmar el resultado de este grupo”**, never **“Todo actualizado”**.

**Actions / effect:** confirmed editorial groups → CP-R02; conflicted group → CP-X01; not-applied known failure → CP-B02 re-preview of that group; unknown → CP-X02 original BO1 status; urgent confirmed groups → public [P04](m1-connected-journey.md#p04-public-sold-out-state) and [CP-B04](#cp-b04-history-and-scoped-recovery). A common factual group cannot split its affected uses; other independent groups may have distinct outcomes, all displayed.

**Errors / recovery / check:** revocation after preview produces denied/not-applied or unknown if execution cannot be checked; no assumed rollback/success. Refresh uses known new bases; retry selects only confirmed not-applied groups after renewed review, not the original whole set. Check J5.2/J4.4: partial result is honest, original operation matters and unrelated drafts remain private.

### CP-B04: History and scoped recovery

**Actor / objective / entry / version:** authorised history viewer/corrector inspects known BO1 outcomes; publication, draft save and live availability are different recorded actions with their actor/scope/source/base/result. A read permission does not confer correction authority.

**Composition / copy:** each group's field changes and known result; current versus proposed correction; dependencies and later changes preserved. **“Revisar corrección de estos cambios”** rather than unconditional **Deshacer todo**. C2 urgent undo preserves a later terrace price 27,00 € and unrelated editorial drafts; a newer availability change is a relevant conflict. Old nutrition/recipe/translation claims are not automatically restored.

**Actions / effect:** editorial restore creates a new reviewed draft → CP-R02/CP-R03/O05; current urgent availability correction → [O08](m1-connected-journey.md#o08-undo-and-current-state-review), then CP-B03 result register; changed/expired target → X07 current-service explicit stock review, not old-service revival. Unknown original action must first enter CP-X02, not be “undone” by assumption.

**Errors / recovery / check:** relevant newer base → CP-X01; permission → CP-X03; failed/unknown correction → CP-X02 preserving known current state. Source/copy membership restoration also compares current recipe and dependency versions, not only name. Check J5.4/J7.3: recovery creates a scoped current correction and paper regeneration remains separate from physical replacement.

## 8. Shared conflict, result and permission recovery

### CP-X01: Conflicting revisions

**Actor / objective / entry / version:** actor reaches a relevant source/draft/placement/glossary/media conflict from import, assistance, sharing or bulk review. Compare recorded base, current and proposed values; no silent winner.

**Composition / copy:** identity/context/source first, **“El contenido cambió desde tu revisión”**, base/current/proposal with dependencies; unrelated changes preserved. C1 known current coffee 2,10 € versus proposal 2,00 €; C2 pan extra current terrace 2,40 € versus proposal 2,30 €; ingredient conflicts show facts and affected uses rather than only text differences.

**Actions / effect:** adopt current or edit/reconfirm a new private proposal → CP-R01/CP-R02 or CP-B02 as appropriate; source change → CP-I02/CP-A01; membership change → CP-S02; return preserves unrelated authorised work. Reconfirming triggers a fresh preview before save/publication/live action. Selecting current does not approve unresolved facts or publish another draft.

**Errors / recovery / check:** current unavailable → CP-X02; denied access → CP-X03. If the source is an authoritative external field, [J14-C03](m1-extended-journeys.md#j14-c03-authoritative-external-changes) ownership applies: import/manual editing cannot overwrite a non-editable field; unresolved provider rules remain a dependency, not silently presumed writable. Check J4.4/J6.2: conflict resolution preserves version/factual boundaries.

### CP-X02: Result register and unknown operation

**Actor / objective / entry / version:** authorised actor checks original operation/action, source/destination/group/base references after lost result or failure. This is a proposed observable result contract, not a job/payment API.

**Composition / copy:** original action and known outcomes, separately **Confirmado / No aplicado / Conflicto / Sin permiso / Resultado desconocido**. **“Comprueba esta operación antes de repetirla”**. Readable current values alone do not prove the original action happened; known expired/absent publication is not described as current.

**Actions / effect:** known import result → CP-I04; incorporation → CP-R02 with recorded ED1; assistance response → CP-A02; bulk → CP-B03; copy/reuse → CP-S02/CP-S03 result; editorial publish → O06 only for that original action; urgent/correction → O08/P04/CP-B03, never O06 editorial by default. Retry a known not-applied group requires refreshed bases/permission and the appropriate review. Unknown stays unknown, with authorised help/status check available; public changes are never fabricated.

**Errors / recovery / check:** revoked status access → CP-X03; source unavailable retains only authorised known information, no repeated provider work/content insertion. Original operation correlation and coherent group enforcement require G3 verification. Check J3.2/J4.4/J5.2: retry/cancel/undo must not duplicate, publish private work or pretend rollback.

### CP-X03: Permission and access boundary

**Actor / objective / entry / version:** person lacks or loses the action-specific source/destination/content/publication/availability/history access. Venue identities and scopes are checked separately from diner accounts.

**Composition / copy:** **“No tienes permiso para esta acción”** names the action only within permitted scope; permitted work and denied groups remain distinct. Revoked venue access removes that venue's private source/proposal content from the view; no export/copy/help disclosure of protected material. **“Solicita acceso a la persona responsable del restaurante”** is a suggested user action, not a sent message or assumed available colleague.

**Actions / effect:** authorised alternative editing → O02/CP-M01 only if that permission actually exists; live-only actor → O07 for allowed scope; permitted status read → CP-X02; otherwise authorised workspace/O01 access-recovery state. Preserve unsaved work only within the future permitted local-retention contract; do not promise a revoked user can keep reading it. No publication/copy/retry merely because the editor was previously opened.

**Errors / recovery / check:** revocation after action may leave an unknown operation; do not assert no change unless confirmed not applied. Shared publication denied for one required use blocks that common group. Check J4.1/J5.2 and private-source separation; actual enforcement, local clearing and retention are G3 dependencies.

## 9. Traceability and author verification

This is the author's bounded reading of the descriptions, not executed importing, translation, image processing, publication or usability tests. The six J3 criteria are the direct target; the other eight rows trace only their affected parts, not closure of their entire source journeys. The [source criteria](../product/m0-journeys-and-criteria.md) stay intact.

| Criterion | Concrete states and transitions | Observable design expectation / remaining evidence |
| --- | --- | --- |
| J3.1 | CP-I01 → CP-M01 → CP-R03/O05; O01/O02 | One-menu C1 and manual entry; draft/live visible; identical routine controls for template/bespoke. Rendered routes and actual autonomy untested. |
| J3.2 | CP-I01–CP-I07, CP-R01, CP-X02 | Three source examples, processing/partial/failure/cancel, source coverage/manual recovery and correlated retry. Real supported formats/source quality and persistence unverified. |
| J3.3 | CP-R01 → CP-S01/CP-S03/CP-S04 → CP-R03 | `24 / 34` unresolved until confirmed format/context; shared versus copied consequences explicit. Restaurant facts still fictional. |
| J3.4 | CP-R01 → CP-R02/CP-S02 → CP-R03 | Positive food declarations retained, remaining pending, ingredient/variant/portion dependencies; coherent shared factual group. Real food/diet/nutrition review required. |
| J3.5 | CP-A01 → CP-A02 or CP-A03 → CP-M01/CP-R02 | Optional accept/edit/reject/failure paths for text/translation/image; source preservation and no false served-dish/certification claim. No real permitted image or provider result. |
| J3.6 | CP-R03 → O05 or CP-R02 | Date/service/area/language/exception preview stays private; E10 and D11 independent. Rendering/navigation untested. |
| J4.1 | CP-I06/CP-R03/CP-S02 → O05, CP-X03 | Explicit selected coherent public scope; incorporation/private assistance never publishes. Enforcement and common-group atomicity pending. |
| J4.4 | CP-X01 → CP-R02/CP-B02, CP-X02 | Base/current/proposed conflict, preserve unrelated work, known/unknown result and refreshed review. Concurrent implementation proof pending. |
| J5.2 | CP-B01 → CP-B02 → CP-B03, CP-X02/CP-X03 | Selected item/context/live availability only, explicit permission/failure/partial/unknown results. No full software or service-lifecycle completion claimed. |
| J5.4 | CP-B03 → CP-B04 → O08/CP-R02, X07 | Field/action responsibility and reviewed correction; preserve newer unrelated data, no expired revival. Full history retention/restore contract pending. |
| J6.1 | CP-S02/CP-B02 → CP-R03 | Price/status stays contextual and language-independent. Shared source is not one global price or status. |
| J6.2 | CP-R02/CP-S02/CP-G02 → CP-R03/J11-O01/J15-O01 | Recipe change flags food/diet/nutrition/factual translations and all affected uses; retain known declarations. Review/fallback comprehension untested. |
| J6.3 | CP-G01 → CP-G02 → CP-R02/CP-R03/O09 | Proper names/meaning and terminology reviewed by occurrence; no fake review, same food state in staff/public output. Real translator/staff review absent. |
| J7.3 | CP-R03/CP-B04 → O09/J11-O03/J12-O02 | Affected generated outputs identifiable by source/version; refresh is distinct from placed paper and unknown physical display. Real output checks pending. |

### Individual affected capability record

Each row below is annotated design coverage, not an implemented or independently accepted capability. No percentage is derived from these rows. The [72-parent map](m1-connected-journey.md#7-compact-coverage-and-remaining-work) retains each parent once and distinguishes remaining work. Dependencies in section 10 apply to every relevant row.

| Capability | This increment / linked behaviour | Still needed for affected capability |
| --- | --- | --- |
| B4.01 | CP-I01–CP-I04/CP-I07: all three intake families | Actual source formats/quality, real intake and failure/recovery evidence |
| B4.02 | CP-I04–CP-I06/CP-R01: source, completeness, identity and ambiguity | Real extraction comparison and restaurant confirmation |
| B4.03 | CP-M01: ordinary mobile price/text/photo; O07 availability | Rendered mobile/accessibility, real photo and persistence evidence |
| B4.04 | CP-S01–CP-S04/CP-B01–CP-B04: share/copy/menu reuse/order/bulk/recovery | Shared-group/per-placement enforcement, actual concurrent operation |
| B4.05 | CP-R02/CP-R03 and O02–O04: private draft and contextual preview | Working preview and comprehension evidence |
| B4.06 | CP-R03/CP-S02 and O05/O06: selected coherent publication | Authorised/atomic application, actual results and independent review |
| B4.07 | CP-R03/CP-S02 → existing X06: changed scheduled target needs review | Existing schedule proposal still needs technical/timing verification; no new scheduler implemented |
| B4.08 | CP-B04/CP-X02 and O08: operation history/scoped correction | Retention, actor/result traceability and implementation recovery |
| B4.09 | CP-X03/CP-B02: action authority and common-use denial | Core permission contract, enforcement/local clearing, independent review |
| B4.10 | CP-A01–CP-A03: text/translation/faithful-image assistance | Permitted real material, provider/cost/processing and faithful review |
| B4.11 | CP-R02/CP-S02: food/diet/nutrition/translation/outputs | Real factual dependency review and coherent implementation |
| B5.02 | CP-A01/CP-A02/CP-R03: translation proposal/review/fallback | Real translation, reviewer responsibility and comprehension |
| B5.03 | CP-G01/CP-G02: venue glossary maintenance and impact | Real venue terms/context and maintained translation review |
| B5.04 | CP-S02/CP-B02: common numbers/status across languages | One context-specific source in implementation |
| B5.05 | CP-R02/CP-G02/CP-R03: affected language and source fallback | Real language evidence and independent comprehension review |
| B5.06 | CP-R01/CP-R02: declared facts per recipe/variant | Actual restaurant ingredient/variant records; no inferred absence |
| B5.07 | CP-R01/CP-R02: declaration versus pending/staff direction | Actual preparation/adaptation statements, maintained facts |
| B5.08 | CP-R03 → O09: staff record shares factual state | Complete maintained staff register and actual output review |
| B5.09 | CP-R02 → J11-O01/J11-O03: recipe/portion invalidation | Existing J11 still lacks real source/values/basis; no new numerical evidence |

### Reader-led walkthroughs

Reset to section 2 fixtures before each row. A link supplies a state description, not an executed action.

| Walkthrough | Connected path and inspection target |
| --- | --- |
| PW01 · C1 PDF/manual | [CP-I01](#cp-i01-choose-source-and-destination) → CP-I02 → CP-I03 → CP-I04 six/page 1 plus unprocessed page 2 → CP-I07/manual → CP-R01 → CP-I05/CP-I06 → CP-R02 → CP-R03/O05. Reject a claim that six parsed items form a complete ten-item menu, or that existing milk/wheat were erased. Manual alternative enters CP-M01 directly. |
| PW02 · C2 photo/reuse | [CP-I04](#cp-i04-result-and-source-coverage) → CP-I05 → CP-R01 `24 / 34` → manual format/area confirmation → CP-S01 → CP-R02/CP-S02 → CP-R03. Compare independent-copy reset CP-S03 and full menu reuse CP-S04; no auto-publication or guessed terrace amount. |
| PW03 · C3 data/assistance | [CP-I02](#cp-i02-check-source-and-map-fields) → CP-I04/CP-R01 → CP-I06 → CP-R02 → CP-A01/CP-A02 or CP-A03 → CP-R03/O05. Reject dish-level menu prices, incomplete composed-menu publication or D11 leakage. Inspect translation/glossary CP-G01/CP-G02 separately. |
| PW04 · Shared recipe/output | [CP-S02](#cp-s02-review-a-shared-change) CS1/r2 → CP-R02 food/diet/nutrition/EN → CP-R03/O05/O06 → O09/J11-O03/J12-O02. Both applicable published uses need coherent facts; paper remains physically unchanged. Denied common use routes CP-X03, not detach bypass. |
| PW05 · Bulk/recovery | [CP-B01](#cp-b01-choose-bulk-mode-and-scope) → CP-B02 → CP-B03 mixed saved/conflict/unknown → CP-X01/CP-X02 → CP-B04. Run independent urgent reset with editorial drafts present, then a later price change and expired-service undo. No whole-operation blind retry or revival. |

### Fresh author counterexamples

All expected results below were checked by reading the final connected descriptions. “Consistent” is a documentary verdict, not a runtime pass. Evidence/limitations are retained under `research-evidence` outside Git.

| Case | Input and branch | Documentary result / remaining proof |
| --- | --- | --- |
| PC01 | C1 no material, one menu, no photos; CP-I01 → CP-M01 | Consistent: manual price/text path, no advanced setup or design purchase. Actual mobile/bespoke usability pending. |
| PC02 | F-PDF complete versus six rows/page 1 only | Consistent: ten proposed not ten reviewed; page 2's four entries visibly unprocessed. Real extraction coverage pending. |
| PC03 | Unsupported/protected source, partial failure, cancellation race | Consistent: original/manual alternative, known cancelled versus prepared/unknown; no public change. Real support/cancel contract pending. |
| PC04 | Lost IB1 result, continuation and repeated incorporation | Consistent: check original operation/address/row identity; no duplicate ED1 rows or whole-batch blind retry. Correlation implementation pending. |
| PC05 | F-PHOTO `24 / 34`, missing terrace and portion labels | Consistent: ambiguous affected price blocked, explicit operator confirmation needed, no guessed multiplier or portion. Real restaurant confirmation absent. |
| PC06 | F-DATA composed-menu price, date rows and invalid amount/time | Consistent: price mapped to menu, absent choices explicit, E10/D11 distinct; entered errors retained. Parser and actual data remain absent. |
| PC07 | Imported blank food cells versus prior milk/wheat; source contradiction | Consistent: blanks do not erase known declarations; contradiction needs factual review, not ignore-to-confirm. Actual food evidence pending. |
| PC08 | Two same-name products, existing croissant draft and newer coffee 2,10 € | Consistent: explicit identity choice and base/current/proposal conflict; no draft overwrite or guessed match. Concurrent persistence pending. |
| PC09 | Text candidate includes unprovided organic certification | Consistent: reject/edit unsupported proposal, original retained; acceptance alone remains draft. Real assistance reliability not tested. |
| PC10 | EN proposal, then recipe source changes before accepting | Consistent: proposal source stale, new comparison/review, no automatic reviewed/public language. Translation review absent. |
| PC11 | Image task with no permitted original; conditional failed upload/provider | Consistent: no asset/result invented; manual work/original preserved. Actual rights-cleared before/after evidence still required. |
| PC12 | Assistance reject versus already saved user edit; unknown response | Consistent: reject only suggestion, original-operation check before retry/cost, preserve allowed newer edits. Provider/result contract pending. |
| PC13 | Glossary name preservation and meaning change in two occurrences | Consistent: contextual review, no automatic public rewrite or price copy; affected factual EN remains pending. Real terms/translator absent. |
| PC14 | Reuse CS1 in terrace | Consistent: common identity/facts but explicit terrace formats/amounts/conditions; no inherited stock or publication. Real sharing contract pending. |
| PC15 | CS1/r2 walnuts with milk/wheat/remaining pending | Consistent: review both published uses, diet/nutrition/EN affected, known positives retained. Facts are fictional; independent review pending. |
| PC16 | One required common use inaccessible or changed; expired use present | Consistent: common publication blocked/refreshed, no permission detach bypass or expired activation; unrelated drafts private. Atomicity/access verification pending. |
| PC17 | Copy CC1 then later CS1 change; detach during known recipe change | Consistent: new private identity, no automatic updates/stock/review; known applicable facts and permissions still required. Membership enforcement pending. |
| PC18 | Whole-menu reuse versus copies and section reordering | Consistent: explicit relation choice, no inherited validity/schedule, complete old/new order preserving item/price/conditions. Rendered order controls untested. |
| PC19 | Mobile price/text/photo replacement/removal with failed save | Consistent: retained allowed inputs, source/rights/dependencies, no zero or source-deletion assertion. Real asset, focus and touch checks pending. |
| PC20 | Two terrace amount edits with selections outside current filter | Consistent: named/count scope, general amounts unchanged; selection/filter change triggers new preview if scope changes. Interaction untested. |
| PC21 | BO1 two groups: one saved, second conflicted/denied after preview; separate reset makes that second result unknown | Consistent: group outcomes explicit; new preview before excluding/retrying; no global success or split common group. Actual partial-result handling pending. |
| PC22 | Urgent cheese/wine bulk with price/text/D11 drafts | Consistent: current contextual availability only; urgent result recovery cannot route to editorial publication. Runtime isolation pending. |
| PC23 | Undo after newer unrelated price versus newer availability or expiry | Consistent: preserve later price, review relevant availability conflict, no past-service revival; source restore reviews dependencies. Runtime/history proof pending. |
| PC24 | Published ingredient/price revision with old paper/snapshot/unknown screen | Consistent: same current/pending facts, flag actual affected outputs; no physical replacement/refresh claim, public historical snapshot differs from unattended display. Real device/paper/interaction evidence absent. |

### Regression review against previous packages

The author read all 16 V rows and all 20 Q rows against the new transitions. These 36 rechecks preserve the earlier scenarios; they do not rerun software or claim new participant evidence. The original review records remain intact.

| Existing cases | New branch compared / result and limits |
| --- | --- |
| V01–V02 | CP-I06/CP-M01/CP-B02: coffee editorial versus urgent croissant; consistent draft isolation and mobile route, no new software proof. |
| V03–V06 | CP-R01/CP-S01/CP-S02: ambiguous portions, general/terrace units/conditions, context/search/food limits; consistent, no ordering or food-safety inference. |
| V07–V10 | CP-I02/CP-I06/CP-R02/CP-R03: E10 first publication versus D11, temporal entry, urgency/undo, milk/EN fallback; consistent, fictional review remains fictional. |
| V11–V13 | CP-X01–CP-X03/CP-B04/CP-S04: action permissions/unknowns, schedule re-review and current stock confirmation; consistent, no implicit access or new scheduler. |
| V14–V16 | CP-R03/CP-M01/CP-B04: output freshness, input recovery and C1 breakfast expiry; consistent, no paper replacement/focus/time enforcement demonstrated. |
| Q01–Q04 | CP-S02/CP-R03/CP-A02: changed saved-option context, separately maintained video versus image task, loaded/unloaded offline and coherent reconciliation; consistent. No automatic relabelling of old saved prices/source; real media absent. |
| Q05–Q06 | CP-R02/CP-S02: nutrition source privacy/basis and recipe/portion invalidation; consistent, no invented nutritional figures or reviewed diets. |
| Q07–Q09 | CP-R03/CP-X03: public-only dedicated output, unconfirmed physical screen and density/reading-distance limits; consistent, no activated display or physical legibility claim. |
| Q10–Q11 | CP-B04/history: new change records do not modify measurement history or fabricate collection/exposure/causality. Existing zero-versus-missing and comparison revision boundaries unchanged. |
| Q12–Q14 | CP-X01/J14-C03: external ownership, direction-specific result and attribution; consistent, local import cannot override a non-editable source field. Six target/access dependencies remain unresolved. |
| Q15–Q17 | CP-X03: operator sources remain separate from public browsing and diner accounts/preferences; existing login/reset revision/purpose rules unchanged. No private profile feeds import or assistance. |
| Q18–Q20 | CP-R02/J15-O01: recipe/variant diet invalidation compatible with current offer; offline logout A/B and local reset/global deletion unchanged. Copying a ficha never copies diner identity/preferences. |

### Corrections during this delivery

These were found by the author in the first working draft, corrected before delivery and rechecked; no independent reviewer is credited.

| Finding | Correction and recheck |
| --- | --- |
| PF01 · Cross-document destination | The draft used a paraphrased J15-O01 heading in its fragment. Link now targets the actual “Maintain explicit venue diet attributes” heading; all fragments are checked structurally. |
| PF02 · Whole-menu maintenance gap | First draft covered only item-level sharing/copy. CP-S04 adds complete menu duplication/relationship choice and CP-B01/B02 add section/item order with non-drag actions. PC18 checks no inherited publication/stock/schedule. |
| PF03 · Ineffective reorder fixture | Initial reorder description retained C1's existing order. CP-B02 now shows an actual Cafés/Desayunos swap with complete previous/proposed order; PC18 checks identity/price preservation. |

### Parallel C1-C3 finding incorporated after delivery review

While updating the external handoff, the author found a concurrently supplied G1/G4 handback against immutable `60d76ad` in `research-evidence/reviews/c1-c3-60d76ad/review-handover.md`. It reports independent documentary C1–C3 review and G4-01/P2, not review of this content block or all J10–J15. Preserve that report/snapshot unchanged. The source O02/O03/O05 now explicitly links uncertain/competing draft saves to CP-X02/CP-X01 with a confirmed reviewable draft revision; X05 also clarifies incomplete food records inside the filtered result as requested. These are G2 author corrections; G4/G1 focused recheck is pending, not performed by this author.

All four branches below reset to public coffee 1,90 €, local 2,00 €, last confirmed private DR1/1,90 € and an unrelated croissant-description draft. No public price changes until a separate authorised confirmed publication. DR2/DR3/DR4 are fictional saved draft revisions, not created database records.

| Recheck | Written input / exact recovery and reviewable source |
| --- | --- |
| DS01 · Save occurred, response lost | O02 → CP-X02 checks original save and confirms DR2/2,00 €; O03 reviews that saved DR2, then O05 revalidates current source/permission. Local entry is reconciled, not silently discarded; croissant unchanged. Documentary expectation consistent, operation verification pending. |
| DS02 · Save confirmed not applied | O02 → CP-X02 confirms not applied, retains allowed local 2,00 € and last saved DR1/1,90 €; compare latest base in CP-X01/CP-R01, explicitly save/refetch confirmed DR2 before O03/O05. Unknown cannot use this not-applied route by assumption. Croissant/public unchanged; runtime correlation pending. |
| DS03 · Competing saved 2,10 € | O02 → CP-X01 shows last known DR1, current DR3/2,10 € and local 2,00 €. Adopt DR3 or deliberately edit/save a new confirmed DR4 after comparison; O03 reviews the chosen confirmed revision and O05 revalidates it. No silent overwrite or croissant inclusion. Documentary consistency checked; concurrency enforcement pending. |
| DS04 · Permission/venue access revoked | O02 → CP-X03: if only edit access lost, show confirmed draft only with actual remaining read permission, no resave/publication; if venue access lost, hide private content and return to authorised workspace/access recovery. CP-X02 leaves original result unknown if status cannot be read. Local retention/clearing follows actual future authority contract, not a promise of continued access. Public/croissant outcomes not claimed changed; implementation pending. |

**Structural verification:** 27 unique defined CP cards with all required fields; 14 mappings to unchanged source criteria; 19 individual affected-capability rows; 24 cases, five walkthroughs and three recorded corrections. All 273 local/internal links across 12 linked/affected documents resolve; tables, unique headings and fences are valid. All 16 V and 20 Q source rows are preserved, with the 36-case regression reading above. The source capability matrix/functional definition and accepted ADR-0008/0009 are unchanged; the first storyboard still contains all 72 parent IDs once with S1/S2 separate, eight tasks and its 14 findings/16 contrasts. Existing J10–J15 still has 38 unique states, all 20 criteria and its 12 findings/20 fresh contrasts. `git diff --check` passed. Reproducible scripts/output and bounded author-review evidence are outside Git in `research-evidence`. Counts measure document integrity, not completed capabilities or M1 percentage.

## 10. Dependencies, delivery and next action

| Dependency / contribution responsible | Effect until resolved / required checkpoint |
| --- | --- |
| G5 restaurant-authorised PDF/photo/data and G2 source review | All three examples remain transcripts; actual extraction completeness, source rights and restaurant factual confirmation are not proven. Supply representative source/quality/failure cases before affected intake acceptance. |
| G3 with G1: accepted formats, source storage/access/retention, operation correlation, shared/placement ownership, per-action permissions, group application/retry/cancel and concurrent recovery | Behaviour is proposed; no APIs/schemas, limits, algorithm or enforcement delivered. Review in M2 #4 before construction; technical incompatibility returns a concrete proposal, not silent scope deletion. |
| G1/G3 with G5/G2: assistance provider, permitted processing, cost and rights-cleared originals/results | Text/translation/image assistance remains descriptive and optional. No provider/cost/send authority or successful media improvement assumed. Resolve before real assisted tasks/affected launch closure. |
| G5 with G2/G4: actual ingredient/recipe/variant/portion facts, diet declarations, nutrition sources and language/glossary review | Known/pending fixture distinctions remain; actual dietary/nutrition/translation completeness and safe factual fallback are unverified. Resolve affected factual records and comprehension before public delivery. |
| G4 independent quality, G3 focused review, coordinated by G1 | Author checking does not satisfy independent approval. Review PC01–PC24, common-scope/per-context authority, source completeness and prior V/Q regressions before affected M1 closure; actual availability/activation is not asserted. |
| G2 visual/interaction and G5 actual staff/diner/device/print inputs | Markdown cannot demonstrate touch/focus/reflow/source comparison, assistance fidelity, paper pagination, physical display or task comprehension. Prepare actual rendering/interactions/participant checks; preserve original M1 evidence requirements. |

Delivery continues on `docs/m1-connected-journey` and draft PR #21, **Refs #5**, with no closing directive or merge. Docs/ADR indices, coverage, current briefs/roadmap references, changelog and external handoff are updated. Source criteria, capability treatment and accepted historical decisions remain intact. No software suite is run for this documentary increment.

**Delivered and checked by the author:** 27 state descriptions, three source-family transcripts, shared/copy/menu/order and bulk/recovery paths, the 14 criterion mappings, 19 individual affected-capability rows, five walkthroughs, 24 fresh contrasts and all 36 prior V/Q regressions. **Proposed/pending review:** the detailed source/placement/publication/assistance contracts and ADR-0011 integration, independent G4/G3 review and remaining M1 work. **Dependent on real evidence:** material/rights/facts/provider/access, actual operation behaviour and visual/device/participant results. None means 27 working screens or 19 completed capabilities.

Next: G1 coordinates independent/technical review using sections 9–10; G2 incorporates actual findings and continues remaining J8 buyer/service/delegation/export and J9 maintenance/digital-use paths, pairing and visual/interaction work. No unavailable specialist, sent communication or completed real test is invented. M1 #5 stays open.
