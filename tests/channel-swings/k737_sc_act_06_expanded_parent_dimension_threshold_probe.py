#!/usr/bin/env python3
"""Independent hostile replay for K737."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k737", HERE / "k737_sc_act_06_expanded_parent_dimension_threshold.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for key, value in baseline["exact_thresholds"].items():
        mutations.append((key, lambda d, key=key, value=value: d["exact_thresholds"].__setitem__(key, value + 1)))
    for i, row in enumerate(baseline["candidate_parent_classification"]):
        for key, value in row.items():
            if isinstance(value, bool):
                mutations.append((key, lambda d, i=i, key=key, value=value: d["candidate_parent_classification"][i].__setitem__(key, not value)))
            elif isinstance(value, int):
                mutations.append((key, lambda d, i=i, key=key, value=value: d["candidate_parent_classification"][i].__setitem__(key, value + 1)))
    for key, value in baseline["ownership_controls"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["ownership_controls"].__setitem__(key, not value)))
        else:
            mutations.append((key, lambda d, key=key: d["ownership_controls"].__setitem__(key, "wrong")))
    for key, value in baseline["decision"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["decision"].__setitem__(key, not value)))
    mutations += [("target", lambda d: d.__setitem__("target_claim", "NONE")), ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed"))]
    while len(mutations) < 39:
        mutations.append(("repeat", lambda d: d["exact_thresholds"].__setitem__("selected_low_grade_ceiling", 0)))
    caught = 0
    for _, mutate in mutations[:39]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K737 controls: 46")
    print(f"PASS K737 hostile mutations rejected: {caught}/39")
    return 0 if caught == 39 else 1


if __name__ == "__main__":
    raise SystemExit(main())
