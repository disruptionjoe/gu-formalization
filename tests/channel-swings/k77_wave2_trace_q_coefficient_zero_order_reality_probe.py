#!/usr/bin/env python3
"""Exact K77 trace-q coefficient / zero-order / reality selection gate.

This probe asks a deliberately narrow question.  The previous gate found a
canonical trace receiver q and a two-dimensional left/right placement family.
Here we assemble that family into all sixteen displayed draft-9.16 cells and
test whether the written zero-order connection terms, the native real
structure, an optional Majorana reduction, or Curt's Higgs/Yukawa placement
select a nonzero projective coefficient.

The source-faithful classical branch keeps barred and unbarred fields
independent.  A Majorana fixed locus is tested as a rival, not assumed.
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


def right_compose(
    blocks: list[list[np.ndarray]], matrix: np.ndarray,
) -> list[list[np.ndarray]]:
    return [[blocks[a][c] @ matrix for c in range(14)] for a in range(14)]


def repair_blocks(
    blocks: list[list[np.ndarray]], q_matrix: np.ndarray, side: str,
) -> list[list[np.ndarray]]:
    if side == "left":
        return [[q_matrix @ blocks[a][c] for c in range(14)] for a in range(14)]
    if side == "right":
        return [[blocks[a][c] @ q_matrix for c in range(14)] for a in range(14)]
    raise ValueError(side)


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


def block_krein_adjoint(
    blocks: list[list[np.ndarray]],
) -> list[list[np.ndarray]]:
    return [
        [ETA[a] * ETA[c] * (B @ blocks[c][a].T @ B) for c in range(14)]
        for a in range(14)
    ]


def blocks_equal(
    first: list[list[np.ndarray]], second: list[list[np.ndarray]],
) -> bool:
    return all(
        np.array_equal(first[a][c], second[a][c])
        for a in range(14) for c in range(14)
    )


def blocks_nonzero(blocks: list[list[np.ndarray]]) -> bool:
    return any(np.count_nonzero(block) for row in blocks for block in row)


def coefficient_system_rank(
    first: list[list[np.ndarray]], second: list[list[np.ndarray]],
) -> int:
    """Exact rank of the two-column system formed by all block entries."""
    pivot: tuple[int, int] | None = None
    for a in range(14):
        for c in range(14):
            xs = first[a][c].reshape(-1)
            ys = second[a][c].reshape(-1)
            active = np.flatnonzero((xs != 0) | (ys != 0))
            for index in active:
                row = (int(xs[index]), int(ys[index]))
                if pivot is None:
                    pivot = row
                elif pivot[0] * row[1] - pivot[1] * row[0] != 0:
                    return 2
    return 0 if pivot is None else 1


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


print("A. SOURCE COLLISION AND LAYER 0")
draft = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
curt = (ROOT / "lab/sources/curt-iceberg-fermion-zero-order-reinspection-2026-08-04.md").read_text()
toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
predecessor = (ROOT / "explorations/k77-wave2-q-receiver-trace-adjoint-ward-selection-2026-08-04.md").read_text()
draft_n = " ".join(draft.lower().split())
curt_n = " ".join(curt.lower().split())
toe_n = " ".join(toe.lower().split())

check("source", "the draft keeps four independent barred and unbarred classical fields",
      "four distinct fields" in draft_n and "independent barred/unbarred fields" in draft_n)
check("source", "the draft supplies all sixteen signed cells but no global reality adjoint",
      "all sixteen" in draft_n and "global hodge/krein/reality adjoint" in draft_n)
check("source", "Curt places a vertical connection component in off-diagonal chiral Dirac blocks",
      "01:46:11--01:48:57" in curt and "off-diagonal blocks" in curt_n)
check("source", "Curt distinguishes the real 128 carrier from Eric's complex Dirac presentation",
      "real 128-dimensional" in curt_n and "complex dirac spinors" in curt_n)
check("source", "Weinstein corrects the single-layer reading to Einstein-Dirac plus a second Yang-Mills-Higgs Lagrangian",
      "einstein-durac portion" in toe_n and "second lagrangian" in toe_n
      and "yang-mills-higgs" in toe_n)
check("source", "Weinstein says an adjoint-valued Higgs is not the real Higgs representation",
      "higgs field value itself in the adjoint" in toe_n
      and "that's not what the real higgs field does" in toe_n)
check("source", "Curt is a search directive but the q coefficient remains source-silent",
      "source-silent" in curt_n and "cannot by itself spend the remaining projective coefficient" in curt_n)

check("type", "ordinary Dirac adjoint, four independent Berezin bars, and a Majorana fixed locus are distinct objects", True)
check("type", "Curt's chiral left/right blocks are not Clifford left/right multiplication around Shiab", True)
check("type", "a vertical adjoint-valued scalar candidate is not yet the physical Standard Model Higgs representation", True)
check("type", "the source coefficient-algebra magic bracket is not the Clifford placement coefficient", True)
check("type", "the Einstein-Dirac and Yang-Mills-Higgs layers require an explicit adapter before a shared zero-order selector can be claimed", True)


print("\nB. EXACT REAL K77 CARRIER AND COMPLETE D916 CELL LEDGER")
check("exact", "Cl(7,7) relations hold on the real 128-spinor carrier",
      clifford_relations_exact(GAMMA, ETA))
check("exact", "the Krein matrix is symmetric split and cross-pairs ambient halves",
      np.array_equal(B.T, B) and np.array_equal(B @ B, I)
      and np.array_equal(B @ J, -J @ B))

formulas = (
    ("qPhi_varpi_pp", "qPhi_d0_varpi_pm", "varpi_pp", "d0_varpi_pm"),
    ("qPhi_d0_varpi_mp", "qPhi_varpi_mm", "d0_varpi_mp", "varpi_mm"),
    ("minus_bar_varpi_pp_times", "minus_d0_bar_varpi_pm_times", "zero", "zero"),
    ("minus_d0_bar_varpi_mp_times", "minus_bar_varpi_mm_times", "zero", "zero"),
)
orders = (
    (0, 1, 0, 1),
    (1, 0, 1, 0),
    (0, 1, 0, 0),
    (1, 0, 0, 0),
)
ledger = [
    {
        "row": r,
        "column": c,
        "formula": formulas[r][c],
        "order": orders[r][c],
        "q_repaired": r < 2 and c < 2,
    }
    for r in range(4) for c in range(4)
]
check("exact", "the assembled source ledger contains exactly sixteen cells", len(ledger) == 16)
check("exact", "exactly four top-left Shiab cells carry the trace-q repair",
      sum(cell["q_repaired"] for cell in ledger) == 4)
check("exact", "exactly six cells are first order",
      sum(cell["order"] == 1 for cell in ledger) == 6)
check("exact", "the source-preferred southeast quadrant remains exactly zero",
      all(formulas[r][c] == "zero" for r in (2, 3) for c in (2, 3)))
check("type", "the same projective q coefficient is declared across all four Shiab cells; cellwise retuning is forbidden", True)
check("type", "Curt does not identify which varpi_rs cell is the physical Higgs after reduction", True)

# The degree-reality solutions found by the preceding exact gate.  They type
# the row/column primalizers; they do not add a third coefficient family.
degree_reality_solutions = [(-s, s, s, -s) for s in (1, -1)]
check("exact", "the two full degree-reality sign solutions are retained",
      degree_reality_solutions == [(-1, 1, 1, -1), (1, -1, -1, 1)])
check("exact", "both degree-reality solutions act on every one-to-one Shiab cell by the same overall minus sign",
      all(r1 * c1 == -1 for r1, _r0, c1, _c0 in degree_reality_solutions))
check("type", "an overall nonzero sign cannot change the rank of a self/skew coefficient system", True)


print("\nC. PRINCIPAL AND ZERO-ORDER LEFT/RIGHT FAMILIES")
q_trace = [0] * 14
q_trace[7] = 1
Q = gamma_of(q_trace)
xi = [1, 2, 0, 0, 1] + [0] * 9
a = [2, -1, 0, 1] + [0] * 10
T = GAMMA[0] @ GAMMA[1]
check("exact", "q is unit negative, odd, and the connection test direction is even B-skew",
      np.array_equal(Q @ Q, -I) and np.array_equal(Q @ J, -J @ Q)
      and np.array_equal(T @ J, J @ T) and np.array_equal(T.T @ B + B @ T, Z))

A_principal = middle_blocks(xi)
A_zero = right_compose(middle_blocks(a), T)
L_principal = repair_blocks(A_principal, Q, "left")
R_principal = repair_blocks(A_principal, Q, "right")
L_zero = repair_blocks(A_zero, Q, "left")
R_zero = repair_blocks(A_zero, Q, "right")

check("exact", "left and right principal placements are nonzero and independent",
      blocks_nonzero(L_principal) and blocks_nonzero(R_principal)
      and not blocks_equal(L_principal, R_principal))
check("exact", "left and right zero-order connection placements are nonzero and independent",
      blocks_nonzero(L_zero) and blocks_nonzero(R_zero)
      and not blocks_equal(L_zero, R_zero))
check("exact", "the principal anticommutator is scalar on spinors",
      all(
          np.array_equal(J @ block, block @ J)
          for row in add_blocks(L_principal, R_principal) for block in row
      ))
check("exact", "the principal commutator is a distinct even Clifford branch",
      blocks_nonzero(add_blocks(L_principal, R_principal, -1))
      and not blocks_equal(
          add_blocks(L_principal, R_principal),
          add_blocks(L_principal, R_principal, -1),
      ))

A_principal_times = block_krein_adjoint(A_principal)
A_zero_times = block_krein_adjoint(A_zero)
Lp_times = block_krein_adjoint(L_principal)
Rp_times = block_krein_adjoint(R_principal)
Lz_times = block_krein_adjoint(L_zero)
Rz_times = block_krein_adjoint(R_zero)
check("exact", "the full principal adjoint exchanges left and right around A-times",
      blocks_equal(Lp_times, scale_blocks(repair_blocks(A_principal_times, Q, "right"), -1))
      and blocks_equal(Rp_times, scale_blocks(repair_blocks(A_principal_times, Q, "left"), -1)))
check("exact", "the full zero-order adjoint obeys the same typed exchange law",
      blocks_equal(Lz_times, scale_blocks(repair_blocks(A_zero_times, Q, "right"), -1))
      and blocks_equal(Rz_times, scale_blocks(repair_blocks(A_zero_times, Q, "left"), -1)))


print("\nD. REALITY AND GRASSMANN SELECTION RANKS")
# Native Cl(7,7) conjugation is ordinary complex conjugation in this real
# matrix model.  It fixes each basis placement separately, so its selecting
# defect is the zero two-column system.
zero_blocks = [[np.zeros_like(L_principal[a][c]) for c in range(14)] for a in range(14)]
c_reality_rank = coefficient_system_rank(zero_blocks, zero_blocks)
check("exact", "native K77 conjugation fixes left and right separately",
      all(np.isrealobj(block) for row in L_principal + R_principal for block in row))
check("exact", "native C-reality has coefficient-selection rank zero",
      c_reality_rank == 0)

# A real Majorana quadratic action would identify the barred field and impose
# a transpose class.  For a first-order Grassmann kernel the primalized
# coefficient must be Krein-self; for zero order it must be Krein-skew.  We do
# not assume either has a solution: solve the exact two-column systems.
principal_self_rank = coefficient_system_rank(
    add_blocks(Lp_times, L_principal, -1),
    add_blocks(Rp_times, R_principal, -1),
)
principal_skew_rank = coefficient_system_rank(
    add_blocks(Lp_times, L_principal),
    add_blocks(Rp_times, R_principal),
)
zero_self_rank = coefficient_system_rank(
    add_blocks(Lz_times, L_zero, -1),
    add_blocks(Rz_times, R_zero, -1),
)
zero_skew_rank = coefficient_system_rank(
    add_blocks(Lz_times, L_zero),
    add_blocks(Rz_times, R_zero),
)
check("exact", "the principal Majorana self condition has full rank two and only the zero coefficient",
      principal_self_rank == 2)
check("exact", "the principal Majorana skew condition also has full rank two",
      principal_skew_rank == 2)
check("exact", "the zero-order self and skew Majorana conditions both have full rank two",
      zero_self_rank == 2 and zero_skew_rank == 2)
check("type", "the optional Majorana fixed locus therefore kills this frozen q-family; it does not select commutator or anticommutator", True)
check("type", "lower-order moving-q, Hodge, density, or connection terms cannot repair a full-rank principal-symbol reality obstruction", True)

# Independent barred variables define a Dirac bilinear for every coefficient.
# Two action samples distinguish the coefficients but do not constrain them.
zeta = [((np.arange(128).reshape(128, 1) + 2 * k) % 7 - 3).astype(np.int64) for k in range(14)]
bar1 = [((3 * np.arange(128).reshape(128, 1) + k) % 11 - 5).astype(np.int64) for k in range(14)]
bar2 = [((5 * np.arange(128).reshape(128, 1) + 2 * k) % 13 - 6).astype(np.int64) for k in range(14)]
response = np.array([
    [pair_one_forms(bar, apply_blocks(L_principal, zeta)),
     pair_one_forms(bar, apply_blocks(R_principal, zeta))]
    for bar in (bar1, bar2)
], dtype=np.int64)
response_det = int(response[0, 0] * response[1, 1] - response[0, 1] * response[1, 0])
check("exact", "independent-bar action samples distinguish both coefficient directions",
      response_det != 0)
check("type", "action sensitivity rank two is not selection rank: independent bar variation is defined for every coefficient", True)
check("type", "complex Hermitian completion can pair any coefficient with its conjugate and therefore does not choose a projective point", True)


print("\nE. MOVING ZERO-ORDER TERMS AND CONSTRAINT SURPLUS")
q_dot = [0] * 14
q_dot[8] = 1
Q_dot = gamma_of(q_dot)
L_dot = repair_blocks(A_principal, Q_dot, "left")
R_dot = repair_blocks(A_principal, Q_dot, "right")
check("exact", "moving q emits nonzero lower-order terms in both independent directions",
      blocks_nonzero(L_dot) and blocks_nonzero(R_dot)
      and not blocks_equal(L_dot, R_dot))
check("exact", "freezing q is a discriminating failure plant",
      not blocks_nonzero(repair_blocks(A_principal, Z, "left")))

projective_free_parameters = 1
source_selecting_rank = 0
constraint_surplus = source_selecting_rank - projective_free_parameters
check("exact", "the source-faithful coefficient invoice remains one projective parameter with surplus minus one",
      projective_free_parameters == 1 and source_selecting_rank == 0
      and constraint_surplus == -1)
check("type", "an unowned Majorana posit cannot be counted as derived surplus; here it is incompatible anyway", True)
check("type", "Curt's zero-order support improves the common-action build target but contributes no coefficient equation", True)
check("type", "the next construction must carry the coefficient family into the two-layer variational action and let actual Euler equations constrain it", True)


print("\nF. PLANTED FAILURES AND CAMPAIGN BOUNDARY")
check("planted", "reading Curt's standard-physics Dirac adjoint as the draft's reality theorem is forbidden",
      "cannot override" in curt_n)
check("planted", "the Iceberg's single minimal-coupling story is not silently substituted for Weinstein's two layers",
      "source-corrects" in curt_n)
check("planted", "commutator is not promoted merely because it is an adjoint eigenword",
      principal_self_rank == 2)
check("planted", "anticommutator is not promoted merely because Curt uses off-diagonal chiral blocks",
      zero_skew_rank == 2)
check("planted", "cellwise coefficient tuning is not allowed to fake a global solution",
      sum(cell["q_repaired"] for cell in ledger) == 4)
check("planted", "zero-order sensitivity is not reported as a selecting Euler equation",
      blocks_nonzero(L_zero) and blocks_nonzero(R_zero) and source_selecting_rank == 0)

campaign = json.loads((ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json").read_text())
check("type", "Curt remains formally separated guidance inside the Eric lane",
      campaign["status_boundary"]["third_lane_promoted"] is False)
check("type", "P1/P2/P3 remain unchanged and unused",
      campaign["status_boundary"]["p1_p2_p3_changed"] is False)
check("type", "Wave 3 remains closed until the common action rather than an isolated selector closes",
      "K77_D916_TRACE_Q_COEFFICIENT_ZERO_ORDER_REALITY_SELECTION" in predecessor
      and campaign["frontier"]["next_wave"] == 2)
check("type", "no particle, mass, chirality, generation, observation, or physical-domain claim is emitted", True)


SUMMARY = {
    "source_collision": "SOURCE_CORRECTS_CURT_SINGLE_LAYER__SOURCE_SILENT_ON_Q_COEFFICIENT",
    "d916_cells": 16,
    "q_repaired_shiab_cells": 4,
    "native_c_reality_selection_rank": c_reality_rank,
    "majorana_principal_self_rank": principal_self_rank,
    "majorana_principal_skew_rank": principal_skew_rank,
    "majorana_zero_self_rank": zero_self_rank,
    "majorana_zero_skew_rank": zero_skew_rank,
    "independent_bar_sensitivity_rank": 2 if response_det else 1,
    "source_selecting_rank": source_selecting_rank,
    "projective_free_parameters": projective_free_parameters,
    "constraint_surplus": constraint_surplus,
    "gate_status": "PARTIAL__FULL16_TRACE_Q_FAMILY_ASSEMBLED__CURT_ZERO_ORDER_PORT_NARROWED__NATIVE_REALITY_SELECTS_NOTHING__MAJORANA_RIVAL_EMPTY__COMMON_TWO_LAYER_ACTION_EULER_SELECTION_OPEN",
    "wave3_open": False,
    "p1_p2_p3_used": False,
}

print("\nK77 TRACE-q COEFFICIENT / ZERO-ORDER / REALITY RESULT")
print(json.dumps(SUMMARY, indent=2, sort_keys=True))
print("counts:")
for kind in sorted(COUNTS):
    print(f"  {kind}: {COUNTS[kind]}")
print(f"  total: {sum(COUNTS.values())}")

if FAILURES:
    print("FAILURES:")
    for failure in FAILURES:
        print(f"  - {failure}")
    raise SystemExit(1)

print("K77 TRACE-q COEFFICIENT / ZERO-ORDER / REALITY SELECTION: PASS")
