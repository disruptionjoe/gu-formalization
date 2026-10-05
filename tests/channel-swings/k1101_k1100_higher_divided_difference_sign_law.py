#!/usr/bin/env python3
"""K1101: higher divided-difference sign law for Stieltjes branches."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1101-k1100-higher-divided-difference-sign-law.json"


def branch(x, alpha=Fraction(2), beta=Fraction(5)):
    return alpha * x + beta - Fraction(1, x + 1) - Fraction(4, x + 3)


def divided_difference(xs, values):
    row = list(values)
    for order in range(1, len(xs)):
        row = [
            (row[i + 1] - row[i]) / (xs[i + order] - xs[i])
            for i in range(len(row) - 1)
        ]
    return row[0]


def build():
    modes = list(range(5))
    values = [branch(Fraction(x)) for x in modes]
    witnesses = {
        str(order): str(divided_difference(modes[: order + 1], values[: order + 1]))
        for order in (2, 3, 4)
    }
    return {
        "schema_version": "1.0",
        "result_id": "K1101-K1100-HIGHER-DIVIDED-DIFFERENCE-SIGN-LAW",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "general_identity": "for k>=2, S[x0,...,xk]=(-1)^(k+1) sum_i w_i/prod_j(x_j+d_i)",
        "strict_sign_rule": "(-1)^(k+1) S[x0,...,xk]>0 iff at least one w_i>0 on the common positive domain",
        "fixture_modes": modes,
        "fixture_values": [str(v) for v in values],
        "fixture_witnesses": witnesses,
        "orders_checked": [2, 3, 4],
        "decision": "every higher exact divided difference alternates sign in the positive diagonal Stieltjes class, but the sign sequence alone does not identify the auxiliary realization",
        "scope_boundary": "conditional scalar rational-function theorem; no source-selected GU Hessian, physical spectrum or measured mode",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["general_identity"].startswith("for k>=2")
    assert "iff at least one w_i>0" in d["strict_sign_rule"]
    assert d["fixture_modes"] == [0, 1, 2, 3, 4]
    assert d["fixture_values"] == ["8/3", "11/2", "118/15", "121/12", "428/35"]
    assert d["fixture_witnesses"] == {"2": "-7/30", "3": "19/360", "4": "-5/504"}
    assert d["orders_checked"] == [2, 3, 4]
    assert "does not identify" in d["decision"]
    assert "no source-selected GU Hessian" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1101 controls: 9/9")
