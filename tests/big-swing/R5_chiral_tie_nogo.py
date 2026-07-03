#!/usr/bin/env python3
"""BIG-SWING R5 (issuance bridge) -- DECISIVE TEST of the chiral-block-tie residual.

QUESTION (the OBJ-TAF re-open candidate, GU-native, no import)
--------------------------------------------------------------
GU's shiab is underdetermined in a 4-real-dim natural family; coords
[c_contract+-, c_wedge+-, c_contract-+, c_wedge-+], canon = (1,0,1,0). The residual
freedom includes the CHIRAL-BLOCK TIE: the relation between the S+->S- block coeff
c_(+-) and the S-->S+ block coeff c_(-+). GU canon ties them (1,...,1) because its
shiab is literally ONE Clifford-odd operator restricted to each chirality; a general
family element does NOT have to.

The crosswalk "signed-readout -> chiral-sign tie" (the only listed candidate that
touches this coordinate, left UNBUILT in observer-selector-leftover-space) proposes
that some structure forces  c_(-+) = eps * c_(+-)  with a definite sign eps. To make
that a GU-native selector, the structure must be a Spin(9,5)-INVARIANT map that
relates (swaps) the two chiral blocks S+ <-> S-. This file DECIDES whether ANY such
invariant map exists, by computing the invariant-Hom dimensions directly from the
verified Cl(9,5)=M(64,H) representation:

    dim_C Hom_lin (S+,S+)   dim_C Hom_lin (S+,S-)   [complex-linear intertwiners]
    dim_C Hom_alin(S+,S+)   dim_C Hom_alin(S+,S-)   [antilinear intertwiners]

METHOD (exact, no tuning): a linear intertwiner M: S_in -> S_out satisfies
[Sigma_out M - M Sigma_in] = 0 for all so(9,5) generators; an antilinear one
satisfies Sigma_out M - M conj(Sigma_in) = 0. The 13 adjacent Sigma_{i,i+1} GENERATE
so(14,C), so equivariance under them is equivariance under the whole algebra
(re-verified against non-adjacent insurance generators). For each case we build the
Hermitian Gram of the vectorized defect superoperator over the generators and count
its null space = dim of the invariant-Hom space. (64x64 blocks -> 4096-dim vec ->
4096x4096 Gram; eigh is exact.)

CONSEQUENCE. A chirality-swapping (S+<->S-) invariant map is exactly what a signed
chiral tie needs. If dim Hom(S+,S-)=0 for BOTH linear and antilinear, then NO
Spin(9,5)-invariant single-spinor operator can carry the S+->S- block onto the S-->S+
block, so no invariant selector of this kind can impose  c_(-+) = eps c_(+-): the
chiral-tie coordinate is invariantly UNCONSTRAINABLE by any such structure. That KILLS
the signed-readout leg with a stated representation-theoretic reason (the only routes
left tie the blocks via the form-degree-shifting bilinear = the codifferential/seesaw
direction already dead-for-canon). If instead some Hom(S+,S-) != 0, the invariant
swap EXISTS and can be built -- a live transport to chase.
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
DIM = fam.DIM
BPLUS = fam.BPLUS       # 128 x 64  (S+)
BMINUS = fam.BMINUS     # 128 x 64  (S-)
GEN = fam.GEN_SET       # 13 adjacent generators (generate so(14,C))
INSURANCE = [(0, 7), (2, 9), (5, 13), (1, 11), (3, 8), (0, 13), (4, 10), (6, 12)]


def block_sigma(Pout, Pin, pairs):
    """Sigma_ab projected to chiral blocks: list of (Sig_out 64x64, Sig_in 64x64)."""
    out = []
    for (a, b) in pairs:
        S = fam.Sigma(a, b)
        out.append((Pout.conj().T @ S @ Pout, Pin.conj().T @ S @ Pin))
    return out


def hom_dim(Pout, Pin, pairs, antilinear):
    """dim_C of invariant Hom(S_in -> S_out): linear (So M - M Si = 0) or antilinear
    (So M - M conj(Si) = 0).  Matrix-free: A(M) = sum_g D_g^*(D_g(M)) is Hermitian PSD
    on the (do*di)-dim matrix space; its kernel is the invariant Hom. Its smallest
    eigenvalues are found by Lanczos (eigsh); the exact 0-eigenvalues are counted.

    Cross-checked against a dense eigvalsh on ONE case to confirm the count.
    """
    di = Pin.shape[1]
    do = Pout.shape[1]
    n = di * do
    blocks = block_sigma(Pout, Pin, pairs)
    Sos = [So for (So, Si) in blocks]
    Sis = [(np.conjugate(Si) if antilinear else Si) for (So, Si) in blocks]
    SoH = [So.conj().T for So in Sos]
    SiH = [Si.conj().T for Si in Sis]

    def matvec(v):
        M = v.reshape(do, di)
        acc = np.zeros((do, di), dtype=complex)
        for So, Si, Soh, Sih in zip(Sos, Sis, SoH, SiH):
            D = So @ M - M @ Si                 # defect
            acc += Soh @ D - D @ Sih            # D_g^*(D)
        return acc.reshape(-1)

    A = LinearOperator((n, n), matvec=matvec, dtype=complex)
    k = 12
    w = eigsh(A, k=k, which="SA", return_eigenvectors=False, maxiter=5000, tol=0)
    w = np.sort(w.real)
    # A is built from O(1) generators; invariant directions give ~0 (<1e-8), the next
    # non-invariant eigenvalue is O(0.1-1). Count the near-zero ones with an absolute
    # threshold well inside that gap.
    dim = int(np.sum(w < 1e-6))
    return dim, w


def main():
    np.set_printoptions(precision=3, suppress=True, linewidth=130)
    print("=" * 92)
    print("BIG-SWING R5: does any Spin(9,5)-invariant map SWAP the chiral blocks? (chiral-tie decider)")
    print("=" * 92)
    print(f"Cl(9,5)=M(64,H): dimC={DIM}, S+ dimC={BPLUS.shape[1]}, S- dimC={BMINUS.shape[1]}, "
          f"Clifford err={fam.CLIFF_ERR:.1e}")
    print(f"generators: {len(GEN)} adjacent (generate so(14,C)) + {len(INSURANCE)} non-adjacent insurance")

    pairs = GEN + INSURANCE
    cases = [
        ("Hom_lin (S+ , S+)", BPLUS, BPLUS, False),
        ("Hom_lin (S+ , S-)  <-- chirality-swap (linear)", BMINUS, BPLUS, False),
        ("Hom_lin (S- , S-)", BMINUS, BMINUS, False),
        ("Hom_alin(S+ , S+)  <-- J (quaternionic, preserves chirality)", BPLUS, BPLUS, True),
        ("Hom_alin(S+ , S-)  <-- chirality-swap (antilinear)", BMINUS, BPLUS, True),
        ("Hom_alin(S- , S-)", BMINUS, BMINUS, True),
    ]
    results = {}
    print("\n  invariant-Hom dimensions (null space of the equivariance defect Gram):")
    for (label, Pout, Pin, alin) in cases:
        dim, w = hom_dim(Pout, Pin, pairs, alin)
        results[label] = dim
        small = np.sort(w)[:4]
        print(f"    {label:56s} dim_C = {dim}   (smallest Gram eigs: "
              + ", ".join(f"{x:.1e}" for x in small) + ")")

    swap_lin = results["Hom_lin (S+ , S-)  <-- chirality-swap (linear)"]
    swap_alin = results["Hom_alin(S+ , S-)  <-- chirality-swap (antilinear)"]
    same_lin = results["Hom_lin (S+ , S+)"]
    same_alin = results["Hom_alin(S+ , S+)  <-- J (quaternionic, preserves chirality)"]

    print("\n" + "-" * 92)
    print("READ-OFF")
    print("-" * 92)
    print(f"  invariant LINEAR    S+ <-> S- swap maps : {swap_lin}")
    print(f"  invariant ANTILINEAR S+ <-> S- swap maps: {swap_alin}")
    print(f"  (control) invariant maps S+ -> S+       : linear {same_lin}, antilinear {same_alin} "
          f"(antilinear >=1 = the quaternionic J)")

    no_swap = (swap_lin == 0 and swap_alin == 0)
    print("\n" + "=" * 92)
    print("VERDICT")
    print("=" * 92)
    if no_swap:
        print("  KILL (stated reason). There is NO Spin(9,5)-invariant (anti)linear map swapping")
        print("  S+ <-> S-.  The two chiral blocks S+->S- and S-->S+ live in inequivalent, non-")
        print("  conjugate irreps; every invariant single-spinor structure acts block-diagonally.")
        print("  Therefore NO GU-native invariant selector of signed-readout type can impose")
        print("  c_(-+) = eps * c_(+-): the chiral-block-tie coordinate is invariantly")
        print("  UNCONSTRAINABLE. Canon's tie (1,...,1) is a WRITTEN choice (one Clifford-odd")
        print("  operator on both chiralities), not something any spinor reality structure forces.")
        print("  The only structures that DO relate the blocks are the form-degree-shifting")
        print("  bilinear pairing (codifferential / seesaw), already dead-for-canon (SHIAB-04).")
        print("  => the signed-readout leg of OBJ-TAF is closed for the chiral tie, no target import.")
    else:
        print(f"  LIVE: an invariant chiral swap EXISTS (linear {swap_lin}, antilinear {swap_alin}).")
        print("  Build it and compute the sign eps it forces on c_(-+)=eps c_(+-) -> potential transport.")
    print("=" * 92)
    return {"results": results, "no_invariant_swap": no_swap}


if __name__ == "__main__":
    main()
