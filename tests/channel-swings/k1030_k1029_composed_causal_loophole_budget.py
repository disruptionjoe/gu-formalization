#!/usr/bin/env python3
"""K1030: compose causal compromise with the K1025 Bell forecast."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1030-k1029-composed-causal-loophole-budget.json"


def build():
    p = 1.0
    v = 0.4
    eta = 0.98
    epsilon = 0.001
    q = 0.001
    record_rate = 0.001
    alpha = 0.05
    half = eta * eta * math.sqrt(p * p + v * v) + (1 - eta) ** 2
    win = 0.5 + half / 4
    b = 0.75 + epsilon
    locality_penalty = q * (1 - b)
    effective_margin = win - b - locality_penalty - record_rate
    n = math.floor(math.log(1 / alpha) / (2 * effective_margin * effective_margin)) + 1
    return {
        "schema_version": "1.0",
        "result_id": "K1030-K1029-COMPOSED-CAUSAL-LOOPHOLE-BUDGET",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "certificate": "w_hat_recorded>3/4+epsilon+q(1/4-epsilon)+R/n+sqrt(log(1/alpha)/(2n))",
        "forecast_model": "K1018 independent equal-efficiency loss plus K1021 setting-TV, K1028 locality-compromise and K1024 record budgets",
        "frozen_point": {"p": "1", "V": "2/5", "eta": "49/50", "epsilon": "1/1000",
                         "compromise_rate": "1/1000", "record_rate": "1/1000",
                         "alpha": "1/20", "expected_win_rate": win,
                         "good_local_ceiling": b, "locality_penalty": locality_penalty,
                         "effective_margin": effective_margin, "n_total": n,
                         "penalty_at_n": math.sqrt(math.log(1 / alpha) / (2 * n)),
                         "penalty_at_n_minus_one": math.sqrt(math.log(1 / alpha) / (2 * (n - 1)))},
        "feasibility_condition": "expected_win_rate>3/4+epsilon+q(1/4-epsilon)+record_rate",
        "inference_boundary": "36,043 trials is an imported-model forecast using supplied predictable pre-score causal-compromise indicators plus setting, loss and record bounds; no empirical locality audit is inferred",
        "remaining_unowned_packet": ["positive state/effect pairing", "action-owned preparation and generator",
            "physical pre-settings herald", "fresh setting source and independence proof",
            "commuting local observables", "measured two-way spacelike event records",
            "detector response calibration", "audited complete systematic-error budget"],
        "ownership": {"gu_protocol_constructed": False, "loophole_free_experiment_claimed": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "+q(1/4-epsilon)+R/n+" in d["certificate"]
    assert all(k in d["forecast_model"] for k in ("K1018", "K1021", "K1028", "K1024"))
    e = d["frozen_point"]
    assert e["n_total"] == 36043
    assert math.isclose(e["locality_penalty"], 0.000249, abs_tol=1e-15)
    assert math.isclose(e["penalty_at_n"], math.sqrt(math.log(20) / (2 * e["n_total"])), abs_tol=1e-15)
    assert math.isclose(e["penalty_at_n_minus_one"], math.sqrt(math.log(20) / (2 * (e["n_total"] - 1))), abs_tol=1e-15)
    assert e["effective_margin"] > e["penalty_at_n"]
    assert e["effective_margin"] <= e["penalty_at_n_minus_one"]
    assert e["compromise_rate"] == "1/1000" and e["record_rate"] == "1/1000"
    assert "expected_win_rate>" in d["feasibility_condition"]
    assert "predictable pre-score" in d["inference_boundary"] and "no empirical locality audit" in d["inference_boundary"]
    assert len(d["remaining_unowned_packet"]) == 8
    assert all(value is False for value in d["ownership"].values())
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1030 controls: 12/12")
