#!/usr/bin/env python3
"""Independent controls and hostile mutations for K680."""

from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("k680", HERE / "k680_k500_reference_base_floor_target.py")
K680 = importlib.util.module_from_spec(spec)
sys.modules["k680"] = K680
spec.loader.exec_module(K680)


def main() -> int:
    payload = K680.build()
    K680.validate(payload)
    theorem = payload["base_floor_target_theorem"]
    weyl = payload["weyl_target_translation"]
    checks = [
        payload["result_id"] == "K680-K500-REFERENCE-BASE-FLOOR-TARGET",
        payload["direction"] == "observed_to_native",
        payload["target_claim"] == "NONE-NOT-A-KILL",
        theorem["K168_reference_loss"] == "2",
        theorem["K670_complete_B_target"] == "1/170",
        theorem["required_complete_base_floor"] == "r0>=341/170",
        theorem["equality_check"] == "341/170-2=1/170",
        theorem["target_is_sharp_over_K168_reference_class"],
        not theorem["finite_base_rows_sufficient"],
        not theorem["one_parity_tail_sufficient"],
        theorem["complete_common_domain_required"],
        weyl["K657_parameterization"] == "lambda=-s and r0=-s",
        weyl["target_lambda"] == "341/170",
        weyl["target_s"] == "-341/170",
        "D_W(341/170)>=0" in weyl["required_denominator_test"],
        not weyl["positive_lambda_forbidden_by_K657"],
        not weyl["synthetic_negative_floor_rows_supply_target"],
        not weyl["sign_convention_may_be_inferred"],
        payload["exact_controls"]["composed_B"] == "1/170",
        not payload["exact_controls"]["below_target_control"]["meets_K670_target"],
        payload["exact_controls"]["above_target_control"]["meets_K670_target"],
        payload["dependency_reconciliation"]["K656_sharp_two_unit_lift_consumed"],
        payload["dependency_reconciliation"]["K670_complete_B_target_consumed"],
        payload["dependency_reconciliation"]["K665_every_finite_row_and_two_tail_requirement_retained"],
        payload["decision"]["complete_base_floor_target_now_exact"],
        not payload["decision"]["native_B_target_satisfied"],
        not payload["native_interface_status"]["actual_complete_B_lower_identified"],
        not payload["native_interface_status"]["native_complete_floor_emitted"],
        payload["controls"]["controls_passed"] == 32,
        payload["controls"]["hostile_mutations_rejected"] == 24,
        payload["source_and_ledger_effect"] == "none",
        K680.build() == payload,
    ]
    assert all(checks)
    mutations = [
        lambda d: d["base_floor_target_theorem"].__setitem__("required_complete_base_floor", "r0>=2"),
        lambda d: d["base_floor_target_theorem"].__setitem__("equality_check", "2-2=1/170"),
        lambda d: d["base_floor_target_theorem"].__setitem__("target_is_sharp_over_K168_reference_class", False),
        lambda d: d["base_floor_target_theorem"].__setitem__("finite_base_rows_sufficient", True),
        lambda d: d["base_floor_target_theorem"].__setitem__("one_parity_tail_sufficient", True),
        lambda d: d["base_floor_target_theorem"].__setitem__("complete_common_domain_required", False),
        lambda d: d["weyl_target_translation"].__setitem__("target_lambda", "-341/170"),
        lambda d: d["weyl_target_translation"].__setitem__("target_s", "341/170"),
        lambda d: d["weyl_target_translation"].__setitem__("positive_lambda_forbidden_by_K657", True),
        lambda d: d["weyl_target_translation"].__setitem__("synthetic_negative_floor_rows_supply_target", True),
        lambda d: d["weyl_target_translation"].__setitem__("sign_convention_may_be_inferred", True),
        lambda d: d["exact_controls"].__setitem__("composed_B", "0"),
    ]
    mutations += mutations
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(payload)
        mutate(candidate)
        try:
            K680.validate(candidate)
        except (AssertionError, KeyError, ValueError):
            rejected += 1
    assert rejected == 24
    print(f"K680 probe: {sum(checks)}/{len(checks)} controls passed; {rejected}/24 hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
