---
title: "WOIT-OS-PHYSICAL-REAL-FORM-GATE: reflection is a real constructor, but a time direction is not GU's missing bit"
status: active_research
doc_type: exploration
created: "2026-07-24"
grade: "standard OS/Spin(4)/Hodge principles plus exact finite controls; no GU reflection-positivity or physical-sector theorem"
---

# WOIT-OS-PHYSICAL-REAL-FORM-GATE

## Decision

Woit's Osterwalder-Schrader proposal is directly relevant to GU's
`192 -> 384` physical-real-form problem because it says that a chiral
Euclidean theory need not be converted to Lorentzian physics by a naive
complex-conjugation closure. The physical state space may instead be
reconstructed using an antilinear reflection `Theta`.

But the exact controls reject three shortcuts:

1. A nonzero Euclidean direction gives an isomorphism
   `c(n):S+ -> S-`, but no fixed nonzero `Spin(4)`-equivariant map
   `S+ -> S-` exists.
2. `n` and `-n` lie in the same `SO(4)` orbit. A selected direction does not
   leave an automatic `Z/2` after rotational quotient.
3. Ordinary Lorentzian conjugation exchanges the `+i` and `-i` Hodge halves.
   Multiplying by `gamma(n)` does not by itself prove that one `192`-dimensional
   GU half is a closed physical carrier.

The Woit principle therefore supplies a **constructor specification**, not the
missing bit or the finished real form.

## Woit's proposal

In [Spacetime is Right-handed](https://arxiv.org/abs/2311.00608), Woit argues
that:

- Euclidean physical-state reconstruction requires a distinguished imaginary
  time direction and an Osterwalder-Schrader reflection;
- Clifford multiplication by the distinguished direction identifies the two
  Euclidean chiral spinor representations;
- one can describe the reconstructed spacetime degrees of freedom using two
  right-handed spinors, while the other `SU(2)` behaves as an internal
  symmetry.

His July 2026
[Notes on Wick Rotation and Chiral Field Theories](https://www.math.columbia.edu/~woit/twistorunification/chiralwick-sketch.pdf)
make the key conceptual move sharper: begin with a Euclidean holomorphic
chiral theory and recover a Minkowski theory through an appropriate
conjugation/reflection, rather than first doubling the holomorphic theory by
complexification.

The focused Theories of Everything interview is unusually helpful here. From
roughly `01:16:39` through `01:19:21`, Woit explains that the selected imaginary
time direction supplies a distinguished `gamma_0`, that `gamma_0` interchanges
left and right Euclidean spinors, and that this motivates the “spacetime is
right-handed” slogan. See the
[automated transcript](https://podscripts.co/podcasts/theories-of-everything-with-curt-jaimungal/peter-woit-a-new-path-to-unification-the-forgotten-geometry).
The transcript's terminology is noisy; the paper is authoritative.

## Standard OS construction

Fix a unit Euclidean vector `n` and the reflection

```text
r_n(x) = x - 2 <n,x> n.
```

Let `A_+` be observables supported in the half-space `<n,x> > 0`. For a scalar
schematic field,

```text
(Theta F)(phi) = conjugate(F(r_n phi)).
```

Fermions require the appropriate spin/reflection matrix. Given a Euclidean
Schwinger functional `E`, define

```text
(F,G)_OS = E[(Theta F) G],  F,G in A_+.
```

The physical Hilbert space exists only after proving reflection positivity:

```text
(F,F)_OS >= 0.
```

One then quotients the null space and completes:

```text
H_phys = completion(A_+ / {F : (F,F)_OS=0}).
```

Choosing `n`, `r_n`, and an antilinear formula is not enough. The action or
Schwinger functions, support algebra, positivity theorem, null quotient, and
Lorentzian group reconstruction are load-bearing.

## Exact finite controls

The checks live in
`tests/woit-principles/test_os_real_form_kernel.py`.

### 1. A direction gives a covariant chiral isomorphism

Write a Euclidean vector `n=(a,b,c,d)` as the quaternion matrix

```text
C(n) =
  [ a+ib    c+id ]
  [ -c+id   a-ib ].
```

Then exactly

```text
C(n)^dag C(n) = |n|^2 I,
det C(n) = |n|^2.
```

For the planted vector `(1,2,3,4)`, both sides equal `30`. Thus nonzero `n`
does give the isomorphism Woit describes.

### 2. The isomorphism cannot be fixed before selecting `n`

Under

```text
Spin(4) = SU(2)_L x SU(2)_R,
S+ = (2,1),
S- = (1,2).
```

A fixed intertwiner `A:S+ -> S-` must intertwine a left generator that acts
nontrivially on `S+` and trivially on `S-`. Hence

```text
A sigma_1 = 0.
```

The coefficient system has exact rank `4/4`, so `A=0`. The family `C(n)` is
covariant as `n` moves; it is not a symmetry-preserving identification at a
fixed background.

### 3. A direction does not supply a sign bit

For `n=e_0`,

```text
R = diag(-1,-1,1,1)
```

has determinant `+1`, lies in `SO(4)`, and sends `n` to `-n`. More generally a
rotation by `pi` in a two-plane containing `n` does the same. Thus the unit
direction space

```text
S^3 = SO(4)/SO(3)
```

is one connected orbit. There is no residual two-point choice `n=+/-`.

By contrast the OS hyperplane reflection

```text
r_n = diag(-1,1,1,1)
```

has determinant `-1`. Its component in `O(4)/SO(4)` is discrete, but it is
part of the added reflection/support structure. It is not derived merely by
choosing a direction.

### 4. Lorentzian Hodge halves are conjugate partners

On Lorentzian two-forms,

```text
*^2 = -1.
```

In the basis `(01,02,03 | 23,31,12)`, the exact real matrix can be written

```text
J(E,B) = (B,-E).
```

The projectors

```text
P_+ = (1-iJ)/2,
P_- = (1+iJ)/2
```

have complex rank three, and

```text
conjugate(P_+) = P_-.
```

This is the finite prototype of the repo's existing physical-signature
correction: one Lorentzian Hodge half is not closed under ordinary physical
conjugation.

## Construction fork for GU

| issue | standard OS control | GU-native question |
|---|---|---|
| starting space | Euclidean field algebra and Schwinger functional | which committed GU Euclidean/observer field space? |
| reflection | `r_n` plus spin action | how does reflection act on the 14d carrier, deck involution, and internal factor? |
| conjugation | antilinear involution `Theta` | does `Theta` preserve a candidate carrier or exchange the `192` halves? |
| inner product | reflection-positive semidefinite OS form | GU starts with a DeWitt/Krein structure; where is the positive physical quotient? |
| null space | quotient determined by Schwinger functions | which GU null modes are gauge, ghost, Hodge-null, or physical? |
| Lorentzian reconstruction | theorem after OS axioms | no source-owned reconstruction theorem yet |
| discrete data | chosen `O(4)` reflection/support orientation | no constructed functor to GU's deck/orientation/anomaly line |

The standard OS theorem reconstructs a positive Hilbert space. A
“Krein-OS” slogan is not the same theorem. GU must either:

- construct a standard reflection-positive Euclidean functional and obtain a
  positive Hilbert quotient; or
- state and prove a different indefinite reconstruction theorem, including
  the role of a fundamental symmetry and its physical quotient.

## Implication for `192 -> 384`

The existing GU authority says:

- one Lorentzian Hodge half has complex dimension `192`;
- it is `K`-null;
- ordinary physical conjugation exchanges it with the other half; and
- the conjugation-stable complex closure is `384` with signature `(192,192)`.

An OS-style `Theta` could change the correct notion of reality because it
combines conjugation with reflection and spin action. It is therefore a
legitimate route to test. Nothing in the finite Woit mechanism determines the
answer, however.

In particular:

- `C(n)` is an isomorphism between the two chiral modules, not a proof that one
  disappears;
- a fixed locus of an antilinear map has a **real** dimension, so it cannot be
  compared to the repo's complex `192/384` counts without an explicit
  scalar-field convention;
- OS null quotient dimensions are dynamical/functional, not determined by
  finite representation rank;
- no `Z/2` remains from `n` versus `-n` under `SO(4)`.

## `GU-OS-THETA-CONSTRUCTOR` packet

A serious next attempt must freeze:

1. `E_GU`: the Euclidean GU field/carrier space and scalar field.
2. `A_+(n)`: the positive-time observable/support algebra.
3. `r_n`: the reflection on base/observer geometry.
4. `U(r_n)`: the lift on all spin, internal, ghost, and deck data.
5. `Theta = U(r_n) o conjugation`: with exact square and grading law.
6. `S_E` or Schwinger functional: source-owned, not a surrogate.
7. The form `(F,G)_Theta` and its positivity/indefinite classification.
8. The null quotient and completed physical state space.
9. The Lorentzian carrier map and its real/complex dimension.
10. The action on `K`, chirality, `Spin(10)`, deck data, and any anomaly line.

Predeclared outcomes:

- `OS-CLOSES-ONE-CARRIER`: the full packet proves a closed physical carrier
  with the desired spectrum.
- `OS-REQUIRES-CLOSURE`: `Theta` still exchanges the halves or the quotient
  retains both.
- `OS-POSITIVITY-FAIL`: the candidate form is not positive on the declared
  physical algebra.
- `OS-UNDERDEFINED`: source action/support/reflection data are missing.
- `OS-EXTERNAL-COMPONENT`: a discrete reflection component is required but not
  derived from GU.

## Scope and grade

- Clifford, intertwiner, orbit, determinant-component, and Hodge statements:
  standard representation/topology results with exact finite witnesses.
- OS reconstruction: standard theorem stated with its hypotheses, not executed
  for GU.
- GU consequences: exploration-grade gate design.
- No claim that Woit's proposal supplies GU's missing bit or solves the
  `192/384` fork.
