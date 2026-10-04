#!/usr/bin/env python3
"""K1012: simultaneous calibration-rectangle certificates."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1012-k1011-calibration-rectangle-certificates.json"


def classify(p_lo, p_hi, v_lo, v_hi):
    return {
        "entanglement_certified": p_lo + 2 * v_lo > 1,
        "entanglement_excluded": p_hi + 2 * v_hi <= 1,
        "chsh_certified": p_lo * p_lo + v_lo * v_lo > 1,
        "chsh_excluded": p_hi * p_hi + v_hi * v_hi <= 1,
    }


def build():
    separator = classify(Fraction(79, 100), Fraction(81, 100), Fraction(31, 100), Fraction(33, 100))
    violator = classify(Fraction(99, 100), Fraction(1), Fraction(39, 100), Fraction(41, 100))
    return {
        "schema_version": "1.0",
        "result_id": "K1012-K1011-CALIBRATION-RECTANGLE-CERTIFICATES",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "simultaneous_event": "p in [pL,pU] and V in [VL,VU] with declared joint confidence",
        "rules": {
            "entanglement_certify": "pL+2VL>1",
            "entanglement_exclude": "pU+2VU<=1",
            "chsh_certify": "pL^2+VL^2>1",
            "chsh_exclude": "pU^2+VU^2<=1",
        },
        "separator_rectangle": {
            "bounds": ["79/100", "81/100", "31/100", "33/100"],
            **separator,
        },
        "violator_rectangle": {
            "bounds": ["99/100", "1", "39/100", "41/100"],
            **violator,
        },
        "nondecision": "failure of a sufficient lower or upper test is inconclusive",
        "ownership": {"gu_calibration_constructed": False, "empirical_score": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(data):
    assert data["rules"]["entanglement_certify"] == "pL+2VL>1"
    assert data["rules"]["entanglement_exclude"] == "pU+2VU<=1"
    assert data["rules"]["chsh_certify"] == "pL^2+VL^2>1"
    assert data["rules"]["chsh_exclude"] == "pU^2+VU^2<=1"
    s = data["separator_rectangle"]
    assert s["entanglement_certified"] is True
    assert s["chsh_excluded"] is True
    assert s["chsh_certified"] is False
    v = data["violator_rectangle"]
    assert v["entanglement_certified"] is True
    assert v["chsh_certified"] is True
    assert "inconclusive" in data["nondecision"]
    assert data["ownership"]["gu_calibration_constructed"] is False
    assert data["ownership"]["empirical_score"] is False
    assert data["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    payload = build()
    validate(payload)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("K1012 controls: 12/12")
