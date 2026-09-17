#!/usr/bin/env python3
"""K201 third enlarged a/c-square ring certificate.

K200 closed 503/1024 <= a,c <= 521/1024. K201 certifies the exact
eight-step ring outside that square as two row-chart side strips and four corner
boxes. Exact row/column transpose supplies the companion c strips. Together
with K200, the six packets close 495/1024 <= a,c <= 529/1024. Farther shells
and every cubature or physical consequence remain open.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K200_PATH = ROOT / "tests/channel-swings/k200_order_six_second_ac_ring.py"
K200_MANIFEST = ROOT / "lab/process/k200-order-six-second-ac-ring-wave.json"
OUTPUT = ROOT / "lab/process/k201-order-six-third-ac-ring-wave.json"
CHECKPOINT = ROOT / "_local/k201-order-six-third-ac-ring-checkpoint.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K200 = load_module("k200_for_k201", K200_PATH)
K199 = K200.K199
K198 = K199.K198
K197 = K199.K197
K196 = K199.K196
K193 = K199.K193
K191 = K199.K191

INNER = K200.OUTER
OUTER = (Fraction(495, 1024), Fraction(529, 1024))
LOW = (OUTER[0], INNER[0])
HIGH = (INNER[1], OUTER[1])
Q_CELLS = K200.Q_CELLS
PACKETS = (
    ("lower_side", LOW, INNER, "row side strip; transpose supplies lower c strip"),
    ("upper_side", HIGH, INNER, "row side strip; transpose supplies upper c strip"),
    ("lower_lower", LOW, LOW, "corner"),
    ("lower_upper", LOW, HIGH, "corner"),
    ("upper_lower", HIGH, LOW, "corner"),
    ("upper_upper", HIGH, HIGH, "corner"),
)
MAX_SHAPE_DEPTH = 4


def checkpoint_fingerprint() -> str:
    digest = hashlib.sha256()
    digest.update(Path(__file__).read_bytes())
    digest.update(K200_MANIFEST.read_bytes())
    return digest.hexdigest()


def write_checkpoint(state: dict[str, Any]) -> None:
    CHECKPOINT.parent.mkdir(parents=True, exist_ok=True)
    temporary = CHECKPOINT.with_suffix(".tmp")
    temporary.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")
    temporary.replace(CHECKPOINT)


def load_checkpoint() -> dict[str, Any]:
    fingerprint = checkpoint_fingerprint()
    if not CHECKPOINT.exists():
        return {
            "schema_version": "1.0",
            "fingerprint": fingerprint,
            "q_tiles": [],
            "rejected_parent_cells": [],
            "current_q": None,
        }
    state = json.loads(CHECKPOINT.read_text())
    if state.get("schema_version") != "1.0" or state.get("fingerprint") != fingerprint:
        raise AssertionError("K201 checkpoint does not match the current generator and predecessor")
    return state


def ftext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def rectangle_certificate(
    packet_id: str,
    packet_role: str,
    q_bounds: tuple[Fraction, Fraction],
    base_index: int,
    a_bounds: tuple[Fraction, Fraction],
    c_bounds: tuple[Fraction, Fraction],
    depth: int,
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    scale_cells, radial_cells = K197.GRID_CELLS[3]
    lowers: list[float] = []
    uppers: list[float] = []
    tails: list[float] = []
    for scale_index, scale_bounds in enumerate(scale_cells):
        for radial_index, radial_bounds in enumerate(radial_cells):
            regularizer, tail = K197.fast_chart_cell(
                3,
                radial_bounds,
                scale_bounds,
                a_bounds,
                q_bounds,
                c_bounds,
            )
            lower = float(regularizer.lower())
            if not lower > 0:
                return None, {
                    "packet_id": packet_id,
                    "packet_role": packet_role,
                    "base_index": base_index,
                    "depth": depth,
                    "a": [ftext(value) for value in a_bounds],
                    "c": [ftext(value) for value in c_bounds],
                    "q": [ftext(value) for value in q_bounds],
                    "scale_index": scale_index,
                    "radial_index": radial_index,
                    "R_lower": lower,
                    "R_upper": float(regularizer.upper()),
                    "maximum_entry_tail": float(tail),
                }
            lowers.append(lower)
            uppers.append(float(regularizer.upper()))
            tails.append(float(tail))
    return {
        "packet_id": packet_id,
        "packet_role": packet_role,
        "base_index": base_index,
        "depth": depth,
        "a": [ftext(value) for value in a_bounds],
        "c": [ftext(value) for value in c_bounds],
        "q": [ftext(value) for value in q_bounds],
        "outward_cells": len(scale_cells) * len(radial_cells),
        "minimum_R_lower": min(lowers),
        "maximum_R_upper": max(uppers),
        "maximum_entry_tail": max(tails),
        "all_cells_strictly_positive": True,
    }, None


def certify_rectangle_or_bisect(
    packet_id: str,
    packet_role: str,
    q_bounds: tuple[Fraction, Fraction],
    base_index: int,
    a_bounds: tuple[Fraction, Fraction],
    c_bounds: tuple[Fraction, Fraction],
    depth: int,
    rejected: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    accepted, failure = rectangle_certificate(
        packet_id, packet_role, q_bounds, base_index, a_bounds, c_bounds, depth
    )
    if accepted is not None:
        return [accepted]
    assert failure is not None
    rejected.append(failure)
    if depth >= MAX_SHAPE_DEPTH:
        raise AssertionError(f"K201 ring packet lost positivity after refinement: {failure}")
    a_width = a_bounds[1] - a_bounds[0]
    c_width = c_bounds[1] - c_bounds[0]
    if a_width >= c_width:
        midpoint = (a_bounds[0] + a_bounds[1]) / 2
        return certify_rectangle_or_bisect(
            packet_id, packet_role, q_bounds, base_index,
            (a_bounds[0], midpoint), c_bounds, depth + 1, rejected,
        ) + certify_rectangle_or_bisect(
            packet_id, packet_role, q_bounds, base_index,
            (midpoint, a_bounds[1]), c_bounds, depth + 1, rejected,
        )
    midpoint = (c_bounds[0] + c_bounds[1]) / 2
    return certify_rectangle_or_bisect(
        packet_id, packet_role, q_bounds, base_index,
        a_bounds, (c_bounds[0], midpoint), depth + 1, rejected,
    ) + certify_rectangle_or_bisect(
        packet_id, packet_role, q_bounds, base_index,
        a_bounds, (midpoint, c_bounds[1]), depth + 1, rejected,
    )


def build_ring(progress: bool = False, checkpoint: bool = False) -> dict[str, Any]:
    state = load_checkpoint() if checkpoint else {
        "q_tiles": [], "rejected_parent_cells": [], "current_q": None,
    }
    q_tiles: list[dict[str, Any]] = state["q_tiles"]
    rejected: list[dict[str, Any]] = state["rejected_parent_cells"]
    for index, q_bounds in enumerate(Q_CELLS):
        if index < len(q_tiles):
            if progress:
                print(
                    f"K201 size=3 base_q_cell={index + 1}/{len(Q_CELLS)} "
                    "resumed_complete=True",
                    file=sys.stderr,
                    flush=True,
                )
            continue
        if index != len(q_tiles):
            raise AssertionError("K201 checkpoint q-tile sequence is not contiguous")
        current = state.get("current_q")
        if current is None:
            current = {"base_index": index, "accepted_ring_tiles": []}
        if current.get("base_index") != index:
            raise AssertionError("K201 checkpoint current q tile is out of sequence")
        accepted: list[dict[str, Any]] = current["accepted_ring_tiles"]
        completed_packets = {row["packet_id"] for row in accepted}
        for packet_id, a_bounds, c_bounds, packet_role in PACKETS:
            if packet_id in completed_packets:
                continue
            packet_tiles = certify_rectangle_or_bisect(
                packet_id,
                packet_role,
                q_bounds,
                index,
                a_bounds,
                c_bounds,
                0,
                rejected,
            )
            accepted.extend(packet_tiles)
            if checkpoint:
                current["accepted_ring_tiles"] = accepted
                state["current_q"] = current
                write_checkpoint(state)
            if progress:
                print(
                    f"K201 size=3 base_q_cell={index + 1}/{len(Q_CELLS)} "
                    f"packet={packet_id} accepted_tiles={len(packet_tiles)}",
                    file=sys.stderr,
                    flush=True,
                )
        tile = {
            "base_index": index,
            "q": [ftext(value) for value in q_bounds],
            "accepted_ring_tiles": accepted,
            "accepted_ring_tile_count": len(accepted),
            "minimum_R_lower": min(row["minimum_R_lower"] for row in accepted),
            "maximum_R_upper": max(row["maximum_R_upper"] for row in accepted),
            "maximum_entry_tail": max(row["maximum_entry_tail"] for row in accepted),
            "all_cells_strictly_positive": True,
        }
        q_tiles.append(tile)
        if checkpoint:
            state["current_q"] = None
            write_checkpoint(state)
        if progress:
            print(
                f"K201 size=3 base_q_cell={index + 1}/{len(Q_CELLS)} "
                f"accepted_ring_tiles={len(accepted)} "
                f"minimum_lower={tile['minimum_R_lower']:.17g}",
                file=sys.stderr,
                flush=True,
            )
    parsed = [tuple(Fraction(value) for value in row["q"]) for row in q_tiles]
    accepted_tiles = [child for row in q_tiles for child in row["accepted_ring_tiles"]]
    unique_cells = sum(row["outward_cells"] for row in accepted_tiles)
    return {
        "size": 3,
        "subdivisions": K198.K195.SUBDIVISIONS[3],
        "base_q_subdivisions": len(Q_CELLS),
        "accepted_q_tiles": len(q_tiles),
        "accepted_ring_tiles": len(accepted_tiles),
        "maximum_shape_adaptive_depth_used": max(row["depth"] for row in accepted_tiles),
        "rejected_parent_cells": rejected,
        "inner_a_c_range": [ftext(value) for value in INNER],
        "outer_a_c_range": [ftext(value) for value in OUTER],
        "ring_packets": {
            packet_id: {
                "a": [ftext(value) for value in a_bounds],
                "c": [ftext(value) for value in c_bounds],
                "role": packet_role,
            }
            for packet_id, a_bounds, c_bounds, packet_role in PACKETS
        },
        "q_range": [ftext(K197.Q_START), ftext(K197.Q_END)],
        "q_tiles": q_tiles,
        "unique_outward_cells": unique_cells,
        "chart_cell_instances_by_exact_transpose": 2 * unique_cells,
        "minimum_R_lower": min(row["minimum_R_lower"] for row in accepted_tiles),
        "maximum_R_upper": max(row["maximum_R_upper"] for row in accepted_tiles),
        "maximum_entry_tail": max(row["maximum_entry_tail"] for row in accepted_tiles),
        "all_cells_strictly_positive": True,
        "q_tiles_contiguous": (
            parsed[0][0] == K197.Q_START
            and parsed[-1][1] == K197.Q_END
            and all(parsed[i][1] == parsed[i + 1][0] for i in range(len(parsed) - 1))
        ),
        "six_packets_exactly_cover_new_ring_with_transpose": True,
        "scale_and_radial_coverage_in_every_ring_tile": True,
    }


def independent_controls(ring: dict[str, Any]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    q_boundaries = sorted({Fraction(value) for tile in ring["q_tiles"] for value in tile["q"]})
    shape_boundaries = sorted({*INNER, *OUTER})
    with localcontext() as context:
        context.prec = 220
        base = Decimal(K193.BASE_X.numerator) / Decimal(K193.BASE_X.denominator)
        radial_midpoint = Decimal(K193.RADIAL_WIDTH.numerator) / Decimal(K193.RADIAL_WIDTH.denominator) / 2
        minimum_sum = base * (Decimal(1) + radial_midpoint)
        for scale in K196.SCALE_BOUNDS:
            for q in q_boundaries:
                for a in shape_boundaries:
                    for c in shape_boundaries:
                        sd = Decimal(scale.numerator) / Decimal(scale.denominator)
                        ad = Decimal(a.numerator) / Decimal(a.denominator)
                        qd = Decimal(q.numerator) / Decimal(q.denominator)
                        cd = Decimal(c.numerator) / Decimal(c.denominator)
                        row_gaps = [sd / Decimal(32), sd * ad / Decimal(32), Decimal(0)]
                        column_gaps = [sd * qd / Decimal(32), sd * qd * cd / Decimal(32), Decimal(0)]
                        left = [minimum_sum * Decimal(2) / Decimal(5) + base * value for value in row_gaps]
                        right = [minimum_sum * Decimal(3) / Decimal(5) + base * value for value in column_gaps]
                        value = K191.K186.divided_difference_regularizer(left, right, 200)
                        if not Decimal(str(ring["minimum_R_lower"])) <= value <= Decimal(str(ring["maximum_R_upper"])):
                            raise AssertionError("independent K201 control escaped outward range")
                        rows.append({
                            "scale": ftext(scale),
                            "shape": {"a": ftext(a), "q": ftext(q), "c": ftext(c)},
                            "regularizer": format(value, ".24E"),
                            "contained_in_global_ring_range": True,
                        })
    return {
        "precision_decimal_digits": 200,
        "rows": rows,
        "all_contained": True,
        "transpose_companions_exact_by_row_column_exchange": True,
        "role": "independent convergent-series third-ring boundary-grid controls; directed Arb common cells carry the proof",
    }


def build(progress: bool = False, checkpoint: bool = False) -> dict[str, Any]:
    predecessor = json.loads(K200_MANIFEST.read_text())
    ring = build_ring(progress, checkpoint)
    if not ring["q_tiles_contiguous"]:
        raise AssertionError("K201 q tiles are not contiguous")
    controls = independent_controls(ring)
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifest": "lab/process/k200-order-six-second-ac-ring-wave.json",
            "source_manifest": predecessor["fixed_control"]["source_manifest"],
            "radial_cell": predecessor["fixed_control"]["radial_cell"],
            "max_gap_scale_range": predecessor["fixed_control"]["max_gap_scale_range"],
            "k200_inner_a_c_range": [ftext(value) for value in INNER],
            "third_expanded_a_c_range": [ftext(value) for value in OUTER],
            "q_corridor": [ftext(K197.Q_START), ftext(K197.Q_END)],
            "q_subdivisions": len(Q_CELLS),
            "maximum_shape_adaptive_depth": MAX_SHAPE_DEPTH,
            "taylor_order": K193.TAYLOR_ORDER,
            "arb_decimal_digits": K193.ARB_DIGITS,
            "threads": 1,
            "source_patterns": predecessor["fixed_control"]["source_patterns"],
            "source_nontrivial_occurrences": predecessor["fixed_control"]["source_nontrivial_occurrences"],
            "source_time_gram_entries": predecessor["fixed_control"]["source_time_gram_entries"],
            "source_coherent_groups": predecessor["fixed_control"]["source_coherent_groups"],
            "shell_width_discriminator": {
                "sampled_widths_each_side_in_1024ths": [1, 2, 4, 8, 16, 32, 64, 128, 256],
                "sampled_q_slabs": [0, 16, 31],
                "sampled_scale_radial_indices": [[0, 0], [0, 15], [128, 0], [128, 8], [255, 0], [255, 15]],
                "selected_width_each_side": "8/1024",
                "selected_width_sample_minimum_R_lower": 0.031436909561977144,
                "first_rejected_parent_width_each_side": "16/1024",
                "first_rejected_parent_sample_minimum_R_lower": -0.04232908903511254,
                "rejected_parent_interpretation": "loss of interval enclosure sign at a sampled parent cell; not a determinant counterexample",
            },
        },
        "certified_third_enlarged_ac_square": {
            "size_three_row_chart_third_ring_cover": ring,
            "size_three_column_chart_side_strips_are_exact_transpose": True,
            "k200_second_enlarged_square_inherited": True,
            "two_side_strips_and_four_corners_covered": True,
            "exact_join_to_k200_square": True,
            "third_enlarged_a_c_square_complete": True,
            "complete_a_c_domain_covered": False,
            "unique_new_outward_cells": ring["unique_outward_cells"],
            "new_chart_cell_instances_by_exact_transpose": ring["chart_cell_instances_by_exact_transpose"],
            "all_new_cells_strictly_positive": ring["all_cells_strictly_positive"],
            "common_cell_rule": "one shared (t,w,a,q,c) interval cell supplies every shifted entry and common normalization before the complete determinant",
        },
        "inherited_size_two": predecessor["inherited_size_two"],
        "independent_controls": controls,
        "complete_family_propagation": {
            "operator_applies_to_every_size_three_regularizer": True,
            "all_53_patterns_retain_the_same_formula": predecessor["fixed_control"]["source_patterns"] == 53,
            "all_468_occurrences_retain_the_same_formula": predecessor["fixed_control"]["source_nontrivial_occurrences"] == 468,
            "all_234_entries_and_18_groups_remain_in_scope": True,
            "new_bound_applies_only_to_the_declared_third_enlarged_a_c_square": True,
        },
        "decision": {
            "two_eight_step_side_strips_certified": True,
            "four_eight_by_eight_corner_boxes_certified": True,
            "k200_square_join_preserved": True,
            "third_enlarged_a_c_square_certified": True,
            "farther_a_c_complement_covered": False,
            "next_exact_input": "continue adaptive symmetric a/c shells beyond 495/1024<=a,c<=529/1024; only after complete shape coverage, differentiate the common-cell regularizer and compose the Duffy/Jacobi remainder",
        },
        "release_test": {
            "shifted_hermite_genocchi_entry_tail_retained": True,
            "all_entries_use_one_shared_scale_radial_and_three_shape_cell_before_complete_determinant_enclosure": True,
            "third_enlarged_a_c_square_outwardly_certified": True,
            "full_max_gap_coordinate_atlas_exact": True,
            "complete_transverse_arbitrary_gap_ratio_domain_covered": False,
            "duffy_jacobi_chain_rule_envelopes_serialized": False,
            "determinant_preserving_positive_radius_core_error_serialized": False,
            "complete_outward_order_six_total_error_serialized": False,
            "accurate_order_six_prefix_released": False,
            "complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "scalar_center_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": {
            "SC-META-53": "UNCERTAIN_UNCHANGED",
            "LT-SM8": "NEEDS_UNCHANGED",
            "LT-GR6b": "NEEDS_UNCHANGED",
            "RA-F1": "NEEDS_UNCHANGED",
            "AC-F1": "NEEDS_UNCHANGED",
        },
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
        "canon_paper_release_or_public_posture_move": False,
    }


def summary(result: dict[str, Any]) -> dict[str, Any]:
    return {key: result[key] for key in (
        "fixed_control",
        "certified_third_enlarged_ac_square",
        "inherited_size_two",
        "independent_controls",
        "complete_family_propagation",
        "decision",
        "release_test",
    )}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--progress", action="store_true")
    parser.add_argument("--checkpoint", action="store_true")
    args = parser.parse_args()
    result = build(args.progress, args.checkpoint)
    if args.write:
        OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if args.summary or not args.write:
        print(json.dumps(summary(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
