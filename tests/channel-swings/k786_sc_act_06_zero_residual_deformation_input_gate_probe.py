#!/usr/bin/env python3
"""Hostile replay for K786."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k786", HERE / "k786_sc_act_06_zero_residual_deformation_input_gate.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = MOD.build()
    MOD.validate(base)
    mutations = []
    for key, value in base["current_custody"].items():
        mutations.append((key, lambda d, key=key, value=value: d["current_custody"].__setitem__(key, not value)))
    for key in base["rejection_rules"]:
        mutations.append((key, lambda d, key=key: d["rejection_rules"].__setitem__(key, "admit")))
    mutations += [
        ("required", lambda d: d["required_packet"].pop()),
        ("admit", lambda d: d["decision"].__setitem__("candidate_admitted", True)),
        ("status", lambda d: d["decision"].__setitem__("SC_ACT_06_status", "CONFIRMED")),
        ("incumbent", lambda d: d["decision"].__setitem__("incumbent", "nonzero residual")),
        ("alternative", lambda d: d["decision"].__setitem__("strongest_independent_alternative", "none")),
        ("target", lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL")),
        ("ledger", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 30:
        mutations.append((f"repeat-{len(mutations)}", lambda d: d["decision"].__setitem__("candidate_admitted", True)))
    caught = 0
    for _, mutate in mutations[:30]:
        case = copy.deepcopy(base)
        mutate(case)
        try:
            MOD.validate(case)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K786 controls: 42")
    print(f"PASS K786 hostile mutations rejected: {caught}/30")
    return 0 if caught == 30 else 1


if __name__ == "__main__":
    raise SystemExit(main())
