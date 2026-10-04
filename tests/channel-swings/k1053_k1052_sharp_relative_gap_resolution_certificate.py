#!/usr/bin/env python3
"""K1053: sharp relative adjacent-gap resolution for the frozen D horns."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1053-k1052-sharp-relative-gap-resolution-certificate.json"


def build():
    d4 = (math.sqrt(19) - 2 * math.sqrt(3)) / (2 * math.sqrt(3) - math.sqrt(7))
    rho = (math.sqrt(d4) - 1) / (math.sqrt(d4) + 1)
    return {
        "schema_version": "1.0",
        "result_id": "K1053-K1052-SHARP-RELATIVE-GAP-RESOLUTION-CERTIFICATE",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "error_model": "each adjacent frequency gap is measured with independent relative error at most rho<1",
        "interval_rule": "D_hat is in [D*(1-rho)/(1+rho),D*(1+rho)/(1-rho)]",
        "mass4_D": "(sqrt(19)-2*sqrt(3))/(2*sqrt(3)-sqrt(7))",
        "separation_condition": "((1+rho)/(1-rho))^2 < D4",
        "sharp_threshold": "rho<(sqrt(D4)-1)/(sqrt(D4)+1)",
        "sharp_threshold_decimal": f"{rho:.15f}",
        "touching_boundary": "at equality the upper mass-one interval equals the lower mass-four interval",
        "fixture": {
            "rho": "1/50",
            "mass1_upper": f"{(1.02 / 0.98):.15f}",
            "mass4_lower": f"{(d4 * 0.98 / 1.02):.15f}",
        },
        "systematics_boundary": "relative adjacent-gap transfer is not a measured detector specification or a complete error budget",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "adjacent frequency gap" in d["error_model"] and "rho<1" in d["error_model"]
    assert d["interval_rule"].startswith("D_hat is in") and "(1+rho)" in d["interval_rule"]
    assert d["mass4_D"].startswith("(sqrt(19)-2*sqrt(3))")
    assert d["separation_condition"] == "((1+rho)/(1-rho))^2 < D4"
    assert d["sharp_threshold"].startswith("rho<(sqrt(D4)-1)")
    assert 0.022 < float(d["sharp_threshold_decimal"]) < 0.023
    assert d["touching_boundary"].startswith("at equality")
    assert d["fixture"]["rho"] == "1/50"
    assert float(d["fixture"]["mass1_upper"]) < float(d["fixture"]["mass4_lower"])
    assert "not a measured detector" in d["systematics_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1053 controls: 11/11")
