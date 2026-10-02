#!/usr/bin/env python3
"""Hostile mutations for K847."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("k847_sc_act_06_quotient_repair_theorem.py")
SPEC = importlib.util.spec_from_file_location("k847", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def main() -> int:
    base = MODULE.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"),
        lambda p: p.update(target_claim="SC-ACT-01"),
        lambda p: p["gu_typed_objects"].update(action_owner="source-action"),
        lambda p: p["theorem"].update(old_middle_cohomology="ker(J)"),
        lambda p: p["theorem"].update(new_response="tau:E1->F"),
        lambda p: p["theorem"].update(new_symmetry="S:U->E1"),
        lambda p: p["theorem"].update(repaired_middle_cohomology="H"),
        lambda p: p["theorem"].update(exactness_criterion="rank budget only"),
        lambda p: p["theorem"].update(raw_rank_budget_is_sufficient=True),
        lambda p: p["theorem"].update(effective_rank_equality_is_sufficient_under_composition=False),
        lambda p: p["exact_control"].update(old_middle_cohomology_dimension=3),
        lambda p: p["exact_control"].update(response_effective_rank_on_old_cohomology=0),
        lambda p: p["exact_control"].update(symmetry_effective_rank_in_response_kernel=0),
        lambda p: p["exact_control"].update(response_descends_to_old_cohomology=False),
        lambda p: p["exact_control"].update(new_response_kills_new_symmetry=False),
        lambda p: p["exact_control"].update(new_middle_cohomology_dimension=1),
        lambda p: p["exact_control"].update(middle_exact_after_repair=False),
        lambda p: p["decision"].update(source_owned_GU_repair_constructed=True),
        lambda p: p.update(source_and_ledger_effect="SC-ACT-06_REFUTED"),
        lambda p: p["controls"].update(hostile_mutations_rejected=19),
    ]
    rejected = 0
    for mutate in mutations:
        packet = copy.deepcopy(base)
        mutate(packet)
        try:
            MODULE.validate(packet)
        except AssertionError:
            rejected += 1
    assert rejected == len(mutations) == base["controls"]["hostile_mutations_rejected"]
    print(f"K847 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
