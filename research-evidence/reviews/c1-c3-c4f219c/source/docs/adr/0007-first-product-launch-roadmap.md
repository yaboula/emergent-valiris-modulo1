---
status: accepted
date: 2026-10-01
deciders: Product owner
---

# ADR-0007: Launch Storefront + Digital Menu before subsequent modules

## Context and problem statement

The historical roadmap planned seven modules within 17 weeks and treated v1.0 as platform completion. Detailed Storefront + Digital Menu research and functional definition now support a different first-product direction. On 1 October 2026, the owner instructed replacement with the supplied roadmap and alignment of the project. Which scope, sequence and evidence rules govern execution?

## Decision drivers

- Complete a marketable first product and viable onboarding, bespoke-design and support service.
- Preserve ambitious accepted capabilities while making launch treatment explicit.
- Build only necessary shared responsibilities, connected to usable journeys.
- Require real evidence without presenting simulations or documents as validation.
- Estimate from actual capacity, backlog and delivery rather than retaining an obsolete calendar.

## Considered options

1. Retain seven modules and the 17-week plan.
2. Adopt the first-product M0–M7 roadmap and schedule future modules from evidence.
3. Build a QR-only utility, excluding broader presence and maintenance.

## Decision outcome

Chosen option: **2**, on the owner's explicit replacement instruction. The [current roadmap](../project/roadmap.md) governs execution.

- `v1.0.0` means commercial Storefront + Digital Menu with necessary Core and delivery service.
- M0 commits scope; M1 designs/checks no-code experience; M2 prepares construction; M3–M5 construct; M6 pilots with real participants; M7 launches/operates.
- Brand, commercial website and offer proceed in parallel with truthful claims.
- Future bookings, reviews, loyalty, reactivation and WhatsApp remain unscheduled opportunities.
- Retire the 17-week estimate, fixed module/version mapping, old discovery/scope gates and simulation-only pilot.
- The evidence-boundary proposal in ADR-0006 is retired, not approved as proof of demand.
- Existing privacy, license, brand, language and merge authority decisions continue. For ADR-0004, construction CI starts from M3 and the v1.0 visibility review is at M7, without changing visibility automatically. For ADR-0005, implementation i18n enforcement starts with construction in M3. These update milestone triggers only.
- Technical stack and layout are selected in M2. Future campaign/visit/booking infrastructure is not a prerequisite.

### Consequences

- Good: scope and commercial delivery align around one complete customer journey.
- Good: existing research remains reusable without falsely binding future modules.
- Trade-off: no fixed launch date or guaranteed next-module order; estimates follow actual delivery evidence.
- Real participant access is required for M6 evidence. Missing participation cannot be replaced by simulations.
- No proposed capability is automatically approved or removed; M0 records treatment, rationale and owner.

### Confirmation

Check active planning documents and GitHub milestones against M0–M7. Historical documents carry explicit applicability notices; supplied research originals remain intact. Every launch capability gets treatment and acceptance boundaries before construction. Pilot and commercial claims distinguish observed use, stated interest, quote acceptance and payment.

## Pros and cons of the options

### Retain the old platform plan

- Good: preserves the original sequence.
- Bad: conflicts with current scope, assumes speculative Core and unsupported timing.

### Adopt the first-product roadmap

- Good: aligns design, construction, service and evidence; preserves modular evolution.
- Bad: needs planning/tracker migration and later decisions about future modules.

### Build a QR-only utility

- Good: narrower implementation.
- Bad: drops the accepted public-presence and maintenance direction without justification.

## More information

[Planning transition](../project/planning-transition.md), [functional proposal](../research/storefront-digital-menu/functional-definition/functional-definition.es.md), [research](../research/storefront-digital-menu/README.md). Issue #9 records the migration; PR review and merge remain the owner's responsibility.
