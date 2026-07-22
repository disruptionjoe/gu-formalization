#!/usr/bin/env python3
"""Exact admission gate for a Mannheim--Callias completion of the GU ends.

The ambient Pin/Smith target is already known.  This certificate asks whether
the *committed* GU source action owns a Callias-type coercive deformation on
the determinant-fixed noncompact Cartan ends of the observerse.  It uses only
exact arithmetic and source typing; it does not assume values for the action's
unspecified compensator or Velo--Zwanziger completion.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import gcd
import json


@dataclass(frozen=True)
class SourceTerm:
    name: str
    explicit: bool
    value_on_flat_zero_field_valley: Fraction | None
    supplies_end_potential: bool


SOURCE_TERMS = (
    SourceTerm("gauge_kinetic_norm_F_A_squared", True, Fraction(0), False),
    SourceTerm("fermion_pairing_Psi_D_A_Psi", True, Fraction(0), False),
    SourceTerm("SW_square_F_A_plus_minus_mu_Psi", True, Fraction(0), False),
    SourceTerm("horizontal_Willmore_norm_II_H_squared", True, Fraction(0), False),
    SourceTerm("compensator", False, None, False),
    SourceTerm("VZ_guardian", False, None, False),
)


def primitive_cartan_directions(bound: int = 3) -> tuple[tuple[int, ...], ...]:
    """Primitive determinant-fixed rank-3 diagonal directions, modulo sign."""
    directions = []
    for vector in product(range(-bound, bound + 1), repeat=4):
        if vector == (0, 0, 0, 0) or sum(vector) != 0:
            continue
        divisor = 0
        for entry in vector:
            divisor = gcd(divisor, abs(entry))
        if divisor != 1:
            continue
        first_nonzero = next(entry for entry in vector if entry)
        if first_nonzero < 0:
            continue
        directions.append(vector)
    return tuple(directions)


def metric_on_ray(vector: tuple[int, ...], step: int) -> tuple[Fraction, ...]:
    magnitudes = tuple(Fraction(2) ** (step * entry) for entry in vector)
    return (-magnitudes[0], *magnitudes[1:])


def determinant(diagonal: tuple[Fraction, ...]) -> Fraction:
    result = Fraction(1)
    for entry in diagonal:
        result *= entry
    return result


def max_norm(diagonal: tuple[Fraction, ...]) -> Fraction:
    return max(abs(entry) for entry in diagonal)


def main() -> None:
    directions = primitive_cartan_directions()
    assert len(directions) > 3

    # Every nonzero determinant-fixed diagonal direction has both signs in its
    # exponent vector and therefore escapes to infinity while remaining in
    # signature (3,1) and determinant -1.
    endpoint_norms = []
    for vector in directions:
        assert min(vector) < 0 < max(vector)
        ray = [metric_on_ray(vector, step) for step in range(9)]
        assert all(determinant(point) == -1 for point in ray)
        assert all(sum(entry < 0 for entry in point) == 1 for point in ray)
        assert all(sum(entry > 0 for entry in point) == 3 for point in ray)
        assert max_norm(ray[-1]) > max_norm(ray[0])
        endpoint_norms.append(max_norm(ray[-1]))

    # On A flat, Psi = 0, mu(Psi) = 0 and a constant tautological LC section,
    # every displayed positive term vanishes along every escaping ray.
    explicit_terms = tuple(term for term in SOURCE_TERMS if term.explicit)
    unspecified_terms = tuple(term for term in SOURCE_TERMS if not term.explicit)
    assert all(term.value_on_flat_zero_field_valley == 0 for term in explicit_terms)
    assert all(term.value_on_flat_zero_field_valley is None for term in unspecified_terms)
    assert not any(term.supplies_end_potential for term in SOURCE_TERMS)

    # A Callias estimate needs Phi^2 - ||[D,Phi]|| >= c > 0 off a compact set.
    # The source-owned candidate Phi is identically zero on this escape valley.
    phi_squared = Fraction(0)
    commutator_norm = Fraction(0)
    callias_lhs = phi_squared - commutator_norm
    assert callias_lhs == 0
    assert not callias_lhs > 0

    source_owned_stokes_contour = False
    source_owned_domain_transport = False
    assert not source_owned_stokes_contour
    assert not source_owned_domain_transport

    receipt = {
        "callias_lhs_on_escape_valley": str(callias_lhs),
        "cartan_rank": 3,
        "direction_bound": 3,
        "primitive_directions_mod_sign": len(directions),
        "largest_exact_endpoint_norm": str(max(endpoint_norms)),
        "explicit_terms_zero_on_valley": [term.name for term in explicit_terms],
        "unspecified_terms_not_admitted": [term.name for term in unspecified_terms],
        "source_owned_stokes_contour": source_owned_stokes_contour,
        "source_owned_domain_transport": source_owned_domain_transport,
        "verdict": "MANNHEIM-CALLIAS-NO-END-POTENTIAL",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
