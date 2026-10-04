---
status: proposed
date: 2026-10-02
deciders: Product owner
---

# ADR-0012: Confirm delegated updates per assignment

## Context and problem statement

The accepted optional delegated-update service (B7.10/J8.3) must preserve restaurant autonomy and the same draft, factual review and publication controls as ordinary editing. A studio worker needs an understandable authority scope; receiving a request, confirming facts and having permission to publish are different conditions.

On 2 October the owner selected **confirmation per assignment** as the principal model rather than a continuing limited authorisation, then authorised execution of the J8/J9 descriptive plan. This ADR remains **proposed** under repository review/integration; the founder's choice is recorded separately from proposed authority/version/result mechanics, actual service terms and M2 contracts. Accepted historical ADRs are unchanged.

## Decision drivers

- Keep autonomous everyday updates available in template and paid bespoke presentation; delegation is optional.
- Make selected fields/values, item/context/service, facts/dependencies and public/private effects visible.
- Avoid publishing another draft, silently expanding an assignment or confusing studio receipt with completed change.
- Preserve action-specific venue access, factual confirmation, unknown-result recovery and relevant version conflicts.
- Define truthful provisional service without inventing staff availability, tariffs, hours or support limits.

## Considered options

1. Explicit confirmation of each delegated assignment and whether it authorises publication.
2. Continuing limited authorisation for agreed change types/scopes, with new confirmation only for exceptions.
3. Any received request implicitly permits the studio to publish any related content.

## Decision outcome

Chosen direction: **Option 1**, selected by the owner. The [J8/J9 design](../design/m1-service-and-maintenance.md) proposes:

- Each assignment identifies venue/items/context/date/service, current/proposed fields, dependencies and confirmed source/scope revision. Draft preparation only and preparation with explicitly authorised publication are distinct; neither permission is silently selected or acquired by receiving a request.
- The studio actor must separately have actual content/live/publication permission for that scope. Restaurant facts/media/food/languages and all affected common uses retain their existing review requirements. Requester confirmation cannot create Core permission or override an authoritative external field.
- Relevant scope/value/source change requires renewed requester confirmation and current coherent publication review. C1 coffee 1,90 € → 2,00 € does not publish the independent croissant draft or a later competing 2,10 € proposal by assumption; C3 future D11 stays private.
- Preparation, sending/receipt, work, draft proposal, known publication/correction and unknown result are distinct. Cancellation/timeout/result loss checks the original assignment/action before retry, with no blanket success or implicit rollback.
- Optional delegated support does not revoke autonomy or turn ordinary content updates into new design commissions. Actual types/volume/response conditions, provider/channel and prices remain D3/G5/G6/founder decisions supported by real evidence.

### Consequences

- Restaurant: clear control over each requested scope; confirmation/reconfirmation creates review work and can delay application. No observed time saving is claimed.
- Diner: public scope/factual coherence is preserved, but unconfirmed corrections may need explicit pending/withholding until reviewed. No food safety guarantee.
- Valiris: assignment/revision/authority traceability, response/recovery and scoped service handling are required. No staffing, service-level commitment, price, margin or implementation is established.
- G3/M2: evaluate identity/action permissions, assignment confirmation/expiry/revocation, content bases/common groups, retention and original-result correlation. No API/database/job/schema/contract mechanism selected by this record.

### Confirmation

Author J8-S07/S08 and J9-X01–X03 descriptions and SC07–SC11/SC26 contrasts; previous draft/urgent/shared/version/access cases are re-read. This is documentary author checking.

Before affected closure, G4 independently checks scope/intent/result understanding; G3 reviews enforceable authority/version/concurrency contracts; G5/G6 supplies actual service scope/channel/terms and restaurant task evidence. Existing independent G4-01 closure does not approve this decision or new states.

## Pros and cons of the options

### Option 1 — Per assignment

- Explicit, understandable authority tied to reviewed values and public/private intent.
- Requires confirmation and relevant re-confirmation for each task; service handover must make that work manageable.

### Option 2 — Continuing limited authority

- Could reduce repeated confirmations for routine permitted tasks.
- Requires carefully maintained types/scope/validity/exclusions and review of boundary cases; not the selected principal model. Introducing it later needs a reviewable owner decision, not inferred service permission.

### Option 3 — Received request as blanket authority

- Appears to shorten service workflow.
- Conflates request receipt, factual confirmation and publish permission, risks unrelated private content and stale scopes. Rejected as incompatible with reviewed publication.

## More information

[Launch commitment](0008-first-launch-capability-commitment.md), [studio composition/content autonomy](0009-studio-design-and-registered-diner-personalisation.md), [shared-context maintenance](0011-shared-menu-content-and-contextual-maintenance.md), [criteria](../product/m0-journeys-and-criteria.md) and [M1 briefs](../product/m1-design-briefs.md).

Revisit detailed mechanics if actual permissions, shared/context sources or service evidence show an incompatible use; G1 consolidates consequences and the founder decides material changes. D3 remains open; this record neither contracts a service nor authorises external communications, implementation, merge or M1 closure.
