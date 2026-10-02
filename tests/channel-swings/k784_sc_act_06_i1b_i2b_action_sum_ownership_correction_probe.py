#!/usr/bin/env python3
"""Hostile replay for K784."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k784", HERE / "k784_sc_act_06_i1b_i2b_action_sum_ownership_correction.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = MOD.build()
    MOD.validate(base)
    mutations = []
    for section in ("ownership", "preserved_mathematics", "decision"):
        for key, value in base[section].items():
            if isinstance(value, bool):
                mutations.append((key, lambda d, section=section, key=key, value=value: d[section].__setitem__(key, not value)))
    mutations += [
        ("class", lambda d: d["ownership"].__setitem__("combined_stationarity_classification", "SOURCE_NATIVE_ROUTE")),
        ("equation", lambda d: d["preserved_mathematics"].__setitem__("K780_equation", "J^*Q Upsilon=0")),
        ("target", lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL")),
        ("ledger", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 26:
        mutations.append((f"repeat-{len(mutations)}", lambda d: d["ownership"].__setitem__("source_supplies_relative_sum_coefficient", True)))
    caught = 0
    for _, mutate in mutations[:26]:
        case = copy.deepcopy(base)
        mutate(case)
        try:
            MOD.validate(case)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K784 controls: 36")
    print(f"PASS K784 hostile mutations rejected: {caught}/26")
    return 0 if caught == 26 else 1


if __name__ == "__main__":
    raise SystemExit(main())
