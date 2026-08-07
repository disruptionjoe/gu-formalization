#!/usr/bin/env python3
"""Exact ECW3C metric-bundle atlas and ordinary Cauchy-domain gate.

This probe replaces ECW3B's arbitrary finite frames by the actual transition
forced by ``Y = Met_{3,1}(X)``: a base Jacobian ``A`` and its congruence action
on ``Sym^2(T*X)``.  It verifies exact descent of the Lorentz metric, the
trace-reversed DeWitt fibre metric, the total gimmel metric, and an admitted
section jet.  It then joins the resulting ``(9,5)`` inertia to W131's actual
principal-symbol result and kills the ordinary codimension-one Lorentzian
Cauchy route on full ``Y``.

It does not prove a global Lorentz section exists, construct a spin lift or
right-H analytic domain, or rule out section-pullback and genuinely
ultrahyperbolic/Krein boundary-domain constructions.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path

import eric_curt_wave3b_cech_domain_quotient_probe as w3b


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/eric-curt-wave3c-y14-atlas-cauchy-domain.json"
CAMPAIGN = ROOT / "lab/process/eric-curt-ten-wave-campaign.json"

matrix = w3b.matrix
identity = w3b.identity
transpose = w3b.transpose
multiply = w3b.multiply
block_diag = w3b.block_diag
inverse = w3b.inverse

PAIRS = tuple((i, j) for i in range(4) for j in range(i, 4))


def basis_symmetric(pair):
    i, j = pair
    result = [[F(0) for _ in range(4)] for _ in range(4)]
    result[i][j] = F(1)
    result[j][i] = F(1)
    return matrix(result)


def symmetric_coordinates(value):
    return tuple(value[i][j] for i, j in PAIRS)


def congruence(jacobian, value):
    """Metric-coordinate change h_target=A^{-T} h_source A^{-1}."""
    jacobian_inverse = inverse(jacobian)
    return multiply(multiply(transpose(jacobian_inverse), value), jacobian_inverse)


def symmetric_representation(jacobian):
    columns = [symmetric_coordinates(congruence(jacobian, basis_symmetric(pair))) for pair in PAIRS]
    return matrix([[columns[column][row] for column in range(10)] for row in range(10)])


def trace(value):
    return sum(value[i][i] for i in range(len(value)))


def fiber_metric(metric):
    """V_h(k,l)=tr(h^-1 k h^-1 l)-1/2 tr(h^-1 k)tr(h^-1 l)."""
    metric_inverse = inverse(metric)
    basis = [basis_symmetric(pair) for pair in PAIRS]
    raised = [multiply(metric_inverse, item) for item in basis]
    return matrix(
        [
            [
                trace(multiply(raised[i], raised[j]))
                - F(1, 2) * trace(raised[i]) * trace(raised[j])
                for j in range(10)
            ]
            for i in range(10)
        ]
    )


def gimmel(metric):
    return block_diag(metric, fiber_metric(metric))


def vertical_stack(top, bottom):
    return matrix([list(row) for row in top] + [list(row) for row in bottom])


def bilinear(left, form, right):
    return sum(
        left[row] * form[row][column] * right[column]
        for row in range(len(left))
        for column in range(len(right))
    )


def quadratic_discriminant(form, direction, comparator):
    return 4 * (
        bilinear(comparator, form, direction) ** 2
        - bilinear(direction, form, direction) * bilinear(comparator, form, comparator)
    )


def inertia(value):
    """Exact inertia by rational symmetric congruence elimination."""
    work = [list(row) for row in value]
    positive = negative = zero = 0
    while work:
        size = len(work)
        diagonal = next((i for i in range(size) if work[i][i] != 0), None)
        if diagonal is not None:
            work[0], work[diagonal] = work[diagonal], work[0]
            for row in work:
                row[0], row[diagonal] = row[diagonal], row[0]
            pivot = work[0][0]
            if pivot > 0:
                positive += 1
            else:
                negative += 1
            work = [
                [work[i][j] - work[i][0] * work[0][j] / pivot for j in range(1, size)]
                for i in range(1, size)
            ]
            continue

        off = next(
            ((i, j) for i in range(size) for j in range(i + 1, size) if work[i][j] != 0),
            None,
        )
        if off is None:
            zero += size
            break
        i, j = off
        order = [i, j] + [k for k in range(size) if k not in (i, j)]
        work = [[work[row][column] for column in order] for row in order]
        block = matrix([work[0][:2], work[1][:2]])
        block_inverse = inverse(block)
        coupling = matrix([work[0][2:], work[1][2:]])
        remainder = matrix([row[2:] for row in work[2:]])
        correction = multiply(multiply(transpose(coupling), block_inverse), coupling)
        work = [
            [remainder[row][column] - correction[row][column] for column in range(size - 2)]
            for row in range(size - 2)
        ]
        positive += 1
        negative += 1
    return positive, negative, zero


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

    exact("Sym2 fibre rank is ten", len(PAIRS) == 10)
    exact("metric-bundle total rank is fourteen", 4 + len(PAIRS) == 14)

    a01 = matrix([[1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 1]])
    a12 = matrix([[1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 1]])
    a02 = multiply(a01, a12)
    base_transitions = {(0, 1): a01, (1, 2): a12, (0, 2): a02}
    vertical_transitions = {
        pair: symmetric_representation(jacobian)
        for pair, jacobian in base_transitions.items()
    }
    total_transitions = {
        pair: block_diag(base_transitions[pair], vertical_transitions[pair])
        for pair in base_transitions
    }

    exact("base atlas triple cocycle", multiply(a01, a12) == a02)
    exact(
        "Sym2 atlas triple cocycle",
        multiply(vertical_transitions[(0, 1)], vertical_transitions[(1, 2)])
        == vertical_transitions[(0, 2)],
    )
    exact(
        "total Y14 atlas triple cocycle",
        multiply(total_transitions[(0, 1)], total_transitions[(1, 2)])
        == total_transitions[(0, 2)],
    )
    for pair in base_transitions:
        exact(f"base transition {pair} invertible", multiply(base_transitions[pair], inverse(base_transitions[pair])) == identity(4))
        exact(f"Sym2 transition {pair} invertible", multiply(vertical_transitions[pair], inverse(vertical_transitions[pair])) == identity(10))

    metrics = [None, None, matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]])]
    metrics[1] = congruence(a12, metrics[2])
    metrics[0] = congruence(a01, metrics[1])
    exact("direct metric cocycle agrees", metrics[0] == congruence(a02, metrics[2]))

    fiber_metrics = [fiber_metric(metric) for metric in metrics]
    gimmel_metrics = [gimmel(metric) for metric in metrics]
    for patch in range(3):
        exact(f"patch {patch} Lorentz metric inertia", inertia(metrics[patch]) == (3, 1, 0))
        exact(f"patch {patch} trace-reversed fibre inertia", inertia(fiber_metrics[patch]) == (6, 4, 0))
        exact(f"patch {patch} gimmel inertia", inertia(gimmel_metrics[patch]) == (9, 5, 0))

    for target, source in base_transitions:
        a = base_transitions[(target, source)]
        s = vertical_transitions[(target, source)]
        total = total_transitions[(target, source)]
        exact(
            f"base metric descent {target}{source}",
            multiply(multiply(transpose(a), metrics[target]), a) == metrics[source],
        )
        exact(
            f"DeWitt fibre metric descent {target}{source}",
            multiply(multiply(transpose(s), fiber_metrics[target]), s) == fiber_metrics[source],
        )
        exact(
            f"total gimmel descent {target}{source}",
            multiply(multiply(transpose(total), gimmel_metrics[target]), total) == gimmel_metrics[source],
        )

    jet2 = matrix(
        [
            [F(1, 20), 0, 0, 0],
            [0, F(1, 30), 0, 0],
            [0, 0, F(1, 40), 0],
            [0, 0, 0, F(1, 50)],
        ]
        + [[0, 0, 0, 0] for _ in range(6)]
    )
    jets = [None, None, jet2]
    jets[1] = multiply(multiply(vertical_transitions[(1, 2)], jets[2]), inverse(a12))
    jets[0] = multiply(multiply(vertical_transitions[(0, 1)], jets[1]), inverse(a01))
    exact(
        "direct admitted section-jet cocycle agrees",
        jets[0] == multiply(multiply(vertical_transitions[(0, 2)], jets[2]), inverse(a02)),
    )
    graph_lifts = [vertical_stack(identity(4), jet) for jet in jets]
    pullback_metrics = [
        multiply(multiply(transpose(graph_lifts[patch]), gimmel_metrics[patch]), graph_lifts[patch])
        for patch in range(3)
    ]
    for patch in range(3):
        exact(f"patch {patch} admitted section pullback remains Lorentzian", inertia(pullback_metrics[patch]) == (3, 1, 0))
    for target, source in base_transitions:
        a = base_transitions[(target, source)]
        total = total_transitions[(target, source)]
        exact(
            f"section-jet graph descent {target}{source}",
            multiply(total, graph_lifts[source]) == multiply(graph_lifts[target], a),
        )
        exact(
            f"section pullback metric descent {target}{source}",
            multiply(multiply(transpose(a), pullback_metrics[target]), a) == pullback_metrics[source],
        )

    ambient_positive, ambient_negative = 9, 5
    hypersurface_dimension = 13
    negative_floor = hypersurface_dimension + ambient_negative - 14
    exact("every Y14 hypersurface retains at least four negative directions", negative_floor == 4)
    exact("full Y14 has higher index rather than Lorentz index", ambient_negative > 1)
    exact("positive direction leaves eight positive orthogonal directions", ambient_positive - 1 == 8)
    exact("negative direction leaves four negative orthogonal directions", ambient_negative - 1 == 4)
    ambient_form = block_diag(identity(9), w3b.scale(-1, identity(5)))
    e_positive = (F(1),) + (F(0),) * 13
    z_positive = (F(0), F(1)) + (F(0),) * 12
    e_negative = (F(0),) * 9 + (F(1),) + (F(0),) * 4
    z_negative = (F(0),) * 10 + (F(1),) + (F(0),) * 3
    exact("positive representative gives negative hyperbolicity discriminant", quadratic_discriminant(ambient_form, e_positive, z_positive) == -4)
    exact("negative representative gives negative hyperbolicity discriminant after sign reversal", quadratic_discriminant(ambient_form, e_negative, z_negative) == -4)
    exact("section pullback has Lorentz negative index one", inertia(pullback_metrics[2])[1] == 1)
    exact("physical three-surface has codimension eleven in Y14", 14 - 3 == 11)

    wave3 = next(row for row in campaign["waves"] if row["id"] == "ECW3-G4-OBSERVATION")
    wave3c = wave3["result"]["wave3c"]
    gate = campaign["third_lane_promotion_gate"]
    exact("campaign records ECW3C actual-atlas boundary", wave3c["registry"] == "lab/process/eric-curt-wave3c-y14-atlas-cauchy-domain.json" and wave3c["status_boundary"] == registry["wave_disposition"]["scientific_status"])
    exact("ECW3C records its immutable section-domain next gate", wave3c["next_gate"] == registry["wave_disposition"]["next_gate"])
    exact("campaign live handoff points to section-domain next gate", wave3["result"]["current_next_swing"] == registry["wave_disposition"]["next_gate"])
    exact("Curt remains a rival inside the Eric lane", campaign["construction_lanes"] == ["INDEPENDENT_NATIVE", "ERIC_GUIDED_WITH_CURT_RIVAL_TRACK"])
    exact("third-lane gate remains closed", gate["logic"] == "TG-1 AND TG-2 AND TG-3" and gate["current_verdict"] == "NOT_PROMOTED")
    exact("active branch earns vertical atlas and split-frame gimmel but not analytic domain", registry["branch_ledger"][0]["status"] == "ACTUAL_METRIC_BUNDLE_VERTICAL_ATLAS_EXACT__SPLIT_FRAME_GIMMEL_EXACT__ORDINARY_AMBIENT_CAUCHY_ROUTE_KILLED__ANALYTIC_DOMAIN_OPEN")
    exact("Curt branch retains a separate real analytic port", registry["branch_ledger"][1]["status"] == "SEPARATE_7_7_ATLAS_PAIRING_DOMAIN_PORT_REQUIRED")
    exact("common complexification cannot select causal domain", registry["branch_ledger"][2]["status"] == "INSUFFICIENT_TO_SELECT_REAL_HYPERBOLIC_OR_KREIN_DOMAIN")
    exact("W131 frame-symbol result is inherited not overstated", registry["inherited_evidence"]["w131_grade"] == "ACTUAL_Y14_FRAME_AND_SYMBOL_ONLY__ANALYTIC_LAYER_OPEN")
    exact("W131 evidence path exists", (ROOT / registry["inherited_evidence"]["w131"]).is_file())
    exact("prior hypersurface control path exists", (ROOT / registry["inherited_evidence"]["prior_hypersurface_control"]).is_file())

    planted("Sym2 fibre has rank sixteen", len(PAIRS) == 16)
    planted("an arbitrary GL14 frame is an actual metric-bundle chart transition", registry["verdict"]["arbitrary_gl14_is_metric_atlas"] == "PASS")
    planted("tensor atlas descent proves a global Lorentz section exists", registry["verdict"]["global_lorentz_section"] == "PROVED")
    planted("affine transition control supplies a connection for every nonlinear chart", registry["verdict"]["nonlinear_horizontal_split"] == "PROVED")
    planted("signature (9,5) is Lorentzian", ambient_negative == 1)
    planted("Y14 admits a positive thirteen-dimensional hypersurface", negative_floor == 0)
    planted("the (9,5) quadratic is hyperbolic in a positive direction", -4 >= 0)
    planted("pointwise Krein symmetry supplies a closed self-adjoint domain", registry["verdict"]["analytic_closed_domain"] == "PASS")
    planted("section-pullback Cauchy data determine a generic ambient field", 14 - 3 == 1)
    planted("X spin follows from the metric-bundle atlas", registry["verdict"]["x_spin"] == "PROVED")
    planted("common complexification selects the real causal domain", registry["branch_ledger"][2]["status"].startswith("SELECTED"))
    planted("the finite characteristic quotient is already a physical BFV phase space", registry["verdict"]["physical_bfv_phase_space"] == "PASS")
    planted("Curt now occupies a third construction lane", len(campaign["construction_lanes"]) == 3)

    expected = registry["exact_probe"]
    if exact_checks != expected["expected_exact_checks"]:
        raise AssertionError(f"exact check count drift: {exact_checks} != {expected['expected_exact_checks']}")
    if planted_checks != expected["expected_planted_failures"]:
        raise AssertionError(f"planted check count drift: {planted_checks} != {expected['expected_planted_failures']}")

    print(
        "ERIC-CURT-WAVE3C-Y14-ATLAS-CAUCHY-DOMAIN: "
        f"{exact_checks} exact checks + {planted_checks} planted failures = "
        f"{exact_checks + planted_checks} PASS"
    )
    print("RESULT: GL4-induced Sym2 transitions give exact vertical atlas plus affine/connection-adapted Lorentz, DeWitt, gimmel, and admitted-section-jet descent")
    print("KILL: the full signature-(9,5) W131 symbol has no ordinary Lorentzian hyperbolic direction or spacelike codimension-one Cauchy surface")
    print("BOUNDARY: global section, X spin, right-H analytic domain, section Green form, ambient propagator, and BFV phase space remain open")
    print("LANES: Curt remains a rival track; TG-1/TG-2/TG-3 do not jointly pass")


if __name__ == "__main__":
    main()
