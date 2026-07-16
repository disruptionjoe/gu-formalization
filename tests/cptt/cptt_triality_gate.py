#!/usr/bin/env python3
"""
Exact low-cost gate for A. Garrett Lisi, "C, P, T, and Triality"
(arXiv:2407.02497v2) versus current GU generation structures.

This script checks only finite and representation-theoretic necessary
conditions.  It does not certify a physical CPTt symmetry, derive three
generations, or verify Lisi's full semilinear matrix representation.

Checks
------
1. Build the binary tetrahedral group 2T as the 24 Hurwitz units and the
   central product (2T x D4)/<(-1,r^2)>.  Verify exact order 96, closure,
   inverses, and the order-three quaternion used in the paper.
2. Verify that the three-cycle has the same real character as a 120-degree
   rotation of GU's native self-dual three-dimensional carrier.
3. Show why a three-cycle on three manually repeated identical sectors is a
   vacuous control, and that a nonidentical third sector breaks equivariance.
4. Apply the Lorentz-Casimir intertwiner obstruction to GU's current typed
   2+1 construction: spin 1/2 cannot be cycled into spin 3/2 by a
   Lorentz-equivariant invertible map.
5. Classify the currently evidenced GU result as KINEMATIC_ONLY.  The evidence
   booleans are an explicit obligation manifest, not machine-derived physics.

Run:
    python -u tests/cptt/cptt_triality_gate.py
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product


Quaternion = tuple[Fraction, Fraction, Fraction, Fraction]
D4Element = tuple[int, int]
ProductElement = tuple[Quaternion, D4Element]
Matrix = tuple[tuple[int, ...], ...]


def qneg(q: Quaternion) -> Quaternion:
    return tuple(-x for x in q)  # type: ignore[return-value]


def qconj(q: Quaternion) -> Quaternion:
    return q[0], -q[1], -q[2], -q[3]


def qnorm_squared(q: Quaternion) -> Fraction:
    return sum((x * x for x in q), start=Fraction(0))


def qmul(x: Quaternion, y: Quaternion) -> Quaternion:
    a, b, c, d = x
    e, f, g, h = y
    return (
        a * e - b * f - c * g - d * h,
        a * f + b * e + c * h - d * g,
        a * g - b * h + c * e + d * f,
        a * h + b * g - c * f + d * e,
    )


Q_ONE: Quaternion = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
Q_MINUS_ONE = qneg(Q_ONE)


def binary_tetrahedral_group() -> frozenset[Quaternion]:
    axes: set[Quaternion] = set()
    for coordinate in range(4):
        for sign in (-1, 1):
            value = [Fraction(0)] * 4
            value[coordinate] = Fraction(sign)
            axes.add(tuple(value))  # type: ignore[arg-type]
    halves = {
        tuple(Fraction(sign, 2) for sign in signs)
        for signs in product((-1, 1), repeat=4)
    }
    return frozenset(axes | halves)


def d4_mul(x: D4Element, y: D4Element) -> D4Element:
    """D4 = <r,s | r^4=s^2=1, srs=r^-1>."""
    r, s = x
    u, v = y
    return ((r + (-1 if s else 1) * u) % 4, (s + v) % 2)


D4 = tuple((r, s) for r in range(4) for s in range(2))
D4_ONE: D4Element = (0, 0)
D4_CENTER: D4Element = (2, 0)


def product_mul(x: ProductElement, y: ProductElement) -> ProductElement:
    return qmul(x[0], y[0]), d4_mul(x[1], y[1])


def central_class(x: ProductElement) -> frozenset[ProductElement]:
    """Class under (q,d) ~ (-q,r^2 d)."""
    paired = (qneg(x[0]), d4_mul(D4_CENTER, x[1]))
    return frozenset((x, paired))


def class_mul(
    x: frozenset[ProductElement], y: frozenset[ProductElement]
) -> frozenset[ProductElement]:
    return central_class(product_mul(next(iter(x)), next(iter(y))))


def mmul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0])))
        for i in range(len(a))
    )


def msub(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(x - y for x, y in zip(arow, brow)) for arow, brow in zip(a, b))


def identity(n: int) -> Matrix:
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))


def block_diag(blocks: tuple[Matrix, ...]) -> Matrix:
    sizes = [len(block) for block in blocks]
    total = sum(sizes)
    out = [[0] * total for _ in range(total)]
    offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            for j, value in enumerate(row):
                out[offset + i][offset + j] = value
        offset += len(block)
    return tuple(tuple(row) for row in out)


def three_copy_cycle(block_size: int) -> Matrix:
    """Cycle copy 0 -> 1 -> 2 -> 0, leaving within-copy indices fixed."""
    total = 3 * block_size
    out = [[0] * total for _ in range(total)]
    for copy in range(3):
        for i in range(block_size):
            out[((copy + 1) % 3) * block_size + i][copy * block_size + i] = 1
    return tuple(tuple(row) for row in out)


def is_zero(a: Matrix) -> bool:
    return all(value == 0 for row in a for value in row)


@dataclass(frozen=True)
class GUObligations:
    native_self_dual_triplet: bool
    native_order_three_element: bool
    three_equal_eigenspace_dimensions: bool
    finite_subgroup_selected_by_frozen_data: bool
    family_frame_identification_derived: bool
    interacting_action_equivariance_shown: bool
    positive_physical_quotient_lift_shown: bool
    full_cptt_action_on_one_gu_carrier: bool

    def classification(self) -> str:
        kinematic = (
            self.native_self_dual_triplet
            and self.native_order_three_element
            and self.three_equal_eigenspace_dimensions
        )
        physical = (
            self.interacting_action_equivariance_shown
            and self.positive_physical_quotient_lift_shown
            and self.full_cptt_action_on_one_gu_carrier
        )
        if physical:
            return "PHYSICAL_CANDIDATE"
        if kinematic:
            return "KINEMATIC_ONLY"
        return "NO_HOST"


def main() -> None:
    print("CPTt TRIALITY QUICK GATE")
    print("=" * 72)

    two_t = binary_tetrahedral_group()
    assert len(two_t) == 24
    assert all(qnorm_squared(q) == 1 for q in two_t)
    assert all(qmul(x, y) in two_t for x in two_t for y in two_t)
    assert all(any(qmul(x, y) == Q_ONE for y in two_t) for x in two_t)

    product_group = tuple((q, d) for q in two_t for d in D4)
    classes = frozenset(central_class(x) for x in product_group)
    assert len(product_group) == 192
    assert len(classes) == 96
    assert all(class_mul(a, b) in classes for a in classes for b in classes)
    identity_class = central_class((Q_ONE, D4_ONE))
    assert all(
        any(class_mul(a, b) == identity_class for b in classes)
        for a in classes
    )
    center = tuple(a for a in classes if all(class_mul(a, b) == class_mul(b, a) for b in classes))
    assert len(center) == 2

    # Equation 6.2 uses the negative Hurwitz unit.  Its raw quaternion order is
    # three.  The positive-sign variant printed later has raw order six, even
    # though its adjoint/projective action still has order three.
    t: Quaternion = tuple(Fraction(-1, 2) for _ in range(4))  # type: ignore[assignment]
    printed_positive = qneg(t)
    assert qmul(qmul(t, t), t) == Q_ONE
    assert qmul(qmul(qmul(printed_positive, printed_positive), printed_positive),
                qmul(qmul(printed_positive, printed_positive), printed_positive)) == Q_ONE
    assert qmul(qmul(printed_positive, printed_positive), printed_positive) == Q_MINUS_ONE
    qi: Quaternion = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
    qj: Quaternion = (Fraction(0), Fraction(0), Fraction(1), Fraction(0))
    qk: Quaternion = (Fraction(0), Fraction(0), Fraction(0), Fraction(1))
    assert qmul(qmul(t, qi), qconj(t)) == qj
    assert qmul(qmul(t, qj), qconj(t)) == qk
    assert qmul(qmul(t, qk), qconj(t)) == qi
    print("PASS  finite positive control: |2T|=24, |2T o D4|=96, center order 2")
    print("PASS  sign control: equation-6.2 t has order 3; positive raw unit has order 6")
    print("PASS  triality control: Ad_t cycles quaternion units i -> j -> k -> i")
    print("PASS  24 Hurwitz units have the exact 24-cell vertex coordinates")

    cycle3: Matrix = ((0, 0, 1), (1, 0, 0), (0, 1, 0))
    assert mmul(mmul(cycle3, cycle3), cycle3) == identity(3)
    assert sum(cycle3[i][i] for i in range(3)) == 0
    assert sum(cycle3[0][j] * (cycle3[1][(j + 1) % 3] * cycle3[2][(j + 2) % 3]
               - cycle3[1][(j + 2) % 3] * cycle3[2][(j + 1) % 3]) for j in range(3)) == 1
    print("PASS  native-carrier comparator: real C3 character is (dimension,trace)=(3,0)")

    d: Matrix = ((2, 0), (0, 3))
    d_other: Matrix = ((2, 0), (0, 5))
    repeated = block_diag((d, d, d))
    split = block_diag((d, d, d_other))
    copy_cycle = three_copy_cycle(2)
    assert is_zero(msub(mmul(copy_cycle, repeated), mmul(repeated, copy_cycle)))
    assert not is_zero(msub(mmul(copy_cycle, split), mmul(split, copy_cycle)))
    print("PASS  vacuity control: a cycle commutes with any manually repeated operator")
    print("PASS  sensitivity control: a different third operator breaks the cycle")

    spin_half_casimir = Fraction(3, 4)
    spin_three_half_casimir = Fraction(15, 4)
    assert spin_half_casimir != spin_three_half_casimir
    assert all(
        (spin_half_casimir - spin_three_half_casimir) * entry != 0
        for entry in (Fraction(1), Fraction(-1), Fraction(2))
    )
    print("PASS  typed 2+1 obstruction: distinct Lorentz Casimirs force every intertwiner to zero")

    obligations = GUObligations(
        native_self_dual_triplet=True,
        native_order_three_element=True,
        three_equal_eigenspace_dimensions=True,
        finite_subgroup_selected_by_frozen_data=False,
        family_frame_identification_derived=False,
        interacting_action_equivariance_shown=False,
        positive_physical_quotient_lift_shown=False,
        full_cptt_action_on_one_gu_carrier=False,
    )
    assert obligations.classification() == "KINEMATIC_ONLY"
    print("PASS  evidence manifest classification: KINEMATIC_ONLY")
    print()
    print("VERDICT")
    print("  KINEMATICALLY_HOSTED: GU has a matching self-dual C3 carrier.")
    print("  NOT_NATIVE_FORCED: frozen GU data does not select the finite subgroup or families.")
    print("  NO_GO (current typed 2+1): nonisomorphic Lorentz sectors cannot be triality-cycled.")
    print("  PHYSICAL_ACTION UNDERDEFINED: action, positivity, and quotient lift are unbuilt.")


if __name__ == "__main__":
    main()
