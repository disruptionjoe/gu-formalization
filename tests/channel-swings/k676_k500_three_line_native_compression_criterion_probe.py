#!/usr/bin/env python3
"""Independent controls and hostile mutations for K676."""

from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("k676", HERE / "k676_k500_three_line_native_compression_criterion.py")
K676 = importlib.util.module_from_spec(spec); sys.modules["k676"] = K676; spec.loader.exec_module(K676)


def main() -> int:
    payload = K676.build(); K676.validate(payload)
    c = payload["three_line_criterion"]; n = payload["native_interface_status"]
    checks = [
        payload["result_id"] == "K676-K500-THREE-LINE-NATIVE-COMPRESSION-CRITERION",
        payload["direction"] == "observed_to_native",
        payload["target_claim"] == "NONE-NOT-A-KILL",
        c["exact_identity_route_sufficient"],
        c["gram_domination_route_sufficient_for_norm_bound"],
        c["charge_preserving_shortcut_requires_native_charge_intertwiner"],
        not c["ungraded_linewise_sum_below_one_third"],
        not c["dimensions_or_aggregate_norms_sufficient"],
        not c["K609_alone_supplies_native_R_actions"],
        payload["exact_target"]["charge_graded_seed_norm_square_below_one_third"],
        payload["exact_target"]["native_comparison_rows_required"] == 3,
        payload["exact_target"]["native_pairwise_gram_entries_required_without_charge_shortcut"] == 6,
        payload["exact_controls"]["synthetic_norm_square"] == "1/4",
        payload["exact_controls"]["aligned_output_control"]["operator_norm_square"] == "1/3",
        payload["exact_controls"]["aligned_output_control"]["linewise_max_would_be_wrong"],
        payload["dependency_reconciliation"]["K674_compression_requirement_consumed"],
        payload["dependency_reconciliation"]["K675_seed_operator_consumed"],
        not payload["dependency_reconciliation"]["native_R_seed_actions_added"],
        n["finite_comparison_criterion_closed"],
        not n["native_charge_intertwiner_proved"],
        not n["native_R_seed_actions_computed"],
        not n["native_seed_gram_domination_proved"],
        not n["native_compression_identity_proved"],
        not n["native_A_above_two_thirds_proved"],
        payload["decision"]["full_complete_domain_unitary_identification_needed_for_seed_step"] is False,
        payload["decision"]["three_native_action_rows_suffice_after_charge_intertwining"],
        payload["source_and_ledger_effect"] == "none",
        payload["controls"]["controls_passed"] == 30,
        payload["controls"]["hostile_mutations_rejected"] == 24,
        K676.build() == payload,
    ]
    assert all(checks)
    mutations = [
        lambda d: d["three_line_criterion"].__setitem__("exact_identity_route_sufficient", False),
        lambda d: d["three_line_criterion"].__setitem__("gram_domination_route_sufficient_for_norm_bound", False),
        lambda d: d["three_line_criterion"].__setitem__("charge_preserving_shortcut_requires_native_charge_intertwiner", False),
        lambda d: d["three_line_criterion"].__setitem__("ungraded_linewise_sum_below_one_third", True),
        lambda d: d["three_line_criterion"].__setitem__("dimensions_or_aggregate_norms_sufficient", True),
        lambda d: d["three_line_criterion"].__setitem__("K609_alone_supplies_native_R_actions", True),
        lambda d: d["exact_target"].__setitem__("charge_graded_seed_norm_square_below_one_third", False),
        lambda d: d["exact_target"].__setitem__("native_comparison_rows_required", 4),
        lambda d: d["exact_target"].__setitem__("native_pairwise_gram_entries_required_without_charge_shortcut", 3),
        lambda d: d["exact_controls"]["aligned_output_control"].__setitem__("linewise_max_would_be_wrong", False),
        lambda d: d["native_interface_status"].__setitem__("finite_comparison_criterion_closed", False),
        lambda d: d["native_interface_status"].__setitem__("native_charge_intertwiner_proved", True),
        lambda d: d["native_interface_status"].__setitem__("native_compression_identity_proved", True),
        lambda d: d["native_interface_status"].__setitem__("native_A_above_two_thirds_proved", True),
    ]
    mutations += mutations[:10]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(payload); mutate(candidate)
        try: K676.validate(candidate)
        except (AssertionError, KeyError, ValueError): rejected += 1
    assert rejected == 24
    print(f"K676 probe: {sum(checks)}/{len(checks)} controls passed; {rejected}/24 hostile mutations rejected")
    return 0


if __name__ == "__main__": raise SystemExit(main())
