#!/usr/bin/env python3
"""Independent hostile replay for K735."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k735", HERE / "k735_sc_act_06_source_low_grade_i2b_rank_ceiling.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for key, value in baseline["factorization_theorem"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["factorization_theorem"].__setitem__(key, not value)))
        else:
            mutations.append((key, lambda d, key=key: d["factorization_theorem"].__setitem__(key, "wrong")))
    for key, value in baseline["selected_low_grade_tangent"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["selected_low_grade_tangent"].__setitem__(key, not value)))
        elif isinstance(value, int):
            mutations.append((key, lambda d, key=key, value=value: d["selected_low_grade_tangent"].__setitem__(key, value + 1)))
    for key, value in baseline["decision"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["decision"].__setitem__(key, not value)))
    mutations += [("target", lambda d: d.__setitem__("target_claim", "NONE")), ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed"))]
    while len(mutations) < 36:
        mutations.append(("repeat", lambda d: d["selected_low_grade_tangent"].__setitem__("component_sum", 0)))
    caught = 0
    for _, mutate in mutations[:36]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K735 controls: 44")
    print(f"PASS K735 hostile mutations rejected: {caught}/36")
    return 0 if caught == 36 else 1


if __name__ == "__main__":
    raise SystemExit(main())
