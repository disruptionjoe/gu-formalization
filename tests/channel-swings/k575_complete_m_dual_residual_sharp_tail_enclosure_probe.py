#!/usr/bin/env python3
"""Independent controls and hostile mutations for K575."""

from __future__ import annotations

import copy
import importlib.util
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k575_probe_target", HERE / "k575_complete_m_dual_residual_sharp_tail_enclosure.py")
K575 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(K575)


def checks(payload: dict) -> list[bool]:
    result = payload["complete_M_dual_residual_norm_square"]
    comparison = payload["comparison_to_K570"]
    decision = payload["decision"]
    lower, upper = map(Fraction, result["interval_exact"])
    return [
        payload["result_id"] == "K575-COMPLETE-M-DUAL-RESIDUAL-SHARP-TAIL-ENCLOSURE",
        payload["fixed_control"]["resolved_vectors"] == 2958,
        payload["fixed_control"]["coherent_groups"] == 201,
        payload["fixed_control"]["self_and_cross_entries"] == 59586,
        0 < lower <= upper,
        result["strictly_positive_lower_endpoint"] is True,
        result["finite_lower_norm_exceeds_sharp_tail"] is True,
        comparison["new_lower_strictly_improves"] is True,
        comparison["new_upper_strictly_improves"] is True,
        comparison["K570_finite_square_unchanged"] is True,
        comparison["only_tail_input_changed"] is True,
        decision["complete_M_dual_residual_numerically_enclosed"] is True,
        decision["complete_M_dual_residual_proved_nonzero"] is True,
        decision["trial_is_not_exact_for_the_fixed_M_dual_operator"] is True,
        decision["K152_shifted_form_dual_residual_emitted"] is False,
        decision["native_K152_interval_emitted"] is False,
        decision["spectral_error_lower_bound_emitted"] is False,
        payload["source_and_ledger_effect"] == "none",
    ]


def main() -> int:
    payload = K575.build()
    controls = checks(payload)
    rejected = 0
    mutations = [
        lambda p: p["complete_M_dual_residual_norm_square"]["interval_exact"].__setitem__(0, "0"),
        lambda p: p["complete_M_dual_residual_norm_square"].__setitem__("strictly_positive_lower_endpoint", False),
        lambda p: p["complete_M_dual_residual_norm_square"].__setitem__("finite_lower_norm_exceeds_sharp_tail", False),
        lambda p: p["comparison_to_K570"].__setitem__("new_lower_strictly_improves", False),
        lambda p: p["comparison_to_K570"].__setitem__("new_upper_strictly_improves", False),
        lambda p: p["comparison_to_K570"].__setitem__("K570_finite_square_unchanged", False),
        lambda p: p["decision"].__setitem__("complete_M_dual_residual_proved_nonzero", False),
        lambda p: p["decision"].__setitem__("trial_is_not_exact_for_the_fixed_M_dual_operator", False),
        lambda p: p["decision"].__setitem__("K152_shifted_form_dual_residual_emitted", True),
        lambda p: p["decision"].__setitem__("spectral_error_lower_bound_emitted", True),
    ]
    for mutate in mutations:
        hostile = copy.deepcopy(payload)
        mutate(hostile)
        try:
            K575.validate(hostile)
        except AssertionError:
            rejected += 1
    print(f"K575 controls: {sum(controls)}/{len(controls)}; hostile: {rejected}/{len(mutations)}")
    return 0 if all(controls) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
