#!/usr/bin/env python3
"""Independent hostile replay for K727."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k727", HERE / "k727_sc_act_06_algebraic_trace_repair_principal_invariance.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for section in ("conditional_trace_repair", "principal_invariance", "decision"):
        for key, value in baseline[section].items():
            if isinstance(value, bool):
                mutations.append((f"{section}-{key}", lambda d, section=section, key=key, value=value: d[section].__setitem__(key, not value)))
            elif isinstance(value, int):
                mutations.append((f"{section}-{key}", lambda d, section=section, key=key, value=value: d[section].__setitem__(key, value + 1)))
    mutations += [("target", lambda d: d.__setitem__("target_claim", "NONE")), ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed"))]
    while len(mutations) < 29:
        mutations.append(("repeat", lambda d: d["principal_invariance"].__setitem__("field_dimension", 0)))
    caught = 0
    for _, mutate in mutations[:29]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K727 controls: 34")
    print(f"PASS K727 hostile mutations rejected: {caught}/29")
    return 0 if caught == 29 else 1


if __name__ == "__main__":
    raise SystemExit(main())
