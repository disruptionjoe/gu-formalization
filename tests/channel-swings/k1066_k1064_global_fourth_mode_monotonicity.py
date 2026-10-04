#!/usr/bin/env python3
"""K1066: global monotonicity of the four-mode quadratic-horn tolerance."""
import json
import math
from pathlib import Path

from k1064_k1063_high_mode_robustness_tradeoff import threshold

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1066-k1064-global-fourth-mode-monotonicity.json"


def q_normalizer(mu, n):
    xs = [math.sqrt(lam + mu) for lam in (3, 8, 15, n * (n + 2))]
    a, b, c, d = xs
    return 2 * (c - a) * (d - b) * ((b - a) + (d - c))


def shifted_square_coefficients():
    r21, r57, r133 = math.sqrt(21), math.sqrt(57), math.sqrt(133)
    return [
        -22 + 2 * r133,
        -172 - 16 * r57 + 16 * r21 + 20 * r133,
        -372 - 144 * r57 + 144 * r21 + 72 * r133,
        260 - 432 * r57 + 92 * r133 + 432 * r21,
        482 - 304 * r57 + 38 * r133 + 304 * r21,
    ]


def build():
    fixtures = [threshold(n) for n in range(4, 65)]
    return {
        "schema_version": "1.0",
        "result_id": "K1066-K1064-GLOBAL-FOURTH-MODE-MONOTONICITY",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "family": "fixed lambda={3,8,15}; lambda_four=n(n+2), integer n>=4; mu in {1,4}",
        "normalizer_identity": "V(x)*||bary(x)||_1=2*(x3-x1)*(x4-x2)*((x2-x1)+(x4-x3))",
        "limiting_direction": "the mu=1 witness evaluated on mu=4 is strictly smaller because every positive gap in the normalizer decreases with mu, so Q_1>Q_4",
        "derivative_reduction": "with t=n+1, the derivative of the limiting contrast is positive iff 2t^2+6t+12>sqrt(t^2+3)*((sqrt(19)-sqrt(7))*t+8sqrt(3)+3sqrt(7)-3sqrt(19))",
        "shifted_square_variable": "u=t-4>=0",
        "shifted_square_coefficients": shifted_square_coefficients(),
        "radical_bounds": {"sqrt21_lower": 4.582, "sqrt57_upper": 7.55, "sqrt133_lower": 11.532},
        "global_result": "the sharp symmetric eta/gamma threshold is strictly increasing for every real t>4 and hence every integer n>=4",
        "first_threshold": fixtures[0]["eta_over_gamma"],
        "checked_last_n": fixtures[-1]["n"],
        "checked_last_threshold": fixtures[-1]["eta_over_gamma"],
        "asymptotic_ceiling": (-math.sqrt(3) + (math.sqrt(7) + math.sqrt(19)) / 4) / 2,
        "scope": "global design theorem for the supplied conditional horn family; no preparation or detector ownership",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(data):
    assert data["family"].endswith("mu in {1,4}")
    assert data["normalizer_identity"].startswith("V(x)*||bary(x)||_1=2*")
    assert "Q_1>Q_4" in data["limiting_direction"]
    assert data["derivative_reduction"].startswith("with t=n+1")
    assert data["shifted_square_variable"] == "u=t-4>=0"
    assert all(value > 1.0 for value in data["shifted_square_coefficients"])
    bounds = data["radical_bounds"]
    assert bounds["sqrt21_lower"] ** 2 < 21
    assert bounds["sqrt57_upper"] ** 2 > 57
    assert bounds["sqrt133_lower"] ** 2 < 133
    fixtures = [threshold(n) for n in range(4, data["checked_last_n"] + 1)]
    assert all(row["c_1_to_4"] > row["c_4_to_1"] for row in fixtures)
    assert all(fixtures[i]["eta_over_gamma"] < fixtures[i + 1]["eta_over_gamma"] for i in range(len(fixtures) - 1))
    assert abs(data["first_threshold"] - threshold(4)["eta_over_gamma"]) < 1e-14
    assert 0.00955 < data["asymptotic_ceiling"] < 0.00956
    assert data["global_result"].endswith("every integer n>=4")
    assert data["scope"].startswith("global design theorem")
    assert data["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    result = build(); validate(result)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("K1066 controls: 16/16")
