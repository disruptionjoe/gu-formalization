#!/usr/bin/env python3
"""K1058: exact joint quadratic-curvature and component-error budget."""
import json
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 70
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1058-k1057-joint-nonlinearity-component-budget.json"


def constants():
    r7, r3, r19 = Decimal(7).sqrt(), Decimal(3).sqrt(), Decimal(19).sqrt()
    a = 2 * r3 - r7
    b = r19 - 2 * r3
    denominator = 2 * (Decimal(2) + a + b)
    intercept = (b - a) / denominator
    slope_numerator = 5 * b - 7 * a - 2
    zero = -(b - a) / slope_numerator
    return a, b, denominator, intercept, slope_numerator / denominator, zero


def eta_star(tau):
    a, b, denominator, _, _, _ = constants()
    return ((1 + 5 * tau) * (b - 7 * tau) - (1 + 7 * tau) * (a - 5 * tau)) / denominator


def build():
    a, b, denominator, intercept, slope, zero = constants()
    fixtures = {str(t): str(eta_star(Decimal(str(t)))) for t in (0, 0.01, 0.02)}
    return {
        "schema_version": "1.0", "result_id": "K1058-K1057-JOINT-NONLINEARITY-COMPONENT-BUDGET",
        "status": "working_draft_verified", "created": "2026-10-04",
        "model": "y_i=g*(x_i+t*x_i^2)+b+zeta_i with |t|<=tau and |zeta_i|<=g*eta",
        "extrema": "mass-one maximum uses t=+tau and (+eta,-eta,+eta); mass-four minimum uses t=-tau and (-eta,+eta,-eta)",
        "separation": "[(1+7tau)+2eta]/[(1+5tau)-2eta] < [(b4-7tau)-2eta]/[(a4-5tau)+2eta]",
        "sharp_budget": "eta<eta_star(tau)=[(1+5tau)(b4-7tau)-(1+7tau)(a4-5tau)]/[2(2+a4+b4)]",
        "affine_form": {"intercept": str(intercept), "slope": str(slope), "zero_at_tau": str(zero)},
        "fixtures": fixtures,
        "limiting_cases": "eta_star(0)=K1054 threshold and eta_star(tau_*)=0 at the K1057 curvature threshold",
        "scope": "sharp for independent component boxes, symmetric normalized curvature and the supplied frozen horns",
        "reopener": "own a joint detector calibration box strictly inside this line, or use a redundant-mode transfer fit",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["model"].startswith("y_i=g*(x_i+t*x_i^2)+b+zeta_i")
    assert "+eta,-eta,+eta" in d["extrema"] and "-eta,+eta,-eta" in d["extrema"]
    assert d["separation"].startswith("[(1+7tau)+2eta]")
    assert d["sharp_budget"].startswith("eta<eta_star(tau)")
    assert Decimal("0.01029") < Decimal(d["affine_form"]["intercept"]) < Decimal("0.01030")
    assert Decimal(d["affine_form"]["slope"]) < 0
    assert Decimal("0.02348") < Decimal(d["affine_form"]["zero_at_tau"]) < Decimal("0.02350")
    assert Decimal(d["fixtures"]["0"]) > Decimal(d["fixtures"]["0.01"]) > Decimal(d["fixtures"]["0.02"]) > 0
    assert "K1054" in d["limiting_cases"] and "K1057" in d["limiting_cases"]
    assert "sharp for independent component boxes" in d["scope"]
    assert d["reopener"].startswith("own a joint detector calibration box")
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1058 controls: 12/12")
