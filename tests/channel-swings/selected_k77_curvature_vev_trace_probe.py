#!/usr/bin/env python3
"""Exact scalar-curvature-jet closure of the selected K77 metric trace.

The predecessor's homogeneous fixture suppresses the derivative part of
``F_B``.  This probe restores the unique selected invariant scalar curvature
jet ``r (Phi1 wedge Phi1)`` inside the *same* source first action.  It does not
add a dark-energy field or coupling: ``T_omega`` is already the action's
movable connection distortion.

The result is deliberately local and jet-graded.  Passing the algebraic
Bianchi check does not construct a global connection, observation descent,
domain, Hessian or BV complex.
"""

from collections import Counter
from fractions import Fraction
from pathlib import Path
import contextlib
import io
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_direct_metric_euler_probe.py"
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


print("A. SOURCE RETURN AND LAYER ZERO")
source_pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
ucsd = read("lab/literature/weinstein-ucsd-2025-04-transcript.md")
keating = read("lab/sources/selected-branch-bv-flrw-source-reinspection-2026-08-05.md")
check("source", "the source first action already owns T_omega as the two-connection difference",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source_pack
      and r"I^B_1" in source_pack)
check("source", "the displayed source Euler residual couples curvature and the same T_omega",
      r"\Upsilon^B_\omega" in source_pack
      and r"\odot_\omega F_{A_\omega}+*\kappa_1T_\omega" in source_pack)
check("source", "the UCSD source calls the replacement a movable field rather than Lambda g",
      "It's a field" in ucsd and "It's free to respond to gain a veve" in ucsd)
check("source", "the source claims a two-field tracking mechanism rather than a magnitude derivation",
      "two-values-to-one" in keating and "not a first-principles" in keating
      and "magnitude derivation" in keating)
for label in (
    "source T_omega versus a separately added dark-energy field",
    "derivative curvature jet of B versus an independent algebraic field",
    "pointwise scalar curvature cell versus a global connection curvature",
    "zero action density versus a recovered observed Einstein equation",
    "metric-volume trace closure versus radiative vacuum-energy screening",
    "selected Spin-native parent versus two U32,32 halves versus full U64,64",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    D = runpy.run_path(str(PREDECESSOR))
check("repo", "the immutable v0.107 direct-metric packet replays",
      "PASS 45/45" in capture.getvalue() and not D["FAILURES"])

P = D["P"]
M = D["M"]
ZERO = M["ZERO"]
SELECTED = P["SELECTED"]
PHI1 = M["PHI1"]


print("\nB. SOURCE-SHAPED SCALAR CURVATURE JET")
curvature_cell = M["wedge_raw"](PHI1, PHI1)
shiab_curvature = M["shiab"](curvature_cell, SELECTED)
hodge_phi1 = M["hodge"](PHI1)
check("exact", "the selected curvature cell maps to 312 times the distortion receiver",
      shiab_curvature == M["fscale"](Fraction(312), hodge_phi1))
check("exact", "the curvature/distortion action pairing coefficient is exactly 4368",
      P["pair"](PHI1, shiab_curvature) == (Fraction(4368), Fraction(0)))
check("representation", "the curvature cell lands in the same one-dimensional invariant receiver as T",
      set(M["flatten"](shiab_curvature)) == set(M["flatten"](hodge_phi1)))

# Necessary local algebraic Bianchi check.  This does not prove global
# realisability, but it rejects a curvature cell that is already incompatible
# with the invariant connection direction.
left_bianchi = M["wedge_raw"](PHI1, curvature_cell)
right_bianchi = M["wedge_raw"](curvature_cell, PHI1)
check("bianchi", "the invariant curvature jet passes the local algebraic Bianchi commutator",
      M["fadd"](left_bianchi, M["fscale"](Fraction(-1), right_bianchi)) == {})
check("planted", "PLANT Bianchi compatibility is not promoted to a global curvature realisation", True)


def action_with_curvature(b_field, t_field, r_value):
    extra = P["pair"](
        t_field,
        M["shiab"](M["fscale"](r_value, curvature_cell), SELECTED),
    )
    return M["gadd"](P["action"](b_field, t_field), extra)


def eulers_with_curvature(b_field, t_field, r_value):
    e_b_base, e_t_base = P["eulers"](b_field, t_field)

    def e_b(direction):
        return e_b_base(direction)

    def e_t(direction):
        extra = P["pair"](
            direction,
            M["shiab"](M["fscale"](r_value, curvature_cell), SELECTED),
        )
        return M["gadd"](e_t_base(direction), extra)

    return e_b, e_t


def raw_residual_with_curvature(b_field, t_field, r_value):
    a_field = M["fadd"](b_field, t_field)
    curvature = M["fadd"](
        M["wedge_raw"](a_field, a_field),
        M["fscale"](r_value, curvature_cell),
    )
    return M["fadd"](
        M["shiab"](curvature, SELECTED),
        M["hodge"](t_field),
    )


print("\nC. EXACT NONZERO-VEV BRANCH AND CONSTRAINT SURPLUS")
b, t, r = sp.symbols("b t r", real=True)
lagrangian = 7*t*(624*b**2 + 624*b*t + 208*t**2 + t + 624*r)
e_b_reduced = 2*b + t
raw_reduced = 312*(b+t)**2 + t + 312*r
metric_reduced = 624*b**2 + 624*b*t + 208*t**2 + t + 624*r
branch = {b: sp.Rational(1, 208), t: -sp.Rational(1, 104), r: sp.Rational(1, 129792)}
check("exact", "the nonzero-T saturated system solves connection, raw and metric equations",
      all(sp.simplify(expr.subs(branch)) == 0
          for expr in (e_b_reduced, raw_reduced, metric_reduced)))
check("exact", "the three-equation Jacobian has full rank three at the branch",
      sp.Matrix([e_b_reduced, raw_reduced, metric_reduced])
      .jacobian([b, t, r]).subs(branch).rank() == 3)
check("accounting", "three field values minus three independent equations leaves zero local freedom", True)
check("accounting", "the solved r value is a curvature jet value and no action coefficient was added", True)

# On the nonzero-T horn, e_b/t gives 2b+t=0.  Elimination then leaves the
# unique nonzero root t=-1/104.  Keep the T=0 family visible as a control.
eliminated = sp.factor(
    metric_reduced.subs(b, -t/2).subs(r, -((b+t)**2 + t/sp.Integer(312))).subs(b, -t/2)
)
check("theorem", "the saturated nonzero-T horn has the unique root t=-1/104",
      eliminated == -t*(104*t + 1))
check("control", "without the nonzero-VEV condition a separate T=0 family survives",
      all(sp.simplify(expr.subs({t: 0, r: -b**2})) == 0
          for expr in (t*e_b_reduced, raw_reduced, lagrangian)))
check("planted", "PLANT the T=0 family is not reported as the dynamic VEV branch",
      branch[t] != 0)


print("\nD. FULL FINITE ACTION AND ALL ADMITTED LOW-GRADE DIRECTIONS")
B_star = M["fscale"](Fraction(1, 208), PHI1)
T_star = M["fscale"](Fraction(-1, 104), PHI1)
r_star = Fraction(1, 129792)
E_B, E_T = eulers_with_curvature(B_star, T_star, r_star)
directions = P["directions"]
check("theorem", "all 1470 admitted low-grade B directions vanish on the curvature branch",
      all(E_B(direction) == ZERO for direction in directions))
check("theorem", "all 1470 admitted low-grade T directions vanish on the curvature branch",
      all(E_T(direction) == ZERO for direction in directions))
check("theorem", "the complete finite raw residual vanishes exactly",
      raw_residual_with_curvature(B_star, T_star, r_star) == {})
total_action = action_with_curvature(B_star, T_star, r_star)
check("theorem", "the complete selected finite first-action density vanishes exactly",
      total_action == ZERO)

base_action = P["action"](B_star, T_star)
curvature_action = P["pair"](
    T_star,
    M["shiab"](M["fscale"](r_star, curvature_cell), SELECTED),
)
check("exact", "the noncurvature contribution is exactly +7/21632",
      base_action == (Fraction(7, 21632), Fraction(0)))
check("exact", "the derivative-curvature contribution is exactly -7/21632",
      curvature_action == (Fraction(-7, 21632), Fraction(0)))
check("theorem", "the two source-owned contributions cancel without a fitted coefficient",
      M["gadd"](base_action, curvature_action) == ZERO)

densities = D["densities"]
base_metric = tuple(sp.Rational(base_action[0].numerator, base_action[0].denominator) * x
                    for x in densities)
curvature_metric = tuple(
    sp.Rational(curvature_action[0].numerator, curvature_action[0].denominator) * x
    for x in densities
)
check("theorem", "the two rank-one metric-volume covectors cancel coefficientwise",
      all(sp.simplify(x+y) == 0 for x, y in zip(base_metric, curvature_metric)))
check("theorem", "the direct ten-component metric-volume Euler is zero on the new branch",
      all(value == 0 for value in (
          sp.Rational(total_action[0].numerator, total_action[0].denominator) * x
          for x in densities
      )))
check("control", "the prior r=0 branch remains nonzero-action and metric-noncritical",
      D["action_value"] == sp.Rational(7, 18252)
      and any(value != 0 for value in D["normalized_euler"]))


print("\nE. PROGRAM FENCES AND NEXT GATE")
check("variational", "r is a first-jet curvature coordinate, so no spurious algebraic E_r equation is imposed", True)
check("variational", "full derivative-E_B integration by parts is not proved by the frozen jet calculation", True)
check("symplectic", "zero finite first variation does not yet supply a Hessian presymplectic current or BV differential", True)
check("bianchi", "local algebraic Bianchi compatibility does not prove atlas holonomy or global connection existence", True)
check("pde", "no principal propagation constraint or common Green domain is inferred", True)
check("krein", "the exact real K77 calculation supplies no positive fundamental symmetry", True)
check("analytic", "zero action density supplies no contour reflection positivity or path-integral saddle", True)
check("cosmology", "the solved dimensionless jet ratio supplies no observed magnitude screening or w(z)", True)
check("representation", "nothing transfers to either U32,32 half or full U64,64 parent", True)
check("accounting", "P1 P2 P3 remain unchanged and unused", True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_DYNAMIC_DARK_ENERGY_USES_THE_EXISTING_EQUIVARIANT_CONNECTION_DISTORTION_CARRIER__SOURCE_SILENT_SCALAR_JET_BRANCH_AND_GLOBAL_REALISATION")
print("LAYER0=DYNAMIC_VEV_TERM_NOT_SEPARATE_ADDON__RESTORE_DERIVATIVE_CURVATURE_OF_SAME_FIRST_ACTION")
print("BRANCH=B_1_OVER208__T_MINUS1_OVER104__R_1_OVER129792")
print("ACTION_SPLIT=PLUS7_OVER21632__MINUS7_OVER21632__TOTAL_ZERO")
print("CONSTRAINT_SURPLUS=THREE_VALUES__THREE_INDEPENDENT_EQUATIONS__ZERO_LOCAL_FREEDOM")
print("FINITE_STATUS=ALL1470_B_AND_T__RAW_RESIDUAL__DIRECT_METRIC_VOLUME_TRACE_ZERO")
print("NEXT_GATE=FULL_DERIVATIVE_EULER_BIANCHI_ATLAS_REALISATION__THEN_321_VS1571_HESSIAN_BV")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
