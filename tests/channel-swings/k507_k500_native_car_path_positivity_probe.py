#!/usr/bin/env python3
"""Probe and hostile self-test for K507."""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("k507_probe_target", HERE / "k507_k500_native_car_path_positivity.py")
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K507")
K507 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(K507)


def checks(payload):
    c = payload["exact_controls"]
    d = payload["decision"]
    t = payload["all_order_theorem"]
    return [
        payload["result_id"] == "K507-K500-NATIVE-CAR-PATH-POSITIVITY",
        len(c["seed_order_rows"]) == 39,
        c["all_39_seed_order_blocks_match_closed_counts"] is True,
        c["all_resolved_signature_blocks_have_one_CAR_sign"] is True,
        c["cauchy_moment_control"]["same_order_determinant_positive"] is True,
        c["cauchy_moment_control"]["one_order_reversed_rejected"] is True,
        "det[kappa(s_i+r_j)]" in t["andreief_identity"]
        and "dnu(E_k)" in t["andreief_identity"],
        "nonnegative" in t["native_cross_terms"],
        d["K505_generic_cancellation_control_retracted"] is False,
        d["K505_generic_obstruction_applies_to_exact_K177_equal_coupling_paths"] is False,
        d["native_path_cross_terms_nonnegative"] is True,
        d["one_native_path_norm_is_a_valid_word_norm_lower_bound"] is True,
        d["uniform_all_level_path_norm_rate_serialized"] is False,
        d["complete_K500_uniform_leakage_emitted"] is False,
        payload["source_and_ledger_effect"] == "none",
    ]


def selftest(payload):
    mutations = [
        lambda p: p["exact_controls"].__setitem__("all_39_seed_order_blocks_match_closed_counts", False),
        lambda p: p["exact_controls"].__setitem__("all_resolved_signature_blocks_have_one_CAR_sign", False),
        lambda p: p["exact_controls"]["cauchy_moment_control"].__setitem__("same_order_determinant_positive", False),
        lambda p: p["decision"].__setitem__("K505_generic_cancellation_control_retracted", True),
        lambda p: p["decision"].__setitem__("native_path_cross_terms_nonnegative", False),
        lambda p: p["decision"].__setitem__("one_native_path_norm_is_a_valid_word_norm_lower_bound", False),
        lambda p: p["decision"].__setitem__("uniform_all_level_path_norm_rate_serialized", True),
        lambda p: p["decision"].__setitem__("complete_K500_uniform_leakage_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        hostile = copy.deepcopy(payload)
        mutate(hostile)
        try:
            K507.validate_payload(hostile)
        except AssertionError:
            rejected += 1
    return rejected, len(mutations)


def main() -> int:
    payload = K507.build()
    controls = checks(payload)
    rejected, total = selftest(payload)
    print(f"K507 controls: {sum(controls)}/{len(controls)}; hostile: {rejected}/{total}")
    return 0 if all(controls) and rejected == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
