# M0 launch capability commitment

Version 0.3 · 1 October 2026 · Accountable owner: Yahya.

**Status: launch scope accepted by owner instruction on 1 October 2026; behaviour design and delivery dependencies remain open.** The owner approved D1 and rejected the D2 deferral recommendation: deliver the D2 capabilities in the first launch, deferring only standalone audio explanations and 3D. See [ADR-0008](../adr/0008-first-launch-capability-commitment.md). Scope acceptance does not establish implementation, provider access, completed review or M0 closure.

## 1. Sources, scope and reading

Use the [roadmap](../project/roadmap.md), [executive brief](../project/m0-execution-brief.md), [functional definition](../research/storefront-digital-menu/functional-definition/functional-definition.es.md) dated 30 September 2026, and retained [language decision](../adr/0005-repository-and-product-language.md). The original references are unchanged. This commitment covers all **72 table capabilities** in the definition's seven blocks. `B2.03 / L71`, for example, is block 2, third capability, line 71 of that source version; translated names retain the same scope. Rules and scenarios in the source prose are carried into [journeys and criteria](m0-journeys-and-criteria.md), not counted as extra table rows.

Preserved directions: Storefront + Digital Menu first, necessary Core, templates and paid bespoke studio design, autonomous everyday maintenance, no committed dates, costs examined for concrete spending decisions. Ordering, payments, POS, delivery and invoicing remain outside this module. Bookings, reviews, loyalty, reactivation and WhatsApp remain future or connected responsibilities. No general competitive research is reopened.

Treatment and approval are independent:

| Treatment | Meaning |
| --- | --- |
| Included | Accepted common launch capability, including its management and correction |
| Configurable | Accepted available-at-launch capability enabled when the restaurant needs it; not postponed |
| Later | Only standalone audio and 3D subparts are deferred by the current decision; no scheduled phase |
| Connection-dependent | Accepted launch connection capability requiring a supported destination/source, access, data and field/failure rules; unresolved dependencies do not move it to a later release |
| Pending | Founder choice required before an affected commitment; recommendation and alternatives recorded |
| Excluded | Explicitly rejected capability; used for the supplementary restaurant page builder, not a later delivery promise |

**Approval `A` means accepted launch scope**, not approved implementation/design or verified data. D1 accepts the original 60 included/configurable rows; D2 accepts the expanded capabilities and connections for launch, with audio/3D deferred. Service packaging (`D3`) remains open until delivery evidence supports terms. Connection target/access decisions remain necessary. Responsibility names identify delivery disciplines, not staffed teams; G1 consolidates and Yahya decides material commitments.

Coverage summary: **36 included, 30 configurable, 6 connection-dependent** across the 72 source rows, all accepted for launch. B3.11 is split into launch video and two explicitly deferred subparts below; those subparts do not inflate the 72-source-row count. [ADR-0009](../adr/0009-studio-design-and-registered-diner-personalisation.md) resolves both supplementary prose ideas: exclude the free-form restaurant page builder; include personalised recommendations for registered, authenticated diners with the necessary account/profile journeys.

## 2. Complete capability matrix

### Block 1 — Presence, identity and personalisation

Source: definition §3, capability table. Shared quality must hold for both design routes.

| Origin | Capability | Actor / task | Treatment | Rationale and dependencies | Principal responsibility | Approval / decision |
| --- | --- | --- | --- | --- | --- | --- |
| B1.01 / L41 | Public venue page | Diner: recognise venue before visiting | Included | Core product entry; maintained venue content and direct menu access | Engineering + Design | A / D1 |
| B1.02 / L42 | Visit information | Diner: plan visit; operator: correct details | Included | Address/contact/local and kitchen hours/exceptions need one maintained source; R03 | Core + Engineering | A / D1 |
| B1.03 / L43 | Venue attributes | Diner: understand relevant facilities | Configurable | Show only restaurant-declared attributes, with explanations for ambiguous labels | Product + Design | A / D1 |
| B1.04 / L44 | Story and editorial content | Buyer: express identity; operator: maintain story | Configurable | Useful where authentic material exists; simple publishable content, not a separate publishing business | Design + Engineering | A / D1 |
| B1.05 / L45 | Visual identity | Buyer/diner: recognise business | Included | Consistent presence/menu identity; usable with limited images; R01 | Design | A / D1 |
| B1.06 / L46 | Base templates | Buyer: obtain usable presentation | Included | Studio-curated presentations; content and routine updates remain common; template count is not fixed | Design + Service | A / D1 |
| B1.07 / L47 | Bespoke studio design | Buyer: purchase distinct representation | Configurable | Retain paid design path; defined commission/revisions and content autonomy; R10 | Service + Design | A / D1, D3 |
| B1.08 / L48 | Domain, share preview and discovery | Diner: recognise/reach venue; buyer: own presence | Included | Stable hosted address, titles and link preview; configurable custom domain subject to ownership/DNS/exit conditions; no ranking promise | Engineering + SEO + Service | A / D1, D3 |
| B1.09 / L49 | Booking connection | Diner: continue to a booking destination | Connection-dependent | External booking link may be configured without implementing booking; live availability/confirmation needs an explicit supported connection; R09 | Engineering + Product | A / D2 |

### Block 2 — Offering, formats and context

Source: definition §4. Configuration changes complexity, not basic quality.

| Origin | Capability | Actor / task | Treatment | Rationale and dependencies | Principal responsibility | Approval / decision |
| --- | --- | --- | --- | --- | --- | --- |
| B2.01 / L69 | Products and categories | Operator: maintain offering; diner: read it | Included | Shared catalogue, optional photos, clear ordering/reuse; public content has an editable counterpart | Core + Engineering | A / D1 |
| B2.02 / L70 | Formats and variants | Diner: compare portions/prices | Configurable | Preserve real formats and their prices; do not infer names from ambiguous imports; R02 | Product + Engineering | A / D1 |
| B2.03 / L71 | Supplements and conditions | Diner: understand price/choice conditions | Configurable | Minimum people, units, weight and add-ons must remain visible at choice; supports R02 | Product + Design | A / D1 |
| B2.04 / L72 | Composed menus | Operator/diner: prepare and understand daily/set menus | Configurable | Explicit price, inclusions, choices, supplements and validity; not order processing | Product + Engineering | A / D1 |
| B2.05 / L73 | Multiple menus | Diner: choose relevant offering | Configurable | Breakfast/drinks/wine/seasonal sets reuse catalogue without compulsory setup for a short café menu | Engineering + Design | A / D1 |
| B2.06 / L74 | Service/date scheduling | Operator: prepare future offering | Configurable | Planned consultation and timed publication must agree; venue timezone/conflicts/preview; R03, R04 | Product + Engineering | A / D1 |
| B2.07 / L75 | Area or location offering | Diner/operator: distinguish actual differences | Configurable | Explicit terrace/venue context with editable differences; Core identifies location and authorised access; no booking/table model | Core + Engineering | A / D1 |
| B2.08 / L76 | Service-time availability | Operator: report sold-out; diner: understand status | Included | Immediate scoped change, visible result/undo, chosen carry-over policy; R04, R05 | Engineering | A / D1 |
| B2.09 / L77 | Manual exception | Operator: override closure/withdrawal | Included | Explicit effect, end and precedence; preview conflicts rather than silently choosing; R03, R05 | Product + Engineering | A / D1 |
| B2.10 / L78 | Operational-system data | Operator: reuse trusted catalogue/status | Connection-dependent | Require authorised field ownership/mapping and failure rules; manual/import path remains usable; R09 | Engineering | A / D2 |

### Block 3 — Find, understand and choose

Source: definition §5. Consultation does not require an account or imply an order.

| Origin | Capability | Actor / task | Treatment | Rationale and dependencies | Principal responsibility | Approval / decision |
| --- | --- | --- | --- | --- | --- | --- |
| B3.01 / L100 | Category navigation | Diner: browse and return | Included | Core consultation; retain place and essential context; R01 | Design + Engineering | A / D1 |
| B3.02 / L101 | Search | Diner: locate a product | Configurable | Long menus benefit; language-aware maintained text, empty-result recovery; unnecessary controls hidden for short menus | Design + Engineering | A / D1 |
| B3.03 / L102 | Useful filters | Diner: narrow a real offering | Configurable | Restaurant-declared dimensions, explicit active filters/reset; missing food data cannot imply safe exclusion; R07 | Product + Design | A / D1 |
| B3.04 / L103 | Allergen consultation | Diner: inspect declared information | Included | Declared versus pending information, access to staff, no inferred suitability; R07 | Product + Engineering | A / D1 |
| B3.05 / L104 | Gradual detail | Diner: compare then inspect | Included | Essential prices/conditions stay visible; additional detail preserves reading position | Design | A / D1 |
| B3.06 / L105 | Dish explanations | Diner: understand unfamiliar item | Configurable | Useful restaurant-supplied preparation/size/context; preserve names and reviewed translations | Content + Service | A / D1 |
| B3.07 / L106 | Restaurant highlights | Operator: promote selected offering | Configurable | Explicitly managed specials; do not claim best-selling without evidence or obstruct browsing | Design + Engineering | A / D1 |
| B3.08 / L107 | Dish/menu deep links | Diner: share or return to offering | Included | Stable content identity; withdrawn/expired target has clear recovery; R03 | Engineering + SEO | A / D1 |
| B3.09 / L108 | Personal comparison list | Diner: remember choices | Configurable | Launch comparison/saved options without account or order semantics; invalid/changed/contextual entries must update honestly; J10 | Design + Engineering | A / D2 |
| B3.10 / L109 | Pairings/product relations | Diner: use venue recommendations | Configurable | Editorial relationships maintained by venue; no individual profiling required | Product + Engineering | A / D1 |
| B3.11 / L110 | Video explanation; audio/3D split below | Diner: understand preparation/portion | Configurable | Launch reviewed venue video with rights, accessible text/captions and manual playback; media failure preserves text/price/food information; J10 | Design + Engineering + Service | A / D2 |

### Block 4 — Prepare, update and publish

Source: definition §6. Review and urgent control are part of the product, not optional studio labour.

| Origin | Capability | Actor / task | Treatment | Rationale and dependencies | Principal responsibility | Approval / decision |
| --- | --- | --- | --- | --- | --- | --- |
| B4.01 / L130 | Menu import | Operator/Service: prepare existing material | Included | PDF, photos and structured spreadsheet/data sources produce reviewable proposals; errors/unsupported files retained for correction, no silent completion; R06 | Engineering + Service | A / D1 |
| B4.02 / L131 | Import review | Operator: verify imported prices/content | Included | Original beside proposal; ambiguous formats, omissions and food fields explicit; restaurant confirms publication; R06, R07 | Product + Design | A / D1 |
| B4.03 / L132 | Mobile editing | Operator: make everyday changes | Included | Routine price/text/photo/availability updates work without designer intervention; R04, R10 | Design + Engineering | A / D1 |
| B4.04 / L133 | Bulk editing and duplication | Operator: update/reuse content | Included | Preview selected scope, distinguish shared item versus copy, recover mistakes; concurrent edits must not silently overwrite | Engineering | A / D1 |
| B4.05 / L134 | Drafts and preview | Operator: check public consequences | Included | Draft/live separation; contextual/date/language preview clearly labelled; R03, R04 | Engineering + Design | A / D1 |
| B4.06 / L135 | Controlled publication | Operator: publish chosen changes | Included | Selected scope and authorised action; urgent status does not publish unrelated drafts; R04 | Engineering | A / D1 |
| B4.07 / L136 | Scheduled publication | Operator: prepare next menu/prices | Configurable | Explicit target content/time/context; cancellation, superseded draft and failed execution states; R03, R04 | Engineering | A / D1 |
| B4.08 / L137 | History and recovery | Operator: understand/correct mistake | Included | Record actor/change; recovery creates a reviewed correction, not accidental reactivation of old states; R05 | Core + Engineering | A / D1 |
| B4.09 / L138 | Team responsibilities | Buyer/operator: separate actions | Configurable | Core permissions distinguish availability/edit/publish; server-side enforcement later, no compulsory complex approval for small venues | Core + Engineering | A / D1 |
| B4.10 / L139 | Text/image assistance | Operator/Service: prepare faithful content | Configurable | Reviewed descriptions/translations and faithful image improvements; never invent ingredients, origin/certification or served dishes; provider/cost choice in M2 | Engineering + Content | A / D1 |
| B4.11 / L140 | Affected-content review | Operator: maintain coherent changes | Included | Ingredient/format changes identify dependent text, food fields and translations before publication; R06, R07 | Product + Engineering | A / D1 |
| B4.12 / L141 | External source of changes | Operator: resolve source ownership/conflicts | Connection-dependent | Define editable fields, inbound changes and conflict resolution before claiming an authoritative external source; R09 | Engineering + Product | A / D2 |

### Block 5 — Languages, information and trust

Source: definition §7. ADR-0005 remains active: guest surfaces ES/EN/FR/DE, Spanish-first management then English, preparation for Arabic/RTL. A restaurant enables reviewed content languages it can maintain; guest interface language support does not fabricate translated venue content.

| Origin | Capability | Actor / task | Treatment | Rationale and dependencies | Principal responsibility | Approval / decision |
| --- | --- | --- | --- | --- | --- | --- |
| B5.01 / L163 | Presence/menu languages | Diner: retain chosen language | Configurable | Supported interface and reviewed content; keep selection through contexts; explicit missing version, Arabic readiness without claiming translated launch content; R06 | Engineering + Content | A / D1 |
| B5.02 / L164 | Assisted translation and review | Operator: maintain offered languages | Included | Applies where languages are offered; human restaurant/content review before publication; preserve factual meaning and shared values | Content + Engineering | A / D1 |
| B5.03 / L165 | Venue glossary | Operator/Service: keep terms consistent | Configurable | Reusable names/ingredients/tone for maintained translations; supports ongoing rather than one-off translation | Content + Service | A / D1 |
| B5.04 / L166 | Shared-data consistency | Operator/diner: trust same prices/status | Included | Price, format, availability and validity are not separately edited per translation; R02, R06 | Core + Engineering | A / D1 |
| B5.05 / L167 | Translation update pending | Diner/operator: recognise affected version | Included | Block stale factual claims; show explicit reviewed-language fallback or temporarily withhold affected content; R06 | Product + Engineering | A / D1 |
| B5.06 / L168 | Ingredients/allergens by variant | Operator/diner: distinguish real differences | Included | Record declared information and review state at relevant format/variant level; no inference from dish name; R07 | Product + Engineering | A / D1 |
| B5.07 / L169 | Venue statements | Diner: distinguish declaration/adaptation | Included | Ingredients, preparation warnings and adaptations on request have distinct meaning; confirm with staff when needed | Content + Product | A / D1 |
| B5.08 / L170 | Staff register/output | Operator: consult reviewed food information | Included | Maintain accessible internal record and relevant generated output; do not reduce information to public icons; R07, R08 | Engineering + Service | A / D1 |
| B5.09 / L171 | Nutritional information | Diner: inspect supported values | Configurable | Launch declared values with source, portion/unit basis and reviewed/pending state; restaurant maintains them, no invented calculations or health guarantee; J11 | Engineering + Service | A / D2 |

### Block 6 — Access, print and distribution

Source: definition §8. Generated artefacts and external publication must not be confused with the live source.

| Origin | Capability | Actor / task | Treatment | Rationale and dependencies | Principal responsibility | Approval / decision |
| --- | --- | --- | --- | --- | --- | --- |
| B6.01 / L191 | Stable link/QR | Diner/operator: keep access after edits | Included | Same owned destination after content changes; end-of-service conditions explicit; R10 | Engineering + Service | A / D1 |
| B6.02 / L192 | Intent-based entry | Diner: discover venue or open menu directly | Included | Respect link/QR intent, explain contextual entry and allow change; no compulsory promotional gateway | Design + Engineering | A / D1 |
| B6.03 / L193 | Account-free consultation | Diner: read without registration/install | Included | Public task does not require individual identification; unavailable service has a recoverable state; R01 | Engineering + Design | A / D1 |
| B6.04 / L194 | Sharing materials | Operator: distribute branded access | Included | Downloadable QR/links and legible physical supports; check destination/context before printing | Design + Service | A / D1 |
| B6.05 / L195 | Printable formats | Operator/diner: use appropriate paper menu | Included | Composed menu/daily/staff output from reviewed content, dedicated paper layout and version/date; R08 | Design + Engineering | A / D1 |
| B6.06 / L196 | Language/use output variants | Operator: distribute right reviewed version | Configurable | Menu/staff/language-specific output uses same content and explicit fallback/pending rules | Design + Engineering | A / D1 |
| B6.07 / L197 | Existing website presence | Buyer: keep useful existing presence | Connection-dependent | Link to owned menu works within B6.01/02; embedding/reusing host chrome needs verified website control/accessibility/update behaviour | Engineering + SEO | A / D2 |
| B6.08 / L198 | External channels | Operator: distribute links/data | Connection-dependent | Sharing links supported by B6.04; automatic data delivery requires tested destination, authorisation and failure visibility; R09 | Engineering + Service | A / D2 |
| B6.09 / L199 | In-venue screens/displays | Operator: reuse content in room | Configurable | Launch dedicated display output from maintained content, context/language/layout settings, visible revision/failure and safe reconnect; representative target device remains to identify; J12 | Design + Engineering | A / D2 |
| B6.10 / L200 | Interrupted-connectivity consultation | Diner: read previously loaded content | Configurable | Launch previously loaded snapshot with version/age/offline disclosure, unavailable-content state and coherent reconnect; never present stale price/food/status as verified live; J10 | Design + Engineering | A / D2 |
| B6.11 / L201 | Export and continuity | Buyer: retrieve content and understand exit | Included | Usable structured content/assets where rights allow; explicit domain/link/service conditions, not a promise to operate after termination; R10 | Engineering + Service | A / D1, D3 |

### Block 7 — Measurement and commercial offer

Source: definition §9. Measurement supports decisions without inventing sales attribution.

| Origin | Capability | Actor / task | Treatment | Rationale and dependencies | Principal responsibility | Approval / decision |
| --- | --- | --- | --- | --- | --- | --- |
| B7.01 / L221 | Presence/menu consultations | Operator: understand digital use | Included | Period-labelled consultation counts with measurement limitations; aggregate browsing measurement is separate from optional registered-diner profiles; no invented individual identity; R11 | Engineering + Product | A / D1 |
| B7.02 / L222 | Access origin | Operator: compare identified entry routes | Configurable | Declared QR/link/campaign tags only where observable; unknown origin stays unknown | Engineering + Commercial | A / D1 |
| B7.03 / L223 | Category/search/filter use | Operator: identify browsing friction | Configurable | Useful unanswered-search and navigation signals, not fabricated activity; privacy/data scope reviewed in M2 | Engineering + Product | A / D1 |
| B7.04 / L224 | Dish interest | Operator: interpret digital attention | Configurable | Views with period/context and limitations; no best-selling/physical-visit inference without data | Engineering + Product | A / D1 |
| B7.05 / L225 | Visit-intent actions | Operator: see map/contact/booking-link actions | Included | Clicks labelled as clicks; external confirmation absent unless a supported connection supplies it | Engineering + Commercial | A / D1 |
| B7.06 / L226 | Other-module outcomes | Operator: relate confirmed connected result | Connection-dependent | Real result data and defensible attribution window/source required; future module is not implicitly committed | Product + Engineering | A / D2 |
| B7.07 / L227 | Quality/maintenance signals | Operator: correct stale/pending content | Included | Actionable translation/import/status/output review queues even with little traffic; R05–R08 | Engineering + Service | A / D1 |
| B7.08 / L228 | Change comparison | Operator: evaluate improvement | Configurable | Launch explicit question/version/period/metric comparison with sample/exposure limits and insufficient-data state; observed differences do not establish causality or sales; J13 | Product + Engineering | A / D2 |
| B7.09 / L229 | Onboarding/design service | Buyer: understand purchased delivery | Included | Define intake, confirmation, template/bespoke path, handover and support/exit; test effort rather than invent rates; R10 | Service + Commercial | A / D1, D3 |
| B7.10 / L230 | Delegated updates | Buyer: choose maintained service | Configurable | Retain optional studio service with change types, volume, hours and escalation agreed separately; autonomy remains; no unlimited support promise | Service + Commercial | A / D1, D3 |

### B3.11 media subparts

| Origin subpart | Capability | Treatment | Approval / reference |
| --- | --- | --- | --- |
| B3.11-AUDIO / L110 | Standalone audio explanation | Later | Explicit owner deferral / D2, ADR-0008 |
| B3.11-3D / L110 | 3D presentation | Later | Explicit owner deferral / D2, ADR-0008 |

Video accessibility remains part of the launch behaviour; audio-only presentation and 3D are separate deferred formats. No automatic playback or fabricated venue content is implied.

## 3. Scope boundaries carried from prose

The owner resolved the two prose-only ideas on 1 October 2026 through ADR-0009. They are tracked separately from the 72 table rows; the rejected builder is excluded, not deferred.

| Origin | Capability | Actor / task | Treatment | Rationale and dependencies | Principal responsibility | Approval / decision |
| --- | --- | --- | --- | --- | --- | --- |
| S1 / §3, L55 | Free-form restaurant page builder | Restaurant: author page composition | Excluded | Owner rejected restaurant-authored design. Keep studio templates/bespoke composition and autonomous content/allowed brand controls; J3/J8 | Design + Service | Rejected / D4, ADR-0009 |
| S2 / §5, L120 | Registered-diner personalised recommendations | Registered diner: find relevant current choices | Configurable | Accepted launch personalisation only when registered and authenticated; requires necessary account/session/preference controls, current published catalogue and honest empty/error fallback; J15, R17 | Core + Product + Engineering | A / D5, ADR-0009 |

Necessary Core supports establishments/locations, shared content, authorised member actions, hours/exceptions, catalogue/languages and traceability/recovery, plus sufficient registered-diner identity/session/preference access for S2. Detailed structure, cross-venue identity boundaries, retention/deletion rules and providers belong to M2. No campaign audience, loyalty visits, reservations, payments or ordering are added merely for future modules. Guest-account registration does not require registration for ordinary menu consultation.

Import/file handling, translation providers, measurement, custom domains and external connections need focused Engineering/Quality/Service input, recorded in the [design briefs](m1-design-briefs.md). No provider, cost, legal certification, cross-channel result or performance threshold is assumed to have been verified.

## 4. Owner decision register

| Decision | Recommendation | Alternative and consequence | Status / affected work |
| --- | --- | --- | --- |
| D1 — First commercial included/configurable commitment | Owner approved the original 60 included/configurable rows on 1 October 2026. | The prior smaller/changed-coverage option was not chosen. Any subsequent material reduction requires a new owner decision. | Accepted launch scope / ADR-0008. Design/technical/service details still require their reviews. |
| D2 — Opportunities, display and connection boundary | Owner rejected deferral and instructed first-launch delivery; only standalone audio and 3D may wait. Personal list, video, nutrition, offline reading, comparison and displays are configurable at launch; six connection capabilities remain launch responsibilities with explicit access/data dependencies. | The original five-opportunity/display deferral is rejected. A connection cannot be declared working without a real supported target/access; missing dependencies must be resolved, not recategorised as later. | Accepted with owner amendment / ADR-0008. Prepare design now; target/device/access choices remain open. |
| D3 — Detailed commercial/service obligations | Retain template and paid bespoke design, optional delegated updates and configurable custom-domain path. Define scope/revisions, content confirmation, support/escalation and domain/export exit before quoting; set package limits/prices from concrete delivery effort. | Commit a particular bespoke package, update window or destination obligation now only after its boundaries/costs are reviewable. Undefined unlimited support would create unsupported obligations. | Detailed terms remain pending for M5/M6 evidence and concrete spending proposals. Does not block M1 common journeys; blocks final commercial promises. |
| D4 — Restaurant content versus design | Owner accepts autonomous content updates and rejects restaurant-designed pages. Valiris retains template/bespoke composition. | A free-form restaurant builder was not chosen; permitted content/brand controls are still designed in M1. | Resolved / ADR-0009. Preserve routine independence in both visual routes. |
| D5 — Registered-diner personalisation | Owner accepts personalised recommendations when the diner has a registered account; require authenticated access to the personal profile. | Venue recommendations still work anonymously. Anonymous individual profiling and mandatory registration for consultation were not chosen. | Accepted launch scope / ADR-0009. Account/profile/recommendation design and technical rules remain to specify. |

D1/D2/D4/D5 are resolved and need no repeat approval. D3 retains concrete commercial decisions for when evidence exists. Identify connection targets/access, display/content inputs and sufficient registered-diner account/recommendation rules during design/M2 preparation. Participant access remains unconfirmed; this does not permit invented validation.

## 5. Review and continuity

Author checks cover source-row mapping and separate scope approval, public/operator/service criteria and new D2 journeys. Independent Quality/Engineering/SEO/Service review and actual user tests remain requested, not completed.

Next: follow the authorised integration/closure record in the [M0 closeout](../project/m0-closeout.md), then design accepted scope including J15, resolve delivery dependencies at their recorded checkpoints and document actual reviews. [GitHub #3](https://github.com/yaboula/valiris-restaurants/issues/3), [#6](https://github.com/yaboula/valiris-restaurants/issues/6) and [Linear YAH-5](https://linear.app/valiris/issue/YAH-5/m0-consolidate-launch-commitment-and-m1-design-briefs) record preparation completion; [#15](https://github.com/yaboula/valiris-restaurants/issues/15) continues the parallel commercial work. M0 completion does not satisfy the later delivery checkpoints.
