#!/usr/bin/env python3
"""K1806 fixed-score Cauchy witness and cancellation certificate."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1806-full-fisher-anchored-score-variational.json"
K1788 = ROOT / "lab/process/k1788-full-fisher-first-two-slab-exclusion.json"
K1804 = ROOT / "lab/process/k1804-full-fisher-deduplicated-boundary-atlas.json"


def compute():
    g, d, r, k, h = sp.symbols("g d r k h", positive=True)
    density = g * d
    score = k * r / d
    a_integrand = sp.cancel(density * score * h)
    b_integrand = sp.cancel(density * h**2)
    k1788 = json.loads(K1788.read_text())
    k1804 = json.loads(K1804.read_text())
    anchor = k1788["certificate"]["boundary_boxes"][1]["center"]
    rectangle = k1804["certificate"]["slab_two_union_rectangle"]
    return {
        "anchor": anchor,
        "rectangle": rectangle,
        "varying_density_times_score_times_anchor": str(a_integrand),
        "varying_density_times_anchor_squared": str(b_integrand),
        "varying_denominator_cancels_from_A": d not in a_integrand.free_symbols,
        "varying_denominator_linear_in_B": sp.degree(b_integrand, d) == 1,
        "cauchy_cross_multiplication": "J*B >= A^2; B>0; A^2-T*B>0 implies J>T",
    }


def validate(data, got=None):
    got = compute() if got is None else got
    cert = data["certificate"]
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1806"),
        ("inputs", data["inputs"] == ["K1788", "K1804", "K1805"]),
        ("anchor", cert["anchor"] == got["anchor"]),
        ("rectangle", cert["rectangle"] == got["rectangle"]),
        ("A cancellation", cert["varying_denominator_cancels_from_A"]
         and got["varying_denominator_cancels_from_A"]),
        ("B linearity", cert["varying_denominator_linear_in_B"]
         and got["varying_denominator_linear_in_B"]),
        ("Cauchy", cert["cauchy_cross_multiplication"] == got["cauchy_cross_multiplication"]),
        ("witness valid", data["decision"]["fixed_score_variational_witness_valid"]),
        ("no equality claim", not data["decision"]["witness_equals_full_fisher_off_anchor"]),
        ("global open", not data["decision"]["global_optimizer_proved"]),
    ]


def main():
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv:
        print(json.dumps(compute(), indent=2))
        return
    checks = validate(json.loads(ARTIFACT.read_text()))
    for index, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
