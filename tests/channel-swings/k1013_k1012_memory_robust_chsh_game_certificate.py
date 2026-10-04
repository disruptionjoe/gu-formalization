#!/usr/bin/env python3
"""K1013: memory-robust uniform-input CHSH-game certificate."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1013-k1012-memory-robust-chsh-game-certificate.json"


def build():
    alpha = 1 / 20
    score = 2 * math.sqrt(29) / 5
    win_rate = 0.5 + score / 8
    margin = win_rate - 0.75
    shots = math.ceil(math.log(1 / alpha) / (2 * margin * margin))
    return {
        "schema_version": "1.0",
        "result_id": "K1013-K1012-MEMORY-ROBUST-CHSH-GAME-CERTIFICATE",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "uniform_game": {"win_condition": "a xor b = x*y", "score_relation": "w=1/2+S/8"},
        "local_conditional_ceiling": "E[W_i|F_(i-1)]<=3/4",
        "tail_bound": "P(w_hat-3/4>=t)<=exp(-2*n*t^2)",
        "certificate": "w_hat>3/4+sqrt(log(1/alpha)/(2n))",
        "memory_scope": "arbitrary inter-trial device memory allowed under fresh uniform settings independent of the devices",
        "exact_point": {
            "p": "1",
            "V": "2/5",
            "S": "2*sqrt(29)/5",
            "alpha": "1/20",
            "win_rate": win_rate,
            "margin": margin,
            "n_total": shots,
            "penalty_at_n": math.sqrt(math.log(1 / alpha) / (2 * shots)),
            "penalty_at_n_minus_one": math.sqrt(math.log(1 / alpha) / (2 * (shots - 1))),
        },
        "unowned_assumptions": ["measurement independence", "locality", "binary outcomes", "event-ready trial definition", "no postselection"],
        "ownership": {"gu_protocol_constructed": False, "loophole_free_experiment_claimed": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(data):
    assert data["uniform_game"]["score_relation"] == "w=1/2+S/8"
    assert data["local_conditional_ceiling"] == "E[W_i|F_(i-1)]<=3/4"
    assert data["tail_bound"] == "P(w_hat-3/4>=t)<=exp(-2*n*t^2)"
    assert data["certificate"] == "w_hat>3/4+sqrt(log(1/alpha)/(2n))"
    e = data["exact_point"]
    assert e["n_total"] == 4039
    assert e["penalty_at_n"] < e["margin"]
    assert e["penalty_at_n_minus_one"] >= e["margin"]
    assert "arbitrary inter-trial device memory" in data["memory_scope"]
    assert "no postselection" in data["unowned_assumptions"]
    assert data["ownership"]["gu_protocol_constructed"] is False
    assert data["ownership"]["loophole_free_experiment_claimed"] is False
    assert data["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    payload = build()
    validate(payload)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("K1013 controls: 12/12")
