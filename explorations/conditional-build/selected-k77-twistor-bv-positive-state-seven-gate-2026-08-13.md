---
artifact_type: exact_twistor_bundle_moving_bv_and_physical_ownership_gate
created: 2026-08-13
status: BASE_AND_NORMAL_TWISTOR_KINEMATICS_CONSTRUCTED_SEPARATELY__MOVING_J_LONGITUDINAL_BRST_CLOSES__ACTUAL_F02_PENROSE_PUSHFORWARD_POSITIVE_DOMAIN_AND_PHYSICAL_COHOMOLOGY_OPEN
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
probe: tests/channel-swings/selected_k77_twistor_bv_positive_state_seven_gate_probe.py
---

# Selected K77 twistor, moving-BV and positive-state seven-gate

## Result first

The seven-gate sequence can be started now, but it does not close the physical
superposition question.  It reaches a precise boundary after constructing more
than the repository previously owned.

Two twistor objects construct exactly and remain distinct:

1. the base correspondence for complexified conformally compactified
   spacetime,

   ```text
   M_C = Gr(2,C^4),
   PT = P(C^4) = CP^3,
   F = F(1,2;4),
   F -> M_C with fibre CP^1;
   ```

2. the normal homogeneous twistor fibre

   ```text
   Z_N = O(6,4)/U(3,2),
   dim_R Z_N = 20, dim_C Z_N = 10.
   ```

The first object parametrizes spacetime two-planes and their projective spinor
lines.  The second parametrizes orthogonal complex structures on the normal
ten-plane.  Neither is the spinor Clifford volume `J10`, neither is one of the
two ambient `C^(32,32)` Weyl carriers, and there is no identification between
them in this result.

The moving normal complex structure admits the minimal longitudinal BRST
extension.  In the repository sign convention,

```text
s psi = c psi,
s J   = [c,J],
s c   = c^2.
```

The exact probe verifies `s^2 psi=0`, `s^2 J=0`, and preservation of both
`J^2=-1` and `J^T eta J=eta`.  This constructs the gauge/longitudinal moving-J
sector.  It is not a complete BV master action: antifields, the physical
Koszul--Tate differential and the action-owned primal carrier remain absent.

For a twistor `(0,1)` connection, the universal superconnection square splits
into:

```text
bosonic:      F_A^(0,2),
BRST mixed:   s A^(0,1) + dbar c + [A^(0,1),c],
ghost two:    s c + c^2,
base-normal:  F_base,normal.
```

After replacing the repository ghost by the standard-sign ghost
`g=-c`, the exact controls verify cancellation of the BRST-mixed and
ghost-number-two pieces under the standard gauge law.  They also verify that
commuting flat controls have zero `F^(0,2)` and zero base-normal mixed
curvature, while noncommuting controls make both obstructions nonzero.

The actual GU values of `F_A^(0,2)` and `F_base,normal` cannot yet be computed:
the repository does not own a twistor `(0,1)` connection obtained from the
operative GU connection, nor the incidence/soldering map that would place the
base and normal constructions over one physical correspondence space.

The seven-gate disposition is therefore:

| gate | result now | ceiling |
|---|---|---|
| 1. separate base and normal twistor bundles | **PASS, local/homogeneous algebraic** | no base-normal identification or global GU bundle |
| 2. moving-J BV extension | **PASS for longitudinal BRST** | full BV master action and physical KT differential open |
| 3. compute `Q_tw^2` | **PASS universal decomposition and ghost cancellation** | actual GU `F^(0,2)` and mixed curvature open |
| 4. Penrose pushforward and symbol comparison | **PARTIAL**: observed `Jhat` symbol linearity and null Dirac--twistor--RS factorization already pass | field bundles, weights, transform and equality with the owned operator open |
| 5. Lorentzian real structure and domain | **PARTIAL**: local signature-`(2,2)` twistor real-form model and local flat observed `H^s` domain | positive-energy selection and global closed Green/Calderon/BFV domain open |
| 6. positive physical pairing | **OPEN** | current action pairings are `Jhat`-isometric but are not a positive physical quotient pairing |
| 7. physical cohomology, interactions and decoherence | **OPEN** | no physical cohomology, twistor interaction, environment, rate coefficient or visibility functional |

The exact conclusion is:

> GU now has a constructed twistor/moving-polarization kinematic candidate.
> It does not yet have a twistor realization of its physical field complex or
> a derivation of quantum superposition.

No ledger, registered verdict, residue, quotient, external datum, canon claim
or public posture moves.

## Gate 1: the objects constructed separately

### 1A. Base correspondence

Let `T=C^4`.  The exact automatic geometry is

```text
M_C = Gr(2,T),                    dim_C = 4,
PT  = P(T),                       dim_C = 3,
F   = {(L,S): L subset S subset T}, dim_C = 5.
```

The two projections have fibres

```text
F -> M_C: CP^1,
F -> PT:  CP^2.
```

For the Lorentzian real form, take

```text
Phi = diag(1,1,-1,-1).
```

The explicit two-plane spanned by `e_1+e_3` and `e_2+e_4` is exactly
`Phi`-null and pairs nondegenerately with the plane spanned by `e_1-e_3` and
`e_2-e_4`.  This is a finite local model of a compactified Lorentzian
spacetime point.  It does not select a positive-energy state space or a time
orientation.

At `S in M_C`,

```text
T_S M_C = Hom(S,T/S).
```

The rank-two plane `S`, the rank-two quotient `Q=T/S`, and either rank-64
ambient Weyl carrier are dimensionally and functorially different.  The
previous exact no-map result remains: a purely right-handed replacement of
`Q` by `S` needs additional real/non-holomorphic structure.

### 1B. Normal homogeneous twistor fibre

On `R^(6,4)` the probe pairs the six positive axes in three same-sign
two-planes and the four negative axes in two same-sign two-planes.  The direct
sum of the five standard quarter-turn matrices gives `J_N` with

```text
J_N^2 = -1,
J_N^T eta_(6,4) J_N = eta_(6,4).
```

The complete `45`-generator `so(6,4)` computation gives

```text
rank(A -> [A,J_N]) = 20,
dim ker(A -> [A,J_N]) = 25.
```

The kernel is the expected `u(3,2)` stabilizer.  If

```text
so(6,4) = h + m,
h = {A:[A,J_N]=0},
m = {A:{A,J_N}=0},
```

then the probe verifies `dim_R m=20`, `I_m(A)=J_N A` has `I_m^2=-1`, and
`[m,m] subset h`.  The normal orbit is therefore the expected Hermitian
symmetric twistor-type space at this algebraic grade.

### Layer-0 prohibition

Three objects named `J` must remain separate:

| object | carrier | role |
|---|---|---|
| base twistor point | rank-two `S subset C^4` | spacetime/right-spinor incidence |
| normal `J_N` | vector `R^(6,4)` | point of `O(6,4)/U(3,2)` |
| Clifford `J10` | real spinor `R^128` | normal volume, with reflection-twisted full-carrier lift `Jhat` |

An exact spin lift or associated-bundle map may relate the last two, but it is
not identity and is not constructed here.

## Gate 2: the moving-J BRST sector

For any `eta`-skew generator `A`, set

```text
delta_A J_N = [A,J_N].
```

All 45 exact generators satisfy

```text
delta_A(J_N^2) = 0,
delta_A(J_N^T eta J_N) = 0.
```

Thus the gauge action is tangent to the normal twistor orbit.  With the
repository ghost signs, the odd Leibniz rule gives

```text
s^2 J = [s c,J] - c(sJ) - (sJ)c
      = [c^2,J] - [c^2,J]
      = 0.
```

Likewise `s^2 psi=(sc-c^2)psi=0`.  A planted non-stabilizer generator has
`[A,J_N] != 0`, so freezing `J_N` would erase a genuinely live orbit tangent.

This is the minimal extension demanded by the prior fixed-`J10` failure.  To
call it a complete BV construction would still require:

- the action and antifield terms solving the classical master equation;
- the source-derived KT differential on the actual primal carrier;
- compatibility with the rank-25 selected gauge image and its reducibility;
- the spin lift relating `J_N` to `J10/Jhat`; and
- global bundle transition and domain data.

## Gate 3: what `Q_tw^2` says now

Write the standard-sign ghost as `g=-c` and let

```text
s g = -g^2,
s A^(0,1) = -dbar g - [A^(0,1),g].
```

The ghost-one and ghost-two components of the universal superconnection
curvature vanish identically.  What remains is geometric rather than BRST:

```text
F_A^(0,2) = dbar A^(0,1) + A^(0,1) wedge A^(0,1),
F_base,normal.
```

The finite probe includes both firing controls:

- commuting constant matrices give zero curvature;
- the pair `E_12,E_21` gives a nonzero diagonal commutator.

Therefore the computation is not rigged to close.  It says that BRST
covariance cannot repair a non-integrable twistor connection.  The next input
must be the actual GU connection lifted to a declared twistor correspondence.

## Gate 4: pushforward and symbol comparison

Two exact prior results compose positively:

1. the reflection-twisted `Jhat` commutes with every observed horizontal
   principal symbol and preserves the gamma-trace carrier;
2. the null characteristic image of the isolated RS symbol has the exact
   Dirac--twistor factorization

   ```text
   F(k)=Pi_kerGamma(k tensor c(k)).
   ```

These are necessary compatibility results.  They are not a Penrose
pushforward.  The following are still absent:

```text
E on PT or the correspondence space,
its line weight and cohomology degree,
the relative dbar complex,
the derived pushforward R p_* q^* E,
an isomorphism to the owned Omega0(S)+Omega1(S) complex,
lower-order and interaction terms.
```

The honest gate is therefore `PRINCIPAL_COMPATIBILITY_PASSES__TRANSFORM_OPEN`.

## Gates 5 and 6: real form, domain and pairing

The local `Phi` model supplies the positive/null/negative twistor strata and
an explicit Lorentzian null spacetime plane.  It does not intrinsically label
one stratum as the physical positive-energy sector: before a real structure,
time orientation and boundary prescription are fixed, the labels can be
exchanged.

The repository separately owns a conditional local flat observed `H^s`
Cauchy carrier with a positive common symmetrizer.  It does not own the
variable/global closed Green, Calderon, maximal-dissipative or BFV domain.
The ambient `Y^14` problem remains ultrahyperbolic and must not inherit an
ordinary Lorentzian domain silently.

Current `Jhat` is an isometry of two Spin-natural action pairings, while
`J10` is an anti-isometry of the trace-owned `H_q`.  None of these facts gives
a positive pairing on physical BV cohomology.  Gate 6 therefore remains open,
not failed by contradiction.

## Gate 7: what cannot yet be asked physically

Until gates 3--6 close, the repository cannot compute:

- the physical cohomology groups carrying amplitudes;
- whether the interacting differential preserves their complex structure;
- whether `+J` and `-J` are gauge, conjugate sectors or superselected;
- a Born/GNS/OS physical pairing;
- a reduced open-system generator;
- a coefficient with units for a decoherence rate; or
- a visibility observable for matter-wave comparison.

The strongest surviving hypothesis is therefore narrower than the panel's
full synthesis:

> A moving normal polarization and a base twistor correspondence can coexist
> as separate associated constructions.  If an action-owned GU connection
> lifts with vanishing `(0,2)` and base-normal mixed curvature, and if its
> Penrose pushforward reproduces the physical BV complex on a positive closed
> Lorentzian domain, then the resulting cohomology is a candidate location for
> superposition.

Every `if` in that sentence names a gate rather than a rhetorical hedge.

## Seven-axis read

| axis | construction and grade |
|---|---|
| Layer 0 | base plane/quotient, normal vector `J_N`, spinor `J10`, Weyl halves, action pairings and physical pairing separated exactly |
| L1 algebra | exact `Gr(2,C^4)` dimensions and exact `so(6,4)=u(3,2)+m` computation |
| L2 representation | moving normal orbit exact; spin lift and `2 tensor 16` branching map still open |
| L3 geometry | local Lorentzian real-form and homogeneous normal fibre constructed; global GU correspondence not built |
| L4 dynamics | longitudinal BRST and universal superconnection decomposition exact; action/master equation open |
| L5 observation | local null plane and prior local `H^s` carrier; global observation/domain open |
| L6 physics | principal compatibility only; Penrose field complex and interactions open |
| L7 positivity | conditional local symmetrizer exists; positive physical cohomology pairing absent |

## Fastest next gates

1. **Program-native twistor carrier.** Produce `V_GU` of complex rank four or
   an exact equivariant map from the selected observed spin bundles to the
   tautological `S,Q` sequence.  Complete the owed `2 tensor 16` branching at
   the same time.
2. **Connection lift.** Pull the operative selected GU connection to the
   correspondence, decompose it into `(1,0)+(0,1)`, and compute the actual
   `F^(0,2)` and base-normal mixed curvature.  A nonzero class kills the
   naive holomorphic complex at that background.
3. **Relative Dolbeault/Penrose gate.** Declare the bundles, weights and
   degrees, compute the first derived pushforward, and compare its symbol to
   the owned full `Omega0+Omega1` operator rather than isolated RS.
4. **Positive-state gate.** Only after the transform, build the Lorentzian
   real structure, positive-frequency/OS boundary prescription, physical BV
   quotient and closed domain together.

## Falsification conditions

The route is killed in its current form if any of the following occurs:

- no program-native/equivariant `C^4`, tautological two-plane or incidence map
  can be constructed from the selected GU data;
- the actual lifted connection has unavoidable nonzero `F^(0,2)` or mixed
  curvature not absorbed by a typed enlargement;
- the Penrose pushforward does not reproduce the owned horizontal Weyl/Dirac/
  RS principal complex;
- the required Lorentzian real structure and closed domain destroy the
  complex cohomology; or
- every candidate physical pairing remains indefinite or degenerate after
  the genuine BV quotient.

## Executable receipt

```text
python3 tests/channel-swings/selected_k77_twistor_bv_positive_state_seven_gate_probe.py
```

passes `47/47` exact algebraic, prior-art, Layer-0, bundle, moving-constraint,
BRST, superconnection, mixed-curvature, ownership and planted-control checks.
The existing exact J10/BV probe and the existing twistor-Grassmannian kernel
are independent composed receipts rather than numbers recopied into this
probe.

## References

- M. F. Atiyah, N. J. Hitchin and I. M. Singer, *Self-duality in
  four-dimensional Riemannian geometry*, Proc. Roy. Soc. Lond. A 362 (1978),
  425--461.
- R. Penrose, *The twistor programme*, Reports on Mathematical Physics 12
  (1977), 65--76.
- P. Woit, *Euclidean Twistor Unification*, arXiv:2104.05099, and *Wick
  Rotating Spinors and Twistors* (April 2026 slides).
- `explorations/woit-principles/twistor-grassmannian-kernel-2026-07-24.md`.
- `explorations/conditional-build/selected-k77-j10-bv-green-descent-gate-2026-08-13.md`.
- `explorations/eric-curt-wave3d-b2c2-null-clifford-omega1-completion-2026-07-31.md`.
