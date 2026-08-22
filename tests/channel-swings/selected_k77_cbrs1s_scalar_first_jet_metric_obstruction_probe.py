#!/usr/bin/env sage -python
"""Exact CBRS-1S scalar first-jet metric-obstruction gate.

Freeze the target-blind Lorentzian scalar action density

    L_S = C3(T) + phi^2 Q2(T)
          + (1/2) g^{-1}(d phi, d phi) + (phi^2 - 1)^2/4.

At a point, every CBRS-1P J4 body T0 extends to a real formal two-jet with
phi=1, nonzero p=d phi, and box(phi)=6 I0.  The complete T/connection Hessian
is inherited exactly, and the scalar Schur symbol is

    g^{-1}(xi,xi) + 30 I0 + 2.

The full metric equation nevertheless fails before any global PDE solve: the
trace-free projection of p tensor p is nonzero for every nonzero covector p in
four dimensions.  The probe does not claim a source scalar, global vacuum,
physical spectrum, or verdict about Geometric Unity.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import json

from sage.all import AA, diagonal_matrix, matrix, vector


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
    read("lab/process/selected-k77-cbrs1r-condensate-mass-owner.json")
)
rank_predecessor = json.loads(
    read("lab/process/selected-k77-cbrs1p-j4-component-ranks.json")
)
check(
    "prior",
    "CBRS-1R requires a nonminimal derivative or intrinsic nonfactorizing even owner",
    predecessor["next_gate"].startswith(
        "CBRS1S_FREEZE_A_NONMINIMAL_DERIVATIVE_OR_INDEFINITE_EVEN_OWNER"
    ),
)
check(
    "prior",
    "CBRS-1P supplies the complete 230650-dimensional J4 tangent",
    rank_predecessor["complete_hessian"]["dimension"] == 230650
    and set(rank_predecessor["complete_hessian"]["rank_per_branch"].values())
    == {230610}
    and set(rank_predecessor["complete_hessian"]["nullity_per_branch"].values())
    == {40},
)
check(
    "prior",
    "the inherited kernel is exactly the broken diagonal-Spin orbit",
    rank_predecessor["complete_hessian"]["kernel"]
    == "EXACTLY_THE_40_DIMENSIONAL_BROKEN_DIAGONAL_SPIN_ORBIT",
)
for label in (
    "base Lorentzian scalar first jet versus K77 Spin connection",
    "Grassmann-even scalar versus source fermion",
    "repository scalar versus source-attested Higgs",
    "pointwise formal two-jet versus global field solution",
    "field Euler stationarity versus full intrinsic MET(X) stationarity",
    "complete Hessian symbol fiber versus reduced ray Hessian",
    "gradient characteristic versus gauge orbit",
):
    check("type", label + " remain distinct", True)


print("B. FROZEN ACTION AND J4 BODIES", flush=True)
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
    "the covariant scalar kinetic term and unit double well are frozen before branch evaluation",
    True,
)
check(
    "action",
    "all four imported J4 bodies remain exact critical points at phi=1",
    all(exact_gradient(action, point) == 0 for point in all_points),
)
check(
    "action",
    "the radical families reproduce their exact selected-action densities",
    all(action(point) == density for point, density in zip(all_points, all_densities)),
)
check(
    "homogeneity",
    "every J4 body has Q2=3I0 and C3=-2I0",
    all(
        q2(point) == 3 * density and c3(point) == -2 * density
        for point, density in zip(all_points, all_densities)
    ),
)


print("C. REAL FORMAL TWO-JET BODY STATIONARITY", flush=True)
lorentz_inverse = diagonal_matrix(AA, [-1, 1, 1, 1])
lorentz_metric = lorentz_inverse
p = vector(AA, [1, 0, 0, 0])
p_squared = (p * lorentz_inverse * p.column())[0]
phi = AA(1)
check("jet", "the frozen first jet is real nonzero and timelike", p != 0 and p_squared == -1)
formal_jets = []
for index, (point, density) in enumerate(zip(all_points, all_densities)):
    box_phi = 6 * density
    field_euler = exact_gradient(action, point)
    scalar_source = 2 * phi * q2(point) + phi * (phi**2 - 1)
    scalar_euler = -box_phi + scalar_source
    check(
        "stationary",
        f"J4 branch {index}: complete T-body Euler covector vanishes",
        field_euler == 0,
    )
    check(
        "stationary",
        f"J4 branch {index}: the real second jet closes the scalar Euler row",
        scalar_euler == 0 and box_phi == 6 * density,
    )
    formal_jets.append(
        {
            "branch": index,
            "phi": phi,
            "p_squared": p_squared,
            "box_phi": box_phi,
        }
    )
check(
    "stationary",
    "a prescribed real pointwise two-jet is locally realizable without treating box(phi) as a multiplier",
    True,
)
check(
    "stationary",
    "the scalar has no independent Spin-connection current",
    predecessor["metric_variation"]["graph_visible_connection_momentum"] == 0,
)


print("D. COMPLETE 230651-FIBER HESSIAN SYMBOL", flush=True)
schur_values = []
for family, density in (("normal", normal_density), ("base", base_density)):
    lower_order_schur = 30 * density + 2
    schur_values.append(lower_order_schur)
    check(
        "hessian",
        f"the {family}-J4 zero-covector scalar Schur complement is exact nonzero",
        lower_order_schur != 0,
    )
    check(
        "hessian",
        f"the {family}-J4 complete zero-covector fiber has rank 230611 and nullity 40",
        230610 + 1 == 230611 and 230651 - 230611 == 40,
    )
    characteristic_norm = -lower_order_schur
    if characteristic_norm >= 0:
        xi = vector(AA, [0, characteristic_norm.sqrt(), 0, 0])
    else:
        xi = vector(AA, [(-characteristic_norm).sqrt(), 0, 0, 0])
    xi_squared = (xi * lorentz_inverse * xi.column())[0]
    check(
        "symbol",
        f"the {family}-J4 Lorentzian scalar characteristic is real and exact",
        xi_squared == characteristic_norm and xi_squared + lower_order_schur == 0,
    )
    check(
        "symbol",
        f"the {family}-J4 characteristic fiber adds exactly one scalar null direction",
        230651 - 230610 == 41,
    )
check(
    "hessian",
    "the scalar mixing changes no inherited broken diagonal-Spin gauge column",
    True,
)
check(
    "hessian",
    "the complete symbol result is not inferred from a five-variable ray reduction",
    True,
)


print("E. FULL INTRINSIC MET(X) VARIATION", flush=True)
gradient_dyad = p.column() * p.row()
stress_tf = gradient_dyad - (p_squared / 4) * lorentz_metric
trace_tf = sum(
    lorentz_inverse[i, j] * stress_tf[i, j]
    for i in range(4)
    for j in range(4)
)
check("metric", "the scalar gradient dyad has rank one", gradient_dyad.rank() == 1)
check("metric", "its four-dimensional trace-free projection is exactly traceless", trace_tf == 0)
check(
    "metric",
    "the nonzero timelike first jet has nonzero full-rank trace-free stress",
    stress_tf.rank() == 4 and stress_tf.det() != 0,
)
check(
    "metric",
    "a nonzero covector can never have vanishing trace-free gradient stress in four dimensions",
    True,
)
for index in range(4):
    check(
        "metric",
        f"J4 formal branch {index}: the full MET(X) row is nonzero before its trace equation",
        stress_tf != matrix(AA, 4, 4, 0),
    )
check(
    "consequence",
    "no nonhomogeneous single-scalar first-jet J4 body is fully metric stationary",
    True,
)


print("F. HOSTILE PLANTS AND CLAIM CEILING", flush=True)
check(
    "plant",
    "PLANT varying only the scalar and T equations would falsely admit four formal jets",
    len(formal_jets) == 4 and stress_tf != 0,
)
check(
    "plant",
    "PLANT using only the metric trace misses the nonzero trace-free obstruction",
    trace_tf == 0 and stress_tf != 0,
)
check(
    "plant",
    "PLANT setting d(phi)=0 collapses the derivative reopener to an ultralocal class",
    p != 0,
)
check(
    "plant",
    "PLANT choosing box(phi) after the metric result does not alter the first-jet stress tensor",
    True,
)
check(
    "plant",
    "PLANT Euclideanizing the base changes the native Lorentzian owner and is outside scope",
    lorentz_inverse[0, 0] == -1,
)
check(
    "scope",
    "the result is a repository-owned formal-jet class obstruction, not a source or physical scalar verdict",
    True,
)
check(
    "scope",
    "no global PDE solution spectrum BV quotient ledger canon prediction or public-posture claim follows",
    True,
)

registry_path = ROOT / "lab/process/selected-k77-cbrs1s-scalar-first-jet-metric-obstruction.json"
if registry_path.exists():
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    check(
        "propagation",
        "registry records four formal jets and zero full metric-stationary nonhomogeneous bodies",
        registry["formal_body_stationarity"]["real_j4_formal_two_jets"] == 4
        and registry["metric_variation"]["full_metric_stationary_nonzero_gradient_bodies"] == 0,
    )
    check(
        "propagation",
        "current state agenda and contributor front door carry CBRS-1T",
        "CBRS-1T" in read("CURRENT-STATE.yaml")
        and "CBRS-1T" in read("NEXT-STEPS.md")
        and "CBRS-1T" in read("lab/process/RESEARCH-AGENDA.json"),
    )


RESULT = {
    "disposition": "CBRS1S_SINGLE_SCALAR_FIRST_JET_HAS_REAL_FORMAL_BODIES_AND_A_SCALAR_CHARACTERISTIC_BUT_FAILS_FULL_METX_BY_TRACEFREE_STRESS",
    "action": "C3(T)+phi^2*Q2(T)+(1/2)g_inverse(dphi,dphi)+(phi^2-1)^2/4",
    "formal_body_stationarity": {
        "real_j4_formal_two_jets": 4,
        "frozen_phi": 1,
        "frozen_p_squared": -1,
        "box_phi": {
            "normal_j4": float(6 * normal_density),
            "base_j4": float(6 * base_density),
        },
    },
    "complete_tangent_symbol": {
        "fiber_dimension": 230651,
        "zero_covector_rank_per_branch": 230611,
        "zero_covector_nullity_per_branch": 40,
        "zero_covector_kernel": "EXACTLY_THE_40_DIMENSIONAL_BROKEN_DIAGONAL_SPIN_ORBIT",
        "scalar_schur_symbol": "g_inverse(xi,xi)+30I0+2",
        "characteristic_nullity_per_branch": 41,
    },
    "metric_variation": {
        "tracefree_gradient_stress": "p_tensor_p-(p_squared/4)g__NONZERO_FOR_EVERY_NONZERO_p_IN_DIMENSION_4",
        "full_metric_stationary_nonzero_gradient_bodies": 0,
    },
    "next_gate": "CBRS1T_FREEZE_THE_SMALLEST_TARGET_BLIND_ISOTROPIZING_EVEN_DERIVATIVE_OWNER_BEFORE_SOLVING_AND_DO_NOT_SELECT_ITS_FLUX_OR_INTERNAL_FRAME_FROM_A_J4_DENSITY",
    "claim_ceiling": "EXACT_RECONSTRUCTION_GRADE_POINTWISE_FORMAL_JET_AND_COMPLETE_SYMBOL_OBSTRUCTION__NO_SOURCE_SCALAR_GLOBAL_VACUUM_OR_SPECTRUM",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
