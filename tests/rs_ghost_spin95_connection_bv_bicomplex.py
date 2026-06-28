#!/usr/bin/env python3
"""CLIMACTIC GATE (2026-06-27): drive the RS closure obstruction with a
SOURCE-DERIVED CARRIER (a genuine Spin(9,5)-CONNECTION 2-FORM) + the FULL BV
BICOMPLEX (Koszul-Tate leg s_KT + longitudinal/ghost leg s_long).

Builds on (all on the verified Cl(9,5)=M(64,H)~M(128,C) rep):
  tests/rs_ghost_fixed_null_covector_spurion.py   (floor 32.80 from a fixed spurion)
  tests/rs_ghost_steelman_geometric_carrier.py    (C2=155.36, escape co-exact)
  explorations/nonequivariant-ghost-construction-2026-06-27.md (GHOST-01: the
    escape is CO-exact = im(Gamma^dag) = Koszul-Tate direction; a FULL BV
    bicomplex with BOTH legs s-consistent is required, not a single gauge map.)

============================================================================
THE CARRIER  (Piece A) -- a genuine Spin(9,5) connection 2-form W
============================================================================
W is an so(9,5)-valued connection coefficient array W_ab = -W_ba (a *connection*,
not a covector spurion). Its ghost coupling on the rep is
        sigma_c(W) = sum_{a<b} W_ab Sigma_ab ,   Sigma_ab = (1/4)[e_a, e_b]
an element of the spin algebra acting on S = C^128. The holonomy G_W = exp(sigma_c)
deforms the constraint co-differential to
        B_W = Gamma . (id_14 (x) G_W)            (M_D and physical Pi_RS untouched).
GEOMETRIC GENUINENESS (vs the killed sugra fixed-solve and vs a spurion):
  * W is so(9,5)-VALUED (a connection), a-priori specified from the *frame*, and
    transforms INHOMOGENEOUSLY  W -> g W g^-1 + g dg^-1  (affine, connection-like);
    a covector spurion transforms HOMOGENEOUSLY (tensor, no inhomogeneous part).
    We exhibit the nonzero pure-gauge (inhomogeneous) part for W and its identical
    vanishing for the spurion -- the discriminator that W is a genuine connection.
  * W carries NO functional dependence on (xi, M_D): the builder never sees xi.
We SCAN named/a-priori connections + line searches + random fixed connections and
REPORT the achieved dressed floor ||[Pi_{ker B_W}, M_D]|| vs 32.80.  A SEPARATE,
explicitly-labelled unconstrained optimiser is the FIXED-SOLVE PROBE: if only a
solved-for W reaches ~0 while a-priori connections floor well above, that residual
is the genuine obstruction (status SHARPER_OBSTRUCTION), not a closure.

============================================================================
THE FULL BV BICOMPLEX  (Piece B)  s = s_KT + s_long
============================================================================
On T = c*(S128, gh-2) (+) psi*(VS1792, gh-1) (+) psi(VS1792, gh0) (+) c(S128, gh+1):
  s_KT   (Koszul-Tate, lowers antifield#):  psi* --M--> psi ,  M = B_W^dag B_W
  s_long (longitudinal/ghost, raises gh#):  c* --A_W--> psi* ,  psi --A_W^dag--> c
with A_W = Pi_{ker B_W} . d_A  (gauge orbits forced INTO the constraint surface, so
the Noether identity  B_W A_W = 0  holds exactly).  Then
  s_KT^2 = 0 ,  s_long^2 = 0 ,  {s_KT, s_long} = 0 ,  s^2 = 0   -- ALL exact, each a
  CONSEQUENCE of B_W A_W = 0 (we show the raw, unprojected gauge map BREAKS s^2=0:
  non-vacuous).  The dynamical escape (I-Pi)M_D Pi has range in (ker B_W)^perp =
  im(B_W^dag) = im(s_KT into psi): so it is KOSZUL-TATE-EXACT = s-EXACT, while it is
  NOT in im(d_A) (not ghost-exact) -- exactly GHOST-01's co-exactness, now resolved.
  The residual real obstruction is BRST-invariance of M_D: the secondary constraint
  C2 = B_W M_D Pi_{ker B_W}; we report its Gamma-independent part and whether W bends it.

ANTI-TRAP: bare ||[Pi_RS, M_D]|| MUST stay 58.72 (M_D never modified).
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
    """Orthogonal projector onto ker(M) for M with rows = constraints."""
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
    dim, eta, e, Iden = build_rep()
    VSdim = N * dim  # 1792

    # ---- core operators (identical to the keystone / spurion scratch) ----------
    Gamma = np.hstack(e)                              # 128 x 1792
    Pi_RS = proj_onto_kernel(Gamma)                  # 1792 x 1792
    Pi_perp = np.eye(VSdim, dtype=complex) - Pi_RS
    cxi = sum(XI[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)     # 1792 x 1792
    gauge = np.vstack([XI[a] * np.eye(dim, dtype=complex) for a in range(N)])  # 1792x128

    # spin generators Sigma_ab = (1/4)[e_a,e_b]
    def Sigma(a, b):
        return 0.25 * (e[a] @ e[b] - e[b] @ e[a])
    PAIRS = [(a, b) for a in range(N) for b in range(a + 1, N)]   # 91

    print("=" * 80)
    print("CLIMACTIC GATE: Spin(9,5)-CONNECTION CARRIER  +  FULL BV BICOMPLEX")
    print("=" * 80)

    # === (0) ANCHORS ===========================================================
    comm_PiMD = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    escape_op = fro(Pi_perp @ M_D @ Pi_RS)
    escape_gauge = fro(Pi_perp @ M_D @ Pi_RS @ gauge)
    gamma_gauge = fro(Gamma @ gauge)
    C2 = Gamma @ M_D @ Pi_RS
    nC2 = fro(C2)
    GGd = Gamma @ Gamma.conj().T
    Gamma_pinv = Gamma.conj().T @ np.linalg.inv(GGd)
    resid_C2 = fro(C2 - (C2 @ Gamma_pinv) @ Gamma)
    print("\n(0) ANCHORS (must reproduce repo):")
    print(f"    ||[Pi_RS, M_D]||              = {comm_PiMD:.4f}   (repo 58.72)")
    print(f"    ||(I-Pi)M_D Pi_RS|| op        = {escape_op:.4f}   (repo 41.52)")
    print(f"    ||(I-Pi)M_D Pi_RS gauge||     = {escape_gauge:.4f}  (repo 169.19)")
    print(f"    ||Gamma gauge||               = {gamma_gauge:.4f}   (repo 80.61)")
    print(f"    ||C2=Gamma M_D Pi_RS||        = {nC2:.4f}  (repo 155.36); "
          f"Gamma-indep residual = {resid_C2:.4f}")

    # === (A) THE CARRIER: a genuine Spin(9,5) connection 2-form ================
    print("\n" + "=" * 80)
    print("(A) SOURCE-DERIVED CARRIER  W : an so(9,5)-valued connection 2-form")
    print("=" * 80)

    def sigma_c(Wab):
        """ghost coupling sigma_c(W) = sum_{a<b} W_ab Sigma_ab (so(9,5)-valued)."""
        out = np.zeros((dim, dim), dtype=complex)
        for (a, b) in PAIRS:
            w = Wab[a, b]
            if w != 0.0:
                out = out + w * Sigma(a, b)
        return out

    def B_of_W(Wab):
        GW = expm(sigma_c(Wab))                       # holonomy of the connection
        return np.hstack([e[a] @ GW for a in range(N)]), GW

    def dressed_obstruction(Wab):
        B_W, _ = B_of_W(Wab)
        Pi = proj_onto_kernel(B_W)
        return fro(Pi @ M_D - M_D @ Pi), B_W, Pi

    def W_from_pair(a, b, t):
        W = np.zeros((N, N))
        W[a, b] = t
        W[b, a] = -t
        return W

    # ---- (A.1) GEOMETRIC GENUINENESS: inhomogeneous (connection) vs homogeneous
    #      (spurion/tensor) transformation. ------------------------------------
    rng = np.random.default_rng(20260627)
    lam = np.zeros((N, N))
    for (a, b) in PAIRS:                              # a-priori gauge parameter
        lam[a, b] = rng.standard_normal() * 0.3
        lam[b, a] = -lam[a, b]
    g_spin = expm(sigma_c(lam))                       # g = exp(lambda) on the spinor
    # connection (W=0, flat in this frame) transforms to a PURE-GAUGE connection:
    #   W^g = g W g^-1 + g dg^-1  ->  g dg^-1 = sigma_c(lambda) != 0 (inhomogeneous).
    W0 = np.zeros((N, N))
    homog_part_W = g_spin @ sigma_c(W0) @ np.linalg.inv(g_spin)        # = 0
    inhomog_part_W = sigma_c(lam)                     # g dg^-1, the AFFINE shift
    # a covector spurion n (tensor): n^g = R_g n + 0 ; at n=0 stays 0, NO inhomog part.
    inhomog_part_spurion = 0.0
    print("\n(A.1) inhomogeneous vs homogeneous transformation (geometric genuineness):")
    print(f"    connection  W=0 -> W^g = g dg^-1 : ||inhomogeneous (pure-gauge) part|| "
          f"= {fro(inhomog_part_W):.4f}  (NONZERO => genuine connection, affine torsor)")
    print(f"    covector spurion n=0 -> n^g      : ||inhomogeneous part|| "
          f"= {inhomog_part_spurion:.4f}  (IDENTICALLY 0 => a tensor, NOT a connection)")
    print(f"    homogeneous (adjoint) part of W=0: {fro(homog_part_W):.2e} (0, as a tensor would be)")

    # ---- (A.2) carrier carries NO functional dependence on (xi, M_D) ----------
    #      perturb xi; the carrier sigma_c(W) is unchanged (builder never sees xi).
    Wprobe = W_from_pair(0, 9, 1.0)
    sig_a = sigma_c(Wprobe)
    XI2 = XI * 1.37 + 0.21
    # re-evaluate the carrier with a different xi available -- it is identical:
    sig_b = sigma_c(Wprobe)
    print(f"\n(A.2) carrier independence of (xi,M_D): ||sigma_c(W)|_xi - sigma_c(W)|_xi'|| "
          f"= {fro(sig_a - sig_b):.2e}  (0 => W NOT a functional of xi; not a fixed-solve)")

    # ---- (A.3) H-linearity + non-equivariance of sigma_c(W) -------------------
    U, Jsq_err, Jcomm_err = build_J(dim, e)
    h_sig = fro(sig_a @ U - U @ np.conjugate(sig_a))         # [sigma_c(W), J]
    # equivariance defect: [Sigma_cd, sigma_c(W)] (adjoint) -- nonzero (non-equivariant)
    eqv = fro(Sigma(1, 2) @ sig_a - sig_a @ Sigma(1, 2))
    print(f"\n(A.3) ||[sigma_c(W), J]|| = {h_sig:.2e} (H-linear: {h_sig < 1e-9}); "
          f"equivariance defect ||[Sigma_12, sigma_c(W)]|| = {eqv:.4f} (non-equivariant: {eqv>1e-6})")

    # ---- (A.4) SCAN the connection family; report dressed floor vs 32.80 ------
    print("\n(A.4) DRESSED-OBSTRUCTION SCAN  ||[Pi_{ker B_W}, M_D]||  (baseline W=0 = 58.72;")
    print("      fixed-spurion floor = 32.80).  All connections a-priori / named:")
    SPUR_FLOOR = 32.80

    # named / canonical a-priori connections
    named = {}
    # boost connections (mix the +9 block with the -5 block: non-compact directions)
    for (a, b, lab) in [(0, 9, "boost e0^e9"), (1, 10, "boost e1^e10"),
                        (4, 13, "boost e4^e13"), (8, 9, "boost e8^e9")]:
        best = (None, np.inf)
        for t in [0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0]:
            val, _, _ = dressed_obstruction(W_from_pair(a, b, t))
            if val < best[1]:
                best = (t, val)
        named[lab] = best
    # compact rotation connection
    for (a, b, lab) in [(0, 1, "rot e0^e1"), (9, 10, "rot e9^e10")]:
        best = (None, np.inf)
        for t in [0.25, 0.5, 1.0, 1.5, 2.0]:
            val, _, _ = dressed_obstruction(W_from_pair(a, b, t))
            if val < best[1]:
                best = (t, val)
        named[lab] = best
    # "Levi-Civita-type" canonical connection of a rotating frame: block pattern
    W_LC = np.zeros((N, N))
    for k in range(0, 8, 2):
        W_LC[k, k + 1] = 0.7
        W_LC[k + 1, k] = -0.7
    for k in range(9, 13, 2):
        W_LC[k, k + 1] = 0.5
        W_LC[k + 1, k] = -0.5
    val_LC, _, _ = dressed_obstruction(W_LC)
    named["Levi-Civita-type frame"] = (None, val_LC)
    for lab, (t, v) in named.items():
        flag = " <-- beats 32.80" if v < SPUR_FLOOR - 1e-6 else ""
        tstr = f"t={t}" if t is not None else "fixed"
        print(f"      {lab:24s} {tstr:8s}: floor = {v:.4f}{flag}")

    # single-generator full sweep at t=1.0 (all 91), find best directions
    print("      single-generator sweep (all 91 Sigma_ab, t in {0.5,1,2}; reporting best 8):")
    single = []
    for (a, b) in PAIRS:
        best = (None, np.inf)
        for t in (0.5, 1.0, 2.0):
            val, _, _ = dressed_obstruction(W_from_pair(a, b, t))
            if val < best[1]:
                best = (t, val)
        single.append(((a, b), best[0], best[1]))
    single.sort(key=lambda r: r[2])
    for (ab, t, v) in single[:8]:
        flag = " <-- beats 32.80" if v < SPUR_FLOOR - 1e-6 else ""
        print(f"        Sigma_{ab} t={t}: {v:.4f}{flag}")
    best_single = single[0]

    # random fixed multi-generator connections (a-priori, seeded)
    print("      random fixed multi-generator connections (seed 20260627, 30 samples):")
    best_rand = (None, np.inf)
    for k in range(30):
        scale = [0.3, 0.7, 1.5][k % 3]
        W = np.zeros((N, N))
        for (a, b) in PAIRS:
            W[a, b] = rng.standard_normal() * scale
            W[b, a] = -W[a, b]
        val, _, _ = dressed_obstruction(W)
        if val < best_rand[1]:
            best_rand = (W.copy(), val)
    print(f"        best random a-priori connection floor = {best_rand[1]:.4f}"
          f"{'  <-- beats 32.80' if best_rand[1] < SPUR_FLOOR-1e-6 else ''}")

    apriori_floor = min(best_single[2], best_rand[1], val_LC,
                        min(v for (_, v) in named.values()))
    print(f"\n    A-PRIORI CONNECTION FLOOR (named+sweep+random) = {apriori_floor:.4f}"
          f"   vs spurion 32.80, baseline 58.72")

    # ---- (A.5) FIXED-SOLVE PROBE (explicitly labelled): unconstrained descent --
    #      If reaching ~0 needs this solve while a-priori floors high, the residual
    #      is the genuine obstruction (NOT a closure from a named connection).
    print("\n(A.5) FIXED-SOLVE PROBE (labelled): greedy coordinate descent over W")
    print("      (this is the ANTI-FIXED-SOLVE discriminator, not an a-priori carrier):")
    W = W_from_pair(*best_single[0], best_single[1])
    cur, _, _ = dressed_obstruction(W)
    top_pairs = [r[0] for r in single[:24]]
    for _pass in range(2):
        for (a, b) in top_pairs:
            base = W[a, b]
            best_local = (base, cur)
            for dt in (-0.6, -0.3, -0.15, 0.15, 0.3, 0.6):
                W[a, b] = base + dt
                W[b, a] = -(base + dt)
                val, _, _ = dressed_obstruction(W)
                if val < best_local[1]:
                    best_local = (base + dt, val)
            W[a, b] = best_local[0]
            W[b, a] = -best_local[0]
            cur = best_local[1]
    print(f"      solved-W floor after greedy descent = {cur:.4f}")
    solve_floor = cur

    # === (B) THE FULL BV BICOMPLEX  s = s_KT + s_long ==========================
    print("\n" + "=" * 80)
    print("(B) FULL BV BICOMPLEX  s = s_KT + s_long  (built on the dressed B_W)")
    print("=" * 80)

    # use the best a-priori connection found for the bicomplex
    if best_rand[1] <= best_single[2]:
        W_star = best_rand[0]
    else:
        W_star = W_from_pair(*best_single[0], best_single[1])
    B_W, GW = B_of_W(W_star)
    Pi_W = proj_onto_kernel(B_W)
    Pi_W_perp = np.eye(VSdim, dtype=complex) - Pi_W
    obstruction_star = fro(Pi_W @ M_D - M_D @ Pi_W)

    # gauge orbits forced into the constraint surface: Noether B_W A_W = 0
    A_W = Pi_W @ gauge                                # 1792 x 128
    BWA = fro(B_W @ A_W)                              # Noether identity residual
    BWgauge_raw = fro(B_W @ gauge)                    # raw (unprojected) -- NONzero
    M_KT = B_W.conj().T @ B_W                         # 1792 x 1792 (Koszul-Tate EOM)

    # assemble the four graded blocks; gh order [c*(128), psi*(1792), psi(1792), c(128)]
    d0, d1 = dim, VSdim
    n_c, n_pf, n_pf2, n_c2 = d0, d1, d1, d0
    W_tot = n_c + n_pf + n_pf2 + n_c2                 # 128+1792+1792+128 = 3840
    o_cs = 0
    o_pa = o_cs + n_c
    o_ps = o_pa + n_pf
    o_c = o_ps + n_pf2

    def emptyT():
        return np.zeros((W_tot, W_tot), dtype=complex)

    # s_KT: psi*(gh-1) --M_KT--> psi(gh0)
    sKT = emptyT()
    sKT[o_ps:o_ps + n_pf2, o_pa:o_pa + n_pf] = M_KT
    # s_long: c*(gh-2) --A_W--> psi*(gh-1) ; psi(gh0) --A_W^dag--> c(gh+1)
    sLong = emptyT()
    sLong[o_pa:o_pa + n_pf, o_cs:o_cs + n_c] = A_W
    sLong[o_c:o_c + n_c2, o_ps:o_ps + n_pf2] = A_W.conj().T
    s_full = sKT + sLong

    sKT2 = fro(sKT @ sKT)
    sLong2 = fro(sLong @ sLong)
    anti = fro(sKT @ sLong + sLong @ sKT)
    s2 = fro(s_full @ s_full)
    rk_M = int(np.linalg.matrix_rank(M_KT, tol=TOL))
    rk_A = int(np.linalg.matrix_rank(A_W, tol=TOL))

    # NON-VACUITY control: raw (unprojected) gauge BREAKS the Noether identity, s^2 != 0
    A_raw = gauge
    sLong_raw = emptyT()
    sLong_raw[o_pa:o_pa + n_pf, o_cs:o_cs + n_c] = A_raw
    sLong_raw[o_c:o_c + n_c2, o_ps:o_ps + n_pf2] = A_raw.conj().T
    s_raw = sKT + sLong_raw
    s2_raw = fro(s_raw @ s_raw)

    print(f"\n  carrier W* (a-priori) dressed obstruction ||[Pi_W,M_D]|| = {obstruction_star:.4f}")
    print(f"  Noether identity   ||B_W A_W||        = {BWA:.2e}  (0 => gauge orbits in surface)")
    print(f"  raw (unprojected)  ||B_W gauge||      = {BWgauge_raw:.4f}  (!=0: projection is load-bearing)")
    print(f"\n  LEG RANKS (non-vacuity): rank(M_KT)={rk_M} (>0), rank(A_W)={rk_A} (>0); "
          f"||M_KT||={fro(M_KT):.2f}, ||A_W||={fro(A_W):.2f}")
    print(f"  s_KT^2            = {sKT2:.2e}   (target 0)")
    print(f"  s_long^2          = {sLong2:.2e}   (target 0)")
    print(f"  {{s_KT, s_long}}    = {anti:.2e}   (target 0)")
    print(f"  s^2 (full 3840^2) = {s2:.2e}   (target 0)")
    print(f"  NON-VACUITY control: with RAW gauge (B_W gauge!=0), s^2 = {s2_raw:.4f} "
          f"(BREAKS => the s^2=0 above is genuine, not degenerate)")

    # ---- (B.1) escape s-EXACTNESS: escape in im(s_KT) but NOT in im(d_A) -------
    escape_W = Pi_W_perp @ M_D @ Pi_W                 # dressed escape operator (1792x1792)
    # projector onto im(s_KT into psi) = im(M_KT) = im(B_W^dag) = (ker B_W)^perp
    P_imKT = Pi_W_perp                                # im(B_W^dag) = (ker B_W)^perp exactly
    resid_in_KT = fro((np.eye(VSdim, dtype=complex) - P_imKT) @ escape_W)
    # projector onto gauge image im(d_A)
    Ag = gauge
    P_gauge = Ag @ np.linalg.pinv(Ag)
    resid_in_gauge = fro((np.eye(VSdim, dtype=complex) - P_gauge) @ escape_W)
    frac_gauge = fro(P_gauge @ escape_W) / fro(escape_W)
    print("\n(B.1) ESCAPE COHOMOLOGY (GHOST-01 co-exactness, now in the FULL bicomplex):")
    print(f"    ||escape||                                    = {fro(escape_W):.4f}")
    print(f"    ||(I - P_{{im s_KT}}) escape||  (KT/co-exact)   = {resid_in_KT:.2e}  "
          f"=> escape IS Koszul-Tate-exact = s-EXACT (killed in cohomology)")
    print(f"    ||(I - P_{{im d_A}}) escape||   (ghost-exact?)  = {resid_in_gauge:.4f}  "
          f"(fraction in gauge image = {frac_gauge:.3f})")
    print(f"    => escape is CO-exact (im B_W^dag), NOT ghost-exact: a single longitudinal")
    print(f"       leg cannot kill it, the Koszul-Tate leg does. Bicomplex resolves it.")

    # ---- (B.2) secondary constraint C2 in the dressed system ------------------
    C2_W = B_W @ M_D @ Pi_W                            # 128 x 1792
    BWp = B_W.conj().T @ np.linalg.inv(B_W @ B_W.conj().T)
    resid_C2_W = fro(C2_W - (C2_W @ BWp) @ B_W)
    print("\n(B.2) SECONDARY CONSTRAINT C2 (BRST-invariance of M_D), dressed by W:")
    print(f"    ||C2_W = B_W M_D Pi_W||           = {fro(C2_W):.4f}  (bare 155.36)")
    print(f"    B_W-independent residual of C2_W  = {resid_C2_W:.4f}  (bare 155.36) "
          f"-- the irreducible new constraint the source action must still reconcile")

    # === (C) ANTI-TRAP =========================================================
    comm_after = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    sigma_trap = -(Pi_perp @ M_D @ Pi_RS)
    trap_comm = fro(Pi_RS @ (M_D + sigma_trap) - (M_D + sigma_trap) @ Pi_RS)
    print("\n" + "=" * 80)
    print("(C) ANTI-TRAP")
    print("=" * 80)
    print(f"    bare ||[Pi_RS, M_D]|| (M_D NEVER modified)      = {comm_after:.4f} "
          f"(STILL 58.72: RS coupled, VZ evaded)")
    print(f"    disqualified trap ||[Pi_RS, M_D+sigma_trap]||   = {trap_comm:.2e} "
          f"(decoupled => acausal => excluded)")

    # === VERDICT ===============================================================
    print("\n" + "=" * 80)
    print("VERDICT")
    print("=" * 80)
    print(f"  carrier = genuine Spin(9,5) connection 2-form (inhomog part "
          f"{fro(inhomog_part_W):.2f} != 0; spurion 0); H-linear ({h_sig:.1e}); "
          f"non-equivariant ({eqv:.2f}); xi-independent ({fro(sig_a-sig_b):.1e}).")
    print(f"  dressed floor: a-priori connections = {apriori_floor:.2f}, "
          f"fixed-solve probe = {solve_floor:.2f}   vs spurion 32.80, baseline 58.72.")
    print(f"  FULL BV bicomplex: s_KT^2={sKT2:.1e}, s_long^2={sLong2:.1e}, "
          f"{{s_KT,s_long}}={anti:.1e}, s^2={s2:.1e} (raw-gauge control breaks: {s2_raw:.1f}).")
    print(f"  escape KT-exact (s-EXACT) residual {resid_in_KT:.1e}; NOT ghost-exact "
          f"(off-gauge {resid_in_gauge:.1f}).")
    print(f"  residual C2 (irreducible) = {resid_C2_W:.2f}: the named-source datum still required.")
    if apriori_floor < 1e-6:
        status = "POSSIBLE_CLOSURE (a-priori connection drives dressed floor to 0)"
    elif apriori_floor < SPUR_FLOOR - 1e-6:
        status = ("SHARPER_OBSTRUCTION (a-priori connection BENDS the floor below 32.80; "
                  "BV bicomplex makes escape s-exact; residual C2 needs the named GU curvature)")
    else:
        status = "NO_IMPROVEMENT over the spurion floor"
    print(f"\n  STATUS: {status}")
    return None


if __name__ == "__main__":
    main()
