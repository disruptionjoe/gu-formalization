#!/usr/bin/env python3
"""Arbitrary-precision exact-chart third-order transport certificate for K1748."""
import json
from decimal import Decimal as D, getcontext
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
getcontext().prec = 80
MAX = 3


class Series:
    def __init__(self, values=0):
        if isinstance(values, Series):
            self.c = values.c[:]
        elif isinstance(values, list):
            self.c = [x if isinstance(x, D) else D(str(x)) for x in values] + [D(0)] * (MAX + 1 - len(values))
            self.c = self.c[:MAX + 1]
        else:
            self.c = [values if isinstance(values, D) else D(str(values))] + [D(0)] * MAX

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
            out[n] = (self.c[n] - sum(out[i] * out[n - i] for i in range(1, n))) / (2*out[0])
        return Series(out)


def root():
    lo, hi = D("0.3270136791"), D("0.3270136792")
    poly = lambda u: 17*u**3 - 38*u**2 + 84*u - 24
    for _ in range(280):
        mid = (lo + hi) / 2
        if poly(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def invariants(p_coefficients, a_coefficients):
    p, a = Series(p_coefficients), Series(a_coefficients)
    b = (1 - p*a) / (1 - p)
    moment = lambda n: p*a**n + (1 - p)*b**n
    m4, m6, m8 = moment(2), moment(3), moment(4)
    u = 3 - m4
    k6 = m6 - 15*m4 + 30
    h8 = m8 - 28*m6 + 210*m4 - 315
    return k6/(u*u.sqrt()), h8/u**2


def main():
    data = json.loads((ROOT / "lab/process/k1748-four-point-third-order-branch.json").read_text())
    solution, remaining, decision = data["third_order_chart_solution"], data["remaining_freedom"], data["decision"]
    u = root()
    support_sum = 2*(6 - 7*u)/(2 - u)
    support_product = support_sum - (3 - u)
    discriminant = support_sum**2 - 4*support_product
    a0 = (support_sum - discriminant.sqrt())/2
    b0 = (support_sum + discriminant.sqrt())/2
    p0 = (b0 - 1)/(b0 - a0)
    eta = D(5)/144*(8551*u*u - 16428*u + 22692)
    theta = u.sqrt()*(-D(115170985)/5136 + D(154557365)/15408*u - D(329295185)/61632*u*u)
    target_r = [D(0), D(35)/3, D(0), -D(80)/3]
    target_x = [D(35), D(0), eta, theta]
    p = [p0] + [D(0)] * MAX
    a = [a0] + [D(0)] * MAX
    determinants = []
    for n in range(1, MAX + 1):
        p[n] = a[n] = D(0)
        r0, x0 = invariants(p, a)
        base = (r0.c[n], x0.c[n])
        p[n], a[n] = D(1), D(0)
        rp, xp = invariants(p, a)
        column_p = (rp.c[n] - base[0], xp.c[n] - base[1])
        p[n], a[n] = D(0), D(1)
        ra, xa = invariants(p, a)
        column_a = (ra.c[n] - base[0], xa.c[n] - base[1])
        determinant = column_p[0]*column_a[1] - column_a[0]*column_p[1]
        determinants.append(determinant)
        rhs_r, rhs_x = target_r[n] - base[0], target_x[n] - base[1]
        p[n] = (rhs_r*column_a[1] - column_a[0]*rhs_x)/determinant
        a[n] = (column_p[0]*rhs_x - rhs_r*column_p[1])/determinant
    r, x = invariants(p, a)
    tol = D("1e-65")
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1748"),
        ("classification", data["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("not a kill", data["target_claim"] == "NONE-NOT-A-KILL"),
        ("root residual", abs(17*u**3 - 38*u**2 + 84*u - 24) < D("1e-70")),
        ("chart order", 0 < a0 < 1 < b0 and 0 < p0 < 1),
        ("jacobian nonzero", all(abs(value) > D(90000) for value in determinants)),
        ("P", abs(p[1] - D("-0.1037580726956868180098412425224564")) < D("1e-34")),
        ("A", abs(a[1] - D("-0.1285250038860326462269688806201854")) < D("1e-34")),
        ("P2", abs(p[2] - D("-0.7045917783886536388640680138475619")) < D("1e-34")),
        ("A2", abs(a[2] - D("-1.0469757447405592350794876880442772")) < D("1e-34")),
        ("theta", abs(theta - D("-11274.244832460378296020699504155082")) < D("1e-30")),
        ("P3", abs(p[3] - D("2.5305736887297247364270697280408398")) < D("1e-34")),
        ("A3", abs(a[3] - D("4.7486091917613828954999629940207666")) < D("1e-34")),
        ("r1", abs(r.c[1] - target_r[1]) < tol),
        ("r2", abs(r.c[2] - target_r[2]) < tol),
        ("r3", abs(r.c[3] - target_r[3]) < tol),
        ("x1", abs(x.c[1] - target_x[1]) < tol),
        ("x2", abs(x.c[2] - target_x[2]) < tol),
        ("x3", abs(x.c[3] - target_x[3]) < D("1e-62")),
        ("exact equation recorded", "Jv_3=" in solution["exact_equations"]),
        ("det recorded", "det J is nonzero" in solution["uniqueness"]),
        ("P3 recorded", "2.530573688729724736" in solution["reported_solution"]),
        ("A3 recorded", "4.748609191761382895" in solution["reported_solution"]),
        ("fourth degree open", "x_4" in remaining["dimension"]),
        ("third unique", decision["third_order_chart_coefficients_unique"]),
        ("fourth chart open", not decision["fourth_order_chart_coefficients_unique"]),
        ("branch open", not decision["complete_local_analytic_branch_unique"]),
        ("global open", not decision["finite_strength_global_optimizer_identified"]),
        ("physical fixed", not decision["source_or_physical_status_changed"]),
        ("factor-six guard", "factor of six" in data["post_flight"]["mistyping_check"]),
        ("counterexample seam", "different x_4 values" in data["post_flight"]["counterexample_seam"]),
        ("local scope", "u=q singular face" in data["scope_guard"] and "complete branch" in data["scope_guard"]),
    ]
    assert len(checks) == 33
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, (label, p, a, r.c, x.c, determinants)
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
