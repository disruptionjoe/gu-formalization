#!/usr/bin/env python3
"""Hostile mutations for K864."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k864", HERE / "k864_sc_act_06_radial_grant_quotient.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = MOD.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"),
        lambda p: p.update(target_claim="SC-ACT-01"),
        lambda p: p["radial_grant"].update(candidate_domain_dimension=16383),
        lambda p: p["radial_grant"].update(candidate_injective=False),
        lambda p: p["radial_grant"].update(composition_zero=False),
        lambda p: p["radial_grant"].update(image_equals_radial_kernel_summand=False),
        lambda p: p["radial_grant"].update(source_action_owned_total_gauge=True),
        lambda p: p["conditional_connection_quotient"].update(kernel_dimension=106511),
        lambda p: p["conditional_connection_quotient"].update(granted_image_dimension=16383),
        lambda p: p["conditional_connection_quotient"].update(quotient_dimension=90124),
        lambda p: p["conditional_connection_quotient"].update(quotient_is_tangential_kernel=False),
        lambda p: p["metric_grant_separation"].update(metric_connection_component_at_flat_T0=4),
        lambda p: p["metric_grant_separation"].update(metric_rank_may_lower_connection_only_quotient=True),
        lambda p: p["metric_grant_separation"].update(K789_90124_is_exact_connection_quotient=True),
        lambda p: p["decision"].update(conditional_connection_quotient_rank_known=False),
        lambda p: p["decision"].update(conditional_connection_quotient_rank=90124),
        lambda p: p["decision"].update(current_owned_old_cohomology_rank_known=True),
        lambda p: p["decision"].update(K859_interval_retracted=True),
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
    print(f"K864 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
