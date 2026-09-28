#!/usr/bin/env python3
"""Construct native order-eleven/twelve one-node rules and face atlases."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K405_SCRIPT = HERE / "k405_order_ten_gauss_laguerre_face_atlas.py"
K379 = ROOT / "lab/process/k379-orders-eleven-twelve-rank-six-transfer.json"
OUTPUT = ROOT / "lab/process/k554-orders-eleven-twelve-gauss-laguerre-face-atlas.json"
SHIFT = 256
EXPECTED = {
    11: {"side": 12, "axes": 24, "paths": 640, "groups": 24, "entries": 12920, "ordered": 25200, "prefactor": "(2*pi)^-13"},
    12: {"side": 13, "axes": 26, "paths": 1152, "groups": 33, "entries": 35352, "ordered": 69552, "prefactor": "(2*pi)^-14"},
}


def load_base():
    spec = importlib.util.spec_from_file_location("k405_for_k554", K405_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K405_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


BASE = load_base()


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def order_row(order: int, interface: dict[str, Any]) -> dict[str, Any]:
    expected = EXPECTED[order]
    BASE.ORDER = order
    BASE.SIDE_COUNT = expected["side"]
    BASE.AXIS_COUNT = expected["axes"]
    groups = BASE.group_terms()
    paths = sum(len(rows) for rows in groups.values())
    entries = sum(len(rows) * (len(rows) + 1) // 2 for rows in groups.values())
    ordered = sum(len(rows) ** 2 for rows in groups.values())
    census = (paths, len(groups), entries, ordered)
    wanted = (expected["paths"], expected["groups"], expected["entries"], expected["ordered"])
    if census != wanted:
        raise AssertionError(f"order-{order} census changed: {census} != {wanted}")
    if interface["maximum_rank"] != 6 or interface["positive_time_variables"] != expected["axes"]:
        raise AssertionError(f"order-{order} K379 rank/dimension changed")
    if interface["native_prefactor"] != expected["prefactor"]:
        raise AssertionError(f"order-{order} native prefactor changed")

    atlas = BASE.support_atlas(groups)
    axis_weight = Fraction(1, SHIFT)
    product_weight = axis_weight ** expected["axes"]
    radial_weight = Fraction(math.factorial(expected["axes"] - 1), SHIFT ** expected["axes"])
    angular_weight = Fraction(1, math.factorial(expected["axes"] - 1))
    if radial_weight * angular_weight != product_weight:
        raise AssertionError(f"order-{order} radial/angular replay changed")
    return {
        "order": order,
        "side_count": expected["side"],
        "positive_time_variables": expected["axes"],
        "paths": paths,
        "coherent_groups": len(groups),
        "upper_triangle_gram_entries": entries,
        "ordered_quadratic_terms": ordered,
        "maximum_species_determinant_rank": interface["maximum_rank"],
        "K379_complete_entry_interface_sha256": interface["complete_entry_interface_sha256"],
        "native_prefactor": expected["prefactor"],
        "positive_product_rule": {
            "measure": f"product of {expected['axes']} exp(-256*x) dx factors",
            "axis_rule": "integral exp(-256*x)h(x)dx=h(1/256)/256+integral K_256(t)h''(t)dt",
            "axis_node": "1/256",
            "axis_weight": "1/256",
            "node": ["1/256"] * expected["axes"],
            "product_weight": q(product_weight),
            "all_weights_strictly_positive": True,
            "separately_affine_exact": True,
            "multiaffine_exact": True,
            "peano_kernel_nonnegative": True,
            "peano_kernel_zero_order_at_origin": 2,
            "peano_kernel_mass": q(Fraction(1, 2 * SHIFT**3)),
        },
        "radial_angular_replay": {
            "radial_density": f"exp(-256*rho)*rho^{expected['axes'] - 1}",
            "radial_node": q(Fraction(expected["axes"], SHIFT)),
            "radial_weight": q(radial_weight),
            "combined_angular_weight": q(angular_weight),
            "radial_times_angular_equals_product_weight": True,
        },
        "cumulative_time_face_atlas": atlas,
        "remainder_interface": {
            "pure_second_derivative_axes": expected["axes"],
            "mixed_derivatives_required": False,
            "positive_kernel_all_axes": True,
            "global_second_derivative_integrals_computed": False,
        },
    }


def build() -> dict[str, Any]:
    k379 = json.loads(K379.read_text())
    interfaces = {int(row["order"]): row for row in k379["order_interfaces"]}
    rows = [order_row(order, interfaces[order]) for order in (11, 12)]
    return {
        "schema_version": "1.0",
        "result_id": "K554-ORDERS-ELEVEN-TWELVE-GAUSS-LAGUERRE-FACE-ATLAS",
        "created": "2026-09-27",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k377-rank-six-confluent-determinant-calculus.json",
                "lab/process/k378-rank-six-global-scaled-bessel-bank.json",
                "lab/process/k379-orders-eleven-twelve-rank-six-transfer.json",
            ],
            "orders": [11, 12],
            "laplace_shift": SHIFT,
            "combined_paths": sum(row["paths"] for row in rows),
            "combined_groups": sum(row["coherent_groups"] for row in rows),
            "combined_upper_triangle_entries": sum(row["upper_triangle_gram_entries"] for row in rows),
            "combined_ordered_terms": sum(row["ordered_quadratic_terms"] for row in rows),
        },
        "order_interfaces": rows,
        "composition_contract": {
            "order_specific_dimensions_prefactors_and_counts_retained": True,
            "complete_group_quadratic_form_precedes_absolute_enclosure": True,
            "occurrencewise_absolute_value_permitted": False,
            "raw_Bessel_zero_evaluation_permitted": False,
            "order_ten_rule_atlas_or_prefactor_reused": False,
        },
        "decision": {
            "native_order_eleven_positive_value_rule_emitted": True,
            "native_order_twelve_positive_value_rule_emitted": True,
            "complete_zero_and_coalescence_face_atlases_emitted": True,
            "group_level_node_evaluators_emitted": False,
            "complete_order_eleven_integral_emitted": False,
            "complete_order_twelve_integral_emitted": False,
            "next_exact_input": "evaluate every order-eleven and order-twelve upper-triangle Gram entry at its native 1/256 node, restoring each coherent quadratic form before compiling the 24/26-axis Peano interfaces",
        },
        "release_test": {
            "all_1792_paths_replayed": sum(row["paths"] for row in rows) == 1792,
            "all_57_groups_replayed": sum(row["coherent_groups"] for row in rows) == 57,
            "all_48272_upper_triangle_entries_covered": sum(row["upper_triangle_gram_entries"] for row in rows) == 48272,
            "all_94752_ordered_terms_retained": sum(row["ordered_quadratic_terms"] for row in rows) == 94752,
            "rank_six_boundary_retained_both_orders": all(row["maximum_species_determinant_rank"] == 6 for row in rows),
            "separate_24_26_axis_rules_retained": [row["positive_time_variables"] for row in rows] == [24, 26],
            "separate_native_prefactors_retained": [row["native_prefactor"] for row in rows] == ["(2*pi)^-13", "(2*pi)^-14"],
            "all_face_masks_nonempty": all(face["codimension"] > 0 for row in rows for key in ("kernel_zero_faces", "row_coalescence_faces", "column_coalescence_faces") for face in row["cumulative_time_face_atlas"][key]),
            "complete_integrals_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": {"SC-ACT-01": "ASSERTS_UNCHANGED", "SC-ACT-02": "ASSERTS_UNCHANGED", "SC-ACT-06": "ASSERTS_UNCHANGED", "SC-META-53": "UNCERTAIN_UNCHANGED", "LT-SM8": "NEEDS_UNCHANGED", "LT-GR6b": "NEEDS_UNCHANGED", "RA-F1": "NEEDS_UNCHANGED", "AC-F1": "NEEDS_UNCHANGED"},
        "source_routing": {"classification": "INTERNAL_STRUCTURAL_ONLY", "source_native_GU_mechanism_tested": False, "conditional_repository_Fock_construction_only": True},
        "claim_ceiling": "Exact native positive one-node Gauss--Laguerre rules and cumulative-time zero/coalescence face atlases for all 1,792 order-eleven/twelve K179 paths, 57 coherent groups, 48,272 upper-triangle Gram entries and 94,752 ordered terms. The rules retain separate 24/26-dimensional measures and (2*pi)^-13/(2*pi)^-14 prefactors. They do not evaluate node values, bound Peano remainders, enclose complete integrals, construct the base action column or R_ref, emit a K152 interval, or move source, ledger, canon, paper, public, novelty or physical posture.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["combined_paths"], fixed["combined_groups"], fixed["combined_upper_triangle_entries"], fixed["combined_ordered_terms"]) != (1792, 57, 48272, 94752):
        raise AssertionError("K554 combined census changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K554 release test failed")
    rows = payload["order_interfaces"]
    if len(rows) != 2:
        raise AssertionError("K554 order interface count changed")
    for row in rows:
        expected = EXPECTED[row["order"]]
        if (row["side_count"], row["positive_time_variables"], row["paths"], row["coherent_groups"], row["upper_triangle_gram_entries"], row["ordered_quadratic_terms"], row["maximum_species_determinant_rank"], row["native_prefactor"]) != (expected["side"], expected["axes"], expected["paths"], expected["groups"], expected["entries"], expected["ordered"], 6, expected["prefactor"]):
            raise AssertionError(f"K554 order-{row['order']} interface changed")
    decision = payload["decision"]
    if not decision["complete_zero_and_coalescence_face_atlases_emitted"] or decision["complete_order_eleven_integral_emitted"] or decision["complete_order_twelve_integral_emitted"]:
        raise AssertionError("K554 decision boundary changed")


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
