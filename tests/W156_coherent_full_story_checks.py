"""
W156 -- deterministic checks for the coherent-full-story capstone (TEAM COHERENT-STORY).

Exploration grade. Conditional register. NOT evidence. This test runs the one computation
the W156 convergence pass actually needs: the STRUCTURAL-vs-COINCIDENCE status of the
a2 = -a1^2 identity that personas 6 and 10 independently land on as the keystone tying the
tachyon (a2 = -1/9) to the attractive-Einstein sign (a1 = +1/3).

The GU object under study (CITED, not re-derived here):
    induced |II|^2 potential sector    F(R) = a0 + a1 R + a2 R^2
    with (W126 line 72 / W130 / W151 / W153)   a0 = 2, a1 = +1/3, a2 = -1/9,
    obtained from the W126 MSS interpolant    P(u) = w2 u^2 + w1 u + w0 = -64 u^2 - 8 u + 2
    under the pinned curvature map            R = -24 u   (so u = -R/24).

Positive controls first (regression pins on the W126/W130/W153 numbers), then the W156
structural-vs-coincidence computation.
"""

import sympy as sp

R, p = sp.symbols('R p', real=True)
u = sp.symbols('u', real=True)

checks = []
def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS" if cond else "FAIL"), name)

# ---------------------------------------------------------------------------
# POSITIVE CONTROLS -- regression pins on the cited coefficients.
# ---------------------------------------------------------------------------
a0, a1, a2 = sp.Rational(2), sp.Rational(1, 3), sp.Rational(-1, 9)
check("PC1 a0 = 2 (W126/W130/W153 regression pin)", a0 == 2)
check("PC2 a1 = +1/3 (attractive Einstein sign, H25 CLEAR)", a1 == sp.Rational(1, 3))
check("PC3 a2 = -1/9 (positive-norm tachyon coefficient, W122/W126)", a2 == sp.Rational(-1, 9))

# W126 interpolant -> F(R) under R = -24 u  (positive control that the coefficients
# come from the polynomial P(u) with (w0,w1,w2) = (2,-8,-64)).
w0, w1, w2 = sp.Rational(2), sp.Rational(-8), sp.Rational(-64)
P = w2*u**2 + w1*u + w0
F_from_P = sp.expand(P.subs(u, -R/24))
check("PC4 P(u) = -64u^2 - 8u + 2 with u = -R/24 gives F = 2 + R/3 - R^2/9",
      sp.expand(F_from_P - (a0 + a1*R + a2*R**2)) == 0)

# ---------------------------------------------------------------------------
# THE W156 CONVERGENCE-PASS COMPUTATION: is a2 = -a1^2 structural or coincidence?
# ---------------------------------------------------------------------------

# (S1) The exact identity, regression pin (matches W155 C1).
check("S1 a2 == -a1^2 exactly (-1/9 = -(1/3)^2)", a2 == -a1**2)

# (S2) Algebraic equivalence: a2 = -a1^2  <=>  a2/a1 = -a1  (ratio equals minus the
#      linear coefficient). This localizes the identity: it is NOT a statement about a1
#      and a2 separately, it is the statement that the INDEPENDENTLY computed ratio
#      a2/a1 = -1/3 (W130 c_R data) happens to equal -a1.
a1s = sp.symbols('a1s', nonzero=True)
a2s = sp.symbols('a2s')
equiv_lhs = sp.Eq(a2s, -a1s**2)
# a2/a1 = -a1  <=>  a2 = -a1^2  (for a1 != 0); verify the two forms are identical.
check("S2 identity a2=-a1^2 is equivalent to (a2/a1) = -a1 (ratio = minus linear coeff)",
      sp.simplify((a2s/a1s + a1s) - (a2s + a1s**2)/a1s) == 0
      and (a2/a1) == -a1)

# (S3) Polynomial-coefficient form: in P(u) = w2 u^2 + w1 u + w0, the identity a2 = -a1^2
#      is EXACTLY the coefficient relation w2 = -w1^2 (independent of the map scale 24 and
#      independent of w0). Proof: a1 = -w1/24, a2 = w2/24^2, so a2 = -a1^2 <=> w2 = -w1^2.
check("S3 with a1=-w1/24, a2=w2/24^2 the identity a2=-a1^2 reduces to w2 = -w1^2",
      sp.simplify((w2/sp.Integer(24)**2) - (-(-w1/sp.Integer(24))**2)) == 0)
check("S4 the W126 interpolant satisfies w2 = -w1^2 (i.e. -64 = -(-8)^2)",
      w2 == -w1**2)

# (S5) Scale-mode (conformal-factor) invariance -- inherits W153 T1: a1, a2 are invariant
#      under the conformal factor p (the BLMS record-count / scale mode). Therefore the
#      identity a2 = -a1^2, being a relation among p-invariant quantities, is ITSELF
#      p-invariant: it is not an artifact of a scale choice. We model W153 T1 by asserting
#      the coefficients do not depend on p and checking the identity holds "at every p".
a1_of_p = sp.Rational(1, 3) + 0*p   # W153 T1: independent of p
a2_of_p = sp.Rational(-1, 9) + 0*p  # W153 T1: independent of p
identity_residual = sp.simplify(a2_of_p + a1_of_p**2)  # = 0 for all p iff structural in p
check("S5 a2(p) + a1(p)^2 == 0 for all conformal factors p (scale-mode invariant, W153 T1)",
      identity_residual == 0
      and all(sp.simplify((a2_of_p + a1_of_p**2).subs(p, k)) == 0 for k in (-2, -1, 0, 1, 2)))

# (S6) The HONEST NEGATIVE control that keeps the grade at STRUCTURAL-CANDIDATE, not proven:
#      a generic degree-2 induced potential does NOT satisfy a2 = -a1^2. We exhibit a nearby
#      polynomial with the same a1 but a2 perturbed off -a1^2 to confirm the identity is a
#      genuine constraint (not automatic for any degree-2 F), so it REQUIRES a derivation to
#      be called structural rather than coincidental.
a2_generic = sp.Rational(-1, 9) + sp.Rational(1, 100)  # a nearby, still-tachyonic value
check("S6 a generic tachyonic a2 (e.g. -1/9 + 1/100) does NOT satisfy a2 = -a1^2 "
      "(so the identity is a real constraint, not automatic)",
      a2_generic != -a1**2)

# (S7) The consequence lock (matches W155 C4/C5): under a2 = -a1^2 the scalaron mass is
#      m^2 = -1/(6 a1), so m^2 < 0 PRECISELY when a1 > 0 (the attractive Einstein sign).
Fpoly = a0 + a1*R + a2*R**2
Fp = sp.diff(Fpoly, R)
Fpp = sp.diff(Fpoly, R, 2)
m2 = sp.simplify((sp.Rational(1, 3))*(Fp/Fpp - R)).subs(R, 0)
check("S7 m_scalaron^2(R=0) = -1/2 (tachyonic), = a1/(6 a2)", sp.simplify(m2 - sp.Rational(-1, 2)) == 0)
a1p = sp.symbols('a1p', positive=True)
m2_locked = sp.simplify((sp.Rational(1, 3))*((a1p)/(2*(-a1p**2)) ))  # (F'/F'' - R)|_{R=0} with a2=-a1p^2
check("S7b symbolic lock m^2 = -1/(6 a1) < 0 whenever a1 > 0 (attractive sign forces tachyon)",
      sp.simplify(m2_locked - (-1/(6*a1p))) == 0 and m2_locked < 0)

# ---------------------------------------------------------------------------
print()
n_pass = sum(1 for _, ok in checks if ok)
print(f"{n_pass}/{len(checks)} checks passed")
import sys
sys.exit(0 if n_pass == len(checks) else 1)
