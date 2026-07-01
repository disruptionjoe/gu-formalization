#!/usr/bin/env python3
"""STEP 2 - Build the candidate boundary Dirac operator D_Sigma and test it.

Step 1 established the escape symbol frame {E_a}, E_a = (I-Pi_RS)(id_14 (x) e_a) Pi_RS,
so E(xi) = sum_a xi_a E_a = (I-Pi_RS) M_D Pi_RS. It is an HS-orthonormal elliptic frame
(Frobenius Gram = 33.9592*I_14), with C2(xi)=21.8043|xi| exactly, but the strict OPERATOR
Clifford identity E(xi)^dag E(xi) = |xi|^2 P fails by ~1.3%. That gap is this step's wall.

The natural self-adjoint boundary operator whose principal symbol is the Hermitian completion
of the escape symbol is

        D_Sigma(xi) = E(xi) + E(xi)^dag         (1792 x 1792, Hermitian by construction)

In the splitting  V = ker(Gamma) (+) im(Gamma^dag)   (dims 1664 + 128) this is

        D_Sigma = [[ 0      E^dag ],
                   [ E      0     ]]            (purely OFF-diagonal == chiral Dirac form)

because E = Q M_D Pi_RS maps ker(Gamma) -> im(Gamma^dag) and E^dag the reverse. This is exactly
the chiral block form of a Dirac boundary operator. We test, with REAL numbers:

  (a) Self-adjoint? ||D_Sigma - D_Sigma^dag||  (APS prerequisite).
  (b) Elliptic where? D_Sigma on the FULL space has rank <= 2*128 = 256 (forced by the 1664 vs 128
      chirality-dimension mismatch), so it is NOT elliptic on V. The honest ellipticity question is
      on the 128-dim boundary spinor space im(Gamma^dag): is the reduced map E(xi) of full rank 128
      with smallest singular value bounded away from 0 for non-null xi? We scan sigma_min(E(xi)) over
      the Euclidean unit sphere, the (9,5) null cone (the physical light cone), and correlate with the
      eta-quadratic form. A genuine Dirac symbol is elliptic exactly off its null cone.
  (c) Does it act WITHIN the constraint surface? Compute Pi_RS D_Sigma Pi_RS (intrinsic part on
      ker Gamma) and Q D_Sigma Q. A pure boundary-coupling operator has both = 0.

Anti-trap: M_D and the bare commutator are NOT modified. Guards re-asserted at the end.

Run: python tests/step2_boundary_dirac.py
"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import gu_bridge  # noqa: E402

N = gu_bridge.N        # 14
DIM = gu_bridge.DIM    # 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)   # (9,5) signature = the physical light cone


def build():
    """Return verified objects + escape frame + orthobases for the chiral splitting."""
    e, Gamma, Pi_RS, M_D = gu_bridge.constraint_objects()
    Q = np.eye(N * DIM, dtype=complex) - Pi_RS          # projector onto im(Gamma^dag), rank 128
    I14 = np.eye(N, dtype=complex)
    E = [Q @ np.kron(I14, e[a]) @ Pi_RS for a in range(N)]
    # orthonormal bases: W spans ker(Gamma) (1664), U spans im(Gamma^dag) (128)
    w, V = np.linalg.eigh(Pi_RS)
    ker_idx = np.where(w > 0.5)[0]
    im_idx = np.where(w <= 0.5)[0]
    W = V[:, ker_idx]      # 1792 x 1664
    U = V[:, im_idx]       # 1792 x 128
    return e, Gamma, Pi_RS, M_D, Q, E, W, U


def cxi_mat(e, xi):
    return sum(xi[a] * e[a] for a in range(N))


def reduced_escape(e, W, U, xi):
    """E(xi) expressed in the chiral orthobases: 128 x 1664 matrix U^dag (id14 x c(xi)) W.

    Its singular values ARE the singular values of the full E(xi); this avoids a 1792^3 SVD.
    """
    cxi = cxi_mat(e, xi)
    MW = np.kron(np.eye(N, dtype=complex), cxi) @ W      # 1792 x 1664
    return U.conj().T @ MW                               # 128 x 1664


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=160)
    e, Gamma, Pi_RS, M_D, Q, E, W, U = build()
    xi = gu_bridge.XI

    # ---- anchors / guards -----------------------------------------------------------------
    bare = float(np.linalg.norm(Pi_RS @ M_D - M_D @ Pi_RS))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi_RS))
    print(f"[anchors] bare ||[Pi_RS,M_D]|| = {bare:.4f} (expect 58.7215)")
    print(f"[anchors] C2 = ||Gamma M_D Pi_RS|| = {C2:.4f} (expect 155.3625)")
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "anchor mismatch"

    E_xi = sum(xi[a] * E[a] for a in range(N))
    assert np.allclose(E_xi, Q @ M_D @ Pi_RS), "E(xi) != escape"

    # =====================================================================================
    # (a) SELF-ADJOINTNESS of D_Sigma = E(xi) + E(xi)^dag.
    # =====================================================================================
    D = E_xi + E_xi.conj().T
    sa_err = float(np.linalg.norm(D - D.conj().T))
    print("\n=== (a) self-adjointness of D_Sigma = E(xi)+E(xi)^dag ===")
    print(f"||D_Sigma - D_Sigma^dag|| = {sa_err:.3e}  (Hermitian completion => 0)")

    # =====================================================================================
    # (c) BLOCK / CONSTRAINT structure (done before b so we know the geometry).
    #   Pi_RS D Pi_RS = intrinsic action ON ker(Gamma); Q D Q = action on the normal space.
    #   E is off-diagonal in the ker/im split => both should be ~0 (pure chiral coupling).
    # =====================================================================================
    intrinsic = float(np.linalg.norm(Pi_RS @ D @ Pi_RS))
    normalblk = float(np.linalg.norm(Q @ D @ Q))
    coupling = float(np.linalg.norm(Q @ D @ Pi_RS))
    print("\n=== (c) constraint-surface action ===")
    print(f"||Pi_RS D Pi_RS|| (intrinsic on ker Gamma) = {intrinsic:.3e}")
    print(f"||Q D Q||        (intrinsic on im Gamma^d) = {normalblk:.3e}")
    print(f"||Q D Pi_RS||    (boundary coupling block) = {coupling:.4f}")
    print("=> D_Sigma is PURE OFF-DIAGONAL: a chiral bulk<->boundary coupling, not an")
    print("   operator intrinsic to ker(Gamma).")

    # =====================================================================================
    # (b) ELLIPTICITY.
    #   Full-space spectrum of D first: eigenvalues come in +/- pairs (= +/- sing.vals of E)
    #   plus a large zero block. Confirm rank <= 256 = 2*128.
    # =====================================================================================
    evals = np.linalg.eigvalsh(D)
    tol = 1e-7 * np.abs(evals).max()
    n_pos = int((evals > tol).sum())
    n_neg = int((evals < -tol).sum())
    n_zero = int((np.abs(evals) <= tol).sum())
    print("\n=== (b) full-space spectrum of D_Sigma (1792-dim) ===")
    print(f"#positive={n_pos}  #negative={n_neg}  #zero={n_zero}  (total {len(evals)})")
    print(f"rank(D_Sigma) = {n_pos + n_neg} (forced ceiling 2*128 = 256; "
          f"kernel dim {n_zero} from the 1664 vs 128 chirality mismatch)")
    print(f"=> NOT elliptic on the full space V. Ellipticity must be read on the 128-dim boundary.")

    # Reduced boundary operator: singular values of E(xi) (128 of them). sigma_min = ellipticity.
    Er = reduced_escape(e, W, U, xi)
    sv = np.linalg.svd(Er, compute_uv=False)
    print("\n--- reduced boundary map E(xi): 128 singular values (at repo xi) ---")
    print(f"rank = {int((sv > 1e-9*sv.max()).sum())} / 128")
    print(f"sigma_max = {sv.max():.4f}   sigma_min = {sv.min():.4f}   "
          f"cond = {sv.max()/sv.min():.2f}")

    # ----- ellipticity scan over the EUCLIDEAN unit sphere -----
    rng = np.random.default_rng(0)
    smin_eu, smax_eu, etaval_eu = [], [], []
    for _ in range(30):
        v = rng.standard_normal(N)
        v = v / np.linalg.norm(v)
        s = np.linalg.svd(reduced_escape(e, W, U, v.astype(complex)), compute_uv=False)
        smin_eu.append(s.min())
        smax_eu.append(s.max())
        etaval_eu.append(float(v @ (ETA * v)))
    smin_eu = np.array(smin_eu); smax_eu = np.array(smax_eu); etaval_eu = np.array(etaval_eu)
    print("\n=== (b) ellipticity scan over Euclidean unit sphere (30 dirs) ===")
    print(f"sigma_min: min={smin_eu.min():.4f} max={smin_eu.max():.4f} "
          f"mean={smin_eu.mean():.4f} std={smin_eu.std():.4f}")
    print(f"sigma_max: min={smax_eu.min():.4f} max={smax_eu.max():.4f} mean={smax_eu.mean():.4f}")
    print(f"sigma_min bounded away from 0? {bool(smin_eu.min() > 1e-3)}  "
          f"(Euclidean-elliptic if yes)")
    # correlation of sigma_min with the (9,5) eta quadratic form
    if smin_eu.std() > 1e-9:
        corr = float(np.corrcoef(smin_eu, etaval_eu)[0, 1])
        print(f"corr(sigma_min, eta-quadratic) over sphere = {corr:+.3f}")

    # ----- on the (9,5) NULL CONE (physical light cone: eta-norm = 0) -----
    smin_null = []
    for _ in range(30):
        sp = rng.standard_normal(9)
        tp = rng.standard_normal(5)
        tp = tp / np.linalg.norm(tp) * np.linalg.norm(sp)   # |time| = |space| => eta-norm 0
        v = np.concatenate([sp, tp])
        v = v / np.linalg.norm(v)
        s = np.linalg.svd(reduced_escape(e, W, U, v.astype(complex)), compute_uv=False)
        smin_null.append(s.min())
    smin_null = np.array(smin_null)
    print("\n=== (b) on the (9,5) NULL CONE (physical light cone, eta-norm=0) ===")
    print(f"sigma_min on cone: min={smin_null.min():.4f} max={smin_null.max():.4f} "
          f"mean={smin_null.mean():.4f}")
    print(f"does the boundary symbol DEGENERATE on the light cone? "
          f"{bool(smin_null.min() < 0.5 * smin_eu.mean())}")

    # ----- timelike vs spacelike extremes -----
    s_time = np.linalg.svd(reduced_escape(e, W, U,
            np.array([0]*9 + [1,0,0,0,0], dtype=complex)), compute_uv=False)
    s_space = np.linalg.svd(reduced_escape(e, W, U,
            np.array([1]+[0]*13, dtype=complex)), compute_uv=False)
    print(f"\npure timelike e_9 : sigma_min={s_time.min():.4f} sigma_max={s_time.max():.4f}")
    print(f"pure spacelike e_0: sigma_min={s_space.min():.4f} sigma_max={s_space.max():.4f}")

    # =====================================================================================
    # VERDICT
    # =====================================================================================
    print("\n=== VERDICT ===")
    is_sa = sa_err < 1e-8
    is_offdiag = intrinsic < 1e-8 and normalblk < 1e-8
    euclid_elliptic = bool(smin_eu.min() > 1e-3)
    cone_degenerates = bool(smin_null.min() < 0.5 * smin_eu.mean())
    print(f"(a) D_Sigma self-adjoint?                       {is_sa} ({sa_err:.1e})")
    print(f"(c) D_Sigma pure chiral coupling (off-diag)?    {is_offdiag}")
    print(f"(b) reduced boundary map full rank 128?         {int((sv>1e-9*sv.max()).sum())==128}")
    print(f"(b) Euclidean-elliptic (sigma_min>0 all dirs)?  {euclid_elliptic} "
          f"(min sigma_min={smin_eu.min():.4f})")
    print(f"(b) degenerates on the (9,5) light cone?        {cone_degenerates}")

    # Guards (anti-trap): bare commutator and C2 unchanged.
    assert abs(bare - 58.7215) < 1e-2, "ANTI-TRAP: bare commutator moved"
    assert abs(C2 - 155.3625) < 1e-2, "C2 moved"

    return {
        "sa_err": sa_err, "intrinsic": intrinsic, "normalblk": normalblk,
        "rank_full": n_pos + n_neg, "n_zero": n_zero,
        "sv_min": float(sv.min()), "sv_max": float(sv.max()),
        "smin_eu_min": float(smin_eu.min()), "smin_eu_mean": float(smin_eu.mean()),
        "smin_null_min": float(smin_null.min()), "smin_null_mean": float(smin_null.mean()),
        "euclid_elliptic": euclid_elliptic, "cone_degenerates": cone_degenerates,
        "bare": bare, "C2": C2,
    }


if __name__ == "__main__":
    main()
