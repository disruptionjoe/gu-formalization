#!/usr/bin/env python3
"""Replay K375 and reject primitive-bank mutations."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k375_rank_five_global_scaled_bessel_bank.py"
PUBLISHED = ROOT / "lab/process/k375-rank-five-global-scaled-bessel-bank.json"
spec = importlib.util.spec_from_file_location("k375_probe_backend", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K375 producer")
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
        rebuilt["fixed_control"]["maximum_derivative_order"] == 10,
        rebuilt["fixed_control"]["half_integer_comparator"] == "K_(23/2)",
        rebuilt["scaled_bessel_contract"]["continuous_zero_limits"] == [str(2 * math.factorial(i)) for i in range(11)],
        rebuilt["scaled_bessel_contract"]["K365_orders_zero_through_eight_replayed"],
        [row["order"] for row in rebuilt["global_scaled_bessel_bank"]["rows"]] == list(range(11)),
        all(row["contained"] for row in rebuilt["positive_controls"]),
        not rebuilt["decision"]["order_nine_factor_transfer_complete"],
        all(rebuilt["release_test"].values()),
    ]
    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("maximum_derivative_order", 9),
        lambda p: p["fixed_control"].__setitem__("exact_compact_rational_bounds", 43),
        lambda p: p["fixed_control"].__setitem__("half_integer_comparator", "K_(21/2)"),
        lambda p: p["scaled_bessel_contract"]["continuous_zero_limits"].__setitem__(10, "1"),
        lambda p: p["scaled_bessel_contract"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["scaled_bessel_contract"].__setitem__("K365_orders_zero_through_eight_replayed", False),
        lambda p: p["global_scaled_bessel_bank"]["rows"].pop(),
        lambda p: p["global_scaled_bessel_bank"]["rows"][10].__setitem__("global_scaled_upper", "0"),
        lambda p: p["positive_controls"][0].__setitem__("contained", False),
        lambda p: p["decision"].__setitem__("order_nine_factor_transfer_complete", True),
        lambda p: p["decision"].__setitem__("numerical_order_nine_integral_emitted", True),
    ):
        candidate = copy.deepcopy(rebuilt)
        mutate(candidate)
        mutations.append(rejected(candidate))
    if not all(controls) or not all(mutations):
        raise AssertionError("K375 probe failed")
    print(f"K375 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
