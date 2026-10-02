#!/usr/bin/env python3
"""Hostile mutations for K850."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k850", HERE / "k850_sc_act_06_flat_quotient_repair_interface.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def main() -> int:
    base = MODULE.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"),
        lambda p: p.update(target_claim="SC-ACT-01"),
        lambda p: p["current_flat_packet"].update(old_middle_cohomology_lower_bound=0),
        lambda p: p["current_flat_packet"].update(source_or_action_owned_tau_bar=True),
        lambda p: p["current_flat_packet"].update(source_or_action_owned_S_bar=True),
        lambda p: p["current_flat_packet"].update(exact_dim_H_q=True),
        lambda p: p["current_flat_packet"].update(kernel_image_equality_every_q=True),
        lambda p: p["future_packet_contract"].update(for_each_nonzero_covector_q=False),
        lambda p: p["future_packet_contract"].update(old_cohomology="ker J"),
        lambda p: p["future_packet_contract"].update(exactness="rank threshold"),
        lambda p: p["future_packet_contract"].update(effective_dimension_identity="raw ranks"),
        lambda p: p["future_packet_contract"].update(uniform_lower_bound_consequence="none"),
        lambda p: p["future_packet_contract"].update(lower_bound_is_sufficient=True),
        lambda p: p["future_packet_contract"].update(raw_rank_budget_is_sufficient=True),
        lambda p: p["decision"].update(K845_scalar_budget_retained_as_necessary=False),
        lambda p: p["decision"].update(current_flat_packet_passes_certificate=True),
        lambda p: p["decision"].update(current_flat_packet_repairability_refuted=True),
        lambda p: p["decision"].update(SC_ACT_06_proved_or_refuted=True),
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
    print(f"K850 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
