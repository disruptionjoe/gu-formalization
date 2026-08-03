#!/usr/bin/env sage
"""Independent Sage Weyl-character certificate for Resolver Wave B / DQ1.

Run with:

    sage tests/observable-algebra/dq1_compact_isotypic_sage.py

This is deliberately separate from the base Python certificate so the ordinary
test harness does not acquire a Sage dependency.  It checks actual B4/B2
character-ring decompositions, not a second implementation of the same manual
Weyl product.  Reality types and Krein-sign multiplicities remain the analytic
compact-Clifford/Schur part of the paired report.
"""
from sage.all import WeylCharacterRing


checks = 0


def check(name, condition):
    global checks
    checks += 1
    print("  [{}] {}".format("ok " if condition else "FAIL", name))
    assert condition, name


B4 = WeylCharacterRing("B4", style="coroots")
B2 = WeylCharacterRing("B2", style="coroots")

s9 = B4(0, 0, 0, 1)
v9 = B4(1, 0, 0, 0)
r9 = B4(1, 0, 0, 1)
s5 = B2(0, 1)
v5 = B2(1, 0)
r5 = B2(1, 1)

check("B4 spinor degree is 16", s9.degree() == 16)
check("B4 RS highest-weight degree is 128", r9.degree() == 128)
check("B4 character identity 9x16 = 16+128", v9 * s9 == s9 + r9)
check("B2 spinor degree is 4", s5.degree() == 4)
check("B2 RS highest-weight degree is 16", r5.degree() == 16)
check("B2 character identity 5x4 = 4+16", v5 * s5 == s5 + r5)

U = s9.degree() * s5.degree()
X = r9.degree() * s5.degree()
Y = s9.degree() * r5.degree()
check("U dimension is 64", U == 64)
check("X dimension is 512", X == 512)
check("Y dimension is 256", Y == 256)
check("one chiral gamma-kernel is 832", U + X + Y == 832)
check("two chiral gamma-kernels total 1664", 2 * (U + X + Y) == 1664)
check("rank-nullity comparator is 1664", 14 * 128 - 128 == 1664)

print("DQ1 Sage verdict: B4xB2 character branching confirmed exactly")
print("checks passed:", checks)
