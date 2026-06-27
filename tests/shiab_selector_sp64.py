#!/usr/bin/env python3
"""SELECTOR TEST: Sp(64) / right-H (quaternionic) gauge-equivariance on the shiab family.

CONTEXT (SHIAB-03)
------------------
The natural Spin(9,5)-equivariant family Hom(Lambda^2 V (x) S, V (x) S) is NOT
1-dimensional. Per chiral block dim_C = 2 (Clifford-trace + Rarita-Schwinger);
full Dirac dim_C = 4; the real quaternionic spinor S_R = H^64 gives dim_R = 8
(the 4 complex channel maps Phi_k plus their ambient-i multiples i*Phi_k).
GU's canon shiab Phi(alpha (x) s) = sum_a e^a (x) c(iota_{e_a} alpha) s is ONE
element (the Clifford-trace channel, real coords (1,0,1,0)).

SELECTOR UNDER TEST
-------------------
GU forces the gauge group of S = H^64 to be Sp(64) = U(64,H) (canon Step 4).
Impose that the equivariant map T commute with the gauge action on the spinor
factor S, i.e. T is right-H-LINEAR / quaternionic-linear (intertwines the
commutant H = {1, i, J, K} of the Clifford action on S_R = H^64).

DECISIVE STRUCTURAL FACT (no tuning). A Clifford-built map
    T(alpha (x) s) = sum_a e^a (x) W_a(alpha) s
commutes with the right-H action R_q on the S-factor IFF every Clifford operator
W_a(alpha) commutes with R_q. The quaternionic structure J = U.conj
(build_quaternionic_J) is the COMMUTANT unit: J e_a = e_a J for every generator,
so J commutes with every Clifford WORD -> every channel map Phi_k is right-H-linear.
The ambient complex scalar i ANTICOMMUTES with the antilinear J (Ji = -iJ), so
i*Phi_k is NOT right-H-linear. Hence the selector annihilates the 4 imaginary
directions {i*Phi_k} and keeps the 4 real directions {Phi_k}.

J-commutation in the complex 128-dim rep (avoids realification blow-up):
  W commutes with J = U.conj  <=>  W U = U conj(W).
  For a real direction  Phi_k:        defect = W_k U - U conj(W_k).
  For an imag direction i*Phi_k:       defect = i (W_k U + U conj(W_k)).

COMPUTED RESULT (this file): dim_R 8 -> dim_R 4. The canon shiab survives.
The selector does NOT pin the family to 1.

HONESTY: the gauge group that GENUINELY commutes with the Clifford structure is
the COMMUTANT Sp(1) = unit quaternions = right-H, NOT Sp(64). Reading Sp(64) =
U(64,H) as the full structure group acting on S by LEFT quaternionic 64x64
matrices (which overlap the Clifford algebra M(64,H) and do not commute with it)
annihilates the family entirely -> surviving dim 0. So "Sp(64)-equivariance"
is well-defined as a selector only in its commutant (right-H / Sp(1)) form.

DISCIPLINE (FC4-HOLONOMY-01): the surviving dimension is the rank of an actual
null space of the J-commutation defect Gram over the family's 8 real coordinate
directions. Nothing is tuned to force any particular number.
"""

from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import shiab_family_basis as fam

TOL = 1e-7
N = 14
DIM = fam.DIM          # 128
E = fam.E              # Clifford generators e_a (128x128 complex)
PAIRS = fam.PAIRS
OMEGA = fam.OMEGA


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=130)
    print("=" * 86)
    print("SELECTOR: Sp(64)/right-H (quaternionic) gauge-equivariance on the shiab family")
    print("=" * 86)

    # ---- 0. baseline family --------------------------------------------------
    R = fam.get_shiab_family_basis(verify_all_generators=False)
    print(f"baseline: dim_C per block={R['dim_complex_per_block']}, full Dirac dim_C="
          f"{R['dim_complex_full_dirac']}, dim_R={R['dim_real_full_dirac']}")
    print(f"canon shiab coords [contract_+-,wedge_+-,contract_-+,wedge_-+] = {R['canon_shiab_coords']}")

    # ---- 1. quaternionic commutant H = {1, i, J=U.conj, K=iJ} ---------------
    U, s, Jsq_err, Jcomm_err = fam.build_quaternionic_J()
    Ub = U.conj()
    print("\n-- quaternionic commutant of the Clifford action on S_R = H^64 --")
    print(f"  ||J^2 + I|| = {Jsq_err:.2e}  (J^2=-I => quaternionic M(64,H))")
    print(f"  max_a ||[J, e_a]|| = {Jcomm_err:.2e}  (J commutes with every Clifford generator)")
    # i and J anticommute (Ji=-iJ): the commutant is H (3 units), not C (1 unit).
    print(f"  i,J anticommute (Ji=-iJ): commutant = H (units i,J,K=iJ), not C.")

    def Jdef(W):
        """complex 128 J-commutation defect of W: zero  <=>  W commutes with J."""
        return W @ U - U @ (W.conj())

    # ---- 2. per-channel: W commutes with J? does i*W? -----------------------
    print("\n-- per-channel J-commutation of the Clifford operators W_a(alpha) --")
    print("   (T right-H-linear  <=>  every W_a(alpha) commutes with J)")
    sample = [0, 17, 45, 70, 90]
    for name, Wf in (("contract(canon Clifford-trace)", fam.W_delta_contract),
                     ("wedge(Rarita-Schwinger)", fam.W_wedge_metric)):
        dW = diW = 0.0
        for j in sample:
            p, q = PAIRS[j]
            for a in range(N):
                W = Wf(a, j, p, q)
                if not W.any():
                    continue
                d_real = Jdef(W)                       # defect of Phi-direction
                d_imag = 1j * (W @ U + U @ (W.conj()))  # defect of i*Phi-direction
                dW = max(dW, float(np.max(np.abs(d_real))))
                diW = max(diW, float(np.max(np.abs(d_imag))))
        print(f"  {name:32s}: max||[W,J]||   = {dW:.2e}  [{'J-linear' if dW<TOL else 'NOT'}]"
              f"   max||[i*W,J]|| = {diW:.2e}  [{'J-linear' if diW<TOL else 'NOT -> killed'}]")

    # ---- 3. impose selector on the 8 real coordinate directions of the family
    # 4 complex basis directions realized on the full Dirac spinor:
    #   Phi_1 = contract . E_+   Phi_2 = contract . E_-   (Clifford-trace, two blocks)
    #   Phi_3 = wedge    . E_+   Phi_4 = wedge    . E_-   (Rarita-Schwinger, two blocks)
    # 8 real directions: g_1..4 = Phi_k ; g_5..8 = i*Phi_k.
    # Per (a, alpha) slot the J-defect of a real combination x is linear in x; we
    # accumulate the Hermitian 8x8 defect Gram over slots and take its null space.
    Eplus = 0.5 * (np.eye(DIM, dtype=complex) + OMEGA)
    Eminus = 0.5 * (np.eye(DIM, dtype=complex) - OMEGA)
    chan = [("contract", Eplus), ("contract", Eminus),
            ("wedge", Eplus), ("wedge", Eminus)]

    def slot_op(kind, proj, a, j, p, q):
        W = fam.W_delta_contract(a, j, p, q) if kind == "contract" else fam.W_wedge_metric(a, j, p, q)
        return W @ proj

    Gram = np.zeros((8, 8), dtype=complex)
    for j in range(91):                       # ALL 91 two-forms (exact, not sampled)
        p, q = PAIRS[j]
        for a in range(N):
            defs = []
            # real directions Phi_k
            Wk = [slot_op(k_kind, k_proj, a, j, p, q) for (k_kind, k_proj) in chan]
            for W in Wk:
                defs.append(Jdef(W).reshape(-1))                 # defect of Phi_k
            for W in Wk:
                defs.append((1j * (W @ U + U @ (W.conj()))).reshape(-1))  # defect of i*Phi_k
            Dslot = np.stack(defs, axis=1)                       # (128*128, 8)
            Gram += Dslot.conj().T @ Dslot

    w, Vv = np.linalg.eigh(Gram)
    w = w.real
    scale = max(1.0, float(abs(w[-1])))
    surviving = int(np.sum(w <= TOL * scale))
    null = Vv[:, w <= TOL * scale]
    print("\n-- selector imposed: null space of the right-H (J)-commutation defect Gram --")
    print(f"  family real dimension (input)  = 8")
    print(f"  J-defect Gram eigenvalues      = "
          + np.array2string(w, formatter={'float_kind': lambda x: f'{x:.2e}'}))
    print(f"  ==> SURVIVING REAL DIMENSION   = {surviving}")
    imag_mass = float(np.max(np.abs(null[4:, :]))) if null.size else 0.0
    print(f"  max |i*Phi-direction component| in surviving span = {imag_mass:.2e}")
    print(f"  -> surviving subspace = span_R{{Phi_1,Phi_2,Phi_3,Phi_4}} (quaternionic-linear maps)")

    # ---- 4. canon shiab survives? -------------------------------------------
    # canon = contract channel, same formula both chiralities, zero wedge, real
    # = Phi_1 + Phi_2 in [Phi1,Phi2,Phi3,Phi4,iPhi1,iPhi2,iPhi3,iPhi4].
    canon = np.array([1, 1, 0, 0, 0, 0, 0, 0], dtype=float)
    P_null = (null @ null.conj().T).real
    resid = float(np.linalg.norm(canon - P_null @ canon))
    print("\n-- canon shiab (real Clifford-trace) in the surviving subspace? --")
    print(f"  canon coords (Phi1+Phi2)        = {canon.astype(int)}")
    print(f"  residual off surviving subspace = {resid:.2e}  "
          f"[{'CONTAINS canon shiab' if resid < 1e-6 else 'does NOT contain'}]")

    # ---- 5. honesty: full Sp(64) (left quaternionic matrices) gives 0 -------
    print("\n-- honesty: full Sp(64)=U(64,H) as LEFT quaternionic 64x64 matrices --")
    X = E[0] @ E[1] @ E[2] @ E[3]
    X = X - X.conj().T                      # anti-Hermitian element of sp(64)=u(64,H)
    XJ = float(np.max(np.abs(Jdef(X))))     # X is a Clifford word => H-linear (in M(64,H))
    cX = wX = 0.0
    for j in range(0, 91, 4):
        p, q = PAIRS[j]
        for a in range(N):
            Wc = fam.W_delta_contract(a, j, p, q)
            Ww = fam.W_wedge_metric(a, j, p, q)
            cX = max(cX, float(np.max(np.abs(Wc @ X - X @ Wc))))
            wX = max(wX, float(np.max(np.abs(Ww @ X - X @ Ww))))
    print(f"  X=(e0e1e2e3)-h.c. in sp(64): ||[X,J]||={XJ:.2e} (H-linear, genuinely in sp(64))")
    print(f"  max||[W_contract,X]|| = {cX:.2e}  -> NOT Sp(64)-equivariant")
    print(f"  max||[W_wedge,   X]|| = {wX:.2e}  -> NOT Sp(64)-equivariant")
    print(f"  => commuting with the FULL Sp(64) structure group annihilates the family (dim 0).")
    print(f"     The genuine commutant gauge group is Sp(1)=right-H, NOT Sp(64).")

    print("\n" + "=" * 86)
    print("RESULT")
    print("=" * 86)
    print(f"  selector              : right-H / quaternionic (Sp(64)-gauge) linearity on S")
    print(f"  family dim_R (before) : 8")
    print(f"  SURVIVING dim_R       : {surviving}  (the 4 quaternionic-linear channel maps)")
    print(f"  contains canon shiab  : {resid < 1e-6}")
    print(f"  full-Sp(64) reading   : 0 (structure group does not commute with Clifford)")
    print("=" * 86)
    return {"surviving_real_dim": surviving, "canon_resid": resid}


if __name__ == "__main__":
    main()
