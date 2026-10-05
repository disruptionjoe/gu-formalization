#!/usr/bin/env python3
"""K1114: propagate scalar sample errors into the Loewner pencil."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1114-k1113-loewner-data-error-propagation.json"


def build():
    m = 2
    eta = Fraction(1, 1000)
    eps_alpha = Fraction(1, 2000)
    eps_beta = Fraction(1, 1000)
    gap = Fraction(1)
    radius = Fraction(3)
    ordinary_entry = 2 * eta / gap + eps_alpha
    shifted_entry = 2 * radius * eta / gap + 2 * radius * eps_alpha + eps_beta
    return {
        "schema_version": "1.0",
        "result_id": "K1114-K1113-LOEWNER-DATA-ERROR-PROPAGATION",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "sample_model": "|S_hat(z)-S(z)|<=eta on two disjoint m-node sets, cross-gap g=min|x_i-y_j|>0, and |x_i|,|y_j|<=R",
        "affine_model": "|alpha_hat-alpha|<=epsilon_alpha and |beta_hat-beta|<=epsilon_beta",
        "ordinary_entry_bound": "|Delta R_ij|<=2*eta/g+epsilon_alpha",
        "ordinary_norm_bound": "||Delta R||_2<=m*(2*eta/g+epsilon_alpha)",
        "shifted_entry_bound": "|Delta P_ij|<=2*R*eta/g+2*R*epsilon_alpha+epsilon_beta",
        "shifted_norm_bound": "||Delta P||_2<=m*(2*R*eta/g+2*R*epsilon_alpha+epsilon_beta)",
        "fixture": {"m": m, "eta": str(eta), "epsilon_alpha": str(eps_alpha), "epsilon_beta": str(eps_beta), "g": str(gap), "R": str(radius)},
        "fixture_ordinary_entry_bound": str(ordinary_entry),
        "fixture_ordinary_norm_bound": str(m * ordinary_entry),
        "fixture_shifted_entry_bound": str(shifted_entry),
        "fixture_shifted_norm_bound": str(m * shifted_entry),
        "decision": "sample spacing and affine-parameter errors must be budgeted jointly before applying rank or generalized-eigenvalue stability",
        "scope_boundary": "deterministic conditional error map; no measured GU branch values, affine calibration or apparatus systematic budget",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["sample_model"].startswith("|S_hat(z)-S(z)|<=eta")
    assert d["affine_model"].startswith("|alpha_hat-alpha|")
    assert d["ordinary_entry_bound"] == "|Delta R_ij|<=2*eta/g+epsilon_alpha"
    assert d["ordinary_norm_bound"].startswith("||Delta R||_2<=m*")
    assert d["shifted_entry_bound"].startswith("|Delta P_ij|<=2*R*eta/g")
    assert d["shifted_norm_bound"].startswith("||Delta P||_2<=m*")
    assert d["fixture"] == {"m": 2, "eta": "1/1000", "epsilon_alpha": "1/2000", "epsilon_beta": "1/1000", "g": "1", "R": "3"}
    assert d["fixture_ordinary_entry_bound"] == "1/400"
    assert d["fixture_ordinary_norm_bound"] == "1/200"
    assert d["fixture_shifted_entry_bound"] == "1/100"
    assert d["fixture_shifted_norm_bound"] == "1/50"
    assert "budgeted jointly" in d["decision"]
    assert "no measured GU branch values" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1114 controls: 14/14")
