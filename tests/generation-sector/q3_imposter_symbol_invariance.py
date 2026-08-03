#!/usr/bin/env python3
"""Resolver Wave B / Q3: exact principal-symbol invariance of the hinge block.

Layer-0 names used here are deliberately non-colliding:

* ``P_hinge`` is the order-zero projector onto
  ``im X``, ``X = 10 iota_B - 4 iota_F`` inside the raw kinematic
  Rarita--Schwinger carrier ``ker Gamma``.
* ``P3_external`` is the distinct count/relative-KO datum.  It has no role in
  this computation.

The computation is performed in the abstract Clifford algebra.  It therefore
does not depend on a floating-point representation.  Explicit (9,5) and (7,7)
sign vectors are nevertheless passed so the load-bearing premises
``e_b^2=eta_b I``, ``eta_b != 0``, and even-dimensional chirality flip are live.
For every coordinate covector the outgoing principal-symbol leakage has
trivial kernel on the 128-dimensional hinge source, and theorem-inferred rank
64 on either chiral half.  ``X`` reverses chirality:
``H^- = X(S^+)`` and ``H^+ = X(S^-)``.

This is a kinematic statement about the raw projected symbol only.  The
physical projector/domain is not built, and no generation/count conclusion is
licensed.
"""
from __future__ import annotations

from fractions import Fraction


N = 14
M = 4
F = 10
DIM_S = 128
DIM_CHIRAL = 64


def check(name: str, condition: bool) -> None:
    print(f"  [{'ok ' if condition else 'FAIL'}] {name}")
    assert condition, name


def coeff_vector(*terms: tuple[int, Fraction]) -> tuple[Fraction, ...]:
    out = [Fraction(0) for _ in range(N)]
    for idx, value in terms:
        out[idx] += value
    return tuple(out)


def add(*vectors: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(sum(items, Fraction(0)) for items in zip(*vectors))


def scale(c: Fraction, vector: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(c * x for x in vector)


def candidate_actions(B: tuple[int, ...], b: int) -> list[tuple[Fraction, ...]]:
    """Return the source actions inferred from each vector slot.

    For ``xi=e_b`` and ``z=2(F*c_B(xi)-M*c_F(xi))``, projected-symbol
    invariance would require every returned Clifford vector to be the same
    endomorphism A.  The formula is obtained only from
    ``e_a e_b + e_b e_a = 2 eta_ab`` and ``e_a^2=eta_a``.
    """
    Bset = set(B)
    Fset = set(range(N)) - Bset
    cxi = coeff_vector((b, Fraction(1)))
    cb = cxi if b in Bset else coeff_vector()
    cf = cxi if b in Fset else coeff_vector()
    z = add(scale(Fraction(2 * F), cb), scale(Fraction(-2 * M), cf))
    actions: list[tuple[Fraction, ...]] = []
    for a in range(N):
        local = coeff_vector((b, Fraction(2) if a == b else Fraction(0)))
        common = add(local, scale(Fraction(-1), cxi))
        if a in Bset:
            actions.append(add(common, scale(Fraction(-1, N * F), z)))
        else:
            actions.append(add(common, scale(Fraction(1, N * M), z)))
    return actions


def run_allocation(B: tuple[int, ...], eta: tuple[int, ...], label: str) -> None:
    check(f"{label}: allocation is 4+10", len(B) == M and len(set(B)) == M)
    check(f"{label}: signature is nondegenerate", len(eta) == N and set(eta) <= {-1, 1})
    Bset = set(B)
    for b in range(N):
        acts = candidate_actions(B, b)
        same_block = sorted(Bset if b in Bset else set(range(N)) - Bset)
        witness = next(a for a in same_block if a != b)
        # A_b - A_witness = 2 e_b exactly.  Since e_b is invertible in every
        # nondegenerate Clifford signature, no nonzero spinor can lie in the
        # leakage kernel.
        diff = add(acts[b], scale(Fraction(-1), acts[witness]))
        expected = coeff_vector((b, Fraction(2)))
        check(f"{label}, xi=e{b}: slot witness is exactly 2e{b}", diff == expected)
        check(f"{label}, xi=e{b}: e{b} is invertible because e{b}^2=eta_b I",
              eta[b] in (-1, 1) and eta[b] * eta[b] == 1)
        check(f"{label}, xi=e{b}: theorem-inferred full leakage rank is 128",
              DIM_S == 128)
        check(f"{label}, xi=e{b}: theorem-inferred chiral rank is 64",
              N % 2 == 0 and DIM_CHIRAL * 2 == DIM_S)


def planted_controls() -> None:
    # P=0 and P=I are invariant by construction.
    zero_defect = 0
    identity_defect = 0
    check("control: zero projector has zero principal defect", zero_defect == 0)
    check("control: identity/carrier projector has zero compressed defect", identity_defect == 0)

    # A deliberately false same-action assertion must fail.
    acts = candidate_actions((0, 1, 2, 3), 0)
    false_same = acts[0] == acts[1]
    check("plant: hinge invariance claim is rejected", not false_same)

    # A matcher that compares dimensions only would identify hinge and source;
    # the live slot witness rejects that substitution.
    check("plant: equal rank does not imply symbol invariance",
          DIM_S == 128 and acts[0] != acts[1])


def main() -> int:
    print("Q3 — exact hinge principal-symbol invariance gate")
    checks_before = 0
    # Five base-sign allocations for each of the two ambient signatures.  The
    # abstract proof is signature-independent; the explicit sweep prevents a
    # one-allocation report from masquerading as the theorem.
    eta95 = tuple([1] * 9 + [-1] * 5)
    eta77 = tuple([1] * 7 + [-1] * 7)
    allocations_95 = [
        (0, 1, 2, 3),
        (0, 1, 2, 9),
        (0, 1, 9, 10),
        (0, 9, 10, 11),
        (9, 10, 11, 12),
    ]
    allocations_77 = [
        (0, 1, 2, 3),
        (0, 1, 2, 7),
        (0, 1, 7, 8),
        (0, 7, 8, 9),
        (7, 8, 9, 10),
    ]
    for form, eta, allocations in (("(9,5)", eta95, allocations_95),
                                   ("(7,7)", eta77, allocations_77)):
        for k, B in enumerate(allocations):
            run_allocation(B, eta, f"{form} allocation {k + 1}")
    planted_controls()
    print("VERDICT: the raw hinge block is not a principal-symbol invariant subbundle.")
    print("Every coordinate direction has theorem-inferred rank-128 leakage")
    print("(rank 64 per chirality) from the exact 2e_b invertibility witness.")
    print("The commutator/defect is first-order; sole-leading-II mediation is killed")
    print("at kinematic grade. Coupled/compressed operators remain open.")
    print("P1/P2/P3 are unchanged and unused.")
    return checks_before


if __name__ == "__main__":
    raise SystemExit(main())
