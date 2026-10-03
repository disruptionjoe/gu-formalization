#!/usr/bin/env python3
"""Hostile mutations for K867."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k867", HERE / "k867_sc_act_06_compact_equivariance_audit.py")
MOD = importlib.util.module_from_spec(SPEC); assert SPEC.loader; SPEC.loader.exec_module(MOD)

def main() -> int:
    base = MOD.build()
    mutations = [
        lambda p: p.update(classification="CONVENTIONAL_ROUTE"), lambda p: p.update(target_claim="SC-ACT-01"),
        lambda p: p["forms"].update(native_signature_counts=[13, 1]), lambda p: p["exact_kernel_witness"].update(J_q_u_zero=False),
        lambda p: p["rotation_controls"]["same_native_sign_rotation"].update(preserves_native_form=False),
        lambda p: p["rotation_controls"]["same_native_sign_rotation"].update(rotated_witness_remains_in_kernel=False),
        lambda p: p["rotation_controls"]["cross_native_sign_rotation"].update(determinant=-1),
        lambda p: p["rotation_controls"]["cross_native_sign_rotation"].update(fixes_q=False),
        lambda p: p["rotation_controls"]["cross_native_sign_rotation"].update(belongs_to_auxiliary_SO13=False),
        lambda p: p["rotation_controls"]["cross_native_sign_rotation"].update(preserves_native_form=True),
        lambda p: p["rotation_controls"]["cross_native_sign_rotation"].update(rotated_witness_remains_in_kernel=True),
        lambda p: p["rotation_controls"]["cross_native_sign_rotation"].update(nonzero_response_term_count=0),
        lambda p: p["decision"].update(K788_kernel_is_auxiliary_SO13_module=True),
        lambda p: p["decision"].update(K863_SO13_tangential_kernel_claim_valid=True),
        lambda p: p["decision"].update(K863_dimension_split_retracted=True),
        lambda p: p["decision"].update(K864_conditional_quotient_dimension_retracted=True),
        lambda p: p["decision"].update(K865_abstract_compact_representation_theorem_retracted=True),
        lambda p: p["decision"].update(SC_ACT_06_proved_or_refuted=True),
        lambda p: p.update(source_and_ledger_effect="SC-ACT-06_REFUTED"),
        lambda p: p["controls"].update(hostile_mutations_rejected=19),
    ]
    rejected = 0
    for mutation in mutations:
        packet = copy.deepcopy(base); mutation(packet)
        try: MOD.validate(packet)
        except (AssertionError, KeyError, TypeError, ValueError): rejected += 1
    assert rejected == len(mutations) == base["controls"]["hostile_mutations_rejected"]
    print(f"K867 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0

if __name__ == "__main__": raise SystemExit(main())
