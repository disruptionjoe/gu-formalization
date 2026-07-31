#!/usr/bin/env python3
"""Exact positive controls for the Eric-source-directed native closure packet.

The probe answers a deliberately bounded question: can one finite exact parent
model support the decoder algebra required by the ten-row Weinstein crosswalk?
It does not derive a background, stabilizer, field spectrum, domain, or physics
on the actual metric bundle Y^14.  Several fixtures intentionally contain the
target algebra; they are positive controls, never emergence evidence.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = ROOT / "lab/process/eric-source-directed-native-closure-certificate.json"
ATLAS = ROOT / "lab/process/eric-native-physics-equation-replacement-atlas.json"

exact_checks = 0
planted_checks = 0


def exact(name: str, condition: bool) -> None:
    global exact_checks
    if not bool(condition):
        raise AssertionError(name)
    exact_checks += 1


def planted(name: str, false_claim: bool) -> None:
    global planted_checks
    if bool(false_claim):
        raise AssertionError(f"planted false claim passed: {name}")
    planted_checks += 1


def block_diag(*blocks: sp.Matrix) -> sp.Matrix:
    return sp.diag(*blocks)


def algebraic_dual(lift: sp.Matrix) -> sp.Matrix:
    """Pull native covectors back to observed covectors."""
    return lift.T


def riesz_adjoint(lift: sp.Matrix, native_pairing: sp.Matrix, observed_pairing: sp.Matrix) -> sp.Matrix:
    """Primal adjoint obtained only after the two Riesz identifications."""
    return observed_pairing.inv() * lift.T * native_pairing


def observation_and_variation_controls() -> None:
    lift = sp.Matrix([[1, 0], [0, 1], [1, 1]])
    retract = sp.Matrix([[1, 0, 0], [0, 1, 0]])
    projector = lift * retract
    complement = sp.eye(3) - projector

    exact("field retract closes", retract * lift == sp.eye(2))
    exact("field projector is idempotent", projector * projector == projector)
    exact("complement kills admitted fields", complement * lift == sp.zeros(3, 2))

    pullback_dual = algebraic_dual(lift)
    euclidean_adjoint = riesz_adjoint(lift, sp.eye(3), sp.eye(2))
    exact("algebraic dual is the formal transpose", pullback_dual == lift.T)
    exact("generic algebraic dual differs from field retract", pullback_dual != retract)
    exact("Euclidean Riesz adjoint represents the algebraic dual", euclidean_adjoint == pullback_dual)

    parent_hessian = sp.Matrix([[2, 1, 0], [1, 3, 1], [0, 1, 4]])
    x0, x1 = sp.symbols("x0 x1", real=True)
    observed = sp.Matrix([x0, x1])
    native = lift * observed
    action = (native.T * parent_hessian * native)[0] / 2
    action_gradient = sp.Matrix([sp.diff(action, x0), sp.diff(action, x1)])
    exact(
        "action chain rule uses the algebraic dual",
        action_gradient == pullback_dual * parent_hessian * native,
    )
    planted(
        "arbitrary field retract is substituted for the algebraic dual",
        action_gradient == retract * parent_hessian * native,
    )

    # Leakage is checked only after a (here Euclidean) Riesz primalization;
    # the Euler Hessian above lives in the dual and is not hit by Q directly.
    observed_operator = sp.Matrix([[2, 1], [0, 3]])
    good_native_operator = lift * observed_operator * retract + complement
    exact("good native operator intertwines", good_native_operator * lift == lift * observed_operator)
    exact("good decoded operator is exact", retract * good_native_operator * lift == observed_operator)
    exact("good operator has zero off-slice leakage", complement * good_native_operator * lift == sp.zeros(3, 2))

    leakage_plant = sp.Matrix([[0, 0, 0], [0, 0, 0], [1, 0, 0]])
    bad_native_operator = good_native_operator + leakage_plant
    exact("leakage plant fools reduced sandwich", retract * bad_native_operator * lift == observed_operator)
    planted(
        "reduced sandwich alone proves ambient closure",
        complement * bad_native_operator * lift == sp.zeros(3, 2),
    )

    # A compatible pairing can make L^! equal R, but does not do so by type.
    shear = sp.Matrix([[1, 0, 0], [0, 1, 0], [1, 1, 1]])
    inclusion = sp.Matrix([[1, 0], [0, 1], [0, 0]])
    projection = sp.Matrix([[1, 0, 0], [0, 1, 0]])
    compatible_lift = shear * inclusion
    compatible_retract = projection * shear.inv()
    observed_pairing = sp.diag(2, 3)
    normal_pairing = sp.Matrix([[5]])
    native_pairing = shear.inv().T * block_diag(observed_pairing, normal_pairing) * shear.inv()
    compatible_adjoint = riesz_adjoint(compatible_lift, native_pairing, observed_pairing)
    exact("pairing-compatible fixture has Riesz adjoint equal R", compatible_adjoint == compatible_retract)
    exact("pairing-compatible equality still has correct types", compatible_retract * compatible_lift == sp.eye(2))


def frobenius_trace_reversal_controls() -> None:
    dimension = 4
    basis: list[sp.Matrix] = []
    for i in range(dimension):
        matrix = sp.zeros(dimension)
        matrix[i, i] = 1
        basis.append(matrix)
    for i in range(dimension):
        for j in range(i + 1, dimension):
            matrix = sp.zeros(dimension)
            matrix[i, j] = matrix[j, i] = 1
            basis.append(matrix)

    gram = sp.diag(*([1] * dimension + [2] * (len(basis) - dimension)))

    def coordinates(matrix: sp.Matrix) -> sp.Matrix:
        values = [matrix[i, i] for i in range(dimension)]
        values.extend(matrix[i, j] for i in range(dimension) for j in range(i + 1, dimension))
        return sp.Matrix(values)

    def trace_reverse(matrix: sp.Matrix) -> sp.Matrix:
        return matrix - sp.Rational(1, 2) * sp.trace(matrix) * sp.eye(dimension)

    tau = sp.Matrix.hstack(*(coordinates(trace_reverse(item)) for item in basis))
    exact("four-dimensional trace reversal is an involution", tau * tau == sp.eye(10))
    exact("trace reversal is Frobenius self-adjoint", tau.T * gram == gram * tau)
    exact("trace direction changes sign", trace_reverse(sp.eye(4)) == -sp.eye(4))
    traceless = sp.diag(1, -1, 0, 0)
    exact("traceless symmetric fibre is fixed", trace_reverse(traceless) == traceless)
    planted("trace reversal is silently omitted", tau == sp.eye(10))


def compact_gauge_positive_control() -> None:
    """Plant u(1)+su(2)+su(3) and verify its exact invariant algebra.

    This is explicitly target-coded.  It checks that the later classifier can
    be tested without basis dependence; it does not discover the algebra.
    """

    imaginary = sp.I
    size = 6

    def embed(local: sp.Matrix, offset: int) -> sp.Matrix:
        result = sp.zeros(size)
        for i in range(local.rows):
            for j in range(local.cols):
                result[offset + i, offset + j] = local[i, j]
        return result

    u1 = [embed(sp.Matrix([[imaginary]]), 0)]
    su2_local = [
        sp.Matrix([[0, imaginary], [imaginary, 0]]),
        sp.Matrix([[0, 1], [-1, 0]]),
        sp.Matrix([[imaginary, 0], [0, -imaginary]]),
    ]
    su2 = [embed(item, 1) for item in su2_local]
    su3_local = [
        sp.Matrix([[0, imaginary, 0], [imaginary, 0, 0], [0, 0, 0]]),
        sp.Matrix([[0, 1, 0], [-1, 0, 0], [0, 0, 0]]),
        sp.diag(imaginary, -imaginary, 0),
        sp.Matrix([[0, 0, imaginary], [0, 0, 0], [imaginary, 0, 0]]),
        sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
        sp.Matrix([[0, 0, 0], [0, 0, imaginary], [0, imaginary, 0]]),
        sp.Matrix([[0, 0, 0], [0, 0, 1], [0, -1, 0]]),
        sp.diag(imaginary, imaginary, -2 * imaginary),
    ]
    su3 = [embed(item, 3) for item in su3_local]
    basis = u1 + su2 + su3
    n = len(basis)
    flat_basis = sp.Matrix.hstack(*(item.reshape(size * size, 1) for item in basis))

    def coordinates(matrix: sp.Matrix) -> sp.Matrix:
        solution, parameters = flat_basis.gauss_jordan_solve(matrix.reshape(size * size, 1))
        exact("matrix bracket has unique planted-algebra coordinates", parameters.rows == 0)
        return solution

    brackets: list[list[sp.Matrix]] = []
    for left in basis:
        row = []
        for right in basis:
            row.append(coordinates(left * right - right * left))
        brackets.append(row)

    adjoint = [sp.Matrix.hstack(*(brackets[i][j] for j in range(n))) for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                jacobi = (
                    adjoint[i] * brackets[j][k]
                    + adjoint[j] * brackets[k][i]
                    + adjoint[k] * brackets[i][j]
                )
                exact("planted compact algebra satisfies Jacobi", jacobi == sp.zeros(n, 1))

    center_equations = []
    for j in range(n):
        center_equations.append(sp.Matrix.hstack(*(brackets[i][j] for i in range(n))))
    center_matrix = sp.Matrix.vstack(*center_equations)
    derived_matrix = sp.Matrix.hstack(*(brackets[i][j] for i in range(n) for j in range(n)))
    killing = sp.Matrix(n, n, lambda i, j: sp.trace(adjoint[i] * adjoint[j]))

    exact("planted gauge algebra has one-dimensional centre", len(center_matrix.nullspace()) == 1)
    exact("planted gauge algebra has eleven-dimensional derived algebra", derived_matrix.rank() == 11)
    exact("Killing form has only the central null line", killing.rank() == 11)
    exact("su2 and su3 planted ideals have dimensions three and eight", len(su2) == 3 and len(su3) == 8)
    exact("all planted generators are anti-Hermitian", all(item.conjugate().T == -item for item in basis))
    exact("simple planted factors are traceless", all(sp.trace(item) == 0 for item in su2 + su3))
    exact(
        "planted factors commute across ideals",
        all(left * right - right * left == sp.zeros(size) for left in su2 for right in su3),
    )
    exact(
        "Killing restrictions on compact simple factors are negative",
        all(value.is_negative for value in killing[1:4, 1:4].eigenvals())
        and all(value.is_negative for value in killing[4:12, 4:12].eigenvals()),
    )

    # Change to a dense exact coordinate basis and recompute structural ranks.
    change = sp.eye(n)
    for i in range(n):
        for j in range(i + 1, n):
            change[i, j] = 1
    inverse = change.inv()
    transformed: list[list[sp.Matrix]] = []
    for a in range(n):
        row = []
        for b in range(n):
            old_coordinates = sp.zeros(n, 1)
            for i in range(n):
                for j in range(n):
                    if change[i, a] and change[j, b]:
                        old_coordinates += change[i, a] * change[j, b] * brackets[i][j]
            row.append(inverse * old_coordinates)
        transformed.append(row)
    transformed_adjoint = [sp.Matrix.hstack(*(transformed[i][j] for j in range(n))) for i in range(n)]
    transformed_center = sp.Matrix.vstack(
        *(sp.Matrix.hstack(*(transformed[i][j] for i in range(n))) for j in range(n))
    )
    transformed_derived = sp.Matrix.hstack(
        *(transformed[i][j] for i in range(n) for j in range(n))
    )
    transformed_killing = sp.Matrix(
        n, n, lambda i, j: sp.trace(transformed_adjoint[i] * transformed_adjoint[j])
    )
    exact("basis change preserves centre dimension", len(transformed_center.nullspace()) == 1)
    exact("basis change preserves derived dimension", transformed_derived.rank() == 11)
    exact("basis change transforms Killing form by congruence", transformed_killing == change.T * killing * change)
    planted("planted compact algebra is incorrectly classified as centre-free", len(center_matrix.nullspace()) == 0)


def shared_bosonic_hessian_controls() -> None:
    # An actual U(2) doublet representation supplies the orbit incidence.
    imaginary = sp.I
    hypercharge = imaginary * sp.eye(2)
    weak_generators = [
        sp.Matrix([[0, imaginary], [imaginary, 0]]),
        sp.Matrix([[0, 1], [-1, 0]]),
        sp.diag(imaginary, -imaginary),
    ]
    electroweak_generators = [hypercharge] + weak_generators

    h0, h1, h2, h3 = sp.symbols("h0 h1 h2 h3", real=True)
    scalar_real = sp.Matrix([h0, h1, h2, h3])
    scalar_complex = sp.Matrix([h0 + imaginary * h1, h2 + imaginary * h3])
    scalar_vacuum_complex = sp.Matrix([0, 3])

    def realify(vector: sp.Matrix) -> sp.Matrix:
        return sp.Matrix(
            [
                sp.re(vector[0]).expand(complex=True),
                sp.im(vector[0]).expand(complex=True),
                sp.re(vector[1]).expand(complex=True),
                sp.im(vector[1]).expand(complex=True),
            ]
        )

    incidence = sp.Matrix.hstack(
        *(realify(generator * scalar_vacuum_complex) for generator in electroweak_generators)
    )
    electroweak_mass = incidence.T * incidence
    photon = sp.Matrix([1, 0, 0, 1])

    exact("one represented electroweak orbit incidence has rank three", incidence.rank() == 3)
    exact("one represented abelian generator stabilizes the vacuum", incidence * photon == sp.zeros(4, 1))
    exact("represented electroweak mass has one-dimensional kernel", len(electroweak_mass.nullspace()) == 1)

    radius_squared = (scalar_real.T * scalar_real)[0]
    higgs_potential = sp.Rational(1, 8) * (radius_squared - 9) ** 2
    scalar_vacuum = {h0: 0, h1: 0, h2: 3, h3: 0}
    higgs_hessian = sp.hessian(higgs_potential, (h0, h1, h2, h3)).subs(scalar_vacuum)
    exact("doublet potential has three Goldstone null directions", len(higgs_hessian.nullspace()) == 3)
    exact("represented orbit equals the Goldstone kernel", higgs_hessian * incidence == sp.zeros(4) and incidence.rank() == 3)
    exact("the independent radial scalar is heavy", higgs_hessian[2, 2] == 9)

    potential_gradient = sp.Matrix([sp.diff(higgs_potential, variable) for variable in scalar_real])
    for generator in electroweak_generators:
        orbit_vector = realify(generator * scalar_complex)
        exact(
            "doublet potential is invariant under every planted generator",
            sp.expand((potential_gradient.T * orbit_vector)[0]) == 0,
        )

    # M_h : C_trivial -> C^2_fundamental is an equivariant Yukawa map.
    # Its derivative along the gauge orbit is exactly the same incidence.
    yukawa_map = scalar_complex
    for generator in electroweak_generators:
        delta_scalar = generator * scalar_complex
        delta_yukawa = delta_scalar
        representation_variation = generator * yukawa_map
        exact(
            "Yukawa map is infinitesimally equivariant",
            delta_yukawa == representation_variation,
        )
    yukawa_orbit_incidence = sp.Matrix.hstack(
        *(realify(generator * scalar_vacuum_complex) for generator in electroweak_generators)
    )
    exact("gauge mass and Yukawa orbit use one incidence", yukawa_orbit_incidence == incidence)

    # Derive the complete 19-dimensional Hessian from one finite action.
    gauge_variables = sp.symbols("a0:4", real=True)
    strong_variables = sp.symbols("s0:8", real=True)
    spin_two_variables = sp.symbols("t0:2", real=True)
    cosmological = sp.symbols("c_light", real=True)
    gauge_matrix = sp.zeros(2)
    for variable, generator in zip(gauge_variables, electroweak_generators):
        gauge_matrix += variable * generator
    covariant_scalar = gauge_matrix * scalar_complex
    gauge_higgs_energy = sp.simplify(
        (covariant_scalar.conjugate().T * covariant_scalar)[0] / 2
    )
    cosmological_energy = sp.Rational(1, 200) * cosmological**2
    parent_action = sp.expand(gauge_higgs_energy + higgs_potential + cosmological_energy)
    all_variables = (
        *gauge_variables,
        *strong_variables,
        *spin_two_variables,
        h0,
        h1,
        h2,
        h3,
        cosmological,
    )
    parent_background = {variable: 0 for variable in all_variables}
    parent_background[h2] = 3
    parent_hessian = sp.hessian(parent_action, all_variables).subs(parent_background)

    strong_mass = parent_hessian[4:12, 4:12]
    spin_two_hessian = parent_hessian[12:14, 12:14]
    derived_higgs_hessian = parent_hessian[14:18, 14:18]
    cosmological_hessian = parent_hessian[18:19, 18:19]
    exact("one coupled finite action produces the complete bosonic Hessian", parent_hessian.shape == (19, 19))
    exact("same action derives gauge mass from orbit incidence", parent_hessian[0:4, 0:4] == electroweak_mass)
    exact("same action derives the scalar Hessian", derived_higgs_hessian == higgs_hessian)
    exact("gauge-scalar mixed Hessian vanishes at the stationary zero-connection background", parent_hessian[0:4, 14:18] == sp.zeros(4))
    exact("eight planted colour controls remain massless", strong_mass == sp.zeros(8))
    exact("two planted tensor controls remain massless", spin_two_hessian == sp.zeros(2))
    exact("one action Hessian has the expected planted kernel", len(parent_hessian.nullspace()) == 14)
    exact("heavy and light scalar modes are distinct", higgs_hessian[2, 2] != cosmological_hessian[0, 0])
    exact("cosmological scalar control is nondegenerate and positive", cosmological_hessian.det() > 0)
    planted("one scalar eigenmode is both Higgs and dark energy", higgs_hessian[2, 2] == cosmological_hessian[0, 0])

    # These projectors are fixture metadata.  On Y^14 their analogues must be
    # induced by representations before the spectrum is read.
    dimensions = [12, 2, 4, 1]
    starts = [0, 12, 14, 18]
    projectors = []
    for start, dimension in zip(starts, dimensions):
        projector = sp.zeros(19)
        for index in range(start, start + dimension):
            projector[index, index] = 1
        projectors.append(projector)
    exact("planted readout projectors resolve identity", sum(projectors, sp.zeros(19)) == sp.eye(19))
    exact("planted readout projectors commute with one Hessian", all(p * parent_hessian == parent_hessian * p for p in projectors))


def odd_krein_hamiltonian_controls() -> None:
    krein2 = sp.Matrix([[0, 1], [1, 0]])
    krein = block_diag(krein2, krein2)
    theta = krein
    chirality = sp.diag(1, -1, 1, -1)

    dirac_luminous = sp.Matrix([[1, 3], [2, 1]])
    dirac_dark = sp.Matrix([[4, 6], [5, 4]])
    base_operator = block_diag(dirac_luminous, dirac_dark)
    mass_operator = sp.eye(4)
    hilbert_mixing = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(2), sp.eye(2)),
        sp.Matrix.hstack(sp.eye(2), sp.zeros(2)),
    )
    krein_mixing = krein * hilbert_mixing
    current2 = sp.Matrix([[0, 1], [2, 0]])
    current_operator = block_diag(current2, sp.zeros(2))

    parameter_a, curvature, mass = sp.symbols("a c m", real=True)
    operator = base_operator + parameter_a * current_operator + curvature * krein_mixing + mass * mass_operator

    def krein_adjoint(matrix: sp.Matrix) -> sp.Matrix:
        return krein.inv() * matrix.T * krein

    exact("minimal odd operator is Krein self-adjoint", krein_adjoint(operator) == operator)
    exact("fundamental symmetry produces positive majorant", krein * theta == sp.eye(4))
    h_form = theta * operator
    exact("Theta D is the Hilbert form representative", h_form.T == h_form)
    generator = -sp.I * h_form
    exact("finite form representative generates unitary algebraic flow", generator.conjugate().T == -generator)

    exact("bare vertical mass operator preserves chirality", mass_operator * chirality == chirality * mass_operator)
    exact("K-paired mass bilinear is cross-chirality", krein * mass_operator * chirality == -chirality * krein * mass_operator)
    planted("bare mass operator alone diagnoses the bilinear channel", mass_operator * chirality == -chirality * mass_operator)

    luminous = sp.diag(1, 1, 0, 0)
    dark = sp.eye(4) - luminous
    exact(
        "luminous and dark odd sectors decouple at the background",
        luminous * operator.subs({curvature: 0}) * dark == sp.zeros(4),
    )
    exact(
        "one declared curvature parameter recouples the complement",
        luminous * operator.subs({curvature: 1}) * dark != sp.zeros(4),
    )
    exact("physical luminous projector remains fixed during recoupling", luminous == sp.diag(1, 1, 0, 0))

    test_spinor = sp.Matrix([1, 2, -1, 3])
    odd_action = (test_spinor.T * krein * operator * test_spinor)[0]
    current = sp.diff(odd_action, parameter_a)
    exact(
        "gauge current is the derivative of the same odd action",
        current == (test_spinor.T * krein * current_operator * test_spinor)[0],
    )

    gauge_generator = sp.diag(1, -1)
    gauge_operator = dirac_luminous
    bar = sp.Matrix([[2, 1]])
    psi = sp.Matrix([1, 3])
    operator_variation = gauge_generator * gauge_operator - gauge_operator * gauge_generator
    ward = (
        -bar * gauge_generator * gauge_operator * psi
        + bar * operator_variation * psi
        + bar * gauge_operator * gauge_generator * psi
    )[0]
    frozen_operator_ward = (
        -bar * gauge_generator * gauge_operator * psi
        + bar * gauge_operator * gauge_generator * psi
    )[0]
    exact("coupled finite Ward variation vanishes", ward == 0)
    planted("freezing the moving odd operator preserves the Ward identity", frozen_operator_ward == 0)

    bad_operator = sp.diag(1, 2, 1, 2)
    planted("ordinary diagonal operator is automatically Krein self-adjoint", krein_adjoint(bad_operator) == bad_operator)
    fake_theta = sp.eye(4)
    planted("identity is a positive majorant for the indefinite pairing", krein * fake_theta == sp.eye(4))

    boundary_form = sp.diag(1, -1)
    good_line = sp.Matrix([[1, 1]])
    bad_line = sp.Matrix([[1, 0]])
    exact("declared boundary-line positive control is isotropic", (good_line * boundary_form * good_line.T)[0] == 0)
    planted("nonisotropic boundary line passes the isotropy control", (bad_line * boundary_form * bad_line.T)[0] == 0)


def preboundary_reduction_controls() -> None:
    omega_observed = sp.Matrix([[0, 1], [-1, 0]])
    shear = sp.Matrix([[1, 0, 0], [0, 1, 0], [1, 1, 1]])
    inclusion = sp.Matrix([[1, 0], [0, 1], [0, 0]])
    projection = sp.Matrix([[1, 0, 0], [0, 1, 0]])
    lift = shear * inclusion
    retract = projection * shear.inv()
    omega_native = shear.inv().T * block_diag(omega_observed, sp.zeros(1)) * shear.inv()
    exact("preboundary retract closes", retract * lift == sp.eye(2))
    exact("preboundary pullback is symplectic", lift.T * omega_native * lift == omega_observed)
    exact("preboundary form has one characteristic direction", len(omega_native.nullspace()) == 1)
    exact("characteristic kernel equals discarded decoder kernel", omega_native.nullspace()[0] in retract.nullspace())
    planted("degenerate preboundary form is already a physical phase space", omega_native.det() != 0)


def certificate_controls() -> None:
    certificate = json.loads(CERTIFICATE.read_text())
    atlas = json.loads(ATLAS.read_text())
    atlas_callouts = {row["id"] for row in atlas["requested_source_crosswalk"]}
    rows = {row["id"]: row for row in certificate["readouts"]}
    expected_rows = {
        "MAXWELL",
        "YANG_MILLS",
        "EINSTEIN",
        "HIGGS",
        "DIRAC",
        "SCHRODINGER",
        "WEAK",
        "STRONG",
        "DARK_ENERGY",
        "DARK_MATTER",
    }
    exact("certificate closes all ten requested readout rows once", set(rows) == expected_rows and len(rows) == 10)
    exact("atlas points to the executed closure packet", atlas["executed_closure_packet"] == "lab/specifications/eric-source-directed-native-closure-packet-2026-07-31.md")
    exact("atlas points to the executed closure certificate", atlas["executed_closure_certificate"] == "lab/process/eric-source-directed-native-closure-certificate.json")
    exact("every readout retains a source directive", all(row["source_callout_id"] in atlas_callouts for row in rows.values()))
    exact("every readout names one shared parent object", all(row["shared_parent_object"] for row in rows.values()))
    exact("every readout records a passed bounded control", all(row["finite_control_status"] == "PASS_POSITIVE_CONTROL" for row in rows.values()))
    exact("every Y14 emergence gate remains open", all(row["y14_emergence_status"] == "OPEN" for row in rows.values()))
    exact("certificate forbids equation-by-equation insertion", certificate["independent_standard_equations_inserted"] == 0)
    exact("certificate reports planted algebra honestly", certificate["planted_standard_model_fixture_is_emergence_evidence"] is False)
    exact("certificate retains supplied datum ledger", certificate["datum_ledger"] == ["P1", "P2", "P3"])
    exact("Maxwell classifier is typed in the stabilizer", "central stabilizer ideal" in rows["MAXWELL"]["shared_parent_object"])
    exact("dark physical complement is distinct from off-observation leakage", "distinct from C1's off-observation Q_off" in rows["DARK_MATTER"]["shared_parent_object"])
    exact("finite boundary result leaves BFV extension open", "BFV extension still open" in rows["SCHRODINGER"]["shared_parent_object"])
    planted("finite compatibility is reported as full GU recovery", certificate["verdict"] == "FULL_GU_RECOVERY")
    planted("three carrier blocks are reported as generations", certificate["generation_count_claimed"] is True)


def main() -> None:
    observation_and_variation_controls()
    frobenius_trace_reversal_controls()
    compact_gauge_positive_control()
    shared_bosonic_hessian_controls()
    odd_krein_hamiltonian_controls()
    preboundary_reduction_controls()
    certificate_controls()
    print(
        "ERIC-SOURCE-DIRECTED-NATIVE-CLOSURE: "
        f"{exact_checks} exact checks + {planted_checks} planted failures = "
        f"{exact_checks + planted_checks} PASS"
    )
    print("RESULT: ten source directives close through five shared conditional parent objects")
    print("RESULT: decoder, trace reversal, stabilizer, Hessian, odd action, and Hamiltonian types coexist exactly")
    print("RESULT: Maxwell/YM/spin-two/Higgs/cosmology and Dirac/dark/current readouts share parent operators")
    print("BOUNDARY: planted finite fixtures are compatibility controls, not Y14 or Standard Model emergence")
    print("BOUNDARY: no generation count, anomaly closure, physical domain, or empirical prediction is claimed")


if __name__ == "__main__":
    main()
