---
status: accepted
date: 2026-09-28
deciders: Product owner
---

# ADR-0002: Keep "Valiris" as the studio brand despite a name collision

## Context and problem statement

"Valiris" is the brand of the software studio that builds this product line. A pre-launch check on 2026-09-28 found that the name is already in use:

**Evidence clarification, 1 October 2026:** the historical findings below are unverified leads, not reproduced registry, website, DNS or trademark findings. Each company identifier, activity/date, product description, launch date, social handle, domain and search result remains unverified because no dated primary lookup record was retained. The accepted brand choice is unchanged; none of these leads establishes legal clearance or a registered right. Recheck the actual primary records before commercial use as required by the mitigations below.

| Finding | Detail | Relevance |
| --- | --- | --- |
| VALIRIS SAS, Paris (SIREN 101 335 990) | Registered 2026-02-13, NAF 6201Z (computer programming). Product: AI guest-messaging and upsell software for short-term rental managers. Uses `valiris.io` and LinkedIn `valirisfr`. Public launch July 2026. | **High**: same activity (software) and adjacent sector (hospitality, AI messaging) |
| VALIRIS SARL, Sanilhac (SIREN 342 442 969) | Business support services, active since 1987 | Low: unrelated sector |
| VALIRIS SAS, Saumur | Active since 2012 | Low: unrelated sector |
| Domains | `valiris.es` and `valiris.app` resolve (registered); `valiris.dev` does not resolve (indicative only) | Medium |
| Trademarks | No trademark found in a web search; the INPI/EUIPO databases were not queried directly | Unknown |

Should the studio keep the "Valiris" brand?

## Decision drivers

- Owner's preference and existing attachment to the brand.
- Legal risk of a future trademark conflict.
- Discoverability: search results for "Valiris software" currently point to the Paris company.
- Cost of renaming, which grows over time.

## Considered options

1. Keep "Valiris" and mitigate the risks
2. Adopt a new studio name now

## Decision outcome

Chosen option: **Keep "Valiris"**, decided by the product owner with the risks explicitly accepted.

### Consequences

- Bad / accepted risk: if the Paris company registers the trademark in classes 9/42, it could oppose the use of "Valiris" for software in the EU, forcing a rebrand after the portfolio and client relationships are built.
- Bad / accepted risk: reduced discoverability of the studio by name alone.

### Mitigations

- The brand is always used together with a descriptive product name (e.g. "Valiris Restaurants"), never alone as a product name.
- No AI guest-messaging product will be marketed under "Valiris" alone, to avoid direct confusion with the Paris company's offering.
- Before any commercial launch, public marketing spend or trademark filing, the INPI (DATA INPI) and EUIPO (eSearch plus) databases are queried directly and this ADR is revisited.
- Brand assets (logo, domain) are kept easy to replace: the name appears in configuration and theme tokens, not hard-coded throughout the code.

### Confirmation

This ADR is reviewed at the M8 release gate and before any commercial use.

## More information

- INPI trademark database: https://data.inpi.fr
- EUIPO eSearch plus: https://euipo.europa.eu/eSearch/
