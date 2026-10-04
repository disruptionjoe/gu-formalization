#!/usr/bin/env python3
"""K1011: observable-coordinate noisy Bell phase diagram."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1011-k1010-observable-noisy-bell-phase-diagram.json"


def build():
    p = Fraction(4, 5)
    lam = Fraction(2, 5)
    visibility = p * lam
    return {
        "schema_version": "1.0",
        "result_id": "K1011-K1010-OBSERVABLE-NOISY-BELL-PHASE-DIAGRAM",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "observable_domain": "0<=V<=p<=1 with V=p*lambda",
        "entanglement_region": "p+2V>1",
        "optimized_chsh_region": "p^2+V^2>1",
        "entangled_chsh_local_region": "p+2V>1 and p^2+V^2<=1",
        "separator": {
            "p": str(p),
            "lambda": str(lam),
            "V": str(visibility),
            "entanglement_lhs": str(p + 2 * visibility),
            "chsh_lhs": str(p * p + visibility * visibility),
        },
        "ownership": {
            "gu_state_or_observable_constructed": False,
            "prediction_or_confirmation": False,
        },
        "claim_ceiling": "exact coordinate transformation inside the imported common-contrast two-qubit model only",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(data):
    assert data["observable_domain"] == "0<=V<=p<=1 with V=p*lambda"
    assert data["entanglement_region"] == "p+2V>1"
    assert data["optimized_chsh_region"] == "p^2+V^2>1"
    s = data["separator"]
    assert Fraction(s["p"]) == Fraction(4, 5)
    assert Fraction(s["lambda"]) == Fraction(2, 5)
    assert Fraction(s["V"]) == Fraction(8, 25)
    assert Fraction(s["entanglement_lhs"]) == Fraction(36, 25) > 1
    assert Fraction(s["chsh_lhs"]) == Fraction(464, 625) < 1
    assert data["ownership"]["gu_state_or_observable_constructed"] is False
    assert data["ownership"]["prediction_or_confirmation"] is False
    assert data["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    payload = build()
    validate(payload)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("K1011 controls: 11/11")
