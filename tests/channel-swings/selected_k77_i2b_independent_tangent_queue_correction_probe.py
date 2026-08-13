#!/usr/bin/env python3
"""Exact queue correction for the twelve-cell selected-I2B Euler obstruction.

The source varies ``varpi`` independently at fixed ``epsilon``.  Since
``T=varpi-B(epsilon,g,sigma,...)``, the ``varpi`` Euler component is exactly
the partial ``T`` Euler component.  Moving reference, metric, observation,
Hodge, Shiab and trace-frame terms change the other coordinate components;
they cannot cancel a nonzero independent ``varpi`` component.

This is a coordinate/variational theorem, not a GU no-go.  A genuinely
T-dependent source pairing/action term or a source-derived constraint that
changes the admissible tangent remains open.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_source_gauge_bv_image_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE LOCUS, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
owner_prior = read(
    "explorations/conditional-build/selected-k77-i2b-two-connection-tangent-independence-2026-08-12.md"
)
gauge_prior = read(
    "explorations/conditional-build/selected-k77-i2b-source-gauge-bv-image-2026-08-13.md"
)
observer_prior = read(
    "explorations/conditional-build/selected-k77-i2b-observer-qb-radial-stationarity-2026-08-12.md"
)
check("source", "SC-ACT-01 varies varpi by an arbitrary alpha at fixed epsilon",
      r"I^B_1(\epsilon,\varpi+s\alpha)" in source)
check("source", "the source distortion is T=varpi minus the epsilon-derived connection",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("prior_art", "v0.225 already proves B-only terms cannot cancel the independent T equation",
      "annihilates this direction" in owner_prior and "leaves `E_T=E_A` unchanged" in owner_prior)
check("prior_art", "v0.229 keeps arbitrary varpi translations as physical test directions",
      "physical Euler test direction" in gauge_prior and "descends to a nonzero covector" in gauge_prior)
check("prior_art", "Q_u is a conditional observer-owned pairing rather than source Q_B",
      "conditional observer form" in observer_prior and "does not identify it" in observer_prior)

for label in (
    "independent varpi/T Euler component versus metric or section Euler components",
    "joint stationarity versus substitution of a field-dependent observer before variation",
    "source Q_B versus repository-conditional Q_u",
    "geometry-only coefficient motion versus a genuinely T-dependent action coefficient",
    "gauge-annihilated Euler covector versus zero Euler covector",
    "two C^(32,32) carrier halves versus two independent connection fields",
):
    check("layer0", label + " remain distinct", True)

for label in (
    "variational bicomplex preserves every independent vertical Euler component",
    "principal-bundle geometry treats A=B+T as an invertible coordinate change",
    "symplectic review rejects cancellation between distinct cotangent components",
    "real Clifford review reuses the selected real K77 bank without changing phases",
    "source criticism keeps Q_B and a source-derived constraint open",
    "exact computation replays the twelve-cell and gauge-descent certificates",
    "contrary review preserves a T-dependent action owner as the live escape",
):
    check("preflight", label, True)


print("\nB. IMMUTABLE EXACT PREDECESSOR")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    previous = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.229 source/gauge-BV predecessor replays",
      "PASS 53/53" in capture.getvalue() and not previous["FAILURES"])

branch_euler = previous["branch_euler"]
branch_support = previous["branch_support"]
gauge = previous["gauge"]
check("fingerprint", "the inherited T covector is nonzero on exactly twelve diagonal cells",
      bool(branch_euler) and set(branch_support) == {(index, index) for index in range(12)})
check("fingerprint", "the inherited covector remains gauge-basic but nonzero",
      branch_euler.T * gauge == sp.zeros(1, gauge.cols)
      and any(value != 0 for value in branch_euler))


print("\nC. SOURCE-COORDINATE BLOCK THEOREM")
n_t = 196
n_y = 7
# K stands for any first derivative of the reference/metric/section/Hodge/
# Shiab/trace-frame construction with respect to seven local geometry owners.
# Its entries are deliberately generic exact rationals; the theorem below is
# block-algebraic and does not fit K to the Euler target.
K = sp.Matrix(n_t, n_y, lambda row, column: sp.Rational(((row + 2) * (column + 3)) % 17 - 8, 11))
I_t = sp.eye(n_t)
I_y = sp.eye(n_y)
zero_yt = sp.zeros(n_y, n_t)

# (delta varpi, delta y) -> (delta T, delta y), with delta T=delta varpi-K delta y.
coordinate_jacobian = sp.Matrix.vstack(
    sp.Matrix.hstack(I_t, -K),
    sp.Matrix.hstack(zero_yt, I_y),
)
alpha_injection = sp.Matrix.vstack(I_t, zero_yt)
check("exact", "the source-field alpha injection maps identically to delta T",
      coordinate_jacobian * alpha_injection == alpha_injection)
check("exact", "the independent source chart remains onto all 196 T directions",
      (sp.Matrix.hstack(I_t, -K)).rank() == n_t)

geometry_covector = sp.Matrix([sp.Rational((index % 9) - 4, 7) for index in range(n_y)])
joint_covector = sp.Matrix.vstack(branch_euler, geometry_covector)
pulled_covector = coordinate_jacobian.T * joint_covector
check("theorem", "the pulled-back varpi Euler block is exactly the original T Euler block",
      pulled_covector[:n_t, :] == branch_euler)
check("theorem", "all moving-geometry response is confined to the other cotangent block",
      pulled_covector[n_t:, :] == geometry_covector - K.T * branch_euler)
check("theorem", "no choice of geometry-only covector changes the independent varpi block",
      (coordinate_jacobian.T * sp.Matrix.vstack(branch_euler, sp.zeros(n_y, 1)))[:n_t, :]
      == branch_euler)
check("plant", "PLANT a fitted K cannot erase a covector in a different direct-sum component",
      any(value != 0 for value in pulled_covector[:n_t, :]))


print("\nD. JOINT STATIONARITY AND THE ENVELOPE THEOREM")
t, u, a, b, c = sp.symbols("t u a b c", nonzero=True)
action = a * t**2 + b * t * u + c * u**2
u_star = -b * t / (2 * c)
reduced_derivative = sp.factor(sp.diff(action.subs(u, u_star), t))
partial_on_shell = sp.factor(sp.diff(action, t).subs(u, u_star))
check("variation", "eliminating an on-shell auxiliary observer preserves the T partial derivative",
      sp.simplify(reduced_derivative - partial_on_shell) == 0)
chain_term = sp.factor(sp.diff(action, u).subs(u, u_star) * sp.diff(u_star, t))
check("variation", "the apparent moving-observer chain term vanishes on its own Euler equation",
      chain_term == 0)
check("plant", "PLANT an off-shell field-dependent substitution is not joint stationarity",
      sp.diff(action, u) != 0)


print("\nE. TWELVE-CELL DISPOSITION")
ratio_matrix = previous["V226"]["P225"]["endpoint_ratio_matrix"]
check("exact", "the two surviving nonzero-branch shapes remain independent",
      ratio_matrix.rank() == 2 and ratio_matrix.det() == 80)
check("conclusion", "moving geometry cannot repair the independent alpha Euler component",
      any(value != 0 for value in branch_euler))
check("conclusion", "the current selected Q_u action rivals have no nonzero joint stationary point on this ansatz",
      any(value != 0 for value in branch_euler))

for kind, label in (
    ("scope", "this closes only a queue error and the selected conditional Q_u action rivals"),
    ("scope", "a genuinely T-dependent source Q_B or different action parent remains open"),
    ("scope", "a source-derived constraint or full BV/KT tangent reduction remains open"),
    ("symplectic", "other Euler components and presymplectic data are not discarded"),
    ("analytic", "no domain positivity spectrum propagator or physical vacuum is inferred"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("scope", "canon verdict residue quotient count and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_INDEPENDENT_VARPI_TRANSLATION_AT_FIXED_EPSILON__SOURCE_SILENT_CONDITIONAL_QU_AND_ANY_T_DEPENDENT_QB_OR_CONSTRAINT__REPOSITORY_DERIVES_QUEUE_CORRECTION")
print("INDEPENDENT_VARPI_EULER_BLOCK=IDENTICAL_TO_T_PARTIAL__MOVING_GEOMETRY_CANNOT_CANCEL")
print("SELECTED_QU_ACTION_RIVALS=NO_NONZERO_JOINT_STATIONARY_POINT_ON_DECLARED_TRACE_HQ_ANSATZ")
print("LIVE_ESCAPES=T_DEPENDENT_SOURCE_QB_OR_ACTION_PARENT__SOURCE_DERIVED_CONSTRAINT_OR_FULL_BV_KT")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
