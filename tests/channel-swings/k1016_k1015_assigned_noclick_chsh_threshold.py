#!/usr/bin/env python3
"""K1016: fixed no-click assignment closes every event-ready CHSH trial."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1016-k1015-assigned-noclick-chsh-threshold.json"


def observed_chsh(eta: float) -> float:
    return 2 * math.sqrt(2) * eta * eta + 2 * (1 - eta) ** 2


def build():
    threshold = 2 / (1 + math.sqrt(2))
    return {
        "schema_version": "1.0",
        "result_id": "K1016-K1015-ASSIGNED-NOCLICK-CHSH-THRESHOLD",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "model": "maximally entangled CHSH optimum, zero ideal one-party marginals, independent equal efficiency eta, every no-click assigned +1",
        "correlator_map": "E'_xy=eta^2 E_xy+(1-eta)^2",
        "observed_chsh": "S_eta=2 sqrt(2) eta^2+2(1-eta)^2",
        "violation_iff": "eta>2/(1+sqrt(2))",
        "threshold": threshold,
        "controls": {"at_zero": observed_chsh(0), "at_threshold": observed_chsh(threshold), "at_one": observed_chsh(1)},
        "disposition": "fixed binary assignment retains every event-ready trial and defeats K1015-style postselection",
        "claim_ceiling": "exact threshold for this state, witness, zero-marginal independent-loss and fixed-assignment model only",
        "ownership": {"gu_detector_model_constructed": False, "loophole_free_experiment_claimed": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "zero ideal one-party marginals" in d["model"]
    assert d["correlator_map"] == "E'_xy=eta^2 E_xy+(1-eta)^2"
    assert d["observed_chsh"].startswith("S_eta=2 sqrt(2)")
    assert d["violation_iff"] == "eta>2/(1+sqrt(2))"
    assert abs(d["threshold"] - 0.8284271247461901) < 1e-15
    assert d["controls"]["at_zero"] == 2
    assert abs(d["controls"]["at_threshold"] - 2) < 1e-14
    assert abs(d["controls"]["at_one"] - 2 * math.sqrt(2)) < 1e-14
    assert "retains every" in d["disposition"]
    assert "this state" in d["claim_ceiling"]
    assert d["ownership"]["gu_detector_model_constructed"] is False
    assert d["ownership"]["loophole_free_experiment_claimed"] is False
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    payload = build(); validate(payload)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("K1016 controls: 13/13")
