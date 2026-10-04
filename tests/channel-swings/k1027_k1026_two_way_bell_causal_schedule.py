#!/usr/bin/env python3
"""K1027: two-way Bell setting-to-remote-outcome causal schedule."""
import json
import math
from pathlib import Path

from k1026_k1025_spacelike_interval_uncertainty_certificate import robust_margin

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1027-k1026-two-way-bell-causal-schedule.json"


def direction(name, distance, delta_t, radius_setting=0.1, radius_outcome=0.1,
              tau_setting=0.05, tau_outcome=0.05):
    margin = robust_margin(distance, radius_setting, radius_outcome, delta_t,
                           tau_setting, tau_outcome)
    return {"direction": name, "distance": distance, "delta_t": delta_t,
            "radius_setting": radius_setting, "radius_outcome": radius_outcome,
            "tau_setting": tau_setting, "tau_outcome": tau_outcome,
            "margin": margin, "certified": margin > 0}


def build():
    passing = [direction("A_setting_to_B_outcome", 10, 2),
               direction("B_setting_to_A_outcome", 10, 3)]
    one_way = [direction("A_setting_to_B_outcome", 10, 2),
               direction("B_setting_to_A_outcome", 10, 10)]
    return {
        "schema_version": "1.0",
        "result_id": "K1027-K1026-TWO-WAY-BELL-CAUSAL-SCHEDULE",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "required_relations": ["A_setting spacelike from B_outcome", "B_setting spacelike from A_outcome"],
        "passing_schedule": passing,
        "one_way_only_control": one_way,
        "decision_rule": "a trial is locality-certified only when both directional robust margins are strictly positive",
        "station_separation_warning": "nominal station separation alone does not certify the setting-to-remote-outcome event pairs",
        "record_requirement": "retain per-trial setting and outcome event intervals plus calibration provenance for both wings",
        "scope": "excludes subluminal or luminal setting-to-remote-outcome influence inside the supplied Minkowski uncertainty model only",
        "ownership": {"physical_events_recorded": False, "minkowski_regime_verified": False,
                      "gu_locality_theorem_constructed": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert len(d["required_relations"]) == 2
    assert all(row["certified"] for row in d["passing_schedule"])
    assert math.isclose(d["passing_schedule"][0]["margin"], 7.7, abs_tol=1e-12)
    assert math.isclose(d["passing_schedule"][1]["margin"], 6.7, abs_tol=1e-12)
    assert d["one_way_only_control"][0]["certified"] is True
    assert d["one_way_only_control"][1]["certified"] is False
    assert "both directional" in d["decision_rule"]
    assert "alone does not certify" in d["station_separation_warning"]
    assert "per-trial" in d["record_requirement"] and "both wings" in d["record_requirement"]
    assert "supplied Minkowski uncertainty model only" in d["scope"]
    assert all(value is False for value in d["ownership"].values())
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1027 controls: 12/12")
