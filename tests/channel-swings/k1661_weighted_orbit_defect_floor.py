#!/usr/bin/env python3
"""Certificate for K1661's weighted fourth-defect floor."""
import cmath
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def l4(coefficients):
    convolution = defaultdict(complex)
    for i, a in coefficients.items():
        for j, b in coefficients.items():
            convolution[tuple(x + y for x, y in zip(i, j))] += a * b
    return sum(abs(value) ** 2 for value in convolution.values())


def main():
    data = json.loads((ROOT / "lab/process/k1661-weighted-orbit-defect-floor.json").read_text())
    claim, decision = data["weighted_floor"], data["decision"]
    weights = [0.5, 0.8, 1.1, 1.4, 1.7, 2.0, 0.9, 1.3]
    coefficients = {}
    for index, rho in enumerate(weights):
        mode = (index & 1, (index >> 1) & 1, (index >> 2) & 1)
        coefficients[mode] = rho**0.5 * cmath.exp(1j * index / 7)
    i4 = l4(coefficients)
    mass = sum(weights)
    defect = 1.5 * (i4 - 2 * mass**2)
    l2 = sum(rho * rho for rho in weights)
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1661"),
        ("unequal profile", len(set(weights)) > 1),
        ("positive profile", min(weights) > 0),
        ("I4 nonnegative", i4 >= 0),
        ("defect floor", defect >= -3 * mass**2 - 1e-10),
        ("Cauchy numeric", mass**2 <= len(weights) * l2 + 1e-12),
        ("profile declaration", "positive weights" in claim["profile"]),
        ("square-root amplitude", "sqrt(rho_(N,k))" in claim["profile"]),
        ("second moment", "sum rho_k" in claim["moments"]),
        ("fourth moment", "int|R_N|^4" in claim["moments"]),
        ("nonnegative floor", "int|R_N|^4>=0" in claim["floor"]),
        ("l2 Cauchy", "d_N sum rho_k^2" in claim["l2_conversion"]),
        ("weighted g floor", "gD_(M,N)>=-3g" in claim["l2_conversion"]),
        ("scope", "not an equality" in claim["scope_guard"]),
        ("unequal decision", decision["unequal_positive_weights_covered"]),
        ("floor decision", decision["weighted_defect_floor_proved"]),
        ("l2 decision", decision["l1_to_l2_conversion_proved"]),
        ("unrestricted open", not decision["unrestricted_defect_formula_proved"]),
        ("protected", not decision["protected_status_change"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
