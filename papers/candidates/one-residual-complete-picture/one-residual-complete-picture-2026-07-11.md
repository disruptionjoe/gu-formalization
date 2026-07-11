# One Residual: A Geometric Framework Accommodates Known Physics With All Remaining Freedom in a Single Source-Action Declaration

**Draft-of-record, started 2026-07-11.** Subsumes the located-not-forced generation-count result (which
becomes one leg here). Every clear is stated at its honest grade -- *existence / consistency*, not
derivation. Geometric Unity (GU) is the concrete instance; the load-bearing structural claim (everything
reduces to one residual) is stated so it holds for **any** geometry that fits, so a reader need not accept
GU. This is NOT a claim that GU (or any geometry) is proven, nor a derivation of all of physics.

## Hardening pass (2026-07-11) -- these corrections GOVERN the body

A 17-agent adversarial hardening (reproduce -> hostile-verify -> audit -> critic) ran on this draft.
**Outcome: no load-bearing claim FAILED, all six cited computations reproduce (exit 0), but several grades
were inflated and are corrected here; these corrections take precedence over any stronger phrasing below
until the body is line-edited.**

**Reproducible-test ledger** (all in `tests/one-residual/`, exit 0, independently verified as real
non-circular computation):

| Claim | Grade (corrected) | Test |
|---|---|---|
| max compact of `su(3,2)` = `su(3)+su(2)+u(1)`, 12 gens, one U(1) | existence (2 disjoint methods) | `forces_maxcompact_independent.py` + `tests/legs/forces_maximal_compact_is_sm.py` |
| Pati-Salam rank-one stabilizer = SM algebra (dim 12, rank 4) | existence (fingerprint match, not explicit iso) | `sm_pati_salam_stabilizer.py` |
| mirror generation: four SM anomaly traces vanish | **existence** (was mis-graded "theorem") | `sm_mirror_anomaly_free.py` |
| Krein unitary repair exists (positive-definite physical sector + Krein-unitary generator) | existence (on a faithful model; standard linear algebra) | `qm_krein_unitary_repair.py` |
| theta-field CPL fit shares DESI **sign** over z<=2 (`w_a<0`) | **consistency, SIGN-ONLY** (LCDM-degenerate; `f_0` a tuned fit) | `dark_energy_desi_sign.py` |
| gravity Branch 2A eliminated (finiteness vs nonzero-theta exclusivity) | disproof of ONE branch (conditional on reconstruction-grade source law) | `gravity_branch2a_eliminated.py` |

**Corrections that govern the body:**
1. **No derivation verbs.** The SM/forces sectors are *realized as / contain / admit* their structures at
   EXISTENCE grade, not "derive / arise / follow from / select". *Which* vacuum/sub-block the dynamics
   picks is the residual.
2. **`su(3,2)` is a non-native sub-block.** GU's native internal algebra is `so(5,5)`, whose maximal
   compact `so(5)+so(5)` is NOT the SM. The SM-as-maximal-compact result is a property of the chosen
   `su(3,2)` sub-block; that this is the selected one is itself source-action-gated (do not claim otherwise).
3. **Dark energy: do NOT head "CLEARED" -- the live canon verdict is OPEN.** State: consistency, SIGN-only,
   LCDM/amplitude-degenerate, `f_0`/`B_i` tuned fits (not GU predictions), EOS machinery reconstruction-grade.
   DESI `w_a=-0.75` is the CMB+DESI+SNe CPL combo (arXiv:2404.03002). The "historical +1.17 was a hardcoded
   slope bug" claim is NOT independently reproduced here -- state only that the corrected fit shares the sign.
4. **Two sub-claims are NOT established and must be dropped/restated:** (a) the mirror "vectorlike
   `n_L-n_R=0`" check is a definitional tautology (16-16 by construction) -- restate vectorlikeness as
   standard SO(10) representation theory, not a computed result; (b) the "so(10) has no independent cubic
   Casimir" umbrella is asserted, never computed -- drop the umbrella; keep only the SM-trace vanishing.
5. **Novelty downgrade.** The 3-primary localization of the count is PRIOR ART (Garcia-Etxebarria-Montero
   arXiv:1808.00009; Wan-Wang-Yau arXiv:2605.26202); our delta is only the no-go/blindness census + the
   *boundary* conjunction. The central "all residual freedom localizes in one selection the dynamics makes"
   has precedent in the string-landscape / moduli-stabilization / vacuum-selection literature (Douglas;
   Susskind hep-th/0302219; KKLT); distinguish rather than claim a novel general theorem.
6. **"One object" is a conjunction, not an identity.** The residuals are *jointly fixed by* a single object
   -- the source action (its field-space declaration TOGETHER WITH its fixed coefficients) -- not literally
   "the same object".
7. **Boundary-localization is principle-grade** (Nielsen-Ninomiya / Callan-Harvey / Kaplan), not proven for
   the true RS/`Y14`-bundle index; and the family-puzzle census "predictive partition" is an author-curated
   table (a same-file string-match), not a computation -- do not cite it as computed.
8. **Reconstruction-grade map** (replace the blanket caveat): reconstruction-grade = the dark-energy EOS
   machinery, the forces-selection mechanism, and the gravity source law; computed-on-faithful-model = QM;
   standard/existence-computed = the group theory (max compact, stabilizer, anomaly traces).

Readiness: **NEEDS FIXES (~19 line-edits), not publication-solid as written, no claim retracted.** The
spine (four sectors existence/consistency-cleared and reproducible, gravity reduced-not-cleared, all
residual freedom jointly fixed by one object) survives at honest grade.

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

### 2.4 Dark energy -- CONSISTENT, sign-only (live canon verdict is OPEN; do not head "cleared")
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

These are **jointly fixed by one object**: the source action (its field-space declaration *together with*
its fixed coefficients). The framework therefore **closes up to a single, precisely-characterized,
currently-unwritten object**, and no sector falsifies it. This is the
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
