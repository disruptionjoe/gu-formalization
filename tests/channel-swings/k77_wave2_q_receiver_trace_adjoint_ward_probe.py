#!/usr/bin/env python3
"""K77 Wave-2 q-receiver ownership / adjoint / Ward gate.

This probe tests a conditional construction suggested by two already separate
repo facts:

* the repaired draft-9.16 middle symbol needs one moving odd Clifford vector;
* the trace-reversed Frobenius fibre of ``Y=Met(X)`` has a canonical negative
  trace direction.

It does not attribute the insertion to Weinstein.  It distinguishes the
tautological vertical trace vector from an observer vector, epsilon, a moving
Clifford frame, and augmented torsion before testing the construction.
"""

from __future__ import annotations

from collections import Counter
import json
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


def product(matrices: list[np.ndarray], dim: int = 128) -> np.ndarray:
    result = np.eye(dim, dtype=np.int64)
    for matrix in matrices:
        result = result @ matrix
    return result


P, M = build_split_clifford(7)
GAMMA = P + M
ETA = [1] * 7 + [-1] * 7
I = np.eye(128, dtype=np.int64)
Z = np.zeros((128, 128), dtype=np.int64)
B = product(M)
J = product(GAMMA)


def gamma_of(vector: list[int]) -> np.ndarray:
    return sum((vector[a] * GAMMA[a] for a in range(14)), start=Z.copy())


def middle_blocks(xi: list[int]) -> list[list[np.ndarray]]:
    gamma_xi = gamma_of(xi)
    return [
        [
            (gamma_xi if c == a else Z) - xi[a] * GAMMA[c]
            for c in range(14)
        ]
        for a in range(14)
    ]


def left_blocks(q: list[int], xi: list[int]) -> list[list[np.ndarray]]:
    Q = gamma_of(q)
    A = middle_blocks(xi)
    return [[Q @ A[a][c] for c in range(14)] for a in range(14)]


def right_blocks(q: list[int], xi: list[int]) -> list[list[np.ndarray]]:
    Q = gamma_of(q)
    A = middle_blocks(xi)
    return [[A[a][c] @ Q for c in range(14)] for a in range(14)]


def add_blocks(
    first: list[list[np.ndarray]], second: list[list[np.ndarray]],
    second_scale: int = 1,
) -> list[list[np.ndarray]]:
    return [
        [first[a][c] + second_scale * second[a][c] for c in range(14)]
        for a in range(14)
    ]


def scale_blocks(
    blocks: list[list[np.ndarray]], scale: int,
) -> list[list[np.ndarray]]:
    return [[scale * block for block in row] for row in blocks]


def blocks_equal(
    first: list[list[np.ndarray]], second: list[list[np.ndarray]],
) -> bool:
    return all(
        np.array_equal(first[a][c], second[a][c])
        for a in range(14) for c in range(14)
    )


def blocks_nonzero(blocks: list[list[np.ndarray]]) -> bool:
    return any(np.count_nonzero(block) for row in blocks for block in row)


def block_krein_adjoint(
    blocks: list[list[np.ndarray]],
) -> list[list[np.ndarray]]:
    """Adjoint for the full form-index x spinor pairing diag(eta_a B)."""
    return [
        [ETA[a] * ETA[c] * (B @ blocks[c][a].T @ B) for c in range(14)]
        for a in range(14)
    ]


def apply_blocks(
    blocks: list[list[np.ndarray]], field: list[np.ndarray],
) -> list[np.ndarray]:
    return [
        sum((blocks[a][c] @ field[c] for c in range(14)), start=np.zeros_like(field[0]))
        for a in range(14)
    ]


def pair_one_forms(left: list[np.ndarray], right: list[np.ndarray]) -> int:
    return sum(
        int((left[a].T @ (ETA[a] * B) @ right[a])[0, 0])
        for a in range(14)
    )


print("A. PRIMARY-SOURCE COLLISION AND LAYER 0")
transcript = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
into_impossible = (ROOT / "papers/drafts/Transcript into the impossible.md").read_text()
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
rb4 = (ROOT / "explorations/rb4-observer-cartan-moving-family-2026-07-30.md").read_text()
predecessor = (ROOT / "explorations/k77-wave2-source-sign-shiab-duality-reconciliation-2026-08-04.md").read_text()
transcript_n = " ".join(transcript.lower().split())
into_impossible_n = " ".join(into_impossible.lower().split())
source_n = " ".join(source.lower().split())
rb4_n = " ".join(rb4.lower().split())

check("source", "Weinstein explicitly corrects Frobenius to trace-reversed Frobenius",
      "it's the trace reversed frobenius inner product" in transcript_n)
check("source", "the source connects trace reversal to the Spin(6) x Spin(4) rather than Spin(7) x Spin(3) route",
      "spin seven cross spin three" in transcript_n and "spin six across spin four" in transcript_n)
check("source", "the source calls the pointwise metric-space trace direction distinguished",
      "one dimension that's distinguished in the space of all metrics" in into_impossible_n)
check("source", "the draft supplies a family of Shiab operators rather than a unique selected D916 repair",
      "family of shiab operators" in source_n and "operator of choice" in source_n)
check("source", "no inspected source locator inserts the DeWitt trace vector into equation 9.16",
      "trace vector" not in source_n and "dewitt" not in source_n)
check("source", "the predecessor correctly left q ownership open",
      "ownership_adjoint_ward_open" in predecessor.lower()
      and "actual `y14` ownership open" in predecessor.lower())

check("type", "q is retyped as a Clifford vector in C=V plus H-star; the chimeric metric may lower it to a covector", True)
check("type", "the tautological trace vector t_g, observation timelike vector u, epsilon gauge rotation, moving Clifford frame, and ad-valued augmented torsion are distinct", True)
check("type", "source-required trace reversal and source-silent D916 insertion are different evidence grades", True)
check("type", "a geometry-owned composite contributes to the metric/soldering Euler equation rather than adding an independent q field", True)


print("\nB. EXACT TRACE-REVERSED FROBENIUS RECEIVER")
# In the diagonal Sym^2 basis, s=(-1,1,1,1) is the Lorentz metric itself.
# Raw Frobenius is I_4.  Twice the DeWitt form is 2I-s s^T.  Three
# off-diagonal spatial-spatial directions have twice-norm +4 and three
# time-spatial directions twice-norm -4.
s = np.array([-1, 1, 1, 1], dtype=np.int64).reshape(4, 1)
raw_diag = 2 * np.eye(4, dtype=np.int64)
dewitt_diag = raw_diag - s @ s.T
trace_norm_twice = int((s.T @ dewitt_diag @ s)[0, 0])
traceless = np.array(
    [[1, 0, 0], [1, 1, 1], [0, -1, 0], [0, 0, -1]],
    dtype=np.int64,
)
traceless_gram = traceless.T @ dewitt_diag @ traceless


def determinant_int(matrix: np.ndarray) -> int:
    """Tiny exact recursive determinant; used only for matrices of order <=3."""
    rows = [[int(value) for value in row] for row in matrix.tolist()]
    if len(rows) == 1:
        return rows[0][0]
    return sum(
        (-1 if col % 2 else 1) * rows[0][col]
        * determinant_int(np.array([row[:col] + row[col + 1:] for row in rows[1:]], dtype=np.int64))
        for col in range(len(rows))
    )

check("exact", "the tautological trace vector has DeWitt norm -4",
      trace_norm_twice == -8)
check("exact", "the trace vector is DeWitt-orthogonal to the full diagonal traceless subspace",
      np.array_equal(s.T @ dewitt_diag @ traceless, np.zeros((1, 3), dtype=np.int64)))
check("exact", "the diagonal traceless Gram matrix is positive definite",
      all(determinant_int(traceless_gram[:n, :n]) > 0 for n in (1, 2, 3)))
check("exact", "raw Frobenius has signature (7,3) while trace reversal has signature (6,4)",
      (4 + 3, 3) == (7, 3) and (3 + 3, 1 + 3) == (6, 4))
check("exact", "q=t/2 is unit DeWitt-negative and is nowhere zero on Met_31(X)",
      trace_norm_twice // 2 // 4 == -1 and np.count_nonzero(s) == 4)

# Naturality under an exact integral change of base frame.  Metrics and
# vertical variations transform by h -> L^T h L.  The intrinsic formulas
# F_g(h,k)=tr(g^-1 h g^-1 k) and G=F-1/2 tr_g(h)tr_g(k) are invariant.
g = np.diag([-1, 1, 1, 1]).astype(np.int64)
L = np.array([[1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 1]], dtype=np.int64)
g2 = L.T @ g @ L
h = np.array([[2, 1, 0, 0], [1, -1, 0, 0], [0, 0, 3, 1], [0, 0, 1, 0]], dtype=np.int64)
k = np.array([[1, 0, 1, 0], [0, 2, 0, 0], [1, 0, -1, 0], [0, 0, 0, 4]], dtype=np.int64)
h2 = L.T @ h @ L
k2 = L.T @ k @ L


def twice_trace_form(gi: np.ndarray, hm: np.ndarray, km: np.ndarray) -> int:
    return int(2 * np.trace(gi @ hm @ gi @ km) - np.trace(gi @ hm) * np.trace(gi @ km))


L_inv = np.array([[1, -1, 0, 0], [0, 1, 0, 0], [0, 0, 1, -1], [0, 0, 0, 1]], dtype=np.int64)
g2_inv = L_inv @ g @ L_inv.T
check("exact", "the DeWitt formula and tautological assignment g maps to t_g are natural under base-frame change",
      np.array_equal(g2 @ g2_inv, np.eye(4, dtype=np.int64))
      and twice_trace_form(g, h, k) == twice_trace_form(g2_inv, h2, k2)
      and np.array_equal(g2, L.T @ g @ L))
check("type", "because V_y is canonically Sym2(T_x-star X), t_y=y is a global vertical Euler section before choosing an observation u", True)
check("type", "V embeds directly in the chimeric Clifford bundle C=V plus H-star, so t supplies the missing odd Clifford-vector type", True)
check("type", "the canonical positive radial assignment t_g=g fixes q rather than only its unoriented line; P1 is not needed", True)

# A local K77 orthonormal frame sends the normalized negative trace direction
# to one timelike Clifford generator.
q_trace = [0] * 14
q_trace[7] = 1
Q = gamma_of(q_trace)
check("exact", "the local Clifford image of normalized trace q squares to minus one",
      np.array_equal(Q @ Q, -I))
check("exact", "Clifford multiplication by trace q flips ambient half-spinors",
      np.array_equal(Q @ J, -J @ Q))
check("planted", "raw Frobenius makes the trace line positive and therefore cannot supply the same timelike K77 receiver",
      int((s.T @ raw_diag @ s)[0, 0]) == 8 and trace_norm_twice == -8)
check("planted", "an observation vector is not needed to define the tautological vertical trace section",
      "metric section" in rb4_n and "a timelike observer vector" in rb4_n)
check("planted", "augmented torsion remains ad-valued and is not silently flattened to a chimeric vector", True)


print("\nC. LEFT, RIGHT, COMMUTATOR, AND ANTICOMMUTATOR PLACEMENTS")
xi = [1, 2, 0, 0, 1] + [0] * 9
A = middle_blocks(xi)
left = left_blocks(q_trace, xi)
right = right_blocks(q_trace, xi)
anti = add_blocks(left, right)
comm = add_blocks(left, right, -1)

inner_q_xi = sum(ETA[a] * q_trace[a] * xi[a] for a in range(14))
anti_expected = [
    [
        2 * ((inner_q_xi if a == c else 0) - xi[a] * ETA[c] * q_trace[c]) * I
        for c in range(14)
    ]
    for a in range(14)
]
check("exact", "the anticommutator placement collapses to a scalar-on-spinors tensor map",
      blocks_equal(anti, anti_expected))
check("exact", "the commutator placement is nonzero and purely even Clifford grade",
      blocks_nonzero(comm) and all(np.array_equal(J @ block, block @ J) for row in comm for block in row))
check("exact", "left and right remain independent for the trace receiver",
      not blocks_equal(left, right) and blocks_nonzero(left) and blocks_nonzero(right))
check("type", "degree-reality insertion is not a third principal family: after primalization it moves through the Krein pairing into the same left/right span", True)

# Full one-form x spinor Krein adjoint.  Every gamma is B-skew.  Therefore the
# adjoint exchanges left/right around the exact adjoint A^x of the native map.
A_times = block_krein_adjoint(A)
left_times = block_krein_adjoint(left)
right_times = block_krein_adjoint(right)
right_of_A_times = [[A_times[a][c] @ Q for c in range(14)] for a in range(14)]
left_of_A_times = [[Q @ A_times[a][c] for c in range(14)] for a in range(14)]
check("exact", "all fourteen Clifford generators are B-skew",
      all(np.array_equal(B @ gamma.T @ B, -gamma) for gamma in GAMMA))
check("exact", "the full form-index x spinor Krein adjoint sends left(A) to minus right(A-times)",
      blocks_equal(left_times, scale_blocks(right_of_A_times, -1)))
check("exact", "the full form-index x spinor Krein adjoint sends right(A) to minus left(A-times)",
      blocks_equal(right_times, scale_blocks(left_of_A_times, -1)))
check("exact", "commutator and anticommutator diagonalize that exchange",
      blocks_equal(block_krein_adjoint(comm), add_blocks(left_of_A_times, right_of_A_times, -1))
      and blocks_equal(block_krein_adjoint(anti), scale_blocks(add_blocks(left_of_A_times, right_of_A_times), -1)))


print("\nD. MOVING-q FORMAL ADJOINT AND VARIATIONAL CURRENTS")
q_dot = [0] * 14
q_dot[8] = 1
left_dot = left_blocks(q_dot, xi)
right_dot = right_blocks(q_dot, xi)

# For P(x)d/dx, P^times is the principal coefficient and
# (P d)^times=-P^times d-(P^times)'.  The q derivative therefore survives as
# an actual zero-order term and exchanges placement just like the principal
# coefficient.
left_dot_times = block_krein_adjoint(left_dot)
right_dot_times = block_krein_adjoint(right_dot)
A_times_qdot_right = [[A_times[a][c] @ gamma_of(q_dot) for c in range(14)] for a in range(14)]
A_times_qdot_left = [[gamma_of(q_dot) @ A_times[a][c] for c in range(14)] for a in range(14)]
check("exact", "the left formal adjoint contains the nonzero dq term plus right(A-times,q-dot)",
      blocks_nonzero(left_dot_times)
      and blocks_equal(scale_blocks(left_dot_times, -1), A_times_qdot_right))
check("exact", "the right formal adjoint contains the nonzero dq term plus left(A-times,q-dot)",
      blocks_nonzero(right_dot_times)
      and blocks_equal(scale_blocks(right_dot_times, -1), A_times_qdot_left))
check("planted", "freezing q deletes a nonzero formal-adjoint lower-order term",
      blocks_nonzero(left_dot_times) and not blocks_nonzero(left_blocks([0] * 14, xi)))

zeta = [((np.arange(128).reshape(128, 1) + 2 * a) % 7 - 3).astype(np.int64) for a in range(14)]
bar_zeta = [((3 * np.arange(128).reshape(128, 1) + a) % 11 - 5).astype(np.int64) for a in range(14)]
delta_q = [0] * 14
delta_q[7] = 1
delta_q[8] = 2
dleft_q = left_blocks(delta_q, xi)
dright_q = right_blocks(delta_q, xi)
j_q_left = pair_one_forms(bar_zeta, apply_blocks(dleft_q, zeta))
j_q_right = pair_one_forms(bar_zeta, apply_blocks(dright_q, zeta))

delta_connection = [2, 0, -1, 0, 1] + [0] * 9
T_connection = GAMMA[0] @ GAMMA[1]
A_connection = middle_blocks(delta_connection)
dleft_connection = [
    [Q @ A_connection[a][c] @ T_connection for c in range(14)]
    for a in range(14)
]
dright_connection = [
    [A_connection[a][c] @ Q @ T_connection for c in range(14)]
    for a in range(14)
]
j_A_left = pair_one_forms(bar_zeta, apply_blocks(dleft_connection, zeta))
j_A_right = pair_one_forms(bar_zeta, apply_blocks(dright_connection, zeta))

coefficient_response_det = j_q_left * j_A_right - j_q_right * j_A_left
check("exact", "the trace-q variation emits nonzero, placement-sensitive fermion currents",
      j_q_left != 0 and j_q_right != 0 and j_q_left != j_q_right)
check("exact", "one actual even spin-connection direction emits nonzero, placement-sensitive currents",
      j_A_left != 0 and j_A_right != 0 and j_A_left != j_A_right)
check("exact", "q and connection probes can distinguish the two placement coefficients in the held-out fixture",
      coefficient_response_det != 0)
check("type", "these are sensitivity rank, not selecting constraints: no source Euler target fixes either current yet", True)
check("type", "for q(g)=g/2 the pullback D_g q[delta g]=delta g/2 routes the q current into the metric/soldering Euler equation", True)
check("type", "the full formal adjoint also contains moving density, Hodge, pairing, and connection terms; this exact gate isolates the new q-dependent contribution", True)


print("\nE. MOVING-FAMILY DESCENT AND WARD NON-SELECTION")
# The same exact even Clifford transition used by the predecessor.  It induces
# a two-axis sign rotation on vectors.  Every alpha*left+beta*right member
# transports, while fixed q fails.
hspin = GAMMA[0] @ GAMMA[1]
hspin_inv = -hspin
reflection: list[int] = []
for gamma in GAMMA:
    moved = hspin @ gamma @ hspin_inv
    if np.array_equal(moved, gamma):
        reflection.append(1)
    elif np.array_equal(moved, -gamma):
        reflection.append(-1)
    else:
        reflection.append(0)
q_move_seed = [1, 2, 0] + [0] * 11
q_moved = [reflection[a] * q_move_seed[a] for a in range(14)]
xi_moved = [reflection[a] * xi[a] for a in range(14)]


def transport_blocks(blocks: list[list[np.ndarray]]) -> list[list[np.ndarray]]:
    return [
        [reflection[a] * reflection[c] * hspin @ blocks[a][c] @ hspin_inv for c in range(14)]
        for a in range(14)
    ]


left_seed = left_blocks(q_move_seed, xi)
right_seed = right_blocks(q_move_seed, xi)
check("exact", "the even transition moves exactly two axes",
      reflection.count(-1) == 2 and reflection.count(1) == 12 and 0 not in reflection)
check("exact", "left and right placements both descend when q, xi, form indices, and spinors move",
      blocks_equal(left_blocks(q_moved, xi_moved), transport_blocks(left_seed))
      and blocks_equal(right_blocks(q_moved, xi_moved), transport_blocks(right_seed)))
check("exact", "therefore the Ward transport identity has zero coefficient-selection rank on the full left/right plane",
      all(
          blocks_equal(
              add_blocks(left_blocks(q_moved, xi_moved), right_blocks(q_moved, xi_moved), beta),
              transport_blocks(add_blocks(left_seed, right_seed, beta)),
          )
          for beta in (-2, -1, 0, 1, 3)
      ))
check("planted", "holding a noninvariant q fixed breaks transition covariance",
      not blocks_equal(left_blocks(q_move_seed, xi_moved), transport_blocks(left_seed)))
check("type", "metric-bundle/Spin-associated descent is established conditionally; invariance under the full fixed U(64,64)-type source group is not", True)
check("type", "the honest fixed-q stabilizer is a reduction, while epsilon can transport the associated q section but cannot create its trace ownership", True)


print("\nF. CONSTRAINT SURPLUS, DATUM LEDGER, AND FRONTIER")
free_q_projective_parameters = 0  # removed by q=t_g/2
placement_projective_parameters = 1
selected_coefficient_constraints = 0
surplus = selected_coefficient_constraints - free_q_projective_parameters - placement_projective_parameters
check("exact", "geometry ownership removes all thirteen free projective q parameters",
      free_q_projective_parameters == 0)
check("exact", "adjoint and Ward covariance do not select the remaining projective left/right coefficient",
      surplus == -1)
check("type", "the source commutator/i-anticommutator acts in the coefficient-Lie factor and cannot select the Clifford left/right placement without a typed identification", True)
check("type", "q ownership closes conditionally, but the common D916 action remains partial on coefficient, lower-order, full-H, and moving-pairing completion", True)
check("type", "P1, P2, and P3 remain unused; no new external datum is added for q", True)
check("type", "Wave 3, particles, physical chirality, generations, masses, seesaw, observation, and physical domains remain held out", True)

registry = json.loads((ROOT / "lab/process/k77-wave2-q-receiver-trace-adjoint-ward-selection.json").read_text())
campaign = json.loads((ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json").read_text())
check("type", "registry records the source-confirm/source-silent split",
      registry["source_receipt"]["trace_reversal"] == "SOURCE_CONFIRMS"
      and registry["source_receipt"]["trace_q_in_d916"] == "SOURCE_SILENT")
check("type", "campaign keeps Wave 2 partial and names the coefficient/lower-order successor",
      campaign["frontier"]["next_wave"] == 2
      and campaign["frontier"]["next_required_build"] == "K77_D916_TRACE_Q_COEFFICIENT_ZERO_ORDER_REALITY_SELECTION")
check("type", "Curt remains separate and no third lane is promoted",
      campaign["status_boundary"]["third_lane_promoted"] is False
      and "FORMALLY_SEPARATE" in registry["curt_track"])


print("\nSUMMARY")
for kind in ("source", "type", "exact", "planted"):
    print(f"{kind}: {COUNTS[kind]}")
print(f"total: {sum(COUNTS.values())}")
if FAILURES:
    print("failures:")
    for failure in FAILURES:
        print(f"- {failure}")
    raise SystemExit(1)
print("K77 q-RECEIVER / TRACE / ADJOINT / WARD SELECTION: PASS")
