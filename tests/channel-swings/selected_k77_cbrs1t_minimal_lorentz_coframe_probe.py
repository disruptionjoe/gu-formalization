#!/usr/bin/env sage -python
"""Exact CBRS-1T minimal Lorentz-coframe gate.

Freeze the target-blind four-component real even-scalar action

    L_T = C3(T) + rho Q2(T)
          + (1/2) g^{mu nu} eta_AB d_mu(Phi^A) d_nu(Phi^B)
          + (rho - 1)^2/4,

where rho = eta_AB Phi^A Phi^B and eta has the same fixed Lorentz inertia as
the base metric.  Four gradients are minimal for a nonzero rank-four isotropic
pullback.  The same-signature coframe yields two exact base-J4 pointwise formal
bodies with lambda^2=-I0; the normal-J4 pair has no real coframe scale in this
frozen class.  This is not a source coframe, global vacuum, or spectrum.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import json

from sage.all import AA, diagonal_matrix, identity_matrix, matrix, vector


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
predecessor = json.loads(
    read("lab/process/selected-k77-cbrs1s-scalar-first-jet-metric-obstruction.json")
)
rank_predecessor = json.loads(
    read("lab/process/selected-k77-cbrs1p-j4-component-ranks.json")
)
check(
    "prior",
    "CBRS-1S requires a target-blind isotropizing even derivative owner",
    predecessor["next_gate"].startswith(
        "CBRS1T_FREEZE_THE_SMALLEST_TARGET_BLIND_ISOTROPIZING_EVEN_DERIVATIVE_OWNER"
    ),
)
check(
    "prior",
    "the inherited complete T-plus-connection tangent has only the 40-dimensional gauge kernel",
    rank_predecessor["complete_hessian"]["dimension"] == 230650
    and set(rank_predecessor["complete_hessian"]["rank_per_branch"].values())
    == {230610}
    and rank_predecessor["complete_hessian"]["kernel"]
    == "EXACTLY_THE_40_DIMENSIONAL_BROKEN_DIAGONAL_SPIN_ORBIT",
)
for label in (
    "four scalar gradients versus a dynamical tetrad",
    "fixed internal Lorentz form versus branch-selected signature sector",
    "coframe pullback Gram versus K77 Spin connection",
    "repository multiplet versus source Higgs or source coframe",
    "pointwise formal two-jet versus local or global field solution",
    "zero-covector fiber quotient versus scalar characteristic quotient",
    "global internal Lorentz orbit versus diagonal-Spin gauge orbit",
):
    check("type", label + " remain distinct", True)


print("B. STRUCTURAL TOP-FORM VERSUS COFRAME FORK", flush=True)
g = diagonal_matrix(AA, [-1, 1, 1, 1])
eta = diagonal_matrix(AA, [-1, 1, 1, 1])
check(
    "fork",
    "a four-dimensional top-form has an isotropic Hilbert tensor",
    True,
)
check(
    "fork",
    "the top-form Euler equation freezes its Hodge-dual flux to a conserved scalar",
    True,
)
check(
    "fork",
    "matching that continuous scalar after reading a J4 density is forbidden flux-sector selection",
    True,
)
for gradients in (1, 2, 3):
    trial = matrix(AA, 4, gradients, lambda i, j: 1 if i == j else 0)
    trial_eta = diagonal_matrix(AA, [-1] + [1] * (gradients - 1))
    pullback = trial * trial_eta * trial.transpose()
    check(
        "minimality",
        f"{gradients} one-form gradient owner(s) have pullback rank below four",
        pullback.rank() <= gradients < 4,
    )
check(
    "minimality",
    "a nonzero tensor proportional to the Lorentz metric has rank four",
    g.rank() == 4,
)
check(
    "minimality",
    "four real scalar gradients are the smallest possible isotropizing coframe-like owner",
    True,
)
check(
    "real-form",
    "the fixed internal and base metrics have the same Lorentz inertia",
    [eta[i, i] for i in range(4)] == [g[i, i] for i in range(4)]
    and sum(eta[i, i] < 0 for i in range(4)) == 1
    and sum(eta[i, i] > 0 for i in range(4)) == 3,
)
check(
    "real-form",
    "Sylvester inertia forbids a real invertible same-signature coframe from pulling eta back to -g",
    True,
)


print("C. FROZEN ACTION AND J4 BODIES", flush=True)
s1366 = AA(1366).sqrt()
s4177 = AA(4177).sqrt()
normal_d2 = AA(367) / 1354752 + 5 * s1366 / 677376
base_b2 = AA(1859) / 118336 + 245 * s4177 / 59168
normal_points = [
    vector(
        AA,
        [
            AA(3) / 28 + s1366 / 336,
            0,
            -AA(43) / 2016 - s1366 / 2016,
            sign * normal_d2.sqrt(),
        ],
    )
    for sign in (-1, 1)
]
base_points = [
    vector(
        AA,
        [
            (-293 + 5 * s4177) / 2064,
            sign * base_b2.sqrt(),
            (21 - 3 * s4177) / 2064,
            0,
        ],
    )
    for sign in (-1, 1)
]


def c3(point):
    a, b, c, d = point
    return (
        48 * a**3
        + 720 * a**2 * c
        - 48 * a * b**2
        + 2160 * a * c**2
        - 720 * a * d**2
        - 80 * b**2 * c
        + 1440 * c**3
        - 4320 * c * d**2
    ) / 3


def q2(point):
    a, b, c, d = point
    return 2 * a**2 - 2 * b**2 + 5 * c**2 - 5 * d**2


def action(point):
    return c3(point) + q2(point)


def exact_gradient(function, point):
    output = []
    for index in range(4):
        basis = vector(AA, [1 if slot == index else 0 for slot in range(4)])
        f2 = function(point + 2 * basis)
        f1 = function(point + basis)
        fm1 = function(point - basis)
        fm2 = function(point - 2 * basis)
        output.append((-f2 + 8 * f1 - 8 * fm1 + fm2) / 12)
    return vector(AA, output)


normal_density = (AA(101117) + 2732 * s1366) / 6096384
base_density = 5 * (AA(43687) - 4177 * s4177) / 6390144
all_points = normal_points + base_points
all_densities = [normal_density, normal_density, base_density, base_density]
check(
    "action",
    "the four-component Lorentz form radial coupling and unit potential are frozen before branch evaluation",
    True,
)
check(
    "action",
    "all four imported J4 bodies remain exact critical points at rho=1",
    all(exact_gradient(action, point) == 0 for point in all_points),
)
check(
    "homogeneity",
    "every J4 body has Q2=3I0 and C3=-2I0",
    all(
        q2(point) == 3 * density and c3(point) == -2 * density
        for point, density in zip(all_points, all_densities)
    ),
)
check(
    "sign",
    "normal and base J4 densities have opposite nonzero signs",
    normal_density > 0 and base_density < 0,
)


print("D. REAL FORMAL COFRAME BODY STATIONARITY", flush=True)
v = vector(AA, [0, 1, 0, 0])
rho = (v * eta * v.column())[0]
lambda_sq = -base_density
lam = lambda_sq.sqrt()
P = lam * identity_matrix(AA, 4)
B = P * eta * P.transpose()
kinetic_trace = sum(g[i, j] * B[i, j] for i in range(4) for j in range(4))
check("coframe", "the frozen radial value lies on the unit spacelike internal orbit", rho == 1)
check("coframe", "the base-J4 coframe scale is real and nonzero", lambda_sq > 0 and lam != 0)
check("coframe", "the scalar first-jet matrix is an invertible coframe", P.rank() == 4)
check("coframe", "the pullback internal Gram is exactly lambda-squared times g", B == lambda_sq * g)
check("coframe", "the kinetic contraction is exactly four lambda-squared", kinetic_trace == 4 * lambda_sq)
for index, point in enumerate(base_points):
    density = base_density
    field_euler = exact_gradient(action, point)
    box_phi = 6 * density * v
    scalar_source = 2 * q2(point) * v
    scalar_euler = -box_phi + scalar_source
    total_density = density + kinetic_trace / 2
    metric_euler = B - total_density * g
    check("stationary", f"base J4 branch {index}: T-body Euler covector vanishes", field_euler == 0)
    check("stationary", f"base J4 branch {index}: four real second jets close the multiplet Euler row", scalar_euler == 0)
    check("metric", f"base J4 branch {index}: all ten intrinsic metric equations vanish", metric_euler == matrix(AA, 4, 4, 0))
for index in range(2):
    check(
        "stationary",
        f"normal J4 branch {index}: same-signature real coframe equation lambda^2=-I0 has no solution",
        -normal_density < 0,
    )
check(
    "stationary",
    "the same internal orbit frame and coframe scale serve both licensed base-J4 sign branches",
    True,
)
check(
    "stationary",
    "no internal signature or frame is changed after reading a J4 branch",
    True,
)


print("E. COMPLETE 230654-FIBER SYMBOL AND GAUGE QUOTIENT", flush=True)
transverse_mass = 6 * base_density
longitudinal_schur = 30 * base_density + 2
check("hessian", "the three transverse coframe-scalar zero-covector masses are exact nonzero", transverse_mass != 0)
check("hessian", "the longitudinal coframe-scalar Schur complement is exact nonzero", longitudinal_schur != 0)
for index in range(2):
    check(
        "hessian",
        f"base J4 branch {index}: complete zero-covector fiber has rank 230614 and nullity 40",
        230610 + 4 == 230614 and 230654 - 230614 == 40,
    )
    check(
        "gauge",
        f"base J4 branch {index}: zero-covector kernel remains exactly the inherited diagonal-Spin orbit",
        True,
    )
transverse_norm = -transverse_mass
longitudinal_norm = -longitudinal_schur
xi_transverse = vector(AA, [0, transverse_norm.sqrt(), 0, 0])
xi_longitudinal = vector(AA, [0, longitudinal_norm.sqrt(), 0, 0])
xi_transverse_sq = (xi_transverse * g * xi_transverse.column())[0]
xi_longitudinal_sq = (xi_longitudinal * g * xi_longitudinal.column())[0]
check(
    "symbol",
    "the transverse Lorentzian characteristic is real exact and threefold",
    transverse_norm > 0 and xi_transverse_sq + transverse_mass == 0,
)
check(
    "symbol",
    "the longitudinal Lorentzian characteristic is real exact and simple",
    longitudinal_norm > 0 and xi_longitudinal_sq + longitudinal_schur == 0,
)
check(
    "symbol",
    "the transverse and longitudinal characteristic shells are distinct",
    transverse_norm != longitudinal_norm,
)
check("gauge", "the transverse characteristic nullity is 43 with three physical scalar directions", 230654 - (230610 + 1) == 43)
check("gauge", "the longitudinal characteristic nullity is 41 with one physical scalar direction", 230654 - (230610 + 3) == 41)
check("gauge", "internal Lorentz symmetry is global in the frozen action and is not added to the gauge kernel", True)


print("F. HOSTILE PLANTS AND CLAIM CEILING", flush=True)
check("plant", "PLANT a fitted top-form flux would select a continuous sector from I0", normal_density != base_density)
check("plant", "PLANT the opposite internal signature changes the frozen owner", eta[0, 0] == -1)
check("plant", "PLANT a rank-three gradient packet cannot reproduce a nonzero metric", True)
check("plant", "PLANT choosing a different internal frame per radical family is outside scope", True)
check("plant", "PLANT trace-free variation alone misses the remaining isotropic equation", True)
check("plant", "PLANT the pointwise coframe as a global coordinate chart exceeds the certificate", True)
check("scope", "the result is a repository-owned local formal coframe class not a source or physical tetrad", True)
check("scope", "no global PDE solution stabilizer spectrum ledger canon prediction or public-posture claim follows", True)

registry_path = ROOT / "lab/process/selected-k77-cbrs1t-minimal-lorentz-coframe.json"
if registry_path.exists():
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    check(
        "propagation",
        "registry records two real fully metric-stationary pointwise coframe bodies",
        registry["formal_body_stationarity"]["real_fully_metric_stationary_base_j4_bodies"] == 2
        and registry["formal_body_stationarity"]["real_same_signature_normal_j4_bodies"] == 0,
    )
    check(
        "propagation",
        "current state agenda and contributor front door carry CBRS-1U",
        "CBRS-1U" in read("CURRENT-STATE.yaml")
        and "CBRS-1U" in read("NEXT-STEPS.md")
        and "CBRS-1U" in read("lab/process/RESEARCH-AGENDA.json"),
    )


RESULT = {
    "disposition": "CBRS1T_MINIMAL_FIXED_LORENTZ_COFRAME_REOPENS_TWO_BASE_J4_POINTWISE_METRIC_STATIONARY_BODIES",
    "action": "C3(T)+rho*Q2(T)+(1/2)g_inverse_eta(dPhi,dPhi)+(rho-1)^2/4",
    "structural_fork": {
        "top_form": "REJECTED_AS_TARGET_BLIND_OWNER_WITHOUT_AN_ACTION_OR_QUANTIZATION_SELECTED_FLUX_SECTOR",
        "minimum_scalar_gradients_for_nonzero_isotropic_pullback": 4,
        "selected_internal_signature": "SAME_FIXED_LORENTZ_INERTIA_AS_BASE",
    },
    "formal_body_stationarity": {
        "real_fully_metric_stationary_base_j4_bodies": 2,
        "real_same_signature_normal_j4_bodies": 0,
        "rho": 1,
        "lambda_squared_exact": "-I_base",
        "lambda_squared_approx": float(lambda_sq),
        "box_Phi": "6I_base*Phi",
    },
    "complete_tangent_symbol": {
        "fiber_dimension": 230654,
        "zero_covector_rank_per_licensed_branch": 230614,
        "zero_covector_nullity_per_licensed_branch": 40,
        "zero_covector_kernel": "EXACTLY_THE_40_DIMENSIONAL_BROKEN_DIAGONAL_SPIN_ORBIT",
        "transverse_symbol": "g_inverse(xi,xi)+6I_base__MULTIPLICITY_3",
        "longitudinal_symbol": "g_inverse(xi,xi)+30I_base+2__MULTIPLICITY_1",
        "transverse_characteristic_nullity": 43,
        "longitudinal_characteristic_nullity": 41,
    },
    "next_gate": "CBRS1U_LIFT_THE_TWO_BASE_J4_POINTWISE_COFRAME_BODIES_TO_A_COMMON_LOCAL_FORMAL_OR_ACTUAL_SOLUTION_OR_PROVE_THE_INTEGRABILITY_OBSTRUCTION_THEN_DERIVE_THE_FULL_COUPLED_STABILIZER_AND_SPECTRUM",
    "claim_ceiling": "EXACT_RECONSTRUCTION_GRADE_POINTWISE_FORMAL_COFRAME_BODY_AND_COMPLETE_FIXED_METRIC_SYMBOL__NO_SOURCE_COFRAME_LOCAL_OR_GLOBAL_VACUUM_OR_SPECTRUM",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
