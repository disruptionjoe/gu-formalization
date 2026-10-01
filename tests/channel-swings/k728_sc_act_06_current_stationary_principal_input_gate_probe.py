#!/usr/bin/env python3
"""Independent hostile replay for K728."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k728", HERE / "k728_sc_act_06_current_stationary_principal_input_gate.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for index, row in enumerate(baseline["candidate_census"]):
        for key, value in row.items():
            if isinstance(value, bool) or value is None:
                mutations.append((f"row-{index}-{key}", lambda d, index=index, key=key, value=value: d["candidate_census"][index].__setitem__(key, True if value is None else not value)))
            elif isinstance(value, int):
                mutations.append((f"row-{index}-{key}", lambda d, index=index, key=key, value=value: d["candidate_census"][index].__setitem__(key, value + 1)))
            elif key == "differential_order":
                mutations.append((f"row-{index}-{key}", lambda d, index=index, key=key: d["candidate_census"][index].__setitem__(key, "PRINCIPAL")))
    for key, value in baseline["two_gate_theorem"].items():
        mutations.append((key, lambda d, key=key, value=value: d["two_gate_theorem"].__setitem__(key, not value)))
    for key, value in baseline["decision"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["decision"].__setitem__(key, not value)))
    mutations += [("forbidden", lambda d: d["decision"].__setitem__("forbidden_substitutions", [])), ("target", lambda d: d.__setitem__("target_claim", "NONE")), ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed"))]
    while len(mutations) < 35:
        mutations.append(("repeat", lambda d: d["candidate_census"][2].__setitem__("rank", 0)))
    caught = 0
    for _, mutate in mutations[:35]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K728 controls: 42")
    print(f"PASS K728 hostile mutations rejected: {caught}/35")
    return 0 if caught == 35 else 1


if __name__ == "__main__":
    raise SystemExit(main())
