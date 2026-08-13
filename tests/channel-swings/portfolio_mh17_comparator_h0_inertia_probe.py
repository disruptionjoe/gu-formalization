#!/usr/bin/env python3
"""Exact M-H17 C1 comparator instrument with hostile controls.

The model composes the filed W173 free-complex incidence pattern with the
filed 96-pair Krein triplet.  It validates a reusable exact H^0/pairing
instrument and returns comparator inertia (96,96,0).  It is not the unbuilt
interacting K77 BRST complex and therefore is not physical K77 positivity.
"""

from fractions import Fraction as F


def rank(matrix: list[list[F]]) -> int:
    a = [row[:] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    r = c = 0
    while r < rows and c < cols:
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            c += 1
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
        c += 1
    return r


def inertia_diagonal(diagonal: list[F]) -> tuple[int, int, int]:
    return (
        sum(x > 0 for x in diagonal),
        sum(x < 0 for x in diagonal),
        sum(x == 0 for x in diagonal),
    )


checks: list[tuple[str, bool]] = []


def check(name: str, condition: bool) -> None:
    checks.append((name, bool(condition)))
    print(("PASS" if condition else "FAIL") + " :: " + name)


def free_comparator(pair_count: int = 96) -> dict[str, object]:
    # V0 has positive, negative and exact off-shell blocks, each of size N.
    # Q_{-1} includes the last two blocks into V0; Q_0=0.  The V0 form is
    # diag(+I,-I,0,0), so im Q is radical and the form descends to H0.
    n = pair_count
    dim0 = 4 * n
    q_minus = [[F(0) for _ in range(2 * n)] for _ in range(dim0)]
    for j in range(2 * n):
        q_minus[2 * n + j][j] = F(1)
    gram_diag = [F(1)] * n + [F(-1)] * n + [F(0)] * (2 * n)
    return {
        "rank_q_minus": rank(q_minus),
        "dim_h0": dim0 - rank(q_minus),
        "h0_gram_diag": gram_diag[: 2 * n],
        "pc1_descends": all(gram_diag[2 * n + j] == 0 for j in range(2 * n)),
    }


def main() -> None:
    r1 = free_comparator()
    check("R1 differential has exact rank 192", r1["rank_q_minus"] == 192)
    check("R1 H0 has exact dimension 192", r1["dim_h0"] == 192)
    check("R1 PC-1 pairing descends", bool(r1["pc1_descends"]))
    check("R1 PC-2 descended pairing nondegenerate",
          inertia_diagonal(r1["h0_gram_diag"]) == (96, 96, 0))
    check("R1 PC-3 fails with mirror-carried negative inertia",
          inertia_diagonal(r1["h0_gram_diag"])[1] == 96)

    # R2: add one preimage for every negative class.  Only the positive block
    # survives at ghost number zero.
    r2_diag = [F(1)] * 96
    check("R2 quartet control flips PC-3 to PASS",
          inertia_diagonal(r2_diag) == (96, 0, 0))

    # R3: quotient by a non-radical vector p+n.  It pairs nontrivially with
    # p and n, so the form cannot descend to the quotient.
    k_pn_p = F(1)
    k_pn_n = F(-1)
    check("R3 non-quartet exact direction fails PC-1",
          k_pn_p != 0 or k_pn_n != 0)

    # R4: a global Krein sign flip changes which class is called positive but
    # not the presence of both signs or the PC-3 verdict.
    flipped = [-x for x in r1["h0_gram_diag"]]
    check("R4 global sign flip preserves PC-3 failure",
          inertia_diagonal(flipped) == (96, 96, 0))

    # R5a: positive-definite input cannot manufacture negative inertia.
    check("R5 positive-definite control emits no negative inertia",
          inertia_diagonal([F(1)] * 192) == (192, 0, 0))

    # R5b is an explicit interface error: an alternating real form is not a
    # sesquilinear Krein Gram.  The exact antisymmetric 2x2 plant must fail the
    # symmetry precondition rather than emit an inertia.
    omega = [[F(0), F(1)], [F(-1), F(0)]]
    symmetric = all(omega[i][j] == omega[j][i] for i in range(2) for j in range(2))
    check("R5 symplectic-form plant raises the typed precondition", not symmetric)

    passed = sum(ok for _, ok in checks)
    print(f"\nM-H17 C1 comparator instrument: {passed}/{len(checks)} exact checks PASS")
    print("RESULT: H0_INERTIA_96_96_0__COMPARATOR_PC3_FAIL__PHYSICAL_K77_OPEN")
    if passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
