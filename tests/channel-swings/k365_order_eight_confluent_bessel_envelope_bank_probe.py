#!/usr/bin/env python3
"""Replay K365 and reject mutations of its order-eight primitive bank."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k365_order_eight_confluent_bessel_envelope_bank.py"
PUBLISHED = ROOT / "lab/process/k365-order-eight-confluent-bessel-envelope-bank.json"


spec = importlib.util.spec_from_file_location("k365_probe_backend", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K365 producer")
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
        rebuilt["fixed_control"]["exact_rational_bounds"] == 36,
        rebuilt["fixed_control"]["positive_Arb_controls"] == 72,
        rebuilt["scaled_bessel_bank"]["continuous_zero_limits"] == [str(2 * math.factorial(i)) for i in range(9)],
        all(row["contained"] for row in rebuilt["positive_controls"]),
        rebuilt["demand_reconciliation"]["K349_orders_zero_through_two_replayed_exactly"],
        not rebuilt["decision"]["uniform_integrand_weighted_boundary_majorant_complete"],
        all(rebuilt["release_test"].values()),
    ]
    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("maximum_derivative_order", 7),
        lambda p: p["fixed_control"].__setitem__("exact_rational_bounds", 35),
        lambda p: p["fixed_control"].__setitem__("positive_Arb_controls", 70),
        lambda p: p["scaled_bessel_bank"]["continuous_zero_limits"].__setitem__(8, "40320"),
        lambda p: p["scaled_bessel_bank"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["positive_controls"][0].__setitem__("contained", False),
        lambda p: p["demand_reconciliation"].__setitem__("maximum_total_order", 7),
        lambda p: p["demand_reconciliation"].__setitem__("K349_orders_zero_through_two_replayed_exactly", False),
        lambda p: p["decision"].__setitem__("uniform_integrand_weighted_boundary_majorant_complete", True),
        lambda p: p["release_test"].__setitem__("analytic_tail_not_overclaimed", False),
    ):
        candidate = copy.deepcopy(rebuilt)
        mutate(candidate)
        mutations.append(rejected(candidate))
    if not all(controls) or not all(mutations):
        raise AssertionError("K365 probe failed")
    print(f"K365 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
