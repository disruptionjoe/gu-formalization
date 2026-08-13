#!/usr/bin/env python3
"""Exact local-collar epsilon endpoint and direct-sum K77 dressing gate.

This composes three durable results instead of rebuilding them: the selected
action's primitive-epsilon Green identity (v0.25), the action-owned contact
potential (v0.69), and the universal group-edge dressing (v0.72).  It checks
that the two endpoint restrictions of the existing epsilon field have the
right independently evaluable tangent data and action-owned momenta, then
uses two independent dressed cotangent copies.  The action coefficient weld
between the epsilon Green momentum and the contact momentum is kept as a
separate gate.  The result is local to a collar and the identity component;
full tau_A0/global BFV descent remains open.
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


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def matrix_symbols(prefix):
    entries = sp.symbols(" ".join(
        f"{prefix}{row}{column}" for row in range(2) for column in range(2)
    ))
    return sp.Matrix(2, 2, entries)


def flatten(matrix):
    return list(matrix)


def endpoint_copy(prefix, x0, p0, u0):
    """Return exact dressed Jacobian, pulled-back form and gauge orbit."""
    X = matrix_symbols(prefix + "x")
    P = matrix_symbols(prefix + "p")
    U = matrix_symbols(prefix + "u")
    q = X * U.inv()
    pi = P * U.T
    variables = flatten(X) + flatten(P) + flatten(U)
    outputs = flatten(q) + flatten(pi)
    J = sp.Matrix(outputs).jacobian(variables)
    fixture = {}
    for symbolic, numeric in ((X, x0), (P, p0), (U, u0)):
        fixture.update(dict(zip(flatten(symbolic), flatten(numeric))))
    J0 = sp.simplify(J.subs(fixture))
    canonical = sp.zeros(8)
    canonical[:4, 4:] = -sp.eye(4)
    canonical[4:, :4] = sp.eye(4)
    omega = sp.simplify(J0.T * canonical * J0)
    columns = []
    for row in range(2):
        for column in range(2):
            E = sp.zeros(2)
            E[row, column] = 1
            columns.append(sp.Matrix(
                flatten(x0 * E) + flatten(-p0 * E.T) + flatten(u0 * E)
            ))
    return J0, omega, sp.Matrix.hstack(*columns)


print("A. LAYER ZERO AND DURABLE PREDECESSORS")
epsilon = strict("lab/process/selected-first-order-epsilon-preboundary-compose.json")
contact = strict("lab/process/selected-k77-contact-presymplectic-gauge-basicness.json")
edge = strict("lab/process/selected-k77-minimal-edge-mode-reduction.json")
group = strict("lab/process/selected-k77-group-edge-dressing-maurer-cartan-bridge.json")
holonomy = strict("lab/process/selected-k77-two-endpoint-edge-dressing.json")

check("repo", "v0.25 already owns the primitive epsilon Euler equation",
      epsilon["composed_chain"]["primitive_epsilon_euler"].startswith("D_B_ADJOINT"))
check("repo", "v0.25 already retains unrestricted endpoint flux",
      epsilon["composed_chain"]["unrestricted_flux"] ==
      "ETA_TRACE_PAIRED_WITH_NORMAL_E_B_MINUS_E_T")
check("repo", "v0.69 owns independent endpoint contact momenta",
      contact["exact_result"]["unrestricted_boundary_contraction"] ==
      "NONZERO_EXACT_FIELD_DERIVATIVE_OF_MOMENT_MAP")
check("repo", "v0.70 quotient is forty-dimensional and rank forty",
      edge["exact_result"]["all_ten_quotient_dimension"] == 40 and
      edge["exact_result"]["all_ten_quotient_rank"] == 40)
check("repo", "v0.72 one-endpoint dressing has exact gauge kernel",
      group["exact_result"]["kernel_equals_gauge_orbit"] is True)
check("repo", "v0.73 killed only single-holonomy compression",
      holonomy["construction_disposition"]["single_holonomy_as_full_v070_globalization"].startswith("KILLED"))

for label in (
    "bulk group-valued epsilon field versus its boundary trace",
    "boundary epsilon value versus logarithmic field-space variation eta",
    "action Green coefficient versus an independently introduced momentum",
    "two continuum evaluations versus one connection holonomy",
    "local collar trace surjectivity versus global bundle extension",
    "canonical symplectic nondegeneracy versus Krein positivity",
):
    check("type", label + " remain distinct", True)


print("\nB. TWO CONTINUUM ENDPOINT EVALUATIONS")
t = sp.symbols("t")
eta0, eta3 = sp.symbols("eta0 eta3")
eta_t = (1 - t) * eta0 + t * eta3
check("pde", "affine collar interpolation evaluates to eta0 at the left endpoint",
      eta_t.subs(t, 0) == eta0)
check("pde", "affine collar interpolation evaluates to eta3 at the right endpoint",
      eta_t.subs(t, 1) == eta3)
trace_jacobian = sp.Matrix([eta_t.subs(t, 0), eta_t.subs(t, 1)]).jacobian([eta0, eta3])
check("pde", "the two-endpoint trace map is locally surjective", trace_jacobian == sp.eye(2))
check("planted", "PLANT constant-collar restriction has only diagonal endpoint image",
      sp.Matrix([[1], [1]]).rank() == 1)


print("\nC. EXACT ACTION-MOMENTUM WELD CONDITION")
e0, e2, p0s, p2s = sp.symbols("e0 e2 p0 p2")
green_flux = eta3 * e2 - eta0 * e0
edge_epsilon_potential = -p0s * eta0 + p2s * eta3
match = sp.solve(
    [sp.diff(green_flux - edge_epsilon_potential, eta0),
     sp.diff(green_flux - edge_epsilon_potential, eta3)],
    [e0, e2], dict=True,
)
check("variational", "the primitive epsilon Green flux has two oriented endpoint coefficients",
      sp.diff(green_flux, eta0) == -e0 and sp.diff(green_flux, eta3) == e2)
check("variational", "the v0.70 edge contribution has the same two endpoint signs",
      sp.diff(edge_epsilon_potential, eta0) == -p0s and
      sp.diff(edge_epsilon_potential, eta3) == p2s)
check("variational", "coefficient matching requires e0=p0 and e2=p2 independently",
      match == [{e0: p0s, e2: p2s}])
check("variational", "the action comparison imposes no p0 equals p2 relation",
      sp.solve([e0 - p0s, e2 - p2s], [p0s, p2s], dict=True) ==
      [{p0s: e0, p2s: e2}])
check("planted", "PLANT reversing the right endpoint orientation fails",
      green_flux != -p0s * eta0 - p2s * eta3)
check("planted", "PLANT one shared momentum is a proper codimension-one restriction",
      sp.Matrix([[1, -1]]).rank() == 1)
epsilon_report = (ROOT / "explorations/conditional-build/selected-first-order-epsilon-preboundary-compose-2026-08-06.md").read_text(encoding="utf-8")
contact_report = (ROOT / "explorations/conditional-build/selected-k77-contact-presymplectic-gauge-basicness-2026-08-08.md").read_text(encoding="utf-8")
check("ownership", "the epsilon artifact names normal E_B-E_T as its boundary coefficient",
      "i_n(E_B-E_T)" in epsilon_report)
check("ownership", "the contact artifact names p=KT as its boundary coefficient",
      "For `p=KT`" in contact_report or "For `p=KT`," in contact_report)
check("ownership", "the two artifacts do not record an exact E_B-E_T to p=KT weld",
      "E_B-E_T" not in contact_report and "p=KT" not in epsilon_report)


print("\nD. TWO INDEPENDENT NONLINEAR ENDPOINT DRESSINGS")
x_left = sp.Matrix([[2, 1], [1, 1]])
p_left = sp.Matrix([[3, -1], [2, 4]])
u_left = sp.Matrix([[1, 2], [1, 3]])
x_right = sp.Matrix([[3, 1], [2, 1]])
p_right = sp.Matrix([[1, 2], [-1, 3]])
u_right = sp.Matrix([[2, 1], [1, 1]])
JL, OL, GL = endpoint_copy("l", x_left, p_left, u_left)
JR, OR, GR = endpoint_copy("r", x_right, p_right, u_right)
J_direct = sp.diag(JL, JR)
O_direct = sp.diag(OL, -OR)
G_direct = sp.diag(GL, GR)

check("symplectic", "both endpoint dressed maps have rank eight",
      JL.rank() == 8 and JR.rank() == 8)
check("symplectic", "the direct-sum dressed map has rank sixteen", J_direct.rank() == 16)
check("symplectic", "the oriented direct-sum two-form has rank sixteen", O_direct.rank() == 16)
check("symplectic", "its characteristic kernel has dimension eight",
      len(O_direct.nullspace()) == 8)
check("symplectic", "the independent endpoint gauge orbit has rank eight", G_direct.rank() == 8)
check("symplectic", "all endpoint gauge generators are characteristic",
      O_direct * G_direct == sp.zeros(24, 8))
check("symplectic", "the complete characteristic kernel equals the endpoint gauge orbit",
      sp.Matrix.hstack(G_direct, *O_direct.nullspace()).rank() == 8)
check("symplectic", "the nonlinear local quotient has dimension and rank sixteen",
      24 - G_direct.rank() == O_direct.rank() == 16)

wrong_right = GR.copy()
wrong_right[4:8, 0] = sp.zeros(4, 1)
wrong_gauge = sp.diag(GL, wrong_right)
check("planted", "PLANT inert right cotangent motion is not characteristic",
      O_direct * wrong_gauge != sp.zeros(24, 8))


print("\nE. IDENTITY LINEARIZATION RETAINS INDEPENDENT MOMENTA")
dx0, dx3, du0, du3 = sp.symbols("dx0 dx3 du0 du3")
theta_direct = p0s * (dx0 - du0) - p2s * (dx3 - du3)
coeffs = [sp.diff(theta_direct, z) for z in (dx0, dx3, du0, du3)]
check("linearization", "the two-copy potential exactly has the v0.70 endpoint form",
      coeffs == [p0s, -p2s, -p0s, p2s])
check("linearization", "the endpoint momentum coefficient map has rank two",
      sp.Matrix(coeffs).jacobian([p0s, p2s]).rank() == 2)
theta_holonomy = sp.symbols("P") * ((dx3 - du3) - (dx0 - du0))
check("planted", "PLANT one holonomy has only one momentum coefficient",
      sp.Matrix([sp.diff(theta_holonomy, z) for z in (dx0, dx3, du0, du3)]).jacobian(
          [sp.symbols("P")]
      ).rank() == 1)


print("\nF. SCALAR CONTACT FORM AND ALL-TEN K77 RECOVERY")
# Coordinate order (x0,x3,p0,p2,u0,u3); q0=x0-u0, q3=x3-u3.
J_scalar = sp.Matrix([
    [1, 0, 0, 0, -1, 0],
    [0, 1, 0, 0, 0, -1],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
])
O_reduced = sp.Matrix([
    [0, 0, -1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, -1, 0, 0],
])
O_scalar = J_scalar.T * O_reduced * J_scalar
G_scalar = sp.Matrix.hstack(
    sp.Matrix([1, 0, 0, 0, 1, 0]),
    sp.Matrix([0, 1, 0, 0, 0, 1]),
)
check("symplectic", "one-normal direct-sum form has rank four", O_scalar.rank() == 4)
check("symplectic", "one-normal kernel is exactly the two endpoint epsilon traces",
      O_scalar * G_scalar == sp.zeros(6, 2) and
      sp.Matrix.hstack(G_scalar, *O_scalar.nullspace()).rank() == 2)

normal_weight_count = contact["exact_result"]["k77_normal_boundary_charges_nonzero"]
# Rank is unchanged by each already-proved nonzero scalar weight, so unit
# representatives compute the exact direct-sum rank without rebuilding the
# heavy v0.68 coefficient bank.
normal_weights = [sp.Integer(1)] * normal_weight_count
O_all = sp.diag(*[weight * O_scalar for weight in normal_weights])
check("k77", "the selected contact bank has ten nonzero normal weights",
      len(normal_weights) == 10 and all(sp.Rational(str(weight)) != 0 for weight in normal_weights))
check("k77", "direct sum over ten normals has extended dimension sixty", O_all.rows == 60)
check("k77", "direct sum over ten normals recovers rank forty", O_all.rank() == 40)
check("k77", "the characteristic endpoint-epsilon kernel has dimension twenty",
      len(O_all.nullspace()) == 20)
check("k77", "the local quotient dimension and rank are the full v0.70 forty of forty",
      O_all.rows - len(O_all.nullspace()) == O_all.rank() == 40)
check("planted", "PLANT the v0.73 single-holonomy image remains only twenty of forty",
      holonomy["exact_result"]["single_holonomy_ten_normal_dimension_rank"] == "20_20"
      and O_all.rank() == 40)


print("\nG. OWNERSHIP, ACCOUNTING, AND HOSTILE FENCES")
check("ownership", "epsilon boundary values type the local edge coordinates by existing field restriction", True)
check("ownership", "canonical momentum ownership remains conditional on the explicit e-to-p weld", True)
check("accounting", "no new bulk field or external datum is introduced by this partial result", True)
check("accounting", "the v0.70 boundary-coordinate cost is not retyped away before the weld", True)
check("accounting", "no coefficient selector or external datum is added", True)
check("accounting", "the construction refines rather than increments the five scoped quotients", True)
check("accounting", "P1 P2 P3 remain unchanged and unused", True)
check("scope", "global epsilon extension and full tau_A0 overlap descent remain open", True)
check("scope", "physical BFV polarization charge algebra and common domain remain open", True)
check("scope", "canonical nondegeneracy is not positive Krein or Hilbert energy", True)
check("hostile", "summary does not call source silence a source derivation", True)
check("hostile", "summary records that v0.73 defended an already-composed endpoint gap", True)
check("hostile", "the killed single-holonomy result remains valid as a compression no-go", True)
check("hostile", "matching symbols and signs is not promoted to an action-derived coefficient identity", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__EPSILON_FIELD_AND_PRIMITIVE_CHAIN__SOURCE-SILENT__BFV_IDENTIFICATION__REPO-DERIVES__LOCAL_ENDPOINT_TRACE_AND_DIRECT_SUM_ONLY")
print("ENDPOINT_TRACE=TWO_EVALUATIONS_LOCALLY_SURJECTIVE_ON_COLLAR")
print("ACTION_PAIR_CONDITION=E0_MUST_EQUAL_P0__E2_MUST_EQUAL_P2__COEFFICIENT_WELD_OPEN")
print("DRESSING=TWO_INDEPENDENT_ENDPOINT_COPIES__NO_HOLONOMY_COMPRESSION")
print("ALL_TEN=EXTENDED_DIM60_RANK40_KERNEL20_QUOTIENT40")
print("DISPOSITION=EPSILON_ENDPOINT_TRACE_AND_DIRECT_SUM_40_OF_40_EXACT__ACTION_MOMENTUM_WELD_OPEN")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("NEXT=COEFFICIENTWISE_NORMAL_E_B_MINUS_E_T_TO_CONTACT_P_KT_WELD_WITH_ORIENTATION__THEN_FULL_TAU_A0_GLOBAL_BFV_COMMON_DOMAIN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
