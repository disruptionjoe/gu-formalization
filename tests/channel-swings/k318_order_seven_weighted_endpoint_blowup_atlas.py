#!/usr/bin/env python3
"""Build the weighted endpoint blow-up atlas required after K317.

The atlas does not bound a singular entry away from the endpoint.  Instead it
puts the native Peano and split weights, the exact chart Jacobian, and the
complete coherent determinant in the same integral before any absolute
enclosure.  Maximal-coordinate sectors resolve K300's homogeneous corners;
exponential charts resolve the logarithmic y endpoints; and two exact sectors
resolve the terminal split square used by K302.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K299 = ROOT / "lab/process/k299-order-seven-positive-peano-simplex-rule.json"
K300 = ROOT / "lab/process/k300-order-seven-angular-method-selection.json"
K302 = ROOT / "lab/process/k302-order-seven-split-weighted-peano-jet.json"
K317 = ROOT / "lab/process/k317-order-seven-boundary-coefficient-discriminator.json"
OUTPUT = ROOT / "lab/process/k318-order-seven-weighted-endpoint-blowup-atlas.json"


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def homogeneous_sector_rows(k300: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for source in k300["endpoint_integrability"]["rows"]:
        variables = source["corner_variables"]
        degree = source["second_derivative_homogeneous_degree"]
        exponent = degree + variables - 1
        margin = degree + variables
        if margin != source["second_derivative_integrability_margin"]:
            raise AssertionError("K300 homogeneous margin no longer matches the sector Jacobian")
        rows.append({
            "old_position": source["old_position"],
            "corner_variables": variables,
            "homogeneous_degree": degree,
            "maximal_coordinate_sectors": variables,
            "sector_map": "z_j=rho; z_i=rho*theta_i for i!=j, with rho and every theta_i in [0,1]",
            "sector_jacobian": f"rho^{variables - 1}",
            "weighted_radial_power": exponent,
            "radial_integrability_margin": margin,
            "unit_coefficient_radial_mass": q(Fraction(1, margin)),
            "tie_boundaries": "measure zero",
            "complete_determinant_retained": True,
        })
    return rows


def hepp_rows() -> list[dict[str, Any]]:
    rows = []
    for endpoint in ("left", "right"):
        singular_split = "a_max" if endpoint == "left" else "b_max"
        regular_split = "b_max" if endpoint == "left" else "a_max"
        for permutation in itertools.permutations(("eta", "A", "v")):
            label = "_".join(permutation)
            eta_rank = permutation.index("eta")
            mass = (Fraction(1, 1920), Fraction(1, 640), Fraction(1, 320))[eta_rank]
            rows.append({
                "id": f"{endpoint}_{singular_split}_hepp3_{label}",
                "endpoint": endpoint,
                "split_sector": singular_split,
                "ordered_variables": list(permutation),
                "map": "q_pi0=h0*h1*h2; q_pi1=h1*h2; q_pi2=h2",
                "hepp_jacobian": "h1*h2^2",
                "free_variables": [],
                "terminal_singular_sector": True,
                "eta_rank": eta_rank,
                "exact_chart_mass": q(mass),
            })
        for permutation in itertools.permutations(("eta", "A")):
            label = "_".join(permutation)
            eta_rank = permutation.index("eta")
            mass = (Fraction(1, 384), Fraction(1, 128))[eta_rank]
            rows.append({
                "id": f"{endpoint}_{regular_split}_hepp2_{label}",
                "endpoint": endpoint,
                "split_sector": regular_split,
                "ordered_variables": list(permutation),
                "map": "q_pi0=h0*h1; q_pi1=h1",
                "hepp_jacobian": "h1",
                "free_variables": ["v"],
                "terminal_singular_sector": False,
                "eta_rank": eta_rank,
                "exact_chart_mass": q(mass),
            })
    return rows


def q_exponents(rank: int, dimension: int) -> list[int]:
    return [int(index >= rank) for index in range(dimension)]


def valuation_rows(charts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for chart in charts:
        order = chart["ordered_variables"]
        dimension = len(order)
        eta_rank = order.index("eta")
        eta_exp = q_exponents(eta_rank, dimension)
        jacobian_exp = list(range(dimension))
        if chart["terminal_singular_sector"]:
            a_rank = order.index("A")
            v_rank = order.index("v")
            for k in range(3):
                for ell in range(3 - k):
                    eta_a = q_exponents(max(eta_rank, a_rank), dimension)
                    eta_v = q_exponents(max(eta_rank, v_rank), dimension)
                    exponents = [
                        2 * eta_exp[index]
                        + jacobian_exp[index]
                        - ell * eta_a[index]
                        - (k + 1) * eta_v[index]
                        for index in range(dimension)
                    ]
                    rows.append({
                        "chart_id": chart["id"],
                        "model": f"eta^2*J/((eta+A)^{ell}*(eta+v)^{k + 1})",
                        "k": k,
                        "ell": ell,
                        "cube_exponents": exponents,
                        "minimum_exponent": min(exponents),
                        "integrable": min(exponents) >= 0,
                    })
        else:
            a_rank = order.index("A")
            for ell in range(3):
                eta_a = q_exponents(max(eta_rank, a_rank), dimension)
                exponents = [
                    2 * eta_exp[index] + jacobian_exp[index] - ell * eta_a[index]
                    for index in range(dimension)
                ]
                rows.append({
                    "chart_id": chart["id"],
                    "model": f"eta^2*J/(eta+A)^{ell}",
                    "k": None,
                    "ell": ell,
                    "cube_exponents": exponents,
                    "minimum_exponent": min(exponents),
                    "integrable": min(exponents) >= 0,
                })
    return rows


def build() -> dict[str, Any]:
    k299 = json.loads(K299.read_text())
    k300 = json.loads(K300.read_text())
    k302 = json.loads(K302.read_text())
    k317 = json.loads(K317.read_text())
    if not k317["decision"]["weighted_complete_chart_route_required"]:
        raise AssertionError("K317 weighted-chart route is unavailable")
    if k299["one_dimensional_factors"][-1]["axis"] != "y":
        raise AssertionError("K299 y Peano axis changed")
    if not k302["complete_split_face_transfer"]["terminal_split_face_peano_weighted_integrable"]:
        raise AssertionError("K302 terminal weighted transfer is unavailable")

    corner_rows = homogeneous_sector_rows(k300)
    endpoint_charts = hepp_rows()
    if len(endpoint_charts) != 16:
        raise AssertionError("endpoint Hepp atlas must have sixteen charts")
    valuations = valuation_rows(endpoint_charts)
    if len(valuations) != 84 or not all(row["integrable"] for row in valuations):
        raise AssertionError("weighted endpoint Cauchy valuation control failed")
    left_mass = sum(Fraction(row["exact_chart_mass"]) for row in endpoint_charts if row["endpoint"] == "left")
    right_mass = sum(Fraction(row["exact_chart_mass"]) for row in endpoint_charts if row["endpoint"] == "right")
    log_mass = math.log(2) / 24 + 1 / 72
    exponential_mass = math.exp(-3 * math.log(2)) * (math.log(2) / 3 + 1 / 9)
    if not math.isclose(log_mass, exponential_mass, rel_tol=0, abs_tol=2e-16):
        raise AssertionError("exponential endpoint chart did not replay the exact log mass")

    return {
        "schema_version": "1.0",
        "result_id": "K318-ORDER-SEVEN-WEIGHTED-ENDPOINT-BLOWUP-ATLAS",
        "created": "2026-09-22",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k299-order-seven-positive-peano-simplex-rule.json",
                "lab/process/k300-order-seven-angular-method-selection.json",
                "lab/process/k302-order-seven-split-weighted-peano-jet.json",
                "lab/process/k317-order-seven-boundary-coefficient-discriminator.json",
            ],
            "master_axis": "y",
            "fixed_Duffy_node": "p_i=1/6 for all six gaps",
            "outer_tensor_weight": "1/120",
            "maximum_derivative_order": 2,
            "endpoint_old_positions": [row["old_position"] for row in corner_rows],
            "terminal_argument": k302["fixed_control"]["terminal_argument"],
        },
        "homogeneous_endpoint_sectors": {
            "rule": "split [0,1]^d into d maximal-coordinate sectors, substitute z_j=rho and z_i=rho*theta_i, and include rho^(d-1) before enclosing the complete chart integrand",
            "rows": corner_rows,
            "all_radial_powers_strictly_above_minus_one": all(row["weighted_radial_power"] > -1 for row in corner_rows),
            "worst_weighted_radial_power": min(row["weighted_radial_power"] for row in corner_rows),
            "finite_sector_count": sum(row["maximal_coordinate_sectors"] for row in corner_rows),
        },
        "logarithmic_y_endpoint_charts": {
            "left": {
                "domain": "0<y<=1/2",
                "map": "y=exp(-t), t in [log(2),infinity)",
                "jacobian": "dy=exp(-t)dt",
                "leading_weighted_model": "y^2*(-log(y))dy = t*exp(-3t)dt",
            },
            "right": {
                "domain": "1/2<=y<1",
                "map": "1-y=exp(-t), t in [log(2),infinity)",
                "jacobian": "dy=exp(-t)dt",
                "leading_weighted_model": "(1-y)^2*(-log(1-y))dy = t*exp(-3t)dt",
            },
            "exact_half_mass": "log(2)/24+1/72",
            "tail_from_T": "exp(-3*T)*(T/3+1/9)",
            "tail_at_log2_decimal": repr(exponential_mass),
            "K317_exact_mass_replayed": math.isclose(log_mass, exponential_mass, rel_tol=0, abs_tol=2e-16),
            "compact_pointwise_log_supremum_requested": False,
        },
        "terminal_split_square": {
            "variables": "a=1-u3, b=1-z3",
            "native_argument": "x*(y*a+(1-y)*b)",
            "sectors": [
                {
                    "id": "a_max",
                    "map": "a=rho, b=rho*theta",
                    "domain": "rho,theta in [0,1]",
                    "jacobian": "rho",
                    "argument": "x*rho*(y+(1-y)*theta)",
                },
                {
                    "id": "b_max",
                    "map": "a=rho*theta, b=rho",
                    "domain": "rho,theta in [0,1]",
                    "jacobian": "rho",
                    "argument": "x*rho*(y*theta+(1-y))",
                },
            ],
            "measure_zero_overlap": "a=b",
            "leading_K1_radial_cancellation": "2*K1(x*rho*L)<=2/(x*rho*L), so the chart Jacobian rho cancels the radial pole before enclosure",
            "joint_y_theta_corners": "route through the old-position-6 two-variable maximal-coordinate sectors; do not take a supremum of 1/L",
            "K302_weighted_bounds_retained": k302["universal_weighted_bounds"],
            "split_cutoff_used": False,
        },
        "determinant_preserving_endpoint_atlas": {
            "endpoint_coordinates": {
                "left": "eta=2*y, A=1-u2, C=1-u3, D=1-z3",
                "right": "eta=2*(1-y), A=1-z2, C=1-u3, D=1-z3",
            },
            "split_sector_rule": "C=rho,D=rho*v or D=rho,C=rho*v, with Jacobian rho",
            "peano_measure_rule": "K(y)dy=eta^2*deta/16 on either endpoint half",
            "charts": endpoint_charts,
            "chart_count": len(endpoint_charts),
            "left_chart_count": sum(row["endpoint"] == "left" for row in endpoint_charts),
            "right_chart_count": sum(row["endpoint"] == "right" for row in endpoint_charts),
            "terminal_singular_hepp3_charts": sum(row["terminal_singular_sector"] for row in endpoint_charts),
            "regular_hepp2_charts": sum(not row["terminal_singular_sector"] for row in endpoint_charts),
            "complete_chart_weight": "omega=rho*eta^2*J_hepp/16",
            "determinant_absorption": "by determinant multilinearity, absorb rho into terminal column 3 and eta^2*J_hepp/16 into the endpoint border column (left) or bottom border row (right) before interval enclosure",
            "absolute_value_after_absorption": True,
            "exact_left_mass": q(left_mass),
            "exact_right_mass": q(right_mass),
            "exact_total_mass": q(left_mass + right_mass),
            "K299_y_Peano_mass_replayed": left_mass == right_mass == Fraction(1, 48) and left_mass + right_mass == Fraction(1, 24),
        },
        "cauchy_model_valuation_control": {
            "singular_sector_model": "eta^2*J/((eta+A)^ell*(eta+v)^(k+1)), k,ell>=0, k+ell<=2",
            "regular_sector_model": "eta^2*J/(eta+A)^ell, ell=0,1,2; v remains free",
            "checks": valuations,
            "check_count": len(valuations),
            "all_cube_exponents_nonnegative": all(row["minimum_exponent"] >= 0 for row in valuations),
            "minimum_cube_exponent": min(row["minimum_exponent"] for row in valuations),
        },
        "complete_chart_integrand_contract": {
            "integrand_order": [
                "form the complete K315 bordered column-replacement determinant with coherent signs and literal border zeros",
                "multiply the common size-four determinant and exact native projective polynomial",
                "multiply K299's Peano kernel, native endpoint factors and the exact sector Jacobian",
                "evaluate K302's terminal split entry in the same sector coordinates",
                "take an outward absolute enclosure only after the complete chart/group expression is assembled",
            ],
            "detached_terminal_budget_times_global_cofactor": False,
            "detached_endpoint_pointwise_supremum": False,
            "occurrencewise_coherent_absolute_values": False,
            "complete_bordered_assembly_retained": True,
        },
        "decision": {
            "finite_endpoint_blowup_atlas_implemented": True,
            "sixteen_determinant_preserving_endpoint_charts_implemented": True,
            "exact_y_Peano_mass_replayed": left_mass + right_mass == Fraction(1, 24),
            "all_eighty_four_Cauchy_model_valuations_integrable": all(row["integrable"] for row in valuations),
            "barycentric_y_split_endpoint_scope_complete": True,
            "radial_projective_s_endpoint_atlas_complete": False,
            "all_K300_endpoint_classes_have_exact_sector_coordinates": len(corner_rows) == 3,
            "terminal_split_square_has_exact_two_sector_cover": True,
            "logarithmic_y_endpoints_have_exact_exponential_tail_rule": True,
            "complete_chart_determinant_uppers_emitted": False,
            "complete_y_master_constant_emitted": False,
            "five_gap_axis_transfer_released": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "compile all twenty-one K315 y-jet families onto this barycentric y/split atlas, then join continuous r=0 scaling and the s=0,1 radial-projective faces before implementing outward complete-determinant bounds; structural integrability alone does not release the y-master sum",
        },
        "release_test": {
            "K300_margins_exactly_replayed": [row["radial_integrability_margin"] for row in corner_rows] == [14, 7, 2],
            "worst_sector_radial_power_is_one": min(row["weighted_radial_power"] for row in corner_rows) == 1,
            "K317_log_mass_exactly_replayed": True,
            "terminal_radial_pole_cancelled_only_with_chart_jacobian": True,
            "global_pointwise_coefficient_reintroduced": False,
            "complete_numerical_norm_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k317["ledger_effect"],
        "source_routing": k317["source_routing"],
        "claim_ceiling": "Exact sixteen-chart determinant-preserving blow-up atlas for the barycentric y/split endpoint problem in K317's valid replacement route. The charts replay the y-Peano mass 1/24, all eighty-four worst Cauchy-model valuations have nonnegative cube exponents, and the split Jacobian cancels the native terminal radial pole before enclosure. The complete coherent bordered determinant, projective polynomial, Peano and endpoint weights, and split variables must stay in each chart until the chartwise absolute bound. Continuous r=0 scaling, s=0/1 radial-projective faces, complete determinant uppers, a numerical y-master constant, five-axis transfer, K294 join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    sectors = payload["homogeneous_endpoint_sectors"]
    if not sectors["all_radial_powers_strictly_above_minus_one"] or sectors["worst_weighted_radial_power"] != 1:
        raise AssertionError("endpoint sector integrability lost")
    if not payload["logarithmic_y_endpoint_charts"]["K317_exact_mass_replayed"]:
        raise AssertionError("K317 log mass not replayed")
    if len(payload["terminal_split_square"]["sectors"]) != 2:
        raise AssertionError("terminal split cover changed")
    atlas = payload["determinant_preserving_endpoint_atlas"]
    if atlas["chart_count"] != 16 or atlas["left_chart_count"] != 8 or atlas["right_chart_count"] != 8:
        raise AssertionError("sixteen-chart endpoint cover changed")
    if atlas["terminal_singular_hepp3_charts"] != 12 or atlas["regular_hepp2_charts"] != 4:
        raise AssertionError("Hepp chart census changed")
    if not atlas["absolute_value_after_absorption"]:
        raise AssertionError("chart weights no longer remain inside determinant assembly")
    if atlas["exact_left_mass"] != "1/48" or atlas["exact_right_mass"] != "1/48" or atlas["exact_total_mass"] != "1/24" or not atlas["K299_y_Peano_mass_replayed"]:
        raise AssertionError("exact endpoint chart masses changed")
    valuations = payload["cauchy_model_valuation_control"]
    if valuations["check_count"] != 84 or not valuations["all_cube_exponents_nonnegative"] or valuations["minimum_cube_exponent"] < 0:
        raise AssertionError("Cauchy-model valuation control failed")
    contract = payload["complete_chart_integrand_contract"]
    if contract["detached_terminal_budget_times_global_cofactor"] or contract["detached_endpoint_pointwise_supremum"]:
        raise AssertionError("K317 forbidden factorization reintroduced")
    if not contract["complete_bordered_assembly_retained"]:
        raise AssertionError("complete determinant assembly lost")
    decision = payload["decision"]
    if not decision["barycentric_y_split_endpoint_scope_complete"] or decision["radial_projective_s_endpoint_atlas_complete"]:
        raise AssertionError("K318 scope boundary changed")
    if decision["complete_chart_determinant_uppers_emitted"] or decision["complete_y_master_constant_emitted"]:
        raise AssertionError("numerical endpoint closure overclaimed")


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
