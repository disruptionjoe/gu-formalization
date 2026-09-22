#!/usr/bin/env python3
"""Independent replay and hostile controls for K323."""

from __future__ import annotations

import copy
import importlib.util
import math
from pathlib import Path


MODULE = Path(__file__).with_name("k323_order_seven_old_position_six_value_pilot.py")


def load_module():
    spec = importlib.util.spec_from_file_location("k323_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K323 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    payload = module.build()
    module.validate_payload(payload)
    bound = payload["complete_weighted_matrix_bound"]
    audit = bound["node_audit"]
    checks = {
        "chart": payload["fixed_control"]["chart_id"] == "left_a_max_hepp3_eta_A_v",
        "old_position": payload["fixed_control"]["old_position"] == 6,
        "family": payload["fixed_control"]["jet_family"] == "value",
        "positive_nonterminal": audit["all_nonterminal_argument_lowers_positive"],
        "terminal_upper": audit["terminal_scaled_upper"] == "2",
        "literal_zeros": audit["literal_zero_slots"] == [[3, 4], [4, 3], [4, 4]],
        "finite": math.isfinite(float(bound["four_group_weighted_chart_abs_upper"])) and float(bound["four_group_weighted_chart_abs_upper"]) > 0,
        "positive_density": len(bound["positive_density_factors_bounded_by_one"]) == 3,
        "absorbed": bound["terminal_weight_absorbed_before_determinant_bound"] and bound["Peano_Hepp_weight_absorbed_before_determinant_bound"],
        "no_permutations": not bound["permutation_or_monomial_absolute_values_used"],
        "no_detached": not bound["detached_terminal_cofactor_used"],
        "scope": payload["scope_boundary"]["pilot_is_not_global_release"],
        "no_release": not payload["decision"]["complete_y_master_constant_emitted"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K323 independent checks failed: {checks}")

    mutations = []
    for mutate in (
        lambda p: p["complete_weighted_matrix_bound"].__setitem__("terminal_weight_absorbed_before_determinant_bound", False),
        lambda p: p["complete_weighted_matrix_bound"].__setitem__("Peano_Hepp_weight_absorbed_before_determinant_bound", False),
        lambda p: p["complete_weighted_matrix_bound"].__setitem__("permutation_or_monomial_absolute_values_used", True),
        lambda p: p["complete_weighted_matrix_bound"].__setitem__("detached_terminal_cofactor_used", True),
        lambda p: p["complete_weighted_matrix_bound"].__setitem__("all_literal_border_zeros_retained", False),
        lambda p: p["complete_weighted_matrix_bound"].__setitem__("positive_density_factors_bounded_by_one", []),
        lambda p: p["complete_weighted_matrix_bound"]["node_audit"].__setitem__("all_nonterminal_argument_lowers_positive", False),
        lambda p: p["scope_boundary"].__setitem__("pilot_is_not_global_release", False),
        lambda p: p["decision"].__setitem__("signed_first_and_second_jet_backend_complete", True),
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
        raise AssertionError(f"K323 hostile controls escaped: {mutations}")
    print(f"K323 probe passed {len(checks)}/{len(checks)} checks and rejected {len(mutations)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
