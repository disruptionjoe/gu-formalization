#!/usr/bin/env python3
"""K433 exact cross-carrier boundary-holonomy intertwiner classification."""

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
    matmul,
    sub,
    transpose,
    zero_matrix,
)


J = [[F(0), F(-1)], [F(1), F(0)]]
NEG_I2 = [[F(-1), F(0)], [F(0), F(-1)]]
H = [[F(1), F(0)], [F(0), F(-1)]]
ZERO2 = [[F(0), F(0)], [F(0), F(0)]]


def matrix_strings(matrix):
    return [[str(entry) for entry in row] for row in matrix]


def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def rational_rank(matrix):
    rows = [list(row) for row in matrix]
    if not rows:
        return 0
    row = 0
    for column in range(len(rows[0])):
        pivot = next((candidate for candidate in range(row, len(rows)) if rows[candidate][column] != 0), None)
        if pivot is None:
            continue
        rows[row], rows[pivot] = rows[pivot], rows[row]
        scale = rows[row][column]
        rows[row] = [entry / scale for entry in rows[row]]
        for candidate in range(len(rows)):
            if candidate == row:
                continue
            multiple = rows[candidate][column]
            if multiple != 0:
                rows[candidate] = [
                    entry - multiple * pivot_entry
                    for entry, pivot_entry in zip(rows[candidate], rows[row], strict=True)
                ]
        row += 1
        if row == len(rows):
            break
    return row


def linear_intertwiner_dimension(source_relative, target_relative):
    basis = [
        [[F(1), F(0)], [F(0), F(0)]],
        [[F(0), F(1)], [F(0), F(0)]],
        [[F(0), F(0)], [F(1), F(0)]],
        [[F(0), F(0)], [F(0), F(1)]],
    ]
    columns = []
    for candidate in basis:
        defect = sub(matmul(candidate, source_relative), matmul(target_relative, candidate))
        columns.append([defect[0][0], defect[0][1], defect[1][0], defect[1][1]])
    constraint_matrix = [list(row) for row in zip(*columns, strict=True)]
    return 4 - rational_rank(constraint_matrix)


def B_at(x: F):
    """Parallel map E_x -> F_x, with flat target transport and source U."""
    return matmul(H, transpose(U_at(x)))


def B_prime_at(x: F):
    return matmul(H, transpose(U_prime_at(x)))


def bulk_intertwiner_defect_at(x: F):
    # A_F=0, so D_F(Bu)-B D_Eu=(B'-B A_E)u.
    return sub(B_prime_at(x), matmul(B_at(x), A_at(x)))


def relative_source(twist):
    return matmul(transpose(U_at(F(1))), twist)


def relative_target(twist):
    # The target connection is flat, so V(0)=V(1)=I.
    return twist


def boundary_case(name: str, source_twist, target_twist):
    source_relative = relative_source(source_twist)
    target_relative = relative_target(target_twist)
    reduced_defect = sub(matmul(H, source_relative), matmul(target_relative, H))
    endpoint_defect = sub(matmul(B_at(F(1)), source_twist), matmul(target_twist, B_at(F(0))))
    assert reduced_defect == endpoint_defect
    return {
        "name": name,
        "source_endpoint_twist": matrix_strings(source_twist),
        "target_endpoint_twist": matrix_strings(target_twist),
        "source_relative_holonomy": matrix_strings(source_relative),
        "target_relative_holonomy": matrix_strings(target_relative),
        "chosen_map_boundary_defect": matrix_strings(endpoint_defect),
        "chosen_map_boundary_compatible": zero_matrix(endpoint_defect),
        "chosen_map_invertible": det2(H) != 0,
        "parallel_boundary_intertwiner_space_dimension": linear_intertwiner_dimension(
            source_relative, target_relative
        ),
    }


def demo() -> dict:
    bulk_parallel = all(zero_matrix(bulk_intertwiner_defect_at(x)) for x in SAMPLES)
    matched_monodromy = boundary_case("monodromy_to_flat_matched", J, I2)
    matched_conjugate = boundary_case("conjugacy_matched", I2, J)
    mismatched = boundary_case("opposite_scalar_relative_holonomy", J, NEG_I2)
    assert bulk_parallel
    assert matched_monodromy["chosen_map_boundary_compatible"] is True
    assert matched_conjugate["chosen_map_boundary_compatible"] is True
    assert mismatched["chosen_map_boundary_compatible"] is False
    assert mismatched["parallel_boundary_intertwiner_space_dimension"] == 0
    return {
        "schema_version": "1.0",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "native_to_observed",
        "cross_carrier_theorem": {
            "bulk_parallel_form": "B(t)=V(t) C U(t)^T",
            "relative_source_holonomy": "S_E=U(1)^T R_E U(0)",
            "relative_target_holonomy": "S_F=V(1)^T R_F V(0)",
            "boundary_criterion": "B maps Dom(D_E,R_E) to Dom(D_F,R_F) iff C S_E=S_F C",
            "invertible_criterion": "an invertible parallel boundary intertwiner exists iff S_E and S_F are conjugate",
            "obstruction": "if the relative holonomies have coprime minimal polynomials then every parallel boundary intertwiner is zero",
        },
        "exact_bulk_fixture": {
            "source_transport": "U(t)=1/(1+t^2)*[[1-t^2,-2t],[2t,1-t^2]]",
            "source_connection": "A_E(t)=-U'(t)U(t)^T",
            "target_transport": "V(t)=I",
            "target_connection": "A_F(t)=0",
            "trivialized_map": matrix_strings(H),
            "map": "B(t)=H U(t)^T",
            "map_invertible": det2(H) != 0,
            "bulk_covariant_intertwining_exact": bulk_parallel,
        },
        "exact_cases": {
            "matched_monodromy": matched_monodromy,
            "matched_conjugate": matched_conjugate,
            "mismatched_opposite_scalar": mismatched,
        },
        "scoped_obstruction": {
            "source_relative_holonomy": "I",
            "target_relative_holonomy": "-I",
            "equation": "C I=(-I) C forces 2C=0",
            "only_parallel_boundary_intertwiner": "zero map",
            "bulk_intertwiner_still_exists": bulk_parallel,
            "obstruction_is_boundary_relative_not_bulk": True,
        },
        "decision": {
            "cross_carrier_boundary_compatibility_classified": True,
            "endpoint_twists_alone_are_not_the_invariant": True,
            "relative_holonomy_conjugacy_controls_invertible_descent": True,
            "mismatched_case_blocks_every_nonzero_parallel_boundary_map": True,
            "actual_corrected_observation_carrier_identified": False,
            "physical_boundary_projector_or_bfv_map_constructed": False,
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
