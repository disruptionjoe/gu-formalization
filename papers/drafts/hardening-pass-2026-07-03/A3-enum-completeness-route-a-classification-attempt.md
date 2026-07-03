---
title: "A3 -- Enum-completeness route-(a) classification attempt: a representation-theoretic derivation of the class-C generator spaces (2/2/2/2/0), replacing the numerical census"
status: draft
doc_type: hardening-artifact
grade: "PARTIAL -- proof-grade for the dimensions 2/2/2/2/0, the bilinear cross-chirality (universal), the C5=0 vanishing, and the Kramers signs C^2 = -1(9,5)/+1(7,7) via Frobenius-Schur multiplication; three named residuals (R1 split-form sesquilinear cross-chirality, R2 which-chirality-operator bookkeeping for T-type, R3 axiom-level RS gamma-traceless projection) keep the FULL classification short of pure axiom-level PROOF grade."
created: 2026-07-03
hardening_item: "Enum-completeness route-(a) classification attempt"
certificate: tests/hardening-pass/enum_route_a_classification.py
stages_only: true
depends_on:
  - canon/enum-completeness-class-c-RESULTS.md
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
  - tests/enum-completeness/verify/indep_check.py
---

# A3. Route (a) as a classification theorem: what closes symbolically and what does not

## 0. One-paragraph verdict

Route (a) **partially closes at proof grade.** The four generator-space **dimensions**
`2 / 2 / 2 / 2` and the cross-chirality-linear vanishing `0` are DERIVED symbolically --
by Schur's lemma applied to the abstract two-block decomposition `W = (3,2,16) (+)
(3,2,16bar)`, with no numerics, no random-Cartan weight peel, and no eigenvalue rounding.
The bilinear-form cross-chirality is derived as a **universal theorem** (valid in every
real form) from the single exact fact `16* = 16bar` (the `D5` diagram automorphism). The
per-block Kramers sign `C^2 = -1` on `(9,5)` and `+1` on `(7,7)` is derived by
**Frobenius-Schur multiplication** of exact per-factor indicators. **What does not close
to pure axiom-level proof grade** is named precisely: (R1) the *sesquilinear* cross-chirality
is split-signature-specific rather than universal -- the compact `(14,0)` control is provably
chirality-diagonal, so the obligation's "cross in every real form" phrasing overreaches and
we correct it; (R2) "antilinear = T-type / chirality-preserving" depends on *which* chirality
operator (full 14d vs internal 10d) one grades by, and reconciling the census's "preserving"
with the internal `conj(16)=16bar` "swap" is not machine-closed here; (R3) the multiplicity-1
of the `j=1` triplet is built from `su(2)` Clebsch-Gordan + `Dirac_10 = 16 (+) 16bar` rather
than from a machine-checked gamma-traceless Rarita-Schwinger projection. Everything asserted
is backed by an exact-arithmetic certificate that **runs to exit 0**
(`tests/hardening-pass/enum_route_a_classification.py`).

This is an honest **grade upgrade attempt** on Theorem 1's class-C completeness (computed ->
toward proof), not a new closure of the enum-completeness verdict (which route (b) already
closed at computed grade). **Nothing here derives, forces, or forbids three generations.**

## 1. What was wrong with the prior route-(a) artifact (and what was actually fine)

`tests/enum-completeness/verify/indep_check.py` lines 248-289 certify the decomposition
`W = (3,2,16) (+) (3,2,16bar)` by a **numerical weight-peel**: it diagonalizes a random
combination `A = sum r_i H_i` of seven Cartan generators, reads imaginary parts of expectation
values as weights, normalizes, and *rounds* to integers (`qerr < 1e-6`). It then asserts the
Schur count "`End_G(W) = 1^2 + 1^2 = 2; bilinear = 2; sesquilinear = 2; antilinear = 2`."

Two distinct concerns, which the house discipline flagged as TRAP #3 and TRAP #4:

- **The peel is computed, not symbolic** (TRAP #3): a random-Cartan diagonalization with
  rounded eigenvalues is a machine computation on the explicit carrier, not a theorem. This
  artifact replaces it with an *exact construction* of the same weight multiset from the
  tensor definition (Part A below), so no eigenvalues are ever rounded.

- **The "`1^2 + 1^2`" shorthand is reality-type-blind** (TRAP #4). Here the honest finding
  is more subtle than the trap's framing anticipated, and it cuts *both* ways:
  - The shorthand **is a valid count** -- but only because all four spaces are **complex**
    vector spaces and Schur-over-`C` gives `dim_C Hom(X,X) = 1` for *every* irrep `X`
    regardless of its real/complex/quaternionic type. Each of the four spaces is a sum over
    the two inequivalent, multiplicity-1 blocks, so each dimension is `1 + 1 = 2` (or `0`)
    *independently of reality type*. The reality type does NOT enter the dimension.
  - The trap's worry -- "a quaternionic block does not contribute 1 to the real endomorphism
    dimension" -- is **correct for the *real* endomorphism algebra** `dim_R End`, where a real
    block contributes 1, complex 2, quaternionic 4. But the census does **not** compute
    `dim_R End`; it solves for complex matrices, so it reports `dim_C`. For `dim_C` the
    reality type is genuinely irrelevant to the count.
  - Where reality type **does** show up is the **qualitative structure**: the Kramers sign
    `C^2 = +-1`, the real/pseudoreal wall, and whether a form is symmetric/Hermitian. Part C
    handles those honestly via Frobenius-Schur multiplication.

So the corrected statement is: **the dimensions `2/2/2/2/0` are reality-type-invariant and
derive from Schur alone; reality type decorates those spaces with signs.** This is reported,
not patched to force any number.

## 2. The delimited class C (unchanged; stated for self-containment)

`C` = structures on the fixed 192-dim carrier `W` (the `j=1` self-dual triplet of the
gamma-traceless Rarita-Schwinger module of `Cl(9,5)`, split `14 = 4 + 10`) that are linear
or antilinear on `W` and equivariant under `G = so(4) (+) so(10)` (physical real form
`so(4) (+) so(5,5)`), built from the sector's own data. The five linear/antilinear generator
spaces are `(C1)` equivariant endomorphisms, `(C2)` invariant bilinear forms, `(C3)`
invariant sesquilinear forms, `(C4)` equivariant antilinear intertwiners, `(C5)`
cross-chirality equivariant linear maps. (`(C6)` characteristic-class inputs are engine-swept
in route (b) and are out of scope here.)

## 3. Part A -- the branching, by exact construction (not a weight peel)

**Claim.** `W = (3,2,16) (+) (3,2,16bar)` as a `G`-module, each block multiplicity 1,
dim `3*2*16 = 96`, total 192; `3` = `su(2)_+` triplet (`j=1`), `2` = `su(2)_-` doublet, `16/16bar`
= `so(10)` half-spinors.

**Derivation.** The Rarita-Schwinger carrier is `Vector_4 (x) Dirac_128` with the gamma-trace
removed, then projected onto the `j=1` self-dual `su(2)_+` triplet. Over `so(4) = su(2)_+ (+)
su(2)_-`: the vector `4 = (2,2)` has doubled spins `(1,1)`; the `Cl(4)` spinor `4 = (2,1) (+)
(1,2)` has doubled spins `(1,0)` and `(0,1)`. Decomposing `Vector (x) so(4)-Dirac` by exact
`su(2)` Clebsch-Gordan (the certificate does this over both factors) gives four `su(2)_+ (x)
su(2)_-` sectors; the `j=1` self-dual triplet sits at doubled spin `(2,1)` with **multiplicity
exactly 1**. The gamma-trace (the pure spinor `(1,0)/(0,1)` content) never touches the `(2,1)`
sector, so trace removal leaves the `(3,2)` intact. Tensoring the `so(10)` spectator
`Dirac_10 = 16 (+) 16bar` gives the two blocks.

The certificate cross-checks this against the **exact weight multiset**: it builds the `16`
and `16bar` as the even/odd-parity sign vectors `(+-1/2)^5`, forms `(triplet {-2,0,2}) x
(doublet {-1,1}) x (16 or 16bar)`, and confirms 192 distinct joint weights partitioning as
`96 + 96` with disjoint blocks. **All integer arithmetic; nothing is diagonalized or rounded.**

**Residual R3.** The multiplicity-1 claim rests on `su(2)` CG plus `Dirac_10 = 16 (+) 16bar`,
both standard, but the gamma-traceless projection is argued in prose, not machine-checked as a
projector on the explicit RS module. A Lean/CAS RS-projection would close R3.

## 4. Part B -- Schur block-matching: the dimensions 2/2/2/2/0

With `W = V (+) Vbar`, `V = (3,2,16)` (chirality `+`), `Vbar = (3,2,16bar)` (chirality `-`),
`V` and `Vbar` **inequivalent complex irreps** (they differ in the `so(10)` label). The three
structure maps on the block labels are exact: dual `X*` (with `3*=3, 2*=2, 16*=16bar`),
conjugation `conj(X)` (with `conj(16)=16bar`), both swapping `V <-> Vbar`. Each generator space
is a set of ordered block pairs `(i,j)` with `block_i` isomorphic to a structure-map of
`block_j`; the dimension is the number of matches (Schur: `1` per matched inequivalent pair):

| space | match rule | dim | chirality of the matches |
|---|---|---|---|
| `(C1)` `End_G(W)` | `block_i ~ block_j` | **2** | both same-chirality (`Id`, `Gamma_c` diagonal) |
| `(C2)` bilinear `W -> W*` | `block_i ~ (block_j)*` | **2** | both **cross**-chirality |
| `(C3)` sesquilinear | `block_i ~ conj((block_j)*)` | **2** | both same-chirality *(compact-form result; see R1)* |
| `(C4)` antilinear `Wbar -> W` | `block_i ~ conj(block_j)` | **2** | both cross-chirality *(abstract; see R2)* |
| `(C5)` cross-chirality linear | opposite chirality & `~` | **0** | -- (Schur: `V != Vbar`) |

`(C1) = 2` and `(C5) = 0` are **clean proof-grade theorems**: the commutant of two distinct
multiplicity-1 complex irreps is `C (+) C`, spanned by `Id` and the grading `Gamma_c`, and there
is no equivariant map between the inequivalent chirality blocks. These need no reality input.

The reality-type-invariance of every entry is shown in the certificate: the matching uses only
`iso`, `dual`, `conj` -- all blind to real/complex/quaternionic type -- so the counts are fixed.

## 5. Part C -- Kramers sign C^2 by Frobenius-Schur multiplication

The per-block antilinear square is the **product of the Frobenius-Schur indicators of the
tensor factors**: `C^2 = FS(su(2)_+ triplet) . FS(su(2)_- doublet) . FS(16)`.

- `FS(triplet, j=1) = +1` (integer spin, real).
- `FS(doublet, j=1/2) = -1` (half-integer spin, quaternionic).
- `FS(16 of so(p,q))` from the **real Clifford classification** of `Cl(p,q)`, a function of
  `(q-p) mod 8` (Bott): `R`-type `-> +1`, `H`-type `-> -1`, `C`-type `-> 0`.

Exact outputs (certificate Part C):

| carrier | internal | `(q-p) mod 8` | type | `FS(16)` | `C^2 = (+1)(-1)FS(16)` |
|---|---|---|---|---|---|
| `(9,5)` | `so(5,5)`, `Cl(5,5)` | `0` | `R` | `+1` | **`-1`** (Kramers, quaternionic block) |
| `(7,7)` | `so(3,7)`, `Cl(3,7)` | `4` | `H` | `-1` | **`+1`** (real, pseudoreal wall) |

Both branches are `Z/2` walls (item (1) Kramers on `(9,5)`; item (2) real/pseudoreal on
`(7,7)`), reproducing the census's signs **from indicators, not from a trace of a numerically
built `C`**. Independent re-derivation: `Majorana-Weyl` spinors exist iff `(q-p) mod 8 = 0`,
true for `Cl(5,5)` (self-conjugate real `16`, the quaternionic sign coming from the `su(2)_-`
doublet) and false for `Cl(3,7)` (`H`-type) -- consistent with the table.

**Why this is *not* a target import.** The signs `-1/+1` are *outputs* of multiplying three
fixed indicators; no reality type was chosen to "land on" a value, and the two signatures give
*different* answers -- exactly the signature-dependence the census reported.

## 6. Part D -- bilinear cross-chirality is a UNIVERSAL theorem; the sesquilinear one is not

**Bilinear (universal).** An invariant bilinear form on `V` exists iff `V ~ V*`. Since `3, 2`
are self-dual, `V` is self-dual iff `16* = 16`. The certificate proves exactly that `weights(16*)
= -weights(16)` equals the `16bar` weight set (negating a 5-component sign vector flips parity,
`even -> odd`), so `16* = 16bar != 16`. Therefore `V` is **not self-dual over C**, no
same-chirality invariant bilinear exists, and every invariant bilinear pairs `V` with `Vbar`.
This argument uses only weights (the `D5` diagram automorphism), **no signature** -- it holds in
**every real form**. This is the clean, universal promotion of the "`16x16` zero-weight-sum count
`= 0`" observation to a theorem.

**Sesquilinear (split-form-specific -- honest correction, R1).** The obligation asked for
sesquilinear cross-chirality "valid in every real form." **This overreaches, and the sector's own
`(14,0)` control disproves it.** A sesquilinear invariant requires the conjugation `conj`, whose
action on chirality is *signature-dependent*. Abstract block-matching (Part B, using
`conj(16)=16bar`) actually returns the **compact-form** answer: chirality-**diagonal**. In the
compact `(14,0)` form the invariant sesquilinear form is definite and diagonal (verified by
`indep_check.py`'s `(14,0)` control, `||P+ F P+|| != 0`). In the **split** internal form the
physical Krein/Dirac pairing *is* cross-chirality with signature `(+96,-96)`. So we DERIVE
`sesquilinear = 2` universally, but claim **cross-chirality only for the split (physical)
signature**. Reported, not patched; the bilinear universality (above) stands.

## 7. Part E -- mapping to the paper's Theorem-1 items

| derived generator | maps to item |
|---|---|
| `(C1)` `End_G = span(Id, Gamma_c)`; graded trace in `{0, +-96, 192}` (all even) | (3)/(4) |
| `(C2)` bilinear `= 2`, cross-chirality hyperbolic pairing, even split | (2)/(3) |
| `(C3)` sesquilinear `= 2`, Krein signature `(+96,-96)` forces net chirality `0` | (3) |
| `(C4)` antilinear `= 2`, T-type, `C^2 = -1(9,5)/+1(7,7)` Kramers `Z/2` | (1)/(2) |
| `(C5)` cross-chirality linear `= 0`: no equivariant chirality flip | (3) |

The multiplicity `3` (triplet dimension) remains a **multiplicand** in `96 = 2^5 . 3`,
`192 = 2^6 . 3` -- never a congruence. Nothing in this derivation divides by `3`, `24`, `96`,
`chi(K3)`, `16+8`, or any generation-count target.

## 8. Honest grade and the exact remaining obligation

**Grade: PARTIAL.** Proof-grade (axiom-level, exact arithmetic) is reached for:
- the dimensions `2/2/2/2/0` (Schur block-matching, reality-type-invariant);
- `(C1)` structure `span(Id, Gamma_c)` and `(C5) = 0`;
- bilinear cross-chirality as a **universal** theorem (`16* = 16bar`);
- the Kramers signs `C^2 = -1/+1` via FS multiplication + Clifford signature `mod 8`.

It falls short of a *complete* axiom-level classification by three **named residuals**:

- **R1 (sesquilinear).** Cross-chirality of the invariant sesquilinear form is
  **split-signature-specific**, not universal; the compact control is diagonal. Closing this to
  a clean theorem needs the signature-dependent charge-conjugation identity that flips chirality
  in the split form -- derivable, but tied to `Cl(5,5)`'s specific `C`-matrix, not to weights
  alone. **The obligation's "every real form" phrasing is corrected to "the physical split form."**

- **R2 (which chirality operator).** "Antilinear = T-type / chirality-preserving" holds for the
  census's grading (the full 14d volume element) but the internal `so(10)` rule `conj(16)=16bar`
  naively *swaps* chirality; the two chirality operators differ by the `so(4)` chirality. A full
  symbolic reconciliation (showing the two swaps compose to a preserve) is sketched, not
  machine-checked.

- **R3 (RS projection).** The `j=1` triplet multiplicity-1 is built from `su(2)` CG +
  `Dirac_10 = 16 (+) 16bar`; a machine-checked gamma-traceless RS projector would make Part A
  fully axiom-level.

**The single sentence the grade upgrade still needs:** a signature-aware charge-conjugation
lemma (closing R1 and R2 together, since both are about how `conj` acts on chirality in the split
`Cl(5,5)`), plus an RS-projector certificate (R3). None of these is expected to change any number;
they convert three prose links into machine-checked steps.

## 9. Scope / integrity

- **Stage only.** This artifact and its certificate were written solely to
  `papers/drafts/hardening-pass-2026-07-03/` and `tests/hardening-pass/`. No edit to `CANON.md`,
  `RESEARCH-STATUS.md`, `NEXT-STEPS.md`, `canon/*`, the paper, or any status frontmatter; no
  `git add/commit/push`; no claim promoted.
- **Verdict unchanged.** The enum-completeness verdict was already closed by route (b) at
  computed grade; this is a *grade* attempt on route (a) only, and it lands PARTIAL.
- **No target import.** `2/2/2/2/0` and the signs are outputs of Schur / FS multiplication; the
  disagreements found (sesquilinear not universal) are reported, not reconciled by fiat.
- **Generation count stays OPEN.** Nothing here derives, forces, or forbids three; the theorem
  is that the sector interior is `2`-primary, full stop.

**Certificate.** `tests/hardening-pass/enum_route_a_classification.py` -- pure stdlib, exact
integer/rational arithmetic, no numpy, no randomness; runs to **exit 0** with every check passing
and the three residuals printed as OPEN.
