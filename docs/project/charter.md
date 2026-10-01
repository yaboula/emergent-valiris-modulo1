# Project charter

## Purpose

Build **Valiris Restaurants**, a production-grade platform for independent restaurants in Spain, and use it as the flagship portfolio product of the Valiris studio. The project must demonstrate end-to-end professional work: research, product definition, UX/UI, architecture, implementation, testing, security, documentation and delivery.

## Context and honesty statement

- This is a **studio-owned product**, not a commissioned project. There is no real client.
- Client input during discovery is replaced by:
  - **simulated restaurant owner interviews**, based on documented fictional profiles;
  - **public evidence**: competitor reviews, industry sources, regulations.
- Everything simulated is **labelled as simulated**. No client, testimonial or metric is invented. Numbers are published only when measured.

## Quality bar

The target level is a **SaaS product in production, built by a small, demanding team**, comparable to a serious startup serving its first customers.

| In scope | Deliberately out of scope (over-engineering at this scale) |
| --- | --- |
| Production-quality code, tests at every level, CI/CD with preview deploys | Microservices, Kubernetes, multi-region |
| Security by design (OWASP ASVS L2 selection), tenant isolation enforced in the database | Formal certifications (SOC 2, ISO 27001) |
| Accessibility (WCAG 2.2 AA), performance budgets (Core Web Vitals) | Heavyweight process frameworks |
| Observability (errors, logs, key metrics) | 24/7 on-call |
| Documentation that a new engineer can use on day one | Exhaustive documentation of trivial code |

## Principles

1. **Evidence-based decisions.** Significant decisions are recorded as ADRs with alternatives and reasons.
2. **Official standards, proportionally applied.** Standards are the frame. We apply what adds value, and document what is omitted and why (see the table below).
3. **Documentation as code.** Docs live in the repository and are reviewed through pull requests.
4. **Quality built in, not bolted on.** Tests, accessibility and security are part of every story. Untested means not done.
5. **Security and privacy by design.** Tenant isolation, least privilege, data minimisation and a documented lawful basis for each purpose; optional promotional permission is separate from necessary service processing.
6. **Simple, but built to extend.** Build what v1.0 needs (YAGNI), behind clear boundaries: platform, vertical, app, and modules.
7. **Demonstrable outcomes.** M0 delivers reviewed documentation; construction milestones deliver usable software. The current first-product roadmap supersedes the historical milestone mapping.
8. **Honesty.** No invented metrics or clients; limitations are documented.
9. **Visible craft.** UI detail, motion, copy, and empty and error states are part of the product.

## Standards and how they are tailored

| Standard | Applied to | Tailoring |
| --- | --- | --- |
| ISO/IEC/IEEE 29148:2018 | Requirements (`docs/srs.md`) | Uses its structure and its requirement quality criteria (necessary, unambiguous, verifiable…). Stakeholder and system requirement documents are merged into one SRS. |
| ISO/IEC 25010:2023 | Quality attributes | Only the relevant characteristics are selected, each with a measurable target. |
| ISO/IEC/IEEE 29119 | Test strategy and manual testing | Uses the test strategy and test case concepts. The full documentation set is not produced. |
| ISTQB Foundation | Manual test design | Equivalence partitioning, boundary values, state transitions, exploratory charters. |
| C4 model | Architecture diagrams | Levels 1–3; level 4 only where it adds clarity. |
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

**Gates** are formal go/no-go reviews:
- Gate 1: problem validated.
- Gate 2: scope frozen.
- One release gate per milestone.

After Gate 2, any new scope goes to the v1.1 backlog.

## Initial risk register

| Risk | Likelihood | Impact | Response |
| --- | --- | --- | --- |
| Scope of 7 modules exceeds the timeline | High | High | "Thin but complete" scope per module, frozen at Gate 2 |
| Strong incumbents in Spain (Qamarero, EterSystem, TheFork, CoverManager) | Certain | Medium | Explicit differentiation defined in M0.2/M0.3. For a portfolio product, depth of execution matters more than market share |
| Brand collision "Valiris" | Medium | High | Accepted risk; mitigations in [ADR-0002](../adr/0002-studio-brand-valiris.md) |
| WhatsApp Business Platform constraints (verification, templates, pricing) | High | Medium | Module scheduled last (M7); test number in development; email and `wa.me` fallback |
| Legal requirements (consent, allergens, deposits/SCA) misunderstood | Medium | High | Dedicated legal research in M0.2; requirements traced in the SRS |
| No real users for validation | Certain | Medium | Simulated client plus public evidence; usability tests with 3–5 people in M8 |
