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
print("  The controls also confirm that representing one twisted diagonal is not WPS and")
print("  that the no-WPS result does not depend on the chosen endomap. Confirmation only:")
print("  the paper's proof is mathematical and does not depend on this run.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = all finite-instance checks passed.")
