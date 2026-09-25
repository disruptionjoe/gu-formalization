#!/usr/bin/env python3
"""K432 exact compressed H640-to-observed covariant intertwiner fixture.

The rank-two carriers below are a conditional rational surrogate for the two
rank-640 carriers in the inherited H640 observation-isomorphism result.  No
rank-640 or rank-1920 matrix is constructed or serialized here.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F

from k429_k77_covariant_incoming_domain_green import (
    A_at,
    I2,
    SAMPLES,
    U_at,
    U_prime_at,
    add,
    g_at,
    matmul,
    matvec,
    primitive_g_at,
    sub,
    transpose,
    v_at,
    vector_sub,
    zero_matrix,
    zero_vector,
)
from k431_k77_parallel_observation_descent import (
    P0,
    P_at,
    P_prime_at,
    commutator_defect_at,
)


F_OBS = [[F(1), F(1)], [F(0), F(1)]]
F_OBS_INV = [[F(1), F(-1)], [F(0), F(1)]]
H_OBS = matmul(transpose(F_OBS_INV), F_OBS_INV)
P_OBS = matmul(matmul(F_OBS, P0), F_OBS_INV)
ZERO2 = [[F(0), F(0)], [F(0), F(0)]]


def observation_at(x: F):
    """J(t): conditional native H carrier -> distinct observed carrier."""
    return matmul(F_OBS, transpose(U_at(x)))


def observation_prime_at(x: F):
    return matmul(F_OBS, transpose(U_prime_at(x)))


def lift_at(x: F):
    """L(t)=J(t)^-1: observed carrier -> conditional native H carrier."""
    return matmul(U_at(x), F_OBS_INV)


def lift_prime_at(x: F):
    return matmul(U_prime_at(x), F_OBS_INV)


def native_source_at(x: F):
    return matvec(U_at(x), g_at(x))


def native_green_at(x: F):
    return matvec(U_at(x), primitive_g_at(x))


def observed_source_at(x: F):
    return matvec(F_OBS, g_at(x))


def observed_green_at(x: F):
    return matvec(F_OBS, primitive_g_at(x))


def projected_native_green_at(x: F):
    return matvec(U_at(x), matvec(P0, primitive_g_at(x)))


def projected_observed_green_at(x: F):
    return matvec(F_OBS, matvec(P0, primitive_g_at(x)))


def exact_checks() -> dict[str, bool]:
    observation_inverse = all(
        zero_matrix(sub(matmul(observation_at(x), lift_at(x)), I2)) for x in SAMPLES
    )
    lift_inverse = all(
        zero_matrix(sub(matmul(lift_at(x), observation_at(x)), I2)) for x in SAMPLES
    )
    gram_transport = all(
        zero_matrix(
            sub(
                matmul(matmul(transpose(observation_at(x)), H_OBS), observation_at(x)),
                I2,
            )
        )
        for x in SAMPLES
    )
    observation_covariant = all(
        zero_matrix(sub(observation_prime_at(x), matmul(observation_at(x), A_at(x))))
        for x in SAMPLES
    )
    lift_covariant = all(
        zero_matrix(add(lift_prime_at(x), matmul(A_at(x), lift_at(x))))
        for x in SAMPLES
    )
    native_projector_idempotent = all(
        zero_matrix(sub(matmul(P_at(x), P_at(x)), P_at(x))) for x in SAMPLES
    )
    observed_projector_idempotent = zero_matrix(sub(matmul(P_OBS, P_OBS), P_OBS))
    native_projector_self_adjoint = all(
        zero_matrix(sub(transpose(P_at(x)), P_at(x))) for x in SAMPLES
    )
    observed_projector_h_self_adjoint = zero_matrix(
        sub(matmul(transpose(P_OBS), H_OBS), matmul(H_OBS, P_OBS))
    )
    observation_projector_intertwines = all(
        zero_matrix(
            sub(matmul(observation_at(x), P_at(x)), matmul(P_OBS, observation_at(x)))
        )
        for x in SAMPLES
    )
    lift_projector_intertwines = all(
        zero_matrix(sub(matmul(P_at(x), lift_at(x)), matmul(lift_at(x), P_OBS)))
        for x in SAMPLES
    )
    native_projector_parallel = all(
        zero_matrix(commutator_defect_at(P_at(x), P_prime_at(x), x)) for x in SAMPLES
    )
    observed_projector_parallel = zero_matrix(ZERO2)

    native_u0 = matvec(U_at(F(0)), v_at(F(0)))
    observed_u0 = matvec(observation_at(F(0)), native_u0)
    lifted_u0 = matvec(lift_at(F(0)), observed_u0)
    boundary_maps = zero_vector(native_u0) and zero_vector(observed_u0)
    boundary_inverse = zero_vector(vector_sub(lifted_u0, native_u0))
    boundary_projection_preserves = zero_vector(matvec(P_at(F(0)), native_u0))

    full_green_intertwines = all(
        zero_vector(
            vector_sub(matvec(observation_at(x), native_green_at(x)), observed_green_at(x))
        )
        and zero_vector(
            vector_sub(matvec(observation_at(x), native_source_at(x)), observed_source_at(x))
        )
        for x in SAMPLES
    )
    native_projected_green_commutes = all(
        zero_vector(
            vector_sub(
                matvec(P_at(x), native_green_at(x)), projected_native_green_at(x)
            )
        )
        for x in SAMPLES
    )
    observed_projected_green_commutes = all(
        zero_vector(
            vector_sub(
                matvec(P_OBS, observed_green_at(x)), projected_observed_green_at(x)
            )
        )
        for x in SAMPLES
    )
    projected_green_intertwines = all(
        zero_vector(
            vector_sub(
                matvec(observation_at(x), projected_native_green_at(x)),
                projected_observed_green_at(x),
            )
        )
        for x in SAMPLES
    )
    return {
        "observation_inverse": observation_inverse,
        "lift_inverse": lift_inverse,
        "gram_transport": gram_transport,
        "observation_variable": observation_at(F(0)) != observation_at(F(1)),
        "lift_variable": lift_at(F(0)) != lift_at(F(1)),
        "observation_covariant_intertwiner": observation_covariant,
        "lift_covariant_intertwiner": lift_covariant,
        "native_projector_idempotent": native_projector_idempotent,
        "observed_projector_idempotent": observed_projector_idempotent,
        "native_projector_self_adjoint": native_projector_self_adjoint,
        "observed_projector_h_self_adjoint": observed_projector_h_self_adjoint,
        "observation_projector_intertwines": observation_projector_intertwines,
        "lift_projector_intertwines": lift_projector_intertwines,
        "native_projector_parallel": native_projector_parallel,
        "observed_projector_parallel": observed_projector_parallel,
        "incoming_boundary_maps": boundary_maps,
        "incoming_boundary_inverse": boundary_inverse,
        "incoming_boundary_projection_preserves": boundary_projection_preserves,
        "full_green_intertwines": full_green_intertwines,
        "native_projected_green_commutes": native_projected_green_commutes,
        "observed_projected_green_commutes": observed_projected_green_commutes,
        "projected_green_intertwines": projected_green_intertwines,
    }


def demo() -> dict:
    checks = exact_checks()
    assert all(checks.values())
    return {
        "schema_version": "1.0",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "compressed_h640_input": {
            "source_result_ref": "lab/process/selected-k77-h640-observation-pullback-bv-typing.json",
            "ambient_rank": 1920,
            "native_h640_rank": 640,
            "observed_rank": 640,
            "observation_restricts_isomorphically": True,
            "full_h640_matrix_serialized": False,
            "full_1920_matrix_serialized": False,
            "fixture_status": "conditional rank-two rational representative of the inherited two-carrier isomorphism fact",
        },
        "two_carrier_fixture": {
            "native_carrier": "H=Q^2 with standard Gram matrix",
            "observed_carrier": "O=Q^2 with Gram matrix F_obs^{-T}F_obs^{-1}",
            "constant_observation_frame": [["1", "1"], ["0", "1"]],
            "constant_inverse_frame": [["1", "-1"], ["0", "1"]],
            "observed_gram": [["1", "-1"], ["-1", "2"]],
            "observation": "J(t)=F_obs U(t)^T",
            "lift": "L(t)=U(t) F_obs^{-1}",
            "exact_laws": checks,
        },
        "covariant_intertwiner": {
            "native_differential": "D_H=d/dt+A(t)",
            "observed_differential": "D_O=d/dt",
            "observation_law": "J'=J A, hence D_O J=J D_H",
            "lift_law": "L'+A L=0, hence D_H L=L D_O",
        },
        "projector_descent": {
            "native_projector": "P_H(t)=U(t) diag(1,0) U(t)^T",
            "observed_projector": [["1", "-1"], ["0", "0"]],
            "intertwining": "J P_H=P_O J and P_H L=L P_O",
            "parallel_on_both_carriers": True,
            "observed_projector_is_self_adjoint_for_observed_gram": True,
        },
        "incoming_boundary_and_green": {
            "native_domain": "u in H1([0,1],H) with u(0)=0",
            "observed_domain": "x in H1([0,1],O) with x(0)=0",
            "boundary_square": "J(0) maps the native zero trace bijectively to the observed zero trace",
            "native_green": "G_H f(t)=U(t) integral_0^t U(s)^T f(s) ds",
            "observed_green": "G_O g(t)=integral_0^t g(s) ds",
            "green_square": "J G_H=G_O J",
            "projected_green_square": "J P_H G_H=P_O G_O J=G_O P_O J",
        },
        "decision": {
            "conditional_two_carrier_covariant_intertwiner_constructed": True,
            "actual_full_h640_or_1920_intertwiner_constructed": False,
            "physical_bv_bfv_observation_constructed": False,
            "source_or_ledger_effect": "none",
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
