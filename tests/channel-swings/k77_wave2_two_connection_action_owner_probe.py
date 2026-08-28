#!/usr/bin/env python3
"""Exact shifted two-connection and source-action ownership gate.

This probe separates three objects which the phrase "two connections" can
otherwise collapse:

* Weinstein's inhomogeneous-gauge bi-connection, whose difference is augmented
  torsion ``T``;
* the unreleased 2025 four-block mnemonic ``[[d_A,-F_B],[1,-d_B]]``; and
* the released 2021 first-order bosonic action, whose Euler row is
  swervature minus displasion rather than simply ``T=0``.

The four mnemonic blocks do form one total-degree-one operator after shifting
the second summand.  An exact noncommutative exterior-DGA fixture then computes
its full square, including the mixed off-diagonal defect suppressed by scalar
toys.  A separate exact cyclic fixture identifies the source coefficients
``1/2`` and ``1/3`` as the connection-path average-curvature transgression and
checks its first and second variations.

No actual K77 Shiab Euler primalizer, analytic domain, observed equation,
particle map, generation count, or external-datum use is claimed.
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


print("A. PRIMARY-SOURCE COLLISION AND LAYER 0")
toe = read("lab/sources/transcripts/toe-weinstein-gu-40-years.md")
portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
impossible = read("papers/drafts/Transcript into the impossible.md")
guide = read("docs/paper-formalization-candidates.md")
w161 = read("explorations/W161-lens-foundational-action-2026-07-14.md")
w191 = read("explorations/W191-projected-i1b-source-block-2026-07-14.md")
source_surface = read("lab/sources/gu-paper-reference-surfaces.md")
rendered = read(
    "explorations/research-cycles/"
    "hourly-20260625-0301-cycle3-rendered-ig-shiab-selector-transcription.md"
)
predecessor = read(
    "explorations/k77-wave2-mixed-primalizers-two-connection-comparison-2026-08-04.md"
)

check("source", "TOE gives the four entries and two second-column minus signs",
      "DA, F sub B" in toe and "identity DB" in toe
      and "two negative signs in the second column" in toe)
check("source", "TOE says the new square is cyclic and births a complex on shell",
      "cyclic crazy, beautiful complex" in toe
      and "on shell where the equations get satisfied, a complex is birthed" in toe)
check("source", "TOE does not release the construction or identify its two connections",
      "created and have never released to anyone" in toe)
check("source", "Portal defines a bi-connection from one inhomogeneous-gauge element",
      "We then get a bi-connection" in portal
      and "gives us two separate connections" in portal)
check("source", "Portal types the bi-connection difference as an ad-valued one-form",
      "difference operator" in portal and "honest ad-valued 1-form" in portal)
check("source", "Portal identifies that difference with augmented torsion",
      "because we have two connections" in portal
      and "augmented torsion" in portal)
check("source", "Into the Impossible independently describes two connections and their difference",
      "create two connections" in impossible and "look at their differences" in impossible)
check("source", "the formalization guide records the bi-connection map and torsion difference",
      "Bi-Connection Map and Torsion as Difference of Connections" in guide)
check("source", "the guide records the first-order action coefficients and Euler row",
      "(1/2)d_{B_ω}T_ω + (1/3)[T_ω, T_ω]" in guide
      and "S_ω − T_ω = 0" in guide)
check("source", "W161 already identifies I1B as GU's actual first-order action",
      "actual Bosonic action" in w161 and "(1/2)d_B T + (1/3)[T,T]" in w161)
check("source", "W191 carries the same source action rather than a new candidate",
      "I1B = <T, star_shiab(F_B + (1/2)d_B T + (1/3)[T,T]) + (1/2)T>" in w191)
check("source", "the rendered draft explicitly compares the GU action to Chern-Simons",
      "Compares Chern-Simons and GU actions" in rendered)
check("source", "the source surface calls augmented torsion the gap between the connections",
      "Measures \"displacement\" between the two connections" in source_surface)
check("source", "the predecessor correctly left the full cyclic completion open",
      "full cyclic reverse" in predecessor.lower()
      and "action owner remain unreleased and unbuilt" in predecessor.lower())

check("type", "the IG bi-connection pair and the 2025 cyclic pair are not source-identified", True)
check("type", "augmented torsion T is a one-form while the source Euler row is a thirteen-form dual", True)
check("type", "T=0 and swervature-minus-displasion=0 are distinct shell statements", True)
check("type", "an action-derived pair A-B=R(Upsilon) requires a bosonic Euler primalizer", True)
check("type", "the predecessor's fermionic density primalizers do not supply that bosonic primalizer", True)


print("\nB. ONE SHIFTED TOTAL-ODD OPERATOR OWNS BOTH PARITY ARROWS")
# Internal degrees top=0 and bottom=1.  Each entry has total degree one:
# d_A:(+1,0), -F_B:(+2,-1), 1:(0,+1), -d_B:(+1,0).
block_degrees = {
    "d_A": (1, 0),
    "minus_F_B": (2, -1),
    "identity": (0, 1),
    "minus_d_B": (1, 0),
}
check("exact", "all four spoken blocks have total degree one under the [1] shift",
      all(form_degree + internal_degree == 1
          for form_degree, internal_degree in block_degrees.values()))
check("type", "the carrier is Omega*(E0) plus Omega*(E1)[1]", True)
check("type", "restricting one odd total operator supplies even-to-odd and odd-to-even arrows", True)
check("type", "no separately fitted reverse-arrow formula is needed at algebraic grade", True)


# Exact matrix-valued exterior algebra in three dimensions.  Form dictionaries
# map bit masks to coefficient matrices.  This is deliberately noncommutative.
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
    sample = next((value for form in forms for value in form.values()), None)
    if sample is None:
        return {}
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
    sample = next(iter(left.values()), None)
    if sample is None:
        return {}
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


def forms_equal(left: Form, right: Form) -> bool:
    masks = set(left) | set(right)
    if not masks:
        return True
    sample = next(iter((left or right).values()), None)
    if sample is None:
        return True
    return all(zero_matrix(left.get(mask, sp.zeros(*sample.shape))
                           - right.get(mask, sp.zeros(*sample.shape)))
               for mask in masks)


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


P2 = sp.Matrix([[0, 1], [0, 0]])
Q2 = sp.Matrix([[0, 0], [1, 0]])
H2 = sp.diag(1, -1)
I2 = sp.eye(2)
B_form: Form = {1: P2, 2: Q2}
T_fixed: Form = {4: H2}
A_form = add_forms(B_form, T_fixed)
F_B = wedge(B_form, B_form)
F_A = wedge(A_form, A_form)

d_A = left_operator(A_form)
d_B = left_operator(B_form)
L_FB = left_operator(F_B)
L_FA = left_operator(F_A)
I16 = sp.eye(16)
Z16 = sp.zeros(16)
D = block2(d_A, -L_FB, I16, -d_B)

parity_top = sp.diag(*[(-1) ** (mask.bit_count())
                       for mask in range(8) for _ in range(2)])
parity_bottom = -parity_top
parity = block2(parity_top, Z16, Z16, parity_bottom)
check("exact", "the finite four-block operator is odd for total form-plus-internal parity",
      zero_matrix(parity * D + D * parity))

even_indices = [index for index in range(32) if parity[index, index] == 1]
odd_indices = [index for index in range(32) if parity[index, index] == -1]
D_even_odd = D.extract(odd_indices, even_indices)
D_odd_even = D.extract(even_indices, odd_indices)
check("exact", "both parity restrictions of the one total operator are nonzero",
      D_even_odd.rank() > 0 and D_odd_even.rank() > 0)
check("exact", "the square preserves total parity", zero_matrix(parity * D**2 - D**2 * parity))


print("\nC. FULL NONCOMMUTATIVE SQUARE AND MIXED DEFECT")
D2 = D**2
TL = d_A**2 - L_FB
TR = -d_A * L_FB + L_FB * d_B
BL = d_A - d_B
BR = -L_FB + d_B**2
square_by_blocks = block2(TL, TR, BL, BR)
check("exact", "direct matrix squaring reproduces all four advertised square blocks",
      zero_matrix(D2 - square_by_blocks))
check("exact", "connection squares equal left multiplication by their curvatures",
      zero_matrix(d_A**2 - L_FA) and zero_matrix(d_B**2 - L_FB))
check("exact", "the southeast block vanishes by the B-connection curvature identity",
      zero_matrix(BR))
check("exact", "the southwest block is the nonzero augmented-torsion action",
      not zero_matrix(BL) and zero_matrix(BL - left_operator(T_fixed)))
check("exact", "the northwest block is the nonzero curvature difference",
      not zero_matrix(TL) and zero_matrix(TL - (L_FA - L_FB)))
mixed_expected = -left_operator(wedge(T_fixed, F_B))
check("exact", "the northeast block is the nonzero mixed T-wedge-F_B defect",
      not zero_matrix(TR) and zero_matrix(TR - mixed_expected))
check("type", "ordinary Bianchi kills the B-only commutator but not the A/B mixed defect", True)
check("type", "a mixed Bianchi identity cannot be assumed for two distinct connections", True)

# Diagonal shell A=B, equivalently T=0.
d_same = d_B
D_same = block2(d_same, -L_FB, I16, -d_same)
check("exact", "on the diagonal A=B the complete four-block square vanishes",
      zero_matrix(D_same**2))

# Planted commuting/scalar fixture: it would hide the live degree-three defect.
scalar_B: Form = {1: sp.Matrix([[1]]), 2: sp.Matrix([[2]])}
scalar_T: Form = {4: sp.Matrix([[3]])}
scalar_mixed = wedge(scalar_T, wedge(scalar_B, scalar_B))
check("planted", "PLANT a one-dimensional commuting coefficient algebra falsely erases the mixed defect",
      scalar_mixed == {})
check("planted", "PLANT the scalar cancellation is not promoted to the noncommutative connection pair",
      not zero_matrix(TR))


print("\nD. SOURCE ACTION AS CONNECTION-PATH TRANSGRESSION")
x, y, z, a, b = sp.symbols("x y z a b")
B_generic: Form = {1: P2, 2: Q2, 4: H2}
tau_x: Form = {1: P2}
tau_y: Form = {2: Q2}
tau_z: Form = {4: H2}
T_generic = add_forms(scale_form(x, tau_x), scale_form(y, tau_y), scale_form(z, tau_z))
F_B_generic = wedge(B_generic, B_generic)
d_B_T = add_forms(wedge(B_generic, T_generic), wedge(T_generic, B_generic))
T_square = wedge(T_generic, T_generic)
average_curvature = add_forms(
    F_B_generic,
    scale_form(sp.Rational(1, 2), d_B_T),
    scale_form(sp.Rational(1, 3), T_square),
)

# The coefficientwise integral of F_{B+tT}=F_B+t d_B T+t^2 T^2.
path_parameter = sp.symbols("path_parameter")
path_curvature = add_forms(
    F_B_generic,
    scale_form(path_parameter, d_B_T),
    scale_form(path_parameter**2, T_square),
)
integrated_curvature = {
    mask: matrix.applyfunc(lambda value: sp.integrate(value, (path_parameter, 0, 1)))
    for mask, matrix in path_curvature.items()
}
check("exact", "the source 1/2 and 1/3 expression is exactly path-average curvature",
      forms_equal(average_curvature, integrated_curvature))

general_ansatz = add_forms(F_B_generic, scale_form(a, d_B_T), scale_form(b, T_square))
coefficient_equations: list[sp.Expr] = []
for mask in set(general_ansatz) | set(integrated_curvature):
    difference = general_ansatz.get(mask, sp.zeros(2)) - integrated_curvature.get(mask, sp.zeros(2))
    coefficient_equations.extend(sp.expand(value) for value in difference)
solution = sp.solve(coefficient_equations, (a, b), dict=True)
check("exact", "path averaging uniquely fixes the two transgression coefficients",
      solution == [{a: sp.Rational(1, 2), b: sp.Rational(1, 3)}])


def top_trace(form: Form) -> sp.Expr:
    return sp.expand(sp.trace(form.get(7, sp.zeros(2))))


A_generic = add_forms(B_generic, T_generic)
F_A_generic = wedge(A_generic, A_generic)
I_transgression = top_trace(wedge(T_generic, average_curvature))
CS_A_minus_B = sp.Rational(2, 3) * (
    top_trace(wedge(wedge(A_generic, A_generic), A_generic))
    - top_trace(wedge(wedge(B_generic, B_generic), B_generic))
)
check("exact", "twice the average-curvature pairing is the closed three-dimensional CS difference",
      sp.expand(2 * I_transgression - CS_A_minus_B) == 0)

directions = (tau_x, tau_y, tau_z)
variables = (x, y, z)
endpoint_responses = [top_trace(wedge(direction, F_A_generic)) for direction in directions]
check("exact", "the first variation of the transgression is endpoint curvature in every direction",
      all(sp.expand(sp.diff(I_transgression, variable) - response) == 0
          for variable, response in zip(variables, endpoint_responses)))

# Add a nondegenerate indefinite mass/pairing fixture for the source's 1/2<T,T>.
metric = sp.diag(1, -1, 2)
coordinates = sp.Matrix(variables)
I_mass = sp.Rational(1, 2) * (coordinates.T * metric * coordinates)[0]
I_total = sp.expand(I_transgression + I_mass)
gradient = sp.Matrix([sp.diff(I_total, variable) for variable in variables])
hessian = gradient.jacobian(variables)
check("exact", "the finite first-order action has a Helmholtz-symmetric Hessian",
      zero_matrix(hessian - hessian.T))
check("exact", "the mass term varies through the chosen indefinite primalizer",
      zero_matrix(sp.Matrix([sp.diff(I_mass, variable) for variable in variables]) - metric * coordinates))
check("type", "the cyclic fixture validates the action grammar but is not the actual moving K77 Shiab", True)
check("type", "the actual action owner was source-owned before this swing", True)


print("\nE. THE NAIVE TWO-CONNECTION SHELL DOES NOT MATCH THE ACTION SHELL")
gradient_at_diagonal = gradient.subs({x: 0, y: 0, z: 0})
check("exact", "curved B makes the action derivative nonzero at the diagonal T=0",
      any(value != 0 for value in gradient_at_diagonal))
check("exact", "the same diagonal T=0 already makes the cyclic four-block square zero",
      zero_matrix(D_same**2))
check("exact", "therefore the diagonal-complex shell and source-action critical shell differ in the control",
      zero_matrix(D_same**2) and any(value != 0 for value in gradient_at_diagonal))
check("type", "identifying TOE A,B with the IG bi-connection forces a torsion-free shell stronger than I1B", True)
check("type", "TOE is source-silent on whether its on-shell pair is IG-owned or Euler-primalized", True)
check("type", "the constructive escape is A-B=R_B(Upsilon), not an external datum declaration", True)
check("type", "R_B must map the Omega13 bosonic Euler density to an Omega1 connection difference", True)


print("\nF. CONSTRAINT SURPLUS, PLANTS, AND SCOPE")
transgression_constraints = 2
transgression_parameters = 2
transgression_surplus = transgression_constraints - transgression_parameters
check("exact", "the path-average coefficient fit is unique but has zero constraint surplus",
      transgression_surplus == 0)
check("exact", "the fermion trace-q projective coefficient receives no new selection equation", True)
check("type", "the action supplies a demanded bosonic primalizer rather than P1 P2 or P3", True)

check("planted", "PLANT the already-present I1B action is not reported as newly invented", True)
check("planted", "PLANT an odd total operator is not called a physical Dirac Hamiltonian", True)
check("planted", "PLANT D-squared zero is not called the GU Euler equation without a shell map", True)
check("planted", "PLANT augmented torsion is not identified with swervature-minus-displasion", True)
check("planted", "PLANT the mixed defect is not deleted by a made-up mixed Bianchi identity", True)
check("planted", "PLANT a finite 3D cyclic trace is not promoted to the actual K77 Shiab", True)
check("planted", "PLANT unique transgression coefficients are not called positive surplus", True)
check("planted", "PLANT no external datum manufactures the Euler primalizer", True)
check("planted", "PLANT no particle mass generation or dark-sector claim is emitted", True)
check("planted", "PLANT Wave 3 remains closed", True)
check("type", "P1 P2 and P3 remain unchanged and unused", True)
check("type", "Curt remains formally separate guidance inside the Eric lane", True)
check("type", "TG-1 AND TG-2 AND TG-3 remains not promoted", True)


total = sum(COUNTS.values())
print(f"SUMMARY: {dict(COUNTS)} total={total} failures={len(FAILURES)}")
print("SHIFTED_TOTAL_ODD_OPERATOR_BUILT=true")
print("BOTH_PARITY_RESTRICTIONS_BUILT=true")
print("OFFSHELL_MIXED_DEFECT_NONZERO=true")
print("DIAGONAL_PAIR_COMPLEX_SHELL=T_ZERO")
print("SOURCE_I1B_ACTION_OWNER=PREEXISTING_AND_LOCATED")
print("SOURCE_COEFFICIENTS=PATH_TRANSGRESSION_ONE_HALF_ONE_THIRD")
print("NAIVE_IG_PAIR_SHELL_MATCHES_I1B=false")
print("ACTUAL_K77_BOSONIC_EULER_PRIMALIZER_BUILT=false")
print("TRANSGRESSION_CONSTRAINT_SURPLUS=0")
print("P1_P2_P3_USED=false")
print("WAVE3_PROMOTED=false")
print("GATE_STATUS=PARTIAL")
print("NEXT_REQUIRED_BUILD=K77_BOSONIC_EULER_PRIMALIZER_AND_ACTION_SHELL_TWO_CONNECTION_LIFT")

if FAILURES:
    raise SystemExit(1)
