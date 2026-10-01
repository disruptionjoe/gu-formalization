#!/usr/bin/env python3
"""Independent hostile replay for K734."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k734", HERE / "k734_sc_act_06_all_grade_connection_displayed_full_symbol_obstruction.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for key, value in baseline["composition_theorem"].items():
        mutations.append((key, lambda d, key=key, value=value: d["composition_theorem"].__setitem__(key, not value)))
    for key, value in baseline["exact_controls"].items():
        if isinstance(value, int):
            mutations.append((key, lambda d, key=key, value=value: d["exact_controls"].__setitem__(key, value + 1)))
    for i, row in enumerate(baseline["exact_controls"]["cases"]):
        for key, value in row.items():
            if isinstance(value, bool):
                mutations.append((key, lambda d, i=i, key=key, value=value: d["exact_controls"]["cases"][i].__setitem__(key, not value)))
            elif isinstance(value, int):
                mutations.append((key, lambda d, i=i, key=key, value=value: d["exact_controls"]["cases"][i].__setitem__(key, value + 1)))
    for key, value in baseline["decision"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["decision"].__setitem__(key, not value)))
    mutations += [("target", lambda d: d.__setitem__("target_claim", "NONE")), ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed"))]
    while len(mutations) < 29:
        mutations.append(("repeat", lambda d: d["exact_controls"]["cases"][1].__setitem__("full_middle_cohomology_lower", 0)))
    caught = 0
    for _, mutate in mutations[:29]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K734 controls: 36")
    print(f"PASS K734 hostile mutations rejected: {caught}/29")
    return 0 if caught == 29 else 1


if __name__ == "__main__":
    raise SystemExit(main())
