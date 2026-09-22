#!/usr/bin/env python3
"""Independent replay and hostile controls for K324."""

from __future__ import annotations

import copy
import importlib.util
import math
from pathlib import Path


MODULE = Path(__file__).with_name("k324_order_seven_complete_value_chart_bank.py")


def load_module():
    spec = importlib.util.spec_from_file_location("k324_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K324 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    payload = module.build()
    module.validate_payload(payload)
    bank = payload["complete_value_chart_bank"]
    rows = bank["rows"]
    checks = {
        "census": len(rows) == 16 and len({row["chart_id"] for row in rows}) == 16,
        "source_order": [row["chart_id"] for row in rows] == bank["source_chart_ids"],
        "left_count": sum(row["endpoint"] == "left" for row in rows) == 8,
        "right_count": sum(row["endpoint"] == "right" for row in rows) == 8,
        "left_column": all(row["endpoint_weight_placement"] == "border column 4" for row in rows if row["endpoint"] == "left"),
        "right_row": all(row["endpoint_weight_placement"] == "border row 4" for row in rows if row["endpoint"] == "right"),
        "terminal_upper": bank["node_audit"]["terminal_scaled_upper"] == "4",
        "no_raw_zero": not bank["node_audit"]["raw_Bessel_evaluation_at_zero_used"],
        "finite": all(math.isfinite(float(row["four_group_weighted_chart_abs_upper"])) and float(row["four_group_weighted_chart_abs_upper"]) > 0 for row in rows),
        "finite_sum": math.isfinite(float(bank["sixteen_chart_weighted_abs_upper"])) and float(bank["sixteen_chart_weighted_abs_upper"]) > 0,
        "mass_census": bank["exact_chart_masses_are_census_not_extra_multiplier"],
        "absorbed": bank["terminal_weight_absorbed_before_determinant_bound"] and bank["Peano_Hepp_weight_absorbed_before_determinant_bound"],
        "no_permutations": not bank["permutation_or_monomial_absolute_values_used"],
        "no_detached": not bank["detached_terminal_cofactor_used"],
        "scope": payload["scope_boundary"]["fixed_slab_bank_is_not_global_release"],
        "no_signed_release": not payload["decision"]["signed_first_and_second_jet_backend_complete"],
        "no_master_release": not payload["decision"]["complete_y_master_constant_emitted"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K324 independent checks failed: {checks}")

    mutations = []
    mutators = (
        lambda p: p["complete_value_chart_bank"]["rows"].pop(),
        lambda p: p["complete_value_chart_bank"]["rows"][1].__setitem__("chart_id", p["complete_value_chart_bank"]["rows"][0]["chart_id"]),
        lambda p: p["complete_value_chart_bank"]["rows"][0].__setitem__("endpoint_weight_placement", "border row 4"),
        lambda p: p["complete_value_chart_bank"]["rows"][8].__setitem__("endpoint_weight_placement", "border column 4"),
        lambda p: p["complete_value_chart_bank"]["rows"][0].__setitem__("four_group_weighted_chart_abs_upper", "inf"),
        lambda p: p["complete_value_chart_bank"]["node_audit"].__setitem__("terminal_scaled_upper", "2"),
        lambda p: p["complete_value_chart_bank"]["node_audit"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["complete_value_chart_bank"].__setitem__("terminal_weight_absorbed_before_determinant_bound", False),
        lambda p: p["complete_value_chart_bank"].__setitem__("Peano_Hepp_weight_absorbed_before_determinant_bound", False),
        lambda p: p["complete_value_chart_bank"].__setitem__("permutation_or_monomial_absolute_values_used", True),
        lambda p: p["complete_value_chart_bank"].__setitem__("detached_terminal_cofactor_used", True),
        lambda p: p["complete_value_chart_bank"].__setitem__("all_literal_border_zeros_retained", False),
        lambda p: p["complete_value_chart_bank"].__setitem__("exact_chart_masses_are_census_not_extra_multiplier", False),
        lambda p: p["scope_boundary"].__setitem__("fixed_slab_bank_is_not_global_release", False),
        lambda p: p["decision"].__setitem__("signed_first_and_second_jet_backend_complete", True),
        lambda p: p["decision"].__setitem__("complete_y_master_constant_emitted", True),
    )
    for mutate in mutators:
        candidate = copy.deepcopy(payload)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except (AssertionError, ValueError):
            mutations.append(True)
        else:
            mutations.append(False)
    if not all(mutations):
        raise AssertionError(f"K324 hostile controls escaped: {mutations}")
    print(f"K324 probe passed {len(checks)}/{len(checks)} checks and rejected {len(mutations)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
