#!/usr/bin/env sage
"""Independent Sage/Weyl-character certificate for Wave C's D5 dictionary.

The principal target is Q5; three Q6 identities are checked here as well so
the wave's shared branching dictionary has a genuinely independent CAS route.
"""
from sage.all import WeylCharacterRing


checks = 0


def check(label, condition):
    global checks
    checks += 1
    print("  [{}] {}".format("ok " if condition else "FAIL", label))
    assert condition, label


D5 = WeylCharacterRing("D5", style="coroots")
V = D5(1, 0, 0, 0, 0)
Fp = D5(0, 0, 0, 0, 1)
Fm = D5(0, 0, 0, 1, 0)
Tp = D5(1, 0, 0, 0, 1)
Tm = D5(1, 0, 0, 1, 0)

I45 = D5(0, 1, 0, 0, 0)
I54 = D5(2, 0, 0, 0, 0)
I210 = D5(0, 0, 0, 1, 1)
I945 = D5(1, 0, 1, 0, 0)
I1050p = D5(1, 0, 0, 0, 2)
I1050m = D5(1, 0, 0, 2, 0)
I10 = V
I120 = D5(0, 0, 1, 0, 0)
I126p = D5(0, 0, 0, 0, 2)
I126m = D5(0, 0, 0, 2, 0)
I320 = D5(1, 1, 0, 0, 0)
I1728 = D5(1, 0, 0, 1, 1)

check("degrees 16,16,144,144",
      (Fp.degree(), Fm.degree(), Tp.degree(), Tm.degree()) == (16, 16, 144, 144))
check("10 x 16+ = 16- + 144+", V * Fp == Fm + Tp)
check("10 x 16- = 16+ + 144-", V * Fm == Fp + Tm)
check("16+ x 144+ same-label branch",
      Fp * Tp == I45 + I54 + I210 + I945 + I1050p)
check("16- x 144- same-label branch",
      Fm * Tm == I45 + I54 + I210 + I945 + I1050m)
check("16+ x 144- crossed branch",
      Fp * Tm == I10 + I120 + I126m + I320 + I1728)
check("16- x 144+ crossed branch",
      Fm * Tp == I10 + I120 + I126p + I320 + I1728)
check("same-chirality spinor square contains the matching 126+",
      Fp * Fp == I10 + I120 + I126p)
check("Sym^2(16+) = 10 + 126+", Fp.symmetric_square() == I10 + I126p)
check("Lambda^2(16+) = 120", Fp.exterior_square() == I120)
check("Lambda^5(10) = 126+ + 126-",
      V.exterior_power(5) == I126p + I126m)
check("dual of 16+ is 16-", Fp.dual() == Fm)
check("conditional complex-linear internal Hom contains the same 126+",
      Fp.dual() * Tp == I10 + I120 + I126p + I320 + I1728)
check("planted chirality mismatch is rejected",
      Fp * Tp != I10 + I120 + I126p + I320 + I1728)

for irrep, degree in [(I45, 45), (I54, 54), (I210, 210), (I945, 945),
                      (I1050p, 1050), (I10, 10), (I120, 120),
                      (I126p, 126), (I320, 320), (I1728, 1728)]:
    check("degree {}".format(degree), irrep.degree() == degree)

check("same-label dimension closure", 45 + 54 + 210 + 945 + 1050 == 16 * 144)
check("crossed dimension closure", 10 + 120 + 126 + 320 + 1728 == 16 * 144)

D7 = WeylCharacterRing("D7", style="coroots")
V14 = D7(1, 0, 0, 0, 0, 0, 0)
S14p = D7(0, 0, 0, 0, 0, 0, 1)
check("D7 chiral spinor degree is 64", S14p.degree() == 64)
check("Lambda^2(S14+) = V14 + Lambda^5(V14)",
      S14p.exterior_square() == V14 + V14.exterior_power(5))

print("Q5 Sage verdict: all four D5 character identities confirmed exactly")
print("checks passed:", checks)
