#!/usr/bin/env python3
"""Replay K549 and reject mutations of its confluent two-scale envelopes."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k549_order_ten_zero_inclusive_determinant_envelope.py"
PUBLISHED = ROOT / "lab/process/k549-order-ten-zero-inclusive-determinant-envelope.json"

spec = importlib.util.spec_from_file_location("k549_probe_backend", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K549 producer")
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
        rebuilt["fixed_control"]["comparable_template_pairs"] == 371,
        rebuilt["fixed_control"]["confluent_templates"] == 75,
        rebuilt["fixed_control"]["rank_compatible_pair_confluent_envelopes"] == 10958,
        rebuilt["envelope_summary"]["maximum_primitive_order_used"] == 10,
        rebuilt["envelope_summary"]["all_42_K546_obstruction_pairs_represented"],
        rebuilt["global_face_envelope_contract"]["same_permutation_two_scale_coupling_preserved"],
        rebuilt["global_face_envelope_contract"]["confluent_factorials_applied_before_absolute_enclosure"],
        rebuilt["decision"]["global_positive_argument_tail_complete"],
        all(rebuilt["release_test"].values()),
    ]
    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("comparable_template_pairs", 370),
        lambda p: p["fixed_control"].__setitem__("confluent_templates", 74),
        lambda p: p["fixed_control"].__setitem__("derivative_orders", [0, 1]),
        lambda p: p["determinant_envelope_bank"].pop(),
        lambda p: p["determinant_envelope_bank"][0].__setitem__("maximum_primitive_order_used", 11),
        lambda p: p["global_face_envelope_contract"].__setitem__("same_permutation_two_scale_coupling_preserved", False),
        lambda p: p["global_face_envelope_contract"].__setitem__("confluent_factorials_applied_before_absolute_enclosure", False),
        lambda p: p["global_face_envelope_contract"].__setitem__("occurrencewise_scalar_exponent_substituted", True),
        lambda p: p["decision"].__setitem__("global_positive_argument_tail_complete", False),
        lambda p: p["release_test"].__setitem__("complete_order_ten_remainder_not_overclaimed", False),
    ):
        candidate = copy.deepcopy(rebuilt)
        mutate(candidate)
        mutations.append(rejected(candidate))
    if not all(controls) or not all(mutations):
        raise AssertionError("K549 probe failed")
    print(f"K549 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
