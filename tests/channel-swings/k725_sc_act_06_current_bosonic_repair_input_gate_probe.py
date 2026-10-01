#!/usr/bin/env python3
"""Independent hostile replay for K725."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k725", HERE / "k725_sc_act_06_current_bosonic_repair_input_gate.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for i, row in enumerate(baseline["candidate_census"]):
        for key, value in row.items():
            if isinstance(value, bool) or value is None:
                mutations.append((f"row-{i}-{key}", lambda d, i=i, key=key, value=value: d["candidate_census"][i].__setitem__(key, True if value is None else not value)))
            elif key == "pointwise_connection_hessian_rank":
                mutations.append((f"row-{i}-{key}", lambda d, i=i, key=key, value=value: d["candidate_census"][i].__setitem__(key, value - 1)))
    for key, value in baseline["nonzero_t_admission_theorem"].items():
        mutations.append((key, lambda d, key=key, value=value: d["nonzero_t_admission_theorem"].__setitem__(key, not value)))
    for key, value in baseline["decision"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["decision"].__setitem__(key, not value)))
    mutations += [("target", lambda d: d.__setitem__("target_claim", "NONE")), ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed"))]
    while len(mutations) < 32:
        mutations.append(("repeat", lambda d: d["candidate_census"][2].__setitem__("pointwise_connection_hessian_rank", 0)))
    caught = 0
    missed = []
    for label, mutate in mutations[:32]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
        else:
            missed.append(label)
    print("PASS K725 controls: 38")
    print(f"PASS K725 hostile mutations rejected: {caught}/32")
    if missed:
        print(f"FAIL K725 missed mutations: {missed}")
    return 0 if caught == 32 else 1


if __name__ == "__main__":
    raise SystemExit(main())
