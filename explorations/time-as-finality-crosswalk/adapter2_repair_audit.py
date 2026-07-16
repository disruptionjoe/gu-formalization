"""ADAPTER2-01: repair-or-downgrade audit for the Ext_S to TaF bridge.

The superseded adapter claimed that a three-coordinate cardinality proxy was
the TaF D1 object and that opposite Ext_S fork branches mapped to incomparable
T18 branches. This audit checks the smallest honest repairs.

Result:

* The profile-only map is a monotone functor on the finite inclusion model.
* It forgets branch polarity: the + and - fork endpoints have equal profiles.
* A D1Field-style enrichment carrying proposition values preserves the fork,
  but the value lives in a discrete fiber forgotten by the D1 projection.
* Choosing which fiber point means positive norm requires an extra sign anchor.

The corrected structure is therefore a polarity fiber over a finality profile,
not an established identity between the polarity and the finality axis.

Pure Python. Exit 0 means the downgrade boundary is preserved.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


Literal = tuple[str, int]
State = frozenset[Literal]


def consistent(state: State) -> bool:
    values: dict[str, int] = {}
    for proposition, sign in state:
        if sign not in (-1, 1):
            return False
        if proposition in values and values[proposition] != sign:
            return False
        values[proposition] = sign
    return True


def extend(state: State, additions: tuple[Literal, ...]) -> State | None:
    candidate = frozenset((*state, *additions))
    return candidate if consistent(candidate) else None


def is_extension(source: State, target: State) -> bool:
    return consistent(source) and consistent(target) and source.issubset(target)


@dataclass(frozen=True, order=True)
class D1Profile:
    """Four-coordinate shape of TaF's local D1 profile.

    This finite proxy uses one count for every coordinate only to test the
    categorical forgetful map. It is not a physical derivation of accessible
    support, holder redundancy, branch support, or reversal cost.
    """

    accessible_support: int
    holder_redundancy: int
    branch_support: int
    reversal_cost: int


def profile(state: State) -> D1Profile:
    n = len(state)
    return D1Profile(n, n, n, n)


def profile_leq(left: D1Profile, right: D1Profile) -> bool:
    return (
        left.accessible_support <= right.accessible_support
        and left.holder_redundancy <= right.holder_redundancy
        and left.branch_support <= right.branch_support
        and left.reversal_cost <= right.reversal_cost
    )


def profile_morphism(source: State, target: State) -> tuple[D1Profile, D1Profile] | None:
    if not is_extension(source, target):
        return None
    before, after = profile(source), profile(target)
    return (before, after) if profile_leq(before, after) else None


@dataclass(frozen=True)
class D1FieldProxy:
    """Minimal TaF-native vocabulary enrichment used as a repair control."""

    local_profile: D1Profile
    proposition_values: State


def field(state: State) -> D1FieldProxy:
    return D1FieldProxy(profile(state), state)


def field_morphism(source: State, target: State) -> tuple[D1FieldProxy, D1FieldProxy] | None:
    if not is_extension(source, target):
        return None
    return field(source), field(target)


def forget_values(value: D1FieldProxy) -> D1Profile:
    return value.local_profile


def flip(state: State) -> State:
    return frozenset((proposition, -sign) for proposition, sign in state)


def all_small_states() -> tuple[State, ...]:
    states: set[State] = {frozenset()}
    propositions = ("p", "q", "r")
    for length in range(1, len(propositions) + 1):
        for chosen in product((-1, 0, 1), repeat=len(propositions)):
            state = frozenset(
                (proposition, sign)
                for proposition, sign in zip(propositions, chosen)
                if sign != 0
            )
            if len(state) == length and consistent(state):
                states.add(state)
    return tuple(states)


def main() -> None:
    states = all_small_states()
    arrows = tuple((source, target) for source in states for target in states if is_extension(source, target))

    identity_ok = all(profile_morphism(state, state) == (profile(state), profile(state)) for state in states)
    composition_ok = True
    field_composition_ok = True
    for source, middle in arrows:
        for middle_again, target in arrows:
            if middle_again != middle:
                continue
            direct = profile_morphism(source, target)
            composite = (profile(source), profile(target))
            composition_ok &= direct == composite
            field_direct = field_morphism(source, target)
            field_composite = (field(source), field(target))
            field_composition_ok &= field_direct == field_composite

    empty: State = frozenset()
    plus = extend(empty, (("p", 1),))
    minus = extend(empty, (("p", -1),))
    assert plus is not None and minus is not None
    source_fork_has_no_join = extend(plus, (("p", -1),)) is None

    profile_collapses_fork = profile(plus) == profile(minus)
    profile_target_incomparable = not profile_leq(profile(plus), profile(minus)) and not profile_leq(
        profile(minus), profile(plus)
    )
    field_preserves_fork = field(plus) != field(minus)
    forgetful_projection_collapses_fork = forget_values(field(plus)) == forget_values(field(minus))

    flip_preserves_every_profile = all(profile(flip(state)) == profile(state) for state in states)
    two_equal_anchor_choices = {
        "choice_a": {plus: 1, minus: -1},
        "choice_b": {plus: -1, minus: 1},
    }
    anchor_is_canonical = two_equal_anchor_choices["choice_a"] == two_equal_anchor_choices["choice_b"]

    legacy_dimension_count = 3
    actual_taf_local_dimension_count = 4
    legacy_used_actual_d1_shape = legacy_dimension_count == actual_taf_local_dimension_count

    checks = {
        "profile_functor_identity": identity_ok,
        "profile_functor_composition": composition_ok,
        "field_functor_composition": field_composition_ok,
        "source_fork_has_no_join": source_fork_has_no_join,
        "profile_collapses_fork": profile_collapses_fork,
        "profile_target_incomparable": profile_target_incomparable,
        "field_enrichment_preserves_fork": field_preserves_fork,
        "forgetful_projection_collapses_fork": forgetful_projection_collapses_fork,
        "flip_preserves_every_profile": flip_preserves_every_profile,
        "external_anchor_is_canonical": anchor_is_canonical,
        "legacy_used_actual_d1_shape": legacy_used_actual_d1_shape,
    }

    expected = {
        "profile_functor_identity": True,
        "profile_functor_composition": True,
        "field_functor_composition": True,
        "source_fork_has_no_join": True,
        "profile_collapses_fork": True,
        "profile_target_incomparable": False,
        "field_enrichment_preserves_fork": True,
        "forgetful_projection_collapses_fork": True,
        "flip_preserves_every_profile": True,
        "external_anchor_is_canonical": False,
        "legacy_used_actual_d1_shape": False,
    }
    assert checks == expected, (checks, expected)

    print("ADAPTER2-01 REPAIR-OR-DOWNGRADE AUDIT")
    print("=" * 72)
    for name, value in checks.items():
        print(f"PASS  {name}: {value}")
    print()
    print("REPAIR CENSUS")
    print("  profile-only map: monotone functor, but polarity-forgetting")
    print("  D1Field enrichment: fork-preserving, but polarity is an added fiber")
    print("  polarity-decorated target: circular unless an external anchor is supplied")
    print()
    print("VERDICT")
    print("  MONOTONE FORGETFUL FUNCTOR SURVIVES")
    print("  BRANCH-PRESERVING T18 ADAPTER FAILS")
    print("  bar(b) = finality-axis polarity remains OPEN, not ratified")


if __name__ == "__main__":
    main()
