#!/usr/bin/env python3
r"""Resolver Wave I: nonlinear Met(X) and connection-induced Theta candidate.

This is a local, exact, three-chart construction.  It distinguishes the
tautological metric ``h`` on ``Met(X)`` from the observer metric whose
Levi-Civita connection supplies the horizontal splitting.  In source order,

    Theta_{Gamma,h}(v, hdot) = (kappa, alpha)
    kappa = hdot - Gamma(v)^T h - h Gamma(v),  alpha = h(v,-).

For matrix calculations only, the two direct summands are swapped to the
Clifford order ``(alpha, kappa) = H* + V`` used by the predecessor probe.

The probe verifies a nonlinear three-chart cocycle, the Christoffel/Hessian
cancellation, trace-reversed vertical and total signatures, an exact adapted
frame descent, a coherent positive Spin lift with a planted sign inconsistency,
chosen-J naturality, and a Riesz-ported associated rank-252 projector family.
It does *not*
construct a global atlas for arbitrary X, prove existence of a Lorentz
observer section or spin structure, identify the observer Levi-Civita
connection with the distinguished source connection, vary a source action,
or close Ward/Green/domain/no-leakage.
"""
from __future__ import annotations

import contextlib
from fractions import Fraction
import importlib
import io
from itertools import combinations
from pathlib import Path
import sys

import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

with contextlib.redirect_stdout(io.StringIO()):
    wave_h = importlib.import_module(
        "resolver_wave_h_public_native_combined_port_probe"
    )


FAILURES: list[str] = []
COUNTS = {
    "exact": 0,
    "numeric": 0,
    "source": 0,
    "type": 0,
    "planted": 0,
}


def check(kind: str, label: str, condition: bool, detail: str = "") -> None:
    COUNTS[kind] += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'} [{kind}]: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def matrix_zero(value: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in value)


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and matrix_zero(left - right)


def compose_subs(value, old, replacement):
    return value.subs(dict(zip(old, replacement)), simultaneous=True)


def block_diag(*blocks: sp.MatrixBase) -> sp.Matrix:
    return sp.diag(*blocks)


R = sp.Rational
ETA4 = sp.diag(1, 1, 1, -1)
ETA14 = sp.diag(*wave_h.ETA)
PAIRS = tuple((i, j) for i in range(4) for j in range(i, 4))


def symmetric_matrix(components) -> sp.Matrix:
    out = sp.zeros(4)
    for value, (i, j) in zip(components, PAIRS):
        out[i, j] = value
        out[j, i] = value
    return out


def symmetric_components(value: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix([value[i, j] for i, j in PAIRS])


def symmetric_representation(change: sp.MatrixBase) -> sp.Matrix:
    """Matrix of k -> change.T k change in the ten independent slots."""
    columns = []
    for column in range(10):
        basis = [sp.Integer(0)] * 10
        basis[column] = sp.Integer(1)
        columns.append(symmetric_components(
            change.T * symmetric_matrix(basis) * change
        ))
    return sp.Matrix.hstack(*columns)


def de_witt_matrix(metric: sp.MatrixBase, trace_reversed: bool = True) -> sp.Matrix:
    inverse = metric.inv()
    columns = []
    basis_matrices = []
    for column in range(10):
        basis = [sp.Integer(0)] * 10
        basis[column] = sp.Integer(1)
        basis_matrices.append(symmetric_matrix(basis))
    for left in basis_matrices:
        row = []
        for right in basis_matrices:
            value = sp.trace(inverse * left * inverse * right)
            if trace_reversed:
                value -= R(1, 2) * sp.trace(inverse * left) * sp.trace(inverse * right)
            row.append(sp.simplify(value))
        columns.append(row)
    return sp.Matrix(columns)


def levi_civita(metric: sp.MatrixBase, coordinates) -> list[sp.Matrix]:
    inverse = metric.inv()
    dimension = metric.rows
    out: list[sp.Matrix] = []
    for direction in range(dimension):
        gamma = sp.zeros(dimension)
        for upper in range(dimension):
            for lower in range(dimension):
                gamma[upper, lower] = sp.simplify(R(1, 2) * sum(
                    inverse[upper, contracted] * (
                        sp.diff(metric[contracted, lower], coordinates[direction])
                        + sp.diff(metric[contracted, direction], coordinates[lower])
                        - sp.diff(metric[direction, lower], coordinates[contracted])
                    )
                    for contracted in range(dimension)
                ))
        out.append(gamma)
    return out


def transform_connection(gamma_old: list[sp.Matrix], old_coordinates,
                         old_in_new, inverse_jacobian: sp.MatrixBase,
                         new_coordinates) -> list[sp.Matrix]:
    """Transform Gamma with B=dx_old/dx_new and A=B^-1."""
    old_substitution = dict(zip(old_coordinates, old_in_new))
    old_gamma = [entry.subs(old_substitution, simultaneous=True)
                 for entry in gamma_old]
    forward = inverse_jacobian.inv()
    out = []
    for direction, coordinate in enumerate(new_coordinates):
        contracted = sp.zeros(4)
        for old_direction in range(4):
            contracted += inverse_jacobian[old_direction, direction] * old_gamma[old_direction]
        out.append(sp.simplify(
            forward * contracted * inverse_jacobian
            + forward * inverse_jacobian.diff(coordinate)
        ))
    return out


def gamma_contraction(gamma: list[sp.Matrix], vector: sp.MatrixBase) -> sp.Matrix:
    out = sp.zeros(4)
    for direction in range(4):
        out += vector[direction] * gamma[direction]
    return out


def theta_matrix(metric: sp.MatrixBase, gamma: list[sp.Matrix]) -> sp.Matrix:
    """Computational order swap(Theta)=(alpha_4,kappa_10)."""
    connection_slots = sp.zeros(10, 4)
    for direction in range(4):
        contracted = gamma[direction].T * metric + metric * gamma[direction]
        connection_slots[:, direction] = symmetric_components(contracted)
    return sp.Matrix.vstack(
        sp.Matrix.hstack(metric, sp.zeros(4, 10)),
        sp.Matrix.hstack(-connection_slots, sp.eye(10)),
    )


def coordinate_gimmel(metric: sp.MatrixBase, gamma: list[sp.Matrix],
                      trace_reversed: bool = True) -> sp.Matrix:
    chimeric = block_diag(
        metric.inv(),
        de_witt_matrix(metric, trace_reversed=trace_reversed),
    )
    theta = theta_matrix(metric, gamma)
    return sp.simplify(theta.T * chimeric * theta)


print("A. NONLINEAR THREE-CHART MET(X) COCYCLE")

x = sp.symbols("x0:4", real=True)
y = sp.symbols("y0:4", real=True)
z = sp.symbols("z0:4", real=True)
a = R(1, 3)
b = R(1, 5)

f01 = sp.Matrix([2 * x[0], x[1] + a * x[0] ** 2, x[2], x[3]])
i10 = sp.Matrix([y[0] / 2, y[1] - a * (y[0] / 2) ** 2, y[2], y[3]])
f12 = sp.Matrix([y[0], y[1], 3 * y[2] + b * y[1] ** 2, y[3]])
i21 = sp.Matrix([z[0], z[1], (z[2] - b * z[1] ** 2) / 3, z[3]])
f02 = sp.Matrix([
    2 * x[0],
    x[1] + a * x[0] ** 2,
    3 * x[2] + b * (x[1] + a * x[0] ** 2) ** 2,
    x[3],
])
i20 = sp.Matrix([
    z[0] / 2,
    z[1] - a * (z[0] / 2) ** 2,
    (z[2] - b * z[1] ** 2) / 3,
    z[3],
])

A01 = f01.jacobian(x)
B01 = i10.jacobian(y)
A12 = f12.jacobian(y)
B12 = i21.jacobian(z)
A02 = f02.jacobian(x)
B02 = i20.jacobian(z)

check("exact", "each nonlinear chart has an exact polynomial/rational inverse",
      matrix_equal(compose_subs(i10, y, f01), sp.Matrix(x))
      and matrix_equal(compose_subs(f01, x, i10), sp.Matrix(y))
      and matrix_equal(compose_subs(i21, z, f12), sp.Matrix(y))
      and matrix_equal(compose_subs(f12, y, i21), sp.Matrix(z)))
check("exact", "the direct and sequential base maps agree on the triple overlap",
      matrix_equal(f02, compose_subs(f12, y, f01))
      and matrix_equal(i20, compose_subs(i10, y, i21)))
check("exact", "the inverse Jacobians obey the same triple-overlap law",
      matrix_equal(B02, compose_subs(B01, y, i21) * B12))
check("planted", "both transition families contain a nonzero Hessian",
      any(sp.diff(f01[row], x[col], x[col]) != 0 for row in range(4) for col in range(4))
      and any(sp.diff(f12[row], y[col], y[col]) != 0 for row in range(4) for col in range(4)))
check("exact", "the oriented base Jacobians have determinants 2, 3, and 6",
      sp.det(A01) == 2 and sp.det(A12) == 3 and sp.det(A02) == 6)

# The observer metric chooses Gamma.  The independent fibre coordinate h below
# is deliberately *not* identified with this metric.
g0 = ETA4
g1 = sp.simplify(B01.T * g0 * B01)
g2 = sp.simplify(B02.T * g0 * B02)
g2_sequential = sp.simplify(B12.T * compose_subs(g1, y, i21) * B12)
gamma0 = [sp.zeros(4) for _ in range(4)]
gamma1_lc = levi_civita(g1, y)
gamma2_lc = levi_civita(g2, z)
gamma1_rule = transform_connection(gamma0, x, i10, B01, y)
gamma2_rule = transform_connection(gamma0, x, i20, B02, z)
gamma2_seq = transform_connection(gamma1_rule, y, i21, B12, z)

check("exact", "the observer metric descends directly and sequentially",
      matrix_equal(g2, g2_sequential))
check("exact", "the transformed zero connection equals the computed Levi-Civita connection",
      all(matrix_equal(left, right) for left, right in zip(gamma1_rule, gamma1_lc))
      and all(matrix_equal(left, right) for left, right in zip(gamma2_rule, gamma2_lc)))
check("exact", "the Christoffel rule itself satisfies the triple-overlap cocycle",
      all(matrix_equal(left, right) for left, right in zip(gamma2_rule, gamma2_seq)))
check("planted", "the nonlinear charts make the transformed Christoffels genuinely nonzero",
      any(not matrix_zero(entry) for entry in gamma1_rule)
      and any(not matrix_zero(entry) for entry in gamma2_rule))


print("\nB. TOTAL-SPACE JACOBIAN AND THETA RECONSTRUCTION CANCELLATION")

h_symbols = sp.symbols("h00 h01 h02 h03 h11 h12 h13 h22 h23 h33", real=True)
k_symbols = sp.symbols("k00 k01 k02 k03 k11 k12 k13 k22 k23 k33", real=True)
h = symmetric_matrix(h_symbols)

B01_source = compose_subs(B01, y, f01)
h1_source = sp.simplify(B01_source.T * h * B01_source)
q0 = sp.Matrix([*x, *h_symbols])
q1_output = sp.Matrix([*f01, *symmetric_components(h1_source)])
D01 = q1_output.jacobian(q0)

h1_symbols = sp.symbols("u00 u01 u02 u03 u11 u12 u13 u22 u23 u33", real=True)
h1_independent = symmetric_matrix(h1_symbols)
B12_source = compose_subs(B12, z, f12)
h2_from_1 = sp.simplify(B12_source.T * h1_independent * B12_source)
q1 = sp.Matrix([*y, *h1_symbols])
q2_from_1 = sp.Matrix([*f12, *symmetric_components(h2_from_1)])
D12 = q2_from_1.jacobian(q1)

B02_source = compose_subs(B02, z, f02)
h2_source = sp.simplify(B02_source.T * h * B02_source)
q2_output = sp.Matrix([*f02, *symmetric_components(h2_source)])
D02 = q2_output.jacobian(q0)

sub_01 = dict(zip(q1, q1_output))
D12_after_01 = D12.subs(sub_01, simultaneous=True)
q2_composed = q2_from_1.subs(sub_01, simultaneous=True)

check("exact", "the fourteen-dimensional total-space maps compose exactly",
      matrix_equal(q2_output, q2_composed))
check("exact", "their full first jets satisfy D02=(D12 after 01)D01",
      matrix_equal(D02, D12_after_01 * D01))

# These are operator identities on the three overlaps, not only point tests.
gamma1_source = [compose_subs(entry, y, f01) for entry in gamma1_rule]
gamma2_source = [compose_subs(entry, z, f02) for entry in gamma2_rule]
gamma2_from_1_source = [compose_subs(entry, z, f12) for entry in gamma2_seq]
theta0_symbolic = theta_matrix(h, gamma0)
theta1_source = theta_matrix(h1_source, gamma1_source)
theta1_independent = theta_matrix(h1_independent, gamma1_rule)
theta2_source = theta_matrix(h2_source, gamma2_source)
theta2_from_1 = theta_matrix(h2_from_1, gamma2_from_1_source)
L01_source = block_diag(B01_source.T, symmetric_representation(B01_source))
L12_source = block_diag(B12_source.T, symmetric_representation(B12_source))
L02_source = block_diag(B02_source.T, symmetric_representation(B02_source))
check("exact", "Theta_recon DPhi=L Theta_recon holds as an operator identity on overlap 01",
      matrix_equal(theta1_source * D01, L01_source * theta0_symbolic))
check("exact", "Theta_recon DPhi=L Theta_recon holds as an operator identity on overlap 12",
      matrix_equal(theta2_from_1 * D12, L12_source * theta1_independent))
check("exact", "Theta_recon DPhi=L Theta_recon holds directly on overlap 02",
      matrix_equal(theta2_source * D02, L02_source * theta0_symbolic))
check("exact", "the three Theta_recon operator diagrams obey the triple composition",
      matrix_equal(
          theta2_source * D02,
          L12_source.subs(sub_01, simultaneous=True)
          * L01_source * theta0_symbolic,
      ))
gamma2_omitted_hessian = [sp.zeros(4) for _ in range(4)]
theta2_omitted_hessian = theta_matrix(h2_source, gamma2_omitted_hessian)
check("planted", "omitting the nonlinear Hessian term breaks the direct Theta_recon diagram",
      not matrix_equal(theta2_omitted_hessian * D02,
                       L02_source * theta0_symbolic))

S01 = symmetric_representation(B01)
S12 = symmetric_representation(B12)
S02 = symmetric_representation(B02)
check("exact", "Sym2(B) has determinant (det B)^5 in rank four",
      sp.simplify(S01.det() - B01.det() ** 5) == 0
      and sp.simplify(S12.det() - B12.det() ** 5) == 0
      and sp.simplify(S02.det() - B02.det() ** 5) == 0)
forward_total_determinant = sp.simplify(A02.det() * S02.det())
check("exact", "the forward Met(X) Jacobian determinant is (det B)^4=1/1296",
      forward_total_determinant == R(1, 1296)
      and sp.simplify(D02.det()) == forward_total_determinant)
check("planted", "the tempting wrong exponents do not equal the total Jacobian",
      forward_total_determinant != B02.det() ** 5
      and forward_total_determinant != B02.det() ** 6)

x_point = {x[0]: R(1, 2), x[1]: R(-2, 3), x[2]: R(3, 5), x[3]: R(1, 7)}
y_point_values = [sp.simplify(value.subs(x_point)) for value in f01]
z_point_values = [sp.simplify(value.subs(x_point)) for value in f02]
y_point = dict(zip(y, y_point_values))
z_point = dict(zip(z, z_point_values))

P_lorentz = sp.Matrix([
    [1, R(1, 2), 0, 0],
    [0, 1, R(1, 3), 0],
    [0, 0, 1, R(1, 4)],
    [0, 0, 0, 1],
])
h_fixtures = [ETA4, sp.simplify(P_lorentz.T * ETA4 * P_lorentz)]
tangent_fixtures = [
    (
        sp.Matrix([R(2, 5), R(-3, 7), R(5, 11), R(7, 13)]),
        sp.Matrix([R(i + 1, 17) for i in range(10)]),
    ),
    (
        sp.Matrix([R(-4, 9), R(5, 8), R(-6, 13), R(2, 3)]),
        sp.Matrix([R((-1) ** i * (i + 2), 19) for i in range(10)]),
    ),
]

raw_fibre_tangent_differs = False
wrong_sign_connection_fails = False
metric_determinant_checks = []
density_checks = []
for fixture_number, (h_fixture, tangent_fixture) in enumerate(
        zip(h_fixtures, tangent_fixtures), start=1):
    h_substitution = dict(zip(h_symbols, symmetric_components(h_fixture)))
    total_substitution = {**x_point, **h_substitution}
    d02 = sp.simplify(D02.subs(total_substitution))
    tangent0 = sp.Matrix([*tangent_fixture[0], *tangent_fixture[1]])
    tangent2 = sp.simplify(d02 * tangent0)
    v0 = tangent_fixture[0]
    k0 = tangent_fixture[1]
    v2 = tangent2[:4, 0]
    hdot2 = tangent2[4:, 0]
    h2_value = sp.simplify(h2_source.subs(total_substitution))
    b02_value = sp.simplify(B02.subs(z_point))
    s02_value = symmetric_representation(b02_value)
    gamma2_value = [sp.simplify(entry.subs(z_point)) for entry in gamma2_rule]
    contracted2 = gamma_contraction(gamma2_value, v2)
    correction2 = symmetric_components(
        contracted2.T * h2_value + h2_value * contracted2
    )
    kappa2 = sp.simplify(hdot2 - correction2)
    alpha0 = sp.simplify(h_fixture * v0)
    alpha2 = sp.simplify(h2_value * v2)

    check("exact", f"fixture {fixture_number}: the vertical contact component is tensorial",
          matrix_equal(kappa2, s02_value * k0))
    check("exact", f"fixture {fixture_number}: the horizontal covector component is tensorial",
          matrix_equal(alpha2, b02_value.T * alpha0))
    check("exact", f"fixture {fixture_number}: the Theta candidate is invertible at the fibre point",
          sp.simplify(theta_matrix(h_fixture, gamma0).det()) != 0
          and sp.simplify(theta_matrix(h2_value, gamma2_value).det()) != 0)
    raw_expected = s02_value * k0
    raw_fibre_tangent_differs |= not matrix_equal(hdot2, raw_expected)
    wrong_gamma2 = [-entry for entry in gamma2_value]
    wrong_contracted2 = gamma_contraction(wrong_gamma2, v2)
    wrong_kappa2 = sp.simplify(hdot2 - symmetric_components(
        wrong_contracted2.T * h2_value + h2_value * wrong_contracted2
    ))
    wrong_sign_connection_fails |= not matrix_equal(wrong_kappa2, raw_expected)

    gimmel0 = coordinate_gimmel(h_fixture, gamma0)
    gimmel2 = coordinate_gimmel(h2_value, gamma2_value)
    check("exact", f"fixture {fixture_number}: the coordinate gimmel metric descends",
          matrix_equal(d02.T * gimmel2 * d02, gimmel0))
    metric_determinant_checks.append(sp.simplify(
        gimmel2.det() * d02.det() ** 2 - gimmel0.det()
    ) == 0)
    density_checks.append(sp.simplify(
        sp.sqrt(sp.Abs(gimmel2.det())) * sp.Abs(d02.det())
        - sp.sqrt(sp.Abs(gimmel0.det()))
    ) == 0)

check("planted", "raw dh is not tensorial before Christoffel cancellation",
      raw_fibre_tangent_differs)
check("planted", "using the wrong Christoffel sign also destroys nonlinear contact descent",
      wrong_sign_connection_fails)
check("exact", "the metric determinant obeys the squared Jacobian law in both fixtures",
      all(metric_determinant_checks))
check("exact", "the induced absolute density obeys its Jacobian law in both fixtures",
      all(density_checks))
check("type", "atlas descent uses first coordinate jets and contact cancellation uses second coordinate jets; no Euler/PDE order follows", True)


print("\nC. TRACE REVERSAL ON THE CHOSEN WAVE-H (9,5) BRANCH")

D_trace = de_witt_matrix(ETA4, trace_reversed=True)
D_raw = de_witt_matrix(ETA4, trace_reversed=False)

vertical_frame_columns = []
for values in (
    [1 / sp.sqrt(2), -1 / sp.sqrt(2), 0, 0],
    [1 / sp.sqrt(6), 1 / sp.sqrt(6), -2 / sp.sqrt(6), 0],
    [1 / sp.sqrt(12), 1 / sp.sqrt(12), 1 / sp.sqrt(12), 3 / sp.sqrt(12)],
):
    matrix = sp.diag(*values)
    vertical_frame_columns.append(symmetric_components(matrix))
for pair in ((0, 1), (0, 2), (1, 2)):
    matrix = sp.zeros(4)
    matrix[pair] = 1 / sp.sqrt(2)
    matrix[pair[::-1]] = 1 / sp.sqrt(2)
    vertical_frame_columns.append(symmetric_components(matrix))
vertical_frame_columns.append(symmetric_components(ETA4 / 2))
for pair in ((0, 3), (1, 3), (2, 3)):
    matrix = sp.zeros(4)
    matrix[pair] = 1 / sp.sqrt(2)
    matrix[pair[::-1]] = 1 / sp.sqrt(2)
    vertical_frame_columns.append(symmetric_components(matrix))
F_VERTICAL = sp.Matrix.hstack(*vertical_frame_columns)
ETA10 = sp.diag(*((1,) * 6 + (-1,) * 4))

check("exact", "trace reversal changes the vertical signature from (7,3) to (6,4)",
      matrix_equal(F_VERTICAL.T * D_trace * F_VERTICAL, ETA10)
      and sum(1 for value in (F_VERTICAL.T * D_raw * F_VERTICAL).diagonal() if value > 0) == 7
      and sum(1 for value in (F_VERTICAL.T * D_raw * F_VERTICAL).diagonal() if value < 0) == 3)
F0 = block_diag(sp.eye(4), F_VERTICAL)
check("exact", "horizontal (3,1) plus trace-reversed vertical (6,4) is exactly (9,5)",
      matrix_equal(F0.T * block_diag(ETA4, D_trace) * F0, ETA14))
check("planted", "raw Frobenius would give (10,4), not the claimed chimeric real form",
      not matrix_equal(F0.T * block_diag(ETA4, D_raw) * F0, ETA14))
check("type", "source order is V_10 plus H*_4; matrix order H*_4 plus V_10 is an explicit swap", True)
check("type", "the observer metric selecting Gamma remains distinct from an arbitrary tautological h", True)
check("type", "the live rival (7,7) real-form branch is untested and not killed here", True)


print("\nD. ADAPTED FRAMES, A COHERENT SPIN LIFT, AND A PLANTED SIGN INCONSISTENCY")

def e_inverse_rotor(scalar, bivector):
    return wave_h.eadd(wave_h.escale(scalar, wave_h.E_ONE),
                       wave_h.escale(-1, bivector))


def spin_orthogonal(spin, spin_inverse) -> sp.Matrix:
    columns = []
    for index in range(14):
        image = wave_h.ead(spin, wave_h.blade((index,)), spin_inverse)
        if any(mask.bit_count() != 1 for mask in image):
            raise AssertionError("Spin conjugation left grade one")
        columns.append(sp.Matrix([
            sp.simplify(image.get(1 << row, 0)) for row in range(14)
        ]))
    return sp.Matrix.hstack(*columns)


bivector03 = wave_h.blade((0, 3), R(3, 4))
bivector01 = wave_h.blade((0, 1), R(4, 5))
r1 = wave_h.eadd(wave_h.blade((), R(5, 4)), bivector03)
r1_inverse = e_inverse_rotor(R(5, 4), bivector03)
r2 = wave_h.eadd(wave_h.blade((), R(3, 5)), bivector01)
r2_inverse = e_inverse_rotor(R(3, 5), bivector01)
s0 = wave_h.E_ONE
s0_inverse = wave_h.E_ONE
s1 = r1
s1_inverse = r1_inverse
s2 = wave_h.emul(r2, r1)
s2_inverse = wave_h.emul(r1_inverse, r2_inverse)

check("exact", "the two rational rotors have exact Clifford inverses",
      wave_h.eequal(wave_h.emul(r1, r1_inverse), wave_h.E_ONE)
      and wave_h.eequal(wave_h.emul(r2, r2_inverse), wave_h.E_ONE)
      and wave_h.eequal(wave_h.emul(s2, s2_inverse), wave_h.E_ONE))
check("planted", "the two local Spin gauges are genuinely noncommuting",
      not wave_h.eequal(wave_h.emul(r2, r1), wave_h.emul(r1, r2)))

O0 = sp.eye(14)
O1 = spin_orthogonal(s1, s1_inverse)
O2 = spin_orthogonal(s2, s2_inverse)
check("exact", "both Spin gauges cover exact SO(9,5) transformations",
      matrix_equal(O1.T * ETA14 * O1, ETA14)
      and matrix_equal(O2.T * ETA14 * O2, ETA14)
      and sp.simplify(O1.det()) == 1 and sp.simplify(O2.det()) == 1)
check("planted", "the rational Lorentz boost distinguishes vector and dual representations",
      (O1 - O1.inv().T).rank() == 2)

b02_value = sp.simplify(B02.subs(z_point))
b01_value = sp.simplify(B01.subs(y_point))
b12_value = sp.simplify(B12.subs(z_point))
L01 = block_diag(b01_value.T, symmetric_representation(b01_value))
L12 = block_diag(b12_value.T, symmetric_representation(b12_value))
L02 = block_diag(b02_value.T, symmetric_representation(b02_value))
check("exact", "the coindex transition has the same pairwise/triple cocycle",
      matrix_equal(L02, L12 * L01))

h0_value = h_fixtures[1]
h1_value = sp.simplify(b01_value.T * h0_value * b01_value)
h2_value = sp.simplify(b02_value.T * h0_value * b02_value)
C0 = block_diag(h0_value.inv(), de_witt_matrix(h0_value))
C1 = block_diag(h1_value.inv(), de_witt_matrix(h1_value))
C2 = block_diag(h2_value.inv(), de_witt_matrix(h2_value))
frame0 = block_diag(
    P_lorentz.T,
    symmetric_representation(P_lorentz) * F_VERTICAL,
)
frame1 = sp.simplify(L01 * frame0 * O1)
frame2 = sp.simplify(L02 * frame0 * O2)
check("exact", "the three adapted frames are pseudo-orthonormal for the local C metrics",
      matrix_equal(frame0.T * C0 * frame0, ETA14)
      and matrix_equal(frame1.T * C1 * frame1, ETA14)
      and matrix_equal(frame2.T * C2 * frame2, ETA14))

R01 = sp.simplify(O1.inv())
R12 = sp.simplify(O2.inv() * O1)
R02 = sp.simplify(O2.inv())
check("exact", "adapted-frame residuals compose and intertwine coordinate descent",
      matrix_equal(R12 * R01, R02)
      and matrix_equal(L01 * frame0, frame1 * R01)
      and matrix_equal(L12 * frame1, frame2 * R12))

g01 = s1_inverse
g01_inverse = s1
g12 = wave_h.emul(s2_inverse, s1)
g12_inverse = wave_h.emul(s1_inverse, s2)
g02 = s2_inverse
g02_inverse = s2
check("exact", "the selected Spin lifts cover the adapted-frame residuals",
      matrix_equal(spin_orthogonal(g01, g01_inverse), R01)
      and matrix_equal(spin_orthogonal(g12, g12_inverse), R12)
      and matrix_equal(spin_orthogonal(g02, g02_inverse), R02))
check("exact", "the Spin lifts have a positive triple-overlap cocycle",
      wave_h.eequal(wave_h.emul(g12, g01), g02))
bad_g02 = wave_h.escale(-1, g02)
bad_g02_inverse = wave_h.escale(-1, g02_inverse)
check("planted", "a single sign flip is invisible in SO but changes the Spin cocycle to minus one",
      matrix_equal(spin_orthogonal(bad_g02, bad_g02_inverse), R02)
      and wave_h.eequal(
          wave_h.emul(bad_g02_inverse, wave_h.emul(g12, g01)),
          wave_h.escale(-1, wave_h.E_ONE),
      ))


print("\nE. CHOSEN J, RAW SOURCE COVECTOR, AND RIESZ-PORTED RANK-252 FAMILY")

def oneform_leg_transform(index_matrix, spin, spin_inverse, value):
    """Transform the first tensor leg and Clifford coefficient separately."""
    out = {}
    for new_index in range(14):
        coefficient = {}
        for old_index, old_coefficient in value.items():
            weight = index_matrix[new_index, old_index]
            if weight != 0:
                coefficient = wave_h.eadd(
                    coefficient,
                    wave_h.escale(
                        weight,
                        wave_h.ead(spin, old_coefficient, spin_inverse),
                    ),
                )
        if coefficient:
            out[new_index] = coefficient
    return wave_h.of_clean(out)


def raised_leg_spin_transform(spin, spin_inverse, value):
    """Wave-H projector carrier: the first leg is Riesz-raised in C."""
    orthogonal = spin_orthogonal(spin, spin_inverse)
    return oneform_leg_transform(orthogonal, spin, spin_inverse, value)


def raw_covector_spin_transform(spin, spin_inverse, value):
    """Raw C* first leg: use the dual representation O^-T."""
    orthogonal = spin_orthogonal(spin, spin_inverse)
    return oneform_leg_transform(orthogonal.inv().T, spin, spin_inverse, value)


def wrong_vector_index_transform(spin, spin_inverse, value):
    """Planted pre-repair law: incorrectly uses O rather than O^-T."""
    orthogonal = spin_orthogonal(spin, spin_inverse)
    return oneform_leg_transform(orthogonal, spin, spin_inverse, value)


def metric_leg(value, musical: sp.MatrixBase):
    """Apply sharp or flat on the first leg in an adapted orthonormal frame."""
    return oneform_leg_transform(musical, wave_h.E_ONE, wave_h.E_ONE, value)


sharp_eta = lambda value: metric_leg(value, ETA14)
flat_eta = lambda value: metric_leg(value, ETA14)


def associated_raised_projector(spin_from_zero, inverse_to_zero, value):
    pulled = raised_leg_spin_transform(inverse_to_zero, spin_from_zero, value)
    projected = wave_h.fixed_projector(pulled)
    return raised_leg_spin_transform(spin_from_zero, inverse_to_zero, projected)


Uraised01 = lambda value: raised_leg_spin_transform(g01, g01_inverse, value)
Uraised10 = lambda value: raised_leg_spin_transform(g01_inverse, g01, value)
Uraised12 = lambda value: raised_leg_spin_transform(g12, g12_inverse, value)
Uraised21 = lambda value: raised_leg_spin_transform(g12_inverse, g12, value)
Uraised02 = lambda value: raised_leg_spin_transform(g02, g02_inverse, value)
Uraised20 = lambda value: raised_leg_spin_transform(g02_inverse, g02, value)
Uraw01 = lambda value: raw_covector_spin_transform(g01, g01_inverse, value)
Uraw10 = lambda value: raw_covector_spin_transform(g01_inverse, g01, value)
Uraw12 = lambda value: raw_covector_spin_transform(g12, g12_inverse, value)
Uraw21 = lambda value: raw_covector_spin_transform(g12_inverse, g12, value)
Uraw02 = lambda value: raw_covector_spin_transform(g02, g02_inverse, value)
Uraw20 = lambda value: raw_covector_spin_transform(g02_inverse, g02, value)

Psrc_raised_0 = wave_h.fixed_projector
Psrc_raised_1 = lambda value: associated_raised_projector(g01, g01_inverse, value)
Psrc_raised_2 = lambda value: associated_raised_projector(g02, g02_inverse, value)
Psrc_raw_0 = lambda value: flat_eta(Psrc_raised_0(sharp_eta(value)))
Psrc_raw_1 = lambda value: flat_eta(Psrc_raised_1(sharp_eta(value)))
Psrc_raw_2 = lambda value: flat_eta(Psrc_raised_2(sharp_eta(value)))

T_raw_0 = wave_h.t0
T_raised_0 = sharp_eta(T_raw_0)
T_raw_1 = Uraw01(T_raw_0)
T_raw_2 = Uraw02(T_raw_0)

check("exact", "sharp_eta intertwines raw dual and raised vector transport on every overlap",
      wave_h.of_equal(sharp_eta(Uraw01(T_raw_0)), Uraised01(sharp_eta(T_raw_0)))
      and wave_h.of_equal(sharp_eta(Uraw12(T_raw_1)), Uraised12(sharp_eta(T_raw_1)))
      and wave_h.of_equal(sharp_eta(Uraw02(T_raw_0)), Uraised02(sharp_eta(T_raw_0))))
check("exact", "the previously constructed distortion tensor fixture transports directly and sequentially",
      wave_h.of_equal(Uraw12(T_raw_1), T_raw_2))
check("exact", "the raw C* transport is invertible on that tensor fixture",
      wave_h.of_equal(Uraw10(T_raw_1), T_raw_0)
      and wave_h.of_equal(Uraw20(T_raw_2), T_raw_0)
      and wave_h.of_equal(Uraw21(T_raw_2), T_raw_1))
check("exact", "the Riesz-ported raw rank-252 projector family intertwines on both overlaps",
      wave_h.of_equal(Psrc_raw_1(T_raw_1), Uraw01(Psrc_raw_0(T_raw_0)))
      and wave_h.of_equal(Psrc_raw_2(T_raw_2), Uraw12(Psrc_raw_1(T_raw_1)))
      and wave_h.of_equal(Psrc_raw_2(T_raw_2), Uraw02(Psrc_raw_0(T_raw_0))))
check("exact", "all three local raw projectors remain idempotent on the tensor fixture",
      wave_h.of_equal(Psrc_raw_0(Psrc_raw_0(T_raw_0)), Psrc_raw_0(T_raw_0))
      and wave_h.of_equal(Psrc_raw_1(Psrc_raw_1(T_raw_1)), Psrc_raw_1(T_raw_1))
      and wave_h.of_equal(Psrc_raw_2(Psrc_raw_2(T_raw_2)), Psrc_raw_2(T_raw_2)))

kernel_raw_0 = wave_h.of_add(T_raw_0, wave_h.of_scale(-1, Psrc_raw_0(T_raw_0)))
kernel_raw_1 = Uraw01(kernel_raw_0)
kernel_raw_2 = Uraw02(kernel_raw_0)
check("exact", "associated image and representative kernel witnesses share the raw cocycle",
      wave_h.of_equal(Psrc_raw_1(kernel_raw_1), {})
      and wave_h.of_equal(Psrc_raw_2(kernel_raw_2), {})
      and wave_h.of_equal(
          Psrc_raw_2(Uraw12(Psrc_raw_1(T_raw_1))),
          Uraw12(Psrc_raw_1(T_raw_1)),
      ))

rho_commutes = True
public_grade_representatives = []
for grade in range(15):
    representative = wave_h.blade(tuple(range(grade)))
    if grade not in wave_h.NATIVE_GRADES:
        representative = wave_h.escale(sp.I, representative)
    public_grade_representatives.append(representative)
for spin, spin_inverse in ((g01, g01_inverse), (g12, g12_inverse), (g02, g02_inverse)):
    for coefficient in [wave_h.typed_mixed, *public_grade_representatives]:
        rho_commutes &= wave_h.eequal(
            wave_h.rho_j(wave_h.ead(spin, coefficient, spin_inverse)),
            wave_h.ead(spin, wave_h.rho_j(coefficient), spin_inverse),
        )
check("exact", "the selected native Spin cocycle preserves the chosen fixed-frame rho_J",
      rho_commutes)
matrix_fixture = wave_h.matrix_fixture


def element_matrix(value):
    out = matrix_fixture.identity128 * 0
    for mask, coefficient in value.items():
        out = out + float(sp.N(coefficient)) * matrix_fixture.word(wave_h.bits(mask))
    return out


matrix_J_preserved = True
matrix_K_preserved = True
for spin, spin_inverse in ((g01, g01_inverse), (g12, g12_inverse), (g02, g02_inverse)):
    spin_matrix = element_matrix(spin)
    inverse_matrix = element_matrix(spin_inverse)
    matrix_J_preserved &= (
        matrix_fixture.max_abs(
            spin_matrix @ wave_h.J_H @ inverse_matrix.conj() - wave_h.J_H
        ) < matrix_fixture.TOL
    )
    matrix_K_preserved &= (
        matrix_fixture.max_abs(
            spin_matrix.conj().T @ wave_h.K @ spin_matrix - wave_h.K
        ) < matrix_fixture.TOL
    )
check("numeric", "the actual 128x128 chosen J_H and Krein K are preserved by all overlap rotors",
      matrix_J_preserved and matrix_K_preserved)
check("type", "chosen-J native-Spin naturality is not source ownership or full public U(K) invariance", True)
check("type", "T_omega is a tensorial difference of two connections, not itself a connection law", True)
check("type", "sources make A0 Levi-Civita-derived, but which observer/Zorro/Y connection equals it remains UNCERTAIN", True)
check("type", "the source gauge transformation epsilon is not the tautological fibre metric h", True)

bad_T_raw_2 = raw_covector_spin_transform(bad_g02, bad_g02_inverse, T_raw_0)
Psrc_raised_bad_2 = lambda value: associated_raised_projector(
    bad_g02, bad_g02_inverse, value
)
Psrc_raw_bad_2 = lambda value: flat_eta(Psrc_raised_bad_2(sharp_eta(value)))
check("planted", "adjoint source/projector transport alone cannot detect the central Spin sign",
      wave_h.of_equal(bad_T_raw_2, T_raw_2)
      and wave_h.of_equal(
          Psrc_raw_bad_2(bad_T_raw_2),
          Psrc_raw_2(T_raw_2),
      ))

# The local projectors are associated by conjugation. Exercise the identity
# on a basis of the entire 252-dimensional image and representative kernel
# sectors rather than only on the mixed tilted source above.
image_basis_intertwines = True
wrong_vector_law_detected = False
for vertical_five_form in combinations(range(4, 14), 5):
    image_tensor = wave_h.wave_f.j_q(
        {vertical_five_form: Fraction(1)}, Fraction(1), Fraction(1)
    )
    basis_raised = wave_h.oneform_from_tensor(image_tensor)
    basis_raw = flat_eta(basis_raised)
    value1 = Uraw01(basis_raw)
    value2 = Uraw02(basis_raw)
    image_basis_intertwines &= (
        wave_h.of_equal(Psrc_raw_0(basis_raw), basis_raw)
        and wave_h.of_equal(Psrc_raw_1(value1), value1)
        and wave_h.of_equal(Psrc_raw_2(value2), value2)
        and wave_h.of_equal(Uraw12(value1), value2)
    )
    wrong_value1 = wrong_vector_index_transform(g01, g01_inverse, basis_raw)
    wrong_vector_law_detected |= not wave_h.of_equal(
        Psrc_raw_1(wrong_value1),
        wrong_vector_index_transform(
            g01, g01_inverse, Psrc_raw_0(basis_raw)
        ),
    )
check("exact", "all 252 selected image basis vectors intertwine under the associated projector family",
      image_basis_intertwines)
check("planted", "using O instead of O^-T on the raw source one-form leg breaks port naturality",
      wrong_vector_law_detected)

kernel_seeds = [
    {0: wave_h.blade((0, 4, 5), Fraction(2, 3))},
    {1: wave_h.blade(tuple(range(10)), Fraction(3, 7))},
    {2: wave_h.escale(sp.I * R(5, 11), wave_h.blade((1,)))},
    {3: wave_h.blade((0, 1, 2, 3, 4, 5), Fraction(7, 13))},
]
representative_kernels_intertwine = True
for seed in kernel_seeds:
    kernel_seed_raised = wave_h.of_add(
        seed, wave_h.of_scale(-1, Psrc_raised_0(seed))
    )
    kernel_seed = flat_eta(kernel_seed_raised)
    representative_kernels_intertwine &= (
        wave_h.of_equal(Psrc_raw_0(kernel_seed), {})
        and wave_h.of_equal(Psrc_raw_1(Uraw01(kernel_seed)), {})
        and wave_h.of_equal(Psrc_raw_2(Uraw02(kernel_seed)), {})
        and wave_h.of_equal(
            Uraw12(Uraw01(kernel_seed)), Uraw02(kernel_seed)
        )
    )
check("exact", "representative grade-3, grade-10, public-complement, and grade-6 kernel sectors intertwine",
      representative_kernels_intertwine)

L_observe = sp.Matrix([[1], [0]])
R_observe = sp.Matrix([[1, 0]])
E_upstairs = sp.Matrix([[0, 0], [1, 0]])
leakage = (sp.eye(2) - L_observe * R_observe) * E_upstairs * L_observe
check("planted", "exact observation splitting still does not imply equation no-leakage",
      R_observe * L_observe == sp.eye(1)
      and R_observe * E_upstairs * L_observe == sp.zeros(1)
      and leakage != sp.zeros(2, 1))


print("\nF. PRIMARY-SOURCE COLLISION AND CLAIM BOUNDARY")

portal = (ROOT / "lab" / "sources" / "transcripts" /
          "portal-special-gu-first-look-2020-04-02.md").read_text()
toe_2025 = (ROOT / "lab" / "sources" / "transcripts" /
            "toe-weinstein-gu-40-years.md").read_text()
formalization_candidates = (ROOT / "docs" /
                            "paper-formalization-candidates.md").read_text()


def bounded_passage(text: str, start: str, end: str) -> str:
    left = text.index(start)
    right = text.index(end, left)
    return text[left:right + len(end)]


portal_chimeric = bounded_passage(portal, "01:12:17", "01:13:00")
portal_connection = bounded_passage(portal, "01:13:00", "01:13:55")
portal_zorro = bounded_passage(portal, "02:22:27", "02:25:09")
portal_tilted = bounded_passage(portal, "02:25:46", "02:33:43")
toe_trace = bounded_passage(toe_2025, "[00:20:51]", "[00:29:16]")
toe_contraction = bounded_passage(toe_2025, "[01:36:35]", "[01:36:56]")

check("source", "SOURCE-CONFIRMS: Portal types C as vertical ten plus horizontal cotangent four",
      "vertical tangent space of 10 dimensions" in portal_chimeric
      and "cotangent space" in portal_chimeric)
check("source", "SOURCE-CONFIRMS: Portal says the C-to-TY identification depends on a connection",
      "missing exactly the data of a connection" in portal_connection)
check("source", "SOURCE-CONFIRMS: Portal explicitly names the Zorro construction",
      "Mark of Zorro" in portal_zorro
      and "connection on the space" in portal_zorro)
check("source", "SOURCE-CONFIRMS: Portal gives the tilted/two-connection source construction",
      "two separate connections" in portal_tilted
      and "difference of two connections" in portal_tilted
      and "Levi-Civita connection" in portal_tilted)
check("source", "SOURCE-CONFIRMS: the 2025 conversation explicitly restores trace reversal",
      "trace reversed Frobenius inner product" in toe_trace
      and "3,7 metric on the fiber" in toe_trace)
check("source", "SOURCE-CORRECTS: the later conversation distinguishes contraction from projection",
      "projection operator" in toe_contraction
      and "contraction operator" in toe_contraction)
check("source", "SOURCE-SILENT: primary transcripts give no explicit Theta_recon formula",
      "Theta_{Gamma" not in portal + toe_2025
      and "hdot-Gamma" not in portal + toe_2025
      and "Theta_Z" not in formalization_candidates)

check("type", "the result is a local exact three-patch fixture, not a global theorem for arbitrary X", True)
check("type", "Lorentz-section existence, spin-structure existence, and analytic closed domains remain open", True)
check("type", "no source action Euler map, Ward identity, Green current, or physical phase space is claimed", True)
check("type", "the A9F rank-128 imposter hinge is untouched and untested by this rank-252 port wave", True)
check("type", "external-ledger P1/P2/P3 remain unchanged and unused", True)


print("\n" + "=" * 116)
total = sum(COUNTS.values())
print("COUNTS:", ", ".join(f"{kind}={count}" for kind, count in COUNTS.items()),
      f"total={total}")
if FAILURES:
    print("RESOLVER WAVE I VERDICT: FAIL")
    for failure in FAILURES:
        print(" -", failure)
    raise SystemExit(1)
print("RESOLVER WAVE I VERDICT: LOCAL_NONLINEAR_METX_THETA_RECONSTRUCTION_AND_RIESZ_PORTED_SPIN_FIXTURE")
print("A nonlinear three-chart metric-bundle cocycle and connection-induced Theta candidate,")
print("trace-reversed gimmel metric, coherent Spin/chosen-J lift, and Riesz-ported associated")
print("rank-252 projector family pass locally. Global/source ownership, actual source Euler,")
print("Ward/Green/domain, and physical observation no-leakage remain open.")
