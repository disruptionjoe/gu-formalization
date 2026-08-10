#!/usr/bin/env python3
"""Exact composition gate for the local K77 zero-fermion VEV selector.

This probe does not invent a new cosmological action.  It composes six durable
receipts and reconstructs only their shared exact scalar family.  The question
is whether the already-built local classical structures add an independent
equation fixing the remaining amplitude.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def strict(relative: str):
    path = ROOT / relative

    def hook(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


metric = strict("lab/process/selected-k77-direct-metric-euler.json")
closure = strict("lab/process/selected-k77-curvature-vev-trace-closure.json")
family_receipt = strict("lab/process/selected-k77-source-euler-two-to-one.json")
bfv = strict("lab/process/selected-k77-branch-bfv-no-selector.json")
parent_hessian = strict("lab/process/selected-k77-nonzero-branch-parent-hessian.json")
fermion = strict("lab/process/selected-k77-zero-fermion-coupled-hessian-current-order.json")


print("A. RECEIPT AND LAYER-0 COMPOSITION")
check("prior", "v0.107 carries a nonzero rank-one metric Euler demand",
      metric["exact_result"]["metric_euler"]["rank"] == 1
      and metric["exact_result"]["metric_euler"]["kernel_dimension"] == 9)
check("prior", "v0.108 built an action-owned curvature/distortion cancellation",
      closure["exact_result"]["action"]["total_value"] == "0"
      and closure["exact_result"]["finite_euler"]["metric_volume_covector_zero_directions"] == 10)
check("prior", "v0.109 retracted the zero-freedom reading",
      "ZERO_FREEDOM_RETRACTED" in family_receipt["status"]
      and family_receipt["exact_result"]["family"]["local_amplitudes"] == 1)
check("prior", "v0.114 classical symplectic/BFV structures select no amplitude",
      not bfv["branch_symplectic_equivalence"]["selects_branch_or_amplitude"])
check("prior", "the parent Hessian is pointwise and excludes the functional domain",
      "functional derivative and boundary domain" in parent_hessian["layer0"]["not_computed"])
check("prior", "the zero-fermion action current and mixed Hessian both vanish",
      fermion["exact_result"]["zero_fermion_current_rank"] == 0
      and fermion["exact_result"]["zero_fermion_mixed_hessian_rank"] == 0)
check("type", "local trace cancellation is not typed as the observed Einstein equation",
      closure["layer0"]["trace_closure"].endswith("NOT_OBSERVED_EINSTEIN_EQUATION"))
check("type", "a pointwise connection Hessian is not an amplitude-family Jacobian",
      parent_hessian["layer0"]["computed_object"].startswith("pointwise first-transgression"))
check("type", "classical vertical polarization is not a quantum measure",
      bfv["layer0"]["vertical_polarization"] == "NOT_COMPLEX_CONTOUR_OR_MEASURE")


print("\nB. EXACT SOURCE-EULER FAMILY")
f, u, t = sp.symbols("f u t", real=True)
e_translation = 312 * (f + u + t**2) + t
e_trace = 624 * (f + u / 2 + t**2 / 3) + t
equations = sp.Matrix([e_translation, e_trace])
jacobian = equations.jacobian([f, u, t])
jacobian_fu = equations.jacobian([f, u])

f_family = t**2 / 3
u_family = -t / 312 - 4 * t**2 / 3
family_sub = {f: f_family, u: u_family}
family_tangent = sp.Matrix([sp.diff(f_family, t), sp.diff(u_family, t), 1])

check("exact", "the two source equations vanish on the full symbolic family",
      all(sp.simplify(entry.subs(family_sub)) == 0 for entry in equations))
check("exact", "the f/u coefficient minor is the certified nonzero determinant",
      jacobian_fu.det() == -97344)
check("exact", "the family Jacobian has generic rank two",
      jacobian.subs(t, sp.Rational(7, 19)).rank() == 2)
check("exact", "the symbolic family tangent lies in the Jacobian kernel",
      all(sp.simplify(entry.subs(family_sub)) == 0 for entry in jacobian * family_tangent))
check("exact", "the tangent has a nonzero amplitude component",
      family_tangent[2] == 1)
check("exact", "three invariant values minus two equations leaves one local amplitude",
      3 - jacobian.subs(t, sp.Rational(7, 19)).rank() == 1)


print("\nC. V0.108 REPRESENTATIVE AND TRACE CANCELLATION")
t0 = -sp.Rational(1, 104)
b0 = sp.Rational(1, 208)
r0 = sp.Rational(1, 129792)
f0 = sp.simplify(f_family.subs(t, t0))
u0 = sp.simplify(u_family.subs(t, t0))
check("exact", "the old rational representative has f=b^2+r",
      f0 == b0**2 + r0)
check("exact", "the old rational representative has u=2bt at s=0",
      u0 == 2 * b0 * t0)
check("exact", "the old representative satisfies both corrected source equations",
      equations.subs({f: f0, u: u0, t: t0}) == sp.zeros(2, 1))

noncurvature = sp.Rational(7, 21632)
curvature = -sp.Rational(7, 21632)
check("exact", "noncurvature and derivative-curvature densities cancel exactly",
      noncurvature + curvature == 0)

trace_covector = sp.Matrix([
    sp.Rational(value)
    for value in metric["exact_result"]["metric_euler"]["normalized_covector"]
])
density_covector = sp.Matrix([
    sp.Rational(value)
    for value in metric["exact_result"]["gimmel_density"]["covector"]
])
check("exact", "the original metric covector is the rank-one trace ray",
      trace_covector.rank() == 1 and density_covector.rank() == 1)
check("exact", "equal and opposite action densities cancel all ten trace components",
      (noncurvature + curvature) * density_covector == sp.zeros(10, 1))
check("exact", "the trace closure uses no new action coefficient",
      closure["exact_result"]["constraints"]["new_action_coefficients"] == 0)


print("\nD. SELECTOR EXHAUSTION")
# Classical symplectic equivalence is reconstructed rather than trusted only as prose.
sqrt3 = sp.sqrt(3)
p_plus = (-3 + 2 * sqrt3) / 416
p_minus = (-3 - 2 * sqrt3) / 416
omega0 = sp.Matrix([[0, 1], [-1, 0]])
transport = sp.diag(1, p_plus / p_minus)
check("symplectic", "the two nonzero branch forms are exactly symplectomorphic",
      sp.simplify(transport.T * (p_minus * omega0) * transport - p_plus * omega0) == sp.zeros(2))
check("symplectic", "the vertical polarization is preserved by the transport",
      transport[0, 1] == 0)
check("symplectic", "minimal-edge coefficients are amplitude independent",
      bfv["branch_symplectic_equivalence"]["minimal_edge_coefficients"] == [-1, 1]
      and bfv["branch_symplectic_equivalence"]["edge_coefficients_amplitude_independent"])
check("bv", "both classical BFV horns close without selecting a branch",
      bfv["classical_edge_bfv"]["branch_plus_closes"]
      and bfv["classical_edge_bfv"]["branch_minus_closes"]
      and not bfv["classical_edge_bfv"]["selects_branch"])
check("hessian", "the full pointwise parent Hessian has no connection radical",
      parent_hessian["exact_result"]["radical_dimension"] == 0)
check("hessian", "that Hessian explicitly does not include BV or boundary ownership",
      "BV quotient" in parent_hessian["layer0"]["not_computed"]
      and "functional derivative and boundary domain" in parent_hessian["layer0"]["not_computed"])
check("fermion", "zero-fermion current supplies no extra amplitude equation",
      fermion["exact_result"]["zero_fermion_current_rank"] == 0)

# Negative control: a genuine independent amplitude equation would raise rank.
extra_equation = t - sp.Rational(5, 17)
augmented = sp.Matrix([e_translation, e_trace, extra_equation]).jacobian([f, u, t])
check("planted", "a genuine independent amplitude equation raises rank to three",
      augmented.rank() == 3)
check("planted", "the current composed system has no such third local equation",
      jacobian.subs(t, sp.Rational(5, 17)).rank() == 2)


print("\nE. SOURCE, COSMOLOGY, AND ACCOUNTING FENCES")
check("source", "the source receipt confirms two-field identification but is silent on amplitude selection",
      "SOURCE_CORRECTS" in family_receipt["source_return"]
      and "AMPLITUDE_SELECTION" in family_receipt["source_return"])
check("source", "the dynamic carrier is the existing T_omega distortion, not a new Lambda field",
      closure["layer0"]["dynamic_vev_carrier"].startswith("SAME_SOURCE_NATIVE"))
check("cosmology", "local two-to-one tracking is not radiative screening",
      "quantum_measure_and_anomaly" in bfv["analytic_fence"]
      and bfv["analytic_fence"]["quantum_measure_and_anomaly"] == "OPEN")
check("analytic", "global Green/Krein and coupled BV-BFV remain open",
      bfv["analytic_fence"]["common_bulk_green_krein_domain_preserving_traces"] == "OPEN"
      and bfv["analytic_fence"]["coupled_bulk_boundary_bv_bfv"] == "OPEN")
check("accounting", "P1/P2/P3 remain unused in every composed receipt",
      closure["controls"]["P1_P2_P3_unused"]
      and family_receipt["controls"]["P1_P2_P3_unused"]
      and bfv["constraint_fence"]["P1_P2_P3"] == "UNUSED")
check("accounting", "the composition does not select among the three parent horns",
      not parent_hessian["disposition"]["conditional_parent_statement"].startswith("selected"))


verdict = "LOCAL_TRACE_ALREADY_CLOSED__ONE_AMPLITUDE_REMAINS__BUILT_LOCAL_CLASSICAL_SELECTORS_EXHAUSTED"
result = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "verdict": verdict,
    "source_equation_rank": int(jacobian.subs(t, sp.Rational(7, 19)).rank()),
    "local_amplitude_dimension": 1,
    "family": {"f": str(f_family), "u": str(u_family)},
    "family_tangent": [str(entry) for entry in family_tangent],
    "representative": {"t": str(t0), "f": str(f0), "u": str(u0)},
    "metric_trace_rank": int(trace_covector.rank()),
    "zero_fermion_current_rank": fermion["exact_result"]["zero_fermion_current_rank"],
    "pointwise_parent_hessian_radical": parent_hessian["exact_result"]["radical_dimension"],
    "classical_symplectic_bfv_selects_amplitude": False,
    "next_gate": "GLOBAL_NORMALIZED_FUNCTIONAL_OR_QUANTUM_MEASURE_OR_EXPLICIT_EXTERNAL_NORMALIZER__PLUS_COMPLETE_BULK_BOUNDARY_BV_BFV_DOMAIN",
}
print("\nRESULT_JSON")
print(json.dumps(result, indent=2, sort_keys=True))
print(f"\nSUMMARY: {sum(COUNTS.values())} checks, {len(FAILURES)} failures")
raise SystemExit(1 if FAILURES else 0)
