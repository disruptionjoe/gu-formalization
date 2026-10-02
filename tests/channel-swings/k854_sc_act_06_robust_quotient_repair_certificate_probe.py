#!/usr/bin/env python3
"""Hostile mutations for K854."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k854", HERE / "k854_sc_act_06_robust_quotient_repair_certificate.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def main() -> int:
    base = MODULE.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"),
        lambda p: p.update(target_claim="SC-ACT-01"),
        lambda p: p["certificate"].update(exact_row_count=13),
        lambda p: p["certificate"].update(robust_row_count=14),
        lambda p: p["certificate"].update(logical_form="disjunction"),
        lambda p: p["certificate"].update(core_equality="raw rank"),
        lambda p: p["certificate"].update(uniformity_theorem="assume a gap"),
        lambda p: p["certificate"].update(uniform_gap_is_an_independent_GU_input=True),
        lambda p: p["certificate"].update(raw_rank_substitution_allowed=True),
        lambda p: p["exact_controls"]["complete_synthetic_candidate"].update(exact_admitted=False),
        lambda p: p["exact_controls"].update(all_single_row_omissions_reject_robust_admission=False),
        lambda p: p["exact_controls"].update(only_missing_robustness_row_preserves_exact_admission=False),
        lambda p: p["current_flat_packet"].update(owned_continuous_tau_bar_family=True),
        lambda p: p["current_flat_packet"]["evaluation"].update(exact_admitted=True),
        lambda p: p["decision"].update(K849_uniformity_row_decomposed_and_resolved=False),
        lambda p: p["decision"].update(current_flat_packet_exact_admitted=True),
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
    print(f"K854 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
