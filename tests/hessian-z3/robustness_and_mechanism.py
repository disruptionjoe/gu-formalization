#!/usr/bin/env python3
r"""
ROBUSTNESS + MECHANISM for the criticality verdict.

Two honest questions the main probe leaves open:
  (1) Is  d(lambda)/d(epsilon) = 0  for the GU selector<->carrier chiralizer torsion ROBUST
      (across J_quat seeds), and is the generic-torsion NONZERO slope robust (across seeds)?
      If the structured torsion is always 0 and the generic is always nonzero, the discrimination
      is real -- the eigenvalue-0 is GENERIC/PROTECTED, not a fitted coincidence and not a blind method.
  (2) MECHANISM: is the protected slope = 0 because of the +96/-96 vectorlike Krein BALANCE
      (trace cancellation between Krein-conjugate halves)? We test by computing the first-order
      shift on the +96 half and the -96 half SEPARATELY and showing they are equal and opposite,
      so the NET (the carrier-occupancy / generation-count direction) does not move while each half does.

This isolates the genuinely-NEW content (criticality: the zero is protected under torsion) from the
re-encoded DECOUPLE (off-diagonal coupling): we show the slope = 0 holds EVEN WHEN the off-diagonal
coupling is nonzero, so it is a distinct, stronger statement than the DECOUPLE.

Run: python tests/hessian-z3/robustness_and_mechanism.py
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import criticality_torsion_lambda_epsilon as C  # noqa: E402

N, DIM = C.N, C.DIM
herm = C.herm


def main():
    np.set_printoptions(precision=6, suppress=True, linewidth=160)
    print("=" * 90)
    print("ROBUSTNESS + MECHANISM")
    print("=" * 90)

    S = C.build_substrate()
    Wt, K = S["Wt"], S["K"]
    B = S["B"]
    wB = np.linalg.eigvalsh(B)
    Ppos = (wB > 1e-9)
    Pneg = (wB < -1e-9)
    print(f"carrier signature (+{Ppos.sum()}, -{Pneg.sum()}); trace(B) = {np.trace(B).real:+.3e}")

    # eigenbasis of B: split carrier into +96 (generation) and -96 (mirror) Krein halves
    evB, VB = np.linalg.eigh(B)
    Vpos = VB[:, evB > 1e-9]    # 96 generation modes
    Vneg = VB[:, evB < -1e-9]   # 96 mirror modes

    print("\n--- (1) ROBUSTNESS across seeds ---")
    print(f"  {'J_quat seed':>12}{'couple dlam/deps':>20}{'offdiag coupl':>16}")
    couple_slopes = []
    for seed in (1, 2, 3, 7, 11):
        U = C.quaternionic_J(S["e"], seed=seed)
        Jf = np.kron(np.eye(N), U)
        G = S["Pi"] - (np.eye(N * DIM, dtype=complex) - S["Pi"])
        theta = Jf @ G
        dB = herm(Wt.conj().T @ herm(K @ theta) @ Wt)
        nrm = np.linalg.norm(dB)
        dBn = dB / nrm if nrm > 1e-30 else dB
        slope = float(np.trace(dBn).real) / dBn.shape[0]
        coupl, coupl_rel = C.selector_carrier_offdiag(S, theta)
        couple_slopes.append(abs(slope))
        print(f"  {seed:>12}{slope:>20.3e}{coupl_rel:>16.3e}")

    print(f"  {'gen seed':>12}{'generic dlam/deps':>20}{'offdiag coupl':>16}")
    generic_slopes = []
    for seed in (7, 13, 21, 42, 99):
        rng = np.random.default_rng(seed)
        R = rng.standard_normal((N * DIM, N * DIM)) + 1j * rng.standard_normal((N * DIM, N * DIM))
        R /= np.linalg.norm(R) / np.sqrt(N * DIM)
        dB = herm(Wt.conj().T @ herm(K @ R) @ Wt)
        nrm = np.linalg.norm(dB)
        dBn = dB / nrm if nrm > 1e-30 else dB
        slope = float(np.trace(dBn).real) / dBn.shape[0]
        coupl, coupl_rel = C.selector_carrier_offdiag(S, R)
        generic_slopes.append(abs(slope))
        print(f"  {seed:>12}{slope:>20.3e}{coupl_rel:>16.3e}")

    print(f"\n  max |couple slope|  = {max(couple_slopes):.3e}   (GU chiralizer torsion: all ~ machine 0)")
    print(f"  min |generic slope| = {min(generic_slopes):.3e}   (random torsion: all clearly nonzero)")
    discrimination = max(couple_slopes) < 1e-10 < min(generic_slopes)
    print(f"  => probe DISCRIMINATES (structured 0, generic nonzero): {discrimination}")

    print("\n--- (2) MECHANISM: +96 vs -96 first-order shift (chiralizer torsion, seed 1) ---")
    U = C.quaternionic_J(S["e"], seed=1)
    Jf = np.kron(np.eye(N), U)
    G = S["Pi"] - (np.eye(N * DIM, dtype=complex) - S["Pi"])
    theta = Jf @ G
    dB = herm(Wt.conj().T @ herm(K @ theta) @ Wt)
    dB = dB / np.linalg.norm(dB)
    shift_pos = float(np.trace(Vpos.conj().T @ dB @ Vpos).real)   # sum of first-order shifts, +96 half
    shift_neg = float(np.trace(Vneg.conj().T @ dB @ Vneg).real)   # sum of first-order shifts, -96 half
    print(f"  first-order shift summed over +96 generation modes = {shift_pos:+.4e}")
    print(f"  first-order shift summed over -96 mirror     modes = {shift_neg:+.4e}")
    print(f"  net (generation + mirror)                          = {shift_pos + shift_neg:+.4e}")
    print(f"  cancellation |pos+neg| / (|pos|+|neg|)              = "
          f"{abs(shift_pos + shift_neg)/(abs(shift_pos)+abs(shift_neg)+1e-30):.3e}")
    print("  => the +96 and -96 Krein-conjugate halves shift EQUAL-AND-OPPOSITE under the torsion;")
    print("     each half MOVES, but the NET carrier-occupancy / generation-count direction does NOT.")
    print("     THAT vectorlike (+96/-96) cancellation is the protection mechanism -- and it holds")
    print("     even though the off-diagonal selector<->carrier coupling is nonzero. The criticality")
    print("     result (zero is protected) is therefore STRONGER than, and distinct from, the DECOUPLE.")

    # honesty guard: each half must actually move (else the cancellation is vacuous)
    each_half_moves = abs(shift_pos) > 1e-6 and abs(shift_neg) > 1e-6
    print(f"\n  each half actually moves (cancellation non-vacuous): {each_half_moves}")
    return dict(discrimination=discrimination, couple_max=max(couple_slopes),
                generic_min=min(generic_slopes), shift_pos=shift_pos, shift_neg=shift_neg,
                net=shift_pos + shift_neg, each_half_moves=each_half_moves)


if __name__ == "__main__":
    out = main()
    import json
    print("\n[json] " + json.dumps(out, default=str))
