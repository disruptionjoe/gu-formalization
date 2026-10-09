#!/usr/bin/env python3
"""Certificate for K1606's exact missing-information identity."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def normal(x, variance):
    return math.exp(-x * x / (2 * variance)) / math.sqrt(2 * math.pi * variance)


def main():
    d = json.loads((ROOT / "lab/process/k1606-gaussian-mixture-missing-information.json").read_text())
    q, z = d["missing_information"], d["decision"]
    checks = [
        ("claim", d["claim_id"] == "K1606"),
        ("posterior", "w_i=p_i f_i/f" in q["mixture"]),
        ("score", "u=sum_i w_i u_i" in q["score_identity"]),
        ("variance", "U-I_Omega" in q["score_identity"]),
        ("hellinger", "sqrt(f_i f_j)" in q["pairwise_bound"]),
        ("gaussian BC", "BC_ij" in q["gaussian_formula"]),
        ("energy", "-(U-I_Omega(nu|mu))/4" in q["energy_identity"]),
        ("scope finite", "fixed finite mixture" in q["scope_guard"]),
    ]

    # Direct scalar quadrature of U-I=M for a genuinely heterogeneous mixture.
    p, s1, s2 = 0.37, 0.55, 1.8
    lo, hi, n = -10.0, 10.0, 40000
    h = (hi - lo) / n
    fisher = missing = 0.0
    for k in range(n + 1):
        x = lo + k * h
        f1, f2 = normal(x, s1), normal(x, s2)
        f = p * f1 + (1 - p) * f2
        w1, w2 = p * f1 / f, (1 - p) * f2 / f
        u1, u2 = (1 - 1 / s1) * x, (1 - 1 / s2) * x
        u = w1 * u1 + w2 * u2
        weight = 0.5 if k in (0, n) else 1.0
        fisher += weight * f * u * u * h
        missing += weight * f * w1 * w2 * (u1 - u2) ** 2 * h
    upper = p * (s1 + 1 / s1 - 2) + (1 - p) * (s2 + 1 / s2 - 2)
    bc = math.sqrt(2 * math.sqrt(s1 * s2) / (s1 + s2))
    hcov = 2 * s1 * s2 / (s1 + s2)
    b = 1 / s2 - 1 / s1
    pair_bound = 0.5 * math.sqrt(p * (1 - p)) * bc * b * b * hcov
    checks += [
        ("quadrature identity", abs((upper - fisher) - missing) < 2e-8),
        ("missing nonnegative", missing > 0),
        ("pair bound", missing <= pair_bound + 2e-8),
        ("posterior decision", z["posterior_score_identity_proved"]),
        ("missing decision", z["exact_missing_information_identity_proved"]),
        ("BC decision", z["pairwise_bhattacharyya_bound_proved"]),
        ("closed form", z["gaussian_pair_integral_closed_form"]),
        ("not all order one", not z["all_order_one_mixtures_controlled"]),
        ("unrestricted open", not z["unrestricted_leading_coefficient_identified"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
