---
title: "WC-ENUM-COMPLETENESS: within the delimited class C of covariant sector-interior structures on the Clifford-RS carrier, the paper's 7-item obstruction enumeration is COMPLETE and every generator is 2-primary. Route (a) classification computed (generator spaces dim 2/2/2/2 under the full split covariance, all invariant forms purely cross-chirality, all antilinear structures T-type with per-block C^2 = -1 in (9,5) / +1 in (7,7), NO equivariant antilinear re-grading exists at all); route (b) engine sweep finds NO sector-interior odd-primary obstruction and shows the class boundary is SHARP (odd primes appear at the first step beyond the sector's data: 54 -> 3, 120 -> 7, 126 -> 5*7, j=3/2 -> 5)."
status: staged
doc_type: result
created: 2026-07-02
grade: "computed + independently re-verified (different gammas, different signature, different null-space algorithm) for the census; theorem-grade exact integer combinatorics for the same-chirality vanishing (16x16 zero-weight count = 0) and exact Fraction arithmetic for the engine (Weyl dim / Casimir / Dynkin over D5, eta family, composition closure); ghost-parity row inherited from canon (not recomputed). NOT a symbolic proof over an abstract axiom set: the classification is a machine-verified computation on the explicit carrier with printed spectral-gap and residual certificates (residuals 1e-12 to 1e-15, gaps O(1))."
method: "Route (a): compute ALL invariant-theoretic generator spaces of class C exactly (generic-element eigenvalue matching + PSD normal-matrix null space; every basis element hard-assert verified against every generator), on Cl(9,5), re-verified on Cl(7,7) + the (14,0) chirality-detecting control + an exact weight-peeling Schur count. Route (b): adversarially generate candidates beyond the equivariant core (gauge twists, boundary/eta, compositions, dressed pairings) and factor each candidate's congruence exactly."
depends_on:
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
  - canon/two-primary-lemma.md
  - canon/frame-triviality-structural-or-evadable-GU-independent-RESULTS.md
  - canon/ghost-parity-krein-synthesis.md
  - canon/boundary-eta-of-mu-RESULTS.md
  - tests/chase/MOVE-5/krein_nogo_chiral_index.py
---

# Enumeration completeness for Theorem 1: the class-C census and the extension engine

**Work card:** WC-ENUM-COMPLETENESS (NEXT-STEPS.md, 2026-07-02 publication-gating section;
journal-gating, priority 1). **Outcome: (i) with a sharply stated boundary** -- completeness
within a delimited class C is established at computed grade, the extension engine finds no
escape, and the boundary of C is shown to be sharp rather than vacuous. **Not promoted to
CANON.md** (pauses for Joe per the card's process gate).

**Scripts (all deterministic, numpy/stdlib only):**
- `tests/enum-completeness/enum_class_c_generators.py` -- route (a) census; ~26 s single pass
  (ENUM_STAGE=1/2 splits it for process-lifetime-capped sandboxes; identical results).
- `tests/enum-completeness/enum_extension_engine.py` -- route (b) engine; < 5 s, exact
  Fraction/integer arithmetic throughout; exit code 1 on any category-D finding (none).
- `tests/enum-completeness/verify/indep_check.py` -- independent re-check: own gamma
  construction (recursive doubling, not Jordan-Wigner), different signature Cl(7,7),
  different null-space algorithm (successive SVD refinement, not normal-matrix eigh),
  the Euclidean (14,0) control, and an exact weight-peeling Schur count; ~17 s.

All three ran to completion this pass (exit 0; hard asserts throughout; census residuals
1e-12..1e-15 with next-eigenvalue gaps O(1)-O(100)).

## The delimitation (class C, stated sharply)

C = all structures on the fixed 192-dimensional generation carrier `W` (the `j=1` self-dual
triplet of the gamma-traceless Rarita-Schwinger module of `Cl(9,5)`, split `14 = 4 + 10`)
that are **linear or antilinear in the carrier and equivariant under the sector's split
symmetry algebra** `G = so(4) (+) so(10)` (real form `so(4) (+) so(5,5)`), built from the
sector's own data:

- (C1) equivariant linear endomorphisms and their trace / graded-trace integers;
- (C2) invariant bilinear forms;
- (C3) invariant sesquilinear forms and their Krein signatures;
- (C4) equivariant antilinear intertwiners and their Kramers signs;
- (C5) index-type integers of equivariant intertwiners between chirality sectors;
- (C6) characteristic-class invariants determined by the sector's own bundle data (spin
  structure; gauge twists by the reps the sector actually contains: 1, 10, 16, 16bar, 45,
  the su(2)_+ triplet, the so(14) frame spinor; the boundary eta data of the RP^3 spine;
  the ghost grading).

**Excluded from C (the boundary):** external backgrounds / spurion VEVs; gauge twists by
reps the sector does not contain; extra global or discrete symmetries (e.g. a Z_9); operators
not equivariant under G (checked down to so(10) alone -- see robustness); and function-space
/ Fredholm structures (WC-FUNCTION-SPACE-EXT).

## Theorem (completeness within C; computed grade)

*Every invariant-theoretic generator of class C carries only 2-primary obstruction content,
and each generator maps onto one of the paper's enumerated items (1)-(7). Hence within C the
7-item enumeration of Theorem 1 is complete: no structure in C imposes an odd-prime congruence
on a net chiral generation count.*

### The generator table (computed; G = so(4)+so(10) on the 192-dim carrier)

| space | dim | computed structure | obstruction content | item |
|---|---|---|---|---|
| (C1) linear commutant | 2 | span(Id, Gamma_c); chirality-diagonal | integers tr/graded-tr in {0, +-96, 192}: all even | (3)/(4) |
| (C2) bilinear forms | 2 | ALL purely cross-chirality (exact torus proof: 16x16 zero-weight-sum count = 0, every real form) | hyperbolic pairing, even split | (2)/(3) |
| (C3) sesquilinear forms | 2 | ALL purely cross-chirality; every Hermitian combination has signature (+96,-96); the physical Krein K lies in the span | net chirality forced 0 | (3) |
| (C4) antilinear intertwiners | 2 | ALL chirality-PRESERVING (T-type), quaternionic per block: C^2 = -1 on W+ and on W- | Kramers Z/2 per chirality sector | (1)/(2) |
| (C5) cross-chirality linear maps | 0 | commutant is chirality-diagonal | no equivariant chirality flip | (3) |
| (C6) characteristic-class inputs | finite arithmetic list | engine-swept (below): eta_q family denominator 2^3; sector gauge indices {0,1,2,4,8}; frame-spinor index 8 = 2^3; sigma mod 16; spinor dims 2^k; ghost 50/50 (inherited from canon/ghost-parity-krein-synthesis.md, not recomputed) | all 2-primary | (4)-(7) |

Robustness: re-run under G' = su(2)_+ (+) so(10) (dims 8/8/8/8) and under so(10) alone
(dims 72/72/72/72 -- the weakest sector-interior covariance): every conclusion persists
(forms cross-chirality, antilinears chirality-preserving, no re-grading, index integers even).

The only odd factor appearing anywhere is the carrier multiplicity 3 inside the *dimensions*
96 = 2^5*3 and 192 = 2^6*3 -- a located dimension, never a congruence (the composition lemma
below makes this precise: 12k = 3 x 4k is three equivariant copies of a mod-4 statement, not
a mod-3 condition on any channel).

### The key computed correction (reported, not patched)

The initial expectation -- that equivariant antilinear maps swap chirality because
"conj(16) = 16bar" -- is **false in the actual real forms** and the computation caught it:
the internal algebras are `so(5,5)` (split; Majorana-Weyl 16 self-conjugate) in signature
(9,5) and `so(3,7)` in (7,7), so **every equivariant antilinear intertwiner PRESERVES
chirality** (a T-type structure). Consequences, all verified:

- The **Kramers/reality fork is signature-dependent but 2-primary on both branches**: on the
  (9,5) carrier every antilinear structure is quaternionic per chirality block (C^2 = -1:
  item 1, Kramers); on (7,7) the S-level structure is real (C C-bar = +1, as Cl(7,7) =
  M(128,R) requires: item 2, the mod-2 real/pseudoreal wall). Both are Z/2 walls.
- **No chirality-swapping equivariant antilinear operator (an AZ-CII-type re-grading -- the
  one antilinear shape that could escape) exists in class C at all**, in either signature and
  under all three covariance choices. This is *sharper than the paper's finite adversarial
  hunt* within the delimited class: the escape direction is provably non-equivariant, which
  also settles the equivariant core of WC-ANTILINEAR-BOUND (the residual for that card is
  exactly the non-equivariant remainder).
- GU's own quaternionic structure `J_quat = id (x) U` compresses onto the carrier *inside*
  the computed antilinear span (leakage 2.8e-14, distance to span 1.1e-13),
  chirality-preserving -- the paper's operator is one of the census generators.

## The extension engine (route b): no escape, boundary sharp

Categories: **A** = sector-available, 2-primary (consistent); **B** = odd-primary but
homotopy-fixed / count-independent (the located carrier); **C** = external channel (needs a
VEV, a non-sector twist, or an added symmetry); **D** = sector-interior odd-primary
obstruction = **contradiction with Theorem 1** (engine exits 1). **Category-D findings: NONE.**

- **E1 gauge twists** (exact Dynkin indices, all D5 irreps with Dynkin-label sum <= 2):
  sector reps -> I(1)=0 (vacuous), I(10)=1 (vacuous), I(16)=I(16bar)=2, I(45)=8: all
  2-primary (category A). Immediately beyond: I(54)=12=2^2*3, I(120)=28=2^2*7,
  I(126)=35=5*7, I(144)=34=2*17, I(210)=56=2^3*7 -- 16 odd-primary reps in this small sweep
  alone, ALL category C (external twists constraining their own R-channel index, not the
  16-channel count). **The boundary of C is sharp, not vacuous.**
- **E1b family channel**: the one realized family rep (the j=1 triplet) has index 4 = 2^2
  (item 4's 4k); a j=3/2 quartet would carry I = 10 = 2*5 (5-primary!) but is excluded by the
  computed embedding enumeration (tests/generation-sector/leg3_family_embedding_enumeration.py).
- **E1c frame-spinor channel**: so(14) half-spinor index = 8 = 2^3 (item 6 in index form).
- **E2 boundary/eta**: the charge-q family (2q^2-4q+1)/8 has odd numerator for every q
  (2-primary, category A). The framing channel -p_1/24 = 2^3*3 is the ONLY odd-primary
  boundary object in the sector's data and its 3-part IS the located carrier e_R = 1/12:
  homotopy-fixed, count-independent, category B. Dai-Freed-type rows (pin+ Z/16, CII towers
  Z/2, Z/8; L(3;1) 3-primary etas; Garcia-Etxebarria--Montero Z_9) are FLAGGED from-memory
  prior art: the 3-primary ones all require data the sector does not contain (a Z/3 deck
  group -- the spine is RP^3 = L(2;1) with deck Z/2; a global Z_9) -- category C.
- **E3 compositions**: lcm/gcd/products of the items' moduli {2,2,4,8,16,2,2} stay 2-primary
  (exhaustive check); multiplicity scaling by 3 puts the odd factor in the value, never in
  the per-channel modulus.
- **E4 gauge-dressed same-chirality pairings** (exact zero-weight quadruple counts):
  R = 1, 10, 45 -> count 0: NO same-chirality invariant pairing exists on the dressed
  carrier (exact vanishing; the Krein/Majorana walls stand). R = 16, 16bar -> possible at
  torus level, but activation requires a background VEV of the dressing field: category C
  (external spurion channel, consistent with SHIAB-05's Lambda^1 finding).

## What this changes and does not change

- **Theorem 1's conditionality upgrades** from "scoped to an enumerated 7-item list, com-
  pleteness open" to "**complete for the delimited class C** (computed grade), engine-swept
  beyond C with no sector-interior escape and a demonstrably sharp boundary." The paper text
  is NOT edited in this pass (outcome is (i), not (iii); wording changes pause for Joe with
  the CANON.md promotion decision).
- **The paper's caveat (d)** (antilinear non-existence is a hunt, not a proof) gains a proven
  equivariant core: within class C there is no antilinear re-grading at all; the honest open
  remainder is exactly the NON-equivariant antilinear space (WC-ANTILINEAR-BOUND).
- **Nothing here forces or forbids three generations.** The census reconfirms, at generator
  level, that the sector's interior is 2-primary and the only odd-primary object in its own
  data is the located (count-independent) carrier.

## Honest caveats

1. The census is a **computation on the explicit carrier**, exact-in-effect with printed
   machine-precision certificates -- not a symbolic proof from axioms. A Lean/CAS-symbolic
   port would upgrade the grade.
2. The G'/G''-robustness Hom bases are verified against 6 held-out random probe combinations
   (a false null vector fails a fresh combination generically) rather than all 45-48
   generators individually; the primary G census and the independent (7,7) check verify
   against every generator.
3. Item (7) (ghost parity) is **inherited** from canon/ghost-parity-krein-synthesis.md and
   the rs_ghost_* scripts, not recomputed here; its class-C role is the hyperbolic (50/50)
   pairing structure, which is the same cross-pairing mechanism as (C2)/(C3).
4. The engine's gauge-index congruence statement uses the standard AGW index normalization
   (index step per unit background charge proportional to the Dynkin ratio); the CLAIM used
   is only the prime content of the ratio, which is normalization-independent.
5. Class C excludes non-equivariant structures by construction; the paper's adversarial hunt
   (frame-dressed antilinear candidates, gauge dressings) lives exactly there and remains a
   hunt (WC-ANTILINEAR-BOUND is the card that bounds it).

## Integrity

No category-D candidate was suppressed: the engine prints every generated candidate with its
exact factorization, including the near-misses (54 -> 3, j=3/2 -> 5, dressed-16 pairings) and
classifies them by what data they would require. The chirality-preserving antilinear finding
CONTRADICTED the initial expectation and the assert was rewritten to classify-and-report
rather than to enforce the expectation; the finding is reported above as a correction. The
multiplicity-3 odd factors (96, 192, 12k) are reported and traced rather than hidden. No
number was fitted; the only target integers appearing anywhere are the carrier's own
(+96,-96) and the items' moduli.
