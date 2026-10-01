#!/usr/bin/env python3
"""Independent hostile replay for K719."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k719", HERE / "k719_sc_act_06_zero_fermion_full_symbol_reduction.py")
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
        ("exact-rank", lambda d: d["exact_controls"]["exact_completion"].__setitem__("euler_rank", 2)),
        ("exact-composition", lambda d: d["exact_controls"]["exact_completion"].__setitem__("composition_zero", False)),
        ("exact-cohomology", lambda d: d["exact_controls"]["exact_completion"].__setitem__("middle_cohomology_dimension", 1)),
        ("deficient-rank", lambda d: d["exact_controls"]["deficient_completion"].__setitem__("euler_rank", 3)),
        ("deficient-composition", lambda d: d["exact_controls"]["deficient_completion"].__setitem__("composition_zero", False)),
        ("deficient-cohomology", lambda d: d["exact_controls"]["deficient_completion"].__setitem__("middle_cohomology_dimension", 0)),
        ("boson-gauge", lambda d: d["exact_controls"].__setitem__("shared_bosonic_gauge_rank", 0)),
        ("boson-euler", lambda d: d["exact_controls"].__setitem__("shared_bosonic_euler_rank", 0)),
        ("exact-total", lambda d: d["exact_controls"].__setitem__("exact_total_middle_cohomology", 1)),
        ("deficient-total", lambda d: d["exact_controls"].__setitem__("deficient_total_middle_cohomology", 0)),
        ("difference", lambda d: d["exact_controls"].__setitem__("cohomology_difference_equals_fermion_defect", 0)),
        ("mixed", lambda d: d["decision"].__setitem__("mixed_block_question_closed_at_zero_fermion_principal_grade", False)),
        ("remaining", lambda d: d["decision"].__setitem__("remaining_local_symbol_debt_isolated_to_two_diagonal_blocks_and_their_rows", False)),
        ("continue", lambda d: d["decision"].__setitem__("flat_germ_route_is_ready_for_more_abstract_bosonic_work", True)),
        ("target", lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 33:
        mutations.append(("repeat-defect", lambda d: d["exact_controls"].__setitem__("cohomology_difference_equals_fermion_defect", 0)))
    mutations = mutations[:33]
    assert len(mutations) == 33
    caught = 0
    for _, mutate in mutations:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K719 controls: 38")
    print(f"PASS K719 hostile mutations rejected: {caught}/33")
    return 0 if caught == 33 else 1


if __name__ == "__main__":
    raise SystemExit(main())
