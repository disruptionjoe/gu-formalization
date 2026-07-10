#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
HOSTILE-REFEREE independent re-derivation for LEG-1 (carrier-bit swing).

The leg's script ASSERTS the index bookkeeping as multiples of A-hat
(ind_A = -21*Ahat etc.). Here the same numbers are RE-DERIVED from first
principles via characteristic classes on a closed spin 4-manifold, using
only:
    A-hat = 1 - p1/24          (degree-4 truncation)
    ch(E_C) = rk + p1(E)       (real E, complexified; c1=0, c2=-p1,
                                ch_2 = (c1^2 - 2 c2)/2 = p1)
    p1[M] = 3 sigma            (Hirzebruch signature theorem)
    ind D = A-hat[M] = -sigma/8
NO chi is imported anywhere; sigma is the only topological input.
The generic-coefficient identities (-19, -21, -20 as 4-manifold densities)
are derived SYMBOLICALLY in p1, then specialized to K3 (sigma = -16) and,
as a Rokhlin-consistent control, to a hypothetical spin 4-manifold with
sigma = -32.  Exact Fractions only.  Exit 0 iff all checks pass.
"""
import sys
from fractions import Fraction as F

fails = []
def check(name, got, want):
    ok = (got == want)
    print(("PASS  " if ok else "FAIL  ") + "%s: %r (want %r)" % (name, got, want))
    if not ok:
        fails.append(name)

# ---- symbolic degree-4 densities in units of p1[M] -------------------------
# A 4d index of D twisted by a virtual bundle W = ch-character (r + a*p1):
#   ind(D (x) W) = [ (1 - p1/24) * (r + a*p1) ]_4 = a*p1 - r*p1/24
# with p1 evaluated on the fundamental class.
def ind_twisted(r, a):
    """index density coefficient of p1[M] for ch(W) = r + a*p1."""
    return a - F(r, 24)

# ch(T_C) for real rank-4 tangent bundle: r = 4, a = +1  (ch_2 = p1)
cT = (4, F(1))

# carrier B (geometric gamma-traceless Q): ch = ch(T_C) + 1  -> r = 5, a = 1
coefB = ind_twisted(5, F(1))          # per p1[M]
# carrier A (ghost-subtracted gravitino): ch = ch(T_C) - 1   -> r = 3, a = 1
coefA = ind_twisted(3, F(1))
# bare twist control: ch = ch(T_C)                           -> r = 4, a = 1
coefBARE = ind_twisted(4, F(1))
# plain Dirac: r = 1, a = 0
coefD = ind_twisted(1, F(0))

check("density B  = 19/24 * p1  (HS eq 11 coefficient)", coefB, F(19, 24))
check("density A  = 7/8   * p1  (ghost-subtracted)", coefA, F(7, 8))
check("density bare = 5/6 * p1  (control row of the adjudication table)",
      coefBARE, F(5, 6))
check("density D  = -1/24 * p1  (plain Dirac)", coefD, F(-1, 24))

# ---- express as multiples of A-hat[M] = -p1/24 -----------------------------
# ind = coef * p1[M]; A-hat[M] = -p1[M]/24  =>  ind / A-hat = -24 * coef
check("B  = -19 * A-hat  (HS Prop 3.1(i), independently derived)",
      -24 * coefB, F(-19))
check("A  = -21 * A-hat  (Witten/AGW ghost-subtracted coefficient)",
      -24 * coefA, F(-21))
check("bare = -20 * A-hat (PTZ 'ghostless' -20, independently derived)",
      -24 * coefBARE, F(-20))
check("D  =   1 * A-hat", -24 * coefD, F(1))

# PTZ bookkeeping falls out of the densities (not assumed):
check("PTZ eq 5.2 gravitino: -21 = -20 - 1 (bare minus one Dirac unit)",
      -24 * coefA, -24 * coefBARE - 1)
check("PTZ eq 5.2 RSA:       -19 = -20 + 1 (bare plus one Dirac unit)",
      -24 * coefB, -24 * coefBARE + 1)
check("PTZ eq 5.1:           -19 = -21 + 2",
      -24 * coefB, -24 * coefA + 2)

# ---- specialize to K3: sigma = -16 (b+ = 3, b- = 19), p1 = 3 sigma = -48 ---
sigma = F(-16)
p1 = 3 * sigma
Ahat = -sigma / 8
check("A-hat(K3) = 2 from sigma only", Ahat, F(2))
check("p1[K3] = -48 (signature theorem, no chi)", p1, F(-48))

indB = coefB * p1
indA = coefA * p1
indBARE = coefBARE * p1
indD = coefD * p1
check("ind B on K3 = -38 = 19*sigma/8", (indB, indB == 19 * sigma / 8),
      (F(-38), True))
check("ind A on K3 = -42 = 21*sigma/8", (indA, indA == 21 * sigma / 8),
      (F(-42), True))
check("ind bare on K3 = -40", indBARE, F(-40))
check("ind D on K3 = 2", indD, F(2))
check("HS additivity ind Q = ind D_TM + ind D: -38 = -40 + 2",
      indBARE + indD, indB)
check("fork B - A = 4 = 2 * ind D", (indB - indA, indB - indA == 2 * indD),
      (F(4), True))
check("mod 3: A = 0, B = 1 (order-3 discriminator)",
      (int(indA) % 3, int(indB) % 3), (0, 1))

# ---- Rokhlin-consistent control (sigma = -32, NOT K3) ----------------------
s2 = F(-32)
check("control sigma=-32: B = -19*(-(-32)/8) = -76 and B = 19*sigma/8 agree",
      (coefB * 3 * s2, coefB * 3 * s2 == 19 * s2 / 8), (F(-76), True))
check("control sigma=-32: A-B fork still 2 Dirac units",
      coefB * 3 * s2 - coefA * 3 * s2, 2 * (-s2 / 8))

# ---- referee independence guard --------------------------------------------
# The derivation above never used: chi, 24/8, A-hat=3, or any assumed -19/-21.
banned = [n for n in dir() if n.lower().startswith("chi")]
check("firewall: no chi symbol used", banned, [])

print()
if fails:
    print("REFEREE RESULT: FAIL (%d)" % len(fails))
    sys.exit(1)
print("REFEREE RESULT: ALL PASS -- the -19/-21/-20 coefficients, the K3 values "
      "(-38/-42/-40/2), the additivity, the fork = 2 Dirac units, and the mod-3 "
      "classes (0,1) are INDEPENDENTLY re-derived from characteristic classes "
      "with sigma as the only topological input.")
sys.exit(0)
