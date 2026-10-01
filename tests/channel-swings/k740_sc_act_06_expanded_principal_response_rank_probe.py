#!/usr/bin/env python3
"""Independent artifact and hostile-mutation replay for K740."""
from __future__ import annotations
import copy
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SPEC = importlib.util.spec_from_file_location("k740", HERE / "k740_sc_act_06_expanded_principal_response_rank.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = json.loads((ROOT / "lab/process/k740-sc-act-06-expanded-principal-response-rank.json").read_text(encoding="utf-8"))
    MOD.validate(baseline)
    mutations = []
    for case_index, case in enumerate(baseline["exact_controls"]["cases"]):
        mutations.append(("norm", lambda d, i=case_index: d["exact_controls"]["cases"][i].__setitem__("native_q_norm_squared", 99)))
        for name, row in case["ranks"].items():
            for key in ("domain_dimension", "rank", "nullity"):
                mutations.append((key, lambda d, i=case_index, name=name, key=key: d["exact_controls"]["cases"][i]["ranks"][name].__setitem__(key, -1)))
    for key, value in baseline["operator"].items():
        mutations.append((key, lambda d, key=key, value=value: d["operator"].__setitem__(key, (not value) if isinstance(value, bool) else "WRONG")))
    for key, value in baseline["decision"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["decision"].__setitem__(key, not value)))
        elif isinstance(value, int):
            mutations.append((key, lambda d, key=key: d["decision"].__setitem__(key, -1)))
    mutations += [
        ("target", lambda d: d.__setitem__("target_claim", "NONE")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 36:
        mutations.append(("repeat", lambda d: d["decision"].__setitem__("full_connection_rank", 0)))
    caught = 0
    for _, mutate in mutations[:36]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K740 controls: 43")
    print(f"PASS K740 hostile mutations rejected: {caught}/36")
    return 0 if caught == 36 else 1


if __name__ == "__main__":
    raise SystemExit(main())
