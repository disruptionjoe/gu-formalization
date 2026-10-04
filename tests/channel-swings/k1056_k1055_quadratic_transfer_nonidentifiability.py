#!/usr/bin/env python3
"""K1056: an unknown monotone quadratic transfer destroys shape identification."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1056-k1055-quadratic-transfer-nonidentifiability.json"


def build():
    modes = [0, 3, 8, 15, 24]
    horns = [1.0, 4.0]
    residuals = []
    derivative_floor = float("inf")
    for mu in horns:
        for lam in modes:
            x = math.sqrt(lam + mu)
            residuals.append(abs((x * x - mu) - lam))
            derivative_floor = min(derivative_floor, 2.0 * x)
    return {
        "schema_version": "1.0",
        "result_id": "K1056-K1055-QUADRATIC-TRANSFER-NONIDENTIFIABILITY",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "dispersion": "x_mu(lambda)=sqrt(lambda+mu) in normalized ruler units",
        "transfer_family": "T_mu(x)=x^2-mu, a strictly increasing quadratic transfer on x>0",
        "common_readout": "T_mu(x_mu(lambda))=lambda for every supplied lambda and every mu>0",
        "scope": "the countermodel holds simultaneously on any finite or infinite positive-mode set",
        "fixture": {"modes": modes, "horns": horns, "maximum_residual": max(residuals), "derivative_floor": derivative_floor},
        "consequence": "without a calibrated restriction below arbitrary quadratic transfer, spectrum shape mu is nonidentifiable even with unlimited modes",
        "affine_boundary": "K1052 remains exact only for a common affine transfer or a separately certified nonlinear extension",
        "reopener": "bound detector curvature or add redundant modes under a finite-dimensional transfer model with nonzero linear response",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["dispersion"].startswith("x_mu(lambda)=sqrt")
    assert d["transfer_family"].startswith("T_mu(x)=x^2-mu") and "strictly increasing" in d["transfer_family"]
    assert d["common_readout"].endswith("every mu>0")
    assert "finite or infinite" in d["scope"]
    assert d["fixture"]["modes"] == [0, 3, 8, 15, 24]
    assert d["fixture"]["horns"] == [1.0, 4.0]
    assert d["fixture"]["maximum_residual"] < 1e-12
    assert d["fixture"]["derivative_floor"] > 0
    assert "nonidentifiable" in d["consequence"] and "unlimited modes" in d["consequence"]
    assert "common affine transfer" in d["affine_boundary"]
    assert d["reopener"].startswith("bound detector curvature")
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1056 controls: 12/12")
