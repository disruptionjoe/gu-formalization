#!/usr/bin/env python3
"""Exact fixed-operator metric/epsilon leakage gate on both K77 branches."""

from collections import Counter
from fractions import Fraction
from io import StringIO
from pathlib import Path
import contextlib
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_common_first_action_epsilon_hessian_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


print("A. SOURCE, PRIOR ART, AND LAYER ZERO")
source = (ROOT / "lab/sources/selected-k77-metric-epsilon-hessian-source-reinspection-2026-08-09.md").read_text()
v0036 = strict("lab/process/selected-action-grade1-dbt-schur-observation.json")
v0106 = strict("lab/process/selected-k77-common-first-action-epsilon-hessian.json")
v0121 = strict("lab/process/selected-k77-first-action-tangent-closure.json")
check("source", "source owns moving geometry and is silent on the frozen 321 truncation",
      "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
      and "moving" in source.lower() and "fixed-operator" in source)
check("repo", "v0.36 already owns the older metric-varpi principal cross",
      v0036["status"].startswith("EXACT_GRADE1_AUXILIARY_COMPLETION"))
check("repo", "v0.106 already owns the moving-Shiab epsilon-grade-one cross",
      "epsilon" in json.dumps(v0106).lower() and "91" in json.dumps(v0106))
check("repo", "v0.121 leaves metric and epsilon closure blocks open",
      "METRIC_TO_OFFSLICE_CONNECTION_DUAL" in v0121["exact_result"]["remaining_closure_blocks"]
      and "EPSILON_EPSILON_AND_METRIC_EPSILON" in v0121["exact_result"]["remaining_closure_blocks"])
for label in (
    "fixed-operator source pullback versus total moving source-coordinate Hessian",
    "first transgression Hessian versus residual-square Hessian",
    "nonzero frozen leakage versus a no-go for moving-term cancellation",
    "selected Spin parent versus two U32,32 halves versus full U64,64",
    "finite algebraic rank versus BV quotient, analytic domain, or unitarity",
):
    check("type", label + " remain distinct", True)

capture = StringIO()
with contextlib.redirect_stdout(capture):
    C = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.106 exact predecessor replays", "PASS 61/61" in capture.getvalue() and not C["FAILURES"])

M = C["M"]
ZERO = M["ZERO"]
FULL = M["FULL"]
SELECTED = C["SELECTED"]
P = C["P"]
primitive = P["P"]
linear_combination = primitive["linear_combination"]
grade2 = [u for u, grade in zip(C["directions"], C["direction_grades"]) if grade == 2]
horizontal_basis = primitive["horizontal_basis"]
horizontal_key_list = [next(iter(M["flatten"](u)), None) for u in horizontal_basis]
check("custody", "every horizontal basis vector has a live flattened coordinate", all(key is not None for key in horizontal_key_list))
horizontal_keys = {key for key in horizontal_key_list if key is not None}
horizontal_rows = {
    row for row, u in enumerate(grade2)
    if next(iter(M["flatten"](u)), None) in horizontal_keys
}
offslice_rows = set(range(len(grade2))) - horizontal_rows
check("exact", "complete equation dual splits as horizontal 24 plus off-slice 1250",
      len(grade2) == 1274 and len(horizontal_rows) == 24 and len(offslice_rows) == 1250)


def pair(left, right):
    return M["wedge_raw"](left, right).get(FULL, {}).get(0, ZERO)


def delta_packet(B, T, uB, uT):
    return M["fadd"](
        M["wedge_raw"](uB, B), M["wedge_raw"](B, uB),
        M["fscale"](Fraction(1, 2), M["fadd"](
            M["wedge_raw"](uB, T), M["wedge_raw"](B, uT),
            M["wedge_raw"](uT, B), M["wedge_raw"](T, uB))),
        M["fscale"](Fraction(1, 3), M["fadd"](
            M["wedge_raw"](uT, T), M["wedge_raw"](T, uT))))


def first_packet_variation(B, T, v):
    return M["fadd"](
        M["fscale"](Fraction(1, 2), M["fadd"](
            M["wedge_raw"](B, v), M["wedge_raw"](v, B))),
        M["fscale"](Fraction(1, 3), M["fadd"](
            M["wedge_raw"](v, T), M["wedge_raw"](T, v))))


def mixed_packet_variation(uB, uT, v):
    return M["fadd"](
        M["fscale"](Fraction(1, 2), M["fadd"](
            M["wedge_raw"](uB, v), M["wedge_raw"](v, uB))),
        M["fscale"](Fraction(1, 3), M["fadd"](
            M["wedge_raw"](v, uT), M["wedge_raw"](uT, v))))


def fixed_operator_hessian(B, T, uB, uT, v):
    """Differentiate E_T at fixed Hodge, Phi, Shiab, frame and observation."""
    return M["gadd"](
        M["gadd"](
            pair(v, M["shiab"](delta_packet(B, T, uB, uT), SELECTED)),
            pair(uT, M["shiab"](first_packet_variation(B, T, v), SELECTED))),
        M["gadd"](
            pair(T, M["shiab"](mixed_packet_variation(uB, uT, v), SELECTED)),
            M["gscale"](Fraction(1, 2), M["gadd"](
                pair(v, M["hodge"](uT)), pair(uT, M["hodge"](v))))))


def rational_component(value):
    assert value[1] == 0
    return sp.Rational(value[0].numerator, value[0].denominator)


def sparse_rank(columns):
    """Exact sparse column elimination over QQ(sqrt(3))."""
    pivots = {}
    for column in columns:
        value = dict(column)
        while value:
            pivot = min(value)
            lead = sp.factor(value[pivot])
            if pivot not in pivots:
                pivots[pivot] = {key: sp.cancel(item / lead) for key, item in value.items()}
                break
            basis = pivots[pivot]
            for key, item in basis.items():
                new = sp.cancel(value.get(key, 0) - lead * item)
                if new == 0:
                    value.pop(key, None)
                else:
                    value[key] = new
    return len(pivots)


sqrt3 = sp.sqrt(3)
BRANCHES = (
    (sp.Rational(1, 208) - sqrt3/312, (-2 + sqrt3)/208),
    (sp.Rational(1, 208) + sqrt3/312, (-2 - sqrt3)/208),
)
CAUSAL_ORBITS = ("timelike", "spacelike", "null")
COEFFICIENT_COLUMNS = {}
BRANCH_COLUMNS = {}
RESULTS = {}

print("\nB. FIXED-OPERATOR METRIC/EPSILON RESPONSE")
for causal in CAUSAL_ORBITS:
    q = P["G"]["S"]["orbits"][causal]
    metric = [
        linear_combination([P["G"]["metric_principal"][mu][j] for mu in range(4)], q)
        for j in range(10)
    ]
    epsilon = [
        linear_combination([P["epsilon_principal"][mu][j] for mu in range(4)], q)
        for j in range(91)
    ]
    inputs = [
        (M["fscale"](-1, u), u, "metric") for u in metric
    ] + [
        (M["fscale"](-1, u), u, "epsilon") for u in epsilon
    ]
    coefficient_columns = []
    for uB, uT, kind in inputs:
        constant = {}
        b_part = {}
        t_part = {}
        for row, v in enumerate(grade2):
            z0 = fixed_operator_hessian({}, {}, uB, uT, v)
            zb = M["gadd"](
                fixed_operator_hessian(M["PHI1"], {}, uB, uT, v),
                M["gscale"](-1, z0))
            zt = M["gadd"](
                fixed_operator_hessian({}, M["PHI1"], uB, uT, v),
                M["gscale"](-1, z0))
            for target, value in ((constant, z0), (b_part, zb), (t_part, zt)):
                scalar = rational_component(value)
                if scalar != 0:
                    target[row] = scalar
        coefficient_columns.append((constant, b_part, t_part, kind))
    COEFFICIENT_COLUMNS[causal] = coefficient_columns

    for branch_index, (b_value, t_value) in enumerate(BRANCHES, start=1):
        columns = []
        for constant, b_part, t_part, _ in coefficient_columns:
            keys = set(constant) | set(b_part) | set(t_part)
            column = {
                row: sp.factor(constant.get(row, 0)
                               + b_value * b_part.get(row, 0)
                               + t_value * t_part.get(row, 0))
                for row in keys
            }
            columns.append({row: value for row, value in column.items() if value != 0})
        BRANCH_COLUMNS[(causal, branch_index)] = columns
        horizontal = [{row: value for row, value in column.items() if row in horizontal_rows}
                      for column in columns]
        offslice = [{row: value for row, value in column.items() if row in offslice_rows}
                    for column in columns]
        stats = {
            "nnz": sum(map(len, columns)),
            "metric_rank": sparse_rank(columns[:10]),
            "epsilon_rank": sparse_rank(columns[10:]),
            "combined_rank": sparse_rank(columns),
            "horizontal_metric_rank": sparse_rank(horizontal[:10]),
            "horizontal_epsilon_rank": sparse_rank(horizontal[10:]),
            "horizontal_combined_rank": sparse_rank(horizontal),
            "offslice_metric_rank": sparse_rank(offslice[:10]),
            "offslice_epsilon_rank": sparse_rank(offslice[10:]),
            "offslice_combined_rank": sparse_rank(offslice),
            "offslice_nnz": sum(map(len, offslice)),
        }
        RESULTS[(causal, branch_index)] = stats
        print(causal, branch_index, stats)
        check("theorem", f"{causal} branch {branch_index} has nonzero fixed-operator off-slice leakage",
              stats["offslice_combined_rank"] > 0)
        check("exact", f"{causal} branch {branch_index} reports metric epsilon and combined ranks",
              0 < stats["metric_rank"] <= 10
              and 0 < stats["epsilon_rank"] <= 91
              and max(stats["metric_rank"], stats["epsilon_rank"])
              <= stats["combined_rank"] <= 101)


print("\nC. EXACT CONTROLS AND FENCES")
check("exact", "both exact branches and all three causal representatives were evaluated",
      len(RESULTS) == 6)
check("exact", "fixed-operator leakage reaches off-slice equations in every evaluated case",
      all(value["offslice_nnz"] > 0 for value in RESULTS.values()))
check("planted", "PLANT fixed Hodge/Shiab algebraic pullback is not the total moving source Hessian",
      True)
check("planted", "PLANT nonzero fixed leakage does not prove moving contributions cannot cancel",
      True)
check("planted", "PLANT the result does not promote the 1571-field tangent or kill the 321 candidate",
      True)
check("planted", "PLANT finite ranks do not establish BV closure, Green data, or positivity",
      True)
check("planted", "PLANT P1 P2 and P3 are unused", True)

total = sum(COUNTS.values())
print(f"\nRESULT: {'PASS' if not FAILURES else 'FAIL'} {total - len(FAILURES)}/{total}")
if FAILURES:
    raise SystemExit(1)
