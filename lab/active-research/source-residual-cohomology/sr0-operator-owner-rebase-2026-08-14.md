---
title: "SR-0 source-residual operator-owner rebase"
status: active_research
doc_type: exact_composition_and_finite_discriminator
created: "2026-08-14"
lane_id: SRC-RES-COH-01
swing_id: SR-0
source_claims: [SC-ACT-01, SC-ACT-04, SC-ACT-05]
ledger_rows: [LT-SM8]
probe: tests/channel-swings/source_residual_cohomology_sr0_operator_owner_probe.py
claim_grade: "EXACT VARIATIONAL IDENTITY AND EXACT FINITE CONTROLS; GU PHYSICAL INTERPRETATION OPEN"
canon_verdict_change: none
---

# SR-0 source-residual operator-owner rebase

## Result first

The superposition/cohomology work should no longer use ordinary source-free
Yang--Mills as its primitive dynamical owner.

The source-faithful hierarchy is:

```text
Upsilon(omega)                         first-order total residual
I2(omega)=(1/2)<Upsilon,Q_B Upsilon>  second action
E2(omega)=(D Upsilon)^! Q_B Upsilon  second Euler covector
```

Ordinary Yang--Mills instead has

```text
I_YM(A)=(1/2)<F_A,F_A>,
E_YM(A)=(D F_A)^! F_A = D_A^*F_A.
```

They coincide only if an additional typed factorization identifies their
fields, pairings, residual maps and lower-order terms. No such identification
has been constructed. The exact K77 theorem that
`II=0 iff D_A^*F_A=0` fails both ways therefore survives as a comparator, but
it does not test the source's `E2=0` equation.

This materially rebases H1:

> The source residual/deformation complex is the primitive candidate. The
> moving reduction, ordinary Yang--Mills detour and local-twistor complex are
> downstream adapters whose compositions must be proved.

## Exact calculus

Let `Phi` denote all fields varied by the second action, let

```text
Upsilon : Phi -> E,
Q_B : E -> E^*,
```

and hold `Q_B` fixed for this identity. Then

```text
d I2 = (D Upsilon)^! Q_B Upsilon.
```

At a background `Phi_*`, the complete Hessian is

```text
H_I2
 = (D Upsilon)^! Q_B (D Upsilon)
   + <Q_B Upsilon, D^2 Upsilon>.
```

The second term vanishes on a genuine residual-zero shell
`Upsilon(Phi_*)=0`; it need not vanish at a nonzero null residual. This is
already material in the selected K77 calculation: the lower-order Hessian
receives a load-bearing contribution from a nonzero Krein-null residual.

Consequently, the proposed Dirac-square/factorization comparison must be run
on an action-owned `Upsilon=0` stationary background or must retain the full
residual-dependent Hessian term.

## Exact finite discriminator

The executable positive/negative control uses exact integer arithmetic on a
two-field residual with a nontrivial Shiab surrogate:

```text
F(x,y)       = (x,y),
S            = diag(2,1),
T            = (-2,0),
Upsilon      = S F + T = (2x-2,y).
```

With Euclidean test pairings only for this finite discriminator,

```text
E_YM = (x,y),
E2   = (4x-4,y).
```

Therefore:

```text
at (0,0): E_YM=0 while E2!=0;
at (1,0): E2=0 while E_YM!=0.
```

The implication fails both ways even before the source's eddy,
field-dependent Shiab, moving metric, fermion residual and indefinite pairing
are added. This finite control proves operator nonidentity, not a theorem
about the full GU solution set.

The same probe checks the Hessian identity on

```text
Upsilon(x,y)=(x^2-x+y-1, x-y).
```

At the exact residual-zero point `(1,1)`, the residual-dependent Hessian term
vanishes. At `(0,0)` it is nonzero and changes the full Hessian. This guards
against replacing the second variation everywhere by the Gauss--Newton term
`(D Upsilon)^! Q_B D Upsilon`.

## Composition with existing repo mathematics

| object | existing exact/source grade | SR-0 disposition |
|---|---|---|
| source-natural fixed-grade `I2B` owner | source-confirmed plus exact pairing classification | primitive second action at its certified scope |
| selected K77 `I2B` Hessian and nonlinear prolongations | exact frozen/local results | retained; not recomputed |
| total adapted `D_A^*F_A` block decomposition | exact local differential geometry | ordinary-YM comparator only |
| local-twistor Bach/Yang--Mills detour | exact/standard transfer at declared scope | downstream complex requiring an intertwiner |
| `D_A R=2 mixed(A)` and reduction current | exact | candidate coupled field map, not source action ownership by itself |
| source deformation-complex sketch | author-stated | construction prompt; no positive physical cohomology follows |

## What SR-0 closes

- using `D_A^*F_A=0` as though it were Weinstein's printed second equation;
- treating the ordinary twistor detour as the source residual complex without
  an adapter;
- dropping the residual-dependent Hessian term away from `Upsilon=0`; and
- taking pointwise `J`, `II=0` or complex planes as the action owner of
  superposition.

## What remains open

- a full action-owned stationary `Upsilon=0` background;
- the total boson/fermion field space, real structure and pairing;
- `L_Upsilon K=0` and its complete reducibility on that background;
- the Dirac--Rarita--Schwinger factorization/intertwiner;
- the off-diagonal mass/VEV block and its curvature dependence;
- endpoint/BFV admission, Lorentzian domain, positivity and physical
  cohomology; and
- any relation to quantum superposition or experiment.

## Next swing

`SR-1` will reuse the source gauge map and existing Ward/BV packets, but it
must evaluate the linearized **total residual** on one action-owned stationary
background. The gate is:

```text
K : gauge parameters -> field variations,
L_Upsilon = D Upsilon|_{Phi_*},
L_Upsilon K = 0,
Upsilon(Phi_*) = 0.
```

If no such background is owned, SR-1 returns `BACKGROUND-MISSING`; it does not
manufacture one by restricting the tangent.

