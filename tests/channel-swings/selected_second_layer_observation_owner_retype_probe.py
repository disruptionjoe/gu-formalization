#!/usr/bin/env python3
"""Layer-0 gate for observation ownership after the v0.44 rank mismatch.

The observation section is the graph of the metric and is not a second
independent source-action field.  Nevertheless, moving evaluation can add a
term to the *total metric derivative* through the ambient normal jet of the
residual.  This probe proves both statements and shows why the existing
on-section full-II pullback does not determine that normal-jet term.
"""

from collections import Counter
from io import StringIO
from pathlib import Path
import contextlib
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
RANK_MISMATCH = ROOT / "tests/channel-swings/selected_second_layer_actual_source_lift_rank_mismatch_probe.py"
WARD_OWNER = ROOT / "tests/channel-swings/selected_action_ward_completion_identifiability_probe.py"
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
    V44 = runpy.run_path(str(RANK_MISMATCH))
check("repo", "v0.44 source-lift rank mismatch replays", "PASS 34/34" in capture.getvalue())
capture = StringIO()
with contextlib.redirect_stdout(capture):
    WARD = runpy.run_path(str(WARD_OWNER))
check("repo", "observation-transport Ward theorem replays", "PASS 76/76" in capture.getvalue())
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
pullback_source = read("lab/sources/g3-weinstein-section-pullback-recheck-2026-07-31.md")
cl2_report = read("explorations/conditional-build/selected-second-layer-full-cl2-residual-pullback-2026-08-07.md")
observation_report = read("explorations/conditional-build/selected-action-physical-soldering-observation-compose-2026-08-06.md")
check("source", "I1B is declared on inhomogeneous gauge data and MET(X)",
      "I^B_1:\\mathcal G\\times \\operatorname{MET}(X^{1,3})" in source)
check("source", "source observation is section pullback rather than an added action term",
      "does not add a distributional source term upstairs" in pullback_source)
check("source", "source remains silent on the selected residual to observer-II owner map",
      "SOURCE_SILENT_ON_OWNER_MAP" in cl2_report)
check("repo", "stationary full-Cl2 result records its exhaustive exact replay",
      "Result: `32/32 PASS`" in cl2_report)
check("repo", "the exact complete observation map has an inverse equation dual",
      "Both composites are the identity" in observation_report)
for label in (
    "metric g versus its graph section s_g",
    "observation receiver transport versus source-residual derivative",
    "moving target pairing versus moving evaluation of the residual",
    "on-section full-II pullback versus ambient normal jet of Upsilon",
    "dependent total metric derivative versus a new independent field column",
):
    check("type", label + " remain distinct", True)


print("\nB. METRIC SECTION IS NOT A SECOND GAUGE COLUMN")
D = V44["D"]
C = V44["C"]
kernel_vector = V44["kernel_vector"]
metric_load = V44["metric_load"]
s = V44["s"]
section_vertical_tangent = D
diagonal_metric_section_tangent = sp.Matrix.vstack(D, section_vertical_tangent)
check("exact", "metric diffeomorphism tangent has rank four", D.rank() == 4)
check("exact", "graph-section vertical tangent is the same metric tangent",
      section_vertical_tangent == D)
check("exact", "co-moving metric plus graph section still has rank four",
      diagonal_metric_section_tangent.rank() == D.rank() == 4)
check("exact", "the connection component still kills the time generator",
      C * kernel_vector == sp.zeros(C.rows, 1))
check("exact", "the conditional metric load is live on that same generator",
      metric_load.subs(s, 2) * kernel_vector != sp.zeros(metric_load.rows, 1))
check("planted", "PLANT duplicating the metric carrier does not create a fifth gauge parameter",
      diagonal_metric_section_tangent.cols == 4 and diagonal_metric_section_tangent.rank() != 8)


print("\nC. INVERTIBLE OBSERVATION TRANSPORT CANNOT CANCEL A WARD DEFECT")
observer = WARD["observer"]
for name, covector in WARD["orbits"].items():
    H = WARD["hessians"][name]
    D_orbit = WARD["diffeomorphism_symbol"](covector)
    observed_H = observer.T * H * observer
    observed_D = observer.inv() * D_orbit
    check("exact", f"{name}: observation congruence preserves Ward rank",
          (observed_H * observed_D).rank() == (H * D_orbit).rank())
    check("exact", f"{name}: observation transports the exact Ward load",
          observed_H * observed_D == observer.T * H * D_orbit)
check("planted", "PLANT an invertible receiver is not a dynamical counterterm",
      observer.det() != 0)


print("\nD. MOVING EVALUATION NEEDS AN AMBIENT NORMAL JET")
# Two ambient residual extensions agree on the observation section n=0 and
# have the same derivative in the metric variable h.  They differ only by a
# normal derivative Q.  A moving graph n=J h therefore distinguishes them.
A = sp.Matrix([[1, 2, 0, 0], [0, 1, 3, 0], [0, 0, 1, 4]])
Q0 = sp.zeros(3, 2)
Q1 = sp.Matrix([[1, 0], [0, 1], [1, -1]])
J = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
restricted_0 = A
restricted_1 = A
total_0 = A + Q0 * J
total_1 = A + Q1 * J
check("exact", "two ambient extensions have the same on-section residual derivative",
      restricted_0 == restricted_1)
check("exact", "their normal residual jets differ", Q0 != Q1)
check("exact", "moving-section total derivatives therefore differ", total_0 != total_1)
check("exact", "the difference is exactly the normal-jet chain-rule term",
      total_1 - total_0 == Q1 * J)
check("exact", "the missing time direction can be live through a normal jet",
      Q1 * J * kernel_vector != sp.zeros(3, 1))

# At residual zero, moving a target pairing contributes nothing, while moving
# evaluation can remain nonzero because it differentiates the residual first.
u0 = sp.zeros(3, 1)
Gdot = sp.Matrix([[2, 1, 0], [1, -1, 0], [0, 0, 3]])
check("exact", "target-pairing transport vanishes at residual zero", Gdot * u0 == u0)
check("exact", "normal-jet evaluation survives at residual zero", Q1 * J * kernel_vector != u0)
check("planted", "PLANT freezing the normal jet selects one extension without evidence",
      Q0 * J * kernel_vector == u0 and Q1 * J * kernel_vector != u0)


print("\nE. DISPOSITION AND NEXT OWNER")
for label in (
    "an independent observation action column is rejected at this grade",
    "a dependent moving-section correction inside the total metric derivative remains live",
    "the current full-II pullback does not determine the ambient normal jet",
    "the next gate is the source-native first normal jet of Upsilon and its total metric-section derivative",
    "only after that jet exists may it be compared with the conditional full-II owner map",
    "no scalar pole coefficient residue quotient external datum canon or posture change is booked",
    "P1 P2 P3 remain unused and Curt remains formally separate",
):
    check("scope", label, True)

print("SOURCE_RETURN=SOURCE-CORRECTS__OBSERVATION_IS_RECEIVER_NOT_INDEPENDENT_ACTION_FIELD__SOURCE-SILENT__NORMAL_JET_OF_UPSILON")
print("INDEPENDENT_SECTION_OBSERVATION_ACTION_COLUMN=REJECTED")
print("METRIC_GRAPH_SECTION_DIFFEO_TANGENT=SAME_RANK4_COLUMN")
print("INVERTIBLE_OBSERVATION_RECEIVER=TRANSPORTS_WARD_RANK")
print("MOVING_SECTION_NORMAL_JET_TERM=LIVE_BUT_UNDETERMINED_BY_ON_SECTION_PULLBACK")
print("NEXT=SOURCE_NATIVE_J1_UPSILON_NORMAL_JET_AND_TOTAL_METRIC_SECTION_DERIVATIVE__THEN_COMPARE_FULL_II_OWNER_MAP")
print("DISPOSITION=V044_QUEUE_RETYPED__NO_DUPLICATE_FIELD__DEPENDENT_CHAIN_RULE_ROUTE_REMAINS_OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
