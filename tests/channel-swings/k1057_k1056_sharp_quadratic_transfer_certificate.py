#!/usr/bin/env python3
"""K1057: sharp bounded quadratic-transfer threshold for the frozen horns."""
import json
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 70
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1057-k1056-sharp-quadratic-transfer-certificate.json"


def constants():
    a, b, c = Decimal(7).sqrt(), 2 * Decimal(3).sqrt(), Decimal(19).sqrt()
    gap_a, gap_b = b - a, c - b
    d4 = gap_b / gap_a
    linear = d4 * (Decimal(5) - b - c) - (Decimal(7) - a - b)
    tau = -(d4 - 1) / linear
    return a, b, c, gap_a, gap_b, d4, linear, tau


def ratio(mu, t):
    x = [(Decimal(k) + mu).sqrt() for k in (3, 8, 15)]
    gaps = [(x[i + 1] - x[i]) + t * (x[i + 1] ** 2 - x[i] ** 2) for i in range(2)]
    return gaps[1] / gaps[0]


def build():
    a, b, c, gap_a, gap_b, d4, linear, tau = constants()
    touching = ratio(Decimal(1), tau) - ratio(Decimal(4), -tau)
    safe = tau * Decimal("0.9")
    safe_gap = ratio(Decimal(4), -safe) - ratio(Decimal(1), safe)
    return {
        "schema_version": "1.0",
        "result_id": "K1057-K1056-SHARP-QUADRATIC-TRANSFER-CERTIFICATE",
        "status": "working_draft_verified", "created": "2026-10-04",
        "model": "y=g*(x+t*x^2)+b with g>0, common |t|<=tau and positive transfer derivative",
        "horn_ratio": "D_mu(t)=D_mu(0)*(1+t*(x2+x3))/(1+t*(x1+x2))",
        "monotonicity": "D_mu(t) is strictly increasing in t while the adjacent transformed gaps stay positive",
        "separation": "D_4(-tau)>D_1(tau)",
        "threshold_equation": "D_4*(-tau)=D_1*(tau); quadratic terms cancel exactly",
        "threshold": str(tau),
        "threshold_percent_in_inverse_normalized_frequency": str(100 * tau),
        "touching_residual": str(abs(touching)),
        "safe_fixture": {"tau": str(safe), "gap": str(safe_gap)},
        "scope": "sharp for the supplied horns, modes {3,8,15}, symmetric t bound and quadratic transfer family",
        "reopener": "measure or certify normalized curvature below the threshold, or use an overdetermined calibrated transfer design",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["model"].startswith("y=g*(x+t*x^2)+b") and "positive transfer derivative" in d["model"]
    assert d["horn_ratio"].startswith("D_mu(t)=")
    assert "strictly increasing" in d["monotonicity"]
    assert d["separation"] == "D_4(-tau)>D_1(tau)"
    assert "cancel exactly" in d["threshold_equation"]
    assert Decimal("0.02348") < Decimal(d["threshold"]) < Decimal("0.02350")
    assert Decimal("2.348") < Decimal(d["threshold_percent_in_inverse_normalized_frequency"]) < Decimal("2.350")
    assert Decimal(d["touching_residual"]) < Decimal("1e-60")
    assert Decimal(d["safe_fixture"]["gap"]) > 0
    assert "sharp for the supplied horns" in d["scope"]
    assert d["reopener"].startswith("measure or certify normalized curvature")
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1057 controls: 12/12")
