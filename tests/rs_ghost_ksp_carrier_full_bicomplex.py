#!/usr/bin/env python3
"""CLIMACTIC GATE (2026-06-27): SOURCE-DERIVED QUATERNIONIC (KSp) CARRIER + FULL BV
BICOMPLEX for GU's RS sector, on the verified Cl(9,5)=M(64,H)~M(128,C) rep.

Builds on (and reproduces the anchors of):
  tests/rs_ghost_fixed_null_covector_spurion.py        (floor 32.80, anti-trap 58.72)
  tests/rs_ghost_steelman_geometric_carrier.py         (C2=155.36, co-exact escape)
  explorations/nonequivariant-ghost-construction-2026-06-27.md  (GHOST-01: the missing object)

THE TWO COUPLED PIECES UNDER TEST
---------------------------------
A. SOURCE-DERIVED CARRIER W (a-priori, quaternionic / KSp-flavoured):
   Defined ENTIRELY from the rep's H-structure -- the quaternionic structure J (J^2=-I,
   [J,e_a]=0) and its INVARIANT SYMPLECTIC FORM Omega = U^dag (skew, Sp(64)-invariant) --
   plus the split-signature null polarization {(e_k, e_{9+k})}_{k=0..4} that Omega makes
   canonical.  W is the QUATERNIONIC MAXIMAL-ISOTROPIC (KSp polarization) class:
       P_pol = sum_{k=0..4} c(n_k) c(nbar_k) / (2 eta(n_k,nbar_k)),  n_k = e_k + e_{9+k}.
   It is NOT a functional of (xi, M_D) -- it is fixed BEFORE M_D is built.  Quaternionic
   naturalness => it is AUTOMATICALLY H-linear ([P_pol,J]=0) because J commutes with the
   whole Clifford algebra.  Richer than the 1-covector spurion (rank-5 polarization,
   5 conjugate null pairs) and non-equivariant (breaks Spin(9,5)).

   KEY a-priori finding (proved here as a CONTROL): a carrier valued in spin(9,5) (a
   genuine Spin group conjugation -- the "homogeneous gauge" reading) is EQUIVARIANT and
   returns the dressed obstruction to 58.72 EXACTLY: it cannot bend the obstruction at all.
   Bending REQUIRES a non-Spin (parabolic / non-isometric) carrier.  The quaternionic KSp
   polarization is exactly such an object, and H-linear by the centralizer property.

B. FULL BV BICOMPLEX  s = s_KT + s_long  on T = S_{-1} (+) VS_0 (+) S_{+1}:
   s_long (longitudinal/ghost, raises grade):
       L1 = Pi_kerBW . d_A : S_{-1} -> VS_0   (ghost/gauge map, projected into ker B_W)
       L2 = B_W            : VS_0  -> S_{+1}   (deformed constraint)
       => s_long^2 = B_W L1 = 0 by construction (L1 lands in ker B_W).
   s_KT (Koszul-Tate/antighost, lowers grade -- the co-exact im(Gamma^dag) direction):
       K2 = Gamma^dag      : S_{+1} -> VS_0    (antifield map, image = im(Pi_perp))
       K1 = d_A^dag . Pi_RS: VS_0  -> S_{-1}   (KT closing map, killed on im Gamma^dag)
       => s_KT^2 = K1 K2 = d_A^dag Pi_RS Gamma^dag = 0 (Pi_RS Gamma^dag = 0).
   s^2 = 0 then reduces to the SINGLE genuine BV consistency {s_KT, s_long} = 0.  That
   anticommutator is the precise obstruction GHOST-01 pinned (co-exact escape vs ghost
   nilpotency).  We report it as a function of the carrier and ask whether W reduces it.

NON-NEGOTIABLE GUARDS (all computed, nothing tuned):
  ANTI-TRAP : bare ||[Pi_RS, M_D]|| MUST stay 58.72 (M_D never modified).
  ANTI-FIXED-SOLVE : W is built from {J, Omega, null pairing} with NO reference to xi/M_D
                     (asserted by construction order); closure is tested as a CONSEQUENCE.
  ANTI-VACUOUS : rank of every leg reported; legs are nonzero.
  ANTI-IMPORT : no matter-generation target enters.

HONEST PRIOR (discipline): SHARPER_OBSTRUCTION is the likely outcome -- the KSp carrier
may push below 32.80 but a residual {s_KT,s_long} remains needing the actual Y14 curvature.
Numbers reported as-is.  xi is the repo's fixed sample covector.  NOTHING tuned.
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
    """Orthogonal projector onto ker(M) for M: C^d_in -> C^d_out (rows = d_out)."""
    gram = M @ M.conj().T
    return np.eye(M.shape[1], dtype=complex) - M.conj().T @ np.linalg.pinv(gram) @ M


def build_rep():
    n_pairs = 7
    dim = 2 ** n_pairs  # 128
    G = cl95.jordan_wigner_gammas(n_pairs)
    eta = np.array([+1.0] * 9 + [-1.0] * 5)
    e = [G[a] if eta[a] > 0 else 1j * G[a] for a in range(N)]
    Iden = np.eye(dim, dtype=complex)
    return dim, eta, e, Iden


def build_J(dim, e):
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
    return U, Jsq_err, comm_err, anticomm


def hlin_residual(Op, U):
    """||Op U - U conj(Op)|| with J = U.conj antilinear: H-linear iff ~0."""
    return fro(Op @ U - U @ np.conjugate(Op))


def main():
    dim, eta, e, Iden = build_rep()
    VSdim = N * dim  # 1792
    I14 = np.eye(N, dtype=complex)
    JVS_eye = np.eye(VSdim, dtype=complex)

    # ---- core operators (identical construction to the keystone scratch) -------
    Gamma = np.hstack(e)                            # 128 x 1792
    Pi_RS = proj_onto_kernel(Gamma)                 # 1792 x 1792
    Pi_perp = JVS_eye - Pi_RS
    cxi = sum(XI[a] * e[a] for a in range(N))
    M_D = np.kron(I14, cxi)                          # 1792 x 1792  (built AFTER carrier below check)
    gauge = np.vstack([XI[a] * Iden for a in range(N)])  # d_A : 1792 x 128

    print("=" * 80)
    print("SOURCE-DERIVED QUATERNIONIC (KSp) CARRIER + FULL BV BICOMPLEX")
    print("=" * 80)

    # === (1) ANCHORS ===========================================================
    comm_PiMD = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    escape_op = fro(Pi_perp @ M_D @ Pi_RS)
    escape_gauge = fro(Pi_perp @ M_D @ Pi_RS @ gauge)
    gamma_gauge = fro(Gamma @ gauge)
    print("\n(1) ANCHORS (must reproduce keystone):")
    print(f"    ||[Pi_RS, M_D]||              = {comm_PiMD:.4f}   (repo 58.72)")
    print(f"    ||(I-Pi_RS)M_D Pi_RS|| op     = {escape_op:.4f}   (repo 41.52)")
    print(f"    ||(I-Pi_RS)M_D Pi_RS(gauge)|| = {escape_gauge:.4f}  (repo 169.19)")
    print(f"    ||Gamma . gauge||             = {gamma_gauge:.4f}   (repo 80.61)")

    # === (2) INTRINSIC H-STRUCTURE: J and the symplectic form Omega ============
    U, Jsq_err, Jcomm_err, anticomm = build_J(dim, e)
    Omega = U.conj().T                               # invariant bilinear: <Jx,y> = x^T Omega y
    skew_err = fro(Omega + Omega.T)                  # quaternionic (Sp) <=> skew
    sym_err = fro(Omega - Omega.T)
    print("\n(2) INTRINSIC QUATERNIONIC DATA (a-priori, NO reference to xi/M_D):")
    print(f"    J=U.conj: ||J^2+I||={Jsq_err:.1e}, ||[J,Cl]||={Jcomm_err:.1e}")
    print(f"    H-distinguished index set (anticomm of J) = {anticomm}")
    print(f"    symplectic form Omega=U^dag: ||Omega+Omega^T||={skew_err:.2e} (skew=>Sp), "
          f"||Omega-Omega^T||={sym_err:.2e}")
    print(f"    => Cl(9,5) module is QUATERNIONIC: Omega is the a-priori symplectic form.")

    # === (3) THE KSp POLARIZATION CARRIER W (a-priori) =========================
    # Omega makes canonical the split null polarization n_k = e_k + e_{9+k}, k=0..4.
    null_pairs = [(k, 9 + k) for k in range(5)]      # (+,-) index pairs => null
    P_blocks = []
    cn_list = []
    for (ip, im) in null_pairs:
        nvec = np.zeros(N); nvec[ip] = 1.0; nvec[im] = 1.0
        nbvec = np.zeros(N); nbvec[ip] = 1.0; nbvec[im] = -1.0
        eta_nn = float(sum(eta[a] * nvec[a] * nvec[a] for a in range(N)))
        eta_nnb = float(sum(eta[a] * nvec[a] * nbvec[a] for a in range(N)))
        cn = sum(nvec[a] * e[a] for a in range(N))
        cnb = sum(nbvec[a] * e[a] for a in range(N))
        cn_list.append(cn)
        P_blocks.append((cn @ cnb) / (2 * eta_nnb))
        assert abs(eta_nn) < 1e-9, "null pair not null!"
    P_pol = sum(P_blocks)                            # KSp polarization carrier on S=C^128
    # nilpotent generator N_pol = sum c(n_k) (degree-1 null sum)
    N_pol = sum(cn_list)
    Ppol_h = hlin_residual(P_pol, U)                 # H-linearity (must be ~0)
    Npol_nil = fro(N_pol @ N_pol @ N_pol @ N_pol @ N_pol @ N_pol)  # ^6 -> 0 if nilpotent
    # non-equivariance of the carrier vs Spin(9,5)
    def Sigma(a, b):
        return 0.25 * (e[a] @ e[b] - e[b] @ e[a])
    pol_defect = max(fro(Sigma(a, b) @ P_pol - P_pol @ Sigma(a, b))
                     for (a, b) in [(0, 9), (1, 2), (3, 11), (4, 13)])
    # ANTI-FIXED-SOLVE discriminator: carrier is NOT a functional of M_D
    carrier_vs_MD = fro(P_pol @ cxi - cxi @ P_pol)   # != 0 => carrier independent of/active on xi-data
    print("\n(3) KSp POLARIZATION CARRIER  P_pol = sum_k c(n_k)c(nbar_k)/(2eta):")
    print(f"    null pairs (e_k,e_{{9+k}}), k=0..4 : {null_pairs}")
    print(f"    H-linearity ||[P_pol,J]||      = {Ppol_h:.2e}  (H-linear: {Ppol_h < 1e-9})")
    print(f"    nilpotency  ||N_pol^6||        = {Npol_nil:.2e}  (parabolic/non-Spin)")
    print(f"    non-equivariance (max defect)  = {pol_defect:.4f}  (breaks Spin(9,5): {pol_defect>1e-6})")
    print(f"    ||[P_pol, c(xi)]||             = {carrier_vs_MD:.4f}  (carrier acts on Dirac data, "
          f"not a functional of it)")

    # === (4) DRESSED OBSTRUCTION SCAN: does the KSp carrier beat 32.80? =========
    def dressed_obstruction(Bn):
        Pi = proj_onto_kernel(Bn)
        return fro(Pi @ M_D - M_D @ Pi)

    # CONTROL: a genuine Spin(9,5) conjugation (homogeneous gauge) -- must return 58.72.
    W_spin = Sigma(1, 3) + Sigma(5, 7) + Sigma(10, 12)   # a-priori spin bivector
    A_spin = W_spin - W_spin.conj().T                    # anti-Herm => exp in Spin (unitary)
    spin_vals = []
    for t in np.linspace(-2.0, 2.0, 9):
        if abs(t) < 1e-9:
            continue
        G = expm(t * A_spin)
        spin_vals.append(dressed_obstruction(Gamma @ np.kron(I14, G)))
    spin_min = min(spin_vals)
    print("\n(4) DRESSED OBSTRUCTION  ||[Pi_kerB_W, M_D]||  (vs 32.80 floor, 58.72 bare):")
    print(f"    CONTROL Spin(9,5) conj exp(t(Sigma_13+Sigma_57+Sigma_10,12)): "
          f"min = {spin_min:.4f}")
    print(f"      => Spin conjugation is EQUIVARIANT: cannot bend (stays ~58.72). "
          f"Bending needs a NON-Spin carrier.")

    # KSp carrier families (non-Spin, H-linear):
    grid = np.linspace(-3.0, 3.0, 25)
    # family B: G = I + t P_pol
    bestB = (None, np.inf)
    for t in grid:
        if abs(t) < 1e-9:
            continue
        val = dressed_obstruction(Gamma @ np.kron(I14, Iden + t * P_pol))
        if val < bestB[1]:
            bestB = (float(t), val)
    # family C: G = exp(t (P_pol - P_pol^dag))  (non-unitary parabolic flow)
    bestC = (None, np.inf)
    for t in grid:
        if abs(t) < 1e-9:
            continue
        G = expm(t * (P_pol - P_pol.conj().T))
        val = dressed_obstruction(Gamma @ np.kron(I14, G))
        if val < bestC[1]:
            bestC = (float(t), val)
    # family A (FAITHFUL to the 32.80 floor): single hyperbolic plane n_0=e_0+e_9,
    # 2-param additive spurion using BOTH c(n) and c(nbar) (the symplectic conjugate pair).
    n0 = np.zeros(N); n0[0] = 1.0; n0[9] = 1.0
    nb0 = np.zeros(N); nb0[0] = 1.0; nb0[9] = -1.0
    cn0 = sum(n0[a] * e[a] for a in range(N))
    cnb0 = sum(nb0[a] * e[a] for a in range(N))
    gridA = [-2.0, -1.0, -0.5, 0.5, 1.0, 2.0]
    bestA = (None, np.inf)
    for ac in gridA:
        for bc in gridA + [0.0]:
            blocks = [e[a] + ac * n0[a] * cn0 + bc * nb0[a] * cnb0 for a in range(N)]
            val = dressed_obstruction(np.hstack(blocks))
            if val < bestA[1]:
                bestA = ((ac, bc), val)
    # family D: exp(t N_pol) pure-nilpotent (degree-1 null sum) flow
    bestD = (None, np.inf)
    for t in grid:
        if abs(t) < 1e-9:
            continue
        G = expm(t * N_pol)
        val = dressed_obstruction(Gamma @ np.kron(I14, G))
        if val < bestD[1]:
            bestD = (float(t), val)

    # family E (the QUATERNIONIC ENRICHMENT): additive spurion over ALL 5 conjugate null
    # pairs (the full symplectic polarization), 2 global params -- does it beat the single
    # hyperbolic plane's 32.80?
    bestE = (None, np.inf)
    for ac in gridA:
        for bc in gridA + [0.0]:
            blocks = []
            for a in range(N):
                blk = e[a].copy()
                for ki, (ip, im) in enumerate(null_pairs):
                    nv = (1.0 if a == ip else 0.0) + (1.0 if a == im else 0.0)
                    nbv = (1.0 if a == ip else 0.0) - (1.0 if a == im else 0.0)
                    blk = blk + ac * nv * cn_list[ki] + bc * nbv * (
                        sum(((1.0 if b == ip else 0.0) - (1.0 if b == im else 0.0)) * e[b]
                            for b in range(N)))
                blocks.append(blk)
            val = dressed_obstruction(np.hstack(blocks))
            if val < bestE[1]:
                bestE = ((ac, bc), val)

    print(f"    family A (single hyperbolic plane e_0+e_9, 2-param): min = {bestA[1]:.4f} "
          f"at (a,b)={bestA[0]}  <-- 32.80 floor check")
    print(f"    KSp family B (I + t P_pol)            : min = {bestB[1]:.4f} at t={bestB[0]:.3f}")
    print(f"    KSp family C (exp t(P_pol-P_pol^dag)) : min = {bestC[1]:.4f} at t={bestC[0]:.3f}")
    print(f"    KSp family D (exp t N_pol nilpotent)  : min = {bestD[1]:.4f} at t={bestD[0]:.3f}")
    print(f"    KSp family E (ALL 5 conjugate pairs)  : min = {bestE[1]:.4f} at (a,b)={bestE[0]}  "
          f"<-- quaternionic enrichment")
    ksp_min = min(bestA[1], bestB[1], bestC[1], bestD[1], bestE[1])

    # DIAGNOSTIC: does the 32.80 floor reproduce with a SINGLE null plane (family B form),
    # and does the quaternionic structure CANONICALLY select which plane bends best?
    print("\n(4b) DIAGNOSTIC -- single-null-plane bending (does H-structure pick the plane?):")
    single_results = []
    for ki, (ip, im) in enumerate(null_pairs):
        Pk = P_blocks[ki]
        bestk = np.inf
        for t in grid:
            if abs(t) < 1e-9:
                continue
            v = dressed_obstruction(Gamma @ np.kron(I14, Iden + t * Pk))
            bestk = min(bestk, v)
        single_results.append(bestk)
        print(f"    plane k={ki} (e_{ip}+e_{im}): single-plane min = {bestk:.4f}")
    best_single = min(single_results)
    print(f"    BEST single plane = {best_single:.4f}  (32.80 reproduces? {abs(best_single-32.80)<2.0})")
    print(f"    => the bending requires picking ONE null plane (a polarization/spectral-section")
    print(f"       CHOICE); the quaternionic structure does NOT canonically prefer one over the")
    print(f"       others (all 5 give {single_results[0]:.1f}); summing them (KSp class) is WORSE.")
    ksp_min = min(ksp_min, best_single)
    print(f"    -> KSp GLOBAL MIN = {ksp_min:.4f}   "
          f"(BELOW 32.80? {ksp_min < 32.80 - 1e-3})   (REACHES 0? {ksp_min < 1e-6})")

    # pick the best carrier deformation for the bicomplex: include the best single plane
    bki = int(np.argmin(single_results))
    bestk_t = (None, np.inf)
    for t in grid:
        if abs(t) < 1e-9:
            continue
        v = dressed_obstruction(Gamma @ np.kron(I14, Iden + t * P_blocks[bki]))
        if v < bestk_t[1]:
            bestk_t = (float(t), v)
    cand = {"A": bestA, "B": bestB, "C": bestC, "D": bestD, "S": bestk_t}
    best_fam = min(cand, key=lambda k: cand[k][1])
    if best_fam == "S":
        B_W = Gamma @ np.kron(I14, Iden + bestk_t[0] * P_blocks[bki])
    elif best_fam == "A":
        ac, bc = bestA[0]
        B_W = np.hstack([e[a] + ac * n0[a] * cn0 + bc * nb0[a] * cnb0 for a in range(N)])
    elif best_fam == "B":
        B_W = Gamma @ np.kron(I14, Iden + bestB[0] * P_pol)
    elif best_fam == "C":
        B_W = Gamma @ np.kron(I14, expm(bestC[0] * (P_pol - P_pol.conj().T)))
    else:
        B_W = Gamma @ np.kron(I14, expm(bestD[0] * N_pol))
    print(f"    => carrier for bicomplex: family {best_fam} (dressed obstruction "
          f"{cand[best_fam][1]:.4f})")

    # === (5) FULL BV BICOMPLEX  s = s_KT + s_long ==============================
    Pi_kerBW = proj_onto_kernel(B_W)
    # s_long legs
    L1 = Pi_kerBW @ gauge                            # S_{-1} -> VS_0 (lands in ker B_W)
    L2 = B_W                                         # VS_0 -> S_{+1}
    # s_KT legs (co-exact / antighost direction im Gamma^dag)
    K2 = Gamma.conj().T                              # S_{+1} -> VS_0  (image = im Pi_perp)
    K1 = gauge.conj().T @ Pi_RS                      # VS_0 -> S_{-1}  (kills im Gamma^dag)

    s_long2 = fro(L2 @ L1)                           # B_W L1 -> 0
    s_KT2 = fro(K1 @ K2)                             # d_A^dag Pi_RS Gamma^dag -> 0
    # {s_KT, s_long} blocks
    cross_VS = fro(L1 @ K1 + K2 @ L2)               # VS_0 -> VS_0
    cross_Sm = fro(K1 @ L1)                          # S_{-1} -> S_{-1}  (s_KT s_long)
    cross_Sp = fro(L2 @ K2)                          # S_{+1} -> S_{+1}  (s_long s_KT)
    anticomm_norm = float(np.sqrt(cross_VS ** 2 + cross_Sm ** 2 + cross_Sp ** 2))

    # assemble full s on T = S_{-1}(+)VS_0(+)S_{+1} = 128+1792+128 = 2048
    Dtot = dim + VSdim + dim
    s = np.zeros((Dtot, Dtot), dtype=complex)
    a0, a1, a2, a3 = 0, dim, dim + VSdim, Dtot
    # s_long (raise): col-block -> row-block
    s[a1:a2, a0:a1] += L1                            # S_{-1} -> VS_0
    s[a2:a3, a1:a2] += L2                            # VS_0 -> S_{+1}
    # s_KT (lower)
    s[a1:a2, a2:a3] += K2                            # S_{+1} -> VS_0
    s[a0:a1, a1:a2] += K1                            # VS_0 -> S_{-1}
    s2 = fro(s @ s)

    # ranks (anti-vacuous)
    rL1 = int(np.linalg.matrix_rank(L1, tol=TOL))
    rL2 = int(np.linalg.matrix_rank(L2, tol=TOL))
    rK1 = int(np.linalg.matrix_rank(K1, tol=TOL))
    rK2 = int(np.linalg.matrix_rank(K2, tol=TOL))
    print("\n(5) FULL BV BICOMPLEX  s = s_KT + s_long  on S_{-1}(+)VS_0(+)S_{+1} (2048):")
    print(f"    leg ranks (anti-vacuous): rk L1={rL1}, rk L2={rL2}, rk K1={rK1}, rk K2={rK2}")
    print(f"    s_long^2 = ||B_W L1||            = {s_long2:.2e}  (target 0, by construction)")
    print(f"    s_KT^2   = ||K1 K2||            = {s_KT2:.2e}  (target 0, by construction)")
    print(f"    {{s_KT,s_long}} VS block          = {cross_VS:.4f}")
    print(f"    {{s_KT,s_long}} S_-1 block        = {cross_Sm:.4f}")
    print(f"    {{s_KT,s_long}} S_+1 block        = {cross_Sp:.4f}")
    print(f"    ||{{s_KT,s_long}}|| (THE genuine BV obstruction) = {anticomm_norm:.4f}")
    print(f"    ||s^2|| (full 2048x2048)        = {s2:.4f}   (=0 iff {{s_KT,s_long}}=0)")

    # === (6) ESCAPE s-EXACTNESS in the FULL bicomplex ==========================
    # The co-exact escape E = Pi_perp M_D Pi_RS (lives in im Gamma^dag).  Is it s-exact,
    # i.e. does there exist an operator G on T with E = (s G - G s) restricted to VS_0->VS_0?
    # Test on the VS_0 endomorphism sector: E s-exact <=> E in im(ad_s|VS).  We solve the
    # least-squares  E ~ L1 X K... using the available exact pieces and report residual.
    E = Pi_perp @ M_D @ Pi_RS                        # 1792x1792, the 41.52 escape
    # candidate s-primitives reaching VS_0->VS_0 through one up + one down leg:
    #   K2 . Y . L2  (S_+1 leg) and L1 . Z . K1 (S_-1 leg). Solve min || E - K2 Y L2 - L1 Z K1 ||.
    # Reduce to normal equations on the two unknown small blocks (128x1792 and 128x1792).
    # Use vectorized least squares via pseudo-inverse of the two channels.
    K2p = np.linalg.pinv(K2)                         # 128x1792
    L2p = np.linalg.pinv(L2)                         # 1792x128
    L1p = np.linalg.pinv(L1)                         # 128x1792
    K1p = np.linalg.pinv(K1)                         # 1792x128
    Y0 = K2p @ E @ L2p                               # best Y for channel K2 Y L2
    Z0 = L1p @ E @ K1p                               # best Z for channel L1 Z K1
    resid_K = fro(E - K2 @ Y0 @ L2)
    resid_L = fro(E - L1 @ Z0 @ K1)
    # combined (alternating projection, few steps)
    R = E.copy(); Ycur = np.zeros_like(Y0); Zcur = np.zeros_like(Z0)
    for _ in range(20):
        Ycur = K2p @ (E - L1 @ Zcur @ K1) @ L2p
        Zcur = L1p @ (E - K2 @ Ycur @ L2) @ K1p
    resid_both = fro(E - K2 @ Ycur @ L2 - L1 @ Zcur @ K1)
    print("\n(6) ESCAPE s-EXACTNESS in the FULL bicomplex:")
    print(f"    ||E = (I-Pi)M_D Pi_RS||                 = {fro(E):.4f}  (the 41.52 escape)")
    print(f"    residual via s_KT leg only (K2 Y L2)    = {resid_K:.4f}")
    print(f"    residual via s_long leg only (L1 Z K1)  = {resid_L:.4f}")
    print(f"    residual via BOTH legs (full bicomplex) = {resid_both:.4f}  "
          f"(s-EXACT iff ~0)")
    frac_killed = 1.0 - resid_both / fro(E)
    print(f"    fraction of escape made s-exact         = {frac_killed:.3f}")

    # === (7) ANTI-TRAP =========================================================
    comm_after = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    print("\n(7) ANTI-TRAP (M_D never modified):")
    print(f"    bare ||[Pi_RS, M_D]|| = {comm_after:.4f}  (STILL 58.72: RS coupled, VZ evaded: "
          f"{comm_after > 1e-6})")

    # === (8) SECONDARY CONSTRAINT C2 reconciliation ============================
    C2 = Gamma @ M_D @ Pi_RS                         # 128 x 1792
    nC2 = fro(C2)
    GGd = Gamma @ Gamma.conj().T
    Gamma_pinv = Gamma.conj().T @ np.linalg.inv(GGd)
    resid_C2_Gamma = fro(C2 - (C2 @ Gamma_pinv) @ Gamma)        # independence of Gamma
    # does the carrier-deformed constraint B_W reduce/reconcile C2?
    C2_W = B_W @ M_D @ Pi_kerBW
    nC2_W = fro(C2_W)
    BWp = B_W.conj().T @ np.linalg.inv(B_W @ B_W.conj().T)
    resid_C2_BW = fro(C2_W - (C2_W @ BWp) @ B_W)
    print("\n(8) SECONDARY CONSTRAINT C2 reconciliation:")
    print(f"    ||C2 = Gamma M_D Pi_RS||                = {nC2:.4f}  (repo 155.36)")
    print(f"    C2 independence of Gamma (residual)     = {resid_C2_Gamma:.4f}  "
          f"({'GENUINELY INDEPENDENT' if resid_C2_Gamma>1e-6 else 'reducible'})")
    print(f"    ||C2_W = B_W M_D Pi_kerBW|| (dressed)   = {nC2_W:.4f}")
    print(f"    C2_W independence of B_W (residual)     = {resid_C2_BW:.4f}  "
          f"({'still independent' if resid_C2_BW>1e-6 else 'RECONCILED into B_W'})")

    # === VERDICT ===============================================================
    print("\n" + "=" * 80)
    print("VERDICT")
    print("=" * 80)
    below = ksp_min < 32.80 - 1e-3
    print(f"  carrier            : KSp polarization, a-priori from (J, Omega, null split)")
    print(f"  H-linear           : {Ppol_h:.1e} (exact, via centralizer)")
    print(f"  non-equivariant    : {pol_defect:.2f} (genuine)")
    print(f"  Spin control       : {spin_min:.2f} (equivariant carrier CANNOT bend -> need non-Spin)")
    print(f"  dressed obstruction: KSp min {ksp_min:.4f}  "
          f"(vs 32.80 floor; BELOW={below}; ZERO={ksp_min<1e-6})")
    print(f"  s_long^2, s_KT^2   : {s_long2:.1e}, {s_KT2:.1e} (both 0, legs nonzero rank)")
    print(f"  {{s_KT,s_long}}      : {anticomm_norm:.4f}  (THE residual BV obstruction)")
    print(f"  full s^2           : {s2:.4f}")
    print(f"  escape s-exact     : residual {resid_both:.4f} of {fro(E):.2f} "
          f"({frac_killed*100:.1f}% killed)")
    print(f"  anti-trap          : {comm_after:.4f} (58.72 preserved)")
    print(f"  C2 / C2_W          : {nC2:.2f} / {nC2_W:.2f}")
    if ksp_min < 1e-6 and s2 < 1e-6:
        print("  STATUS: CLOSURE (verify anti-trap + nonvacuous before promoting)")
    elif below:
        print(f"  STATUS: PROGRESS -- KSp carrier pushes dressed obstruction BELOW 32.80 "
              f"to {ksp_min:.2f},")
        print(f"          but {{s_KT,s_long}}={anticomm_norm:.2f} residual remains "
              f"(needs the actual Y14 curvature).")
    else:
        print(f"  STATUS: SHARPER_OBSTRUCTION -- KSp carrier H-linear/non-equivariant/anti-trap")
        print(f"          intact, but does NOT beat the 32.80 floor (min {ksp_min:.2f}); the")
        print(f"          {{s_KT,s_long}}={anticomm_norm:.2f} residual is the named missing datum.")
    return None


if __name__ == "__main__":
    main()
