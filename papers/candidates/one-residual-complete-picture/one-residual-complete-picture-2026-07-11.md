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
**four of five are cleared at existence/consistency grade**: (i) the Standard Model gauge algebra is
realized *exactly* as the maximal compact of the ambient `su(3,2)` -- `su(3)+su(2)+u(1)`, a single `u(1)`,
no extra photon (reproducible; `su(3,2)` is a non-native sub-block, so *which* sub-block the dynamics
selects is itself the residual), and the forced mirror matter is anomaly-free (four SM traces vanish,
computed) and -- by standard SO(10) representation theory -- vectorlike and mass-liftable; (ii) the same
maximal-compact selection *admits* exactly the SM forces (a breaking to exactly them exists), avoiding the
"28-photon" adjoint-breaking catastrophe; (iii) quantum structure is unitary-repairable on the indefinite
(Krein) inner product (a positive-definite physical sector and a Krein-unitary generator exist, on a
faithful model); (iv) dark energy is *consistent* (sign only) with the DESI CPL combo (`w_a=-0.75`,
arXiv:2404.03002): the corrected, re-verified fit shares the sign (`w_a<0`), though it is
LCDM-amplitude-degenerate (`f_0` a tuned fit) and its equation-of-state machinery is reconstruction-grade.
The fifth sector, gravity, is *not* cleared but *reduced*: one conservative branch is newly eliminated by
exact computation, leaving a single undetermined scalar (an ambient-curvature Willmore-EL coefficient). The
central finding is that **the four cleared sectors' remaining freedom, the one open gravity scalar, and the
fermion generation count are jointly fixed by one object**: the source action (its field-space declaration
together with its fixed coefficients), a rigid, finite residual. The generation count is *located, not forced* -- a special case.
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
- **Grade discipline (per sector, not a blanket caveat):** *reconstruction-grade* (read from a spoken
  account, not a written action) = the dark-energy equation-of-state machinery, the forces-selection
  mechanism, and the gravity source law; *computed on a faithful model* = the quantum (Krein) repair;
  *standard / existence-computed* = the group theory (maximal compact, Pati-Salam stabilizer, anomaly
  traces). Existence/consistency clears are marked as such and never called derivations.

## 2. The five sectors

### 2.1 Standard Model gauge group and content -- CLEARED (existence)
The ambient pseudo-unitary structure **contains** the SM gauge algebra exactly as its maximal compact via
the Cartan-involution / Krein form (not adjoint-Higgs breaking); *which* sub-block/vacuum the dynamics
selects is source-action-gated (the residual). The maximal compact of `su(3,2)` is **exactly**
`su(3)+su(2)+u(1)` -- 12 generators, block-diagonal, precisely one `u(1)`, no extra photon
(`tests/one-residual/forces_maxcompact_independent.py`, `tests/legs/forces_maximal_compact_is_sm.py`,
exit 0). **Caveat:** `su(3,2)` is a non-native standalone sub-block -- GU's native internal algebra is
`so(5,5)`, whose maximal compact `so(5)+so(5)` is *not* the SM; that `su(3,2)` is the selected block is
part of the residual, not derived. Independently, the Pati-Salam rank-one breaking vector has stabilizer
exactly the SM algebra (dim 12, rank 4, one `u(1)`; identified by invariant fingerprint, not an explicit
isomorphism -- `tests/one-residual/sm_pati_salam_stabilizer.py`, exit 0). The forced mirror generation's
four SM anomaly traces vanish exactly (`tests/one-residual/sm_mirror_anomaly_free.py`, exit 0); its
vectorlike (`16 (+) 16bar`) content and mass-liftability above collider bounds are standard SO(10)
representation theory (not a computed result here) -- the textbook-safe way to add matter, not an
unobserved light state.

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
A dynamical, equivariant scalar replaces the static cosmological constant. The corrected,
independently re-verified CPL fit over the DESI window (`z<=2`) is `w_0 = -0.777, w_a = -0.248` -- the
*same sign* as the DESI CPL combo (`w_a = -0.75`, CMB+DESI+SNe, arXiv:2404.03002)
(`tests/one-residual/dark_energy_desi_sign.py`, exit 0). Honest scope: this is a **sign-only** consistency
result -- the sector is LCDM-amplitude-degenerate (`f_0` and the `B_i` are tuned fits, not GU predictions),
the equation-of-state machinery is reconstruction-grade, and **the live canon verdict on this sector is
OPEN**. It is consistent with data, not falsified, and makes no distinguishing prediction yet.

### 2.5 Gravity -- OPEN, reduced (not cleared, not falsified)
The gravitational sector is the section-shape equation; exact strong-field solutions (Schwarzschild/Kerr)
are the target. Weak field is compatible (leading Willmore-EL residual vanishes by harmonicity; solar-
system PPN smallness holds a fortiori). Exact computation newly *eliminates* one conservative branch (bare
source `D_A*F_A = theta`: a nonzero geometric `theta ~ M/rho^2` forces a divergent gauge action, mutually
exclusive with a finite-action field), leaving a single surviving branch whose fate hinges on **one
undetermined scalar** -- the sign/coefficient of the ambient-curvature (`R^Y.B`) term in the Willmore
Euler-Lagrange variation at `O(M^2/r^4)` (`tests/one-residual/gravity_branch2a_eliminated.py`, exit 0).
That coefficient is fixed only by a written, branch-fixed source action. **Reconstruction-grade caveat:**
the branch's defining source law `D_A*F_A = theta` and the identification `theta = d log(Psi)` are
reconstruction-grade; the `M/rho^2` scaling and the finiteness-vs-divergence exclusivity that eliminates
Branch 2A are robust.

## 3. The generation count as one instance (subsumes "located, not forced")

The fermion generation count is not forced by the framework's structure; it is *located* -- a rigid,
finite 2-bit residual of the source action's field-space declaration. Two grades, kept separate: it is
**provably a rigid, finite residual** by the primary-partition no-go (`Hom(Z/3,Z)=0`; elementary/folklore
CRT arithmetic, genuinely computed, `tests/family-puzzle/primary_partition_lemma.py`), and it is
**located** in the odd-primary boundary summand at **principle grade** under the no-net-chirality-needs-a-
boundary principle (Nielsen-Ninomiya / Callan-Harvey / Kaplan; not proven for the true RS/`Y14`-bundle
index). The 3-primary localization of the count is **prior art** (Garcia-Etxebarria-Montero arXiv:1808.00009;
Wan-Wang-Yau arXiv:2605.26202); our delta is the 2-primary-blindness *no-go census* plus the *boundary*
conjunction. This is the same *kind* of object as the gauge-vacuum selection (Sec. 2.1-2.2) and the gravity
scalar (Sec. 2.5): a selection the dynamics makes, not a contradiction.

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

Each novelty bullet names its nearest precedent and precise delta:
- **(i) Reduction of all residual freedom to one source-action object.** Nearest precedent: the
  string-landscape / moduli-stabilization / vacuum-selection literature (Douglas; Susskind hep-th/0302219;
  KKLT), where the low-energy content is likewise a selection the (flux/moduli) dynamics makes. Delta: we
  do not posit a landscape; we show, for one candidate geometry, that *every* residual (gauge vacuum, count,
  gravity coefficient) collapses to the *single* source-action object and characterize it (rigid, finite).
  Honest boundary: in field theory "a theory is its action" is near-truism; the content is the explicit
  conjunction across sectors, not a new general theorem.
- **(ii) Odd-primary/boundary localization of the count.** Nearest precedent: Garcia-Etxebarria-Montero
  (arXiv:1808.00009) and Wan-Wang-Yau (arXiv:2605.26202) already locate the count in the 3-primary summand.
  Delta: the 2-primary-blindness *no-go census* (which standard tools *cannot* force an odd count) conjoined
  with the *boundary* (anomaly-inflow) localization. The 3-primary localization alone is not new.
- **(iii) Adversarial no-falsification-across-sectors at honest grade.** The Standard-Model embedding is
  standard SO(10)/Pati-Salam representation theory verified for consistency (not a novel SM derivation);
  the Krein/indefinite-metric quantization draws on generalized-Born-rule work. The novel content is the
  reproducible, honestly-graded, no-sector-falsifies map itself.

## Status / open gaps before submission

1. **DONE:** all six clears are reproducible in-repo tests (`tests/one-residual/`, all exit 0) --
   SM stabilizer, mirror anomaly-traces, QM Krein repair, dark-energy sign, gravity Branch-2A, forces
   max-compact; grades corrected to honest per the Hardening pass ledger above.
2. **DONE (this pass):** per-sector grading + reconstruction map + prior-art distinctions folded into the
   body (Secs 1, 2.1, 2.4, 2.5, 3, 7).
3. **Two genuine remaining gaps:** (a) compute the mirror `16bar` content / mass-lift honestly (the current
   `n_L-n_R=0` check is a definitional tautology; restated as standard rep theory for now); (b) a real
   `so(10)` cubic-Casimir test *or* drop the umbrella (currently dropped in the text).
4. **The load-bearing open object:** settle the gravity scalar via the branch-fixed source action ->
   upgrades to 5/5 or a clean gravity disproof (either strengthens the paper). Same object pins the count.
5. Figures: the sector scoreboard; the maximal-compact = SM computation; the primary-partition table.

Grade: structural result at honest grade; four sectors existence/consistency-cleared (one reproducible),
gravity reduced-not-cleared, the reduction-to-one-object is the contribution. Target: hep-th / math-ph.
External publication Joe-gated. Supersedes/subsumes
`papers/candidates/generation-number-boundary-odd-primary/` and the located-not-forced draft as legs.
