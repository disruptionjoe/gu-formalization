#!/usr/bin/env python3
"""Hostile mutations for K851."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k851", HERE / "k851_sc_act_06_compact_cosphere_hodge_gap.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def main() -> int:
    base = MODULE.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"),
        lambda p: p.update(target_claim="SC-ACT-01"),
        lambda p: p["theorem"].update(base="noncompact K"),
        lambda p: p["theorem"].update(data="arbitrary maps"),
        lambda p: p["theorem"].update(pointwise_exactness="raw rank threshold"),
        lambda p: p["theorem"].update(middle_hodge_operator="tau only"),
        lambda p: p["theorem"].update(kernel_identity="ker tau"),
        lambda p: p["theorem"].update(exactness_equivalence="always"),
        lambda p: p["theorem"].update(compactness_conclusion="pointwise only"),
        lambda p: p["theorem"].update(uniform_splitting="unbounded"),
        lambda p: p["theorem"].update(uniform_gap_is_separate_input_after_hypotheses=True),
        lambda p: p["exact_family_control"].update(analytic_uniform_gap=0),
        lambda p: p["exact_family_control"].update(all_cardinal_compositions_zero=False),
        lambda p: p["exact_family_control"].update(all_cardinal_exact=False),
        lambda p: p["exact_family_control"]["cardinal_checks"][0].update(rank_tau=1),
        lambda p: p["decision"].update(K849_uniformity_row_resolved_conditionally=False),
        lambda p: p["decision"].update(finite_covector_sampling_sufficient=True),
        lambda p: p["decision"].update(source_owned_GU_maps_constructed=True),
        lambda p: p.update(source_and_ledger_effect="SC-ACT-06_PROVED"),
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
    print(f"K851 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
