#!/usr/bin/env python3
"""K429 variable covariant derivative with a closed incoming Green domain."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F


I2 = [[F(1), F(0)], [F(0), F(1)]]
SAMPLES = [F(0), F(1, 5), F(1, 2), F(3, 4), F(1)]


def transpose(matrix):
    return [list(row) for row in zip(*matrix, strict=True)]


def matmul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def matvec(matrix, vector):
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def add(left, right):
    return [[left[i][j] + right[i][j] for j in range(len(left[0]))] for i in range(len(left))]


def sub(left, right):
    return [[left[i][j] - right[i][j] for j in range(len(left[0]))] for i in range(len(left))]


def vector_add(left, right):
    return [a + b for a, b in zip(left, right, strict=True)]


def vector_sub(left, right):
    return [a - b for a, b in zip(left, right, strict=True)]


def zero_matrix(matrix) -> bool:
    return all(entry == 0 for row in matrix for entry in row)


def zero_vector(vector) -> bool:
    return all(entry == 0 for entry in vector)


def U_at(x: F):
    den = 1 + x * x
    c = (1 - x * x) / den
    s = 2 * x / den
    return [[c, -s], [s, c]]


def U_prime_at(x: F):
    den2 = (1 + x * x) ** 2
    cp = -4 * x / den2
    sp = 2 * (1 - x * x) / den2
    return [[cp, -sp], [sp, cp]]


def A_at(x: F):
    a = 2 / (1 + x * x)
    return [[F(0), a], [-a, F(0)]]


def v_at(x: F):
    return [x * x + x, x**3 - 2 * x]


def v_prime_at(x: F):
    return [2 * x + 1, 3 * x * x - 2]


def g_at(x: F):
    return [1 + x, 1 - x]


def primitive_g_at(x: F):
    return [x + x * x / 2, x - x * x / 2]


def verify_conjugation_at(x: F) -> bool:
    u_prime = vector_add(matvec(U_prime_at(x), v_at(x)), matvec(U_at(x), v_prime_at(x)))
    covariant = vector_add(u_prime, matvec(A_at(x), matvec(U_at(x), v_at(x))))
    return zero_vector(vector_sub(covariant, matvec(U_at(x), v_prime_at(x))))


def verify_green_at(x: F) -> bool:
    primitive = primitive_g_at(x)
    u_prime = vector_add(matvec(U_prime_at(x), primitive), matvec(U_at(x), g_at(x)))
    covariant = vector_add(u_prime, matvec(A_at(x), matvec(U_at(x), primitive)))
    return zero_vector(vector_sub(covariant, matvec(U_at(x), g_at(x))))


def verify_fixture() -> dict[str, bool]:
    orthogonal = all(zero_matrix(sub(matmul(transpose(U_at(x)), U_at(x)), I2)) for x in SAMPLES)
    skew = all(zero_matrix(add(transpose(A_at(x)), A_at(x))) for x in SAMPLES)
    transport_ode = all(zero_matrix(add(U_prime_at(x), matmul(A_at(x), U_at(x)))) for x in SAMPLES)
    return {
        "transport_is_orthogonal": orthogonal,
        "connection_is_skew": skew,
        "connection_is_variable": A_at(F(0)) != A_at(F(1)),
        "transport_ode_exact": transport_ode,
        "gauge_conjugation": all(verify_conjugation_at(x) for x in SAMPLES),
        "incoming_green_right_inverse": all(verify_green_at(x) for x in SAMPLES),
        "incoming_trace_zero": zero_vector(matvec(U_at(F(0)), primitive_g_at(F(0)))),
        "endpoint_transport": U_at(F(0)) == I2 and U_at(F(1)) == [[F(0), F(-1)], [F(1), F(0)]],
    }


def demo() -> dict:
    checks = verify_fixture()
    assert all(checks.values())
    return {
        "schema_version": "1.0",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "native_to_native",
        "conditional_action_reduction": {
            "carrier": "real rank-two subbundle over [0,1]",
            "covariant_differential": "D_A=d/dt+A(t)",
            "transport": "U(t)=1/(1+t^2)*[[1-t^2,-2t],[2t,1-t^2]]",
            "connection": "A(t)=-U'(t)U(t)^T=[[0,2/(1+t^2)],[-2/(1+t^2),0]]",
            "source_status": "source-admitted D_B covariant-differential form; rank-two reduction and coefficient are conditional repository choices",
        },
        "exact_fixture": checks,
        "incoming_domain": {
            "definition": "Dom(D_in)={u in H1([0,1],R2):u(0)=0}",
            "closed_dense_domain": True,
            "range": "L2([0,1],R2)",
            "kernel_dimension": 0,
            "cokernel_dimension": 0,
            "bijective": True,
        },
        "green_operator": {
            "formula": "(G_in f)(t)=U(t)*integral_0^t U(s)^T f(s) ds",
            "two_sided_inverse_on_domain": True,
            "l2_operator_norm": "2/pi",
            "bounded_l2_to_h1": True,
            "derivative_bound": "||u'||_2 <= (1+4/pi)||f||_2",
        },
        "pairing": {
            "bulk": "standard real L2 pairing preserved by orthogonal U",
            "green_identity": "<D_A u,v>+<u,D_A v>=[u(t).v(t)]_0^1",
            "formal_skew_adjoint": True,
            "adjoint_domain": "Dom(D_out)={v in H1:v(1)=0}",
            "outgoing_green": "(G_out f)(t)=-U(t)*integral_t^1 U(s)^T f(s) ds",
            "adjoint_relation": "G_in^*=-G_out",
        },
        "decision": {
            "variable_connection_forces_nonclosed_range": False,
            "explicit_boundary_condition_can_close_range": True,
            "bounded_green_inverse_exists": True,
            "physical_k77_domain_constructed": False,
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
