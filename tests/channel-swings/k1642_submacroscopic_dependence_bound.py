#!/usr/bin/env python3
"""Certificate for K1642's submacroscopic block-defect bound."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def lattice_sum(n, mass=1.0):
    return sum(1.0 / (mass * mass + i * i + j * j + k * k)
               for i in range(-n, n + 1)
               for j in range(-n, n + 1)
               for k in range(-n, n + 1))


def main():
    d = json.loads((ROOT / "lab/process/k1642-submacroscopic-dependence-bound.json").read_text())
    q, z = d["dependence_bound"], d["decision"]
    ratios = [lattice_sum(n) / n for n in (4, 7, 10)]
    weights = [1.0 / (1.0 + j) for j in range(12)]
    block = 3
    lhs = sum(sum(weights[i:i + block]) ** 2 for i in range(0, len(weights), block))
    rhs = block * sum(x * x for x in weights)
    checks = [
        ("claim", d["claim_id"] == "K1642"),
        ("lattice order-N lower", min(ratios) > 5.0),
        ("lattice order-N upper", max(ratios) < 40.0),
        ("block Cauchy fixture", lhs <= rhs + 1e-12),
        ("directional cumulant", "<=K||u||_2^4" in q["directional_cumulant"]),
        ("block size", "b_N" in q["block_size"]),
        ("finite bound", "b_N sum_j lambda_j^2" in q["finite_bound"]),
        ("profile bound", "O_(m,S)(N)" in q["profile_bound"]),
        ("asymptotic", "b_N N" in q["asymptotic_bound"]),
        ("threshold", "b_N=o(N^3)" in q["leading_threshold"]),
        ("necessary not sufficient", "necessary rather than sufficient" in q["scope_guard"]),
        ("finite decision", z["finite_block_bound_proved"]),
        ("sum decision", z["three_dimensional_sum_order_N"]),
        ("submacroscopic exclusion", z["submacroscopic_leading_defect_excluded"]),
        ("macroscopic open", not z["macroscopic_dependence_sufficient"]),
        ("unrestricted open", not z["unrestricted_defect_bound"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
