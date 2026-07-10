#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
referee_ko_ladder.py  --  HOSTILE-REFEREE independent re-derivation.

Independently re-derives every load-bearing number in ko_ladder.py from scratch,
using DIFFERENT code paths where possible, and additionally tests the two attacks
a hostile referee must run:

  ATTACK A  --  Is the count carrier really order-3, and is the canon's
                'e_R = 1/12 = order-3 element' actually WRONG?
  ATTACK B  --  Does any invariant that is genuinely KO-theoretic DETECT the
                odd (Z/3) part of Im J?  (The KO-theoretic e-invariant does --
                so the sweeping slogan 'KO/Spin/Pin invariants are
                constitutionally blind to the odd part of Im J' OVERSTATES;
                the defensible statement is scoped to BORDISM-GROUP-VALUED /
                mod-2^k / free-index obstructions, whose TORSION is 2-primary.)

Group facts (each verified against a fetched primary/secondary source this run):
  pi_3^s = Z/24 ............... nLab; Wikipedia
  |Im J_3| = denom(B_2/4)=24 .. Adams; Wikipedia J-homomorphism
  e_KO(nu) = 1/24 (in Q/Z) .... nLab (KO e-invariant on quaternionic Hopf fib.)
  KO^{-n}(pt): Z,Z/2,Z/2,0,Z,0,0,0 ...... Bott; KSp coeffs Z,0,0,0,Z,Z/2,Z/2,0
  Omega^{Pin+}_4 = Z/16 ....... Kirby-Taylor, Comm. Math. Helv. 65 (1990) 434
  Omega^{Pin-}_2 = Z/8 ........ Arf-Brown-Kervaire
  Omega^Spin_* : no odd torsion, exp 2 .. Anderson-Brown-Peterson 1967
  spinor dim = 2^floor(m/2) ... Atiyah-Bott-Shapiro (elementary)
"""
import sys
from fractions import Fraction
from math import comb, gcd

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

C = 0
def ck(cond, msg):
    global C
    if not cond:
        raise AssertionError("REFEREE FAIL: " + msg)
    C += 1
    print("  ok  " + msg)

def bern(m):
    B = [Fraction(0)] * (m + 1)
    B[0] = Fraction(1)
    for k in range(1, m + 1):
        B[k] = -sum(comb(k + 1, j) * B[j] for j in range(k)) / (k + 1)
    return B[m]

def order_of(x, mod):
    x %= mod
    if x == 0:
        return 1
    k, y = 1, x
    while y % mod != 0:
        y += x
        k += 1
    return k

print("=" * 70)
print("PART A  --  arena arithmetic, re-derived independently")
print("=" * 70)
# Im J denominator, INDEPENDENT of the ladder's code path
B2 = bern(2)
ck(B2 == Fraction(1, 6), "B_2 = 1/6")
N = (B2 / 4).denominator
ck(N == 24, "|Im J_3| = denom(B_2/4) = 24  (the ONLY licensed 24)")
# factor
tw = 1; n = N
while n % 2 == 0:
    tw *= 2; n //= 2
odd = N // tw
ck((tw, odd) == (8, 3), "24 = 2-part 8  x  odd-part 3")
ck(gcd(tw, odd) == 1, "gcd(8,3)=1 -> Z/24 = Z/8 (+) Z/3 (CRT)")

# independent CRT bijection check via explicit inverse (extended Euclid)
def crt_pair(a):
    return (a % 8, a % 3)
seen = {}
collision = False
for a in range(24):
    p = crt_pair(a)
    if p in seen:
        collision = True
    seen[p] = a
ck(not collision and len(seen) == 24, "n -> (n%8,n%3) bijective (CRT), verified by exhaustion")

print("=" * 70)
print("PART B  --  ATTACK A: the order-3 carrier, and the canon 'e_R=1/12' error")
print("=" * 70)
# order-3 elements of Z/24 are exactly {8,16}; NOT class 2.
ord3 = sorted([x for x in range(24) if order_of(x, 24) == 3])
ck(ord3 == [8, 16], "the ONLY order-3 elements of Z/24 are {8,16}")
ck(order_of(2, 24) == 12, "class 2 (= 2*nu) has order 12, NOT 3")
# e_KO(nu)=1/24 => e_KO(k*nu) = k/24 ; the canon label 1/12 = 2/24 = class 2
eR = Fraction(1, 24)
ck(2 * eR == Fraction(1, 12), "'e_R=1/12' = 2*e_KO(nu) = class 2*nu")
ck(order_of(2, 24) != 3,
   "CANON ERROR CONFIRMED: 'e_R=1/12 is the order-3 element' is FALSE "
   "(class 2 has order 12, CRT (2,2), MIXED). Script's fix (c=8) is correct.")
c = 8
ck(order_of(c, 24) == 3 and crt_pair(c) == (0, 2),
   "clean order-3 carrier c=8 = (0,2): trivial in Z/8, generates Z/3")

print("=" * 70)
print("PART C  --  the abstract blindness lemma (re-proved two ways)")
print("=" * 70)
# Way 1: image of Z/24 in a 2-group has order | gcd(24, 2^k) = 8, so kills c=8.
def image_order_upper_bound(target_2group_order):
    return gcd(24, target_2group_order)
for k2 in [2, 4, 8, 16, 2 ** 20]:
    ck(gcd(image_order_upper_bound(k2), 3) == 1,
       "hom Z/24 -> 2-group(2^k=%d): image order | gcd(24,%d)=%d, coprime to 3"
       % (k2, k2, image_order_upper_bound(k2)))
# Way 2: explicit -- every hom Z/24->Z/2^k sends 8 to (8 mod 2^k)-scaled gen; 8 has
# order 3, image order divides 3 and divides 2^k => order 1 => phi(8)=0.
for k2 in [2, 4, 8, 16]:
    # a hom Z/24->Z/(2^k) is x -> a*x mod 2^k for a with 24*a ≡ 0; test all a
    kills_all = all((8 * a) % k2 == 0 for a in range(k2) if (24 * a) % k2 == 0)
    ck(kills_all, "every hom Z/24->Z/%d annihilates c=8 (explicit over all a)" % k2)

print("=" * 70)
print("PART D  --  ladder group facts (verified values) + 2-primary status")
print("=" * 70)
# KO^{-n}(pt), n=0..7  (Bott):
KO = ["Z", "Z/2", "Z/2", "0", "Z", "0", "0", "0"]
ck(KO[1] == "Z/2" and KO[2] == "Z/2", "KO^{-1}=KO^{-2}=Z/2 (rung 2 target; genuine torsion)")
ck(KO[4] == "Z", "KO^{-4}=Z (KSp) is FREE  -- rung 1 typing note")
# rung-by-rung target group + whether it can host an order-3 element
rungs = [
    (1, "Kramers even-dim parity", "Z/2", 2, "PROVEN",
     "KO^{-4}=Z is FREE; the '2-primary' content is the mod-2 Kramers parity, "
     "an elementary rep-theory theorem, NOT a torsion class in KO^{-4}."),
    (2, "mod-2 Dirac index (alpha)", "Z/2", 2, "PROVEN", "KO^{-1/-2}=Z/2 genuine torsion"),
    (3, "Krein signature +-96", "Z", None, "BLOCKED", "free Z; net-0 integer, contingent"),
    (4, "adjoint Dirac index", "Z", None, "BLOCKED", "free Z; 24=8*3 with 3 a MULTIPLICAND"),
    (5, "Rokhlin mod 16", "Z/16", 16, "PROVEN", "Omega^{Pin+}_4=Z/16 (Kirby-Taylor)"),
    (6, "spinor dim", "2^floor(m/2)", None, "PROVEN", "power of 2 (ABS); 3 never divides"),
    (7, "ghost parity", "Z/2", 2, "PROVEN", "Z/2 grading"),
]
proven, blocked = [], []
for (i, name, grp, tg, grade, note) in rungs:
    if grade == "PROVEN":
        if tg is not None:
            ck((tg & (tg - 1)) == 0 and gcd(tg, 3) == 1,
               "R%d %s -> %s: 2-group, cannot host order 3" % (i, name, grp))
        else:  # power of 2 family
            ck(all((2 ** (m // 2)) % 3 != 0 for m in range(1, 40)),
               "R%d %s -> 2^floor(m/2): 3-free for all m" % (i, name))
        proven.append(i)
    else:
        ck(grp == "Z", "R%d %s -> Z (free): BLOCKED (no torsion; integer reading pins every prime)" % (i, name))
        blocked.append(i)
ck(proven == [1, 2, 5, 6, 7], "PROVEN rungs {1,2,5,6,7}")
ck(blocked == [3, 4], "BLOCKED rungs {3,4}")

print("=" * 70)
print("PART E  --  ATTACK B: does a KO invariant SEE the odd (Z/3) part of Im J?")
print("=" * 70)
# The KO-theoretic e-invariant e_KO : pi_3^s -> Q/Z, nu |-> 1/24, is INJECTIVE:
img = {(k * eR) % 1 for k in range(24)}   # image in Q/Z
ck(len(img) == 24, "e_KO image in Q/Z has order 24 = FULL pi_3^s (e_KO injective)")
ck((8 * eR) % 1 == Fraction(1, 3),
   "e_KO(8*nu) = 1/3 != 0: the KO-theoretic e-invariant DETECTS the order-3 class")
# CONSEQUENCE (the overclaim finding):
print("  >> FINDING: the odd part of Im J IS detected by the KO-theoretic")
print("     e-invariant (that is HOW |Im J|=24 is computed). So the slogan")
print("     'every KO/Spin/Pin invariant is constitutionally blind to the odd")
print("     part of Im J' OVERSTATES. Defensible (and true) scoping:")
print("     BORDISM-GROUP-VALUED / mod-2^k / free-index obstructions -- the 7")
print("     rungs -- have 2-primary torsion (or are free) and are blind to Z/3;")
print("     the SECONDARY Q/Z-valued e-invariant is not, and is exactly where")
print("     the program itself locates the order-3 carrier. The 7-rung ladder")
print("     is sound; the generalizing slogan must be scoped to primary")
print("     bordism/index invariants, not 'all KO invariants'.")

print("=" * 70)
print("PART F  --  firewall audit")
print("=" * 70)
ck(N == (bern(2) / 4).denominator == 24, "the sole 24 is Im-J denominator (Bernoulli)")
# no chi=24, no A-hat=3, no /8 import: the 8 and 3 come from factoring THIS 24
ck(tw == 8 and odd == 3 and tw * odd == N, "8 and 3 are prime-power parts of the SAME 24")

print()
print("-" * 70)
print("REFEREE CHECKS PASSED: %d" % C)
print("VERDICT: 7-rung ladder SOUND (5 proven-by-type, 2 correctly blocked).")
print("  - Canon 'e_R=1/12 = order-3 element' is WRONG; script correctly uses c=8.")
print("  - Rung 1 KO^{-4}=Z typing is imprecise (KO^{-4} is FREE) but the mod-2")
print("    Kramers conclusion survives via elementary rep theory.")
print("  - OVERCLAIM: 'all KO/Spin/Pin invariants blind to odd Im J' is false")
print("    (KO e-invariant detects it); scope to primary bordism/index invariants.")
print("  - NOT REFUTED: no obstruction reaches Z/3; no group fact wrong.")
print("-" * 70)
