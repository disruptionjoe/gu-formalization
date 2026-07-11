# One Residual: A Geometric Framework Accommodates Known Physics With All Remaining Freedom in a Single Source-Action Declaration

**Draft-of-record, started 2026-07-11.** Subsumes the located-not-forced generation-count result (which
becomes one leg here). Every clear is stated at its honest grade -- *existence / consistency*, not
derivation. Geometric Unity (GU) is the concrete instance; the load-bearing structural claim (everything
reduces to one residual) is stated so it holds for **any** geometry that fits, so a reader need not accept
GU. This is NOT a claim that GU (or any geometry) is proven, nor a derivation of all of physics.

## Abstract

We report a structural result about a candidate geometric-unification framework and its relation to the
five sectors it must account for -- the Standard Model gauge group and content, the forces, quantum
(indefinite-metric) structure, dark energy, and gravity. Under an adversarial program that granted a
working source action and then tried to *falsify* each sector, **no sector falsifies the framework**, and
**four of five are cleared at existence/consistency grade**: (i) the Standard Model gauge algebra arises
*exactly* -- the maximal compact of the ambient `su(3,2)` is `su(3)+su(2)+u(1)` with a single `u(1)` and no
extra photon (reproducible computation), and the forced mirror matter is vectorlike, anomaly-free, and
mass-liftable; (ii) the forces follow from the same maximal-compact selection, avoiding the "28-photon"
adjoint-breaking catastrophe; (iii) quantum structure is unitary-repairable on the indefinite (Krein)
inner product (a positive-definite physical sector and a Krein-unitary generator exist); (iv) dark energy
is consistent with DESI (a previously-reported sign conflict was a code error; the corrected fit shares
DESI's sign). The fifth sector, gravity, is *not* cleared but *reduced*: one conservative branch is newly
eliminated by exact computation, leaving a single undetermined scalar (an ambient-curvature Willmore-EL
coefficient). The central finding is that **the four cleared sectors' remaining freedom, the one open
gravity scalar, and the fermion generation count are the same object**: the source action's field-space
declaration, a rigid, finite residual. The generation count is *located, not forced* -- a special case.
The framework thus **closes up to one precisely-characterized object**, and we exhibit that object. We do
not claim the framework is proven; we claim it is not falsified on any sector and that its entire residual
freedom is localized in one place.

## 1. What is and is not claimed

- **Claimed:** no sector falsifies the framework; four sectors are consistent and the structures they
  require provably *exist*; the total remaining freedom across all sectors is a single object (the source
  action's field-space declaration), which we characterize (rigid, finite, a bounded discrete/parametric
  residual).
- **Not claimed:** that the framework *derives* the Standard Model / forces / dark energy (it accommodates
  them and the required structures exist -- *which* the dynamics selects is the residual); that gravity is
  closed (it is reduced to one scalar); that three generations are *forced* (they are located, not forced);
  that the framework is GU-specific (the reduction-to-one-residual is geometry-agnostic).
- **Grade discipline:** GU's scaffold is partly reconstruction-grade (read from a spoken account, not a
  written action). Existence/consistency clears are marked as such and never called derivations.

## 2. The five sectors

### 2.1 Standard Model gauge group and content -- CLEARED (existence)
The ambient pseudo-unitary structure selects its gauge algebra by a maximal-compact / Cartan-involution
mechanism (the framework's native indefinite-metric / Krein form), not adjoint-Higgs breaking. The maximal
compact of `su(3,2)` is **exactly** `su(3)+su(2)+u(1)` -- 12 generators, block-diagonal, precisely one
`u(1)`, no extra photon (`tests/legs/forces_maximal_compact_is_sm.py`, exit 0). Independently, a
Pati-Salam rank-one breaking vector has stabilizer exactly the SM algebra (dim 12, rank 4). The forced
mirror generation is vectorlike (`16 (+) 16bar`), anomaly-free in all four SM channels, and gappable at a
free modulus above collider bounds -- the textbook-safe way to add matter, not an unobserved light state.

### 2.2 Forces -- CLEARED (existence)
Same maximal-compact selection. The "28-photon catastrophe" requires rank-preserving *adjoint-only*
breaking, which the framework does not use; so no extra gauge boson / fourth force is structurally forced,
and a breaking to exactly the SM forces exists and is admissible.

### 2.3 Quantum structure / unitarity -- CLEARED (existence)
The matter inner product is indefinite (Krein). A concrete unitarity *repair* exists: the physical sector
is positive-definite and a Krein-unitary generator (`S^dag K S = K`) exists. No forced negative-probability
violation. (The generalized-Born-rule quantization layer is imported; the framework supplies the Krein
kinematics, and unitary QM is recoverable on it.)

### 2.4 Dark energy -- CLEARED (consistency)
A dynamical, equivariant scalar replaces the static cosmological constant. A previously-reported sign
conflict with DESI was a code error (a hardcoded density-slope); the corrected, independently re-verified
fit over the DESI window is `w_0 = -0.777, w_a = -0.248` -- the *same sign* as DESI (`w_a = -0.75`). The
sector is LCDM-degenerate (amplitude a fit), so it does not yet make a *distinguishing* prediction, but it
is consistent with data, not falsified.

### 2.5 Gravity -- OPEN, reduced (not cleared, not falsified)
The gravitational sector is the section-shape equation; exact strong-field solutions (Schwarzschild/Kerr)
are the target. Weak field is compatible (leading Willmore-EL residual vanishes by harmonicity; solar-
system PPN smallness holds a fortiori). Exact computation newly *eliminates* one conservative branch (bare
source `D_A*F_A = theta`: a nonzero geometric `theta ~ M/rho^2` forces a divergent gauge action, mutually
exclusive with a finite-action field), leaving a single surviving branch whose fate hinges on **one
undetermined scalar** -- the sign/coefficient of the ambient-curvature (`R^Y.B`) term in the Willmore
Euler-Lagrange variation at `O(M^2/r^4)`. That coefficient is fixed only by a written, branch-fixed source
action.

## 3. The generation count as one instance (subsumes "located, not forced")

The fermion generation count is not forced by the framework's structure; it is *located* -- a rigid,
finite 2-bit residual of the source action's field-space declaration, provably a boundary quantity in the
odd-primary summand (the primary-partition no-go + the no-net-chirality-without-a-boundary principle;
`tests/family-puzzle/primary_partition_lemma.py`, `tests/nielsen-ninomiya/`). This is the same *kind* of
object as the gauge-vacuum selection (Sec. 2.1-2.2) and the gravity scalar (Sec. 2.5): a selection the
dynamics makes, not a contradiction.

## 4. The central result: everything reduces to one object

Collecting the open freedom across all five sectors:
- **gauge-vacuum / sub-block selection** (which theta-stable block / breaking vacuum) -- source-action-gated;
- **the generation count** -- a rigid finite residual of the source-action field-space declaration;
- **the gravity scalar** -- a coefficient of the branch-fixed source action.

These are **one object**: the source action's field-space declaration. The framework therefore **closes up
to a single, precisely-characterized, currently-unwritten object**, and no sector falsifies it. This is the
generalization of "located, not forced" from the generation count to the *entire* residual freedom of the
framework.

## 5. Geometry-agnostic core (why a skeptic need not accept GU)

The reduction-to-one-residual is not a GU claim. Any geometry that accommodates the five sectors faces the
same structure: its dynamics (source action) is the single object that selects the gauge vacuum, fixes the
strong-field gravitational coefficient, and declares the generation-sector field space; and the generation
count is a boundary quantity in the odd-primary summand *regardless of the geometry* (Sec. 3, GU-independent).
So the load-bearing statement -- *a geometric unification's entire residual freedom localizes in one
source-action object, of which the generation count is a boundary/odd-primary instance* -- holds whether or
not GU is the correct geometry. GU is the concrete carrier that let us compute it.

## 6. What would close it (the single construction problem)

One object decides everything remaining: a **forced/derived** source action written with fixed coefficients.
It simultaneously (a) fixes the gravity scalar -- CLEAR (a 5/5 complete picture) or DISPROOF (a clean
strong-field falsification, telling us exactly where a nearby geometry must differ) -- and (b) pins the
generation count and the gauge vacuum. A *free* build p-hacks the residual (established); the honest form
is a forced construction, for which no armchair mechanism was found (a complete forcing rubric + an
out-of-rubric hunt came up empty). The residual is thus real, finite, and not resolvable without building
the object.

## 7. Relation to prior work / honest boundary

The generation-count sub-result relates to the family-puzzle bordism literature (Garcia-Etxebarria-Montero;
Wang; Wan-Wang-Yau) via the primary-partition reading. The Standard-Model embedding is standard
SO(10)/Pati-Salam representation theory verified for consistency (not a novel SM derivation). The Krein /
indefinite-metric quantization draws on generalized-Born-rule work. The novel content is (i) the
reduction-of-all-residual-freedom-to-one-object result, (ii) the boundary/odd-primary localization of the
count, and (iii) the adversarial no-falsification-across-sectors finding at honest grade.

## Status / open gaps before submission

1. Re-land the SM Pati-Salam stabilizer and gravity Branch-2A elimination as reproducible in-repo tests
   (forces/SM maximal-compact already landed).
2. Grade each sector precisely in the text (existence vs consistency vs reduced) and carry the
   reconstruction caveat.
3. Settle the gravity scalar via the branch-fixed source action -> upgrades to 5/5 or a clean gravity
   disproof (either strengthens the paper).
4. Full literature comparison for the reduction-to-one-residual and boundary-localization novelty claims.
5. Figures: the sector scoreboard; the maximal-compact = SM computation; the primary-partition table.

Grade: structural result at honest grade; four sectors existence/consistency-cleared (one reproducible),
gravity reduced-not-cleared, the reduction-to-one-object is the contribution. Target: hep-th / math-ph.
External publication Joe-gated. Supersedes/subsumes
`papers/candidates/generation-number-boundary-odd-primary/` and the located-not-forced draft as legs.
