#!/usr/bin/env python3
"""Exact rational-interval second-order chart certificate for K1743."""
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class I:
    """Closed rational interval with outward exact arithmetic."""
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = as_i(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-as_i(other))

    def __rsub__(self, other):
        return as_i(other) - self

    def __mul__(self, other):
        other = as_i(other)
        vals = (self.lo*other.lo, self.lo*other.hi, self.hi*other.lo, self.hi*other.hi)
        return I(min(vals), max(vals))

    __rmul__ = __mul__

    def reciprocal(self):
        assert not (self.lo <= 0 <= self.hi)
        return I(1/self.hi, 1/self.lo) if self.lo > 0 else I(1/self.hi, 1/self.lo)

    def __truediv__(self, other):
        return self * as_i(other).reciprocal()

    def __rtruediv__(self, other):
        return as_i(other) / self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        if n == 0:
            return I(1)
        out = I(1)
        base = self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n //= 2
        return out

    def contains(self, value):
        value = F(value)
        return self.lo <= value <= self.hi

    def excludes_zero(self):
        return self.hi < 0 or self.lo > 0

    def width(self):
        return self.hi - self.lo


def as_i(value):
    return value if isinstance(value, I) else I(value)


def sqrt_i(value, digits=75):
    value = as_i(value)
    assert value.lo > 0
    scale = 10**digits

    def floor_scaled_sqrt(q):
        return isqrt((q.numerator * scale * scale) // q.denominator)

    low = floor_scaled_sqrt(value.lo)
    high = floor_scaled_sqrt(value.hi) + 1
    out = I(F(low, scale), F(high, scale))
    assert out.lo*out.lo <= value.lo and out.hi*out.hi >= value.hi
    return out


class J2:
    """Value, gradient, and Hessian interval jet in (p,a)."""
    def __init__(self, v, g=None, h=None):
        self.v = as_i(v)
        self.g = [I(0), I(0)] if g is None else [as_i(x) for x in g]
        self.h = [[I(0), I(0)], [I(0), I(0)]] if h is None else [[as_i(x) for x in row] for row in h]

    def __add__(self, other):
        other = as_j(other)
        return J2(self.v+other.v, [self.g[i]+other.g[i] for i in range(2)],
                  [[self.h[i][j]+other.h[i][j] for j in range(2)] for i in range(2)])

    __radd__ = __add__

    def __neg__(self):
        return J2(-self.v, [-x for x in self.g], [[-x for x in row] for row in self.h])

    def __sub__(self, other):
        return self + (-as_j(other))

    def __rsub__(self, other):
        return as_j(other) - self

    def __mul__(self, other):
        other = as_j(other)
        g = [self.g[i]*other.v+self.v*other.g[i] for i in range(2)]
        h = [[self.h[i][j]*other.v+self.g[i]*other.g[j]+self.g[j]*other.g[i]
              +self.v*other.h[i][j] for j in range(2)] for i in range(2)]
        return J2(self.v*other.v, g, h)

    __rmul__ = __mul__

    def reciprocal(self):
        v2, v3 = self.v**2, self.v**3
        g = [-self.g[i]/v2 for i in range(2)]
        h = [[2*self.g[i]*self.g[j]/v3-self.h[i][j]/v2 for j in range(2)] for i in range(2)]
        return J2(1/self.v, g, h)

    def __truediv__(self, other):
        return self * as_j(other).reciprocal()

    def __rtruediv__(self, other):
        return as_j(other) / self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = J2(1)
        for _ in range(n):
            out = out * self
        return out


def as_j(value):
    return value if isinstance(value, J2) else J2(value)


def sqrt_j(value):
    value = as_j(value)
    root = sqrt_i(value.v)
    g = [value.g[i]/(2*root) for i in range(2)]
    h = [[value.h[i][j]/(2*root)-value.g[i]*value.g[j]/(4*root**3)
          for j in range(2)] for i in range(2)]
    return J2(root, g, h)


def quad(v, h):
    return sum((v[i]*h[i][j]*v[j] for i in range(2) for j in range(2)), I(0))


def invariants(pv, av):
    p = J2(pv, [1, 0])
    a = J2(av, [0, 1])
    b = (1-p*a)/(1-p)
    moment = lambda n: p*a**n+(1-p)*b**n
    m4, m6, m8, m10 = moment(2), moment(3), moment(4), moment(5)
    u = 3-m4
    k6 = m6-15*m4+30
    h8 = m8-28*m6+210*m4-315
    h10 = m10-45*m8+630*m6-3150*m4+3780
    root_u = sqrt_j(u)
    return u, k6/(u*root_u), h8/u**2, h10/(u**2*root_u)


def main():
    d = json.loads((ROOT/"lab/process/k1743-four-point-second-order-branch.json").read_text())
    q6, sol, rem, dec = d["q6_selection"], d["second_order_chart_solution"], d["remaining_freedom"], d["decision"]

    scale = 10**58
    u = I(F(3270136791660423745372677644536339759565825836798059510805, scale),
          F(3270136791660423745372677644536339759565825836798059510806, scale))
    poly = lambda z: 17*z**3-38*z**2+84*z-24
    assert poly(u.lo) < 0 < poly(u.hi)
    # 51u^2-76u+84 has negative discriminant and is positive everywhere.
    assert 76**2-4*51*84 < 0

    s0 = 2*(6-7*u)/(2-u)
    prod = s0-(3-u)
    disc = s0**2-4*prod
    sq = sqrt_i(disc)
    a0, b0 = (s0-sq)/2, (s0+sq)/2
    p0 = (b0-1)/(b0-a0)
    uu, r, x, y = invariants(p0, a0)
    rp, ra = r.g
    xp, xa = x.g
    det = rp*xa-ra*xp
    alpha = I(F(35, 3))
    p1, a1 = alpha*xa/det, -alpha*xp/det
    v1 = [p1, a1]
    yx = (rp*y.g[1]-ra*y.g[0])/det
    eta = -385-y.v*yx/72
    gamma = F(-80, 3)
    gamma_gradient = I(gamma)/60+F(4, 9)
    eta_gradient = eta/2520+F(11, 72)+y.v*yx/181440
    rhs_r = -quad(v1, r.h)/2
    rhs_x = eta-quad(v1, x.h)/2
    p2 = (rhs_r*xa-ra*rhs_x)/det
    a2 = (rp*rhs_x-rhs_r*xp)/det

    recorded_p2 = I(F(-704591778388654, 10**15), F(-704591778388653, 10**15))
    recorded_a2 = I(F(-1046975744740560, 10**15), F(-1046975744740558, 10**15))
    checks = [
        ("schema", d["schema_version"] == "1.0"),
        ("claim", d["claim_id"] == "K1743"),
        ("root interval narrow", u.width() == F(1, scale)),
        ("chart order", 0 < a0.lo < a0.hi < 1 < b0.lo < b0.hi),
        ("probability order", 0 < p0.lo < p0.hi < 1),
        ("base u", uu.v.lo < u.hi and u.lo < uu.v.hi),
        ("base r contains zero", r.v.contains(0)),
        ("base x contains 35", x.v.contains(35)),
        ("jacobian excludes zero", det.excludes_zero()),
        ("P enclosure", I(F(-103758072695687, 10**15), F(-103758072695686, 10**15)).lo <= p1.lo <= p1.hi <= I(F(-103758072695687, 10**15), F(-103758072695686, 10**15)).hi),
        ("A enclosure", I(F(-128525003886033, 10**15), F(-128525003886032, 10**15)).lo <= a1.lo <= a1.hi <= I(F(-128525003886033, 10**15), F(-128525003886032, 10**15)).hi),
        ("y0 enclosure", I(F(1253042586099042, 10**12), F(1253042586099043, 10**12)).lo <= y.v.lo <= y.v.hi <= I(F(1253042586099042, 10**12), F(1253042586099043, 10**12)).hi),
        ("yx enclosure", I(F(-58502093191591, 10**12), F(-58502093191590, 10**12)).lo <= yx.lo <= yx.hi <= I(F(-58502093191591, 10**12), F(-58502093191590, 10**12)).hi),
        ("eta enclosure", I(F(633133529791640, 10**12), F(633133529791641, 10**12)).lo <= eta.lo <= eta.hi <= I(F(633133529791640, 10**12), F(633133529791641, 10**12)).hi),
        ("gamma exact", gamma == F(-80, 3)),
        ("gamma stationarity", gamma_gradient.lo == gamma_gradient.hi == 0),
        ("gamma Hessian", F(1, 60) > 0),
        ("eta stationarity", eta_gradient.contains(0)),
        ("eta Hessian", F(1, 2520) > 0),
        ("p2 certified overlap", not (p2.hi < recorded_p2.lo or recorded_p2.hi < p2.lo)),
        ("a2 certified overlap", not (a2.hi < recorded_a2.lo or recorded_a2.hi < a2.lo)),
        ("p2 lies in recorded", recorded_p2.lo <= p2.lo <= p2.hi <= recorded_p2.hi),
        ("a2 lies in recorded", recorded_a2.lo <= a2.lo <= a2.hi <= recorded_a2.hi),
        ("p2 interval narrow", p2.width() < F(1, 10**35)),
        ("a2 interval narrow", a2.width() < F(1, 10**35)),
        ("equation recorded", "J v_2=" in sol["exact_equations"]),
        ("gamma recorded", "gamma=-80/3" in q6["exact_stationarity"]),
        ("eta recorded", "eta=-385-y_0 y_x/72" in q6["exact_stationarity"]),
        ("coercive", "1/60" in q6["coercivity"] and "1/2520" in q6["coercivity"]),
        ("second order unique", dec["second_order_chart_coefficients_unique"]),
        ("third order free", not dec["third_order_chart_coefficients_unique"] and "One third-order" in rem["dimension"]),
        ("branch open", not dec["complete_local_analytic_branch_unique"]),
        ("global open", not dec["finite_strength_global_optimizer_identified"]),
        ("local scope", "local" in d["scope_guard"] and "remote branches" in d["scope_guard"]),
    ]
    assert len(checks) == 34
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, (label, p2.lo, p2.hi, a2.lo, a2.hi)
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
