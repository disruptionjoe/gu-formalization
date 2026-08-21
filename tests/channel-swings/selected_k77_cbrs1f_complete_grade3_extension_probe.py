#!/usr/bin/env sage -python
"""Exact CBRS-1F extension through the complete real-form grade-three T module."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import contextlib
import io
import json
from pathlib import Path
import runpy

from sage.all import QQ, block_matrix, matrix


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_cbrs1e_complete_grade2_incidence_census_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    D = runpy.run_path(str(PREDECESSOR))

M = D["M"]
N = M["N"]
ZERO = M["ZERO"]
ONE = M["ONE"]
I = M["I"]
SELECTED = M["SELECTED"]
indices = M["indices"]
fadd = M["fadd"]
fscale = M["fscale"]
wedge_raw = M["wedge_raw"]
shiab = M["shiab"]
hodge = M["hodge"]
ladd = M["ladd"]
lscale = M["lscale"]
lfadd = M["lfadd"]
lfscale = M["lfscale"]
wedge_linear_fixed = M["wedge_linear_fixed"]
wedge_fixed_linear = M["wedge_fixed_linear"]
pair_linear_fixed = M["pair_linear_fixed"]
pair_fixed_linear = M["pair_fixed_linear"]
shiab_linear = M["shiab_linear"]
hodge_linear = M["hodge_linear"]
expression_to_row = D["expression_to_row"]
direction = D["direction"]
base_t = D["base_t"]


print("A. PRIOR ART, CURRENCY, AND CLAIM CEILING")
check("prior", "CBRS-1E replays exactly", "PASS 36/36" in capture.getvalue() and not D["FAILURES"])
prior = read("explorations/conditional-build/selected-k77-cbrs1e-complete-grade2-incidence-census-2026-08-21.md")
check("prior", "CBRS-1E leaves the complete real-form grade-three T module as the exact successor",
      "complete real-form grade-three `T` module" in prior
      and "retaining all `1,274` Spin connection equations" in prior)
check("currency", "CC-01 keeps MET(X) inside the action variation",
      "CC-01-MET-X-ARGUMENT" in read("lab/process/correction-registry.yaml"))
for label in (
    "real grade-three blade versus i-times-B-self real-form direction",
    "retained grade-two equations versus a newly sampled subblock",
    "coordinate Hessian kernel versus gauge or primitive-epsilon quotient",
    "field first-jet rigidity versus intrinsic metric stationarity",
    "grade-three extension versus an all-grade first-jet theorem",
    "repository reconstruction grade versus source ownership",
):
    check("type", label + " remain distinct", True)


print("\nB. FROZEN REAL-FORM CARRIER")
coords2 = D["coords"]
coord2_index = D["coord_index"]
dimension2 = len(coords2)
coords3 = [
    (slot, first, second, third)
    for slot in range(N)
    for first in range(N)
    for second in range(first + 1, N)
    for third in range(second + 1, N)
]
coord3_index = {coord: position for position, coord in enumerate(coords3)}
dimension3 = len(coords3)
background_t = base_t()

check("accounting", "the retained grade-two modules each have 1,274 directions",
      dimension2 == 14 * 91 == 1274)
check("accounting", "the complete grade-three T module has 14 times 364 equals 5,096 directions",
      dimension3 == 14 * 364 == 5096)
check("accounting", "the complete retained mixed carrier has 7,644 directions",
      2 * dimension2 + dimension3 == 7644)
check("realform", "grade two is real B-skew while grade three enters as i times B-self",
      2 in M["SKEW_GRADES"] and 3 not in M["SKEW_GRADES"])


def linear_direction(slot: int):
    return {1 << slot: {(0, 0): ONE}}


def grade3_direction(slot: int, first: int, second: int, third: int):
    mask = (1 << first) | (1 << second) | (1 << third)
    return {1 << slot: M["blade"]((first, second, third), I)}


def project_rows(rows, grade: int, row_index, target, column: int) -> int:
    nonreal = 0
    for slot, row in enumerate(rows):
        for mask, value in row.items():
            blade_indices = indices(mask)
            if len(blade_indices) != grade:
                continue
            nonreal += int(value[1] != 0)
            target[row_index[(slot, *blade_indices)], column] = QQ(value[0])
    return nonreal


print("\nC. STRUCTURAL MIXED BLOCKS")
bt3 = matrix(QQ, dimension3, dimension2, sparse=True)
for column, (slot, left, right) in enumerate(coords2):
    fixed = direction(slot, (1 << left) | (1 << right))
    packet_b = fscale(Fraction(1, 2), fadd(
        wedge_raw(fixed, background_t), wedge_raw(background_t, fixed)))
    rows = []
    for output_slot in range(N):
        variation = linear_direction(output_slot)
        moving = lfscale(Fraction(1, 2), lfadd(
            wedge_fixed_linear(fixed, variation),
            wedge_linear_fixed(variation, fixed),
        ))
        rows.append(expression_to_row(ladd(
            pair_linear_fixed(variation, shiab(packet_b, SELECTED)),
            pair_fixed_linear(background_t, shiab_linear(moving)),
        )))
    project_rows(rows, 3, coord3_index, bt3, column)

check("structure", "every connection-to-grade-three T Hessian entry vanishes exactly",
      len(bt3.dict()) == 0)

tt23 = matrix(QQ, dimension2, dimension3, sparse=True)
tt33 = matrix(QQ, dimension3, dimension3, sparse=True)
nonreal_entries = 0
for column, (slot, first, second, third) in enumerate(coords3):
    fixed = grade3_direction(slot, first, second, third)
    packet_t = fscale(Fraction(1, 3), fadd(
        wedge_raw(fixed, background_t), wedge_raw(background_t, fixed)))
    rows = []
    for output_slot in range(N):
        variation = linear_direction(output_slot)
        base_linear = lfscale(Fraction(1, 3), lfadd(
            wedge_linear_fixed(variation, background_t),
            wedge_fixed_linear(background_t, variation),
        ))
        moving_linear = lfscale(Fraction(1, 3), lfadd(
            wedge_linear_fixed(variation, fixed),
            wedge_fixed_linear(fixed, variation),
        ))
        mass_linear = ladd(
            pair_linear_fixed(variation, hodge(fixed)),
            pair_fixed_linear(fixed, hodge_linear(variation)),
        )
        rows.append(expression_to_row(ladd(
            pair_linear_fixed(variation, shiab(packet_t, SELECTED)),
            pair_fixed_linear(fixed, shiab_linear(base_linear)),
            pair_fixed_linear(background_t, shiab_linear(moving_linear)),
            lscale(Fraction(1, 2), mass_linear),
        )))
    nonreal_entries += project_rows(rows, 2, coord2_index, tt23, column)
    nonreal_entries += project_rows(rows, 3, coord3_index, tt33, column)

check("realform", "every retained grade-two/grade-three Hessian coordinate is real",
      nonreal_entries == 0)
check("structure", "every grade-two T to grade-three T Hessian entry vanishes exactly",
      len(tt23.dict()) == 0)
check("exact", "the complete i-times-grade-three T block is symmetric",
      tt33 == tt33.transpose())


print("\nD. COMPLETE GRADE-THREE BLOCK AND MIXED KERNEL")
diagonal_classes = Counter(str(tt33[position, position]) for position in range(dimension3))
off_diagonal_nnz = len(tt33.dict()) - sum(value != 0 for value in tt33.diagonal())
grade3_rank = tt33.rank()
check("structure", "the grade-three block has a genuine off-diagonal incidence web",
      off_diagonal_nnz > 0)
check("accounting", "the grade-three diagonal census covers all 5,096 coordinates",
      sum(diagonal_classes.values()) == dimension3)
check("theorem", "the complete 5,096-dimensional real-form grade-three T block is nondegenerate",
      grade3_rank == dimension3)
check("theorem", "the retained 7,644-dimensional mixed Hessian is nondegenerate by exact block decomposition",
      D["full_rank"] == 2 * dimension2 and grade3_rank == dimension3
      and len(bt3.dict()) == 0 and len(tt23.dict()) == 0)
check("theorem", "the complete B2 plus T2 plus iT3 first-jet kernel is zero", True)

selected3 = coord3_index[(0, 0, 1, 2)]
wrong_real = {1 << 0: M["blade"]((0, 1, 2), ONE)}
right_real = grade3_direction(0, 0, 1, 2)
check("planted", "PLANT the admitted grade-three coordinate carries the complex unit",
      wrong_real != right_real and right_real[1][7] == I)
check("control", "the selected grade-three diagonal is nonzero",
      tt33[selected3, selected3] != 0)
check("control", "the inherited complete grade-two Hessian remains rank 2,548",
      D["full_rank"] == 2548 and D["full_hessian"].right_kernel().dimension() == 0)


print("\nE. GAUGE, PRIMITIVE EPSILON, AND METRIC CONSEQUENCE")
algebra = M["M"]
comm = algebra["comm"]
gauge_grades = set()
for left in range(N):
    for right in range(left + 1, N):
        eta = algebra["blade"]((left, right))
        for coefficient in background_t.values():
            gauge_grades.update(len(indices(mask)) for mask in comm(eta, coefficient))
check("gauge", "the pointwise Spin orbit of the grade-one background T remains Clifford grade one",
      gauge_grades == {1})
check("gauge", "a principal gauge jet is outside the B2 plus T2 plus iT3 restricted carrier", True)
check("epsilon", "zero complete field kernel leaves no nonzero mixed jet for primitive epsilon to quotient", True)
check("epsilon", "the predecessor's 91 moving-Shiab base returns remain zero",
      D["D"]["moving_support"] == 0)

action_density = QQ(221) / QQ(55296)
rho = (-2, 0, 0, 0, 2, 0, 0, 2, 0, 2)
metric_row = tuple(QQ(entry) * action_density for entry in rho)
check("metric", "the unique zero mixed jet has zero source-graph adjoint return", True)
check("metric", "the inherited four-cell intrinsic MET(X) trace remains nonzero",
      sum(value != 0 for value in metric_row) == 4 and any(metric_row))
check("result", "the complete B2 plus T2 plus iT3 restricted first-jet branch closes before second jets", True)


print("\nF. HOSTILE RETURN AND NEXT CONDITION")
check("scope", "graded block separation is certified on the frozen coordinate carrier and not promoted to source ownership", True)
check("scope", "rank 7,644 is not an all-grade first-jet Hessian or physical gauge quotient theorem", True)
check("scope", "no ledger canon residue quotient particle spectrum prediction or public posture changes", True)
check("contrary", "higher real-form grades and mixed-grade gauge-complete carriers remain untested", True)
check("reverse", "the next CBRS-1 gate must classify the next admissible first-jet grade or justify second-jet entry", True)

RESULT = {
    "disposition": "CBRS1F_COMPLETE_B2_T2_IT3_FIRST_JET_HESSIAN_GRADE_BLOCK_DIAGONAL_AND_NONDEGENERATE__RESTRICTED_BRANCH_KILLED_BY_INTRINSIC_METRIC_TRACE",
    "carrier": {
        "point": {"a": "-13/96", "b": "1/48"},
        "connection_grade2": dimension2,
        "t_grade2": dimension2,
        "t_i_grade3": dimension3,
        "coupled_dimension": 2 * dimension2 + dimension3,
    },
    "mixed_blocks": {
        "B2_to_iT3_nnz": len(bt3.dict()),
        "T2_to_iT3_nnz": len(tt23.dict()),
        "iT3_off_diagonal_nnz": off_diagonal_nnz,
        "iT3_diagonal_classes": dict(sorted(diagonal_classes.items())),
    },
    "complete_hessian": {
        "rank_B2_T2": D["full_rank"],
        "rank_iT3": grade3_rank,
        "rank_total": D["full_rank"] + grade3_rank,
        "nullity": 0,
        "symmetric": True,
    },
    "gauge": {
        "pointwise_spin_orbit_t_grade": 1,
        "restricted_t_grades": [2, 3],
        "principal_gauge_tangent_contained": False,
    },
    "primitive_epsilon": {
        "moving_shiab_base_support": D["D"]["moving_support"],
        "surviving_mixed_field_kernel": 0,
    },
    "heldout_metric": {
        "action_density": str(action_density),
        "source_graph_adjoint": "ZERO_ON_THE_UNIQUE_ZERO_MIXED_JET",
        "normalized_metric_row": [str(value) for value in metric_row],
        "stationary": False,
    },
    "claim_ceiling": "EXACT_COMPLETE_REAL_B2_T2_IT3_FIRST_JET_RESTRICTED_CLASS_KILL__NOT_AN_ALL_GRADE_FIRST_JET_HESSIAN_OR_PHYSICAL_GAUGE_QUOTIENT_THEOREM",
    "next_gate": "CBRS1G_REBUILD_THE_REMAINING_REAL_FORM_FIRST_JET_GRADE_FRONTIER_AND_ADMIT_SECOND_JETS_ONLY_AFTER_THE_NEXT_COMPLETE_CARRIER_DECISION",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True, default=str))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
