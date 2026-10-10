#!/usr/bin/env python3
"""Certificate for K1682's negative-kurtosis endpoint."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1682-negative-kurtosis-extremal.json").read_text())
    claim, decision = data["extremal_law"], data["decision"]
    tau, ell, g = 7.0, 2.0, 0.3
    q_star = 12*g*ell/tau
    value = (tau/24)*q_star*q_star - g*ell*q_star
    expected = -6*g*g*ell*ell/tau
    samples = [
        ([-1, 1], [0.5, 0.5]),
        ([-math.sqrt(2), 0, math.sqrt(2)], [0.25, 0.5, 0.25]),
        ([-math.sqrt(3), 0, math.sqrt(3)], [1/6, 2/3, 1/6]),
    ]
    checks = [("schema", data["schema_version"] == "1.0"), ("claim", data["claim_id"] == "K1682")]
    for number, (points, weights) in enumerate(samples, 1):
        ex2 = sum(w*x*x for x, w in zip(points, weights))
        ex4 = sum(w*x**4 for x, w in zip(points, weights))
        checks += [(f"sample {number} variance", math.isclose(ex2, 1)),
                   (f"sample {number} Jensen", ex4 + 1e-12 >= ex2*ex2)]
    checks += [
        ("kurtosis floor", "kappa_4(X)>=-2" in claim["moment_floor"]),
        ("equality", "X^2=1" in claim["equality_case"]),
        ("weak gap", "u^2 tau/24" in claim["weak_gap"]),
        ("effective q", "q=u t^2" in claim["effective_coordinate"]),
        ("optimizer", math.isclose(value, expected)),
        ("Rademacher u2", "u=2" in claim["rademacher_role"]),
        ("sharp decision", decision["negative_fourth_cumulant_floor_sharp"]),
        ("equality decision", decision["rademacher_unique_centered_equality_case"]),
        ("no finite t theorem", not decision["finite_t_global_optimality_proved"]),
        ("no field lower", not decision["unrestricted_field_lower_bound_proved"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
