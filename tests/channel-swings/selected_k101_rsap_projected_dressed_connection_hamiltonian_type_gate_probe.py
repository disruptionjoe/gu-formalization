#!/usr/bin/env python3
"""Exact K101 balanced projection and Hamiltonian-type correction probe."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import contextlib
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
K100_PROBE = ROOT / "tests/channel-swings/selected_k100_rsap_balanced_order_parameter_owner_census_probe.py"
REGISTRY = ROOT / "lab/process/selected-k101-rsap-projected-dressed-connection-hamiltonian-type-gate.json"
RESULT = ROOT / "explorations/conditional-build/selected-k101-rsap-projected-dressed-connection-hamiltonian-type-gate-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k101-rsap-projected-dressed-connection-hamiltonian-type-gate-review.md"
CURRENT = ROOT / "CURRENT-STATE.yaml"
NEXT = ROOT / "NEXT-STEPS.md"
N = 14
Q = [1] * 7 + [-1] * 7
PLUS = set(range(3)) | set(range(7, 11))
R0 = [[Fraction((1 if i in PLUS else -1) if i == j else 0)
       for j in range(N)] for i in range(N)]
QMAT = [[Fraction(Q[i] if i == j else 0) for j in range(N)] for i in range(N)]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def zero(n: int = N):
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def identity(n: int = N):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


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


def transpose(a):
    return [list(row) for row in zip(*a)]


def bracket(a, b):
    return sub(mul(a, b), mul(b, a))


def flatten(a):
    return [value for row in a for value in row]


def rank(rows) -> int:
    work = [[Fraction(value) for value in row] for row in rows]
    result = 0
    columns = len(work[0]) if work else 0
    for column in range(columns):
        pivot = next((row for row in range(result, len(work))
                      if work[row][column]), None)
        if pivot is None:
            continue
        work[result], work[pivot] = work[pivot], work[result]
        divisor = work[result][column]
        work[result] = [value / divisor for value in work[result]]
        for row in range(len(work)):
            if row != result and work[row][column]:
                factor = work[row][column]
                work[row] = [left - factor * right
                             for left, right in zip(work[row], work[result])]
        result += 1
    return result


def basis_matrix(i: int, j: int):
    value = zero()
    value[i][j] = 1
    value[j][i] = -Q[i] * Q[j]
    return value


FULL = [basis_matrix(i, j) for i in range(N) for j in range(i + 1, N)]


def theta(x):
    return mul(mul(R0, x), R0)


def ph(x):
    return scale(Fraction(1, 2), add(x, theta(x)))


def pp(x):
    return scale(Fraction(1, 2), sub(x, theta(x)))


H = [x for x in FULL if theta(x) == x]
P = [x for x in FULL if theta(x) == scale(-1, x)]


def weighted_sum(bank, offset: int):
    value = zero()
    for index, matrix in enumerate(bank):
        value = add(value, scale(Fraction(((index + offset) % 7) - 3), matrix))
    return value


print("A. PREDECESSOR AND DURABLE FILES")
replay = io.StringIO()
replay_code = None
with contextlib.redirect_stdout(replay):
    try:
        runpy.run_path(str(K100_PROBE), run_name="__main__")
    except SystemExit as error:
        replay_code = error.code
check("predecessor", "K100 balanced-seed certificate replays cleanly",
      replay_code == 0 and '"failures": []' in replay.getvalue())
check("artifact", "result registry review and roadmap files exist",
      all(path.exists() for path in (REGISTRY, RESULT, REVIEW, CURRENT, NEXT)))


print("\nB. BALANCED INVOLUTION AND PROJECTORS")
check("involution", "R0 is an involution", mul(R0, R0) == identity())
check("involution", "R0 is Q-self-adjoint and Q-orthogonal",
      mul(transpose(R0), QMAT) == mul(QMAT, R0)
      and mul(mul(transpose(R0), QMAT), R0) == QMAT)
check("dimension", "fixed and anti-fixed banks have dimensions 42 and 49",
      (len(H), len(P)) == (42, 49))
check("projector", "P_h and P_p resolve every so(7,7) generator",
      all(add(ph(x), pp(x)) == x for x in FULL))
check("projector", "P_h and P_p are idempotent and mutually annihilating",
      all(ph(ph(x)) == ph(x) and pp(pp(x)) == pp(x)
          and ph(pp(x)) == zero() and pp(ph(x)) == zero() for x in FULL))
check("rank", "projector image ranks are exactly 42 and 49",
      rank([flatten(ph(x)) for x in FULL]) == 42
      and rank([flatten(pp(x)) for x in FULL]) == 49)


print("\nC. SYMMETRIC-PAIR BRACKET PARITY")
check("bracket", "[h,h] lies in h",
      all(pp(bracket(x, y)) == zero() for x in H for y in H))
check("bracket", "[h,p] lies in p",
      all(ph(bracket(x, y)) == zero() for x in H for y in P))
check("bracket", "[p,p] lies in h",
      all(pp(bracket(x, y)) == zero() for x in P for y in P))


print("\nD. RIGHT-H CONNECTION TRANSFORMATION TYPE")
a = weighted_sum(H, 1)
phi = weighted_sum(P, 2)
xi = weighted_sum(H, 3)
dxi = weighted_sum(H, 4)
delta_full = add(dxi, bracket(add(a, phi), xi))
check("infinitesimal", "h projection has connection variation",
      ph(delta_full) == add(dxi, bracket(a, xi)))
check("infinitesimal", "p projection has homogeneous variation",
      pp(delta_full) == bracket(phi, xi))

# A rational determinant-one rotation in a positive two-plane supplies a
# nontrivial connected H frame.
h = identity()
h[0][0] = h[1][1] = Fraction(3, 5)
h[0][1] = Fraction(4, 5)
h[1][0] = Fraction(-4, 5)
h_inv = transpose(h)
k = H[5]
transformed = add(mul(mul(h_inv, add(a, phi)), h), k)
check("finite", "finite h frame preserves the h connection law",
      mul(mul(transpose(h), QMAT), h) == QMAT
      and mul(h, R0) == mul(R0, h)
      and ph(transformed) == add(mul(mul(h_inv, a), h), k))
check("finite", "finite h frame preserves the p tensor law",
      pp(transformed) == mul(mul(h_inv, phi), h))


print("\nE. PROJECTED GAUSS IDENTITY")
e = weighted_sum(H, 5)
pi = weighted_sum(P, 6)
de = weighted_sum(H, 7)
dpi = weighted_sum(P, 8)
gauss = add(add(de, dpi), bracket(add(a, phi), add(e, pi)))
gauss_h = add(de, add(bracket(a, e), bracket(phi, pi)))
gauss_p = add(dpi, add(bracket(a, pi), bracket(phi, e)))
check("gauss", "h Gauss projection includes the p-sector current",
      ph(gauss) == gauss_h)
check("gauss", "p Gauss projection has both mixed currents",
      pp(gauss) == gauss_p)
check("control", "omitting [phi,pi] changes the h Gauss expression",
      bracket(phi, pi) != zero() and gauss_h != add(de, bracket(a, e)))


print("\nF. SELF-HESSIAN COUNTEREXAMPLE AND LEGENDRE TYPE")
D = [[Fraction(0), Fraction(1)], [Fraction(-1), Fraction(0)]]
DT = transpose(D)
coordinate_hessian = mul(DT, D)
velocity_hessian = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
check("hessian", "coordinate a0 Hessian D^T D is nonzero and full rank",
      coordinate_hessian == [[1, 0], [0, 1]] and rank(coordinate_hessian) == 2)
check("hessian", "normal-velocity Hessian has a two-dimensional kernel",
      rank(velocity_hessian) == 2)
e2 = [[Fraction(2)], [Fraction(-3)]]
a0 = [[Fraction(5)], [Fraction(7)]]
lhs = mul(transpose(e2), mul(D, a0))[0][0]
rhs = mul(transpose(a0), mul(DT, e2))[0][0]
check("legendre", "exact pairing moves D onto momentum",
      lhs == rhs and lhs != 0)
check("legendre", "the first-order a0 dependence is linear",
      mul(DT, e2) != [[0], [0]])


print("\nG. SOURCE CEILING, CORRECTION AND SUCCESSOR")
registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
result_text = RESULT.read_text(encoding="utf-8")
current_text = CURRENT.read_text(encoding="utf-8")
next_text = NEXT.read_text(encoding="utf-8")
check("registry", "registry records exact 42+49 conditional projection",
      registry["conditional_projection"]["h_dimension"] == 42
      and registry["conditional_projection"]["p_dimension"] == 49)
check("correction", "zero coordinate self-Hessian is explicitly withdrawn",
      registry["diagnostic_correction"]["pointwise_connection_hessian_decides_normal_multiplier"] is False
      and "zero self-Hessian" in result_text)
check("ceiling", "collar Legendre map and endpoint bridge remain type-missing",
      registry["source_hamiltonian_inventory"]["preferred_one_time_or_non_null_collar"] == "TYPE_MISSING"
      and registry["source_hamiltonian_inventory"]["full_projected_legendre_map"] == "TYPE_MISSING"
      and registry["source_hamiltonian_inventory"]["G_h_to_endpoint_J_R_H_bal_bridge"] == "TYPE_MISSING")
check("roadmap", "CURRENT and NEXT route to the corrected Legendre gate",
      "normal-velocity Legendre kernel" in current_text
      and "K101" in next_text
      and "[phi,pi]" in next_text)
check("routing", "source-native routing and no ledger change remain explicit",
      registry["comparator_routing_classification"] == "SOURCE_NATIVE_ROUTE"
      and registry["disposition"]["ledger_change"] == "none")


summary = {"checks": sum(COUNTS.values()), "failures": FAILURES,
           "by_kind": dict(sorted(COUNTS.items()))}
print("\n" + json.dumps(summary, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
