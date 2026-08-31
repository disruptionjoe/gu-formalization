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
  (XII) Restriction along a surjective group homomorphism preserves complete
        equivariant-map and fixed-point spaces; non-surjective restriction may
        enlarge them, and explicit coinduction satisfies the finite adjunction.
  (XIII) The balanced-product orbit quotient carries the induced action and
         satisfies the induction-restriction adjunction, including trivial-
         subgroup and nontrivial quotient controls.
  (XIV) Induction along the identity collapses equivariantly to the seed, and
        induction along a composite agrees with nested induction.
  (XV)  For nonnormal subgroups of S3, the K-orbits of the restricted induced
        point carrier are exactly K\\G/H, representative stabilizers equal
        the transported subgroup-intersection condition, and equivariant seed
        maps preserve the canonical Mackey fibers naturally. Distinct
        representatives of one double coset produce equivariantly equivalent
        summands through their common intrinsic fiber.
  Controls:
    * identity alpha can make a diagonal equal a row, but does not create WPS for |B| >= 2;
    * a singleton codomain admits WPS;
    * a three-grade flip fixing the boundary admits invariant valuations, while a
      fixed-point-free three-cycle restores the diagonal escape and no-invariance results.

Deterministic, Python standard library only, exit 0 on success.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

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


def orbit_quotient(group, domain, act_domain):
    """Return finite orbit classes and the class index of every point."""
    classes = []
    class_of = {}
    for point in domain:
        if point in class_of:
            continue
        orbit = tuple(sorted({act_domain(g, point) for g in group}))
        index = len(classes)
        classes.append(orbit)
        for member in orbit:
            class_of[member] = index
    return classes, class_of


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

print("(XII) CHANGE OF ACTING GROUPS AND COINDUCTION:")
c4 = list(range(4))
c2 = list(range(2))
phi_c4_c2 = lambda h: h % 2
act_c2_regular = lambda g, value: (value + g) % 2
act_c4_restricted = lambda h, value: act_c2_regular(phi_c4_c2(h), value)
c2_equivariant = equivariant_maps(
    c2, c2, c2, act_c2_regular, act_c2_regular
)
c4_restricted_equivariant = equivariant_maps(
    c4, c2, c2, act_c4_restricted, act_c4_restricted
)
check(
    "surjective C4 -> C2 restriction preserves the complete map space",
    {
        tuple(mapping[a] for a in c2)
        for mapping in c2_equivariant
    }
    == {
        tuple(mapping[a] for a in c2)
        for mapping in c4_restricted_equivariant
    },
)
check(
    "surjective C4 -> C2 restriction preserves the exact two-map count",
    len(c2_equivariant) == len(c4_restricted_equivariant) == 2,
)
flip3_fixed_under_c2 = [
    value for value in B3
    if all(cyclic_act(flip3, g, value) == value for g in c2)
]
flip3_fixed_under_c4_restriction = [
    value for value in B3
    if all(cyclic_act(flip3, phi_c4_c2(h), value) == value for h in c4)
]
check(
    "surjective restriction preserves the common fixed-point subtype",
    flip3_fixed_under_c2 == flip3_fixed_under_c4_restriction == ["boundary"],
)
trivial_group = [0]
trivially_restricted_maps = equivariant_maps(
    trivial_group, c2, c2,
    lambda _h, value: value,
    lambda _h, value: value,
)
check(
    "non-surjective restriction can strictly enlarge the map space",
    len(c2_equivariant) == 2 and len(trivially_restricted_maps) == 4,
)

# For the unique map 1 -> C2 and a trivial 1-action on B2, the coinduced
# carrier is every function C2 -> B2. C2 acts on those functions by right
# translation, and the adjunction sends f : C2 -> B2 to
# F(a)(g) = f(g + a).
coinduced_carrier = list(product(B2, repeat=len(c2)))
act_coinduced = lambda x, values: tuple(
    values[(g + x) % 2] for g in c2
)
restricted_map_space = list(all_valuations(c2, B2))
coinduced_equivariant_maps = equivariant_maps(
    c2, c2, coinduced_carrier, act_c2_regular, act_coinduced
)
check(
    "trivial-subgroup coinduced carrier contains all four functions",
    len(coinduced_carrier) == 4,
)
check(
    "restriction and coinduction have the same four-map census",
    len(restricted_map_space) == len(coinduced_equivariant_maps) == 4,
)
adjunction_images = {
    tuple(
        tuple(mapping[(g + a) % 2] for g in c2)
        for a in c2
    )
    for mapping in restricted_map_space
}
actual_coinduced_maps = {
    tuple(mapping[a] for a in c2)
    for mapping in coinduced_equivariant_maps
}
check(
    "finite restriction-coinduction formula reaches the complete map space",
    adjunction_images == actual_coinduced_maps,
)
check(
    "evaluation at the identity inverts every finite adjunction image",
    all(
        tuple(image[a][0] for a in c2) ==
        tuple(mapping[a] for a in c2)
        for mapping, image in zip(restricted_map_space, [
            tuple(
                tuple(mapping[(g + a) % 2] for g in c2)
                for a in c2
            )
            for mapping in restricted_map_space
        ])
    ),
)

print("(XIII) INDUCTION AND THE BALANCED-PRODUCT QUOTIENT:")


def finite_induction_control(H, G, B, phi, act_B, act_C):
    """Construct G x_H B and both finite sides of the adjunction."""
    raw_pairs = list(product(G, B))
    act_pair = lambda h, pair: (
        (pair[0] - phi(h)) % len(G),
        act_B(h, pair[1]),
    )
    classes, class_of = orbit_quotient(H, raw_pairs, act_pair)
    quotient = list(range(len(classes)))
    act_induced = lambda x, q: class_of[
        ((x + classes[q][0][0]) % len(G), classes[q][0][1])
    ]
    induced_maps = equivariant_maps(G, quotient, c2, act_induced, act_C)
    act_restricted_C = lambda h, value: act_C(phi(h), value)
    seed_maps = equivariant_maps(H, B, c2, act_B, act_restricted_C)
    evaluated = {
        tuple(mapping[class_of[(0, b)]] for b in B)
        for mapping in induced_maps
    }
    seed_space = {tuple(mapping[b] for b in B) for mapping in seed_maps}
    inverse_images = set()
    inverse_well_defined = True
    for seed in seed_maps:
        values = []
        for orbit in classes:
            candidate_values = {
                act_C(g, seed[b]) for g, b in orbit
            }
            inverse_well_defined &= len(candidate_values) == 1
            values.append(next(iter(candidate_values)))
        inverse_images.add(tuple(values))
    actual_induced = {
        tuple(mapping[q] for q in quotient) for mapping in induced_maps
    }
    return (
        classes,
        induced_maps,
        seed_maps,
        evaluated,
        seed_space,
        inverse_well_defined,
        inverse_images,
        actual_induced,
    )


trivial_induction = finite_induction_control(
    [0], c2, B2, lambda _h: 0,
    lambda _h, value: value,
    act_c2_regular,
)
check(
    "trivial-subgroup induction retains all four raw G x B classes",
    len(trivial_induction[0]) == 4,
)
check(
    "trivial-subgroup induction and restriction have the same four-map census",
    len(trivial_induction[1]) == len(trivial_induction[2]) == 4,
)
check(
    "trivial-subgroup adjunction evaluation reaches every seed map",
    trivial_induction[3] == trivial_induction[4],
)
check(
    "trivial-subgroup inverse is quotient-well-defined and complete",
    trivial_induction[5] and trivial_induction[6] == trivial_induction[7],
)

identity_induction = finite_induction_control(
    c2, c2, c2, lambda h: h,
    act_c2_regular,
    act_c2_regular,
)
check(
    "identity induction collapses four raw pairs to two balanced classes",
    len(identity_induction[0]) == 2,
)
check(
    "nontrivial balanced quotient preserves the complete two-map adjunction",
    len(identity_induction[1]) == len(identity_induction[2]) == 2
    and identity_induction[3] == identity_induction[4]
    and identity_induction[5]
    and identity_induction[6] == identity_induction[7],
)

print("(XIV) INDUCTION IDENTITY AND COMPOSITION COHERENCE:")


def finite_induced_carrier(H, G, B, phi, act_B):
    raw_pairs = list(product(G, B))
    act_pair = lambda h, pair: (
        (pair[0] - phi(h)) % len(G),
        act_B(h, pair[1]),
    )
    classes, class_of = orbit_quotient(H, raw_pairs, act_pair)
    act_induced = lambda x, q: class_of[
        ((x + classes[q][0][0]) % len(G), classes[q][0][1])
    ]
    return classes, class_of, act_induced


identity_classes, identity_class_of, identity_act = finite_induced_carrier(
    c2, c2, c2, lambda g: g, act_c2_regular,
)
identity_values = {
    q: {(g + b) % 2 for g, b in orbit}
    for q, orbit in enumerate(identity_classes)
}
check(
    "identity induction evaluation is well-defined on every balanced class",
    all(len(values) == 1 for values in identity_values.values()),
)
identity_map = {q: next(iter(values)) for q, values in identity_values.items()}
check(
    "identity induction collapses bijectively to the two-point seed",
    len(identity_classes) == 2 and set(identity_map.values()) == set(c2),
)
check(
    "identity induction collapse is C2-equivariant",
    all(
        identity_map[identity_act(g, q)] == act_c2_regular(g, identity_map[q])
        for g in c2 for q in range(len(identity_classes))
    ),
)

K1 = [0]
H2 = c2
G4 = list(range(4))
phi_trivial = lambda _k: 0
psi_double = lambda h: 2 * h
act_k_trivial = lambda _k, value: value
direct_classes, direct_class_of, direct_act = finite_induced_carrier(
    K1, G4, B2, lambda k: psi_double(phi_trivial(k)), act_k_trivial,
)
inner_classes, inner_class_of, inner_act = finite_induced_carrier(
    K1, H2, B2, phi_trivial, act_k_trivial,
)
nested_classes, nested_class_of, nested_act = finite_induced_carrier(
    H2, G4, list(range(len(inner_classes))), psi_double, inner_act,
)
nested_flat_values = {}
for q, outer_orbit in enumerate(nested_classes):
    values = set()
    for g, inner_q in outer_orbit:
        for h, b in inner_classes[inner_q]:
            values.add(direct_class_of[((g + psi_double(h)) % 4, b)])
    nested_flat_values[q] = values
check(
    "nested induction flattening is well-defined across both quotient layers",
    all(len(values) == 1 for values in nested_flat_values.values()),
)
nested_flat_map = {
    q: next(iter(values)) for q, values in nested_flat_values.items()
}
check(
    "direct and iterated induction have the same eight-class carrier",
    len(direct_classes) == len(nested_classes) == 8
    and set(nested_flat_map.values()) == set(range(len(direct_classes))),
)
check(
    "composition flattening is C4-equivariant",
    all(
        nested_flat_map[nested_act(g, q)] == direct_act(g, nested_flat_map[q])
        for g in G4 for q in range(len(nested_classes))
    ),
)

print("(XV) SUBGROUP MACKEY DOUBLE-COSET INTERFACE:")


def perm_mul(p, q):
    """Permutation product p*q: apply q first, then p."""
    return tuple(p[q[i]] for i in range(len(p)))


def perm_inv(p):
    inverse = [0] * len(p)
    for i, image in enumerate(p):
        inverse[image] = i
    return tuple(inverse)


s3 = list(permutations(range(3)))
s3_one = (0, 1, 2)
s3_t01 = (1, 0, 2)
s3_c012 = (1, 2, 0)
K_s3 = [s3_one, s3_t01]
H_s3 = [s3_one, s3_t01]
right_cosets, right_coset_of = orbit_quotient(
    H_s3,
    s3,
    lambda h, g: perm_mul(g, perm_inv(h)),
)
restricted_k_action = lambda k, q: right_coset_of[
    perm_mul(k, right_cosets[q][0])
]
restricted_orbits, restricted_orbit_of = orbit_quotient(
    K_s3,
    list(range(len(right_cosets))),
    restricted_k_action,
)
double_cosets, double_coset_of = orbit_quotient(
    list(product(K_s3, H_s3)),
    s3,
    lambda kh, g: perm_mul(perm_mul(kh[0], g), perm_inv(kh[1])),
)
check(
    "S3 induction from a transposition subgroup has three right cosets",
    len(right_cosets) == 3 and sorted(map(len, right_cosets)) == [2, 2, 2],
)
check(
    "restricted K-action has one fixed coset and one two-coset orbit",
    len(restricted_orbits) == 2
    and sorted(map(len, restricted_orbits)) == [1, 2],
)
check(
    "the explicit left-right action has the two nonnormal S3 double cosets",
    len(double_cosets) == 2 and sorted(map(len, double_cosets)) == [2, 4],
)
orbit_to_double_values = {}
for outer_q, right_coset_indexes in enumerate(restricted_orbits):
    values = {
        double_coset_of[g]
        for right_q in right_coset_indexes
        for g in right_cosets[right_q]
    }
    orbit_to_double_values[outer_q] = values
check(
    "nested restricted-induction orbits map well-definedly and bijectively to double cosets",
    all(len(values) == 1 for values in orbit_to_double_values.values())
    and {
        next(iter(values)) for values in orbit_to_double_values.values()
    } == set(range(len(double_cosets))),
)


def restricted_stabilizer(g):
    q = right_coset_of[g]
    return {k for k in K_s3 if restricted_k_action(k, q) == q}


def transported_intersection(g):
    return {
        k for k in K_s3
        if any(perm_mul(k, g) == perm_mul(g, h) for h in H_s3)
    }


check(
    "the identity-coset stabilizer is the full transported intersection",
    restricted_stabilizer(s3_one) == transported_intersection(s3_one)
    and len(restricted_stabilizer(s3_one)) == 2,
)
check(
    "a nonnormal three-cycle representative has trivial transported stabilizer",
    restricted_stabilizer(s3_c012) == transported_intersection(s3_c012)
    and len(restricted_stabilizer(s3_c012)) == 1,
)


def finite_induced_carrier_group(H, G, B, mul, inv, phi, act_B):
    """Balanced-product induction for a finite group given by operations."""
    raw_pairs = list(product(G, B))
    act_pair = lambda h, pair: (
        mul(pair[0], inv(phi(h))),
        act_B(h, pair[1]),
    )
    classes, class_of = orbit_quotient(H, raw_pairs, act_pair)
    act_induced = lambda x, q: class_of[
        (mul(x, classes[q][0][0]), classes[q][0][1])
    ]
    return classes, class_of, act_induced


act_h_seed = lambda h, b: b if h == s3_one else 1 - b
target_seed_classes, target_seed_class_of, target_seed_act = (
    finite_induced_carrier_group(
        H_s3, s3, B2, perm_mul, perm_inv, lambda h: h, act_h_seed,
    )
)


def transported_h(g, k):
    matches = [
        h for h in H_s3 if perm_mul(k, g) == perm_mul(g, h)
    ]
    assert len(matches) == 1
    return matches[0]


def finite_mackey_summand(g):
    subgroup = [k for k in K_s3 if transported_h_exists(g, k)]
    action = lambda k, b: act_h_seed(transported_h(g, k), b)
    classes, class_of, act = finite_induced_carrier_group(
        subgroup, K_s3, B2, perm_mul, perm_inv, lambda k: k, action,
    )
    image_values = {
        q: {
            target_seed_class_of[(perm_mul(k, g), b)]
            for k, b in orbit
        }
        for q, orbit in enumerate(classes)
    }
    image_map = {
        q: next(iter(values)) for q, values in image_values.items()
    }
    return classes, act, image_values, image_map


def transported_h_exists(g, k):
    return any(perm_mul(k, g) == perm_mul(g, h) for h in H_s3)


identity_summand = finite_mackey_summand(s3_one)
cycle_summand = finite_mackey_summand(s3_c012)
check(
    "nontrivial H-seed induction has six balanced classes",
    len(target_seed_classes) == 6,
)
check(
    "identity representative carries the two-class full-intersection summand",
    len(identity_summand[0]) == 2
    and all(len(values) == 1 for values in identity_summand[2].values()),
)
check(
    "three-cycle representative carries the four-class trivial-intersection summand",
    len(cycle_summand[0]) == 4
    and all(len(values) == 1 for values in cycle_summand[2].values()),
)
check(
    "both nontrivial-seed summand maps are injective",
    len(set(identity_summand[3].values())) == len(identity_summand[0])
    and len(set(cycle_summand[3].values())) == len(cycle_summand[0]),
)
check(
    "the two representative summands partition the complete restricted induction",
    set(identity_summand[3].values()).isdisjoint(
        set(cycle_summand[3].values())
    )
    and set(identity_summand[3].values())
    | set(cycle_summand[3].values())
    == set(range(len(target_seed_classes))),
)
check(
    "the nontrivial-seed summand maps are K-equivariant",
    all(
        summand[3][summand[1](k, q)]
        == target_seed_act(k, summand[3][q])
        for summand in (identity_summand, cycle_summand)
        for k in K_s3
        for q in range(len(summand[0]))
    ),
)

chosen_double_coset_reps = [orbit[0] for orbit in double_cosets]
canonical_double_index = {
    q: double_coset_of[target_seed_classes[q][0][0]]
    for q in range(len(target_seed_classes))
}
canonical_mackey_fibers = {
    double_q: {
        q for q in range(len(target_seed_classes))
        if canonical_double_index[q] == double_q
    }
    for double_q in range(len(double_cosets))
}
check(
    "canonical double-coset fibers partition restricted induction without representatives",
    set().union(*canonical_mackey_fibers.values())
    == set(range(len(target_seed_classes)))
    and sum(len(fiber) for fiber in canonical_mackey_fibers.values())
    == len(target_seed_classes),
)

# A distinct representative of the nontrivial double coset must produce the
# same intrinsic fiber. Inverting its injective assembly map on that fiber
# gives the representative-change equivalence, which must commute with both
# assembly and the left K-action.
cycle_double_q = double_coset_of[s3_c012]
alternate_cycle_rep = next(
    g for g in double_cosets[cycle_double_q] if g != s3_c012
)
alternate_cycle_summand = finite_mackey_summand(alternate_cycle_rep)
alternate_cycle_inverse = {
    target_q: summand_q
    for summand_q, target_q in alternate_cycle_summand[3].items()
}
representative_change = {
    summand_q: alternate_cycle_inverse[target_q]
    for summand_q, target_q in cycle_summand[3].items()
}
check(
    "distinct same-double-coset representatives assemble onto one intrinsic fiber",
    alternate_cycle_rep != s3_c012
    and set(cycle_summand[3].values())
    == set(alternate_cycle_summand[3].values())
    == canonical_mackey_fibers[cycle_double_q],
)
check(
    "representative change is bijective and commutes with assembly",
    len(set(representative_change.values())) == len(cycle_summand[0])
    and all(
        alternate_cycle_summand[3][representative_change[q]]
        == cycle_summand[3][q]
        for q in range(len(cycle_summand[0]))
    ),
)
check(
    "representative-change equivalence is K-equivariant",
    all(
        representative_change[cycle_summand[1](k, q)]
        == alternate_cycle_summand[1](k, representative_change[q])
        for k in K_s3 for q in range(len(cycle_summand[0]))
    ),
)
check(
    "the restricted K-action preserves every canonical double-coset fiber",
    all(
        target_seed_act(k, q) in fiber
        for fiber in canonical_mackey_fibers.values()
        for q in fiber
        for k in K_s3
    ),
)

# The nontrivial seed involution commutes with the H-action. Applying it in
# the seed coordinate must descend to induction, preserve every canonical
# double-coset fiber, commute with K, and square to the identity.
seed_involution = lambda b: 1 - b
induced_seed_map_values = {
    q: {
        target_seed_class_of[(g, seed_involution(b))]
        for g, b in orbit
    }
    for q, orbit in enumerate(target_seed_classes)
}
check(
    "equivariant seed involution descends well-definedly to the balanced quotient",
    all(len(values) == 1 for values in induced_seed_map_values.values()),
)
induced_seed_map = {
    q: next(iter(values)) for q, values in induced_seed_map_values.items()
}
check(
    "induced seed map preserves the intrinsic double-coset index fiberwise",
    all(
        canonical_double_index[induced_seed_map[q]] == canonical_double_index[q]
        for q in range(len(target_seed_classes))
    ),
)
check(
    "induced seed map is K-equivariant and its square is the identity",
    all(
        induced_seed_map[target_seed_act(k, q)]
        == target_seed_act(k, induced_seed_map[q])
        for k in K_s3 for q in range(len(target_seed_classes))
    )
    and all(
        induced_seed_map[induced_seed_map[q]] == q
        for q in range(len(target_seed_classes))
    ),
)
check(
    "canonical fiber assembly is natural under the induced seed map",
    all(
        induced_seed_map[q] in canonical_mackey_fibers[double_q]
        for double_q, fiber in canonical_mackey_fibers.items()
        for q in fiber
    ),
)
chosen_mackey_summands = [
    finite_mackey_summand(g) for g in chosen_double_coset_reps
]
global_mackey_assembly = {
    (double_q, summand_q): summand[3][summand_q]
    for double_q, summand in enumerate(chosen_mackey_summands)
    for summand_q in range(len(summand[0]))
}
check(
    "chosen representatives index exactly their double-coset classes",
    all(
        double_coset_of[g] == double_q
        for double_q, g in enumerate(chosen_double_coset_reps)
    ),
)
check(
    "the chosen-summand coproduct assembles bijectively onto restricted induction",
    len(set(global_mackey_assembly.values()))
    == len(global_mackey_assembly)
    == len(target_seed_classes)
    and set(global_mackey_assembly.values())
    == set(range(len(target_seed_classes))),
)
check(
    "the global Mackey coproduct assembly is K-equivariant and index-preserving",
    all(
        global_mackey_assembly[(double_q, summand[1](k, summand_q))]
        == target_seed_act(
            k, global_mackey_assembly[(double_q, summand_q)]
        )
        for double_q, summand in enumerate(chosen_mackey_summands)
        for k in K_s3
        for summand_q in range(len(summand[0]))
    ),
)

print("(XVIII) FINITE-ACTION BURNSIDE MACKEY CONTROLS:")


def burnside_orbit_signature(carrier, action):
    """Orbit-size multiset: an additive finite K-set isomorphism invariant."""
    orbits, _ = orbit_quotient(K_s3, list(carrier), action)
    return tuple(sorted(len(orbit) for orbit in orbits))


restricted_burnside_signature = burnside_orbit_signature(
    range(len(target_seed_classes)), target_seed_act,
)
summand_burnside_signatures = [
    burnside_orbit_signature(range(len(summand[0])), summand[1])
    for summand in chosen_mackey_summands
]
coproduct_burnside_signature = tuple(
    sorted(size for signature in summand_burnside_signatures for size in signature)
)
check(
    "Burnside addition is disjoint coproduct on nonnormal-S3 orbit signatures",
    coproduct_burnside_signature == restricted_burnside_signature,
)
check(
    "restriction after induction has the complete transported-intersection Burnside class",
    len(global_mackey_assembly) == len(target_seed_classes)
    and coproduct_burnside_signature == restricted_burnside_signature,
)
check(
    "omitting either double-coset transfer summand changes the Burnside class",
    all(signature != restricted_burnside_signature
        for signature in summand_burnside_signatures),
)
check(
    "the Burnside double-coset identity preserves total carrier cardinality",
    sum(restricted_burnside_signature)
    == sum(sum(signature) for signature in summand_burnside_signatures)
    == len(target_seed_classes),
)

# Hom-form Mackey control. Use a three-point K-set whose nonidentity element
# swaps 0 and 1 and fixes 2. Restriction to each transported intersection
# gives one seed-map factor, and the global equivalence must identify the
# complete K-equivariant map space with the Cartesian product of those factors.
mackey_codomain = tuple(range(3))
mackey_codomain_act = lambda k, c: (
    c if k == s3_one or c == 2 else 1 - c
)


def enumerate_equivariant_maps(domain, codomain, acting_group, act_domain, act_codomain):
    maps = []
    for values in product(codomain, repeat=len(domain)):
        if all(
            values[act_domain(group_element, x)]
            == act_codomain(group_element, values[x])
            for group_element in acting_group
            for x in domain
        ):
            maps.append(values)
    return maps


restricted_induced_homs = enumerate_equivariant_maps(
    range(len(target_seed_classes)),
    mackey_codomain,
    K_s3,
    target_seed_act,
    mackey_codomain_act,
)
mackey_seed_hom_factors = []
for representative in chosen_double_coset_reps:
    intersection = [
        k for k in K_s3 if transported_h_exists(representative, k)
    ]
    transported_seed_act = lambda k, b, representative=representative: (
        act_h_seed(transported_h(representative, k), b)
    )
    mackey_seed_hom_factors.append(
        enumerate_equivariant_maps(
            B2,
            mackey_codomain,
            intersection,
            transported_seed_act,
            mackey_codomain_act,
        )
    )


def restrict_mackey_hom_to_seeds(values):
    return tuple(
        tuple(values[target_seed_class_of[(representative, b)]] for b in B2)
        for representative in chosen_double_coset_reps
    )


restricted_seed_families = {
    restrict_mackey_hom_to_seeds(values)
    for values in restricted_induced_homs
}
all_seed_families = set(product(*mackey_seed_hom_factors))
check(
    "Hom-form Mackey factors have the expected nonnormal S3 cardinalities",
    [len(factor) for factor in mackey_seed_hom_factors] == [3, 9]
    and len(restricted_induced_homs) == 27,
)
check(
    "restriction to transported seeds realizes the complete Hom-form Mackey product",
    restricted_seed_families == all_seed_families
    and len(restricted_seed_families) == len(restricted_induced_homs),
)
check(
    "a non-equivariant target map cannot masquerade as a complete Mackey seed family",
    any(
        restrict_mackey_hom_to_seeds(values) not in all_seed_families
        for values in product(mackey_codomain, repeat=len(target_seed_classes))
        if values not in restricted_induced_homs
    ),
)

# Free-module Mackey linearization control. A finitely supported coefficient
# vector on the canonical coproduct is pushed forward by summing coefficients
# over equal images. The canonical assembly is bijective, so support and
# coefficients are preserved exactly; naturality and K-equivariance are the
# linear extensions of the already-checked basis squares.
def linearize_finite_map(vector, mapping):
    out = {}
    for basis, coefficient in vector.items():
        image = mapping[basis] if isinstance(mapping, dict) else mapping(basis)
        out[image] = out.get(image, 0) + coefficient
        if out[image] == 0:
            del out[image]
    return out


assembly_inverse = {
    target: source for source, target in global_mackey_assembly.items()
}
canonical_seed_map = {
    source: assembly_inverse[induced_seed_map[target]]
    for source, target in global_mackey_assembly.items()
}
canonical_identity_map = {source: source for source in global_mackey_assembly}
restricted_induced_identity_map = {
    target: target for target in range(len(target_seed_classes))
}
check(
    "canonical Mackey and restricted-induction action functors preserve identity",
    all(canonical_identity_map[source] == source for source in canonical_identity_map)
    and all(
        restricted_induced_identity_map[target] == target
        for target in restricted_induced_identity_map
    ),
)
check(
    "canonical Mackey and restricted-induction action functors preserve composition",
    all(
        canonical_seed_map[canonical_seed_map[source]] == source
        for source in canonical_seed_map
    )
    and all(
        induced_seed_map[induced_seed_map[target]] == target
        for target in induced_seed_map
    ),
)
check(
    "canonical Mackey assembly is a natural isomorphism on every action carrier",
    all(
        global_mackey_assembly[canonical_seed_map[source]]
        == induced_seed_map[global_mackey_assembly[source]]
        for source in global_mackey_assembly
    ),
)

# The ordinary category of supplied actions is not preadditive. Already for
# the trivial group, there is no total map from the nonempty one-point action
# to the empty action, while a preadditive category would supply a zero
# morphism between every pair of objects.
trivial_point_carrier = (0,)
trivial_empty_carrier = ()
point_to_empty_maps = [
    values
    for values in product(trivial_empty_carrier, repeat=len(trivial_point_carrier))
]
empty_to_point_maps = list(
    product(trivial_point_carrier, repeat=len(trivial_empty_carrier))
)
check(
    "the raw action category has no point-to-empty morphism",
    trivial_point_carrier
    and not trivial_empty_carrier
    and point_to_empty_maps == [],
)
check(
    "the empty-to-point direction retains its unique empty map",
    empty_to_point_maps == [()],
)

# Free additivization replaces each raw hom-set by finitely supported integer
# combinations. The empty point-to-empty generator set therefore has one
# element, the zero combination, while a bijective Mackey assembly extends
# coefficientwise and additively.
point_to_empty_free_hom = [{}]
check(
    "the free additive envelope has exactly the formal zero point-to-empty morphism",
    point_to_empty_maps == [] and point_to_empty_free_hom == [{}],
)
free_left = dict(list(global_mackey_assembly.items())[:2])
free_vector_a = {source: coefficient for source, coefficient in zip(free_left, (2, -1))}
free_vector_b = {source: coefficient for source, coefficient in zip(free_left, (-3, 4))}
free_vector_sum = {
    source: free_vector_a.get(source, 0) + free_vector_b.get(source, 0)
    for source in free_left
}
check(
    "canonical Mackey assembly extends additively to formal integer combinations",
    linearize_finite_map(free_vector_sum, global_mackey_assembly)
    == {
        target:
        linearize_finite_map(free_vector_a, global_mackey_assembly).get(target, 0)
        + linearize_finite_map(free_vector_b, global_mackey_assembly).get(target, 0)
        for target in free_left.values()
    },
)

# A one-dimensional exact instance of the general observation-pullback
# obstruction: the normal gamma map is invertible, the ambient trace cancels,
# and literal pullback retains the nonzero horizontal trace.
horizontal_trace = 2
normal_gamma = 3
normal_inverse_of_horizontal_trace = Fraction(horizontal_trace, normal_gamma)
ambient_trace = horizontal_trace - normal_gamma * normal_inverse_of_horizontal_trace
check("ambient gamma-kernel lift cancels exactly", ambient_trace == 0)
check("literal observation retains nonzero horizontal trace", horizontal_trace != 0)

# Finite representation-support mirror of the Lean adjoint/144 certificate.
family_partner_support = {"45", "54", "210", "945", "1050"}
symmetric_adjoint_support = {"1", "54", "210", "770"}
alternating_adjoint_support = {"45", "945"}
ps_singlets = {"45": 0, "54": 1, "210": 1, "945": 0, "1050": 0}
symmetric_owners = family_partner_support & symmetric_adjoint_support
alternating_owners = family_partner_support & alternating_adjoint_support
check("cubic adjoint channel is available", "45" in family_partner_support)
check("linear adjoint background has no PS singlet", ps_singlets["45"] == 0)
check("symmetric quadratic owners are exactly 54 and 210", symmetric_owners == {"54", "210"})
check("alternating quadratic owners are exactly 45 and 945", alternating_owners == {"45", "945"})
check("only symmetric owners preserve PS", all(ps_singlets[x] == 1 for x in symmetric_owners) and all(ps_singlets[x] == 0 for x in alternating_owners))
free_mackey_vector = {(0, 0): 2, (1, 1): -3, (1, 3): 5}
assembled_free_mackey_vector = linearize_finite_map(
    free_mackey_vector, global_mackey_assembly
)
check(
    "free-module Mackey assembly preserves every basis coefficient and support size",
    len(assembled_free_mackey_vector) == len(free_mackey_vector)
    and all(
        assembled_free_mackey_vector[global_mackey_assembly[source]] == coefficient
        for source, coefficient in free_mackey_vector.items()
    ),
)
check(
    "free-module Mackey assembly is natural under the linearized seed map",
    linearize_finite_map(
        linearize_finite_map(free_mackey_vector, canonical_seed_map),
        global_mackey_assembly,
    )
    == linearize_finite_map(assembled_free_mackey_vector, induced_seed_map),
)
def canonical_mackey_k_action(k):
    return {
        (double_q, summand_q): (
            double_q,
            chosen_mackey_summands[double_q][1](k, summand_q),
        )
        for double_q, summand in enumerate(chosen_mackey_summands)
        for summand_q in range(len(summand[0]))
    }


def restricted_induced_k_action(k):
    return {
        target: target_seed_act(k, target)
        for target in range(len(target_seed_classes))
    }


for k in K_s3:
    canonical_k_action = canonical_mackey_k_action(k)
    target_k_action = restricted_induced_k_action(k)
    check(
        f"free-module Mackey assembly intertwines the K action for {k}",
        linearize_finite_map(
            linearize_finite_map(free_mackey_vector, canonical_k_action),
            global_mackey_assembly,
        )
        == linearize_finite_map(assembled_free_mackey_vector, target_k_action),
    )

# Bundled permutation-representation controls. The basis permutations must
# satisfy the group identity and multiplication laws, and canonical assembly
# must be an intertwiner for the complete representation rather than one
# isolated action check.
canonical_identity_action = canonical_mackey_k_action(s3_one)
target_identity_action = restricted_induced_k_action(s3_one)
check(
    "canonical and restricted-induced permutation representations preserve identity",
    all(canonical_identity_action[x] == x for x in canonical_identity_action)
    and all(target_identity_action[x] == x for x in target_identity_action),
)
check(
    "canonical and restricted-induced permutation representations preserve multiplication",
    all(
        canonical_mackey_k_action(perm_mul(k, l))[x]
        == canonical_mackey_k_action(k)[canonical_mackey_k_action(l)[x]]
        for k in K_s3
        for l in K_s3
        for x in canonical_identity_action
    )
    and all(
        restricted_induced_k_action(perm_mul(k, l))[x]
        == restricted_induced_k_action(k)[restricted_induced_k_action(l)[x]]
        for k in K_s3
        for l in K_s3
        for x in target_identity_action
    ),
)
check(
    "canonical Mackey assembly is an intertwiner on every representation basis vector",
    all(
        global_mackey_assembly[canonical_mackey_k_action(k)[x]]
        == restricted_induced_k_action(k)[global_mackey_assembly[x]]
        for k in K_s3
        for x in canonical_identity_action
    ),
)

# A hostile would-be generator that collapses two basis vectors cannot square
# to the identity, so it cannot define the C2 permutation representation.
hostile_generator_action = dict(canonical_mackey_k_action(s3_t01))
hostile_generator_action[(1, 3)] = hostile_generator_action[(1, 1)]
check(
    "a nonbijective hostile generator fails the permutation-representation group law",
    any(
        hostile_generator_action[hostile_generator_action[x]] != x
        for x in hostile_generator_action
    ),
)

# Hostile noninjective basis transport merges two coefficients and therefore
# fails the support-preservation conclusion required of an equivalence.
hostile_basis_collapse = dict(global_mackey_assembly)
hostile_basis_collapse[(1, 3)] = hostile_basis_collapse[(1, 1)]
check(
    "a noninjective hostile basis transport cannot preserve free-module support",
    len(linearize_finite_map(free_mackey_vector, hostile_basis_collapse))
    < len(free_mackey_vector),
)

print("(XVI) FINITE PROOF-STABLE KERNEL CERTIFICATES:")

shiab_dimensions = {
    "spin_plus": 64,
    "spin_minus": 64,
    "vector_spin_plus": 832,
    "vector_spin_minus": 832,
    "two_form_spin_plus": 4928,
    "two_form_spin_minus": 4928,
}
shiab_source = {
    "+": {"spin_plus": 1, "vector_spin_minus": 1, "two_form_spin_plus": 1},
    "-": {"spin_minus": 1, "vector_spin_plus": 1, "two_form_spin_minus": 1},
}
shiab_target = {
    "+": {"spin_minus": 1, "vector_spin_plus": 1},
    "-": {"spin_plus": 1, "vector_spin_minus": 1},
}


def representation_dimension(row):
    return sum(
        multiplicity * shiab_dimensions[label]
        for label, multiplicity in row.items()
    )


def schur_overlap(source, target):
    return sum(
        source.get(label, 0) * target.get(label, 0)
        for label in shiab_dimensions
    )


shiab_blocks = {
    (source_chirality, target_chirality): schur_overlap(
        shiab_source[source_chirality], shiab_target[target_chirality]
    )
    for source_chirality in ("+", "-")
    for target_chirality in ("+", "-")
}
check(
    "supplied Shiab decomposition rows have the declared product dimensions",
    all(representation_dimension(row) == 91 * 64 for row in shiab_source.values())
    and all(representation_dimension(row) == 14 * 64 for row in shiab_target.values()),
)
check(
    "Shiab Schur overlap gives zero same-chirality blocks and two cross blocks",
    shiab_blocks == {("+", "+"): 0, ("+", "-"): 2, ("-", "+"): 2, ("-", "-"): 0},
)
check(
    "the supplied full-Dirac Shiab multiplicity is four and not unique",
    sum(shiab_blocks.values()) == 4 and shiab_blocks[("+", "-")] != 1,
)

# Scalar exact control for the abstract block-kernel theorem.  With E=1,
# A=5, B=2, C=3, the Schur complement is -1 and the only integer kernel
# point in a symmetric witness box is zero.
block_kernel = [
    (x, y)
    for x in range(-8, 9)
    for y in range(-8, 9)
    if 5 * x + 2 * y == 0 and 3 * x + y == 0
]
check(
    "invertible E and injective Schur complement give a trivial block kernel",
    block_kernel == [(0, 0)],
)
singular_block_witness = (0, 1)
check(
    "a singular eliminated block can carry a nonzero kernel witness",
    singular_block_witness != (0, 0)
    and 1 * singular_block_witness[0] + 0 * singular_block_witness[1] == 0
    and 0 * singular_block_witness[0] + 0 * singular_block_witness[1] == 0,
)

print("(XVII) OBSERVATION DESCENT AND PAIRED REAL-SECTOR CONTROLS:")

# gamma_A(x,y)=x+y has right inverse s |-> (s,0).  The good observation is
# exactly gamma_A, so it preserves the kernel and factors through gamma_A.
ambient_gamma = lambda v: v[0] + v[1]
right_inverse = lambda s: (s, 0)
good_observation = lambda v: v[0] + v[1]
hostile_observation = lambda v: v[0]
factor = lambda s: good_observation(right_inverse(s))
descent_box = [(x, y) for x in range(-4, 5) for y in range(-4, 5)]
check(
    "split-surjective kernel preservation agrees with explicit factorization",
    all(
        good_observation(v) == factor(ambient_gamma(v))
        for v in descent_box
    )
    and all(
        ambient_gamma(v) != 0 or good_observation(v) == 0
        for v in descent_box
    ),
)
check(
    "a hostile observation that does not factor fails kernel preservation",
    ambient_gamma((1, -1)) == 0 and hostile_observation((1, -1)) != 0,
)

chirality = lambda v: (v[0], -v[1])
conjugation = lambda v: (v[1], v[0])
hostile_conjugation = lambda v: v
sample = [(x, y) for x in range(-3, 4) for y in range(-3, 4)]
check(
    "swap conjugation is involutive and anticommutes with chirality",
    all(conjugation(conjugation(v)) == v for v in sample)
    and all(
        chirality(conjugation(v))
        == tuple(-z for z in conjugation(chirality(v)))
        for v in sample
    ),
)
check(
    "anticommuting conjugation exchanges plus and minus sectors",
    chirality(conjugation((2, 0)))
    == tuple(-z for z in conjugation((2, 0)))
    and chirality(conjugation((0, 3))) == conjugation((0, 3))
    and chirality(hostile_conjugation((2, 0)))
    != tuple(-z for z in hostile_conjugation((2, 0))),
)

print("(XIX) FINITE SPAN-CATEGORY CONTROLS:")

# For trivial actions, an isomorphism class of finite spans A <- X -> B is
# exactly a matrix of natural-number fiber multiplicities. Pullback
# composition counts matching middle fibers, hence is matrix multiplication.
def span_comp(left, right):
    return [
        [sum(left[i][j] * right[j][k] for j in range(len(right)))
         for k in range(len(right[0]))]
        for i in range(len(left))
    ]


span_ab = [[1, 2, 0], [0, 1, 1]]
span_bc = [[1, 0], [2, 1], [1, 3]]
span_cd = [[2, 1], [0, 1]]
id_a = [[1, 0], [0, 1]]
id_b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
check(
    "finite span pullback composition has identity multiplicity matrices",
    span_comp(id_a, span_ab) == span_ab
    and span_comp(span_ab, id_b) == span_ab,
)
check(
    "finite span pullback composition is associative on nontrivial fibers",
    span_comp(span_comp(span_ab, span_bc), span_cd)
    == span_comp(span_ab, span_comp(span_bc, span_cd)),
)
hostile_entrywise = [
    [span_ab[i][j] * span_bc[i][j]
     for j in range(min(len(span_ab[0]), len(span_bc[0])))]
    for i in range(min(len(span_ab), len(span_bc)))
]
check(
    "hostile entrywise pairing is not span pullback composition",
    hostile_entrywise != span_comp(span_ab, span_bc),
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
print("  Surjective change of acting groups preserves complete map and fixed-point")
print("  spaces, non-surjective restriction need not, and right-translation coinduction")
print("  realizes the restriction-coinduction adjunction on the finite controls.")
print("  The balanced-product quotient carries the complementary induced action, and")
print("  evaluation on [1,b] realizes the induction-restriction adjunction, including")
print("  trivial-subgroup and nontrivial quotient controls with explicit inverse.")
print("  Identity induction collapses equivariantly to its seed, while nested")
print("  induction flattens equivariantly to induction along the composite map.")
print("  For nonnormal S3 subgroups, restricted point induction has exactly the")
print("  double-coset orbit partition and the transported-intersection stabilizers.")
print("  With a nontrivial two-point H-seed, the transported-intersection inductions")
print("  map injectively and K-equivariantly to disjoint two- and four-class summands")
print("  whose union is the complete six-class restricted induced carrier.")
print("  Equivariant seed maps descend to that carrier, preserve its intrinsic")
print("  double-coset fibers, commute with K, and act naturally on canonical assembly.")
print("  Distinct representatives of one double coset give equivariantly equivalent")
print("  summands through the same intrinsic fiber, with assembly unchanged.")
print("  The Hom-form Mackey map space is the product of transported-intersection")
print("  seed-map factors; the nonnormal S3 control realizes 27 = 3 x 9 exactly.")
print("  Free-module linearization preserves canonical Mackey basis coefficients,")
print("  support size, seed-map naturality and K-equivariance; a noninjective hostile")
print("  basis transport fails the support law as required.")
print("  The linearized K-actions satisfy the representation identity and product laws,")
print("  canonical assembly is a representation intertwiner on every basis vector, and")
print("  a nonbijective hostile generator fails the C2 group law as required.")
print("  At action-functor level, identity and composition are preserved and canonical")
print("  assembly satisfies the complete naturality square before linearization.")
print("  The raw supplied-action category has no point-to-empty morphism, so it is")
print("  not preadditive and the current natural isomorphism is not yet an additive")
print("  Mackey functor; an additive span/transfer completion remains separate work.")
print("  Its free integer-linear envelope adds the unique formal zero in the empty")
print("  hom-set and lifts canonical Mackey assembly coefficientwise and additively,")
print("  without manufacturing span morphisms or restriction/transfer structure.")
print("  The finite-action Burnside group now makes disjoint coproduct additive and")
print("  descends subgroup restriction and induction; the nonnormal-S3 control checks")
print("  that restriction after induction is exactly the 2+4 double-coset coproduct.")
print("  Omitting either transported-intersection transfer summand changes its class.")
print("  The supplied Shiab decomposition rows dimension-check and their Schur overlap")
print("  gives the chiral matrix [[0,2],[2,0]] and full-Dirac total four.")
print("  A determinant-free scalar block control confirms the explicit E-inverse and")
print("  injective-Schur hypotheses, while a singular-E witness shows the premise matters.")
print("  Split-surjective observation preserves the ambient kernel exactly through the")
print("  displayed factorization control; a hostile nonfactorizing observation leaks it.")
print("  Involutive swap conjugation anticommutes with chirality and exchanges its two")
print("  eigensectors; commuting identity conjugation is rejected by the hostile control.")
print("  Arbitrary finite spans compose by pullback: on trivial actions their fiber")
print("  multiplicity matrices have exact identity and associativity laws, while a")
print("  hostile entrywise pairing is rejected as the wrong composition.")
print("  The controls also confirm that representing one twisted diagonal is not WPS and")
print("  that the no-WPS result does not depend on the chosen endomap. Confirmation only:")
print("  the paper's proof is mathematical and does not depend on this run.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = all finite-instance checks passed.")
