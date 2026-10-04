#!/usr/bin/env python3
"""K1039: current quotient/apparatus demands do not select the K77 mass horn."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1039-k1038-mass-horn-nonselection.json"


def build():
    rows = ["physical_quotient", "state_effect_pairing", "action_generator", "local_observables"]
    horns = [
        {"mass_squared": 1, "zero_mode_frequency": 1, "structural_rows": rows, "passes": True},
        {"mass_squared": 4, "zero_mode_frequency": 2, "structural_rows": rows, "passes": True},
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1039-K1038-MASS-HORN-NONSELECTION",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "horns": horns,
        "common_data": "same [0,1]xT3 domain, exact K77 quotient, positive pairing, states/effects, local copy algebra and gauge radical",
        "separating_observable": "the spatial zero-mode frequency is 1 versus 2",
        "nonselection_theorem": "K1031--K1038 structural compatibility is invariant under replacing mass squared 1 by 4, so it cannot select one candidate action",
        "heldout": {"family": "zero-mode dispersion or response measured on an independently owned preparation", "status": "proposed_unscored", "frozen_score": False},
        "ownership_boundary": "neither mass coefficient is source-selected; measuring a supplied candidate is not GU prediction credit",
        "claim_ceiling": "exact two-horn nonselection inside the K77 repository-owned candidate class only",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert [h["mass_squared"] for h in d["horns"]] == [1, 4]
    assert [h["zero_mode_frequency"] for h in d["horns"]] == [1, 2]
    assert all(h["passes"] is True for h in d["horns"])
    assert d["horns"][0]["structural_rows"] == d["horns"][1]["structural_rows"]
    assert "same [0,1]xT3" in d["common_data"]
    assert "1 versus 2" in d["separating_observable"]
    assert "cannot select" in d["nonselection_theorem"]
    assert d["heldout"] == {"family": "zero-mode dispersion or response measured on an independently owned preparation", "status": "proposed_unscored", "frozen_score": False}
    assert "neither mass coefficient is source-selected" in d["ownership_boundary"]
    assert "candidate class only" in d["claim_ceiling"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1039 controls: 12/12")
