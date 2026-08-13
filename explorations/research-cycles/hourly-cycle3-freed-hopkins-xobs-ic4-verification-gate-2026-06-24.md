---
title: "Cycle 3 Freed-Hopkins X_obs / IC4 Verification Dependency Gate"
date: 2026-06-24
problem_label: "hourly-cycle3-freed-hopkins-xobs-ic4-verification-gate"
status: exploration
verdict: PARK_CONDITIONALLY_RESOLVED_NOT_CLOSED
---

# Cycle 3 Freed-Hopkins X_obs / IC4 Verification Dependency Gate

## 1. Verdict

**Verdict: PARK_CONDITIONALLY_RESOLVED_NOT_CLOSED.**

The Freed-Hopkins Option B survivor is not verified as a closed no-go. It is
lane-narrowed and conditionally resolved:

- `X_obs^sol = M_RF(K3)` is a conditional identification, not a verified theorem.
- The `KSp^0 = KO^4` family over the arithmetic/orbifold base is conditional on RC4.
- The gravitational-background relabeling argument is valid only after both of those
  inputs are supplied.
- There is **no GENUINE_OBSTRUCTION promotion** in this gate.

The current strongest honest state is:

```text
Met(X^4) fails by contractibility.
Omega^2 BSp(64) fails by ordinary Sp(64)-gauge-background relabeling.
X_obs^sol conditionally fails by gravitational-background relabeling if
  IC4 C/D/F, IC4 F3/F5, and RC4 are verified.
Until then: park as lane-narrowed CONDITIONALLY_RESOLVED.
```

This gate therefore blocks promotion from lane-narrowed `CONDITIONALLY_RESOLVED` to a
closed no-go until the named proof objects below exist on tracked, independently checked
files. It also names the exact reopen conditions.

## 2. Dependency chain and same-session circularity guard

The closure chain has this dependency order:

| step | claim | current state | gate effect |
|---|---|---|---|
| FH-root | Bordism-invariant observer data either descends or relabels as ordinary background/tangential data; Option B is the only formal escape. | `OPEN` in `freed-hopkins-nonforgettable-observer-2026-06-23.md`. | Cannot support a closed no-go by itself. |
| OptionB-A | Full metric section space `Met(X^4)` is contractible. | Established for the naive full section-space candidate. | Eliminates the naive candidate. |
| OptionB-B | `Omega^2 BSp(64)` is noncontractible but is ordinary Sp(64) gauge-background data. | Conditional/reconstruction but structurally stable. | Eliminates the gauge-moduli candidate by relabeling. |
| IC4-B/F5 | The solution lies in the K3 topological class. | Conditional; depends on index split, RS `+8`, additivity, Rokhlin, and the `ch_2` correction. | Required before `M_RF(K3)` is even the right target. |
| IC4-C | The GU section field equation reduces to the Einstein equation. | Conditional reconstruction grade; component/CAS and geometric residuals remain. | Required before solution sections become Einstein metrics. |
| IC4-D/F3 | The selected K3 section is source-free in the trace-free equation. | Conditional; surviving YM, mixed, spinor, hidden-curvature, or non-LC source terms remain open. | Required before Einstein-with-matter is excluded. |
| IC4-F | Ricci-flat K3/Yau metric selection is available at the needed moduli level. | Conditional; Yau data and continuation conventions are not fully fixed. | Required for the `M_RF(K3)` gravitational-background identification. |
| XOBS | `X_obs^sol = M_RF(K3)` and `M_RF(K3) = O(3,19;Z)\D` is noncontractible. | Conditional on IC4-B/C/D/F and F3/F5. | Supplies noncontractibility but not non-background status. |
| RC4 | `KSp^0 = KO^4` and the Fredholm-family classification apply over the arithmetic/orbifold base. | Open/conditional; finite-CW or compact-Hausdorff arguments do not automatically cover `Gamma\D`. | Required before the K-theory class and relabeling are well typed. |
| Relabel | The family index over `M_RF(K3)` is ordinary gravitational/tangential background data. | Conditional on XOBS plus RC4. | Would close Option B only if all upstream gates are verified. |

**Same-session guard.** The load-bearing FH/IC4/XOBS files were authored in the same
2026-06-23 session and several were explicitly downgraded for same-session verdict
inflation. Separation into different files does not count as independent verification.
A future promotion requires later-session or independently checked proof objects for
IC4 C/D/F, F3/F5, RC4, and the FH-root theorem. Until that happens, any attempted
`GENUINE_OBSTRUCTION` upgrade is a rollback event.

## 3. What current FH/IC4 sources establish

The current sources establish a real narrowing, not a closed obstruction.

`freed-hopkins-nonforgettable-observer-2026-06-23.md` establishes the structural pressure:
eta-invariant, pin data, and Maslov data either depend on ordinary background/tangential
structure or fail as bordism-invariant observer data. It leaves Option B open.

`freed-hopkins-optionb-ksp-family-2026-06-23.md` eliminates two concrete Option B
candidates. The full section space `Met(X^4)` is contractible, so it carries no reduced
`KSp^0` obstruction. The gauge-moduli candidate is noncontractible, but it relabels as an
ordinary Sp(64) gauge background. The only survivor is the true solution-section moduli
`X_obs^sol`.

`ic4-ricci-flat-k3-selection-2026-06-23.md` gives the conditional route by which
`X_obs^sol` could become the K3 Ricci-flat metric moduli:

```text
K3 topology fixed
+ IC4 reduces GU section equation to source-free Einstein
+ Hitchin-Thorpe on K3
+ Yau-Calabi at fixed complex/Kahler data
= Ricci-flat K3 moduli family
```

But IC4 itself records the open gates: Gate C is only a conditional Einstein-equation
reduction; Gate D is only a conditional vacuum/source-free gate; Gate F is conditional
at the Yau-data/moduli-selection level; F3 leaves trace-free GU sources open; F5 leaves
the K3 topology-forcing chain open.

`freed-hopkins-xobs-sol-k3-moduli-2026-06-23.md` then computes the strongest conditional
case. If `X_obs^sol = M_RF(K3)`, global Torelli identifies the unit-volume moduli with an
arithmetic quotient of the period domain:

```text
D = O(3,19)/(O(3) x O(19))
M_RF(K3) ~= O(3,19;Z)\D
```

The domain `D` is contractible, while the quotient is an aspherical arithmetic orbifold,
so the moduli is noncontractible. That is a positive result for Option B's first test.
It is also exactly why the relabeling argument fires conditionally: the noncontractible
parameter is just the gravitational background metric moduli.

`canon/no-go-class-relative-map.md` and `roadmap/objection-triage-register.md` both
record the same status: FH Option B is lane-narrowed and `CONDITIONALLY_RESOLVED`, not a
closed `GENUINE_OBSTRUCTION`.

## 4. Strongest positive verification attempt

Assume, for the sake of the strongest positive attempt, all of the following:

1. IC4-F5 verifies that the relevant compact solution topology is K3-type.
2. IC4-C verifies the component-level reduction from the GU section equation to the
   Einstein equation.
3. IC4-D/F3 verifies that the selected K3 section has no trace-free GU source.
4. IC4-F verifies the Ricci-flat K3/Yau moduli interpretation at the level needed for
   `M_RF(K3)`.
5. RC4 verifies `KSp^0 = KO^4` or supplies the correct equivariant/orbifold replacement
   over `O(3,19;Z)\D`.
6. The FH-root no-go lemma is upgraded from `OPEN` to a theorem covering the current GU
   observer data.

Under those assumptions the closure proof is short:

```text
X_obs^sol = M_RF(K3).
M_RF(K3) is noncontractible by global Torelli and the arithmetic quotient.
The noncontractibility is the noncontractibility of gravitational metric backgrounds.
The index family over it is the ordinary gravitational/tangential-background family.
Therefore the `KSp^0` class is in the image of a background-extension functor.
Therefore Option B does not supply non-forgettable observer anomaly data.
```

This is the strongest positive verification attempt available from the current sources.
It is coherent, and it is worth preserving as the promotion target. It is not yet a
verified no-go because the assumptions are exactly the open gates.

## 5. First exact obstruction or missing proof object

The first exact obstruction is the missing verified IC4 Einstein-vacuum reduction on the
K3 topological class. More precisely, the first missing proof object is:

**IC4-C/D/F3 verification certificate.** A component-level and geometrically invariant
certificate proving all of the following on the selected K3-type LC section:

```text
[G^Y_T]^TF = T^{YM,TF} + T^{mix,TF}
C_Gauss = 1
T^{GU,TF}_{mu nu} = 0
```

and proving that IC3 torsion corrections, the `(6,4)` normal-bundle Weitzenboeck sign,
`O(theta^3)` distortion terms, IC2 negative-mode/gauge issues, spinor stress, YM stress,
mixed-flux stress, and hidden-curvature trace-free terms do not leave a residual source.

Without this proof object, IC4 may select Einstein-with-matter, a proper GU sublocus, or
a different field-equation moduli. In any of those cases the statement
`X_obs^sol = M_RF(K3)` is not established.

The next missing proof objects are also load-bearing:

- **IC4-F5 K3 topology certificate:** derive the K3 topological class without importing
  the target generation count. This must close the index split, RS `+8`, index
  additivity, Rokhlin assumptions, and `ch_2(S(6,4))` correction gate.
- **IC4-F moduli-level Yau certificate:** show that the Ricci-flat K3 output is the
  correct solution moduli for this gate, and state separately whether GU fixes a single
  complex structure/Kahler class or only the full hyperkahler moduli family.
- **RC4 orbifold K-theory certificate:** define the correct base category for
  `Gamma\D` and prove the H-linear Fredholm-family class is represented in `KSp^0`,
  `KO^4`, or the appropriate equivariant/orbifold replacement.
- **FH-root theorem certificate:** close the currently open structural lemma for the
  present GU observer data, so that background relabeling plus contractibility exhausts
  the current Option B candidates.

## 6. Reopen/promote/park decision

**Park now.** The lane stays `CONDITIONALLY_RESOLVED / lane-narrowed`. It is useful and
decision-grade, but not closed.

**Promote later only if all of these are supplied:**

1. IC4-C verified: GU section equation reduces to Einstein at component level with the
   named residuals discharged.
2. IC4-D/F3 verified: no trace-free GU source survives on the selected K3 section.
3. IC4-F5 verified: K3 topology is forced by the GU chain, not fitted.
4. IC4-F verified at the moduli level needed for `X_obs^sol = M_RF(K3)`.
5. RC4 verified: the KSp/KO family classification is valid over the arithmetic/orbifold
   base, or an equivariant/orbifold replacement gives the same relabeling result.
6. The FH-root no-go lemma is upgraded from `OPEN` to a theorem covering current GU
   observer data.
7. The promotion is made in a later independently checked session, not by same-session
   circular chaining.

If those objects are present, the artifact can be promoted from lane-narrowed
`CONDITIONALLY_RESOLVED` to a closed no-go for the current Freed-Hopkins Option B
observer-pairing route.

**Reopen if any one of these happens:**

1. IC4-C fails, so the solution equation is not Einstein.
2. IC4-D/F3 fails, so the solution locus is Einstein-with-matter or otherwise sourced.
3. IC4-F5 fails, so the relevant solution topology is not forced to be K3.
4. IC4-F fails in a way that changes the solution moduli from `M_RF(K3)`.
5. RC4 fails, so the `KSp^0 = KO^4` class over the arithmetic/orbifold base is not
   well typed or does not descend as claimed.
6. The GU solution locus is a proper sublocus of `M_RF(K3)` carrying a non-extendable
   `KO^4` class not inherited from gravitational backgrounds.
7. A non-gauge, non-metric Sp(64) or H-linear observer structure is constructed with a
   noncontractible moduli and a `KSp^0` class outside ordinary background-extension
   images.
8. A same-session or conditional source attempts to promote the lane to
   `GENUINE_OBSTRUCTION`; that promotion must be rolled back.

## 7. Rollback/falsification conditions

Rollback this gate's park verdict only under one of two kinds of evidence.

**Promotion evidence:** all promotion proof objects in Section 6 exist and pass later
independent review. Then the conditional relabeling argument becomes a closed no-go for
the current Option B route.

**Reopening evidence:** any reopen condition in Section 6 is met. The most important
falsifiers are concrete:

- a surviving trace-free GU source (`F3`);
- failure of the K3 topology-forcing chain (`F5`);
- failure of the `KSp^0 = KO^4` lift over the arithmetic/orbifold base (`RC4`);
- a proper non-background GU solution submoduli with a non-extendable `KO^4` class;
- an independent observer Sp(64)/H structure not reducible to gauge or metric
  background.

The following are not sufficient for promotion: compatibility with `M_RF(K3)`, reuse of
same-session conditional files, the noncontractibility of `M_RF(K3)` alone, or the fact
that the relabeling argument is structurally plausible.

## 8. Machine-readable JSON summary

```json
{
  "artifact": "HOURLY_CYCLE3_FREED_HOPKINS_XOBS_IC4_VERIFICATION_GATE",
  "date": "2026-06-24",
  "verdict": "PARK_CONDITIONALLY_RESOLVED_NOT_CLOSED",
  "closed_no_go_promoted": false,
  "genuine_obstruction_promotion": false,
  "no_GENUINE_OBSTRUCTION_promotion": true,
  "same_session_guard_required": true,
  "same_session_guard": "same-session load-bearing FH/IC4/XOBS files from 2026-06-23 cannot close each other without later independent verification",
  "status_by_claim": {
    "X_obs_sol_equals_M_RF_K3": "conditional_on_IC4_C_D_F_and_F3_F5",
    "KSp0_over_arithmetic_orbifold_base": "conditional_on_RC4",
    "gravitational_background_relabeling": "conditional_on_XOBS_identification_and_RC4",
    "Option_B_closed_no_go": "not_currently_verified"
  },
  "required_dependencies": [
    "IC4_C",
    "IC4_D",
    "IC4_F",
    "IC4_F3",
    "IC4_F5",
    "RC4",
    "FH_root_no_go_theorem",
    "same_session_guard"
  ],
  "dependency_chain": [
    {
      "id": "FH_root",
      "claim": "bordism-invariant observer data descend or relabel; Option B is sole escape",
      "current_status": "OPEN",
      "needed_for_promotion": true
    },
    {
      "id": "IC4_C",
      "claim": "GU section equation reduces to Einstein equation",
      "current_status": "CONDITIONAL_PASS_RECONSTRUCTION_GRADE",
      "needed_for_promotion": true
    },
    {
      "id": "IC4_D_F3",
      "claim": "selected K3 section is source-free with no trace-free GU source",
      "current_status": "CONDITIONAL_PASS_WITH_F3_OPEN",
      "needed_for_promotion": true
    },
    {
      "id": "IC4_F5",
      "claim": "K3 topology is actually forced",
      "current_status": "CONDITIONAL_PASS_WITH_F5_OPEN",
      "needed_for_promotion": true
    },
    {
      "id": "IC4_F",
      "claim": "Ricci-flat K3/Yau moduli interpretation is valid for X_obs_sol",
      "current_status": "CONDITIONAL_PASS",
      "needed_for_promotion": true
    },
    {
      "id": "RC4",
      "claim": "KSp0 equals KO4 or correct equivariant/orbifold replacement over Gamma\\D",
      "current_status": "OPEN_CONDITIONAL",
      "needed_for_promotion": true
    }
  ],
  "current_sources_establish": [
    "Met(X4)_candidate_contractible",
    "Omega2_BSp64_candidate_gauge_background_relabels",
    "X_obs_sol_noncontractible_if_equal_to_M_RF_K3",
    "gravitational_relabeling_if_X_obs_sol_equals_M_RF_K3_and_RC4_holds",
    "lane_narrowed_not_closed"
  ],
  "first_missing_proof_object": "IC4_C_D_F3_VERIFICATION_CERTIFICATE",
  "required_promotion_proof_objects": [
    "IC4_C_component_Einstein_reduction_certificate",
    "IC4_D_F3_no_trace_free_GU_source_certificate",
    "IC4_F5_K3_topology_forcing_certificate",
    "IC4_F_moduli_level_Ricci_flat_K3_Yau_certificate",
    "RC4_KSp0_KO4_arithmetic_orbifold_or_equivariant_certificate",
    "FH_root_no_go_theorem_for_current_GU_observer_data",
    "later_session_independent_verification_record"
  ],
  "park_decision": "park_as_lane_narrowed_conditionally_resolved",
  "promote_decision_if_dependencies_close": "promote_to_closed_no_go_for_current_Option_B_route",
  "reopen_conditions": [
    "IC4_C_fails",
    "IC4_D_or_F3_fails_with_surviving_trace_free_source",
    "IC4_F5_fails_K3_topology_not_forced",
    "IC4_F_changes_solution_moduli_from_M_RF_K3",
    "RC4_fails_or_requires_nonrelabeling_equivariant_KSp_class",
    "proper_GU_solution_sublocus_has_nonextendable_KO4_class",
    "independent_non_gauge_non_metric_Sp64_or_H_observer_structure_constructed",
    "same_session_conditional_promotion_to_GENUINE_OBSTRUCTION_attempted"
  ],
  "rollback_conditions": [
    "promotion_without_IC4_C_D_F_F3_F5_RC4",
    "promotion_without_FH_root_theorem",
    "promotion_from_same_session_conditional_chain",
    "claiming_noncontractibility_alone_closes_Option_B",
    "claiming_gravitational_relabeling_without_X_obs_sol_equals_M_RF_K3"
  ]
}
```
