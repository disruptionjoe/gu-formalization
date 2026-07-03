---
title: "WC-ANTILINEAR-BOUND: the paper's antilinear finite adversarial hunt is CLOSED over a delimited class S -- an index-nullity THEOREM, not a search. S = all Krein-compatible antilinear operators on the 192-dim carrier (M^dag K M = lambda K-bar, lambda real nonzero; no equivariance, frame, square, or continuity assumption; every rung of a declared symmetry-breaking ladder down to symmetry-free). Every C in S maps the chirality pair to a K-Lagrangian pair, so every physical subspace keeps net chiral index EXACTLY 0 under every C-induced re-grading: no admissible antilinear chiralizer exists in S. The hunted operator (frame-non-trivial antilinear CII swap) EXISTS in S (closed-form witnesses, all four sign patterns) and still forces nothing. Outside S admissibility itself fails: non-Krein antilinear operators do not act on the sector's physical states."
status: canon
canon_promoted_at: "2026-07-03"
doc_type: result
created: 2026-07-02
grade: "proof-grade for the index-nullity theorem (5-line finite-dimensional linear algebra; premises machine-certified: K Hermitian involution, signature (96,96), purely cross-chirality, K Gamma_c = -Gamma_c K) with adversarial machine instantiation (8 operators x 4 physical subspaces, chi_C = 0 as exact integer ranks, isotropy residuals ~3e-14); computed + independently re-verified for the ladder census (own gammas, different embedding, different seed, different rank algorithm); exact integer weight/Clebsch arithmetic reproduces the entire census dimension table; exact linear-algebra certificates (C5) for strict-admissibility non-existence at L1/L1b; ONE search-grade cell (strict A2+A3 at L5, 120 deterministic starts, not load-bearing). NOT a symbolic proof over an abstract axiom set, and NOT a function-space statement (WC-FUNCTION-SPACE-EXT)."
method: "Step 1 delimit (class S + declared 9-rung ladder + formalized admissibility A1-A4 and frame-triviality); Step 2 decide per rung (exhaustive antilinear Hom censuses, preserve/swap splits, frame charges, exact admissibility certificates); Step 3 symmetry-free bound (index-nullity theorem + closed-form witness construction + sharpness controls); independent re-check (exact combinatorics + independent substrate + Cl(7,7) + (14,0) premise-failure control)."
depends_on:
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
  - canon/enum-completeness-class-c-RESULTS.md
  - canon/frame-triviality-structural-or-evadable-GU-independent-RESULTS.md
  - canon/ghost-parity-krein-synthesis.md
  - canon/two-primary-lemma.md
---

# The antilinear bound: from finite adversarial hunt to delimited theorem

**Work card:** WC-ANTILINEAR-BOUND (NEXT-STEPS.md, 2026-07-02 publication-gating section;
journal-gating, priority 2). **Outcome: (a)+(b) -- a non-existence PROOF over a rigorously
delimited class, with exhaustive certificates on every rung of a declared symmetry ladder
and the outside-class residual stated in one sentence.** The failure condition (an
admissible frame-non-trivial antilinear chiralizer that forces a nonzero index) did NOT
fire -- and the result is sharper than "not found": the candidate operators exist and are
exhibited, and a theorem shows none of them (nor anything else in the class) can force.
**Not promoted to CANON.md** (pauses for Joe per the card's process gate).

**Scripts (all deterministic, numpy/stdlib only; total 247 hard asserts, all passed):**
- `tests/antilinear-bound/antilinear_ladder_census.py` -- the declared ladder, per-rung
  censuses and admissibility certificates; ~39 s (ANTI_STAGE=1/2 splits it).
- `tests/antilinear-bound/antilinear_symmetry_free_bound.py` -- the index-nullity theorem
  with closed-form witnesses and sharpness controls; ~2 s.
- `tests/antilinear-bound/verify/indep_check.py` -- independent re-check (own gammas,
  different embedding/seed/rank algorithm, exact integer combinatorics, Cl(7,7), (14,0)
  control); ~4 s.

## Step 1 -- the delimitation (class S, stated sharply)

The reviewer's demand: state the operator algebra, functional class, and topology; then
prove non-existence or give an exhaustive certificate for that bounded class; state the
outside-class residual honestly.

**Operator algebra / functional class.** All antilinear operators `C = M . conj`,
`M` a complex 192 x 192 matrix, on the fixed generation carrier `W` (the `j=1` self-dual
triplet of the gamma-traceless Rarita-Schwinger module of `Cl(9,5)`, split `14 = 4 + 10`,
frame `so(4)` compact, internal `so(5,5)` split). Finite dimension makes the topology
trivial: no boundedness, continuity, or closure conditions are needed or assumed -- this
is the WHOLE antilinear operator space of the carrier, a 73728-real-dimensional vector
space, not a finite candidate list.

**Admissibility (the structures the paper's physical argument actually uses):**
- **(A1) carrier-preserving** -- operators live on (or compress to) the 192-dim carrier
  with zero leakage, as in the enum-completeness census;
- **(A2) Krein compatibility** = the antiunitary condition stated correctly for antilinear
  maps: `k(Cx, Cy) = lambda conj(k(x, y))` for all `x, y`, i.e. `M^dag K M = lambda K-bar`
  with `lambda` real nonzero (`+1` Krein-antiunitary, `-1` anti-antiunitary, general
  `lambda` the conformal closure). On this carrier **A2 is ghost-grading compatibility**:
  the ghost sector enters the carrier kinematics only through the hyperbolic 50/50 Krein
  pairing (`canon/ghost-parity-krein-synthesis.md`), so respecting the ghost structure is
  exactly respecting `K`. (The conjugate matters: `||Im K|| = 10.4`, `K-bar != K`; the
  correct `K-bar` form was caught and fixed during this pass.)
- **(A3) Wigner/Kramers normalization**: `C^2 = eps I`, `eps = +-1` (the paper's escape
  has `eps = -1`); tracked separately because the theorem below does not need it;
- **(A4) chiralizer shape**: a nonzero chirality-swapping component
  (`C Gamma_c = -Gamma_c C` in the pure case) -- the AZ-CII-type re-grading direction, the
  one antilinear shape Theorem 2 leaves open, mapping between chirality sectors so as to
  permit an odd net index.

**Frame-triviality (the paper's criterion, formalized):** `C` is frame-trivial iff it
commutes with every tangent-frame `so(4)` rotation: `M rho(f)-bar = rho(f) M` for all six
frame generators (this is the paper's computed criterion "`max ||[J_quat, any
tangent-frame rotation]|| = 0.00e+00`" in the correct antilinear form). The frame charge
`fc(C) = max_f ||M rho(f)-bar - rho(f) M||` vanishes iff `C` is frame-trivial.

**The class:** `S` = A1 + A2 (with A3/A4 analyzed as refinements inside it). `S` contains
every rung of the declared ladder below, down to and including fully symmetry-free
operators.

**The declared symmetry-breaking ladder** (every rung a genuine Lie subalgebra of the
sector's own `g = so(4) (+) so(5,5)`, real forms as the sector fixes them):
L0 `so(4)+so(5,5)` (full; the enum-completeness core) -> L2 `so(3)+so(5,5)` (frame broken)
-> L2b `so(5,5)` alone -> L3 `so(4)+t5` (internal broken to its split Cartan) -> L4
`t2+t5` (Cartan only) -> L1/L1b `so(4)+so(5,4)/so(4,5)` (internal broken to the two so(9)
forms) -> L5 `so(3)+so(5,4)` (both broken -- the adversarial rung) -> L6 symmetry-free.
A monotonicity lemma (`h in h'` implies `Anti_h'(W) in Anti_h(W)`) makes L2b close every
rung containing `so(5,5)`; each rung is also computed directly.

## Step 2 -- the decision per rung (computed; independently re-verified)

| rung | anti dim | swap dim | frame charge of swaps | decision |
|---|---|---|---|---|
| L0 `so(4)+so(5,5)` | 2 | 0 | -- | (i) PROOF: no chiralizer shape exists (re-verifies enum-completeness) |
| L2 `so(3)+so(5,5)` | 4 | 0 | -- | (i) PROOF |
| L2b `so(5,5)` alone | 72 | 0 | -- | (i) PROOF + monotonicity |
| L3 `so(4)+t5` | 32 | 0 | -- | (i) PROOF (split weights conjugation-fixed) |
| L4 `t2+t5` Cartan-only | 192 | 0 | -- | (i) PROOF |
| L1 `so(4)+so(5,4)` | 4 | 2 | 0 (forced by equivariance) | (ii) certificate: swaps exist but are frame-trivial BY EQUIVARIANCE; strict admissibility (A2 AND A3): NON-EXISTENCE by the exact C5 certificate |
| L1b `so(4)+so(4,5)` | 4 | 2 | 0 (forced) | (ii) same |
| L5 `so(3)+so(5,4)` | 8 | 4 | ~20 (frame-ACTIVE) | (ii) certificate: frame-active swaps exist; strict A2+A3 not found (search-grade, 120 deterministic starts, not load-bearing); rung CLOSED by the index-nullity theorem |
| L6 symmetry-free | full space | -- | arbitrary | (a) THEOREM (Step 3) |

Highlights: (1) the chiralizer *shape* (an antilinear swap) exists equivariantly only when
the internal algebra is broken to an `so(9)` form -- the exact rep-theoretic reason is
that the split-form `16` and `16bar` have disjoint (real, conjugation-fixed) weight sets
that merge on restriction to `B4`; the entire dimension table above is reproduced by
**exact integer weight/Clebsch combinatorics** in the verify script. (2) Wherever the
frame `so(4)` survives, every swap candidate is frame-trivial *by equivariance* -- the
paper's frame-non-trivial escape is structurally excluded at those rungs, not hunted away.
(3) At L1/L1b the closed-form C5 certificate decides strict admissibility exactly: the A3
(Kramers) system is solvable on the swap span, but the joint A2 magnitude constraint
`uv = |z|^2` fails (exact linear algebra) -- **no strict admissible swap exists at any
rung with an unbroken frame**.

## Step 3 -- the symmetry-free bound: the index-nullity theorem

**Theorem (antilinear index nullity on S).** *For every antilinear `C = M . conj` with
`M^dag K M = lambda K-bar` (`lambda` real nonzero): (1) `M` is invertible; (2) the images
`C(W_+), C(W_-)` form a K-Lagrangian complementary pair -- they are the eigenspaces of the
C-induced re-grading `Gamma_C = C Gamma_c C^-1`; (3) every physical subspace `P` (maximal
K-positive, dim 96) meets both in `0` only; (4) hence the net chiral index of `P` is
EXACTLY 0 in the re-graded chirality -- and in the original (Theorem 2's operator-free
graph argument). Corollary: **no admissible antilinear chiralizer exists in S** --
equivariant or not, frame-trivial or frame-active, `C^2 = -1` or not.*

*Proof.* (1) `K`, `K-bar` invertible and `lambda != 0`. (2) For `x, y` in `W_+`:
`k(Cx, Cy) = lambda conj(k(x, y)) = 0` because `W_+` is K-isotropic (the Krein form is
purely cross-chirality); so `C(W_+)` is K-isotropic of maximal dimension 96, i.e.
K-Lagrangian; same for `C(W_-)`; bijectivity gives the direct sum; `Gamma_C` is linear,
squares to `I`, and fixes the images. (3) A K-positive vector cannot be K-null. (4) The
projection of `P` onto `C(W_+)` along `C(W_-)` has kernel `P ^ C(W_-) = 0`, hence is an
isomorphism onto a 96-dim image; same for the other side; `chi_C(P) = 96 - 96 = 0`. QED.

**Non-vacuity (the decisive honest point).** The operator the paper hunted -- a
frame-non-trivial antilinear class-CII chiralizer candidate -- **exists** in S once all
symmetry is dropped. The bound script constructs, in closed form, strict witnesses for all
four sign patterns `(C^2, lambda) = (+-1, +-1)`: in a Lagrangian pairing basis `Q`
(`Q^dag K Q = [[0,I],[I,0]]`), `M = Q S conj(Q)^-1` with `S = [[0, A], [eps conj(A)^-1,
0]]` and `A = (lambda*eps) A^T`; then `M M-bar = eps I` and `M^dag K M = lambda K-bar`
hold identically. The `(-1, +1)` witness is exactly the AZ-CII shape (Kramers,
Krein-antiunitary, chirality-swapping) with frame charge `fc ~ 19` (frame-ACTIVE) and
internal non-equivariance `~10`. Together with Krein-unitary dressings (class-S members
beyond the Wigner-normalized subset), 8 operators x 4 random physical subspaces give
`chi_C(P) = 0` as exact integer ranks, isotropy residuals `~3e-14`. **Existence was never
the issue: Krein compatibility alone pins the index at 0.** The hunt found no forcing
operator because there is provably none to find -- in the entire class, not merely among
tested candidates.

**Where nonzero counts actually live (sharpness).** The only selections carrying nonzero
graded content are K-NULL, unphysical ones -- e.g. `W_+` itself with the paper's vectorlike
`+96` (Gram norm `1e-14`: it contains no physical state). Definiteness transport:
`k(Cx, Cx) = lambda k(x, x)`, so class-S operators map physical subspaces to
`(+/-)`-definite subspaces (verified: image Grams exactly `+-1`) and can never reach a
K-null selection. A D1-style control shows the selection trace varies continuously
(`-96.000 -> -95.750` along a Krein-unitary path): a tunable overlap, not an index.

## The outside-class residual (one sentence, as the card demands)

**No admissible antilinear chiralizer exists in S (S = all Krein-compatible antilinear
operators on the 192-dim carrier, `M^dag K M = lambda K-bar`, `lambda` real nonzero --
every covariance from full `so(4)+so(5,5)` down to symmetry-free, with no square or
continuity assumption); outside S, admissibility itself fails, because an antilinear
operator that breaks Krein/ghost compatibility does not act on the sector's physical
states at all (a computed control maps a physical subspace to an indefinite-Gram image),
so "net count of physical chiral states" is undefined for it by the paper's own criteria;
the one genuinely open remainder is the function-space setting (sections, Fredholm
indices, spectral flow), which is the separate card WC-FUNCTION-SPACE-EXT.**

## What this changes and does not change

- **The paper's caveat (d) upgrades** from "the antilinear non-existence leg is an open
  finite adversarial hunt, not a closed proof" to "closed over the delimited class S at
  proof grade (finite-dimensional; machine-certified premises and adversarial
  instantiation); residual: non-Krein antilinear operators (admissibility fails by
  definition) and the function-space extension." Paper edits applied (v2.5.2, both
  copies, minimal).
- **The paper's Section 6 hunt classification is confirmed and explained**: its
  "chirality-reversing (net 0)" category is now a theorem covering the entire class; its
  frame-charge analysis (gauge dressings, `p_1 = 0`) remains correct but is no longer
  load-bearing for the antilinear leg -- frame-activity is irrelevant to forcing inside S.
- **The enum-completeness result extends**: the equivariant core (no antilinear re-grading
  in class C) now sits at the top of a decided ladder; the non-equivariant residual that
  card named is closed.
- **Nothing here forces or forbids three generations**, and nothing touches the
  function-space setting.

## Honest caveats

1. The index-nullity theorem is finite-dimensional kinematics on the explicit carrier; its
   premises (cross-chirality `K`, signature `(96,96)`) are machine-certified with printed
   residuals, not derived symbolically from axioms. A Lean port would upgrade the grade.
2. One cell is search-grade and flagged: strict (A2 AND A3) admissibility at L5 (120
   deterministic Gauss-Newton starts on the exact structure-constant system found
   nothing). The rung's closure does not depend on it.
3. The (14,0) Euclidean control shows the theorem's premise is load-bearing: where `K` is
   grading-aligned rather than cross-chirality, a physical subspace does carry
   `|chi| = 96`. The theorem is a fact about this sector's Krein structure, not a
   tautology.
4. The Hom censuses are exact-in-effect numerics (spectral-gap certified) whose dimension
   table is independently reproduced by exact integer combinatorics; the two decisive
   rungs are recomputed on an independent substrate.
5. This bounds operators ON the fixed carrier; external backgrounds, spurion VEVs, added
   symmetries, and non-sector twists are outside by construction (they are the enum-
   completeness engine's category C, and the paper's "external on present evidence"
   conclusion is about exactly that channel).

## Integrity

The strongest available adversarial finding was PUBLISHED, not suppressed: admissible
frame-active antilinear CII swap operators exist symmetry-free and are exhibited in closed
form -- a fact the paper's hunt language ("none was found") could be misread to deny. The
finding does not gate the paper the other way: the same pass proves none of them is a
chiralizer (index exactly 0, every physical subspace, both gradings). A formalization
error in this pass's own first draft (Krein-antiunitarity as `M^dag K M = lambda K`
instead of `lambda K-bar`) was caught by reality-checking `K` (`||Im K|| = 10.4`) and
fixed before any result was recorded; the L1/L1b certificates were recomputed after the
fix. The one search-grade cell is labeled as such and carries no load. No number was
fitted; the only target integers anywhere are the carrier's own `(+96, -96)` and `0`.
