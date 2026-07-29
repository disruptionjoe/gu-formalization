#!/usr/bin/env python3
r"""
THE VERTICAL-VEV CHIRALITY BRIDGE.

Decides the open bridge left by
explorations/layer0-pass-on-the-two-higgs-objects-2026-07-29.md, which returned
HOMONYM-WITH-NAMED-BRIDGE.

THE QUESTION.  SA-Y1's Higgs is the Lambda^0 carrier: dim Hom 1, OPPOSITE
chirality, the Dirac-Yukawa mass channel.  Weinstein's "the Higgs is an
illusion" object is the IG connection perturbation a in Omega^1(ad), which the
same channel table lists as Lambda^1: dim Hom 1, SAME chirality, "not a Lorentz
scalar."  Under 14D -> 4D, Lambda^1(V14) gives Lambda^1(V4) plus TEN 4D scalars
(the fibre directions), and 4D chirality is NOT 14D chirality.  So:

    does a VERTICAL (fibre-direction) vev of a supply a 4D
    OPPOSITE-chirality Dirac mass?

THE STRUCTURE BEING TESTED.  omega_14 = omega_4 . omega_10 up to phase, so 14D
chirality is the product of base and fibre chirality.  A 4D Dirac mass must
FLIP omega_4.  Clifford multiplication by a vertical vector anticommutes with
each of the FOUR horizontal gammas -- an even number -- so the parity argument
predicts it COMMUTES with omega_4 and therefore CANNOT be a 4D mass.  This
probe checks that against the explicit representation instead of trusting the
parity count.

DECLARED SPLIT (a choice, stated before computing): base (3,1) = indices
{0,1,2} from the plus block and {9} from the minus block; fibre (6,4) =
{3,...,8} plus {10,...,13}.  The result must depend only on the COUNTS, not on
which indices are chosen -- tested by permuting the assignment.

CONSTRUCTION FORK: program-native Cl(9,5) = M(64,H) carrier from the verified
in-repo representation.  No positive-Hilbert substitution.

Deterministic, foreground, numpy only, no writes, no network.
EXIT 0 = ran and all controls passed; the PRINTED findings are the result.
"""
from __future__ import annotations

import os
import sys
from itertools import combinations

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402

FAILURES: list[str] = []


def check(label: str, condition: bool) -> None:
    if condition:
        print(f"PASS: {label}")
    else:
        FAILURES.append(label)
        print(f"FAIL: {label}")


e = gb.gammas()
N = 14
DIM = e[0].shape[0]
I = np.eye(DIM, dtype=complex)

PLUS = list(range(9))     # eta = +1
MINUS = list(range(9, 14))  # eta = -1

# declared split, stated before computing
BASE = [0, 1, 2, 9]                       # (3,1)
FIBRE = [3, 4, 5, 6, 7, 8, 10, 11, 12, 13]  # (6,4)


def chirality(idx: list[int]) -> np.ndarray:
    """omega for a sub-block: the ordered product of its gammas."""
    out = I.copy()
    for a in sorted(idx):
        out = out @ e[a]
    return out


def commutes(A: np.ndarray, B: np.ndarray, tol: float = 1e-9) -> bool:
    return np.max(np.abs(A @ B - B @ A)) < tol


def anticommutes(A: np.ndarray, B: np.ndarray, tol: float = 1e-9) -> bool:
    return np.max(np.abs(A @ B + B @ A)) < tol


print("=" * 74)
print("VERTICAL-VEV CHIRALITY BRIDGE  --  can a fibre vev be a 4D Dirac mass?")
print("=" * 74)
print(f"  declared base (3,1) : {BASE}")
print(f"  declared fibre (6,4): {FIBRE}")

# ------------------------------------------------------- P1 Clifford sanity
print("\n[P1] Clifford relations on the verified representation")
ok_cliff = True
for a in range(N):
    for b in range(N):
        want = 2.0 * (1.0 if a < 9 else -1.0) * (1.0 if a == b else 0.0)
        got = e[a] @ e[b] + e[b] @ e[a]
        if np.max(np.abs(got - want * I)) > 1e-9:
            ok_cliff = False
check("gamma_a gamma_b + gamma_b gamma_a = 2 eta_ab", ok_cliff)

om4 = chirality(BASE)
om10 = chirality(FIBRE)
om14 = chirality(list(range(N)))
check("omega_14 = omega_4 . omega_10 up to phase",
      np.max(np.abs(om4 @ om10 - om14)) < 1e-9
      or np.max(np.abs(om4 @ om10 + om14)) < 1e-9)

# -------------------------------------------- THE CORE: what does a vev flip?
print("\n[CORE] does Clifford multiplication by each direction FLIP omega_4?")
base_flip = [a for a in BASE if anticommutes(e[a], om4)]
fibre_flip = [a for a in FIBRE if anticommutes(e[a], om4)]
fibre_pres = [a for a in FIBRE if commutes(e[a], om4)]

print(f"  base directions that FLIP omega_4  : {len(base_flip)}/4   {base_flip}")
print(f"  fibre directions that FLIP omega_4 : {len(fibre_flip)}/10")
print(f"  fibre directions that PRESERVE it  : {len(fibre_pres)}/10  {fibre_pres}")

check("every BASE direction flips omega_4 (would be a mass, breaks Lorentz)",
      len(base_flip) == 4)
check("every FIBRE direction PRESERVES omega_4", len(fibre_pres) == 10)

# ------------------------------------- the same question against omega_10
fibre_flip10 = [a for a in FIBRE if anticommutes(e[a], om10)]
print(f"\n  (cross-check) fibre directions flipping omega_10: {len(fibre_flip10)}/10")
check("fibre directions flip omega_10, hence flip omega_14",
      len(fibre_flip10) == 10)

# ---------------------------------------------- N1 split-choice independence
print("\n[N1] result must depend only on the COUNTS, not the index choice")
alt_splits = [
    ([0, 1, 3, 9], [2, 4, 5, 6, 7, 8, 10, 11, 12, 13]),
    ([5, 6, 7, 12], [0, 1, 2, 3, 4, 8, 9, 10, 11, 13]),
    ([2, 7, 8, 13], [0, 1, 3, 4, 5, 6, 9, 10, 11, 12]),
]
stable = True
for b, f in alt_splits:
    o4 = chirality(b)
    if not all(commutes(e[a], o4) for a in f):
        stable = False
check("fibre-preserves-omega_4 holds for every alternative split", stable)

# ------------------------------------------- N2 planted odd-size block control
print("\n[N2] a planted ODD-size base block must give the OPPOSITE behaviour")
odd_base = [0, 1, 2]              # 3 directions, odd
o3 = chirality(odd_base)
odd_others = [a for a in range(N) if a not in odd_base]
odd_flip = [a for a in odd_others if anticommutes(e[a], o3)]
check("with an odd-size base block, outside directions FLIP instead",
      len(odd_flip) == len(odd_others))
print(f"  odd base {odd_base}: {len(odd_flip)}/{len(odd_others)} outside dirs flip")
print("  -> confirms the effect is the EVEN-COUNT parity, not an artifact.")

# ----------------------------------------------------------------- verdict
print("\n" + "=" * 74)
if FAILURES:
    print(f"CONTROLS FAILED: {FAILURES}")
    print("RESULT: VOID.")
    sys.exit(1)

print("VERDICT: BRIDGE-FAILS")
print("=" * 74)
print(
    "\nA vertical (fibre-direction) vev PRESERVES 4D chirality, on every split\n"
    "tested.  A 4D Dirac mass must FLIP omega_4.  Therefore a vev of the IG\n"
    "connection perturbation in the fibre directions CANNOT supply the\n"
    "cross-chirality Dirac mass channel that SA-Y1 requires.\n"
    "\nThe mechanism is parity, not accident: a vertical gamma anticommutes with\n"
    "each of the FOUR base gammas, an even number, so it commutes with their\n"
    "product.  Control N2 confirms this by flipping the behaviour when the base\n"
    "block is given an ODD size.\n"
    "\nThe only directions that DO flip omega_4 are the four BASE directions --\n"
    "and a vev there breaks 4D Lorentz invariance, so that route is closed for\n"
    "a different and equally decisive reason."
)
print(
    "\nCONSEQUENCE FOR THE TERM-BY-TERM PASS.  The Layer-0 bridge is CLOSED\n"
    "NEGATIVE.  SA-Y1 stands as a genuine UNMET FORCED row, and T10 -- an\n"
    "explicit Lambda^0 Yukawa carrier -- IS REQUIRED.  Weinstein's Mexican-hat\n"
    "mechanism from ||F_A||^2 may still supply the POTENTIAL and the symmetry\n"
    "breaking; what this shows is that it does not, by the vertical-vev route,\n"
    "supply the fermion MASS channel."
)
print(
    "\nSCOPE.  This tests the Clifford/chirality obstruction only.  It does not\n"
    "exclude a mass arising through a composite operator, a derivative coupling,\n"
    "or the seesaw block structure Weinstein describes separately.  It closes\n"
    "one named route, which is what it was built to do."
)
