---
title: "Positive pairings and unstable waves in the observed two field model"
status: active_research
claim_verdict: conditional_theorem
doc_type: exact_static_symmetrizer_theorem_and_wave_energy_test
created: 2026-10-07
target_claim: NONE-NOT-A-KILL
bears_on: SC-META-53
claim_ceiling: "Whole-line theorem for the explicitly declared observed two-field wave equation; no native I1B bridge or GU quantum verdict"
probe: tests/channel-swings/nguyen_static_pairing_energy_probe.py
manifest: lab/process/nguyen-static-pairing-and-energy.json
---

# Positive pairings and unstable waves in the observed two field model

The literal moving-background model studied in K117 admits more positive
spatial pairings than its instantaneous spectral grading suggests. All
Hermitian multiplication pairings can be classified exactly. Some nonconstant
backgrounds admit a positive pairing that makes the spatial operator
self-adjoint, including backgrounds crossing the old spectral wall.
Nevertheless, among smooth bounded backgrounds on the whole spatial line,
only a positive constant background has nonnegative wave energy within this
class. An explicit nonconstant profile has two exact exponentially growing
modes.

This addresses one proposed response to Nguyen §3.1: supplying a positive
pairing is not enough to establish stable physical dynamics. It does not
refute GU, identify GU's physical state space, or supersede K117. The native
I1B action, the observed scalar model, and a quantization of either remain
distinct. SC-META-53 stays UNCERTAIN.

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> operator and energy calculation on the observed two-field model. It supplies
> no particle-physics comparator or bridge to native GU dynamics. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: complete local multiplication symmetrizer classification and bounded-profile wave-energy theorem
carrier: two complex scalar components on the spatial real line with wave Cauchy data LAYER=toy CHIRALITY=N/A
pairing: positive spatial Hermitian multiplication form W distinguished from the wave energy and any physical probability pairing ON=observed_two_field_model
real_structure: real coefficient wave operator complexified for spectral analysis
grading: two scalar channels after an explicit bounded similarity and a constant orthogonal rotation
action_owner: repository-construction -- literal observed K117 quadratic with a stated Lorentzian sign; no identification with I1B
target: stationary local positive pairing as a proposed quantum-consistency repair MAP-TYPE=not-a-map
```

## The equation and its scope

Let `b>0`, let `r=r(x)` be a prescribed smooth real static background, and set

```text
K(r) = [[r,1],[1,0]],                 M = diag(0,b),
B = K^-1 K' = [[0,0],[r',0]],
U = -K^-1 M = [[0,-b],[0,br]],
D = -I d_x^2 - B d_x + U,
u_tt + D u = 0.                                             (1)
```

The quadratic action convention is

```text
I[u;r] = (1/2) integral [u_t^T K u_t - u_x^T K u_x + u^T M u] dt dx.
```

Thus `K u_tt-(K u_x)'-M u=0`. This is the favorable wave sign: at constant
`r>0`, the two squared frequencies are `q^2` and `q^2+br`. Changing the
overall action sign changes no equation; changing the relative mass sign
would be a different equation. The spatial transpose formula extends to
complex fields by Hermitian adjoint.

The coefficient matrices come from
[K117](selected-k117-rsap-tt-symbol-order-custody-and-moving-hessian-gate-2026-08-15.md).
The background is not asserted to solve a native GU equation. The profile
condition derived below is a symmetrizer condition, not an independently
derived equation of motion for `r`.
[K118](selected-k118-rsap-tt-full-moving-d3-owner-sufficiency-and-action-layer-gate-2026-08-15.md)
still separates this observed model from I1B, I2B and the observer extrinsic
functional. No coefficients are transferred among them here.

Initially all formal identities are on compactly supported smooth fields.
The whole-line result assumes bounded smooth `r` and uses the closed domain
constructed below. It imposes no spectral projection, gauge removal,
additional constraint or reflecting boundary.

## All Hermitian multiplication pairings

For a time-independent Hermitian matrix function `W(x)`, formal symmetry of
`D` in `integral u^dagger W v dx` means `WD=D^dagger W`. Equating derivative
coefficients gives

```text
2W' = B^T W + W B,
WU-U^T W + W''-(B^T W)' = 0.                              (2)
```

Write `W=[[X,Y+iZ],[Y-iZ,V]]` with real entries. The first equation gives

```text
X'=r'Y,       Y'=r'V/2,       Z'=0,       V'=0.
```

Consequently its complete solution, without assuming monotonicity of `r`, is

```text
W = [[a+d r+e r^2/4, d+e r/2+i f],
     [d+e r/2-i f,  e]],                                (3)
```

where `a,d,e,f` are constants. The `(2,2)` coefficient in the second equation
of (2) is `2 i b f`. Hence `f=0`. Its remaining independent coefficient is

```text
-ab + be r^2/4 - e r''/2 = 0.                            (4)
```

Positivity requires `e>0` and `ae-d^2>0`. Set `e=s`, `a/e=c^2`,
`d/e=beta`. The exact classification is therefore

```text
W = s [[c^2+beta r+r^2/4, beta+r/2],
       [beta+r/2,       1]],
s>0, c>0, |beta|<c,
r'' = (b/2)(r^2-4c^2).                                  (5)
```

These conditions are necessary and sufficient for a positive Hermitian
multiplication symmetrizer. They include the constant profiles. At `r=0`
as an identically constant profile, the condition would force `c=0`, so no
positive member exists.

K117 tested preservation of its particular instantaneous spectral grading.
Equation (2) tests the complete differential operator: derivatives of the
weight can compensate its lower-order adjoint defect. The broader result in
(5) does not contradict K117's narrower transport mismatch.

## An exact pair of scalar operators

Whenever a positive pairing exists, choose the allowed representative
`s=1`, `beta=0`. Factor it by

```text
F = [[c,0],[r/2,1]],             W=F^T F.
```

Using (5), conjugation yields

```text
F D F^-1 = -I d_x^2 + [[br/2,-bc],[-bc,br/2]].           (6)
```

A constant orthogonal rotation with columns `(1,1)/sqrt(2)` and
`(1,-1)/sqrt(2)` separates the operator into

```text
D_minus = -d_x^2 + b(r/2-c),
D_plus  = -d_x^2 + b(r/2+c).                             (7)
```

In these same channel coordinates, every pairing in (5) becomes the
constant weight `s diag(1+beta/c,1-beta/c)`. Both factors are positive.
Thus the sign of each channel's quadratic form is unchanged by choosing a
different allowed `s` or `beta`; the representative loses no energy repair.

There is no fitted potential or discarded derivative in this transformation.
For bounded `r`, the first integral

```text
(r')^2/2 - b r^3/6 + 2bc^2 r = constant                 (8)
```

also bounds `r'`, while (5) bounds `r''`. Thus `F,F^-1` and their required
derivatives are bounded. The real bounded potentials in (7) give self-adjoint
Schrodinger operators on `H^2(R)`; pulling back this domain supplies a closed
realization of (1) in the weighted spatial Hilbert space. This is more than a
pointwise positive matrix, but is still not a positive norm on wave Cauchy
data.

## Stable energy on bounded backgrounds

**Theorem.** For the class in (1) and (5) with bounded smooth `r` on `R`,
`D` is nonnegative exactly when `r` is the constant `2c`.

First, `r` cannot exceed `2c` anywhere. On any connected interval where
`r>2c`, equation (5) gives strict convexity. A bounded interval with endpoint
values `2c` cannot contain such a convex graph. A half-infinite interval
would cross its finite endpoint with a derivative pointing into the upper
region and then increase in slope, contradicting boundedness. If the interval
is the entire line, bounded strict convexity is likewise impossible.

Therefore `V_minus=b(r/2-c)<=0` everywhere. Unless `r=2c` identically, it is
strictly negative on some finite interval `I`, with
`delta=-integral_I V_minus dx>0`. Take a real trial function equal to one on
`I` and taper linearly to zero over lengths `L` on either side. Its kinetic
form is `2/L`; its potential form is at most `-delta`. Choosing
`L>2/delta` makes its quadratic form negative. Smooth compactly supported
approximations retain the strict inequality. Thus `D_minus` cannot be
nonnegative. Conversely, `r=2c` gives potentials `0` and `2bc`, both
nonnegative. This proves the theorem without a finite spectral truncation.

The conserved wave energy for the symmetrized realization is

```text
E_W = (1/2)||u_t||_W^2 + (1/2)<u,D u>_W.               (9)
```

A negative quadratic direction makes (9) unbounded below by amplitude
scaling. It is not repaired by positivity of `W`. At the positive constant
background, (9) is nonnegative; the massless channel has no uniform positive
spectral gap. Neither outcome is a claim about a GU Fock space or the
Hamiltonian obtained by canonically quantizing the original indefinite
action.

## Two explicit growing modes

Let `k^2=bc/2` and choose

```text
r(x)=2c-6c sech^2(kx).                                  (10)
```

This smooth bounded nonconstant profile satisfies (5) exactly. The pairing
`W` remains uniformly positive even when `r` crosses zero: for the chosen
representative, `det W=c^2` and `tr W<=5c^2+1`. The scalar potentials are

```text
V_minus=-6k^2 sech^2(kx),
V_plus =4k^2-6k^2 sech^2(kx).
```

Direct differentiation gives two square-integrable eigenfunctions of
`D_minus`:

```text
sech^2(kx)           has eigenvalue -4k^2,
sinh(kx) sech^2(kx)  has eigenvalue -k^2.                (11)
```

Both functions and their derivatives decay exponentially, so they belong to
the stated operator domain. Pullback through `F` and the constant rotation
gives actual modes of the two-field equation, with time dependence
`exp(2kt)` and `exp(kt)`. These are exact expressions, not numerical
eigenvalues or finite-difference evidence.

For any growing mode of rate `gamma>0`, the phase-space generator restricts to
`A=[[0,1],[gamma^2,0]]`. If a positive stationary Hermitian phase pairing `G`
were conserved, `A^dagger G+GA=0` would imply
`2gamma v^dagger Gv=0` on the eigenvector `Av=gamma v`, which is impossible.
Thus the positive spatial weight is expressly not a positive conserved
physical wave norm covering these modes.

## What the result changes in the Nguyen investigation

The local positive-pairing route has now been tested beyond the particular
K117 spectral grading. It succeeds at spatial self-adjointness for the exact
profiles (5), but fails to give nonnegative whole-line wave energy for every
bounded nonconstant profile in that class. The constant stable control
survives. This narrows one proposed repair; it neither establishes nor
refutes the source's proposed maximal-compact shielding in SC-META-53.

A source-derived constraint could still exclude unstable states, but it must
be derived and propagated by the same equations. A boundary law, extra
interaction, different background class, or nonlocal/time-dependent pairing
would change the tested hypotheses and needs a new calculation. The whole-line
result must not be exported to the ambient ultrahyperbolic `Y14` problem.

The native constraint route remains separately governed by
[K1145](k1145-i1b-dynamical-cohomology-admission-compiler-2026-10-05.md).
Its nonnegative-Hessian test is a declared restriction criterion, not by
itself a proof that every negative off-shell Lorentzian action direction is
a negative-probability physical state.

The recent literature and exact transfer requirements are recorded in
[the primary-source intake](../../lab/sources/quantum-positivity-primary-pack-2026-10-07.md).
Off-shell infrared finiteness and preservation of a different scalar action's
coupling relation do not remove the eigenmodes in (11).

## Reproduction and verification boundary

```bash
uv run --no-project --with sympy==1.14.0 python -B tests/channel-swings/nguyen_static_pairing_energy_probe.py
```

The certificate checks the complete Hermitian transport equations, the
remaining adjoint equation, positivity determinants, exact channel reduction,
first integral, both growing modes and the phase-metric obstruction. It also
rejects an arbitrary moving profile. The bounded-profile and quadratic-form
arguments above are analytic proofs; the script does not claim to enumerate
the continuum or certify full GU. No source claim, canon result, or protected
physics verdict is promoted.

The derivation and scope were independently reviewed after construction;
the reviewer also reproduced the symbolic checks with SymPy 1.14.0.
This review does not promote the result to canon or supply a native action
bridge. The receipt records both the focused checks and pre-existing
repository audit failures.
