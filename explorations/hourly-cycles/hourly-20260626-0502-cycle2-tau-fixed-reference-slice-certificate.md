---
title: "Hourly 20260626 0502 Cycle 2 Tau Fixed Reference Slice Certificate"
date: "2026-06-26"
status: exploration
doc_type: frontier_run_lane_artifact
run_id: "hourly-20260626-0502"
cycle: 2
lane: "TauFixedReferenceSliceCertificate"
artifact_id: "TauFixedReferenceSliceCertificate_2A_V0"
verdict: "NOT_ADMITTED_TAU_PLUS_EQUIVARIANCE_ONLY_NO_SOURCE_LOCKED_FIXED_REFERENCE_GRAPH"
owned_path: "explorations/hourly-20260626-0502-cycle2-tau-fixed-reference-slice-certificate.md"
claim_status_change: false
---

# Hourly 20260626 0502 Cycle 2 Tau Fixed Reference Slice Certificate

## 1. Verdict

`TauFixedReferenceSliceCertificate_2A_V0` does not admit Branch 2A.

Current repo sources do not derive an A-independent, fixed-reference graph

```text
beta = beta_0(epsilon,s)
Phi_tau(epsilon,beta,s) = beta - beta_0(epsilon,s) = 0
```

as the allowed IG variation space.

Precise decision:

```text
tau_fixed_reference_slice_admitted: false
source_fixed_gamma_present:        true, but only as a tau-plus/equivariance reference
source_to_slice_lock_present:      false
D_beta_Phi_available_from_source:  false
proper_K_beta_proved_from_source:  false
D_A_Phi_zero_proved:               false
gauge_covariance_of_theta:         true at equivariance level
gauge_covariance_of_slice:         conditional, not source-locked
target_import_used:                false
```

The strongest source fact is the fixed distinguished reference connection
`nabla_aleph` used in the tau-plus homomorphism. That is enough to define a
candidate fixed-reference Maurer-Cartan graph. It is not enough to prove that
general IG fields `(epsilon,beta)` in the action must lie on that graph.

Therefore tau-plus currently supplies equivariance and a natural candidate
subgroup/slice, not a Branch 2A variational constraint.

## 2. What was derived directly from repo sources

The following items are directly supported by the required sources and the canonical
dark-energy note checked for the strongest fixed-reference locator.

1. `IG = G semidirect Omega^1(Y,ad P)` exists for `G = Sp(64)`.

   The Sp(64) tau-plus note verifies that the inhomogeneous gauge group and tau-plus
   homomorphism are group-theoretic and survive the `(9,5)` correction. The dimension
   mismatch with the old `U(128)` story is not an obstruction.

2. Tau-plus can be written with a distinguished reference connection.

   The canonical dark-energy note fixes `nabla_aleph` and defines

   ```text
   tau^+(g) = (g, d_{nabla_aleph}(g) g^{-1}).
   ```

   The divergence-free exploration uses the same fixed-reference form. This gives a
   real source-side reference object. It is not merely a target-fitted invention.

3. Some tau-plus notation uses `d_A`.

   The Sp(64) tau-plus exploration writes the construction schematically as

   ```text
   tau^+(g) = (g, g^{-1} d_A g)
   ```

   and describes `A` as a distinguished connection. The action/IG notes also use `A`
   for the dynamical connection. This notation is not enough, by itself, to prove
   A-independence in the action-variation sense. If this `A` is the dynamical action
   variable, the graph is Branch 2B, not Branch 2A.

4. Tau-plus equivariance is supported.

   The double-coset construction supports the adjoint transformation law for theta:
   the left tau-plus factor cancels and the right factor acts by `Ad(g_b)^{-1}`.
   This is an equivariance statement for theta/double-coset geometry.

5. The conditional Branch 2A tangent theorem is already established.

   If a source-derived, gauge-covariant, A-independent `Phi` exists, then

   ```text
   K_beta = ker(D_beta Phi)
   Ad(epsilon) theta in K_beta^perp
   ```

   and `D_A Phi = 0` preserves the bare source equation. This is conditional; it
   does not supply `Phi`.

6. Free beta still collapses theta.

   With

   ```text
   theta = A - Gamma(epsilon) - Ad(epsilon^-1) beta
   ```

   free variation of beta gives

   ```text
   c_theta Ad(epsilon) theta = 0,
   theta = 0.
   ```

   So a Branch 2A claim must really restrict beta variations before the action is
   varied.

## 3. Strongest positive fixed-reference slice construction

The strongest positive construction is the following conditional fixed-reference graph:

```text
Gamma_ref := nabla_aleph or a source-fixed connection derived from carrier/section geometry

beta_0(epsilon,s) =
  epsilon^{-1} d_{Gamma_ref} epsilon
```

or the equivalent convention

```text
beta_0(epsilon,s) =
  d_{Gamma_ref}(epsilon) epsilon^{-1}.
```

The side convention must be fixed before computing signs and adjoint actions. Either
way, the candidate constraint is

```text
Phi_tau(epsilon,beta,s) = beta - beta_0(epsilon,s) = 0.
```

If this graph were source-locked as the allowed IG variation space, it would have the
right formal Branch 2A properties:

```text
D_beta Phi_tau(delta beta) = delta beta
K_beta = ker(D_beta Phi_tau) = 0
K_beta proper: yes
D_A Phi_tau = 0, if Gamma_ref is fixed under the dynamical A variation
E_beta: c_theta Ad(epsilon) theta + lambda = 0
E_A:    g_A^-2 D_A^*F_A - c_theta theta = 0
```

It would also have a clean anti-target-smuggling story because `nabla_aleph` and
tau-plus appear before Schwarzschild, Kerr, FLRW `xi_eff`, DESI, or Lambda targets
are invoked.

But this is a conditional construction, not a repo-derived Branch 2A packet. The
source files establish the tau-plus image as a subgroup/action used for equivariance.
They do not state:

```text
All admissible IG variations in the action satisfy beta = beta_0(epsilon,s).
```

The difference is decisive. A graph inside `IG` is not yet a restriction on the
field space varied by the action.

## 4. First exact obstruction or missing proof object

The first missing proof object is the source-to-slice restriction theorem:

```text
TauSourceToSliceRestrictionTheorem_2A_V1
```

It must prove, from source-side GU/tau-plus/IG geometry, that the admissible IG field
space is

```text
C_IG(s) = {
  (epsilon,beta) : beta = beta_0(epsilon,s)
}
```

rather than the full semidirect product

```text
G semidirect Omega^1(Y,ad P).
```

Minimum missing subproofs:

```text
1. Identify Gamma_ref and prove it is not the dynamical action connection A.
2. Define beta_0(epsilon,s) with a fixed left/right convention.
3. Prove admissible IG fields lie on beta = beta_0(epsilon,s).
4. Prove admissible variations are tangent to that graph.
5. Prove D_A Phi_tau = 0 in the action-variation sense.
6. Prove graph covariance under the same gauge action used in the action.
7. Compute D_epsilon beta_0 and D_s beta_0.
8. Prove no target observable selected the graph or conormal directions.
```

The first obstruction is not that `nabla_aleph` is absent. It is present. The
obstruction is that `nabla_aleph` is used to build an equivariant tau-plus action,
not to lock the beta field in the variational principle.

If the only available tau-plus graph is read with the dynamical action connection
`A`, then:

```text
Phi_tau = beta - epsilon^{-1} d_A epsilon
D_A Phi_tau != 0
```

and the connection equation becomes

```text
g_A^-2 D_A^*F_A - c_theta theta + (D_A Phi_tau)^*lambda = 0.
```

That is Branch 2B, not fixed-reference Branch 2A.

## 5. Constructive next object

Build a two-receipt source object:

```text
TauReferenceAndSliceLockReceipt_2A_V1
```

with these decision fields:

```text
reference_receipt:
  Gamma_ref_source_locator
  fixed_under_delta_A: true/false
  relation_to_action_Gamma(epsilon)
  relation_to tau-plus d_A notation

slice_lock_receipt:
  allowed_field_space_is_tau_graph: true/false
  Phi_tau
  D_beta Phi_tau
  K_beta
  D_A Phi_tau
  gauge_covariance_verifier
  anti_target_smuggling_verifier
```

This split matters because the current repo appears to have the first half in a
limited sense: a fixed `nabla_aleph` reference for tau-plus. It lacks the second
half: the proof that this reference graph is the field space.

Pass/fail outputs should be:

```text
TAU_FIXED_REFERENCE_2A_ADMITTED:
  fixed Gamma_ref plus source-locked tau graph plus D_A Phi = 0.

TAU_REFERENCE_ONLY_EQUIVARIANCE:
  fixed Gamma_ref exists, but tau-plus only supplies equivariance.

TAU_DYNAMIC_A_2B_ONLY:
  tau graph necessarily uses the dynamical connection and corrects E_A.

TAU_NO_SLICE_USE_BRANCH_3:
  no source-native slice; move to a source-forced dynamical IG current.
```

The current run returns:

```text
TAU_REFERENCE_ONLY_EQUIVARIANCE
```

with a warning that some `d_A` notation remains ambiguous and must be disambiguated
against the action variable.

## 6. Meaning for BranchFixedIGVariationSourceLock_V0

`BranchFixedIGVariationSourceLock_V0` remains blocked.

This artifact narrows the Branch 2A failure:

```text
not:  there is no fixed reference anywhere.
yes:  a fixed tau-plus reference exists.
but:  the fixed reference is not promoted into a source-locked IG variation graph.
```

Therefore `DerivedAIndependentIGConstraintPacket_2A` is still absent:

```text
source-derived Phi:        absent
D_beta Phi:                absent as source result
proper K_beta:             absent as source result
D_A Phi = 0:               absent as action-variation proof
bare source preservation:  conditional only
```

Branch 2A must not be accepted from the formal observation that
`Phi_tau = beta - beta_0` would have `D_beta Phi_tau = Id`. That computation is
useful only after the source proves that `Phi_tau = 0` is the actual branch.

## 7. Next meaningful computation/proof step

Do not compute Schwarzschild/Kerr, FLRW `xi_eff`, or DESI windows from this branch
yet. The next meaningful proof step is:

```text
Reference disambiguation:
  Compare nabla_aleph, Gamma(epsilon), and dynamical A.
  Prove which one appears in tau-plus and which one is varied in the action.

Then:
  Prove or refute that omega = (epsilon,beta) is constrained to tau^+(epsilon)
  or to a tau-plus-derived graph.
```

The first concrete calculation inside that proof is:

```text
For beta_0(epsilon,s) = epsilon^{-1} d_{Gamma_ref} epsilon,
compute D_epsilon beta_0 and D_s beta_0,
then verify covariance of Phi_tau under the action gauge group.
```

But that calculation should be labeled conditional until the source-to-slice lock is
proved.

## 8. Terrain classification and forbidden shortcut

Terrain:

```text
primary terrain:   provenance-verifier
secondary terrain: smooth-variational
guard terrain:     gauge-slice/descent
```

Reason:

| terrain | role |
|---|---|
| provenance-verifier | The branch turns on whether the tau graph is source-forced, not useful after target fitting. |
| smooth-variational | The certificate needs `D_beta Phi`, `K_beta`, and `D_A Phi` in an action variation. |
| gauge-slice/descent | The graph must be intrinsic under the tau-plus/double-coset gauge action. |

Forbidden shortcut:

```text
Do not treat tau-plus equivariance as a variational slice.
```

Also forbidden:

```text
Do not select the fixed-reference graph because it preserves D_A^*F_A = theta,
avoids theta = 0, helps exact GR, or leaves room for negative xi_eff.
```

First invariant to test:

```text
Does the source identify C_IG with the tau-plus graph, or does it keep
IG = G semidirect Omega^1(Y,ad P) as the field space?
```

Kill condition:

```text
If omega = (epsilon,beta) remains a general IG element and tau^+(G) is only a
subgroup used for the double-coset action, Branch 2A is not source-locked.
```

## 9. Claim-status consistency result

No claim status changed.

Consistency result:

```text
claim-status workflow triggered: no
claim ledgers edited: no
IG-VARIATION promoted: no
ACTION-GR promoted: no
THETA-XI promoted: no
BranchFixedIGVariationSourceLock_V0 closed: no
```

This artifact is status-consistent with the current repo:

```text
IG-VARIATION remains blocked.
ACTION-GR remains open.
THETA-XI remains open.
Branch 2A remains conditional/underdefined.
Branch 2B remains possible if tau-plus uses dynamical A.
Branch 3 remains the honest fallback if no source-locked slice exists.
```

## 10. JSON summary

```json
{
  "artifact_id": "TauFixedReferenceSliceCertificate_2A_V0",
  "run_id": "hourly-20260626-0502",
  "cycle": 2,
  "artifact_path": "explorations/hourly-20260626-0502-cycle2-tau-fixed-reference-slice-certificate.md",
  "verdict": "not_admitted_tau_plus_equivariance_only_no_source_locked_fixed_reference_graph",
  "tau_fixed_reference_slice_admitted": false,
  "source_fixed_gamma_present": true,
  "source_fixed_gamma_status": "nabla_aleph_reference_present_for_tau_plus_equivariance_not_promoted_to_variation_slice",
  "source_to_slice_lock_present": false,
  "D_beta_Phi_source_derived": false,
  "proper_K_beta_source_proved": false,
  "D_A_Phi_zero_proved": false,
  "gauge_covariance_status": "theta_equivariance_supported_slice_covariance_conditional_not_source_locked",
  "dynamic_A_reading": "branch_2b_if_tau_plus_d_uses_dynamical_action_A",
  "tau_plus_current_role": "equivariance_and_candidate_graph_not_allowed_variation_space",
  "target_import_used": false,
  "meaning_for_BranchFixedIGVariationSourceLock_V0": "blocked_branch_2a_packet_absent_despite_fixed_reference_tau_plus_locator",
  "next_frontier_object": "TauReferenceAndSliceLockReceipt_2A_V1"
}
```

## Sources read

Required sources:

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/hourly-20260626-0502-cycle1-branch2a-source-constraint-test.md`
- `explorations/constraint-first-ig-tangent-space-gate-2026-06-24.md`
- `explorations/ig-dimension-matching-sp64-tau-plus-2026-06-22.md`
- `explorations/goal-draft-ig-constraint-derivation-2026-06-24.md`
- `explorations/gu-closed-loop-action-ig-branch-2026-06-24.md`

Additional source locators checked:

- `canon/dark-energy-theta-divergence-free.md`
- `explorations/dark-energy-divergence-free-proof-2026-06-22.md`
- `tests/constraint_first_ig_tangent_gate.py`
- `tests/hourly_20260626_0502_cycle1_source_locks_audit.py`
