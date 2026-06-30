---
title: "Cycle 1 VZ Subprincipal and E-Block Proof Gate"
date: 2026-06-24
status: exploration/cycle1_gate
doc_type: vz_subprincipal_eblock_proof_gate
verdict: "NOT_FULL_EVASION__FC_VZ_1_CONDITIONAL_NOT_CLOSED__FC_VZ_4_OPEN_NOT_CLOSED"
owned_path: "explorations/cycle-gates-and-audits/cycle1-vz-subprincipal-eblock-proof-gate-2026-06-24.md"
companion_audit: "tests/cycle1_vz_subprincipal_eblock_proof_gate_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "lab/process/runbooks/five-lane-frontier-run.md"
  - "lab/roadmap/objection-triage-register.md"
  - "explorations/vz-evasion/vz-proof-grade-closure-attempt-2026-06-24.md"
  - "explorations/vz-evasion/vz-subprincipal-symbol-rs-2026-06-23.md"
  - "explorations/vz-evasion/vz-e-block-independent-rederivation-2026-06-24.md"
  - "explorations/vz-evasion/vz-principal-symbol-convention-reconciliation-2026-06-24.md"
  - "explorations/vz-evasion/vz-proof-grade-verification-gate-2026-06-24.md"
  - "tests/vz_typed_symbol_gate.py"
---

# Cycle 1 VZ Subprincipal and E-Block Proof Gate

## 1. Verdict

The current repo does **not** contain enough to claim full VZ evasion.

The strongest honest status is:

```text
principal-symbol result: valid for the typed D_roll spine with Phi_d and lambda_d != 0
FC-VZ-1: conditionally supported, not proof-grade closed
FC-VZ-4: open / reconstruction-supported, not proof-grade closed
full GU VZ causality and hyperbolicity: not closed
```

So the objection is not merely "nothing beyond principal order exists." The repo has real
lower-order work: the E-block algebra is determinant-free once the typed symbol is granted,
and the subprincipal notes give a plausible real-principal-type route. But neither gate is
closed at proof grade. The current VZ posture should remain:

```text
14D VZ: CONDITIONALLY_EVADED
4D VZ: CONDITIONALLY_RESOLVED at principal-symbol level only
full dynamical VZ: OPEN / gated
```

No downstream file should say `full VZ evasion`, `VZ verified`, or `proof-grade VZ
causality` unless **both** FC-VZ-1 and FC-VZ-4 are closed.

## 2. Principal-Symbol Result That Remains Valid

The typed-spine principal-symbol result remains a genuine positive result.

For the rolled 0/1 operator

```text
D_roll(u, psi) = (d_A^* psi, d_A u + Phi_2(d_A psi)) + Z_A(u, psi),
Phi_d := Phi_2 o d_A,
F_xi := sigma_1(Phi_d)(xi),
```

the principal block is

```text
sigma_D(xi)(u, psi) = (i_xi psi, xi tensor u + F_xi psi),
(F_xi psi)_A = xi_A gamma^B psi_B - gamma(xi) psi_A.
```

Under that hypothesis, the Schur spin-3/2 principal symbol has no non-null kernel when
`lambda_d != 0`; for the typed spine, `lambda_d = 1`. This remains valid as a typed-spine
principal-symbol computation and is exactly what `tests/vz_typed_symbol_gate.py` audits.

The important boundary is equally sharp: if the actual GU operator has only the zero-order
curvature insertion

```text
Phi_F := Phi_2(F_A tensor -)
```

and no first-order `Phi_d` term in the relevant one-form block, the present `F_xi` and
E-block are not the actual operator's principal symbol. In that branch the current
principal-symbol evasion cannot be used.

## 3. E-Block Invertibility Status and Direct-Proof Gap

**FC-VZ-1 status: conditionally supported, not proof-grade closed.**

The determinant-free E-block proof is algebraically clean once the typed symbol model is
accepted. In embedded trace notation the candidate Q-sector block is

```text
E(xi) = [[0,        (1/14) G],
         [(1/14) G, (13/98) G]],
G = gamma(xi),  G^2 = q Id,  q = g_Y(xi, xi).
```

For `q != 0`, the kernel proof is direct: the top row gives `G s = 0`, hence `s = 0`;
then the bottom row gives `G phi = 0`, hence `phi = 0`. This does not use
`det(M) = det(E) det(S_R)`.

The proof-grade gap is not the arithmetic. The gap is binding that arithmetic to the
actual GU operator and the actual Q-sector. FC-VZ-1 closes only when these E-block
invertibility conditions are all named and discharged:

```text
actual_operator_has_Phi_d: D_GU's 0/1 block contains Phi_2(d_A psi)
principal_coefficient_nonzero: lambda_d != 0 for the spin-3/2 Schur route
Q_sector_exact: Q = E_0 direct-sum Im(j) for the 14D gamma-trace split
coordinate_convention_fixed: trace-coordinate and embedded-coordinate matrices are not mixed
chirality_domains_fixed: Gamma, j, G, Phi_d have typed S^+ <-> S^- domains
non_null_cone_only: q = g_Y(xi,xi) != 0 and G^2 = q Id in the same convention
null_locus_exact: E can fail only on q = 0, not at mixed non-null covectors
determinant_free: the Schur proof is downstream of E-invertibility, not a proof of it
```

The repo has strong conditional evidence for this list, especially in the 2026-06-24
E-block rederivation and proof-grade closure attempt. It still lacks the source-closed
operator certificate that makes the displayed `E(xi)` the actual `P_Q sigma_D(xi) P_Q`.

## 4. Subprincipal/Extrinsic-Curvature Characteristic Status

**FC-VZ-4 status: open / reconstruction-supported, not proof-grade closed.**

The existing subprincipal files make a plausible case that lower-order terms do not create
new characteristics once the principal operator is of real principal type. They also argue
that spin connection, Shiab curvature, and section second fundamental form terms enter as
zero-order contributions and therefore affect WKB amplitude rather than characteristic
directions.

That is not yet the same thing as closing FC-VZ-4. The missing proof object is an explicit
4D section-pulled Schur subprincipal computation:

```text
sigma_0^inv(S_{R_s}^{4D,full})(x, eta)
```

with every term traced from the actual operator, including:

```text
A_s^(0), B_s^(0), C_s^(0), E_s^(0)
the E_s^(1)^(-1) Schur corrections
Poisson-bracket / invariant-subprincipal corrections
II_s^H = s*(theta) and normal-index mixing
Sp(64) curvature and Phi_F terms
curved-gauge horizontal/normal frame splitting
mass and other Z_A ledger terms
```

The current files give the correct shape of the argument, but the 4D proof-grade gate is
still live because no artifact yet computes that full object and proves that no `II_s`
or curved-section term contributes an effective first-order spacelike characteristic.

## 5. First Exact Obstruction or Missing Proof Object

The first obstruction in dependency order is the **actual-operator certificate**:

```text
VZ-OPERATOR certificate:
  D_GU's rolled 0/1 principal block is D_roll with Phi_d := Phi_2 o d_A,
  with typed chiral domains, Q-sector splitting, lambda_d, and Z_A lower-order ledger fixed.
```

Without that certificate, FC-VZ-1 is only a theorem about the typed D_roll model, not the
actual GU operator. Closing it would upgrade the 14D principal-symbol leg, but it would
not close full VZ: FC-VZ-4 would still require the section-pulled subprincipal/extrinsic
curvature certificate above.

The first direct kill conditions are correspondingly simple:

```text
FC-VZ-1 kill:
  find non-null xi with ker E(xi) != 0 for the actual Q-sector, or prove that the
  actual operator lacks the Phi_d principal block used to build E(xi).

FC-VZ-4 kill:
  compute the actual 4D section-pulled operator and find a non-null eta with
  ker sigma_1(S_{R_s}^{4D,full})(eta) != 0 after II_s / subprincipal reduction,
  or show that II_s sources an effective first-order spacelike characteristic.
```

## 6. What This Means for GU Causality/Hyperbolicity

The VZ objection has not defeated GU in the current repo. The typed principal-symbol
mechanism is coherent, nontrivial, and still the right place to push.

But the repo also cannot yet cite a theorem-grade causal/hyperbolic GU spin-3/2 system.
At present the safe claim is:

```text
GU has a conditional principal-symbol VZ evasion mechanism.
The mechanism is supported by conditional E-block algebra and reconstruction-grade
subprincipal reasoning.
It is not yet a full hyperbolicity theorem for the physical 4D effective RS dynamics.
```

For GU causality this is a live, high-value frontier gate rather than a closed win or a
falsification.

## 7. Next Meaningful Computation

The next computation should be a proof certificate, not another determinant check.

1. Write the canonical typed `D_GU` 0/1 operator certificate. It must distinguish
   `Phi_2`, `Phi_d := Phi_2 o d_A`, and `Phi_F := Phi_2(F_A tensor -)`, fix chirality and
   Q-sector coordinates, and emit `E(xi) = P_Q sigma_D(xi) P_Q`.
2. Attach a symbolic audit over the Clifford quotient `G^2 = q` proving the two-sided
   E-block inverse/kernel statement for arbitrary non-null `xi`.
3. Then compute `sigma_0^inv(S_{R_s}^{4D,full})` with `II_s^H`, `Z_A`, and curved-frame
   terms. The pass condition is not "sigma_0 has no real eigenvalues"; the pass condition is
   "no effective first-order spacelike characteristic and real principal type survives."

This is the shortest path to deciding whether OBJ-VZ is a real evasion or an order-by-order
optimism artifact.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "cycle1-vz-subprincipal-eblock-proof-gate-2026-06-24",
  "verdict": "NOT_FULL_EVASION__GATES_NOT_CLOSED",
  "full_vz_evasion_claim": false,
  "full_vz_evasion_allowed_only_if": [
    "FC-VZ-1.status == closed",
    "FC-VZ-4.status == closed"
  ],
  "principal_symbol_status": {
    "separated_from_subprincipal": true,
    "status": "valid_conditional_principal_symbol",
    "scope": "typed_D_roll_with_Phi_d_and_lambda_d_nonzero",
    "rollback": "actual_D_GU_lacks_Phi_d_or_lambda_d_zero_for_spin_three_halves_Schur_route"
  },
  "subprincipal_status": {
    "separated_from_principal": true,
    "status": "reconstruction_supported_not_closed",
    "scope": "section_pulled_4D_effective_RS_operator",
    "missing_proof_object": "explicit_sigma_0_inv_S_Rs_4D_full_with_II_s_H_Z_A_and_Poisson_terms"
  },
  "gates": {
    "FC-VZ-1": {
      "name": "E-block invertibility on non-null 14D cone",
      "status": "conditional_not_closed",
      "proof_grade": "conditional_reconstruction",
      "conditions_named": [
        "actual_operator_has_Phi_d",
        "principal_coefficient_lambda_d_nonzero_for_Schur_route",
        "Q_sector_exact_E0_plus_Im_j",
        "coordinate_convention_fixed",
        "chirality_domains_fixed",
        "non_null_q_and_G_squared_equals_q_Id",
        "null_locus_exact",
        "determinant_free_kernel_or_inverse_proof"
      ],
      "missing_proof_object": "source_closed_operator_to_E_block_certificate_for_actual_D_GU",
      "kill_conditions": [
        "non_null_xi_with_kernel_E_xi_for_actual_Q_sector",
        "actual_operator_invalidates_F_xi_principal_block",
        "Q_sector_has_extra_component_creating_non_null_kernel"
      ]
    },
    "FC-VZ-4": {
      "name": "subprincipal/extrinsic-curvature spacelike-characteristic gate",
      "status": "open_not_closed",
      "proof_grade": "reconstruction_support_only",
      "conditions_named": [
        "actual_4D_section_pulled_operator_fixed",
        "II_s_H_enters_only_zero_order",
        "curved_frame_horizontal_normal_splitting_verified",
        "real_principal_type_survives",
        "no_effective_first_order_spacelike_characteristic"
      ],
      "missing_proof_object": "explicit_section_pulled_subprincipal_Schur_symbol_with_II_s_H_and_Z_A_ledger",
      "kill_conditions": [
        "II_s_sources_effective_first_order_spacelike_characteristics",
        "curved_section_symbol_has_non_null_kernel",
        "constraint_propagation_generates_VZ_style_spacelike_secondary_characteristics"
      ]
    }
  },
  "rollback_conditions": [
    "actual_operator_lacks_Phi_d",
    "lambda_d_zero_for_spin_three_halves_Schur_route",
    "non_null_E_block_kernel_found",
    "Q_sector_not_E0_plus_Im_j",
    "II_s_sources_effective_first_order_spacelike_characteristics",
    "curved_section_symbol_not_real_principal_type",
    "standalone_RS_Lagrangian_with_VZ_characteristics_found"
  ],
  "next_meaningful_computation": [
    "canonical_typed_D_GU_0_1_operator_certificate",
    "symbolic_E_block_inverse_or_kernel_audit_for_actual_Q_sector",
    "explicit_sigma_0_inv_S_Rs_4D_full_with_II_s_H_Z_A_and_curved_frame_terms"
  ]
}
```
