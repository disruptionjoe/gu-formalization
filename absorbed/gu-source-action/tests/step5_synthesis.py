#!/usr/bin/env python3
"""STEP 5 - Synthesis + honest verdict for SPEC 5(iii).

SPEC 5(iii) asks for: "a BV-to-boundary-Dirac map tying the BV Koszul-Tate differential to an
actual geometric boundary Dirac operator WHOSE APS SPECTRAL SECTION CONNECTS TO THE OBSTRUCTION C2."

Steps 1-4 built the map and probed every joint. This file recomputes the load-bearing number
from EACH step in one place (on the repo xi, fast - no random scans) and asserts the chain, then
renders the honest verdict: the construction is REAL up to the squared/Laplacian level, but the
APS-spectral-section clause FAILS for a structurally-forced reason (eta = 0), so C2 lands as the
HS symbol-NORM of the boundary Dirac, NOT as its index. This is an honest NEGATIVE on 5(iii) with
a precisely-named wall - the eta=0 grading obstruction - not a forward connection.

Chain recomputed here:
  [1] C2 is a degree-1 first-order SYMBOL norm:  C2(xi) = K*|xi|,  K = C2/|xi| = sqrt(N*kappa).
  [2] D_Sigma = E + E^dag is EXACTLY self-adjoint:  ||D - D^dag|| = 0.
  [3] eta(D_Sigma) = #pos - #neg = 0, FORCED by the anticommuting Z2 grading G = Pi_RS - Q
      ({G,D} = 0) => spectral section trivial => CANNOT carry C2 as an index.
  [4] M_KT = N*(D_Sigma^2)|_surface EXACTLY  and  trace(M_KT) = C2^2  => C2 = HS norm, sqrt(trace).

Guards re-asserted: bare ||[Pi_RS,M_D]|| = 58.7215 untouched; C2 = 155.3625; nothing solved from
the target; all objects a-priori from the bridge.

Run: python tests/step5_synthesis.py
"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import gu_bridge  # noqa: E402

N = gu_bridge.N        # 14
DIM = gu_bridge.DIM    # 128


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=160)
    e, Gamma, Pi_RS, M_D = gu_bridge.constraint_objects()
    xi = np.asarray(gu_bridge.XI, dtype=complex)
    Q = np.eye(N * DIM, dtype=complex) - Pi_RS

    # ---- guards / anchors ------------------------------------------------------------------
    bare = float(np.linalg.norm(Pi_RS @ M_D - M_D @ Pi_RS))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi_RS))
    print(f"[guard] bare ||[Pi_RS,M_D]|| = {bare:.4f}  (must stay 58.7215; driving->0 is acausal)")
    print(f"[guard] C2 = ||Gamma M_D Pi_RS|| = {C2:.4f}  (155.3625)")
    assert abs(bare - 58.7215) < 1e-2, "ANTI-TRAP: bare commutator moved"
    assert abs(C2 - 155.3625) < 1e-2, "C2 moved"

    # =====================================================================================
    # [1] C2 is a degree-1 first-order SYMBOL norm:  C2(xi) = K|xi|.
    # =====================================================================================
    xi_norm = float(np.linalg.norm(xi.real))
    K = C2 / xi_norm
    # homogeneity: C2(2xi)/C2(xi) = 2 exactly (degree-1)
    M_D2 = np.kron(np.eye(N, dtype=complex), sum((2 * xi[a]) * e[a] for a in range(N)))
    C2_2xi = float(np.linalg.norm(Gamma @ M_D2 @ Pi_RS))
    deg1 = C2_2xi / C2
    print("\n=== [1] C2 is a first-order symbol norm (degree-1 homogeneous) ===")
    print(f"|xi| = {xi_norm:.4f} ;  K = C2/|xi| = {K:.4f} ;  C2(2xi)/C2(xi) = {deg1:.6f} (expect 2)")

    # =====================================================================================
    # [2] boundary Dirac D_Sigma = E + E^dag is EXACTLY self-adjoint (APS prereq).
    # =====================================================================================
    E = Q @ M_D @ Pi_RS
    D = E + E.conj().T
    sa_err = float(np.linalg.norm(D - D.conj().T))
    print("\n=== [2] D_Sigma = E + E^dag self-adjoint (APS prerequisite) ===")
    print(f"||D_Sigma - D_Sigma^dag|| = {sa_err:.3e}  (expect 0)")

    # =====================================================================================
    # [3] eta(D_Sigma) = 0 FORCED by anticommuting grading G = Pi_RS - Q (spectral section trivial).
    # =====================================================================================
    G = Pi_RS - Q
    anti = float(np.linalg.norm(G @ D + D @ G))            # {G,D} = 0
    g2 = float(np.linalg.norm(G @ G - np.eye(N * DIM)))     # G^2 = I (genuine Z2 grading)
    ev = np.linalg.eigvalsh(D)
    tol = 1e-7 * (abs(ev).max() + 1e-30)
    npos = int((ev > tol).sum())
    nneg = int((ev < -tol).sum())
    nzero = int((np.abs(ev) <= tol).sum())
    eta = npos - nneg
    print("\n=== [3] eta(D_Sigma) = 0, forced by anticommuting Z2 grading (THE WALL) ===")
    print(f"||G^2 - I|| = {g2:.3e} ;  ||{{G,D_Sigma}}|| = {anti:.3e}  (anticommutes => mirror spectrum)")
    print(f"#pos = {npos} ;  #neg = {nneg} ;  #zero = {nzero} ;  eta = #pos-#neg = {eta}")
    print(f"=> APS spectral section is SYMMETRIC (trivial); cannot carry C2 as an index.")

    # =====================================================================================
    # [4] M_KT = N*(D_Sigma^2)|_surface EXACTLY and trace(M_KT) = C2^2 => C2 = HS symbol norm.
    # =====================================================================================
    w, V = np.linalg.eigh(Pi_RS)
    W = V[:, np.where(w > 0.5)[0]]                          # 1792 x 1664 surface orthobasis
    B = Gamma @ M_D @ Pi_RS
    BW = B @ W
    M_KT = BW.conj().T @ BW                                 # Koszul-Tate Hessian on surface
    EW = E @ W
    EdE = EW.conj().T @ EW                                  # (E^dag E)|_surface = (D_Sigma^2)|_surface block
    rel_prop = float(np.linalg.norm(M_KT - N * EdE)) / float(np.linalg.norm(M_KT))
    tr_MKT = float(np.trace(M_KT).real)
    hs = np.sqrt(tr_MKT)
    print("\n=== [4] M_KT = N*(D_Sigma^2)|_surface EXACTLY ;  C2 = sqrt(trace M_KT) (HS norm) ===")
    print(f"||M_KT - N*(D_Sigma^2)|_surf|| / ||M_KT|| = {rel_prop:.3e}  (expect ~0, EXACT)")
    print(f"trace(M_KT) = {tr_MKT:.4f} ;  C2^2 = {C2**2:.4f} ;  sqrt(trace) = {hs:.4f} = C2")

    # =====================================================================================
    # VERDICT
    # =====================================================================================
    print("\n=== VERDICT on SPEC 5(iii) ===")
    map_built = sa_err < 1e-10 and rel_prop < 1e-10
    section_connects = (eta != 0)                          # the clause that 5(iii) actually needs
    c2_is_norm = abs(hs - C2) < 1e-6
    print(f"BV-to-boundary-Dirac MAP exists (D_Sigma self-adjoint, M_KT=N D^2)?  {map_built}")
    print(f"APS spectral section CONNECTS to C2 (eta != 0)?                      {section_connects}")
    print(f"C2 realized as the HS SYMBOL NORM sqrt(trace M_KT) instead?          {c2_is_norm}")
    print()
    print("READING: the BV-to-boundary-Dirac MAP is genuinely built - D_Sigma is an exactly")
    print("self-adjoint, boundary-elliptic first-order operator and its Laplacian on the")
    print("constraint surface IS the Koszul-Tate Hessian (M_KT = N*D_Sigma^2, rel 9e-16). But")
    print("the clause SPEC 5(iii) actually requires - 'APS spectral section connects to C2' -")
    print("FAILS for a forced reason: the chiral grading G = Pi_RS - Q anticommutes with D_Sigma,")
    print("mirroring its spectrum about 0, so eta = 0 and the spectral section is trivial. C2 is")
    print("a degree-1 SYMBOL norm (C2 = K|xi|, = sqrt(trace M_KT)), a magnitude living in the")
    print("singular-value scale of D_Sigma, NOT a sign-asymmetry / index. So this line does NOT")
    print("close 5(iii); it converts the open problem into a precise theorem-shaped obstruction:")
    print("  any boundary Dirac whose square is the (positive) Koszul-Tate Hessian inherits an")
    print("  anticommuting chiral grading and therefore eta=0, so C2 can never be its APS index.")
    print("NEXT CONCRETE STEP: break the grading - the index route needs an operator whose square")
    print("is NOT the bare positive Hessian (e.g. a curvature/connection term that fails to")
    print("anticommute with G, or a NON-self-adjoint / non-chiral boundary operator), OR abandon")
    print("the index reading and pursue C2 as a genuine first-order symbol invariant (its natural")
    print("home, per steps 1 & 4). The eta-route as posed is closed.")

    # Guards
    assert abs(bare - 58.7215) < 1e-2, "ANTI-TRAP"
    assert abs(C2 - 155.3625) < 1e-2, "C2 moved"
    assert abs(deg1 - 2.0) < 1e-6, "C2 must be degree-1 homogeneous"
    assert sa_err < 1e-10, "D_Sigma must be self-adjoint"
    assert anti < 1e-10 and g2 < 1e-10, "G must be an anticommuting Z2 grading"
    assert eta == 0, "eta must be 0 (the wall)"
    assert rel_prop < 1e-10, "M_KT = N*D_Sigma^2 must hold exactly"
    assert c2_is_norm, "C2 must equal sqrt(trace M_KT) (HS norm)"

    return {
        "bare": bare, "C2": C2, "K": K, "deg1": deg1,
        "sa_err": sa_err, "g2": g2, "anti": anti,
        "npos": npos, "nneg": nneg, "nzero": nzero, "eta": eta,
        "rel_prop": rel_prop, "trace_MKT": tr_MKT, "hs": hs,
        "map_built": map_built, "section_connects": section_connects, "N": N,
    }


if __name__ == "__main__":
    main()
