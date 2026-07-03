# The Signed-Readout Boundary Theorem: Monotone Provenance, Non-Monotone Readout, and an Integer Index on Compact Spaces

**Draft, internal tier. Publication DEFERRED (Joe-gated). Not submitted anywhere.** This paper states and
proves a self-contained theorem in ordered-algebra and index theory. It is **GU-independent**: it makes no
reference to Geometric Unity, to `chi(K3)`, or to the numbers 24 / 8 / 3 -- no such number is assumed,
divided by, or normalized to, and the paper claims nothing about any generation count. Four load-bearing
caveats hold throughout: **(a)** the abstract core (Parts M, P, C) is proved unconditionally and by
elementary means; **(b)** the integer-index and K-theory enhancements (Parts Z, K) are proved and
machine-certified **only on finite / compact spaces** -- no non-compact functional analysis is performed;
**(c)** the extension of Parts Z / K to a genuinely **non-compact** Dirac operator is **conditional** on two
explicit analytic hypotheses, OC1 and OC2, which are stated but **not** discharged here (Section 8) and appear
genuinely open; **(d)** all verification is **internal-tier** -- computed, re-run, and adversarially reviewed
within one AI-directed process, **not** independently replicated or peer-reviewed. See Sections 0 and 9.

*Repository working copy. Source exploration:
[`explorations/big-swing-2026-07-03/R3-signed-readout-standalone-theorem.md`](../../explorations/big-swing-2026-07-03/R3-signed-readout-standalone-theorem.md).
Canonical spine (citable):
[`canon/signed-readout-boundary-theorem-RESULTS.md`](../../canon/signed-readout-boundary-theorem-RESULTS.md).
Executable certificate:
[`tests/big-swing/R3_signed_readout_certificate.py`](../../tests/big-swing/R3_signed_readout_certificate.py)
(22/22 checks PASS, exit 0, re-run 2026-07-03). Suggested classification: primary **math-ph**; secondary
**math.OA** (ordered / Krein-space algebra), **math.KT** (quaternionic K-theory augmentation). Keywords:
lattice-ordered abelian group, Jordan-Hahn decomposition, signed accumulator, monotone map, Ginsparg-Wilson
relation, overlap Dirac operator, spectral flow, Atiyah-Janich, quaternionic Fredholm index, KSp.*

Internal version 1.0, 2026-07-03.

---

## Abstract

We isolate and prove a small, self-contained theorem about **signed accumulators**: maps that tally weighted
evidence into a lattice-ordered group and read out a net value. The phenomenon it captures is that a signed
readout can **lose monotonicity while its underlying bookkeeping never does**, and that the loss is completely
controlled by a single sign invariant.

Let `X` be a set of event types, `E = N_0^{(X)}` the free commutative monoid on `X` with its divisibility
(information) order, `G` a lattice-ordered abelian group, and `w : X -> G` a weight with signed readout
`R_w : E -> G`. We prove three unconditional, elementary facts. **(M)** `R_w` is monotone iff every weight
`w(x)` lies in the positive cone `G_+`. **(P)** The provenance map `Prov_w = (R_{w_+}, R_{w_-})` built from the
Jordan-Hahn positive/negative parts of `w` is monotone for **every** `w`. **(C)** Since the readout
`r(p, n) = p - n` is monotone in `p` and anti-monotone in `n`, monotone provenance and non-monotone readout
**coexist exactly** when the negative part `w_-` is nonzero; the negative cone is a complete obstruction
invariant.

We then enhance the codomain `G = Z` to an integer index. On a **finite** (hence compact) chiral space we
instantiate the readout with a **Ginsparg-Wilson overlap Dirac operator** `D = a^{-1}(1 + gamma5 * eps)`,
`eps = sign(H)`, and prove **(Z)** its axial charge `Q = -\tfrac12 Tr(eps)` is an integer equal to the signed
chirality of the zero modes, locally constant under deformations off a codimension-1 crossing locus and jumping
by `+-1` across a simple crossing -- the Atiyah-Janich stability mechanism in its two-line finite-dimensional
form. Adding a quaternionic structure `J` (`J^2 = -1`) we prove **(K)** the complex index of an H-linear
operator is even and `index_H = index_C / 2` realizes the `KSp^0(pt) = Z` augmentation. Every algebraic and
numeric claim is checked by an executable certificate (22/22, exit 0).

The abstract core (M, P, C) and the compact enhancements (Z, K) are **unconditional**. The **only** open piece
is the extension of Z / K to a **non-compact** Dirac operator on an open manifold: the topology is unchanged,
but the required analytic inputs -- Fredholmness with closed range, and norm-continuity of the bounded
transform along the allowed deformations -- are fenced as two labeled hypotheses OC1 and OC2 that we do **not**
discharge (Section 8). The pieces (Krein-space graph arguments, GW index theory, quaternionic Fredholm
classification) are classical; the contribution is the **assembly** into one boundary theorem with a single
sign invariant and an honest compact / non-compact fence. This is an internal-tier draft; external replication
is the outstanding step.

---

## 0. What is claimed, and at what grade

| Component | Content | Grade in this paper |
|---|---|---|
| **Part M** | monotone-readout criterion (iff) | proved, unconditional, elementary |
| **Part P** | the provenance layer is always monotone (Jordan-Hahn split) | proved, unconditional |
| **Part C** | coexistence: monotone provenance + non-monotone readout iff a weight is negative | proved, unconditional |
| **Part Z** (compact/finite) | integer index + topological protection on a **finite** Ginsparg-Wilson operator | proved and machine-certified, unconditional; no non-compact analysis |
| **Part K** (finite shadow) | H-linear (quaternionic) index is even; `index_H = index_C / 2` is the `KSp^0(pt) = Z` augmentation | proved and machine-certified, unconditional (finite-dimensional) |
| **Part Z / K** (non-compact operator) | same conclusions for a non-compact Dirac operator on an open manifold `Y` | **CONDITIONAL** on two explicit analytic hypotheses OC1, OC2 -- **not** discharged here (Section 8) |

**Headline.** The abstract boundary theorem (M, P, C) is a complete, unconditional, elementary theorem, and
its integer / K-theory enhancements (Z, K) are closed unconditionally on compact / finite spaces. The one open
piece is the non-compact operator extension, fenced behind two **labeled** hypotheses (OC1, OC2) that this
paper honestly does not discharge. Every clause of M, P, C, Z, K is verified by the runnable certificate
`tests/big-swing/R3_signed_readout_certificate.py` (22/22 checks, exit 0). Nothing here concerns any physical
generation count, and no target number is imported anywhere.

---

## 1. Standing data and definitions

### 1.1 The evidence monoid

Let `X` be a nonempty set of **contribution event types**. Let

```
E = N_0^{(X)} = { e : X -> N_0 with finite support }
```

be the **free commutative monoid** on `X`, written additively, with identity `0_E` and generators `[x]`
(`x in X`). Equip `E` with the **information (divisibility) order**

```
e <=_E e'    iff    e' = e + d for some d in E,
```

i.e. the coordinatewise order `e(x) <= e'(x)`. `(E, <=_E)` is a directed, well-founded, cancellative poset
with least element `0_E`, and `e ∨ e' = e + e'` is a join.

### 1.2 The readout codomain

Let `(G, +, <=_G)` be a **lattice-ordered abelian group** (an abelian group with a translation-invariant
partial order in which every pair has a meet and a join). Write the positive cone
`G_+ = { g in G : 0_G <=_G g }`; it is closed under `+` and under multiplication by `N_0`. Canonical
instances: `Z` (`G_+ = N_0`), `Z^n` and `R^n` (coordinatewise), `R` (`G_+ = R_{>=0}`).

### 1.3 Weight, signed readout, Jordan-Hahn split

A **weight** is any map `w : X -> G`. Its **signed readout** is the unique monoid homomorphism extending `w`
(freeness of `E`):

```
R_w : E -> G,   R_w(e) = sum_{x in X} e(x) * w(x).
```

The **Jordan-Hahn (positive/negative) split** exists because `G` is a lattice:

```
w_+(x) = w(x) ∨ 0_G,   w_-(x) = (-w(x)) ∨ 0_G,   w = w_+ - w_-,   w_+, w_- : X -> G_+.
```

Define the **provenance map** and the **readout map**:

```
Prov_w : E -> G_+ x G_+,   Prov_w(e) = ( R_{w_+}(e), R_{w_-}(e) )   (product order),
r : G_+ x G_+ -> G,        r(p, n) = p - n,        so   R_w = r ∘ Prov_w.
```

`R_w` is **monotone** if `e <=_E e' => R_w(e) <=_G R_w(e')`.

---

## 2. Part M -- the monotone-readout criterion (unconditional)

**Theorem M.** `R_w` is monotone **iff** `w(x) in G_+` for every `x in X` (equivalently `w_- ≡ 0_G`).

*Proof.* (⇒) If `R_w` is monotone, then for each `x`, `0_E <=_E [x]` and `R_w(0_E) = 0_G` give
`0_G <=_G R_w([x]) = w(x)`, so `w(x) in G_+`. (⇐) If every `w(x) in G_+` and `e <=_E e'`, write `e' = e + d`,
`d = sum_j m_j [x_j]`, `m_j in N_0`. Then `R_w(e') = R_w(e) + sum_j m_j w(x_j)`; each `w(x_j) in G_+`, `G_+` is
closed under `N_0`-scaling and addition, so the sum is in `G_+`, and translation invariance gives
`R_w(e) <=_G R_w(e')`. ∎

**Corollary (failure witness).** If some `w(x_0) <_G 0_G`, the pair `(0_E, [x_0])` witnesses
non-monotonicity: `0_E <=_E [x_0]` while `R_w([x_0]) = w(x_0) <_G 0_G = R_w(0_E)`.

*Certificate (Block A1/A2).* Theorem M is checked **exhaustively** over all weight patterns in `{-1,0,1}^{k·n}`
for `G = Z` (27 patterns) and `G = Z^2` (729 patterns), 0 mismatches, and by 20000 randomized trials
confirming the canonical witness `(0_E, [x_0])` alone controls the iff.

---

## 3. Part P -- the provenance layer is always monotone (unconditional)

**Theorem P.** For every weight `w : X -> G`, `Prov_w` is order-preserving.

*Proof.* `w_+, w_- : X -> G_+`, so by Theorem M (⇐) both `R_{w_+}` and `R_{w_-}` are monotone; hence each
coordinate of `Prov_w` is monotone, i.e. `Prov_w` is monotone for the product order. ∎

**Proposition (minimality).** Among all splits `(a, b)` with `a, b : X -> G_+` and `a - b = w`, the Jordan-Hahn
split `(w_+, w_-)` is the pointwise least in both coordinates: any other split has `a(x) >=_G w_+(x)` and
`b(x) >=_G w_-(x)`.

*Proof.* `a - b = w = w_+ - w_-` gives `a - w_+ = b - w_- =: s`. In a lattice-ordered group, `a >= w` and
`a >= 0` force `a >= w ∨ 0 = w_+`, so `s = a - w_+ >= 0`, whence `b = w_- + s >= w_-`. ∎

*Certificate (Block A3/A4).* Theorem P and minimality are checked over 20000 + 5000 randomized trials, 0
failures.

---

## 4. Part C -- the boundary (coexistence, unconditional)

**Theorem C.** The readout `r(p, n) = p - n` is monotone in `p` and anti-monotone in `n`. Hence for
`R_w = r ∘ Prov_w`:

1. `Prov_w` is monotone for **every** `w` (Theorem P);
2. `R_w` is monotone **iff** `w_- ≡ 0` (Theorem M);
3. whenever some `w(x_0) <_G 0`, one has **simultaneously** monotone provenance and non-monotone readout, and
   the transition occurs **exactly** at `w_- = 0`.

*Proof.* `r(p + d, n) = r(p, n) + d >= r(p, n)` for `d in G_+`; `r(p, n + d) = r(p, n) - d <= r(p, n)`. Items
(1), (2) are Theorems P, M. For (3): if `w(x_0) < 0`, the pair `(0_E, [x_0])` has
`Prov_w(0_E) = (0, 0) <= (w_+(x_0), w_-(x_0)) = Prov_w([x_0])` (monotone provenance) while
`R_w([x_0]) = w(x_0) < 0 = R_w(0_E)` (non-monotone readout). ∎

This is the structural content of the boundary theorem: non-monotonicity of a signed accumulator is **entirely
localized in the readout subtraction** `p - n`; the provenance layer never loses monotonicity, and the negative
cone `w_-` is a complete obstruction invariant.

*Certificate (Block A3).* The coexistence dichotomy (readout non-monotone iff `w_- != 0`) is verified over
20000 randomized trials, 0 failures.

---

## 5. Part Z (finite / compact) -- integer index and topological protection, UNCONDITIONAL

Parts M, P, C are pure order-algebra. Part Z asks, for `G = Z`: is the readout integer a **topologically
protected** invariant, stable under deformation? On a **finite** (equivalently compact) space this is fully
rigorous with elementary spectral flow, **with no non-compact functional analysis.** We instantiate it with a
canonical, GU-free physical operator -- the **Ginsparg-Wilson (overlap) Dirac operator** -- so the readout
integer is literally a lattice axial charge.

### 5.1 Finite Ginsparg-Wilson data

Work in a finite-dimensional chiral space `C^N`, `N` even, with chirality
`gamma5 = diag(+1_{n_+}, -1_{n_-})`, `n_+ = n_- = N/2` (so `Tr gamma5 = 0`). Let `H` be any Hermitian matrix
with no zero eigenvalue and set the **sign operator**

```
eps = sign(H) = H (H^2)^{-1/2},    eps = eps^dagger,    eps^2 = 1.
```

Define the overlap Dirac operator (spacing `a > 0`): `D = a^{-1}(1 + gamma5 * eps)`.

**Lemma (GW relation, exact).** `gamma5 D + D gamma5 = a D gamma5 D`. *Proof.* With `eps^2 = 1`,
`(1 + gamma5 eps) gamma5 (1 + gamma5 eps) = 2 gamma5 + eps + gamma5 eps gamma5 = a^2 D gamma5 D`, and
`gamma5 D + D gamma5 = a^{-1}(2 gamma5 + eps + gamma5 eps gamma5)`; equal. ∎

**Lemma (modified chirality).** `gamma-hat_5 := gamma5(1 - a D) = -eps`, so `gamma-hat_5^dagger = gamma-hat_5`
and `gamma-hat_5^2 = 1`.

### 5.2 The integer axial charge and its three faces

Define the **axial charge / index**

```
Q(H) := -\tfrac12 Tr(eps) = -\tfrac{a}{2} Tr(gamma5 D) = \tfrac12 Tr(gamma-hat_5).
```

All three expressions agree (the two lemmas plus `Tr gamma5 = 0`). Since `eps` has eigenvalues `+-1` and `N`
is even, `Tr(eps) = n_+^H - n_-^H` is an even integer, so **`Q(H) in Z`** -- unconditionally, at finite lattice
spacing. When `H` is chosen so that `D` has exact zero modes, `Q` equals their signed chirality count
`n_+ - n_-` (the Ginsparg-Wilson / Hasenfratz-Laliena-Niedermayer index theorem); this is the lattice axial
charge `Q_A`.

*Certificate (Block B).* For a generic `gamma5`-Hermitian random `H`, the GW relation holds to `7.2e-15`,
`gamma-hat_5^2 = 1`, and the three routes for `Q` agree. For an **engineered** `H` with 2 right-handed and 3
left-handed chiral zero-mode seeds, `D` has exactly 5 zero modes with chirality `n_+ = 2`, `n_- = 3`, giving
`Q = n_+ - n_- = -1 = -\tfrac12 Tr eps` (all routes agree). The value `-1` is whatever the explicit
construction yields; **no target is imposed.**

### 5.3 Signed-readout coexistence, physically

Assign weight `+1` to a right-handed zero mode and `-1` to a left-handed one. Provenance `(n_+, n_-)` is
monotone as modes accumulate; the readout `Q_A = n_+ - n_-` is non-monotone. Adding one left-handed mode moves
provenance `(2, 3) -> (2, 4)` (up in both coordinates) while `Q_A: -1 -> -2` (down). This is a **GU-independent
physical realization of Theorem C**: Ginsparg-Wilson lattice fermions are exactly the "monotone provenance,
non-monotone readout" phenomenon.

### 5.4 Topological protection = finite-dimensional Atiyah-Janich

**Theorem Z (finite).** Along any continuous path `t -> H(t)` of Hermitian matrices, `Q(H(t))` is
integer-valued and **locally constant off the codimension-1 locus where `H(t)` acquires a zero eigenvalue**;
across a simple crossing it jumps by exactly `+-1` (spectral flow).

*Proof.* `Q(H) = -\tfrac12(\#\text{pos} - \#\text{neg})` eigenvalues; eigenvalues are continuous in `H`, and
the sign count changes only when an eigenvalue passes through 0. A simple crossing flips one sign, changing
`\#\text{pos} - \#\text{neg}` by `+-2`, hence `Q` by `+-1`; between crossings the spectrum stays off 0, so `Q`
is constant. ∎

This is the Atiyah-Janich stability mechanism in the finite-dimensional case, where it is a two-line proof: the
index is the `pi_0`-class of the map `t -> eps(t)` into Hermitian involutions, locally constant because the
invertibility locus is open.

*Certificate (Block B7).* Deform `H(s) = H - sI` across the whole spectrum; `Q(s)` sweeps 12 unit steps (one
per eigenvalue of the `N = 12` system), range `[-6, +6] = [-N/2, +N/2]`, every jump `+-1` located exactly at a
spectral crossing (gap `< 0.05`). Textbook spectral flow, machine-verified.

**Why the fence sits where it does.** Part Z is the place a non-compact `L^2` Atiyah-Janich argument would be
needed for the open-manifold case (OC1, Section 8). This section shows the **topological** content of Part Z --
integrality plus protection -- is **unconditional and elementary on any finite / compact space**, realized by a
genuine GU-free operator. The remaining non-compact difficulty (Section 8) is purely **analytic** (is a given
non-compact operator Fredholm and continuous?), not topological.

---

## 6. Part K (finite shadow) -- the KSp augmentation, UNCONDITIONAL

**Setup.** Put a quaternionic structure on `C^{2m}`: `J psi = Omega * conj(psi)` with
`Omega = I_m ⊗ (i sigma_y)`, so `J` is antilinear and `J^2 = -1`. An operator `A` is **H-linear (quaternionic /
self-dual)** iff `A J = J A`, equivalently `Omega^{-1} A Omega = conj(A)`.

**Theorem K (finite).** For an H-linear `A`, `ker A` and `coker A` are `J`-invariant; since `J` is antilinear
with `J^2 = -1`, each is even-complex-dimensional (Kramers). Hence `index_C(A)` is even and

```
index_H(A) := index_C(A) / 2 = dim_H ker A - dim_H coker A  in Z
```

is well-defined -- the `KSp^0(pt) = Z` augmentation. Equivalently, all singular values of `A` occur in equal
Kramers pairs.

*Proof.* If `A v = 0` then `A(Jv) = J(A v) = 0`, so `ker A` is `J`-invariant. `J` antilinear with `J^2 = -1`
implies no `J`-invariant subspace is odd-dimensional over `C` (`v` and `Jv` are `C`-independent and span a
`J`-stable plane). Same for `coker A ≅ ker A^dagger`, `A^dagger` being H-linear too. ∎

This is the finite-dimensional shadow of the infinite-dimensional statement
`[X, Fred_H(K_H)] = KSp^0(X) = KO^{-4}(X)` (the Atiyah-Singer skew-adjoint / quaternionic Fredholm
classification), capturing the augmentation `KSp^0(X) -> KSp^0(pt) = Z` with nothing beyond linear algebra.

*Certificate (Block C).* `J^2 = -1` verified; over 200 random H-linear operators, self-duality holds, singular
values are Kramers-paired, and every engineered rank-deficient H-linear operator has even complex kernel.

---

## 7. The complete standalone theorem (as stated)

Assembling Sections 2-6 into one statement, all hypotheses explicit:

> **Signed-Readout Boundary Theorem (self-contained form).**
> Let `X` be a nonempty set, `E = N_0^{(X)}` with the information order, `G` a lattice-ordered abelian group,
> `w : X -> G` a weight with signed readout `R_w`, Jordan-Hahn split `(w_+, w_-)`, provenance `Prov_w`, and
> readout `r(p, n) = p - n`. Then:
> - **(M)** `R_w` is monotone iff `w(x) in G_+` for all `x`;
> - **(P)** `Prov_w` is monotone for every `w`;
> - **(C)** `R_w = r ∘ Prov_w`, `r` monotone in `p` and anti-monotone in `n`, so monotone provenance coexists
>   with non-monotone readout exactly when `w_- != 0`.
> Moreover, if `G = Z` and the weight data are realized by a **finite** Ginsparg-Wilson operator
> `D = a^{-1}(1 + gamma5 eps)` (`eps^2 = 1`, `gamma5^2 = 1`, `Tr gamma5 = 0`), then:
> - **(Z)** `Q = -\tfrac12 Tr eps in Z` is the axial charge, equal to the signed chirality of the zero modes,
>   locally constant under deformations off the codimension-1 spectral-crossing locus and jumping by `+-1`
>   across a simple crossing;
> - **(K)** if in addition `D` is H-linear for a quaternionic structure `J`, then `Q` is even and
>   `Q / 2 = index_H` is the `KSp^0(pt) = Z` augmentation.

Every clause is proved above and machine-certified. This is a complete theorem a referee can check; it never
mentions Geometric Unity or any physical constant.

### 7.1 Two non-GU instances

The theorem is not about any one model. Two independent instances, neither of which is Geometric Unity:

- **Instance I (finite Ginsparg-Wilson lattice).** `G = Z`; `X` = the chiral zero-mode types of an overlap
  Dirac operator on a finite lattice; `w = +1` on right-handed, `-1` on left-handed modes. `R_w` is the axial
  charge `Q_A`; Parts Z, K apply verbatim (Section 5). This is a standard object of lattice gauge theory,
  entirely GU-free.
- **Instance II (abstract signed accumulators).** `G` any lattice-ordered abelian group; `X` = any set of
  event types; `w` any signed weighting. `E = N_0^{(X)}` tallies how many events of each type have occurred;
  `Prov_w` records the running positive and negative totals separately; `R_w` is the net score. Parts M, P, C
  apply verbatim. Concrete realizations: a ledger with credits and debits (`G = Z` or `R`); a multi-currency
  balance (`G = Z^n`); any additive scoring rule that can subtract. Here the theorem says the net score can go
  down as evidence accumulates **iff** some event type carries a negative weight, and the separated
  positive/negative provenance is always monotone.

Neither instance references GU, `chi(K3)`, or the numbers 24 / 8 / 3.

---

## 8. The two labeled hypotheses for the NON-COMPACT case (honest fence)

The **only** place the theorem does not apply verbatim is when one wants Parts Z / K for a genuinely
**non-compact** Dirac operator `D_Y` on an open manifold `Y` -- the setting of any continuum index theorem on a
non-compact space. The topological engine of Sections 5-6 is unchanged; what is missing is purely the analytic
input that places `D_Y` into that engine. We state it as two explicit hypotheses and **do not claim to
discharge them.**

- **(OC1) Continuous Fredholm realization.** There is a fixed separable Hilbert space `K` and a continuous map
  `t -> F_t in Fred(K)` (norm / gap topology), where `F_t = D_t(1 + D_t^* D_t)^{-1/2}` is the bounded transform
  of the deformation family, and the path stays in the Fredholm locus (no essential spectrum reaching 0,
  discrete sector transported continuously). **Given OC1, Theorem Z holds for `D_Y` verbatim** by the
  Atiyah-Janich classifying-space theorem (`Fred(K) ≃ Z x BU`), of which Section 5.4 is the
  finite-dimensional case.

- **(OC2) H-linear Fredholm realization.** The same map lands in the quaternionic Fredholm space,
  `t -> F_t in Fred_H(K_H)`, `K_H = L^2(Y, H^r)`, each `F_t` commuting with the quaternionic structure.
  **Given OC2, Theorem K holds for `D_Y` verbatim**, `[F] in [X, Fred_H(K_H)] = KSp^0(X)`, augmenting to
  `index_H in Z`; Section 6 is the finite-dimensional case.

**Where the wall is (plainly).** OC1 and OC2 are **not** topological gaps -- the topology is done (Sections 5,
6, and the classical classifying-space theorems). They are **analytic** facts about a **specific** non-compact
operator: one must prove that `D_Y` (with a chosen Sobolev domain, on the chosen `L^2`) is **Fredholm** with
**closed range** and **finite-dimensional kernel / cokernel**, and that the chosen deformation family is
**norm-continuous in the bounded transform** and **never leaves the Fredholm locus** (the relevant discrete
sector must persist). For an open manifold this does **not** follow from ellipticity alone; it requires control
at infinity (invertibility of the asymptotic operator, a spectral gap, or a Callias / relative-index
mechanism). This paper does not carry out that analysis, and to the best of our knowledge it is genuinely open
for the operators that motivate it. Clearing it would require: (i) an explicit Sobolev domain and self-adjoint
extension for `D_Y`; (ii) a spectral gap / invertibility at infinity giving Fredholmness on the relevant
sector; (iii) gap-continuity of the allowed deformations.

The theorem is therefore stated in two tiers: **unconditional** (Sections 2-7, abstract core + finite / compact
Z / K) and **conditional on OC1 / OC2** (the non-compact application). No status of the non-compact case is
promoted here.

---

## 9. What is NOT claimed

- **Not** claimed: that Parts Z / K hold for any non-compact Dirac operator. That is conditional on OC1 / OC2,
  which are stated but not discharged (Section 8).
- **Not** claimed: anything about a physical generation count, `chi(K3)`, the Standard-Model spectrum, or the
  numbers 24 / 8 / 3. This paper is deliberately independent of all of them; none appears as an input, target,
  or normalization. The certificate's integers (`Q = -1`, the range `[-6, 6]`, the 5 zero modes) are whatever
  the explicitly constructed matrices produce, not chosen to match any constant.
- **Not** claimed: novelty for the individual ingredients. The Krein / lattice-ordered decomposition, GW index
  theory, and quaternionic Fredholm classification are classical (Section 10). The contribution is the
  **assembly** and the single sign invariant, plus the explicit compact / non-compact fence.
- **Not** claimed: external validation. Every check is **internal-tier** -- computed, re-run, and adversarially
  reviewed within one AI-directed process; no result has been independently replicated or peer-reviewed.
- **Not** claimed: physics. "Certificate passes" means the stated algebraic and numeric identities hold on the
  constructed finite examples, not that any physical theory is correct.

**Falsification conditions.** The theorem is falsified by any of: `E` not free commutative (a relation
`[x] = 0_E` collapses the (⇒) witness); `G` not lattice-ordered (`w ∨ 0` undefined); order not
translation-invariant (Theorem M (⇐) fails); `w` not single-valued (`R_w` ill-defined); the information order
replaced by an external order in which `0_E <=_E [x]` can fail (then M is necessary, not sufficient); the
GW / overlap structure broken with `eps^2 != 1` (Part Z integrality fails); an operator only `C`-linear, not
`H`-linear (Part K index need not be even); or OC1 / OC2 failing (`D_Y` not Fredholm, 0 in essential spectrum,
or discrete sector not transported -- then Parts Z / K do not apply to `D_Y`, the open case fenced in
Section 8).

---

## 10. Relation to prior art

The pieces are classical; we concede each and claim only the assembly.

- **Ordered algebra / Jordan-Hahn.** The positive/negative decomposition of a signed measure or a
  lattice-ordered group element (`w = w_+ - w_-`) is the Jordan-Hahn decomposition; its minimality and the
  translation-invariance arguments are standard `l`-group theory (Birkhoff). Parts M, P, C are elementary
  consequences; we claim no novelty for the decomposition itself, only for its packaging as a monotone
  provenance layer with the negative cone as a complete obstruction invariant.
- **Krein-space graph argument.** The "maximal definite subspace of an indefinite form is a graph, hence
  balanced" mechanism underlying the coexistence picture is classical Krein-space / indefinite-metric linear
  algebra (Bognar; Azizov-Iokhvidov). No novelty is claimed for it.
- **Ginsparg-Wilson / overlap index.** The GW relation, the overlap operator `D = a^{-1}(1 + gamma5 eps)`,
  `gamma-hat_5 = gamma5(1 - aD)`, and the index `Q = -\tfrac12 Tr eps` are due to Ginsparg-Wilson, Neuberger,
  and Hasenfratz-Laliena-Niedermayer; the finite-dimensional spectral-flow protection is the standard
  Atiyah-Janich mechanism. We reproduce, not extend, these.
- **Quaternionic Fredholm / KSp.** The even-index (Kramers) property of H-linear operators and the
  `KSp^0(pt) = Z` augmentation are Atiyah-Singer skew-adjoint K-theory. Part K is their finite-dimensional
  shadow.

**Our narrow contribution.** The assembly: one boundary theorem in which (i) the monotonicity failure of a
signed readout is pinned to a single sign invariant (the negative cone), (ii) that invariant's integer
enhancement is a topologically protected index on compact spaces, realized by a concrete GU-free operator,
and (iii) the compact-to-non-compact gap is fenced explicitly as OC1 / OC2 rather than glossed. We have not
searched exhaustively for prior statements of exactly this assembly; the ingredients are certainly known.

---

## 11. Reproducibility appendix

The certificate `tests/big-swing/R3_signed_readout_certificate.py` verifies every algebraic and numeric claim.
Run:

```
cd C:/Users/joe/JB/CapacityOS/repos/public/gu-formalization
python tests/big-swing/R3_signed_readout_certificate.py
```

Result on this machine: **22/22 checks PASS, exit 0** (re-run 2026-07-03). Highlights:

- **Block A (Parts M, P, C).** Theorem M exhaustive over 27 (`G = Z`) and 729 (`G = Z^2`) weight patterns, 0
  mismatches; the `(0_E, [x_0])` witness over 20000 trials; provenance monotonicity, the coexistence
  dichotomy, and Jordan-Hahn minimality over 45000 randomized trials, 0 failures.
- **Block B (Part Z, finite GW).** GW relation exact to `7.2e-15`; `gamma-hat_5^2 = 1`; three index routes
  agree; engineered `Q = -1 = n_+ - n_-` with 5 exact zero modes; coexistence witness `(2,3) -> (2,4)`,
  `Q: -1 -> -2`; topological protection with 12 spectral crossings sweeping `Q in [-6, +6]`, every jump `+-1`
  at a zero-crossing.
- **Block C (Part K, KSp).** `J^2 = -1`; 200 H-linear operators Kramers-paired; even complex kernels.

No number in the certificate is a target import: `Q = -1`, the range `[-6, 6]`, and the 5 zero modes are all
determined by the explicitly constructed matrices, not chosen to match any physical constant.

**Provenance.** Full proofs and the OC1 / OC2 fence:
`explorations/big-swing-2026-07-03/R3-signed-readout-standalone-theorem.md`. Canonical (citable) spine:
`canon/signed-readout-boundary-theorem-RESULTS.md`.

**Verification status.** By the project's three-tier vocabulary, every result here is at most **internally
established**: computed, re-run, and adversarially reviewed **within the same AI-directed process** that
produced it (reproduced, not replicated). No result is externally established -- independently replicated,
peer-reviewed, or signed off by a named specialist. The V3 -> V4 crossing (independent replication or a
Lean / Coq port) is the outstanding tier upgrade. Publication is **DEFERRED** pending Joe's review; nothing is
submitted.

---

## 12. Conclusion

We proved a small, self-contained boundary theorem for signed accumulators. Its abstract core (Parts M, P, C)
is unconditional and elementary: a signed readout loses monotonicity **exactly** when some weight is negative,
while the separated positive/negative provenance is **always** monotone -- the negative cone is a complete
obstruction invariant. Enhancing the codomain to `Z`, the readout integer becomes a **topologically protected
index** on finite / compact spaces (Part Z), realized concretely and GU-freely by the Ginsparg-Wilson overlap
Dirac operator, and it acquires a quaternionic `KSp^0(pt) = Z` augmentation when the operator is H-linear
(Part K); both are proved and machine-certified (22/22, exit 0). The single genuinely open piece is the
extension to a **non-compact** Dirac operator, which is not topological but analytic, and which we fence
honestly as two labeled hypotheses OC1 / OC2 that we do not discharge. The theorem is complete as stated:
unconditional in the compact / finite tier, conditional-on-OC1 / OC2 in the non-compact tier. This is an
internal-tier draft; independent external replication is requested and is the outstanding step.
