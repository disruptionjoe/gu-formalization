#!/usr/bin/env python3
"""Hostile mutations for K860."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k860", HERE / "k860_sc_act_06_homogeneous_intertwiner_gate.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = MOD.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"),
        lambda p: p.update(target_claim="SC-ACT-01"),
        lambda p: p["theorem"].update(base="G"),
        lambda p: p["theorem"].update(bijection="Hom_G(E,F)=all linear maps"),
        lambda p: p["theorem"].update(rank_reduction="rank may jump"),
        lambda p: p["theorem"].update(composition_reduction="automatic"),
        lambda p: p["theorem"].update(exactness_reduction="sampled points suffice"),
        lambda p: p["theorem"].update(ordinary_triviality_is_not_in_this_bijection=False),
        lambda p: p["exact_control"].update(generic_intertwiner_shape="all matrices"),
        lambda p: p["exact_control"].update(forbidden_off_diagonal_entries=[]),
        lambda p: p["exact_control"].update(projection_times_injection=[[1]]),
        lambda p: p["exact_control"].update(image_equals_kernel=False),
        lambda p: p["exact_control"].update(rank_sum=1),
        lambda p: p["decision"].update(complete_cosphere_check_reduced_to_one_isotropy_fibre_after_equivariance=False),
        lambda p: p["decision"].update(current_GU_isotropy_modules_authenticated=True),
        lambda p: p["decision"].update(current_source_owned_intertwiners_constructed=True),
        lambda p: p.update(source_and_ledger_effect="SC-ACT-06_PROVED"),
        lambda p: p["controls"].update(hostile_mutations_rejected=17),
    ]
    rejected = 0
    for mutation in mutations:
        packet = copy.deepcopy(base)
        mutation(packet)
        try:
            MOD.validate(packet)
        except AssertionError:
            rejected += 1
    assert rejected == len(mutations) == base["controls"]["hostile_mutations_rejected"]
    print(f"K860 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
