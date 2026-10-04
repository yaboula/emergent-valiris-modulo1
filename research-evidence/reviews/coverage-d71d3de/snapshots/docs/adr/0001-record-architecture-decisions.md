---
status: accepted
date: 2026-09-28
deciders: Product owner
---

# ADR-0001: Record architecture decisions

## Context and problem statement

Valiris Restaurants is built by a very small team and must demonstrate a professional, evidence-based engineering process. Decisions made in conversation or in someone's head are lost, cannot be reviewed and cannot be explained to clients or future contributors. How do we keep a durable, reviewable record of significant decisions?

## Decision drivers

- Traceability: every significant decision must be explainable months later.
- Reviewability: decisions should go through the same pull request review as code.
- Low overhead: the format must be light enough to be used consistently.

## Considered options

1. Architecture Decision Records in Markdown (MADR 4) inside the repository
2. Decisions recorded in a wiki or external tool (Notion, Confluence)
3. No formal record; rely on commit messages and pull request descriptions

## Decision outcome

Chosen option: **ADRs in Markdown using MADR 4, stored in `docs/adr/`**, because they live next to the code, are versioned and reviewed through pull requests, and have a widely recognised, lightweight structure.

### Consequences

- Good: decisions are versioned, reviewable, searchable and visible in the repository history.
- Good: new contributors and clients can understand why the system is the way it is.
- Bad / accepted trade-off: writing ADRs takes time; mitigated by using them only for significant decisions (see [`README.md`](README.md)).

### Confirmation

Pull requests that introduce a significant decision without an ADR are sent back in review.

## Pros and cons of the options

### ADRs in the repository (MADR 4)

- Good: docs-as-code, same workflow as code, no extra tool.
- Bad: less convenient for non-technical readers.

### External wiki

- Good: rich editing.
- Bad: drifts from the code, not versioned with it, extra tool to maintain.

### No formal record

- Good: zero overhead.
- Bad: rationale is lost; alternatives considered are never documented.

## More information

- MADR: https://adr.github.io/madr/
- Michael Nygard, "Documenting Architecture Decisions" (2011).
