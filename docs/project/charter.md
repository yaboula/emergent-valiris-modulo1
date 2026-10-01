# Project charter

## Purpose

Build and commercialise **Storefront + Digital Menu** as the first Valiris Restaurants product for independent restaurants in Spain, with its necessary Core and a viable onboarding, design and support service. Use the work as the Valiris studio’s flagship portfolio evidence. The project must demonstrate end-to-end professional work: research, product definition, UX/UI, architecture, implementation, testing, security, documentation and delivery.

## Context and honesty statement

- This is a **studio-owned product**, not a commissioned project; no client or pilot participation is assumed.
- Existing competitive evidence and fictional scenarios inform design but do not validate demand, usability, purchasing or service economics.
- General competitive scouting is complete. New research answers specific launch decisions; real diner/operator checks belong in experience design and the pilot.
- Everything fictional is labelled. No client, testimonial, test result, paid commitment or metric is invented.
- M6 requires authorised real participants. Their absence blocks that evidence rather than permitting simulated replacement; independent preparation can continue.

## Quality bar

The target level is a **SaaS product in production, built by a small, demanding team**, comparable to a serious startup serving its first customers.

| In scope | Deliberately out of scope (over-engineering at this scale) |
| --- | --- |
| Production-quality code, risk-appropriate tests, CI/CD with preview deploys | Microservices, Kubernetes, multi-region |
| Security by design (OWASP ASVS L2 selection), tenant isolation enforced in the database | Formal certifications (SOC 2, ISO 27001) |
| Accessibility (WCAG 2.2 AA), performance budgets (Core Web Vitals) | Heavyweight process frameworks |
| Observability (errors, logs, key metrics) | 24/7 on-call |
| Documentation that a new engineer can use on day one | Exhaustive documentation of trivial code |

## Principles

1. **Evidence-based decisions.** Significant decisions are recorded as ADRs with alternatives and reasons.
2. **Official standards, proportionally applied.** Standards are the frame. We apply what adds value, and document what is omitted and why (see the table below).
3. **Documentation as code.** Docs live in the repository and are reviewed through pull requests.
4. **Quality built in, not bolted on.** Verification, accessibility and security accompany design and construction, with checks proportional to risk and behaviour.
5. **Security and privacy by design.** Tenant isolation, least privilege, data minimisation and a documented lawful basis for each purpose; optional promotional permission is separate from necessary service processing.
6. **Simple, but built to extend.** Build the necessary Core with first-product journeys. Future modules and verticals do not justify speculative infrastructure.
7. **Done means demonstrated.** Planning and design milestones close on evidence; software deliveries are checked in the appropriate environment from M3.
8. **Honesty.** No invented metrics or clients; limitations are documented.
9. **Visible craft.** UI detail, motion, copy, and empty and error states are part of the product.

## Standards and how they are tailored

| Standard | Applied to | Tailoring |
| --- | --- | --- |
| ISO/IEC/IEEE 29148:2018 | Requirements (`docs/srs.md`) | Uses relevant requirement quality criteria (necessary, unambiguous, verifiable…). Consolidate the launch commitment and construction criteria where useful; a full template set is not required. |
| ISO/IEC 25010:2023 | Quality attributes | Only the relevant characteristics are selected, each with a measurable target. |
| ISO/IEC/IEEE 29119 | Test strategy and manual testing | Uses the test strategy and test case concepts. The full documentation set is not produced. |
| ISTQB Foundation | Manual test design | Equivalence partitioning, boundary values, state transitions, exploratory charters. |
| C4 model | Architecture diagrams | Use only diagram levels needed to explain consequential responsibilities and interfaces. |
| MADR 4 | Architecture decisions | As is. |
| OWASP ASVS 4/5, STRIDE | Security requirements, threat model | L2 requirements are selected by relevance and traced to tests. |
| WCAG 2.2 AA | Accessibility | Full AA target on guest-facing and owner surfaces. |
| GDPR / LOPDGDD, LSSI-CE | Privacy and commercial communications | Compliance requirements live in the SRS. This is not legal advice. |
| Regulation (EU) 1169/2011 | Allergen information on menus | Record the applicable declared allergens for each dish, with missing/pending information explicit. Do not mark every dish with all 14 allergens or infer safety from an empty record. [AESAN guidance](https://eletiquetadocuentamucho.aesan.gob.es/alergias.html), checked 1 October 2026. |
| Conventional Commits, SemVer, Keep a Changelog | Versioning and history | As is. |

## Roles and decision-making

| Role | Who | Responsibilities |
| --- | --- | --- |
| Product owner and lead engineer | Studio founder | Owns vision, scope and priorities; researches, designs, implements, tests and documents; approves gates, ADRs and pull requests |

The [current roadmap](roadmap.md) defines outcome-based M0–M7 exit criteria. M0 commits launch scope; M1 checks experience; M2 prepares construction; M3–M5 implement; M6 pilots with real participants; M7 launches and operates. The former “problem validated”/“scope frozen” gates and automatic v1.1 deferral rule no longer govern execution.

Record material scope changes with rationale, impact and owner decision. An accepted capability is not dropped for technical convenience. Six responsibility areas coordinate work without implying six staffed teams; Yahya retains decision and merge authority.

## Initial risk register

| Risk | Likelihood | Impact | Response |
| --- | --- | --- | --- |
| Scope grows beyond first-product capacity | High | High | M0 capability commitments, explicit trade-offs, recalibration from real deliveries |
| Strong competitors and weak willingness-to-pay evidence | High | High | Specific hypotheses and real checks; distinguish interest, quotes and payments |
| Brand collision "Valiris" | Medium | High | Accepted risk in [ADR-0002](../adr/0002-studio-brand-valiris.md) |
| Maintenance duplicates restaurant work | High | High | Map actual sources and test publication, urgent changes and reviewed imports |
| Food-information or privacy promises exceed capabilities | Medium | High | Trace requirements to actual data/processes; do not infer safety or compliance |
| No real participants available | Unknown | High | Arrange authorised diner/operator participation; record M1 limitations and block missing M6 evidence |
| Service costs exceed the offer | Unknown | High | Measure onboarding, support and bespoke-design effort in M6; adjust commercial conditions |
| Future-module policies or dependencies | Unknown | Medium | Recheck when that module is prioritised; no fixed launch order |
