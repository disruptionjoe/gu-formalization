"""
W155 -- deterministic checks for the ten-divergent-personas tachyon reframe sweep.

Exploration grade. Conditional register. These are NOT evidence; they compute the
load-bearing numbers that decide INSIGHT / PLAUSIBLE / RELABEL / DEAD-END for the
reframes in explorations/W155-ten-divergent-personas-tachyon-2026-07-14.md.

The GU object under study (CITED, not re-derived here):
    induced |II|^2 potential sector    F(R) = a0 + a1 R + a2 R^2
    with (W126 line 72 / W130 / W151 line 7)   a0 = 2, a1 = +1/3, a2 = -1/9,
    and W126 theorem: c_3 = c_4 = ... = 0 EXACTLY (potential sector is exactly degree 2).

Positive controls first (Starobinsky healthy scalaron), then the W155 computations.
"""

import sympy as sp

R, M, phi = sp.symbols('R M phi', real=True)
a0, a1, a2 = sp.Rational(2), sp.Rational(1, 3), sp.Rational(-1, 9)

checks = []
def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS" if cond else "FAIL"), name)

# ---------------------------------------------------------------------------
# POSITIVE CONTROLS -- Starobinsky f(R) = R + R^2/(6 M^2), M^2 > 0, healthy.
# ---------------------------------------------------------------------------
f_star = R + R**2/(6*M**2)
fpp_star = sp.diff(f_star, R, 2)
check("PC1 Starobinsky f'' = 1/(3M^2) > 0 (healthy, non-tachyonic)",
      sp.simplify(fpp_star - 1/(3*M**2)) == 0)
# Starobinsky scalaron mass m^2 = (1/3)(f'/f'' - R); at R=0 -> M^2 > 0.
fp_star = sp.diff(f_star, R)
m2_star = sp.simplify((sp.Rational(1,3))*(fp_star/fpp_star - R)).subs(R, 0)
check("PC2 Starobinsky scalaron m^2(R=0) = +M^2 > 0", sp.simplify(m2_star - M**2) == 0)

# ---------------------------------------------------------------------------
# CORE IDENTITY (persona 6 / persona 10 convergence): a2 = -a1^2 exactly.
# ---------------------------------------------------------------------------
check("C1 a2 == -a1**2 exactly (-1/9 = -(1/3)^2)", a2 == -a1**2)
check("C2 ratio a2/a1 == -1/3", sp.Rational(a2, 1)/a1 == sp.Rational(-1, 3))

F = a0 + a1*R + a2*R**2
Fp = sp.diff(F, R)
Fpp = sp.diff(F, R, 2)

# f(R) tachyon criterion is f'' < 0 (standard: f'' > 0 required for a healthy scalaron).
check("C3 F'' = 2 a2 = -2/9 < 0 everywhere (f(R) tachyon criterion met)",
      Fpp == sp.Rational(-2, 9) and Fpp < 0)

# ---------------------------------------------------------------------------
# THE DEBIT->FEATURE LOCK: m_scalaron^2 = (1/3)(F'/F'' - R) at R=0 = -1/(6 a1).
# Negative IFF a1 > 0 (attractive Einstein sign). This is the headline number.
# ---------------------------------------------------------------------------
m2_gu = sp.simplify((sp.Rational(1, 3))*(Fp/Fpp - R)).subs(R, 0)
check("C4 GU scalaron m^2(R=0) = a1/(6 a2) = -1/2 (tachyonic)",
      sp.simplify(m2_gu - sp.Rational(-1, 2)) == 0)
# symbolic lock: with a2 = -a1s^2, m^2 = -1/(6 a1s), sign forced by sign(a1s).
a1s = sp.symbols('a1s', positive=True)
Fs = a0 + a1s*R - a1s**2 * R**2
m2_lock = sp.simplify((sp.Rational(1,3))*(sp.diff(Fs,R)/sp.diff(Fs,R,2) - R)).subs(R,0)
check("C5 LOCK: if a2=-a1^2 then m^2(R=0) = -1/(6 a1), <0 iff a1>0 (attractive)",
      sp.simplify(m2_lock + 1/(6*a1s)) == 0)

# ---------------------------------------------------------------------------
# F(R) SHAPE: downward parabola. Real roots, single Morse maximum (persona 5).
# ---------------------------------------------------------------------------
roots = sorted(sp.solve(F, R))
check("C6 F(R) roots at R = -3 and R = 6 (real, F = -(1/9)(R-6)(R+3))",
      roots == [sp.Integer(-3), sp.Integer(6)])
Rmax = sp.solve(Fp, R)[0]
check("C7 F has a single extremum at R = 3/2 (F''<0 => a MAXIMUM, Morse A_1)",
      Rmax == sp.Rational(3, 2))
check("C8 F_max = F(3/2) = 9/4", sp.simplify(F.subs(R, Rmax) - sp.Rational(9, 4)) == 0)
# Catastrophe DEAD-END: potential sector is exactly quadratic (W126 c_3=c_4=0),
# so no cubic germ -> no fold/cusp; the extremum is a non-degenerate Morse point.
check("C9 no cubic term in F (W126 c_3=0): d^3F/dR^3 = 0 => Morse, NOT a catastrophe",
      sp.diff(F, R, 3) == 0)

# ---------------------------------------------------------------------------
# INFLATION honest obstruction (persona 1B): Einstein-frame potential.
# V(R) = (R F' - F)/(2 F'^2). Compute sign and the f'=0 pole.
# ---------------------------------------------------------------------------
V = sp.simplify((R*Fp - F)/(2*Fp**2))
num = sp.simplify(R*Fp - F)
check("C10 numerator R F' - F = -(R^2+18)/9 < 0 for all real R",
      sp.simplify(num - (-(R**2 + 18)/9)) == 0)
# denominator 2 F'^2 >= 0, zero only at R=3/2 -> V < 0 everywhere, pole at the F-max.
check("C11 Einstein-frame V(R) < 0 everywhere with a pole at R=3/2 (F'=0): "
      "NOT a Starobinsky plateau (wrong R^2 sign)",
      sp.simplify(Fp.subs(R, sp.Rational(3, 2))) == 0)
# sample: V(0) negative and finite
V0 = V.subs(R, 0)
check("C12 V(0) = -9 < 0 (finite, negative -- hilltop/AdS-like, not inflationary plateau)",
      sp.simplify(V0 - (-9)) == 0)

# ---------------------------------------------------------------------------
# PATTERN / SATURATION hooks (personas 3, 7): scalar dispersion peaks at k=0.
# Free scalaron dispersion omega^2 = k^2 + m^2, m^2<0 -> growth rate
# gamma(k) = sqrt(-m^2 - k^2) is MAXIMAL at k=0 (runaway), NOT finite-k (Turing).
# A finite-wavelength band would need the k^4 (massive spin-2) sector coupling.
# ---------------------------------------------------------------------------
k = sp.symbols('k', nonnegative=True)
m2val = sp.Rational(-1, 2)
growth2 = -m2val - k**2   # gamma^2 for the unstable scalar branch
dgdk = sp.diff(growth2, k)
check("C13 scalar-only growth^2 = 1/2 - k^2 is monotone-decreasing in k "
      "(peaks at k=0: RUNAWAY, not a finite-k Turing band by itself)",
      sp.simplify(dgdk - (-2*k)) == 0)
check("C14 unstable band k in [0, 1/sqrt(2)) (k_cut = sqrt(-m^2)); finite-k peak "
      "requires the R^2 k^4 / spin-2 sector (persona 3 open check)",
      sp.simplify(sp.sqrt(-m2val) - 1/sp.sqrt(2)) == 0)

print()
n_pass = sum(1 for _, ok in checks if ok)
print(f"{n_pass}/{len(checks)} checks passed")
assert n_pass == len(checks), "W155 checks FAILED"
print("W155 all checks exit 0")
