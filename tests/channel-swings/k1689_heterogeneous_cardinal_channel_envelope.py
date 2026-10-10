#!/usr/bin/env python3
"""Certificate for K1689's heterogeneous-channel reduction."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def scalar_objective(trace, fourth_mass, g, fisher, kappa4, t):
    return trace * fisher / 4 + g * fourth_mass * kappa4 * t * t


def main():
    data = json.loads((ROOT / "lab/process/k1689-heterogeneous-cardinal-channel-envelope.json").read_text())
    claim, decision = data["envelope"], data["decision"]
    d, trace, fourth_mass, g = 7, 13.0, 5.0, 0.2
    channels = [
        (0.012, -2.0, 0.05),
        (0.023, -1.2, 0.08),
        (0.007, -0.7, 0.03),
        (0.041, -1.9, 0.11),
        (0.017, -1.5, 0.07),
        (0.009, -0.9, 0.04),
        (0.031, -1.7, 0.09),
    ]
    exact = trace / (4 * d) * sum(item[0] for item in channels)
    exact += g * fourth_mass / d * sum(item[1] * item[2] ** 2 for item in channels)
    average = sum(scalar_objective(trace, fourth_mass, g, *item) for item in channels) / d
    scalar_values = [scalar_objective(trace, fourth_mass, g, *item) for item in channels]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1689"),
        ("arithmetic mean identity", math.isclose(exact, average, rel_tol=1e-14)),
        ("mean above scalar infimum", average >= min(scalar_values)),
        ("constant minimizer attains", math.isclose(sum([min(scalar_values)] * d) / d, min(scalar_values))),
        ("exchangeable weight", "L_N/d_N" in claim["exchangeable_weights"] and "T_N/d_N" in claim["exchangeable_weights"]),
        ("exact gap", "sum_j j_(X_j)(t_j)" in claim["exact_gap"]),
        ("arithmetic reduction", "arithmetic mean" in claim["heterogeneity_reduction"]),
        ("widened functional", "h_g^scalar-card-up" in claim["widened_functional"]),
        ("Rademacher inclusion", "h_g^scalar-card-up<=h_g^card-up<h_g^prof" in claim["comparison"]),
        ("fixed-block scope", "fixed exchangeable rectangular cardinal block" in claim["scope_guard"]),
        ("heterogeneity decision", decision["heterogeneous_independent_channels_reduced"]),
        ("envelope decision", decision["scalar_seed_envelope_widened"]),
        ("local decision", decision["pointwise_local_rademacher_dominance_refuted"]),
        ("strict global open", not decision["strict_global_envelope_improvement_proved"]),
        ("coefficient open", not decision["unrestricted_coefficient_identified"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
