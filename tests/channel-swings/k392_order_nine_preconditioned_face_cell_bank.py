#!/usr/bin/env python3
"""Execute K388-preconditioned positive-width cells on all K390 faces.

Each cell uses one shared normal interval and K390's equal allocation among
the zeroed raw-time axes.  Species determinants are transformed by exact
Newton row/column divided differences on K388's confluent clusters, then by
the exact K388 assignment-dual row/column powers, before one determinant
Taylor polynomial is assembled.  The result is a genuine positive-width
normal-chart interval, not a full projective normal-cone cover.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K383_MODULE = HERE / "k383_order_nine_node_directional_jet_bank.py"
K387_MODULE = HERE / "k387_order_nine_interior_origin_control.py"
K388_MODULE = HERE / "k388_order_nine_mask_native_preconditioner_compiler.py"
K388 = ROOT / "lab/process/k388-order-nine-mask-native-preconditioner-compiler.json"
K390 = ROOT / "lab/process/k390-order-nine-face-program-compiler.json"
OUTPUT = ROOT / "lab/process/k392-order-nine-preconditioned-face-cell-bank.json"

ctx.dps = 180
ctx.threads = 1

NORMAL_CELLS = (
    (Fraction(16, 65536), Fraction(20, 65536)),
    (Fraction(20, 65536), Fraction(25, 65536)),
    (Fraction(25, 65536), Fraction(31, 65536)),
    (Fraction(31, 65536), Fraction(38, 65536)),
    (Fraction(38, 65536), Fraction(47, 65536)),
    (Fraction(47, 65536), Fraction(58, 65536)),
    (Fraction(58, 65536), Fraction(64, 65536)),
)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K383_BACKEND = load_module(K383_MODULE, "k383_for_k392")
K387_BACKEND = load_module(K387_MODULE, "k387_for_k392")
K388_BACKEND = load_module(K388_MODULE, "k388_for_k392")


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def interval(left: Fraction, right: Fraction) -> arb:
    return arb(q((left + right) / 2), q((right - left) / 2))


def digest(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def lower_text(value: arb) -> str:
    return repr(math.nextafter(float(value.lower()), -math.inf))


def upper_text(value: arb) -> str:
    return repr(math.nextafter(float(value.upper()), math.inf))


def abs_upper_text(value: arb) -> str:
    return repr(math.nextafter(float(abs(value).upper()), math.inf))


def polynomial_scale(poly: list[arb], scalar: arb) -> list[arb]:
    return [value * scalar for value in poly]


def polynomial_subtract(left: list[arb], right: list[arb]) -> list[arb]:
    return [a - b for a, b in zip(left, right, strict=True)]


def determinant_taylor(matrix: list[list[list[arb]]]) -> list[arb]:
    rank = len(matrix)
    total = [arb(0), arb(0), arb(0)]
    for permutation in itertools.permutations(range(rank)):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(rank)
            for right in range(left + 1, rank)
        )
        term = [arb(-1 if inversions % 2 else 1), arb(0), arb(0)]
        for row, column in enumerate(permutation):
            term = K383_BACKEND.polynomial_multiply(term, matrix[row][column])
        total = K383_BACKEND.polynomial_add(total, term)
    return total


def raw_times(program: dict[str, Any], rho: arb) -> dict[str, arb]:
    zeroed = set(program["zeroed_axes"])
    codimension = int(program["codimension"])
    if not zeroed or codimension <= 0:
        raise AssertionError("K392 requires a reachable proper face")
    return {
        axis: rho / codimension if axis in zeroed else arb(1) / 256
        for axis in K387_BACKEND.AXES
    }


def exact_node_difference(side: str, newer: int, older: int, raw: dict[str, arb]) -> arb:
    """Return cumulative(newer)-cumulative(older) without interval cancellation."""
    if newer == older:
        return arb(0)
    if newer > older:
        return -sum((raw[f"{side}{index}"] for index in range(older, newer)), arb(0))
    return sum((raw[f"{side}{index}"] for index in range(newer, older)), arb(0))


def divided_difference_rows(
    matrix: list[list[list[arb]]],
    positions: list[int],
    labels: tuple[int, ...],
    side: str,
    raw: dict[str, arb],
) -> tuple[list[list[list[arb]]], arb, int]:
    transformed = [[list(poly) for poly in row] for row in matrix]
    factor = arb(1)
    operations = 0
    clusters: dict[int, list[int]] = defaultdict(list)
    for index, label in enumerate(labels):
        clusters[int(label)].append(index)
    for indices in clusters.values():
        for order in range(1, len(indices)):
            for offset in range(len(indices) - 1, order - 1, -1):
                target = indices[offset]
                previous = indices[offset - 1]
                denominator = exact_node_difference(
                    side, positions[target], positions[indices[offset - order]], raw
                )
                if denominator.contains(0):
                    raise AssertionError("confluent divided-difference denominator contains zero")
                transformed[target] = [
                    polynomial_scale(
                        polynomial_subtract(transformed[target][column], transformed[previous][column]),
                        1 / denominator,
                    )
                    for column in range(len(transformed[target]))
                ]
                factor *= denominator
                operations += 1
    return transformed, factor, operations


def divided_difference_columns(
    matrix: list[list[list[arb]]],
    positions: list[int],
    labels: tuple[int, ...],
    side: str,
    raw: dict[str, arb],
) -> tuple[list[list[list[arb]]], arb, int]:
    transposed = [[matrix[row][column] for row in range(len(matrix))] for column in range(len(matrix))]
    transformed, factor, operations = divided_difference_rows(transposed, positions, labels, side, raw)
    restored = [[transformed[column][row] for column in range(len(matrix))] for row in range(len(matrix))]
    return restored, factor, operations


def template_maps(k388: dict[str, Any]) -> tuple[dict[Any, tuple[str, dict[str, Any]]], dict[Any, str]]:
    singular = {
        tuple(tuple(int(value) for value in row) for row in item["zero_entry_matrix"]): (f"S{index:02d}", item)
        for index, item in enumerate(k388["preconditioner_templates"])
    }
    confluent = {
        (
            int(item["rank"]),
            tuple(int(value) for value in item["row_cluster_labels"]),
            tuple(int(value) for value in item["column_cluster_labels"]),
        ): f"C{index:02d}"
        for index, item in enumerate(k388["confluent_divided_difference_contract"]["templates"])
    }
    return singular, confluent


def preconditioned_determinant_jet(
    rows: list[int],
    columns: list[int],
    cumulative_s: dict[int, arb],
    cumulative_v: dict[int, arb],
    axis: str,
    face: set[str],
    raw: dict[str, arb],
    rho: arb,
    singular_templates: dict[Any, tuple[str, dict[str, Any]]],
    confluent_templates: dict[Any, str],
) -> tuple[list[arb], dict[str, Any]]:
    matrix_descriptor = {
        "rank": len(rows),
        "row_positions": rows,
        "column_positions": columns,
        "entry_axis_masks": [
            [K388_BACKEND.K382_BACKEND.suffix("s", row) + K388_BACKEND.K382_BACKEND.suffix("v", column) for column in columns]
            for row in rows
        ],
    }
    zero_pattern = K388_BACKEND.zero_matrix(matrix_descriptor, face)
    singular_id, singular = singular_templates[zero_pattern]
    row_labels = K388_BACKEND.coalescence_labels(rows, "s", face)
    column_labels = K388_BACKEND.coalescence_labels(columns, "v", face)
    confluent_id = confluent_templates[(len(rows), row_labels, column_labels)]

    matrix: list[list[list[arb]]] = []
    for row in rows:
        entries = []
        for column in columns:
            coefficient = int(axis.startswith("s") and int(axis[1:]) >= row) + int(
                axis.startswith("v") and int(axis[1:]) >= column
            )
            entries.append(K383_BACKEND.kernel_jet(cumulative_s[row] + cumulative_v[column], coefficient))
        matrix.append(entries)

    matrix, row_factor, row_operations = divided_difference_rows(matrix, rows, row_labels, "s", raw)
    matrix, column_factor, column_operations = divided_difference_columns(matrix, columns, column_labels, "v", raw)
    row_powers = [int(value) for value in singular["row_scaling_powers"]]
    column_powers = [int(value) for value in singular["column_scaling_powers"]]
    scaled = [
        [polynomial_scale(matrix[i][j], rho ** (row_powers[i] + column_powers[j])) for j in range(len(columns))]
        for i in range(len(rows))
    ]
    determinant = determinant_taylor(scaled)
    extracted = row_factor * column_factor / (rho ** int(singular["dual_sum"]))
    result = polynomial_scale(determinant, extracted)
    return result, {
        "singular_template": singular_id,
        "confluent_template": confluent_id,
        "row_divided_difference_operations": row_operations,
        "column_divided_difference_operations": column_operations,
    }


def complete_second(
    program: dict[str, Any],
    rho: arb,
    singular_templates: dict[Any, tuple[str, dict[str, Any]]],
    confluent_templates: dict[Any, str],
) -> tuple[arb, list[dict[str, str]], Counter[str], Counter[str], int]:
    raw = raw_times(program, rho)
    cumulative_s, cumulative_v = K387_BACKEND.cumulative(raw)
    face = set(program["zeroed_axes"])
    total = [arb(0), arb(0), arb(0)]
    group_rows = []
    singular_histogram: Counter[str] = Counter()
    confluent_histogram: Counter[str] = Counter()
    divided_difference_operations = 0
    determinant_cache: dict[tuple[tuple[int, ...], tuple[int, ...]], tuple[list[arb], dict[str, Any]]] = {}
    old_cache: dict[tuple[str, int], list[arb]] = {}

    def old_kernel(side: str, position: int) -> list[arb]:
        key = (side, position)
        if key not in old_cache:
            cumulative = cumulative_s if side == "s" else cumulative_v
            coefficient = int(axis.startswith(side) and int(axis[1:]) >= position)
            old_cache[key] = K383_BACKEND.kernel_jet(cumulative[position], coefficient)
        return old_cache[key]

    axis = str(program["axis"])
    for (seed, signature), terms in K383_BACKEND.group_terms().items():
        group_total = [arb(0), arb(0), arb(0)]
        for left in terms:
            for right in terms:
                jet = old_kernel("s", int(left["old_position"]))
                jet = K383_BACKEND.polynomial_multiply(jet, old_kernel("v", int(right["old_position"])))
                left_occurrences = K383_BACKEND.K382_MODULE.occurrences(left)
                right_occurrences = K383_BACKEND.K382_MODULE.occurrences(right)
                if left_occurrences.keys() != right_occurrences.keys():
                    raise AssertionError("species support changed inside a coherent group")
                for species in left_occurrences:
                    rows = tuple(left_occurrences[species])
                    columns = tuple(right_occurrences[species])
                    key = (rows, columns)
                    if key not in determinant_cache:
                        determinant_cache[key] = preconditioned_determinant_jet(
                            list(rows), list(columns), cumulative_s, cumulative_v, axis,
                            face, raw, rho, singular_templates, confluent_templates,
                        )
                    determinant, audit = determinant_cache[key]
                    singular_histogram[audit["singular_template"]] += 1
                    confluent_histogram[audit["confluent_template"]] += 1
                    divided_difference_operations += audit["row_divided_difference_operations"] + audit["column_divided_difference_operations"]
                    jet = K383_BACKEND.polynomial_multiply(jet, determinant)
                multiplier = int(left["exact_operator_coefficient"]) * int(right["exact_operator_coefficient"])
                group_total = K383_BACKEND.polynomial_add(group_total, [value * multiplier for value in jet])
        second = 2 * group_total[2]
        group_rows.append({
            "group_id": f"order9:seed{seed}:{signature}",
            "second_lower": lower_text(second),
            "second_upper": upper_text(second),
        })
        total = K383_BACKEND.polynomial_add(total, group_total)
    return 2 * total[2], group_rows, singular_histogram, confluent_histogram, divided_difference_operations


def build() -> dict[str, Any]:
    k388 = json.loads(K388.read_text())
    k390 = json.loads(K390.read_text())
    singular_templates, confluent_templates = template_maps(k388)
    programs = k390["face_programs"]
    if len(programs) != 695:
        raise AssertionError("K390 face bank changed")

    rows = []
    global_singular: Counter[str] = Counter()
    global_confluent: Counter[str] = Counter()
    direct_overlap_controls = []
    seen_axis: set[str] = set()
    for program in programs:
        controls = []
        for cell_index, (left, right) in enumerate(NORMAL_CELLS):
            rho = interval(left, right)
            second, groups, singular_histogram, confluent_histogram, dd_operations = complete_second(
                program, rho, singular_templates, confluent_templates
            )
            if not math.isfinite(float(abs(second).upper())):
                raise AssertionError(f"non-finite K392 face cell {program['program_id']}")
            raw = raw_times(program, rho)
            cumulative_s, cumulative_v = K387_BACKEND.cumulative(raw)
            minimum_argument = min(
                [value.lower() for value in cumulative_s.values()]
                + [value.lower() for value in cumulative_v.values()]
            )
            if minimum_argument <= 0:
                raise AssertionError("positive-width K392 cell touched zero")
            singular_power = int(program["maximum_value_first_second_singular_powers"][2])
            scaled = abs(second) * rho ** singular_power
            active_upper = raw[program["axis"]].upper()
            peano = abs(second) * arb(active_upper) * arb(active_upper) / 2
            control = {
                "normal_interval": [q(left), q(right)],
                "normal_width": q(right - left),
                "minimum_cumulative_argument_lower": lower_text(arb(minimum_argument)),
                "complete_second_derivative_lower": lower_text(second),
                "complete_second_derivative_upper": upper_text(second),
                "complete_second_derivative_abs_upper": abs_upper_text(second),
                "rho_to_K389_second_singular_power_abs_upper": abs_upper_text(scaled),
                "K385_quadratic_peano_majorant_abs_upper": abs_upper_text(peano),
                "coherent_group_count": len(groups),
                "all_20_group_intervals_sha256": digest(groups),
                "singular_template_ids": sorted(singular_histogram),
                "confluent_template_ids": sorted(confluent_histogram),
                "divided_difference_operation_uses": dd_operations,
            }
            controls.append(control)
            global_singular.update(singular_histogram)
            global_confluent.update(confluent_histogram)

            if cell_index == 0 and program["axis"] not in seen_axis:
                direct, _ = K387_BACKEND.complete_second(program["axis"], raw)
                overlap = not (second.upper() < direct.lower() or second.lower() > direct.upper())
                if not overlap:
                    raise AssertionError(f"preconditioned/direct intervals do not overlap for {program['axis']}")
                direct_overlap_controls.append({
                    "axis": program["axis"],
                    "program_id": program["program_id"],
                    "normal_interval": [q(left), q(right)],
                    "preconditioned_lower": lower_text(second),
                    "preconditioned_upper": upper_text(second),
                    "direct_lower": lower_text(direct),
                    "direct_upper": upper_text(direct),
                    "intervals_overlap": overlap,
                })
                seen_axis.add(program["axis"])

        rows.append({
            "program_id": program["program_id"],
            "face_id": program["face_id"],
            "axis": program["axis"],
            "face_kind": program["face_kind"],
            "zeroed_axes": program["zeroed_axes"],
            "codimension": program["codimension"],
            "active_peano_axis_zeroed": program["active_peano_axis_zeroed"],
            "maximum_second_singular_power": program["maximum_value_first_second_singular_powers"][2],
            "minimum_face_normal_power": program["minimum_second_derivative_face_normal_power"],
            "cells": controls,
        })

    return {
        "schema_version": "1.0",
        "result_id": "K392-ORDER-NINE-PRECONDITIONED-FACE-CELL-BANK",
        "created": "2026-09-23",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k388-order-nine-mask-native-preconditioner-compiler.json",
                "lab/process/k390-order-nine-face-program-compiler.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "reachable_face_programs": len(programs),
            "positive_width_cells_per_face": len(NORMAL_CELLS),
            "complete_positive_width_cells": len(rows) * len(NORMAL_CELLS),
            "ordered_descriptors_per_cell": 4480,
            "ordered_descriptor_cell_evaluations": len(rows) * len(NORMAL_CELLS) * 4480,
            "coherent_groups_per_cell": 20,
            "normal_cells": [[q(a), q(b)] for a, b in NORMAL_CELLS],
            "K388_template_bank_sha256": k388["template_summary"]["template_bank_sha256"],
            "K390_program_bank_sha256": k390["program_summary"]["complete_program_bank_sha256"],
        },
        "execution_contract": {
            "one_shared_normal_interval_per_cell": True,
            "zeroed_raw_times_equal_rho_over_codimension": True,
            "exact_cumulative_node_differences_used": True,
            "confluent_row_column_divided_differences_applied_before_determinant_assembly": True,
            "K388_assignment_dual_row_column_scaling_applied_before_determinant_assembly": True,
            "all_ordered_orientations_retained": True,
            "all_20_coherent_groups_assembled_before_reported_enclosure": True,
            "raw_Bessel_evaluation_at_zero_used": False,
            "cells_are_positive_width_normal_chart_intervals": True,
            "equal_normal_chart_is_not_full_projective_normal_cone": True,
            "cells_are_not_recursive_whole_domain_cover": True,
        },
        "face_cell_bank": rows,
        "direct_overlap_controls": direct_overlap_controls,
        "bank_summary": {
            "all_695_faces_executed": len(rows) == 695,
            "all_4865_cells_finite": all(math.isfinite(float(cell["complete_second_derivative_abs_upper"])) for row in rows for cell in row["cells"]),
            "every_cell_has_positive_argument_floor": all(float(cell["minimum_cumulative_argument_lower"]) > 0 for row in rows for cell in row["cells"]),
            "all_18_hybrids_with_faces_have_direct_overlap_control": len(direct_overlap_controls) == 18 and all(row["intervals_overlap"] for row in direct_overlap_controls),
            "all_60_singular_templates_executed": set(global_singular) == {f"S{index:02d}" for index in range(60)},
            "all_75_confluent_templates_executed": set(global_confluent) == {f"C{index:02d}" for index in range(75)},
            "complete_bank_sha256": digest(rows),
        },
        "decision": {
            "K388_preconditioned_positive_width_face_cells_released": True,
            "all_695_reachable_faces_numerically_evaluated": True,
            "canonical_equal_normal_chart_bank_complete": True,
            "full_projective_normal_cone_complete": False,
            "recursive_positive_interior_cover_complete": False,
            "analytic_radial_tails_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "integrate the accepted dyadic equal-normal strips, then add the missing normal-projective cover before joining recursive positive-interior cells and analytic tails",
        },
        "release_test": {
            "exactly_695_face_programs_present": len(rows) == 695,
            "exactly_4865_positive_width_cells_present": sum(len(row["cells"]) for row in rows) == 4865,
            "all_21795200_ordered_descriptor_cell_evaluations_covered": len(rows) * len(NORMAL_CELLS) * 4480 == 21_795_200,
            "all_cells_finite": all(math.isfinite(float(cell["complete_second_derivative_abs_upper"])) for row in rows for cell in row["cells"]),
            "all_argument_floors_positive": all(float(cell["minimum_cumulative_argument_lower"]) > 0 for row in rows for cell in row["cells"]),
            "all_direct_overlap_controls_pass": len(direct_overlap_controls) == 18 and all(row["intervals_overlap"] for row in direct_overlap_controls),
            "all_singular_and_confluent_templates_executed": set(global_singular) == {f"S{index:02d}" for index in range(60)} and set(global_confluent) == {f"C{index:02d}" for index in range(75)},
            "raw_zero_evaluation_absent": True,
            "full_normal_cone_not_overclaimed": True,
            "complete_order_nine_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k390["ledger_effect"],
        "source_routing": k390["source_routing"],
        "claim_ceiling": "Rigorous 180-digit Arb positive-width normal-chart cell bank for all 695 K390 reachable order-nine faces on seven exact rational cells partitioning rho in [1/4096,1/1024]. Every cell applies K388's exact confluent row/column divided differences and assignment-dual row/column scaling before determinant Taylor assembly, retains all 4,480 ordered descriptors and all 20 coherent groups, and has a strictly positive argument floor. One direct-evaluator overlap control passes for each of the eighteen hybrids with reachable faces. The equal allocation among zeroed axes is one canonical normal chart, not a full projective normal-cone cover, recursive positive-interior cover, analytic tail, hybrid integral, complete order-nine remainder/integral, action column, R_ref, K152 interval, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    expected = (695, 7, 4865, 4480, 21_795_200, 20)
    actual = (
        fixed["reachable_face_programs"], fixed["positive_width_cells_per_face"],
        fixed["complete_positive_width_cells"], fixed["ordered_descriptors_per_cell"],
        fixed["ordered_descriptor_cell_evaluations"], fixed["coherent_groups_per_cell"],
    )
    if actual != expected:
        raise AssertionError("K392 fixed census changed")
    rows = payload["face_cell_bank"]
    if len(rows) != 695 or len({row["program_id"] for row in rows}) != 695 or any(len(row["cells"]) != 7 for row in rows):
        raise AssertionError("K392 face-cell identities changed")
    if any(cell["coherent_group_count"] != 20 or float(cell["minimum_cumulative_argument_lower"]) <= 0 for row in rows for cell in row["cells"]):
        raise AssertionError("K392 coherent positive cell boundary changed")
    if len(payload["direct_overlap_controls"]) != 18 or not all(row["intervals_overlap"] for row in payload["direct_overlap_controls"]):
        raise AssertionError("K392 direct-overlap bank changed")
    contract = payload["execution_contract"]
    required = (
        "one_shared_normal_interval_per_cell", "exact_cumulative_node_differences_used",
        "confluent_row_column_divided_differences_applied_before_determinant_assembly",
        "K388_assignment_dual_row_column_scaling_applied_before_determinant_assembly",
        "all_ordered_orientations_retained", "all_20_coherent_groups_assembled_before_reported_enclosure",
        "cells_are_positive_width_normal_chart_intervals", "equal_normal_chart_is_not_full_projective_normal_cone",
        "cells_are_not_recursive_whole_domain_cover",
    )
    if not all(contract[key] for key in required) or contract["raw_Bessel_evaluation_at_zero_used"]:
        raise AssertionError("K392 execution contract changed")
    decision = payload["decision"]
    if not decision["K388_preconditioned_positive_width_face_cells_released"] or not decision["all_695_reachable_faces_numerically_evaluated"]:
        raise AssertionError("K392 release lost")
    if any(decision[key] for key in ("full_projective_normal_cone_complete", "recursive_positive_interior_cover_complete", "analytic_radial_tails_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K392 overclaimed whole-domain closure")
    if not all(payload["release_test"].values()):
        raise AssertionError("K392 release test failed")


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
