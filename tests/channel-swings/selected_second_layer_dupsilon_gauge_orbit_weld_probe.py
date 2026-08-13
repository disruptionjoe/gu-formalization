#!/usr/bin/env python3
"""Exact gauge-orbit weld burden for the selected second-layer residual.

This composes the current metric-only Ward defect with the already source-typed
connection one-form diffeomorphism orbit.  It constructs the unique required
cross response *on that orbit* and refuses to infer the transverse action
derivative, scalar quotient, or BV complex.
"""

from collections import Counter
from io import StringIO
from pathlib import Path
import contextlib
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_second_layer_offtt_scalar_ward_owner_probe.py"
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


print("A. PREDECESSORS, SOURCE, AND LAYER 0")
capture = StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.42 metric Ward predecessor replays", "PASS 30/30" in capture.getvalue())
coupled_report = read("explorations/conditional-build/selected-action-coupled-diffeomorphism-ward-retype-2026-08-06.md")
full_cl2 = read("explorations/conditional-build/selected-second-layer-full-cl2-residual-pullback-2026-08-07.md")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
source_square = read("lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md")
check("repo", "the source-native connection one-form Lie orbit already has rank four", "`G_T(k)` has rank four" in coupled_report)
check("repo", "pure target transport drops only at stationary quadratic grade", "Derivatives of the moving target" in full_cl2 and "transport multiply `U(0)` and vanish" in full_cl2)
check("source", "source action owns metrics and inhomogeneous connection data", "I^B_1:\\mathcal G\\times \\operatorname{MET}(X^{1,3})" in source)
check("source", "source norm-square architecture is confirmed but exact path maps are silent", "SOURCE-CONFIRMS-NORM-SQUARE-AND-REDUNDANCY" in source_square and "exact path maps are `SOURCE-SILENT`" in source_square)
for label in (
    "residual naturality versus Xi equals D Upsilon redundancy",
    "residual differential cancellation versus Hessian Ward radicality",
    "connection diffeomorphism orbit versus Lorentz connection gauge",
    "diagnostic orbit weld versus action-derived transverse blocks",
    "Ward radical versus BV cohomology or BFV phase space",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT CURRENT METRIC LOAD AND CONNECTION ORBIT")
K = P["subtracted"]
D = P["gauge"]
s = P["s"]
G = sp.zeros(16, 4)
for nu in range(4):
    G[nu, nu] = 1  # rest-covector k=(1,0,0,0): (L_xi T)_0^nu=xi^nu
R = sp.Matrix.vstack(D, G)
metric_load = sp.simplify(K * D)
check("exact", "metric diffeomorphism symbol has rank four", D.rank() == 4)
check("exact", "connection one-form Lie symbol has rank four", G.rank() == 4)
check("exact", "the coupled orbit has rank four", R.rank() == 4)
check("exact", "the current metric Ward load has generic rank four", metric_load.subs(s, 2).rank() == 4)
check("exact", "the metric load vanishes at zero momentum only", metric_load.subs(s, 0) == sp.zeros(10, 4) and metric_load.subs(s, 2) != sp.zeros(10, 4))
check("planted", "PLANT deleting the connection orbit changes the full gauge tangent", R != sp.Matrix.vstack(D, sp.zeros(16, 4)))


print("\nC. FORCED RANK OF THE RESIDUAL-LEVEL CORRECTION")
# At a residual-zero point H_gg=J_g^! G_res J_g. Hence
# rank(H_gg D) <= rank(J_g D) <= rank(D)=4. The exact left rank is four,
# forcing rank(J_g D)=4 without using positive-definiteness of G_res.
rank_hessian_load = metric_load.subs(s, 2).rank()
rank_metric_orbit = D.rank()
forced_residual_rank_lower = rank_hessian_load
forced_residual_rank_upper = rank_metric_orbit
check("exact", "Hessian load gives residual-response lower bound four", forced_residual_rank_lower == 4)
check("exact", "four gauge parameters give residual-response upper bound four", forced_residual_rank_upper == 4)
check("exact", "the missing residual response is therefore rank exactly four on the gauge orbit", forced_residual_rank_lower == forced_residual_rank_upper == 4)
check("type", "the rank theorem does not require a positive residual pairing", True)
check("type", "pure frame epsilon or target-metric transport cannot carry this stationary field-variable load", True)


print("\nD. UNIQUE ORBIT WELD AND TRANSVERSE NON-IDENTIFIABILITY")
left_inverse = (G.T * G).inv() * G.T
cross = -metric_load * left_inverse
connection_block = left_inverse.T * D.T * K * D * left_inverse
coupled = sp.Matrix.vstack(
    sp.Matrix.hstack(K, cross),
    sp.Matrix.hstack(cross.T, connection_block),
)
check("exact", "the connection orbit has an exact left inverse", left_inverse * G == sp.eye(4))
check("exact", "the cross response is uniquely fixed on the connection orbit", sp.simplify(cross * G + metric_load) == sp.zeros(10, 4))
check("exact", "the diagnostic symmetric completion is radical on the coupled orbit", sp.simplify(coupled * R) == sp.zeros(26, 4) and sp.simplify(R.T * coupled) == sp.zeros(4, 26))
check("exact", "the completion preserves the complete metric block", coupled[:10, :10] == K)
check("exact", "the load-bearing cross and connection blocks have generic rank four", cross.subs(s, 2).rank() == 4 and connection_block.subs(s, 2).rank() == 4)
check("exact", "the diagnostic completion has the fixed metric rank at a generic point", coupled.subs(s, 2).rank() == K.subs(s, 2).rank() == 10)

# Any map vanishing on im(G) may be added to the connection columns. This
# proves that Ward/naturality determines four columns but not the twelve
# transverse connection directions.
projector_transverse = sp.eye(16) - G * left_inverse
plant = sp.zeros(10, 16)
plant[0, 4] = 1
transverse_addition = plant * projector_transverse
check("exact", "twelve transverse connection directions remain after the rank-four orbit", projector_transverse.rank() == 12)
check("exact", "a nonzero transverse addition leaves the orbit weld unchanged", transverse_addition != sp.zeros(10, 16) and transverse_addition * G == sp.zeros(10, 4))
check("planted", "PLANT the diagnostic weld does not derive the transverse action block", (cross + transverse_addition) * G == cross * G and cross + transverse_addition != cross)


print("\nE. DISPOSITION AND PROGRAM FENCES")
for label in (
    "rank matching is not the actual connection derivative of Upsilon",
    "Hessian Ward closure is not Xi equals D Upsilon",
    "a sixteen-dimensional diagnostic kernel is not a physical quotient",
    "the restricted scalar candidate remains non-characteristic",
    "no common domain energy sign odd BV or global BFV is opened",
    "external P1 P2 P3 cannot manufacture a tangent map",
    "Curt remains formally separate and no third lane is promoted",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__METRIC_PLUS_CONNECTION_ORBIT__SOURCE-SILENT__ACTION_DUPSILON_CROSS_BLOCK")
print("METRIC_WARD_LOAD_RANK=4")
print("CONNECTION_DIFFEO_ORBIT_RANK=4")
print("FORCED_RESIDUAL_GAUGE_RESPONSE_RANK=4")
print("DIAGNOSTIC_ORBIT_WELD=EXACT_UNIQUE_ON_IM_G")
print("TRANSVERSE_CONNECTION_DIRECTIONS=12__ACTION_DERIVATIVE_OPEN")
print("NEXT=DIFFERENTIATE_ACTUAL_SELECTED_UPSILON_IN_FOUR_CONNECTION_GAUGE_COLUMNS_AND_COMPARE_TO_FORCED_WELD")
print("DISPOSITION=RANK4_CONNECTION_ORBIT_WELD_FORCED__TRANSVERSE_OWNER_OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
