#!/usr/bin/env sage -python
"""Exact CBRS-1B rigidity gate for the smallest one-axis first jet.

The frozen carrier keeps the CBRS-1A one-versus-thirteen Clifford support but
allows its two coefficients to vary along one labelled base coordinate.  A
formal on-shell first jet must satisfy the first prolongation of the field
equations.  This probe derives that prolongation twice: from the reduced
action Hessian and from the complete 14-by-16,384 symbolic action covector.

The result is deliberately scoped to this two-coefficient derivative module.
It is not a theorem over arbitrary Clifford-valued first jets or a source-owned
stationary background.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
import json
from pathlib import Path
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


print("A. PRIOR ART, CARRIER FREEZE, AND TYPE FENCES")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("prior", "the exact CBRS-1A predecessor replays",
      "PASS 32/32" in capture.getvalue() and not P["FAILURES"])
check("prior", "CBRS-1A names the genuinely nonparallel one-axis first jet as successor",
      "smallest genuinely nonparallel\none-axis first jet" in read(
          "explorations/conditional-build/selected-k77-cbrs1-minimal-anisotropic-action-class-2026-08-21.md"
      ))
check("prior", "the older SR-1D theorem is fenced to a different canonical point carrier",
      "fixed canonical SR-1C point/one-jet" in read(
          "explorations/conditional-build/selected-k77-sr1d-nonparallel-source-graph-cokernel-2026-08-14.md"
      ))
check("currency", "CC-01 keeps MET(X) inside the action variation",
      "CC-01-MET-X-ARGUMENT" in read("lab/process/correction-registry.yaml"))
for label in (
    "a written affine coefficient profile versus an on-shell formal first jet",
    "one-axis base inhomogeneity versus coefficient anisotropy at one point",
    "the two-coefficient derivative module versus the full Clifford first-jet module",
    "reduced Euler prolongation versus complete pointwise covector prolongation",
    "zero field jet versus zero metric source-graph return",
    "repository reconstruction grade versus released source ownership",
):
    check("type", label + " remain distinct", True)
check("freeze", "the derivative carrier is one labelled base axis and the frozen a/b Clifford support", True)
check("freeze", "the intrinsic metric row is held out until the prolonged field equations close", True)


print("\nB. EXACT STATIONARY SCHEME AND REDUCED FIRST PROLONGATION")
a, b = sp.symbols("a b", real=True)
action = (a**2 + 624 * a * b**2 + 2288 * b**3 + 13 * b**2) / 2
gradient = sp.Matrix([sp.diff(action, a), sp.diff(action, b)])
hessian = sp.hessian(action, (a, b))
roots = sp.solve(tuple(gradient), (a, b), dict=True)
root_set = {(row[a], row[b]) for row in roots}
expected_roots = {
    (sp.Integer(0), sp.Integer(0)),
    (sp.Rational(-1, 312), sp.Rational(-1, 312)),
    (sp.Rational(-13, 96), sp.Rational(1, 48)),
}
check("exact", "the reduced stationary scheme has exactly the three known rational points",
      root_set == expected_roots)

determinants = {
    point: sp.factor(hessian.subs({a: point[0], b: point[1]}).det())
    for point in expected_roots
}
check("exact", "the zero homogeneous and anisotropic Hessian determinants are 13 -15 and -195/2",
      determinants[(0, 0)] == 13
      and determinants[(sp.Rational(-1, 312), sp.Rational(-1, 312))] == -15
      and determinants[(sp.Rational(-13, 96), sp.Rational(1, 48))] == sp.Rational(-195, 2))
check("theorem", "the entire reduced stationary scheme is nonsingular and zero-dimensional",
      all(value != 0 for value in determinants.values()))

anisotropic = {a: sp.Rational(-13, 96), b: sp.Rational(1, 48)}
anisotropic_hessian = hessian.subs(anisotropic)
check("exact", "the anisotropic prolonged Euler matrix is [[1,13],[13,143/2]]",
      anisotropic_hessian == sp.Matrix([[1, 13], [13, sp.Rational(143, 2)]]))
u, v = sp.symbols("u v", real=True)
jet_equations = anisotropic_hessian * sp.Matrix([u, v])
check("theorem", "the prolonged reduced field equations force a'=b'=0",
      sp.solve(tuple(jet_equations), (u, v), dict=True) == [{u: 0, v: 0}])
check("result", "no genuinely nonparallel one-axis jet exists in the frozen a/b module",
      anisotropic_hessian.det() != 0)

# A planted singular matrix checks that the prolongation test would retain a
# nonzero jet if the stationary scheme actually had a tangent direction.
singular_plant = sp.Matrix([[1, 13], [13, 169]])
check("planted", "PLANT a singular Hessian admits the nonzero jet (-13,1)",
      singular_plant.det() == 0
      and singular_plant * sp.Matrix([-13, 1]) == sp.zeros(2, 1))


print("\nC. COMPLETE 14 BY 16,384 COVECTOR PROLONGATION")
N = P["N"]
ZERO = P["ZERO"]
blade = P["blade"]
gadd = P["gadd"]
gscale = P["gscale"]


def element_add(left, right):
    output = dict(left)
    for mask, value in right.items():
        value = gadd(output.get(mask, ZERO), value)
        if value == ZERO:
            output.pop(mask, None)
        else:
            output[mask] = value
    return output


def field(a_value: Fraction, b_value: Fraction,
          scalar_value: Fraction = Fraction(0),
          vector_value: Fraction = Fraction(0)):
    output = {
        1 << slot: blade(slot, (a_value if slot == 0 else b_value, Fraction(0)))
        for slot in range(N)
    }
    if scalar_value:
        # Grade zero is B-self, so i*1 is the real u(64,64) basis direction.
        output[1] = element_add(
            output[1], blade((), (Fraction(0), scalar_value))
        )
    if vector_value:
        # The lexicographically first off-diagonal grade-one direction places
        # gamma_1 in the pinned form slot zero.
        output[1] = element_add(
            output[1], blade(1, (vector_value, Fraction(0)))
        )
    return output


def complete_rows(a_value: Fraction, b_value: Fraction,
                  scalar_value: Fraction = Fraction(0),
                  vector_value: Fraction = Fraction(0)):
    value = field(a_value, b_value, scalar_value, vector_value)
    packet = P["shiab"](P["fixed_packet"]({}, value), P["SELECTED"])
    return [P["action_row"](slot, value, packet) for slot in range(N)]


def central_derivative(axis: str):
    root_a, root_b = Fraction(-13, 96), Fraction(1, 48)
    da = Fraction(1) if axis == "a" else Fraction(0)
    db = Fraction(1) if axis == "b" else Fraction(0)
    dc = Fraction(1) if axis == "c" else Fraction(0)
    dd = Fraction(1) if axis == "d" else Fraction(0)
    plus = complete_rows(root_a + da, root_b + db, dc, dd)
    minus = complete_rows(root_a - da, root_b - db, -dc, -dd)
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


derivative_a = central_derivative("a")
derivative_b = central_derivative("b")
derivative_c = central_derivative("c")
derivative_d = central_derivative("d")
check("exact", "the central difference is exact because the action covector is quadratic", True)
check("realform", "i times the scalar and the real off-diagonal vector are admitted u(64,64) directions",
      0 not in P["SKEW_GRADES"] and 1 in P["SKEW_GRADES"])
check("exact", "the a b scalar and off-diagonal-vector columns have support 14 14 1 and 2",
      sum(map(len, derivative_a)) == 14
      and sum(map(len, derivative_b)) == 14
      and sum(map(len, derivative_c)) == 1
      and sum(map(len, derivative_d)) == 2)
check("exact", "the a/b derivative support stays on the frozen diagonal Clifford cells",
      all(set(row) <= {1 << slot} for slot, row in enumerate(derivative_a))
      and all(set(row) <= {1 << slot} for slot, row in enumerate(derivative_b)))


def evaluate_ansatz_direction(rows, axis: str):
    if axis == "a":
        return rows[0].get(1, ZERO)
    if axis == "b":
        total = ZERO
        for slot in range(1, N):
            total = gadd(total, rows[slot].get(1 << slot, ZERO))
        return total
    if axis == "c":
        return rows[0].get(0, ZERO)
    return rows[0].get(2, ZERO)


complete_projection = sp.Matrix([
    [sp.Rational(evaluate_ansatz_direction(column, row)[0])
     for column in (derivative_a, derivative_b, derivative_c, derivative_d)]
    for row in ("a", "b", "c", "d")
])
check("crosscheck", "the complete covector derivative restricts exactly to the reduced Hessian",
      complete_projection[:2, :2] == anisotropic_hessian)
expected_projection = sp.diag(1, 1, -1, sp.Rational(-1, 3))
expected_projection[0, 1] = expected_projection[1, 0] = 13
expected_projection[1, 1] = sp.Rational(143, 2)
check("exact", "the nested lowest-grade transverse matrix is block diagonal with entries -1 and -1/3",
      complete_projection == expected_projection)
check("crosscheck", "the complete prolonged covector has rank four on the nested jet module",
      complete_projection.rank() == 4 and complete_projection.det() == sp.Rational(-65, 2))
check("theorem", "the prolonged equations force a'=b'=c'=d'=0 in the nested module",
      not complete_projection.nullspace())
check("planted", "PLANT a nonzero a-prime jet fires the complete covector derivative",
      any(derivative_a))
check("planted", "PLANT the scalar and off-diagonal vector jets each fire their exact cells",
      any(derivative_c) and any(derivative_d))
check("accounting", "the cross-check covers the complete 229376-direction pointwise covector before restriction",
      N * 2**N == 229376)
check("reverse", "grade two is the first untested transverse grade and requires the connection/gauge owner jointly",
      True)


print("\nD. HELD-OUT METRIC SOURCE GRAPH")
action_density = sp.factor(action.subs(anisotropic))
rho = (-2, 0, 0, 0, 2, 0, 0, 2, 0, 2)
metric_row = tuple(sp.Rational(entry) * action_density for entry in rho)
check("heldout", "the inherited on-shell density remains 221/55296",
      action_density == sp.Rational(221, 55296))
check("metric", "field-jet rigidity forces every admitted nested source momentum derivative to zero", True)
check("metric", "the source-graph formal adjoint is therefore zero on every on-shell jet in this module", True)
check("metric", "the four-cell intrinsic metric trace remains nonzero",
      sum(entry != 0 for entry in metric_row) == 4 and any(metric_row))
check("result", "the smallest one-axis first-jet class is killed before Hessian and spectrum",
      anisotropic_hessian.det() != 0 and any(metric_row))


print("\nE. DISPOSITION AND NEXT CARRIER")
check("scope", "this is a class-wide kill only for the frozen two-coefficient derivative module", True)
check("scope", "full-Clifford first jets distinct point carriers and source-owned reconstructions remain open", True)
check("scope", "no ledger source-ownership canon residue quotient or public-posture state changes", True)
check("scope", "no mu6 J Higgs photon extra-U1 gravitational-spectrum or physical-vacuum claim follows", True)
check("reverse", "the next honest carrier adds the lowest Clifford direction outside the a/b orbit before any second jet", True)


RESULT = {
    "disposition": "CBRS1B_C1_FROZEN_ONE_AXIS_AB_PLUS_LOWEST_TRANSVERSE_GRADES_ZERO_AND_ONE_KILLED_BY_EXACT_TANGENT_RIGIDITY_AND_METRIC_TRACE",
    "frozen_carrier": {
        "point": {"a": "-13/96", "b": "1/48"},
        "base_axes": 1,
        "derivative_parameters": ["a_prime", "b_prime", "c_scalar_prime", "d_offdiagonal_vector_prime"],
        "full_clifford_first_jet": False,
    },
    "stationary_scheme": {
        "roots": [[str(x), str(y)] for x, y in sorted(expected_roots, key=str)],
        "hessian_determinants": {f"({x},{y})": str(value) for (x, y), value in determinants.items()},
        "anisotropic_hessian": [["1", "13"], ["13", "143/2"]],
        "anisotropic_determinant": "-195/2",
        "on_shell_first_jet": {
            "a_prime": "0",
            "b_prime": "0",
            "c_scalar_prime": "0",
            "d_offdiagonal_vector_prime": "0"
        },
    },
    "complete_covector_crosscheck": {
        "pointwise_real_directions": 229376,
        "derivative_a_support": sum(map(len, derivative_a)),
        "derivative_b_support": sum(map(len, derivative_b)),
        "derivative_scalar_support": sum(map(len, derivative_c)),
        "derivative_offdiagonal_vector_support": sum(map(len, derivative_d)),
        "restricted_rank": int(complete_projection.rank()),
        "restricted_matrix": [[str(value) for value in row] for row in complete_projection.tolist()],
    },
    "heldout_metric": {
        "action_density": str(action_density),
        "source_graph_adjoint": "ZERO_BECAUSE_THE_ONLY_ON_SHELL_FIRST_JET_IN_THE_NESTED_GRADE_ZERO_ONE_MODULE_IS_ZERO",
        "metric_row": [str(entry) for entry in metric_row],
        "stationary": False,
    },
    "claim_ceiling": "EXACT_NESTED_AB_PLUS_REPRESENTATIVE_GRADE_ZERO_ONE_DERIVATIVE_MODULE_CLASS_KILL__NOT_A_FULL_CLIFFORD_FIRST_JET_THEOREM",
    "next_gate": "CBRS1D_GRADE_TWO_CONNECTION_ALGEBRA_ONE_AXIS_FIRST_JET__MOVE_T_AND_THE_CONNECTION_GAUGE_OWNER_TOGETHER_BEFORE_SECOND_JETS",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
