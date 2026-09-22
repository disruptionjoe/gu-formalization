#!/usr/bin/env python3
"""Independent replay and hostile controls for K318."""

from __future__ import annotations

import copy
import importlib.util
import math
from pathlib import Path


MODULE = Path(__file__).with_name("k318_order_seven_weighted_endpoint_blowup_atlas.py")


def load_module():
    spec = importlib.util.spec_from_file_location("k318_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K318 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    payload = module.build()
    module.validate_payload(payload)
    rows = payload["homogeneous_endpoint_sectors"]["rows"]
    checks = {
        "old_positions": [row["old_position"] for row in rows] == [2, 4, 6],
        "margins": [row["radial_integrability_margin"] for row in rows] == [14, 7, 2],
        "powers": [row["weighted_radial_power"] for row in rows] == [13, 6, 1],
        "sector_count": payload["homogeneous_endpoint_sectors"]["finite_sector_count"] == 9,
        "split_sector_count": len(payload["terminal_split_square"]["sectors"]) == 2,
        "split_overlap": payload["terminal_split_square"]["measure_zero_overlap"] == "a=b",
        "endpoint_charts": payload["determinant_preserving_endpoint_atlas"]["chart_count"] == 16,
        "endpoint_split": payload["determinant_preserving_endpoint_atlas"]["left_chart_count"] == payload["determinant_preserving_endpoint_atlas"]["right_chart_count"] == 8,
        "hepp_census": payload["determinant_preserving_endpoint_atlas"]["terminal_singular_hepp3_charts"] == 12 and payload["determinant_preserving_endpoint_atlas"]["regular_hepp2_charts"] == 4,
        "weight_inside": payload["determinant_preserving_endpoint_atlas"]["absolute_value_after_absorption"],
        "exact_mass": payload["determinant_preserving_endpoint_atlas"]["exact_left_mass"] == payload["determinant_preserving_endpoint_atlas"]["exact_right_mass"] == "1/48" and payload["determinant_preserving_endpoint_atlas"]["exact_total_mass"] == "1/24",
        "valuation_count": payload["cauchy_model_valuation_control"]["check_count"] == 84,
        "valuation_nonnegative": payload["cauchy_model_valuation_control"]["all_cube_exponents_nonnegative"] and payload["cauchy_model_valuation_control"]["minimum_cube_exponent"] >= 0,
        "scope_boundary": payload["decision"]["barycentric_y_split_endpoint_scope_complete"] and not payload["decision"]["radial_projective_s_endpoint_atlas_complete"],
        "left_log_map": "exp(-t)" in payload["logarithmic_y_endpoint_charts"]["left"]["map"],
        "right_log_map": "exp(-t)" in payload["logarithmic_y_endpoint_charts"]["right"]["map"],
        "log_mass": math.isclose(float(payload["logarithmic_y_endpoint_charts"]["tail_at_log2_decimal"]), math.log(2) / 24 + 1 / 72, rel_tol=0, abs_tol=2e-16),
        "complete_assembly": payload["complete_chart_integrand_contract"]["complete_bordered_assembly_retained"],
        "no_pointwise_sup": not payload["complete_chart_integrand_contract"]["detached_endpoint_pointwise_supremum"],
        "no_release": not payload["decision"]["complete_y_master_constant_emitted"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K318 independent checks failed: {checks}")

    mutations = []
    for mutate in (
        lambda p: p["homogeneous_endpoint_sectors"].__setitem__("worst_weighted_radial_power", -1),
        lambda p: p["homogeneous_endpoint_sectors"].__setitem__("all_radial_powers_strictly_above_minus_one", False),
        lambda p: p["logarithmic_y_endpoint_charts"].__setitem__("K317_exact_mass_replayed", False),
        lambda p: p["terminal_split_square"].__setitem__("sectors", p["terminal_split_square"]["sectors"][:1]),
        lambda p: p["determinant_preserving_endpoint_atlas"].__setitem__("chart_count", 15),
        lambda p: p["determinant_preserving_endpoint_atlas"].__setitem__("terminal_singular_hepp3_charts", 11),
        lambda p: p["determinant_preserving_endpoint_atlas"].__setitem__("absolute_value_after_absorption", False),
        lambda p: p["determinant_preserving_endpoint_atlas"].__setitem__("exact_total_mass", "1/12"),
        lambda p: p["determinant_preserving_endpoint_atlas"].__setitem__("K299_y_Peano_mass_replayed", False),
        lambda p: p["cauchy_model_valuation_control"].__setitem__("check_count", 83),
        lambda p: p["cauchy_model_valuation_control"].__setitem__("all_cube_exponents_nonnegative", False),
        lambda p: p["decision"].__setitem__("radial_projective_s_endpoint_atlas_complete", True),
        lambda p: p["complete_chart_integrand_contract"].__setitem__("detached_terminal_budget_times_global_cofactor", True),
        lambda p: p["complete_chart_integrand_contract"].__setitem__("detached_endpoint_pointwise_supremum", True),
        lambda p: p["complete_chart_integrand_contract"].__setitem__("complete_bordered_assembly_retained", False),
        lambda p: p["decision"].__setitem__("complete_chart_determinant_uppers_emitted", True),
        lambda p: p["decision"].__setitem__("complete_y_master_constant_emitted", True),
    ):
        candidate = copy.deepcopy(payload)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            mutations.append(True)
        else:
            mutations.append(False)
    if not all(mutations):
        raise AssertionError(f"K318 hostile controls escaped: {mutations}")
    print(f"K318 probe passed {len(checks)}/{len(checks)} checks and rejected {len(mutations)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
