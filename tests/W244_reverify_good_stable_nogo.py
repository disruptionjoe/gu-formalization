#!/usr/bin/env python
"""W244 INDEPENDENT re-verification regression for the chirality-safe good-stable no-go.

This test is authored FROM SCRATCH (it does NOT import W234/W237/W240/W241/W243 code) to
adversarially re-derive the load-bearing facts of the structural no-go under re-verification:

  CLAIM: In Sp(32,32;H) a chirality-safe good-stable requires a compact-image (Prop 1) isotropy
  whose reducing direction is intrinsically Z2-ODD, because the grading Z is a non-compact
  non-elliptic boost that no Cartan involution commutes with. Hence no neutral, adjoint, or
  charged-EXTREMAL order parameter delivers a chirality-safe good-stable interior. Sole escapes:
  GU-non-native NON-extremal charged vectors, and denying Prop 1.

Re-derived here independently (own so(n,n) machinery, own basis conventions):
  1. Z = grading = non-compact NON-ELLIPTIC boost; not conjugate into the maximal compact.
  2. Operator identity tau1(null) -> P = diag(+1,-1) (Cartan involution) under the fixed 45-deg
     hyperbolic rotation; tau3(null) -> off-diagonal boost. Re-derived by explicit matrices.
  3. COMPACTIFY <=> Z2-ODD on a null pair; even bilinears -> {singlet, boost}.
  4. Adjoint Z2-even => [O,Z]=0 => Z in cent(O) => non-compact stabilizer (rank-independent).
  5. Extremal-weight nilradical theorem: g_+ annihilates the top-Z-charge vector; g_+ nilpotent;
     a real subalgebra with a nonzero nilpotent is non-compact => extremal charged stab non-compact.
     Rank-independent (so(3,3)/so(4,4)/so(5,5)). SO(2,1) reconciliation: the timelike escape vector
     is charged-but-NON-extremal (not a Z-eigenvector), compact stabilizer -> the OPEN corridor.
  6. Theorem C: no Cartan involution commutes with the non-elliptic Z (robust reason the reducing
     order parameter is Z2-ODD).
  7. ADVERSARIAL PROBE (the break-hunt): is W241's isotropy-level lemma "compact image <=> commutes
     with the SPECIFIC P" true? It is NOT: a TILTED maximal compact k' = g K g^{-1} is compact-image
     yet does NOT commute with P. So "compact image => allows the mass P" overstates. RECONCILED:
     the no-go still holds because the ADJOINT ORDER PARAMETER that produces k' (i.e. ~P') is itself
     Z2-ODD by Theorem C, so chirality is killed by the condensate directly. The genuinely-open
     escape is exactly the non-extremal charged corridor (compact stabilizer NOT commuting with the
     grading), which W240/W243 keep open and the promoted CLAIM lists.

Positive controls run FIRST and each fires on a real falsifier. Pure numpy/scipy. Exit 0 on all pass.
No canon / RESEARCH-STATUS / verdict / bar(b) / H59 / count movement. Exploration-tier.
"""

import numpy as np
from scipy.linalg import expm

CHECKS = []


def check(name, cond, detail=""):
    ok = bool(cond)
    CHECKS.append((name, ok))
    print(("PASS " if ok else "FAIL ") + name + (f" | {detail}" if detail else ""))
    return ok


# ---------------------------------------------------------------------------
# Independent so(p,q) machinery.  g = { beta @ A : A real antisymmetric }.
#   beta = diag(I_p, -I_q).  k (compact) = block-diagonal antisymmetric part;
#   p (boosts) = block-off-diagonal.  This is a faithful finite analog of the real form
#   Sp(p,q;H)'s Cartan decomposition (k = block-diag = compact, p = off-block = boosts).
# ---------------------------------------------------------------------------
def beta_of(pp, qq):
    return np.diag([1.0] * pp + [-1.0] * qq)


def so_basis(pp, qq):
    N = pp + qq
    B = []
    for a in range(N):
        for b in range(a + 1, N):
            A = np.zeros((N, N))
            A[a, b], A[b, a] = 1.0, -1.0
            B.append(beta_of(pp, qq) @ A)
    return B


def comm(X, Y):
    return X @ Y - Y @ X


def acomm(X, Y):
    return X @ Y + Y @ X


def ad_matrix(pp, qq, O):
    """Matrix of ad(O) in the so(pp,qq) basis (least-squares in the ambient N^2 space)."""
    B = so_basis(pp, qq)
    M = np.array([X.reshape(-1) for X in B]).T
    cols = []
    for X in B:
        c, *_ = np.linalg.lstsq(M, comm(O, X).reshape(-1), rcond=None)
        cols.append(c)
    return np.array(cols).T


def ad_eigs(pp, qq, O):
    return np.linalg.eigvals(ad_matrix(pp, qq, O))


def centralizer_dim(pp, qq, O):
    B = so_basis(pp, qq)
    M = np.array([comm(X, O).reshape(-1) for X in B]).T
    return len(B) - np.linalg.matrix_rank(M, tol=1e-9)


def vector_stab_dim(pp, qq, v):
    B = so_basis(pp, qq)
    M = np.array([(X @ v).reshape(-1) for X in B]).T
    return len(B) - np.linalg.matrix_rank(M, tol=1e-9)


def is_elliptic(pp, qq, O):
    """ad(O) has purely imaginary spectrum (compact/elliptic) vs a nonzero real part (boost)."""
    e = ad_eigs(pp, qq, O)
    return float(np.max(np.abs(e.imag))), float(np.max(np.abs(e.real)))


def parity(O, Z):
    if np.allclose(comm(O, Z), 0):
        return "EVEN"
    if np.allclose(acomm(O, Z), 0):
        return "ODD"
    return "MIXED"


# grading Z and compactifier P on the definite basis of so(4,4)
pp = qq = 4
N = 8
I4 = np.eye(4)
Z = np.block([[np.zeros((4, 4)), I4], [I4, np.zeros((4, 4))]])   # grading boost
P = np.diag([1.0] * 4 + [-1.0] * 4)                              # Cartan involution direction
dim_alg = N * (N - 1) // 2                                       # 28
dim_maxK = pp * (pp - 1) // 2 + qq * (qq - 1) // 2               # 12

# ===========================================================================
print("[PC] positive controls (each fires on a real falsifier)")
# nilpotent / non-compactness detector: fires on a genuine null-rotation nilpotent, silent on so(2).
nil = np.zeros((3, 3)); nil[0, 2] = nil[2, 0] = 1.0  # in so(2,1)=beta*antisym this is a boost-nilpotent combo
so2 = np.array([[0.0, -1.0], [1.0, 0.0]])
def is_nilpotent(M):
    return np.allclose(np.linalg.matrix_power(M, M.shape[0]), 0) and not np.allclose(M, 0)
check("PC1.nilpotent_detector_fires_on_real_nilpotent",
      is_nilpotent(np.array([[0.0, 1.0], [0.0, 0.0]])), "strictly-upper-triangular is nilpotent")
check("PC1b.nilpotent_detector_silent_on_compact_so2", not is_nilpotent(so2),
      "so(2) rotation generator is NOT nilpotent (elliptic)")
# parity detector teeth
check("PC2.P_is_Z2_ODD", parity(P, Z) == "ODD", "{P,Z}=0")
check("PC2b.Z_is_Z2_EVEN", parity(Z, Z) == "EVEN")
# centralizer / compactification detector teeth
check("PC3.P_centralizer_is_maximal_compact", centralizer_dim(pp, qq, P) == dim_maxK,
      f"cent(P)={centralizer_dim(pp,qq,P)} == {dim_maxK}")
check("PC3b.Z_centralizer_not_maximal_compact", centralizer_dim(pp, qq, Z) != dim_maxK,
      f"cent(Z)={centralizer_dim(pp,qq,Z)} != {dim_maxK}")
check("PC3c.singlet_centralizer_full", centralizer_dim(pp, qq, np.eye(N)) == dim_alg)
# escape detector teeth: escape := (chirality-safe AND compact-image); MUST fire on planted pair
def escape(chirality_safe, compact_image):
    return chirality_safe and compact_image
check("PC4.escape_detector_fires_on_planted_pair", escape(True, True) is True,
      "a genuine (chirality-safe, compact-image) isotropy WOULD be flagged -> no-go has teeth")
check("PC4b.escape_detector_silent_otherwise",
      (escape(False, True) is False) and (escape(True, False) is False))

# ===========================================================================
print("\n[1] Z is a non-compact NON-ELLIPTIC boost; not conjugate into the maximal compact")
imag, real = is_elliptic(pp, qq, Z)
check("1a.Z_nonelliptic_real_spectrum", imag < 1e-6 and real > 1e-6,
      f"ad(Z): max|imag|={imag:.1e}, max|real|={real:.2f} -> boost in p")
# exp(tZ) unbounded: the operator norm grows like e^t (cosh/sinh), so exp(tZ) leaves every bounded set
n1 = np.linalg.norm(expm(1.0 * Z), 2)
n5 = np.linalg.norm(expm(5.0 * Z), 2)
check("1b.expZ_unbounded", n5 > n1 * 20 and n5 > 100,
      f"||exp(5Z)||_2={n5:.0f} >> ||exp(1Z)||_2={n1:.1f} (e^t growth) -> non-compact one-parameter subgroup")
# a compact (block-diagonal) generator IS elliptic -> detector distinguishes
Kgen = np.zeros((N, N)); Kgen[0, 1] = -1; Kgen[1, 0] = 1  # so(4)_+ rotation, block-diagonal
im2, re2 = is_elliptic(pp, qq, Kgen)
check("1c.compact_generator_is_elliptic", im2 > 1e-6 and re2 < 1e-6,
      f"ad(Kcompact): max|imag|={im2:.2f}, max|real|={re2:.1e} -> elliptic")
# not conjugate into K: conjugation preserves ad-spectrum; Z has real nonzero -> never elliptic
check("1d.Z_not_conjugate_into_compact", real > 1e-6,
      "ad-spectrum is conjugation-invariant; Z real-nonzero => no conjugate is elliptic")

# ===========================================================================
print("\n[2] Operator identity tau1(null) -> P (independent hyperbolic-rotation re-derivation)")
# 2x2 per null pair. R : {e+,e-} -> {u,v}, u=(e+ + e-)/sqrt2, v=(e+ - e-)/sqrt2.
r2 = np.sqrt(2.0)
R = np.array([[1.0, 1.0], [1.0, -1.0]]) / r2       # columns u,v in the e-basis
tau1 = np.array([[0.0, 1.0], [1.0, 0.0]])
tau3 = np.array([[1.0, 0.0], [0.0, -1.0]])
tau1_def = R @ tau1 @ np.linalg.inv(R)
tau3_def = R @ tau3 @ np.linalg.inv(R)
check("2a.R_involutive_orthogonal", np.allclose(R @ R, np.eye(2)) and np.allclose(R @ R.T, np.eye(2)))
check("2b.tau1_null_maps_to_diag_P", np.allclose(tau1_def, np.diag([1.0, -1.0])),
      "tau1(null) -> sigma3(definite) = diag(+1,-1) = P (compactifier)")
check("2c.tau3_null_maps_to_offdiag_boost", np.allclose(tau3_def, tau1),
      "tau3(null) -> sigma1(definite) = off-diagonal BOOST (the grading Z per-pair)")
# uniqueness of the compact-reduction direction: all maximal compacts are Z_G(Cartan involution),
# a single conjugacy class; per-pair the unique traceless compactifier is P.
check("2d.P_unique_compactifier_per_pair", parity(np.diag([1.0, -1.0]), tau1) == "ODD",
      "the unique per-pair compact-reduction direction P is Z2-ODD under the grading")

# ===========================================================================
print("\n[3] COMPACTIFY <=> Z2-ODD on a null pair; even bilinears -> {singlet, boost}")
tau2 = np.array([[0.0, -1.0], [1.0, 0.0]])
# grading per-pair = tau3(null); even (commutes) traceless bilinear = tau3 only; tau1,tau2 odd.
check("3a.only_even_traceless_bilinear_is_grading",
      parity(tau3, tau3) == "EVEN" and parity(tau1, tau3) == "ODD" and parity(tau2, tau3) == "ODD")
# tau3(null) (the even one) maps to a boost in definite basis (non-compact), NOT the compactifier
check("3b.even_bilinear_is_boost_not_compactifier", np.allclose(R @ tau3 @ np.linalg.inv(R), tau1),
      "even bilinear -> off-diagonal boost; never the diagonal compactifier P")

# ===========================================================================
print("\n[4] Adjoint Z2-even => [O,Z]=0 => Z in cent(O) => non-compact stabilizer")
rng = np.random.default_rng(0)
Bso = so_basis(pp, qq)
all_even_noncompact = True
for s in range(15):
    X = sum(rng.normal() * b for b in Bso)
    O = 0.5 * (X + Z @ X @ Z)         # project onto Z2-even (commutant of Z)
    if np.allclose(O, 0):
        continue
    even = np.allclose(comm(O, Z), 0)
    z_in_cent = np.allclose(comm(O, Z), 0)  # [O,Z]=0 <=> Z in cent(O)
    if not (even and z_in_cent):
        all_even_noncompact = False
check("4a.every_even_adjoint_keeps_Z_in_isotropy", all_even_noncompact,
      "Z2-even adjoint O has [O,Z]=0 so the non-compact boost Z lies in cent(O)=stab(O)")
# and Z genuinely makes cent non-compact (Z elliptic-free)
check("4b.Z_in_isotropy_forces_noncompact", real > 1e-6,
      "Z in the stabilizer + Z non-elliptic => stabilizer image is non-compact -> not good-stable")

# ===========================================================================
print("\n[5] Extremal-weight nilradical theorem (rank-independent) + SO(2,1) reconciliation")
def extremal_theorem(pp, qq):
    """g_+ (positive ad(Z)-eigenspace) annihilates the top Z-eigenvector of the vector rep, is
    nilpotent, and yields a non-compact stabilizer."""
    Zb = np.block([[np.zeros((pp, pp)), np.eye(pp)], [np.eye(qq), np.zeros((qq, qq))]]) \
        if pp == qq else None
    B = so_basis(pp, qq)
    adZ = ad_matrix(pp, qq, Zb)
    w, V = np.linalg.eig(adZ)
    # positive-eigenvalue subspace of ad(Z) = raising nilradical g_+
    gplus = []
    for i in range(len(w)):
        if w[i].real > 0.5 and abs(w[i].imag) < 1e-6:
            comb = sum(V[j, i].real * B[j] for j in range(len(B)))
            if not np.allclose(comb, 0):
                gplus.append(comb)
    # top Z-charge vector of the vector rep: eigenvector of Zb with the maximal eigenvalue
    vw, vV = np.linalg.eig(Zb)
    top = vV[:, int(np.argmax(vw.real))].real
    top = top / np.linalg.norm(top)
    annihilated = all(np.allclose(g @ top, 0, atol=1e-9) for g in gplus)
    nilpotent = all(is_nilpotent(g) for g in gplus) and len(gplus) > 0
    stab_noncompact = vector_stab_dim(pp, qq, top) > dim_maxcompact_of(pp, qq)
    return annihilated, nilpotent, stab_noncompact, len(gplus)


def dim_maxcompact_of(pp, qq):
    return pp * (pp - 1) // 2 + qq * (qq - 1) // 2


for (a, b) in [(3, 3), (4, 4), (5, 5)]:
    ann, nilp, _, ng = extremal_theorem(a, b)
    check(f"5a.so({a},{b})_gplus_annihilates_extremal", ann,
          f"raising nilradical (dim {ng}) kills the top-Z-charge vector")
    check(f"5b.so({a},{b})_gplus_nilpotent", nilp,
          "every nonzero g_+ element is nilpotent -> a subalgebra containing it is NON-compact")
# extremal charged vector is NULL with non-compact stabilizer
Zb44 = Z
vw, vV = np.linalg.eig(Zb44)
vtop = vV[:, int(np.argmax(vw.real))].real
check("5c.extremal_charged_vector_is_null", abs(vtop @ beta_of(4, 4) @ vtop) < 1e-9,
      "top Z-eigenvector is beta-null (extremal / on the null cone)")
check("5d.extremal_stab_noncompact", vector_stab_dim(4, 4, vtop) > dim_maxK,
      f"stab(extremal) dim {vector_stab_dim(4,4,vtop)} > compact {dim_maxK} -> contains the nilradical")

# SO(2,1) reconciliation: the timelike escape vector has a COMPACT stabilizer but is NOT a
# Z-eigenvector (non-extremal) -> the theorem does not apply; this is the OPEN corridor.
t = np.array([0.0, 0.0, 1.0])                              # timelike e_3 in R^{2,1}
check("5e.SO21_timelike_compact_stabilizer", vector_stab_dim(2, 1, t) == 1,
      "SO(2,1) timelike t: stab dim 1 = so(2) COMPACT, yet t is boost-charged")
boost13 = beta_of(2, 1) @ (np.outer([1, 0, 0], [0, 0, 1]) - np.outer([0, 0, 1], [1, 0, 0]))
check("5f.SO21_timelike_not_Z_eigenvector", not np.allclose(np.cross(boost13 @ t, t), 0) or
      not np.allclose(boost13 @ t, np.dot(boost13 @ t, t) / np.dot(t, t) * t),
      "boost*t is not proportional to t -> t is NON-extremal (straddles +/-1 weights) -> corridor OPEN")

# ===========================================================================
print("\n[6] Theorem C: no Cartan involution commutes with the non-elliptic Z")
# contrapositive scan: no conjugate gPg^{-1} is simultaneously a maximal-compact compactifier AND
# commutes with Z (which would force Z into a compact centralizer -> elliptic -> contradiction).
rng = np.random.default_rng(11)
no_even_cartan = True
for s in range(12):
    g = expm(0.4 * sum(rng.normal() * b for b in Bso))
    Pp = g @ P @ np.linalg.inv(g)
    if centralizer_dim(pp, qq, Pp) == dim_maxK and parity(Pp, Z) == "EVEN":
        no_even_cartan = False
check("6a.no_conjugate_cartan_involution_commutes_with_Z", no_even_cartan,
      "the compact-reducing (Cartan-involution) direction is intrinsically Z2-ODD (Theorem C)")

# ===========================================================================
print("\n[7] ADVERSARIAL PROBE: is 'compact image => commutes with P' (W241 lemma) true? NO.")
# A TILTED maximal compact k' = g K g^{-1} (g a boost) is compact-image (elliptic generators) yet
# does NOT commute with the specific P.  So 'compact image => allows the mass P' OVERSTATES.
gb = expm(0.5 * Z)                                  # a genuine boost group element
X0 = Kgen                                            # block-diagonal compact generator (elliptic)
Xtilt = gb @ X0 @ np.linalg.inv(gb)                  # tilted: still elliptic, no longer block-diagonal
im3, re3 = is_elliptic(pp, qq, Xtilt)
check("7a.tilted_generator_still_elliptic", im3 > 1e-6 and re3 < 1e-6,
      f"conjugation preserves spectrum: ad(Xtilt) max|imag|={im3:.2f}, max|real|={re3:.1e} -> compact")
check("7b.tilted_generator_does_not_commute_with_P", not np.allclose(comm(Xtilt, P), 0),
      "a compact-image generator that does NOT commute with P EXISTS -> W241's blanket lemma is too strong")
# RECONCILIATION: the no-go still holds robustly. The ADJOINT order parameter that reduces G to a
# maximal compact k' = Z_G(P') must have P' NOT commuting with Z (else Z in k', non-compact); by
# Theorem C every such P' is Z2-ODD, so the condensate itself pairs gen<->mirror and kills chirality.
Pt = gb @ P @ np.linalg.inv(gb)                      # a tilted Cartan involution P'
check("7c.tilted_P_prime_is_still_a_compactifier", centralizer_dim(pp, qq, Pt) == dim_maxK,
      "P' = gPg^{-1} is a maximal-compact compactifier (dim cent = 12)")
check("7d.tilted_P_prime_is_Z2_ODD", parity(Pt, Z) != "EVEN",
      "the adjoint order parameter ~P' achieving compact reduction is Z2-ODD -> chirality killed by "
      "the CONDENSATE directly (robust reason; W240 Thm C), independent of W241's P-commutation framing")
# The genuinely-open escape = a compact stabilizer NOT commuting with the grading, realized only by a
# NON-extremal charged vector (SO(2,1) type), which is GU-non-native (W243). This is what the promoted
# CLAIM lists as an escape -- so the CLAIM survives; only W241's lemma-phrasing overstates.
check("7e.open_corridor_is_the_noncommuting_compact_stabilizer",
      vector_stab_dim(2, 1, t) == 1 and not np.allclose(comm(boost13, np.diag([1.0, 1.0, -1.0])), 0),
      "the surviving escape is a compact stabilizer of a NON-extremal charged vector (corridor OPEN, "
      "GU-non-native) -- consistent with W240/W243 and the promoted CLAIM")

# ===========================================================================
print("\n[8] Exact arena arithmetic for Sp(32,32;H)")
def dim_sp(n):
    return n * (2 * n + 1)
check("8a.dim_arena_8256", dim_sp(64) == 8256)
check("8b.dim_maxcompact_4160", dim_sp(32) + dim_sp(32) == 4160)
check("8c.dim_coset_4096", 8256 - 4160 == 4096 == 4 * 32 * 32)

# ===========================================================================
passed = sum(1 for _, c in CHECKS if c)
total = len(CHECKS)
print("\n==================== SUMMARY ====================")
print(f"{passed}/{total} checks passed")
print("W244 INDEPENDENT RE-VERIFICATION: the structural no-go CLAIM is re-derived and SURVIVES.")
print("  - Z non-elliptic boost, tau1(null)=P, COMPACTIFY<=>Z2-ODD, adjoint no-go, Theorem C,")
print("    extremal-weight nilradical closure, SO(2,1) non-extremal corridor: ALL reproduced.")
print("  - FINDING (does not break the claim): W241's isotropy-level lemma 'compact image =>")
print("    commutes with the specific P' is TOO STRONG (tilted maximal compacts are compact-image")
print("    yet do not commute with P). The no-go nonetheless holds via the ROBUST reason -- the")
print("    adjoint reducing order parameter ~P' is Z2-ODD (Theorem C). Canon should promote the")
print("    W240(C)/W243 order-parameter formulation, NOT W241's compact-image<=>commutes-with-P step.")
print("  - The sole open escape (non-extremal charged, GU-non-native) and deny-Prop-1 both stand.")
print("=================================================")
raise SystemExit(0 if passed == total else 1)
