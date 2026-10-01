> Historical discovery context (September 2026). The [current first-product roadmap](../project/roadmap.md) supersedes the former M0 subphases, Gate 1/2 and seven-module v1 timetable. Findings remain research inputs; old milestone references are historical, not launch commitments. No commercial validation is established.

# Discovery synthesis and Gate 1

Prepared: 2026-09-28. Owner: Yahya, product owner and lead engineer. **Decision status: pending owner review.**

## Recommendation

Recommend a **conditional go for portfolio product definition**, with commercial demand explicitly unvalidated. The research supports investigating reliable guest-facing information, booking operations and repeat-guest workflows; it does not support claims of a unique bundle, demand at a particular price, reduced no-shows or improved retention.

The proposed evidence boundary is recorded in [ADR-0006](../adr/0006-discovery-evidence-boundary.md), status proposed. No scope, provider or pricing decision is accepted by this document. That previous seven-module v1 planning constraint is retired. The current launch commitment covers Storefront + Digital Menu and necessary Core; this historical synthesis has not yet been rebuilt from the latest module research.

## Evidence inventory

| Evidence class | Available | What it establishes | What it cannot establish |
| --- | --- | --- | --- |
| Official statistics and sector research | [INE market/ICT sources and SEGITTUR summary](market.md) | Enterprise context, size-dependent digital adoption and qualitative adoption barriers | Segment-specific prevalence, addressable buyers or sales forecast |
| Vendor primary pages | [Seven named products/channels plus manual substitutes](competitors.md) | Advertised overlap, observed tariffs and purchasing constraints | Actual usability, outcomes or undisclosed plan capabilities |
| Public software reviews | [50 distinct records](review-ledger.md), [method](review-mining.md) | Reported failure modes, useful workflows and contradictory experiences | Population incidence, current vendor defect status or causal ROI |
| Fictional scenario exercises | [Three labelled simulations](interviews/script.md) | Questions, contrast cases and candidate requirements | Real participants, validated demand or willingness to pay |
| Law/provider policies | [L-01–12](legal.md) | Design constraints and unresolved prerequisites | Certification or complete legal clearance |

## Prioritised problems

These ranks express severity and relevance judgments for design, not a market prevalence score.

| Rank / problem | Evidence | Confidence and counterevidence | Candidate response / next check |
| --- | --- | --- | --- |
| P1: service-time tasks fail or slow down | Reliability/UX reports RM-001, 008, 014, 017, 027, 030, 034; useful app reports RM-021–023/031; SEGITTUR adoption-barrier summary | Moderate confidence that the failure mode matters; current incidence unknown. Incumbents also receive positive feedback. | Mobile task flows, explicit recovery states and regression tests. Define task budgets in M0.3; do not promise uptime without measurements. |
| P2: booking changes and notifications become inconsistent | RM-005, 007, 010, 012, 019, 020, 029; fictional neighbourhood contrast | Moderate reported signal; several TheFork reports are historical and may share release causes. | Shared current booking record, capacity invariants, observable delivery and clear manual-entry path. Probe simultaneous edits and external channels. |
| P3: guest/card retrieval interrupts useful loyalty work | RM-026, 028, 044, 049, 050 | Moderate exploratory signal; country/segment transfer is limited. An incumbent customer database is itself valued. | Recover guest/card access and show transaction history without opening a fraud path. Test lost-card and changed-phone tasks. |
| P4: accurate public information must remain maintainable | Official allergen rules L-06/07; vendor menu tooling; RM-006 concerns photos, not allergens | High confidence in the obligation; low direct evidence of unmet menu-maintenance demand. | Owner-reviewed menu/variant/translation states; quick availability update and human safety escalation. Validate an actual update workflow. |
| P5: consented return-visit workflows may help local venues | Loyalty mixed reports RM-042–050 and advertised competing tools; fictional cafe scenario | Low confidence in incremental commercial value; no causal retention or reactivation result. Tourist contrast weakens fit. | Trace confirmed visits and consent; measure observed return visits separately from campaign attribution. Test adoption before claiming benefit. |

## Jobs to be done (hypotheses)

- When a service is busy, let me record and change a booking quickly so the team acts on current capacity.
- When menu information changes, let me publish a reviewed update so guests and staff see consistent information.
- When a returning guest cannot find a loyalty card, let me resolve their eligibility safely without blocking the queue.
- When I contact an inactive guest, let me use recorded permission and see a defensible outcome rather than counting clicks as visits.
- When a guest asks a repetitive question, let them get a grounded answer or reach staff without unsafe guesses.

These statements are proposed interpretations. They are not quotations from restaurant owners.

## Differentiation hypothesis

**Hypothesis:** a focused companion to the restaurant's existing POS, designed for small teams' mobile guest-service tasks, could earn preference through clear information, dependable booking updates and recoverable loyalty workflows.

This is an execution hypothesis, not an established competitive moat. EterSystem already overlaps strongly; Qamarero and booking incumbents already link customer workflows. Commission-free direct booking, Wallet cards, multilingual menus and AI features are not individually unique. Marketplaces also supply consumer demand that Valiris cannot currently replace.

The largest weakness is the absence of POS data: booking completion must be confirmed, public menu scans do not prove visits, and a loyalty redemption does not automatically establish spend. Parallel booking channels add another inconsistency risk. M0.3 must define honest manual-confirmation and reconciliation boundaries before using those facts for reviews, rewards or reactivation. No POS/channel integration is added to v1 here.

## Falsification and measurement plan

Proposed evaluation targets require owner approval in M0.3; none are achieved metrics:

1. Observe 3–5 usability participants in M8 with a seeded demo: manual booking/change, menu availability update, guest/card recovery and marketing opt-out. Record unassisted completion, time and critical errors; participant type must be reported. General usability participants cannot validate restaurant purchasing demand.
2. Use integration tests to verify capacity, duplicate processing, cross-tenant denial, uniform review invitations and suppression before promotional sends. Define thresholds and environments in M0.3/M0.4.
3. For future commercial validation, interview independent target operators about recent incidents and current spending. Reject or narrow the positioning if incumbents already solve these tasks sufficiently, duplicate entry overwhelms value, or an actual migration/purchase commitment fails to materialise. No outreach has been conducted.
4. Separate booking-created, attendance-confirmed, reward-issued, campaign-delivered, campaign-clicked and return-visit-observed. A seeded demo can verify event handling; it cannot demonstrate business uplift or causal attribution.

## Gate 1 review record

| Field | Recorded state |
| --- | --- |
| Requested decision | Accept a limited portfolio-discovery gate and proceed to M0.3, or request more evidence |
| Recommendation | Conditional go for portfolio definition; commercial demand unvalidated |
| Decision | **Pending — not passed** |
| Decider | Yahya, product owner and lead engineer |
| Approval date / review reference | Not recorded |
| Deliverable status | Research set prepared; owner review outstanding |

The original issue required Gate 1. That requirement is retired by ADR-0007; issue #2 now tracks research integration without claiming a passed gate. If the gate means commercial validation, the present evidence is insufficient and the recommendation is no-go for that claim. Accepting the proposed narrower meaning requires explicit review of ADR-0006, rather than quietly redefining validation.

### Conditions to record before a pass

- Acknowledge the absence of real interviews and paid demand; approve or reject ADR-0006's evidence boundary.
- Accept or revise the target segment and the companion-product hypothesis without treating it as a proven differentiator.
- Carry the legal register, unresolved provider terms and weakly evidenced retention assumptions into M0.3/M0.4.
- Review and merge M0.1's PR #7, including its pending foundational decisions; then review this dependent research PR.

## Handoff to M0.3 and M0.4

For [issue #3](https://github.com/yaboula/valiris-restaurants/issues/3), turn P1–P5 and L-01–12 into traceable stories/NFRs with testable criteria. Keep seven modules thin; decide what a real visit means, which workflows stay manual, and how module-off states behave. Do not add ordering, delivery, POS, invoicing or Google partnership work as implicit discoveries.

For [issue #4](https://github.com/yaboula/valiris-restaurants/issues/4), formalise tenancy/RLS, events, payment responsibilities, retention and provider choices. Reliability signals should inform recovery and regression strategy; avoid treating a complaint about an incumbent app as a reason to adopt unnecessary infrastructure.
