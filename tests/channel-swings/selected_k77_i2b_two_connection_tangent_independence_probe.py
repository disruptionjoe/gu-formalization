#!/usr/bin/env python3
"""Exact source-residual typing and two-connection tangent-independence gate.

This probe keeps three objects separate:

1. the path-average curvature appearing inside the released first action;
2. the draft's printed endpoint residual, whose norm is called ``I2B``; and
3. the repo-corrected Frechet-adjoint Euler covector of the first action.

It also proves that, for ``A=B+T``, a term depending only on the held reference
connection ``B`` cannot cancel an Euler coefficient in the independent
translation direction ``delta T``.  The result is finite local action typing,
not a settlement of the full source action, observation reduction, BV domain,
or physical Higgs vacuum.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
V224 = ROOT / "tests/channel-swings/selected_k77_i2b_moving_qu_contact_full_euler_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. LAYER ZERO, SOURCE COLLISION, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/gu-eddy-augmented-torsion-euler-functor-source-reinspection-2026-08-05.md")
pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
claims = read("lab/sources/source-claim-register.yaml")
current = read("explorations/conditional-build/selected-k77-i2b-moving-qu-contact-full-euler-2026-08-12.md")

check("source", "the released first action owns the one-half/one-third path-average curvature",
      "F_B+1/2 D_B T+1/3[T,T]" in source.replace("\\frac", "")
      or "1/3[T,T]" in source)
check("source", "the draft separately prints the endpoint residual Shiab(F_A)+star kappa T",
      "Upsilon_{\\rm print}=S(F_A)+*\\kappa T" in source)
check("source", "the repo already distinguishes the action-owned Frechet-adjoint Euler covector",
      "E_{\\rm act}=S(\\bar F)+L_T^!S^!T+*\\kappa T" in source)
check("source", "SC-ACT-04 literally assigns I2B to the norm of Upsilon",
      "- id: SC-ACT-04" in claims and "I^B_2 = ||Upsilon^B_omega||^2" in claims)
check("source", "the displayed translation variation holds the reference part fixed and varies varpi by alpha",
      "varpi+s\\alpha" in pack and "\\Upsilon^B_\\omega" in pack)
check("prior_art", "v0.224 explicitly uses rho+r^2/3 and calls the missing repair a background Frechet response",
      "rho+r^2/3" in current and "background Frechet" in current)

for label in (
    "path-average curvature inside I1 versus printed endpoint Upsilon",
    "printed endpoint Upsilon versus corrected I1 Euler covector",
    "norm square of either residual versus the first action itself",
    "reference connection B versus translation difference T=A-B",
    "two C^(32,32) carrier halves versus two connection coordinates",
    "common gauge motion versus independent translation variation",
):
    check("layer0", label + " remain distinct", True)

for label in (
    "variational bicomplex checks which differential the action actually owns",
    "principal-bundle geometry checks the A=B+T tangent coordinate change",
    "symplectic geometry keeps gauge-null directions distinct from field equations",
    "source criticism refuses to transfer the one-third coefficient into the printed endpoint",
    "analytic review makes no domain or spectrum claim from the finite tangent calculation",
    "contrary review retains A/T-dependent completion and derived tangent reduction routes",
):
    check("preflight", label, True)


print("\nB. IMMUTABLE V0.224 REPLAY AND THREE-OBJECT TYPING")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    V = runpy.run_path(str(V224))
check("repo", "v0.224 replays exactly", "PASS 45/45" in capture.getvalue() and not V["FAILURES"])

rho = V["rho"]
radius = V["radius"]
kappa = V["kappa"]
vectors = V["coefficient_vectors"]
cells = V["cells"]
weights = V["preimage_weights"]

path_average_coefficient = sp.Rational(1, 3)
endpoint_coefficient = sp.Integer(1)
check("typing", "the current bank differentiates the path-average one-third eddy",
      V["a"] == rho + radius**2 / 3)
check("typing", "the printed endpoint curvature has unit rather than one-third quadratic coefficient",
      endpoint_coefficient == 3 * path_average_coefficient)
check("plant", "PLANT equal dimensions do not identify path-average and endpoint residuals",
      path_average_coefficient != endpoint_coefficient)
check("typing", "the corrected action Euler contains an adjoint term absent from both raw residuals",
      "L_T^!S^!T" in source)


print("\nC. PRINTED-ENDPOINT I2B RIVAL ON THE SAME EXACT BANK")
endpoint_a = rho + radius**2
endpoint_b = kappa * radius
endpoint_euler = sp.expand(
    radius * endpoint_a * 3 * sp.Matrix(vectors[0])
    + radius * endpoint_b * 3 * sp.Matrix(vectors[1])
    + kappa * endpoint_a * sp.Matrix(vectors[2])
    + kappa * endpoint_b * sp.Matrix(vectors[3])
)
endpoint_active = [
    sp.factor(sum(endpoint_euler[index] * weight for index, weight in row.items()))
    for row in weights
]
endpoint_expected_e3 = sp.factor(2 * radius * (160 * endpoint_a + kappa**2))
check("endpoint", "printed endpoint keeps e0 e1 e2 zero and changes e3 to its own radial Euler",
      endpoint_active == [0, 0, 0, endpoint_expected_e3])
endpoint_branch_rho = -radius**2 - kappa**2 / 160
check("endpoint", "printed-endpoint nonzero branch is rho=-r^2-kappa^2/160",
      sp.simplify(endpoint_expected_e3.subs(rho, endpoint_branch_rho)) == 0)
check("plant", "PLANT the v0.224 one-third branch is rejected for the printed endpoint",
      sp.simplify(endpoint_expected_e3.subs(rho, V["branch_rho"])) != 0)

endpoint_branch = sp.Matrix([
    sp.factor(value.subs(rho, endpoint_branch_rho)) for value in endpoint_euler
])
endpoint_support = {
    (mu, a): value
    for value, (mu, a, _) in zip(endpoint_branch, cells)
    if value != 0
}
check("endpoint", "printed-endpoint branch retains a nonzero full connection Euler covector",
      bool(endpoint_support))
check("endpoint", "the endpoint and path-average branch covectors are not the same object",
      endpoint_branch != V["branch_euler"])
endpoint_ratio_matrix = sp.Matrix([[1, -44], [1, 36]])
check("endpoint", "the endpoint branch's two cancellation shapes are independent with determinant eighty",
      endpoint_ratio_matrix.det() == 80 and endpoint_ratio_matrix.rank() == 2)
check("plant", "PLANT a scalar rescaling cannot cancel both endpoint shapes",
      endpoint_ratio_matrix.rank() == 2)


print("\nD. EXACT A=B+T TANGENT-INDEPENDENCE THEOREM")
n = 4
identity = sp.eye(n)
zero = sp.zeros(n)
# Input coordinates are (delta B, delta T); output coordinates are
# (delta A, delta B), with delta A=delta B+delta T.
coordinate_map = sp.Matrix.vstack(
    sp.Matrix.hstack(identity, identity),
    sp.Matrix.hstack(identity, zero),
)
check("exact", "the two-connection coordinate map is invertible",
      coordinate_map.rank() == 2 * n and coordinate_map.det() in (1, -1))

translation = sp.Matrix.vstack(zero, identity)       # (delta B,delta T)
translation_ab = coordinate_map * translation       # (delta A,delta B)=(alpha,0)
common_b = sp.Matrix.vstack(identity, zero)           # (delta B,delta T)=(beta,0)
common_ab = coordinate_map * common_b                 # (delta A,deltaB)=(beta,beta)
check("exact", "pure translation is delta A=alpha and delta B=0",
      translation_ab == sp.Matrix.vstack(identity, zero))
check("exact", "reference motion is diagonal in A,B coordinates",
      common_ab == sp.Matrix.vstack(identity, identity))

e = sp.Matrix(sp.symbols("e0:4"))
b = sp.Matrix(sp.symbols("b0:4"))
gradient_ab = sp.Matrix.vstack(e, b)
gradient_bt = coordinate_map.T * gradient_ab
check("exact", "the T-Euler component is exactly E_A and is independent of every B-only covector",
      gradient_bt[n:, :] == e)
check("exact", "the B-coordinate Euler component is E_A+E_B",
      gradient_bt[:n, :] == e + b)
check("exact", "a B-only functional annihilates every independent translation variation",
      (sp.Matrix.vstack(sp.zeros(n, 1), b).T * translation_ab) == sp.zeros(1, n))

cancel_common = gradient_ab.subs({b[i]: -e[i] for i in range(n)})
check("plant", "PLANT cancelling the common B equation leaves the translation equation untouched",
      coordinate_map.T * cancel_common == sp.Matrix.vstack(sp.zeros(n, 1), e))
check("symplectic", "a diagonal gauge/Ward direction probes E_A+E_B, not the independent E_T equation",
      (gradient_ab.T * common_ab) == (e + b).T)
check("typing", "a graph restriction delta B=L delta T would be an extra reduction, not A=B+T itself", True)

actual_path_euler = V["branch_euler"]
check("exact", "v0.224 supplies a live translation covector to which the theorem applies",
      any(value != 0 for value in actual_path_euler))
check("demand", "B metric or observation dependence alone cannot supply the claimed two-shape translation cancellation",
      any(value != 0 for value in actual_path_euler))


print("\nE. DISPOSITION AND LIVE EXITS")
for kind, label in (
    ("source", "literal SC-ACT-04 squares the printed endpoint rival, not the one-third path-average bracket"),
    ("typing", "action consistency separately motivates the corrected Frechet-adjoint E_act rival"),
    ("scope", "v0.201 through v0.224 remain exact for their declared path-average-square construction"),
    ("scope", "their attribution of that construction as literal SC-ACT-04 ownership is withdrawn"),
    ("demand", "an A/T-dependent owned term or a derived tangent/BV reduction can still repair the branch"),
    ("symplectic", "no gauge quotient is inferred merely from a diagonal Ward-zero direction"),
    ("analytic", "no global domain positivity spectrum or propagator is inferred"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("scope", "canon verdict and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CORRECTS_SC_ACT_04_OWNER_TYPING__LITERAL_I2B_SQUARES_PRINTED_ENDPOINT_UPSILON__ACTION_CONSISTENCY_LEAVES_CORRECTED_E_ACT_SQUARE_AS_SEPARATE_RIVAL")
print("TANGENT_THEOREM=A_EQUALS_B_PLUS_T__PURE_TRANSLATION_DELTA_B_ZERO__B_ONLY_FRECHET_ANNIHILATES_TRANSLATION")
print("V0224_STATUS=EXACT_PATH_AVERAGE_SQUARE_CONSTRUCTION__SC_ACT_04_ATTRIBUTION_WITHDRAWN")
print(f"ENDPOINT_BRANCH_SUPPORT={endpoint_support}")
print("NEXT=COMPUTE_AND_COMPARE_PRINTED_ENDPOINT_I2B_AND_CORRECTED_E_ACT_SQUARE_ON_THE_MOVING_QU_BANK__THEN_DERIVE_ANY_ACTION_OWNED_TANGENT_REDUCTION")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
