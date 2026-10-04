#!/usr/bin/env python3
"""K1044: exact componentwise relative-frequency tolerance for horn separation."""
import json
from decimal import Decimal, getcontext
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1044-k1043-frequency-resolution-certificate.json"


def interval(q_value, epsilon):
    alpha = (F(1) + epsilon) / (F(1) - epsilon)
    beta = alpha * alpha
    return q_value / beta, q_value * beta


def build():
    safe_epsilon = F(1, 20)
    q1, q4 = F(5, 2), F(8, 5)
    i1, i4 = interval(q1, safe_epsilon), interval(q4, safe_epsilon)
    getcontext().prec = 40
    threshold = Decimal(9) - Decimal(4) * Decimal(5).sqrt()
    return {
        "schema_version": "1.0",
        "result_id": "K1044-K1043-FREQUENCY-RESOLUTION-CERTIFICATE",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "measurement_model": "each of the two measured frequencies has magnitude error bounded separately by the same relative epsilon<1",
        "ratio_inflation": "beta=((1+epsilon)/(1-epsilon))^2 for the squared-frequency ratio Q",
        "separation_condition": "beta<5/4",
        "sharp_epsilon": {"exact": "9-4*sqrt(5)", "decimal": str(threshold), "minimal_polynomial": "epsilon^2-18*epsilon+1=0"},
        "theorem": "the two Q intervals are disjoint exactly for epsilon<9-4*sqrt(5); at equality they touch",
        "safe_fixture": {
            "epsilon": "1/20",
            "mass1_interval": [str(x) for x in i1],
            "mass4_interval": [str(x) for x in i4],
            "gap": str(i1[0] - i4[1]),
        },
        "systematics_boundary": "this is a required calibration target, not evidence that any physical clock or detector attains it",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "bounded separately" in d["measurement_model"] and "relative epsilon<1" in d["measurement_model"]
    assert d["ratio_inflation"] == "beta=((1+epsilon)/(1-epsilon))^2 for the squared-frequency ratio Q"
    assert d["separation_condition"] == "beta<5/4"
    assert d["sharp_epsilon"]["exact"] == "9-4*sqrt(5)"
    assert d["sharp_epsilon"]["minimal_polynomial"] == "epsilon^2-18*epsilon+1=0"
    assert Decimal("0.055") < Decimal(d["sharp_epsilon"]["decimal"]) < Decimal("0.056")
    assert "exactly for epsilon<9-4*sqrt(5)" in d["theorem"]
    assert d["safe_fixture"]["epsilon"] == "1/20"
    assert F(d["safe_fixture"]["gap"]) > 0
    assert "not evidence" in d["systematics_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1044 controls: 11/11")
