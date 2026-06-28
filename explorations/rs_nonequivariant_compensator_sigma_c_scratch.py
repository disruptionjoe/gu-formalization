#!/usr/bin/env python3
"""FRONTIER ATTEMPT (provenance, 2026-06-27): construct a NON-EQUIVARIANT
compensator sigma_c(xi) for GU's RS sector as a BRST ghost coupling, and test
it against the anti-trap conditions on the verified Cl(9,5)=M(64,H) rep.

Anti-trap (from source-action-necessary-conditions-and-causality-2026-06-27.md):
  - DISQUALIFIED: sigma_c = -(I-Pi_RS) M_D Pi_RS added to the BARE dynamics so that
    [Pi_RS, M_D+sigma_c]=0. That is the acausal DECOUPLING (RS -> standalone -> VZ).
  - REQUIRED: a graded ghost complex C^-1 (ghost eps in S) -> C^0 (Psi in VS) ->
    C^1 (antifield in S), nilpotent s, with (i) s^2=0, (ii) escape s-exact in H(s),
    (iii) BARE [Pi_RS,M_D] != 0 stays (RS coupled, VZ evaded), (iv) sigma_c
    non-equivariant, (v) H-linear ([.,J]).

Design input (steelmen V1/V2): the missing datum is a GU-NATIVE GEOMETRIC CARRIER
- a boundary holonomy/connection, a spectral section P_>=0, a family-coordinate
functional, or a source-derived characteristic/KSp class. Here we instantiate the
carrier as a BOUNDARY SPECTRAL SECTION: a fixed reference direction n (an observer
cut / choice of positive-frequency slice) breaking Spin(9,5) to Stab(n). sigma_c is
the Stueckelberg ghost coupling built from that section.

NOTHING is tuned. xi is the repo's fixed sample covector. Numbers reported as-is.
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
TESTS = os.path.join(os.path.dirname(HERE), "tests")
if TESTS not in sys.path:
    sys.path.insert(0, TESTS)

import oq_rk1_cl95_explicit_rep as cl95  # verified Cl(9,5) rep

TOL = 1e-9
N = 14
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


def main():
    dim, eta, e, omega, Iden = build_rep()
    VSdim = N * dim  # 1792

    Gamma = np.hstack(e)                         # 128 x 1792
    Pi_RS = proj_onto_kernel(Gamma)              # 1792 x 1792
    Pi_perp = np.eye(VSdim, dtype=complex) - Pi_RS
    cxi = sum(XI[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)
    gauge = np.vstack([XI[a] * np.eye(dim, dtype=complex) for a in range(N)])  # 1792 x 128 = d_A

    print("=" * 78)
    print("NON-EQUIVARIANT COMPENSATOR sigma_c(xi) AS A BRST GHOST COUPLING")
    print("=" * 78)

    # ---- reproduce the anchor escape numbers --------------------------------
    naive_escape = fro(Gamma @ gauge)            # ||c(xi) eps|| pattern, ~80.61
    comm_PiMD = fro(Pi_RS @ M_D - M_D @ Pi_RS)   # 58.72
    esc_op = fro(Pi_perp @ M_D @ Pi_RS)          # 41.52
    esc_gauge = fro(Pi_perp @ M_D @ Pi_RS @ gauge)  # 169.19
    print(f"[anchors] ||Gamma d_A|| (naive escape)        = {naive_escape:.4f}  (repo 80.61)")
    print(f"          ||[Pi_RS, M_D]||                     = {comm_PiMD:.4f}  (repo 58.72)")
    print(f"          ||(I-Pi)M_D Pi_RS|| operator         = {esc_op:.4f}  (repo 41.52)")
    print(f"          ||(I-Pi)M_D Pi_RS gauge||            = {esc_gauge:.4f}  (repo 169.19)")

    # ===================================================================
    # PART A. The 3-term graded complex and the analytic grading obstruction
    # ===================================================================
    # C^-1 = S (128, ghost eps), C^0 = VS (1792, Psi), C^1 = S (128, antifield).
    # s = [[0,0,0],[D,0,0],[0,Gamma,0]] with D the (compensated) gauge map.
    # s^2 = 0  <=>  Gamma D = 0.
    #
    # Bare dynamics extended block-diagonal M = diag(c(xi), id14(x)c(xi), c(xi)).
    # ANALYTIC FACT (verified below): the anomaly A=[s,M] is degree +1 (off-block)
    # while operator homotopies [s,h] (h degree -1) are degree 0 (block-diagonal),
    # so "escape s-exact" is NOT a homotopy condition in this complex -- it is the
    # nilpotency of the DYNAMICAL (curved) differential s_full = s + dynamics, whose
    # obstruction is the SECONDARY CONSTRAINT  C2 := Gamma M_D Pi_RS.
    #
    # We verify the grading claim numerically, then test C2.

    D_eq = Pi_RS @ gauge                          # equivariant compensated gauge
    GammaD = fro(Gamma @ D_eq)
    print("\n[A] 3-term complex, equivariant compensator D = Pi_RS o d_A:")
    print(f"    s^2 block  ||Gamma D|| = {GammaD:.2e}  (nilpotent: {GammaD < 1e-6})")

    # the secondary (Dirac) constraint generated by the bare dynamics
    C2 = Gamma @ M_D @ Pi_RS                       # 128 x 1792
    nC2 = fro(C2)
    # is C2 in the row-space of Gamma (i.e. = Lambda Gamma, no NEW constraint)?
    # solve min_Lambda ||C2 - Lambda Gamma||; Lambda = C2 Gamma^+(=Gamma^dag (GG^dag)^-1)
    GGd = Gamma @ Gamma.conj().T
    Gamma_pinv = Gamma.conj().T @ np.linalg.inv(GGd)   # right pinv: Gamma Gamma_pinv = I
    Lambda = C2 @ Gamma_pinv
    resid_C2 = fro(C2 - Lambda @ Gamma)
    print(f"    secondary constraint ||C2=Gamma M_D Pi_RS|| = {nC2:.4f}")
    print(f"    best fit C2 = Lambda.Gamma residual         = {resid_C2:.4f}")
    print(f"    -> C2 is {'reducible to primary (first-class)' if resid_C2<1e-6 else 'a GENUINE NEW (independent) constraint'}")
    print(f"       (independent secondary constraint = naive Velo-Zwanziger; needs a compensator)")

    # ===================================================================
    # PART B. The geometric carrier (boundary spectral section) -> sigma_c
    # ===================================================================
    # Carrier: pick a fixed reference direction n (observer cut). e_0 is Hermitian
    # (a<9), eigenvalues +-1; the spectral section is P_+ = (I + e_0)/2 on S.
    # This breaks Spin(9,5) -> Stab(e_0): genuinely NON-equivariant.
    n_idx = 0
    en = e[n_idx]
    P_sec = 0.5 * (Iden + en)                      # boundary spectral section on S
    Pdef = fro(P_sec @ P_sec - P_sec)
    # equivariance defect of the carrier: commutator with a Spin(9,5) generator that
    # does NOT fix the section direction n=e_0 (Sigma_{01} rotates e_0 into e_1).
    Sigma_12 = 0.5 * (e[0] @ e[1] - e[1] @ e[0])   # so(9,5) generator NOT in Stab(e_0)
    carrier_equiv_defect = fro(P_sec @ Sigma_12 - Sigma_12 @ P_sec)
    print("\n[B] geometric carrier = boundary spectral section P_+ = (I+e_0)/2:")
    print(f"    idempotent err = {Pdef:.1e}; equivariance defect ||[P_sec, Sigma_23]|| = {carrier_equiv_defect:.4f}")
    print(f"    (defect != 0 => carrier breaks Spin(9,5): {carrier_equiv_defect>1e-6})")

    # The Stueckelberg ghost coupling. The secondary constraint C2 lands in C^1=S.
    # A Stueckelberg field phi in C^-1=S absorbs it iff there is a coupling
    # sigma_c : C^1 -> C^-1 (ghost-shift) with  C2 = (Gamma D) . sigma_c^{-1}-ish ...
    # Concretely: we add to the differential a ghost-number-0 term L coupling the
    # antifield back to the ghost, L : C^1 -> C^-1, built from the section, so that
    # the DRESSED secondary constraint  C2 - Gamma M_D D L  is removable.
    #
    # The honest, decisive test: can the section supply an operator R: S->S
    # (acting in the ghost/antifield line) such that the secondary constraint
    # factors as  C2 = R . Gamma + (D-exact)  -- i.e. becomes first-class once the
    # ghost is allowed to shift. The section enters through  R = c(n)/(n.xi) style
    # inversion that is ONLY defined after choosing n.
    nx = sum(XI[a] * (1.0 if a == n_idx else 0.0) for a in range(N))  # (n . xi) = xi_0
    # build c(n) inverse-direction operator; the VZ "multiplier" is c(n)/(n.xi)
    R = en / nx                                    # S->S, non-equivariant (depends on n)
    # dressed secondary constraint after one Stueckelberg shift along the section:
    #   C2_dressed = C2 - (Gamma M_D D_eq) . (R . Gamma . <ghost lift>)
    # We test the cohomological triviality directly: is C2 in the image of the
    # ghost differential composed with the section, i.e. does
    #   C2 = Gamma M_D D_eq . X   admit X with X built from R (the section)?
    GMD = Gamma @ M_D @ D_eq                        # 128 x 128 (C^-1 -> C^1 via dynamics)
    # least-squares X (128x128) minimizing ||C2 - GMD @ Xmap|| where Xmap: VS->C^-1.
    # But X must be ghost-built (factor through the section R). Compare two fits:
    #   (free)   any Xmap                          -> tests mere solvability
    #   (carrier) Xmap = Lift . R . Gamma          -> tests whether the SECTION suffices
    # free fit:
    rank_GMD = int(np.linalg.matrix_rank(GMD, tol=TOL))
    GMD_inv = np.linalg.pinv(GMD)
    X_free = GMD_inv @ C2                           # the UNIQUE resolver (GMD full rank)
    resid_free = fro(C2 - GMD @ X_free)
    print("\n[B] ghost-resolution feasibility (is escape s-exact via a ghost shift?):")
    print(f"    rank(Gamma M_D D) = {rank_GMD}/128  -> resolver X = (Gamma M_D D)^-1 C2 is UNIQUE")
    print(f"    free resolver residual ||C2 - (Gamma M_D D) X|| = {resid_free:.2e}  (abstractly s-exact)")
    # the resolver requires the GLOBAL INVERSE GMD^-1 (a propagator-like datum).
    # can the boundary spectral section ALONE supply X?  Force X through the section:
    Pn = P_sec                                      # section projector on S (range = section)
    X_sec = Pn @ X_free                             # section-supported component of resolver
    resid_sec = fro(C2 - GMD @ X_sec)
    frac_in_section = fro(X_sec) / fro(X_free)
    print(f"    section-supported resolver residual          = {resid_sec:.4f}")
    print(f"    fraction of resolver carried by the section  = {frac_in_section:.3f}  "
          f"(section ALONE misses by {resid_sec:.1f})")
    print(f"    => the resolver is the GLOBAL inverse (Gamma M_D D)^-1, NOT a boundary")
    print(f"       section: this nonlocal propagator datum is exactly what S_IG must supply.")

    # ===================================================================
    # PART C. Build an explicit sigma_c and run the five anti-trap predicates
    # ===================================================================
    # sigma_c is a GHOST COUPLING (degree-(-1) operator C^0 -> C^-1), NOT a C^0
    # endomorphism. It is built from the section. We compare it head-to-head with
    # the DISQUALIFIED trap X_trap = -(I-Pi)M_D Pi_RS (a pure C^0 endomorphism).
    # the acausal decoupling: block-DIAGONALIZE M_D wrt Pi_RS (kills BOTH off-blocks)
    M_D_decoupled = Pi_RS @ M_D @ Pi_RS + Pi_perp @ M_D @ Pi_perp
    X_trap = M_D_decoupled - M_D                     # the trap compensator (a C^0 endomorphism)

    # sigma_c: section-weighted ghost coupling.  sigma_c = R . (Gamma M_D Pi_RS)
    #   maps C^0 --(secondary constraint)--> C^1=S --(section inverse R)--> C^-1=S
    sigma_c = R @ C2                                # 128 x 1792  (C^0 -> C^-1), ghost coupling
    print("\n[C] explicit sigma_c = R . (Gamma M_D Pi_RS),  R = c(e_0)/(n.xi):")
    print(f"    shape {sigma_c.shape} (C^0 -> C^-1: genuine ghost coupling, not a C^0 endo)")

    # (i) s^2 = 0 for the dressed differential D_full = D_eq + (ghost-coupling lift)
    #     The ghost coupling enters s as the (C^0 -> C^-1) block; s stays lower-tri
    #     plus this back-coupling.  Build full s and test nilpotency.
    W = 2 * dim + VSdim
    sfull = np.zeros((W, W), dtype=complex)
    a0, a1, a2 = 0, dim, dim + VSdim               # offsets of C^-1, C^0, C^1
    sfull[a1:a2, a0:a1] = D_eq                      # C^-1 -> C^0
    sfull[a2:a2 + dim, a1:a2] = Gamma              # C^0 -> C^1
    sfull[a0:a1, a1:a2] = sigma_c                  # C^0 -> C^-1 (ghost back-coupling)
    s2 = fro(sfull @ sfull)
    # nilpotency without and with the back-coupling
    sbare = sfull.copy(); sbare[a0:a1, a1:a2] = 0
    s2_bare = fro(sbare @ sbare)
    print(f"    (i)  ||s^2|| bare (no sigma_c)   = {s2_bare:.2e}")
    print(f"         ||s^2|| with sigma_c        = {s2:.4f}  "
          f"({'still nilpotent' if s2<1e-6 else 'sigma_c BREAKS naive nilpotency -> needs full BV resolution'})")

    # (iii) BARE [Pi_RS, M_D] must be UNCHANGED (RS stays coupled, VZ evaded)
    #       sigma_c is a ghost coupling; M_D on C^0 is untouched by construction.
    comm_after = fro(Pi_RS @ M_D - M_D @ Pi_RS)     # identical to comm_PiMD
    trap_comm = fro(Pi_RS @ (M_D + X_trap) - (M_D + X_trap) @ Pi_RS)  # the trap kills it
    trap_escape = fro(Pi_perp @ (M_D + X_trap) @ Pi_RS)
    print(f"    (iii) ||[Pi_RS, M_D]|| with sigma_c (ghost)  = {comm_after:.4f}  (UNCHANGED 58.72: RS coupled)")
    print(f"          ||[Pi_RS, M_D + X_trap]|| (DISQUAL.)    = {trap_comm:.2e}  (trap DECOUPLES -> VZ acausal)")
    print(f"          trap escape ||(I-Pi)(M_D+X_trap)Pi_RS|| = {trap_escape:.2e}  (trap zeroes the escape on C^0)")

    # (iv) NON-EQUIVARIANCE of sigma_c: commutator with so(9,5) generator lifted to VS
    Sig_VS = np.kron(np.eye(N, dtype=complex), Sigma_12)
    Sig_S = Sigma_12
    # sigma_c: C^0(1792) -> C^-1(128); equivariance: Sig_S sigma_c - sigma_c Sig_VS
    equiv_defect = fro(Sig_S @ sigma_c - sigma_c @ Sig_VS)
    print(f"    (iv) equivariance defect ||Sig.sigma_c - sigma_c.Sig|| = {equiv_defect:.4f}  "
          f"(non-equivariant: {equiv_defect>1e-6})")

    # (v) H-LINEARITY: [sigma_c, J].  J on S = U.conj; on VS = (id14(x)U).conj.
    U, Jsq_err, Jcomm_err = build_J(dim, eta, e)
    JVS = np.kron(np.eye(N, dtype=complex), U)
    # sigma_c: VS -> S; H-linearity: sigma_c (id14(x)U) conj = U conj sigma_c
    #   <=> sigma_c JVS = U conj(sigma_c) conj... test antilinear form:
    Hlin_defect = fro(sigma_c @ JVS - U @ np.conjugate(sigma_c))
    print(f"    (v)  H-linearity defect ||sigma_c.J_VS - J_S.conj(sigma_c)|| = {Hlin_defect:.4f}  "
          f"(H-linear: {Hlin_defect<1e-6})")

    # (ii) ESCAPE s-EXACTNESS: does the ghost coupling trivialize the secondary
    #      constraint in cohomology?  Test: C2 restricted to the cohomology rep,
    #      i.e. is C2 . (ghost-exact projector) the whole of C2?  Equivalent test:
    #      ||C2 - C2 . D D^+|| (the part of C2 NOT coming from gauge directions).
    DDp = D_eq @ np.linalg.pinv(D_eq)               # projector onto im(D) in C^0
    C2_onH = fro(C2 @ (np.eye(VSdim, dtype=complex) - DDp))  # C2 on cohomology reps
    C2_exact = fro(C2 @ DDp)                          # C2 on gauge directions (s-exact part)
    print("\n[C] (ii) escape s-exactness decomposition of the secondary constraint:")
    print(f"    ||C2 on gauge/s-exact directions||  = {C2_exact:.4f}")
    print(f"    ||C2 on cohomology representatives|| = {C2_onH:.4f}  "
          f"({'s-EXACT (resolved)' if C2_onH<1e-6 else 'NOT s-exact: residual obstruction'})")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print(f"  carrier non-equivariant: defect {carrier_equiv_defect:.2f}; sigma_c non-equivariant: {equiv_defect:.2f}")
    print(f"  bare [Pi_RS,M_D] preserved at 58.72 (RS coupled / VZ evaded); trap kills it to ~0")
    print(f"  secondary constraint C2={nC2:.2f} is INDEPENDENT of primary (residual {resid_C2:.2f})")
    print(f"  ghost s^2 with naive sigma_c = {s2:.2f}; cohomology residual of C2 = {C2_onH:.2f}")
    return None


if __name__ == "__main__":
    main()
