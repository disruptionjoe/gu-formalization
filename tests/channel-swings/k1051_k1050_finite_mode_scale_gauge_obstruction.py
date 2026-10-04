#!/usr/bin/env python3
"""K1051: absolute scale is a gain gauge for every supplied dispersion mode."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1051-k1050-finite-mode-scale-gauge-obstruction.json"


def omega(lam, ruler_sq, mass_sq):
    return math.sqrt(ruler_sq * lam + mass_sq)


def build():
    modes = [0, 1, 3, 8, 15]
    ruler_sq, mass_sq, gain, offset, scale = 2.0, 5.0, 7.0 / 3.0, -0.4, 11.0
    original = [gain * omega(lam, ruler_sq, mass_sq) + offset for lam in modes]
    transformed = [
        (gain / math.sqrt(scale)) * omega(lam, scale * ruler_sq, scale * mass_sq) + offset
        for lam in modes
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1051-K1050-FINITE-MODE-SCALE-GAUGE-OBSTRUCTION",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "dispersion": "omega_lambda(r,m)=sqrt(r*lambda+m), with r=s^2>0 and m=m^2>0",
        "readout": "y_lambda=g*omega_lambda(r,m)+b with common g>0 and common b",
        "scale_action": "(r,m,g,b)->(c*r,c*m,g/sqrt(c),b) for every c>0",
        "invariance": "the complete readout family y_lambda is unchanged for every supplied mode lambda",
        "identified_parameter": "mu=m/r is invariant under the scale action; absolute r and m are not",
        "mode_scope": "any finite or infinite collection of dispersion modes sharing the same coefficients",
        "fixture": {
            "modes": modes,
            "scale": scale,
            "maximum_residual": max(abs(a - b) for a, b in zip(original, transformed)),
        },
        "consequence": "adding modes or using affine invariants cannot identify absolute mass while common gain and the spatial ruler scale are both free",
        "reopener": "independently own one dimensional scale or calibrate the common gain against an external standard",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["dispersion"].startswith("omega_lambda") and "r=s^2>0" in d["dispersion"]
    assert d["readout"].startswith("y_lambda=g*") and "common b" in d["readout"]
    assert d["scale_action"] == "(r,m,g,b)->(c*r,c*m,g/sqrt(c),b) for every c>0"
    assert "unchanged" in d["invariance"] and "every supplied mode" in d["invariance"]
    assert d["identified_parameter"].startswith("mu=m/r") and "absolute r and m are not" in d["identified_parameter"]
    assert d["mode_scope"].startswith("any finite or infinite")
    assert d["fixture"]["modes"] == [0, 1, 3, 8, 15]
    assert d["fixture"]["scale"] == 11.0 and d["fixture"]["maximum_residual"] < 1e-12
    assert "adding modes" in d["consequence"] and "absolute mass" in d["consequence"]
    assert d["reopener"].startswith("independently own one dimensional scale")
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1051 controls: 11/11")
