#!/usr/bin/env python3
"""Freeze the exact tensor Peano contract consumed after K407--K408."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
K405 = ROOT / "lab/process/k405-order-ten-gauss-laguerre-face-atlas.json"
K407 = ROOT / "lab/process/k407-order-ten-axis-jet-compiler.json"
K408 = ROOT / "lab/process/k408-order-ten-node-directional-jet-bank.json"
OUTPUT = ROOT / "lab/process/k409-order-ten-positive-peano-contract.json"

SHIFT = 256
AXES = tuple([f"s{i}" for i in range(1, 12)] + [f"v{i}" for i in range(1, 12)])


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict:
    k405 = json.loads(K405.read_text())
    k407 = json.loads(K407.read_text())
    k408 = json.loads(K408.read_text())
    kernel_mass = Fraction(1, 2 * SHIFT**3)
    node_weight = Fraction(1, SHIFT)
    rows = []
    local_rows = {row["axis"]: row for row in k408["axis_node_jets"]}
    for index, axis in enumerate(AXES):
        rows.append(
            {
                "axis": axis,
                "preceding_axes_fixed_at_node": index,
                "following_axes_integrated_exactly": len(AXES) - index - 1,
                "preceding_node_weight": q(node_weight**index),
                "peano_kernel_mass": q(kernel_mass),
                "hybrid_global_integrand": f"abs(partial_{axis}^2 H) with {index} preceding raw times at 1/256, {axis}=t against K_256(t), and {21-index} following raw times under exp(-256*x) dx",
                "local_node_second_derivative_lower_control": local_rows[axis]["raw_second_derivative_lower"],
                "local_node_second_derivative_upper_control": local_rows[axis]["raw_second_derivative_upper"],
                "local_control_is_not_a_global_bound": True,
            }
        )
    return {
        "schema_version": "1.0",
        "result_id": "K409-ORDER-TEN-POSITIVE-PEANO-CONTRACT",
        "created": "2026-09-24",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k405-order-ten-gauss-laguerre-face-atlas.json",
                "lab/process/k407-order-ten-axis-jet-compiler.json",
                "lab/process/k408-order-ten-node-directional-jet-bank.json",
            ],
            "native_axes": list(AXES),
            "axis_node": "1/256",
            "axis_weight": "1/256",
            "product_weight": k405["positive_product_gauss_laguerre_rule"]["product_weight"],
            "K405_face_atlas_sha256": k405["cumulative_time_face_atlas"]["atlas_sha256"],
            "K407_compiled_entry_interface_sha256": k407["compiled_entry_interface"]["sha256"],
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
        "tensor_telescoping": {
            "identity": "I^22-Q^22=sum_{a=1}^{22} Q^{a-1} tensor (I-Q)_a tensor I^{22-a}",
            "mixed_derivatives_required": False,
            "pure_second_directional_terms": 22,
            "axis_contracts": rows,
            "absolute_remainder_bound_requires": "one zero-safe whole-domain integral of each listed complete coherent pure-second functional",
            "node_jet_substitution_for_global_integral_forbidden": True,
            "global_entrywise_supremum_before_group_assembly_forbidden": True,
        },
        "decision": {
            "complete_twenty_two_axis_remainder_formula_emitted": True,
            "complete_twenty_two_axis_remainder_numerically_bounded": False,
            "complete_order_ten_integral_emitted": False,
            "rank_five_order_ten_global_cover_released": False,
            "next_required_object": "zero-safe whole-orthant determinant-preserving interval atlas for the twenty-two K407 pure-second coherent functionals",
        },
        "release_test": {
            "all_22_axis_contracts_present": len(rows) == 22,
            "preceding_and_following_counts_partition_21": all(row["preceding_axes_fixed_at_node"] + row["following_axes_integrated_exactly"] == 21 for row in rows),
            "positive_kernel_mass_exact": q(kernel_mass) == "1/33554432",
            "only_pure_second_derivatives_required": True,
            "node_controls_not_promoted": all(row["local_control_is_not_a_global_bound"] for row in rows),
            "complete_order_ten_integral_not_overclaimed": True,
        },
        "ledger_effect": k408["ledger_effect"],
        "source_routing": k408["source_routing"],
        "claim_ceiling": "Exact positive Peano-kernel and tensor-telescoping contract for the native twenty-two-axis order-ten rule. It identifies the twenty-two complete coherent pure-second hybrid integrals, their exact node/integration ordering and kernel mass 1/33554432, and forbids substituting K408's local node jets for global bounds. It emits no numerical remainder, complete order-ten integral, action column, R_ref residual, K152 interval, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict) -> None:
    fixed = payload["fixed_control"]
    if fixed["native_axes"] != list(AXES) or fixed["axis_node"] != "1/256" or fixed["axis_weight"] != "1/256":
        raise AssertionError("K409 native rule changed")
    identity = payload["one_axis_identity"]
    if not identity["kernel_nonnegative"] or not identity["kernel_continuous_at_node"] or identity["kernel_zero_order_at_origin"] != 2 or identity["kernel_mass"] != "1/33554432":
        raise AssertionError("K409 Peano kernel contract changed")
    tensor = payload["tensor_telescoping"]
    if tensor["mixed_derivatives_required"] or tensor["pure_second_directional_terms"] != 22 or len(tensor["axis_contracts"]) != 22:
        raise AssertionError("K409 tensor contract changed")
    if not tensor["node_jet_substitution_for_global_integral_forbidden"] or not tensor["global_entrywise_supremum_before_group_assembly_forbidden"]:
        raise AssertionError("K409 forbidden shortcut admitted")
    decision = payload["decision"]
    if not decision["complete_twenty_two_axis_remainder_formula_emitted"] or decision["complete_twenty_two_axis_remainder_numerically_bounded"] or decision["complete_order_ten_integral_emitted"] or decision["rank_five_order_ten_global_cover_released"]:
        raise AssertionError("K409 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K409 release test failed")


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
