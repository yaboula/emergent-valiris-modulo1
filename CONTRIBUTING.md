# Contributing to Valiris Restaurants

This guide defines how work flows through the repository. It applies to documentation and code alike: documentation is treated as code.

## Roles

| Role | Responsibility |
| --- | --- |
| Product owner and lead engineer | Owns vision, scope and priorities; designs, implements and documents; approves gates, ADRs and pull requests |

## Workflow

1. **Every change starts from an issue** (user story, task, research or bug) assigned to a milestone (`M0`–`M8`).
2. **Create a short-lived branch from `main`** using the naming convention below.
3. **Open a pull request early**, fill in the template, link the issue (`Closes #123`).
4. **The pull request is merged only when it meets the Definition of Done** and the authorised review is complete. The product owner may delegate review and merge of approved work; material product decisions remain with the owner. Keep branch protections active.
5. **Merge strategy: squash merge.** The squash commit message follows Conventional Commits.

`main` is always releasable. Each milestone ends with a tagged release (`v0.1.0`, `v0.2.0`, … `v1.0.0`).

## Branch naming

```text
<type>/<milestone>-<short-description>
```

Examples: `docs/m0-research-competitors`, `feat/m3-booking-availability`, `fix/m2-menu-allergen-icons`.

## Commit messages

We follow [Conventional Commits 1.0](https://www.conventionalcommits.org/en/v1.0.0/):

```text
<type>(<scope>): <summary in imperative mood>
```

| Type | Use for |
| --- | --- |
| `feat` | A user-visible capability |
| `fix` | A bug fix |
| `docs` | Documentation only |
| `refactor` | Code change without behaviour change |
| `test` | Adding or fixing tests |
| `perf` | Performance improvement |
| `build` / `ci` | Build system, dependencies, pipelines |
| `chore` | Repository maintenance |

Scopes map to the architecture: `core`, `db`, `storefront`, `booking`, `reviews`, `loyalty`, `reactivation`, `whatsapp`, `ui`, `restaurants`, `adr`, `research`, `product`.

## Architecture decisions

Any decision that is costly to reverse, affects several modules or selects between real alternatives requires an ADR in [`docs/adr/`](docs/adr/README.md), using the template provided there.

## Definition of Done

A change is done when **all** of the following hold:

- [ ] Acceptance criteria of the linked issue are met.
- [ ] Automated tests cover the change and pass in CI (from M1 onwards).
- [ ] No accessibility violations reported by automated checks (from M1 onwards).
- [ ] Security and privacy impact considered (tenant isolation, personal data, consent).
- [ ] Documentation updated (ADR, SRS, glossary, README or module docs as relevant).
- [ ] `CHANGELOG.md` updated under `[Unreleased]` when the change is user-visible or structural.
- [ ] Deployed to a preview environment and verified (from M1 onwards).

## Language

Repository content (code, documentation, commits, issues) is written in **English**. The product UI is Spanish-first with full internationalisation (see ADR-0005).
