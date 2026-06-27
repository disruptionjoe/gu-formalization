#!/usr/bin/env python3
"""SELECTOR TEST: quaternionic H-linearity (right-H-linearity / commute with J).

CONTEXT (SHIAB-03)
------------------
The natural Spin(9,5)-equivariant family Hom(Lambda^2 V (x) S, V (x) S) is NOT
1-dimensional. Computed from first principles (tests/shiab_family_basis.py):

    complex dim per chiral block = 2   (contract = Clifford-trace ; wedge = Rarita-Schwinger)
    complex dim full Dirac       = 4
    REAL  dim full Dirac         = 8   (= the 4 complex maps Phi_k PLUS their i-multiples
                                        i*Phi_k, because S_R = H^64 was COUNTED: i is a
                                        quaternion unit acting Spin-equivariantly on S_R).

This script imposes ONE candidate selector and COMPUTES the surviving dimension
from first principles (FC4-HOLONOMY-01: nothing tuned to force dim 1).

SELECTOR  (origin: gu_derived -- Cl(9,5)=M(64,H) is forced by the (9,5) signature)
----------------------------------------------------------------------------------
Require RIGHT-H-LINEARITY: the map must commute with the quaternionic structure
J (J^2 = -1, J commutes with every Clifford generator e_a, J preserves chirality)
on S = H^64. Equivalently T is a homomorphism of right-H-modules:

    (1 (x) J_cod) o T  =  T o (1 (x) J_dom)              [J acts on the spinor factor]

The real family is 8 BECAUSE the quaternionic doubling {Phi_k, i*Phi_k} was counted.
H-linearity (commute with i AND J = commute with all of H) cuts the i-multiples:
i*Phi_k is complex-linear (commutes with i) but ANTI-commutes with J in the sense
that it fails J-commutation, so it is removed.

WHAT IS COMPUTED
----------------
For each chiral block the complex Hom space is span{ T_contract, T_wedge } (dim_C 2).
A general real-family element is  T = c1 T_contract + c2 T_wedge ,  c1,c2 in C
(4 real params/block, 8 total). H-linearity, evaluated on the spinor factor in
chiral coordinates, reduces (for every form index j and codomain vector index a) to

    Tmat[a,j] A_in  -  A_out conj( Tmat[a,j] )  =  0

where J_in(s) = A_in conj(s),  J_out(w) = A_out conj(w) are the antilinear chiral
representatives of J. This is a REAL-linear system in (Re c1, Im c1, Re c2, Im c2);
its real null space is the surviving H-linear subdimension -- COMPUTED, not assumed.
We also (a) verify A conj(A) = -I (J^2=-1), (b) verify J preserves chirality
(no S+<->S- leakage), (c) check whether GU's canon contract shiab survives, and
(d) confirm the i-multiple i*Phi is killed.
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
N = fam.N  # 14


def chiral_J(Bout, Bin, U):
    """Antilinear representative of J on a chiral block: J(s) = A conj(s).
    A_in  = Bin^dag  U conj(Bin),  acting on the chiral coordinate space.
    Returns (A, J_sq_err, leak_err) with J_sq_err = ||A conj(A) + I|| (J^2=-1)
    and leak_err measuring S+<->S- leakage (should be ~0; J preserves chirality)."""
    A = Bin.conj().T @ U @ np.conjugate(Bin)
    Jsq = A @ np.conjugate(A)                       # J^2 represented matrix
    J_sq_err = float(np.max(np.abs(Jsq + np.eye(A.shape[0]))))
    # leakage: the component of U conj(Bin) outside span(Bin) seen from the OTHER chirality
    leak = Bout.conj().T @ U @ np.conjugate(Bin)
    leak_err = float(np.max(np.abs(leak)))
    return A, J_sq_err, leak_err


def block_slices(Wfun, Pin, Pout):
    """Return slices S[a][j] = 64x64 (out x in) Clifford matrix for the map
    T(e_p^e_q (x) s) = sum_a e^a (x) Wfun(a,j,p,q) s, projected to the chiral block."""
    T = fam.build_T(Wfun, Pin, Pout)   # shape (14, dimOut, 91, dimIn)
    return T  # index as T[a, :, j, :]


def hlinear_defect(c1, c2, Tc, Tw, A_in, A_out):
    """Stacked H-linearity defect over all (a,j):
       Tmat[a,j] A_in - A_out conj(Tmat[a,j]),  Tmat = c1 Tc + c2 Tw.
    Returns a complex 1-D array (flattened)."""
    Tmat = c1 * Tc + c2 * Tw                          # (14, do, 91, di)
    # for each (a,j): M = Tmat[a,:,j,:]  ->  M A_in - A_out conj(M)
    out = np.empty_like(Tmat)
    for a in range(Tmat.shape[0]):
        for j in range(Tmat.shape[2]):
            M = Tmat[a, :, j, :]
            out[a, :, j, :] = M @ A_in - A_out @ np.conjugate(M)
    return out.reshape(-1)


def real_nullspace_dim(Tc, Tw, A_in, A_out):
    """Build the REAL linear map p=(Re c1, Im c1, Re c2, Im c2) -> stacked real+imag
    of the H-linearity defect; return (surviving_real_dim, constraint_rank,
    singular_values, basis_real_params)."""
    basis_p = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
    cols = []
    for (x1, y1, x2, y2) in basis_p:
        d = hlinear_defect(x1 + 1j * y1, x2 + 1j * y2, Tc, Tw, A_in, A_out)
        cols.append(np.concatenate([d.real, d.imag]))
    Mreal = np.stack(cols, axis=1)            # (Nbig, 4) real matrix
    sv = np.linalg.svd(Mreal, compute_uv=False)
    scale = max(1.0, float(sv[0]) if sv.size else 1.0)
    rank = int(np.sum(sv > TOL * scale))
    surviving = 4 - rank
    # explicit real null space basis (the surviving H-linear directions).
    # Mreal is tall (Nbig x 4); full_matrices=False gives the full 4x4 right-singular
    # basis Vt (rows), whose trailing rows (zero singular value) span the null space.
    _, _, Vt = np.linalg.svd(Mreal, full_matrices=False)
    null_basis = Vt[rank:, :] if rank < 4 else np.zeros((0, 4))
    return surviving, rank, sv, null_basis


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=120)
    print("=" * 84)
    print("SELECTOR: quaternionic H-linearity  (commute with J, J^2=-1) on S=H^64")
    print("=" * 84)

    U, s, Jsq_err_full, Jcomm_err = fam.build_quaternionic_J()
    print(f"J = U.conj built: ||J^2+I||(full 128) = {Jsq_err_full:.2e} (=> J^2=-I, M(64,H)); "
          f"||[J, e_a]|| = {Jcomm_err:.2e} (=> J commutes with Clifford)")

    blocks_spec = {
        "S+ -> S-": (fam.BPLUS, fam.BMINUS),
        "S- -> S+": (fam.BMINUS, fam.BPLUS),
    }

    total_surviving = 0
    canon_ok_all = True
    imult_killed_all = True
    per_block = {}
    for bname, (Pin, Pout) in blocks_spec.items():
        A_in, jsq_in, leak_in = chiral_J(Pout, Pin, U)
        A_out, jsq_out, leak_out = chiral_J(Pin, Pout, U)

        Tc = block_slices(fam.W_delta_contract, Pin, Pout)   # GU canon contract channel
        Tw = block_slices(fam.W_wedge_metric, Pin, Pout)     # Rarita-Schwinger wedge

        surviving, rank, sv, null_basis = real_nullspace_dim(Tc, Tw, A_in, A_out)

        # canon shiab in this block = contract channel, REAL coeff: c1=1, c2=0  (p=(1,0,0,0))
        d_canon = hlinear_defect(1.0 + 0j, 0.0, Tc, Tw, A_in, A_out)
        canon_defect = float(np.max(np.abs(d_canon)))
        canon_ok = canon_defect < TOL
        canon_ok_all = canon_ok_all and canon_ok

        # i-multiple of canon = i*contract: c1 = i, c2 = 0  (p=(0,1,0,0)) -- expect KILLED
        d_imult = hlinear_defect(1j, 0.0, Tc, Tw, A_in, A_out)
        imult_defect = float(np.max(np.abs(d_imult)))
        imult_killed = imult_defect > TOL
        imult_killed_all = imult_killed_all and imult_killed

        total_surviving += surviving
        per_block[bname] = dict(surviving=surviving, rank=rank, sv=sv,
                                jsq_in=jsq_in, jsq_out=jsq_out,
                                leak_in=leak_in, leak_out=leak_out,
                                canon_defect=canon_defect, canon_ok=canon_ok,
                                imult_defect=imult_defect, imult_killed=imult_killed,
                                null_basis=null_basis)

        print("\n" + "-" * 84)
        print(f"BLOCK  {bname}")
        print("-" * 84)
        print(f"  J^2=-I chiral check: ||A_in conj(A_in)+I||={jsq_in:.2e}, "
              f"||A_out conj(A_out)+I||={jsq_out:.2e}")
        print(f"  J preserves chirality (no leak): leak_in={leak_in:.2e}, leak_out={leak_out:.2e}")
        print(f"  family dim this block (pre-selector): real 4  (c1,c2 in C: contract,wedge)")
        print(f"  H-linearity constraint singular values: "
              + np.array2string(sv, formatter={'float_kind': lambda x: f'{x:.2e}'}))
        print(f"  constraint rank = {rank}   ==> SURVIVING H-linear real dim = {surviving}")
        print(f"  GU canon contract shiab (c1=1 real, c2=0) H-linear? {canon_ok} "
              f"(defect={canon_defect:.2e})")
        print(f"  i*contract (c1=i) killed by selector? {imult_killed} "
              f"(defect={imult_defect:.2e})")

    print("\n" + "=" * 84)
    print("RESULT")
    print("=" * 84)
    print(f"  pre-selector REAL family dim (full Dirac)        = 8")
    print(f"  pre-selector COMPLEX family dim (full Dirac)     = 4")
    print(f"  SURVIVING H-linear REAL dim (full Dirac)         = {total_surviving}")
    print(f"  surviving per block (S+->S-, S-->S+)            = "
          + ", ".join(f"{b}:{r['surviving']}" for b, r in per_block.items()))
    print(f"  GU canon shiab survives in EVERY block?          = {canon_ok_all}")
    print(f"  i-multiples (quaternionic doubling) killed?      = {imult_killed_all}")
    print(f"  => selector cuts 8 -> {total_surviving} (real). Canon shiab retained; "
          f"NOT pinned to 1.")
    print("=" * 84)

    return dict(total_surviving=total_surviving, canon_ok_all=canon_ok_all,
                imult_killed_all=imult_killed_all, per_block=per_block,
                Jsq_err_full=Jsq_err_full, Jcomm_err=Jcomm_err)


if __name__ == "__main__":
    main()
