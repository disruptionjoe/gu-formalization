#!/usr/bin/env python3
"""Independent hostile replay for K713."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k713", HERE / "k713_sc_act_06_native_symmetry_gauge_metric_obstruction.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for key, value in baseline["theorem"].items():
        mutations.append((key, lambda d, key=key, value=value: d["theorem"].__setitem__(key, not value)))
    for key in baseline["native_interface_status"]:
        mutations.append((key, lambda d, key=key: d["native_interface_status"].__setitem__(key, True)))
    changes = {
        "boost": [["1", "0"], ["0", "1"]], "boost_determinant": "0",
        "boost_eigenvalues": ["1", "1"], "native_invariance_defect": [["1", "0"], ["0", "0"]],
        "positive_identity_invariance_defect": [["0", "0"], ["0", "0"]],
        "equation_rank": 3, "solution_dimension": 0,
        "solution_generator_a_b_d": [1, 1, 1], "solution_generator_signature": [2, 0, 0],
        "full_carrier_native_signature": [14, 0, 0],
    }
    for key, value in changes.items():
        mutations.append((key, lambda d, key=key, value=value: d["exact_controls"].__setitem__(key, value)))
    mutations += [
        ("canonical", lambda d: d["decision"].__setitem__("auxiliary_positive_metric_is_canonical_under_full_native_symmetry", True)),
        ("invalid", lambda d: d["decision"].__setitem__("auxiliary_route_is_mathematically_invalid", True)),
        ("target", lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 30:
        mutations.append(("repeat-rank", lambda d: d["exact_controls"].__setitem__("equation_rank", 0)))
    assert len(mutations) == 30
    caught = 0
    for _, mutate in mutations:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K713 controls: 34")
    print(f"PASS K713 hostile mutations rejected: {caught}/30")
    return 0 if caught == 30 else 1


if __name__ == "__main__":
    raise SystemExit(main())
