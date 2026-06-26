---
title: "Hourly 20260626 1102 Cycle 1 Tau Omega Variation Source Span Audit"
date: "2026-06-26"
run_id: "hourly-20260626-1102"
cycle: 1
lane: 2
doc_type: "frontier_run_lane_artifact"
artifact_id: "TauActionOmegaVariationDeclarationSourceSpanAudit_1102_C1_L2_V1"
verdict: "NEGATIVE_NO_DECLARATION_SPAN"
owned_path: "explorations/hourly-20260626-1102-cycle1-tau-omega-variation-source-span-audit.md"
claim_status_change: false
---

# Hourly 20260626 1102 Cycle 1 Tau Omega Variation Source Span Audit

## 1. Verdict

Verdict: **NEGATIVE_NO_DECLARATION_SPAN**.

The local 2021 draft is present:

```text
Geometric_UnityDraftApril1st2021.pdf
```

The audited draft windows contain a real tau/action source cluster:

```text
G = H semidirect N
N = Omega^1(Y, ad(P_H))
omega = (epsilon, varpi)
T_omega / T_g as augmented or displaced torsion
I_1^B : G x MET(X^{1,3}) -> R
I_2^B = ||Upsilon_omega^B||^2
S_GU comparison in Section 12.4
```

The source also contains one displayed directional variation in the varpi
direction:

```text
d/ds I_1^B((epsilon_Y, varpi_Y + s alpha), metric_X)
```

That is not enough to select an admissible omega-domain. No audited span
explicitly declares, for the tau sector, which omega components are varied,
which are held fixed, and whether the admissible variation domain is:

```text
FREE_OVER_OMEGA1_ADP
GRAPH_CONSTRAINED_FIXED_ALEPH
GRAPH_CONSTRAINED_DYNAMIC_A
BACKGROUND_OR_NONVARIATION_POLICY
```

Therefore the selected audit enum is:

```text
NEGATIVE_NO_DECLARATION_SPAN
```

No exact-GR restart and no theta restart are allowed from this artifact.

## 2. What Was Derived Directly From Repo Sources

Directly from `Geometric_UnityDraftApril1st2021.pdf`:

- Sections 5.2-5.4, PDF pp. 32-33, define the ambient function spaces and
  inhomogeneous gauge group: `A = Conn(P_H)`, `N = Omega^1(Y, ad(P_H))`, and
  `G = H semidirect N`, with natural left/right actions on the connection
  affine space.
- Sections 6.1-6.4, PDF pp. 36-39, introduce a base connection `A0`, the
  tilted map into `G`, a projection/surjection from `G` to `N`, and the
  bi-connection map. These are reference-connection and quotient/projection
  structures, not action-domain variation declarations.
- Section 7.1, PDF p. 40, defines augmented torsion from a group element in
  `G`, normalized in prior repo transcription as
  `T_g = varpi - epsilon^-1 d_A0 epsilon`.
- Section 9.1, PDF pp. 43-45, defines the first-order bosonic action
  `I_1^B : G x MET(X^{1,3}) -> R`, expands it using shifted torsion,
  the Shiab contraction, `B_omega`, curvature, and Chern-Simons-like terms,
  and displays the varpi-direction first variation.
- Section 9.2, PDF pp. 45-47, gives the second-order bosonic action
  `I_2^B = ||Upsilon_omega^B||^2` and the second-order equation
  `D_omega^* Upsilon_omega = 0`.
- Section 12.4, PDF pp. 56-57, compares the GU expression to a
  Chern-Simons-like form and states the omega/context formulas normalized in
  prior repo transcription as `omega=(epsilon,varpi)`, `varpi` measured
  relative to the Levi-Civita spin connection, and
  `T_omega = varpi - epsilon^-1 d_{nabla^g} epsilon`.

Directly from prior repo artifacts:

- `hourly-20260626-1003-cycle2-tau-beta-variation-domain-source-row.md`
  defines the verifier row and returns `UNDECLARED`.
- `hourly-20260626-1003-cycle3-tau-source-locator-packet.md` records that
  the strongest candidate source locator is the Section 9.1 action window,
  but that it lacks the required admissible variation-domain declaration.
- `hourly-20260626-0904-cycle3-tau-field-space-trichotomy.md` keeps
  `FULL_IG_FREE_BETA`, `FIXED_ALEPH_GRAPH`, and `DYNAMIC_A_GRAPH`
  logically possible but unselected.
- `gu-minimal-action-spec-2026-06-24.md` and
  `primary-gu-interface-contract-2026-06-24.md` explain why this is
  load-bearing: free independent beta variation against only a bare theta norm
  forces `theta = 0`, so nonzero-theta branches require an explicit variation
  branch or nonvariation/constraint policy.

No downstream exact-GR, theta, FLRW, coefficient, residual, or target-success
criterion was used to choose the enum.

## 3. Span Table

| source span | action_object | omega_field_list | directional_variation | admissible_variation_domain | held_fixed_policy | reference_connection_role | graph_or_free_enum |
|---|---|---|---|---|---|---|---|
| Draft Sections 5.2-5.4, PDF pp. 32-33 | none; ambient connection-space and group definitions | `epsilon in H`, `varpi in N = Omega^1(Y, ad(P_H))`, `G = H semidirect N` | none | not declared; field space is defined, not varied | none | no selected action reference; only affine connection space `A` | `NEGATIVE_NO_DECLARATION_SPAN` |
| Draft Section 6.1, PDF p. 36 | none | `h in H`, base connection `A0`, induced second component in `G` | none | not declared | none | fixed base/reference connection `A0` defines tilted embedding | `NEGATIVE_NO_DECLARATION_SPAN` |
| Draft Sections 6.2-6.4, PDF pp. 37-39 | none | `g=(epsilon,varpi)` plus projection to `N`; bi-connection sections | none | not declared | none | `A0` supplies projection/bi-connection reference; no tau action variation policy | `NEGATIVE_NO_DECLARATION_SPAN` |
| Draft Section 7.1, PDF p. 40 | none; action input field only | `g=(epsilon,varpi)`, `T_g = varpi - epsilon^-1 d_A0 epsilon` in normalized repo transcription | none | not declared | none | fixed `A0` appears inside augmented torsion | `NEGATIVE_NO_DECLARATION_SPAN` |
| Draft Section 9.1, PDF pp. 43-44, eqs. 9.1-9.6 | yes: `I_1^B : G x MET(X^{1,3}) -> R`; expanded first-order bosonic action | `omega_Y=(epsilon_Y,varpi_Y)`; `T_omega`, `B_omega`, `F_{B_omega}` | EL packet `dI_1^B=(Upsilon_omega,Xi_omega)`; no component policy in pp. 43-44 | not declared; action domain `G x MET` is not an admissible variation-domain declaration | none | Levi-Civita/spin connection appears through `B_omega` and shifted torsion | `NEGATIVE_NO_DECLARATION_SPAN` |
| Draft Section 9.1, PDF p. 45, eqs. 9.7-9.10 | yes: same `I_1^B` | displayed as `(epsilon_Y, varpi_Y+s alpha)` with `metric_X` | yes: varpi-direction derivative against `alpha` | not declared; a single displayed derivative does not state the full tau omega field space, graph, or background policy | display keeps `epsilon_Y` and `metric_X` fixed for that derivative only; not a global held-fixed policy | `B_omega` and torsion objects appear, but no fixed-versus-dynamic reference rule is declared | `NEGATIVE_NO_DECLARATION_SPAN` |
| Draft Section 9.2, PDF pp. 45-47, eqs. 9.11-9.15 | yes: `I_2^B = ||Upsilon_omega^B||^2` | inherited `omega` from Section 9.1 | yes: second-order variation/equation `D_omega^* Upsilon_omega = 0` | not declared | no explicit omega held-fixed declaration | `D_omega` is an operator in the bosonic EL bridge; not a reference-graph policy | `NEGATIVE_NO_DECLARATION_SPAN` |
| Draft Section 12.4, PDF pp. 56-57, eqs. 12.4-12.7 | yes: Chern-Simons/GU comparison expression `S_GU(...)` | `omega=(epsilon,varpi)`, `T_omega = varpi - epsilon^-1 d_{nabla^g} epsilon` in prior transcription | none as an admissible-domain declaration | not declared | none | comparison distinguishes trivial connection and Levi-Civita spin connection measurements; no graph/free/background policy | `NEGATIVE_NO_DECLARATION_SPAN` |

Audit conclusion from the table:

```text
action_object_found = true
directional_varpi_variation_found = true
positive_variation_domain_declaration_found = false
```

## 4. Strongest Positive Construction Attempt

The strongest positive construction is:

```text
Candidate A:
  source span:
    Draft Section 9.1, PDF pp. 43-45
  action object:
    I_1^B((epsilon_Y,varpi_Y), metric_X)
  directional variation:
    d/ds I_1^B((epsilon_Y,varpi_Y+s alpha), metric_X)
  positive reading attempted:
    varpi admits at least one displayed infinitesimal direction alpha.
```

This candidate almost looks like `FREE_OVER_OMEGA1_ADP`, but it fails the
required source-declaration test. The source has not said:

```text
alpha ranges over the full Omega^1(Y, ad(P_H)) action tangent space;
epsilon is held fixed as a policy rather than only in this displayed derivative;
varpi/beta is freely varied as the tau sector's admissible domain;
graph constraints are absent;
the reference connection is fixed rather than dynamical;
background/nonvariation policy is intended or rejected.
```

The function type `I_1^B : G x MET -> R` also does not close the gap. It
states where the action can be evaluated, not which directions are admissible
when deriving the tau equations.

Therefore Candidate A is a positive action/EL locator and a positive
varpi-direction derivative locator, but it is not a positive omega variation
domain declaration.

## 5. First Exact Obstruction Or Missing Object

First exact obstruction:

```text
No audited source span declares the tau action's admissible
omega=(epsilon,varpi/beta) variation domain with varied components,
held-fixed components, and reference-connection policy.
```

The missing object is:

```text
TauActionOmegaVariationDeclarationPacket_V1
```

Minimum required fields:

```text
source_locator:
  source file, section, page/equation span, source status

action_object:
  the action or variational sector governed by the declaration

omega_dictionary:
  source epsilon, varpi, omega, A0, B_omega, T_omega
  mapped to repo epsilon, beta/varpi, A, nabla_aleph, theta conventions

variation_declaration:
  varied omega components
  held-fixed omega components
  boundary/domain restrictions
  statement that the declaration applies to the tau sector

admissible_domain_enum:
  FREE_OVER_OMEGA1_ADP
  GRAPH_CONSTRAINED_FIXED_ALEPH
  GRAPH_CONSTRAINED_DYNAMIC_A
  BACKGROUND_OR_NONVARIATION_POLICY

if graph-shaped:
  graph equation
  fixed-reference versus dynamic-A role
  tangent policy
  multiplier-current policy if D_A Phi != 0

if background/nonvariation:
  explicit nonvariation statement and Noether/gauge-covariance cost

anti_target_guard:
  enum unchanged after exact-GR/theta/FLRW/coefficient target labels are erased
```

The first failed field in the strongest source span is:

```text
variation_declaration
```

## 6. Constructive Next Object

The next object should be a branch-opening declaration packet, not another
downstream computation:

```text
TauActionOmegaVariationDeclarationPacket_V1
```

It can be filled in one of two honest ways:

1. Source-positive route: find a source span, note, erratum, transcript, or
   author-level declaration that explicitly states the tau omega variation
   policy, then re-run this audit.
2. Reconstruction route: declare a reconstruction branch as a reconstruction
   object, not as a source declaration, and name the branch cost:
   free-beta collapse, fixed-reference graph proof debt, dynamic-A multiplier
   current, or background/spurion Noether cost.

Acceptance test:

```text
Accept a positive packet only if deleting every exact-GR/theta/FLRW target
phrase leaves the same selected omega-domain enum.
```

## 7. Meaning For Exact-GR/Theta Restart

Exact-GR restart:

```text
exact_gr_restart_allowed = false
```

Reason: the action/source-law tuple still lacks a source-selected tau omega
variation branch. Schwarzschild/Kerr or GR utility cannot choose between free,
fixed-graph, dynamic-graph, or background omega policies.

Theta restart:

```text
theta_restart_allowed = false
```

Reason: theta claims are directly sensitive to beta/varpi variation. A free
beta reading with only the bare theta norm kills nonzero theta, while graph or
dynamic branches need the missing source-declared tangent/current policy.

No target import was used.

## 8. Terrain Classification And Guardrails

Terrain classification:

```text
primary: provenance-verifier
secondary: smooth-variational
secondary: gauge-slice/descent
guard: target-erasure anti-smuggling
```

Forbidden shortcut:

```text
Do not promote G = H semidirect N into FREE_OVER_OMEGA1_ADP.
Do not promote I_1^B : G x MET -> R into an admissible variation domain.
Do not promote d/ds I_1^B((epsilon,varpi+s alpha),metric) into a full omega policy.
Do not promote T_omega = varpi - epsilon^-1 d_A0 epsilon into a graph constraint.
Do not use d_A/A0 notation to select fixed-aleph or dynamic-A.
Do not choose the enum because exact-GR or theta would benefit from it.
```

Invariant:

```text
The selected enum must be source-span invariant and target-label invariant.
If all exact-GR, theta, FLRW, DESI, coefficient, and residual labels are
replaced by dummy names, the enum must not change.
```

Kill condition:

```text
Kill any positive variation-domain enum unless the cited source span explicitly
declares varied/held-fixed omega components and the admissible tau omega domain.
```

Current kill condition result:

```text
positive enum killed
selected enum = NEGATIVE_NO_DECLARATION_SPAN
```

## 9. Certificate/Witness Shape

| certificate field | witness in this audit |
|---|---|
| public inputs | required posture/runbook files; prior tau source-row/locator/trichotomy artifacts; minimal action/interface contracts; local 2021 draft PDF |
| source spans audited | draft Sections 5.2-5.4, 6.1-6.4, 7.1, 9.1, 9.2, 12.4 |
| action witness | present: `I_1^B : G x MET(X^{1,3}) -> R`, `I_2^B`, Section 12.4 `S_GU` comparison |
| omega witness | present: `omega=(epsilon,varpi)`, `N=Omega^1(Y,ad(P_H))`, `T_omega/T_g` |
| directional variation witness | present: `varpi_Y+s alpha` derivative in Section 9.1 |
| admissible-domain witness | absent |
| held-fixed policy witness | absent as a policy; only display-level fixed `epsilon_Y` and `metric_X` in one derivative |
| reference-role witness | present as `A0`/Levi-Civita/reference connection context, absent as fixed-vs-dynamic variation policy |
| enum witness | `NEGATIVE_NO_DECLARATION_SPAN` |
| verifier predicate | accept a positive enum only from explicit varied/held-fixed/domain declaration |
| semantic lift | no exact-GR or theta branch unlock |
| anti-smuggling guard | target labels were not used; target-erasure leaves verdict unchanged |
| rollback condition | any positive enum based only on field definitions, action type, one derivative, or target utility resets to negative |

Verifier predicate:

```text
SourceSpanDeclaresTauOmegaDomain(S) =
  S has a tau/action object
  and S lists omega components
  and S states which omega components are varied
  and S states which omega components are held fixed
  and S declares free/graph/dynamic/background admissible domain
  and S is target-label invariant.
```

For the strongest source span:

```text
SourceSpanDeclaresTauOmegaDomain(Section_9_1_pp_43_45) = false
```

because the admissible-domain declaration is absent.

## 10. JSON Summary

```json
{
  "artifact_id": "TauActionOmegaVariationDeclarationSourceSpanAudit_1102_C1_L2_V1",
  "run_id": "hourly-20260626-1102",
  "cycle": 1,
  "lane": 2,
  "artifact_path": "explorations/hourly-20260626-1102-cycle1-tau-omega-variation-source-span-audit.md",
  "source_span_audit_attempted": true,
  "local_2021_draft_pdf_present": true,
  "source_spans_audited": [
    "5.2-5.4",
    "6.1-6.4",
    "7.1",
    "9.1",
    "9.2",
    "12.4"
  ],
  "action_object_found": true,
  "omega_field_list_found": true,
  "directional_varpi_variation_found": true,
  "positive_variation_domain_declaration_found": false,
  "selected_variation_domain_enum": "NEGATIVE_NO_DECLARATION_SPAN",
  "free_over_omega1_adp_declared": false,
  "graph_constrained_fixed_aleph_declared": false,
  "graph_constrained_dynamic_a_declared": false,
  "background_or_nonvariation_policy_declared": false,
  "exact_gr_restart_allowed": false,
  "theta_restart_allowed": false,
  "target_import_used": false,
  "claim_status_change": false,
  "first_exact_obstruction": "TauActionOmegaVariationDeclarationPacket_V1_absent",
  "constructive_next_object": "TauActionOmegaVariationDeclarationPacket_V1",
  "terrain": [
    "provenance-verifier",
    "smooth-variational",
    "gauge-slice/descent"
  ],
  "forbidden_shortcut": "field_definition_or_action_type_or_single_directional_derivative_as_variation_domain_declaration",
  "invariant": "source_span_and_target_label_erasure_do_not_change_selected_enum",
  "kill_condition": "reset_to_NEGATIVE_NO_DECLARATION_SPAN_without_explicit_varied_held_fixed_omega_domain_declaration"
}
```

## Sources Read And Verification Notes

Required sources read:

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/hourly-20260626-1003-cycle3-tau-source-locator-packet.md`
- `explorations/hourly-20260626-1003-cycle2-tau-beta-variation-domain-source-row.md`
- `explorations/hourly-20260626-0904-cycle3-tau-field-space-trichotomy.md`
- `explorations/gu-minimal-action-spec-2026-06-24.md`
- `explorations/primary-gu-interface-contract-2026-06-24.md`
- `sources/media-index.md`

Additional repo-local manuscript transcription rows checked:

- `explorations/hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md`
- `explorations/hourly-20260625-0601-cycle1-author-manuscript-dgu-01-operator-receipt-candidate.md`
- `explorations/hourly-20260625-0502-cycle2-author-manuscript-ig-selector-receipt-gate.md`
- `explorations/hourly-20260625-0301-cycle2-manuscript-ig-selector-identity-packet.md`

Verification performed:

```text
confirmed Geometric_UnityDraftApril1st2021.pdf is present locally
extracted target PDF windows with local pypdf
confirmed owned output path did not exist before writing
created only the owned output artifact
did not edit tests, canon, status, or claim-ledger files
did not commit or push
```
