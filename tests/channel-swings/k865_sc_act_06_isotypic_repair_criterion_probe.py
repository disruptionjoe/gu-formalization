#!/usr/bin/env python3
"""Hostile mutations for K865."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k865", HERE / "k865_sc_act_06_isotypic_repair_criterion.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = MOD.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"),
        lambda p: p.update(target_claim="SC-ACT-01"),
        lambda p: p["theorem"].update(group="SO(14)"),
        lambda p: p["theorem"].update(compact_semisimplicity_used=False),
        lambda p: p["theorem"].update(division_algebras_allowed=["R"]),
        lambda p: p["theorem"].update(intertwiners_reduce_to_multiplicity_space_maps=False),
        lambda p: p["theorem"].update(exact_pair_exists_iff="total dimensions agree"),
        lambda p: p["theorem"].update(raw_total_dimension_suffices=True),
        lambda p: p["exact_controls"]["typed_exact_control"].update(H_multiplicities={"trivial": 3}),
        lambda p: p["exact_controls"]["typed_exact_control"].update(criterion_passes=False),
        lambda p: p["exact_controls"]["typed_exact_control"].update(image_equals_kernel_by_type=False),
        lambda p: p["exact_controls"]["dimension_matched_type_mismatch"].update(raw_dimension_H=12),
        lambda p: p["exact_controls"]["dimension_matched_type_mismatch"].update(missing_type="trivial"),
        lambda p: p["exact_controls"]["dimension_matched_type_mismatch"].update(Hom_SO13_A_to_H_rank=13),
        lambda p: p["exact_controls"]["dimension_matched_type_mismatch"].update(criterion_passes=True),
        lambda p: p["decision"].update(raw_rank_budget_is_sufficient_for_naturality=True),
        lambda p: p["decision"].update(current_GU_repair_admitted=True),
        lambda p: p["decision"].update(SC_ACT_06_proved_or_refuted=True),
        lambda p: p.update(source_and_ledger_effect="SC-ACT-06_PROVED"),
        lambda p: p["controls"].update(hostile_mutations_rejected=19),
    ]
    rejected = 0
    for mutation in mutations:
        packet = copy.deepcopy(base)
        mutation(packet)
        try:
            MOD.validate(packet)
        except (AssertionError, KeyError, TypeError, ValueError):
            rejected += 1
    assert rejected == len(mutations) == base["controls"]["hostile_mutations_rejected"]
    print(f"K865 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
