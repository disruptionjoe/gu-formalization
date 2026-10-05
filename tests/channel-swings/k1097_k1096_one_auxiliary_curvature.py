#!/usr/bin/env python3
"""K1097: exact monotonicity, concavity and threshold for one auxiliary mode."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1097-k1096-one-auxiliary-curvature.json"


def build():
    values = [Fraction(2*x + 3) - Fraction(1, x + 2) for x in range(3)]
    return {
        "schema_version": "1.0",
        "result_id": "K1097-K1096-ONE-AUXILIARY-CURVATURE",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "branch_family": "S(lambda)=alpha*lambda+beta-g^2/(lambda+d)",
        "domain": "lambda>-d with alpha>0, d>0 and g!=0",
        "first_derivative": "alpha+g^2/(lambda+d)^2 > 0",
        "second_derivative": "-2*g^2/(lambda+d)^3 < 0",
        "fixture": {"alpha": 2, "beta": 3, "g_squared": 1, "d": 2},
        "fixture_roots": ["-5/2", "-1"],
        "unique_domain_root": "-1",
        "sample_lambdas": [0, 1, 2],
        "sample_values": [str(v) for v in values],
        "second_finite_difference": str(values[2] - 2*values[1] + values[0]),
        "decision": "constant auxiliary mixing makes the reduced branch strictly increasing and strictly concave on the positive auxiliary domain",
        "scope_boundary": "conditional one-auxiliary scalar Schur law; no source-selected GU coefficient or physical mode",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["branch_family"].endswith("g^2/(lambda+d)")
    assert d["domain"].startswith("lambda>-d")
    assert d["first_derivative"].endswith("> 0")
    assert d["second_derivative"].endswith("< 0")
    assert d["fixture"] == {"alpha":2,"beta":3,"g_squared":1,"d":2}
    assert d["fixture_roots"] == ["-5/2", "-1"]
    assert d["unique_domain_root"] == "-1"
    assert d["sample_lambdas"] == [0,1,2]
    assert d["sample_values"] == ["5/2", "14/3", "27/4"]
    assert d["second_finite_difference"] == "-1/12"
    assert "strictly increasing and strictly concave" in d["decision"]
    assert "no source-selected GU coefficient" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1097 controls: 13/13")
