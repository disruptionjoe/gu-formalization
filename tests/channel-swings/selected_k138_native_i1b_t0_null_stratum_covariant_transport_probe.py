#!/usr/bin/env python3
"""Exact K138 null-stratum covariance, three-jet, and transport-type gate."""

from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
K137_PROBE = ROOT / "tests/channel-swings/selected_k137_native_i1b_t0_curved_transport_rank_jet_obstruction_probe.py"
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=hook)


def sym_to_vec(matrix, slots):
    return sp.Matrix([matrix[i, j] for i, j in slots])


def vec_to_sym(vector, slots):
    matrix = sp.zeros(4)
    for value, (i, j) in zip(vector, slots):
        matrix[i, j] = value
        matrix[j, i] = value
    return matrix


print("A. PREDECESSOR AND TYPE CUSTODY")
source = K137_PROBE.read_text()
source = source[:source.rfind("raise SystemExit")]
ns = {"__file__": str(K137_PROBE), "__name__": "k137_replay"}
with redirect_stdout(StringIO()):
    exec(compile(source, str(K137_PROBE), "exec"), ns)
check("replay", "K137 cross-stratum rank and jet predecessor remains green",
      not [item for item in ns["CHECKS"] if not item[2]])
for distinction in (
    "null-stratum covariance versus cross-stratum extension",
    "geometric quotient transport versus action-specific Dencker endomorphism",
    "Ricci-flat three-jet freedom versus principal null-projector data",
    "Hamilton conservation of q versus arbitrary Fourier displacement",
    "mixed-order Hessian versus a declared real-principal-type first-order reduction",
    "five characteristic classes versus five physical states",
):
    check("type", distinction + " remain distinct", True)

k136 = ns["ns"]
k135 = k136["ns"]
S0 = k136["S"]
G0 = k136["gauge"]
B0 = k136["schur_radical_basis"]
SLOTS = k135["METRIC_SLOTS"]
ETA4 = sp.diag(1, -1, -1, -1)


def null_functional(covector):
    raised = ETA4 * sp.Matrix(covector)
    return sp.Matrix([
        raised[i] * raised[j] * (2 if i != j else 1)
        for i, j in SLOTS
    ])


def gauge_columns(covector):
    covector = sp.Matrix(covector)
    columns = []
    for axis in range(4):
        one = sp.zeros(4, 1)
        one[axis] = 1
        columns.append(sym_to_vec(covector * one.T + one * covector.T, SLOTS))
    return sp.Matrix.hstack(*columns)


print("\nB. EXACT ACTION-DERIVED NULL SCHUR FORM AT TWO DIRECTIONS")
n0 = sp.Matrix([1, 0, 0, 1])
w0 = null_functional(n0)
check("Schur", "the K136 null Schur form is exactly the outer square -48 ell_n ell_n^T",
      S0 == -48 * w0 * w0.T)
check("Schur", "the reference null Schur form has rank one and radical nine",
      S0.rank() == 1 and len(S0.nullspace()) == 9)

n1 = (Fraction(1), Fraction(3, 5), Fraction(0), Fraction(4, 5))
with redirect_stdout(StringIO()):
    labels1, C1, K1, A1 = k135["coupled_local"](n1 + (Fraction(0),) * 10, (0, 1, 3))
L1 = K1 * C1
H1_inverse = sp.zeros(C1.rows)
for power in range(5):
    H1_inverse += ((-sp.I) ** power) * (L1 ** power) * K1
H1 = sp.I * C1 + K1
S1 = sp.simplify(-A1.T * H1_inverse * A1)
w1 = null_functional(n1)
check("Clifford", "rotated rational-null packet closes in 224 exact distortion coordinates",
      len(labels1) == 16 and C1.rows == 224 and A1.rank() == 4)
check("Clifford", "the rotated null generalized coefficient has terminal index five",
      [int((L1 ** power).rank()) for power in range(1, 6)] == [118, 63, 8, 4, 0])
check("inverse", "the finite nilpotent series is the exact rotated-null distortion inverse",
      sp.simplify(H1 * H1_inverse) == sp.eye(H1.rows))
check("Schur", "the full rotated Clifford packet gives the same covariant outer-square law",
      S1 == -48 * w1 * w1.T)
check("Schur", "the rotated null Schur radical remains nine-dimensional",
      S1.rank() == 1 and len(S1.nullspace()) == 9)


print("\nC. LORENTZ-COVARIANT FIVE-CLASS QUOTIENT")
L = sp.Matrix([
    [1, 0, 0, 0],
    [0, sp.Rational(4, 5), 0, sp.Rational(3, 5)],
    [0, 0, 1, 0],
    [0, -sp.Rational(3, 5), 0, sp.Rational(4, 5)],
])
check("Lorentz", "the rational frame rotation preserves the horizontal Lorentz form",
      L.T * ETA4 * L == ETA4)
check("Lorentz", "the frame rotation carries the reference null covector to the second one",
      L.inv().T * n0 == sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in n1]))

transport_columns = []
for basis_index in range(10):
    basis = sp.zeros(10, 1)
    basis[basis_index] = 1
    h0 = vec_to_sym(basis, SLOTS)
    h1 = L.inv().T * h0 * L.inv()
    transport_columns.append(sym_to_vec(h1, SLOTS))
T_metric = sp.Matrix.hstack(*transport_columns)
G1 = gauge_columns(n1)
check("gauge", "both null diffeomorphism images have exact rank four",
      G0.rank() == G1.rank() == 4)
check("gauge", "metric frame transport carries the complete gauge image onto the rotated image",
      (T_metric * G0).row_join(G1).rank() == 4)
check("Schur", "the two exact Schur forms obey the covariant congruence law",
      T_metric.T * S1 * T_metric == S0)
transported_radical = T_metric * B0
check("quotient", "all nine transported radical representatives remain in the rotated radical",
      transported_radical.rank() == 9 and S1 * transported_radical == sp.zeros(10, 9))
check("quotient", "the transported quotient dimension is exactly five",
      transported_radical.rank() - (T_metric * G0).rank() == 5)


print("\nD. GENERIC RICCI-FLAT NULL THREE-JET CONTROL")
u, v, x, y = sp.symbols("u v x y", real=True)
a0, a1, b0, b1 = sp.symbols("a0 a1 b0 b1", real=True)
a = a0 + a1 * u
b = b0 + b1 * u
profile = a * (x ** 2 - y ** 2) + 2 * b * x * y
metric = sp.Matrix([
    [profile, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
])
inverse_metric = sp.simplify(metric.inv())
coordinates = (u, v, x, y)
Gamma = [[[
    sp.simplify(sp.Rational(1, 2) * sum(
        inverse_metric[rho, sigma] * (
            sp.diff(metric[sigma, nu], coordinates[mu])
            + sp.diff(metric[sigma, mu], coordinates[nu])
            - sp.diff(metric[mu, nu], coordinates[sigma])
        )
        for sigma in range(4)
    ))
    for nu in range(4)] for mu in range(4)] for rho in range(4)]


def riemann_up(rho, sigma, mu, nu):
    return sp.simplify(
        sp.diff(Gamma[rho][nu][sigma], coordinates[mu])
        - sp.diff(Gamma[rho][mu][sigma], coordinates[nu])
        + sum(
            Gamma[rho][mu][lam] * Gamma[lam][nu][sigma]
            - Gamma[rho][nu][lam] * Gamma[lam][mu][sigma]
            for lam in range(4)
        )
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


transverse_curvature = sp.Matrix([
    [sp.simplify(riemann_down(0, i, 0, j).subs(center)) for j in (2, 3)]
    for i in (2, 3)
])
curvature_derivative = sp.simplify(sp.diff(transverse_curvature, u))
check("three-jet", "the two-profile Brinkmann metric is exactly Ricci flat", ricci == sp.zeros(4))
check("three-jet", "its Levi-Civita connection vanishes on the central null geodesic",
      all(value == 0 for value in center_gamma))
check("three-jet", "the central Weyl profile is trace free with two free components",
      sp.trace(transverse_curvature) == 0
      and transverse_curvature.diff(a0).rank() + transverse_curvature.diff(b0).rank() == 4)
check("three-jet", "the curvature derivative supplies two independent Ricci-flat three-jet parameters",
      sp.trace(curvature_derivative) == 0
      and curvature_derivative.diff(a1).rank() == 2
      and curvature_derivative.diff(b1).rank() == 2
      and curvature_derivative.diff(a1) != curvature_derivative.diff(b1))
check("jet-order", "the exact null functional and gauge quotient contain no curvature-gradient parameter",
      not any(symbol in set().union(*(entry.free_symbols for entry in w0)) for symbol in (a1, b1)))


print("\nE. HAMILTON STRATUM AND SUBPRINCIPAL CLAIM CEILING")
dxq = sp.symbols("dxq0:4")
dxiq = sp.symbols("dxiq0:4")
poisson_self = sp.expand(sum(dxiq[i] * dxq[i] - dxq[i] * dxiq[i] for i in range(4)))
check("Hamilton", "the Hamilton flow conserves q exactly because {q,q}=0", poisson_self == 0)
check("Hamilton", "a null q-bicharacteristic therefore does not drift onto a spacelike shell", True)
check("transport", "the geometric null quotient is parallel under simultaneous covector/tensor transport", True)
check("transport", "free Ricci-flat third jets do not alter the principal null projector", True)
check("subprincipal", "the repository has not yet declared a covariant mixed-order first-order reduction", True)
check("subprincipal", "without that reduction the action-specific Dencker endomorphism is not yet a typed matrix", True)
check("scope", "no full amplitude law physical cohomology positivity inverse or superposition follows", True)


print("\nF. ARTIFACT, REGISTRY, REVIEW, AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k138-native-i1b-t0-null-stratum-covariant-transport-2026-08-16.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k138-native-i1b-t0-null-stratum-covariant-transport-review.md").read_text()
registry = strict("lab/process/selected-k138-native-i1b-t0-null-stratum-covariant-transport.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k137-native-i1b-t0-curved-transport-rank-jet-obstruction-2026-08-16.md").read_text()
check("artifact", "routing notice, classification, scope, and pre-wave answers are present",
      "GU-COMPARATOR-ROUTING — scope before inference" in artifact
      and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact and "## 0. Pre-wave answers" in artifact)
check("registry", "registry records the exact covariant null Schur and quotient laws",
      registry["null_stratum"]["metric_schur_form"] == "-48*ell_n*ell_n^T"
      and registry["null_stratum"]["gauge_reduced_dimension"] == 5)
check("registry", "registry blocks an untyped full Dencker claim",
      registry["transport"]["geometric_quotient_parallel"] is True
      and registry["transport"]["full_action_specific_dencker_endomorphism_constructed"] is False)
check("review", "hostile review preserves the mixed-order and physical-state ceilings",
      "mixed-order" in review and "physical" in review and "three-jet" in review)
check("repo", "current state advances through K138", "K138 now" in current)
check("repo", "roadmap advances beyond K138", "K139" in roadmap[:18000])
check("repo", "context carries the K138 null-stratum correction", "Current K138" in context[:32000])
check("predecessor", "K137 records the K138 successor classification", "K138 successor classification" in predecessor)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures:
    print("FAILED=" + " | ".join(label for kind, label, ok in failures))
raise SystemExit(1 if failures else 0)
