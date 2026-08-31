#!/usr/bin/env python3
"""Exact finite controls for the fixed-middle Burnside balance quotient.

The positive model is the balanced product

    (H\\S3) x_{S3} (S3/H)  ~=  H\\S3/H

for the nonnormal order-two subgroup H=< (01) >.  The probe also checks both
regular-biset unit laws and the two parenthesizations of a three-biset product.
Hostile variants omit balance moves or quotient the two factors independently.
"""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass
from typing import Callable, FrozenSet, Hashable, Iterable, Sequence, TypeVar


Permutation = tuple[int, int, int]
T = TypeVar("T", bound=Hashable)
U = TypeVar("U", bound=Hashable)


def compose(p: Permutation, q: Permutation) -> Permutation:
    """Composition p after q."""

    return tuple(p[q[i]] for i in range(3))  # type: ignore[return-value]


def inverse(p: Permutation) -> Permutation:
    out = [0, 0, 0]
    for i, value in enumerate(p):
        out[value] = i
    return tuple(out)  # type: ignore[return-value]


S3: tuple[Permutation, ...] = tuple(itertools.permutations(range(3)))
IDENTITY: Permutation = (0, 1, 2)
TRANSPOSITION_01: Permutation = (1, 0, 2)
H: FrozenSet[Permutation] = frozenset({IDENTITY, TRANSPOSITION_01})


def left_coset(g: Permutation) -> FrozenSet[Permutation]:
    return frozenset(compose(h, g) for h in H)


def right_coset(g: Permutation) -> FrozenSet[Permutation]:
    return frozenset(compose(g, h) for h in H)


LEFT_COSETS = tuple(sorted({left_coset(g) for g in S3}, key=lambda c: sorted(c)))
RIGHT_COSETS = tuple(sorted({right_coset(g) for g in S3}, key=lambda c: sorted(c)))


def right_on_left_coset(
    coset: FrozenSet[Permutation], g: Permutation
) -> FrozenSet[Permutation]:
    return frozenset(compose(x, g) for x in coset)


def left_on_right_coset(
    g: Permutation, coset: FrozenSet[Permutation]
) -> FrozenSet[Permutation]:
    return frozenset(compose(g, x) for x in coset)


def double_coset(g: Permutation) -> FrozenSet[Permutation]:
    return frozenset(compose(compose(h1, g), h2) for h1 in H for h2 in H)


@dataclass
class UnionFind:
    parent: dict[Hashable, Hashable]

    @classmethod
    def on(cls, values: Iterable[Hashable]) -> "UnionFind":
        return cls({value: value for value in values})

    def find(self, value: Hashable) -> Hashable:
        parent = self.parent[value]
        if parent != value:
            self.parent[value] = self.find(parent)
        return self.parent[value]

    def union(self, left: Hashable, right: Hashable) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            self.parent[right_root] = left_root

    def classes(self) -> tuple[FrozenSet[Hashable], ...]:
        buckets: dict[Hashable, set[Hashable]] = {}
        for value in self.parent:
            buckets.setdefault(self.find(value), set()).add(value)
        return tuple(frozenset(bucket) for bucket in buckets.values())


def balanced_classes(
    left_values: Sequence[T],
    right_values: Sequence[U],
    right_action: Callable[[T, Permutation], T],
    left_action: Callable[[Permutation, U], U],
    acting_elements: Sequence[Permutation] = S3,
) -> tuple[FrozenSet[tuple[T, U]], ...]:
    pairs = tuple(itertools.product(left_values, right_values))
    uf = UnionFind.on(pairs)
    for left, right in pairs:
        for g in acting_elements:
            uf.union((right_action(left, g), right), (left, left_action(g, right)))
    return tuple(frozenset(c) for c in uf.classes())  # type: ignore[arg-type]


def class_lookup(classes: Sequence[FrozenSet[T]]) -> dict[T, FrozenSet[T]]:
    return {value: cls for cls in classes for value in cls}


def constant_value(cls: Iterable[T], function: Callable[[T], U]) -> U:
    values = {function(value) for value in cls}
    assert len(values) == 1
    return tuple(values)[0]


def independent_orbit_quotient_count() -> int:
    pairs = tuple(itertools.product(LEFT_COSETS, RIGHT_COSETS))
    uf = UnionFind.on(pairs)
    for x, y in pairs:
        for g in S3:
            uf.union((right_on_left_coset(x, g), y), (x, y))
            uf.union((x, left_on_right_coset(g, y)), (x, y))
    return len(uf.classes())


def run_probe() -> dict[str, object]:
    checks: list[str] = []

    assert len(S3) == 6 and len(H) == 2
    checks.append("finite_S3_and_order_two_subgroup")

    conjugates = {
        frozenset(compose(compose(g, h), inverse(g)) for h in H) for g in S3
    }
    assert len(conjugates) == 3 and H in conjugates
    checks.append("H_is_explicitly_nonnormal")

    ill_defined_witness = None
    for a in S3:
        for a_prime in right_coset(a):
            for b in S3:
                if right_coset(compose(a, b)) != right_coset(compose(a_prime, b)):
                    ill_defined_witness = (a, a_prime, b)
                    break
            if ill_defined_witness:
                break
        if ill_defined_witness:
            break
    assert ill_defined_witness is not None
    checks.append("nonnormal_quotient_group_shortcut_rejected")

    direct = balanced_classes(
        LEFT_COSETS,
        RIGHT_COSETS,
        right_on_left_coset,
        left_on_right_coset,
    )
    direct_signatures = {
        constant_value(
            cls,
            lambda pair: double_coset(
                compose(min(pair[0]), min(pair[1]))
            ),
        )
        for cls in direct
    }
    all_double_cosets = {double_coset(g) for g in S3}
    assert len(direct) == 2
    assert direct_signatures == all_double_cosets
    checks.append("balance_classes_equal_double_coset_fibers")

    regular = S3
    left_unit_stage = balanced_classes(
        LEFT_COSETS,
        regular,
        right_on_left_coset,
        lambda g, m: compose(g, m),
    )
    assert len(left_unit_stage) == len(LEFT_COSETS) == 3
    for cls in left_unit_stage:
        constant_value(cls, lambda pair: right_on_left_coset(pair[0], pair[1]))
    checks.append("right_regular_identity_biset_law")

    right_unit_stage = balanced_classes(
        regular,
        RIGHT_COSETS,
        compose,
        left_on_right_coset,
    )
    assert len(right_unit_stage) == len(RIGHT_COSETS) == 3
    for cls in right_unit_stage:
        constant_value(cls, lambda pair: left_on_right_coset(pair[0], pair[1]))
    checks.append("left_regular_identity_biset_law")

    left_stage_lookup = class_lookup(left_unit_stage)

    def left_stage_right_action(
        cls: FrozenSet[tuple[FrozenSet[Permutation], Permutation]], g: Permutation
    ) -> FrozenSet[tuple[FrozenSet[Permutation], Permutation]]:
        x, m = list(cls)[0]
        return left_stage_lookup[(x, compose(m, g))]

    left_associated = balanced_classes(
        left_unit_stage,
        RIGHT_COSETS,
        left_stage_right_action,
        left_on_right_coset,
    )

    right_stage_lookup = class_lookup(right_unit_stage)

    def right_stage_left_action(
        g: Permutation,
        cls: FrozenSet[tuple[Permutation, FrozenSet[Permutation]]],
    ) -> FrozenSet[tuple[Permutation, FrozenSet[Permutation]]]:
        m, y = list(cls)[0]
        return right_stage_lookup[(compose(g, m), y)]

    right_associated = balanced_classes(
        LEFT_COSETS,
        right_unit_stage,
        right_on_left_coset,
        right_stage_left_action,
    )

    def left_associated_signature(
        value: tuple[
            FrozenSet[tuple[FrozenSet[Permutation], Permutation]],
            FrozenSet[Permutation],
        ]
    ) -> FrozenSet[Permutation]:
        stage, y = value
        x, m = list(stage)[0]
        return double_coset(compose(compose(min(x), m), min(y)))

    def right_associated_signature(
        value: tuple[
            FrozenSet[Permutation],
            FrozenSet[tuple[Permutation, FrozenSet[Permutation]]],
        ]
    ) -> FrozenSet[Permutation]:
        x, stage = value
        m, y = list(stage)[0]
        return double_coset(compose(compose(min(x), m), min(y)))

    left_signatures = {
        constant_value(cls, left_associated_signature) for cls in left_associated
    }
    right_signatures = {
        constant_value(cls, right_associated_signature) for cls in right_associated
    }
    assert len(left_associated) == len(right_associated) == 2
    assert left_signatures == right_signatures == all_double_cosets
    checks.append("three_biset_associativity_coherence")

    trivial_group_product = balanced_classes(
        ("x0", "x1"),
        ("y0", "y1", "y2"),
        lambda x, _g: x,
        lambda _g, y: y,
        (IDENTITY,),
    )
    assert len(trivial_group_product) == 6
    checks.append("identity_group_reduces_to_cartesian_product")

    omitted = balanced_classes(
        LEFT_COSETS,
        RIGHT_COSETS,
        right_on_left_coset,
        left_on_right_coset,
        (IDENTITY,),
    )
    assert len(omitted) == 9 and len(omitted) != len(direct)
    checks.append("hostile_identity_only_relation_rejected")

    subgroup_only = balanced_classes(
        LEFT_COSETS,
        RIGHT_COSETS,
        right_on_left_coset,
        left_on_right_coset,
        tuple(H),
    )
    assert len(subgroup_only) > len(direct)
    checks.append("hostile_omitted_nonnormal_moves_rejected")

    over_quotient_count = independent_orbit_quotient_count()
    assert over_quotient_count == 1 and over_quotient_count != len(direct)
    checks.append("hostile_independent_over_quotient_rejected")

    return {
        "status": "PASS",
        "checks": len(checks),
        "check_names": checks,
        "balanced_double_cosets": len(direct),
        "left_associated_classes": len(left_associated),
        "right_associated_classes": len(right_associated),
        "identity_only_classes": len(omitted),
        "subgroup_only_classes": len(subgroup_only),
        "over_quotient_classes": over_quotient_count,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    result = run_probe()
    if args.selftest:
        print(f"PASS {result['checks']}/{result['checks']}")
    else:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
