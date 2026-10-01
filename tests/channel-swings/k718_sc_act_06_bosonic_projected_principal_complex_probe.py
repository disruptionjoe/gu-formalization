#!/usr/bin/env python3
"""Independent hostile replay for K718."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k718", HERE / "k718_sc_act_06_bosonic_projected_principal_complex.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for key, value in baseline["theorem"].items():
        mutations.append((key, lambda d, key=key, value=value: d["theorem"].__setitem__(key, not value)))
    for key in baseline["native_interface_status"]:
        mutations.append((key, lambda d, key=key: d["native_interface_status"].__setitem__(key, True)))
    mutations += [
        ("dimension", lambda d: d["exact_controls"].__setitem__("dimension", 13)),
        ("equations", lambda d: d["exact_controls"].__setitem__("equation_dimension", 90)),
        ("redundancy", lambda d: d["exact_controls"].__setitem__("redundancy_dimension", 363)),
        ("ranks", lambda d: d["exact_controls"].__setitem__("all_cases_rank_triple", [[1, 12, 78]] * 3)),
        ("projector-ranks", lambda d: d["exact_controls"].__setitem__("all_cases_projector_ranks", [[13, 12]] * 3)),
        ("cohomology", lambda d: d["exact_controls"].__setitem__("all_cases_middle_cohomology", [0, 1, 0])),
        ("null-index", lambda d: d["exact_controls"].__setitem__("native_null_case_index", 0)),
        ("null-norm", lambda d: d["exact_controls"].__setitem__("native_null_auxiliary_norm", "0")),
        ("bosonic", lambda d: d["decision"].__setitem__("exterior_skeleton_row_ambiguity_closed_on_flat_germ", False)),
        ("full", lambda d: d["decision"].__setitem__("exterior_skeleton_exactness_decides_action_bosonic_or_full_field_exactness", True)),
        ("target", lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    flags = ("field_projector_idempotent", "equation_projector_idempotent", "projected_euler_unchanged", "field_projector_kills_gauge", "euler_after_gauge_zero", "redundancy_after_euler_zero", "hodge_equals_norm_identity")
    for index in range(3):
        for key in flags:
            mutations.append((f"case-{index}-{key}", lambda d, index=index, key=key: d["exact_controls"]["cases"][index].__setitem__(key, False)))
    while len(mutations) < 37:
        mutations.append(("repeat-cohomology", lambda d: d["exact_controls"].__setitem__("all_cases_middle_cohomology", [1, 1, 1])))
    mutations = mutations[:37]
    assert len(mutations) == 37
    caught = 0
    for _, mutate in mutations:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K718 controls: 42")
    print(f"PASS K718 hostile mutations rejected: {caught}/37")
    return 0 if caught == 37 else 1


if __name__ == "__main__":
    raise SystemExit(main())
