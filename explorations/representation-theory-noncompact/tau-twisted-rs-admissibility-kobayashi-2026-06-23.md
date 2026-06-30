---
title: "Tau-Twisted RS Admissibility: Direct Oshima-Matsuki / Kobayashi Check"
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
problem_label: "tau-twisted-rs-admissibility-kobayashi"
verdict: FAILS
owned_by: "Task 1"
---

# Tau-Twisted RS Admissibility: Direct Criterion Check

## Verdict

**FAILS as stated.**

The tau-twisted sector

```text
L^2(SL(4,R) x_{SO_0(3,1)} tau_RS),
tau_RS = 4D(1/2,0) + 4D(0,1/2),
```

does **not** currently satisfy the relevant Oshima-Matsuki / Kobayashi admissibility
gates needed for an analytic RS discrete contribution.

More precisely:

1. The scalar Oshima-Matsuki/Flensted-Jensen discrete-spectrum gate fails for the actual
   metric pair: `rank(G/H)=3`, while `rank(K/(K cap H))=1`.
2. The coefficient `tau_RS` is a nontrivial finite-dimensional Lorentz spinor
   representation of the noncompact group `SO_0(3,1)`. It is not unitary, so the displayed
   object is not a standard Hilbert `L^2` induced representation unless an additional
   indefinite or nonunitary analytic framework is specified.
3. The Kobayashi admissible-restriction / discrete-decomposability route fails for this
   symmetric pair. The classification of symmetric pairs admitting an infinite-dimensional
   discretely decomposable `(g,K)`-module does not include
   `(sl(4,R), so(3,1))`.
4. The compact asymptotic cone calculation shows that twisting by the spin-1/2
   `K cap H` type changes only the lowest/parity data. It does not remove the nonzero
   cone obstruction and therefore does not justify `rank_correction(tau_RS)=2`.

The rank-independent physical count `C^32 -> C^16 -> dim_H=8` may still be cited as a
separate reconstruction-grade count. It is not an Oshima-Matsuki/Kobayashi proof of a
finite discrete Plancherel atom.

## Inputs Inspected

Requested local inputs:

- `explorations/representation-theory-noncompact/tau-correction-oshima-matsuki-rs-2026-06-23.md`
- `explorations/representation-theory-noncompact/oq-weyl3-root-wall-plancherel-2026-06-23.md`
- `explorations/generation-sector/oq3b-rs-index-8-2026-06-23.md`
- `explorations/representation-theory-noncompact/oq1-split-rank-verification-2026-06-23.md`
- `explorations/representation-theory-noncompact/split-rank-reconciliation-audit-2026-06-23.md`
- `NEXT-STEPS.md`
- `DERIVATION-PROGRESS.md`

External primary sources used:

- Flensted-Jensen, "Discrete series for semisimple symmetric spaces", Annals of
  Mathematics 111 (1980), 253-311:
  https://annals.math.princeton.edu/1980/111-2/p05
- Oshima and Matsuki, "A Description of Discrete Series for Semisimple Symmetric Spaces",
  Adv. Stud. Pure Math. 4 (1984), 331-390:
  https://projecteuclid.org/ebooks/advanced-studies-in-pure-mathematics/Group-Representations-and-Systems-of-Differential-Equations/chapter/A-Description-of-Discrete-Series-for-Semisimple-Symmetric-Spaces/10.2969/aspm/00410331.pdf
- Kobayashi, "Discrete decomposability of the restriction of A_q(lambda) with respect
  to reductive subgroups and its applications", Invent. Math. 117 (1994), 181-205:
  https://www.ms.u-tokyo.ac.jp/~toshi/texpdf/invent94-full.pdf
- Kobayashi and Oshima, "Classification of symmetric pairs with discretely decomposable
  restrictions of (g,K)-modules", arXiv:1202.5743:
  https://arxiv.org/pdf/1202.5743
- Kobayashi, "Admissible restrictions of irreducible representations of reductive Lie
  groups: symplectic geometry and discrete decomposability", arXiv:1907.12964:
  https://arxiv.org/pdf/1907.12964
- Kobayashi and Oda, "A vanishing theorem for modular symbols on locally symmetric
  spaces", Comment. Math. Helv. 73 (1998), 45-70:
  https://www.ms.u-tokyo.ac.jp/~toshi/texpdf/CMH98.pdf

## Criterion 1: Scalar Oshima-Matsuki/Flensted-Jensen Gate

The scalar criterion used in the local notes is:

```text
Disc L^2(G/H) is nonzero iff rank(G/H) = rank(K/(K cap H)).
```

Kobayashi 1994 records this as the Flensted-Jensen, Matsuki, and Oshima existence
criterion for semisimple symmetric spaces. Oshima-Matsuki is the classification source.

For the actual metric pair:

```text
G = SL(4,R)
H = SO_0(3,1)
dsigma_B(X) = -J X^T J^{-1},  J = diag(1,1,1,-1)
K = SO(4)
K cap H = SO(3)
```

The corrected local matrix computation gives:

```text
p_G cap q_B = span{H_1,H_2,H_3,S_12,S_13,S_23}
a_q = span{H_1,H_2,H_3}
rank(G/H) = dim(a_q) = 3
```

Meanwhile:

```text
K/(K cap H) = SO(4)/SO(3) ~= S^3
rank(K/(K cap H)) = 1
```

Therefore:

```text
rank(G/H) = 3 != 1 = rank(K/(K cap H)).
```

So scalar `L^2(SL(4,R)/SO_0(3,1))` has no Oshima-Matsuki/Flensted-Jensen discrete
series. This agrees with the already-opened `tau-correction-oshima-matsuki-rs` and
`split-rank-reconciliation-audit` notes.

## Criterion 2: Hilbert `L^2` Precondition For The Coefficient

For a genuine Hilbert representation `L^2(G x_H V_tau)`, the fiber representation
`tau` must carry an `H`-invariant positive Hermitian form, so that the section norm is
well-defined and the left `G` action is unitary.

Here:

```text
H = SO_0(3,1) ~= PSL(2,C) at Lie algebra level
tau_RS = 4D(1/2,0) + 4D(0,1/2)
```

The summands `D(1/2,0)` and `D(0,1/2)` are nontrivial finite-dimensional Lorentz
spinor representations. A noncompact semisimple group has no nontrivial finite-dimensional
unitary representations. Thus `tau_RS` is not unitary.

Consequences:

```text
standard unitary L^2(G x_H tau_RS): not defined as stated
Oshima-Matsuki Hilbert discrete spectrum: not directly applicable
Kobayashi unitary branching/admissibility: not directly applicable to tau_RS as a Hilbert fiber
```

One can still formulate nonunitary smooth induced modules, hyperfunction boundary-value
problems, or indefinite Lorentz-covariant bundles. But that is a different object from the
displayed Hilbert `L^2` sector and must be specified before using Plancherel or Fredholm
language.

## Criterion 3: Kobayashi Discrete-Decomposability Route

The relevant Kobayashi-style admissibility test is not a rank subtraction. It is a
restriction criterion for a finite-length `(g,K)` module `X`.

A compact version is:

```text
X is K'-admissible iff AS_K(X) cap C_K(K') = {0},
```

where:

```text
AS_K(X) = asymptotic K-support of X
C_K(K') = t_+^* cap sqrt(-1) Ad^*(K)(k')^perp
K' = K cap H
```

Kobayashi-Oshima also classify symmetric pairs `(g,h)` for which there exists at least
one infinite-dimensional irreducible `(g,K)` module that is discretely decomposable as
an `(h,K cap H)` module.

For this problem:

```text
g = sl(4,R)
h = so(3,1)
K = Spin(4) ~= SU(2)_L x SU(2)_R
K' = Spin(3) ~= SU(2)_diag
```

The classification table for simple `g` includes, for `sl(2n,R)`, the symmetric subpairs

```text
sl(n,C) + u(1)
sp(n,R)
```

and not the metric pair

```text
so(p,2n-p), in particular so(3,1) inside sl(4,R).
```

For `n=2`, `so(3,1) ~= sl(2,C)_R` has real dimension `6`; it is not the listed
`sl(2,C)_R + u(1)` case, which has real dimension `7`, and it is not `sp(2,R)`.

Thus the Kobayashi-Oshima existence classification gives:

```text
There is no infinite-dimensional irreducible (sl(4,R),K)-module X
that is discretely decomposable as an (so(3,1),K') module.
```

This falsifies the admissible-restriction route for the RS contribution. The trivial
`G` representation is irrelevant because it restricts to the trivial `H` type and cannot
produce the spinor coefficient `D(1/2,0)` or `D(0,1/2)`.

Important nuance: Kobayashi's restriction theory is not the same as the scalar
Oshima-Matsuki relative discrete-series problem. In fact, for irreducible symmetric
spaces there are exclusivity phenomena between relative discrete series and discretely
decomposable restrictions. The point here is narrower: if the local argument wants a
Kobayashi admissible-restriction proof of a finite RS `H`-multiplicity, this pair fails
the direct classification gate.

## Compact Cone Calculation For The RS Spinor Twist

The coefficient itself can also be checked at the compact `K` level.

Use the double cover:

```text
K = Spin(4) = SU(2)_L x SU(2)_R
K' = Spin(3) = SU(2)_diag
```

Irreducible `K` types are labelled by pairs `(j_L,j_R)`. Their restriction to the diagonal
`SU(2)` is the Clebsch-Gordan sum:

```text
V_{j_L} tensor V_{j_R}|_{SU(2)_diag}
  = direct sum_{j=|j_L-j_R|}^{j_L+j_R} V_j.
```

The RS coefficient restricts to:

```text
tau_RS|_{K'} = 8 V_{1/2}.
```

Therefore the compactly induced `K` module has:

```text
Hom_K(V_{j_L,j_R}, Ind_{K'}^K V_{1/2})
  ~= Hom_{K'}(V_{j_L,j_R}|_{K'}, V_{1/2}).
```

The condition for `V_{1/2}` to occur is:

```text
|j_L - j_R| <= 1/2 <= j_L + j_R
```

with the usual half-integral parity condition. In particular the infinite families

```text
(j_L,j_R) = (n + 1/2, n)
(j_L,j_R) = (n, n + 1/2)
```

occur for all sufficiently large `n`.

The normalized highest weights of these families tend to the diagonal ray:

```text
R_{\ge 0} (1,1).
```

For `K/K' = (SU(2) x SU(2))/SU(2)_diag ~= S^3`, the moment cone is exactly this
diagonal ray:

```text
C_K(K') = R_{\ge 0} (1,1).
```

Thus the spinor coefficient has nonzero asymptotic intersection with the Kobayashi cone:

```text
AS_K(Ind_{K'}^K tau_RS) cap C_K(K') contains R_{\ge 0}(1,1).
```

This is the opposite of the vanishing condition. It also explains why the proposed
shortcut

```text
split-rank_tau = split-rank(G/H) - 2
```

is not a Kobayashi cone computation. Tensoring with a finite-dimensional representation
does not change asymptotic `K`-support; it can shift bottom `K` types and parity, but it
does not remove an asymptotic ray.

This is also the relevant reading of the Kobayashi-Oda modular-symbol source cited in the
local notes: its usable obstruction/vanishing mechanism is an asymptotic-support cone
condition. It is not a theorem that a Lorentz spinor coefficient subtracts two dimensions
from the symmetric-space split rank.

## What The Root-Wall Calculation Does And Does Not Prove

The `oq-weyl3-root-wall-plancherel` note correctly observes that:

```text
lambda_RS = (1/2,0,0,-1/2)
<e_2-e_3, lambda_RS> = 0
```

does not force a zero in the shifted A3 formal-degree product, because the local product
being used is evaluated at `lambda_RS + rho_G`.

That removes one possible zero-factor objection. It does **not** prove:

```text
Disc L^2(G/H,tau_RS) nonzero
Kobayashi admissibility
finite Hom_H multiplicity 8
rank_correction(tau_RS)=2
```

So the root-wall check is compatible with this note's negative verdict.

## Calculations Attempted

### 1. Symmetric-space rank

From the corrected `sigma_B` matrix calculation:

```text
dim a_q = 3
rank K/K' = 1
```

The scalar Oshima-Matsuki criterion fails.

### 2. Coefficient unitarity

The summands `D(1/2,0)` and `D(0,1/2)` are nontrivial finite-dimensional Lorentz spinor
representations. They are not unitary representations of noncompact `SO_0(3,1)`. Therefore
the displayed Hilbert `L^2` sector is not defined in the ordinary unitary-induced sense.

### 3. Kobayashi-Oshima classification

The symmetric pair `(sl(4,R), so(3,1))` is not in the classification list of symmetric
pairs admitting any infinite-dimensional irreducible discretely decomposable restriction.
This rules out the admissible-restriction route.

### 4. Compact spinor branching

The branching calculation:

```text
(j_L,j_R)|_{diag SU(2)} contains 1/2
iff |j_L-j_R| <= 1/2 <= j_L+j_R
```

produces unbounded families asymptotic to `(1,1)`. Hence the spinor twist keeps the same
nonzero moment cone and supplies no rank correction.

## Failure Conditions

**F1. Nonunitary coefficient.** The stated Hilbert space
`L^2(G x_H tau_RS)` is not a standard unitary induced `L^2` space because `tau_RS` is
nonunitary. This failure currently fires.

**F2. Scalar equal-rank failure.** For the actual metric pair, `rank(G/H)=3` and
`rank(K/K')=1`. This failure currently fires.

**F3. Discrete-decomposability classification failure.** The pair
`(sl(4,R), so(3,1))` is absent from the Kobayashi-Oshima list of symmetric pairs that
admit an infinite-dimensional irreducible discretely decomposable restriction. This failure
currently fires for the Kobayashi route.

**F4. Compact cone obstruction.** The spinor coefficient gives unbounded `K` types whose
limit is the nonzero diagonal ray `C_K(K')`. The Kobayashi cone vanishing condition fails;
finite-dimensional twisting does not erase this ray. This failure currently fires.

**F5. Missing Hom normalization.** No direct computation gives
`dim Hom_H(pi^infty, tau_RS)=8` for a discrete `G` summand. The number `8` is still a
physical fiber count, not a verified relative Plancherel multiplicity.

**F6. Possible reformulation outside this note.** A future nonunitary vector-bundle or
hyperfunction-boundary theorem could define a different problem and produce a discrete
object. That would not rescue the current `rank_correction=2` shortcut; it would be a new
analytic construction with different hypotheses.

## Next Action

Do **not** use:

```text
rank_correction(tau_RS)=2
split-rank_tau = 3 - 2 = 1
```

as an analytic gate.

If the RS analytic contribution is still needed, the next bounded task should be one of:

1. Reformulate the Lorentz spinor coefficient as a precise nonunitary
   Casselman-Wallach or hyperfunction-boundary problem, then compute
   `Hom_H(pi^infty, tau_RS)` for a named candidate `pi`.
2. Find a primary vector-bundle relative-discrete-series theorem that explicitly allows
   nonunitary finite-dimensional `H` coefficients and apply its hypotheses to
   `(SL(4,R), SO_0(3,1), tau_RS)`.
3. Otherwise demote the RS analytic contribution to the independent physical count:
   `C^32` physical RS modes, chiral half `C^16`, hence `dim_H=8`.

Until one of those is completed, the representation-theoretic RS contribution should be
recorded as:

```text
scalar Oshima-Matsuki/FJ:        FAILS
unitary tau-twisted L2 sector:   FAILS_AS_STATED
Kobayashi admissible restriction: FAILS
rank_correction=2 shortcut:      FALSIFIED / DO NOT USE
physical H-line count:           separate reconstruction-grade support for 8
```
