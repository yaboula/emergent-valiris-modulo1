# Valiris Restaurants

> All-in-one platform for independent restaurants: digital menu, table bookings, reviews, loyalty, customer reactivation and a WhatsApp assistant — built by **Valiris**.

![status](https://img.shields.io/badge/status-M0%20discovery-blue)
![license](https://img.shields.io/badge/license-proprietary-lightgrey)

## What it is

Valiris Restaurants helps small and mid-sized restaurants in Spain fill tables, cut no-shows and bring guests back — without per-cover commissions and with the guest data owned by the restaurant.

It is the first vertical product of the Valiris product line. It is built on a reusable, sector-agnostic **platform** (core + generic modules) with a restaurant-specific **vertical** and **app** on top, so future products (e.g. barbershops, beauty salons) reuse the platform and ship their own frontend.

| Module | Purpose |
| --- | --- |
| Storefront + QR Menu | Public restaurant page and multilingual menu with the 14 EU allergens |
| Table Bookings | Shifts, party size, capacity, reminders, waitlist, deposit/card guarantee |
| Reviews | Post-visit feedback, Google review invitation, alerts, AI-assisted replies |
| Loyalty | Stamps/points via QR, rewards, Wallet pass |
| Reactivation | Detects guests who stopped coming and runs consented campaigns |
| WhatsApp Assistant | AI receptionist grounded on the restaurant's real data, with human handover |

## Project status

The project is in **M0 — Discovery, specification and design**. No application code exists yet by design: every decision is researched and recorded first.

- Roadmap: [`docs/project/roadmap.md`](docs/project/roadmap.md)
- Project charter (philosophy, quality bar, standards, roles, risks): [`docs/project/charter.md`](docs/project/charter.md)
- Architecture decisions: [`docs/adr/`](docs/adr/README.md)
- Glossary: [`docs/glossary.md`](docs/glossary.md)

## Repository layout

```text
docs/            Documentation as code (research, product, architecture, ADRs, testing)
.github/         Issue/PR templates and repository automation
scripts/         Repository tooling (e.g. GitHub label sync)
```

The application monorepo layout (`apps/`, `packages/platform/`, `packages/verticals/`, `packages/ui-base/`) is introduced in M1 and described in the architecture documentation.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the workflow, branch and commit conventions, and the Definition of Done.

## License

Copyright (c) 2026 Valiris. All rights reserved. See [`LICENSE`](LICENSE).
