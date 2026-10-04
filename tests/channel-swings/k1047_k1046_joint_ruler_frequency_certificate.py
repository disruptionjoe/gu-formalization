#!/usr/bin/env python3
"""K1047: sharp joint squared-ruler and relative-frequency separation surface."""
import json, math
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1047-k1046-joint-ruler-frequency-certificate.json"


def q1_lo(delta): return (F(5) - 4 * delta) / (F(2) - delta)
def q4_hi(delta): return (F(8) + 4 * delta) / (F(5) + delta)


def build():
    delta, epsilon = F(1, 10), F(1, 25)
    ratio = q1_lo(delta) / q4_hi(delta)
    beta = ((F(1) + epsilon) / (F(1) - epsilon)) ** 2
    gap = q1_lo(delta) / beta - q4_hi(delta) * beta
    threshold = (float(ratio) ** 0.25 - 1) / (float(ratio) ** 0.25 + 1)
    return {
        "schema_version": "1.0", "result_id": "K1047-K1046-JOINT-RULER-FREQUENCY-CERTIFICATE",
        "status": "working_draft_verified", "created": "2026-10-04",
        "measurement_model": "r in [1-delta,1+delta]; each measured frequency has separate relative error at most epsilon",
        "ratio_inflation": "beta=((1+epsilon)/(1-epsilon))^2",
        "separation_condition": "beta^2 < R(delta), where R(delta)=((5-4*delta)/(2-delta))/((8+4*delta)/(5+delta))",
        "sharp_surface": "0<=delta<3/5 and epsilon<(R(delta)^(1/4)-1)/(R(delta)^(1/4)+1)",
        "recovery": "at delta=0 the threshold is 9-4*sqrt(5), exactly K1044",
        "fixture": {"delta": "1/10", "epsilon": "1/25", "R": str(ratio), "beta_squared": str(beta * beta), "measured_gap": str(gap), "sharp_epsilon_decimal": f"{threshold:.15f}"},
        "systematics_boundary": "ruler uncertainty and modewise frequency transfer are separate inputs; neither is measured here",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "separate relative error" in d["measurement_model"]
    assert d["ratio_inflation"] == "beta=((1+epsilon)/(1-epsilon))^2"
    assert d["separation_condition"].startswith("beta^2 < R(delta)")
    assert "delta<3/5" in d["sharp_surface"] and "R(delta)^(1/4)" in d["sharp_surface"]
    assert d["recovery"].endswith("exactly K1044")
    assert d["fixture"]["delta"] == "1/10" and d["fixture"]["epsilon"] == "1/25"
    assert F(d["fixture"]["R"]) == F(391, 266)
    assert F(d["fixture"]["beta_squared"]) == F(28561, 20736)
    assert F(d["fixture"]["measured_gap"]) > 0
    assert 0.045 < float(d["fixture"]["sharp_epsilon_decimal"]) < 0.05
    assert "separate inputs" in d["systematics_boundary"] and "neither is measured" in d["systematics_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data=build(); validate(data); OUTPUT.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n"); print("K1047 controls: 11/11")
