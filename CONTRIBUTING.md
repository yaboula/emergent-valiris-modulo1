# Contributing to Valiris Restaurants

This guide defines how work flows through the repository. It applies to documentation and code alike: documentation is treated as code.

## Roles

| Role | Responsibility |
| --- | --- |
| Product owner and lead engineer | Owns vision, scope and priorities; designs, implements and documents; approves gates, ADRs and pull requests |

## Workflow

1. **Every change starts from an issue** (user story, task, research or bug) assigned to a milestone (`M0`–`M7`).
2. **Create a short-lived branch from `main`** using the naming convention below. If a change depends on an unmerged PR, stack its branch and PR on that dependency, state the review order, and transplant only the dependent commits after the earlier squash merge; retarget and check the resulting diff.
3. **Open a pull request early**, fill in the template, link the issue (`Closes #123`).
4. **The pull request is merged only when it meets the Definition of Done** and the authorised review is complete. The product owner may delegate review and merge of approved work; material product decisions remain with the owner. Keep branch protections active.
5. **Merge strategy: squash merge.** The squash commit message follows Conventional Commits.

`main` remains reviewable and coherent. M0–M2 deliver decisions, prototypes and preparation, not usable-application releases. Software deliveries begin in M3 and integrate earlier work. Deployed releases are identifiable with relevant notes; a tag is not required for every task. `v1.0.0` is the first commercial Storefront + Digital Menu release with necessary Core. See [the roadmap](docs/project/roadmap.md).

## Branch naming

```text
<type>/<milestone>-<short-description>
```

Examples: `docs/m0-research-competitors`, `feat/m3-menu-publication`, `fix/m4-menu-allergen-labels`.

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
- [ ] Risk-appropriate automated and manual checks cover the change; construction CI passes from M3. No implementation tests are required for unrelated documentation edits.
- [ ] Relevant accessibility checks are completed: design review in M1 and automated/manual implementation checks from M3.
- [ ] Security and privacy impact considered (tenant isolation, personal data, consent).
- [ ] Documentation updated (ADR, SRS, glossary, README or module docs as relevant).
- [ ] `CHANGELOG.md` updated under `[Unreleased]` when the change is user-visible or structural.
- [ ] Outcome is demonstrable; software changes are verified in the appropriate environment from M3. Planning/design deliverables do not require application deployment.

## Language

Repository content (code, documentation, commits, issues) is written in **English**. The product UI is Spanish-first with full internationalisation (see ADR-0005).
