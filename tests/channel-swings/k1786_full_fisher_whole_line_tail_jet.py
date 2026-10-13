#!/usr/bin/env python3
"""Rigorous whole-line tail majorants for the K1781 full-Fisher jet.

The compact K1781 evaluator integrates on ``[-11,11]``.  This script bounds
both omitted tails for one rational slab-three parameter box.  It propagates
positive polynomial-exponential majorants through the mixture denominator,
residual, reciprocal, square, Gaussian factor, and prefactor through Hessian
order, then integrates every resulting

    x^n exp(-a x^2 + b x),  x >= 11,

by completing the square and using the exact incomplete-Gaussian recurrence.
"""
from __future__ import annotations

import importlib.util
import json
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

from flint import arb

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1786-full-fisher-whole-line-tail-jet.json"
BASE = ROOT / "tests/channel-swings/k1781_full_fisher_compact_jet.py"
SPEC = importlib.util.spec_from_file_location("k1781", BASE)
k = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(k)

CENTER_T = F(332081, 6250000) - F(260596946, 10**16)
CENTER_Z = F(880503, 1562500) + F(258758592, 10**15)
RADIUS_T = F(1, 100000000000)
RADIUS_Z = F(1, 10000000000)
TAIL_START = F(11)


def upper(x) -> arb:
    return arb(abs(arb(x)).upper())


def lower(x) -> arb:
    return arb(arb(x).lower())


def pscale(p, c):
    c = upper(c)
    return [c * x for x in p]


def padd(p, q):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else arb(0)) +
            (q[i] if i < len(q) else arb(0)) for i in range(n)]


def pmul(p, q):
    out = [arb(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def px(p):
    return [arb(0), *p]


@dataclass
class Term:
    gaussian_power: int
    linear_power: int
    polynomial: list


def tadd(*groups):
    return [term for group in groups for term in group]


def tscale(group, c):
    return [Term(t.gaussian_power, t.linear_power, pscale(t.polynomial, c)) for t in group]


def tmul(left, right):
    return [Term(a.gaussian_power + b.gaussian_power,
                 a.linear_power + b.linear_power,
                 pmul(a.polynomial, b.polynomial))
            for a in left for b in right]


def tx(group):
    return [Term(t.gaussian_power, t.linear_power, px(t.polynomial)) for t in group]


def const(c, gaussian_power=0, linear_power=0, degree=0):
    return [Term(gaussian_power, linear_power, [arb(0)] * degree + [upper(c)])]


@dataclass
class MJet:
    v: list
    g: list
    h: list

    def __add__(self, other):
        return MJet(tadd(self.v, other.v),
                    [tadd(self.g[i], other.g[i]) for i in range(2)],
                    [[tadd(self.h[i][j], other.h[i][j]) for j in range(2)] for i in range(2)])

    def __mul__(self, other):
        return MJet(
            tmul(self.v, other.v),
            [tadd(tmul(self.g[i], other.v), tmul(self.v, other.g[i])) for i in range(2)],
            [[tadd(tmul(self.h[i][j], other.v), tmul(self.g[i], other.g[j]),
                   tmul(self.g[j], other.g[i]), tmul(self.v, other.h[i][j]))
              for j in range(2)] for i in range(2)],
        )

    def times_x(self):
        return MJet(tx(self.v), [tx(x) for x in self.g], [[tx(x) for x in row] for row in self.h])


def constant_jet(x):
    return MJet(const(x.v), [const(x.g[i]) for i in range(2)],
                [[const(x.h[i][j]) for j in range(2)] for i in range(2)])


def exponential_basis(amp, exponent):
    """Majorize amp(theta)*cosh/sinh(exponent(theta)*x)."""
    a0 = upper(amp.v)
    a1 = [upper(x) for x in amp.g]
    a2 = [[upper(amp.h[i][j]) for j in range(2)] for i in range(2)]
    c1 = [upper(x) for x in exponent.g]
    c2 = [[upper(exponent.h[i][j]) for j in range(2)] for i in range(2)]
    value = [Term(0, 1, [a0])]
    gradient = [[Term(0, 1, [a1[i], a0 * c1[i]])] for i in range(2)]
    hessian = [[None, None], [None, None]]
    for i in range(2):
        for j in range(2):
            hessian[i][j] = [Term(0, 1, [
                a2[i][j],
                a1[i] * c1[j] + a1[j] * c1[i] + a0 * c2[i][j],
                a0 * c1[i] * c1[j],
            ])]
    return MJet(value, gradient, hessian)


def reciprocal_majorant(denominator, floor):
    m = lower(floor)
    assert m > 0
    value = const(1 / m)
    gradient = [tscale(denominator.g[i], 1 / m**2) for i in range(2)]
    hessian = [[tadd(tscale(denominator.h[i][j], 1 / m**2),
                       tscale(tmul(denominator.g[i], denominator.g[j]), 2 / m**3))
                for j in range(2)] for i in range(2)]
    return MJet(value, gradient, hessian)


def gaussian_majorant(a):
    a1 = [upper(x) for x in a.g]
    a2 = [[upper(a.h[i][j]) for j in range(2)] for i in range(2)]
    value = const(1, gaussian_power=1)
    gradient = [const(a1[i], gaussian_power=1, degree=2) for i in range(2)]
    hessian = [[tadd(const(a2[i][j], gaussian_power=1, degree=2),
                      const(a1[i] * a1[j], gaussian_power=1, degree=4))
                for j in range(2)] for i in range(2)]
    return MJet(value, gradient, hessian)


def gaussian_moment_tail(n, a, b, start):
    """Upper bound integral_start^infinity x^n exp(-a*x^2+b*x) dx."""
    a, b, start = lower(a), upper(b), lower(start)
    shift = b / (2 * a)
    edge = start - shift
    assert edge > 0
    e = (-a * edge**2).exp()
    moments = [arb(0)] * (n + 1)
    moments[0] = (arb.pi() / a).sqrt() * (a.sqrt() * edge).erfc() / 2
    if n >= 1:
        moments[1] = e / (2 * a)
    for degree in range(2, n + 1):
        moments[degree] = edge**(degree - 1) * e / (2 * a) + \
            arb(degree - 1) * moments[degree - 2] / (2 * a)
    total = arb(0)
    for degree in range(n + 1):
        total += arb(__import__("math").comb(n, degree)) * shift**(n - degree) * moments[degree]
    return (b**2 / (4 * a)).exp() * total


def integrate_terms(terms, gaussian_rate, linear_rate):
    total = arb(0)
    for term in terms:
        assert term.gaussian_power == 1
        b = arb(term.linear_power) * linear_rate
        for degree, coefficient in enumerate(term.polynomial):
            total += upper(coefficient) * gaussian_moment_tail(
                degree, gaussian_rate, b, k.aq(TAIL_START))
    return 2 * total


def compute():
    t = k.J.var(k.ball(CENTER_T - RADIUS_T, CENTER_T + RADIUS_T), 0)
    z = k.J.var(k.ball(CENTER_Z - RADIUS_Z, CENTER_Z + RADIUS_Z), 1)
    p, a, b, v = k.channel(t, z)
    ra, rb, rt = a.sqrt(), b.sqrt(), t.sqrt()
    ca, cb = rt * ra / v, rt * rb / v
    wa = p * (-t * a / (2 * v)).exp()
    wb = (1 - p) * (-t * b / (2 * v)).exp()
    linear_rate = max(upper(ca.v), upper(cb.v))

    denominator = exponential_basis(wa, ca) + exponential_basis(wb, cb)
    numerator = exponential_basis(wa * ra, ca) + exponential_basis(wb * rb, cb)
    residual = numerator + (constant_jet(rt) * denominator).times_x()
    residual_square = residual * residual
    denominator_floor = lower((wa + wb).v)
    reciprocal = reciprocal_majorant(denominator, denominator_floor)
    prefactor = constant_jet(t / (v**2 * v.sqrt() * k.J((2 * arb.pi()).sqrt())))
    gaussian_rate_jet = k.J(1) / (2 * v)
    gaussian = gaussian_majorant(gaussian_rate_jet)
    density = prefactor * gaussian * residual_square * reciprocal
    gaussian_rate = lower(gaussian_rate_jet.v)

    bounds = {
        "value": integrate_terms(density.v, gaussian_rate, linear_rate),
        "gradient": {"t": integrate_terms(density.g[0], gaussian_rate, linear_rate),
                     "z": integrate_terms(density.g[1], gaussian_rate, linear_rate)},
        "hessian": {"tt": integrate_terms(density.h[0][0], gaussian_rate, linear_rate),
                    "tz": integrate_terms(density.h[0][1], gaussian_rate, linear_rate),
                    "zz": integrate_terms(density.h[1][1], gaussian_rate, linear_rate)},
    }
    return {
        "parameter_box": {
            "center": {"t": str(CENTER_T), "z": str(CENTER_Z)},
            "radius": {"t": str(RADIUS_T), "z": str(RADIUS_Z)},
        },
        "tail_start": str(TAIL_START),
        "denominator_floor": k.enc(denominator_floor),
        "gaussian_rate_floor": k.enc(gaussian_rate),
        "linear_exponent_ceiling": k.enc(linear_rate),
        "absolute_two_tail_bounds": {
            "value": k.enc(bounds["value"]),
            "gradient": {key: k.enc(value) for key, value in bounds["gradient"].items()},
            "hessian": {key: k.enc(value) for key, value in bounds["hessian"].items()},
        },
        "term_counts": {
            "value": len(density.v),
            "gradient_t": len(density.g[0]),
            "gradient_z": len(density.g[1]),
            "hessian_tt": len(density.h[0][0]),
            "hessian_tz": len(density.h[0][1]),
            "hessian_zz": len(density.h[1][1]),
        },
    }


def validate(data, got=None):
    got = compute() if got is None else got
    cert = data["certificate"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1786"),
        ("box", cert["parameter_box"] == got["parameter_box"]),
        ("tail start", cert["tail_start"] == got["tail_start"]),
        ("denominator positive", arb(cert["denominator_floor"]) > 0),
        ("gaussian rate positive", arb(cert["gaussian_rate_floor"]) > 0),
        ("term counts", cert["term_counts"] == got["term_counts"]),
    ]
    for group in ("gradient", "hessian"):
        for key, value in got["absolute_two_tail_bounds"][group].items():
            checks.append((f"{group}.{key}", arb(cert["absolute_two_tail_bounds"][group][key]).contains(arb(value))))
    checks.append(("value", arb(cert["absolute_two_tail_bounds"]["value"]).contains(
        arb(got["absolute_two_tail_bounds"]["value"]))))
    checks += [
        ("whole-line local jet", data["decision"]["whole_line_local_parameter_jet_certified"]),
        ("not full slab", not data["decision"]["whole_slab_parameter_jet_certified"]),
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
