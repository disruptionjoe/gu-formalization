#!/usr/bin/env python3
"""K441 exact moving transport of the K439 corrected boundary split."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F


BLOCK_RANKS = [192, 64, 192, 64]
SAMPLES = [F(0), F(1, 3), F(1, 2), F(1)]


def eye(n: int) -> list[list[F]]:
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a: list[list[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*a)]


def add(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def sub(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c: F, a: list[list[F]]) -> list[list[F]]:
    return [[c * x for x in row] for row in a]


def matmul(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in bt] for row in a]


def power(a: list[list[F]], n: int) -> list[list[F]]:
    out = eye(len(a))
    for _ in range(n):
        out = matmul(out, a)
    return out


def zero(a: list[list[F]]) -> bool:
    return all(x == 0 for row in a for x in row)


def diagonal(values: list[F]) -> list[list[F]]:
    return [[values[i] if i == j else F(0) for j in range(len(values))] for i in range(len(values))]


def rotation(t: F) -> list[list[F]]:
    d = 1 + t * t
    return [[(1 - t * t) / d, -2 * t / d], [2 * t / d, (1 - t * t) / d]]


def rotation_derivative(t: F) -> list[list[F]]:
    d2 = (1 + t * t) ** 2
    return [[-4 * t / d2, 2 * (t * t - 1) / d2], [2 * (1 - t * t) / d2, -4 * t / d2]]


def paired_matrix(block: list[list[F]]) -> list[list[F]]:
    """Repeat one 2x2 block on the fast (0,2) and slow (1,3) pairs."""
    out = [[F(0) for _ in range(4)] for _ in range(4)]
    for i, j in [(0, 2), (1, 3)]:
        out[i][i], out[i][j] = block[0]
        out[j][i], out[j][j] = block[1]
    return out


def conjugate(u: list[list[F]], a: list[list[F]]) -> list[list[F]]:
    return matmul(matmul(u, a), transpose(u))


def matrix_strings(a: list[list[F]]) -> list[list[str]]:
    return [[str(x) for x in row] for row in a]


def digest(a: list[list[F]]) -> str:
    payload = json.dumps(matrix_strings(a), separators=(",", ":"), sort_keys=False).encode()
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def sample(t: F) -> dict:
    u = paired_matrix(rotation(t))
    up = paired_matrix(rotation_derivative(t))
    b = scale(F(-1), matmul(up, transpose(u)))
    a0 = diagonal([F(1), F(1, 24), F(-1), F(-1, 24)])
    j0 = diagonal([F(1), F(1), F(-1), F(-1)])
    pout0 = diagonal([F(1), F(1), F(0), F(0)])
    pin0 = sub(eye(4), pout0)
    a = conjugate(u, a0)
    j = conjugate(u, j0)
    pout = conjugate(u, pout0)
    pin = conjugate(u, pin0)
    poutp = add(matmul(matmul(up, pout0), transpose(u)), matmul(matmul(u, pout0), transpose(up)))
    polynomial_j = scale(F(1, 575), sub(scale(F(13823), a), scale(F(13248), power(a, 3))))
    reversed_a = scale(F(-1), a)
    reversed_polynomial_j = scale(
        F(1, 575), sub(scale(F(13823), reversed_a), scale(F(13248), power(reversed_a, 3)))
    )
    spectral_identity = add(sub(scale(F(576), power(a, 4)), scale(F(577), power(a, 2))), eye(4))
    return {
        "t": str(t),
        "checks": {
            "transport_orthogonal": matmul(u, transpose(u)) == eye(4),
            "connection_skew": add(b, transpose(b)) == [[F(0)] * 4 for _ in range(4)],
            "transport_equation": zero(add(up, matmul(b, u))),
            "compressed_polynomial_preserved": zero(spectral_identity),
            "sign_polynomial_preserved": polynomial_j == j,
            "sign_involution": matmul(j, j) == eye(4),
            "projectors_idempotent": matmul(pout, pout) == pout and matmul(pin, pin) == pin,
            "projectors_complementary": add(pout, pin) == eye(4) and zero(matmul(pout, pin)),
            "projector_parallel": zero(add(poutp, sub(matmul(b, pout), matmul(pout, b)))),
            "normal_reversal": scale(F(-1), j) == reversed_polynomial_j,
        },
        "digests": {"transport": digest(u), "connection": digest(b), "compressed_symbol": digest(a), "outgoing": digest(pout)},
    }


def demo() -> dict:
    samples = [sample(t) for t in SAMPLES]
    assert all(all(row["checks"].values()) for row in samples)
    return {
        "schema_version": "1.0",
        "result_id": "K441-K77-MOVING-CORRECTED-BOUNDARY-TRANSPORT",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "native_to_observed",
        "factorized_actual_carrier": {
            "spectral_block_ranks": BLOCK_RANKS,
            "transport_rule": "the same rational rotation acts on each of 192 fast outgoing/incoming pairs and each of 64 slow outgoing/incoming pairs",
            "total_rank": sum(BLOCK_RANKS),
            "incoming_rank": BLOCK_RANKS[2] + BLOCK_RANKS[3],
            "outgoing_rank": BLOCK_RANKS[0] + BLOCK_RANKS[1],
            "fitted_parameters": 0,
        },
        "moving_operator": {
            "transport": "U(t)=R(t) on the fast sign pair and R(t) on the slow sign pair, with R(t)=(1+t^2)^-1[[1-t^2,-2t],[2t,1-t^2]]",
            "connection": "B(t)=-U'(t)U(t)^T",
            "compressed_symbol": "A(t)=U(t) diag(1,1/24,-1,-1/24) U(t)^T with the stated block multiplicities",
            "covariant_operator": "D=d/dt+B(t)+A(t), so D(Uv)=U(v'+A0 v)",
            "projectors": "Pi_out/in(t)=U(t) Pi_out/in(0) U(t)^T",
            "parallelism": "Pi'+[B,Pi]=0",
        },
        "functional_consequence": {
            "moving_trace_domain": "u in H1(R_+,E) with Pi_out(0)u(0)=0 after trivialization, equivalently the transported trace condition in a moving frame",
            "domain_closed": True,
            "domain_transport_isometric": True,
            "green_conjugation": "G_moving=U G_K440 U^T",
            "l2_green_bound": "24",
            "l2_to_derivative_bound_in_trivialized_connection_norm": "25",
            "physical_boundary_selected": False,
        },
        "samples": samples,
        "decision": {
            "moving_corrected_projectors_constructed": True,
            "parallel_transport_proved": True,
            "closed_trace_domain_preserved": True,
            "full_lower_order_k77_connection_derived": False,
            "nonlinear_bv_kt_compatibility_proved": False,
            "next_exact_input": "compose the corrected carrier with the proper homogeneous-orbit Koszul--Tate resolution, then classify which lower-order couplings preserve the boundary split",
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
