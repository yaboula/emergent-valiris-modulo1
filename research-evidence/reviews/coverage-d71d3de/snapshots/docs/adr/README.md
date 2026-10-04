# Architecture Decision Records

This directory contains the Architecture Decision Records (ADRs) of Valiris Restaurants, written in the [MADR 4](https://adr.github.io/madr/) format.

## When to write an ADR

Write an ADR when a decision:

- is costly to reverse (data model, framework, hosting, tenancy model);
- affects more than one module or the platform/vertical boundary;
- chooses between real alternatives with different trade-offs;
- accepts a known risk.

## Process

1. Copy [`template.md`](template.md) to `NNNN-short-title.md` using the next free number.
2. Open a pull request with status `proposed`.
3. The product owner accepts or rejects it in review; the status is updated before merging.
4. ADRs are immutable once accepted. To change a decision, write a new ADR and mark the old one as `superseded by ADR-NNNN`.

## Index

| ADR | Title | Status |
| --- | --- | --- |
| [0001](0001-record-architecture-decisions.md) | Record architecture decisions | Accepted |
| [0002](0002-studio-brand-valiris.md) | Keep "Valiris" as the studio brand despite a name collision | Accepted |
| [0003](0003-product-name.md) | Name the product "Valiris Restaurants" | Accepted |
| [0004](0004-repository-visibility-and-license.md) | Private repository and proprietary license until v1.0 | Accepted |
| [0005](0005-repository-and-product-language.md) | English for the repository, Spanish-first product UI | Accepted |
| [0006](0006-discovery-evidence-boundary.md) | Define the evidence boundary for the discovery gate | Rejected; retired by ADR-0007 |
| [0007](0007-first-product-launch-roadmap.md) | Launch Storefront + Digital Menu before subsequent modules | Accepted by owner instruction; PR integration pending |
| [0008](0008-first-launch-capability-commitment.md) | Commit first-launch capabilities and defer only audio and 3D | Accepted by owner instruction; PR integration pending |
| [0009](0009-studio-design-and-registered-diner-personalisation.md) | Keep studio design and personalise for registered diners | Accepted by owner instruction; PR integration pending |
| [0010](0010-diner-account-and-display-recovery.md) | Share diner identity, scope preferences by venue and hide unconfirmed display prices | Proposed record of owner-selected design directions; technical contracts/review pending |
| [0011](0011-shared-menu-content-and-contextual-maintenance.md) | Prefer shared item content with explicit contextual maintenance | Proposed record of owner-selected reuse direction; field ownership, coherent operation and technical review pending |
| [0012](0012-confirm-delegated-updates-per-assignment.md) | Confirm delegated updates per assignment | Proposed record of owner-selected confirmation model; actual service terms/authority/version/result contracts pending |
