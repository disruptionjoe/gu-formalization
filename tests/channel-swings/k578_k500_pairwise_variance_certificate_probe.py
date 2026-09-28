#!/usr/bin/env python3
"""Independent controls and hostile mutations for K578."""

from __future__ import annotations

import copy
import importlib.util
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k578_probe_target", HERE / "k578_k500_pairwise_variance_certificate.py")
K578 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(K578)


def checks(payload: dict) -> list[bool]:
    controls = payload["exact_controls"]
    decision = payload["decision"]
    return [
        payload["result_id"] == "K578-K500-PAIRWISE-VARIANCE-CERTIFICATE",
        K578.weighted_variance([1, 4], [2, -1]) == Fraction(36, 25),
        K578.pairwise_variance([1, 4], [2, -1]) == Fraction(36, 25),
        K578.oscillation_upper([2, -1]) == Fraction(9, 4),
        K578.pairwise_variance([1, 4], [9, 6]) == Fraction(36, 25),
        controls["row_count"] == 3,
        controls["all_pairwise_identities_pass"] is True,
        controls["all_oscillation_bounds_pass"] is True,
        payload["theorem"]["no_word_lower_required"] is True,
        len(payload["native_data_contract"]["required_per_level"]) == 3,
        len(payload["native_data_contract"]["forbidden_substitutions"]) == 3,
        decision["K510_factorial_path_template_bypassed"] is True,
        decision["direct_normalized_variance_route_released"] is True,
        decision["native_uniform_all_level_variance_emitted"] is False,
        decision["complete_K500_uniform_leakage_emitted"] is False,
        decision["noncyclic_floor_emitted"] is False,
        decision["native_K152_interval_emitted"] is False,
        payload["source_and_ledger_effect"] == "none",
    ]


def main() -> int:
    payload = K578.build()
    controls = checks(payload)
    mutations = [
        lambda p: p["theorem"].__setitem__("no_word_lower_required", False),
        lambda p: p["exact_controls"].__setitem__("row_count", 2),
        lambda p: p["exact_controls"].__setitem__("K501_control_replayed", False),
        lambda p: p["exact_controls"].__setitem__("scalar_shifted_K501_control", "0"),
        lambda p: p["exact_controls"].__setitem__("all_pairwise_identities_pass", False),
        lambda p: p["exact_controls"].__setitem__("all_oscillation_bounds_pass", False),
        lambda p: p["decision"].__setitem__("K510_factorial_path_template_bypassed", False),
        lambda p: p["decision"].__setitem__("direct_normalized_variance_route_released", False),
        lambda p: p["decision"].__setitem__("native_uniform_all_level_variance_emitted", True),
        lambda p: p["decision"].__setitem__("complete_K500_uniform_leakage_emitted", True),
        lambda p: p["decision"].__setitem__("noncyclic_floor_emitted", True),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        hostile = copy.deepcopy(payload)
        mutate(hostile)
        try:
            K578.validate(hostile)
        except AssertionError:
            rejected += 1
    print(f"K578 controls: {sum(controls)}/{len(controls)}; hostile: {rejected}/{len(mutations)}")
    return 0 if all(controls) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
