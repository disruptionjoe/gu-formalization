#!/usr/bin/env python3
"""Independent hostile-mutation probe for K662."""

from __future__ import annotations

from copy import deepcopy
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PRODUCER = HERE / "k662_k500_reference_preserving_boundary_coordinate_group.py"


def load_producer():
    spec = importlib.util.spec_from_file_location("k662_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K662 producer")
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
        lambda p: p["coordinate_group_theorem"].__setitem__("reference_extension_unchanged", False),
        lambda p: p["coordinate_group_theorem"].__setitem__("complete_denominator_nonnegativity_equivalent", False),
        lambda p: p["coordinate_group_theorem"].__setitem__("friedrichs_status_created", True),
        lambda p: p["coordinate_group_theorem"].__setitem__("numerical_floor_invariant_for_general_U", True),
        lambda p: p["coordinate_group_theorem"].__setitem__("K661_symplectic_swap_covered", True),
        lambda p: p["exact_controls"].__setitem__("congruence_identity", False),
        lambda p: p["exact_controls"].__setitem__("floor_bound_holds", False),
        lambda p: p["exact_controls"].__setitem__("approximant_congruence_identity", False),
        lambda p: p["exact_controls"].__setitem__("error_bound_holds", False),
        lambda p: p["exact_controls"].__setitem__("approximant_floor_bound_holds", False),
        lambda p: p["exact_controls"].__setitem__("conservative_margin_nonnegative", False),
        lambda p: p["exact_controls"].__setitem__("unitary_swap_floor_invariant", False),
        lambda p: p["exact_controls"].__setitem__("unitary_swap_error_norm_invariant", False),
        lambda p: p["native_interface_status"].__setitem__("actual_native_coordinate_group_law_proved", True),
    ]
    caught = sum(rejected(module, payload, mutate) for mutate in mutations)
    assert caught == len(mutations)
    exact = payload["exact_controls"]
    assert exact["original_denominator_floor"] == "1"
    assert exact["transformed_denominator_floor"] == "3/8"
    assert exact["operator_norm_error"] == "1/20"
    assert exact["transformed_operator_norm_error"] == "2/25"
    print(f"K662 independent probe: 18 controls passed; {caught}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
