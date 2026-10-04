---
status: accepted
date: 2026-09-28
deciders: Product owner
---

# ADR-0005: English for the repository, Spanish-first product UI

## Context and problem statement

The product targets restaurants in Spain, while the repository is also a portfolio piece for international freelance clients (Upwork, Malt, LinkedIn) and employers. In which language do we write the code, the documentation and the product interface?

## Decision drivers

- International readability of the repository for clients and employers.
- Industry convention: code, commits and technical documentation are written in English.
- End users (restaurant staff in Spain and their guests, many of them tourists) need a native-quality UI.

## Considered options

1. English repository, Spanish-first internationalized UI
2. Spanish for everything
3. English for everything, including the UI

## Decision outcome

Chosen option: **English for the repository (code, docs, commits, issues); Spanish-first UI with full internationalization.**

- The owner panel ships in Spanish first, then English.
- The guest-facing surfaces (storefront, menu, booking) ship in Spanish, English, French and German, with the architecture ready for Arabic (right-to-left).
- The [glossary](../glossary.md) keeps the Spanish domain term next to every English term, so that the code and the UI stay consistent.

### Consequences

- Good: the repository is readable by international reviewers; the product feels native to its users.
- Bad / accepted trade-off: every domain concept needs a precise translation, which the glossary maintains.

### Confirmation

Review checks that no user-facing string is hard-coded. From M1, this is enforced by the i18n lint rules.

## Current milestone applicability

[ADR-0007](0007-first-product-launch-roadmap.md) updates the historical M1 trigger: implementation i18n enforcement begins with construction in M3. The language decision above remains in force.
