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

print("\n[verdict]")
print("  Small finite instances confirm the pointwise diagonal and invariance statements.")
print("  The controls also confirm that representing one twisted diagonal is not WPS and")
print("  that the no-WPS result does not depend on the chosen endomap. Confirmation only:")
print("  the paper's proof is mathematical and does not depend on this run.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = all finite-instance checks passed.")
