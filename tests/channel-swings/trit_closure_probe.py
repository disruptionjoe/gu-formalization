"""Finite structural probe for the pre-registered trit-closure swing.

The probe asks whether a three-element total-order nesting supplies a natural
order-three wrap.  It deliberately tests only the shape already frozen by the
TRIT-INTERPRETATION triage; it imports no P2C truth and makes no physics claim.
"""

from itertools import permutations


POINTS = (0, 1, 2)  # world >= access >= standpoint, written top to bottom


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[i]] for i in POINTS)


def order(permutation: tuple[int, ...]) -> int:
    current = POINTS
    for n in range(1, 7):
        current = compose(permutation, current)
        if current == POINTS:
            return n
    raise AssertionError("permutation order exceeded S3 bound")


def preserves_total_order(permutation: tuple[int, ...]) -> bool:
    return all(
        (i <= j) == (permutation[i] <= permutation[j])
        for i in POINTS
        for j in POINTS
    )


def preserves_directed_path(permutation: tuple[int, ...]) -> bool:
    edges = {(0, 1), (1, 2)}
    return {(permutation[a], permutation[b]) for a, b in edges} == edges


def preserves_undirected_triangle(permutation: tuple[int, ...]) -> bool:
    edges = {frozenset((0, 1)), frozenset((1, 2)), frozenset((2, 0))}
    return {
        frozenset((permutation[a], permutation[b]))
        for a, b in ((0, 1), (1, 2), (2, 0))
    } == edges


def main() -> None:
    group = tuple(permutations(POINTS))
    chain_aut = tuple(p for p in group if preserves_total_order(p))
    directed_path_aut = tuple(p for p in group if preserves_directed_path(p))
    triangle_aut = tuple(p for p in group if preserves_undirected_triangle(p))
    order_three = tuple(p for p in group if order(p) == 3)

    checks = {
        "E1_total_chain_automorphism_group_is_trivial": chain_aut == (POINTS,),
        "E2_no_order_three_chain_automorphism": not set(chain_aut) & set(order_three),
        "E3_directed_chain_control_has_no_wrap": directed_path_aut == (POINTS,),
        "E4_unoriented_triangle_control_has_full_S3": len(triangle_aut) == 6,
        "E5_unoriented_triangle_contains_both_3cycles": len(set(triangle_aut) & set(order_three)) == 2,
        "F1_any_wrap_adds_non_chain_structure": all(not preserves_total_order(p) for p in order_three),
        "F2_arity_match_does_not_supply_cyclic_action": len(POINTS) == 3 and len(chain_aut) == 1,
    }
    failed = [name for name, passed in checks.items() if not passed]
    for name, passed in checks.items():
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    print(
        "HEADLINE: CLOSURE-FAILS-NATURALITY; "
        f"{len(checks) - len(failed)} checks pass; "
        "the total nesting supplies no order-three automorphism; "
        "an S3-symmetric triangle does only after adding a wrap edge."
    )
    if failed:
        raise SystemExit(f"failed checks: {', '.join(failed)}")


if __name__ == "__main__":
    main()
