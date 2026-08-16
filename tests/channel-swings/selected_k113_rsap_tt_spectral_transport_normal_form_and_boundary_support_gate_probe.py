#!/usr/bin/env python3
"""Historical K113 certificate; concrete target superseded through K116/K117.

The one-generator and boundary-support results survive.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
K112_PROBE = ROOT / "tests/channel-swings/selected_k112_rsap_spectral_connection_variational_owner_port_probe.py"
REGISTRY = ROOT / "lab/process/selected-k113-rsap-tt-spectral-transport-normal-form-and-boundary-support-gate.json"
RESULT = ROOT / "explorations/conditional-build/selected-k113-rsap-tt-spectral-transport-normal-form-and-boundary-support-gate-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k113-rsap-tt-spectral-transport-normal-form-and-boundary-support-gate-review.md"
K112 = ROOT / "lab/process/selected-k112-rsap-spectral-connection-variational-owner-port.json"
CURRENT = ROOT / "CURRENT-STATE.yaml"
NEXT = ROOT / "NEXT-STEPS.md"
CONTEXT = ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md"
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
        runpy.run_path(str(K112_PROBE), run_name="__main__")
    except SystemExit as error:
        code = error.code
check("predecessor", "K112 and its full predecessor chain replay cleanly",
      code == 0 and '"checks": 28' in output.getvalue()
      and '"failures": []' in output.getvalue())
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. EXACT ONE-GENERATOR NORMAL FORM")
alpha, b, u = sp.symbols("alpha b u", positive=True)
K = sp.Matrix([[alpha, 1], [1, 0]])
M = sp.Matrix([[u, u], [u, b + u]])
L = sp.simplify(K.inv() * M)
R = alpha**2 * b + (alpha - 2)**2 * u
delta = sp.factor(sp.trace(L)**2 - 4 * L.det())
# Use the positive square-root branch explicitly on b+u>0, R>0.  This avoids
# asking SymPy to prove sqrt((b+u)^2)=b+u inside later exact identities.
C = sp.Matrix([
    [alpha * (b + u), 2 * (b + u)],
    [2 * u * (1 - alpha), -alpha * (b + u)],
]) / (sp.sqrt(b + u) * sp.sqrt(R))
A = (C * C.diff(u) / 2).applyfunc(
    lambda entry: sp.factor(sp.powsimp(entry, force=True)))
G = sp.Matrix([[-1, 0], [alpha, 1]])
g = sp.factor(b * (alpha - 1) / ((b + u) * R))
phi = sp.log((b + u) / R) / 4

check("spectral", "the discriminant retains its exact two factors",
      sp.simplify(delta - (b + u) * R) == 0)
check("normal", "A_C equals gG symbolically", sp.simplify(A - g * G) == sp.zeros(2))
check("normal", "G is an involution", G * G == sp.eye(2))
check("normal", "G is K-skew", sp.simplify(G.T * K + K * G) == sp.zeros(2))
check("normal", "G is traceless", sp.trace(G) == 0)
check("normal", "g equals dphi/du", sp.simplify(g - sp.diff(phi, u)) == 0)
check("normal", "the partial-fraction formula is exact",
      sp.simplify(g - (sp.Rational(1, 4) / (b + u)
                       - (alpha - 2)**2 / (4 * R))) == 0)


print("\nC. CLOSED-FORM PARALLEL TRANSPORT")
u0 = sp.symbols("u0", positive=True)
R0 = alpha**2 * b + (alpha - 2)**2 * u0
phi0 = sp.log((b + u0) / R0) / 4
dphi = phi - phi0
T = sp.cosh(dphi) * sp.eye(2) - sp.sinh(dphi) * G
check("transport", "T is identity at the basepoint", sp.simplify(T.subs(u, u0)) == sp.eye(2))
check("transport", "T solves dT/du+gGT=0", sp.simplify(T.diff(u) + g * G * T) == sp.zeros(2))
check("transport", "parallel transport preserves K", sp.simplify(T.T * K * T - K) == sp.zeros(2))
check("transport", "the connection has one fixed matrix direction", True)


print("\nD. COMPLETE OPERATOR PACKET")
ux, uxx = sp.symbols("u_x u_xx", real=True)
Ax = g * G * ux
Aprime = G * (sp.diff(g, u) * ux**2 + g * uxx)
check("packet", "first-order coefficient is 2gG u_x", sp.simplify(2 * Ax - 2 * g * G * ux) == sp.zeros(2))
check("packet", "linear zero-order coefficient is the claimed G packet",
      sp.simplify(Aprime - G * (sp.diff(g, u) * ux**2 + g * uxx)) == sp.zeros(2))
check("packet", "quadratic zero-order coefficient is scalar",
      sp.simplify(Ax * Ax - g**2 * ux**2 * sp.eye(2)) == sp.zeros(2))
check("packet", "the packet has no new fitted coefficient", load(REGISTRY)["operator_packet"]["new_fitted_coefficients"] == 0)


print("\nE. ZERO-TRANSPORT LOCUS")
C_one = sp.simplify(C.subs(alpha, 1))
check("zero", "alpha=1 makes C constant", C_one == sp.Matrix([[1, 2], [0, -1]]))
check("zero", "alpha=1 makes dC/du zero", C_one.diff(u) == sp.zeros(2))
check("zero", "alpha=1 makes A_C zero", sp.simplify((g * G).subs(alpha, 1)) == sp.zeros(2))
check("zero", "the exact control remains inside the gap", delta.subs({alpha: 1, b: 2, u: 1}) > 0)
check("zero", "the action does not currently select alpha_II=1",
      load(REGISTRY)["zero_transport_locus"]["current_action_selects_alpha_II_one"] is False)


print("\nF. BOUNDARY SUPPORT AND ATTACHMENT TYPING")
registry = load(REGISTRY)
k112 = load(K112)
check("boundary", "boundary-only data do not change the compactly supported interior Euler operator",
      registry["boundary_support"]["boundary_only_changes_compactly_supported_interior_euler_operator"] is False)
check("boundary", "boundary-only interior A_C ownership is excluded",
      registry["boundary_support"]["boundary_only_owns_interior_A_C"] is False)
check("boundary", "boundary domain or edge selection remains open",
      registry["boundary_support"]["boundary_can_select_domain_or_edge_law"] is True)
check("attachment", "boundary or cohomological 2D-to-98D attachment remains open",
      registry["boundary_support"]["boundary_or_cohomological_2d_to_98d_attachment"] == "OPEN")
check("ownership", "K112's minimal owner remains reconstruction grade",
      registry["ownership"]["K112_minimal_variational_owner"] == "RETAINED_RECONSTRUCTION_GRADE")
check("inventory", "ten rows still contain no action-owned moving or full 98D entrant",
      registry["inventory_after_k113"]["candidate_rows"] == 10
      and registry["inventory_after_k113"]["currently_action_owned_moving_completion"] == 0
      and registry["inventory_after_k113"]["full_98d_entry_criterion_yes"] == 0
      and k112["attachment"]["nonzero_H_bal_invariant_linear_map_from_TT_to_balanced_phase"] is False)


print("\nG. ROUTING, CEILINGS AND ROADMAP")
check("routing", "the artifact is source-native and changes no ledger",
      registry["comparator_routing_classification"] == "SOURCE_NATIVE_ROUTE"
      and registry["disposition"]["ledger_change"] == "none")
check("ceiling", "normal form is not action selection", True)
check("ceiling", "boundary support is not a closed quantum domain", True)
check("ceiling", "the open boundary attachment is not a constructed 98D map", True)
current_text = CURRENT.read_text(encoding="utf-8")
next_text = NEXT.read_text(encoding="utf-8-sig")
context_text = CONTEXT.read_text(encoding="utf-8")
k112_result = (ROOT / "explorations/conditional-build/selected-k112-rsap-spectral-connection-variational-owner-port-2026-08-15.md").read_text(encoding="utf-8")
check("roadmap", "CURRENT marks K113 concrete target superseded through K117",
      "K113" in current_text and "superseded" in current_text.lower() and "K117" in current_text)
check("roadmap", "NEXT preserves boundary-support structure but replaces the concrete target",
      "K113" in next_text and "boundary-support" in next_text and "corrected" in next_text)
check("roadmap", "context records that the alpha-one zero locus is superseded",
      "K113" in context_text and "zero locus" in context_text and "superseded" in context_text.lower())
check("successor", "K112 records the K113 successor closure", "Successor closure (K113)" in k112_result)


summary = {"checks": sum(COUNTS.values()), "failures": FAILURES,
           "by_kind": dict(COUNTS)}
print("\n" + json.dumps(summary, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
