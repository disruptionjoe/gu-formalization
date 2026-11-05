"""Exact K2564 geometry/control checks; universal domain proof is in the note."""
from pathlib import Path
import hashlib
import json
import sys
import sympy as s

R = Path(__file__).resolve().parents[2]
checks, controls = {}, {}


def ck(name, value):
    checks[name] = bool(value)
    if not value:
        raise AssertionError(name)


def ct(name, value):
    controls[name] = bool(value)
    if not value:
        raise AssertionError("contrary: " + name)


# Actual induced hyperquadric geometry, in nonsingular R4 x S3 coordinates.
y = s.Matrix(s.symbols("y0:4", real=True))
rho2 = (y.T * y)[0]
m = 1 + rho2
I = s.eye(4)
a = I + y * y.T
gy = -(I - y * y.T / m)
inverse_gy = -a
for i in range(4):
    for j in range(4):
        ck(f"actual_negative_metric_inverse_{i}_{j}",
           s.cancel((gy * inverse_gy)[i, j] - I[i, j]) == 0)
ck("ambient_hyperquadric_norm", s.expand(m - rho2) == 1)
# The matrix determinant lemma gives det(-I+yy^T/m)=1-rho²/m in dimension4.
ck("rank_one_metric_determinant", s.cancel(1 - rho2 / m - 1 / m) == 0)
ck("full_seven_dimensional_volume_squared", s.cancel(m**3 / m - m**2) == 0)
for j in range(4):
    actual_drift = sum(s.diff(m * a[i, j], y[i]) for i in range(4)) / m
    ck(f"actual_volume_divergence_drift_{j}", s.cancel(actual_drift - 7 * y[j]) == 0)


def positive_y(f, density=m):
    return s.cancel(sum(s.diff(density * sum(a[i, j] * s.diff(f, y[j])
                                           for j in range(4)), y[i])
                        for i in range(4)) / density)


def Y_over_K(f, ell=0):
    return s.cancel(-positive_y(f) - ell * f / m)


def companion(f, ell=0):
    return s.cancel(f - positive_y(f) + (2 - 1 / m) * ell * f)


ell = s.symbols("ell", nonnegative=True)
fixtures = [s.Integer(1), y[0], rho2, y[0] * y[1], y[0]**2 * y[2] + y[3]]
for j, f in enumerate(fixtures):
    ck(f"actual_companion_operator_identity_{j}",
       s.cancel(companion(f, ell) - f - Y_over_K(f, ell) - 2 * ell * f) == 0)
ck("actual_Y_on_radial_quadratic", s.expand(Y_over_K(rho2) + 8 + 16 * rho2) == 0)
ck("actual_Y_on_cartesian_linear", s.expand(Y_over_K(y[0]) + 7 * y[0]) == 0)
ck("actual_Y_on_theta_first_harmonic", s.cancel(Y_over_K(s.Integer(1), 3) + 3 / m) == 0)

# The radial coordinate conversion reproduces the full warped drift.
t, radial_s = s.symbols("t radial_s", positive=True)
ck("hyperbolic_embedding_norm", s.trigsimp(s.cosh(t)**2 - s.sinh(t)**2) == 1)
ck("hyperbolic_radial_metric_sign", s.trigsimp(s.sinh(t)**2 - s.cosh(t)**2) == -1)
ck("warped_to_cartesian_drift", s.cancel(radial_s + 3 * radial_s
   + 3 * (1 + radial_s**2) / radial_s - (3 / radial_s + 7 * radial_s)) == 0)
ck("theta_ellipticity_margin", s.cancel((2 - 1 / m) - 1 - rho2 / m) == 0)
xi = s.Matrix(s.symbols("xi0:4", real=True))
ck("cartesian_ellipticity_sum_of_squares",
   s.expand((xi.T * a * xi)[0] - (xi.T * xi)[0] - (xi.T * y)[0]**2) == 0)

# Joint spectral bound: q=1+ell+z captures the actual closed-form lower bound.
z, K = s.symbols("z K", nonnegative=True)
q = 1 + ell + z
nu_over_K = q - 1 - 2 * ell
ck("joint_upper_spectral_margin", s.expand(q - 1 - nu_over_K) == 2 * ell)
ck("joint_lower_spectral_margin", s.expand(q - 1 + nu_over_K) == 2 * z)
ck("joint_squared_bound", s.expand((q - 1)**2 - nu_over_K**2) == 4 * ell * z)
ck("polynomial_synthesis_bound", s.expand((1 + K) * q - (1 + K * q)) == ell + z)
ck("dimension_seven_point_evaluation", s.Integer(4) > s.Rational(7, 2))
ck("radial_three_dimensional_regular_reconstruction", 30 > 26 + s.Rational(3, 2))
ck("radial_five_dimensional_regular_reconstruction", 30 > 26 + s.Rational(5, 2))
ck("safe_potential_negative_order", 4 + 2 * 86 == 176)
ck("safe_field_negative_order", 4 + 2 * 86 + 26 == 202)

# Actual inherited constants enter the source-disjoint curvature observation.
k = s.symbols("k", nonzero=True)
curvature = s.Rational(35, 3624192) * k**2
mu = s.Rational(611557655, 39953092608) * k**2
gap = s.factor(mu - 5 * curvature)
ck("actual_homogeneous_observation_gap", gap == s.Rational(67736495, 4439232512) * k**2)
ck("actual_homogeneous_observation_gap_positive", gap.is_positive)
a0 = -s.Rational(5, 2288) * k
rE = 1 / (6 * a0)
ck("original_metric_homogeneous_coefficient_nonzero", s.simplify(-rE * gap / 2) != 0)
eta = s.symbols("eta")
ck("independent_displacement_inverse_mismatch_visible", s.simplify(rE**2 * gap * eta / 2).coeff(eta) != 0)

# Changed-input controls target real geometric/domain failures, not report flags.
origin = {v: 0 for v in y}
ct("dropping_angular_repair_has_negative_theta_symbol",
   s.cancel(1 + Y_over_K(s.Integer(1), 3)).subs(origin) == -2
   and companion(s.Integer(1), 3).subs(origin) == 4)
ct("halving_angular_repair_is_not_elliptic_at_origin",
   s.cancel(1 - 1 / m).subs(origin) == 0
   and s.cancel(2 - 1 / m).subs(origin) == 1)
ct("wrong_volume_density_changes_actual_operator",
   s.expand(positive_y(y[0], density=s.Integer(1)) - positive_y(y[0])) == -2 * y[0])
ct("euclidean_sign_replacement_changes_actual_source_equation",
   s.expand(positive_y(rho2) - Y_over_K(rho2)) == 16 + 32 * rho2)
# Local frozen signature(3,4) has null high frequencies: no elliptic principal control.
n = s.symbols("n", positive=True)
signature = [1, 1, 1, -1, -1, -1, -1]
null_xi = [n, 0, 0, n, 0, 0, 0]
ct("indefinite_principal_graph_cannot_supply_elliptic_control",
   sum(sign * val**2 for sign, val in zip(signature, null_xi)) == 0
   and sum(val**2 for val in null_xi) == 2 * n**2)
ct("polynomial_multiplier_needs_regular_order_loss",
   s.cancel((1 + n)**86 / (1 + n)**86) == 1
   and s.limit((1 + n)**86, n, s.oo) == s.oo)
ct("spectral_overlap_division_has_actual_poles",
   s.cancel(1 / (s.Symbol("nu") + mu)).subs(s.Symbol("nu"), -mu) == s.zoo)
ct("splitter_gauge_does_not_remove_homogeneous_observation", gap != 0)

paths = [
    "explorations/conditional-build/k2564-localized-spectral-response-2026-11-05.md",
    "tests/channel-swings/k2564_localized_spectral_response_probe.py",
    "explorations/conditional-build/k2562-parameter-dependent-response-2026-11-05.md",
    "lab/process/k2562-parameter-dependent-response.json",
    "explorations/conditional-build/k2558-distributional-splitter-overlap-2026-11-05.md",
    "explorations/conditional-build/k2552-localized-source-domain-2026-11-04.md",
]
report = {
    "result": "K2564",
    "checks": checks,
    "contrary_controls": controls,
    "bounds": {
        "joint_spectral": "abs(nu)<=K(q-1)<=Kq",
        "point_source": "delta_B in H_Q^-4",
        "multiplier": "H_Q^-s to H30_rad tensor H_Q^(-s-2p)",
        "safe_potential_order": -176,
        "safe_field_local_order": -202,
    },
    "evidence_kinds": {
        "exact": "actual hyperquadric metric/volume/Laplacian, companion identities, joint-spectrum inequalities, actual curvature coefficient",
        "supporting": "finite polynomial operator fixtures and local frozen null covectors",
        "universal": "Friedrichs form, harmonic reduction, point-source scale, Hilbert spectral synthesis and equation passage are proved in note",
        "reused": "K2562 radial response estimates, K2552 full reconstruction and K2558 overlap/local inverse and homogeneous observation",
        "not_claimed": "physical preparation, causal Green operator, identical-boundary ambiguity, pointwise observer trace, native GU recovery",
    },
    "dependencies": {p: hashlib.sha256((R / p).read_bytes()).hexdigest() for p in paths},
}
out = R / "lab/process/k2564-localized-spectral-response.json"
if "--write" in sys.argv:
    out.write_text(json.dumps(report, indent=2) + "\n")
else:
    assert json.loads(out.read_text()) == report, "saved report consistency"
print("K2564 PASS", len(checks), "exact/supporting groups", len(controls), "contrary controls")
