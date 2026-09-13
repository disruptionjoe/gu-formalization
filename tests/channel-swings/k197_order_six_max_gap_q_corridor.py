#!/usr/bin/env python3
"""K197 complete q-to-1 max-gap overlap-corridor certificate.

K196 proved the exact two-chart atlas and two local determinant-positive
product blocks. K197 holds K196's certified ``a,c`` interval fixed and covers
the remaining dominant-chart balance ratio from the upper K196 face through
``q=1``. Every accepted cell feeds one shared ``(t,w,a,q,c)`` interval into
all shifted entries, the common normalization, and then the complete
determinant. The remaining ``a,c`` complement and every cubature consequence
stay open.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K196_PATH = ROOT / "tests/channel-swings/k196_order_six_max_gap_product_atlas.py"
K196_MANIFEST = ROOT / "lab/process/k196-order-six-max-gap-product-atlas-wave.json"
OUTPUT = ROOT / "lab/process/k197-order-six-max-gap-q-corridor-wave.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K196 = load_module("k196_for_k197", K196_PATH)
K195 = K196.K195
K193 = K196.K193
K191 = K196.K191

Q_START = K196.PRODUCT_BOUNDS[K196.Q][1]
Q_END = Fraction(1)
BASE_Q_SUBDIVISIONS = {2: 1, 3: 32}
MAX_ADAPTIVE_DEPTH = 3


@lru_cache(maxsize=None)
def compiled_interval(expression):
    """Compile K191's exact interval-expression tree once per expression.

    K191's evaluator recursively inspects every SymPy node on every cell.  The
    K197 corridor has 132,096 cells, so this preserves the identical ordered
    Arb operations while moving that structural inspection out of the hot
    loop.  Constants are constructed once at the configured Arb precision.
    """

    constants: list[Any] = []

    def source(node) -> str:
        if node.is_Number:
            index = len(constants)
            constants.append(K195.arb(str(node)))
            return f"constants[{index}]"
        if node.is_Symbol:
            index = len(constants)
            constants.append(node)
            return f"values[constants[{index}]]"
        if node.is_Add:
            return "(" + " + ".join(["zero", *(source(arg) for arg in node.args)]) + ")"
        if node.is_Mul:
            return "(" + " * ".join(["one", *(source(arg) for arg in node.args)]) + ")"
        if node.is_Pow:
            base, exponent = node.args
            if not exponent.is_Integer:
                raise ValueError("only integer powers occur in K197 expressions")
            return f"({source(base)} ** {int(exponent)})"
        raise TypeError(f"unsupported SymPy node {type(node).__name__}")

    body = source(expression)
    evaluator = eval(
        f"lambda values, constants, zero, one: {body}",
        {"__builtins__": {}},
    )
    zero = K195.arb(0)
    one = K195.arb(1)
    frozen_constants = tuple(constants)
    return lambda values: evaluator(values, frozen_constants, zero, one)


def fast_shifted_entry_enclosure(
    size: int,
    row: int,
    column: int,
    w_bounds: tuple[Fraction, Fraction],
    s_bounds: tuple[Fraction, Fraction],
    a_bounds: tuple[Fraction, Fraction],
    q_bounds: tuple[Fraction, Fraction],
    c_bounds: tuple[Fraction, Fraction],
):
    gaps = K195.primitive_gap_bounds(size, s_bounds, a_bounds, q_bounds, c_bounds)
    independent = {K191.W: w_bounds, **gaps}
    lower, upper = K193.entry_argument_bounds(size, row, column, independent)
    midpoint = (lower + upper) / 2
    shift = Fraction(round(midpoint * 512), 512)
    radius = max(shift - lower, upper - shift)
    values = K195.chart_values(w_bounds, s_bounds, a_bounds, q_bounds, c_bounds)
    values[K191.W] = values[K191.W] - K193.ball(shift)
    coefficients = K195.K194.shifted_coefficients(shift)
    polynomial = K195.arb(0)
    for power in range(row + column, K193.TAYLOR_ORDER + 1):
        polynomial += coefficients[power] * compiled_interval(
            K195.chart_monomial(power, size, row, column)
        )(values)
    derivative_order = row + column
    tail_order = K193.TAYLOR_ORDER + 1
    combinatorial = Fraction(
        K195.math.factorial(tail_order),
        K195.math.factorial(tail_order - derivative_order)
        * K195.math.factorial(row)
        * K195.math.factorial(column),
    )
    tail = (
        (
            K193.derivative_abs_at_base(lower, tail_order)
            + K195.arb(K195.math.factorial(tail_order))
            / K193.ball(1 + lower) ** (tail_order + 1)
        )
        / K195.math.factorial(tail_order)
        * K193.ball(combinatorial)
        * K193.ball(radius) ** (tail_order - derivative_order)
    ).upper()
    return polynomial + K195.arb(0, tail), tail


def fast_chart_cell(
    size: int,
    w_bounds: tuple[Fraction, Fraction],
    s_bounds: tuple[Fraction, Fraction],
    a_bounds: tuple[Fraction, Fraction],
    q_bounds: tuple[Fraction, Fraction],
    c_bounds: tuple[Fraction, Fraction],
):
    values = K195.chart_values(w_bounds, s_bounds, a_bounds, q_bounds, c_bounds)
    matrix = []
    maximum_tail = 0.0
    for row in range(size):
        result_row = []
        for column in range(size):
            residual, tail = fast_shifted_entry_enclosure(
                size, row, column, w_bounds, s_bounds, a_bounds, q_bounds, c_bounds
            )
            cauchy = compiled_interval(K195.chart_cauchy(size, row, column))(values)
            result_row.append(cauchy + residual)
            maximum_tail = max(maximum_tail, float(tail))
        matrix.append(result_row)
    normalization = compiled_interval(K195.chart_normalization(size))(values)
    return normalization * K191.determinant(matrix), maximum_tail


GRID_CELLS = {
    size: (
        K196.split(*K196.SCALE_BOUNDS, K195.SUBDIVISIONS[size]["scale"]),
        K196.split(Fraction(0), K193.RADIAL_WIDTH, K195.SUBDIVISIONS[size]["radial"]),
    )
    for size in (2, 3)
}


def ftext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def q_cell_certificate(
    size: int,
    q_bounds: tuple[Fraction, Fraction],
    base_index: int,
    depth: int,
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    scale_cells, radial_cells = GRID_CELLS[size]
    lowers: list[float] = []
    uppers: list[float] = []
    tails: list[float] = []
    for scale_index, scale_bounds in enumerate(scale_cells):
        for radial_index, radial_bounds in enumerate(radial_cells):
            regularizer, tail = fast_chart_cell(
                size,
                radial_bounds,
                scale_bounds,
                K196.PRODUCT_BOUNDS[K196.A],
                q_bounds,
                K196.PRODUCT_BOUNDS[K196.C],
            )
            lower = float(regularizer.lower())
            if not lower > 0:
                return None, {
                    "base_index": base_index,
                    "depth": depth,
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
        "q": [ftext(value) for value in q_bounds],
        "outward_cells": len(scale_cells) * len(radial_cells),
        "minimum_R_lower": min(lowers),
        "maximum_R_upper": max(uppers),
        "maximum_entry_tail": max(tails),
        "all_cells_strictly_positive": True,
    }, None


def certify_or_bisect(
    size: int,
    q_bounds: tuple[Fraction, Fraction],
    base_index: int,
    depth: int,
    rejected: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    accepted, failure = q_cell_certificate(size, q_bounds, base_index, depth)
    if accepted is not None:
        return [accepted]
    assert failure is not None
    rejected.append(failure)
    if depth >= MAX_ADAPTIVE_DEPTH:
        raise AssertionError(
            "q corridor lost positivity after adaptive refinement "
            f"size={size} q={q_bounds} failure={failure}"
        )
    midpoint = (q_bounds[0] + q_bounds[1]) / 2
    return certify_or_bisect(
        size, (q_bounds[0], midpoint), base_index, depth + 1, rejected
    ) + certify_or_bisect(
        size, (midpoint, q_bounds[1]), base_index, depth + 1, rejected
    )


def build_corridor(size: int, progress: bool = False) -> dict[str, Any]:
    base_cells = K196.split(Q_START, Q_END, BASE_Q_SUBDIVISIONS[size])
    accepted: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    for base_index, bounds in enumerate(base_cells):
        accepted.extend(certify_or_bisect(size, bounds, base_index, 0, rejected))
        if progress:
            current = [row for row in accepted if row["base_index"] == base_index]
            print(
                f"K197 size={size} base_q_cell={base_index + 1}/{len(base_cells)} "
                f"accepted_tiles={len(current)} "
                f"minimum_lower={min(row['minimum_R_lower'] for row in current):.17g}",
                file=sys.stderr,
                flush=True,
            )
    unique_cells = sum(row["outward_cells"] for row in accepted)
    q_bounds = [tuple(Fraction(value) for value in row["q"]) for row in accepted]
    return {
        "size": size,
        "subdivisions": K195.SUBDIVISIONS[size],
        "base_q_subdivisions": BASE_Q_SUBDIVISIONS[size],
        "accepted_q_tiles": len(accepted),
        "maximum_adaptive_depth_used": max(row["depth"] for row in accepted),
        "rejected_parent_cells": rejected,
        "q_range": [ftext(Q_START), ftext(Q_END)],
        "a_range": [ftext(value) for value in K196.PRODUCT_BOUNDS[K196.A]],
        "c_range": [ftext(value) for value in K196.PRODUCT_BOUNDS[K196.C]],
        "q_tiles": accepted,
        "unique_outward_cells": unique_cells,
        "chart_cell_instances_by_exact_transpose": 2 * unique_cells,
        "minimum_R_lower": min(row["minimum_R_lower"] for row in accepted),
        "maximum_R_upper": max(row["maximum_R_upper"] for row in accepted),
        "maximum_entry_tail": max(row["maximum_entry_tail"] for row in accepted),
        "all_cells_strictly_positive": True,
        "q_tiles_contiguous": (
            q_bounds[0][0] == Q_START
            and q_bounds[-1][1] == Q_END
            and all(q_bounds[index][1] == q_bounds[index + 1][0] for index in range(len(q_bounds) - 1))
        ),
        "scale_and_radial_coverage_in_every_q_tile": True,
    }


def independent_controls(corridors: dict[str, dict[str, Any]]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    with localcontext() as context:
        context.prec = 220
        base = Decimal(K193.BASE_X.numerator) / Decimal(K193.BASE_X.denominator)
        radial_midpoint = (
            Decimal(K193.RADIAL_WIDTH.numerator)
            / Decimal(K193.RADIAL_WIDTH.denominator)
            / 2
        )
        minimum_sum = base * (Decimal(1) + radial_midpoint)
        for size in (2, 3):
            boundaries = sorted(
                {
                    Fraction(value)
                    for tile in corridors[str(size)]["q_tiles"]
                    for value in tile["q"]
                }
            )
            shapes = (
                [(K195.RAY[K195.A], K195.RAY[K195.C])]
                if size == 2
                else [
                    (a, c)
                    for a in K196.PRODUCT_BOUNDS[K196.A]
                    for c in K196.PRODUCT_BOUNDS[K196.C]
                ]
            )
            for scale in K196.SCALE_BOUNDS:
                for q in boundaries:
                    for a, c in shapes:
                        sd = Decimal(scale.numerator) / Decimal(scale.denominator)
                        ad = Decimal(a.numerator) / Decimal(a.denominator)
                        qd = Decimal(q.numerator) / Decimal(q.denominator)
                        cd = Decimal(c.numerator) / Decimal(c.denominator)
                        row_gaps = (
                            [sd / Decimal(32), Decimal(0)]
                            if size == 2
                            else [sd / Decimal(32), sd * ad / Decimal(32), Decimal(0)]
                        )
                        column_gaps = (
                            [sd * qd / Decimal(32), Decimal(0)]
                            if size == 2
                            else [sd * qd / Decimal(32), sd * qd * cd / Decimal(32), Decimal(0)]
                        )
                        left = [
                            minimum_sum * Decimal(2) / Decimal(5) + base * value
                            for value in row_gaps
                        ]
                        right = [
                            minimum_sum * Decimal(3) / Decimal(5) + base * value
                            for value in column_gaps
                        ]
                        value = K191.K186.divided_difference_regularizer(left, right, 200)
                        lower = Decimal(str(corridors[str(size)]["minimum_R_lower"]))
                        upper = Decimal(str(corridors[str(size)]["maximum_R_upper"]))
                        if not lower <= value <= upper:
                            raise AssertionError("independent q-corridor control escaped directed range")
                        rows.append(
                            {
                                "size": size,
                                "scale": ftext(scale),
                                "shape": {"a": ftext(a), "q": ftext(q), "c": ftext(c)},
                                "regularizer": format(value, ".24E"),
                                "contained_in_global_corridor_range": True,
                            }
                        )
    return {
        "precision_decimal_digits": 200,
        "rows": rows,
        "all_contained": True,
        "role": "independent convergent-series q-tile boundary controls; directed Arb common cells carry the proof",
    }


def build(progress: bool = False) -> dict[str, Any]:
    predecessor = json.loads(K196_MANIFEST.read_text())
    corridors = {str(size): build_corridor(size, progress) for size in (2, 3)}
    if not all(row["q_tiles_contiguous"] for row in corridors.values()):
        raise AssertionError("q-corridor tiles are not contiguous")
    controls = independent_controls(corridors)
    unique_cells = sum(row["unique_outward_cells"] for row in corridors.values())
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifest": "lab/process/k196-order-six-max-gap-product-atlas-wave.json",
            "source_manifest": predecessor["fixed_control"]["source_manifest"],
            "radial_cell": predecessor["fixed_control"]["radial_cell"],
            "max_gap_scale_range": predecessor["fixed_control"]["max_gap_scale_range"],
            "a_range": [ftext(value) for value in K196.PRODUCT_BOUNDS[K196.A]],
            "c_range": [ftext(value) for value in K196.PRODUCT_BOUNDS[K196.C]],
            "q_corridor": [ftext(Q_START), ftext(Q_END)],
            "base_q_subdivisions": {str(key): value for key, value in BASE_Q_SUBDIVISIONS.items()},
            "maximum_adaptive_depth": MAX_ADAPTIVE_DEPTH,
            "taylor_order": K193.TAYLOR_ORDER,
            "arb_decimal_digits": K193.ARB_DIGITS,
            "threads": 1,
            "source_patterns": predecessor["fixed_control"]["source_patterns"],
            "source_nontrivial_occurrences": predecessor["fixed_control"]["source_nontrivial_occurrences"],
            "source_time_gram_entries": predecessor["fixed_control"]["source_time_gram_entries"],
            "source_coherent_groups": predecessor["fixed_control"]["source_coherent_groups"],
        },
        "certified_q_to_one_corridor": {
            "sizes": corridors,
            "unique_outward_cells": unique_cells,
            "chart_cell_instances_by_exact_transpose": 2 * unique_cells,
            "all_cells_strictly_positive": all(row["all_cells_strictly_positive"] for row in corridors.values()),
            "common_cell_rule": "one shared (t,w,a,q,c) interval cell supplies every shifted entry and common normalization before the complete determinant",
            "k196_join": "q=8227/10240 is the upper face of K196's certified product block",
            "chart_seam": "q=1 is the exact row/column max-gap seam",
            "row_and_column_instances_related_by_exact_transpose": True,
            "complete_for_fixed_a_c_block": True,
        },
        "independent_controls": controls,
        "complete_family_propagation": {
            "operator_applies_to_every_size_two_and_three_regularizer": True,
            "all_53_patterns_retain_the_same_formula": predecessor["fixed_control"]["source_patterns"] == 53,
            "all_468_occurrences_retain_the_same_formula": predecessor["fixed_control"]["source_nontrivial_occurrences"] == 468,
            "all_234_entries_and_18_groups_remain_in_scope": True,
            "new_bound_applies_only_to_the_fixed_a_c_q_corridor": True,
        },
        "decision": {
            "complete_q_to_one_corridor_for_fixed_a_c_block": True,
            "k196_local_block_connected_to_q_one_seam": True,
            "remaining_a_c_complement_covered": False,
            "next_exact_input": "adaptively tile the remaining a/c shells using the accepted q-corridor resolution profile; only after the complete shape cover closes, differentiate the common-cell regularizer and compose the Duffy/Jacobi remainder",
        },
        "release_test": {
            "shifted_hermite_genocchi_entry_tail_retained": True,
            "all_entries_use_one_shared_scale_radial_and_three_shape_cell_before_complete_determinant_enclosure": True,
            "q_to_one_corridor_outwardly_certified": True,
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
        "certified_q_to_one_corridor": result["certified_q_to_one_corridor"],
        "independent_controls": result["independent_controls"],
        "complete_family_propagation": result["complete_family_propagation"],
        "decision": result["decision"],
        "release_test": result["release_test"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--progress", action="store_true")
    args = parser.parse_args()
    result = build(progress=args.progress)
    if args.write:
        OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if args.summary or not args.write:
        print(json.dumps(summary(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
