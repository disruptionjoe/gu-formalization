#!/usr/bin/env python3
"""K431 parallel-projector observation descent for the K429 differential."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F

from k429_k77_covariant_incoming_domain_green import (
    A_at,
    SAMPLES,
    U_at,
    U_prime_at,
    add,
    matmul,
    matvec,
    sub,
    transpose,
    vector_sub,
    zero_matrix,
    zero_vector,
)


P0 = [[F(1), F(0)], [F(0), F(0)]]
J = [[F(0), F(-1)], [F(1), F(0)]]


def P_at(x: F):
    return matmul(matmul(U_at(x), P0), transpose(U_at(x)))


def P_prime_at(x: F):
    return add(
        matmul(matmul(U_prime_at(x), P0), transpose(U_at(x))),
        matmul(matmul(U_at(x), P0), transpose(U_prime_at(x))),
    )


def commutator_defect_at(projector, projector_prime, x: F):
    return add(projector_prime, sub(matmul(A_at(x), projector), matmul(projector, A_at(x))))


def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def rank2(matrix):
    if det2(matrix) != 0:
        return 2
    if any(entry != 0 for row in matrix for entry in row):
        return 1
    return 0


def primitive_g_at(x: F):
    return [x + x * x / 2, x - x * x]


def verify_green_intertwining_at(x: F) -> bool:
    green_f = matvec(U_at(x), primitive_g_at(x))
    projected_green = matvec(P_at(x), green_f)
    green_projected = matvec(U_at(x), [primitive_g_at(x)[0], F(0)])
    return zero_vector(vector_sub(projected_green, green_projected))


def demo() -> dict:
    parallel = all(zero_matrix(commutator_defect_at(P_at(x), P_prime_at(x), x)) for x in SAMPLES)
    zeros = [[F(0), F(0)], [F(0), F(0)]]
    constant_defects = [commutator_defect_at(P0, zeros, x) for x in SAMPLES]
    endpoint_compatibility = sub(matmul(P_at(F(1)), J), matmul(J, P_at(F(0))))
    identity_twist_defect = sub(P_at(F(1)), P_at(F(0)))
    idempotent = all(zero_matrix(sub(matmul(P_at(x), P_at(x)), P_at(x))) for x in SAMPLES)
    self_adjoint = all(zero_matrix(sub(transpose(P_at(x)), P_at(x))) for x in SAMPLES)
    assert parallel and idempotent and self_adjoint
    assert all(rank2(defect) == 2 for defect in constant_defects)
    assert zero_matrix(endpoint_compatibility)
    assert not zero_matrix(identity_twist_defect)
    assert all(verify_green_intertwining_at(x) for x in SAMPLES)
    return {
        "schema_version": "1.0",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "descent_theorem": {
            "projector": "P(t)^2=P(t)=P(t)^T",
            "criterion": "D_A(Pu)=P D_Au iff P'+[A,P]=0",
            "interpretation": "the observed subbundle must be parallel for the action connection",
            "boundary_compatibility": "P(1)R=R P(0)",
        },
        "exact_parallel_fixture": {
            "projector": "P(t)=U(t) diag(1,0) U(t)^T",
            "idempotent": idempotent,
            "self_adjoint": self_adjoint,
            "parallel_defect_zero": parallel,
            "rank": 1,
            "incoming_green_intertwines": all(verify_green_intertwining_at(x) for x in SAMPLES),
            "monodromy_twist_boundary_compatible": zero_matrix(endpoint_compatibility),
            "identity_twist_boundary_compatible": zero_matrix(identity_twist_defect),
        },
        "shortcut_control": {
            "constant_projector": "diag(1,0)",
            "commutator_defect_rank": min(rank2(defect) for defect in constant_defects),
            "descends": False,
        },
        "observed_subcomplex": {
            "carrier_rank": 1,
            "differential": "ordinary derivative after parallel trivialization",
            "incoming_kernel_dimension": 0,
            "incoming_cokernel_dimension": 0,
            "monodromy_matched_kernel_dimension": 1,
            "monodromy_matched_cokernel_dimension": 1,
        },
        "decision": {
            "same_carrier_observation_descent_constructed": True,
            "arbitrary_constant_projector_descends": False,
            "green_intertwining_requires_parallelism_and_boundary_compatibility": True,
            "corrected_clifford_projector_identified": False,
            "physical_observation_or_cohomology_constructed": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
