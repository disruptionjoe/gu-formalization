#!/usr/bin/env python3
"""K1042: freeze a two-mode dispersion holdout on one common ruler."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1042-k1041-two-mode-dispersion-holdout.json"


def q(mass_squared):
    return F(4 + mass_squared, 1 + mass_squared)


def build():
    q1, q4 = q(1), q(4)
    return {
        "schema_version": "1.0",
        "result_id": "K1042-K1041-TWO-MODE-DISPERSION-HOLDOUT",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "pre_registration": {
            "spatial_scale_squared": 1,
            "mode_eigenvalues": [1, 4],
            "observable": "Q=omega(lambda=4)^2/omega(lambda=1)^2",
            "calibration_use": "none -- K1037 used only lambda=0 fixtures",
        },
        "horns": [
            {"mass_squared": 1, "omega_squared": [2, 5], "Q": str(q1)},
            {"mass_squared": 4, "omega_squared": [5, 8], "Q": str(q4)},
        ],
        "ordering": "Q_mass1>Q_mass4",
        "gap": str(q1 - q4),
        "midpoint": str((q1 + q4) / 2),
        "heldout_status": "frozen_candidate_holdout_unscored",
        "credit_boundary": "distinguishing supplied candidates is not GU prediction or confirmation because neither coefficient nor ruler is source-selected",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    p = d["pre_registration"]
    assert p["spatial_scale_squared"] == 1 and p["mode_eigenvalues"] == [1, 4]
    assert p["observable"].startswith("Q=omega(lambda=4)^2")
    assert "K1037 used only lambda=0" in p["calibration_use"]
    assert d["horns"] == [
        {"mass_squared": 1, "omega_squared": [2, 5], "Q": "5/2"},
        {"mass_squared": 4, "omega_squared": [5, 8], "Q": "8/5"},
    ]
    assert d["ordering"] == "Q_mass1>Q_mass4"
    assert d["gap"] == "9/10" and d["midpoint"] == "41/20"
    assert d["heldout_status"] == "frozen_candidate_holdout_unscored"
    assert "not GU prediction or confirmation" in d["credit_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1042 controls: 10/10")
