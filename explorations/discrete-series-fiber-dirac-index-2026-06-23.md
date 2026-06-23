---
title: "Discrete-Series / Fiber Dirac Index Test"
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
verdict: "ORDINARY_FINITE_L2_KERNEL_CONDITION_NOT_COHERENT"
depends_on:
  - "DERIVATION-PROGRESS.md"
  - "NEXT-STEPS.md"
  - "explorations/generation-count-cl95-dirac-derham-2026-06-22.md"
  - "explorations/generation-count-sm-branching-closure-2026-06-22.md"
  - "explorations/n5-ind-h-analytic-conditions-2026-06-22.md"
  - "explorations/n6-w2-y14-gysin-spin-structure-2026-06-22.md"
---

# Discrete-Series / Fiber Dirac Index Test

**Purpose.** Test the sharpened N5 analytic condition:

> Does the Dirac operator on GL(4,R)/O(3,1), with vertical spinor module S(6,4),
> have `dim_H ker D_fib = 24`?

**Verdict.** As an ordinary finite-dimensional `L2` kernel statement, the condition is
not coherent. If `D_fib` is the homogeneous fiber operator on

```
F = GL(4,R)/O(3,1),
```

then a nonzero `L2` kernel is a unitary representation of `GL(4,R)` under left
translation. Such a kernel cannot have ordinary finite dimension 24. The
Atiyah-Schmid/Parthasarathy discrete-series route also does not apply directly:
their standard construction is for `G/K` with compact isotropy `K`, while this fiber is
`G/H` with noncompact isotropy `H = O(3,1)`. The correct replacement is a relative
discrete-series problem for a reductive symmetric space, and the basic equal-rank test
is unfavorable for `GL(4,R)/O(3,1)`.

This does **not** refute the verified SM branching result. It says the remaining
analytic condition cannot be "finite quaternionic dimension of the fiber `L2` kernel
equals 24" without adding a different index target: compactification/APS data, a
lattice quotient, or an explicitly defined equivariant multiplicity/formal index.

---

## 1. Setup Fixed From Prior Notes

The relevant fiber over `x in X^4` is the space of Lorentzian metrics on `T_x X`:

```
F = GL(4,R)/O(3,1).
```

Its actual dimension is

```
dim GL(4,R) - dim O(3,1) = 16 - 6 = 10.
```

The compact retract is

```
O(4)/(O(3) x O(1)) = S^3/{+/-1} = RP^3.
```

So `F` has homotopy type `RP^3`, but it is not literally `RP^3`; it is a
noncompact 10-manifold. Any index computation sensitive to `L2` analysis must use the
noncompact 10-dimensional homogeneous space, not only the compact retract.

The vertical metric has signature `(6,4)`. The local spinor content used in the
generation-count notes is the complex half-spinor convention

```
S(6,4) = C^16,
```

which branches under the maximal compact subgroup

```
Spin(6) x Spin(4) ~= SU(4) x SU(2)_L x SU(2)_R
```

as

```
(4,2,1) + (4bar,1,2).
```

That branching result remains the positive representation-theory input: one
Pati-Salam / SM generation per vertical spinor block.

Two cautions are needed before turning this into an index claim.

First, `S(6,4) = C^16` is a complex half-spinor convention, not an intrinsic
quaternionic module. Therefore `dim_H ker D_fib` is not defined from the vertical
module alone. A quaternionic count can only be inherited from the full 14-dimensional
spinor module `S(9,5) = H^64` and the full `H`-linear GU operator.

Second, the fiber metric is pseudo-Riemannian and the isotropy group `O(3,1)` is
noncompact. The coefficient representation obtained from spinors is not automatically
a finite-dimensional unitary representation of `O(3,1)` with a positive invariant
Hermitian metric. The standard Fredholm theory for an elliptic Dirac operator therefore
requires a positive-definite analytic model or a specified equivariant
representation-theoretic model. Without that choice, "the `L2` kernel of the fiber
Dirac operator" is not yet a complete analytic object.

---

## 2. Finite Kernel Obstruction

Assume nevertheless that a homogeneous fiber Dirac operator and a `G`-invariant Hilbert
`L2` model have been defined:

```
D_fib : L2(F, G x_H S(6,4)) -> L2(F, G x_H S(6,4)),
G = GL(4,R), H = O(3,1).
```

The operator is `G`-equivariant under left translation. Hence

```
ker_L2(D_fib)
```

is a closed unitary representation of `G`.

If this kernel had ordinary finite dimension 24 over the quaternions (or any nonzero
finite dimension over `R`, `C`, or the quaternions), then `G` would act through a
finite-dimensional unitary representation. On the connected semisimple derived part
`SL(4,R)`, every finite-dimensional unitary representation is trivial. Thus a
finite-dimensional kernel would have to be trivial on `SL(4,R)`.

That does not give a generation-count space:

1. A trivial finite-dimensional subrepresentation would be represented by invariant
   sections.
2. Invariant sections are constant along the noncompact homogeneous space in the
   relevant homogeneous trivialization.
3. `GL(4,R)/O(3,1)` has infinite invariant volume in the noncompact directions, so
   nonzero constant sections are not `L2`.

Therefore the ordinary `L2` kernel is not expected to be a nonzero finite-dimensional
space. The natural alternatives are:

- `ker_L2(D_fib) = 0`,
- an infinite-dimensional discrete component of `L2(G/H, S)`,
- continuous spectrum with no Fredholm kernel,
- a finite-dimensional kernel only after compactification, boundary conditions, or a
  quotient by a lattice.

So the literal condition

```
dim_H ker_L2(D_fib) = 24
```

fails as a coherent homogeneous-fiber statement.

---

## 3. Why Atiyah-Schmid Does Not Directly Apply

The prior notes phrase the remaining condition as "S(6,4) is in the discrete series of
GL(4,R)." That is not the correct object.

Atiyah-Schmid and Parthasarathy construct group discrete series using Dirac operators
on

```
G/K
```

where `K` is maximal compact. In the present fiber,

```
H = O(3,1)
```

is noncompact. The space is a reductive symmetric space `G/H`, not the Riemannian
symmetric space `G/K`.

There is also a group-level obstruction. Harish-Chandra's ordinary discrete-series
criterion requires a compact Cartan subgroup, equivalently equal rank for the
semisimple part:

```
rank(SL(4,R)) = rank(SO(4)) ?
3 != 2.
```

So `SL(4,R)`, and hence `GL(4,R)` modulo center, has no ordinary Harish-Chandra
discrete series. The phrase "discrete series of GL(4,R)" cannot close this problem in
the same way it closes the `SL(2,R)` or equal-rank `G/K` cases.

The right language is **relative discrete series for the symmetric space `G/H`** or,
with spinor coefficients, discrete summands of

```
L2(G x_H S(6,4)).
```

This changes what must be computed.

---

## 4. Relative Discrete-Series Rank Test

For a reductive symmetric space `G/H`, the Flensted-Jensen / Oshima-Matsuki theory uses
an equal-rank condition of the form

```
rank(G/H) = rank(K / (K cap H))
```

for the scalar relative discrete series.

For the present pair, choose

```
G = GL(4,R),        K = O(4),
H = O(3,1),         K cap H = O(3) x O(1).
```

The compact quotient is

```
K / (K cap H) = O(4)/(O(3) x O(1)) = RP^3,
```

which has symmetric-space rank

```
rank(K / (K cap H)) = 1.
```

For `G/H`, the noncompact rank is the dimension of a maximal abelian subspace in the
appropriate `p cap q` part. Concretely, in the `GL(4,R)` model this contains the
diagonal symmetric matrices, giving rank `4`; after passing to the semisimple
`SL(4,R)` part, the trace-zero diagonal subspace has rank `3`.

Thus the basic rank comparison is

```
GL form: 4 != 1
SL form: 3 != 1
```

This is a strong obstruction to the scalar relative discrete-series mechanism for
`GL(4,R)/O(3,1)`.

For the spinor-twisted bundle, the exact theorem to invoke must be stated with the
coefficient representation

```
tau = S(6,4)|_{Spin(3,1)}
```

and the space

```
L2(G x_H tau).
```

But even if a twisted relative discrete component existed, its representation space
would be an infinite-dimensional `G`-module with finite multiplicity, not a
24-dimensional vector-space kernel. The number "24" would have to be a multiplicity,
formal dimension, or index pairing, not `dim_H ker D_fib`.

---

## 5. Concrete Computation That Would Actually Decide It

A correct Harish-Chandra/Parthasarathy computation should be formulated as follows.

### Step A: Fix the connected symmetric pair

Use the connected semisimple pair to remove component and center noise:

```
G0 = SL(4,R),
H0 = SO_0(3,1),
K0 = SO(4),
K0 cap H0 = SO(3).
```

Let

```
g = h + q
```

be the symmetric-pair decomposition and let the isotropy representation of `H0` on
`q` be the trace-free part of the metric-variation representation. For the `GL` version
there is one additional scalar trace direction.

### Step B: Identify the coefficient representation

Compute the lift

```
H0 = SO_0(3,1) -> SO(6,4) -> Spin(6,4)
```

coming from the action of Lorentz transformations on

```
Sym^2(R^{3,1}*)
```

with trace reversal. Then decompose the spinor coefficient

```
tau = S(6,4)
```

as a representation of

```
Spin(3,1) ~= SL(2,C).
```

This is not the same as the Pati-Salam branching under
`Spin(6) x Spin(4)`. The Pati-Salam computation controls SM charges; the fiber
Dirac computation needs the noncompact isotropy representation of `Spin(3,1)`.

### Step C: Apply the Parthasarathy square

For each irreducible representation `pi` appearing discretely in

```
L2(G0 x_H0 tau),
```

the homogeneous Dirac square has the schematic form

```
D_tau^2 = -pi(C_g) + tau(C_h) + rho-constant
```

with signs and constants depending on the pseudo-Riemannian convention. A zero mode
requires the Casimir equality

```
pi(C_g) = tau(C_h) + rho-constant.
```

Equivalently, in Dirac-cohomology language, the infinitesimal character of `pi`
must match a Weyl-group translate of an `H`-type occurring in `tau` plus the relevant
rho-shift. This is the concrete Parthasarathy/Harish-Chandra calculation.

### Step D: Check the spectral side

Before counting anything, determine whether those candidate `pi` actually occur as
discrete summands in

```
L2(G0/H0, tau).
```

The rank calculation above says the usual scalar relative discrete-series route is
blocked. If no twisted discrete summands occur, then the homogeneous fiber `L2` kernel
is zero or continuous-spectrum-only. If twisted summands occur despite the scalar
rank obstruction, the result is still a finite multiplicity of infinite-dimensional
`G0`-representations, not a 24-dimensional kernel.

### Step E: Define the number to compare with 24

Only after Step D can one define a number to compare with the generation-count
prediction. Candidate numbers are:

- multiplicity of a discrete summand in `L2(G/H, tau)`,
- formal degree / equivariant index contribution,
- an APS index after choosing a compactification of the metric cone,
- a finite-dimensional kernel on a compact quotient `Gamma \ G/H`.

These are different invariants and need not equal each other.

---

## 6. Consequences for the Generation Count

The representation-theory statement

```
S(6,4) -> one Pati-Salam generation
```

remains coherent and useful.

The analytic statement

```
dim_H ker D_fib = 24
```

does not currently survive as an ordinary `L2` kernel claim on the homogeneous fiber.
The obstruction is not a small missing character calculation; it is a mismatch of
analytic category:

- noncompact homogeneous space,
- noncompact isotropy,
- pseudo-Riemannian vertical metric,
- no ordinary group discrete series for `SL(4,R)`,
- unfavorable equal-rank test for scalar relative discrete series,
- finite-dimensional nonzero `L2` kernel incompatible with `G`-equivariance.

The least misleading restatement is:

> The three-generation count requires an explicitly defined equivariant or compactified
> index whose value is 24 quaternionic units. The homogeneous fiber Dirac operator on
> `GL(4,R)/O(3,1)` does not by itself provide a finite `H`-dimensional kernel of size 24.

---

## 7. Pass / Fail Conditions For A Follow-Up

**Pass, revised.** A follow-up can rescue the analytic count only by providing one of:

1. A compactification of `GL(4,R)/O(3,1)` with natural APS or other boundary condition
   and an explicit index calculation equal to 24.
2. A compact locally symmetric quotient `Gamma \ GL(4,R)/O(3,1)` with a geometrically
   forced index equal to 24 independent of arbitrary choices.
3. A precise equivariant index or relative-discrete-series multiplicity for
   `L2(G x_H S(6,4))`, together with a proof that this is the physical generation
   counter.
4. A full 14-dimensional `D_GU` computation showing that horizontal coupling and the
   rolled-up complex produce a finite 4D zero-mode space even though the isolated fiber
   operator does not.

**Fail.** The current version fails if it continues to require:

```
ordinary dim_H ker_L2(D_fib on GL(4,R)/O(3,1)) = 24.
```

That finite-kernel condition is not the output of Harish-Chandra/Parthasarathy theory
for this homogeneous space.

---

## References

- Harish-Chandra, "Discrete series for semisimple Lie groups I", Acta Mathematica 113
  (1965), 241-318. Criterion: compact Cartan / equal-rank condition for ordinary
  group discrete series.
  https://projecteuclid.org/journals/acta-mathematica/volume-113/issue-none/Discrete-series-for-semisimple-Lie-groups-I--Construction-of/10.1007/BF02391779.pdf
- R. Parthasarathy, "Dirac operator and the discrete series", Annals of Mathematics
  96 (1972), 1-30.
  https://annals.math.princeton.edu/1972/96-1/p01
- M. F. Atiyah and W. Schmid, "A geometric construction of the discrete series for
  semisimple Lie groups", Inventiones Mathematicae 42 (1977), 1-62.
  https://eudml.org/doc/142495
- M. Flensted-Jensen, "Discrete series for semisimple symmetric spaces", Annals of
  Mathematics 111 (1980), 253-311.
  https://annals.math.princeton.edu/1980/111-2/p05
- T. Oshima and T. Matsuki, "A description of discrete series for semisimple symmetric
  spaces", Advanced Studies in Pure Mathematics 4 (1984), 331-390.
  https://projecteuclid.org/ebooks/advanced-studies-in-pure-mathematics/Group-Representations-and-Systems-of-Differential-Equations/chapter/A-Description-of-Discrete-Series-for-Semisimple-Symmetric-Spaces/10.2969/aspm/00410331.pdf

---

*Filed: 2026-06-23. Bounded Task 4/5 exploration. No roadmap/status files updated.*
