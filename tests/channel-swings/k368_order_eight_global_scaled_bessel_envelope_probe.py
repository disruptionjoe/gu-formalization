#!/usr/bin/env python3
"""Replay K368 and reject mutations of its compact-plus-tail join."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k368_order_eight_global_scaled_bessel_envelope.py"
PUBLISHED = ROOT / "lab/process/k368-order-eight-global-scaled-bessel-envelope.json"

spec = importlib.util.spec_from_file_location("k368_probe_backend", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K368 producer")
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
        rebuilt["fixed_control"]["maximum_derivative_order"] == 8,
        rebuilt["fixed_control"]["half_integer_comparator"] == "K_(19/2)",
        rebuilt["fixed_control"]["positive_Arb_controls"] == 27,
        [row["order"] for row in rebuilt["global_scaled_bessel_bank"]["rows"]] == list(range(9)),
        all(row["contained"] for row in rebuilt["positive_controls"]),
        rebuilt["tail_contract"]["all_global_bounds_exact_rational"],
        not rebuilt["decision"]["determinant_level_whole_radial_face_majorants_complete"],
        all(rebuilt["release_test"].values()),
    ]
    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("maximum_derivative_order", 7),
        lambda p: p["fixed_control"].__setitem__("half_integer_comparator", "K_(17/2)"),
        lambda p: p["fixed_control"].__setitem__("positive_Arb_controls", 26),
        lambda p: p["global_scaled_bessel_bank"]["rows"].pop(),
        lambda p: p["global_scaled_bessel_bank"]["rows"][0].__setitem__("global_scaled_upper", "0"),
        lambda p: p["tail_contract"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["tail_contract"].__setitem__("all_global_bounds_exact_rational", False),
        lambda p: p["positive_controls"][0].__setitem__("contained", False),
        lambda p: p["decision"].__setitem__("determinant_level_whole_radial_face_majorants_complete", True),
        lambda p: p["release_test"].__setitem__("complete_order_eight_remainder_not_overclaimed", False),
    ):
        candidate = copy.deepcopy(rebuilt)
        mutate(candidate)
        mutations.append(rejected(candidate))
    if not all(controls) or not all(mutations):
        raise AssertionError("K368 probe failed")
    print(f"K368 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
