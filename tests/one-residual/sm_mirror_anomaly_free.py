#!/usr/bin/env python3
"""
One Residual paper -- Sec 2.1 re-land as a reproducible test.

CLAIM (existence/theorem grade): the forced mirror generation is VECTORLIKE and
ANOMALY-FREE. Concretely, one SM generation = the 16 of so(10) (a full generation
plus a right-handed neutrino). All four Standard-Model anomaly coefficients vanish:

    Tr Y            (U(1)_Y - gravity / U(1) linear)
    Tr Y^3          (U(1)_Y^3)
    Tr(Y * T2^2)    (U(1)_Y - SU(2)_L^2)
    Tr(Y * C^2)     (U(1)_Y - SU(3)_c^2)

Umbrella: so(10) has no independent cubic Casimir (its symmetric d-symbol vanishes
for the 16), so the whole generation is automatically anomaly-free; the four SM
channels above are the concrete SM-decomposed instantiation of that statement.

Vectorlike: the mirror is 16 (+) 16bar, so n_L - n_R = 0 identically.

REAL computation: we enumerate all 16 left-handed Weyl states of one generation
with their exact (Y, T3, color-Cartan) charges using sympy Rational (no floats,
no hardcoded answers) and sum the anomaly traces. Every trace must be EXACTLY 0.

Exit 0 iff all checks are exact zeros.
"""

import sys
from sympy import Rational as R, Integer

# ---------------------------------------------------------------------------
# Build the 16 left-handed Weyl states of one SM generation (= 16 of so(10)).
#
# Each state carries:
#   Y   : weak hypercharge (Gell-Mann-Nishijima Q = T3 + Y)
#   T3  : third weak-isospin component (SU(2)_L Cartan eigenvalue)
#   Cc  : an SU(3)_c Cartan eigenvalue (we use diag(1/2, -1/2, 0) on a color
#         triplet; sum over a triplet of Cc^2 = 1/2 = the fundamental index)
#
# Multiplet content of one generation:
#   Q  = (u,d)_L : color triplet, SU(2) doublet, Y=+1/6   -> 6 states
#   u^c          : color (anti)triplet, singlet, Y=-2/3   -> 3 states
#   d^c          : color (anti)triplet, singlet, Y=+1/3   -> 3 states
#   L  = (nu,e)_L: color singlet, SU(2) doublet, Y=-1/2   -> 2 states
#   e^c          : singlet, Y=+1                          -> 1 state
#   nu^c         : singlet, Y=0  (the 16th of so(10))     -> 1 state
# Total: 6+3+3+2+1+1 = 16.
# ---------------------------------------------------------------------------

COLOR_CARTAN = [R(1, 2), R(-1, 2), R(0)]   # SU(3) Cartan diag on a triplet
ISO_CARTAN   = [R(1, 2), R(-1, 2)]          # SU(2) T3 on a doublet

states = []  # list of dicts: Y, T3, Cc

def add_multiplet(Y, iso_doublet, color_triplet):
    t3_vals = ISO_CARTAN if iso_doublet else [R(0)]
    cc_vals = COLOR_CARTAN if color_triplet else [R(0)]
    for t3 in t3_vals:
        for cc in cc_vals:
            states.append({"Y": R(Y), "T3": t3, "Cc": cc,
                           "iso": iso_doublet, "col": color_triplet})

# Y passed as (num, den) via R() -> use sympy Rational directly
add_multiplet(R(1, 6),  iso_doublet=True,  color_triplet=True)   # Q
add_multiplet(R(-2, 3), iso_doublet=False, color_triplet=True)   # u^c
add_multiplet(R(1, 3),  iso_doublet=False, color_triplet=True)   # d^c
add_multiplet(R(-1, 2), iso_doublet=True,  color_triplet=False)  # L
add_multiplet(R(1),     iso_doublet=False, color_triplet=False)  # e^c
add_multiplet(R(0),     iso_doublet=False, color_triplet=False)  # nu^c

# ---------------------------------------------------------------------------
# Structural sanity: exactly 16 states.
# ---------------------------------------------------------------------------
n_states = len(states)

# ---------------------------------------------------------------------------
# Anomaly traces (exact rational sums over all 16 states).
#   For the mixed SU(2)^2 and SU(3)^2 channels the trace uses a single Cartan
#   generator squared; summing over a full multiplet reproduces the group index.
# ---------------------------------------------------------------------------
tr_Y     = sum(s["Y"] for s in states)
tr_Y3    = sum(s["Y"]**3 for s in states)
tr_Y_T2  = sum(s["Y"] * s["T3"]**2 for s in states)
tr_Y_C2  = sum(s["Y"] * s["Cc"]**2 for s in states)

# Vectorlike-ness (16 (+) 16bar) and the so(10)-cubic-Casimir umbrella are NOT asserted here --
# they are computed for real in tests/one-residual/sm_so10_cubic_casimir_and_mirror.py (the 16bar is
# the genuine charge-conjugate by the full 5-Cartan weight system; the so(10) cubic Casimir vanishes on
# the 16). This test establishes only the four SM anomaly TRACES for one generation.

# ---------------------------------------------------------------------------
# Report.
# ---------------------------------------------------------------------------
checks = []
def check(name, value, target=Integer(0)):
    ok = (value == target)
    checks.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name:22s} = {value!s:>6}  (expect {target})")

print("=== SM one-generation anomaly traces (16 of so(10)) ===")
print(f"[{'PASS' if n_states == 16 else 'FAIL'}] state count           = {n_states:>6}  (expect 16)")
checks.append(n_states == 16)
check("Tr Y",          tr_Y)
check("Tr Y^3",        tr_Y3)
check("Tr(Y * T2^2)",  tr_Y_T2)
check("Tr(Y * C^2)",   tr_Y_C2)

all_ok = all(checks)
print("-" * 60)
print("RESULT:", "PASS -- all four SM anomaly traces vanish for one generation "
      "(vectorlike / so(10)-cubic-Casimir computed in sm_so10_cubic_casimir_and_mirror.py)"
      if all_ok else "FAIL")
sys.exit(0 if all_ok else 1)
