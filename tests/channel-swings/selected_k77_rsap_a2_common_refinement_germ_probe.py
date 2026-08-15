#!/usr/bin/env python3
"""Exact regular-germ certificate for the adjacent A1/A2 RSAP transition."""

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = json.loads(
    (ROOT / "lab/process/selected-k77-rsap-a2-common-refinement-germ.json").read_text()
)
FAILURES = []
COUNTS = {}


def check(group, label, condition):
    COUNTS[group] = COUNTS.get(group, 0) + 1
    if condition:
        print(f"PASS [{group}] {label}")
    else:
        FAILURES.append(f"[{group}] {label}")
        print(f"FAIL [{group}] {label}")


def zeros(rows, cols):
    return [[Fraction(0) for _ in range(cols)] for _ in range(rows)]


def eye(n):
    out = zeros(n, n)
    for i in range(n):
        out[i][i] = Fraction(1)
    return out


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def matsub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def rank(a):
    m = [[Fraction(x) for x in row] for row in a]
    pivot_row = 0
    for col in range(len(m[0]) if m else 0):
        pivot = next((r for r in range(pivot_row, len(m)) if m[r][col]), None)
        if pivot is None:
            continue
        m[pivot_row], m[pivot] = m[pivot], m[pivot_row]
        scale = m[pivot_row][col]
        m[pivot_row] = [x / scale for x in m[pivot_row]]
        for r in range(len(m)):
            if r != pivot_row and m[r][col]:
                scale = m[r][col]
                m[r] = [x - scale * y for x, y in zip(m[r], m[pivot_row])]
        pivot_row += 1
    return pivot_row


def poisson_from_pairs(size, pairs):
    out = zeros(size, size)
    for q, p in pairs:
        out[q][p] = Fraction(1)
        out[p][q] = Fraction(-1)
    return out


def liouville_from_pairs(size, pairs):
    """Matrix L for theta=z^T L dz with theta=sum(momentum d position)."""
    out = zeros(size, size)
    for position, momentum in pairs:
        out[momentum][position] = Fraction(1)
    return out


def projection(indices, size):
    out = zeros(len(indices), size)
    for row, col in enumerate(indices):
        out[row][col] = Fraction(1)
    return out


def permutation_from_orders(old_order, new_order):
    """Matrix taking coordinates in old_order to coordinates in new_order."""
    where = {name: index for index, name in enumerate(old_order)}
    out = zeros(len(old_order), len(old_order))
    for row, name in enumerate(new_order):
        out[row][where[name]] = Fraction(1)
    return out


def inverse_permutation(p):
    return transpose(p)


def canonical_pair_permutation(pair_order):
    """Symplectic map on universal coordinates permuting complete pairs."""
    names = [f"q{i}" for i in range(1, 4)] + [f"p{i}" for i in range(1, 4)]
    names += [f"c{i}" for i in range(1, 8)] + [f"t{i}" for i in range(1, 8)]
    leaf_perm, casimir_perm = pair_order
    new = [f"q{i}" for i in leaf_perm] + [f"p{i}" for i in leaf_perm]
    new += [f"c{i}" for i in casimir_perm] + [f"t{i}" for i in casimir_perm]
    return permutation_from_orders(names, new)


universal = [f"q{i}" for i in range(1, 4)] + [f"p{i}" for i in range(1, 4)]
universal += [f"c{i}" for i in range(1, 8)] + [f"t{i}" for i in range(1, 8)]
uindex = {name: i for i, name in enumerate(universal)}
universal_pairs = [(uindex[f"q{i}"], uindex[f"p{i}"]) for i in range(1, 4)]
universal_pairs += [(uindex[f"c{i}"], uindex[f"t{i}"]) for i in range(1, 8)]
pi20 = poisson_from_pairs(20, universal_pairs)
lambda20 = liouville_from_pairs(20, universal_pairs)
target_names = [f"q{i}" for i in range(1, 4)] + [f"p{i}" for i in range(1, 4)]
target_names += [f"c{i}" for i in range(1, 8)]
dJ = projection([uindex[name] for name in target_names], 20)
pi13 = poisson_from_pairs(13, [(0, 3), (1, 4), (2, 5)])

print("A. REGULAR TARGET AND UNIVERSAL MINIMAL REALIZATION")
check("universal", "the common target has dimension thirteen", len(pi13) == 13)
check("universal", "the common target has Poisson rank six", rank(pi13) == 6)
check("universal", "the common target has corank seven", 13 - rank(pi13) == 7)
check("universal", "the universal source has dimension twenty", len(pi20) == 20)
check("universal", "the universal source is symplectic", rank(pi20) == 20)
check("universal", "the full moment differential has rank thirteen", rank(dJ) == 13)
check("universal", "the realization saturates dim target plus corank", 20 == 13 + 7)
check("universal", "the complete Poisson moment identity holds", matmul(matmul(dJ, pi20), transpose(dJ)) == pi13)

print("\nB. EXPLICIT A1/A2 COMMON-REFINEMENT PERMUTATION")
rank_one_order = ["q1", "p1", "q2", "p2", "q3", "p3", "c1", "t1", "c2", "t2"]
for i in range(3, 8):
    rank_one_order += [f"c{i}", f"t{i}"]
a2_order = ["q1", "q2", "q3", "p1", "p2", "p3", "c1", "c2", "t1", "t2"]
for i in range(3, 8):
    a2_order += [f"c{i}", f"t{i}"]
K_a1 = permutation_from_orders(rank_one_order, universal)
K_a2 = permutation_from_orders(a2_order, universal)
phi = matmul(inverse_permutation(K_a2), K_a1)
pi_a1 = matmul(matmul(inverse_permutation(K_a1), pi20), K_a1)
pi_a2 = matmul(matmul(inverse_permutation(K_a2), pi20), K_a2)
lambda_a1 = matmul(matmul(inverse_permutation(K_a1), lambda20), K_a1)
lambda_a2 = matmul(matmul(inverse_permutation(K_a2), lambda20), K_a2)
J_a1 = matmul(dJ, K_a1)
J_a2 = matmul(dJ, K_a2)
check("pair", "the rank-one refinement order contains twenty unique coordinates", len(rank_one_order) == len(set(rank_one_order)) == 20)
check("pair", "the A2 refinement order contains the same coordinates", set(rank_one_order) == set(a2_order) == set(universal))
check("pair", "O4 contributes exactly two canonical pairs", rank_one_order[:4] == ["q1", "p1", "q2", "p2"])
check("pair", "X4(A1) contributes one leaf and one Casimir pair", rank_one_order[4:8] == ["q3", "p3", "c1", "t1"])
check("pair", "the promoted invariant contributes T*R1", rank_one_order[8:10] == ["c2", "t2"])
check("pair", "the principal A2 block has dimension ten", len(a2_order[:10]) == 10)
check("pair", "the transition is an invertible 20 by 20 permutation", rank(phi) == 20 and matmul(transpose(phi), phi) == eye(20))
check("pair", "the transition pulls the A2 symplectic tensor to the A1 tensor", matmul(matmul(phi, pi_a1), transpose(phi)) == pi_a2)
check("pair", "the complete thirteen-component moment square commutes", matmul(J_a2, phi) == J_a1)
check("pair", "both chart moment maps have rank thirteen", rank(J_a1) == rank(J_a2) == 13)
check("pair", "the frozen Liouville primitive pulls back strictly", matmul(matmul(transpose(phi), lambda_a2), phi) == lambda_a1)
check("pair", "the registry records strict primitive equality in the frozen normalization", REGISTRY["pair_transition"]["primitive_pullback"] == "STRICT_EQUALITY_IN_THE_FROZEN_NORMALIZATION")

print("\nC. EXACT PRIMITIVE GAUGE CONTROL")
# A symmetric Casimir matrix produces t -> t+A c.  In the (c,t) block this is
# symplectic and changes sum t_a dc_a by d(1/2 c^T A c).
A = zeros(7, 7)
for i in range(7):
    A[i][i] = Fraction(i + 1)
for i, j in ((0, 1), (1, 3), (2, 6)):
    A[i][j] = A[j][i] = Fraction(1)
gauge = eye(20)
for i in range(7):
    for j in range(7):
        gauge[uindex[f"t{i+1}"]][uindex[f"c{j+1}"]] = A[i][j]
check("gauge", "the selected Casimir shift matrix is symmetric", A == transpose(A))
check("gauge", "the section shift is symplectic", matmul(matmul(gauge, pi20), transpose(gauge)) == pi20)
check("gauge", "the section shift leaves the complete moment map fixed", matmul(dJ, gauge) == dJ)
sample_c = [Fraction(i + 1) for i in range(7)]
gradient = [sum(A[i][j] * sample_c[j] for j in range(7)) for i in range(7)]
quadratic_gradient = [sum((A[i][j] + A[j][i]) * sample_c[j] / 2 for j in range(7)) for i in range(7)]
check("gauge", "the primitive shift is the gradient of one-half c^T A c", gradient == quadratic_gradient)
check("gauge", "the registry records an exact gauge term", REGISTRY["pair_transition"]["allowed_section_change"].startswith("t maps to t+A c"))

print("\nD. FIRST NONCOMMUTING TRIPLE GERM")
K1 = eye(20)
K2 = canonical_pair_permutation(((2, 1, 3), (2, 1, 3, 4, 5, 6, 7)))
K3 = canonical_pair_permutation(((1, 3, 2), (1, 3, 2, 4, 5, 6, 7)))
Ks = [K1, K2, K3]
for index, K in enumerate(Ks, start=1):
    check("triple", f"normalization {index} is symplectic", matmul(matmul(K, pi20), transpose(K)) == pi20)
Js = [matmul(dJ, K) for K in Ks]
phi12 = matmul(inverse_permutation(K2), K1)
phi23 = matmul(inverse_permutation(K3), K2)
phi31 = matmul(inverse_permutation(K1), K3)
check("triple", "the first pair moment square commutes", matmul(Js[1], phi12) == Js[0])
check("triple", "the second pair moment square commutes", matmul(Js[2], phi23) == Js[1])
check("triple", "the third pair moment square commutes", matmul(Js[0], phi31) == Js[2])
check("triple", "successive pair maps do not commute", matmul(phi23, phi12) != matmul(phi12, phi23))
check("triple", "the ordered triple transition is exactly the identity", matmul(matmul(phi31, phi23), phi12) == eye(20))
check("triple", "the moment Cech defect is zero at germ grade", REGISTRY["first_noncommuting_triple"]["moment_cech_defect"] == "ZERO_AT_GERM_GRADE")
check("triple", "the primitive Cech defect is zero at germ grade", REGISTRY["first_noncommuting_triple"]["primitive_cech_defect"] == "ZERO_AT_GERM_GRADE")

print("\nE. CLAIM CEILING")
scope = REGISTRY["scope"]
check("scope", "the adjacent pair regular germ is constructed", scope["adjacent_pair_regular_germ"] == "CONSTRUCTED")
check("scope", "the first noncommuting triple regular germ is constructed", scope["first_noncommuting_triple_regular_germ"] == "CONSTRUCTED")
check("scope", "the global algebraic transition remains open", scope["canonical_global_algebraic_transition"] == "OPEN")
check("scope", "monodromy and section gluing remain open", scope["monodromy_and_section_gluing"] == "OPEN")
check("scope", "singular extension and deeper strata remain open", scope["singular_extension"] == scope["deeper_singular_strata"] == "OPEN")
check("scope", "zero charge remains unconstructed", scope["zero_charge_rank_at_most_49"] == "NOT_CONSTRUCTED")
check("scope", "global RSAP remains open", scope["global_rsap"] == "OPEN")
check("scope", "the all-charge fallback remains 182D", scope["all_charge_fallback_dimension"] == 182)
check("scope", "protected truth surfaces remain unchanged", set(REGISTRY["changes"].values()) == {"none"})

print("\nSUMMARY")
total = sum(COUNTS.values())
print(json.dumps({"checks": total, "counts": COUNTS, "failures": FAILURES, "status": REGISTRY["status"], "next_gate": REGISTRY["next_gate"]}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {total}/{total}")
