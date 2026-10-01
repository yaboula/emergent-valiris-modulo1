---
status: accepted
date: 2026-09-28
deciders: Product owner
---

# ADR-0003: Name the product "Valiris Restaurants"

## Context and problem statement

Valiris is a studio with a planned line of vertical products (restaurants first, then other sectors such as barbershops or beauty salons), all built on a shared platform. The first product needs a name that works in the Spanish market, reads well internationally for the portfolio, and sets the naming pattern for future products.

## Decision drivers

- Immediate clarity for restaurant owners (what the product is, at a glance).
- A naming pattern that scales to future verticals.
- Distinctiveness from existing restaurant software in Spain (Qamarero, EterSystem, TheFork, CoverManager).
- Mitigation of the brand collision described in [ADR-0002](0002-studio-brand-valiris.md): the product name must never be "Valiris" alone.

## Considered options

1. **Descriptive names:** Valiris Restaurants, Valiris Restaurantes, Valiris for Restaurants, Valiris Resto
2. **Evocative names:** Valiris Sobremesa, Valiris Mesa, Valiris Tavola, Valiris Sala, Valiris Covers

## Decision outcome

Chosen option: **"Valiris Restaurants"**, a descriptive, English name. The product owner preferred a direct, self-explanatory name, like the naming used by established vertical software lines (for example "Square for Restaurants").

### Consequences

- Good: it is self-explanatory, and future products follow the same pattern (e.g. "Valiris Barbershops").
- Good: the English form suits the international portfolio and is still understood in Spain.
- Bad / accepted trade-off: descriptive names are weak trademarks on their own. The distinctive element is "Valiris" (see ADR-0002).
- The UI may present localized descriptors (e.g. "Valiris Restaurants · para restaurantes"). The product name itself is not translated.

### Naming conventions derived from this decision

| Artifact | Value |
| --- | --- |
| Product name | Valiris Restaurants |
| Repository | `yaboula/valiris-restaurants` |
| npm scope | `@valiris/*` (studio scope shared across products) |
| Restaurant app package | `apps/restaurants` |
| Public attribution on restaurant pages | "Powered by Valiris Restaurants" |

### Confirmation

Naming is checked in review. Configuration and theme tokens hold the product name so it can be changed in one place.
