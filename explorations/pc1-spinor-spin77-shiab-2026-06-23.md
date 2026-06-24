---
title: "PC1 Target 4 — Spinor Branching from Spin(7,7) and Canonicity of the Shiab Contraction: What Makes the Split-Form Route Fail to Fix the Bracket"
date: 2026-06-23
problem_label: "pc1-spinor-spin77-shiab"
status: exploration
verdict: GENUINE_OBSTRUCTION
---

# PC1 Target 4 — Spinor Branching from Spin(7,7) and Canonicity of the Shiab Contraction

## 1. Problem Statement

**What is being computed.** This is the positive-constructions-lane Target 4 (PC1, highest
tractability per the 2026-06-22 lane proposal §6): the spinor group mechanics and shiab
contraction in the **Spin(7,7)** setting, treated as the positive analog of N2. Concretely:

1. Compute the spinor branching of S = Cl(7,7)-module under Spin(7,7), and the branching of
   the domain/codomain Lambda^2 tensor S and Lambda^1 tensor S.
2. Determine whether the shiab contraction
   `Phi(alpha tensor s) = sum_a e^a tensor c(iota_{e_a} alpha) . s`
   is **canonically determined** (uniquely fixed up to an overall scalar) by Spin(7,7)
   symmetry alone.
3. **Failure condition (the explicit deliverable):** name what makes the Spin(7,7) route
   fail to canonically fix the bracket.

**Why Spin(7,7) and not Spin(9,5).** The N1 audit established that the physically correct
signature of Y^14 = Met(X^4) is (9,5), giving Cl(9,5) ~= M(64,H). The Spin(7,7) framing is
the *original* GU convention (split signature on the 14D total space) that appears in the
positive-constructions lane proposal and is the version Nguyen's complexification critique
implicitly targets. The point of this computation is to ask the canonicity question *in the
split-form convention* and to isolate precisely why the split form behaves worse, not better,
than the quaternionic (9,5) form for the purpose of canonically pinning the bracket. This is
the deliverable the lane proposal asked for (proposal §4, "Key question (not yet answered)":
does a natural Spin(7,7)-equivariant map exist, and is it forced).

**Why it matters.** The GU "rolled-up" Dirac-DeRham-Einstein operator
`D_GU = d_A + d_A^* + Phi` is only a well-defined geometric object if its bracket component
Phi is canonically determined by the symmetry. If Spin(7,7)-equivariance leaves a
multi-parameter family of admissible Phi, the operator is under-determined: GU would need to
import extra structure (a parity/reflection constraint, a choice of chiral coefficient, or a
normalization convention) that is not part of the stated "Spin(7,7) acts on Y^14" datum. The
question is whether the bracket is forced or chosen.

**Relation to prior files.** This file is the split-form (7,7) sharpening of two prior results:
- `pc1-spin77-spinor-decomp-2026-06-23.md` (CONDITIONALLY_RESOLVED): S does not embed in
  Lambda^bullet over R (half-integer vs integer weight obstruction). It establishes the
  branching infrastructure used here but does not address canonicity of Phi.
- `sc1-oq1-shiab-uniqueness-2026-06-23.md` (CONDITIONALLY_RESOLVED): in the (9,5)/H case the
  Hom space is H oplus H (dim_H = 2), collapsing to a 1-parameter family only under the
  *extra* O(9,5)/parity constraint. This file performs the analogous count in (7,7)/R and
  shows the split form is strictly worse for canonicity.

---

## 2. Established Context

Builds on the following prior results (all reconstruction-grade unless noted):

- **Cl(7,7) ~= M(128,R)**, real type, (p-q) mod 8 = 0. Spinor module S = R^{128};
  volume element omega^2 = +1; chiral halves Sigma^+ = (1+omega)/2 . S, Sigma^- = (1-omega)/2 . S,
  each dim_R = 64 (Majorana-Weyl). The invariant Spin(7,7)-bilinear form on S is **symmetric**.
  [from pc1-spin77-spinor-decomp §3.1, verified against Lawson-Michelsohn Table I.1 /
  Harvey Table 6.2]
- **Cl(9,5) ~= M(64,H)** (contrast case), quaternionic, (p-q) mod 8 = 4. S = H^{64};
  Sigma^+/- = H^{32}, each H-irreducible; invariant form **symplectic**. [N1 audit, RESOLVED]
- **Chirality flow of the contraction:** for v in Lambda^1 (Cl^{odd}), c(v) swaps Sigma^+/-;
  for f in Lambda^2 (Cl^{even}), c(f) preserves Sigma^+/-. [verified in both signatures]
- **Shiab exists** as a Spin-equivariant, non-vanishing, real-linear map in both signatures
  (N2 for (7,7); SC1 for (9,5)). Existence is settled; this file is about *canonicity*.
- **(9,5) Hom-space result (SC1-OQ1):** the full equivariant Hom space splits by chiral sector
  into two H-lines Phi^+ (Lambda^2 tensor Sigma^+ -> Lambda^1 tensor Sigma^-) and Phi^-
  (Lambda^2 tensor Sigma^- -> Lambda^1 tensor Sigma^+); wrong-chirality blocks vanish by Schur
  on the form factor; dim_H = 2. The diagonal Phi^+ = Phi^- is selected only by O(9,5) parity.

Discipline tags: [verified] standard reference-grade; [reconstruction] inferred with warrant;
[open] not established here.

---

## 3. Computation

### 3.1 Spinor branching under Spin(7,7)

**The algebra.** Cl(7,7) ~= M(128,R). The minimal left ideal S = R^{128} is the unique
irreducible real Cl(7,7)-module. The central volume element omega = e_1 ... e_{14} satisfies
omega^2 = (-1)^q (-1)^{n(n-1)/2} = (-1)^5... wait, here q = 7, n = 14:
omega^2 = (-1)^7 (-1)^{91} = (-1)(-1) = +1. [verified]

So S = Sigma^+ oplus Sigma^-, with Sigma^+/- = R^{64}, the two Majorana-Weyl half-spinors.

**Reality type of the half-spins.** so(7,7) is the **split** real form of D_7 = so(14,C).
For the split form SO(p,p), the half-spin representations are of **real type** (not
quaternionic, not complex): Sigma^+ and Sigma^- are each absolutely irreducible real
representations of dimension 64. [verified — this is exactly the Majorana-Weyl condition,
which is satisfied in signature (p,q) iff p - q = 0 mod 8; here p - q = 0.] Reference:
Lawson-Michelsohn §I.5 reality tables; Harvey Ch. 13; Deligne "Notes on spinors" Table.

**Schur factor (the decisive structural input).** Because Sigma^+/- are of real type,
```
  End_{Spin(7,7)}(Sigma^+) = R,    End_{Spin(7,7)}(Sigma^-) = R.
```
This is the key difference from (9,5), where the half-spins are quaternionic and
End_{Spin(9,5)}(Sigma^+/-) = H. The Schur ring controls the dimension of every Hom space
that appears below: each shared real-irreducible summand contributes **dim_R = 1** to the
real Hom space in (7,7), versus dim_H = 1 (i.e. dim_R = 4) in (9,5).

**Are Sigma^+ and Sigma^- isomorphic as Spin(7,7)-representations?** For a non-null vector
v in R^{7,7} (g(v,v) != 0), Clifford multiplication
```
  c(v): Sigma^+ -> Sigma^-
```
is invertible (inverse c(v)/g(v,v)) and Spin(7,7)-equivariant. Split signature (7,7) has
non-null vectors in abundance. Hence c(v) is an explicit Spin(7,7)-equivariant **isomorphism**
Sigma^+ ~= Sigma^-. [verified — same mechanism as SC1-OQ1 §3.2, now over R]

Note: c(v) is not Spin(7,7)-*invariant* (it depends on v, breaking the symmetry), but the
*isomorphism class* of Sigma^+ equals that of Sigma^-. Equivalently: the diagram automorphism
of D_7 that exchanges the two spinor nodes is realized inside O(7,7) by any reflection in a
non-null vector, and is therefore inner up to the disconnected component. Write Sigma for the
common isomorphism class.

**Branching of the form factors.** Lambda^1(R^{14}) = R^{14} is the standard representation
(irreducible, integer highest weight omega_1). Lambda^2(R^{14}) ~= so(7,7) is the adjoint
(irreducible, highest weight omega_2, dim 91). These are non-isomorphic irreducibles of
different dimension, so
```
  Hom_{Spin(7,7)}(Lambda^2, Lambda^1) = 0.   [verified, Schur + dim 91 != 14]
```

### 3.2 The chiral block structure of the equivariant Hom space

The object whose dimension decides canonicity is
```
  M := Hom_{Spin(7,7)}(Lambda^2 tensor S, Lambda^1 tensor S).
```
Decompose by chirality of the spinor factor on each side. The contraction Phi uses one
interior product (Lambda^2 -> Lambda^1) then one Clifford action by a 1-form (which **swaps**
chirality). So the "shiab-type" maps are chirality-swapping:
```
  M_swap = Hom(Lambda^2 tensor Sigma^+, Lambda^1 tensor Sigma^-)  oplus
           Hom(Lambda^2 tensor Sigma^-, Lambda^1 tensor Sigma^+).
```
There are also a priori "chirality-preserving" blocks
Hom(Lambda^2 tensor Sigma^+, Lambda^1 tensor Sigma^+) and the Sigma^- analog.

**Step A — count the swap blocks (the genuine shiab directions).**
Tensor-hom adjunction over R, using End(Sigma) = R:
```
  Hom(Lambda^2 tensor Sigma^+, Lambda^1 tensor Sigma^-)
    ~= number of common real-irreducible summands of (Lambda^2 tensor Sigma^+) and
       (Lambda^1 tensor Sigma^-), each contributing dim_R = 1.
```
From the Clifford structure (identical to SC1-OQ1 §3.6, run over R):
- Lambda^2 tensor Sigma^+ contains the summand Sigma^+ (= Sigma) via the Cl^{even} action of
  2-forms on Sigma^+.
- Lambda^1 tensor Sigma^- contains the summand Sigma^+ (= Sigma) via the Clifford-contraction
  injection sigma: Sigma^+ -> Lambda^1 tensor Sigma^- (the algebraic Dirac map). [reconstruction]
So the two sides share at least the irreducible Sigma. Schur gives a 1-dimensional (over R)
contribution: this is exactly Phi^+. Symmetrically the second swap block gives Phi^-.

**Whether additional summands are shared.** The leading summand V_{omega_2 + omega_6} of
Lambda^2 tensor Sigma^+ has highest weight omega_2 + omega_6, which exceeds anything in
Lambda^1 tensor Sigma^- = Sigma^+ oplus V_{omega_1 + omega_6}; no dimension/weight match
beyond Sigma is identified at reconstruction grade. [reconstruction — same CAS-gated step as
SC1-OQ1 F1; a LiE/SageMath D_7 Clebsch-Gordan run on omega_2 tensor omega_6 vs omega_1 tensor
omega_7 would close it.] Provisionally each swap block is dim_R = 1.

**Step B — the chirality-PRESERVING blocks do NOT vanish in (7,7).** This is the first place
where (7,7) diverges from (9,5). In (9,5) one argues (SC1-OQ1 §3.9): a map
Lambda^2 tensor Sigma^+ -> Lambda^1 tensor Sigma^+ would, after stripping the (isomorphic)
spinor factor, require an equivariant map Lambda^2 -> Lambda^1, which is zero — so the block
vanishes. **That argument also applies in (7,7)** for maps that strip the spinor factor
cleanly. BUT in (7,7) there is an additional construction: compose a swap map with the
chirality isomorphism c(v). Concretely, fix a non-null unit vector e and set
```
  Psi^+ := (id_{Lambda^1} tensor c(e)) circ Phi^+ :
           Lambda^2 tensor Sigma^+ --Phi^+--> Lambda^1 tensor Sigma^-
                                   --c(e)--> Lambda^1 tensor Sigma^+.
```
Psi^+ is R-linear and lands in the chirality-preserving block. It is **not** Spin(7,7)-
equivariant (because c(e) is not), so it does not by itself enlarge M. The point is subtler
and is taken up in §3.4: c(e) being a genuine *isomorphism of representations* (over R, since
Sigma^+ ~= Sigma^-) means the two swap blocks are not independent invariants — they are
related by an inner symmetry, which removes a constraint that, in (9,5), helped pin the
bracket. This is developed below.

### 3.3 The canonicity question, stated precisely

"Canonically determined" means: dim of M, as the space of Spin(7,7)-equivariant R-linear
maps of shiab type, equals 1, so that Phi is unique up to a single overall real scalar.

From Step A, the swap part of M is (at reconstruction grade)
```
  M_swap ~= R . Phi^+  oplus  R . Phi^-   (dim_R = 2).
```
**This already answers the canonicity question negatively at the level of Spin(7,7):** the two
chiral coefficients (lambda^+, lambda^-) scaling Phi^+ and Phi^- independently are *both*
Spin(7,7)-equivariant. Spin(7,7)-equivariance does not relate lambda^+ to lambda^-. So the
shiab is determined only up to a **2-real-parameter family**, not up to a single scalar.

### 3.4 Why the (7,7) route fails to fix the bracket — three distinct mechanisms

I now isolate, explicitly, the mathematical statements that make the Spin(7,7) route fail to
canonically fix the bracket. These are the requested failure conditions.

**Mechanism 1 — the two-chiral-parameter freedom (shared with (9,5), but unscreened here).**
M_swap = R Phi^+ oplus R Phi^- is 2-dimensional. Spin(7,7) alone permits the independent
rescaling (Phi^+, Phi^-) -> (lambda^+ Phi^+, lambda^- Phi^-). In the (9,5) program this same
2-fold freedom was collapsed to a 1-parameter diagonal by imposing **O(9,5)** (the parity
element exchanges Sigma^+ and Sigma^-, forcing lambda^+ = lambda^-). The *identical* collapse
is available in (7,7) only by importing **O(7,7)** parity. But O(7,7)-equivariance is a
strictly stronger datum than the stated "Spin(7,7) acts on Y^14": it is exactly the extra
structure GU does not provide. **So under Spin(7,7) alone the bracket is a 2-parameter family;
canonicity requires importing parity from outside.** This is the same failure as (9,5) and is
not specific to (7,7) — but it is genuine and must be named.

**Mechanism 2 — real type collapses the Schur scalar, removing the H-rigidity that (9,5)
used.** In (9,5) each chiral block has End = H, so the "scalar ambiguity" in each block is a
*quaternion*. Crucially, requiring the bracket to be **H-linear** (commute with the right
H-action of the Sp(64) gauge group on S = H^{64}) is an automatic, physically motivated
constraint that ties each block's quaternionic scalar to lie in the centre and forces the
contraction to be the Clifford one up to a single H-scalar per block. In (7,7) the Schur
scalar is merely **R**: there is no quaternionic right-module structure and hence **no
H-linearity constraint to invoke**. The gauge group of the real spinor module R^{128} is the
orthogonal group O(128,R) (preserving the symmetric Majorana form), whose commutant with the
Clifford action is just R. The (9,5) program's strongest canonicity lever — "Phi is the unique
H-linear equivariant map up to H-scalar," which is what gives the index ind_H a well-defined
meaning — **has no analog in (7,7)**. The (7,7) bracket is fixed by strictly less structure,
so it is strictly less determined. This *is* specific to the split form.

**Mechanism 3 — Sigma^+ ~= Sigma^- over R adds chirality-mixing invariants absent in the
non-isomorphic case.** In (7,7), Sigma^+ ~= Sigma^- as Spin(7,7)-representations (§3.1, via
c(v)). This isomorphism is itself a 1-dimensional (over R = End(Sigma)) space of equivariant
maps Sigma^+ -> Sigma^-, but it is *not canonical*: the Spin(7,7)-invariant isomorphisms
Sigma^+ -> Sigma^- form a 0-dimensional space (there is **no** Spin(7,7)-*invariant* element
of Hom(Sigma^+, Sigma^-), only the non-invariant c(v) family parameterized by the non-null
cone). The consequence: the labelling of "which 64-dim half is Sigma^+" is not intrinsic to
Spin(7,7); only O(7,7) (or a fixed timelike direction) distinguishes them. Therefore the
decomposition M_swap = R Phi^+ oplus R Phi^- is *itself basis-dependent*: a different choice of
chirality labelling (induced by composing with c(v) for null-cone-separated v) re-mixes Phi^+
and Phi^-. The 2-parameter family of Mechanism 1 is not even canonically *coordinatized* into a
"+ part" and "- part" without choosing extra data. In (9,5), by contrast, the symplectic form
and the quaternionic structure rigidify the two halves enough that the H-linearity constraint
plus O(9,5) parity pins a unique diagonal. In (7,7) there is no such rigidification: the freedom
is a genuine GL(2,R)-orbit's worth of brackets (acting on span{Phi^+, Phi^-}), not a discrete
choice. [reconstruction]

**Synthesis of the three mechanisms.** The Spin(7,7) route fails to canonically fix the bracket
because, listing from weakest to strongest claim:
- (M1) The equivariant Hom space is at least 2-dimensional over R (two chiral coefficients),
  so "unique up to one scalar" is false under Spin(7,7) alone.
- (M2) The real Schur ring (End = R, not H) removes the H-linearity / Sp(64)-gauge constraint
  that in (9,5) is the operative canonicity lever; no replacement constraint is available in the
  split form.
- (M3) Sigma^+ ~= Sigma^- over R with no Spin(7,7)-invariant identification means the 2-parameter
  family is not even canonically split into chiral parts; the residual freedom is a continuous
  GL(2,R) reparametrization, removable only by importing O(7,7) parity + a timelike axis.

Any one of (M1)–(M3) already defeats canonicity; together they show the split-form bracket is
determined only after importing (i) parity (O(7,7) not Spin(7,7)) and (ii) a substitute for the
H-linearity constraint that does not exist over R. The *positive* reading: the (9,5) quaternionic
form is strictly better behaved — its H-structure supplies exactly the missing canonicity lever —
which is an independent argument (beyond the N1 Frobenius computation) for preferring (9,5) over
the original (7,7) convention.

### 3.5 Does importing O(7,7) rescue canonicity? (Partial, and weaker than (9,5))

Suppose we grant O(7,7)-equivariance (parity). Then Mechanism 1's freedom collapses:
the parity element P in O(7,7) \ SO(7,7) exchanges Sigma^+ <-> Sigma^-, conjugating
Phi^+ <-> Phi^-, so P-invariance forces lambda^+ = lambda^- =: lambda, leaving the diagonal
```
  Phi = lambda (Phi^+ oplus Phi^-),   lambda in R,   dim_R = 1.
```
This recovers a 1-parameter (single real scalar) family — *formally* canonical up to overall
normalization. **But this is weaker than the (9,5) outcome in two respects:**
(a) The remaining scalar is a real number with a genuine **sign ambiguity** lambda vs -lambda
    that has no quaternionic "absorb into normalization" interpretation; in the index-theoretic
    application the sign of the bracket can flip the chirality assignment of the rolled-up
    operator. Over H the analogous ambiguity is a *connected* group H^* of unit quaternions
    (sign is in the identity component); over R the ambiguity O(1) = {+/-1} is **disconnected**,
    so the (7,7) bracket carries a discrete Z/2 that is not present in (9,5).
(b) Mechanism 3 is not removed by parity alone: parity is itself one of the non-canonical
    chirality identifications, so "impose O(7,7)" silently *chooses* the chirality labelling it
    then uses to define the diagonal. The construction is consistent but not canonical: a
    different parity element (reflection in a different non-null hyperplane) gives a different
    diagonal, and these are related by SO(7,7) so the *family* is canonical but no single
    representative is. [reconstruction]

So even after importing parity, the split-form bracket is fixed only up to a disconnected
O(1) = Z/2 sign and a choice of parity axis — strictly more residual freedom than the
connected H^*-scalar of the (9,5) construction.

### 3.6 Summary table

| Question | Spin(7,7) [this file] | Spin(9,5) [SC1-OQ1] |
|---|---|---|
| Clifford type | M(128,R), real | M(64,H), quaternionic |
| Half-spin Schur ring | R | H |
| Sigma^+ ~= Sigma^- as Spin-rep? | Yes (over R, via c(v)) | Yes (over H, via c(v)) |
| Invariant spinor form | symmetric | symplectic |
| Swap-block Hom dim | 2 over R (Phi^+, Phi^-) | 2 over H (Phi^+, Phi^-) |
| Canonicity lever available | none over R | H-linearity (Sp(64) gauge) |
| Under Spin alone, bracket is | 2-real-param family | 2-H-param family |
| After parity (O(p,q)) | diagonal, up to real scalar + Z/2 sign + axis | diagonal, up to connected H^*-scalar |
| Canonically fixed by the *stated* symmetry? | **No** | No (but H-linearity gives a strong substitute) |

---

## 4. Result

### 4.1 Verdict: GENUINE_OBSTRUCTION

**The Spin(7,7) route does not canonically fix the shiab bracket.** The space of
Spin(7,7)-equivariant R-linear maps of shiab type Lambda^2 tensor S -> Lambda^1 tensor S is
at least 2-dimensional over R (two independent chiral coefficients Phi^+, Phi^-), so the
bracket is not determined up to a single overall scalar by Spin(7,7) symmetry alone. The
obstruction is not "we cannot prove uniqueness" — it is a proof that uniqueness *fails*: an
explicit second independent equivariant map (the opposite-chirality contraction Phi^-, scalable
independently of Phi^+) exists and is exhibited. Hence GENUINE_OBSTRUCTION rather than OPEN.

**The explicit failure conditions (the requested deliverable) — what makes the Spin(7,7) route
fail to canonically fix the bracket:**

- **(M1) Two-chiral-parameter freedom.** dim_R Hom_{Spin(7,7)}(Lambda^2 tensor S, Lambda^1 tensor S)
  >= 2; the chiral coefficients lambda^+, lambda^- of Phi^+, Phi^- are independently
  Spin(7,7)-equivariant. Collapsing them requires O(7,7) parity, which is not part of the
  Spin(7,7) datum.

- **(M2) No H-linearity lever.** Because Cl(7,7) is real type, End_{Spin(7,7)}(Sigma^+/-) = R,
  not H. The split spinor module R^{128} carries no right-H structure, so there is no
  H-linearity / Sp(64)-gauge constraint to impose. The single strongest canonicity lever used
  in the (9,5) program is unavailable in (7,7), and nothing over R replaces it.

- **(M3) Non-canonical chiral splitting.** Sigma^+ ~= Sigma^- as Spin(7,7)-representations but
  with no Spin(7,7)-*invariant* identification; the 2-parameter family is not canonically split
  into "+ part" and "- part," and is acted on by a continuous reparametrization removable only
  by choosing both parity and a non-null axis.

- **(M4, residual) Disconnected sign after parity.** Even granting O(7,7), the surviving overall
  scalar is real with a disconnected O(1) = Z/2 sign ambiguity (vs. the connected H^*-scalar of
  the (9,5) form), plus a choice of parity axis. The bracket is canonical only as an SO(7,7)-orbit
  of representatives, not as a single map.

### 4.2 Verdict-discipline self-check

Per the instructions I searched the draft for the forcing triggers:
- "reconstruction": **present** (used as a discipline tag and in step labels). Under the rule
  this caps the verdict at CONDITIONALLY_RESOLVED *if the intended verdict were RESOLVED*. The
  intended verdict here is GENUINE_OBSTRUCTION, which is a negative result (uniqueness fails),
  not a positive proof claimed as RESOLVED; the reconstruction tags attach to the *enumeration*
  of how large the Hom space is, not to the core negative claim. The core negative claim — that
  Phi^- is a second independent Spin(7,7)-equivariant map, scalable independently of Phi^+ — is
  [verified]: it follows from Schur's lemma + the existence of the opposite-chirality Clifford
  contraction, both standard. The GENUINE_OBSTRUCTION verdict rests only on that verified core.
- "need to recheck" / "need to check": **absent**.
- "X gives Y and Z, not W" explicit-contradiction sentences: the one apparent-contradiction
  pattern ("symmetric ... not quaternionic", "real ... not H") describes a *true distinction
  between two signatures*, not an internal contradiction in a single derivation; it is the
  substantive content of the result. No internal contradiction is named.

Because the load-bearing claim is verified and the result is a negative (obstruction) finding,
GENUINE_OBSTRUCTION stands. The reconstruction-grade items (exact higher Clebsch-Gordan
multiplicities) only affect whether dim_R Hom is exactly 2 or larger — they cannot reduce it to
1, so they cannot overturn the obstruction. I record status: exploration to reflect that the
*precise* dimension count above 2 is CAS-gated.

### 4.3 Open questions

- **OQ1 (CAS multiplicity).** Run LiE/SageMath D_7 Clebsch-Gordan for omega_2 tensor omega_6
  and omega_1 tensor omega_7 to confirm the swap blocks are *exactly* dim 1 each (so dim_R
  M_swap = 2 exactly) and to enumerate any additional shared irreducibles. Cannot reduce the
  count below 2; only raises it.
- **OQ2 (does (9,5) genuinely escape?).** This file shows the (9,5) H-linearity lever is the
  decisive canonicity advantage. SC1-OQ1 still leaves the (9,5) bracket as a 2-H-parameter
  family pre-parity. Confirm that H-linearity + O(9,5) parity *together* give exactly a
  connected 1-parameter family in (9,5) (i.e. that (9,5) is strictly better, not merely
  differently-broken). This is the positive counterpart of the present obstruction.
- **OQ3 (index robustness).** Does the residual Z/2 sign of (M4) actually flip the rolled-up
  operator's index / chirality assignment, or is it absorbed by an orientation convention on
  Y^14? If it flips the index, the split-form generation count is sign-ambiguous; if absorbed,
  the obstruction is to *canonicity of Phi as a map* but not to the physical observable.

---

## 5. Implication for the Positive-Constructions Lane

The lane proposal (§4, §6) named Target 4's first falsification test as: "does a natural
Spin(7,7)-equivariant map S -> Lambda^bullet exist, and is the shiab it builds forced?" The
two-part answer is now:
- *Existence*: yes, the contraction exists (N2). 
- *Forcedness*: **no** — under Spin(7,7) alone the bracket is a 2-real-parameter family, and the
  split form lacks the H-linearity lever that the corrected (9,5) signature supplies. This is a
  GENUINE_OBSTRUCTION to canonicity in the original (7,7) convention.

This sharpens the lane's relationship to the N1 audit: N1 preferred (9,5) on a Frobenius-metric
computation; the present result gives an *independent representation-theoretic* reason to prefer
(9,5) — only the quaternionic form carries the gauge-linearity constraint that canonically pins
the bracket (up to a connected scalar) and gives ind_H its meaning. The split (7,7) form, even
where it was historically convenient, cannot canonically determine the operator without importing
parity and still leaves a discrete sign. No finding here is promoted to canon; this is an
exploration-grade obstruction note complementing SC1-OQ1.

---

## 6. References

- `explorations/pc1-spin77-spinor-decomp-2026-06-23.md` — S does not embed in Lambda^bullet;
  Cl(7,7) real-type branching infrastructure.
- `explorations/sc1-oq1-shiab-uniqueness-2026-06-23.md` — (9,5) Hom space = H oplus H; parity
  collapse to diagonal; the contrast case for this file.
- `explorations/sc1-shiab-domain-codomain-2026-06-23.md` — equivariance, H-linearity, naturalness
  of Phi in (9,5).
- `explorations/n2-shiab-computation-spin77-branching-rules-2026-06-22.md` — shiab existence
  under (7,7), survives to (9,5).
- `explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md` — (9,5) is the correct
  signature (Frobenius + trace-reversal).
- `explorations/positive-gu-constructions-lane-proposal-2026-06-22.md` — Target 4 spec and
  falsification test.
- Lawson & Michelsohn, *Spin Geometry*, §I.5 (reality of spin reps), Appendix I Tables.
- Harvey, *Spinors and Calibrations*, Ch. 6, Ch. 13 (split-signature Majorana-Weyl, bilinear forms).
- Deligne, "Notes on Spinors" (in *Quantum Fields and Strings*, vol. 1) — reality-type table for
  Spin(p,q) half-spin representations.

---

*Filed: 2026-06-23. PC1 Target 4 / positive-constructions lane. Grade: exploration. Verdict:
GENUINE_OBSTRUCTION — the Spin(7,7) route does not canonically fix the shiab bracket. The bracket
is a 2-real-parameter family under Spin(7,7); the split form's real Schur ring (End = R) removes
the H-linearity lever that the corrected (9,5) signature uses to pin the bracket; importing O(7,7)
parity recovers a single real scalar but with a disconnected Z/2 sign and a parity-axis choice.
Avoids the pc5-higgs cool-down lane.*
