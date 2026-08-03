#!/usr/bin/env sage
"""Independent Sage/Weyl-character certificate for Resolver Wave D."""
from sage.all import WeylCharacterRing


checks = 0


def check(label, condition):
    global checks
    checks += 1
    print("  [{}] {}".format("ok " if condition else "FAIL", label))
    assert condition, label


D5 = WeylCharacterRing("D5", style="coroots")
V = D5(1, 0, 0, 0, 0)
L3 = D5(0, 0, 1, 0, 0)          # 120
L4 = D5(0, 0, 0, 1, 1)          # 210 = Lambda6 as well
H126p = D5(0, 0, 0, 0, 2)
H126m = D5(0, 0, 0, 2, 0)
HOOK1728 = D5(1, 0, 0, 1, 1)

L5 = V.exterior_power(5)
L6 = V.exterior_power(6)
L7 = V.exterior_power(7)

check("Lambda5 is the conjugate 126 pair", L5 == H126p + H126m)
check("Lambda6 is dual to Lambda4 and has degree 210",
      L6 == L4 and L6.degree() == 210)
check("Lambda7 is dual to Lambda3 and has degree 120",
      L7 == L3 and L7.degree() == 120)
check("V tensor Lambda6 decomposes as Lambda5 + Lambda7 + hook1728",
      V * L6 == L5 + L7 + HOOK1728)
check("all four irreducibles occur with multiplicity one",
      (V * L6).coefficient(H126p.highest_weight()) == 1
      and (V * L6).coefficient(H126m.highest_weight()) == 1
      and (V * L6).coefficient(L3.highest_weight()) == 1
      and (V * L6).coefficient(HOOK1728.highest_weight()) == 1)
check("dimension closure is 2100=126+126+120+1728",
      (V * L6).degree() == 2100 == 126 + 126 + 120 + 1728)
check("a planted second 126 copy is rejected",
      V * L6 != 2 * H126p + H126m + L7 + HOOK1728)

# Full D7 classification before the 4+10 observer reduction.
D7 = WeylCharacterRing("D7", style="coroots")
V14 = D7(1, 0, 0, 0, 0, 0, 0)
L5_14 = V14.exterior_power(5)
L6_14 = V14.exterior_power(6)
L7_14 = V14.exterior_power(7)
L10_14 = V14.exterior_power(10)
L7P_14 = D7(0, 0, 0, 0, 0, 2, 0)
L7M_14 = D7(0, 0, 0, 0, 0, 0, 2)
HOOK6_14 = D7(1, 0, 0, 0, 0, 1, 1)
check("full D7 contraction target Lambda5 has degree 2002",
      L5_14.degree() == 2002)
check("D7 Lambda7 split and grade-six hook are explicit irreducible characters",
      L7_14 == L7P_14 + L7M_14
      and V14 * L6_14 == L5_14 + L7P_14 + L7M_14 + HOOK6_14
      and (V14 * L6_14).coefficient(L5_14.highest_weight()) == 1
      and (V14 * L6_14).coefficient(HOOK6_14.highest_weight()) == 1)
check("full D7 grade-six hook has degree 36608",
      HOOK6_14.degree() == 36608
      and (V14 * L6_14).degree() == 42042)

# Grade ten supplies an independent Hodge--wedge route.  Its existence means
# the source must select or relate two native amplitudes; Wave D does not spend
# an orientation datum to choose between them.
grade10_product = V14 * L10_14
check("abstract grade-ten comparator carrier contains Lambda5 once",
      grade10_product.coefficient(L5_14.highest_weight()) == 1)
check("grade-six and grade-ten are two distinct native algebraic carriers",
      L6_14 != L10_14)

print("Q7 Sage verdict: the local D5 carrier contains exactly one real")
print("Lambda5 isotypic component, i.e. one conjugate 126+ plus 126- pair.")
print("checks passed:", checks)
