#!/usr/bin/env python3
"""Replay K367 and reject mutations of its confluent two-scale envelopes."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k367_order_eight_zero_inclusive_determinant_envelope.py"
PUBLISHED = ROOT / "lab/process/k367-order-eight-zero-inclusive-determinant-envelope.json"

spec = importlib.util.spec_from_file_location("k367_probe_backend", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K367 producer")
backend = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = backend
spec.loader.exec_module(backend)


def rejected(payload: dict) -> bool:
    try:
        backend.validate_payload(payload)
    except AssertionError:
        return True
    return False


def main() -> int:
    rebuilt = backend.build()
    published = json.loads(PUBLISHED.read_text())
    controls = [
        rebuilt == published,
        rebuilt["fixed_control"]["comparable_template_pairs"] == 146,
        rebuilt["fixed_control"]["confluent_templates"] == 38,
        rebuilt["envelope_summary"]["maximum_primitive_order_used"] == 8,
        rebuilt["envelope_summary"]["all_12_K364_obstruction_pairs_represented"],
        rebuilt["closed_strip_contract"]["same_permutation_two_scale_coupling_preserved"],
        rebuilt["closed_strip_contract"]["confluent_factorials_applied_before_absolute_enclosure"],
        not rebuilt["decision"]["global_positive_argument_tail_complete"],
        all(rebuilt["release_test"].values()),
    ]
    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("comparable_template_pairs", 145),
        lambda p: p["fixed_control"].__setitem__("confluent_templates", 37),
        lambda p: p["fixed_control"].__setitem__("derivative_orders", [0, 1]),
        lambda p: p["determinant_envelope_bank"].pop(),
        lambda p: p["determinant_envelope_bank"][0].__setitem__("maximum_primitive_order_used", 9),
        lambda p: p["closed_strip_contract"].__setitem__("same_permutation_two_scale_coupling_preserved", False),
        lambda p: p["closed_strip_contract"].__setitem__("confluent_factorials_applied_before_absolute_enclosure", False),
        lambda p: p["closed_strip_contract"].__setitem__("occurrencewise_scalar_exponent_substituted", True),
        lambda p: p["decision"].__setitem__("global_positive_argument_tail_complete", True),
        lambda p: p["release_test"].__setitem__("complete_order_eight_remainder_not_overclaimed", False),
    ):
        candidate = copy.deepcopy(rebuilt)
        mutate(candidate)
        mutations.append(rejected(candidate))
    if not all(controls) or not all(mutations):
        raise AssertionError("K367 probe failed")
    print(f"K367 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
