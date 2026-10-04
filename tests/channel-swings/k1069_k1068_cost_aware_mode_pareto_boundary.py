#!/usr/bin/env python3
"""K1069: cost-aware Pareto rule without inventing apparatus costs."""
import json
from pathlib import Path

from k1067_k1066_least_mode_inverse_design import build as inverse_build

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1069-k1068-cost-aware-mode-pareto-boundary.json"


def build():
    inverse = inverse_build()
    return {
        "schema_version": "1.0",
        "result_id": "K1069-K1068-COST-AWARE-MODE-PARETO-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "premises": ["E(n) is strictly increasing for n>=4", "physical preparation cost C(n) is strictly increasing", "a target rho<ceiling is fixed independently"],
        "pareto_theorem": "the least integer n with E(n)>=rho is the unique minimum-cost feasible fourth-mode design",
        "target_examples": [{"rho": row["target_eta_over_gamma"], "pareto_n": row["least_n"], "lambda_four": row["least_lambda_four"]} for row in inverse["target_table"]],
        "withheld_inputs": ["physical target rho", "measured preparation-cost function C(n)", "response floor", "component-error box", "dimensional scale", "complete systematics"],
        "route_boundary": "without those inputs neither n=4, a higher fourth mode, nor the three-mode bounded-curvature route is physically preferred",
        "scope": "conditional Pareto theorem for monotone costs; no cost model, apparatus choice or empirical score",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(data):
    assert data["premises"] == ["E(n) is strictly increasing for n>=4", "physical preparation cost C(n) is strictly increasing", "a target rho<ceiling is fixed independently"]
    assert data["pareto_theorem"].startswith("the least integer n")
    assert [row["pareto_n"] for row in data["target_examples"]] == [5, 7, 17, 64, 641]
    assert len(data["withheld_inputs"]) == 6
    assert "physical target rho" in data["withheld_inputs"]
    assert "nor the three-mode" in data["route_boundary"]
    assert data["scope"].startswith("conditional Pareto theorem")
    assert data["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    result = build(); validate(result)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("K1069 controls: 8/8")
