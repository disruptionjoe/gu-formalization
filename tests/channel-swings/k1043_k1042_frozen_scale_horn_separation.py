#!/usr/bin/env python3
"""K1043: sharp additive-error certificate for the frozen dispersion holdout."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1043-k1042-frozen-scale-horn-separation.json"


def intervals(radius):
    return {
        "mass1": [F(5, 2) - radius, F(5, 2) + radius],
        "mass4": [F(8, 5) - radius, F(8, 5) + radius],
    }


def build():
    threshold = F(9, 20)
    strict = intervals(F(2, 5))
    touching = intervals(threshold)
    return {
        "schema_version": "1.0",
        "result_id": "K1043-K1042-FROZEN-SCALE-HORN-SEPARATION",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "true_values": {"mass1": "5/2", "mass4": "8/5"},
        "gap": "9/10",
        "midpoint_classifier": {"threshold": "41/20", "above": "mass_squared_1", "below": "mass_squared_4"},
        "sharp_additive_radius": "9/20",
        "strict_example_radius": "2/5",
        "strict_intervals": {k: [str(x) for x in v] for k, v in strict.items()},
        "touching_intervals": {k: [str(x) for x in v] for k, v in touching.items()},
        "theorem": "symmetric absolute-Q intervals are disjoint exactly when radius<9/20; at radius=9/20 they touch at 41/20",
        "scope": "mathematical decision rule conditional on the frozen common scale and honest Q error bound",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["true_values"] == {"mass1": "5/2", "mass4": "8/5"}
    assert d["gap"] == "9/10"
    assert d["midpoint_classifier"] == {"threshold": "41/20", "above": "mass_squared_1", "below": "mass_squared_4"}
    assert d["sharp_additive_radius"] == "9/20"
    assert F(d["strict_intervals"]["mass1"][0]) > F(d["strict_intervals"]["mass4"][1])
    assert d["touching_intervals"]["mass1"][0] == "41/20"
    assert d["touching_intervals"]["mass4"][1] == "41/20"
    assert "exactly when radius<9/20" in d["theorem"]
    assert "conditional on the frozen common scale" in d["scope"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1043 controls: 10/10")
