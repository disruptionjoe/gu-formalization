#!/usr/bin/env python3
"""Replay K378 and reject rank-six primitive mutations."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k378_rank_six_global_scaled_bessel_bank.py"
PUBLISHED = ROOT / "lab/process/k378-rank-six-global-scaled-bessel-bank.json"
spec = importlib.util.spec_from_file_location("k378_probe_backend", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K378 producer")
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
        rebuilt["fixed_control"]["maximum_derivative_order"] == 12,
        rebuilt["fixed_control"]["half_integer_comparator"] == "K_(27/2)",
        rebuilt["scaled_bessel_contract"]["continuous_zero_limits"] == [str(2 * math.factorial(i)) for i in range(13)],
        rebuilt["tail_contract"]["K375_orders_zero_through_ten_global_dominated"],
        [row["order"] for row in rebuilt["global_scaled_bessel_bank"]["rows"]] == list(range(13)),
        all(row["contained"] for row in rebuilt["positive_controls"]),
        not rebuilt["decision"]["orders_eleven_twelve_factor_transfer_complete"],
        all(rebuilt["release_test"].values()),
    ]
    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("maximum_derivative_order", 11),
        lambda p: p["fixed_control"].__setitem__("exact_compact_rational_bounds", 51),
        lambda p: p["fixed_control"].__setitem__("half_integer_comparator", "K_(25/2)"),
        lambda p: p["scaled_bessel_contract"]["continuous_zero_limits"].__setitem__(12, "1"),
        lambda p: p["scaled_bessel_contract"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["tail_contract"].__setitem__("K375_orders_zero_through_ten_global_dominated", False),
        lambda p: p["global_scaled_bessel_bank"]["rows"].pop(),
        lambda p: p["global_scaled_bessel_bank"]["rows"][12].__setitem__("global_scaled_upper", "0"),
        lambda p: p["positive_controls"][0].__setitem__("contained", False),
        lambda p: p["decision"].__setitem__("orders_eleven_twelve_factor_transfer_complete", True),
        lambda p: p["decision"].__setitem__("numerical_orders_eleven_twelve_integrals_emitted", True),
    ):
        candidate = copy.deepcopy(rebuilt)
        mutate(candidate)
        mutations.append(rejected(candidate))
    if not all(controls) or not all(mutations):
        raise AssertionError("K378 probe failed")
    print(f"K378 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
