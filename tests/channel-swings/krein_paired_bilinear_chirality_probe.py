#!/usr/bin/env python3
r"""
KREIN-PAIRED BILINEAR CHIRALITY -- does pairing with K restore the 4D mass channel?

CORRECTS THE SCOPE of vertical_vev_chirality_bridge_probe.py.

That probe asked: does the OPERATOR e_vertical flip omega_4?  Answer: no.  But
the physical object is not the operator, it is the BILINEAR

    <Psi, M Psi>_K  =  Psi^dagger K M Psi

and a 4D Dirac mass requires the COMPOSITE K.M to be chirality-crossing, not M
alone.  GU's Krein form is documented as "purely cross-chirality" -- it pairs
E+ with E- -- so K may itself supply the flip that M lacks.  The earlier probe
never composed them.  That is a scope error in the question asked, not an
arithmetic error in what was computed.

PREDICTION FROM PARITY (stated before computing).  For products of distinct
gammas, e_A e_B = (-1)^(|A||B| - |A cap B|) e_B e_A.  With K_S a product of the
nine plus-gammas (|A|=9), omega_4 a product of four (|B|=4), overlapping in
three, the sign is (-1)^(36-3) = -1: K ANTICOMMUTES with omega_4.  Composing
with e_vertical (which commutes with omega_4) should then ANTICOMMUTE -- i.e.
the bilinear IS cross-chirality and the mass channel is restored.

If that confirms, the BRIDGE-FAILS verdict is WRONG and must be retracted.

Deterministic, foreground, numpy only, no writes, no network.
EXIT 0 = ran and all controls passed; the PRINTED findings are the result.
"""
from __future__ import annotations

import os
import sys

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
DIM = e[0].shape[0]
I = np.eye(DIM, dtype=complex)

BASE = [0, 1, 2, 9]
FIBRE = [3, 4, 5, 6, 7, 8, 10, 11, 12, 13]


def prod(idx):
    out = I.copy()
    for a in sorted(idx):
        out = out @ e[a]
    return out


def commutes(A, B, tol=1e-9):
    return np.max(np.abs(A @ B - B @ A)) < tol


def anticommutes(A, B, tol=1e-9):
    return np.max(np.abs(A @ B + B @ A)) < tol


def relation(A, B):
    if anticommutes(A, B):
        return "ANTICOMMUTES (flips)"
    if commutes(A, B):
        return "commutes (preserves)"
    return "NEITHER"


om4 = prod(BASE)
K_S = prod(range(9))          # the in-repo Krein operator: product of the 9 plus-gammas

print("=" * 74)
print("KREIN-PAIRED BILINEAR CHIRALITY  --  does K restore the 4D mass channel?")
print("=" * 74)

# --------------------------------------------------------- P1 K is a Krein form
print("\n[P1] the Krein operator")
print(f"  K_S = product of the nine plus-gammas;  K^2 = "
      f"{'+1' if np.allclose(K_S @ K_S, I) else '-1' if np.allclose(K_S @ K_S, -I) else '?'}")
check("K_S is invertible", abs(np.linalg.det(K_S)) > 1e-6)

# ------------------------------------------- CORE 1: does K itself flip omega_4?
print("\n[CORE 1] K vs omega_4  (the step the earlier probe never took)")
rel_K = relation(K_S, om4)
print(f"  K_S vs omega_4 : {rel_K}")
check("K ANTICOMMUTES with omega_4 (K is 4D-chirality-crossing)",
      anticommutes(K_S, om4))

# --------------------------------- CORE 2: the composite K.M for a fibre vev
print("\n[CORE 2] the BILINEAR operator K . e_a for each fibre direction")
cross = []
for a in FIBRE:
    M = e[a]
    KM = K_S @ M
    if anticommutes(KM, om4):
        cross.append(a)
print(f"  fibre directions whose K.e_a ANTICOMMUTES with omega_4 "
      f"(cross-chirality bilinear): {len(cross)}/10")
check("EVERY fibre direction gives a cross-chirality Krein bilinear",
      len(cross) == 10)

# ---------------------------------------------- contrast with the bare operator
print("\n[CONTRAST] bare operator vs Krein-paired bilinear")
bare_cross = [a for a in FIBRE if anticommutes(e[a], om4)]
print(f"  bare e_a  cross-chirality : {len(bare_cross)}/10   <- what the earlier probe measured")
print(f"  K . e_a   cross-chirality : {len(cross)}/10   <- what the mass term actually is")

# ------------------------------------------------------------ N1 base contrast
print("\n[N1] base directions must behave OPPOSITELY under the same composition")
base_cross_bare = [a for a in BASE if anticommutes(e[a], om4)]
base_cross_K = [a for a in BASE if anticommutes(K_S @ e[a], om4)]
print(f"  bare e_a (base): {len(base_cross_bare)}/4 cross;  "
      f"K.e_a (base): {len(base_cross_K)}/4 cross")
check("composition with K inverts the base/fibre pattern",
      len(base_cross_bare) == 4 and len(base_cross_K) == 0)

# --------------------------------------------- N2 planted non-Krein comparison
print("\n[N2] a planted identity pairing must NOT restore the channel")
planted = [a for a in FIBRE if anticommutes(I @ e[a], om4)]
check("identity pairing leaves fibre directions chirality-preserving",
      len(planted) == 0)

# --------------------------------------------------------- N3 split robustness
print("\n[N3] robustness across alternative base/fibre assignments")
alts = [([0, 1, 3, 9], [2, 4, 5, 6, 7, 8, 10, 11, 12, 13]),
        ([5, 6, 7, 12], [0, 1, 2, 3, 4, 8, 9, 10, 11, 13])]
robust = True
for b, f in alts:
    o = prod(b)
    if not all(anticommutes(K_S @ e[a], o) for a in f):
        robust = False
check("cross-chirality bilinear holds on alternative splits", robust)

# ----------------------------------------------------------------- verdict
print("\n" + "=" * 74)
if FAILURES:
    print(f"CONTROLS FAILED: {FAILURES}")
    print("RESULT: VOID.")
    sys.exit(1)

print("VERDICT: BRIDGE-SUCCEEDS  (the earlier BRIDGE-FAILS verdict is WRONG)")
print("=" * 74)
print(
    "\nThe Krein form is itself 4D-chirality-crossing: K ANTICOMMUTES with\n"
    "omega_4.  So although the bare operator e_vertical PRESERVES omega_4, the\n"
    "bilinear <Psi, e_vertical Psi>_K -- which is what a mass term actually is --\n"
    "is CROSS-CHIRALITY, on all ten fibre directions and on every split tested.\n"
    "\nThe earlier probe measured the wrong object.  Its arithmetic was correct;\n"
    "the question was wrong.  A mass term is a BILINEAR, and in a Krein setting\n"
    "the pairing carries chirality structure of its own.\n"
    "\nControl N1 shows the composition INVERTS the pattern: the base directions,\n"
    "which flip omega_4 bare, become chirality-PRESERVING once paired with K.\n"
    "So the Krein form does not trivially flip everything -- it exchanges the two\n"
    "classes, which is exactly what a cross-chirality pairing should do."
)
print(
    "\nCONSEQUENCE.  T10 is NOT established as required.  A vertical vev of the IG\n"
    "connection perturbation CAN supply a cross-chirality mass bilinear in the\n"
    "Krein setting.  Weinstein's 'minimal coupling and Yukawa coupling are the\n"
    "same thing' survives this test rather than failing it.\n"
    "\nWHAT IS STILL NOT SHOWN: that the resulting mass is Lorentz-invariant in 4D,\n"
    "that it lands in the Lambda^0 channel SA-Y1 names rather than merely being\n"
    "cross-chirality, that it is nonzero, or that its magnitude is anything in\n"
    "particular.  Cross-chirality is necessary, not sufficient."
)
