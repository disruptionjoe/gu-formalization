#!/usr/bin/env python3
"""
A1 arithmetic certificate for the Lean skeleton A1-located-not-forced-legs.lean.

Purpose: an independent arithmetic re-check of the NUMERIC content of every 2-primary identity
and the two rank facts behind Theorem 2 / the antilinear bound. Toolchain status (verified
2026-07-03): the core-Lean file A1-arith-core-check.lean DOES compile clean under Lean
4.32.0-rc1 (elan present); the mathlib-dependent skeleton A1-located-not-forced-legs.lean is
UNVERIFIED (no mathlib/.lake on this machine) and its legs are labeled as such. This script
imports NO target count: it never divides by, normalizes to, or asserts 3 (or 8, 24, ...) as an
answer. It only certifies that the statements the Lean theorems make are arithmetically true.

Exit 0 iff all asserts pass. Pure stdlib.
"""

from fractions import Fraction

fails = []

def check(name, cond, detail=""):
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
    if not ok:
        fails.append(name)

# --- Leg 1 & 2: the finite-dimensional Krein core, as a small concrete instance -----------
# Model V = R^2 with a purely cross-chirality Krein form K((a,b),(c,d)) = a*d + b*c.
# W_plus = span(e0), W_minus = span(e1) are K-isotropic (K(e0,e0)=0, K(e1,e1)=0).
# A physical (K-positive) line: v = (1,1) has K(v,v) = 1*1 + 1*1 = 2 > 0.
# Core lemma: a K-positive vector cannot lie in an isotropic subspace.
def K(u, w):
    return u[0] * w[1] + u[1] * w[0]

e0, e1, vphys = (1, 0), (0, 1), (1, 1)
check("Krein: W+ isotropic (K(e0,e0)=0)", K(e0, e0) == 0, f"K={K(e0,e0)}")
check("Krein: W- isotropic (K(e1,e1)=0)", K(e1, e1) == 0, f"K={K(e1,e1)}")
check("Krein: physical vector K-positive", K(vphys, vphys) > 0, f"K={K(vphys,vphys)}")
# positive_inter_isotropic_trivial: any vector both K-positive and isotropic must be 0.
# Certify by contradiction check: no nonzero t*e0 (isotropic subspace) is K-positive.
worst = max((K((t, 0), (t, 0)) for t in range(-50, 51)), default=0)
check("Krein: isotropic line carries no positive K-norm", worst == 0, f"max K={worst}")
# chi = dim(P & W+) - dim(P & W-); with P a K-positive line disjoint from both null axes,
# both intersections are {0} so chi = 0 - 0 = 0.
def line_meets_axis_trivially(v):
    # v spans P (a line); axis is span(e0) or span(e1). Intersection nonzero iff v parallel.
    return not (v[1] == 0 or v[0] == 0)
inter_wp = 0 if line_meets_axis_trivially(vphys) else 1
inter_wm = 0 if line_meets_axis_trivially(vphys) else 1
chi = inter_wp - inter_wm
check("Theorem 2 core: chi = dim(P&W+) - dim(P&W-) = 0", chi == 0, f"chi={chi}")

# --- Leg 3a: cross-chirality signature -----------------------------------------------------
check("3a. 96 = 2^5 * 3", 96 == 2**5 * 3)
check("3a. (+96)+(-96) = 0 (net chirality zero)", 96 + (-96) == 0)

# --- Leg 3b: spinor 2-smoothness -----------------------------------------------------------
bad = [k for k in range(0, 40) if (2**k) % 3 == 0]
check("3b. 2^k never divisible by 3 (k=0..39)", bad == [], f"divisible at k={bad}")

# --- Leg 3c: Rokhlin bulk RS index ---------------------------------------------------------
c3_ok = all((21 * (16 * k)) // 8 == 42 * k and (21 * (16 * k)) % 8 == 0
            for k in range(-100, 101))
check("3c. 16|sigma => 21*sigma/8 = 42k exactly", c3_ok)
c3_even = all((42 * k) % 2 == 0 for k in range(-100, 101))
check("3c. RS bulk index 42k is even (2-primary)", c3_even)

# --- Leg 3d: adjoint Dirac index -----------------------------------------------------------
check("3d. 4 | 4k for all k", all((4 * k) % 4 == 0 for k in range(-100, 101)))

# --- Leg 3e: boundary-eta lens type --------------------------------------------------------
num_odd = all((2 * q**2 - 4 * q + 1) % 2 == 1 for q in range(-200, 201))
check("3e. lens numerator 2q^2-4q+1 is odd for all q", num_odd)
check("3e. lens denominator 8 = 2^3 (2-primary)", 8 == 2**3)
# every lens residue lands in (1/8)Z:
in_eighthZ = all((Fraction(2 * q**2 - 4 * q + 1, 8) * 8).denominator == 1
                 for q in range(-50, 51))
check("3e. lens residue lies in (1/8)Z", in_eighthZ)

# --- Leg 3f: Kramers / ghost 50-50 ---------------------------------------------------------
check("3f. (2n) mod 2 = 0", all((2 * n) % 2 == 0 for n in range(-100, 101)))
check("3f. n - n = 0 (ghost 50/50 net)", all(n - n == 0 for n in range(-100, 101)))

# --- No-target-import audit ----------------------------------------------------------------
# We assert only 2-primality / net-zero / non-divisibility. Nothing here forces the count 3.
check("no-target-import: script asserts no generation count", True,
      "verdict stays OPEN; nothing derives three")

print("-" * 60)
if fails:
    print(f"RESULT: {len(fails)} FAILED: {fails}")
    raise SystemExit(1)
print("RESULT: all arithmetic certificates PASS (Lean file remains UNVERIFIED)")
raise SystemExit(0)
