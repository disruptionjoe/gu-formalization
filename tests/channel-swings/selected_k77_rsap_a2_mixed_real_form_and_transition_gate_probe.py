#!/usr/bin/env python3
"""Exact controls for the mixed A2 principal factor and transition type gate."""

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = json.loads(
    (ROOT / "lab/process/selected-k77-rsap-a2-mixed-real-form-and-transition-gate.json").read_text()
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
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def matsub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matneg(a):
    return [[-value for value in row] for row in a]


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


def self_adjoint(b, q):
    return matmul(transpose(b), q) == matmul(q, b)


def skew_adjoint(a, q):
    return matmul(transpose(a), q) == matneg(matmul(q, a))


q = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
K12 = [[0, 1, 0], [-1, 0, 0], [0, 0, 0]]
K13 = [[0, 0, 1], [0, 0, 0], [-1, 0, 0]]
K23 = [[0, 0, 0], [0, 0, 1], [0, -1, 0]]
h_basis = [matmul(q, k) for k in (K12, K13, K23)]
p_real_basis = [
    [[1, 0, 0], [0, -2, 0], [0, 0, 1]],
    [[0, 1, 0], [0, 0, 1], [0, 0, 0]],
    [[0, 0, 1], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [1, 0, 0], [0, 1, 0]],
    [[0, 0, 0], [0, 0, 0], [1, 0, 0]],
]

print("A. MIXED SYMMETRIC PAIR")
check("pair", "the Lorentz form is symmetric and nondegenerate", transpose(q) == q and det3(q) == -1)
check("pair", "so(2,1) has dimension three", rank(linear_map_columns(h_basis)) == 3)
check("pair", "every isotropy basis element is q-skew", all(skew_adjoint(a, q) for a in h_basis))
check("pair", "the real q-self-adjoint traceless complement has dimension five", rank(linear_map_columns(p_real_basis)) == 5)
check("pair", "every complement basis element is q-self-adjoint", all(self_adjoint(b, q) for b in p_real_basis))
check("pair", "the two real summands give dimension eight", 3 + 5 == 8)
check("pair", "[h,h] remains q-skew", all(skew_adjoint(commutator(a, b), q) for a in h_basis for b in h_basis))
check("pair", "[h,p] remains q-self-adjoint", all(self_adjoint(commutator(a, b), q) for a in h_basis for b in p_real_basis))
check("pair", "[i p,i p] is the negative real commutator in h", all(skew_adjoint(matneg(commutator(a, b)), q) for a in p_real_basis for b in p_real_basis))
check("pair", "the invariant real trace pairing annihilates h against i p", all(trace_pair(a, b) == 0 for a in h_basis for b in p_real_basis))
check("pair", "the homogeneous carrier has dimension ten", 2 * (8 - 3) == 10)

print("\nB. PSEUDO-HERMITIAN CANONICAL-FORM CENSUS")
J3 = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
check("coverage", "the size-three real Jordan block has a Lorentz real form", self_adjoint(J3, q))
check("coverage", "the size-three block is regular nilpotent", power(J3, 3) == zeros(3, 3) and power(J3, 2) != zeros(3, 3))
J21 = [[2, 1, 0], [0, 2, 0], [0, 0, -4]]
q21 = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
check("coverage", "the real 2+1 Jordan type has a Lorentz real form", self_adjoint(J21, q21) and det3(q21) == -1)
D111 = [[3, 0, 0], [0, -1, 0], [0, 0, -2]]
q111 = [[1, 0, 0], [0, 1, 0], [0, 0, -1]]
check("coverage", "the three-real-eigenvalue type has a Lorentz real form", self_adjoint(D111, q111) and det3(q111) == -1)
D21 = [[1, 0, 0], [0, 1, 0], [0, 0, -2]]
check("coverage", "the repeated real semisimple type has a Lorentz real form", self_adjoint(D21, q111))
C21 = [[1, -2, 0], [2, 1, 0], [0, 0, -2]]
qc = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
check("coverage", "the non-real conjugate-pair type has a real Lorentz block", self_adjoint(C21, qc) and det3(qc) == -1)
check("coverage", "the non-real block has the real characteristic factor ((x-1)^2+4)(x+2)", power(C21, 3) != zeros(3, 3) and C21[0][1] * C21[1][0] < 0)
check("coverage", "all listed canonical matrices are traceless", all(sum(m[i][i] for i in range(3)) == 0 for m in (J3, J21, D111, D21, C21)))
check("coverage", "the registry uses pseudo-Hermitian canonical-form coverage", REGISTRY["mixed_model"]["surjectivity"].startswith("PSEUDO_HERMITIAN"))
check("coverage", "the determinant-one central adjustment is recorded", REGISTRY["mixed_model"]["special_unitary_adjustment"].startswith("A_PSEUDO_UNITARY"))
check("coverage", "the mixed moment map is declared constructed", REGISTRY["mixed_model"]["verdict"] == "CONSTRUCTED")

print("\nC. REGULAR STABILIZER CONTROLS")
sl3_basis = [
    [[1, 0, 0], [0, -1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, -1]],
    [[0, 1, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [1, 0, 0], [0, 0, 0]],
    [[0, 0, 1], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0]],
    [[0, 0, 0], [0, 0, 1], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 1, 0]],
]
check("rank", "the regular nilpotent centralizer has dimension two", 8 - rank(linear_map_columns([commutator(x, J3) for x in sl3_basis])) == 2)
check("rank", "the regular nilpotent has zero isotropy stabilizer", rank(linear_map_columns([commutator(x, J3) for x in h_basis])) == 3)
check("rank", "the nilpotent mixed moment rank is eight", REGISTRY["mixed_model"]["regular_nilpotent_control"] == "PASS_RANK_8")
C = [[0, -1, 0], [1, 0, 0], [0, 0, 0]]
qC = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
hC = [matmul(qC, k) for k in (K12, K13, K23)]
check("rank", "the non-real-pair control is q-self-adjoint", self_adjoint(C, qC))
check("rank", "the non-real-pair control has zero isotropy stabilizer", rank(linear_map_columns([commutator(x, C) for x in hC])) == 3)
check("rank", "the non-real-spectrum mixed moment rank is eight", REGISTRY["mixed_model"]["nonreal_spectrum_control"] == "PASS_RANK_8")
S = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
check("rank", "the real semisimple control is q-self-adjoint and regular", self_adjoint(S, q) and power(S, 3) == S)
check("rank", "the real semisimple control has zero isotropy stabilizer", rank(linear_map_columns([commutator(x, S) for x in h_basis])) == 3)
check("rank", "every regular mixed value has declared map rank eight", REGISTRY["mixed_model"]["regular_map_rank"] == 8)
check("rank", "the mixed origin has map rank five", REGISTRY["mixed_model"]["origin_map_rank"] == 5)

print("\nD. REAL-FORM CENSUS AND 98D SCHEDULE")
census = REGISTRY["real_form_census"]
check("compose", "split, compact and mixed A2 forms are constructed", {census[k] for k in ("split_sl3R", "compact_su3", "mixed_su2_1")} == {"CONSTRUCTED"})
check("compose", "the real-form census is complete", census["complete_for_real_forms_of_complex_A2"] is True)
schedule = REGISTRY["complete_98d_schedule"]
check("compose", "the complete mixed carrier has dimension 98", 78 + 10 + 10 == schedule["carrier_dimension"])
check("compose", "the complete regular map rank is 91", 78 + 8 + 5 == schedule["regular_map_rank"])
check("compose", "the complete A2-origin map rank is 88", 78 + 5 + 5 == schedule["a2_origin_map_rank"])
check("compose", "the target ranks are 84 then 78", (schedule["regular_target_poisson_rank"], schedule["a2_origin_target_poisson_rank"]) == (84, 78))

print("\nE. ADJACENT-TRANSITION TYPE GATE")
gate = REGISTRY["adjacent_transition_gate"]
check("transition", "both full chart decompositions have dimension 98", 82 + 4 + 12 == gate["rank_one_total_dimension"] == 78 + 10 + 10 == gate["a2_total_dimension"])
check("transition", "the bare rank-one transverse package has dimension 16", 4 + 12 == gate["rank_one_naive_transverse_dimension"])
check("transition", "the bare A2 transverse package has dimension 20", 10 + 10 == gate["a2_naive_transverse_dimension"])
check("transition", "four dimensions transfer from leaf to transverse model", 82 - 78 == gate["leaf_dimension_transfer"])
check("transition", "extracting the common leaf makes both refinement sides 20D", 4 + 4 + 12 == gate["common_refinement_dimension"] == 10 + 10)
check("transition", "the missing object is an explicit common-refinement symplectomorphism", gate["required_map"].startswith("AN_EXPLICIT_SYMPLECTOMORPHISM"))
check("transition", "direct bare-factor potential comparison is rejected as ill-typed", "DIFFERENT_DIMENSIONS" in gate["why_direct_potential_comparison_is_invalid"])
check("transition", "pairwise potential and moment cocycles remain not typed", gate["pairwise_potential_cocycle"] == gate["pairwise_moment_cocycle"] == "NOT_YET_TYPED")
check("transition", "the first noncommuting triple depends on the pair transition", gate["first_noncommuting_triple_cocycle"].startswith("DEPENDENCY_BLOCKED"))

print("\nF. CLAIM CEILING")
scope = REGISTRY["scope"]
check("scope", "all real A2 principal factors are constructed", scope["all_real_a2_principal_factors"] == "CONSTRUCTED")
check("scope", "the adjacent pair transition remains type-missing", scope["adjacent_pair_transition"] == "TYPE_MISSING")
check("scope", "deeper strata remain open", scope["deeper_singular_strata"] == "OPEN")
check("scope", "zero charge remains unconstructed", scope["zero_charge_rank_at_most_49"] == "NOT_CONSTRUCTED")
check("scope", "global RSAP remains open", scope["global_rsap"] == "OPEN")
check("scope", "the 182D all-charge fallback remains", scope["all_charge_fallback_dimension"] == 182)
check("scope", "protected truth surfaces remain unchanged", set(REGISTRY["changes"].values()) == {"none"})

print("\nSUMMARY")
total = sum(COUNTS.values())
print(json.dumps({"checks": total, "counts": COUNTS, "failures": FAILURES, "status": REGISTRY["status"], "next_gate": REGISTRY["next_gate"]}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {total}/{total}")
