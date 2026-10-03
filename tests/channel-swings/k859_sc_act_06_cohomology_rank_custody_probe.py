#!/usr/bin/env python3
"""Hostile mutations for K859."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k859", HERE / "k859_sc_act_06_cohomology_rank_custody.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = MOD.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"),
        lambda p: p.update(target_claim="SC-ACT-01"),
        lambda p: p["rank_theorem"].update(authenticated_kernel_dimension=106511),
        lambda p: p["rank_theorem"].update(granted_symmetry_rank_ceiling=16387),
        lambda p: p["rank_theorem"].update(conditional_exact_rank_interval=[90124, 106511]),
        lambda p: p["rank_theorem"].update(current_certified_statement="dim(H_q)=90124"),
        lambda p: p["rank_theorem"].update(maximal_grant_is_not_owned_rank=False),
        lambda p: p["rank_theorem"].update(lower_bound_is_not_exact_rank=False),
        lambda p: p["exact_controls"].update(orbits=["native_positive"]),
        lambda p: p["exact_controls"].update(lower_endpoint=90123),
        lambda p: p["exact_controls"].update(upper_endpoint=106511),
        lambda p: p["exact_controls"].update(interval_width=0),
        lambda p: p["exact_controls"].update(abstract_attainable_count=1),
        lambda p: p["decision"].update(**{"90124_promoted_to_exact_bundle_rank": True}),
        lambda p: p["decision"].update(current_exact_old_cohomology_rank_known=True),
        lambda p: p["decision"].update(rank_nonidentifiability_under_current_custody=False),
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
    print(f"K859 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
