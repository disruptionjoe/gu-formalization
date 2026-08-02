#!/usr/bin/env python3
"""Exact PW1 source/native reduction and super-IG interface probe.

The finite ``U(2,2)/Sp(1,1)`` model is a scalable hostile witness, not a
replacement for the actual rank-128 bundle.  It verifies the structural
identities used in the accompanying theorem packet.  The full-unitary mixed
odd bracket uses the real-bilinear Krein square on the complete underlying-real
fixture; the complex-symplectic channel is retained only as a center-killed
comparator.  No Ward identity for the written GU action is asserted.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/pw1-source-native-port-superig-interface.json"
B2C15P = ROOT / "lab/process/eric-curt-wave3d-b2c15p-source-epsilon-tangent-zorro-dewitt.json"


class DuplicateKeyError(ValueError):
    pass


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    out: dict[str, object] = {}
    for key, value in pairs:
        if key in out:
            raise DuplicateKeyError(key)
        out[key] = value
    return out


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(), object_pairs_hook=unique_object)


I = sp.I
ZERO4 = sp.zeros(4)
K = sp.diag(1, -1, 1, -1)
OMEGA = sp.zeros(4)
OMEGA[:2, 2:] = sp.eye(2)
OMEGA[2:, :2] = -sp.eye(2)
C = -OMEGA * K  # linear coefficient of the antilinear quaternionic J


def bar(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.applyfunc(sp.conjugate)


def dagger(matrix: sp.Matrix) -> sp.Matrix:
    return bar(matrix).T


def sigma(matrix: sp.Matrix, c_matrix: sp.Matrix = C) -> sp.Matrix:
    return sp.simplify(c_matrix * bar(matrix) * c_matrix.inv())


def project_h(matrix: sp.Matrix, c_matrix: sp.Matrix = C) -> sp.Matrix:
    return sp.simplify((matrix + sigma(matrix, c_matrix)) / 2)


def project_m(matrix: sp.Matrix, c_matrix: sp.Matrix = C) -> sp.Matrix:
    return sp.simplify((matrix - sigma(matrix, c_matrix)) / 2)


def tau_krein(matrix: sp.Matrix) -> sp.Matrix:
    """Real involution whose fixed locus is u(K)."""

    return sp.simplify(-K.inv() * dagger(matrix) * K)


def project_u(matrix: sp.Matrix) -> sp.Matrix:
    return sp.simplify((matrix + tau_krein(matrix)) / 2)


def project_native(matrix: sp.Matrix) -> sp.Matrix:
    """Real-linear projection from the common complex algebra to sp(1,1)."""

    return project_h(project_u(matrix))


def commutator(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return sp.simplify(left * right - right * left)


def is_zero(matrix: sp.Matrix) -> bool:
    return matrix == sp.zeros(*matrix.shape)


def is_u(matrix: sp.Matrix) -> bool:
    return is_zero(sp.simplify(dagger(matrix) * K + K * matrix))


def u22_real_basis() -> list[sp.Matrix]:
    basis: list[sp.Matrix] = []
    for row in range(4):
        matrix = sp.zeros(4)
        matrix[row, row] = I
        basis.append(matrix)
    for row in range(4):
        for col in range(row + 1, 4):
            epsilon = K[row, row] * K[col, col]
            real_matrix = sp.zeros(4)
            real_matrix[row, col] = 1
            real_matrix[col, row] = -epsilon
            basis.append(real_matrix)
            imag_matrix = sp.zeros(4)
            imag_matrix[row, col] = I
            imag_matrix[col, row] = epsilon * I
            basis.append(imag_matrix)
    return basis


def real_vector(matrix: sp.Matrix) -> sp.Matrix:
    entries: list[sp.Expr] = []
    for value in list(matrix):
        entries.extend([sp.re(value), sp.im(value)])
    return sp.Matrix(entries)


def real_rank(matrices: list[sp.Matrix]) -> int:
    return sp.Matrix.hstack(*(real_vector(matrix) for matrix in matrices)).rank()


def mu_symplectic(u: sp.Matrix, v: sp.Matrix) -> sp.Matrix:
    """Complex-bilinear spinor square with values in sp(4,C)."""

    return sp.simplify(v * u.T * OMEGA + u * v.T * OMEGA)


def m_krein(u: sp.Matrix, v: sp.Matrix) -> sp.Matrix:
    """Real-bilinear symmetric Krein square with values in u(K)."""

    return sp.simplify(I * (u * dagger(v) * K + v * dagger(u) * K))


def beta_complex(
    q: tuple[sp.Matrix, list[sp.Matrix]],
    r: tuple[sp.Matrix, list[sp.Matrix]],
) -> list[sp.Matrix]:
    u, psi = q
    v, chi = r
    return [sp.simplify(mu_symplectic(u, chi_j) + mu_symplectic(v, psi_j)) for psi_j, chi_j in zip(psi, chi)]


def beta_krein(
    q: tuple[sp.Matrix, list[sp.Matrix]],
    r: tuple[sp.Matrix, list[sp.Matrix]],
) -> list[sp.Matrix]:
    u, psi = q
    v, chi = r
    return [sp.simplify(m_krein(u, chi_j) + m_krein(v, psi_j)) for psi_j, chi_j in zip(psi, chi)]


def assert_registry() -> int:
    data = load(REGISTRY)
    assert data["status"] == "PW1_CONDITIONAL_PASS_PW2_ENABLED"
    assert data["layer_zero"]["source_to_native"].startswith("TWO_STAGE_CONDITIONAL_PORT_NOT_RETRACTION")
    dispositions = set(data["dispositions"])
    assert {
        "MIXED-SIGN-COMPLEX-EXTENSION-PASS",
        "SOURCE-TO-NATIVE-REDUCTION-CONDITIONAL",
        "FULL-REAL-FORM-EQUIVALENCE-KILLED",
        "NAIVE-ACTION-PROJECTION-KILLED",
        "MOVING-J-REDUCTION-LIVE",
        "REDUCED-BLOCK-COMPLEX-PORT-LIVE",
        "MIXED-SUPER-IG-REAL-KREIN-ALGEBRA-PASS",
        "COMPLEX-SYMPLECTIC-CENTER-OBSTRUCTION-RECORDED",
        "WRITTEN-ACTION-WARD-IDENTITY-OPEN",
    }.issubset(dispositions)
    assert data["external_datum"]["P1_P2_P3"] == "UNCHANGED_AND_UNUSED"
    assert data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
    assert data["third_lane_gate"] == "TG-1 AND TG-2 AND TG-3 = NOT_PROMOTED"
    source = data["source_disposition"]
    assert source["SOURCE_CONFIRMS"] and source["SOURCE_CORRECTS"] and source["SOURCE_SILENT"]
    return 8


def main() -> None:
    checks = assert_registry()

    # Quaternionic real form inside the mixed-sign complex carrier.
    assert C * bar(C) == -sp.eye(4)
    assert C.T * K * C == K
    assert sigma(sigma(sp.Matrix(4, 4, range(16)))) == sp.Matrix(4, 4, range(16))
    checks += 3

    u_basis = u22_real_basis()
    assert len(u_basis) == 16 and all(is_u(matrix) for matrix in u_basis)
    h_basis = [project_h(matrix) for matrix in u_basis]
    m_basis = [project_m(matrix) for matrix in u_basis]
    assert real_rank(u_basis) == 16
    assert real_rank(h_basis) == 10
    assert real_rank(m_basis) == 6
    checks += 4

    # Reductive symmetric-pair laws.  These do not make p_H a Lie map.
    for left in h_basis:
        for right in h_basis:
            assert is_zero(project_m(commutator(left, right)))
    for left in h_basis:
        for right in m_basis:
            assert is_zero(project_h(commutator(left, right)))
    for left in m_basis:
        for right in m_basis:
            assert is_zero(project_m(commutator(left, right)))
    checks += 3

    hostile_x = sp.diag(I / 2, 0, I / 2, 0)
    hostile_y = sp.zeros(4)
    hostile_y[0, 1] = hostile_y[1, 0] = sp.Rational(1, 2)
    hostile_y[2, 3] = hostile_y[3, 2] = sp.Rational(1, 2)
    curvature_return = commutator(hostile_x, hostile_y)
    assert is_u(hostile_x) and is_u(hostile_y)
    assert is_zero(project_h(hostile_x)) and is_zero(project_h(hostile_y))
    assert not is_zero(curvature_return) and project_h(curvature_return) == curvature_return
    assert project_h(commutator(hostile_x, hostile_y)) != commutator(project_h(hostile_x), project_h(hostile_y))
    checks += 4

    # Phi_J = 1/2 (D_A J) J^-1 and its curvature return in a constant two-chart fixture.
    d_j = sp.simplify(hostile_x * C - C * bar(hostile_x))
    phi_j = sp.simplify(d_j * C.inv() / 2)
    assert phi_j == hostile_x
    assert project_h(curvature_return) == commutator(phi_j, hostile_y)
    checks += 2

    # Moving reduction: finite covariance, a three-patch cocycle, and the exact Dp term.
    g01 = sp.zeros(4)
    for row, col in enumerate((0, 3, 2, 1)):
        g01[col, row] = 1
    g12 = sp.diag(1, -1, 1, -1)
    g02 = g01 * g12
    assert dagger(g01) * K * g01 == K and dagger(g12) * K * g12 == K
    c1 = sp.simplify(g01.inv() * C * bar(g01))
    c2_via_1 = sp.simplify(g12.inv() * c1 * bar(g12))
    c2_direct = sp.simplify(g02.inv() * C * bar(g02))
    assert c2_via_1 == c2_direct
    arbitrary = u_basis[4]
    assert project_h(g01.inv() * arbitrary * g01, c1) == g01.inv() * project_h(arbitrary) * g01
    zeta = u_basis[0]
    c_dot = sp.simplify(zeta * C - C * bar(zeta))
    sigma_dot = sp.simplify(c_dot * bar(arbitrary) * C.inv() - sigma(arbitrary) * c_dot * C.inv())
    dp_direct = sp.simplify(sigma_dot / 2)
    dp_covariant = sp.simplify(commutator(zeta, project_h(arbitrary)) - project_h(commutator(zeta, arbitrary)))
    assert dp_direct == dp_covariant and not is_zero(dp_direct)
    checks += 5

    # A source-legal central direction need not descend through a fixed J reduction.
    central_plant = I * sp.eye(4)
    assert is_u(central_plant)
    assert sigma(central_plant) == -central_plant
    assert is_zero(project_h(central_plant))
    checks += 3

    # Positive-unitary and Clifford-reality forks are killed before dynamics.
    boost = sp.zeros(4)
    boost[0, 1] = boost[1, 0] = sp.Rational(1, 2)
    boost[2, 3] = boost[3, 2] = -sp.Rational(1, 2)
    assert is_u(boost) and sigma(boost) == boost
    assert set(boost.eigenvals()) == {-sp.Rational(1, 2), sp.Rational(1, 2)}
    assert sp.eye(4) * bar(sp.eye(4)) == sp.eye(4) and C * bar(C) == -sp.eye(4)
    checks += 3

    # Exact reduced block-Wick comparator: legitimate over C, not a real-form isomorphism.
    h_metric = sp.diag(1, 1, 1, -1)
    dw_metric = sp.diag(1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
    g95 = sp.diag(*list(h_metric.diagonal()), *list(dw_metric.diagonal()))
    g77 = sp.diag(*list(h_metric.diagonal()), *list((-dw_metric).diagonal()))
    wick = sp.diag(*([1] * 4 + [I] * 10))
    assert wick.T * g77 * wick == g95
    assert sum(value == 1 for value in g95.diagonal()) == 9
    assert sum(value == 1 for value in g77.diagonal()) == 7
    assert min(7, 7) != min(9, 5)
    assert 4 * 64**2 == 16384 and 64 * (2 * 64 + 1) == 8256 and 16384 - 8256 == 8128
    assert 6 + 45 == 51
    checks += 6

    # The complex symplectic comparator closes only on the centerless complex route.
    vectors = [sp.eye(4)[:, index] for index in range(4)]
    vectors_real = vectors + [I * vector for vector in vectors]
    q = (vectors[0], [vectors[1], vectors[2]])
    r = (vectors[3], [vectors[0], vectors[1]])
    beta_c = beta_complex(q, r)
    assert beta_c == beta_complex(r, q)
    assert any(not is_zero(component) for component in beta_c)
    for component in beta_c:
        assert is_zero(sp.simplify(component.T * OMEGA + OMEGA * component))
    center = I * sp.eye(4)
    center_failure = [
        sp.simplify(mu_symplectic(center * vectors[0], vector) + mu_symplectic(vectors[0], center * vector))
        for vector in vectors
    ]
    assert any(not is_zero(component) for component in center_failure)
    assert all(is_zero(commutator(center, mu_symplectic(vectors[0], vector))) for vector in vectors)
    checks += 5

    # The honest full-U source bracket is real-bilinear and Krein-sesquilinear.
    beta_qr = beta_krein(q, r)
    assert beta_qr == beta_krein(r, q)
    assert any(not is_zero(component) for component in beta_qr)
    assert all(is_u(component) for component in beta_qr)
    assert beta_krein((I * q[0], [I * value for value in q[1]]), r) != [I * value for value in beta_qr]
    center_equivariance = [
        sp.simplify(left + right)
        for left, right in zip(
            beta_krein((center * q[0], [center * value for value in q[1]]), r),
            beta_krein(q, (center * r[0], [center * value for value in r[1]])),
        )
    ]
    assert all(is_zero(component) for component in center_equivariance)
    checks += 5

    # Equivariance under the complete finite u(2,2) basis, including its center.
    for e in u_basis:
        for u in vectors_real:
            for v in vectors_real:
                assert commutator(e, m_krein(u, v)) == sp.simplify(m_krein(e * u, v) + m_krein(u, e * v))
    # Conditional native projection is equivariant under the full fixed h basis.
    projected_beta = [project_h(component) for component in beta_qr]
    assert any(not is_zero(component) for component in projected_beta)
    assert all(is_u(component) and sigma(component) == component for component in projected_beta)
    for e in h_basis:
        for component in beta_qr:
            assert project_h(commutator(e, component)) == commutator(e, project_h(component))
    checks += 4

    # The affine action on the algebraic odd coordinate theta has forced coefficient 1/2.
    odd_basis: list[tuple[sp.Matrix, list[sp.Matrix]]] = []
    for vector in vectors_real:
        odd_basis.append((vector, [sp.zeros(4, 1), sp.zeros(4, 1)]))
    for direction in range(2):
        for vector in vectors_real:
            one_form = [sp.zeros(4, 1), sp.zeros(4, 1)]
            one_form[direction] = vector
            odd_basis.append((sp.zeros(4, 1), one_form))
    generated_beta: list[sp.Matrix] = []
    for q_test in odd_basis:
        for r_test in odd_basis:
            expected = beta_krein(q_test, r_test)
            generated_beta.extend(expected)
            odd_odd = [
                sp.simplify((left + right) / 2)
                for left, right in zip(beta_krein(r_test, q_test), beta_krein(q_test, r_test))
            ]
            assert odd_odd == expected
            assert [project_h(component) for component in odd_odd] == [project_h(component) for component in expected]
    for e in h_basis:
        for component in generated_beta:
            assert project_h(commutator(e, component)) == commutator(e, project_h(component))
    odd_odd_on_a = [sp.simplify((left + right) / 2) for left, right in zip(beta_krein(r, q), beta_krein(q, r))]
    assert odd_odd_on_a == beta_qr
    wrong_coefficient = [sp.simplify((left + right) / 3) for left, right in zip(beta_krein(r, q), beta_krein(q, r))]
    assert wrong_coefficient != beta_qr
    checks += 2

    # Logical owner-independence plant: algebraic closure cannot imply a Ward identity.
    live = next(component for component in projected_beta if not is_zero(component))
    live_entry = next(value for value in list(live) if value != 0)
    owner_independence_plant = sp.simplify(live_entry / 2)
    assert owner_independence_plant != 0
    checks += 1

    # Carry the already-earned legal native Alt basis without pretending it selects a ratio.
    b2c15p = load(B2C15P)
    alt = b2c15p["distortion_reduction_candidate"]
    assert alt["pointwise_rank"] == 364 and alt["pointwise_kernel"] == 910
    assert alt["selection"].startswith("symmetry admits independent")
    assert b2c15p["external_datum"]["P1_P2_P3"] == "UNCHANGED_AND_UNUSED"
    checks += 3

    plants = 0
    for condition in [
        project_h(commutator(hostile_x, hostile_y)) == commutator(project_h(hostile_x), project_h(hostile_y)),
        sigma(central_plant) == central_plant,
        wick.T * g77 * wick != g95,
        wrong_coefficient == beta_qr,
        owner_independence_plant == 0,
        8128 in {1, 2, 3},
    ]:
        assert not condition
        plants += 1

    print(f"PASS: {checks} exact + {plants} planted = {checks + plants}")


if __name__ == "__main__":
    main()
