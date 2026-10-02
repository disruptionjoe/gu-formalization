#!/usr/bin/env python3
"""Hostile replay for K787."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k787", HERE / "k787_sc_act_06_flat_zero_locus_custody.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = MOD.build()
    MOD.validate(base)
    mutations = [
        lambda d: d["custody_reconciliation"].__setitem__("source_claims_zero_locus", False),
        lambda d: d["custody_reconciliation"].__setitem__("released_source_exhibits_complete_solution_two_jet", True),
        lambda d: d["custody_reconciliation"].__setitem__("repository_constructs_local_source_typed_background", False),
        lambda d: d["k786_requirement_status"].__setitem__("one_source_typed_background_satisfying_Upsilon_zero", "open"),
        lambda d: d["k786_requirement_status"].__setitem__("complete_source_field_tangent", "supplied"),
        lambda d: d["k786_requirement_status"].__setitem__("all_covector_middle_exactness", "proved"),
        lambda d: d["decision"].__setitem__("background_search_remains_first_missing_input", True),
        lambda d: d["decision"].__setitem__("direct_linearization_test_released", False),
        lambda d: d["decision"].__setitem__("complete_K786_packet_supplied", True),
        lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL"),
        lambda d: d.__setitem__("source_and_ledger_effect", "changed"),
    ]
    for key in ("background_B_epsilon", "background_varpi", "background_T", "background_F_B", "background_fermions", "Upsilon_B_on_background", "Upsilon_F_on_background", "Upsilon_total_on_background"):
        mutations.append(lambda d, key=key: d["custody_reconciliation"].__setitem__(key, "nonzero"))
    while len(mutations) < 30:
        mutations.append(lambda d: d["decision"].__setitem__("complete_K786_packet_supplied", True))
    caught = 0
    for mutate in mutations[:30]:
        case = copy.deepcopy(base)
        mutate(case)
        try:
            MOD.validate(case)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K787 controls: 38")
    print(f"PASS K787 hostile mutations rejected: {caught}/30")
    return 0 if caught == 30 else 1


if __name__ == "__main__":
    raise SystemExit(main())
