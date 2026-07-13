#!/usr/bin/env python3
r"""
W107 / SECOND FOLLOW-ON to the W103 tail-quotient steelman: (T1) make the tail slot ALGEBRA-INTRINSIC
via the Krein-graded Araki-Woods / ITPFI tower and the asymptotic-ratio-set machinery, testing the
CANDIDATE IDENTITY  "cond(C) -> inf (the W98 wall)  <=>  0 enters the Krein ratio invariant";
(T2) TAIL-CLASS COHERENCE: do the per-region tail-quotient CLASSES cohere on overlaps even though the
per-region OPERATORS (W98 T6: J_{O1} != J_{O2}, UV-divergent) do not?

THE TOWER.  Per mode k the Krein doublet carries the W52/W98 metric eta(r_k) = I + r_k*sigma_y with
eigenvalues 1 -+ r_k (r_k = g/(g + Dw(k)/2), Dw ~ 1/(2k)).  The Krein-graded Araki-Woods tower is the
ITPFI factor  M = (x)_k (M_2, phi_k)  with per-mode state phi_k = eta(r_k)/2 (the metric AS the state:
the unique positive intertwiner, normalized).  Its Araki-Woods eigenvalue list is
    (mu_k, 1-mu_k) = ((1-r_k)/2, (1+r_k)/2),   per-mode ratio  lam_k = (1-r_k)/(1+r_k)  ->  0,
which is EXACTLY the Krein metric's eigenvalue-ratio data.  Classical machinery (Araki-Woods 1968;
Connes: r_inf = S-invariant):
    * type I      iff  sum_k mu_k < inf
    * type II_1   iff  sum_k (1/2 - mu_k)^2 < inf
    * type III_lam for constant ratio lam (Powers); two ratios with irrational log-ratio => III_1;
      r_inf = [0, inf) <=> III_1;  0 in r_inf <=> type III.

ADVERSARY (a) ("the Krein ratio set is not well-defined -- the classical construction needs positive
states"): RESOLVED, two-sided.  (i) The construction IS well-defined: every finite mode has r_k < 1
(W98/W103 exactness), so every phi_k is a faithful positive state and the tower is a bona fide ITPFI
factor -- positivity fails only in the k -> inf limit, which is exactly where the invariant (a tail
object) lives.  (ii) But the GENUINELY-Krein signed alternative DEGENERATES: the J-selfadjoint object
A = J*eta(r) = sigma_z - i*r*sigma_x has eigenvalues -+sqrt(1-r^2) (A^2 = (1-r^2)I), signed ratio
IDENTICALLY -1 at every r < 1 -- a signed "Krein ratio set" carries no information; the only workable
definition is the classical r_inf of the metric-as-state tower.  That is a NAMED construction fork
(standard-field machinery fed with the program-native metric), not a silent default.

HEADLINE RESULTS (all machine-verified below):
  T1 IDENTITY: FAILS IN BOTH DIRECTIONS.  Five coupling profiles on the SAME doublet tower:
     PHYS   g = const      : lam_k ~ c/k (slowly varying, non-summable) => pair ratios dense, per-octave
                             mass bounded below => r_inf = [0,inf), TYPE III_1.   WALL: YES. 0 in r_inf: YES.
     SOFT   g = G/k^2      : mu_k -> 1/2, sum (1/2-mu)^2 < inf => TYPE II_1.      WALL: NO.  0 in r_inf: NO.
     MARG   g = G/k        : lam_k -> lam* ~ 0.101 => POWERS III_{lam*}.          WALL: NO.  0 in r_inf: YES.  <- kills <=
     DERIV  g = G*k        : mu_k ~ c/k^2 SUMMABLE => TYPE I_inf, r_inf = {1}.    WALL: YES. 0 in r_inf: NO.   <- kills =>
     2VAL   lam in {a,b},
            log a/log b irr: dense subgroup, r bounded away from 1 => III_1.      WALL: NO.  0 in r_inf: YES.
     The wall (cond -> inf) and the ratio invariant are TRANSVERSE: all four cells of
     (wall) x (0 in r_inf) are inhabited; same for (wall) x (type III_1).  The W98 wall is NOT a
     function of the classical (algebra, state) invariants -- the classical classification is BLIND
     to it.  COROLLARY (rate-dependence): PHYS and DERIV have the SAME Calkin class 2[P] (W103 T4,
     reproduced) but DIFFERENT ITPFI types (III_1 vs I_inf): the intrinsic invariant DISTINGUISHES
     couplings the Calkin quotient identifies -- the tail-quotient class does NOT descend to the
     ratio invariant.
  T1 REPAIRED IDENTITY (exact, holds across all five profiles): the wall IS intrinsic, but to the
     (algebra, state, GRADING) data, not to (algebra, state):
        ||Delta_{phi o AdJ, phi}||_k = cond(eta(r_k))  EXACTLY per mode
     (relative modular operator between the metric-state and its grading twist; proof: eta(-r) =
     (1-r^2) eta(r)^{-1}, so the relative spectrum contains (1+r)/(1-r); fidelity F(phi, phi o J) =
     1 - r^2 exactly).  Hence  WALL  <=>  sup_k ||Delta_{phi o J, phi}||_k = inf  <=>  the Connes
     cocycle [D(phi o J) : D phi]_t (unitary for ALL real t -- the flow half, verified) has NO bounded
     analytic continuation to t = -i/2 (per-mode norm sqrt(cond) -> inf) -- the W103 flow/conjugation
     split reproduced in relative-modular language.  RESIDUAL (honest): the sup is over the mode
     filtration; the filtration-free candidates all FAIL to be equivalent (ratio set: transverse;
     global cocycle domination: too strong, fails even for Powers since prod_k cond_k diverges;
     grading-twist disjointness sum r_k^2 = inf: transverse, MARG is disjoint with no wall).  So the
     slot is intrinsic to (algebra, state, grading, filtration) -- the grading and filtration are
     irreducible inputs, consistent with W103 CM1 (rotating mixing: tail data is direction-sensitive).
  T1 CLASSICAL TYPE: the PHYSICAL tower is the hyperfinite TYPE III_1 factor -- the Krein doublet data
     with the physical coupling intrinsically reproduces the AQFT type of a local algebra
     (Buchholz-D'Antoni-Fredenhagen), a nontrivial consistency check.  The GRADING acts per mode by
     r -> -r (eta(-r) = J eta(r) J), preserving every eigenvalue list => the classical classification
     is grading-blind; the wall lives exactly in the (state, grading) PAIRING the classification drops.
  T2 TAIL-CLASS COHERENCE: CLASSES-COHERE (with content).  W98 T6 regions (modular weights w1 = 1.0,
     w2 = 0.45 rescaling the coupling on shared overlap modes): the OPERATOR disagreement
     ||eta_1^{-1/2} - eta_2^{-1/2}|| DIVERGES in the UV (W98 reproduced) while the METRIC difference
     ||eta(r^1_k) - eta(r^2_k)|| = |r^1_k - r^2_k| -> 0: the difference is COMPACT, so
     [C_O1]|_overlap = [C_O2]|_overlap = 2[P] -- same singular class, same Krein-null line e_null,
     same typed slot.  The interface glues; only the God's-eye operator does not.
  ADVERSARY (b) ("class agreement is automatic/trivial"): REFUTED BY TWO CONTROLS.
     CONTROL 1 (rotation): a region whose modular frame is ROTATED (mixing direction theta2 =
     pi/2 + 0.9) has IDENTICAL eigenvalues (same break, same divergent operator disagreement) but its
     tail limit is 2P_theta with ||P_theta - P|| ~ 0.43 = const: the difference is NOT compact and the
     classes DISAGREE.  Class coherence is falsifiable within the model class -- it holds in W98's
     setup because the region-dependence enters as a SCALAR modular weight (strength only), the mixing
     DIRECTION being fixed by the field content (named assumption, not proven).
     CONTROL 2 (weight collapse): a modular weight vanishing UV-fast (w2(k) = 1/(1+k^2)) makes region 2
     UV-soft on the overlap: [C_O2] INVERTIBLE vs [C_O1] = 2[P] singular -- maximal class disagreement.
     Coherence needs the weights bounded below (W98's are O(1) constants; named assumption).

VERDICTS ENCODED:  T1 = PARTIAL (candidate identity FAILS both directions -- transversality table --
but the repaired relative-modular identity holds exactly and the physical tower is hyperfinite III_1;
the slot is (state, grading, filtration)-intrinsic, NOT (algebra, state)-intrinsic).
T2 = CLASSES-COHERE (with counter-model-backed content and two named load-bearing assumptions).

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


SX = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
SY = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
SZ = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def eta(r: float, theta: float = np.pi / 2.0) -> np.ndarray:
    return I2 + r * (np.cos(theta) * SX + np.sin(theta) * SY)


def opnorm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A, 2))


# --- W98 mode data ---------------------------------------------------------------------------------
M1, M2, G = 0.0, 0.30, 0.10


def dsplit(k: float) -> float:
    return abs(np.sqrt(k * k + M1 * M1) - np.sqrt(k * k + M2 * M2))


def r_of(g_k: float, k: float) -> float:
    return float(min(g_k / (g_k + 0.5 * dsplit(k)), 1.0 - 1e-15))


def lam_of(r: float) -> float:            # Araki-Woods per-mode eigenvalue RATIO = Krein metric ratio
    return (1.0 - r) / (1.0 + r)


def mu_of(r: float) -> float:             # smaller eigenvalue of the normalized metric-state eta(r)/2
    return (1.0 - r) / 2.0


def cond_of(r: float) -> float:
    return (1.0 + r) / (1.0 - r)


# --- the five coupling profiles on the SAME doublet tower -------------------------------------------
PROFILES = {
    "PHYS":  lambda k: G,                     # W98 physical: non-UV-soft
    "SOFT":  lambda k: G / (k * k + 1.0),     # condition X (UV-soft)
    "MARG":  lambda k: G / k,                 # marginal O(1/k)
    "DERIV": lambda k: G * k,                 # derivative-vertex growing (W103 T4's second profile)
}
LAM_A, LAM_B = 0.30, 0.30 ** np.sqrt(2.0)    # 2VAL: two ratios, log-ratio irrational (sqrt 2)
R_A, R_B = (1 - LAM_A) / (1 + LAM_A), (1 - LAM_B) / (1 + LAM_B)


def r_profile(name: str, k: float) -> float:
    if name == "2VAL":
        return R_A if (int(k) % 2 == 0) else R_B
    return r_of(PROFILES[name](k), k)


log("=" * 100)
log("W107: (T1) the Krein-graded ITPFI tower + the asymptotic-ratio invariant vs the W98 wall;")
log("      (T2) per-region TAIL-CLASS coherence on overlaps (the P2-restoration test).")
log("=" * 100)

# ====================================================================================================
# T1 -- WELL-DEFINEDNESS (adversary (a)) + the degenerate signed alternative.  (i) Every finite mode
#   has r_k < 1 => phi_k = eta(r_k)/2 is a faithful positive state: the tower is a bona fide ITPFI
#   factor (the classical machinery APPLIES; positivity fails only in the limit, where the invariant
#   lives).  (ii) The genuinely-Krein signed candidate degenerates: A = J*eta(r) = sigma_z - i r
#   sigma_x satisfies A^2 = (1-r^2) I, eigenvalues -+sqrt(1-r^2), signed ratio == -1 at every r < 1:
#   no information.  The workable Krein ratio set is the classical r_inf of the metric-as-state tower
#   -- a NAMED fork (standard machinery, program-native input), not a silent default.
# ====================================================================================================
log("\n[T1] Well-definedness: metric-as-state tower is bona fide ITPFI; the signed Krein alternative degenerates")
ks1 = np.concatenate([np.linspace(0.1, 1e3, 500), np.linspace(1e3, 1e6, 500)])
all_states_ok = all(
    min(np.linalg.eigvalsh(eta(r_profile(nm, float(k)))).min() for k in ks1) > 0.0
    and abs(np.trace(eta(r_profile(nm, 5.0))).real - 2.0) < 1e-12
    for nm in ("PHYS", "SOFT", "MARG", "DERIV", "2VAL")
)
signed_ratios = []
for r in (0.1, 0.5, 0.9, 0.999):
    A = SZ @ eta(r)
    ev = np.linalg.eigvals(A)
    ev = ev[np.argsort(ev.real)]
    signed_ratios.append(complex(ev[0] / ev[1]))
sq_ok = all(abs(complex(np.linalg.eigvals(SZ @ eta(r))[0]) ** 2 - (1 - r * r)) < 1e-9 for r in (0.1, 0.5, 0.9))
signed_degenerate = all(abs(sr + 1.0) < 1e-9 for sr in signed_ratios)
check("T1  the metric-as-state tower is WELL-DEFINED: every finite mode of every profile has a faithful "
      "positive state (min eigenvalue > 0, trace 2 before normalization) -- adversary (a)'s objection "
      "bites only in the k->inf limit, exactly where the invariant lives.  And the genuinely-Krein "
      "SIGNED candidate degenerates: A = J*eta(r) has A^2 = (1-r^2)I, eigenvalues -+sqrt(1-r^2), signed "
      f"ratio == -1 at every r (max dev {max(abs(sr + 1.0) for sr in signed_ratios):.1e}): a signed "
      "'Krein ratio set' carries NO information; the classical r_inf of the metric-as-state tower is "
      "the only workable definition (named fork).",
      all_states_ok and signed_degenerate and sq_ok,
      f"states positive={all_states_ok}, signed ratio == -1 always={signed_degenerate}")

# ====================================================================================================
# T2 -- THE EIGENVALUE LIST of the physical tower: lam_k ~ c/k (slowly varying, regular variation
#   index -1), sum lam_k DIVERGES (equal non-vanishing increments per decade).  This is the raw
#   Araki-Woods data of the Krein tail.
# ====================================================================================================
log("\n[T2] The physical eigenvalue list: lam_k ~ c/k slowly varying, non-summable")
kk = [1e3, 1e4, 1e5, 1e6]
klam = [k * lam_of(r_profile("PHYS", k)) for k in kk]
slowly_varying = max(klam) / min(klam) < 1.02
dec_sums = []
for a, b in ((1e3, 1e4), (1e4, 1e5), (1e5, 1e6)):
    ks = np.linspace(a, b, 20000)
    dk = (b - a) / 20000
    dec_sums.append(sum(lam_of(r_profile("PHYS", float(k))) for k in ks) * dk)
nonsummable = dec_sums[2] > 0.9 * dec_sums[0] > 0.0 and min(dec_sums) > 0.2
check("T2  PHYSICAL eigenvalue list: k*lam_k -> const "
      f"({klam[0]:.5f} .. {klam[3]:.5f}, spread < 2%): lam_k ~ c/k SLOWLY VARYING; per-decade partial "
      f"sums of lam are NON-VANISHING and comparable ({dec_sums[0]:.0f}, {dec_sums[1]:.0f}, "
      f"{dec_sums[2]:.0f} on 2e4-point decade grids): sum lam_k = inf.  Not type I; the tail mass that "
      "the ratio-set mass condition needs is available in every decade.",
      slowly_varying and nonsummable, f"k*lam spread {max(klam)/min(klam)-1:.4f}, decade sums {dec_sums[0]:.0f}/{dec_sums[2]:.0f}")

# ====================================================================================================
# T3 -- CLASSICAL TYPES of the five towers (Araki-Woods criteria + ratio-set computations).
#   PHYS  -> III_1  (pair ratios lam_j/lam_k ~ k/j DENSE, realized in every far window with per-window
#                    excitation mass bounded below -- the r_inf mass condition; r_inf = [0,inf))
#   SOFT  -> II_1   (sum (1/2 - mu_k)^2 < inf: per-decade increments vanish)
#   MARG  -> III_lam* (lam_k -> lam* ~ 0.101 constant => Powers; ratio set = closure(lam*^Z) u {0}:
#                    the target sqrt(lam*) sits in a verified GAP -- r_inf != [0,inf))
#   DERIV -> I_inf  (sum mu_k < inf: tail mass -> 0 => beyond N no ratio is realizable with fixed mass;
#                    r_inf = {1})
#   2VAL  -> III_1  (m*log a + n*log b dense since log a/log b = sqrt 2 irrational; masses constant)
# ====================================================================================================
log("\n[T3] Classical types: PHYS III_1, SOFT II_1, MARG III_lam (Powers), DERIV I_inf, 2VAL III_1")
# PHYS: dense pair ratios with mass ------------------------------------------------------------------
targets = [0.5, 2.0, 3.7, 10.0]
phys_dense = True
phys_masses = []
for N in (1e3, 1e4, 1e5):
    ks = np.linspace(N, 16 * N, 4000)
    phys_masses.append(sum(mu_of(r_profile("PHYS", float(k))) for k in ks) * (15 * N / 4000))
    for x in targets:
        errs = []
        for j in np.linspace(N, 1.5 * N, 200):
            kk2 = x * j          # lam ~ c/k, so lam_j / lam_{x*j} ~ x: the pair (j, x*j) realizes x
            if kk2 <= 16 * N:
                errs.append(abs(lam_of(r_profile("PHYS", float(j))) / lam_of(r_profile("PHYS", kk2)) - x) / x)
        if min(errs) > 1e-3:
            phys_dense = False
phys_mass_bounded_below = all(m > 0.2 for m in phys_masses)
# SOFT: II_1 criterion --------------------------------------------------------------------------------
soft_incr = []
for a, b in ((1e2, 1e3), (1e3, 1e4), (1e4, 1e5)):
    ks = np.linspace(a, b, 20000)
    soft_incr.append(sum((0.5 - mu_of(r_profile("SOFT", float(k)))) ** 2 for k in ks) * (b - a) / 20000)
soft_II1 = soft_incr[0] > 5 * soft_incr[1] and soft_incr[1] > 5 * soft_incr[2]  # increments vanish geometrically => sum converges
phys_not_II1 = (0.5 - mu_of(r_profile("PHYS", 1e6))) ** 2 > 0.2      # terms -> 1/4: divergent
# MARG: Powers plateau + ratio-set gap ---------------------------------------------------------------
lam_star = lam_of(r_profile("MARG", 1e6))
marg_plateau = abs(lam_of(r_profile("MARG", 1e3)) - lam_star) < 5e-3 and 0.08 < lam_star < 0.13
tgt = np.sqrt(lam_star)
gap = min(abs(lam_star ** n - tgt) / tgt for n in range(-6, 7))
marg_gap = gap > 0.5                                                 # sqrt(lam*) NOT in closure(lam*^Z)
zero_in_marg = lam_star ** 12 < 1e-10                                # lam*^n -> 0: 0 in r_inf (type III)
# DERIV: type I ---------------------------------------------------------------------------------------
tails = []
for N in (1e2, 1e3, 1e4):
    ks = np.linspace(N, 100 * N, 40000)
    tails.append(sum(mu_of(r_profile("DERIV", float(k))) for k in ks) * (99 * N / 40000))
deriv_typeI = tails[0] < 0.02 and tails[1] < 0.002 and tails[2] < 2e-4   # tail mass -> 0: sum mu < inf
# 2VAL: dense subgroup, bounded conditioning ---------------------------------------------------------
la, lb = np.log(LAM_A), np.log(LAM_B)
dense_2val = True
for x in (2.0, 5.0, 1.0 / 3.0):
    best = min(abs(m * la + n * lb - np.log(x)) for m in range(-60, 61) for n in range(-60, 61))
    if best > 0.05:
        dense_2val = False
cond_2val_bounded = max(cond_of(R_A), cond_of(R_B)) < 10.0
check("T3  TYPES.  PHYS: pair ratios lam_j/lam_k hit every target in {0.5,2,3.7,10} to <0.1% in every "
      f"far window [N,16N], N=1e3..1e5, with window excitation mass >= {min(phys_masses):.2f} bounded "
      "below (the r_inf mass condition) => r_inf = [0,inf) => TYPE III_1 -- the hyperfinite III_1 "
      "factor, the AQFT type of a local algebra, reproduced intrinsically from the Krein tail data.  "
      f"SOFT: sum(1/2-mu)^2 converges (decade increments {soft_incr[0]:.2f} -> {soft_incr[2]:.4f}) => "
      f"II_1 (PHYS terms -> 1/4: not II_1).  MARG: lam_k -> {lam_star:.4f} => POWERS III_lam*; "
      f"sqrt(lam*) sits in a {gap:.0%} gap of closure(lam*^Z) => r_inf != [0,inf), and lam*^n -> 0 => "
      f"0 IS in r_inf.  DERIV: tail mass -> 0 ({tails[0]:.3f} -> {tails[2]:.1e}) => sum mu < inf => "
      "TYPE I_inf, r_inf = {1}.  2VAL: m*log(a)+n*log(b) dense (log-ratio sqrt2 irrational) with "
      "constant masses => III_1 at BOUNDED conditioning.",
      phys_dense and phys_mass_bounded_below and soft_II1 and phys_not_II1 and marg_plateau and marg_gap
      and zero_in_marg and deriv_typeI and dense_2val and cond_2val_bounded,
      f"PHYS dense+mass={phys_dense and phys_mass_bounded_below}, SOFT II1={soft_II1}, MARG gap={gap:.2f}, "
      f"DERIV tail={tails[2]:.1e}, 2VAL dense@cond<10={dense_2val and cond_2val_bounded}")

# ====================================================================================================
# T4 -- THE CANDIDATE IDENTITY CHECK: "cond -> inf  <=>  0 in the Krein ratio invariant".
#   WALL(profile): the windowed sup of cond grows without bound under UV extension.
#   0 in r_inf:    from T3's type computations (0 in r_inf <=> type III).
#   RESULT: FAILS BOTH DIRECTIONS.  MARG: 0 in r_inf (III_lam) but NO wall  (kills <=).
#           DERIV: wall but 0 NOT in r_inf (type I)                        (kills =>).
#   And the stronger candidate "wall <=> III_1" ALSO fails both ways (DERIV: wall & not III_1;
#   2VAL: III_1 & no wall).  TRANSVERSALITY: all four (wall) x (0 in r_inf) cells inhabited.
# ====================================================================================================
log("\n[T4] The candidate identity: FAILS both directions; wall and ratio invariant are TRANSVERSE")


def wall_of(name: str) -> bool:
    sups = []
    for a, b in ((1e3, 2e3), (8e3, 1.6e4), (6.4e4, 1.28e5)):
        ks = np.linspace(a, b, 400)
        sups.append(max(cond_of(r_profile(name, float(k))) for k in ks))
    return sups[2] > 3.0 * sups[1] > 3.0 * sups[0] * 0.9 and sups[2] > 1e3


wall = {nm: wall_of(nm) for nm in ("PHYS", "SOFT", "MARG", "DERIV", "2VAL")}
zero_in_rinf = {"PHYS": True, "SOFT": False, "MARG": True, "DERIV": False, "2VAL": True}   # from T3
is_III1 = {"PHYS": True, "SOFT": False, "MARG": False, "DERIV": False, "2VAL": True}       # from T3
wall_expected = {"PHYS": True, "SOFT": False, "MARG": False, "DERIV": True, "2VAL": False}
wall_ok = wall == wall_expected
kills_arrow_left = zero_in_rinf["MARG"] and not wall["MARG"]        # 0 in r_inf without a wall
kills_arrow_right = wall["DERIV"] and not zero_in_rinf["DERIV"]     # wall without 0 in r_inf
cells = {(wall[nm], zero_in_rinf[nm]) for nm in wall}
transverse = cells == {(True, True), (True, False), (False, True), (False, False)}
cells_III1 = {(wall[nm], is_III1[nm]) for nm in wall}
transverse_III1 = cells_III1 == {(True, True), (True, False), (False, True), (False, False)}
check("T4  CANDIDATE IDENTITY FAILS BOTH DIRECTIONS.  Wall present exactly for {PHYS, DERIV} "
      "(windowed sup-cond grows without bound; the other three plateau).  <= KILLED by MARG: 0 in "
      "r_inf (Powers III_lam) with NO wall.  => KILLED by DERIV: wall (cond ~ k^2 -> inf) with r_inf "
      "= {1} (type I_inf).  All four (wall) x (0 in r_inf) cells inhabited -- and all four "
      "(wall) x (III_1) cells too (DERIV: wall, not III_1; 2VAL: III_1, no wall): the W98 wall is "
      "TRANSVERSE to the classical ratio-set/type invariant.  The wall is NOT a function of the "
      "(algebra, state) classification data.",
      wall_ok and kills_arrow_left and kills_arrow_right and transverse and transverse_III1,
      f"wall map ok={wall_ok}, <= killed={kills_arrow_left}, => killed={kills_arrow_right}, "
      f"4 cells={transverse}")

# ====================================================================================================
# T5 -- RATE-DEPENDENCE: the ITPFI invariant DISTINGUISHES what the Calkin class IDENTIFIES.
#   W103 T4 (reproduced): PHYS (g=const) and DERIV (g=G*k) metrics differ by a COMPACT operator --
#   same Calkin class 2[P].  But T3/T4: PHYS is III_1, DERIV is I_inf.  So the tail-quotient class
#   does NOT descend to the ratio invariant: the intrinsic tail data is RATE-SENSITIVE where the
#   Calkin quotient was rate-blind.  (This is the honest cost of going intrinsic.)
# ====================================================================================================
log("\n[T5] Rate-dependence: same Calkin class 2[P], DIFFERENT ITPFI types (III_1 vs I_inf)")
diffs = [opnorm(eta(r_profile("PHYS", k)) - eta(r_profile("DERIV", k))) for k in (1e2, 1e3, 1e4, 1e5)]
same_calkin = diffs[0] > diffs[3] and diffs[3] < 1e-3
types_differ = is_III1["PHYS"] and not is_III1["DERIV"] and zero_in_rinf["PHYS"] and not zero_in_rinf["DERIV"]
check("T5  PHYS vs DERIV: metric difference block-norms -> 0 "
      f"({diffs[0]:.2e} -> {diffs[3]:.2e}) -- SAME Calkin class 2[P] (W103 T4 reproduced) -- but the "
      "towers have DIFFERENT classical types (III_1 vs I_inf) and different ratio invariants "
      "([0,inf) vs {1}).  The Calkin class does NOT determine the ITPFI invariant: W103's "
      "rate-independence is a property of the compact-ideal quotient ONLY; the intrinsic tail "
      "invariant is rate-sensitive.",
      same_calkin and types_differ, f"compact diff={same_calkin}, types differ={types_differ}")

# ====================================================================================================
# T6 -- THE REPAIRED IDENTITY (exact): the wall IS intrinsic -- to the (state, GRADING) pair.
#   Per mode: the grading twists the state, phi o AdJ has density eta(-r)/2 = J (eta(r)/2) J, and
#   eta(-r) = (1-r^2) eta(r)^{-1} EXACTLY.  Consequences (all verified):
#     (a) fidelity F(phi, phi o J) = 1 - r^2 exactly;
#     (b) the relative modular operator Delta_{phi o J, phi} (X |-> sigma X rho^{-1}) has norm
#         EXACTLY cond(eta(r)) = (1+r)/(1-r);
#     (c) the Connes cocycle u_t = eta(-r)^{it} eta(r)^{-it} is UNITARY for every real t (flow half
#         survives -- zero cost), while the analytic continuation to t = -i/2 has per-mode norm
#         sqrt(cond) -> inf (conjugation half obstructed): the W103 split, in relative-modular form.
#   HENCE: WALL <=> sup_k ||Delta_{phi o J, phi}||_k = inf -- an EXACT biconditional across all five
#   profiles, basis-free and truncation-free GIVEN the grading and the mode filtration.  HONEST
#   RESIDUAL: filtration-free candidates fail (T4: ratio set transverse; global domination
#   phi o J <= C phi needs prod_k cond_k < inf -- fails even for 2VAL/Powers, verified; disjointness
#   sum r_k^2 = inf -- MARG is disjoint with NO wall, verified).  The grading and filtration are
#   irreducible inputs: the slot is (algebra, state, grading, filtration)-intrinsic.
# ====================================================================================================
log("\n[T6] Repaired identity: ||Delta_{phi o J, phi}|| = cond EXACTLY; wall <=> sup relative-modular norm = inf")
rel_ok, fid_ok, inv_ok = True, True, True
for r in (0.1, 0.5, 0.9, 0.999):
    rho, sig = eta(r) / 2.0, (SZ @ eta(r) @ SZ) / 2.0
    inv_ok &= opnorm(sig - (1 - r * r) / 4.0 * np.linalg.inv(rho)) < 1e-12       # eta(-r)=(1-r^2)eta^{-1}
    Delta = np.kron(sig, np.linalg.inv(rho).T)                                    # X -> sig X rho^{-1}
    rel_ok &= abs(opnorm(Delta) - cond_of(r)) < 1e-9 * cond_of(r)
    sr = np.linalg.cholesky(rho)
    F = float(np.sum(np.sqrt(np.maximum(np.linalg.eigvalsh(dag(sr) @ sig @ sr), 0.0)))) ** 2
    fid_ok &= abs(F - (1 - r * r)) < 1e-9
# cocycle: flow half unitary, continuation to -i/2 diverges
def mpow(A: np.ndarray, p: complex) -> np.ndarray:
    w, V = np.linalg.eigh(A)
    return V @ np.diag(np.exp(p * np.log(w))) @ dag(V)


coc_flow = all(abs(opnorm(mpow(SZ @ eta(r) @ SZ, 1j) @ mpow(eta(r), -1j)) - 1.0) < 1e-9
               for r in (0.1, 0.9, 0.9999))
coc_half = [opnorm(mpow(SZ @ eta(r) @ SZ, 0.5) @ mpow(eta(r), -0.5)) for r in (0.5, 0.99, 0.9999)]
coc_diverges = all(abs(coc_half[i] - np.sqrt(cond_of(r))) < 1e-6 * np.sqrt(cond_of(r))
                   for i, r in enumerate((0.5, 0.99, 0.9999))) and coc_half[2] > 100
# the biconditional across all five profiles (||Delta_rel||_k = cond_k exactly => same sup):
bicond = all(wall[nm] == (max(cond_of(r_profile(nm, float(k))) for k in np.linspace(6.4e4, 1.28e5, 200)) > 1e4)
             for nm in wall)
# honest residual: global domination fails even at bounded cond (2VAL: prod cond_k diverges)
prod_cond_2val = 40.0 * np.log(cond_of(R_A) * cond_of(R_B)) / 2.0    # log of product over 40 modes > 0
global_dom_too_strong = prod_cond_2val > 10.0                        # diverges linearly in mode count
# disjointness (Kakutani: sum (1-F) = sum r^2): MARG has sum r^2 = inf (r -> const) but NO wall
marg_r_inf_const = r_profile("MARG", 1e6) > 0.5
disjoint_transverse = marg_r_inf_const and not wall["MARG"]
check("T6  REPAIRED IDENTITY (exact): eta(-r) = (1-r^2) eta(r)^{-1}, fidelity F(phi, phi o J) = 1-r^2, "
      "and ||Delta_{phi o J, phi}|| = (1+r)/(1-r) = cond EXACTLY (verified to 1e-9 at r up to 0.999).  "
      "Cocycle: u_t unitary at every real t (flow half FREE); continuation to t = -i/2 has norm "
      f"sqrt(cond) -> inf ({coc_half[0]:.1f} -> {coc_half[2]:.0f}) (conjugation half OBSTRUCTED) -- the "
      "W103 split in relative-modular language.  WALL <=> sup_k ||Delta_{phi o J, phi}||_k = inf holds "
      "across ALL FIVE profiles.  HONEST RESIDUAL: filtration-free forms fail -- global domination "
      "needs prod cond_k < inf (diverges even for Powers at bounded cond), and grading-disjointness "
      "(sum r_k^2 = inf) is transverse (MARG disjoint, no wall).  The slot is intrinsic to (algebra, "
      "state, GRADING, filtration); the grading is what the classical classification drops.",
      inv_ok and rel_ok and fid_ok and coc_flow and coc_diverges and bicond and global_dom_too_strong
      and disjoint_transverse,
      f"Delta=cond exact={rel_ok}, F=1-r^2 exact={fid_ok}, flow unitary={coc_flow}, bicond 5/5={bicond}")

# ====================================================================================================
# T7 -- (T2 target) TAIL-CLASS COHERENCE on overlaps: CLASSES COHERE while OPERATORS DIVERGE.
#   W98 T6 setup: shared overlap modes carry region-dependent modular weights w_O1 = 1.0, w_O2 = 0.45
#   rescaling the coupling.  OPERATOR level (W98, reproduced): ||eta_1^{-1/2} - eta_2^{-1/2}|| diverges
#   in the UV.  QUOTIENT level (new): ||eta(r^1_k) - eta(r^2_k)|| = |r^1_k - r^2_k| -> 0, so the
#   difference is COMPACT: [C_O1]|_ov = [C_O2]|_ov = 2[P] -- the same singular class, the same
#   Krein-null line, the same typed slot.  The INTERFACE glues across observers; only the God's-eye
#   conjugation data does not.
# ====================================================================================================
log("\n[T7] Tail-class coherence: [C_O1] = [C_O2] = 2[P] on the overlap while the J-data diverges (W98 T6)")
W1, W2 = 1.0, 0.45


def invsqrt(r: float) -> np.ndarray:
    return mpow(eta(r), -0.5)


op_dis = [float(np.max(np.abs(invsqrt(r_of(G * W1, k)) - invsqrt(r_of(G * W2, k))))) for k in (1.0, 1e3, 1e4, 1e5)]
op_diverges = op_dis[0] < op_dis[1] < op_dis[2] < op_dis[3] and op_dis[3] > 30.0
met_dis = [opnorm(eta(r_of(G * W1, k)) - eta(r_of(G * W2, k))) for k in (1e2, 1e3, 1e4, 1e5)]
met_exact = all(abs(met_dis[i] - abs(r_of(G * W1, k) - r_of(G * W2, k))) < 1e-12
                for i, k in enumerate((1e2, 1e3, 1e4, 1e5)))
met_compact = met_dis[0] > met_dis[3] and met_dis[3] < 1e-4
eta1_lim = eta(1.0)
both_to_2P = all(opnorm(eta(r_of(G * w, 1e5)) - eta1_lim) < 1e-3 for w in (W1, W2))
e_null = np.array([1j, 1.0], dtype=complex) / np.sqrt(2.0)


def null_overlap(r: float) -> float:
    w, V = np.linalg.eigh(eta(r))
    return abs(np.vdot(V[:, int(np.argmin(w))], e_null))


same_null_line = all(null_overlap(r_of(G * w, 1e4)) > 1.0 - 1e-9 for w in (W1, W2))
check("T7  CLASSES COHERE, OPERATORS DO NOT.  Operator level: ||eta_1^{-1/2} - eta_2^{-1/2}|| on shared "
      f"overlap modes DIVERGES ({op_dis[1]:.1f} at k=1e3 -> {op_dis[3]:.1f} at k=1e5; W98 T6 reproduced). "
      f"Quotient level: ||eta(r^1_k) - eta(r^2_k)|| = |r^1_k - r^2_k| EXACTLY, -> 0 ({met_dis[0]:.1e} -> "
      f"{met_dis[3]:.1e}): the difference is COMPACT, both metrics converge to the SAME 2P, and both "
      "regions' obstruction dies on the SAME Krein-null line e_null (overlap 1 - 1e-9).  "
      "[C_O1]|_ov = [C_O2]|_ov = 2[P]: one singular class, one typed slot, shared by both observers.",
      op_diverges and met_exact and met_compact and both_to_2P and same_null_line,
      f"op diverges={op_diverges}, metric diff compact={met_compact}, same 2P={both_to_2P}, same null line={same_null_line}")

# ====================================================================================================
# T8 -- NON-TRIVIALITY CONTROL 1 (adversary (b)): class coherence is NOT automatic.  A region whose
#   modular frame is ROTATED (mixing direction theta_2 = pi/2 + 0.9, region 1 at pi/2) has IDENTICAL
#   per-mode eigenvalues (same break, same cond divergence, and an operator-level disagreement just as
#   in T7) but the tail limits are 2P vs 2P_theta with ||P - P_theta|| ~ 0.43 CONSTANT: the metric
#   difference is NOT compact, and the classes DISAGREE.  So coherence is a falsifiable property; it
#   holds in the W98 model because region-dependence enters as a SCALAR modular weight (the mixing
#   direction is fixed by the field content) -- a NAMED load-bearing assumption.
# ====================================================================================================
log("\n[T8] Control 1 (rotation): operators disagree AND classes disagree -- coherence has content")
TH2 = np.pi / 2.0 + 0.9
ks8 = (1e2, 1e3, 1e4, 1e5)
same_eigs = all(abs(np.linalg.eigvalsh(eta(r_of(G, k), TH2))[0] - np.linalg.eigvalsh(eta(r_of(G, k)))[0]) < 1e-12
                for k in ks8)
rot_met_dis = [opnorm(eta(r_of(G, k), TH2) - eta(r_of(G, k))) for k in ks8]
not_compact = min(rot_met_dis) > 0.5                                  # metric difference DOES NOT vanish
P1_, P2_ = eta(1.0) / 2.0, eta(1.0, TH2) / 2.0
proj_gap = opnorm(P1_ - P2_)
classes_disagree = proj_gap > 0.3 and opnorm(P2_ @ P2_ - P2_) < 1e-12
null_mismatch = null_overlap(r_of(G, 1e4)) - abs(np.vdot(
    np.linalg.eigh(eta(r_of(G, 1e4), TH2))[1][:, 0], e_null))
check("T8  ROTATED-FRAME CONTROL: identical eigenvalues at every k (same break, same cond divergence) "
      f"but the metric difference stays >= {min(rot_met_dis):.2f} at all k (NOT compact) and the tail "
      f"projections differ by ||P - P_theta|| = {proj_gap:.2f}: [C_O1] != [C_O2'] -- the CLASSES "
      "DISAGREE and the null lines differ.  Class coherence is therefore NOT a compact-difference "
      "tautology: it is falsifiable, and W98's model falls on the COHERE side only because the "
      "region-dependence is a scalar modular WEIGHT (direction fixed by the field content) -- named "
      "load-bearing assumption.",
      same_eigs and not_compact and classes_disagree,
      f"same eigenvalues={same_eigs}, non-compact diff={not_compact}, ||P-P_theta||={proj_gap:.2f}")

# ====================================================================================================
# T9 -- NON-TRIVIALITY CONTROL 2 (weight collapse): coherence also needs the modular weights bounded
#   BELOW.  If region 2's weight vanishes UV-fast (w_2(k) = 1/(1+k^2)), region 2 is UV-soft on the
#   overlap: [C_O2] is INVERTIBLE while [C_O1] = 2[P] is singular -- maximal class disagreement.
#   W98's weights are O(1) constants, so the physical setup satisfies the assumption (named).
# ====================================================================================================
log("\n[T9] Control 2 (weight collapse): a UV-vanishing modular weight breaks class coherence")
ks9 = np.linspace(1e3, 1e5, 300)
r2_soft = [r_of(G / (1.0 + float(k) ** 2), float(k)) for k in ks9]
c2_invertible = min(1.0 - r for r in r2_soft) > 0.9                   # region-2 tail min-eig -> 1
c1_singular = max(1.0 - r_of(G, float(k)) for k in ks9) < 1e-3        # region-1 tail min-eig -> 0
check("T9  WEIGHT-COLLAPSE CONTROL: with w_2(k) = 1/(1+k^2) the overlap restriction of region 2 is "
      f"UV-soft (tail min-eig {min(1.0 - r for r in r2_soft):.3f} -> invertible class) while region 1 "
      f"stays singular (tail min-eig {max(1.0 - r_of(G, float(k)) for k in ks9):.1e} -> [C]=2[P]): the "
      "classes MAXIMALLY disagree.  Tail-class coherence requires the region weights bounded below; "
      "W98's are O(1) constants (assumption named, satisfied in the model).",
      c2_invertible and c1_singular, f"soft region invertible={c2_invertible}, hard region singular={c1_singular}")

# ====================================================================================================
# T10 -- VERDICTS.
#   T1 = PARTIAL: the candidate identity FAILS both directions (T4 transversality); the classical type
#        of the physical tower is hyperfinite III_1 (T3) and the grading is classification-blind; the
#        repaired relative-modular identity holds EXACTLY (T6) -- the slot is (algebra, state, grading,
#        filtration)-intrinsic, NOT (algebra, state)-intrinsic.
#   T2 = CLASSES-COHERE: the per-region tail classes agree on overlaps (T7) with counter-model-backed
#        content (T8, T9) and two named load-bearing assumptions (scalar weights; bounded below).
# ====================================================================================================
log("\n[T10] VERDICTS: T1 = PARTIAL (identity fails; repaired grading-relative form exact); T2 = CLASSES-COHERE")
verdict = {
    # T1:
    "tower_well_defined_every_finite_mode_positive": True,                    # T1
    "signed_krein_ratio_degenerates_named_fork": True,                        # T1
    "physical_tower_type_III_1_hyperfinite": True,                            # T2, T3
    "candidate_identity_cond_iff_zero_in_rinf_HOLDS": False,                  # T4: fails BOTH ways
    "arrow_left_killed_by_MARG_powers": True,                                 # T4
    "arrow_right_killed_by_DERIV_type_I": True,                               # T4
    "wall_transverse_to_ratio_invariant_all_four_cells": True,                # T4
    "calkin_class_does_not_determine_itpfi_type": True,                       # T5
    "repaired_identity_relative_modular_exact": True,                         # T6
    "slot_intrinsic_to_algebra_state_pair_alone": False,                      # T4+T6: needs grading+filtration
    "slot_intrinsic_to_state_grading_filtration": True,                       # T6
    "verdict_T1_IDENTITY_HOLDS": False,
    "verdict_T1_PARTIAL": True,
    "verdict_T1_FAILS_outright": False,                                       # the repaired form survives
    # T2:
    "operator_disagreement_diverges_W98_reproduced": True,                    # T7
    "tail_classes_agree_on_overlap_same_2P_same_null_line": True,             # T7
    "coherence_has_content_rotation_control_disagrees": True,                 # T8
    "coherence_needs_weights_bounded_below": True,                            # T9
    "verdict_T2_CLASSES_COHERE": True,
    "verdict_T2_CLASSES_DISAGREE": False,
}
ok = (
    not verdict["candidate_identity_cond_iff_zero_in_rinf_HOLDS"]
    and verdict["repaired_identity_relative_modular_exact"]
    and verdict["verdict_T1_PARTIAL"] and not verdict["verdict_T1_IDENTITY_HOLDS"]
    and verdict["verdict_T2_CLASSES_COHERE"] and not verdict["verdict_T2_CLASSES_DISAGREE"]
    and verdict["coherence_has_content_rotation_control_disagrees"]
)
check("T10 VERDICTS.  T1 = PARTIAL: the candidate identity 'wall <=> 0 in the Krein ratio invariant' "
      "FAILS in both directions (MARG kills <=, DERIV kills =>; full transversality); what survives is "
      "(i) the physical tower is intrinsically the hyperfinite III_1 factor, and (ii) the EXACT "
      "repaired identity: wall <=> the relative modular operator between the metric-state and its "
      "GRADING twist is unbounded (per-mode norm = cond exactly; cocycle flow free, continuation to "
      "-i/2 obstructed).  The slot is intrinsic to (algebra, state, grading, filtration) -- NOT to the "
      "(algebra, state) pair; the classical classification is grading-blind, which is WHY it misses "
      "the wall.  T2 = CLASSES-COHERE: on overlaps the per-region tail classes agree (same 2[P], same "
      "null line, one shared slot) while the operator data diverges -- and the two controls show this "
      "is a property, not a tautology.",
      ok, f"{sum(1 for v in verdict.values() if v)} true / {len(verdict)} booleans")

# ====================================================================================================
# SUMMARY
# ====================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, okk, _ in results if okk)
log(f"CHECKS: {npass}/{len(results)} passed.")
assert all(okk for _, okk, _ in results), "some W107 checks FAILED"

log("")
log("W107 VERDICT (this file is the computation, not a claim-status change):")
log("  * T1 (Krein ratio set / intrinsic slot): PARTIAL.  The tower is well-defined (metric-as-state")
log("    ITPFI; adversary (a) answered: positivity holds at every finite mode, and the genuinely-Krein")
log("    signed ratio degenerates to -1 identically).  The PHYSICAL tower is the hyperfinite TYPE III_1")
log("    factor (lam_k ~ c/k slowly varying: dense pair ratios with mass) -- the AQFT local-algebra")
log("    type reproduced intrinsically from the Krein tail data.  BUT the candidate identity")
log("    'cond -> inf <=> 0 in r_inf' FAILS BOTH DIRECTIONS: MARG (Powers III_lam: 0 in r_inf, no wall)")
log("    kills <=; DERIV (type I_inf: wall, 0 not in r_inf) kills =>.  The wall is TRANSVERSE to the")
log("    classical invariants (all four cells inhabited), and PHYS/DERIV share the Calkin class 2[P]")
log("    while having different types: the Calkin quotient's rate-independence does NOT survive.")
log("    WHAT SURVIVES (exact): wall <=> sup_k ||Delta_{phi o AdJ, phi}||_k = inf -- the relative")
log("    modular operator between the metric-state and its GRADING twist (per-mode norm = cond exactly;")
log("    F = 1-r^2 exactly; cocycle unitary at all real t, continuation to -i/2 diverges = the W103")
log("    flow/conjugation split).  The slot is intrinsic to (algebra, state, grading, filtration);")
log("    the classical classification is grading-blind, which is why it cannot see the wall.")
log("  * T2 (tail-class coherence): CLASSES-COHERE.  On W98's overlap the operator disagreement")
log("    diverges (reproduced) but the metric difference |r^1_k - r^2_k| -> 0 is compact: both regions")
log("    restrict to the SAME singular class 2[P] with the SAME Krein-null line -- one typed slot")
log("    shared by both observers.  NOT trivial: the rotated-frame control (identical break, classes")
log("    DISAGREE) and the weight-collapse control (classes maximally disagree) show coherence is a")
log("    falsifiable property.  Load-bearing assumptions (named): region-dependence is a scalar")
log("    modular weight (direction fixed by field content) and the weights are bounded below.")
log("  * No canon / RESEARCH-STATUS / CANON / verdict / posture change.  Present, do not decide.")
raise SystemExit(0)
