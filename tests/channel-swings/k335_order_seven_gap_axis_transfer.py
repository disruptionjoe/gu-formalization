#!/usr/bin/env python3
"""Audit and discharge the high-order envelope gate for K334 gap transfer.

K309 proves that every Duffy gap-axis second derivative stays inside the same
regularized determinant architecture, but raises the D4 kernel order to eight.
K328 serialized only orders zero through six because that was sufficient for
the y master.  The recurrence itself is general.  This result emits the exact
rational order-seven/eight scaled envelopes and binds all five K309 axes to the
accepted K334 subdivision.  It also records the still-missing axis-native
numeric entry-jet map; structural template counts are not silently converted
into constants.
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
HERE = Path(__file__).resolve().parent
K328_MODULE = HERE / "k328_order_seven_scaled_derivative_envelope_bank.py"
K305 = ROOT / "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json"
K309 = ROOT / "lab/process/k309-order-seven-gap-axis-transfer-audit.json"
K328 = ROOT / "lab/process/k328-order-seven-scaled-derivative-envelope-bank.json"
K334 = ROOT / "lab/process/k334-order-seven-recursive-global-subdivision.json"
OUTPUT = ROOT / "lab/process/k335-order-seven-gap-axis-transfer.json"

ORDERS = (7, 8)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    module = load_module(K328_MODULE, "k335_k328_backend")
    k305 = json.loads(K305.read_text())
    k309 = json.loads(K309.read_text())
    k328 = json.loads(K328.read_text())
    k334 = json.loads(K334.read_text())
    if not k334["decision"]["five_gap_axis_transfer_released"]:
        raise AssertionError("K334 accepted subdivision not released")
    if not k309["decision"]["same_regularized_operator_architecture_valid_for_all_five_gap_axes"]:
        raise AssertionError("K309 transfer architecture unavailable")

    widths = [Fraction(value) for value in k328["fixed_control"]["widths"]]
    rows = []
    controls = []
    for width in widths:
        bounds = [module.scaled_derivative_upper(order, width) for order in ORDERS]
        rows.append({
            "width": q(width),
            "orders": list(ORDERS),
            "Phi_abs_uppers": [q(value) for value in bounds],
        })
        for order in ORDERS:
            for argument in (width / 4, width):
                controls.append(module.positive_control(order, width, argument))
    if not all(item["contained"] for item in controls):
        raise AssertionError("an order-seven/eight Arb control escaped")

    axis_rows = []
    for item in k309["axis_transfer"]:
        axis_rows.append({
            "axis": item["axis"],
            "duffy_node": item["duffy_node"],
            "duffy_weight_exponent": item["duffy_weight_exponent"],
            "peano_kernel_integral": item["peano_kernel_integral"],
            "D4_maximum_kernel_derivative_order": item["D4_maximum_kernel_derivative_order"],
            "bordered_B5_maximum_kernel_derivative_order": item["bordered_B5_maximum_kernel_derivative_order"],
            "accepted_subdivision_checksum": k334["recursive_cover"]["coverage_checksum"],
            "accepted_finite_leaf_count": k334["recursive_cover"]["finite_leaf_count"],
            "shared_geometry_reuse_released": True,
            "high_order_scaled_envelopes_available": item["D4_maximum_kernel_derivative_order"] <= 8,
            "numerical_axis_constant_emitted": False,
        })

    missing = [
        "the exact affine Duffy derivative vector dp_i/dt_j on every labelled K334 leaf",
        "value/first/second intervals for the explicit P*V4_left*V4_right*V3_left*V3_right factor on each axis",
        "the shared-entry D4 and bordered-B5 directional jet matrices implementing K305 column replacements before determinant enclosure",
        "the projective-face preconditioned order-seven/eight slot map and the corresponding radial tail degree ledger",
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K335-ORDER-SEVEN-GAP-AXIS-TRANSFER",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json",
                "lab/process/k309-order-seven-gap-axis-transfer-audit.json",
                "lab/process/k328-order-seven-scaled-derivative-envelope-bank.json",
                "lab/process/k334-order-seven-recursive-global-subdivision.json",
            ],
            "extended_scaled_derivative_orders": list(ORDERS),
            "widths": [q(value) for value in widths],
            "gap_axes": [item["axis"] for item in axis_rows],
        },
        "order_seven_eight_scaled_envelopes": {
            "definition": "Phi_m(w)=w^(m+1)*abs((2*K1)^(m)(w))",
            "rows": rows,
            "positive_argument_controls": controls,
            "all_bounds_exact_rational": True,
            "raw_Bessel_evaluation_at_zero_used": False,
            "all_controls_contained": all(item["contained"] for item in controls),
        },
        "axis_transfer": axis_rows,
        "numerical_transfer_gate": {
            "K305_group_axis_order_master_count": k305["template_compression"]["new_group_axis_order_master_functionals"],
            "K305_gap_group_axis_order_master_count": k305["template_compression"]["gap_group_axis_order_masters_after"],
            "K309_structural_operator_specification_complete": True,
            "K334_subdivision_geometry_reusable": True,
            "scaled_kernel_orders_zero_through_eight_available": True,
            "axis_native_numeric_entry_jet_map_serialized": False,
            "missing_executable_fields": missing,
            "structural_template_counts_are_not_numerical_constants": True,
        },
        "decision": {
            "all_five_gap_axes_bound_to_K334_subdivision": True,
            "order_seven_eight_zero_safe_envelopes_complete": True,
            "complete_gap_axis_constants_emitted": False,
            "complete_six_axis_peano_norm_emitted": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "serialize the four missing axis-native numeric maps, then evaluate the K305 shared-entry column-replacement determinants on every accepted K334 leaf before applying each K299 Peano mass",
        },
        "release_test": {
            "five_axes_replayed": [item["axis"] for item in axis_rows] == ["t0", "t1", "t2", "t3", "t4"],
            "all_high_order_controls_contained": all(item["contained"] for item in controls),
            "K334_checksum_replayed_on_every_axis": len({item["accepted_subdivision_checksum"] for item in axis_rows}) == 1,
            "no_gap_constant_inferred_from_y_bank": all(not item["numerical_axis_constant_emitted"] for item in axis_rows),
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k334["ledger_effect"],
        "source_routing": k334["source_routing"],
        "claim_ceiling": "Exact rational zero-safe scaled Bessel envelopes through orders seven and eight, discharging K309's high-order kernel-envelope prerequisite for every gap axis and binding all five axes to K334's accepted recursive subdivision checksum. K305/K309 provide structural column-replacement and face-integrability contracts but not the four serialized axis-native numerical maps listed here, so no gap-axis constant, six-axis Peano norm, K294 gamma join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim is emitted.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["extended_scaled_derivative_orders"] != [7, 8] or fixed["gap_axes"] != ["t0", "t1", "t2", "t3", "t4"]:
        raise AssertionError("order or axis census changed")
    bank = payload["order_seven_eight_scaled_envelopes"]
    if not bank["all_bounds_exact_rational"] or bank["raw_Bessel_evaluation_at_zero_used"] or not bank["all_controls_contained"]:
        raise AssertionError("high-order envelope contract changed")
    if any(row["orders"] != [7, 8] or len(row["Phi_abs_uppers"]) != 2 for row in bank["rows"]):
        raise AssertionError("high-order row changed")
    axes = payload["axis_transfer"]
    if len(axes) != 5 or any(not row["shared_geometry_reuse_released"] or not row["high_order_scaled_envelopes_available"] for row in axes):
        raise AssertionError("axis transfer readiness changed")
    gate = payload["numerical_transfer_gate"]
    if gate["axis_native_numeric_entry_jet_map_serialized"] or len(gate["missing_executable_fields"]) != 4:
        raise AssertionError("numeric transfer gate misstated")
    if not gate["structural_template_counts_are_not_numerical_constants"]:
        raise AssertionError("structural counts were promoted to constants")
    decision = payload["decision"]
    if decision["complete_gap_axis_constants_emitted"] or decision["complete_six_axis_peano_norm_emitted"] or decision["k294_gamma_join_released"]:
        raise AssertionError("downstream result overclaimed")


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
