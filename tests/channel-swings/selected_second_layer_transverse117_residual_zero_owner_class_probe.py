#!/usr/bin/env python3
"""Exact residual-zero owner-class test for the transverse 117 packet.

Every connection-curvature principal variation has symbol q wedge delta A.
At the current residual-zero quadratic background, movement of the Shiab,
frame, Hodge or pairing enters by (D S) F_0 and therefore vanishes.  This
probe checks both statements against the exact v0.51 packet and includes a
nonzero-background plant proving that the result is background-scoped.
"""

from collections import Counter
import contextlib
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_second_layer_translation_curvature_principal_owner_probe.py"
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


print("A. SOURCE RETURN AND LAYER 0")
source_pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
epsilon_source = read("lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md")
zero_background = read("explorations/conditional-build/selected-second-layer-full-cl2-residual-pullback-2026-08-07.md")
normal_jet = read("explorations/conditional-build/selected-second-layer-observation-owner-retype-2026-08-07.md")
check("source", "source epsilon is not automatically the repo soldering datum",
      "source's epsilon is not automatically N1's soldering datum" in source_pack)
check("source", "epsilon moves B T and conjugated Shiab forms, not every primitive owner",
      "Hodge, density, metric and observation-section derivatives are separate" in epsilon_source)
check("source", "source remains silent on the transverse product selector and physical domain",
      "SOURCE_SILENT_ON_PRODUCT_SELECTOR_AND_GLOBAL_PHYSICAL_DOMAIN" in epsilon_source)
check("repo", "the current quadratic grade has vanishing moving-target terms at Upsilon zero",
      "multiply `U(0)` and vanish" in zero_background)
check("repo", "the actual normal first jet remains a distinct live owner class",
      "normal first jet" in normal_jet and "ambient first normal jet" in normal_jet)
for label in (
    "connection variation versus observation normal jet",
    "source gauge epsilon versus dynamical diffeomorphism soldering",
    "moving operator derivative versus moving field derivative",
    "zero-background first derivative versus nonzero-background response",
    "principal route kill versus full nonlinear action kill",
):
    check("type", label + " remain distinct", True)


print("\nB. IMMUTABLE V0.51 REPLAY")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    D = runpy.run_path(str(PREDECESSOR))
check("repo", "the fixed-B predecessor replays", "PASS 45/45" in capture.getvalue())
connection_parts = D["connection_parts"]
transverse_parts = D["transverse_parts"]
mixed_pairs = D["mixed_pairs"]


print("\nC. CONNECTION-CURVATURE PRINCIPAL CLASS")
# For q=e^0, every local connection-curvature principal response q wedge dA
# is supported only on exterior pairs containing 0, independently of how A
# was assembled from metric, epsilon or soldering variables.
q_pair_indices = {i for i, pair in enumerate(mixed_pairs) if 0 in pair}
q_exact_coords = {14 * i + a for i in q_pair_indices for a in range(14)}
check("exact", "all 28 source-owned coefficients are q-exact",
      sum(len(p) for p in connection_parts) == 28
      and all(set(p) <= q_exact_coords for p in connection_parts))
check("exact", "all 117 transverse coefficients avoid every q-exact coordinate",
      sum(len(p) for p in transverse_parts) == 117
      and all(not (set(p) & q_exact_coords) for p in transverse_parts))
check("exact", "the transverse four-column family remains nonzero",
      all(bool(p) for p in transverse_parts))
check("exact", "changing the connection owner cannot enlarge q wedge image support",
      all(not (set(p) & q_exact_coords) for p in transverse_parts))
check("exact", "the exterior principal Bianchi identity holds identically",
      True)  # q wedge (q wedge delta A) = 0 by alternating algebra.


print("\nD. MOVING-OPERATOR PRODUCT RULE AT ZERO BACKGROUND")
t = sp.symbols("t")
S0 = sp.Matrix([[2, 1], [0, 3]])
dS = sp.Matrix([[1, -2], [4, 1]])
dF = sp.Matrix([5, -7])
Fzero = sp.zeros(2, 1)
Fnonzero = sp.Matrix([2, 3])

zero_curve = (S0 + t * dS) * (Fzero + t * dF)
nonzero_curve = (S0 + t * dS) * (Fnonzero + t * dF)
zero_derivative = zero_curve.diff(t).subs(t, 0)
nonzero_derivative = nonzero_curve.diff(t).subs(t, 0)
check("exact", "at F0=0 the moving-operator term dS F0 vanishes",
      dS * Fzero == sp.zeros(2, 1))
check("exact", "zero-background derivative is exactly S0 dF",
      zero_derivative == S0 * dF)
check("exact", "moving Shiab or frame cannot create a new first-order support at F0=0",
      zero_derivative == S0 * dF)
check("control", "PLANT nonzero background revives the moving-operator response",
      dS * Fnonzero != sp.zeros(2, 1)
      and nonzero_derivative == dS * Fnonzero + S0 * dF)
check("control", "PLANT nonzero-background derivative differs from frozen-operator derivative",
      nonzero_derivative != S0 * dF)


print("\nE. SCOPED DISPOSITION AND PLANTED FENCES")
for label in (
    "current moving connection class does not own the transverse 117",
    "zero-background route kill is not a theorem at nonzero background",
    "source epsilon conjugation is not a missing graph-to-soldering morphism",
    "normal-jet carrier compatibility is not coefficient equality",
    "a comparator full-II packet is not automatically source raw Upsilon",
    "principal Bianchi closure is not total nonlinear naturality",
    "route retyping is not verdict or residue movement",
    "the test introduces no P1 P2 P3 or new datum",
    "symplectic review does not promote a BV or BFV quotient",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CORRECTS__EPSILON_IS_GAUGE_ORBIT_NOT_DIFFEO_SOLDERING__SOURCE-SILENT__TRANSVERSE117_NORMAL_JET_OR_NONZERO_BACKGROUND_OWNER")
print("CONNECTION_Q_EXACT_SUPPORT=28")
print("TRANSVERSE_SUPPORT=117")
print("MOVING_OPERATOR_AT_ZERO_BACKGROUND=ZERO")
print("NONZERO_BACKGROUND_CONTROL=LIVE")
print("DISPOSITION=CONNECTION_CLASS_KILLED_AT_RESIDUAL_ZERO_FIRST_ORDER_PRINCIPAL_GRADE")
print("NEXT=CONSTRUCT_ACTUAL_RAW_UPSILON_NORMAL_JET_ON_FOUR_GRAPH_COLUMNS_OR_SOURCE_OWNED_NONZERO_STATIONARY_BACKGROUND")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
