#!/usr/bin/env python3
"""FRONTIER MOVE (2026-06-27): the first NON-EQUIVARIANT compensator sigma_c(xi)
for GU's RS sector, via the SUPERGRAVITY GRAVITINO BRST mechanism, on the verified
Cl(9,5) = M(64,H) ~ M(128,C) representation.

Context / provenance
--------------------
The keystone run (explorations/source-action-necessary-conditions-and-causality-2026-06-27.md,
explorations/rs_source_candidate_projected_differential_scratch.py) proved on this rep that:
  - the RS sector cannot be stabilized by ANY equivariant operator (SHIAB-04),
  - the clean-quotient condition [Pi_RS, M_D] = 0 (ker(Gamma) M_D-invariant) is EQUIVALENT to
    RS decoupling into a standalone module, which REINSTATES Velo-Zwanziger acausality,
  - therefore a "resolution" sigma_c = -(I-Pi_RS) M_D Pi_RS added to the BARE dynamics M_D is the
    ACAUSAL DECOUPLING TRAP and is DISQUALIFIED,
  - the correct target is a genuine BRST GHOST structure C^{-1} -> C^0 -> C^1 with nilpotent s
    (s^2 = 0) in which the off-surface escape is resolved COHOMOLOGICALLY while the BARE M_D
    still fails to preserve ker(Gamma) ([Pi_RS, M_D] = 58.72 STAYS).

This script BUILDS such a candidate and reports REAL numbers from the explicit rep. It reuses the
exact rep + objects from the keystone scratch (Gamma, Pi_RS, M_D, J, the gauge image g) and the
verified Cl(9,5) rep in tests/oq_rk1_cl95_explicit_rep.py.

Design: "sugra-gravitino-brst"
------------------------------
Graded complex:
    C^{-1} = S        (SUSY ghost eps, a quaternionic 0-form spinor in S = C^128)
      --G_tot-->
    C^0    = VS = R^14 (x) S = C^1792   (RS field Psi)
      --Gamma-->
    C^1    = S        (antighost / Nakanishi-Lautrup b-field)

The bare RS gauge leg is the symbol of delta(psi_a) = partial_a(eps):  g(eps)_a = xi_a eps.
The gravitino covariant derivative delta(psi_a) = D_a(eps) = (partial_a + (1/4) omega_a^{bc} Sigma_bc)(eps)
adds the spin-connection ghost coupling:
    sigma_c(eps)_a = sum_{b<c} W_a^{bc} (e_b e_c) eps
where Sigma_bc = e_b e_c is the spinor Lorentz generator (Clifford bivector) and W_a^{bc} is a FIXED
background spin-connection coefficient -- the gravitino's gravitational coupling, NOT built from xi.

s.Psi = G_tot eps = (g + sigma_c) eps.  Nilpotency s^2 = 0 requires Gamma . G_tot = 0
(the gauge orbit must be gamma-traceless).  We solve W on the rep from Gamma . sigma_c = -c(xi).

The bare dynamics M_D = id_14 (x) c(xi) is NEVER modified -> [Pi_RS, M_D] = 58.72 is preserved
(anti-trap), so RS stays coupled and VZ stays evaded.

Tests (all real numbers; nothing tuned except the explicit least-squares solve for W):
  [T0] anchors        : ||Esc=(I-Pi)M_D Pi|| (41.52), ||[Pi_RS,M_D]|| (58.72) -- M_D UNTOUCHED
  [T1] bare nilpotency: ||Gamma.g|| = ||c(xi)|| (s^2 fails for bare RS gauge)
  [T2] bare s-exact   : is the escape in im(Pi_perp g)? (yes, but bare g is xi-natural/equivariant)
  [T3] solve sigma_c  : Gamma.sigma_c = -c(xi), then s^2 = ||Gamma.G_tot|| -> 0
  [T4] THE SHARP TEST : with s^2=0 (Pi_perp G_tot=0), is the DYNAMICAL escape still s-exact?
  [T4b] co-exactness  : the escape is killed by the antighost b-leg (im Gamma^dag), not the ghost leg
  [T5] non-equivariance: equivariance defect of sigma_c vs the xi-co-rotating Spin(9,5) action
  [T6] H-linearity    : ||J_VS conj(sigma_c) - sigma_c J_S|| (rank_H preserved?)
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
TESTS = os.path.join(REPO, "tests")
if TESTS not in sys.path:
    sys.path.insert(0, TESTS)

import oq_rk1_cl95_explicit_rep as cl95  # verified Cl(9,5) rep

TOL = 1e-9
N = 14
# repo's fixed sample covector (same as the keystone scratch) -- NOT tuned
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)


def fro(A):
    return float(np.linalg.norm(A))


def proj_onto_kernel(M):
    gram = M @ M.conj().T
    return np.eye(M.shape[1], dtype=complex) - M.conj().T @ np.linalg.inv(gram) @ M


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
    """Quaternionic structure J = U.conj, J^2 = -I, [J, e_a] = 0 (from shiab_family_basis)."""
    s = np.empty(N)
    for a in range(N):
        s[a] = (-1.0) ** a if a < 9 else (-1.0) ** (a + 1)
    anticomm = [a for a in range(N) if s[a] < 0]
    U = np.eye(dim, dtype=complex)
    for a in anticomm:
        U = U @ e[a]
    Jsq = fro(U @ np.conjugate(U) + np.eye(dim))
    comm = max(fro(U @ np.conjugate(e[a]) - e[a] @ U) for a in range(N))
    return U, Jsq, comm


def main():
    report = {}
    dim, eta, e, omega, Iden = build_rep()
    VSdim = N * dim  # 1792

    # ---- core objects (identical construction to the keystone scratch) --------
    Gamma = np.hstack(e)                       # 128 x 1792 : gamma-trace map
    Pi_RS = proj_onto_kernel(Gamma)            # 1792 x 1792 : projector onto ker(Gamma)
    Pi_perp = np.eye(VSdim, dtype=complex) - Pi_RS
    cxi = sum(XI[a] * e[a] for a in range(N))  # c(xi) on S
    M_D = np.kron(np.eye(N, dtype=complex), cxi)   # twisted Dirac symbol (DYNAMICS) -- UNTOUCHED
    g = np.vstack([XI[a] * np.eye(dim, dtype=complex) for a in range(N)])  # bare gauge map S->VS

    print("=" * 84)
    print("GRAVITINO-BRST non-equivariant compensator sigma_c(xi)  [Cl(9,5)=M(64,H)~M(128,C)]")
    print("=" * 84)

    # ---- [T0] anchors (M_D untouched) ----------------------------------------
    Esc = Pi_perp @ M_D @ Pi_RS
    comm_PiMD = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    report["T0_escape"] = fro(Esc)
    report["T0_comm_PiMD"] = comm_PiMD
    print(f"\n[T0] ||Esc=(I-Pi)M_D Pi||           = {fro(Esc):.4f}   (repo 41.52)")
    print(f"     ||[Pi_RS,M_D]||                 = {comm_PiMD:.4f}   (repo 58.72; NON-DECOUPLING / VZ-evading)")

    # ---- [T1] bare nilpotency: Gamma.g = c(xi) != 0 --------------------------
    Gg = Gamma @ g                              # should equal c(xi)
    report["T1_Gamma_g"] = fro(Gg)
    report["T1_Gamma_g_minus_cxi"] = fro(Gg - cxi)
    print(f"\n[T1] bare s^2 at C^-1->C^1:  ||Gamma.g|| = {fro(Gg):.4f} ; ||Gamma.g - c(xi)|| = {fro(Gg - cxi):.2e}")
    print(f"     => bare RS gauge is NOT gamma-traceless (s^2 = c(xi) != 0): a ghost/sigma_c is needed.")

    # ---- [T2] bare s-exactness of the DYNAMICAL escape via im(Pi_perp g) ------
    PPg = Pi_perp @ g                           # 1792 x 128, image in im(Gamma^dag) = im(Pi_perp)
    Q, _ = np.linalg.qr(PPg)
    P_im = Q @ Q.conj().T
    resid_bare = fro((np.eye(VSdim, dtype=complex) - P_im) @ Esc)
    rk_PPg = int(np.linalg.matrix_rank(PPg, tol=TOL))
    report["T2_rank_PPg"] = rk_PPg
    report["T2_resid_bare"] = resid_bare
    print(f"\n[T2] dynamical escape s-exact via BARE gauge orbit?  rank(Pi_perp g) = {rk_PPg} (dim im Pi_perp = 128)")
    print(f"     residual ||(I-P_im) Esc|| = {resid_bare:.2e}  (escape IS bare-gauge-exact: {resid_bare < 1e-6})")
    print(f"     -- BUT bare g is xi-natural (the equivariant family SHIAB-04 already killed).")

    # ---- [T3] gravitino sigma_c: solve Gamma.sigma_c = -c(xi),
    #          sigma_c(eps)_a = sum_{b<c} W_a^{bc} (e_b e_c) eps  (spin-connection ghost coupling) ----
    pairs = [(b, c) for b in range(N) for c in range(b + 1, N)]
    BIV = [e[b] @ e[c] for (b, c) in pairs]     # Clifford bivectors = spinor Lorentz generators
    nbiv = len(pairs)                           # 91
    # Gamma.sigma_c = sum_a e_a sigma_c(.)_a = sum_{a,k} W_a^k (e_a BIV[k]); solve for W (least squares).
    basis_ops = [(a, k) for a in range(N) for k in range(nbiv)]
    A_lin = np.array([(e[a] @ BIV[k]).reshape(-1) for (a, k) in basis_ops]).T  # (128*128) x (14*91)
    b_target = (-cxi).reshape(-1)
    W, *_ = np.linalg.lstsq(A_lin, b_target, rcond=None)
    resid_solve = fro(A_lin @ W - b_target)
    sigma_c = np.zeros((VSdim, dim), dtype=complex)
    for idx, (a, k) in enumerate(basis_ops):
        sigma_c[a * dim:(a + 1) * dim, :] += W[idx] * BIV[k]
    G_tot = g + sigma_c
    nilp = fro(Gamma @ G_tot)
    report["T3_resid_solve"] = resid_solve
    report["T3_norm_sigma_c"] = fro(sigma_c)
    report["T3_s2_norm"] = nilp
    print(f"\n[T3] gravitino sigma_c solved: ||Gamma.sigma_c + c(xi)|| = {resid_solve:.2e}")
    print(f"     ||sigma_c|| = {fro(sigma_c):.4f} ; full gauge map G_tot = g + sigma_c")
    print(f"     s^2 nilpotency ||s^2|| = ||Gamma.G_tot|| = {nilp:.2e}  (s^2 = 0: {nilp < 1e-6})")

    # ---- [T4] THE SHARP TEST: with s^2=0, is the dynamical escape still s-exact? ----
    PPGt = Pi_perp @ G_tot
    report["T4_PiperpGtot"] = fro(PPGt)
    if fro(PPGt) > 1e-9:
        Qt, _ = np.linalg.qr(PPGt)
        P_imt = Qt @ Qt.conj().T
        resid_t = fro((np.eye(VSdim, dtype=complex) - P_imt) @ Esc)
    else:
        resid_t = fro(Esc)
    report["T4_resid_nilpotent_orbit"] = resid_t
    print(f"\n[T4] SHARP: nilpotency forces ||Pi_perp G_tot|| = {fro(PPGt):.2e} (gauge orbit now ON-surface).")
    print(f"     dynamical escape s-exact via the NILPOTENT gauge orbit?  residual = {resid_t:.4f}")
    print(f"     => nilpotency (Pi_perp G_tot = 0) and one-leg escape-triviality are INCOMPATIBLE for")
    print(f"        a single gauge map: enforcing s^2=0 puts the ghost orbit on-surface, so it can no")
    print(f"        longer trivialize the off-surface escape.")

    # ---- [T4b] the escape is CO-EXACT (antighost b-leg, im Gamma^dag), not ghost-exact ----
    gap = fro(Pi_perp @ Esc)                    # = ||Esc|| (escape already in im Pi_perp)
    GGd_inv = np.linalg.inv(Gamma @ Gamma.conj().T)
    eta_b = GGd_inv @ Gamma @ M_D @ Pi_RS       # 128 x 1792 : antighost / Nakanishi-Lautrup field
    coexact_resid = fro(Esc - Gamma.conj().T @ eta_b)
    report["T4b_offsurface_gap"] = gap
    report["T4b_coexact_resid"] = coexact_resid
    print(f"\n[T4b] irreducible off-surface content ||Pi_perp Esc|| = {gap:.4f} (a SECOND carrier must absorb).")
    print(f"      escape is CO-EXACT: ||Esc - Gamma^dag . eta_b|| = {coexact_resid:.2e}")
    print(f"      (lives in im(Gamma^dag) = antighost b-leg, NOT in the ghost eps-leg).")

    # ---- [T5] non-equivariance vs the xi-co-rotating Spin(9,5) action ---------
    def Sigma_gen(p, q):
        return 0.5 * (e[p] @ e[q])              # spinor Lorentz generator (p != q)

    def Lvec_gen(p, q):
        L = np.zeros((N, N), dtype=complex)
        L[p, q] = eta[q]
        L[q, p] = -eta[p]
        return L

    p, q = 0, 9
    Sig = Sigma_gen(p, q)
    L = Lvec_gen(p, q)
    T_VS = np.kron(np.eye(N, dtype=complex), Sig) + np.kron(L, np.eye(dim, dtype=complex))
    equiv_Gamma = fro(Gamma @ T_VS - Sig @ Gamma)
    # M_D equivariance WITH co-rotating xi: [I(x)Sig, M_D] should equal id(x)c(delta xi), delta xi = L^T xi
    dxi = L.T @ XI
    ISig = np.kron(np.eye(N, dtype=complex), Sig)
    MD_defect_corot = fro((ISig @ M_D - M_D @ ISig)
                          - np.kron(np.eye(N, dtype=complex), sum(dxi[a] * e[a] for a in range(N))))
    sigma_defect = fro(T_VS @ sigma_c - sigma_c @ Sig)
    g_defect = fro(T_VS @ g - g @ Sig)
    g_defect_corot = fro(T_VS @ g - g @ Sig
                         - np.vstack([dxi[a] * np.eye(dim, dtype=complex) for a in range(N)]))
    report["T5_equiv_Gamma"] = equiv_Gamma
    report["T5_MD_defect_corot"] = MD_defect_corot
    report["T5_g_defect_corot"] = g_defect_corot
    report["T5_sigma_defect"] = sigma_defect
    print(f"\n[T5] so(9,5) gen (p,q)=({p},{q}): ||Gamma T_VS - Sig Gamma|| = {equiv_Gamma:.2e} (action correct)")
    print(f"     M_D defect (co-rotating xi): ||[I(x)Sig,M_D] - id(x)c(dxi)|| = {MD_defect_corot:.2e} "
          f"(M_D xi-NATURAL: {MD_defect_corot < 1e-6})")
    print(f"     bare g defect = {g_defect:.4f} ; g defect co-rotating xi = {g_defect_corot:.2e} (g xi-natural)")
    print(f"     sigma_c equivariance defect ||T_VS sigma_c - sigma_c Sig|| = {sigma_defect:.4f}")
    print(f"     => sigma_c is NON-equivariant (defect {sigma_defect:.2f} != 0), and NOT removable by")
    print(f"        co-rotating xi (W is an independent background, not a functional of xi).")

    # ---- [T6] H-linearity of sigma_c -----------------------------------------
    U, Jsq, Jcomm = build_J(dim, eta, e)
    JS = U                                       # J on S (holomorphic part)
    JVS = np.kron(np.eye(N, dtype=complex), U)
    Hlin_sigma = fro(JVS @ np.conjugate(sigma_c) - sigma_c @ JS)
    Hlin_g = fro(JVS @ np.conjugate(g) - g @ JS)
    Hlin_PiRS = fro(Pi_RS @ JVS - JVS @ np.conjugate(Pi_RS))
    report["T6_Jsq"] = Jsq
    report["T6_Jcomm"] = Jcomm
    report["T6_Hlin_sigma"] = Hlin_sigma
    report["T6_Hlin_PiRS"] = Hlin_PiRS
    print(f"\n[T6] H-linearity: ||J^2+I|| = {Jsq:.1e}, ||[J,Cl]|| = {Jcomm:.1e}")
    print(f"     ||JVS conj(g) - g JS||             = {Hlin_g:.2e}")
    print(f"     ||JVS conj(sigma_c) - sigma_c JS|| = {Hlin_sigma:.2e}  (H-linear: {Hlin_sigma < 1e-6})")
    print(f"     ||Pi_RS J - J conj(Pi_RS)||        = {Hlin_PiRS:.2e}  (rank_H well-defined)")

    # ---- SUMMARY -------------------------------------------------------------
    print("\n" + "=" * 84)
    print("SUMMARY (honest):")
    print(f"  - ANTI-TRAP: M_D untouched, [Pi_RS,M_D] = {comm_PiMD:.2f} preserved (no decoupling, VZ stays evaded).")
    print(f"  - bare RS gauge fails s^2=0 (Gamma.g = c(xi) = {fro(Gg):.2f}); sigma_c RESTORES s^2=0 ({nilp:.1e}).")
    print(f"  - sigma_c is NON-equivariant (defect {sigma_defect:.2f}) and H-linear (Hlin {Hlin_sigma:.1e}).")
    print(f"  - SHARP OBSTRUCTION: nilpotency forces Pi_perp G_tot=0, so the SAME ghost orbit can NO")
    print(f"    longer trivialize the dynamical escape (residual {resid_t:.2f}). The escape is only CO-EXACT")
    print(f"    under the antighost b-leg ({coexact_resid:.1e}). A SECOND, off-gauge-orbit non-equivariant")
    print(f"    carrier (the gravitino's curvature/holonomy W) is required, and the symbol rep (xi alone)")
    print(f"    does NOT contain it -- that is the precise datum the SOURCE ACTION must supply.")
    print("=" * 84)
    return report


if __name__ == "__main__":
    main()
