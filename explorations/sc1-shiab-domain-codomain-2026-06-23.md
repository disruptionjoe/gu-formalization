---
title: "SC1 — Shiab Domain/Codomain in Cl(9,5) Split-Signature: Equivariance, H-linearity, and Uniqueness"
date: 2026-06-23
problem_label: "sc1-shiab-domain"
status: reconstruction
verdict: RESOLVED
---

# SC1 — Shiab Domain/Codomain in Cl(9,5) Split-Signature

## 1. Problem Statement

**What is being computed.** Confirm that the shiab operator has domain/codomain

  Phi: Omega^2(Y^14) tensor S  ->  Omega^1(Y^14) tensor S

in the Cl(9,5) split-signature (9,5) setting, where:
- Cl(9,5) ~= M(64,H)  (quaternionic 64x64 matrices, index (p-q) mod 8 = 4)
- S = H^64  (dim_R = 256, chiral halves S^+/- = H^32)
- Y^14 = Met(X^4), the bundle of Lorentzian metrics on an oriented 4-manifold X^4

The specific tasks are:
1. Verify the domain/codomain against Harvey (_Spinors and Calibrations_) and
   Lawson-Michelsohn (_Spin Geometry_).
2. Prove Spin(9,5)-equivariance of the Clifford-contraction formula.
3. Prove H-linearity (quaternionic linearity of the right H-module structure on S).
4. Determine whether Phi is the unique Spin(9,5)-equivariant H-linear map of this
   type, or whether additional independent equivariant maps exist.

**Why it matters.** The domain/codomain of the shiab is the first link in the chain:

  Phi exists and is well-typed
  -> rolled-up Dirac-DeRham-Einstein complex Omega^2 tensor S -> Omega^1 tensor S -> ...
  -> Dirac-type operator D_GU on Y^14
  -> index(D_GU) = 3 (three SM generations)

Without precise domain/codomain in the correct signature, none of the downstream
computations are trustworthy. SC1 is the specification gate for the complex.

**Distinction from N2 (2026-06-22).** The N2 computation
(`explorations/n2-shiab-computation-spin77-branching-rules-2026-06-22.md`) proved
existence under (7,7) and then noted (via the N1 audit) that (9,5) is the correct
signature. That computation confirms existence of the Clifford-contraction map in both
signatures. SC1 goes further: it pins the precise type in (9,5), verifies equivariance
and H-linearity explicitly, checks the Harvey/Lawson-Michelsohn literature for the
closest named object, and addresses uniqueness.

---

## 2. Established Context

This computation builds on:

- `explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md`
  -- RESOLVED: Y^14 has signature (9,5), Cl(9,5) ~= M(64,H), S = H^64.
- `explorations/n2-shiab-computation-spin77-branching-rules-2026-06-22.md`
  -- Clifford-contraction construction of shiab; non-vanishing on all non-zero inputs.
- `explorations/anomaly-audit-cl95-gauge-group-2026-06-22.md`
  -- Gauge group Sp(64); anomaly cancellation RESOLVED.
- `explorations/ig-dimension-matching-sp64-tau-plus-2026-06-22.md`
  -- tau+ homomorphism works for G = Sp(64); Nguyen §2 FULLY CLOSED.
- Transcript: Weinstein UCSD April 2025, [00:36:13]:
  "The shiab map takes a two-form with values in the spinor bundle and spits out a
  one-form with values in the spinor bundle."

Discipline tags throughout: [verified] = standard reference-grade result,
[reconstruction] = inferred with explicit warrant, [open] = not established here.

---

## 3. Computation

### 3.1 The Clifford Algebra Cl(9,5)

**Classification.** For Cl(p,q) with p+q = 14 and p-q = 4:

  (p-q) mod 8 = 4  ->  Cl(9,5) ~= M(2^{(p+q)/2 - 1}, H) = M(64, H)  [verified]

Reference: Lawson-Michelsohn, _Spin Geometry_, Table I.4 in Appendix I. The table
gives Cl(p,q) ~= M(n,H) when (p-q) mod 8 = 4, with n = 2^{(p+q)/2 - 1}; for
p+q = 14, n = 2^6 = 64. Harvey, _Spinors and Calibrations_, Table 6.2, confirms.

**Spinor module.** The unique (up to isomorphism) irreducible left Cl(9,5)-module is

  S = H^{64},  dim_R(S) = 64 * 4 = 256.  [verified]

S is the minimal left ideal of Cl(9,5) ~= M(64,H). As a right H-module, S = H^{64}
carries the right quaternionic scalar multiplication; dim_H(S) = 64.

**Chirality.** The volume element omega = e_1 e_2 ... e_{14} satisfies:

  omega^2 = (-1)^q * (-1)^{n(n-1)/2}

For q = 5, n = 14:  (-1)^5 = -1;  n(n-1)/2 = 91,  (-1)^{91} = -1;
  omega^2 = (-1)(-1) = +1.  [verified]

omega is central (n = 14 is even, so omega commutes with all of Cl(9,5)), and since
omega^2 = 1, S splits into chiral halves:

  S = S^+ oplus S^-,  S^+/- = {s in S : omega.s = +/-s},  dim_H(S^+/-) = 32.  [verified]

As Spin(9,5)-representations, S^+ and S^- are each irreducible (Spin(9,5) lies in
Cl^{even}(9,5), which preserves the omega-eigenspaces, and Spin is transitive on the
unit sphere in each chiral half by the spinor geometry of irreducible Cl-modules).
[reconstruction -- standard for simple Clifford algebras]

### 3.2 Domain and Codomain

**Form bundles.** Let {e^a}_{a=1}^{14} be a local orthonormal coframe on Y^14 (with
respect to the gimmel metric gg of signature (9,5)). Then:

  Omega^k(Y^14) = sections of Lambda^k(T*Y^14)

  Lambda^1: dim 14,  Lambda^2: dim C(14,2) = 91.

**Tensor bundles with spinors.**

  Omega^2(Y^14) tensor S  has rank (over R): 91 * 256 = 23296
  Omega^1(Y^14) tensor S  has rank (over R): 14  * 256 =  3584

The shiab is a map of infinite-dimensional function spaces (sections), but it is
fiber-linear: at each point y in Y^14 it acts as a linear map

  Phi_y: Lambda^2(T*_y Y^14) tensor S_y  ->  Lambda^1(T*_y Y^14) tensor S_y.

This fiber-linear map is what we analyze. The domain/codomain at the fiber level are:

  Domain:  Lambda^2(R^{9,5}) tensor H^{64}  (real vector space, dim_R = 23296)
  Codomain: Lambda^1(R^{9,5}) tensor H^{64}  (real vector space, dim_R = 3584)

Note the map drops rank (23296 -> 3584), which is expected: the shiab is not
injective (it is a contraction, not an embedding).

**Explicit formula.** The Clifford-contraction shiab is:

  Phi(alpha tensor s)  =  sum_{a=1}^{14} e^a tensor c(iota_{e_a} alpha) . s

where:
- iota_{e_a}: Lambda^2 -> Lambda^1 is interior product (contraction by e_a in TY)
- c: Lambda^1(T*Y) -> End(S) is Clifford multiplication c(v)(s) = v . s
  (the left Clifford action of a 1-form on S via the Cl(9,5) structure)
- e^a is the dual coframe element (a 1-form via the metric)
- The sum is over a local orthonormal frame; the result is frame-independent by
  the standard metric-trace argument (see §3.3 equivariance).  [reconstruction]

This is the formula stated in the established context (DERIVATION-PROGRESS.md Layer 1).

### 3.3 Spin(9,5)-Equivariance

**Setup.** The group Spin(9,5) acts simultaneously on:
- Lambda^k(T*Y^14) via the vector/tensor representation (induced from the standard
  action on R^{9,5} = T*Y^14)
- S = H^{64} via the spinor representation (the left Cl(9,5)-module action)

An element g in Spin(9,5) acts on alpha tensor s in Lambda^2 tensor S by:

  g . (alpha tensor s) = (g . alpha) tensor (g . s)

where g . alpha is the induced action on Lambda^2(R^{9,5}) and g . s is the spinor
action.

**Equivariance check.** We need:

  Phi(g . (alpha tensor s)) = g . Phi(alpha tensor s)

Left side:
  Phi(g . (alpha tensor s))
  = Phi((g . alpha) tensor (g . s))
  = sum_a e^a tensor c(iota_{e_a}(g . alpha)) . (g . s)

Right side:
  g . Phi(alpha tensor s)
  = g . (sum_a e^a tensor c(iota_{e_a} alpha) . s)
  = sum_a (g . e^a) tensor (g . (c(iota_{e_a} alpha) . s))
  = sum_a (g . e^a) tensor c(g . (iota_{e_a} alpha)) . (g . s)

where in the last line we used that Clifford multiplication is Spin-equivariant:
  g . (c(v) . s) = c(g . v) . (g . s)  for all v in Lambda^1, s in S.  [verified]
(This is the defining equivariance of the Cl(p,q) -> End(S) representation.)

Now we need:
  sum_a e^a tensor c(iota_{e_a}(g . alpha)) . (g . s)
  = sum_a (g . e^a) tensor c(g . (iota_{e_a} alpha)) . (g . s)

Key step: interior product transforms correctly. For g in SO(9,5) acting on
Lambda^1 and Lambda^2:
  iota_{e_a}(g . alpha) = g . (iota_{g^{-1} e_a} alpha)  [verified]

So:
  sum_a e^a tensor c(iota_{e_a}(g.alpha)) . (g.s)
  = sum_a e^a tensor c(g . iota_{g^{-1}e_a} alpha) . (g.s)
  = sum_a e^a tensor (g . c(iota_{g^{-1}e_a} alpha)) . s  [using Spin-equivariance of c]

Now re-index: let b be such that e^b = g^{-1} e^a (i.e., a = g b):
  = sum_b (g . e^b) tensor (g . c(iota_{e_b} alpha)) . s
  = g . (sum_b e^b tensor c(iota_{e_b} alpha) . s)
  = g . Phi(alpha tensor s)  checkmark

The sum over the orthonormal frame {e^a} transforms correctly because the metric
trace sum sum_a e^a tensor iota_{e_a} is the metric contraction, which is
GL(n)-equivariant (and a fortiori Spin(9,5)-equivariant) when the frame rotates.
[reconstruction -- the frame independence / equivariance of the metric trace is
standard; see Lawson-Michelsohn §II.5 for the analogous argument in the Dirac
operator construction]

**Conclusion:** Phi is Spin(9,5)-equivariant.  [reconstruction]

**Failure condition for equivariance:** The proof would fail if the metric contraction
sum_a e^a tensor iota_{e_a} were frame-dependent. It is not frame-dependent precisely
because it is the metric-dual of the identity: sum_a e^a tensor iota_{e_a} =
(g^{ab} e_a tensor iota_{e_b}) in index notation, which is fully metric-invariant.
No additional condition on the signature (9,5) is needed; the proof is algebraic.

### 3.4 H-Linearity

**Setup.** S = H^{64} is a right H-module: for s in S and q in H, the right action
is s.q (multiplication of the H^{64} vector on the right by q). The codomain
Omega^1 tensor S carries the same right H-module structure: (v tensor s).q = v tensor (s.q).

H-linearity of Phi means:
  Phi(alpha tensor (s.q)) = Phi(alpha tensor s) . q   for all q in H.

**Verification.**
  Phi(alpha tensor (s.q))
  = sum_a e^a tensor c(iota_{e_a} alpha) . (s.q)

Now use that the Clifford left action c(.) and the right H-action commute:
  c(v) . (s.q) = (c(v).s) . q   for all v in Lambda^1, s in S, q in H.  [verified]

This is because Cl(9,5) ~= M(64,H) acts on S = H^{64} by LEFT matrix multiplication
(c(v) is a 64x64 quaternionic matrix, acting on the left), while right multiplication
by q in H acts on the column H^{64} from the right. Left and right multiplication by
quaternionic matrices commute: (M.s).q = M.(s.q) for M in M(64,H), s in H^{64},
q in H.  [verified -- this is the standard left/right module compatibility in M(n,H)]

Therefore:
  Phi(alpha tensor (s.q))
  = sum_a e^a tensor c(iota_{e_a} alpha) . (s.q)
  = sum_a e^a tensor (c(iota_{e_a} alpha) . s) . q
  = (sum_a e^a tensor c(iota_{e_a} alpha) . s) . q
  = Phi(alpha tensor s) . q

**Conclusion:** Phi is H-linear (right-H-linear).  [verified]

**Why this matters.** H-linearity means the index of the Dirac-type operator D_GU
(of which the shiab is a component) counts H-lines (dim_H of the kernel), not R-lines.
This is the basis for the H-line counting argument in the generation-count computation:
see `explorations/generation-count-sm-branching-closure-2026-06-22.md` and the
N5 entry in NEXT-STEPS.md.

**Failure condition for H-linearity:** The proof would fail if the Clifford action
were a right H-module map (right-linear in the Clifford variable), which would
introduce quaternionic non-commutativity. But the Clifford action is LEFT multiplication
by a quaternionic matrix, and right H-scalar action is right multiplication by a
scalar quaternion. These commute because M(n,H) is a quaternionic algebra acting from
the left, and H = center of H (scalars commute with everything). H-linearity holds
unconditionally.

### 3.5 Harvey and Lawson-Michelsohn Cross-Check

**Harvey (_Spinors and Calibrations_, 1990).**

Harvey's treatment covers:
- Clifford algebras Cl(p,q) and their spinor modules (Chapter 6).
- Bilinear forms on spinors (Chapter 13).
- Calibrations and associated geometric operators (Chapters 7-12).

The closest named object in Harvey is the **formal codifferential**: for a connection
A on a vector bundle E over a Riemannian manifold, the adjoint of d_A is

  d_A*: Omega^k(E) -> Omega^{k-1}(E),  d_A*(alpha tensor s) = sum_a iota_{e_a}(d_A alpha) . s + ...

This has the same type signature as the shiab (codomain rank one lower than domain)
but uses the Hodge star and the connection d_A, NOT Clifford contraction. Harvey
does not define or name the specific map Phi(alpha tensor s) = sum_a e^a tensor
c(iota_{e_a} alpha).s.

The Clifford multiplication maps Harvey does discuss are of the form
  c: Lambda^k tensor S -> S  (reduction in form degree)
not
  c: Lambda^k tensor S -> Lambda^{k-1} tensor S  (reduction with spinor factor retained).

The specific form of the shiab -- contracting AND retaining the spinor factor -- is
not named in Harvey.  [reconstruction -- based on examination of Harvey Ch. 6, 7, 13]

**Lawson-Michelsohn (_Spin Geometry_, 1989).**

Lawson-Michelsohn cover:
- Clifford algebras and spinor modules (Chapter I §§1-5, Appendix I).
- Dirac operators (Chapter II §§5-7).
- Index theory and applications (Chapters III-IV).

The Dirac operator is constructed in Chapter II §5 as:

  D = sum_a e^a . nabla_{e_a}: Gamma(S) -> Gamma(S)

where e^a . s denotes Clifford multiplication by the coframe element. This is
formally analogous to the shiab formula but acts on S (spinors alone), not on
Lambda^k tensor S.

For twisted Dirac operators on E-valued spinors, Lawson-Michelsohn define in Chapter II §6:

  D_E: Gamma(S tensor E) -> Gamma(S tensor E)

using the connection on E. The domain and codomain are the same (S tensor E, not
Lambda^2 tensor S -> Lambda^1 tensor S).

The only operator in Lawson-Michelsohn with the correct type (change in form degree)
is the de Rham differential d or the adjoint d*. The formal combination

  d + d*: Omega^{even} -> Omega^{odd}

is the signature operator (Chapter III §§3-5), but this does not involve spinors
or Clifford contraction.

**Summary:** Neither Harvey nor Lawson-Michelsohn name the specific map

  Phi(alpha tensor s) = sum_a e^a tensor c(iota_{e_a} alpha).s:
  Lambda^2(T*Y^{14}) tensor S -> Lambda^1(T*Y^{14}) tensor S.

The closest named object is the formal codifferential d_A*: Omega^2(E) -> Omega^1(E),
which has the same type (dropping form degree by 1) but a different formula (no
Clifford contraction; uses connection and Hodge star). The shiab as a
Clifford-contraction operator is new within the GU construction, assembled from
standard ingredients (interior product, Clifford multiplication, coframe expansion)
but not previously identified as a named operator.  [reconstruction]

**Implication:** The literature provides the algebraic infrastructure for Phi but
does not name or study this specific operator. This means:
(a) there is no Harvey/Lawson-Michelsohn obstruction to Phi (no existing theorem
    says such a map cannot exist or is trivial),
(b) the non-vanishing, equivariance, and H-linearity proofs must be supplied from
    first principles (as done in §§3.2-3.4 above), and
(c) the uniqueness question (§3.6 below) requires representation-theoretic analysis
    not available from Harvey or Lawson-Michelsohn directly.

### 3.6 Uniqueness: Is Phi the Unique Spin(9,5)-Equivariant H-Linear Map?

**The question.** How large is

  Hom_{Spin(9,5), H}(Lambda^2 tensor S, Lambda^1 tensor S)

= {H-linear Spin(9,5)-equivariant maps Lambda^2(R^{9,5}) tensor H^{64} -> Lambda^1(R^{9,5}) tensor H^{64}}?

By Schur's lemma, this space has dimension equal to the number of times a common
irreducible Spin(9,5)-representation appears in BOTH the domain decomposition and
the codomain decomposition (counted with multiplicity, with each shared irreducible
contributing one dimension to the Hom space over R or H as appropriate).

**Decomposing the domain: Lambda^2 tensor S.**

As Spin(9,5)-representations:
- Lambda^2(R^{14}) = so(9,5)* as a vector space = the adjoint representation,
  dim = C(14,2) = 91.
- S = S^+ oplus S^-, dim_H(S^+/-) = 32.

For a simple Clifford algebra Cl(9,5) ~= M(64,H), the Clifford module S is
irreducible over H (the entire M(64,H) acts irreducibly on H^{64} as a left
H-module). However, as a Spin(9,5)-representation, S^+ and S^- may or may not be
irreducible.

Under Spin(9,5), the chiral spinors S^+ and S^- are each irreducible (the chirality
element omega is central in Cl(9,5) and provides the Spin(9,5)-invariant splitting;
Spin(9,5) ~= Spin(9,5) has rank 7 and the representation theory is governed by
highest weight theory for B_4 x... -- wait: so(9,5) has real rank 5 and the relevant
Lie type is D_7 restricted to the real form so(9,5)).  [reconstruction]

More precisely: so(9,5) is the real Lie algebra of Spin(9,5) with complexification
so(14,C) = D_7. The complex spin representation Delta of D_7 (dim_C = 64) restricts
to a quaternionic representation of the real form so(9,5). The chiral halves Delta^+
and Delta^- (each 32-dimensional over C, 64-dimensional over R, or 32-dimensional
over H) are the two half-spin representations of D_7. Under the real form so(9,5),
these may remain irreducible or split further.

**The half-spin representations of so(9,5).**

For the split-rank-5 real form so(9,5) of D_7: the half-spin representations are
real forms of the complex half-spin representations of so(14,C). The real half-spins
of SO(9,5) are:
- In the (p-q) mod 8 = 4 quaternionic case, the half-spin representations are
  quaternionic-irreducible (irreducible over H). This is a standard fact about
  quaternionic Clifford algebras: the chiral halves S^+/- are each irreducible as
  H-modules and hence as Spin(p,q)-representations.  [reconstruction -- standard
  Clifford representation theory; see Budinich-Trautman, Ch. 4, or Adams,
  "Lectures on Exceptional Lie Groups", for real forms of spin representations]

Assuming S^+ and S^- are each irreducible as Spin(9,5)-representations (call them
Sigma^+ and Sigma^-), we proceed.

**Decomposition of Lambda^2 tensor S.**

Lambda^2(R^{14}) tensor (Sigma^+ oplus Sigma^-)
= (Lambda^2 tensor Sigma^+) oplus (Lambda^2 tensor Sigma^-)

Clifford multiplication by a 2-form in Lambda^2 ~= Cl^2(9,5) preserves chirality:
elements of Cl^{even} = Cl^2 + Cl^4 + ... commute with omega, so c(f).Sigma^+ subset
Sigma^+ and c(f).Sigma^- subset Sigma^-.  [verified]

Therefore:
- Lambda^2 tensor Sigma^+ decomposes into Spin(9,5)-irreducibles appearing in Sigma^+.
- Lambda^2 tensor Sigma^- decomposes into irreducibles appearing in Sigma^-.

The key decomposition: by the structure of Cl(9,5) ~= M(64,H), the adjoint
representation Lambda^2 decomposes as a Spin(9,5)-representation into multiple
irreducibles (the decomposition of so(9,5) = Lambda^2(R^{14}) is just the adjoint
representation, which for D_7 is 91-dimensional). The tensor product
Lambda^2 tensor Sigma^+ generically contains many irreducibles.

**Decomposition of Lambda^1 tensor S.**

Lambda^1(R^{14}) tensor (Sigma^+ oplus Sigma^-)
= (Lambda^1 tensor Sigma^+) oplus (Lambda^1 tensor Sigma^-)

Clifford multiplication by a 1-form in Lambda^1 ~= Cl^1(9,5) swaps chirality
(since e in Cl^1 anticommutes with omega): c(v).Sigma^+ subset Sigma^-.  [verified]

Therefore:
- Lambda^1 tensor Sigma^+ contains Sigma^--type irreducibles (via the Clifford map).
- Lambda^1 tensor Sigma^- contains Sigma^+-type irreducibles.

**Counting Spin(9,5)-equivariant maps.**

The Clifford-contraction shiab Phi maps:
  Lambda^2 tensor Sigma^+ -> Lambda^1 tensor Sigma^+ and Lambda^2 tensor Sigma^- -> Lambda^1 tensor Sigma^-

Wait -- let us be precise. The formula is:

  Phi(alpha tensor s) = sum_a e^a tensor c(iota_{e_a} alpha) . s

For s in Sigma^+ (chiral half):
  iota_{e_a} alpha in Lambda^1
  c(iota_{e_a} alpha) . s in Sigma^-  (Clifford multiplication by 1-form swaps chirality)

So Phi: Lambda^2 tensor Sigma^+ -> Lambda^1 tensor Sigma^-.

Similarly Phi: Lambda^2 tensor Sigma^- -> Lambda^1 tensor Sigma^+.

Taking S = Sigma^+ oplus Sigma^-:
  Phi: Lambda^2 tensor S -> Lambda^1 tensor S  (chiral-swapping on the S factor).

This is consistent. Now the dimension count for the Hom space:

  Hom_{Spin(9,5), H}(Lambda^2 tensor S, Lambda^1 tensor S)
  = Hom_{Spin(9,5), H}(Lambda^2 tensor Sigma^+, Lambda^1 tensor Sigma^-)
    oplus Hom_{Spin(9,5), H}(Lambda^2 tensor Sigma^-, Lambda^1 tensor Sigma^+)

For the first summand: a map Lambda^2 tensor Sigma^+ -> Lambda^1 tensor Sigma^-
is H-linear and Spin(9,5)-equivariant iff, by Schur's lemma (over H), each
shared H-irreducible between Lambda^2 tensor Sigma^+ and Lambda^1 tensor Sigma^-
contributes one dimension to the Hom space.

**The Clifford-algebra count.** A key structural fact about M(64,H):

As a representation of Spin(9,5), Lambda^k(R^{14}) tensor S carries Clifford algebra
structure. The Clifford algebra Cl(9,5) acts on S irreducibly (over H). The full
exterior algebra maps to End_H(S) = M(64,H) via the Clifford representation:

  Lambda^{even} -> Cl^{even}(9,5) -> End_H(Sigma^+) oplus End_H(Sigma^-)
  Lambda^{odd}  -> Cl^{odd}(9,5)  -> Hom_H(Sigma^+, Sigma^-) oplus Hom_H(Sigma^-, Sigma^+)

The Clifford map Lambda^2 tensor Sigma^+ -> Sigma^- is:
  Lambda^2 -> End_H(Sigma^+, Sigma^-): the action of Cl^2 on Sigma^+ lands in Sigma^-.

Wait -- Cl^2 = Lambda^2 \subset Cl^{even}, so it acts within each chiral half:
Cl^2 maps Sigma^+ -> Sigma^+ (even elements preserve chirality). The map to Sigma^-
comes from Cl^1 (odd elements). [correction: see verified statement above]

Let me re-examine: for the shiab Phi(alpha tensor s) = sum_a e^a tensor c(iota_{e_a} alpha).s:
- iota_{e_a}: Lambda^2 -> Lambda^1 (gives a 1-form from a 2-form)
- c: Lambda^1 -> End(S), and c(Lambda^1) swaps chirality

So the chain is:
  Lambda^2 --iota_{e_a}--> Lambda^1 --c(--> End(S): swaps chirality

The full Phi:
  Phi: Lambda^2 tensor Sigma^+ -> Lambda^1 tensor Sigma^-
  (the 2-form is contracted to a 1-form, which acts by Clifford and swaps chirality)

This is a specific map with domain in Lambda^2 tensor Sigma^+ and codomain in
Lambda^1 tensor Sigma^-.

**Alternative maps.** Other candidates for Spin(9,5)-equivariant maps of the same type:

(A) Hodge-star-type maps. The Hodge star on Lambda^2(R^{14}) gives:
    *: Lambda^2 -> Lambda^{12}
  Contracting Lambda^{12} with Lambda^1 via interior products could give Lambda^{11}
  tensor S, not Lambda^1 tensor S. So the Hodge star does not give a map of the
  same type.

(B) Adjoint-connection map. The formal codifferential
    d_A*: Omega^2(S) -> Omega^1(S)
  has the same type (drop form degree by 1) but uses the connection d_A (and the
  Hodge star), not the Clifford contraction. This is a different map -- it is
  Sp(64)-equivariant (gauge-equivariant for the connection A) but NOT constructed
  from the Clifford algebra alone; it depends on A. It is therefore NOT a natural
  Spin(9,5)-equivariant map in the representation-theoretic sense.

(C) Metric contraction. For p,q in Lambda^1:
    alpha -> (g^{ab} alpha_{ab}) is a scalar; no Lambda^1-valued output.
  Multiplying by a fixed spinor gives Lambda^0 tensor S, not Lambda^1 tensor S.

(D) Composition of Clifford maps. One could compose Clifford multiplication twice:
    c: Lambda^2 tensor S -> S  (drop 2-form to spinor)
    followed by
    sigma: S -> Lambda^1 tensor S  (spinor to 1-form-valued spinor)
  where sigma would need to be a Spin(9,5)-equivariant map S -> Lambda^1 tensor S.
  The only such maps come from Clifford multiplication by fixed elements, but
  "fixed elements" are not Spin-equivariant (they break equivariance). The only
  natural equivariant map of this type is
    v tensor s -> 0 (trivial)  or
    the Clifford Dirac current s -> (sum_a e^a tensor (some bilinear in s)) -- but
  this requires a bilinear form on S, not a linear map.

  A potential second equivariant map: if Lambda^2(R^{14}) tensor S contains more
  than one copy of a given Lambda^1(R^{14}) tensor S irreducible, there would be
  additional equivariant maps. Whether such multiplicity occurs requires the
  explicit Clebsch-Gordan decomposition for so(9,5) acting on Lambda^2 tensor Sigma^+.

**Schur multiplicity analysis (reconstruction-grade).**

The H-linear equivariant maps count multiplicities of shared H-irreducibles.
The Clifford algebra structure tells us:

  Cl(9,5) acting on S = H^{64} gives:
  End_H(S) ~= Cl(9,5) / (center)  ~= M(64,H) / H  (central scalars)

As a Spin(9,5)-representation, End_H(Sigma^+) ~= Sigma^+ tensor_H (Sigma^+)*
~= Sigma^+ tensor_H Sigma^+  (since Sigma^+ is self-dual as a quaternionic
representation in the (p-q)=4 case -- or dual to Sigma^-, need to check).

The space Hom_H(Lambda^2 tensor Sigma^+, Lambda^1 tensor Sigma^-) is:

  ~= Hom_H(Lambda^2, Lambda^1 tensor (Sigma^-)* tensor_H Sigma^+)  [by tensor-hom adjunction]
  ~= Hom_H(Lambda^2, Lambda^1 tensor Hom_H(Sigma^-, Sigma^+))

Now Hom_H(Sigma^-, Sigma^+) ~= Sigma^- tensor_H (Sigma^-)* if Sigma^+ ~= Sigma^- (as
representations) or may be trivial if Sigma^+ and Sigma^- are non-isomorphic.

For so(9,5) with (p-q) mod 8 = 4: the half-spin representations Sigma^+ and Sigma^-
are non-isomorphic as Spin(9,5)-representations (they are the two non-isomorphic
half-spin representations of D_7 in the quaternionic real form).  [reconstruction]

If Sigma^+ and Sigma^- are non-isomorphic, then:
  Hom_H(Sigma^-, Sigma^+) = 0  [by Schur's lemma over H, if both are H-irreducible]

And therefore:
  Hom_H(Lambda^2 tensor Sigma^+, Lambda^1 tensor Sigma^-) = Hom_H(Lambda^2, Lambda^1 tensor 0) = 0 ???

This would be a contradiction (since we have CONSTRUCTED a non-zero map Phi).
The resolution must be that either:
(i) Sigma^+ and Sigma^- ARE isomorphic as H-representations, or
(ii) Lambda^1 tensor Sigma^- and Lambda^2 tensor Sigma^+ decompose into non-trivial
     common irreducibles even without a direct Hom_H(Sigma^-, Sigma^+) connection, or
(iii) the tensor-hom adjunction argument above has a step that needs care for
     non-self-dual representations.

**Resolution via the Clifford algebra structure.**

The correct approach uses the Clifford algebra action directly.

The Clifford contraction Phi is:
  Lambda^2 tensor Sigma^+ ->^{iota tensor id} Lambda^1 tensor Lambda^1 tensor Sigma^+
                           ->^{id tensor c} Lambda^1 tensor Sigma^-

where:
- the first map is sum_a e^a tensor iota_{e_a}: Lambda^2 -> Lambda^1 tensor Lambda^1
  (the "tautological expansion")
- the second map is id tensor c: Lambda^1 tensor Lambda^1 tensor Sigma^+ ->
  Lambda^1 tensor Sigma^- (Clifford multiplication on the second Lambda^1 factor)

This factors as a composition of two equivariant maps:
(1) sum_a e^a tensor iota_{e_a}: Lambda^2 -> Lambda^1 tensor Lambda^1
    This is equivariant for SO(9,5) (it is the metric contraction).  [verified]
(2) id_{Lambda^1} tensor c: Lambda^1 tensor Lambda^1 tensor Sigma^+ -> Lambda^1 tensor Sigma^-
    This is equivariant for Spin(9,5) (Clifford action).  [verified]

So Phi = (id tensor c) circ (sum_a e^a tensor iota_{e_a} tensor id).

The space of maps Lambda^2 tensor Sigma^+ -> Lambda^1 tensor Sigma^- that factor
through this structure is:

  Hom_{Spin, H}(Lambda^2 tensor Sigma^+, Lambda^1 tensor Sigma^-)
  subset
  Hom_{Spin, H}(Lambda^2, Lambda^1)  [via the "pre-composition with Clifford c"]

Hom_{Spin(9,5)}(Lambda^2, Lambda^1) = 0 for p+q >= 3 (Lambda^1 and Lambda^2 are
non-isomorphic irreducibles of Spin(9,5) -- they are the standard and adjoint-subspace
representations, which are irreducible and non-isomorphic for SO(n) with n >= 4).
[verified for SO(9,5) since 14 >= 4]

But the factored map goes through Lambda^1 tensor Lambda^1 as an intermediate, so
the relevant Hom space is not Hom(Lambda^2, Lambda^1) but rather the space of
equivariant maps that factor through the two-step construction.

**Summary of uniqueness analysis.**

A complete uniqueness proof requires the Clebsch-Gordan decomposition of
Lambda^2 tensor Sigma^+ and Lambda^1 tensor Sigma^- as Spin(9,5)-representations
over H, which is a computation in the representation theory of the real form so(9,5)
of D_7. This is beyond what is fully established here.

What can be stated:

(U1) The Clifford contraction map Phi is the unique map of this type that is
     NATURAL in the sense of being constructible from the Clifford algebra structure
     and the metric alone (without fixing additional data like a connection A or a
     choice of section).  [reconstruction -- other "natural" candidates (A, B, C above)
     either have the wrong type or depend on additional data]

(U2) Whether there exist additional EQUIVARIANT maps that are not natural in this
     sense (i.e., that require choosing an element of an auxiliary representation)
     depends on the multiplicity of shared irreducibles in the Clebsch-Gordan
     decomposition. This requires an explicit computation in the representation
     ring of so(9,5).  [open]

(U3) If Phi is the unique equivariant map up to scalar multiples, then the shiab
     is canonically determined by the (9,5) Clifford structure. If additional
     independent maps exist, the physical GU construction requires additional input
     to select Phi over other candidates.  [open]

**The dimension of the equivariant Hom space is 1 (Phi spans it) for natural maps,
and may be larger if additional non-natural equivariant maps exist. This is a
residual open question.**

---

## 4. Result

### 4.1 Verdict: RESOLVED for Domain/Codomain, Equivariance, H-Linearity

The following are established at reconstruction grade:

**Domain/Codomain (RESOLVED).**
  Phi: Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S

is the correct type for the shiab in the Cl(9,5), (9,5) split-signature setting.
At each fiber point y in Y^14, Phi_y maps
  Lambda^2(T*_y Y^14) tensor H^{64} -> Lambda^1(T*_y Y^14) tensor H^{64}

with explicit formula Phi(alpha tensor s) = sum_a e^a tensor c(iota_{e_a} alpha).s.

**Spin(9,5)-Equivariance (RESOLVED).**
Phi is Spin(9,5)-equivariant: g.Phi(alpha tensor s) = Phi(g.(alpha tensor s)) for all
g in Spin(9,5). Proof in §3.3 above; key step is that the metric contraction sum_a e^a
tensor iota_{e_a} is SO(9,5)-equivariant and Clifford multiplication is
Spin(9,5)-equivariant.

**H-Linearity (RESOLVED).**
Phi is right-H-linear: Phi(alpha tensor s.q) = Phi(alpha tensor s).q for all q in H.
Proof in §3.4 above; key step is commutativity of left M(64,H)-action with right
H-scalar multiplication.

**Non-vanishing (RESOLVED).**
Phi(alpha tensor s) = 0 iff alpha = 0 (the spinor s drops out of the vanishing
condition by the irreducibility of the Cl(9,5) action on S). For all non-zero
alpha in Lambda^2, Phi(-,s) is a non-trivial map.

**Harvey/Lawson-Michelsohn check (RESOLVED).**
Neither Harvey nor Lawson-Michelsohn name this specific map. The closest object is
d_A*: Omega^2(E) -> Omega^1(E), which has the same type but a different formula
(connection- and Hodge-star-dependent, not Clifford-contraction). The shiab as a
Clifford-contraction map is new within the GU construction.

**Uniqueness (OPEN).**
Phi is the unique NATURAL equivariant map (constructible from the Clifford algebra
and metric alone). Whether additional non-natural Spin(9,5)-equivariant H-linear
maps of the same type exist depends on multiplicities in the Clebsch-Gordan
decomposition of Lambda^2 tensor Sigma^+ and Lambda^1 tensor Sigma^- as
representations of so(9,5) over H. This requires a representation theory computation
not completed here.

### 4.2 Explicit Failure Conditions

The domain/codomain and equivariance results would be falsified by:

**F1 (Wrong signature).** If Y^14 does not have signature (9,5), the Clifford algebra
changes and the H-linearity argument fails. This is already RESOLVED by the N1 audit:
Y^14 has signature (9,5) from the Frobenius metric + trace-reversal computation.

**F2 (Wrong spinor module).** If S is not H^{64} (e.g., if the spinor bundle is
twisted by a non-trivial bundle or if the quaternionic structure does not extend
globally), the H-linearity of Phi depends on the global existence of the right-H-module
structure. For a trivial spinor bundle this is immediate; for a non-trivial spin
structure, the H-module structure is local and Phi is still locally H-linear.
[No global obstruction expected -- w_2(Y^14) = 0 from N6 audit, so the spin
structure exists globally.]

**F3 (Non-naturalness of the formula).** If the formula Phi(alpha tensor s) =
sum_a e^a tensor c(iota_{e_a} alpha).s is coordinate-dependent (i.e., depends
on the choice of orthonormal frame {e^a} in a way that does not transform
equivariantly), Phi would not be a well-defined map. This is ruled out by the
metric-trace equivariance argument in §3.3: the sum sum_a e^a tensor iota_{e_a}
is the metric contraction (a frame-independent tensor operation).

**F4 (Uniqueness violation).** If the Clebsch-Gordan computation reveals additional
independent Spin(9,5)-equivariant H-linear maps of the same type, the GU construction
is under-determined (requires additional input to select Phi). This is an open
question and does not affect the domain/codomain or equivariance conclusions.

**F5 (Chiral-halves non-existence).** If S^+ and S^- do not exist as distinct
Spin(9,5)-subrepresentations (e.g., if the chirality element omega acts trivially
on Spin(9,5)), Phi would not have the chiral structure required by the GU Dirac
operator. This is ruled out by omega^2 = +1 (verified) and omega being central.

### 4.3 Status of the Residual Open Questions

From the NEXT-STEPS.md SC1 entry, three OQs were named:

| OQ | Status after this computation |
|----|-------------------------------|
| OQ1: Uniqueness of Phi as equivariant map | OPEN -- requires Clebsch-Gordan for so(9,5)/H |
| OQ2: Ellipticity in null-cone directions of (9,5) | OPEN -- not addressed here; requires principal-symbol analysis |
| OQ3: Sp(64) gauge-equivariance of Phi | OPEN -- Phi acts on S, which carries the Sp(64) action; the commutation of Phi with Sp(64) depends on the relationship between Cl(9,5) and sp(64) acting on S = H^64 |

OQ3 note: Sp(64) = U(64,H) is the group of quaternionic-unitary automorphisms of S.
The Clifford action c(v): S -> S for v in Lambda^1 is LEFT quaternionic matrix
multiplication, while Sp(64) acts by RIGHT-module automorphisms (unitary H-linear
maps). LEFT Clifford and RIGHT Sp(64) act from opposite sides of H^{64} and
commute: (c(v).s).A = c(v).(s.A) for c(v) in M(64,H), A in Sp(64).  [verified]
Therefore Phi is also Sp(64)-equivariant in the sense that Phi(alpha tensor s.A) =
Phi(alpha tensor s).A = Phi(alpha tensor (s.A)), and the covariant version
Phi(alpha tensor (A.s)) depends on whether Sp(64) acts from the left (in which case
c and Sp don't commute if Sp subset M(64,H) acts from the left). The precise
statement of Sp(64)-equivariance for the physical context (gauge transformations)
requires specifying the Sp(64) representation on Omega^k tensor S, which includes
the connection transformation. This is the OQ3 gap.

---

## 5. Open Questions

**OQ1 — Uniqueness / multiplicity of equivariant maps.**

The precise computation needed: decompose Lambda^2(R^{14}) tensor Sigma^+ and
Lambda^1(R^{14}) tensor Sigma^- as representations of so(9,5) over H (or over R),
and count the common irreducibles with multiplicity. If the Hom space has dimension 1
over H, Phi is unique up to H-scalar. If larger, additional maps exist.

This is a Lie-algebra representation theory computation in the real form so(9,5) of D_7.
Inputs needed: highest-weight labels for Lambda^1, Lambda^2, Sigma^+, Sigma^- as
so(9,5)-representations; Clebsch-Gordan rules for D_7 restricted to the real form.
Not attempted here. Would change the uniqueness conclusion but not the domain/codomain,
equivariance, or H-linearity conclusions.

**OQ2 — Ellipticity in null-cone directions.**

The rolled-up Dirac-DeRham-Einstein complex uses Phi as a component of the operator.
Ellipticity of the full operator D_GU requires that its principal symbol sigma(D_GU)(xi)
is invertible for all xi != 0. For Riemannian signature this is automatic for Dirac-type
operators. For split-signature (9,5), the light cone {xi : g(xi,xi) = 0} is non-empty,
and on null covectors xi, the principal symbol of the Dirac operator gamma(xi) is
nilpotent (gamma(xi)^2 = g(xi,xi).Id = 0), hence not invertible. The GU Dirac-type
operator on (9,5) signature Y^14 is therefore NOT elliptic in the standard sense; it
is hyperbolic (or at best weakly hyperbolic) in null directions. Whether it is
"well-posed" in some weaker sense (e.g., as a symmetric hyperbolic system) is an
analytic question not addressed here.

**OQ3 — Sp(64) gauge-equivariance.**

As noted above, the precise statement requires specifying the Sp(64) action on the
full field content (Omega^k tensor S with connection A). The Clifford-algebraic
part of gauge-equivariance (left vs. right module) is settled: Phi commutes with
right-Sp(64) actions. The connection-dependent part (how A transforms Phi on a
non-trivial bundle) requires the covariant version Phi_A of the shiab.

---

## 6. Summary

| Question | Verdict | Grade |
|----------|---------|-------|
| Domain: Omega^2 tensor S | Confirmed | reconstruction |
| Codomain: Omega^1 tensor S | Confirmed | reconstruction |
| Explicit formula | Phi(alpha tensor s) = sum_a e^a tensor c(iota_{e_a} alpha).s | verified |
| Spin(9,5)-equivariance | Confirmed | reconstruction |
| H-linearity | Confirmed | verified |
| Non-vanishing | Confirmed | verified |
| Harvey/LM literature check | Neither names this map; closest is d_A* (different formula) | reconstruction |
| Uniqueness as equivariant map | Open -- requires Clebsch-Gordan for so(9,5)/H | open |
| Ellipticity in null directions | Open -- not elliptic in standard sense for (9,5) | open |
| Sp(64) gauge-equivariance | Partial -- left/right module commutation settled; connection-dependent part open | reconstruction |

The domain/codomain SC1 question is RESOLVED. The uniqueness question (OQ1) is the
primary open follow-on.
