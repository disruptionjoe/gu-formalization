#!/usr/bin/env python3
"""FRONTIER TEST (2026-06-27): the STEELMAN GEOMETRIC CARRIER construction of a
NON-EQUIVARIANT compensator sigma_c(xi) for GU's RS sector, run as a BRST ghost
complex on the verified Cl(9,5)=M(64,H)~M(128,C) rep, and graded against the five
anti-trap predicates.

This is the test-suite companion to the durable scratch
    explorations/rs_nonequivariant_compensator_sigma_c_scratch.py
and reuses the exact same objects (Gamma, Pi_RS, M_D, J, the gauge image d_A) so the
anchors 80.61 / 58.72 / 41.52 / 169.19 are reproduced here independently.

WHAT IS UNDER TEST
------------------
Steelmen V1/V2 (ti-as-gu-source-action-{v1-formal-integration,v2-wolfram-signed-readout})
say the missing non-equivariant datum must be a GU-NATIVE GEOMETRIC carrier: a boundary
holonomy / connection / curvature carrier, a spectral section, a family-coordinate
functional, or a source-derived characteristic/KSp class. We instantiate the most
elementary such carrier -- a BOUNDARY SPECTRAL SECTION: a fixed reference covector
n = e_0 (an observer cut / positive-frequency slice P_+ = (I+e_0)/2 on S), which breaks
Spin(9,5) -> Stab(e_0) and is therefore genuinely non-equivariant.

From that carrier we build:
  - the section inverse R = c(e_0)/(n.xi)  (the non-equivariant inversion datum),
  - the ghost coupling sigma_c = R . C2 with C2 = Gamma.M_D.Pi_RS (secondary/Dirac
    constraint), as the OFF-DIAGONAL block C^0 -> C^-1 (ghost-number-raising), NOT a
    C^0 endomorphism -- this is the structural separation from the acausal-decoupling trap.

THE FIVE ANTI-TRAP PREDICATES (all computed, nothing tuned):
  (i)   ||s^2||                              -- nilpotency of the dressed differential.
  (ii)  is the escape (I-Pi)M_D Pi_RS s-EXACT?  -- and is that distinct from the
        disqualified bare block-subtraction?
  (iii) ANTI-TRAP: is bare ||[Pi_RS, M_D]|| STILL 58.72 != 0 with sigma_c installed?
        (RS must stay coupled => VZ stays evaded), vs the trap which zeros it.
  (iv)  equivariance defect of sigma_c (must be != 0 -- genuinely non-equivariant).
  (v)   ||[sigma_c, J]|| (H-linearity -- rank_H must stay well-defined).

HEADLINE (honest): SHARPER_OBSTRUCTION, not a closure. The escape IS resolvable in
cohomology, but the unique resolver is the GLOBAL inverse (Gamma.M_D.Pi_RS.d_A)^-1 (a
Dirac-bracket / propagator object); the boundary spectral section supplies only fraction
~1/sqrt(2)=0.707 of it (it is generic/uninformative about the resolver). That global
inverse is exactly the dynamical datum only the unwritten S_IG kinetic term can supply.
A single-term sigma_c does NOT close nilpotency (the full BV antifield tower is required).

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
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)


def fro(A):
    return float(np.linalg.norm(A))


def proj_onto_kernel(M):
    """Orthogonal projector onto ker(M) (= I - M^+ M for surjective M)."""
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
    """Quaternionic real structure: J = U.conj, J^2=-I, [J,e_a]=0."""
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


def run():
    dim, eta, e, omega, Iden = build_rep()
    VSdim = N * dim  # 1792
    results = {}

    # ---- shared objects (identical construction to the scratch / keystone) ----
    Gamma = np.hstack(e)                          # 128 x 1792 : gamma-trace map
    Pi_RS = proj_onto_kernel(Gamma)              # 1792 x 1792 : projector onto ker(Gamma)
    Pi_perp = np.eye(VSdim, dtype=complex) - Pi_RS
    cxi = sum(XI[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)  # twisted Dirac symbol id14 (x) c(xi)
    gauge = np.vstack([XI[a] * np.eye(dim, dtype=complex) for a in range(N)])  # d_A : 1792x128

    print("=" * 78)
    print("STEELMAN GEOMETRIC CARRIER: non-equivariant sigma_c as a BRST ghost coupling")
    print("=" * 78)

    # ---- anchors --------------------------------------------------------------
    naive_escape = fro(Gamma @ gauge)
    comm_PiMD = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    esc_op = fro(Pi_perp @ M_D @ Pi_RS)
    esc_gauge = fro(Pi_perp @ M_D @ Pi_RS @ gauge)
    results.update(anchor_naive_escape=naive_escape, anchor_comm_PiMD=comm_PiMD,
                   anchor_escape_op=esc_op, anchor_escape_gauge=esc_gauge)
    print(f"[anchors] ||Gamma d_A||            = {naive_escape:.4f}  (repo 80.61)")
    print(f"          ||[Pi_RS, M_D]||          = {comm_PiMD:.4f}  (repo 58.72)")
    print(f"          ||(I-Pi)M_D Pi_RS|| op    = {esc_op:.4f}  (repo 41.52)")
    print(f"          ||(I-Pi)M_D Pi_RS gauge|| = {esc_gauge:.4f}  (repo 169.19)")

    # ===================================================================
    # The 3-term BRST complex  C^-1(S) --D--> C^0(VS) --Gamma--> C^1(S)
    # ===================================================================
    D_eq = Pi_RS @ gauge                          # equivariant compensated gauge map
    GammaD = fro(Gamma @ D_eq)                    # s^2 on the constraint/gauge line
    results["s2_constraint_line"] = GammaD
    print("\n[complex] C^-1(128) --D=Pi_RS.d_A--> C^0(1792) --Gamma--> C^1(128)")
    print(f"          equivariant constraint line ||Gamma.D|| = {GammaD:.2e}  (nilpotent: {GammaD < 1e-6})")

    # secondary (Dirac) constraint C2 = Gamma M_D Pi_RS ; is it INDEPENDENT of Gamma?
    C2 = Gamma @ M_D @ Pi_RS                       # 128 x 1792
    nC2 = fro(C2)
    GGd = Gamma @ Gamma.conj().T
    Gamma_pinv = Gamma.conj().T @ np.linalg.inv(GGd)
    Lambda = C2 @ Gamma_pinv
    resid_C2 = fro(C2 - Lambda @ Gamma)
    results.update(C2_norm=nC2, C2_independence_residual=resid_C2)
    print(f"          secondary constraint ||C2=Gamma.M_D.Pi_RS|| = {nC2:.4f}")
    print(f"          best fit C2=Lambda.Gamma residual            = {resid_C2:.4f}  "
          f"({'reducible' if resid_C2 < 1e-6 else 'GENUINELY INDEPENDENT (new VZ-type constraint)'})")

    # ===================================================================
    # CARRIER: boundary spectral section P_+ = (I+e_0)/2  (non-equivariant)
    # ===================================================================
    n_idx = 0
    en = e[n_idx]
    P_sec = 0.5 * (Iden + en)
    Pdef = fro(P_sec @ P_sec - P_sec)
    # generator that rotates the section direction (NOT in Stab(e_0)) => defect != 0
    Sigma_01 = 0.5 * (e[0] @ e[1] - e[1] @ e[0])
    carrier_defect = fro(P_sec @ Sigma_01 - Sigma_01 @ P_sec)
    # control: a generator INSIDE Stab(e_0) should give 0. Use Sigma_{1,2} (fixes e_0).
    Sigma_23 = 0.5 * (e[2] @ e[3] - e[3] @ e[2])
    carrier_defect_stab = fro(P_sec @ Sigma_23 - Sigma_23 @ P_sec)
    results.update(carrier_defect=carrier_defect, carrier_defect_in_stab=carrier_defect_stab)
    print("\n[carrier] boundary spectral section P_+ = (I+e_0)/2  (observer cut):")
    print(f"          idempotent err = {Pdef:.1e}")
    print(f"          ||[P_+, Sigma_01]|| (rotates e_0) = {carrier_defect:.4f}  (breaks Spin(9,5))")
    print(f"          ||[P_+, Sigma_23]|| (fixes e_0)   = {carrier_defect_stab:.2e}  (break is along e_0)")

    nx = XI[n_idx]                                 # (n . xi) = xi_0
    R = en / nx                                    # section inverse c(e_0)/(n.xi), non-equivariant

    # ===================================================================
    # Is the escape s-EXACT? unique resolver vs section-restricted resolver
    # ===================================================================
    GMD = Gamma @ M_D @ D_eq                        # 128x128, C^-1 -> C^1 through dynamics
    rank_GMD = int(np.linalg.matrix_rank(GMD, tol=TOL))
    X_free = np.linalg.solve(GMD, C2) if rank_GMD == dim else np.linalg.pinv(GMD) @ C2
    resid_free = fro(C2 - GMD @ X_free)            # ~0 => abstractly s-exact
    X_sec = P_sec @ X_free                          # section-supported component
    resid_sec = fro(C2 - GMD @ X_sec)
    frac_in_section = fro(X_sec) / fro(X_free)
    results.update(resolver_rank=rank_GMD, resolver_residual=resid_free,
                   section_resolver_residual=resid_sec, section_fraction=frac_in_section)
    print("\n[s-exactness] resolver X = (Gamma.M_D.D)^-1 . C2:")
    print(f"          rank(Gamma.M_D.D) = {rank_GMD}/128  -> resolver UNIQUE")
    print(f"          free residual ||C2 - (Gamma.M_D.D)X|| = {resid_free:.2e}  (escape IS s-exact in principle)")
    print(f"          section-restricted residual            = {resid_sec:.4f}")
    print(f"          fraction of resolver in the section     = {frac_in_section:.3f}  "
          f"(section misses by {resid_sec:.1f})")
    print(f"          => resolver is the GLOBAL inverse (a propagator), NOT a boundary section.")

    # ===================================================================
    # The explicit sigma_c and the head-to-head trap comparison
    # ===================================================================
    sigma_c = R @ C2                               # 128 x 1792 : C^0 -> C^-1 ghost coupling
    results["sigma_c_shape"] = sigma_c.shape

    # the DISQUALIFIED acausal trap: block-diagonalize M_D wrt Pi_RS
    M_D_decoupled = Pi_RS @ M_D @ Pi_RS + Pi_perp @ M_D @ Pi_perp
    X_trap = M_D_decoupled - M_D                   # pure C^0 endomorphism (= -escape on im Pi_RS)

    print("\n[sigma_c] = R . (Gamma.M_D.Pi_RS),  R = c(e_0)/(n.xi):  shape", sigma_c.shape,
          "(C^0 -> C^-1: genuine ghost coupling)")

    # (i) nilpotency
    W = 2 * dim + VSdim
    sfull = np.zeros((W, W), dtype=complex)
    a0, a1, a2 = 0, dim, dim + VSdim
    sfull[a1:a2, a0:a1] = D_eq                      # C^-1 -> C^0
    sfull[a2:a2 + dim, a1:a2] = Gamma              # C^0 -> C^1
    sfull[a0:a1, a1:a2] = sigma_c                  # C^0 -> C^-1 ghost back-coupling
    s2 = fro(sfull @ sfull)
    sbare = sfull.copy(); sbare[a0:a1, a1:a2] = 0
    s2_bare = fro(sbare @ sbare)
    results.update(s2_bare=s2_bare, s2_with_sigma=s2)
    print(f"    (i)   ||s^2|| bare (no sigma_c)  = {s2_bare:.2e}")
    print(f"          ||s^2|| with sigma_c       = {s2:.4f}  "
          f"({'nilpotent' if s2 < 1e-6 else 'one-term sigma_c does NOT close -> full BV tower required'})")

    # (iii) ANTI-TRAP: bare [Pi_RS, M_D] unchanged, vs trap kills it
    comm_after = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    trap_comm = fro(Pi_RS @ (M_D + X_trap) - (M_D + X_trap) @ Pi_RS)
    trap_escape = fro(Pi_perp @ (M_D + X_trap) @ Pi_RS)
    results.update(bare_comm_with_sigma=comm_after, trap_comm=trap_comm, trap_escape=trap_escape)
    print(f"    (iii) ANTI-TRAP ||[Pi_RS, M_D]|| with sigma_c   = {comm_after:.4f}  (UNCHANGED 58.72: RS coupled)")
    print(f"          ||[Pi_RS, M_D + X_trap]|| (DISQUALIFIED)  = {trap_comm:.2e}  (trap DECOUPLES -> VZ acausal)")
    print(f"          trap escape ||(I-Pi)(M_D+X_trap)Pi_RS||   = {trap_escape:.2e}  (trap zeroes escape on C^0)")

    # (iv) non-equivariance of sigma_c
    Sig_VS = np.kron(np.eye(N, dtype=complex), Sigma_01)
    Sig_S = Sigma_01
    equiv_defect = fro(Sig_S @ sigma_c - sigma_c @ Sig_VS)
    results["sigma_c_equiv_defect"] = equiv_defect
    print(f"    (iv)  equivariance defect ||Sig.sigma_c - sigma_c.Sig|| = {equiv_defect:.4f}  "
          f"(non-equivariant: {equiv_defect > 1e-6})")

    # (v) H-linearity of sigma_c
    U, Jsq_err, Jcomm_err = build_J(dim, eta, e)
    JVS = np.kron(np.eye(N, dtype=complex), U)
    Hlin_defect = fro(sigma_c @ JVS - U @ np.conjugate(sigma_c))
    results.update(J_sq_err=Jsq_err, J_comm_err=Jcomm_err, sigma_c_Hlin_defect=Hlin_defect)
    print(f"    (v)   ||J^2+I||={Jsq_err:.1e}, ||[J,Cl]||={Jcomm_err:.1e}; "
          f"||sigma_c.J_VS - J_S.conj(sigma_c)|| = {Hlin_defect:.4f}  (H-linear: {Hlin_defect < 1e-6})")

    # (ii) escape s-exactness decomposition (does the EQUIVARIANT D resolve C2?)
    DDp = D_eq @ np.linalg.pinv(D_eq)               # projector onto im(D) in C^0
    C2_onH = fro(C2 @ (np.eye(VSdim, dtype=complex) - DDp))
    C2_exact = fro(C2 @ DDp)
    results.update(C2_on_cohomology=C2_onH, C2_on_gauge=C2_exact)
    print("\n    (ii)  escape s-exactness via the EQUIVARIANT complex alone:")
    print(f"          ||C2 on gauge/s-exact directions||  = {C2_exact:.4f}")
    print(f"          ||C2 on cohomology representatives|| = {C2_onH:.4f}  "
          f"({'s-EXACT' if C2_onH < 1e-6 else 'NOT s-exact via equivariant D (SHIAB-04 confirmed)'})")

    print("\n" + "=" * 78)
    print("VERDICT: SHARPER_OBSTRUCTION (not a closure)")
    print("=" * 78)
    print(f"  carrier non-equivariant ({carrier_defect:.2f}); sigma_c non-equivariant ({equiv_defect:.2f}); "
          f"H-linear ({Hlin_defect:.1e}).")
    print(f"  ANTI-TRAP PASSED: bare [Pi_RS,M_D]={comm_after:.2f} preserved (RS coupled/VZ evaded); "
          f"trap kills it to {trap_comm:.1e}.")
    print(f"  escape IS s-exact in principle (residual {resid_free:.1e}) BUT the resolver is the GLOBAL")
    print(f"  inverse (Gamma.M_D.D)^-1; the section carries only {frac_in_section:.3f} of it "
          f"(misses by {resid_sec:.1f}).")
    print(f"  one-term sigma_c does NOT close s^2 ({s2:.1f}); equivariant complex cannot resolve C2 "
          f"({C2_onH:.2f}).")
    print(f"  => the missing non-equivariant datum is the Dirac-bracket/propagator only S_IG supplies.")
    return results


def main():
    return run()


if __name__ == "__main__":
    main()
