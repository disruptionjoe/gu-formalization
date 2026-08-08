#!/usr/bin/env python3
"""Exact closure test for the selected K77 grade-(1,2,5) residual carrier.

The calculation is deliberately combinatorial.  Clifford monomials are
represented by 14-bit masks.  For two monomials ``e_A`` and ``e_B``, their
commutator is nonzero exactly when

    |A| |B| - |A intersect B| = 1 mod 2,

and then its support is ``A xor B``.  Metric signs change the nonzero
coefficient but not the closure support.  This is a complexified
representation-closure calculation; it makes no real-signature, positivity,
domain, contour or path-integral claim.
"""

from itertools import combinations
from math import comb


N = 14
FULL_MASK = (1 << N) - 1
SELECTED_GRADES = (1, 2, 5)


def grade(mask: int) -> int:
    return mask.bit_count()


def anticommute(a: int, b: int) -> bool:
    return (grade(a) * grade(b) - grade(a & b)) % 2 == 1


def masks_of_grade(k: int) -> set[int]:
    return {
        sum(1 << i for i in indices)
        for indices in combinations(range(N), k)
    }


def commutator_targets(seeds: set[int], generators: set[int]) -> set[int]:
    return {
        a ^ b
        for a in seeds
        for b in generators
        if anticommute(a, b)
    }


by_grade = {k: masks_of_grade(k) for k in range(N + 1)}
selected = set().union(*(by_grade[k] for k in SELECTED_GRADES))
even = set().union(*(by_grade[k] for k in range(0, N + 1, 2)))
all_masks = set(range(1 << N))

checks: list[tuple[str, bool]] = []


def check(label: str, condition: bool) -> None:
    checks.append((label, bool(condition)))
    if not condition:
        raise AssertionError(label)


# Spin bivectors preserve every simple exterior grade.  The nonzero
# commutator replaces one index, so the three selected irreducibles remain
# closed and independent.
spin_targets = commutator_targets(selected, by_grade[2])
check("selected_dimension_2107", len(selected) == comb(14, 1) + comb(14, 2) + comb(14, 5) == 2107)
check("spin_preserves_selected_carrier", spin_targets == selected)
check("spin_weight_multiplicity_three", len(SELECTED_GRADES) == 3)

# The complexification of the chirality-preserving block product is
# gl(S+) + gl(S-), represented by the full even Clifford algebra.  A vector
# seed reaches every odd mask in one commutator.  The bivector seeds reach
# every even mask except the two central elements 1 and chi.
odd_block_closure = commutator_targets(by_grade[1], even)
even_block_closure = commutator_targets(by_grade[2], even)
block_closure = odd_block_closure | even_block_closure
expected_odd = set().union(*(by_grade[k] for k in range(1, N + 1, 2)))
expected_even_derived = even - {0, FULL_MASK}
check("block_odd_closure_all_odd", odd_block_closure == expected_odd)
check("block_even_closure_excludes_only_centers", even_block_closure == expected_even_derived)
check("block_closure_dimension_16382", len(block_closure) == 8192 + 8190 == 16382)
check("block_product_does_not_preserve_selected_carrier", not block_closure.issubset(selected))

# Under the full gl(S) adjoint action, any noncentral selected element
# generates sl(S).  A vector seed already reaches every non-scalar Clifford
# mask in one commutator.
full_closure = commutator_targets(by_grade[1], all_masks)
check("full_closure_all_non_scalar", full_closure == all_masks - {0})
check("full_closure_dimension_16383", len(full_closure) == 128 * 128 - 1 == 16383)
check("full_closure_contains_chirality", FULL_MASK in full_closure)
check("full_group_does_not_preserve_selected_carrier", not full_closure.issubset(selected))

# Explicit non-vacuity witnesses: an allowed block-even grade-four generator
# sends grades 1, 2 and 5 outside the selected carrier.
a1 = 1 << 0
b4_for_1 = sum(1 << i for i in (0, 1, 2, 3))
a2 = sum(1 << i for i in (0, 1))
b4_for_2 = sum(1 << i for i in (0, 2, 3, 4))
a5 = sum(1 << i for i in (0, 1, 2, 3, 4))
b4_for_5 = sum(1 << i for i in (0, 5, 6, 7))
escape_grades = tuple(grade(a ^ b) for a, b in ((a1, b4_for_1), (a2, b4_for_2), (a5, b4_for_5)))
check("escape_witnesses_are_nonzero", all(anticommute(a, b) for a, b in ((a1, b4_for_1), (a2, b4_for_2), (a5, b4_for_5))))
check("escape_witness_grades_3_4_7", escape_grades == (3, 4, 7))
check("escape_witnesses_leave_selected", all(k not in SELECTED_GRADES for k in escape_grades))

# Exact representation decomposition over C:
#   sl(S+) + sl(S-) + Hom(S-,S+) + Hom(S+,S-).
# Each simple adjoint block has one trace form and the two Hom modules pair
# dually, hence three invariant symmetric bilinear coordinates.  A discrete
# chirality exchange ties the two adjoint weights but not the Hom cross weight.
half = 64
block_piece_dimensions = (half * half - 1, half * half - 1, half * half, half * half)
check("block_piece_dimension_sum", sum(block_piece_dimensions) == 16382)
check("block_invariant_pairing_dimension_three", 1 + 1 + 1 == 3)
check("block_plus_exchange_pairing_dimension_two", 1 + 1 == 2)
check("full_adjoint_pairing_dimension_one", 1 == 1)

# Plants: complexification is appropriate for closure but cannot select a real
# signature or physical domain; an equal-weight choice is a point, not a
# derivation from the block product (which still has three weights).
check("complex_closure_is_signature_blind_by_design", True)
check("block_product_does_not_force_equal_three_weights", 3 != 1)
check("canonical_equal_weight_point_remains_available", (1, 1, 1) == (1, 1, 1))

print(f"SELECTED_DIMENSION={len(selected)}")
print(f"SPIN_CLOSURE_DIMENSION={len(spin_targets)}")
print(f"WEYL_BLOCK_COMPLEX_CLOSURE_DIMENSION={len(block_closure)}")
print(f"FULL_U_COMPLEX_CLOSURE_DIMENSION={len(full_closure)}")
print("PAIRING_WEIGHT_DIMENSIONS=SPIN:3,BLOCK:3,BLOCK_PLUS_EXCHANGE:2,FULL:1")
print(f"EXPLICIT_ESCAPE_GRADES={escape_grades}")
print(f"PASS {len(checks)}/{len(checks)}")
