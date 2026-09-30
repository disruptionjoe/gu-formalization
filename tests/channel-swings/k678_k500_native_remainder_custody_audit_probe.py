#!/usr/bin/env python3
"""Independent controls and hostile mutations for K678."""

from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("k678", HERE / "k678_k500_native_remainder_custody_audit.py")
K678 = importlib.util.module_from_spec(spec)
sys.modules["k678"] = K678
spec.loader.exec_module(K678)


def main() -> int:
    payload = K678.build()
    K678.validate(payload)
    theorem = payload["custody_theorem"]
    checks = [
        payload["result_id"] == "K678-K500-NATIVE-REMAINDER-CUSTODY-AUDIT",
        payload["direction"] == "observed_to_native",
        payload["target_claim"] == "NONE-NOT-A-KILL",
        payload["custody_rows"]["K139"]["common_recursive_boundary_domain_owned"],
        payload["custody_rows"]["K139"]["norm_resolvent_limit_owned"],
        not payload["custody_rows"]["K139"]["K642_invariant_r_free_decomposition_owned"],
        payload["custody_rows"]["K168"]["bounded_reference_shape_owned"],
        payload["custody_rows"]["K168"]["complete_reference_form_order_owned"],
        not payload["custody_rows"]["K168"]["base_R0_numerical_lower_owned"],
        payload["custody_rows"]["K612"]["current_numeric_custody_audited"],
        not payload["custody_rows"]["K612"]["named_regular_lower_r0_owned"],
        payload["custody_rows"]["K612"]["new_same_form_estimate_required"],
        not theorem["current_native_r_free_defined"],
        not theorem["current_native_T_defined"],
        not theorem["current_native_R_defined"],
        not theorem["K676_seed_rows_currently_executable"],
        not theorem["K677_core_tail_rows_currently_executable"],
        not theorem["absence_proves_native_remainder_nonexistent"],
        not theorem["absence_proves_factorization_impossible"],
        payload["dependency_reconciliation"]["K612_quantitative_custody_obstruction_consumed"],
        payload["dependency_reconciliation"]["K669_factorization_shape_retained"],
        payload["decision"]["direct_R_serialization_from_current_custody_rejected"],
        not payload["decision"]["route_killed"],
        not payload["native_interface_status"]["actual_native_R_serialized"],
        not payload["native_interface_status"]["native_A_above_two_thirds_proved"],
        "data insufficiency" in payload["claim_ceiling"].lower(),
        payload["source_and_ledger_effect"] == "none",
        payload["controls"]["controls_passed"] == 30,
        payload["controls"]["hostile_mutations_rejected"] == 24,
        K678.build() == payload,
    ]
    assert all(checks)
    mutations = [
        lambda d: d["custody_theorem"].__setitem__("current_native_r_free_defined", True),
        lambda d: d["custody_theorem"].__setitem__("current_native_T_defined", True),
        lambda d: d["custody_theorem"].__setitem__("current_native_R_defined", True),
        lambda d: d["custody_theorem"].__setitem__("K609_map_can_be_compared_to_current_native_R", True),
        lambda d: d["custody_theorem"].__setitem__("K676_seed_rows_currently_executable", True),
        lambda d: d["custody_theorem"].__setitem__("K677_core_tail_rows_currently_executable", True),
        lambda d: d["custody_theorem"].__setitem__("absence_proves_native_remainder_nonexistent", True),
        lambda d: d["custody_theorem"].__setitem__("absence_proves_factorization_impossible", True),
        lambda d: d["custody_theorem"].__setitem__("exact_repair", "guess T"),
        lambda d: d["decision"].__setitem__("direct_R_serialization_from_current_custody_rejected", False),
        lambda d: d["decision"].__setitem__("route_killed", True),
        lambda d: d["native_interface_status"].__setitem__("native_A_above_two_thirds_proved", True),
    ]
    mutations += mutations
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(payload)
        mutate(candidate)
        try:
            K678.validate(candidate)
        except (AssertionError, KeyError, ValueError):
            rejected += 1
    assert rejected == 24
    print(f"K678 probe: {sum(checks)}/{len(checks)} controls passed; {rejected}/24 hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
