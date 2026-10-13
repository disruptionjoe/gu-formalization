#!/usr/bin/env python3
"""K1807: certified compact anchored-score Cauchy witness on slab two.

Fix the score ``h`` at K1788's rational boundary KKT anchor.  For a varying
parameter ``theta`` put ``A=E_theta[s_theta h]`` and ``B=E_theta[h^2]``.
Cauchy gives ``J(theta) >= A(theta)^2/B(theta)``.  Crucially, the varying
density denominator cancels from ``A`` and occurs only linearly in ``B``.

This program integrates normalized bivariate parameter jets on ``[-11,11]``.
It uses point coefficients through total degree five at the exact rectangle
midpoint and sixth-order coefficient enclosures over the complete exact K1804
slab-two rectangle.  A sign-independent absolute polynomial bound proves a
strict compact-window margin for ``A^2 - threshold*B``.
"""
from __future__ import annotations

import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

from flint import arb, ctx, fmpq

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1807-full-fisher-anchored-score-compact-taylor.json"
ctx.dps = 80
ctx.threads = 1

Q = F(1, 1024)
RADIUS = F(11)
CELL_HALF_WIDTH = F(1, 16)
OBSERVATION_ORDER = 12
PARAMETER_ORDER = 6
THRESHOLD = F(31835729061, 200000000000000000)
T_LO = F(56314519603, 1099511627776)
T_HI = F(887855469, 17179869184)
Z_LO = F(589, 1024)
Z_HI = F(1185, 2048)
ANCHOR_T = T_HI
ANCHOR_Z = F(576161143609, 10**12)


def aq(x) -> arb:
    x = F(x)
    return arb(fmpq(x.numerator, x.denominator))


def ball(lo: F, hi: F) -> arb:
    lo, hi = F(lo), F(hi)
    return arb(fmpq((lo + hi).numerator, (lo + hi).denominator),
               fmpq((hi - lo).numerator, (hi - lo).denominator)) / 2


class P:
    """Normalized bivariate Taylor jet through configurable total degree."""

    order = PARAMETER_ORDER

    def __init__(self, coefficients=None):
        self.c = {(i, j): arb(0)
                  for i in range(self.order + 1)
                  for j in range(self.order + 1 - i)}
        if coefficients is None:
            return
        if isinstance(coefficients, dict):
            for key, value in coefficients.items():
                if sum(key) <= self.order:
                    self.c[key] = arb(value)
        else:
            self.c[(0, 0)] = arb(coefficients)

    @staticmethod
    def lift(value):
        return value if isinstance(value, P) else P(value)

    @staticmethod
    def var(value, axis):
        key = (1, 0) if axis == 0 else (0, 1)
        return P({(0, 0): value, key: 1})

    @property
    def constant(self):
        return self.c[(0, 0)]

    def nonconstant(self):
        out = P(self.c)
        out.c[(0, 0)] = arb(0)
        return out

    def __add__(self, other):
        other = self.lift(other)
        return P({key: self.c[key] + other.c[key] for key in self.c})

    __radd__ = __add__

    def __neg__(self):
        return P({key: -value for key, value in self.c.items()})

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __rsub__(self, other):
        return self.lift(other) - self

    def __mul__(self, other):
        if isinstance(other, Y):
            return NotImplemented
        other = self.lift(other)
        out = P()
        for (i, j), left in self.c.items():
            for (k, ell), right in other.c.items():
                if i + j + k + ell <= self.order:
                    out.c[(i + k, j + ell)] += left * right
        return out

    __rmul__ = __mul__

    def __pow__(self, exponent):
        if exponent == 0:
            return P(1)
        if exponent < 0:
            return (self ** (-exponent)).reciprocal()
        out, base = P(1), self
        while exponent:
            if exponent & 1:
                out = out * base
            base = base * base
            exponent //= 2
        return out

    def reciprocal(self):
        base = self.constant
        assert not base.contains(0)
        u = self.nonconstant() * (1 / base)
        out, power = P(1), P(1)
        for degree in range(1, self.order + 1):
            power = power * u
            out += (-1 if degree % 2 else 1) * power
        return out * (1 / base)

    def __truediv__(self, other):
        if not isinstance(other, P):
            return self * (1 / arb(other))
        return self * self.lift(other).reciprocal()

    def __rtruediv__(self, other):
        return self.lift(other) / self

    def exp(self):
        base = self.constant
        u = self.nonconstant()
        out, power = P(1), P(1)
        for degree in range(1, self.order + 1):
            power = power * u
            out += power / factorial(degree)
        return base.exp() * out

    def sqrt(self):
        base = self.constant
        assert base > 0
        u = self.nonconstant() * (1 / base)
        coefficients = [F(1)]
        for degree in range(1, self.order + 1):
            coefficients.append(coefficients[-1] * (F(1, 2) - (degree - 1)) / degree)
        out, power = P(0), P(1)
        for degree, coefficient in enumerate(coefficients):
            if degree:
                power = power * u
            out += aq(coefficient) * power
        return base.sqrt() * out

    def sinh(self):
        return (self.exp() - (-self).exp()) / 2

    def cosh(self):
        return (self.exp() + (-self).exp()) / 2


class Y:
    """Observation-coordinate Taylor series with parameter-jet coefficients."""

    def __init__(self, coefficients):
        self.c = [P.lift(value) for value in coefficients]

    @property
    def n(self):
        return len(self.c)

    @staticmethod
    def lift(value, n):
        if isinstance(value, Y):
            assert value.n == n
            return value
        return Y([value] + [0] * (n - 1))

    def __add__(self, other):
        other = self.lift(other, self.n)
        return Y([self.c[index] + other.c[index] for index in range(self.n)])

    __radd__ = __add__

    def __neg__(self):
        return Y([-value for value in self.c])

    def __sub__(self, other):
        return self + (-self.lift(other, self.n))

    def __rsub__(self, other):
        return self.lift(other, self.n) - self

    def __mul__(self, other):
        other = self.lift(other, self.n)
        return Y([sum((self.c[k] * other.c[index - k]
                       for k in range(index + 1)), P(0))
                  for index in range(self.n)])

    __rmul__ = __mul__

    def reciprocal(self):
        out = [self.c[0].reciprocal()]
        for index in range(1, self.n):
            out.append(-sum((self.c[k] * out[index - k]
                             for k in range(1, index + 1)), P(0)) / self.c[0])
        return Y(out)

    def __truediv__(self, other):
        return self * self.lift(other, self.n).reciprocal()

    def __rtruediv__(self, other):
        return self.lift(other, self.n) / self

    def __pow__(self, exponent):
        out, base = self.lift(1, self.n), self
        while exponent:
            if exponent & 1:
                out = out * base
            base = base * base
            exponent //= 2
        return out

    def exp(self):
        out = [self.c[0].exp()]
        for index in range(1, self.n):
            out.append(sum((aq(k) * self.c[k] * out[index - k]
                            for k in range(1, index + 1)), P(0)) / aq(index))
        return Y(out)

    def sinh(self):
        return (self.exp() - (-self).exp()) / 2

    def cosh(self):
        return (self.exp() + (-self).exp()) / 2


def channel(t: P, z: P):
    c = 2 - aq(Q) / t**2
    p = c / (c + z**2)
    a = 1 - z
    b = 1 + c / z
    v = 1 - t
    return p, a, b, v


def mixture_parts(y: Y, t: P, z: P):
    p, a, b, v = channel(t, z)
    ra, rb, rt, rv = a.sqrt(), b.sqrt(), t.sqrt(), v.sqrt()
    ca, cb = rt * ra / v, rt * rb / v
    wa, wb = p * (-t * a / (2 * v)).exp(), (1 - p) * (-t * b / (2 * v)).exp()
    denominator = wa * (ca * y).cosh() + wb * (cb * y).cosh()
    assert denominator.c[0].constant > 0
    numerator = wa * ra * (ca * y).sinh() + wb * rb * (cb * y).sinh()
    residual = numerator - rt * y * denominator
    gaussian = (-(y * y) / (2 * v)).exp()
    return denominator, residual, gaussian, rt, rv, v


def witness_integrands(y: Y, t: P, z: P):
    """Return compact integrands for A and B with a fixed anchor score."""
    denominator, residual, gaussian, rt, rv, v = mixture_parts(y, t, z)
    t0, z0 = P(aq(ANCHOR_T)), P(aq(ANCHOR_Z))
    denominator0, residual0, _, rt0, _, v0 = mixture_parts(y, t0, z0)
    h0 = rt0 * residual0 / (v0 * denominator0)
    normal = P((2 * arb.pi()).sqrt())
    a_integrand = rt * gaussian * residual * h0 / (v * rv * normal)
    b_integrand = gaussian * denominator * h0**2 / (rv * normal)
    return a_integrand, b_integrand


def compact_jets(tlo: F, thi: F, zlo: F, zhi: F):
    t, z = P.var(ball(tlo, thi), 0), P.var(ball(zlo, zhi), 1)
    h = CELL_HALF_WIDTH
    cells = int(RADIUS / h)
    totals = [P(0), P(0)]
    for index in range(-cells, cells):
        midpoint = (F(index) + F(1, 2)) * h
        local_half = h / 2
        point_y = Y([P(aq(midpoint)), P(1)] + [P(0)] * (OBSERVATION_ORDER - 2))
        point = witness_integrands(point_y, t, z)
        pieces = [P(0), P(0)]
        for which in range(2):
            for degree in range(0, OBSERVATION_ORDER, 2):
                pieces[which] += point[which].c[degree] * aq(
                    2 * local_half**(degree + 1) / F(degree + 1))
        interval_y = Y([P(ball(midpoint - local_half, midpoint + local_half)), P(1)]
                       + [P(0)] * (OBSERVATION_ORDER - 2))
        remainders = witness_integrands(interval_y, t, z)
        scale = aq(2 * local_half**OBSERVATION_ORDER / F(OBSERVATION_ORDER))
        for which in range(2):
            remainder = remainders[which].c[OBSERVATION_ORDER - 1]
            for key in pieces[which].c:
                pieces[which].c[key] += arb(0, (abs(remainder.c[key]) * scale).upper())
            totals[which] += pieces[which]
    return tuple(totals)


def enc(value: arb) -> str:
    return value.str(38, radius=True, more=True)


def abs_upper(value: arb) -> arb:
    return arb(abs(value).upper())


def polynomial_lower(jet: P, rt: F, rz: F, max_degree: int) -> arb:
    out = arb(jet.c[(0, 0)].lower())
    for (i, j), coefficient in jet.c.items():
        if i + j == 0 or i + j > max_degree:
            continue
        out -= abs_upper(coefficient) * aq(rt**i * rz**j)
    return out


def polynomial_upper(jet: P, rt: F, rz: F, max_degree: int) -> arb:
    out = arb(jet.c[(0, 0)].upper())
    for (i, j), coefficient in jet.c.items():
        if i + j == 0 or i + j > max_degree:
            continue
        out += abs_upper(coefficient) * aq(rt**i * rz**j)
    return out


def remainder_bound(global_jet: P, rt: F, rz: F, degree: int) -> arb:
    return sum((abs_upper(coefficient) * aq(rt**i * rz**j)
                for (i, j), coefficient in global_jet.c.items()
                if i + j == degree), arb(0))


def compute():
    P.order = PARAMETER_ORDER
    center_t, center_z = (T_LO + T_HI) / 2, (Z_LO + Z_HI) / 2
    radius_t, radius_z = (T_HI - T_LO) / 2, (Z_HI - Z_LO) / 2
    point_a, point_b = compact_jets(center_t, center_t, center_z, center_z)
    global_a, global_b = compact_jets(T_LO, T_HI, Z_LO, Z_HI)
    point_l = point_a**2 - aq(THRESHOLD) * point_b
    global_l = global_a**2 - aq(THRESHOLD) * global_b
    degree = PARAMETER_ORDER
    compact_a_lower = polynomial_lower(point_a, radius_t, radius_z, degree - 1) \
        - remainder_bound(global_a, radius_t, radius_z, degree)
    compact_b_upper = polynomial_upper(point_b, radius_t, radius_z, degree - 1) \
        + remainder_bound(global_b, radius_t, radius_z, degree)
    compact_a_upper = polynomial_upper(point_a, radius_t, radius_z, degree - 1) \
        + remainder_bound(global_a, radius_t, radius_z, degree)
    margin_lower = polynomial_lower(point_l, radius_t, radius_z, degree - 1) \
        - remainder_bound(global_l, radius_t, radius_z, degree)
    return {
        "chart": {"q": "1/1024"},
        "rectangle": {"t": [str(T_LO), str(T_HI)], "z": [str(Z_LO), str(Z_HI)]},
        "center": {"t": str(center_t), "z": str(center_z)},
        "radius": {"t": str(radius_t), "z": str(radius_z)},
        "anchor": {"t": str(ANCHOR_T), "z": str(ANCHOR_Z)},
        "threshold": str(THRESHOLD),
        "window": "[-11,11]",
        "cell_half_width": "1/16",
        "observation_taylor_order": OBSERVATION_ORDER,
        "parameter_taylor_order": PARAMETER_ORDER,
        "compact_cell_count": 352,
        "compact_bounds": {
            "a_lower": enc(compact_a_lower),
            "a_upper": enc(compact_a_upper),
            "b_upper": enc(compact_b_upper),
            "cross_margin_lower": enc(margin_lower),
            "a_positive": bool(compact_a_lower > 0),
            "a_absolute_upper_lt_2e_minus_7": bool(compact_a_upper < arb("2e-7")),
            "b_upper_positive": bool(compact_b_upper > 0),
            "cross_margin_positive": bool(margin_lower > 0),
        },
        "center_normalized_coefficients": {
            "A": {f"{i},{j}": enc(point_a.c[(i, j)])
                  for i in range(PARAMETER_ORDER + 1)
                  for j in range(PARAMETER_ORDER + 1 - i)},
            "B": {f"{i},{j}": enc(point_b.c[(i, j)])
                  for i in range(PARAMETER_ORDER + 1)
                  for j in range(PARAMETER_ORDER + 1 - i)},
            "L": {f"{i},{j}": enc(point_l.c[(i, j)])
                  for i in range(PARAMETER_ORDER + 1)
                  for j in range(PARAMETER_ORDER + 1 - i)},
        },
        "degree_six_remainder_bounds": {
            "A": enc(remainder_bound(global_a, radius_t, radius_z, degree)),
            "B": enc(remainder_bound(global_b, radius_t, radius_z, degree)),
            "L": enc(remainder_bound(global_l, radius_t, radius_z, degree)),
        },
    }


def validate(data, got=None):
    got = compute() if got is None else got
    certificate = data["certificate"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1807"),
        ("backend", data["backend"] == "python-flint==0.9.0"),
        ("chart", certificate["chart"] == got["chart"]),
        ("rectangle", certificate["rectangle"] == got["rectangle"]),
        ("anchor", certificate["anchor"] == got["anchor"]),
        ("window", certificate["window"] == got["window"]),
        ("orders", certificate["observation_taylor_order"] == 12
         and certificate["parameter_taylor_order"] == 6),
        ("cells", certificate["compact_cell_count"] == 352),
        ("positive A", arb(certificate["compact_bounds"]["a_lower"]) > 0),
        ("positive margin", arb(certificate["compact_bounds"]["cross_margin_lower"]) > 0),
    ]
    for key in ("a_lower", "b_upper", "cross_margin_lower"):
        checks.append((f"compact bound {key}",
                       arb(certificate["compact_bounds"][key]).contains(
                           arb(got["compact_bounds"][key]))))
    checks.append(("A cap", certificate["compact_bounds"]["a_absolute_upper_lt_2e_minus_7"]
                   and got["compact_bounds"]["a_absolute_upper_lt_2e_minus_7"]))
    checks += [
        ("compact witness certified", data["decision"]["complete_slab_two_compact_witness_certified"]),
        ("whole line separate", not data["decision"]["complete_slab_two_whole_line_witness_certified"]),
        ("global open", not data["decision"]["global_optimizer_proved"]),
    ]
    return checks


def main():
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv:
        print(json.dumps(compute(), indent=2))
        return
    data = json.loads(ARTIFACT.read_text())
    checks = validate(data)
    for index, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
