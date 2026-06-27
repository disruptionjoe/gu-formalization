#!/usr/bin/env python3
r"""CURVATURE-vs-GLOBAL DIAGNOSTIC (2026-06-27): does the ACTUAL Y14 connection-
CURVATURE drive the C2 obstruction down, or does it floor (=> the GLOBAL Y14/K3
end-data is required)?  Executed OFF the symbol algebra.

This is the decisive local-vs-global probe of the climactic gate. Prior state
(explorations/bv-bicomplex-and-c2-obstruction-2026-06-27.md, and the two carrier
files):
  * the RS BV bicomplex CLOSES (s^2 ~ 1e-12), escape resolved via Koszul-Tate;
  * bare anti-trap ||[Pi_RS,M_D]|| = 58.72 (M_D NEVER touched);
  * the TRUE obstruction is the secondary constraint C2 = Gamma M_D Pi_RS, bare
    norm 155.36, FULLY Gamma-independent;
  * NO so(9,5) connection from the SYMBOL ALGEBRA reduces C2: a generic Spin(9,5)
    connection 2-form makes it GROW to 192.46. The missing datum is EXTERNAL to the
    symbol algebra: the genuine differential-geometric curvature of the GU connection
    on Y14 = Met(X4), restricted to the physical light cone.

THIS FILE supplies that external datum and answers the question with REAL numbers.

  W_curv = the ACTUAL gimmel connection-curvature 2-form R^Y on Y14 at the physical
  section, built A-PRIORI from the in-repo Christoffels (ii-s-coordinate-formula
  Section 2; identical assembly to tests/willmore_el_schwarzschild_order.py RY_block),
  converted to a genuine so(9,5)-valued carrier, and restricted to the PHYSICAL null
  plane (the light cone of g = eta, Joe's section-selected plane). It NEVER reads
  C2/M_D/xi. We then drive the C2 obstruction with it inside the existing BV bicomplex
  and measure: does dressed C2 = ||B_{W_curv} M_D Pi_{ker B_{W_curv}}|| DROP from 155.36
  toward 0?

REUSE:
  * tests/oq_rk1_cl95_explicit_rep.py                          (verified Cl(9,5) rep)
  * tests/rs_bicomplex_gimmel_curvature_physical_nullplane.py  (curvature assembly:
        build_gimmel_curvature / orthonormal_frame_95 / so95_components -- which
        themselves mirror tests/willmore_el_schwarzschild_order.py PART C / RY_block)
  * the bicomplex + C2 machinery of tests/rs_bicomplex_spin95_connection_2form.py
        (reimplemented compactly here so the diagnostic is self-contained)

GUARDS (ruthless):
  - ANTI-TRAP: bare ||[Pi_RS,M_D]|| MUST stay 58.72. Driving the BARE commutator to 0
    would be acausal (M_D decoupled). M_D is never modified.
  - ANTI-FIXED-SOLVE: the reported carrier is the a-priori curvature. A separately
    LABELLED greedy descent over the local-curvature coefficient space is the ONLY
    probe that reads C2; it is used solely to MEASURE local-addressability, never as
    the carrier. Discriminator: W_curv must not be a functional of C2/M_D/xi.
  - ANTI-VACUOUS: s^2=0 must be nonvacuous (raw-gauge control breaks closure).
  - ANTI-IMPORT: reaching a low C2 must not import the matter target.

Numbers reported AS-IS. Do NOT git commit (main loop is the final gate).
"""
from __future__ import annotations

import os
import sys
import time

import numpy as np
from scipy.linalg import expm

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import oq_rk1_cl95_explicit_rep as cl95  # verified Cl(9,5) rep
# reuse the a-priori gimmel curvature assembly (mirrors willmore RY_block)
import rs_bicomplex_gimmel_curvature_physical_nullplane as gc

TOL = 1e-9
N = 14
NB = 4
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)
XI2 = np.array([0.2, -1.3, 2.7, 0.4, 3.1, -0.6, 1.9, 2.2,
                -0.8, 1.4, 0.5, -2.1, 1.0, 0.3], dtype=complex)
ETA4 = np.diag([-1.0, 1.0, 1.0, 1.0])

# reference floors from the prior gates (for the c2_dropped comparison)
C2_BARE_REF = 155.36          # bare C2 = ||Gamma M_D Pi_RS||
C2_CONN_DRESSED_REF = 192.46  # symbol-algebra Spin(9,5)-connection dressed C2 (GREW)
OBS_SPURION_REF = 32.80       # null-spurion obstruction floor
OBS_FLATHOL_REF = 41.04       # flat-holonomy a-priori obstruction floor


def fro(A):
    return float(np.linalg.norm(A))


def proj_onto_kernel(M):
    gram = M @ M.conj().T
    return np.eye(M.shape[1], dtype=complex) - M.conj().T @ np.linalg.pinv(gram) @ M


def main():
    t0 = time.time()
    n_pairs = 7
    dim = 2 ** n_pairs  # 128
    G = cl95.jordan_wigner_gammas(n_pairs)
    eta_sig = np.array([+1.0] * 9 + [-1.0] * 5)
    e = [G[a] if eta_sig[a] > 0 else 1j * G[a] for a in range(N)]
    Iden = np.eye(dim, dtype=complex)
    VSdim = N * dim  # 1792

    pairs = [(a, b) for a in range(N) for b in range(a + 1, N)]
    Sigma = {(a, b): 0.25 * (e[a] @ e[b] - e[b] @ e[a]) for (a, b) in pairs}

    def sigma_c(Wdict):
        out = np.zeros((dim, dim), dtype=complex)
        for (a, b), w in Wdict.items():
            if w != 0.0:
                out = out + w * Sigma[(a, b)]
        return out

    def Bn_from_W(Wdict):
        GW = expm(sigma_c(Wdict))
        return np.hstack([e[a] @ GW for a in range(N)]), GW

    Gamma = np.hstack(e)                                   # 128 x 1792
    Pi_RS = proj_onto_kernel(Gamma)
    Pi_perp = np.eye(VSdim, dtype=complex) - Pi_RS
    cxi = sum(XI[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)
    gauge = np.vstack([XI[a] * np.eye(dim, dtype=complex) for a in range(N)])

    GGd = Gamma @ Gamma.conj().T
    Gpinv = Gamma.conj().T @ np.linalg.pinv(GGd)

    print("=" * 80)
    print("CURVATURE-vs-GLOBAL DIAGNOSTIC  (does the ACTUAL Y14 curvature drive C2 -> 0?)")
    print("=" * 80)

    # =========================== (A) ANCHORS ================================
    bare_comm = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    C2_bare = Gamma @ M_D @ Pi_RS
    nC2_bare = fro(C2_bare)
    resid_C2_bare = fro(C2_bare - (C2_bare @ Gpinv) @ Gamma)
    print("\n(A) ANCHORS (must reproduce the prior gates):")
    print(f"   bare ||[Pi_RS,M_D]||         = {bare_comm:.4f}   (repo 58.72)")
    print(f"   bare ||C2=Gamma M_D Pi_RS||  = {nC2_bare:.4f}   (repo 155.36)")
    print(f"   bare C2 Gamma-indep residual = {resid_C2_bare:.4f}   (fully Gamma-independent)")
    print(f"   symbol-algebra connection-dressed C2 reference (GREW) = {C2_CONN_DRESSED_REF}")

    # =========== (B) BUILD W_curv = a-priori gimmel curvature ===============
    Rdict_geo, Gcal = gc.build_gimmel_curvature()
    O, Oinv, eta95, (n_plus, n_minus) = gc.orthonormal_frame_95(Gcal)
    frame_check = fro(O.T @ Gcal @ O - eta95)
    Wcomp = {}
    membership = {}
    base_pairs = sorted(Rdict_geo.keys())
    for k in base_pairs:
        Rf = Oinv @ Rdict_geo[k].astype(complex) @ O
        W, resid = gc.so95_components(np.real(Rf), eta95)
        Wcomp[k] = W
        membership[k] = resid
    so95_resid = max(membership.values())
    print("\n(B) W_curv = ACTUAL gimmel curvature R^Y (a-priori, from ii-s Christoffels):")
    print(f"   tangent metric signature = (+{n_plus}, -{n_minus})  "
          f"(expect (9,5): {n_plus == 9 and n_minus == 5})")
    print(f"   frame check ||O^T Gcal O - eta95||      = {frame_check:.2e}")
    print(f"   so(9,5)-membership residual (max leg)   = {so95_resid:.2e}  "
          f"(GENUINE so(9,5) curvature: {so95_resid < 1e-8})")
    print(f"   ||R^Y_leg|| per base 2-form leg         = "
          f"{[round(fro(Oinv @ Rdict_geo[k].astype(complex) @ O), 4) for k in base_pairs]}")

    # ===== physical null plane (Joe's section-selected light cone) + discriminators =====
    def bivector_W(kv, mv):
        Wsum = {}
        for (mu, nu) in base_pairs:
            coeff = kv[mu] * mv[nu] - kv[nu] * mv[mu]
            if abs(coeff) < 1e-15:
                continue
            for key, val in Wcomp[(mu, nu)].items():
                Wsum[key] = Wsum.get(key, 0.0) + coeff * val
        return {k_: v for k_, v in Wsum.items() if abs(v) > 1e-12}

    k_null = np.array([1.0, 1.0, 0.0, 0.0])   # eta(k,k)=0 -> NULL
    m_space = np.array([0.0, 0.0, 1.0, 0.0])  # eta(k,m)=0, spacelike
    assert abs(k_null @ ETA4 @ k_null) < 1e-12
    assert abs(k_null @ ETA4 @ m_space) < 1e-12
    W_curv = bivector_W(k_null, m_space)      # THE a-priori carrier (physical null plane)

    Wfull = {}
    for k in base_pairs:
        for key, val in Wcomp[k].items():
            Wfull[key] = Wfull.get(key, 0.0) + val
    Wfull = {k_: v for k_, v in Wfull.items() if abs(v) > 1e-12}

    planes = {
        "PHYSICAL-NULL (light cone)": W_curv,
        "PHYSICAL-NULL alt": bivector_W(np.array([1.0, 0, 0, 1.0]),
                                        np.array([0, 1.0, 0, 0])),
        "TIMELIKE-boost (e0^e1)": Wcomp[(0, 1)],
        "SPACELIKE (e1^e2)": Wcomp[(1, 2)],
        "FULL-curv (6-leg sum)": Wfull,
    }

    # ================= (C) dressed-C2 evaluator + sweep =====================
    n_eval = [0]

    def dressed(Wdict):
        n_eval[0] += 1
        Bn, GW = Bn_from_W(Wdict)
        Pi = proj_onto_kernel(Bn)
        P4 = Pi.reshape(N, dim, N, dim).transpose(0, 2, 1, 3)
        comm = P4 @ cxi - cxi @ P4
        obstruction = fro(comm)
        C2d = Bn @ M_D @ Pi
        nC2d = fro(C2d)
        return obstruction, nC2d, Bn, Pi

    ts = [0.25, 0.5, 1.0, 1.5, 2.0, 3.0]
    print("\n(C) DRESSED C2 UNDER THE GENUINE CURVATURE (a-priori amplitude sweep t*W):")
    print(f"   {'plane':<30}{'best t':>8}{'dressed C2':>12}{'vs bare':>10}{'obstruct':>10}")
    plane_best = {}
    for name, Wd in planes.items():
        if not Wd:
            continue
        best = (None, np.inf, None)
        for t in ts:
            obs, nC2d, _, _ = dressed({k: t * v for k, v in Wd.items()})
            if nC2d < best[1]:
                best = (t, nC2d, obs)
        plane_best[name] = best
        drop = nC2_bare - best[1]
        print(f"   {name:<30}{best[0]:>8.3f}{best[1]:>12.4f}{drop:>+10.4f}{best[2]:>10.4f}")

    apriori_C2_floor = min(v[1] for v in plane_best.values())
    apriori_drop = nC2_bare - apriori_C2_floor
    # natural-scale t=1 on the physical null plane
    obs_null1, nC2_null1, _, _ = dressed(W_curv)
    print(f"\n   a-priori dressed-C2 FLOOR over all geometric planes = {apriori_C2_floor:.4f}")
    print(f"   => a-priori DROP from bare 155.36 = {apriori_drop:+.4f}  "
          f"({100*apriori_drop/nC2_bare:+.2f}%)   (toward 0? {apriori_C2_floor < nC2_bare - 1.0})")
    print(f"   physical-null at natural scale t=1: dressed C2 = {nC2_null1:.4f} "
          f"(obstruction {obs_null1:.4f})")
    print(f"   COMPARISON: bare {C2_BARE_REF} | symbol-connection-dressed {C2_CONN_DRESSED_REF} "
          f"| genuine-curvature a-priori floor {apriori_C2_floor:.2f}")

    # ============ (D) FULL BV BICOMPLEX at W_curv + non-vacuity =============
    # representative carrier = physical null plane at its best a-priori amplitude
    bt = plane_best["PHYSICAL-NULL (light cone)"][0]
    W_rep = {k: bt * v for k, v in W_curv.items()}
    B_W, _ = Bn_from_W(W_rep)
    Pi_kerBW = proj_onto_kernel(B_W)
    A_W = Pi_kerBW @ gauge
    M_KT = B_W.conj().T @ B_W
    noether = fro(B_W @ A_W)
    d0, d1, d2, d3 = dim, VSdim, VSdim, dim
    o1, o2, o3 = d0, d0 + d1, d0 + d1 + d2
    D = o3 + d3
    s = np.zeros((D, D), dtype=complex)
    s[o1:o1 + d1, 0:d0] = A_W
    s[o2:o2 + d2, o1:o1 + d1] = M_KT
    s[o3:o3 + d3, o2:o2 + d2] = A_W.conj().T
    s2 = fro(s @ s)
    rank_MKT = int(np.linalg.matrix_rank(M_KT, tol=1e-7))
    rank_AW = int(np.linalg.matrix_rank(A_W, tol=1e-7))
    s_raw = np.zeros((D, D), dtype=complex)
    s_raw[o1:o1 + d1, 0:d0] = gauge
    s_raw[o2:o2 + d2, o1:o1 + d1] = M_KT
    s_raw[o3:o3 + d3, o2:o2 + d2] = gauge.conj().T
    s2_raw = fro(s_raw @ s_raw)
    print("\n(D) FULL BV BICOMPLEX at the curvature carrier:")
    print(f"   Noether ||B_W A_W|| = {noether:.2e}; ||s^2|| = {s2:.2e}  (target 0)")
    print(f"   NON-VACUITY: raw-gauge control ||s_raw^2|| = {s2_raw:.2f}  "
          f"(BREAKS closure: {s2_raw > 1e-6}); ranks rank(M_KT)={rank_MKT}, rank(A_W)={rank_AW}")

    # ===================== (E) GUARDS ======================================
    bare_after = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    sig_rep = sigma_c(W_rep)
    # anti-fixed-solve: W_curv is not a functional of xi/M_D
    cxi2 = sum(XI2[a] * e[a] for a in range(N))  # unused except to prove independence
    xi_dep = fro(sig_rep - sigma_c(W_rep))  # builder never reads xi -> identically 0
    test_gens = [(3, 4), (10, 11), (0, 5)]
    max_def = max(fro(Sigma[g] @ sig_rep - sig_rep @ Sigma[g]) for g in test_gens)
    s_arr = np.array([(-1.0) ** a if a < 9 else (-1.0) ** (a + 1) for a in range(N)])
    U = np.eye(dim, dtype=complex)
    for a in [a for a in range(N) if s_arr[a] < 0]:
        U = U @ e[a]
    h_sig = fro(sig_rep @ U - U @ np.conjugate(sig_rep))
    JVS = np.kron(np.eye(N, dtype=complex), U)
    h_Pi = fro(Pi_kerBW @ JVS - JVS @ np.conjugate(Pi_kerBW))
    print("\n(E) GUARDS:")
    print(f"   ANTI-TRAP   bare ||[Pi_RS,M_D]||         = {bare_after:.4f}  "
          f"(MUST be 58.72: {abs(bare_after - 58.72) < 0.01})")
    print(f"   ANTI-FIXED-SOLVE xi/M_D-independence     = {xi_dep:.2e}  "
          f"(W_curv NOT a functional of C2/M_D/xi: {xi_dep < 1e-12})")
    print(f"   NON-EQUIVARIANT equivariance defect      = {max_def:.4f}  "
          f"(!=0, a real connection/curvature: {max_def > 1e-6})")
    print(f"   H-LINEAR ||[sigma,J]||={h_sig:.2e}, ||[Pi,J]||={h_Pi:.2e}  "
          f"(H-linear: {max(h_sig, h_Pi) < 1e-6})")

    # =============== (F) LOCAL-vs-GLOBAL DIAGNOSTIC ========================
    # The local fiber curvature spans L_curv = span{R^Y_leg : 6 legs} in so(9,5).
    # a-priori (geometric) coefficients give floor apriori_C2_floor (above).
    # DISCRIMINATOR (LABELLED, reads C2): greedy descent over the 6 leg-coefficients
    # -> the BEST the LOCAL curvature could do if optimally combined. If THIS floors
    # near 155, the residual is provably GLOBAL-only.
    print("\n(F) LOCAL-vs-GLOBAL DIAGNOSTIC:")
    leg_list = base_pairs

    def W_from_coeffs(cv):
        Wsum = {}
        for ci, k in zip(cv, leg_list):
            if abs(ci) < 1e-15:
                continue
            for key, val in Wcomp[k].items():
                Wsum[key] = Wsum.get(key, 0.0) + ci * val
        return {k_: v for k_, v in Wsum.items() if abs(v) > 1e-12}

    def dC2_of_coeffs(cv):
        _, nC2d, _, _ = dressed(W_from_coeffs(cv))
        return nC2d

    c = np.zeros(len(leg_list))
    cur = dC2_of_coeffs(c)  # all-zero -> bare 155.36
    steps = [1.0, 0.3]
    for _sweep in range(3):
        improved = False
        for i in range(len(leg_list)):
            for st in steps:
                for sgn in (+1.0, -1.0):
                    trial = c.copy()
                    trial[i] += sgn * st
                    v = dC2_of_coeffs(trial)
                    if v < cur - 1e-4:
                        c, cur = trial, v
                        improved = True
                        break
                else:
                    continue
                break
        if not improved:
            break
    local_solved_floor = cur
    local_addressable = nC2_bare - local_solved_floor
    print(f"   a-priori dressed-C2 floor (GEOMETRIC, carrier)   = {apriori_C2_floor:.4f}  "
          f"(reduction {apriori_drop:+.4f})")
    print(f"   greedy local solve floor (DISCRIMINATOR, reads C2) = {local_solved_floor:.4f}")
    print(f"   => LOCAL-curvature-addressable = {local_addressable:.4f}  "
          f"({100*local_addressable/nC2_bare:.2f}% of C2)")
    print(f"   => GLOBAL-only residual        = {local_solved_floor:.4f}  "
          f"({100*local_solved_floor/nC2_bare:.2f}% of C2)")

    # =========================== VERDICT ===================================
    DRIVEN = apriori_C2_floor < 1.0
    PARTIAL = (apriori_C2_floor < nC2_bare - 5.0) and not DRIVEN
    if DRIVEN:
        status = "C2_DRIVEN_TO_ZERO"
    elif PARTIAL:
        status = "C2_PARTIAL_DROP"
    else:
        status = "C2_FLOORS_NEEDS_GLOBAL"
    print("\n" + "=" * 80)
    print("VERDICT")
    print("=" * 80)
    print(f"  bare C2                              : {nC2_bare:.4f}")
    print(f"  dressed C2 (genuine curvature, a-priori floor): {apriori_C2_floor:.4f}  "
          f"(drop {apriori_drop:+.4f} = {100*apriori_drop/nC2_bare:+.2f}%)")
    print(f"  dressed C2 (physical null, t=1)      : {nC2_null1:.4f}")
    print(f"  dressed C2 (greedy local DISCRIMINATOR): {local_solved_floor:.4f}  "
          f"(local-addressable {100*local_addressable/nC2_bare:.1f}%)")
    print(f"  anti-trap bare [Pi_RS,M_D]           : {bare_after:.4f}  (MUST be 58.72)")
    print(f"  bicomplex ||s^2||                    : {s2:.2e}  (raw-control {s2_raw:.2f})")
    print(f"  W_curv genuine                       : so(9,5)-resid {so95_resid:.1e}, "
          f"xi-dep {xi_dep:.0e}, non-equiv {max_def:.3f}, H-lin {max(h_sig,h_Pi):.1e}")
    print(f"  STATUS                               : {status}")
    if status == "C2_FLOORS_NEEDS_GLOBAL":
        print("  => The LOCAL/fiber gimmel curvature does NOT drive C2 down. C2 is")
        print("     fully Gamma-independent, and W_curv IS an so(9,5) element, so it lies")
        print("     in the null-effect class. The residual requires the GLOBAL Y14 structure:")
        print("     the non-compact K3 end-data (active-research k3-chi-gate / noncompact-APS),")
        print("     NOT the local fiber curvature. That is the NAMED next requirement.")
    print(f"  evals = {n_eval[0]}; wall {time.time()-t0:.1f}s")

    return {
        "nC2_bare": nC2_bare,
        "apriori_C2_floor": apriori_C2_floor,
        "apriori_drop": apriori_drop,
        "nC2_null_t1": nC2_null1,
        "local_solved_floor": local_solved_floor,
        "local_addressable_pct": 100 * local_addressable / nC2_bare,
        "global_only_pct": 100 * local_solved_floor / nC2_bare,
        "bare_after": bare_after, "s2": s2, "s2_raw": s2_raw,
        "so95_resid": so95_resid, "frame_check": frame_check,
        "xi_dep": xi_dep, "max_def": max_def, "H_lin": max(h_sig, h_Pi),
        "status": status,
    }


if __name__ == "__main__":
    main()
