# A Two-Arena Representation-Theory Core: Chiral-Spinor Hom-Vanishing, the CRT Splitting of the Stable 3-Stem, and 2-Primary Blindness

**Draft. Internal tier. Not submitted. Publication DEFERRED / Joe-gated.**

**This paper does NOT derive a fermion generation count and asserts NO Geometric Unity (GU) physical premise.**
It records three exact, self-contained representation-theory / arithmetic facts that the GU generation-sector
program leans on, stated so that each stands on its own mathematics with no GU input. The value here is not a
physics claim; it is a small, honestly-graded, certificate-backed core that other work can cite without
inheriting any of GU's open questions.

Version 0.1, 2026-07-03. Working copy in the `gu-formalization` research-truth repo.

Two caveats hold throughout and are stated once here in full:

- **(i) No target integer is imported.** The only integers that appear are `0`, dimension factors of the form
  `2^a` or `2^a * 3`, the carrier's own signature `(+96, -96)`, and the homotopy moduli `8, 3, 24`. Nothing is
  normalized to `3`, `8`, `24`, `chi(K3)`, or any other physically suggestive value. The number three, where it
  appears, is a *multiplicand* inside a dimension, never the output of a congruence.
- **(ii) Verification is exact-integer and (for one leg) canon-corroborated; the Lean is proof-terms-written,
  not machine-verified in this pass.** See Section 5 for the full, honest grading. In short: the claims of this
  paper stand on the exact-integer certificate `tests/big-swing/R4_crt_two_arena.py` (re-run this session,
  exit 0) and, for fact (A), on the independent canon corroboration `canon/shiab-existence-cl95.md` (SHIAB-05,
  exact, checksum `16384 = 128^2`, component errors `0.00e+00`). The Lean source
  `tests/big-swing/R4_TwoArena.lean` is written free of `sorry` and `axiom`, but its recompilation was **not**
  reproduced here, and we do **not** advertise it as machine-verified.

---

## Abstract

We isolate three exact, unconditional facts, each stated as self-contained mathematics needing no external
physical input, and verify each an unusually strong way. **(A)** For the real orthogonal Lie algebra `so(9,5)`
acting on its 128-dimensional Dirac spinor `S = S^+ (+) S^-`, the same-chirality invariant scalar bilinear
vanishes: `dim Hom_{so(9,5)}(S^+ (x) S^+, Lambda^0) = 0`, while the cross-chirality pairing has dimension 1.
Equivalently, the chiral spinor `S^+` is not self-dual; its dual is the opposite chirality. **(B)** The stable
3-stem `pi_3^s = Z/24` splits by the Chinese Remainder Theorem as `Z/8 (+) Z/3` into disjoint (intersection
`{0}`) summands, and every group homomorphism from `Z/24` into a 2-group `Z/2^k` annihilates the order-3
summand: no power-of-two-valued invariant can detect the `Z/3` arena. **(C)** The class-C generator dimensions
and the associated signature/carrier dimensions are 2-primary up to a single multiplicative factor of 3
(`2+2+2+2 = 2^3`; `96 = 2^5 * 3`; `192 = 2^6 * 3`; and `3` never divides `2^k`). Fact (A) is verified by an
explicit Clifford-module null-space computation in two gamma bases and two signatures with self-dual controls,
cross-checked by exact-integer weight combinatorics, and independently corroborated in canon. Fact (B) is
exact-integer certified (exhaustive) and is the GU-independent arithmetic spine of the "located, not forced"
program. We make no claim about a generation count and derive no physics.

---

## 1. Introduction

The larger program this note serves ("located, not forced";
`papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md`) studies whether a
fermion generation count can be forced by the internal structure of a real Clifford Rarita-Schwinger sector.
That program's headline verdict is deliberately negative-and-open: it does **not** claim three generations.
Three of its load-bearing sub-facts, however, are pure mathematics that hold irrespective of whether GU is
correct or whether any generation count exists at all. This note extracts exactly those three, states them
cleanly, and grades their verification honestly.

The point of the extraction is separability. A downstream reader who wants the arithmetic of the two-arena
splitting, or the Spin(9,5) same-chirality Hom-vanishing, should be able to cite a self-contained statement
without importing any GU premise, any reconstruction-grade identification, or any of the program's open bridges
(the `order-3-class -> integer-3` conjecture, the function-space APS/end residual, and so on). None of those
open items appears below, because none is needed for (A), (B), or (C).

The three facts are ordered by how much representation theory each carries: (A) is genuine `so(9,5)` invariant
theory; (B) is elementary finite abelian group arithmetic with a homotopy-theoretic backdrop cited (not
re-proved); (C) is a factorization list. We state each with a proof or computation sketch, then grade all three
together in Section 5.

**What this note is not.** It is not a derivation of the generation count, and it forces or forbids nothing about
the number three. (A) is a Hom-vanishing, (B) is an arithmetic blindness, (C) is a list of factorizations. The
representation-theory-to-index step and the `order-3-class -> integer-3` bridge remain exactly as open as the
canon says (`canon/three-generations-locate-not-force-CRT-RESULTS.md`); they are outside this note's scope.

---

## 2. Fact (A): Spin(9,5) chiral-spinor Hom-vanishing

### Statement

Let `so(9,5)` act on its 128-dimensional Dirac spinor `S = S^+ (+) S^-`, each Weyl summand of dimension 64.

> **Theorem A.** `dim Hom_{so(9,5)}(S^+ (x) S^+, Lambda^0) = 0`, and `dim Hom_{so(9,5)}(S^+ (x) S^-, Lambda^0) = 1`.

Equivalently, `S^+` is not self-dual: its dual is the opposite chirality, `S^+ ~= (S^-)^*`. There is no
`so(9,5)`-invariant bilinear pairing of two same-chirality spinors into the trivial (scalar) representation; the
invariant scalar (charge-conjugation) pairing exists only off-diagonally, between `S^+` and `S^-`.

### Proof / computation sketch

**Structural reason.** For `so(2r)` a chiral (Weyl) spinor weight is an `r`-tuple of entries `+-1/2` with an
even number of minus signs. A trivial summand of `S^+ (x) S^+` requires a weight `w` in `S^+` whose negative
`-w` also lies in `S^+`. Negation flips every sign, sending the minus-count `m` to `r - m`. For `r` odd, `m`
even forces `r - m` odd, so `-w` always lands in the opposite chirality `S^-`. Hence the same-chirality
zero-weight count is exactly 0 and no trivial summand can occur. The carrier here has `n = p + q = 14`, so
`r = 7` is odd. (This is the standard "which Clifford charge-conjugation matrix flips chirality" fact,
`n = 14 ≡ 6 mod 8` real chirality-flipping, reduced to a one-line parity statement. The same parity argument
covers the internal `so(10)` wall, `r = 5`, also odd. For `r` even, e.g. `Spin(4k)`, the weight self-pairs and
`S^+` is self-dual — the control case.)

**Explicit verification (certificate).** `tests/big-swing/R4_spin95_hom_vanishing.py` establishes Theorem A three
independent ways:

| route | method | `dim Hom(S^+ (x) S^+, triv)` | control `dim Hom(S^+ (x) S^-, triv)` |
|---|---|---|---|
| (I) explicit `Cl(9,5)`, Jordan-Wigner gammas | full `so`-invariant bilinear null space (exact spectral gap) | `0` | `1` |
| (II) explicit `Cl(9,5)`, recursive-doubling gammas | independent basis, same method | `0` | `1` |
| (II) explicit `Cl(7,7)`, same `n = 14` | different signature | `0` | `1` |
| (II) control `Cl(4,0)`, `r = 2` even | method must SEE a nonzero | `1` (self-dual) | — |
| (II) control `Cl(8,0)`, `r = 4` even | non-triviality control | `1` (self-dual) | — |
| (III) exact weight combinatorics | integer count of same-chirality zero-weight pairs | `0` | — |

The Euclidean `Cl(4,0)` and `Cl(8,0)` controls are load-bearing: the same null-space method returns `1` there
(where `r` is even and `S^+` is genuinely self-dual), so a returned `0` is a real vanishing, not a method that
always returns `0`. Route (III) needs no linear algebra: the exact same-chirality zero-weight counts are
`so(14) r=7: 0 of 64`; `so(10) r=5: 0 of 16`; `so(6) r=3: 0 of 4`; and, for the even controls,
`so(4) r=2: 2 of 2`, `so(8) r=4: 8 of 8`, `so(12) r=6: 32 of 32` (self-dual).

**Independent canon corroboration.** The same object is recorded independently at `canon/shiab-existence-cl95.md`
(CORRECTION SHIAB-05, 2026-06-30): computed over the verified `Cl(9,5) = M(64, H)` representation by decomposing
`End(S) = (+)_k Lambda^k` and solving for the `Spin(9,5)`-invariant bilinear space by trace-orthonormal
projection onto antisymmetrized Clifford words. That computation gives the same
`dim Hom_{Spin(9,5)}(S^+ (x) S^+, Lambda^0) = 0`, with a hard checksum `sum_k mult = 16384 = 128^2 = (dim S)^2`
and all component errors `0.00e+00` (`tests/chase/MOVE-4/move4_spinor_square_forms.py`, with independent recheck
`tests/chase/MOVE-4/verify/indep_check.py`). This is exact, unconditional representation theory of `Spin(9,5)`,
independent of whether GU is correct; it settles only which channels the equivariant family contains.

**Scope of the Lean core.** `tests/big-swing/R4_TwoArena.lean` (namespace `WeightParity`) states the exact
combinatorial obstruction as arithmetic: `minusCount_neg` (negation sends the minus-count `m` to `r - m`),
`neg_flips_chirality` / `no_same_chirality_zero_weight` (for `r` odd, no even-chirality weight has an
even-chirality negative), the self-dual control `even_r_self_pairs` (for `r` even), instantiated at `r = 7`
(Spin(9,5)/Spin(7,7)) and `r = 5` (internal so(10)). What the Lean states is the *weight-parity obstruction*
(the same-chirality zero-weight count vanishes). What it does **not** cover is the representation-theoretic
implication "no zero weight => no trivial summand" (a weight-count is a necessary condition) or the exact
`dim = 1` cross-pairing; those come from the explicit Clifford null-space computation and the SHIAB-05
corroboration, not from the Lean. And, per Section 5, the Lean is proof-terms-written, not machine-verified in
this pass.

---

## 3. Fact (B): the CRT two-arena splitting of `pi_3^s` and 2-primary blindness

### Statement

> **Theorem B.** `pi_3^s = Z/24 ~= Z/8 x Z/3` (Chinese Remainder Theorem, `gcd(8,3) = 1`). The 2-primary
> subgroup `<3> = {0,3,6,...,21}` (order 8) and the odd subgroup `<8> = {0,8,16}` (order 3) intersect only at
> `0`. Consequently every homomorphism `f : Z/24 -> Z/2^k` annihilates the order-3 arena: `f(8) = 0`. No
> power-of-two-valued invariant can detect the `Z/3` summand.

### Proof / computation sketch

`pi_3^s = Z/24` is cited from stable homotopy theory (Adams' image-of-`J`: in stem `4s-1`, `Im J` is cyclic of
order the denominator of `B_{2s}/4s`; for `s=1` this is `24`, and `Im J_3 = Z/24`); we do not re-prove it. The
load-bearing content this note formalizes is the *arithmetic of the splitting and the blindness*:

- **Splitting.** The map `Z/24 -> Z/8 x Z/3`, `x -> (x mod 8, x mod 3)`, is a bijective homomorphism on all 24
  elements (Chinese Remainder, `gcd(8,3) = 1`).
- **Disjointness.** The 2-primary subgroup (elements of order dividing 8) is `<3>`, the odd subgroup (elements of
  order dividing 3) is `<8>`, and `<3> ∩ <8> = {0}`.
- **Blindness.** A homomorphism `f : Z/24 -> Z/2^k` is determined by `f(1)`. For the order-3 element `8`, the
  image `f(8)` satisfies `3 * f(8) = f(24) = 0` and `2^k * f(8) = 0`; since `gcd(3, 2^k) = 1`, the additive
  order of `f(8)` divides `gcd(3, 2^k) = 1`, so `f(8) = 0`. Every power-of-two-valued invariant is blind to the
  order-3 arena.

### Certificate

`tests/big-swing/R4_crt_two_arena.py` certifies all of the above with **exact integer arithmetic** (no floating
point), re-run this session, **exit 0**: the explicit iso `Z/24 -> Z/8 x Z/3` (bijective homomorphism checked on
all 24 elements and inverted by CRT reconstruction); disjointness (`<3> ∩ <8> = {0}`, with `<3>` order 8 and
`<8>` order 3); **exhaustive** 2-primary blindness (every hom `Z/24 -> Z/2^k` for `k = 1..6`, enumerated by
`f(1)`, sends `8 -> 0`), plus the general coprimality lemma for `k` up to 10; and the Adams backbone
(`e_R = 1/12` has additive order 12 in `Q/Z`, 3-primary component `4 e_R = 1/3` of order 3; `|Im J_3| = 24 = 8*3`,
`gcd(8,3) = 1`).

### Lean core (proof-terms-written; see Section 5 for grade)

`R4_TwoArena.lean` (namespace `CRT`) writes proof terms for: `twoArena : ZMod 24 ~=+* ZMod 8 x ZMod 3` via
`ZMod.chineseRemainder`; `eq_zero_of_coprime_nsmul` (an element killed by two coprime integers is `0`, via
`addOrderOf | gcd = 1`); `two_primary_blind (f : ZMod 24 ->+ ZMod (2^k)) : f 8 = 0`; and `arenas_disjoint` (the
only common multiple of 3 and 8 in `Z/24` is `0`). The source contains no `sorry` and no `axiom`. Recompilation
was not reproduced in this pass (Section 5); the canonical content stands on the exact-integer certificate above.

### Why this is the arithmetic spine of "located, not forced"

In the parent program the 2-primary arena `Z/8` is where every enumerated obstruction of the generation no-go
lives (Kramers `Z/2`, Rokhlin mod `2^4`, adjoint `4k`, real/pseudoreal mod-2 index, the cross-chirality Krein
signature, ghost `Z/2`). The odd arena `Z/3` is the unique CRT-disjoint sector where a homotopy-theoretic count
could conceivably live, and it carries the Adams `e`-invariant `e_R = 1/12` (additive order 12 in `Q/Z`,
3-primary part `Z/3`). Blindness is the exact arithmetic reason a 2-primary no-go is structurally unable to see
the odd-torsion sector — the spine of "located, not forced," here isolated as a GU-independent theorem of
arithmetic. Fact (B) is the same fact recorded in the parent draft's Section 5 and at
`canon/enum-completeness-class-c-RESULTS.md` / `canon/core-theorems-symbolic-proof-RESULTS.md`; this note adds a
self-contained, certificate-backed restatement, not a competing claim.

---

## 4. Fact (C): class-C 2-primary generator arithmetic

### Statement and computation

The enum-completeness census (`canon/enum-completeness-class-c-RESULTS.md`) computes the invariant-theoretic
generator spaces of class C on the carrier with dimensions `2 + 2 + 2 + 2` (linear commutant, bilinear,
sesquilinear, antilinear), totalling `8 = 2^3`; the cross-chirality Krein signature is `96 = 2^5 * 3`; the
carrier dimension is `192 = 2^6 * 3`; spinor dimensions are pure powers of two. The arithmetic backbone is:

- `generator_dims_two_primary`: `2 + 2 + 2 + 2 = 2^3`;
- `ninety_six_factor`: `96 = 2^5 * 3`;
- `carrier_dim_factor`: `192 = 2^6 * 3`;
- `spinor_dim_not_div_three`: `3` never divides `2^k`.

The only odd factor anywhere is the multiplicative carrier multiplicity `3` inside a dimension — never a
per-channel congruence. This is the factorization content behind fact (B)'s statement that no enumerated
generator imposes an odd-prime congruence. The full generator classification itself remains a computation on the
explicit carrier (`canon/enum-completeness-class-c-RESULTS.md`); fact (C) records only the 2-primary arithmetic
of the resulting dimensions.

These identities are written as Lean proof terms in `R4_TwoArena.lean` (namespace `TwoPrimaryGenerators`) and
are elementary `norm_num` / divisibility facts; they are also implied directly by the integer certificates. Their
grade is the Section 5 grade for the Lean layer.

---

## 5. Verification status (honest grading)

This is the section the repo exists for. Each leg is graded by the strongest verification actually reproduced,
not by the strongest verification available in principle.

**Fact (B) — exact-integer certified, this session.** `tests/big-swing/R4_crt_two_arena.py` runs with exact
integer arithmetic (no floating point) and returns exit 0 (re-run 2026-07-03). The splitting, disjointness, and
2-primary blindness are checked by direct enumeration over all 24 elements and all homs into `Z/2^k` for
`k = 1..6`, plus a coprimality lemma to `k = 10`. This is the strongest grade in the note and the claims of (B)
rest here.

**Fact (A) — exact computation plus independent canon corroboration.**
`tests/big-swing/R4_spin95_hom_vanishing.py` performs the explicit Clifford null-space computation in two gamma
bases and two signatures, with self-dual Euclidean controls that return nonzero (so the method can see a
nonzero), and cross-checks by exact-integer weight combinatorics. Independently, `canon/shiab-existence-cl95.md`
(SHIAB-05) records the same `dim Hom = 0` from a separate trace-orthonormal projection computation with hard
checksum `16384 = 128^2` and component errors `0.00e+00`. Two independent computations, two signatures, two
methods, agreeing on `0`. The numeric second-basis / second-signature re-derivation inside the R4 script is
asserted by the source run; the canon SHIAB-05 corroboration is the independent anchor.

**Fact (C) — 2-primary arithmetic, implied by the integer certificates.** The factorizations are elementary and
are entailed by the same exact-integer material; the risk here is essentially nil.

**The Lean layer — proof terms written, source free of `sorry` / `axiom`, recompilation NOT reproduced.** This
is the critical honesty point. `tests/big-swing/R4_TwoArena.lean` is written to compile against the repo's
mathlib and contains no `sorry` and no `axiom` in its source. However:

- Its recompilation was **not** reproduced in this pass. We have not observed `lake env lean` (or equivalent)
  return exit 0 on this file in this session.
- The sibling Lean file `Lean/GUFormalization/LocatedNotForcedLegs.lean` — the same repo's parallel
  located-not-forced Lean skeleton — states explicitly in its own header: "Lean 4.32.0-rc1 IS installed on this
  machine (via elan), but mathlib is NOT provisioned (no `.lake`), so this `import Mathlib` file has **not** been
  typechecked. Proof terms are written out (no `sorry`), but do NOT cite any statement here as 'proved in Lean'
  until it compiles." `R4_TwoArena.lean` also does `import Mathlib` and is subject to the same unprovisioned-mathlib
  status.

Therefore we grade the Lean as **"proof terms written, source free of `sorry`/`axiom` — recompilation not
reproduced,"** NOT as machine-verified. The source-exploration front matter's phrase "Lean 4 compiled, no sorry,
no axiom" overstates what was reproduced; the accurate statement is that the proof terms are written and the
source is clean, but a clean recompilation against a provisioned mathlib has not been observed here. Do not cite
any statement in this note as "proved in Lean." Every claim of this note stands independently on the
exact-integer certificate (fact B) and on the exact computation plus SHIAB-05 canon corroboration (fact A).

**Verification tier.** All verification reported here is **internal**: computations reproduced and adversarially
reviewed within the same AI-directed process that produced them; no result has been independently replicated or
peer-reviewed outside this repo. The exact-integer certificate and the two-method agreement for fact (A) are the
strongest internal evidence available; they are not a substitute for external replication.

### Status-of-claims table

| Claim | Grade |
| --- | --- |
| (A) `dim Hom_{so(9,5)}(S^+ (x) S^+, Lambda^0) = 0`; cross-pairing `= 1` | Exact computation (2 bases, 2 signatures, controls) + independent canon corroboration (SHIAB-05, checksum `16384`, errors `0.00e+00`) |
| (B) `pi_3^s = Z/24 = Z/8 (+) Z/3`, disjoint; 2-primary blindness `f(8)=0` | Exact-integer certified, exhaustive, exit 0 (re-run this session); `pi_3^s = Z/24` cited from Adams (not re-proved) |
| (C) generator dims `2+2+2+2 = 2^3`; `96 = 2^5·3`; `192 = 2^6·3`; `3 ∤ 2^k` | 2-primary arithmetic, entailed by the integer certificates |
| Lean proof terms (`R4_TwoArena.lean`), all three legs | Proof terms written, source free of `sorry`/`axiom` — recompilation NOT reproduced; do not cite as machine-verified |
| A generation count / any GU physical premise | Not claimed; out of scope |

---

## 6. Relation to prior art and to the located-not-forced program

**To the located-not-forced program.** Fact (B) is the arithmetic spine of "located, not forced": the CRT
disjointness of `Z/8` and `Z/3` plus 2-primary blindness is the precise reason a 2-primary no-go cannot see the
odd-torsion sector where a homotopy-theoretic count could live. The parent candidate paper
(`papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md`, Section 5) uses this
as its central structural fact; the earlier draft
`papers/drafts/two-primary-no-go-three-primary-boundary-class-2026-06-28.md` develops the 2-vs-3-primary theme
with the `RP^3` boundary class and the Adams `e`-invariant. This note is the standalone, certificate-backed
rep-theory / arithmetic core: it does **not** duplicate those papers' generation-count discussion, the located
order-3 carrier, the tangential-vs-gauge fork, or the `order-3-class -> integer-3` bridge. It carries only the
three facts that are true independent of any of that.

**To the literature.** The stable-homotopy input `pi_3^s = Z/24` and its use in family-number discussions is not
novel to this program; the CRT primary decomposition `Z/24 = Z/8 (+) Z/3` is elementary. The fact (A)
Hom-vanishing is standard Clifford-module representation theory (which charge-conjugation matrix flips chirality
for `n ≡ 6 mod 8`), here stated cleanly for the full `so(9,5)` carrier and certified. This note claims no novelty
for these facts as mathematics; its contribution is the clean, separable, honestly-graded statement of exactly
the three that the generation-sector program depends on, decoupled from the program's open physics.

---

## 7. What is NOT claimed

- **No generation count.** Nothing here forces or forbids three, or any number. Fact (A) is a Hom-vanishing,
  fact (B) is an arithmetic blindness, fact (C) is a factorization list.
- **No GU physical premise.** No GU-specific step is used or assumed. The facts hold whether or not GU is
  correct.
- **No representation-theory-to-index bridge.** The step from "same-chirality invariant scalar bilinear is
  absent" to any physical mass or index statement, and the `order-3-class -> integer-3` identification, remain
  exactly as open as `canon/three-generations-locate-not-force-CRT-RESULTS.md` records. They are out of scope.
- **No machine-verified Lean.** Per Section 5, the Lean is proof-terms-written with clean source, not recompiled
  here. Do not cite any statement as "proved in Lean."
- **No external replication.** All verification is internal tier.

---

## 8. Reproducibility appendix

**Fact (B) certificate.** `tests/big-swing/R4_crt_two_arena.py` — exact-integer, no floating point. Run with any
Python 3 (uses only `fractions` and `math` from the standard library). Re-run 2026-07-03, exit 0. Verifies the
CRT iso on all 24 elements, disjointness of the two arenas, exhaustive 2-primary blindness for `k = 1..6` (plus
the coprimality lemma to `k = 10`), and the Adams backbone numbers.

**Fact (A) certificate.** `tests/big-swing/R4_spin95_hom_vanishing.py` — Python/numpy. Heavy (128-dimensional
Clifford module, `so`-invariant bilinear null-space solve). Verifies Theorem A three ways (two gamma bases, two
signatures `Cl(9,5)` and `Cl(7,7)`, Euclidean `Cl(4,0)`/`Cl(8,0)` self-dual controls, exact weight
combinatorics). Independent canon corroboration: `canon/shiab-existence-cl95.md` (SHIAB-05), with runnable
computation `tests/chase/MOVE-4/move4_spinor_square_forms.py` and independent recheck
`tests/chase/MOVE-4/verify/indep_check.py` (checksum `16384 = 128^2`, errors `0.00e+00`).

**Lean source.** `tests/big-swing/R4_TwoArena.lean` — namespaces `WeightParity` (fact A obstruction), `CRT`
(fact B), `TwoPrimaryGenerators` (fact C). Source free of `sorry` and `axiom`. Intended compilation:
`~/.elan/bin/lake env lean tests/big-swing/R4_TwoArena.lean` against the repo's provisioned mathlib. **Not
recompiled in this pass**; mathlib provisioning status is the same caveat noted in
`Lean/GUFormalization/LocatedNotForcedLegs.lean`. Treat as proof-terms-written, not machine-verified.

**Sources.** Source exploration: `explorations/big-swing-2026-07-03/R4-two-arena-rep-theory-core.md`. Canon spine
this note serves: `canon/two-arena-rep-theory-core-RESULTS.md`. Fact (A) canon corroboration:
`canon/shiab-existence-cl95.md`. Parent program: the located-not-forced candidate and the two-primary/three-primary
draft cited in Section 6. Open bridges (out of scope):
`canon/three-generations-locate-not-force-CRT-RESULTS.md`.
</content>
</invoke>
