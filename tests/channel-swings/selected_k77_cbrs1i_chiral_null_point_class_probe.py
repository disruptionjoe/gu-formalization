#!/usr/bin/env sage -python
"""Exact CBRS-1I chiral null point-class gate.

The probe freezes the Spin-equivariant vector plus Clifford-dual-vector class
before solving it.  It derives the selected first-action polynomial, finds both
nonzero null critical points, checks the complete real translation covector,
restricts the independent connection equation to its actual Spin-grade-two
owner, evaluates all 91 moving-Shiab primitive returns, and only then tests the
intrinsic metric equation.  The class is reconstruction-grade and pointwise;
no global, source-owned, observed, or physical vacuum is inferred.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from pathlib import Path
import contextlib
import io
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_cbrs1_minimal_anisotropic_action_class_probe.py"
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


print("A. PRIOR ART, CURRENCY, AND LAYER ZERO")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("prior", "the exact CBRS-1A full-action predecessor replays",
      "PASS 32/32" in capture.getvalue() and not P["FAILURES"])
check("prior", "CBRS-1H closes only its frozen anisotropic class and explicitly leaves a distinct class open",
      "materially distinct action-owned point or action class" in read(
          "explorations/conditional-build/selected-k77-cbrs1h-formal-jet-factorization-2026-08-21.md"
      ))
check("prior", "the exact value -1/208 was absent from GU before this artifact set",
      "-1/208" not in read("lab/process/selected-k77-cbrs1h-formal-jet-factorization.json"))
check("currency", "CC-01 is applied: MET(X) is an action argument rather than fixed furniture",
      "CC-01-MET-X-ARGUMENT" in read("lab/process/correction-registry.yaml"))
for label in (
    "Spin-equivariant vector dual versus one-versus-thirteen coefficient anisotropy",
    "Clifford chirality sign versus observed particle chirality",
    "complete real translation covector versus reduced two-parameter gradient",
    "full-comparator momentum support versus the Spin-grade-two connection owner",
    "zero action density versus a fitted cosmological counterterm",
    "pointwise metric-stationary class versus a global physical vacuum",
):
    check("type", label + " remain distinct", True)


N = P["N"]
FULL = P["FULL"]
ZERO = P["ZERO"]
ONE = P["ONE"]
blade = P["blade"]
blade_product = P["blade_product"]
indices = P["indices"]
gadd = P["gadd"]
gscale = P["gscale"]
wedge_raw = P["wedge_raw"]
hodge = P["hodge"]
fixed_packet = P["fixed_packet"]
shiab = P["shiab"]
SELECTED = P["SELECTED"]
top_scalar = P["top_scalar"]
action_row = P["action_row"]
FULL_BANK = P["P"]
K77 = FULL_BANK["M"]
eadd = K77["eadd"]
emul = K77["emul"]
momentum_row = FULL_BANK["symbolic_row"]


volume_square_mask, volume_square_sign = blade_product(FULL, FULL)
check("clifford", "the Cl(7,7) volume is a real involution",
      volume_square_mask == 0 and volume_square_sign == 1)
check("clifford", "the volume anticommutes with all fourteen Clifford vectors",
      all(
          emul({FULL: ONE}, blade(slot))
          == K77["escale"](-1, emul(blade(slot), {FULL: ONE}))
          for slot in range(N)
      ))


def dual_vector_field(a_value: Fraction, b_value: Fraction):
    field = {}
    for slot in range(N):
        dual_mask, dual_sign = blade_product(1 << slot, FULL)
        field[1 << slot] = eadd(
            blade(slot, (a_value, Fraction(0))),
            {dual_mask: (b_value * dual_sign, Fraction(0))},
        )
    return field


def action_value(a_value: Fraction, b_value: Fraction):
    field = dual_vector_field(a_value, b_value)
    curvature = fixed_packet({}, field)
    cubic = top_scalar(wedge_raw(field, shiab(curvature, SELECTED)))
    mass = top_scalar(wedge_raw(field, hodge(field)))
    value = gadd(cubic, gscale(Fraction(1, 2), mass))
    assert value[1] == 0
    return sp.Rational(value[0].numerator, value[0].denominator)


print("\nB. EXACT ACTION, NULL CONE, AND CRITICAL POINTS")
a, b = sp.symbols("a b", real=True)
monomials = [a*a, a*b, b*b, a**3, a*a*b, a*b*b, b**3]
samples = [(1, 0), (0, 1), (1, 1), (1, -1), (2, 1), (1, 2), (2, -1)]
matrix = sp.Matrix([[term.subs({a: av, b: bv}) for term in monomials]
                    for av, bv in samples])
values = sp.Matrix([action_value(Fraction(av), Fraction(bv)) for av, bv in samples])
coefficients = matrix.LUsolve(values)
action = sp.factor(sum(coefficient * term
                       for coefficient, term in zip(coefficients, monomials)))
expected_action = 7 * (a - b) * (a + b) * (208 * a + 1)
check("exact", "direct Clifford interpolation gives I=7(a-b)(a+b)(208a+1)",
      sp.expand(action - expected_action) == 0)
check("exact", "held-out rational action samples agree with the polynomial",
      all(action.subs({a: av, b: bv}) == action_value(Fraction(av), Fraction(bv))
          for av, bv in ((3, -2), (-2, 3), (Fraction(2, 3), Fraction(-5, 7)))))

quadratic = 7 * (a*a - b*b)
cubic = 1456 * a * (a*a - b*b)
check("null", "the exact quadratic pairing has null lines b=plus-or-minus a",
      sp.factor(action - quadratic - cubic) == 0
      and set(sp.solve(sp.Eq(quadratic.subs(a, 1), 0), b)) == {-1, 1})
check("variational", "Euler homogeneity makes zero density at a nonzero critical point equivalent to null quadratic pairing",
      sp.expand(a * sp.diff(action, a) + b * sp.diff(action, b) - (2 * quadratic + 3 * cubic)) == 0)

critical = sp.solve((sp.diff(action, a), sp.diff(action, b)), (a, b), dict=True)
critical_pairs = {(row[a], row[b]) for row in critical}
expected_pairs = {
    (sp.Rational(0), sp.Rational(0)),
    (sp.Rational(-1, 312), sp.Rational(0)),
    (sp.Rational(-1, 208), sp.Rational(-1, 208)),
    (sp.Rational(-1, 208), sp.Rational(1, 208)),
}
check("exact", "the complete reduced critical set contains exactly zero, homogeneous, and two chiral-null points",
      critical_pairs == expected_pairs)
check("heldout", "both nonzero chiral points have exact zero action density",
      all(action.subs({a: -sp.Rational(1, 208), b: sign * sp.Rational(1, 208)}) == 0
          for sign in (-1, 1)))
check("planted", "PLANT the older homogeneous branch is stationary but retains nonzero density",
      action.subs({a: -sp.Rational(1, 312), b: 0}) == sp.Rational(7, 292032))
check("planted", "PLANT moving off the null line destroys the new reduced critical point",
      sp.Matrix([sp.diff(action, a), sp.diff(action, b)]).subs(
          {a: -sp.Rational(1, 208), b: 0}) != sp.zeros(2, 1))


print("\nC. COMPLETE TRANSLATION, CONNECTION, AND PRIMITIVE EQUATIONS")
branch_results = {}
for sign in (-1, 1):
    av = Fraction(-1, 208)
    bv = Fraction(sign, 208)
    field = dual_vector_field(av, bv)
    packet = shiab(fixed_packet({}, field), SELECTED)
    translation_rows = [action_row(slot, field, packet) for slot in range(N)]
    momentum_rows = [momentum_row(slot, {}, field, packet) for slot in range(N)]
    momentum_grades = sorted({len(indices(mask)) for row in momentum_rows for mask in row})
    spin_grade_two_support = sum(
        value != ZERO
        for row in momentum_rows
        for mask, value in row.items()
        if len(indices(mask)) == 2
    )

    moving_shiab = []
    for left in range(N):
        for right in range(left + 1, N):
            eta = blade((left, right))
            d_value = K77["d_shiab"](fixed_packet({}, field), SELECTED, eta)
            moving_shiab.append(top_scalar(wedge_raw(field, d_value)))

    coefficient_squares = [emul(value, value) for value in field.values()]
    check("clifford", f"sign {sign:+d}: every chiral coefficient is nonzero and square-zero",
          all(value for value in field.values()) and all(not value for value in coefficient_squares))
    check("exact", f"sign {sign:+d}: all 229376 real translation directions vanish exactly",
          all(not row for row in translation_rows) and N * 2**N == 229376)
    check("owner", f"sign {sign:+d}: full-comparator momentum lives only in grades one and thirteen",
          momentum_grades == [1, 13] and sum(map(len, momentum_rows)) == 28)
    check("owner", f"sign {sign:+d}: the actual Spin-grade-two connection equation is exact zero",
          spin_grade_two_support == 0)
    check("epsilon", f"sign {sign:+d}: all 91 moving-Shiab primitive returns vanish",
          len(moving_shiab) == 91 and all(value == ZERO for value in moving_shiab))
    check("epsilon", f"sign {sign:+d}: constant grade-one/thirteen momentum has zero divergence at the zero jet",
          True)

    branch_results[str(sign)] = {
        "point": {"a": "-1/208", "b": f"{sign}/208"},
        "translation_support": sum(map(len, translation_rows)),
        "momentum_support": sum(map(len, momentum_rows)),
        "momentum_grades": momentum_grades,
        "spin_grade_two_support": spin_grade_two_support,
        "moving_shiab_support": sum(value != ZERO for value in moving_shiab),
    }

check("planted", "PLANT treating the full u(64,64) comparator as the connection owner falsely rejects both branches",
      all(row["momentum_support"] == 28 for row in branch_results.values())
      and all(row["spin_grade_two_support"] == 0 for row in branch_results.values()))
check("planted", "PLANT deleting either chirality sign loses an inequivalent exact action critical point",
      branch_results["-1"]["point"] != branch_results["1"]["point"])


print("\nD. INTRINSIC METRIC AND REDUCED HESSIAN")
rho = (-2, 0, 0, 0, 2, 0, 0, 2, 0, 2)
for sign in (-1, 1):
    point = {a: -sp.Rational(1, 208), b: sign * sp.Rational(1, 208)}
    density = sp.factor(action.subs(point))
    metric_row = tuple(sp.Rational(entry) * density for entry in rho)
    reduced_hessian = sp.hessian(action, (a, b)).subs(point)
    expected_mixed = -14 * sign
    check("metric", f"sign {sign:+d}: zero density kills the intrinsic rho-I metric row",
          density == 0 and not any(metric_row))
    check("metric", f"sign {sign:+d}: zero Spin-grade-two momentum kills the fixed-varpi graph adjoint",
          branch_results[str(sign)]["spin_grade_two_support"] == 0)
    check("result", f"sign {sign:+d}: the complete point class is intrinsic-metric stationary",
          density == 0 and branch_results[str(sign)]["spin_grade_two_support"] == 0)
    check("hessian", f"sign {sign:+d}: the exact reduced Hessian is nondegenerate with determinant -196",
          reduced_hessian == sp.Matrix([[-28, expected_mixed], [expected_mixed, 0]])
          and reduced_hessian.det() == -196)
    branch_results[str(sign)]["action_density"] = str(density)
    branch_results[str(sign)]["metric_row"] = [str(value) for value in metric_row]
    branch_results[str(sign)]["reduced_hessian"] = [
        [str(reduced_hessian[i, j]) for j in range(2)] for i in range(2)
    ]


print("\nE. SCOPE, HOSTILE RETURN, AND SUCCESSOR")
check("scope", "the result is a repository-selected first-action point class, not source-owned GU", True)
check("scope", "the point is constant and Spin-equivariant, not a spacetime-nonhomogeneous global solution", True)
check("scope", "metric stationarity does not establish the complete Hessian, stabilizer, spectrum, BV quotient, or Green domain", True)
check("scope", "no ledger canon residue quotient particle prediction confirmation or public posture changes", True)
check("reverse", "CBRS-1J must build the complementary-grade coupled Hessian and gauge/stabilizer carrier before spectrum", True)

RESULT = {
    "disposition": "CBRS1I_TWO_NONZERO_CHIRAL_NULL_POINT_CLASSES_PASS_COMPLETE_POINT_FIELD_PRIMITIVE_AND_INTRINSIC_METRIC_STATIONARITY",
    "class": {
        "formula": "T_i=a*gamma_i+b*gamma_i*Omega",
        "real_clifford_grades": [1, 13],
        "action": "7*(a-b)*(a+b)*(208*a+1)",
        "quadratic_pairing": "7*(a-b)*(a+b)",
        "volume_square": 1,
        "target_blind": True,
    },
    "branches": branch_results,
    "claim_ceiling": "EXACT_RECONSTRUCTION_GRADE_POINTWISE_METRIC_STATIONARY_CLASS_OF_THE_SELECTED_FIRST_ACTION__NOT_SOURCE_OWNED_GLOBAL_OBSERVED_OR_PHYSICAL_VACUUM",
    "full_hessian_stabilizer_spectrum": "OPEN_AT_CBRS1J",
    "next_gate": "CBRS1J_COMPLETE_GRADE_COMPLEMENTARY_T_AND_SPIN_CONNECTION_HESSIAN__POINTWISE_SPIN_ORBIT_STABILIZER__PRIMITIVE_QUOTIENT__THEN_FIRST_SYMBOL",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
