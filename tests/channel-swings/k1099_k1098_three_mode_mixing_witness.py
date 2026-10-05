#!/usr/bin/env python3
"""K1099: exact three-mode witness and its identification boundary."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1099-k1098-three-mode-mixing-witness.json"


def build():
    samples = [Fraction(8,3), Fraction(11,2), Fraction(118,15)]
    finite_second = samples[2] - 2*samples[1] + samples[0]
    divided_second = finite_second / 2
    return {
        "schema_version": "1.0",
        "result_id": "K1099-K1098-THREE-MODE-MIXING-WITNESS",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "general_identity": "S[x0,x1,x2]=-sum_i w_i/((x0+d_i)(x1+d_i)(x2+d_i))",
        "sign_rule": "strictly negative for ordered modes in the positive domain iff at least one w_i>0",
        "fixture_modes": [0,1,2],
        "fixture_values": [str(v) for v in samples],
        "finite_second_difference": str(finite_second),
        "second_divided_difference": str(divided_second),
        "single_auxiliary_alias": {
            "weight": "7/5", "shift": 1, "alpha": "32/15", "beta": "61/15",
            "same_three_values": True,
        },
        "decision": "three exact modes detect nonzero positive auxiliary mixing within the assumed class but do not identify auxiliary multiplicity, shifts or weights",
        "zero_witness_boundary": "zero excludes positive constant mixing only after the diagonal Stieltjes class and exact samples are independently owned",
        "scope_boundary": "conditional three-mode classifier; no prepared physical modes, error model or GU-owned auxiliary sector",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["general_identity"].startswith("S[x0,x1,x2]=-")
    assert d["sign_rule"].startswith("strictly negative")
    assert d["fixture_modes"] == [0,1,2]
    assert d["fixture_values"] == ["8/3", "11/2", "118/15"]
    assert d["finite_second_difference"] == "-7/15"
    assert d["second_divided_difference"] == "-7/30"
    assert d["single_auxiliary_alias"] == {"weight":"7/5","shift":1,"alpha":"32/15","beta":"61/15","same_three_values":True}
    assert "do not identify auxiliary multiplicity" in d["decision"]
    assert "only after" in d["zero_witness_boundary"]
    assert "no prepared physical modes" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1099 controls: 11/11")
