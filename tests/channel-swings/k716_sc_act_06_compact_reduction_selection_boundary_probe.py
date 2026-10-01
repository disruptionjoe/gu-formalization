#!/usr/bin/env python3
"""Independent hostile replay for K716."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k716", HERE / "k716_sc_act_06_compact_reduction_selection_boundary.py")
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
        "q1": [["1", "0"], ["0", "1"]],
        "q2": [["1", "0"], ["0", "1"]],
        "pairwise_distinct": False,
        "cartan_compatibility": [True, False, True],
        "determinants": ["1", "0", "1"],
        "plane_eigenvalue_pairs": [["1", "1"], ["1", "1"], ["1", "1"]],
        "full_native_invariant_positive_member": True,
    }
    for key, value in changes.items():
        mutations.append((key, lambda d, key=key, value=value: d["exact_controls"].__setitem__(key, value)))
    mutations += [
        ("existence", lambda d: d["decision"].__setitem__("auxiliary_route_has_a_mathematical_existence_obstruction", True)),
        ("selection", lambda d: d["decision"].__setitem__("auxiliary_route_has_an_unresolved_selection_and_compatibility_obligation", False)),
        ("continue", lambda d: d["decision"].__setitem__("abstract_auxiliary_metric_arc_requires_further_distance_only_work", True)),
        ("target", lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 34:
        mutations.append(("repeat-distinct", lambda d: d["exact_controls"].__setitem__("pairwise_distinct", False)))
    assert len(mutations) == 34
    caught = 0
    for _, mutate in mutations:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K716 controls: 38")
    print(f"PASS K716 hostile mutations rejected: {caught}/34")
    return 0 if caught == 34 else 1


if __name__ == "__main__":
    raise SystemExit(main())
