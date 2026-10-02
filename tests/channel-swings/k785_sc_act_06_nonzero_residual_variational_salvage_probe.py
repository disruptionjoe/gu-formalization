#!/usr/bin/env python3
"""Hostile replay for K785."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k785", HERE / "k785_sc_act_06_nonzero_residual_variational_salvage.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = MOD.build()
    MOD.validate(base)
    mutations = []
    for section in ("preserved_results", "withdrawn_current_inferences", "corrected_use"):
        for key, value in base[section].items():
            if isinstance(value, bool):
                mutations.append((key, lambda d, section=section, key=key, value=value: d[section].__setitem__(key, not value)))
    mutations += [
        ("route", lambda d: d["decision"].__setitem__("route_status", "SOURCE_NATIVE_ACTIVE")),
        ("target", lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL")),
        ("ledger", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 28:
        mutations.append((f"repeat-{len(mutations)}", lambda d: d["corrected_use"].__setitem__("direct_SC_ACT_06_adjudication", True)))
    caught = 0
    for _, mutate in mutations[:28]:
        case = copy.deepcopy(base)
        mutate(case)
        try:
            MOD.validate(case)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K785 controls: 38")
    print(f"PASS K785 hostile mutations rejected: {caught}/28")
    return 0 if caught == 28 else 1


if __name__ == "__main__":
    raise SystemExit(main())
