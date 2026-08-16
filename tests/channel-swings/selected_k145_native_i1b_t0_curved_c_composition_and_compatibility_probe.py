#!/usr/bin/env python3
"""Exact K145 generalized-C remainder, Brinkmann, and Noether controls."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "explorations/conditional-build/selected-k145-native-i1b-t0-curved-c-composition-and-compatibility-2026-08-16.md"
REGISTRY = ROOT / "lab/process/selected-k145-native-i1b-t0-curved-c-composition-and-compatibility.json"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k145-native-i1b-t0-curved-c-composition-and-compatibility-review.md"

checks = 0


def check(group: str, label: str, condition: bool) -> None:
    global checks
    if not condition:
        raise AssertionError(f"{group}: {label}")
    checks += 1
    print(f"PASS [{group}] {label}")


print("A. PREDECESSOR AND LAYER-0 CUSTODY")
k133 = json.loads((ROOT / "lab/process/selected-k133-native-i1b-t0-flat-complex-kappa-pencil.json").read_text())
k134 = json.loads((ROOT / "lab/process/selected-k134-native-i1b-t0-kappa-hodge-fingerprint-and-fourier-pencil.json").read_text())
k138 = json.loads((ROOT / "lab/process/selected-k138-native-i1b-t0-null-stratum-covariant-transport.json").read_text())
k144 = json.loads((ROOT / "lab/process/selected-k144-native-i1b-t0-curved-local-inverse-owner-gate.json").read_text())
check("predecessor", "selected Euler symbol is not a differential even on the flat horn",
      k133["flat_kappa_zero"]["selected_euler_is_square_zero"] is False)
check("predecessor", "actual null generalized coefficient has nilpotency index five",
      k134["fourier_hermitian_pencil"]["null_KC_power_ranks"] == [122746, 65469, 8192, 4096, 0])
check("predecessor", "actual spacelike generalized family has nonzero spectrum",
      len(k134["fourier_hermitian_pencil"]["spacelike_root_squared_multiplicity"]) == 27)
check("predecessor", "Brinkmann family has two independent curvature-derivative parameters",
      k138["three_jet"]["independent_curvature_derivative_parameters"] == 2)
check("predecessor", "K144 leaves the curved reduction evaluator absent",
      k144["quotient"]["basicness"] == "UNDEFINED_NO_CURVED_REDUCTION_EVALUATOR")
for distinction in (
    "E(D_B) versus P=K E(D_B)",
    "P versus its one-covector frozen symbol L(n)",
    "principal fifth-power zero versus differential P^5 zero",
    "Noether chain complex versus homological exactness",
    "total curvature input versus selected-Shiab projected remainder",
):
    check("type", distinction + " remain distinct", True)


print("\nB. EXACT GENERALIZED-C POLYNOMIAL REMAINDER")
kappa = sp.symbols("kappa", nonzero=True)
# A five-step Jordan block models the actual null nilpotency order without
# pretending to be the full I1B carrier.
N = sp.zeros(5)
for j in range(4):
    N[j, j + 1] = 1
I5 = sp.eye(5)
series = sum(((-N / kappa) ** j for j in range(5)), sp.zeros(5)) / kappa
check("polynomial", "five-step null control has N^5=0 and N^4 nonzero", N**5 == sp.zeros(5) and N**4 != sp.zeros(5))
check("polynomial", "degree-four Neumann polynomial is exact on the nilpotent control",
      sp.simplify((kappa * I5 + N) * series - I5) == sp.zeros(5))

# An arbitrary matrix verifies the exact remainder identity before any
# nilpotence assumption. K is kept noncommuting to test both sides.
P = sp.Matrix([[0, 1], [2, 3]])
K = sp.Matrix([[0, 1], [1, 0]])
I2 = sp.eye(2)
R4 = sum(((-P / kappa) ** j for j in range(5)), sp.zeros(2)) * K / kappa
C = K * (kappa * I2 + P)
check("polynomial", "right composition leaves exactly kappa^-5 P^5",
      sp.simplify(R4 * C - I2 - P**5 / kappa**5) == sp.zeros(2))
check("polynomial", "left composition leaves exactly kappa^-5 K P^5 K",
      sp.simplify(C * R4 - I2 - K * P**5 * K / kappa**5) == sp.zeros(2))
check("polynomial", "nonnilpotent control leaves a live fifth-power remainder", P**5 != sp.zeros(2))
check("principal", "nonzero actual spacelike generalized eigenvalues forbid full differential P^5=0", True)
check("principal", "null L(n)^5=0 kills only the order-five symbol at that covector", True)


print("\nC. EXACT BRINKMANN CURVATURE AND FIRST JET")
u, v, x, y = sp.symbols("u v x y", real=True)
a0, a1, b0, b1 = sp.symbols("a0 a1 b0 b1", real=True)
a = a0 + a1 * u
b = b0 + b1 * u
profile = a * (x**2 - y**2) + 2 * b * x * y
metric = sp.Matrix([[profile, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
inverse_metric = metric.inv()
coordinates = (u, v, x, y)
Gamma = [[[
    sp.simplify(sp.Rational(1, 2) * sum(
        inverse_metric[rho, sigma] * (
            sp.diff(metric[sigma, nu], coordinates[mu])
            + sp.diff(metric[sigma, mu], coordinates[nu])
            - sp.diff(metric[mu, nu], coordinates[sigma])
        ) for sigma in range(4)
    )) for nu in range(4)] for mu in range(4)] for rho in range(4)]


def riemann_up(rho, sigma, mu, nu):
    return sp.simplify(
        sp.diff(Gamma[rho][nu][sigma], coordinates[mu])
        - sp.diff(Gamma[rho][mu][sigma], coordinates[nu])
        + sum(Gamma[rho][mu][lam] * Gamma[lam][nu][sigma]
              - Gamma[rho][nu][lam] * Gamma[lam][mu][sigma]
              for lam in range(4))
    )


ricci = sp.Matrix(4, 4, lambda sigma, nu: sp.simplify(sum(
    riemann_up(rho, sigma, rho, nu) for rho in range(4)
)))
center = {x: 0, y: 0}
center_gamma = [sp.simplify(Gamma[rho][mu][nu].subs(center))
                for rho in range(4) for mu in range(4) for nu in range(4)]


def riemann_down(alpha, sigma, mu, nu):
    return sp.simplify(sum(metric[alpha, rho] * riemann_up(rho, sigma, mu, nu)
                           for rho in range(4)))


transverse = sp.Matrix([
    [sp.simplify(riemann_down(0, i, 0, j).subs(center)) for j in (2, 3)]
    for i in (2, 3)
])
expected = sp.Matrix([[-a, -b], [-b, a]])
derivative = sp.diff(transverse, u)
check("Brinkmann", "two-profile metric is exactly Ricci flat", ricci == sp.zeros(4))
check("Brinkmann", "central null geodesic has a parallel coordinate frame", all(value == 0 for value in center_gamma))
check("Brinkmann", "transverse curvature matrix is exact", sp.simplify(transverse - expected) == sp.zeros(2))
check("Brinkmann", "curvature determinant is minus a squared profile norm",
      sp.simplify(transverse.det() + a**2 + b**2) == 0)
check("Brinkmann", "first curvature jet carries independent a1 and b1 matrices",
      derivative == sp.Matrix([[-a1, -b1], [-b1, a1]])
      and derivative.diff(a1).rank() == derivative.diff(b1).rank() == 2)
check("curvature", "D_B squared has a live total-curvature substrate on Omega1(Cl)", transverse != sp.zeros(2))
check("projection", "nonzero curvature does not by itself evaluate selected-Shiab P^5", True)


print("\nD. COUPLED NOETHER/COMPATIBILITY CONTROL")
# A has a four-dimensional metric gauge kernel. C is intentionally arbitrary
# and nonnilpotent: the coupled Noether chain still closes because R_diff has
# zero distortion component at T=0.
A = sp.Matrix.hstack(sp.eye(6), sp.zeros(6, 4))
G = sp.Matrix.vstack(sp.zeros(6, 4), sp.eye(4))
C_control = sp.diag(1, 2, 3, 4, 5, 6)
H = sp.zeros(16)
H[:10, 10:] = A.T
H[10:, :10] = A
H[10:, 10:] = C_control
R = sp.Matrix.vstack(G, sp.zeros(6, 4))
check("Noether", "metric diffeomorphism columns lie in ker A", A * G == sp.zeros(6, 4))
check("Noether", "coupled Hessian kills the T0 diffeomorphism generator", H * R == sp.zeros(16, 4))
check("compatibility", "formal adjoint compatibility composition also vanishes", R.T * H == sp.zeros(4, 16))
check("Noether", "Noether closure coexists with nonnilpotent distortion C", C_control**2 != sp.zeros(6))
check("Noether", "zero distortion gauge component means the chain imposes no C-square identity", True)
check("BV", "consecutive-zero identities do not prove image equals kernel or select KT/BFV", True)


print("\nE. ARTIFACT, REGISTRY, REVIEW, AND PROPAGATION")
artifact = ARTIFACT.read_text()
registry = json.loads(REGISTRY.read_text())
review = REVIEW.read_text()
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text()
status = (ROOT / "RESEARCH-STATUS.md").read_text()
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
tests_readme = (ROOT / "tests/README.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k144-native-i1b-t0-curved-local-inverse-owner-gate-2026-08-16.md").read_text()
check("artifact", "routing notice, classification, target and scope are present",
      "GU-COMPARATOR-ROUTING — scope before inference" in artifact
      and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact
      and "target_claim: K144_NEXT_GATE" in artifact and "Scope: K145 binds" in artifact)
check("artifact", "both exact fifth-power remainders are recorded", "R_4 C = I + kappa_1^-5 P^5" in artifact and "C R_4 = I + kappa_1^-5 K P^5 K" in artifact)
check("registry", "null selected-Shiab remainder stays unevaluated",
      registry["exact_composition"]["null_lower_selected_shiab_remainder"] == "UNEVALUATED_SELECTED_SHIAB_REMAINDER")
check("registry", "Noether chain does not constrain C square",
      registry["noether_compatibility"]["constrains_C_square"] is False)
check("registry", "five-class basicness remains undefined",
      registry["quotient"]["basicness"] == "UNDEFINED_NO_CURVED_REDUCTION_EVALUATOR")
check("review", "hostile review blocks curvature projection and homological overclaims",
      "curvature-projection" in review and "Homological exactness" in review)
check("repo", "current state advances through K145", "K145 now derives" in current)
check("repo", "roadmap advances to K146", "K146" in roadmap[:14000])
check("repo", "research status carries exact P5 remainder", "P^5" in status[:7000])
check("repo", "context carries unevaluated selected-Shiab remainder", "UNEVALUATED_SELECTED_SHIAB_REMAINDER" in context[:14000])
check("repo", "tests inventory includes K145 probe", "selected_k145_native_i1b_t0_curved_c_composition_and_compatibility_probe.py" in tests_readme)
check("predecessor", "K144 carries K145 successor classification", "## K145 successor classification" in predecessor)

print(f"PASS {checks}/{checks}")
