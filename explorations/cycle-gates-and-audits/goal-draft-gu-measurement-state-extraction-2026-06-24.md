---
title: "Goal Draft: GU Measurement/State Extraction for the Pati-Salam CHSH Gate"
date: 2026-06-24
status: goal-draft
verdict: AMBITIOUS_GOAL_REQUIRES_GU_RHO_AND_MEASUREMENT_POSTULATE
owned_path: "explorations/cycle-gates-and-audits/goal-draft-gu-measurement-state-extraction-2026-06-24.md"
depends_on:
  - explorations/time-as-finality-crosswalk/observer-finality-gu-measurement-postulate-gate-2026-06-24.md
  - explorations/time-as-finality-crosswalk/observer-finality-gu-derived-chsh-state-attempt-2026-06-24.md
  - explorations/time-as-finality-crosswalk/observer-finality-pati-salam-chsh-fixture-2026-06-24.md
  - explorations/cycle-gates-and-audits/gu-typed-operator-action-spine-2026-06-24.md
  - explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md
executable:
  - tests/h3_pati_salam_gu_measurement_gate.py
  - tests/h3_pati_salam_chsh_candidate_state.py
  - tests/h3_pati_salam_chsh_correlator.py
---

# Goal Draft: GU Measurement/State Extraction for the Pati-Salam CHSH Gate

## Goal Statement

Build an auditable GU measurement/state extraction pipeline for the Pati-Salam CHSH
gate.

The target is not to find another Bell-state control. The target is to derive, from GU
operator/action data, a finite Alice/Bob state and measurement interface:

```text
GU zero modes / propagator / two-point state / local algebra state
  -> finite Pati-Salam Alice/Bob reduction
  -> rho_AB in End(H_A tensor H_B)
  -> GU-admissible local +/-1 observables A, A', B, B'
  -> locality/NAC verification
  -> executable CHSH result
```

The ambitious positive outcome is:

```text
role(rho_AB) = "gu_derived"
provenance(rho_AB) starts with "gu-derived:"
provenance(A,A',B,B') starts with "gu-admissible:"
CHSH(rho_AB; A,A',B,B') > 2 + 1e-6
```

The equally important negative outcome is a clean demotion: if the GU-derived state is
separable, if the admissible observables are only commuting charge readouts, or if every
admissible CHSH test stays at `<= 2`, then the observer/finality Pati-Salam CHSH claim is
not physically forced by GU. That would still be a valuable result because it would replace
ansatz optimism with a real state-extraction theorem or no-go.

Controls and ansatz states cannot count as GU-derived. In particular, the maximally
entangled control, the product control, the CPT-paired color-mixed SU(2) Bell ansatz, and
the pure rank-8 CPT-paired Bell ansatz must remain rejected unless an independent GU
zero-mode/two-point calculation actually produces their density matrix and observable
provenance.

## Why This Matters

The formal observer/finality layer has a sharp executable surface, but it is not yet a
physical Pati-Salam result. The missing bridge is the GU measurement postulate plus the
state extraction map. Without that bridge, the existing `2*sqrt(2)` values prove only that
the finite CHSH plumbing works and that the desired obstruction is reachable by controls.

This goal matters because it would decide whether GU supplies the physical content needed
for a real Bell/CHSH forcing claim:

- representation labels would be upgraded into an actual finite density matrix;
- generic vacuum-entanglement language would be replaced by a computed reduced state;
- convenient Pauli controls would be replaced by physically admissible GU observables;
- locality and NAC would be checked for the same live measurement scenario;
- the claim DAG would gain a binary status transition instead of another narrative layer.

In short: this is the narrowest high-value gate where GU can either earn the Pati-Salam
CHSH claim or lose it honestly.

## Current Fixture/Gate Result

The finite proxy already exists:

```text
H_A = V_L = C^4_color tensor C^2_SU(2)_L
H_B = V_R = C^4_anticolor tensor C^2_SU(2)_R
H_AB = H_A tensor H_B
dim(H_AB) = 64
V_L = (4,2,1)
V_R = (4bar,1,2)
```

The control observables are Pauli-type operators on the SU(2) factors:

```text
A  = Z_L
A' = X_L
B  = (Z_R + X_R) / sqrt(2)
B' = (Z_R - X_R) / sqrt(2)
```

The executable controls pass:

```text
rho_control_phi_8        CHSH = 2.828427124746 = 2*sqrt(2)
rho_control_product_00   CHSH = 1.414213562373
```

The strongest current Pati-Salam-labeled ansatz states also reach Tsirelson:

```text
rho_ansatz_cpt_color_mixed_su2_phi   CHSH = 2.828427124746
rho_ansatz_cpt_pure_rank8_phi        CHSH = 2.828427124746
```

Those two ansatz states are deliberately rejected by the GU gate:

```text
GU gate requires role='gu_derived', got 'ansatz'
```

The live GU gate is still pending:

```text
python tests/h3_pati_salam_gu_measurement_gate.py
  -> SKIP_MISSING_GU_INPUTS

python tests/h3_pati_salam_gu_measurement_gate.py --require-gu
  -> FAIL, because no GU-derived rho_AB and no GU-admissible observables are supplied
```

The known missing pieces are:

```text
finite GU zero-mode basis / projector / covariance
GU-induced finite Gram matrix / inner product
density-matrix extraction map to rho_AB
direct-sum field data -> two-observer tensor-product state
GU measurement postulate for admissible noncommuting settings
locality/NAC bridge for the same live state and observables
```

## Exact Deliverables

### D1. GU Source Object

Supply at least one source object with provenance from the GU operator/action spine:

```text
P_ZM                 zero-mode projector
ker(D_GU) basis      after section pullback and physical constraints
G_LR(x_A,x_B)        GU two-point function
K_AB                 finite covariance kernel
omega                GU local-algebra state
```

It must be clear whether the source comes from `D_roll`, a fuller `D_GU`, a section
pullback, a vacuum state, a propagator, or another typed GU construction.

### D2. Finite Pati-Salam Reduction

Define the finite reduction to:

```text
H_A = V_L or a justified finite Alice space
H_B = V_R or a justified finite Bob space
```

including the projection onto:

```text
V_L = (4,2,1)
V_R = (4bar,1,2)
```

and the map from direct-sum field data to the two-system tensor product used by CHSH.

### D3. GU Inner Product And Gram Data

State the GU-induced inner product and its finite reduction:

```text
<psi,phi>_GU
G_A, G_B, and, if needed, G_AB
```

The density matrix and observables must be Hermitian with respect to the GU finite pairing,
not merely with respect to a convenient Euclidean basis. If the standard finite pairing is
used, the derivation must explain why the GU pairing reduces to it.

### D4. Density Matrix Extraction

Produce:

```text
rho_AB in End(H_A tensor H_B)
rho_AB >= 0
Tr(rho_AB) = 1
role = "gu_derived"
provenance = "gu-derived:<specific construction>"
```

The extraction must specify normalization, color/isospin contractions, CPT or left-right
symmetry assumptions, phase conventions, and whether the result is pure, mixed, separable,
partially entangled, or maximally entangled.

### D5. Measurement Postulate

Define the physically admissible local readout algebra:

```text
A, A' in End(H_A)
B, B' in End(H_B)
A^2 = A'^2 = B^2 = B'^2 = I
A = A*, A' = A'*, B = B*, B' = B'*
provenance starts with "gu-admissible:"
```

The postulate must say why the selected same-party settings may be noncommuting. Diagonal
SM/Pati-Salam charge projectors alone are not enough if they only generate commuting
readouts.

### D6. Locality And NAC Certificate

Check, for the derived scenario:

```text
[A_x, B_y] = 0 for Alice/Bob separated regions
rho_AB is not postselected on later settings
Alice settings do not depend on Bob future data
Bob settings do not depend on Alice future data
```

This certificate should connect the finite matrix commutation check to the GU null-cone /
section-pullback / NAC story rather than treating locality as only a tensor-product
convention.

### D7. Executable Integration

Wire the result into the existing hooks:

```text
supply_gu_derived_rho_ab()
supply_gu_admissible_observables()
```

without weakening the role/provenance checks or copying any control/ansatz object into the
GU slot.

### D8. Outcome Report

Emit one explicit outcome:

```text
GU_DERIVED_STATE_FOUND
SEPARABLE_OR_NO_VIOLATION
STRONG_ANSATZ_ONLY
OPEN_MISSING_GU_MEASUREMENT_POSTULATE
OPEN_MISSING_GU_STATE_EXTRACTION
INVALID_CONTROL_PROMOTION
```

The outcome must update the live claim posture without upgrading downstream claims beyond
the evidence.

## Acceptance Criteria

The positive gate passes only if all of the following hold:

1. `rho_AB` is derived from a stated GU source object, not inserted as a Bell state.
2. `rho_AB` has `role="gu_derived"` and `provenance` beginning with `gu-derived:`.
3. `rho_AB` is Hermitian, positive semidefinite, trace one, and typed on the stated
   finite Alice/Bob spaces.
4. The finite inner product or Gram convention is GU-derived or explicitly justified.
5. The Alice/Bob factorization is derived or explicitly reduced from GU local algebras,
   not merely inferred from the direct sum `V_L + V_R`.
6. The observables are self-adjoint `+/-1` operators with provenance beginning with
   `gu-admissible:`.
7. The measurement postulate explains admissible noncommuting same-party settings.
8. Alice/Bob observables commute locally and satisfy the NAC/no-postselection discipline.
9. The existing executable gate computes:

```text
CHSH = Tr(rho_AB (A tensor B + A tensor B' + A' tensor B - A' tensor B'))
CHSH > 2 + 1e-6
```

10. Known controls and ansatz states remain rejected when presented as GU evidence.

## Failure/Demotion Criteria

Demote or fail the goal if any of the following occurs:

- The only violating states are the existing controls or CPT/Bell ansatz states.
- A state is called GU-derived because it has Pati-Salam labels but no GU source object.
- CPT pairing is used as a substitute for a density matrix, Schmidt spectrum, or
  covariance calculation.
- Generic Reeh-Schlieder, Bisognano-Wichmann, or vacuum-entanglement language is used
  without a finite `rho_AB` extraction.
- The measurement postulate permits only commuting charge projectors and therefore cannot
  realize a nontrivial CHSH setting pair.
- The chosen observables are Pauli controls with relabeled provenance instead of
  physically derived readouts.
- The GU-derived state is separable, SU(2)-uncorrelated, or otherwise gives
  `CHSH <= 2` for all GU-admissible settings.
- The finite result depends on postselection, future settings, or a hidden nonlocal
  Alice/Bob coupling.
- The finite inner product is chosen for convenience and conflicts with the GU pairing.
- The result passes only after weakening role/provenance checks in the executable gate.

The correct demotion in these cases is not "the fixture failed." The fixture already
works. The correct demotion is that GU has not physically forced the Pati-Salam CHSH
violation.

## Dependencies

Mathematical and physical dependencies:

```text
typed GU operator/action spine
section-pullback carrier and physical zero-mode space
Pati-Salam split S(6,4) -> (4,2,1) + (4bar,1,2)
finite GU inner product / Gram reduction
GU vacuum, propagator, covariance, or local-algebra state
CPT / left-right symmetry status of the selected branch
measurement postulate for admissible local readouts
locality/NAC bridge for the live measurement scenario
```

Executable dependencies:

```text
tests/h3_pati_salam_chsh_correlator.py
tests/h3_pati_salam_chsh_candidate_state.py
tests/h3_pati_salam_gu_measurement_gate.py
```

Governance dependencies:

```text
OBS-CHSH remains executable_controls_pending until this gate closes
controls remain controls
ansatz states remain ansatz
status upgrades must name the closure condition that changed
```

## First 3 Concrete Work Packets

### Work Packet 1: Measurement Interface Contract

Write the minimal formal contract for a GU-derived CHSH submission:

```text
GuSource
FiniteReduction
GuInnerProduct
DensityExtraction
AdmissibleObservableSet
LocalityNacCertificate
```

The immediate output is a specification that says exactly what data must be supplied to
replace the pending hooks. This packet should also list forbidden shortcuts, especially
copying `rho_control_phi_8`, `rho_ansatz_cpt_color_mixed_su2_phi`, or
`rho_ansatz_cpt_pure_rank8_phi` into the GU slot.

### Work Packet 2: State Extraction Prototype

Choose one GU source lane and compute the finite `rho_AB` all the way down:

```text
zero-mode projector lane
two-point/covariance lane
or local-algebra state lane
```

The first prototype does not need to violate CHSH. It does need to produce a real density
matrix with trace, positivity, Gram/Hermiticity, color/isospin contraction, and
left/right/CPT assumptions visible. If the derived state is maximally mixed or separable,
record that as useful evidence instead of repairing it with an ansatz.

### Work Packet 3: Measurement Postulate Prototype

Derive one nontrivial admissible local observable set from GU/Pati-Salam readout rules:

```text
A, A' on H_A
B, B' on H_B
```

The prototype must explain whether these are spectral projectors of physical charges,
gauge-rotated isospin readouts, local field-operator functions, or another GU observer
readout. It must also explain why the same-party settings can be noncommuting while
Alice/Bob settings commute locally.

## What This Would Lead To

If the goal succeeds positively, the project gets its first genuine physical Pati-Salam
CHSH forcing artifact:

```text
GU-derived rho_AB
GU-admissible observables
locality/NAC certificate
CHSH > 2 + 1e-6
```

That would upgrade `OBS-CHSH` from executable controls pending to a real derived
measurement result, subject to whatever dependencies remain in the GU operator/action and
section-pullback lanes.

If the goal succeeds negatively, the project still gains a high-value result:

```text
GU-derived rho_AB exists but no admissible violation occurs
or admissible observables are too commuting/classical
or the extraction map blocks the finite CHSH claim
```

That would demote the physical-forcing interpretation while preserving the formal
observer/finality layer and the finite fixture as controls.

Either way, this goal turns the Pati-Salam CHSH story from "the desired Bell state is
reachable" into "GU either derives the state and measurements, or it does not." That is the
right next ambition.

