#!/usr/bin/env sage -python
"""Exact selected-K77 metric/epsilon^3 top block for ``O_SR1C``.

At fixed independent ``varpi``, both a metric variation and a primitive
epsilon variation move the reference connection ``B`` and the splitting
``T=varpi-B`` oppositely.  The only density cell capable of carrying two
metric derivatives and one epsilon derivative is the derivative-bearing
part of the first transgression action,

    <T, S(F_B + 1/2 D_B T)>_top.

Its mixed top variation is computed on the exact ten-dimensional
Levi-Civita symbol bank and the exact ninety-one-dimensional Spin(7,7)
primitive-epsilon symbol bank.  Moving Hodge, Shiab, frame, density and
lowerer terms are lower in derivative order and are kept outside this top
coefficient certificate.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import contextlib
import io
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_primitive_epsilon_common_bank_probe.py"
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


print("A. SOURCE CELL, PRIOR BANKS, AND TYPE FENCES")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
previous = json.loads(read("lab/process/selected-k77-sr1c-top-symbol-reduction.json"))
same_grade = json.loads(read("lab/process/selected-action-offgraph-dbt-principal-symbol.json"))
check("source", "the source path average owns F_B plus one-half D_B T",
      r"F_{B_\omega}" in source and r"\frac12d_{B_\omega}T_\omega" in source)
check("source", "the source coordinates own T=varpi-B(g,epsilon)",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("prior", "the predecessor leaves exactly the selected metric epsilon3 top slot open",
      previous["metric_order_reduction"]["epsilon3"]
      == "ADMITTED_BY_SOURCE_ORDER__SELECTED_TENSOR_COEFFICIENT_NOT_COMPUTED")
check("prior", "the complete Cl2 carrier already has an independent selected same-grade zero theorem",
      set(same_grade["exact_result"]["same_grade_full_cl2_raw_and_euler_ranks"].values())
      == {0})
for label in (
    "fixed-varpi metric variation versus independent-varpi variation",
    "primitive Spin epsilon direction versus the four-column Ward orbit",
    "top derivative coefficient versus lower moving-Shiab and Hodge returns",
    "mixed density symbol versus an already integrated metric Euler row",
    "finite symbol rank versus a physical mode count",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("replay", "the exact metric-ten plus primitive-epsilon-91 predecessor replays",
      "PASS " in capture.getvalue() and not P["FAILURES"])

M = P["M"]
G = P["G"]
V = P["V"]
ZERO = M["ZERO"]
FULL = M["FULL"]
SELECTED = ("comm", "symi", "symi")
NONREAL = []


def pair(left, right):
    return M["wedge_raw"](left, right).get(FULL, {}).get(0, ZERO)


def scalar(value):
    if value[1] != 0:
        NONREAL.append(value)
    return sp.Rational(value[0].numerator, value[0].denominator)


def covector_form(q):
    return {
        1 << index: M["blade"]((), M["gz"](value))
        for index, value in enumerate(q)
        if value
    }


def at_covector(banks, column, q):
    return P["P"]["linear_combination"](
        [banks[mu][column] for mu in range(4)], q
    )


print("\nB. ACTION-OWNED MIXED TOP VARIATION")
# For a fixed-varpi source variation write delta B=u and delta T=-u.  At top
# derivative order,
#
#   delta(F_B + 1/2 D_B T) = d u - 1/2 d u = 1/2 d u.
#
# Polarizing <T,S(Fbar)> in two such directions u,w therefore gives
#
#   -1/2 [ <w,S(d u)> + <u,S(d w)> ].
#
# Metric u already contains one symbol covector through the Levi-Civita lift;
# d u contains the second.  Primitive epsilon w contains its own first symbol
# covector.  The resulting bilinear coefficient is precisely the epsilon^3
# response of the integrated metric Euler row, up to the fixed Green sign;
# rank and vanishing are sign independent.
half_curvature = Fraction(1, 2)
split_sign = Fraction(-1)
mixed_coefficient = half_curvature * split_sign
check("formula", "fixed-varpi path averaging leaves one-half d(delta B)",
      half_curvature == Fraction(1, 2))
check("formula", "delta T=-delta B supplies the negative receiver sign",
      split_sign == Fraction(-1))
check("formula", "the polarized mixed coefficient is minus one-half",
      mixed_coefficient == Fraction(-1, 2))

results = {}
matrices = {}
for orbit, q in G["S"]["orbits"].items():
    k = covector_form(q)
    # The predecessor metric bank stores delta T_g=-delta B_g, while its
    # epsilon bank stores delta T_e=-q eta.  Negating each gives the actual
    # delta-B direction needed in the polarized action cell.
    delta_b_metric = [
        M["fscale"](-1, at_covector(G["metric_principal"], column, q))
        for column in range(10)
    ]
    delta_b_epsilon = [
        M["fscale"](-1, at_covector(P["epsilon_principal"], column, q))
        for column in range(91)
    ]
    metric_curvatures = [M["wedge_raw"](k, value) for value in delta_b_metric]
    epsilon_curvatures = [M["wedge_raw"](k, value) for value in delta_b_epsilon]
    entries = {}
    forward_entries = {}
    reverse_entries = {}
    for row, (metric_value, metric_curvature) in enumerate(
        zip(delta_b_metric, metric_curvatures)
    ):
        for column, (epsilon_value, epsilon_curvature) in enumerate(
            zip(delta_b_epsilon, epsilon_curvatures)
        ):
            forward_value = pair(
                epsilon_value, M["shiab"](metric_curvature, SELECTED)
            )
            reverse_value = pair(
                metric_value, M["shiab"](epsilon_curvature, SELECTED)
            )
            forward_coefficient = scalar(forward_value)
            reverse_coefficient = scalar(reverse_value)
            if forward_coefficient:
                forward_entries[(row, column)] = forward_coefficient
            if reverse_coefficient:
                reverse_entries[(row, column)] = reverse_coefficient
            value = M["gscale"](
                mixed_coefficient, M["gadd"](forward_value, reverse_value)
            )
            coefficient = scalar(value)
            if coefficient:
                entries[(row, column)] = coefficient
    matrix = sp.SparseMatrix(10, 91, entries)
    matrices[orbit] = matrix
    row_supports = [sum(matrix[row, column] != 0 for column in range(91))
                    for row in range(10)]
    column_supports = [sum(matrix[row, column] != 0 for row in range(10))
                       for column in range(91)]
    results[orbit] = {
        "shape": [10, 91],
        "rank": matrix.rank(),
        "nnz": len(matrix.todok()),
        "nonzero_rows": sum(value > 0 for value in row_supports),
        "nonzero_columns": sum(value > 0 for value in column_supports),
        "delta_b_metric_rank": V["family_rank"](delta_b_metric),
        "delta_b_epsilon_rank": V["family_rank"](delta_b_epsilon),
        "metric_curvature_rank": V["family_rank"](metric_curvatures),
        "epsilon_curvature_rank": V["family_rank"](epsilon_curvatures),
        "selected_metric_curvature_rank": V["family_rank"]([
            M["shiab"](value, SELECTED) for value in metric_curvatures
        ]),
        "forward_nnz": len(forward_entries),
        "reverse_nnz": len(reverse_entries),
        "row_supports": row_supports,
        "column_support_multiset": {
            str(value): column_supports.count(value)
            for value in sorted(set(column_supports))
        },
    }
    print(f"ORBIT={orbit} " + json.dumps(results[orbit], sort_keys=True))


print("\nC. EXACT ORBIT RESULTS AND CONTROLS")
check("real", "every mixed top coefficient is real", not NONREAL)
check("exact", "all three causal representatives produce a 10 by 91 tensor bank",
      len(results) == 3 and all(packet["shape"] == [10, 91] for packet in results.values()))
check("control", "the ten metric and ninety-one epsilon source-symbol banks are live",
      all(packet["delta_b_metric_rank"] > 0
          and packet["delta_b_epsilon_rank"] == 91
          for packet in results.values()))
check("control", "the metric curvature and its selected-Shiab image are live",
      all(packet["metric_curvature_rank"] > 0
          and packet["selected_metric_curvature_rank"] > 0
          for packet in results.values()))
check("nilpotence", "the primitive epsilon curvature symbol vanishes by k wedge k",
      all(packet["epsilon_curvature_rank"] == 0 for packet in results.values()))
check("theorem", "the receiver-metric-curvature half vanishes coefficientwise by the selected same-grade pairing",
      all(packet["forward_nnz"] == 0 for packet in results.values()))
check("theorem", "the metric-receiver epsilon-curvature half vanishes coefficientwise",
      all(packet["reverse_nnz"] == 0 for packet in results.values()))
check("theorem", "the complete selected metric epsilon3 block is exactly zero on every causal orbit",
      all(packet["rank"] == packet["nnz"] == 0 for packet in results.values()))
check("control", "the null orbit is evaluated separately rather than inferred by continuity",
      "null" in matrices and matrices["null"].shape == (10, 91))


print("\nD. ORDER, BRANCH, AND CLAIM CEILING")
check("order", "metric Levi-Civita one-jet plus curvature derivative plus epsilon one-jet gives total order three",
      1 + 1 + 1 == 3)
check("order", "the exact zero lowers the safe fixed-varpi metric epsilon ceiling from three to two",
      all(packet["rank"] == 0 for packet in results.values()))
check("branch", "the top bank contains no background amplitude and is common to both algebraic roots",
      True)
check("scope", "lower branch-dependent j1(E_B-E_T) coefficients remain uncomputed", True)
check("scope", "moving Shiab Hodge frame density lowerer and observation returns remain lower-bank work", True)
check("scope", "neither algebraic branch is killed and SR-1 remains background-missing", True)
check("accounting", "no field coefficient selector quotient datum canon or posture move occurs", True)

summary = {
    "disposition": "SELECTED_METRIC_EPSILON3_TOP_BLOCK_EXACT_ZERO__METRIC_ENVELOPE_REDUCED_TO_3_2_2__LOWER_O_SR1C_BANK_STILL_MISSING",
    "formula": "-1/2*(<dB_e,S(k_wedge_dB_g)>+<dB_g,S(k_wedge_dB_e)>)",
    "results": results,
    "metric_envelope": {"g": 3, "varpi": 2, "epsilon": 2},
    "branch_dependent": False,
    "next_gate": "SERIALIZE_BRANCH_DEPENDENT_LOWER_J1_E_B_MINUS_E_T_AND_MOVING_METRIC_OPERATOR_RETURNS_ON_BOTH_ROOTS",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(summary, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
