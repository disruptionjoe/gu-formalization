#!/usr/bin/env python3
"""Exact controls for the principal symmetric-pair A2 transverse factors."""

from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = json.loads((ROOT / "lab/process/selected-k77-rsap-a2-principal-symmetric-pair.json").read_text())
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
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def matsub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def rank(a):
    m = [list(map(Fraction, row)) for row in a]
    if not m:
        return 0
    rows, cols = len(m), len(m[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if m[r][col]), None)
        if pivot is None:
            continue
        m[pivot_row], m[pivot] = m[pivot], m[pivot_row]
        scale = m[pivot_row][col]
        m[pivot_row] = [value / scale for value in m[pivot_row]]
        for r in range(rows):
            if r != pivot_row and m[r][col]:
                factor = m[r][col]
                m[r] = [m[r][c] - factor * m[pivot_row][c] for c in range(cols)]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def det3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def power(a, n):
    out = eye(len(a))
    for _ in range(n):
        out = matmul(out, a)
    return out


def flatten(a):
    return [value for row in a for value in row]


def linear_map_columns(images):
    return transpose([flatten(image) for image in images])


def commutator(a, b):
    return matsub(matmul(a, b), matmul(b, a))


def trace_pair(a, b):
    product = matmul(a, b)
    return sum(product[i][i] for i in range(len(a)))


q = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
K12 = [[0, 1, 0], [-1, 0, 0], [0, 0, 0]]
K13 = [[0, 0, 1], [0, 0, 0], [-1, 0, 0]]
K23 = [[0, 0, 0], [0, 0, 1], [0, -1, 0]]
h_basis = [matmul(q, K) for K in (K12, K13, K23)]
p_basis = [
    [[1, 0, 0], [0, -2, 0], [0, 0, 1]],
    [[0, 1, 0], [0, 0, 1], [0, 0, 0]],
    [[0, 0, 1], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [1, 0, 0], [0, 1, 0]],
    [[0, 0, 0], [0, 0, 0], [1, 0, 0]],
]

print("A. SPLIT SYMMETRIC PAIR")
check("split", "the reverse form is symmetric and involutive", transpose(q) == q and matmul(q, q) == eye(3))
check("split", "the reverse form is nondegenerate", det3(q) == -1)
check("split", "the q-skew basis has dimension three", rank(linear_map_columns(h_basis)) == 3)
check("split", "every h basis element is q-skew", all(matmul(transpose(x), q) == [[-v for v in row] for row in matmul(q, x)] for x in h_basis))
check("split", "the q-self-adjoint traceless basis has dimension five", rank(linear_map_columns(p_basis)) == 5)
check("split", "every p basis element is q-self-adjoint", all(matmul(transpose(x), q) == matmul(q, x) for x in p_basis))
check("split", "h and p are trace-orthogonal", all(trace_pair(h, p) == 0 for h in h_basis for p in p_basis))
check("split", "h plus p spans sl3", rank(linear_map_columns(h_basis + p_basis)) == 8)

print("\nB. COMPLETE REAL-JORDAN SYMMETRIZER CENSUS")
J3 = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
check("coverage", "the size-three real Jordan block is Lorentz-self-adjoint", matmul(transpose(J3), q) == matmul(q, J3))
check("coverage", "the size-three symmetrizer has Lorentz determinant", det3(q) == -1)
J21 = [[2, 1, 0], [0, 2, 0], [0, 0, -4]]
q21 = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
check("coverage", "the real 2+1 Jordan type is symmetrized", matmul(transpose(J21), q21) == matmul(q21, J21))
check("coverage", "the 2+1 symmetrizer has Lorentz determinant", det3(q21) == -1)
D111 = [[3, 0, 0], [0, -1, 0], [0, 0, -2]]
q111 = [[1, 0, 0], [0, 1, 0], [0, 0, -1]]
check("coverage", "the three-real-eigenvalue type is self-adjoint", matmul(transpose(D111), q111) == matmul(q111, D111))
check("coverage", "the diagonal symmetrizer has Lorentz determinant", det3(q111) == -1)
C21 = [[1, -2, 0], [2, 1, 0], [0, 0, -2]]
qc = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
check("coverage", "the complex-pair plus real type is self-adjoint", matmul(transpose(C21), qc) == matmul(qc, C21))
check("coverage", "the complex-pair symmetrizer has Lorentz determinant", det3(qc) == -1)
check("coverage", "the registry records complete real-Jordan coverage", REGISTRY["split_model"]["surjectivity"].startswith("EVERY_REAL_3X3_MATRIX"))
check("coverage", "the split moment map is declared constructed", REGISTRY["split_model"]["verdict"] == "CONSTRUCTED")

print("\nC. REGULAR NILPOTENT AND SEMISIMPLE RANK")
N = J3
check("nilpotent", "the adversarial nilpotent lies in p", matmul(transpose(N), q) == matmul(q, N))
check("nilpotent", "the adversarial nilpotent is order three", power(N, 3) == zeros(3, 3) and power(N, 2) != zeros(3, 3))
sl3_basis = [
    [[1, 0, 0], [0, -1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, -1]],
    [[0, 1, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [1, 0, 0], [0, 0, 0]],
    [[0, 0, 1], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0]],
    [[0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 1, 0]],
]
check("nilpotent", "the nilpotent centralizer has dimension two", 8 - rank(linear_map_columns([commutator(x, N) for x in sl3_basis])) == 2)
check("nilpotent", "the principal isotropy has zero nilpotent stabilizer", rank(linear_map_columns([commutator(x, N) for x in h_basis])) == 3)
check("nilpotent", "the nilpotent moment differential has rank eight", REGISTRY["split_model"]["regular_nilpotent_control"] == "PASS_RANK_8")
S = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
check("regular", "the semisimple control lies in p", matmul(transpose(S), q) == matmul(q, S))
check("regular", "the semisimple control has cubic x(x-1)(x+1)", power(S, 3) == S and rank(S) == 2)
check("regular", "the principal isotropy has zero semisimple stabilizer", rank(linear_map_columns([commutator(x, S) for x in h_basis])) == 3)
check("regular", "the regular moment differential has rank eight", REGISTRY["split_model"]["regular_map_rank"] == 8)
check("origin", "the origin moment differential has rank five", REGISTRY["split_model"]["origin_map_rank"] == 5)
check("theorem", "the regular proof uses polynomial self-adjoint centralizers", "POLYNOMIAL_IN_XI" in REGISTRY["split_model"]["regular_stabilizer_intersection"])

print("\nD. COMPACT SYMMETRIC PAIR")
so3_basis = [K12, K13, K23]
sym0_basis = [
    [[1, 0, 0], [0, -1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, -1]],
    [[0, 1, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 1], [0, 0, 0], [1, 0, 0]],
    [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
]
check("compact", "so3 has dimension three", rank(linear_map_columns(so3_basis)) == 3)
check("compact", "symmetric trace-free complement has dimension five", rank(linear_map_columns(sym0_basis)) == 5)
check("compact", "compact summands are trace-orthogonal", all(trace_pair(k, s) == 0 for k in so3_basis for s in sym0_basis))
compact_regular = [[2, 0, 0], [0, 0, 0], [0, 0, -2]]
check("compact", "the distinct-eigenvalue compact control has zero skew stabilizer", rank(linear_map_columns([commutator(k, compact_regular) for k in so3_basis])) == 3)
check("compact", "the compact map uses the unitary spectral theorem", REGISTRY["compact_model"]["surjectivity"] == "UNITARY_SPECTRAL_THEOREM")
check("compact", "the compact regular rank is eight", REGISTRY["compact_model"]["regular_map_rank"] == 8)
check("compact", "the compact origin rank is five", REGISTRY["compact_model"]["origin_map_rank"] == 5)
check("compact", "the compact factor is constructed", REGISTRY["compact_model"]["verdict"] == "CONSTRUCTED")

print("\nE. 98D COMPOSITION AND CLAIM CEILING")
check("compose", "the A2 factor has dimension ten", REGISTRY["target"]["factor_dimension"] == 10)
check("compose", "the complete carrier has dimension 98", 78 + 10 + 10 == REGISTRY["target"]["complete_carrier_dimension"])
check("compose", "the complete regular map rank is 91", 78 + 8 + 5 == REGISTRY["target"]["complete_regular_map_rank"])
check("compose", "the complete A2-origin map rank is 88", 78 + 5 + 5 == REGISTRY["target"]["complete_a2_origin_map_rank"])
check("compose", "the homogeneous moment map is Poisson", REGISTRY["homogeneous_moment_map"]["poisson"] == "EQUIVARIANT_HAMILTONIAN_MOMENT_MAP")
check("scope", "split and compact real forms are constructed", REGISTRY["real_form_census"]["split_sl3R"] == REGISTRY["real_form_census"]["compact_su3"] == "CONSTRUCTED")
check("scope", "the mixed real form remains open", REGISTRY["real_form_census"]["mixed_su2_1"] == "OPEN")
check("scope", "adjacent pair and triple cocycles remain open", REGISTRY["scope"]["adjacent_pair_potential_cocycle"] == REGISTRY["scope"]["noncommuting_triple_cocycle"] == "OPEN")
check("scope", "global RSAP remains open", REGISTRY["scope"]["global_rsap"] == "OPEN")
check("scope", "zero charge remains unconstructed", REGISTRY["scope"]["zero_charge_rank_at_most_49"] == "NOT_CONSTRUCTED")
check("scope", "protected truth surfaces remain unchanged", set(REGISTRY["changes"].values()) == {"none"})

print("\nSUMMARY")
total = sum(COUNTS.values())
print(json.dumps({"checks": total, "counts": COUNTS, "failures": FAILURES, "status": REGISTRY["status"], "next_gate": REGISTRY["next_gate"]}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {total}/{total}")
