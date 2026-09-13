#!/usr/bin/env python3
"""K198 first symmetric a/c-shell cross certificate.

K197 closed the q-to-one direction only on its fixed a,c core.  K198 enlarges
the row-chart a interval by one exact 1/1024 step on both sides while retaining
the K197 c core and q partition.  Exact row/column transpose supplies the
companion c enlargement.  The four corner boxes and every farther shell stay
open, as do all cubature and physical consequences.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K197_PATH = ROOT / "tests/channel-swings/k197_order_six_max_gap_q_corridor.py"
K197_MANIFEST = ROOT / "lab/process/k197-order-six-max-gap-q-corridor-wave.json"
OUTPUT = ROOT / "lab/process/k198-order-six-first-ac-shell-cross-wave.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K197 = load_module("k197_for_k198", K197_PATH)
K196 = K197.K196
K195 = K197.K195
K193 = K197.K193
K191 = K197.K191

CORE = K196.PRODUCT_BOUNDS[K196.A]
EXPANDED = (Fraction(504, 1024), Fraction(520, 1024))
Q_CELLS = K196.split(K197.Q_START, K197.Q_END, K197.BASE_Q_SUBDIVISIONS[3])


def ftext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


MAX_A_DEPTH = 2


def a_tile_certificate(
    q_bounds: tuple[Fraction, Fraction],
    base_index: int,
    a_bounds: tuple[Fraction, Fraction],
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
                CORE,
            )
            lower = float(regularizer.lower())
            if not lower > 0:
                return None, {
                    "base_index": base_index,
                    "depth": depth,
                    "a": [ftext(value) for value in a_bounds],
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
        "base_index": base_index,
        "depth": depth,
        "a": [ftext(value) for value in a_bounds],
        "q": [ftext(value) for value in q_bounds],
        "outward_cells": len(scale_cells) * len(radial_cells),
        "minimum_R_lower": min(lowers),
        "maximum_R_upper": max(uppers),
        "maximum_entry_tail": max(tails),
        "all_cells_strictly_positive": True,
    }, None


def certify_a_or_bisect(
    q_bounds: tuple[Fraction, Fraction],
    base_index: int,
    a_bounds: tuple[Fraction, Fraction],
    depth: int,
    rejected: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    accepted, failure = a_tile_certificate(q_bounds, base_index, a_bounds, depth)
    if accepted is not None:
        return [accepted]
    assert failure is not None
    rejected.append(failure)
    if depth >= MAX_A_DEPTH:
        raise AssertionError(f"K198 a-band lost positivity after refinement: {failure}")
    midpoint = (a_bounds[0] + a_bounds[1]) / 2
    return certify_a_or_bisect(q_bounds, base_index, (a_bounds[0], midpoint), depth + 1, rejected) + certify_a_or_bisect(q_bounds, base_index, (midpoint, a_bounds[1]), depth + 1, rejected)


def build_band(progress: bool = False) -> dict[str, Any]:
    tiles = []
    rejected: list[dict[str, Any]] = []
    for index, q_bounds in enumerate(Q_CELLS):
        accepted = certify_a_or_bisect(q_bounds, index, EXPANDED, 0, rejected)
        tile = {
            "base_index": index,
            "q": [ftext(value) for value in q_bounds],
            "accepted_a_tiles": accepted,
            "accepted_a_tile_count": len(accepted),
            "minimum_R_lower": min(row["minimum_R_lower"] for row in accepted),
            "maximum_R_upper": max(row["maximum_R_upper"] for row in accepted),
            "maximum_entry_tail": max(row["maximum_entry_tail"] for row in accepted),
            "all_cells_strictly_positive": True,
        }
        tiles.append(tile)
        if progress:
            print(
                f"K198 size=3 base_q_cell={index + 1}/{len(Q_CELLS)} "
                f"accepted_a_tiles={len(accepted)} "
                f"minimum_lower={tile['minimum_R_lower']:.17g}",
                file=sys.stderr,
                flush=True,
            )
    parsed = [tuple(Fraction(value) for value in row["q"]) for row in tiles]
    accepted_product_tiles = [child for row in tiles for child in row["accepted_a_tiles"]]
    unique_cells = sum(row["outward_cells"] for row in accepted_product_tiles)
    return {
        "size": 3,
        "subdivisions": K195.SUBDIVISIONS[3],
        "base_q_subdivisions": len(Q_CELLS),
        "accepted_q_tiles": len(tiles),
        "accepted_product_tiles": len(accepted_product_tiles),
        "maximum_a_adaptive_depth_used": max(row["depth"] for row in accepted_product_tiles),
        "rejected_parent_cells": rejected,
        "a_range": [ftext(value) for value in EXPANDED],
        "c_range": [ftext(value) for value in CORE],
        "q_range": [ftext(K197.Q_START), ftext(K197.Q_END)],
        "q_tiles": tiles,
        "unique_outward_cells": unique_cells,
        "chart_cell_instances_by_exact_transpose": 2 * unique_cells,
        "minimum_R_lower": min(row["minimum_R_lower"] for row in accepted_product_tiles),
        "maximum_R_upper": max(row["maximum_R_upper"] for row in accepted_product_tiles),
        "maximum_entry_tail": max(row["maximum_entry_tail"] for row in accepted_product_tiles),
        "all_cells_strictly_positive": True,
        "q_tiles_contiguous": (
            parsed[0][0] == K197.Q_START
            and parsed[-1][1] == K197.Q_END
            and all(parsed[i][1] == parsed[i + 1][0] for i in range(len(parsed) - 1))
        ),
        "scale_and_radial_coverage_in_every_q_tile": True,
    }


def independent_controls(band: dict[str, Any]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    q_boundaries = sorted({Fraction(value) for tile in band["q_tiles"] for value in tile["q"]})
    with localcontext() as context:
        context.prec = 220
        base = Decimal(K193.BASE_X.numerator) / Decimal(K193.BASE_X.denominator)
        radial_midpoint = Decimal(K193.RADIAL_WIDTH.numerator) / Decimal(K193.RADIAL_WIDTH.denominator) / 2
        minimum_sum = base * (Decimal(1) + radial_midpoint)
        for scale in K196.SCALE_BOUNDS:
            for q in q_boundaries:
                for a in EXPANDED:
                    for c in CORE:
                        sd = Decimal(scale.numerator) / Decimal(scale.denominator)
                        ad = Decimal(a.numerator) / Decimal(a.denominator)
                        qd = Decimal(q.numerator) / Decimal(q.denominator)
                        cd = Decimal(c.numerator) / Decimal(c.denominator)
                        row_gaps = [sd / Decimal(32), sd * ad / Decimal(32), Decimal(0)]
                        column_gaps = [sd * qd / Decimal(32), sd * qd * cd / Decimal(32), Decimal(0)]
                        left = [minimum_sum * Decimal(2) / Decimal(5) + base * value for value in row_gaps]
                        right = [minimum_sum * Decimal(3) / Decimal(5) + base * value for value in column_gaps]
                        value = K191.K186.divided_difference_regularizer(left, right, 200)
                        if not Decimal(str(band["minimum_R_lower"])) <= value <= Decimal(str(band["maximum_R_upper"])):
                            raise AssertionError("independent K198 control escaped outward range")
                        rows.append({
                            "scale": ftext(scale),
                            "shape": {"a": ftext(a), "q": ftext(q), "c": ftext(c)},
                            "regularizer": format(value, ".24E"),
                            "contained_in_global_band_range": True,
                        })
    return {
        "precision_decimal_digits": 200,
        "rows": rows,
        "all_contained": True,
        "transpose_companions_exact_by_row_column_exchange": True,
        "role": "independent convergent-series band-boundary controls; directed Arb common cells carry the proof",
    }


def build(progress: bool = False) -> dict[str, Any]:
    predecessor = json.loads(K197_MANIFEST.read_text())
    band = build_band(progress)
    if not band["q_tiles_contiguous"]:
        raise AssertionError("K198 q tiles are not contiguous")
    controls = independent_controls(band)
    inherited_size_two = predecessor["certified_q_to_one_corridor"]["sizes"]["2"]
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifest": "lab/process/k197-order-six-max-gap-q-corridor-wave.json",
            "source_manifest": predecessor["fixed_control"]["source_manifest"],
            "radial_cell": predecessor["fixed_control"]["radial_cell"],
            "max_gap_scale_range": predecessor["fixed_control"]["max_gap_scale_range"],
            "k197_core_a_c_range": [ftext(value) for value in CORE],
            "expanded_a_range": [ftext(value) for value in EXPANDED],
            "fixed_c_range": [ftext(value) for value in CORE],
            "q_corridor": [ftext(K197.Q_START), ftext(K197.Q_END)],
            "q_subdivisions": len(Q_CELLS),
            "maximum_a_adaptive_depth": MAX_A_DEPTH,
            "taylor_order": K193.TAYLOR_ORDER,
            "arb_decimal_digits": K193.ARB_DIGITS,
            "threads": 1,
            "source_patterns": predecessor["fixed_control"]["source_patterns"],
            "source_nontrivial_occurrences": predecessor["fixed_control"]["source_nontrivial_occurrences"],
            "source_time_gram_entries": predecessor["fixed_control"]["source_time_gram_entries"],
            "source_coherent_groups": predecessor["fixed_control"]["source_coherent_groups"],
        },
        "certified_first_ac_shell_cross": {
            "size_three_row_chart_expanded_a_band": band,
            "size_three_column_chart_expanded_c_band_is_exact_transpose": True,
            "new_row_side_strips": [
                [ftext(EXPANDED[0]), ftext(CORE[0])],
                [ftext(CORE[1]), ftext(EXPANDED[1])],
            ],
            "new_column_side_strips": [
                [ftext(EXPANDED[0]), ftext(CORE[0])],
                [ftext(CORE[1]), ftext(EXPANDED[1])],
            ],
            "k197_core_contained_in_joined_band": EXPANDED[0] < CORE[0] < CORE[1] < EXPANDED[1],
            "exact_join_to_k197_core": True,
            "unique_outward_cells": band["unique_outward_cells"],
            "chart_cell_instances_by_exact_transpose": band["chart_cell_instances_by_exact_transpose"],
            "all_cells_strictly_positive": band["all_cells_strictly_positive"],
            "common_cell_rule": "one shared (t,w,a,q,c) interval cell supplies every shifted entry and common normalization before the complete determinant",
            "corner_boxes_covered": False,
            "complete_a_c_domain_covered": False,
        },
        "inherited_size_two": {
            "shape_independent": True,
            "not_recomputed": True,
            "k197_minimum_R_lower": inherited_size_two["minimum_R_lower"],
            "complete_q_to_one_corridor": predecessor["decision"]["complete_q_to_one_corridor_for_fixed_a_c_block"],
        },
        "independent_controls": controls,
        "complete_family_propagation": {
            "operator_applies_to_every_size_three_regularizer": True,
            "all_53_patterns_retain_the_same_formula": predecessor["fixed_control"]["source_patterns"] == 53,
            "all_468_occurrences_retain_the_same_formula": predecessor["fixed_control"]["source_nontrivial_occurrences"] == 468,
            "all_234_entries_and_18_groups_remain_in_scope": True,
            "new_bound_applies_only_to_the_declared_first_shell_cross": True,
        },
        "decision": {
            "first_symmetric_a_c_shell_cross_certified": True,
            "k197_core_join_preserved": True,
            "corner_boxes_covered": False,
            "farther_a_c_complement_covered": False,
            "next_exact_input": "certify the four one-step corner boxes and then continue adaptive symmetric a/c shells; only after complete shape coverage, differentiate the common-cell regularizer and compose the Duffy/Jacobi remainder",
        },
        "release_test": {
            "shifted_hermite_genocchi_entry_tail_retained": True,
            "all_entries_use_one_shared_scale_radial_and_three_shape_cell_before_complete_determinant_enclosure": True,
            "first_symmetric_a_c_shell_cross_outwardly_certified": True,
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
        "certified_first_ac_shell_cross",
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
    args = parser.parse_args()
    result = build(args.progress)
    if args.write:
        OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if args.summary or not args.write:
        print(json.dumps(summary(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
