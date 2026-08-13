---
artifact_type: construction_result
created: 2026-08-06
status: INTRINSIC_HOMOGENEOUS_WARD_EXACT__MOVING_SHIAB_LOAD_BEARING__FULL_DIRECT_MOVING_PREBOUNDARY_CLASS_OPEN
ledger_rows: [LT-GR1, LT-GR2b, LT-GR5, LT-GR6, LT-SM8]
source_return: SOURCE-CONFIRMS
canon_verdict_change: none
---

# Selected cubic intrinsic homogeneous Ward closure

## Result in plain English

The intrinsic augmented-torsion part of the candidate action now survives the
next internal-gauge test exactly.  The previous wave removed the shared
derivative of the two connections by using the source-owned difference
`T=A-B`.  This wave varies the remaining lower-order part,

```text
delta_chi T = [T,chi],
```

together with the source's moving `Phi1/Phi2` Shiab data and the invariant
top-scalar pairing.  The full intrinsic variation is zero for all 91 bivector
generators of the exact K77 Clifford evaluator.

This is information-bearing: if the Shiab data are incorrectly frozen, four
of the 91 generators leave nonzero exact defects (`-8`, `-8/3`, `-8/3`,
`-8/3`). Reversing the moving-`Phi` sign doubles those defects. The moving
Shiab owner is therefore load-bearing, not decoration.

The result does **not** close the whole GU action. Direct curvature, full
second-fundamental-form and defect terms, moving metric/Hodge/DeWitt/Krein and
observation terms, primitive epsilon Euler/Green data, diffeomorphism and odd
BV closure, and the physical preboundary/BFV quotient remain open.

## Layer 0: six distinctions that control the claim

1. The already-closed principal affine derivative is not the homogeneous
   commutator tested here.
2. Primitive epsilon variation (`D_B eta`) is not the simultaneous internal
   gauge orbit (`[T,chi]`).
3. Varying the input `T wedge T` is not enough; `Phi1/Phi2` and hence the
   selected Shiab map move as well.
4. A pointwise invariant scalar is not the full covariant preboundary class.
5. The ordinary even internal-gauge Ward identity is not odd super-IG BV
   closure or diffeomorphism descent.
6. Zero gauge variation is not a nonzero reduced physical transition.

## Source collision

`SOURCE-CONFIRMS`, narrowly scoped. The primary-source reconstruction makes
`Phi_i(epsilon)=Ad_(epsilon^-1) Phi_i^0`, supplies the two-connection
augmented-torsion grammar, and identifies equivariance as the purpose of the
moving Shiab construction. It does not state the exact 91-generator Ward
theorem, a global bundle theorem, or any physical quotient. The companion
pullback/source audit remains `SOURCE-SILENT` on the full moving Ward/BV and
physical-domain questions.

## Lightweight ten-lens preassessment

- Affine gauge geometry required the principal/homogeneous split.
- Differential geometry required moving `T`, `Phi1`, and `Phi2` together.
- Invariant theory required a structural derivation and a nonvacuous exact
  scan.
- Variational PDE required varying the written scalar fragment.
- Shiab geometry required both input and insertion response.
- Krein/operator theory allowed only the native invariant pairing, with no
  positivity inference.
- Symplectic/BV analysis required fencing the preboundary and reduced phase
  space.
- Source criticism limited the source return to the arena it actually states.
- Constraint accounting required zero fitted coefficients and no P1/P2/P3.
- Epistemic breadth required retiring the superseded frozen-Shiab burden while
  leaving absent action owners open.

## Exact theorem and calculation

For the admitted inner action `delta_chi X=[X,chi]`:

1. `delta_chi` is a derivation of the raw exterior/Clifford product.
2. Hodge acts on form indices and commutes with the coefficient inner action.
3. Varying both the input and `Phi1/Phi2` insertions gives
   `delta_chi Shiab(X)=[Shiab(X),chi]`.
4. The invariant top-scalar coefficient trace kills the total commutator.

Therefore the quadratic and selected cubic intrinsic action variations vanish.
The production probe checks this on every one of the 91 K77 bivector basis
generators, including a nonzero radial branch. A separate Sage construction
over `QQ` rebuilds a four-dimensional exterior algebra and three-dimensional
matrix coefficient algebra; it reproduces exact moving covariance and a
nonzero frozen defect `-4`. That Sage route is a structural control, not a
second exhaustive K77 realization.

## Constraint and datum accounting

No compensator, fit coefficient, selector, measure or normalization was
introduced. The construction uses the source-owned moving insertions. Residue
stays `84 continuous + >=19 function-valued + 9 forks`; the four already-ranked
quotients are unchanged; P1/P2/P3 remain unused.

## Symplectic and variational boundary

The simultaneous homogeneous inner variation is pointwise and algebraic at
this fragment grade. Its cancellation says that this intrinsic scalar descends
through that internal orbit. It does not establish a fifth quotient or a
nonzero class on reduced covariant phase space. Primitive epsilon variation
still contains a covariant derivative and therefore has a distinct Green/
preboundary row. Direct and moving geometry may change the presymplectic
potential and boundary charge. No BFV phase space, Fock metric, Q1 pole or
physical sheet follows.

## Seven-axis disposition

- L1 syntactic: exact action fragment and transformation rules are written.
- L2 type: all tested terms share the exterior/Clifford coefficient algebra.
- L3 algebraic: exact for all 91 K77 bivector generators.
- L4 geometric: pointwise inner action only; global bundle descent is open.
- L5 variational: intrinsic homogeneous scalar Ward variation is exact;
  primitive epsilon and moving geometry are open.
- L6 analytic: no domain, positivity or Green theorem is claimed.
- L7 physical: no particle, pole, cosmological or unitarity result is claimed.

## Ledger movement and next gate

Ledger v0.23 makes distance-only migrations on `LT-GR1`, `LT-GR2b`,
`LT-GR5`, `LT-GR6`, and `LT-SM8`. Verdicts, reason kinds, denominator,
residue, quotient count and revival triggers do not change.

The next high-information gate is to assemble the remaining direct curvature,
full-II and defect `D3` owners with moving metric/Hodge/DeWitt/Krein pairing
and observation response, then derive their Euler/Ward/preboundary rows. Only
the complete reduced class may advance to Q1.

## Executable evidence

- `tests/channel-swings/selected_cubic_intrinsic_homogeneous_ward_closure_probe.py`
- `tests/channel-swings/selected_cubic_intrinsic_homogeneous_ward_closure_independent.sage`
- `lab/process/selected-cubic-intrinsic-homogeneous-ward-closure.json`
- `lab/process/hostile-reviews/2026-08-06-selected-cubic-intrinsic-homogeneous-ward-closure-review.md`
