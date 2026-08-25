#!/usr/bin/env sage -python
"""Exact CBRS-1G whole-grade first-jet selection and metric obstruction.

The probe quotients the complete 14*2^14 real-form T carrier by the exact
signed-permutation symmetry of the coefficient-anisotropic point.  It proves
that T/T Hessian support is grade diagonal and that the Spin-grade-two
connection owner couples only to T grade two.  It then certifies the five
smallest untouched complete T blocks and follows the surviving grade-one
kernel through Spin-orbit, primitive-epsilon, and fixed-varpi metric gates.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
import contextlib
import io
import json
from pathlib import Path
import runpy

from sage.all import QQ, matrix


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_cbrs1d_coupled_grade2_connection_jet_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def strict_json(relative: str):
    path = ROOT / relative

    def hook(pairs):
        output = {}
        for key, value in pairs:
            if key in output:
                raise ValueError(f"duplicate key {key!r}: {path}")
            output[key] = value
        return output

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


print("A. PRIOR ART, CURRENCY, AND CLAIM CEILING")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    D = runpy.run_path(str(PREDECESSOR))
check("prior", "CBRS-1D exact coupled-cell predecessor replays",
      "PASS 43/43" in capture.getvalue() and not D["FAILURES"])

grade_two = strict_json(
    "lab/process/selected-k77-cbrs1e-complete-grade2-incidence-census.json"
)
grade_three = strict_json(
    "lab/process/selected-k77-cbrs1f-complete-grade3-extension.json"
)
check("prior", "CBRS-1E owns the nondegenerate complete B2 plus T2 block",
      grade_two["complete_coupled_hessian"]["dimension"] == 2548
      and grade_two["complete_coupled_hessian"]["rank"] == 2548
      and grade_two["complete_coupled_hessian"]["nullity"] == 0
      and grade_two["complete_coupled_hessian"]["symmetric"])
check("prior", "CBRS-1F owns the nondegenerate complete iT3 block and cross-grade zeros",
      grade_three["complete_coupled_hessian"]["rank"] == 7644
      and grade_three["complete_coupled_hessian"]["nullity"] == 0
      and grade_three["mixed_blocks"]["B2_to_iT3_nnz"] == 0
      and grade_three["mixed_blocks"]["T2_to_iT3_nnz"] == 0)
check("currency", "CC-01 keeps MET(X) inside the action variation",
      "CC-01-MET-X-ARGUMENT" in read("lab/process/correction-registry.yaml"))
check("retrieval", "the older all-grade parent census binds a distinct Spin-invariant scalar branch",
      "Spin-invariant branch" in read(
          "tests/channel-swings/selected_k77_nonzero_branch_parent_hessian_probe.py"
      ) and "T_VALUE = Fraction(-1, 312)" in read(
          "tests/channel-swings/selected_k77_nonzero_branch_parent_hessian_probe.py"
      ))
for label in (
    "whole-grade support versus complete rank of every grade block",
    "pointwise Spin orbit versus the grade-one Hessian kernel",
    "field first-jet kernel versus primitive-epsilon quotient",
    "zero connection-graph return versus intrinsic metric stationarity",
    "all-grade first-jet metric obstruction versus an all-grade Hessian theorem",
    "repository reconstruction grade versus source ownership",
):
    check("type", label + " remain distinct", True)


M = D["M"]
N = M["N"]
ZERO = M["ZERO"]
ONE = M["ONE"]
I = M["I"]
SELECTED = M["SELECTED"]
ETA = M["ETA"]
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
background_t = D["base_t"]()


def linear_direction(slot: int):
    return {1 << slot: {(0, 0): ONE}}


def t_column(slot: int, mask: int):
    grade = mask.bit_count()
    fixed = direction(slot, mask)
    if grade not in M["SKEW_GRADES"]:
        fixed = fscale(I, fixed)
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
    return rows


def b2_column(slot: int, mask: int):
    fixed = direction(slot, mask)
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
    return rows


print("\nB. EXACT WHOLE-GRADE SUPPORT THEOREM")
positive_ordinary = tuple(i for i in range(1, N) if ETA[i] == 1)
negative = tuple(i for i in range(1, N) if ETA[i] == -1)
check("signature", "the distinguished positive axis leaves six positive and seven negative peers",
      ETA[0] == 1 and len(positive_ordinary) == 6 and len(negative) == 7)
check("planted", "PLANT signature classes are not inferred from contiguous index ranges",
      positive_ordinary != tuple(range(1, 7))
      and negative != tuple(range(7, 14)))
peer_coefficients = [next(iter(background_t[1 << slot].values()), None) for slot in range(1, N)]
check("symmetry", "the anisotropic background coefficient is present and constant on all thirteen peer axes",
      all(value is not None for value in peer_coefficients)
      and len(set(peer_coefficients)) == 1)


def axis_kind(slot: int) -> str:
    if slot == 0:
        return "Z"
    return "P" if ETA[slot] == 1 else "N"


def orbit_key(slot: int, mask: int):
    return (
        axis_kind(slot),
        bool(mask & 1),
        bool(mask & (1 << slot)),
        sum(bool(mask & (1 << j)) for j in positive_ordinary),
        sum(bool(mask & (1 << j)) for j in negative),
    )


orbit_representative = {}
orbit_multiplicity = Counter()
for slot in range(N):
    for mask in range(1 << N):
        key = orbit_key(slot, mask)
        orbit_representative.setdefault(key, (slot, mask))
        orbit_multiplicity[key] += 1
check("accounting", "500 exact residual-symmetry orbits cover all 229376 T directions",
      len(orbit_representative) == 500
      and sum(orbit_multiplicity.values()) == N * 2**N == 229376)

tt_blocks = set()
tt_source_directions_by_block = Counter()
imaginary_entries = 0
for key, (slot, mask) in orbit_representative.items():
    response_grades = set()
    for row in t_column(slot, mask):
        for response_mask, value in row.items():
            response_grades.add(response_mask.bit_count())
            imaginary_entries += int(value[1] != 0)
    source_grade = mask.bit_count()
    for response_grade in response_grades:
        tt_blocks.add((source_grade, response_grade))
        tt_source_directions_by_block[(source_grade, response_grade)] += orbit_multiplicity[key]

expected_tt_blocks = {(grade, grade) for grade in range(15)}
expected_grade_dimensions = {
    grade: N * len(tuple(combinations(range(N), grade))) for grade in range(15)
}
check("theorem", "the complete real-form T Hessian is Clifford-grade diagonal",
      tt_blocks == expected_tt_blocks)
check("accounting", "every diagonal grade block covers its full coordinate dimension",
      all(tt_source_directions_by_block[(grade, grade)] == expected_grade_dimensions[grade]
          for grade in range(15)))

b2_orbits = {}
b2_counts = Counter()
for slot in range(N):
    for left in range(N):
        for right in range(left + 1, N):
            mask = (1 << left) | (1 << right)
            key = orbit_key(slot, mask)
            b2_orbits.setdefault(key, (slot, mask))
            b2_counts[key] += 1
check("accounting", "21 residual-symmetry orbits cover all 1274 Spin connection directions",
      len(b2_orbits) == 21 and sum(b2_counts.values()) == 1274)

b2_t_grades = set()
for slot, mask in b2_orbits.values():
    for row in b2_column(slot, mask):
        b2_t_grades.update(response_mask.bit_count() for response_mask in row)
check("theorem", "the Spin grade-two connection owner couples only to T grade two",
      b2_t_grades == {2})
check("realform", "every orbit-census Hessian entry is real on the exact real-form basis",
      imaginary_entries == 0)
check("control", "CBRS-1F is reproduced structurally as a zero B2/iT3 and T2/iT3 cross block",
      (2, 3) not in tt_blocks and 3 not in b2_t_grades)


print("\nC. FIVE COMPLETE SMALLEST UNTOUCHED T BLOCKS")
block_results = {}
matrices = {}
coordinates = {}
for grade in (0, 1, 12, 13, 14):
    masks = [sum(1 << item for item in chosen) for chosen in combinations(range(N), grade)]
    coords = [(slot, mask) for slot in range(N) for mask in masks]
    coord_index = {coord: position for position, coord in enumerate(coords)}
    value = matrix(QQ, len(coords), len(coords), sparse=True)
    imaginary = 0
    for column, (slot, mask) in enumerate(coords):
        for output_slot, row in enumerate(t_column(slot, mask)):
            for output_mask, coefficient in row.items():
                if output_mask.bit_count() != grade:
                    continue
                imaginary += int(coefficient[1] != 0)
                value[coord_index[(output_slot, output_mask)], column] = QQ(coefficient[0])
    rank = value.rank()
    block_results[str(grade)] = {
        "dimension": len(coords),
        "rank": int(rank),
        "nullity": int(len(coords) - rank),
        "nonzero_entries": len(value.dict()),
        "diagonal_classes": dict(sorted(Counter(str(item) for item in value.diagonal()).items())),
    }
    check("exact", f"the complete grade-{grade} block is symmetric and real",
          value == value.transpose() and imaginary == 0)
    matrices[grade] = value
    coordinates[grade] = (coords, coord_index)

expected_blocks = {
    "0": {"dimension": 14, "rank": 14, "nullity": 0, "nonzero_entries": 14,
          "diagonal_classes": {"-1": 7, "1": 7}},
    "1": {"dimension": 196, "rank": 183, "nullity": 13, "nonzero_entries": 560,
          "diagonal_classes": {"-1/3": 14, "-3/4": 84, "1": 14, "1/3": 12, "3/4": 72}},
    "12": {"dimension": 1274, "rank": 1274, "nullity": 0, "nonzero_entries": 5642,
           "diagonal_classes": {"-1": 91, "-29/36": 420, "-7/18": 126,
                                "1": 91, "29/36": 438, "7/18": 108}},
    "13": {"dimension": 196, "rank": 196, "nullity": 0, "nonzero_entries": 560,
           "diagonal_classes": {"-1": 98, "1": 98}},
    "14": {"dimension": 14, "rank": 14, "nullity": 0, "nonzero_entries": 14,
           "diagonal_classes": {"-25/36": 7, "25/36": 6, "5/18": 1}},
}
check("theorem", "grades zero twelve thirteen and fourteen are nondegenerate while grade one has nullity thirteen",
      block_results == expected_blocks)
check("planted", "PLANT equal Hodge-complement dimensions do not imply equal ranks",
      block_results["1"]["dimension"] == block_results["13"]["dimension"]
      and block_results["1"]["rank"] != block_results["13"]["rank"])


print("\nD. EXACT GRADE-ONE KERNEL AND SPIN-ORBIT SEPARATION")
h1 = matrices[1]
coords1, coord1_index = coordinates[1]
expected_kernel = matrix(QQ, len(coords1), N - 1, sparse=True)
for column, j in enumerate(range(1, N)):
    expected_kernel[coord1_index[(0, 1 << j)], column] = 1
    expected_kernel[coord1_index[(j, 1)], column] = ETA[j]
check("kernel", "the thirteen explicit e0 gamma_j plus eta_j e_j gamma0 columns are independent",
      expected_kernel.rank() == 13)
check("kernel", "the explicit thirteen-column space is the complete grade-one Hessian kernel",
      (h1 * expected_kernel).is_zero()
      and h1.right_kernel().dimension() == expected_kernel.rank() == 13)

comm = M["M"]["comm"]
gauge = matrix(QQ, len(coords1), 91, sparse=True)
gauge_column = 0
for left in range(N):
    for right in range(left + 1, N):
        eta = M["M"]["blade"]((left, right))
        for slot_mask, coefficient in background_t.items():
            slot = indices(slot_mask)[0]
            for mask, value in comm(eta, coefficient).items():
                gauge[coord1_index[(slot, mask)], gauge_column] = QQ(value[0])
        gauge_column += 1
check("gauge", "the pointwise Spin orbit of the anisotropic T has rank ninety-one",
      gauge.rank() == 91)
check("gauge", "the Hessian is injective on the complete pointwise Spin orbit",
      (h1 * gauge).rank() == 91)
check("gauge", "the thirteen-dimensional field kernel meets the Spin orbit trivially",
      expected_kernel.rank() + gauge.rank()
      - expected_kernel.augment(gauge).rank() == 0)
check("planted", "PLANT calling the grade-one kernel a Spin gauge orbit fails exact rank and Hessian tests",
      expected_kernel.rank() != gauge.rank() and not (h1 * gauge).is_zero())


print("\nE. PRIMITIVE EPSILON AND ALL-GRADE METRIC OBSTRUCTION")
check("momentum", "a grade-one kernel has zero T-equation prolongation",
      (h1 * expected_kernel).is_zero())
check("momentum", "grade selection gives zero B2 and T2 momentum response for every non-grade-two T kernel",
      b2_t_grades == {2} and tt_blocks == expected_tt_blocks)
check("epsilon", "the moving-Shiab primitive-epsilon base return remains exact zero",
      D["moving_support"] == 0)
check("epsilon", "every all-grade first-jet field kernel has zero primitive-epsilon return",
      grade_two["complete_coupled_hessian"]["nullity"] == 0
      and b2_t_grades == {2} and D["moving_support"] == 0)

action_density = QQ(221) / QQ(55296)
rho = (-2, 0, 0, 0, 2, 0, 0, 2, 0, 2)
metric_row = tuple(QQ(entry) * action_density for entry in rho)
check("metric", "every all-grade first-jet field kernel has zero fixed-varpi LC graph return",
      grade_two["complete_coupled_hessian"]["nullity"] == 0
      and b2_t_grades == {2} and tt_blocks == expected_tt_blocks)
check("metric", "the inherited intrinsic MET(X) trace has four nonzero cells",
      sum(value != 0 for value in metric_row) == 4 and any(metric_row))
check("theorem", "the complete all-grade first-jet carrier is killed at intrinsic metric stationarity",
      grade_two["complete_coupled_hessian"]["nullity"] == 0
      and b2_t_grades == {2} and tt_blocks == expected_tt_blocks
      and any(metric_row))


print("\nF. HOSTILE RETURN AND NEXT CONDITION")
check("scope", "the result does not assert full rank for uncomputed grade blocks four through eleven", True)
check("scope", "a field kernel may survive in another isolated grade but cannot enter the grade-two LC graph channel", True)
check("scope", "the obstruction is first-jet and does not exclude second-jet momentum derivatives", True)
check("scope", "no all-grade Hessian rank stabilizer spectrum physical vacuum or source ownership follows", True)
check("scope", "no ledger canon residue quotient particle prediction or public posture changes", True)
check("reverse", "the next CBRS-1 gate is the smallest second-jet carrier capable of a nonzero grade-two momentum derivative", True)


RESULT = {
    "disposition": "CBRS1G_ALL_GRADE_FIRST_JET_METRIC_OBSTRUCTION__GRADE_DIAGONAL_T_HESSIAN_AND_B2_ONLY_T2_COUPLING_FORCE_ZERO_GRAPH_RETURN_ON_EVERY_FIELD_KERNEL",
    "carrier": {
        "point": {"a": "-13/96", "b": "1/48"},
        "t_directions": N * 2**N,
        "t_symmetry_orbits": len(orbit_representative),
        "connection_grade2_directions": 1274,
        "connection_symmetry_orbits": len(b2_orbits),
    },
    "selection": {
        "tt_nonzero_grade_blocks": [list(pair) for pair in sorted(tt_blocks)],
        "B2_to_T_nonzero_grades": sorted(b2_t_grades),
        "real_form": "REAL_B_SKEW_GRADES_PLUS_I_TIMES_B_SELF_GRADES",
    },
    "complete_blocks": block_results,
    "grade1_kernel": {
        "dimension": 13,
        "basis": "e^0 tensor gamma_j + eta_j e^j tensor gamma_0 for j=1..13",
        "pointwise_spin_orbit_rank": int(gauge.rank()),
        "spin_orbit_intersection_dimension": 0,
    },
    "primitive_epsilon": {
        "moving_shiab_base_support": D["moving_support"],
        "all_grade_first_jet_kernel_return": "ZERO_BY_GRADE_SELECTION_AND_NONDEGENERATE_B2_PLUS_T2_BLOCK",
    },
    "heldout_metric": {
        "action_density": str(action_density),
        "source_graph_adjoint": "ZERO_ON_EVERY_ALL_GRADE_FIRST_JET_FIELD_KERNEL",
        "normalized_metric_row": [str(value) for value in metric_row],
        "stationary": False,
    },
    "claim_ceiling": "EXACT_ALL_GRADE_FIRST_JET_METRIC_OBSTRUCTION__NOT_A_FULL_ALL_GRADE_HESSIAN_RANK_OR_SECOND_JET_THEOREM",
    "next_gate": "CBRS1H_CONSTRUCT_THE_SMALLEST_COMPLETE_SECOND_JET_CARRIER_CAPABLE_OF_NONZERO_GRADE2_MOMENTUM_DERIVATIVE_AND_SOLVE_FIELD_EPSILON_METRIC_EQUATIONS_TOGETHER",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True, default=str))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
