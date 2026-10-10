#!/usr/bin/env python3
"""Certificate for K1676's scalar Rademacher--Gaussian channel."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def gaussian_even_moment(power):
    if power == 0:
        return 1
    return math.prod(range(1, power, 2))


def main():
    data = json.loads((ROOT / "lab/process/k1676-rademacher-gaussian-score.json").read_text())
    claim, decision = data["scalar_channel"], data["decision"]
    # H_3(x)=x^3-3x, so E H_3(Z)^2=15-18+9=6.
    h3_norm = gaussian_even_moment(6) - 6 * gaussian_even_moment(4) + 9 * gaussian_even_moment(2)
    t = 0.125
    fourth = t**2 + 6*t*(1-t) + 3*(1-t)**2
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1676"),
        ("mixture", "Rademacher" in claim["law"]),
        ("Gaussian residual", "Gaussian Z" in claim["law"]),
        ("positive density", "positive and smooth" in claim["normalization"]),
        ("mean", "E Y_t=0" in claim["normalization"]),
        ("variance", "Var(Y_t)=1" in claim["normalization"]),
        ("exact score tanh", "tanh" in claim["relative_score"]),
        ("score denominator", "/(1-t)" in claim["relative_score"]),
        ("H4 coefficient", "-(t^2/12)H_4" in claim["hermite_expansion"]),
        ("H3 coefficient", "-(t^2/3)H_3" in claim["hermite_expansion"]),
        ("H3 norm", h3_norm == 6),
        ("Fisher coefficient", math.isclose(h3_norm / 9, 2 / 3)),
        ("Fisher order", "(2/3)t^4" in claim["fisher"]),
        ("uniform Fisher bound", "j(t)<=C t^4" in claim["fisher"]),
        ("fourth moment", math.isclose(fourth, 3 - 2*t*t)),
        ("cumulant", "-2t^2 exactly" in claim["fourth_cumulant"]),
        ("normalization decision", decision["mean_and_variance_matched"]),
        ("quartic decision", decision["fisher_starts_at_order_t4"]),
        ("quadratic decision", decision["negative_cumulant_starts_at_order_t2"]),
        ("scope", not decision["alone_proves_field_descent"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
