#!/usr/bin/env python3
"""K1102: exact four-mode recovery for one auxiliary pole."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1102-k1101-four-mode-one-auxiliary-identification.json"


def divided_second(x0, x1, x2, y0, y1, y2):
    return ((y2 - y1) / (x2 - x1) - (y1 - y0) / (x1 - x0)) / (x2 - x0)


def build():
    xs = [Fraction(i) for i in range(4)]
    original = [Fraction(8,3), Fraction(11,2), Fraction(118,15), Fraction(121,12)]
    alias = [Fraction(8,3), Fraction(11,2), Fraction(118,15), Fraction(607,60)]
    q0 = -divided_second(*xs[:3], *alias[:3])
    q1 = -divided_second(*xs[1:], *alias[1:])
    ratio = q0 / q1
    shift = (xs[3] - ratio * xs[0]) / (ratio - 1)
    weight = q0 * (xs[0] + shift) * (xs[1] + shift) * (xs[2] + shift)
    beta = alias[0] + weight / (xs[0] + shift)
    alpha = alias[1] + weight / (xs[1] + shift) - beta
    return {
        "schema_version": "1.0",
        "result_id": "K1102-K1101-FOUR-MODE-ONE-AUXILIARY-IDENTIFICATION",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "recovery_identity": "q0=-S[x0,x1,x2], q1=-S[x1,x2,x3], r=q0/q1=(x3+d)/(x0+d), d=(x3-r*x0)/(r-1)",
        "fixture_modes": [0, 1, 2, 3],
        "q0": str(q0), "q1": str(q1), "ratio": str(ratio),
        "recovered": {"shift": str(shift), "weight": str(weight), "alpha": str(alpha), "beta": str(beta)},
        "two_auxiliary_values": [str(v) for v in original],
        "one_auxiliary_alias_values": [str(v) for v in alias],
        "fourth_mode_residual_original_minus_alias": str(original[3] - alias[3]),
        "decision": "four distinct exact modes identify the one-auxiliary branch whenever q0 and q1 are positive, while the fourth mode rejects K1099's three-mode alias",
        "scope_boundary": "one-pole conditional inverse theorem; no physical multiplicity bound, preparation, error model or detector record",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["recovery_identity"].startswith("q0=-S")
    assert d["fixture_modes"] == [0, 1, 2, 3]
    assert (d["q0"], d["q1"], d["ratio"]) == ("7/30", "7/120", "4")
    assert d["recovered"] == {"shift":"1","weight":"7/5","alpha":"32/15","beta":"61/15"}
    assert d["two_auxiliary_values"][-1] == "121/12"
    assert d["one_auxiliary_alias_values"][-1] == "607/60"
    assert d["fourth_mode_residual_original_minus_alias"] == "-1/30"
    assert "identify the one-auxiliary branch" in d["decision"]
    assert "no physical multiplicity bound" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1102 controls: 10/10")
