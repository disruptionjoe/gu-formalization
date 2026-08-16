#!/usr/bin/env python3
"""Historical K115 certificate; concrete fingerprint superseded by K116.

The abstract local moving-frame ODE classification survives.
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
K114_PROBE = ROOT / "tests/channel-swings/selected_k114_rsap_tt_alpha_normalization_invariant_owner_gate_probe.py"
REGISTRY = ROOT / "lab/process/selected-k115-rsap-tt-moving-jacobian-classification-and-gap-wall-gate.json"
RESULT = ROOT / "explorations/conditional-build/selected-k115-rsap-tt-moving-jacobian-classification-and-gap-wall-gate-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k115-rsap-tt-moving-jacobian-classification-and-gap-wall-gate-review.md"
K114 = ROOT / "lab/process/selected-k114-rsap-tt-alpha-normalization-invariant-owner-gate.json"
K113 = ROOT / "lab/process/selected-k113-rsap-tt-spectral-transport-normal-form-and-boundary-support-gate.json"
SOURCE_PACKET = ROOT / "explorations/unified-source-datum-packet-v0-2026-07-30.md"
COEFFICIENT_CENSUS = ROOT / "explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md"
ABSORBED_SOURCE = ROOT / "absorbed/gu-source-action"
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
        runpy.run_path(str(K114_PROBE), run_name="__main__")
    except SystemExit as error:
        code = error.code
check("predecessor", "K114 and its complete predecessor chain replay cleanly",
      code == 0 and '"checks": 35' in output.getvalue()
      and '"failures": []' in output.getvalue())
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. CONNECTION AND COMPLETE LOCAL FRAME CLASS")
alpha, b, u, u0 = sp.symbols("alpha b u u0", real=True)
K = sp.Matrix([[alpha, 1], [1, 0]])
G = sp.Matrix([[-1, 0], [alpha, 1]])
R = alpha**2 * b + (alpha - 2)**2 * u
R0 = alpha**2 * b + (alpha - 2)**2 * u0
phi = sp.log((b + u) / R) / 4
phi0 = sp.log((b + u0) / R0) / 4
g = sp.simplify(sp.diff(phi, u))
delta = sp.symbols("delta", real=True)
E = sp.cosh(delta) * sp.eye(2) + sp.sinh(delta) * G
Einv = sp.cosh(delta) * sp.eye(2) - sp.sinh(delta) * G

check("generator", "G is an involution", G * G == sp.eye(2))
check("generator", "G is traceless with determinant minus one",
      sp.trace(G) == 0 and G.det() == -1)
check("generator", "G is K-skew", G.T * K + K * G == sp.zeros(2))
check("rapidity", "dphi/du equals the K113 rational coefficient",
      sp.simplify(g - b * (alpha - 1) / ((b + u) * R)) == 0)
check("exponential", "the closed exponential and inverse multiply to identity",
      sp.simplify(E * Einv) == sp.eye(2))
check("exponential", "the exponential derivative is E times G",
      sp.simplify(sp.diff(E, delta) - E * G) == sp.zeros(2))
check("frame", "the moving-frame Maurer-Cartan form is G dphi",
      sp.simplify(Einv * sp.diff(E, delta) - G) == sp.zeros(2))
check("transport", "the inverse frame solves parallel transport",
      sp.simplify(sp.diff(Einv, delta) + G * Einv) == sp.zeros(2))
check("classification", "the class has no new functional freedom",
      load(REGISTRY)["complete_local_adapter_class"]["new_functional_freedom"] == 0)


print("\nC. INVARIANT OWNER FINGERPRINT")
check("volume", "the moving frame has unit determinant", sp.simplify(E.det()) == 1)
check("Krein", "the moving frame preserves K", sp.simplify(E.T * K * E - K) == sp.zeros(2))
check("spectrum", "moving eigenvalues are exp plus/minus rapidity",
      E.eigenvals() == {sp.exp(delta): 1, sp.exp(-delta): 1})
ratio_squared = sp.simplify(sp.exp(4 * (phi - phi0)))
check("spectrum", "the squared eigenvalue ratio is the exact rational cross-ratio",
      sp.simplify(ratio_squared - ((b + u) * R0) / (R * (b + u0))) == 0)
v_minus = sp.Matrix([1, -alpha / 2])
v_plus = sp.Matrix([0, 1])
check("eigenline", "G has the fixed minus eigenline", G * v_minus == -v_minus)
check("eigenline", "G has the fixed plus eigenline", G * v_plus == v_plus)


print("\nD. GAP-WALL AND COMMUTING CONTROLS")
check("wall", "the b+u wall sends exp(2 delta_phi) to zero generically",
      sp.limit(sp.sqrt((b + u) * R0 / (R * (b + u0))), u, -b, dir="+") == 0)
wall_R = sp.simplify(-alpha**2 * b / (alpha - 2)**2)
ratio = sp.sqrt((b + u) * R0 / (R * (b + u0)))
check("wall", "the R wall makes the eigenvalue ratio unbounded generically",
      sp.limit(ratio.subs({alpha: 3, b: 1, u0: 0}), u, wall_R.subs({alpha: 3, b: 1}), dir="-") == sp.oo)
check("wall", "the registry forbids only a bounded invertible same-frame extension",
      load(REGISTRY)["gap_wall_gate"]["bounded_invertible_same_frame_extension"] is False)
check("control", "alpha one makes R=b+u and phi identically zero",
      sp.simplify(R.subs(alpha, 1) - (b + u)) == 0
      and sp.simplify(phi.subs(alpha, 1)) == 0)
check("control", "a constant background has identity transport",
      sp.simplify(E.subs(delta, 0) - sp.eye(2)) == sp.zeros(2))


print("\nE. SERIALIZED SOURCE/ACTION OWNER AUDIT")
registry = load(REGISTRY)
k113 = load(K113)
k114 = load(K114)
source_packet = SOURCE_PACKET.read_text(encoding="utf-8")
census = COEFFICIENT_CENSUS.read_text(encoding="utf-8")
absorbed_text = "\n".join(
    path.read_text(encoding="utf-8", errors="ignore")
    for path in sorted(ABSORBED_SOURCE.rglob("*")) if path.is_file()
)
check("ownership", "alpha_II remains reconstructed coefficient U7",
      "alpha_{II}" in source_packet and "**U7**" in census and "`alpha_II`" in census)
check("ownership", "the absorbed source custody does not name alpha_II",
      "alpha_II" not in absorbed_text and "alpha_{II}" not in absorbed_text)
check("ownership", "K113 records no released moving-TT adapter",
      k113["ownership"]["released_action_moving_TT_jacobian"] == "NOT_CONSTRUCTED")
check("ownership", "K114 retains the generic-alpha adapter target",
      k114["ownership"]["generic_alpha_K113_transport_target"] == "RETAINED")
check("ownership", "the current matching serialized owner count is zero",
      registry["serialized_owner_audit"]["current_matching_source_action_owner_count"] == 0)
check("ceiling", "stationary background and physical cohomology remain open",
      registry["ceilings"]["stationary_moving_background"] == "NOT_CONSTRUCTED"
      and registry["ceilings"]["physical_BFV_cohomology"] == "OPEN")
check("routing", "the result is source-native and changes no ledger",
      registry["comparator_routing_classification"] == "SOURCE_NATIVE_ROUTE"
      and registry["disposition"]["ledger_change"] == "none")


print("\nF. ROADMAP AND SUCCESSOR CLOSURE")
current_text = CURRENT.read_text(encoding="utf-8")
next_text = NEXT.read_text(encoding="utf-8-sig")
context_text = CONTEXT.read_text(encoding="utf-8")
k114_result = (ROOT / "explorations/conditional-build/selected-k114-rsap-tt-alpha-normalization-invariant-owner-gate-2026-08-15.md").read_text(encoding="utf-8")
check("roadmap", "CURRENT records K115 as concretely superseded by K116",
      "K115" in current_text and "superseded" in current_text.lower() and "K116" in current_text)
check("roadmap", "NEXT blocks reuse of the historical K115 fingerprint",
      "K115" in next_text and "SUPERSEDED IN CONCRETE FORM BY K116" in next_text)
check("roadmap", "context routes owner work to the corrected K116 target",
      "K115" in context_text and "Do not run an owner census" in context_text and "K116" in context_text)
check("successor", "K114 records the K115 successor closure",
      "Successor closure (K115)" in k114_result)


summary = {"checks": sum(COUNTS.values()), "failures": FAILURES,
           "by_kind": dict(COUNTS)}
print("\n" + json.dumps(summary, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
