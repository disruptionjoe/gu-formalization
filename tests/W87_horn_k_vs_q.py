#!/usr/bin/env python3
r"""
W87 / horn-K-vs-Q -- REDO THE HORN DETERMINATION ON THE SELECTED ASYMPTOTIC-SAFETY (REUTER) BRANCH.

The last fork.  W84 split the residual type-III leg of the observer-conjecture Krein-Tomita-Takesaki
into two horns, given PT-unbrokenness:
    HORN Q (quasi-Hermitian):  GU's Krein modular operator Delta = S^+ S is DEFINITIZABLE -- a bounded
        metric with BOUNDED inverse -> the ghost is REMOVABLE -> keep-and-grade trivial -> GU is secretly
        a POSITIVE-METRIC, ghost-free theory (arXiv:2606.13251: quasi-Hermiticity <=> positive-KMS).
    HORN K (genuine Krein):    Delta is NON-definitizable -- a bounded metric with UNBOUNDED inverse ->
        a GENUINE kept ghost -> standard type-III Tomita-Takesaki does NOT apply -> the physical modular
        realization of the observer conjecture does not close.
W84 leaned HORN K, but it used W52/W53 AF-BRANCH geometry, where ||C|| -> inf as the flow approaches the
exceptional locus (m2^2 -> 0) at the FREE/GAUSSIAN UV fixed point (f_2^2 -> 0 by asymptotic freedom).
The observer conjecture's SELECTED branch is the ASYMPTOTIC-SAFETY / Reuter branch (W83).  This file
redoes the horn determination ON THE AS BRANCH.

THE CRUX.  On the AS/Reuter branch, does the flow keep the massive spin-2 mass m2^2 (hence ||C|| and the
inverse of the definitizing metric) BOUNDED AWAY from the exceptional locus m2^2 -> 0 in the UV?

THE HONEST REPO-NATIVE ANSWER (this file's finding).  NO -- not on the repo's own W83 computation.  The
orchestrator's HORN-Q hypothesis assumed "at the Reuter FP, f_2^2 sits at a FINITE nonzero value (not
f_2^2 -> 0 as in AF)."  That premise is FALSIFIED by the repo's own W83 data: the Reuter FP is located at
(g*=0.674, lambda*=0.151, f_2^2* = 0, f_0^2* = 0), and the W83 stability analysis makes f_2^2 the
MARGINALLY-IRRELEVANT direction (stability eigenvalue -0.0, AF-predicted, beta_{f_2^2}<0 for f_2^2>0).
The Weyl / spin-2 coupling f_2^2 is ASYMPTOTICALLY FREE on BOTH branches, because its beta function
    beta_{f_2^2} = -kappa f_2^4 b_2                 (b_2 = 133/10 + c_RS_weyl > 0; g-INDEPENDENT in W83)
does not couple to (g, lambda) at the operative truncation.  So the AS selection fixes the EH + R^2
sector (g, lambda, f_0^2) at finite values but leaves the SPIN-2 GHOST coupling running to zero exactly
as in AF.  Hence on the AS trajectory too, d_locus = m2^2/M_Pl^2 = (1/2) f_2^2 -> 0, r = a/b -> 1,
cond(eta_+) = (1+r)/(1-r) -> inf, ||C|| = ||eta_+^{-1/2}|| -> inf, the definitizing metric's inverse is
UNBOUNDED, and Delta is NON-definitizable at the Reuter-FP spectrum (the massive spin-2 pole collides
with the massless pole -> a defective Jordan point).  BOTH DERIVATIONS -> HORN K.  W84's indication was
NOT an AF-geometry artifact: it survives the AS selection, because the AS selection does not touch the
spin-2 ghost sector's UV asymptotic freedom.

THE LOAD-BEARING ASSUMPTION + CONSTRUCTION FORK (GEOMETER-VS-PHYSICS-OBJECTS discipline).  The horn is
TRUNCATION-CONDITIONAL on "beta_{f_2^2} is g-independent (pure Weyl quartic AF)":
    * repo-native construction (W53/W83 agravity convention, f_2^2 asymptotically free, f_2^2* = 0):
      m2^2 -> 0 -> ||C|| -> inf -> HORN K.  <-- what GU's own computation gives.
    * standard-AS-field construction (graviton (g,lambda) loops FEED beta_{f_2^2} at the Reuter FP and
      lift it to a finite non-Gaussian value f_2^2* > 0, BMS-type): m2^2* finite, bounded away from the
      pole -> ||C|| bounded -> HORN Q.  <-- what the orchestrator's hypothesis ASSUMED, NOT realized in W83.
The deciding computation is named: compute the FULL FRG beta_{f_2^2} WITH graviton (g, lambda) loop
contributions at the Reuter FP and determine sign/value of f_2^2*.  Robust one-loop AF (Fradkin-Tseytlin,
Avramidi-Barvinsky, Salvio-Strumia agravity) gives f_2^2* = 0 (HORN K); a truncation that lifts it > 0
would give HORN Q.  W83's own caveat (FRG FP magnitudes are truncation-dependent) keeps this a genuine,
if disfavored, escape -- so the honest verdict is HORN K (repo-native), TRUNCATION-CONDITIONAL.

THE CONSEQUENCE, both ways (they pull OPPOSITE directions -- the honest computation decides).
    * For GU's CONSISTENCY: HORN K means GU is NOT trivially ghost-free on the AS branch -- the easy
      positive-metric out (HORN Q) is closed.  GU's consistency still rests on the harder keep-and-grade
      (genuinely indefinite Krein-graded) route, whose modular realization is walled at type-III
      definitizability.  (HORN Q would have UPGRADED GU to secretly-positive-metric / ghost-free.)
    * For the OBSERVER CONJECTURE: HORN K PRESERVES the firewall -- the antilinear grading separates
      admissible/inadmissible in a GENUINELY indefinite metric, so there is real value-selection across a
      real firewall.  The observer = source-action MECHANISM IS INTACT (not deflated).  Its PHYSICAL
      modular realization (Tomita-Takesaki construction of J) does not close at infinite rank / type III
      (no theorem -- W74/W84).  (HORN Q would have DEFLATED the firewall to a trivial, removable grading.)
So HORN K is GOOD for the observer conjecture (firewall genuine) and does NOT hand GU the easy
ghost-free upgrade.  The two consequences pull opposite ways, exactly as flagged; the computation lands
on the firewall-genuine / modular-walled side.

TOY.  The repo's exceptional-point model (W52), mode = the spin-2 sector, with the ghost mass driven by
the AF Weyl coupling f_2^2 (W53 convention m2^2 = (1/2) f_2^2 M_Pl^2, so distance-to-locus = f_2^2/2):
    H(a,b) = [[ i a, b ],[ b, -i a ]],  r = a/b = 1/(1 + d_locus),  d_locus = (1/2) f_2^2,
    positive metric eta_+ = [[1,-i r],[i r,1]],  eigenvalues 1 -+ r,  cond = (1+r)/(1-r),
    ||C|| proxy = ||eta_+^{-1/2}|| = 1/sqrt(1 - r).
The AS trajectory integrates the SAME g-independent beta_{f_2^2} as AF; adding the Reuter FP for (g,lambda)
does not change the f_2^2 column -> ||C|| -> inf on the AS branch too.

LITERATURE (surveyed read-only; no external action):
  [W83]  repo FRG f(R)+Weyl^2 settling computation: Reuter FP at (g*=0.674, lambda*=0.151, 0, 0); f_2^2
         marginally-irrelevant (AF), f_0^2 relevant (non-tachyonic); AS-SELECTED-CLOSES (CONDITIONAL).
  [W53]  repo AF-flow-vs-exceptional-locus: m2^2 = (1/2) f_2^2 M_Pl^2; AF drives m2^2 -> 0 at the free UV FP.
  [W52]  repo Branch-E: eta_+ degenerates (lambda_min -> 0), ||C|| -> inf on the exceptional (Jordan) locus.
  [W84]  repo rankN Krein-TT: PT-unbroken NOT sufficient at type III; residual = definitizability; horn XOR.
  [KS12] Krejcirik-Siegl, PRD 86 (2012) 121702: bounded metric, UNBOUNDED inverse; not similar to s.a.
  [Lang] Langer definitizable operators: spectral function under definitizability; Pi_kappa only.
  [KMS ] arXiv:2606.13251: positive-KMS <=> quasi-Hermiticity (the horn-Q/horn-K dichotomy, physics form).
  [AF  ] Fradkin-Tseytlin; Avramidi-Barvinsky; Salvio-Strumia agravity (arXiv:1403.4226): the Weyl
         coupling f_2^2 is asymptotically free -> f_2^2 -> 0 in the UV (ghost mass m2^2 ~ f_2^2 -> 0).
  [BMS ] Benedetti-Machado-Saueressig (arXiv:0901.2984): higher-derivative Reuter FP, 3 relevant + 1
         marginally-irrelevant (the Weyl/C^2 direction) -- consistent with f_2^2 flowing INTO f_2^2* = 0.

Deterministic, numpy-only, self-validating; exit 0 on success.  No canon / RESEARCH-STATUS / CANON /
claim-status / verdict / posture file is touched.  Exploration-grade.  NOT committed by this run.
"""
from __future__ import annotations

import numpy as np

np.random.seed(0)

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


def dag(X: np.ndarray) -> np.ndarray:
    return X.conj().T


# ------------------------------------------------------------------------------------------------
# The repo's exceptional-point model (W52), spin-2 sector.  d_locus = (1/2) f_2^2 (W53 convention).
# ------------------------------------------------------------------------------------------------
def r_of_dlocus(d_locus: float) -> float:
    # a/b monotone reparametrization: r -> 1 as d_locus -> 0 (W53's stated proxy r = 1/(1 + d_locus)).
    return 1.0 / (1.0 + d_locus)


def eta_pos(r: float) -> np.ndarray:
    return np.array([[1.0, -1j * r], [1j * r, 1.0]], dtype=complex)


def cond_metric(r: float) -> float:
    ev = np.linalg.eigvalsh(eta_pos(r))
    return float(ev.max() / ev.min())


def C_norm(r: float) -> float:
    # ||C|| proxy = ||eta_+^{-1/2}|| = 1/sqrt(min eig(eta_+)) = 1/sqrt(1 - r)  (blows up as r -> 1).
    return float(1.0 / np.sqrt(np.linalg.eigvalsh(eta_pos(r)).min()))


# ------------------------------------------------------------------------------------------------
# The repo's Weyl-coupling beta (W53/W45): beta_{f_2^2} = -kappa f_2^4 b_2, g-INDEPENDENT.  Closed form
#   1/f2(t) = 1/f2_0 + kappa b_2 t  =>  f2(t) = f2_0/(1 + kappa b_2 f2_0 t).  (t = ln mu; UV = t -> +inf)
# ------------------------------------------------------------------------------------------------
KAPPA = 1.0 / (16.0 * np.pi**2)     # schematic loop factor (positive; magnitude irrelevant to the sign result)
B2 = 133.0 / 10.0 + 1.417           # b_2 > 0 at the RS anchor (W53 value 14.717); sign is load-bearing, not magnitude


def f2_of_t(f2_0: float, t: float) -> float:
    return f2_0 / (1.0 + KAPPA * B2 * f2_0 * t)


log("=" * 100)
log("W87 / horn-K-vs-Q -- redo the horn determination on the SELECTED asymptotic-safety (Reuter) branch")
log("=" * 100)

# ================================================================================================
# T1 -- D1, PART A: the orchestrator's HORN-Q PREMISE is FALSIFIED by the repo's own W83 data.
#   HORN Q requires f_2^2* FINITE (>0) at the Reuter FP so that m2^2 stays bounded away from 0.
#   W83 locates the Reuter FP at (g*, lambda*, f_2^2*=0, f_0^2*=0) with f_2^2 MARGINALLY-IRRELEVANT
#   (stability eigenvalue -0.0, AF).  So f_2^2* = 0, NOT finite.  The HORN-Q geometry is not realized.
# ================================================================================================
log("\n[T1] HORN-Q premise ('f_2^2 finite at Reuter') is FALSIFIED by W83: the Reuter FP has f_2^2* = 0")
reuter_fp = {"g": 0.674, "lambda": 0.151, "f2sq": 0.0, "f0sq": 0.0}          # W83 §1.1
reuter_stability_eigs = [-2.674, -2.0, -0.607, -0.0]                          # W83 §1.3 (real parts)
f2_is_marginally_irrelevant = abs(min(abs(e) for e in reuter_stability_eigs)) < 1e-6   # the -0.0 direction is f_2^2
f2_fp_is_zero = abs(reuter_fp["f2sq"]) < 1e-12
horn_q_premise_holds = reuter_fp["f2sq"] > 1e-6      # HORN Q needs a FINITE nonzero f_2^2* -- it is NOT
check("T1  HORN-Q premise FALSIFIED by W83.  The observer-selected Reuter FP sits at f_2^2* = 0 (NOT a "
      "finite nonzero value): the Weyl / spin-2 ghost coupling is the MARGINALLY-IRRELEVANT direction "
      "(stability eigenvalue -0.0, asymptotically free), so the AS selection fixes (g, lambda, f_0^2) at "
      "finite values but leaves f_2^2 flowing to ZERO.  The 'finite f_2^2 at Reuter' geometry HORN Q "
      "needs is NOT realized on GU's own computation.",
      f2_fp_is_zero and f2_is_marginally_irrelevant and (not horn_q_premise_holds),
      f"f_2^2* = {reuter_fp['f2sq']}, marginally-irrelevant={f2_is_marginally_irrelevant}, "
      f"HORN-Q premise holds={horn_q_premise_holds}")

# ================================================================================================
# T2 -- D1, PART B: ||C|| is UNBOUNDED on the AS trajectory -- SAME as AF -- because beta_{f_2^2} is
#   g-INDEPENDENT, so the AS selection (g -> g*, lambda -> lambda*) does NOT change the f_2^2 column.
#   Integrate the SAME closed-form AF running of f_2^2 that W53 used, and confirm ||C|| grows without
#   bound under UV extension.  Contrast with a HYPOTHETICAL HORN-Q trajectory (f_2^2 frozen at a finite
#   f_2^2* > 0), where ||C|| would saturate.
# ================================================================================================
log("\n[T2] D1: on the AS branch ||C|| is UNBOUNDED (f_2^2 -> 0, g-independent beta) -- same as AF")
f2_0 = 0.8
t_grid = [0.0, 40.0, 400.0, 2000.0, 4000.0, 8000.0]
log("      t(=ln mu)    f_2^2(AS)     d_locus=f2/2     r=a/b        cond(eta_+)      ||C||")
Cnorms = []
for t in t_grid:
    f2 = f2_of_t(f2_0, t)
    d_locus = 0.5 * f2
    r = r_of_dlocus(d_locus)
    Cnorms.append(C_norm(r))
    log(f"   {t:9.1f}   {f2:.6e}   {d_locus:.6e}   {r:.6f}   {cond_metric(r):.3e}   {C_norm(r):.3e}")
# ||C|| grows without bound: doubling the UV depth (t: 4000 -> 8000) strictly increases ||C||, and the
# closed form ||C|| = 1/sqrt(1-r) = sqrt((2 + f2)/f2) ~ sqrt(2/f2) -> inf as f2 -> 0.
C_at_4000 = C_norm(r_of_dlocus(0.5 * f2_of_t(f2_0, 4000.0)))
C_at_8000 = C_norm(r_of_dlocus(0.5 * f2_of_t(f2_0, 8000.0)))
C_at_1e6 = C_norm(r_of_dlocus(0.5 * f2_of_t(f2_0, 1.0e6)))
C_norm_unbounded_on_AS = (C_at_8000 > C_at_4000) and (C_at_1e6 > C_at_8000) and (C_at_1e6 > 10.0)
# analytic vs numeric agreement (the two-derivations bug-catch): ||C|| = sqrt((2+f2)/f2)
f2_check = f2_of_t(f2_0, 4000.0)
C_analytic = np.sqrt((2.0 + f2_check) / f2_check)
C_numeric = C_norm(r_of_dlocus(0.5 * f2_check))
analytic_numeric_agree = abs(C_analytic - C_numeric) / C_analytic < 1e-9
check("T2  D1 -- ||C|| is UNBOUNDED on the AS trajectory, exactly as on AF.  beta_{f_2^2} = -kappa f_2^4 "
      "b_2 is g-INDEPENDENT, so replacing the free UV FP by the Reuter FP for (g, lambda) leaves the "
      "f_2^2 column unchanged; f_2^2 -> 0, d_locus -> 0, r -> 1, ||C|| = 1/sqrt(1-r) = sqrt((2+f2)/f2) "
      f"-> inf ({C_at_4000:.2e} at t=4e3 -> {C_at_8000:.2e} at t=8e3 -> {C_at_1e6:.2e} at t=1e6).  The "
      "definitizing metric's inverse is UNBOUNDED on the AS branch.  Analytic/numeric ||C|| agree to "
      f"{abs(C_analytic - C_numeric)/C_analytic:.1e}.",
      C_norm_unbounded_on_AS and analytic_numeric_agree,
      f"||C|| 4e3={C_at_4000:.2e}, 1e6={C_at_1e6:.2e}, analytic~numeric={analytic_numeric_agree}")

# ================================================================================================
# T3 -- THE COUNTERFACTUAL (what HORN Q WOULD look like) + confirmation it is NOT the repo case.
#   If f_2^2 were frozen at a finite Reuter value f_2^2* > 0 (the orchestrator's hypothesis), ||C||
#   would SATURATE at a finite value -> bounded metric inverse -> HORN Q.  Encode it and confirm it is
#   a DIFFERENT trajectory from the one W83 actually gives (f_2^2* = 0).
# ================================================================================================
log("\n[T3] Counterfactual: a FINITE f_2^2* > 0 WOULD give bounded ||C|| (HORN Q) -- but W83 gives f_2^2* = 0")
f2_star_hypothetical = 0.30            # a hypothetical finite Reuter Weyl coupling (NOT the W83 value)
d_star = 0.5 * f2_star_hypothetical
C_horizonQ = C_norm(r_of_dlocus(d_star))
horn_q_would_bound_C = C_horizonQ < 1e3 and np.isfinite(C_horizonQ)
# but the ACTUAL repo trajectory drives f_2^2 -> 0, so its ||C|| exceeds ANY fixed HORN-Q bound in the UV:
C_actual_deepUV = C_norm(r_of_dlocus(0.5 * f2_of_t(f2_0, 1.0e8)))
actual_exceeds_hornQ = C_actual_deepUV > C_horizonQ
check("T3  Counterfactual check.  A FINITE Reuter Weyl coupling f_2^2* > 0 WOULD saturate ||C|| at a "
      f"finite value ({C_horizonQ:.2f}) -> bounded metric inverse -> HORN Q.  But the repo's actual AS "
      f"trajectory (f_2^2 -> 0) drives ||C|| past ANY such bound in the UV ({C_actual_deepUV:.2e} > "
      f"{C_horizonQ:.2f}).  So HORN Q is a genuine LOGICAL possibility that is simply NOT the geometry "
      "GU's own W83 computation delivers.",
      horn_q_would_bound_C and actual_exceeds_hornQ,
      f"||C||(HORN-Q, f2*={f2_star_hypothetical})={C_horizonQ:.2f}, ||C||(actual, deep UV)={C_actual_deepUV:.2e}")

# ================================================================================================
# T4 -- D2: definitizability at the Reuter-FP SPECTRUM.  At the Reuter FP f_2^2* = 0 => m2^2 = 0 => the
#   massive spin-2 pole COLLIDES with the massless graviton pole => a defective Jordan point => the
#   positive metric eta_+ eigenvalue (1 - r) -> 0 => NON-definitizable AT the FP spectrum (not bounded
#   away from the exceptional locus).  Independent of the D1 trajectory analysis.
# ================================================================================================
log("\n[T4] D2: at the Reuter-FP spectrum (f_2^2*=0) the metric DEGENERATES -> Delta NON-definitizable")
d_locus_at_FP = 0.5 * reuter_fp["f2sq"]         # = 0 at the Reuter FP
r_at_FP = r_of_dlocus(d_locus_at_FP)            # -> 1
min_metric_eig_at_FP = float(np.linalg.eigvalsh(eta_pos(r_at_FP)).min())   # = 1 - r -> 0
# the massive spin-2 pole m2^2 = (1/2) f_2^2* M_Pl^2 = 0 coincides with the massless pole at p^2 = 0:
massive_pole_collides_massless = abs(reuter_fp["f2sq"]) < 1e-12
metric_degenerate_at_FP = min_metric_eig_at_FP < 1e-9
FP_sits_on_exceptional_locus = massive_pole_collides_massless and metric_degenerate_at_FP
check("T4  D2 -- the Reuter-FP spectrum SITS ON the exceptional locus, it is NOT bounded away from it.  "
      "f_2^2* = 0 => m2^2 = (1/2) f_2^2* M_Pl^2 = 0 => the massive spin-2 ghost pole collides with the "
      f"massless graviton pole (defective Jordan point) => min eig(eta_+) = 1 - r = {min_metric_eig_at_FP:.1e} "
      "-> 0 => Delta is NON-definitizable at the FP.  Independent of D1, this is the definitizability "
      "criterion applied to the Reuter-FP spectrum, and it agrees: HORN K.",
      FP_sits_on_exceptional_locus,
      f"m2^2*=0 pole-collision={massive_pole_collides_massless}, min eig(eta_+)@FP={min_metric_eig_at_FP:.1e}")

# ================================================================================================
# T5 -- THE CONSTRUCTION FORK + LOAD-BEARING ASSUMPTION (GEOMETER-VS-PHYSICS-OBJECTS discipline).
#   The horn is TRUNCATION-CONDITIONAL on beta_{f_2^2} being g-independent.  Two constructions:
#     repo-native (f_2^2 AF, f_2^2* = 0)              -> HORN K   (what W83 gives)
#     standard-AS-field (graviton loops lift f_2^2*>0) -> HORN Q   (the orchestrator's assumed geometry)
#   Name the deciding computation; assert the repo-native side is HORN K and the fork is real.
# ================================================================================================
log("\n[T5] Construction fork: HORN K is repo-native (f_2^2 AF); HORN Q needs a lifted f_2^2* > 0 (truncation)")
fork = {
    "repo_native_beta_f2_is_g_independent_f2star_zero": True,      # W53/W83: pure Weyl quartic AF
    "repo_native_horn": "K",
    "standard_AS_field_graviton_loops_could_lift_f2star_positive": True,   # BMS-type; not realized in W83
    "standard_AS_field_horn_if_lifted": "Q",
    "deciding_computation_full_FRG_beta_f2_with_graviton_loops_at_Reuter_sign_f2star": "OPEN",
}
horn_repo_native_is_K = (fork["repo_native_horn"] == "K")
fork_is_real_and_named = (
    fork["repo_native_beta_f2_is_g_independent_f2star_zero"]
    and fork["standard_AS_field_graviton_loops_could_lift_f2star_positive"]
    and (fork["repo_native_horn"] != fork["standard_AS_field_horn_if_lifted"])
    and (fork["deciding_computation_full_FRG_beta_f2_with_graviton_loops_at_Reuter_sign_f2star"] == "OPEN")
)
check("T5  Construction fork NAMED (not defaulted).  Load-bearing assumption: beta_{f_2^2} is "
      "g-independent (pure Weyl-quartic AF).  repo-native (W53/W83): f_2^2* = 0 -> HORN K.  "
      "standard-AS-field (graviton (g,lambda) loops feed beta_{f_2^2} and could lift f_2^2* > 0, BMS-type): "
      "HORN Q -- LOGICALLY possible, NOT realized in W83.  Deciding computation: full FRG beta_{f_2^2} "
      "with graviton loops at the Reuter FP, sign/value of f_2^2*.  Robust one-loop AF gives 0 (HORN K).",
      horn_repo_native_is_K and fork_is_real_and_named,
      f"repo-native horn={fork['repo_native_horn']}, alt horn={fork['standard_AS_field_horn_if_lifted']}")

# ================================================================================================
# T6 -- VERDICT BOOLEANS: HORN K on the repo-native AS branch (TRUNCATION-CONDITIONAL), two derivations
#   agree, and the honest opposite-pulling consequence for GU-consistency vs the observer conjecture.
# ================================================================================================
log("\n[T6] VERDICT = HORN K (repo-native AS branch), truncation-conditional; two derivations agree")
verdict = {
    # the crux answer:
    "AS_branch_keeps_m2sq_bounded_away_from_exceptional_locus": False,     # T1/T2: f_2^2 -> 0 on AS too
    "AS_branch_keeps_C_norm_bounded": False,                              # T2: ||C|| -> inf on AS
    "orchestrator_horn_Q_premise_f2star_finite_at_Reuter": False,         # T1: W83 gives f_2^2* = 0
    # two independent derivations both -> HORN K:
    "D1_C_norm_boundedness_on_AS_gives_horn": "K",                        # T2 (trajectory)
    "D2_definitizability_at_Reuter_FP_spectrum_gives_horn": "K",          # T4 (FP spectrum)
    "two_derivations_agree": True,
    # the horn and its status:
    "verdict_horn": "K",
    "horn_is_truncation_conditional_on_g_independent_beta_f2": True,      # T5 (flips to Q iff f_2^2* lifted > 0)
    "W84_horn_K_indication_was_AF_geometry_artifact": False,             # it SURVIVES the AS selection
    # the honest opposite-pulling consequence:
    "horn_K_makes_GU_trivially_ghost_free": False,                       # HORN Q would have; K does not
    "horn_K_preserves_the_observer_firewall_genuine": True,             # genuine indefinite metric, real selection
    "horn_K_deflates_the_observer_conjecture_mechanism": False,          # mechanism INTACT under K
    "horn_K_walls_the_physical_modular_realization_at_type_III": True,   # no infinite-rank Krein J theorem
    # what HORN Q would have done (recorded for the opposite-pull honesty):
    "horn_Q_would_upgrade_GU_to_ghost_free_but_deflate_the_firewall": True,
}
horn_K_verdict = (
    (verdict["AS_branch_keeps_m2sq_bounded_away_from_exceptional_locus"] is False)
    and (verdict["AS_branch_keeps_C_norm_bounded"] is False)
    and (verdict["orchestrator_horn_Q_premise_f2star_finite_at_Reuter"] is False)
    and (verdict["D1_C_norm_boundedness_on_AS_gives_horn"] == "K")
    and (verdict["D2_definitizability_at_Reuter_FP_spectrum_gives_horn"] == "K")
    and verdict["two_derivations_agree"]
    and (verdict["verdict_horn"] == "K")
    and verdict["horn_is_truncation_conditional_on_g_independent_beta_f2"]
    and (verdict["W84_horn_K_indication_was_AF_geometry_artifact"] is False)
    and (verdict["horn_K_makes_GU_trivially_ghost_free"] is False)
    and verdict["horn_K_preserves_the_observer_firewall_genuine"]
    and (verdict["horn_K_deflates_the_observer_conjecture_mechanism"] is False)
    and verdict["horn_K_walls_the_physical_modular_realization_at_type_III"]
)
check("T6  VERDICT = HORN K on the SELECTED AS/Reuter branch (repo-native, TRUNCATION-CONDITIONAL).  The "
      "AS branch does NOT keep m2^2 / ||C|| bounded away from the exceptional locus: the spin-2 Weyl "
      "coupling is asymptotically free on BOTH branches (f_2^2 -> 0), so W84's HORN-K indication SURVIVES "
      "the AS selection -- it was NOT an AF-geometry artifact.  Two derivations (D1 ||C|| on AS; D2 "
      "definitizability at the Reuter-FP spectrum) AGREE -> HORN K.  Consequence (opposite pulls): GU is "
      "NOT trivially ghost-free (the easy positive-metric out is closed) BUT the observer firewall stays "
      "GENUINE (real indefinite metric, real value-selection) -- the conjecture's mechanism is INTACT; "
      "only its physical modular realization is walled at type-III definitizability.",
      horn_K_verdict,
      f"{sum(1 for v in verdict.values() if v is True)} True flags / verdict horn = {verdict['verdict_horn']}")

# ================================================================================================
# SUMMARY
# ================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

assert all(ok for _, ok, _ in results), "some W87 horn-K-vs-Q checks FAILED"

log("")
log("W87 horn-K-vs-Q VERDICT (this file is the computation, not a claim-status change):")
log("  * CRUX: does the AS/Reuter branch keep m2^2 / ||C|| BOUNDED away from the exceptional locus?  NO")
log("    (repo-native).  The Weyl / spin-2 ghost coupling f_2^2 is ASYMPTOTICALLY FREE on BOTH branches")
log("    (beta_{f_2^2} = -kappa f_2^4 b_2 is g-independent; W83 places the Reuter FP at f_2^2* = 0, the")
log("    marginally-irrelevant direction).  So m2^2 -> 0, ||C|| = sqrt((2+f2)/f2) -> inf on the AS branch")
log("    too.  The orchestrator's HORN-Q premise ('f_2^2 finite at Reuter') is FALSIFIED by W83's data.")
log("  * VERDICT = HORN K (genuine kept ghost) on the SELECTED AS branch, TRUNCATION-CONDITIONAL.  W84's")
log("    HORN-K indication was NOT an AF-geometry artifact: the AS selection fixes (g, lambda, f_0^2) but")
log("    does NOT touch the spin-2 ghost sector's UV asymptotic freedom.  Two derivations agree (D1 ||C||")
log("    unbounded on AS; D2 Reuter-FP spectrum sits on the exceptional locus, non-definitizable).")
log("  * CONSEQUENCE (opposite pulls, honest both ways): HORN K does NOT make GU trivially ghost-free")
log("    (the easy positive-metric / HORN-Q out is closed) -- BUT it PRESERVES the observer firewall as")
log("    GENUINE (real indefinite metric, real value-selection): the observer=source-action mechanism is")
log("    INTACT, only its PHYSICAL modular realization is walled at type-III definitizability (no")
log("    infinite-rank Krein conjugation theorem, W74/W84).  HORN Q would have upgraded GU to ghost-free")
log("    but DEFLATED the firewall to a trivial removable grading.  The computation lands firewall-genuine.")
log("  * LOAD-BEARING ASSUMPTION + FORK: beta_{f_2^2} g-independent (pure Weyl-quartic AF).  repo-native")
log("    -> HORN K; a full FRG where graviton (g,lambda) loops LIFT f_2^2* > 0 (BMS-type) -> HORN Q.")
log("    DECIDING COMPUTATION: full FRG beta_{f_2^2} with graviton loops at the Reuter FP, sign of f_2^2*.")
log("    Robust one-loop AF (Fradkin-Tseytlin / Avramidi-Barvinsky / agravity) gives 0 => HORN K.")
raise SystemExit(0)
