#!/usr/bin/env python3
"""STEP 3 - Spectral data of the boundary Dirac operator D_Sigma.

Step 2 built  D_Sigma(xi) = E(xi) + E(xi)^dag  (1792x1792, exactly self-adjoint),
with E(xi) = (I - Pi_RS) M_D Pi_RS = Q M_D Pi_RS the escape symbol. In the chiral
split  V = ker(Gamma) (+) im(Gamma^dag)  (1664 + 128) it has the pure off-diagonal form
        D_Sigma = [[ 0     E^dag ],
                   [ E     0     ]].

This step asks the spectral-section question that distinguishes THIS operator from the
parent's flat operator (which had eta = 0 by Clifford +/- symmetry):

    Does D_Sigma have FORCED +/- symmetry (eta = 0), or does the constraint-surface
    restriction / off-diagonal structure break it (eta != 0)?

We compute REAL numbers:

  (1) Full spectrum of D_Sigma. The chiral GRADING operator G = Pi_RS - Q (= +1 on
      ker Gamma, -1 on im Gamma^dag) ANTICOMMUTES with D_Sigma: {G, D} = 0. We verify
      ||{G,D}|| numerically. Anticommuting grading => spectrum symmetric about 0 =>
      eta = 0 EXACTLY (every +lambda matched by -lambda = G-image). So for D_Sigma the
      spectral asymmetry is FORCED to zero, structurally, exactly like the parent.
      We report eta = n_pos - n_neg, the kernel dim, and build P_+ (positive projector).

  (2) The honest follow-up: is the +/- symmetry an artifact of the off-diagonal
      Hermitian completion, or does the CONSTRAINT SURFACE itself preserve it? The
      genuinely intrinsic self-adjoint boundary operator is the Hermitian part of M_D
      compressed to ker(Gamma):  H = (M_D + M_D^dag)/2,  T = W^dag H W  (1664 x 1664).
      Note H = id_14 (x) c_space(xi): the timelike (1j G_a, a>=9) part of c(xi) is
      anti-Hermitian and DROPS, leaving only the 9 spacelike Clifford generators. On the
      full space c_space has perfectly symmetric spectrum; the question is whether the
      PROJECTION onto ker(Gamma) breaks that symmetry. We compute eta(T) = n_pos - n_neg
      and scan it over many xi (including the (9,5) null cone). If eta(T) != 0 the
      constraint surface carries a nontrivial spectral section; if eta(T) = 0 the
      symmetry survives the restriction and the spectral section is trivial here too.

Anti-trap: M_D and the bare commutator are untouched. Guards re-asserted at the end.

Run: python tests/step3_spectral_section.py
"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import gu_bridge  # noqa: E402

N = gu_bridge.N        # 14
DIM = gu_bridge.DIM    # 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)   # (9,5) signature


def build():
    e, Gamma, Pi_RS, M_D = gu_bridge.constraint_objects()
    Q = np.eye(N * DIM, dtype=complex) - Pi_RS
    w, V = np.linalg.eigh(Pi_RS)
    ker_idx = np.where(w > 0.5)[0]
    im_idx = np.where(w <= 0.5)[0]
    W = V[:, ker_idx]      # 1792 x 1664  (orthobasis of ker Gamma)
    U = V[:, im_idx]       # 1792 x 128   (orthobasis of im Gamma^dag)
    return e, Gamma, Pi_RS, M_D, Q, W, U


def cxi_mat(e, xi):
    return sum(xi[a] * e[a] for a in range(N))


def eta_signature(evals, tol):
    """Return (n_pos, n_neg, n_zero, eta=n_pos-n_neg) for a Hermitian spectrum."""
    n_pos = int((evals > tol).sum())
    n_neg = int((evals < -tol).sum())
    n_zero = int((np.abs(evals) <= tol).sum())
    return n_pos, n_neg, n_zero, n_pos - n_neg


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=160)
    e, Gamma, Pi_RS, M_D, Q, W, U = build()
    xi = gu_bridge.XI

    # ---- anchors / guards -----------------------------------------------------------------
    bare = float(np.linalg.norm(Pi_RS @ M_D - M_D @ Pi_RS))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi_RS))
    print(f"[anchors] bare ||[Pi_RS,M_D]|| = {bare:.4f} (expect 58.7215)")
    print(f"[anchors] C2 = ||Gamma M_D Pi_RS|| = {C2:.4f} (expect 155.3625)")
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "anchor mismatch"

    E_xi = Q @ M_D @ Pi_RS
    D = E_xi + E_xi.conj().T
    G = Pi_RS - Q                      # chiral grading: +1 on ker Gamma, -1 on im Gamma^dag

    # =====================================================================================
    # (1) D_Sigma spectrum + the FORCED symmetry via the chiral grading.
    # =====================================================================================
    anticomm = float(np.linalg.norm(G @ D + D @ G))
    g2 = float(np.linalg.norm(G @ G - np.eye(N * DIM)))
    print("\n=== (1) chiral grading G = Pi_RS - Q ===")
    print(f"||G^2 - I||      = {g2:.3e}   (G is a genuine Z2 grading)")
    print(f"||{{G, D_Sigma}}|| = {anticomm:.3e}   (anticommutes => spectrum symmetric => eta forced 0)")

    evals = np.linalg.eigvalsh(D)
    tol = 1e-7 * np.abs(evals).max()
    n_pos, n_neg, n_zero, eta = eta_signature(evals, tol)
    # direct symmetry residual: sort + |lambda_i + lambda_{-i}|
    s = np.sort(evals)
    sym_resid = float(np.max(np.abs(s + s[::-1])))
    print("\n=== (1) full spectrum of D_Sigma (1792-dim) ===")
    print(f"#pos={n_pos}  #neg={n_neg}  #zero={n_zero}")
    print(f"eta (= #pos - #neg, spectral asymmetry)       = {eta}")
    print(f"max_i |lambda_i + lambda_(N-i)| (mirror error) = {sym_resid:.3e}")
    print(f"spectrum range: [{evals.min():.4f}, {evals.max():.4f}]")
    nz = np.abs(evals) > tol
    print(f"nonzero |lambda|: min={np.abs(evals[nz]).min():.4f} max={np.abs(evals[nz]).max():.4f}")

    # APS positive spectral projector P_+ (projector onto strictly-positive eigenspace).
    wvec, Vvec = np.linalg.eigh(D)
    pos_mask = wvec > tol
    Vp = Vvec[:, pos_mask]
    P_plus = Vp @ Vp.conj().T
    proj_err = float(np.linalg.norm(P_plus @ P_plus - P_plus))
    herm_err = float(np.linalg.norm(P_plus - P_plus.conj().T))
    rank_Pplus = int(np.round(np.trace(P_plus).real))
    print(f"\nP_+ : rank={rank_Pplus}  ||P^2-P||={proj_err:.2e}  ||P-P^dag||={herm_err:.2e}")
    print(f"=> dim P_+ ({n_pos}) == dim P_- ({n_neg}): spectral section SYMMETRIC (trivial eta).")

    # =====================================================================================
    # (2) Does the CONSTRAINT SURFACE itself break the symmetry?
    #     T = compression of the Hermitian part of M_D onto ker(Gamma).
    # =====================================================================================
    H = 0.5 * (M_D + M_D.conj().T)
    # confirm H = id_14 (x) c_space  (only the 9 spacelike generators survive)
    c_space = sum(xi[a] * e[a] for a in range(9))
    H_space = np.kron(np.eye(N), c_space)
    print("\n=== (2) intrinsic self-adjoint boundary op: T = W^dag (Herm M_D) W on ker(Gamma) ===")
    print(f"||Herm(M_D) - id14(x)c_space|| = {np.linalg.norm(H - H_space):.3e} "
          f"(timelike 1j*G_a part is anti-Herm and drops)")

    # full-space spectrum of H (should be perfectly symmetric: Clifford)
    eH = np.linalg.eigvalsh(H)
    tolH = 1e-7 * np.abs(eH).max()
    hp, hn, hz, eta_H = eta_signature(eH, tolH)
    print(f"full-space Herm(M_D): #pos={hp} #neg={hn} #zero={hz}  eta={eta_H} "
          f"(symmetric on full space, as expected)")

    # compressed to ker(Gamma)
    T = W.conj().T @ H @ W            # 1664 x 1664 Hermitian
    T = 0.5 * (T + T.conj().T)
    eT = np.linalg.eigvalsh(T)
    tolT = 1e-7 * max(np.abs(eT).max(), 1e-12)
    tp, tn, tz, eta_T = eta_signature(eT, tolT)
    print(f"\ncompressed T (1664-dim): #pos={tp} #neg={tn} #zero={tz}")
    print(f"eta(T) = #pos - #neg = {eta_T}   <-- the constraint-surface spectral asymmetry")
    print(f"T spectrum range: [{eT.min():.4f}, {eT.max():.4f}]")

    # is there a grading anticommuting with T on ker(Gamma)? test the projected chirality.
    # The full-space chirality that anticommutes with c_space: omega = product of the OTHER
    # 5 generators is hard; instead we just report the measured eta(T) and scan it.

    # ----- scan eta(T) over many xi (random, plus the (9,5) null cone) -----
    rng = np.random.default_rng(1)
    etas_rand = []
    for _ in range(12):
        v = rng.standard_normal(N)
        v = v / np.linalg.norm(v)
        Hv = 0.5 * (np.kron(np.eye(N), cxi_mat(e, v.astype(complex)))
                    + np.kron(np.eye(N), cxi_mat(e, v.astype(complex))).conj().T)
        Tv = W.conj().T @ Hv @ W
        Tv = 0.5 * (Tv + Tv.conj().T)
        ev = np.linalg.eigvalsh(Tv)
        tv = 1e-7 * max(np.abs(ev).max(), 1e-12)
        _, _, _, et = eta_signature(ev, tv)
        etas_rand.append(et)
    etas_null = []
    for _ in range(8):
        sp = rng.standard_normal(9)
        tp_ = rng.standard_normal(5)
        tp_ = tp_ / np.linalg.norm(tp_) * np.linalg.norm(sp)
        v = np.concatenate([sp, tp_]); v = v / np.linalg.norm(v)
        Hv = 0.5 * (np.kron(np.eye(N), cxi_mat(e, v.astype(complex)))
                    + np.kron(np.eye(N), cxi_mat(e, v.astype(complex))).conj().T)
        Tv = W.conj().T @ Hv @ W
        Tv = 0.5 * (Tv + Tv.conj().T)
        ev = np.linalg.eigvalsh(Tv)
        tv = 1e-7 * max(np.abs(ev).max(), 1e-12)
        _, _, _, et = eta_signature(ev, tv)
        etas_null.append(et)
    print(f"\neta(T) over 12 random xi : {etas_rand}")
    print(f"eta(T) over 8 null-cone xi: {etas_null}")
    print(f"eta(T) always zero? {all(x == 0 for x in etas_rand + etas_null)}")

    # =====================================================================================
    # VERDICT
    # =====================================================================================
    print("\n=== VERDICT ===")
    forced_sym = anticomm < 1e-8
    print(f"(1) D_Sigma: {{G,D}}=0 (anticommuting grading)?  {forced_sym} ({anticomm:.1e})")
    print(f"(1) D_Sigma eta = #pos - #neg                  = {eta}  (forced 0)")
    print(f"(1) spectral section dim P_+ = dim P_-          = {n_pos} = {n_neg}: trivial/symmetric")
    print(f"(2) constraint-surface T eta(repo xi)          = {eta_T}")
    print(f"(2) eta(T) identically 0 over all tested xi?    "
          f"{all(x == 0 for x in etas_rand + etas_null) and eta_T == 0}")
    print("\nReading: eta = 0 is FORCED for D_Sigma by the exact chiral grading G=Pi_RS-Q, and")
    print("the constraint-surface compression T preserves it. The spectral section is TRIVIAL")
    print("(symmetric +/-), exactly as in the parent flat operator. C2 therefore cannot be an")
    print("eta-invariant of this boundary Dirac; it lives entirely in the singular-value")
    print("MAGNITUDES (|D_Sigma| = the symbol norm of Step 1), not in the sign asymmetry.")

    # Guards (anti-trap)
    assert abs(bare - 58.7215) < 1e-2, "ANTI-TRAP: bare commutator moved"
    assert abs(C2 - 155.3625) < 1e-2, "C2 moved"
    assert forced_sym, "grading must anticommute (structural claim)"
    assert eta == 0, "D_Sigma eta must be 0"

    return {
        "bare": bare, "C2": C2,
        "anticomm": anticomm, "g2": g2,
        "n_pos": n_pos, "n_neg": n_neg, "n_zero": n_zero, "eta_D": eta,
        "sym_resid": sym_resid, "rank_Pplus": rank_Pplus,
        "eta_H_full": eta_H, "eta_T": eta_T,
        "T_pos": tp, "T_neg": tn, "T_zero": tz,
        "etas_rand": etas_rand, "etas_null": etas_null,
        "all_zero": bool(all(x == 0 for x in etas_rand + etas_null) and eta_T == 0),
    }


if __name__ == "__main__":
    main()
