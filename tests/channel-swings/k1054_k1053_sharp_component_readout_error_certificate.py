#!/usr/bin/env python3
"""K1054: sharp componentwise additive-readout error for the three-mode horns."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1054-k1053-sharp-component-readout-error-certificate.json"


def build():
    a4 = 2 * math.sqrt(3) - math.sqrt(7)
    b4 = math.sqrt(19) - 2 * math.sqrt(3)
    eta = (b4 - a4) / (4 + 2 * a4 + 2 * b4)
    eta_fixture = 0.01
    mass1_upper = (1 + 2 * eta_fixture) / (1 - 2 * eta_fixture)
    mass4_lower = (b4 - 2 * eta_fixture) / (a4 + 2 * eta_fixture)
    return {
        "schema_version": "1.0",
        "result_id": "K1054-K1053-SHARP-COMPONENT-READOUT-ERROR-CERTIFICATE",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "readout_model": "y_i=g*omega_i+b+zeta_i with g>0 and |zeta_i|<=g*eta independently",
        "offset_cancellation": "the common b cancels from both adjacent differences",
        "shared_middle_extrema": {
            "mass1_upper": "(1+2*eta)/(1-2*eta)",
            "mass4_lower": "(b4-2*eta)/(a4+2*eta)",
            "a4": "2*sqrt(3)-sqrt(7)",
            "b4": "sqrt(19)-2*sqrt(3)",
        },
        "sharp_threshold": "eta<(sqrt(19)+sqrt(7)-4*sqrt(3))/(4+2*sqrt(19)-2*sqrt(7))",
        "sharp_threshold_decimal": f"{eta:.15f}",
        "touching_boundary": "at equality the exact mass-one upper and mass-four lower ratios coincide",
        "fixture": {
            "eta": "1/100",
            "mass1_upper": f"{mass1_upper:.15f}",
            "mass4_lower": f"{mass4_lower:.15f}",
        },
        "normalization_boundary": "eta is error in gain-normalized frequency units; the theorem does not calibrate g or construct a detector",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["readout_model"].startswith("y_i=g*omega_i+b+zeta_i") and "independently" in d["readout_model"]
    assert d["offset_cancellation"].startswith("the common b cancels")
    assert d["shared_middle_extrema"]["mass1_upper"] == "(1+2*eta)/(1-2*eta)"
    assert d["shared_middle_extrema"]["mass4_lower"] == "(b4-2*eta)/(a4+2*eta)"
    assert d["shared_middle_extrema"]["a4"].startswith("2*sqrt(3)")
    assert d["shared_middle_extrema"]["b4"].startswith("sqrt(19)")
    assert "sqrt(19)+sqrt(7)-4*sqrt(3)" in d["sharp_threshold"]
    assert 0.0102 < float(d["sharp_threshold_decimal"]) < 0.0104
    assert d["touching_boundary"].startswith("at equality")
    assert d["fixture"]["eta"] == "1/100"
    assert float(d["fixture"]["mass1_upper"]) < float(d["fixture"]["mass4_lower"])
    assert "does not calibrate g" in d["normalization_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1054 controls: 13/13")
