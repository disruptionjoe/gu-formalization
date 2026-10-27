#!/usr/bin/env python3
"""Exact scoped controls, not a derivation of a GU cosmology or physical spectrum."""
from itertools import product
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[2]
checks = []


def check(name, condition):
    assert bool(condition), name
    checks.append(name)


# Reproduce an existing diagnostic, not a new derivation from the native action.
owner = ROOT / "explorations/conditional-build/selected-second-layer-tt-euler-preboundary-helicity-2026-08-07.md"
text = owner.read_text()
check("inherited coefficient locators", all(x in text for x in
      ("15376/13689", "340/4563", "14356/13689", "1922/3589")))
A, B = s.Rational(15376, 13689), -s.Rational(340, 4563)
C4, C2 = A + B, A / 2
m2 = s.cancel(C2 / C4)
x, c = s.symbols("x c", real=True)
P = C4*x*x + C2*x
check("TT coefficients", (C4, C2, m2) ==
      (s.Rational(14356, 13689), s.Rational(7688, 13689), s.Rational(1922, 3589)))
check("distinct TT roots", s.expand(P-C4*x*(x+m2)) == 0 and m2 > 0)
check("opposite simple-pole derivatives", s.diff(P, x).subs(x, 0) == C2
      and s.diff(P, x).subs(x, -m2) == -C2 and C2 != 0)
check("not constant multiple of flat Bach", s.diff(P-c*x*x, x).subs(x, 0) != 0)
check("trace-only double-root countercontrol", s.diff(x*x, x).subs(x, 0) == 0)

# Three-dimensional radial flat biharmonic equation away from r=0.
r = s.symbols("r", positive=True)
n = s.symbols("n", integer=True)
lap = lambda f: s.diff(f, r, 2) + 2*s.diff(f, r)/r
check("radial biharmonic indicial polynomial",
      s.simplify(lap(lap(r**n))-n*(n+1)*(n-1)*(n-2)*r**(n-4)) == 0)
check("four vacuum radial modes", all(s.simplify(lap(lap(r**i))) == 0 for i in (-1, 0, 1, 2)))
check("non-biharmonic cubic countercontrol", s.simplify(lap(lap(r**3))) == 24/r)

# Full algebraic curvature tensor of FLRW in an orthonormal Lorentz frame.
# acc = a_ddot/a, sec = (a_dot^2+k)/a^2; these are independent here, so k is not fixed.
acc, sec, defect = s.symbols("acc sec defect", real=True)
eta = (-1, 1, 1, 1)
g = lambda i, j: eta[i] if i == j else s.S.Zero


def curvature(delta=s.S.Zero):
    R = s.MutableDenseNDimArray.zeros(4, 4, 4, 4)
    for i in range(4):
        for j in range(i+1, 4):
            value = -acc if i == 0 else sec
            if (i, j) == (0, 1):
                value += delta
            R[i, j, i, j] = R[j, i, j, i] = value
            R[i, j, j, i] = R[j, i, i, j] = -value
    return R


def weyl(R):
    Ric = s.Matrix(4, 4, lambda j, l: sum(eta[i]*R[i, j, i, l] for i in range(4)))
    scalar = s.expand(sum(eta[j]*Ric[j, j] for j in range(4)))
    C = []
    for i, j, k, l in product(range(4), repeat=4):
        C.append(s.expand(R[i, j, k, l] - s.Rational(1, 2)*(
            g(i, k)*Ric[j, l]-g(i, l)*Ric[j, k]
            -g(j, k)*Ric[i, l]+g(j, l)*Ric[i, k])
            +scalar*s.Rational(1, 6)*(g(i, k)*g(j, l)-g(i, l)*g(j, k))))
    return Ric, scalar, C


Ric, scalar, C = weyl(curvature())
check("FLRW Ricci contraction", Ric == s.diag(-3*acc, acc+2*sec, acc+2*sec, acc+2*sec))
check("FLRW scalar contraction", scalar == 6*(acc+sec))
check("all 256 Weyl components vanish", all(v == 0 for v in C))
check("anisotropic curvature countercontrol", any(v != 0 for v in weyl(curvature(defect))[2]))

# Distinct smooth flat-FLRW histories illustrate nonselection by pure C^2.
# They are not asserted solutions of any complete GU or conformal-matter action.
t, h = s.symbols("t h", positive=True)
histories = (s.exp(h*t), s.sqrt(t))
hubbles = [s.simplify(s.diff(a, t)/a) for a in histories]
scalars = [s.simplify(6*(s.diff(a, t, 2)/a+(s.diff(a, t)/a)**2)) for a in histories]
check("different conformally flat histories", hubbles == [h, 1/(2*t)] and scalars == [12*h*h, 0])

# AP is ruler-independent; absolute distances still require normalization.
z, H0, rd, light, integ, E = s.symbols("z H0 rd light integ E", positive=True)
DH, DM = light/(H0*E), light*integ/H0
F = s.cancel((DM/rd)/(DH/rd))
check("AP ruler and normalization cancel", F == E*integ)
u = s.symbols("u", nonnegative=True)
ap0 = z
ap2 = s.simplify((1+z)**2*s.integrate((1+u)**-2, (u, 0, z)))
check("distinct flat expansion shapes", ap2 == z*(1+z) and s.simplify(ap2-ap0) == z*z)

print(json.dumps({"status": "PASS", "exact_checks": len(checks), "checks": checks,
                  "scope": "inherited TT regression, curvature identities and observational algebra; no GU spectrum or cosmological fit"}, indent=2))
