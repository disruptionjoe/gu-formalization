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
enough to be falsified, not that it fits.)

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
  distance model** -- the sector is *cornered* (no single `f_0` satisfies both the CPL contour and the raw BAO
  distances) rather than dead. This is a distinct non-CPL dark-energy model, not an accommodation and not a
  clean kill.
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
  supposed to risk. Two residual O(1) inputs remain (the `alpha = 1/3` exclusion curve is argued not
  digitized; the background-vs-TT normalization of `c_L`).
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
  `+2.55 sigma` from the DR2 primary source) is soft rather than fatal. The `ACCOMMODATES` headline is, on
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
