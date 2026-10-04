#!/usr/bin/env python3
"""K1028: sharp local ceiling with a bounded compromised-trial fraction."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1028-k1027-locality-compromise-fraction-boundary.json"


def mixed_ceiling(b, q):
    return b + q * (1 - b)


def build():
    controls = [{"b": b, "q": q, "ceiling": mixed_ceiling(b, q)} for b, q in
                ((0.75, 0.0), (0.75, 0.1), (0.8, 0.25), (0.75, 1.0))]
    return {
        "schema_version": "1.0",
        "result_id": "K1028-K1027-LOCALITY-COMPROMISE-FRACTION-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "good_trial_ceiling": "E[W_i|past,good]<=b_i",
        "compromised_trial_ceiling": "E[W_i|past,compromised]<=1",
        "fraction_bound": "predictable compromise indicators c_i are fixed before W_i and sum_i c_i<=qn",
        "aggregate_ceiling": "b+q(1-b)",
        "sharpness": "mix a strategy saturating b on good trials with perfect wins on every compromised trial",
        "finite_count_form": "[(n-C)b+C]/n=b+(C/n)(1-b)",
        "controls": controls,
        "scope": "a supplied audit bound on causally uncertified or communication-capable trials; no physical locality audit is constructed",
        "ownership": {"compromise_fraction_audited": False, "communication_model_gu_owned": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["good_trial_ceiling"].endswith("<=b_i")
    assert d["compromised_trial_ceiling"].endswith("<=1")
    assert "fixed before W_i" in d["fraction_bound"] and "sum_i c_i<=qn" in d["fraction_bound"]
    assert d["aggregate_ceiling"] == "b+q(1-b)"
    assert "perfect wins" in d["sharpness"]
    assert d["finite_count_form"] == "[(n-C)b+C]/n=b+(C/n)(1-b)"
    expected = (0.75, 0.775, 0.85, 1.0)
    for row, value in zip(d["controls"], expected):
        assert math.isclose(row["ceiling"], value, abs_tol=1e-15)
    assert "no physical locality audit" in d["scope"]
    assert all(value is False for value in d["ownership"].values())
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1028 controls: 13/13")
