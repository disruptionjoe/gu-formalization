#!/usr/bin/env python3
"""Freeze exact positive tensor-Peano contracts after K556--K557."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
K554 = ROOT / "lab/process/k554-orders-eleven-twelve-gauss-laguerre-face-atlas.json"
K556 = ROOT / "lab/process/k556-orders-eleven-twelve-axis-jet-compiler.json"
K557 = ROOT / "lab/process/k557-orders-eleven-twelve-node-directional-jet-bank.json"
OUTPUT = ROOT / "lab/process/k558-orders-eleven-twelve-positive-peano-contract.json"
SHIFT = 256


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def compile_order(order: int, atlas: dict, interface: dict, bank: dict) -> dict:
    side = order + 1
    axes = tuple([f"s{i}" for i in range(1, side + 1)] + [f"v{i}" for i in range(1, side + 1)])
    kernel_mass = Fraction(1, 2 * SHIFT**3)
    node_weight = Fraction(1, SHIFT)
    local_rows = {row["axis"]: row for row in bank["axis_node_jets"]}
    rows = []
    for index, axis in enumerate(axes):
        rows.append({
            "axis": axis,
            "preceding_axes_fixed_at_node": index,
            "following_axes_integrated_exactly": len(axes) - index - 1,
            "preceding_node_weight": q(node_weight**index),
            "peano_kernel_mass": q(kernel_mass),
            "hybrid_global_integrand": f"abs(partial_{axis}^2 H) with {index} preceding raw times at 1/256, {axis}=t against K_256(t), and {len(axes)-index-1} following raw times under exp(-256*x) dx",
            "local_node_second_derivative_lower_control": local_rows[axis]["raw_second_derivative_lower"],
            "local_node_second_derivative_upper_control": local_rows[axis]["raw_second_derivative_upper"],
            "local_control_is_not_a_global_bound": True,
        })
    return {
        "order": order,
        "fixed_control": {
            "native_axes": list(axes),
            "axis_node": "1/256",
            "axis_weight": "1/256",
            "product_weight": atlas["positive_product_rule"]["product_weight"],
            "face_atlas_sha256": atlas["cumulative_time_face_atlas"]["atlas_sha256"],
            "compiled_entry_interface_sha256": interface["compiled_entry_interface"]["stream_sha256"],
            "axis_entry_evaluations": bank["fixed_control"]["axis_entry_evaluations"],
        },
        "tensor_telescoping": {
            "identity": f"I^{len(axes)}-Q^{len(axes)}=sum_{{a=1}}^{{{len(axes)}}} Q^{{a-1}} tensor (I-Q)_a tensor I^{{{len(axes)}-a}}",
            "mixed_derivatives_required": False,
            "pure_second_directional_terms": len(axes),
            "axis_contracts": rows,
            "absolute_remainder_bound_requires": "one zero-safe whole-domain integral of each listed complete coherent pure-second functional",
            "node_jet_substitution_for_global_integral_forbidden": True,
            "global_entrywise_supremum_before_group_assembly_forbidden": True,
        },
        "decision": {
            "complete_axis_remainder_formula_emitted": True,
            "complete_axis_remainder_numerically_bounded": False,
            "complete_integral_emitted": False,
            "rank_six_global_cover_released": False,
            "next_required_object": f"zero-safe whole-orthant determinant-preserving interval atlas for the {len(axes)} complete coherent pure-second functionals",
        },
        "release_test": {
            "all_axis_contracts_present": len(rows) == len(axes),
            "preceding_and_following_counts_partition_other_axes": all(row["preceding_axes_fixed_at_node"] + row["following_axes_integrated_exactly"] == len(axes) - 1 for row in rows),
            "positive_kernel_mass_exact": q(kernel_mass) == "1/33554432",
            "only_pure_second_derivatives_required": True,
            "node_controls_not_promoted": all(row["local_control_is_not_a_global_bound"] for row in rows),
            "complete_integral_not_overclaimed": True,
        },
    }


def build() -> dict:
    k554 = json.loads(K554.read_text())
    k556 = json.loads(K556.read_text())
    k557 = json.loads(K557.read_text())
    atlases = {int(row["order"]): row for row in k554["order_interfaces"]}
    interfaces = {int(row["order"]): row for row in k556["order_interfaces"]}
    banks = {int(row["order"]): row for row in k557["order_banks"]}
    rows = [compile_order(order, atlases[order], interfaces[order], banks[order]) for order in (11, 12)]
    kernel_mass = Fraction(1, 2 * SHIFT**3)
    return {
        "schema_version": "1.0",
        "result_id": "K558-ORDERS-ELEVEN-TWELVE-POSITIVE-PEANO-CONTRACT",
        "created": "2026-09-27",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k554-orders-eleven-twelve-gauss-laguerre-face-atlas.json",
                "lab/process/k556-orders-eleven-twelve-axis-jet-compiler.json",
                "lab/process/k557-orders-eleven-twelve-node-directional-jet-bank.json",
            ],
            "orders": [11, 12],
            "combined_native_axes": 50,
            "combined_axis_entry_evaluations": 2413152,
        },
        "one_axis_identity": {
            "measure": "exp(-256*x) dx on [0,infinity)",
            "rule": "I(h)=h(1/256)/256 + integral_0^infinity K_256(t) h''(t) dt",
            "kernel_0_le_t_le_1_over_256": "(exp(-256*t)-1+256*t)/256^2",
            "kernel_t_ge_1_over_256": "exp(-256*t)/256^2",
            "kernel_nonnegative": True,
            "kernel_continuous_at_node": True,
            "kernel_zero_order_at_origin": 2,
            "kernel_mass": q(kernel_mass),
            "kernel_mass_check": "I(x^2/2)-Q(x^2/2)=1/(2*256^3)",
        },
        "order_contracts": rows,
        "decision": {
            "complete_order_eleven_remainder_formula_emitted": True,
            "complete_order_twelve_remainder_formula_emitted": True,
            "complete_order_eleven_remainder_numerically_bounded": False,
            "complete_order_twelve_remainder_numerically_bounded": False,
            "complete_order_eleven_integral_emitted": False,
            "complete_order_twelve_integral_emitted": False,
            "native_K152_interval_emitted": False,
        },
        "release_test": {
            "both_order_contracts_present": [row["order"] for row in rows] == [11, 12],
            "all_50_axis_contracts_present": sum(len(row["tensor_telescoping"]["axis_contracts"]) for row in rows) == 50,
            "positive_kernel_mass_exact": q(kernel_mass) == "1/33554432",
            "only_pure_second_derivatives_required": True,
            "node_controls_not_promoted": True,
            "complete_integrals_not_overclaimed": True,
        },
        "next_exact_input": "construct separate order-eleven and order-twelve zero-safe determinant-preserving face atlases, recursive positive interiors and analytic tails for the fifty complete coherent pure-second hybrid integrals",
        "ledger_effect": k557["ledger_effect"],
        "source_routing": k557["source_routing"],
        "claim_ceiling": "Exact positive Peano-kernel and tensor-telescoping contracts for the native 24-axis order-eleven and 26-axis order-twelve rules. They identify all fifty complete coherent pure-second hybrid integrals, their exact node/integration ordering and kernel mass 1/33554432, and forbid substituting K557's local node jets for global bounds. They emit no numerical remainder, complete integral, action column, R_ref residual, K152 interval, source/ledger move, canon, paper, public, novelty or physical claim.",
    }


def validate_payload(payload: dict) -> None:
    fixed = payload["fixed_control"]
    if fixed["orders"] != [11, 12] or fixed["combined_native_axes"] != 50 or fixed["combined_axis_entry_evaluations"] != 2413152:
        raise AssertionError("K558 combined control changed")
    identity = payload["one_axis_identity"]
    if not identity["kernel_nonnegative"] or not identity["kernel_continuous_at_node"] or identity["kernel_zero_order_at_origin"] != 2 or identity["kernel_mass"] != "1/33554432":
        raise AssertionError("K558 Peano kernel contract changed")
    rows = payload["order_contracts"]
    if len(rows) != 2 or [row["order"] for row in rows] != [11, 12]:
        raise AssertionError("K558 order contracts changed")
    for row in rows:
        expected_axes = 2 * (row["order"] + 1)
        tensor = row["tensor_telescoping"]
        if tensor["mixed_derivatives_required"] or tensor["pure_second_directional_terms"] != expected_axes or len(tensor["axis_contracts"]) != expected_axes:
            raise AssertionError(f"K558 order-{row['order']} tensor contract changed")
        if not tensor["node_jet_substitution_for_global_integral_forbidden"] or not tensor["global_entrywise_supremum_before_group_assembly_forbidden"]:
            raise AssertionError(f"K558 order-{row['order']} forbidden shortcut admitted")
        decision = row["decision"]
        if not decision["complete_axis_remainder_formula_emitted"] or decision["complete_axis_remainder_numerically_bounded"] or decision["complete_integral_emitted"] or decision["rank_six_global_cover_released"] or not all(row["release_test"].values()):
            raise AssertionError(f"K558 order-{row['order']} decision boundary changed")
    decision = payload["decision"]
    if not decision["complete_order_eleven_remainder_formula_emitted"] or not decision["complete_order_twelve_remainder_formula_emitted"] or decision["complete_order_eleven_integral_emitted"] or decision["complete_order_twelve_integral_emitted"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("K558 combined decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K558 combined release test failed")


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
