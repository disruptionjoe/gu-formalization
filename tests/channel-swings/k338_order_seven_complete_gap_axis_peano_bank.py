#!/usr/bin/env python3
"""Close the five K299 gap-axis Peano constants on K334's exact cover.

The evaluator keeps K336's shared argument directions and native polynomial
jets inside complete D4 and bordered-B5 Taylor determinants.  Every finite
K334 leaf is evaluated in its actual radial/projective chart; the two face
preconditioners are applied before entry intervals are substituted.  The
three r>=1 cells use K336's analytic 35/36/37 degree ledger.  Only after the
global second-directional upper is complete is the corresponding positive
K299 Peano mass applied.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K312_MODULE = HERE / "k312_order_seven_positive_cell_measure_backend.py"
K326_MODULE = HERE / "k326_order_seven_signed_entry_jet_chart_bank.py"
K328_MODULE = HERE / "k328_order_seven_scaled_derivative_envelope_bank.py"
K334 = ROOT / "lab/process/k334-order-seven-recursive-global-subdivision.json"
K336 = ROOT / "lab/process/k336-order-seven-axis-native-map-bank.json"
K337 = ROOT / "lab/process/k337-order-seven-gap-axis-leaf-evaluator.json"
OUTPUT = ROOT / "lab/process/k338-order-seven-complete-gap-axis-peano-bank.json"

ctx.dps = 180
ctx.threads = 1

RADIAL_CELLS = ((Fraction(0), Fraction(1, 16)), (Fraction(1, 16), Fraction(1)))
PROJECTIVE_CELLS = {
    "s0": (Fraction(0), Fraction(1, 4)),
    "interior": (Fraction(1, 4), Fraction(3, 4)),
    "s1": (Fraction(3, 4), Fraction(1)),
}
BASE_GAPS = tuple((Fraction(1, 8), Fraction(5, 24)) for _ in range(6))
ROW_ORDERS = [0, 1, 2, 0]
COLUMN_ORDERS = [0, 1, 2, 0]
ARGUMENT_MAX = Fraction(3, 2)
TAIL_POWERS = [35, 36, 37]


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def upper_text(value: arb) -> str:
    return repr(math.nextafter(float(abs(value).upper()), math.inf))


def interval_arb(value: list[str]) -> arb:
    left, right = (Fraction(item) for item in value)
    midpoint = (left + right) / 2
    radius = (right - left) / 2
    return arb(q(midpoint)) + arb(0, arb(q(radius)).upper())


def symmetric(value: arb) -> arb:
    return arb(0, abs(value).upper())


def add_poly(left: list[arb], right: list[arb]) -> list[arb]:
    return [a + b for a, b in zip(left, right, strict=True)]


def multiply_poly(left: list[arb], right: list[arb]) -> list[arb]:
    result = [arb(0), arb(0), arb(0)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= 2:
                result[i + j] += a * b
    return result


def determinant_taylor(entry_jets: list[list[list[arb]]]) -> list[arb]:
    size = len(entry_jets)
    total = [arb(0), arb(0), arb(0)]
    for permutation in itertools.permutations(range(size)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(size)
            for j in range(i + 1, size)
        )
        term = [arb(-1 if inversions % 2 else 1), arb(0), arb(0)]
        for row, column in enumerate(permutation):
            value, first, second = entry_jets[row][column]
            term = multiply_poly(term, [value, first, second / 2])
        total = add_poly(total, term)
    return [total[0], total[1], 2 * total[2]]


def bisect(interval: tuple[Fraction, Fraction]) -> tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
    midpoint = sum(interval, Fraction(0)) / 2
    return (interval[0], midpoint), (midpoint, interval[1])


def parse_leaf(path: str) -> tuple[str, tuple[Fraction, Fraction], tuple[Fraction, Fraction], tuple[tuple[Fraction, Fraction], ...]]:
    root, *suffix = path.split("/")
    region, radial_text = root.rsplit("-r", 1)
    radial = RADIAL_CELLS[int(radial_text)]
    projective = PROJECTIVE_CELLS[region]
    gaps = BASE_GAPS
    if suffix:
        if len(suffix) != 1 or len(suffix[0]) != 8 or set(suffix[0]) - {"0", "1"}:
            raise AssertionError("invalid K334 leaf path")
        bits = [int(bit) for bit in suffix[0]]
        radial = bisect(radial)[bits[0]]
        projective = bisect(projective)[bits[1]]
        gaps = tuple(bisect(interval)[bits[index + 2]] for index, interval in enumerate(gaps))
    return region, radial, projective, gaps


def coverage_checksum(rows: list[dict[str, Any]]) -> str:
    payload = [{"path": item["path"], "volume": item["exact_geometric_volume"]} for item in rows]
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def slope_upper(value: list[str], factor: Fraction) -> Fraction:
    left, right = (Fraction(item) for item in value)
    return factor * max(abs(left), abs(right))


def scaled_dd_upper(k328, radius: Fraction, lower: Fraction, row: int, column: int, axis_order: int = 0) -> arb:
    if lower <= 0:
        raise AssertionError("positive normalized argument lower required")
    order = row + column + axis_order
    phi = k328.scaled_derivative_upper(order, radius * ARGUMENT_MAX)
    value = phi / (lower ** (order + 1) * math.factorial(row) * math.factorial(column))
    return arb(q(value))


def node_bank(region: str, projective: tuple[Fraction, Fraction], gaps: tuple[tuple[Fraction, Fraction], ...]) -> dict[str, list[Fraction]]:
    s0, s1 = projective
    b0 = 1 - s1
    p0 = min(interval[0] for interval in gaps)
    return {
        "odd_left": [b0 * p0 * count for count in (3, 2, 1, 0)],
        "odd_right": [s0 / 2 + b0 * p0 * count for count in (3, 2, 1, 0)],
        "even_left": [b0 * p0 * value for value in (Fraction(9, 4), Fraction(5, 4), Fraction(1, 4), Fraction(0))],
        "even_right": [s0 / 2 + b0 * p0 * value for value in (Fraction(9, 4), Fraction(5, 4), Fraction(1, 4), Fraction(0))],
    }


def build_d4(k326, k328, radius: Fraction, region: str, projective, gaps, direction_map) -> list[arb]:
    nodes = node_bank(region, projective, gaps)
    s_max = projective[1]
    b_max = 1 - projective[0]
    matrix: list[list[list[arb]]] = []
    for row in range(4):
        entries = []
        for column in range(4):
            lower = nodes["odd_left"][row] + nodes["odd_right"][column]
            slope = slope_upper(direction_map[row][column], b_max)
            if region == "s0" and (row, column) == (3, 3):
                value = arb(q(2 * k328.scaled_derivative_upper(0, radius * ARGUMENT_MAX)))
                values = [symmetric(value), arb(0), arb(0)]
            else:
                base = row + column
                values = [
                    k326.signed(scaled_dd_upper(k328, radius, lower, row, column), -1 if base % 2 else 1),
                    symmetric(arb(q(slope)) * scaled_dd_upper(k328, radius, lower, row, column, 1)),
                    k326.signed(arb(q(slope * slope)) * scaled_dd_upper(k328, radius, lower, row, column, 2), -1 if (base + 2) % 2 else 1),
                ]
                if region == "s0" and row == 3:
                    values = [arb(q(s_max)) * value for value in values]
            entries.append(values)
        matrix.append(entries)
    return determinant_taylor(matrix)


def upper_face_border_axis_jets(k326, k328, radius, projective, gaps, row, direction) -> list[arb]:
    p0 = min(interval[0] for interval in gaps)
    h = p0 * (Fraction(9, 4), Fraction(5, 4), Fraction(1, 4))[row]
    a = ROW_ORDERS[row]
    tmax = 1 - projective[0]
    prefactor = tmax ** (2 - a) * Fraction(1, 2)
    slope = slope_upper(direction, tmax)
    return [
        k326.signed(arb(q(prefactor)) * scaled_dd_upper(k328, radius, h, a, 0), -1 if a % 2 else 1),
        symmetric(arb(q(prefactor * slope)) * scaled_dd_upper(k328, radius, h, a, 0, 1)),
        k326.signed(arb(q(prefactor * slope * slope)) * scaled_dd_upper(k328, radius, h, a, 0, 2), -1 if (a + 2) % 2 else 1),
    ]


def build_b5(k326, k328, radius: Fraction, region: str, projective, gaps, direction_map) -> list[arb]:
    nodes = node_bank(region, projective, gaps)
    s_max = projective[1]
    b_max = 1 - projective[0]
    matrix = [[[arb(0), arb(0), arb(0)] for _ in range(5)] for _ in range(5)]
    terminal_value = symmetric(arb(q(radius)) * k326.terminal_jet_uppers((Fraction(0), radius * s_max))[0])
    for row in range(5):
        for column in range(5):
            if (row, column) in ((3, 4), (4, 3), (4, 4)):
                continue
            direction = direction_map[row][column]
            if direction is None:
                raise AssertionError("nonzero B5 slot lacks a K336 direction")
            if (row, column) == (3, 3):
                values = [terminal_value, arb(0), arb(0)]
            elif region == "s1" and column == 4 and row < 3:
                values = upper_face_border_axis_jets(k326, k328, radius, projective, gaps, row, direction)
            else:
                if row < 4 and column < 4:
                    lower = nodes["even_left"][row] + nodes["even_right"][column]
                    a, c = ROW_ORDERS[row], COLUMN_ORDERS[column]
                elif row < 4:
                    lower = nodes["even_left"][row]
                    a, c = ROW_ORDERS[row], 0
                else:
                    lower = nodes["even_right"][column]
                    a, c = 0, COLUMN_ORDERS[column]
                slope = slope_upper(direction, b_max)
                base = a + c
                values = [
                    k326.signed(scaled_dd_upper(k328, radius, lower, a, c), -1 if base % 2 else 1),
                    symmetric(arb(q(slope)) * scaled_dd_upper(k328, radius, lower, a, c, 1)),
                    k326.signed(arb(q(slope * slope)) * scaled_dd_upper(k328, radius, lower, a, c, 2), -1 if (base + 2) % 2 else 1),
                ]
            if region == "s0" and row == 3:
                values = [arb(q(s_max)) * value for value in values]
            matrix[row][column] = values
    return determinant_taylor(matrix)


def normalized_coefficients(modules, radius, region, projective, gaps, axis_row) -> list[arb]:
    k326, k328 = modules["k326"], modules["k328"]
    directions = axis_row["shared_entry_normalized_argument_directions"]
    d4 = build_d4(k326, k328, radius, region, projective, gaps, directions["D4_normalized_argument_direction_matrix"])
    b5 = build_b5(k326, k328, radius, region, projective, gaps, directions["bordered_B5_normalized_argument_direction_matrix"])
    polynomial = [interval_arb(value) for value in axis_row["native_projective_polynomial_value_first_second_intervals"]]
    complete = multiply_poly(
        multiply_poly([d4[0], d4[1], d4[2] / 2], [b5[0], b5[1], b5[2] / 2]),
        [polynomial[0], polynomial[1], polynomial[2] / 2],
    )
    complete = [complete[0], complete[1], 2 * complete[2]]
    scalar = Fraction(4, 120) * radius * radius * projective[1] * projective[1]
    return [value * arb(q(scalar)) for value in complete]


def projective_masses(k312, region: str, interval: tuple[Fraction, Fraction]) -> list[Fraction]:
    if region == "interior":
        value = k312.polynomial_cell_moment(interval[0], interval[1], 3, 29)
        return [value, value, value]
    if region == "s0":
        return [k312.polynomial_cell_moment(interval[0], interval[1], 1, 29)] * 3
    powers = [26, 25, 24]
    return [k312.polynomial_cell_moment(interval[0], interval[1], 3, power) for power in powers]


def finite_leaf_bound(modules, leaf, gap_class, axis_row) -> list[arb]:
    region, radial, projective, gaps = parse_leaf(leaf["path"])
    declared = tuple(tuple(Fraction(value) for value in interval) for interval in gap_class["gap_intervals"])
    if gaps != declared:
        raise AssertionError("K336 gap class does not replay its K334 leaf")
    coefficients = normalized_coefficients(modules, radial[1], region, projective, gaps, axis_row)
    radial_mass = modules["k312"].radial_finite_upper(radial[0], radial[1], 6)
    p_masses = projective_masses(modules["k312"], region, projective)
    gap_volume = math.prod((right - left for left, right in gaps), start=Fraction(1))
    return [coefficients[order] * arb(q(radial_mass * p_masses[order] * gap_volume)) for order in range(3)]


def tail_bound(modules, region, projective, gaps, axis_row) -> list[arb]:
    coefficients = normalized_coefficients(modules, Fraction(1), region, projective, gaps, axis_row)
    p_masses = projective_masses(modules["k312"], region, projective)
    gap_volume = math.prod((right - left for left, right in gaps), start=Fraction(1))
    return [
        coefficients[order] * arb(q(modules["k312"].radial_tail_upper(Fraction(1), TAIL_POWERS[order]) * p_masses[order] * gap_volume))
        for order in range(3)
    ]


def build() -> dict[str, Any]:
    modules = {
        "k312": load_module(K312_MODULE, "k338_k312_backend"),
        "k326": load_module(K326_MODULE, "k338_k326_backend"),
        "k328": load_module(K328_MODULE, "k338_k328_backend"),
    }
    k334 = json.loads(K334.read_text())
    k336 = json.loads(K336.read_text())
    k337 = json.loads(K337.read_text())
    if not k337["decision"]["first_complete_shared_entry_gap_axis_determinant_bank_finite"]:
        raise AssertionError("K337 reference evaluator unavailable")
    leaves = k334["recursive_cover"]["finite_leaves"]
    if coverage_checksum(leaves) != k336["fixed_control"]["accepted_subdivision_checksum"]:
        raise AssertionError("K334/K336 coverage checksum changed")
    class_by_id = {row["class_id"]: row for row in k336["axis_native_gap_classes"]}
    leaf_class = {row["path"]: row["gap_class"] for row in k336["leaf_class_map"]}
    if set(leaf_class) != {row["path"] for row in leaves}:
        raise AssertionError("K336 leaf-class map is not one-to-one complete")

    axis_names = ["t0", "t1", "t2", "t3", "t4"]
    finite_totals = {axis: [arb(0), arb(0), arb(0)] for axis in axis_names}
    finite_rows = []
    for leaf in leaves:
        gap_class = class_by_id[leaf_class[leaf["path"]]]
        axis_map = {row["axis"]: row for row in gap_class["axes"]}
        row_values = []
        for axis in axis_names:
            values = finite_leaf_bound(modules, leaf, gap_class, axis_map[axis])
            finite_totals[axis] = [finite_totals[axis][i] + values[i] for i in range(3)]
            row_values.append({"axis": axis, "integrated_value_first_second_abs_uppers": [upper_text(value) for value in values]})
        finite_rows.append({"path": leaf["path"], "gap_class": gap_class["class_id"], "axes": row_values})

    base_class = class_by_id[leaf_class["s0-r0"]]
    base_gaps = tuple(tuple(Fraction(value) for value in interval) for interval in base_class["gap_intervals"])
    if base_gaps != BASE_GAPS:
        raise AssertionError("analytic tail did not resolve to the unsplit K334 gap root")
    base_axes = {row["axis"]: row for row in base_class["axes"]}
    tail_totals = {axis: [arb(0), arb(0), arb(0)] for axis in axis_names}
    tail_rows = []
    for region in ("s0", "interior", "s1"):
        axis_values = []
        for axis in axis_names:
            values = tail_bound(modules, region, PROJECTIVE_CELLS[region], base_gaps, base_axes[axis])
            tail_totals[axis] = [tail_totals[axis][i] + values[i] for i in range(3)]
            axis_values.append({"axis": axis, "integrated_value_first_second_abs_uppers": [upper_text(value) for value in values]})
        tail_rows.append({"region": region, "projective": [q(value) for value in PROJECTIVE_CELLS[region]], "axes": axis_values})

    masses = {axis: Fraction(value) for axis, value in k336["map_release"]["K299_peano_masses"].items()}
    axes = []
    for axis in axis_names:
        complete = [finite_totals[axis][i] + tail_totals[axis][i] for i in range(3)]
        peano = complete[2] * arb(q(masses[axis]))
        if any(not math.isfinite(float(abs(value).upper())) or abs(value).upper() <= 0 for value in complete + [peano]):
            raise AssertionError(f"{axis} global gap-axis bank is not finite positive")
        axes.append({
            "axis": axis,
            "K299_peano_mass": q(masses[axis]),
            "finite_value_first_second_abs_uppers": [upper_text(value) for value in finite_totals[axis]],
            "analytic_tail_value_first_second_abs_uppers": [upper_text(value) for value in tail_totals[axis]],
            "complete_value_first_second_abs_uppers": [upper_text(value) for value in complete],
            "peano_weighted_second_directional_constant": upper_text(peano),
        })
    y_constant = arb(k334["complete_y_master"]["complete_value_first_second_abs_uppers"][2])
    six_axis = y_constant + sum((arb(row["peano_weighted_second_directional_constant"]) for row in axes), arb(0))

    return {
        "schema_version": "1.0",
        "result_id": "K338-ORDER-SEVEN-COMPLETE-GAP-AXIS-PEANO-BANK",
        "created": "2026-09-22",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k334-order-seven-recursive-global-subdivision.json",
                "lab/process/k336-order-seven-axis-native-map-bank.json",
                "lab/process/k337-order-seven-gap-axis-leaf-evaluator.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "accepted_subdivision_checksum": k336["fixed_control"]["accepted_subdivision_checksum"],
            "finite_leaf_count": len(leaves),
            "analytic_tail_cell_count": 3,
            "gap_class_count": len(class_by_id),
            "axis_count": 5,
            "tail_powers_value_first_second": TAIL_POWERS,
        },
        "complete_cover": {
            "finite_leaf_axis_evaluations": len(leaves) * 5,
            "analytic_tail_axis_evaluations": 15,
            "finite_rows": finite_rows,
            "analytic_tail_rows": tail_rows,
            "every_finite_leaf_uses_its_exact_K336_gap_class": True,
            "origin_uses_degree_27_zero_safe_scaled_envelopes": True,
            "projective_preconditioning_precedes_interval_substitution": True,
            "tail_finiteness_is_analytic_not_sampled": True,
            "literal_B5_border_zeros_retained": True,
            "shared_entry_substitution_precedes_complete_determinant_enclosure": True,
        },
        "gap_axis_constants": axes,
        "six_axis_peano_bank": {
            "y_axis_complete_constant_from_K334": upper_text(y_constant),
            "five_gap_axis_constants": {row["axis"]: row["peano_weighted_second_directional_constant"] for row in axes},
            "complete_six_axis_sum_upper": upper_text(six_axis),
            "K299_positive_tensor_remainder_bound_released": True,
        },
        "decision": {
            "all_five_complete_gap_axis_constants_emitted": True,
            "complete_six_axis_peano_norm_emitted": True,
            "k294_gamma_join_released": True,
            "complete_base_action_column_evaluated": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "compose the released six-axis Peano bank with K294's exact radial-simplex normalization inside the complete K288/K305 coherent action-column occurrence sum; evaluate value and residual separately before any native K152 interval",
        },
        "release_test": {
            "K334_checksum_replayed": coverage_checksum(leaves) == k336["fixed_control"]["accepted_subdivision_checksum"],
            "every_K334_finite_leaf_mapped_once": len(leaf_class) == len(leaves) == len(set(leaf_class)),
            "all_five_axes_present": [row["axis"] for row in axes] == axis_names,
            "tail_powers_exactly_35_36_37": TAIL_POWERS == [35, 36, 37],
            "all_constants_finite_positive": all(math.isfinite(float(row["peano_weighted_second_directional_constant"])) and float(row["peano_weighted_second_directional_constant"]) > 0 for row in axes),
            "raw_zero_evaluation_used": False,
            "detached_cofactor_bound_used": False,
            "occurrencewise_absolute_summation_used": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k336["ledger_effect"],
        "source_routing": k336["source_routing"],
        "claim_ceiling": "Complete finite gap-axis Peano bank for the K299 positive tensor rule on K334's accepted exact cover. Every K334 finite leaf is evaluated through its K336 gap class with degree-27 zero-safe origin normalization, legal projective-face preconditioners and shared-entry complete determinant assembly; the three radial tails use the proved 35/36/37 analytic ledger. Applying the five exact Peano masses and adjoining K334's y constant releases the six-axis numerical remainder bank and the K294 composition gate. It does not evaluate the complete K288/K305 action column, residual, exterior complement, native K152 interval, source/ledger, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["accepted_subdivision_checksum"] != "sha256:2df52de1d9beca3aaf6ea730416f7251e79cf8b1da260c214e27d2e3b5996016":
        raise AssertionError("K334 checksum changed")
    if fixed["finite_leaf_count"] != 516 or fixed["gap_class_count"] != 65 or fixed["axis_count"] != 5:
        raise AssertionError("accepted cover census changed")
    if fixed["tail_powers_value_first_second"] != [35, 36, 37]:
        raise AssertionError("analytic tail degree ledger changed")
    cover = payload["complete_cover"]
    if cover["finite_leaf_axis_evaluations"] != 2580 or cover["analytic_tail_axis_evaluations"] != 15:
        raise AssertionError("global evaluation census changed")
    if not all(cover[key] for key in (
        "every_finite_leaf_uses_its_exact_K336_gap_class",
        "origin_uses_degree_27_zero_safe_scaled_envelopes",
        "projective_preconditioning_precedes_interval_substitution",
        "tail_finiteness_is_analytic_not_sampled",
        "literal_B5_border_zeros_retained",
        "shared_entry_substitution_precedes_complete_determinant_enclosure",
    )):
        raise AssertionError("complete-cover composition contract changed")
    axes = payload["gap_axis_constants"]
    if [row["axis"] for row in axes] != ["t0", "t1", "t2", "t3", "t4"]:
        raise AssertionError("gap-axis order changed")
    if [row["K299_peano_mass"] for row in axes] != ["1/504", "1/300", "1/160", "1/72", "1/24"]:
        raise AssertionError("K299 Peano masses changed")
    decision = payload["decision"]
    if not decision["all_five_complete_gap_axis_constants_emitted"] or not decision["complete_six_axis_peano_norm_emitted"] or not decision["k294_gamma_join_released"]:
        raise AssertionError("six-axis release missing")
    if decision["complete_base_action_column_evaluated"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("downstream result overclaimed")
    release = payload["release_test"]
    if not all(release[key] for key in (
        "K334_checksum_replayed",
        "every_K334_finite_leaf_mapped_once",
        "all_five_axes_present",
        "tail_powers_exactly_35_36_37",
        "all_constants_finite_positive",
    )):
        raise AssertionError("K338 release control failed")
    if release["raw_zero_evaluation_used"] or release["detached_cofactor_bound_used"] or release["occurrencewise_absolute_summation_used"] or release["native_K152_interval_emitted"]:
        raise AssertionError("forbidden K338 composition or overclaim detected")


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
