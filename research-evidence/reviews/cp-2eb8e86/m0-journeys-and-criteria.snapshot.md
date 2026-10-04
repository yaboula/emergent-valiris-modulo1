# M0 journeys and initial acceptance criteria

Version 0.3 · 1 October 2026 · Accountable owner: Yahya.

**Status: proposed behavioural criteria for accepted launch scope.** D1 is approved and D2 is amended by the owner to launch all enumerated capabilities except standalone audio and 3D; see [ADR-0008](../adr/0008-first-launch-capability-commitment.md). Inputs: [capability matrix](m0-capability-matrix.md), [reference definition](../research/storefront-digital-menu/functional-definition/functional-definition.es.md) and [roadmap](../project/roadmap.md). Criteria still need M1 review and later specification; no test or technical design is claimed complete. G1 consolidates public, operator and buyer coherence; independent Quality review remains pending.

## 1. Contrast cases and evidence boundary

| Case | Design fixture to prepare | Behaviours it must expose |
| --- | --- | --- |
| C1 — Simple café | Short stable menu, no photos, one location and ordinary hours | Immediate account-free consultation; useful visual identity; straightforward setup/price/availability changes; advanced configuration not compulsory |
| C2 — Variants and areas | Restaurant menu with terrace/general context, portion variants, supplements and a long wine section | Price/format/condition clarity; context switching; helpful search/filter/detail; no implication that a QR creates an order |
| C3 — Daily menu and languages | Date/service-limited composed menu; ES plus a reviewed other language; a future draft and food-information gaps | Before-visit planning, scheduling/exception conflict, translation changes, urgent availability versus draft, print version freshness |

These fixtures are **proposed design examples**, not clients, interviews or verified restaurant behaviour. Real materials and rights to use them are unconfirmed. Interface language coverage stays aligned with ADR-0005; C3 uses a contrast translation to exercise behaviour without claiming all translations are complete.

For each criterion, an M1 prototype/scenario walkthrough can check visible intent, states and recovery. It cannot establish database isolation, reliable timed execution, accessibility implementation, demand or reduced maintenance effort. M2 prepares sufficient rules/technical checks; M3–M5 implement and verify them. Real diner/operator sessions require access and consent; record assistance and outcomes separately from expert review. Missing real participants blocks the real evidence, not honest internal exploration.

## 2. Cross-journey rules

| Rule | Proposed invariant and relevant exceptions |
| --- | --- |
| R01 — Access and reading | Public presence/menu can be consulted without account/install. Direct-menu entry respects intent. Price/condition/food-state text does not rely only on colour/icons. Useful without photos; keyboard/focus/text enlargement and assistive-technology needs are designed and later checked. |
| R02 — Price and context | Product, variant/format, amount, supplement/weight/minimum condition, area/location, service/date and language express one coherent published offering. Essential conditions are visible at choice; context changes cannot silently retain an inapplicable price. |
| R03 — Planned versus current offering | A closed service does not hide a useful future/general menu. Planned offer is labelled without a stock guarantee. Explicit manual exceptions have scope/end and precedence over ordinary schedule; unresolved conflicting schedules are surfaced before affected publication. Preview is labelled as preview and shows selected context/date/language. |
| R04 — Draft and publication isolation | Draft content stays unpublished until authorised selected publication. An urgent availability action changes only its intended live state. Concurrent edits or changed scheduled targets produce an explicit conflict/review state, not silent overwrites or accidental bundled publication. A failure does not claim a successful public result. |
| R05 — Recovery and temporary-state lifecycle | Confirmation/result/undo identify affected content. Temporary exceptions and sold-out states have a visible end or explicit next-service review policy chosen by the venue; no silent restock. Recovery is reviewed against current price/context/availability/translation state. |
| R06 — Review and languages | Import/assistance produces an editable proposal with visible source/uncertainty. Shared price/status/validity are common across languages. Factual/ingredient changes mark affected translations; stale factual content cannot silently appear current. Proposed default: explicit reviewed-language fallback for affected content, or withhold the affected assertion/item when fallback would mislead; unrelated current content remains usable. Restaurant reviews supplied facts; specialist translation input may be needed for factual equivalence. |
| R07 — Food-information meaning | Distinguish declared/reviewed, pending, preparation warnings and adaptations on request. Missing data never means allergen-free, suitability or certified safety. Variants retain real differences. Allergy-exclusion filters separate unknowns with an explanation; direct consultation and staff assistance remain available. |
| R08 — Live source versus outputs | Printable menus, daily menus, staff records and QR supports have appropriate layout, source/context/language and version/date. A changed live menu does not update old physical sheets. Mark affected generated outputs for review/regeneration; language/food pending states do not disappear in print. |
| R09 — Connection boundaries | Links, generated outputs and automatic data sync have different meaning. Connected work identifies source/destination, access, field ownership, last known result and failure/conflict. Failure elsewhere does not silently overwrite owned content or claim all channels updated. These connected behaviours are conditional, not active integrations. |
| R10 — Product and service autonomy | Templates and bespoke design support routine content/price/photo/availability updates through common management. Service scope, revisions, content responsibility, support/delegated changes, domain rights and export/exit are understandable before commitment. Export is not a promise that the hosted service continues after termination. |
| R11 — Evidence and measurement | Views, searches and map/contact/booking-link clicks are labelled digital events with period/source/limitations. Unknown traffic/source stays unknown; zero collected data is distinct from unavailable measurement. No physical attendance, confirmed booking, revenue, causal uplift or individual identity is invented. |
| R12 — Personal choices and media | Personal saved/comparison options remain account-free and are never orders; changed price/context/availability must be reconciled. Restaurant-supplied video has review/rights, explicit playback, text/caption alternatives and failure recovery; no forced media gateway or invented dish representation. |
| R13 — Declared nutrition | Values identify source, portion/unit basis and review state; unknown nutrition remains unknown. Variant/ingredient changes flag affected values. Never invent totals or imply certified accuracy, dietary suitability or a medical recommendation. |
| R14 — Offline consultation | Only actually loaded content can be read offline, with snapshot version/time and clear stale-state warning. No current-stock/price/food guarantee is inferred; unavailable cached content and reconnect conflicts are explicit. Reconnect adopts a coherent current publication and reconciles saved choices. |
| R15 — In-venue displays | A dedicated read-only output uses reviewed content with explicit location/area/service/language. Drafts do not leak; layout, current revision, reconnect and stale/failure states are inspectable. An unattended screen must not keep obsolete prices/food claims looking current. |
| R16 — Comparison limits | A comparison identifies question, version/change, metric, periods, denominator/exposure where known, missing data and limitations. Insufficient data is a supported state, not a reason to defer the feature; no causal or sales uplift is invented. |
| R17 — Registered-diner personalisation | Personal recommendations require registered, authenticated account access; ordinary consultation and venue recommendations stay account-free. Necessary account/preferences belong to the committed launch, with explicit empty/error/no-match states and user account controls. Proposed initial inputs are explicitly supplied preferences; no behavioural history is invented. Recommended items use current published context/availability/prices, disclose limited input and never infer allergen safety. Signed-out or another-user/venue state must not expose private preferences or personalised cached output. Account scope, authentication method and data rules need M2 review. |

## 3. Journeys and verifiable initial criteria

### J1 — Diner before the visit

Entry through venue page/shared link/search result → recognise venue → inspect visit information → open general or planned menu → read formats/conditions/food information → choose contact/map or supported external booking route.

- **J1.1:** venue identity, location and current/published hours/exceptions are understandable; local versus kitchen hours can be distinguished. C1/C3; R01, R03.
- **J1.2:** a closed-current-service state permits useful published general/future-menu consultation with validity/context; it never promises future stock. C3; R03.
- **J1.3:** prices, variant names and relevant conditions are visible while comparing; missing food information is explicit and points to the venue's staff. C2/C3; R02, R07.
- **J1.4:** language changes preserve the chosen context/task; missing/affected translation follows R06. Map/contact/booking exits state what happens next, without implying confirmation. C3; R06, R09, R11.
- **J1.5:** an expired/withdrawn deep link explains the changed target and permits return to the current appropriate menu; it does not show an old price as current. C2/C3; R02, R03.

### J2 — Diner during the visit

Direct/menu-context QR → verify venue/area/service/language → browse/search/filter if useful → compare item/variant and declared food information → inspect detail/pairing → return without losing orientation.

- **J2.1:** C1 reaches a readable menu without registration/install, compulsory editorial gateway, photos or advanced setup. Identity accompanies the task; promotions do not block it. R01.
- **J2.2:** C2 terrace entry names the context. Changing to general offering explicitly updates applicable product/price/condition and resolves unavailable selections rather than silently carrying them over. R02.
- **J2.3:** search matches the displayed language's reviewed offering; no results gives a way to revise query/reset filters. Active filters are visible; a short C1 menu can omit those controls. C1/C2; R01, R06.
- **J2.4:** C2 filters do not represent preferences and allergens as one universal suitability indicator. Unknown food records are explicitly separated in an exclusion result and remain discoverable for staff confirmation. R07.
- **J2.5:** a sold-out/withdrawn item and an expired composed menu have distinguishable states; details keep essentials visible and return to the reading location. A retained deep link recovers to relevant current content. C2/C3; R02, R03.
- **J2.6:** loss of connectivity enters the committed offline path for loaded content, with snapshot age/warning and retry/reconnect. Unloaded content has a clear unavailable state; stale content is never labelled verified live. C1–C3; R14; J10.

### J3 — Operator prepares and reviews content

Authorised venue/location entry → enter visit information → choose template or studio-delivered design → import/enter menu → review source and uncertainties → set variants/context/languages/food information → preview.

- **J3.1:** C1 can prepare a short menu without configuring areas, composed menus, multiple languages or filters; a draft/live distinction exists in both presentation routes. R01, R04, R10.
- **J3.2:** PDF/photo/structured-file examples show import-in-progress, partial/failed import and retry/manual correction. The source remains available; no unsupported content is invented or silently omitted. R06.
- **J3.3:** C2 source `24 / 34` without format labels stays an explicit unresolved mapping; the operator confirms labels/amounts before publishing that price structure. Duplicate/shared item choices show their effect. R02, R06.
- **J3.4:** missing food information may be published only as explicitly pending with staff direction; dietary/absence claims cannot be inferred. Changes to a variant/ingredient identify dependent fields/versions requiring review. C2/C3; R06, R07.
- **J3.5:** assistance is optional; operator can accept/edit/reject faithful text/translation/image improvement proposals. Provider/service failure preserves the original and permits manual work. Dish identity, ingredients and certifications are never invented. R06.
- **J3.6:** C3 preview can inspect date, service, area and language with applicable exception/translation state; a preview is never mistaken for the public live result. R03, R04.

### J4 — Operator publishes or schedules

Review selected changes → inspect publication scope/affected contexts/versions → resolve conflicts → publish now or choose explicit schedule → confirm result → inspect live content/history.

- **J4.1:** the chosen scope is clear before publishing. Required price/context conflicts must be resolved; partial reviewed publication never sweeps in unrelated drafts. Permission denial leaves public state unchanged. C2/C3; R02, R04.
- **J4.2:** C3 scheduling specifies venue-local date/time, content version and validity; an exception/conflicting schedule is visible. Editing a scheduled target prompts review/rescheduling, not an undocumented overwrite. R03, R04.
- **J4.3:** scheduled/cancelled/failed/superseded/live states are distinguishable. A failure retains the previous known live offering and gives a recovery action; retries must not produce a second conflicting publication. R04, R05.
- **J4.4:** unavailable/changed-underfoot data is shown as a conflict with current versus proposed value. The operator can revise the affected selection without losing unrelated draft work. C2/C3; R04.

### J5 — Operator changes availability during service

Open current service on mobile → select item → mark sold out with scope/end policy → see public result → undo/correct → review previous temporary states at next service.

- **J5.1:** C3 has an unrelated future price/text draft. Marking one item sold out changes only that live availability; draft values stay unpublished. Preview/result clearly identifies the item/context and allows undo. R04, R05.
- **J5.2:** insufficient permission, failed save or concurrent change has an explicit result; it never reports availability changed without evidence. Bulk action previews selected items/contexts. C1/C2; R04.
- **J5.3:** next-service review shows old temporary states and chosen restoration policy. The venue explicitly restores availability or keeps the exception; future menus do not automatically guarantee stock. R03, R05.
- **J5.4:** history shows the changed field/responsibility. Restoring older content previews current context and dependent translation/food states before publication; recovery cannot silently reactivate expired content. R05, R06.

### J6 — Operator changes ingredient or language content

Edit declared ingredient/variant → identify affected descriptions/allergens/glossary/translations → review factual consequences → publish selected coherent changes → inspect public fallback and maintenance queue.

- **J6.1:** changing a shared price/status updates its value across enabled languages; it does not require separate price copies. C3; R02, R06.
- **J6.2:** an ingredient change marks affected translation/food claims for review. If an affected language is not reviewed, the public version uses the explicit reviewed-language fallback or withholds the affected assertion/item per R06; unchanged current items are not silently removed. R06, R07.
- **J6.3:** glossary proposals preserve names/terms, while the reviewer verifies meaning. Published content does not claim a review that has not occurred. Register and staff output carry the same food-information state. R06, R07, R08.

### J7 — Operator distributes and refreshes outputs

Choose published context/date/language → generate paper/staff/QR output → review layout and version → distribute → change live content → identify affected output → regenerate and replace physical material.

- **J7.1:** C1/C2/C3 outputs handle no photos, long names, several formats/conditions and page breaks without losing essential prices or food-state meaning. A paper layout is not a mobile screenshot. R01, R02, R07, R08.
- **J7.2:** generated output shows its context/language and publication/version reference. A pending translation uses an explicit policy consistently; an internal draft output is visibly labelled draft. R06, R08.
- **J7.3:** after a price/ingredient change, the old generated document is identifiable as needing review/regeneration. The interface never suggests that old table sheets have changed; the operator replaces them. R08.
- **J7.4:** regenerating menu content retains the stable owned QR destination. QR context/destination is checked before distribution; a wrong/withdrawn target has recovery. Existing web/channel links are separated from uncommitted embed/sync. R03, R09, R10.

### J8 — Buyer receives service and retains control

Understand product/setup/template/bespoke/delegated options → agree commission and content responsibilities → provide materials → confirm restaurant facts → receive published reviewed content and training → make independent routine change → understand support and export/domain/service exit.

- **J8.1:** proposal distinguishes ongoing product, setup/template application, bespoke work, delegated changes and new design evolution. No price, revision allowance, urgent-response window or unlimited support is invented. R10; D3.
- **J8.2:** restaurant confirmation of content and responsible action is visible at handover. Both template/bespoke paths permit everyday price/text/photo/availability updates without a new design purchase. C1–C3; R10.
- **J8.3:** training/support instructions explain change/correction and escalation. A delegated change is recorded against the venue's authority, reviewed and confirmed, using the same publication controls. R04, R10.
- **J8.4:** export can return owned/reusable content and assets with explicit omissions/rights; the buyer understands custom-domain control, hosted-link consequences and ended services. No continuing hosting or transfer of a third-party website is implied. R10; D3.

### J9 — Operator interprets use and maintenance

Open maintenance/digital-use view → identify pending translation/import/temporary state/output → correct and verify → inspect period-labelled digital signals → decide whether further evidence is needed.

- **J9.1:** pending work points to affected content and a corrective action. Little traffic does not hide actionable content-maintenance signals. C1–C3; R05–R08.
- **J9.2:** consulted items and map/contact/booking-link clicks show period, observable context/source and measurement limits. Missing collection/unknown attribution is explicit; views are not customers, bookings or sales. R11.
- **J9.3:** optional search/filter signals can surface no-result searches without identifying individual diners. Connected launch outcomes require real source/window data; change-comparison reports observed metrics with limitations, never unsupported causality. R09, R11, R16; J13/J14.

### J10 — Diner compares choices, views video and continues offline

Save options without account → compare actual variant/context/conditions → view optional venue video → lose connectivity → consult loaded snapshot → reconnect and reconcile changes.

- **J10.1:** save/remove/reset options; show selected variant/context and current known price/food state. The list is explicitly personal and cannot be submitted as an order. A changed/withdrawn/sold-out option is identified rather than silently remaining available. C2/C3; R02, R12.
- **J10.2:** video playback is optional; essentials remain readable without playback. Text/captions, unavailable/failed video and a changed/withdrawn video are represented. Operator can add, review, replace and remove rights-cleared video using ordinary draft/publication controls. R04, R12.
- **J10.3:** offline reading uses actually loaded snapshot content, version/time and stale-state warning; missing items/translations/media are explicit. Pending food information cannot disappear or become assured by caching. R07, R14.
- **J10.4:** reconnect adopts one coherent new publication, flags changed saved-option price/availability/context and permits removal/reselection. Offline edits are not silently treated as published operator changes. R04, R14.

### J11 — Operator maintains declared nutritional information

Record source and portion/unit basis → enter reviewed or pending values by relevant variant → publish → diner inspects meaning → change ingredients/portion → flag values for review.

- **J11.1:** C2/C3 include declared values and an unknown record. Diner can distinguish them, read their basis and consult staff; no invented inference from recipe/name. R07, R13.
- **J11.2:** operator reviews source/units/portion and relevant variant before publishing; ingredient/portion changes flag affected nutrition and translations. Unknown values stay explicit in public, print, offline and display outputs. R06–R08, R13–R15.

### J12 — Operator publishes and monitors an in-venue display

Choose reviewed offering/context/language and display layout → preview representative device → publish/refresh dedicated output → change live offering → observe revision → lose/recover connectivity.

- **J12.1:** a read-only display example exposes context, readable prices/conditions and reviewed food/nutrition states using the same source as public/print output. Routine content changes do not require another bespoke design commission. R02, R10, R15.
- **J12.2:** draft content remains private; refresh/update shows the published revision. Stale/unavailable display content has an explicit state, with reconnect to a coherent version rather than endless obsolete data presented as current. R04, R14, R15.
- **J12.3:** representative device/viewing-distance/content constraints are recorded when available. Browser/output design can proceed with labelled examples; no physical-device fleet, remote management or hardware compatibility is falsely claimed. R15.

### J13 — Operator compares a content change

Choose concrete question/change/version and digital metric → inspect periods and known exposure → compare observed values → see insufficient/missing-data limits → record interpretation.

- **J13.1:** shows question, change/version, period, observed count/rate basis where known and missing collection. A selected interval with inadequate data displays insufficiency; it does not fabricate a positive result. R11, R16.
- **J13.2:** before/after differences disclose contextual/exposure differences and do not prove sales or causality. Operator can revise comparison periods/question without changing historical measurements. R11, R16.

### J14 — Operator connects a supported source or destination

Identify real system/channel and permitted data → obtain authorised access → map field ownership/context → review transfer/result → inspect public/owned/external states → handle rejection/conflict/retry/revocation.

- **J14.1:** cover the six matrix connection rows: booking destination, operational data, authoritative external change source, existing website embed, external channel distribution and confirmed outcome attribution. Each needs a real target; an unspecified connection is recorded as a delivery dependency, not a finished generic connector. R09.
- **J14.2:** distinguish link-only routing from embedded/live/confirmed data behaviour. Actual ownership, last result, pending/failed transfer and authorisation loss are visible; a failed destination does not claim cross-channel success. R04, R09.
- **J14.3:** a connected confirmed outcome requires an actual permitted data source and defensible attribution; retain future-module boundaries. Target selection/access is unresolved and must be addressed for launch, not silently postponed. R09, R11.

### J15 — Registered diner manages preferences and receives recommendations

Browse publicly → voluntarily register/sign in → manage explicit preferences → see personalised current choices → revise preferences/context → inspect recommendation detail/food state → sign out or use recovery/account controls.

- **J15.1:** anonymous users can continue reading the same menu without registering. The personalisation entry explains its account requirement and allows returning to ordinary consultation; venue-selected recommendations remain available. R01, R17.
- **J15.2:** prototype registration/sign-in, verification-required where the selected method requires it, failed/expired/recovery and sign-out states. A registered but signed-out diner cannot access another person's private profile or personalised result. Guest identity never grants restaurant-management permissions. R17.
- **J15.3:** signed-in users with no preferences/history receive an honest empty-input/fallback state. Proposed initial preferences are supplied deliberately and can be reviewed/changed/reset; no visits, purchases or tastes are fabricated. Input selection and algorithm remain design/M2 decisions. R11, R17.
- **J15.4:** recommendations draw from the actual published venue/area/service/variant and current known availability. Show relevant preference reasons/limits; a changed/withdrawn item is reconciled, not recommended with an old price. Missing food data remains explicit and never becomes a personal safety guarantee. C2/C3; R02, R07, R17.
- **J15.5:** no matching items, unavailable personalisation or expired session has a recovery path to ordinary browsing and applicable venue recommendations. Signing out clears or restricts private personalisation state; offline/shared-device cases do not reveal another user's preferences. R14, R17.
- **J15.6:** show preference/account controls and the necessary account recovery/removal path. Exact identity scope, access/deletion/retention effects and promotion choices require M2 review; registration does not silently subscribe the diner to campaigns. No account implementation or compliance result is claimed. R17.

## 4. Coverage map

Ranges below enumerate all accepted source-row capabilities. Connection target/access dependencies stay explicit; only audio/3D media subparts are deferred.

| Journeys / boundaries | Capability coverage |
| --- | --- |
| J1 and J8: venue/identity and commissioning | B1.01–B1.08 |
| J1.4/J14 booking connection | B1.09 |
| J1–J5: catalogue, contextual offer and availability | B2.01–B2.09 |
| J14 operational source | B2.10 |
| J2: browsing, search, food detail and deep links | B3.01–B3.08, B3.10 |
| J10 personal list/video; audio/3D subparts explicitly deferred | B3.09, B3.11 |
| J3–J6: import, editing, publication, review and recovery | B4.01–B4.11 |
| J14 source-of-change ownership | B4.12 |
| J1.4/J6/J7: languages and food information | B5.01–B5.08 |
| J11 nutritional-source/review cases | B5.09 |
| J1/J2/J7: stable intentional access and outputs | B6.01–B6.06 |
| J7.4/J14 embed/external sync | B6.07–B6.08 |
| J12 dedicated display output | B6.09 |
| J2.6/J10 offline/reconnect | B6.10 |
| J8.4 export/exit | B6.11 |
| J9 digital-use signals | B7.01–B7.05 |
| J9.3/J14 confirmed results | B7.06 |
| J9.1 maintenance and J13 limited observed comparison | B7.07–B7.08 |
| J8 service and delegation | B7.09–B7.10 |

Supplementary prose coverage: **S1 (§3/L55)** is the excluded restaurant page builder; J3.1/J8.2 retain autonomous content editing and studio design. **S2 (§5/L120)** is accepted registered-diner personalisation, covered by R17/J15. This separate mapping does not change the 72 parent-row coverage count.

## 5. Proposed review method and closure evidence

First perform author scenario walkthroughs across C1–C3; preserve paths, inputs, expected observable result and open questions. Independent Quality reviews critical transitions, comprehension and accessibility design; Engineering reviews feasibility and future verification needs. These activities have not yet occurred with prototypes.

When real diners/operators are accessible, use concrete tasks: find terrace price/conditions, understand pending food information, prepare a daily menu, mark sold out with another draft present, change an ingredient/translation, refresh print and make a routine bespoke-design edit. Record completion, misunderstandings, errors, assistance and recovery without assuming target success rates, time savings or willingness to pay. Fictional walkthroughs and guided demos remain separately labelled.

Block affected design closure when a scenario shows a wrong price/context, unintended public draft, false food assurance, hidden stale factual translation, unrecoverable critical action or a commission-dependent routine edit. Record other issues with impact, responsibility and proposed treatment. M1 closure requires the actual completed reviews/tests with limitations; this criteria document alone does not satisfy it.

Current descriptive evidence: [C1–C3](../design/m1-connected-journey.md) and [J10–J15](../design/m1-extended-journeys.md), in the owner's selected Markdown medium. [ADR-0010](../adr/0010-diner-account-and-display-recovery.md) records the 2 October selections: shared Valiris diner identity, venue-scoped tastes/diet, email/password and withdrawal of unconfirmed display prices/availability. Earlier open design questions in R17/J15 are refined by these selections; exact matching is proposed and actual provider/session/data lifecycle contracts remain M2 work. No criterion or coverage row above is removed or weakened.

Next checkpoint: independent/technical review and remaining G2 design/interaction evidence under [M1 #5](https://github.com/yaboula/valiris-restaurants/issues/5), using the [M1 briefs](m1-design-briefs.md). M0 is integrated and closed. D1/D2 are resolved through ADR-0008 and D4/D5 through [ADR-0009](../adr/0009-studio-design-and-registered-diner-personalisation.md). Real content/participants, device, six connection targets/access and M2 technical/privacy contracts remain dependencies. Dates/spending are uncommitted; descriptive coverage alone does not meet M1's original evidence requirements.

Further descriptive evidence: [content preparation and maintenance](../design/m1-content-preparation.md#9-traceability-and-author-verification) traces all six J3 criteria and the affected parts of J4.1/J4.4, J5.2/J5.4, J6.1–J6.3 and J7.3. [ADR-0011](../adr/0011-shared-menu-content-and-contextual-maintenance.md) records the owner's principal shared-content direction; no source criterion above is changed. The 27 CP state descriptions, 24 fresh author contrasts and 36 previous V/Q rechecks do not constitute actual import, translation/image review, enforced shared publication, independent quality or M1 closure. Real inputs/rights/providers and technical contracts remain explicit dependencies.

Further J8/J9 evidence: [service, continuity and maintenance](../design/m1-service-and-maintenance.md#7-criteria-capabilities-and-connected-walkthroughs) traces the seven unchanged criteria J8.1–J8.4 and J9.1–J9.3 to 22 descriptive states, 14 affected capability rows and connected paths. [ADR-0012](../adr/0012-confirm-delegated-updates-per-assignment.md) records owner-selected per-assignment delegated confirmation; actual service terms, authority/export/domain/measurement contracts and independent/real/interaction evidence remain pending. Twenty-six author contrasts and all 64 prior V/Q/PC/DS rows are read against new paths, not executed product tests. External G4-01 scoped closure does not approve these states; G4-J15-01 now has a [scoped descriptive correction](../design/m1-extended-journeys.md#12-g4-j15-01-category-lifecycle-correction-and-focused-recheck) and six LC contrasts, refining Q17/J15.3/J15.4 evidence without altering those source criteria; independent G4/G1 recheck remains pending. No criteria, launch treatment or original M1 closure requirement changes.
