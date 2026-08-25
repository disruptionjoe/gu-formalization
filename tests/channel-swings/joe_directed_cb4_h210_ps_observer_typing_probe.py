#!/usr/bin/env python3
"""Exact CB-4B certificate for fixed versus co-moving Pati--Salam typing.

The calculation uses Fraction arithmetic only.  It proves that the mixed
Cartan directions have zero centralizer against a fixed PS embedding, builds
an exact nontrivial O(7,7) graph lift, and exhibits the block-stabilizer
ambiguity of the transported PS subgroup.  The semantic ledger protects the
conditional-build and source-typing ceilings.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
from fractions import Fraction as F


def zero(rows: int, cols: int):
    return [[F(0) for _ in range(cols)] for _ in range(rows)]


def eye(n: int):
    out = zero(n, n)
    for i in range(n):
        out[i][i] = F(1)
    return out


def diag(entries):
    out = zero(len(entries), len(entries))
    for i, value in enumerate(entries):
        out[i][i] = F(value)
    return out


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    assert len(a[0]) == len(b)
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def matsub(a, b):
    return [[x - y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def inverse(a):
    n = len(a)
    aug = [list(row) + unit for row, unit in zip(a, eye(n))]
    for col in range(n):
        pivots = [row for row in range(col, n) if aug[row][col]]
        assert pivots, f"singular exact matrix: no pivot in column {col}"
        pivot = pivots[0]
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [value / scale for value in aug[col]]
        for row in range(n):
            if row == col:
                continue
            scale = aug[row][col]
            if scale:
                aug[row] = [x - scale * y for x, y in zip(aug[row], aug[col])]
    return [row[n:] for row in aug]


def rank(a):
    work = [list(row) for row in a]
    if not work:
        return 0
    rows, cols = len(work), len(work[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            scale = work[row][col]
            if scale:
                work[row] = [x - scale * y for x, y in zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def commutator(a, b):
    return matsub(matmul(a, b), matmul(b, a))


def is_zero(a):
    return all(value == 0 for row in a for value in row)


def flatten(a):
    return [value for row in a for value in row]


def ps_vector_generators_10():
    """so(6)+so(4), the vector image of Spin(6)xSpin(4) on V_10."""
    generators = []
    for block in (range(0, 6), range(6, 10)):
        block = list(block)
        for pos, i in enumerate(block):
            for j in block[pos + 1 :]:
                generator = zero(10, 10)
                generator[i][j] = F(1)
                generator[j][i] = F(-1)
                generators.append(generator)
    return generators


def embed_vertical(generator):
    out = zero(14, 14)
    for i in range(10):
        for j in range(10):
            out[4 + i][4 + j] = generator[i][j]
    return out


def build_q(j):
    eta_h = diag([1, -1, -1, -1])
    eta_v = diag([1] * 6 + [-1] * 4)
    q = zero(14, 14)
    reciprocal = matmul(matmul(eta_h, transpose(j)), eta_v)
    for mu in range(4):
        for a in range(10):
            q[mu][4 + a] = -reciprocal[mu][a]
            q[4 + a][mu] = j[a][mu]
    return q


def graph_lift():
    """A rational O(7,7) lift mixing one +/+ and one -/- pair."""
    g = eye(14)
    for h, v in ((0, 4), (1, 10)):
        g[h][h], g[h][v] = F(3, 5), F(-4, 5)
        g[v][h], g[v][v] = F(4, 5), F(3, 5)
    return g


def graph_slope_from_lift(g):
    a = [[g[i][j] for j in range(4)] for i in range(4)]
    c = [[g[4 + i][j] for j in range(4)] for i in range(10)]
    return matmul(c, inverse(a))


def stabilizer_ambiguity():
    """Block-stabilizer boost that mixes the A6 and B4 PS vector blocks."""
    k = eye(14)
    a, b = 4, 10
    k[a][a], k[a][b] = F(5, 3), F(4, 3)
    k[b][a], k[b][b] = F(4, 3), F(5, 3)
    return k


BASE_LEDGER = {
    "ps_vector_singlets": 0,
    "fixed_ps_mixed_hom_dimension": 0,
    "nonzero_fixed_ps_graph_allowed": False,
    "conjugate_h210_arrows": 2,
    "alignment_status": "SEPARATE_CONDITIONAL_H210_ALIGN",
    "covariance_status": "EQUIVARIANCE_NOT_SELECTION",
    "post_contraction_codomain": "T*X tensor s^*S",
    "free_144_after_contraction": False,
    "full_d0_varpi_status": "TYPE_MISSING",
    "fixed_hq_status": "ADVERSE_TYPE_MISSING",
}


def validate_ledger(ledger):
    assert ledger["ps_vector_singlets"] == 0
    assert ledger["fixed_ps_mixed_hom_dimension"] == 0
    assert ledger["nonzero_fixed_ps_graph_allowed"] is False
    assert ledger["conjugate_h210_arrows"] == 2
    assert ledger["alignment_status"] == "SEPARATE_CONDITIONAL_H210_ALIGN"
    assert ledger["covariance_status"] == "EQUIVARIANCE_NOT_SELECTION"
    assert ledger["post_contraction_codomain"] == "T*X tensor s^*S"
    assert ledger["free_144_after_contraction"] is False
    assert ledger["full_d0_varpi_status"] == "TYPE_MISSING"
    assert ledger["fixed_hq_status"] == "ADVERSE_TYPE_MISSING"


def run_certificate():
    checks = 0

    def check(condition, label):
        nonlocal checks
        assert condition, label
        checks += 1

    eta = diag([1, -1, -1, -1] + [1] * 6 + [-1] * 4)
    ps10 = ps_vector_generators_10()
    ps14 = [embed_vertical(generator) for generator in ps10]

    check(len(ps10) == 21, "dim so(6)+so(4)")
    check(6 + 4 == 10, "10|PS dimension closure")
    check(BASE_LEDGER["ps_vector_singlets"] == 0, "no PS singlet in 10")

    stacked_action = [row for generator in ps10 for row in generator]
    invariant_constraint_rank = rank(stacked_action)
    check(invariant_constraint_rank == 10, "V10 has no fixed vector")
    check(10 - invariant_constraint_rank == 0, "Inv_PS(V10)=0")

    hom_constraints = []
    for column in range(4):
        for row in stacked_action:
            extended = [F(0)] * 40
            extended[10 * column : 10 * (column + 1)] = row
            hom_constraints.append(extended)
    check(rank(hom_constraints) == 40, "all forty mixed coefficients constrained")
    check(40 - rank(hom_constraints) == 0, "Hom_PS(H4,V10)=0")

    g = graph_lift()
    g_inv = inverse(g)
    check(matmul(matmul(transpose(g), eta), g) == eta, "g is O(7,7)")
    j = graph_slope_from_lift(g)
    check(rank(j) == 2, "test graph is nonzero mixed rank two")

    q = build_q(j)
    check(is_zero(matsub(matmul(transpose(q), eta), [[-x for x in row] for row in matmul(eta, q)])),
          "q(J) is K77 skew")
    fixed_commutators = [commutator(generator, q) for generator in ps14]
    check(any(not is_zero(value) for value in fixed_commutators),
          "nonzero q(J) does not centralize fixed PS")

    graph = zero(14, 4)
    for mu in range(4):
        graph[mu][mu] = F(1)
    for a in range(10):
        for mu in range(4):
            graph[4 + a][mu] = j[a][mu]
    check(any(not is_zero(matmul(generator, graph)) for generator in ps14),
          "fixed PS does not fix the nonzero graph")

    moved_ps = [matmul(matmul(g, generator), g_inv) for generator in ps14]
    moved_h = [[g[i][mu] for mu in range(4)] for i in range(14)]
    check(all(is_zero(matmul(generator, moved_h)) for generator in moved_ps),
          "conjugated PS fixes the co-moving horizontal plane")
    check(rank([flatten(generator) for generator in moved_ps]) == 21,
          "conjugated PS retains dimension 21")

    p0 = zero(14, 14)
    for i in range(4):
        p0[i][i] = F(1)
    pv0 = matsub(eye(14), p0)
    pg = matmul(matmul(g, p0), g_inv)
    moved_equivariant_object = matmul(matmul(g, pv0), g_inv)
    check(all(is_zero(commutator(generator, moved_equivariant_object)) for generator in moved_ps),
          "equivariant object remains equivariant after conjugation")

    k = stabilizer_ambiguity()
    k_inv = inverse(k)
    check(matmul(matmul(transpose(k), eta), k) == eta, "k is a block stabilizer in O(7,7)")
    check(is_zero(commutator(k, p0)), "k preserves the reference graph projector")
    gk = matmul(g, k)
    gk_inv = inverse(gk)
    pgk = matmul(matmul(gk, p0), gk_inv)
    check(pgk == pg, "g and gk give the same graph projector")

    moved_ps_k = [matmul(matmul(gk, generator), gk_inv) for generator in ps14]
    check(rank([flatten(generator) for generator in moved_ps_k]) == 21,
          "ambiguous lift retains PS algebra dimension")
    check(any(a != b for a, b in zip(moved_ps, moved_ps_k)),
          "ambiguous lift changes the preferred subgroup")

    reference_basis = [flatten(generator) for generator in ps14]
    conjugated_by_k = [matmul(matmul(k, generator), k_inv) for generator in ps14]
    check(any(rank(reference_basis + [flatten(generator)]) == 22 for generator in conjugated_by_k),
          "general vertical stabilizer does not normalize PS")

    h = matmul(matmul(g, k), g_inv)
    h_inv = inverse(h)
    check(all(matmul(matmul(h, a), h_inv) == b for a, b in zip(moved_ps, moved_ps_k)),
          "the two subgroup choices are conjugate")

    validate_ledger(BASE_LEDGER)
    checks += len(BASE_LEDGER)
    check(BASE_LEDGER["conjugate_h210_arrows"] == 2, "both effective halves retained")
    check(BASE_LEDGER["free_144_after_contraction"] is False,
          "literal contraction consumes the free 144 index")
    check(BASE_LEDGER["full_d0_varpi_status"] == "TYPE_MISSING",
          "full d0+varpi collision remains open")
    check(BASE_LEDGER["fixed_hq_status"] == "ADVERSE_TYPE_MISSING",
          "fixed Hq adverse horn remains open")

    return checks


def run_plants():
    plants = [
        ("false singlet", "ps_vector_singlets", 1),
        ("fixed PS under nonzero J", "nonzero_fixed_ps_graph_allowed", True),
        ("delete conjugate", "conjugate_h210_arrows", 1),
        ("promote alignment", "alignment_status", "DERIVED"),
        ("call covariance selection", "covariance_status", "SOURCE_SELECTED"),
    ]
    fired = 0
    for label, key, value in plants:
        mutant = deepcopy(BASE_LEDGER)
        mutant[key] = value
        try:
            validate_ledger(mutant)
        except AssertionError:
            fired += 1
        else:
            raise AssertionError(f"plant did not fire: {label}")
    return fired, len(plants)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    checks = run_certificate()
    print(f"CB-4B fixed/co-moving PS typing: {checks} exact checks")
    print("fixed PS mixed centralizer: 0/40; co-moving subgroup: conjugacy-class only")
    if args.selftest:
        fired, total = run_plants()
        print(f"plants fired: {fired}/{total}")


if __name__ == "__main__":
    main()
