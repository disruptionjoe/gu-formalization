---
title: "Hourly 20260626 1102 Cycle 2 Tau No Declaration Branch Mode Firewall"
date: "2026-06-26"
run_id: "hourly-20260626-1102"
cycle: 2
lane: 2
doc_type: "frontier_run_lane_artifact"
artifact_id: "TauNoDeclarationBranchModeFirewall_1102_C2_L2_V1"
verdict: "closed_firewall_no_source_selected_branch_mode"
owned_path: "explorations/hourly-20260626-1102-cycle2-tau-no-declaration-branch-mode-firewall.md"
claim_status_change: false
---

# Hourly 20260626 1102 Cycle 2 Tau No Declaration Branch Mode Firewall

## 1. Verdict

Verdict: **closed branch-mode firewall**.

`NEGATIVE_NO_DECLARATION_SPAN` is now a use rule, not only a source-audit
result. When no tau omega variation declaration exists, the source-selected
branch-mode slot is empty:

```text
source_selected_tau_branch_mode = null
```

The following four names remain legal only as reconstruction-only modes:

```text
FREE_OVER_OMEGA1_ADP
GRAPH_CONSTRAINED_FIXED_ALEPH
GRAPH_CONSTRAINED_DYNAMIC_A
BACKGROUND_OR_NONVARIATION_POLICY
```

None may be used as a source-selected branch for exact-GR, theta, FLRW,
coefficient, residual, or source-law claims. A later worker may explore any of
them only with an explicit `reconstruction_only` label, a mode-specific
certificate, and a rollback condition saying that source-selection has not
been obtained.

Immediate decision:

```text
source_selected_branch_mode_present = false
reconstruction_only_modes_allowed = true
exact_gr_restart_allowed = false
theta_restart_allowed = false
```

## 2. What Was Derived Directly From Repo Sources

From `RESEARCH-POSTURE.md` and the five-lane runbook:

- compatibility, candidate algebra, and downstream usefulness cannot be
  promoted into derivation or source selection;
- live reconstruction branches must carry assumptions, falsification
  conditions, proof/speculation labels, dependency tracking, and anti-target
  guards;
- a lane should identify the first exact missing object rather than using a
  downstream physics target to choose it.

From `hourly-20260626-1102-cycle1-tau-omega-variation-source-span-audit.md`:

- the local source corpus contains tau/action ingredients, including an action
  object, omega fields, torsion-like expressions, and a displayed
  `varpi+s alpha` directional variation;
- the audited source spans do not declare which tau omega components are varied,
  which are held fixed, or whether the admissible domain is free, graph
  constrained, dynamic-A constrained, or background/nonvariation;
- the selected audit result is `NEGATIVE_NO_DECLARATION_SPAN`.

From `hourly-20260626-1003-cycle3-tau-source-locator-packet.md` and
`hourly-20260626-1003-cycle2-tau-beta-variation-domain-source-row.md`:

- the source-row verifier is defined, but its current repo-local output is
  `UNDECLARED`;
- `FREE_OVER_OMEGA1_ADP`, `GRAPH_CONSTRAINED_FIXED_ALEPH`, and
  `GRAPH_CONSTRAINED_DYNAMIC_A` were all checked as possible rows and not
  selected;
- exact-GR and theta restarts are barred until a positive non-UNDECLARED source
  branch exists.

From `gu-minimal-action-spec-2026-06-24.md` and
`primary-gu-interface-contract-2026-06-24.md`:

- if `beta` is freely and independently varied with only the bare theta norm,
  then the beta Euler-Lagrange equation forces `theta = 0`;
- nonzero-theta branches must therefore remove free beta variations, constrain
  them, replace the source with a total-current/dynamical IG law, or explicitly
  treat IG variables as background/spurions with a Noether cost;
- the relevant branch variants are branch-dependent and cannot be silently
  unified into one source law.

No exact-GR, theta, FLRW, DESI, coefficient, or residual target was used to
choose a branch mode.

## 3. Branch-Mode Firewall Table

| branch-mode name | source-selected status under no declaration | reconstruction-only use allowed | forbidden use | promotion condition |
|---|---|---|---|---|
| `FREE_OVER_OMEGA1_ADP` | not admitted | may be explored as `TauRecon_FreeOmega1AdP_FreeBetaCollapseControl_V1`, mainly to prove the free-beta negative control and check whether any added IG dynamics prevents `theta=0` | may not be cited from `G = H semidirect Omega^1`; may not support nonzero theta, exact-GR, or theta dark energy under only the bare theta norm; may not treat one `varpi+s alpha` derivative as full free-domain selection | a source or branch packet must explicitly admit arbitrary `delta beta` in the tau action and state the complete IG action/source law; if only `S_theta` is present, the admitted consequence is `theta=0`, not nonzero theta |
| `GRAPH_CONSTRAINED_FIXED_ALEPH` | not admitted | may be explored as `TauRecon_FixedAlephGraphPacket_V1` with a graph `Phi_tau^aleph(epsilon,beta,s)=0`, fixed reference `nabla_aleph`, tangent policy, and `D_A Phi_tau^aleph = 0` in the declared convention | may not treat tau-plus formulas, `A0`, `nabla_aleph`, or torsion notation as proof that the action field space is the graph; may not restart exact-GR/theta with a bare source law as source-selected | a source or proof packet must state that the tau action domain is this fixed-reference graph and must supply the graph equation, tangent space, and fixed-reference proof |
| `GRAPH_CONSTRAINED_DYNAMIC_A` | not admitted | may be explored as `TauRecon_DynamicAGraphMultiplierPacket_V1` with `Phi_tau(A,epsilon,beta,s)=0`, `D_A Phi_tau != 0`, and the resulting multiplier-current or corrected source law | may not use ambiguous `d_A` notation as dynamic-A selection; may not retain the bare source law `D_A^*F_A = theta` after introducing an A-dependent constraint; may not ignore multiplier currents | a source or proof packet must declare the A-dependent graph and derive the corrected A equation, including the multiplier-current term |
| `BACKGROUND_OR_NONVARIATION_POLICY` | not admitted | may be explored as `TauRecon_BackgroundSpurionPolicyPacket_V1` with `delta epsilon = delta beta = 0`, transformation rules, and an explicit Noether/gauge-covariance cost | may not silently hold IG variables fixed while claiming a variational theorem; may not treat display-level fixed `epsilon` or `metric` as a global nonvariation policy; may not claim generated theta/xi physics without the spurion cost | a source or proof packet must explicitly state the background/nonvariation policy or derive it as a gauge-fixed/spurion branch with the associated conservation-law cost |

Firewall rule for all rows:

```text
No declaration means no source-selected branch. Reconstruction labels may name
the mode, but they do not unlock exact-GR or theta branch claims.
```

## 4. Strongest Positive Reconstruction-Only Construction Attempt

The strongest positive reconstruction-only attempt is the fixed-aleph graph
sandbox, because it is the least invasive branch that can block arbitrary
`delta beta` without adding an A-dependent multiplier current:

```text
TauRecon_FixedAlephGraphPacket_V1

candidate field space:
  C_IG^aleph(s) = { (epsilon,beta) : Phi_tau^aleph(epsilon,beta,s) = 0 }

candidate graph shape:
  Phi_tau^aleph(epsilon,beta,s)
    = beta - d_{nabla_aleph}(epsilon) epsilon^{-1}

candidate tangent rule:
  D_beta Phi_tau^aleph(delta beta)
  + D_epsilon Phi_tau^aleph(delta epsilon)
  + D_s Phi_tau^aleph(delta s)
  = 0

fixed-reference rule:
  D_A Phi_tau^aleph = 0
```

If that packet were proved as a reconstruction branch, it would explain why
`beta` is not freely varied, avoid the immediate free-beta `theta=0` collapse,
and preserve a possible bare theta source law at reconstruction grade.

It still fails the firewall as a source-selected branch because the repo has
not supplied:

```text
source declaration that the tau action domain is C_IG^aleph(s);
derivation that Phi_tau^aleph is the action constraint rather than candidate algebra;
complete tangent theorem for epsilon, beta, s, and boundary variations;
proof that the fixed reference is held fixed under the action's delta_A convention.
```

The other reconstruction-only objects remain named but weaker for immediate
positive use:

```text
TauRecon_FreeOmega1AdP_FreeBetaCollapseControl_V1
TauRecon_DynamicAGraphMultiplierPacket_V1
TauRecon_BackgroundSpurionPolicyPacket_V1
```

## 5. First Exact Obstruction Or Missing Object

First exact obstruction:

```text
No source-selected tau branch-mode declaration exists.
```

This blocks writes to:

```text
source_selected_tau_branch_mode
source_selected_tau_source_law
source_selected_tau_exact_gr_input
source_selected_tau_theta_input
```

The missing source-promotion object is:

```text
SourceSelectedTauBranchModeDeclarationPacket_V1
```

Minimum fields:

```text
source_locator:
  file, section/page/equation span, and source status

action_object:
  action or variational sector governed by the declaration

selected_mode:
  one of FREE_OVER_OMEGA1_ADP,
  GRAPH_CONSTRAINED_FIXED_ALEPH,
  GRAPH_CONSTRAINED_DYNAMIC_A,
  BACKGROUND_OR_NONVARIATION_POLICY

variation_policy:
  varied omega components
  held-fixed omega components
  boundary/domain restrictions
  whether epsilon, beta/varpi, A, and s vary

mode_specific_data:
  free mode: beta domain and full IG action/source law
  fixed graph: graph equation, fixed reference, tangent rule, D_A Phi = 0
  dynamic graph: graph equation, D_A Phi != 0, multiplier-current policy
  background mode: nonvariation statement and Noether/gauge-covariance cost

anti_target_guard:
  selected mode unchanged after deleting exact-GR, theta, FLRW, DESI,
  coefficient, residual, and success-target labels
```

For the strongest fixed-aleph reconstruction attempt, the first missing proof
object is:

```text
TauFixedAlephGraphDerivationAndTangentCertificate_V1
```

Without that object, fixed-aleph remains a reconstruction hypothesis and not a
branch selected by GU source material.

## 6. Constructive Next Object

The constructive next object is a reconstruction branch packet, not an
exact-GR or theta computation:

```text
TauReconstructionOnlyBranchPacket_V1
```

One packet should be written per explored mode. Required fields:

```text
mode_name:
  one of the four firewall names

status:
  reconstruction_only

source_selection:
  false

field_space:
  complete admissible fields and tangent variations

action_terms:
  S_theta, S_IG, constraints, multipliers, cross terms, and boundary terms

EL_tuple:
  E_s, E_A, E_epsilon, E_beta, E_Psi, plus E_lambda or E_IG if present

source_law:
  bare theta source, corrected multiplier-current source, theta_eff,
  or background/spurion law, as appropriate

cost:
  free-beta collapse, fixed-graph proof debt, dynamic-A current, or Noether cost

claim_scope:
  what exact-GR/theta may cite as conditional reconstruction only

kill_condition:
  computation or proof failure that kills the branch
```

Priority order:

```text
1. TauRecon_FixedAlephGraphPacket_V1
2. TauRecon_DynamicAGraphMultiplierPacket_V1
3. TauRecon_BackgroundSpurionPolicyPacket_V1
4. TauRecon_FreeOmega1AdP_FreeBetaCollapseControl_V1
```

This order does not select a source branch. It only orders reconstruction work
by expected information gain: fixed-aleph first because it is the cleanest
nonzero-theta candidate; dynamic-A next because it is honest about corrected
source laws; background next because it can host theta but carries a Noether
cost; free beta last as the negative control unless extra IG dynamics is added.

## 7. Meaning For Exact-GR/Theta Claims

For exact-GR claims:

```text
exact_gr_restart_allowed = false
```

An exact-GR lane may say that the source-selected tau branch is blocked. It may
not choose fixed-aleph, dynamic-A, free-beta, or background policy because the
choice would help Schwarzschild/Kerr. A future exact-GR calculation may be run
only after a complete reconstruction-only branch packet exists, and even then
the result must be labeled conditional reconstruction rather than
source-selected GU.

For theta claims:

```text
theta_restart_allowed = false
```

The free-beta mode is currently a negative control: with only the bare theta
norm it kills nonzero theta. The fixed-aleph, dynamic-A, and background modes
can be named as possible nonzero-theta hosts, but none is admitted as a
source-selected theta branch. No FLRW theta-xi, DESI-sign, coefficient, or
theta dark-energy claim may cite these modes as GU-selected.

Allowed exact-GR/theta language:

```text
"blocked by absent source-selected tau branch mode"
"conditional on reconstruction-only branch packet X"
"negative control under free beta"
```

Forbidden exact-GR/theta language:

```text
"GU selects fixed-aleph graph"
"GU selects dynamic-A graph"
"GU holds beta background"
"the source action freely varies beta"
"exact GR/theta restarts from NEGATIVE_NO_DECLARATION_SPAN"
```

## 8. Terrain Classification, Forbidden Shortcut, Invariant, Kill Condition

Terrain classification:

```text
primary: provenance-verifier
secondary: branch-mode firewall
secondary: smooth-variational
secondary: gauge-slice/descent
guard: target-erasure anti-smuggling
```

Forbidden shortcut:

```text
Do not convert absence of a source declaration into permission to pick the
most useful reconstruction branch.

Do not treat ambient IG notation, one displayed varpi derivative, tau-plus
candidate algebra, ambiguous d_A notation, or display-level fixed variables as
source-selected branch modes.

Do not let exact-GR, theta, FLRW, DESI, coefficient, or residual success choose
between free, fixed-graph, dynamic-graph, and background modes.
```

Invariant:

```text
The firewall decision is unchanged under target-label erasure. If every
exact-GR, Schwarzschild, Kerr, theta, FLRW, DESI, xi, coefficient, and residual
phrase is replaced by a dummy label, source_selected_tau_branch_mode remains
null and all four positive modes remain reconstruction_only.
```

Kill condition:

```text
Kill any exact-GR/theta branch result that records one of the four modes as
source-selected without SourceSelectedTauBranchModeDeclarationPacket_V1.

Kill any reconstruction-only branch packet that omits its field space, tangent
policy, EL tuple, source-law cost, target-erasure guard, or rollback condition.
```

## 9. Certificate/Witness Shape

| certificate field | required witness |
|---|---|
| public inputs | posture, five-lane runbook, cycle-1 negative source-span audit, 1003 source-locator packet, 1003 source-row verifier, minimal action spec, primary interface contract |
| firewall witness | `source_selected_tau_branch_mode = null`; four positive names assigned only to `reconstruction_only_tau_modes` |
| mode witness | for each mode, a reconstruction object name, allowed use, forbidden use, and promotion condition |
| verifier predicate | a branch is source-selected iff `SourceSelectedTauBranchModeDeclarationPacket_V1` exists and names that branch with varied/held-fixed fields and target-erasure guard |
| semantic lift | no exact-GR or theta lift from the firewall; only future conditional reconstruction packets can be consumed |
| anti-smuggling guard | target-label erasure leaves the branch-mode decision unchanged |
| rollback condition | any artifact using a reconstruction-only mode as source-selected resets to blocked/underdefined |

Verifier predicate:

```text
SourceSelectedTauBranchModeAllowed(M) =
  M is one of the four named modes
  and SourceSelectedTauBranchModeDeclarationPacket_V1 exists
  and the packet declares the tau action field space
  and the packet states varied and held-fixed omega components
  and the packet supplies mode-specific tangent/source-law data
  and the selected mode survives target-label erasure.
```

Current result:

```text
SourceSelectedTauBranchModeAllowed(FREE_OVER_OMEGA1_ADP) = false
SourceSelectedTauBranchModeAllowed(GRAPH_CONSTRAINED_FIXED_ALEPH) = false
SourceSelectedTauBranchModeAllowed(GRAPH_CONSTRAINED_DYNAMIC_A) = false
SourceSelectedTauBranchModeAllowed(BACKGROUND_OR_NONVARIATION_POLICY) = false
```

Reconstruction predicate:

```text
ReconstructionOnlyTauModeAllowed(M) =
  M is one of the four named modes
  and the artifact labels M as reconstruction_only
  and it does not claim source selection
  and it gives field space, tangent policy, EL tuple, source-law cost,
  target-erasure guard, and kill condition.
```

Current result:

```text
ReconstructionOnlyTauModeAllowed(M) = true as a permission rule,
provided the mode-specific branch packet is written before physics claims use it.
```

## 10. JSON Summary

```json
{
  "artifact_id": "TauNoDeclarationBranchModeFirewall_1102_C2_L2_V1",
  "run_id": "hourly-20260626-1102",
  "cycle": 2,
  "lane": 2,
  "artifact_path": "explorations/hourly-20260626-1102-cycle2-tau-no-declaration-branch-mode-firewall.md",
  "verdict_class": "closed_firewall_no_source_selected_branch_mode",
  "firewall_defined": true,
  "firewall_applied": true,
  "source_selected_branch_mode_present": false,
  "reconstruction_only_modes_allowed": true,
  "exact_gr_restart_allowed": false,
  "theta_restart_allowed": false,
  "free_beta_branch_admitted": false,
  "fixed_aleph_graph_admitted": false,
  "dynamic_a_graph_admitted": false,
  "background_policy_admitted": false,
  "target_import_used": false,
  "claim_status_change": false,
  "source_selected_tau_branch_mode": null,
  "allowed_reconstruction_only_modes": [
    "FREE_OVER_OMEGA1_ADP",
    "GRAPH_CONSTRAINED_FIXED_ALEPH",
    "GRAPH_CONSTRAINED_DYNAMIC_A",
    "BACKGROUND_OR_NONVARIATION_POLICY"
  ],
  "reconstruction_only_objects_named": [
    "TauRecon_FreeOmega1AdP_FreeBetaCollapseControl_V1",
    "TauRecon_FixedAlephGraphPacket_V1",
    "TauRecon_DynamicAGraphMultiplierPacket_V1",
    "TauRecon_BackgroundSpurionPolicyPacket_V1",
    "TauReconstructionOnlyBranchPacket_V1"
  ],
  "source_promotion_object": "SourceSelectedTauBranchModeDeclarationPacket_V1",
  "strongest_reconstruction_only_attempt": "TauRecon_FixedAlephGraphPacket_V1",
  "first_exact_obstruction": "no_source_selected_tau_branch_mode_declaration",
  "constructive_next_object": "TauReconstructionOnlyBranchPacket_V1",
  "terrain": [
    "provenance-verifier",
    "branch-mode-firewall",
    "smooth-variational",
    "gauge-slice/descent"
  ],
  "forbidden_shortcut": "no_declaration_does_not_permit_target_selected_reconstruction_branch_as_source_selected",
  "invariant": "target_label_erasure_leaves_source_selected_tau_branch_mode_null",
  "kill_condition": "reset_exact_gr_theta_use_to_blocked_if_any_mode_is_source_selected_without_SourceSelectedTauBranchModeDeclarationPacket_V1"
}
```
