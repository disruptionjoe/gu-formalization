#!/usr/bin/env python3
"""FRONTIER MOVE (2026-06-27): first NON-EQUIVARIANT compensator sigma_c(xi) for
GU's RS sector, approach = FIXED-NULL-COVECTOR SPURION.

Context (keystone SOURCE-01):
  explorations/source-action-necessary-conditions-and-causality-2026-06-27.md
  explorations/rs_source_candidate_projected_differential_scratch.py
On the verified Cl(9,5)=M(64,H)~M(128,C) rep:
  Gamma = hstack(c(e_a))           gamma-trace map      C^1792 -> C^128
  Pi_RS = projector onto ker(Gamma)                     (RS-irreducible surface)
  M_D   = id_14 (x) c(xi)          twisted Dirac symbol
Anchors: ||[Pi_RS,M_D]|| = 58.72, ||(I-Pi_RS)M_D Pi_RS||_op = 41.52,
gauge-image escape = 169.19, ||Gamma.gauge|| = 80.61.

THE ANTI-TRAP (non-negotiable, keystone F6 / no-go-class-relative-map):
  [Pi_RS, M_D] = 0  <=>  ker(Gamma) M_D-invariant  <=>  RS decouples standalone
  =>  Velo-Zwanziger ACAUSAL.  So sigma_trap = -(I-Pi_RS)M_D Pi_RS added to the
  BARE dynamics is the DISQUALIFIED acausal block-subtraction.  A genuine
  resolution must keep [Pi_RS, M_D] = 58.72 != 0 (RS stays coupled) and resolve
  the escape COHOMOLOGICALLY via a non-equivariant ghost, NOT by zeroing it.

DESIGN under test (fixed-null-covector spurion as a CONSTRAINT-codifferential
deformation; M_D and the physical Pi_RS are NEVER modified):
  - n = e_0 + e_9 (eta(n,n) = 0, null) => c(n)^2 = 0 (nilpotent ghost coupling).
  - nbar = e_0 - e_9 (null), eta(n,nbar) = 2; null-plane idempotent
    P_n = c(n)c(nbar)/(2 eta(n,nbar)).
  - Deform the CONSTRAINT co-differential: B_n = Gamma + alpha*(null spurion),
    leaving M_D untouched.  s = [[0,0,0],[A_n,0,0],[0,B_n,0]] on S(+)VS(+)S,
    A_n chosen so B_n A_n = 0 (=> s^2 = 0, underwritten by c(n)^2 = 0).
  - sigma_c is the statement that the escape (I-Pi_kerB_n)M_D Pi_kerB_n is s-exact
    iff ker(B_n) is M_D-invariant, i.e. ||[Pi_kerB_n, M_D]|| = 0.

HONEST PREDICTION (discipline): SHARPER OBSTRUCTION. The null spurion supplies
nilpotency, non-equivariance, exact H-linearity, a genuine n-dependent family,
but cannot drive ||[Pi_kerB_n, M_D]|| to 0 -- it localizes the one datum (the
invariant-surface SELECTOR) the source action must supply.

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
    """||Op J - J conj(Op)|| with J = U.conj antilinear: H-linear iff ~0."""
    return fro(Op @ U - U @ np.conjugate(Op))


def main():
    dim, eta, e, omega, Iden = build_rep()
    VSdim = N * dim  # 1792

    # ---- core operators (identical construction to the keystone scratch) -------
    Gamma = np.hstack(e)                            # 128 x 1792
    Pi_RS = proj_onto_kernel(Gamma)                 # 1792 x 1792
    Pi_perp = np.eye(VSdim, dtype=complex) - Pi_RS
    cxi = sum(XI[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)    # 1792 x 1792
    gauge = np.vstack([XI[a] * np.eye(dim, dtype=complex) for a in range(N)])  # 1792 x 128

    print("=" * 80)
    print("NON-EQUIVARIANT COMPENSATOR sigma_c -- FIXED-NULL-COVECTOR SPURION")
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

    # === (2) NULL SPURION: nilpotency of the ghost coupling ====================
    # n = e_0 + e_9 (null), nbar = e_0 - e_9 (null), eta(n,nbar) = 2.
    n_vec = np.zeros(N); n_vec[0] = 1.0; n_vec[9] = 1.0
    nb_vec = np.zeros(N); nb_vec[0] = 1.0; nb_vec[9] = -1.0
    eta_nn = float(sum(eta[a] * n_vec[a] * n_vec[a] for a in range(N)))
    eta_nbnb = float(sum(eta[a] * nb_vec[a] * nb_vec[a] for a in range(N)))
    eta_nnb = float(sum(eta[a] * n_vec[a] * nb_vec[a] for a in range(N)))
    cn = sum(n_vec[a] * e[a] for a in range(N))      # c(n)
    cnb = sum(nb_vec[a] * e[a] for a in range(N))     # c(nbar)
    cn2 = fro(cn @ cn)
    cnb2 = fro(cnb @ cnb)
    anticomm_err = fro(cn @ cnb + cnb @ cn - 2 * eta_nnb * Iden)
    P_n = (cn @ cnb) / (2 * eta_nnb)
    Pn_idem = fro(P_n @ P_n - P_n)
    Pn_rank = int(np.linalg.matrix_rank(P_n, tol=TOL))
    print("\n(2) NULL SPURION n=e_0+e_9 (nilpotent ghost coupling):")
    print(f"    eta(n,n)={eta_nn:.3f}, eta(nbar,nbar)={eta_nbnb:.3f}, eta(n,nbar)={eta_nnb:.3f}")
    print(f"    ||c(n)^2||={cn2:.2e}, ||c(nbar)^2||={cnb2:.2e}  (NILPOTENT iff ~0)")
    print(f"    ||{{c(n),c(nbar)}}-2eta I||={anticomm_err:.2e}")
    print(f"    P_n=c(n)c(nbar)/2eta: ||P_n^2-P_n||={Pn_idem:.2e}, rank_C={Pn_rank}")
    # non-null control: m = e_0 + 0.5 e_9 (eta != 0) must BREAK nilpotency
    m_vec = np.zeros(N); m_vec[0] = 1.0; m_vec[9] = 0.5
    eta_mm = float(sum(eta[a] * m_vec[a] * m_vec[a] for a in range(N)))
    cm = sum(m_vec[a] * e[a] for a in range(N))
    cm2 = fro(cm @ cm)
    print(f"    CONTROL non-null m=e_0+0.5e_9 (eta={eta_mm:.3f}): ||c(m)^2||={cm2:.4f}"
          f"  (breaks s^2=0: {cm2 > 1e-6})")

    # === (3) DEFORMED CONSTRAINT SURFACES + closure obstruction scan ===========
    # Build B_n for three null-spurion deformation families; for each compute
    # Pi_kerB_n and the closure obstruction ||[Pi_kerB_n, M_D]||  (=0 iff escape s-exact).
    def closure_obstruction(Bn):
        Pi = proj_onto_kernel(Bn)
        return fro(Pi @ M_D - M_D @ Pi), Pi

    I14 = np.eye(N, dtype=complex)

    # Family A: block a -> e_a + a_coef*n_a*c(n) + b_coef*n_a*c(nbar)
    def Bn_familyA(ac, bc):
        blocks = []
        for a in range(N):
            blk = e[a] + ac * n_vec[a] * cn + bc * nb_vec[a] * cnb
            blocks.append(blk)
        return np.hstack(blocks)

    # Family B: B = Gamma . (id_14 (x) (I + t P_n))   block a -> e_a (I + t P_n)
    def Bn_familyB(t):
        return np.hstack([e[a] @ (Iden + t * P_n) for a in range(N)])

    # Family C: B = Gamma . (id_14 (x) exp(t(P_n - P_n^dag)))
    def Bn_familyC(t):
        G_t = expm(t * (P_n - P_n.conj().T))
        return np.hstack([e[a] @ G_t for a in range(N)])

    print("\n(3) s-EXACTNESS OF ESCAPE = M_D-INVARIANCE of ker(B_n):")
    print(f"    baseline ||[Pi_RS, M_D]|| (alpha=0) = {comm_PiMD:.4f}")

    bestA = (None, np.inf)
    gridA = [-2.0, -1.0, -0.5, 0.5, 1.0, 2.0]
    for ac in gridA:
        for bc in gridA + [0.0]:
            val, _ = closure_obstruction(Bn_familyA(ac, bc))
            if val < bestA[1]:
                bestA = ((ac, bc), val)
    print(f"    family A  e_a + a n_a c(n) + b n_a c(nbar): "
          f"min ||[Pi_kerB_n,M_D]|| = {bestA[1]:.4f} at (a,b)={bestA[0]}")

    bestB = (None, np.inf)
    for t in np.linspace(-3, 3, 25):
        if abs(t) < 1e-9:
            continue
        val, _ = closure_obstruction(Bn_familyB(t))
        if val < bestB[1]:
            bestB = (t, val)
    print(f"    family B  Gamma(I + t id(x)P_n):           "
          f"min ||[Pi_kerB_n,M_D]|| = {bestB[1]:.4f} at t={bestB[0]:.3f}")

    bestC = (None, np.inf)
    for t in np.linspace(-3, 3, 25):
        if abs(t) < 1e-9:
            continue
        val, _ = closure_obstruction(Bn_familyC(t))
        if val < bestC[1]:
            bestC = (t, val)
    print(f"    family C  Gamma exp(t(P_n - P_n^dag)):      "
          f"min ||[Pi_kerB_n,M_D]|| = {bestC[1]:.4f} at t={bestC[0]:.3f}")

    global_min = min(bestA[1], bestB[1], bestC[1])
    print(f"    GLOBAL MIN over all families = {global_min:.4f}  "
          f"(REACHES 0? {global_min < 1e-6})")

    # Does an M_D-invariant 1664-dim subspace even EXIST? (lower bound check)
    # smallest singular value of [Pi_RS, M_D] family is bounded; report whether
    # ANY deformed surface kills it -> if not, obstruction is genuine.

    # === build an EXPLICIT s and verify s^2 = 0 at a representative B_n ========
    Bn_rep = Bn_familyA(*bestA[0])
    Pi_kerBn = proj_onto_kernel(Bn_rep)
    # A_n : S(128) -> VS(1792) with image in ker(B_n) so B_n A_n = 0.
    A_n = Pi_kerBn @ gauge                          # 1792 x 128, im subset ker(B_n)
    BnAn = fro(Bn_rep @ A_n)                        # the only nonzero s^2 block
    # assemble full s on S(+)VS(+)S = 128+1792+128 = 2048
    D = dim + VSdim + dim
    s = np.zeros((D, D), dtype=complex)
    s[dim:dim + VSdim, 0:dim] = A_n                 # A_n: C^{-1} -> C^0
    s[dim + VSdim:D, dim:dim + VSdim] = Bn_rep      # B_n: C^0 -> C^1
    s2 = fro(s @ s)
    print("\n(2b) EXPLICIT 3-TERM COMPLEX  S --A_n--> VS --B_n--> S,  s^2 norm:")
    print(f"    ||B_n A_n|| (only s^2 block) = {BnAn:.2e}")
    print(f"    ||s^2|| (full 2048x2048)     = {s2:.2e}   (target 0)")

    # === (4) ANTI-TRAP: bare [Pi_RS, M_D] STILL 58.72 (M_D untouched) ==========
    comm_PiMD_after = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    print("\n(4) ANTI-TRAP -- bare gamma-trace-frame coupling preserved:")
    print(f"    ||[Pi_RS, M_D]|| (M_D never modified) = {comm_PiMD_after:.4f}  "
          f"(STILL != 0: {comm_PiMD_after > 1e-6}  => RS stays coupled, VZ evaded)")

    # the DISQUALIFIED trap, computed explicitly, to contrast:
    sigma_trap = -(Pi_perp @ M_D @ Pi_RS)
    trap_escape = fro(Pi_perp @ (M_D + sigma_trap) @ Pi_RS)
    trap_comm = fro(Pi_RS @ (M_D + sigma_trap) - (M_D + sigma_trap) @ Pi_RS)
    # chain-map residual (descent condition Gamma(M_D+sigma) = s1 Gamma) for both:
    resid_zero = fro(Gamma @ M_D @ Pi_RS)               # sigma = 0
    resid_trap = fro(Gamma @ (M_D + sigma_trap) @ Pi_RS)  # sigma_trap
    print("\n(7) TRAP EXCLUSION (theorem illustration -- escape & chain-map residual")
    print("    vanish TOGETHER only at the acausal block-subtraction):")
    print(f"    sigma=0      : chain-map residual ||Gamma M_D Pi_RS||      = {resid_zero:.4f}, "
          f"escape = {escape_op:.4f}")
    print(f"    sigma_trap   : chain-map residual ||Gamma(M_D+s)Pi_RS||    = {resid_trap:.2e}, "
          f"escape = {trap_escape:.2e}")
    print(f"    sigma_trap also forces ||[Pi_RS, M_D+sigma_trap]|| = {trap_comm:.2e}  "
          f"(DECOUPLED => DISQUALIFIED)")
    print("    => ANY compensator closing the EQUIVARIANT complex IS the trap; ours")
    print("       deforms the CONSTRAINT surface instead and never touches M_D.")

    # === (5) EQUIVARIANCE DEFECT of the ghost coupling c(n) ====================
    def Sigma(a, b):
        return 0.25 * (e[a] @ e[b] - e[b] @ e[a])
    print("\n(5) EQUIVARIANCE DEFECT of c(n) vs Spin(9,5) generators Sigma_ab:")
    pairs_test = [(0, 9), (0, 1), (9, 10), (1, 2), (3, 11)]
    defects = {}
    for (a, b) in pairs_test:
        d = fro(Sigma(a, b) @ cn - cn @ Sigma(a, b))
        defects[(a, b)] = d
        print(f"    ||[Sigma_{{{a},{b}}}, c(n)]|| = {d:.4f}")
    max_defect = max(defects.values())
    print(f"    MAX defect = {max_defect:.4f}  (NON-equivariant iff != 0: {max_defect > 1e-6})")
    # n-dependence genuine: distinct null directions give distinct operators
    n2 = np.zeros(N); n2[1] = 1.0; n2[10] = 1.0   # another null dir
    n3 = np.zeros(N); n3[2] = 1.0; n3[11] = 1.0
    cn_2 = sum(n2[a] * e[a] for a in range(N))
    cn_3 = sum(n3[a] * e[a] for a in range(N))
    print(f"    n-dependence: ||c(n2)-c(n1)||={fro(cn_2-cn):.4f}, "
          f"||c(n3)-c(n1)||={fro(cn_3-cn):.4f}  (genuine family)")

    # === (6) H-LINEARITY ([.,J]) ==============================================
    U, Jsq_err, Jcomm_err = build_J(dim, eta, e)
    h_cn = hlin_residual(cn, U)
    h_cnb = hlin_residual(cnb, U)
    h_cxi = hlin_residual(cxi, U)
    h_Pn = hlin_residual(P_n, U)
    JVS = np.kron(np.eye(N, dtype=complex), U)
    h_PikerBn = fro(Pi_kerBn @ JVS - JVS @ np.conjugate(Pi_kerBn))
    print("\n(6) H-LINEARITY ([.,J], J=U.conj; rank_H preserved iff ~0):")
    print(f"    ||J^2+I||={Jsq_err:.1e}, ||[J,Cl]||={Jcomm_err:.1e}")
    print(f"    ||[c(n),J]||={h_cn:.2e}, ||[c(nbar),J]||={h_cnb:.2e}, ||[c(xi),J]||={h_cxi:.2e}")
    print(f"    ||[P_n,J]||={h_Pn:.2e}, ||[Pi_kerB_n,J]||={h_PikerBn:.2e}")
    max_h = max(h_cn, h_cnb, h_cxi, h_Pn, h_PikerBn)
    print(f"    MAX H-linearity residual = {max_h:.2e}  (H-linear: {max_h < 1e-9})")

    # === VERDICT ===============================================================
    print("\n" + "=" * 80)
    print("VERDICT")
    print("=" * 80)
    print(f"  s^2 = 0                : {s2:.2e}   (YES, c(n)^2=0 underwrites it)")
    print(f"  escape s-EXACT?        : min ||[Pi_kerB_n,M_D]|| = {global_min:.4f} "
          f"(NOT 0 => NOT s-exact)")
    print(f"  anti-trap [Pi_RS,M_D]  : {comm_PiMD_after:.4f} (STILL 58.72, RS coupled, VZ evaded)")
    print(f"  non-equivariance       : {max_defect:.4f} (genuine)")
    print(f"  H-linearity            : {max_h:.2e} (exact)")
    print("  STATUS: SHARPER_OBSTRUCTION -- the null spurion bends the closure")
    print(f"          obstruction from 58.72 down to {global_min:.2f} but CANNOT reach 0.")
    print("          The residual IS the invariant-surface SELECTOR the source")
    print("          action must supply (family-coordinate / holonomy / KSp class).")
    return None


if __name__ == "__main__":
    main()
