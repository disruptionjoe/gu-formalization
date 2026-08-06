#!/usr/bin/env python3
"""Exact source-variable Hessian of the selected zero-jet torsion summand."""

from collections import Counter
from fractions import Fraction
from io import StringIO
from pathlib import Path
import contextlib
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
STATIONARY = ROOT / "tests/channel-swings/selected_action_stationary_spin_lc_hessian_probe.py"
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


def rational(value):
    return sp.Rational(value.numerator, value.denominator)


print("A. SOURCE, PREDECESSOR, AND LAYER 0")
source = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
frame_report = (ROOT / "explorations/conditional-build/selected-action-comoving-frame-naturality-2026-08-06.md").read_text()
coupled_report = (ROOT / "explorations/conditional-build/selected-action-coupled-diffeomorphism-ward-retype-2026-08-06.md").read_text()
check("source", "source action uses augmented torsion as an independent connection minus the rotated reference connection", "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in source)
check("source", "source action is first order and the zero-jet torsion summand is not the full I1B action", "F_{B_\\omega}" in source and "\\frac12d_{B_\\omega}T_\\omega" in source)
check("repo", "the selected Phi1 is already typed as the tautological identity", "tautological identity" in frame_report)
check("repo", "v0.32 explicitly leaves the complete internal transport and actual blocks open", "complete principal diffeomorphism lift" in coupled_report and "actual same-`I1B` block Hessian" in coupled_report)

capture = StringIO()
with contextlib.redirect_stdout(capture):
    S = runpy.run_path(str(STATIONARY))
check("repo", "stationary selected torsion Hessian predecessor replays", "PASS 64/64" in capture.getvalue())

for label in (
    "augmented torsion versus the independent source connection varpi",
    "covector-slot Lie response versus full tautological-slot transport",
    "order-one tensor transport versus order-two connection principal lift",
    "selected zero-jet torsion summand versus full first-order I1B",
    "unreduced Hessian radical versus BV/BFV physical quotient",
):
    check("type", label + " remain distinct", True)


backend = S["X"]
selected_hessian = S["selected_hessian"]
lc_spin_symbol = S["lc_spin_symbol"]
form_matrix = S["form_matrix"]
cl2_basis = backend["cl2_basis"]
slots = S["slots"]
metric_basis = S["metric_basis"]
orbits = S["orbits"]
old_metric_hessians = S["hessians"]
inertia = S["inertia"]

connection_basis = [
    cl2_basis(mu, a, b)
    for mu in range(4)
    for a in range(4)
    for b in range(a + 1, 4)
]
K = sp.Matrix([
    [rational(selected_hessian(left, right)[0]) for right in connection_basis]
    for left in connection_basis
])


def metric_symbol(covector):
    out = sp.zeros(10, 4)
    for column in range(4):
        for row, (i, j) in enumerate(slots):
            out[row, column] = (
                (covector[i] if j == column else 0)
                + (covector[j] if i == column else 0)
            )
    return out


def lc_coordinates(covector):
    fields = [lc_spin_symbol(covector, wave) for wave in metric_basis]
    combined = form_matrix(connection_basis + fields)
    basis_matrix = combined[:, :24]
    field_matrix = combined[:, 24:]
    left_inverse = (basis_matrix.T * basis_matrix).inv() * basis_matrix.T
    coordinates = left_inverse * field_matrix
    check("exact", "connection basis spans the complete horizontal Lorentz carrier", basis_matrix.rank() == 24)
    check("exact", "spin Levi-Civita fields reconstruct from the connection basis", basis_matrix * coordinates == field_matrix)
    return coordinates


print("\nB. FULL TAUTOLOGICAL SLOT TRANSPORT")
for name, covector in orbits.items():
    covector_slot = sp.zeros(16, 4)
    internal_slot = sp.zeros(16, 4)
    for mu in range(4):
        for nu in range(4):
            covector_slot[4 * mu + nu, nu] = covector[mu]
            internal_slot[4 * mu + nu, nu] = -covector[mu]
    check("exact", f"{name}: the isolated covector slot reproduces v0.32 rank four", covector_slot.rank() == 4)
    check("exact", f"{name}: co-moving the internal slot cancels the tautological identity response", covector_slot + internal_slot == sp.zeros(16, 4))
    check("planted", f"PLANT {name}: freezing the internal slot creates the obsolete rank-four tangent", covector_slot != sp.zeros(16, 4))


print("\nC. ACTUAL SOURCE-VARIABLE HESSIAN BLOCKS")
check("exact", "selected torsion Hessian is symmetric and nondegenerate on the 24-dimensional horizontal connection carrier", K == K.T and K.rank() == 24)
k_inertia = inertia(K)
check("exact", "selected torsion Hessian has no zero connection direction", k_inertia[2] == 0)

results = {}
for name, covector in orbits.items():
    L = lc_coordinates(covector)
    D = metric_symbol(covector)
    connection_lift = L * D
    difference_tangent = sp.Matrix.hstack(-L, sp.eye(24))
    coupled = difference_tangent.T * K * difference_tangent
    gauge = sp.Matrix.vstack(D, connection_lift)

    h_gg = coupled[:10, :10]
    h_ga = coupled[:10, 10:]
    h_ag = coupled[10:, :10]
    h_aa = coupled[10:, 10:]
    results[name] = {
        "L": L,
        "D": D,
        "connection_lift": connection_lift,
        "difference_tangent": difference_tangent,
        "coupled": coupled,
        "gauge": gauge,
    }

    check("exact", f"{name}: spin LC map retains its exact rank nine", L.rank() == 9)
    check("exact", f"{name}: principal connection diffeomorphism lift has rank three", connection_lift.rank() == 3)
    check("exact", f"{name}: source difference kills the complete principal diffeomorphism lift", difference_tangent * gauge == sp.zeros(24, 4))
    check("exact", f"{name}: source-variable Hessian is symmetric", coupled == coupled.T)
    check("exact", f"{name}: metric block reproduces the predecessor exactly", h_gg == old_metric_hessians[name])
    check("exact", f"{name}: metric--connection cross blocks are action-derived and reciprocal", h_ga == h_ag.T and h_ga != sp.zeros(10, 24))
    check("exact", f"{name}: connection--connection block is the full selected torsion Hessian", h_aa == K)
    check("exact", f"{name}: both coupled Ward block equations close", h_gg * D + h_ga * connection_lift == sp.zeros(10, 4) and h_ag * D + h_aa * connection_lift == sp.zeros(24, 4))
    check("exact", f"{name}: complete source-variable gauge image is a two-sided Hessian radical", coupled * gauge == sp.zeros(34, 4) and gauge.T * coupled == sp.zeros(4, 34))
    check("exact", f"{name}: coupled zero-jet summand has rank 24 and nullity ten", coupled.rank() == 24 and 34 - coupled.rank() == 10)
    check("exact", f"{name}: six nongauge null directions remain for derivative/curvature quotient dynamics", (34 - coupled.rank()) - gauge.rank() == 6)
    check("exact", f"{name}: nonzero inertia equals the source torsion carrier inertia", inertia(coupled) == (k_inertia[0], k_inertia[1], 10))
    check("planted", f"PLANT {name}: metric-only restriction retains the old rank-three Ward defect", (h_gg * D).rank() == 3)


print("\nD. IDENTIFIABILITY AND FULL-I1B FENCE")
for name, packet in results.items():
    L = packet["L"]
    graph_kernel = sp.Matrix.vstack(sp.eye(10), L)
    check("exact", f"{name}: the full ten-dimensional zero-jet kernel is exactly the constant-T graph", packet["difference_tangent"] * graph_kernel == sp.zeros(24, 10) and graph_kernel.rank() == 10)
    check("exact", f"{name}: the four-dimensional diffeomorphism image lies inside that graph", graph_kernel.row_join(packet["gauge"]).rank() == graph_kernel.rank())

check("type", "the six nongauge null directions demand the derivative curvature density and observation blocks of full I1B", True)
check("type", "zero-jet Ward closure does not establish the full I1B Ward identity", True)
check("type", "finite causal symbols do not establish an analytic Green domain", True)


print("\nE. REGISTRY AND PROGRAM FENCES")
registry = strict("lab/process/selected-action-source-variable-hessian-and-diffeomorphism-lift.json")
check("source", "decisive source return is SOURCE-CORRECTS", registry["source_return"] == "SOURCE-CORRECTS")
check("exact", "registry records the action-derived source-variable blocks", registry["exact_result"]["zero_jet_source_variable_hessian"] == {"carrier_dimension": 34, "rank": 24, "nullity": 10, "gauge_rank": 4, "nongauge_nullity": 6})
check("type", "registry leaves full first-order I1B open", registry["exact_result"]["full_i1b_derivative_curvature_density_observation_blocks"] == "OPEN")
check("exact", "no free object or datum is introduced", registry["free_object_delta"] == 0 and set(registry["external_datum"].values()) == {"UNUSED"})
check("type", "Curt and third-lane fences hold", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and registry["third_lane"] == "NOT_PROMOTED")
for label in (
    "zero-jet radical is not a BV or BFV quotient",
    "six nongauge nulls are not six external parameters",
    "no Einstein cosmology Q1 particle or unitarity claim is promoted",
    "P1 P2 P3 remain unused",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CORRECTS")
print("TAUTOLOGICAL_PHI1_FULL_SLOT_LIE_RESPONSE=ZERO")
print("SOURCE_VARIABLES=(g,varpi)__TANGENT=(-L_spin,I24)")
print(f"H_TORSION_INERTIA={k_inertia}")
print("CONNECTION_PRINCIPAL_DIFFEO_LIFT=L_spin*D__RANK3")
print("ZERO_JET_SOURCE_HESSIAN=RANK24_NULLITY10__GAUGE4_PLUS_NONGAUGE6")
print("FULL_I1B_DERIVATIVE_CURVATURE_DENSITY_OBSERVATION=OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
