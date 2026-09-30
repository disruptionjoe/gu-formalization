#!/usr/bin/env python3
"""Independent hostile-mutation probe for K661."""

from __future__ import annotations

from copy import deepcopy
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PRODUCER = HERE / "k661_k500_friedrichs_reference_nonidentifiability.py"


def load_producer():
    spec = importlib.util.spec_from_file_location("k661_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K661 producer")
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
        lambda p: p["interval_control"].__setitem__("green_identity_exact_on_polynomial_controls", False),
        lambda p: p["interval_control"].__setitem__("swapped_green_identity_valid", False),
        lambda p: p["interval_control"].__setitem__("dirichlet_is_friedrichs", False),
        lambda p: p["interval_control"].__setitem__("swapped_reference_is_friedrichs", True),
        lambda p: p["exact_controls"].__setitem__("constant_is_neumann_not_dirichlet", False),
        lambda p: p["exact_controls"].__setitem__("dirichlet_witness_is_dirichlet_not_neumann", False),
        lambda p: p["exact_controls"].__setitem__("both_constant_families_norm_resolvent_converge", False),
        lambda p: p["custody_theorem"].__setitem__("norm_resolvent_convergence_alone_selects_friedrichs", True),
        lambda p: p["custody_theorem"].__setitem__("fixed_native_reference_is_not_friedrichs", True),
    ]
    caught = sum(rejected(module, payload, mutate) for mutate in mutations)
    assert caught == len(mutations)
    rows = payload["exact_controls"]["green_rows"]
    assert len(rows) == 3
    assert all(row["both_green_identities_hold"] for row in rows)
    print(f"K661 independent probe: 12 controls passed; {caught}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
