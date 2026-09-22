#!/usr/bin/env python3
"""Independent replay and hostile controls for K319."""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path


MODULE = Path(__file__).with_name("k319_order_seven_weighted_chart_composition.py")


def load_module():
    spec = importlib.util.spec_from_file_location("k319_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K319 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    payload = module.build()
    module.validate_payload(payload)
    rows = payload["complete_family_chart_compilation"]
    checks = {
        "families": len(rows) == 21,
        "orders": {order: sum(row["y_derivative_order"] == order for row in rows) for order in (0, 1, 2)} == {0: 1, 1: 5, 2: 15},
        "monomials": payload["census"]["weighted_nonzero_determinant_monomials"] == 1674,
        "terminal_histogram": payload["census"]["terminal_monomials_by_jet_order_with_cross_factors"] == {"0": 378, "1": 162, "2": 18},
        "second_terminal_histogram": payload["census"]["second_family_terminal_monomials_by_jet_order_with_cross_factors"] == {"0": 288, "1": 144, "2": 18},
        "endpoint_chart_count": payload["fixed_control"]["K318_endpoint_chart_count"] == 16,
        "all_endpoint_charts": payload["sufficiency_audit"]["every_family_has_all_sixteen_endpoint_charts"],
        "structural_integrability": payload["sufficiency_audit"]["all_chart_weights_structurally_integrable"],
        "numerical_missing": not payload["sufficiency_audit"]["all_complete_chart_determinant_uppers_available"],
        "coverage_missing": payload["sufficiency_audit"]["barycentric_y_split_atlas_complete"] and not payload["sufficiency_audit"]["radial_projective_s_endpoint_atlas_complete"],
        "cross_two": payload["composition_contract"]["cross_factor_two_retained"],
        "zeros": payload["composition_contract"]["literal_border_zeros_retained"],
        "signed_second_sum": payload["composition_contract"]["all_fifteen_second_families_summed_before_absolute_value"],
        "no_detached": not payload["composition_contract"]["detached_global_coefficient_used"],
        "no_release": not payload["decision"]["complete_y_master_constant_emitted"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K319 independent checks failed: {checks}")

    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("bordered_family_count", 20),
        lambda p: p["fixed_control"].__setitem__("y_derivative_family_counts", {"0": 1, "1": 5, "2": 14}),
        lambda p: p["fixed_control"].__setitem__("K318_endpoint_chart_count", 15),
        lambda p: p["census"].__setitem__("K315_weighted_monomial_census_replayed", False),
        lambda p: p["census"].__setitem__("K315_terminal_histogram_replayed", False),
        lambda p: p["census"].__setitem__("second_family_terminal_monomials_by_jet_order_with_cross_factors", {"0": 287, "1": 144, "2": 18}),
        lambda p: p["composition_contract"].__setitem__("detached_cofactor_used", True),
        lambda p: p["composition_contract"].__setitem__("detached_global_coefficient_used", True),
        lambda p: p["composition_contract"].__setitem__("occurrencewise_coherent_absolute_values_used", True),
        lambda p: p["composition_contract"].__setitem__("cross_factor_two_retained", False),
        lambda p: p["composition_contract"].__setitem__("literal_border_zeros_retained", False),
        lambda p: p["composition_contract"].__setitem__("all_fifteen_second_families_summed_before_absolute_value", False),
        lambda p: p["sufficiency_audit"].__setitem__("every_family_has_all_sixteen_endpoint_charts", False),
        lambda p: p["sufficiency_audit"].__setitem__("all_complete_chart_determinant_uppers_available", True),
        lambda p: p["sufficiency_audit"].__setitem__("radial_projective_s_endpoint_atlas_complete", True),
        lambda p: p["decision"].__setitem__("complete_y_master_inputs_sufficient", True),
        lambda p: p["decision"].__setitem__("complete_y_master_constant_emitted", True),
        lambda p: p["decision"].__setitem__("five_gap_axis_transfer_released", True),
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
        raise AssertionError(f"K319 hostile controls escaped: {mutations}")
    print(f"K319 probe passed {len(checks)}/{len(checks)} checks and rejected {len(mutations)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
