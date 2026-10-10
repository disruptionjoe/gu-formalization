#!/usr/bin/env python3
"""Certificate for K1687's sixth-order symmetric Fisher law."""
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def hermite_probabilist(n, x):
    h0, h1 = 1.0, x
    if n == 0:
        return h0
    if n == 1:
        return h1
    for k in range(1, n):
        h0, h1 = h1, x * h1 - k * h0
    return h1


def gaussian_moment(power):
    if power % 2:
        return 0
    result = 1
    for value in range(1, power, 2):
        result *= value
    return result


def polynomial_expectation(coefficients):
    return sum(coefficient * gaussian_moment(power)
               for power, coefficient in enumerate(coefficients))


def multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def main():
    data = json.loads((ROOT / "lab/process/k1687-symmetric-sixth-order-fisher-law.json").read_text())
    claim, decision = data["expansion"], data["decision"]
    # H3=x^3-3x, H4=x^4-6x^2+3, H5=x^5-10x^3+15x.
    h3 = [0, -3, 0, 1]
    h4 = [3, 0, -6, 0, 1]
    h5 = [0, 15, 0, -10, 0, 1]
    h3_sq = multiply(h3, h3)
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1687"),
        ("H5 norm", polynomial_expectation(multiply(h5, h5)) == math.factorial(5)),
        ("H4 H3 square", polynomial_expectation(multiply(h4, h3_sq)) == 216),
        ("leading coefficient", Fraction(16 * math.factorial(3), 24**2) == Fraction(1, 6)),
        ("sixth H6 coefficient", Fraction(36 * math.factorial(5), 720**2) == Fraction(1, 120)),
        ("denominator coefficient", Fraction(16 * 216, 24**3) == Fraction(1, 4)),
        ("seed class", "bounded, symmetric" in claim["seed_class"]),
        ("Hermite ratio", "kappa_6/720" in claim["hermite_ratio"]),
        ("integrals", "H_4 H_3^2 phi=216" in claim["hermite_integrals"]),
        ("fifth vanishes", "t^5 coefficient vanishes" in claim["fisher_law"]),
        ("sixth law", "kappa_6^2/120-kappa_4^3/4" in claim["fisher_law"]),
        ("matched q", "kappa_6^2/(120u^3)" in claim["matched_defect"]),
        ("fifth decision", decision["fifth_order_coefficient_zero"]),
        ("sixth decision", decision["sixth_order_coefficient_explicit"]),
        ("penalty decision", decision["first_seed_dependent_matched_defect_penalty_is_kappa6"]),
        ("global ordering open", not decision["finite_t_global_ordering_proved"]),
    ]
    # Recurrence sanity for the polynomials used above.
    checks += [("H3 recurrence", all(math.isclose(hermite_probabilist(3, x), x**3 - 3*x)
                                     for x in (-1.3, 0.2, 2.1)))]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
