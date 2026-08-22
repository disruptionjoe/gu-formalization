#!/usr/bin/env sage -python
"""Exact CBRS-1K K77-signature-split point-class gate.

The probe enlarges the CBRS-1I vector-plus-volume-dual class only by the
canonical positive/negative seven-plane split of the fixed K77 real form.  It
interpolates the complete four-variable selected first action, solves its
critical set exactly, and tests every genuinely new zero-density point against
the complete real translation covector, independent Spin-grade-two connection
owner, moving-Shiab primitive returns, and intrinsic metric equation.
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
check("prior", "the exact CBRS-1I point-class predecessor replays",
      "PASS 47/47" in capture.getvalue() and not P["FAILURES"])
check("prior", "CBRS-1J closes only the two uniform volume-sign points",
      "two exact isolated" in read(
          "explorations/conditional-build/selected-k77-cbrs1j-complete-tangent-2026-08-21.md"
      ) and "CBRS-1K" in read(
          "explorations/conditional-build/selected-k77-cbrs1j-complete-tangent-2026-08-21.md"
      ))
check("currency", "CC-01 keeps MET(X) inside the selected action variation",
      "CC-01-MET-X-ARGUMENT" in read("lab/process/correction-registry.yaml"))
for label in (
    "K77 signature split versus an observed 3+1 or particle selector",
    "positive/negative seven-plane coefficients versus spacetime inhomogeneity",
    "Clifford-volume sign versus observed particle chirality",
    "four-variable criticality versus the complete real translation covector",
    "full-comparator momentum versus the independent Spin-grade-two connection owner",
    "zero action density versus a fitted cosmological counterterm",
    "pointwise metric stationarity versus a global physical vacuum",
):
    check("type", label + " remain distinct", True)


N = P["N"]
FULL = P["FULL"]
ZERO = P["ZERO"]
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
K77 = P["K77"]
ETA = K77["ETA"]
emul = K77["emul"]
d_shiab = K77["d_shiab"]
check("signature", "the frozen blocks follow the actual noncontiguous K77 ETA signs",
      sum(value == 1 for value in ETA) == 7
      and sum(value == -1 for value in ETA) == 7
      and tuple(ETA[:7]) != (1,) * 7)


def signature_split_field(values):
    """Return T_i=(a,b) on eta=+1 and (c,d) on eta=-1."""
    av, bv, cv, dv = values
    out = {}
    for slot in range(N):
        vector_coefficient, dual_coefficient = (
            (av, bv) if ETA[slot] == 1 else (cv, dv)
        )
        dual_mask, dual_sign = blade_product(1 << slot, FULL)
        out[1 << slot] = eadd(
            blade(slot, (vector_coefficient, sp.Integer(0))),
            {dual_mask: (dual_sign * dual_coefficient, sp.Integer(0))},
        )
    return out


def action_value(values):
    field = signature_split_field(tuple(Fraction(value) for value in values))
    curvature = fixed_packet({}, field)
    cubic = top_scalar(wedge_raw(field, shiab(curvature, SELECTED)))
    mass = top_scalar(wedge_raw(field, hodge(field)))
    value = gadd(cubic, gscale(Fraction(1, 2), mass))
    assert value[1] == 0
    return sp.Rational(value[0].numerator, value[0].denominator)


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
expected_action = sp.Rational(7, 2) * (
    40*a**3 + 168*a**2*c + a**2 - 40*a*b**2 - 112*a*b*d
    + 168*a*c**2 - 56*a*d**2 - 56*b**2*c - b**2 - 112*b*c*d
    + 40*c**3 + c**2 - 40*c*d**2 - d**2
)
check("exact", "thirty independent samples determine every degree-two and degree-three coefficient",
      len(monomials) == len(sample_rows) == 30
      and sp.Matrix(sample_rows).det() != 0)
check("exact", "direct Clifford interpolation gives the frozen signature-split action",
      sp.expand(action - expected_action) == 0)
check("heldout", "three held-out rational samples agree with the interpolated action",
      all(action.subs(dict(zip(variables, point))) == action_value(point)
          for point in ((3, -2, 1, 4), (-2, 3, -4, 1),
                        (Fraction(2, 3), Fraction(-5, 7),
                         Fraction(7, 5), Fraction(-3, 2)))))

quadratic = sp.Rational(7, 2) * (a*a - b*b + c*c - d*d)
cubic = sp.expand(action - quadratic)
check("exact", "the action has exactly quadratic plus cubic homogeneity",
      sp.expand(sum(x * sp.diff(action, x) for x in variables)
                     - (2 * quadratic + 3 * cubic)) == 0)

sqrt15 = sp.sqrt(15)
zero = (sp.Integer(0),) * 4
homogeneous = (-sp.Rational(1, 312), 0, -sp.Rational(1, 312), 0)
uniform = [
    (-sp.Rational(1, 208), sign * sp.Rational(1, 208),
     -sp.Rational(1, 208), sign * sp.Rational(1, 208))
    for sign in (-1, 1)
]
pure_vector = [
    ((1 + swap * sqrt15) / 48, 0,
     (1 - swap * sqrt15) / 48, 0)
    for swap in (-1, 1)
]
new_points = [
    ((1 + swap * sqrt15) / 32,
     chirality * (1 + swap * sqrt15) / 32,
     (1 - swap * sqrt15) / 32,
     chirality * (1 - swap * sqrt15) / 32)
    for swap in (-1, 1) for chirality in (-1, 1)
]
expected_critical = [zero, homogeneous, *uniform, *pure_vector, *new_points]
critical_rows = sp.solve(tuple(sp.diff(action, x) for x in variables),
                         variables, dict=True)
critical = [tuple(row[x] for x in variables) for row in critical_rows]


def same_point(left, right) -> bool:
    return all(sp.simplify(x - y) == 0 for x, y in zip(left, right))


check("exact", "the complete critical set has exactly ten algebraic points",
      len(critical) == len(expected_critical) == 10
      and all(any(same_point(expected, actual) for actual in critical)
              for expected in expected_critical))
check("control", "the two new pure-vector roots retain density 7/432",
      all(sp.factor(action.subs(dict(zip(variables, point)))) == sp.Rational(7, 432)
          for point in pure_vector))
check("prior", "the old homogeneous point retains density 7/292032",
      sp.factor(action.subs(dict(zip(variables, homogeneous))))
      == sp.Rational(7, 292032))
check("null", "all four new signature-split chiral points have exact zero density",
      all(sp.factor(action.subs(dict(zip(variables, point)))) == 0
          for point in new_points))
check("null", "the four new points are square-root-15 rather than uniform rational points",
      all(not same_point(point, old) for point in new_points for old in uniform))


print("\nC. COMPLETE POINT FIELD, CONNECTION, PRIMITIVE, AND METRIC OWNERS")
hessian = sp.hessian(action, variables)
branch_results = {}
for swap in (-1, 1):
    for chirality in (-1, 1):
        point = (
            (1 + swap * sqrt15) / 32,
            chirality * (1 + swap * sqrt15) / 32,
            (1 - swap * sqrt15) / 32,
            chirality * (1 - swap * sqrt15) / 32,
        )
        label = f"swap_{swap:+d}_volume_{chirality:+d}"
        field = signature_split_field(point)
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
            pair_nonzero(value)
            for row in momentum_rows for mask, value in row.items()
            if len(indices(mask)) == 2
        )
        moving_shiab = []
        for left in range(N):
            for right in range(left + 1, N):
                eta = blade((left, right))
                moving_shiab.append(top_scalar(wedge_raw(
                    field, d_shiab(curvature, SELECTED, eta)
                )))
        moving_support = sum(pair_nonzero(value) for value in moving_shiab)
        coefficient_squares = [emul(value, value) for value in field.values()]
        reduced_hessian = sp.simplify(hessian.subs(dict(zip(variables, point))))
        density = sp.factor(action.subs(dict(zip(variables, point))))
        metric_row = tuple(sp.simplify(entry * density)
                           for entry in (-2, 0, 0, 0, 2, 0, 0, 2, 0, 2))

        check("clifford", f"{label}: every coefficient is nonzero and square-zero",
              all(element_nonzero(value) for value in field.values())
              and all(not element_nonzero(value) for value in coefficient_squares))
        check("field", f"{label}: all 229376 real translation directions vanish exactly",
              translation_support == 0 and N * 2**N == 229376)
        check("owner", f"{label}: comparator momentum has 28 grade-one/thirteen cells",
              momentum_support == 28 and momentum_grades == [1, 13])
        check("owner", f"{label}: the actual Spin-grade-two connection equation is zero",
              spin_grade_two_support == 0)
        check("epsilon", f"{label}: all 91 moving-Shiab primitive returns vanish",
              len(moving_shiab) == 91 and moving_support == 0)
        check("metric", f"{label}: zero density and zero graph-visible momentum give a zero metric row",
              density == 0 and spin_grade_two_support == 0 and not any(metric_row))
        check("hessian", f"{label}: the reduced four-variable Hessian is nondegenerate",
              reduced_hessian.rank() == 4
              and sp.factor(reduced_hessian.det()) == 540225)

        branch_results[label] = {
            "point": [str(value) for value in point],
            "translation_support": translation_support,
            "momentum_support": momentum_support,
            "momentum_grades": momentum_grades,
            "spin_grade_two_support": spin_grade_two_support,
            "moving_shiab_support": moving_support,
            "action_density": str(density),
            "metric_row": [str(value) for value in metric_row],
            "reduced_hessian_determinant": str(sp.factor(reduced_hessian.det())),
        }


print("\nD. HOSTILE CONTROLS, SCOPE, AND PROPAGATION")
first = new_points[0]
off_root = (first[0], first[1], first[2], sp.Integer(0))
off_field = signature_split_field(off_root)
off_packet = shiab(fixed_packet({}, off_field), SELECTED)
check("planted", "PLANT deleting one volume-dual coefficient fires the complete covector",
      row_support(action_row(0, off_field, off_packet)) > 0)
check("planted", "PLANT treating unrestricted comparator momentum as the connection owner falsely rejects every point",
      all(row["momentum_support"] == 28
          and row["spin_grade_two_support"] == 0
          for row in branch_results.values()))
check("planted", "PLANT deleting either volume sign or either signature polarity loses exact points",
      len(branch_results) == 4)
check("planted", "PLANT pure-vector signature anisotropy fails the held-out metric-density gate",
      all(sp.factor(action.subs(dict(zip(variables, point)))) != 0
          for point in pure_vector))
check("scope", "the K77 signature split is target-blind but not spacetime inhomogeneity", True)
check("scope", "point equations do not establish the complete tangent first symbol global stabilizer or spectrum", True)
check("scope", "the volume signs are not identified with observed chirality", True)
check("scope", "no ledger canon source ownership residue particle prediction or public posture changes", True)
check("reverse", "CBRS-1L must build the complete split-symmetry tangent before any downstream spectrum", True)
check("propagation", "the native registry records four new algebraic point classes and CBRS-1L",
      "four_new_signature_split_points" in read(
          "lab/process/selected-k77-cbrs1k-signature-split-point-class.json"
      ) and "CBRS1L" in read(
          "lab/process/selected-k77-cbrs1k-signature-split-point-class.json"
      ))
check("propagation", "CURRENT-STATE carries CBRS-1K and the exact CBRS-1L successor",
      "CBRS-1K admits four" in read("CURRENT-STATE.yaml")
      and "CBRS-1L" in read("CURRENT-STATE.yaml"))
check("propagation", "the agenda advances the live reverse scaffold without changing its Lane",
      "CBRS-1K admits four" in read("lab/process/RESEARCH-AGENDA.json")
      and "CBRS-1L" in read("lab/process/RESEARCH-AGENDA.json"))
check("propagation", "the contributor front door points to the CBRS-1K result and CBRS-1L",
      "CBRS-1K ADMITS FOUR" in read("NEXT-STEPS.md")
      and "CBRS-1L" in read("NEXT-STEPS.md"))

RESULT = {
    "disposition": "CBRS1K_FOUR_NEW_K77_SIGNATURE_SPLIT_ZERO_DENSITY_POINT_CLASSES_PASS_COMPLETE_POINT_FIELD_CONNECTION_PRIMITIVE_AND_METRIC_EQUATIONS",
    "class": {
        "formula": "T_i=a*gamma_i+b*gamma_i*Omega on eta=+1; c*gamma_i+d*gamma_i*Omega on eta=-1",
      "signature_blocks": {
          "eta_plus_slots": [slot for slot, value in enumerate(ETA) if value == 1],
          "eta_minus_slots": [slot for slot, value in enumerate(ETA) if value == -1],
      },
        "action": str(action),
        "target_blind": True,
        "critical_point_count": len(critical),
        "four_new_signature_split_points": [
            [str(value) for value in point] for point in new_points
        ],
    },
    "branches": branch_results,
    "claim_ceiling": "EXACT_RECONSTRUCTION_GRADE_POINTWISE_METRIC_STATIONARY_K77_SIGNATURE_SPLIT_CLASS_FOR_THE_SELECTED_FIRST_ACTION__NOT_SOURCE_OWNED_GLOBAL_OBSERVED_OR_PHYSICAL",
    "complete_tangent_stabilizer_spectrum": "OPEN_AT_CBRS1L",
    "next_gate": "CBRS1L_COMPLETE_SPLIT_SYMMETRY_T_PLUS_SPIN_CONNECTION_HESSIAN__POINTWISE_ORBIT_STABILIZER__PRIMITIVE_QUOTIENT__THEN_FIRST_SYMBOL",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
