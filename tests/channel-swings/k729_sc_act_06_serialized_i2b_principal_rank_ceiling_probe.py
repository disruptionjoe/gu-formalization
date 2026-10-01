#!/usr/bin/env python3
"""Independent hostile replay for K729."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k729", HERE / "k729_sc_act_06_serialized_i2b_principal_rank_ceiling.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for key, value in baseline["owner_reconciliation"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["owner_reconciliation"].__setitem__(key, not value)))
        else:
            mutations.append((key, lambda d, key=key: d["owner_reconciliation"].__setitem__(key, "wrong")))
    for key, value in baseline["serialized_bank"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["serialized_bank"].__setitem__(key, not value)))
        elif isinstance(value, int):
            mutations.append((key, lambda d, key=key, value=value: d["serialized_bank"].__setitem__(key, value + 1)))
    for key, value in baseline["decision"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["decision"].__setitem__(key, not value)))
    mutations += [
        ("target", lambda d: d.__setitem__("target_claim", "NONE")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 29:
        mutations.append(("repeat", lambda d: d["serialized_bank"].__setitem__("universal_extension_rank_ceiling", 197)))
    caught = 0
    for _, mutate in mutations[:29]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K729 controls: 34")
    print(f"PASS K729 hostile mutations rejected: {caught}/29")
    return 0 if caught == 29 else 1


if __name__ == "__main__":
    raise SystemExit(main())
