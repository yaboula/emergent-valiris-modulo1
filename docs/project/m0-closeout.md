# M0 closeout and M1 handover

Version 0.3 · 1 October 2026 · Accountable owner: Yahya.

**Status: M0 integrated and closed on 1 October 2026; G2 starts [M1 #5](https://github.com/yaboula/valiris-restaurants/issues/5).** The [M0 milestone](https://github.com/yaboula/valiris-restaurants/milestone/1) has zero open items; #1/#2/#3/#6/#9/#17 are closed and Linear YAH-5 is Done. All five PRs are integrated; section 6 preserves their sequence and SHAs as completed evidence. This record checks the existing exit criteria and assigns outstanding delivery work to its actual checkpoint. Subsequent milestone evidence is not claimed complete.

## 1. Committed product and evidence boundary

First commercial release: Storefront + Digital Menu, necessary Core and onboarding/design/support. Target context remains independent restaurants and cafés in Spain. The product helps diners understand an actual offering and operators prepare, review, publish and maintain it; QR is an entry route. The [roadmap](roadmap.md) controls milestone boundaries.

The [capability commitment](../product/m0-capability-matrix.md) records all 72 source table rows: 36 Included, 30 Configurable and six Connection-dependent, accepted by D1/D2. Standalone audio and 3D are deferred subparts. D4 excludes restaurant-authored page composition while retaining autonomous content updates and studio template/bespoke design. D5 adds recommendations for authenticated registered diners; ordinary consultation remains account-free. [ADR-0008](../adr/0008-first-launch-capability-commitment.md) and [ADR-0009](../adr/0009-studio-design-and-registered-diner-personalisation.md) record those decisions. Supplementary prose references do not change the 72-row count.

The original [functional definition](../research/storefront-digital-menu/functional-definition/functional-definition.es.md) is a source inventory, not independent demand evidence. [Master research](../research/storefront-digital-menu/README.md) provides advertised patterns and source references; the [historical research inventory](../research/README.md) records public-review and fictional-scenario limitations. None establishes unmet demand, recommendation effectiveness, willingness to pay or service margin. No new general competitive research is needed to close this preparation milestone. Rebuilding the historical synthesis or checking a time-sensitive claim remains separate, decision-specific work before using it in a product or commercial claim.

## 2. Exit-criteria audit

The criteria below are those in the [executive brief](m0-execution-brief.md), the roadmap and existing issues #3/#6. This is an author audit, not an independent Quality review.

| Criterion | Evidence and result | Integration checkpoint or later work |
| --- | --- | --- |
| Every source capability has explicit treatment, source, rationale, responsibility and dependency | Matrix: 72 exact parent IDs/line references, 36/30/6 counts; separate media subparts and S1/S2 prose decisions. D1/D2/D4/D5 resolved. | Reviewed and integrated through PR #19 as 3ef9d6f; no repeat scope questionnaire. |
| Diner/operator/buyer journeys have initial criteria and representative cases | [Journeys](../product/m0-journeys-and-criteria.md): J1–J15/R01–R17; full parent coverage; C1 café, C2 variants/areas and C3 daily menu/languages explicitly proposed cases. | M1 produces and checks actual prototypes; fixtures are not participant evidence. |
| Design and supporting responsibilities have usable briefs | [M1 briefs](../product/m1-design-briefs.md): public/management objectives, scope, states, outputs, review criteria; targeted Engineering, Quality, Service, Commercial/SEO questions and expected outputs. | Specialists execute/review in the affected milestone; prepared consultations are not claimed answered. |
| Open consequential work has responsibility, next action and affected checkpoint | Carry-over register below plus the six-target dependency register in the M1 briefs. No launch-defining scope question remains unresolved. | Resolve each dependency before its affected design/construction/pilot/offer checkpoint; accepted scope cannot be dropped silently. |
| Capacity, tools, content and participant access are recorded honestly | Resource snapshot below; Yahya is the sole accountable person, no dates, staffing, purchases or participant access presumed. | Confirm actual execution capability before commissioning work or promising delivery; costs considered at concrete choices. |

Result: preparation evidence, authorised review, integration and formal tracker closure are complete. This author audit is not an independent Quality review or proof of subsequent milestone delivery.

## 3. Resource snapshot

| Resource | Actual recorded state | Execution consequence |
| --- | --- | --- |
| Accountable capacity | Yahya owns product decisions, engineering and merges. G1–G6 identify responsibilities, not staffed teams. Availability has no committed calendar estimate. | Coordinate a small active set from actual progress; do not promise dates or imply available independent reviewers. |
| Repository and tracking | Git/Node/pnpm and authenticated GitHub workflow are available; PRs #7/#8/#16/#18/#19 are integrated, M0 is closed and Linear YAH-5 is Done. | Use #5 for G2 design, #4 for M2 and #15 for the parallel commercial line; M0 records are completed antecedents. |
| No-code prototyping | No specific design-tool access or completed prototype is confirmed. | G2 confirms an available method before prototype execution; report interactive versus static fidelity honestly. |
| Venue and media inputs | Real menus, reviewed translations/nutrition, rights-cleared video and display hardware/context are unconfirmed. | Prepare clearly fictional C1–C3 cases where needed; obtain actual material/access before claiming real delivery. |
| Participants and independent review | No real diner/operator sessions or independent specialist review completed. | Record actual reviewer/access availability in M1; real participant evidence remains required by M6. |
| Integration access | No supported external target, credentials or successful connected outcome is established. | Preserve all six accepted capabilities; resolve target, authorised data and supported operation before affected construction. |
| Spending and service capacity | No fixed budget, pricing/support promise or unit economics approved. | Present concrete tool/service decisions when needed; measure delivery effort for D3 before commercial commitments. |

## 4. Carry-over register

Yahya is accountable for coordinating all rows. The responsibility column identifies the contribution needed; it does not assign an unavailable person. Existing outcome issues remain the tracking locations, avoiding a second backlog. A checkpoint is a dependency, not a calendar date.

| Outstanding work | Responsibility | Next action and evidence required | Checkpoint / existing outcome |
| --- | --- | --- | --- |
| Public/management experience and content fixtures | G2 Product Designer with early Visual Designer; G1 consolidates | Confirm prototyping method; create C1–C3 content/state inventory and capability/criterion-to-path map; produce both prototypes including J15 with coordinated UI/print composition. | M1 design closure / [#5](https://github.com/yaboula/valiris-restaurants/issues/5) |
| Critical behaviour, accessibility and feasibility review | G4 independent Quality with G3 Engineering | Review publication/urgent updates, food/translation states, current-context recommendations, private sessions and recovery; record findings and corrections in both public/operator paths. | Affected M1 paths before design closure; implementation checks from M3 / #5 and [#4](https://github.com/yaboula/valiris-restaurants/issues/4) |
| Six connection targets and authorised operations | G1 Product with G3 Engineering/G5 Service | Resolve B1.09 booking destination, B2.10 operational source, B4.12 external change authority, B6.07 existing website, B6.08 distribution destination and B7.06 confirmed-outcome source using the brief's register. Identify actual access/data and failure boundaries; escalate a material commitment change to the owner. | Target-specific design before finalising that path; support/access before affected M3–M5 construction / #5, #4, [#11](https://github.com/yaboula/valiris-restaurants/issues/11), [#12](https://github.com/yaboula/valiris-restaurants/issues/12) |
| Registered-diner identity and personalisation | G1 Product with G3 Engineering/G4 Quality | Design voluntary access/preferences/empty-error-recovery states; specify sufficient account scope, inputs, authentication, data/access and retention/deletion rules. Explicit preferences are a proposed starting point, not a selected algorithm. | M1 paths, M2 technical decisions, M4 complete public capability / #5, #4, #11 |
| Actual video/nutrition/language and screen inputs | G5 Service with G2 Design/G4 Quality | Obtain permitted material, reviewed portion/variant information and representative device/context; maintain missing/pending states where content is unavailable. | Design examples labelled in M1; actual content/support before affected M4–M5 delivery / #5, #11, #12 |
| Offline freshness, import/scheduling/recovery and measurement rules | G3 Engineering with G1 Product/G4 Quality | Specify testable contracts from the proposed R01–R17 behaviours; retain stale/conflict/insufficient-data cases without fabricated outcomes. | M2 backlog and affected M3–M5 delivery / #4, [#10](https://github.com/yaboula/valiris-restaurants/issues/10), #11, #12 |
| Real use and service evidence | G5 Service with G1 Product | Obtain authorised participants/materials; distinguish expert walkthroughs from real sessions, autonomous use from demos and effort from assumptions. | Available real checks in M1; required real pilot evidence in M6 / #5, [#13](https://github.com/yaboula/valiris-restaurants/issues/13) |
| D3 commercial terms and concrete spending | G6 Commercial/G5 Service with owner | Prepare truthful brand/site/offer work; measure setup, bespoke revisions, support and exit effort; submit reviewable terms/tool costs when relevant. No unsupported prices or effectiveness claims. | Parallel preparation; evidence during M5/M6 and founder-approved commitments before M7 / [#15](https://github.com/yaboula/valiris-restaurants/issues/15) |

Missing targets or participants remain genuine delivery constraints. Recording them here satisfies M0 dependency identification; it does not satisfy their later checkpoint, waive independent review or defer accepted launch capabilities.

## 5. M1 handover order

G2's active assignment is [M1 #5](https://github.com/yaboula/valiris-restaurants/issues/5), using the two [design briefs](../product/m1-design-briefs.md). Product Designer leads architecture, interaction, states, UX writing, the functional no-code prototype and coverage; Visual Designer joins with the first journeys/content for art direction, UI, identity, templates and print composition. G1 consolidates decisions; G4 retains independent review. G3/G5/G6 contribute to concrete questions rather than a blanket document review.

Start with information architecture and C1–C3 fixture/state coverage. Connect the operator prepare/review/publish path to public before/during-visit consultation and urgent maintenance; include permissions, context/price, translation/food and recovery risks early. Then complete the remaining committed paths, including personalisation, offline, video/nutrition, screens, comparison and connected states. The 72 capabilities are coverage references, not navigation destinations; C1 does not require C2/C3 configuration. This is design ordering, not a launch-scope reduction.

Return interactive public/management prototypes, visual/print direction, a capability/criterion coverage map, proposed/resolved rules and actual review findings. Record fictional content, fidelity limits and absent participants. No additional M0 closure or scope approval, new Product chat or speculative design system is required to start. M1 closure needs the actual evidence defined in #5.

## 6. Completed integration and closure evidence

| Order | PR | M0 outcome |
| --- | --- | --- |
| 1 | [#7 — Foundational documentation](https://github.com/yaboula/valiris-restaurants/pull/7) | Integrated as b36dfe2; three review findings corrected and threads resolved; #1 historically closed. |
| 2 | [#8 — Research inputs](https://github.com/yaboula/valiris-restaurants/pull/8) | Integrated as f5d459c; [#2](https://github.com/yaboula/valiris-restaurants/issues/2) records traceable inputs and honest historical limits, without a retired gate or demand claim. |
| 3 | [#16 — Current roadmap](https://github.com/yaboula/valiris-restaurants/pull/16) | Integrated as 186ca62; [#9](https://github.com/yaboula/valiris-restaurants/issues/9) records current milestone boundaries and planning migration. |
| 4 | [#18 — Executive brief](https://github.com/yaboula/valiris-restaurants/pull/18) | Integrated as b44510b; [#17](https://github.com/yaboula/valiris-restaurants/issues/17) records the execution framework. |
| 5 | [#19 — Commitment and closeout](https://github.com/yaboula/valiris-restaurants/pull/19) | Integrated as 3ef9d6f; [#3](https://github.com/yaboula/valiris-restaurants/issues/3) and [#6](https://github.com/yaboula/valiris-restaurants/issues/6) closed: accepted scope, usable briefs and recorded dependencies/resources. |

The owner authorised delegated review and squash integration, replacing the previous owner-only merge rule. Branch protections remain active. After each predecessor merge, only its dependent changes were transplanted onto the new base, the next PR was retargeted and its diff checked. This avoids duplicate ancestor changes. Commit authors/trailers are checked; historical commits retain their original approved identity and new squash commits use the owner's verified GitHub identity/email.

Issue #15 runs through M7, so its full commercial outcome belongs to the M7 tracker milestone; the M0 preparation contribution is evidenced here and in the briefs. Moving its completion milestone does not postpone its parallel execution.

All M0 outcomes were reviewed, integrated and confirmed closed; the M0 milestone is closed and [Linear YAH-5](https://linear.app/valiris/issue/YAH-5/m0-consolidate-launch-commitment-and-m1-design-briefs) is Done. #5/#4/#15 and later outcomes remain open. This is completed integration evidence, not a pending prerequisite for design. No application tag, implementation test, prototype, commercial clearance or launch announcement was required for M0.
