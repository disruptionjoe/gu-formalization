#!/usr/bin/env python3
"""Serialize the four axis-native maps required by K335.

The accepted K334 cover stores independent rational gap boxes.  The Duffy
direction is evaluated through trailing gap sums, which is the simplex-native
formula and remains regular on every accepted box.  The explicit projective
factor is differentiated by exact interval automatic differentiation as one
product, rather than by detached occurrence bounds.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K299 = ROOT / "lab/process/k299-order-seven-positive-peano-simplex-rule.json"
K300 = ROOT / "lab/process/k300-order-seven-angular-method-selection.json"
K305 = ROOT / "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json"
K330 = ROOT / "lab/process/k330-order-seven-radial-tail-control.json"
K331 = ROOT / "lab/process/k331-order-seven-projective-face-homogeneity.json"
K334 = ROOT / "lab/process/k334-order-seven-recursive-global-subdivision.json"
K335 = ROOT / "lab/process/k335-order-seven-gap-axis-transfer.json"
OUTPUT = ROOT / "lab/process/k336-order-seven-axis-native-map-bank.json"

GAPS = ("r0", "r1", "r2", "c0", "c1", "c2")
BASE_GAPS = tuple((Fraction(1, 8), Fraction(5, 24)) for _ in GAPS)
Interval = tuple[Fraction, Fraction]
Jet = tuple[Interval, Interval, Interval]


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def add(left: Interval, right: Interval) -> Interval:
    return left[0] + right[0], left[1] + right[1]


def scale(value: Interval, factor: Fraction) -> Interval:
    candidates = (value[0] * factor, value[1] * factor)
    return min(candidates), max(candidates)


def multiply(left: Interval, right: Interval) -> Interval:
    candidates = (
        left[0] * right[0], left[0] * right[1],
        left[1] * right[0], left[1] * right[1],
    )
    return min(candidates), max(candidates)


def divide_positive(numerator: Interval, denominator: Interval) -> Interval:
    if numerator[0] < 0 or denominator[0] <= 0:
        raise AssertionError("positive interval division precondition failed")
    return numerator[0] / denominator[1], numerator[1] / denominator[0]


def interval_sum(values: list[Interval]) -> Interval:
    result = (Fraction(0), Fraction(0))
    for value in values:
        result = add(result, value)
    return result


def jet_multiply(left: Jet, right: Jet) -> Jet:
    value = multiply(left[0], right[0])
    first = add(multiply(left[1], right[0]), multiply(left[0], right[1]))
    second = interval_sum([
        multiply(left[2], right[0]),
        scale(multiply(left[1], right[1]), Fraction(2)),
        multiply(left[0], right[2]),
    ])
    return value, first, second


def bisect(interval: Interval, bit: int) -> Interval:
    midpoint = (interval[0] + interval[1]) / 2
    return (interval[0], midpoint) if bit == 0 else (midpoint, interval[1])


def leaf_gaps(path: str) -> tuple[Interval, ...]:
    parts = path.split("/")
    if len(parts) == 1:
        return BASE_GAPS
    if len(parts) != 2 or len(parts[1]) != 8 or set(parts[1]) - {"0", "1"}:
        raise AssertionError("invalid K334 leaf path")
    bits = [int(bit) for bit in parts[1]]
    return tuple(bisect(interval, bits[index + 2]) for index, interval in enumerate(BASE_GAPS))


def duffy_direction(gaps: tuple[Interval, ...], axis: int) -> list[Interval]:
    trailing = interval_sum(list(gaps[axis:]))
    next_trailing = interval_sum(list(gaps[axis + 1:]))
    if next_trailing[0] <= 0:
        raise AssertionError("Duffy trailing mass touched zero")
    result: list[Interval] = []
    for index, gap in enumerate(gaps):
        if index < axis:
            result.append((Fraction(0), Fraction(0)))
        elif index == axis:
            result.append(trailing)
        else:
            magnitude = multiply(gap, divide_positive(trailing, next_trailing))
            result.append((-magnitude[1], -magnitude[0]))
    return result


def barycentric_direction(axis: int) -> list[Fraction]:
    leading = Fraction(6 - axis, 6)
    later = -leading / (5 - axis)
    return [Fraction(0) if index < axis else leading if index == axis else later for index in range(6)]


def factor_coefficients() -> list[tuple[str, list[Fraction]]]:
    factors: list[tuple[str, list[Fraction]]] = []

    def add_factor(name: str, entries: dict[int, Fraction], multiplier: Fraction = Fraction(1)) -> None:
        factors.append((name, [multiplier * entries.get(index, Fraction(0)) for index in range(6)]))

    for index, name in enumerate(GAPS):
        add_factor(name, {index: Fraction(1)})
    for side, offset in (("left", 0), ("right", 3)):
        a, b, c = offset, offset + 1, offset + 2
        add_factor(f"V4_{side}_a", {a: Fraction(1)})
        add_factor(f"V4_{side}_b", {b: Fraction(1)})
        add_factor(f"V4_{side}_c", {c: Fraction(1)})
        add_factor(f"V4_{side}_ab", {a: Fraction(1), b: Fraction(1)})
        add_factor(f"V4_{side}_bc", {b: Fraction(1), c: Fraction(1)})
        add_factor(f"V4_{side}_abc", {a: Fraction(1), b: Fraction(1), c: Fraction(1)})
        add_factor(f"V3_{side}_02", {a: Fraction(1), b: Fraction(1)}, Fraction(3, 4))
        add_factor(f"V3_{side}_24", {b: Fraction(1), c: Fraction(1)}, Fraction(3, 4))
        add_factor(f"V3_{side}_sum", {a: Fraction(1), b: Fraction(2), c: Fraction(1)}, Fraction(3, 4))
    if len(factors) != 24:
        raise AssertionError("native projective factor census changed")
    return factors


def linear_interval(coefficients: list[Fraction], values: list[Interval]) -> Interval:
    return interval_sum([scale(value, coefficient) for value, coefficient in zip(values, coefficients, strict=True)])


def projective_jet(gaps: tuple[Interval, ...], direction: list[Interval]) -> Jet:
    result: Jet = ((Fraction(1), Fraction(1)), (Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)))
    for _, coefficients in factor_coefficients():
        factor: Jet = (
            linear_interval(coefficients, list(gaps)),
            linear_interval(coefficients, direction),
            (Fraction(0), Fraction(0)),
        )
        result = jet_multiply(result, factor)
    return result


def node_direction_bank(direction: list[Interval]) -> dict[str, Any]:
    zero = (Fraction(0), Fraction(0))
    unit = (Fraction(1), Fraction(1))
    split = (Fraction(0), Fraction(1))

    def weighted(indices: list[tuple[int, Interval]]) -> Interval:
        return interval_sum([multiply(direction[index], coefficient) for index, coefficient in indices])

    odd_left = [
        weighted([(0, unit), (1, unit), (2, unit)]),
        weighted([(1, unit), (2, unit)]),
        weighted([(2, unit)]),
        zero,
    ]
    odd_right = [
        weighted([(3, unit), (4, unit), (5, unit)]),
        weighted([(4, unit), (5, unit)]),
        weighted([(5, unit)]),
        zero,
    ]
    even_left = [
        weighted([(0, split), (1, unit), (2, unit)]),
        weighted([(1, split), (2, unit)]),
        weighted([(2, split)]),
        zero,
    ]
    even_right = [
        weighted([(3, split), (4, unit), (5, unit)]),
        weighted([(4, split), (5, unit)]),
        weighted([(5, split)]),
        zero,
    ]
    d4 = [[add(left, right) for right in odd_right] for left in odd_left]
    b5: list[list[Interval | None]] = []
    for row in range(5):
        entries: list[Interval | None] = []
        for column in range(5):
            if (row, column) in ((3, 4), (4, 3), (4, 4)):
                entries.append(None)
            elif row < 4 and column < 4:
                entries.append(add(even_left[row], even_right[column]))
            elif row < 4:
                entries.append(even_left[row])
            else:
                entries.append(even_right[column])
        b5.append(entries)
    return {
        "normalization": "multiply every normalized argument direction by b before kernel-chain evaluation",
        "split_coefficient_interval": ["0", "1"],
        "odd_left_node_directions": [interval_row(value) for value in odd_left],
        "odd_right_node_directions": [interval_row(value) for value in odd_right],
        "even_left_node_directions": [interval_row(value) for value in even_left],
        "even_right_node_directions": [interval_row(value) for value in even_right],
        "D4_normalized_argument_direction_matrix": [[interval_row(value) for value in row] for row in d4],
        "bordered_B5_normalized_argument_direction_matrix": [
            [None if value is None else interval_row(value) for value in row] for row in b5
        ],
    }


def interval_row(value: Interval) -> list[str]:
    return [q(value[0]), q(value[1])]


def abs_upper(value: Interval) -> Fraction:
    return max(abs(value[0]), abs(value[1]))


def class_id(gaps: tuple[Interval, ...]) -> str:
    encoded = json.dumps([[q(a), q(b)] for a, b in gaps], separators=(",", ":")).encode()
    return "gap-class-" + hashlib.sha256(encoded).hexdigest()[:12]


def slot_maps() -> dict[str, Any]:
    d4 = []
    for row in range(4):
        d4.append([
            {
                "base_kernel_derivative_order": row + column,
                "axis_jet_kernel_derivative_orders": [row + column + order for order in range(3)],
            }
            for column in range(4)
        ])
    base_orders = [0, 1, 2, 0]
    b5 = []
    for row in range(5):
        entries = []
        for column in range(5):
            if (row, column) in ((3, 4), (4, 3), (4, 4)):
                entries.append({"literal_zero": True, "axis_jet_kernel_derivative_orders": []})
            else:
                row_order = base_orders[row] if row < 4 else 0
                column_order = base_orders[column] if column < 4 else 0
                base = row_order + column_order
                entries.append({
                    "literal_zero": False,
                    "base_kernel_derivative_order": base,
                    "axis_jet_kernel_derivative_orders": [base + order for order in range(3)],
                })
        b5.append(entries)
    return {
        "D4": d4,
        "bordered_B5": b5,
        "D4_maximum_kernel_derivative_order": max(
            max(entry["axis_jet_kernel_derivative_orders"]) for row in d4 for entry in row
        ),
        "bordered_B5_maximum_kernel_derivative_order": max(
            max(entry["axis_jet_kernel_derivative_orders"] or [0]) for row in b5 for entry in row
        ),
        "column_replacement_rule": "for coefficient order q, assemble the shared entry q-jets first and apply the complete determinant Taylor coefficient; retain both first-first replacements with factor two at q=2",
        "literal_zero_slots": [[3, 4], [4, 3], [4, 4]],
    }


def build() -> dict[str, Any]:
    k299 = json.loads(K299.read_text())
    k300 = json.loads(K300.read_text())
    k305 = json.loads(K305.read_text())
    k330 = json.loads(K330.read_text())
    k331 = json.loads(K331.read_text())
    k334 = json.loads(K334.read_text())
    k335 = json.loads(K335.read_text())
    cover = k334["recursive_cover"]
    if cover["coverage_checksum"] != "sha256:2df52de1d9beca3aaf6ea730416f7251e79cf8b1da260c214e27d2e3b5996016":
        raise AssertionError("K334 accepted cover changed")
    if len(k335["numerical_transfer_gate"]["missing_executable_fields"]) != 4:
        raise AssertionError("K335 transfer gate changed")

    unique: dict[str, tuple[Interval, ...]] = {}
    leaf_map = []
    for leaf in cover["finite_leaves"]:
        gaps = leaf_gaps(leaf["path"])
        identifier = class_id(gaps)
        unique[identifier] = gaps
        leaf_map.append({"path": leaf["path"], "gap_class": identifier})

    classes = []
    for identifier, gaps in sorted(unique.items()):
        axes = []
        for axis in range(5):
            direction = duffy_direction(gaps, axis)
            polynomial = projective_jet(gaps, direction)
            axes.append({
                "axis": f"t{axis}",
                "dp_dt_interval": [interval_row(value) for value in direction],
                "d2p_dt2_exact": ["0"] * 6,
                "sum_dp_dt_exact": "0",
                "barycentric_control": [q(value) for value in barycentric_direction(axis)],
                "shared_entry_normalized_argument_directions": node_direction_bank(direction),
                "native_projective_polynomial_value_first_second_intervals": [interval_row(value) for value in polynomial],
                "native_projective_polynomial_value_first_second_abs_uppers": [q(abs_upper(value)) for value in polynomial],
            })
        classes.append({
            "class_id": identifier,
            "gap_intervals": [interval_row(value) for value in gaps],
            "axes": axes,
        })

    slots = slot_maps()
    face_rows = k300["face_transfer"]["projective_face_second_derivative_margins"]
    tail_powers = k330["polynomial_growth_ledger"]["tail_integrand_value_first_second_powers"]
    return {
        "schema_version": "1.0",
        "result_id": "K336-ORDER-SEVEN-AXIS-NATIVE-MAP-BANK",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k299-order-seven-positive-peano-simplex-rule.json",
                "lab/process/k300-order-seven-angular-method-selection.json",
                "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json",
                "lab/process/k330-order-seven-radial-tail-control.json",
                "lab/process/k331-order-seven-projective-face-homogeneity.json",
                "lab/process/k334-order-seven-recursive-global-subdivision.json",
                "lab/process/k335-order-seven-gap-axis-transfer.json",
            ],
            "gap_order": list(GAPS),
            "gap_axes": [f"t{axis}" for axis in range(5)],
            "accepted_subdivision_checksum": cover["coverage_checksum"],
            "accepted_finite_leaf_count": cover["finite_leaf_count"],
            "unique_gap_box_class_count": len(classes),
            "native_projective_linear_factor_count": len(factor_coefficients()),
        },
        "leaf_class_map": leaf_map,
        "axis_native_gap_classes": classes,
        "shared_entry_directional_jet_map": slots,
        "face_tail_degree_ledger": {
            "projective_one_gap_face_count": sum(row["codimension"] == 1 for row in face_rows),
            "projective_codimension_two_face_count": sum(row["codimension"] == 2 for row in face_rows),
            "worst_gap_face_second_derivative_integrability_margin": min(row["second_derivative_integrability_margin"] for row in face_rows),
            "s0_complete_product_pole_orders_value_first_second": k331["s0_face"]["complete_product_worst_pole_orders_value_first_second"],
            "s0_remaining_integrated_powers_value_first_second": k331["s0_face"]["remaining_integrated_powers_value_first_second"],
            "s1_complete_product_pole_orders_value_first_second": k331["s1_face"]["complete_product_worst_pole_orders_value_first_second"],
            "s1_remaining_integrated_powers_value_first_second": k331["s1_face"]["remaining_integrated_powers_value_first_second"],
            "radial_normalized_complete_powers_value_first_second": k330["polynomial_growth_ledger"]["complete_coefficient_value_first_second_powers"],
            "radial_tail_integrand_powers_value_first_second": tail_powers,
            "gap_derivative_reason": "dimensionless affine Duffy motion distributes total derivative order q between D4 and bordered B5; each kernel chain factor contributes one radial power, so every product term retains the common 29+q normalized degree and 35+q tail power",
            "projective_preconditioning_precedes_interval_substitution": True,
        },
        "map_release": {
            "exact_affine_duffy_derivative_vectors_serialized": True,
            "native_projective_polynomial_value_first_second_intervals_serialized": True,
            "shared_entry_D4_and_bordered_B5_directional_jet_slots_serialized": True,
            "projective_face_and_radial_tail_degree_ledger_serialized": True,
            "all_K335_missing_map_classes_serialized": True,
            "K305_group_axis_order_master_count": k305["template_compression"]["new_group_axis_order_master_functionals"],
            "K299_peano_masses": {
                row["axis"]: row["peano_kernel"]["integral"]
                for row in k299["one_dimensional_factors"] if row["axis"] != "y"
            },
        },
        "decision": {
            "axis_native_numeric_map_bank_complete": True,
            "first_complete_gap_axis_leaf_evaluation_released": True,
            "complete_gap_axis_constants_emitted": False,
            "complete_six_axis_peano_norm_emitted": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "substitute K336's leaf-class direction and polynomial jets into the zero-safe shared-entry interval evaluator, assemble each K305 determinant coefficient before enclosure, and evaluate the first complete t0 leaf bank before extending the same engine to t1--t4",
        },
        "release_test": {
            "every_K334_finite_leaf_mapped_once": len(leaf_map) == cover["finite_leaf_count"] == len({row["path"] for row in leaf_map}),
            "all_five_axes_present_on_every_gap_class": all([row["axis"] for row in item["axes"]] == ["t0", "t1", "t2", "t3", "t4"] for item in classes),
            "all_second_chart_derivatives_exact_zero": all(all(value == "0" for value in row["d2p_dt2_exact"]) for item in classes for row in item["axes"]),
            "barycentric_direction_sums_zero": all(sum(Fraction(value) for value in row["barycentric_control"]) == 0 for item in classes for row in item["axes"]),
            "D4_order_eight_replayed": slots["D4_maximum_kernel_derivative_order"] == 8,
            "bordered_B5_order_six_replayed": slots["bordered_B5_maximum_kernel_derivative_order"] == 6,
            "tail_powers_replayed": tail_powers == [35, 36, 37],
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k335["ledger_effect"],
        "source_routing": k335["source_routing"],
        "claim_ceiling": "Exact rational axis-native map bank for all five K299 Duffy axes on every accepted K334 finite leaf, compressed into repeated gap-box classes. It serializes the affine gap directions, complete native projective-polynomial value/first/second intervals, shared-entry D4 and bordered-B5 directional jet slots through kernel orders eight and six, and the projective-face/radial-tail degree ledger. This releases complete determinant leaf evaluation but does not itself emit a gap-axis constant, six-axis Peano norm, K294 gamma join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["accepted_subdivision_checksum"] != "sha256:2df52de1d9beca3aaf6ea730416f7251e79cf8b1da260c214e27d2e3b5996016":
        raise AssertionError("K334 checksum changed")
    if fixed["accepted_finite_leaf_count"] != len(payload["leaf_class_map"]):
        raise AssertionError("leaf map incomplete")
    if fixed["unique_gap_box_class_count"] != len(payload["axis_native_gap_classes"]):
        raise AssertionError("gap class census changed")
    if len({row["path"] for row in payload["leaf_class_map"]}) != fixed["accepted_finite_leaf_count"]:
        raise AssertionError("leaf identity duplicate")
    class_ids = {row["class_id"] for row in payload["axis_native_gap_classes"]}
    if {row["gap_class"] for row in payload["leaf_class_map"]} != class_ids:
        raise AssertionError("leaf-to-gap-class map does not close")
    for item in payload["axis_native_gap_classes"]:
        if [row["axis"] for row in item["axes"]] != ["t0", "t1", "t2", "t3", "t4"]:
            raise AssertionError("gap axis census changed")
        for row in item["axes"]:
            if row["sum_dp_dt_exact"] != "0" or row["d2p_dt2_exact"] != ["0"] * 6:
                raise AssertionError("affine Duffy contract changed")
            if len(row["native_projective_polynomial_value_first_second_intervals"]) != 3:
                raise AssertionError("projective jet order changed")
            entry_map = row["shared_entry_normalized_argument_directions"]
            if len(entry_map["D4_normalized_argument_direction_matrix"]) != 4 or any(len(matrix_row) != 4 for matrix_row in entry_map["D4_normalized_argument_direction_matrix"]):
                raise AssertionError("D4 argument-direction map changed")
            if len(entry_map["bordered_B5_normalized_argument_direction_matrix"]) != 5 or any(len(matrix_row) != 5 for matrix_row in entry_map["bordered_B5_normalized_argument_direction_matrix"]):
                raise AssertionError("bordered B5 argument-direction map changed")
            if [[r, c] for r in range(5) for c in range(5) if entry_map["bordered_B5_normalized_argument_direction_matrix"][r][c] is None] != [[3, 4], [4, 3], [4, 4]]:
                raise AssertionError("bordered B5 literal-zero direction map changed")
            if any(Fraction(value) < 0 for value in row["native_projective_polynomial_value_first_second_abs_uppers"]):
                raise AssertionError("projective absolute upper invalid")
    slots = payload["shared_entry_directional_jet_map"]
    if slots["D4_maximum_kernel_derivative_order"] != 8 or slots["bordered_B5_maximum_kernel_derivative_order"] != 6:
        raise AssertionError("kernel derivative order changed")
    if slots["literal_zero_slots"] != [[3, 4], [4, 3], [4, 4]]:
        raise AssertionError("literal border zeros changed")
    ledger = payload["face_tail_degree_ledger"]
    if ledger["worst_gap_face_second_derivative_integrability_margin"] != 1:
        raise AssertionError("projective gap face margin changed")
    if ledger["radial_tail_integrand_powers_value_first_second"] != [35, 36, 37]:
        raise AssertionError("radial tail degree changed")
    if not all(payload["map_release"][key] for key in (
        "exact_affine_duffy_derivative_vectors_serialized",
        "native_projective_polynomial_value_first_second_intervals_serialized",
        "shared_entry_D4_and_bordered_B5_directional_jet_slots_serialized",
        "projective_face_and_radial_tail_degree_ledger_serialized",
        "all_K335_missing_map_classes_serialized",
    )):
        raise AssertionError("K335 map release incomplete")
    decision = payload["decision"]
    if decision["complete_gap_axis_constants_emitted"] or decision["complete_six_axis_peano_norm_emitted"] or decision["k294_gamma_join_released"]:
        raise AssertionError("downstream numerical result overclaimed")


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
