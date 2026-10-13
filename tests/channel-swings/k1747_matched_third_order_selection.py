#!/usr/bin/env python3
"""Exact algebraic centers and high-precision recurrence replay for K1747."""
import json
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
getcontext().prec = 70
MAX = 14


class Q:
    """Q[u]/(17u^3-38u^2+84u-24)."""
    def __init__(self, a=0, b=0, c=0):
        self.c = (F(a), F(b), F(c))

    def __add__(self, other):
        other = other if isinstance(other, Q) else Q(other)
        return Q(*(self.c[i] + other.c[i] for i in range(3)))

    __radd__ = __add__

    def __neg__(self):
        return Q(*(-x for x in self.c))

    def __sub__(self, other):
        return self + (-(other if isinstance(other, Q) else Q(other)))

    def __rsub__(self, other):
        return Q(other) - self

    def __mul__(self, other):
        other = other if isinstance(other, Q) else Q(other)
        out = [F(0)] * 5
        for i, a in enumerate(self.c):
            for j, b in enumerate(other.c):
                out[i + j] += a * b
        for degree in (4, 3):
            value = out[degree]
            out[degree] = 0
            out[degree - 1] += F(38, 17) * value
            out[degree - 2] -= F(84, 17) * value
            out[degree - 3] += F(24, 17) * value
        return Q(*out[:3])

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return Q(*(x / F(scalar) for x in self.c))

    def __eq__(self, other):
        other = other if isinstance(other, Q) else Q(other)
        return self.c == other.c

    def eval(self, u):
        return sum(D(x.numerator) / D(x.denominator) * u**i for i, x in enumerate(self.c))


class Series:
    def __init__(self, values=0):
        def as_decimal(value):
            if isinstance(value, D):
                return value
            if isinstance(value, F):
                return D(value.numerator) / D(value.denominator)
            return D(str(value))

        if isinstance(values, Series):
            self.c = values.c[:]
        elif isinstance(values, list):
            self.c = [as_decimal(x) for x in values] + [D(0)] * (MAX + 1 - len(values))
            self.c = self.c[:MAX + 1]
        else:
            self.c = [as_decimal(values)] + [D(0)] * MAX

    def __add__(self, other):
        other = Series(other)
        return Series([a + b for a, b in zip(self.c, other.c)])

    __radd__ = __add__

    def __neg__(self):
        return Series([-x for x in self.c])

    def __sub__(self, other):
        return self + (-Series(other))

    def __rsub__(self, other):
        return Series(other) - self

    def __mul__(self, other):
        other = Series(other)
        out = [D(0)] * (MAX + 1)
        for i, a in enumerate(self.c):
            for j, b in enumerate(other.c[:MAX + 1 - i]):
                out[i + j] += a * b
        return Series(out)

    __rmul__ = __mul__

    def inverse(self):
        out = [D(0)] * (MAX + 1)
        out[0] = 1 / self.c[0]
        for n in range(1, MAX + 1):
            out[n] = -sum(self.c[i] * out[n - i] for i in range(1, n + 1)) / self.c[0]
        return Series(out)

    def __truediv__(self, other):
        return self * Series(other).inverse()

    def __rtruediv__(self, other):
        return Series(other) / self

    def __pow__(self, n):
        out, base = Series(1), self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n //= 2
        return out

    def sqrt(self):
        out = [self.c[0].sqrt()] + [D(0)] * MAX
        for n in range(1, MAX + 1):
            out[n] = (self.c[n] - sum(out[i] * out[n - i] for i in range(1, n))) / (2 * out[0])
        return Series(out)

    def shift(self, n):
        return Series([D(0)] * n + self.c[:MAX + 1 - n])


def root():
    lo, hi = D("0.3270136791"), D("0.3270136792")
    poly = lambda u: 17*u**3 - 38*u**2 + 84*u - 24
    for _ in range(240):
        mid = (lo + hi) / 2
        if poly(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def derived_invariants(r, x, u0):
    coefficients = [u0] + [D(0)] * MAX

    def recurrence(u):
        m2 = 3 - u
        m3 = u * u.sqrt() * r + 15 - 15*u
        support_sum = (m3 - m2) / (m2 - 1)
        support_product = support_sum - m2
        m4 = support_sum*m3 - support_product*m2
        h8 = m4 - 28*m3 + 210*m2 - 315
        return h8/u**2 - x, (m2, m3, m4, support_sum, support_product)

    for n in range(1, 5):
        coefficients[n] = D(0)
        f0 = recurrence(Series(coefficients))[0].c[n]
        coefficients[n] = D(1)
        f1 = recurrence(Series(coefficients))[0].c[n]
        coefficients[n] = -f0 / (f1 - f0)
    u = Series(coefficients)
    _, (m2, m3, m4, support_sum, support_product) = recurrence(u)
    m5 = support_sum*m4 - support_product*m3
    m6 = support_sum*m5 - support_product*m4
    m7 = support_sum*m6 - support_product*m5
    h10 = m5 - 45*m4 + 630*m3 - 3150*m2 + 3780
    h12 = m6 - 66*m5 + 1485*m4 - 13860*m3 + 51975*m2 - 62370 + 10395
    h14 = m7 - 91*m6 + 3003*m5 - 45045*m4 + 315315*m3 - 945945*m2 + 945945 - 135135
    return h10/(u**2*u.sqrt()), h12/u**3, h14/(u**3*u.sqrt())


def objective(delta, theta, u, eta):
    r = Series([0, D(35)/3, 0, -D(80)/3, delta])
    x = Series([35, 0, eta, theta])
    y, z, w = derived_invariants(r, x, u)
    laws = {
        4: Series(F(1, 6)),
        6: F(1, 4) + r*r/120,
        7: -F(7, 36)*r,
        8: (x*x - 70*x + 7455 + 420*r*r)/5040,
        9: r*(9*x - 855 - 5*r*r)/360,
        10: (y*y + 420*y*r + 1260*x*x - 138600*x - 3150*x*r*r + 5658660 + 680190*r*r)/362880,
        11: -F(11, 302400)*(21210*r**3 + 21*r*r*y + 70*r*x*x - 22960*r*x + 1162350*r - 20*x*y + 700*y),
        12: (5416026*r**4 - 25391520*r*r*x - 924*r*r*z + 2184571620*r*r - 27720*r*x*y + 3437280*r*y - 11550*x**3 + 5174235*x*x + 990*x*z - 406340550*x + 2970*y*y + z*z - 23100*z + 10313399250)/39916800,
        13: -F(303667, 288)*r + F(1045889, 25920)*r**3 + F(23257, 720)*r*x - F(4199, 3456)*y + F(7553, 43200)*r**3*x - F(4433, 20160)*r*x*x - F(2249, 25920)*r*r*y + F(4693, 120960)*x*y + F(13, 3240)*r*z - F(13, 86400)*x*x*y - F(13, 181440)*r*y*y - F(13, 302400)*r*x*z + F(13, 1088640)*y*z,
        14: F(14236183, 2304) + F(5230869, 2560)*r*r - F(48181, 144)*x + F(954499, 57600)*r**4 - F(719411, 17280)*r*r*x + F(136111, 23040)*x*x + F(2359, 480)*r*y - F(511, 6912)*z + F(2581, 25600)*r*r*x*x + F(7, 240)*r**3*y - F(7, 240)*x**3 + F(40471, 518400)*r*x*y - F(1043, 172800)*r*r*z + F(107, 25600)*y*y + F(301, 103680)*x*z + F(7, 103680)*r*w - F(7, 207360)*x*y*y - F(7, 518400)*x*x*z - F(1, 69120)*r*y*z - F(1, 1036800)*r*x*w + F(1, 1036800)*z*z + F(1, 3110400)*y*w + F(1, 6227020800)*w*w,
    }
    total = Series(0)
    for order, law in laws.items():
        total += law.shift(order)
    return total


def dec(q):
    return D(q.numerator) / D(q.denominator)


def main():
    data = json.loads((ROOT / "lab/process/k1747-matched-third-order-selection.json").read_text())
    comp, boundary, decision = data["matched_composition"], data["selection_boundary"], data["decision"]
    u = root()
    eta_q = F(5, 144) * Q(22692, -16428, 8551)
    c13_q = Q(F(-1106156462305219, 146242381824), F(1199574446836877, 358958573568), F(-3070510880607707, 1754908581888))
    delta_q = Q(F(1445435, 2016), F(-635045, 2016), F(3955475, 24192))
    theta_q = Q(F(-115170985, 5136), F(154557365, 15408), F(-329295185, 61632))
    c7_q = Q(F(12332720769441440108771, 615151615026364416), F(-1815428110971411518207, 205050538342121472), F(4893667392875414390381, 1054545625759481856))
    eta = eta_q.eval(u)
    sqrt_u = u.sqrt()
    delta = sqrt_u * delta_q.eval(u)
    theta = sqrt_u * theta_q.eval(u)
    c13 = sqrt_u * c13_q.eval(u)
    c7 = c7_q.eval(u)
    base = objective(D(0), D(0), u, eta)
    dp, dm = objective(D(1), D(0), u, eta), objective(D(-1), D(0), u, eta)
    tp, tm = objective(D(0), D(1), u, eta), objective(D(0), D(-1), u, eta)
    linear_delta = (dp.c[14] - dm.c[14]) / 2
    square_delta = (dp.c[14] + dm.c[14]) / 2 - base.c[14]
    linear_theta = (tp.c[14] - tm.c[14]) / 2
    square_theta = (tp.c[14] + tm.c[14]) / 2 - base.c[14]
    selected = objective(delta, theta, u, eta)
    tol = D("1e-50")
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1747"),
        ("cubic field", Q(0, 1)**3 if False else Q(0)),
        ("eta decimal", abs(eta - D("633.133529791640596111297145796179")) < D("1e-30")),
        ("delta decimal", abs(delta - D("361.098949224460002161412005610689")) < D("1e-30")),
        ("theta decimal", abs(theta - D("-11274.2448324603782960206995041551")) < D("1e-28")),
        ("c13 decimal", abs(c13 - D("-3807.46622100699525543917367061619")) < D("1e-28")),
        ("c7 decimal", abs(c7 - D("17649.2758735076487445695516903179")) < D("1e-28")),
        ("c13 recurrence", abs(base.c[13] - c13) < tol),
        ("c13 delta blind", abs(dp.c[13] - dm.c[13]) < tol),
        ("c13 theta blind", abs(tp.c[13] - tm.c[13]) < tol),
        ("delta square", abs(square_delta - D(1)/120) < tol),
        ("theta square", abs(square_theta - D(1)/5040) < tol),
        ("delta stationarity", abs(linear_delta + delta/D(60)) < tol),
        ("theta stationarity", abs(linear_theta + theta/D(2520)) < tol),
        ("selected coefficient", abs(selected.c[14] - c7) < D("1e-45")),
        ("q13 blind recorded", "independent of delta=r_4 and theta=x_3" in comp["thirteen_halves_selection"]),
        ("completed square", "(delta-delta_*)^2/120" in comp["seven_completed_square"]),
        ("theta square recorded", "(theta-theta_*)^2/5040" in comp["seven_completed_square"]),
        ("first selector", "q^7 is the first" in boundary["first_theta_selector"]),
        ("fourth order open", "x_4" in boundary["fourth_order"]),
        ("q13 decision", not decision["q_thirteen_halves_selects_theta"]),
        ("q7 decision", decision["q_seven_is_first_theta_selector"]),
        ("third invariant unique", decision["third_order_invariant_jet_unique"]),
        ("branch open", not decision["complete_local_analytic_branch_unique"]),
        ("finite strength open", not decision["finite_strength_branch_certified"]),
        ("remote open", not decision["remote_or_singular_boundaries_excluded"]),
        ("physical fixed", not decision["source_or_physical_status_changed"]),
        ("counterexample seam", "Arbitrary x_4 paths" in data["post_flight"]["counterexample_seam"]),
        ("local scope", "u=q singular face" in data["scope_guard"]),
    ]
    checks[2] = ("cubic field", Q(0, 1)*Q(0, 1)*Q(0, 1) == Q(24, -84, 38)/17)
    assert len(checks) == 30
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, (label, base.c[13], c13, selected.c[14], c7)
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
