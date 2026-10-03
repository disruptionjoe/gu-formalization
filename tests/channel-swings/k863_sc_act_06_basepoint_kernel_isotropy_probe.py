#!/usr/bin/env python3
"""Hostile mutations for K863."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k863", HERE / "k863_sc_act_06_basepoint_kernel_isotropy.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = MOD.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"),
        lambda p: p.update(target_claim="SC-ACT-01"),
        lambda p: p["basepoint_split"].update(isotropy_group="SO(12)"),
        lambda p: p["basepoint_split"].update(radial_summand_dimension=16383),
        lambda p: p["basepoint_split"].update(tangential_domain_dimension=212991),
        lambda p: p["basepoint_split"].update(tangential_response_rank=122863),
        lambda p: p["basepoint_split"].update(tangential_kernel_dimension=90127),
        lambda p: p["basepoint_split"].update(full_kernel_dimension=106511),
        lambda p: p["basepoint_split"].update(both_summands_SO13_invariant=False),
        lambda p: p["radial_isotropy_module"].update(restriction="Cl_14 is trivial"),
        lambda p: p["radial_isotropy_module"].update(irreducible_degrees=list(range(6))),
        lambda p: p["radial_isotropy_module"].update(irreducible_dimensions=[1, 13]),
        lambda p: p["radial_isotropy_module"].update(multiplicity_each_degree_0_through_6=2),
        lambda p: p["radial_isotropy_module"].update(dimension_check=8192),
        lambda p: p["decision"].update(radial_kernel_isotropy_module_authenticated=False),
        lambda p: p["decision"].update(tangential_irreducible_multiplicities_computed=True),
        lambda p: p["decision"].update(old_cohomology_module_authenticated=True),
        lambda p: p["decision"].update(q_lambda_promoted_to_owned_total_gauge=True),
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
    print(f"K863 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
