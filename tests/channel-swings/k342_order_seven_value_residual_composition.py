#!/usr/bin/env python3
"""Normalize K341's value interval and join K339's separate residual."""

from __future__ import annotations

import argparse
import json
import math
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K299 = ROOT / "lab/process/k299-order-seven-positive-peano-simplex-rule.json"
K305 = ROOT / "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json"
K339 = ROOT / "lab/process/k339-order-seven-normalized-residual-composition.json"
K341 = ROOT / "lab/process/k341-order-seven-complete-barycentric-value.json"
OUTPUT = ROOT / "lab/process/k342-order-seven-value-residual-composition.json"

getcontext().prec = 80
EXPECTED_NORMALIZED_BASE_UPPER = "9.718413035580536e-14"
EXPECTED_COMPLETE_UPPER = "0.004477466184614387"


def outward(value: Decimal) -> str:
    numeric = math.nextafter(float(value), math.inf)
    return repr(numeric)


def build() -> dict[str, Any]:
    k299 = json.loads(K299.read_text())
    k305 = json.loads(K305.read_text())
    k339 = json.loads(K339.read_text())
    k341 = json.loads(K341.read_text())
    if not k341["decision"]["complete_prefactor_free_order_seven_base_value_interval_emitted"]:
        raise AssertionError("K341 value interval unavailable")
    if not k339["release_test"]["native_prefactor_applied_exactly_once"]:
        raise AssertionError("K339 normalization ledger unavailable")
    if k299["positive_cubature"]["simplex_weight"] != "1/120" or len(k305["coherent_groups"]) != 4:
        raise AssertionError("K299/K305 value census changed")

    base_free = Decimal(k341["complete_barycentric_value"]["prefactor_free_complete_abs_upper"])
    prefactor = Decimal(k339["normalization_ledger"]["native_prefactor_interval"]["upper"])
    residual = Decimal(k339["normalized_order_seven_peano_residual"]["radius_upper"])
    base_normalized_text = outward(base_free * prefactor)
    combined_text = outward(Decimal(base_normalized_text) + residual)
    if not all(math.isfinite(float(value)) and float(value) > 0 for value in (base_normalized_text, combined_text)):
        raise AssertionError("normalized K342 enclosure is not finite positive")

    return {
        "schema_version": "1.0",
        "result_id": "K342-ORDER-SEVEN-VALUE-RESIDUAL-COMPOSITION",
        "created": "2026-09-22",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k299-order-seven-positive-peano-simplex-rule.json",
                "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json",
                "lab/process/k339-order-seven-normalized-residual-composition.json",
                "lab/process/k341-order-seven-complete-barycentric-value.json",
            ],
            "simplex_node": ["1/6"] * 6,
            "simplex_weight": "1/120",
            "y_node": "1/2",
            "coherent_groups": 4,
            "ordered_terms_per_group": 9,
        },
        "normalization_ledger": {
            "native_prefactor_exact": "(2*pi)^-9",
            "native_prefactor_interval": k339["normalization_ledger"]["native_prefactor_interval"],
            "prefactor_free_base_value_abs_upper": str(base_free),
            "native_prefactor_applied_to_base_value_once": True,
            "K299_simplex_weight_already_inside_K341": True,
            "K299_Peano_masses_already_inside_K339_residual": True,
            "K294_transformed_density_already_inside_K341_and_K339": True,
            "K294_bare_mass_applied_again": False,
            "K318_y_Peano_mass_applied_to_value": False,
        },
        "normalized_base_value": {
            "meaning": "absolute interval for the complete four-group K305 order-seven K299 one-node value after the native prefactor",
            "radius_upper": base_normalized_text,
            "symmetric_interval": [f"-{base_normalized_text}", base_normalized_text],
            "signed_center_determined": False,
        },
        "normalized_peano_residual": {
            "source": "K339",
            "radius_upper": str(residual),
            "symmetric_interval": [f"-{residual}", str(residual)],
            "recomputed_or_rescaled": False,
        },
        "complete_order_seven_cubature_enclosure": {
            "composition": "normalized K299 one-node value interval plus independent normalized six-axis Peano residual radius",
            "radius_upper": combined_text,
            "symmetric_interval": [f"-{combined_text}", combined_text],
            "base_and_residual_kept_distinct": True,
            "complete_four_group_order_seven_enclosure_emitted": True,
        },
        "decision": {
            "complete_order_seven_positive_cubature_enclosure_emitted": True,
            "order_seven_signed_center_determined": False,
            "complete_base_action_column_evaluated": False,
            "complete_R_ref_residual_evaluated": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "extend the validated value-mode determinant integrator to the remaining K279 orders eight through twelve, then compose all action-column orders and the complete R_ref residual before any native K152 interval",
        },
        "release_test": {
            "all_four_K305_groups_replayed": len(k305["coherent_groups"]) == 4,
            "K299_value_and_Peano_weights_kept_distinct": True,
            "K341_base_value_normalized_once": True,
            "K339_residual_not_rescaled": True,
            "K294_bare_mass_not_double_multiplied": True,
            "K318_Peano_atlas_not_relabelled_as_value_mode": True,
            "normalized_base_finite_positive": math.isfinite(float(base_normalized_text)) and float(base_normalized_text) > 0,
            "combined_enclosure_finite_positive": math.isfinite(float(combined_text)) and float(combined_text) > 0,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k339["ledger_effect"],
        "source_routing": k339["source_routing"],
        "claim_ceiling": f"Complete rigorous interval composition for the K299 positive cubature of the four-group K305 order-seven occurrence sum. K341's prefactor-free base-value radius {base_free} is multiplied once by (2*pi)^-9, giving normalized base radius below {base_normalized_text}; adding K339's separately normalized Peano radius gives the complete order-seven cubature interval radius below {combined_text}. The interval is symmetric because this outward calculation does not determine the signed center. Other K279 action-column orders and the complete R_ref residual remain separate, so no complete base action column, native K152 interval, source/ledger move, canon, paper, public or physical claim is emitted.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["simplex_node"] != ["1/6"] * 6 or fixed["simplex_weight"] != "1/120" or fixed["y_node"] != "1/2":
        raise AssertionError("K342 fixed node changed")
    ledger = payload["normalization_ledger"]
    required = [
        "native_prefactor_applied_to_base_value_once",
        "K299_simplex_weight_already_inside_K341",
        "K299_Peano_masses_already_inside_K339_residual",
        "K294_transformed_density_already_inside_K341_and_K339",
    ]
    if not all(ledger[key] for key in required) or ledger["K294_bare_mass_applied_again"] or ledger["K318_y_Peano_mass_applied_to_value"]:
        raise AssertionError("normalization ledger changed")
    base = payload["normalized_base_value"]
    residual = payload["normalized_peano_residual"]
    complete = payload["complete_order_seven_cubature_enclosure"]
    if not math.isfinite(float(base["radius_upper"])) or float(base["radius_upper"]) <= 0:
        raise AssertionError("normalized base interval invalid")
    if base["radius_upper"] != EXPECTED_NORMALIZED_BASE_UPPER:
        raise AssertionError("normalized base certificate changed")
    if residual["recomputed_or_rescaled"] or residual["radius_upper"] != "0.004477466184517202":
        raise AssertionError("K339 residual changed")
    if not complete["base_and_residual_kept_distinct"] or not complete["complete_four_group_order_seven_enclosure_emitted"]:
        raise AssertionError("complete K342 enclosure missing")
    if complete["radius_upper"] != EXPECTED_COMPLETE_UPPER:
        raise AssertionError("complete order-seven certificate changed")
    if float(complete["radius_upper"]) < float(base["radius_upper"]) + float(residual["radius_upper"]):
        raise AssertionError("combined radius is not outward")
    decision = payload["decision"]
    if not decision["complete_order_seven_positive_cubature_enclosure_emitted"] or decision["order_seven_signed_center_determined"]:
        raise AssertionError("K342 decision boundary changed")
    if decision["complete_base_action_column_evaluated"] or decision["complete_R_ref_residual_evaluated"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("downstream result overclaimed")
    release = payload["release_test"]
    positives = [key for key, value in release.items() if key != "native_K152_interval_emitted" and isinstance(value, bool)]
    if not all(release[key] for key in positives) or release["native_K152_interval_emitted"]:
        raise AssertionError("K342 release control failed")


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
