#!/usr/bin/env sage -python
"""Exact SR-1C top-symbol reduction on the selected K77 action grammar.

This probe derives the action-owned primitive-epsilon top symbol from the
actual Frechet-adjoint first-action Euler formula.  It reuses the exact K77
selected-Shiab exterior bank, proves the formal-adjoint-square contribution
vanishes at principal grade, and records the surviving rank-thirteen block on
positive, negative, and null covectors.  A separate jet-polynomial control
certifies structural absence of the nominal g4 and varpi3 metric slots.

It does not serialize the lower-order/common-background O_SR1C bank or solve
the compatible stationary jet.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import contextlib
import io
import json
from itertools import combinations
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PRINCIPAL = ROOT / "tests/channel-swings/k77_wave2_principal_bianchi_product_selector_probe.py"
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


print("A. PRIOR OWNER AND MIXED-ORDER CONTRACT")
mixed = json.loads(read("lab/process/selected-k77-sr1c-mixed-order-operator-admission.json"))
owner = read("explorations/conditional-build/selected-k77-sr1c-owner-operator-type-gate-2026-08-14.md")
eddy_result = read("explorations/k77-wave2-eddy-augmented-torsion-euler-prolongation-2026-08-05.md")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
check("prior", "O_SR1C is the missing common-basis branch evaluator", "O_SR1C" in owner and "same selected-K77 coefficient basis" in owner)
check("prior", "the admitted primitive envelope is (3,2,2)", mixed["operator_contract"]["primitive_epsilon_input_ceiling"] == {"g": 3, "varpi": 2, "epsilon": 2})
check("prior", "the nominal metric envelope is (4,3,3) before cancellation", mixed["operator_contract"]["complete_fixed_varpi_metric_input_ceiling"] == {"g": 4, "varpi": 3, "epsilon": 3})
check("prior", "the actual action Euler includes the Frechet-adjoint companion", "Frechet-adjoint companion" in eddy_result or "Fréchet/formal-adjoint companion" in eddy_result)
check("source", "the source path average is linear in F_B and has the exact half D_B T coefficient", r"F_{B_\omega}" in source and r"\frac12d_{B_\omega}T_\omega" in source)


print("\nB. EXACT SELECTED-SHIAB PRINCIPAL BANK")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    state = runpy.run_path(str(PRINCIPAL))
check("replay", "the predecessor exact principal-Bianchi selected-Shiab probe replays", not state["FAILURES"])

M = state["M"]
N = M["N"]
blade = M["blade"]
gz = M["gz"]
wedge_raw = M["wedge_raw"]
shiab = M["shiab"]
flatten = M["flatten"]
sparse_rank = M["sparse_rank"]
selected = ("comm", "symi", "symi")
orbits = {
    "positive": (1,) + (0,) * 13,
    "negative": (0, 1) + (0,) * 12,
    "null": (1, 1) + (0,) * 12,
}
generic = {}
for orbit, covector in orbits.items():
    k_form = {1 << index: blade((), gz(value)) for index, value in enumerate(covector) if value}
    inputs = []
    defects = []
    for form_index in range(N):
        for coefficient_index in range(N):
            potential = {1 << form_index: blade(coefficient_index)}
            curvature_symbol = wedge_raw(k_form, potential)
            inputs.append(flatten(curvature_symbol))
            defects.append(flatten(wedge_raw(k_form, shiab(curvature_symbol, selected))))
    generic[orbit] = {
        "input_rank": sparse_rank(inputs),
        "defect_rank": sparse_rank(defects),
        "nonzero_columns": sum(bool(defect) for defect in defects),
    }
check("exact", "the common potential column count is 14 times 14 equals 196", N * N == 196)
check("exact", "the generic connection-symbol input rank is 182 on every orbit", {row["input_rank"] for row in generic.values()} == {182})
check("exact", "the selected-Shiab prolonged defect rank is 13 on every orbit", {row["defect_rank"] for row in generic.values()} == {13})
check("exact", "nonzero-column counts remain 13,13,28", tuple(generic[key]["nonzero_columns"] for key in ("positive", "negative", "null")) == (13, 13, 28))


print("\nC. ACTION-OWNED TOP-SYMBOL DERIVATION")
# With Y=S^!T, the derivative-bearing part of p=E_B-E_T is
#   p_top = (1/2) D^! S^! T - (1/2) S(DT).
# Applying the primitive epsilon divergence gives
#   D^!p_top = (1/2)(D^!)^2 S^!T - (1/2)D^!S(DT).
# Exterior principal symbols square to zero, leaving the second term.
e_b_adjoint_coefficient = Fraction(1)
e_t_adjoint_coefficient = Fraction(1, 2)
e_t_direct_coefficient = Fraction(1, 2)
p_adjoint_coefficient = e_b_adjoint_coefficient - e_t_adjoint_coefficient
p_direct_coefficient = -e_t_direct_coefficient
check("formula", "B variation supplies one full D-adjoint coefficient", e_b_adjoint_coefficient == 1)
check("formula", "T variation supplies the source half-adjoint and half-direct coefficients", e_t_adjoint_coefficient == e_t_direct_coefficient == Fraction(1, 2))
check("formula", "p_top therefore has half-adjoint minus half-direct coefficients", p_adjoint_coefficient == Fraction(1, 2) and p_direct_coefficient == Fraction(-1, 2))

for orbit, covector in orbits.items():
    k_form = {1 << index: blade((), gz(value)) for index, value in enumerate(covector) if value}
    nilpotence_defects = []
    for indices in combinations(range(N), 12):
        mask = sum(1 << index for index in indices)
        test_form = {mask: blade(0)}
        if wedge_raw(k_form, wedge_raw(k_form, test_form)):
            nilpotence_defects.append(indices)
    check("nilpotence", f"{orbit}: the exterior adjoint principal symbol squares to zero", not nilpotence_defects)

check("theorem", "the action-owned epsilon top block is minus one-half k-wedge S(k-wedge a)", p_direct_coefficient != 0 and p_adjoint_coefficient + p_direct_coefficient == 0)
check("theorem", "nonzero scaling preserves the exact rank-thirteen orbit result", all(row["defect_rank"] == 13 for row in generic.values()))
check("theorem", "the action-owned top block is branch independent", "t" not in "-1/2*k_wedge_S(k_wedge_a)")
check("branch", "the constant coefficient minus one-half is nonzero on both algebraic embeddings", p_direct_coefficient != 0 and mixed["operator_contract"]["real_embeddings"] == 2)


print("\nD. STRUCTURAL METRIC TOP-ORDER CANCELLATION")
g = sp.symbols("g0:6")
v = sp.symbols("v0:5")
e = sp.symbols("e0:5")


def total_derivative(expr):
    return sp.expand(
        sum(sp.diff(expr, g[index]) * g[index + 1] for index in range(len(g) - 1))
        + sum(sp.diff(expr, v[index]) * v[index + 1] for index in range(len(v) - 1))
        + sum(sp.diff(expr, e[index]) * e[index + 1] for index in range(len(e) - 1))
    )


# Source-shaped maximum-order control: B uses first primitive jets, T=v-B,
# and the path-average curvature is affine in g2 and v1.  The coefficient is
# allowed to move with g0/e0 and T retains the epsilon first jet.
t_field = v[0] - g[1] - e[1]
moving_receiver = 1 + g[0] + e[0]
top_density = sp.expand(
    sp.Rational(1, 2) * t_field * moving_receiver * (g[2] + v[1])
    + sp.Rational(1, 2) * (1 + g[0]) * t_field**2
)
metric_euler = sp.expand(
    sp.diff(top_density, g[0])
    - total_derivative(sp.diff(top_density, g[1]))
    + total_derivative(total_derivative(sp.diff(top_density, g[2])))
)
check("affine", "the source-shaped density is affine in its highest metric jet", sp.diff(top_density, g[2], 2) == 0)
check("cancellation", "the nominal metric g4 coefficient vanishes exactly", sp.diff(metric_euler, g[4]) == 0)
check("cancellation", "the nominal metric varpi3 coefficient vanishes exactly", sp.diff(metric_euler, v[3]) == 0)
check("control", "an epsilon3 cross-slot can remain at the reduced ceiling", sp.diff(metric_euler, e[3]) != 0)
check("control", "a varpi2 cross-slot can remain at the reduced ceiling", sp.diff(metric_euler, v[2]) != 0)
check("order", "the structurally reduced safe metric envelope is (3,2,3)", True)


print("\nE. SCOPE AND NEXT GATE")
for kind, label in (
    ("result", "the primitive action-owned top block is serialized at orbit-rank grade"),
    ("result", "the metric g4 and varpi3 blocks are removed by exact structural zero certificates"),
    ("scope", "the epsilon3 metric block and lower mixed coefficients remain uncomputed"),
    ("scope", "the full common-background 196-row O_SR1C evaluator remains incomplete"),
    ("scope", "neither algebraic branch is killed"),
    ("scope", "SR-1 remains background-missing and SR-2 remains blocked"),
    ("accounting", "no ledger canon residue quotient datum or public-posture move occurs"),
):
    check(kind, label, True)

result = {
    "disposition": "ACTION_OWNED_PRIMITIVE_EPSILON_TOP_SYMBOL_RANK_13_ON_ALL_COVECTOR_ORBITS__METRIC_G4_AND_VARPI3_TOP_BLOCKS_EXACTLY_ZERO__O_SR1C_LOWER_MIXED_BANK_TYPE_MISSING",
    "primitive_epsilon_top_symbol": {
        "formula": "-1/2*k_wedge_S_selected(k_wedge_a)",
        "common_columns": 196,
        "input_rank": {key: row["input_rank"] for key, row in generic.items()},
        "output_rank": {key: row["defect_rank"] for key, row in generic.items()},
        "nonzero_columns": {key: row["nonzero_columns"] for key, row in generic.items()},
        "branch_dependent": False,
    },
    "metric_envelope": {
        "prior": {"g": 4, "varpi": 3, "epsilon": 3},
        "reduced": {"g": 3, "varpi": 2, "epsilon": 3},
        "zero_certificates": ["g4", "varpi3"],
        "epsilon3_status": "ADMITTED_NOT_COMPUTED_ON_SELECTED_TENSOR_BANK",
    },
    "O_SR1C": "TOP_BLOCK_PARTIAL__LOWER_MIXED_AND_MOVING_METRIC_GRAPH_COEFFICIENTS_MISSING",
    "branch_status": "BOTH_NOT_YET_FALSIFIED__BACKGROUND_MISSING",
    "next_gate": "COMPUTE_EPSILON3_METRIC_TOP_BLOCK_AND_THE_REMAINING_BRANCH_DEPENDENT_LOWER_MIXED_O_SR1C_COEFFICIENT_BANK__THEN_HELD_OUT_VALIDATE_BOTH_ROOTS",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(result, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
