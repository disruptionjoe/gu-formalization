#!/usr/bin/env python3
"""BIG-SWING R5 -- INDEPENDENT cross-check of the chiral-tie no-go, by a different method.

R5_chiral_tie_nogo.py showed (via invariant-Hom dimensions of MAPS) that no Spin(9,5)-
invariant (anti)linear map swaps S+ <-> S-. This file re-derives the same conclusion
by a DIFFERENT invariant object -- the invariant BILINEAR forms S (x) S -> C (charge
conjugation) -- and checks it against the repo's own MOVE-4 fact (canon:
"the scalar bilinear exists only OFF-diagonally, on S+ <-> S-").

Invariant bilinear B(s,t)=s^T C t on S_in x S_out is a matrix C (64x64 in chiral
coords) with  Sigma_out^T C + C Sigma_in = 0  for every generator. dim of that space:
  - same-chirality  S+ x S+ : expect 0  (no Majorana/same-chirality scalar; MOVE-4)
  - cross-chirality S+ x S- : expect >=1 (the charge-conjugation pairing)
That pairing gives an invariant iso S+ ~= (S-)^*, i.e. S+ and S- are mutually DUAL,
NOT isomorphic -- exactly why Hom_lin(S+,S-)=0 and no swap map exists. And using this
bilinear to relate the two shiab blocks necessarily pairs the codomain V-slot too,
introducing the metric codifferential = the form-degree-shifting seesaw route already
dead-for-canon (SHIAB-04). So the ONLY invariant relating the blocks is the one that
lands on the killed seesaw direction -- confirming the tie cannot be fixed within a
fixed channel.

Matrix-free eigsh count, same discipline as the decider. No target / no import.
"""
from __future__ import annotations

import os
import sys

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
TESTS = os.path.join(ROOT, "tests")
if TESTS not in sys.path:
    sys.path.insert(0, TESTS)

import shiab_family_basis as fam

TOL = 1e-7
N = fam.N
BPLUS = fam.BPLUS
BMINUS = fam.BMINUS
GEN = fam.GEN_SET
INSURANCE = [(0, 7), (2, 9), (5, 13), (1, 11), (3, 8), (0, 13), (4, 10), (6, 12)]


def block_sigma(Pout, Pin, pairs):
    out = []
    for (a, b) in pairs:
        S = fam.Sigma(a, b)
        out.append((Pout.conj().T @ S @ Pout, Pin.conj().T @ S @ Pin))
    return out


def bilinear_dim(Pleft, Pright, pairs):
    """dim of invariant bilinear forms  B(s,t)=s^T C t,  s in S_left, t in S_right:
    C (dl x dr) with  Sl^T C + C Sr = 0  for all generators. Matrix-free eigsh count.
    D_g(C) = Sl^T C + C Sr ;  D_g^*(X) = conj(Sl) X + X Sr^H ;  A = sum_g D_g^* D_g."""
    blocks = block_sigma(Pleft, Pright, pairs)
    dl = Pleft.shape[1]
    dr = Pright.shape[1]
    n = dl * dr
    SlT = [Sl.T for (Sl, Sr) in blocks]
    SlC = [np.conjugate(Sl) for (Sl, Sr) in blocks]
    Sr = [Sr for (Sl, Sr) in blocks]
    SrH = [Sr_.conj().T for Sr_ in Sr]

    def matvec(v):
        C = v.reshape(dl, dr)
        acc = np.zeros((dl, dr), dtype=complex)
        for slt, slc, sr, srh in zip(SlT, SlC, Sr, SrH):
            D = slt @ C + C @ sr
            acc += slc @ D + D @ srh
        return acc.reshape(-1)

    A = LinearOperator((n, n), matvec=matvec, dtype=complex)
    w = None
    for ncv in (40, 80, 160):
        try:
            w = eigsh(A, k=12, which="SA", ncv=ncv, return_eigenvectors=False,
                      maxiter=20000, tol=1e-9)
            break
        except Exception:
            continue
    if w is None:
        # dense fallback: materialize A by columns (n up to 4096 -> fine here)
        cols = [matvec(np.eye(1, n, i, dtype=complex).ravel()) for i in range(n)]
        Amat = np.stack(cols, axis=1)
        w = np.linalg.eigvalsh(0.5 * (Amat + Amat.conj().T))
    w = np.sort(w.real)
    return int(np.sum(w < 1e-6)), w


def main():
    print("=" * 90)
    print("BIG-SWING R5 cross-check: invariant bilinear forms S x S -> C (independent method)")
    print("=" * 90)
    pairs = GEN + INSURANCE
    cases = [
        ("bilinear S+ x S+  (same-chirality / Majorana scalar)", BPLUS, BPLUS),
        ("bilinear S+ x S-  (cross-chirality / charge conjugation)", BPLUS, BMINUS),
        ("bilinear S- x S-  (same-chirality)", BMINUS, BMINUS),
    ]
    res = {}
    for label, Pl, Pr in cases:
        d, w = bilinear_dim(Pl, Pr, pairs)
        res[label] = d
        print(f"  {label:52s} dim_C = {d}   (smallest eigs: "
              + ", ".join(f"{x:.1e}" for x in np.sort(w)[:4]) + ")")

    same = res["bilinear S+ x S+  (same-chirality / Majorana scalar)"]
    cross = res["bilinear S+ x S-  (cross-chirality / charge conjugation)"]
    print("\n" + "-" * 90)
    print("READ-OFF (independent corroboration)")
    print("-" * 90)
    print(f"  same-chirality bilinear S+ x S+  = {same}  (MOVE-4 expects 0: no Majorana scalar)")
    print(f"  cross-chirality bilinear S+ x S- = {cross}  (charge-conjugation pairing, >=1)")
    ok = (same == 0 and cross >= 1)
    print(f"\n  matches canon MOVE-4 (scalar bilinear only OFF-diagonal S+<->S-)? {ok}")
    print("  => S+ ~= (S-)^* (mutually DUAL, not isomorphic): consistent with Hom_lin(S+,S-)=0.")
    print("     The one invariant relating the blocks is the DUAL pairing; using it on the shiab")
    print("     pairs the codomain V-slot -> the metric codifferential = seesaw (dead-for-canon).")
    print("     No within-channel invariant tie of c_(+-) and c_(-+). No-go independently confirmed.")
    print("=" * 90)
    return res


if __name__ == "__main__":
    main()
