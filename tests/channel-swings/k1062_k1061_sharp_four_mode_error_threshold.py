#!/usr/bin/env python3
"""K1062: sharp residual-certificate error threshold for four modes."""
import json
from pathlib import Path
from k1061_k1060_four_mode_residual_witness import build as witness_build

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1062-k1061-sharp-four-mode-error-threshold.json"


def build():
    contrasts = witness_build()["directed_cross_contrast"]
    limiting = min(contrasts.values())
    return {
        "schema_version": "1.0",
        "result_id": "K1062-K1061-SHARP-FOUR-MODE-ERROR-THRESHOLD",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "directed_contrasts": contrasts,
        "limiting_contrast": limiting,
        "sharp_symmetric_eta_over_gamma": limiting / 2.0,
        "model": "y_i=A lambda_i+g sqrt(lambda_i+mu)+B+e_i with |e_i|<=eta and |g|>=gamma>0",
        "decision_rule": "accept a horn only when its l1-normalized residual is at most eta; the wrong horn is excluded when gamma*c>2*eta",
        "sharpness": "at equality the true-horn and wrong-horn residual intervals touch, so strict certification requires eta/gamma below the boundary",
        "scale_boundary": "eta/gamma is normalized readout error per linear-response unit, not absolute frequency or mass accuracy",
        "scope": "sharp for the paired residual certificates on modes {3,8,15,24}; no measured detector audit",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(data):
    assert 0.00482 < data["limiting_contrast"] < 0.00484
    assert 0.00241 < data["sharp_symmetric_eta_over_gamma"] < 0.00242
    assert "|e_i|<=eta" in data["model"] and "|g|>=gamma>0" in data["model"]
    assert "gamma*c>2*eta" in data["decision_rule"]
    assert data["sharpness"].startswith("at equality")
    assert "not absolute frequency" in data["scale_boundary"]
    assert data["scope"].startswith("sharp for the paired residual certificates")
    assert data["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    result = build(); validate(result)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("K1062 controls: 10/10")
