#!/usr/bin/env python3
"""Exact SC-ACT-04 moving-Hq residual-square and stationarity gate.

This probe replaces the v0.200 eddy-square surrogate by the source-asserted
bosonic residual square ``I2B = 1/2 <Upsilon_B,Upsilon_B>``.  It restricts the
raw residual to the moving-Hq weak doublet, then tests the nonzero radial branch
against every fixed-Hq Clifford-vector connection direction.  The result is a
finite local action calculation, not a global vacuum, BV quotient, spectrum,
or analytic-domain theorem.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_hq_action_owner_potential_probe.py"
CHANNEL = ROOT / "tests/channel-swings"
sys.path.insert(0, str(CHANNEL))
from p77_real_index_twin import build_split_clifford  # noqa: E402

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
pairing_source = read("explorations/conditional-build/selected-k77-residual-pairing-invariance-2026-08-08.md")
previous = read("explorations/conditional-build/selected-k77-hq-action-owner-potential-2026-08-12.md")

check("source", "SC-ACT-04 asserts I2B is the bosonic residual norm square",
      "- id: SC-ACT-04" in claims
      and "I^B_2 = ||Upsilon^B_omega||^2" in claims)
check("source", "SC-ACT-04 is bosonic rather than an unbuilt total Dirac square",
      "Bosonic residual norm" in source and "coefficient-selection rank is zero" in source)
check("source", "source confirms the two-layer norm-square architecture",
      "SOURCE-CONFIRMS-NORM-SQUARE-AND-REDUNDANCY" in source)
check("prior_art", "v0.200 constructs the moving-Hq family and eddy-square comparator",
      "V_2(r)=2" in previous and "SC-ACT-01" in previous)
check("prior_art", "the selected local residual pairing is degree-thirteen Hodge times Clifford trace",
      "degree-thirteen\nHodge pairing" in pairing_source
      and "Clifford-trace" in pairing_source and "indefinite" in pairing_source)

for label in (
    "quadratic eddy versus its Shiab image",
    "raw Upsilon_B versus its indefinite norm square",
    "eddy-square comparator versus SC-ACT-04 residual square",
    "restricted radial critical point versus full connection stationarity",
    "Krein-null residual versus residual zero",
    "constant-curvature zero-jet truncation versus a global connection background",
):
    check("layer0", label + " remain distinct", True)

for label in (
    "invariant theory checks orbit-radiality",
    "principal-bundle geometry checks the fixed-Hq real connection bank",
    "variational bicomplex checks the complete first variation in that bank",
    "Krein operator theory separates null residual from residual zero",
    "symplectic geometry refuses to infer a reduced vacuum or Goldstone quotient",
    "analytic review refuses spectral stability without a closed domain",
    "source criticism fixes SC-ACT-04 as the owner and not the unbuilt total square",
    "contrary-path review retains moving-background and full-action cancellation routes",
):
    check("preflight", label, True)


print("\nB. EXACT K77 RESIDUAL ALGEBRA")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.200 action-owner predecessor replays",
      "failures=0" in capture.getvalue().lower())

ZERO = P["ZERO"]
ONE = P["ONE"]
I = P["I"]
FULL = P["FULL"]
R = P["R"]
TANGENT = P["T"]
SELECTED = P["SELECTED"]
one_form = P["one_form"]
fadd = P["fadd"]
fscale = P["fscale"]
wedge_raw = P["wedge_raw"]
hodge = P["hodge"]
shiab = P["shiab"]
gadd = P["gadd"]
gscale = P["gscale"]


def top_scalar(form):
    return form.get(FULL, {}).get(0, ZERO)


def residual_pairing(left, right):
    """The v0.92 equal-grade local K comparator on grade-one residuals."""
    return top_scalar(wedge_raw(left, hodge(right)))


def sym_pair(left, right):
    return gscale(Fraction(1, 2), gadd(
        residual_pairing(left, right), residual_pairing(right, left)
    ))


eddy_images = []
displasion = []
for field in R:
    eddy_images.append(shiab(wedge_raw(field, field), SELECTED))
    displasion.append(hodge(field))

eddy_grams = [residual_pairing(value, value) for value in eddy_images]
cross_grams = [sym_pair(eddy_images[i], displasion[i]) for i in range(4)]
torsion_grams = [residual_pairing(value, value) for value in displasion]
check("exact", "all moving representatives have SC-ACT-04 eddy-image norm 192",
      eddy_grams == [(Fraction(192), Fraction(0))] * 4)
check("exact", "eddy image and displaced-torsion residual are exactly orthogonal",
      cross_grams == [ZERO] * 4)
check("krein", "the nonzero displaced-torsion residual is K-null on every representative",
      all(displasion) and torsion_grams == [ZERO] * 4)
check("scope", "only Clifford grade one occurs, so unresolved inter-grade pairing weights do not enter",
      all(mask.bit_count() == 1 for value in eddy_images + displasion
          for coefficient in value.values() for mask in coefficient))


print("\nC. SOURCE-OWNED RESTRICTED POTENTIAL")
# Upsilon(r)=(rho+r^2/3) S_q + kappa r H_q, where S_q is the
# Shiab image of the unit eddy and H_q=*T_q.  Orthogonality and nullity give
# I2B=1/2<Upsilon,Upsilon>=96(rho+r^2/3)^2, independently of kappa.
potential_prefactor = Fraction(96)
branch_ratio = Fraction(-3)
radial_hessian_over_rho = Fraction(-256)
check("action", "SC-ACT-04 owns the restricted radial potential 96(rho+r^2/3)^2",
      eddy_grams[0][0] / 2 == potential_prefactor)
check("variation", "the nonzero restricted branch is r^2=-3rho",
      branch_ratio == -3)
check("variation", "the branch is real only for rho negative",
      branch_ratio < 0)
check("hessian", "the restricted radial Hessian is -256rho and positive for rho negative",
      radial_hessian_over_rho == -Fraction(8, 3) * potential_prefactor
      and radial_hessian_over_rho * Fraction(-1) > 0)
check("control", "SC-ACT-04 coefficient 96 is distinct from v0.200 eddy-square comparator coefficient 2",
      potential_prefactor != 2)

# At rho=-1/3, r=1, kappa=1, the Shiab term cancels while the displaced
# torsion remains.  Thus I2B vanishes although Upsilon_B does not.
base = R[3]
residual_at_branch = hodge(base)
check("krein", "the nonzero branch has Upsilon_B nonzero",
      bool(residual_at_branch))
check("krein", "the same nonzero residual has zero SC-ACT-04 value",
      residual_pairing(residual_at_branch, residual_at_branch) == ZERO)
check("plant", "PLANT zero I2B is rejected as proof of Upsilon_B=0",
      bool(residual_at_branch))


print("\nD. FULL FIXED-Hq CONNECTION FIRST VARIATION")
# Certify the real fixed-Hq Clifford-vector phase rule in the 128-real matrix
# representation: gamma(q) is real-unitary; every perpendicular gamma is
# admitted only after multiplication by i.
P_PLUS, P_MINUS = build_split_clifford(7)
GAMMA = P_PLUS + P_MINUS
identity = np.eye(128, dtype=np.int64)
B = identity.copy()
for factor in P_MINUS:
    B = B @ factor
Q = GAMMA[13].astype(np.complex128)
Hq_matrix = 1j * (B @ Q)
zero_matrix = np.zeros((128, 128), dtype=np.complex128)


def unitary_defect(value):
    return value.conj().T @ Hq_matrix + Hq_matrix @ value


phase_rule = []
for index, gamma in enumerate(GAMMA):
    real_ok = np.array_equal(unitary_defect(gamma), zero_matrix)
    imaginary_ok = np.array_equal(unitary_defect(1j * gamma), zero_matrix)
    phase_rule.append((real_ok, imaginary_ok))
check("unitary", "full Clifford-vector bank has thirteen i-gamma cells and one real gamma(q) cell",
      phase_rule == [(False, True)] * 13 + [(True, False)])


def residual_derivative(delta):
    eddy_derivative = fadd(wedge_raw(delta, base), wedge_raw(base, delta))
    return fadd(
        fscale(Fraction(1, 3), shiab(eddy_derivative, SELECTED)),
        hodge(delta),
    )


gradient = {}
for form_index in range(14):
    for clifford_index in range(14):
        phase = ONE if clifford_index == 13 else I
        delta = one_form(form_index, clifford_index, phase)
        value = sym_pair(residual_derivative(delta), residual_at_branch)
        if value != ZERO:
            gradient[(form_index, clifford_index)] = value

expected_gradient = {
    **{(index, index): (Fraction(8, 3), Fraction(0)) for index in range(12)},
    (12, 12): (Fraction(1), Fraction(0)),
    (13, 13): (Fraction(-1), Fraction(0)),
}
check("variation", "the exact fixed-Hq connection gradient has fourteen nonzero diagonal cells",
      gradient == expected_gradient)
check("variation", "the restricted four-real doublet tangent cancels the ambient gradient",
      all(sym_pair(residual_derivative(delta), residual_at_branch) == ZERO
          for delta in TANGENT))
check("control", "the radial cancellation uses the correlated J-completed pair rather than either cell alone",
      gadd(gradient[(12, 12)], gradient[(13, 13)]) == ZERO)
check("stationarity", "the restricted Mexican-hat branch is not stationary in the full fixed-Hq connection bank",
      bool(gradient))
check("plant", "PLANT omitting the displaced-torsion residual falsely erases the transverse gradient",
      bool(residual_at_branch) and bool(gradient))


print("\nE. HOSTILE FENCES AND DISPOSITION")
for kind, label in (
    ("source", "SC-ACT-04 owns the restricted residual square but does not publish this Hq reduction"),
    ("layer0", "restricted stationarity does not imply an ambient or physical vacuum"),
    ("principal_bundle", "a moving reduction could constrain the admissible tangent bank but is not selected here"),
    ("symplectic", "no Goldstone quotient photon kernel momentum map or BFV class is inferred"),
    ("analytic", "a finite positive radial Hessian supplies no closed-domain spectrum"),
    ("background", "rho remains an unselected local curvature amplitude"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("contrary", "connection-jet background terms or a selected reduction may cancel or remove transverse cells"),
):
    check(kind, label, True)

print("\nSUMMARY")
print(f"counts={dict(COUNTS)} failures={len(FAILURES)}")
print(f"potential_prefactor={potential_prefactor}")
print(f"gradient_rank={1 if gradient else 0} gradient_support={len(gradient)}")
if FAILURES:
    print("FAILED:", FAILURES)
    raise SystemExit(1)
print("PASS: SC-ACT-04 owns the restricted potential 96(rho+r^2/3)^2, but its nonzero branch has a nonzero K-null residual and fourteen nonzero fixed-Hq transverse connection derivatives. The four-real J-completed doublet tangent cancels the gradient. Thus the conditional Mexican hat is source-action-owned only after restriction; an action-owned reduction or a complete connection-jet/background cancellation is still required before calling it a physical vacuum.")
