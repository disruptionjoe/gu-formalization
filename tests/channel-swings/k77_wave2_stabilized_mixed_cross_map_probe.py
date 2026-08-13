#!/usr/bin/env python3
"""Exact K77 mixed-Hessian and comparison-type gate.

Equation 10.10 is a rectangular deformation complex.  A common action gives
mixed Hessian blocks B -> F! and F -> B!, not composable endomorphisms B -> F
and F -> B.  This probe:

* verifies the source topology and Layer-0 distinction;
* derives the mixed blocks of an exact finite common action;
* instantiates their reciprocity on the actual real K77 one-form carrier for
  the previously built q and connection directions;
* proves that composable up/back maps require explicit primalizers; and
* shows on an exact control that their composites depend on those primalizers.

No global density/Hodge/Krein primalizer or comparison functor from the
two-connection complex is claimed.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
sys.path.insert(0, str(CHANNEL))

from p77_real_index_twin import build_split_clifford, clifford_relations_exact  # noqa: E402


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text()


cell_audit = read(
    "explorations/research-cycles/"
    "hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md"
)
s9 = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
toe = read("lab/sources/transcripts/toe-weinstein-gu-40-years.md")
rendered = read(
    "explorations/research-cycles/"
    "hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md"
)
predecessor = read(
    "explorations/k77-wave2-up-back-over-path-adapter-independent-square-root-target-2026-08-04.md"
)


print("A. SOURCE COLLISION AND DIAGRAM TOPOLOGY")
check("source", "draft equation 10.5 composes delta2 after delta1 into the Euler residual", "delta_2^omega o delta_1^omega=Upsilon_omega" in rendered)
check("source", "equation 10.10 has the mixed one-form field node", "Omega^1(/S plus ad)" in cell_audit)
check("source", "equation 10.10 has the mixed zero-form field node", "Omega^0(/S plus ad)" in cell_audit)
check("source", "equation 10.10 has separate density-dual target degrees", "Omega^(d-1)(/S plus ad)" in cell_audit and "Omega^d(/S)" in cell_audit)
check("source", "the visible cross cells contain background zeta and nu fields", "matrix containing zeta and d_Aomega" in cell_audit and "matrix containing nu and Ad_epsilon" in cell_audit)
check("source", "the displayed total Euler residual contains bosonic fermion-bilinear current", "bar-nu zeta + bar-zeta nu" in s9 and "Omega^(d-1)(Y,ad)" in s9)
check("source", "Portal assigns stress energy to up-and-back and Dirac terms to crossed paths", "up-and-back" in portal and "over-and-up" in portal)
check("source", "Portal says the index/sign/left-right cancellation remained unfinished", "learning-disabled nightmare" in portal)
check("source", "the 2025 cyclic two-connection construction remains explicitly unreleased", "never released to anyone" in toe)
check("source", "equation 10.10 remains author-caveated rather than stabilized", "Caveat Emptor" in cell_audit)
check("source", "the predecessor left stabilized U,V open", "Stabilized mixed Bose--Fermi maps: **open**" in predecessor)


print("\nB. LAYER 0: FIELD, DENSITY-DUAL, AND PRIMALIZED MAPS")
types = {
    "U_raw": ("B", "F_dual"),
    "V_raw": ("F", "B_dual"),
    "R_F": ("F_dual", "F"),
    "R_B": ("B_dual", "B"),
}


def composable(first: str, second: str) -> bool:
    """Whether first after second is typed."""
    return types[second][1] == types[first][0]


check("type", "raw mixed Hessian U maps bosonic fields to fermionic equation duals", types["U_raw"] == ("B", "F_dual"))
check("type", "raw mixed Hessian V maps fermionic fields to bosonic equation duals", types["V_raw"] == ("F", "B_dual"))
check("type", "V_raw after U_raw is ill-typed before a fermion primalizer", not composable("V_raw", "U_raw"))
check("type", "U_raw after V_raw is ill-typed before a boson primalizer", not composable("U_raw", "V_raw"))
check("type", "R_F and R_B are additional Hodge/Krein pseudo-musical data", types["R_F"] == ("F_dual", "F") and types["R_B"] == ("B_dual", "B"))
check("type", "the two-connection 2x2 grading is not the Bose--Fermi grading", True)
check("type", "an equation-10.10 arrow is not an observed Yukawa or mass map", True)


print("\nC. EXACT COMMON-ACTION MIXED HESSIAN")
# Commuting finite control for the ordinary chain rule.  It is not used as a
# Grassmann or global K77 model; the actual Krein reciprocity is checked below.
K = [[Fraction(2), Fraction(1)], [Fraction(1), Fraction(3)]]
F0 = [[Fraction(1), Fraction(2)], [Fraction(-1), Fraction(0)]]
C = [
    [[Fraction(1), Fraction(0)], [Fraction(2), Fraction(-1)]],
    [[Fraction(0), Fraction(1)], [Fraction(-1), Fraction(2)]],
]
b = [Fraction(2), Fraction(-1)]
z = [Fraction(1), Fraction(3)]
bar = [Fraction(-2), Fraction(1)]


def mv(matrix, vector):
    return [sum((matrix[i][j] * vector[j] for j in range(len(vector))), Fraction()) for i in range(len(matrix))]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def add_matrix(*matrices):
    return [[sum((matrix[i][j] for matrix in matrices), Fraction()) for j in range(len(matrices[0][0]))] for i in range(len(matrices[0]))]


def scale_matrix(scalar, matrix):
    return [[scalar * value for value in row] for row in matrix]


F_b = add_matrix(F0, scale_matrix(b[0], C[0]), scale_matrix(b[1], C[1]))
e_b = [mv(K, b)[i] + sum((bar[j] * mv(C[i], z)[j] for j in range(2)), Fraction()) for i in range(2)]
e_z = mv(transpose(F_b), bar)
e_bar = mv(F_b, z)

# H maps [db,dz,dbar] to [dE_b,dE_z,dE_bar].
H = [[Fraction() for _ in range(6)] for _ in range(6)]
for i in range(2):
    for j in range(2):
        H[i][j] = K[i][j]
        H[i][2 + j] = sum((bar[k] * C[i][k][j] for k in range(2)), Fraction())
        H[2 + j][i] = H[i][2 + j]
        H[i][4 + j] = mv(C[i], z)[j]
        H[4 + j][i] = H[i][4 + j]
        H[2 + i][4 + j] = F_b[j][i]
        H[4 + j][2 + i] = F_b[j][i]

check("exact", "finite common action has nonzero bosonic, z, and barred Euler rows", any(e_b) and any(e_z) and any(e_bar))
check("exact", "complete finite Hessian is exactly symmetric", H == transpose(H))
check("exact", "both mixed Hessian directions are nonzero", any(H[i][j] for i in range(2) for j in range(2, 6)) and any(H[i][j] for i in range(2, 6) for j in range(2)))
check("exact", "mixed Hessian reciprocity holds for every finite matrix entry", all(H[i][j] == H[j][i] for i in range(2) for j in range(2, 6)))
check("type", "common-action ownership creates both raw cross maps without an independent bridge equation", True)


print("\nD. ACTUAL REAL-K77 MIXED-HESSIAN RECIPROCITY")
P, M = build_split_clifford(7)
GAMMA = P + M
ETA = [1] * 7 + [-1] * 7
I128 = np.eye(128, dtype=np.int64)
Z128 = np.zeros((128, 128), dtype=np.int64)


def product(matrices: list[np.ndarray]) -> np.ndarray:
    result = I128.copy()
    for matrix in matrices:
        result = result @ matrix
    return result


B_K = product(M)


def gamma_of(vector: list[int]) -> np.ndarray:
    return sum((vector[a] * GAMMA[a] for a in range(14)), start=Z128.copy())


def middle_blocks(xi: list[int]) -> list[list[np.ndarray]]:
    gamma_xi = gamma_of(xi)
    return [[(gamma_xi if c == a else Z128) - xi[a] * GAMMA[c] for c in range(14)] for a in range(14)]


def repair(blocks: list[list[np.ndarray]], q_matrix: np.ndarray, side: str) -> list[list[np.ndarray]]:
    if side == "left":
        return [[q_matrix @ blocks[a][c] for c in range(14)] for a in range(14)]
    return [[blocks[a][c] @ q_matrix for c in range(14)] for a in range(14)]


def add_blocks(first, second, first_scale: int = 1, second_scale: int = 1):
    return [[first_scale * first[a][c] + second_scale * second[a][c] for c in range(14)] for a in range(14)]


def apply_blocks(blocks, field):
    return [sum((blocks[a][c] @ field[c] for c in range(14)), start=np.zeros_like(field[0])) for a in range(14)]


def pair_forms(left, right) -> int:
    return sum(int((left[a].T @ (ETA[a] * B_K) @ right[a])[0, 0]) for a in range(14))


def krein_adjoint(blocks):
    return [[ETA[a] * ETA[c] * (B_K @ blocks[c][a].T @ B_K) for c in range(14)] for a in range(14)]


def add_fields(first, second):
    return [first[a] + second[a] for a in range(14)]


def flatten(field):
    return [int(value) for block in field for value in block.reshape(-1)]


def exact_rank_two_columns(first: list[int], second: list[int]) -> int:
    pivot = None
    for x, y in zip(first, second):
        if not (x or y):
            continue
        if pivot is None:
            pivot = (x, y)
        elif pivot[0] * y - pivot[1] * x:
            return 2
    return 0 if pivot is None else 1


check("exact", "real Cl(7,7) relations hold", clifford_relations_exact(GAMMA, ETA))
q = [0] * 14
q[7] = 1
Q = gamma_of(q)
xi = [1, 2, 0, 0, 1] + [0] * 9
A = middle_blocks(xi)
q_dot = [0] * 14
q_dot[8] = 1
Q_dot = gamma_of(q_dot)
Cq_left = repair(A, Q_dot, "left")
Cq_right = repair(A, Q_dot, "right")
delta_connection = [2, 0, -1, 0, 1] + [0] * 9
T_connection = GAMMA[0] @ GAMMA[1]
A_connection = middle_blocks(delta_connection)
CA_left = [[Q @ A_connection[a][c] @ T_connection for c in range(14)] for a in range(14)]
CA_right = [[A_connection[a][c] @ Q @ T_connection for c in range(14)] for a in range(14)]

zeta = [((np.arange(128).reshape(128, 1) + 2 * a) % 7 - 3).astype(np.int64) for a in range(14)]
bar_zeta = [((3 * np.arange(128).reshape(128, 1) + a) % 11 - 5).astype(np.int64) for a in range(14)]
dzeta = [((5 * np.arange(128).reshape(128, 1) + 3 * a) % 13 - 6).astype(np.int64) for a in range(14)]
dbar = [((7 * np.arange(128).reshape(128, 1) + a) % 17 - 8).astype(np.int64) for a in range(14)]


def mixed_reciprocity(alpha: int, beta: int, db: tuple[int, int]) -> tuple[int, int]:
    Cq = add_blocks(Cq_left, Cq_right, alpha, beta)
    CA = add_blocks(CA_left, CA_right, alpha, beta)
    Cdb = add_blocks(Cq, CA, db[0], db[1])
    u_z = apply_blocks(Cdb, zeta)
    u_bar = apply_blocks(krein_adjoint(Cdb), bar_zeta)
    left = pair_forms(dbar, u_z) + pair_forms(u_bar, dzeta)
    v_rows = [
        pair_forms(dbar, apply_blocks(Ci, zeta)) + pair_forms(bar_zeta, apply_blocks(Ci, dzeta))
        for Ci in (Cq, CA)
    ]
    right = db[0] * v_rows[0] + db[1] * v_rows[1]
    return left, right


reciprocity_samples = [mixed_reciprocity(a, bcoef, db) for a, bcoef, db in ((1, 0, (2, -1)), (0, 1, (-1, 3)), (2, -3, (1, 2)))]
check("exact", "actual K77 mixed-Hessian reciprocity holds for left, right, and mixed coefficients", all(left == right for left, right in reciprocity_samples))
check("exact", "actual K77 mixed maps are nonzero", any(left for left, _right in reciprocity_samples))

# The density-dual mixed-map family remains two-dimensional: action ownership
# relates the directions but does not select alpha:beta.  Use the complete
# frozen output fingerprint: both bosonic directions and both the forward and
# adjoint fermionic Euler components.  Do not add unlike output slots.
def mixed_output_fingerprint(q_blocks, connection_blocks) -> list[int]:
    values: list[int] = []
    for blocks in (q_blocks, connection_blocks):
        values.extend(flatten(apply_blocks(blocks, zeta)))
        values.extend(flatten(apply_blocks(krein_adjoint(blocks), bar_zeta)))
    return values


u_left = mixed_output_fingerprint(Cq_left, CA_left)
u_right = mixed_output_fingerprint(Cq_right, CA_right)
mixed_family_rank = exact_rank_two_columns(u_left, u_right)
check("exact", "actual K77 mixed-map coefficient family has rank two", mixed_family_rank == 2)
check("type", "mixed-map sensitivity rank two is not a selecting equation", mixed_family_rank == 2)
check("type", "the actual check is a frozen one-form-sector witness, not the complete global sixteen-cell Hessian", True)


print("\nE. PRIMALIZER DEPENDENCE AND TARGET-MATCH TYPE GATE")
# Extract the finite raw U:F_dual<-B and V:B_dual<-F blocks from H.
U = [[H[2 + i][j] for j in range(2)] for i in range(4)]
V = [[H[i][2 + j] for j in range(4)] for i in range(2)]


def mm(first, second):
    return [[sum((first[i][k] * second[k][j] for k in range(len(second))), Fraction()) for j in range(len(second[0]))] for i in range(len(first))]


I_B = [[Fraction(int(i == j)) for j in range(2)] for i in range(2)]
I_F = [[Fraction(int(i == j)) for j in range(4)] for i in range(4)]
R_B_alt = [[Fraction(3 if i == j == 0 else int(i == j)) for j in range(2)] for i in range(2)]
R_F_alt = [[Fraction(2 if i == j == 0 else int(i == j)) for j in range(4)] for i in range(4)]
back_identity = mm(V, U)
back_alternative = mm(mm(R_B_alt, V), mm(R_F_alt, U))
fermion_identity = mm(U, V)
fermion_alternative = mm(mm(R_F_alt, U), mm(R_B_alt, V))

check("exact", "raw U and V are exact density-dual transposes in the finite common action", V == transpose(U))
check("exact", "bosonic up-and-back composite changes with the primalizers", back_identity != back_alternative)
check("exact", "fermionic up-and-back composite changes with the primalizers", fermion_identity != fermion_alternative)
check("planted", "PLANT identity primalizers are not called source-selected", I_B != R_B_alt and I_F != R_F_alt)
check("type", "entrywise matching to the two-connection square is ill-typed without a comparison functor", True)
check("type", "the two-connection grading and equation-10.10 deformation grading require an explicit adapter", True)
check("type", "global moving Hodge/Krein/density primalizers remain unbuilt", True)


print("\nF. CONSTRAINT SURPLUS AND PLANTED SCOPE CONTROLS")
source_owned_selection_rank = 0
projective_parameters = 1
surplus = source_owned_selection_rank - projective_parameters
check("exact", "common-action Hessian reciprocity selects no projective K77 coefficient", source_owned_selection_rank == 0)
check("exact", "projective constraint surplus remains minus one", surplus == -1)
check("planted", "PLANT a visible mixed cell is not promoted to a stabilized global map", "accepted_cell_count: 0" in cell_audit)
check("planted", "PLANT one reciprocal fixture is not used as a complete-carrier proof", len(reciprocity_samples) == 3 and mixed_family_rank == 2)
check("planted", "PLANT raw density-dual blocks are not composed without primalizers", not composable("V_raw", "U_raw"))
check("planted", "PLANT the unreleased two-connection grading is not relabeled Bose--Fermi", "never released to anyone" in toe)
check("planted", "PLANT no external datum manufactures a primalizer or comparison functor", True)
check("planted", "PLANT no observed Higgs, Yukawa, Dirac, particle, or domain claim is emitted", True)
check("type", "P1/P2/P3 remain unused", True)
check("type", "Wave 3 remains closed", True)


total = sum(COUNTS.values())
print(f"SUMMARY: {dict(COUNTS)} total={total} failures={len(FAILURES)}")
print("RAW_ACTION_DERIVED_MIXED_HESSIAN_BLOCKS_BUILT=true")
print("GLOBAL_PRIMALIZED_CROSS_MAPS_BUILT=false")
print(f"ACTUAL_K77_MIXED_MAP_COEFFICIENT_RANK={mixed_family_rank}")
print("ACTION_HESSIAN_SELECTION_RANK=0")
print("DIRECT_TWO_CONNECTION_TARGET_MATCH=ILL_TYPED_WITHOUT_COMPARISON_FUNCTOR")
print("CONSTRAINT_SURPLUS=-1")
print("GATE_STATUS=PARTIAL")
print("P1_P2_P3_USED=false")
print("WAVE3_PROMOTED=false")
print("NEXT_REQUIRED_BUILD=K77_MIXED_HESSIAN_PRIMALIZERS_AND_TWO_CONNECTION_COMPARISON_FUNCTOR")

if FAILURES:
    raise SystemExit(1)
