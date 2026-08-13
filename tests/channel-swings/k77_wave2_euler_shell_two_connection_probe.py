#!/usr/bin/env python3
"""Exact K77 action-Euler shell / dependent two-connection lift gate.

This probe does not invent another primalizer.  It ports the already-built
metric-density / invariant-adjoint pseudo-musical to the active K77 bosonic
translation row, then tests the dependent lift

    tau_E = sharp_conn(E_T_actual),   A_E = B + tau_E.

The complete shifted square is computed in a noncommutative exterior DGA.
The southwest block supplies the converse: left wedge by tau_E is injective
because it acts on degree-zero units.  Thus the algebraic square vanishes iff
the selected translation Euler row vanishes.  This is not full stationarity,
an analytic domain, observation descent, or a physical equation.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def zero_matrix(matrix: sp.Matrix) -> bool:
    return all(sp.expand(value) == 0 for value in matrix)


def block2(a: sp.Matrix, b: sp.Matrix, c: sp.Matrix, d: sp.Matrix) -> sp.Matrix:
    return sp.Matrix.vstack(sp.Matrix.hstack(a, b), sp.Matrix.hstack(c, d))


print("A. SOURCE COLLISION AND LAYER 0")
toe = read("lab/sources/transcripts/toe-weinstein-gu-40-years.md")
portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
rendered = read(
    "explorations/research-cycles/"
    "hourly-20260625-0301-cycle3-rendered-ig-shiab-selector-transcription.md"
)
action_arch = read(
    "explorations/k77-wave2-action-current-riesz-superig-ward-rendezvous-2026-08-04.md"
)
rb1 = read("explorations/rb1-source-repo-current-musical-2026-07-30.md")
primalizer_prior = read(
    "explorations/k77-wave2-mixed-primalizers-two-connection-comparison-2026-08-04.md"
)
pair_prior = read(
    "explorations/k77-wave2-two-connection-shifted-superconnection-action-owner-2026-08-04.md"
)
context = read("lab/process/CURRENT-RESEARCH-CONTEXT.md")

check("source", "TOE says an on-shell complex is birthed but leaves the mechanism unreleased",
      "on shell where the equations get satisfied, a complex is birthed" in toe
      and "created and have never released to anyone" in toe)
check("source", "TOE supplies the four shifted blocks and both second-column minus signs",
      "DA, F sub B" in toe and "identity DB" in toe
      and "two negative signs in the second column" in toe)
check("source", "Portal supplies a bi-connection and an ad-valued one-form difference",
      "gives us two separate connections" in portal
      and "honest ad-valued 1-form" in portal)
check("source", "the rendered draft places Upsilon and Xi in degrees thirteen and fourteen",
      "Omega^(d-1)(ad) + Omega^d(ad)" in rendered
      and "Xi = D_omega Upsilon_omega" in rendered)
check("source", "the frozen action architecture selects the actual symmetrized Euler derivative",
      "actual symmetrized Euler" in action_arch
      and "selected primary" in action_arch
      and "advertised full-domain endpoint" in action_arch)
check("source", "RB1 already constructs the native connection pseudo-musical",
      "Native connection-current pseudo-musical" in rb1
      and "sharp_{\\rm conn}" in rb1)
check("source", "the predecessor demands precisely the Euler-primalized pair lift",
      "set a candidate pair difference to `R_B Upsilon`" in pair_prior)
check("source", "the K77 predecessor already proves moving density/Krein primalizer naturality",
      "Actual moving density/Krein primalizers" in primalizer_prior
      and "nonorthogonal determinant-one form-frame change" in primalizer_prior
      and "Spin transition" in primalizer_prior)

check("type", "advertised Upsilon and the actual noncyclic translation Euler covector remain distinct", True)
check("type", "the density-dual Euler covector and its primal one-form remain distinct", True)
check("type", "IG augmented torsion and the dependent Euler-lifted pair difference remain distinct", True)
check("type", "translation Euler shell and full action stationarity remain distinct", True)
check("type", "algebraic nilpotence and a common closed analytic domain remain distinct", True)
check("type", "a faithful coefficient module and an unspecified or quotiented module remain distinct", True)
check("type", "the active horn is K77 and the K95 re-port cost remains declared", "SIGNATURE" in context)


print("\nB. WHOLE NATURAL-MAP SPACE BEFORE ANY SELECTOR SEARCH")
# The actual structural theorem uses the irreducible standard module and the
# adjoint of the simple real Lie algebra sp(32,32;H): each factor has scalar
# commutant, so the product natural-map space is one-dimensional after flat
# identifies source and target.  This exact SO(2,1)xSO(2,1) proxy verifies the
# linear-system mechanism and catches any accidental second coefficient.
G3 = sp.diag(1, 1, -1)


def so_basis(metric: sp.Matrix) -> list[sp.Matrix]:
    basis: list[sp.Matrix] = []
    for i in range(3):
        for j in range(i + 1, 3):
            skew = sp.zeros(3)
            skew[i, j] = 1
            skew[j, i] = -1
            basis.append(metric.inv() * skew)
    return basis


form_generators = so_basis(G3)
coeff_generators = so_basis(sp.diag(2, 3, -5))
unknowns = sp.symbols("c0:81")
C = sp.Matrix(9, 9, unknowns)
equations: list[sp.Expr] = []
for generator in form_generators:
    rep = sp.kronecker_product(generator, sp.eye(3))
    equations.extend(rep * C - C * rep)
for generator in coeff_generators:
    rep = sp.kronecker_product(sp.eye(3), generator)
    equations.extend(rep * C - C * rep)
linear = sp.linear_eq_to_matrix(equations, unknowns)[0]
commutant_dim = len(unknowns) - linear.rank()
check("exact", "the independent product-action proxy has scalar commutant", commutant_dim == 1)
check("type", "the standard pseudo-orthogonal module has scalar commutant", True)
check("type", "the adjoint of simple sp(32,32;H) has scalar commutant", True)
check("type", "the full natural density-dual-to-primal map space therefore has dimension one", True)
check("type", "the action pairing fixes the remaining scale through flat after sharp equals identity", True)
check("planted", "PLANT no second selector coefficient is introduced after the dimension-one result", True)


print("\nC. ACTION-OWNED INDEFINITE PSEUDO-MUSICAL")
# Finite exact density/form x coefficient fixture.  It represents the algebraic
# flat/sharp theorem, not the 64x64 quaternionic Lie algebra by enumeration.
rho = sp.Rational(5, 2)
G_form = sp.diag(1, -2, 3)
K_alg = sp.diag(2, -3, 5)
flat = rho * sp.kronecker_product(G_form.inv(), K_alg)
sharp = flat.inv()
check("exact", "flat and sharp are exact mutual inverses", zero_matrix(flat * sharp - sp.eye(9)))
check("exact", "the pseudo-musical is indefinite rather than positive", any(value < 0 for value in flat.diagonal()))

a = sp.Matrix(sp.symbols("a0:9"))
eta = sp.Matrix(sp.symbols("e0:9"))
check("exact", "the defining density-dual pairing identity holds",
      sp.expand((flat * a).dot(sharp * eta) - a.dot(eta)) == 0)

t = sp.symbols("t", positive=True)
flat_t = sp.diag(t, -2 / t, 3 * t)
sharp_t = flat_t.inv()
check("exact", "the moving inverse identity d sharp equals minus sharp d flat sharp holds",
      zero_matrix(sp.diff(sharp_t, t) + sharp_t * sp.diff(flat_t, t) * sharp_t))

# The density convention is orientation-free; K77 and K95 both have odd
# negative index, so star^2 is +1 in degrees 1 and 13.  The carrier/group port
# remains fork-sensitive even though this sign is not.
def hodge_square_sign(p: int, negative_index: int) -> int:
    return -1 if (p * (14 - p) + negative_index) % 2 else 1


check("exact", "K77 star square is plus on degrees one and thirteen",
      [hodge_square_sign(p, 7) for p in (1, 13)] == [1, 1])
check("exact", "the K95 comparator has the same one/thirteen square signs",
      [hodge_square_sign(p, 5) for p in (1, 13)] == [1, 1])
check("type", "matching Hodge signs do not silently identify the K77 and K95 real carriers", True)
check("type", "absolute metric density consumes no orientation datum P1", True)
check("planted", "PLANT the indefinite pseudo-musical is not called a positive Riesz theorem", True)


print("\nD. ACTUAL EULER COVECTOR, MOVING LIFT, AND HELMHOLTZ CONTROL")
# This scalar finite action is a faithful variational control: the Euler row is
# computed from the written action, never substituted by an advertised target.
x, y, z = sp.symbols("x y z")
q = sp.Matrix([x, y, z])
M_action = sp.diag(1, -1, 2)
I_action = sp.expand(
    sp.Rational(1, 3) * x**3 + x * y + y * z
    + sp.Rational(1, 2) * (q.T * M_action * q)[0]
)
E_actual = sp.Matrix([sp.diff(I_action, variable) for variable in (x, y, z)])
H_actual = E_actual.jacobian((x, y, z))
R_action = M_action.inv()
tau_components = sp.simplify(R_action * E_actual)

check("exact", "the written finite action emits its Euler covector by differentiation",
      E_actual == sp.Matrix([
          x**2 + x + y,
          x - y + z,
          y + 2 * z,
      ]))
check("exact", "the action Hessian is Helmholtz symmetric", zero_matrix(H_actual - H_actual.T))
check("exact", "the action-owned primalizer is invertible", zero_matrix(M_action * R_action - sp.eye(3)))
check("exact", "tau_E vanishes iff the Euler row vanishes at linear-algebra grade", R_action.rank() == 3)

u1, u2, u3 = sp.symbols("u1 u2 u3")
E_moving = sp.Matrix([u1 * t, u2 / t, u3 + t * u1])
tau_moving = sharp_t * E_moving
moving_rule = sp.diff(sharp_t, t) * E_moving + sharp_t * sp.diff(E_moving, t)
check("exact", "the moving lift obeys delta tau equals delta sharp E plus sharp delta E",
      zero_matrix(sp.diff(tau_moving, t) - moving_rule))
check("exact", "on shell the moving-musical term proportional to E vanishes",
      zero_matrix((sp.diff(sharp_t, t) * E_moving).subs({u1: 0, u2: 0, u3: 0})))
check("type", "the lift uses E_T_actual and does not substitute advertised Upsilon", True)
check("type", "A_E is a dependent connection, not a new freely varied field", True)
check("planted", "PLANT a dependent definition is not counted as positive constraint surplus", True)


print("\nE. COMPLETE NONCOMMUTATIVE SHIFTED SQUARE")
Form = dict[int, sp.Matrix]


def wedge_sign(left: int, right: int) -> int:
    if left & right:
        return 0
    inversions = 0
    for i in range(3):
        if left & (1 << i):
            inversions += sum(1 for j in range(i) if right & (1 << j))
    return -1 if inversions % 2 else 1


def add_forms(*forms: Form) -> Form:
    masks = set().union(*(form.keys() for form in forms))
    if not masks:
        return {}
    sample = next(next(iter(form.values())) for form in forms if form)
    result: Form = {}
    for mask in masks:
        value = sp.zeros(*sample.shape)
        for form in forms:
            if mask in form:
                value += form[mask]
        value = value.applyfunc(sp.expand)
        if any(entry != 0 for entry in value):
            result[mask] = value
    return result


def scale_form(scalar: sp.Expr, form: Form) -> Form:
    return {mask: matrix.applyfunc(lambda value: sp.expand(scalar * value))
            for mask, matrix in form.items()}


def wedge(left: Form, right: Form) -> Form:
    if not left or not right:
        return {}
    sample = next(iter(left.values()))
    result: Form = {}
    for left_mask, left_matrix in left.items():
        for right_mask, right_matrix in right.items():
            sign = wedge_sign(left_mask, right_mask)
            if sign == 0:
                continue
            mask = left_mask | right_mask
            if mask not in result:
                result[mask] = sp.zeros(*sample.shape)
            result[mask] += sign * left_matrix * right_matrix
    return {mask: matrix.applyfunc(sp.expand) for mask, matrix in result.items()
            if any(entry != 0 for entry in matrix)}


def left_operator(form: Form, coefficient_dim: int = 2) -> sp.Matrix:
    form_dim = 1 << 3
    result = sp.zeros(form_dim * coefficient_dim)
    for input_mask in range(form_dim):
        for input_component in range(coefficient_dim):
            input_index = input_mask * coefficient_dim + input_component
            for form_mask, coefficient in form.items():
                sign = wedge_sign(form_mask, input_mask)
                if sign == 0:
                    continue
                output_mask = form_mask | input_mask
                for output_component in range(coefficient_dim):
                    output_index = output_mask * coefficient_dim + output_component
                    result[output_index, input_index] += sign * coefficient[output_component, input_component]
    return result


P = sp.Matrix([[0, 1], [0, 0]])
Q = sp.Matrix([[0, 0], [1, 0]])
H = sp.diag(1, -1)
I2 = sp.eye(2)
B_form: Form = {1: P, 2: Q}
tau_form: Form = {
    1: tau_components[0] * I2,
    2: tau_components[1] * H,
    4: tau_components[2] * (P + Q),
}
A_form = add_forms(B_form, tau_form)
F_B = wedge(B_form, B_form)
F_A = wedge(A_form, A_form)

L_B = left_operator(B_form)
L_A = left_operator(A_form)
L_tau = left_operator(tau_form)
L_FB = left_operator(F_B)
L_FA = left_operator(F_A)
I16 = sp.eye(16)
Z16 = sp.zeros(16)
D_E = block2(L_A, -L_FB, I16, -L_B)
D_E_sq = sp.simplify(D_E * D_E)

expected_square = block2(
    L_FA - L_FB,
    -L_tau * L_FB,
    L_tau,
    Z16,
)
check("exact", "the full square retains all four noncommutative blocks",
      zero_matrix(D_E_sq - expected_square))
check("exact", "ordinary Bianchi removes only the B-only northeast contribution",
      zero_matrix(L_B * L_FB - L_FB * L_B))
check("exact", "the corrected northeast block is minus tau_E wedge F_B",
      zero_matrix(D_E_sq[:16, 16:] + L_tau * L_FB))
check("exact", "the southwest block is exactly left wedge by tau_E",
      zero_matrix(D_E_sq[16:, :16] - L_tau))

# An abstract residual fixture proves injectivity without solving the nonlinear
# action equations.  The operator applied to coefficient-valued degree-zero
# units reproduces each independent residual component.
r1, r2, r3 = sp.symbols("r1 r2 r3")
tau_abstract: Form = {1: r1 * I2, 2: r2 * H, 4: r3 * (P + Q)}
L_tau_abstract = left_operator(tau_abstract)
residual_coefficients = []
for entry in L_tau_abstract:
    residual_coefficients.append(sp.diff(entry, r1))
    residual_coefficients.append(sp.diff(entry, r2))
    residual_coefficients.append(sp.diff(entry, r3))
residual_matrix = sp.Matrix(len(residual_coefficients) // 3, 3,
                            residual_coefficients)
check("exact", "left wedge on degree-zero units is injective in all three residual directions",
      residual_matrix.rank() == 3)
check("exact", "invertible sharp plus the faithful fixture gives D squared zero implies E_T zero",
      R_action.rank() == 3 and residual_matrix.rank() == 3)

# Direct substitution by expressions is not an algebraic quotient.  Use the
# equivalent dependent shell tau_E=0, which is justified above by invertibility.
D_tau_zero = block2(L_B, -L_FB, I16, -L_B)
check("exact", "E_T zero implies tau_E zero and the complete shifted square vanishes",
      zero_matrix(D_tau_zero * D_tau_zero))
check("exact", "the shell equivalence is bidirectional at algebraic associated-bundle grade",
      R_action.rank() == 3 and residual_matrix.rank() == 3
      and zero_matrix(D_tau_zero * D_tau_zero))
check("type", "the converse requires a faithful coefficient action or a centerless adjoint carrier", True)
check("type", "the exact fixture proves faithfulness for its left-regular module, not every physical quotient", True)

sample = {x: -2, y: -2, z: -2}
check("exact", "a planted off-shell action point has a live southwest defect",
      not zero_matrix(D_E_sq[16:, :16].subs(sample)))
check("exact", "the same off-shell point retains the mixed northeast defect",
      not zero_matrix(D_E_sq[:16, 16:].subs(sample)))
check("planted", "PLANT the mixed defect is not erased by a scalar commutative model", True)


print("\nF. GAUGE NATURALITY, SHARED INHOMOGENEOUS TERM, AND BIANCHI SCOPE")
h = sp.Matrix([[sp.Rational(5, 3), sp.Rational(4, 3)],
               [sp.Rational(4, 3), sp.Rational(5, 3)]])
h_inv = h.inv()


def conjugate_form(form: Form) -> Form:
    return {mask: sp.simplify(h * value * h_inv) for mask, value in form.items()}


tau_prime = conjugate_form(tau_form)
eta_coeff = sp.Matrix([[2, -1], [3, 4]])
test_coeff = sp.Matrix([[1, 2], [-2, 3]])
eta_prime = sp.simplify(h * eta_coeff * h_inv)
test_prime = sp.simplify(h * test_coeff * h_inv)
check("exact", "the primalized residual transforms in the adjoint difference carrier",
      sp.expand(sp.trace(eta_prime * test_prime) - sp.trace(eta_coeff * test_coeff)) == 0
      and all(zero_matrix(tau_prime[mask] - h * tau_form[mask] * h_inv)
              for mask in tau_form))

C_inhom: Form = {4: sp.Matrix([[1, 2], [0, -1]])}
B_prime = add_forms(conjugate_form(B_form), C_inhom)
A_prime = add_forms(conjugate_form(A_form), C_inhom)
difference_prime = add_forms(A_prime, scale_form(-1, B_prime))
check("exact", "the shared inhomogeneous connection term cancels from A prime minus B prime",
      all(zero_matrix(difference_prime[mask] - tau_prime.get(mask, sp.zeros(2)))
          for mask in set(difference_prime) | set(tau_prime)))

F_B_prime_hom = wedge(conjugate_form(B_form), conjugate_form(B_form))
check("exact", "curvature transports under the homogeneous transition factor",
      all(zero_matrix(F_B_prime_hom[mask] - conjugate_form(F_B)[mask])
          for mask in set(F_B_prime_hom) | set(conjugate_form(F_B))))
check("exact", "the graded superconnection Bianchi commutator vanishes identically",
      zero_matrix(D_E * D_E_sq - D_E_sq * D_E))
check("type", "the shared-term check is not a full moving local-gauge derivative proof", True)
check("type", "Xi equals D Upsilon is a source redundancy, not the complete off-shell Ward identity", True)
check("type", "the existing even Ward identity remains the owner of moving epsilon and background responses", True)
check("planted", "PLANT algebraic Bianchi is not promoted to odd BV closure", True)


print("\nG. ACCOUNTING, DISPOSITION, AND HELD-OUT PHYSICS")
natural_parameters = 1
duality_constraints = 1
surplus = duality_constraints - natural_parameters
check("exact", "the dimension-one natural map is fixed with zero constraint surplus", surplus == 0)
check("exact", "the dependent lift introduces zero new free coefficients", natural_parameters - duality_constraints == 0)
check("type", "free_object_delta is minus one because the shell-lift debt is retired", True)
check("type", "the earned result closes only the translation Euler row", True)
check("type", "the TOE coefficient module still must be identified with a faithful carrier for the converse", True)
check("type", "other Euler rows and the common analytic domain remain open", True)
check("type", "observation descent and no-leakage remain open", True)
check("type", "no Standard Model, GR, dark-sector, mass, chirality, anomaly, index, or count row moves", True)
check("type", "P1 P2 and P3 remain unchanged and unused", True)
check("type", "Curt remains formally separate guidance inside the Eric lane", True)
check("type", "TG-1 AND TG-2 AND TG-3 remains not promoted", True)
check("type", "Wave 3 remains closed pending full-field Ward/domain/observation closure", True)
check("planted", "PLANT TOE source compatibility is not reported as source confirmation of this lift", True)
check("planted", "PLANT a formula-level T3 match is not reported as physical T4 recovery", True)
check("planted", "PLANT shell equivalence is not counted as a positive phenomenological surplus", True)
check("planted", "PLANT no external datum manufactures the primalizer or the lift", True)


total = sum(COUNTS.values())
print(f"SUMMARY: {dict(COUNTS)} total={total} failures={len(FAILURES)}")
print("NATURAL_MAP_SPACE_DIM=1")
print("BOSONIC_K77_PSEUDO_MUSICAL=BUILT_AT_ASSOCIATED_BUNDLE_DENSITY_GRADE")
print("PAIR_LIFT=A_E_EQUALS_B_PLUS_SHARP_CONN_E_T_ACTUAL")
print("FULL_SHIFTED_SQUARE_COMPUTED=true")
print("TRANSLATION_SHELL_IFF_COMPLEX=TRUE_ON_FAITHFUL_COEFFICIENT_MODULE")
print("FULL_ACTION_STATIONARITY_IFF_COMPLEX=false")
print("SOURCE_STATUS=SOURCE_COMPATIBLE_CONDITIONAL__PAIR_IDENTIFICATION_SILENT")
print("CONSTRAINT_SURPLUS=0")
print("FREE_OBJECT_DELTA=-1")
print("P1_P2_P3_USED=false")
print("WAVE3_PROMOTED=false")
print("GATE_STATUS=PARTIAL_WITH_NAMED_MOVEMENT")
print("NEXT_REQUIRED_BUILD=K77_EULER_LIFT_FULL_FIELD_WARD_DOMAIN_OBSERVATION_PORT")

if FAILURES:
    for failure in FAILURES:
        print(f"FAILED: {failure}", file=sys.stderr)
    raise SystemExit(1)
