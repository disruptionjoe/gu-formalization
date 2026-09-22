#!/usr/bin/env python3
"""Integrate the complete K305 value functional at the K299 node.

The six projective gaps and y are fixed at p_i=1/6 and y=1/2.  K334's
radial/projective refinement is deduplicated from its gap refinement, giving
twelve finite r/s cells plus three analytic radial tails.  On each cell the
two K340 terminal sectors keep their Jacobian in the complete bordered matrix;
the four K305 groups are bounded only after their coherent determinants form.
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
K314_MODULE = HERE / "k314_order_seven_projective_face_oracle.py"
K326_MODULE = HERE / "k326_order_seven_signed_entry_jet_chart_bank.py"
K328_MODULE = HERE / "k328_order_seven_scaled_derivative_envelope_bank.py"
K338_MODULE = HERE / "k338_order_seven_complete_gap_axis_peano_bank.py"
K299 = ROOT / "lab/process/k299-order-seven-positive-peano-simplex-rule.json"
K305 = ROOT / "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json"
K334 = ROOT / "lab/process/k334-order-seven-recursive-global-subdivision.json"
K340 = ROOT / "lab/process/k340-order-seven-barycentric-value-atlas.json"
OUTPUT = ROOT / "lab/process/k341-order-seven-complete-barycentric-value.json"

ctx.dps = 180
ctx.threads = 1

FIXED_GAPS = tuple((Fraction(1, 6), Fraction(1, 6)) for _ in range(6))
PROJECTIVE_CELLS = {
    "s0": (Fraction(0), Fraction(1, 4)),
    "interior": (Fraction(1, 4), Fraction(3, 4)),
    "s1": (Fraction(3, 4), Fraction(1)),
}
TAIL_POWER = 35
EXPECTED_RS_CHECKSUM = "sha256:035429c0d55c405368fb7a70319b9ab68993e85db1d01a34c49623ad2085e643"
EXPECTED_COMPLETE_UPPER = "1.4832493544503225e-06"
ROW_ORDERS = [0, 1, 2, 0]
COLUMN_ORDERS = [0, 1, 2, 0]


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


def bisect(interval: tuple[Fraction, Fraction]) -> tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
    middle = (interval[0] + interval[1]) / 2
    return (interval[0], middle), (middle, interval[1])


def transpose(matrix: list[list[arb]]) -> list[list[arb]]:
    return [list(row) for row in zip(*matrix, strict=True)]


def determinant(matrix: list[list[arb]]) -> arb:
    total = arb(0)
    for permutation in itertools.permutations(range(len(matrix))):
        inversions = sum(permutation[i] > permutation[j] for i in range(len(matrix)) for j in range(i + 1, len(matrix)))
        term = arb(-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def deduplicated_rs_cells(k334: dict[str, Any], k338) -> list[dict[str, Any]]:
    cells: dict[str, dict[str, Any]] = {}
    for leaf in k334["recursive_cover"]["finite_leaves"]:
        region, radial, projective, _ = k338.parse_leaf(leaf["path"])
        parts = leaf["path"].split("/")
        cell_id = parts[0] if len(parts) == 1 else f"{parts[0]}/{parts[1][:2]}"
        candidate = {
            "id": cell_id,
            "region": region,
            "radial": radial,
            "projective": projective,
        }
        if cell_id in cells and cells[cell_id] != candidate:
            raise AssertionError("K334 gap leaves disagree on their r/s projection")
        cells[cell_id] = candidate
    return [cells[key] for key in sorted(cells)]


def rs_checksum(cells: list[dict[str, Any]]) -> str:
    payload = [
        {
            "id": row["id"],
            "region": row["region"],
            "radial": [q(value) for value in row["radial"]],
            "projective": [q(value) for value in row["projective"]],
        }
        for row in cells
    ]
    return "sha256:" + hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def d4_value(k326, k328, k338, radius: Fraction, region: str, projective) -> arb:
    nodes = k338.node_bank(region, projective, FIXED_GAPS)
    matrix: list[list[arb]] = []
    for row in range(4):
        entries = []
        for column in range(4):
            lower = nodes["odd_left"][row] + nodes["odd_right"][column]
            if region == "s0" and (row, column) == (3, 3):
                value = k326.symmetric(arb(q(2 * k328.scaled_derivative_upper(0, radius * k338.ARGUMENT_MAX))))
            else:
                base = row + column
                value = k326.signed(k338.scaled_dd_upper(k328, radius, lower, row, column), -1 if base % 2 else 1)
                if region == "s0" and row == 3:
                    value *= arb(q(projective[1]))
            entries.append(value)
        matrix.append(entries)
    return determinant(matrix)


def upper_face_border_value(k326, k328, k338, radius: Fraction, projective, row: int) -> arb:
    p = Fraction(1, 6)
    h = p * (Fraction(9, 4), Fraction(5, 4), Fraction(1, 4))[row]
    a = ROW_ORDERS[row]
    tmax = 1 - projective[0]
    prefactor = tmax ** (2 - a) * Fraction(1, 2)
    return k326.signed(arb(q(prefactor)) * k338.scaled_dd_upper(k328, radius, h, a, 0), -1 if a % 2 else 1)


def left_b5_value(k326, k328, k338, radius: Fraction, region: str, projective) -> list[list[arb]]:
    nodes = k338.node_bank(region, projective, FIXED_GAPS)
    matrix = [[arb(0) for _ in range(5)] for _ in range(5)]
    x_upper = radius * projective[1]
    for row in range(5):
        for column in range(5):
            if (row, column) in ((3, 4), (4, 3), (4, 4)):
                continue
            if (row, column) == (3, 3):
                value = k326.symmetric(arb(4))
            elif region == "s1" and column == 4 and row < 3:
                value = upper_face_border_value(k326, k328, k338, radius, projective, row)
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
                value = k326.signed(k338.scaled_dd_upper(k328, radius, lower, a, c), -1 if (a + c) % 2 else 1)
                if row < 4 and column == 3:
                    value *= arb(q(x_upper))
                if column == 4 or row == 4:
                    value *= arb("1/2")
            if region == "s0" and row == 3:
                value *= arb(q(projective[1]))
            matrix[row][column] = value
    return matrix


def sector_value(modules: dict[str, Any], radius: Fraction, region: str, projective) -> arb:
    k312, k314, k326, k328, k338 = (modules[name] for name in ("k312", "k314", "k326", "k328", "k338"))
    d4 = d4_value(k326, k328, k338, radius, region, projective)
    left = left_b5_value(k326, k328, k338, radius, region, projective)
    right = transpose(left)
    left_det = determinant(left)
    right_det = determinant(right)
    projective_polynomial = k314.projective_polynomial_upper(
        {name: interval for name, interval in zip(k314.GAPS, FIXED_GAPS, strict=True)}
    )
    scalar = Fraction(4, 120) * radius * radius * projective[1] * projective[1] * Fraction(1, 16) * projective_polynomial
    return arb(q(scalar)) * d4 * (left_det + right_det)


def finite_cell_value(modules: dict[str, Any], cell: dict[str, Any]) -> arb:
    coefficient = sector_value(modules, cell["radial"][1], cell["region"], cell["projective"])
    radial_mass = modules["k312"].radial_finite_upper(cell["radial"][0], cell["radial"][1], 6)
    projective_mass = modules["k338"].projective_masses(modules["k312"], cell["region"], cell["projective"])[0]
    return coefficient * arb(q(radial_mass * projective_mass))


def tail_value(modules: dict[str, Any], region: str, projective) -> arb:
    coefficient = sector_value(modules, Fraction(1), region, projective)
    radial_mass = modules["k312"].radial_tail_upper(Fraction(1), TAIL_POWER)
    projective_mass = modules["k338"].projective_masses(modules["k312"], region, projective)[0]
    return coefficient * arb(q(radial_mass * projective_mass))


def build() -> dict[str, Any]:
    modules = {
        "k312": load_module(K312_MODULE, "k341_k312"),
        "k314": load_module(K314_MODULE, "k341_k314"),
        "k326": load_module(K326_MODULE, "k341_k326"),
        "k328": load_module(K328_MODULE, "k341_k328"),
        "k338": load_module(K338_MODULE, "k341_k338"),
    }
    k299 = json.loads(K299.read_text())
    k305 = json.loads(K305.read_text())
    k334 = json.loads(K334.read_text())
    k340 = json.loads(K340.read_text())
    if not k340["decision"]["value_mode_barycentric_terminal_split_atlas_complete"]:
        raise AssertionError("K340 value atlas unavailable")
    if k299["positive_cubature"]["simplex_node"] != ["1/6"] * 6:
        raise AssertionError("K299 node changed")
    if len(k305["coherent_groups"]) != 4:
        raise AssertionError("K305 group census changed")

    cells = deduplicated_rs_cells(k334, modules["k338"])
    finite_rows = []
    finite_total = arb(0)
    for cell in cells:
        value = finite_cell_value(modules, cell)
        finite_total += abs(value)
        finite_rows.append({
            "id": cell["id"],
            "region": cell["region"],
            "radial": [q(v) for v in cell["radial"]],
            "projective": [q(v) for v in cell["projective"]],
            "two_sector_four_group_abs_upper": upper_text(value),
        })
    tail_rows = []
    tail_total = arb(0)
    for region, projective in PROJECTIVE_CELLS.items():
        value = tail_value(modules, region, projective)
        tail_total += abs(value)
        tail_rows.append({
            "region": region,
            "projective": [q(v) for v in projective],
            "radial_tail_power": TAIL_POWER,
            "two_sector_four_group_abs_upper": upper_text(value),
        })
    total = finite_total + tail_total
    if not math.isfinite(float(total.upper())) or total.upper() <= 0:
        raise AssertionError("complete barycentric value upper is not finite positive")

    rs_volume = sum(
        ((row["radial"][1] - row["radial"][0]) * (row["projective"][1] - row["projective"][0]) for row in cells),
        Fraction(0),
    )
    return {
        "schema_version": "1.0",
        "result_id": "K341-ORDER-SEVEN-COMPLETE-BARYCENTRIC-VALUE",
        "created": "2026-09-22",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k299-order-seven-positive-peano-simplex-rule.json",
                "lab/process/k305-order-seven-coherent-bordered-functional-compiler.json",
                "lab/process/k334-order-seven-recursive-global-subdivision.json",
                "lab/process/k340-order-seven-barycentric-value-atlas.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "simplex_node": ["1/6"] * 6,
            "simplex_weight": "1/120",
            "y_node": "1/2",
            "terminal_sector_count": 2,
            "coherent_group_count": 4,
            "finite_rs_cell_count": len(cells),
            "analytic_tail_cell_count": len(tail_rows),
            "radial_tail_power": TAIL_POWER,
            "rs_cover_checksum": rs_checksum(cells),
        },
        "deduplicated_radial_projective_cover": {
            "source_K334_leaf_count": len(k334["recursive_cover"]["finite_leaves"]),
            "finite_rs_cells": finite_rows,
            "analytic_tail_cells": tail_rows,
            "exact_finite_rs_volume_sum": q(rs_volume),
            "gap_refinement_not_integrated_at_fixed_barycenter": True,
            "barycenter_boundary_ownership": "gap refinements are discarded after r/s projection because p_i is fixed exactly; no adjacent gap leaf is summed twice",
            "tail_finiteness_is_analytic_not_sampled": True,
        },
        "complete_barycentric_value": {
            "prefactor_free_finite_abs_upper": upper_text(finite_total),
            "prefactor_free_analytic_tail_abs_upper": upper_text(tail_total),
            "prefactor_free_complete_abs_upper": upper_text(total),
            "symmetric_interval": [f"-{upper_text(total)}", upper_text(total)],
            "K299_simplex_weight_applied_once": True,
            "K318_y_Peano_mass_applied": False,
            "K294_bare_mass_applied_again": False,
        },
        "assembly_contract": {
            "all_four_K305_groups_included": True,
            "all_eight_split_variables_retained": True,
            "terminal_jacobian_absorbed_into_complete_column_or_row": True,
            "literal_B5_zeros_retained": True,
            "complete_group_determinant_precedes_absolute_value": True,
            "occurrencewise_absolute_sum_used": False,
            "detached_terminal_cofactor_used": False,
            "raw_Bessel_zero_evaluation_used": False,
            "degree_27_origin_normalization_used": True,
            "projective_face_preconditioners_used": True,
        },
        "decision": {
            "complete_prefactor_free_order_seven_base_value_interval_emitted": True,
            "native_prefactor_applied": False,
            "K339_residual_joined": False,
            "complete_base_action_column_evaluated": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "apply the native (2*pi)^-9 scalar once to this base-value interval, then add K339's separately normalized Peano residual radius",
        },
        "ledger_effect": k340["ledger_effect"],
        "source_routing": k340["source_routing"],
        "claim_ceiling": "Finite complete outward interval for the four-group K305 order-seven value functional at K299's node p_i=1/6,y=1/2. Twelve deduplicated K334 radial/projective cells and three analytic tails cover the full half-line; both K340 terminal sectors and all eight split variables remain inside complete bordered determinants. The simplex weight is applied once, while K318's Peano mass and K294's bare mass are not reapplied. The native (2*pi)^-9 scalar and K339 residual join remain separate, and no complete base action column, R_ref residual, K152 interval, source/ledger move, canon, paper, public or physical claim is emitted.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["simplex_node"] != ["1/6"] * 6 or fixed["simplex_weight"] != "1/120" or fixed["y_node"] != "1/2":
        raise AssertionError("K341 fixed node changed")
    if fixed["terminal_sector_count"] != 2 or fixed["coherent_group_count"] != 4:
        raise AssertionError("sector/group census changed")
    if fixed["finite_rs_cell_count"] != 12 or fixed["analytic_tail_cell_count"] != 3 or fixed["radial_tail_power"] != 35:
        raise AssertionError("radial/projective cover census changed")
    if fixed["rs_cover_checksum"] != EXPECTED_RS_CHECKSUM:
        raise AssertionError("deduplicated r/s cover identity changed")
    cover = payload["deduplicated_radial_projective_cover"]
    if cover["source_K334_leaf_count"] != 516 or cover["exact_finite_rs_volume_sum"] != "1":
        raise AssertionError("deduplicated r/s cover changed")
    if not cover["gap_refinement_not_integrated_at_fixed_barycenter"] or not cover["tail_finiteness_is_analytic_not_sampled"]:
        raise AssertionError("fixed-node cover contract changed")
    value = payload["complete_barycentric_value"]
    if value["prefactor_free_complete_abs_upper"] != EXPECTED_COMPLETE_UPPER:
        raise AssertionError("complete barycentric value certificate changed")
    if not math.isfinite(float(value["prefactor_free_complete_abs_upper"])) or float(value["prefactor_free_complete_abs_upper"]) <= 0:
        raise AssertionError("complete value upper is invalid")
    if not value["K299_simplex_weight_applied_once"] or value["K318_y_Peano_mass_applied"] or value["K294_bare_mass_applied_again"]:
        raise AssertionError("value normalization ledger changed")
    assembly = payload["assembly_contract"]
    required = [
        "all_four_K305_groups_included",
        "all_eight_split_variables_retained",
        "terminal_jacobian_absorbed_into_complete_column_or_row",
        "literal_B5_zeros_retained",
        "complete_group_determinant_precedes_absolute_value",
        "degree_27_origin_normalization_used",
        "projective_face_preconditioners_used",
    ]
    if not all(assembly[key] for key in required):
        raise AssertionError("complete assembly contract failed")
    if assembly["occurrencewise_absolute_sum_used"] or assembly["detached_terminal_cofactor_used"] or assembly["raw_Bessel_zero_evaluation_used"]:
        raise AssertionError("forbidden K341 enclosure introduced")
    decision = payload["decision"]
    if not decision["complete_prefactor_free_order_seven_base_value_interval_emitted"] or decision["native_prefactor_applied"] or decision["K339_residual_joined"]:
        raise AssertionError("K341 release boundary changed")
    if decision["complete_base_action_column_evaluated"] or decision["native_K152_interval_emitted"]:
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
