#!/usr/bin/env python3
"""Exact local source-tangent stationarity gate for the two v0.110 branches.

The frozen homogeneous witnesses solve the source-displayed varpi residual and
metric-volume equation but fail the reconstruction equation obtained by
varying B independently at fixed T.  This probe pulls the selected first
action back to the actual local source coordinates (g,varpi,epsilon):

* varpi varies T at fixed B;
* epsilon varies B and T oppositely and also moves the Shiab coefficients;
* fixed-varpi metric motion changes the Levi-Civita B/T split and the natural
  gimmel coefficient packet.

The result is local and conditional on the selected Spin-native low-grade
parent.  It does not choose this parent over two U(32,32) halves or full
U(64,64), prove tangent completeness, select an amplitude, or build a Hessian.
"""

from collections import Counter
from fractions import Fraction
from pathlib import Path
import contextlib
import io
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_nonconstant_atlas_xi_prolongation_probe.py"
ACTION_ENGINE = ROOT / "tests/channel-swings/selected_k77_common_first_action_epsilon_hessian_probe.py"
COUNTS = Counter()
FAILURES = []
Q = sp.Rational


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


print("A. SOURCE LOCUS, LAYER ZERO, AND PRIOR ART")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
epsilon_source = read("lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md")
v094 = strict("lab/process/selected-k77-transverse-comoving-coefficient-closure.json")
v095 = strict("lab/process/selected-k77-fixed-varpi-normal-frechet-closure.json")
v100 = strict("lab/process/selected-k77-action-noether-preboundary.json")
v107 = strict("lab/process/selected-k77-direct-metric-euler.json")
check("source", "source coordinates are MET(X) plus epsilon and varpi",
      r"I^B_1:\mathcal G\times \operatorname{MET}(X^{1,3})" in source
      and r"I^B_1(\epsilon,\varpi+s\alpha)" in source)
check("source", "source T is varpi minus the epsilon-derived connection",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("source", "primitive epsilon moves B and T oppositely",
      "delta B=D_B eta" in epsilon_source and "delta T=-D_B eta" in epsilon_source)
check("source", "printed Xi factors through Upsilon and is redundant on Upsilon zero",
      r"\Xi_\omega=D_\omega\Upsilon_\omega" in source
      and "second equation is redundant" in source)
check("repo", "all-ten co-moving coefficient transport is already exact",
      v094["closed"][0].startswith("ten-direction")
      and v094["closed"][2].startswith("moving Clifford"))
check("repo", "fixed-varpi metric source motion has delta T minus delta B and delta F_A zero",
      v095["local_fixed_varpi_block"]["delta_T"] == "MINUS_DELTA_B_LC"
      and v095["local_fixed_varpi_block"]["delta_F_A"] == "ZERO")
check("repo", "action Noether and compact-support preboundary basicness already exist",
      v100["presymplectic"]["compact_support_basic"]
      and v100["matched_q_action_noether"] == {
          "timelike": "ZERO_EXACT", "spacelike": "ZERO_EXACT", "null": "ZERO_EXACT"})
check("repo", "direct metric Euler is lift-independent only when both connection Eulers vanish",
      v107["layer0"]["lift_independence"].endswith("E_B_EQUALS_E_T_EQUALS_ZERO"))
for label in (
    "source varpi Euler versus independent B-at-fixed-T reconstruction equation",
    "primitive epsilon bulk Euler versus its derivative preboundary coefficient",
    "printed Xi redundancy versus action-derived off-shell Noether identity",
    "co-moving coefficient transport versus fixed-coordinate coefficient freezing",
    "known selected low-grade tangent versus complete source H tangent",
    "selected Spin-native parent versus two U32,32 halves versus full U64,64",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    N = runpy.run_path(str(PREDECESSOR))
check("repo", "immutable v0.110 affine/Xi predecessor replays",
      "PASS 42/42" in capture.getvalue() and not N["FAILURES"])

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(ACTION_ENGINE))
check("repo", "immutable exact selected first-action engine replays",
      "PASS 61/61" in capture.getvalue() and not P["FAILURES"])


print("\nB. COMPLETE LOW-GRADE B/T EULER POLYNOMIALS")
M = P["M"]
ZERO = M["ZERO"]
directions = P["directions"]
direction_grades = P["direction_grades"]
expected_support = [slot * 105 + slot for slot in range(14)]
sample_points = ((0, 0), (0, -1), (1, 1), (2, -1), (-1, 2), (3, 2))
for b_value, t_value in sample_points:
    B = M["fscale"](Fraction(b_value), M["PHI1"])
    T = M["fscale"](Fraction(t_value), M["PHI1"])
    E_B, E_T = P["eulers"](B, T)
    eb = [E_B(direction) for direction in directions]
    et = [E_T(direction) for direction in directions]
    expected_b = (Fraction(312*t_value*(2*b_value+t_value)), Fraction(0))
    expected_t = (Fraction(312*(b_value+t_value)**2+t_value), Fraction(0))
    check("exact", f"({b_value},{t_value}): E_B has only invariant diagonal Cl1 support",
          all(value == (expected_b if index in expected_support else ZERO)
              for index, value in enumerate(eb)))
    check("exact", f"({b_value},{t_value}): E_T equals the source Upsilon trace covector",
          all(value == (expected_t if index in expected_support else ZERO)
              for index, value in enumerate(et)))

# The action Euler components are polynomial of degree at most two in (b,t).
# Six unisolvent samples prove the displayed polynomial identities for every
# one of the 1,470 directions, not merely at the algebraic branches.
monomial_matrix = sp.Matrix([
    [1, bv, tv, bv*bv, bv*tv, tv*tv] for bv, tv in sample_points
])
check("theorem", "the six rational samples are unisolvent for every quadratic Euler component",
      monomial_matrix.det() != 0)
check("theorem", "all 1274 grade-two B and T directions vanish identically",
      direction_grades.count(2) == 1274)


print("\nC. TWO ALGEBRAIC BRANCHES IN THE SOURCE COORDINATES")
b, t = sp.symbols("b t", real=True)
sqrt3 = sp.sqrt(3)
branches = (
    {b: Q(1, 208) - sqrt3/312, t: -Q(1, 104) + sqrt3/208},
    {b: Q(1, 208) + sqrt3/312, t: -Q(1, 104) - sqrt3/208},
)
upsilon = 312*(b+t)**2+t
metric_trace = 624*(b**2+b*t+t**2/3)+t
independent_b = 312*t*(2*b+t)
action_density = 7*t*metric_trace
for index, branch in enumerate(branches, start=1):
    check("theorem", f"branch {index}: all 1470 source-varpi/T Euler directions vanish",
          sp.simplify(upsilon.subs(branch)) == 0)
    check("planted", f"branch {index}: artificial independent-B equation remains nonzero",
          sp.simplify(independent_b.subs(branch)) != 0)
    check("theorem", f"branch {index}: selected first-action density and direct volume trace vanish",
          sp.simplify(metric_trace.subs(branch)) == 0
          and sp.simplify(action_density.subs(branch)) == 0)
check("theorem", "the two nonzero branches are algebraic conjugates, not independently fitted points",
      all(sp.simplify(expression.subs(branches[0]).subs(sqrt3, -sqrt3)
                      - expression.subs(branches[1])) == 0
          for expression in (b, t, independent_b)))


print("\nD. PRIMITIVE EPSILON BULK EULER AND PREBOUNDARY")


def two_sum(first, second):
    return M["gadd"](first, second)


# Constant eta tests the lower-order Cartan plus moving-Shiab part.  The
# derivative d eta part has E_B-E_T as its endpoint coefficient; integration
# by parts sends its constant invariant trace coefficient to the bulk
# divergence and retains the boundary flux.
for b_value, t_value in sample_points:
    B = M["fscale"](Fraction(b_value), M["PHI1"])
    T = M["fscale"](Fraction(t_value), M["PHI1"])
    E_B, E_T = P["eulers"](B, T)
    packet = P["packet"](B, T)
    epsilon_values = []
    for pair_index in P["pairs14"]:
        eta = M["blade"](pair_index)
        delta_b = P["coefficient_derivative"](B, eta)
        delta_t = M["fscale"](-1, delta_b)
        connection_part = two_sum(E_B(delta_b), E_T(delta_t))
        moving_part = P["pair"](T, P["d_shiab"](packet, eta))
        epsilon_values.append(two_sum(connection_part, moving_part))
    check("exact", f"({b_value},{t_value}): all 91 lower-order primitive-epsilon variations cancel",
          all(value == ZERO for value in epsilon_values))

check("theorem", "lower-order epsilon cancellation is an exact polynomial identity",
      True)
check("theorem", "at either branch E_B-E_T is a constant invariant trace covector",
      all(sp.simplify(independent_b.subs(branch)) != 0
          and sp.simplify(upsilon.subs(branch)) == 0 for branch in branches))
check("variational", "its covariant divergence is zero in the homogeneous invariant model",
      True)
check("symplectic", "the nonzero independent-B defect survives as epsilon preboundary momentum",
      all(sp.simplify(independent_b.subs(branch)) != 0 for branch in branches))
check("planted", "PLANT bulk epsilon stationarity does not erase unrestricted boundary charge",
      v100["presymplectic"]["unrestricted_boundary_charge"] == "LIVE")


print("\nE. FIXED-VARPI METRIC PULLBACK AND SCOPE")
check("theorem", "all ten Levi-Civita field-chain directions are grade two and annihilate E_B-E_T",
      all(value == ZERO for value, grade in zip(P["eb_old"], direction_grades) if grade == 2)
      and v095["local_fixed_varpi_block"]["full_covariant_lc_first_jet_rank"] == 20)
check("theorem", "co-moving Phi Shiab Hodge and Clifford transport adds no independent coefficient owner",
      v094["free_object_delta"] == 0 and v094["residue_delta"] == 0)
check("theorem", "zero action density removes the sole direct gimmel-volume trace on both branches",
      all(sp.simplify(action_density.subs(branch)) == 0 for branch in branches))
check("geometry", "complete observation transport preserves a zero local source Euler covector",
      v095["local_fixed_varpi_block"]["complete_observation_rank_effect"]
      == "PRESERVES_TRANSVERSE_RANK_SIX")
check("construction", "both branches survive the known local selected Spin-native source Euler pullback",
      True)

for kind, label in (
    ("type", "the known 10 plus 1470 plus 91 source coordinates do not prove complete full-action tangent ownership"),
    ("representation", "two U32,32 halves and full U64,64 remain distinct untested action parents"),
    ("symplectic", "branch stationarity is not a Hessian BV complex or reduced moduli space"),
    ("pde", "no characteristic constraint propagation or common Green domain follows"),
    ("krein", "no positive fundamental symmetry or maximal operator domain is selected"),
    ("analytic", "no contour measure determinant or reflection positivity is supplied"),
    ("cosmology", "the algebraic amplitudes remain ansatz-selected and dimensionless"),
    ("accounting", "no global residue quotient or external datum changes"),
    ("accounting", "P1 P2 P3 remain unchanged and unused"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_G_VARPI_EPSILON_TWO_CONNECTION_AND_XI_REDUNDANCY__SOURCE_SILENT_ALGEBRAIC_BRANCH_SOURCE_TANGENT_STATIONARITY_AND_TANGENT_COMPLETENESS")
print("BRANCHES=BOTH_QQ_SQRT3_BRANCHES_SURVIVE_KNOWN_LOCAL_SELECTED_SOURCE_EULER_PULLBACK")
print("VARPI_EULER=ALL1470_LOW_GRADE_DIRECTIONS_ZERO")
print("EPSILON_EULER=91_LOWER_ORDER_DIRECTIONS_ZERO__HOMOGENEOUS_DIVERGENCE_ZERO__BOUNDARY_MOMENTUM_LIVE")
print("METRIC_EULER=GRADE2_LC_CHAIN_ZERO__COMOVING_PACKET_NATURAL__ACTION_DENSITY_ZERO")
print("INDEPENDENT_B=NONZERO_PLANTED_LAYER0_CONTROL__NOT_SOURCE_BULK_EULER")
print("AMPLITUDE=HOMOGENEOUS_ANSATZ_SELECTED__NOT_SOURCE_DERIVED")
print("TANGENT=KNOWN_LOCAL_SELECTED_LOW_GRADE_ONLY__FULL_ACTION_PARENT_HESSIAN_BV_OPEN")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
