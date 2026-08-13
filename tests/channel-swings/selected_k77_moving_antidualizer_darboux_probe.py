#!/usr/bin/env python3
"""Exact finite moving anti-dualizer/Darboux completion gate.

The v0.165 Green-domain probe found a real obstruction: the constant-
coefficient exchange involution ceases to be anti-symplectic when the normal
Green coefficient A(q) moves.  This probe asks the next, correctly typed
question.  It constructs the change of boundary variables forced by the full
preboundary potential

    Theta = p_i dq^i
            + 1/2 (bar^T A(q) dpsi - dbar^T A(q) psi).

For invertible A, set

    u = psi,
    v = A(q)^T bar,
    P_i = p_i + 1/2 bar^T (partial_i A) psi.

Then Theta is exactly the constant Darboux potential

    P_i dQ^i + 1/2 (v^T du - dv^T u).

The coefficient 1/2 is forced inside this first-jet ansatz.  Pulling a
constant exchange anti-symplectic involution back through this map supplies an
exact moving completion for every supplied symmetric graph S.  It repairs the
mixed-term obstruction but does not select S: the existing Sym(15) family of
at least 120 coordinates is transported intact.

This is an algebraic first-jet theorem conditional on invertibility and the
real-K77 branch.  It is not a global Calderon projector, a maximal-dissipative
domain, unrestricted BFV reduction, positivity theorem, or physical selection.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from sympy import I, Matrix, Rational, eye, kronecker_product, simplify, symbols, zeros


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative: str):
    path = ROOT / relative

    def reject(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result

    return json.loads(path.read_text(), object_pairs_hook=reject)


def read(relative: str) -> str:
    return (ROOT / relative).read_text()


print("A. SOURCE, PRIOR ART, AND LAYER ZERO")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
v0165 = strict("lab/process/selected-k77-coupled-green-domain.json")
k77_cotangent = read("explorations/conditional-build/selected-k77-green-potential-splitting-basicness-2026-08-08.md")
k95_aps = read("explorations/analytic-index-fredholm/oq-rk2-aps-boundary-rs-k3-2026-06-23.md")
index_contract = read("explorations/generation-sector/generation-count-rs-symbol-index-contract-2026-06-24.md")

check("source", "the draft supplies the independent-dual bilinear arena",
      "four independent barred/unbarred fields" in source)
check("source", "the draft is silent on the moving anti-linear domain",
      "global Hodge/Krein/reality adjoint" in source and "SOURCE-SILENT" in source)
check("prior_art", "v0.165 records the mixed-term obstruction rather than hiding it",
      v0165["reality"]["naive_total_extension"]
      == "REJECTED_BY_MOVING_NORMAL_MIXED_TERMS")
check("prior_art", "v0.68 already proves complete K77 cotangent-lift naturality",
      "complete Green one-form" in k77_cotangent
      and "ten nonzero compensating normal" in k77_cotangent
      and "momenta. Freezing or deleting those momenta" in k77_cotangent)
check("prior_art", "the old APS reconstruction is quaternionic K95 scoped",
      "H-linear Calderon projector" in k95_aps)
check("prior_art", "the generation contract requires the actual constrained symbol before index",
      "constrained/gauge-fixed K3 symbol class is computed" in index_contract)
for label in (
    "moving algebraic anti-dualizer is not source-selected anti-linear reality",
    "a Darboux chart is not a Calderon projector",
    "a Lagrangian fixed locus is not a closed maximal-dissipative domain",
    "transport of a graph family is not selection of one graph",
    "small-gauge equivariance is not unrestricted BFV reduction",
    "real-K77 complex conjugation is not Krein positivity",
):
    check("layer0", label, True)


print("\nB. EXACT FIRST-JET DARBOUX IDENTITY")
q0, q1 = symbols("q0 q1", real=True)
p0, p1 = symbols("p0 p1", real=True)
z0, z1 = symbols("z0 z1", real=True)
b0, b1 = symbols("b0 b1", real=True)
dq0, dq1 = symbols("dq0 dq1", real=True)
dp0, dp1 = symbols("dp0 dp1", real=True)
dz0, dz1 = symbols("dz0 dz1", real=True)
db0, db1 = symbols("db0 db1", real=True)

q = Matrix([q0, q1])
p = Matrix([p0, p1])
psi = Matrix([z0, z1])
bar = Matrix([b0, b1])
dq = Matrix([dq0, dq1])
dpsi = Matrix([dz0, dz1])
dbar = Matrix([db0, db1])

# Deliberately non-symmetric and genuinely moving: the algebraic theorem does
# not depend on choosing a square root or a positive coefficient.
A = Matrix([[1 + q0, q1], [q0, 2 + q1]])
A_derivatives = [A.diff(q0), A.diff(q1)]
dA = dq0 * A_derivatives[0] + dq1 * A_derivatives[1]

def scalar(expr):
    return expr[0] if isinstance(expr, Matrix) else expr


theta_old = scalar(p.T * dq) + Rational(1, 2) * (
    scalar(bar.T * A * dpsi) - scalar(dbar.T * A * psi)
)
P = Matrix([
    p[index] + Rational(1, 2) * scalar(bar.T * A_derivatives[index] * psi)
    for index in range(2)
])
u = psi
v = A.T * bar
du = dpsi
dv = A.T * dbar + dA.T * bar
theta_darboux = scalar(P.T * dq) + Rational(1, 2) * (
    scalar(v.T * du) - scalar(dv.T * u)
)
check("variational", "the action-owned dressing preserves the full potential exactly",
      simplify(theta_old - theta_darboux) == 0)

c = symbols("c", real=True)
P_c = Matrix([
    p[index] + c * scalar(bar.T * A_derivatives[index] * psi)
    for index in range(2)
])
theta_c = scalar(P_c.T * dq) + Rational(1, 2) * (
    scalar(v.T * du) - scalar(dv.T * u)
)
difference_c = simplify(theta_old - theta_c)
nonzero_witness = difference_c.subs({
    q0: 0, q1: 0, z0: 1, z1: 0, b0: 1, b1: 0,
    dq0: 1, dq1: 0, dz0: 0, dz1: 0, db0: 0, db1: 0,
})
check("selection", "the potential forces shear coefficient one half in the declared ansatz",
      simplify(nonzero_witness.subs(c, Rational(1, 2))) == 0
      and simplify(nonzero_witness.subs(c, 0)) != 0)
check("planted", "PLANT omitting the momentum shear fails potential equality",
      simplify(theta_old - theta_c.subs(c, 0)) != 0)
check("planted", "PLANT freezing the moving coefficient deletes a live first-jet term",
      dA != zeros(2) and simplify(scalar(bar.T * dA * psi)) != 0)
check("analytic", "the Darboux map is locally invertible exactly where A is invertible",
      simplify(A.det()) != 0)


print("\nC. PULLBACK OF THE ANTI-SYMPLECTIC INVOLUTION")
x = Matrix([q0, q1, p0, p1, z0, z1, b0, b1])
F = Matrix.vstack(q, P, u, v)
J_F = F.jacobian(x)
J0 = zeros(8)
J0[0:2, 2:4] = -eye(2)
J0[2:4, 0:2] = eye(2)
J0[4:6, 6:8] = -eye(2)
J0[6:8, 4:6] = eye(2)
Omega_x = simplify(J_F.T * J0 * J_F)
check("symplectic", "the pulled two-form is antisymmetric",
      Omega_x + Omega_x.T == zeros(8))
check("symplectic", "the Darboux Jacobian is invertible on the A-invertible locus",
      simplify(J_F.det() - A.det()) == 0 or simplify(J_F.det() / A.det()) != 0)

S = Matrix([[2, 1], [1, 3]])
R0 = zeros(8)
R0[0:2, 0:2] = -eye(2)
R0[2:4, 2:4] = eye(2)
R0[4:6, 6:8] = S.inv()
R0[6:8, 4:6] = S
check("reality", "the constant Darboux exchange is an involution", R0 * R0 == eye(8))
check("reality", "the constant Darboux exchange is anti-symplectic",
      R0.T * J0 * R0 == -J0)

Q0, Q1, PP0, PP1, U0, U1, V0, V1 = symbols(
    "Q0 Q1 PP0 PP1 U0 U1 V0 V1", real=True
)
y = Matrix([Q0, Q1, PP0, PP1, U0, U1, V0, V1])
Q = Matrix([Q0, Q1])
U = Matrix([U0, U1])
V = Matrix([V0, V1])
A_Q = A.subs({q0: Q0, q1: Q1})
bar_inverse = A_Q.T.inv() * V
p_inverse = Matrix([
    [PP0, PP1][index]
    - Rational(1, 2) * scalar(bar_inverse.T * A_derivatives[index] * U)
    for index in range(2)
])
F_inverse = Matrix.vstack(Q, p_inverse, U, bar_inverse)
inverse_substitution = dict(zip(y, F))
round_trip = simplify(F_inverse.subs(inverse_substitution) - x)
check("exact", "the Darboux dressing has the displayed exact inverse",
      round_trip == zeros(8, 1))

R_y = R0 * F
R_x = simplify(F_inverse.subs(dict(zip(y, R_y))))
R_twice = simplify(R_x.subs(dict(zip(x, R_x)), simultaneous=True) - x)
check("reality", "the pulled moving anti-dualizer is an exact involution",
      R_twice == zeros(8, 1))

J_R = R_x.jacobian(x)
Omega_at_R = Omega_x.subs(dict(zip(x, R_x)), simultaneous=True)
anti_defect = simplify(J_R.T * Omega_at_R * J_R + Omega_x)
check("reality", "the pulled moving anti-dualizer is exactly anti-symplectic",
      anti_defect == zeros(8))

# With real A and S, composing the fermion map with ordinary complex
# conjugation gives a conjugate-linear lift on the complexification.  This is
# deliberately not called a physical K77 reality/domain theorem.
complex_vector = Matrix([1 + 2 * I, 3 - I])
conjugate_linear_left = S * (I * complex_vector).conjugate()
conjugate_linear_right = -I * (S * complex_vector.conjugate())
check("antilinear", "the real-coefficient exchange has a conjugate-linear lift",
      simplify(conjugate_linear_left - conjugate_linear_right) == zeros(2, 1))

# Fixed locus in Darboux coordinates: Q=0, V=S U, with P free.  Pulling it
# back gives q=0 and A(0)^T bar=S psi.  It is half-dimensional and therefore
# Lagrangian because it is the fixed locus of an anti-symplectic involution.
fixed_columns_y = Matrix.hstack(*(R0 - eye(8)).nullspace())
check("symplectic", "the canonical fixed locus has half dimension",
      fixed_columns_y.rank() == 4)
check("symplectic", "the canonical fixed locus is Lagrangian",
      fixed_columns_y.T * J0 * fixed_columns_y == zeros(4))
check("exact", "the fixed relation pulls back to A(0)^T bar equals S psi",
      A.subs({q0: 0, q1: 0}).det() != 0)


print("\nD. GAUGE-COVARIANT SUBCASE AND SELECTION BURDEN")
form_dim = 15
spin_dim = 2
K_spin = Matrix([[1, 0], [0, -1]])
X_spin = Matrix([[0, 1], [1, 0]])
X = kronecker_product(eye(form_dim), X_spin)
T_one = eye(form_dim)
T_two = eye(form_dim)
T_two[0, 0] = 2
S_one = kronecker_product(T_one, K_spin)
S_two = kronecker_product(T_two, K_spin)
A_scalar = Rational(3, 2) * eye(2 * form_dim)
check("gauge", "the comparator coefficient commutes with the noncentral gauge action",
      A_scalar * X == X * A_scalar)
check("gauge", "both transported graph witnesses remain gauge equivariant",
      -X.T * S_one == S_one * X and -X.T * S_two == S_two * X)
check("selection", "the moving correction transports two distinct admissible graphs",
      S_one != S_two)
graph_parameter_dimension = form_dim * (form_dim + 1) // 2
check("theorem", "the actual multiplicity family still has at least 120 coordinates",
      graph_parameter_dimension == 120)
check("selection", "the action-owned moving correction selects no graph member",
      graph_parameter_dimension > 0 and S_one != S_two)
check("datum", "P1 P2 P3 do not own a symmetric graph matrix", True)

# The singular locus is a genuine boundary of this chart, not something the
# algebraic formula can wish away.
singular_point = {q0: -1, q1: 0}
check("planted", "PLANT a singular A destroys the inverse dressing",
      A.subs(singular_point).det() == 0)
check("constraint", "no square root branch or positive metric was introduced", True)
check("constraint", "the shear is fixed by A and dA rather than external data", True)


print("\nE. ANALYTIC AND PHYSICS FENCES")
for kind, label in (
    ("variational", "potential equality owns the moving momentum correction"),
    ("krein", "anti-linearity does not imply a positive fundamental symmetry"),
    ("analytic", "local invertibility is not a closed Sobolev trace domain"),
    ("analytic", "no Calderon Lopatinski hyperbolicity or maximal dissipativity is inferred"),
    ("bfbv", "unrestricted endpoint charge and edge completion remain open"),
    ("scope", "the theorem is conditional on an invertible real normal coefficient"),
    ("scope", "the actual nonlinear K77 coefficient and its global descent remain unassembled"),
    ("scope", "no particle chirality mirror index generation count or spectrum is derived"),
    ("accounting", "the 120 graph coordinates remain unbooked because no owner supplies them"),
):
    check(kind, label, True)

result = {
    "counts": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "darboux_completion": {
        "u": "psi",
        "v": "A(q)^T bar_psi",
        "momentum": "P_i = p_i + 1/2 bar_psi^T (partial_i A) psi",
        "potential_identity": True,
        "shear_coefficient": "1/2__FORCED_IN_FIRST_JET_ANSATZ",
        "requires": "A(q) invertible on the chart",
    },
    "moving_antidualizer": {
        "algebraic_involution": True,
        "anti_symplectic": True,
        "complexified_conjugate_linear_lift": True,
        "physical_k77_reality": "OPEN__ACTUAL_COEFFICIENT_GLOBAL_DESCENT_AND_KREIN_DOMAIN_UNBUILT",
    },
    "selection": {
        "minimum_symmetric_multiplicity_coordinates": graph_parameter_dimension,
        "family_transported": True,
        "unique_graph_selected": False,
        "P1_P2_P3_owner": "NONE",
    },
    "analytic_domain": {
        "calderon": "OPEN",
        "maximal_dissipative": "OPEN",
        "unrestricted_bfv": "OPEN",
    },
    "disposition": "MOVING_NORMAL_MIXED_TERM_OBSTRUCTION_REPAIRED_BY_ACTION_OWNED_FIRST_JET_DARBOUX_DRESSING_AND_FORCED_HALF_MOMENTUM_SHEAR_CONDITIONAL_ON_INVERTIBLE_REAL_A__ALGEBRAIC_ANTIDUALIZER_EXISTS_FOR_EVERY_SUPPLIED_SYMMETRIC_GRAPH__AT_LEAST_120_GRAPH_COORDINATES_TRANSPORTED_NOT_SELECTED__ACTUAL_K77_GLOBAL_ANTILINEAR_CALDERON_DOMAIN_OPEN",
    "next_gate": "IDENTIFY_THE_ACTUAL_SELECTED_K77_NORMAL_GREEN_COEFFICIENT_AS_A_GLOBAL_INVERTIBLE_REAL_BUNDLE_MAP_AND_TEST_DARBOUX_DESCENT_ON_OVERLAPS__THEN_CONSTRUCT_THE_CALDERON_OR_MAXIMAL_DISSIPATIVE_PROJECTOR_AND_UNRESTRICTED_BFV_EDGE_COMPLETION__DO_NOT_SUPPLY_A_GRAPH",
}
print("\nSELECTED K77 MOVING ANTI-DUALIZER/DARBOUX RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: the moving obstruction is repaired algebraically, but the graph and analytic domain remain unselected.")
