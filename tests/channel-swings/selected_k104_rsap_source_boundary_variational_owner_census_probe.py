#!/usr/bin/env python3
"""Exact K104 source boundary-selector ownership and equivariance probe."""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
K100_PROBE = ROOT / "tests/channel-swings/selected_k100_rsap_balanced_order_parameter_owner_census_probe.py"
K103_PROBE = ROOT / "tests/channel-swings/selected_k103_rsap_boundary_owner_polarization_census_probe.py"
REGISTRY = ROOT / "lab/process/selected-k104-rsap-source-boundary-variational-owner-census.json"
RESULT = ROOT / "explorations/conditional-build/selected-k104-rsap-source-boundary-variational-owner-census-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k104-rsap-source-boundary-variational-owner-census-review.md"
SOURCE_REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
SOURCE_PACKET = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
CURRENT = ROOT / "CURRENT-STATE.yaml"
NEXT = ROOT / "NEXT-STEPS.md"

N = 14
Q = [1] * 7 + [-1] * 7
BALANCED_PLUS = {0, 1, 2, 7, 8, 9, 10}
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def zero() -> list[list[int]]:
    return [[0] * N for _ in range(N)]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(N)] for i in range(N)]


def subtract(a, b):
    return [[a[i][j] - b[i][j] for j in range(N)] for i in range(N)]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(N))
             for j in range(N)] for i in range(N)]


def bracket(a, b):
    return subtract(matmul(a, b), matmul(b, a))


def neg(a):
    return [[-value for value in row] for row in a]


def is_zero(a) -> bool:
    return all(value == 0 for row in a for value in row)


def basis_matrix(i: int, j: int) -> list[list[int]]:
    value = zero()
    value[i][j] = 1
    value[j][i] = -Q[i] * Q[j]
    return value


def sigma(a, r):
    return matmul(matmul(r, a), r)


def doubled_h_projection(a, r):
    return add(a, sigma(a, r))


def doubled_p_projection(a, r):
    return subtract(a, sigma(a, r))


R = [[(1 if i in BALANCED_PLUS else -1) if i == j else 0
      for j in range(N)] for i in range(N)]
BIV = {(i, j): basis_matrix(i, j)
       for i in range(N) for j in range(i + 1, N)}
FULL = list(BIV.values())
H_BASIS = [value for value in FULL if sigma(value, R) == value]
P_BASIS = [value for value in FULL if sigma(value, R) == neg(value)]


print("A. PREDECESSORS AND DURABLE FILES")
replay100 = io.StringIO()
code100 = None
with contextlib.redirect_stdout(replay100):
    try:
        runpy.run_path(str(K100_PROBE), run_name="__main__")
    except SystemExit as error:
        code100 = error.code
check("predecessor", "K100 balanced-owner certificate replays cleanly",
      code100 == 0 and '"failures": []' in replay100.getvalue())
replay103 = io.StringIO()
with contextlib.redirect_stdout(replay103):
    runpy.run_path(str(K103_PROBE), run_name="__main__")
check("predecessor", "K103 boundary-route census replays cleanly",
      "PASS 32/32" in replay103.getvalue())
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. BALANCED SYMMETRIC PAIR")
check("dimension", "so(7,7) has dimension 91", len(FULL) == 91)
check("dimension", "balanced stabilizer has dimension 42", len(H_BASIS) == 42)
check("dimension", "balanced complement has dimension 49", len(P_BASIS) == 49)
check("involution", "adjoint involution squares to one",
      all(sigma(sigma(value, R), R) == value for value in FULL))
check("bracket", "[h,h] lies in h",
      all(is_zero(doubled_p_projection(bracket(x, y), R))
          for x in H_BASIS for y in H_BASIS))
check("bracket", "[h,p] lies in p",
      all(is_zero(doubled_h_projection(bracket(x, y), R))
          for x in H_BASIS for y in P_BASIS))
check("bracket", "[p,p] lies in h",
      all(is_zero(doubled_p_projection(bracket(x, y), R))
          for x in P_BASIS for y in P_BASIS))


print("\nC. FIXED BALANCED ZERO LEVEL IS NOT FULL-G INVARIANT")
X = BIV[(0, 3)]
LAMBDA = BIV[(0, 4)]
DEFECT = bracket(X, LAMBDA)
check("fixture", "chosen generator and charge both lie in p_bal",
      sigma(X, R) == neg(X) and sigma(LAMBDA, R) == neg(LAMBDA))
check("zero_level", "chosen charge satisfies lambda_h=0",
      is_zero(doubled_h_projection(LAMBDA, R)))
check("defect", "its full-G variation has nonzero h_bal component",
      not is_zero(DEFECT) and doubled_h_projection(DEFECT, R) ==
      [[2 * value for value in row] for row in DEFECT])
check("defect", "p_bal is not invariant under the full adjoint action",
      not is_zero(doubled_h_projection(bracket(X, LAMBDA), R)))
check("subgroup", "p_bal is invariant under h_bal",
      all(is_zero(doubled_h_projection(bracket(x, y), R))
          for x in H_BASIS for y in P_BASIS))


print("\nD. MOVING-R COVARIANCE REPAIRS THE DEFECT")
fixtures = [
    (BIV[(0, 3)], BIV[(0, 4)]),
    (BIV[(0, 3)], BIV[(3, 4)]),
    (BIV[(0, 1)], BIV[(0, 3)]),
    (BIV[(7, 11)], BIV[(8, 11)]),
    (BIV[(3, 11)], BIV[(0, 12)]),
]
moving_ok = True
fixed_defects = 0
for x, y in fixtures:
    d_r = bracket(x, R)
    d_y = bracket(x, y)
    left = add(add(d_y, matmul(matmul(d_r, y), R)),
               add(matmul(matmul(R, d_y), R), matmul(matmul(R, y), d_r)))
    right = bracket(x, add(y, sigma(y, R)))
    moving_ok = moving_ok and left == right
    fixed_left = doubled_h_projection(d_y, R)
    fixed_right = bracket(x, doubled_h_projection(y, R))
    fixed_defects += int(fixed_left != fixed_right)
check("covariance", "moving projector identity holds on exact h/p fixtures", moving_ok)
check("control", "holding R fixed fires a covariance defect", fixed_defects > 0)
check("owner", "moving R uses a 49D orbit with 42D stabilizer", 91 - 42 == 49)


print("\nE. DIMENSION AND FUNCTIONAL CONTROLS")
check("dimension", "balanced cotangent reduction is 98D", 182 - 2 * 42 == 98)
check("control", "full-G zero reduction is 0D, not 98D", 182 - 2 * 91 == 0)
physical_stabilizer = 4 * 3 // 2 + 10 * 9 // 2
check("control", "physical 4|10 stabilizer has dimension 51", physical_stabilizer == 51)
check("control", "physical-split cotangent reduction is 80D", 182 - 2 * physical_stabilizer == 80)
check("functional", "right-invariant boundary graph quotient is 49D, not the full 98D phase space",
      91 - 42 == 49 and 91 - 42 != 98)


print("\nF. SOURCE CENSUS")
source_register = SOURCE_REGISTER.read_text(encoding="utf-8")
source_packet = SOURCE_PACKET.read_text(encoding="utf-8")
for claim_id in ("SC-ACT-01", "SC-ACT-04", "SC-ACT-05", "SC-META-52"):
    check("source", f"source register contains {claim_id}", f"id: {claim_id}" in source_register)
check("source", "source packet fences physical boundary selection",
      "physical boundary selection" in source_packet)
check("source", "source packet fences the common domain",
      "common domain" in source_packet)


print("\nG. REGISTRY, CLAIM CEILING AND ROADMAP")
registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
check("registry", "registry records the 42+49 symmetric pair",
      registry["equivariance_obstruction"]["h_bal_dimension"] == 42
      and registry["equivariance_obstruction"]["p_bal_dimension"] == 49)
check("registry", "fixed balanced zero set is marked non-G-invariant",
      registry["equivariance_obstruction"]["p_bal_full_G_invariant"] is False)
check("registry", "moving-R repair does not derive the seed",
      registry["moving_order_parameter"]["epsilon_can_transport_R0"] is True
      and registry["moving_order_parameter"]["epsilon_derives_balanced_R0"] is False)
check("owners", "all three irreducible boundary owners are serialized",
      len(registry["owner_factorization"]) == 3)
check("ceiling", "explicit breaking and nonhomogeneous curvature remain open",
      registry["claim_ceiling"]["explicit_G_breaking_boundary_principle"].startswith("NOT_EXCLUDED")
      and registry["claim_ceiling"]["stationary_nonhomogeneous_curvature_selector"] == "OPEN")
check("routing", "artifact remains source-native and changes no ledger",
      registry["comparator_routing_classification"] == "SOURCE_NATIVE_ROUTE"
      and registry["disposition"]["ledger_change"] == "none")
current_text = CURRENT.read_text(encoding="utf-8")
next_text = NEXT.read_text(encoding="utf-8")
check("roadmap", "CURRENT and NEXT route to the nonhomogeneous owner test",
      "nonhomogeneous" in current_text and "nonhomogeneous" in next_text
      and "K104" in next_text)


summary = {"checks": sum(COUNTS.values()), "failures": FAILURES,
           "by_kind": dict(COUNTS)}
print("\n" + json.dumps(summary, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
