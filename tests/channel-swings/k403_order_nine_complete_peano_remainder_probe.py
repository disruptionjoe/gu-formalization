#!/usr/bin/env python3
"""Replay K403 and reject omitted, reordered, or double-normalized remainders."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k403_order_nine_complete_peano_remainder.py"
PUBLISHED = ROOT / "lab/process/k403-order-nine-complete-peano-remainder.json"
spec = importlib.util.spec_from_file_location("k403_probe_backend", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K403 producer")
backend = importlib.util.module_from_spec(spec)
spec.loader.exec_module(backend)


def rejected(payload: dict) -> bool:
    try:
        backend.validate_payload(payload)
    except (AssertionError, KeyError, ValueError):
        return True
    return False


def main() -> int:
    published = json.loads(PUBLISHED.read_text())
    controls = [
        backend.build() == published,
        published["fixed_control"]["hybrid_terms"] == 20,
        not published["fixed_control"]["native_prefactor_applied"],
        published["remainder_contract"]["all_twenty_pure_second_terms_present"],
        not published["remainder_contract"]["mixed_derivatives_required"],
        published["decision"]["complete_order_nine_raw_remainder_emitted"],
        not published["decision"]["complete_order_nine_integral_enclosed"],
        all(published["release_test"].values()),
        published["hybrid_remainder_bank"][-1]["exact_cumulative_abs_upper"] == published["remainder_contract"]["exact_raw_complete_remainder_abs_upper"],
    ]
    mutations = []
    for path, value in [
        (("fixed_control", "hybrid_terms"), 19),
        (("fixed_control", "native_prefactor_applied"), True),
        (("decision", "complete_order_nine_raw_remainder_emitted"), False),
        (("decision", "complete_order_nine_integral_enclosed"), True),
        (("release_test", "axis_order_matches_K384"), False),
        (("release_test", "cumulative_sum_exact"), False),
        (("release_test", "native_prefactor_not_double_applied"), False),
        (("release_test", "native_K152_interval_not_emitted"), False),
    ]:
        mutant = copy.deepcopy(published)
        mutant[path[0]][path[1]] = value
        mutations.append(rejected(mutant))
    mutant = copy.deepcopy(published)
    mutant["hybrid_remainder_bank"][0]["exact_hybrid_abs_upper"] = "0"
    mutations.append(rejected(mutant))
    if not all(controls) or not all(mutations):
        raise AssertionError("K403 probe failed")
    print(f"K403 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
