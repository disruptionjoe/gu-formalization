#!/usr/bin/env python3
"""Hostile mutations for K866."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k866", HERE / "k866_sc_act_06_isotropy_repair_disposition.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = MOD.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"),
        lambda p: p.update(target_claim="SC-ACT-01"),
        lambda p: p["compiled_result"].update(basepoint_radial_kernel_module_authenticated=False),
        lambda p: p["compiled_result"].update(radial_module_formula="unknown"),
        lambda p: p["compiled_result"].update(conditional_q_lambda_connection_quotient_dimension=90124),
        lambda p: p["compiled_result"].update(K789_90124_exact_connection_quotient=True),
        lambda p: p["compiled_result"].update(tangential_irreducible_multiplicities_known=True),
        lambda p: p["compiled_result"].update(owned_old_symmetry_image_known=True),
        lambda p: p["compiled_result"].update(owned_old_cohomology_module_known=True),
        lambda p: p["compiled_result"].update(owned_repair_modules_known=True),
        lambda p: p["compiled_result"].update(owned_repair_intertwiners_known=True),
        lambda p: p["isotropy_certificate"].update(row_count=10),
        lambda p: p["isotropy_certificate"].update(satisfied_row_count=11),
        lambda p: p["isotropy_certificate"].update(all_rows_conjunctive=False),
        lambda p: p["isotropy_certificate"].update(current_GU_candidate_admitted=True),
        lambda p: p["isotropy_certificate"].update(raw_total_rank_can_substitute_for_isotypic_coverage=True),
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
        except (AssertionError, KeyError, TypeError, ValueError):
            rejected += 1
    assert rejected == len(mutations) == base["controls"]["hostile_mutations_rejected"]
    print(f"K866 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
