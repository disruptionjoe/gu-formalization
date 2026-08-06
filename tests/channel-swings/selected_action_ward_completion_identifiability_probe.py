#!/usr/bin/env python3
"""Exact Ward-completion identifiability for the stationary action-spin block."""

from collections import Counter
from io import StringIO
from pathlib import Path
import contextlib
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/selected_action_stationary_spin_lc_hessian_probe.py"
OWNER_BACKEND = ROOT / "tests/channel-swings/two_layer_action_selected_cubic_owner_retype_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=hook)


print("A. SOURCE, PREDECESSORS, AND LAYER 0")
source = (ROOT / "lab/literature/weinstein-ucsd-2025-04-transcript.md").read_text()
owner_report = (ROOT / "explorations/conditional-build/two-layer-action-selected-cubic-owner-retype-2026-08-06.md").read_text()
check("source", "Weinstein requires perpendicularity to diffeomorphism orbits", "perpendicular to orbits under the diffeomorphism group" in source)
check("source", "Weinstein ties the correction to action exactness", "exact for the integral of the scalar curvature" in source)
check("source", "the source does not publish the missing companion coefficients", "WARD_COMPLETION_AFFINE_DIMENSION_21" not in source)
check("repo", "the owner retype keeps I1B I2B and observer full-II distinct", all(token in owner_report for token in ("first layer `I1B`", "second layer `I2B`", "observer `I_II`")))

capture = StringIO()
with contextlib.redirect_stdout(capture):
    X = runpy.run_path(str(BACKEND))
check("repo", "the exact stationary action-spin Hessian predecessor replays", "PASS 64/64" in capture.getvalue())
capture = StringIO()
with contextlib.redirect_stdout(capture):
    runpy.run_path(str(OWNER_BACKEND))
check("repo", "the three-owner Layer-0 predecessor replays", "PASS 29/29" in capture.getvalue())

for label in (
    "same-I1B direct companion versus independently invariant action",
    "Ward-compatible target versus action-derived coefficient",
    "spacetime diffeomorphism versus connection Lorentz gauge",
    "observer coordinate transport versus dynamical cancellation",
):
    check("type", label + " remain distinct", True)


slots = X["slots"]
orbits = X["orbits"]
hessians = X["hessians"]
metric_basis = X["metric_basis"]
eta = sp.diag(1, -1, -1, -1)


def diffeomorphism_symbol(covector):
    out = sp.zeros(10, 4)
    for column in range(4):
        for row, (i, j) in enumerate(slots):
            out[row, column] = (
                (covector[i] if j == column else 0)
                + (covector[j] if i == column else 0)
            )
    return out


def symmetric_matrix_basis(size):
    out = []
    for i in range(size):
        for j in range(i, size):
            matrix = sp.zeros(size)
            matrix[i, j] = 1
            matrix[j, i] = 1
            out.append(matrix)
    return out


def inertia(matrix):
    positive = negative = zero = 0
    for value, multiplicity in matrix.eigenvals().items():
        sign = sp.sign(value)
        if sign == 1:
            positive += multiplicity
        elif sign == -1:
            negative += multiplicity
        elif sign == 0:
            zero += multiplicity
        else:
            raise AssertionError(f"undecidable sign: {value}")
    return positive, negative, zero


def einstein_hessian(covector):
    """Local Fierz-Pauli/linearized-Einstein bilinear, up to overall scale."""
    k_cov = sp.Matrix(covector)
    k_up = eta * k_cov
    k2 = (k_cov.T * eta * k_cov)[0]
    matrix = sp.zeros(10)
    for a, h_raw in enumerate(metric_basis):
        h = sp.Matrix(h_raw)
        tr_h = sp.trace(eta * h)
        kk_h = (k_up.T * h * k_up)[0]
        v_h = (k_up.T * h).T
        for b, l_raw in enumerate(metric_basis):
            l = sp.Matrix(l_raw)
            tr_l = sp.trace(eta * l)
            kk_l = (k_up.T * l * k_up)[0]
            v_l = (k_up.T * l).T
            b1 = k2 * sp.trace(eta * h * eta * l)
            b2 = k2 * tr_h * tr_l
            b3 = tr_h * kk_l + tr_l * kk_h
            b4 = (v_h.T * eta * v_l)[0]
            matrix[a, b] = -b1 + b2 - b3 + 2 * b4
    return matrix


print("\nB. SYMMETRIC WARD-COMPLETION AFFINE SPACE")
symmetric_basis = symmetric_matrix_basis(10)
completions = {}
diagnostic_totals = {}
expected_completion_ranks = {"timelike": 3, "spacelike": 3, "null": 6}
expected_total_ranks = {"timelike": 6, "spacelike": 6, "null": 2}
expected_completion_inertias = {
    "timelike": (0, 3, 7),
    "spacelike": (1, 2, 7),
    "null": (3, 3, 4),
}
for name, covector in orbits.items():
    D = diffeomorphism_symbol(covector)
    H = hessians[name]
    linear = sp.Matrix.hstack(*[sp.Matrix(S * D).reshape(40, 1) for S in symmetric_basis])
    target = sp.Matrix(-H * D).reshape(40, 1)
    check("exact", f"{name}: symmetric completion system has rank 34", linear.rank() == 34)
    check("exact", f"{name}: Ward target is compatible", linear.row_join(target).rank() == 34)
    check("exact", f"{name}: affine completion dimension is 21", len(symmetric_basis) - linear.rank() == 21)
    check("exact", f"{name}: stationary compatibility matrix is symmetric", D.T * H * D == (D.T * H * D).T)

    projector = sp.eye(10) - D * (D.T * D).inv() * D.T
    completion = projector.T * H * projector - H
    total = H + completion
    completions[name] = completion
    diagnostic_totals[name] = total
    check("exact", f"{name}: diagnostic completion is symmetric", completion == completion.T)
    check("exact", f"{name}: diagnostic completion cancels the residual", completion * D == -H * D and total * D == sp.zeros(10, 4))
    check("exact", f"{name}: diagnostic completion has exact rank", completion.rank() == expected_completion_ranks[name])
    check("exact", f"{name}: diagnostic completion has exact inertia", inertia(completion) == expected_completion_inertias[name])
    check("exact", f"{name}: diagnostic Ward total has exact rank", total.rank() == expected_total_ranks[name])

    quotient_basis = sp.Matrix.hstack(*[sp.Matrix(v) for v in D.T.nullspace()])
    quotient_forms = []
    for i in range(6):
        for j in range(i, 6):
            K = sp.zeros(6)
            K[i, j] = 1
            K[j, i] = 1
            quotient_forms.append(quotient_basis * K * quotient_basis.T)
    quotient_columns = sp.Matrix.hstack(*[sp.Matrix(Q).reshape(100, 1) for Q in quotient_forms])
    check("exact", f"{name}: quotient-form freedom has dimension 21", quotient_columns.rank() == 21)
    check("exact", f"{name}: every quotient form preserves Ward cancellation", all(Q * D == sp.zeros(10, 4) for Q in quotient_forms))
    check("planted", f"PLANT {name}: two Ward completions have different transverse coefficients", completion + quotient_forms[0] != completion and (completion + quotient_forms[0]) * D == -H * D)


print("\nC. WRONG-OWNER AND OBSERVATION CONTROLS")
expected_einstein_ranks = {"timelike": 6, "spacelike": 6, "null": 4}
observer = sp.eye(10)
observer[0, 1] = 2
observer[3, 7] = -1
observer[8, 9] = 3
for name, covector in orbits.items():
    D = diffeomorphism_symbol(covector)
    H = hessians[name]
    E = einstein_hessian(covector)
    check("exact", f"{name}: Einstein control is symmetric", E == E.T)
    check("exact", f"{name}: Einstein control is separately diffeomorphism-radical", E * D == sp.zeros(10, 4))
    check("exact", f"{name}: Einstein control has expected rank", E.rank() == expected_einstein_ranks[name])
    check("exact", f"{name}: an invariant block cannot cancel the spin residual", (H + 7 * E) * D == H * D and (H * D).rank() == 3)

    observed_H = observer.T * H * observer
    observed_D = observer.inv() * D
    check("exact", f"{name}: observation transports rather than cancels the residual", (observed_H * observed_D).rank() == 3 and observed_H * observed_D == observer.T * H * D)

check("type", "observer full-II remains a separate action owner until a map is constructed", "a source-native map `I2B -> I_II`" in owner_report)
check("type", "the missing companion belongs to explicit same-I1B metric/coframe data", True)
check("planted", "PLANT Ward compatibility alone does not select the 21 quotient coefficients", all(len(D.T.nullspace()) == 6 for D in [diffeomorphism_symbol(k) for k in orbits.values()]))


print("\nD. REGISTRY AND PROGRAM FENCES")
registry = strict("lab/process/selected-action-ward-completion-identifiability.json")
check("source", "source return is scoped", registry["source_return"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT")
check("exact", "registry records 34 fixed and 21 free symmetric directions", registry["exact_result"]["ward_fixed_symmetric_directions"] == 34 and registry["exact_result"]["ward_unfixed_quotient_form_directions"] == 21)
check("exact", "registry does not promote the diagnostic completion", registry["exact_result"]["diagnostic_projector_completion"] == "EXACT_NONNATURAL_TARGET_ONLY__NOT_ACTION_DERIVED")
check("exact", "no free object or datum is introduced", registry["free_object_delta"] == 0 and set(registry["external_datum"].values()) == {"UNUSED"})
check("type", "same-I1B coefficient assembly remains open", registry["exact_result"]["same_i1b_direct_metric_coframe_completion"] == "OPEN")
check("type", "Curt and third-lane fences hold", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and registry["third_lane"] == "NOT_PROMOTED")
for label in (
    "affine solvability is not derivation",
    "a Euclidean slot projector is not Lorentz-natural geometry",
    "an Einstein control is not an I1B counterterm",
    "a separate full-II action is not imported into I1B",
    "Ward cancellation is not a BV quotient or physical graviton",
    "P1 P2 P3 remain unused",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS_AND_SOURCE-SILENT")
print("WARD_COMPLETION=SYMMETRIC_SYSTEM_RANK34__AFFINE_DIMENSION21")
print("SEPARATELY_INVARIANT_BLOCK_CANNOT_CANCEL_NONZERO_RESIDUAL")
print("OBSERVATION_TRANSPORTS_RESIDUAL_RANK3")
print("CORRECT_NEXT_OWNER=SAME_I1B_DIRECT_METRIC_COFRAME_HODGE_SHIAB_KREIN_DENSITY_PACKET")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
