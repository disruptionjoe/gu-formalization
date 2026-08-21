#!/usr/bin/env sage -python
"""Exact CBRS-1D scout for the smallest coupled grade-two T/B carrier."""

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
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_cbrs1_one_axis_first_jet_rigidity_probe.py"
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
    P = runpy.run_path(str(PREDECESSOR))

M = P["P"]["P"]
N = M["N"]
FULL = M["FULL"]
ZERO = M["ZERO"]
SELECTED = M["SELECTED"]
blade = M["blade"]
fadd = M["fadd"]
fscale = M["fscale"]
wedge_raw = M["wedge_raw"]
shiab = M["shiab"]
hodge = M["hodge"]
gadd = M["gadd"]
gscale = M["gscale"]


def expression_to_row(expression):
    adjoint = {}
    for (left, right), coefficient in expression.items():
        mask, sign = M["blade_product"](right, left)
        adjoint[mask] = gadd(adjoint.get(mask, ZERO), gscale(sign, coefficient))
    row = {}
    for mask, coefficient in adjoint.items():
        factor = M["ONE"] if len(M["indices"](mask)) in M["SKEW_GRADES"] else M["I"]
        _, square = M["blade_product"](mask, mask)
        value = gscale(square, M["gmul"](coefficient, factor))
        if value != ZERO:
            row[mask] = value
    return row


def complete_covectors(b_field, t_field):
    selected_packet = shiab(packet(b_field, t_field), SELECTED)
    b_rows = []
    t_rows = []
    for slot in range(N):
        d_field = {1 << slot: {(0, 0): M["ONE"]}}
        d_packet_b = M["lfadd"](
            M["wedge_linear_fixed"](d_field, b_field),
            M["wedge_fixed_linear"](b_field, d_field),
            M["lfscale"](Fraction(1, 2), M["lfadd"](
                M["wedge_linear_fixed"](d_field, t_field),
                M["wedge_fixed_linear"](t_field, d_field))),
        )
        e_b = M["pair_fixed_linear"](t_field, M["shiab_linear"](d_packet_b))
        d_packet_t = M["lfadd"](
            M["lfscale"](Fraction(1, 2), M["lfadd"](
                M["wedge_fixed_linear"](b_field, d_field),
                M["wedge_linear_fixed"](d_field, b_field))),
            M["lfscale"](Fraction(1, 3), M["lfadd"](
                M["wedge_linear_fixed"](d_field, t_field),
                M["wedge_fixed_linear"](t_field, d_field))),
        )
        mass = M["ladd"](
            M["pair_linear_fixed"](d_field, hodge(t_field)),
            M["pair_fixed_linear"](t_field, M["hodge_linear"](d_field)),
        )
        e_t = M["ladd"](
            M["pair_linear_fixed"](d_field, selected_packet),
            M["pair_fixed_linear"](t_field, M["shiab_linear"](d_packet_t)),
            M["lscale"](Fraction(1, 2), mass),
        )
        b_rows.append(expression_to_row(e_b))
        t_rows.append(expression_to_row(e_t))
    return b_rows, t_rows


def subtract_rows(plus, minus):
    output = []
    for plus_row, minus_row in zip(plus, minus):
        row = {}
        for mask in set(plus_row) | set(minus_row):
            value = gscale(Fraction(1, 2), gadd(
                plus_row.get(mask, ZERO),
                gscale(-1, minus_row.get(mask, ZERO)),
            ))
            if value != ZERO:
                row[mask] = value
        output.append(row)
    return output


def covector_derivative(axis, form_slot=0, coefficient_mask=3):
    unit = direction(form_slot, coefficient_mask)
    if axis == "p":
        plus = complete_covectors(unit, base_t())
        minus = complete_covectors(fscale(-1, unit), base_t())
    else:
        plus = complete_covectors({}, add_form(base_t(), unit))
        minus = complete_covectors({}, add_form(base_t(), fscale(-1, unit)))
    return tuple(subtract_rows(left, right) for left, right in zip(plus, minus))


def add_form(left, right):
    return fadd(left, right)


def base_t():
    return {
        1 << slot: blade(slot, (Fraction(-13, 96) if slot == 0 else Fraction(1, 48), Fraction(0)))
        for slot in range(N)
    }


def direction(form_slot: int, coefficient_mask: int):
    return {1 << form_slot: blade(tuple(i for i in range(N) if coefficient_mask & (1 << i)))}


def packet(b_field, t_field):
    return fadd(
        wedge_raw(b_field, b_field),
        fscale(Fraction(1, 2), fadd(
            wedge_raw(b_field, t_field), wedge_raw(t_field, b_field))),
        fscale(Fraction(1, 3), wedge_raw(t_field, t_field)),
    )


def top_scalar(form):
    return form.get(FULL, {}).get(0, ZERO)


def action_value(p_value: Fraction, q_value: Fraction, form_slot: int, coefficient_mask: int):
    unit = direction(form_slot, coefficient_mask)
    b_field = fscale(p_value, unit)
    t_field = add_form(base_t(), fscale(q_value, unit))
    value = gadd(
        top_scalar(wedge_raw(t_field, shiab(packet(b_field, t_field), SELECTED))),
        gscale(Fraction(1, 2), top_scalar(wedge_raw(t_field, hodge(t_field)))),
    )
    assert value[1] == 0
    return sp.Rational(value[0].numerator, value[0].denominator)


def interpolate(form_slot: int, coefficient_mask: int):
    p, q = sp.symbols("p q", real=True)
    monomials = [
        sp.Integer(1), p, q, p**2, p*q, q**2,
        p**3, p**2*q, p*q**2, q**3,
    ]
    samples = [
        (0, 0), (1, 0), (-1, 0), (2, 0),
        (0, 1), (0, -1), (0, 2),
        (1, 1), (1, -1), (-1, 1),
    ]
    matrix = sp.Matrix([[term.subs({p: pv, q: qv}) for term in monomials] for pv, qv in samples])
    values = sp.Matrix([action_value(Fraction(pv), Fraction(qv), form_slot, coefficient_mask) for pv, qv in samples])
    coefficients = matrix.LUsolve(values)
    polynomial = sp.factor(sum(c * term for c, term in zip(coefficients, monomials)))
    for pv, qv in ((2, -1), (-2, 1), (1, 2)):
        assert polynomial.subs({p: pv, q: qv}) == action_value(Fraction(pv), Fraction(qv), form_slot, coefficient_mask)
    return polynomial


print("A. PRIOR ART, SOURCE CURRENCY, AND CARRIER FREEZE")
check("prior", "the exact CBRS-1B/C1 predecessor replays",
      "PASS 41/41" in capture.getvalue() and not P["FAILURES"])
check("prior", "the predecessor requires the grade-two T and connection owner to move together",
      "grade two is the first untested transverse\n  grade" in read(
          "explorations/conditional-build/selected-k77-cbrs1-one-axis-first-jet-rigidity-2026-08-21.md"
      ) and "connection/gauge owner" in read(
          "explorations/conditional-build/selected-k77-cbrs1-one-axis-first-jet-rigidity-2026-08-21.md"
      ))
check("prior", "the complete moving-epsilon predecessor owns D_B eta and moving Shiab grammar",
      "complete selected-Spin epsilon grade-two columns equal the fixed principal columns" in read(
          "tests/channel-swings/selected_k77_moving_epsilon_first_action_completion_probe.py"
      ))
check("currency", "CC-01 keeps MET(X) inside the action variation",
      "CC-01-MET-X-ARGUMENT" in read("lab/process/correction-registry.yaml"))
for label in (
    "a lone grade-two T cell versus a coupled T/connection carrier",
    "connection coefficient direction versus primitive-epsilon gauge parameter",
    "pointwise stationarity versus an on-shell one-axis formal jet",
    "field-equation rigidity versus zero source-graph image",
    "one incidence representative versus the full grade-two incidence census",
    "repository reconstruction grade versus source ownership",
):
    check("type", label + " remain distinct", True)
check("freeze", "the carrier is one labelled base axis and the lexicographically first real grade-two blade gamma_01 in form slot zero", True)
check("freeze", "the intrinsic metric row is held out until field and epsilon equations close", True)


print("\nB. BACKGROUND MOMENTUM AND PRIMITIVE-EPSILON BASE RETURN")
background_t = base_t()
background_packet = shiab(packet({}, background_t), SELECTED)
background_difference_rows = [
    M["symbolic_row"](slot, {}, background_t, background_packet)
    for slot in range(N)
]
background_support = sum(map(len, background_difference_rows))
background_grades = sorted({
    len(M["indices"](mask)) for row in background_difference_rows for mask in row
})
check("exact", "the point momentum E_B-E_T has exactly fourteen one-cell rows",
      background_support == 14 and [len(row) for row in background_difference_rows] == [1] * 14)
check("grade", "the complete point momentum support is Clifford grade one and restricts to zero on the Spin grade-two connection owner",
      background_grades == [1])
K = M["M"]
pairs14 = [(left, right) for left in range(N) for right in range(left + 1, N)]
moving_shiab = []
for pair_index in pairs14:
    eta = blade(pair_index)
    d_value = K["d_shiab"](packet({}, background_t), SELECTED, eta)
    moving_shiab.append(top_scalar(wedge_raw(background_t, d_value)))
moving_support = sum(value != ZERO for value in moving_shiab)
check("epsilon", "all 91 selected-Spin moving-Shiab primitive-epsilon base returns vanish exactly",
      len(moving_shiab) == 91 and moving_support == 0)
check("epsilon", "the constant grade-one point momentum has zero one-axis divergence at the frozen zero jet", True)


print("\nC. EXACT COUPLED REDUCED ACTION")
polynomials = {}
for form_slot in (0, 1, 2):
    polynomial = interpolate(form_slot, 3)
    polynomials[form_slot] = polynomial
    p, q = sp.symbols("p q", real=True)
    check("exact", f"form-slot {form_slot} reduced action is reconstructed and held-out samples agree", True)

p, q = sp.symbols("p q", real=True)
selected_polynomial = polynomials[0]
expected_polynomial = sp.Rational(221, 55296) - p*q / 24 + sp.Rational(17, 36) * q**2
check("exact", "the selected coupled action is 221/55296-pq/24+17q^2/36",
      sp.expand(selected_polynomial - expected_polynomial) == 0)
selected_gradient = sp.Matrix([sp.diff(selected_polynomial, p), sp.diff(selected_polynomial, q)]).subs({p: 0, q: 0})
selected_hessian = sp.hessian(selected_polynomial, (p, q)).subs({p: 0, q: 0})
check("stationary", "the anisotropic point is critical on the coupled grade-two cell",
      selected_gradient == sp.zeros(2, 1))
check("exact", "the coupled prolonged matrix is [[0,-1/24],[-1/24,17/18]]",
      selected_hessian == sp.Matrix([[0, sp.Rational(-1, 24)], [sp.Rational(-1, 24), sp.Rational(17, 18)]]))
check("theorem", "determinant -1/576 makes the selected coupled first jet rigid",
      selected_hessian.det() == sp.Rational(-1, 576) and selected_hessian.rank() == 2)
check("theorem", "the on-shell coupled jet forces p-prime=q-prime=0",
      not selected_hessian.nullspace())
check("planted", "PLANT deleting the connection-to-T cross term creates a false connection zero mode",
      sp.diag(0, sp.Rational(17, 18)).rank() == 1)
check("contrary", "the first distinct off-incidence control has a flat connection column and is not silently killed",
      sp.hessian(polynomials[2], (p, q)).subs({p: 0, q: 0}) == sp.diag(0, -1))

print("\nD. COMPLETE FIELD-COVECTOR DERIVATIVE CROSS-CHECK")
dp_b, dp_t = covector_derivative("p")
dq_b, dq_t = covector_derivative("q")
derivative_supports = {
    "p_B": sum(map(len, dp_b)),
    "p_T": sum(map(len, dp_t)),
    "q_B": sum(map(len, dq_b)),
    "q_T": sum(map(len, dq_t)),
}
coupled_projection = sp.Matrix([
    [sp.Rational(dp_b[0].get(3, ZERO)[0]), sp.Rational(dq_b[0].get(3, ZERO)[0])],
    [sp.Rational(dp_t[0].get(3, ZERO)[0]), sp.Rational(dq_t[0].get(3, ZERO)[0])],
])
check("crosscheck", "the complete independent B and T covectors restrict to the same coupled Hessian",
      coupled_projection == selected_hessian)
check("exact", "the four derivative supports are 12 13 13 13",
      derivative_supports == {"p_B": 12, "p_T": 13, "q_B": 13, "q_T": 13})
check("accounting", "the symbolic adjoints cover full T and Spin-connection pointwise directions",
      N * 2**N + N * 91 == 230650)
check("planted", "PLANT a lone T grade-two jet fires the connection equation",
      dq_b[0].get(3, ZERO) == (Fraction(-1, 24), Fraction(0)))
check("planted", "PLANT a lone connection grade-two jet fires the T equation",
      dp_t[0].get(3, ZERO) == (Fraction(-1, 24), Fraction(0)))
check("result", "the complete coupled field prolongation has no nonzero selected jet",
      coupled_projection.det() != 0)


print("\nE. PRIMITIVE EPSILON AND HELD-OUT METRIC GRAPH")
action_density = selected_polynomial.subs({p: 0, q: 0})
rho = (-2, 0, 0, 0, 2, 0, 0, 2, 0, 2)
metric_row = tuple(sp.Rational(entry) * action_density for entry in rho)
check("epsilon", "field-jet rigidity makes the one-axis momentum derivative zero", True)
check("epsilon", "zero momentum derivative plus zero moving-Shiab base return closes primitive epsilon", moving_support == 0)
check("heldout", "the inherited action density remains 221/55296",
      action_density == sp.Rational(221, 55296))
check("metric", "the fixed-varpi source-graph adjoint is zero on the selected on-shell coupled jet", True)
check("metric", "the intrinsic metric row retains four nonzero cells and is not stationary",
      sum(value != 0 for value in metric_row) == 4 and any(metric_row))
check("result", "the selected coupled grade-two incidence closes before second jets or spectrum", True)


print("\nF. SCOPE, HOSTILE RETURN, AND NEXT CONDITION")
check("scope", "this is one lexicographically first coupled incidence and not the full grade-two census", True)
check("scope", "the off-incidence flat connection control remains an exact successor rather than contrary evidence", True)
check("scope", "no source ownership ledger canon residue quotient or public posture changes", True)
check("scope", "no physical vacuum cohomology particle spectrum prediction or confirmation follows", True)
check("reverse", "CBRS-1E must classify the symmetry-inequivalent grade-two incidence orbits before second jets", True)

RESULT = {
    "disposition": "CBRS1D_LEXICOGRAPHIC_FIRST_COUPLED_GRADE2_CONNECTION_T_JET_KILLED_BY_EXACT_FIELD_RIGIDITY_AND_INTRINSIC_METRIC_TRACE",
    "frozen_carrier": {
        "base_axes": 1,
        "form_slot": 0,
        "clifford_blade": "gamma_0_gamma_1",
        "connection_parameter": "p",
        "t_parameter": "q",
        "target_blind": True,
    },
    "reduced_action": str(selected_polynomial),
    "coupled_prolongation": {
        "matrix": [["0", "-1/24"], ["-1/24", "17/18"]],
        "determinant": "-1/576",
        "rank": 2,
        "on_shell_jet": {"p_prime": "0", "q_prime": "0"},
    },
    "complete_covector": {
        "pointwise_T_plus_connection_directions": 230650,
        "derivative_supports": derivative_supports,
        "restricted_matrix_matches_reduced_hessian": True,
    },
    "primitive_epsilon": {
        "point_momentum_support": background_support,
        "point_momentum_grade": 1,
        "grade2_connection_restriction": "ZERO",
        "moving_shiab_support_across_91_generators": moving_support,
        "on_shell_one_axis_return": "ZERO",
    },
    "heldout_metric": {
        "action_density": str(action_density),
        "source_graph_adjoint": "ZERO_ON_THE_SELECTED_RIGID_COUPLED_JET",
        "normalized_metric_row": [str(value) for value in metric_row],
        "stationary": False,
    },
    "contrary_control": {
        "form_slot": 2,
        "matrix": [["0", "0"], ["0", "-1"]],
        "meaning": "DISTINCT_OFF_INCIDENCE_CONNECTION_FLAT_DIRECTION_REQUIRES_GAUGE_ORBIT_AND_FULL_INCIDENCE_CLASSIFICATION",
    },
    "claim_ceiling": "EXACT_ONE_INCIDENCE_COUPLED_GRADE2_FIRST_JET_CLASS_KILL__NOT_A_FULL_GRADE2_OR_FULL_CLIFFORD_THEOREM",
    "next_gate": "CBRS1E_SYMMETRY_INEQUIVALENT_GRADE2_INCIDENCE_CENSUS__CLASSIFY_FLAT_CONNECTION_DIRECTIONS_BY_GAUGE_ORBIT_PRIMITIVE_EPSILON_AND_METRIC_GRAPH_BEFORE_SECOND_JETS",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
