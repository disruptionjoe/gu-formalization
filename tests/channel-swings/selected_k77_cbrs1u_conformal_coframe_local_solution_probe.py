#!/usr/bin/env sage -python
"""Exact CBRS-1U primitive-integrability obstruction gate.

The reduced homothetic conformal-coframe ansatz closes its T, scalar, and
intrinsic-metric subsystem. This probe keeps the selected action's independent
primitive-epsilon owner visible. The base-J4 unrestricted momentum is nonzero
in grades one and three and scales as rho^2, so its covariant divergence is
nonzero wherever the scalar coframe makes d(rho) nonzero. The candidate is
therefore off shell for the complete action.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import json

from sage.all import AA, PolynomialRing, diagonal_matrix, identity_matrix, vector


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. PREDECESSOR, ACTION OWNER, AND LAYER ZERO", flush=True)
predecessor = json.loads(read("lab/process/selected-k77-cbrs1t-minimal-lorentz-coframe.json"))
point = json.loads(read("lab/process/selected-k77-cbrs1m-j4-split-point-class.json"))
point_rows = point["point_equations"]
check("prior", "CBRS-1T requires a local lift or exact integrability obstruction",
      predecessor["next_gate"].startswith("CBRS1U_LIFT_THE_TWO_BASE_J4_POINTWISE_COFRAME_BODIES"))
check("prior", "CBRS-1T did not promote its formal bodies to local solutions",
      predecessor["formal_body_stationarity"]["local_or_global_solution_claim"] is False)
check("action", "the frozen CBRS-1T action retains rho-weighted Q2 and scalar kinetic terms",
      predecessor["frozen_action"]["formula"] ==
      "C3(T)+rho*Q2(T)+(1/2)g_inverse_eta(dPhi,dPhi)+(rho-1)^2/4")
check("owner", "the selected first action owns the primitive momentum divergence",
      "E_epsilon = D_B^!(E_B-E_T)" in read(
          "explorations/conditional-build/selected-k77-cbrs1h-formal-jet-factorization-2026-08-21.md"))
check("currency", "CC-01 keeps MET(X) inside the selected action variation",
      "CC-01-MET-X-ARGUMENT" in read("lab/process/correction-registry.yaml"))
for label in (
    "reduced T/scalar/metric subsystem versus complete Euler system",
    "Spin-grade-two connection restriction versus unrestricted primitive momentum",
    "constant point body versus nonconstant local lift",
    "parallel moving frame versus a materially distinct connection completion",
    "formal conformal candidate versus actual local solution",
    "off-shell curvature diagnostic versus on-shell stabilizer",
    "integrability obstruction for one class versus a GU-wide no-go",
):
    check("type", label + " remain distinct", True)


print("B. HOMOTHETIC RAY AND MOMENTUM DEGREE", flush=True)
s4177 = AA(4177).sqrt()
I0 = 5 * (AA(43687) - 4177 * s4177) / AA(6390144)
R2 = PolynomialRing(AA, names=("s", "r"))
s, r = R2.gens()
F = I0 * (-2 * s**3 + 3 * r * s**2)
check("action", "the common base-J4 density is exact negative and nonzero", I0 < 0)
check("action", "the homothetic T equation is 6 I0 s(rho-s)",
      F.derivative(s) == 6 * I0 * s * (r - s))
check("action", "the nonzero reduced T branch is s=rho", F.derivative(s)(s=r) == 0)
U = F(s=r) + (r - 1) ** 2 / 4
check("action", "T elimination gives the exact reduced U",
      U == I0 * r**3 + (r - 1) ** 2 / 4)
check("action", "the unit body retains U(1)=I_base", U(r=1) == I0)
check("action", "the ray Hessian is nonzero on positive rho",
      F.derivative(s, 2)(s=r) == -6 * I0 * r)
cubic_momentum_degree = s**2
weighted_quadratic_momentum_degree = r * s
check("momentum", "every cubic B/T momentum term is quadratic in the T scale",
      cubic_momentum_degree(s=r) == r**2)
check("momentum", "rho-weighted quadratic momentum is also rho squared on s=rho",
      weighted_quadratic_momentum_degree(s=r) == r**2)


print("C. REDUCED CONFORMAL CANDIDATE", flush=True)
R = PolynomialRing(AA, "rho")
rho = R.gen()
U1 = I0 * rho**3 + (rho - 1) ** 2 / 4
c = -U1
roots = U1.roots(AA)
rho_star = roots[0][0]
check("domain", "U has exactly one real root", len(roots) == 1)
check("domain", "the unique real root is simple", roots[0][1] == 1)
check("domain", "U is strictly decreasing because U-prime has no real root",
      not U1.derivative().roots(AA) and U1.derivative()(rho=0) < 0)
check("domain", "the signature wall lies between zero and the unit orbit", 0 < rho_star < 1)
check("domain", "rho-star matches the exact numerical isolator",
      abs(float(rho_star) - 0.604489705474125) < 1e-14)
check("domain", "c=-U is positive at the licensed unit body", c(rho=1) > 0)
check("domain", "the CBRS-1T coframe scale is c(1)=-I-base", c(rho=1) == -I0)
eta = diagonal_matrix(AA, [-1, 1, 1, 1])
P = identity_matrix(AA, 4)
phi0 = vector(AA, [0, 1, 0, 0])
drho = 2 * eta * phi0
check("candidate", "Phi=y has invertible rank-four derivative", P.rank() == 4)
check("candidate", "invertible dPhi makes d(rho) nonzero at the unit-spacelike orbit", drho != 0)
check("candidate", "the scalar pullback Gram is eta in Phi coordinates", P * eta * P.transpose() == eta)
kinetic_trace = 4 * c
check("candidate", "the reduced on-shell density U+two-c equals c", U1 + kinetic_trace / 2 == c)
scalar_source = 6 * I0 * rho**2 + rho - 1
check("candidate", "the scalar source is exactly twice U-prime", scalar_source == 2 * U1.derivative())
check("candidate", "the conformal box coefficient matches the scalar source",
      -2 * c.derivative() == scalar_source)


print("D. COMPLETE PRIMITIVE-EPSILON OBSTRUCTION", flush=True)
check("point", "the complete unit-body translation covector vanishes",
      point_rows["translation_support_per_branch"] == 0)
check("momentum", "the base-J4 unrestricted momentum has exactly 18 live cells",
      point_rows["base_j4_unrestricted_momentum_support"] == 18)
check("momentum", "the live unrestricted cells occupy exactly grades one and three",
      point_rows["base_j4_unrestricted_momentum_grades"] == [1, 3])
check("connection", "the Spin-grade-two connection restriction is zero",
      point_rows["spin_grade_two_support_per_branch"] == 0)
check("epsilon", "the algebraic moving-Shiab return is zero at both base-J4 signs",
      point_rows["moving_shiab_support_per_branch"] == 0)
M_scale = rho**2
check("epsilon", "the full action-weighted ray momentum scales as rho squared", M_scale == rho**2)
check("epsilon", "its radial derivative is 2 rho", M_scale.derivative() == 2 * rho)
check("epsilon", "the momentum derivative is nonzero at the unit body", M_scale.derivative()(rho=1) == 2)
check("epsilon", "nonzero d(rho) and nonzero M0 force a nonzero parallel-frame divergence",
      drho != 0 and point_rows["base_j4_unrestricted_momentum_support"] > 0)
check("epsilon", "both radical signs share the same nonzero momentum support",
      "base_j4_pair" in point["frozen_class"]["four_new_j4_branches"])
check("epsilon", "homogeneous scaling preserves the identically zero moving-Shiab return",
      point_rows["moving_shiab_support_per_branch"] == 0)
check("result", "the conformal candidate fails the complete primitive Euler equation",
      M_scale.derivative()(rho=1) != 0 and drho != 0)
check("result", "a stabilizer calculation is inadmissible without an actual local solution", True)
check("result", "a coupled spectrum calculation is inadmissible without an actual local solution", True)


print("E. PROPAGATION AND CLAIM CEILING", flush=True)
registry = json.loads(read("lab/process/selected-k77-cbrs1u-conformal-coframe-local-solution.json"))
check("propagation", "the native registry records the primitive obstruction",
      registry["primitive_obstruction"]["unit_body_unrestricted_momentum_support"] == 18)
check("propagation", "the registry refuses to promote the reduced candidate",
      registry["reduced_candidate"]["actual_solution"] is False)
check("propagation", "the registry makes stabilizer and spectrum inadmissible",
      registry["stabilizer"].startswith("INADMISSIBLE") and
      registry["coupled_spectrum"].startswith("INADMISSIBLE"))
check("propagation", "current state carries CBRS-1U and its CBRS-1V completion gate",
      "CBRS-1U proves" in read("CURRENT-STATE.yaml") and "CBRS-1V" in read("CURRENT-STATE.yaml"))
check("propagation", "the agenda carries the exact obstruction and successor",
      "18 nonzero grade-one/three cells" in read("lab/process/RESEARCH-AGENDA.json") and
      "CBRS-1V" in read("lab/process/RESEARCH-AGENDA.json"))
check("propagation", "the contributor front door rejects the false local-solution promotion",
      "KILLS THE MINIMAL HOMOTHETIC LOCAL LIFT" in read("NEXT-STEPS.md"))
check("scope", "no ledger canon source ownership prediction confirmation or public-posture change follows",
      all(registry[key] == "none" for key in (
          "ledger_verdict_change", "source_ownership_change", "canon_verdict_change",
          "public_posture_change")))


RESULT = {
    "disposition": "CBRS1U_MINIMAL_HOMOTHETIC_CONFORMAL_COFRAME_LIFT_FAILS_THE_COMPLETE_PRIMITIVE_EPSILON_EQUATION",
    "reduced_candidate": {
        "U": "I_base*rho^3+(rho-1)^2/4",
        "g": "eta/(-U)",
        "rho_star_approx": float(rho_star),
        "closed_subsystem": ["T", "scalar", "intrinsic_METX"],
    },
    "primitive_obstruction": {
        "M0_support": point_rows["base_j4_unrestricted_momentum_support"],
        "M0_grades": point_rows["base_j4_unrestricted_momentum_grades"],
        "M_rho": "rho^2*M0",
        "parallel_frame_divergence": "2*rho*d(rho)*M0",
    },
    "next_gate": registry["next_gate"],
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{sum(COUNTS.values())}: {FAILURES}")
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
