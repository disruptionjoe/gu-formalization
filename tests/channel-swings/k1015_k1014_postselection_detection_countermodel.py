#!/usr/bin/env python3
"""K1015: local postselection/detection countermodel."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1015-k1014-postselection-detection-countermodel.json"


def retained_table():
    rows = []
    for x in (0, 1):
        for y in (0, 1):
            detected = []
            for u in (0, 1):
                for v in (0, 1):
                    da = int(x == u)
                    db = int(y == v)
                    a = 0
                    b = u * v if y == v else 0
                    if da and db:
                        detected.append({"u": u, "v": v, "a": a, "b": b, "win": (a ^ b) == x * y})
            rows.append({"x": x, "y": y, "joint_detection_probability": "1/4", "retained": detected})
    return rows


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1015-K1014-POSTSELECTION-DETECTION-COUNTERMODEL",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "hidden_variable": "lambda=(u,v) uniform on {0,1}^2",
        "local_detection": {"alice": "D_A=1 iff x=u", "bob": "D_B=1 iff y=v"},
        "local_outputs": "a=0; on Bob's detected setting y=v choose b=u*v; other local outputs arbitrary",
        "table": retained_table(),
        "single_party_detection_probability": "1/2",
        "joint_detection_probability": "1/4",
        "postselected_win_rate": "1",
        "disposition": "discarding no-click trials can turn a fully local model into an apparently perfect retained CHSH sample",
        "claim_ceiling": "explicit low-efficiency counterexample only; no optimal detector-efficiency threshold",
        "ownership": {"gu_detector_model_constructed": False, "empirical_loophole_closed": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(data):
    assert data["hidden_variable"] == "lambda=(u,v) uniform on {0,1}^2"
    assert data["local_detection"]["alice"] == "D_A=1 iff x=u"
    assert data["local_detection"]["bob"] == "D_B=1 iff y=v"
    assert len(data["table"]) == 4
    assert all(len(row["retained"]) == 1 for row in data["table"])
    assert all(row["retained"][0]["win"] is True for row in data["table"])
    assert data["single_party_detection_probability"] == "1/2"
    assert data["joint_detection_probability"] == "1/4"
    assert data["postselected_win_rate"] == "1"
    assert "fully local model" in data["disposition"]
    assert "no optimal detector-efficiency threshold" in data["claim_ceiling"]
    assert data["ownership"]["gu_detector_model_constructed"] is False
    assert data["ownership"]["empirical_loophole_closed"] is False
    assert data["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    payload = build()
    validate(payload)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("K1015 controls: 14/14")
