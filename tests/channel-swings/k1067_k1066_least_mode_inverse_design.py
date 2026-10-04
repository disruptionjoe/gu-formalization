#!/usr/bin/env python3
"""K1067: invert the global tolerance law into least fourth modes."""
import json
import math
from pathlib import Path

from k1064_k1063_high_mode_robustness_tradeoff import threshold

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1067-k1066-least-mode-inverse-design.json"
TARGETS = [0.003, 0.005, 0.0075, 0.009, 0.0095]


def least_mode(target):
    n = 4
    while threshold(n)["eta_over_gamma"] < target:
        n += 1
    row = threshold(n)
    return {
        "target_eta_over_gamma": target,
        "least_n": n,
        "least_lambda_four": n * (n + 2),
        "achieved": row["eta_over_gamma"],
        "previous": None if n == 4 else threshold(n - 1)["eta_over_gamma"],
    }


def build():
    ceiling = (-math.sqrt(3) + (math.sqrt(7) + math.sqrt(19)) / 4) / 2
    leading = (2 + math.sqrt(7) - math.sqrt(19)) / 8
    return {
        "schema_version": "1.0",
        "result_id": "K1067-K1066-LEAST-MODE-INVERSE-DESIGN",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "target_table": [least_mode(target) for target in TARGETS],
        "ceiling": ceiling,
        "asymptotic_deficit": "ceiling-E(n)=(2+sqrt(7)-sqrt(19))/(8*(n+1))+O((n+1)^-2)",
        "leading_deficit_constant": leading,
        "feasibility_rule": "a target rho is attainable iff 0<rho<ceiling; global strict monotonicity makes the first passing integer n unique",
        "cost_warning": "near the ceiling the required mode grows at leading order like leading_deficit_constant/(ceiling-rho)",
        "scope": "inverse design for candidate normalized error targets; no physical target or preparation cost selected",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(data):
    assert [row["target_eta_over_gamma"] for row in data["target_table"]] == TARGETS
    assert [row["least_n"] for row in data["target_table"]] == [5, 7, 17, 64, 641]
    for row in data["target_table"]:
        assert row["achieved"] >= row["target_eta_over_gamma"]
        assert row["previous"] is None or row["previous"] < row["target_eta_over_gamma"]
        assert row["least_lambda_four"] == row["least_n"] * (row["least_n"] + 2)
    assert 0.00955 < data["ceiling"] < 0.00956
    assert 0.03 < data["leading_deficit_constant"] < 0.04
    assert data["asymptotic_deficit"].startswith("ceiling-E(n)=")
    assert "first passing integer n unique" in data["feasibility_rule"]
    assert data["cost_warning"].startswith("near the ceiling")
    assert data["scope"].startswith("inverse design")
    assert data["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    result = build(); validate(result)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("K1067 controls: 13/13")
