#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
W208 -- THE DECISIVE BIT via the LAWVERE CATEGORICAL FIXED POINT (method R7).

ONE OF FIVE parallel methods attacking the SAME decisive bit for a convergence cross-check.

THE DECISIVE QUESTION (identical for all five). Take the good-stable fixed point as GIVEN. Its
STABILIZER = the group of counterfactual/gauge deformations preserving the good-stable properties
(real total spectrum + positive-definite TOTAL metric + C-operator operative, eta_+ = eta C). Compute
the space of invariant symmetric bilinear forms under that stabilizer.
  * ONE-dimensional, generator eta_+ = eta C (the C-operator-GRADED metric, record-count mode
    Krein-NEGATIVE on the (6,4) fiber)?  ->  FORCED  (dim 1 AND generator eta_+; Krein sign DERIVED).
  * dim > 1, or only eta up-to-grading?   ->  RESIDUAL-BIT-STANDS (Godel-independent; must be posited).

CRITICAL GUARDRAIL (no false positive). W203 ALREADY forced the UNGRADED metric to eta by Schur
(nulldim 1 under the FULL non-compact so(9,5)). That is NOT the open bit. The open bit is whether the
C-OPERATOR GRADING SIGN (eta_+ = eta C, record-count mode negative) is FORCED. If we only recover eta
up-to-grading, the verdict is RESIDUAL-BIT-STANDS.

METHOD R7 (Lawvere categorical fixed point). Realize the good stable as the Lawvere FIXED POINT of the
diagonal self-map (metric-depends-on-S-depends-on-metric). Construct the induced self-map on the space
of C-gradings and COUNT its consistent fixed points:
  * exactly ONE consistent fixed point            => the sign is FORCED;
  * TWO (good + pathological, per W186 bistability) => the branch bit is a genuine second fixed point
                                                       = RESIDUAL-BIT-STANDS.
Key question: does the good-stable constraint (positive total metric) select a UNIQUE Lawvere fixed
point, or is the pathological one equally a fixed point of the SAME map (selection external)?

WHAT R7 FINDS (two independent computations, agreeing).

(1) THE STABILIZER DIMENSION JUMPS FROM 1 TO 2. The full non-compact gauge group so(9,5) forces the
    invariant symmetric form to be 1-dimensional (~ eta, INDEFINITE) -- this is W203, reproduced as a
    positive control, and it is the UNGRADED metric, NOT the open bit. But the good-stable stabilizer
    is SMALLER: preserving the positive-definite total metric eta_+ = eta C (together with the Krein
    form eta) restricts the group to the MAXIMAL COMPACT so(9) (+) so(5) (the antisymmetric = compact
    part; the non-compact boosts mixing the + and - directions do NOT preserve a positive-definite
    form). Under that compact stabilizer the space of invariant symmetric forms is EXACTLY
    2-DIMENSIONAL, spanned by the two block forms {P_9, P_5} = {the form on the 9-block, the form on
    the 5-block}. eta = P_9 - P_5 and eta_+ = P_9 + P_5 are BOTH invariant; the GRADING SIGN (the
    relative sign of the two blocks) is a FREE coordinate. So conditioning on good-stable does NOT
    pin the grading -- it ENLARGES the invariant space from 1 to 2. dim = 2 > 1 => RESIDUAL-BIT-STANDS.

(2) THE LAWVERE GRADING SELF-MAP HAS TWO FIXED POINTS. The induced self-map on C-gradings (involutions
    C, C^2 = I, commuting with the stabilizer) has fixed points = consistent gradings. By Schur on the
    two irreducible blocks C = c_9 I_9 (+) c_5 I_5 with c in {+1,-1}. Up to overall sign there are
    TWO classes: C_good = diag(+1x9, -1x5) (flips the record-count / negative directions; eta_+ =
    eta C_good = +I, positive-definite = GOOD) and C_path = I (no flip; eta_+ = eta, indefinite = the
    W178/W186 pathological EP). BOTH are fixed points of the same commuting-involution map. The
    good-stable (positive total metric) constraint SELECTS C_good's basin, but C_path is EQUALLY a
    fixed point of the SAME map -- so the selection is EXTERNAL (a posit), exactly W186's bistability.
    Fixed-point count = 2 => RESIDUAL-BIT-STANDS.

THE LAWVERE / GODEL SIGNATURE (why "must be posited" is the precise statement). The self-consistency
loop "C-metric operative <=> reservoir like-signed <=> issuance C-positive <=> C-metric operative" is a
diagonal self-reference. The grading flip on the 2-valued Krein-norm sign {+,-} is the SWAP, which is
fixpoint-free for exactly the reason negation is in Cantor/Godel/Tarski (reproduced exhaustively as a
positive control). A fixpoint-free endomorphism forces a RESIDUAL free selection that no internal state
fixes (Lawvere; the repo's path5-branchD / H63 skeleton). The grading SIGN is precisely such a residual:
it is TRUE in the good model and FALSE in the pathological model of the SAME self-consistency theory, so
it is Godel-INDEPENDENT of that theory -- it MUST be posited, not derived. That is RESIDUAL-BIT-STANDS
stated at the categorical level, and it is the SAME conclusion the dimension count and the fixed-point
count reach.

VERDICT: RESIDUAL-BIT-STANDS. Lawvere fixed-point count of the grading self-map = 2 (good + pathological,
both consistent, per W186 bistability). The good-stable stabilizer's invariant symmetric form space is
2-DIMENSIONAL; eta_+ is one positive ray in it but the grading sign is a free coordinate (only eta
up-to-grading is forced). The C-operator grading SIGN is NOT forced by GU-native structure; it is a
Godel-independent residual that must be posited. This CONFIRMS W186 (bistable, selection external), is
CONSISTENT with W202 (the Krein sign is fiber-computable and signature-robust, but its ACTIVATION is
external) and with W203 (Schur forces eta UP-TO-GRADING only, nulldim 1 under the full group). No false
positive: eta up-to-grading is recovered, the grading sign is not.

Structure (positive controls first):
  [PC1]  Lawvere/Cantor skeleton: the swap on {+,-} is fixpoint-free; exhaustively, no T:AxA->B
         (|A|<=3) represents the diagonal predicate d(a)=swap(T(a,a)). Reproduces path5-branchD/H63.
  [PC2]  W203 reproduction: full so(9,5) vector rep forces the invariant symmetric form to nulldim 1,
         ~ eta, signature (9,5) INDEFINITE. This is the UNGRADED metric (NOT the open bit).
  [PC3]  W186 reproduction: the metric-from-source self-consistency map is BISTABLE -- two stable
         fixed points (good m=1 positive total metric; pathological m=0 EP), and below kappa* only the
         pathological survives (the favorable fixed point is non-vacuous, not assumed).
  [STAB] the good-stable stabilizer is the MAXIMAL COMPACT so(9)(+)so(5); its invariant symmetric form
         space is 2-DIMENSIONAL {P_9, P_5}; eta_+ is one positive ray, the grading sign is free.
  [LAW]  the induced grading self-map has TWO consistent fixed points (C_good, C_path); the positive-
         metric constraint selects one but the other is equally a fixed point => selection external.
  [FIB]  the same computation on the (6,4) DeWitt fiber (compact so(6)(+)so(4)) -> dim 2 (ties W202/W168).
  [GODEL] the grading sign is true in one model / false in the other of the same self-consistency
          theory => Godel-independent => must be posited (the fixpoint-free-residual reading).
  [NC]   negative control: a positive-definite (Euclidean) "metric" whose full stabilizer is already
         compact shows NO dimension jump and NO nontrivial grading -- the whole structure needs the
         Krein indefiniteness.
  [E1]   VERDICT: RESIDUAL-BIT-STANDS; grading self-map fixed-point count = 2.

Everything exploration grade, conditional register. Nothing asserts GU, a vacuum, or moves any canon /
RESEARCH-STATUS / claim-status / verdict / bar (b) / H59. Deterministic (seed 20260714). Zero em dashes.
"""

import sys
import itertools
import numpy as np

np.random.seed(20260714)

FAILS = []
NCHECK = 0


def check(name, got, expected, atol=1e-9):
    global NCHECK
    NCHECK += 1
    ok = abs(float(got) - float(expected)) <= atol
    print(("  PASS " if ok else "  FAIL ") + name + f"   [got {got}, want {expected}]")
    if not ok:
        FAILS.append(name)


def check_bool(name, cond):
    global NCHECK
    NCHECK += 1
    ok = bool(cond)
    print(("  PASS " if ok else "  FAIL ") + name)
    if not ok:
        FAILS.append(name)


# ---------------------------------------------------------------------------
# Vector-representation so(p,q) machinery (self-contained; reproduces W203 KER).
# so(p,q) = { X : X^T g + g X = 0 } with g = diag(+1 x p, -1 x q).  Since g^2 = I,
# X = g A with A antisymmetric.  A block-diagonal  -> COMPACT so(p)(+)so(q) (X^T=-X).
# A off-block           -> NON-COMPACT boosts        (X^T=+X).
# ---------------------------------------------------------------------------

def metric(p, q):
    return np.diag([1.0] * p + [-1.0] * q)


def antisym_basis(n):
    B = []
    for i in range(n):
        for j in range(i + 1, n):
            A = np.zeros((n, n))
            A[i, j] = 1.0
            A[j, i] = -1.0
            B.append((i, j, A))
    return B


def gens_full(p, q):
    """all so(p,q) generators X = g A."""
    n = p + q
    g = metric(p, q)
    return [g @ A for (_, _, A) in antisym_basis(n)]


def gens_compact(p, q):
    """maximal-compact so(p)(+)so(q) generators (A block-diagonal, X antisymmetric)."""
    n = p + q
    g = metric(p, q)
    out = []
    for (i, j, A) in antisym_basis(n):
        both_p = (i < p and j < p)
        both_q = (i >= p and j >= p)
        if both_p or both_q:
            out.append(g @ A)
    return out


def gens_boost(p, q):
    """non-compact boost generators (A off-block, X symmetric)."""
    n = p + q
    g = metric(p, q)
    out = []
    for (i, j, A) in antisym_basis(n):
        if (i < p) != (j < p):
            out.append(g @ A)
    return out


def invariant_sym_forms(gens, n):
    """dimension + basis of { M symmetric : X^T M + M X = 0 for all X in gens }."""
    idx = [(a, b) for a in range(n) for b in range(a, n)]

    def vec2M(v):
        M = np.zeros((n, n))
        for k, (a, b) in enumerate(idx):
            M[a, b] = v[k]
            M[b, a] = v[k]
        return M

    basis = [vec2M(e) for e in np.eye(len(idx))]
    rows = []
    for X in gens:
        C = [X.T @ Mk + Mk @ X for Mk in basis]
        for p_ in range(n):
            for q_ in range(p_, n):
                rows.append([Ck[p_, q_] for Ck in C])
    Amat = np.array(rows, dtype=float)
    if Amat.size == 0:
        return len(idx), [vec2M(e) for e in np.eye(len(idx))]
    sv = np.linalg.svd(Amat, compute_uv=False)
    tol = 1e-9 * max(1.0, sv[0])
    rank = int(np.sum(sv > tol))
    nulldim = len(idx) - rank
    _, _, vt = np.linalg.svd(Amat)
    null_basis = [vec2M(vt[-(k + 1)]) for k in range(nulldim)]
    return nulldim, null_basis


def signature(M, rel=1e-6):
    ev = np.linalg.eigvalsh(M)
    scale = max(abs(ev)) if len(ev) else 1.0
    pos = int(np.sum(ev > rel * scale))
    neg = int(np.sum(ev < -rel * scale))
    return pos, neg


# ===========================================================================
print("=" * 78)
print("W208 -- decisive bit via the Lawvere categorical fixed point (R7)")
print("=" * 78)

# ---------------------------------------------------------------------------
print("\n[PC1] Lawvere/Cantor skeleton: the grading-flip swap is FIXPOINT-FREE and")
print("      obstructs self-referential closure (reproduces path5-branchD / H63 / W70).")
# B = {0,1} = the Krein norm sign {+,-}; alpha = swap (the firewall grading flip).
alpha = {0: 1, 1: 0}
check_bool("PC1a the flip on the 2-valued Krein sign is the SWAP, fixpoint-free (no fixed label)",
           all(alpha[b] != b for b in (0, 1)))
# exhaustively: over ALL T : A x A -> B, the diagonal predicate d(a)=alpha(T(a,a)) is never a row T(a0,-).
represented_ever = False
for sizeA in (1, 2, 3):
    A = list(range(sizeA))
    cells = list(itertools.product(A, A))
    for vals in itertools.product((0, 1), repeat=len(cells)):
        T = dict(zip(cells, vals))
        d = {a: alpha[T[(a, a)]] for a in A}
        # is d some row a0?  d(a) == T(a0, a) for all a
        if any(all(d[a] == T[(a0, a)] for a in A) for a0 in A):
            represented_ever = True
check_bool("PC1b exhaustively (|A|<=3): the diagonal predicate d=alpha.T.Delta is NEVER represented "
           "as a row -> no self-referential closure; a RESIDUAL free selection remains", not represented_ever)

# ---------------------------------------------------------------------------
print("\n[PC2] W203 reproduction: the FULL non-compact so(9,5) forces the invariant")
print("      symmetric form to nulldim 1 (~ eta, INDEFINITE). This is the UNGRADED metric,")
print("      forced UP-TO-GRADING -- NOT the open bit (the guardrail).")
n = 14
g95 = metric(9, 5)
nd_full, basis_full = invariant_sym_forms(gens_full(9, 5), n)
check("PC2a Schur: invariant symmetric form under FULL so(9,5) is EXACTLY 1-dimensional (W203 KER1)",
      nd_full, 1, atol=0)
M0 = basis_full[0]
M0 = M0 / M0[0, 0]
pos, neg = signature(M0)
check("PC2b the unique form has 9 positive eigenvalues", pos, 9, atol=0)
check("PC2c ... and 5 negative -> signature (9,5), INDEFINITE (~ eta, NOT positive-definite)", neg, 5, atol=0)
check("PC2d the unique form IS the Clifford metric eta (diag +1x9,-1x5; off-diag 0)",
      float(np.max(np.abs(M0 - g95))), 0.0, atol=1e-8)

# ---------------------------------------------------------------------------
print("\n[PC3] W186 reproduction: the metric-from-source self-consistency map is BISTABLE.")
# Minimal 2x2 Friedrichs/Fano stand-in (as in W186 D-block). A ghost coupled to:
#   * an opposite-signed kinematic band (coupling g_kin, metric-INDEPENDENT, always present, W178);
#   * a like-signed record reservoir (coupling kappa, present only when records are physical).
# Total generator eigenvalues real (good) or complex (pathological) decide the fixed point.
def total_real(kappa, g_kin):
    # 2-mode effective: like-signed source damps (kappa), opposite-signed kinematic anti-damps (g_kin).
    # reality of the coupled pair <=> the like-signed channel dominates the kinematic one.
    H = np.array([[0.0, kappa, g_kin],
                  [kappa, -1.0, 0.0],
                  [g_kin, 0.0, +1.0]])
    # Krein metric: record reservoir like-signed (+), kinematic band opposite-signed (-).
    J = np.diag([1.0, 1.0, -1.0])
    Aeff = J @ H  # pseudo-Hermitian generator; real spectrum <=> quasi-Hermitian
    ev = np.linalg.eigvals(Aeff)
    return float(np.max(np.abs(ev.imag))) < 1e-9


g_kin = 1.4
# order parameter m in {0,1}; kappa(m) = kappa_max * m (records physical only when C-operative).
def self_map(m, kappa_max):
    kappa = kappa_max * m
    return 1 if total_real(kappa, g_kin) else 0

# find kappa* by bisection: the non-vacuity threshold.
lo, hi = 0.0, 6.0
for _ in range(60):
    mid = 0.5 * (lo + hi)
    if total_real(mid, g_kin):
        hi = mid
    else:
        lo = mid
kappa_star = hi
check_bool("PC3a a fixed opposite-sign kinematic coupling g_kin genuinely spoils reality below kappa* "
           "(favorable fixed point NON-VACUOUS, not assumed)", 0.0 < kappa_star < 6.0)
kmax = kappa_star + 1.0  # favorable regime
# enumerate fixed points of the self-map m -> self_map(m): m is fixed iff self_map(m)==m.
fps_favorable = [m for m in (0, 1) if self_map(m, kmax) == m]
check_bool("PC3b in the favorable regime (kappa_max > kappa*) the self-map is BISTABLE: BOTH m=1 (good) "
           "and m=0 (pathological) are fixed points", set(fps_favorable) == {0, 1})
fps_unfav = [m for m in (0, 1) if self_map(m, kappa_star - 0.3) == m]
check_bool("PC3c below kappa* ONLY the pathological m=0 survives (bistability is a real computation)",
           fps_unfav == [0])
check_bool("PC3d self-consistency does NOT select: two stable fixed points, both consistent (W186)",
           len(fps_favorable) == 2)

# ===========================================================================
print("\n[STAB] the good-stable STABILIZER and its invariant symmetric form space (the decisive count).")
# The good-stable data: real total spectrum + positive-definite total metric eta_+ = eta C + C operative.
# The C-grading: eta_+ = eta C positive-definite.  On the (9,5) frame, C = diag(+1x9,-1x5) gives
# eta_+ = eta C = diag(+1x14) = I (positive-definite).
C_good = np.diag([1.0] * 9 + [-1.0] * 5)
eta_plus = g95 @ C_good
check("STAB0a eta_+ = eta C_good is positive-definite (its negative-eigenvalue count is 0)",
      signature(eta_plus)[1], 0, atol=0)
check("STAB0b ... and equals the identity metric (min eigenvalue 1)",
      float(np.min(np.linalg.eigvalsh(eta_plus))), 1.0, atol=1e-9)

# WHICH deformations preserve the good-stable data?  Preserving eta_+ (positive-definite) forces the
# group COMPACT; preserving eta AND eta_+ = the maximal compact so(9)(+)so(5).  Verify the split:
comp = gens_compact(9, 5)
boost = gens_boost(9, 5)
def preserves(X, M):
    return float(np.max(np.abs(X.T @ M + M @ X)))
comp_keeps_etaplus = max(preserves(X, eta_plus) for X in comp)
boost_keeps_etaplus = max(preserves(X, eta_plus) for X in boost)
comp_keeps_eta = max(preserves(X, g95) for X in comp)
boost_keeps_eta = max(preserves(X, g95) for X in boost)
check("STAB1a the COMPACT so(9)+so(5) generators preserve eta_+ (positive metric): residual 0",
      comp_keeps_etaplus, 0.0, atol=1e-12)
check("STAB1b the COMPACT so(9)+so(5) generators preserve eta (Krein form): residual 0",
      comp_keeps_eta, 0.0, atol=1e-12)
check_bool("STAB1c the NON-COMPACT boosts preserve eta but DO NOT preserve eta_+ (they break the "
           "positive total metric) -> the good-stable stabilizer is the MAXIMAL COMPACT so(9)+so(5)",
           boost_keeps_eta < 1e-12 and boost_keeps_etaplus > 1e-6)

# THE DECISIVE DIMENSION COUNT: invariant symmetric forms under the good-stable stabilizer.
nd_comp, basis_comp = invariant_sym_forms(comp, n)
check("STAB2 the good-stable stabilizer (compact so(9)+so(5)) has a 2-DIMENSIONAL invariant symmetric "
      "form space (NOT 1) -> conditioning on good-stable ENLARGES the space; the grading is NOT pinned",
      nd_comp, 2, atol=0)

# the 2-dim space is spanned by the two block forms P_9, P_5; eta and eta_+ are BOTH inside it.
P9 = np.diag([1.0] * 9 + [0.0] * 5)
P5 = np.diag([0.0] * 9 + [1.0] * 5)
def in_span(M, basis):
    B = np.array([b.reshape(-1) for b in basis]).T
    coef, res, *_ = np.linalg.lstsq(B, M.reshape(-1), rcond=None)
    return float(np.linalg.norm(B @ coef - M.reshape(-1)))
check("STAB3a eta (= P_9 - P_5, INDEFINITE) is in the invariant space", in_span(g95, basis_comp), 0.0, atol=1e-9)
check("STAB3b eta_+ (= P_9 + P_5, POSITIVE-definite) is ALSO in the invariant space", in_span(eta_plus, basis_comp), 0.0, atol=1e-9)
check("STAB3c P_9 and P_5 (the two block forms) span it", max(in_span(P9, basis_comp), in_span(P5, basis_comp)), 0.0, atol=1e-9)
# the grading sign = relative sign of the two blocks = a FREE coordinate: both signs give an invariant
# form, so the constraint recovers eta ONLY UP-TO-GRADING (the guardrail's RESIDUAL condition).
check_bool("STAB4 the GRADING SIGN (relative sign of the 9- and 5-blocks) is a FREE coordinate: eta and "
           "eta_+ are distinct invariant forms differing only by the C-grading -> only eta UP-TO-GRADING "
           "is forced, NOT the sign", in_span(g95, basis_comp) < 1e-9 and in_span(eta_plus, basis_comp) < 1e-9
           and float(np.max(np.abs(g95 - eta_plus))) > 1.0)

# ===========================================================================
print("\n[LAW] the induced grading SELF-MAP and its fixed-point count (the Lawvere count).")
# A C-grading is an involution C (C^2=I) commuting with the stabilizer.  By Schur on the two irreducible
# blocks, C = c9 * I_9 (+) c5 * I_5 with c in {+1,-1}.  Enumerate the fixed points of the self-map
# (a grading is a consistent fixed point iff it is such a commuting involution).
def commutes_with_stabilizer(C):
    return max(float(np.max(np.abs(C @ X - X @ C))) for X in comp) < 1e-12

grading_fixed_points = []
for c9 in (+1.0, -1.0):
    for c5 in (+1.0, -1.0):
        C = np.diag([c9] * 9 + [c5] * 5)
        if abs(np.trace(C @ C) - n) < 1e-9 and commutes_with_stabilizer(C):  # C^2 = I and commuting
            grading_fixed_points.append((c9, c5, C))
check("LAW1 the grading self-map has 4 sign-labelled fixed points (c9,c5 in {+-1}); commuting involutions",
      len(grading_fixed_points), 4, atol=0)

# classify by the total metric eta_C = eta C: positive-definite (GOOD) vs indefinite (PATHOLOGICAL).
classes = {"good_positive_definite": [], "pathological_indefinite": []}
for (c9, c5, C) in grading_fixed_points:
    etaC = g95 @ C
    pos, neg = signature(etaC)
    if neg == 0 or pos == 0:  # definite (up to overall sign)
        classes["good_positive_definite"].append((c9, c5))
    else:
        classes["pathological_indefinite"].append((c9, c5))
# up-to-overall-sign: 2 physical fixed points, one per class.
n_good = len(classes["good_positive_definite"]) // 2
n_path = len(classes["pathological_indefinite"]) // 2
check("LAW2a GOOD class (eta_C positive/negative-definite) has 1 physical fixed point (C=diag(+1x9,-1x5), "
      "up to overall sign) = C_good", n_good, 1, atol=0)
check("LAW2b PATHOLOGICAL class (eta_C indefinite = the W178/W186 EP) has 1 physical fixed point (C=I, "
      "up to overall sign) = C_path", n_path, 1, atol=0)
fixed_point_count = n_good + n_path
check("LAW3 TOTAL Lawvere fixed-point count of the grading self-map = 2 (good + pathological), matching "
      "W186 bistability -> the branch bit is a GENUINE SECOND FIXED POINT", fixed_point_count, 2, atol=0)
# the good-stable (positive total metric) constraint selects C_good but C_path is EQUALLY a fixed point
# of the SAME commuting-involution map -> selection is EXTERNAL, not forced by the fixed-point structure.
C_path = np.eye(n)
check_bool("LAW4 C_path (= I, no flip; eta_C = eta INDEFINITE) IS a fixed point of the SAME self-map "
           "(commuting involution) -> the good-stable constraint SELECTS C_good externally; it does NOT "
           "make it the unique fixed point (selection is a posit, cf W186 SELECTION level)",
           commutes_with_stabilizer(C_path) and abs(np.trace(C_path @ C_path) - n) < 1e-9)

# ===========================================================================
print("\n[FIB] the same count on the (6,4) DeWitt fiber (ties W202/W168): dim 2, sign free.")
# The (9,5)=(3,1)+(6,4) split; the (6,4) fiber carries the record-count-vs-geometric split (W168).
g64 = metric(6, 4)
nd64_full, _ = invariant_sym_forms(gens_full(6, 4), 10)
nd64_comp, _ = invariant_sym_forms(gens_compact(6, 4), 10)
check("FIB1 full so(6,4) on the fiber forces nulldim 1 (~ the fiber eta, INDEFINITE)", nd64_full, 1, atol=0)
check("FIB2 the good-stable fiber stabilizer (compact so(6)+so(4)) has a 2-DIM invariant form space -> "
      "the (6,4)-fiber record-count grading sign is a FREE coordinate too (consistent with W202/W168)",
      nd64_comp, 2, atol=0)

# ===========================================================================
print("\n[GODEL] the grading sign is model-dependent across the two fixed points => Godel-independent.")
# eta_C is positive-definite in the GOOD model and indefinite in the PATHOLOGICAL model; both satisfy the
# same self-consistency (commuting-involution) theory.  A statement true in one model and false in the
# other is INDEPENDENT of the theory -> must be POSITED, not derived (the fixpoint-free-residual reading).
good_positive = signature(g95 @ C_good)[1] == 0
path_positive = signature(g95 @ C_path)[1] == 0
check_bool("GODEL1 'the total metric is positive-definite' is TRUE in the good model and FALSE in the "
           "pathological model of the SAME self-consistency theory -> Godel-INDEPENDENT of GU-native "
           "structure; the grading sign MUST BE POSITED (RESIDUAL free selection, PC1)",
           good_positive and (not path_positive))

# ===========================================================================
print("\n[NC] negative control: a genuinely Euclidean (positive-definite) frame shows NO dim jump.")
# If the metric were positive-definite to begin with (signature (14,0)), its full stabilizer is ALREADY
# compact so(14); there is no compact/non-compact split, no grading, and Schur gives nulldim 1 (no
# second invariant, no free sign).  The whole R7 structure REQUIRES the Krein indefiniteness.
g_euclid = metric(14, 0)
nd_e_full, _ = invariant_sym_forms(gens_full(14, 0), 14)
nd_e_comp, _ = invariant_sym_forms(gens_compact(14, 0), 14)
check("NC1 a positive-definite (14,0) frame: full stabilizer = compact so(14), nulldim 1 (no split)",
      nd_e_full, 1, atol=0)
check("NC2 ... and the 'compact' generator set IS the full set, so NO dimension jump (nulldim stays 1) "
      "-> the dim-2 result and the free grading NEED the Krein indefiniteness (not an artifact)",
      nd_e_comp, 1, atol=0)

# ===========================================================================
print("\n[E1] VERDICT.")
verdict_residual = (nd_comp == 2) and (fixed_point_count == 2) and (in_span(eta_plus, basis_comp) < 1e-9) \
    and (in_span(g95, basis_comp) < 1e-9)
check_bool("E1 RESIDUAL-BIT-STANDS: grading self-map fixed-point count = 2 (good + pathological); the "
           "good-stable stabilizer's invariant symmetric form space is 2-dimensional; eta_+ is one "
           "positive ray but the grading SIGN is a free, Godel-independent coordinate (eta up-to-grading "
           "only). The C-operator grading sign is NOT forced; it must be posited.", verdict_residual)

# ===========================================================================
print("\n" + "=" * 78)
if FAILS:
    print(f"RESULT: {NCHECK - len(FAILS)}/{NCHECK} PASS -- {len(FAILS)} FAILED")
    for f in FAILS:
        print("   FAILED:", f)
    print("\nVERDICT: TEST FAILED (see above).")
    sys.exit(1)
print(f"RESULT: {NCHECK}/{NCHECK} PASS  (exit 0)")
print("\nVERDICT (R7, Lawvere categorical fixed point): RESIDUAL-BIT-STANDS.")
print("  Grading self-map Lawvere fixed-point count = 2 (good + pathological, per W186 bistability).")
print("  Good-stable stabilizer (maximal compact so(9)+so(5)) invariant symmetric form space = dim 2.")
print("  eta_+ is one positive ray; the C-operator grading SIGN is a Godel-independent residual that")
print("  must be POSITED -- only eta UP-TO-GRADING is forced (the W203 nulldim-1 is the ungraded metric).")
print("  Convergence: agrees with W186 (bistable, selection external); consistent with W202 (fiber sign")
print("  robust but ACTIVATION external) and W203 (Schur forces eta up-to-grading only). No canon move.")
sys.exit(0)
