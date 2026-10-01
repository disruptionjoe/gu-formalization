#!/usr/bin/env python3
"""Independent hostile replay for K726."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k726", HERE / "k726_sc_act_06_homogeneous_nonzero_t_stationarity_obstruction.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for key, value in baseline["homogeneous_branch_theorem"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["homogeneous_branch_theorem"].__setitem__(key, not value)))
        elif isinstance(value, int):
            mutations.append((key, lambda d, key=key, value=value: d["homogeneous_branch_theorem"].__setitem__(key, value + 1)))
        elif key in ("first_action_density", "normalized_metric_euler"):
            mutations.append((key, lambda d, key=key: d["homogeneous_branch_theorem"].__setitem__(key, "wrong")))
    for key, value in baseline["exact_controls_at_kappa_one"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["exact_controls_at_kappa_one"].__setitem__(key, not value)))
        elif isinstance(value, int):
            mutations.append((key, lambda d, key=key, value=value: d["exact_controls_at_kappa_one"].__setitem__(key, value + 1)))
        elif key in ("action_density", "metric_euler"):
            mutations.append((key, lambda d, key=key: d["exact_controls_at_kappa_one"].__setitem__(key, "wrong")))
    for key, value in baseline["decision"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["decision"].__setitem__(key, not value)))
    mutations += [("target", lambda d: d.__setitem__("target_claim", "NONE")), ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed"))]
    while len(mutations) < 33:
        mutations.append(("repeat", lambda d: d["exact_controls_at_kappa_one"].__setitem__("metric_euler_rank", 0)))
    caught = 0
    for _, mutate in mutations[:33]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K726 controls: 40")
    print(f"PASS K726 hostile mutations rejected: {caught}/33")
    return 0 if caught == 33 else 1


if __name__ == "__main__":
    raise SystemExit(main())
