#!/usr/bin/env python3
"""BIG-SWING R5 (issuance bridge) -- why the OBVIOUS GU-native signed-readout map fails.

This is the CORROBORATING probe that motivates the decisive no-go in
R5_chiral_tie_nogo.py. A "signed-readout -> chiral-block-tie" selector needs a
Spin(9,5)-invariant antilinear structure that SWAPS the two chiral blocks S+ <-> S-
(so that requiring the shiab to respect it would force c_(-+) = eps * c_(+-)).

The natural GU-native antilinear structures on the Cl(9,5)=M(64,H) spinor are the
quaternionic J = U.conj (which Cl(9,5)=M(64,H) forces) and its chirality twist
omega.J. This file computes, from the verified representation, that BOTH are
Spin(9,5)-invariant antilinear maps but BOTH PRESERVE chirality (block-diagonal:
S+ -> S+, S- -> S-). Hence neither can tie the blocks. That is the concrete reason
the "obvious" construction fails, and it points to the general statement (no invariant
swap exists at all) proven in R5_chiral_tie_nogo.py.

No target imported; no cross-repo internals. Objects are omega and J from the family
module only.
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
TESTS = os.path.join(ROOT, "tests")
if TESTS not in sys.path:
    sys.path.insert(0, TESTS)

import shiab_family_basis as fam

TOL = 1e-7
N = fam.N
DIM = fam.DIM
OMEGA = fam.OMEGA


def antilinear_diag(Q, label):
    """Diagnostics for the antilinear map Theta(s) = Q conj(s):
    Spin-invariance, Theta^2 sign, and chirality behaviour (preserve vs swap)."""
    I = np.eye(DIM, dtype=complex)
    Pp = 0.5 * (I + OMEGA)
    Pm = 0.5 * (I - OMEGA)
    Th2 = Q @ np.conjugate(Q)
    # Spin invariance: Theta Sigma = Sigma Theta  <=>  Q conj(Sigma) = Sigma Q
    spin = 0.0
    for a in range(N):
        for b in range(a + 1, N):
            Sig = fam.Sigma(a, b)
            spin = max(spin, float(np.max(np.abs(Q @ np.conjugate(Sig) - Sig @ Q))))
    # chirality: as an antilinear op, Theta restricted to S+ has "matrix" A = Q conj(Pp)
    # acting on conj(s). Output in S- iff Pm A = A ; output in S+ iff Pp A = A.
    A_plus = Q @ np.conjugate(Pp)
    stay = float(np.max(np.abs(Pp @ A_plus - A_plus)))   # ~0 => S+ -> S+ (preserve)
    swap = float(np.max(np.abs(Pm @ A_plus - A_plus)))   # ~0 => S+ -> S- (swap)
    return {
        "label": label,
        "spin_invariance_err": spin,
        "theta_sq_plus_I": float(np.max(np.abs(Th2 + I))),
        "theta_sq_minus_I": float(np.max(np.abs(Th2 - I))),
        "chirality_preserve_err": stay,
        "chirality_swap_err": swap,
    }


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=120)
    print("=" * 90)
    print("BIG-SWING R5 probe: the natural GU-native antilinear maps and their chirality action")
    print("=" * 90)
    U, s, Jsq, Jcomm = fam.build_quaternionic_J()
    print(f"Cl(9,5)=M(64,H): ||J^2+I||={Jsq:.1e}, ||[J,Clifford]||={Jcomm:.1e}  (J = U.conj)")

    candidates = [
        (U, "J = U.conj                (quaternionic structure)"),
        (OMEGA @ U, "omega.J = (omega U).conj   (chirality-twisted)"),
    ]
    all_preserve = True
    any_swap = False
    for Q, label in candidates:
        d = antilinear_diag(Q, label)
        sq = "-I" if d["theta_sq_plus_I"] < TOL else ("+I" if d["theta_sq_minus_I"] < TOL else "?")
        preserves = d["chirality_preserve_err"] < TOL
        swaps = d["chirality_swap_err"] < TOL
        all_preserve = all_preserve and preserves
        any_swap = any_swap or swaps
        print("\n  " + label)
        print(f"    Spin(9,5)-invariant antilinear? defect = {d['spin_invariance_err']:.1e} "
              f"[{'YES' if d['spin_invariance_err'] < TOL else 'no'}]")
        print(f"    Theta^2 = {sq}")
        print(f"    chirality:  preserve-err = {d['chirality_preserve_err']:.1e}  "
              f"swap-err = {d['chirality_swap_err']:.1e}  "
              f"-> {'PRESERVES (block-diagonal)' if preserves else ('SWAPS' if swaps else 'mixed')}")

    print("\n" + "=" * 90)
    print("READ-OFF")
    print("=" * 90)
    print(f"  every natural GU-native antilinear map (J and omega.J) is Spin-invariant but")
    print(f"  chirality-PRESERVING: {all_preserve}.   any chirality SWAP found: {any_swap}.")
    print("  => the obvious 'signed-readout' operator does NOT tie the chiral blocks (it acts")
    print("     block-diagonally). Whether ANY invariant swap exists is settled in")
    print("     R5_chiral_tie_nogo.py (answer: none, linear or antilinear).")
    print("=" * 90)
    return {"all_preserve_chirality": all_preserve, "any_swap": any_swap}


if __name__ == "__main__":
    main()
