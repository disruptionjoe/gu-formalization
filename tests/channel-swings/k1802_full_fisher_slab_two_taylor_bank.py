#!/usr/bin/env python3
"""Exact K1802 discriminator for the slab-two local enclosure route.

K1801 supplies the cancellation-preserving compact parameter jet, but a global
slab-two theorem also needs a whole-line box remainder.  This script tests the
strongest already available exact fallback at the actual K1788 KKT point: the
degree-thirteen Hermite score projection.  It proves that projection remains
strictly below the admitted upper threshold while the full Fisher value is
strictly above it, quantifying the positive complement that a successful local
Taylor/enclosure bank must certify.
"""
import json
from fractions import Fraction as F
from pathlib import Path

from flint import arb, fmpq
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1802-full-fisher-slab-two-taylor-bank.json"
K1788 = ROOT / "lab/process/k1788-full-fisher-first-two-slab-exclusion.json"

Q0 = sp.Rational(1, 1024)
T0 = sp.Rational(887855469, 17179869184)
Z0 = sp.Rational(576161143609, 10**12)
UPPER = sp.Rational(31835729061, 200000000000000000)
DEGREE = 13


def projection_value():
    c = 2 - Q0 / T0**2
    w = c / Z0 - Z0
    mu = {0: sp.Integer(1), 1: sp.Integer(0), 2: c}
    for order in range(3, 2 * DEGREE + 2):
        mu[order] = sp.cancel(w * mu[order - 1] + c * mu[order - 2])
    raw = {
        order: sp.cancel(sum(sp.binomial(order, index) * mu[index]
                             for index in range(order + 1)))
        for order in range(2 * DEGREE + 2)
    }

    def hx(order):
        return sp.cancel(sum(
            (-1)**index * sp.factorial(order)
            / (sp.factorial(index) * sp.factorial(order - 2 * index) * 2**index)
            * raw[(order - 2 * index) // 2]
            for index in range(order // 2 + 1)
        ))

    hy = {order: sp.cancel(T0**(order // 2) * hx(order))
          for order in range(0, 2 * DEGREE + 1, 2)}
    degrees = list(range(3, DEGREE + 1, 2))
    vector = sp.Matrix([hy[order + 1] for order in degrees])
    gram = sp.Matrix([[
        sp.cancel(sum(
            sp.factorial(index) * sp.binomial(left, index)
            * sp.binomial(right, index) * hy[left + right - 2 * index]
            for index in range(min(left, right) + 1)
        ))
        for right in degrees] for left in degrees])
    return sp.cancel((vector.T * (gram.inv(method="DM") * vector))[0])


def as_arb(value):
    numerator, denominator = map(int, sp.fraction(value))
    return arb(fmpq(numerator, denominator))


def compute():
    projection = projection_value()
    threshold_deficit = UPPER - projection
    k1788 = json.loads(K1788.read_text())
    full_value = arb(k1788["certificate"]["boundary_boxes"][1]["boundary_stationary_value_enclosure"])
    complement_floor = arb(full_value.lower()) - as_arb(projection)
    return {
        "point": {"t": str(T0), "z": str(Z0), "q": "1/1024"},
        "odd_projection_degree": DEGREE,
        "odd_basis_dimension": len(range(3, DEGREE + 1, 2)),
        "projection_value_decimal": str(sp.N(projection, 32)),
        "threshold_decimal": str(sp.N(UPPER, 32)),
        "threshold_minus_projection_decimal": str(sp.N(threshold_deficit, 32)),
        "projection_strictly_below_threshold": bool(threshold_deficit > 0),
        "threshold_deficit_gt_1e_minus_15": bool(threshold_deficit > sp.Rational(1, 10**15)),
        "full_fisher_minus_projection_lower_enclosure": complement_floor.str(40, radius=True, more=True),
        "full_fisher_minus_projection_gt_2_5e_minus_14": bool(complement_floor > arb("2.5e-14")),
    }


def validate(data, got=None):
    got = compute() if got is None else got
    certificate = data["certificate"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1802"),
        ("inputs", data["inputs"] == ["K1788", "K1801"]),
        ("point", certificate["point"] == got["point"]),
        ("degree", certificate["odd_projection_degree"] == 13),
        ("dimension", certificate["odd_basis_dimension"] == 6),
        ("projection below", certificate["projection_strictly_below_threshold"]
         and got["projection_strictly_below_threshold"]),
        ("deficit floor", certificate["threshold_deficit_gt_1e_minus_15"]
         and got["threshold_deficit_gt_1e_minus_15"]),
        ("complement enclosure", arb(certificate["full_fisher_minus_projection_lower_enclosure"])
         .contains(arb(got["full_fisher_minus_projection_lower_enclosure"]))),
        ("complement floor", certificate["full_fisher_minus_projection_gt_2_5e_minus_14"]
         and got["full_fisher_minus_projection_gt_2_5e_minus_14"]),
        ("projection route insufficient", data["decision"]["degree_thirteen_projection_only_closure_rejected"]),
        ("Taylor bank open", not data["decision"]["complete_whole_line_slab_two_taylor_bank_certified"]),
        ("slab open", not data["decision"]["slab_two_globally_excluded"]),
    ]
    return checks


def main():
    got = compute()
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv:
        print(json.dumps(got, indent=2))
        return
    data = json.loads(ARTIFACT.read_text())
    checks = validate(data, got)
    for index, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
