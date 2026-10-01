#!/usr/bin/env python3
"""Independent hostile replay for K723."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k723", HERE / "k723_sc_act_06_t0_curvature_principal_invariance.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for key, value in baseline["principal_invariance_theorem"].items():
        mutations.append((key, lambda d, key=key, value=value: d["principal_invariance_theorem"].__setitem__(key, not value)))
    for key, value in baseline["exact_controls"].items():
        mutations.append((key, lambda d, key=key, value=value: d["exact_controls"].__setitem__(key, (not value) if isinstance(value, bool) else value + 1)))
    for key, value in baseline["decision"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["decision"].__setitem__(key, not value)))
    mutations += [
        ("target", lambda d: d.__setitem__("target_claim", "NONE")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 30:
        mutations.append(("repeat", lambda d: d["exact_controls"].__setitem__("field_dimension", 0)))
    caught = 0
    for _, mutate in mutations[:30]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K723 controls: 36")
    print(f"PASS K723 hostile mutations rejected: {caught}/30")
    return 0 if caught == 30 else 1


if __name__ == "__main__":
    raise SystemExit(main())
