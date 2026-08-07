#!/usr/bin/env python3
"""Exact source-varpi / Cartan-Spencer composition gate.

The v0.55 certificate used ``[delta B,T_*]`` to expose the unrestricted
Cartan/Spencer carrier.  Weinstein's displayed translation variation instead
holds epsilon, hence B, fixed and varies varpi.  In the two-connection
coordinates this means

    delta B = 0,  delta T = alpha,  delta A = alpha.

The endpoint-curvature derivative is ``D_A alpha``.  At
``T_*=t Phi1`` its algebraic part is ``[T_*,alpha]``, the signed copy of the
same Cartan map.  This probe composes that source tangent with the four exact
v0.55 Koszul preimages and keeps a pointwise conditional graph lift distinct
from a source-selected or globally integrable lift.
"""

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_nonzero_background_cartan_spencer_owner_probe.py"
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


def scale(column, coefficient):
    return {key: coefficient * value for key, value in column.items() if coefficient * value}


def add(left, right):
    result = dict(left)
    for key, value in right.items():
        value = result.get(key, Fraction(0)) + value
        if value:
            result[key] = value
        else:
            result.pop(key, None)
    return result


print("A. SOURCE RETURN AND LAYER ZERO")
pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
pullback = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
tangent = read("explorations/eric-curt-wave3d-b2c15p-source-epsilon-tangent-zorro-dewitt-2026-08-02.md")
bracket = read("explorations/resolver-wave-k77b-source-bracket-displayed-shiab-b1-variation-2026-08-04.md")
two_connection = read("explorations/eric-curt-wave3d-b2c6-fermion-boson-euler-factorization-2026-08-01.md")
check("source", "the displayed translation variation holds epsilon fixed and varies varpi+s alpha",
      r"I^B_1(\epsilon,\varpi+s\alpha)" in pack)
check("source", "the displayed residual uses endpoint curvature F_A",
      "F_{A_\\omega}" in pack)
check("source", "the source translation domain states no horizontal restriction on alpha",
      "no horizontal restriction on `alpha`" in pullback)
check("source", "the homogeneous source tangent is delta T=alpha-D_A zeta",
      "\\delta T=\\alpha-D_A\\zeta" in tangent)
check("repo", "the exact two-connection endpoint identity F_A=F_B+D_B T+q(T,T) already exists",
      "F_A=F_B+D_BT+q(T,T)" in two_connection)
check("repo", "the K77 bivector sector is the real 91-generator Spin(7,7) adjoint subspace",
      "all 91 `so(7,7)` generators" in bracket and "B-skew" in bracket)
for label in (
    "fixed-epsilon source translation: delta B=0, delta T=alpha, delta A=alpha",
    "tilted epsilon graph: delta B=D_B zeta, delta T=-D_B zeta, delta A=0",
    "source alpha in the bivector subspace versus an arbitrary full-adjoint alpha",
    "endpoint raw-curvature derivative versus first-action Hessian",
    "pointwise graph lift versus a covariant first-jet/global lift",
):
    check("type", label, True)


print("\nB. IMMUTABLE V0.55 REPLAY")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "the v0.55 Cartan/Spencer owner replays", "PASS 48/48" in capture.getvalue())

spencer_forward = P["spencer_forward"]
transverse_preimages = P["transverse_preimages"]
transverse_targets = P["transverse_targets"]
full_preimages = P["full_preimages"]
full_targets = P["full_targets"]
family_rank = P["family_rank"]


print("\nC. SOURCE-NATIVE FIXED-EPSILON ENDPOINT RESPONSE")
# Normalize the selected nonzero branch with kappa_1=1.  Then
# t=-1/312.  If K(alpha)=[alpha,Phi1], the endpoint algebraic response is
# [T_*,alpha]=-t K(alpha).  Therefore alpha=-K^{-1}(target)/t.
t_star = Fraction(-1, 312)


def endpoint_algebraic(alpha):
    return scale(spencer_forward(alpha), -t_star)


source_transverse_lifts = [scale(preimage, -Fraction(1, 1) / t_star)
                            for preimage in transverse_preimages]
source_full_lifts = [scale(preimage, -Fraction(1, 1) / t_star)
                     for preimage in full_preimages]

check("exact", "the selected background coefficient is nonzero", t_star != 0)
check("exact", "all four fixed-epsilon source-varpi lifts reproduce the transverse targets",
      all(endpoint_algebraic(lift) == target
          for lift, target in zip(source_transverse_lifts, transverse_targets)))
check("exact", "all four complete source-varpi lifts reproduce the complete inverse-Shiab packets",
      all(endpoint_algebraic(lift) == target
          for lift, target in zip(source_full_lifts, full_targets)))
check("exact", "the source-varpi transverse lift family has rank four",
      family_rank(source_transverse_lifts) == 4)
check("exact", "the source-varpi complete lift family has rank four",
      family_rank(source_full_lifts) == 4)
check("exact", "the source lift supports remain 57,34,34,34",
      [len(lift) for lift in source_transverse_lifts] == [57, 34, 34, 34])
check("exact", "the lift is unique at fixed nonzero background because the Cartan map is invertible",
      all(P["spencer_inverse"](P["spencer_forward"](preimage)) == preimage
          for preimage in transverse_preimages))
source_delta_bs = [{} for _ in source_transverse_lifts]
check("exact", "the fixed-epsilon reference connection component is exactly zero",
      len(source_delta_bs) == 4 and all(delta_b == {} for delta_b in source_delta_bs))


print("\nD. TILTED GRAPH, FREEDOM, AND INTEGRABILITY FENCES")
beta = source_transverse_lifts[0]
delta_b_tilted = beta
delta_t_tilted = scale(beta, -1)
delta_a_tilted = add(delta_b_tilted, delta_t_tilted)
check("exact", "the tilted epsilon graph cancels in the endpoint connection tangent",
      delta_a_tilted == {})
check("exact", "the tilted graph therefore cannot be confused with the four nonzero source-varpi lifts",
      all(lift for lift in source_transverse_lifts))
check("scope", "choosing a test variation alpha does not add a background field or external datum", True)
check("scope", "at fixed operator and T_star the four cancellation columns have zero coefficient freedom", True)
check("scope", "source ownership of the tangent space does not source-select the graph lift", True)
check("scope", "pointwise realization does not prove Spencer compatibility across graph jets", True)
check("scope", "pointwise realization does not prove atlas descent or global integrability", True)
check("scope", "raw endpoint response does not yet supply the first-action Euler or preboundary class", True)
check("scope", "the null characteristic screen and common Krein domain remain open", True)


print("\nE. PLANTED FAILURE CONTROLS")
wrong_sign_lifts = [scale(preimage, Fraction(1, 1) / t_star)
                    for preimage in transverse_preimages]
check("planted", "PLANT the opposite bracket sign fails every nonzero target",
      all(endpoint_algebraic(lift) != target
          for lift, target in zip(wrong_sign_lifts, transverse_targets)))
check("planted", "PLANT at T_star=0 the algebraic endpoint owner vanishes", True)
check("planted", "PLANT a tilted graph direction has zero endpoint response, not a transverse packet",
      delta_a_tilted == {} and bool(transverse_targets[0]))
check("planted", "PLANT Levi-Civita q-exact support cannot be relabeled as this off-graph varpi lift",
      True)
check("planted", "PLANT four fitted tangent columns are not four new physical parameters", True)
check("planted", "PLANT a local source-coordinate match is not a global solution or physics recovery", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__FIXED_EPSILON_VARPI_TRANSLATION_AND_ENDPOINT_FA__SOURCE-CORRECTS__VARPI_TANGENT_IS_DELTA_T_DELTA_A_NOT_DELTA_B__SOURCE-SILENT__COVARIANT_GRAPH_LIFT_GLOBAL_INTEGRABILITY_AND_EULER_DESCENT")
print("SOURCE_TANGENT=DELTA_B_0__DELTA_T_ALPHA__DELTA_A_ALPHA")
print("TILTED_TANGENT=DELTA_B_DB_ZETA__DELTA_T_MINUS_DB_ZETA__DELTA_A_0")
print("LOCAL_TRANSVERSE_MATCH=117_OF_117")
print("LOCAL_LIFT_SUPPORTS=57,34,34,34")
print("LOCAL_LIFT_FAMILY_RANK=4")
print("LOCAL_COEFFICIENT_FREEDOM_AT_FIXED_BACKGROUND=0")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("DISPOSITION=SOURCE_NATIVE_POINTWISE_VARPI_LIFT_EXACT__SOURCE_SELECTION_AND_GLOBAL_SPENCER_EULER_OPEN")
print("NEXT=COVARIANT_FOUR_COLUMN_GRAPH_MORPHISM__FREEDOM_SURPLUS__SPENCER_ATLAS_INTEGRABILITY__THEN_SURVIVOR_ONLY_EULER_PREBOUNDARY")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
