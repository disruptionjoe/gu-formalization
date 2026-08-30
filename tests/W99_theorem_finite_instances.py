"""W99 -- finite-instance confirmation for the paper
"A Diagonal No-Go for Self-Valuations and an Invariance Classification"
(papers/candidates/observer-value-selection-theorem/observer-value-selection-theorem-2026-07-11.md).

This is confirmation, not proof.  The paper proves a pointwise diagonal lemma and the
pointwise invariance criterion for arbitrary sets.  This script exhaustively checks small
finite instances, including controls that separate the diagonal construction from weak
point-surjectivity (WPS).

Checks:
  (I-a) If alpha is fixed-point-free, every alpha-twisted diagonal escapes every row.
  (I-b) Independently of alpha, no WPS map A x A -> B exists when |B| >= 2.
  (II)  A valuation is alpha-invariant exactly when every value in its image is fixed.
  (III) The finite invariant-valuation census is |Fix(alpha)|^|A|, including
        the unique empty-domain valuation when Fix(alpha) is empty.
  (IV)  For the regular left action of a finite cyclic group on itself,
        equivariant maps are determined uniquely by their value at identity
        and their count is the full codomain size, not its fixed-point count.
  (V)   For a transitive finite group action, equivariant maps are determined
        by the values fixed by one point stabilizer, including non-free cases.
  (VI)  For an arbitrary finite group action, equivariant maps are determined
        by one stabilizer-fixed value per domain orbit and their count is the
        product of the orbitwise fixed-value counts.
  (VII) Stabilizer-fixed seed spaces are transported bijectively between orbit
        representatives; free domain actions and trivial codomain actions both
        reduce the census to |B| raised to the number of domain orbits.
  (VIII) Equivariant relabeling of the domain preserves the complete map space;
         when every point stabilizer imposes one common fixed-value condition,
         the census is the common factor raised to the number of domain orbits.
  (IX)  Equivariant relabeling of the codomain preserves the complete map and
        fixed-seed spaces; domain relabeling induces a bijection of orbit sets,
        and domain/codomain transports commute.
  (X)   Equivariant maps, common-fixed values and point-stabilizer-fixed seeds
        into an indexed product decompose exactly into their coordinate
        families, with product cardinalities and empty-index/factor edges.
  (XI)  Equivariant maps out of an indexed coproduct decompose into component
        families, while the conjugation function-space action identifies
        equivariant maps with fixed points and satisfies equivariant currying.
  Controls:
    * identity alpha can make a diagonal equal a row, but does not create WPS for |B| >= 2;
    * a singleton codomain admits WPS;
    * a three-grade flip fixing the boundary admits invariant valuations, while a
      fixed-point-free three-cycle restores the diagonal escape and no-invariance results.

Deterministic, Python standard library only, exit 0 on success.
"""
from __future__ import annotations

from itertools import product

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  -- ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


def all_T(A, B):
    """All functions T: A x A -> B, represented as dictionaries."""
    pairs = [(a0, a1) for a0 in A for a1 in A]
    for values in product(B, repeat=len(pairs)):
        yield dict(zip(pairs, values))


def all_valuations(A, B):
    """All functions p: A -> B, represented as dictionaries."""
    for values in product(B, repeat=len(A)):
        yield dict(zip(A, values))


def diagonal_escapes_every_row(T, A, alpha):
    diagonal = {x: alpha[T[(x, x)]] for x in A}
    return all(
        any(T[(a0, x)] != diagonal[x] for x in A)
        for a0 in A
    )


def some_T_represents_its_twisted_diagonal(A, B, alpha):
    return any(not diagonal_escapes_every_row(T, A, alpha) for T in all_T(A, B))


def is_weakly_point_surjective(T, A, B):
    valuations = list(all_valuations(A, B))
    return all(
        any(all(T[(a0, x)] == p[x] for x in A) for a0 in A)
        for p in valuations
    )


def some_wps_T(A, B):
    return any(is_weakly_point_surjective(T, A, B) for T in all_T(A, B))


def invariant(p, A, alpha):
    return all(alpha[p[x]] == p[x] for x in A)


def invariant_count(A, B, alpha):
    return sum(invariant(p, A, alpha) for p in all_valuations(A, B))


def cyclic_act(alpha, power, value):
    for _ in range(power):
        value = alpha[value]
    return value


def regular_equivariant(mapping, order, alpha):
    return all(
        mapping[(g + x) % order] == cyclic_act(alpha, g, mapping[x])
        for g in range(order)
        for x in range(order)
    )


def regular_equivariant_maps(order, grades, alpha):
    return [
        mapping
        for mapping in all_valuations(list(range(order)), grades)
        if regular_equivariant(mapping, order, alpha)
    ]


def equivariant(mapping, group, domain, act_domain, act_codomain):
    return all(
        mapping[act_domain(g, a)] == act_codomain(g, mapping[a])
        for g in group
        for a in domain
    )


def equivariant_maps(group, domain, grades, act_domain, act_codomain):
    return [
        mapping
        for mapping in all_valuations(domain, grades)
        if equivariant(mapping, group, domain, act_domain, act_codomain)
    ]


def stabilizer_fixed_values(group, basepoint, grades, act_domain, act_codomain):
    stabilizer = [g for g in group if act_domain(g, basepoint) == basepoint]
    return [b for b in grades if all(act_codomain(g, b) == b for g in stabilizer)]


def orbit_representatives(group, domain, act_domain):
    representatives = []
    seen = set()
    for a in domain:
        if a not in seen:
            representatives.append(a)
            seen.update(act_domain(g, a) for g in group)
    return representatives


def product_action(actions, g, value):
    """Coordinatewise action on a heterogeneous finite product."""
    return tuple(action(g, coordinate) for action, coordinate in zip(actions, value))


B2 = [0, 1]
swap = {0: 1, 1: 0}
ident = {0: 0, 1: 1}

print("[W99] finite-instance confirmation for the diagonal self-valuation paper\n")

print("(I-a) TWISTED DIAGONAL ESCAPE with fixed-point-free alpha:")
for n in (1, 2, 3):
    A = list(range(n))
    check(
        f"|A|={n}: the twisted diagonal escapes every row for every T",
        all(diagonal_escapes_every_row(T, A, swap) for T in all_T(A, B2)),
    )

print("(I-b) NO WEAK POINT-SURJECTIVITY for a non-singleton codomain:")
for n in (1, 2, 3):
    A = list(range(n))
    check(f"|A|={n}, |B|=2: no WPS map A x A -> B", not some_wps_T(A, B2))

print("      Cantor cross-check (no surjection A -> P(A)):")
for n in (1, 2, 3):
    A = list(range(n))
    subsets = [frozenset(x for x in A if bits[x]) for bits in product([0, 1], repeat=n)]
    surjection_exists = any(len(set(assignment)) == len(subsets)
                             for assignment in product(subsets, repeat=n))
    check(f"|A|={n}: no surjection A -> P(A)", not surjection_exists)

print("(II) POINTWISE INVARIANCE CRITERION:")
for n in (1, 2, 3):
    A = list(range(n))
    criterion_holds = all(
        invariant(p, A, swap)
        == all(p[x] in {b for b in B2 if swap[b] == b} for x in A)
        for p in all_valuations(A, B2)
    )
    check(f"|A|={n}: p is invariant iff its image lies in Fix(alpha)", criterion_holds)
    check(
        f"|A|={n}: no swap-invariant valuation",
        not any(invariant(p, A, swap) for p in all_valuations(A, B2)),
    )

print("(III) EXACT FINITE INVARIANT-VALUATION CENSUS:")
finite_actions = (
    ("two-grade swap", B2, swap),
    ("two-grade identity", B2, ident),
    (
        "three-grade boundary-fixing flip",
        ["below", "boundary", "above"],
        {"below": "above", "boundary": "boundary", "above": "below"},
    ),
    (
        "three-grade cycle",
        ["below", "boundary", "above"],
        {"below": "boundary", "boundary": "above", "above": "below"},
    ),
)
for label, grades, alpha in finite_actions:
    fixed_count = sum(alpha[b] == b for b in grades)
    for n in (0, 1, 2, 3):
        domain = list(range(n))
        actual = invariant_count(domain, grades, alpha)
        expected = fixed_count**n
        check(
            f"{label}, |A|={n}: |Inv|=|Fix|^|A|",
            actual == expected,
            f"actual={actual}, expected={fixed_count}^{n}={expected}",
        )

print("CONTROL: identity alpha has fixed points, but WPS remains a separate question:")
A = [0, 1]
check(
    "some T represents its identity-twisted diagonal",
    some_T_represents_its_twisted_diagonal(A, B2, ident),
)
check(
    "constant valuations are identity-invariant",
    invariant({0: 0, 1: 0}, A, ident),
)
check(
    "no WPS map exists for |B|=2 even when alpha is identity",
    not some_wps_T(A, B2),
    "diagonal-row equality is not WPS",
)

print("CONTROL: a singleton codomain admits weak point-surjectivity:")
B1 = [0]
check("the unique T on A={0,1}, B={0} is WPS", some_wps_T(A, B1))

print("CONTROL: three-grade actions distinguish fixed and fixed-point-free cases:")
B3 = ["below", "boundary", "above"]
flip3 = {"below": "above", "boundary": "boundary", "above": "below"}
cycle3 = {"below": "boundary", "boundary": "above", "above": "below"}
boundary_valuation = {0: "boundary", 1: "boundary"}
check("the boundary valuation is flip-invariant", invariant(boundary_valuation, A, flip3))
check(
    "the flip-twisted diagonal can equal a row",
    some_T_represents_its_twisted_diagonal(A, B3, flip3),
    "this defeats only the fixed-point-free diagonal argument",
)
for n in (1, 2):
    A3 = list(range(n))
    check(
        f"|A|={n}: a fixed-point-free three-cycle makes every twisted diagonal escape",
        all(diagonal_escapes_every_row(T, A3, cycle3) for T in all_T(A3, B3)),
    )
    check(
        f"|A|={n}, |B|=3: no WPS map exists",
        not some_wps_T(A3, B3),
    )
    check(
        f"|A|={n}: no three-cycle-invariant valuation",
        not any(invariant(p, A3, cycle3) for p in all_valuations(A3, B3)),
    )

print("(IV) REGULAR-DOMAIN EQUIVARIANT-MAP CLASSIFICATION:")
regular_cases = (
    ("C2 swap", 2, B2, swap),
    ("C2 identity", 2, B2, ident),
    ("C3 cycle", 3, B3, cycle3),
)
for label, order, grades, alpha in regular_cases:
    maps = regular_equivariant_maps(order, grades, alpha)
    identity_values = [mapping[0] for mapping in maps]
    check(
        f"{label}: |Eqv(G,B)|=|B|",
        len(maps) == len(grades),
        f"actual={len(maps)}, expected={len(grades)}",
    )
    check(
        f"{label}: evaluation at identity is bijective",
        sorted(identity_values) == sorted(grades),
    )

check(
    "fixed-point-free C2 swap still has two regular equivariant maps",
    len(regular_equivariant_maps(2, B2, swap)) == 2,
    "domain transport replaces pointwise fixedness",
)
check(
    "an empty codomain has no regular equivariant map",
    len(regular_equivariant_maps(2, [], {})) == 0,
)

print("(V) TRANSITIVE ORBIT-STABILIZER EQUIVARIANT-MAP CLASSIFICATION:")
transitive_cases = (
    (
        "C2 trivial singleton / boundary-fixing flip",
        list(range(2)),
        [0],
        B3,
        lambda _g, _a: 0,
        lambda g, b: cyclic_act(flip3, g, b),
    ),
    (
        "C4 on two cosets / C4 regular codomain",
        list(range(4)),
        list(range(2)),
        list(range(4)),
        lambda g, a: (g + a) % 2,
        lambda g, b: (g + b) % 4,
    ),
    (
        "C4 on two cosets / parity codomain",
        list(range(4)),
        list(range(2)),
        B2,
        lambda g, a: (g + a) % 2,
        lambda g, b: (g + b) % 2,
    ),
)
for label, group, domain, grades, act_domain, act_codomain in transitive_cases:
    maps = equivariant_maps(group, domain, grades, act_domain, act_codomain)
    for basepoint in domain:
        fixed = stabilizer_fixed_values(
            group, basepoint, grades, act_domain, act_codomain
        )
        basepoint_values = [mapping[basepoint] for mapping in maps]
        check(
            f"{label}, basepoint={basepoint}: |Eqv(A,B)|=|B^Stab|",
            len(maps) == len(fixed),
            f"actual={len(maps)}, expected={len(fixed)}",
        )
        check(
            f"{label}, basepoint={basepoint}: evaluation is bijective",
            sorted(basepoint_values) == sorted(fixed),
        )

check(
    "non-free singleton action retains only the boundary value",
    len(equivariant_maps(
        list(range(2)), [0], B3, lambda _g, _a: 0,
        lambda g, b: cyclic_act(flip3, g, b)
    )) == 1,
    "the full stabilizer removes below and above",
)
check(
    "C4 two-coset action can have no equivariant map",
    len(equivariant_maps(
        list(range(4)), list(range(2)), list(range(4)),
        lambda g, a: (g + a) % 2, lambda g, b: (g + b) % 4
    )) == 0,
    "the order-two stabilizer acts fixed-point-freely on the codomain",
)

print("(VI) ARBITRARY-DOMAIN ORBIT-PRODUCT CLASSIFICATION:")
arbitrary_cases = (
    (
        "C2 swap orbit plus fixed point / boundary-fixing flip",
        list(range(2)),
        [0, 1, 2],
        B3,
        lambda g, a: (1 - a) if (g % 2 and a < 2) else a,
        lambda g, b: cyclic_act(flip3, g, b),
    ),
    (
        "two C2-fixed domain points / fixed-point-free codomain",
        list(range(2)),
        [0, 1],
        B2,
        lambda _g, a: a,
        lambda g, b: cyclic_act(swap, g, b),
    ),
    (
        "C4 regular orbit plus two-coset orbit / regular codomain",
        list(range(4)),
        list(range(6)),
        list(range(4)),
        lambda g, a: (g + a) % 4 if a < 4 else 4 + ((g + a - 4) % 2),
        lambda g, b: (g + b) % 4,
    ),
    (
        "empty C2 domain / fixed-point-free codomain",
        list(range(2)),
        [],
        B2,
        lambda _g, a: a,
        lambda g, b: cyclic_act(swap, g, b),
    ),
)
for label, group, domain, grades, act_domain, act_codomain in arbitrary_cases:
    maps = equivariant_maps(group, domain, grades, act_domain, act_codomain)
    representatives = orbit_representatives(group, domain, act_domain)
    fixed_factors = [
        stabilizer_fixed_values(
            group, representative, grades, act_domain, act_codomain
        )
        for representative in representatives
    ]
    expected_count = 1
    for factor in fixed_factors:
        expected_count *= len(factor)
    actual_seeds = sorted(tuple(mapping[a] for a in representatives) for mapping in maps)
    expected_seeds = sorted(product(*fixed_factors))
    check(
        f"{label}: |Eqv(A,B)|=product_orbits |B^Stab|",
        len(maps) == expected_count,
        f"actual={len(maps)}, expected={expected_count}, factors={[len(x) for x in fixed_factors]}",
    )
    check(
        f"{label}: orbit-representative evaluation is bijective",
        actual_seeds == expected_seeds,
    )

check(
    "mixed free/fixed C2 domain has three equivariant maps",
    len(equivariant_maps(
        list(range(2)), [0, 1, 2], B3,
        lambda g, a: (1 - a) if (g % 2 and a < 2) else a,
        lambda g, b: cyclic_act(flip3, g, b)
    )) == 3,
    "the free orbit contributes three seeds and the fixed orbit contributes one",
)
check(
    "the empty domain has one equivariant map as an empty orbit product",
    len(equivariant_maps(
        list(range(2)), [], B2, lambda _g, a: a,
        lambda g, b: cyclic_act(swap, g, b)
    )) == 1,
)

print("(VII) REPRESENTATIVE TRANSPORT AND QUOTIENT CLOSED FORMS:")
representative_transport_cases = (
    (
        "free C2 orbit / boundary-fixing codomain",
        list(range(2)), [0, 1], B3,
        lambda g, a: (g + a) % 2,
        lambda g, b: cyclic_act(flip3, g, b),
        0, 1,
    ),
    (
        "fixed C2 orbit / boundary-fixing codomain",
        list(range(2)), [0], B3,
        lambda _g, _a: 0,
        lambda g, b: cyclic_act(flip3, g, b),
        0, 1,
    ),
)
for label, group, domain, grades, act_domain, act_codomain, a, g in representative_transport_cases:
    source = stabilizer_fixed_values(group, a, grades, act_domain, act_codomain)
    target_a = act_domain(g, a)
    target = stabilizer_fixed_values(group, target_a, grades, act_domain, act_codomain)
    transported = sorted(act_codomain(g, b) for b in source)
    check(
        f"{label}: codomain action transports stabilizer-fixed seeds bijectively",
        transported == sorted(target),
        f"source={source}, transported={transported}, target={target}",
    )
    check(
        f"{label}: orbit-representative seed count is unchanged",
        len(source) == len(target),
    )

free_action_cases = (
    (
        "two free C2 orbits / boundary-fixing codomain",
        list(range(2)), list(range(4)), B3,
        lambda g, a: (a // 2) * 2 + ((a + g) % 2),
        lambda g, b: cyclic_act(flip3, g, b),
    ),
    (
        "two regular C3 orbits / regular codomain",
        list(range(3)), list(range(6)), list(range(3)),
        lambda g, a: (a // 3) * 3 + ((a + g) % 3),
        lambda g, b: (g + b) % 3,
    ),
    (
        "empty free C2 domain / empty codomain",
        list(range(2)), [], [],
        lambda _g, a: a,
        lambda _g, b: b,
    ),
)
for label, group, domain, grades, act_domain, act_codomain in free_action_cases:
    representatives = orbit_representatives(group, domain, act_domain)
    is_free = all(
        g == 0 or act_domain(g, a) != a
        for g in group for a in domain
    )
    actual = len(equivariant_maps(
        group, domain, grades, act_domain, act_codomain
    ))
    expected = len(grades) ** len(representatives)
    check(f"{label}: domain action is free", is_free)
    check(
        f"{label}: |Eqv(A,B)|=|B|^|A/G|",
        actual == expected,
        f"actual={actual}, expected={len(grades)}^{len(representatives)}={expected}",
    )

trivial_codomain_cases = (
    (
        "mixed free/fixed C2 domain / trivial three-value codomain",
        list(range(2)), [0, 1, 2], B3,
        lambda g, a: (1 - a) if (g % 2 and a < 2) else a,
        lambda _g, b: b,
    ),
    (
        "regular-plus-coset C4 domain / trivial two-value codomain",
        list(range(4)), list(range(6)), B2,
        lambda g, a: (g + a) % 4 if a < 4 else 4 + ((g + a - 4) % 2),
        lambda _g, b: b,
    ),
    (
        "empty C2 domain / empty trivial codomain",
        list(range(2)), [], [],
        lambda _g, a: a,
        lambda _g, b: b,
    ),
)
for label, group, domain, grades, act_domain, act_codomain in trivial_codomain_cases:
    representatives = orbit_representatives(group, domain, act_domain)
    is_trivial = all(
        act_codomain(g, b) == b for g in group for b in grades
    )
    actual = len(equivariant_maps(
        group, domain, grades, act_domain, act_codomain
    ))
    expected = len(grades) ** len(representatives)
    check(f"{label}: codomain action is trivial", is_trivial)
    check(
        f"{label}: orbit-constant maps satisfy |Eqv(A,B)|=|B|^|A/G|",
        actual == expected,
        f"actual={actual}, expected={len(grades)}^{len(representatives)}={expected}",
    )

print("(VIII) DOMAIN EQUIVALENCE AND UNIFORM-STABILIZER CLOSED FORM:")
group = list(range(2))
domain = [0, 1, 2]
relabeled_domain = ["left", "right", "fixed"]
domain_equiv = dict(zip(domain, relabeled_domain))
domain_equiv_symm = {value: key for key, value in domain_equiv.items()}
act_domain = lambda g, a: (1 - a) if (g % 2 and a < 2) else a
act_relabeled = lambda g, c: domain_equiv[act_domain(g, domain_equiv_symm[c])]
act_codomain = lambda g, b: cyclic_act(flip3, g, b)
maps = equivariant_maps(group, domain, B3, act_domain, act_codomain)
relabeled_maps = equivariant_maps(
    group, relabeled_domain, B3, act_relabeled, act_codomain
)
transported_maps = {
    tuple(mapping[domain_equiv_symm[c]] for c in relabeled_domain)
    for mapping in maps
}
target_maps = {
    tuple(mapping[c] for c in relabeled_domain) for mapping in relabeled_maps
}
check(
    "mixed C2 action relabeling is equivariant",
    all(
        domain_equiv[act_domain(g, a)] == act_relabeled(g, domain_equiv[a])
        for g in group for a in domain
    ),
)
check(
    "equivariant domain relabeling preserves map cardinality",
    len(maps) == len(relabeled_maps),
    f"source={len(maps)}, target={len(relabeled_maps)}",
)
check(
    "precomposition transports the complete equivariant-map space",
    transported_maps == target_maps,
)

uniform_cases = (
    (
        "two C4 two-coset orbits / parity-flip codomain",
        list(range(4)), list(range(4)), B3,
        lambda g, a: (a // 2) * 2 + ((a + g) % 2),
        lambda g, b: cyclic_act(flip3, g, b),
    ),
    (
        "three fixed C2 points / boundary-fixing codomain",
        list(range(2)), list(range(3)), B3,
        lambda _g, a: a,
        lambda g, b: cyclic_act(flip3, g, b),
    ),
)
for label, group, domain, grades, act_domain, act_codomain in uniform_cases:
    representatives = orbit_representatives(group, domain, act_domain)
    fixed_sets = [
        stabilizer_fixed_values(
            group, a, grades, act_domain, act_codomain
        )
        for a in domain
    ]
    common_factor = fixed_sets[0]
    actual = len(equivariant_maps(
        group, domain, grades, act_domain, act_codomain
    ))
    expected = len(common_factor) ** len(representatives)
    check(
        f"{label}: every point has the same stabilizer-fixed set",
        all(factor == common_factor for factor in fixed_sets),
        f"fixed_sets={fixed_sets}",
    )
    check(
        f"{label}: |Eqv(A,B)|=|B^H|^|A/G|",
        actual == expected,
        f"actual={actual}, expected={len(common_factor)}^{len(representatives)}={expected}",
    )

mixed_group = list(range(2))
mixed_domain = [0, 1, 2]
mixed_fixed_sets = [
    stabilizer_fixed_values(
        mixed_group, a, B3,
        lambda g, x: (1 - x) if (g % 2 and x < 2) else x,
        lambda g, b: cyclic_act(flip3, g, b),
    )
    for a in mixed_domain
]
check(
    "mixed free/fixed domain is rejected by the uniform-stabilizer hypothesis",
    any(factor != mixed_fixed_sets[0] for factor in mixed_fixed_sets[1:]),
    f"fixed_sets={mixed_fixed_sets}",
)

print("(IX) CODOMAIN EQUIVALENCE AND ORBIT-QUOTIENT NATURALITY:")
group = list(range(2))
domain = [0, 1, 2]
relabeled_domain = ["left", "right", "fixed"]
domain_equiv = dict(zip(domain, relabeled_domain))
domain_equiv_symm = {value: key for key, value in domain_equiv.items()}
act_domain = lambda g, a: (1 - a) if (g % 2 and a < 2) else a
act_relabeled = lambda g, c: domain_equiv[act_domain(g, domain_equiv_symm[c])]
act_codomain = lambda g, b: cyclic_act(flip3, g, b)
relabeled_grades = [-1, 0, 1]
codomain_equiv = dict(zip(B3, relabeled_grades))
codomain_equiv_symm = {value: key for key, value in codomain_equiv.items()}
act_relabeled_codomain = lambda g, value: codomain_equiv[
    cyclic_act(flip3, g, codomain_equiv_symm[value])
]
check(
    "boundary-fixing codomain relabeling is equivariant",
    all(
        codomain_equiv[cyclic_act(flip3, g, b)]
        == act_relabeled_codomain(g, codomain_equiv[b])
        for g in group for b in B3
    ),
)
source_maps = equivariant_maps(group, domain, B3, act_domain, act_codomain)
target_maps = equivariant_maps(
    group, domain, relabeled_grades, act_domain, act_relabeled_codomain
)
postcomposed_maps = {
    tuple(codomain_equiv[mapping[a]] for a in domain)
    for mapping in source_maps
}
target_tuples = {
    tuple(mapping[a] for a in domain) for mapping in target_maps
}
check(
    "equivariant codomain relabeling preserves map cardinality",
    len(source_maps) == len(target_maps),
    f"source={len(source_maps)}, target={len(target_maps)}",
)
check(
    "postcomposition transports the complete equivariant-map space",
    postcomposed_maps == target_tuples,
)

source_common_fixed = [
    b for b in B3 if all(cyclic_act(flip3, g, b) == b for g in group)
]
target_common_fixed = [
    b for b in relabeled_grades
    if all(act_relabeled_codomain(g, b) == b for g in group)
]
check(
    "codomain equivalence transports common fixed values",
    sorted(codomain_equiv[b] for b in source_common_fixed)
    == sorted(target_common_fixed),
)
for a in domain:
    source_fixed = stabilizer_fixed_values(
        group, a, B3, act_domain, act_codomain
    )
    target_fixed = stabilizer_fixed_values(
        group, a, relabeled_grades, act_domain, act_relabeled_codomain
    )
    check(
        f"codomain equivalence transports the stabilizer-fixed seed at {a}",
        sorted(codomain_equiv[b] for b in source_fixed) == sorted(target_fixed),
    )

source_orbits = {
    frozenset(act_domain(g, a) for g in group)
    for a in domain
}
target_orbits = {
    frozenset(act_relabeled(g, c) for g in group)
    for c in relabeled_domain
}
transported_orbits = {
    frozenset(domain_equiv[a] for a in orbit) for orbit in source_orbits
}
check(
    "equivariant domain relabeling induces a bijection of orbit quotients",
    transported_orbits == target_orbits,
    f"source={source_orbits}, target={target_orbits}",
)

def transport_domain(mapping):
    return {c: mapping[domain_equiv_symm[c]] for c in relabeled_domain}


def transport_codomain(mapping):
    return {key: codomain_equiv[value] for key, value in mapping.items()}


domain_then_codomain = {
    tuple(transport_codomain(transport_domain(mapping))[c]
          for c in relabeled_domain)
    for mapping in source_maps
}
codomain_then_domain = {
    tuple(transport_domain(transport_codomain(mapping))[c]
          for c in relabeled_domain)
    for mapping in source_maps
}
check(
    "domain precomposition and codomain postcomposition commute",
    domain_then_codomain == codomain_then_domain,
)

print("(X) INDEXED-CODOMAIN PRODUCT PRESERVATION:")
group = list(range(2))
domain = [0, 1, 2]
act_domain = lambda g, a: (1 - a) if (g % 2 and a < 2) else a
component_grades = [B3, B2]
component_actions = [
    lambda g, b: cyclic_act(flip3, g, b),
    lambda _g, b: b,
]
component_maps = [
    equivariant_maps(group, domain, grades, act_domain, action)
    for grades, action in zip(component_grades, component_actions)
]
product_grades = list(product(*component_grades))
act_product = lambda g, value: product_action(component_actions, g, value)
product_maps = equivariant_maps(
    group, domain, product_grades, act_domain, act_product
)
assembled_maps = {
    tuple(tuple(mapping[a] for mapping in family) for a in domain)
    for family in product(*component_maps)
}
actual_product_maps = {
    tuple(mapping[a] for a in domain) for mapping in product_maps
}
check(
    "mixed C2 product: complete equivariant-map space is the coordinate product",
    actual_product_maps == assembled_maps,
)
check(
    "mixed C2 product: equivariant-map cardinalities multiply",
    len(product_maps) == len(component_maps[0]) * len(component_maps[1]) == 12,
    f"combined={len(product_maps)}, factors={[len(maps) for maps in component_maps]}",
)

component_common_fixed = [
    [b for b in grades if all(action(g, b) == b for g in group)]
    for grades, action in zip(component_grades, component_actions)
]
product_common_fixed = [
    value for value in product_grades
    if all(act_product(g, value) == value for g in group)
]
check(
    "mixed C2 product: common-fixed values are coordinatewise",
    set(product_common_fixed) == set(product(*component_common_fixed)),
)
check(
    "mixed C2 product: common-fixed cardinalities multiply",
    len(product_common_fixed)
    == len(component_common_fixed[0]) * len(component_common_fixed[1]) == 2,
)

for basepoint, expected in ((0, 6), (2, 2)):
    component_seeds = [
        stabilizer_fixed_values(
            group, basepoint, grades, act_domain, action
        )
        for grades, action in zip(component_grades, component_actions)
    ]
    product_seeds = stabilizer_fixed_values(
        group, basepoint, product_grades, act_domain, act_product
    )
    check(
        f"mixed C2 product: stabilizer seed at {basepoint} is coordinatewise",
        set(product_seeds) == set(product(*component_seeds)),
    )
    check(
        f"mixed C2 product: stabilizer seed count at {basepoint} multiplies",
        len(product_seeds)
        == len(component_seeds[0]) * len(component_seeds[1]) == expected,
        f"combined={len(product_seeds)}, factors={[len(seed) for seed in component_seeds]}",
    )

empty_index_grades = [()]
empty_index_maps = equivariant_maps(
    group, domain, empty_index_grades, act_domain, lambda _g, value: value
)
check(
    "empty codomain index has exactly one equivariant map",
    len(empty_index_maps) == 1,
)
check(
    "empty codomain index has one common-fixed value",
    len(empty_index_grades) == 1,
)

fixed_domain = [0]
empty_factor_grades = [B2, B2]
empty_factor_actions = [
    lambda g, b: cyclic_act(swap, g, b),
    lambda _g, b: b,
]
empty_factor_product = list(product(*empty_factor_grades))
empty_factor_act = lambda g, value: product_action(
    empty_factor_actions, g, value
)
empty_factor_component_maps = [
    equivariant_maps(
        group, fixed_domain, grades, lambda _g, a: a, action
    )
    for grades, action in zip(empty_factor_grades, empty_factor_actions)
]
empty_factor_product_maps = equivariant_maps(
    group, fixed_domain, empty_factor_product, lambda _g, a: a,
    empty_factor_act,
)
check(
    "one empty equivariant-map factor annihilates the indexed product",
    len(empty_factor_component_maps[0]) == 0
    and len(empty_factor_component_maps[1]) == 2
    and len(empty_factor_product_maps) == 0,
)

print("(XI) DOMAIN COPRODUCTS AND THE EQUIVARIANT INTERNAL HOM:")
group = list(range(2))
coproduct_components = [[0, 1], ["fixed"]]
tagged_domain = [
    (index, value)
    for index, component in enumerate(coproduct_components)
    for value in component
]
component_domain_actions = [
    lambda g, value: 1 - value if g % 2 else value,
    lambda _g, value: value,
]
act_tagged_domain = lambda g, tagged: (
    tagged[0], component_domain_actions[tagged[0]](g, tagged[1])
)
act_codomain = lambda g, value: cyclic_act(flip3, g, value)
coproduct_maps = equivariant_maps(
    group, tagged_domain, B3, act_tagged_domain, act_codomain
)
component_map_spaces = [
    equivariant_maps(group, component, B3, action, act_codomain)
    for component, action in zip(coproduct_components, component_domain_actions)
]
assembled_coproduct_maps = {
    tuple(
        family[index][value]
        for index, component in enumerate(coproduct_components)
        for value in component
    )
    for family in product(*component_map_spaces)
}
actual_coproduct_maps = {
    tuple(mapping[tagged] for tagged in tagged_domain)
    for mapping in coproduct_maps
}
check(
    "heterogeneous C2 coproduct: maps split exactly into component families",
    actual_coproduct_maps == assembled_coproduct_maps,
)
check(
    "heterogeneous C2 coproduct: component map cardinalities multiply",
    len(coproduct_maps)
    == len(component_map_spaces[0]) * len(component_map_spaces[1]) == 3,
    f"combined={len(coproduct_maps)}, factors={[len(maps) for maps in component_map_spaces]}",
)
empty_coproduct_maps = equivariant_maps(
    group, [], [], lambda _g, tagged: tagged, lambda _g, value: value
)
check(
    "empty coproduct has one map even into the empty codomain",
    len(empty_coproduct_maps) == 1,
)
empty_component_spaces = [
    equivariant_maps(group, [], B3, lambda _g, value: value, act_codomain),
    component_map_spaces[1],
]
check(
    "an empty coproduct component contributes the singleton map-space factor",
    len(empty_component_spaces[0]) == 1
    and len(empty_component_spaces[1]) == 1,
)

c3 = list(range(3))
regular3 = list(range(3))
act_regular3 = lambda g, value: (value + g) % 3
function_values = list(product(regular3, repeat=len(regular3)))


def conjugation_function_action(g, values):
    """(g.f)(c) = g.f(g^-1.c) for the regular C3 action."""
    return tuple(
        act_regular3(g, values[(c - g) % 3])
        for c in regular3
    )


fixed_functions = [
    values for values in function_values
    if all(conjugation_function_action(g, values) == values for g in c3)
]
regular_equivariant_functions = equivariant_maps(
    c3, regular3, regular3, act_regular3, act_regular3
)
regular_equivariant_tuples = {
    tuple(mapping[c] for c in regular3)
    for mapping in regular_equivariant_functions
}
check(
    "C3 internal hom: conjugation-fixed functions are exactly equivariant maps",
    set(fixed_functions) == regular_equivariant_tuples,
)
check(
    "C3 internal hom: inverse placement leaves exactly three fixed functions",
    len(fixed_functions) == 3,
)

diagonal_domain = list(product(regular3, regular3))
act_diagonal = lambda g, pair: (
    act_regular3(g, pair[0]), act_regular3(g, pair[1])
)
uncurried_maps = equivariant_maps(
    c3, diagonal_domain, regular3, act_diagonal, act_regular3
)
curried_maps = equivariant_maps(
    c3, regular3, function_values, act_regular3,
    conjugation_function_action,
)
curried_from_uncurried = {
    tuple(
        tuple(mapping[(a, c)] for c in regular3)
        for a in regular3
    )
    for mapping in uncurried_maps
}
actual_curried = {
    tuple(mapping[a] for a in regular3)
    for mapping in curried_maps
}
check(
    "C3 exponential law: currying transports the complete equivariant-map space",
    curried_from_uncurried == actual_curried,
)
check(
    "C3 exponential law: both sides have the predicted 27 maps",
    len(uncurried_maps) == len(curried_maps) == 27,
)

print("\n[verdict]")
print("  Small finite instances confirm the pointwise diagonal and invariance statements.")
print("  They also confirm the exact finite census, including 0^0 = 1 for the")
print("  unique valuation on an empty domain.")
print("  For acted-on domains, they confirm the separate regular-action theorem:")
print("  equivariant maps are seeded freely at identity and counted by |B|.")
print("  For general transitive domains, they confirm the sharper orbit-stabilizer")
print("  theorem: only basepoint values fixed by its stabilizer seed equivariant maps.")
print("  For arbitrary domains, they confirm the orbit-product theorem: each orbit")
print("  contributes its own stabilizer-fixed seed factor, including the empty product.")
print("  Acting between orbit representatives transports those seed factors bijectively.")
print("  Free domain actions and trivial codomain actions both reduce the product to")
print("  |B|^|A/G|, with the empty quotient retaining its unique empty function.")
print("  Equivariant domain relabeling preserves the complete map space, and a uniform")
print("  stabilizer condition reduces the product to |B^H|^|A/G|; a mixed hostile")
print("  control confirms that unequal stabilizer-fixed sets do not satisfy the premise.")
print("  Equivariant codomain relabeling preserves map and fixed-seed spaces; domain")
print("  relabeling transports the orbit quotient, and the two coordinate changes commute.")
print("  Equivariant maps into indexed codomain products decompose coordinatewise, as do")
print("  common-fixed and stabilizer-fixed seeds; finite counts multiply, the empty index")
print("  contributes one map, and an empty component factor annihilates the product.")
print("  Dually, maps out of indexed acted-on coproducts split into component families;")
print("  the empty index and empty components retain their singleton map-space factors.")
print("  The conjugation action on function spaces has exactly the equivariant maps as")
print("  fixed points, and diagonal-domain equivariance is preserved by currying.")
print("  The controls also confirm that representing one twisted diagonal is not WPS and")
print("  that the no-WPS result does not depend on the chosen endomap. Confirmation only:")
print("  the paper's proof is mathematical and does not depend on this run.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = all finite-instance checks passed.")
