---
artifact_type: conditional_build_correction
created: 2026-08-07
status: OWNER_MAP_RETYPED__RAW_CARRIER_COMPATIBLE__ACTUAL_PROLONGATION_OPEN
source_return: SOURCE-CORRECTS__USE_RAW_UPSILON_DIFFERENTIAL__SOURCE-SILENT__BACKGROUND_SUBTRACTION_OWNER_AND_PROLONGED_ORBIT_COEFFICIENTS
ledger: lab/process/conditional-physics-ledger-v0.46.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected second-layer normal-jet carrier compatibility

## Result in plain English

The source has enough geometric room for the missing moving-section response,
but the recent argument was trying to infer that response from the wrong
object.

The exact selected residual map before any background subtraction is a
`1,274 x 10` Jacobian. On the four metric diffeomorphism directions it has
rank four, including a nonzero response on the time generator missed by the
independent-connection lift. Every one of the four compensating normal-jet
columns lies inside the already-built rank-`1,190` mixed-normal image of the
selected `comm/symi/symi` Shiab. There is therefore **no carrier or
representation obstruction**, and no new datum is needed merely to express
the correction.

But the off-TT operator used in v0.42 is

\[
 K_{bg}(s)=J(s)^!GJ(s)-J(0)^!GJ(0).
\]

It is not

\[
 [J(s)-J(0)]^!G[J(s)-J(0)].
\]

At the exact test point `s=2`, the difference between those two ten-by-ten
matrices has rank ten. Consequently the rank-monotonicity step in v0.43 cannot
infer a source `D Upsilon` from `K_bg`: it applies to one Gram factorization,
not a difference of two Gram forms.

So the construction is retyped rather than killed:

```text
kept:    exact raw selected residual map and mixed-normal source carrier
kept:    all TT/SO3/off-TT arithmetic as conditional full-II comparators
removed: claim that the background-subtracted Hessian forces D Upsilon
next:    compute the actual prolonged diffeomorphism jet of the source fields
         and compare raw Upsilon coefficientwise on four graph-orbit columns
```

## Layer 0

| phrase | object used here | object kept distinct |
| --- | --- | --- |
| raw residual differential | `J(s)=D Upsilon_cond(s)` from the exact selected `Cl2 <- II <- g` map | the source-native total `D Upsilon` |
| background subtraction | difference of two Hessians `K(s)-K(0)` | Gram of a residual difference |
| normal first jet | derivative of the Euler residual along metric-fibre directions | conormal Legendre symbol of the first-order action |
| carrier compatibility | required four columns lie in the selected mixed-normal Shiab image | actual prolonged field-jet coefficients |
| selected product | repo-selected `comm/symi/symi` row from Bianchi plus nonvacuity | Weinstein's unrecovered preferred historical selector |

This is the control that the previous Runs did not perform. Controls verified
their matrix arithmetic, but Layer 0 asks whether the subtracted matrix still
has the residual-Gram owner required by the inference. It does not.

## Source return and archaeology

The 2021 source displays the raw bosonic residual

\[
 \Upsilon^B=\odot F_A+*\kappa_1T
\]

and the second action as its norm square. It does not display a
zero-momentum subtraction of the Hessian, an action term that generates such a
subtraction, or the four prolonged graph-orbit coefficients.

The source-owned normal carrier was not actually new. The 2026-08-05
conormal-symbol wave already proved that `I1B` retains ambient normal first
jets, and the moving-Shiab wave computed all 85 mixed-normal exterior
directions. On the later-selected `comm/symi/symi` row the complete
grade-one bank has rank `1,190`. v0.45 did not compose those facts with its
new four-column burden.

```text
SOURCE-CORRECTS:
  use the raw Upsilon differential unless an action-owned subtraction is built.

SOURCE-SILENT:
  the background-subtraction owner and the actual prolonged diffeomorphism
  coefficients that must realize the four compatible columns.
```

## Exact construction

The complete selected residual map `T` is the already-certified sparse
`1,274 x 100` matrix. The constant-section metric-to-`II` maps at rest momentum
square zero and two are `P_0` and `P_2`, giving

\[
 J_0=TP_0,\qquad J_2=TP_2.
\]

Both `J_2` and `J_2-J_0` have rank ten. Their restrictions to the rank-four
metric diffeomorphism symbol `D` have rank four, and both are nonzero on
`e_0`.

With the exact target metric `G`, define

\[
 K_{bg}=J_2^!GJ_2-J_0^!GJ_0,
 \qquad
 K_{diff}=(J_2-J_0)^!G(J_2-J_0).
\]

The probe proves

```text
K_bg != K_diff,
rank(K_bg-K_diff) = 10,
rank(K_bg D) = rank(K_diff D) = 4.
```

The last equality is the nonvacuous trap: identical Ward-defect ranks do not
make the two owners equal.

For source-carrier compatibility, the exact K77 Shiab is primalized from
degree thirteen to the same one-form/Clifford-grade-two target. The selected
mixed-normal bank has `85 x 14 = 1,190` columns and rank `1,190`. Appending the
four columns `-J_2D` changes its rank by zero; appending the four formal
difference columns `-(J_2-J_0)D` also changes rank by zero. The raw time column
has 58 nonzero coefficients and the difference time column has 13, so neither
containment result is vacuous.

This proves possibility in the correct carrier. It does not solve for or
identify the source-owned diffeomorphism prolongation.

## Specialist and hostile review

- **Differential geometry:** the graph variation is induced by the metric;
  the missing coefficient is the prolonged Lie derivative of existing
  ambient fields, not a second section variable.
- **Representation theory:** exact image containment replaces dimension
  matching; the selected source image genuinely contains all four columns.
- **Variational PDE:** the Hessian difference is not a residual square, so its
  rank cannot be pulled backward through a nonexistent single Jacobian.
- **Symplectic geometry:** neither image containment nor a diagnostic Ward
  radical constructs the covariant presymplectic quotient or BFV phase space.
- **Krein/operator theory:** the result uses the actual indefinite target
  metric but makes no positivity, self-adjointness or closed-domain claim.
- **Source criticism:** raw `Upsilon` and its norm square are source-displayed;
  the subtraction and prolonged coefficients are source-silent.
- **Repo archaeology:** two August 5 normal-jet theorems were already present;
  the error was failure to compose them and failure to type the subtraction.

Both two-sided hostile charges fire. The summary may not turn carrier
compatibility into an actual coefficient match, and the lane may not defend a
rigorous rank argument whose Gram owner disappeared under subtraction.

## Progress and fences

```text
Ledger v0.46 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 25 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 3
  - the source mixed-normal first-jet carrier was already built
  - all four raw required orbit columns lie in that carrier
  - background-subtracted Hessian is not a residual Gram
frontier_conditions_opened: 1
  - explicit action/counterterm owner for any background subtraction
remaining_named_conditions: 4
  - actual prolonged raw-Upsilon diffeomorphism field jet and owner comparison
  - optional action-owned background subtraction
  - scalar and massless constraint quotient
  - coupled fermion Hessian and common domain
```

No scalar pole, coefficient, fifth quotient, external datum, canon verdict or
public posture changes. P1/P2/P3 remain unused. Curt remains formally separate
and no third lane is promoted.

## Next gate

Construct the source-owned first prolongation `j1(L_xi A)` together with the
moving Hodge, Shiab, Levi-Civita and graph terms in raw `D Upsilon`. Evaluate
only the four graph diffeomorphism columns and compare them coefficientwise
with the conditional full-`II` residual map. If a background-subtracted
operator is still desired, derive it from an explicit action or counterterm
before using it for scalar, pole or physical-spectrum claims.

The exact probe passes `42/42`, including planted failures against Gram
equivocation, rank-only matching, selector attribution, carrier-equals-map and
physical-quotient promotion.
