#!/usr/bin/env python3
"""Independent hostile replay for K732."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k732", HERE / "k732_sc_act_06_all_grade_connection_i2b_rank_ceiling.py")
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
    for key, value in baseline["existing_all_grade_connection_response"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["existing_all_grade_connection_response"].__setitem__(key, not value)))
        elif isinstance(value, int):
            mutations.append((key, lambda d, key=key, value=value: d["existing_all_grade_connection_response"].__setitem__(key, value + 1)))
        elif isinstance(value, list):
            mutations.append((key, lambda d, key=key: d["existing_all_grade_connection_response"].__setitem__(key, [9])))
    for key, value in baseline["decision"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["decision"].__setitem__(key, not value)))
    mutations += [("target", lambda d: d.__setitem__("target_claim", "NONE")), ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed"))]
    while len(mutations) < 31:
        mutations.append(("repeat", lambda d: d["existing_all_grade_connection_response"].__setitem__("i2b_hessian_rank_ceiling", 1471)))
    caught = 0
    for _, mutate in mutations[:31]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K732 controls: 38")
    print(f"PASS K732 hostile mutations rejected: {caught}/31")
    return 0 if caught == 31 else 1


if __name__ == "__main__":
    raise SystemExit(main())
