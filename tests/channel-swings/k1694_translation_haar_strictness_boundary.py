#!/usr/bin/env python3
"""Exact fourth-cumulant mixing controls for K1694."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1694-translation-haar-strictness-boundary.json").read_text())
    theta = math.pi / 7.0
    row = [math.cos(theta), math.sin(theta)]
    square_sum = sum(v * v for v in row)
    fourth_sum = sum(v**4 for v in row)
    kappa4 = -0.7
    transformed = kappa4 * fourth_sum
    conclusion = data["conclusion"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1694"),
        ("orthogonal row", abs(square_sum - 1.0) < 1e-14),
        ("genuine mixing", 0.0 < fourth_sum < 1.0),
        ("cumulant changes", abs(transformed - kappa4) > 1e-3),
        ("manifest cumulant", "sum_j v_j^4" in data["witness"]["transformed_cumulant"]),
        ("noninvariance", data["witness"]["noninvariance"] is True),
        ("strict saving", conclusion["strict_finite_cutoff_fisher_saving"] is True),
        ("covariance", conclusion["covariance_preserved"] is True),
        ("Wick defect", conclusion["integrated_wick_defect_preserved"] is True),
        ("N4 open", conclusion["order_N4_saving_proved"] is False),
        ("Gaussian excluded", "Gaussian channels" in data["scope_guard"]),
        ("permutation excluded", "coordinate permutations" in data["scope_guard"]),
        ("correlated open", "correlated cumulant tensors" in data["scope_guard"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
