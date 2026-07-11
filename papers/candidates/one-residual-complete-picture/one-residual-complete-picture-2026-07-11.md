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
| gravity Branch 2A eliminated (finiteness vs nonzero-theta exclusivity) | disproof of ONE branch (conditional on reconstruction-grade source law) -- *SUPERSEDED by the Wave 1-8 block below; the gravity leg is now a tree-level conditional theorem, not a single-scalar/branch reduction* | `gravity_branch2a_eliminated.py` |

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

## Wave 1-8 gravity arc (2026-07-11) -- upgrades the gravity leg to a CONDITIONAL THEOREM; this block GOVERNS Sec 2.5

An 8-wave adversarial arc (each wave: compute -> hostile-verify -> honest grade; each writeup in
`explorations/wave1..wave8/`, each check in `tests/wave1..wave8/`, all exit 0) drove the gravity leg from
"reduced to one undetermined scalar" (the state the Abstract and Sec 2.5 below were first written in) to a
**conditional theorem at tree level.** *This block supersedes the older "single undetermined Willmore-EL
coefficient / Branch-2A" framing wherever they conflict; that scalar's SIGN is now computed (Wave 7), and the
residual is no longer a scalar but a single soldering postulate plus a dimensionful scale (Wave 8).*

**Honest posture (unchanged, load-bearing).** GU is a heterodox theory most physicists do not accept. This is
a **reconstruction / audit**: *taken seriously and computed carefully, here is exactly what holds on the
gravity sector and at what grade* -- **not** an endorsement, not "GU is correct," not "gravity is proven
physics." Every clear below is **tree-level** and **conditional**; loop-level unitarity is untouched.

**The conditional theorem (state it exactly this conservatively).** *GU's gravity sector, taken seriously, is
a conditional theorem: at tree level it Stelle-clears* -- induced Einstein-Hilbert `R^X` + `Weyl^2` + a
DeWitt `Lambda`; the `|II|^2` functional forced II-class; the massive ghost's sign CONFIRMED healthy by two
independent methods; the Krein ghost-parity clears it in the Bateman-Turok sense -- ***conditional on one
natural-but-unforced soldering postulate*** (`A = spin-lift(grad^gimmel)`) ***plus the dimensionful scale***
`mu_DW`. The fermion/`C2` residual and loop-level unitarity remain open, and the dark-energy sector sits
**~3-4 sigma** from DESI. This **subsumes** the located-not-forced generation count as one facet of the single
residual.

**Wave ledger** (all `tests/waveN/*.py`, exit 0, exploration-grade, none promoted to canon):

| Wave | Claim | Grade | Test |
|---|---|---|---|
| H1 | exact Schwarzschild is Bach-flat at ALL orders in `M` (nonzero Weyl -> genuine cancellation); Kerr Ricci-flat hence Bach-flat; GU H-class spin-2 residual **is** the Bach operator (`box^2 h = -4 Bach^(1)`) | **computation** (exact sympy all-orders; Kerr exact rational identity at 4 `theta` slices) + structural (spin-2 identity) | `tests/wave1/H1_bach_flat_exact_vacua.py` |
| H9 | pure Bach = `box^2` = coincident-pole DEGENERATE (Pais-Uhlenbeck Jordan block); Bateman-Turok ghost-parity `[P,S_free]=0` holds kinematically but is non-unique at the degeneracy; Bach clears via BT **only if Stelle-type**, not pure conformal | **structural** (exact partial-fraction / commutant computation; physics gloss lower-confidence) | `tests/wave2/H9_ghost_parity_bach_sector.py` |
| H15 | Gauss identity `|II|^2 = |H|^2 - R^X`; in 4D `int R^X` is dynamical (NOT topological) -> `|II|^2` => Stelle `R+Weyl^2` (ghost clears), `|H|^2` => pure Bach (ghost open). Verdict **C (under-determined)** with a strong structural lean to `|II|^2` | **conditional computation** (each branch's consequence exact); structural for the lean | `tests/wave3/H15_gravity_fork_R_term.py` |
| H18 | II-class **FORCED** (`theta = full II_s`, action = YM full `|theta|^2`); the Clifford-odd shiab "trace-before-norm" counter **REFUTED** for the bosonic leg | **structural** (two premises P1/P2 remain reconstruction/transcript, both lean II-class) | `tests/wave4/H18_forcing_II_vs_H.py` |
| H21 | P1 (`s*(theta) = II_s`) **PROVEN off-shell**, full-tensor, in the canonical gauge (it IS the Gauss formula); the literal-vs-horizontal convention refuted as a **non-trace** additive shift (fork does not re-open) | **proven-identity** (exact-sampling / Schwartz-Zippel; off-shell), MODULO the canonical-connection/bundle identification = the soldering | `tests/wave5/H21_theta_equals_II_proof.py` |
| H16 | the wrong-sign **antigravity KILL is RETIRED** (Gauss `-R^X` -> healthy massless graviton, `m^2=+1/2>0`, attractive, positive `G`); but loop unitarity OPEN (BT tree-only; their spin-2 ghost decouples) -> **CONTESTED-CORNER** (lands on the attractive side of the Stelle-Mannheim corner) | **exact** (flat-ambient sign) + **primary-source-fenced** (loop, not computed) | `tests/wave5/H16_stelle_viability.py` |
| H24 | leading curved-ambient `R^Y` = a **computed Lambda** (0-derivative, branch-neutral) -> cannot flip the sign (retires H16's central worry); residual collapses to **one number `C_RY` vs `-1/2`**; `mu_DW` = source-action overall scale (ratios geometric, magnitude free). H24's hand-waved `C_RY<0` was flagged provisional | **computation** (leading Lambda) + honest-open (residual number deferred) | `tests/wave6/H24_RY_normalization.py` |
| H25 | `C_RY` **COMPUTED POSITIVE** by two independent methods (Gauss-ratio `+1/3`; direct `|II|^2` 2nd variation `+3/4`); `m^2_eff = 1/2 + C_RY > 1/2 > 0` -> the KILL is excluded **by SIGN**. Overturns H24's provisional `C_RY<0` | **computation** (two methods + exact H15 flat-calibration); SIGN robust, absolute magnitude normalization-gated | `tests/wave7/H25_II_first_variation_CRY.py` |
| H23 | spin-lift `so(9,5) -> End_H(S)` is the **unique canonical lift** (exact homomorphism, 91 gens, residual 0); gauge group is the **non-compact** `Sp(32,32;H)` (sharpens canon "Sp(64)"); `[P,S]=0` HOLDS (`M_D` Krein-self-adjoint) but **SIGN-BLIND**; the identification `A = spin-lift(grad^gimmel)` is **NOT FORCED** (a codim-8165 soldering postulate); `mu_DW` NOT fixed | **PARTIAL**: (A)(B)(C) exact rep-theoretic identities (residual 0); (D) the soldering is a negative result (dimension gap unambiguous) | `tests/wave8/H23_source_action_construction.py` |

**Net movement of the gravity leg:** OPEN/reduced -> **clear-MODULO-soldering at tree level.** The functional
is forced II-class (H18), P1 is proven (H21), the induced-Einstein sign survives the curved ambient by an
explicitly computed positive `C_RY` (H25, overturning the earlier hand-waved worry), and the Krein ghost
parity clears it (H23 C). What remains is exactly **one bosonic soldering postulate**
`pi = spin-lift(grad^gimmel)` (H23 D) **plus** the dimensionful `mu_DW` (H24/H25) -- both the SAME unbuilt
object as the source action. The soldering is *natural* (the reference is the unique metric-compatible
torsion-free lift) but **GU's dynamics does not supply it**, and `S = |theta|^2` does not force it (the vacuum
is not `theta = 0`). This is **strictly softer** than, and provably distinct from, the fermion sector's `C2`
wall where the generation count actually lives.

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
faithful model); (iv) dark energy is *sign-consistent* (correct quadrant, `w_a<0`) with the DESI DR2 CPL constraints,
verified against the primary source arXiv:2503.14738: GU nails `w_0` but **under-evolves** `|w_a|` (~0.27 vs
~0.86) and sits **~3-4 sigma** from DESI -- LCDM-amplitude-degenerate (`f_0` a tuned fit), its
equation-of-state machinery reconstruction-grade, and a genuine near-falsifying handle kept in the open, NOT
a clear.
The fifth sector, gravity, is upgraded by an 8-wave arc (see the Wave 1-8 block above) to a **conditional
theorem**: at *tree level* it Stelle-clears (induced Einstein-Hilbert `R^X` + `Weyl^2` + a DeWitt `Lambda`;
the `|II|^2` functional forced the II-class; the massive-ghost sign confirmed healthy by two independent
methods; the Krein ghost-parity clears it in the Bateman-Turok sense) -- **conditional on one
natural-but-unforced soldering postulate** (`A = spin-lift(grad^gimmel)`) **plus the dimensionful scale**
`mu_DW`; loop-level unitarity remains open. The central finding is that **the four cleared sectors' remaining
freedom, the gravity soldering-postulate-plus-scale, the fermion `C2`/generation residual, and the gauge
vacuum are jointly fixed by one object**: the source action (its field-space declaration together with its
fixed coefficients), a rigid, finite residual. The generation count is *located, not forced* -- a special case.
The framework thus **closes up to one precisely-characterized object**, and we exhibit that object. We do
not claim the framework is proven; we claim it is not falsified on any sector and that its entire residual
freedom is localized in one place.

## 1. What is and is not claimed

- **Claimed:** no sector falsifies the framework; four sectors are consistent and the structures they
  require provably *exist*; gravity is a **tree-level conditional theorem** (Stelle-clears conditional on one
  soldering postulate + `mu_DW`); the total remaining freedom across all sectors is a single object (the source
  action's field-space declaration together with its fixed coefficients), which we characterize (rigid, finite,
  a bounded discrete/parametric residual).
- **Not claimed:** that the framework *derives* the Standard Model / forces / dark energy (it accommodates
  them and the required structures exist -- *which* the dynamics selects is the residual); that gravity is
  *unconditionally* closed (it is a tree-level conditional theorem, conditional on the soldering postulate
  `A = spin-lift(grad^gimmel)` + `mu_DW`; loop-level unitarity is open); that dark energy is confirmed (it is
  sign-consistent but ~3-4 sigma from DESI); that three generations are *forced* (they are located, not
  forced); that GU is correct or proven -- this is a reconstruction/audit of a heterodox theory, at honest
  grade; that the framework is GU-specific (the reduction-to-one-residual is geometry-agnostic).
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
four SM anomaly traces vanish exactly (`tests/one-residual/sm_mirror_anomaly_free.py`), now grounded in the
**computed** vanishing of the `so(10)` cubic Casimir on the 16 (`max_abc |Tr({Sigma_a,Sigma_b}Sigma_c)| =
0`, `tests/one-residual/sm_so10_cubic_casimir_and_mirror.py`) -- the real reason one-generation anomalies
cancel; and the `16bar` is exhibited as the genuine charge-conjugate mirror (its full 5-Cartan weight
system is the negatives of the 16's), a real vectorlike pair rather than a definitional tautology.
Mass-liftability above collider bounds is standard -- the textbook-safe way to add matter, not an
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

### 2.4 Dark energy -- CONSISTENT in sign, but ~3-4 SIGMA from DESI (live canon verdict OPEN; do not head "cleared")
A dynamical, equivariant scalar replaces the static cosmological constant. The theta-sector point
(`f_0 = 0.125`) is `(w_0, w_a) = (-0.768, -0.273)` (`tests/one-residual/dark_energy_desi_sign.py`, exit 0;
the DESI DR2 CPL constraints were verified against the **primary source** arXiv:2503.14738 Eqs. (26)-(28) in
`tests/wave1/H3_desi_verified_and_intersection.py`, exit 0). Two honest facts, both kept in plain sight:
- **Positive:** GU **nails `w_0`** (`-0.768` vs DESI+CMB+DESY5 `-0.752`, `-0.28` marginal-sigma) and sits in
  the **correct quadrant/sign** (`w_a < 0`), distinguishing it from LCDM and from `w<-1` phantom models.
- **Negative (load-bearing, do not bury):** GU **under-evolves** -- it predicts `|w_a| ~ 0.27` where DESI
  wants `~0.86`, a marginal `+2.5 sigma` on `w_a`; the one-parameter `f_0` family is **misaligned** with the
  DESI `w_0`-`w_a` degeneracy (joint Mahalanobis, ρ-scanned, **~3-4 sigma**, closest approach ~3.47 sigma).
  This is a **genuine, near-falsifying observational handle** -- a way GU can be *excluded*, not a confirmation.

Honest scope: this is a **sign-only** consistency result -- the sector is LCDM-amplitude-degenerate (`f_0` and
the `B_i` are tuned fits, not GU predictions), the equation-of-state machinery is reconstruction-grade, its
divergence-free property rests on the unproven Assumption 3, and **the live canon verdict on this sector is
OPEN**. The earlier hope that the gravity intersection would pin `f_0` and close dark energy's weakest point
does **not** robustly hold: with the corrected Willmore residual (`M^2/r^6`, not `M^2/r^4`) the order match
breaks, so `f_0` stays free and the DESI tension stands on its own with no gravitational lifeline
(`tests/wave1/H3_desi_verified_and_intersection.py`).

### 2.5 Gravity -- CONDITIONAL THEOREM at tree level (conditional on one soldering postulate + `mu_DW`); loop-level OPEN
*Governed by the Wave 1-8 block above; this supersedes the earlier "one undetermined Willmore-EL
scalar / Branch-2A" framing.* The gravitational sector is the section-shape equation. The 8-wave arc
establishes, at the honest grades tabulated above, the following **conditional** chain (each link is a
reproducible `tests/waveN/` check, exit 0):

1. **The exact vacua clear in the Bach branch.** Exact Schwarzschild is Bach-flat at all orders in `M` (its
   Weyl tensor is nonzero, so this is a genuine strong-field cancellation, not triviality) and Kerr is
   Ricci-flat hence Bach-flat; GU's H-class pure-gravity spin-2 residual **is** the Bach operator
   (`box^2 h = -4 Bach^(1)`) (H1). This clears the strong-field wall that had blocked the Willmore-only
   branch -- *conditional* on GU's functional being the conformally-invariant combination on all sectors.
2. **The functional is forced II-class.** By the Gauss identity `|II|^2 = |H|^2 - R^X`, and because in 4D
   `int R^X` is *dynamical* (not topological), the full-distortion `|II|^2` functional carries a genuine
   Einstein-Hilbert term -> Stelle `R^X + Weyl^2`, lifting the degenerate pure-Bach `box^2` to `box(box+m^2)`
   (a healthy massless graviton + a *distinct* massive ghost) (H15). That GU's action norms the **full**
   `II_s` (not its trace) is argued from its Yang-Mills / double-copy structure, and the Clifford-odd shiab
   "trace-before-norm" counter is refuted for the bosonic leg (H18) -- at **structural** grade, resting on
   two reconstruction/transcript premises (P1, P2), both leaning II-class.
3. **P1 is proven.** `s*(theta) = II_s` is the Gauss formula for the graph section into `(Met(X), gimmel)`,
   proven **off-shell**, full-tensor, in the canonical gauge; the literal-vs-horizontal convention is a
   **non-trace** additive shift, so the `|II|^2`-vs-`|H|^2` fork does not re-open (H21).
4. **The ghost sign is healthy -- the antigravity KILL is retired.** The Gauss `-R^X` gives a healthy
   massless graviton (attractive, positive Newton constant) with `m^2 = +1/2 > 0` in the flat ambient (H16);
   the *leading* curved-ambient `R^Y` correction is a computed `Lambda` (0-derivative, branch-neutral) and
   **cannot** flip the sign (H24); and the residual sign coefficient `C_RY` is **computed POSITIVE** by two
   independent methods (`m^2_eff = 1/2 + C_RY > 1/2 > 0`), so the KILL is excluded **by sign**, not merely by
   magnitude (H25, overturning H24's provisional `C_RY < 0`).
5. **The ghost clears in the Krein sense.** The spin-lift `so(9,5) -> End_H(S)` is the unique canonical lift
   (exact homomorphism); it lands in the **non-compact** real form `Sp(32,32;H)` (sharpening canon's "Sp(64)");
   the Krein ghost-parity `P = K` implements the Cartan involution and `[P,S] = 0` holds for the natural
   covariant dynamics (`M_D` Krein-self-adjoint) -- the Bateman-Turok tree-level positivity condition (H23 A/B/C).

**The one condition.** All of the above is **clear-MODULO-soldering**: it holds given the single postulate
`A = spin-lift(grad^gimmel)` (equivalently `pi = spin-lift(grad^gimmel)`), which makes `theta` *be* the
geometric second fundamental form. That identification is a **codimension-8165 constraint per point** that
GU's kinematics does **not** impose and that `S = |theta|^2` does **not** force (its Euler-Lagrange equation
is `d_A * theta = source`, not `theta = 0`; the vacuum is not the soldered configuration) (H23 D). The
postulate is *natural* -- the reference is the unique metric-compatible torsion-free lift -- but underived;
it is the **same class** as canon Assumption 3 / the unbuilt source action. The dimensionful scale `mu_DW`
(which sets the ghost mass `m_ghost^2 = m^2_eff * mu_DW^2`; Planckian and decoupled for the natural
`mu_DW ~ M_Pl`, but that value is smuggled, not derived) is likewise the source action's overall
normalization (H24). And **loop-level unitarity is OPEN** -- Bateman-Turok prove tree-level positivity only,
and their spin-2 ghost decouples; this is the generic-Stelle-Mannheim frontier, which GU's structure resolves
no better than the generic theory (H16 BAR 1, primary-source-fenced). So the branch lands in the *contested*
Stelle-Mannheim corner -- but on its *attractive* side, with the wrong-sign kill retired.

**Net:** gravity is **not** unconditionally cleared and **not** falsified; it is a **tree-level conditional
theorem** whose single condition (soldering + `mu_DW`) is the same unbuilt source action that gates every
other residual. The generation count does **not** live here -- it lives in the fermion sector's `C2` wall
(Sec 3), which this arc leaves untouched and which is strictly harder than the gravity soldering.

## 3. The generation count as one instance (subsumes "located, not forced")

The fermion generation count is not forced by the framework's structure; it is *located* -- a rigid,
finite 2-bit residual of the source action's field-space declaration. Two grades, kept separate: it is
**provably a rigid, finite residual** by the primary-partition no-go (`Hom(Z/3,Z)=0`; elementary/folklore
CRT arithmetic, genuinely computed, `tests/family-puzzle/primary_partition_lemma.py`), and it is
**located** in the odd-primary boundary summand at **principle grade** under the no-net-chirality-needs-a-
boundary principle (Nielsen-Ninomiya / Callan-Harvey / Kaplan; not proven for the true RS/`Y14`-bundle
index). The 3-primary localization of the count is **prior art** (Garcia-Etxebarria-Montero arXiv:1808.00009;
Wan-Wang-Yau arXiv:2605.26202); our delta is the 2-primary-blindness *no-go census* plus the *boundary*
conjunction. The generation count actually **lives in the fermion sector's `C2` wall** (the boundary
symbol-norm `C2` that is *not* an index, per the source-action buildbench), which the Wave 1-8 gravity arc
leaves untouched (H23) -- it is the same *kind* of object as the gauge-vacuum selection (Sec. 2.1-2.2) and
the gravity soldering (Sec. 2.5): a selection the dynamics makes, not a contradiction, and strictly harder
than the gravity soldering.

## 4. The central result: everything reduces to one object

Collecting the open freedom across all five sectors:
- **gauge-vacuum / sub-block selection** (which theta-stable block / breaking vacuum) -- source-action-gated;
- **the generation count / fermion `C2` residual** -- a rigid finite residual of the source-action field-space
  declaration, living in the fermion `C2` wall;
- **the gravity soldering postulate** `A = spin-lift(grad^gimmel)` **plus the scale `mu_DW`** -- the one
  bosonic constraint (codim-8165 per point) that GU's dynamics does not supply, together with the overall
  normalization; both are properties of the branch-fixed source action (Sec 2.5, H23/H24).

These are **jointly fixed by one object**: the source action (its field-space declaration *together with*
its fixed coefficients). The framework therefore **closes up to a single, precisely-characterized,
currently-unwritten object**, and no sector falsifies it. This is the
generalization of "located, not forced" from the generation count to the *entire* residual freedom of the
framework. **Honesty brake (the E-audit rule, kept explicit):** "reduced to one X" is *not itself* progress
-- the "one object" is genuinely a **conjunction** of distinct data (the soldering `!=` `mu_DW` `!=` the
fermion `C2`/2-bit count `!=` the gauge vacuum), stably named but not literally one object; only a **forced**
construction of the source action, or a genuine **discriminator** (e.g. the DESI tension), changes the
epistemic state.

## Open premises and honest negatives (every conditional in plain sight)

The conditional theorem and the four clears rest on the following premises and carry the following live
negatives. None is buried; each is load-bearing for the honesty of the result.

**Open premises (the conditions):**
1. **The soldering postulate** `A = spin-lift(grad^gimmel)` -- NOT forced by GU's kinematics or by
   `S = |theta|^2` (a codim-8165 constraint per point). Natural but underived (H23 D). *The* gravity condition.
2. **`mu_DW`** -- the dimensionful overall scale is NOT derived; only dimensionless ratios are geometric.
   `mu_DW ~ M_Pl` (Planckian, decoupled ghost) is natural but smuggled (H24/H25 BAR 2).
3. **The `|II|^2`-vs-`|H|^2` functional choice (OQ2-A)** -- II-class is *forced* only at **structural /
   transcript** grade via premise P2 (action = YM full `|theta|^2`); a Willmore-type `|H|^2` variant would
   change the branch (H18). P1 (`s*theta = II_s`) is proven off-shell (H21), but conditional on premise 1.
4. **Loop-level unitarity** -- only **tree level** is shown. Bateman-Turok prove tree-level positivity, and
   their spin-2 ghost decouples; the full-Stelle loop ghost is the generic-Stelle-Mannheim open frontier,
   which GU resolves no better than the generic theory (H16 BAR 1).
5. **The generation count is located, NOT forced** -- located in the odd-primary boundary summand at
   **principle** grade (Nielsen-Ninomiya / Callan-Harvey / Kaplan), not proven for the true RS/`Y14` index;
   the count itself is a rigid 2-bit residual, not derived (Sec 3).
6. **Heterodox status** -- GU is a heterodox theory most physicists do not accept. This document is a
   reconstruction/audit ("taken seriously and computed carefully, here is what holds and at what grade"),
   not an endorsement; the SM/QM inputs use standard rep theory / generalized-Born-rule work, not novel derivations.

**Honest negatives (kept IN -- they are load-bearing):**
- **DESI ~3-4 sigma.** Dark energy under-evolves `|w_a|` (~0.27 vs ~0.86) and sits ~3-4 sigma from DESI DR2
  (arXiv:2503.14738) -- a genuine near-falsifying handle (Sec 2.4). The gravity intersection does NOT rescue
  `f_0` (the corrected `M^2/r^6` residual breaks the order match, H3).
- **The soldering is unforced.** No GU-internal principle was found (after adversarially looking) that forces
  `theta` onto the second-fundamental-form locus; naming it as an assumption is the honest outcome (H23).
- **The contested Stelle-Mannheim corner.** The cleared branch inherits (does not resolve) that corner's
  unresolved loop-unitarity dispute; it lands on the *attractive* side, with the wrong-sign kill retired, but
  the corner is contested, not clean (H16).
- **`Sp(32,32;H)` is non-compact.** The gauge group the connection actually carries is the non-compact real
  form; the Krein/indefinite metric exists only because the internal group is non-compact (H23 B) -- stated,
  not hidden.
- **Grades are tree-level and existence/consistency**, never "proven physics." The `[P,S]=0` that clears the
  ghost is **sign-blind**: it buys positivity, it does NOT select the generation count (H23 C) -- no chiral
  selection was manufactured.

## 5. Geometry-agnostic core (why a skeptic need not accept GU)

The reduction-to-one-residual is not a GU claim. Any geometry that accommodates the five sectors faces the
same structure: its dynamics (source action) is the single object that selects the gauge vacuum, supplies the
soldering that fixes the strong-field gravitational sector, and declares the generation-sector field space; and the generation
count is a boundary quantity in the odd-primary summand *regardless of the geometry* (Sec. 3, GU-independent).
So the load-bearing statement -- *a geometric unification's entire residual freedom localizes in one
source-action object, of which the generation count is a boundary/odd-primary instance* -- holds whether or
not GU is the correct geometry. GU is the concrete carrier that let us compute it.

## 6. What would close it (the single construction problem)

One object decides everything remaining: a **forced/derived** source action written with fixed coefficients.
It simultaneously (a) supplies (or falsifies) the gravity **soldering** `A = spin-lift(grad^gimmel)` and fixes
`mu_DW` -- turning the tree-level conditional theorem into an unconditional CLEAR (a 5/5 complete picture) or a
clean strong-field DISPROOF (telling us exactly where a nearby geometry must differ) -- and (b) pins the
fermion `C2`/generation count and the gauge vacuum. The precise next object is the **soldering carrier**: a
GU-internal dynamics or constraint that forces `pi` onto `spin-lift(grad^gimmel)` (candidate: a Palatini-type
first-order variation of `|theta|^2` driving `pi` to the metric-compatible lift on-shell, which must NOT
reduce to the acausal-trapped `theta = 0`), or a falsification of it. A *free* build p-hacks the residual
(established); the honest form is a forced construction, for which no armchair mechanism was found (a complete
forcing rubric + an out-of-rubric hunt came up empty). The residual is thus real, finite, and not resolvable
without building the object. **Loop-level `[P,S]=0`** is the separate, harder, generic-Stelle-shared frontier,
unchanged and not resolvable without the action.

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

1. **DONE:** the sector clears are reproducible in-repo tests (`tests/one-residual/`, all exit 0) --
   SM stabilizer, mirror anomaly-traces, QM Krein repair, dark-energy sign, forces max-compact; grades
   corrected to honest per the Hardening pass ledger above.
1b. **DONE (Wave 1-8):** the gravity leg is upgraded to a tree-level conditional theorem with the full
   `tests/wave1..wave8/` arc (all exit 0), superseding the older single-scalar / Branch-2A framing (Wave 1-8
   block + Sec 2.5). The DESI DR2 numbers are verified against the primary source arXiv:2503.14738 (H3).
2. **DONE (this pass):** per-sector grading + reconstruction map + prior-art distinctions + the Wave 1-8
   conditional-theorem framing + the explicit open-premises/negatives section folded into the body
   (Secs 1, 2.1, 2.4, 2.5, 3, 4, "Open premises", 7).
3. **SM-leg gaps CLOSED (2026-07-11 hardening):** (a) the mirror `16bar` content is now computed as the
   genuine charge-conjugate (full 5-Cartan weight system = negatives of the 16), replacing the definitional
   `n_L-n_R=16-16` tautology; (b) the `so(10)` cubic Casimir is now computed to vanish on the 16
   (`max |d| = 0`), the real umbrella for one-generation anomaly cancellation
   (`tests/one-residual/sm_so10_cubic_casimir_and_mirror.py`, exit 0).
4. **The load-bearing open object:** supply (or falsify) the gravity **soldering** `A = spin-lift(grad^gimmel)`
   and fix `mu_DW` via the branch-fixed source action -> upgrades the tree-level conditional theorem to an
   unconditional 5/5 or a clean gravity disproof (either strengthens the paper). Same object pins the fermion
   `C2`/count. Loop-level `[P,S]=0` is the separate, harder frontier.
5. Figures: the sector scoreboard; the Wave 1-8 gravity ledger; the maximal-compact = SM computation; the
   primary-partition table.

Grade: structural result at honest grade; four sectors existence/consistency-cleared (reproducible), gravity
a **tree-level conditional theorem** (clear-modulo-soldering + `mu_DW`; loop-level open), the
reduction-to-one-object is the contribution. All quantitative claims tie to reproducible tests
(`tests/one-residual/`, `tests/wave1..wave8/`, `tests/legs/`, `tests/family-puzzle/`, all exit 0). Target:
hep-th / math-ph. External publication Joe-gated (NOT in scope here: no arXiv, no submission). Supersedes/subsumes
`papers/candidates/generation-number-boundary-odd-primary/` and the located-not-forced draft as legs.
