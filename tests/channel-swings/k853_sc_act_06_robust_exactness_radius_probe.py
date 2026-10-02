#!/usr/bin/env python3
"""Hostile mutations for K853."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k853", HERE / "k853_sc_act_06_robust_exactness_radius.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def main() -> int:
    base = MODULE.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"),
        lambda p: p.update(target_claim="SC-ACT-01"),
        lambda p: p["theorem"].update(baseline_gap="pointwise"),
        lambda p: p["theorem"].update(hodge_difference_bound="epsilon"),
        lambda p: p["theorem"].update(stability_condition="always"),
        lambda p: p["theorem"].update(explicit_radius="infinity"),
        lambda p: p["theorem"].update(composition_is_required=False),
        lambda p: p["theorem"].update(positive_hodge_without_composition_certifies_a_complex=True),
        lambda p: p["exact_controls"]["baseline"].update(mu=0),
        lambda p: p["exact_controls"]["certified_radius"].update(decimal=1),
        lambda p: p["exact_controls"]["certified_radius"].update(difference_bound=1.2),
        lambda p: p["exact_controls"]["certified_radius"].update(bound_below_mu=False),
        lambda p: p["exact_controls"]["safe_diagonal_perturbation"].update(composition_zero=False),
        lambda p: p["exact_controls"]["composition_breaker"].update(valid_complex=True),
        lambda p: p["exact_controls"]["outside_radius_collapse"].update(middle_exact=True),
        lambda p: p["decision"].update(K851_uniform_gap_has_quantitative_stability_margin=False),
        lambda p: p["decision"].update(arbitrary_perturbations_preserve_complex_structure=True),
        lambda p: p["decision"].update(source_owned_GU_perturbation_constructed=True),
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
    print(f"K853 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
