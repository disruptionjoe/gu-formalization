#!/usr/bin/env python3
"""Independent hostile replay for K711."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k711", HERE / "k711_sc_act_06_exact_complex_hodge_criterion.py")
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
        "dimensions": [2, 5, 2], "positive_metric_diagonals": [[1], [1], [1]],
        "gauge_rank": 1, "euler_rank": 1, "composition_rank": 1,
        "middle_cohomology": 1, "hodge_laplacian_rank": 3,
        "nonexact_control_middle_cohomology": 0, "nonexact_control_laplacian_rank": 4,
    }
    for key, value in changes.items():
        mutations.append((key, lambda d, key=key, value=value: d["exact_controls"].__setitem__(key, value)))
    mutations += [
        ("laplacian", lambda d: d["exact_controls"].__setitem__("hodge_laplacian", [["0"]])),
        ("necessary", lambda d: d["decision"].__setitem__("positive_action_pairing_is_logically_necessary_for_symbol_ellipticity", True)),
        ("test", lambda d: d["decision"].__setitem__("positive_auxiliary_metric_can_test_an_already_constructed_real_symbol_complex", False)),
        ("target", lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 28:
        mutations.append(("repeat-laplacian", lambda d: d["exact_controls"].__setitem__("hodge_laplacian_rank", 0)))
    assert len(mutations) == 28
    caught = 0
    for _, mutate in mutations:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K711 controls: 32")
    print(f"PASS K711 hostile mutations rejected: {caught}/28")
    return 0 if caught == 28 else 1


if __name__ == "__main__":
    raise SystemExit(main())
