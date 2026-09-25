#!/usr/bin/env python3
"""K451 exact physical-Gram-relative audit of the K447 finite defects."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction

from k447_k152_charge_sector_galerkin_defect_census import K163, defect, qstr


EXPECTED_RADII = {
    (0, 0): Fraction(23118267391392752342114377141, 146346923226707931087360000000),
    (1, 0): Fraction(565919717438264971286768741333, 5268489236161485519144960000000),
    (0, 1): Fraction(565919717438264971286768741333, 5268489236161485519144960000000),
}


def rational(matrix):
    if any(entry.b for row in matrix for entry in row):
        raise AssertionError("physical Gram audit unexpectedly left Q")
    return [[entry.a for entry in row] for row in matrix]


def physical_gram(charge: tuple[int, int]):
    root_two = K163.Q2(Fraction(0), Fraction(1))
    packet = K163.regular_pullback([2], [root_two], charge, 4)
    _, free, _, cstar = K163.charge_components([2], [root_two], charge)
    unit = K163.identity(len(free))
    shifted = K163.add(free, K163.scale(4, unit))
    shifted_inverse = K163.diagonal([K163.Q2.of(1) / shifted[i][i] for i in range(len(unit))])
    g = K163.scale(-1, K163.matmul(shifted_inverse, cstar))
    s = K163.inverse(K163.add(unit, K163.scale(-1, g)))
    weights = []
    for state in packet["states"]:
        weight = K163.Q2.of(1)
        for _ in range(K163.bath_particles(state, 1)):
            weight *= root_two
        weights.append(weight)
    basis = K163.diagonal(weights)
    return K163.matmul(basis, K163.matmul(K163.transpose(s), K163.matmul(s, basis)))


def ldl_positive(matrix: list[list[Fraction]]) -> bool:
    size = len(matrix); lower = [[Fraction(i == j) for j in range(size)] for i in range(size)]; pivots = []
    for i in range(size):
        pivot = matrix[i][i] - sum(lower[i][k] ** 2 * pivots[k] for k in range(i))
        if pivot <= 0: return False
        pivots.append(pivot)
        for j in range(i + 1, size):
            lower[j][i] = (matrix[j][i] - sum(lower[j][k] * lower[i][k] * pivots[k] for k in range(i))) / pivot
    return True


def sector(charge: tuple[int, int]) -> dict:
    d_q2 = defect(charge, "regular"); m_q2 = physical_gram(charge)
    d, gram = rational(d_q2), rational(m_q2)
    relative = rational(K163.matmul(K163.inverse(m_q2), d_q2))
    row_sums = [sum(abs(entry) for entry in row) for row in relative]
    beta = max(row_sums)
    if beta != EXPECTED_RADII[charge]: raise AssertionError("physical-Gram radius drifted")
    plus = [[beta * gram[i][j] + d[i][j] for j in range(len(d))] for i in range(len(d))]
    minus = [[beta * gram[i][j] - d[i][j] for j in range(len(d))] for i in range(len(d))]
    return {
        "charge": list(charge), "dimension": len(d),
        "physical_Gram_positive_definite": ldl_positive(gram),
        "relative_operator": "M^-1 D",
        "relative_operator_entries_rational": True,
        "induced_infinity_radius": qstr(beta),
        "radius_row": row_sums.index(beta),
        "two_sided_form_bound": "-beta*M <= D <= beta*M",
        "plus_certificate_positive_definite": ldl_positive(plus),
        "minus_certificate_positive_definite": ldl_positive(minus),
        "defect_nonzero": any(entry for row in d for entry in row),
    }


def demo() -> dict:
    sectors = [sector(charge) for charge in ((0, 0), (1, 0), (0, 1))]
    return {
        "schema_version": "1.0", "result_id": "K451-K152-PHYSICAL-GRAM-INDEPENDENT-DEFECT",
        "classification": "INTERNAL_STRUCTURAL_ONLY", "direction": "observed_to_native",
        "sectors": sectors,
        "decision": {
            "finite_independent_rebuild_has_physical_Gram_relative_bound": all(row["plus_certificate_positive_definite"] and row["minus_certificate_positive_definite"] for row in sectors),
            "q10_q01_radii_equal": sectors[1]["induced_infinity_radius"] == sectors[2]["induced_infinity_radius"],
            "bound_is_cofinal_decay_estimate": False,
            "bound_applies_to_fixed_limiting_form_restriction": False,
            "native_K152_interval_emitted": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--demo", action="store_true"); args = parser.parse_args()
    if not args.demo: parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True)); return 0


if __name__ == "__main__": raise SystemExit(main())
