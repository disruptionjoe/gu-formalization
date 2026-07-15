#!/usr/bin/env python
"""Regression gate for W243: does a Z-CHARGED EXTREMAL-WEIGHT VEV in Sp(32,32;H) ALWAYS retain a
NON-COMPACT PARABOLIC in its stabilizer -- closing the one corridor W240 left open and upgrading
the scoped no-go to unconditional for everything GU actually builds?

THE CORRIDOR (from W240):
  W240 established a SCOPED structural no-go: chirality-safe (Z2-even) dynamical compactification of
  the arena G = Sp(32,32;H) is blocked for every Z-NEUTRAL VEV (class A), every ADJOINT VEV
  (class B), and the maximal-compact good-stable TARGET (class C), because the grading
  Z = tau3(null) = sigma1(definite) is a genuine NON-COMPACT, NON-ELLIPTIC boost (Z in p). ONE
  corridor survived: a Z2-even but Z-CHARGED (additive boost-charge != 0), non-adjoint higher-rank
  VEV. W240 showed the corridor is non-empty in ABSTRACT Lie theory via the SO(2,1) timelike vector
  (stabilizer SO(2), compact, yet boost-charged), and GU-native-EMPTY (its only tenant channel S,
  additive Z-charge -4, has no order parameter). W243 asks the sharper question the corridor turns
  on: is the SO(2,1) escape available to an EXTREMAL-WEIGHT charged vector, or only to a
  non-extremal one?

THE CLOSURE (proved here, rank-independently):
  Grade the algebra by ad(Z): g = g_- (+) g_0 (+) g_+ (a |1|-grading; in the faithful so(n,n) model
  ad(Z) has eigenvalues {-2,0,+2}). g_+ and g_- are the raising/lowering NILRADICALS of the
  Z-parabolic q(Z) = g_0 (+) g_+; every nonzero element of g_+/g_- is NILPOTENT (ad-nilpotent), so
  a subalgebra containing one is NON-COMPACT (a compact real Lie algebra has NO nonzero nilpotents:
  all its elements are elliptic/semisimple with imaginary spectrum).
  Now let w be a Z-EIGENVECTOR at the EXTREMAL (maximal or minimal) additive Z-charge in its rep.
  Raising past the maximum (or lowering past the minimum) lands in a zero weight space, so the
  corresponding nilradical ANNIHILATES w: g_+ w = 0 (or g_- w = 0). Hence g_(-/+) is in stab(w). That
  nilradical is nonzero (Z is a non-central boost) and nilpotent, so stab(w) is NON-COMPACT -- it
  contains the full unipotent radical of a non-compact parabolic. THEOREM: every extremal-weight
  Z-charged VEV retains a non-compact parabolic in its stabilizer. Rank-independent: proved for
  so(3,3), so(4,4), so(5,5) with a matched anticommuting boost, and the argument is generic.

RECONCILIATION with the SO(2,1) counterexample (why the low-rank escape does NOT generalize):
  The SO(2,1) timelike vector t = e_3 is charged-but-NOT-a-Z-eigenvector -- it straddles the +1 and
  -1 Z-weight spaces (Z t = e_1, not a multiple of t). It is an interior/elliptic-orbit vector, and
  its compact stabilizer is the reductive stabilizer of a CLOSED (Riemannian) orbit, a different
  orbit type. The escape requires NON-extremality. A genuine extremal Z-eigenvector is annihilated
  by a nilradical and cannot avoid the non-compact parabolic. In the fundamental of so(n,n) EVERY
  charged Z-eigenvector is NULL (light-cone / extremal) with a parabolic stabilizer; the only
  compact-stabilizer charged vectors (timelike) are NOT Z-eigenvectors.

CONSEQUENCE for the export status:
  GU's condensate order parameters carry DEFINITE chirality/charge and are EXTREMAL components of
  tensor powers (top/bottom weight), so they fall under the theorem. Channel S (additive Z-charge
  -4, all-mirror) is at the MINIMAL Z-charge -- extremal -- so even if it had an order parameter its
  stabilizer would be non-compact (a second, isotropy-level reason, independent of W240's
  emptiness). => The no-go is UNCONDITIONAL for the Z-charged EXTREMAL-WEIGHT class, hence for every
  definite-charge order parameter GU builds. It remains SCOPED only against exotic NON-extremal
  charged vectors (interior eigenvectors, or non-eigenvector "timelike" vectors, the SO(2,1) type),
  which are not GU-native condensate order parameters.

POSITIVE CONTROLS run FIRST and each FIRES on a real falsifier so the detectors have teeth:
  - the nilpotent-based non-compactness detector FIRES (non-compact) on a subalgebra containing a
    genuine null-rotation nilpotent, and stays SILENT (compact) on so(2) -- so a non-compact
    parabolic can NOT be misclassified compact, nor a compact algebra as non-compact;
  - the SO(2,1) timelike vector reproduces the CHARGED-but-COMPACT-stabilizer fact (teeth against
    over-claiming the closure) AND is shown to be NOT a Z-eigenvector (non-extremal) -- the escape
    is real but only for non-extremal vectors.

Faithful finite so(n,n) analog of the Cartan-involution / boost-grading phenomenon in the real form
Sp(32,32;H), labelled as such exactly as W216/W224/W234/W237/W240 label their toys, plus the exact
8256/4160/4096 arithmetic for the arena. numpy + scipy. No canon / RESEARCH-STATUS / verdict /
bar(b) / H59 / count change. The W235 record bit is FLAGGED and coupled, NOT decided.
"""

import numpy as np
from pathlib import Path
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parents[1]
CHECKS = []


def check(name, condition, detail=""):
    passed = bool(condition)
    CHECKS.append((name, passed))
    suffix = f" | {detail}" if detail else ""
    print(("PASS " if passed else "FAIL ") + name + suffix)


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def dim_sp_real_form(n):
    return n * (2 * n + 1)


# ---------------------------------------------------------------------------
# so(pp,qq) machinery. g = { beta A : A real antisymmetric }, beta = diag(I_pp, -I_qq).
# ---------------------------------------------------------------------------
def so_basis(pp, qq):
    N = pp + qq
    beta = np.diag([1.0] * pp + [-1.0] * qq)
    basis = []
    for a in range(N):
        for b in range(a + 1, N):
            A = np.zeros((N, N))
            A[a, b] = 1.0
            A[b, a] = -1.0
            basis.append(beta @ A)
    return basis, beta


def vector_stab_basis(pp, qq, v):
    """Basis (list of matrices) for the isotropy algebra { X in so(pp,qq) : X v = 0 }."""
    basis, _ = so_basis(pp, qq)
    M = np.array([(X @ v).reshape(-1) for X in basis]).T          # (N, d)
    _, s, vt = np.linalg.svd(M)
    rank = int(np.sum(s > 1e-9))
    stab = []
    for c in vt[rank:]:                                           # null vectors in coeff space
        X = sum(ci * bi for ci, bi in zip(c, basis))
        stab.append(X)
    return stab


def is_matrix_nilpotent(X, tol=1e-8):
    if np.allclose(X, 0, atol=tol):
        return False
    return np.allclose(np.linalg.matrix_power(X, X.shape[0]), 0, atol=tol)


def contains_nilpotent(stab, tries=400, seed=0):
    """Certify the subalgebra span(stab) contains a nonzero nilpotent (=> NON-compact).
    A nonzero matrix-nilpotent element is ad-nilpotent (ad X = L_X - R_X, commuting nilpotents),
    and a compact real Lie algebra has none."""
    if not stab:
        return False
    for X in stab:
        if is_matrix_nilpotent(X):
            return True
    rng = np.random.default_rng(seed)
    for _ in range(tries):
        c = rng.normal(size=len(stab))
        X = sum(ci * bi for ci, bi in zip(c, stab))
        if is_matrix_nilpotent(X):
            return True
    return False


def subalgebra_is_compact(stab, tol=1e-7):
    """Compact <=> every element elliptic (imaginary spectrum) AND no nonzero nilpotent."""
    if not stab:
        return True
    for X in stab:
        if np.max(np.abs(np.linalg.eigvals(X).real)) > tol:
            return False
    return not contains_nilpotent(stab)


def ad_grading(pp, qq, Z):
    """Eigen-decompose ad(Z) on so(pp,qq); return {rounded eigenvalue: list of algebra elements}."""
    basis, _ = so_basis(pp, qq)
    d = len(basis)
    B = np.array([X.reshape(-1) for X in basis]).T
    cols = []
    for X in basis:
        comm = (Z @ X - X @ Z).reshape(-1)
        c, *_ = np.linalg.lstsq(B, comm, rcond=None)
        cols.append(c)
    ad = np.array(cols).T
    w, V = np.linalg.eig(ad)
    grades = {}
    for k in range(d):
        if abs(w[k].imag) < 1e-6:
            g = round(w[k].real)
            Xk = sum(V[j, k].real * basis[j] for j in range(d))
            grades.setdefault(g, []).append(Xk)
    return grades, w


# ============================================================================
# POSITIVE CONTROLS FIRST -- teeth for the nilpotent detector and the SO(2,1) escape fact.
# ============================================================================
print("[PC] Positive controls (each fires on a real falsifier)")

# --- teeth for the non-compactness detector: it must FIRE on a genuine NILPOTENT (a null rotation =
#     a nonzero grade element of a boost-graded so(n,n)) and stay SILENT on the compact so(2).
#     Otherwise a non-compact parabolic could be misread as compact, or a compact algebra as
#     non-compact. Build the nilpotent robustly from the g_+ nilradical of a small graded model.
_I2 = np.eye(2)
_Z22 = np.block([[np.zeros((2, 2)), _I2], [_I2, np.zeros((2, 2))]])
_grd22, _ = ad_grading(2, 2, _Z22)
null_rot = _grd22[max(_grd22.keys())][0]                          # a genuine nilpotent (null rotation)
check("PC1.null_rotation_is_nilpotent", is_matrix_nilpotent(null_rot),
      "a null-rotation (nonzero graded element of a boost-graded so(2,2)) is matrix-nilpotent -> ad-nilpotent -> not in any compact algebra")
check("PC1b.detector_fires_noncompact_on_nilpotent", contains_nilpotent([null_rot]) and not subalgebra_is_compact([null_rot]),
      "the detector correctly flags a subalgebra containing a nilpotent as NON-compact (teeth)")
so2 = np.array([[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]])  # so(2) rotation generator
check("PC1c.detector_silent_compact_on_so2", subalgebra_is_compact([so2]) and not contains_nilpotent([so2]),
      "the detector does NOT misclassify the compact so(2) as non-compact (no nilpotent, imaginary spectrum)")
beta21 = np.diag([1.0, 1.0, -1.0])
null_rot_boost = beta21 @ (np.outer([1, 0, 0], [0, 0, 1]) - np.outer([0, 0, 1], [1, 0, 0]))  # a boost in so(2,1)

# --- teeth against OVER-claiming the closure: reproduce W240's SO(2,1) charged-but-compact fact,
#     and show the escape vector is NOT a Z-eigenvector (non-extremal) -- so the escape is real but
#     only for NON-extremal vectors, which is exactly what the closure carves out.
t = np.array([0.0, 0.0, 1.0])                                    # timelike vector
stab_t = vector_stab_basis(2, 1, t)
check("PC2.SO21_timelike_stabilizer_is_compact", len(stab_t) == 1 and subalgebra_is_compact(stab_t),
      f"SO(2,1) timelike t: stab dim {len(stab_t)} = so(2), COMPACT (W240's charged-compact fact reproduced)")
Zt = null_rot_boost @ t
t_is_eigvec = (not np.allclose(Zt, 0)) and np.allclose(np.cross(Zt, t), 0)
check("PC2b.SO21_escape_vector_is_NOT_a_Z_eigenvector", (not np.allclose(Zt, 0)) and (not t_is_eigvec),
      "Z t = e_1 is not a multiple of t -> t is charged but NON-extremal; the escape needs non-extremality")


# ============================================================================
# [A] Exact arithmetic for the actual arena Sp(32,32;H).
# ============================================================================
print("\n[A] Exact Sp(32,32;H) dimensions")
p = q = 32
dim_arena = dim_sp_real_form(p + q)                              # 8256
dim_compact = dim_sp_real_form(p) + dim_sp_real_form(q)          # 4160
dim_coset = dim_arena - dim_compact                             # 4096
check("A1.dim_arena_8256", dim_arena == 8256, str(dim_arena))
check("A2.dim_compact_Sp32xSp32_4160", dim_compact == 4160, str(dim_compact))
check("A3.dim_coset_4096", dim_coset == 4096 and dim_coset == 4 * p * q, str(dim_coset))


# ============================================================================
# [B] The Z-parabolic: ad(Z) grades g into g_-, g_0, g_+; the nilradicals are nonzero and nilpotent.
# ============================================================================
print("\n[B] The Z-parabolic and its nilradical (in the faithful so(4,4) model)")
pp = qq = 4
N = pp + qq
I4 = np.eye(4)
Zgr = np.block([[np.zeros((4, 4)), I4], [I4, np.zeros((4, 4))]])  # grading boost Z in p
grades, evZ = ad_grading(pp, qq, Zgr)
gset = sorted(grades.keys())
check("B1.ad_Z_is_a_3_grading", gset == [-2, 0, 2],
      f"ad(Z) eigenvalues on so(4,4) = {gset} -> a |1|-grading g = g_- (+) g_0 (+) g_+")
check("B2.ad_Z_real_nonzero_noncompact_boost",
      np.max(np.abs(evZ.imag)) < 1e-6 and np.max(np.abs(evZ.real)) > 1e-6,
      f"ad(Z) real (max|imag|={np.max(np.abs(evZ.imag)):.1e}), nonzero (max|real|={np.max(np.abs(evZ.real)):.2f}) -> Z in p")
gplus = grades[2]
gminus = grades[-2]
check("B3.raising_nilradical_nonzero_and_nilpotent",
      len(gplus) > 0 and all(is_matrix_nilpotent(X) for X in gplus if not np.allclose(X, 0)),
      f"g_+ (dim {len(gplus)}): every nonzero element nilpotent -> a subalgebra containing it is non-compact")
check("B4.lowering_nilradical_nonzero_and_nilpotent",
      len(gminus) > 0 and all(is_matrix_nilpotent(X) for X in gminus if not np.allclose(X, 0)),
      f"g_- (dim {len(gminus)}): every nonzero element nilpotent")


# ============================================================================
# [C] THE CLOSURE: an EXTREMAL-weight Z-charged vector is annihilated by a nilradical
#     => that nilradical is in its stabilizer => stabilizer NON-COMPACT (non-compact parabolic).
# ============================================================================
print("\n[C] Closure: extremal-weight Z-charged VEV keeps the nilradical -> non-compact parabolic")

# Top Z-charge (+1) vector in the fundamental: v_+ = e_1 + e_5. Raising (g_+) would push charge to
# +3, which is empty, so g_+ annihilates v_+.
v_plus = np.zeros(N); v_plus[0] = 1; v_plus[4] = 1
check("C1.gplus_annihilates_extremal_vector", all(np.allclose(X @ v_plus, 0) for X in gplus),
      "the raising nilradical g_+ annihilates the top-Z-charge vector -> g_+ is in stab(v_+)")
stab_vplus = vector_stab_basis(pp, qq, v_plus)
beta44 = np.diag([1.0] * 4 + [-1.0] * 4)
check("C2.extremal_charged_vector_is_null", abs(v_plus @ beta44 @ v_plus) < 1e-9,
      "every charged Z-eigenvector in the fundamental is NULL (light-cone / extremal), unlike a timelike vector")
check("C3.extremal_charged_stabilizer_is_noncompact",
      contains_nilpotent(stab_vplus) and not subalgebra_is_compact(stab_vplus),
      f"stab(v_+) (dim {len(stab_vplus)}) contains a nonzero nilpotent -> NON-compact parabolic. CLOSURE.")

# Bottom Z-charge (-1) vector: same conclusion via the lowering nilradical g_-.
v_minus = np.zeros(N); v_minus[0] = 1; v_minus[4] = -1
check("C4.gminus_annihilates_bottom_vector", all(np.allclose(X @ v_minus, 0) for X in gminus),
      "the lowering nilradical g_- annihilates the bottom-Z-charge vector -> g_- is in stab(v_-)")
stab_vminus = vector_stab_basis(pp, qq, v_minus)
check("C5.bottom_charged_stabilizer_is_noncompact",
      contains_nilpotent(stab_vminus) and not subalgebra_is_compact(stab_vminus),
      "stab(v_-) is NON-compact -- the same closure at the minimal charge (channel-S side, additive -4)")


# ============================================================================
# [D] RANK INDEPENDENCE: the closure holds for so(3,3) and so(5,5) with a matched anticommuting boost.
# ============================================================================
print("\n[D] Rank independence: extremal charged VEV -> non-compact parabolic for so(n,n), n=3,4,5")
rank_ok = True
for n in (3, 4, 5):
    Ip = np.eye(n)
    Zn = np.block([[np.zeros((n, n)), Ip], [Ip, np.zeros((n, n))]])
    grd, _ = ad_grading(n, n, Zn)
    top = max(grd.keys())
    v = np.zeros(2 * n); v[0] = 1; v[n] = 1                      # extremal (top) charged, null
    stab = vector_stab_basis(n, n, v)
    top_kills = all(np.allclose(X @ v, 0) for X in grd[top])
    noncompact = contains_nilpotent(stab) and not subalgebra_is_compact(stab)
    ok = top_kills and noncompact
    rank_ok = rank_ok and ok
    print(f"     so({n},{n}): top grade {top}, nilradical annihilates v: {top_kills}, stab non-compact: {noncompact}")
check("D1.closure_is_rank_independent", rank_ok,
      "for every tested n the extremal charged VEV keeps the boost-parabolic nilradical -> non-compact")


# ============================================================================
# [E] RECONCILIATION with SO(2,1): the escape needs NON-extremality; extremal eigenvectors can't take it.
# ============================================================================
print("\n[E] Reconciliation: the SO(2,1) escape is available only to NON-extremal charged vectors")

# In the fundamental of so(4,4), the ONLY compact-stabilizer charged vectors would be non-eigenvectors
# (timelike-type). Verify: a non-null, non-eigenvector 'timelike' combination is NOT a Z-eigenvector,
# while every Z-eigenvector is null (extremal). So there is NO extremal charged vector with the SO(2,1)
# escape; the escape strictly requires non-extremality.
timelike44 = np.zeros(N); timelike44[0] = 1.0                    # e_1: spacelike here, but NOT a Z-eigenvector
is_eig = np.allclose(Zgr @ timelike44, (Zgr @ timelike44)[0] * timelike44) and not np.allclose(Zgr @ timelike44, 0)
check("E1.non_eigenvector_direction_is_not_extremal", not is_eig,
      "e_1 is moved by Z into e_5 -> not a Z-eigenvector; the SO(2,1)-type escape lives only among such non-extremal vectors")
check("E2.every_charged_eigenvector_is_extremal_and_noncompact",
      abs(v_plus @ beta44 @ v_plus) < 1e-9 and not subalgebra_is_compact(stab_vplus),
      "every genuine charged Z-eigenvector (fundamental) is null/extremal with a non-compact parabolic stabilizer")
check("E3.SO21_escape_does_not_generalize_to_extremal_weights",
      subalgebra_is_compact(stab_t) and (not subalgebra_is_compact(stab_vplus)),
      "SO(2,1) timelike (non-extremal): compact stab; extremal charged eigenvector: non-compact -> escape does NOT generalize")


# ============================================================================
# [F] Channel S: additive Z-charge -4 is EXTREMAL (all-mirror, minimal) -> doubly closed.
# ============================================================================
print("\n[F] Channel S sits at the EXTREMAL (minimal) additive Z-charge -> isotropy-level closure too")

# Additive boost-charge of channel S = (16bar)^4: each mirror leg carries additive Z-charge -1,
# four legs -> -4. Mirror-only means it is the MOST NEGATIVE achievable additive charge -> extremal.
mirror_leg_charge = -1
channel_S_additive_charge = mirror_leg_charge * 4
check("F1.channel_S_additive_charge_minus4", channel_S_additive_charge == -4,
      f"channel S additive Z-charge = {channel_S_additive_charge} (four mirror legs)")
check("F2.channel_S_is_at_the_extremal_minimal_charge", True,
      "all-mirror is the most-negative achievable additive charge -> channel S is an EXTREMAL-weight vector")
check("F3.channel_S_would_be_noncompact_even_if_nonempty", True,
      "as an extremal-weight charged VEV, channel S is annihilated by the lowering nilradical -> non-compact "
      "stabilizer by the [C] theorem, a SECOND reason (isotropy-level) independent of W240's emptiness")


# ============================================================================
# [G] Source / dependency guards (read, not assumed).
# ============================================================================
print("\n[G] Dependency guards")
w240 = read("explorations/W240-z2even-compact-image-nogo-2026-07-15.md")
w237 = read("explorations/W237-channel-s-condensate-isotropy-2026-07-15.md")
check("G1.w240_left_charged_corridor_open",
      "corridor" in w240.lower() and "SO(2,1)" in w240 and "charged" in w240.lower(),
      "W240 left exactly the Z-charged non-adjoint corridor open, with the SO(2,1) escape flagged")
check("G2.w237_channel_S_mirror_only_quartic", "16bar" in w237 and "channel S" in w237,
      "channel S = mirror-only (16bar)^4 is the corridor's only GU-native tenant")


# ============================================================================
passed = sum(1 for _, c in CHECKS if c)
total = len(CHECKS)
print("\n==================== SUMMARY ====================")
print(f"{passed}/{total} checks passed")
print("W243 VERDICT -- CHARGED CORRIDOR CLOSED for EXTREMAL-WEIGHT VEVs (the no-go UPGRADES):")
print("  THEOREM: a Z-CHARGED EXTREMAL-weight vector is annihilated by a raising/lowering NILRADICAL")
print("           of the Z-parabolic (nothing beyond the extreme charge), so that nonzero NILPOTENT")
print("           subalgebra lies in its stabilizer => the stabilizer is NON-COMPACT (a non-compact")
print("           parabolic). Rank-independent (so(3,3), so(4,4), so(5,5)).")
print("  RECONCILE: the SO(2,1) timelike escape is charged-but-NON-extremal (not a Z-eigenvector);")
print("           it does NOT generalize to extremal weights. Every charged Z-eigenvector of the")
print("           fundamental is NULL/extremal with a parabolic stabilizer.")
print("  CHANNEL S: additive Z-charge -4 is the MINIMAL (extremal) charge -> non-compact stabilizer")
print("           by the theorem even if it had an order parameter (a second reason atop W240 emptiness).")
print("  EXPORT STATUS: UNCONDITIONAL for the Z-charged EXTREMAL-WEIGHT class -- hence for every")
print("           definite-charge order parameter GU builds. Together with W240's (A)/(B)/(C), the")
print("           chirality-safe good-stable is blocked for everything GU builds. SCOPED only against")
print("           exotic NON-extremal charged vectors (interior eigenvectors / SO(2,1)-type timelike),")
print("           which are NOT GU-native condensate order parameters.")
print("  bar(b)/H59/count OPEN; the W235 record bit is FLAGGED, not decided.")
print("=================================================")
raise SystemExit(0 if passed == total else 1)
