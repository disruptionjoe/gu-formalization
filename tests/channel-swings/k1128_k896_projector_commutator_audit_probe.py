#!/usr/bin/env python3
"""Hostile mutations for K1128."""
from copy import deepcopy
from k1128_k896_projector_commutator_audit import build, validate


def main():
    mutations = [
        ("formal_projector", "T=A"), ("transpose", "T^T=(I-P)A"),
        ("first_order_self_adjoint_condition", "T^T=T"),
        ("equivalent_condition", "{P,A}=2A"),
        ("corrected_defect", "T-T^T"), ("corrected_defect_rank", 130912),
        ("retired_zero_order_defect_rank", 16382), ("completed_map_rank", 0),
        ("radial_descent_restored", False), ("first_order_principal_integrability", True),
        ("projector_action_owned", True), ("classification_theorem", "Q^T=Q"),
        ("zero_order_symmetric_completion_classification_survives", True),
        ("correction_scope", "no correction"), ("source_and_ledger_effect", "PROMOTED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1128 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
