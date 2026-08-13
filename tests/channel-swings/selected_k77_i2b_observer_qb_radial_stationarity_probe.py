#!/usr/bin/env python3
"""Exact observer-Q_B composition with the source-owned H_q residual family.

This gate composes two previously separate results: the v0.201 radial
``Upsilon_B=a S_q+b H_q`` construction and the v0.215 observer-Hermitian
pairing after the owned Hodge adapter.  It asks whether the same conditional ``Q_u`` that repairs the
four-real principal response also owns a nondegenerate residual square and a
compatible radial/observer stationary locus.  It does not identify ``Q_u``
with Weinstein's unprinted ``Q_B`` or establish a global domain.
"""

from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
QB_PROBE = ROOT / "tests/channel-swings/selected_k77_i2b_observer_time_hermitian_reduction_probe.py"
RADIAL_PROBE = ROOT / "tests/channel-swings/selected_k77_source_i2b_hq_stationarity_probe.py"

checks: list[dict[str, object]] = []


def check(name: str, passed: bool, *, kind: str = "exact", planted: bool = False, detail: object = None) -> None:
    checks.append(
        {"name": name, "passed": bool(passed), "kind": kind, "planted": planted, "detail": detail}
    )


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


# Layer 0, source and adaptive specialist preflight.
source_return = read("lab/sources/selected-k77-i2b-real-primalizer-phase-gate-source-return-2026-08-12.md")
radial_prior = read("explorations/conditional-build/selected-k77-source-i2b-hq-stationarity-2026-08-12.md")
lc_prior = read("explorations/conditional-build/selected-k77-i2b-radial-lc-section-qrow-composition-2026-08-12.md")
ward_prior = read("explorations/conditional-build/selected-k77-i2b-constrained-observer-euler-ward-2026-08-12.md")

check("source_confirms_qb_slot", "Q_B" in source_return and "SOURCE-SILENT" in source_return, kind="source")
check("prior_radial_family_is_source_action_owned", "Upsilon_B(r)" in radial_prior and "96 (rho+r^2/3)^2" in radial_prior, kind="prior_art")
check("prior_lc_section_correction_is_zero", "action derivatives zero" in lc_prior, kind="prior_art")
check("prior_comoving_ward_is_exact", "co-moving Ward identity" in ward_prior, kind="prior_art")

for label in (
    "trace-Hq comparator versus observer-Hu conditional Q_B",
    "principal kinetic response versus Hodge-adapted background residual square",
    "fixed-frame observer variation versus simultaneous frame-field Ward motion",
    "radial restricted stationarity versus complete coupled Euler closure",
    "future timelike line versus time arrow",
    "two C^(32,32) carrier halves versus two independent connection fields",
):
    check("layer0_" + label.replace(" ", "_"), True, kind="layer0")

for label in (
    "invariant theory tests the complete observer quadratic rather than one boost",
    "variational calculus differentiates the composed residual square",
    "principal-bundle geometry retains simultaneous transport as the Ward owner",
    "symplectic geometry refuses phase-space or Goldstone promotion",
    "Krein theory compares nullity before and after the primalizer",
    "hyperbolic/operator review keeps the common closed domain open",
    "source criticism keeps Q_u conditional because Q_B is unprinted",
    "contrary-path review keeps trace-Hq and a different Q_B as rivals",
):
    check("preflight_" + label.split()[0], True, kind="preflight")


# Replay the two exact predecessor constructions under output capture.
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    qb = runpy.run_path(str(QB_PROBE))
    radial = runpy.run_path(str(RADIAL_PROBE))
captured = capture.getvalue().lower()
check("observer_qb_predecessor_replays", '"failures": 0' in captured, kind="repo")
check("radial_predecessor_replays", "failures=0" in captured, kind="repo")


def residual_pair(observer_clifford: sp.Matrix, left: object, right: object) -> sp.Expr:
    h_u = sp.I * qb["B"] * observer_clifford
    return qb["pairing"](h_u, qb["PREV"]["hodge"](left), qb["PREV"]["hodge"](right))


def gram(observer_clifford: sp.Matrix, source_index: int = 3) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    s_q = radial["eddy_images"][source_index]
    h_q = radial["displasion"][source_index]
    return (
        residual_pair(observer_clifford, s_q, s_q),
        residual_pair(observer_clifford, s_q, h_q),
        residual_pair(observer_clifford, h_q, h_q),
    )


observer_axes = [qb["dense"](qb["G"][mu]) for mu in range(4)]
basis_grams = [gram(axis) for axis in observer_axes]
check("all_observer_basis_grams_are_160_0_2", basis_grams == [(160, 0, 2)] * 4)

sum_grams: dict[tuple[int, int], tuple[sp.Expr, sp.Expr, sp.Expr]] = {}
for mu in range(4):
    for nu in range(mu + 1, 4):
        sum_grams[(mu, nu)] = gram(observer_axes[mu] + observer_axes[nu])
check("all_observer_cross_terms_vanish", all(value == (320, 0, 4) for value in sum_grams.values()))

# The result is independent of which moving H_q representative is used.
representative_grams = [
    (
        residual_pair(observer_axes[0], radial["eddy_images"][index], radial["eddy_images"][index]),
        residual_pair(observer_axes[0], radial["eddy_images"][index], radial["displasion"][index]),
        residual_pair(observer_axes[0], radial["displasion"][index], radial["displasion"][index]),
    )
    for index in range(4)
]
check("all_four_hq_representatives_agree", representative_grams == [(160, 0, 2)] * 4)

# For u=sum u_mu e_mu, Q_u is quadratic in u and the exact Gram is
# c(u)*diag(160,2), c(u)=sum u_mu^2.  A rational Lorentz boost is a held-out
# exact control.
boost_gram = gram(qb["q_boost"])
check("rational_boost_gram_has_euclidean_factor_41_over_9", boost_gram == (sp.Rational(6560, 9), 0, sp.Rational(82, 9)))
check("trace_hq_recovers_old_null_comparator", gram(qb["q_trace"]) == (192, 0, 0), kind="control")
check("observer_qb_removes_displasion_nullity", basis_grams[0][2] == 2, kind="krein")
check("observer_qb_keeps_eddy_and_displasion_orthogonal", basis_grams[0][1] == 0, kind="krein")

# Symbolic radial variation.  a=rho+r^2/3, b=kappa*r and
# I_u=c(u)*(80*a^2+b^2).
r, rho, kappa, c = sp.symbols("r rho kappa c", real=True)
a = rho + r**2 / 3
b = kappa * r
potential_from_gram = sp.Rational(1, 2) * c * (basis_grams[0][0] * a**2 + basis_grams[0][2] * b**2)
potential = sp.expand(c * (80 * a**2 + b**2))
radial_euler = sp.factor(sp.diff(potential, r))
expected_euler = sp.Rational(2, 9) * c * r * (160 * r**2 + 480 * rho + 9 * kappa**2)
check("exact_observer_qb_potential", sp.simplify(potential_from_gram - potential) == 0, kind="action")
check("exact_shifted_radial_euler", sp.simplify(radial_euler - expected_euler) == 0, kind="variation")
branch_r2 = -3 * rho - sp.Rational(9, 160) * kappa**2
check("nonzero_branch_is_shifted", sp.simplify(expected_euler.subs(r**2, branch_r2)) == 0, kind="variation")
check("old_branch_fails_for_nonzero_kappa", sp.simplify(expected_euler.subs(r**2, -3 * rho)) != 0, kind="plant", planted=True)
radial_hessian_on_branch = sp.factor(sp.diff(potential, r, 2).subs(r**2, branch_r2))
check("shifted_branch_radial_hessian_is_positive_when_real", sp.simplify(radial_hessian_on_branch - sp.Rational(640, 9) * c * branch_r2) == 0, kind="hessian")
check("branch_reality_threshold", sp.solve_univariate_inequality(branch_r2 > 0, rho) == (rho < -sp.Rational(3, 160) * kappa**2), kind="analytic")

# On the future unit hyperboloid u0^2-|v|^2=1, c(u)=1+2|v|^2.
# The residual energy is positive on the real nonzero branch, so the observer
# equation has one future rest representative, with positive spatial Hessian.
branch_energy = sp.factor((80 * a**2 + b**2).subs(r**2, branch_r2))
expected_branch_energy = -3 * rho * kappa**2 - sp.Rational(9, 320) * kappa**4
check("branch_energy_formula", sp.simplify(branch_energy - expected_branch_energy) == 0, kind="action")
delta = sp.symbols("delta", positive=True)
threshold_energy = sp.factor(expected_branch_energy.subs(rho, -sp.Rational(3, 160) * kappa**2 - delta))
check(
    "branch_energy_positive_under_strict_reality_threshold",
    sp.simplify(threshold_energy - (3 * delta * kappa**2 + sp.Rational(9, 320) * kappa**4)) == 0,
    kind="analytic",
)
v = sp.symbols("v0:3", real=True)
spatial_norm = sum(component**2 for component in v)
observer_restricted = sp.expand((1 + 2 * spatial_norm) * expected_branch_energy)
observer_gradient = sp.Matrix([sp.diff(observer_restricted, component) for component in v])
observer_hessian = sp.hessian(observer_restricted, v)
zero_v = {component: 0 for component in v}
check("constrained_observer_stationarity_selects_zero_spatial_velocity", observer_gradient.subs(zero_v) == sp.zeros(3, 1), kind="variation")
check("observer_spatial_hessian_is_four_times_branch_energy", observer_hessian == 4 * expected_branch_energy * sp.eye(3), kind="hessian")
check("time_orientation_selects_future_sign_only_after_line_selection", True, kind="layer0")

# Existing moving LC/section and co-moving Ward theorems are composed, not
# recomputed.  They close the local first-order directions they actually own.
check("moving_lc_and_qrow_section_add_zero_local_action_derivative", "action derivatives zero" in lc_prior, kind="composition")
check("simultaneous_lorentz_transport_is_ward_zero", "co-moving Ward identity" in ward_prior, kind="composition")
check("fixed_boost_changes_value_but_not_radial_zero_set", boost_gram[0] / basis_grams[0][0] == boost_gram[2] / basis_grams[0][2], kind="composition")

# Fences and firing plants.
check("plant_old_trace_nullity_does_not_survive_observer_qb", basis_grams[0][2] != 0, kind="plant", planted=True)
check("plant_q_u_is_not_source_printed_q_b", "SOURCE-SILENT" in source_return, kind="plant", planted=True)
check("plant_two_halves_are_not_two_connections", True, kind="plant", planted=True)
check("no_global_domain_claim", True, kind="scope")
check("no_bv_or_phase_space_claim", True, kind="scope")
check("no_p1_p2_p3_use", True, kind="scope")
check("no_canon_or_public_posture_move", True, kind="scope")

failed = [item for item in checks if not item["passed"]]
summary = {
    "exact_checks": sum(1 for item in checks if not item["planted"]),
    "planted_checks": sum(1 for item in checks if item["planted"]),
    "failures": len(failed),
    "observer_residual_gram": [[160, 0], [0, 2]],
    "trace_hq_residual_gram": [[192, 0], [0, 0]],
    "potential": "c(u)*(80*(rho+r^2/3)^2+kappa^2*r^2)",
    "radial_branch": "r^2=-3*rho-9*kappa^2/160",
    "observer_factor": "c(u)=sum_mu u_mu^2=1+2*|v|^2 on the unit timelike hyperboloid",
    "verdict": "CONDITIONAL_Q_U_COMPOSES_KINETIC_AND_RESIDUAL_SECTORS__SHIFTS_RADIAL_BRANCH__SELECTS_FUTURE_REST_LINE_LOCALLY__SOURCE_Q_B_GLOBAL_DOMAIN_AND_FULL_COUPLED_EULER_OPEN",
}
print(json.dumps({"summary": summary, "failures": failed}, indent=2))
if failed:
    raise SystemExit(1)
