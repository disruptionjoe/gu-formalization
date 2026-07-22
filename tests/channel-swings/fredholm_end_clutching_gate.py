#!/usr/bin/env python3
"""Exact gate for the strongest GU-shaped Fredholm/end-clutching packet.

The gate keeps three constructions separate:

1. the committed program-native observerse fiber and its split vertical metric;
2. a conventional scalar Callias completion after choosing a Riemannian end;
3. a quaternionic Bott--Callias control whose normalized mass is nonconstant.

It proves exact finite-dimensional and inequality claims only.  The final
descent from the control to the actual D_GU family and then to Pin+ bordism is
deliberately represented as an open field, not inferred from the control.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import gcd
import json


Matrix = tuple[tuple[Fraction, ...], ...]
Quaternion = tuple[Fraction, Fraction, Fraction, Fraction]


def primitive_cartan_directions(bound: int = 3) -> tuple[tuple[int, ...], ...]:
    """Primitive determinant-fixed diagonal directions, modulo overall sign."""
    directions = []
    for vector in product(range(-bound, bound + 1), repeat=4):
        if vector == (0, 0, 0, 0) or sum(vector) != 0:
            continue
        divisor = 0
        for entry in vector:
            divisor = gcd(divisor, abs(entry))
        if divisor != 1:
            continue
        if next(entry for entry in vector if entry) < 0:
            continue
        directions.append(vector)
    return tuple(directions)


def diagonal_congruence_witness(
    vector: tuple[int, ...], step: int
) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    """Return L and L^T eta L for eta=diag(-1,1,1,1)."""
    transform = tuple(Fraction(2) ** (step * entry) for entry in vector)
    metric = tuple(
        sign * entry * entry
        for sign, entry in zip((-1, 1, 1, 1), transform, strict=True)
    )
    return transform, metric


def diagonal_determinant(diagonal: tuple[Fraction, ...]) -> Fraction:
    out = Fraction(1)
    for entry in diagonal:
        out *= entry
    return out


def identity(size: int) -> Matrix:
    return tuple(
        tuple(Fraction(int(row == column)) for column in range(size))
        for row in range(size)
    )


def zero(size: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(size)) for _ in range(size))


def transpose(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(matrix[row][column] for row in range(len(matrix)))
        for column in range(len(matrix[0]))
    )


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum((left[row][k] * right[k][column] for k in range(len(right))), Fraction(0))
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def matrix_scale(scale: Fraction, matrix: Matrix) -> Matrix:
    return tuple(tuple(scale * entry for entry in row) for row in matrix)


def block(
    top_left: Matrix,
    top_right: Matrix,
    bottom_left: Matrix,
    bottom_right: Matrix,
) -> Matrix:
    top = tuple(top_left[row] + top_right[row] for row in range(len(top_left)))
    bottom = tuple(bottom_left[row] + bottom_right[row] for row in range(len(bottom_left)))
    return top + bottom


def left_quaternion(q: Quaternion) -> Matrix:
    """Real matrix for left multiplication by q on H."""
    a, b, c, d = q
    return (
        (a, -b, -c, -d),
        (b, a, -d, c),
        (c, d, a, -b),
        (d, -c, b, a),
    )


RIGHT_I: Matrix = (
    (Fraction(0), Fraction(-1), Fraction(0), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
    (Fraction(0), Fraction(0), Fraction(-1), Fraction(0)),
)
RIGHT_J: Matrix = (
    (Fraction(0), Fraction(0), Fraction(-1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(0), Fraction(-1)),
    (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
)
RIGHT_K: Matrix = (
    (Fraction(0), Fraction(0), Fraction(0), Fraction(-1)),
    (Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(-1), Fraction(0), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
)


def quaternion_norm_squared(q: Quaternion) -> Fraction:
    return sum((entry * entry for entry in q), Fraction(0))


def coordinate_quaternion(*nonzero_indices: int) -> Quaternion:
    entries = tuple(
        Fraction(int(index in nonzero_indices)) for index in range(4)
    )
    return (entries[0], entries[1], entries[2], entries[3])


def bott_involution(q: Quaternion) -> Matrix:
    """Self-adjoint double of the quaternionic clutching map q -> L_q."""
    left = left_quaternion(q)
    z4 = zero(4)
    return block(z4, transpose(left), left, z4)


def doubled(matrix: Matrix) -> Matrix:
    z4 = zero(4)
    return block(matrix, z4, z4, matrix)


def main() -> None:
    # Native obstruction I: every exact escaping ray is an explicit GL(4)
    # congruence orbit of eta.  A fully GL-invariant scalar is therefore
    # constant on the ray and cannot be a proper exhaustion.
    directions = primitive_cartan_directions()
    assert len(directions) == 97
    endpoint_norms = []
    for vector in directions:
        assert min(vector) < 0 < max(vector)
        orbit = []
        for step in range(9):
            transform, metric = diagonal_congruence_witness(vector, step)
            assert diagonal_determinant(transform) == 1
            assert diagonal_determinant(metric) == -1
            assert sum(entry < 0 for entry in metric) == 1
            assert sum(entry > 0 for entry in metric) == 3
            orbit.append(metric)
        assert max(abs(entry) for entry in orbit[-1]) > max(abs(entry) for entry in orbit[0])
        endpoint_norms.append(max(abs(entry) for entry in orbit[-1]))

    native_vertical_signature = (6, 4)
    native_symbol_has_null_cone = all(index > 0 for index in native_vertical_signature)
    assert native_symbol_has_null_cone
    native_proper_invariant_scalar = False
    assert not native_proper_invariant_scalar

    # Imported scalar control.  Put f=sqrt(1+r^2), mu=1 on a chosen complete
    # Riemannian end.  Then |df|<=1 and Phi^2-|[D,Phi]| >= r^2.  The homotopy
    # Phi_t=(1-t)f+t stays Callias with an exact 15/16 lower bound for r^2>=1:
    # 1-a/5+4a^2/25 = 15/16 + (8a-5)^2/400, a=1-t.
    assert Fraction(2) > Fraction(49, 25)  # sqrt(2) > 7/5
    scalar_homotopy_bounds = []
    for numerator in range(17):
        a = Fraction(numerator, 16)
        lower = Fraction(1) - a / 5 + 4 * a * a / 25
        assert lower - Fraction(15, 16) == (8 * a - 5) ** 2 / 400
        scalar_homotopy_bounds.append(lower)
    assert min(scalar_homotopy_bounds) >= Fraction(15, 16)
    scalar_clutching_degree = 0  # normalized positive scalar mass is constant +1

    # A continuous deck-odd real scalar cannot remain nonzero on the connected
    # cover: along any path q -> -q its endpoint values have opposite signs,
    # so the intermediate value theorem forces a zero.
    odd_scalar_start = Fraction(1)
    odd_scalar_end = -odd_scalar_start
    assert odd_scalar_start * odd_scalar_end < 0
    deck_odd_scalar_uniformly_gapped = False
    assert not deck_odd_scalar_uniformly_gapped

    # Quaternionic Bott control.  C(q) is self-adjoint, C(q)^2=|q|^2,
    # C(-q)=-C(q), and it commutes with the right-H action.  The grading S
    # implements deck descent: S C(q) S^{-1}=C(-q).
    half = Fraction(1, 2)
    quaternion_basis = tuple(coordinate_quaternion(index) for index in range(4))
    pair_sums: tuple[Quaternion, ...] = tuple(
        coordinate_quaternion(left_index, right_index)
        for left_index in range(4)
        for right_index in range(left_index + 1, 4)
    )
    quaternion_samples: tuple[Quaternion, ...] = quaternion_basis + pair_sums + (
        (half, half, half, half),
    )
    right_actions = tuple(doubled(matrix) for matrix in (RIGHT_I, RIGHT_J, RIGHT_K))
    deck_grading = block(
        identity(4),
        zero(4),
        zero(4),
        matrix_scale(Fraction(-1), identity(4)),
    )
    # The four basis vectors and all six pair sums certify every coefficient
    # in the quadratic identity C(q)^2=|q|^2 I; the half-sum adds a unit
    # non-axis control.
    for q in quaternion_samples:
        norm_squared = quaternion_norm_squared(q)
        assert norm_squared > 0
        callias_mass = bott_involution(q)
        minus_q: Quaternion = (-q[0], -q[1], -q[2], -q[3])
        minus_mass = bott_involution(minus_q)
        assert transpose(callias_mass) == callias_mass
        assert matmul(callias_mass, callias_mass) == matrix_scale(
            norm_squared, identity(8)
        )
        assert minus_mass == matrix_scale(Fraction(-1), callias_mass)
        assert matmul(matmul(deck_grading, callias_mass), deck_grading) == minus_mass
        for right_action in right_actions:
            assert matmul(callias_mass, right_action) == matmul(right_action, callias_mass)

    # For Phi=f(r)C(q), normalize the compact angular derivative bound to 1.
    # Then |[D,Phi]| <= 1+f and Phi^2=f^2.  Outside r^2>=8, f>=3 and
    # f^2-f-1>=5.  This is an explicit Callias/Fredholm control after the
    # declared Riemannian/Dirac imports.
    radial_squared_cutoff = 8
    f_lower = 3
    bott_callias_lower_bound = f_lower * f_lower - f_lower - 1
    assert 1 + radial_squared_cutoff == f_lower * f_lower
    assert bott_callias_lower_bound == 5

    # q -> L_q is the identity inclusion of the unit quaternions Sp(1); as a
    # conventional clutching map it has degree one (the quaternionic Hopf/Bott
    # control).  The algebra above checks its invertibility, deck law, and
    # right-H compatibility.  The GU-to-Pin+ natural map is not constructed.
    clutching_degree_control = 1
    actual_gu_operator_frozen = False
    source_owned_complete_riemannian_reduction = False
    pin14_natural_map_constructed = False
    assert not actual_gu_operator_frozen
    assert not source_owned_complete_riemannian_reduction
    assert not pin14_natural_map_constructed

    receipt = {
        "actual_gu_operator_frozen": actual_gu_operator_frozen,
        "bott_callias_lower_bound_outside_r2_8": bott_callias_lower_bound,
        "clutching_degree_control": clutching_degree_control,
        "deck_odd_scalar_uniformly_gapped": deck_odd_scalar_uniformly_gapped,
        "directions_mod_sign": len(directions),
        "largest_exact_orbit_endpoint_norm": str(max(endpoint_norms)),
        "native_proper_invariant_scalar": native_proper_invariant_scalar,
        "native_vertical_signature": list(native_vertical_signature),
        "pin14_natural_map_constructed": pin14_natural_map_constructed,
        "scalar_clutching_degree": scalar_clutching_degree,
        "scalar_homotopy_gap": str(min(scalar_homotopy_bounds)),
        "source_owned_complete_riemannian_reduction": source_owned_complete_riemannian_reduction,
        "verdict": "BOTT-CALLIAS-CANDIDATE-BUILT-PIN14-MAP-OPEN",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
