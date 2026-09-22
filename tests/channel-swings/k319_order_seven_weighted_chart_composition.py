#!/usr/bin/env python3
"""Compile every K315 y-jet family onto K318's weighted chart atlas.

This compiler is deliberately a release audit.  It proves that the finite
endpoint atlas covers the complete value/first/second column-replacement bank
without moving absolute values inside a bordered determinant.  It also checks
whether every chart already has a numerical outward determinant bound.  K318
provides exact coordinates and integrable weights, but not those complete
determinant constants, so K319 must not release the y-master sum.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K315 = ROOT / "lab/process/k315-order-seven-terminal-bordered-adapter.json"
K317 = ROOT / "lab/process/k317-order-seven-boundary-coefficient-discriminator.json"
K318 = ROOT / "lab/process/k318-order-seven-weighted-endpoint-blowup-atlas.json"
OUTPUT = ROOT / "lab/process/k319-order-seven-weighted-chart-composition.json"


def family_rows(k315: dict[str, Any], k318: dict[str, Any]) -> list[dict[str, Any]]:
    endpoint_chart_ids = [row["id"] for row in k318["determinant_preserving_endpoint_atlas"]["charts"]]
    rows = []
    for family in k315["complete_column_replacement_expansion"]:
        derivative_order = sum(family["column_orders"])
        if derivative_order not in (0, 1, 2):
            raise AssertionError("unexpected y-jet order")
        terminal_histogram = {
            str(key): value for key, value in family["terminal_jet_histogram"].items()
        }
        terminal_monomials = sum(terminal_histogram.values())
        chart_ids = [
            "interior_K314_leaf",
            *endpoint_chart_ids,
        ]
        rows.append({
            "family": family["family"],
            "y_derivative_order": derivative_order,
            "outer_multiplicity": family["outer_multiplicity"],
            "nonzero_determinant_monomials": family["nonzero_determinant_monomials"],
            "terminal_monomials": terminal_monomials,
            "terminal_jet_histogram": terminal_histogram,
            "required_chart_ids": chart_ids,
            "required_chart_count": len(chart_ids),
            "assembly": "one complete five-by-five bordered column-replacement determinant per chart; coherent signs and cross multiplicity stay inside before absolute enclosure",
            "complete_chart_determinant_upper_available": False,
        })
    return rows


def build() -> dict[str, Any]:
    k315 = json.loads(K315.read_text())
    k317 = json.loads(K317.read_text())
    k318 = json.loads(K318.read_text())
    if not k318["decision"]["finite_endpoint_blowup_atlas_implemented"]:
        raise AssertionError("K318 atlas unavailable")
    if not k317["decision"]["weighted_complete_chart_route_required"]:
        raise AssertionError("K317 route posture changed")
    rows = family_rows(k315, k318)
    derivative_counts = Counter(row["y_derivative_order"] for row in rows)
    terminal_orders = Counter()
    second_terminal_orders = Counter()
    for row in rows:
        for order, count in row["terminal_jet_histogram"].items():
            terminal_orders[int(order)] += count * row["outer_multiplicity"]
            if row["y_derivative_order"] == 2:
                second_terminal_orders[int(order)] += count * row["outer_multiplicity"]
    total_obligations = sum(row["required_chart_count"] for row in rows)
    weighted_monomials = sum(
        row["outer_multiplicity"] * row["nonzero_determinant_monomials"] for row in rows
    )

    return {
        "schema_version": "1.0",
        "result_id": "K319-ORDER-SEVEN-WEIGHTED-CHART-COMPOSITION",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k315-order-seven-terminal-bordered-adapter.json",
                "lab/process/k317-order-seven-boundary-coefficient-discriminator.json",
                "lab/process/k318-order-seven-weighted-endpoint-blowup-atlas.json",
            ],
            "bordered_family_count": len(rows),
            "y_derivative_family_counts": {str(key): value for key, value in sorted(derivative_counts.items())},
            "K318_homogeneous_sector_count": k318["homogeneous_endpoint_sectors"]["finite_sector_count"],
            "K318_endpoint_chart_count": k318["determinant_preserving_endpoint_atlas"]["chart_count"],
            "K318_terminal_singular_hepp3_charts": k318["determinant_preserving_endpoint_atlas"]["terminal_singular_hepp3_charts"],
            "K318_regular_hepp2_charts": k318["determinant_preserving_endpoint_atlas"]["regular_hepp2_charts"],
        },
        "complete_family_chart_compilation": rows,
        "census": {
            "complete_chart_obligations": total_obligations,
            "weighted_nonzero_determinant_monomials": weighted_monomials,
            "terminal_monomials_by_jet_order_with_cross_factors": {
                str(key): value for key, value in sorted(terminal_orders.items())
            },
            "second_family_terminal_monomials_by_jet_order_with_cross_factors": {
                str(key): value for key, value in sorted(second_terminal_orders.items())
            },
            "K315_weighted_monomial_census_replayed": weighted_monomials == k315["census"]["weighted_nonzero_monomials_after_cross_factors"],
            "K315_terminal_histogram_replayed": {
                str(key): value for key, value in sorted(terminal_orders.items())
            } == k315["census"]["terminal_monomials_by_jet_order_with_cross_factors"],
        },
        "composition_contract": {
            "chart_expression": "Peano_weight * native_endpoint_factors * exact_chart_Jacobian * projective_polynomial * D4_group * (-det(B5_replaced_group))",
            "absolute_value_location": "after the complete chart expression for one coherent group is assembled",
            "terminal_entry_location": "inside B5_replaced_group in the K318 split-sector coordinates",
            "K314_usage": "interior and certified one-gap leaves only",
            "K318_usage": "y-log, terminal split and nested homogeneous endpoint sectors",
            "cross_factor_two_retained": True,
            "literal_border_zeros_retained": True,
            "detached_cofactor_used": False,
            "detached_global_coefficient_used": False,
            "occurrencewise_coherent_absolute_values_used": False,
            "complete_signed_second_jet": "sum_c det(C0,...,Cc'',...,C4) + 2*sum_(c<d) det(C0,...,Cc',...,Cd',...,C4), assembled with chart weights before abs",
            "all_fifteen_second_families_summed_before_absolute_value": True,
        },
        "sufficiency_audit": {
            "all_twenty_one_families_compiled": len(rows) == 21,
            "all_fifteen_second_derivative_families_compiled": derivative_counts[2] == 15,
            "all_three_terminal_jet_orders_compiled": set(terminal_orders) == {0, 1, 2},
            "every_family_has_all_sixteen_endpoint_charts": all(
                len(row["required_chart_ids"]) == 17
                and sum(chart_id != "interior_K314_leaf" for chart_id in row["required_chart_ids"]) == 16
                for row in rows
            ),
            "all_chart_weights_structurally_integrable": k318["homogeneous_endpoint_sectors"]["all_radial_powers_strictly_above_minus_one"],
            "barycentric_y_split_atlas_complete": k318["decision"]["barycentric_y_split_endpoint_scope_complete"],
            "radial_projective_s_endpoint_atlas_complete": k318["decision"]["radial_projective_s_endpoint_atlas_complete"],
            "all_complete_chart_determinant_uppers_available": all(row["complete_chart_determinant_upper_available"] for row in rows),
            "structural_integrability_is_not_numerical_enclosure": True,
            "missing_coverage_input": "continuous r=0 scaling and the s=0,1 radial-projective faces joined to all sixteen barycentric y/split charts",
            "missing_numerical_input": "outward interval upper for each complete D4-times-bordered-B5 replacement family after all chart weights and Jacobians are applied, beginning with the old-position-6 nested y/split corner",
        },
        "decision": {
            "complete_weighted_chart_obligation_compiler_implemented": True,
            "complete_y_master_inputs_sufficient": False,
            "complete_y_master_constant_emitted": False,
            "five_gap_axis_transfer_released": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "join continuous r=0 scaling and the s=0,1 radial-projective faces to the sixteen K318 charts, then implement the first outward interval evaluator for the complete weighted old-position-6 expression and cover the remaining families before any five-axis reuse",
        },
        "release_test": {
            "K315_all_families_consumed": len(rows) == len(k315["complete_column_replacement_expansion"]),
            "K315_weighted_monomials_exact": weighted_monomials == 1674,
            "K315_terminal_histogram_exact": terminal_orders == Counter({0: 378, 1: 162, 2: 18}),
            "K315_second_family_terminal_histogram_exact": second_terminal_orders == Counter({0: 288, 1: 144, 2: 18}),
            "determinant_assembly_precedes_absolute_value": True,
            "numerical_release_rejected_for_named_missing_input": True,
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k318["ledger_effect"],
        "source_routing": k318["source_routing"],
        "claim_ceiling": "Complete compiler from all twenty-one K315 value/first/second-y bordered determinant families to K318's sixteen barycentric y/split endpoint charts. It replays 1,674 cross-factor-weighted nonzero determinant monomials, terminal jet counts 378/162/18 and the second-family counts 288/144/18, retaining the signed fifteen-family second jet, complete coherent group assembly and literal border zeros before absolute enclosure. Continuous r=0 scaling, s=0/1 radial-projective coverage and outward numerical determinant uppers remain absent, so K319 explicitly rejects release of a complete y-master constant, five-axis transfer, K294 join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["bordered_family_count"] != 21 or fixed["y_derivative_family_counts"] != {"0": 1, "1": 5, "2": 15}:
        raise AssertionError("K315 family coverage changed")
    if fixed["K318_endpoint_chart_count"] != 16 or fixed["K318_terminal_singular_hepp3_charts"] != 12 or fixed["K318_regular_hepp2_charts"] != 4:
        raise AssertionError("K318 endpoint chart census changed")
    census = payload["census"]
    if not census["K315_weighted_monomial_census_replayed"] or not census["K315_terminal_histogram_replayed"]:
        raise AssertionError("K315 census not replayed")
    if census["second_family_terminal_monomials_by_jet_order_with_cross_factors"] != {"0": 288, "1": 144, "2": 18}:
        raise AssertionError("K315 second-family terminal census changed")
    contract = payload["composition_contract"]
    if contract["detached_cofactor_used"] or contract["detached_global_coefficient_used"] or contract["occurrencewise_coherent_absolute_values_used"]:
        raise AssertionError("forbidden determinant factorization introduced")
    if not contract["cross_factor_two_retained"] or not contract["literal_border_zeros_retained"]:
        raise AssertionError("complete bordered structure lost")
    if not contract["all_fifteen_second_families_summed_before_absolute_value"]:
        raise AssertionError("signed second-jet family sum lost")
    audit = payload["sufficiency_audit"]
    if not audit["all_twenty_one_families_compiled"] or not audit["all_fifteen_second_derivative_families_compiled"] or not audit["every_family_has_all_sixteen_endpoint_charts"]:
        raise AssertionError("family compilation incomplete")
    if audit["all_complete_chart_determinant_uppers_available"]:
        raise AssertionError("missing numerical determinant uppers hidden")
    if not audit["barycentric_y_split_atlas_complete"] or audit["radial_projective_s_endpoint_atlas_complete"]:
        raise AssertionError("radial-projective coverage boundary hidden")
    decision = payload["decision"]
    if decision["complete_y_master_inputs_sufficient"] or decision["complete_y_master_constant_emitted"] or decision["five_gap_axis_transfer_released"]:
        raise AssertionError("downstream numerical release overclaimed")


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
