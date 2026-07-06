#!/usr/bin/env python3
"""Finite CALM/GW axial-charge query gate.

This validator checks the order-theoretic shape named by
`lab/active-research/calm-gw-boundary/gw-chiral-charge-calm-check-2026-07-06.md`.

It is intentionally finite and dependency-free. It does not prove anything about
the actual GW operator. It checks that a signed charge query is monotone when it
keeps its nonnegative Jordan components visible, and that the scalar net and
rounded integer readouts fail monotonicity after those components are forgotten.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from typing import Callable, Iterable, TypeVar


ASSERTS = 0
T = TypeVar("T")


@dataclass(frozen=True)
class ChargeAtom:
    name: str
    plus: Fraction
    minus: Fraction
    role: str


AtomSet = frozenset[ChargeAtom]
Query = Callable[[AtomSet], T]
Order = Callable[[T, T], bool]


def check(condition: bool, message: str) -> None:
    global ASSERTS
    ASSERTS += 1
    assert condition, message


def all_subsets(atoms: tuple[ChargeAtom, ...]) -> list[AtomSet]:
    subsets: list[AtomSet] = []
    for size in range(len(atoms) + 1):
        for combo in combinations(atoms, size):
            subsets.append(frozenset(combo))
    return subsets


def inclusion_pairs(subsets: Iterable[AtomSet]) -> list[tuple[AtomSet, AtomSet]]:
    pool = list(subsets)
    return [(left, right) for left in pool for right in pool if left.issubset(right)]


def prefer_signed_cancellation_witness(
    pairs: Iterable[tuple[AtomSet, AtomSet]],
) -> list[tuple[AtomSet, AtomSet]]:
    def rank(pair: tuple[AtomSet, AtomSet]) -> tuple[int, int, int]:
        smaller, larger = pair
        added = larger - smaller
        has_positive_base = any(atom.plus > atom.minus for atom in smaller)
        adds_negative = any(atom.minus > atom.plus for atom in added)
        return (0 if has_positive_base and adds_negative else 1, len(smaller), len(larger))

    return sorted(pairs, key=rank)


def jordan_query(events: AtomSet) -> tuple[Fraction, Fraction]:
    return (
        sum((event.plus for event in events), Fraction(0)),
        sum((event.minus for event in events), Fraction(0)),
    )


def plus_projection(events: AtomSet) -> Fraction:
    return jordan_query(events)[0]


def minus_projection(events: AtomSet) -> Fraction:
    return jordan_query(events)[1]


def net_query(events: AtomSet) -> Fraction:
    plus, minus = jordan_query(events)
    return plus - minus


def rounded_integer_query(events: AtomSet) -> int:
    net = net_query(events)
    if net >= 1:
        return 1
    if net <= -1:
        return -1
    return 0


def product_order(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> bool:
    return left[0] <= right[0] and left[1] <= right[1]


def scalar_order(left: Fraction, right: Fraction) -> bool:
    return left <= right


def int_order(left: int, right: int) -> bool:
    return left <= right


def monotonicity_witness(
    pairs: Iterable[tuple[AtomSet, AtomSet]],
    query: Query[T],
    order: Order[T],
) -> tuple[AtomSet, AtomSet, T, T] | None:
    for smaller, larger in pairs:
        q_small = query(smaller)
        q_large = query(larger)
        if not order(q_small, q_large):
            return smaller, larger, q_small, q_large
    return None


def names(events: AtomSet) -> str:
    if not events:
        return "{}"
    return "{" + ", ".join(sorted(event.name for event in events)) + "}"


def format_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def format_value(value: object) -> str:
    if isinstance(value, tuple):
        return "(" + ", ".join(format_fraction(item) for item in value) + ")"
    if isinstance(value, Fraction):
        return format_fraction(value)
    return str(value)


def assert_monotone(
    label: str,
    pairs: Iterable[tuple[AtomSet, AtomSet]],
    query: Query[T],
    order: Order[T],
) -> None:
    witness = monotonicity_witness(pairs, query, order)
    check(witness is None, f"{label} should be monotone, witness: {witness}")


def assert_non_monotone(
    label: str,
    pairs: Iterable[tuple[AtomSet, AtomSet]],
    query: Query[T],
    order: Order[T],
) -> tuple[AtomSet, AtomSet, T, T]:
    witness = monotonicity_witness(pairs, query, order)
    check(witness is not None, f"{label} should have a monotonicity violation")
    assert witness is not None
    return witness


def main() -> None:
    print("=" * 88)
    print("CALM/GW BOUNDARY: FINITE AXIAL-CHARGE MONOTONICITY GATE")
    print("=" * 88)

    atoms = (
        ChargeAtom("gw_plus_zero_mode", Fraction(6, 5), Fraction(0), "positive GW contribution"),
        ChargeAtom("gw_minus_partner", Fraction(0), Fraction(11, 10), "negative GW contribution"),
        ChargeAtom("boundary_tail_plus", Fraction(2, 5), Fraction(0), "positive boundary tail"),
        ChargeAtom("boundary_tail_minus", Fraction(0), Fraction(1, 5), "negative boundary tail"),
    )

    for atom in atoms:
        check(atom.plus >= 0 and atom.minus >= 0, f"{atom.name} must have nonnegative components")

    subsets = all_subsets(atoms)
    pairs = inclusion_pairs(subsets)
    print(f"  atoms: {len(atoms)}")
    print(f"  subsets checked: {len(subsets)}")
    print(f"  inclusion pairs checked: {len(pairs)}")

    assert_monotone("Jordan-component charge", pairs, jordan_query, product_order)
    assert_monotone("positive component projection", pairs, plus_projection, scalar_order)
    assert_monotone("negative component projection", pairs, minus_projection, scalar_order)
    print("\nAccepted readout:")
    print("  Jordan-component charge (Q_plus, Q_minus) is monotone in product order.")

    cancellation_pairs = prefer_signed_cancellation_witness(pairs)
    net_witness = assert_non_monotone("scalar net charge", cancellation_pairs, net_query, scalar_order)
    rounded_witness = assert_non_monotone(
        "rounded integer index", cancellation_pairs, rounded_integer_query, int_order
    )

    print("\nRejected readouts:")
    for label, witness in (
        ("scalar net charge", net_witness),
        ("rounded integer index", rounded_witness),
    ):
        smaller, larger, q_small, q_large = witness
        print(f"  {label}:")
        print(f"    smaller input: {names(smaller)} -> {format_value(q_small)}")
        print(f"    larger input:  {names(larger)} -> {format_value(q_large)}")

    print("\nInterpretation:")
    print("  PASS. The finite gate preserves monotonicity only while signed charge")
    print("  remains exposed as nonnegative Jordan components. The scalar and rounded")
    print("  readouts are the non-monotone forgetful steps, not coordination-free")
    print("  certificates for an actual GW operator.")
    print(f"  hard asserts passed: {ASSERTS}")


if __name__ == "__main__":
    main()
