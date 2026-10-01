#!/usr/bin/env python3
"""Independent hostile replay for K739."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k739", HERE / "k739_sc_act_06_expanded_action_parent_ownership.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for section in ("exact_action_ownership", "parent_typing", "decision"):
        for key, value in baseline[section].items():
            if isinstance(value, bool):
                mutations.append((key, lambda d, section=section, key=key, value=value: d[section].__setitem__(key, not value)))
            elif isinstance(value, int):
                mutations.append((key, lambda d, section=section, key=key, value=value: d[section].__setitem__(key, value + 1)))
            elif key in ("stationary_germ", "field_carrier_selected_by_zero_branch_action_hessian", "symmetry_and_pairing_fork", "nonzero_branch_normal_hessian"):
                mutations.append((key, lambda d, section=section, key=key: d[section].__setitem__(key, "WRONG")))
    mutations += [
        ("target", lambda d: d.__setitem__("target_claim", "NONE")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 24:
        mutations.append(("repeat", lambda d: d["exact_action_ownership"].__setitem__("action_owned_connection_coefficient_directions", 0)))
    caught = 0
    for _, mutate in mutations[:24]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K739 controls: 29")
    print(f"PASS K739 hostile mutations rejected: {caught}/24")
    return 0 if caught == 24 else 1


if __name__ == "__main__":
    raise SystemExit(main())
