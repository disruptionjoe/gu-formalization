#!/usr/bin/env python3
"""Replay K372 and reject missing terms, double normalization, and overclaims."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k372_order_eight_complete_integral_enclosure.py"
PUBLISHED = ROOT / "lab/process/k372-order-eight-complete-integral-enclosure.json"
spec = importlib.util.spec_from_file_location("k372_probe_backend", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K372 producer")
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
        published["fixed_control"]["ordered_descriptors"] == 2400,
        published["fixed_control"]["coherent_groups"] == 23,
        published["fixed_control"]["hybrid_remainder_terms"] == 18,
        published["fixed_control"]["native_prefactor_application_count"] == 1,
        published["complete_integral_enclosure"]["node_interval_contained"],
        published["composition_contract"]["complete_order_eight_integral_enclosed"],
        published["decision"]["rank_five_order_nine_calculus_released"],
        not published["decision"]["native_K152_interval_emitted"],
        all(published["release_test"].values()),
    ]
    mutations = []
    for path, value in [
        (("fixed_control", "ordered_descriptors"), 2399),
        (("fixed_control", "coherent_groups"), 22),
        (("fixed_control", "hybrid_remainder_terms"), 17),
        (("fixed_control", "native_prefactor_application_count"), 2),
        (("composition_contract", "native_prefactor_applied_exactly_once"), False),
        (("composition_contract", "K345_product_weight_reapplied"), True),
        (("composition_contract", "K341_normalization_reused"), True),
        (("decision", "rank_five_order_nine_calculus_released"), False),
        (("decision", "action_column_emitted"), True),
        (("decision", "native_K152_interval_emitted"), True),
    ]:
        mutant = copy.deepcopy(published)
        mutant[path[0]][path[1]] = value
        mutations.append(rejected(mutant))
    mutant = copy.deepcopy(published)
    mutant["complete_integral_enclosure"]["complete_order_eight_integral_interval_exact"] = ["1", "-1"]
    mutations.append(rejected(mutant))
    if not all(controls) or not all(mutations):
        raise AssertionError("K372 probe failed")
    print(f"K372 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
