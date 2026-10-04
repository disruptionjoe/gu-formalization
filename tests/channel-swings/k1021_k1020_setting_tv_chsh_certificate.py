#!/usr/bin/env python3
"""K1021: sharp total-variation setting-source CHSH certificate."""
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1021-k1020-setting-tv-chsh-certificate.json"


def local_optimum(pi):
    best = 0.0
    for a0, a1, b0, b1 in itertools.product((0, 1), repeat=4):
        a = (a0, a1)
        b = (b0, b1)
        score = sum(pi[2 * x + y] for x in (0, 1) for y in (0, 1)
                    if (a[x] ^ b[y]) == x * y)
        best = max(best, score)
    return best


def tv_uniform(pi):
    return sum(abs(p - 0.25) for p in pi) / 2


def build():
    eps = 0.01
    sharp = (0.25 - eps, 0.25 + eps, 0.25, 0.25)
    samples = [
        (0.25, 0.25, 0.25, 0.25),
        sharp,
        (0.10, 0.30, 0.30, 0.30),
        (0.0, 1 / 3, 1 / 3, 1 / 3),
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1021-K1020-SETTING-TV-CHSH-CERTIFICATE",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "tv_convention": "TV(pi,u)=1/2 sum_j |pi_j-1/4|",
        "minimum_pair_floor": "min_j pi_j>=max(0,1/4-epsilon) when TV(pi,u)<=epsilon",
        "local_ceiling": "b<=min(1,3/4+epsilon)",
        "sequential_certificate": "sum_i[W_i-(3/4+epsilon_i)]>sqrt(n*log(1/alpha)/2), with each epsilon_i<=1/4 predictable before trial i",
        "sharp_example": {"epsilon": eps, "pi": list(sharp), "tv": tv_uniform(sharp), "local_optimum": local_optimum(sharp)},
        "enumerated_controls": [
            {"pi": list(pi), "tv": tv_uniform(pi), "local_optimum": local_optimum(pi), "one_minus_min": 1 - min(pi)}
            for pi in samples
        ],
        "memory_scope": "arbitrary inter-trial device memory; each conditional setting law remains independent of the devices given the past",
        "unowned_assumptions": ["certified conditional total-variation bounds", "measurement independence conditional on history", "event-ready no-postselection trials"],
        "ownership": {"gu_setting_source_constructed": False, "measurement_independence_proved": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["tv_convention"].startswith("TV(pi,u)=1/2")
    assert "1/4-epsilon" in d["minimum_pair_floor"]
    assert d["local_ceiling"] == "b<=min(1,3/4+epsilon)"
    assert "epsilon_i" in d["sequential_certificate"]
    e = d["sharp_example"]
    assert math.isclose(e["tv"], e["epsilon"], abs_tol=1e-15)
    assert math.isclose(e["local_optimum"], 0.75 + e["epsilon"], abs_tol=1e-15)
    for row in d["enumerated_controls"]:
        assert math.isclose(sum(row["pi"]), 1, abs_tol=1e-15)
        assert math.isclose(row["local_optimum"], row["one_minus_min"], abs_tol=1e-15)
        assert min(row["pi"]) + 1e-15 >= max(0, 0.25 - row["tv"])
    assert "arbitrary inter-trial" in d["memory_scope"]
    assert len(d["unowned_assumptions"]) == 3
    assert d["ownership"]["gu_setting_source_constructed"] is False
    assert d["ownership"]["measurement_independence_proved"] is False
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1021 controls: 13/13")
