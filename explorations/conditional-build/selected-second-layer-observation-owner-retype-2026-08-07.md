---
artifact_type: conditional_build_correction
created: 2026-08-07
status: INDEPENDENT_OBSERVATION_COLUMN_REJECTED__DEPENDENT_NORMAL_JET_ROUTE_OPEN
source_return: SOURCE-CORRECTS__OBSERVATION_IS_RECEIVER_NOT_INDEPENDENT_ACTION_FIELD__SOURCE-SILENT__NORMAL_JET_OF_UPSILON
ledger: lab/process/conditional-physics-ledger-v0.45.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected second-layer observation-owner retype

## Result in plain English

The next construction should not add an independent “observation field” to
repair the missing diffeomorphism direction. A metric and its graph section
are the same ten degrees of freedom, and Weinstein's source describes
observation as the section/pullback receiver for an upstairs action—not as a
second independently varied field of that action.

That does **not** make observation irrelevant. When the metric section moves,
evaluation of an ambient residual has the chain rule

\[
 \delta(r_s^1\Upsilon)
 =r_s^1(D\Upsilon\,\delta\phi)
 +(D_s r_s^1)[\delta s]j^1\Upsilon .
\]

The second term can be nonzero even when `Upsilon` itself vanishes on the
section, because it uses the **normal first jet** of the ambient residual.
The existing selected full-`II` pullback specifies only the on-section map; it
does not specify this normal jet. Therefore v0.44's broad phrase
“section/observation participation” is retyped:

```text
not:  add an independent section/observation action column
yes:  construct the dependent moving-section term inside the total metric
      derivative, from the ambient source residual's actual normal jet
```

The cheap Layer-0 test prevents a duplicate field while preserving the live
geometric route.

## Layer 0

| phrase | object proved here | object kept distinct |
| --- | --- | --- |
| metric section | graph `s_g(x)=(x,g(x))`, whose vertical variation is `h=delta g` | an independent section field with its own action coordinate |
| observation | complete field/equation receiver and moving evaluation | a dynamical counterterm |
| target transport | changes of frame, target pairing and receiver multiplying `Upsilon(0)` | normal derivative of `Upsilon` before evaluation |
| selected full-`II` map | on-section rank-100 conditional pullback into selected `Cl2` | ambient first normal jet of source `Upsilon` |
| owner question | whether the source residual realizes the conditional observer map | a refutation of every GU second action |

This fires Layer 0 before another calculation: a second copy of the metric
carrier cannot be inferred merely because the words “metric” and “section”
occur separately.

## Source return

The 2021 action is declared on inhomogeneous gauge data together with
`MET(X)`. The Oxford/Portal, Into the Impossible, and TOE sources describe
fields upstairs being observed by a metric section and pullback. The existing
source recheck explicitly says this operation does not add a distributional
source term upstairs.

```text
SOURCE-CORRECTS:
  observation is a receiver/package around the upstairs theory, not an
  independently declared second metric field in I2B.

SOURCE-SILENT:
  the normal first jet of Upsilon along the observation section, its complete
  total metric-section derivative, and equality with the selected full-II map.
```

## Exact composition

Let `D` be the rank-four metric diffeomorphism symbol. Since

\[
 \delta s_g=(0,\delta g),
\]

the graph-section vertical tangent is the same matrix `D`. Stacking metric and
graph-section copies along their required diagonal still has rank four, not
eight. It adds no fifth gauge parameter and no new freely specifiable action
column.

The earlier observation theorem supplies an invertible receiver `O`. On every
timelike, spacelike, and null representative,

\[
 H_{obs}=O^T H O,\qquad D_{obs}=O^{-1}D,
\]

so

\[
 H_{obs}D_{obs}=O^T H D.
\]

The exact Ward-defect rank is preserved. Observation transport cannot be
credited as a counterterm.

The normal-jet underdetermination is independent and equally exact. Two
ambient residual extensions can have the same restriction and the same
on-section metric derivative `A`, but normal derivatives `Q_0=0` and
`Q_1!=0`. For a moving graph with vertical derivative `J`, their total
derivatives are

\[
 A+Q_0J\quad\hbox{and}\quad A+Q_1J.
\]

They differ, and the exact plant makes `Q_1 J e_0` nonzero on the same time
generator missed by the rank-three connection lift. Thus a dependent repair
is possible in type, but the on-section full-`II` map cannot select it.

## What changed from v0.44

v0.44 correctly proved that the actual connection component cannot cancel the
conditional metric load on `e_0`. It did not prove that a new observation
field exists. v0.45 keeps the rank obstruction and retracts only the ambiguous
next-step wording.

The remaining construction is now specific:

1. compute the ambient source-native first jet of
   `Upsilon^B=odot F_A+*kappa_1 T` along the admitted metric section;
2. include the dependent moving-section chain-rule term in the **same** metric
   derivative;
3. test total naturality on `e_0` and then all four diffeomorphism generators;
4. compare that source-native derivative with the conditional selected
   full-`II` owner map;
5. only after equality or a typed difference is known, continue to transverse
   variables, scalar/massless constraints, the fermion Hessian and a common
   domain.

## Specialist and hostile review

- **Differential geometry:** graph-section variation is induced by metric
  variation; the normal jet is the actual missing geometric datum.
- **Representation theory:** two isomorphic written carriers do not become two
  independent representations without an owner map.
- **Variational PDE:** an invertible equation receiver preserves symbol rank;
  moving evaluation is instead a jet-prolongation term.
- **Symplectic geometry:** receiver transport neither creates a new radical nor
  performs reduction; the eventual total derivative must still generate the
  correct presymplectic Noether identity.
- **Krein/operator theory:** all current conclusions use exact ranks and chain
  rules, not positivity or a claimed closed domain.
- **Source criticism:** the sources support the receiver architecture and are
  silent on the coefficientwise normal jet.
- **Repo archaeology:** v0.31 already proved observation transports rather than
  cancels, while the moving-observation gate already typed the normal-jet chain
  rule; composing them prevents a redundant new field.

Both hostile charges fired. The summary may not erase the live dependent
normal-jet route, and the lane may not defend a superseded interpretation in
which “section” means an independently supplied field.

## Progress and fences

```text
Ledger v0.45 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 25 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 3
  - metric and graph-section tangents are the same rank-four column
  - invertible observation transport cannot cancel the Ward defect
  - an independent observation action field is not source-owned
frontier_conditions_opened: 1
  - source-native normal first jet of Upsilon
remaining_named_conditions: 4
  - source-native normal jet and total metric-section derivative
  - selected-Upsilon versus full-II owner-map comparison
  - scalar and massless constraint quotient
  - coupled fermion Hessian and common domain
```

No scalar pole, coefficient, residue reduction, fifth quotient, external
datum, canon verdict or public posture changes. P1/P2/P3 remain unused. Curt
remains formally separate and no third lane is promoted.

## Verification

`tests/channel-swings/selected_second_layer_observation_owner_retype_probe.py`
passes `40/40`, including exact predecessor composition and planted failures
against carrier duplication, receiver-as-counterterm, frozen normal jets and
external-datum substitution.
