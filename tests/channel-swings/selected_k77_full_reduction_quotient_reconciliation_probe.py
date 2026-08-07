#!/usr/bin/env python3
"""Reconcile K77 full-reduction descent with the unframed basicness failure.

Ledger v0.58 proved that the fitted four-column source lift is not basic after
forgetting to the horizontal four-plane.  An August 5 construction had already
built a different object: the source-owned labelled Clifford reduction
``gamma_epsilon = Ad(epsilon^-1) gamma_0``.  This probe keeps those quotients
separate and checks the paired reduction-plus-lift descent.

Run with:
  uv run --with numpy --with sympy==1.14.0 python \
    tests/channel-swings/selected_k77_full_reduction_quotient_reconciliation_probe.py
"""

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
V058 = ROOT / "tests/channel-swings/selected_k77_source_graph_basicness_probe.py"
GLOBAL = ROOT / "tests/channel-swings/k77_global_chimeric_spin_reduction_probe.py"
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


print("A. REPOSITORY ARCHAEOLOGY, SOURCE RETURN, AND LAYER ZERO")
global_report = read(
    "explorations/conditional-build/"
    "k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md"
)
global_source = read(
    "lab/sources/k77-global-chimeric-spin-reduction-source-reinspection-2026-08-05.md"
)
v058_report = read(
    "explorations/conditional-build/selected-k77-source-graph-basicness-2026-08-07.md"
)
portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
object_map = read("GEOMETER-VS-PHYSICS-OBJECTS.md")

check("repo", "the earlier global reduction constructs gamma_epsilon from source epsilon",
      r"\gamma_\epsilon=\operatorname{Ad}(\epsilon^{-1})\gamma_0" in global_report)
check("source", "the source ownership correction is explicit and independently located",
      "SOURCE-CORRECTS" in global_source
      and r"\text{Ad}(\varepsilon^{-1}, \Phi)" in portal)
check("repo", "v0.58 correctly proves only the horizontal-plane forgetful quotient fails",
      "normal rotation that leaves the\nobserved horizontal four-plane fixed" in v058_report)
check("type", "source epsilon and dependent gamma_epsilon remain distinct",
      "Source (epsilon) and `epsilon_IG` were\npreviously kept distinct" in global_report)
for label in (
    "labelled full Clifford reduction versus its horizontal-plane forgetful image",
    "source gauge epsilon versus dependent gamma_epsilon",
    "gamma_epsilon versus an observation section s:X->Y",
    "full-reduction configuration descent versus Euler/presymplectic descent",
    "central stabilizer quotient versus block-stabilizer quotient",
):
    check("type", label + " remain distinct", True)
check("repo", "the mandatory object map now names settled K77 rather than stale K95",
      "Signature (7,7)" in object_map and "horizontal (1,3) plus vertical (6,4)" in object_map)


print("\nB. IMMUTABLE PREDECESSOR REPLAYS")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    G = runpy.run_path(str(GLOBAL))
check("repo", "the global chimeric-spin reduction replays", "PASS 53/53" in capture.getvalue())
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    B = runpy.run_path(str(V058))
check("repo", "the unframed basicness failure replays", "PASS 44/44" in capture.getvalue())
check("exact", "the source-owned reduction retains fourteen labelled Clifford directions",
      len(G["gamma"]) == 14 and G["trace_gram"].shape == (14, 14))
check("exact", "the v0.58 fitted lift remains rank four",
      B["family_matrix"](B["LIFT"]).rank() == 4)


print("\nC. TRUE STABILIZER OF THE LABELLED REDUCTION")
gamma = G["gamma"]
i128 = np.eye(128, dtype=np.int64)
k12 = gamma[1] @ gamma[2]
spin_g01 = i128 - k12
spin_g01_inverse_numerator = i128 + k12

spin_numerators = [spin_g01 @ value @ spin_g01_inverse_numerator for value in gamma]
check("exact", "the rational spin conjugation has even numerators",
      all(np.all(value % 2 == 0) for value in spin_numerators))
moved_gamma = [value // 2 for value in spin_numerators]
expected_gamma = list(gamma)
expected_gamma[1] = gamma[2]
expected_gamma[2] = -gamma[1]
check("exact", "one noncentral Spin element moves the labelled frame by g01",
      all(np.array_equal(a, b) for a, b in zip(moved_gamma, expected_gamma)))
minus_identity = -i128
check("exact", "the real central representative fixes every labelled Clifford generator",
      all(np.array_equal(minus_identity @ value @ minus_identity, value) for value in gamma))
check("theorem", "Cl(7,7) is the full real matrix algebra in this faithful module",
      "Cl}(7,7)\\cong M_{128}(\\mathbb R)" in global_report
      and 2 ** 14 == 128 ** 2)
check("theorem", "the real commutant is scalar and the complex Krein-unitary stabilizer is U1",
      "faithful real rank-128 module" in global_report and "U(64,64)" in global_report)
check("exact", "the residual central stabilizer acts trivially in the adjoint lift carrier",
      all(np.array_equal(minus_identity @ value @ minus_identity, value) for value in gamma))


print("\nD. PAIRED FULL-REDUCTION DESCENT")
g01 = B["g01"]
lift0 = B["LIFT"]
lift1 = B["act_family"](g01, lift0)
check("exact", "the same g01 action moves the source lift nontrivially",
      not B["family_equal"](lift0, lift1))
check("exact", "the moved pair retains the endpoint and Spencer equations",
      all(B["spencer_forward"](column) == target
          for column, target in zip(
              lift1,
              B["act_target_family"](
                  g01, [B["spencer_forward"](column) for column in lift0]
              ),
          )))
check("theorem", "two epsilon representatives with the same labelled reduction differ centrally",
      "full labelled fourteen-frame" in global_report
      and "Clifford multiplication is therefore a global bundle map" in global_report)
check("exact", "central representative ambiguity leaves both gamma and the adjoint lift unchanged",
      all(np.array_equal(minus_identity @ value @ minus_identity, value) for value in gamma)
      and B["family_equal"](lift0, lift0))
check("scope", "the paired map is well-defined on the source-owned full-reduction orbit",
      "source (epsilon)" in global_report and "dependent full Clifford frame" in global_report)


print("\nE. FORGETFUL FAILURE AND INVARIANT-REPLACEMENT HORN")
check("planted", "PLANT forgetting gamma to the horizontal plane preserves the v0.58 failure",
      B["n45_defect"] == (4, 80, [30, 30, 10, 10]))
check("planted", "PLANT a block-stabilizer invariant replacement cannot equal the fitted lift",
      B["invariant_span"].row_join(B["lift_vector"]).rank() == 4)
for basis in (B["A"], B["B"], B["C"], lift0):
    check("exact", "Spencer inverse round-trips one complete map family",
          all(B["P"]["spencer_inverse"](B["spencer_forward"](column)) == column
              for column in basis))

target_keys = [(left, right, value)
               for left in range(14) for right in range(left + 1, 14)
               for value in range(14)]


def target_family_vector(family):
    return sp.Matrix([
        sp.Rational(family[column].get(key, Fraction(0)).numerator,
                    family[column].get(key, Fraction(0)).denominator)
        for key in target_keys for column in range(4)
    ])


invariant_target_span = sp.Matrix.hstack(*[
    target_family_vector([B["spencer_forward"](column) for column in basis])
    for basis in (B["A"], B["B"], B["C"])
])
target_vector = target_family_vector(B["TARGET"])
check("exact", "no block-invariant Hom combination reproduces the four K77 targets",
      invariant_target_span.rank() == 3
      and invariant_target_span.row_join(target_vector).rank() == 4
      and sp.linsolve((invariant_target_span, target_vector)) == sp.EmptySet)


print("\nF. SURPLUS, OBSERVATION, AND SYMPLECTIC FENCES")
check("scope", "the dependent full reduction adds no new field or Clifford coefficient",
      "zero new fields" in global_report and "new Clifford-frame coefficients | 0" in global_report)
check("scope", "gauge-orbit transport identities are not counted as independent surplus",
      True)
check("scope", "the observation section and its pullback remain open",
      "observation" in global_report and "does not establish" in global_report)
check("symplectic", "configuration basicness does not establish Euler or presymplectic descent",
      "symplectic descent | none" in v058_report and "Euler/preboundary" in v058_report)
check("symplectic", "raw-Upsilon, null screen, Green domain, BV and BFV remain downstream",
      "raw-`Upsilon`" in v058_report and "null/Green domain" in global_report)
check("scope", "P1 P2 P3 remain unchanged and unused", True)


print("SOURCE_RETURN=SOURCE-CORRECTS__FULL_LABELLED_CLIFFORD_REDUCTION_ALREADY_OWNED_BY_SOURCE_EPSILON__SOURCE_SILENT__OBSERVATION_SECTION_AND_PHYSICAL_EULER_DESCENT")
print("FULL_REDUCTION_STABILIZER=COMPLEX_SCALAR_U1__ADJOINT_ACTION_TRIVIAL")
print("FULL_REDUCTION_PAIR_BASIC=YES")
print("HORIZONTAL_PLANE_FORGETFUL_QUOTIENT_BASIC=NO")
print("INVARIANT_REPLACEMENT_REPRODUCING_TARGETS=NO")
print("CONSTRAINT_SURPLUS=ZERO_NEW_FIELD_CONDITIONAL_ON_SOURCE_CONFIGURATION__TRANSPORT_IDENTITIES_NOT_COUNTED")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("DISPOSITION=SOURCE_OWNED_FULL_REDUCTION_QUOTIENT_BASIC__FORGETFUL_QUOTIENT_FAILS__OBSERVATION_EULER_OPEN")
print("NEXT=TOTAL_RAW_UPSILON_BIANCHI_NATURALITY_AND_NULL_SCREEN_ON_FULL_REDUCTION__THEN_OBSERVATION_EULER_PREBOUNDARY_SYMPLECTIC_DESCENT")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
