#!/usr/bin/env python3
"""Replay K547 and reject native derivative-bank mutations."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = HERE / "k547_order_ten_zero_safe_scaled_derivative_bank.py"
PUBLISHED = ROOT / "lab/process/k547-order-ten-zero-safe-scaled-derivative-bank.json"
spec = importlib.util.spec_from_file_location("k547_probe_backend", PRODUCER)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load K547 producer")
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
    native = rebuilt["native_order_ten_reconciliation"]
    controls = [
        rebuilt == published,
        rebuilt["fixed_control"]["maximum_derivative_order"] == 10,
        len(rebuilt["positive_controls"]) == 121,
        native["K410_orders_zero_through_two_replayed_exactly"],
        native["K375_global_bank_recomputed_exactly"],
        not native["order_eight_or_order_nine_face_atlas_reused"],
        all(row["contained"] for row in rebuilt["positive_controls"]),
        not rebuilt["decision"]["uniform_integrand_weighted_boundary_majorant_complete"],
        all(rebuilt["release_test"].values()),
    ]
    mutations = []
    for mutate in (
        lambda p: p["fixed_control"].__setitem__("maximum_derivative_order", 9),
        lambda p: p["fixed_control"].__setitem__("exact_compact_rational_bounds", 43),
        lambda p: p["native_order_ten_reconciliation"].__setitem__("maximum_row_divided_difference_order", 3),
        lambda p: p["native_order_ten_reconciliation"].__setitem__("K410_orders_zero_through_two_replayed_exactly", False),
        lambda p: p["native_order_ten_reconciliation"].__setitem__("K375_global_bank_recomputed_exactly", False),
        lambda p: p["native_order_ten_reconciliation"].__setitem__("order_eight_or_order_nine_face_atlas_reused", True),
        lambda p: p["scaled_bessel_contract"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["positive_controls"][0].__setitem__("contained", False),
        lambda p: p["decision"].__setitem__("uniform_integrand_weighted_boundary_majorant_complete", True),
        lambda p: p["release_test"].__setitem__("native_K152_interval_not_emitted", False),
    ):
        candidate = copy.deepcopy(rebuilt)
        mutate(candidate)
        mutations.append(rejected(candidate))
    if not all(controls) or not all(mutations):
        raise AssertionError("K547 probe failed")
    print(f"K547 probe: {sum(controls)}/{len(controls)} controls passed; {sum(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
