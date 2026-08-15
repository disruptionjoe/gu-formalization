---
title: "Selected-K102 I1B partial-Legendre Gauss owner"
status: active_research
doc_type: exact_conditional_nonnull_collar_partial_legendre_and_owner_discriminator
created: "2026-08-15"
registry: lab/process/selected-k102-rsap-i1b-partial-legendre-gauss-owner.json
probe: tests/channel-swings/selected_k102_rsap_i1b_partial_legendre_gauss_owner_probe.py
grade: "CONDITIONAL NONNULL I1B PARTIAL LEGENDRE EXACT; VARPI NORMAL OWNS DIAGONAL GAUSS; B(EPSILON) NORMAL IS A VELOCITY, NOT THE RIGHT-H MULTIPLIER"
target_claim: K101_NEXT_GATE__SOURCE_I1B_RECOVERS_STANDALONE_J_R_H_BAL_ZERO_FROM_PROJECTED_B_EPSILON_NORMAL
target_verdict: NO_AT_LOCAL_FORMAL_I1B_GRADE__ADJACENT_FULL_G_DIAGONAL_GAUSS_OWNER_EXACT
canon_verdict_change: none
---

# Selected-K102 I1B partial-Legendre Gauss owner

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

`GU-COMPARATOR-ROUTING-CLASSIFICATION: SOURCE_NATIVE_ROUTE`

## Result first

On an explicitly conditional non-null collar, the released bosonic `I1B`
grammar does have an exact partial Legendre decomposition. It does **not**
make the normal component of `B(epsilon)` the multiplier sought by the reverse
RSAP scaffold.

The owner typing is instead:

```text
B(epsilon)_n = Ad(epsilon^-1) Gamma_n + epsilon^-1 partial_n epsilon
             = b_n^0 + v.
```

Thus `B(epsilon)_n` contains the right-trivialized epsilon normal velocity
`v`. It is a dependent velocity, not an independently variable normal
connection component. The independent source connection is `varpi`, with

```text
T_n = varpi_n-B(epsilon)_n = varpi_n-b_n^0-v.
```

After the partial Legendre transform, `varpi_n` is linear and imposes the
source's **diagonal full-`G` Gauss law**

```text
G_full = Div_varpi(Pi)-lambda = 0,
```

up to the displayed convention for the invariant pairing and endpoint
orientation. Here `Pi` is the momentum conjugate to tangential `varpi`, while
`lambda` is the epsilon momentum already identified by the action
preboundary calculation as

```text
lambda = i_n(E_B-E_T).
```

Conditional projection by `R_0` gives

```text
G_h = partial_i e^i+[a_i,e^i]+[phi_i,pi^i]-lambda_h = 0.
```

The mandatory `[phi,pi]` term from K101 is present. Crucially, this equation
sets `lambda_h` equal to bulk covariant flux; it does not set
`lambda_h=J_R,H_bal` to zero. The desired K99 multiplier term is therefore not
hidden in `I1B`. The source owns an adjacent, standard gauge-theoretic role—
diagonal bulk-plus-epsilon gauge invariance—but not the reverse scaffold's
standalone right-`H_bal` cotangent reduction.

## Layer 0: the normals and owners that must not be merged

| phrase | object here | kept distinct from |
|---|---|---|
| collar normal `n` | one conditionally chosen non-null conormal to a codimension-one boundary in `Y14` | the ten-dimensional normal bundle of the observation section `X4 -> Y14` |
| `B(epsilon)_n` | dependent gauge-rotated reference connection containing epsilon velocity | independent multiplier |
| `varpi_n` | normal component of the independently varied source connection | the distortion `T_n` by itself |
| epsilon momentum `lambda` | coefficient of `epsilon^-1 delta epsilon` on the collar | an independently imposed zero moment level |
| diagonal Gauss law | `Div(Pi)-lambda=0` from simultaneous source gauge symmetry | right-`H_bal` constraint `lambda_h=0` |
| conditional `H_bal` projection | use of external balanced `R_0` | source selection of `H_bal` as the gauge group |

The earlier exact ten-normal action bank concerns observation-section normal
directions. It cannot be silently retyped as this codimension-one canonical
collar. What composes here is its general preboundary formula
`i_n(E_B-E_T)`, not the ten-row observation-normal count.

## Source-native transgression normal form

Let `A=varpi=B+T`. In the repository's exact `q(T,T)` convention,

```text
F_A=F_B+D_B T+q(T,T)
```

and the written source combination becomes

```text
C(B,T)
 = F_B+(1/2)D_B T+(1/3)q(T,T)
 = (1/2)(F_A+F_B)-(1/6)q(T,T).
```

This already-certified identity is the efficient primitive-coordinate form.
For `B(epsilon)=epsilon^-1 Gamma epsilon+epsilon^-1 d epsilon`,

```text
F_B=epsilon^-1 F_Gamma epsilon.
```

Consequently `F_B` contains no epsilon derivative after the exact
Maurer--Cartan cancellation. On the displayed zero-order moving-Shiab family,
the epsilon normal velocity enters `I1B` only through `T_n`.

No ordinary Yang--Mills action is substituted here. The derivation uses the
actual one-half/one-third transgression coefficients, arbitrary algebraic
dependence on `T_n`, and the source connection curvature `F_varpi`.

## Universal partial-Legendre identity

Suppress tangential indices and all algebraic fields not relevant to the
chain rule. Any local `I1B` density on the fixed collar has the form

```text
ell = ell(T_n, X_i, other),
T_n = varpi_n-b_n^0-v,
X_i = partial_n varpi_i-D_i varpi_n,
v   = epsilon^-1 partial_n epsilon.
```

Define

```text
K       = partial ell/partial T_n,
Pi^i    = partial ell/partial X_i,
lambda  = partial ell/partial v = -K.
```

There is no `partial_n varpi_n`. The direct `varpi_n` equation is

```text
K-D^!_i Pi^i=0.
```

Writing `Div(Pi)=-D^!_i Pi^i` and using `lambda=-K` gives

```text
Div(Pi)-lambda=0.
```

The same result is visible before solving any Legendre relation. Retain
`T_n,X_i` as auxiliary first-order variables and use

```text
v=varpi_n-b_n^0-T_n,
partial_n varpi_i=X_i+D_i varpi_n.
```

Then the canonical Hamiltonian is affine in `varpi_n`; its coefficient is the
negative of the displayed Gauss expression. No invertibility of the
`T_n -> lambda` map is required. If that map is singular, additional primary
constraints remain, but this owner identity survives.

An exact nonlinear polynomial fixture in the probe has nonzero
`varpi_n` coordinate Hessian, nonzero epsilon-velocity Hessian, no
`partial_n varpi_n`, and nevertheless an affine canonical `varpi_n` term.
This simultaneously preserves K101's diagnostic correction and proves the
new owner statement.

## Balanced projection and why it is not the RSAP zero level

Decompose tangential connection and momentum with K100's conditional seed:

```text
varpi_i=a_i+phi_i,
Pi^i=e^i+pi^i.
```

The symmetric-pair brackets give

```text
P_h Div_varpi(Pi)
 = partial_i e^i+[a_i,e^i]+[phi_i,pi^i].
```

Therefore variation of `a_n=P_h varpi_n` imposes

```text
partial_i e^i+[a_i,e^i]+[phi_i,pi^i]-lambda_h=0.   (I1B)
```

K97/K99 require the different equation

```text
lambda_h=J_R,H_bal=0.                              (RSAP)
```

The first does not imply the second. Exact nonzero fixtures satisfy the I1B
constraint with `lambda_h=Div(Pi)_h != 0`. Setting the bulk flux to zero would
recover the desired level, but that is a new boundary condition or
polarization choice. The selected action's prior Noether/preboundary theorem
instead leaves unrestricted endpoint transformations charged.

This is also why the full-algebra Gauss law was the wrong *replacement* for
the reverse scaffold but remains the correct source-native object: it is an
adjacent constraint with a different moment map and quotient.

## Claim ceiling and source return

The result is exact for the released bosonic `I1B`, its displayed zero-order
moving-Shiab family, a fixed local non-null collar and formal partial Legendre
calculus. It does not select the collar as physical time, construct a global
ultrahyperbolic Hamiltonian domain, prove Legendre regularity, include `I2B`
or fermions, or choose the balanced seed/right gauge declaration.

```text
SOURCE-CONFIRMS:
  epsilon, independent varpi, T=varpi-B(epsilon), I1B transgression grammar.

REPOSITORY-COMPOSES:
  primitive transgression normal form, velocity ownership, partial Legendre
  identity, existing epsilon preboundary momentum and balanced projection.

SOURCE-SILENT:
  preferred collar/time, balanced H reduction, lambda_h zero boundary level,
  global Hamiltonian/BFV domain and physical polarization.
```

No ledger, datum, quotient, canon claim, public posture, W/mirror choice,
chirality or generation count changes.

## Next gate

Do not keep testing `B(epsilon)_n` as a multiplier. It is an epsilon velocity.
Run an exact **boundary-owner and polarization census** for the three ways the
diagonal constraint could be turned into the standalone RSAP zero level:

1. an action-selected zero `h_bal` bulk-flux boundary condition;
2. a boundary edge completion whose combined moment map leaves precisely
   `lambda_h=0`; or
3. K99's explicit new right-`H_bal` multiplier term.

For each, compute the resulting characteristic distribution and dimension,
and reject any route that kills the live charged boundary sector by naming it
gauge. Reproduce this gate with:

```bash
python3 tests/channel-swings/selected_k102_rsap_i1b_partial_legendre_gauss_owner_probe.py
```

> **Successor closure (K103).** The three remaining boundary routes are now
> exactly classified. Zero `h_bal` bulk flux and K99's explicit multiplier
> both give the `98D` quotient by imposing `lambda_h=0`; neither preserves
> generic endpoint charge, and neither is selected by the current action. A
> minimal `H_bal` edge extension preserves that charge but has a `182D`
> quotient, not `98D`. Adding `lambda_h=0` after the edge extension reaches
> `98D` only by reinstating the zero-charge horn. The missing object is a
> source/action-owned physical boundary disposition, not another algebraic
> reduction.
