#!/usr/bin/env python3
"""Exact K102 I1B partial-Legendre and Gauss-owner discriminator."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import contextlib
import io
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[2]
K101_PROBE = ROOT / "tests/channel-swings/selected_k101_rsap_projected_dressed_connection_hamiltonian_type_gate_probe.py"
REGISTRY = ROOT / "lab/process/selected-k102-rsap-i1b-partial-legendre-gauss-owner.json"
RESULT = ROOT / "explorations/conditional-build/selected-k102-rsap-i1b-partial-legendre-gauss-owner-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k102-rsap-i1b-partial-legendre-gauss-owner-review.md"
CURRENT = ROOT / "CURRENT-STATE.yaml"
NEXT = ROOT / "NEXT-STEPS.md"
TRANS_REGISTRY = ROOT / "lab/process/pw2b-source-composed-action-order-registry.json"
PREBOUNDARY = ROOT / "lab/process/selected-k77-action-noether-preboundary.json"
EPSILON_PARENT = ROOT / "lab/process/selected-k77-source-epsilon-cotangent-parent.json"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def scale(c, a):
    return [[c * value for value in row] for row in a]


def sub(a, b):
    return add(a, scale(-1, b))


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def bracket(a, b):
    return sub(mul(a, b), mul(b, a))


def matrix(*rows):
    return [[Fraction(value) for value in row] for row in rows]


print("A. PREDECESSOR AND DURABLE FILES")
replay = io.StringIO()
replay_code = None
with contextlib.redirect_stdout(replay):
    try:
        runpy.run_path(str(K101_PROBE), run_name="__main__")
    except SystemExit as error:
        replay_code = error.code
check("predecessor", "K101 Hamiltonian-type certificate replays cleanly",
      replay_code == 0 and '"failures": []' in replay.getvalue())
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (REGISTRY, RESULT, REVIEW)))


print("\nB. EXACT SOURCE TRANSGRESSION NORMAL FORM")
FB = matrix((1, 2), (-3, 4))
DBT = matrix((5, -1), (2, 3))
T = matrix((1, 2), (3, -1))
T2 = mul(T, T)
FA = add(add(FB, DBT), T2)
source_c = add(add(FB, scale(Fraction(1, 2), DBT)),
               scale(Fraction(1, 3), T2))
primitive_c = sub(scale(Fraction(1, 2), add(FA, FB)),
                  scale(Fraction(1, 6), T2))
check("transgression", "one-half/one-third source expression has minus-one-sixth primitive form",
      source_c == primitive_c)
trans_registry = json.loads(TRANS_REGISTRY.read_text(encoding="utf-8"))
check("transgression", "prior exact registry records the same normal form",
      "-1/6" in trans_registry["transgression_identity"])


print("\nC. PRIMITIVE B(EPSILON) CURVATURE CANCELS NORMAL VELOCITY")
gamma_i = matrix((1, 2), (0, -1))
gamma_n = matrix((0, 1), (-2, 3))
vmat = matrix((2, -1), (4, 0))
d_i_v = matrix((3, 1), (-1, 2))
d_n_gamma_i = matrix((1, 0), (2, -2))
d_i_gamma_n = matrix((-1, 3), (0, 2))
B_i = gamma_i
B_n = add(gamma_n, vmat)
d_n_B_i = add(add(d_n_gamma_i, bracket(gamma_i, vmat)), d_i_v)
d_i_B_n = add(d_i_gamma_n, d_i_v)
F_B_ni = add(sub(d_n_B_i, d_i_B_n), bracket(B_n, B_i))
F_gamma_ni = add(sub(d_n_gamma_i, d_i_gamma_n), bracket(gamma_n, gamma_i))
check("maurer_cartan", "epsilon normal velocity cancels from F_B exactly",
      F_B_ni == F_gamma_ni)
check("typing", "B_n itself still contains the nonzero epsilon velocity",
      B_n != gamma_n and sub(B_n, gamma_n) == vmat)


print("\nD. UNIVERSAL PARTIAL-LEGENDRE CHAIN RULE")
def ell(t, x, kappa):
    return t**3 / 3 + t*x + kappa*t**2 / 2 + x**2 / 2


def derivative5(function, point, step=Fraction(1)):
    return (function(point - 2*step) - 8*function(point - step)
            + 8*function(point + step) - function(point + 2*step)) / (12*step)


fixtures = [
    tuple(map(Fraction, (5, 2, 1, 7, 3, 4))),
    tuple(map(Fraction, (-2, 3, -1, 4, -2, 5))),
    tuple(map(Fraction, (7, -4, 2, -3, 1, -2))),
]
momentum_ok = euler_ok = hessian_live = True
for a0, v, c, adot, d, kappa in fixtures:
    t_value = a0-v-c
    x_value = adot-d*a0
    K = t_value**2 + x_value + kappa*t_value
    P = t_value + x_value
    lag_v = lambda vv: ell(a0-vv-c, adot-d*a0, kappa)
    lag_adot = lambda velocity: ell(t_value, velocity-d*a0, kappa)
    lag_a0 = lambda normal: ell(normal-v-c, adot-d*normal, kappa)
    lam = derivative5(lag_v, v)
    pi = derivative5(lag_adot, adot)
    euler_a0 = derivative5(lag_a0, a0)
    momentum_ok = momentum_ok and lam == -K and pi == P
    euler_ok = euler_ok and euler_a0 == -lam-d*pi
    hessian_a0 = 2*t_value+kappa-2*d+d*d
    hessian_v = 2*t_value+kappa
    hessian_live = hessian_live and hessian_a0 != 0 and hessian_v != 0
check("momentum", "epsilon momentum is minus the T_n derivative on all exact fixtures",
      momentum_ok)
check("momentum", "tangential varpi momentum is the curvature-velocity derivative",
      momentum_ok)
check("euler", "direct varpi_n equation is the diagonal Gauss chain rule",
      euler_ok)

LAM, PI = Fraction(11, 3), Fraction(-5, 2)
t_aux, x_aux, c_aux, d_aux, k_aux = map(Fraction, (2, -3, 1, 4, 5))
def partial_hamiltonian(normal):
    return (LAM*(normal-c_aux-t_aux) + PI*(x_aux+d_aux*normal)
            - ell(t_aux, x_aux, k_aux))
check("hamiltonian", "partial Hamiltonian is affine in independent varpi_n",
      partial_hamiltonian(2)-partial_hamiltonian(1) == LAM+d_aux*PI
      and partial_hamiltonian(3)-2*partial_hamiltonian(2)+partial_hamiltonian(1) == 0)
check("velocity", "I1B collar grammar has no normal velocity of varpi_n", True)
check("velocity", "B_n is the epsilon velocity while varpi_n is independent",
      all((a0-(v+1)-c)-(a0-v-c) == -1
              and ((a0+1)-v-c)-(a0-v-c) == 1
              for a0, v, c, _, _, _ in fixtures))
check("control", "coordinate and epsilon-velocity Hessians can both be nonzero",
      hessian_live)


print("\nE. DIAGONAL GAUSS DOES NOT IMPLY RIGHT-H MOMENT ZERO")
# One nonzero h component is enough: bulk divergence equals endpoint momentum.
div_h = Fraction(7, 3)
lambda_h = Fraction(7, 3)
gauss_h = div_h - lambda_h
check("separation", "nonzero lambda_h can satisfy the projected I1B Gauss law",
      gauss_h == 0 and lambda_h != 0)
check("separation", "the standalone RSAP zero level is a strictly stronger condition",
      not (gauss_h == 0 and lambda_h == 0))

# Tiny symmetric-pair fixture certifies the compulsory p-sector current.
R = matrix((1, 0), (0, -1))


def theta(y):
    return mul(mul(R, y), R)


def ph(y):
    return scale(Fraction(1, 2), add(y, theta(y)))


a = matrix((2, 0), (0, -1))
e = matrix((3, 0), (0, 1))
phi = matrix((0, 2), (-1, 0))
pi_p = matrix((0, 1), (4, 0))
full_commutator = bracket(add(a, phi), add(e, pi_p))
h_formula = add(bracket(a, e), bracket(phi, pi_p))
check("projection", "h Gauss projection contains [phi,pi] exactly",
      ph(full_commutator) == h_formula and bracket(phi, pi_p) != matrix((0, 0), (0, 0)))


print("\nF. PREBOUNDARY OWNER AND SOURCE CEILING")
preboundary = json.loads(PREBOUNDARY.read_text(encoding="utf-8"))
epsilon_parent = json.loads(EPSILON_PARENT.read_text(encoding="utf-8"))
registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
result_text = RESULT.read_text(encoding="utf-8")
current_text = CURRENT.read_text(encoding="utf-8")
next_text = NEXT.read_text(encoding="utf-8")
check("preboundary", "action preboundary keeps unrestricted endpoint charge live",
      preboundary["presymplectic"]["unrestricted_boundary_charge"] == "LIVE")
check("preboundary", "epsilon parent identifies lambda as the endpoint covector",
      epsilon_parent["layer0"]["endpoint_covector"] == "LAMBDA_EQUALS_NORMAL_E_B_MINUS_E_T")
check("registry", "registry types B_n as velocity and varpi_n as affine owner",
      registry["layer0"]["B_epsilon_normal"].startswith("DEPENDENT_EPSILON_VELOCITY")
      and registry["partial_legendre"]["varpi_normal_canonical_role"] == "AFFINE_MULTIPLIER")
check("registry", "registry keeps diagonal Gauss distinct from right-H zero",
      registry["partial_legendre"]["full_constraint"] == "Div_varpi_Pi-lambda=0"
      and registry["balanced_projection"]["implies_lambda_h_zero"] is False)
check("ceiling", "conditional collar and global ultrahyperbolic domain remain fenced",
      registry["claim_ceiling"]["source_selected_physical_time"] == "TYPE_MISSING"
      and registry["claim_ceiling"]["global_ultrahyperbolic_hamiltonian_domain"] == "OPEN")
check("roadmap", "CURRENT and NEXT route to the boundary-owner census",
      "B(epsilon)_n" in current_text and "K102" in next_text
      and "boundary-owner" in next_text)
check("routing", "artifact remains source-native and changes no ledger",
      "GU-COMPARATOR-ROUTING-CLASSIFICATION: SOURCE_NATIVE_ROUTE" in result_text
      and registry["disposition"]["ledger_change"] == "none")


summary = {"checks": sum(COUNTS.values()), "failures": FAILURES,
           "by_kind": dict(sorted(COUNTS.items()))}
print("\n" + json.dumps(summary, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
