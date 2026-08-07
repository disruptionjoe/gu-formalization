---
artifact_type: conditional_build_correction
created: 2026-08-07
status: V052_MOVING_OPERATOR_KILL_RETRACTED__CONNECTION_Q_EXACT_CLASS_SURVIVES__CONSTITUENT_BACKGROUND_RESPONSE_OPEN
source_return: SOURCE-CONFIRMS__UPSILON_HAS_DISTINCT_CURVATURE_AND_TORSION_CONSTITUENTS__SOURCE-SILENT__PHYSICAL_METRIC_OPERATOR_DERIVATIVE_ON_SELECTED_BACKGROUND
ledger: lab/process/conditional-physics-ledger-v0.53.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected second-layer residual-constituent operator correction

## Result

Ledger v0.52 correctly proved that every connection-curvature principal
variation remains `q wedge delta A`, so that class owns the 28 q-exact
coefficients and cannot own the 117 transverse coefficients. It incorrectly
extended a stationary norm-square simplification to the raw residual itself.

The source residual is a sum

```text
Upsilon = Shiab(F_A) + Hodge(kappa T).
```

`Upsilon_0=0` does not imply `F_A0=0` and `T_0=0`. In fact the selected branch
already has `T*=-(kappa_1/312)Phi1`, which is nonzero. Therefore physical
metric movement can contribute

```text
(D Shiab) F_A* + (D Hodge)(kappa T*)
```

even when the total residual vanishes. An exact two-component counterexample
has two nonzero cancelling constituents, total residual zero, and a nonzero
independent operator derivative. A second control makes both operators move
by one common equivariant transport; that derivative is `K Upsilon_0=0`.
Thus pure frame/gauge co-motion still cancels, while independent physical
Shiab/Hodge variation remains open.

## Layer 0

| object | correct statement | forbidden collapse |
| --- | --- | --- |
| stationary norm square | derivatives of its target pairing/receiver multiply total `Upsilon_0` | raw `D Upsilon` operator terms |
| raw residual | sum of curvature and torsion constituents | one input field called `F_0=Upsilon_0` |
| pure co-motion | common conjugation/transport gives `K Upsilon_0=0` | independent physical metric variation of Shiab and Hodge |
| connection curvature | principal symbol remains q-exact | all moving-operator response |
| selected background | nonzero `T*` is already constructed | constituent-zero flat vacuum |

## Corrected next gate

Construct the actual selected stationary constituent background
`(F_A*,T*)`, using the residual equation and the exact selected-Shiab map;
then compute the physical metric-normal derivatives of Shiab and Hodge on
those constituents, together with the ambient field normal jet. Compare the
four resulting graph columns coefficientwise with the transverse 117. Do not
search another connection-curvature symbol, and do not assume pure co-motion
covers physical metric variation.

## Reviews and boundary

- Differential geometry keeps common equivariant transport separate from
  primitive metric dependence of Hodge/Shiab.
- Variational PDE keeps the stationary norm-square Hessian theorem intact but
  forbids using it as a raw-residual derivative theorem.
- Symplectic geometry confirms that this correction still supplies no Euler,
  presymplectic, BV or BFV descent.
- Krein/operator theory notes that no positivity or domain assumption enters.
- Source criticism confirms the two constituent terms and is silent on their
  selected physical metric derivative.
- Repo archaeology caught the contradiction with the already-built nonzero
  stationary `T*` branch.

The two hostile charges both fired: the summary outran the product-rule
artifact, and the lane began defending a mistyped input. v0.52 is preserved as
provenance; v0.53 appends the correction.

```text
Ledger v0.53 — 82/82 mapped
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84 + >=19 functions + 9 forks · 4 scoped quotients
frontier closed: 3 · opened: 1 · remaining: 5
```

P1/P2/P3 remain unused. Curt remains separate. No verdict, canon or posture
moves. Main probe: `17/17 PASS`.
