---
status: accepted
date: 2026-09-28
deciders: Product owner
---

# ADR-0004: Private repository and proprietary license until v1.0

## Context and problem statement

The repository serves two goals: it is a commercial product of the Valiris studio, and it is the flagship portfolio piece for freelance clients and employers. Who can see the code, and under which license?

## Decision drivers

- Protect the product while it is incomplete and before any commercial decision.
- Showcase the engineering process (history, pull requests, ADRs) to clients once it is ready.
- Keep the option of commercial exploitation open.

## Considered options

1. Private until v1.0, proprietary license ("all rights reserved")
2. Public from day one, proprietary license
3. Public, open source (MIT)

## Decision outcome

Chosen option: **Private until v1.0, proprietary license**, decided by the product owner.

### Consequences

- Good: unfinished work is not exposed, and the commercial options stay open.
- Good: the full history, including research and decisions from day one, is preserved and becomes visible when published.
- Bad / accepted trade-off: until v1.0, clients cannot browse the code. Portfolio evidence is shared through the case study, demos and on-request access (GitHub collaborator invite).
- Good: `main` is protected by the repository ruleset "Protect main":
  - no deletion and no force push;
  - linear history;
  - changes only through pull requests, merged with squash, with all review threads resolved.

### Confirmation

- The ruleset is active (`GET /repos/{owner}/{repo}/rules/branches/main` lists `deletion`, `non_fast_forward`, `required_linear_history` and `pull_request`).
- From M1, required status checks (CI) are added to the ruleset.
- At the M8 release gate, the repository visibility is reviewed: it becomes public, keeping the proprietary license.

## Current milestone applicability

[ADR-0007](0007-first-product-launch-roadmap.md) updates the historical milestone triggers: construction checks begin in M3 and commercial v1.0 review occurs in M7. The substantive decision above remains in force.
