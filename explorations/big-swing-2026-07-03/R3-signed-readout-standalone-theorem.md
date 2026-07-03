---
title: "The Signed-Readout Boundary Theorem: A Self-Contained, GU-Independent Statement and Proof"
date: 2026-07-03
problem_label: "R3-signed-readout-standalone-theorem"
status: exploration
verdict: HOME_RUN_ON_ABSTRACT_CORE_AND_PART_Z; OC1_OC2_REMAIN_LABELED_HYPOTHESES
certificate: tests/big-swing/R3_signed_readout_certificate.py
certificate_result: "22/22 checks PASS, exit 0"
---

# The Signed-Readout Boundary Theorem
## A self-contained, referee-checkable, GU-independent theorem with proof

> **Scope statement (read first).** This document is deliberately written so that
> it stands **without any reference to Geometric Unity, to the number 24, 3, 8, to
> chi(K3), or to the Standard-Model spectrum.** No such number is assumed, divided
> by, or normalized to. The theorem is a statement in ordered-algebra + index
> theory. Two independent physical instances are given (a finite Ginsparg-Wilson
> lattice, and abstract signed accumulators); neither is GU. A separate,
> clearly-fenced final section records exactly which two hypotheses (OC1, OC2)
> would have to be supplied by hard non-compact analysis to apply the same theorem
> to a *non-compact* Dirac operator, and states honestly that those two hypotheses
> are **not** discharged here.

---

## 0. What is claimed, and at what grade

| Component | Content | Grade in this document |
|---|---|---|
| **Part M** | Monotone-readout criterion (iff) | **Proved, unconditional, elementary.** |
| **Part P** | Provenance layer is always monotone (PN/Jordan) | **Proved, unconditional.** |
| **Part C** | Coexistence: monotone provenance + non-monotone readout iff a weight is negative | **Proved, unconditional.** |
| **Part Z (compact/finite)** | Integer index + topological protection, instantiated on a **finite** Ginsparg-Wilson operator | **Proved and machine-certified, unconditional.** No non-compact analysis. |
| **Part K (finite shadow)** | H-linear (quaternionic) index is even; `index_H = index_C/2` is the `KSp^0(pt)=Z` augmentation | **Proved and machine-certified, unconditional** (finite dimensional). |
| **Part Z/K (non-compact operator)** | Same conclusions for a non-compact Dirac operator on an open manifold `Y` | **CONDITIONAL** on two explicit analytic hypotheses `OC1`, `OC2`; those are **NOT** discharged here (Section 8). |

The honest headline: **the abstract boundary theorem (M, P, C) is a complete,
unconditional theorem, and its integer/K-theory enhancements (Z, K) are closed
unconditionally on compact/finite spaces.** The only thing that remains a labeled
hypothesis is the *analytic* input needed to run the identical machinery on a
*non-compact* operator -- and that input is a genuine open problem, stated as such.

A runnable certificate `tests/big-swing/R3_signed_readout_certificate.py`
verifies every algebraic and numeric claim below (22/22 checks, exit 0).

---

## 1. Standing data and definitions

### 1.1 The evidence monoid

Let `X` be a nonempty set (the **contribution event types**). Let

```
E = N_0^{(X)} = { e : X -> N_0 with finite support }
```

be the **free commutative monoid** on `X`, written additively, with identity
`0_E` and generators `[x]` (`x in X`). Equip `E` with the **information order**

```
e <=_E e'    iff    e' = e + d for some d in E,
```

i.e. the coordinatewise order `e(x) <= e'(x)` for all `x`. `(E, <=_E)` is a
directed, well-founded, cancellative poset with least element `0_E`, and
`e ∨ e' = e + e'` is a join.

### 1.2 The readout codomain

Let `(G, +, <=_G)` be a **lattice-ordered abelian group** (an abelian group with
a translation-invariant partial order in which every pair has a meet and a join).
Write the **positive cone**

```
G_+ = { g in G : 0_G <=_G g }.
```

`G_+` is closed under `+` and under multiplication by `N_0`. Canonical instances:
`Z` (`G_+ = N_0`), `Z^n` and `R^n` (coordinatewise), `R` (`G_+ = R_{>=0}`).

### 1.3 Weight, signed readout, PN/Jordan split

A **weight** is any map `w : X -> G`. Its **signed readout** is the unique monoid
homomorphism extending `w` (freeness of `E`):

```
R_w : E -> G,   R_w(e) = sum_{x in X} e(x) * w(x).
```

The **PN/Jordan split** of `w` (Jordan-Hahn positive/negative parts, which exist
because `G` is a lattice):

```
w_+(x) = w(x) ∨ 0_G,   w_-(x) = (-w(x)) ∨ 0_G,   so   w = w_+ - w_-,  w_+, w_- : X -> G_+.
```

The **provenance map** and **readout map**:

```
Prov_w : E -> G_+ x G_+,   Prov_w(e) = ( R_{w_+}(e), R_{w_-}(e) )     (product order),
r : G_+ x G_+ -> G,        r(p, n) = p - n,        so     R_w = r ∘ Prov_w.
```

`R_w` is **monotone** if `e <=_E e' => R_w(e) <=_G R_w(e')`.

---

## 2. Part M -- the monotone-readout criterion (proved, unconditional)

**Theorem M.** `R_w` is monotone **iff** `w(x) in G_+` for every `x in X`
(equivalently `w_- ≡ 0_G`).

**Proof.**
(⇒) Suppose `R_w` is monotone. Fix `x in X`. Since `0_E <=_E [x]` and `R_w` is a
homomorphism with `R_w(0_E) = 0_G`, monotonicity gives
`0_G = R_w(0_E) <=_G R_w([x]) = w(x)`, so `w(x) in G_+`.

(⇐) Suppose `w(x) in G_+` for all `x`. If `e <=_E e'` then `e' = e + d`,
`d = sum_j m_j [x_j]` with `m_j in N_0`. Then
`R_w(e') = R_w(e) + sum_j m_j w(x_j)`. Each `w(x_j) in G_+`, and `G_+` is closed
under `N_0`-scaling and addition, so `sum_j m_j w(x_j) in G_+`; by translation
invariance `R_w(e) <=_G R_w(e')`. ∎

**Corollary (failure witness).** If some `w(x_0) <_G 0_G`, the pair
`(0_E, [x_0])` witnesses non-monotonicity: `0_E <=_E [x_0]` but
`R_w([x_0]) = w(x_0) <_G 0_G = R_w(0_E)`.

*Certificate:* Block A of the script verifies Theorem M **exhaustively** over all
weight patterns in `{-1,0,1}^{k·n}` for `G = Z` and `G = Z^2` (27 and 729 patterns,
0 mismatches) and by 20000 randomized trials confirming the canonical witness
`(0_E,[x_0])` alone controls the iff.

---

## 3. Part P -- the provenance layer is always monotone (proved)

**Theorem P.** For every weight `w : X -> G`, the provenance map `Prov_w` is
order-preserving: `e <=_E e' => Prov_w(e) <=_{G_+ x G_+} Prov_w(e')`.

**Proof.** `w_+, w_- : X -> G_+` by construction, so by Theorem M (⇐ direction)
both `R_{w_+}` and `R_{w_-}` are monotone; hence each coordinate of `Prov_w` is
monotone, i.e. `Prov_w` is monotone for the product order. ∎

**Proposition (minimality, PJ5).** Among all splits `(a, b)` with `a, b : X -> G_+`
and `a - b = w`, the Jordan-Hahn split `(w_+, w_-)` is the pointwise least in both
coordinates: any other split has `a(x) >=_G w_+(x)` and `b(x) >=_G w_-(x)`.

**Proof.** `a - b = w = w_+ - w_-` gives `a - w_+ = b - w_- =: s`. Since
`a = w_+ + s >= 0` and `w_+ = w ∨ 0 >= w`, and `a >= w` as well as `a >= 0`, one
gets `s = a - w_+ >= 0` (in a lattice-ordered group `a >= w` and `a >= 0` force
`a >= w ∨ 0 = w_+`). Then `b = w_- + s >= w_-`. ∎

*Certificate:* Block A3/A4 verifies Theorem P and minimality over 20000 + 5000
randomized trials, 0 failures.

---

## 4. Part C -- the boundary (coexistence), proved

**Theorem C.** The readout map `r(p,n) = p - n` is monotone in `p` and
**anti-monotone** in `n`. Consequently, for the factorization `R_w = r ∘ Prov_w`:

1. `Prov_w` is monotone for **every** `w` (Theorem P);
2. `R_w` is monotone **iff** `w_- ≡ 0` (Theorem M);
3. therefore, whenever some `w(x_0) <_G 0`, one has simultaneously **monotone
   provenance and non-monotone readout** -- and the transition happens **exactly**
   at `w_- = 0`, not before.

**Proof.** `r(p+d, n) = r(p,n) + d >= r(p,n)` for `d in G_+` (monotone in `p`);
`r(p, n+d) = r(p,n) - d <= r(p,n)` (anti-monotone in `n`). Items (1),(2) are
Theorems P, M. For (3): if `w(x_0) < 0`, the pair `(0_E, [x_0])` has
`Prov_w(0_E) = (0,0) <= (w_+(x_0), w_-(x_0)) = Prov_w([x_0])` (monotone provenance)
while `R_w([x_0]) = w(x_0) < 0 = R_w(0_E)` (non-monotone readout). ∎

This is the **structural content** of the boundary theorem: non-monotonicity of a
signed accumulator is *entirely localized in the readout subtraction* `p - n`; the
provenance layer never loses monotonicity. The negative cone `w_-` is a complete
obstruction invariant.

---

## 5. Part Z (finite/compact) -- integer index and topological protection, UNCONDITIONAL

Part M/P/C are algebra. Part Z asks: when `G = Z`, is the readout integer a
*topologically protected* invariant -- stable under deformation? On a **finite**
(equivalently compact) space this is fully rigorous with elementary spectral flow,
**with no non-compact functional analysis whatsoever.** We instantiate it with the
canonical physical example, the **Ginsparg-Wilson (overlap) Dirac operator**, so
the theorem's integer readout is literally a lattice axial charge.

### 5.1 Finite Ginsparg-Wilson data

Work in a finite-dimensional chiral Hilbert space `C^N`, `N` even, with chirality
`gamma5 = diag(+1_{n_+}, -1_{n_-})`, `n_+ = n_- = N/2` (so `Tr gamma5 = 0`). Let
`H` be any Hermitian matrix with no zero eigenvalue, and set the **sign operator**

```
eps = sign(H) = H (H^2)^{-1/2},    eps = eps^dagger,   eps^2 = 1.
```

Define the **overlap Dirac operator** (lattice spacing `a > 0`):

```
D = (1/a)( 1 + gamma5 * eps ).
```

**Lemma (GW relation, exact).** `D` satisfies the Ginsparg-Wilson relation

```
gamma5 D + D gamma5 = a D gamma5 D.
```

**Proof.** With `eps^2 = 1`,
`(1 + gamma5 eps) gamma5 (1 + gamma5 eps) = 2 gamma5 + eps + gamma5 eps gamma5`
`= a^2 D gamma5 D`, while
`gamma5 D + D gamma5 = (1/a)(2 gamma5 + eps + gamma5 eps gamma5)`. Equal. ∎

**Lemma (modified chirality).** `gamma-hat_5 := gamma5(1 - a D) = -eps`, hence
`gamma-hat_5 = gamma-hat_5^dagger` and `gamma-hat_5^2 = 1`.

### 5.2 The integer axial charge and its three faces

Define the **axial charge / index**

```
Q(H) := -(1/2) Tr(eps) = -(a/2) Tr(gamma5 D) = (1/2) Tr(gamma-hat_5).
```

All three expressions are equal (Lemmas above and `Tr gamma5 = 0`). Because
`eps` has eigenvalues `+-1` and `N` is even, `Tr(eps) = n_+^H - n_-^H` is an even
integer, so **`Q(H) in Z`** -- unconditionally, at finite lattice spacing.

When `H` is chosen so that `D` has exact zero modes, `Q` equals their signed
chirality count `n_+ - n_-` (Ginsparg-Wilson / Hasenfratz-Laliena-Niedermayer
index theorem). This is the axial charge `Q_A` of lattice gauge theory.

*Certificate (Block B):* For a generic `gamma5`-Hermitian random `H`, the GW
relation holds to `7.2e-15`, `gamma-hat_5^2=1`, and the three routes for `Q` agree.
For an **engineered** `H` with `2` right-handed and `3` left-handed chiral zero-mode
seeds, `D` has exactly `5` zero modes with chirality `n_+ = 2`, `n_- = 3`, giving
`Q = n_+ - n_- = -1 = -(1/2)Tr eps` (all three routes agree). *(The value `-1` is
whatever this construction yields; no target is imposed.)*

### 5.3 Signed-readout coexistence, physically

Assign weight `+1` to a right-handed zero mode and `-1` to a left-handed one.
Provenance `(n_+, n_-)` is monotone as modes accumulate; the readout
`Q_A = n_+ - n_-` is non-monotone. Adding one left-handed mode moves provenance
`(2,3) -> (2,4)` (up in both coordinates) while `Q_A: -1 -> -2` (down). This is a
**GU-independent physical realization of Theorem C** -- Ginsparg-Wilson lattice
fermions are exactly the "monotone provenance, non-monotone readout" phenomenon.

### 5.4 Topological protection = finite-dimensional Atiyah-Janich (proved)

**Theorem Z (finite).** Along any continuous path `t -> H(t)` of Hermitian
matrices, `Q(H(t))` is integer-valued and **locally constant off the codimension-1
locus where `H(t)` acquires a zero eigenvalue**; across a simple crossing it jumps
by exactly `+-1` (spectral flow).

**Proof.** `Q(H) = -(1/2)(#pos - #neg)` eigenvalues; eigenvalues are continuous in
`H`, and the sign count can only change when an eigenvalue passes through `0`. A
simple crossing flips one sign, changing `#pos - #neg` by `+-2`, hence `Q` by
`+-1`. Between crossings the spectrum stays off `0`, so `Q` is constant. ∎

This *is* the Atiyah-Janich stability mechanism, in the finite-dimensional case
where it is a two-line proof: the index is the class of the map
`t -> eps(t) in {Hermitian involutions}` into the space that classifies `pi_0`,
and it is locally constant because the Fredholm (here: invertibility) locus is
open.

*Certificate (Block B7):* deform `H(s) = H - sI` across its whole spectrum;
`Q(s)` sweeps `12` unit steps (one per eigenvalue of the `N=12` system), range
`[-6, +6] = [-N/2, +N/2]`, every jump `+-1` and located exactly at a spectral
crossing (gap `< 0.05`). This is textbook spectral flow, machine-verified.

**Why this matters for the whole program.** Part Z is the place the earlier notes
flagged as gated by "Atiyah-Janich in a non-compact `L^2` setting" (OC1). The
present section shows the *topological* content of Part Z -- integrality plus
protection -- is **unconditional and elementary on any finite/compact space**, and
that a genuine, GU-free physical operator (the overlap/GW Dirac operator)
instantiates it. The non-compact difficulty (Section 8) is purely *analytic*
(is a given non-compact operator Fredholm and continuous?), not topological.

---

## 6. Part K (finite shadow) -- the KSp augmentation, UNCONDITIONAL

**Setup.** Put a quaternionic structure on `C^{2m}`: `J psi = Omega * conj(psi)`
with `Omega = I_m ⊗ (i sigma_y)`, so `J` is antilinear and `J^2 = -1`. An operator
`A` is **H-linear (quaternionic / self-dual)** iff `A J = J A`, equivalently
`Omega^{-1} A Omega = conj(A)`.

**Theorem K (finite).** For an H-linear `A`, `ker A` and `coker A` are
`J`-invariant; since `J` is antilinear with `J^2 = -1`, each is even-complex-
dimensional (Kramers). Hence `index_C(A)` is even and

```
index_H(A) := index_C(A)/2 = dim_H ker A - dim_H coker A  in Z
```

is well-defined -- the `KSp^0(pt) = Z` augmentation. Equivalently, all singular
values of `A` occur in equal Kramers pairs.

**Proof.** If `A v = 0` then `A (Jv) = J (A v) = 0`, so `ker A` is `J`-invariant.
`J` antilinear, `J^2 = -1` implies no `J`-invariant subspace is odd-dimensional
over `C` (a `J`-invariant vector and `Jv` are `C`-independent and span a
`J`-stable plane). Same for `coker A ≅ ker A^dagger` (`A^dagger` is also
H-linear). ∎

This is the finite-dimensional shadow of the infinite-dimensional statement
`[X, Fred_H(K_H)] = KSp^0(X) = KO^{-4}(X) = KO^4(X)` (Atiyah-Singer skew-adjoint /
quaternionic Fredholm classification). It captures the augmentation
`KSp^0(X) -> KSp^0(pt) = Z` without any topology beyond linear algebra.

*Certificate (Block C):* `J^2 = -1` verified; over 200 random H-linear operators,
self-duality holds, singular values are Kramers-paired, and every engineered
rank-deficient H-linear operator has even complex kernel.

---

## 7. The complete standalone theorem (as stated)

Assembling Sections 2-6 into one statement, with all hypotheses explicit:

> **Signed-Readout Boundary Theorem (self-contained form).**
> Let `X` be a nonempty set, `E = N_0^{(X)}` with the information order, `G` a
> lattice-ordered abelian group, `w : X -> G` a weight with signed readout `R_w`,
> PN/Jordan split `(w_+, w_-)`, provenance `Prov_w`, and readout `r(p,n)=p-n`.
> Then:
> - **(M)** `R_w` is monotone iff `w(x) in G_+` for all `x`;
> - **(P)** `Prov_w` is monotone for every `w`;
> - **(C)** `R_w = r ∘ Prov_w`, `r` is monotone in `p` and anti-monotone in `n`,
>   so monotone provenance coexists with non-monotone readout exactly when
>   `w_- != 0`.
> Moreover, if `G = Z` and the weight data are realized by a **finite**
> Ginsparg-Wilson operator `D = (1/a)(1 + gamma5 eps)` (`eps^2 = 1`,
> `gamma5^2 = 1`, `Tr gamma5 = 0`), then:
> - **(Z)** `Q = -(1/2)Tr eps in Z` is the axial charge, equal to the signed
>   chirality of the zero modes, and is locally constant under deformations off
>   the (codimension-1) spectral-crossing locus, jumping by `+-1` across a simple
>   crossing;
> - **(K)** if in addition `D` is H-linear for a quaternionic structure `J`, then
>   `Q` is even and `Q/2 = index_H` is the `KSp^0(pt) = Z` augmentation.

Every clause is proved above and machine-certified. **This is a complete theorem a
referee can check; it never mentions GU.**

---

## 8. The two labeled hypotheses for the NON-COMPACT case (honest fence)

The *only* place the theorem does not yet apply verbatim is when one wants Part Z/K
for a genuinely **non-compact** Dirac operator `D_Y` on an open manifold `Y`
(the setting relevant to the GU program, and to any continuum index theorem on a
non-compact space). The topological engine of Sections 5-6 is unchanged; what is
missing is purely the analytic input that puts `D_Y` into that engine. We state it
as two explicit hypotheses and **do not claim to discharge them.**

- **(OC1) Continuous Fredholm realization.** There is a fixed separable Hilbert
  space `K` and a continuous map `t -> F_t in Fred(K)` (norm/gap topology), where
  `F_t = D_t(1 + D_t^* D_t)^{-1/2}` is the bounded transform of the deformation
  family, and the path stays in the Fredholm locus (no essential spectrum reaching
  `0`, discrete sector transported continuously). **Given OC1, Theorem Z holds for
  `D_Y` verbatim** by the Atiyah-Janich classifying-space theorem
  (`Fred(K) ≃ Z x BU`), of which Section 5.4 is the finite-dimensional case.

- **(OC2) H-linear Fredholm realization.** The same map lands in the quaternionic
  Fredholm space, `t -> F_t in Fred_H(K_H)`, `K_H = L^2(Y, H^r)`, with each `F_t`
  commuting with the quaternionic structure. **Given OC2, Theorem K holds for
  `D_Y` verbatim**, `[F] in [X, Fred_H(K_H)] = KSp^0(X) = KO^4(X)`, augmenting to
  `index_H in Z`; Section 6 is the finite-dimensional case.

**Where the wall is (stated plainly).** OC1 and OC2 are not topological gaps --
the topology is done (Sections 5, 6, and the classical classifying-space theorems).
They are *analytic* facts about a *specific* non-compact operator: one must prove
that `D_Y` (with a chosen Sobolev domain, on the chosen `L^2`) is **Fredholm** with
**closed range** and **finite-dimensional kernel/cokernel**, and that the chosen
deformation family is **norm-continuous in the bounded transform** and **never
leaves the Fredholm locus** (in particular the relevant discrete-series /
`L^2`-sector must persist). For an open manifold this does **not** follow from
ellipticity alone; it requires control of the operator at infinity (invertibility
of the asymptotic operator, a spectral gap, or a suitable Callias/relative-index
mechanism). **This document does not carry out that analysis, and to the best of
this note's knowledge it is genuinely open for the GU operator.** Clearing it would
require: (i) an explicit Sobolev domain and self-adjoint extension for `D_Y`;
(ii) a proof of a spectral gap / invertibility at infinity giving Fredholmness on
the relevant sector; (iii) graph/gap continuity of the allowed deformations.

Because of this, the theorem is stated in two tiers: **unconditional** (Sections
2-7, abstract + finite/compact Part Z/K), and **conditional on OC1/OC2** (the
non-compact application). No status of the non-compact case is promoted; the
generation-count verdict is untouched by this document.

---

## 9. Falsification conditions

The theorem is falsified by any of:

- **F1** `E` not free commutative (a relation `[x] = 0_E` collapses the `(⇒)`
  witness; Theorem M's iff degenerates). *Guard:* `E = N_0^{(X)}`.
- **F2** `G` not lattice-ordered (`w ∨ 0` may not exist; Prov_w undefined).
  *Guard:* hypothesis H3.
- **F3** order not translation-invariant (Theorem M `(⇐)` fails). *Guard:* ordered
  abelian group.
- **F4** `w` not single-valued on `X` (`R_w` ill-defined). *Guard:* `w` a function.
- **F5** information order replaced by an external causal order in which
  `0_E <=_E [x]` can fail (then M is necessary, not sufficient). *Guard:* free
  divisibility order; the record-graph layer treats causal orders separately.
- **F6 (Part Z)** the GW/overlap structure broken: if `eps^2 != 1` the GW relation
  and integrality both fail. *Guard:* `eps = sign(H)`, verified `||eps^2-1|| < 1e-13`.
- **F7 (Part K)** operator only C-linear, not H-linear: the index lands in
  `K^0 = KU^0`, not `KSp^0`, and need not be even. *Guard:* verify `A J = J A`.
- **F8 (non-compact)** OC1/OC2 fail: `D_Y` not Fredholm, or `0` in essential
  spectrum, or discrete sector not transported -- then Part Z/K do not apply to
  `D_Y` and no integer is protected. *This is the open case, fenced in Section 8.*

---

## 10. Certificate

`tests/big-swing/R3_signed_readout_certificate.py` -- run:

```
cd C:/Users/joe/JB/CapacityOS/repos/public/gu-formalization
python tests/big-swing/R3_signed_readout_certificate.py
```

Result on this machine: **22/22 checks PASS, exit 0.** Highlights:
- Block A: Theorem M exhaustive over 27 (`G=Z`) and 729 (`G=Z^2`) weight patterns,
  0 mismatches; P, C, minimality over 45000 randomized trials, 0 failures.
- Block B: GW relation exact to `7.2e-15`; `gamma-hat_5^2 = 1`; three index routes
  agree; engineered `Q = -1 = n_+ - n_-` with `5` exact zero modes; coexistence
  witness `(2,3)->(2,4)`, `Q: -1 -> -2`; topological protection with `12` spectral
  crossings sweeping `Q in [-6, +6]`, every jump `+-1` at a zero-crossing.
- Block C: `J^2=-1`; 200 H-linear operators Kramers-paired; even complex kernels.

No number in the certificate is a target import: `Q = -1`, the range `[-6,6]`, and
the `5` zero modes are all determined by the explicitly constructed matrices, not
chosen to match any physical constant.

---

## 11. Honest outcome

**Home run on the abstract core and on compact Part Z/K.** The signed-readout
boundary theorem is now a **complete, self-contained, GU-independent theorem with
full proofs** (Parts M, P, C unconditional; Parts Z, K unconditional on
finite/compact spaces), backed by a passing executable certificate. The genuine,
GU-free physical instance -- Ginsparg-Wilson lattice fermions -- realizes the
coexistence phenomenon and the protected integer index concretely.

**Where it stops (the wall).** The two open upgrade conditions OC1 (continuous
non-compact Fredholm realization) and OC2 (H-linear version) are **not** closed
here. They are not topological -- the topology is complete -- but *analytic*
facts about a specific non-compact operator (Fredholmness, closed range,
continuity of the bounded transform, persistence of the discrete sector). They are
stated as explicit, clearly-labeled hypotheses so the theorem is *complete as
stated*: unconditional in the compact/finite tier, and conditional-on-OC1/OC2 in
the non-compact tier. Clearing the wall needs a real non-compact analysis (Sobolev
domain, spectral gap at infinity, gap-continuity) that this session does not
perform and that appears genuinely open for the GU operator. No cross-repo or
generation-count status is changed.
