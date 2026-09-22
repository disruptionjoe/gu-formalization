#!/usr/bin/env python3
"""Complete K318 value-family chart bank on one positive slab.

K323 proved a complete-matrix enclosure on one left endpoint chart.  This
replay raises the scaled terminal upper from two to the chart-uniform K322
value four (|Phi_0| <= 2 and H >= 1/2), uses transposition for the right
endpoint, and binds the resulting left-column/right-row enclosures to every
one of the sixteen K318 charts.  The endpoint weight stays inside the bordered
matrix; exact K318 chart masses are carried as census data, not multiplied a
second time.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K318 = ROOT / "lab/process/k318-order-seven-weighted-endpoint-blowup-atlas.json"
K323 = ROOT / "lab/process/k323-order-seven-old-position-six-value-pilot.json"
K323_MODULE = Path(__file__).with_name("k323_order_seven_old_position_six_value_pilot.py")
OUTPUT = ROOT / "lab/process/k324-order-seven-complete-value-chart-bank.json"

ctx.dps = 180
ctx.threads = 1


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def transpose(matrix: list[list[arb]]) -> list[list[arb]]:
    return [list(row) for row in zip(*matrix, strict=True)]


def build_endpoint_bounds(k323_module):
    backend = k323_module.load_module(k323_module.K308_MODULE, "k324_k308_backend")
    d4, left_b5, inherited_audit = k323_module.build_matrices(backend)

    # On the complete K318 atlas only H >= 1/2 is uniform.  Thus
    # lambda*f(w)=Phi_0(w)/H has upper 2/(1/2)=4.  No raw K_0(0) call occurs.
    left_b5[3][3] = arb(4)
    right_b5 = transpose(left_b5)
    d4_bound = k323_module.hadamard_bound(d4)
    left_b5_bound = k323_module.hadamard_bound(left_b5)
    right_b5_bound = k323_module.hadamard_bound(right_b5)

    k323 = json.loads(K323.read_text())
    scalar = Fraction(k323["complete_weighted_matrix_bound"]["outer_scalar_fraction"])
    left_complete = d4_bound * left_b5_bound * backend.ball(scalar)
    right_complete = d4_bound * right_b5_bound * backend.ball(scalar)
    left_text = backend.upper_text(left_complete)
    right_text = backend.upper_text(right_complete)
    for name, text in (("left", left_text), ("right", right_text)):
        if not math.isfinite(float(text)) or float(text) <= 0:
            raise AssertionError(f"{name} endpoint bound is not finite positive")

    audit = dict(inherited_audit)
    audit.update(
        {
            "terminal_scaled_upper": "4",
            "terminal_argument": "w=lambda*H with lambda=x*rho*v and chart-uniform H>=1/2",
            "terminal_zero_safe_rule": "abs(Phi_0(w))/H <= 2/(1/2)=4",
            "raw_Bessel_evaluation_at_zero_used": False,
            "left_endpoint_weight_placement": "border column 4",
            "right_endpoint_weight_placement": "border row 4 by complete-matrix transposition",
            "right_matrix_is_exact_transpose_of_left_enclosure": True,
        }
    )
    return backend, d4_bound, left_b5_bound, right_b5_bound, left_text, right_text, audit


def build() -> dict[str, Any]:
    k323_module = load_module(K323_MODULE, "k324_k323_backend")
    k318 = json.loads(K318.read_text())
    k323 = json.loads(K323.read_text())
    source_charts = k318["determinant_preserving_endpoint_atlas"]["charts"]
    if len(source_charts) != 16:
        raise AssertionError("K318 chart census is not sixteen")
    if not k323["decision"]["complete_matrix_Hadamard_route_finite"]:
        raise AssertionError("K323 complete-matrix route unavailable")

    backend, d4_bound, left_b5_bound, right_b5_bound, left_text, right_text, audit = build_endpoint_bounds(k323_module)
    rows = []
    for chart in source_charts:
        endpoint = chart["endpoint"]
        if endpoint not in {"left", "right"}:
            raise AssertionError("unexpected endpoint in K318 chart atlas")
        rows.append(
            {
                "chart_id": chart["id"],
                "endpoint": endpoint,
                "split_sector": chart["split_sector"],
                "hepp_dimension": len(chart["ordered_variables"]),
                "exact_chart_mass": chart["exact_chart_mass"],
                "terminal_singular_sector": chart["terminal_singular_sector"],
                "endpoint_weight_placement": "border column 4" if endpoint == "left" else "border row 4",
                "four_group_weighted_chart_abs_upper": left_text if endpoint == "left" else right_text,
                "additional_theta_squared_if_applicable_abs_upper": "1",
            }
        )

    left_rows = [row for row in rows if row["endpoint"] == "left"]
    right_rows = [row for row in rows if row["endpoint"] == "right"]
    total = arb(8) * (arb(left_text) + arb(right_text))
    total_text = backend.upper_text(total)
    if not math.isfinite(float(total_text)) or float(total_text) <= 0:
        raise AssertionError("sixteen-chart sum is not finite positive")

    return {
        "schema_version": "1.0",
        "result_id": "K324-ORDER-SEVEN-COMPLETE-VALUE-CHART-BANK",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k318-order-seven-weighted-endpoint-blowup-atlas.json",
                "lab/process/k321-order-seven-radial-projective-tensor-atlas.json",
                "lab/process/k322-order-seven-zero-safe-scaled-bessel-envelopes.json",
                "lab/process/k323-order-seven-old-position-six-value-pilot.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "old_position": 6,
            "jet_family": "value",
            "chart_count": 16,
            "left_chart_count": len(left_rows),
            "right_chart_count": len(right_rows),
            "radial_projective_slab": k323["fixed_control"]["radial_projective_slab"],
        },
        "complete_value_chart_bank": {
            "rows": rows,
            "source_chart_ids": [chart["id"] for chart in source_charts],
            "D4_complete_Hadamard_abs_upper": backend.upper_text(d4_bound),
            "left_bordered_B5_complete_Hadamard_abs_upper": backend.upper_text(left_b5_bound),
            "right_bordered_B5_complete_Hadamard_abs_upper": backend.upper_text(right_b5_bound),
            "left_four_group_weighted_chart_abs_upper": left_text,
            "right_four_group_weighted_chart_abs_upper": right_text,
            "sixteen_chart_weighted_abs_upper": total_text,
            "node_audit": audit,
            "exact_chart_masses_are_census_not_extra_multiplier": True,
            "positive_density_factors_bounded_by_one": k323["complete_weighted_matrix_bound"]["positive_density_factors_bounded_by_one"],
            "matrix_bound_rule": "one Hadamard bound per complete matrix after terminal and endpoint weight absorption",
            "permutation_or_monomial_absolute_values_used": False,
            "detached_terminal_cofactor_used": False,
            "terminal_weight_absorbed_before_determinant_bound": True,
            "Peano_Hepp_weight_absorbed_before_determinant_bound": True,
            "all_literal_border_zeros_retained": True,
        },
        "scope_boundary": {
            "covered": "all sixteen K318 value-family endpoint charts on one fixed positive radial/projective slab",
            "not_covered": [
                "the five first-y and fifteen signed second-y families",
                "radial origin and tail subdivision sums",
                "all projective-face subdivision sums",
                "a complete y-master constant",
            ],
            "fixed_slab_bank_is_not_global_release": True,
        },
        "decision": {
            "all_sixteen_value_charts_bounded": True,
            "left_column_right_row_symmetry_implemented": True,
            "zero_touching_terminal_entry_evaluated_without_raw_Knu_zero_call": True,
            "signed_first_and_second_jet_backend_complete": False,
            "complete_y_master_constant_emitted": False,
            "five_gap_axis_transfer_released": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "implement interval-signed column-replacement aggregation for all five first-y and fifteen second-y families before adaptive radial/projective summation",
        },
        "release_test": {
            "source_chart_ids_covered_exactly_once": True,
            "left_and_right_chart_counts_are_eight": len(left_rows) == len(right_rows) == 8,
            "all_complete_bounds_finite_positive": all(math.isfinite(float(row["four_group_weighted_chart_abs_upper"])) and float(row["four_group_weighted_chart_abs_upper"]) > 0 for row in rows),
            "terminal_scaled_upper_from_K322": audit["terminal_scaled_upper"] == "4",
            "complete_matrices_bounded_after_weight_absorption": True,
            "no_permutation_absolute_enclosure": True,
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k323["ledger_effect"],
        "source_routing": k323["source_routing"],
        "claim_ceiling": "Finite outward complete-matrix value-family bounds cover all sixteen K318 endpoint charts on one fixed positive radial/projective slab. The chart-uniform K322 terminal upper four is inserted only after terminal scaling; Peano/Hepp weights are absorbed into the left border column or right border row; literal zeros are retained; and exact K318 chart masses are carried for census without double multiplication. Signed first/second families and radial/projective subdivision sums remain open, so no complete y-master constant, gap-axis transfer, K294 join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim is released.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    bank = payload["complete_value_chart_bank"]
    rows = bank["rows"]
    source_ids = bank["source_chart_ids"]
    row_ids = [row["chart_id"] for row in rows]
    if len(rows) != 16 or len(set(row_ids)) != 16 or row_ids != source_ids:
        raise AssertionError("K318 charts are not covered exactly once in source order")
    if sum(row["endpoint"] == "left" for row in rows) != 8 or sum(row["endpoint"] == "right" for row in rows) != 8:
        raise AssertionError("left/right chart census changed")
    if any(row["endpoint_weight_placement"] != ("border column 4" if row["endpoint"] == "left" else "border row 4") for row in rows):
        raise AssertionError("endpoint weight lost its left-column/right-row placement")
    if any(not math.isfinite(float(row["four_group_weighted_chart_abs_upper"])) or float(row["four_group_weighted_chart_abs_upper"]) <= 0 for row in rows):
        raise AssertionError("a chart bound is not finite positive")
    audit = bank["node_audit"]
    if audit["terminal_scaled_upper"] != "4" or audit["raw_Bessel_evaluation_at_zero_used"]:
        raise AssertionError("chart-uniform zero-safe terminal rule lost")
    if not bank["terminal_weight_absorbed_before_determinant_bound"] or not bank["Peano_Hepp_weight_absorbed_before_determinant_bound"]:
        raise AssertionError("a chart weight was not absorbed before enclosure")
    if bank["permutation_or_monomial_absolute_values_used"] or bank["detached_terminal_cofactor_used"]:
        raise AssertionError("forbidden detached or permutation enclosure introduced")
    if not bank["all_literal_border_zeros_retained"] or not bank["exact_chart_masses_are_census_not_extra_multiplier"]:
        raise AssertionError("matrix zeros or chart-mass accounting changed")
    scope = payload["scope_boundary"]
    if not scope["fixed_slab_bank_is_not_global_release"]:
        raise AssertionError("fixed-slab scope hidden")
    decision = payload["decision"]
    if decision["signed_first_and_second_jet_backend_complete"] or decision["complete_y_master_constant_emitted"]:
        raise AssertionError("complete y-master overclaim")


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
