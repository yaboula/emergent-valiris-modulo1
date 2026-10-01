---
status: accepted
date: 2026-10-01
deciders: Product owner
---

# ADR-0008: Commit first-launch capabilities and defer only audio and 3D

## Context and problem statement

The first-product roadmap requires explicit launch treatment for every Storefront + Digital Menu reference capability. The initial matrix proposed 60 included/configurable capabilities, with five opportunities deferred, displays pending and six connections conditional. The owner approved D1 and rejected that D2 deferral recommendation, instructing launch delivery with only audio and 3D postponed.

## Decision drivers

- Preserve the owner's product ambition and complete reference coverage.
- Separate configurable launch capability from deferral and unresolved delivery dependencies.
- Keep shared content, reviewed publication, food-information honesty and independent Quality review across additional outputs and automation.
- Retain outcome-based execution, no committed dates and spending decisions based on concrete proposals.

## Considered options

1. Original D2 recommendation: defer personal list, rich media, nutrition, offline consultation and change comparison; consider displays later; leave connections conditional.
2. Owner-amended launch: include those capabilities and displays, deliver video and launch connections, defer only standalone audio and 3D.

## Decision outcome

Chosen option: **owner-amended launch**, accepted by explicit owner direction on 1 October 2026. D1 is approved; the original D2 deferral recommendation is rejected.

- Retain the original 36 common and 24 configurable capabilities.
- Add personal comparison list, video explanation, nutritional information, offline consultation, change comparison and in-venue displays as configurable launch capabilities. Configurable means available at launch when relevant.
- Keep the six connection capabilities in the launch commitment. Resolve supported sources/destinations, access, field ownership, data and failure states; unknown dependencies do not authorise silent deferral or claims of functioning integration.
- Split source B3.11: video at launch; standalone audio explanations and 3D later.
- Maintain other-module responsibility boundaries. This does not authorise building all future booking/loyalty/messaging modules or every provider connector.
- The free-form owner editor and individualised recommender are separate prose-only ideas omitted from the enumerated D2 question. Their inclusion needs explicit clarification; neither is silently approved or deferred.
- Pricing/support/commission/domain details remain pending concrete evidence. Accepted scope is not implementation, validation, commercial readiness or M0 completion.

### Consequences

- Good: launch scope matches the owner's decision and preserves both public benefit and maintainable operator counterparts.
- Accepted trade-off: additional media/content, offline freshness, nutritional sourcing, display operation and comparison requirements increase design, delivery and review work. No time, cost or margin estimate is invented.
- Delivery dependency: connected outcomes need an actual source of confirmed results without absorbing other-module execution. Resolve access and targets during preparation; flag blocked evidence honestly.

### Confirmation

Check all 72 source rows once, approved scope separate from proposed detailed rules, and explicit audio/3D subparts. Review public/operator/output journeys for the added capabilities, including changed personal selections, unavailable nutrition, stale offline content, display failure and insufficient comparison data. Confirm actual target/access choices before declaring a connection complete. Preserve independent Quality review and real-test limits.

## Pros and cons of the options

### Original D2 recommendation

- Good: fewer delivery dependencies and content formats.
- Bad: does not meet the owner's chosen first-launch ambition; rejected by the owner.

### Owner-amended launch

- Good: first launch covers the chosen full reference scope, with only the explicit media-format deferrals.
- Bad / accepted: more maintenance, provider/data and verification work; missing prerequisites need resolution rather than assumptions.

## More information

- [Current capability matrix](../product/m0-capability-matrix.md), [journeys and criteria](../product/m0-journeys-and-criteria.md), [M1 design briefs](../product/m1-design-briefs.md).
- [ADR-0007](0007-first-product-launch-roadmap.md) retains the first-product sequence and modular boundaries.
- [GitHub #3](https://github.com/yaboula/valiris-restaurants/issues/3) and [PR #19](https://github.com/yaboula/valiris-restaurants/pull/19) record integration work. Acceptance is by owner instruction; PR integration remains pending.
