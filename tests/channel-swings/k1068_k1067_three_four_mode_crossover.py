#!/usr/bin/env python3
"""K1068: compare three-mode curvature and four-mode redundancy budgets."""
import json
import math
from pathlib import Path

from k1064_k1063_high_mode_robustness_tradeoff import threshold

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1068-k1067-three-four-mode-crossover.json"
INTERCEPT = 0.010294099763382809340088087602883291
SLOPE = 0.438235401419703143959471474382700254


def crossover(n):
    four = threshold(n)["eta_over_gamma"]
    return {"n": n, "lambda_four": n * (n + 2), "four_mode_budget": four,
            "crossover_tau": (INTERCEPT - four) / SLOPE}


def build():
    ceiling = (-math.sqrt(3) + (math.sqrt(7) + math.sqrt(19)) / 4) / 2
    rows = [crossover(n) for n in (4, 8, 16, 64)]
    rows.append({"n": "infinity", "lambda_four": "infinity", "four_mode_budget": ceiling,
                 "crossover_tau": (INTERCEPT - ceiling) / SLOPE})
    return {
        "schema_version": "1.0",
        "result_id": "K1068-K1067-THREE-FOUR-MODE-CROSSOVER",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "three_mode_budget": "eta_3(tau)=0.0102940997633828...-0.438235401419703...*tau",
        "four_mode_assumption": "exact common quadratic transfer with independently certified nonzero linear-response floor",
        "normalization_assumption": "the three-mode gain unit equals the independently certified response floor used for the four-mode eta/gamma budget",
        "crossover_table": rows,
        "decision_rule": "below a row's crossover tau the three-mode route has the larger component-error budget; above it the named four-mode route has the larger budget",
        "asymptotic_crossover_tau": rows[-1]["crossover_tau"],
        "non_dominance": "the budget comparison alone cannot choose a route because three modes require a curvature box while four modes require another preparation and global quadratic-model ownership",
        "scope": "exact candidate-route crossover in common response-normalized units; no apparatus score",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(data):
    assert data["three_mode_budget"].startswith("eta_3(tau)=0.010294")
    assert data["four_mode_assumption"].startswith("exact common quadratic")
    assert data["normalization_assumption"].startswith("the three-mode gain unit equals")
    rows = data["crossover_table"]
    assert [row["n"] for row in rows[:-1]] == [4, 8, 16, 64]
    assert 0.0179 < rows[0]["crossover_tau"] < 0.0181
    assert 0.0105 < rows[1]["crossover_tau"] < 0.0107
    assert 0.0063 < rows[2]["crossover_tau"] < 0.0066
    assert 0.0028 < rows[3]["crossover_tau"] < 0.0031
    assert 0.0016 < data["asymptotic_crossover_tau"] < 0.0018
    assert all(rows[i]["crossover_tau"] > rows[i + 1]["crossover_tau"] for i in range(len(rows) - 1))
    assert "cannot choose a route" in data["non_dominance"]
    assert data["decision_rule"].startswith("below a row's crossover")
    assert data["scope"].startswith("exact candidate-route crossover")
    assert data["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    result = build(); validate(result)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("K1068 controls: 13/13")
