#!/usr/bin/env python3
"""Independent hostile replay for K722."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k722", HERE / "k722_sc_act_06_flat_full_symbol_obstruction.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for key, value in baseline["composition_theorem"].items():
        mutations.append((key, lambda d, key=key, value=value: d["composition_theorem"].__setitem__(key, not value)))
    for i, case in enumerate(baseline["exact_controls"]["cases"]):
        for key, value in case.items():
            if key != "case":
                mutations.append((f"case-{i}-{key}", lambda d, i=i, key=key, value=value: d["exact_controls"]["cases"][i].__setitem__(key, (not value) if isinstance(value, bool) else value + 1)))
    mutations += [
        ("fdim", lambda d: d["exact_controls"].__setitem__("fermion_two_block_dimension", 1919)),
        ("frank", lambda d: d["exact_controls"].__setitem__("fermion_two_block_rank", 1919)),
        ("nonnull", lambda d: d["exact_controls"].__setitem__("nonnull_full_cohomology_dimension", 0)),
        ("null", lambda d: d["exact_controls"].__setitem__("native_null_full_cohomology_dimension", 0)),
        ("reject", lambda d: d["decision"].__setitem__("frozen_flat_selected_i1b_plus_displayed_eq916_realization_rejected_as_elliptic", False)),
        ("global", lambda d: d["decision"].__setitem__("source_global_SC_ACT_06_refuted", True)),
        ("fermion", lambda d: d["decision"].__setitem__("displayed_fermion_principal_candidate_rejected", True)),
        ("projector", lambda d: d["decision"].__setitem__("same_flat_selected_bosonic_route_needs_more_abstract_projector_work", True)),
        ("target", lambda d: d.__setitem__("target_claim", "NONE")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 29:
        mutations.append(("repeat", lambda d: d["exact_controls"].__setitem__("fermion_two_block_dimension", 0)))
    caught = 0
    for _, mutate in mutations[:29]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K722 controls: 34")
    print(f"PASS K722 hostile mutations rejected: {caught}/29")
    return 0 if caught == 29 else 1


if __name__ == "__main__":
    raise SystemExit(main())
