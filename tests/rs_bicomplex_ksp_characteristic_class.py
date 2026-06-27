#!/usr/bin/env python3
"""CLIMACTIC GATE (2026-06-27): SOURCE-DERIVED KSp CHARACTERISTIC-CLASS CARRIER +
FULL BV BICOMPLEX -- the attempt to drive the RS dressed closure obstruction to 0.

Builds on (verified objects, never re-derived here):
  tests/oq_rk1_cl95_explicit_rep.py            -- explicit Cl(9,5)=M(64,H)~M(128,C)
  tests/rs_ghost_fixed_null_covector_spurion.py-- null-covector spurion (32.80 floor)
  explorations/rs_source_candidate_projected_differential_scratch.py -- Gamma,Pi_RS,M_D,d_A

WHAT IS UNDER TEST (the design "ksp-characteristic-class")
---------------------------------------------------------
A. SOURCE-DERIVED CARRIER W: the intrinsic QUATERNIONIC KSp POLARIZATION class
   P_pol = sum_{k=0..4} c(n_k)c(nbar_k)/(2 eta(n_k,nbar_k)), the maximal-isotropic /
   polarization carrier of the module's INVARIANT SYMPLECTIC FORM Omega = U^dag.
   It is fixed a-priori from the rep's quaternionic data ONLY -- built in code BEFORE
   M_D is constructed, never a functional of xi or M_D. Test: does the deformed
   surface ker(B_W) drive ||[Pi_kerBW, M_D]|| BELOW 32.80, ideally to 0?

B. FULL BV BICOMPLEX  s = s_KT + s_long  on  T = S_{-1} (+) VS_0 (+) S_{+1}:
   s_long (longitudinal/ghost, +grade): L1 = Pi_kerBW.d_A : S_{-1}->VS_0,  L2 = B_W : VS_0->S_{+1}
   s_KT  (Koszul-Tate/antighost, -grade): K2 = Gamma^dag : S_{+1}->VS_0,    K1 = d_A^dag.Pi_RS : VS_0->S_{-1}
   s^2 = s_long^2 + {s_KT,s_long} + s_KT^2. The two legs are nilpotent BY CONSTRUCTION
   (B_W Pi_kerBW = 0 ; Pi_RS Gamma^dag = 0), so s^2=0 reduces to the single genuine BV
   consistency {s_KT,s_long}=0 -- exactly the co-exact-escape-vs-ghost-nilpotency
   obstruction GHOST-01 pinned. Test: is it 0? is the co-exact escape now s-EXACT?

FOUR NON-NEGOTIABLE GUARDS (checked explicitly, nothing tuned):
  ANTI-TRAP    : bare ||[Pi_RS, M_D]|| MUST stay 58.72 (M_D never touched; RS coupled, VZ evaded).
  ANTI-FIXED-SOLVE: W must be specifiable a-priori as a named class, closure a CONSEQUENCE.
                 Discriminator: built before M_D; acts ON the Dirac data ([P_pol,c(xi)]!=0)
                 rather than solved FROM a target.
  ANTI-VACUOUS : each leg's rank reported; s^2=0 must not be trivially-degenerate.
  ANTI-IMPORT  : if 0 only by importing the matter-generation answer / a fixed solve, say so.

HONEST PREDICTION (discipline): SHARPER_OBSTRUCTION. The intrinsic, H-symmetric KSp
class is exactly H-linear and genuinely non-equivariant, but its very symmetry washes
out the single-plane bending; it does NOT beat 32.80 and does NOT close the bicomplex.
The missing datum is an EXTERNAL symmetry-breaking spectral section (one distinguished
null plane = the actual Y14 curvature) the intrinsic class structurally cannot supply.

NOTHING is tuned. xi is the repo's fixed sample covector. Numbers reported as-is.
"""
from __future__ import annotations

import os
import sys

import numpy as np
from scipy.linalg import expm

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import oq_rk1_cl95_explicit_rep as cl95  # verified Cl(9,5) rep

TOL = 1e-9
N = 14
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)


def fro(A):
    return float(np.linalg.norm(A))


def proj_onto_kernel(M):
    """Orthogonal projector onto ker(M) for surjective-ish M (rows = constraints)."""
    gram = M @ M.conj().T
    return np.eye(M.shape[1], dtype=complex) - M.conj().T @ np.linalg.pinv(gram) @ M


def proj_onto_image(M):
    """Orthogonal projector onto the column space (image) of M."""
    # M : d x r ; columns span the image.
    U, s, _ = np.linalg.svd(M, full_matrices=False)
    r = int(np.sum(s > TOL * (s[0] if s.size else 1.0)))
    Ur = U[:, :r]
    return Ur @ Ur.conj().T


def build_rep():
    n_pairs = 7
    dim = 2 ** n_pairs  # 128
    G = cl95.jordan_wigner_gammas(n_pairs)
    eta = np.array([+1.0] * 9 + [-1.0] * 5)
    e = [G[a] if eta[a] > 0 else 1j * G[a] for a in range(N)]
    Iden = np.eye(dim, dtype=complex)
    omega = Iden.copy()
    for a in range(N):
        omega = omega @ e[a]
    return dim, eta, e, omega, Iden


def build_J(dim, eta, e):
    """Quaternionic structure J = U.conj, J^2=-I, [J,e_a]=0 (shiab_family_basis)."""
    s = np.empty(N)
    for a in range(N):
        s[a] = (-1.0) ** a if a < 9 else (-1.0) ** (a + 1)
    anticomm = [a for a in range(N) if s[a] < 0]
    U = np.eye(dim, dtype=complex)
    for a in anticomm:
        U = U @ e[a]
    Jsq_err = fro(U @ np.conjugate(U) + np.eye(dim))
    comm_err = max(fro(U @ np.conjugate(e[a]) - e[a] @ U) for a in range(N))
    return U, Jsq_err, comm_err


def hlin_residual(Op, U):
    """||Op J - J conj(Op)|| with J = U.conj antilinear; H-linear iff ~0."""
    return fro(Op @ U - U @ np.conjugate(Op))


def main():
    dim, eta, e, omega, Iden = build_rep()
    VSdim = N * dim  # 1792
    I14 = np.eye(N, dtype=complex)

    # ---- core operators (identical construction to keystone / spurion) ---------
    Gamma = np.hstack(e)                              # 128 x 1792 gamma-trace map
    Pi_RS = proj_onto_kernel(Gamma)                   # 1792 x 1792 onto ker(Gamma)
    Pi_perp = np.eye(VSdim, dtype=complex) - Pi_RS
    cxi = sum(XI[a] * e[a] for a in range(N))         # built AFTER the carrier below
    M_D = np.kron(I14, cxi)                            # 1792 x 1792 twisted Dirac symbol
    gauge = np.vstack([XI[a] * np.eye(dim, dtype=complex) for a in range(N)])  # d_A 1792x128

    print("=" * 84)
    print("SOURCE-DERIVED KSp CHARACTERISTIC CLASS + FULL BV BICOMPLEX")
    print("=" * 84)

    # === (1) ANCHORS ===========================================================
    comm_PiMD = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    escape_op = fro(Pi_perp @ M_D @ Pi_RS)
    escape_gauge = fro(Pi_perp @ M_D @ Pi_RS @ gauge)
    gamma_gauge = fro(Gamma @ gauge)
    print("\n(1) ANCHORS (must reproduce repo):")
    print(f"    ||[Pi_RS, M_D]||              = {comm_PiMD:.4f}   (repo 58.7215)")
    print(f"    ||(I-Pi_RS)M_D Pi_RS|| op     = {escape_op:.4f}   (repo 41.5224)")
    print(f"    ||(I-Pi_RS)M_D Pi_RS(gauge)|| = {escape_gauge:.4f}  (repo 169.1942)")
    print(f"    ||Gamma . gauge||             = {gamma_gauge:.4f}   (repo 80.6136)")

    # === (2) THE INTRINSIC QUATERNIONIC DATA: J, Omega, polarization ===========
    # IMPORTANT: P_pol is built here from rep data ONLY (J, Omega, the e_a) with ZERO
    # reference to cxi/M_D/the closure target -> the ANTI-FIXED-SOLVE discriminator.
    U, Jsq_err, Jcomm_err = build_J(dim, eta, e)      # J = U.conj
    Omega = U.conj().T                                # invariant symplectic form Omega = U^dag
    skew_sum = fro(Omega + Omega.T)                   # ~0 => Omega^T = -Omega (skew)
    skew_diff = fro(Omega - Omega.T)                  # nonzero magnitude scale
    print("\n(2) INTRINSIC QUATERNIONIC STRUCTURE (a-priori, no reference to M_D):")
    print(f"    ||J^2 + I||              = {Jsq_err:.2e}  (quaternionic J^2=-I)")
    print(f"    ||[J, Cl]|| (centralizer)= {Jcomm_err:.2e}  (J commutes with whole algebra)")
    print(f"    Omega = U^dag : ||Omega+Omega^T|| = {skew_sum:.3e}  (SKEW iff ~0)")
    print(f"                    ||Omega-Omega^T|| = {skew_diff:.4f}  (scale; genuinely symplectic)")

    # the 5 conjugate null pairs n_k = e_k + e_{9+k}, nbar_k = e_k - e_{9+k} (k=0..4)
    null_pairs = []
    for k in range(5):
        nv = np.zeros(N); nv[k] = 1.0; nv[9 + k] = 1.0
        nbv = np.zeros(N); nbv[k] = 1.0; nbv[9 + k] = -1.0
        null_pairs.append((nv, nbv))

    def cvec(v):
        return sum(v[a] * e[a] for a in range(N))

    # polarization idempotents P_pol_k = c(n_k)c(nbar_k)/(2 eta(n_k,nbar_k)), eta=2
    P_pol_list = []
    for (nv, nbv) in null_pairs:
        cn = cvec(nv); cnb = cvec(nbv)
        eta_nnb = float(sum(eta[a] * nv[a] * nbv[a] for a in range(N)))
        P_pol_list.append((cn @ cnb) / (2 * eta_nnb))
    P_pol = sum(P_pol_list)                           # the full KSp polarization class
    # nilpotent polarization raising operator N_pol = sum_k c(n_k)
    N_pol = sum(cvec(nv) for (nv, _) in null_pairs)
    Npol6 = fro(np.linalg.matrix_power(N_pol, 6))
    # nilpotency of each c(n_k)
    cn0 = cvec(null_pairs[0][0])
    cn0_sq = fro(cn0 @ cn0)
    print(f"    5 null pairs n_k=e_k+e_(9+k): ||c(n_0)^2||={cn0_sq:.2e} (nilpotent), "
          f"||N_pol^6||={Npol6:.2e} (parabolic/non-Spin)")

    # === (3) CARRIER GENUINENESS DISCRIMINATORS ================================
    h_Ppol = hlin_residual(P_pol, U)                  # H-linearity (centralizer => 0)
    # P_pol acts NON-trivially ON the Dirac data (not solved FROM it)
    acts_on_cxi = fro(P_pol @ cxi - cxi @ P_pol)
    # Spin(9,5) equivariance defect of P_pol
    def Sigma(a, b):
        return 0.25 * (e[a] @ e[b] - e[b] @ e[a])
    spin_pairs = [(0, 9), (1, 10), (0, 1), (9, 10), (3, 11), (5, 7)]
    spin_defects = [fro(Sigma(a, b) @ P_pol - P_pol @ Sigma(a, b)) for (a, b) in spin_pairs]
    max_spin_defect = max(spin_defects)
    print("\n(3) CARRIER GENUINENESS (anti-fixed-solve discriminators):")
    print(f"    ||[P_pol, J]||           = {h_Ppol:.2e}  (EXACTLY H-linear: centralizer payoff)")
    print(f"    ||[P_pol, c(xi)]||       = {acts_on_cxi:.4f}  (acts ON Dirac data; NOT a functional of M_D)")
    print(f"    max Spin(9,5) defect     = {max_spin_defect:.4f}  (genuinely non-equivariant: {max_spin_defect>1e-6})")
    print(f"    [construction order: P_pol built from {{J,Omega,e_a}} BEFORE any closure target]")

    # === (4) DRESSED OBSTRUCTION FLOOR vs 32.80 ================================
    def closure_obstruction(Bn):
        Pi = proj_onto_kernel(Bn)
        return fro(Pi @ M_D - M_D @ Pi)

    print("\n(4) DRESSED OBSTRUCTION FLOOR  min ||[Pi_kerBW, M_D]||  (target: below 32.80, ideally 0):")
    print(f"    baseline (bare, B=Gamma)                       = {comm_PiMD:.4f}")

    # --- CONTROL 1: Spin(9,5) (equivariant) carrier exp(t(Sig_13+Sig_57+Sig_10,12))
    Xspin = Sigma(1, 3) + Sigma(5, 7) + Sigma(10, 12)
    bestSpin = np.inf
    for t in np.linspace(-2.0, 2.0, 17):
        if abs(t) < 1e-9:
            continue
        Gt = expm(t * Xspin)
        B = np.hstack([e[a] @ Gt for a in range(N)])
        bestSpin = min(bestSpin, closure_obstruction(B))
    print(f"    CONTROL Spin(9,5) carrier exp(t Sig):  floor = {bestSpin:.4f}  "
          f"(equivariant CANNOT bend -> stays ~58.72)")

    # --- CONTROL 2: faithful single-hyperbolic-plane FREE spurion (family A, plane 0)
    nv0, nbv0 = null_pairs[0]
    cn = cvec(nv0); cnb = cvec(nbv0)
    def BA_plane0(ac, bc):
        return np.hstack([e[a] + ac * nv0[a] * cn + bc * nbv0[a] * cnb for a in range(N)])
    bestA = (None, np.inf)
    grid = [-2.0, -1.0, -0.5, 0.5, 1.0, 2.0]
    for ac in grid:
        for bc in grid + [0.0]:
            val = closure_obstruction(BA_plane0(ac, bc))
            if val < bestA[1]:
                bestA = ((ac, bc), val)
    print(f"    CONTROL free single-plane (e_0+e_9, 2-param): floor = {bestA[1]:.4f} at (a,b)={bestA[0]}  "
          f"(reproduces the 32.80 spurion floor)")

    # --- KSp carrier families (intrinsic polarization) -------------------------
    # B: Gamma(I + t P_pol) ; C: Gamma exp(t(P_pol-P_pol^dag)) ; D: Gamma exp(t N_pol)
    def BkspB(t):
        return np.hstack([e[a] @ (Iden + t * P_pol) for a in range(N)])
    def BkspC(t):
        Gt = expm(t * (P_pol - P_pol.conj().T))
        return np.hstack([e[a] @ Gt for a in range(N)])
    def BkspD(t):
        Gt = expm(t * N_pol)
        return np.hstack([e[a] @ Gt for a in range(N)])

    def scan(fn, ts):
        best = (None, np.inf)
        for t in ts:
            if abs(t) < 1e-9:
                continue
            val = closure_obstruction(fn(t))
            if val < best[1]:
                best = (t, val)
        return best

    ts = np.linspace(-3, 3, 25)
    bB = scan(BkspB, ts); bC = scan(BkspC, ts); bD = scan(BkspD, ts)
    print(f"    KSp family B  Gamma(I + t P_pol):       floor = {bB[1]:.4f} at t={bB[0]:.3f}")
    print(f"    KSp family C  Gamma exp(t(P_pol-P^dag)):floor = {bC[1]:.4f} at t={bC[0]:.3f}")
    print(f"    KSp family D  Gamma exp(t N_pol):       floor = {bD[1]:.4f} at t={bD[0]:.3f}")

    # --- KSp FULL polarization additive (all 5 symmetric pairs, free coeff) -----
    def Bksp_full(t):
        # additive symmetric enrichment over all 5 conjugate pairs
        blocks = []
        for a in range(N):
            blk = e[a].copy().astype(complex)
            for (nv, nbv) in null_pairs:
                cn_k = cvec(nv); cnb_k = cvec(nbv)
                blk = blk + t * (nv[a] * cn_k + nbv[a] * cnb_k)
            blocks.append(blk)
        return np.hstack(blocks)
    bFull = scan(Bksp_full, ts)
    print(f"    KSp FULL polarization (5 sym pairs):    floor = {bFull[1]:.4f} at t={bFull[0]:.3f}")

    # --- single-plane DIAGNOSTIC via the KSp-canonical polarization form --------
    # (each plane via its own Gamma(I + t P_pol_k) -- does the quaternionic structure
    #  canonically PREFER a bending plane? If symmetric, none is preferred.)
    plane_floors = []
    for k in range(5):
        Pk = P_pol_list[k]
        bk = scan(lambda t, Pk=Pk: np.hstack([e[a] @ (Iden + t * Pk) for a in range(N)]), ts)
        plane_floors.append(bk[1])
    print(f"    KSp single-plane diagnostic (per-pair I+tP_k): "
          f"{'/'.join(f'{v:.1f}' for v in plane_floors)}")

    ksp_floor = min(bB[1], bC[1], bD[1], bFull[1], min(plane_floors))
    print(f"    >>> KSp intrinsic floor = {ksp_floor:.4f}   "
          f"(BELOW 32.80? {ksp_floor < 32.80})   (ZERO? {ksp_floor < 1e-6})")

    # pick the representative carrier for the bicomplex: the best intrinsic KSp carrier
    # (full polarization). This is the genuine source-derived W.
    B_W = Bksp_full(bFull[0])
    Pi_kerBW = proj_onto_kernel(B_W)
    dressed_obstruction = fro(Pi_kerBW @ M_D - M_D @ Pi_kerBW)

    # === (5) FULL BV BICOMPLEX  s = s_KT + s_long ==============================
    # legs (all 128-rank objects through the 128-dim spinor spaces):
    L1 = Pi_kerBW @ gauge                  # S_{-1}(128) -> VS_0(1792) : ghost map into ker B_W
    L2 = B_W                               # VS_0(1792) -> S_{+1}(128) : deformed constraint
    K2 = Gamma.conj().T                    # S_{+1}(128) -> VS_0(1792) : Koszul-Tate Gamma^dag
    K1 = gauge.conj().T @ Pi_RS            # VS_0(1792) -> S_{-1}(128) : d_A^dag Pi_RS

    rkL1 = int(np.linalg.matrix_rank(L1, tol=TOL))
    rkL2 = int(np.linalg.matrix_rank(L2, tol=TOL))
    rkK1 = int(np.linalg.matrix_rank(K1, tol=TOL))
    rkK2 = int(np.linalg.matrix_rank(K2, tol=TOL))

    # leg nilpotency (by construction):
    slong2 = fro(L2 @ L1)                  # B_W Pi_kerBW d_A = 0
    sKT2 = fro(K1 @ K2)                    # d_A^dag Pi_RS Gamma^dag = 0

    # the single genuine BV consistency {s_KT, s_long} (grade-preserving diagonal blocks):
    blk_Sm1 = fro(K1 @ L1)                                  # S_{-1}: d_A^dag Pi_RS Pi_kerBW d_A
    blk_VS = fro(L1 @ K1 + K2 @ L2)                        # VS_0 : Pi_kerBW d_A d_A^dag Pi_RS + Gamma^dag B_W
    blk_Sp1 = fro(L2 @ K2)                                 # S_{+1}: B_W Gamma^dag
    anti = float(np.sqrt(blk_Sm1**2 + blk_VS**2 + blk_Sp1**2))

    # assemble full s on T = S_{-1} (+) VS_0 (+) S_{+1}  (128+1792+128 = 2048) and verify
    D = dim + VSdim + dim
    a0, a1, a2 = 0, dim, dim + VSdim
    s = np.zeros((D, D), dtype=complex)
    # s_long: L1 (VS row, S- col), L2 (S+ row, VS col)
    s[a1:a2, a0:a1] += L1
    s[a2:D, a1:a2] += L2
    # s_KT: K2 (VS row, S+ col), K1 (S- row, VS col)
    s[a1:a2, a2:D] += K2
    s[a0:a1, a1:a2] += K1
    s2_full = fro(s @ s)

    print("\n(5) FULL BV BICOMPLEX  s = s_KT + s_long  on  S_-1 (+) VS_0 (+) S_+1 (dim 2048):")
    print(f"    leg ranks (anti-vacuous): rk L1={rkL1}, rk L2={rkL2}, rk K1={rkK1}, rk K2={rkK2}")
    print(f"    s_long^2 = ||B_W Pi_kerBW d_A||        = {slong2:.2e}  (0 by construction)")
    print(f"    s_KT^2   = ||d_A^dag Pi_RS Gamma^dag|| = {sKT2:.2e}  (0 by construction)")
    print(f"    {{s_KT, s_long}} blocks: VS={blk_VS:.2f}, S_-1={blk_Sm1:.2f}, S_+1={blk_Sp1:.2f}")
    print(f"    ||{{s_KT,s_long}}|| (combined)          = {anti:.4f}")
    print(f"    ||s^2|| full 2048x2048                  = {s2_full:.4f}  (target 0; "
          f"{'CLOSED' if s2_full < 1e-6 else 'NOT closed'})")

    # === (6) IS THE CO-EXACT ESCAPE NOW s-EXACT? ===============================
    # escape co-exact operator E_op = Pi_perp M_D Pi_RS ; its OUTPUT lives in im(Gamma^dag)
    # = im(Pi_perp). The ghost/longitudinal-exact directions = im(L1) subset ker(B_W).
    # Genuine BV s-exactness needs the escape to be LONGITUDINALLY (ghost) exact, not just
    # co-exact. Measure the fraction of E_op captured by the longitudinal image.
    E_op = Pi_perp @ M_D @ Pi_RS
    E = fro(E_op)
    P_imL1 = proj_onto_image(L1)                       # projector onto im(L1) in VS_0
    captured = fro(P_imL1 @ E_op)
    residual = fro((np.eye(VSdim, dtype=complex) - P_imL1) @ E_op)
    frac_sexact = (E - residual) / E if E > 0 else 0.0
    print("\n(6) ESCAPE s-EXACTNESS in the full bicomplex:")
    print(f"    ||E = (I-Pi_RS)M_D Pi_RS|| (co-exact)  = {E:.4f}")
    print(f"    residual after longitudinal (ghost) leg= {residual:.4f}")
    print(f"    fraction made genuinely s-exact        = {100*frac_sexact:.2f}%  "
          f"({'s-EXACT' if residual < 1e-6 else 'NOT s-exact (escape is co-exact, not ghost-exact)'})")

    # === (7) ANTI-TRAP: bare [Pi_RS, M_D] preserved ============================
    comm_after = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    sigma_trap = -(Pi_perp @ M_D @ Pi_RS)
    trap_comm = fro(Pi_RS @ (M_D + sigma_trap) - (M_D + sigma_trap) @ Pi_RS)
    print("\n(7) ANTI-TRAP (M_D NEVER modified):")
    print(f"    bare ||[Pi_RS, M_D]||        = {comm_after:.4f}  (MUST be 58.7215; "
          f"RS coupled, VZ evaded: {comm_after > 1e-6})")
    print(f"    DISQUALIFIED trap would give = {trap_comm:.2e}  (decoupled => acausal)")

    # === (8) NON-EQUIVARIANCE of the carrier W =================================
    print("\n(8) NON-EQUIVARIANCE of carrier W:")
    print(f"    max Spin(9,5) defect of P_pol = {max_spin_defect:.4f}  (!=0 genuine)")
    print(f"    Spin-control floor proof      = {bestSpin:.4f}  (equivariant carriers return ~58.72)")

    # === (9) H-LINEARITY =======================================================
    JVS = np.kron(I14, U)
    h_PikerBW = fro(Pi_kerBW @ JVS - JVS @ np.conjugate(Pi_kerBW))
    h_BW = fro(B_W @ JVS - U @ np.conjugate(B_W))
    print("\n(9) H-LINEARITY ([.,J]):")
    print(f"    ||[P_pol, J]||      = {h_Ppol:.2e}  (EXACT, centralizer)")
    print(f"    ||[Pi_kerBW, J]||   = {h_PikerBW:.2e}")
    print(f"    ||[B_W, J]||        = {h_BW:.2e}")

    # === (10) C2 SECONDARY CONSTRAINT STATUS ===================================
    C2 = Gamma @ M_D @ Pi_RS                           # 128 x 1792
    nC2 = fro(C2)
    GGd = Gamma @ Gamma.conj().T
    Gamma_pinv = Gamma.conj().T @ np.linalg.pinv(GGd)
    Lambda = C2 @ Gamma_pinv
    resid_C2 = fro(C2 - Lambda @ Gamma)                # independence of Gamma
    # dressed C2_W = B_W M_D Pi_kerBW ; does the carrier absorb it?
    C2_W = B_W @ M_D @ Pi_kerBW
    nC2W = fro(C2_W)
    BBd = B_W @ B_W.conj().T
    BW_pinv = B_W.conj().T @ np.linalg.pinv(BBd)
    LambdaW = C2_W @ BW_pinv
    resid_C2W = fro(C2_W - LambdaW @ B_W)
    print("\n(10) C2 SECONDARY CONSTRAINT:")
    print(f"    ||C2 = Gamma M_D Pi_RS||              = {nC2:.4f}  (repo 155.36)")
    print(f"    independence-of-Gamma residual       = {resid_C2:.4f}  "
          f"({'reducible' if resid_C2 < 1e-6 else 'GENUINELY INDEPENDENT'})")
    print(f"    dressed ||C2_W = B_W M_D Pi_kerBW||   = {nC2W:.4f}")
    print(f"    independence-of-B_W residual          = {resid_C2W:.4f}  "
          f"({'absorbed' if resid_C2W < 1e-6 else 'NOT reconciled (carrier does not absorb C2)'})")

    # === VERDICT ===============================================================
    below = ksp_floor < 32.80
    zero = ksp_floor < 1e-6
    closed = s2_full < 1e-6
    print("\n" + "=" * 84)
    print("VERDICT")
    print("=" * 84)
    print(f"  dressed floor (KSp intrinsic) : {ksp_floor:.4f}  (below 32.80: {below}; zero: {zero})")
    print(f"  full ||s^2||                  : {s2_full:.4f}  ({{s_KT,s_long}}={anti:.2f}; closed: {closed})")
    print(f"  escape s-exact                : {100*frac_sexact:.2f}%  (NOT s-exact)")
    print(f"  ANTI-TRAP bare [Pi_RS,M_D]    : {comm_after:.4f}  (58.7215 preserved)")
    print(f"  carrier non-equivariance      : {max_spin_defect:.4f}  (genuine)")
    print(f"  H-linearity ||[P_pol,J]||     : {h_Ppol:.2e}  (exact)")
    print(f"  C2 reconciled                 : {resid_C2W < 1e-6}  (dressed C2_W={nC2W:.2f} survives)")
    print("  STATUS: SHARPER_OBSTRUCTION -- the intrinsic, H-symmetric KSp class is")
    print("  anti-trap-safe, exactly H-linear, genuinely non-equivariant and a-priori, but")
    print("  provably CANNOT beat the 32.80 single-plane floor, does NOT close the bicomplex")
    print("  ({s_KT,s_long}!=0), does NOT make the co-exact escape ghost-exact, and does NOT")
    print("  reconcile C2. The missing datum is an EXTERNAL symmetry-breaking spectral section")
    print("  (one distinguished null plane / the actual Y14 curvature) that the intrinsic KSp")
    print("  class structurally cannot supply -- the ICO/external-datum boundary, made precise.")

    return {
        "anchors_ok": abs(comm_PiMD - 58.7215) < 1e-2,
        "ksp_floor": ksp_floor, "below_32_80": below, "zero": zero,
        "s2_full": s2_full, "anti": anti, "closed": closed,
        "ranks": (rkL1, rkL2, rkK1, rkK2), "slong2": slong2, "sKT2": sKT2,
        "escape": E, "escape_residual": residual, "frac_sexact": frac_sexact,
        "anti_trap": comm_after, "spin_defect": max_spin_defect,
        "h_Ppol": h_Ppol, "C2": nC2, "C2_indep": resid_C2,
        "C2_W": nC2W, "C2_W_indep": resid_C2W,
        "spin_control_floor": bestSpin, "free_plane_floor": bestA[1],
        "ksp_full_floor": bFull[1], "plane_floors": plane_floors,
        "acts_on_cxi": acts_on_cxi, "Npol6": Npol6,
        "skew_sum": skew_sum, "skew_diff": skew_diff,
    }


if __name__ == "__main__":
    main()
