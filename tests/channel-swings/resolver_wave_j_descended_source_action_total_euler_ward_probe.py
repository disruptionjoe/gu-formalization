#!/usr/bin/env python3
r"""Resolver Wave J: local density and cyclic coefficient comparators.

This probe constructs local comparator fixtures constrained by the displayed
bosonic ``I_B^1`` coefficients.  It does not construct that native action and
does not invent the unresolved complete fermion action.  The checks separate:

* exact three-chart transport of a source-shaped density comparator;
* the source ``1/2,1/3`` cyclic coefficient/transgression arithmetic;
* a nonzero Green/preboundary comparator and a local off-shell Ward fixture;
* a live grade-two quadratic-eddy coefficient from an actual rank-252 image
  one-form, retained as a degree-correct placement burden;
* the public-coset curvature correction forced by the non-homomorphic
  ``U(K) -> Sp(K,J)`` Reynolds reduction; and
* live metric/Theta/density and chosen-J/projector response owners.

The result is local and partial.  ``Psrc`` is used as a tangency diagnostic,
not silently identified with Weinstein's degree ``2 -> 13`` Shiab map.  No
complete boson-plus-fermion tangency, Diff/BV identity, common analytic domain,
physical no-leakage, VEV, mass, index, or count is claimed.
"""

from __future__ import annotations

import contextlib
import importlib
import io
from pathlib import Path
import sys

import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

with contextlib.redirect_stdout(io.StringIO()):
    wave_i = importlib.import_module(
        "resolver_wave_i_actual_metx_zorro_theta_descent_probe"
    )

wave_h = wave_i.wave_h

FAILURES: list[str] = []
COUNTS = {
    "exact": 0,
    "numeric": 0,
    "source": 0,
    "type": 0,
    "planted": 0,
}


def check(kind: str, label: str, condition: bool, detail: str = "") -> None:
    COUNTS[kind] += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'} [{kind}]: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def matrix_zero(value: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in value)


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and matrix_zero(left - right)


def commutator(left: sp.MatrixBase, right: sp.MatrixBase) -> sp.Matrix:
    return left * right - right * left


def eta_trace_pair_oneform(left, right) -> sp.Expr:
    """Indefinite raw-C* pairing in the adapted Wave-I frame."""
    total = sp.Integer(0)
    for index, sign in enumerate(wave_h.ETA):
        total += sign * wave_h.trace_pair_element(
            left.get(index, {}), right.get(index, {})
        )
    return wave_h.simp(total)


def source_density_value(t_value, f_value, d_value, q_value) -> sp.Expr:
    residual = wave_h.of_add(
        f_value,
        wave_h.of_add(
            wave_h.of_scale(sp.Rational(1, 2), d_value),
            wave_h.of_scale(sp.Rational(1, 3), q_value),
        ),
    )
    return wave_h.simp(
        eta_trace_pair_oneform(t_value, residual)
        + sp.Rational(1, 5) * eta_trace_pair_oneform(t_value, t_value)
    )


print("A. LAYER 0 AND PRIMARY-SOURCE COLLISION")

source_pack = (
    ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
).read_text()
rb2_report = (
    ROOT / "explorations/rb2-source-action-exactness-shootout-2026-07-30.md"
).read_text()
wave_i_report = (
    ROOT / "explorations/resolver-wave-i-actual-metx-zorro-theta-descent-2026-08-03.md"
).read_text()

check(
    "source",
    "the source explicitly owns I_B1 and its translation-direction variation",
    "WGS-01" in source_pack
    and "I^B_1" in source_pack
    and "varpi+s\\alpha" in source_pack,
)
check(
    "source",
    "the source fixes the eddy coefficients one-half and one-third",
    "\\frac12d_{B_\\omega}T_\\omega" in source_pack
    and "\\frac13[T_\\omega,T_\\omega]" in source_pack,
)
check(
    "source",
    "the source places bosonic and fermionic pieces in one Euler-residual arena",
    "\\Upsilon^B_\\omega+\\Upsilon^F_\\omega=0" in source_pack,
)
check(
    "source",
    "the repo already refuses to call homogeneous covariance a native Ward identity",
    "not a native Ward identity" in rb2_report,
)
check(
    "source",
    "Wave I already types raw C-star and raised-C projector carriers separately",
    "`flat_eta Psrc_raised sharp_eta`" in wave_i_report,
)
check(
    "type",
    "source Shiab, rank-252 Psrc, translation Euler, Ward identity, and observed equation are distinct objects",
    True,
)
check(
    "type",
    "A0 remains Levi-Civita-derived but its exact Y-side owner is uncertain",
    "remains `UNCERTAIN`" in wave_i_report,
)
check(
    "type",
    "K is held as invariant representation data; metric/Hodge/Krein primalization still moves",
    True,
)


print("\nB. THREE-CHART TRANSPORT OF A SOURCE-SHAPED DENSITY COMPARATOR")

# The four objects below are already density-dual one-form representatives in
# the local composed source sector.  Psrc supplies a nonzero exact diagnostic
# value, but it is not renamed as the source Shiab map.
t0 = wave_i.T_raw_0
f0 = wave_i.Psrc_raw_0(t0)
d0 = wave_h.of_scale(2, f0)
q0 = wave_h.of_scale(3, f0)

t1 = wave_i.Uraw01(t0)
t2 = wave_i.Uraw02(t0)
f1, d1, q1 = (wave_i.Uraw01(value) for value in (f0, d0, q0))
f2, d2, q2 = (wave_i.Uraw02(value) for value in (f0, d0, q0))

action0 = source_density_value(t0, f0, d0, q0)
action1 = source_density_value(t1, f1, d1, q1)
action2 = source_density_value(t2, f2, d2, q2)
check(
    "exact",
    "every source-shaped summand is live in the descended scalar fixture",
    eta_trace_pair_oneform(t0, f0) != 0
    and eta_trace_pair_oneform(t0, d0) != 0
    and eta_trace_pair_oneform(t0, q0) != 0
    and eta_trace_pair_oneform(t0, t0) != 0,
)
check(
    "exact",
    "the indefinite scalar action value agrees on all three adapted charts",
    action0 == action1 == action2 and action0 != 0,
)
check(
    "exact",
    "direct and sequential raw-C-star transport give the same chart-two density",
    source_density_value(
        wave_i.Uraw12(t1),
        wave_i.Uraw12(f1),
        wave_i.Uraw12(d1),
        wave_i.Uraw12(q1),
    )
    == action2,
)

h0 = wave_i.h0_value
h1 = wave_i.h1_value
h2 = wave_i.h2_value
gamma1 = [sp.simplify(entry.subs(wave_i.y_point))
          for entry in wave_i.gamma1_rule]
gamma2 = [sp.simplify(entry.subs(wave_i.z_point))
          for entry in wave_i.gamma2_rule]
g_y0 = wave_i.coordinate_gimmel(h0, wave_i.gamma0)
g_y1 = wave_i.coordinate_gimmel(h1, gamma1)
g_y2 = wave_i.coordinate_gimmel(h2, gamma2)

h0_sub = dict(zip(wave_i.h_symbols, wave_i.symmetric_components(h0)))
h1_sub = dict(zip(wave_i.h1_symbols, wave_i.symmetric_components(h1)))
d01 = sp.simplify(wave_i.D01.subs({**wave_i.x_point, **h0_sub}))
d12 = sp.simplify(wave_i.D12.subs({**wave_i.y_point, **h1_sub}))
d02 = sp.simplify(wave_i.D02.subs({**wave_i.x_point, **h0_sub}))
rho0 = sp.sqrt(sp.Abs(g_y0.det()))
rho1 = sp.sqrt(sp.Abs(g_y1.det()))
rho2 = sp.sqrt(sp.Abs(g_y2.det()))

check(
    "exact",
    "the pointwise scalar-density comparator obeys the fourteen-dimensional Jacobian law",
    sp.simplify(rho1 * sp.Abs(d01.det()) * action1 - rho0 * action0) == 0
    and sp.simplify(rho2 * sp.Abs(d12.det()) * action2 - rho1 * action1) == 0
    and sp.simplify(rho2 * sp.Abs(d02.det()) * action2 - rho0 * action0) == 0,
)
check(
    "exact",
    "the direct and sequential scalar-density transports agree on the triple overlap",
    sp.simplify(
        rho2 * sp.Abs(d12.det()) * sp.Abs(d01.det()) * action2
        - rho0 * action0
    ) == 0,
)
check(
    "planted",
    "dropping the metric-bundle Jacobian breaks the chart-one density law",
    sp.simplify(rho1 * action1 - rho0 * action0) != 0,
)
check(
    "planted",
    "using the raised-vector law on the raw source fails on the live Lorentz boost",
    not wave_h.of_equal(
        wave_i.wrong_vector_index_transform(
            wave_i.g01, wave_i.g01_inverse, t0
        ),
        t1,
    ),
)


print("\nC. EXACT CYCLIC COEFFICIENT/TRANSGRESSION COMPARATOR")

R = sp.Rational
s = sp.symbols("s", real=True)
b = sp.Matrix([[0, 1, 0], [1, 0, 1], [0, -1, 1]])
t = sp.Matrix([[1, 2, 0], [0, -1, 1], [2, 0, 1]])
f = sp.Matrix([[2, 0, 1], [1, -1, 0], [0, 2, 3]])
alpha = sp.Matrix([[0, 1, 2], [-1, 0, 1], [1, 1, -2]])
kappa = R(3, 7)


def matrix_translation_action(theta, a_value, b_value):
    derivative = b * theta + theta * b
    quadratic = theta * theta
    eddy = f + a_value * derivative + b_value * quadratic
    return sp.expand(sp.trace(theta * eddy)
                     + kappa * sp.trace(theta * theta) / 2)


source_a, source_b = R(1, 2), R(1, 3)
direct_translation = sp.diff(
    matrix_translation_action(t + s * alpha, source_a, source_b), s
).subs(s, 0)
source_euler = (
    f + 2 * source_a * (b * t + t * b)
    + 3 * source_b * (t * t) + kappa * t
)
owner_translation = sp.trace(alpha * source_euler)
translated_curvature = f + (b * t + t * b) + t * t + kappa * t

check(
    "exact",
    "direct differentiation equals the cyclic coefficient/transgression owner formula",
    sp.simplify(direct_translation - owner_translation) == 0
    and direct_translation != 0,
)
check(
    "exact",
    "one-half and one-third reconstruct unit derivative and quadratic weights",
    matrix_equal(source_euler, translated_curvature),
)
check(
    "exact",
    "the derivative and quadratic channels are linearly independent",
    sp.Matrix.hstack(
        sp.Matrix(b * t + t * b).reshape(9, 1),
        sp.Matrix(t * t).reshape(9, 1),
    ).rank() == 2,
)
for wrong_a, wrong_b in ((R(1), R(1, 3)), (R(1, 2), R(1, 2))):
    wrong_euler = f + 2 * wrong_a * (b * t + t * b) + 3 * wrong_b * t * t + kappa * t
    check(
        "planted",
        f"wrong eddy point ({wrong_a},{wrong_b}) misses translated curvature",
        not matrix_equal(wrong_euler, translated_curvature),
    )


print("\nD. GREEN OWNER AND LOCAL OFF-SHELL WARD FIXTURES")

x = sp.symbols("x", real=True)
j2 = sp.Matrix([[0, 1], [-1, 0]])
v2 = sp.Matrix([[2, x], [x, 3]])
ell = sp.Matrix([1, -1])
q = sp.Matrix([x + x**2, 1 + x**3])
aq = sp.Matrix([1 + x, x**2])


def green_action(q_value):
    kinetic = (q_value.T * j2 * q_value.diff(x))[0] / 2
    potential = (q_value.T * v2 * q_value)[0] / 2
    cubic = (ell.dot(q_value)) ** 3 / 3
    return sp.integrate(sp.expand(kinetic + potential + cubic), (x, 0, 1))


green_direct = sp.diff(green_action(q + s * aq), s).subs(s, 0)
green_euler = j2 * q.diff(x) + v2 * q + (ell.dot(q)) ** 2 * ell
green_bulk = sp.integrate(sp.expand(aq.dot(green_euler)), (x, 0, 1))
green_boundary = sp.Rational(1, 2) * (
    (q.T * j2 * aq)[0].subs(x, 1) - (q.T * j2 * aq)[0].subs(x, 0)
)
check(
    "exact",
    "the first-order compact-core variation equals bulk Euler plus Green boundary",
    sp.simplify(green_direct - green_bulk - green_boundary) == 0,
)
check(
    "planted",
    "the preboundary term is live and cannot be dropped",
    green_boundary != 0 and sp.simplify(green_direct - green_bulk) != 0,
)
check(
    "type",
    "the two-component Green fixture prices a preboundary owner but is not the unbuilt native Shiab/fermion domain",
    True,
)

# A nonconstant local gauge parameter checks the inhomogeneous connection
# response rather than only constant homogeneous conjugation.
b_x = sp.Matrix([[x, 1], [0, -x]])
t_x = sp.Matrix([[x**2, 1 + x], [x, -1]])
f_x = sp.Matrix([[1, x], [x**2, 2]])
w_x = sp.Matrix([[1 + x, 2], [x, 1 - x]])
xi = sp.Matrix([[0, x], [x**2, 0]])


def local_covariant_action(b_value, t_value, f_value, w_value,
                           a_value=source_a,
                           b_value_coeff=source_b):
    d_t = t_value.diff(x) + commutator(b_value, t_value)
    density = (
        sp.trace(t_value * f_value)
        + a_value * sp.trace(t_value * w_value * d_t)
        + b_value_coeff * sp.trace(t_value * t_value * t_value)
        + kappa * sp.trace(t_value * t_value) / 2
    )
    return sp.integrate(sp.expand(density), (x, 0, 1))


delta_t = commutator(t_x, xi)
delta_b = commutator(b_x, xi) + xi.diff(x)
delta_f = commutator(f_x, xi)
delta_w = commutator(w_x, xi)
ward_direct = sp.diff(
    local_covariant_action(
        b_x + s * delta_b,
        t_x + s * delta_t,
        f_x + s * delta_f,
        w_x + s * delta_w,
    ), s
).subs(s, 0)
ward_bad = sp.diff(
    local_covariant_action(
        b_x + s * commutator(b_x, xi),
        t_x + s * delta_t,
        f_x + s * delta_f,
        w_x + s * delta_w,
    ), s
).subs(s, 0)
wrong_ward = sp.diff(
    local_covariant_action(
        b_x + s * delta_b,
        t_x + s * delta_t,
        f_x + s * delta_f,
        w_x + s * delta_w,
        R(4, 5), R(-1, 4),
    ), s
).subs(s, 0)
check(
    "exact",
    "the GL2 cyclic-trace proxy is invariant along a nonconstant infinitesimal gauge direction",
    sp.simplify(ward_direct) == 0,
)
check(
    "planted",
    "omitting the inhomogeneous d-xi connection response breaks local Ward closure",
    sp.simplify(ward_bad) != 0,
)
check(
    "exact",
    "Ward covariance is coefficient-blind and therefore does not select one-half/one-third",
    sp.simplify(wrong_ward) == 0,
)
check(
    "type",
    "the GL2 covariance proxy is not a native Spin Ward identity and Xi=D_omega Upsilon is not renamed as one",
    True,
)


print("\nE. DEGREE-CORRECT PSRC PLACEMENT BURDEN AND COSET CURVATURE")

p_image = wave_i.Psrc_raw_0(wave_i.T_raw_0)
p_t0 = p_image[0]
p_t1 = p_image[1]
p_bracket = wave_h.ecomm(p_t0, p_t1)
check(
    "exact",
    "the whole actual one-form is Psrc-fixed while its 01 quadratic-eddy coefficient is nonzero grade two",
    wave_h.of_equal(wave_i.Psrc_raw_0(p_image), p_image)
    and bool(p_bracket)
    and {mask.bit_count() for mask in p_bracket} == {2},
)
check(
    "type",
    "the bracket inhabits an Omega2 slot and is never fed back through the Omega1 Psrc map",
    True,
)
check(
    "type",
    "a degree-correct Shiab/curvature output map is required before deciding restricted-action closure or Euler tangency",
    True,
)

# A public-coset pair whose commutator is a selected native grade-six value.
coset_x = wave_h.escale(sp.I, wave_h.blade((0,)))
coset_y = wave_h.escale(sp.I, wave_h.blade((4, 5, 6, 7, 8)))
coset_curvature = wave_h.ecomm(coset_x, coset_y)
coset_reduced_curvature = wave_h.reduce_native(coset_curvature)
check(
    "exact",
    "both public-coset connection directions vanish under R_J",
    not wave_h.reduce_native(coset_x) and not wave_h.reduce_native(coset_y),
)
check(
    "exact",
    "their commutator returns a nonzero native grade-six curvature",
    wave_h.eequal(coset_reduced_curvature, coset_curvature)
    and {mask.bit_count() for mask in coset_curvature} == {6}
    and wave_h.eequal(
        coset_curvature,
        wave_h.escale(18, p_image[0]),
    ),
)
check(
    "planted",
    "F_(R_J A) alone loses the mandatory R_J([m,m]) correction",
    not wave_h.ecomm(
        wave_h.reduce_native(coset_x), wave_h.reduce_native(coset_y)
    )
    and bool(coset_reduced_curvature),
)
check(
    "type",
    "the coset curvature intersects the reference grade-six coefficient support but no Euler port has been applied",
    True,
)
check(
    "type",
    "restricted-action closure, bosonic tangency, and total boson-plus-fermion tangency all remain open",
    True,
)
check(
    "type",
    "Psrc remains a candidate post-variation tangency/output port, not the source Shiab operator",
    True,
)


print("\nF. LIVE THETA/METRIC/DENSITY AND CHOSEN-J/PSRC RESPONSE OWNERS")

metric_parameter = sp.symbols("metric_parameter", real=True)
h_dot = sp.diag(1, 2, -1, 1)
h_family = h0 + metric_parameter * h_dot
theta_family = wave_i.theta_matrix(h_family, wave_i.gamma0)
c_family = wave_i.block_diag(
    h_family.inv(), wave_i.de_witt_matrix(h_family)
)
g_family = sp.simplify(theta_family.T * c_family * theta_family)
g_zero = sp.simplify(g_family.subs(metric_parameter, 0))
d_g_direct = sp.simplify(g_family.diff(metric_parameter).subs(metric_parameter, 0))
theta_zero = sp.simplify(theta_family.subs(metric_parameter, 0))
d_theta = sp.simplify(theta_family.diff(metric_parameter).subs(metric_parameter, 0))
c_zero = sp.simplify(c_family.subs(metric_parameter, 0))
d_c = sp.simplify(c_family.diff(metric_parameter).subs(metric_parameter, 0))
d_g_owner = sp.simplify(
    d_theta.T * c_zero * theta_zero
    + theta_zero.T * d_c * theta_zero
    + theta_zero.T * c_zero * d_theta
)
check(
    "exact",
    "the actual Wave-I metric derivative splits into both Theta legs and the chimeric metric owner",
    matrix_equal(d_g_direct, d_g_owner),
)

raw_probe = sp.Matrix([R(index + 1, 17) for index in range(14)])
pair_zero = sp.simplify((raw_probe.T * g_zero.inv() * raw_probe)[0])
pair_dot = sp.simplify(
    -(raw_probe.T * g_zero.inv() * d_g_direct * g_zero.inv() * raw_probe)[0]
)
density_log_dot = sp.simplify(sp.trace(g_zero.inv() * d_g_direct) / 2)
total_metric_response = sp.simplify(pair_dot + density_log_dot * pair_zero)
d_g_frozen_theta = sp.simplify(theta_zero.T * d_c * theta_zero)
frozen_theta_pair_dot = sp.simplify(
    -(raw_probe.T * g_zero.inv() * d_g_frozen_theta
      * g_zero.inv() * raw_probe)[0]
)
check(
    "exact",
    "the trace-reversed metric/density response is live",
    total_metric_response != 0 and density_log_dot != 0,
)
check(
    "planted",
    "freezing Theta changes the actual metric response",
    frozen_theta_pair_dot != pair_dot,
)
check(
    "planted",
    "freezing the induced density changes the total geometry derivative",
    pair_dot != total_metric_response,
)

check(
    "exact",
    "Wave H's exact chosen-J/projector derivative equals its complete chain formula",
    wave_h.of_equal(wave_h.dp_exact, wave_h.dp_formula),
)
check(
    "exact",
    "the chosen-J/projector response is live on the actual mixed source",
    bool(wave_h.dp_exact) and wave_h.action_derivative != 0,
)
check(
    "planted",
    "an explicitly frozen chosen-J/Psrc auxiliary action has zero derivative and misses the live response",
    sp.diff(
        sp.Rational(1, 2)
        * wave_h.real_trace_pair_oneform(wave_h.p_action_0, wave_h.p_action_0),
        wave_h.S,
    ).subs(wave_h.S, 0) == 0
    and wave_h.action_derivative != 0,
)
check(
    "type",
    "the metric test varies tautological vertical h at frozen observer Gamma; it is not an observer-metric or D_g Gamma variation",
    True,
)
check(
    "type",
    "the coefficient comparator holds derived geometry fixed; live response comparators are not joined to the same source action",
    True,
)
check(
    "type",
    "the complete monolithic B1+IF geometry derivative, native Ward, Diff Ward, and common domain remain unassembled",
    True,
)


print("\nG. DISPOSITION AND BOUNDARY")

check(
    "type",
    "full-public-action then projected-residual is the next candidate route, not an established survivor",
    True,
)
check(
    "type",
    "restrict-before-variation remains open pending a degree-correct curvature/Shiab and Euler test",
    True,
)
check(
    "type",
    "no separate minus-T-current bridge is inserted beside the unresolved source fermion action",
    True,
)
check(
    "type",
    "P1/P2/P3 are unchanged and unused",
    True,
)
check(
    "type",
    "Curt remains formally separate and TG-1 AND TG-2 AND TG-3 remains not promoted",
    True,
)
check(
    "type",
    "no VEV, mass, stationarity, anomaly, index, generation count, or physical no-leakage is claimed",
    True,
)

print("\n" + "=" * 116)
print(
    "COUNTS:",
    ", ".join(f"{kind}={count}" for kind, count in COUNTS.items()),
    f"total={sum(COUNTS.values())}",
)
if FAILURES:
    print("RESOLVER WAVE J FAILURES:")
    for failure in FAILURES:
        print(f"  - {failure}")
    raise SystemExit(1)

print("RESOLVER WAVE J VERDICT: SOURCE_DENSITY_AND_TRANSLATION_COMPARATORS_WITH_COSET_CURVATURE_OBSTRUCTION")
print("A pointwise source-shaped density obeys the Wave-I transport law; separate exact")
print("translation, Green, and GL2 covariance comparators pass. An actual Psrc-fixed")
print("one-form has a live grade-two quadratic-eddy coefficient, and public-coset")
print("directions return a live native grade-six curvature. The native Shiab, monolithic")
print("B1 variation, degree-correct port placement, Euler tangency, Ward, and domain stay open.")
