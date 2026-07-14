---
artifact_type: exploration
status: exploration (5-persona inline team; deterministic test; H59 North-Star flow/grading-side advance)
created: 2026-07-13
hypothesis: H59
branch: "W119 -- FIRST minimal FRG truncation probing the Krein grading at the negative fixed-ratio: does the one-loop AF picture (unique Gaussian UV FP, negative fixed ratio f_0^2/f_2^2 < 0, RG-stable spin-2 grading) SURVIVE or BREAK when the one-loop betas are replaced by a Wetterich-equation truncation (EH + Weyl^2 + R^2, three regulator families), with the ghost-mass construction fork carried on both branches?"
title: "VERDICT: SURVIVES-WITH-ONE-CATALOGUED-BREAK. In the minimal FRG truncation (polynomial R^2 + Weyl^2 + canonical EH linear terms; Litim + exponential + shape-swept regulators): (1) the AF trajectory SURVIVES -- f_2^2* = 0 is a structural root and f_2^2 stays marginally irrelevant; (2) the NEGATIVE FIXED-RATIO SURVIVES at every admissible regulator -- both roots of the dressed ratio quadratic stay real and strictly negative across the whole computed threshold band (structural Vieta argument: any positive dressing preserves the signs; a sign flip is IMPOSSIBLE, and losing realness needs a ~70x dressing asymmetry the admissible band cannot supply -- worst-case grid discriminant 63.4 > 0); (3) the spin-2 Krein grading is RG-STABLE at every finite scale on BOTH ghost-mass fork branches -- the fork decides ONLY the UV-endpoint behavior (agravity branch m2^2 ~ f_2^2: pinch onto the locus at the free endpoint = W53's BOUNDARY, now regulator-swept; GU-native fixed-scale branch m2 = sqrt(m2_eff) mu_DW: d_locus = m2_eff in [5/6,5/4] constant = STAYS-CLEAR, no pinch), and W89's eta_C scheme fork can lift even branch A clear of the locus (HORN-Q side); (4) the ONE thing that BREAKS is the UNIQUENESS clause of the one-loop picture -- canonical linear terms destroy the homogeneous-quadratic structure and the Reuter FP appears, exactly the non-Gaussian FP the one-loop argument could not see, already catalogued (W83/W88), NOT a new ambiguity: a 300-seed multistart hunt finds NO fixed point outside the enumerable {Gaussian, Reuter} families; (5) the spin-0 conformal-mode sign (M_0^2 < 0 on the AF trajectory) is UNCHANGED by dressing -- the FRG truncation neither rescues nor kills it, W78's physical-vs-gauge question remains the load-bearing open item. H59 itself remains OPEN (W48 gate: flow-side evidence is insufficient; no loop amplitude computed)."
grade: "DERIVED-on-PORTED, exploration-grade, truncation- and regulator-dependence explicit. DERIVED/STRUCTURAL: threshold-integrand positivity r - y r' = s y^2 e^y/(e^y-1)^2 > 0 for the whole exponential shape family (sympy identity); the Vieta sign argument (any positive dressing keeps both ratio roots negative when real); the breaking-asymmetry bound F_break = (5+b_2)^2/(4*(5/6)*(5/3)) = 70.0 vs the computed admissible band's worst case 24.4; f_2^2* = 0 as structural root; the grading-locus behavior on both fork branches; homogeneity breaking by canonical terms; the exhaustive FP enumeration of the truncation. COMPUTED (two routes where load-bearing): threshold integrals by quadrature vs closed form/analytic reductions (Litim 1/n!; exponential Phi^2_2(0)=1, Phi^1_1(0)=pi^2/6); dressed ratio roots (numpy companion matrix vs explicit quadratic formula, agree to 1e-14); dressed AF flow (RK4 vs analytic leading-log, agree to 1e-14). PORTED (cited, not re-derived): the one-loop marginal coefficients via the W45 BetaSystem import (133/10 + c_RS anchor; 5/3, 5, 5/6); the schematic EH/Reuter sector (W83 calibration, reproduced as positive control); eta_C's two-scheme result (W89, imported with its stated lifted-root band [0.07,0.16]); the ghost-mass fork branch definitions (Salvio-Strumia agravity vs wave20/H43/path4 fixed-scale). The dressing-assignment question (which threshold integral dresses which quadratic coefficient) is NOT resolved -- it is a paper-scale Hessian computation; the asserted conclusions are exactly the ones robust to the assignment (swept over an over-wide band). Deterministic test tests/W119_h59_frg_krein_negative_ratio.py, 17/17, exit 0, with 4 positive controls + 1 negative control. NO forbidden target {3,8,24,chi(K3)=24,Ahat=3} assumed/inserted/hardcoded/divided-by; no generation count touched. NO canon / RESEARCH-STATUS / claim-status / verdict / posture changed. H59 remains OPEN."
depends_on:
  - explorations/H57-flow-stage2-fixed-point-critical-surface-2026-07-11.md
  - explorations/H60-firm-asymptotic-freedom-2026-07-11.md
  - explorations/path2-wave2-target1-af-flow-vs-exceptional-locus-2026-07-11.md
  - explorations/H59-krein-loop-positivity-gate-2026-07-12.md
  - explorations/frg-fr-weyl-af-as-fork-2026-07-11.md
  - explorations/full-frg-fr-weyl-rs-stage1-2026-07-11.md
  - explorations/branch1-eta-c-across-regulators-2026-07-11.md
  - explorations/conformal-factor-mode-gauge-status-2026-07-11.md
  - tests/W45_H57_stage1_beta_system.py
  - tests/W53_path2_target1_af_vs_locus.py
  - tests/W88_full_frg_stage1.py
  - tests/W89_eta_c_across_regulators.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W119_h59_frg_krein_negative_ratio.py
external_refs:
  - "Wetterich, Exact evolution equation for the effective potential, PLB 301 (1993) 90"
  - "Litim, Optimized renormalization group flows, PRD 64 (2001) 105007 -- the optimized regulator; Phi^p_n(0)=1/n!"
  - "Reuter & Saueressig, Quantum Einstein Gravity, NJP 14 (2012) 055022, arXiv:1202.2274 -- threshold functions, regulator robustness"
  - "Codello & Percacci, Fixed points of higher-derivative gravity, PRL 97 (2006) 221301"
  - "Codello, Percacci & Rahmede, Ann. Phys. 324 (2009) 414, arXiv:0805.2909 -- f(R) FRG"
  - "Benedetti, Machado & Saueressig, Asymptotic safety in higher-derivative gravity, MPLA 24 (2009) 2233, arXiv:0901.2984"
  - "Ohta & Percacci, Higher derivative gravity and asymptotic safety in diverse dimensions, CQG 31 (2014) 015024"
  - "Falls, Litim, Nikolakopoulos & Rahmede, A bootstrap towards asymptotic safety, arXiv:1301.4191"
  - "Fradkin & Tseytlin, NPB 201 (1982) 469; Avramidi & Barvinsky, PLB 159 (1985) 269 -- one-loop AF of the Weyl coupling"
  - "Salvio & Strumia, Agravity, JHEP 06 (2014) 080, arXiv:1403.4226 -- agravity ghost-mass convention m2^2 ~ f_2^2 M_Pl^2"
---

# W119 -- first minimal FRG truncation: the Krein grading at the negative fixed-ratio

**Role.** H59's North Star is Krein loop-positivity at the negative AF fixed-ratio -- the single point
where the AF flow (H57/H60) and Krein positivity touch. The one-loop arc (W45/W46/W47) established the
picture perturbatively; W53 showed the spin-2 grading is RG-stable at one loop; the W83/W88/W89 FRG line
attacked the AF-vs-AS fork and the horn (K vs Q). What no prior wave did is ask the H59-shaped FRG
question directly: **do the three one-loop ingredients H59 consumes -- Gaussian UV FP, negative fixed
ratio, grading RG-stability -- survive together in a minimal FRG truncation, with the Krein grading
tracked and the ghost-mass construction fork carried?** W119 answers that, bounded honestly.

Deterministic test: `tests/W119_h59_frg_krein_negative_ratio.py` (17/17, exit 0; numpy + sympy;
4 positive controls, 1 negative control; two independent routes for every load-bearing number).

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline) -- named, both branches computed

| Fork | Standard-physics side | GU program-native side | Handling here |
|---|---|---|---|
| **Ghost mass** | agravity (Salvio-Strumia): `m2^2 = (1/2) f_2^2(k) M_Pl^2` -- rides the running coupling | fixed-scale: `m2 = sqrt(m2_eff) mu_DW`, `m2_eff in [5/6, 5/4]` (wave20/H43/path4) -- a fixed physical mass tied to the DeWitt ratio-only scale | **BOTH branches computed** (cheap). Branch dependence isolated: it decides ONLY the UV-endpoint behavior (Section 4). NOT defaulted. |
| **Gravity action** | freely chosen `R^2`/Weyl^2 | induced `\|II\|^2` -> 4th-order Stelle + induced EH (H49/H25) | Stelle/agravity + EH truncation (the physics-side representation of the induced action, the W83/W88 standing assumption, inherited). |
| **Positivity object** | positive Hilbert space | Krein keep-and-grade `[P,S]=0` | Keep-and-grade. What is tracked here is the GRADING's distance to the exceptional locus `m2^2 = 0` (branch-E/W53 object), NOT loop positivity itself (out of scope; W48 gate). |
| **eta_C scheme** (within-physics, W89) | EH-adapted `Z_h = Z_N` -> `eta_C > 0` | Weyl-adapted `Z_h = 1/f_2^2` -> `eta_C = 0` | IMPORTED as W89's open two-scheme fork; both branches' consequences for the grading computed (Section 4, D3). Not re-decided. |

## 1. Persona 1 -- FRG practitioner: truncation, regulators, ported-vs-derived

**Truncation chosen (minimal defensible).** Polynomial `f(R)`-to-`R^2` + `Weyl^2` + canonical
Einstein-Hilbert dimensionless pair `(g = G k^2, lambda = Lambda/k^2)` -- the W88 Stage-1 truncation,
reused, on the sphere/dS background with York/TT decomposition. This is the smallest system that can see
BOTH the AF trajectory (marginal `(f_2^2, f_0^2)` block) and the grading locus (spin-2 TT block,
`m2^2 = 0` pole collision). Matter enters through the RS anchor already inside the imported `b_2`
(W45's `c_RS_weyl = 17/12`).

**Regulators.** Three families: Litim/optimized `r(y) = (1-y)theta(1-y)`; exponential
`r(y) = y/(e^y-1)`; exponential shape sweep `r_s(y) = s y/(e^y-1)`, `s in [0.5, 2]` (the W85/W86/W89
family). Threshold functions `Phi^p_n(0)` computed by direct quadrature AND by closed form/analytic
reduction (two routes): Litim `1/n!` (Litim 2001); exponential `Phi^2_2(0) = 1` exactly (the integrand
reduces to `y e^{-y}` -- derived in-file) and `Phi^1_1(0) = pi^2/6`. The computed admissible band across
all families and the three relevant `(p,n)` types is `[0.50, 2.47]` (deliberately over-wide: it includes
`Phi^1_1`-type integrals that are unlikely to be the ones dressing the quartic coefficients).

**Ported vs derived (the honest ledger).**
- PORTED: the one-loop marginal coefficients (`b_2 = 133/10 + c_RS`; `5/3, 5, 5/6`), imported live from
  the W45 `BetaSystem` (KNOWN/PORTED grade inherited); the schematic EH/Reuter sector (W83 calibration);
  `eta_C`'s two-scheme result (W89); the ghost-mass fork branch definitions.
- DERIVED here: the threshold positivity identity; the dressed-ratio Vieta argument; the
  breaking-asymmetry bound; the grading-locus tracking on both fork branches under dressing; the
  homogeneity-breaking demonstration; the FP enumeration of the truncation.
- NOT DONE (named): the exact Hessian projection assigning specific `Phi^p_n` to specific quadratic
  coefficients (paper-scale). The conclusions asserted are exactly the ones swept robust to that
  assignment. At the Gaussian point itself no assignment is needed: the one-loop coefficients of
  marginal couplings are universal (regulator-independent), so the dressing question only bites along
  the flow at finite `(g, lambda)`.

## 2. Persona 2 -- Krein/PT specialist: where positivity enters, and what would falsify grading stability

The Krein grading enters the truncation at exactly one place: the **spin-2 TT block's pole structure**.
The positivity-defining grading `eta_+` degenerates precisely on the exceptional locus `m2^2 = 0`
(branch-E's Jordan collision; W52/W53), so the truncation-level proxy for "grading intact" is
`d_locus = m2^2 / (fixed scale)^2 > 0`. Loop positivity itself does NOT enter this truncation -- and
saying so is load-bearing: by the W48 gate, flow-side evidence (this file) is *necessary context but
insufficient* for H59. What this truncation CAN see is whether the flow ever drives the grading through
its degeneration point, which is the prerequisite question.

**Falsifiers of grading stability, stated in advance and checked:**
1. A regulator in the admissible families for which `f_2^2(k)` hits 0 at finite `k` (finite-scale locus
   crossing). CHECKED: impossible -- `beta_{f_2^2} = -kappa Phi_2 b_2 f_2^4` with `Phi_2 > 0` (threshold
   positivity, sympy identity) and `b_2 > 0` gives the exact solution
   `1/f_2^2(t) = 1/f_2^2(0) + kappa Phi_2 b_2 t`, strictly positive at every finite `t`. Verified RK4 vs
   analytic at both band extremes (rel. err ~1e-14). NOT falsified.
2. A dressed fixed-ratio root turning positive (which would change which trajectory is UV-complete and
   re-pose the grading question on a different trajectory). CHECKED: impossible for any positive
   dressing (Section 3). NOT falsified.
3. A hidden interacting FP in the marginal sector at which the grading sits at or past the locus.
   CHECKED: the truncation's FP set is exhaustively enumerable; no such FP exists (Section 5).
   NOT falsified.

So within this truncation, grading RG-stability at all finite scales is not merely observed -- it is
*forced* by threshold positivity plus the sign of `b_2`. The only remaining soft spot is the UV endpoint
itself, and that is exactly where the two named forks (ghost-mass branch, eta_C scheme) live.

## 3. Persona 3 -- higher-derivative gravity expert: against known 4th-order results; the fork carried

**Check against Stelle/agravity/FT-AB.** At the Gaussian point the dressed system reduces to the known
one-loop 4th-order results by universality: `b_2 = 133/10 + matter` (Fradkin-Tseytlin;
Avramidi-Barvinsky; Salvio-Strumia), and the fixed-ratio quadratic
`(5/6) r^2 + (5 + b_2) r + 5/3 = 0` reproduces W46's roots `r* = -0.0848, -23.575` (positive control
PC3, matched to 2e-4). The FRG adds two things the one-loop picture cannot have: threshold dressing
along the flow, and canonical linear terms for `(g, lambda)`. The first is shown harmless to all three
H59 ingredients; the second produces the Reuter FP -- consistent with Codello-Percacci (2006),
Benedetti-Machado-Saueressig (2009), Ohta-Percacci (2014), where the Weyl coupling remains
asymptotically free alongside the non-Gaussian EH-sector FP. Nothing found here contradicts the known
4th-order literature; the truncation reproduces its structure.

**The ghost-mass construction fork, computed on both branches (cheap, so both were computed):**
- **Branch A (agravity `m2^2 = (1/2) f_2^2 M_Pl^2`).** `d_locus = (1/2) f_2^2(k)`: strictly positive at
  every finite scale for every admissible regulator (both dressing extremes integrated), monotonically
  -> 0. The grading pinches onto the locus ONLY at the free UV endpoint. W53's BOUNDARY verdict
  survives FRG dressing unchanged.
- **Branch B (fixed-scale `m2 = sqrt(m2_eff) mu_DW`).** `d_locus = m2_eff in [5/6, 5/4]`:
  scale-INDEPENDENT and strictly positive at every scale INCLUDING the endpoint. STAYS-CLEAR, no pinch.
- **Branch dependence, isolated:** the fork decides ONLY the UV-endpoint behavior (BOUNDARY vs
  STAYS-CLEAR). At all finite scales the two branches agree: grading stable. The fork is carried open,
  per the construction-fork discipline -- and note it interacts with W89's eta_C scheme fork: on the
  EH-adapted scheme (HORN-Q side) the lifted root `f_2^2* in [0.07, 0.16]` bounds even branch A away
  from the locus at the endpoint (`d_locus(UV) in [0.034, 0.076] > 0`). So THREE of the four
  fork-branch combinations end clear of the locus; only (agravity mass) x (Weyl-adapted scheme) pinches,
  and that pinch is at the free point where the ghost decouples.

## 4. Persona 4 -- numerical/symbolic engineer: the reproducible system

`tests/W119_h59_frg_krein_negative_ratio.py`, 17/17 checks, exit 0. Structure:

- **Controls.** PC1: Litim `Phi^p_n(0) = 1/n!` by quadrature (4 cases, 1e-5). PC2: exponential
  `Phi^2_2(0) = 1`, `Phi^1_1(0) = pi^2/6` -- analytic reduction vs quadrature. PC3: universal limit
  reproduces W46's roots. PC4: schematic EH sector reproduces W83/W88's Reuter calibration (pure
  gravity `g* = 0.700`, `g* lambda* = 0.109`; GU content `g* = 0.674`). NC1 (negative control):
  `c_RS_weyl = -20` flips `b_2 < 0` and the machinery DETECTS AF breakage -- the passes are not vacuous.
- **Two independent routes for every load-bearing number.** Thresholds: quadrature vs closed
  form/analytic reduction. Dressed ratio roots: numpy companion matrix vs explicit quadratic formula
  (agree to 1.4e-14 over the whole 5^4 grid). Dressed AF flow: RK4 (4e5 steps to t=4000) vs the exact
  `1/f_2^2` linear law (agree to ~1e-14).
- **The dressed-ratio sweep (the load-bearing new computation).** All four dressing factors swept
  independently over the computed band `[0.50, 2.47]` (5^4 grid): every combination gives two real,
  strictly negative roots; minimum discriminant on the grid 63.4 (at the adversarial corner
  `Phi_A = Phi_C = 2.47, Phi_B = Phi_2 = 0.50`); minimum coefficient 0.417 > 0.
- **The margin, quantified.** Losing realness needs `(Phi_A Phi_C)/(Phi_mid^2) >= F_break =
  (5+b_2)^2 / (4 (5/6)(5/3)) = 70.0`. The over-wide band supplies at most `(2.47/0.50)^2 = 24.4`.
  Margin 2.9x on the deliberately worst-case reading; the realistic band (p=2 integrals only, per W89:
  `[0.5, 1.12]`) supplies 5.0, margin 14x.

## 5. Persona 5 -- adversarial skeptic: trying to break AF

**Attack 1: "the one-loop no-interacting-FP theorem (H60) is an artifact -- beyond one loop a
non-Gaussian FP appears and kills the AF story."** PARTLY LANDS, in the already-catalogued way. The
canonical linear terms destroy homogeneity (`beta(lam g) != lam^2 beta(g)`, residual 0.72 -- computed),
so H60's uniqueness theorem is one-loop-specific, and the Reuter FP appears. But this is the KNOWN break
(W83/W88), and it does not kill AF: `f_2^2* = 0` remains a structural root (both terms of
`beta_{f_2^2}` vanish there) and `f_2^2` remains the marginally-irrelevant direction at the Reuter FP
(BMS 3+1). The skeptic's hunt for a THIRD mechanism fails: in this truncation the FP set is exhaustively
enumerable (`beta_g = 2g - A g^2` has exactly the roots `{0, 2/A}`; `lambda` solves linearly; the
marginal block's roots are those of quadratics), and a 300-seed multistart Newton in 4D converges 300/300
times onto the enumerated set -- zero roots outside it.

**Attack 2: "the negative fixed-ratio is a scheme accident -- some admissible regulator flips it."**
FAILS, structurally. By Vieta, the dressed quadratic's root product `Phi_A c_A / (Phi_C c_C) > 0` and
root sum `-(Phi_B c_B + Phi_2 b_2)/(Phi_C c_C) < 0` for ANY positive dressing -- and threshold
positivity is an identity (`r - y r' = s y^2 e^y/(e^y-1)^2 > 0`), not an observation. A sign flip is
impossible; the only escape is losing realness, and that needs a 70x asymmetry the band cannot supply.

**Attack 3: "the grading result is rigged by the ghost-mass convention."** ANSWERED by carrying the
fork: both branches computed, the branch dependence isolated to the UV endpoint, neither defaulted
(Section 3). The finite-scale stability statement is branch-INDEPENDENT.

**Attack 4: "this is a truncation, not a proof -- and the dressing-assignment was never derived."**
CONCEDED, loudly. The exact `Phi`-to-coefficient assignment is a paper-scale Hessian computation not
done here; the conclusions are those robust to sweeping it over an over-wide band. The EH magnitudes are
schematic (W83 calibration, reproduced as a control). Beyond-`R^2` invariants, full functional `f(R)`,
and genuine loop positivity are all outside this truncation. Grade: DERIVED-on-PORTED, no better.

**Honest grade of the verdict.** SURVIVES is asserted at the level of: structural sign arguments +
computed band sweeps within THIS truncation, calibrated by controls that reproduce known FRG results.
It is not a proof of AF beyond one loop; it is the statement that the minimal FRG truncation gives NO
sign of the one-loop picture breaking, and quantifies how far the admissible regulator freedom sits from
the nearest breaking point (2.9x-14x).

## 6. Verdict

**SURVIVES-WITH-ONE-CATALOGUED-BREAK.**

| One-loop ingredient | FRG-truncation fate |
|---|---|
| Gaussian UV FP / AF trajectory | **SURVIVES** (structural root; marginally irrelevant at both FPs) |
| Negative fixed-ratio `r* < 0` (both roots) | **SURVIVES** at every admissible regulator (Vieta + threshold positivity; worst-case discriminant 63.4 > 0; margin 2.9x-14x from breaking) |
| Spin-2 grading RG-stability (finite scales) | **SURVIVES** on both ghost-mass fork branches |
| Grading at the UV endpoint | **FORK-DEPENDENT** (agravity: pinch/BOUNDARY; fixed-scale: STAYS-CLEAR; EH-adapted eta_C lifts even agravity clear) -- carried open |
| UNIQUENESS of the Gaussian FP | **BREAKS** -- Reuter FP appears (canonical terms); already catalogued (W83/W88), no new ambiguity, no hidden third FP |
| Spin-0 conformal-mode sign | **UNCHANGED** -- `M_0^2 < 0` on the AF trajectory for every admissible dressing; W78's physical-vs-gauge question remains THE open item |

**Not AMBIGUOUS.** The blind-branch trigger ("the truncation is ambiguous, here is where") is NOT
pulled: within this truncation every H59-relevant readout is either robust (ratio sign, finite-scale
grading stability, FP enumeration) or resolves into an ALREADY-NAMED open fork (ghost-mass branch,
eta_C Z_h scheme, spin-0 gauge status) rather than a new ambiguity.

**What this leaves for H59.** Unchanged in kind, sharpened in confidence: the state-space side (loop
positivity at the negative ratio, per the W48 packet) is still the missing piece; the flow side now
holds at FRG-truncation level, not just one loop. The single highest-value next swings remain
(1) the W48 minimal source-action loop computation at the negative ratio, and (2) settling the spin-0
physical-vs-gauge status (W78) -- both state-space, neither a flow calculation.

## What this does NOT do

No loop amplitude computed; no positivity claim (W48 gate respected). No exact threshold-to-coefficient
Hessian projection (named, swept instead). No resolution of the ghost-mass fork or the eta_C scheme fork
(carried). No canon / RESEARCH-STATUS / claim-status / verdict / posture change. H59 remains **OPEN**.
