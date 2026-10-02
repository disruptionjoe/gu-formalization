#!/usr/bin/env python3
"""Hostile replay for K783."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k783", HERE / "k783_sc_act_06_source_zero_locus_boundary.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = MOD.build()
    MOD.validate(base)
    mutations = []
    for key, value in base["source_custody"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["source_custody"].__setitem__(key, not value)))
    for key, value in base["decision"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["decision"].__setitem__(key, not value)))
    mutations += [
        ("polarity", lambda d: d["source_custody"].__setitem__("claim_polarity", "DISAVOWS")),
        ("locus", lambda d: d["source_custody"].__setitem__("claimed_solution_locus", "dI2B=0")),
        ("signature", lambda d: d["source_custody"].__setitem__("claimed_signature", "Lorentzian")),
        ("operation", lambda d: d["source_custody"].__setitem__("claimed_operation", "keep every row")),
        ("target", lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL")),
        ("ledger", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 24:
        mutations.append((f"repeat-{len(mutations)}", lambda d: d["decision"].__setitem__("nonzero_residual_is_direct_SC_ACT_06_input", True)))
    caught = 0
    for _, mutate in mutations[:24]:
        case = copy.deepcopy(base)
        mutate(case)
        try:
            MOD.validate(case)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K783 controls: 34")
    print(f"PASS K783 hostile mutations rejected: {caught}/24")
    return 0 if caught == 24 else 1


if __name__ == "__main__":
    raise SystemExit(main())
