#!/usr/bin/env python3
"""Hostile mutations for K1126."""
from copy import deepcopy
from k1126_k895_first_order_formal_adjoint_correction import build, validate


def main():
    mutations = [
        ("formal_adjoint", "D*=sum A^T partial"),
        ("principal_self_adjoint_condition", "A_mu^T=A_mu"),
        ("fourier_condition", "A(xi) is Hermitian"),
        ("fixture_A_transpose", [[0, 2], [-2, 0]]),
        ("fixture_formally_self_adjoint", False),
        ("k895_selected_coefficient_rank", 130911),
        ("k895_coefficient_is_skew", False),
        ("k895_zero_order_transpose_defect_rank_retired", 0),
        ("k895_first_order_principal_helmholtz_defect_rank", 130912),
        ("k895_principal_obstruction_survives", True),
        ("complete_hessian_established", True),
        ("remaining_requirements", []),
        ("correction_scope", "all ranks withdrawn"),
        ("source_and_ledger_effect", "PROMOTED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1126 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
