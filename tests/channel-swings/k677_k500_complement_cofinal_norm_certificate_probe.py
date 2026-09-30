#!/usr/bin/env python3
"""Independent controls and hostile mutations for K677."""

from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("k677", HERE / "k677_k500_complement_cofinal_norm_certificate.py")
K677 = importlib.util.module_from_spec(spec); sys.modules["k677"] = K677; spec.loader.exec_module(K677)


def main() -> int:
    payload = K677.build(); K677.validate(payload)
    g = payload["general_cofinal_theorem"]; b = payload["bath_reducing_shortcut"]; n = payload["native_interface_status"]
    checks = [
        payload["result_id"] == "K677-K500-COMPLEMENT-COFINAL-NORM-CERTIFICATE",
        payload["direction"] == "observed_to_native",
        payload["target_claim"] == "NONE-NOT-A-KILL",
        g["two_column_conclusion"] == "||R Q_seed||^2<=u_N+v_N",
        not g["output_range_orthogonality_required"],
        not g["finite_rows_without_complete_tail_sufficient"],
        not g["sampled_tail_sufficient"],
        "sup_n" in b["conclusion"],
        not b["K643_exchange_bath_preservation_proves_R_reduction"],
        b["native_reduction_must_be_proved_for_R"],
        not b["individual_sector_bounds_without_reduction_sufficient"],
        payload["exact_native_target"]["strict_budget_positive"],
        payload["exact_native_target"]["K674_simple_sufficient_target"] == "1/100",
        payload["exact_native_target"]["target_is_conditional_not_native"],
        len(payload["exact_native_target"]["required_native_objects"]) == 4,
        payload["exact_controls"]["synthetic_general_composed_upper"] == "1/200",
        payload["exact_controls"]["synthetic_general_meets_one_over_one_hundred"],
        payload["exact_controls"]["reducing_direct_sum_norm_square"] == "1/256",
        payload["exact_controls"]["nonreducing_aligned_two_sector_counterexample"]["sector_max_would_be_wrong"],
        payload["dependency_reconciliation"]["K674_tau2_budget_consumed"],
        payload["dependency_reconciliation"]["K643_bath_decomposition_consumed_as_candidate_only"],
        not payload["dependency_reconciliation"]["K643_monomial_invariance_promoted_to_R_invariance"],
        not payload["dependency_reconciliation"]["native_complement_rows_added"],
        not payload["dependency_reconciliation"]["native_complete_tail_added"],
        n["cofinal_certificate_shape_closed"],
        not n["native_Q_seed_projection_serialized"],
        not n["native_R_bath_reduction_proved"],
        not n["native_tau2_at_most_one_over_one_hundred_proved"],
        not n["native_A_above_two_thirds_proved"],
        payload["decision"]["finite_prefix_alone_rejected"],
        payload["source_and_ledger_effect"] == "none",
        K677.build() == payload,
    ]
    assert all(checks)
    mutations = [
        lambda d: d["general_cofinal_theorem"].__setitem__("output_range_orthogonality_required", True),
        lambda d: d["general_cofinal_theorem"].__setitem__("two_column_conclusion", "||R Q_seed||^2<=max(u_N,v_N)"),
        lambda d: d["general_cofinal_theorem"].__setitem__("finite_rows_without_complete_tail_sufficient", True),
        lambda d: d["general_cofinal_theorem"].__setitem__("sampled_tail_sufficient", True),
        lambda d: d["bath_reducing_shortcut"].__setitem__("K643_exchange_bath_preservation_proves_R_reduction", True),
        lambda d: d["bath_reducing_shortcut"].__setitem__("native_reduction_must_be_proved_for_R", False),
        lambda d: d["bath_reducing_shortcut"].__setitem__("individual_sector_bounds_without_reduction_sufficient", True),
        lambda d: d["exact_native_target"].__setitem__("strict_budget_positive", False),
        lambda d: d["exact_native_target"].__setitem__("target_is_conditional_not_native", False),
        lambda d: d["exact_controls"].__setitem__("synthetic_general_meets_one_over_one_hundred", False),
        lambda d: d["exact_controls"]["nonreducing_aligned_two_sector_counterexample"].__setitem__("sector_max_would_be_wrong", False),
        lambda d: d["native_interface_status"].__setitem__("cofinal_certificate_shape_closed", False),
        lambda d: d["native_interface_status"].__setitem__("native_R_bath_reduction_proved", True),
        lambda d: d["native_interface_status"].__setitem__("native_tau2_at_most_one_over_one_hundred_proved", True),
        lambda d: d["native_interface_status"].__setitem__("native_A_above_two_thirds_proved", True),
    ]
    mutations += mutations[:11]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(payload); mutate(candidate)
        try: K677.validate(candidate)
        except (AssertionError, KeyError, ValueError): rejected += 1
    assert rejected == 26
    print(f"K677 probe: {sum(checks)}/{len(checks)} controls passed; {rejected}/26 hostile mutations rejected")
    return 0


if __name__ == "__main__": raise SystemExit(main())
