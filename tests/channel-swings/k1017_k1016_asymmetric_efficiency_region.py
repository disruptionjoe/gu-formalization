#!/usr/bin/env python3
"""K1017: asymmetric detector-efficiency region for fixed no-click assignment."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1017-k1016-asymmetric-efficiency-region.json"


def factor(a, b):
    return math.sqrt(2) * a * b + (1-a) * (1-b)


def build():
    sym = 2 / (1 + math.sqrt(2))
    return {
        "schema_version": "1.0", "result_id": "K1017-K1016-ASYMMETRIC-EFFICIENCY-REGION",
        "status": "working_draft_verified", "created": "2026-10-04",
        "model": "K1016 with independent setting-independent local efficiencies eta_A and eta_B",
        "correlator_map": "E'_xy=eta_A eta_B E_xy+(1-eta_A)(1-eta_B)",
        "observed_chsh": "S=2[sqrt(2) eta_A eta_B+(1-eta_A)(1-eta_B)]",
        "violation_iff": "sqrt(2) eta_A eta_B+(1-eta_A)(1-eta_B)>1",
        "symmetric_reduction": "eta>2/(1+sqrt(2))", "symmetric_threshold": sym,
        "controls": {"perfect_alice_bob_threshold": 1/math.sqrt(2), "symmetric_boundary_factor": factor(sym, sym), "perfect": factor(1,1)},
        "claim_ceiling": "exact unequal-efficiency surface for the fixed K1016 model, not a detector theorem for arbitrary states or inequalities",
        "ownership": {"loss_independence_derived_from_gu": False, "apparatus_calibrated": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "independent setting-independent" in d["model"]
    assert d["correlator_map"].startswith("E'_xy=eta_A eta_B")
    assert d["observed_chsh"].startswith("S=2[")
    assert d["violation_iff"].endswith(">1")
    assert d["symmetric_reduction"] == "eta>2/(1+sqrt(2))"
    assert abs(d["symmetric_threshold"] - 0.8284271247461901) < 1e-15
    assert abs(d["controls"]["perfect_alice_bob_threshold"] - 1/math.sqrt(2)) < 1e-15
    assert abs(d["controls"]["symmetric_boundary_factor"] - 1) < 1e-14
    assert abs(d["controls"]["perfect"] - math.sqrt(2)) < 1e-14
    assert "not a detector theorem" in d["claim_ceiling"]
    assert d["ownership"]["loss_independence_derived_from_gu"] is False
    assert d["ownership"]["apparatus_calibrated"] is False
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    payload=build(); validate(payload); OUTPUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
    print("K1017 controls: 13/13")
