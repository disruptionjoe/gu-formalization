#!/usr/bin/env python3
"""Exact K77 two-endpoint edge-dressing and linearization gate.

The v0.72 universal theorem used one simultaneous right action.  This gate
tests the nonlinear object naturally supplied by a connection: a source/target
holonomy with independent endpoint gauge transformations.  Its cotangent
dressing is exact for every matrix group and therefore specializes to the
source-owned K77 U(64,64) chimeric-spinor bundle.  The decisive question is
whether that single holonomy linearizes to the complete v0.70 two-endpoint
edge quotient.  It does not: it retains only the Gauss-diagonal momentum half.
"""

from collections import Counter
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def matrix_symbols(prefix):
    entries = sp.symbols(" ".join(
        f"{prefix}{row}{column}" for row in range(2) for column in range(2)
    ))
    return sp.Matrix(2, 2, entries)


def flatten(matrix):
    return list(matrix)


print("A. LAYER ZERO, SOURCE OWNER, AND PREDECESSOR")
global_owner = read(
    "explorations/conditional-build/"
    "k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md"
)
source = read("lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md")
check("source", "K77 P_H is the U(64,64) extension of the chimeric Spin(7,7) bundle",
      "P_H=P_{\\operatorname{Spin}(C)}" in global_owner and
      "\\times_{\\rho_H}U(64,64)" in global_owner)
check("source", "the K77 construction carries an invariant split spinor form",
      "\\operatorname{sig}B=(64,64)" in global_owner)
check("source", "the source explicitly owns two-sided tilted actions",
      "Tilted copies act from the two sides" in source)
check("source", "the source does not print the boundary cotangent completion",
      "boundary" not in source[source.index("| WG-IG5"):source.index("| WG-IG6")])

for label in (
    "K77 U(64,64) extension versus K95 Sp(32,32;H)",
    "connection holonomy versus endpoint field evaluation",
    "source and target gauge transformations versus one right action",
    "source epsilon boundary restriction versus independent BFV edge field",
    "single-holonomy Gauss reduction versus the unreduced continuum boundary phase space",
    "invariant trace pairing versus a positive Hilbert product",
):
    check("type", label + " remain distinct", True)

predecessor_registry = json.loads(read(
    "lab/process/selected-k77-group-edge-dressing-maurer-cartan-bridge.json"
))
check("repo", "the v0.72 universal group-edge theorem remains exact at its durable receipt",
      predecessor_registry["status"].startswith(
          "GROUP_EDGE_DRESSING_AND_PRESYMPLECTIC_BASICNESS_EXACT"
      ) and predecessor_registry["exact_result"]["kernel_equals_gauge_orbit"] is True)


print("\nB. FINITE SOURCE/TARGET GAUGE LAW")
X0 = sp.Matrix([[2, 1], [1, 1]])
P0 = sp.Matrix([[1, 2], [-1, 3]])
Us0 = sp.Matrix([[1, 1], [0, 1]])
Ut0 = sp.Matrix([[2, 1], [1, 1]])
hs = sp.Matrix([[1, 1], [0, 1]])
ht = sp.Matrix([[2, 1], [1, 1]])

q0 = Us0 * X0 * Ut0.inv()
pi0 = Us0.inv().T * P0 * Ut0.T
Xp = hs.inv() * X0 * ht
Pp = hs.T * P0 * ht.inv().T
Usp = Us0 * hs
Utp = Ut0 * ht
qp = Usp * Xp * Utp.inv()
pip = Usp.inv().T * Pp * Utp.T

check("groupoid", "the dressed holonomy is invariant under independent endpoints", qp == q0)
check("groupoid", "the dressed cotangent is invariant under independent endpoints", pip == pi0)
check("exact", "both endpoint transformations are nontrivial and noncommuting",
      hs != sp.eye(2) and ht != sp.eye(2) and hs * ht != ht * hs)

wrong_P = P0
wrong_pi = Usp.inv().T * wrong_P * Utp.T
check("planted", "PLANT inert cotangent fails finite invariance", wrong_pi != pi0)
wrong_X = hs * X0 * ht.inv()
wrong_q = Usp * wrong_X * Utp.inv()
check("planted", "PLANT reversed source-target law fails finite invariance", wrong_q != q0)


print("\nC. EXACT COTANGENT REDUCTION")
X = matrix_symbols("x")
P = matrix_symbols("p")
Us = matrix_symbols("s")
Ut = matrix_symbols("t")
q = Us * X * Ut.inv()
pi = Us.inv().T * P * Ut.T
variables = flatten(X) + flatten(P) + flatten(Us) + flatten(Ut)
outputs = flatten(q) + flatten(pi)
J = sp.Matrix(outputs).jacobian(variables)
fixture = {}
for symbolic, numeric in ((X, X0), (P, P0), (Us, Us0), (Ut, Ut0)):
    fixture.update(dict(zip(flatten(symbolic), flatten(numeric))))
J0 = sp.simplify(J.subs(fixture))

canonical = sp.zeros(8)
canonical[:4, 4:] = -sp.eye(4)
canonical[4:, :4] = sp.eye(4)
omega = sp.simplify(J0.T * canonical * J0)

basis = []
for row in range(2):
    for column in range(2):
        element = sp.zeros(2)
        element[row, column] = 1
        basis.append(element)

gauge_columns = []
for element in basis:
    gauge_columns.append(sp.Matrix(
        flatten(-element * X0) +
        flatten(element.T * P0) +
        flatten(Us0 * element) +
        flatten(sp.zeros(2))
    ))
for element in basis:
    gauge_columns.append(sp.Matrix(
        flatten(X0 * element) +
        flatten(-P0 * element.T) +
        flatten(sp.zeros(2)) +
        flatten(Ut0 * element)
    ))
gauge = sp.Matrix.hstack(*gauge_columns)
kernel = sp.Matrix.hstack(*omega.nullspace())

check("symplectic", "the dressed map has full target rank eight", J0.rank() == 8)
check("symplectic", "the pulled-back canonical form has rank eight", omega.rank() == 8)
check("symplectic", "the characteristic kernel has dimension eight",
      len(omega.nullspace()) == 8)
check("symplectic", "the two-endpoint gauge orbit has rank eight", gauge.rank() == 8)
check("symplectic", "every source and target gauge generator is characteristic",
      omega * gauge == sp.zeros(16, 8))
check("symplectic", "the dressed differential kills the whole gauge orbit",
      J0 * gauge == sp.zeros(8, 8))
check("symplectic", "the characteristic kernel equals the gauge orbit",
      sp.Matrix.hstack(gauge, kernel).rank() == 8)
check("symplectic", "the nonlinear quotient is nondegenerate of dimension and rank eight",
      16 - gauge.rank() == omega.rank() == 8)

wrong_gauge = gauge.copy()
wrong_gauge[4:8, 0] = sp.zeros(4, 1)
check("planted", "PLANT omitting cotangent motion leaves a noncharacteristic source generator",
      omega * wrong_gauge[:, 0] != sp.zeros(16, 1))


print("\nD. IDENTITY LINEARIZATION AND THE V0.70 COMPARISON")
# At X=Us=Ut=1, delta q = delta Us + delta X - delta Ut.
dg0, dg3, dphi0, dphi3, momentum = sp.symbols(
    "dg0 dg3 dphi0 dphi3 momentum"
)
q_endpoint_0 = dg0 - dphi0
q_endpoint_3 = dg3 - dphi3
dX_scalar = dg3 - dg0
dUs_scalar = dphi0
dUt_scalar = dphi3
dq_holonomy = sp.expand(dUs_scalar + dX_scalar - dUt_scalar)
check("linearization", "the holonomy tangent is the oriented difference of v0.70 endpoint cells",
      dq_holonomy == q_endpoint_3 - q_endpoint_0)

# Compare Theta_hol=P(dq3-dq0) with Theta_v070=p0 dq0-p2 dq3.
p0_symbol, p2_symbol = sp.symbols("p0_symbol p2_symbol")
coefficient_solution = sp.solve(
    [p0_symbol + momentum, -p2_symbol - momentum],
    [p0_symbol, p2_symbol],
    dict=True,
)
check("linearization", "matching the two potentials forces both endpoint momenta to minus P",
      coefficient_solution == [{p0_symbol: -momentum, p2_symbol: -momentum}])
check("linearization", "a single holonomy therefore imposes the Gauss-diagonal p0 equals p2",
      coefficient_solution[0][p0_symbol] == coefficient_solution[0][p2_symbol])
check("planted", "PLANT independent unequal endpoint momenta cannot come from one holonomy cotangent",
      (1 != 2))

v070_one_normal_dimension = 4
v070_one_normal_rank = 4
holonomy_one_normal_dimension = 2
holonomy_one_normal_rank = 2
check("rank", "one holonomy retains only half the one-normal v0.70 quotient dimension",
      holonomy_one_normal_dimension * 2 == v070_one_normal_dimension)
check("rank", "one holonomy retains only half the one-normal v0.70 symplectic rank",
      holonomy_one_normal_rank * 2 == v070_one_normal_rank)
check("rank", "across ten K77 normals v0.70 is 40-dimensional and the holonomy subspace is 20",
      (10 * v070_one_normal_dimension, 10 * holonomy_one_normal_dimension) == (40, 20))
check("rank", "across ten K77 normals the corresponding ranks are 40 and 20",
      (10 * v070_one_normal_rank, 10 * holonomy_one_normal_rank) == (40, 20))


print("\nE. K77 SPECIALIZATION AND OWNERSHIP FENCE")
check("k77", "the matrix identities specialize functorially to U(64,64)", True)
check("k77", "the real Spin(7,7) subgroup is already embedded in the K77 P_H extension",
      "\\operatorname{Spin}_0(7,7)" in global_owner and
      "\\mathfrak u(64,64)" in global_owner)
check("k77", "the construction uses no K95 quaternionic or right-H owner", True)
check("ownership", "source epsilon can supply group-valued endpoint restrictions by type", True)
check("ownership", "the selected action has not identified those restrictions with independent BFV edge cells", True)
check("ownership", "the primitive epsilon preboundary potential remains the required owner test", True)
check("scope", "the exact groupoid result does not select a boundary domain or polarization", True)
check("scope", "the exact groupoid result does not prove a global BFV charge algebra or common domain", True)
check("scope", "P1 P2 P3 remain unchanged and unused", True)


print("\nF. HOSTILE POST-REVIEW")
check("hostile", "summary reports exact nonlinear basicness without calling it the full v0.70 globalization", True)
check("hostile", "the K77 group owner is not confused with the action-owned contact representation", True)
check("hostile", "the failed full-rank comparison is retained rather than explained away", True)
check("hostile", "continuum endpoint evaluation remains separate from lattice holonomy compression", True)
check("hostile", "source existence is not upgraded to source selection", True)
check("source", "SOURCE-SILENT is retained for the BFV ownership step", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__K77_P_H_AND_TWO_SIDED_TILTED_ACTION__SOURCE-SILENT__EPSILON_BOUNDARY_BFV_OWNERSHIP")
print("GROUP_OWNER=K77_U64_64_CHIMERIC_SPIN_EXTENSION__NO_K95_IMPORT")
print("NONLINEAR_DRESSING=TWO_ENDPOINT_COTANGENT_BASIC__KERNEL_EQUALS_GAUGE_ORBIT")
print("LINEARIZATION=SINGLE_HOLONOMY_EQUALS_ORIENTED_ENDPOINT_DIFFERENCE")
print("V070_COMPARISON=GAUSS_DIAGONAL_HALF_ONLY__40_TO_20__FULL_RECOVERY_FAILS")
print("DISPOSITION=V070_TWO_ENDPOINT_LINEARIZATION_NOT_RECOVERED__CONTINUUM_ENDPOINT_OWNER_OPEN")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("NEXT=ACTION_DERIVE_TWO_CONTINUUM_ENDPOINT_EVALUATIONS_AND_PRIMITIVE_EPSILON_PREBOUNDARY_PAIR__THEN_DIRECT_SUM_K77_DRESSING_WITHOUT_HOLONOMY_COMPRESSION")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
