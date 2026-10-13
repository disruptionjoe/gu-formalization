#!/usr/bin/env python3
"""Rational interval certificate and finite-channel boundary control for K1744.

The interval layer below uses only ``fractions.Fraction``.  It certifies
algebraic chart data and the axis-frozen singular-boundary comparison.  The
Gaussian-mixture Fisher values are deliberately kept in a separate ordinary
floating layer: scipy's quadrature is not an interval integrator.
"""
from __future__ import annotations

import importlib.util
import json
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1744-interval-finite-channel-boundary.json"


class I:
    """Closed rational interval with elementary outward operations."""

    SCALE = 10 ** 50

    def __init__(self, lo, hi=None):
        raw_lo = lo if isinstance(lo, Q) else Q(lo)
        raw_hi = raw_lo if hi is None else (hi if isinstance(hi, Q) else Q(hi))
        # Fixed decimal rational rounding prevents denominator explosion while
        # preserving an auditable outward enclosure after every operation.
        lo_n = (raw_lo.numerator * self.SCALE) // raw_lo.denominator
        hi_floor = (raw_hi.numerator * self.SCALE) // raw_hi.denominator
        hi_n = hi_floor if Q(hi_floor, self.SCALE) == raw_hi else hi_floor + 1
        self.lo = Q(lo_n, self.SCALE)
        self.hi = Q(hi_n, self.SCALE)
        assert self.lo <= self.hi

    @staticmethod
    def lift(value):
        return value if isinstance(value, I) else I(value)

    def __add__(self, other):
        other = self.lift(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __rsub__(self, other):
        return self.lift(other) - self

    def __mul__(self, other):
        other = self.lift(other)
        products = (self.lo * other.lo, self.lo * other.hi,
                    self.hi * other.lo, self.hi * other.hi)
        return I(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.lift(other)
        assert not (other.lo <= 0 <= other.hi)
        return self * I(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return self.lift(other) / self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        if n == 0:
            return I(1)
        if n % 2 == 0 and self.lo < 0 < self.hi:
            return I(0, max(self.lo ** n, self.hi ** n))
        values = (self.lo ** n, self.hi ** n)
        return I(min(values), max(values))

    def sqrt(self, digits=45):
        assert self.lo >= 0
        scale = 10 ** digits

        def lower(x):
            return Q(isqrt((x.numerator * scale * scale) // x.denominator), scale)

        lo = lower(self.lo)
        hi0 = lower(self.hi)
        hi = hi0 if hi0 * hi0 == self.hi else hi0 + Q(1, scale)
        assert lo * lo <= self.lo and hi * hi >= self.hi
        return I(lo, hi)

    def subset(self, other):
        other = self.lift(other)
        return other.lo <= self.lo and self.hi <= other.hi


class Jet:
    """Value and two chart partials over rational intervals."""

    def __init__(self, value, dp=0, da=0):
        self.v, self.dp, self.da = I.lift(value), I.lift(dp), I.lift(da)

    @staticmethod
    def lift(value):
        return value if isinstance(value, Jet) else Jet(value)

    def __add__(self, other):
        other = self.lift(other)
        return Jet(self.v + other.v, self.dp + other.dp, self.da + other.da)

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.v, -self.dp, -self.da)

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __rsub__(self, other):
        return self.lift(other) - self

    def __mul__(self, other):
        other = self.lift(other)
        return Jet(self.v * other.v,
                   self.dp * other.v + self.v * other.dp,
                   self.da * other.v + self.v * other.da)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.lift(other)
        return Jet(self.v / other.v,
                   (self.dp * other.v - self.v * other.dp) / other.v ** 2,
                   (self.da * other.v - self.v * other.da) / other.v ** 2)

    def __rtruediv__(self, other):
        return self.lift(other) / self

    def __pow__(self, n):
        if n == 0:
            return Jet(1)
        return Jet(self.v ** n, n * self.v ** (n - 1) * self.dp,
                   n * self.v ** (n - 1) * self.da)


def poly(u):
    return 17 * u ** 3 - 38 * u ** 2 + 84 * u - 24


def invariants(pv, av):
    p, a = Jet(pv, 1, 0), Jet(av, 0, 1)
    b = (1 - p * a) / (1 - p)
    m4 = p * a ** 2 + (1 - p) * b ** 2
    m6 = p * a ** 3 + (1 - p) * b ** 3
    m8 = p * a ** 4 + (1 - p) * b ** 4
    u = 3 - m4
    k6 = m6 - 15 * m4 + 30
    h8 = m8 - 28 * m6 + 210 * m4 - 315
    return u, k6, h8 / u ** 2


def decimal_box(interval, digits=12):
    scale = 10 ** digits

    def floor_scaled(x):
        return (x.numerator * scale) // x.denominator

    low_i = floor_scaled(interval.lo)
    high_floor = floor_scaled(interval.hi)
    high_i = high_floor if Q(high_floor, scale) == interval.hi else high_floor + 1

    def render(n):
        sign = "-" if n < 0 else ""
        n = abs(n)
        whole, frac = divmod(n, scale)
        return f"{sign}{whole}.{frac:0{digits}d}"

    return [render(low_i), render(high_i)]


def qbox(pair):
    return I(Q(pair[0]), Q(pair[1]))


def build_exact_certificate():
    # Decimal endpoints are rational; signs isolate the unique root because
    # p'(u)=51u^2-76u+84 has negative discriminant and is everywhere positive.
    u = I(Q("0.327013679166041"), Q("0.327013679166043"))
    assert poly(u.lo) < 0 < poly(u.hi)
    derivative_discriminant = Q(76) ** 2 - 4 * 51 * 84
    assert derivative_discriminant < 0

    S = 2 * (6 - 7 * u) / (2 - u)
    R = S - (3 - u)
    disc = S ** 2 - 4 * R
    root_disc = disc.sqrt()
    a0 = (S - root_disc) / 2
    b0 = (S + root_disc) / 2
    p0 = (b0 - 1) / (b0 - a0)
    uu, k6, x = invariants(p0, a0)
    jac = k6.dp * x.da - k6.da * x.dp
    c = Q(35, 3) * u * u.sqrt()
    P = c * x.da / jac
    A = -c * x.dp / jac

    # Derive the K1728 fixed-raw-radii tangent internally instead of trusting
    # its printed beta: Pk=beta, Ak=beta*a0*(b0-a0), with beta fixed by kappa6.
    direction_a = a0 * (b0 - a0)
    beta = c / (k6.dp + k6.da * direction_a)
    xi_k1728 = x.dp * beta + x.da * beta * direction_a
    q5_excess = xi_k1728 ** 2 / 5040

    # A rational finite-strength section: s=1/32, q=s^2=1/1024.
    q = Q(1, 1024)
    p_star = p0 + P / 32
    a_star = a0 + A / 32
    u_star, _, _ = invariants(p_star, a_star)
    # At fixed p, u=q has the unique lower chart intercept
    # a_sing=1-sqrt((2-q)(1-p)/p).  This is a concrete boundary
    # discriminator, not a claim about global Euclidean distance.
    a_sing = 1 - (((2 - q) * (1 - p_star) / p_star).sqrt())
    singular_gap = a_star - a_sing
    face_gaps = {
        "p=0": p_star,
        "p=1": 1 - p_star,
        "a=0": a_star,
        "a=1": 1 - a_star,
    }
    assert singular_gap.lo > 0
    assert singular_gap.hi < min(g.lo for g in face_gaps.values())
    assert u_star.v.lo > q
    return {
        "u": decimal_box(u, 15),
        "p0": decimal_box(p0),
        "a0": decimal_box(a0),
        "b0": decimal_box(b0),
        "jacobian": decimal_box(jac, 6),
        "P": decimal_box(P),
        "A": decimal_box(A),
        "k1728_beta": decimal_box(beta),
        "k1728_xi": decimal_box(xi_k1728),
        "k1728_q5_excess": decimal_box(q5_excess, 9),
        "q": "1/1024",
        "p_star": decimal_box(p_star),
        "a_star": decimal_box(a_star),
        "u_star": decimal_box(u_star.v),
        "a_singular_at_fixed_p": decimal_box(a_sing),
        "singular_vertical_gap": decimal_box(singular_gap),
        "face_gaps": {name: decimal_box(gap) for name, gap in face_gaps.items()},
    }


def load_float_backend():
    path = ROOT / "tests/channel-swings/k1733_finite_strength_four_point_benchmark.py"
    spec = importlib.util.spec_from_file_location("k1733_backend", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate():
    data = json.loads(ARTIFACT.read_text())
    exact = build_exact_certificate()
    recorded = data["exact_rational_interval_certificate"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1744"),
        ("interval kind", data["proof_partition"]["interval_proof"] == "dependency-free rational outward intervals"),
        ("exact algebra separated", "not finite-strength" in data["proof_partition"]["exact_algebra"]),
        ("float separated", "not interval" in data["proof_partition"]["ordinary_floating_regression"]),
    ]
    for key, value in exact.items():
        checks.append((f"replay {key}", recorded[key] == value))

    # Ordinary floating regression is replayed, but never enters the proof.
    K = load_float_backend()
    q = 1 / 1024
    P = sum(map(float, exact["P"])) / 2
    A = sum(map(float, exact["A"])) / 2
    p0 = sum(map(float, exact["p0"])) / 2
    a0 = sum(map(float, exact["a0"])) / 2
    beta = sum(map(float, exact["k1728_beta"])) / 2
    b0 = sum(map(float, exact["b0"])) / 2
    selected = (p0 + P / 32, a0 + A / 32)
    fixed = (p0 + beta / 32, a0 + beta * a0 * (b0 - a0) / 32)
    js120, js180 = K.f4(selected, q, 120), K.f4(selected, q, 180)
    jk120, jk180 = K.f4(fixed, q, 120), K.f4(fixed, q, 180)
    regression = data["ordinary_floating_regression"]
    checks += [
        ("selected replay 120", abs(js120 - regression["selected_linear"]["order_120"]) < 2e-19),
        ("selected replay 180", abs(js180 - regression["selected_linear"]["order_180"]) < 2e-19),
        ("fixed replay 120", abs(jk120 - regression["k1728_linear"]["order_120"]) < 2e-19),
        ("fixed replay 180", abs(jk180 - regression["k1728_linear"]["order_180"]) < 2e-19),
        ("floating comparison", js180 < jk180),
        ("order agreement only", abs(js120 - js180) < 1e-18 and abs(jk120 - jk180) < 1e-18),
        ("missing dependency", data["finite_strength_interval_boundary"]["missing_dependency"] == "python-flint==0.9.0 (Arb), plus an implemented certified whole-line quadrature and Gaussian-tail enclosure"),
        ("no finite proof", not data["decision"]["finite_strength_fisher_ordering_interval_proved"]),
        ("boundary proved", data["decision"]["axis_frozen_singular_boundary_discriminator_proved"]),
        ("global open", not data["decision"]["global_two_radius_optimizer_proved"]),
        ("all seed open", not data["decision"]["all_seed_optimizer_proved"]),
        ("source protected", not data["decision"]["source_or_physical_status_change"]),
    ]
    for index, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    validate()
