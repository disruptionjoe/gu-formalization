#!/usr/bin/env python3
"""Independent hostile-mutation probe for K663."""

from __future__ import annotations

from copy import deepcopy
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PRODUCER = HERE / "k663_k500_sharp_cancellation_graph_floor.py"


def load_producer():
    spec = importlib.util.spec_from_file_location("k663_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K663 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def rejected(module, payload, mutate) -> bool:
    candidate = deepcopy(payload)
    mutate(candidate)
    try:
        module.validate(candidate)
    except (AssertionError, KeyError, TypeError, ValueError):
        return True
    return False


def main() -> int:
    module = load_producer()
    payload = module.build()
    module.validate(payload)
    mutations = [
        lambda p: p["sharp_floor_theorem"].__setitem__("sharp_for_declared_scalar_information", False),
        lambda p: p["sharp_floor_theorem"].__setitem__("dimension_free", False),
        lambda p: p["sharp_floor_theorem"].__setitem__("complete_spectator_space_required", False),
        lambda p: p["sharp_floor_theorem"].__setitem__("positive_floor_iff", "A>0 and B>0"),
        lambda p: p["sharp_floor_theorem"].__setitem__("young_optimization_recovers_lambda_minus", False),
        lambda p: p["exact_control"].__setitem__("sharp_conservative_floor", "1/4"),
        lambda p: p["exact_control"].__setitem__("K642_fixed_floor", "5/8"),
        lambda p: p["exact_control"].__setitem__("strict_improvement", False),
        lambda p: p["exact_control"].__setitem__("positive_floor_test_passes", False),
        lambda p: p["exact_control"].__setitem__("rayleigh_equals_floor", False),
        lambda p: p["native_interface_status"].__setitem__("actual_complete_effective_A_identified", True),
        lambda p: p["native_interface_status"].__setitem__("actual_complete_effective_B_identified", True),
        lambda p: p["native_interface_status"].__setitem__("named_complete_sector_floor_emitted", True),
        lambda p: p["composition"].__setitem__("K642_native_constants_created", True),
        lambda p: p["exact_control"].__setitem__("controls_are_synthetic", False),
        lambda p: p["decision"].__setitem__("native_floor_supplied", True),
        lambda p: p.__setitem__("source_and_ledger_effect", "changed"),
        lambda p: p.__setitem__("target_claim", "KILL"),
    ]
    caught = sum(rejected(module, payload, mutate) for mutate in mutations)
    assert caught == len(mutations)
    exact = payload["exact_control"]
    assert exact["A"] == "3/4"
    assert exact["B"] == "21/32"
    assert exact["determinant_margin"] == "125/256"
    print(f"K663 independent probe: 22 controls passed; {caught}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
