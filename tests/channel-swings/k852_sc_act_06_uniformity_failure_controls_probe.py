#!/usr/bin/env python3
"""Hostile mutations for K852."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k852", HERE / "k852_sc_act_06_uniformity_failure_controls.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def main() -> int:
    base = MODULE.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"),
        lambda p: p.update(target_claim="SC-ACT-01"),
        lambda p: p["controls"]["noncompact_continuous_exact"].update(pointwise_exact=False),
        lambda p: p["controls"]["noncompact_continuous_exact"].update(continuous=False),
        lambda p: p["controls"]["noncompact_continuous_exact"].update(compact=True),
        lambda p: p["controls"]["noncompact_continuous_exact"].update(gap_infimum=1),
        lambda p: p["controls"]["noncompact_continuous_exact"].update(inverse_norm_supremum=1),
        lambda p: p["controls"]["compact_discontinuous_exact"].update(continuous=True),
        lambda p: p["controls"]["compact_discontinuous_exact"].update(compact=False),
        lambda p: p["controls"]["compact_discontinuous_exact"].update(gap_infimum=1),
        lambda p: p["controls"]["compact_continuous_nonexact"].update(pointwise_exact=True),
        lambda p: p["controls"]["compact_continuous_nonexact"].update(gap_minimum=1),
        lambda p: p["controls"]["compact_continuous_exact_positive"].update(gap_minimum=0),
        lambda p: p["decision"].update(compactness_is_load_bearing=False),
        lambda p: p["decision"].update(continuity_is_load_bearing=False),
        lambda p: p["decision"].update(pointwise_exactness_is_load_bearing=False),
        lambda p: p["decision"].update(finite_sampling_proves_uniformity=True),
        lambda p: p["decision"].update(source_owned_GU_family_tested=True),
        lambda p: p.update(source_and_ledger_effect="SC-ACT-06_REFUTED"),
        lambda p: p["probe_contract"].update(hostile_mutations_rejected=19),
    ]
    rejected = 0
    for mutate in mutations:
        packet = copy.deepcopy(base)
        mutate(packet)
        try:
            MODULE.validate(packet)
        except AssertionError:
            rejected += 1
    assert rejected == len(mutations) == base["probe_contract"]["hostile_mutations_rejected"]
    print(f"K852 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
