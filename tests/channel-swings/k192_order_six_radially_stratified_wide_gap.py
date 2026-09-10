#!/usr/bin/env python3
"""K192 radially stratified wide-gap extension of the K191 certificate.

K191 proves its normalized divided-difference Taylor enclosure uniformly on
``2^-200 <= x <= 1/4`` when each row and column spread is at most ``x/512``.
The high-radial cap controls that global radius.  This module keeps K191's
exact algebra and outward tail theorem, but certifies the much wider radius
``x/48`` on ``2^-200 <= x <= 1/8``.  The union is an outward stratified
certificate, not arbitrary gap-ratio coverage or a cubature remainder.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K191_PATH = ROOT / "tests/channel-swings/k191_order_six_near_coalescent_taylor_box.py"
K191_MANIFEST = ROOT / "lab/process/k191-order-six-near-coalescent-taylor-box-wave.json"
OUTPUT = ROOT / "lab/process/k192-order-six-radially-stratified-wide-gap-wave.json"

LOW_RADIAL_FLOOR_POWER = 200
LOW_RADIAL_CAP_POWER = 3
LOW_RADIAL_CAP = Fraction(1, 8)
WIDE_GAP_RELATIVE_RADIUS = Fraction(1, 48)
REJECTED_GAP_RELATIVE_RADIUS = Fraction(1, 32)
REJECTED_CELL_BASE = Fraction(31, 256)
REJECTED_CELL_UPPER = Fraction(1, 8)
REJECTED_RADIAL_WIDTH_BOUND = Fraction(1, 31)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K191 = load_module("k191", K191_PATH)


def reset_k191(radius: Fraction) -> None:
    """Select one exact radius and clear every cache that depends on it."""

    K191.GAP_RELATIVE_RADIUS = radius
    K191.RADIAL_LOW_POWER = LOW_RADIAL_FLOOR_POWER
    K191.RADIAL_HIGH_POWER = LOW_RADIAL_CAP_POWER
    K191.monomial_dd_bounds.cache_clear()
    K191.cauchy_linear_coefficients.cache_clear()


def rejected_candidate_control() -> dict[str, Any]:
    """Record a baseline-first failure of the next coarse uniform radius."""

    reset_k191(REJECTED_GAP_RELATIVE_RADIUS)
    rejected = False
    message = ""
    try:
        K191.cell_certificate(
            REJECTED_CELL_BASE,
            REJECTED_CELL_UPPER,
            3,
            REJECTED_RADIAL_WIDTH_BOUND,
        )
    except AssertionError as exc:
        rejected = True
        message = str(exc)
    if not rejected:
        raise AssertionError("the registered 1/32 size-three negative control unexpectedly certified")
    return {
        "candidate_gap_radius": K191.fraction_text(REJECTED_GAP_RELATIVE_RADIUS),
        "size": 3,
        "cell_base_x": K191.fraction_text(REJECTED_CELL_BASE),
        "cell_upper_x": K191.fraction_text(REJECTED_CELL_UPPER),
        "radial_width_bound": K191.fraction_text(REJECTED_RADIAL_WIDTH_BOUND),
        "strict_positive_cell_rejected": True,
        "exception": message,
        "role": "pre-registered scale control only; it does not prove 1/48 maximal",
    }


def noncoalescent_face_scaffold() -> dict[str, Any]:
    """Bank the exact face topology and a point control for the next chart.

    This deliberately stops before an outward shifted-Taylor certificate.  It
    proves that the Cauchy normalization is regular on arbitrary face centers,
    enumerates every nonempty size-three active-gap mask, and checks generic
    noncoalescent Bessel values independently.  The missing object is thereby
    narrowed to a shifted Hermite--Genocchi/Taylor tail evaluator.
    """

    labels = ("r0", "r1", "c0", "c1")
    centers = (Fraction(1, 32), Fraction(1, 64), Fraction(1, 40), Fraction(1, 80))
    masks = []
    for mask in range(1, 1 << len(labels)):
        masks.append(
            {
                "active": [labels[index] for index in range(len(labels)) if mask & (1 << index)],
                "center": {
                    labels[index]: K191.fraction_text(centers[index] if mask & (1 << index) else Fraction(0))
                    for index in range(len(labels))
                },
            }
        )

    exact_face_controls = {}
    for size, relevant_labels in ((2, ("r0", "c0")), (3, labels)):
        expressions = K191.cauchy_dd_matrix(size)
        relevant_masks = [
            row for row in masks
            if row["active"] and all(label in relevant_labels for label in row["active"])
        ]
        passed = 0
        for row in relevant_masks:
            substitutions = {
                K191.W: K191.sp.Rational(1, 64),
                K191.R0: K191.sp.Rational(row["center"]["r0"]),
                K191.R1: K191.sp.Rational(row["center"]["r1"]),
                K191.C0: K191.sp.Rational(row["center"]["c0"]),
                K191.C1: K191.sp.Rational(row["center"]["c1"]),
            }
            matrix = K191.sp.Matrix(
                [[K191.sp.cancel(value.subs(substitutions)) for value in matrix_row] for matrix_row in expressions]
            )
            nodes_r = K191.row_nodes(size)
            nodes_c = K191.column_nodes(size)
            product = K191.sp.prod(
                1 + substitutions[K191.W] + node_r.subs(substitutions) + node_c.subs(substitutions)
                for node_r in nodes_r for node_c in nodes_c
            )
            if K191.sp.cancel(matrix.det(method="domain-ge") * product) != 1:
                raise AssertionError("noncoalescent Cauchy face control failed")
            passed += 1
        exact_face_controls[str(size)] = {
            "checked": len(relevant_masks),
            "passed": passed,
        }

    x_fraction = Fraction(31, 256)
    x = Decimal(x_fraction.numerator) / Decimal(x_fraction.denominator)
    left_minimum = x * Decimal(2) / 5
    right_minimum = x * Decimal(3) / 5
    controls = []
    for size, row_offsets, column_offsets in (
        (2, (Fraction(1, 32), Fraction(0)), (Fraction(1, 40), Fraction(0))),
        (
            3,
            (Fraction(1, 32), Fraction(1, 64), Fraction(0)),
            (Fraction(1, 40), Fraction(1, 80), Fraction(0)),
        ),
    ):
        left = [
            left_minimum + x * Decimal(offset.numerator) / Decimal(offset.denominator)
            for offset in row_offsets
        ]
        right = [
            right_minimum + x * Decimal(offset.numerator) / Decimal(offset.denominator)
            for offset in column_offsets
        ]
        with localcontext() as context:
            context.prec = 220
            value = K191.K186.divided_difference_regularizer(left, right, 200)
        if not value > 0:
            raise AssertionError("generic noncoalescent point control lost positivity")
        controls.append(
            {
                "size": size,
                "base_x": K191.fraction_text(x_fraction),
                "row_offsets": [K191.fraction_text(value) for value in row_offsets],
                "column_offsets": [K191.fraction_text(value) for value in column_offsets],
                "regularizer": format(value, ".24E"),
                "strictly_positive": True,
            }
        )

    return {
        "pure_cauchy_normalization_exact_face_controls": exact_face_controls,
        "size_three_nonempty_active_gap_masks": masks,
        "size_three_face_mask_count": len(masks),
        "generic_noncoalescent_point_controls": controls,
        "coalescent_hull_candidate_1_over_32_rejected": True,
        "shifted_taylor_entry_tail_serialized": False,
        "exact_missing_operator": "outward shifted Hermite--Genocchi divided-difference Taylor entries with a common face-center dependency model and determinant-level Cauchy cofactors",
        "role": "exact face-atlas scaffold and failure localization; not an outward noncoalescent box certificate",
    }


def build() -> dict[str, Any]:
    predecessor = json.loads(K191_MANIFEST.read_text())
    rejected = rejected_candidate_control()
    face_scaffold = noncoalescent_face_scaffold()
    reset_k191(WIDE_GAP_RELATIVE_RADIUS)
    by_size, bands = K191.adaptive_radial_certificates()

    for size in (2, 3):
        cells = by_size[size]
        if Fraction(cells[0]["base_x"]) != Fraction(1, 2**LOW_RADIAL_FLOOR_POWER):
            raise AssertionError("wide-gap radial floor mismatch")
        if Fraction(cells[-1]["upper_x"]) != LOW_RADIAL_CAP:
            raise AssertionError("wide-gap radial cap mismatch")

    source_patterns = predecessor["fixed_control"]["source_patterns"]
    source_occurrences = predecessor["fixed_control"]["source_nontrivial_occurrences"]
    direct = K191.direct_controls(by_size)
    predecessor_sizes = predecessor["outward_certificate"]["sizes"]
    high_cap_cells = {
        str(size): [
            cell
            for cell in predecessor_sizes[str(size)]
            if Fraction(cell["base_x"]) >= LOW_RADIAL_CAP
        ]
        for size in (2, 3)
    }
    if any(not cells for cells in high_cap_cells.values()):
        raise AssertionError("K191 high-radial cap cells are missing")
    if any(Fraction(cells[0]["base_x"]) != LOW_RADIAL_CAP for cells in high_cap_cells.values()):
        raise AssertionError("K191 high-radial cap does not begin at 1/8")
    if any(Fraction(cells[-1]["upper_x"]) != Fraction(1, 4) for cells in high_cap_cells.values()):
        raise AssertionError("K191 high-radial cap does not end at 1/4")

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifest": "lab/process/k191-order-six-near-coalescent-taylor-box-wave.json",
            "source_manifest": predecessor["fixed_control"]["source_manifest"],
            "domain": predecessor["fixed_control"]["domain"],
            "low_radial_argument_range": "2^-200<=x<=1/8",
            "high_radial_argument_range": "1/8<=x<=1/4",
            "low_radial_maximum_row_spread_over_cell_base": K191.fraction_text(WIDE_GAP_RELATIVE_RADIUS),
            "low_radial_maximum_column_spread_over_cell_base": K191.fraction_text(WIDE_GAP_RELATIVE_RADIUS),
            "high_radial_maximum_row_spread_over_cell_base": predecessor["fixed_control"]["maximum_row_spread_over_cell_base"],
            "high_radial_maximum_column_spread_over_cell_base": predecessor["fixed_control"]["maximum_column_spread_over_cell_base"],
            "taylor_order": K191.TAYLOR_ORDER,
            "arb_decimal_digits": K191.ARB_DIGITS,
            "threads": 1,
            "source_patterns": source_patterns,
            "source_nontrivial_occurrences": source_occurrences,
            "source_time_gram_entries": predecessor["fixed_control"]["source_time_gram_entries"],
            "source_coherent_groups": predecessor["fixed_control"]["source_coherent_groups"],
        },
        "retained_theorem": {
            "normalized_identity": predecessor["normalized_identity"],
            "taylor_theorem": {
                **predecessor["taylor_theorem"],
                "eta": "cell-specific radial width plus twice 1/48 on the low-radial stratum; global maximum 1/6",
            },
            "algebra_or_tail_rule_changed": False,
            "radial_gap_domain_stratified_before_new_algebra": True,
        },
        "low_radial_wide_gap_certificate": {
            "radial_cells": len(by_size[2]),
            "dyadic_band_subdivisions": bands,
            "sizes": {str(size): by_size[size] for size in (2, 3)},
            "all_cells_strictly_positive": True,
            "minimum_R_lower_by_size": {
                str(size): min(cell["R_lower"] for cell in by_size[size])
                for size in (2, 3)
            },
            "maximum_R_upper_by_size": {
                str(size): max(cell["R_upper"] for cell in by_size[size])
                for size in (2, 3)
            },
            "maximum_entry_tail_radius_by_size": {
                str(size): max(cell["maximum_entry_tail_radius"] for cell in by_size[size])
                for size in (2, 3)
            },
        },
        "retained_high_radial_certificate": {
            "source": "K191 outward_certificate cells restricted to base_x>=1/8",
            "sizes": high_cap_cells,
            "all_cells_strictly_positive": True,
        },
        "stratified_union": {
            "radial_range_has_no_gap": True,
            "wide_gap_radius_gain_factor": "32/3",
            "low_radial_certificate_new": True,
            "high_radial_certificate_reused_exactly": True,
            "all_53_patterns_covered_conditionally_on_the_stratified_spread_rule": source_patterns == 53,
            "all_468_occurrences_covered_conditionally_on_the_stratified_spread_rule": source_occurrences == 468,
            "all_234_entries_and_18_groups_remain_in_scope": True,
        },
        "independent_controls": direct,
        "rejected_candidate_control": rejected,
        "noncoalescent_face_scaffold": face_scaffold,
        "decision": {
            "radially_stratified_wide_gap_region_certified": True,
            "arbitrary_gap_ratio_coverage_complete": False,
            "certified_region": "2^-200<=x<=1/8 with row/column spread<=1/48 of the local cell base, union 1/8<=x<=1/4 with K191 row/column spread<=1/512",
            "residual_region": "spread>1/48 on x<=1/8, or spread>1/512 on x>=1/8, within the K188 positive-radius core",
            "noncoalescent_face_topology_banked": True,
            "noncoalescent_face_recentering_required_next": True,
            "duffy_jacobi_composition_released": False,
            "next_exact_input": "construct noncoalescent face charts for the residual maximum-gap strata, expand the normalized divided-difference matrix about each face center with outward tails, and cover every K186 pattern before Duffy/Jacobi composition",
        },
        "release_test": {
            "normalized_divided_difference_identity_banked": True,
            "analytic_entry_tail_bound_banked": True,
            "radially_stratified_wide_gap_cells_serialized": True,
            "complete_radial_argument_range_retained": True,
            "all_53_patterns_propagated_on_certified_union": True,
            "all_468_occurrences_propagated_on_certified_union": True,
            "arbitrary_gap_ratio_domain_covered": False,
            "noncoalescent_face_atlas_serialized": False,
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
    low = result["low_radial_wide_gap_certificate"]
    high = result["retained_high_radial_certificate"]
    return {
        "fixed_control": result["fixed_control"],
        "retained_theorem": result["retained_theorem"],
        "low_radial_wide_gap_certificate": {
            key: value for key, value in low.items() if key != "sizes"
        },
        "retained_high_radial_cell_counts": {
            size: len(cells) for size, cells in high["sizes"].items()
        },
        "stratified_union": result["stratified_union"],
        "independent_controls": result["independent_controls"],
        "rejected_candidate_control": result["rejected_candidate_control"],
        "decision": result["decision"],
        "release_test": result["release_test"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if args.summary or not args.write:
        print(json.dumps(summary(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
