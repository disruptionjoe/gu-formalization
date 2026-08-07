#!/usr/bin/env python3
"""Exact ECW3A observation-dual and leakage gate.

This finite rational model separates the field lift/retract, algebraic equation
dual, and pairing-dependent Krein adjoint.  It then constructs two ambient
operators with the same induced four-dimensional equation: one preserves the
lifted image and one has a nonzero kernel-valued leakage term.  The same
separation is checked for a nonlinear Euler-shaped map.

The model freezes the logical gate required by Wave 3.  It is not a global
Y^14 observation section, a closed domain, or a physical equation.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/eric-curt-wave3a-observation-dual-leakage.json"
CAMPAIGN = ROOT / "lab/process/eric-curt-ten-wave-campaign.json"


def matrix(rows):
    return tuple(tuple(F(entry) for entry in row) for row in rows)


def identity(size):
    return matrix([[int(i == j) for j in range(size)] for i in range(size)])


def transpose(value):
    return tuple(tuple(value[i][j] for i in range(len(value))) for j in range(len(value[0])))


def multiply(left, right):
    assert len(left[0]) == len(right)
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(len(right))), F(0))
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def add(left, right):
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(len(left[0])))
        for i in range(len(left))
    )


def subtract(left, right):
    return tuple(
        tuple(left[i][j] - right[i][j] for j in range(len(left[0])))
        for i in range(len(left))
    )


def scale(factor, value):
    factor = F(factor)
    return tuple(tuple(factor * entry for entry in row) for row in value)


def matvec(value, vector):
    assert len(value[0]) == len(vector)
    return tuple(sum((row[j] * vector[j] for j in range(len(vector))), F(0)) for row in value)


def vec_add(left, right):
    return tuple(x + y for x, y in zip(left, right, strict=True))


def vec_sub(left, right):
    return tuple(x - y for x, y in zip(left, right, strict=True))


def dot(left, right):
    return sum((x * y for x, y in zip(left, right, strict=True)), F(0))


def bilinear(left, metric, right):
    return dot(left, matvec(metric, right))


def is_zero_matrix(value):
    return all(entry == 0 for row in value for entry in row)


def is_zero_vector(value):
    return all(entry == 0 for entry in value)


def quadratic_x(vector):
    x0, x1, x2, x3 = vector
    return (x0 * x1, x1 * x1, x2 * x3, x0 * x0 - x3 * x3)


def leakage_quadratic(vector):
    x0, x1, x2, x3 = vector
    return (x0 * x0, x1 * x2, x2 * x2, x3 * x0)


exact_checks = 0
planted_checks = 0


def exact(name, condition):
    global exact_checks
    if not condition:
        raise AssertionError(f"exact check failed: {name}")
    exact_checks += 1


def planted(name, false_claim):
    global planted_checks
    if false_claim:
        raise AssertionError(f"planted false claim unexpectedly passed: {name}")
    planted_checks += 1


def main():
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    campaign = json.loads(CAMPAIGN.read_text(encoding="utf-8"))

    # L: X^4 -> Y^14 is a declared tubular lift.  R is a non-orthogonal left
    # inverse, chosen to make the type distinction from L^vee and L^! visible.
    lift = matrix([[int(i == j) for j in range(4)] for i in range(14)])
    normal_mix = matrix(
        [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        ]
    )
    retract = matrix(
        [
            [int(i == j) for j in range(4)] + list(normal_mix[i])
            for i in range(4)
        ]
    )
    equation_dual = transpose(lift)
    projector = multiply(lift, retract)
    off_projector = subtract(identity(14), projector)

    # Native-signature finite pairing: the first four lifted directions have
    # Lorentz (3,1), while Y carries (9,5).
    metric_y = matrix(
        [[(1 if i < 3 or 4 <= i < 10 else -1) if i == j else 0 for j in range(14)] for i in range(14)]
    )
    metric_x = multiply(multiply(transpose(lift), metric_y), lift)
    metric_x_inverse = metric_x  # diagonal entries are +/-1
    riesz_adjoint = multiply(multiply(metric_x_inverse, equation_dual), metric_y)

    exact("ambient pairing has signature (9,5)", sum(metric_y[i][i] > 0 for i in range(14)) == 9 and sum(metric_y[i][i] < 0 for i in range(14)) == 5)
    exact("induced observed pairing has signature (3,1)", sum(metric_x[i][i] > 0 for i in range(4)) == 3 and sum(metric_x[i][i] < 0 for i in range(4)) == 1)
    exact("field retract is a left inverse", multiply(retract, lift) == identity(4))
    exact("lift-retract projector is idempotent", multiply(projector, projector) == projector)
    exact("projector fixes the lifted image", multiply(projector, lift) == lift)
    exact("off-image projector kills the lift", is_zero_matrix(multiply(off_projector, lift)))
    exact("equation dual has X-covector by Y-covector shape", len(equation_dual) == 4 and len(equation_dual[0]) == 14)
    exact("Krein-Riesz adjoint is a left inverse for the metric lift", multiply(riesz_adjoint, lift) == identity(4))
    exact("chosen field retract is not the algebraic equation dual", retract != equation_dual)
    exact("chosen field retract is not the Krein-Riesz adjoint", retract != riesz_adjoint)

    x = tuple(F(entry) for entry in (2, -1, 3, 4))
    y = tuple(F(entry) for entry in (1, 2, -1, 3, 1, -2, 1, 0, 2, -1, 3, 1, -2, 4))
    alpha_y = tuple(F(entry) for entry in (3, 1, -2, 4, 1, 0, -1, 2, 0, 1, -3, 2, 1, -1))
    exact("algebraic dual satisfies covector pairing", dot(alpha_y, matvec(lift, x)) == dot(matvec(equation_dual, alpha_y), x))
    exact("Krein adjoint satisfies indefinite pairing", bilinear(matvec(lift, x), metric_y, y) == bilinear(x, metric_x, matvec(riesz_adjoint, y)))

    # N spans four explicit kernel directions of R.  It is the allowed hidden
    # leakage channel: observation cannot see it, but image preservation can.
    kernel_lift_rows = []
    for row in range(14):
        if row < 4:
            kernel_lift_rows.append([-normal_mix[row][column] for column in range(4)])
        else:
            kernel_lift_rows.append([int(row == 4 + column) for column in range(4)])
    kernel_lift = matrix(kernel_lift_rows)
    exact("kernel lift is invisible to R", is_zero_matrix(multiply(retract, kernel_lift)))
    exact("kernel lift is wholly off image", multiply(off_projector, kernel_lift) == kernel_lift)
    exact("kernel witness is nonzero", not is_zero_matrix(kernel_lift))

    operator_x = matrix(
        [
            [2, 1, 0, 0],
            [0, -1, 1, 0],
            [1, 0, 1, 1],
            [0, 0, 1, 3],
        ]
    )
    kernel_weight = matrix([[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]])
    preserving_operator = add(multiply(multiply(lift, operator_x), retract), scale(2, off_projector))
    leaking_operator = add(preserving_operator, multiply(multiply(kernel_lift, kernel_weight), retract))

    exact("preserving operator intertwines upstairs", multiply(preserving_operator, lift) == multiply(lift, operator_x))
    exact("preserving operator induces the registered downstairs operator", multiply(multiply(retract, preserving_operator), lift) == operator_x)
    exact("preserving operator has zero off-image leakage", is_zero_matrix(multiply(multiply(off_projector, preserving_operator), lift)))
    exact("leaking operator induces the same downstairs operator", multiply(multiply(retract, leaking_operator), lift) == operator_x)
    exact("paired operators are observationally identical", multiply(multiply(retract, preserving_operator), lift) == multiply(multiply(retract, leaking_operator), lift))
    exact("leaking operator has a nonzero hidden channel", not is_zero_matrix(multiply(multiply(off_projector, leaking_operator), lift)))

    def equation_x(vector4):
        return vec_add(matvec(operator_x, vector4), quadratic_x(vector4))

    def preserving_euler(vector14):
        observed = matvec(retract, vector14)
        return vec_add(matvec(preserving_operator, vector14), matvec(lift, quadratic_x(observed)))

    def leaking_euler(vector14):
        observed = matvec(retract, vector14)
        return vec_add(preserving_euler(vector14), matvec(kernel_lift, leakage_quadratic(observed)))

    lifted_x = matvec(lift, x)
    pass_value = preserving_euler(lifted_x)
    fail_value = leaking_euler(lifted_x)
    exact("nonlinear preserving map induces E_X", matvec(retract, pass_value) == equation_x(x))
    exact("nonlinear preserving map closes on the image", is_zero_vector(matvec(off_projector, pass_value)))
    exact("nonlinear leaking map induces the same E_X", matvec(retract, fail_value) == equation_x(x))
    exact("nonlinear leaking map leaves the image", not is_zero_vector(matvec(off_projector, fail_value)))
    exact("nonlinear paired maps differ upstairs", pass_value != fail_value)

    wave3 = next(row for row in campaign["waves"] if row["id"] == "ECW3-G4-OBSERVATION")
    gate = campaign["third_lane_promotion_gate"]
    exact("campaign remains ready while ECW3A records a partial result", wave3["status"] == registry["wave_disposition"]["campaign_status"] and wave3["result"]["status_boundary"] == "DECISIVE_FINITE_MAP_AND_LEAKAGE_GATE_ONLY__ACTUAL_Y14_FUNCTOR_OPEN")
    exact("campaign points to the ECW3A registry", wave3["result"]["registry"] == "lab/process/eric-curt-wave3a-observation-dual-leakage.json")
    exact("Curt remains a rival inside the Eric lane", campaign["construction_lanes"] == ["INDEPENDENT_NATIVE", "ERIC_GUIDED_WITH_CURT_RIVAL_TRACK"])
    exact("third-lane gate remains conjunctive and closed", gate["logic"] == "TG-1 AND TG-2 AND TG-3" and gate["current_verdict"] == "NOT_PROMOTED")
    exact("active real carrier owns the exact finite pairing gate", registry["branch_ledger"][0]["status"] == "EXACT_FINITE_GATE_ONLY__GLOBAL_Y14_OPEN")
    exact("Curt real carrier retains an explicit port debit", registry["branch_ledger"][1]["status"] == "PORT_REQUIRED_FOR_PAIRING_ADJOINT_DOMAIN_AND_DYNAMICS")
    exact("common complexification cannot select the real adjoint", registry["branch_ledger"][2]["status"] == "INSUFFICIENT_TO_SELECT_REAL_KREIN_ADJOINT_OR_DOMAIN")
    exact("next gate is global domain and quotient", registry["wave_disposition"]["next_gate"] == "ECW3B-GLOBAL-DESCENT-DOMAIN-QUOTIENT")

    planted("left inverse implies ambient identity", projector == identity(14))
    planted("field retract equals equation dual", retract == equation_dual)
    planted("field retract equals Krein-Riesz adjoint", retract == riesz_adjoint)
    planted("native ambient pairing is positive definite", all(metric_y[i][i] > 0 for i in range(14)))
    planted("observed linear intertwining proves no leakage", is_zero_matrix(multiply(multiply(off_projector, leaking_operator), lift)))
    planted("leaking operator preserves the image", multiply(leaking_operator, lift) == multiply(lift, operator_x))
    planted("observed nonlinear equation proves closure", is_zero_vector(matvec(off_projector, fail_value)))
    planted("paired ambient operators are identical", preserving_operator == leaking_operator)
    planted("complexification selects the real adjoint", registry["branch_ledger"][2]["status"].startswith("SELECTED"))
    planted("partial TG-1 promotes Curt", gate["status"]["TG-1"].startswith("PASS") and gate["current_verdict"] == "PROMOTED")
    planted("Curt already occupies a third construction lane", len(campaign["construction_lanes"]) == 3)

    expected = registry["exact_probe"]
    if exact_checks != expected["expected_exact_checks"]:
        raise AssertionError(f"exact check count drift: {exact_checks} != {expected['expected_exact_checks']}")
    if planted_checks != expected["expected_planted_failures"]:
        raise AssertionError(f"planted check count drift: {planted_checks} != {expected['expected_planted_failures']}")

    print(
        "ERIC-CURT-WAVE3A-OBSERVATION-DUAL-LEAKAGE: "
        f"{exact_checks} exact checks + {planted_checks} planted failures = "
        f"{exact_checks + planted_checks} PASS"
    )
    print("RESULT: R, L^vee, and L^! are typed separately on an exact (9,5)->(3,1) finite gate")
    print("RESULT: identical observed linear and nonlinear equations do not imply image preservation")
    print("BOUNDARY: actual global Y14 descent, Krein domain, quotient, and preboundary reduction remain open")
    print("LANES: Curt remains a rival track; TG-1/TG-2/TG-3 do not jointly pass")


if __name__ == "__main__":
    main()
