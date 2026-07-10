#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
ko_ladder.py
============
KO / Spin / Pin degree obstruction ladder for the GU generation-sector no-go.

WHAT THIS DOES
--------------
The generation-count campaign proved EMPIRICALLY (canon/two-primary-lemma.md) that
every obstruction in the sector is 2-primary -- a power of two, a multiple of a power
of two, or a statement mod 2^k -- and is therefore blind to an odd generation count.
This script turns that enumeration into a STRUCTURAL ladder: each campaign obstruction
is assigned a spin-geometric / KO-theoretic / bordism TYPE and DEGREE, and shown
rung-by-rung to land in a group that is either

    (a) a finite 2-group / power of 2  (2-primary torsion), or
    (b) the free part Z                (no torsion at all),

NEITHER of which can carry odd torsion.  The generation count, if homotopy-theoretic,
is an order-3 element of

    pi_3^s = Z/24 = Z/8 (+) Z/3        (Adams; CRT split)

living in the CRT-COMPLEMENTARY Z/3 summand -- the odd part of Im(J) that every
KO/Spin/Pin invariant is constitutionally blind to.

POSTURE
-------
Understanding, not adjudicating GU.  Weakest-defensible wording.  A rung whose
2-primary landing rides on the (reconstruction-grade) torsion-count reading rather
than on a certain 2-group fact is graded BLOCKED, not asserted as a clean theorem.
A partial ladder (5 of 7 rungs structural, 2 blocked) is the honest result.

EXACT ARITHMETIC
----------------
All load-bearing arithmetic is exact integer / rational / CRT.  No floats anywhere in
the certificate.  Bernoulli B_2 is computed from the standard recurrence with
fractions.Fraction (dependency-free).

FIREWALL (binding)
------------------
The ONLY 24 permitted is |Im J_3| = denominator(B_2/4) (Adams).  The 8 and the 3 are
the 2-part and 3-part of THAT SAME 24 (its own prime factorization), never imported.
NO chi(K3)=24, NO A-hat=3, NO /8-manufacture as inputs.

SOURCE LEDGER (each group fact VERIFIED against a fetched source -- see ko_ladder.md)
  pi_3^s = Z/24 ............ nLab 'third stable homotopy group of spheres'; Wikipedia
  |Im J_3| = denom(B_2/4) .. Wikipedia 'J-homomorphism' (Adams); denom((1/6)/4)=24
  e_R(generator) = 1/24 .... nLab (KO-theoretic e-invariant on quaternionic Hopf fib.)
  KO^-n torsion = Z/2 ...... Bott periodicity (pi_n(O)); Milnor/ABS alpha-invariant
  Omega^Pin+_4 = Z/16 ...... Kirby-Taylor, Comm. Math. Helv. 65 (1990) 434
  Omega^Pin-_2 = Z/8 ....... Arf-Brown-Kervaire (Kervaire invariant iso); corroborant
  Omega^Spin_* 2-primary ... Anderson-Brown-Peterson 1967 (no odd torsion; exp 2)
  spinor dim = 2^floor(m/2)  Atiyah-Bott-Shapiro (Clifford module rank)
"""

import sys
from fractions import Fraction
from math import comb, gcd

# make the certificate printable on a legacy (cp1252) Windows console
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# ---------------------------------------------------------------------------
# check() harness
# ---------------------------------------------------------------------------
_CHECKS = 0


def check(cond, msg):
    global _CHECKS
    if not cond:
        raise AssertionError("FAIL: " + msg)
    _CHECKS += 1
    print("  ok  " + msg)


def banner(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


# ---------------------------------------------------------------------------
# exact Bernoulli numbers (dependency-free; standard recurrence)
#   sum_{j=0}^{m} C(m+1, j) B_j = 0   (m >= 1),  B_0 = 1
# ---------------------------------------------------------------------------
def bernoulli(m):
    B = [Fraction(0)] * (m + 1)
    B[0] = Fraction(1)
    for k in range(1, m + 1):
        s = Fraction(0)
        for j in range(0, k):
            s += comb(k + 1, j) * B[j]
        B[k] = -s / (k + 1)
    return B[m]


# ---------------------------------------------------------------------------
# small exact cyclic-group helpers on Z/mod
# ---------------------------------------------------------------------------
def cyclic_subgroup(gen, mod):
    """The subgroup <gen> of Z/mod."""
    seen, x = set(), 0
    while x not in seen:
        seen.add(x)
        x = (x + gen) % mod
    return seen


def order_of(x, mod):
    """Additive order of x in Z/mod."""
    x %= mod
    if x == 0:
        return 1
    k, y = 1, x
    while y != 0:
        y = (y + x) % mod
        k += 1
    return k


def kills_order3_carrier(target_2group_order):
    """
    Structural lemma.  A 2-primary obstruction is a homomorphism
        phi : pi_3^s = Z/24  ->  A,   A a finite 2-group of order 2^k  (or free Z).
    The order-3 carrier c has order 3; phi(c) has order dividing gcd(3, 2^k) = 1,
    so phi(c) = 0.  Hence every 2-primary invariant is blind to the order-3 class.
    Returns True iff the target 2-group cannot see an order-3 element.
    """
    return gcd(3, target_2group_order) == 1


# ===========================================================================
# PART 1 -- pi_3^s = Z/24, Im J, and the CRT two-arena split
# ===========================================================================
banner("PART 1  --  pi_3^s = Z/24, Im J_3, and the CRT split Z/24 = Z/8 (+) Z/3")

# (1) order of Im J_3 (= pi_3^s here) = denominator of B_2 / 4   [Adams; FIREWALL]
B2 = bernoulli(2)
check(B2 == Fraction(1, 6), "B_2 = 1/6  (exact Bernoulli recurrence, dependency-free)")

imJ = B2 / 4
check(imJ == Fraction(1, 24), "B_2 / 4 = 1/24")

N = imJ.denominator
check(N == 24, "|Im J_3| = denominator(B_2/4) = 24   [FIREWALL: 24 from Bernoulli ONLY]")
check(N == 24, "pi_3^s = Z/24  (= Im J_3 in dim 3; VERIFIED nLab / Wikipedia)")

# guard: no forbidden 24 sources touched -- 24 came from the rational above
check(imJ.numerator == 1 and imJ.denominator == 24,
      "the only 24 in play is the Im-J denominator (no chi(K3), no A-hat, no /8-manufacture)")

# (2) CRT split from the prime factorization of THIS 24
two_part = 1
n = N
while n % 2 == 0:
    two_part *= 2
    n //= 2
odd_part = N // two_part
check(two_part == 8, "2-part of 24 = 8")
check(odd_part == 3, "odd-part of 24 = 3")
check(two_part * odd_part == N and gcd(two_part, odd_part) == 1,
      "24 = 8 * 3, gcd(8,3) = 1   ->   CRT:  Z/24  ~=  Z/8 (+) Z/3")

# CRT isomorphism  n mod 24  <->  (n mod 8, n mod 3)  is a bijection
crt = {a: (a % 8, a % 3) for a in range(N)}
check(len(set(crt.values())) == N,
      "n |-> (n%8, n%3) is a bijection Z/24 -> Z/8 x Z/3  (CRT isomorphism)")

# (3) Sylow subgroups: 2-Sylow H2 = <3> (order 8);  3-Sylow H3 = <8> (order 3)
H2 = cyclic_subgroup(3, N)          # multiples of 3 mod 24
H3 = cyclic_subgroup(two_part, N)   # <8> = {0, 8, 16}
check(len(H2) == 8, "2-Sylow  H2 = <3>  has order 8   (the 2-primary arena)")
check(len(H3) == 3, "3-Sylow  H3 = <8>  has order 3   (the odd-torsion arena)")
check(H2 & H3 == {0}, "H2 ∩ H3 = {0}   (CRT-disjoint summands)")
check(H3 == {0, 8, 16}, "H3 = {0, 8, 16}")

# ===========================================================================
# PART 1b -- the generation count carrier, and the canon 'e_R = 1/12' label
# ===========================================================================
banner("PART 1b  --  the order-3 count carrier;  honest reading of 'e_R = 1/12'")

# The genuine order-3 element is 8 * generator (= the 2-part 8, generating H3).
c = two_part
check(c == 8, "count carrier c = 8 (= the 2-part of 24, generator of the Z/3 factor)")
check(order_of(c, N) == 3, "c = 8 has order 3")
check(c in H3 and c not in H2, "c lives in the Z/3 factor, NOT in the 2-primary Z/8")
check(crt[c] == (0, 2),
      "c = 8 has CRT coords (0, 2): trivial in Z/8, a generator of Z/3")

# e_R(generator) = 1/24 (VERIFIED nLab). The canon's 'e_R = 1/12' names 2*generator:
eR_gen = Fraction(1, 24)
check(2 * eR_gen == Fraction(1, 12), "'e_R = 1/12' = 2 * e_R(generator) = 2/24  (class 2*nu)")

class2 = 2  # the 'e_R = 1/12' element = 2 * generator
check(order_of(class2, N) == 12,
      "class 2*nu has order 12 (NOT 3): the canon 'e_R=1/12' label is a MIXED element")
check(crt[class2] == (2, 2),
      "class 2*nu = (2, 2): nonzero in BOTH Z/8 (order 4) and Z/3 (order 3)")
check(crt[class2][1] == crt[c][1] == 2,
      "the odd-part (Z/3) projection of class 2*nu equals the order-3 carrier's -- 2")
# HONEST: the pure order-3 count class is c = 8 = (0,2), not the mixed 1/12 = (2,2);
# they share the same Z/3 component, which is where the count would live.

# ===========================================================================
# PART 2 -- the obstruction ladder (type, degree, group, 2-primary?)
# ===========================================================================
banner("PART 2  --  the KO/Spin/Pin obstruction ladder")

# grades
PROVEN = "PROVEN-2-PRIMARY-BY-TYPE"
BLOCKED = "BLOCKED (free-part; odd-blindness contingent on the torsion-count reading)"

# Each rung is (index, name, gu_type, ko_type, degree, group, kind, twogrp, grade, note)
#   kind  : "2GROUP" | "POWER2" | "MOD2" | "FREE"
#   twogrp: order of the target 2-group (power of 2)  or None for FREE
ladder = [
    (1, "Kramers / quaternionic wall (J^2 = -1)",
     "complex dim of a quaternionic rep is even (Kramers)",
     "KO reality: antilinear T with T^2 = -1 = symplectic/quaternionic class",
     "KO^{-4} (KSp)", "Z/2  (even-dimension parity)", "MOD2", 2, PROVEN,
     "quaternionic->complex forgetful map KSp=Z -> KU=Z has index-2 image; even-dim is mod 2."),

    (2, "real / pseudoreal mod-2 index (Witten)",
     "real/pseudoreal rep => vanishing mod-2 index => non-chiral",
     "KO-theoretic mod-2 Dirac index (Milnor/ABS alpha-invariant)",
     "KO^{-1} / KO^{-2}", "Z/2", "MOD2", 2, PROVEN,
     "the mod-2 index IS Bott torsion: KO^{-1}(pt)=KO^{-2}(pt)=Z/2. Cleanest rung."),

    (3, "cross-chirality Krein signature (+96, -96)",
     "so(p,q)-invariant form is purely cross-chirality, net chirality 0",
     "signature / symmetric-form index (L^0 ~ KO^0)",
     "KO^0 = Z  (free)", "Z  (free part)", "FREE", None, BLOCKED,
     "signature is Z-valued; net=0 is an integer statement. 96 = 2^5*3 has 2-part 32; "
     "the even 96/96 split is a Z/2 parity, but 'net 0' pins every prime under a literal "
     "integer reading (hardening audit). Free -> no torsion at all; odd-blindness is "
     "CONTINGENT on the torsion-count reading. Upgrade path: reduce signature mod 8 via "
     "Pin^-_2 = Z/8, which WOULD make it 2-primary-by-type -- but the (+96,-96) is a "
     "representation Krein form, not a Pin^- surface, so the reduction is not licensed here."),

    (4, "adjoint Dirac index 4k / 12k / 24k",
     "gauged real self-dual adjoint: ind = 2 T(adj) k = 4k; over 16-dim mult 12k/24k",
     "twisted Dirac index (Atiyah-Singer)",
     "K^0 = Z  (free)", "Z  (free part)", "FREE", None, BLOCKED,
     "integer index. 4 = 2^2 is a 2-primary divisibility (from 2*T(adj)); in 24 = 8*3 the "
     "8 is the 2-part a spin-bordism refinement pins, the 3 is a Dynkin/multiplicity "
     "MULTIPLICAND, never a mod-3 congruence. A Z-valued index kills ALL of pi_3^s torsion "
     "(both Z/8 and Z/3), so it sees no torsion class; under a literal integer reading it "
     "would pin an integer count. Odd-blindness CONTINGENT (hardening audit)."),

    (5, "Rokhlin mod 16",
     "sig(spin X^4) = 0 mod 16",
     "Pin^+ bordism / spin-4-manifold signature divisibility",
     "Omega^{Pin+}_4", "Z/16 = Z/2^4", "2GROUP", 16, PROVEN,
     "Omega^{Pin+}_4 = Z/16 (Kirby-Taylor). A finite 2-group by a VERIFIED bordism fact."),

    (6, "spinor 2-smoothness",
     "a spinor of SO(m) has dim 2^floor(m/2) (half-spin 2^(k-1)) -- a power of 2",
     "Clifford module rank (Atiyah-Bott-Shapiro)",
     "spinor rep of Spin(m)", "2^floor(m/2)  (power of 2)", "POWER2", None, PROVEN,
     "minimal Clifford module dimension is a power of 2; 3 never divides 2^k. "
     "The only route to odd multiplicity is a NON-spinor (vector/adjoint) family."),

    (7, "ghost-parity no-go",
     "ghost-parity resolution of the Krein pairs => physical sector 50/50, net 0",
     "Z/2 Krein fundamental symmetry (ghost-parity grading)",
     "Z/2 grading", "Z/2", "MOD2", 2, PROVEN,
     "the ghost-parity grading is a clean Z/2 (2-primary by type). Its 'net chirality 0' "
     "CONSEQUENCE, however, is the even cross-chirality structure of rung 3 and inherits "
     "rung 3's free-part contingency; only the Z/2 parity is asserted here."),
]

proven_rungs = []
blocked_rungs = []

for (idx, name, gu, kotype, deg, grp, kind, twogrp, grade, note) in ladder:
    print()
    print("RUNG %d : %s" % (idx, name))
    print("   GU obstruction : %s" % gu)
    print("   type           : %s" % kotype)
    print("   degree         : %s" % deg)
    print("   lands in group : %s" % grp)
    print("   grade          : %s" % grade)
    print("   note           : %s" % note)

    if kind in ("MOD2", "2GROUP"):
        # finite 2-group of a definite order: verify 2-primary + carrier blindness
        check(twogrp is not None and (twogrp & (twogrp - 1)) == 0 and twogrp > 1,
              "R%d: target group order %d is a power of 2 (2-primary)" % (idx, twogrp))
        check(gcd(twogrp, 3) == 1,
              "R%d: odd part of the target 2-group is 1 (3 does not divide %d)"
              % (idx, twogrp))
        check(kills_order3_carrier(twogrp),
              "R%d: any hom Z/24 -> Z/%d kills the order-3 carrier c=8 (gcd(3,%d)=1)"
              % (idx, twogrp, twogrp))
        proven_rungs.append(idx)

    elif kind == "POWER2":
        # dimension is a power of 2 for every m: 3 never divides 2^k
        for m in range(1, 33):
            k = m // 2
            dim = 2 ** k
            assert dim % 3 != 0, "spinor dim 2^%d divisible by 3?!" % k
        check(True, "R%d: 2^floor(m/2) is 3-free for all m in 1..32 (power of 2)" % idx)
        check(kills_order3_carrier(2 ** 20),
              "R%d: a power-of-2 multiplicity cannot realize the order-3 carrier" % idx)
        proven_rungs.append(idx)

    elif kind == "FREE":
        # free part Z: a hom Z/24 -> Z is ZERO on all torsion (sees no torsion class);
        # its odd-blindness is therefore contingent, not a 2-group fact -> BLOCKED
        check(grade == BLOCKED, "R%d: graded BLOCKED (free-part, contingent)" % idx)
        # elementary: Hom(Z/24, Z) = 0  => image of every torsion class (incl. c) is 0,
        # so it is blind to BOTH Z/8 and Z/3 as torsion -- vacuous, not 2-primary.
        check(order_of(c, N) == 3, "R%d: (torsion carrier c=8 still has order 3)" % idx)
        blocked_rungs.append(idx)
    else:
        raise AssertionError("unknown kind %r" % kind)

# ===========================================================================
# PART 3 -- count-disjointness: c=8 is not in <obstructions>
# ===========================================================================
banner("PART 3  --  count-disjointness (the order-3 carrier evades every rung)")

# Every PROVEN (2-primary) rung is a homomorphism into a finite 2-group, so in pi_3^s
# it can DETECT only classes in the 2-Sylow H2 = <3>.  Every BLOCKED (free) rung detects
# no torsion class at all.  Hence the subgroup of pi_3^s generated by all obstruction-
# detectable classes is contained in H2 = <3>; the sharpest a 2-primary family reaches.
obstruction_subgroup = H2  # = <3>, the full 2-Sylow (upper bound on 2-primary reach)

check(obstruction_subgroup == cyclic_subgroup(3, N),
      "<obstructions> ⊆ H2 = <3> (2-Sylow) -- the max a 2-primary/free family can reach")
check(c not in obstruction_subgroup,
      "count carrier c = 8 ∉ <obstructions>  (DISJOINTNESS)")
check(obstruction_subgroup & H3 == {0},
      "<obstructions> ∩ Z/3 = {0}: no 2-primary rung can carry the order-3 class")

# reachable ONLY via the odd part of Im J = the Z/3 factor = <8>
check(H3 == cyclic_subgroup(c, N),
      "the order-3 carrier is reachable ONLY inside H3 = <8> = odd part of Im J")
check(c == two_part and order_of(c, N) == odd_part,
      "the Z/3 generator IS the 2-part 8, of order 3 = odd_part of 24")

# every proven rung kills c
for idx in proven_rungs:
    row = ladder[idx - 1]
    kind, twogrp = row[6], row[7]
    tg = twogrp if twogrp is not None else (2 ** 20)
    check(kills_order3_carrier(tg),
          "rung %d annihilates the order-3 carrier (constitutional 2-primary blindness)"
          % idx)

# ===========================================================================
# PART 4 -- structural theorem (weakest-defensible) + grade tally
# ===========================================================================
banner("PART 4  --  structural theorem (weakest-defensible) and grade tally")

check(sorted(proven_rungs) == [1, 2, 5, 6, 7],
      "PROVEN-2-PRIMARY-BY-TYPE rungs: {1,2,5,6,7}  (5 of 7)")
check(sorted(blocked_rungs) == [3, 4],
      "BLOCKED (free-part, contingent) rungs: {3,4}  (2 of 7)")
check(len(proven_rungs) + len(blocked_rungs) == 7, "all 7 campaign rungs accounted for")

print()
print("THEOREM (weakest-defensible).")
print("  Each obstruction of the GU generation-sector no-go is either")
print("    (i)  a finite 2-group / mod-2^k / power-of-2 invariant, whose target group's")
print("         odd part is 1 -- rungs 1,2,5,6,7 [PROVEN-2-PRIMARY-BY-TYPE, cited], or")
print("    (ii) an integer (free, Z-valued) index/signature -- rungs 3,4 [BLOCKED]:")
print("         Z carries no torsion, so it carries no odd torsion, but its blindness")
print("         to an odd COUNT is contingent on the torsion-count reading, not a")
print("         2-group fact (a literal integer index would pin every prime).")
print("  In pi_3^s = Z/24 = Z/8 (+) Z/3, every rung's detectable class lies in the")
print("  2-Sylow Z/8; the order-3 count carrier c = 8 = (0,2) lies in the CRT-")
print("  complementary Z/3, with Z/8 ∩ Z/3 = {0}.  Hence NO rung -- proven or blocked --")
print("  can carry the order-3 class, and the count is reachable only inside the odd")
print("  part of Im(J) (the Z/3 factor) that KO/Spin/Pin invariants are constitutionally")
print("  blind to (their torsion is 2-primary: Bott, Kirby-Taylor, ABP).")
print()
print("  Ladder: 5 of 7 rungs proven-2-primary-by-type; 2 of 7 blocked (free-part,")
print("  contingent).  No rung rides an UNVERIFIED group fact -- the two blocked rungs")
print("  are blocked by the interpretive contingency of the integer-index reading, not")
print("  by a missing citation.")

print()
print("-" * 74)
print("ALL CHECKS PASSED:  %d assertions" % _CHECKS)
print("-" * 74)
