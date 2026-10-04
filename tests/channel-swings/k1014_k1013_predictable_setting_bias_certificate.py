#!/usr/bin/env python3
"""K1014: predictable biased-input CHSH-game certificate."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1014-k1013-predictable-setting-bias-certificate.json"


def build():
    alpha = 1 / 20
    q = 0.24
    score = 2 * math.sqrt(29) / 5
    win_rate = 0.5 + score / 8
    margin = win_rate - (1 - q)
    shots = math.ceil(math.log(1 / alpha) / (2 * margin * margin))
    return {
        "schema_version": "1.0",
        "result_id": "K1014-K1013-PREDICTABLE-SETTING-BIAS-CERTIFICATE",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "per_trial_local_ceiling": "b_i=1-min_(x,y) pi_i(x,y)",
        "variable_bias_certificate": "sum_i(W_i-b_i)>sqrt(n*log(1/alpha)/2)",
        "q_floor_certificate": "w_hat>1-q+sqrt(log(1/alpha)/(2n)) when min pi_i>=q",
        "tightness": "a deterministic local CHSH strategy can choose its single losing pair at a minimum-probability input",
        "example": {
            "q": q,
            "local_ceiling": 1 - q,
            "ideal_win_rate": win_rate,
            "margin": margin,
            "alpha": "1/20",
            "n_total": shots,
            "penalty_at_n": math.sqrt(math.log(1 / alpha) / (2 * shots)),
        },
        "unowned_assumptions": ["known predictable setting law", "settings independent of hidden device state conditional on history", "event-ready no-postselection trials"],
        "ownership": {"gu_randomness_source_constructed": False, "measurement_independence_proved": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(data):
    assert data["per_trial_local_ceiling"] == "b_i=1-min_(x,y) pi_i(x,y)"
    assert data["variable_bias_certificate"] == "sum_i(W_i-b_i)>sqrt(n*log(1/alpha)/2)"
    assert data["q_floor_certificate"] == "w_hat>1-q+sqrt(log(1/alpha)/(2n)) when min pi_i>=q"
    assert "single losing pair" in data["tightness"]
    e = data["example"]
    assert e["q"] == 0.24
    assert e["local_ceiling"] == 0.76
    assert e["n_total"] == 17475
    assert e["penalty_at_n"] < e["margin"]
    assert "settings independent of hidden device state conditional on history" in data["unowned_assumptions"]
    assert data["ownership"]["gu_randomness_source_constructed"] is False
    assert data["ownership"]["measurement_independence_proved"] is False
    assert data["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    payload = build()
    validate(payload)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("K1014 controls: 11/11")
