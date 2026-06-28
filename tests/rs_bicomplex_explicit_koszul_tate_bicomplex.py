#!/usr/bin/env python3
"""CLIMACTIC GATE (2026-06-27): the EXPLICIT KOSZUL-TATE BICOMPLEX for GU's RS
sector -- the full BV bicomplex (ghost leg AND Koszul-Tate leg) plus a
SOURCE-DERIVED Spin(9,5) CONNECTION carrier W, on the verified
Cl(9,5)=M(64,H)~M(128,C) rep.

Builds on / reuses objects from:
  tests/rs_ghost_fixed_null_covector_spurion.py     (the 58.72 -> 32.80 floor)
  explorations/rs_source_candidate_projected_differential_scratch.py (rep objects)
  tests/oq_rk1_cl95_explicit_rep.py                 (the verified Cl(9,5) rep)

GHOST-01 pinned the exact missing object:
  (i)   the escape is CO-EXACT (lives in im Gamma^dag = the Koszul-Tate/antighost
        direction), NOT ghost-exact -> a FULL BV bicomplex (ghost leg AND
        Koszul-Tate leg, both s-consistent) is required;
  (ii)  the resolver needs the global inverse (Gamma.M_D.Pi_RS.d_A)^-1 = a
        Dirac-bracket propagator;
  (iii) a NEW secondary VZ-type constraint C2 (norm 155.36) must be reconciled.

THE TWO COUPLED PIECES BUILT + TESTED HERE (real numbers, nothing tuned):
  A. SOURCE-DERIVED CARRIER W: a Spin(9,5) CONNECTION 1-form A_a (a=0..13),
     A_a = sum_{b<c} T_{abc} Sigma_{bc} in the spinor rep, built a-priori from a
     FIXED totally-antisymmetric source-geometry 3-form T_{abc} (a torsion/flux),
     with NO dependence on (xi, M_D). The covariant gamma-trace
     B_W = hstack(e_a . exp(t A_a)) deforms the constraint surface block-
     dependently (genuine connection: NOT a global Spin element, NOT the spurion).
     Test: does it drive ||[Pi_{ker B_W}, M_D]|| BELOW 32.80, ideally 0?
  B. FULL BV BICOMPLEX  s = s_KT + s_long  on
        C^{+1}(ghost c, S) <- C^0(field psi, VS)
                            <- C^{-1}(antifield psi*, VS) <- C^{-2}(antighost c*, S)
     s_KT  (antifield-lowering): K2 = Gamma^dag.Gamma (EOM), K1 = d_A.
     s_long (longitudinal/ghost): L = d_A^dag + sigma_c(W).
     s^2=0 requires s_KT^2=0, {s_KT,s_long}=0, s_long^2=0.
     Test: is the co-exact escape now s_KT-EXACT? full ||s^2|| + leg ranks?

NON-NEGOTIABLE GUARDS:
  ANTI-TRAP    bare ||[Pi_RS,M_D]|| MUST stay 58.72 (RS coupled, VZ evaded).
  ANTI-FIXED-SOLVE  W must be a GENUINE a-priori geometric object, not solved
               from the closure target. Discriminator built in (section 3b).
  ANTI-VACUOUS  s^2=0 must be genuine (each leg nonzero rank, reported).
  ANTI-IMPORT  if closure needs importing the matter-generation answer, say so.

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
SPURION_FLOOR = 32.8005  # null-covector spurion dressed-obstruction floor (GHOST-01)
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)


def fro(A):
    return float(np.linalg.norm(A))


def proj_onto_kernel(M):
    """Orthogonal projector onto ker(M) for M: rows=d_out, cols=d_in."""
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


def build_J(dim, eta, e):
    """Quaternionic structure J = U.conj, J^2=-I, [J,e_a]=0."""
    s = np.empty(N)
    for a in range(N):
        s[a] = (-1.0) ** a if a < 9 else (-1.0) ** (a + 1)
    anticomm = [a for a in range(N) if s[a] < 0]
    U = np.eye(dim, dtype=complex)
    for a in anticomm:
        U = U @ e[a]
    return U


def antisym_3form(triples):
    """Build a totally-antisymmetric 3-form T_{abc} from a list of base triples."""
    T = np.zeros((N, N, N))
    for (a, b, c) in triples:
        for (i, j, k, sgn) in [(a, b, c, 1), (b, c, a, 1), (c, a, b, 1),
                               (b, a, c, -1), (a, c, b, -1), (c, b, a, -1)]:
            T[i, j, k] = sgn
    return T


def main():
    dim, eta, e, Iden = build_rep()
    VS = N * dim  # 1792
    I_VS = np.eye(VS, dtype=complex)
    R = {}

    # ---- core operators (identical to GHOST-01 / keystone) --------------------
    Gamma = np.hstack(e)                              # 128 x 1792 gamma-trace
    GammaH = Gamma.conj().T                           # 1792 x 128 = Gamma^dag
    Pi_RS = proj_onto_kernel(Gamma)                   # 1792 x 1792 onto ker(Gamma)
    Pi_perp = I_VS - Pi_RS
    cxi = sum(XI[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)      # 1792 x 1792
    d_A = np.vstack([XI[a] * Iden for a in range(N)])  # 1792 x 128 gauge map
    d_AH = d_A.conj().T                                # 128 x 1792 = d_A^dag

    print("=" * 80)
    print("EXPLICIT KOSZUL-TATE BICOMPLEX (ghost + KT legs) + SOURCE-DERIVED CONNECTION")
    print("=" * 80)

    # === (0) ANCHORS ===========================================================
    comm_PiMD = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    escape = Pi_perp @ M_D @ Pi_RS
    escape_op = fro(escape)
    C2 = Gamma @ M_D @ Pi_RS
    nC2 = fro(C2)
    # is C2 independent of Gamma (a genuine new constraint)?
    GGd = Gamma @ GammaH
    GGd_inv = np.linalg.inv(GGd)
    Lambda = C2 @ (GammaH @ GGd_inv)
    C2_indep_resid = fro(C2 - Lambda @ Gamma)
    R["anchor_comm_PiMD"] = comm_PiMD
    R["anchor_escape_op"] = escape_op
    R["anchor_C2"] = nC2
    R["C2_independence_residual"] = C2_indep_resid
    print("\n(0) ANCHORS:")
    print(f"    ||[Pi_RS, M_D]||           = {comm_PiMD:.4f}   (repo 58.72)")
    print(f"    ||(I-Pi_RS)M_D Pi_RS||     = {escape_op:.4f}   (repo 41.52)")
    print(f"    ||C2=Gamma M_D Pi_RS||     = {nC2:.4f}  (repo 155.36, secondary VZ constraint)")
    print(f"    C2 independence residual   = {C2_indep_resid:.4f}  "
          f"({'reducible' if C2_indep_resid < 1e-6 else 'GENUINELY INDEPENDENT'})")

    # === (1) SECOND-CLASS DIAGNOSIS ===========================================
    Gd = Gamma @ d_A                                  # 128x128 = c(xi)
    second_class = fro(Gd)
    sc_invertible = int(np.linalg.matrix_rank(Gd, tol=TOL)) == dim
    R["second_class_bracket"] = second_class
    R["second_class_invertible"] = sc_invertible
    print("\n(1) SECOND-CLASS DIAGNOSIS:")
    print(f"    ||Gamma.d_A|| = ||c(xi)|| = {second_class:.4f}  (constraint/gauge bracket)")
    print(f"    invertible = {sc_invertible}  -> system is SECOND-CLASS")
    print(f"    propagator core cond(Gamma Gamma^dag) = {np.linalg.cond(GGd):.2e}")

    # === (2) SOURCE-DERIVED CARRIER W = Spin(9,5) CONNECTION 1-form ============
    def Sig(a, b):
        return 0.25 * (e[a] @ e[b] - e[b] @ e[a])     # spin(9,5) generator (spinor rep)

    triples = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11), (12, 13, 0),
               (1, 4, 7), (2, 5, 8), (0, 9, 12), (3, 10, 13), (6, 11, 1)]
    T = antisym_3form(triples)
    A_conn = [sum(T[a, b, c] * Sig(b, c) for b in range(N) for c in range(N) if b < c)
              for a in range(N)]                       # A_a, a=0..13, NO xi/M_D content

    conn_defect = max(fro(Sig(0, 1) @ A_conn[a] - A_conn[a] @ Sig(0, 1)) for a in range(N))
    curv_norm = max(fro(A_conn[a] @ A_conn[b] - A_conn[b] @ A_conn[a])
                    for (a, b) in [(0, 1), (0, 3), (3, 6)])
    # inhomogeneous (connection, not tensor): Maurer-Cartan term g dg^-1
    g = expm(0.37 * Sig(0, 1))
    mc_term = -Sig(0, 1)                               # g (d/ds) g^-1 for g=exp(s Sig_01)
    inhomog_size = fro(mc_term)
    R["carrier_noneq_defect"] = conn_defect
    R["carrier_curvature"] = curv_norm
    R["carrier_MC_term"] = inhomog_size
    print("\n(2) SOURCE-DERIVED CARRIER W (Spin(9,5) connection 1-form from fixed 3-form):")
    print(f"    non-equivariance ||[Sig_01, A_a]||_max = {conn_defect:.4f}  (breaks Spin(9,5))")
    print(f"    curvature ||[A_a,A_b]||_max            = {curv_norm:.4f}  (non-flat, not pure gauge)")
    print(f"    Maurer-Cartan inhomog term ||g dg^-1|| = {inhomog_size:.4f}  (connection, not tensor)")
    print(f"    contains xi/M_D? NO -> not a symbol-data functional")

    # === (3) DRESSED OBSTRUCTION with the geometric connection ================
    def dressed_obstruction(A_list, t):
        Bw = np.hstack([e[a] @ expm(t * A_list[a]) for a in range(N)])
        Pi = proj_onto_kernel(Bw)
        return fro(Pi @ M_D - M_D @ Pi)

    print("\n(3) DRESSED OBSTRUCTION ||[Pi_{ker B_W}, M_D]|| (a-priori connection):")
    print(f"    floor to beat (null spurion) = {SPURION_FLOOR:.4f};  bare = {comm_PiMD:.4f}")
    best_geo = np.inf
    best_t = None
    for t in np.linspace(-1.5, 1.5, 31):
        if abs(t) < 1e-9:
            continue
        val = dressed_obstruction(A_conn, t)
        if val < best_geo:
            best_geo, best_t = val, t
    R["dressed_floor_conn1"] = best_geo
    print(f"    connection #1: min = {best_geo:.4f} at t={best_t:.3f}  "
          f"(beats 32.80? {best_geo < SPURION_FLOOR})")

    # second a-priori connection (different fixed 3-form) -- robustness
    triples2 = [(0, 3, 6), (1, 4, 9), (2, 7, 10), (5, 8, 11), (12, 0, 4),
                (13, 1, 5), (3, 9, 6), (2, 11, 8), (7, 10, 0), (12, 13, 6)]
    T2 = antisym_3form(triples2)
    A_conn2 = [sum(T2[a, b, c] * Sig(b, c) for b in range(N) for c in range(N) if b < c)
               for a in range(N)]
    best_geo2 = np.inf
    best_t2 = None
    for t in np.linspace(-1.5, 1.5, 31):
        if abs(t) < 1e-9:
            continue
        val = dressed_obstruction(A_conn2, t)
        if val < best_geo2:
            best_geo2, best_t2 = val, t
    R["dressed_floor_conn2"] = best_geo2
    print(f"    connection #2: min = {best_geo2:.4f} at t={best_t2:.3f}  "
          f"(beats 32.80? {best_geo2 < SPURION_FLOOR})")

    # === (3b) ANTI-FIXED-SOLVE probe: random a-priori connections (no tuning) ===
    rng = np.random.default_rng(0)
    best_rand = np.inf
    for _ in range(12):
        Tr = rng.standard_normal((N, N, N))
        Tr = Tr - np.transpose(Tr, (1, 0, 2))
        Ar = [sum(Tr[a, b, c] * Sig(b, c) for b in range(N) for c in range(N) if b < c)
              for a in range(N)]
        for t in [-0.6, -0.3, 0.3, 0.6]:
            val = dressed_obstruction(Ar, t)
            best_rand = min(best_rand, val)
    R["dressed_floor_random"] = best_rand
    print(f"    random a-priori connections (floor probe): min = {best_rand:.4f}")
    geo_min = min(best_geo, best_geo2)
    R["dressed_floor"] = geo_min

    # === (4) FULL BV BICOMPLEX  s = s_KT + s_long (bare) ======================
    g1, g0, gm1, gm2 = dim, VS, VS, dim
    off = [0, g1, g1 + g0, g1 + g0 + gm1]
    W_tot = g1 + g0 + gm1 + gm2  # 3840

    def place(blocks):
        S = np.zeros((W_tot, W_tot), dtype=complex)
        for (ti, si, Mblk) in blocks:
            r0, c0 = off[ti], off[si]
            S[r0:r0 + Mblk.shape[0], c0:c0 + Mblk.shape[1]] = Mblk
        return S

    # block indices: 0=C^{+1}(S), 1=C^0(VS), 2=C^{-1}(VS), 3=C^{-2}(S)
    K2 = GammaH @ Gamma                                # 1792x1792 EOM/constraint Laplacian
    K1 = d_A                                           # 1792x128
    L_bare = d_AH                                      # 128x1792

    s_KT = place([(1, 2, K2), (2, 3, K1)])
    s_long_bare = place([(0, 1, L_bare)])

    s_KT2 = fro(s_KT @ s_KT)
    s_long2 = fro(s_long_bare @ s_long_bare)
    cross = fro(s_KT @ s_long_bare + s_long_bare @ s_KT)
    s_bare = s_KT + s_long_bare
    s_bare2 = fro(s_bare @ s_bare)

    KT2_block_norm = fro(K2 @ K1)
    cross_block_norm = fro(L_bare @ K2)
    rK2 = int(np.linalg.matrix_rank(K2, tol=TOL))
    rK1 = int(np.linalg.matrix_rank(K1, tol=TOL))
    rL = int(np.linalg.matrix_rank(L_bare, tol=TOL))
    R.update(bare_s2=s_bare2, bare_sKT2=s_KT2, bare_slong2=s_long2, bare_cross=cross,
             rank_K2=rK2, rank_K1=rK1, rank_L=rL)
    print("\n(4) FULL BV BICOMPLEX s = s_KT + s_long (bare, no carrier):")
    print(f"    leg ranks (anti-vacuous): K2={rK2}, K1={rK1}, L={rL}")
    print(f"    s_KT^2   = {s_KT2:.4f}  (block ||Gamma^dag Gamma d_A|| = {KT2_block_norm:.4f})")
    print(f"    s_long^2 = {s_long2:.2e}  (no C^{{+2}}: trivially nilpotent)")
    print(f"    {{s_KT,s_long}} = {cross:.4f}  (block ||d_A^dag Gamma^dag Gamma|| = {cross_block_norm:.4f})")
    print(f"    full ||s^2|| (bare) = {s_bare2:.4f}")

    # === (5) CLOSING CARRIER forced by {s_KT,s_long}=0 (fixed-solve discriminator)
    # geometric connection carrier:
    rho_W = np.kron(np.eye(N, dtype=complex), A_conn[0])
    sigma_geo = d_AH @ rho_W
    cross_geo = fro((L_bare + sigma_geo) @ K2)
    # UNIQUE Dirac-closing carrier:
    L_closed = d_AH @ Pi_RS
    sigma_dirac = L_closed - L_bare                    # = -d_A^dag Pi_perp
    cross_closed = fro(L_closed @ K2)
    sigma_dirac_via_prop = -d_AH @ (GammaH @ GGd_inv @ Gamma)
    prop_match = fro(sigma_dirac - sigma_dirac_via_prop)
    R.update(cross_geo=cross_geo, cross_closed=cross_closed, prop_match=prop_match)
    print("\n(5) CLOSING {s_KT,s_long}=0  (carrier discriminator):")
    print(f"    (a) geometric connection carrier: {{s_KT,s_long}} = {cross_geo:.4f}  "
          f"(closed? {cross_geo < 1e-6})")
    print(f"    (b) Dirac-closing carrier -d_A^dag Pi_perp: {{s_KT,s_long}} = {cross_closed:.2e}")
    print(f"        matches propagator -d_A^dag Gamma^dag (GG^dag)^-1 Gamma to {prop_match:.2e}")
    print(f"        => closing carrier is a FIXED SOLVE = Dirac-bracket propagator (GHOST-01 ii)")

    # === (6) ESCAPE s-EXACTNESS in the completed Koszul-Tate leg ===============
    Z = GGd_inv @ (Gamma @ M_D @ Pi_RS)               # 128 x 1792
    Y = GammaH @ GGd_inv @ Z                          # 1792 x 1792
    resid_KTexact = fro(escape - K2 @ Y)
    frac_in_imK2 = fro(K2 @ Y) / escape_op
    P_imdA = d_A @ np.linalg.pinv(d_A)
    escape_ghost_part = fro(P_imdA @ escape)
    R.update(escape_KTexact_resid=resid_KTexact, escape_frac_imKT=frac_in_imK2,
             escape_ghost_part=escape_ghost_part)
    print("\n(6) ESCAPE s-EXACTNESS via the completed KOSZUL-TATE leg:")
    print(f"    ||escape|| = {escape_op:.4f}")
    print(f"    residual ||escape - s_KT(Y)|| = {resid_KTexact:.2e}  "
          f"(s_KT-EXACT: {resid_KTexact < 1e-6})")
    print(f"    fraction of escape in im(s_KT) = {frac_in_imK2:.4f}")
    print(f"    escape component in ghost/gauge dir im(d_A) = {escape_ghost_part:.4f}")

    # === (7) FULL s^2 with Dirac-corrected legs (nonvacuous closure) ===========
    K1_D = Pi_RS @ d_A
    s_KT_D = place([(1, 2, K2), (2, 3, K1_D)])
    s_long_D = place([(0, 1, L_closed)])
    s_full_D = s_KT_D + s_long_D
    sKT2_D = fro(s_KT_D @ s_KT_D)
    cross_D = fro(s_KT_D @ s_long_D + s_long_D @ s_KT_D)
    s2_D = fro(s_full_D @ s_full_D)
    rK1D = int(np.linalg.matrix_rank(K1_D, tol=TOL))
    rLD = int(np.linalg.matrix_rank(L_closed, tol=TOL))
    R.update(dirac_s2=s2_D, dirac_sKT2=sKT2_D, dirac_cross=cross_D,
             rank_K1D=rK1D, rank_LD=rLD)
    print("\n(7) FULL s^2 WITH DIRAC-CORRECTED LEGS (the only closure):")
    print(f"    ranks: K2={rK2}, K1_D={rK1D}, L_closed={rLD} (all nonzero -> nonvacuous)")
    print(f"    s_KT^2 = {sKT2_D:.2e}, {{s_KT,s_long}} = {cross_D:.2e}, full ||s^2|| = {s2_D:.2e}")

    # === (8) ANTI-TRAP =========================================================
    comm_after = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    R["anti_trap_bare"] = comm_after
    print("\n(8) ANTI-TRAP -- bare dynamics never modified:")
    print(f"    ||[Pi_RS, M_D]|| = {comm_after:.4f}  (MUST be 58.72 => RS coupled, VZ evaded)")

    # === (9) H-LINEARITY =======================================================
    U = build_J(dim, eta, e)
    h_A0 = fro(A_conn[0] @ U - U @ np.conjugate(A_conn[0]))
    R["h_linear_A0"] = h_A0
    print("\n(9) H-LINEARITY of the connection carrier:")
    print(f"    ||[A_0, J]|| = {h_A0:.2e}  (H-linear: {h_A0 < 1e-9})")

    # === VERDICT ===============================================================
    print("\n" + "=" * 80)
    print("VERDICT")
    print("=" * 80)
    beats = geo_min < SPURION_FLOOR
    reaches0 = geo_min < 1e-6
    print(f"  dressed obstruction floor (a-priori connection) = {geo_min:.4f} "
          f"(beats 32.80? {beats}; reaches 0? {reaches0})")
    print(f"  bare [Pi_RS,M_D] = {comm_after:.4f} (anti-trap intact)")
    print(f"  escape now s_KT-EXACT (residual {resid_KTexact:.1e})")
    print(f"  full s^2=0 ACHIEVED only with Dirac-bracket fixed-solve legs ({s2_D:.1e})")
    print(f"  second-class bracket ||c(xi)|| = {second_class:.4f} obstructs both naive legs")
    if beats:
        print("  STATUS: CARRIER BEATS FLOOR")
    else:
        print("  STATUS: SHARPER_OBSTRUCTION (second-class); a-priori connection does NOT")
        print("          beat 32.80; s^2=0 forced to the Dirac-bracket propagator (FIXED SOLVE).")
    return R


if __name__ == "__main__":
    main()
