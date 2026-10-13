#!/usr/bin/env python3
"""Exact matched-series and cubic-field certificate for K1742."""
import json
from decimal import Decimal, getcontext
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAX = 12


class Series:
    def __init__(self, values=0):
        if isinstance(values, Series):
            self.c = values.c[:]
        elif isinstance(values, list):
            self.c = [F(x) for x in values] + [F(0)] * (MAX + 1 - len(values))
            self.c = self.c[:MAX + 1]
        else:
            self.c = [F(values)] + [F(0)] * MAX

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
        out = [F(0)] * (MAX + 1)
        for i, a in enumerate(self.c):
            for j, b in enumerate(other.c[:MAX + 1 - i]):
                out[i + j] += a * b
        return Series(out)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return Series([x / F(scalar) for x in self.c])

    def __pow__(self, power):
        result, base = Series(1), self
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power //= 2
        return result

    def shift(self, amount):
        return Series([F(0)] * amount + self.c[:MAX + 1 - amount])


def matched_coefficients(gamma, eta, y0, y1, y2, z0, tail):
    delta, epsilon, theta, iota, z1 = tail
    r = Series([0, F(35, 3), 0, gamma, delta, epsilon])
    x = Series([35, 0, eta, theta, iota])
    y = Series([y0, y1, y2])
    z = Series([z0, z1])
    laws = {
        4: Series(F(1, 6)),
        6: F(1, 4) + r**2 / 120,
        7: -F(7, 36) * r,
        8: (x**2 - 70*x + 7455 + 420*r**2) / 5040,
        9: r * (9*x - 855 - 5*r**2) / 360,
        10: (y**2 + 420*y*r + 1260*x**2 - 138600*x - 3150*x*r**2
             + 5658660 + 680190*r**2) / 362880,
        11: -F(11, 302400) * (21210*r**3 + 21*r**2*y + 70*r*x**2 - 22960*r*x
                              + 1162350*r - 20*x*y + 700*y),
        12: (5416026*r**4 - 25391520*r**2*x - 924*r**2*z + 2184571620*r**2
             - 27720*r*x*y + 3437280*r*y - 11550*x**3 + 5174235*x**2
             + 990*x*z - 406340550*x + 2970*y**2 + z**2 - 23100*z
             + 10313399250) / 39916800,
    }
    total = Series(0)
    for order, law in laws.items():
        total += law.shift(order)
    return total.c[11], total.c[12]


def expected12(gamma, eta, y0, y1, y2, z0):
    return F(1, 119750400) * (
        23760*eta**2 + 18295200*eta + 997920*gamma**2 + 53222400*gamma
        + 8910*y0**2 + 660*y0*y2 + 330*y1**2 + 1617000*y1
        + 3*z0**2 + 34650*z0 + 6173349875
    )


class Q:
    """Element c0+c1*u+c2*u^2 of Q[u]/(17u^3-38u^2+84u-24)."""
    def __init__(self, c0=0, c1=0, c2=0):
        self.c = (F(c0), F(c1), F(c2))

    def __add__(self, other):
        other = other if isinstance(other, Q) else Q(other)
        return Q(*(a + b for a, b in zip(self.c, other.c)))

    __radd__ = __add__

    def __neg__(self):
        return Q(*(-x for x in self.c))

    def __sub__(self, other):
        return self + (-(other if isinstance(other, Q) else Q(other)))

    def __rsub__(self, other):
        return Q(other) - self

    def __mul__(self, other):
        other = other if isinstance(other, Q) else Q(other)
        coefficients = [F(0)] * 5
        for i, a in enumerate(self.c):
            for j, b in enumerate(other.c):
                coefficients[i + j] += a * b
        for degree in (4, 3):
            value = coefficients[degree]
            coefficients[degree] = 0
            coefficients[degree - 1] += F(38, 17) * value
            coefficients[degree - 2] -= F(84, 17) * value
            coefficients[degree - 3] += F(24, 17) * value
        return Q(*coefficients[:3])

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return Q(*(x / F(scalar) for x in self.c))

    def __eq__(self, other):
        other = other if isinstance(other, Q) else Q(other)
        return self.c == other.c

    def eval(self, u):
        return sum(Decimal(x.numerator) / Decimal(x.denominator) * u**i for i, x in enumerate(self.c))


def root():
    getcontext().prec = 70
    lo, hi = Decimal("0.3270136791"), Decimal("0.3270136792")
    poly = lambda u: 17*u**3 - 38*u**2 + 84*u - 24
    assert poly(lo) < 0 < poly(hi)
    for _ in range(230):
        mid = (lo + hi) / 2
        if poly(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    data = json.loads((ROOT / "lab/process/k1742-matched-second-order-selection.json").read_text())
    law, chart, decision = data["matched_composition"], data["chart_selection"], data["decision"]
    samples = [
        (F(-80, 3), F(7), F(11), F(-13), F(17), F(-19), (F(2), F(3), F(5), F(7), F(11))),
        (F(4), F(-9, 2), F(23, 3), F(29, 5), F(-31, 7), F(37, 11), (F(-2), F(5), F(-7), F(13), F(-17))),
        (F(-5, 8), F(41, 6), F(-43, 9), F(47, 10), F(53, 12), F(-59, 13), (F(3), F(-4), F(8), F(-9), F(14))),
    ]
    checks = [("schema", data["schema_version"] == "1.0"), ("claim", data["claim_id"] == "K1742")]
    for i, sample in enumerate(samples, 1):
        gamma, eta, y0, y1, y2, z0, tail = sample
        c11, c12 = matched_coefficients(*sample)
        checks += [
            (f"eleven-halves sample {i}", c11 == y0*(y1 + 2450) / 181440),
            (f"sixth sample {i}", c12 == expected12(gamma, eta, y0, y1, y2, z0)),
        ]

    inv_u = Q(84, -38, 17) / 24
    y0_sqrt_u = F(5, 2) * Q(372, -300, 119)
    yx_sqrt_u = -Q(132, 0, 17) / 4
    y0_yx = y0_sqrt_u * yx_sqrt_u * inv_u
    expected_product = -F(5, 2) * Q(33780, -16428, 8551)
    eta_star = Q(-385) - y0_yx / 72
    expected_eta = F(5, 144) * Q(22692, -16428, 8551)
    y1 = -F(35, 48) * Q(19404, -7764, 4097)
    q11_sqrt_u = y0_sqrt_u * (y1 + 2450) / 181440
    expected_q11_sqrt_u = -F(5, 62208) * Q(558420, -219948, 122111)
    q6_a = Q(F(1, 5040))
    q6_b = -Q(22692, -16428, 8551) / 72576
    q6_c = Q(19318292611092, -7922860068588, 4157570075183) / 24601522176
    q6_min = q6_c - q6_a * eta_star * eta_star
    expected_q6_min = Q(5754743605564, -2519891655876, 1319167228301) / 8200507392
    u = root()
    checks += [
        ("classification", data["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("not a kill", data["target_claim"] == "NONE-NOT-A-KILL"),
        ("field inverse", Q(0, 1) * inv_u == Q(1)),
        ("y0Yx field product", y0_yx == expected_product),
        ("eta field center", eta_star == expected_eta),
        ("q11 field value", q11_sqrt_u == expected_q11_sqrt_u),
        ("q6 eta center from derivative", q6_b + 2*q6_a*eta_star == Q(0)),
        ("q6 exact minimum", q6_min == expected_q6_min),
        ("eta decimal", abs(eta_star.eval(u) - Decimal("633.133529791640596111297145796")) < Decimal("1e-27")),
        ("q6 decimal", abs(q6_min.eval(u) - Decimal("618.470706254850014084939899775")) < Decimal("1e-27")),
        ("eleven-halves blind", "independent of eta and gamma" in law["eleven_halves_selection"]),
        ("completed square", "(gamma+80/3)^2/120" in law["completed_square"]),
        ("eta square", "(eta-eta_*)^2/5040" in law["completed_square"]),
        ("gamma center", "gamma_*=-80/3" in law["selected_centers"]),
        ("jacobian uniqueness", "det d(kappa_6,x)/d(p,a) is nonzero" in chart["second_order"]),
        ("third order remains", "One third-order chart degree of freedom" in chart["third_order_boundary"]),
        ("q11 no selector", not decision["q_eleven_halves_selects_second_order_chart"]),
        ("q6 first selector", decision["q_six_is_first_later_second_order_selector"]),
        ("second order unique", decision["remaining_second_order_chart_motion_unique"]),
        ("third order open", not decision["third_order_chart_motion_unique"]),
        ("branch open", not decision["complete_local_analytic_branch_unique"]),
        ("finite strength open", not decision["finite_strength_branch_certified"]),
        ("remote boundary open", not decision["remote_or_singular_boundaries_excluded"]),
        ("physical status fixed", not decision["source_or_physical_status_changed"]),
        ("moving remainder guard", "uniform moving-seed remainder" in data["scope_guard"]),
    ]
    assert len(checks) == 33
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
