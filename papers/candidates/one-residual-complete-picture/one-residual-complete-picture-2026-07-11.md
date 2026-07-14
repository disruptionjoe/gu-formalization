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
3. **Dark energy: do NOT head "CLEARED" -- the live canon verdict is OPEN.** *[This correction is itself
   SUPERSEDED in the falsifying direction by the 2026-07-13 block below: the sector is now falsified as the
   DESI CPL summary and excluded as a CMB-consistently-calibrated distance model; the sign-only consistency
   row above is a historical test grade, not the current verdict.]* State: consistency, SIGN-only,
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
**~3-4 sigma** from DESI *[historical phrasing; the 2026-07-13 block below hardens this to falsified-as-CPL
plus excluded-as-CMB-calibrated-distance-model]*. This **subsumes** the located-not-forced generation count
as one facet of the single residual.

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
| H27 | the soldering is **PROVABLY a genuine postulate**: a Palatini variation of `S` does NOT force the connection onto the spin-lift (Palatini forces IFF linear-in-curvature; GU is the *square* -> algebraic route = acausal `theta=0` trap + circular, kinetic route = YM moduli family). Positive control (linear-Palatini toy) correctly flags FORCED -> the no-go detects real forcing | **no-go** (exact ranks + positive control; HIGH) -> the conditional theorem is the PROVEN final state, gravity cannot be made unconditional within the built structure | `tests/wave10/H27_soldering_palatini.py` |

**Net movement of the gravity leg:** OPEN/reduced -> **clear-MODULO-soldering at tree level.** The functional
is forced II-class (H18), P1 is proven (H21), the induced-Einstein sign survives the curved ambient by an
explicitly computed positive `C_RY` (H25, overturning the earlier hand-waved worry), and the Krein ghost
parity clears it (H23 C). What remains is exactly **one bosonic soldering postulate**
`pi = spin-lift(grad^gimmel)` (H23 D) **plus** the dimensionful `mu_DW` (H24/H25) -- both the SAME unbuilt
object as the source action. The soldering is *natural* (the reference is the unique metric-compatible
torsion-free lift) but **GU's dynamics does not supply it**, and `S = |theta|^2` does not force it (the vacuum
is not `theta = 0`). **H27 (Wave 10) upgrades this from "not yet forced" to PROVABLY a genuine postulate:** a
first-order (Palatini) variation of `S` does *not* drive the connection onto the spin-lift on-shell -- the
Palatini theorem forces a connection *only* for actions linear in its curvature, and GU's action is the
*square* of a first-order potential (Weinstein's "first-order then its square"), which breaks the forcing both
ways (algebraic -> the acausal `theta=0` trap, which is also circular; kinetic -> a YM-type moduli family).
A positive control (a genuine linear-Palatini toy the same machinery correctly flags FORCED) certifies the
no-go detects real forcing rather than merely preserving GU (`tests/wave10/H27_soldering_palatini.py`, exit 0).
So the conditional theorem is the **proven final state within the currently built structure**, not a gap
awaiting closure. This is **strictly softer** than, and provably distinct from, the fermion sector's `C2`
wall where the generation count actually lives.

## 2026-07-13 three-wave consolidation (W119-W126, H46C, H52, Track 2, Yukawa, requirements spec) -- this block GOVERNS Secs 2.4, 4, 6 and the Open premises / honest negatives

Three adversarial waves ran on 2026-07-13 (each result a 5-persona inline team with a deterministic
test; every test re-run for this consolidation, W127, exit codes recorded below). Two hard movements
and one sharpening govern everything downstream of this block:

1. **Dark energy is falsification-hardened.** H46C (wave 46) executed the theta_star re-solve of GU's
   own CMB-calibrated amplitude: GU's own calibration OVERSHOOTS the BAO-preferred amplitude by
   `+5.7 sigma_A` (`dAIC = +35.78` at GU's own calibration; `+16.03` with `omega_m h^2` profiled for
   both models), and the freed-amplitude shape win (`dAIC = -3.17`) has NO CMB-consistent realization.
   With per-`f_0` CMB calibration the BAO-preferred `f_0` is the LCDM limit `f_0 -> 0` (bound
   `f_0 < ~0.027-0.03` vs the CPL-needed `0.125`). The prior softening "viable as a distance model"
   is **SUPERSEDED** wherever it appears below: GU's dark energy is falsified as the DESI CPL summary
   AND excluded as a CMB-consistently-calibrated distance model for `f_0 >= ~0.03`; it survives only
   as a subdominant component in the LCDM limit. (Canon: CORRECTION DARK-ENERGY-05, already cascaded;
   verdict on the canon EOS file stays OPEN at that component-only scope.)
2. **The AF branch carries a NATIVE, tree-unliftable, positive-norm tachyonic scalaron.** W122 proved
   the spin-0 conformal-mode sign is physical, not gauge (exact auxiliary-field/Legendre route; a
   gauge parameter provably has nowhere to enter; `m_0^2 = gamma/(6c) < 0` on the AF trajectory, `c` the
   direct `R^2` coefficient, reciprocal to the agravity `f_0^2` and negative with it; the mode is
   positive-norm, so it is a tachyon, not a ghost, and there is nothing for keep-and-grade to grade).
   W123 closed the porting-artifact escape (convention chain pinned end to end by an exact
   cross-lineage identity; no admissible field content flips the sign; and a one-line monotonicity
   theorem FORBIDS positive-`f_0^2` AF trajectories outright -- `f_0^2 > 0` Landau-poles in bounded
   `t`, so `f_0^2 < 0` at every finite scale on every AF trajectory). W126 closed tree-level vacuum
   lifting EXACTLY: the induced `|II|^2` potential sector terminates at `R^2` identically
   (`c_3 = c_4 = ... = 0`, all orders in `phi`, two routes; MSS-slice `F(R) = 2 + R/3 - R^2/9`), the
   unique extremum is the tachyonic top with a runaway to the `f' = 0` wall, and the loop-`R^3`
   rescue is ghost-infested or out-of-validity on both W46 branches. **This is not a conditional
   antecedent: it is a property of the AF branch of the declared action.** The two thin escapes are
   named in the honest-negatives section: the AF-vs-AS fork (the Reuter fixed point W119 catalogued)
   and a non-perturbative mechanism beyond the computed truncations.
3. **The residual object is sharper.** The source-action requirements spec consolidates every leg's
   demands into 27 rows (8 FORCED / 9 DECLARATION / 10 FIT) with NO outright contradiction among the
   FORCED items (five named tensions carried openly). W125 then ran the first build attempt against
   that spec: a five-term `g = 1` ker-Gamma candidate at symbol level, with the SA-C4 kill-test BUILT
   for the first time and TEST-BUILT-PASSING on the candidate, the shiab revision `t* = -1/6` exact,
   and payoff NONE (0 of 10 FITs emitted source-first, machine-checked reasons). The single object
   blocking the full build, the remaining loop packet, and SA-G9 alike is **the covariant operator on
   `Y14`** (the flat symbol model does not carry it).

**Notation note (W123's disambiguation, applied throughout this paper).** `f_0^2` is a SIGNED coupling
despite the square notation. Two repo conventions exist: the UV-arc/W119 usage (`f_0^2` = the agravity
coupling, `R^2` coefficient `1/(6 f_0^2)`) and the W79/W122 usage (`f_0^2` = the direct `R^2`
coefficient). W123 verified the two are reciprocal and hence SIGN-consistent (magnitude formulas
differ). In this paper `f_0^2` always means the agravity coupling, the UV-arc convention; every sign
claim is convention-robust.

**Consolidation verification ledger** (W127 re-runs, 2026-07-14; all deterministic):

| Result | Claim (honest grade) | Test | Re-run |
|---|---|---|---|
| W119 | AF trajectory + negative fixed-ratio + Krein spin-2 grading SURVIVE a minimal FRG truncation (Litim + exponential + shape-swept regulators); the one-loop UNIQUENESS clause breaks -- the Reuter FP appears, already catalogued (W83/W88), no new ambiguity; ghost-mass fork confined to the UV endpoint (DERIVED-on-PORTED, truncation-dependence explicit) | `tests/W119_h59_frg_krein_negative_ratio.py` (17/17) | exit 0 |
| W120/W121 | CLOP order-of-limits ambiguity EVADED at fixed order (it attaches to the removal prescription's deformation step, which keep-and-grade does not perform); no-local-positive-metric theorem HARDENED (4 of 6 hypotheses necessary, one provably tight; x-dependent finite-order operators excluded) | `tests/W120_path2_target2_keepgrade_vs_clop.py` (16/16), `tests/W121_path2_target3_hypothesis_hardening.py` (11/11) | exit 0, exit 0 |
| W122 | the spin-0 scalaron is PHYSICAL, positive-norm, tachyonic on the AF trajectory; gauge channel exhausted (exact Legendre route, gauge parameter has nowhere to enter; exact within the 4th-order truncation) | `tests/W122_spin0_scalaron_auxfield.py` (27 checks) | exit 0 |
| W123 | tachyon NATIVE-ROBUST: convention chain pinned (exact cross-lineage identity); fixed-ratio sign robust across the whole admissible band; positive-`f_0^2` AF trajectories FORBIDDEN (monotonicity theorem + Landau bound) | `tests/W123_native_r2_sign_convention_audit.py` (34/34) | exit 0 |
| W124 | at two loops the graded prescription is UNAMBIGUOUS at fixed order (no ambiguity of its own; anomalous-threshold hunt empty); the CLOP band's endpoints are exactly the two families' answers (`0` and `+1` x `Im S_gg`); even-cut inter-family disagreement (+1 vs 0) stands; the odd-cut leak persists at `s > (2m+M)^2` (numerical-controlled; spin-2 tensor numerators OPEN) | `tests/W124_stageA_sunset_graded_vs_LW_CLOP.py` (16/16), `tests/W124_stageB_overlap_kite_cuts.py` (11/11) | exit 0, exit 0 |
| W125 | first source-action build vs the 27-row spec: PARTIAL; SA-C4 kill-test built and TEST-BUILT-PASSES at symbol level; `t* = -1/6` exact; payoff NONE; blocking object = the covariant operator on `Y14` | `tests/W125_built_candidate_assembly.py` (14/14), `tests/W125_sac4_subprincipal_built.py` (9/9) | exit 0, exit 0 |
| W126 | beyond-4th-order vacuum lifting CLOSED at tree level EXACTLY: `|II|^2` conformal potential sector terminates at `R^2` identically, all orders; `F(R) = 2 + R/3 - R^2/9`; runaway stands; loop-`R^3` rescue ghost-infested or out-of-validity | `tests/W126_beyond4th_conformal_iisq.py` (32 checks) | exit 0 |
| H46B (wave 45) | DESI DR2 + Planck digit gate CLEARED against primary sources (arXiv:2503.14738 Table 4 + official likelihood files; arXiv:1807.06209) | `tests/wave45/H46B_referee_grade_desi_verification.py` (33/33) | exit 0 |
| H46C (wave 46) | DE FALSIFICATION-HARDENED: excluded as a CMB-consistently-calibrated distance model too (`dAIC = +35.78`; `f_0 < ~0.027` 3-sigma-equivalent vs CPL-needed `0.125`); the freed-amplitude rescue DISSOLVES | `tests/wave46/H46C_theta_star_cmb_calibration.py` (20/20) | exit 0 |
| H52 (wave 32) | the `alpha = 1/3` sub-mm exclusion boundary is now CITED, not argued: `lambda_max = 47.6 um` (Lee 2020, via the published `n = 1` bound); the H36 window `[60.0, 73.6] um` EXCLUDED-CITED, margin 1.9-9.8x; resolved `mu_DW` floor `[3.4, 4.7] meV` envelope (supersedes H50's 2007-data floor 3.0-3.6 meV) | `tests/wave32/H52_alpha13_boundary_cited.py` (18/18) | exit 0 |
| Track 2 | the conditional theory GU-given-S emits its numbers (never asserting S): `alpha = 1/3` fixed; inside the allowed `mu_DW` window GU-given-S predicts EXACTLY GR at LIGO (massless pole exactly massless; massive companion 9+ orders above the excitable band); `mu_DW >= ~3.4-4.8 meV`, no experimental upper edge | `tests/track2/T2A_graviton_sector_numbers.py` (8/8), `T2B_dark_energy_curves.py` (4/4) | exit 0, exit 0 |
| Yukawa (H28) | channel table COMPLETE and rigid (one channel per `Lambda^k`/chirality block); non-form Higgs carriers FORBIDDEN (dim Hom = 0, exact); hierarchy SILENT (three surviving couplings free); mod-3 Froggatt-Nielsen charges provably STERILE (all 27 assignments); the `1+2` block texture is pattern-compatible only, not derived | `tests/yukawa-scoping/yukawa_trilinear_channels.py` (20/20) | recorded run cited (2026-07-13, exit 0; >10-min suite, not re-run) |
| Requirements spec (H41) | 27 rows, 8 FORCED / 9 DECLARATION / 10 FIT; zero outright contradictions among FORCED; five named tensions | `tests/spec-consistency/source_action_requirements_consistency.py` (33/33) | exit 0 |

The H51 DeWitt-coefficient slow suite is likewise cited at its recorded run (2026-07-12, exit 0), not
re-run.

## Abstract

We report a structural result about a candidate geometric-unification framework and its relation to the
five sectors it must account for -- the Standard Model gauge group and content, the forces, quantum
(indefinite-metric) structure, dark energy, and gravity. Under an adversarial program that granted a
working source action and then tried to *falsify* each sector, **no sector falsifies the framework's
structure, but one sector's distinctive observational signal is now excluded in every tested register**;
**three of five are cleared at existence/consistency grade**: (i) the Standard Model gauge algebra is
realized *exactly* as the maximal compact of the ambient `su(3,2)` -- `su(3)+su(2)+u(1)`, a single `u(1)`,
no extra photon (reproducible; `su(3,2)` is a non-native sub-block, so *which* sub-block the dynamics
selects is itself the residual), and the forced mirror matter is anomaly-free (four SM traces vanish,
computed) and -- by standard SO(10) representation theory -- vectorlike and mass-liftable; (ii) the same
maximal-compact selection *admits* exactly the SM forces (a breaking to exactly them exists), avoiding the
"28-photon" adjoint-breaking catastrophe; (iii) quantum structure is unitary-repairable on the indefinite
(Krein) inner product (a positive-definite physical sector and a Krein-unitary generator exist, on a
faithful model); (iv) dark energy is the framework's hard negative: after the full adversarial arc (CPL projection,
raw BAO likelihood, and finally GU's own theta_star CMB calibration, all against primary sources) the
theta sector is **falsified as the DESI CPL summary AND excluded as a CMB-consistently-calibrated
distance model** for `f_0 >= ~0.03` (`dAIC = +35.8` at GU's own calibration); it survives only as a
subdominant component in the LCDM limit, so the sector no longer supplies evidence *for* the framework
in any tested register (Sec. 2.4 and the honest-negatives ledger).
The fifth sector, gravity, is upgraded by an 8-wave arc (see the Wave 1-8 block above) to a **conditional
theorem**: at *tree level* it Stelle-clears (induced Einstein-Hilbert `R^X` + `Weyl^2` + a DeWitt `Lambda`;
the `|II|^2` functional forced the II-class; the massive-ghost sign confirmed healthy by two independent
methods; the Krein ghost-parity clears it in the Bateman-Turok sense) -- **conditional on one
natural-but-unforced soldering postulate** (`A = spin-lift(grad^gimmel)`) **plus the dimensionful scale**
`mu_DW`; loop-level unitarity remains open. On the ultraviolet side the 2026-07-13 waves cut both ways:
the renormalizable-plus-asymptotically-free picture *survives* its first FRG truncation (W119), and the
graded prescription is unambiguous at fixed order through two loops (W124); but the same AF branch is now
shown to carry a **native, positive-norm, tree-unliftable tachyonic scalaron** (W122/W123/W126) -- a
property of the declared action's AF branch, not a conditional antecedent, with exactly two thin escapes
(the AF-vs-AS fork; a non-perturbative mechanism). The central finding is that **the cleared sectors'
remaining freedom, the gravity soldering-postulate-plus-scale, the fermion `C2`/generation residual, and the
gauge vacuum are jointly fixed by one object**: the source action (its field-space declaration together with
its fixed coefficients), a rigid, finite residual -- now specified by a 27-row requirements spec (8 FORCED /
9 DECLARATION / 10 FIT, zero contradictions) whose first build attempt names the single blocking object, the
covariant operator on `Y14`. The generation count is *located, not forced* -- a special case.
The framework thus **closes up to one precisely-characterized object**, and we exhibit that object. We do
not claim the framework is proven; we claim its structure is not falsified on any sector -- while stating
plainly that its dark-energy signal is excluded in every register tested so far and that its AF branch
carries a genuine tachyonic instability -- and that its entire residual freedom is localized in one place.

## 1. What is and is not claimed

- **Claimed:** no sector falsifies the framework's *structure*; three sectors (SM content, forces, quantum
  structure) are consistent and the structures they require provably *exist*; gravity is a **tree-level
  conditional theorem** (Stelle-clears conditional on one soldering postulate + `mu_DW`); dark energy is the
  honest hard negative -- falsified as the DESI CPL summary and excluded as a CMB-consistently-calibrated
  distance model, surviving only as a subdominant component (2026-07-13 block above); the AF branch of the
  declared action carries a native, tree-unliftable tachyonic scalaron (a computed property, stated, not
  hidden); the total remaining freedom across all sectors is a single object (the source action's field-space
  declaration together with its fixed coefficients), which we characterize (rigid, finite, a bounded
  discrete/parametric residual, now specified by the 27-row requirements spec).
- **Not claimed:** that the framework *derives* the Standard Model / forces / dark energy (it accommodates
  them and the required structures exist -- *which* the dynamics selects is the residual); that gravity is
  *unconditionally* closed (it is a tree-level conditional theorem, conditional on the soldering postulate
  `A = spin-lift(grad^gimmel)` + `mu_DW`; loop-level unitarity is open); that dark energy is confirmed or even
  viable in any register tested so far (it is falsified as the CPL summary and excluded as a CMB-calibrated
  distance model; the historical "sign-consistent but ~3-4 sigma" phrasing is SUPERSEDED by the 2026-07-13
  block); that three generations are *forced* (they are located, not
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

### 2.4 Dark energy -- FALSIFIED as the DESI CPL summary AND EXCLUDED as a CMB-consistently-calibrated distance model (survives only as a subdominant component; canon verdict OPEN at that scope)

**Current verdict (2026-07-13 block above, GOVERNS this section; CORRECTION DARK-ENERGY-05 cascaded to
canon).** The full adversarial chain now reads: the `(w_0, w_a)` CPL projection is falsified (H43/H44);
the raw-BAO "viable as a distance model" reading is SUPERSEDED -- H46C's theta_star re-solve shows GU's
own CMB-calibrated amplitude overshoots the BAO preference by `+5.7 sigma_A` (`dAIC = +35.78`; profiled
`+16.03`), the freed-amplitude shape win has no CMB-consistent realization, and per-`f_0` calibration
prefers the LCDM limit (`f_0 < ~0.027-0.03` vs the CPL-needed `0.125`). What survives is a theta
component too small to be GU's distinctive signal. The paragraphs below are retained as the honest
historical chain (each stage was real when computed); read them through this verdict.

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
(`tests/wave1/H3_desi_verified_and_intersection.py`). A second rescue candidate -- combining the evolving
`theta`-sector with the *constant* `O(M^0)` DeWitt-`Lambda` (Sec. 2.4/B-thread) as an independent two-fluid
dark energy -- was tested and **also fails**: a `w=-1` constant supplies zero evolution while DESI wants more,
so both marginals move *away* from DESI (`w_a` flattens); the only nominal joint gain is fragile
degeneracy-sliding that vanishes as the assumed `w_0`-`w_a` correlation goes to zero, and the best mix is
still a failing `~3.6 sigma` fit (`tests/wave11/H_DE_combined_dewitt_theta_desi.py`). A third move -- the
*fair* comparison the (w0,wa)-plane headline invites: the **actual non-CPL `theta` w(z)** (Klein-Gordon field)
compared on **distances** (what BAO measures) with **`Omega_m` floating** -- was also run and **confirms the
tension is not a projection artifact** (`tests/wave11/H_DE_actual_wz_floating_bg.py`): the actual `w(z)` is
nearly CPL over `z<=2` (so the shallow evolution is intrinsic, not a lossy fit), and the `Omega_m` float that
would reach distance-consistency requires `Omega_m ~ 0.275`, which is `6.4 sigma` from the CMB-pinned value --
excluded by the very DESI+CMB combination that reports the tension; at the CMB `Omega_m` a real `~2.6%`
distance offset remains. So the `~3-4 sigma` DESI tension is a **robust live negative**: two independent
rescue routes (DeWitt-`Lambda` combination; fair distance comparison) were tested and neither holds. The
**prediction-vs-fit** question is then settled (`tests/wave11/H_DE_prediction_vs_fit.py`): scanning the
`theta` amplitude `f_0` and field mass `M^2` shows the two-component **shape CAN fit DESI** (best distance
residual `0.99%`, inside BAO precision, at `(f_0~2, M^2~1)`) -- so it is **not** a hard structural failure --
but the model *default* `(f_0=0.125, M^2=8)` is itself in tension (`2.63%`) and the good-fit region is far
from it. Since `f_0` is a **free input** (nothing built forces it), the DESI tension is **soft /
amplitude-gated**, not a present falsification: GU's dark-energy sector is *under-determined* pending the
built `theta` dynamics that would fix `f_0`, and it becomes a genuine hard test only if the source action
forces `f_0` near the in-tension default. So DESI, like the gravity soldering (Sec. 2.5), routes to the
**same single unbuilt object** -- the source action -- as a conditional/soft negative, not a hard kill. (This
is not a rescue: `~3-4 sigma` at the default parameters is real; `soft` means the model is not yet committed
enough to be falsified, not that it fits.) **[SUPERSEDED (H46C, 2026-07-13): the "soft / amplitude-gated,
not a present falsification" register above is historical. The amplitude freedom it leaned on has no
CMB-consistent realization; the sector is now falsified as a CPL fit AND excluded as a CMB-calibrated
distance model for `f_0 >= ~0.03`. See the section header and the 2026-07-13 block.]**

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
symbol-norm `C2` that is *not* an index, per the source-action buildbench) -- it is the same *kind* of object
as the gauge-vacuum selection (Sec. 2.1-2.2) and the gravity soldering (Sec. 2.5): a selection the dynamics
makes, not a contradiction.

**Wave 12-13 upgrade -- located-not-forced is now PROVABLE within the built structure (the fermion analog of
the gravity no-go H27).** H29 (`tests/wave12/H29_fermion_c2_wall.py`) characterized `C2` exactly as the
gamma-trace of the Velo-Zwanziger constraint-leakage -- a particle-hole-odd, Kramers, Krein-self-adjoint
object of symmetry class **CII**, whose index/`eta` is **theorem-forced to zero** -- so the count is
theorem-*forbidden* from the fermion index. H37 (`tests/wave13/H37_count_nogo.py`) then proved the endgame: to
*force* an odd count you need a grading-breaking boundary-Dirac with `eta != 0`, and on the built
`(9,5)`+positive-Hessian+no-import structure that is **mutually exclusive** (positivity forces the grading;
the only symmetry escape, the antilinear chiralizer, has tangent-frame charge 0 = the forbidden import) -- a
genuine **NO-GO**, with a **positive control** (the same test on `(7,7)`, `J^2=+1`, DOES admit the odd rank-3,
so the method is not rigged). This places the count in a clean **seven-axis map** (`explorations/seven-axis-
count-map-L0-L7-2026-07-11.md`): the baseline (L0) and all six selector-side axes (L1-L6, the six-axis
`no-go-class-relative-map`) are LOCKED, and the only *geometry-side* escape is **L7 = the `(9,5)`-vs-`(7,7)`
signature** -- the `J^2` sign that flips the Kramers leg. Wave 14 (`tests/wave14/H19_seven_seven_branch.py`,
exit 0) then computed L7 itself and found it **live-but-non-deriving**: adopting `(7,7)` *lifts the Kramers
veto* (odd ranks 1,3,5,7 become admissible) but is **structurally incapable of supplying the count**. The
signature is a **2-primary** datum (`p-q mod 8 in Z/8`); the count 3 lives in the orthogonal **Z/3** arena of
`pi_3^s = Z/24`; `|Hom(Z/8,Z/3)| = 1` (the zero map), and the triplet carrier is neutral Krein (net index 0)
in *both* signatures. So the count does **not** collapse onto the signature -- no geometry axis reaches the
`Z/3` arena where 3 lives. Below the built `(9,5)` the count is *provably* located-not-forced (the structural
twin of the gravity conditional theorem); its real decider is **signature-independent** -- a `Z/3`-arena
chiral selector (a ghost-parity matter dynamics `[P_ghost, S]=0`), to be attacked *without* first settling
the signature. Honest limits: L0's lock is conditional on two cited canon legs (`C-01`; the
chiralizer-uniqueness capstone); `(7,7)` is a declared choice, not GU-native, and *widens* under-determination
rather than deriving three.

Wave 15 (`tests/wave15/H38_z3_chiral_selector.py`, exit 0) then computed that signature-independent selector
and narrowed the count one level further. A **derived Z/3 grading IS present** in the built `(9,5)` matter
sector -- the order-3 subgroup of the self-dual `SU(2)+` acting on the `192 = 3x64` triplet, where the `3` is
`dim Lambda^2_+(R^4)` (self-dual 2-forms, forced by the 4-base; **not** imported, **not** ambient triality,
which `Spin(14)` lacks). But ghost parity `[P, S]=0` is **2-primary and index-preserving** (the physical
chiral index is fixed at 0 for every ghost-parity-preserving dynamics), so it **permits** the vectorlike
`3 + 3` and cannot **select** a chiral 3 -- the same `|Hom(Z/2, Z/3)| = 1` blindness, one arena over. This
cleanly **splits** the count into two arena-orthogonal objects: a 2-primary *unitarity* condition `[P, S]=0`
(the same object as loop-level ghost unitarity) and a 3-primary *count* selector, which must be
**index-changing**. The count's decider is therefore the **K-class the source-action operator names on the
generation carrier** -- and that is a property of the *same* unbuilt source action the gravity soldering
reduces to. **The count and the gravity residual now sit on the one residual**, sharpening this paper's
central thesis: not two open problems, but one object with two faces.

Wave 16 (`tests/wave16/H39_sourceaction_kclass.py`, exit 0) computed that K-class two independent ways and
put the count in *exactly* gravity's shape. The four RS-carrier indices (A = -42, B = -38, bare = -40,
double = -44) reproduce from published densities and from twist additivity; only **carrier B is
index-changing** (residue 1 mod 3, order-3 `rho = (0,2,1)` nonzero), so any count-selector must be B. But
*which* carrier the source action names is a **field-space declaration** arithmetic cannot force
(gamma-trace-constrained field space names B; full field space with BRST ghost-subtraction names A) -- the
exact structural twin of the gravity soldering being a genuine postulate. So **the count is a conditional
theorem modulo one K-class declaration**, just as gravity is Stelle-clear modulo one soldering postulate.
Two further honest results: (i) the count is narrowed but *not pinned to 3* -- the derived chiral-slot ceiling
is `dim Lambda^2_+ = 3`, the realized odd rank is free in `{1, 3}` (a net index of exactly 3 has residue 0
mod 3 = carrier A's residue, so no residue certifies three); (ii) selecting the count via carrier B does
**not** break gravity's ghost clearance -- the count index is 3-primary and `[P, S]=0` is 2-primary
(`gcd(2,3)=1`), and a Krein-self-adjoint operator can carry a nonzero chiral index (the K3 Dirac operator is
self-adjoint with index -2). So the two faces are not just the same object but **coherent, non-conflicting
selections of it**. The whole framework therefore reduces to a single terminal object: the source action with
its field-space declaration **forced** from GU's structure rather than chosen. A free choice would p-hack the
carrier; only a forced build resolves the last freedom -- the honest boundary this paper draws.

Wave 17 (`tests/wave17/H40_terminal_sourceaction.py`, exit 0) attempted that forced build and mapped the
terminal state precisely. The Porrati-Rahman **causal window is a genuine structural forcing**: the built
minimal Dirac symbol leaks off the constraint surface (`C2 = ||Gamma M_D Pi_RS|| = 155.36`, the
Velo-Zwanziger acausal trigger, present as built), and the leakage is degree-1 in the covector, so it is
nonzero on GU's curved `Y14` -- a real acausality whose cure is *demanded*, not imported. Imposing causality
kills the two uncured carrier corners and collapses the residual to the two **causal** cures `{A, B}` -- one
bit genuinely removed by structure. But both survivors are causal, so causality does **not** force the final
constrain-vs-gauge bit; that stays a B-leaning lean. Three honest consequences define the boundary: (i) the
**generation count is `{1, 3}`, not pinned to 3** -- the order-3 symmetry acts on `Lambda^2_+` as an `SO(3)`
rotation (one fixed axis plus one rotated pair), and a net index of exactly 3 sits in the fixed-axis residue
(carrier A's), so no order-3 datum can certify three (the "order-3 forces three" inference was checked and
refused); (ii) the gravity soldering (even sector) and the count's gamma-trace constraint (odd sector) are
two logically independent declarations of the one object, unifiable only under a single geometric-posture
meta-choice; (iii) the framework is **one forced build from complete, and that build needs one unbuilt input**
-- the source action's causal-cure term (a non-minimal Rarita-Schwinger coupling), which the built action
does not yet contain. GU has the acausality *trigger*, not the *cure*. This is the honest terminal boundary:
a single named unbuilt term stands between the present structure and a closed source action, and even across
that term the generation count remains `{1, 3}` rather than a derived three.

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
currently-unwritten object**, and no sector falsifies its structure. This is the
generalization of "located, not forced" from the generation count to the *entire* residual freedom of the
framework.

**The residual, sharpened (2026-07-13).** The one object is no longer only *named*; it is *specified*: the
requirements spec consolidates every leg's demands into 27 rows (8 FORCED / 9 DECLARATION / 10 FIT), sourced
to artifact and test, with NO outright contradiction among the FORCED rows and five named tensions carried
openly (`tests/spec-consistency/source_action_requirements_consistency.py`, 33/33, exit 0). The Yukawa
scoping adds the matter-sector rows at computed grade: the trilinear channel table is complete and rigid,
non-form Higgs carriers are FORBIDDEN exactly (dim Hom = 0), the derived Z/3 cuts 9 couplings to 3 (the
`1+2` block texture, pattern-compatible only), mod-3 Froggatt-Nielsen charges are provably STERILE for all
27 assignments, and the mass hierarchy is SILENT -- source-action-gated like everything else
(`tests/yukawa-scoping/yukawa_trilinear_channels.py`, 20/20, recorded run). And the first build attempt
against the full spec (W125) got a five-term candidate to symbol level, built and passed the SA-C4 kill-test
for the first time, emitted zero of ten FITs source-first (payoff NONE, machine-checked reasons), and named
the single blocking object for the full build, the loop packet, and SA-G9 alike: **the covariant operator on
`Y14`**.

**And its honest counterweight.** The conditional theorem's ledger has also grown a hard entry that is NOT
an antecedent: the AF-branch scalaron tachyon (honest negatives below) is a computed property of the
declared action, not a freedom the source action can select away -- what the source action can still decide
is which *branch* (AF vs AS, via the Reuter fork) the theory runs on, and only the AS branch or a
non-perturbative mechanism could remove the instability. Stated per branch: on AF, renormalizability +
asymptotic freedom + spin-2 grading stability + two-loop graded cleanliness AND the tachyon; on AS
(Reuter-fork), none of these is yet computed.

**Honesty brake (the E-audit rule, kept explicit):** "reduced to one X" is *not itself* progress
-- the "one object" is genuinely a **conjunction** of distinct data (the soldering `!=` `mu_DW` `!=` the
fermion `C2`/2-bit count `!=` the gauge vacuum), stably named but not literally one object; only a **forced**
construction of the source action, or a genuine **discriminator**, changes the epistemic state. The DESI
tension, cited here in earlier drafts as the example discriminator, has now discriminated -- negatively
(Sec 2.4). **E1/Lakatos watch note (added at referee's insistence, 2026-07-13):** the one-object pattern has
now recurred one level down -- the "single unbuilt object" was the source action; after the first build
attempt it is the covariant operator on `Y14` *inside* the source action. A research programme whose sole
blocking object keeps reappearing at a sharper location is exhibiting exactly the pattern the E1 rule exists
to flag; we record the recurrence openly and treat "reduced to the `Y14` operator" as a MAP, not progress,
until that operator is built or shown unbuildable.

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
4. **Loop-level unitarity** -- only **tree level** is shown for *positivity*. Bateman-Turok prove tree-level
   positivity, and their spin-2 ghost decouples; the full-Stelle loop *positivity* is the generic-Stelle-
   Mannheim open frontier (H16 BAR 1). This premise is now *narrowed* by the UV arc (Waves 42-47, see the UV
   bullet in the honest-status ledger below): GU is power-counting **renormalizable** and, in a one-loop
   truncation, **asymptotically free**, so the loop question is no longer "does GU resolve the ghost no better
   than the generic theory" but the single sharply-located residual of loop *positivity* at the negative
   fixed-ratio. Renormalizability and asymptotic freedom are established (at their grades); loop positivity
   alone remains open. *2026-07-13 update, both directions:* the AF picture SURVIVES its first FRG
   truncation (W119: AF trajectory, negative fixed-ratio, and RG-stable spin-2 grading all survive across
   regulator families; the one-loop uniqueness clause breaks via the already-catalogued Reuter FP, which is
   the AF-vs-AS fork made concrete; the ghost-mass construction fork is confined to the UV endpoint); the
   graded prescription EVADES the CLOP order-of-limits ambiguity at fixed order (W120: the ambiguity
   attaches to the removal step keep-and-grade does not perform) and develops NO ambiguity of its own at
   two loops (W124: graded-unambiguous at fixed order; the CLOP band's endpoints are exactly the two
   families' answers, `0` and `+1` times the graded cut); the no-local-positive-metric theorem is hardened
   (W121). The remaining price is precise: the even-cut inter-family disagreement (+1 vs 0) and the
   odd-ghost-cut leak at `s > (2m+M)^2` persist -- that leak IS the open loop-positivity question, now at
   two-loop scalar-core resolution (spin-2 tensor numerators OPEN). Note the boundary of this premise: the
   spin-0 tachyon (honest negatives below) is NOT part of it -- it is unconditional on the AF branch and no
   loop-positivity outcome removes it.
5. **The generation count is located, NOT forced** -- located in the odd-primary boundary summand at
   **principle** grade (Nielsen-Ninomiya / Callan-Harvey / Kaplan), not proven for the true RS/`Y14` index;
   the count itself is a rigid 2-bit residual, not derived (Sec 3).
6. **Heterodox status** -- GU is a heterodox theory most physicists do not accept. This document is a
   reconstruction/audit ("taken seriously and computed carefully, here is what holds and at what grade"),
   not an endorsement; the SM/QM inputs use standard rep theory / generalized-Born-rule work, not novel derivations.

**Honest negatives (kept IN -- they are load-bearing):**
- **Dark energy is FALSIFIED against DESI's `(w_0, w_a)` CPL contour (the arc's first hard negative).** This
  sector no longer merely "tensions" with DESI; it fails the comparison DESI headlines. H42
  (`explorations/wave19/`) found `f_0` is **not source-first derivable** (it needs the unbuilt source-action
  inputs `B_i`, `mu_DW`), and that freeing `f_0` does not help. H43 (`explorations/wave20/`) then closed the
  remaining freedoms: **no admissible OQ2 `M^2`** (root systems `BC_1=8`, `A_1=7`, `S^3=3`, threshold `20.25`),
  **no point in the entire free `(M^2, f_0)` plane** (global closest `3.20 sigma`), and **no ansatz variant**
  (1-component `3.18 sigma`) rotates the GU locus into the DESI degeneracy. It is a robust shape/direction
  miss (canonical joint `4.19 sigma`). **Two honest bounds on the scope**, both computed not asserted: (i) this
  falsifies the `(w_0, w_a)` **CPL parameterization** DESI reports, not the raw expansion history -- GU's `w(z)`
  is non-CPL and reaches `~1%` RMS on fixed-`Omega_m` distances (near BAO precision), so the CPL projection is
  lossy; (ii) the one untested freedom is the **background** -- H43 assumed an LCDM background, and a
  self-consistent `theta`-backreacted background (H44) is the sole remaining thing that could rotate the locus.
  The gravity intersection does not rescue `f_0` either (the corrected `M^2/r^6` residual breaks the order
  match, H3). Wave 25 (H44) then closed that escape: a self-consistent `theta`-backreacted background
  (backreaction real, `+3.6%` on `H` at `z ~ 1`) shifts the locus amplitude but not its direction (closest
  `3.22 sigma` vs `3.20`), so the falsification is not a fixed-background artifact. Net: on the
  parameterization the data is reported in, GU's dark energy is **falsified as a `(w_0, w_a)` CPL fit** --
  every CPL-projection rescue route (amplitude, OQ2 `M^2`, component count, initial conditions, self-consistent
  background) is spent. But Wave 29 (H46, `explorations/wave29/`) then tested the raw expansion history against
  the actual DESI DR2 BAO likelihood (13-dim mean + full covariance, Planck CMB prior) and found **MARGINAL,
  not a distance-level kill**: at the disciplined canonical-plus-CMB-fixed point GU is excluded
  (`delta chi^2 = +21.6` vs LCDM), but that exclusion evaporates the moment the overall amplitude or `f_0` is
  freed -- shape-marginalized, GU is competitive-to-better than LCDM (`delta chi^2 = -3.2`). So the honest
  register is precise: GU's dark energy is **falsified as the CPL summary DESI headlines, but viable as a
  distance model [SUPERSEDED by H46C -- see the end of this bullet]** -- the sector is *cornered* (no single `f_0` satisfies both the CPL contour and the raw BAO
  distances) rather than dead. This is a distinct non-CPL dark-energy model, not an accommodation and not a
  clean kill. **CORRECTION (W113, the joint-profile re-run):** H46's residual "`f_0` tension" was a
  fixed-amplitude-slice ARTIFACT. Profiling jointly over `(f_0, amplitude)` (amplitude analytically
  marginalized): the canonical `f_0 = 0.125` sits INSIDE the joint `Delta chi^2 <= 1` band (`Delta = +0.10`;
  band `f_0 in [0.04, 0.15]`, best `-3.27` at `f_0 = 0.10`, GU-beats-LCDM window `[0.005, 0.25]`). The ENTIRE
  canonical exclusion lives in a single direction: GU needs the BAO amplitude `+1.81%` above the Planck
  calibration (pinning it costs `chi^2 = +41.3`). So the honest current statement: the shape AND the canonical
  `f_0` are both viable; the sector's one residual exclusion is an amplitude-calibration direction, not a shape
  or parameter tension. (`tests/W113`, reproduces H46's numbers exactly before extending; no DESI DR3 BAO exists
  as of 2026-07.) **FALSIFICATION-HARDENED (H46C, wave 46, 2026-07-13; supersedes both the "viable as a
  distance model" register above and the W113 "amplitude-direction-only" softening):** the Wave 45 blocker B1
  was executed -- instead of arguing the Planck amplitude onto GU, GU's OWN CMB-calibrated amplitude was
  computed by imposing the measured acoustic scale `100 theta_star = 1.04110` on GU's own `H(z)`. Result:
  `H0_GU = 63.75` (`-5.4%`), so GU's own calibration OVERSHOOTS the BAO-preferred amplitude for its own shape
  by `+5.7 sigma_A`; the three-way table is `dAIC = +21.58` (Planck-fixed amplitude) / `+35.78` (GU's own
  theta_star calibration) / `-3.17` (amplitude freed -- now shown to have NO CMB-consistent realization);
  profiling `omega_m h^2` for BOTH models under the Planck prior leaves `dAIC = +16.03`. With per-`f_0` CMB
  calibration the BAO-preferred `f_0` is the LCDM limit `f_0 -> 0` (3-sigma-equivalent bound `f_0 < ~0.027`),
  so the W113 in-band `f_0 = 0.125` reading was an artifact of holding the amplitude at the Planck value. Net:
  GU's dark energy is **falsified as the DESI CPL summary AND excluded as a CMB-consistently-calibrated
  distance model for `f_0 >= ~0.03`**; it survives only as a subdominant component indistinguishable from a
  small addition to LCDM. Scope, honest: exploration grade, `M^2 = 8 H0^2` only (OQ2 open), BAO + theta_star
  only; the canon verdict stays OPEN at exactly that component-only scope (CORRECTION DARK-ENERGY-05).
  Digits verified against primary sources (H46B, `tests/wave45/H46B_referee_grade_desi_verification.py`,
  33/33, exit 0); `tests/wave46/H46C_theta_star_cmb_calibration.py`, 20/20, exit 0, with LCDM positive
  controls recovering Planck's `theta_star` and `h = 0.6736`.
- **The gravity sector survives a direct kill attempt, but the "Lambda emerges" headline does not.** An
  adversarial probe of the Bach/Weyl graviton sector (H49, `explorations/wave28/`) confirmed GU's linearized
  operator IS the conformal/Bach operator (`box^2 h = -4 Bach`, re-derived) and then found that on the favored
  `|II|^2` branch **no known conformal-gravity refutation transfers**: the Ostrogradsky ghost is tree-cleared
  (Krein), and the Horne / Hobson-Lasenby no-flat-rotation-curves result is evaded because the Einstein-Hilbert
  term makes the Bach sector a *short-range* massive spin-2 (Yukawa range `< 52 um`), so there is no long-range
  `gamma*r` to refute. GU is thus a genuinely distinct, testable 4th-order theory, not refuted conformal
  gravity -- but this survival is `|II|^2`-specific (pure `|H|^2` inherits the refutation and dies). Two honest
  costs: (i) a **class-level scope-kill** -- a scale-free two-metric action fixes only `O(1)` ratios, so the
  observed `Lambda / M_Pl^4 ~ 10^-123` needs an imported scale the action cannot contain; the claim that
  *Lambda emerges from the two-metric structure* is dead for GU and for the entropic (Bianconi) alternative
  alike, though neither theory is falsified by it (neither derives the magnitude); (ii) all of GU's empirical
  content is gated on the single scale `mu_DW` -- at `mu_DW ~ M_Pl` every deviation is `~10^-35 m` and
  decoupled, while at `mu_DW ~ meV` (the dark-energy scale) GU predicts a **sub-millimetre Stelle-Yukawa
  deviation**, its one live falsifiable handle. Wave 30 (H50, `explorations/wave30/`) made this concrete: one
  `mu_DW` sets *both* the DeWitt-Lambda (`rho_Lambda ~ c_L mu_DW^4`) and the graviton mass
  (`m2 = sqrt(m2_eff) mu_DW`), so *identifying* the DeWitt-Lambda with the observed dark energy (the H36
  postulate, not forced) fixes `mu_DW ~ 2.3 meV` and **predicts** a Yukawa of range `lambda` at strength
  `alpha = 1/3`. Wave 31 (H51) then computed the last unknown -- the DeWitt coefficient `c_L = 3/8` exactly
  (from the horizontal sectional) -- giving `lambda = 60-74 um`. Against the actual short-range-gravity bounds
  (Kapner/Lee/Tan) that prediction is **excluded** (the `alpha = 1/3` reach sits near `45-52 um`), by an O(1)
  but robust margin. So GU's first parameter-linked prediction, taken to the end, **self-falsifies the H36
  identification** (DeWitt-Lambda = the observed dark energy is ruled out by sub-millimetre gravity,
  O(1)-robustly) -- it does *not* falsify GU-gravity itself, which survives, but *without* H36 the scale
  `mu_DW` is free and GU is decoupled/untestable in this channel. This is the honest arc of GU's first genuine
  prediction: it was computed to the end and it failed conditionally, exactly what a real prediction is
  supposed to risk. Two residual O(1) inputs remained (the `alpha = 1/3` exclusion curve argued not
  digitized; the background-vs-TT normalization of `c_L`). **Upgrade (H52, wave 32, 2026-07-13): the H36
  exclusion is now CITED, not argued.** The `alpha = 1/3` boundary is anchored to published numbers:
  `lambda_max(alpha = 1/3) = 47.6 um` (Lee 2020, via the published `n = 1` radion bound `M* >= 7.1 TeV` and
  the published fit `lambda = 2.4 (TeV/M*)^2 mm`); the H36 window `[60.0, 73.6] um` is EXCLUDED-CITED with
  margin 1.9-9.8x, and the resolved `mu_DW` floor is `>= 3.71-4.54 meV` central (envelope `[3.4, 4.7] meV`),
  superseding H50's 2007-data floor of 3.0-3.6 meV (`tests/wave32/H52_alpha13_boundary_cited.py`, 18/18,
  exit 0). Of the two residual O(1) inputs, the exclusion-curve digitization is DISCHARGED; the
  background-vs-TT normalization of `c_L` remains (W126 additionally flags a 16/3 normalization ratio
  between the flat-slice and horizontal-sectional chains; signs robust). Track 2's conditional ledger
  (given the declared postulate set S, stated and never asserted) then fixes the surviving phenomenology
  plainly: `alpha = 1/3` exact; the allowed window is `mu_DW >= ~3.4-4.8 meV` with no experimental upper
  edge; and inside the window GU-given-S predicts EXACTLY GR at LIGO (massless pole exactly massless; the
  massive companion 9+ orders above the excitable band)
  (`tests/track2/T2A_graviton_sector_numbers.py`, 8/8, exit 0).
- **The AF branch carries a NATIVE, tree-unliftable, positive-norm tachyonic scalaron (W122/W123/W126) --
  the UV arc's hard negative, at full strength.** On every asymptotically-free trajectory of the declared
  4th-order action the spin-0 (conformal-mode) scalaron has `m_0^2 = gamma/(6c) < 0` (with `c` the direct
  `R^2` coefficient, reciprocal to and sign-matching the agravity `f_0^2` used elsewhere in this paper;
  the coincidence with the published agravity `M_0^2` under the convention map is an exact identity, W123)
  and POSITIVE
  norm: a genuine spectral instability, not a ghost, so there is nothing for the keep-and-grade Krein
  rescue to grade. Three escapes were attacked and closed. (i) *Not a gauge artifact* (W122): the exact
  auxiliary-field/Legendre route derives the mass with no gauge parameter anywhere it could enter;
  `Weyl^2` contributes exactly zero spin-0; the Euclidean conformal-factor problem is cleanly delineated
  as category-inapplicable to a Lorentzian mass sign (`tests/W122_spin0_scalaron_auxfield.py`, 27 checks,
  exit 0). (ii) *Not a porting artifact* (W123): the convention chain repo <-> Avramidi-Barvinsky <->
  agravity is pinned by an exact cross-lineage identity with physical anchors at both ends (`gamma > 0` =
  attractive gravity, computed natively two ways; `f_0^2 < 0` = tachyon in the literature's own reading);
  no admissible field content can flip the fixed-ratio sign (the flip threshold is unreachable, the
  self-coefficient a sum of perfect squares with `d_RS_R2 = 0` computed); and a one-line MONOTONICITY
  THEOREM forbids positive-`f_0^2` AF trajectories outright -- `f_0^2 > 0` Landau-poles in bounded `t`,
  so `f_0^2 < 0` at EVERY finite scale on EVERY AF trajectory
  (`tests/W123_native_r2_sign_convention_audit.py`, 34/34, exit 0). (iii) *No tree-level vacuum lift*
  (W126): the induced `|II|^2` functional's potential sector on the conformal family terminates at `R^2`
  IDENTICALLY (`c_3 = c_4 = ... = 0`, all orders in `phi`, two independent routes; MSS-slice
  `F(R) = 2 + R/3 - R^2/9`, whose negative tree-level `R^2` coefficient natively corroborates the ported
  sign direction); the unique extremum is the tachyonic top and the potential runs away to the `f' = 0`
  wall; the loop-`R^3` rescue is ghost-infested in its window and out-of-validity beyond it on both W46
  branches (`tests/W126_beyond4th_conformal_iisq.py`, 32 checks, exit 0). **Stated plainly, branch by
  branch:** this is NOT a conditional antecedent -- it is a computed property of the AF branch of the
  declared action. On the AF branch, GU keeps renormalizability, asymptotic freedom, the RG-stable spin-2
  Krein grading, and fixed-order graded cleanliness through two loops -- and it keeps the tachyon. The two
  thin escapes, named: (a) the **AF-vs-AS fork** -- W119's FRG truncation shows the Reuter fixed point
  appears once canonical linear terms are included (already catalogued, W83/W88; a 300-seed hunt finds no
  fixed point outside {Gaussian, Reuter}); an asymptotically-SAFE branch is a different flow whose
  scalaron status is NOT computed here; (b) a **non-perturbative mechanism** beyond the computed
  truncations (tree-exact potential; one-loop and minimal-FRG flows). Nothing built today realizes either
  escape.
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
- **Zero parameter-free predictions to date.** An adversarial predictive-content audit (H34,
  `explorations/wave18/`) classified every material claim and found the honest register is *accommodation*,
  not derivation: no claim emits an observed number source-first with no free parameter or chosen sub-block
  doing the load-bearing work. The single novel positive is the *compression* (all remaining freedom routes
  to one named source-action object) -- a structural result, not a prediction. The one place the framework
  touches data (dark energy) is a fit on `f_0`, which is exactly why the DESI tension (marginal `w_a` at
  `+2.55 sigma` from the DR2 primary source) was then read as soft rather than fatal *[SUPERSEDED: H46C has
  since removed the amplitude freedom that made it soft -- see the DE bullet above]*. The `ACCOMMODATES` headline is, on
  this ledger, honest and if anything conservative. **Update (H50-H51):** GU produced its first genuine
  parameter-linked prediction and then *computed it to the end*. Given the H36 identification (DeWitt-Lambda =
  the observed dark energy), the single scale `mu_DW` is fixed and GU predicts a specific sub-millimetre
  gravity deviation (`lambda = 60-74 um` after `c_L = 3/8` was computed exactly, `alpha = 1/3`). Against the
  actual short-range-gravity bounds that prediction is **excluded** -- so the exercise **conditionally
  falsifies the H36 identification** rather than yielding a standing prediction. Net: GU still has **zero
  standing predictions** (the one candidate was computed and it failed conditionally), it *does* now have a
  demonstrated *capacity* to emit falsifiable numbers, and GU-gravity itself survives while being decoupled
  without a scale principle. The honest register is unchanged -- accommodation, plus a demonstrated (and so far
  self-falsifying) predictive channel.
- **The scientific register, stated plainly (H53 falsifiability audit).** A full sector-by-sector audit
  settles what GU is at present: **a consistent, reconstruction-grade geometric *framework*, not a standing
  theory.** Of eleven channels, four require the free scale `mu_DW`/`f_0`, three are settled (all failures or
  scope-kills), three are gated on the unbuilt source action, and exactly one is scale-independent -- the
  4th-order action structure (7-vs-2 propagating DOF), which is a genuine *property* distinguishing GU from GR
  but **not an accessible observable**: every GU-vs-GR effect scales as `(E/m2)^2` and vanishes as
  `mu_DW -> M_Pl`. So GU is **falsifiable in principle, decoupled in practice** -- zero standing predictions,
  though its predictive *capacity* is demonstrated (it emitted a real number that self-falsified, so it is not
  vacuous). Consequently GU's very falsifiability rests on building the source action (the one object that
  would force `mu_DW`): that build is the *falsifiability* keystone, not merely the coherence keystone. Until
  it exists, the honest verb is **accommodates**, and the honest noun is **framework**.
- **The keystone is not a blank build -- it is a mapped, shape-dimension-1 family (landscape assessment).** A
  methods scan + a consistency-carve (Waves 34-35, `explorations/wave34`, `wave35`) reframe the source action
  from "blocked/hardest/unforceable" to a *small, mapped* object. The causal-cure term GU needs is a *known*
  constructible type (a Porrati-Rahman non-minimal massive-spin-3/2 coupling); imposing all constraints jointly
  for the first time -- causality, count-selection, positivity, Krein, soldering -- leaves the source action
  determined **up to a single gravity-shape ratio** (`beta/alpha`, the `|II|^2`-vs-`|II_0|^2` fork) plus two
  overall scales, with the cure and the carrier both *forced* and GU neither killed (the joint constraints are
  consistent) nor yet fully forced. Crucially, UV-completeness -- GU being a standing theory rather than a
  finite-cutoff EFT -- reduces to a single concrete, GU-internal question: **does `Sp(32,32;H) + [P,S]=0`
  furnish a guardian symmetry (a local-SUSY / super-Higgs gravitino)?** If it does, GU is UV-complete *and* the
  gravitino mass would fix `mu_DW`, promoting the framework to a falsifiable theory in one stroke. The honest
  register is unchanged today (framework), but the path to a theory is now a well-posed question, not a wall.
- **The guardian question is answered: GU is *not* a supergravity (a five-branch blind investigation).** The
  well-posed question above was attacked by five independent, mutually-blind specialist teams
  (`explorations/wave37`-`wave41`), and they converged: GU has the *field content* of a supergravity -- its
  Rarita-Schwinger field **is** a gravitino (the `ker Gamma` cure is exactly the gravitino gauge condition),
  and an abstract graded algebra `siso(9,5|N)` exists -- but it **lacks the guardian symmetry**. The ghost-
  clearing `[P,S]=0` is a bosonic Krein parity, not the SUSY Ward identity (GU clears its ghost the *anti*-SUSY
  way); the graded symmetry GU's structure actually realizes closes on the spin connection, not on
  translations, so it is not spacetime supersymmetry; and even a local SUSY would not UV-complete GU's *finite*
  content (no Regge tower). Both hoped-for payoffs therefore fail: no UV-completion, and `mu_DW` stays free
  (super-Higgs *relates* the scale, it does not fix it). The honest conclusion is that GU is a **one-scale
  finite-cutoff EFT** -- gravitino-shaped but not supersymmetric -- whose only remaining route to UV-status is
  *renormalization-theoretic* (Stelle-style 4th-order renormalizability plus the Krein ghost rescue extended to
  the matter sector), not a symmetry. That route, like everything else, routes back to the one unbuilt source
  action.
- **The renormalization route is open, and it is GU's strongest positive UV result: renormalizable and
  asymptotically free, with only loop positivity left (the UV arc, Waves 42-47).** The renormalization-theoretic
  route named above was then attacked directly, and it is the best the framework has done on the ultraviolet.
  *Renormalizability (H58, `tests/W44...`, CONFIRMED):* two independent power-counting computations give a
  superficial degree of divergence `D <= 4` on the `ker Gamma` subspace for every loop order -- the
  Rarita-Schwinger sector does **not** spoil renormalizability, because the `ker Gamma` transverse projector has
  momentum-degree 0 and removes exactly the `n = 2` Velo-Zwanziger danger modes that make a generic
  gravity-coupled spin-3/2 non-renormalizable (the projector's degree-0, gamma-traceless property is *computed*,
  residuals `~1e-16`, not assumed). The RS sector adds its own *finite, closed* counterterm set beyond pure
  Stelle -- an extension, not a proliferation, which is the content of renormalizability. *Asymptotic freedom
  (H57/H60, `tests/W45-W47`, DERIVED-on-PORTED, one-loop truncation):* running the ported agravity one-loop beta
  functions (Weyl coupling asymptotically free, `b_2 = 133/10 > 0`) with the RS matter contribution added, the
  Gaussian point is the **unique** UV fixed point -- so GU realizes asymptotic *freedom* (couplings flow to
  zero), stronger than mere safety, and the Weyl coupling `f_2` is thereby *predicted* rather than tuned (the one
  genuine predictivity gain over generic higher-derivative gravity). The firming pass (H60) made this
  *structural*, not merely numerical: the one-loop system is homogeneous-quadratic (`beta(k g) = k^2 beta(g)`),
  which mathematically **forbids** any isolated interacting fixed point for *any* value of the (imperfectly
  known) `ker Gamma` matter coefficients, so no non-Gaussian fixed point can appear at this order regardless of
  the one uncertain input (the RS trace-anomaly coefficient, tightened to `[1.02, 1.82]`; asymptotic freedom
  survives for any value above `-13.3`). The UV critical surface has dimension `~3` in the known gravitational
  sector (`M_Pl = mu_DW`, `Lambda`, `f_0^2`), so predictivity is preserved. **Honest scope, stated sharply:**
  this is a one-loop, small-truncation result (an *indication* made structurally robust, not a proof -- a genuine
  functional-RG/Reuter truncation and higher loops remain), and a UV fixed point is a statement about the
  *renormalization-group flow only*: it does **not** settle Krein loop *positivity*, which is independent. The
  arc in fact *locates* where the two remaining UV questions touch -- the asymptotically-free trajectory sits at a
  **negative** conformal-mode ratio `f_0^2 / f_2^2 < 0`, and whether that wrong-sign direction is admissible is
  exactly the loop-positivity question. **[REFINED by W122/W123/W126, 2026-07-13: the wrong-sign direction is
  now ANSWERED in the spin-0 channel -- it is a genuine positive-norm tachyonic scalaron, native and
  tree-unliftable (see the dedicated honest-negative bullet above), a spectral instability logically distinct
  from, and not curable by, the spin-2 loop-positivity question.]** Net register, updated: GU is a
  renormalizable, asymptotically-free, finite-content 4th-order theory -- a picture that now also SURVIVES its
  first FRG truncation (W119: AF trajectory, negative fixed-ratio, and spin-2 grading stability all survive
  regulator-sweeps; the sole break is the one-loop uniqueness clause, via the already-catalogued Reuter FP =
  the AF-vs-AS fork) and is fixed-order-clean through two loops on the graded side (W120/W124: the CLOP
  ambiguity attaches only to the removal prescription; the graded theory develops no ambiguity of its own;
  its price is the persisting odd-ghost-cut leak) -- whose remaining UV obstructions are now TWO, cleanly
  split: (1) loop positivity of the keep-and-grade Krein rescue for the spin-2 ghost, the open frontier of
  PT/Krein QFT (no keep-and-grade rescue is proven at loop level anywhere: Kuntz 2024, Nakayama 2023,
  Bateman-Turok tree-only), an inherited frontier problem, not a GU-specific defect; and (2) the AF-branch
  spin-0 tachyon, which IS GU-specific (it follows from the declared action's induced `gamma > 0` conjoined
  with `f_0^2 < 0` on every AF trajectory) and survives every escape computed to date. The earlier "one
  solved frontier problem away from UV-complete" phrasing is accordingly SUPERSEDED: one inherited frontier
  problem plus one GU-specific instability (with its two named thin escapes) stand between the finite-cutoff
  EFT verdict and UV-completeness.

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
without building the object. *2026-07-13 update:* the construction problem is now engineering-posed -- the
27-row requirements spec is the closure criterion, the first build attempt (W125) reached symbol level with
the SA-C4 kill-test passing, and the named blocking object is the **covariant operator on `Y14`** (the
propagator and vertex on the bundle, not the flat symbol). Building that operator is the next concrete step;
per the E1/Lakatos watch note (Sec 4), naming it is a map, not progress. **Loop-level `[P,S]=0` positivity**
is the separate, harder, generic-Stelle-shared
frontier. The UV arc (Waves 42-47) sharpened it without closing it: GU is now established renormalizable and
(one-loop) asymptotically free, so the UV question is reduced to loop *positivity* alone, and that residual is
*located* at the negative conformal-mode ratio `f_0^2/f_2^2 < 0` on the asymptotically-free trajectory. It
remains the open frontier of PT/Krein QFT and is not resolvable without a loop-level treatment of the keep-and-
grade rescue (candidate route: an FRG/Reuter truncation, which could also promote the one-loop asymptotic
freedom to a non-perturbative statement). *2026-07-13 update:* the first leg of that candidate route is
executed -- W119's minimal FRG truncation confirms the AF picture survives (and concretizes the AF-vs-AS fork
via the catalogued Reuter FP), and the two-loop fixed-order landscape is computed (W120/W121/W124: graded
prescription unambiguous at fixed order; CLOP band endpoints are the two families' answers; the odd-cut leak
persists as the precise open price). What no truncation or fixed-order result touches is the AF-branch spin-0
tachyon (honest negatives): closing loop positivity for the spin-2 ghost would NOT lift it; only the AS
branch or a non-perturbative mechanism could.

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
   `C2`/count. Loop-level `[P,S]=0` positivity is the separate, harder frontier.
4b. **DONE (UV arc, Waves 42-47):** GU is established power-counting **renormalizable** (H58, `tests/W44...`,
   `D <= 4` on the `ker Gamma` subspace; the RS sector adds a finite closed counterterm set) and, in a one-loop
   truncation, **asymptotically free** (H57/H60, `tests/W45-W47`, all exit 0; unique Gaussian UV fixed point,
   `f_2` predicted, `~3`-parameter critical surface incl. `mu_DW`; made structural via homogeneous-quadratic
   betas that forbid an interacting fixed point). Folded into the honest-status ledger and premise 4. The sole
   remaining UV obstruction is loop *positivity* of the keep-and-grade Krein rescue, located at the negative
   fixed-ratio -- the open frontier of PT/Krein QFT, not a GU-specific defect. Grade: DERIVED-on-PORTED,
   one-loop / small-truncation (an indication made robust, not a proof); FRG/higher-loop firm-up is future work.
4c. **DONE (2026-07-13 three-wave consolidation, folded in by W127):** (a) the dark-energy verdict is
   falsification-hardened (H46B digit gate + H46C theta_star calibration; Sec 2.4 header + honest-negatives
   bullet; every prior "viable as a distance model" / "soft, amplitude-gated" statement carries a
   supersession marker); (b) the AF-branch scalaron tachyon is folded in at full strength as a native,
   tree-unliftable computed property (W122/W123/W126; dedicated honest-negative bullet; premise 4 boundary
   note); (c) the UV/loop state is updated (W119 FRG survival with the Reuter/AF-vs-AS fork catalogued;
   W120/W121/W124 fixed-order graded cleanliness through two loops, odd-cut leak as the precise open price);
   (d) the residual is sharpened to the 27-row requirements spec + the W125 first build with SA-C4 passing
   and the covariant operator on `Y14` as the single blocking object, with the E1/Lakatos watch note added
   (Sec 4); (e) H36's sub-mm exclusion upgraded to EXCLUDED-CITED with the resolved `mu_DW` floor (H52), and
   Track 2's conditional GU-given-S ledger recorded at its firewalled grade; (f) the Yukawa channel table and
   its no-gos folded in (Sec 4). Verification ledger with W127 re-run exit codes in the 2026-07-13 block.
5. Figures: the sector scoreboard; the Wave 1-8 gravity ledger; the maximal-compact = SM computation; the
   primary-partition table.

Grade: structural result at honest grade; three sectors existence/consistency-cleared (reproducible), gravity
a **tree-level conditional theorem** (clear-modulo-soldering + `mu_DW`; loop-level open; AF-branch scalaron
tachyon stated as a computed negative), dark energy the honest hard negative (falsified as the CPL summary,
excluded as a CMB-calibrated distance model, surviving as a subdominant component only), the
reduction-to-one-object is the contribution. All quantitative claims tie to reproducible tests
(`tests/one-residual/`, `tests/wave1..wave8/`, `tests/legs/`, `tests/family-puzzle/`, plus the 2026-07-13
consolidation ledger's tests, all exit 0). Target:
hep-th / math-ph. External publication Joe-gated (NOT in scope here: no arXiv, no submission). Supersedes/subsumes
`papers/candidates/generation-number-boundary-odd-primary/` and the located-not-forced draft as legs.
