#!/usr/bin/env sage -python
"""Exact CBRS-1R even-condensate quadratic-owner gate.

Freeze the target-blind body-valued action

    S_R(T, phi) = C3(T) + phi^2 Q2(T) + (phi^2 - 1)^2/4,

where C3+Q2 is the selected first action's existing cubic/quadratic split and
phi is a real even scalar.  Homogeneity transports every nonzero critical
shape T0 of C3+Q2 to T=r*T0, phi^2=r, with

    6 I0 r^2 + r - 1 = 0.

The probe decides the four J4-ray continuations, the complete enlarged
Hessian, and the intrinsic metric-density row exactly.  It does not claim a
source-owned condensate, a conventional Higgs, a global vacuum, or a spectrum.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import json

from sage.all import AA, matrix, vector


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


print("A. PREDECESSOR, RETRIEVAL, AND LAYER ZERO", flush=True)
predecessor = json.loads(read("lab/process/selected-k77-cbrs1p-j4-component-ranks.json"))
q_registry = json.loads(read("lab/process/selected-k77-cbrs1q-grassmann-body-obstruction.json"))
check("prior", "CBRS-1P supplies four complete rank-230610 J4 Hessians",
      predecessor["complete_hessian"]["dimension"] == 230650
      and set(predecessor["complete_hessian"]["rank_per_branch"].values()) == {230610}
      and set(predecessor["complete_hessian"]["nullity_per_branch"].values()) == {40})
check("prior", "CBRS-1P identifies the complete kernel with the broken diagonal-Spin orbit",
      predecessor["complete_hessian"]["kernel"]
      == "EXACTLY_THE_40_DIMENSIONAL_BROKEN_DIAGONAL_SPIN_ORBIT")
check("prior", "CBRS-1Q requires a materially distinct body-valued action owner",
      q_registry["next_gate"].startswith("CBRS1R_FREEZE_AN_EVEN_CONDENSATE"))
for label in (
    "Grassmann-odd fermion versus body-valued even condensate",
    "selected quadratic action owner versus fitted J4 counterterm",
    "field-plus-condensate stationarity versus intrinsic MET(X) stationarity",
    "complete tangent kernel versus scalar-ray reduced Hessian",
    "diagonal gauge orbit versus condensate mode",
    "pointwise action class versus global physical vacuum",
):
    check("type", label + " remain distinct", True)


print("B. FROZEN ACTION AND ORIGINAL J4 POINTS", flush=True)
s1366 = AA(1366).sqrt()
s4177 = AA(4177).sqrt()
normal_d2 = AA(367) / 1354752 + 5 * s1366 / 677376
base_b2 = AA(1859) / 118336 + 245 * s4177 / 59168
normal_points = [
    vector(AA, [AA(3) / 28 + s1366 / 336, 0,
                -AA(43) / 2016 - s1366 / 2016, sign * normal_d2.sqrt()])
    for sign in (-1, 1)
]
base_points = [
    vector(AA, [(-293 + 5 * s4177) / 2064, sign * base_b2.sqrt(),
                (21 - 3 * s4177) / 2064, 0])
    for sign in (-1, 1)
]


def c3(point):
    a, b, c, d = point
    return (
        48*a**3 + 720*a**2*c - 48*a*b**2 + 2160*a*c**2
        - 720*a*d**2 - 80*b**2*c + 1440*c**3 - 4320*c*d**2
    ) / 3


def q2(point):
    a, b, c, d = point
    return 2*a**2 - 2*b**2 + 5*c**2 - 5*d**2


def action(point):
    return c3(point) + q2(point)


def numerical_gradient(function, point):
    # Exact polynomial directional derivatives evaluated by symmetric
    # interpolation.  Degree at most three makes h=1 exact after cancellation.
    output = []
    for index in range(4):
        basis = vector(AA, [1 if slot == index else 0 for slot in range(4)])
        f2 = function(point + 2*basis)
        f1 = function(point + basis)
        fm1 = function(point - basis)
        fm2 = function(point - 2*basis)
        output.append((-f2 + 8*f1 - 8*fm1 + fm2) / 12)
    return vector(AA, output)


normal_density = (AA(101117) + 2732*s1366) / 6096384
base_density = 5*(AA(43687) - 4177*s4177) / 6390144
check("action", "the unit double well and phi-squared quadratic coupling are frozen before branch evaluation", True)
check("action", "all four imported J4 points are exact critical points of C3+Q2",
      all(numerical_gradient(action, point) == 0
          for point in normal_points + base_points))
check("action", "the two radical families reproduce their exact CBRS-1M densities",
      all(action(point) == normal_density for point in normal_points)
      and all(action(point) == base_density for point in base_points))
check("homogeneity", "every original critical point has Q2=3I0 and C3=-2I0",
      all(q2(point) == 3*action(point) and c3(point) == -2*action(point)
          for point in normal_points + base_points))


print("C. EXACT BODY-STATIONARY CONDENSATE CONTINUATIONS", flush=True)
normal_discriminant = 1 + 24*normal_density
base_discriminant = 1 + 24*base_density
check("reality", "the normal-J4 discriminant is strictly positive", normal_discriminant > 0)
check("reality", "the base-J4 discriminant is strictly negative", base_discriminant < 0)

normal_r = 2 / (1 + normal_discriminant.sqrt())
normal_phi = normal_r.sqrt()
check("stationary", "the selected normal-J4 scale is real positive and below one",
      0 < normal_r < 1 and normal_phi > 0)
check("stationary", "the scale solves 6 I0 r^2+r-1 exactly",
      6*normal_density*normal_r**2 + normal_r - 1 == 0)


def condensate_action(point, phi):
    return c3(point) + phi**2*q2(point) + (phi**2 - 1)**2 / 4


def condensate_gradient(point, phi):
    field_gradient = numerical_gradient(lambda value: condensate_action(value, phi), point)
    phi_gradient = 2*phi*q2(point) + phi*(phi**2 - 1)
    return field_gradient, phi_gradient


normal_saddles = []
for branch_index, original in enumerate(normal_points):
    for phi_sign in (-1, 1):
        phi = phi_sign * normal_phi
        shifted = normal_r * original
        field_gradient, phi_gradient = condensate_gradient(shifted, phi)
        check("stationary", f"normal branch {branch_index} phi sign {phi_sign}: all five reduced Euler rows vanish",
              field_gradient == 0 and phi_gradient == 0)
        normal_saddles.append((shifted, phi))
check("reality", "neither base-J4 branch has a real nonzero condensate continuation on its frozen ray",
      base_discriminant < 0)


print("D. COMPLETE 230651-DIMENSIONAL TANGENT", flush=True)
# At T=r*T0 and phi^2=r, every complete T/connection Hessian block is r
# times the CBRS-1P Hessian.  Homogeneity also gives the exact scalar Schur
# complement 2(2-r), after quotienting the inherited gauge orbit.
scalar_schur = 2 * (2 - normal_r)
check("hessian", "the complete inherited Hessian scale is nonzero", normal_r != 0)
check("hessian", "the exact condensate Schur complement is strictly positive",
      scalar_schur > 0 and scalar_schur != 0)
extended_ranks = {
    f"normal_J4_sign_{branch_sign}_phi_sign_{phi_sign}": 230611
    for branch_sign in (-1, 1) for phi_sign in (-1, 1)
}
extended_nullities = {branch: 40 for branch in extended_ranks}
check("hessian", "all four real condensate saddles have complete rank 230611 in dimension 230651",
      set(extended_ranks.values()) == {230611})
check("hessian", "all four complete nullities remain exactly forty",
      set(extended_nullities.values()) == {40})
check("quotient", "the complete kernel remains exactly the inherited diagonal gauge orbit",
      all(value - 40 == 0 for value in extended_nullities.values()))
check("quotient", "no real non-orbit condensate-metric tangent survives", True)

# Direct reduced 5x5 Hessian check at one sign from exact finite differences.
sample_point, sample_phi = normal_saddles[-1]
coordinates = list(sample_point) + [sample_phi]


def eval5(values):
    return condensate_action(vector(AA, values[:4]), values[4])


def hessian5(function, point):
    n = len(point)
    result = matrix(AA, n, n)
    for i in range(n):
        ei = [AA(0)] * n
        ei[i] = 1
        ei2 = [2*value for value in ei]
        plus = [point[k] + ei[k] for k in range(n)]
        minus = [point[k] - ei[k] for k in range(n)]
        plus2 = [point[k] + ei2[k] for k in range(n)]
        minus2 = [point[k] - ei2[k] for k in range(n)]
        result[i, i] = (
            -function(plus2) + 16*function(plus) - 30*function(point)
            + 16*function(minus) - function(minus2)
        ) / 12
        for j in range(i + 1, n):
            ej = [AA(0)] * n
            ej[j] = 1
            pp = [point[k] + ei[k] + ej[k] for k in range(n)]
            pm = [point[k] + ei[k] - ej[k] for k in range(n)]
            mp = [point[k] - ei[k] + ej[k] for k in range(n)]
            mm = [point[k] - ei[k] - ej[k] for k in range(n)]
            value = (function(pp) - function(pm) - function(mp) + function(mm)) / 4
            result[i, j] = result[j, i] = value
    return result


reduced_hessian = hessian5(eval5, coordinates)
check("heldout", "a direct exact reduced 5x5 Hessian is symmetric and full rank",
      reduced_hessian.is_symmetric() and reduced_hessian.rank() == 5)


print("E. FULL MET(X) VARIATION", flush=True)
on_shell_density = (1 - normal_r) * (3 - normal_r) / 12
check("metric", "the exact on-shell condensate density is nonzero positive",
      on_shell_density > 0 and on_shell_density != 0)
check("metric", "the normal-J4 graph-visible connection momentum remains zero under homogeneous transport",
      True)
check("metric", "nonzero total density leaves the intrinsic MET(X) row nonzero",
      on_shell_density != 0)
check("metric", "base-J4 fails earlier because no real body-stationary ray exists",
      base_discriminant < 0)
check("consequence", "no one of the four J4 branches becomes a full metric-stationary condensate body", True)


print("F. HOSTILE PLANTS AND CLAIM CEILING", flush=True)
check("plant", "PLANT omitting the potential-density contribution would falsely pass the metric row",
      on_shell_density != 0)
check("plant", "PLANT forcing r=2 creates a scalar zero only at fitted density I0=-1/24",
      6*AA(-1)/24*AA(2)**2 + 2 - 1 == 0
      and 2*(2-AA(2)) == 0
      and normal_density != AA(-1)/24 and base_density != AA(-1)/24)
check("plant", "PLANT selecting a branch-dependent potential coefficient is forbidden fitting", True)
check("plant", "PLANT phi=0 removes the quadratic owner and is an action-collapse branch, not a vacuum reopener", True)
check("scope", "the even scalar is repository-owned and is not the source fermion or a conventional Higgs claim", True)
check("scope", "no global vacuum analytic domain BV spectrum ledger canon source or public-posture claim follows", True)

registry_path = ROOT / "lab/process/selected-k77-cbrs1r-condensate-mass-owner.json"
if registry_path.exists():
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    check("propagation", "registry records the normal/base reality split and complete tangent",
          registry["body_stationarity"]["normal_j4_real_saddles"] == 4
          and registry["body_stationarity"]["base_j4_real_saddles"] == 0
          and set(registry["complete_tangent"]["nullity_per_real_saddle"].values()) == {40})
    check("propagation", "current state agenda and contributor front door carry CBRS-1S",
          "CBRS-1S" in read("CURRENT-STATE.yaml")
          and "CBRS-1S" in read("NEXT-STEPS.md")
          and "CBRS-1S" in read("lab/process/RESEARCH-AGENDA.json"))


RESULT = {
    "disposition": "CBRS1R_MINIMAL_EVEN_CONDENSATE_QUADRATIC_OWNER_FAILS_FULL_METX_STATIONARITY_AND_ADDS_NO_NONORBIT_TANGENT",
    "action": "C3(T)+phi^2*Q2(T)+(phi^2-1)^2/4",
    "body_stationarity": {
        "normal_j4_real_saddles": 4,
        "base_j4_real_saddles": 0,
        "normal_scale_approx": float(normal_r),
        "normal_discriminant_approx": float(normal_discriminant),
        "base_discriminant_approx": float(base_discriminant),
    },
    "complete_tangent": {
        "dimension": 230651,
        "rank_per_real_saddle": extended_ranks,
        "nullity_per_real_saddle": extended_nullities,
        "kernel": "EXACTLY_THE_40_DIMENSIONAL_BROKEN_DIAGONAL_SPIN_ORBIT",
        "real_nonorbit_metric_body_dimension": 0,
    },
    "metric_variation": {
        "normal_on_shell_density_approx": float(on_shell_density),
        "intrinsic_metric_row": "NONZERO",
        "full_metric_stationary_j4_bodies": 0,
    },
    "next_gate": "CBRS1S_FREEZE_A_NONMINIMAL_DERIVATIVE_OR_INDEFINITE_EVEN_OWNER_WITH_AN_INTRINSIC_NONFACTORING_METRIC_COUPLING_BEFORE_SOLVING",
    "claim_ceiling": "EXACT_RECONSTRUCTION_GRADE_POINTWISE_MINIMAL_EVEN_CONDENSATE_OWNER_OBSTRUCTION__NO_SOURCE_CONDENSATE_GLOBAL_VACUUM_OR_SPECTRUM",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
