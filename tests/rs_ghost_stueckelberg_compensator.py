#!/usr/bin/env python3
"""FRONTIER MOVE (2026-06-27): the first NON-EQUIVARIANT compensator sigma_c for GU's RS sector.

Approach: STUECKELBERG COMPENSATOR on the verified Cl(9,5)=M(64,H)~M(128,C) rep
(VS = R^14 (x) S = C^1792).  Reuses the objects of
explorations/rs_source_candidate_projected_differential_scratch.py and
tests/oq_rk1_cl95_explicit_rep.py (Gamma, Pi_RS, M_D, J, gauge image).

We BUILD a genuine non-equivariant, H-linear sigma_c, assemble a graded BRST/Stueckelberg
differential s on C^{-1} -> C^0 -> C^1, and COMPUTE every mandated predicate with REAL
numbers from the explicit rep:

  (0) keystone anchors reproduced (||[Pi_RS,M_D]||, operator escape, gauge escape).
  (1) ||s^2|| on the minimal leg (target 0).
  (2) is the off-surface escape (I-Pi_RS) M_D Pi_RS  s-EXACT?  (vs the disqualified
      bare-subtraction decoupling trap).
  (3) ANTI-TRAP: bare ||[Pi_RS,M_D]|| STILL 58.72 != 0 (RS stays coupled => VZ stays evaded);
      AND effective ||[Pi_RS,M_eff]|| also != 0 (no decoupling introduced).
  (4) equivariance defect of sigma_c against Stab_eta(xi) (must be != 0 = genuinely
      non-equivariant) vs the defects of M_D, Pi_RS (must be ~0 = covariant).
  (5) ||[sigma_c, J]|| (H-linearity, target 0).

sigma_c construction (STUECKELBERG, fixed-frame background datum):
  L      = (xi xi^T)/(xi . xi)_delta   longitudinal projector on R^14 built with the
           EUCLIDEAN inner product delta_ab (NOT the indefinite Cl(9,5) metric eta_{9,5}).
  L_VS   = L (x) I_128
  sigma_c = - L_VS . M_D . Pi_RS        (added to bare M_D:  M_eff = M_D + sigma_c)

The Euclidean frame is the non-equivariant datum: a choice of time-space split that breaks
Spin(9,5).  The covariant alternative L_eta = (xi (eta xi)^T)/<xi,xi>_eta sits inside the
equivariant family SHIAB-04 already killed (and <xi,xi>_eta can vanish for null xi).

NOTHING is tuned. xi is the repo's fixed sample covector. Numbers reported as-is.
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import oq_rk1_cl95_explicit_rep as cl95  # verified Cl(9,5) rep

TOL = 1e-9
N = 14
DIM = 128
VSDIM = N * DIM  # 1792
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)


def fro(A):
    return float(np.linalg.norm(A))


def proj_onto_kernel(M):
    gram = M @ M.conj().T
    return np.eye(M.shape[1], dtype=complex) - M.conj().T @ np.linalg.inv(gram) @ M


def build_rep():
    G = cl95.jordan_wigner_gammas(7)
    eta = np.array([+1.0] * 9 + [-1.0] * 5)
    e = [G[a] if eta[a] > 0 else 1j * G[a] for a in range(N)]
    Iden = np.eye(DIM, dtype=complex)
    return eta, e, Iden


def build_J(e):
    """Quaternionic structure J = U.conj on S, J^2=-I, [J,e_a]=0."""
    s = np.empty(N)
    for a in range(N):
        s[a] = (-1.0) ** a if a < 9 else (-1.0) ** (a + 1)
    anticomm = [a for a in range(N) if s[a] < 0]
    U = np.eye(DIM, dtype=complex)
    for a in anticomm:
        U = U @ e[a]
    Jsq = fro(U @ np.conjugate(U) + np.eye(DIM))
    comm = max(fro(U @ np.conjugate(e[a]) - e[a] @ U) for a in range(N))
    return U, Jsq, comm


# ---- efficient kron(.,I) / kron(I,.) actions on VS operators (avoid 1792 kron) -----
def L_vec(rho, O):
    """kron(rho, I_128) @ O  ;  rho is 14x14, O is 1792x1792."""
    return np.einsum('ab,bsJ->asJ', rho, O.reshape(N, DIM, VSDIM)).reshape(VSDIM, VSDIM)


def R_vec(rho, O):
    """O @ kron(rho, I_128)."""
    return np.einsum('Ibs,ba->Ias', O.reshape(VSDIM, N, DIM), rho).reshape(VSDIM, VSDIM)


def L_spin(S, O):
    """kron(I_14, S) @ O ; S is 128x128."""
    return np.einsum('st,atJ->asJ', S, O.reshape(N, DIM, VSDIM)).reshape(VSDIM, VSDIM)


def R_spin(S, O):
    """O @ kron(I_14, S)."""
    return np.einsum('Iat,ts->Ias', O.reshape(VSDIM, N, DIM), S).reshape(VSDIM, VSDIM)


def main():
    eta, e, Iden = build_rep()
    eta_mat = np.diag(eta).astype(complex)

    # ---- core operators -----------------------------------------------------------
    Gamma = np.hstack(e)                                  # 128 x 1792
    Pi_RS = proj_onto_kernel(Gamma)                       # 1792 x 1792
    Pi_perp = np.eye(VSDIM, dtype=complex) - Pi_RS
    cxi = sum(XI[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)          # twisted Dirac symbol
    gauge = np.vstack([XI[a] * Iden for a in range(N)])   # 1792 x 128  pure-gauge image

    print("=" * 84)
    print("STUECKELBERG NON-EQUIVARIANT COMPENSATOR sigma_c  (Cl(9,5)=M(64,H), VS=C^1792)")
    print("=" * 84)

    # === (0) reproduce keystone anchors ===========================================
    comm_PiMD = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    escape = Pi_perp @ M_D @ Pi_RS                        # operator-level off-surface escape
    op_escape = fro(escape)
    gauge_escape = fro(Pi_perp @ M_D @ Pi_RS @ gauge)
    print("\n[0] KEYSTONE ANCHORS (must match repo):")
    print(f"    ||[Pi_RS, M_D]||                 = {comm_PiMD:.4f}   (repo 58.7215)")
    print(f"    ||(I-Pi_RS) M_D Pi_RS|| operator = {op_escape:.4f}   (repo 41.5224)")
    print(f"    ||(I-Pi_RS) M_D Pi_RS (gauge)||  = {gauge_escape:.4f}   (repo 169.1942)")

    # === build sigma_c (Stueckelberg, Euclidean longitudinal projector) ===========
    nrm2_delta = float(np.real(XI @ XI))                  # euclidean <xi,xi>_delta
    L = np.outer(XI, XI) / nrm2_delta                     # 14x14, L^2=L, rank 1
    L_VS_M_Pi = L_vec(L, M_D @ Pi_RS)                     # L_VS @ M_D @ Pi_RS
    sigma_c = -L_VS_M_Pi
    M_eff = M_D + sigma_c

    # covariant alternative L_eta (sits in the equivariant family already killed)
    nrm2_eta = complex(XI @ eta_mat @ XI)
    L_eta = np.outer(XI, eta_mat @ XI) / nrm2_eta
    print("\n[sigma_c] STUECKELBERG COMPENSATOR  sigma_c = -(L (x) I) M_D Pi_RS")
    print(f"    L idempotent err={fro(L@L-L):.1e}, rank(L)={int(np.linalg.matrix_rank(L,tol=TOL))}")
    print(f"    <xi,xi>_delta = {nrm2_delta:.4f}   <xi,xi>_eta = {nrm2_eta.real:.4f}")
    print(f"    ||L_euclid - L_eta|| = {fro(L-L_eta):.4f}   (frame datum is genuinely extra)")
    print(f"    ||sigma_c|| = {fro(sigma_c):.4f}")

    # === (1) graded BRST/Stueckelberg complex  C^{-1} -A-> C^0 -Gamma-> C^1 ========
    #   V_{-1}=S(128) ghost eps ; V_0=VS(1792) RS field ; V_1=S(128) antighost.
    #   s.eps = A eps ,  A = Pi_RS @ gauge (the Stueckelberg embedding, into ker Gamma)
    #   s.Psi = Gamma Psi .   s^2 on the leg  <=>  Gamma A = 0.
    A = Pi_RS @ gauge                                     # 1792 x 128
    s2_leg = fro(Gamma @ A)                               # ||s^2|| on -1->0->1
    print("\n[1] NILPOTENCY  ||s^2|| on minimal leg  C^-1 -A-> C^0 -Gamma-> C^1:")
    print(f"    A = Pi_RS gauge,  ||Gamma A|| = {s2_leg:.2e}   (target 0)")

    # === (2) is the escape s-EXACT? ===============================================
    #  coboundaries from C^{-1} live in im(A) subset ker(Gamma) = im(Pi_RS).
    #  the escape lives in im(Pi_perp) = ker(Gamma)^perp.  These are ORTHOGONAL,
    #  so NO Stueckelberg embedding can make the escape s-exact in the minimal complex.
    overlap = fro(Pi_RS @ escape) / op_escape
    print("\n[2] s-EXACTNESS of the escape (I-Pi_RS) M_D Pi_RS:")
    print(f"    ||Pi_RS . escape|| / ||escape|| = {overlap:.2e}")
    print(f"    -> escape is orthogonal to ALL minimal-complex coboundaries (im Pi_RS):")
    print(f"       NOT s-exact in the minimal Stueckelberg complex.")
    #  BV / antifield-doubled: Pi_perp = Gamma^dag (Gamma Gamma^dag)^-1 Gamma identically,
    #  so the antighost direction 'factors' the escape -- but this is TAUTOLOGICAL.
    GG = Gamma @ Gamma.conj().T
    Pi_perp_id = Gamma.conj().T @ np.linalg.inv(GG) @ Gamma
    taut = fro(Pi_perp - Pi_perp_id)
    bv_factor = fro(escape - Pi_perp_id @ M_eff @ Pi_RS)
    print(f"    [BV antifield] ||Pi_perp - Gamma^dag(GG^dag)^-1 Gamma|| = {taut:.2e} (identity)")
    print(f"       => antighost 'exactness' ||escape - Gamma^dag(..)Gamma M_eff Pi_RS|| = "
          f"{bv_factor:.2e}  (structurally forced, NOT content)")
    #  the REAL test: closing the nilpotent BV differential WITH the dynamics
    #  (master-equation / antibracket round-trip).
    master = fro(Pi_RS @ M_eff @ Pi_perp @ M_eff @ Pi_RS)
    master_bare = fro(Pi_RS @ M_D @ Pi_perp @ M_D @ Pi_RS)
    print(f"    [MASTER EQ] ||Pi_RS M_eff Pi_perp M_eff Pi_RS|| = {master:.4f}  != 0")
    print(f"                ||Pi_RS M_D   Pi_perp M_D   Pi_RS|| = {master_bare:.4f}  (bare)")
    print(f"       => this residual is the SHARPENED OBSTRUCTION: the BV antibracket / "
          f"odd-symplectic\n          pairing the SOURCE ACTION must supply.")

    # escape split: how much of the escape does sigma_c (longitudinal) absorb?
    L_escape = fro(L_vec(L, escape))
    T_escape = fro(L_vec(np.eye(N, dtype=complex) - L, escape))
    resid_escape = fro(Pi_perp @ M_eff @ Pi_RS)
    print("\n    escape split (longitudinal absorbed vs transverse surviving):")
    print(f"    ||L . escape|| (absorbed)  = {L_escape:.4f}")
    print(f"    ||T . escape|| (survives)  = {T_escape:.4f}")
    print(f"    ||(I-Pi_RS) M_eff Pi_RS||  = {resid_escape:.4f}   (residual escape after sigma_c)")

    # === (3) ANTI-TRAP: RS must stay coupled (no decoupling) =======================
    comm_PiMeff = fro(Pi_RS @ M_eff - M_eff @ Pi_RS)
    print("\n[3] ANTI-TRAP (RS must NOT decouple => VZ stays evaded):")
    print(f"    bare      ||[Pi_RS, M_D]||   = {comm_PiMD:.4f}   (STILL 58.72 != 0  -> coupled)")
    print(f"    effective ||[Pi_RS, M_eff]|| = {comm_PiMeff:.4f}   (!= 0 -> still coupled)")
    decoupling_trap = (comm_PiMeff < 1e-6)
    print(f"    decoupling trap triggered? {decoupling_trap}  (False = anti-trap PASSED)")

    # === (4) equivariance defect against Stab_eta(xi) =============================
    # Spin(9,5) bivector gens Sigma_ab=(1/2)e_a e_b; vector action rho_C = C @ eta for
    # antisymmetric C.  Stab_eta(xi): C antisym with C y = 0, y = eta xi.
    # Full gen on VS:  G_C = kron(C eta, I) + kron(I, Sigma_C),  Sigma_C=(1/4)sum C_ab e_a e_b.
    y = eta_mat @ XI                                      # eta-lowered covector (real)
    yv = np.real(y)
    # orthonormal basis of euclidean complement of y in R^14
    Q, _ = np.linalg.qr(np.column_stack([yv, np.eye(N)]))
    fperp = Q[:, 1:N]                                     # 14 x 13, all perp to y
    gens = []
    for i in range(fperp.shape[1]):
        for j in range(i + 1, fperp.shape[1]):
            C = np.outer(fperp[:, i], fperp[:, j]) - np.outer(fperp[:, j], fperp[:, i])
            gens.append(C.astype(complex))               # 78 antisym gens, C y = 0

    eaeb = np.stack([np.stack([e[a] @ e[b] for b in range(N)]) for a in range(N)])  # 14x14x128x128

    def Sigma_of(C):
        return 0.25 * np.einsum('ab,abst->st', C, eaeb)

    def defect(O):
        tot = 0.0
        for C in gens:
            rho = C @ eta_mat                             # vector action
            S = Sigma_of(C)
            GO = L_vec(rho, O) + L_spin(S, O)
            OG = R_vec(rho, O) + R_spin(S, O)
            tot += fro(GO - OG) ** 2
        return float(np.sqrt(tot))

    # sanity: a generator C y = 0 ?
    maxCy = max(fro(C @ yv) for C in gens)
    def_MD = defect(M_D)
    def_Pi = defect(Pi_RS)
    def_sig = defect(sigma_c)
    print("\n[4] EQUIVARIANCE DEFECT vs Stab_eta(xi)  (78 gens, aggregate Frobenius):")
    print(f"    stabilizer check  max||C y|| = {maxCy:.1e}  (gens fix xi)")
    print(f"    defect(M_D)     = {def_MD:.3e}   (covariant ~ 0)")
    print(f"    defect(Pi_RS)   = {def_Pi:.3e}   (covariant ~ 0)")
    print(f"    defect(sigma_c) = {def_sig:.4f}   (NON-equivariant: {def_sig > 1.0})")

    # === (5) H-linearity  [sigma_c, J] ===========================================
    U, Jsq, Jcomm = build_J(e)
    JVS = np.kron(np.eye(N, dtype=complex), U)
    Hlin = fro(sigma_c @ JVS - JVS @ np.conjugate(sigma_c))
    print("\n[5] H-LINEARITY  (J = I_14 (x) U,  antilinear):")
    print(f"    ||J^2+I||={Jsq:.1e}, ||[J,Cl]||={Jcomm:.1e}")
    print(f"    ||sigma_c J - J conj(sigma_c)|| = {Hlin:.2e}   (H-linear: {Hlin < 1e-6})")

    # === verdict ==================================================================
    print("\n" + "=" * 84)
    print("VERDICT")
    print("=" * 84)
    print(f"  sigma_c is genuinely NON-EQUIVARIANT (defect {def_sig:.1f}), H-LINEAR ({Hlin:.1e}),")
    print(f"  and ANTI-TRAP holds (bare [Pi_RS,M_D]={comm_PiMD:.2f}, eff [Pi_RS,M_eff]="
          f"{comm_PiMeff:.2f}; RS stays coupled).")
    print(f"  It absorbs the longitudinal escape ({L_escape:.2f} of {op_escape:.2f}) but the escape")
    print(f"  is NOT s-exact in the minimal complex (orthogonal, {overlap:.1e}); closing the")
    print(f"  nilpotent BV differential leaves master-eq residual {master:.2f} != 0.")
    print(f"  STATUS: SHARPER_OBSTRUCTION -- the missing datum is the BV antibracket / odd-")
    print(f"  symplectic pairing on the RS complex, exactly what the source action supplies.")

    return {
        "comm_PiMD": comm_PiMD, "op_escape": op_escape, "gauge_escape": gauge_escape,
        "s2_leg": s2_leg, "overlap": overlap, "bv_factor": bv_factor, "master": master,
        "L_escape": L_escape, "T_escape": T_escape, "resid_escape": resid_escape,
        "comm_PiMeff": comm_PiMeff, "def_MD": def_MD, "def_Pi": def_Pi, "def_sig": def_sig,
        "Hlin": Hlin, "L_minus_Leta": fro(L - L_eta), "sigma_norm": fro(sigma_c),
    }


if __name__ == "__main__":
    main()
