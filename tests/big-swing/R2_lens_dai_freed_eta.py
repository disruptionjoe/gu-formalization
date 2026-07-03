#!/usr/bin/env python3
# R2 BIG SWING -- corroborating Dai-Freed eta toy on a genuine Z_3 bordism class.
# ============================================================================================
# The companion certificate R2_spin_bordism_mod3.py proved STRUCTURALLY that Omega^Spin_5(B G_SM)
# has no 3-torsion (the SM mod-3 Dai-Freed arena is empty). Here we CONFIRM the same verdict from a
# completely independent, concrete direction: an actual eta-invariant / APS rho-invariant on a
# manifold that DOES carry a Z_3 (the lens space L(3;1,1) = S^3/Z_3), coupling the whole SM chiral
# content to the flat Z_3 <= U(1)_Y Wilson line, and reading whether the SM boundary data produces a
# nonzero mod-3 phase (=> would pin the count) or exactly zero (=> does not).
#
# THE OBJECT. Reduced eta of the twisted Dirac operator on L(p;1,1), character a (Atiyah-Patodi-
# Singer / Donnelly):
#     xi_a = (1/p) * sum_{j=1..p-1}  zeta^{a j} / ( 2i sin(pi j / p) )^2 ,   zeta = e^{2 pi i / p}.
# It is real and rational (a lens-space rho invariant). We compute it numerically at high precision
# and rationalize, and we VALIDATE it by the internal identity  sum_a xi_a = 0  (the p characters
# reassemble the eta of the p-fold cover S^3, which is 0).
#
# THE GRAVITATIONAL SUBTLETY (handled honestly). xi_0 is the untwisted (pure-gravity) piece. Because
# Omega^Spin_3(pt) = 0, L(3;1,1) BOUNDS as a spin manifold, so the pure-gravity eta xi_0 is NOT an
# anomaly -- it is removable by a local gravitational counterterm. The genuine flat-bundle (gauge)
# Dai-Freed invariant is therefore the reference-subtracted rho_a = xi_a - xi_0, valued in (1/p)Z.
#
# THE SM ASSEMBLY. Each left-handed Weyl fermion of hypercharge Y6 (integer, = 6*Y) couples to the
# flat Z_3 <= U(1)_Y with character a = Y6 mod 3, contributing rho_{a}. The total mod-3 phase of one
# generation is  Theta = sum_fields rho_{Y6 mod 3} = sum_a mult_a * rho_a.
#     If Theta != 0 mod Z: n generations give n*Theta; cancellation forces a constraint on n mod 3
#         -> the count would be PINNED mod 3.  If Theta = 0 mod Z: NO constraint -> NOT pinned.
#
# ROBUST BACKBONE (normalization-independent, exact integer arithmetic). rho_a in (1/3)Z, so
# Theta = sum_a mult_a * rho_a is an integer AS SOON AS every nonzero-charge multiplicity mult_a is
# divisible by 3. We compute the SM's (mult_0, mult_1, mult_2) and find (3or4, 6, 6): the charged
# classes have multiplicity 6 == 0 mod 3. This is COLOR TRIALITY -- every colored multiplet arrives
# in 3 colors, so its count is a multiple of 3 -- which is the SAME fact the structural certificate
# saw as "3-locally B G_SM ~ BU(3), the Z_3 is color triality." The mod-3 phase vanishes for ANY spin
# structure / normalization convention, because it is killed by an integer divisibility, not by a
# fitted number.
#
# NO TARGET IMPORT: 3 is the order of the torsion arena we probe; we never assume 3 generations,
# never divide by 3 to get an answer, never use chi=24 / /8 / Ahat=3. The verdict is READ OFF.
# ============================================================================================
import numpy as np
from fractions import Fraction

NA = 0
def check(c, m):
    global NA; NA += 1
    assert c, "FAIL: " + m

def rationalize(x, maxden=10000):
    return Fraction(x).limit_denominator(maxden)

# ------------------------------------------------------------------------------------------
# (1) Reduced eta xi_a on L(p;1,1) via the APS/Donnelly trig sum.  Compute for several p, validate.
# ------------------------------------------------------------------------------------------
def xi_lens(p, a):
    """Reduced eta of twisted Dirac on L(p;1,1), character a, as an exact Fraction (rationalized)."""
    s = 0.0 + 0.0j
    for j in range(1, p):
        denom = (2j * np.sin(np.pi * j / p)) ** 2       # (2 i sin)^2 = -4 sin^2  (real, negative)
        s += np.exp(2j * np.pi * a * j / p) / denom
    val = (s / p)
    check(abs(val.imag) < 1e-9, "xi_%d on L(%d;1,1) must be REAL (got imag %.2e)" % (a, p, val.imag))
    return rationalize(val.real)

print("=" * 94)
print("(1) Reduced eta xi_a on L(p;1,1): real, rational, and sum_a xi_a = 0 (internal validation).")
print("=" * 94)
for p in [2, 3, 5, 7]:
    xis = [xi_lens(p, a) for a in range(p)]
    tot = sum(xis, Fraction(0))
    print("  p=%d:  xi_a = %s   sum_a xi_a = %s" % (p, [str(x) for x in xis], tot))
    check(tot == 0, "sum_a xi_a must be 0 on L(%d;1,1) (p-fold cover S^3 has eta 0)" % p)

# ------------------------------------------------------------------------------------------
# (2) p=3: gauge (reference-subtracted) rho invariant rho_a = xi_a - xi_0, valued in (1/3)Z.
# ------------------------------------------------------------------------------------------
p = 3
xi = [xi_lens(p, a) for a in range(p)]
rho = [xi[a] - xi[0] for a in range(p)]
print()
print("=" * 94)
print("(2) p=3 gauge rho invariant  rho_a = xi_a - xi_0  (xi_0 = pure gravity = local counterterm,")
print("    since Omega^Spin_3(pt)=0 => L(3;1,1) bounds => no gravitational anomaly).")
print("=" * 94)
print("  xi  = %s" % [str(x) for x in xi])
print("  rho = %s   (rho_0=0; charged rho in (1/3)Z)" % [str(x) for x in rho])
check(rho[0] == 0, "rho_0 must be 0")
for a in (1, 2):
    check(rho[a].denominator == 3, "rho_%d must live in (1/3)Z (denominator 3), got %s" % (a, rho[a]))

# ------------------------------------------------------------------------------------------
# (3) SM one-generation content: left-handed Weyl fermions, integer hypercharge Y6 = 6*Y.
#     (field, Y6, multiplicity=#color x #weak Weyl components)
# ------------------------------------------------------------------------------------------
SM = [
    ("Q  (quark doublet, 3 color x 2 weak)", 1, 6),
    ("u^c (anti-up,       3 color)",        -4, 3),
    ("d^c (anti-down,     3 color)",         2, 3),
    ("L  (lepton doublet, 2 weak)",         -3, 2),
    ("e^c (positron,      singlet)",         6, 1),
]
SM_with_nu = SM + [("nu^c (right neutrino, singlet)", 0, 1)]

def local_anomaly_check(content):
    grav = sum(m * Y6 for (_, Y6, m) in content)   # mixed grav-U(1)_Y : sum Y  (=0)
    cubic = sum(m * Y6 ** 3 for (_, Y6, m) in content)   # U(1)_Y^3 : sum Y^3  (=0)
    return grav, cubic

def mult_by_class(content):
    mult = {0: 0, 1: 0, 2: 0}
    for (_, Y6, m) in content:
        mult[Y6 % 3] += m
    return mult

def theta(content):
    return sum(mult_by_class(content)[a] * rho[a] for a in range(3))

print()
print("=" * 94)
print("(3) SM one generation coupled to the flat Z_3 <= U(1)_Y on L(3;1,1).")
print("=" * 94)
for label, content in [("no nu^c (15 Weyl)", SM), ("with nu^c (16 Weyl)", SM_with_nu)]:
    g, c = local_anomaly_check(content)
    check(g == 0, "SM %s: mixed grav-U(1)_Y anomaly sum Y must be 0 (got %d)" % (label, g))
    check(c == 0, "SM %s: U(1)_Y^3 anomaly sum Y^3 must be 0 (got %d)" % (label, c))
    mult = mult_by_class(content)
    Th = theta(content)
    print("  %-20s  local anomalies (sumY, sumY^3) = (%d, %d)  [anomaly-free]" % (label, g, c))
    print("      Weyl multiplicity by hypercharge class mod 3: mult_0=%d mult_1=%d mult_2=%d"
          % (mult[0], mult[1], mult[2]))
    print("      => mod-3 Dai-Freed phase  Theta = sum_a mult_a rho_a = %s   (== 0 mod Z: %s)"
          % (Th, Th.denominator == 1))
    check(Th.denominator == 1, "SM %s: Theta must be an INTEGER => mod-3 phase 0 => count NOT pinned" % label)
    # robustness: the charged-class multiplicities are divisible by 3 (color triality), so Theta in Z
    # for ANY rho in (1/3)Z -- independent of the eta normalization/spin-structure convention.
    check(mult[1] % 3 == 0 and mult[2] % 3 == 0,
          "SM %s: charged-class Weyl multiplicities must be divisible by 3 (color triality)" % label)

# ------------------------------------------------------------------------------------------
# (4) NON-VACUITY: contents that DO carry a nonzero mod-3 phase (the toy is not trivially zero).
# ------------------------------------------------------------------------------------------
print()
print("=" * 94)
print("(4) NON-VACUITY: the eta toy CAN be nonzero mod 3 (so 'SM gives 0' is a real measurement).")
print("=" * 94)
bare      = [("single charge-1 Weyl", 1, 1)]                                  # locally anomalous
one_color = [("charge-1", 1, 1), ("charge-1", 1, 1)]                          # mult_1 = 2, not /3
Th_bare = theta(bare); Th_one = theta(one_color)
print("  single charge-1 Weyl:            mult=%s  Theta = %s  (nonzero mod Z: %s)"
      % (mult_by_class(bare), Th_bare, Th_bare.denominator != 1))
print("  two charge-1 Weyls (mult_1=2):   mult=%s  Theta = %s  (nonzero mod Z: %s)"
      % (mult_by_class(one_color), Th_one, Th_one.denominator != 1))
check(Th_bare.denominator != 1, "a single charged Weyl MUST give a nonzero mod-3 phase (non-vacuity)")
check(Th_one.denominator != 1, "mult not divisible by 3 MUST give nonzero mod-3 phase (non-vacuity)")

print()
print("#" * 94)
print("# VERDICT (R2 eta toy): CONFIRMS the structural certificate from the concrete eta side.")
print("#  The SM one-generation chiral content, coupled to the flat Z_3 <= U(1)_Y on the genuine")
print("#  Z_3-carrying bordism class L(3;1,1), produces mod-3 Dai-Freed phase Theta = 0 (INTEGER),")
print("#  for both 15- and 16-Weyl content, for ANY eta normalization -- because the charged-class")
print("#  Weyl multiplicities are 6, 6 (== 0 mod 3): COLOR TRIALITY. n generations give n*0 = 0:")
print("#  the count is NOT pinned mod 3.  This is the same triality mechanism the structural")
print("#  certificate saw as Omega^Spin_5(B G_SM) having no 3-torsion (3-locally B G_SM ~ BU(3)).")
print("#  Non-vacuity: a bare charged Weyl gives Theta = 1/3 != 0, so the toy can detect a mod-3 pin.")
print("#  Dimension note (honest): L(3;1,1) is 3-dim (directly a 2D-theory Dai-Freed test); the 4D")
print("#  SM lives on 5-manifolds -- but the triality/divisibility mechanism is dimension-independent")
print("#  and the rigorous 4D statement is the Omega^Spin_5 certificate. NO target imported.")
print("#  hard asserts passed: %d" % NA)
print("#" * 94)
