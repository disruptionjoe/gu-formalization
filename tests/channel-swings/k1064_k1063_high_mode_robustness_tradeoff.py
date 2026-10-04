#!/usr/bin/env python3
"""K1064: fourth-mode preparation versus robust quadratic-horn separation."""
import json
import math
from pathlib import Path
from k1061_k1060_four_mode_residual_witness import witness, frequencies, dot

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1064-k1063-high-mode-robustness-tradeoff.json"
N_VALUES = [4, 5, 6, 8, 12, 16, 24, 32, 64, 128]


def threshold(n):
    modes = [3, 8, 15, n * (n + 2)]
    c14 = abs(dot(witness(4, modes), frequencies(1, modes)))
    c41 = abs(dot(witness(1, modes), frequencies(4, modes)))
    return {"n": n, "lambda_four": modes[-1], "c_1_to_4": c14, "c_4_to_1": c41,
            "eta_over_gamma": min(c14, c41) / 2.0}


def three_node_limit(mu, other):
    modes = [3, 8, 15]
    xs, ys = frequencies(mu, modes), frequencies(other, modes)
    raw = []
    for i, xi in enumerate(xs):
        product = 1.0
        for j, xj in enumerate(xs):
            if i != j: product *= xi - xj
        raw.append(1.0 / product)
    scale = sum(abs(v) for v in raw)
    weights = [v / scale for v in raw]
    return abs(dot(weights, ys))


def build():
    table = [threshold(n) for n in N_VALUES]
    limits = {"c_1_to_4": three_node_limit(4, 1), "c_4_to_1": three_node_limit(1, 4)}
    return {
        "schema_version": "1.0",
        "result_id": "K1064-K1063-HIGH-MODE-ROBUSTNESS-TRADEOFF",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "fixed_modes": [3, 8, 15],
        "prepared_fourth_mode_family": "lambda_n=n(n+2), n>=4",
        "fixture_table": table,
        "asymptotic_directed_contrasts": limits,
        "asymptotic_symmetric_eta_over_gamma": min(limits.values()) / 2.0,
        "limit_proof": "after l1 normalization, the fourth barycentric weight vanishes and the first three weights converge to the l1-normalized three-node second-divided-difference witness",
        "monotonicity_ceiling": "the listed fixtures increase; no global monotonicity theorem is claimed",
        "apparatus_tradeoff": "higher prepared modes improve the conditional error budget but increase preparation range and do not own the dimensional ruler or detector model",
        "scope": "analytic high-mode limit plus finite checked fixtures for the supplied horn family",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(data):
    assert data["fixed_modes"] == [3, 8, 15]
    assert data["prepared_fourth_mode_family"] == "lambda_n=n(n+2), n>=4"
    table = data["fixture_table"]
    assert [row["n"] for row in table] == N_VALUES
    assert all(table[i]["eta_over_gamma"] < table[i + 1]["eta_over_gamma"] for i in range(len(table) - 1))
    assert 0.00241 < table[0]["eta_over_gamma"] < 0.00242
    assert 0.00955 < data["asymptotic_symmetric_eta_over_gamma"] < 0.00956
    assert "fourth barycentric weight vanishes" in data["limit_proof"]
    assert data["monotonicity_ceiling"].endswith("no global monotonicity theorem is claimed")
    assert "do not own the dimensional ruler" in data["apparatus_tradeoff"]
    assert data["scope"].startswith("analytic high-mode limit")
    assert data["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    result = build(); validate(result)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("K1064 controls: 12/12")
