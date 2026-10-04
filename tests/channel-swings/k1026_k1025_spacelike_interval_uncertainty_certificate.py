#!/usr/bin/env python3
"""K1026: robust spacelike separation under event-coordinate uncertainty."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1026-k1025-spacelike-interval-uncertainty-certificate.json"


def robust_margin(distance, radius_a, radius_b, delta_t, tau_a, tau_b, c=1.0):
    spatial_floor = max(0.0, distance - radius_a - radius_b)
    temporal_ceiling = abs(delta_t) + tau_a + tau_b
    return spatial_floor - c * temporal_ceiling


def build():
    cases = [
        {"name": "robust_spacelike", "distance": 10.0, "radius_a": 0.1, "radius_b": 0.1,
         "delta_t": 2.0, "tau_a": 0.05, "tau_b": 0.05},
        {"name": "boundary", "distance": 2.0, "radius_a": 0.125, "radius_b": 0.125,
         "delta_t": 1.5, "tau_a": 0.125, "tau_b": 0.125},
        {"name": "not_certified", "distance": 2.0, "radius_a": 0.1, "radius_b": 0.1,
         "delta_t": 2.0, "tau_a": 0.05, "tau_b": 0.05},
    ]
    for row in cases:
        row["margin"] = robust_margin(**{k: row[k] for k in
            ("distance", "radius_a", "radius_b", "delta_t", "tau_a", "tau_b")})
        row["certified"] = row["margin"] > 0
    return {
        "schema_version": "1.0",
        "result_id": "K1026-K1025-SPACELIKE-INTERVAL-UNCERTAINTY-CERTIFICATE",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "metric_convention": "spacelike when ||Delta x||>c|Delta t|",
        "robust_condition": "L_nom-r_A-r_B>c(|Delta t_nom|+tau_A+tau_B)",
        "margin": "m=max(0,L_nom-r_A-r_B)-c(|Delta t_nom|+tau_A+tau_B)",
        "sharpness": "aligned spatial errors attain the distance floor and aligned clock errors attain the time ceiling",
        "controls": cases,
        "audit_boundary": "positive margin certifies every event pair in the supplied uncertainty sets; nonpositive margin is inconclusive, not proof of timelike influence",
        "ownership": {"measured_coordinates_supplied": False, "clock_calibration_supplied": False,
                      "gu_spacetime_protocol_constructed": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["metric_convention"] == "spacelike when ||Delta x||>c|Delta t|"
    assert d["robust_condition"] == "L_nom-r_A-r_B>c(|Delta t_nom|+tau_A+tau_B)"
    assert "max(0,L_nom-r_A-r_B)" in d["margin"]
    assert "aligned spatial errors" in d["sharpness"] and "clock errors" in d["sharpness"]
    by_name = {row["name"]: row for row in d["controls"]}
    assert math.isclose(by_name["robust_spacelike"]["margin"], 7.7, abs_tol=1e-12)
    assert by_name["robust_spacelike"]["certified"] is True
    assert math.isclose(by_name["boundary"]["margin"], 0.0, abs_tol=1e-12)
    assert by_name["boundary"]["certified"] is False
    assert by_name["not_certified"]["margin"] < 0
    assert "inconclusive" in d["audit_boundary"]
    assert all(value is False for value in d["ownership"].values())
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1026 controls: 12/12")
