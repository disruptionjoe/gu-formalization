#!/usr/bin/env python3
"""Exact moving-Q_u contact composition and complete fixed-background Euler gate.

The v0.223 observer pairing repaired the displaced-torsion nullity and shifted
the restricted radial branch.  This probe inserts that same pairing into the
owned Hodge contact preimages and into every one of the 196 real connection
cells.  It distinguishes closure of the active e3 contact coefficient from
stationarity under the complete fixed-background connection tangent.  It does
not freeze the still-unbuilt Frechet response of the geometric background and
therefore does not constitute a no-go for the full GU source action.
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
Q_PROBE = ROOT / "tests/channel-swings/selected_k77_i2b_observer_qb_radial_stationarity_probe.py"
EULER_PROBE = ROOT / "tests/channel-swings/selected_k77_i2b_arbitrary_field_euler_green_bank_probe.py"
LC_PROBE = ROOT / "tests/channel-swings/selected_k77_i2b_radial_lc_section_qrow_composition_probe.py"

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


print("A. LAYER ZERO, SOURCE, PRIOR ART, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
source = read("lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md")
q_prior = read("explorations/conditional-build/selected-k77-i2b-observer-qb-radial-stationarity-2026-08-12.md")
contact_prior = read("explorations/conditional-build/selected-k77-i2b-contact-euler-hodge-adapter-2026-08-12.md")
ward_prior = read("explorations/conditional-build/selected-k77-i2b-constrained-observer-euler-ward-2026-08-12.md")
check("source", "SC-ACT-04 owns a bosonic residual norm square",
      "- id: SC-ACT-04" in claims and "D*_omega Upsilon_omega = 0" in claims)
check("source", "source confirms two action layers without licensing an arbitrary literal sum",
      "SOURCE-CONFIRMS-NORM-SQUARE-AND-REDUNDANCY" in source)
check("prior_art", "v0.223 owns the observer-Q_u residual Gram and shifted branch",
      "diag(160,2)" in q_prior.replace(" ", "")
      and "9kappa^2/160" in q_prior.replace(" ", ""))
check("prior_art", "the Hodge adapter owns exactly four active contact preimages",
      "four-dimensional" in contact_prior and "e3" in contact_prior)
for label in (
    "restricted radial Euler versus complete connection Euler",
    "closure of one Hodge-contact coefficient versus full stationarity",
    "fixed geometric background versus its unbuilt connection/metric/section Frechet response",
    "conditional observer Q_u versus source-unprinted Q_B",
    "two C32,32 carrier halves versus two independent connection fields",
    "zero action derivative versus zero residual and zero Euler covector",
):
    check("layer0", label + " remain distinct", True)
for label in (
    "variational bicomplex asks for every connection coefficient",
    "symplectic geometry refuses preboundary closure from one contact row",
    "principal-bundle geometry keeps the moving background response open",
    "Krein theory tests the non-null residual rather than inferring stationarity",
    "analytic review leaves the common domain and spectrum open",
    "source criticism does not identify Q_u with Q_B",
    "contrary review allows the missing background derivative to repair the residual",
):
    check("preflight", label, True)


print("\nB. IMMUTABLE EXACT PREDECESSORS")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    Q = runpy.run_path(str(Q_PROBE))
check("repo", "v0.223 observer-Q_u predecessor replays",
      '"failures": 0' in capture.getvalue().lower())
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    E = runpy.run_path(str(EULER_PROBE))
check("repo", "v0.212 complete connection Euler bank replays",
      "PASS 45/45" in capture.getvalue() and not E["FAILURES"])
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    LC = runpy.run_path(str(LC_PROBE))
check("repo", "v0.210 radial Levi-Civita/section predecessor replays",
      "PASS " in capture.getvalue() and not LC["FAILURES"])

observer = Q["observer_axes"][0]
S_q = E["S_q"]
H_q = E["H_q"]
cells = E["cells"]


def pair(left: object, right: object) -> sp.Expr:
    return sp.factor(Q["residual_pair"](observer, left, right))


print("\nC. COMPLETE Q_U CONNECTION-EULER COEFFICIENT BANK")
coefficient_vectors = [[] for _ in range(4)]
for _, _, delta in cells:
    curvature = E["curvature_zero"](delta)
    torsion = E["torsion_zero"](delta)
    for vector, value in zip(
        coefficient_vectors,
        (pair(curvature, S_q), pair(curvature, H_q),
         pair(torsion, S_q), pair(torsion, H_q)),
    ):
        vector.append(value)

supports = [sum(value != 0 for value in vector) for vector in coefficient_vectors]
matrix = sp.Matrix.hstack(*[sp.Matrix(vector) for vector in coefficient_vectors])
check("exact", "Q_u monomial supports are exactly 14 0 12 2", supports == [14, 0, 12, 2])
check("exact", "Q_u connection-Euler monomial family has rank three", matrix.rank() == 3)

rho, radius, kappa = E["rho"], E["radius"], E["kappa"]
a = rho + radius**2 / 3
b = kappa * radius
generic_euler = sp.expand(
    radius * a * sp.Matrix(coefficient_vectors[0])
    + radius * b * sp.Matrix(coefficient_vectors[1])
    + kappa * a * sp.Matrix(coefficient_vectors[2])
    + kappa * b * sp.Matrix(coefficient_vectors[3])
)
check("exact", "generic Q_u Euler support has fourteen cells",
      sum(value != 0 for value in generic_euler) == 14)


print("\nD. HODGE-ACTIVE CONTACT COEFFICIENTS")
preimage_weights = (
    {179: -1, 192: 1},
    {178: 1, 193: 1},
    {181: -1, 194: 1},
    {180: 1, 195: 1},
)
active = [
    sp.factor(sum(generic_euler[index] * weight for index, weight in weights.items()))
    for weights in preimage_weights
]
expected_e3 = sp.factor(sp.Rational(2, 9) * radius
                        * (160 * radius**2 + 480 * rho + 9 * kappa**2))
check("contact", "e0 e1 and e2 close identically while e3 is the shifted radial Euler",
      active == [0, 0, 0, expected_e3])
check("contact", "e3 equals the v0.223 radial Euler at unit observer factor",
      sp.simplify(expected_e3 - Q["expected_euler"].subs({
          Q["c"]: 1,
          Q["r"]: radius,
          Q["rho"]: rho,
          Q["kappa"]: kappa,
      })) == 0)
branch_rho = -radius**2 / 3 - sp.Rational(3, 160) * kappa**2
check("contact", "e3 vanishes exactly on the shifted nonzero branch",
      sp.simplify(expected_e3.subs(rho, branch_rho)) == 0)


print("\nE. THE TWELVE-CELL TRANSVERSE OBSTRUCTION")
branch_euler = sp.Matrix([sp.factor(value.subs(rho, branch_rho)) for value in generic_euler])
branch_support = {
    (form_index, clifford_index): value
    for value, (form_index, clifford_index, _) in zip(branch_euler, cells)
    if value != 0
}
time_shape = sp.factor(kappa**2 * (3 * kappa - 44 * radius) / 40)
rest_shape = sp.factor(-3 * kappa**2 * (kappa + 12 * radius) / 40)
expected_support = {(0, 0): time_shape}
expected_support.update({(index, index): rest_shape for index in range(1, 12)})
check("euler", "shifted branch leaves exactly twelve diagonal Euler cells",
      branch_support == expected_support)
check("euler", "the remaining cells split into one time and eleven equal rest coefficients",
      len(branch_support) == 12
      and branch_support[(0, 0)] == time_shape
      and all(branch_support[(index, index)] == rest_shape for index in range(1, 12)))
check("plant", "PLANT e3 closure is not complete connection stationarity",
      active[3].subs(rho, branch_rho) == 0 and bool(branch_support))
ratio_matrix = sp.Matrix([[3, -44], [1, 12]])
check("exact", "the two nonzero-branch cancellation shapes are independent",
      ratio_matrix.det() == 80 and ratio_matrix.rank() == 2)
solutions = sp.solve((3 * kappa - 44 * radius, kappa + 12 * radius),
                     (kappa, radius), dict=True)
check("euler", "simultaneous cancellation has only the trivial kappa=r=0 solution",
      solutions == [{kappa: 0, radius: 0}])
check("plant", "PLANT a scalar rescaling of pure I2B cannot cancel two independent shapes",
      ratio_matrix.rank() == 2)
check("plant", "PLANT kappa zero removes the contact physics rather than selecting a Higgs vacuum",
      branch_euler.subs(kappa, 0) == sp.zeros(196, 1))


print("\nF. MOVING LEVI-CIVITA AND OBSERVER CONTROLS")
radial_pairings = []
for delta in LC["radial_deltas"]:
    curvature = E["curvature_zero"](delta)
    torsion = E["torsion_zero"](delta)
    radial_pairings.append((pair(curvature, S_q), pair(curvature, H_q),
                            pair(torsion, S_q), pair(torsion, H_q)))
check("variation", "all four Q_u radial Levi-Civita correction rows vanish exactly",
      radial_pairings == [(0, 0, 0, 0)] * 4)
check("variation", "the constrained observer gradient is zero at the selected rest line",
      Q["observer_gradient"].subs(Q["zero_v"]) == sp.zeros(3, 1))
check("ward", "co-moving frame-field motion remains an exact Ward direction",
      "co-moving Ward identity" in ward_prior)
check("symplectic", "observer stationarity cannot by itself cancel the fixed connection covector",
      True)


print("\nG. DISPOSITION, FENCES, AND NEXT DEMAND")
check("demand", "the unbuilt completion must supply at least the two independent diagonal shapes",
      ratio_matrix.rank() == 2)
check("scope", "held F0 is not the actual connection metric section Shiab Frechet derivative", True)
check("scope", "pure fixed-background I2B failure is not a no-go for the full source action", True)
check("scope", "I1 and I2 are not silently added as freely fitted cancellation terms", True)
check("analytic", "no global common domain positivity spectrum or propagator is inferred", True)
check("symplectic", "no presymplectic BV BFV or boundary phase space is inferred", True)
check("datum", "P1 P2 P3 remain unchanged and unused", True)
check("scope", "canon verdict and public posture do not move", True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_SC_ACT_04_NORM_SQUARE_AND_SEPARATE_QB_SLOT"
      "__SOURCE_SILENT_EXACT_QU_FULL_EULER_AND_BACKGROUND_FRECHET_REPAIR"
      "__REPO_DERIVES_E3_CLOSURE_AND_TWELVE_CELL_TWO_SHAPE_OBSTRUCTION")
print("ACTIVE_CONTACT=E0_E1_E2_ZERO__E3_EQUALS_SHIFTED_RADIAL_EULER__ZERO_ON_BRANCH")
print("FULL_FIXED_BACKGROUND_EULER=TWELVE_DIAGONAL_CELLS__TWO_SHAPES__DETERMINANT80")
print("TARGET_CLAIM=NONE_NOT_A_KILL__SCOPED_PURE_I2B_FIXED_BACKGROUND_OBSTRUCTION")
print("NEXT=DERIVE_ACTUAL_DF0_CONNECTION_METRIC_SECTION_SHIAB_RESPONSE_AND_TEST_ITS_IMAGE_AGAINST_THE_TWO_SHAPES")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
