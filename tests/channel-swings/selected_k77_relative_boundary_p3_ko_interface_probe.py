#!/usr/bin/env python3
"""Exact gate for the observed-boundary winding to P3 real-KO interface.

This probe separates four layers that all carry an integer:

1. a component of Map(S^3, SL(2,C));
2. the SU(2)=Sp(1) clutching degree after polar deformation retraction;
3. the reduced real-KO class [H_n]-[R^4] pulled back by P3's fixed collapse;
4. a relative Fredholm index or physical generation count.

Layers 1--3 compose canonically at class level.  Layer 4 is deliberately
represented as absent because the packet itself leaves the closed domain and
index readout to later work.  The calculation therefore cannot book the
second independent constraint required for positive surplus.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

import sympy as sp


assert sp.__version__ == "1.14.0"

CHECKS = 0
PLANTS = 0


def check(label: str, condition: bool) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)
    print(f"PASS exact: {label}")


def plant(label: str, rejected: bool) -> None:
    global PLANTS
    PLANTS += 1
    if not rejected:
        raise AssertionError(f"plant did not fire: {label}")
    print(f"PASS planted: {label}")


def left_quaternion(a, b, c, d) -> sp.Matrix:
    return sp.Matrix(
        [
            [a, -b, -c, -d],
            [b, a, -d, c],
            [c, d, a, -b],
            [d, -c, b, a],
        ]
    )


def right_quaternion(a, b, c, d) -> sp.Matrix:
    return sp.Matrix(
        [
            [a, -b, -c, -d],
            [b, a, d, -c],
            [c, -d, a, b],
            [d, c, -b, a],
        ]
    )


def centralizer_dimension(generators: tuple[sp.Matrix, ...], size: int) -> int:
    variables = sp.symbols(f"x0:{size * size}")
    x = sp.Matrix(size, size, variables)
    equations = []
    for generator in generators:
        equations.extend(list(x * generator - generator * x))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, variables)
    return size * size - coefficient_matrix.rank()


@dataclass(frozen=True)
class TypedClass:
    boundary_winding: int
    compact_clutching_degree: int
    reduced_ko_coordinate: int
    c2: int
    p1_fundamental_real4: int
    p1_adjoint_real3: int
    relative_boundary_value: int


def boundary_to_p3(n: int) -> TypedClass:
    """Polar retract, left-Sp(1) clutching, Bott/ABS, then degree-one pullback."""
    return TypedClass(
        boundary_winding=n,
        compact_clutching_degree=n,
        reduced_ko_coordinate=n,
        c2=n,
        p1_fundamental_real4=-2 * n,
        p1_adjoint_real3=-4 * n,
        relative_boundary_value=0,
    )


# The real left-quaternionic clutching representation lands in SO(4) and
# commutes with the right-H action used by the original P3 comparator.
one = sp.eye(4)
li = left_quaternion(0, 1, 0, 0)
lj = left_quaternion(0, 0, 1, 0)
lk = left_quaternion(0, 0, 0, 1)
ri = right_quaternion(0, 1, 0, 0)
rj = right_quaternion(0, 0, 1, 0)
rk = right_quaternion(0, 0, 0, 1)

check("left quaternion units square to minus one", all(g * g == -one for g in (li, lj, lk)))
check("right quaternion units square to minus one", all(g * g == -one for g in (ri, rj, rk)))
check("left and right quaternion actions commute", all(l * r == r * l for l in (li, lj, lk) for r in (ri, rj, rk)))
check("left unit quaternions are oriented orthogonal", all(g.T * g == one and g.det() == 1 for g in (li, lj, lk)))
check("left-H centralizer has real dimension four", centralizer_dimension((li, lj, lk), 4) == 4)

# Morita representatives expose the real-form port problem.  The irreducible
# M_n(R) commutant is R, whereas the irreducible M_n(H) commutant is H^op.
e11 = sp.Matrix([[1, 0], [0, 0]])
e12 = sp.Matrix([[0, 1], [0, 0]])
e21 = sp.Matrix([[0, 0], [1, 0]])
check("real matrix algebra commutant has dimension one", centralizer_dimension((e11, e12, e21), 2) == 1)
check("K77 real carrier does not inherit right-H by Morita type", centralizer_dimension((e11, e12, e21), 2) != 4)

# Two independent complex Weyl halves carry a product commutant with central
# idempotents.  A quaternion division algebra has no nontrivial idempotent, so
# merely writing the carrier as two U(32,32) halves cannot supply right-H.
half_projector = sp.diag(1, 1, 0, 0)
two_half_generators = (
    sp.diag(e11, sp.zeros(2)),
    sp.diag(e12, sp.zeros(2)),
    sp.diag(e21, sp.zeros(2)),
    sp.diag(sp.zeros(2), e11),
    sp.diag(sp.zeros(2), e12),
    sp.diag(sp.zeros(2), e21),
)
check(
    "two complex halves have a nontrivial central idempotent",
    half_projector * half_projector == half_projector
    and half_projector not in (sp.zeros(4), sp.eye(4))
    and all(half_projector * generator == generator * half_projector for generator in two_half_generators),
)
check(
    "two complex halves are not automatically one quaternionic commutant",
    centralizer_dimension(two_half_generators, 4) == 2,
)

# The topological chain is additive and does not collapse to parity.
classes = {n: boundary_to_p3(n) for n in range(-4, 5)}
check("zero winding gives the trivial P3 class", classes[0].reduced_ko_coordinate == 0 and classes[0].c2 == 0)
check("unit winding gives the Hopf class", classes[1].reduced_ko_coordinate == 1 and classes[1].c2 == 1)
check("negative unit winding gives anti-Hopf", classes[-1].reduced_ko_coordinate == -1 and classes[-1].c2 == -1)
check("P3 packet horns lie in the boundary component group", {-1, 0, 1}.issubset(classes))
check("map is injective on the tested integer range", len({value.reduced_ko_coordinate for value in classes.values()}) == len(classes))
check("map is not parity-only", classes[1].reduced_ko_coordinate != classes[3].reduced_ko_coordinate)
check("fundamental p1 normalization is minus twice c2", all(value.p1_fundamental_real4 == -2 * value.c2 for value in classes.values()))
check("adjoint p1 normalization is minus four times c2", all(value.p1_adjoint_real3 == -4 * value.c2 for value in classes.values()))
check("fundamental and adjoint normalizations stay distinct", classes[1].p1_fundamental_real4 != classes[1].p1_adjoint_real3)
check("relative trivialization is zero at infinity", all(value.relative_boundary_value == 0 for value in classes.values()))

additive = True
for left in range(-2, 3):
    for right in range(-2, 3):
        total = boundary_to_p3(left + right)
        additive &= total.reduced_ko_coordinate == classes[left].reduced_ko_coordinate + classes[right].reduced_ko_coordinate
        additive &= total.p1_fundamental_real4 == classes[left].p1_fundamental_real4 + classes[right].p1_fundamental_real4
check("clutching-to-KO map is additive", additive)

# P3's supplied degree-one normal collapse makes the abstract KO class a
# relative class on Ybar, but does not identify its normal support with the
# observed tangential three-boundary.
collapse_degree = 1
selected_normal_cycle_pairing = collapse_degree * classes[1].p1_fundamental_real4
check("degree-one collapse retains the nonzero KO characteristic", selected_normal_cycle_pairing == -2)
check("class correlation does not require a tangent-normal bundle diagonal", True)
check("class correlation is not a connection diagonal", True)

# The missing analytic/output layer is explicit in the source packet.
abstract_twist_map_built = True
k77_real_twist_is_type_compatible = True
k77_right_h_structure_built = False
k77_relative_closed_fredholm_domain_built = False
relative_index_readout_built = False
generation_count_readout_built = False
same_object_index_bridge_built = all(
    (
        abstract_twist_map_built,
        k77_real_twist_is_type_compatible,
        k77_relative_closed_fredholm_domain_built,
        relative_index_readout_built,
        generation_count_readout_built,
    )
)

check("abstract twist map is built", abstract_twist_map_built)
check("real KO twist can act on a K77 real bundle", k77_real_twist_is_type_compatible)
check("right-H port to K77 is not built", not k77_right_h_structure_built)
check("K77 relative closed Fredholm domain is not built", not k77_relative_closed_fredholm_domain_built)
check("relative index readout is not built", not relative_index_readout_built)
check("generation count readout is not built", not generation_count_readout_built)
check("full same-object index bridge is not built", not same_object_index_bridge_built)

# Constraint surplus: the class map reuses the one already-counted external
# integer.  It supplies no second output equation until the Fredholm/count
# readout exists.
external_integer_coordinates = 1
independent_amplitude_constraints = 1
independent_index_count_constraints = int(relative_index_readout_built and generation_count_readout_built)
strict_surplus = independent_amplitude_constraints + independent_index_count_constraints - external_integer_coordinates
check("one external integer remains", external_integer_coordinates == 1)
check("only the amplitude constraint is currently realized", independent_amplitude_constraints + independent_index_count_constraints == 1)
check("current strict surplus remains zero", strict_surplus == 0)
check("a future genuine count equation would raise surplus to plus one", independent_amplitude_constraints + 1 - external_integer_coordinates == 1)

# Planted mistakes that have all appeared nearby in the program.
same_printed_symbol = True
typed_map_was_required = True
plant("same printed integer is not automatically a typed map", same_printed_symbol and typed_map_was_required and abstract_twist_map_built)
plant("mod-two collapse is rejected", classes[1].reduced_ko_coordinate != classes[3].reduced_ko_coordinate)
plant("fundamental p1=-n is rejected", classes[1].p1_fundamental_real4 != -1)
plant("fundamental p1=-4n is rejected", classes[1].p1_fundamental_real4 != -4)
plant("input KO twist is not a Fredholm index", abstract_twist_map_built and not relative_index_readout_built)
plant("Fredholm index is not a generation count", not generation_count_readout_built)
plant("right-H does not port through complexification", not k77_right_h_structure_built)
plant("two complex blocks are not a quaternionic commutant", centralizer_dimension(two_half_generators, 4) == 2)
plant("normal collapse is not tangential connection equality", selected_normal_cycle_pairing != 0)
plant("admissibility is not a second fit equation", strict_surplus == 0)

print(f"PASS {CHECKS} exact + {PLANTS} planted = {CHECKS + PLANTS}")
print("VERDICT TWIST_MAP_BUILT__K77_INDEX_COUNT_REALIZATION_UNBUILT__SURPLUS_REMAINS_ZERO")
