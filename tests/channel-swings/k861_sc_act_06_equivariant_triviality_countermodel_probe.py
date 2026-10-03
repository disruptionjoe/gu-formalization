#!/usr/bin/env python3
"""Hostile mutations for K861."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k861", HERE / "k861_sc_act_06_equivariant_triviality_countermodel.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = MOD.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"),
        lambda p: p.update(target_claim="SC-ACT-01"),
        lambda p: p["countermodel"].update(base="S^12"),
        lambda p: p["countermodel"].update(ordinary_rank=90),
        lambda p: p["countermodel"].update(ordinary_bundle_trivial=False),
        lambda p: p["countermodel"].update(rank_in_K856_stable_range=False),
        lambda p: p["countermodel"].update(isotropy_fixed_dimension=1),
        lambda p: p["countermodel"].update(nonzero_equivariant_section_exists=True),
        lambda p: p["countermodel"].update(equivariant_orthonormal_frame_exists=True),
        lambda p: p["countermodel"].update(ordinary_constant_frames_exist=False),
        lambda p: p["exact_control"].update(fibre_dimension=5),
        lambda p: p["exact_control"].update(stacked_infinitesimal_action_rank=5),
        lambda p: p["exact_control"].update(joint_invariant_dimension=1),
        lambda p: p["decision"].update(K856_ordinary_triviality_retracted=True),
        lambda p: p["decision"].update(K857_abstract_frame_promoted_to_natural_owner=True),
        lambda p: p["decision"].update(current_GU_naturality_gate_passed=True),
        lambda p: p.update(source_and_ledger_effect="SC-ACT-06_REFUTED"),
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
    print(f"K861 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
