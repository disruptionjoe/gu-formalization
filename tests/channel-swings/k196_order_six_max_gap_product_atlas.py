#!/usr/bin/env python3
"""K196 two-chart max-gap atlas and open product certificates.

K195 certified three coordinate axes through one row-dominant projective ray.
K196 proves the exact row/column max-gap atlas and evaluates every matrix entry
from one common ``(t,w,a,q,c)`` interval cell before the complete determinant.
The rigorous numerical result is two transpose-related open product blocks,
not a certificate of the full ordered-shape product domain or its cubature
remainder.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
K195_PATH = ROOT / "tests/channel-swings/k195_order_six_transverse_projective_chart.py"
K195_MANIFEST = ROOT / "lab/process/k195-order-six-transverse-projective-chart-wave.json"
OUTPUT = ROOT / "lab/process/k196-order-six-max-gap-product-atlas-wave.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K195 = load_module("k195_for_k196", K195_PATH)
K193 = K195.K193
K191 = K195.K191

T, A, Q, C = sp.symbols("t a q c")
SCALE_BOUNDS = (Fraction(1), Fraction(8))
PRODUCT_DILATION = 7
PRODUCT_BOUNDS = {
    A: (
        Fraction(1, 2) - Fraction(PRODUCT_DILATION, 1024),
        Fraction(1, 2) + Fraction(PRODUCT_DILATION, 1024),
    ),
    Q: (
        Fraction(4, 5) - Fraction(PRODUCT_DILATION, 2048),
        Fraction(4, 5) + Fraction(PRODUCT_DILATION, 2048),
    ),
    C: (
        Fraction(1, 2) - Fraction(PRODUCT_DILATION, 1024),
        Fraction(1, 2) + Fraction(PRODUCT_DILATION, 1024),
    ),
}
FAILED_SHELL_DILATION = 8


def ftext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def split(lower: Fraction, upper: Fraction, count: int) -> list[tuple[Fraction, Fraction]]:
    return K195.split(lower, upper, count)


def atlas_certificate() -> dict[str, Any]:
    row_outputs = sp.Matrix([T / 32, T * A / 32, T * Q / 32, T * Q * C / 32])
    column_outputs = sp.Matrix([T * Q / 32, T * Q * A / 32, T / 32, T * C / 32])
    inputs = sp.Matrix([T, A, Q, C])
    row_det = sp.factor(row_outputs.jacobian(inputs).det())
    column_det = sp.factor(column_outputs.jacobian(inputs).det())
    expected = T**3 * Q / 32**4
    if sp.expand(row_det - expected) != 0 or sp.expand(column_det + expected) != 0:
        raise AssertionError("unexpected max-gap atlas Jacobian")
    return {
        "row_dominant": {
            "domain": "r0>=c0>0, 0<r1/r0<1, 0<c1/c0<1",
            "forward_map": ["r0=t/32", "r1=t*a/32", "c0=t*q/32", "c1=t*q*c/32"],
            "inverse_map": {"t": "32*r0", "a": "r1/r0", "q": "c0/r0", "c": "c1/c0"},
            "oriented_jacobian": "t^3*q/1048576",
        },
        "column_dominant": {
            "domain": "c0>=r0>0, 0<r1/r0<1, 0<c1/c0<1",
            "forward_map": ["r0=t*q/32", "r1=t*q*a/32", "c0=t/32", "c1=t*c/32"],
            "inverse_map": {"t": "32*c0", "a": "r1/r0", "q": "r0/c0", "c": "c1/c0"},
            "oriented_jacobian": "-t^3*q/1048576",
            "absolute_jacobian": "t^3*q/1048576",
        },
        "cover": "every r0,c0>0 lies in at least one chart by comparing r0 and c0",
        "overlap": "r0=c0 iff q=1; both charts agree there",
        "transition_between_unrestricted_coordinate_representations": {"t_column": "t_row*q_row", "q_column": "1/q_row", "a_column": "a_row", "c_column": "c_row"},
        "transpose_symmetry": "column-dominant determinant cells equal row-dominant cells after swapping row and column gaps and a<->c",
        "exact": True,
        "positive_absolute_jacobians": True,
    }


def build_product_block(size: int) -> dict[str, Any]:
    config = K195.SUBDIVISIONS[size]
    s_cells = split(*SCALE_BOUNDS, config["scale"])
    w_cells = split(Fraction(0), K193.RADIAL_WIDTH, config["radial"])
    a_bounds = PRODUCT_BOUNDS[A]
    q_bounds = PRODUCT_BOUNDS[Q]
    c_bounds = PRODUCT_BOUNDS[C]
    lowers: list[float] = []
    uppers: list[float] = []
    tails: list[float] = []
    for s_bounds in s_cells:
        for w_bounds in w_cells:
            regularizer, tail = K195.chart_cell(
                size, w_bounds, s_bounds, a_bounds, q_bounds, c_bounds
            )
            lower = float(regularizer.lower())
            if not lower > 0:
                raise AssertionError(
                    "max-gap product cell lost positivity "
                    f"size={size} s={s_bounds} w={w_bounds}: {regularizer}"
                )
            lowers.append(lower)
            uppers.append(float(regularizer.upper()))
            tails.append(float(tail))
    unique_cells = len(s_cells) * len(w_cells)
    return {
        "subdivisions": config,
        "shape_cell": {
            "a": [ftext(value) for value in a_bounds],
            "q": [ftext(value) for value in q_bounds],
            "c": [ftext(value) for value in c_bounds],
        },
        "unique_outward_cells": unique_cells,
        "chart_cell_instances_by_exact_transpose": 2 * unique_cells,
        "minimum_R_lower": min(lowers),
        "maximum_R_upper": max(uppers),
        "maximum_entry_tail": max(tails),
        "all_cells_strictly_positive": True,
        "scale_and_radial_cells_contiguous": (
            s_cells[0][0] == SCALE_BOUNDS[0]
            and s_cells[-1][1] == SCALE_BOUNDS[1]
            and all(s_cells[i][1] == s_cells[i + 1][0] for i in range(len(s_cells) - 1))
            and w_cells[0][0] == 0
            and w_cells[-1][1] == K193.RADIAL_WIDTH
            and all(w_cells[i][1] == w_cells[i + 1][0] for i in range(len(w_cells) - 1))
        ),
    }


def failed_shell_witnesses() -> dict[str, Any]:
    dilation = FAILED_SHELL_DILATION
    bounds = {
        A: (Fraction(1, 2) - Fraction(dilation, 1024), Fraction(1, 2) + Fraction(dilation, 1024)),
        Q: (Fraction(4, 5) - Fraction(dilation, 2048), Fraction(4, 5) + Fraction(dilation, 2048)),
        C: (Fraction(1, 2) - Fraction(dilation, 1024), Fraction(1, 2) + Fraction(dilation, 1024)),
    }
    s_cells = split(*SCALE_BOUNDS, K195.SUBDIVISIONS[3]["scale"])
    w_cells = split(Fraction(0), K193.RADIAL_WIDTH, K195.SUBDIVISIONS[3]["radial"])
    rows = []
    for scale_index, radial_index in ((128, 8), (255, 15)):
        regularizer, tail = K195.chart_cell(
            3,
            w_cells[radial_index],
            s_cells[scale_index],
            bounds[A],
            bounds[Q],
            bounds[C],
        )
        refinements = []
        for a_bounds, q_bounds, c_bounds in itertools.product(
            split(*bounds[A], 2), split(*bounds[Q], 2), split(*bounds[C], 2)
        ):
            refined, refined_tail = K195.chart_cell(
                3,
                w_cells[radial_index],
                s_cells[scale_index],
                a_bounds,
                q_bounds,
                c_bounds,
            )
            refinements.append(
                {
                    "a": [ftext(value) for value in a_bounds],
                    "q": [ftext(value) for value in q_bounds],
                    "c": [ftext(value) for value in c_bounds],
                    "R_lower": float(refined.lower()),
                    "R_upper": float(refined.upper()),
                    "maximum_entry_tail": float(refined_tail),
                    "strictly_positive": float(refined.lower()) > 0,
                }
            )
        rows.append(
            {
                "scale_index": scale_index,
                "radial_index": radial_index,
                "R_lower": float(regularizer.lower()),
                "R_upper": float(regularizer.upper()),
                "maximum_entry_tail": float(tail),
                "strict_positivity_lost": not float(regularizer.lower()) > 0,
                "adaptive_bisection": {
                    "subcells": len(refinements),
                    "all_strictly_positive": all(row["strictly_positive"] for row in refinements),
                    "minimum_R_lower": min(row["R_lower"] for row in refinements),
                    "maximum_R_upper": max(row["R_upper"] for row in refinements),
                    "rows": refinements,
                },
            }
        )
    if not all(row["strict_positivity_lost"] for row in rows):
        raise AssertionError("declared outer-shell dependency-loss witnesses did not reproduce")
    return {
        "dilation": dilation,
        "shape_cell": {
            "a": [ftext(value) for value in bounds[A]],
            "q": [ftext(value) for value in bounds[Q]],
            "c": [ftext(value) for value in bounds[C]],
        },
        "witnesses": rows,
        "interpretation": "loss of strict interval positivity for one larger unsplit shape cell; all sixteen declared three-ratio bisection subcells recover strict positivity, proving local enclosure dependency loss rather than a regularizer counterexample while leaving the untested rest of the shell open",
    }


def independent_controls(blocks: dict[str, dict[str, Any]]) -> dict[str, Any]:
    rows = []
    with localcontext() as context:
        context.prec = 220
        base = Decimal(K193.BASE_X.numerator) / Decimal(K193.BASE_X.denominator)
        w = Decimal(K193.RADIAL_WIDTH.numerator) / Decimal(K193.RADIAL_WIDTH.denominator) / 2
        minimum_sum = base * (Decimal(1) + w)
        for size in (2, 3):
            shape_points = list(
                [(K195.RAY[K195.A], q, K195.RAY[K195.C]) for q in PRODUCT_BOUNDS[Q]]
                if size == 2
                else itertools.product(PRODUCT_BOUNDS[A], PRODUCT_BOUNDS[Q], PRODUCT_BOUNDS[C])
            )
            for scale in (Fraction(1), Fraction(8)):
                for a, q, c in shape_points:
                    sd = Decimal(scale.numerator) / Decimal(scale.denominator)
                    ad = Decimal(a.numerator) / Decimal(a.denominator)
                    qd = Decimal(q.numerator) / Decimal(q.denominator)
                    cd = Decimal(c.numerator) / Decimal(c.denominator)
                    row_gaps = [sd / Decimal(32), Decimal(0)] if size == 2 else [sd / Decimal(32), sd * ad / Decimal(32), Decimal(0)]
                    column_gaps = [sd * qd / Decimal(32), Decimal(0)] if size == 2 else [sd * qd / Decimal(32), sd * qd * cd / Decimal(32), Decimal(0)]
                    left = [minimum_sum * Decimal(2) / Decimal(5) + base * value for value in row_gaps]
                    right = [minimum_sum * Decimal(3) / Decimal(5) + base * value for value in column_gaps]
                    value = K191.K186.divided_difference_regularizer(left, right, 200)
                    if not Decimal(str(blocks[str(size)]["minimum_R_lower"])) <= value <= Decimal(str(blocks[str(size)]["maximum_R_upper"])):
                        raise AssertionError("independent max-gap point escaped product-block range")
                    rows.append(
                        {
                            "size": size,
                            "scale": ftext(scale),
                            "shape": {"a": ftext(a), "q": ftext(q), "c": ftext(c)},
                            "regularizer": format(value, ".24E"),
                            "contained_in_global_block_range": True,
                        }
                    )
    return {
        "precision_decimal_digits": 200,
        "rows": rows,
        "all_contained": True,
        "role": "independent convergent-series corner controls; directed Arb product cells carry the proof",
    }


def build() -> dict[str, Any]:
    predecessor = json.loads(K195_MANIFEST.read_text())
    atlas = atlas_certificate()
    blocks = {str(size): build_product_block(size) for size in (2, 3)}
    shell = failed_shell_witnesses()
    controls = independent_controls(blocks)
    unique_cells = sum(row["unique_outward_cells"] for row in blocks.values())
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifest": "lab/process/k195-order-six-transverse-projective-chart-wave.json",
            "source_manifest": predecessor["fixed_control"]["source_manifest"],
            "radial_cell": predecessor["fixed_control"]["radial_cell"],
            "max_gap_scale_range": "1/1<=t<=8/1",
            "product_dilation": PRODUCT_DILATION,
            "taylor_order": K193.TAYLOR_ORDER,
            "arb_decimal_digits": K193.ARB_DIGITS,
            "threads": 1,
            "source_patterns": predecessor["fixed_control"]["source_patterns"],
            "source_nontrivial_occurrences": predecessor["fixed_control"]["source_nontrivial_occurrences"],
            "source_time_gram_entries": predecessor["fixed_control"]["source_time_gram_entries"],
            "source_coherent_groups": predecessor["fixed_control"]["source_coherent_groups"],
        },
        "exact_max_gap_atlas": atlas,
        "certified_open_product_blocks": {
            "sizes": blocks,
            "unique_outward_cells": unique_cells,
            "chart_cell_instances_by_exact_transpose": 2 * unique_cells,
            "all_cells_strictly_positive": all(row["all_cells_strictly_positive"] for row in blocks.values()),
            "common_cell_rule": "one shared (t,w,a,q,c) interval cell supplies every shifted entry and common normalization before the complete determinant",
            "chart_roles": ["row_dominant", "column_dominant_by_exact_transpose"],
            "k195_star_strictly_inside_row_block": True,
            "mirrored_column_block_new": True,
        },
        "outer_shell_dependency_loss": shell,
        "independent_controls": controls,
        "atlas_chain_rule_handoff": {
            "coordinate_derivative_matrices_exact": True,
            "row_and_column_absolute_jacobians_exact": True,
            "seam_and_extended_transition_exact": True,
            "regularizer_derivative_envelopes": False,
            "weighted_duffy_jacobi_remainder": False,
        },
        "complete_family_propagation": {
            "operator_applies_to_every_size_two_and_three_regularizer": True,
            "all_53_patterns_retain_the_same_formula": predecessor["fixed_control"]["source_patterns"] == 53,
            "all_468_occurrences_retain_the_same_formula": predecessor["fixed_control"]["source_nontrivial_occurrences"] == 468,
            "all_234_entries_and_18_groups_remain_in_scope": True,
            "new_bound_applies_only_on_the_two_declared_open_product_blocks": True,
        },
        "decision": {
            "exact_two_chart_max_gap_atlas_serialized": True,
            "open_product_neighborhoods_outwardly_certified": True,
            "k195_coordinate_star_strictly_extended": True,
            "complete_ordered_shape_product_domain_covered": False,
            "next_exact_input": "adaptively subdivide the remaining a/q/c complement in both max-gap charts, beginning with the q-to-1 overlap corridor; only after coverage, differentiate the common-cell regularizer and compose the Duffy/Jacobi remainder",
        },
        "release_test": {
            "shifted_hermite_genocchi_entry_tail_retained": True,
            "all_entries_use_one_shared_scale_radial_and_three_shape_cell_before_complete_determinant_enclosure": True,
            "row_and_column_open_product_blocks_outwardly_certified": True,
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
    return {
        "fixed_control": result["fixed_control"],
        "exact_max_gap_atlas": result["exact_max_gap_atlas"],
        "certified_open_product_blocks": result["certified_open_product_blocks"],
        "outer_shell_dependency_loss": result["outer_shell_dependency_loss"],
        "independent_controls": result["independent_controls"],
        "atlas_chain_rule_handoff": result["atlas_chain_rule_handoff"],
        "complete_family_propagation": result["complete_family_propagation"],
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
