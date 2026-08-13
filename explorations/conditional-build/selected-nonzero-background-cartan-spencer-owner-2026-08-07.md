---
artifact_type: conditional_build_result
created: 2026-08-07
status: FULL_UNRESTRICTED_CARTAN_SPENCER_CARRIER_OWNER__LEVI_CIVITA_SUBCLASS_Q_EXACT__INDEPENDENT_VARPI_OR_AMBIENT_NORMAL_JET_OPEN
source_return: SOURCE-CONFIRMS__TWO_CONNECTION_TRANSLATION_CURVATURE_AND_NONZERO_T_BRANCH__SOURCE-SILENT__ACTUAL_FOUR_COLUMN_INDEPENDENT_VARPI_SOLDERING_OBSERVATION_NORMAL_JET
ledger: lab/process/conditional-physics-ledger-v0.55.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected nonzero-background Cartan/Spencer owner

## Result in plain English

The missing transverse `117` coefficients now have an exact geometric carrier,
but not yet the actual GU field jet.

The earlier fixed-reference calculation kept only the principal term

```text
q wedge delta T.
```

That term can own the `28` coefficients whose exterior pair contains `q`, and
cannot touch the other `117`. On the already-selected nonzero branch

```text
T_* = t Phi1,   t = -kappa_1/312 != 0,
```

the linearization of the full translation curvature also contains

```text
[delta B,T_*].
```

For an unrestricted metric-compatible connection variation this is the
standard Cartan/Spencer map

```text
V* tensor so(7,7)  -->  Lambda2 V* tensor V.
```

Both spaces have dimension `1,274`, and the exact Koszul formula is a
two-sided inverse on every basis vector. Applying that inverse to the four
transverse packets reproduces all `117` coefficients exactly. Their unique
preimages have supports `57,34,34,34` and rank four. Combining those responses
with the already-owned `28` q-wedge coefficients reconstructs all four complete
inverse-Shiab packets coefficientwise.

The important correction is the Levi-Civita restriction. A true moving
Levi-Civita connection obeys the linearized torsion-free equation

```text
D_B(delta Phi1) + [delta B,Phi1] = 0.
```

At principal covector `q`, this forces `[delta B,Phi1]` back into
`q wedge delta Phi1`. Its transverse intersection is therefore exactly zero.
So the unrestricted connection carrier succeeds, while the Levi-Civita
subclass alone does not. The live next route is the independent `varpi`
connection/ambient observation normal jet, or another source-owned higher jet;
it is not another attempt to squeeze the `117` out of Levi-Civita motion.

## Layer 0

| phrase | object proved here | object kept distinct |
| --- | --- | --- |
| Cartan/Spencer map | algebraic response `[delta B,t Phi1]` on unrestricted metric-compatible connection variations | the principal connection symbol `q wedge delta T` |
| carrier owner | an exact preimage for each of the four transverse packets | the actual GU graph-column tangent law selecting those preimages |
| Levi-Civita variation | connection variation constrained by the linearized torsion-free structure equation | an arbitrary `V* tensor so(7,7)` variation |
| independent connection | the source-owned `varpi`/full-adjoint field class that may contain non-Levi-Civita directions | the gauge-rotated Levi-Civita reference alone |
| raw curvature | the coefficient-one translation-curvature term in `F_A` | the coefficient-one-half path-average term in the first action |
| nonzero background | the selected `T_*=-(kappa_1/312)Phi1` branch | a new external scale or free background datum |
| exact packet | `28+117` coefficients in a selected odd two-form carrier | `145` physical modes, an Einstein equation or a reduced state space |

Layer 0 therefore gives two answers, not one: `YES` for the unrestricted
connection carrier; `NO` for the torsion-free Levi-Civita subclass. Neither is
yet the coefficientwise independent-`varpi`/observation tangent demanded by
the Ward and Euler maps.

## Exact theorem

Let `V` carry the settled signature `(7,7)` metric `eta`, let `Phi1` be the
tautological soldering form and write a metric-compatible connection variation
as `omega_(mu,ab)=-omega_(mu,ba)`. The algebraic linearization at
`T_*=t Phi1` is, up to the nonzero scalar `t`,

```text
K(omega)^c_(mu,nu)
  = omega_mu^c_nu - omega_nu^c_mu.
```

Lowering the output index, the inverse is the Koszul formula

```text
omega_(mu,a,b)
  = 1/2 (K_(mu,b,a) - K_(b,a,mu) + K_(a,mu,b)).
```

The executable certificate checks both composites on all `1,274` basis
vectors, with the actual signature signs. Hence `K` is an isomorphism for
every `t != 0`. At `t=0` it vanishes; that planted control prevents the
nonzero-background conclusion from being read as background-independent.

The four exact transverse targets have `51,22,22,22` nonzero coefficients.
Their Koszul preimages have `57,34,34,34` coefficients and rank four. Every
forward image equals the target coefficientwise. The four complete
`28+117` packets also have exact preimages and rank four.

## Why the Levi-Civita subclass does not close the packet

For a Levi-Civita connection, `D_B Phi1=0`. Linearizing gives

```text
[delta B,Phi1] = -D_B(delta Phi1).
```

At principal grade the right side is `-q wedge delta Phi1`, supported only on
exterior pairs containing `q`. All `117` transverse coefficients use exterior
pairs not containing `q`. The intersection is zero coefficientwise, and every
one of the four required Koszul preimages lies outside this constrained
subclass.

This does not contradict Weinstein's gauge-rotated Levi-Civita prescription.
It says precisely what that prescription can and cannot supply at this grade.
The source also owns an independent full-adjoint connection `varpi` and an
observation construction. Whether their complete tangent/normal-jet law
selects the four required non-Levi-Civita preimages is still unconstructed.

## Source return

The released material confirms:

- augmented torsion is a full adjoint-valued difference of two connections;
- the curvature packet contains `D_B T`;
- the selected construction admits a nonzero `T=t Phi1` branch; and
- the gauge-rotated Levi-Civita connection occupies the contorsion slot.

It does not print the actual four independent-`varpi`/soldering/observation
normal-jet columns or show that they equal the Koszul preimages above.

```text
SOURCE-CONFIRMS:
  the two-connection translation-curvature arena, nonzero T branch and
  gauge-rotated Levi-Civita role.

SOURCE-SILENT:
  the actual four-column independent-varpi/soldering/observation normal jet.
```

## Specialist and hostile review

- **Differential geometry:** the two-sided inverse is the ordinary Koszul
  inversion of the Cartan torsion map; the Levi-Civita subspace is separately
  constrained by the linearized first structure equation.
- **Representation theory:** the equality of dimensions is not used alone;
  both composites are checked on all basis vectors and the four packet
  preimages are checked coefficientwise.
- **Variational PDE / hyperbolic equations:** the lower-order nonzero-background
  map does not change the `q`-exact principal symbol or close the null screen.
- **Symplectic geometry:** carrier ownership is not an Euler covector,
  presymplectic current, characteristic quotient or BFV class. The first-action
  coefficient remains distinct from the raw residual coefficient.
- **Krein/operator theory:** no positivity, self-adjointness, Green operator or
  common closed domain is inferred from a finite algebraic isomorphism.
- **Source criticism:** source-owned carrier types are recorded as confirmation;
  the missing four coefficients remain source-silent.
- **Repo archaeology:** v0.51 explicitly left lower-order commutators open;
  v0.54 supplied the needed nonzero constituent background. This wave composes
  those results instead of restarting the principal-symbol search.

The summary-overreach charge rejects “Levi-Civita supplies the 117.” The
superseded-object charge rejects another moving-operator or q-wedge search.

## Progress and fences

```text
Ledger v0.55 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 4
  - nonzero-background Cartan/Spencer map constructed exactly
  - unrestricted connection carrier proved rank 1,274 and invertible
  - all transverse 117 coefficients assigned exact rank-four carrier preimages
  - Levi-Civita constrained subclass proved q-exact and disjoint from 117
frontier_conditions_opened: 0
remaining_named_conditions: 3
  - actual independent-varpi/soldering/observation normal jet on four columns
  - null characteristic screen and total raw-Upsilon Bianchi/naturality
  - Euler/preboundary, physical constraint quotient and common domain
```

No verdict, residue, quotient, external datum, canon or public posture moves.
`P1/P2/P3` remain unused. Curt remains formally separate and no third lane is
promoted.

## Next gate

Construct the actual tangent law of the independent full-adjoint `varpi`
connection together with the ambient soldering/observation normal jet on the
same four graph columns. Compare its connection components with the exact
Koszul preimages `57,34,34,34`. If it matches, compose the complete raw
`Upsilon` derivative and test total Bianchi/naturality; if it stays in the
Levi-Civita q-exact subclass, the transverse route requires a separately
source-owned higher jet. Keep the null characteristic screen separate.

The executable probe passes `48/48`, including full two-sided basis checks,
immutable predecessor replays and planted failures against background,
Levi-Civita, Euler, quotient, mode-count and datum inflation.
