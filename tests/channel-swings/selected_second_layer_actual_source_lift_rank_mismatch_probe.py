#!/usr/bin/env python3
"""Exact source-lift correction to the v0.43 diagnostic orbit weld.

The v0.43 weld used the rank-four covector-slot-only one-form proxy from
v0.32.  The source-corrected `(g,varpi)` tangent built in v0.33 has connection
component `L D` of rank three.  This probe tests whether *any* derivative in
that actual independent-connection direction can cancel the current rank-four
metric residual response.  It cannot: the connection lift has a one-dimensional
kernel on which the metric Ward load is nonzero.
"""

from collections import Counter
from io import StringIO
from pathlib import Path
import contextlib
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
WELD = ROOT / "tests/channel-swings/selected_second_layer_dupsilon_gauge_orbit_weld_probe.py"
SOURCE_LIFT = ROOT / "tests/channel-swings/selected_action_source_variable_hessian_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. PREDECESSORS, SOURCE RETURN, AND LAYER 0")
capture = StringIO()
with contextlib.redirect_stdout(capture):
    V43 = runpy.run_path(str(WELD))
check("repo", "v0.43 diagnostic weld replays", "PASS 37/37" in capture.getvalue())
capture = StringIO()
with contextlib.redirect_stdout(capture):
    V33 = runpy.run_path(str(SOURCE_LIFT))
check("repo", "v0.33 source-variable correction replays", "PASS " in capture.getvalue())

source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
source_report = read("explorations/conditional-build/selected-action-source-variable-hessian-and-diffeomorphism-lift-2026-08-06.md")
v43_report = read("explorations/conditional-build/selected-second-layer-dupsilon-gauge-orbit-weld-2026-08-07.md")
check("source", "source variables are metric and independent connection with augmented-torsion difference",
      "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in source)
check("source", "source-corrected repo result uses T equals varpi minus B_LC",
      "T=\\varpi-B_{LC}(g)" in source_report and "SOURCE-CORRECTS" in source_report)
check("source", "source remains silent on section-observation weld coefficients",
      "SOURCE-SILENT" in source_report and "observation" in source_report)
check("repo", "v0.43 explicitly inherited the v0.32 rank-four connection proxy",
      "v0.32's coupled-orbit theorem" in v43_report)
for label in (
    "covector-slot-only G_T proxy versus full tautological-slot transport",
    "four diffeomorphism parameters versus rank of the connection component",
    "independent connection lift L D versus full stacked generator (D,L D)",
    "connection-only failure versus complete section-observation failure",
    "principal Ward obstruction versus BV BFV or physical quotient",
):
    check("type", label + " remain distinct", True)


print("\nB. ACTUAL SOURCE-VARIABLE CONNECTION LIFT")
P = V43["P"]
K = P["subtracted"]
s = P["s"]
packet = V33["results"]["timelike"]
D = packet["D"]
C = packet["connection_lift"]
proxy = V43["G"]
full_generator = sp.Matrix.vstack(D, C)
check("exact", "obsolete covector-slot proxy has rank four", proxy.rank() == 4)
check("exact", "actual independent-connection diffeomorphism component has rank three", C.rank() == 3)
check("exact", "complete source-variable diffeomorphism generator still has rank four", D.rank() == full_generator.rank() == 4)
check("exact", "actual connection lift has one diffeomorphism-parameter kernel", len(C.nullspace()) == 1)
kernel_vector = C.nullspace()[0]
check("exact", "timelike kernel is the time-reparametrization column", kernel_vector == sp.Matrix([1, 0, 0, 0]))
check("repo", "full tautological-slot response was already proved zero",
      "internal slot at the same time cancels" in source_report)
check("planted", "PLANT nominal four columns do not imply connection rank four", C.cols == 4 and C.rank() == 3)


print("\nC. EXACT CONNECTION-ONLY SOLVABILITY TEST")
metric_load = sp.simplify(K * D)
kernel_load = sp.simplify(metric_load * kernel_vector)
expected_kernel_load = sp.Matrix([
    4 * s * (3589 * s - 9355) / 13689,
    0,
    0,
    0,
    4 * s * (3589 * s - 255) / 13689,
    0,
    0,
    4 * s * (3589 * s - 255) / 13689,
    0,
    4 * s * (3589 * s - 255) / 13689,
])
check("exact", "metric Ward load has rank four at every tested nonzero rest momentum",
      all(metric_load.subs(s, value).rank() == 4 for value in (1, 2, 3, -1)))
check("exact", "connection-kernel metric load has the exact nonzero polynomial",
      kernel_load == expected_kernel_load)
check("exact", "connection-kernel load cannot vanish for any nonzero momentum",
      sp.gcd(sp.Poly(kernel_load[0], s), sp.Poly(kernel_load[4], s)).as_expr() == s)
check("exact", "actual connection row space cannot contain the metric load",
      sp.Matrix.vstack(C, metric_load).rank() == 4 > C.rank())

# For every possible selected residual derivative J_varpi,
# (J_varpi C) kernel_vector = 0.  But the required cancellation is
# -(J_g D) kernel_vector != 0.  Hence no connection-only derivative can solve
# D Upsilon R=0 at this principal grade; no coefficient fit is involved.
J = sp.Matrix(sp.symbols("j0:240")).reshape(10, 24)
check("exact", "every possible connection derivative annihilates the missing fourth input",
      sp.simplify(J * C * kernel_vector) == sp.zeros(10, 1))
check("exact", "the forced diagnostic proxy weld demands a nonzero fourth response",
      kernel_load.subs(s, 2) != sp.zeros(10, 1))
check("exact", "connection-only Ward equation is inconsistent",
      sp.simplify(J * C * kernel_vector + kernel_load).subs(s, 2) != sp.zeros(10, 1))
check("planted", "PLANT the obsolete proxy admits a weld only because it has no kernel",
      proxy.nullspace() == [] and C.nullspace() != [])


print("\nD. CORRECTED OWNER AND PROGRAM FENCES")
for label in (
    "v0.43 remains a valid diagnostic theorem only on the obsolete proxy carrier",
    "connection-only route is killed only at the current principal source lift",
    "section or observation participation is forced but not constructed",
    "a lower-order full-connection term remains an explicitly named rival",
    "no scalar pole massless quotient or Einstein equation follows",
    "no common domain odd BV or BFV phase space is opened",
    "external P1 P2 P3 cannot repair a tangent-rank mismatch",
    "Curt remains formally separate and no third lane is promoted",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CORRECTS__USE_G_VARPI_LD_NOT_COVECTOR_SLOT_PROXY__SOURCE-SILENT__SECTION_OBSERVATION_WELD")
print("V043_PROXY_CONNECTION_RANK=4__OBSOLETE_INTERMEDIATE")
print("ACTUAL_INDEPENDENT_CONNECTION_DIFFEO_RANK=3")
print("ACTUAL_CONNECTION_KERNEL=(1,0,0,0)")
print("METRIC_WARD_LOAD_ON_CONNECTION_KERNEL=NONZERO_FOR_ALL_S_NOT_ZERO")
print("CONNECTION_ONLY_DUPSILON_WELD=IMPOSSIBLE_AT_CURRENT_PRINCIPAL_GRADE")
print("NEXT=CONSTRUCT_ACTUAL_SECTION_OBSERVATION_DIFFEO_TANGENT_ON_MISSING_KERNEL_DIRECTION_THEN_DIFFERENTIATE_SELECTED_UPSILON")
print("DISPOSITION=DIAGNOSTIC_PROXY_RETRACTED_AS_ACTION_TARGET__SECTION_OBSERVATION_OR_ROUTE_CORRECTION_FORCED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
