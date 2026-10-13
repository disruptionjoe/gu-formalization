#!/usr/bin/env python3
"""Certified third-order compact-window parameter jets for K1801.

The coefficients are normalized bivariate Taylor coefficients in ``(t,z)``:
``c[i,j] = d_t^i d_z^j f / (i! j!)``.  Keeping the parameter polynomial
symbolic until every density operation is complete preserves the cancellations
lost by coarse entrywise interval Hessians.  Observation-coordinate integration
uses K1781's certified 352-cell order-12 Taylor rule on ``[-11,11]``.
"""
from __future__ import annotations

import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

from flint import arb, ctx, fmpq

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1801-full-fisher-third-order-compact-jet.json"
ctx.dps = 80
ctx.threads = 1

Q = F(1, 1024)
RADIUS = F(11)
CELL_HALF_WIDTH = F(1, 16)
OBSERVATION_ORDER = 12
PARAMETER_ORDER = 3


def aq(x) -> arb:
    x = F(x)
    return arb(fmpq(x.numerator, x.denominator))


def ball(lo: F, hi: F) -> arb:
    lo, hi = F(lo), F(hi)
    return arb(fmpq((lo + hi).numerator, (lo + hi).denominator),
               fmpq((hi - lo).numerator, (hi - lo).denominator)) / 2


class P:
    """Normalized bivariate Taylor jet through total degree three."""

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


def density(y: Y, t: P, z: P) -> Y:
    p, a, b, v = channel(t, z)
    ra, rb, rt, rv = a.sqrt(), b.sqrt(), t.sqrt(), v.sqrt()
    ca, cb = rt * ra / v, rt * rb / v
    wa, wb = p * (-t * a / (2 * v)).exp(), (1 - p) * (-t * b / (2 * v)).exp()
    denominator = wa * (ca * y).cosh() + wb * (cb * y).cosh()
    assert denominator.c[0].constant > 0
    numerator = wa * ra * (ca * y).sinh() + wb * rb * (cb * y).sinh()
    residual = numerator - rt * y * denominator
    gaussian = (-(y * y) / (2 * v)).exp()
    prefactor = t / (v**2 * rv * P((2 * arb.pi()).sqrt()))
    return prefactor * gaussian * residual**2 / denominator


def compact_jet(tlo: F, thi: F, zlo: F, zhi: F) -> P:
    t, z = P.var(ball(tlo, thi), 0), P.var(ball(zlo, zhi), 1)
    h = CELL_HALF_WIDTH
    cells = int(RADIUS / h)
    total = P(0)
    for index in range(-cells, cells):
        midpoint = (F(index) + F(1, 2)) * h
        local_half = h / 2
        point_y = Y([P(aq(midpoint)), P(1)] + [P(0)] * (OBSERVATION_ORDER - 2))
        point = density(point_y, t, z)
        piece = P(0)
        for degree in range(0, OBSERVATION_ORDER, 2):
            piece += point.c[degree] * aq(2 * local_half**(degree + 1) / F(degree + 1))
        interval_y = Y([P(ball(midpoint - local_half, midpoint + local_half)), P(1)]
                       + [P(0)] * (OBSERVATION_ORDER - 2))
        remainder = density(interval_y, t, z).c[OBSERVATION_ORDER - 1]
        scale = aq(2 * local_half**OBSERVATION_ORDER / F(OBSERVATION_ORDER))
        for key in piece.c:
            piece.c[key] += arb(0, (abs(remainder.c[key]) * scale).upper())
        total += piece
    return total


def enc(value: arb) -> str:
    return value.str(38, radius=True, more=True)


def compute():
    P.order = PARAMETER_ORDER
    t = F(887855469, 17179869184)
    z = F(576161143609, 10**12)
    jet = compact_jet(t, t, z, z)
    return {
        "chart": {"q": "1/1024", "t": str(t), "z": str(z)},
        "window": "[-11,11]",
        "cell_half_width": "1/16",
        "observation_taylor_order": OBSERVATION_ORDER,
        "parameter_taylor_order": PARAMETER_ORDER,
        "compact_cell_count": 352,
        "normalized_coefficients": {
            f"{i},{j}": enc(jet.c[(i, j)])
            for i in range(PARAMETER_ORDER + 1)
            for j in range(PARAMETER_ORDER + 1 - i)
        },
    }


def validate(data, got=None):
    got = compute() if got is None else got
    certificate = data["certificate"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1801"),
        ("backend", data["backend"] == "python-flint==0.9.0"),
        ("chart", certificate["chart"] == got["chart"]),
        ("window", certificate["window"] == got["window"]),
        ("orders", certificate["observation_taylor_order"] == 12
         and certificate["parameter_taylor_order"] == 3),
        ("cells", certificate["compact_cell_count"] == 352),
        ("ten coefficients", len(certificate["normalized_coefficients"]) == 10),
    ]
    for key, value in got["normalized_coefficients"].items():
        checks.append((f"coefficient {key}",
                       arb(certificate["normalized_coefficients"][key]).contains(arb(value))))
    checks += [
        ("third order certified", data["decision"]["compact_third_order_parameter_jet_certified"]),
        ("whole line separate", not data["decision"]["whole_line_third_order_parameter_jet_certified"]),
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
