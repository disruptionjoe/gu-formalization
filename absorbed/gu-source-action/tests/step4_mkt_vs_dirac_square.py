#!/usr/bin/env python3
"""STEP 4 - The BV<->Dirac identification: is M_KT = D_Sigma^2 (+ lower order)?

The bicomplex Koszul-Tate operator B is the twisted gamma-trace (constraint) map restricted
to the surface; its Hessian is M_KT = B^dag B. The natural twisted Koszul-Tate operator,
fixed a-priori from the bridge (NOT solved from any target), is

        B = Gamma @ M_D @ Pi_RS            (128 x 1792, maps ker(Gamma) -> boundary)

Note ||B|| = ||Gamma M_D Pi_RS|| = C2 EXACTLY, so M_KT = B^dag B has top eigenvalue C2^2.
M_KT = Pi_RS M_D Gamma^dag Gamma M_D Pi_RS acts on the 1664-dim constraint surface ker(Gamma).

The boundary Dirac from Step 2 is  D_Sigma = E(xi) + E(xi)^dag,  E(xi) = Q M_D Pi_RS,
Q = I - Pi_RS. Because E maps ker(Gamma) -> im(Gamma^dag), E^2 = (E^dag)^2 = 0, so

        D_Sigma^2 = E^dag E   (+)   E E^dag      (block diagonal: surface (+) boundary)

i.e. the supersymmetric Dirac-Laplacian. The "Dirac-square = Hessian" bridge is the claim
that the SURFACE block (E^dag E) IS the Koszul-Tate Hessian M_KT, up to lower order.

KEY ALGEBRA (verified numerically below, not assumed):
  Gamma Gamma^dag = sum_a e_a e_a^dag = N * I   (each Clifford generator is unitary: tight frame).
  Hence the surface projector  Q = Gamma^dag (Gamma Gamma^dag)^{-1} Gamma = Gamma^dag Gamma / N.
  Then  E^dag E = Pi_RS M_D Q M_D Pi_RS = (1/N) Pi_RS M_D Gamma^dag Gamma M_D Pi_RS = (1/N) M_KT.

So the PREDICTION is  M_KT = N * (D_Sigma^2)|_surface  EXACTLY (N = 14), with the constant N
being the canonical tight-frame redundancy of the gamma-trace map -- an a-priori structural
constant, not a fitted one, and NOT a lower-order term (both sides are degree-2 homogeneous
in xi). We test all of this with real numbers and report:

  (1) ||Gamma Gamma^dag - N I|| (tight-frame check) and ||Q - Gamma^dag Gamma / N||.
  (2) ||M_KT - N*E^dag E|| / ||M_KT||         (the EXACT proportional identification).
  (3) ||M_KT - (D_Sigma^2)|_surface|| / ||M_KT||  (the BARE equation: off by the constant N).
  (4) degree of the discrepancy M_KT - D_Sigma^2 in xi (constant-multiple vs genuine lower order).
  (5) eigenvalue spectra: eig(M_KT) vs N*eig(E^dag E); top eig(M_KT) vs C2^2.
  (6) E^2 = 0 and the block-diagonality of D_Sigma^2 (so the surface block is well-defined).

Anti-trap: M_D and the bare commutator are untouched; B and Q are built from the bridge only.
Guards re-asserted at the end.

Run: python tests/step4_mkt_vs_dirac_square.py
"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import gu_bridge  # noqa: E402

N = gu_bridge.N        # 14
DIM = gu_bridge.DIM    # 128


def build():
    e, Gamma, Pi_RS, M_D = gu_bridge.constraint_objects()
    Q = np.eye(N * DIM, dtype=complex) - Pi_RS
    w, V = np.linalg.eigh(Pi_RS)
    ker_idx = np.where(w > 0.5)[0]      # ker(Gamma): 1664
    W = V[:, ker_idx]                   # 1792 x 1664 orthobasis of the constraint surface
    return e, Gamma, Pi_RS, M_D, Q, W


def cxi_mat(e, xi):
    return sum(xi[a] * e[a] for a in range(N))


def mkt_on_surface(e, Gamma, Pi_RS, W, xi):
    """M_KT = B^dag B with B = Gamma M_D Pi_RS, expressed on the 1664-dim surface basis W."""
    M_D = np.kron(np.eye(N, dtype=complex), cxi_mat(e, xi))
    B = Gamma @ M_D @ Pi_RS                       # 128 x 1792
    BW = B @ W                                    # 128 x 1664 (B restricted to surface)
    return BW.conj().T @ BW                       # 1664 x 1664 Hermitian = M_KT|_surface


def edge_on_surface(e, Q, Pi_RS, W, xi):
    """(E^dag E)|_surface, E = Q M_D Pi_RS, expressed on the surface basis W."""
    M_D = np.kron(np.eye(N, dtype=complex), cxi_mat(e, xi))
    E = Q @ M_D @ Pi_RS                           # 1792 x 1792
    EW = E @ W                                     # 1792 x 1664
    return EW.conj().T @ EW                        # 1664 x 1664 = (E^dag E)|_surface


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=160)
    e, Gamma, Pi_RS, M_D, Q, W = build()
    xi = gu_bridge.XI

    # ---- anchors / guards -----------------------------------------------------------------
    bare = float(np.linalg.norm(Pi_RS @ M_D - M_D @ Pi_RS))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi_RS))
    print(f"[anchors] bare ||[Pi_RS,M_D]|| = {bare:.4f} (expect 58.7215)")
    print(f"[anchors] C2 = ||Gamma M_D Pi_RS|| = {C2:.4f} (expect 155.3625)")
    assert abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "anchor mismatch"

    # =====================================================================================
    # (1) Tight-frame check: Gamma Gamma^dag = N I, and Q = Gamma^dag Gamma / N.
    # =====================================================================================
    GGd = Gamma @ Gamma.conj().T                  # 128 x 128
    tight_err = float(np.linalg.norm(GGd - N * np.eye(DIM)))
    Q_pred = Gamma.conj().T @ Gamma / N
    q_err = float(np.linalg.norm(Q - Q_pred))
    print("\n=== (1) tight-frame structure of the gamma-trace map ===")
    print(f"||Gamma Gamma^dag - N*I||  = {tight_err:.3e}   (N={N}; each e_a unitary => tight frame)")
    print(f"||Q - Gamma^dag Gamma / N|| = {q_err:.3e}   (surface projector IS frame-normalized)")

    # =====================================================================================
    # (6) E^2 = 0 and block-diagonality of D_Sigma^2 (surface block well-defined).
    # =====================================================================================
    E_full = Q @ M_D @ Pi_RS
    D = E_full + E_full.conj().T
    D2 = D @ D
    e2_err = float(np.linalg.norm(E_full @ E_full))
    # off-diagonal (surface<->boundary) blocks of D^2 should vanish
    offdiag = float(np.linalg.norm(Q @ D2 @ Pi_RS))
    print("\n=== (6) D_Sigma^2 structure ===")
    print(f"||E(xi)^2|| = {e2_err:.3e}   (E nilpotent => D^2 block-diagonal)")
    print(f"||Q D^2 Pi_RS|| (surface<->boundary block of D^2) = {offdiag:.3e}  (=> block diagonal)")

    # =====================================================================================
    # (2) EXACT proportional identification:  M_KT = N * (E^dag E)|_surface.
    # =====================================================================================
    M_KT = mkt_on_surface(e, Gamma, Pi_RS, W, xi)
    EdE = edge_on_surface(e, Q, Pi_RS, W, xi)
    nrm_MKT = float(np.linalg.norm(M_KT))
    rel_prop = float(np.linalg.norm(M_KT - N * EdE)) / nrm_MKT
    print("\n=== (2) EXACT identification: M_KT = N * (D_Sigma^2)|_surface ===")
    print(f"||M_KT|| = {nrm_MKT:.4f}")
    print(f"||M_KT - N*(E^dag E)|| / ||M_KT|| = {rel_prop:.3e}   (expect ~0: EXACT proportionality)")

    # =====================================================================================
    # (3) BARE equation:  M_KT =?= (D_Sigma^2)|_surface   (off by the constant N).
    # =====================================================================================
    rel_bare = float(np.linalg.norm(M_KT - EdE)) / nrm_MKT
    print("\n=== (3) BARE equation: M_KT =?= (D_Sigma^2)|_surface ===")
    print(f"||M_KT - (E^dag E)|| / ||M_KT|| = {rel_bare:.4f}   (NOT ~0: differs by factor N)")
    print(f"ratio ||M_KT|| / ||E^dag E|| = {nrm_MKT/float(np.linalg.norm(EdE)):.4f}  (expect N={N})")

    # =====================================================================================
    # (4) Order of the discrepancy: is M_KT - D_Sigma^2 lower-order in xi, or a constant
    #     multiple of the same degree? Both M_KT and D^2 are degree-2 homogeneous; the
    #     residual 13*E^dag E - E E^dag is ALSO degree-2 => a constant multiple, not lower order.
    # =====================================================================================
    def deg(fn, k=2):
        a = float(np.linalg.norm(fn(xi)))
        b = float(np.linalg.norm(fn(2.0 * np.asarray(xi))))
        return b / a, 2.0 ** k

    f_MKT = lambda x: mkt_on_surface(e, Gamma, Pi_RS, W, np.asarray(x, dtype=complex))
    f_res = lambda x: (mkt_on_surface(e, Gamma, Pi_RS, W, np.asarray(x, dtype=complex))
                       - edge_on_surface(e, Q, Pi_RS, W, np.asarray(x, dtype=complex)))
    r_mkt, exp2 = deg(f_MKT)
    r_res, _ = deg(f_res)
    print("\n=== (4) homogeneity degree (||f(2xi)||/||f(xi)|| ; degree-2 => 4.0) ===")
    print(f"M_KT:               ratio = {r_mkt:.4f}  (expect {exp2:.1f})")
    print(f"M_KT - D^2 residual: ratio = {r_res:.4f}  (expect {exp2:.1f} => SAME degree, constant multiple,")
    print(f"                                          NOT a lower-order Dirac remainder)")

    # =====================================================================================
    # (5) Spectra: eig(M_KT) vs N*eig(E^dag E); top eig(M_KT) vs C2^2.
    # =====================================================================================
    ev_MKT = np.linalg.eigvalsh(M_KT)[::-1]
    ev_NEdE = (N * np.linalg.eigvalsh(EdE))[::-1]
    spec_err = float(np.max(np.abs(ev_MKT - ev_NEdE)))
    top = float(ev_MKT[0])
    tr_MKT = float(np.trace(M_KT).real)   # = ||B||_F^2 = C2^2 (C2 is a Frobenius/HS norm)
    print("\n=== (5) spectra ===")
    print(f"max_i |eig_i(M_KT) - N*eig_i(E^dag E)| = {spec_err:.3e}  (=> identical spectra)")
    print(f"trace(M_KT) = {tr_MKT:.4f} ;  C2^2 = {C2**2:.4f} ;  sqrt(trace) = {np.sqrt(tr_MKT):.4f} = C2")
    print(f"top eig(M_KT) = {top:.4f}  (operator-norm mode; C2 is the HS norm = sqrt(trace))")
    print(f"rank(M_KT) = {int((ev_MKT > 1e-7*top).sum())} / {M_KT.shape[0]}  "
          f"(surface modes seen by the boundary Dirac)")

    # =====================================================================================
    # VERDICT
    # =====================================================================================
    print("\n=== VERDICT ===")
    exact_prop = rel_prop < 1e-10
    bare_fails = rel_bare > 0.1
    constant_multiple = abs(r_res - 4.0) < 1e-3
    print(f"M_KT = N*(D_Sigma^2)|_surface EXACTLY?        {exact_prop} (rel {rel_prop:.1e})")
    print(f"bare M_KT = D_Sigma^2 FAILS (factor N off)?    {bare_fails} (rel {rel_bare:.3f})")
    print(f"discrepancy is a constant multiple (deg-2)?    {constant_multiple} (ratio {r_res:.3f})")
    print(f"trace(M_KT) = C2^2 (HS norm) ?                  {abs(np.sqrt(tr_MKT)-C2) < 1e-6}")
    print("\nReading: the boundary Dirac D_Sigma is, up to the canonical tight-frame constant")
    print(f"sqrt(N)=sqrt({N}), the SQUARE ROOT of the Koszul-Tate Hessian on the constraint")
    print("surface:  M_KT = N * (E^dag E) = N * (D_Sigma^2)|_surface, EXACTLY. The constant N is")
    print("Gamma Gamma^dag = N*I (gamma-trace tight-frame redundancy), a-priori not fitted, and it")
    print("is a same-degree multiple, NOT a lower-order remainder -- so 'M_KT = D_Sigma^2' holds")
    print("only after normalizing the Koszul-Tate map by 1/sqrt(N). The BV<->boundary-Dirac bridge")
    print("thus HOLDS at the full operator (Hessian) level, beyond Step 1's symbol level; but the")
    print("missing datum it points to (D_Sigma's spectral section) was shown trivial in Step 3,")
    print("so this identification carries C2 as the HS symbol norm sqrt(trace M_KT)=C2, not an index.")

    # Guards (anti-trap)
    assert abs(bare - 58.7215) < 1e-2, "ANTI-TRAP: bare commutator moved"
    assert abs(C2 - 155.3625) < 1e-2, "C2 moved"
    assert tight_err < 1e-9, "tight-frame Gamma Gamma^dag = N I must hold a-priori"
    assert exact_prop, "M_KT = N*(E^dag E) must hold exactly"
    assert abs(np.sqrt(tr_MKT) - C2) < 1e-6, "trace(M_KT) must equal C2^2 (HS norm)"

    return {
        "bare": bare, "C2": C2,
        "tight_err": tight_err, "q_err": q_err,
        "e2_err": e2_err, "offdiag": offdiag,
        "nrm_MKT": nrm_MKT, "rel_prop": rel_prop, "rel_bare": rel_bare,
        "ratio_MKT_EdE": nrm_MKT / float(np.linalg.norm(EdE)),
        "r_res": r_res, "spec_err": spec_err, "top": top, "trace_MKT": tr_MKT, "C2sq": C2**2,
        "N": N,
    }


if __name__ == "__main__":
    main()
