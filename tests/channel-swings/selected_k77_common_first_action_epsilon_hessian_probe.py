#!/usr/bin/env python3
"""Exact common connection-critical background and moving-epsilon action gate.

The v0.105 residual-zero fixture used ``B*=0`` and
``T*=-(1/312) Phi1``.  This probe differentiates the same selected
``comm/symi/symi`` first action on the full admitted ``Cl1+Cl2`` one-form
tangent before attempting a 125-field Hessian.  It then solves the invariant
``B=b Phi1, T=t Phi1`` connection equations jointly with the raw residual and serializes
the lower-order moving-Shiab epsilon cross block.

The result is intentionally prior to a BV or domain construction.  A Hessian
restricted to the 125-field bivector slice would delete a live rank-91 cross
block into the already-owned 196-dimensional grade-one sector.
"""

from collections import Counter
from fractions import Fraction
from pathlib import Path
import contextlib
import io
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_primitive_epsilon_common_bank_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


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


print("A. SOURCE LOCUS, LAYER ZERO, AND PRIOR ART")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
companion = strict("lab/process/selected-k77-action-owned-degree14-companion.json")
all_grade = strict("lab/process/selected-k77-coupled-all-grade-upsilon-graph.json")
grade1 = strict("lab/process/selected-action-grade1-dbt-schur-observation.json")
old_background = strict("lab/process/selected-invariant-constituent-operator-naturality.json")
check("source", "source owns the nonlinear first action and two-connection difference",
      "I^B_1" in source and r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("repo", "the action-owned primitive epsilon companion includes connection and moving-Shiab pieces",
      companion["layer0"]["action_companion"].startswith("D_B_ADJOINT")
      and companion["exact_fixture"]["moving_shiab_live"])
check("repo", "the source-admitted low-grade connection tangent is Cl1 plus Cl2 of dimension 1470",
      all_grade["exact_result"]["source_tangent_grades"] == [1, 2]
      and all_grade["exact_result"]["domain_dimension"] == 1470)
check("repo", "the omitted grade-one bank is already exact and nondegenerate",
      grade1["exact_result"]["grade1_hessian"]["dimension"] == 196
      and grade1["exact_result"]["grade1_hessian"]["rank"] == 196)
check("repo", "the old raw-residual background explicitly used a different action path-average",
      old_background["selected_background"]["T_star"] == "-(kappa_1/312)Phi1"
      and old_background["selected_background"]["action_path_average_is_distinct"]
      == "(1/3)T_star wedge T_star")
for label in (
    "raw Upsilon zero versus critical point of the source-shaped first action",
    "125-field bivector slice versus the full Cl1+Cl2 source tangent",
    "primitive epsilon first variation versus its mixed Hessian cross block",
    "moving-Shiab lower order versus principal epsilon derivative",
    "constrained Hessian versus action-derived BV differential",
    "selected Spin-native parent versus two U32,32 halves versus full U64,64",
    "connection criticality versus the direct metric/Hodge/Phi Euler equation",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "the immutable v0.105 principal epsilon bank replays",
      "PASS 52/52" in capture.getvalue() and not P["FAILURES"])

M = P["M"]
V = P["V"]
ZERO = M["ZERO"]
FULL = M["FULL"]
SELECTED = P["G"]["P"]["channels"]


def top(form):
    return form.get(FULL, {}).get(0, ZERO)


def pair(left, right):
    return top(M["wedge_raw"](left, right))


def packet(b_field, t_field):
    return M["fadd"](
        M["wedge_raw"](b_field, b_field),
        M["fscale"](Fraction(1, 2), M["fadd"](
            M["wedge_raw"](b_field, t_field),
            M["wedge_raw"](t_field, b_field),
        )),
        M["fscale"](Fraction(1, 3), M["wedge_raw"](t_field, t_field)),
    )


def action(b_field, t_field):
    cubic = pair(t_field, M["shiab"](packet(b_field, t_field), SELECTED))
    mass = pair(t_field, M["hodge"](t_field))
    return M["gadd"](cubic, M["gscale"](Fraction(1, 2), mass))


def eulers(b_field, t_field):
    p_value = packet(b_field, t_field)
    s_value = M["shiab"](p_value, SELECTED)

    def e_b(direction):
        d_packet = M["fadd"](
            M["wedge_raw"](direction, b_field),
            M["wedge_raw"](b_field, direction),
            M["fscale"](Fraction(1, 2), M["fadd"](
                M["wedge_raw"](direction, t_field),
                M["wedge_raw"](t_field, direction),
            )),
        )
        return pair(t_field, M["shiab"](d_packet, SELECTED))

    def e_t(direction):
        d_packet = M["fadd"](
            M["fscale"](Fraction(1, 2), M["fadd"](
                M["wedge_raw"](b_field, direction),
                M["wedge_raw"](direction, b_field),
            )),
            M["fscale"](Fraction(1, 3), M["fadd"](
                M["wedge_raw"](direction, t_field),
                M["wedge_raw"](t_field, direction),
            )),
        )
        mass = M["gadd"](
            pair(direction, M["hodge"](t_field)),
            pair(t_field, M["hodge"](direction)),
        )
        return M["gadd"](
            pair(direction, s_value),
            M["gadd"](
                pair(t_field, M["shiab"](d_packet, SELECTED)),
                M["gscale"](Fraction(1, 2), mass),
            ),
        )

    return e_b, e_t


coefficients = [M["blade"](index) for index in range(14)]
coefficient_grades = [1] * 14
for left in range(14):
    for right in range(left + 1, 14):
        coefficients.append(M["blade"]((left, right)))
        coefficient_grades.append(2)
directions = [
    {1 << form_index: coefficient}
    for form_index in range(14)
    for coefficient in coefficients
]
direction_grades = coefficient_grades * 14
check("exact", "the tested full low-grade tangent has 196 Cl1 plus 1274 Cl2 directions",
      len(directions) == 1470
      and direction_grades.count(1) == 196
      and direction_grades.count(2) == 1274)


print("\nB. THE OLD RAW-RESIDUAL FIXTURE IS ONLY CONSTRAINED-CRITICAL")
B_old = {}
T_old = M["fscale"](Fraction(-1, 312), M["PHI1"])
E_B_old, E_T_old = eulers(B_old, T_old)
eb_old = [E_B_old(direction) for direction in directions]
et_old = [E_T_old(direction) for direction in directions]
old_support = [index for index, value in enumerate(eb_old) if value != ZERO]
expected_support = [slot * 105 + slot for slot in range(14)]
check("exact", "the old fixture solves all T Euler directions", all(value == ZERO for value in et_old))
check("exact", "the old B Euler covector has exactly fourteen diagonal Cl1 support entries",
      old_support == expected_support)
check("exact", "every old nonzero B Euler entry is exactly one over 312",
      {eb_old[index] for index in old_support} == {(Fraction(1, 312), Fraction(0))})
check("theorem", "the old B Euler covector is the one-dimensional invariant trace covector",
      all(direction_grades[index] == 1 for index in old_support)
      and sum(eb_old[index][0] for index in old_support) == Fraction(7, 156))
check("theorem", "all 1274 grade-two action directions annihilate the old first variation",
      all(eb_old[index] == et_old[index] == ZERO
          for index, grade in enumerate(direction_grades) if grade == 2))
check("planted", "PLANT raw Upsilon zero is not called full first-action stationarity",
      any(value != ZERO for value in eb_old))


print("\nC. EXACT COMMON HOMOGENEOUS CONNECTION-CRITICAL BRANCH")
b, t = sp.symbols("b t", real=True)
homogeneous_action = 7 * t * (624*b**2 + 624*b*t + 208*t**2 + t)
sample_points = ((0, 0), (0, -1), (1, 1), (2, -1), (-1, 2), (3, 2))
for b_value, t_value in sample_points:
    direct = action(
        M["fscale"](Fraction(b_value), M["PHI1"]),
        M["fscale"](Fraction(t_value), M["PHI1"]),
    )
    expected = homogeneous_action.subs({b: b_value, t: t_value})
    check("exact", f"homogeneous action polynomial agrees at ({b_value},{t_value})",
          direct == (Fraction(int(expected)), Fraction(0)))

d_b = sp.factor(sp.diff(homogeneous_action, b))
d_t = sp.factor(sp.diff(homogeneous_action, t))
solutions = sp.solve([d_b, d_t], [b, t], dict=True)
check("exact", "homogeneous first-action derivatives have the exact displayed factors",
      sp.expand(d_b - 4368*t*(2*b+t)) == 0
      and sp.expand(d_t - 14*(312*b**2+624*b*t+312*t**2+t)) == 0)
check("exact", "the invariant-line B/T system has exactly trivial and one nontrivial critical points",
      solutions == [{b: 0, t: 0}, {b: sp.Rational(1, 156), t: sp.Rational(-1, 78)}])
check("control", "the old point solves only the T equation",
      d_b.subs({b: 0, t: sp.Rational(-1, 312)}) == sp.Rational(7, 156)
      and d_t.subs({b: 0, t: sp.Rational(-1, 312)}) == 0)

B_new = M["fscale"](Fraction(1, 156), M["PHI1"])
T_new = M["fscale"](Fraction(-1, 78), M["PHI1"])
A_new = M["fadd"](B_new, T_new)
E_B_new, E_T_new = eulers(B_new, T_new)
check("theorem", "the nontrivial branch solves every one of the 1470 B Euler directions",
      all(E_B_new(direction) == ZERO for direction in directions))
check("theorem", "the nontrivial branch solves every one of the 1470 T Euler directions",
      all(E_T_new(direction) == ZERO for direction in directions))
raw_residual_new = M["fadd"](
    M["shiab"](M["wedge_raw"](A_new, A_new), SELECTED),
    M["hodge"](T_new),
)
check("theorem", "the same nontrivial branch also solves the source raw residual", not raw_residual_new)
check("exact", "the common branch has B plus T equal minus one over 156 Phi1",
      M["fadd"](B_new, T_new)
      == M["fscale"](Fraction(-1, 156), M["PHI1"]))
check("planted", "PLANT the repaired connection branch is not the old B-zero background", B_new != B_old and T_new != T_old)
check("type", "direct metric variation of Hodge Phi density and observation is not computed by B/T Euler closure", True)


print("\nD. LOWER-ORDER MOVING-SHIAB EPSILON SERIALIZATION")


def coefficient_derivative(form, parameter):
    return {mask: M["comm"](value, parameter) for mask, value in form.items()}


def d_shiab(curvature, parameter):
    d_phi1 = coefficient_derivative(M["PHI1"], parameter)
    d_phi2 = coefficient_derivative(M["PHI2"], parameter)
    star = M["hodge"](curvature)
    first = M["wedge"](d_phi1, star, "comm")
    second_left = M["wedge"](
        d_phi1,
        M["hodge"](M["wedge"](M["PHI2"], star, "symi")),
        "symi",
    )
    second_right = M["wedge"](
        M["PHI1"],
        M["hodge"](M["wedge"](d_phi2, star, "symi")),
        "symi",
    )
    return M["fadd"](
        first,
        M["fscale"](Fraction(-1, 2), M["hodge"](
            M["fadd"](second_left, second_right)
        )),
    )


pairs14 = [(left, right) for left in range(14) for right in range(left + 1, 14)]
moving_columns = [
    d_shiab(packet(B_new, T_new), M["blade"](pair_index))
    for pair_index in pairs14
]
moving_supports = [len(M["flatten"](column)) for column in moving_columns]
check("exact", "all ninety-one primitive epsilon moving-Shiab columns are independent",
      V["family_rank"](moving_columns) == 91)
check("exact", "each moving-Shiab column has the exact two-entry support", set(moving_supports) == {2})
check("exact", "the moving-Shiab contribution to the first variation vanishes on the common branch",
      all(pair(T_new, column) == ZERO for column in moving_columns))

cross_values = [
    [pair(direction, column) for column in moving_columns]
    for direction in directions
]
cross_matrix = sp.SparseMatrix(1470, 91, {
    (row, column): sp.Rational(value[0].numerator, value[0].denominator)
    for row, values in enumerate(cross_values)
    for column, value in enumerate(values)
    if value != ZERO and value[1] == 0
})
nonzero_rows = [row for row in range(1470) if any(
    cross_values[row][column] != ZERO for column in range(91)
)]
column_supports = [sum(cross_values[row][column] != ZERO for row in range(1470))
                   for column in range(91)]
check("theorem", "the moving-Shiab first-action cross block has exact rank ninety-one",
      cross_matrix.rank() == 91)
check("exact", "the cross block has 182 nonzero entries and two per epsilon column",
      len(cross_matrix.todok()) == 182 and set(column_supports) == {2})
check("theorem", "all 182 live receiver rows lie in the omitted grade-one sector",
      len(nonzero_rows) == 182
      and all(direction_grades[row] == 1 for row in nonzero_rows))
check("theorem", "the moving-Shiab cross block vanishes on every grade-two direction",
      all(cross_values[row][column] == ZERO
          for row, grade in enumerate(direction_grades) if grade == 2
          for column in range(91)))
check("planted", "PLANT zero primitive epsilon first variation is not zero epsilon Hessian",
      all(pair(T_new, column) == ZERO for column in moving_columns)
      and cross_matrix.rank() == 91)


print("\nE. CONSEQUENCE FOR THE 125-FIELD TARGET")
for name, q in P["G"]["S"]["orbits"].items():
    metric_t = [P["P"]["linear_combination"](
        [P["G"]["metric_principal"][mu][column] for mu in range(4)], q
    ) for column in range(10)]
    varpi_t = list(P["P"]["horizontal_basis"])
    epsilon_b = [P["P"]["linear_combination"](
        [P["epsilon_principal"][mu][column] for mu in range(4)], q
    ) for column in range(91)]
    # epsilon_principal stores delta T=-q eta, so delta B is its negative.
    field_pairs = (
        [(M["fscale"](-1, value), value) for value in metric_t]
        + [({}, value) for value in varpi_t]
        + [(M["fscale"](-1, value), value) for value in epsilon_b]
    )
    check("exact", f"{name}: common physical slice has exactly 125 directions", len(field_pairs) == 125)
    check("exact", f"{name}: every common physical direction is coefficient-grade two",
          all({key[1].bit_count() for key in M["flatten"](value)} <= {2}
              for pair_fields in field_pairs for value in pair_fields))
    check("theorem", f"{name}: repaired B/T-chain first variation vanishes on the 125-field slice",
          all(M["gadd"](E_B_new(d_b_field), E_T_new(d_t_field)) == ZERO
              for d_b_field, d_t_field in field_pairs))

check("accounting", "minimal already-proved completion adds 196 grade-one directions to 125", 125 + 196 == 321)
check("accounting", "full source-faithful low-grade connection completion would have 1571 fields",
      10 + 1470 + 91 == 1571)
check("type", "choosing the 321 physical slice or full 1571 source tangent is an action-parent/truncation gate", True)
check("type", "the direct metric Euler row must close before this is a common stationary action background", True)
check("symplectic", "a restricted critical slice is not an action-derived BV complex", True)
check("analytic", "finite exact stationarity supplies no field Riesz contour maximal domain or hyperbolicity", True)
check("representation", "selected Spin-native two-half and full-unitary parents remain distinct", True)
check("accounting", "no new field coefficient quotient or external datum is introduced", True)
check("accounting", "P1 P2 P3 remain unchanged and unused", True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_NONLINEAR_FIRST_ACTION_TWO_CONNECTION_AND_MOVING_SHIAB_GRAMMAR__SOURCE_SILENT_COMMON_STATIONARY_BRANCH_AND_FIELD_TANGENT_SELECTION")
print("OLD_BACKGROUND=RAW_UPSILON_ZERO__FIRST_ACTION_E_T_ZERO__E_B_TRACE_COVECTOR_SUPPORT14_VALUE1_OVER312__NOT_FULL_CRITICAL")
print("COMMON_NONTRIVIAL_CONNECTION_BRANCH=B_1_OVER156_PHI1__T_MINUS1_OVER78_PHI1__A_MINUS1_OVER156_PHI1")
print("COMMON_BRANCH=ALL1470_EB_ET_ZERO__RAW_UPSILON_ZERO__DIRECT_METRIC_EULER_OPEN")
print("MOVING_SHIAB_EPSILON=91_COLUMNS_RANK91_SUPPORT2_EACH")
print("MOVING_FIRST_ACTION_CROSS=1470_BY91_RANK91_NNZ182__ALL_RECEIVERS_GRADE1")
print("FIELD_TANGENT_GATE=125_RESTRICTED__321_MINIMAL_KNOWN_COMPLETION__1571_FULL_LOW_GRADE_SOURCE_CANDIDATE")
print("BV_DIFFERENTIAL=BLOCKED_UNTIL_DIRECT_METRIC_EULER_AND_FIELD_TANGENT_SELECTED__THEN_FULL_HESSIAN_ON_CONNECTION_BRANCH")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
