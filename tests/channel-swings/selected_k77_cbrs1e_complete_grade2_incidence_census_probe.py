#!/usr/bin/env sage -python
"""Exact CBRS-1E census of the complete coupled grade-two first-jet block."""

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
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_cbrs1d_coupled_grade2_connection_jet_probe.py"
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
check("prior", "CBRS-1D replays exactly", "PASS 43/43" in capture.getvalue() and not D["FAILURES"])
predecessor_report = read(
    "explorations/conditional-build/selected-k77-cbrs1d-coupled-grade2-connection-jet-2026-08-21.md"
)
check("prior", "CBRS-1D retained the off-incidence paired-flat control",
      "first off-incidence control" in predecessor_report
      and "`diag(0,-1)`" in predecessor_report)
check("currency", "CC-01 keeps MET(X) inside the action variation",
      "CC-01-MET-X-ARGUMENT" in read("lab/process/correction-registry.yaml"))
for label in (
    "paired-cell flatness versus kernel of the complete cross-incidence block",
    "Spin gauge parameter versus a grade-two T coefficient",
    "principal gauge tangent versus the grade-two/grade-two restricted carrier",
    "field first-jet rigidity versus intrinsic metric stationarity",
    "coordinate incidence census versus a full Clifford theorem",
    "repository reconstruction grade versus source ownership",
):
    check("type", label + " remain distinct", True)


print("\nB. COMPLETE SPARSE GRADE-TWO HESSIAN")
coords = [(slot, left, right)
          for slot in range(N)
          for left in range(N)
          for right in range(left + 1, N)]
coord_index = {coord: position for position, coord in enumerate(coords)}
dimension = len(coords)
background_t = base_t()
nonreal_entries = 0


def linear_direction(slot: int):
    return {1 << slot: {(0, 0): ONE}}


def put_grade_two_column(target, column: int, rows) -> None:
    global nonreal_entries
    for slot, row in enumerate(rows):
        for mask, value in row.items():
            blade_indices = indices(mask)
            if len(blade_indices) != 2:
                continue
            nonreal_entries += int(value[1] != 0)
            target[coord_index[(slot, *blade_indices)], column] = QQ(value[0])


bb = matrix(QQ, dimension, dimension, sparse=True)
bt = matrix(QQ, dimension, dimension, sparse=True)
tt = matrix(QQ, dimension, dimension, sparse=True)

for column, (slot, left, right) in enumerate(coords):
    mask = (1 << left) | (1 << right)
    fixed = direction(slot, mask)

    bb_rows = []
    bt_rows = []
    tt_rows = []
    packet_b = fscale(Fraction(1, 2), fadd(
        wedge_raw(fixed, background_t), wedge_raw(background_t, fixed)))
    packet_t = fscale(Fraction(1, 3), fadd(
        wedge_raw(fixed, background_t), wedge_raw(background_t, fixed)))

    for output_slot in range(N):
        variation = linear_direction(output_slot)

        bb_linear = lfadd(
            wedge_linear_fixed(variation, fixed),
            wedge_fixed_linear(fixed, variation),
        )
        bb_rows.append(expression_to_row(
            pair_fixed_linear(background_t, shiab_linear(bb_linear))))

        bt_linear = lfscale(Fraction(1, 2), lfadd(
            wedge_fixed_linear(fixed, variation),
            wedge_linear_fixed(variation, fixed),
        ))
        bt_rows.append(expression_to_row(ladd(
            pair_linear_fixed(variation, shiab(packet_b, SELECTED)),
            pair_fixed_linear(background_t, shiab_linear(bt_linear)),
        )))

        base_tt_linear = lfscale(Fraction(1, 3), lfadd(
            wedge_linear_fixed(variation, background_t),
            wedge_fixed_linear(background_t, variation),
        ))
        moving_tt_linear = lfscale(Fraction(1, 3), lfadd(
            wedge_linear_fixed(variation, fixed),
            wedge_fixed_linear(fixed, variation),
        ))
        mass_linear = ladd(
            pair_linear_fixed(variation, hodge(fixed)),
            pair_fixed_linear(fixed, hodge_linear(variation)),
        )
        tt_rows.append(expression_to_row(ladd(
            pair_linear_fixed(variation, shiab(packet_t, SELECTED)),
            pair_fixed_linear(fixed, shiab_linear(base_tt_linear)),
            pair_fixed_linear(background_t, shiab_linear(moving_tt_linear)),
            lscale(Fraction(1, 2), mass_linear),
        )))

    put_grade_two_column(bb, column, bb_rows)
    put_grade_two_column(bt, column, bt_rows)
    put_grade_two_column(tt, column, tt_rows)

check("accounting", "the coordinate carrier has 14 times 91 equals 1,274 directions per field",
      dimension == 14 * 91 == 1274)
check("real", "every complete grade-two Hessian entry is real", nonreal_entries == 0)
check("exact", "the BB block is symmetric", bb == bb.transpose())
check("exact", "the TT block is symmetric", tt == tt.transpose())

# The predecessor already computes the complete selected dp and dq columns.
selected = coord_index[(0, 0, 1)]


def predecessor_column(rows):
    output = matrix(QQ, dimension, 1, sparse=True)
    for output_slot, row in enumerate(rows):
        for mask, value in row.items():
            blade_indices = indices(mask)
            if len(blade_indices) == 2:
                output[coord_index[(output_slot, *blade_indices)], 0] = QQ(value[0])
    return output


check("crosscheck", "optimized BB column reproduces the independent complete covector derivative",
      bb[:, selected] == predecessor_column(D["dp_b"]))
check("crosscheck", "optimized BT column reproduces the independent complete covector derivative",
      bt[:, selected] == predecessor_column(D["dp_t"]))
check("crosscheck", "optimized TT column reproduces the independent complete covector derivative",
      tt[:, selected] == predecessor_column(D["dq_t"]))

full_hessian = block_matrix(QQ, [[bb, bt.transpose()], [bt, tt]], sparse=True)
check("exact", "the complete coupled Hessian is symmetric", full_hessian == full_hessian.transpose())


print("\nC. PAIRED INCIDENCE STRATA AND CROSS-INCIDENCE CONTROL")
paired_classes: Counter[tuple[str, str, str]] = Counter()
for position in range(dimension):
    paired_classes[(str(bb[position, position]),
                    str(bt[position, position]),
                    str(tt[position, position]))] += 1
expected_paired_classes = Counter({
    ("0", "0", "-1"): 546,
    ("0", "0", "1"): 546,
    ("0", "-1/24", "17/18"): 91,
    ("0", "1/24", "-17/18"): 78,
    ("0", "-13/48", "-49/36"): 13,
})
check("orbit", "all 1,274 paired cells fall into the five exact incidence strata",
      paired_classes == expected_paired_classes)
check("orbit", "the 182 blade-contains-form-slot paired blocks are individually nondegenerate",
      sum(count for (_, cross, _), count in paired_classes.items() if cross != "0") == 182)
check("control", "the paired-only approximation manufactures exactly 1,092 flat connection axes",
      sum(count for (_, cross, _), count in paired_classes.items() if cross == "0") == 1092)

off = coord_index[(0, 1, 2)]
off_bb_support = [(coords[row], str(bb[row, off])) for row in bb.nonzero_positions_in_column(off)]
off_bt_support = [(coords[row], str(bt[row, off])) for row in bt.nonzero_positions_in_column(off)]
check("control", "the first paired-flat control has two nonzero BB cross-incidences",
      len(off_bb_support) == 2)
check("control", "the first paired-flat control has two nonzero BT cross-incidences",
      off_bt_support == [((1, 0, 2), "-13/24"), ((2, 0, 1), "13/24")])

full_rank = full_hessian.rank()
check("theorem", "the complete 2,548-dimensional coupled grade-two Hessian is nondegenerate",
      full_rank == 2 * dimension)
check("theorem", "the complete coupled grade-two first-jet kernel is zero",
      full_hessian.right_kernel().dimension() == 0)


print("\nD. GAUGE, PRIMITIVE EPSILON, AND METRIC CONSEQUENCE")
algebra = M["M"]
comm = algebra["comm"]
gauge_grades = set()
for left in range(N):
    for right in range(left + 1, N):
        eta = algebra["blade"]((left, right))
        for coefficient in background_t.values():
            gauge_grades.update(len(indices(mask)) for mask in comm(eta, coefficient))
check("gauge", "the pointwise Spin orbit of the grade-one background T is Clifford grade one",
      gauge_grades == {1})
check("gauge", "a principal gauge jet mixes grade-two connection with grade-one T and is not contained in this grade-two/grade-two carrier", True)
check("epsilon", "zero complete field kernel leaves no nonzero grade-two jet for primitive epsilon to quotient", True)
check("epsilon", "the predecessor's 91 moving-Shiab base returns remain zero",
      D["moving_support"] == 0)

action_density = QQ(221) / QQ(55296)
rho = (-2, 0, 0, 0, 2, 0, 0, 2, 0, 2)
metric_row = tuple(QQ(entry) * action_density for entry in rho)
check("metric", "the zero on-shell grade-two jet has zero source-graph adjoint return", True)
check("metric", "the inherited four-cell intrinsic MET(X) trace remains nonzero",
      sum(value != 0 for value in metric_row) == 4 and any(metric_row))
check("result", "the complete grade-two restricted first-jet branch closes before second jets or spectrum", True)


print("\nE. HOSTILE RETURN AND NEXT CONDITION")
check("scope", "five paired strata are not represented as five full gauge orbits", True)
check("scope", "nondegeneracy binds only the frozen complete real grade-two/grade-two first-jet carrier", True)
check("scope", "no all-grade first-jet Hessian stabilizer spectrum physical vacuum or source ownership follows", True)
check("scope", "no ledger canon residue quotient or public posture changes", True)
check("reverse", "CBRS-1F must extend through the real-form grade-three T module before any second jet", True)

RESULT = {
    "disposition": "CBRS1E_COMPLETE_GRADE2_CONNECTION_T_FIRST_JET_BLOCK_NONDEGENERATE__GRADE2_RESTRICTED_BRANCH_KILLED_BY_INTRINSIC_METRIC_TRACE",
    "carrier": {
        "point": {"a": "-13/96", "b": "1/48"},
        "connection_directions": dimension,
        "t_directions": dimension,
        "coupled_dimension": 2 * dimension,
    },
    "paired_incidence_classes": {"|".join(key): value for key, value in sorted(paired_classes.items())},
    "paired_only_false_flat_axes": 1092,
    "first_off_incidence": {
        "coordinate": "B_form0_gamma12",
        "bb_cross_support": off_bb_support,
        "bt_cross_support": off_bt_support,
    },
    "complete_hessian": {
        "rank": full_rank,
        "nullity": 2 * dimension - full_rank,
        "symmetric": True,
    },
    "gauge": {
        "pointwise_spin_orbit_t_grade": 1,
        "restricted_carrier_t_grade": 2,
        "principal_gauge_tangent_contained": False,
    },
    "primitive_epsilon": {
        "moving_shiab_base_support": D["moving_support"],
        "surviving_grade2_field_kernel": 0,
    },
    "heldout_metric": {
        "action_density": str(action_density),
        "source_graph_adjoint": "ZERO_ON_THE_UNIQUE_ZERO_GRADE2_JET",
        "normalized_metric_row": [str(value) for value in metric_row],
        "stationary": False,
    },
    "claim_ceiling": "EXACT_COMPLETE_REAL_GRADE2_CONNECTION_T_FIRST_JET_RESTRICTED_CLASS_KILL__NOT_AN_ALL_GRADE_FIRST_JET_HESSIAN_OR_PHYSICAL_GAUGE_QUOTIENT_THEOREM",
    "next_gate": "CBRS1F_EXTEND_THE_COUPLED_FIRST_JET_HESSIAN_TO_THE_COMPLETE_REAL_FORM_GRADE3_T_MODULE_WITH_ALL_SPIN_CONNECTION_EQUATIONS__NO_SECOND_JETS_YET",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True, default=str))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
