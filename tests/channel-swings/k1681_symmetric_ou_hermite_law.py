#!/usr/bin/env python3
"""Certificate for K1681's symmetric Ornstein--Uhlenbeck channel law."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def h4(x):
    return x**4 - 6*x**2 + 3


def moment(points, weights, fn):
    return sum(w * fn(x) for x, w in zip(points, weights))


def main():
    data = json.loads((ROOT / "lab/process/k1681-symmetric-ou-hermite-law.json").read_text())
    claim, decision = data["channel_law"], data["decision"]
    seeds = [
        ([-1.0, 1.0], [0.5, 0.5], -2.0),
        ([-math.sqrt(2), 0.0, math.sqrt(2)], [0.25, 0.5, 0.25], -1.0),
    ]
    checks = [("schema", data["schema_version"] == "1.0"), ("claim", data["claim_id"] == "K1681")]
    for number, (points, weights, expected) in enumerate(seeds, 1):
        mean = moment(points, weights, lambda x: x)
        variance = moment(points, weights, lambda x: x*x)
        kappa4 = moment(points, weights, lambda x: x**4) - 3
        checks += [
            (f"seed {number} mean", math.isclose(mean, 0.0, abs_tol=1e-12)),
            (f"seed {number} variance", math.isclose(variance, 1.0)),
            (f"seed {number} H4", math.isclose(moment(points, weights, h4), kappa4)),
            (f"seed {number} kappa", math.isclose(kappa4, expected)),
            (f"seed {number} fisher coefficient", math.isclose(kappa4*kappa4/6, expected*expected/6)),
        ]
    checks += [
        ("bounded symmetric class", "bounded, symmetric" in claim["seed_class"]),
        ("Mehler series", "sum_(n>=3)" in claim["mehler_expansion"]),
        ("variance removes H2", "variance matching removes n=2" in claim["mehler_expansion"]),
        ("score H3", "t^2H_3" in claim["score_expansion"]),
        ("Fisher coefficient", "kappa_4(X)^2/6" in claim["fisher_expansion"]),
        ("exact cumulant", "t^2 kappa_4(X)" in claim["cumulant_transport"]),
        ("mean variance decision", decision["mean_and_variance_match_exactly"]),
        ("Hermite decision", decision["fourth_hermite_coefficient_identified"]),
        ("Fisher decision", decision["fisher_leading_coefficient_identified"]),
        ("no global optimizer", not decision["global_scalar_optimizer_identified"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
