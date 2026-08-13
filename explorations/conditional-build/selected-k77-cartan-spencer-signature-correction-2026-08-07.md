---
artifact_type: conditional_build_correction
created: 2026-08-07
status: COEFFICIENT_REPAIR_THEOREM_SURVIVES__OLD_EXACT_VALUES_SUPERSEDED__COVARIANT_GRAPH_DESCENT_OPEN
source_return: SOURCE-CONFIRMS__SPIN77_Y77_AND_NORMAL64_PRESENTATION__SOURCE-SILENT__FOUR_COLUMN_GRAPH_SELECTION_AND_DESCENT
ledger: lab/process/conditional-physics-ledger-v0.57.json
canon_verdict_change: none
---

# K77 Cartan/Spencer signature correction

## Result in plain English

The last two pointwise Cartan/source-`varpi` Runs used the wrong signs while
calling them `(7,7)`. Their metric actually had inertia `(9,5)`. Because the
same wrong metric was used in both the forward map and its inverse, every
self-consistency control passed.

Rebuilding the complete chain with the settled K77 metric changes every one
of the four target columns and every one of the four source lifts. The old
exact coefficient values must not be used in the atlas calculation.

The structural theorem survives:

```text
correct K77 inertia                         (7,7)
raw graph-target supports                  58,29,29,29
non-null connection/transverse split       7+51, 7+22, 7+22, 7+22
K77 Koszul/source-lift supports             57,34,34,34
four-column family rank                     4
pointwise coefficient freedom              0
```

Exactly `12` target coordinates change in each column, and the final Koszul
preimages change in `30,34,34,34` coordinates. The old coefficient values are
superseded. Thus this is a real coefficient
correction, not a prose-only relabeling, but it does not retract pointwise
source-coordinate realizability.

## Layer 0: what failed

The settled K77 chimeric metric is the direct sum of horizontal `(1,3)` and
vertical trace-reversed `(6,4)` blocks. In the coordinate ordering used by the
selected Shiab backend its signs are

```text
(+,-,-,-, +,+,+,+,+,+, -,-,-,-),
```

with inertia `(7,7)`.

The v0.46 normal-jet comparator and v0.55 Spencer probe instead executed

```text
(-,+,+,+, +,+,+,+,+,+, -,-,-,-),
```

with inertia `(9,5)`, although the v0.55 report called it the settled `(7,7)`
metric. The error entered twice:

1. it set the four raw graph-target coefficients; and
2. it set the later Koszul inverse.

An inverse can perfectly invert the wrong forward map. Therefore the old
left/right inverse checks proved algebraic exactness on the conditional
`Cl(9,5)` fork, not correct porting to K77. This is a worked instance of the
standing rule that controls verify the computation stated; Layer 0 verifies
that the computation is about the intended object.

## Exact corrected chain

The executable does not merely flip signs in the last formula. It reconstructs
the full dependency chain:

1. Rebuild the raw `1,274 x 10` conditional residual Jacobian using the K77
   metric. It retains rank ten, and its four graph-orbit columns retain rank
   four and supports `58,29,29,29`.
2. Solve those four new targets inside the already exact K77 selected-Shiab
   image. All four solve uniquely with supports `58,29,29,29`.
3. Apply the non-null `q=e^0` split. The connection pieces retain support
   seven and the transverse pieces retain `51,22,22,22`, totaling `117`.
4. Apply the Koszul inverse using the actual K77 signs. It reproduces every
   transverse target and yields supports `57,34,34,34`, rank four.
5. Compose with the fixed-epsilon source tangent at
   `T*=-(kappa_1/312)Phi1`. All four corrected source-`varpi` lifts reproduce
   the corrected targets coefficientwise.

The old source lifts fail all four corrected endpoint targets. Equal ranks and
support counts are therefore not sufficient provenance for reusing their
coefficients.

## Source return

Curt's transcript presentation and the released draft both name the split
`Spin(7,7)`/`Y^(7,7)` carrier, with the draft explicitly writing a `(6,4)`
normal block. The repository, not the source, supplies the exact coordinate
sign convention and correction.

```text
SOURCE-CONFIRMS:
  Spin(7,7), Y^(7,7), and the displayed (6,4) normal-block presentation.

SOURCE-SILENT:
  the four fitted source-varpi columns, their covariant graph selection,
  exact K77 overlap law, Spencer integrability and Euler descent.
```

## Constraint surplus and external datum

The correction adds no field, coefficient, sign datum, choice of background,
or external datum. At the fixed nonzero background the K77 Cartan map is still
invertible, so the corrected pointwise lift has zero coefficient freedom.

The global surplus remains uncomputed. Transition, graph-natural, Spencer,
Bianchi and action constraints have not yet been ranked against any remaining
freedom. P1/P2/P3 remain unchanged and unused.

## Specialist and hostile review

- **Differential geometry:** signature is part of the bundle metric, not a
  label. A natural Koszul formula must use the metric on the actual bundle.
- **Representation theory:** `Cl(7,7)` and `Cl(9,5)` are different real
  Clifford forks even though the tensor-domain dimensions agree and both
  Spencer maps are isomorphisms.
- **Variational PDE / hyperbolic equations:** the correction changes lower
  coefficient data but does not change the still-open principal/null/domain
  analysis.
- **Symplectic geometry:** no Euler covector, Green current, presymplectic
  reduction or BFV class follows from the repaired pointwise lift.
- **Krein/operator theory:** changing real form is load-bearing for the Krein
  carrier; the result makes no positivity or common-domain claim.
- **Source criticism:** source evidence selects the K77 presentation but does
  not print this four-column construction.
- **Repo archaeology:** the selected-Shiab backend already held the correct
  K77 signs. The defect arose when the conditional `(9,5)` full-II comparator
  was composed with it and then mislabeled.

Both hostile charges fire. The summary had outrun the executed metric, and a
rigorous inverse was defending a superseded fork. The repair refuses the
opposite overreaction: the coefficient error does not kill a signature-
independent isomorphism once the whole target chain is recomputed.

## Progress and fences

```text
Ledger v0.57 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 1
  - the pointwise four-column chain is now coefficient-correct on K77
frontier_conditions_opened: 0
remaining_named_conditions: 3
  - covariant four-column graph morphism plus constraint-surplus count
  - Spencer/atlas integrability and total raw-Upsilon Bianchi/naturality
  - survivor-only Euler/preboundary, null quotient and common domain
```

No verdict, residue, quotient, canon verdict or public posture moves. The five
affected ledger rows receive mapping-grade/provenance corrections only.

## Next gate

Resume the previously selected gate using only the corrected K77 columns:
construct one covariant four-column source-`varpi` graph morphism, count its
constraint surplus, and test Spencer compatibility plus actual three-patch
K77 atlas descent with a non-descending plant. Only surviving columns may
advance to raw-`Upsilon` Bianchi/naturality and first-action
Euler/preboundary/symplectic descent.

The exact probe passes `43/43`, including historical replays and planted
failures against self-validating signature pairs, support/rank-only reuse and
global promotion.
