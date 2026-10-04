---
status: proposed
date: 2026-10-02
deciders: Product owner
---

# ADR-0010: Share diner identity, scope preferences by venue and hide unconfirmed display prices

## Context and problem statement

ADR-0009 accepted authenticated registered-diner personalisation but left account scope, inputs and authentication method for focused design/M2 work. J10–J15 also require a clear difference between a diner reading a loaded historical snapshot and an unattended venue display presenting an offering as current. The owner selected the directions below on 2 October and subsequently authorised implementation of the descriptive design plan.

This record remains **proposed** in the draft PR under the repository ADR review process. That status does not reopen the explicitly selected design directions; it records that the ADR's integration/review and consequential technical contracts are not completed. No accepted historical ADR is changed.

## Decision drivers

- Keep public consultation, venue-curated suggestions and local comparison account-free.
- Give diners one recognisable identity without carrying a private preference profile across restaurants or granting staff permissions.
- Use deliberate inputs with honest diet/allergen/nutrition limits rather than inventing behavioural history.
- Make unattended-display uncertainty unmistakable when staff cannot monitor every viewer.
- Preserve complete launch scope and identify actual identity, data, content and freshness dependencies.

## Considered options

1. Separate diner accounts per restaurant; one Valiris account with a shared global preference profile; one Valiris account with venue-scoped preferences.
2. Tastes only; tastes and declared diet; tastes and budget. Behavioural history is not established as an available input.
3. Email-link access; email and password, including registration/verification/recovery.
4. Display the old priced menu with an age warning during uncertainty; remove unconfirmed prices/availability and retain venue identity/staff guidance.

## Decision outcome

Owner-selected design directions:

- **One Valiris diner account with preferences scoped by venue.** Restaurants cannot inspect the private profile; diner sign-in grants no restaurant-management authorisation. Technical provider, identity/session permissions and storage remain M2 decisions.
- **Explicit tastes and declared diet.** The approved descriptive plan starts with published venue categories and Sin preferencia / Vegetariano / Vegano, matching diet only against restaurant-confirmed attributes. No inference from a dish name, budget input, invented visits/purchases, stored medical-allergy profile or personal food-safety guarantee is introduced.
- **Email and password.** Include optional registration, verification, sign-in, password recovery, sign-out and account controls while retaining public reading. Exact provider, policies, mail/token/session protections and account access/removal/retention effects need #4 review before affected closure and implementation.
- **Remove unconfirmed prices and availability from unattended displays.** Retain venue identity and a staff-consultation message until a coherent applicable publication is confirmed. Dependent item/food/nutrition assertions are also removed from this recovery composition so it cannot imply an old menu is current. Detection and recovery timing need engineering specification and actual tests.

The handset offline reader remains a deliberately labelled historical loaded snapshot with version/time/coverage and stale-price/availability warning; it is not the unattended-display policy. Do not cache private account/preferences/personalised results in that public snapshot. Account switch/sign-out clears private state and the session's local comparison list; server-side session invalidation remains an implementation obligation, with unknown/offline logout represented honestly.

These directions supplement ADR-0009 without changing the 72-row launch commitment or separate S1/S2 mapping. Recommendation ranking, category lifecycle, verification-before-personalisation and recovery session handling in the [extended storyboard](../design/m1-extended-journeys.md) are reviewable design proposals, not claims of accepted engineering contracts.

### Consequences

- Diner: one access route and deliberate local preferences, with registration/recovery effort. Diet matches remain limited by explicit venue data; public reading is always available.
- Restaurant: no private diner-profile access; content/diet/nutrition declarations need authorised maintenance. During display uncertainty, staff must answer offering/price questions. No time saving or additional sales is demonstrated.
- Valiris: shared identity, per-venue private inputs, source-dependent matching and robust display recovery add data/security/operation responsibilities. No provider spend, commercial margin, schedule or implementation is established.
- Accepted trade-off: no private offline personalisation; hide unsaved private form/results when session/connection cannot be authorised. Unattended display sacrifices menu detail during uncertainty instead of continuing a stale priced presentation.

### Confirmation

Trace J15.1–J15.6 to anonymous/registration/verification/recovery/preferences/results/no-match/sign-out/account-control states, including diner A/B and second-venue isolation. Trace J12.1–J12.3 to dedicated source/context/layout, removal of old price/stock on uncertainty and coherent restore. Review J10 offline differences and known allergen/diet/nutrition limits across outputs. Author document walkthroughs are separate from independent G4/G3 review and real-user/device/runtime proof; none closes M1 alone.

## Pros and cons of the options

- Per-restaurant accounts make scope locally obvious but require repeated access. A global profile reduces re-entry but carries preferences across venue context. The chosen shared identity/local profile needs both clear UI scope and data isolation.
- Tastes only avoid diet-attribute intake but do not satisfy the selected input family. Budget adds price-target interpretation and was not selected. Declared diet supports explicit filtering with a real source/review burden; it cannot infer safe food.
- Email-link access avoids password management but requires a different mail/session flow. Email/password is the selected method and requires password-manager support, verification, recovery and security review; no provider capability is presumed.
- A warned old display preserves detail but may be read as current from a distance. The chosen withdrawal policy is clearer during uncertainty but requires staff fallback and dependable freshness detection.

## More information

[ADR-0009](0009-studio-design-and-registered-diner-personalisation.md), [J10–J15 criteria](../product/m0-journeys-and-criteria.md), [extended design and review/dependency register](../design/m1-extended-journeys.md), [M1 #5](https://github.com/yaboula/valiris-restaurants/issues/5), [technical preparation #4](https://github.com/yaboula/valiris-restaurants/issues/4). Revisit material directions only through an explicit owner decision supported by concrete review evidence; unresolved technical details are not permission to silently change accepted scope.
