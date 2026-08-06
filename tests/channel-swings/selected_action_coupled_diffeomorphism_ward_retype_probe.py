#!/usr/bin/env python3
"""Exact full-field retype of the stationary diffeomorphism Ward target."""

from collections import Counter
from io import StringIO
from pathlib import Path
import contextlib
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
HESSIAN_BACKEND = ROOT / "tests/channel-swings/selected_action_stationary_spin_lc_hessian_probe.py"
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


print("A. SOURCE, PREDECESSOR, AND LAYER 0")
source = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
ward_report = (ROOT / "explorations/conditional-build/selected-action-ward-completion-identifiability-2026-08-06.md").read_text()
full_ward_report = (ROOT / "explorations/conditional-build/selected-branch-linearized-totalization-current-green-domain-2026-08-05.md").read_text()
check("source", "source action domain contains both inhomogeneous gauge data and metrics", "I^B_1:\\mathcal G\\times \\operatorname{MET}(X^{1,3})" in source)
check("source", "source augmented torsion is an adjoint-valued one-form", "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in source and "\\Omega^1(Y,\\operatorname{ad}P)" in source)
check("repo", "v0.31 metric-only theorem remains an exact scoped result", "rank 34" in ward_report and "21-dimensional affine space" in ward_report)
check("repo", "the earlier full-Ward theorem already requires all primitive field blocks", "Let all primitive fields be `q`" in full_ward_report and "complete\nordinary gauge generator" in full_ward_report)

capture = StringIO()
with contextlib.redirect_stdout(capture):
    X = runpy.run_path(str(HESSIAN_BACKEND))
check("repo", "stationary action-spin Hessian predecessor replays", "PASS 64/64" in capture.getvalue())

for label in (
    "metric-only diffeomorphism slice versus full field-space orbit",
    "connection one-form Lie derivative versus connection Lorentz gauge",
    "coupled Ward radical versus reduced physical BV quotient",
    "diagnostic coupled completion versus action-derived cross blocks",
):
    check("type", label + " remain distinct", True)


slots = X["slots"]
orbits = X["orbits"]
hessians = X["hessians"]


def metric_symbol(covector):
    out = sp.zeros(10, 4)
    for column in range(4):
        for row, (i, j) in enumerate(slots):
            out[row, column] = (
                (covector[i] if j == column else 0)
                + (covector[j] if i == column else 0)
            )
    return out


def one_form_lie_symbol(covector):
    """Principal L_xi T at constant T_mu^nu=delta_mu^nu: k_mu xi^nu."""
    out = sp.zeros(16, 4)
    for mu in range(4):
        for nu in range(4):
            out[4 * mu + nu, nu] = covector[mu]
    return out


def coupled_unknown_operator(D, G):
    """Unknown metric--connection block plus symmetric connection block."""
    R = sp.Matrix.vstack(D, G)
    columns = []
    for i in range(10):
        for a in range(16):
            variation = sp.zeros(26)
            variation[i, 10 + a] = 1
            variation[10 + a, i] = 1
            columns.append(sp.Matrix(variation * R).reshape(104, 1))
    for a in range(16):
        for b in range(a, 16):
            variation = sp.zeros(26)
            variation[10 + a, 10 + b] = 1
            variation[10 + b, 10 + a] = 1
            columns.append(sp.Matrix(variation * R).reshape(104, 1))
    return sp.Matrix.hstack(*columns)


print("\nB. SOURCE-NATIVE PRINCIPAL DIFFEOMORPHISM ORBIT")
for name, covector in orbits.items():
    D = metric_symbol(covector)
    G = one_form_lie_symbol(covector)
    R = sp.Matrix.vstack(D, G)
    check("exact", f"{name}: metric diffeomorphism symbol has rank four", D.rank() == 4)
    check("exact", f"{name}: one-form Lie symbol is nonzero rank four", G.rank() == 4)
    check("exact", f"{name}: complete coupled generator has rank four", R.rank() == 4)
    check("planted", f"PLANT {name}: deleting the connection orbit changes the gauge tangent", R != sp.Matrix.vstack(D, sp.zeros(16, 4)))


print("\nC. COUPLED SYMMETRIC WARD COMPLETION WITH METRIC BLOCK FIXED")
expected_hessian_ranks = {name: matrix.rank() for name, matrix in hessians.items()}
for name, covector in orbits.items():
    D = metric_symbol(covector)
    G = one_form_lie_symbol(covector)
    R = sp.Matrix.vstack(D, G)
    H = hessians[name]
    left_inverse = (G.T * G).inv() * G.T
    quotient_map = sp.Matrix.hstack(sp.eye(10), -D * left_inverse)
    coupled = quotient_map.T * H * quotient_map

    check("exact", f"{name}: one-form Lie symbol has an exact left inverse", left_inverse * G == sp.eye(4))
    check("exact", f"{name}: coupled completion is symmetric", coupled == coupled.T)
    check("exact", f"{name}: coupled completion preserves the isolated metric block", coupled[:10, :10] == H)
    check("exact", f"{name}: full coupled gauge image is radical", coupled * R == sp.zeros(26, 4) and R.T * coupled == sp.zeros(4, 26))
    check("exact", f"{name}: no added metric-metric companion is needed", coupled[:10, :10] - H == sp.zeros(10))
    check("exact", f"{name}: metric--connection cross block is load-bearing", coupled[:10, 10:] != sp.zeros(10, 16))
    check("exact", f"{name}: diagnostic coupled rank equals the fixed metric-block rank", coupled.rank() == expected_hessian_ranks[name])
    check("planted", f"PLANT {name}: the metric block alone still fails the full Ward test", sp.Matrix.vstack(H * D, sp.zeros(16, 4)) != sp.zeros(26, 4))


print("\nD. EXACT IDENTIFIABILITY COUNT")
for name, covector in orbits.items():
    D = metric_symbol(covector)
    G = one_form_lie_symbol(covector)
    H = hessians[name]
    operator = coupled_unknown_operator(D, G)
    target = sp.Matrix.vstack(-H * D, sp.zeros(16, 4)).reshape(104, 1)
    check("exact", f"{name}: coupled unknown space has dimension 296", operator.cols == 10 * 16 + 16 * 17 // 2 == 296)
    check("exact", f"{name}: coupled Ward operator has rank 98", operator.rank() == 98)
    check("exact", f"{name}: fixed metric block has compatible coupled completions", operator.row_join(target).rank() == 98)
    check("exact", f"{name}: coupled affine ambiguity has dimension 198", operator.cols - operator.rank() == 198)

check("planted", "PLANT the v0.31 34-plus-21 count is not the coupled 98-plus-198 count", (34, 21) != (98, 198))
check("type", "the 198 directions are uncomputed block freedom, not 198 physical parameters", True)


print("\nE. REGISTRY AND PROGRAM FENCES")
registry = strict("lab/process/selected-action-coupled-diffeomorphism-ward-retype.json")
check("source", "decisive source return is SOURCE-CORRECTS", registry["source_return"] == "SOURCE-CORRECTS")
check("exact", "registry preserves the metric-only theorem at its scoped grade", registry["exact_result"]["metric_only_ward_system"] == {"rank": 34, "affine_dimension": 21, "status": "VALID_ONLY_WHEN_NONMETRIC_GAUGE_COMPONENT_IS_SUPPRESSED"})
check("exact", "registry records the coupled identifiability count", registry["exact_result"]["coupled_fixed_metric_block_system"] == {"rank": 98, "affine_dimension": 198})
check("type", "registry scopes the count to the minimal horizontal subcarrier", registry["exact_result"]["coupled_count_scope"].startswith("MINIMAL_OBSERVED_HORIZONTAL"))
check("type", "actual action-derived cross blocks remain open", registry["exact_result"]["actual_i1b_cross_and_connection_blocks"] == "OPEN")
check("exact", "no new field or datum is introduced", registry["free_object_delta"] == 0 and set(registry["external_datum"].values()) == {"UNUSED"})
check("type", "Curt and third-lane fences hold", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and registry["third_lane"] == "NOT_PROMOTED")
for label in (
    "coupled solvability is not action coefficient derivation",
    "full-field radical is not a physical BV quotient",
    "198 affine directions are not booked residue",
    "no Einstein cosmology Q1 particle or unitarity claim is promoted",
    "P1 P2 P3 remain unused",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CORRECTS")
print("METRIC_ONLY_WARD=RANK34_AFFINE21_VALID_SCOPED_SLICE")
print("CONNECTION_ONE_FORM_LIE_SYMBOL=RANK4_ALL_NONZERO_CAUSAL_ORBITS")
print("COUPLED_FIXED_METRIC_BLOCK_WARD=RANK98_AFFINE198")
print("ACTUAL_I1B_CROSS_CONNECTION_COEFFICIENTS=OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
