#!/usr/bin/env python3
"""Exact K112 spectral-connection variational owner and attachment gate."""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
K111_PROBE = ROOT / "tests/channel-swings/selected_k111_rsap_tt_spectral_transport_connection_owner_gate_probe.py"
REGISTRY = ROOT / "lab/process/selected-k112-rsap-spectral-connection-variational-owner-port.json"
RESULT = ROOT / "explorations/conditional-build/selected-k112-rsap-spectral-connection-variational-owner-port-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k112-rsap-spectral-connection-variational-owner-port-review.md"
K111 = ROOT / "lab/process/selected-k111-rsap-tt-spectral-transport-connection-owner-gate.json"
K107 = ROOT / "lab/process/selected-k107-rsap-phase-space-compatible-complex-positivity.json"
K105 = ROOT / "lab/process/selected-k105-rsap-curvature-sign-owner-qualification.json"
K104 = ROOT / "lab/process/selected-k104-rsap-source-boundary-variational-owner-census.json"
K98 = ROOT / "lab/process/selected-k98-rsap-balanced-bfv-selection-classifier.json"
CURRENT = ROOT / "CURRENT-STATE.yaml"
NEXT = ROOT / "NEXT-STEPS.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


print("A. PREDECESSOR AND DURABLE FILES")
output = io.StringIO()
code = None
with contextlib.redirect_stdout(output):
    try:
        runpy.run_path(str(K111_PROBE), run_name="__main__")
    except SystemExit as error:
        code = error.code
check("predecessor", "K111 and its full predecessor chain replay cleanly",
      code == 0 and '"checks": 40' in output.getvalue()
      and '"failures": []' in output.getvalue())
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. K111 SPECTRAL FAMILY")
alpha, b, u = sp.symbols("alpha b u", real=True)
K = sp.Matrix([[alpha, 1], [1, 0]])
M0 = sp.Matrix([[0, 0], [0, b]])
v = sp.Matrix([1, 1])
M = M0 + u * v * v.T
L = sp.simplify(K.inv() * M)
trace = sp.factor(sp.trace(L))
delta = sp.factor(trace**2 - 4 * L.det())
C = sp.simplify((2 * L - trace * sp.eye(2)) / sp.sqrt(delta))
Cp = sp.simplify(C.diff(u))
A = sp.simplify(C * Cp / 2)
Ap = sp.simplify(A.diff(u))
H = sp.simplify(K * C)
sample = {alpha: sp.Rational(3, 2), b: 2, u: 1}
Ks = K.subs(sample)
Ms = M.subs(sample)
Ls = sp.simplify(L.subs(sample))
Cs = sp.simplify(C.subs(sample))
As = sp.simplify(A.subs(sample))
Aps = sp.simplify(Ap.subs(sample))
Hs = sp.simplify(H.subs(sample))
check("spectral", "sample is gapped and on the free-connected component",
      delta.subs(sample) > 0 and (b + u).subs(sample) > 0)
check("spectral", "C is involutive and K-self-adjoint",
      Cs * Cs == sp.eye(2) and Cs.T * Ks == Ks * Cs)
check("spectral", "H=KC is positive definite", Hs.is_positive_definite)
check("connection", "A_C is nonzero and K-skew",
      As != sp.zeros(2) and sp.simplify(As.T * Ks + Ks * As) == sp.zeros(2))


print("\nC. MINIMAL VARIATIONAL COMPLETION")
# For L=(1/2)(phi'+A phi)^T K(phi'+A phi)-(1/2)phi^T M phi,
# d/dx(dL/dphi')-dL/dphi has the displayed matrix coefficients.
first_euler = sp.simplify(Ks * As - As.T * Ks)
zero_connection_euler = sp.simplify(Ks * Aps - As.T * Ks * As)
check("variational", "Euler first-derivative coefficient is 2 K A",
      sp.simplify(first_euler - 2 * Ks * As) == sp.zeros(2))
check("variational", "normalized first-derivative coefficient is 2 A",
      sp.simplify(Ks.inv() * first_euler - 2 * As) == sp.zeros(2))
check("variational", "Euler zero-order connection coefficient is K(A'+A^2)",
      sp.simplify(zero_connection_euler - Ks * (Aps + As * As)) == sp.zeros(2))
check("variational", "normalized mass coefficient is the K111 pencil L=K^-1 M",
      sp.simplify(Ks.inv() * Ms - Ls) == sp.zeros(2))
check("variational", "the covariant quadratic reproduces the full D_A coefficient pattern",
      sp.simplify(Ks.inv() * zero_connection_euler - (Aps + As * As)) == sp.zeros(2))


print("\nD. BACKGROUND OWNER CEILING")
q0, q1, p0, p1 = sp.symbols("q0 q1 p0 p1", real=True)
q = sp.Matrix([q0, q1])
p = sp.Matrix([p0, p1])
cov_p = p + A * q
density = sp.expand((cov_p.T * K * cov_p)[0] / 2 - (q.T * M * q)[0] / 2)
u_source = sp.diff(density, u)
zero_fields = {q0: 0, q1: 0, p0: 0, p1: 0}
check("background", "TT quadratic u-Euler source vanishes at zero TT field",
      sp.simplify(u_source.subs(zero_fields)) == 0)
k105 = load(K105)
stationary = k105["current_stationary_carrier_census"]
check("background", "current stationary census has five classes and zero survivors",
      stationary["serialized_candidate_classes"] == 5
      and stationary["full_local_stationarity_survivors"] == 0
      and not stationary["curvature_concomitant_evaluable_on_current_eligible_stationary_carrier"])
k111 = load(K111)
check("ownership", "selected cubic owns no TT derivative connection terms",
      k111["action_owner"]["tt_derivative_hessian"] == "ZERO"
      and not k111["action_owner"]["selected_cubic_owns_A_C_terms"])


print("\nE. C-COMPATIBLE GREEN BOUNDARY FORM")
x0, x1, y0, y1, vx0, vx1, vy0, vy1 = sp.symbols(
    "x0 x1 y0 y1 vx0 vx1 vy0 vy1", real=True)
x = sp.Matrix([x0, x1])
y = sp.Matrix([y0, y1])
vx = sp.Matrix([vx0, vx1])
vy = sp.Matrix([vy0, vy1])
boundary_left = (Cs * x).T * Ks * vy - (Cs * vx).T * Ks * y
boundary_right = x.T * Ks * (Cs * vy) - vx.T * Ks * (Cs * y)
check("boundary", "C can move between Green-form slots",
      sp.simplify(boundary_left[0] - boundary_right[0]) == 0)
k98 = load(K98)
check("bfv", "finite classical BFV closes but analytic and physical domains do not",
      k98["bfv"]["classical_master_equation"] == "EXACTLY_ZERO"
      and k98["bfv"]["analytic_domain"] == "NOT_CONSTRUCTED"
      and k98["bfv"]["physical_cohomology"] == "NOT_CONSTRUCTED")
k104 = load(K104)
source = k104["source_census"]
check("bfv", "released source displays none of the balanced boundary/gauge owners",
      source["balanced_boundary_density_or_domain_law"] == "NOT_DISPLAYED"
      and source["zero_h_flux_selection"] == "NOT_DISPLAYED"
      and source["right_h_bal_gauge_declaration"] == "NOT_DISPLAYED")


print("\nF. INVARIANT LINEAR ATTACHMENT")
k107 = load(K107)
dims = k107["krein_and_constraint"]["nonzero_proper_H_invariant_linear_subquotient_dimensions"]
check("attachment", "balanced phase nonzero proper invariant subquotients are 49D", dims == [49])
check("attachment", "a nonzero invariant image of a 2D carrier is excluded", min(dims) > 2)
check("control", "non-invariant and nonlinear attachment routes remain outside this obstruction",
      k107["claim_ceiling"]["does_not_bind"].startswith("nonlinear_BFV_cohomology_noninvariant"))


print("\nG. REGISTRY, ROUTING AND CEILINGS")
registry = load(REGISTRY)
check("registry", "registry records exact reconstruction-grade variational ownership",
      registry["minimal_variational_completion"]["free_connection_coefficient_count"] == 0
      and registry["minimal_variational_completion"]["grade"].startswith("EXACT_LOCAL"))
check("registry", "registry fences reconstructed action from current source ownership",
      registry["ownership"]["mathematical_variational_owner_exists"]
      and not registry["ownership"]["released_source_action_displays_this_covariant_TT_quadratic"])
check("registry", "registry retains stationary, BFV and noninvariant attachment ceilings",
      registry["stationary_background"]["action_owned_smooth_gapped_moving_background"] == "NOT_CONSTRUCTED"
      and registry["boundary_and_bfv"]["positive_physical_cohomology"] == "NOT_CONSTRUCTED"
      and registry["attachment"]["noninvariant_background_owned_map"] == "OPEN")
result_text = RESULT.read_text(encoding="utf-8")
review_text = REVIEW.read_text(encoding="utf-8")
check("routing", "produced prose carries routing notice and declared classification",
      all("GU-COMPARATOR-ROUTING" in text and "Classification: `SOURCE_NATIVE_ROUTE`" in text
          for text in (result_text, review_text)))
check("scope", "result names the reconstructed-action and invariant-linear ceilings",
      "new reconstructed action data" in result_text.lower()
      and "invariant linear attachment obstruction" in result_text.lower())


print("\nH. CURRENT-STATE AND ROADMAP PROPAGATION")
current = CURRENT.read_text(encoding="utf-8")
roadmap = NEXT.read_text(encoding="utf-8-sig")
check("state", "current state carries K112 variational result and next owner packet",
      "K112" in current and "minimal local quadratic variational owner" in current
      and all(token in current for token in ("non-invariant", "nonlinear", "cohomological")))
check("roadmap", "roadmap carries K112 before K111", roadmap.find("K112") < roadmap.find("K111"))
check("roadmap", "roadmap blocks source-owned and physical overpromotion",
      all(token in roadmap.lower() for token in
          ("reconstruction-grade", "new action", "do not append a physical")))


print("\nSUMMARY")
summary = {"checks_by_kind": dict(sorted(COUNTS.items())), "checks": sum(COUNTS.values()), "failures": FAILURES}
print(json.dumps(summary, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
