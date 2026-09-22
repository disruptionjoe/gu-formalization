#!/usr/bin/env python3
"""Certify finite K308-derived bounds on explicit dyadic radial shells.

This is an interior-shell adapter, not a complete origin or projective-face
oracle.  It rescales the K308 positive angular slab, records degree-27
normalized spine controls, and uses the maximum radius on four complete
ratio-four shells to bound H=r^27*R4*R5_border outwardly.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K308_MODULE = Path(__file__).with_name(
    "k308_order_seven_regularized_y_master_operator.py"
)
K310 = ROOT / "lab/process/k310-order-seven-two-radius-origin-compactification.json"
K312 = ROOT / "lab/process/k312-order-seven-positive-cell-measure-backend.json"
OUTPUT = ROOT / "lab/process/k313-order-seven-scaled-radial-shell-oracle.json"
DEGREE = 27


def load_k308():
    spec = importlib.util.spec_from_file_location("k313_k308_backend", K308_MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K308 backend")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def radial_cell(base: dict[str, tuple[Fraction, Fraction]], lower: Fraction, upper: Fraction):
    cell = dict(base)
    cell["x"] = (lower * base["x"][0], upper * base["x"][1])
    cell["b"] = (lower * base["b"][0], upper * base["b"][1])
    return cell


def evaluate(module, cell, multiplier: Fraction) -> dict[str, Any]:
    original = module.CELL
    try:
        module.CELL = cell
        bank = module.outward_cell_bank()
    finally:
        module.CELL = original
    raw = bank["D4_times_bordered_B5_regularized_y_jet_abs_upper"]
    scaled = [
        module.upper_text(module.arb(value) * module.ball(multiplier))
        for value in raw
    ]
    return {
        "cell": bank["cell"],
        "raw_regularized_y_jet_abs_upper": raw,
        "multiplier": str(multiplier),
        "scaled_y_jet_abs_upper": scaled,
    }


def component_ratios(rows: list[dict[str, Any]]) -> list[float]:
    first = [float(value) for value in rows[0]["scaled_y_jet_abs_upper"]]
    last = [float(value) for value in rows[-1]["scaled_y_jet_abs_upper"]]
    return [last_value / first_value for first_value, last_value in zip(first, last)]


def build() -> dict[str, Any]:
    module = load_k308()
    k310 = json.loads(K310.read_text())
    k312 = json.loads(K312.read_text())
    if k310["fixed_control"]["regularized_product_simultaneous_degree"] != -DEGREE:
        raise AssertionError("K310 degree-27 normalization changed")
    if not k312["decision"]["positive_cell_measure_backend_implemented"]:
        raise AssertionError("K312 measure backend is unavailable")

    base = dict(module.CELL)
    spine_scales = [Fraction(1, 4**depth) for depth in range(5)]
    spines = []
    for scale in spine_scales:
        row = evaluate(module, radial_cell(base, scale, scale), scale**DEGREE)
        row["scale"] = str(scale)
        row["normalization"] = "scale^27 * regularized-product jet bound"
        spines.append(row)

    shells = []
    for lower in spine_scales[1:]:
        upper = 4 * lower
        cell = radial_cell(base, lower, upper)
        radius_max = cell["x"][1] + cell["b"][1]
        row = evaluate(module, cell, radius_max**DEGREE)
        row.update({
            "lower_scale": str(lower),
            "upper_scale": str(upper),
            "radius_max": str(radius_max),
            "bound_rule": "r^27 <= radius_max^27 on the complete shell slab",
        })
        shells.append(row)

    spine_ratios = component_ratios(spines)
    shell_ratios = component_ratios(shells)
    if any(not math.isfinite(value) or value <= 0 or value >= 1.01 for value in spine_ratios + shell_ratios):
        raise AssertionError("scaled radial controls are not stable on the admitted atlas")

    return {
        "schema_version": "1.0",
        "result_id": "K313-ORDER-SEVEN-SCALED-RADIAL-SHELL-ORACLE",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k308-order-seven-regularized-y-master-operator.json",
                "lab/process/k310-order-seven-two-radius-origin-compactification.json",
                "lab/process/k312-order-seven-positive-cell-measure-backend.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "scaled_regularizer_degree": DEGREE,
            "base_positive_angular_slab": {
                key: [str(value[0]), str(value[1])] for key, value in base.items()
            },
        },
        "radial_spine_controls": {
            "rows": spines,
            "last_to_first_component_ratios": [repr(value) for value in spine_ratios],
            "interpretation": "finite sampled controls of degree-27 normalization; not a proof of a continuous limit at r=0",
        },
        "dyadic_shell_oracle": {
            "shell_ratio": 4,
            "rows": shells,
            "last_to_first_component_ratios": [repr(value) for value in shell_ratios],
            "coverage": "four explicit closed radial shell slabs on the K308 interior angular cell",
            "outward_reason": "K308 bounds the raw regularized product over each union cell and r^27 is bounded by the exact shell radius maximum",
        },
        "decision": {
            "scaled_interior_shell_oracle_implemented": True,
            "degree_27_spine_stability_observed": True,
            "four_ratio_four_shells_certified": True,
            "continuous_origin_oracle_implemented": False,
            "projective_face_oracle_implemented": False,
            "terminal_split_face_composed": False,
            "complete_y_master_constant_emitted": False,
            "five_gap_axis_constants_emitted": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "derive a repeated-node projective-face divided-difference oracle and join it to these interior shells before any complete y-master adaptive sum",
        },
        "release_test": {
            "all_scaled_bounds_finite_positive": all(
                math.isfinite(float(value)) and float(value) > 0
                for row in [*spines, *shells]
                for value in row["scaled_y_jet_abs_upper"]
            ),
            "spine_ratios_below_1_01": all(value < 1.01 for value in spine_ratios),
            "shell_ratios_below_1_01": all(value < 1.01 for value in shell_ratios),
            "complete_origin_overclaim": False,
            "projective_face_overclaim": False,
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k312["ledger_effect"],
        "claim_ceiling": "Rigorous outward value/first-y/second-y bounds for H=r^27*R4*R5_border on four explicit ratio-four radial shell slabs inside K308's positive angular cell, plus five finite degree-27 normalized spine controls. The shell bounds retain the complete coherent D4-times-bordered-B5 determinant and use exact radius maxima. They do not cover r=0 continuously, either projective radial face, terminal split faces, the full angular domain, a complete y or gap-axis Peano constant, K294 gamma strata, an action-column value or residual, a native K152 interval, or any source, ledger, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    if payload["fixed_control"]["scaled_regularizer_degree"] != DEGREE:
        raise AssertionError("scaled degree changed")
    spines = payload["radial_spine_controls"]["rows"]
    shells = payload["dyadic_shell_oracle"]["rows"]
    if [row["scale"] for row in spines] != ["1", "1/4", "1/16", "1/64", "1/256"]:
        raise AssertionError("spine atlas changed")
    if [(row["lower_scale"], row["upper_scale"]) for row in shells] != [
        ("1/4", "1"), ("1/16", "1/4"), ("1/64", "1/16"), ("1/256", "1/64")
    ]:
        raise AssertionError("shell atlas changed")
    if not payload["release_test"]["all_scaled_bounds_finite_positive"]:
        raise AssertionError("nonfinite scaled bound")
    if not payload["release_test"]["spine_ratios_below_1_01"] or not payload["release_test"]["shell_ratios_below_1_01"]:
        raise AssertionError("radial stability control failed")
    decision = payload["decision"]
    if not decision["scaled_interior_shell_oracle_implemented"] or not decision["four_ratio_four_shells_certified"]:
        raise AssertionError("interior shell result missing")
    forbidden = (
        "continuous_origin_oracle_implemented",
        "projective_face_oracle_implemented",
        "terminal_split_face_composed",
        "complete_y_master_constant_emitted",
        "five_gap_axis_constants_emitted",
        "k294_gamma_join_released",
    )
    if any(decision[key] for key in forbidden):
        raise AssertionError("K313 boundary or closure overclaim")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
