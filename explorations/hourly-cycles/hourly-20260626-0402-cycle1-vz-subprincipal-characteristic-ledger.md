---
title: "Hourly 20260626 0402 Cycle 1 VZ Subprincipal Characteristic Ledger"
date: "2026-06-26"
run_id: "hourly-20260626-0402"
cycle: 1
lane: "VZSubprincipalCharacteristicLedger"
doc_type: "frontier_ledger"
artifact_id: "VZSubprincipalCharacteristicLedger_V0"
verdict: "blocked_principal_symbol_not_full_vz_closure"
owned_path: "explorations/hourly-20260626-0402-cycle1-vz-subprincipal-characteristic-ledger.md"
---

# Hourly 20260626 0402 Cycle 1 VZ Subprincipal Characteristic Ledger

## 1. Verdict

Verdict: **blocked / conditional, not full VZ closure**.

The typed-spine principal-symbol result remains a real positive construction:
if the actual 14D GU 0/1 operator has the typed principal block

```text
sigma_1(D_roll)(xi)(u, psi) = (i_xi psi, xi tensor u + F_xi psi)
F_xi = sigma_1(Phi_2 o d_A)(xi)
```

with nonzero `lambda_d`, then the typed spin-3/2 Schur principal symbol has no
non-null kernel. The formal typed E-block arithmetic is also tested in the
Clifford quotient `G^2 = q`.

That does **not** close VZ for GU. Two proof objects are still missing before
full VZ closure can be claimed:

```text
FC-VZ-1 data:
  E_actual^epsilon(y, xi)
    = P_Q,out^epsilon sigma_1(D_GU^epsilon)(y, xi) I_Q,in^epsilon
  extracted from the actual GU operator and proved invertible for every real
  non-null mixed 14D covector.

FC-VZ-4 data:
  sigma_0^inv(S_Rs_4D_full)(x, eta)
  and the coupled RS/gamma-trace characteristic matrix after section pullback,
  including II_s^H = s*(theta), curved horizontal/normal frame terms, Z_A,
  Poisson/invariant-subprincipal corrections, and constraint-source terms.
```

Current status remains:

```text
14D VZ: CONDITIONALLY_EVADED, gated on actual-operator E-block invertibility.
4D VZ: CONDITIONALLY_RESOLVED at principal-symbol level only.
Full dynamical VZ: OPEN / gated.
```

No claim ledger should be promoted or demoted from this lane.

## 2. Sources Read First

Required coordination and terrain sources:

| source | use |
|---|---|
| `RESEARCH-POSTURE.md` | Kept Mission A constructive but blocked verdicts honest. |
| `process/runbooks/five-lane-frontier-run.md` | Used the frontier-lane verdict vocabulary and no-overclaim contract. |
| `explorations/remaining-math-topography-ledger-v0-2026-06-26.md` | Confirmed VZ terrain as microlocal-subprincipal and named the forbidden shortcut. |

VZ and typed-spine sources:

| source | use |
|---|---|
| `canon/no-go-class-relative-map.md` targeted VZ excerpts | Current VZ status and FC-VZ-1 / FC-VZ-4 caps. |
| `roadmap/objection-triage-register.md` targeted VZ row | OBJ-VZ decisive tests and kill conditions. |
| `RESEARCH-STATUS.md` targeted VZ correction excerpts | VZ-01 and VZ-02 correction posture. |
| `DERIVATION-PROGRESS.md` targeted VZ correction excerpts | Same-claim warning that `ker S_R` and E-invertibility are not independent evidence. |
| `explorations/gu-typed-operator-action-spine-2026-06-24.md` | Typed `D_roll`, `Phi_2` / `Phi_d` / `Phi_F` separation, and `Z_A` lower-order ledger. |
| `explorations/vz-principal-symbol-convention-reconciliation-2026-06-24.md` | The convention under which `F_xi` is first order. |
| `explorations/vz-proof-grade-closure-attempt-2026-06-24.md` | Strongest typed-spine principal-symbol proof. |
| `explorations/vz-e-block-independent-rederivation-2026-06-24.md` | Determinant-free E-block coefficient and kernel proof, conditional on the typed symbol. |
| `explorations/vz-proof-grade-verification-gate-2026-06-24.md` | Same-session and proof-grade cap on FC-VZ-1. |
| `explorations/cycle1-vz-subprincipal-eblock-proof-gate-2026-06-24.md` | Prior separation of principal, E-block, and subprincipal gates. |
| `explorations/cycle2-vz-actual-operator-e-block-certificate-2026-06-24.md` | Definition of `E_actual` and exact actual-operator data missing. |
| `explorations/hourly-cycle1-vz-subprincipal-characteristic-contract-2026-06-24.md` | Prior FC-VZ-4 contract and missing actual subprincipal object. |
| `explorations/vz-subprincipal-symbol-rs-2026-06-23.md` | Reconstruction-grade subprincipal attempt and its limits under later caps. |
| `explorations/vz-14d-mixed-covectors-2026-06-23.md` | Mixed-covector conditional verdict and E-invertibility circularity correction. |
| `explorations/vz-oq2-lower-order-curvature-2026-06-23.md` | Lower-order curvature argument and why it is not enough for section-pulled FC-VZ-4. |
| `tests/vz_typed_symbol_gate.py` | Formal typed algebra audit for coefficients and inverses. |
| `explorations/hourly-20260626-0103-cycle3-dgu-symbol-vz-transition-closeout.md` | Current DGU source-row blocker before symbol/VZ replay. |
| `explorations/hourly-20260626-0202-cycle3-dgu-symbol-vz-closeout.md` | Current no-restart posture before primary source row. |
| `explorations/hourly-20260625-0301-cycle1-manuscript-dgu-vz-operator-receipt-candidates.md` | Manuscript source search: zero accepted DGU/VZ operator receipts. |
| `explorations/hourly-20260625-0502-cycle2-author-manuscript-dgu-vz-action-receipt-gate.md` | Positive bosonic action locator quarantined, no accepted DGU/VZ 0/1 receipt. |

## 3. Specific GU Claim/Bridge Under Test

The bridge under test is:

```text
typed D_roll principal-symbol theorem
  -> actual D_GU^epsilon 0/1 symbol certificate
  -> actual E-block invertibility for all non-null mixed 14D covectors
  -> actual 14D spin-3/2 Schur principal symbol
  -> section-pulled 4D full Schur operator
  -> no spacelike characteristics after II_s / subprincipal / constraint terms.
```

The current repo closes only the first step inside the typed-spine model. It
does not supply the actual `D_GU^epsilon` source row, the actual `E_actual`
projection, or the section-pulled invariant subprincipal characteristic matrix.

Therefore the claim under test is not "is the typed principal symbol coherent?"
It is:

```text
Does the current typed-spine principal-symbol result already provide enough
data to claim full VZ causality for GU?
```

Answer: no.

## 4. Terrain Classification And Forbidden Shortcut

Primary terrain: **microlocal-subprincipal**.

There is a provenance prerequisite because the actual operator/source row is
still missing, but the mathematical wall itself is microlocal: characteristic
sets, Schur symbols, invariant subprincipal symbols, mixed covectors, and
section-pulled constraint characteristics.

Forbidden shortcut:

```text
Treating typed principal-symbol closure, or formal E-block algebra for a
supplied matrix, as full VZ closure for the actual GU operator.
```

Two secondary shortcuts are also forbidden:

```text
1. Treating "lower-order terms do not change the principal symbol" as a proof
   that section-pulled II_s / constraint propagation cannot create an effective
   first-order spacelike characteristic.

2. Using VZ success to choose the actual operator, its `Phi_d` coefficient,
   Q-sector, or coordinate normalization.
```

First invariant to test:

```text
For E-block:
  ker E_actual^epsilon(y, xi) = 0 for all real xi with
  q = g_Y^{-1}(xi, xi) != 0, including mixed horizontal/vertical covectors.

For FC-VZ-4:
  ker Char_RS_constraint_actual(x, eta; II_s^H, Z_A, K_mu_nu) = 0 for all
  real eta with g_s^{-1}(eta, eta) != 0.
```

Kill condition:

```text
A non-null E_actual kernel, or a spacelike characteristic of the actual
section-pulled coupled RS/constraint system after II_s^H and lower-order
terms are included.
```

## 5. Strongest Positive Construction Attempt

The best positive construction starts from the typed spine:

```text
D_roll^epsilon(u, psi)
  = (d_A^* psi, d_A u + lambda_d Phi_2(d_A psi)) + Z_A^epsilon(u, psi)
```

with:

```text
Phi_2                      zero-order algebraic shiab
Phi_d := Phi_2 o d_A       first-order differential composite
Phi_F := Phi_2(F_A tensor -) zero-order curvature insertion
F_xi := sigma_1(Phi_d)(xi)
Z_A                        lower-order ledger
```

For the supplied typed block, the Q-sector coefficients are coherent:

```text
E_coord = [[0,        (1/14) G],
           [G,        (13/7) G]]

E_embed = [[0,        (1/14) G],
           [(1/14) G, (13/98) G]]

G = gamma(xi), q = g_Y^{-1}(xi, xi), G^2 = q Id.
```

The determinant-free kernel proof is strong:

```text
q != 0 and E(phi, s) = 0
  -> G s = 0
  -> s = 0
  -> G phi = 0
  -> phi = 0.
```

With `lambda_d != 0`, the typed spin-3/2 Schur principal symbol has no non-null
kernel. This is the strongest available positive VZ construction.

The best continuation is to compute the full section-pulled Schur operator:

```text
S_Rs_4D_full
  = A_s_full - B_s_full (E_s_full)^(-1) C_s_full
```

and then compute its invariant subprincipal characteristic data. If all lower
and constraint terms remain transport/amplitude/source terms rather than
effective first-order characteristic terms, then the VZ route becomes much
stronger.

This positive construction remains conditional because the displayed typed
block has not been extracted from the actual source-closed `D_GU^epsilon`.

## 6. First Exact Obstruction Or Missing Proof Object

The earliest dependency is:

```text
source-closed actual D_GU^epsilon 0/1-sector operator certificate
```

Without it, neither `E_actual` nor `S_Rs_4D_full` is an actual-GU object.

The VZ-specific missing packet has two required proof objects.

### A. Direct Actual E-Block Invertibility Data

Missing object:

```text
E_actual^epsilon(y, xi)
  = P_Q,out^epsilon sigma_1(D_GU^epsilon)(y, xi) I_Q,in^epsilon
```

Required data:

```text
1. Actual sigma_1(D_GU^epsilon) on the 0/1 sector.
2. Coefficients:
   a = coefficient of i_xi psi,
   b = coefficient of xi tensor u,
   lambda_d = coefficient of Phi_2(d_A psi).
3. Order separation:
   Phi_2, Phi_d, Phi_F, and F_xi are distinct.
4. Exact Q sectors:
   Q_in^epsilon = S^epsilon plus Im(j_epsilon),
   Q_out^epsilon = S^{-epsilon} plus Im(j_{-epsilon}).
5. Chiral domains, Gamma, j, P_Q,out, I_Q,in, and trace normalization.
6. Signature and Clifford convention:
   signature(g_Y) = (9,5), G^2 = q Id.
7. One coordinate convention:
   trace coordinates or embedded coordinates, not mixed.
8. Extra first-order Q-block terms proved absent or included in a new kernel proof.
9. Quantification over all real mixed horizontal/vertical covectors, not samples.
10. A direct kernel or two-sided inverse proof, downstream of the actual extraction,
    not determinant circularity.
```

Important distinction:

```text
a*b != 0 is enough for the minimal two-row E-kernel argument once the actual
Q-block matches the certificate. lambda_d != 0 is additionally required for the
current spin-3/2 Schur principal-symbol VZ route.
```

### B. Section-Pulled Subprincipal / Extrinsic Characteristic Data

Missing object:

```text
sigma_0^inv(S_Rs_4D_full)(x, eta)
```

from the same actual `D_GU^epsilon`, with:

```text
S_Rs_4D_full
  = A_s_full - B_s_full (E_s_full)^(-1) C_s_full.
```

Required terms:

```text
A_s^(0), B_s^(0), C_s^(0), E_s^(0)
E_s^(1)^(-1) Schur corrections
Poisson-bracket corrections
invariant-subprincipal correction
II_s^H = s*(theta)
curved horizontal/normal frame derivatives
Codazzi / section-pullback terms
Phi_F zero-order curvature insertion
spin and gimmel connection terms
mass, gauge-fixing, boundary, and remaining Z_A terms
gamma-trace constraint source K_mu_nu
```

The actual pass/fail object is not merely `sigma_0` as an amplitude ledger. It is
the coupled characteristic matrix for the RS and constraint subsystem after the
section pullback:

```text
Char_RS_constraint_actual(x, eta; II_s^H, Z_A, K_mu_nu).
```

Pass condition:

```text
For every admissible (x, eta) with eta != 0 and g_s^{-1}(eta, eta) != 0,
the actual coupled characteristic matrix has no kernel.
```

This is the first missing FC-VZ-4 proof object. General real-principal-type
language and generic zero-order arguments are not enough until this actual
section-pulled matrix is computed.

## 7. What Would Change If The Hole Closed

If the actual E-block certificate closed, FC-VZ-1 could stop being a conditional
typed-spine assumption. The 14D Schur replay would then have an actual-GU
`E_actual^(-1)` rather than a formal supplied inverse.

If the section-pulled subprincipal/extrinsic characteristic certificate also
closed, the 4D VZ statement could move beyond "principal-symbol only" to an
actual-operator microlocal result:

```text
No spacelike characteristics for the actual section-pulled RS/constraint
system through principal and invariant-subprincipal order, including II_s^H.
```

That would materially strengthen the VZ route. It would not by itself authorize
this worker to change claim ledgers, and it would not automatically settle every
full dynamical issue unless the same certificate also closes the constrained
Hamiltonian / energy-estimate gates now tracked separately.

## 8. What Would Falsify Or Demote The Route

The E-block route is falsified or demoted if:

```text
actual D_GU^epsilon lacks the required first-order 0/1 block;
a = 0 or b = 0 in the actual Q block;
lambda_d = 0, which leaves possible E-invertibility but collapses the current
  spin-3/2 Schur principal route;
the actual Q sector is not S plus Im(j), or has extra principal components;
there exists real xi with q != 0 and ker E_actual^epsilon(y, xi) != 0;
the proof covers only pure or sample covectors, not all mixed covectors;
the block proof uses `det(M) = det(E) det(S_R)` to prove E-invertibility.
```

The subprincipal/extrinsic route is falsified or demoted if:

```text
II_s^H, curved frame derivatives, K_mu_nu, or a Z_A term enters the effective
  order-one characteristic matrix with a spacelike root;
there exists real eta with g_s^{-1}(eta, eta) != 0 and nontrivial kernel in the
  actual section-pulled coupled RS/constraint characteristic matrix;
the sourced symmetric-hyperbolic estimate for phi = Gamma^4D Psi fails in a way
  that creates spacelike constraint propagation;
a source-derived standalone 4D GU RS Lagrangian is found and its VZ
  characteristic matrix has spacelike roots;
the computation chooses coefficients, sectors, or normalizations using desired
  VZ success rather than source/operator data.
```

## 9. Next Meaningful Computation Or Proof Step

Next frontier object:

```text
VZActualEBlockAndSubprincipalCharacteristicCertificate_V0
```

Prerequisite:

```text
PrimarySourceDGU01SectorRuleRowInstance_V1
```

because current closeouts still block symbol/VZ replay before a primary row or
same-operator witness exists.

Certificate sequence:

```text
1. Emit the source-closed actual D_GU^epsilon 0/1 operator certificate:
   domain, codomain, chirality, 0/1 sector rule, coefficients, and Z_A ledger.

2. Extract:
   E_actual^epsilon = P_Q,out sigma_1(D_GU^epsilon) I_Q,in.

3. Prove the actual E-block kernel/inverse statement for all q != 0 and all
   real mixed 14D covectors.

4. Build:
   S_Rs_4D_full = A_s_full - B_s_full (E_s_full)^(-1) C_s_full
   from the same actual operator.

5. Compute:
   sigma_0^inv(S_Rs_4D_full)(x, eta)
   with II_s^H, curved frame, Phi_F, mass/gauge-fixing/Z_A, Poisson, and
   K_mu_nu terms included.

6. Form and test the coupled RS/constraint characteristic matrix. The pass
   condition is no non-null real kernel, not merely no change to the original
   principal symbol by isolated zero-order terms.
```

## 10. Claim-Status Consistency Result

No claim status changes were made. No claim ledgers were edited. The
claim-status consistency workflow is not triggered by this artifact because it
sharpens a blocker and explicitly refuses VZ promotion.

Consistency result:

```text
target_import_used: false
principal_symbol_full_closure_claimed: false
FC-VZ-1 closed: false
FC-VZ-4 closed: false
full VZ closure claimed: false
```

## 11. JSON Summary

```json
{
  "artifact_id": "VZSubprincipalCharacteristicLedger_V0",
  "run_id": "hourly-20260626-0402",
  "cycle": 1,
  "lane": "VZSubprincipalCharacteristicLedger",
  "artifact_path": "explorations/hourly-20260626-0402-cycle1-vz-subprincipal-characteristic-ledger.md",
  "verdict_class": "blocked_principal_symbol_not_full_vz_closure",
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "principal_symbol_full_closure_claimed": false,
  "terrain": "microlocal-subprincipal_with_upstream_actual_operator_provenance_dependency",
  "first_missing_object": "source_closed_actual_D_GU_epsilon_0_1_operator_certificate_enabling_E_actual_and_sigma0_inv_S_Rs_4D_full",
  "e_block_invertibility_established": false,
  "mixed_covector_characteristic_established": false,
  "next_frontier_object": "VZActualEBlockAndSubprincipalCharacteristicCertificate_V0"
}
```
