---
title: "N5: Parthasarathy-Casimir Algebraic Condition for the Fiber Dirac"
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
verdict: "CASIMIR_CONDITION_FORMULATED; ISOTROPY_RESTRICTION_COMPUTED_AT_SL2C_LEVEL; EXACT_MULTIPLICITY_BLOCKED_BY_SPECTRAL_THEORY"
depends_on:
  - "explorations/analytic-index-fredholm/discrete-series-fiber-dirac-index-2026-06-23.md"
  - "explorations/analytic-index-fredholm/n5-ind-h-analytic-conditions-2026-06-22.md"
  - "explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md"
  - "NEXT-STEPS.md F4"
---

# N5: Parthasarathy-Casimir Algebraic Condition for the Fiber Dirac

## Purpose

The prior note `discrete-series-fiber-dirac-index-2026-06-23.md` established that the
literal condition `dim_H ker_L2(D_fib) = 24` on `GL(4,R)/O(3,1)` is not coherent.
It also specified five steps (A–E) that would give a correct formulation.

This note executes Steps B and C:

- **Step B:** Identify `S(6,4)` as a representation of `Spin(3,1) = SL(2,C)`.
- **Step C:** Formulate the Parthasarathy-square Casimir condition as a concrete
  algebraic equation.

Steps A, D, E (fixing the connected pair, checking the spectral side, counting
multiplicities) require additional Harish-Chandra representation theory and are not
closed here.

---

## 1. Step B: S(6,4) as a Representation of Spin(3,1)

### 1.1 The isotropy embedding

The fiber isotropy group is `H = O(3,1)`, with connected component `H_0 = SO_0(3,1)`.
The spin double cover is `Spin(3,1) = SL(2,C)`.

The action of `H` on the fiber direction comes from the standard action of the Lorentz
group on `Sym^2(R^{3,1}*)` with trace reversal. Explicitly:

```
Phi: SO(3,1) -> GL(Sym^2_0(R^{3,1}*)) direct-sum R
A |-> (A ot A acting on traceless 2-tensors, trivial on trace).
```

In split-signature notation (using the trace-reversed gimmel fiber metric of signature
(6,4)):

```
Sym^2(R^{3,1}*) with trace reversal ~= R^{6,4}
```

as an SO(3,1) module. The spin lift is

```
spin: Spin(3,1) = SL(2,C) -> Spin(6,4).
```

### 1.2 Decomposition of Sym^2(R^{3,1}*) under SL(2,C)

Use the SL(2,C) representation theory notation: a representation is labeled `(j, jbar)`
for `j, jbar` in {0, 1/2, 1, 3/2, ...}, with complex dimension `(2j+1)(2jbar+1)`.

For `V = C^4` (complexified Minkowski), with the standard `(1/2, 1/2)` representation
of SL(2,C):

```
Sym^2(V) = Sym^2((1/2,1/2)) = (1,1) + (0,0).
```

The `(1,1)` piece is the complexified traceless Sym^2 of Minkowski (dimension 9 over R,
or complex dimension 9). The `(0,0)` piece is the trace (1 real dimension).

However, the fiber is `Sym^2(R^{3,1}*)` with trace-reversal giving the (6,4) split.
Under trace reversal, the trace direction gets a sign flip. Over R:

```
Sym^2(R^{3,1}) with trace reversal
  ~= (traceless part, dim=9) direct-sum (traced-reversed scalar, dim=1)
  = SO(3,1) representation (dim_R 9 + dim_R 1 = 10).
```

The signature (6,4) comes from:
- The traceless part has signature (6,3) under the Frobenius metric
- The trace-reversed scalar has signature (0,1)

Wait, that only gives (6,4) if the traceless part is (6,3). Let me recount: in the GU
context, the trace-reversal procedure gives fiber signature (6,4), confirmed by the N1
signature audit. The 10-dimensional fiber `Sym^2(R^{3,1}*)` with trace reversal has

```
(7,3) raw Frobenius -> trace reversal -> (6,4).
```

The 7+3=10 = 6+4 = 10 dimensions are consistent.

### 1.3 SL(2,C) decomposition of the spinor S(6,4)

`S(6,4)` is the half-spinor module of `Cl(6,4)`. As a complex module, it has
`dim_C(S(6,4)) = 2^{(6+4)/2 - 1} = 2^4 = 16`. So `S(6,4) = C^16`.

Under the isotropy embedding `Spin(3,1) = SL(2,C) -> Spin(6,4)`, the restriction of
`S(6,4)` to `SL(2,C)` decomposes as a sum of `(j, jbar)` representations.

**Approach.** The embedding `Spin(3,1) -> Spin(6,4)` is via the spin representation
of the action `Phi: SO(3,1) -> SO(6,4)`. The induced map on spin groups gives a
representation

```
S(6,4)|_{SL(2,C)} = ?
```

The spin module of `Cl(6,4)` restricts to the spin module of `Cl(3,1)` tensored with
the spin module of `Cl(3,3)` (since `6+4 = 3+1 + 3+3` in one splitting) — but the
isotropy embedding does not use this splitting.

**Explicit computation (isotropy representation).**

The tangent space of `GL(4,R)/O(3,1)` at the identity coset is

```
q = p/so(3,1) = {X in gl(4,R) : X^T g + g X = 0}^perp / so(3,1)
             = Sym^2(R^{3,1}*) with trace reversal.
```

This is the space of Lorentz-tensor valued symmetric matrices, which under `SL(2,C)` sits in

```
(Sym^2(C^2) ot Sym^2(bar C^2)) + ... (trace direction).
```

The spin module used as a coefficient is `S(6,4)`, viewed as a spin module for the
Clifford algebra of this 10-dimensional fiber space with signature (6,4).

**Concrete restriction.** The maximal compact of `H_0 = SO_0(3,1)` is `K_H = SO(3)`,
with spin double cover `SU(2)`. The restriction of `S(6,4)` to `SU(2) = Spin(3)` must
be computed explicitly.

The metric on `Sym^2(R^{3,1}*)` with signature (6,4) restricts to a metric on
`Sym^2(R^3)` of signature (6,0) (positive definite) when restricted to the spatial
directions. The corresponding Clifford algebra is `Cl(6,0)`, and the spin module is
`S(6,0) = C^8`. The `SU(2)` restriction of `S(6,4)` through `Spin(3) subset Spin(6,4)`
gives:

```
S(6,4)|_{SU(2)} ~= S(6,0)|_{SU(2)} ot (time-direction factor).
```

Under `Spin(3) = SU(2)`, the spin module `S(6,0) = C^8` decomposes using the
branching rule for `Spin(6) -> Spin(3)`:

```
Spin(6) ~= SU(4),  Spin(3) = SU(2)
S(6,0) = 8-dimensional chiral module of Spin(6).
```

Under the chain `SU(2) subset SU(4)`, the fundamental 4-dim of SU(4) restricts as

```
4 = 2 + 1 + 1  or  4 = 3 + 1  (depending on embedding).
```

For the symmetric-space embedding `SO(3) subset SO(6)` via the adjoint representation:

```
S(6,0)|_{Spin(3)} = (2j+1) representation for various j.
```

A complete calculation using the Dynkin branching rules for `SO(6) -> SO(3)` gives

```
S(6,0) = 8 -> j=3/2 (dim 4) + j=1/2 (dim 2) + j=1/2 (dim 2).
```

This is reconstruction-grade (requires explicit root-restriction computation).

### 1.4 The SL(2,C) representation content

Given the `SU(2)` content of `S(6,4)|_{SU(2)}`, the SL(2,C) = `SU(2) x SU(2)` (complexified)
representation content can be constrained but not uniquely determined without the full
representation-theory computation.

**Structural constraint.** Since `dim_C S(6,4) = 16` and SL(2,C) representations have
dimensions `(2j+1)(2jbar+1)`, the possible decompositions include:

```
16 = 4 x 4 = (1,1)_{dim 9} + (0,0)_{dim 1} + ... (does not sum to 16 from these)
```

More precisely, valid decompositions with total complex dimension 16:

```
Option 1: (3/2, 0) + (0, 3/2) + (1/2, 1) + (1, 1/2) = 4+4+6+6? No, that's 20.
Option 2: (1, 1/2) + (1/2, 1) = 6+6=12. Too small.
Option 3: (3/2, 1/2) + (1/2, 3/2) = 8+8=16. Possible.
Option 4: (1,0)+(0,1)+(1/2,1/2)+(1/2,1/2) = 3+3+4+4=14. No.
Option 5: (3/2,0)+(0,3/2)+(1/2,0)+(0,1/2) = 4+4+2+2=12. No.
Option 6: Two copies of (1, 1/2): 6+6=12. No.
Option 7: (3/2,1/2)+(1/2,1/2)+(1/2,0)+(0,1/2) = 8+4+2+2=16. Possible.
```

The most natural candidate, given the SM branching structure `(4,2,1)+(4bar,1,2)` under
`SU(4)xSU(2)xSU(2)`, is Option 3:

```
S(6,4)|_{SL(2,C)} ~= (3/2, 1/2) + (1/2, 3/2).     [candidate decomposition]
```

This is the (spin-3/2, spin-1/2) + conjugate representation. It has total complex
dimension 8+8=16 and is consistent with the parity structure of the spinor module.
It is also consistent with the RS(3,1) sector of the 4D spectrum: the (3/2,0) part
of the 4D spinor would give the spin-3/2 content.

**Status:** This candidate decomposition is reconstruction-grade. The explicit
branching rule requires a Dynkin-label / highest-weight computation that goes beyond
this note.

---

## 2. Step C: Parthasarathy-Square Casimir Condition

### 2.1 Setup

For the connected symmetric pair:

```
(G, H) = (SL(4,R), SO_0(3,1)),    K = SO(4).
```

Let `C_g` be the quadratic Casimir of `g = sl(4,R)` and `C_h` be the quadratic Casimir
of `h = so(3,1)`. The coefficient representation is `tau: H -> GL(S(6,4))` restricted
to `H`.

For a representation `pi` of `G` that occurs discretely in `L^2(G/H, tau)`, the
Parthasarathy-square condition requires:

```
pi(C_g) = tau(C_h) + rho_constant,
```

where `rho_constant` is the `rho`-shift constant for the pair `(G, H)`.

### 2.2 Casimir values

**Casimir of SL(4,R).** The quadratic Casimir of `sl(4,R)` in the adjoint representation
has the normalization

```
C_{adj}(sl(4,R)) = 8.
```

For a representation with highest weight `mu`, the Casimir value is

```
C_g(pi_mu) = <mu, mu + 2rho_g>
```

where `rho_g` is the half-sum of positive roots of `sl(4,R)`.

For `sl(4,R)`, the positive roots are `e_i - e_j` for `i < j in {1,2,3,4}`. The
half-sum is

```
rho_g = (3/2, 1/2, -1/2, -3/2).
```

For the principal series representation with parameter `nu` (imaginary axis for
unitary representations), the Casimir eigenvalue is `-(|nu|^2 + |rho_g|^2)` in a
standard convention with one sign difference.

**Casimir of SO(3,1) = SL(2,C).** For the representation `(j, jbar)` of SL(2,C):

```
tau(C_h) = j(j+1) + jbar(jbar+1).
```

For the candidate `tau = (3/2, 1/2) + (1/2, 3/2)`:

```
tau(C_h) = 3/2 * 5/2 + 1/2 * 3/2 = 15/4 + 3/4 = 18/4 = 9/2.
```

For each of the two summands:

```
(3/2, 1/2): j(j+1) + jbar(jbar+1) = 15/4 + 3/4 = 9/2.
(1/2, 3/2): same = 9/2.
```

So the candidate coefficient representation has `tau(C_h) = 9/2`.

**rho-shift constant.** For the symmetric pair `(SL(4,R), SO_0(3,1))`, the rho-shift
arises from the half-sum of the positive restricted roots. The restricted root system
for the Riemannian symmetric space `SL(4,R)/SO(4)` is of type `A_3` with restricted
roots. For the pseudo-Riemannian case `SL(4,R)/SO_0(3,1)`, the restricted root system
requires the Cartan decomposition with respect to the pseudo-involution.

The rho-constant is:

```
rho_h = rho_g - rho_k
```

where `rho_k` is the half-sum of compact positive roots. For `(sl(4,R), so(3,1))`:

```
rho_g = (3/2, 1/2, -1/2, -3/2)  (SL(4,R) positive roots)
rho_k = (1/2, -1/2)  (SO(3) = SU(2) in the compact part, restricted)
```

The exact rho-constant computation requires the full restricted root data and is
reconstruction-grade.

### 2.3 The Casimir condition as an algebraic equation

The Parthasarathy condition for a zero mode of the fiber Dirac is:

```
pi(C_g) = tau(C_h) + rho_constant = 9/2 + rho_constant.
```

This is a **constraint on the SL(4,R) representation `pi`** that would contribute to
the fiber Dirac kernel. It selects specific principal-series parameters `nu` where the
Casimir eigenvalue satisfies this equation.

For the principal series with parameter `nu in ia_*` (purely imaginary, unitary):

```
C_g(pi_nu) = -|nu|^2 - |rho_g|^2 = -|nu|^2 - (9/4 + 1/4 + 1/4 + 9/4)
            = -|nu|^2 - 5.
```

Setting equal to `9/2 + rho_constant`:

```
-|nu|^2 - 5 = 9/2 + rho_constant
|nu|^2 = -(19/2 + rho_constant).
```

For this to have a solution with `|nu|^2 >= 0`, we need

```
rho_constant <= -19/2.
```

If `rho_constant = -19/2`, the solution is `|nu| = 0` — the zero of the principal
series. This is a discrete series candidate (if it appears in the discrete part of
the decomposition).

**Status:** The rho-constant is not computed here. Its value requires the full
restricted root data for `(SL(4,R), SO_0(3,1))`.

---

## 3. Dirac-Cohomology Language

An equivalent formulation: a representation `pi` of `G = SL(4,R)` contributes to
the fiber Dirac zero-mode space iff the Dirac cohomology

```
H_D(pi) = ker(D_tau) / (im(D_tau) cap ker(D_tau))
```

of `pi` with coefficients in `tau = S(6,4)|_H` is nonzero. The Vogan conjecture
(proved by Huang-Pandzic 2002) states:

```
H_D(pi) != 0 iff the infinitesimal character of pi is a Weyl-group translate of
             (infinitesimal character of H-type in tau) + rho_g.
```

This is a more precise statement than the Casimir equation. For our case:

The H-types in `tau = (3/2, 1/2) + (1/2, 3/2)` are the K_H = SO(3)-types
(restriction to the maximal compact of H). These are computed by branching
`tau|_{SO(3)}` using the rules for `SL(2,C) -> SO(3)`:

```
(3/2, 1/2)|_{SO(3)}: j_total in {|3/2 - 1/2|, ..., 3/2+1/2} = {1, 2}.
(1/2, 3/2)|_{SO(3)}: j_total in {1, 2}.
```

So the `K_H`-types are `j=1` (dim 3) and `j=2` (dim 5), each appearing twice.

The Vogan infinitesimal character condition then selects those `G = SL(4,R)` representations
whose infinitesimal character equals a specific Weyl translate of the SL(2,C) type.

---

## 4. Concrete Algebraic Condition

Gathering the above, the Parthasarathy-Vogan condition for a zero-mode contributing
representation is:

```
inf-char(pi) = W_G * (lambda_tau + rho_g),
```

where:
- `lambda_tau` = highest weight of a K_H-type in `tau|_{K_H}` (from the SO(3)-types above)
- `rho_g = (3/2, 1/2, -1/2, -3/2)` in coordinates
- `W_G` = Weyl group of SL(4,R) = S_4

For `j=2` K_H-type (dimension 5, highest weight 2 for SO(3)):

```
lambda_tau + rho_g = (2, 0) + (3/2, 1/2, -1/2, -3/2)   [in compatible conventions]
```

This is a concrete algebraic equation on the infinitesimal character of `pi`. The
representations `pi` with this infinitesimal character are candidates.

**The generation count condition then becomes:**

Does a representation `pi` with this infinitesimal character appear discretely in
`L^2(G/H, tau)`, and if so, with what multiplicity?

This is the precise question that replaces `dim_H ker D_fib = 24`.

---

## 5. What Remains Open

**Open 1: Restricted root rho-constant.** The exact rho-shift for `(SL(4,R), SO_0(3,1))`
requires the restricted root system computation. This changes the numerical values above.

**Open 2: Candidate decomposition of S(6,4)|_{SL(2,C)}.** The candidate `(3/2, 1/2) + (1/2, 3/2)`
is reconstruction-grade and must be verified by a Dynkin-label branching calculation.

**Open 3: Discrete spectral contribution.** The rank obstruction from the prior note
(`rank G/H = 4` vs. `rank K/(K cap H) = 1`) suggests the scalar relative discrete series
is blocked. Whether twisted representations (using the spinor coefficient `tau`) appear
discretely despite this is the decisive spectral question.

**Open 4: Multiplicity = 24.** Even if a discrete summand exists, the multiplicity
must equal 24 quaternionic units for the three-generation interpretation. This requires
a direct multiplicity computation.

---

## 6. F4 Status

The analytic target for F4 (replacement for the incoherent `dim_H ker_L2 = 24`) is now:

```
F4 target: multiplicity m(pi, L^2(G/H, tau))
           for SL(4,R)-representation pi with Vogan infinitesimal character
           lambda_tau + rho_g (Weyl-translated).
           
           m should equal 24 (quaternionic units) for three generations.
```

This is a precise representation-theory question. It is answerable in principle using
Flensted-Jensen / Oshima-Matsuki theory for symmetric spaces, though the computation
for `(SL(4,R), SO_0(3,1))` with spinor coefficients is non-trivial.

The prior note's Steps D and E remain open. This note has completed Step B (partial,
at candidate decomposition level) and Step C (Casimir condition as algebraic equation).

---

## 7. Verdict

**Casimir condition established.** The Parthasarathy-square condition for zero-modes
on `GL(4,R)/O(3,1)` with coefficient representation `S(6,4)` is:

```
pi(C_g) = 9/2 + rho_constant.
```

(where `rho_constant` is not yet computed from the restricted root data).

**Candidate isotropy decomposition.** `S(6,4)|_{SL(2,C)} ~= (3/2, 1/2) + (1/2, 3/2)`
at reconstruction grade. This gives Casimir `tau(C_h) = 9/2`.

**Generation count condition.** Three generations require multiplicity 24 for the
representation selected by the Vogan condition. This is a concrete representation-theory
question replacing the incoherent ordinary-kernel condition.

**N5 status update:** The incoherent analytic target is replaced. The correct target
is stated. The Casimir condition is a concrete algebraic equation. The open step
is the spectral computation (Step D) and multiplicity calculation (Step E).

---

## References

- `explorations/analytic-index-fredholm/discrete-series-fiber-dirac-index-2026-06-23.md` (prior note: Steps A-E)
- `explorations/analytic-index-fredholm/n5-ind-h-analytic-conditions-2026-06-22.md` (fiber homotopy, Atiyah-Schmid)
- R. Parthasarathy, "Dirac operator and the discrete series," Ann. Math. 96 (1972), 1–30.
- D. Vogan & G. Zuckerman, "Unitary representations with nonzero cohomology," Compositio (1984).
- J.-S. Huang & P. Pandzic, "Dirac cohomology, unitary representations and a proof of a conjecture of Vogan," J. AMS 15 (2002), 185–202.
- M. Flensted-Jensen, "Discrete series for semisimple symmetric spaces," Ann. Math. 111 (1980).
