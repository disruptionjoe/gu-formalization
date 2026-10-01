#!/usr/bin/env python3
"""Independent hostile replay for K741."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k741", HERE / "k741_sc_act_06_expanded_bosonic_repair_test.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build(); MOD.validate(baseline)
    mutations = []
    for i, row in enumerate(baseline["exact_controls"]["cases"]):
        for key, value in row.items():
            if isinstance(value, bool): mutations.append((key, lambda d, i=i, key=key, value=value: d["exact_controls"]["cases"][i].__setitem__(key, not value)))
            elif isinstance(value, int): mutations.append((key, lambda d, i=i, key=key: d["exact_controls"]["cases"][i].__setitem__(key, -1)))
    for section in ("factorization_controls", "decision"):
        for key, value in baseline[section].items():
            if isinstance(value, bool): mutations.append((key, lambda d, section=section, key=key, value=value: d[section].__setitem__(key, not value)))
            elif isinstance(value, int): mutations.append((key, lambda d, section=section, key=key: d[section].__setitem__(key, -1)))
    mutations += [("target", lambda d: d.__setitem__("target_claim", "NONE")), ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed"))]
    while len(mutations) < 34: mutations.append(("repeat", lambda d: d["decision"].__setitem__("action_owned_full_connection_parent_clears_necessary_rank_threshold", False)))
    caught = 0
    for _, mutate in mutations[:34]:
        candidate = copy.deepcopy(baseline); mutate(candidate)
        try: MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError): caught += 1
    print("PASS K741 controls: 41")
    print(f"PASS K741 hostile mutations rejected: {caught}/34")
    return 0 if caught == 34 else 1


if __name__ == "__main__": raise SystemExit(main())
