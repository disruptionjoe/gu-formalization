#!/usr/bin/env python3
"""Certified compact-window value/gradient/Hessian jets for K1781.

The evaluator differentiates the positive-denominator full-Fisher density in
the exact ``(t,z)`` chart with second-order interval dual numbers.  The
Gaussian observation coordinate is integrated by the same interval Taylor
scheme as K1749.  This file certifies only the compact window ``[-11,11]``;
whole-line parameter derivatives still require K1782's tail composition.
"""
from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path

from flint import arb, ctx, fmpq

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1781-full-fisher-compact-jet.json"
ctx.dps = 80
ctx.threads = 1

Q = F(1, 1024)
RADIUS = F(11)
CELL_HALF_WIDTH = F(1, 16)
ORDER = 12


def aq(x) -> arb:
    x = F(x)
    return arb(fmpq(x.numerator, x.denominator))


def ball(lo: F, hi: F) -> arb:
    lo, hi = F(lo), F(hi)
    return arb(fmpq((lo + hi).numerator, (lo + hi).denominator),
               fmpq((hi - lo).numerator, (hi - lo).denominator)) / 2


class J:
    """A two-variable value, gradient and true Hessian Arb jet."""

    def __init__(self, v, g=(0, 0), h=((0, 0), (0, 0))):
        self.v = arb(v)
        self.g = [arb(g[0]), arb(g[1])]
        self.h = [[arb(h[0][0]), arb(h[0][1])],
                  [arb(h[1][0]), arb(h[1][1])]]

    @staticmethod
    def lift(x):
        return x if isinstance(x, J) else J(x)

    @staticmethod
    def var(v, index):
        g = [arb(0), arb(0)]
        g[index] = arb(1)
        return J(v, g)

    def __add__(self, other):
        other = self.lift(other)
        return J(self.v + other.v,
                 [self.g[i] + other.g[i] for i in range(2)],
                 [[self.h[i][j] + other.h[i][j] for j in range(2)] for i in range(2)])

    __radd__ = __add__

    def __neg__(self):
        return J(-self.v, [-x for x in self.g], [[-x for x in row] for row in self.h])

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __rsub__(self, other):
        return self.lift(other) - self

    def __mul__(self, other):
        if isinstance(other, T):
            return NotImplemented
        other = self.lift(other)
        return J(
            self.v * other.v,
            [self.g[i] * other.v + self.v * other.g[i] for i in range(2)],
            [[self.h[i][j] * other.v + self.g[i] * other.g[j]
              + self.g[j] * other.g[i] + self.v * other.h[i][j]
              for j in range(2)] for i in range(2)],
        )

    __rmul__ = __mul__

    def unary(self, v, first, second):
        return J(v, [first * x for x in self.g],
                 [[first * self.h[i][j] + second * self.g[i] * self.g[j]
                   for j in range(2)] for i in range(2)])

    def reciprocal(self):
        return self.unary(1 / self.v, -1 / self.v**2, 2 / self.v**3)

    def __truediv__(self, other):
        return self * self.lift(other).reciprocal()

    def __rtruediv__(self, other):
        return self.lift(other) / self

    def __pow__(self, n):
        if n == 0:
            return J(1)
        if n < 0:
            return (self ** (-n)).reciprocal()
        out, base = J(1), self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n //= 2
        return out

    def sqrt(self):
        root = self.v.sqrt()
        return self.unary(root, 1 / (2 * root), -1 / (4 * self.v * root))

    def exp(self):
        value = self.v.exp()
        return self.unary(value, value, value)

    def sinh(self):
        return self.unary(self.v.sinh(), self.v.cosh(), self.v.sinh())

    def cosh(self):
        return self.unary(self.v.cosh(), self.v.sinh(), self.v.cosh())


class T:
    """A truncated observation-coordinate Taylor series of parameter jets."""

    def __init__(self, coeffs):
        self.c = [J.lift(x) for x in coeffs]

    @property
    def n(self):
        return len(self.c)

    @staticmethod
    def lift(x, n):
        if isinstance(x, T):
            assert x.n == n
            return x
        return T([x] + [0] * (n - 1))

    def __add__(self, other):
        other = self.lift(other, self.n)
        return T([self.c[i] + other.c[i] for i in range(self.n)])

    __radd__ = __add__

    def __neg__(self):
        return T([-x for x in self.c])

    def __sub__(self, other):
        return self + (-self.lift(other, self.n))

    def __rsub__(self, other):
        return self.lift(other, self.n) - self

    def __mul__(self, other):
        other = self.lift(other, self.n)
        return T([sum((self.c[k] * other.c[j - k] for k in range(j + 1)), J(0))
                  for j in range(self.n)])

    __rmul__ = __mul__

    def reciprocal(self):
        out = [self.c[0].reciprocal()]
        for j in range(1, self.n):
            out.append(-sum((self.c[k] * out[j - k] for k in range(1, j + 1)), J(0))
                       / self.c[0])
        return T(out)

    def __truediv__(self, other):
        return self * self.lift(other, self.n).reciprocal()

    def __rtruediv__(self, other):
        return self.lift(other, self.n) / self

    def __pow__(self, n):
        out, base = T.lift(1, self.n), self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n //= 2
        return out

    def exp(self):
        out = [self.c[0].exp()]
        for j in range(1, self.n):
            out.append(sum((aq(k) * self.c[k] * out[j - k] for k in range(1, j + 1)), J(0)) / aq(j))
        return T(out)

    def sinh(self):
        return (self.exp() - (-self).exp()) / 2

    def cosh(self):
        return (self.exp() + (-self).exp()) / 2


def channel(t: J, z: J):
    c = 2 - aq(Q) / t**2
    p = c / (c + z**2)
    a = 1 - z
    b = 1 + c / z
    v = 1 - t
    return p, a, b, v


def density(y: T, t: J, z: J) -> T:
    p, a, b, v = channel(t, z)
    ra, rb, rt, rv = a.sqrt(), b.sqrt(), t.sqrt(), v.sqrt()
    ca, cb = rt * ra / v, rt * rb / v
    wa, wb = p * (-t * a / (2 * v)).exp(), (1 - p) * (-t * b / (2 * v)).exp()
    d = wa * (ca * y).cosh() + wb * (cb * y).cosh()
    assert d.c[0].v > 0
    n = wa * ra * (ca * y).sinh() + wb * rb * (cb * y).sinh()
    residual = n - rt * y * d
    gaussian = (-(y * y) / (2 * v)).exp()
    prefactor = t / (v**2 * rv * J((2 * arb.pi()).sqrt()))
    return prefactor * gaussian * residual**2 / d


def compact_jet(tlo: F, thi: F, zlo: F, zhi: F) -> J:
    t, z = J.var(ball(tlo, thi), 0), J.var(ball(zlo, zhi), 1)
    h = CELL_HALF_WIDTH
    cells = int(RADIUS / h)
    total = J(0)
    for index in range(-cells, cells):
        midpoint = (F(index) + F(1, 2)) * h
        local_half = h / 2
        yp = T([J(aq(midpoint)), J(1)] + [J(0)] * (ORDER - 2))
        point = density(yp, t, z)
        piece = J(0)
        for degree in range(0, ORDER, 2):
            piece += point.c[degree] * aq(2 * local_half**(degree + 1) / F(degree + 1))
        yi = T([J(ball(midpoint - local_half, midpoint + local_half)), J(1)] + [J(0)] * (ORDER - 2))
        rem = density(yi, t, z).c[ORDER - 1]
        scale = aq(2 * local_half**ORDER / F(ORDER))
        piece.v += arb(0, (abs(rem.v) * scale).upper())
        for i in range(2):
            piece.g[i] += arb(0, (abs(rem.g[i]) * scale).upper())
            for j in range(2):
                piece.h[i][j] += arb(0, (abs(rem.h[i][j]) * scale).upper())
        total += piece
    return total


def enc(x: arb) -> str:
    return x.str(38, radius=True, more=True)


def compute():
    t = F(5314315, 100000000)
    z = F(56344011, 100000000)
    jet = compact_jet(t, t, z, z)
    return {
        "chart": {"q": "1/1024", "t": str(t), "z": str(z)},
        "window": "[-11,11]",
        "cell_half_width": "1/16",
        "taylor_order": ORDER,
        "compact_cell_count": 352,
        "value": enc(jet.v),
        "gradient": {"t": enc(jet.g[0]), "z": enc(jet.g[1])},
        "hessian": {"tt": enc(jet.h[0][0]), "tz": enc(jet.h[0][1]), "zz": enc(jet.h[1][1])},
    }


def validate(data, got=None):
    got = compute() if got is None else got
    cert = data["certificate"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1781"),
        ("backend", data["backend"] == "python-flint==0.9.0"),
        ("chart", cert["chart"] == got["chart"]),
        ("window", cert["window"] == got["window"]),
        ("cells", cert["compact_cell_count"] == got["compact_cell_count"]),
    ]
    for key in ("value",):
        checks.append((key, arb(cert[key]).contains(arb(got[key]))))
    for group in ("gradient", "hessian"):
        for key, value in got[group].items():
            checks.append((f"{group}.{key}", arb(cert[group][key]).contains(arb(value))))
    checks += [
        ("compact certified", data["decision"]["compact_window_value_gradient_hessian_certified"]),
        ("whole line open", not data["decision"]["whole_line_parameter_jet_certified"]),
        ("Newton open", not data["decision"]["three_slab_interval_newton_completed"]),
    ]
    return checks


def main():
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv:
        print(json.dumps(compute(), indent=2))
        return
    data = json.loads(ARTIFACT.read_text())
    checks = validate(data)
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
