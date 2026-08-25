#!/usr/bin/env python3
"""Exact ECW3B Cech-descent, domain, and quotient compatibility gate.

The probe conjugates one exact observation/Euler packet through three rational
patch frames.  It verifies field and equation descent, algebraic-dual and
Krein-adjoint naturality, nonlinear no-leakage, a finite invariant Krein graph
domain, and reduction of a pulled-back preboundary form by its characteristic
kernel.  A planted kernel-valued patch lift keeps every local ``R_i L_i=1``
identity while failing overlap descent.

This is a finite compatibility theorem.  It does not construct an atlas on
the actual metric bundle, prove existence of a Lorentz section for an
arbitrary four-manifold, or supply an analytic closed operator domain.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path

import eric_curt_wave3a_observation_dual_leakage_probe as w3a


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/eric-curt-wave3b-cech-domain-quotient.json"
CAMPAIGN = ROOT / "lab/process/eric-curt-ten-wave-campaign.json"

matrix = w3a.matrix
identity = w3a.identity
transpose = w3a.transpose
multiply = w3a.multiply
add = w3a.add
subtract = w3a.subtract
scale = w3a.scale
matvec = w3a.matvec
vec_add = w3a.vec_add
is_zero_matrix = w3a.is_zero_matrix
is_zero_vector = w3a.is_zero_vector


def inverse(value):
    size = len(value)
    assert size == len(value[0])
    augmented = [list(value[row]) + list(identity(size)[row]) for row in range(size)]
    for column in range(size):
        pivot = next(row for row in range(column, size) if augmented[row][column] != 0)
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [entry / divisor for entry in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    augmented[row][index] - factor * augmented[column][index]
                    for index in range(2 * size)
                ]
    return tuple(tuple(row[size:]) for row in augmented)


def block_diag(left, right):
    rows = len(left) + len(right)
    columns = len(left[0]) + len(right[0])
    result = [[F(0) for _ in range(columns)] for _ in range(rows)]
    for i, row in enumerate(left):
        for j, entry in enumerate(row):
            result[i][j] = entry
    for i, row in enumerate(right):
        for j, entry in enumerate(row):
            result[len(left) + i][len(left[0]) + j] = entry
    return matrix(result)


def lower_block_frame(observed, normal_shear, normal):
    result = []
    for row in range(4):
        result.append(list(observed[row]) + [F(0)] * 10)
    for row in range(10):
        result.append(list(normal_shear[row]) + list(normal[row]))
    return matrix(result)


def rank(value):
    work = [list(row) for row in value]
    rows = len(work)
    columns = len(work[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, rows) if work[row][column] != 0), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        divisor = work[pivot_row][column]
        work[pivot_row] = [entry / divisor for entry in work[pivot_row]]
        for row in range(rows):
            if row != pivot_row and work[row][column] != 0:
                factor = work[row][column]
                work[row] = [
                    work[row][index] - factor * work[pivot_row][index]
                    for index in range(columns)
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def quadratic(vector):
    x0, x1, x2, x3 = vector
    return (x0 * x1, x1 * x1, x2 * x2, x0 * x3)


def bilinear(left, form, right):
    return w3a.dot(left, matvec(form, right))


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

    lift0 = matrix([[int(i == j) for j in range(4)] for i in range(14)])
    normal_mix = matrix(
        [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        ]
    )
    retract0 = matrix(
        [[int(i == j) for j in range(4)] + list(normal_mix[i]) for i in range(4)]
    )
    projector0 = multiply(lift0, retract0)
    off0 = subtract(identity(14), projector0)

    metric_y0 = matrix(
        [[(1 if i < 3 or 4 <= i < 10 else -1) if i == j else 0 for j in range(14)] for i in range(14)]
    )
    metric_x0 = multiply(multiply(transpose(lift0), metric_y0), lift0)
    adjoint0 = multiply(multiply(inverse(metric_x0), transpose(lift0)), metric_y0)

    domain_basis0 = matrix(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 1],
        ]
    )
    domain_retract0 = matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    domain_projector0 = multiply(domain_basis0, domain_retract0)
    domain_metric0 = multiply(multiply(transpose(domain_basis0), metric_x0), domain_basis0)
    theta_domain = matrix([[1, 0, 0], [0, 1, 0], [0, 0, -1]])

    operator_x0 = matrix(
        [
            [2, 0, 0, 1],
            [0, 3, 0, 0],
            [0, 0, 5, 0],
            [-1, 0, 0, 4],
        ]
    )
    operator_y0 = add(multiply(multiply(lift0, operator_x0), retract0), scale(2, off0))

    def euler_x0(vector4):
        return vec_add(matvec(operator_x0, vector4), quadratic(vector4))

    def euler_y0(vector14):
        observed = matvec(retract0, vector14)
        return vec_add(matvec(operator_y0, vector14), matvec(lift0, quadratic(observed)))

    observed_frames = [
        identity(4),
        block_diag(matrix([[1, 1], [0, 1]]), matrix([[2, 0], [0, 1]])),
        block_diag(matrix([[1, 0], [1, 1]]), matrix([[1, 0], [0, 3]])),
    ]
    shear1 = matrix(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [1, -1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, -1],
            [1, 0, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    )
    shear2 = matrix(
        [
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [1, 0, -1, 0],
            [0, 1, 0, -1],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    )
    ambient_frames = [
        identity(14),
        lower_block_frame(observed_frames[1], shear1, identity(10)),
        lower_block_frame(observed_frames[2], shear2, block_diag(scale(2, identity(5)), identity(5))),
    ]

    observed_inverses = [inverse(frame) for frame in observed_frames]
    ambient_inverses = [inverse(frame) for frame in ambient_frames]
    lifts = [
        multiply(multiply(ambient_frames[i], lift0), observed_inverses[i])
        for i in range(3)
    ]
    retracts = [
        multiply(multiply(observed_frames[i], retract0), ambient_inverses[i])
        for i in range(3)
    ]
    projectors = [multiply(lifts[i], retracts[i]) for i in range(3)]
    off_projectors = [subtract(identity(14), projectors[i]) for i in range(3)]
    metric_ys = [
        multiply(multiply(transpose(ambient_inverses[i]), metric_y0), ambient_inverses[i])
        for i in range(3)
    ]
    metric_xs = [
        multiply(multiply(transpose(observed_inverses[i]), metric_x0), observed_inverses[i])
        for i in range(3)
    ]
    adjoints = [
        multiply(multiply(inverse(metric_xs[i]), transpose(lifts[i])), metric_ys[i])
        for i in range(3)
    ]

    domain_bases = [multiply(observed_frames[i], domain_basis0) for i in range(3)]
    domain_retracts = [multiply(domain_retract0, observed_inverses[i]) for i in range(3)]
    domain_projectors = [multiply(domain_bases[i], domain_retracts[i]) for i in range(3)]
    operator_xs = [
        multiply(multiply(observed_frames[i], operator_x0), observed_inverses[i])
        for i in range(3)
    ]

    def euler_x(patch, vector4):
        return matvec(observed_frames[patch], euler_x0(matvec(observed_inverses[patch], vector4)))

    def euler_y(patch, vector14):
        return matvec(ambient_frames[patch], euler_y0(matvec(ambient_inverses[patch], vector14)))

    x0 = tuple(F(entry) for entry in (1, 2, 0, -1))
    for patch in range(3):
        x_i = matvec(observed_frames[patch], x0)
        lifted = matvec(lifts[patch], x_i)
        exact(f"patch {patch} local retract", multiply(retracts[patch], lifts[patch]) == identity(4))
        exact(f"patch {patch} image projector", multiply(projectors[patch], projectors[patch]) == projectors[patch])
        exact(f"patch {patch} observed nonlinear equation", matvec(retracts[patch], euler_y(patch, lifted)) == euler_x(patch, x_i))
        exact(f"patch {patch} nonlinear no leakage", is_zero_vector(matvec(off_projectors[patch], euler_y(patch, lifted))))
        exact(f"patch {patch} adjoint naturality", adjoints[patch] == multiply(multiply(observed_frames[patch], adjoint0), ambient_inverses[patch]))
        exact(f"patch {patch} finite graph domain retract", multiply(domain_retracts[patch], domain_bases[patch]) == identity(3))
        exact(
            f"patch {patch} transported domain metric",
            multiply(multiply(transpose(domain_bases[patch]), metric_xs[patch]), domain_bases[patch]) == domain_metric0,
        )
        exact(f"patch {patch} linear domain invariance", multiply(operator_xs[patch], domain_bases[patch]) == multiply(domain_projectors[patch], multiply(operator_xs[patch], domain_bases[patch])))
        exact(f"patch {patch} nonlinear domain invariance", is_zero_vector(matvec(subtract(identity(4), domain_projectors[patch]), euler_x(patch, x_i))))

    exact("domain metric has signature (2,1)", [domain_metric0[i][i] for i in range(3)] == [1, 1, -1])
    exact("fundamental symmetry gives positive finite majorant", multiply(domain_metric0, theta_domain) == identity(3))
    exact("operator is Krein self-adjoint", multiply(transpose(operator_x0), metric_x0) == multiply(metric_x0, operator_x0))

    def transition(frames, inverses, target, source):
        return multiply(frames[target], inverses[source])

    t01 = transition(ambient_frames, ambient_inverses, 0, 1)
    t12 = transition(ambient_frames, ambient_inverses, 1, 2)
    t02 = transition(ambient_frames, ambient_inverses, 0, 2)
    h01 = transition(observed_frames, observed_inverses, 0, 1)
    h12 = transition(observed_frames, observed_inverses, 1, 2)
    h02 = transition(observed_frames, observed_inverses, 0, 2)
    exact("ambient Cech triple cocycle", multiply(t01, t12) == t02)
    exact("observed Cech triple cocycle", multiply(h01, h12) == h02)

    for target, source in ((0, 1), (1, 2), (0, 2)):
        tij = transition(ambient_frames, ambient_inverses, target, source)
        hij = transition(observed_frames, observed_inverses, target, source)
        exact(f"lift descent {target}{source}", multiply(tij, lifts[source]) == multiply(lifts[target], hij))
        exact(f"retract descent {target}{source}", multiply(retracts[target], tij) == multiply(hij, retracts[source]))
        exact(f"domain-basis descent {target}{source}", multiply(hij, domain_bases[source]) == domain_bases[target])
        exact(f"domain-projector descent {target}{source}", multiply(hij, domain_projectors[source]) == multiply(domain_projectors[target], hij))
        exact(
            f"equation-dual descent {target}{source}",
            multiply(transpose(lifts[target]), transpose(inverse(tij)))
            == multiply(transpose(inverse(hij)), transpose(lifts[source])),
        )
        exact(f"Krein-adjoint descent {target}{source}", multiply(adjoints[target], tij) == multiply(hij, adjoints[source]))
        x_source = matvec(observed_frames[source], x0)
        y_source = matvec(lifts[source], x_source)
        exact(f"nonlinear Euler descent {target}{source}", euler_y(target, matvec(tij, y_source)) == matvec(tij, euler_y(source, y_source)))
        exact(f"observed equation descent {target}{source}", euler_x(target, matvec(hij, x_source)) == matvec(hij, euler_x(source, x_source)))

    omega0 = matrix([[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    kernel0 = matrix([[0, 0], [0, 0], [1, 0], [0, 1]])
    quotient0 = matrix([[1, 0], [0, 1], [0, 0], [0, 0]])
    quotient_form = multiply(multiply(transpose(quotient0), omega0), quotient0)
    exact("preboundary form has rank two", rank(omega0) == 2)
    exact("declared characteristic kernel is exact", is_zero_matrix(multiply(omega0, kernel0)) and rank(kernel0) == 2)
    exact("characteristic quotient is nondegenerate", rank(quotient_form) == 2)
    polarization = (F(1), F(0))
    complement = (F(0), F(1))
    exact("quotient polarization is isotropic", bilinear(polarization, quotient_form, polarization) == 0)
    exact("polarization complement is paired", bilinear(polarization, quotient_form, complement) != 0)

    omega_xs = [
        multiply(multiply(transpose(observed_inverses[patch]), omega0), observed_inverses[patch])
        for patch in range(3)
    ]
    kernel_xs = [multiply(observed_frames[patch], kernel0) for patch in range(3)]
    quotient_xs = [multiply(observed_frames[patch], quotient0) for patch in range(3)]
    omega_ys = [
        multiply(multiply(transpose(retracts[patch]), omega_xs[patch]), retracts[patch])
        for patch in range(3)
    ]
    for patch in range(3):
        exact(f"patch {patch} preboundary pullback", multiply(multiply(transpose(lifts[patch]), omega_ys[patch]), lifts[patch]) == omega_xs[patch])
        exact(f"patch {patch} characteristic kernel", is_zero_matrix(multiply(omega_xs[patch], kernel_xs[patch])))
        exact(f"patch {patch} quotient form", multiply(multiply(transpose(quotient_xs[patch]), omega_xs[patch]), quotient_xs[patch]) == quotient_form)
        domain_omega = multiply(multiply(transpose(domain_bases[patch]), omega_xs[patch]), domain_bases[patch])
        exact(f"patch {patch} domain quotient rank", rank(domain_omega) == 2)

    for target, source in ((0, 1), (1, 2), (0, 2)):
        hij = transition(observed_frames, observed_inverses, target, source)
        exact(
            f"preboundary-form descent {target}{source}",
            multiply(multiply(transpose(hij), omega_xs[target]), hij) == omega_xs[source],
        )
        exact(f"characteristic-kernel descent {target}{source}", multiply(hij, kernel_xs[source]) == kernel_xs[target])
        exact(f"quotient-frame descent {target}{source}", multiply(hij, quotient_xs[source]) == quotient_xs[target])

    kernel_lift0_rows = []
    for row in range(14):
        if row < 4:
            kernel_lift0_rows.append([-normal_mix[row][column] for column in range(4)])
        else:
            kernel_lift0_rows.append([int(row == 4 + column) for column in range(4)])
    kernel_lift0 = matrix(kernel_lift0_rows)
    bad_increment = multiply(
        multiply(ambient_frames[2], kernel_lift0),
        multiply(matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]), observed_inverses[2]),
    )
    bad_lift2 = add(lifts[2], bad_increment)
    exact("hostile patch remains locally split", multiply(retracts[2], bad_lift2) == identity(4))
    exact("hostile patch fails overlap descent", multiply(t12, bad_lift2) != multiply(lifts[1], h12))

    wave3 = next((row for row in campaign["waves"] if row["id"] == "ECW3-G4-OBSERVATION"), None)
    if wave3 is None:
        raise AssertionError("campaign is missing the Wave 3 observation row")
    wave3b = wave3["result"]["wave3b"]
    gate = campaign["third_lane_promotion_gate"]
    exact("campaign records ECW3B finite boundary", wave3b["registry"] == "lab/process/eric-curt-wave3b-cech-domain-quotient.json" and wave3b["status_boundary"] == registry["wave_disposition"]["scientific_status"])
    exact("campaign points to actual Y14 next gate", wave3["result"]["next_swing"] == registry["wave_disposition"]["next_gate"])
    exact("Curt remains a rival inside the Eric lane", campaign["construction_lanes"] == ["INDEPENDENT_NATIVE", "ERIC_GUIDED_WITH_CURT_RIVAL_TRACK"])
    exact("third-lane gate remains closed", gate["logic"] == "TG-1 AND TG-2 AND TG-3" and gate["current_verdict"] == "NOT_PROMOTED")
    exact("active branch owns only a finite compatibility theorem", registry["branch_ledger"][0]["status"] == "EXACT_FINITE_COMPATIBILITY__ACTUAL_Y14_ANALYSIS_OPEN")
    exact("Curt branch retains the real-domain port", registry["branch_ledger"][1]["status"] == "PORT_REQUIRED_FOR_REAL_PAIRING_DOMAIN_AND_PREBOUNDARY_DESCENT")
    exact("common complexification cannot choose a real domain", registry["branch_ledger"][2]["status"] == "INSUFFICIENT_TO_SELECT_REAL_CLOSED_DOMAIN_OR_POLARIZATION")

    planted("local left inverses imply Cech descent", multiply(t12, bad_lift2) == multiply(lifts[1], h12))
    planted("field retract equals equation dual on every patch", all(retracts[i] == transpose(lifts[i]) for i in range(3)))
    planted("equation dual equals Krein adjoint on every patch", all(transpose(lifts[i]) == adjoints[i] for i in range(3)))
    planted("finite invariant graph proves analytic closedness", registry["verdict"]["analytic_closed_domain"] == "PASS")
    planted("degenerate preboundary form is already symplectic", rank(omega0) == 4)
    planted("characteristic kernel survives as a physical mode", rank(multiply(omega0, kernel0)) != 0)
    planted("isotropic line alone fixes physical time", registry["verdict"]["physical_time"] == "SELECTED")
    planted("admitted metric section proves existence for arbitrary X", registry["verdict"]["arbitrary_x_lorentz_section"] == "PROVED")
    planted("common complexification selects the real domain", registry["branch_ledger"][2]["status"].startswith("SELECTED"))
    planted("finite ECW3B closes all of Wave 3", wave3["result"]["next_swing"].startswith("ECW4"))
    planted("Curt now occupies a third construction lane", len(campaign["construction_lanes"]) == 3)

    expected = registry["exact_probe"]
    if exact_checks != expected["expected_exact_checks"]:
        raise AssertionError(f"exact check count drift: {exact_checks} != {expected['expected_exact_checks']}")
    if planted_checks != expected["expected_planted_failures"]:
        raise AssertionError(f"planted check count drift: {planted_checks} != {expected['expected_planted_failures']}")

    print(
        "ERIC-CURT-WAVE3B-CECH-DOMAIN-QUOTIENT: "
        f"{exact_checks} exact checks + {planted_checks} planted failures = "
        f"{exact_checks + planted_checks} PASS"
    )
    print("RESULT: three rational patches transport the nonlinear observation packet, duals, finite Krein domain, and characteristic quotient")
    print("RESULT: local R_i L_i=1 does not imply Cech descent")
    print("BOUNDARY: actual Y14 atlas, Lorentz-section existence, analytic closed domain, and BFV phase space remain open")
    print("LANES: Curt remains a rival track; TG-1/TG-2/TG-3 do not jointly pass")


if __name__ == "__main__":
    main()
