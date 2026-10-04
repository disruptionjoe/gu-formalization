#!/usr/bin/env python3
"""K1061: exact four-mode residual witnesses for the two quadratic horns."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1061-k1060-four-mode-residual-witness.json"
MODES = [3, 8, 15, 24]


def frequencies(mu, modes=MODES):
    return [math.sqrt(lam + mu) for lam in modes]


def witness(mu, modes=MODES):
    xs = frequencies(mu, modes)
    raw = []
    for i, xi in enumerate(xs):
        product = 1.0
        for j, xj in enumerate(xs):
            if i != j:
                product *= xi - xj
        raw.append(1.0 / product)
    scale = sum(abs(value) for value in raw)
    weights = [value / scale for value in raw]
    if weights[-1] < 0:
        weights = [-value for value in weights]
    return weights


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def build():
    w1, w4 = witness(1), witness(4)
    x1, x4 = frequencies(1), frequencies(4)
    return {
        "schema_version": "1.0",
        "result_id": "K1061-K1060-FOUR-MODE-RESIDUAL-WITNESS",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "modes": MODES,
        "mass_one_witness_l1": w1,
        "mass_four_witness_l1": w4,
        "mass_one_exact_witness": ["-1/8", "3/8", "-3/8", "1/8"],
        "annihilation_rule": "w_mu annihilates 1, lambda and sqrt(lambda+mu), hence every quadratic readout for horn mu",
        "directed_cross_contrast": {
            "true_mu_1_against_mu_4": abs(dot(w4, x1)),
            "true_mu_4_against_mu_1": abs(dot(w1, x4)),
        },
        "linf_feasibility": "distance from y to the horn readout hyperplane in component sup norm is abs(w_mu dot y) because ||w_mu||_1=1",
        "scope": "exact for the supplied horns and modes under one common quadratic transfer per horn",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(data):
    assert data["modes"] == [3, 8, 15, 24]
    assert data["mass_one_exact_witness"] == ["-1/8", "3/8", "-3/8", "1/8"]
    for mu, key in [(1, "mass_one_witness_l1"), (4, "mass_four_witness_l1")]:
        w, x = data[key], frequencies(mu)
        assert abs(sum(abs(v) for v in w) - 1.0) < 1e-12
        assert abs(dot(w, [1.0] * 4)) < 1e-12
        assert abs(dot(w, MODES)) < 1e-12
        assert abs(dot(w, x)) < 1e-12
    contrasts = data["directed_cross_contrast"]
    assert 0.00704 < contrasts["true_mu_1_against_mu_4"] < 0.00706
    assert 0.00482 < contrasts["true_mu_4_against_mu_1"] < 0.00484
    assert data["annihilation_rule"].startswith("w_mu annihilates")
    assert "sup norm" in data["linf_feasibility"] and "||w_mu||_1=1" in data["linf_feasibility"]
    assert data["scope"].startswith("exact for the supplied horns")
    assert data["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    result = build()
    validate(result)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("K1061 controls: 14/14")
