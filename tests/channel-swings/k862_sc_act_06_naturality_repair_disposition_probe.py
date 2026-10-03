#!/usr/bin/env python3
"""Hostile mutations for K862."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k862", HERE / "k862_sc_act_06_naturality_repair_disposition.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = MOD.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"),
        lambda p: p.update(target_claim="SC-ACT-01"),
        lambda p: p["compiled_result"].update(current_exact_old_cohomology_rank_known=True),
        lambda p: p["compiled_result"].update(current_rank_interval_under_grant=[90124, 90124]),
        lambda p: p["compiled_result"].update(homogeneous_maps_reduce_to_isotropy_intertwiners=False),
        lambda p: p["compiled_result"].update(ordinary_triviality_implies_natural_frame=True),
        lambda p: p["compiled_result"].update(current_old_isotropy_module_authenticated=True),
        lambda p: p["compiled_result"].update(current_owned_repair_intertwiners_supplied=True),
        lambda p: p["compiled_result"].update(current_flat_exact_admitted=True),
        lambda p: p["naturality_certificate"].update(row_count=10),
        lambda p: p["naturality_certificate"].update(all_rows_conjunctive=False),
        lambda p: p["naturality_certificate"].update(arbitrary_global_frame_allowed_as_owner=True),
        lambda p: p["naturality_certificate"].update(rank_lower_bound_allowed_as_exact_dimension=True),
        lambda p: p["exact_controls"].update(current_GU_candidate_admitted=True),
        lambda p: p["exact_controls"].update(all_single_row_omissions_reject=False),
        lambda p: p["decision"].update(naturality_reopens_an_ordinary_topological_obstruction=True),
        lambda p: p["decision"].update(current_flat_packet_repaired=True),
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
        except AssertionError:
            rejected += 1
    assert rejected == len(mutations) == base["controls"]["hostile_mutations_rejected"]
    print(f"K862 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
