#!/usr/bin/env python3
"""Hostile mutations for K849."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k849", HERE / "k849_sc_act_06_exact_repair_certificate.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def main() -> int:
    base = MODULE.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"),
        lambda p: p.update(target_claim="SC-ACT-01"),
        lambda p: p["certificate"].update(row_count=9),
        lambda p: p["certificate"].update(rows=MODULE.ROWS[:-1]),
        lambda p: p["certificate"].update(logical_form="disjunction"),
        lambda p: p["certificate"].update(core_equality="rank only"),
        lambda p: p["certificate"].update(raw_rank_substitution_allowed=True),
        lambda p: p["exact_controls"]["complete_synthetic_candidate"].update(admitted=False),
        lambda p: p["exact_controls"]["complete_synthetic_candidate"].update(missing_rows=["ownership"]),
        lambda p: p["exact_controls"].update(all_single_row_omissions_rejected=False),
        lambda p: p["exact_controls"]["one_missing_row_controls"].pop("kernel_image_equality"),
        lambda p: p["exact_controls"]["one_missing_row_controls"]["kernel_image_equality"].update(admitted=True),
        lambda p: p["exact_controls"]["one_missing_row_controls"]["kernel_image_equality"].update(missing_rows=[]),
        lambda p: p["decision"].update(necessary_and_sufficient_finite_symbol_interface_emitted=False),
        lambda p: p["decision"].update(rank_threshold_without_descent_and_overlap_rejected=False),
        lambda p: p["decision"].update(source_owned_GU_candidate_admitted=True),
        lambda p: p["decision"].update(next_exact_input="Use raw ranks."),
        lambda p: p.update(source_and_ledger_effect="SC-ACT-06_REFUTED"),
        lambda p: p["pinned_inputs"]["k847"].update(sha256="bad"),
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
    print(f"K849 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
