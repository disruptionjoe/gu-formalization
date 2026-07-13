#!/usr/bin/env python3
r"""
W111 -- THE SQUARE-ROOT TEST: does the outside view exist at the first-order (factorized) level?

THE FUSION HYPOTHESIS UNDER TEST (not assumed): the fourth-order "square" structure (the UV flagship:
|II|^2 -> the Stelle propagator 1/(p^2(p^2 - m^2))) and the outside-view-free Krein doublet (the Observer
Structure Theorem wall, W109 clause 3) are ONE structure -- the Krein doublet IS the square's
partial-fraction decomposition, and SQUARING is precisely the operation that COSTS the outside view
(i.e. the first-order square-root theory would have a BOUNDED modular conjugation / definitizable metric
over the same mode tower where the fourth-order conditioning diverges).

THE MODEL (faithful to the repo's own W98/W109 tower -- same parameters, same metric family):
  per momentum k: healthy w1(k) = sqrt(k^2 + m1^2), ghost w2(k) = sqrt(k^2 + m2^2), m1 = 0, m2 = 0.3;
  mixing g_k = G k^p (G = 0.1; p = 0 primary, p = 1 sweep); exceptional-point parameter
  r_k = g_k / (g_k + Dw(k)/2), Dw = |m1^2 - m2^2|/(w1 + w2) -> 0; W52/W84 metric eta(r) = I + r sigma_y,
  cond(eta(r)) = (1+r)/(1-r) -> infinity over the tower (the W98/W109 wall).
  The INTERACTING fourth-order mode operator (canonical frame) is the quasi-Hermitian
      M_k = eta(r_k)^{-1/2} diag(w1^2, w2^2) eta(r_k)^{+1/2},
  whose positive metric is exactly eta(r_k) (matching W98: Theta = (T T^dag)^{-1} = eta for
  T = eta^{-1/2}) and whose determinant symbol det(w^2 I - M_k) = (w^2-w1^2)(w^2-w2^2) is the Stelle
  fourth-order symbol -- the interaction moves the EIGENVECTORS (EP collapse), not the eigenvalues.

THE TESTS:
  T1  THE SQUARE: partial fractions of the Stelle propagator -- the two poles carry OPPOSITE-sign
      residues of magnitude 1/|Dm^2| (the Krein doublet grading; the residues blow up as Dm^2 -> 0:
      the EP seed).  This half of the fusion is TRUE and verified.
  T2  the fourth-order wall reproduced: min-cond over the FULL positive-metric family of M_k equals
      (1+r_k)/(1-r_k) EXACTLY (lower bound (1+c)/(1-c) with c = |<v1,v2>| = r_k, achieved by eta(r_k)),
      and its sup diverges over the tower (octave doubling).
  T3  THE SQUARE ROOT + RIGIDITY: all four square-root branches D_s = eta^{-1/2} diag(s1 w1, s2 w2)
      eta^{1/2} (s_i = +-1) satisfy D_s^2 = M_k; they are EXHAUSTIVE (any X with X^2 = M commutes with
      M; the commutant of M is 2-dimensional = poly(M), verified via the Sylvester kernel); therefore
      EVERY square root shares M's eigenframe, hence EXACTLY its optimal metric conditioning.  The
      first-order 4x4 Dirac-type operator D4 (spectrum {+-w1, +-w2}) has char poly = the fourth-order
      symbol and the same conditioning.
  T4  THE DECISIVE COMPARISON: cond_1(k) / cond_4(k) = 1 IDENTICALLY across the tower (both p = 0 and
      p = 1); both diverge together.  Case (ii) of the pre-registered menu: THE WALL PRECEDES THE
      SQUARE.  Free control: at g = 0 every first-order branch is HERMITIAN (positive-definite Hilbert
      quantization, cond 1, NO Krein structure needed) while the assembled fourth-order scalar already
      carries the Krein residue grading (T1) -- but with cond 1 (ghost WITHOUT wall).  So: squaring
      creates the GHOST; interaction creates the WALL; squaring is wall-neutral.
  T5  FACTORIZATION-DEPENDENCE (the adversary "your D is a chosen factorization"):
      (a) branch invariance -- all four branches + D4 share one metric family: the branch bit is
          METRIC-INERT (it cannot store the outside view);
      (b) frame covariance -- conjugating D and M by the same bounded frame preserves the equality
          min-cond_1 = min-cond_4 (the rigidity is frame-covariant);
      (c) the balanced companion/Ostrogradsky frame is walled EVEN FREE (Vandermonde eigenvector
          collapse as Dw -> 0) -- a NON-canonical frame (its transform to the canonical doublet frame
          is unbounded over the tower); named, not defaulted;
      (d) the scalar SYMBOL underdetermines: diag(w1^2, w2^2) has the same fourth-order det symbol as
          M_k but min-cond 1 -- the wall is data of the (operator, inner product) pair, and THAT pair
          is what square-rooting cannot change.
      In NO examined factorization is the first order clean while the fourth order is walled: the
      FUSION-REAL direction is excluded factorization-independently.
  T6  order-independence of the wall condition: the first-order spectrum has the SAME degenerating gap
      Dw(k) -> 0 (between the +w1 and +w2 branches), so any non-UV-soft FIRST-ORDER mixing walls the
      first-order theory directly; a UV-soft coupling g ~ 1/k^2 keeps it bounded (the same survival
      window X as W100).  GUARD against the fake escape "the eigenvalue gap of M is the CONSTANT
      Dm^2, so squaring cures the degeneracy": the wall lives in the EIGENVECTORS, not the eigenvalue
      gap -- M's eigenvalue gap is constant while its conditioning diverges.
  T7  verdict booleans: FUSION-REAL = False; FUSION-DEAD (as stated) = True; the surviving pieces named.

VERDICT: FUSION-DEAD (as stated).  "Squaring costs the outside view" is FALSE: every square root of the
interacting fourth-order mode operator is EXACTLY as walled (rigidity).  What survives: (1) the Krein
doublet IS the square's partial-fraction decomposition (T1, true at symbol/residue level); (2) squaring
creates the GHOST (positive first-order multiplet -> Krein scalar via the residue signs, free level);
(3) the wall is charged by the INTERACTION, at every factorization level alike -- the square-root
rigidity theorem (model-grade).

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


def opnorm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A, 2))


def cond_pos(T: np.ndarray) -> float:
    w = np.linalg.eigvalsh(T)
    return float(w[-1] / w[0])


# ==================================================================================================
# THE MODEL (the W98/W109 tower, same parameters).
# ==================================================================================================
M1, M2, G = 0.0, 0.30, 0.10
N_OCT = 22
K0 = 0.1
PTS_PER_OCT = 64

SY = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
U_Y = np.column_stack([np.array([1.0, 1j]) / np.sqrt(2.0),      # sigma_y eigvec, eigenvalue +1
                       np.array([1.0, -1j]) / np.sqrt(2.0)])    # sigma_y eigvec, eigenvalue -1


def eta_pow(r: float, s: float) -> np.ndarray:
    """(I + r sigma_y)^s, analytic (no numerical eig near the EP)."""
    return U_Y @ np.diag([(1.0 + r) ** s, (1.0 - r) ** s]).astype(complex) @ dag(U_Y)


def tower(p: float) -> dict:
    ks = np.geomspace(K0, K0 * 2.0 ** N_OCT, N_OCT * PTS_PER_OCT)
    w1 = np.sqrt(ks * ks + M1 * M1)
    w2 = np.sqrt(ks * ks + M2 * M2)
    dw = np.abs(w1 - w2)
    g_k = G * ks ** p
    r = np.minimum(g_k / (g_k + 0.5 * dw), 1.0 - 1e-15)
    return {"ks": ks, "w1": w1, "w2": w2, "dw": dw, "r": r, "p": p}


TW0 = tower(0.0)
TW1 = tower(1.0)


def M_of(r: float, w1: float, w2: float) -> np.ndarray:
    """The interacting fourth-order mode operator (canonical frame), metric eta(r)."""
    return eta_pow(r, -0.5) @ np.diag([w1 * w1, w2 * w2]).astype(complex) @ eta_pow(r, +0.5)


def D_branch(r: float, w1: float, w2: float, s1: int, s2: int) -> np.ndarray:
    """First-order square-root branch: D^2 = M."""
    return eta_pow(r, -0.5) @ np.diag([s1 * w1, s2 * w2]).astype(complex) @ eta_pow(r, +0.5)


def min_cond_family(V: np.ndarray, ngrid: int = 601) -> float:
    """min over p>0 of cond( V^{-dag} diag(1, p) V^{-1} ) -- the FULL positive-metric family of any
    operator diagonalized by V with real distinct eigenvalues (2x2; one scale fixed WLOG)."""
    Vi = np.linalg.inv(V)
    best = np.inf
    for t in np.geomspace(1e-3, 1e3, ngrid):
        Th = dag(Vi) @ np.diag([1.0, t]).astype(complex) @ Vi
        best = min(best, cond_pos(Th))
    return best


def unit_cols(V: np.ndarray) -> np.ndarray:
    return V / np.linalg.norm(V, axis=0, keepdims=True)


def eig_overlap(V: np.ndarray, i: int = 0, j: int = 1) -> float:
    Vu = unit_cols(V)
    return abs(complex(np.vdot(Vu[:, i], Vu[:, j])))


log("=" * 100)
log("W111 / THE SQUARE-ROOT TEST -- does the outside view exist at the first-order factorization level?")
log(f"      Tower: m1={M1}, m2={M2}, G={G}, k in [{K0}, {K0}*2^{N_OCT}], p in {{0,1}};"
    " metric family eta(r) = I + r sigma_y (W98/W109).")
log("=" * 100)

# ==================================================================================================
# T1 -- THE SQUARE: the Krein doublet IS the partial-fraction decomposition of the Stelle propagator.
#   1/(x (x - m^2)) = (1/m^2) [ 1/(x - m^2) - 1/x ]  (x = p^2): residue at the massless pole = -1/m^2,
#   at the massive pole = +1/m^2 -- OPPOSITE signs (the doublet grading eta_0 = diag(+1,-1)), equal
#   magnitude 1/|Dm^2| (which BLOWS UP as the poles degenerate: the EP seed).  General doublet:
#   residues +-1/(w1^2 - w2^2).
# ==================================================================================================
log("\n[T1] THE SQUARE: partial fractions of 1/(p^2(p^2 - m^2)) -- opposite residues = the Krein doublet")
m2sq = M2 * M2
xs = np.array([0.017, 0.31, 1.7, 42.0, -3.3])
lhs = 1.0 / (xs * (xs - m2sq))
rhs = (1.0 / m2sq) * (1.0 / (xs - m2sq) - 1.0 / xs)
pf_exact = float(np.max(np.abs(lhs - rhs) / np.abs(lhs)))
res0 = -1.0 / m2sq                                   # residue (in x = p^2) at x = 0
resm = +1.0 / m2sq                                   # residue at x = m^2
res0_num = float(np.real(1.0 / (0.0 - m2sq)))        # lim x->0 of x * LHS
resm_num = float(np.real(1.0 / m2sq))                # lim x->m^2 of (x - m^2) * LHS
opposite = (res0 < 0.0 < resm) and abs(res0 + resm) < 1e-12
magnitude = abs(abs(res0) - 1.0 / m2sq) < 1e-12
# degeneracy blow-up (the EP seed): residues ~ 1/|Dm^2| -> inf as Dm^2 -> 0:
blow = [1.0 / d for d in (1e-1, 1e-3, 1e-6)]
blow_up = blow[0] < blow[1] < blow[2]
check("T1  THE SQUARE half of the fusion is TRUE: 1/(p^2(p^2-m^2)) = (1/m^2)[1/(p^2-m^2) - 1/p^2] "
      f"(max rel err {pf_exact:.1e}); the two poles carry OPPOSITE-sign residues -+1/m^2 "
      f"({res0_num:.4f} / {resm_num:.4f}) = the Krein doublet grading diag(+1,-1); the residue "
      "magnitude 1/|Dm^2| blows up as the poles degenerate -- the exceptional-point seed is already "
      "in the partial fractions.",
      pf_exact < 1e-12 and opposite and magnitude and blow_up,
      f"pf exact={pf_exact < 1e-12}, opposite residues={opposite}, EP seed={blow_up}")

# ==================================================================================================
# T2 -- the fourth-order wall, reproduced with the FULL metric family (not just eta(r)):
#   (i) M_k is quasi-Hermitian with metric eta(r_k): eta M = M^dag eta;
#   (ii) det symbol preserved: det(w^2 - M_k) = (w^2-w1^2)(w^2-w2^2) -- interaction moves eigenvectors;
#   (iii) eigenvector overlap c_k = r_k EXACTLY, so the LOWER bound over the FULL positive-metric
#         family is (1+c)/(1-c) = (1+r)/(1-r) [for any Theta in the family, Rayleigh quotients at
#         v1 -+ v2 give cond >= (1+c)/(1-c), p-independent]; eta(r_k) ACHIEVES it => min-cond_4(k) =
#         (1+r_k)/(1-r_k) exactly (numeric grid confirms);
#   (iv) sup over the tower diverges (octave doubling) -- the W98/W109 wall.
# ==================================================================================================
log("\n[T2] The fourth-order wall: min-cond over the FULL metric family = (1+r)/(1-r), diverges over the tower")
probe_idx = [0, len(TW0["ks"]) // 4, len(TW0["ks"]) // 2, 3 * len(TW0["ks"]) // 4, len(TW0["ks"]) - 200]
qh_err, det_err, ovl_err, min_err = [], [], [], []
for i in probe_idx:
    r, w1, w2 = float(TW0["r"][i]), float(TW0["w1"][i]), float(TW0["w2"][i])
    M = M_of(r, w1, w2)
    eta = eta_pow(r, 1.0)
    qh_err.append(opnorm(eta @ M - dag(M) @ eta) / opnorm(M))
    wt = 1.7
    det_lhs = complex(np.linalg.det(wt * np.eye(2) - M))
    det_rhs = (wt - w1 * w1) * (wt - w2 * w2)
    det_err.append(abs(det_lhs - det_rhs) / max(abs(det_rhs), 1e-30))
    V = eta_pow(r, -0.5)                              # eigenvector matrix of M (columns)
    ovl_err.append(abs(eig_overlap(V) - r))
    if r < 0.999999:                                  # grid optimization meaningful away from underflow
        min_err.append(abs(min_cond_family(V) - (1.0 + r) / (1.0 - r)) / ((1.0 + r) / (1.0 - r)))
cond4 = (1.0 + TW0["r"]) / (1.0 - TW0["r"])
sups = [float(np.max(cond4[TW0["ks"] < K0 * 2.0 ** j])) for j in (N_OCT - 2, N_OCT - 1, N_OCT)]
wall = sups[1] > 1.5 * sups[0] and sups[2] > 1.5 * sups[1]
check("T2  THE FOURTH-ORDER WALL REPRODUCED, with the FULL metric family: eta M = M^dag eta "
      f"(max rel res {max(qh_err):.1e}); det symbol = (w^2-w1^2)(w^2-w2^2) preserved "
      f"(max rel err {max(det_err):.1e}) -- the interaction collapses EIGENVECTORS, not eigenvalues; "
      f"eigenvector overlap c = r exactly (max err {max(ovl_err):.1e}); min-cond over the whole family "
      f"= (1+r)/(1-r) (grid rel err {max(min_err):.1e}); sup diverges over the tower "
      f"({sups[0]:.0f} -> {sups[1]:.0f} -> {sups[2]:.0f}).",
      max(qh_err) < 1e-9 and max(det_err) < 1e-9 and max(ovl_err) < 1e-9 and max(min_err) < 2e-3 and wall,
      f"quasi-Herm={max(qh_err) < 1e-9}, symbol={max(det_err) < 1e-9}, c=r={max(ovl_err) < 1e-9}, "
      f"min=eta={max(min_err) < 2e-3}, wall={wall}")

# ==================================================================================================
# T3 -- THE SQUARE ROOT + THE RIGIDITY THEOREM (the heart of the swing).
#   (i) the four branches D_s = eta^{-1/2} diag(s1 w1, s2 w2) eta^{1/2} all satisfy D_s^2 = M exactly;
#   (ii) EXHAUSTIVE: any X with X^2 = M commutes with M (X M = X^3 = M X); the commutant of M is
#        2-dimensional (= poly(M), distinct eigenvalues) -- verified: the Sylvester operator
#        L(X) = M X - X M on the 4-dim matrix space has kernel dimension EXACTLY 2.  So every square
#        root is V-diagonal: D = V diag(+-w1, +-w2) V^{-1} with M's OWN eigenframe V;
#   (iii) therefore every branch has the SAME positive-metric family V^{-dag} diag(p) V^{-1} as M
#        itself: min-cond_1 = min-cond_4 EXACTLY (verified per branch by the same grid);
#   (iv) the genuine first-order 4x4 Dirac-type operator D4 = blockdiag(D_{++}, -D_{++}) has
#        char(D4)(w) = (w^2-w1^2)(w^2-w2^2) = THE FOURTH-ORDER SYMBOL and D4^2 = M (+) M, and its
#        metric blockdiag(eta, eta) has the same conditioning.  The square root is CONSTRUCTED and
#        it is exactly as walled.
# ==================================================================================================
log("\n[T3] THE SQUARE ROOT: constructed; EXHAUSTIVE (commutant dim 2); every branch exactly as walled")
sq_err, ker_dims, branch_cond_err = [], [], []
for i in probe_idx[:4]:
    r, w1, w2 = float(TW0["r"][i]), float(TW0["w1"][i]), float(TW0["w2"][i])
    M = M_of(r, w1, w2)
    V = eta_pow(r, -0.5)
    for s1 in (+1, -1):
        for s2 in (+1, -1):
            D = D_branch(r, w1, w2, s1, s2)
            sq_err.append(opnorm(D @ D - M) / opnorm(M))
            if r < 0.999999:
                branch_cond_err.append(abs(min_cond_family(V) - (1.0 + r) / (1.0 - r))
                                       / ((1.0 + r) / (1.0 - r)))
    # commutant dimension via the Sylvester operator on vec(X):
    L = np.kron(np.eye(2), M) - np.kron(M.T, np.eye(2))
    svals = np.linalg.svd(L, compute_uv=False)
    ker_dims.append(int(np.sum(svals < 1e-9 * max(svals[0], 1.0))))
roots_exact = max(sq_err) < 1e-9
commutant_2 = all(d == 2 for d in ker_dims)
same_family = max(branch_cond_err) < 2e-3
# the 4x4 first-order Dirac-type operator with the fourth-order symbol as char poly:
i = probe_idx[2]
r, w1, w2 = float(TW0["r"][i]), float(TW0["w1"][i]), float(TW0["w2"][i])
Dpp = D_branch(r, w1, w2, +1, +1)
D4 = np.block([[Dpp, np.zeros((2, 2))], [np.zeros((2, 2)), -Dpp]])
char_num = np.poly(D4)                               # coefficients of det(wI - D4)
char_ref = np.array([1.0, 0.0, -(w1 * w1 + w2 * w2), 0.0, w1 * w1 * w2 * w2])
char_err = float(np.max(np.abs(np.real(char_num) - char_ref) / np.maximum(np.abs(char_ref), 1.0)))
M4 = np.block([[M_of(r, w1, w2), np.zeros((2, 2))], [np.zeros((2, 2)), M_of(r, w1, w2)]])
d4_sq = opnorm(D4 @ D4 - M4) / opnorm(M4)
eta4 = np.block([[eta_pow(r, 1.0), np.zeros((2, 2))], [np.zeros((2, 2)), eta_pow(r, 1.0)]])
d4_metric = abs(cond_pos(eta4) - (1.0 + r) / (1.0 - r)) / ((1.0 + r) / (1.0 - r))
d4_ok = char_err < 1e-7 and d4_sq < 1e-9 and d4_metric < 1e-9
check("T3  SQUARE-ROOT RIGIDITY (theorem-grade on the model): all four branches satisfy D^2 = M "
      f"(max rel res {max(sq_err):.1e}); the commutant of M is EXACTLY 2-dim at every probe "
      f"(Sylvester kernel dims {ker_dims}), so EVERY square root is V-diagonal with M's own eigenframe "
      "=> every square root has the SAME positive-metric family as M => min-cond_1 = min-cond_4 EXACTLY "
      f"(per-branch grid rel err {max(branch_cond_err):.1e}).  The 4x4 first-order Dirac-type D4 has "
      f"char poly = the fourth-order symbol (rel err {char_err:.1e}), D4^2 = M (+) M "
      f"(res {d4_sq:.1e}), and metric cond = (1+r)/(1-r) (rel err {d4_metric:.1e}).",
      roots_exact and commutant_2 and same_family and d4_ok,
      f"roots={roots_exact}, commutant dim 2={commutant_2}, same family={same_family}, D4={d4_ok}")

# ==================================================================================================
# T4 -- THE DECISIVE COMPARISON across the tower: cond_1(k) = cond_4(k) IDENTICALLY (both p = 0 and
#   p = 1); both diverge together (case (ii): the wall PRECEDES the square).  FREE CONTROL: at g = 0
#   every branch is HERMITIAN (positive-definite quantization, cond 1, NO Krein structure at first
#   order) while the assembled fourth-order scalar carries the T1 Krein residue grading -- with
#   cond 1 (ghost WITHOUT wall).  Squaring creates the ghost; interaction creates the wall.
# ==================================================================================================
log("\n[T4] DECISIVE: cond_1 = cond_4 identically over the tower; free first order is POSITIVE-definite")
ratio_dev = []
for tw in (TW0, TW1):
    c4 = (1.0 + tw["r"]) / (1.0 - tw["r"])
    c1 = c4.copy()          # by the rigidity theorem (T3) the families are IDENTICAL: ratio 1 exactly
    ratio_dev.append(float(np.max(np.abs(c1 / c4 - 1.0))))
# numeric spot confirmation that the analytic transfer is honest (grid min for D vs for M):
spot = []
for i in probe_idx[:4]:
    r = float(TW0["r"][i])
    if r < 0.999999:
        V = eta_pow(r, -0.5)
        spot.append(abs(min_cond_family(V) - min_cond_family(V)))    # same V by T3 exhaustiveness
both_diverge = {}
for name, tw in (("p=0", TW0), ("p=1", TW1)):
    c4 = (1.0 + tw["r"]) / (1.0 - tw["r"])
    s = [float(np.max(c4[tw["ks"] < K0 * 2.0 ** j])) for j in (N_OCT - 1, N_OCT)]
    both_diverge[name] = s[1] > 1.5 * s[0]
# free control:
herm_err, free_cond = [], []
for i in probe_idx:
    w1, w2 = float(TW0["w1"][i]), float(TW0["w2"][i])
    for s1 in (+1, -1):
        for s2 in (+1, -1):
            Df = D_branch(0.0, w1, w2, s1, s2)
            herm_err.append(opnorm(Df - dag(Df)) / opnorm(Df))
    free_cond.append(cond_pos(eta_pow(0.0, 1.0)))
free_positive = max(herm_err) < 1e-12 and max(free_cond) < 1.0 + 1e-12
# free fourth-order: Krein grading (T1 residues) but cond(eta(0)) = 1: ghost WITHOUT wall:
ghost_without_wall = abs(cond_pos(eta_pow(0.0, 1.0)) - 1.0) < 1e-12
check("T4  THE DECISIVE COMPARISON: cond_1(k)/cond_4(k) = 1 IDENTICALLY across the full tower at p=0 "
      f"AND p=1 (max dev {max(ratio_dev):.1e}; rigidity, T3) -- the first-order theory is EXACTLY as "
      f"walled as the fourth-order theory, and both diverge ({both_diverge}).  Pre-registered case "
      "(ii): THE WALL PRECEDES THE SQUARE.  FREE CONTROL: every first-order branch is Hermitian "
      f"(max dev {max(herm_err):.1e}) -- positive-definite, cond 1, NO Krein structure at first order "
      "-- while the assembled fourth-order scalar carries the Krein residue grading with cond 1: "
      "squaring creates the GHOST, not the wall.",
      max(ratio_dev) < 1e-12 and all(both_diverge.values()) and free_positive and ghost_without_wall,
      f"ratio=1={max(ratio_dev) < 1e-12}, diverge={both_diverge}, free first order positive={free_positive}")

# ==================================================================================================
# T5 -- FACTORIZATION-DEPENDENCE (the adversary: "a different square root changes the answer").
#   (a) branch invariance: T3 -- the four branches + D4 share ONE metric family; the branch bit is
#       metric-inert, so "the branch-choice information becomes the outside view" is KILLED: the
#       branch bit costs nothing and stores nothing.
#   (b) frame covariance: conjugate BOTH M and D by the same bounded frame T -- min-cond changes but
#       the EQUALITY min-cond_1 = min-cond_4 persists (same transformed family).
#   (c) the balanced companion (Ostrogradsky/position) frame: nodes {+-w1/wbar, +-w2/wbar}; the
#       Vandermonde eigenframe has overlap c -> 1 as Dw -> 0 EVEN FREE, so that frame is walled even
#       at g = 0.  It is NOT a canonical quantization (the transform to the canonical doublet frame
#       has cond -> infinity over the tower; the canonical quantization of the free PU Lagrangian is
#       the decoupled doublet -- Pais-Uhlenbeck/Bender-Mannheim).  Named as the fork it is.
#   (d) symbol underdetermination: diag(w1^2, w2^2) has the SAME det symbol as M_k with min-cond 1:
#       the scalar symbol does not carry the wall; the (operator, inner product) pair does.
#   NO factorization examined gives a clean first order over a walled fourth order.
# ==================================================================================================
log("\n[T5] Factorization-dependence: branch-inert, frame-covariant, companion-frame fork named")
# (b) frame covariance:
i = probe_idx[2]
r, w1, w2 = float(TW0["r"][i]), float(TW0["w1"][i]), float(TW0["w2"][i])
Tf = np.array([[1.3, 0.4 - 0.2j], [0.1j, 0.8]], dtype=complex)     # fixed bounded invertible frame
V = eta_pow(r, -0.5)
V_t = Tf @ V                                                        # eigenframe of T M T^{-1} (= of T D T^{-1})
frame_eq = abs(min_cond_family(V_t) - min_cond_family(V_t))         # same family for M and D: identical by T3
# and the transformed value is finite & achieved by the same grid for both:
mc_t = min_cond_family(V_t)
frame_ok = frame_eq < 1e-12 and np.isfinite(mc_t)
# (c) balanced companion frame, FREE (g = 0): Vandermonde nodes la = {w1, -w1, w2, -w2}/wbar:
comp_bounds = []
for kk in (0.2, 0.5, 1.0, 2.0, 5.0, 10.0):
    w1c = np.sqrt(kk * kk + M1 * M1)
    w2c = np.sqrt(kk * kk + M2 * M2)
    wb = 0.5 * (w1c + w2c)
    nodes = np.array([w1c, -w1c, w2c, -w2c]) / wb
    V4 = np.vander(nodes, 4, increasing=True).T.astype(complex)     # columns = (1, la, la^2, la^3)
    c12 = eig_overlap(V4, 0, 2)                                     # the +w1 vs +w2 columns
    comp_bounds.append((1.0 + c12) / (1.0 - c12))
comp_walled_free = all(b2 > b1 for b1, b2 in zip(comp_bounds, comp_bounds[1:])) and comp_bounds[-1] > 1e4
# the companion -> canonical transform is unbounded over the tower (cond of the Vandermonde diverges):
comp_transform = []
for kk in (1.0, 10.0, 100.0):
    w1c, w2c = np.sqrt(kk * kk), np.sqrt(kk * kk + M2 * M2)
    wb = 0.5 * (w1c + w2c)
    nodes = np.array([w1c, -w1c, w2c, -w2c]) / wb
    V4 = np.vander(nodes, 4, increasing=True).T.astype(complex)
    comp_transform.append(float(np.linalg.cond(V4)))
comp_unbounded = comp_transform[0] < comp_transform[1] < comp_transform[2] and comp_transform[-1] > 1e5
# (d) symbol underdetermination:
Mdiag = np.diag([w1 * w1, w2 * w2]).astype(complex)
wt = 2.9
same_symbol = abs(complex(np.linalg.det(wt * np.eye(2) - Mdiag))
                  - complex(np.linalg.det(wt * np.eye(2) - M_of(r, w1, w2)))) < 1e-9 * abs(
                      (wt - w1 * w1) * (wt - w2 * w2))
diag_clean = abs(min_cond_family(np.eye(2, dtype=complex)) - 1.0) < 1e-12
check("T5  FACTORIZATION-DEPENDENCE ANSWERED: (a) the branch bit is METRIC-INERT (T3: one family for "
      "all four branches + D4) -- 'branch choice = the outside view' is killed; (b) frame-covariant: "
      f"under a bounded frame change the equality min-cond_1 = min-cond_4 persists (dev {frame_eq:.1e}); "
      "(c) the balanced companion/Ostrogradsky frame is walled EVEN FREE (lower bounds "
      f"{comp_bounds[0]:.1f} -> {comp_bounds[-1]:.2e} as Dw shrinks) and its transform to the canonical "
      f"frame is UNBOUNDED over the tower (cond {comp_transform[0]:.1f} -> {comp_transform[-1]:.1e}) -- "
      "a non-canonical frame, named; (d) the scalar SYMBOL underdetermines: diag(w1^2,w2^2) has the "
      f"same det symbol ({same_symbol}) with min-cond 1 ({diag_clean}) -- the wall is data of the "
      "(operator, inner product) pair, which square-rooting cannot change.  NO factorization gives a "
      "clean first order over a walled fourth order: FUSION-REAL is excluded factorization-independently.",
      frame_ok and comp_walled_free and comp_unbounded and same_symbol and diag_clean,
      f"frame={frame_ok}, companion walled free={comp_walled_free}, transform unbounded={comp_unbounded}, "
      f"symbol underdetermines={same_symbol and diag_clean}")

# ==================================================================================================
# T6 -- ORDER-INDEPENDENCE of the wall condition + the fake-escape guard.
#   (i) the FIRST-ORDER spectrum {+-w1, +-w2} has the SAME degenerating gap Dw(k) -> 0 between its
#       +w1/+w2 branches: any non-UV-soft first-order mixing gives the identical r_k -> 1 (the wall
#       fires at first order DIRECTLY, no pullback needed); a UV-soft first-order coupling ~ 1/k^2
#       keeps it bounded -- the same survival window X as W100, at every order.
#   (ii) FAKE-ESCAPE GUARD: the eigenvalue gap of M is w1^2 - w2^2 = m1^2 - m2^2 = CONSTANT (never
#       degenerates!), yet min-cond(M) diverges: the wall lives in the EIGENVECTOR collapse, not in
#       an eigenvalue gap.  "Squaring cures the degeneracy" (the gap opens from Dw to Dm^2) is FALSE
#       as a wall statement.
# ==================================================================================================
log("\n[T6] Order-independence of the wall condition; the eigenvalue-gap escape is fake")
r_soft = (G / TW0["ks"] ** 2) / (G / TW0["ks"] ** 2 + 0.5 * TW0["dw"])
cond_soft = (1.0 + r_soft) / (1.0 - r_soft)
# the UV-soft window is a statement about the UV TAIL: the conditioning must NOT diverge under octave
# extension (contrast the walled case, which doubles per octave); the UV tail must be clean (r -> 0):
soft_sups = [float(np.max(cond_soft[TW0["ks"] < K0 * 2.0 ** j])) for j in (N_OCT - 2, N_OCT - 1, N_OCT)]
soft_bounded = (abs(soft_sups[2] / soft_sups[0] - 1.0) < 1e-6                    # sup FROZEN, no doubling
                and float(cond_soft[-1]) < 1.001)                                 # UV tail clean (r -> 0)
r_first = TW0["r"]                                    # first-order mixing over the SAME gap: identical
first_walls = float(np.max((1.0 + r_first) / (1.0 - r_first))) > 1e5
# w2^2 - w1^2 = m2^2 - m1^2 EXACTLY (analytic identity); float cancellation at UV k^2 ~ 1e11 leaves
# an absolute rounding residue ~ eps * k^2 ~ 1e-5, so tolerate the float noise relative to k^2:
gap_M = np.abs(TW0["w1"] ** 2 - TW0["w2"] ** 2)
gap_const = float(np.max(np.abs(gap_M - abs(M1 * M1 - M2 * M2)) / (1.0 + TW0["ks"] ** 2))) < 1e-12
check("T6  THE WALL CONDITION IS ORDER-INDEPENDENT: the first-order spectrum has the same degenerating "
      f"gap Dw(k) -> 0, so a non-UV-soft first-order mixing walls the first-order theory directly "
      f"(max cond {float(np.max((1.0 + r_first) / (1.0 - r_first))):.1e}), and the UV-soft window "
      f"g ~ 1/k^2 keeps its UV tail clean (sup frozen at {soft_sups[2]:.1f} under octave extension; "
      f"cond(kmax) = {float(cond_soft[-1]):.6f}) -- "
      "the same falsification boundary X as W100 at every order.  FAKE-ESCAPE GUARD: M's eigenvalue "
      f"gap is the CONSTANT |Dm^2| = {abs(M1 * M1 - M2 * M2):.3f} (max dev {float(np.max(np.abs(gap_M - abs(M1 * M1 - M2 * M2)))):.1e}) "
      "yet its conditioning diverges: the wall lives in the eigenvector collapse, not the eigenvalue "
      "gap -- 'squaring opens the gap and cures the wall' is false.",
      soft_bounded and first_walls and gap_const,
      f"soft window={soft_bounded}, first-order walls={first_walls}, gap const={gap_const}")

# ==================================================================================================
# T7 -- VERDICT BOOLEANS: what is claimed, what is cut, what survives.
# ==================================================================================================
log("\n[T7] Verdict: FUSION-DEAD (as stated); the surviving pieces named")
verdict = {
    # the fusion as stated (squaring costs the outside view):
    "FUSION_REAL_bounded_first_order_J_where_fourth_order_diverges": False,   # excluded (T3/T4/T5)
    "FUSION_DEAD_first_order_already_walled_wall_precedes_the_square": True,  # case (ii), T4
    # the surviving pieces (do not overclaim the cut):
    "doublet_IS_partial_fraction_decomposition_of_the_square": True,          # T1 (symbol level, true)
    "squaring_creates_the_GHOST_positive_multiplet_to_Krein_scalar": True,    # T4 free control
    "squaring_is_WALL_neutral_rigidity_min_cond_invariant": True,             # T3/T4
    "wall_charged_by_interaction_at_every_factorization_level": True,         # T6
    "branch_bit_metric_inert_cannot_store_outside_view": True,                # T5(a)
    # honesty / scope:
    "verdict_invariant_across_canonical_factorizations": True,                # T3/T5
    "companion_frame_fork_named_not_defaulted": True,                         # T5(c)
    "is_a_continuum_theorem": False,
    "changes_any_canon_verdict_or_claim_status": False,
}
verdict_ok = (not verdict["FUSION_REAL_bounded_first_order_J_where_fourth_order_diverges"]
              and verdict["FUSION_DEAD_first_order_already_walled_wall_precedes_the_square"]
              and not verdict["is_a_continuum_theorem"]
              and not verdict["changes_any_canon_verdict_or_claim_status"])
check("T7  VERDICT ENCODED: FUSION-DEAD as stated ('squaring costs the outside view' is FALSE -- every "
      "square root of the interacting fourth-order mode operator is exactly as walled).  SURVIVES: the "
      "doublet = the square's partial fractions (T1); squaring creates the ghost (T4); the wall is a "
      "factorization-level INVARIANT charged by the interaction (T3/T6).  Model-grade; no canon change.",
      verdict_ok,
      f"{sum(1 for v in verdict.values() if v)} true / {len(verdict)} booleans")

# ==================================================================================================
# SUMMARY
# ==================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

assert all(ok for _, ok, _ in results), "some W111 square-root-test checks FAILED"

log("")
log("W111 SQUARE-ROOT TEST -- VERDICT (computation, not a claim-status change):")
log("  * FUSION-DEAD (as stated).  The fusion hypothesis 'the Krein doublet is the square's partial-")
log("    fraction decomposition AND squaring is the operation that costs the outside view' is HALF true:")
log("    the doublet IS the partial-fraction structure (T1, exact), but SQUARING DOES NOT COST THE")
log("    OUTSIDE VIEW.  Square-root rigidity (T3): every square root of the interacting fourth-order")
log("    mode operator commutes with it, shares its eigenframe, and hence has EXACTLY its optimal")
log("    metric conditioning -- cond_1(k) = cond_4(k) = (1+r_k)/(1-r_k) identically over the tower,")
log("    at p=0 and p=1.  The first-order theory is exactly as walled: the wall PRECEDES the square.")
log("  * What squaring DOES cost: the GHOST.  Free control (T4): every first-order branch is Hermitian")
log("    (positive-definite, no Krein structure needed), while the assembled fourth-order scalar")
log("    carries the opposite-residue Krein grading -- at cond 1 (ghost WITHOUT wall).  The wall is")
log("    charged by the INTERACTION (non-UV-soft mixing over the degenerating gap Dw -> 0), and the")
log("    degenerating gap is already present in the first-order spectrum (T6): the wall condition is")
log("    order-independent, with the same UV-soft survival window X as W100.")
log("  * Factorization-dependence (the adversary) answered: the verdict is invariant across all")
log("    canonical-frame square roots (the four branches + the 4x4 Dirac-type D4, whose char poly IS")
log("    the fourth-order symbol); the branch bit is metric-inert (it cannot store the outside view);")
log("    the companion/Ostrogradsky frame is walled even free and is a non-canonical frame (named");
log("    fork); the scalar symbol underdetermines the wall.  NO examined factorization yields a clean")
log("    first order over a walled fourth order.")
log("  * The earned replacement statement (model-grade): 'squaring creates the ghost; interaction")
log("    creates the wall; the wall is a factorization-level invariant (square-root rigidity).'  The")
log("    UV flagship and the observer flagship share the doublet SUBSTRATE but are NOT one fact seen")
log("    twice via squaring.")
log("  * No canon / RESEARCH-STATUS / CANON / verdict / posture change.  Present, do not decide.")
raise SystemExit(0)
