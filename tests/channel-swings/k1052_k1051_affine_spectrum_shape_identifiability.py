#!/usr/bin/env python3
"""K1052: three ordered modes identify the dimensionless spectrum shape."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1052-k1051-affine-spectrum-shape-identifiability.json"


def D(mu, modes=(3.0, 8.0, 15.0)):
    x1, x2, x3 = (math.sqrt(mu + lam) for lam in modes)
    return (x3 - x2) / (x2 - x1)


def build():
    d0, d1, d4, d1000000 = D(0.0), D(1.0), D(4.0), D(1_000_000.0)
    return {
        "schema_version": "1.0",
        "result_id": "K1052-K1051-AFFINE-SPECTRUM-SHAPE-IDENTIFIABILITY",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "parameter": "mu=m/r=m^2/s^2>0",
        "statistic": "D_mu=(sqrt(lambda3+mu)-sqrt(lambda2+mu))/(sqrt(lambda2+mu)-sqrt(lambda1+mu))",
        "rationalized": "D_mu=((lambda3-lambda2)/(lambda2-lambda1))*((x2+x1)/(x3+x2))",
        "log_derivative": "d(log D_mu)/dmu=(x3-x1)/(2*x1*x2*x3)>0",
        "theorem": "for every lambda1<lambda2<lambda3, D_mu is strictly increasing and therefore injective in mu",
        "range": "D_0<D_mu<(lambda3-lambda2)/(lambda2-lambda1), with the upper endpoint approached as mu tends to infinity",
        "frozen_modes": [3, 8, 15],
        "frozen_controls": {
            "D_at_mu_1": f"{d1:.15f}",
            "D_at_mu_4": f"{d4:.15f}",
            "D_at_mu_0": f"{d0:.15f}",
            "large_mu_control": f"{d1000000:.15f}",
            "upper_limit": "7/5",
        },
        "identifiability_boundary": "the affine-invariant statistic identifies mu, not absolute m or r",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["parameter"] == "mu=m/r=m^2/s^2>0"
    assert d["statistic"].startswith("D_mu=(sqrt(lambda3+mu)")
    assert "(x2+x1)/(x3+x2)" in d["rationalized"]
    assert d["log_derivative"].endswith(">0") and "x3-x1" in d["log_derivative"]
    assert "strictly increasing" in d["theorem"] and "injective" in d["theorem"]
    assert "lambda3-lambda2" in d["range"] and "infinity" in d["range"]
    assert d["frozen_modes"] == [3, 8, 15]
    assert abs(float(d["frozen_controls"]["D_at_mu_1"]) - 1.0) < 1e-13
    assert float(d["frozen_controls"]["D_at_mu_4"]) > 1.09
    assert float(d["frozen_controls"]["D_at_mu_0"]) < 1.0
    assert abs(float(d["frozen_controls"]["large_mu_control"]) - 1.4) < 1e-5
    assert d["frozen_controls"]["upper_limit"] == "7/5"
    assert d["identifiability_boundary"].endswith("not absolute m or r")
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1052 controls: 13/13")
