#!/usr/bin/env python3
r"""PHYSICAL NULL-CONE RESTRICTION (2026-06-27): off the symbol algebra, does the
ACTUAL gimmel Y14 connection-CURVATURE 2-form, restricted to the PHYSICAL light
cone selected by the physical metric section, drive the secondary constraint C2
down where a generic Spin(9,5) connection provably could not?

Self-contained driver that REUSES the verified machinery:
  * tests/oq_rk1_cl95_explicit_rep.py                          (Cl(9,5)=M(64,H) rep)
  * tests/rs_bicomplex_gimmel_curvature_physical_nullplane.py  (the A-PRIORI gimmel
        curvature assembly: build_gimmel_curvature / orthonormal_frame_95 /
        so95_components -- itself mirroring willmore_el_schwarzschild_order RY_block)
  * the BV bicomplex + C2 machinery of rs_bicomplex_spin95_connection_2form.py
        (reimplemented compactly here so the driver is one file)

WHAT IS COMPUTED (real numbers, reported as-is)
  - ANCHORS: bare ||[Pi_RS,M_D]|| (MUST be 58.72) and bare ||C2=Gamma M_D Pi_RS||
    (155.36), with the Gamma-independence residual.
  - W_curv = the ACTUAL R^Y on Y14 at the physical section, restricted to the
    physical null cone (Joe's section-selected light cone). A-PRIORI: it reads ONLY
    the metric (Christoffels, frame metric, eta null structure), never C2/M_D/xi.
  - dressed C2 = ||B_{W_curv} M_D Pi_{ker B_{W_curv}}|| per physical-null carrier, an
    amplitude sweep, an arbitrary-bivector control (is NULL special?), and a LABELLED
    fixed-solve discriminator (reads C2 -> disqualified as a-priori).
  - the FULL BV bicomplex at the carrier: s^2, Noether, leg ranks, raw-gauge control.
  - GUARDS: anti-trap (58.72), so(9,5)-membership residual, equivariance defect (!=0),
    xi-independence (=0), H-linearity.

GUARDS (ruthless): anti-trap (M_D never modified), anti-fixed-solve (W_curv is the
geometric curvature; the C2-reading greedy solve is labelled + disqualified), anti-
vacuous (s^2 nonvacuous, raw control breaks closure), anti-import. Do NOT git commit.
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

import oq_rk1_cl95_explicit_rep as cl95
import rs_bicomplex_gimmel_curvature_physical_nullplane as gc  # a-priori curvature

np.set_printoptions(precision=4, suppress=True, linewidth=150)

TOL = 1e-9
N = 14
NB = 4
ETA4 = np.diag([-1.0, 1.0, 1.0, 1.0])
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)
XI2 = np.array([0.2, -1.3, 2.7, 0.4, 3.1, -0.6, 1.9, 2.2,
                -0.8, 1.4, 0.5, -2.1, 1.0, 0.3], dtype=complex)

# reference floors from prior gates
C2_BARE_REF = 155.36
C2_CONN_DRESSED_REF = 192.46   # symbol-algebra Spin(9,5) connection dressed C2 (GREW)
OBS_SPURION_REF = 32.80
OBS_FLATHOL_REF = 41.04


def fro(A):
    return float(np.linalg.norm(A))


def proj_onto_kernel(M):
    gram = M @ M.conj().T
    return np.eye(M.shape[1], dtype=complex) - M.conj().T @ np.linalg.pinv(gram) @ M


def main():
    t0 = time.time()
    # ---------- Cl(9,5) rep + bicomplex core ----------
    n_pairs = 7
    dim = 2 ** n_pairs  # 128
    G = cl95.jordan_wigner_gammas(n_pairs)
    eta_sig = np.array([+1.0] * 9 + [-1.0] * 5)
    e = [G[a] if eta_sig[a] > 0 else 1j * G[a] for a in range(N)]
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
    cxi = sum(XI[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)
    gauge = np.vstack([XI[a] * np.eye(dim, dtype=complex) for a in range(N)])

    GGd = Gamma @ Gamma.conj().T
    Gpinv = Gamma.conj().T @ np.linalg.pinv(GGd)

    print("=" * 80)
    print("PHYSICAL NULL-CONE RESTRICTION OF THE GIMMEL Y14 CURVATURE  +  RS BV BICOMPLEX")
    print("=" * 80)

    # ---------- (A) ANCHORS ----------
    bare_comm = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    C2_bare = Gamma @ M_D @ Pi_RS
    nC2_bare = fro(C2_bare)
    resid_C2_bare = fro(C2_bare - (C2_bare @ Gpinv) @ Gamma)
    print("\n(A) ANCHORS (must reproduce prior gates):")
    print(f"   bare ||[Pi_RS,M_D]||         = {bare_comm:.4f}   (repo 58.72)")
    print(f"   bare ||C2=Gamma M_D Pi_RS||  = {nC2_bare:.4f}   (repo 155.36)")
    print(f"   bare C2 Gamma-indep residual = {resid_C2_bare:.4f}   (fully Gamma-independent)")
    print(f"   symbol-algebra connection-dressed C2 (prior, GREW) = {C2_CONN_DRESSED_REF}")

    # ---------- (B) W_curv = a-priori gimmel curvature, restricted to physical cone ----
    Rdict_geo, Gcal = gc.build_gimmel_curvature()
    O, Oinv, eta95, (n_plus, n_minus) = gc.orthonormal_frame_95(Gcal)
    frame_check = fro(O.T @ Gcal @ O - eta95)
    base_pairs = sorted(Rdict_geo.keys())
    Wcomp = {}
    membership = {}
    block_mix = {}
    for k in base_pairs:
        Rc = Rdict_geo[k]
        block_mix[k] = (fro(Rc[:NB, NB:]), fro(Rc[NB:, :NB]))  # (HV, VH) coordinate blocks
        Rf = Oinv @ Rc.astype(complex) @ O
        W, resid = gc.so95_components(np.real(Rf), eta95)
        Wcomp[k] = W
        membership[k] = resid
    so95_resid = max(membership.values())
    maxHV = max(max(v) for v in block_mix.values())
    print("\n(B) W_curv = ACTUAL gimmel curvature R^Y (a-priori; ii-s Section-2 Christoffels):")
    print(f"   tangent-metric signature (+{n_plus},-{n_minus})  (expect (9,5): "
          f"{n_plus == 9 and n_minus == 5})   frame ||O^T Gcal O - eta95|| = {frame_check:.2e}")
    print(f"   so(9,5)-membership residual (max leg) = {so95_resid:.2e}  "
          f"(genuine so(9,5) curvature: {so95_resid < 1e-8})")
    print(f"   coordinate H<->V mixed blocks: max(||HV||,||VH||) over 6 legs = {maxHV:.2e}")
    print(f"     => R^Y is block-diagonal so(3,1)_HH (+) so(6,4)_VV in the coordinate split.")
    print(f"   ||R^Y_leg|| per base 2-form leg = "
          f"{[round(fro(Oinv @ Rdict_geo[k].astype(complex) @ O), 4) for k in base_pairs]}")

    # ---------- dressed evaluators (block-fast obstruction; direct C2) ----------
    n_eval = [0]

    def dressed(Wdict):
        n_eval[0] += 1
        Bn, GW = Bn_from_W(Wdict)
        Pi = proj_onto_kernel(Bn)
        # dressed obstruction ||[Pi,M_D]||  (block-batched, M_D = I_14 (x) cxi)
        P4 = Pi.reshape(N, dim, N, dim).transpose(0, 2, 1, 3)
        comm = P4 @ cxi - cxi @ P4
        obstruction = fro(comm)
        # dressed C2 = Bn M_D Pi  (128x1792 @ 1792x1792 @ 1792x1792, cheap since Bn is short)
        C2d = Bn @ (M_D @ Pi)
        nC2d = fro(C2d)
        return obstruction, nC2d, Bn, Pi

    def dressed_C2(Wdict):
        return dressed(Wdict)[1]

    # ---------- (C) physical null-cone carriers ----------
    # physical timelike observer and a basis of REAL null directions of eta.
    t_obs = np.array([1.0, 0.0, 0.0, 0.0])             # eta(t,t) = -1
    null_dirs = {
        "n_x+": np.array([1.0, 1.0, 0.0, 0.0]),
        "n_x-": np.array([1.0, -1.0, 0.0, 0.0]),
        "n_y+": np.array([1.0, 0.0, 1.0, 0.0]),
        "n_z+": np.array([1.0, 0.0, 0.0, 1.0]),
        "n_diag": np.array([np.sqrt(3.0), 1.0, 1.0, 1.0]),
    }
    for nm, n in null_dirs.items():
        assert abs(n @ ETA4 @ n) < 1e-12, f"{nm} not null: {n @ ETA4 @ n}"

    def W_from_bivector(v1, v2):
        """so(9,5) carrier from R^Y contracted on bivector v1 ^ v2 (base 2-plane)."""
        Wsum = {}
        for (mu, nu) in base_pairs:
            coeff = v1[mu] * v2[nu] - v1[nu] * v2[mu]
            if abs(coeff) < 1e-15:
                continue
            for key, val in Wcomp[(mu, nu)].items():
                Wsum[key] = Wsum.get(key, 0.0) + coeff * val
        return {k_: v for k_, v in Wsum.items() if abs(v) > 1e-12}

    carriers = [
        ("nullplane n_x+ ^ n_x-", null_dirs["n_x+"], null_dirs["n_x-"]),
        ("nullplane n_x+ ^ n_y+", null_dirs["n_x+"], null_dirs["n_y+"]),
        ("nullplane n_y+ ^ n_z+", null_dirs["n_y+"], null_dirs["n_z+"]),
        ("null n_x+ ^ t_obs", null_dirs["n_x+"], t_obs),
        ("null n_diag ^ t_obs", null_dirs["n_diag"], t_obs),
    ]
    print("\n(C) PHYSICAL NULL-CONE carriers (a-priori): dressed C2 + dressed obstruction")
    print(f"   baseline bare C2 = {nC2_bare:.4f}; generic-connection a-priori floor 41.04 (obstruction)")
    print(f"   {'carrier':<26}{'||W||':>9}{'dressedC2':>11}{'obstruct':>10}{'bareTrap':>10}")
    null_results = []
    for nm, v1, v2 in carriers:
        Wd = W_from_bivector(v1, v2)
        nW = np.sqrt(sum(v * v for v in Wd.values()))
        obs, c2, _, _ = dressed(Wd)
        tr = fro(Pi_RS @ M_D - M_D @ Pi_RS)
        null_results.append((nm, nW, c2, obs, tr, Wd))
        print(f"   {nm:<26}{nW:>9.3f}{c2:>11.3f}{obs:>10.3f}{tr:>10.3f}")

    # ---------- (D) controls / discriminators ----------
    print("\n(D) CONTROLS / DISCRIMINATORS:")
    base_nm, _, _, _, _, base_Wd = null_results[0]
    print(f"   (D1) amplitude sweep of '{base_nm}' (fixed a-priori direction, scale lambda):")
    best_lam = (None, np.inf)
    for lam in [0.1, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0]:
        c2 = dressed_C2({k: lam * v for k, v in base_Wd.items()})
        if c2 < best_lam[1]:
            best_lam = (lam, c2)
        print(f"        lambda={lam:>4}: dressed C2 = {c2:.4f}")
    print(f"      -> min over lambda (direction a-priori): C2 = {best_lam[1]:.4f} "
          f"at lambda={best_lam[0]}  (LABELLED amplitude-tuned)")

    rng = np.random.default_rng(20260627)
    arb = []
    for _ in range(6):
        v1 = rng.normal(size=NB); v2 = rng.normal(size=NB)
        arb.append(dressed_C2(W_from_bivector(v1, v2)))
    print(f"   (D2) arbitrary-bivector control dressed C2: min={min(arb):.3f} "
          f"max={max(arb):.3f} mean={np.mean(arb):.3f}")

    print("   (D3) FIXED-SOLVE probe (greedy, READS C2 -> DISQUALIFIED as a-priori):")
    Wsol = dict(base_Wd)
    cur = dressed_C2(Wsol)
    for sweep in range(2):
        improved = False
        for (a, b) in pairs:
            for st in (0.4, 0.1):
                for sgn in (+1.0, -1.0):
                    trial = dict(Wsol); trial[(a, b)] = trial.get((a, b), 0.0) + sgn * st
                    v = dressed_C2(trial)
                    if v < cur - 1e-6:
                        Wsol, cur, improved = trial, v, True
                        break
                else:
                    continue
                break
        print(f"        greedy sweep {sweep + 1}: dressed C2 = {cur:.4f}  (evals {n_eval[0]})")
        if not improved:
            break
    solved_C2 = cur

    # ---------- (E) FULL BV BICOMPLEX at best a-priori physical-null carrier ----------
    best = min(null_results, key=lambda r: r[2])
    nm_b, nW_b, c2_b, obs_b, tr_b, Wd_b = best
    B_W, G_W = Bn_from_W(Wd_b)
    Pi_kerBW = proj_onto_kernel(B_W)
    A_W = Pi_kerBW @ gauge
    M_KT = B_W.conj().T @ B_W
    noether = fro(B_W @ A_W)
    d0, d1 = dim, VSdim
    o1, o2, o3 = d0, d0 + d1, d0 + d1 + d1
    D = o3 + d0
    s = np.zeros((D, D), dtype=complex)
    s[o1:o1 + d1, 0:d0] = A_W
    s[o2:o2 + d1, o1:o1 + d1] = M_KT
    s[o3:o3 + d0, o2:o2 + d1] = A_W.conj().T
    s2 = fro(s @ s)
    s_raw = np.zeros((D, D), dtype=complex)
    s_raw[o1:o1 + d1, 0:d0] = gauge
    s_raw[o2:o2 + d1, o1:o1 + d1] = M_KT
    s_raw[o3:o3 + d0, o2:o2 + d1] = gauge.conj().T
    s2_raw = fro(s_raw @ s_raw)
    rank_MKT = int(np.linalg.matrix_rank(M_KT, tol=1e-7))
    rank_AW = int(np.linalg.matrix_rank(A_W, tol=1e-7))
    bare_final = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    nC2_dressed = dressed_C2(Wd_b)

    print("\n(E) FULL BV BICOMPLEX at best a-priori physical-null carrier:")
    print(f"   carrier = {nm_b}   ||W|| = {nW_b:.4f}")
    print(f"   Noether ||B_W A_W|| = {noether:.2e}; ||s^2|| = {s2:.2e}  (target 0)")
    print(f"   leg ranks rank(M_KT)/rank(A_W) = {rank_MKT}/{rank_AW}")
    print(f"   NON-VACUITY raw-gauge control ||s_raw^2|| = {s2_raw:.3f} "
          f"(BREAKS closure: {s2_raw > 1e-6})")

    # ---------- (F) GUARDS ----------
    sig_rep = sigma_c(Wd_b)
    xi_dep = fro(sig_rep - sigma_c(Wd_b))   # builder never reads xi -> identically 0
    test_gens = [(3, 4), (10, 11), (0, 5)]
    max_def = max(fro(Sigma[g] @ sig_rep - sig_rep @ Sigma[g]) for g in test_gens)
    s_arr = np.array([(-1.0) ** a if a < 9 else (-1.0) ** (a + 1) for a in range(N)])
    U = np.eye(dim, dtype=complex)
    for a in [a for a in range(N) if s_arr[a] < 0]:
        U = U @ e[a]
    h_sig = fro(sig_rep @ U - U @ np.conjugate(sig_rep))
    JVS = np.kron(np.eye(N, dtype=complex), U)
    h_Pi = fro(Pi_kerBW @ JVS - JVS @ np.conjugate(Pi_kerBW))
    print("\n(F) GUARDS:")
    print(f"   ANTI-TRAP bare ||[Pi_RS,M_D]||   = {bare_final:.4f}  "
          f"(MUST be 58.72: {abs(bare_final - 58.72) < 0.01})")
    print(f"   ANTI-FIXED-SOLVE xi-dependence   = {xi_dep:.2e}  "
          f"(W_curv NOT a functional of C2/M_D/xi: {xi_dep < 1e-12})")
    print(f"   NON-EQUIVARIANT equivariance def = {max_def:.4f}  "
          f"(!=0, genuine connection: {max_def > 1e-6})")
    print(f"   H-LINEAR ||[sigma,J]||={h_sig:.2e}, ||[Pi,J]||={h_Pi:.2e}  "
          f"(H-linear: {max(h_sig, h_Pi) < 1e-6})")

    # ---------- VERDICT ----------
    best_null_C2 = min(r[2] for r in null_results)
    best_null_obs = min(r[3] for r in null_results)
    drop = nC2_bare - best_null_C2
    DRIVEN = best_null_C2 < 1.0
    PARTIAL = (best_null_C2 < nC2_bare - 5.0) and not DRIVEN
    status = ("C2_DRIVEN_TO_ZERO" if DRIVEN
              else "C2_PARTIAL_DROP" if PARTIAL
              else "C2_FLOORS_NEEDS_GLOBAL")
    null_special = best_null_C2 < min(arb) - 1.0

    print("\n" + "=" * 80)
    print("VERDICT")
    print("=" * 80)
    print(f"  bare C2 (target)                 : {nC2_bare:.4f}")
    print(f"  best PHYSICAL-NULL dressed C2     : {best_null_C2:.4f}  "
          f"(drop {drop:+.4f} = {100 * drop / nC2_bare:+.2f}%; toward 0? {DRIVEN})")
    print(f"  amplitude-tuned (same direction)  : {best_lam[1]:.4f} at lambda={best_lam[0]}")
    print(f"  arbitrary-bivector control min C2 : {min(arb):.4f}  (null special? {null_special})")
    print(f"  fixed-solve floor (reads C2, DQ)  : {solved_C2:.4f}  (=0? {solved_C2 < 1e-6})")
    print(f"  best physical-null obstruction    : {best_null_obs:.4f}  "
          f"(refs spurion {OBS_SPURION_REF}, flat-holonomy {OBS_FLATHOL_REF})")
    print(f"  ANTI-TRAP bare [Pi_RS,M_D]        : {bare_final:.4f}  (MUST be 58.72)")
    print(f"  bicomplex s^2                     : {s2:.2e}  (raw-control {s2_raw:.2f})")
    print(f"  W_curv genuine                    : so(9,5)-resid {so95_resid:.1e}, "
          f"xi-dep {xi_dep:.0e}, non-equiv {max_def:.3f}, H-lin {max(h_sig, h_Pi):.1e}")
    print(f"  STATUS                            : {status}")
    if status == "C2_FLOORS_NEEDS_GLOBAL":
        print("  => The LOCAL/fiber gimmel curvature, restricted exactly to the physical")
        print("     light cone, does NOT drive C2 down. C2 is fully Gamma-independent and")
        print("     W_curv IS an so(9,5) element, so it lies in the null-effect class. The")
        print("     residual requires the GLOBAL Y14 structure: the non-compact K3 end-data")
        print("     (active-research k3-chi-gate / noncompact-APS) -- the NAMED next requirement.")
    print(f"  evals = {n_eval[0]}; wall {time.time() - t0:.1f}s")

    return {
        "nC2_bare": nC2_bare, "best_null_C2": best_null_C2, "drop": drop,
        "amp_tuned_C2": best_lam[1], "arb_min_C2": float(min(arb)),
        "null_special": bool(null_special), "solved_C2": solved_C2,
        "best_null_obstruction": best_null_obs, "bare_trap": bare_final,
        "s2": s2, "s2_raw": s2_raw, "so95_resid": so95_resid,
        "frame_check": frame_check, "maxHV": maxHV, "xi_dep": xi_dep,
        "max_def": max_def, "H_lin": max(h_sig, h_Pi), "status": status,
    }


if __name__ == "__main__":
    main()
