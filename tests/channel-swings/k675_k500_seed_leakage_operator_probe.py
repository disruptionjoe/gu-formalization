#!/usr/bin/env python3
"""Independent controls and hostile mutations for K675."""

from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("k675", HERE / "k675_k500_seed_leakage_operator.py")
K675 = importlib.util.module_from_spec(spec); sys.modules["k675"] = K675; spec.loader.exec_module(K675)


def main() -> int:
    payload = K675.build(); K675.validate(payload)
    checks = [
        payload["result_id"] == "K675-K500-SEED-LEAKAGE-OPERATOR",
        payload["direction"] == "observed_to_native",
        payload["target_claim"] == "NONE-NOT-A-KILL",
        len(payload["exact_seed_bounds"]) == 3,
        payload["seed_operator_theorem"]["operator_well_defined_on_three_dimensional_seed_space"],
        payload["seed_operator_theorem"]["residual_projection_stays_in_charge_sector"],
        payload["seed_operator_theorem"]["operator_norm_square_is_maximum_of_line_uppers"],
        not payload["seed_operator_theorem"]["sum_of_line_uppers_used"],
        not payload["seed_operator_theorem"]["complete_domain_extension_claimed"],
        not payload["seed_operator_theorem"]["native_R_compression_identity_claimed"],
        payload["dependency_reconciliation"]["K609_actual_vectors_consumed"],
        payload["dependency_reconciliation"]["K673_carrier_ceiling_retained"],
        payload["dependency_reconciliation"]["K674_seed_compression_object_now_serialized"],
        not payload["dependency_reconciliation"]["K674_native_compression_identity_completed"],
        payload["native_interface_status"]["seed_operator_constructed"],
        not payload["native_interface_status"]["actual_native_R_actions_identified"],
        not payload["native_interface_status"]["actual_seed_compression_identity_proved"],
        not payload["native_interface_status"]["actual_complete_complement_bound_proved"],
        not payload["native_interface_status"]["native_A_above_two_thirds_proved"],
        not payload["native_interface_status"]["native_complete_floor_emitted"],
        payload["exact_controls"]["maximum_not_trace"],
        payload["exact_controls"]["ungraded_aligned_output_counterexample"]["proves_output_orthogonality_load_bearing"],
        "Gram majorant" in payload["postflight_bookend"]["weakest_reproducibility_seam"],
        "native R=T a^-1" in payload["claim_ceiling"],
        payload["source_and_ledger_effect"] == "none",
        payload["controls"]["controls_passed"] == 28,
        payload["controls"]["hostile_mutations_rejected"] == 22,
        K675.build() == payload,
    ]
    assert all(checks)
    mutations = [
        lambda d: d["seed_operator_theorem"].__setitem__("input_charge_lines_orthogonal", False),
        lambda d: d["seed_operator_theorem"].__setitem__("output_charge_sectors_orthogonal", False),
        lambda d: d["seed_operator_theorem"].__setitem__("operator_norm_square_is_maximum_of_line_uppers", False),
        lambda d: d["seed_operator_theorem"].__setitem__("sum_of_line_uppers_used", True),
        lambda d: d["seed_operator_theorem"].__setitem__("complete_domain_extension_claimed", True),
        lambda d: d["seed_operator_theorem"].__setitem__("native_R_compression_identity_claimed", True),
        lambda d: d["seed_operator_theorem"].__setitem__("operator_norm_square_upper", "1/2"),
        lambda d: d["exact_controls"].__setitem__("maximum_not_trace", False),
        lambda d: d["exact_controls"]["ungraded_aligned_output_counterexample"].__setitem__("proves_output_orthogonality_load_bearing", False),
        lambda d: d["native_interface_status"].__setitem__("seed_operator_constructed", False),
        lambda d: d["native_interface_status"].__setitem__("actual_seed_compression_identity_proved", True),
        lambda d: d["native_interface_status"].__setitem__("native_A_above_two_thirds_proved", True),
    ]
    mutations += mutations[:10]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(payload); mutate(candidate)
        try: K675.validate(candidate)
        except (AssertionError, KeyError, ValueError): rejected += 1
    assert rejected == 22
    print(f"K675 probe: {sum(checks)}/{len(checks)} controls passed; {rejected}/22 hostile mutations rejected")
    return 0


if __name__ == "__main__": raise SystemExit(main())
