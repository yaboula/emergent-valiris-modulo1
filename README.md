Current M1 documentation and design work is consolidated through the owner-authorised main integration. See the [operating handoff](HANDOFF.md) and [source/review register](research-evidence/reviews/main-integration-2026-10-04/README.md). This repository contains planning, fictional ORILLA content, retained source evidence and visual proposals; it is not yet a usable application or completed M1 release.

# Valiris Restaurants

> Public presence and a living digital menu for independent restaurants — built by **Valiris**, with a modular product vision.

![status](https://img.shields.io/badge/status-M1%20experience%20design-blue)
![license](https://img.shields.io/badge/license-proprietary-lightgrey)

## What it is

Valiris Restaurants is a studio-owned product for independent restaurants and cafés in Spain. Its first commercial release is **Storefront + Digital Menu** and the Core necessary to prepare, review, publish and maintain restaurant information. QR is one access route, alongside public links and other channels. Templates and paid bespoke design are supported delivery directions; detailed launch commitments are settled in M0.

Bookings, reviews, loyalty, reactivation and a WhatsApp assistant remain future modular possibilities without a committed implementation order. Ordering, payments, POS, delivery and invoicing are outside the first module. Demand, usability, willingness to pay and service economics still require real evidence.

Shared responsibilities will evolve with actual product needs. Future verticals remain a vision, not a requirement to implement a sector-agnostic platform before the first usable journey.

## Project status

**M0 is integrated and closed; G2's active assignment is [M1 #5](https://github.com/yaboula/valiris-restaurants/issues/5).** Launch scope and first-prototype briefs are delivered. Start with the [public and operator design briefs](docs/product/m1-design-briefs.md); the [closeout](docs/project/m0-closeout.md) records completed integration and pending delivery dependencies. M1 covers no-code experience design, M2 construction preparation, M3–M5 implementation, M6 a real pilot, and M7 launch. No completed prototype, application implementation or commercial validation is claimed.

- Operating entry point: [HANDOFF.md](HANDOFF.md), [AGENTS.md](AGENTS.md) and [assignment/evidence index](coordination/README.md)
- Roadmap: [`docs/project/roadmap.md`](docs/project/roadmap.md)
- Project charter (philosophy, quality bar, standards, roles, risks): [`docs/project/charter.md`](docs/project/charter.md)
- Research inputs and historical evidence: [`docs/research/`](docs/research/README.md)
- Architecture decisions: [`docs/adr/`](docs/adr/README.md)
- Glossary: [`docs/glossary.md`](docs/glossary.md)

## Repository layout

```text
AGENTS.md        Shared project instructions and mandatory Git workflow
HANDOFF.md       Current operating state with retained history
coordination/    Specialist assignments, protocol and storage provenance
research-evidence/ Immutable source/review records and delivery assets
docs/            Documentation as code (research, product, architecture, ADRs, testing)
.github/         Issue/PR templates and repository automation
scripts/         Repository tooling (e.g. GitHub label sync)
```

Technical structure is selected in M2 from the first product’s needs. Necessary Core is implemented with the connected journeys in M3–M5; the earlier monorepo layout is not a committed construction prerequisite.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the workflow, branch and commit conventions, and the Definition of Done.

## License

Copyright (c) 2026 Valiris. All rights reserved. See [`LICENSE`](LICENSE).
