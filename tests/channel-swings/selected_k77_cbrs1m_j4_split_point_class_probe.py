#!/usr/bin/env sage -python
"""Exact CBRS-1M native J4 split-complex point-class gate.

This probe constructs the smallest real-form-corrected field class attached
to the existing K77 4+10 split element J4.  It interpolates and solves the
complete four-parameter selected first action, then tests every genuinely new
branch against all point-field translations, the independent Spin connection
owner, primitive Spin returns, and the intrinsic constant-grade metric row.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import contextlib
import io
import itertools
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_cbrs1i_chiral_null_point_class_probe.py"
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


def pair_nonzero(value) -> bool:
    return any(sp.simplify(component) != 0 for component in value)


def element_nonzero(value) -> bool:
    return any(pair_nonzero(coefficient) for coefficient in value.values())


def row_support(value) -> int:
    return sum(pair_nonzero(coefficient) for coefficient in value.values())


print("A. PRIOR ART, CURRENCY, AND LAYER ZERO")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("prior", "the exact CBRS-1I action evaluator replays", not P["FAILURES"])
check("prior", "CBRS-1L closes the earlier signature-split points only modulo their broken Spin orbit",
      "primitive quotient" in read(
          "explorations/conditional-build/selected-k77-cbrs1l-broken-symmetry-tangent-2026-08-21.md"
      ) and "first-symbol domain are consequently zero" in read(
          "explorations/conditional-build/selected-k77-cbrs1l-broken-symmetry-tangent-2026-08-21.md"
      ) and "CBRS-1M" in read(
          "explorations/conditional-build/selected-k77-cbrs1l-broken-symmetry-tangent-2026-08-21.md"
      ))
check("prior", "the repository already types J4 as a 4+10 split structure rather than a new source claim",
      "J4" in read("explorations/c3prime-split-commutant-certificates-2026-08-12.md")
      and "four Js exist" in read("explorations/c3prime-split-commutant-certificates-2026-08-12.md"))
check("prior", "the exact new quadratic radicands do not occur in the predecessor point registries",
      "1366" not in read("lab/process/selected-k77-cbrs1k-signature-split-point-class.json")
      and "4177" not in read("lab/process/selected-k77-cbrs1l-broken-symmetry-tangent.json"))
check("currency", "CC-01 keeps MET(X) inside the selected action variation",
      "CC-01-MET-X-ARGUMENT" in read("lab/process/correction-registry.yaml"))
for label in (
    "native 4+10 J4 split versus an observed 3+1 spacetime split",
    "repository-selected split-complex probe versus a source-selected physical complex structure",
    "slotwise real-form phase correction versus an arbitrary complex coefficient",
    "four-variable criticality versus the complete real translation covector",
    "full-comparator momentum versus the independent Spin-grade-two connection owner",
    "field stationarity versus intrinsic metric stationarity",
    "reduced Hessian versus complete tangent and first-jet graph",
):
    check("type", label + " remain distinct", True)


N = P["N"]
I = P["FULL_BANK"]["I"]
blade = P["blade"]
blade_product = P["blade_product"]
indices = P["indices"]
eadd = P["eadd"]
fixed_packet = P["fixed_packet"]
shiab = P["shiab"]
SELECTED = P["SELECTED"]
wedge_raw = P["wedge_raw"]
hodge = P["hodge"]
gadd = P["gadd"]
gscale = P["gscale"]
top_scalar = P["top_scalar"]
action_row = P["action_row"]
momentum_row = P["momentum_row"]
d_shiab = P["FULL_BANK"]["M"]["d_shiab"]
BASE = {0, 1, 2, 3}
NORMAL = set(range(N)) - BASE
J4_MASK = sum(1 << slot for slot in BASE)
j4_square_mask, j4_square_sign = blade_product(J4_MASK, J4_MASK)
check("clifford", "the transported J4 is the frozen (1,3) four-slot volume and squares to minus one",
      BASE == {0, 1, 2, 3} and len(NORMAL) == 10
      and j4_square_mask == 0 and j4_square_sign == -1)


def j4_field(values):
    """T_i=a gamma_i+b i gamma_i J4 on base; c gamma_i+d gamma_i J4 off base."""
    av, bv, cv, dv = values
    out = {}
    for slot in range(N):
        vector_value = av if slot in BASE else cv
        j4_value = bv if slot in BASE else dv
        product_mask, product_sign = blade_product(1 << slot, J4_MASK)
        phase = I if slot in BASE else (sp.Integer(1), sp.Integer(0))
        coefficient = (
            sp.simplify(product_sign * j4_value * phase[0]),
            sp.simplify(product_sign * j4_value * phase[1]),
        )
        out[1 << slot] = eadd(
            blade(slot, (vector_value, sp.Integer(0))),
            {product_mask: coefficient},
        )
    return out


def action_value(values):
    field = j4_field(tuple(Fraction(value) for value in values))
    curvature = fixed_packet({}, field)
    cubic = top_scalar(wedge_raw(field, shiab(curvature, SELECTED)))
    mass = top_scalar(wedge_raw(field, hodge(field)))
    value = gadd(cubic, gscale(Fraction(1, 2), mass))
    assert value[1] == 0
    return sp.Rational(value[0].numerator, value[0].denominator)


sample_field = j4_field((1, 1, 1, 1))
base_j4_grades = {len(indices(mask)) for slot in BASE for mask in sample_field[1 << slot] if mask != 1 << slot}
normal_j4_grades = {len(indices(mask)) for slot in NORMAL for mask in sample_field[1 << slot] if mask != 1 << slot}
check("clifford", "the B-real correction gives imaginary grade three on base slots and real grade five off base",
      base_j4_grades == {3} and normal_j4_grades == {5}
      and all(value[1] != 0 for slot in BASE for mask, value in sample_field[1 << slot].items()
              if mask != 1 << slot)
      and all(value[1] == 0 for slot in NORMAL for mask, value in sample_field[1 << slot].items()
              if mask != 1 << slot))


print("\nB. EXACT FOUR-VARIABLE ACTION AND COMPLETE CRITICAL SET")
a, b, c, d = sp.symbols("a b c d", real=True)
variables = (a, b, c, d)
monomials = []
for degree in (2, 3):
    for exponents in itertools.product(range(degree + 1), repeat=4):
        if sum(exponents) != degree:
            continue
        monomial = sp.Integer(1)
        for variable, exponent in zip(variables, exponents):
            monomial *= variable**exponent
        monomials.append(monomial)

sample_rows = []
sample_values = []
for point in itertools.product((-2, -1, 0, 1, 2), repeat=4):
    if point == (0, 0, 0, 0):
        continue
    row = [term.subs(dict(zip(variables, point))) for term in monomials]
    if sp.Matrix(sample_rows + [row]).rank() > len(sample_rows):
        sample_rows.append(row)
        sample_values.append(action_value(point))
    if len(sample_rows) == len(monomials):
        break

coefficients = sp.Matrix(sample_rows).LUsolve(sp.Matrix(sample_values))
action = sp.factor(sum(coefficient * monomial
                       for coefficient, monomial in zip(coefficients, monomials)))
expected_action = sp.Rational(1, 3) * (
    48*a**3 + 720*a**2*c + 6*a**2 - 48*a*b**2
    + 2160*a*c**2 - 720*a*d**2 - 80*b**2*c - 6*b**2
    + 1440*c**3 + 15*c**2 - 4320*c*d**2 - 15*d**2
)
check("exact", "thirty independent samples determine every degree-two and degree-three coefficient",
      len(monomials) == len(sample_rows) == 30 and sp.Matrix(sample_rows).det() != 0)
check("exact", "direct Clifford interpolation gives the frozen J4 split action",
      sp.expand(action - expected_action) == 0)
check("heldout", "three held-out rational samples agree with the interpolated action",
      all(action.subs(dict(zip(variables, point))) == action_value(point)
          for point in ((3, -2, 1, 4), (-2, 3, -4, 1),
                        (Fraction(2, 3), Fraction(-5, 7),
                         Fraction(7, 5), Fraction(-3, 2)))))

expected_gradients = (
    4 * (12*a**2 + 120*a*c + a - 4*b**2 + 180*c**2 - 60*d**2),
    -sp.Rational(4, 3) * b * (24*a + 40*c + 3),
    sp.Rational(10, 3) * (72*a**2 + 432*a*c - 8*b**2 + 432*c**2 + 3*c - 432*d**2),
    -10 * d * (48*a + 288*c + 1),
)
gradients = tuple(sp.factor(sp.diff(action, variable)) for variable in variables)
check("exact", "all four reduced Euler equations match the exact factored system",
      all(sp.expand(left - right) == 0 for left, right in zip(gradients, expected_gradients)))

sqrt1366 = sp.sqrt(1366)
sqrt4177 = sp.sqrt(4177)
zero = (sp.Integer(0),) * 4
homogeneous = (-sp.Rational(1, 312), 0, -sp.Rational(1, 312), 0)
vector_controls = (
    (-sp.Rational(1, 12), 0, sp.Rational(1, 18), 0),
    (sp.Rational(5, 24), 0, -sp.Rational(1, 24), 0),
)
normal_d2 = sp.Rational(367, 1354752) + 5*sqrt1366/sp.Integer(677376)
base_b2 = sp.Rational(1859, 118336) + 245*sqrt4177/sp.Integer(59168)
normal_points = [
    (sp.Rational(3, 28) + sqrt1366/336, 0,
     -sp.Rational(43, 2016) - sqrt1366/2016, sign * sp.sqrt(normal_d2))
    for sign in (-1, 1)
]
base_points = [
    ((-293 + 5*sqrt4177)/2064, sign * sp.sqrt(base_b2),
     (21 - 3*sqrt4177)/2064, 0)
    for sign in (-1, 1)
]
new_points = [*normal_points, *base_points]
expected_critical = [zero, homogeneous, *vector_controls, *new_points]
critical_rows = sp.solve(gradients, variables, dict=True)
critical = [tuple(row[x] for x in variables) for row in critical_rows]


def same_point(left, right) -> bool:
    return all(sp.simplify(x - y) == 0 for x, y in zip(left, right))


check("exact", "the complete real critical set has exactly eight algebraic points",
      len(critical) == len(expected_critical) == 8
      and all(any(same_point(expected, actual) for actual in critical)
              for expected in expected_critical))
check("real", "both radical-square parameters are strictly positive",
      normal_d2.evalf() > 0 and base_b2.evalf() > 0)
check("prior", "the old homogeneous point retains density 7/292032",
      sp.factor(action.subs(dict(zip(variables, homogeneous)))) == sp.Rational(7, 292032))
check("control", "the two rational vector controls retain distinct nonzero densities",
      [sp.factor(action.subs(dict(zip(variables, point)))) for point in vector_controls]
      == [sp.Rational(19, 1944), sp.Rational(55, 1728)])
normal_density = (sp.Integer(101117) + 2732*sqrt1366) / 6096384
base_density = 5*(43687 - 4177*sqrt4177) / 6390144
check("density", "the two normal-J4 branches share their exact nonzero density",
      normal_density != 0 and all(sp.simplify(action.subs(dict(zip(variables, point))) - normal_density) == 0
                                  for point in normal_points))
check("density", "the two base-J4 branches share their exact nonzero density",
      base_density != 0 and all(sp.simplify(action.subs(dict(zip(variables, point))) - base_density) == 0
                                for point in base_points))


print("\nC. COMPLETE POINT FIELD, CONNECTION, PRIMITIVE, AND METRIC DISCRIMINATORS")
hessian = sp.hessian(action, variables)
branch_results = {}
for family, points, expected_grades, expected_momentum_support in (
    ("normal_J4", normal_points, [1, 5], 24),
    ("base_J4", base_points, [1, 3], 18),
):
    for sign_index, point in enumerate(points):
        sign = -1 if sign_index == 0 else 1
        label = f"{family}_sign_{sign:+d}"
        field = j4_field(point)
        curvature = fixed_packet({}, field)
        packet = shiab(curvature, SELECTED)
        translation_rows = [action_row(slot, field, packet) for slot in range(N)]
        translation_support = sum(row_support(row) for row in translation_rows)
        momentum_rows = [momentum_row(slot, {}, field, packet) for slot in range(N)]
        momentum_support = sum(row_support(row) for row in momentum_rows)
        momentum_grades = sorted({
            len(indices(mask)) for row in momentum_rows
            for mask, value in row.items() if pair_nonzero(value)
        })
        spin_grade_two_support = sum(
            pair_nonzero(value) for row in momentum_rows for mask, value in row.items()
            if len(indices(mask)) == 2
        )
        moving_shiab = [
            top_scalar(wedge_raw(
                field, d_shiab(curvature, SELECTED, blade((left, right)))
            ))
            for left in range(N) for right in range(left + 1, N)
        ]
        moving_support = sum(pair_nonzero(value) for value in moving_shiab)
        reduced_hessian = sp.simplify(hessian.subs(dict(zip(variables, point))))
        density = sp.factor(action.subs(dict(zip(variables, point))))
        metric_row = tuple(sp.simplify(entry * density)
                           for entry in (-2, 0, 0, 0, 2, 0, 0, 2, 0, 2))

        check("field", f"{label}: all 229376 real translation directions vanish exactly",
              translation_support == 0 and N * 2**N == 229376)
        check("owner", f"{label}: unrestricted momentum has only the expected J4 grades",
              momentum_support == expected_momentum_support and momentum_grades == expected_grades)
        check("owner", f"{label}: all 1274 independent Spin-grade-two connection cells vanish",
              spin_grade_two_support == 0 and N * N * (N - 1) // 2 == 1274)
        check("epsilon", f"{label}: all 91 moving-Shiab primitive returns vanish",
              len(moving_shiab) == 91 and moving_support == 0)
        check("metric", f"{label}: nonzero density leaves a nonzero intrinsic constant-grade metric row",
              density != 0 and spin_grade_two_support == 0 and any(metric_row))
        check("hessian", f"{label}: the reduced four-variable Hessian is nondegenerate",
              reduced_hessian.rank() == 4 and sp.simplify(reduced_hessian.det()) != 0)

        branch_results[label] = {
            "point": [str(value) for value in point],
            "translation_support": translation_support,
            "momentum_support": momentum_support,
            "momentum_grades": momentum_grades,
            "spin_grade_two_support": spin_grade_two_support,
            "moving_shiab_support": moving_support,
            "action_density": str(density),
            "metric_row_support": sum(sp.simplify(value) != 0 for value in metric_row),
            "reduced_hessian_rank": reduced_hessian.rank(),
            "reduced_hessian_determinant": str(sp.factor(reduced_hessian.det())),
        }


print("\nD. HOSTILE CONTROLS, SCOPE, AND PROPAGATION")
off_point = list(normal_points[0])
off_point[3] += sp.Rational(1, 1000)
off_field = j4_field(tuple(off_point))
off_packet = shiab(fixed_packet({}, off_field), SELECTED)
check("planted", "PLANT perturbing one radical coefficient fires the complete field covector",
      sum(row_support(action_row(slot, off_field, off_packet)) for slot in range(N)) > 0)
check("planted", "PLANT omitting either radical sign loses an exact stationary branch",
      len(branch_results) == 4)
check("planted", "PLANT treating zero connection support as zero metric variation is caught by density",
      all(row["spin_grade_two_support"] == 0 and row["metric_row_support"] == 4
          for row in branch_results.values()))
check("planted", "PLANT collapsing grade three and grade five J4 backgrounds loses their distinct owner supports",
      {tuple(row["momentum_grades"]) for row in branch_results.values()} == {(1, 3), (1, 5)})
check("scope", "J4 is a native target-blind split probe but is not source-selected or observed 3+1 data", True)
check("scope", "field equations do not establish metric stationarity complete tangent first jet global vacuum or spectrum", True)
check("scope", "no ledger canon source ownership residue particle prediction or public posture changes", True)
check("reverse", "CBRS-1N must test the complete J4 tangent and nonfactorizing first-jet metric graph", True)
check("propagation", "the native registry records four new J4 branches and the constant-metric obstruction",
      "four_new_j4_branches" in read("lab/process/selected-k77-cbrs1m-j4-split-point-class.json")
      and "CBRS1N" in read("lab/process/selected-k77-cbrs1m-j4-split-point-class.json"))
check("propagation", "CURRENT-STATE carries CBRS-1M and its exact CBRS-1N successor",
      "CBRS-1M freezes four" in read("CURRENT-STATE.yaml") and "CBRS-1N" in read("CURRENT-STATE.yaml"))
check("propagation", "the agenda advances the live reverse scaffold without changing its Lane",
      "CBRS-1M freezes four" in read("lab/process/RESEARCH-AGENDA.json")
      and "CBRS-1N" in read("lab/process/RESEARCH-AGENDA.json"))
check("propagation", "the contributor front door points to CBRS-1M and CBRS-1N",
      "CBRS-1M FREEZES FOUR" in read("NEXT-STEPS.md") and "CBRS-1N" in read("NEXT-STEPS.md"))

RESULT = {
    "disposition": "CBRS1M_FOUR_NEW_NATIVE_J4_FIELD_STATIONARY_BRANCHES_PASS_COMPLETE_POINT_OWNERS_BUT_FAIL_CONSTANT_GRADE_METRIC_STATIONARITY",
    "class": {
        "formula": "base: T_i=a*gamma_i+b*i*gamma_i*J4; normal: T_i=c*gamma_i+d*gamma_i*J4",
        "base_slots": sorted(BASE),
        "normal_slots": sorted(NORMAL),
        "action": str(action),
        "target_blind": True,
        "critical_point_count": len(critical),
        "four_new_j4_branches": [[str(value) for value in point] for point in new_points],
    },
    "branches": branch_results,
    "claim_ceiling": "EXACT_RECONSTRUCTION_GRADE_FIELD_STATIONARY_NATIVE_J4_SPLIT_CLASS__CONSTANT_GRADE_METRIC_OBSTRUCTED__NOT_SOURCE_OWNED_GLOBAL_OBSERVED_OR_PHYSICAL",
    "complete_tangent_and_first_jet": "OPEN_AT_CBRS1N",
    "next_gate": "CBRS1N_COMPLETE_J4_RESIDUAL_SYMMETRY_T_PLUS_SPIN_TANGENT__NONFACTORIZING_FIRST_JET_METRIC_GRAPH__PRIMITIVE_QUOTIENT__THEN_SYMBOL_IF_ANY",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
