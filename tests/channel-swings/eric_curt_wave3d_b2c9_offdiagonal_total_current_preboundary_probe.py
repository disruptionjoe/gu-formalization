#!/usr/bin/env python3
r"""B2C9 first-jet Euler, fermion-current, and total-preboundary probe.

This exact rational probe begins at the 2021 independent-dual fermion packet
instead of guessing a supersymmetry action.  It keeps four objects separate:

* the finite graph-source bosonic action and its *full first-jet* Euler
  covector (the older twelve-coordinate reconstruction is only its algebraic
  zero-jet part);
* the source-displayed zero-southeast fermion block and the draft-admitted
  nonzero-southeast coefficient family;
* an independent density-dual row field and a generic same-field
  moving-lowerer control (not the active constrained-real pullback);
* the adjoint Euler current, ordinary-gauge Ward current, and Green/
  preboundary current.

The finite fermion model suppresses spin/form multiplicities and active
Hodge/Shiab/adjoint projections but retains the
two connection owners, all four zero-order blocks, the moving indefinite
lowerer, and exact first-jet gauge law.  It is an architecture theorem, not a
claim to be the missing active Cl(9,5) Grassmann action or a selected physical
domain.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import runpy
import sys


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests/channel-swings"
if str(CHANNEL) not in sys.path:
    sys.path.insert(0, str(CHANNEL))

G2 = runpy.run_path(str(CHANNEL / "g2_native_variational_shiab_probe.py"))
B2C7 = runpy.run_path(
    str(CHANNEL / "eric_curt_wave3d_b2c7_two_connection_somatic_obstruction_probe.py")
)

FAILURES: list[str] = []
EXACT = 0
SOURCE_RECEIPTS = 0
TYPE_LEVEL = 0
PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(label)


def source_receipt(label: str, condition: bool, detail: str = "") -> None:
    global SOURCE_RECEIPTS
    SOURCE_RECEIPTS += 1
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: source receipt - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"source receipt: {label}")


def type_level(label: str, condition: bool = True, detail: str = "") -> None:
    global TYPE_LEVEL
    TYPE_LEVEL += 1
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: type-level - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"type-level: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    status = "PASS" if not false_claim else "FAIL"
    print(f"{status}: planted rejection - {label}", flush=True)
    if false_claim:
        FAILURES.append(f"planted: {label}")


def richardson(function):
    return (
        F(8) * (function(F(1)) - function(F(-1)))
        - (function(F(2)) - function(F(-2)))
    ) / F(12)


def richardson_tuple(function):
    p1, m1, p2, m2 = function(F(1)), function(F(-1)), function(F(2)), function(F(-2))
    return tuple(F(8) * (a - b) / F(12) - (c - d) / F(12) for a, b, c, d in zip(p1, m1, p2, m2))


def mzero():
    return G2["ZERO"]


def madd(left, right):
    return G2["add"](left, right)


def msub(left, right):
    return G2["sub"](left, right)


def mscale(value, matrix):
    return G2["scale"](F(value), matrix)


def mcomm(left, right):
    return G2["comm"](left, right)


def matrix_zero(matrix) -> bool:
    return all(entry == 0 for row in matrix for entry in row)


def nested_nonzero(value) -> bool:
    if isinstance(value, (tuple, list)):
        return any(nested_nonzero(item) for item in value)
    return value != 0


def transpose(matrix):
    return tuple(tuple(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0])))


def f1_add(left, right):
    return tuple(madd(a, b) for a, b in zip(left, right))


def f1_scale(value, form):
    return tuple(mscale(value, item) for item in form)


def f2_add(left, right):
    return tuple(madd(a, b) for a, b in zip(left, right))


def f2_scale(value, form):
    return tuple(mscale(value, item) for item in form)


def f2_comm(chi, form):
    return tuple(mcomm(chi, item) for item in form)


def matrix_line(base, direction, parameter):
    return madd(base, mscale(parameter, direction))


def form_line(base, direction, parameter):
    return tuple(matrix_line(item, delta, parameter) for item, delta in zip(base, direction))


def source_checks() -> None:
    rendered = (
        ROOT
        / "explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md"
    ).read_text()
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    b2c7_report = (
        ROOT / "explorations/eric-curt-wave3d-b2c7-two-connection-somatic-obstruction-2026-08-01.md"
    ).read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()

    source_receipt(
        "draft p46 types barred/unbarred zeta and nu as the independent fermion packet",
        "equations (9.18)--(9.20)" in pack
        and "Omega^{d-1}(Y,S)" in pack
        and "Omega^d(Y,S)" in pack,
    )
    source_receipt(
        "draft p46 supplies the explicit adjoint-valued bilinear current component",
        r"\bar\nu\zeta+\bar\zeta\nu+\mathscr S_\omega\bar\zeta\zeta" in b2c7_report,
    )
    source_receipt(
        "draft keeps first-order-total and second-order-sourced coupling architectures rival",
        r"\Upsilon^B_\omega+\Upsilon^F_\omega=0" in pack
        and r"D_\omega^*\Upsilon^B_\omega=\Upsilon^F_\omega" in pack,
    )
    source_receipt(
        "modern two-connection on-shell object is explicitly unreleased",
        "have never released" in toe and "on shell where the equations get satisfied" in toe,
    )
    type_level("physical nu is not a BV ghost, odd parameter, or neutrino-species label")
    type_level("adjoint Euler current, Noether current, observed Maxwell current, and Green current are distinct")
    type_level("independent density-dual and constrained symplectic-real variations are distinct")
    type_level("the two draft coupling architectures are compared, not indiscriminately summed")
    type_level("the B2C8 2025-shaped cones are repo reconstructions, not released Weinstein formulas")
    type_level("the active Frobenius-fibre lowerer remains the trace-reversed (9,5), not an ordinary positive product")


# ---------------------------------------------------------------------------
# Full first-jet bosonic Euler covector.

PAIRS = ((0, 1), (0, 2), (1, 2))


def antisymmetrize(jets):
    return tuple(msub(jets[j][i], jets[i][j]) for i, j in PAIRS)


def source_lagrangian(background) -> F:
    b, t, h, b_jets, t_jets, _h_jets, metric_scale, kappa = background
    db = antisymmetrize(b_jets)
    dt = antisymmetrize(t_jets)
    current = G2["source_curvature"](b, db, t, dt, F(1, 2), F(1, 3))
    return G2["wedge_pair"](t, G2["shiab_insert"](h, current)) + (
        F(kappa, 2) * metric_scale * G2["inner1"](t, t)
    )


def shift_background(background, direction, parameter):
    b, t, h, b_jets, t_jets, h_jets, metric_scale, kappa = background
    db, dt, dh, dbj, dtj, dhj = direction
    return (
        form_line(b, db, parameter),
        form_line(t, dt, parameter),
        matrix_line(h, dh, parameter),
        tuple(form_line(row, drow, parameter) for row, drow in zip(b_jets, dbj)),
        tuple(form_line(row, drow, parameter) for row, drow in zip(t_jets, dtj)),
        form_line(h_jets, dhj, parameter),
        metric_scale,
        kappa,
    )


def zero_direction():
    z1 = (mzero(),) * 3
    zj = (z1, z1, z1)
    return z1, z1, mzero(), zj, zj, z1


def replace_direction(direction, index, value):
    out = list(direction)
    out[index] = value
    return tuple(out)


def algebraic_t_derivative(background, test_form) -> F:
    direction = replace_direction(zero_direction(), 1, test_form)
    return richardson(lambda parameter: source_lagrangian(shift_background(background, direction, parameter)))


def momentum(background, derivative_index, test_form) -> F:
    rows = [[mzero() for _ in range(3)] for _ in range(3)]
    for component in range(3):
        rows[component][derivative_index] = test_form[component]
    direction = replace_direction(
        zero_direction(), 4, tuple(tuple(row) for row in rows)
    )
    return richardson(lambda parameter: source_lagrangian(shift_background(background, direction, parameter)))


def spatial_shift(background, derivative_index, parameter):
    b, t, h, b_jets, t_jets, h_jets, metric_scale, kappa = background
    return (
        tuple(matrix_line(b[i], b_jets[i][derivative_index], parameter) for i in range(3)),
        tuple(matrix_line(t[i], t_jets[i][derivative_index], parameter) for i in range(3)),
        matrix_line(h, h_jets[derivative_index], parameter),
        b_jets,
        t_jets,
        h_jets,
        metric_scale,
        kappa,
    )


def full_euler_functional(background, test_form) -> F:
    algebraic = algebraic_t_derivative(background, test_form)
    divergence = sum(
        (
            richardson(
                lambda parameter, j=j: momentum(
                    spatial_shift(background, j, parameter), j, test_form
                )
            )
            for j in range(3)
        ),
        F(0),
    )
    return algebraic - divergence


def gauge_direction(background, chi, chi_jets, chi_second, freeze_h_jet=False, omit_b_jet=False):
    b, t, h, b_jets, t_jets, h_jets, _metric_scale, _kappa = background
    delta_b = tuple(msub(mcomm(chi, b[i]), chi_jets[i]) for i in range(3))
    delta_t = tuple(mcomm(chi, t[i]) for i in range(3))
    delta_h = mcomm(chi, h)
    delta_b_jets = []
    delta_t_jets = []
    for i in range(3):
        row_b = []
        row_t = []
        for j in range(3):
            row_b.append(
                mzero()
                if omit_b_jet
                else msub(
                    madd(mcomm(chi, b_jets[i][j]), mcomm(chi_jets[j], b[i])),
                    chi_second[i][j],
                )
            )
            row_t.append(madd(mcomm(chi, t_jets[i][j]), mcomm(chi_jets[j], t[i])))
        delta_b_jets.append(tuple(row_b))
        delta_t_jets.append(tuple(row_t))
    delta_h_jets = tuple(
        mzero()
        if freeze_h_jet
        else madd(mcomm(chi, h_jets[j]), mcomm(chi_jets[j], h))
        for j in range(3)
    )
    return (
        delta_b,
        delta_t,
        delta_h,
        tuple(delta_b_jets),
        tuple(delta_t_jets),
        delta_h_jets,
    )


def bosonic_fixture():
    M = G2["M"]
    b = (M(1, 1, 0, -1), M(0, 1, 2, 1), M(2, -1, 1, 0))
    t = (M(0, 2, -1, 1), M(1, -1, 1, 2), M(-1, 0, 2, 1))
    h = M(1, 2, -1, 0)
    b_jets = (
        (M(1, 0, 0, -1), M(0, 1, -1, 0), M(1, 2, 0, -1)),
        (M(-1, 0, 1, 2), M(0, 2, 1, -1), M(2, 0, -1, 1)),
        (M(0, 1, 2, 0), M(1, -1, 0, 2), M(-1, 2, 1, 0)),
    )
    t_jets = (
        (M(0, 1, -2, 1), M(1, 0, 2, -1), M(-1, 1, 0, 2)),
        (M(2, -1, 0, 1), M(0, -1, 1, 2), M(1, 2, -1, 0)),
        (M(-1, 0, 1, 1), M(2, 1, 0, -1), M(0, 2, -2, 1)),
    )
    h_jets = (M(0, 1, 2, -1), M(1, -1, 0, 2), M(2, 0, -1, 1))
    return b, t, h, b_jets, t_jets, h_jets, F(7, 5), F(5, 3)


def bosonic_first_jet_checks() -> None:
    M = G2["M"]
    background = bosonic_fixture()
    chi = M(0, 1, -1, 0)
    chi_jets = (M(1, 0, 0, -1), M(0, 1, 1, 0), M(2, -1, 0, 1))
    chi_second = (
        (M(0, 1, 1, 0), M(1, 0, -1, 1), M(0, 2, 1, -1)),
        (M(1, 0, -1, 1), M(2, -1, 0, 0), M(-1, 1, 2, 0)),
        (M(0, 2, 1, -1), M(-1, 1, 2, 0), M(1, 0, 0, -1)),
    )
    basis = []
    for slot in range(3):
        for matrix_index in range(4):
            entries = [mzero(), mzero(), mzero()]
            entries[slot] = B2C7["unit2"](matrix_index)
            basis.append(tuple(entries))
    test = basis[0]
    tangent = gauge_direction(background, chi, chi_jets, chi_second)
    derivatives = tuple(
        richardson(
            lambda parameter, item=item: full_euler_functional(
                shift_background(background, tangent, parameter), item
            )
        )
        for item in basis
    )
    coadjoints = tuple(
        full_euler_functional(background, tuple(mcomm(chi, component) for component in item))
        for item in basis
    )
    derivative, coadjoint = derivatives[0], coadjoints[0]
    exact(
        "finite horizontally completed first-jet Euler covector obeys the invariant coadjoint sign in all twelve basis directions",
        all(left + right == 0 and right != 0 for left, right in zip(derivatives, coadjoints)),
    )
    exact("completed Euler fixture is nonvacuous", full_euler_functional(background, test) != 0)

    zero_chi = mzero()
    pure_jet = gauge_direction(background, zero_chi, chi_jets, chi_second)
    pure_derivatives = tuple(
        richardson(
            lambda parameter, item=item: full_euler_functional(
                shift_background(background, pure_jet, parameter), item
            )
        )
        for item in basis
    )
    pure_derivative = pure_derivatives[0]
    pure_tangent_nonzero = nested_nonzero(pure_jet)
    exact(
        "nonzero pure dchi gauge jet is invisible to the completed Euler covector in all twelve basis directions",
        pure_tangent_nonzero and all(value == 0 for value in pure_derivatives),
    )

    frozen_h = gauge_direction(background, chi, chi_jets, chi_second, freeze_h_jet=True)
    frozen_h_derivative = richardson(
        lambda parameter: full_euler_functional(
            shift_background(background, frozen_h, parameter), test
        )
    )
    reject("freeze the first jet of the moving Shiab insertion", frozen_h_derivative + coadjoint == 0)

    omitted_b_jet = gauge_direction(background, chi, chi_jets, chi_second, omit_b_jet=True)
    omitted_derivative = richardson(
        lambda parameter: full_euler_functional(
            shift_background(background, omitted_b_jet, parameter), test
        )
    )
    reject("omit the prolonged connection-jet law", omitted_derivative + coadjoint == 0)
    reject("use the opposite coadjoint sign", derivative - coadjoint == 0)

    # The B2C7 reconstruction varies T with d(delta T)=0 and therefore omits
    # the horizontal divergence.  Its failure is retained as a control.
    b, t, h, b_jets, t_jets, _hj, _m, kappa = background
    db, dt = antisymmetrize(b_jets), antisymmetrize(t_jets)
    old_euler = lambda bg: B2C7["reconstruct_euler_form"](
        bg[0], bg[1], antisymmetrize(bg[3]), antisymmetrize(bg[4]), bg[2], kappa
    )[0]
    old_pure = richardson_tuple(
        lambda parameter: tuple(
            entry
            for component in old_euler(shift_background(background, pure_jet, parameter))
            for row in component
            for entry in row
        )
    )
    reject("the old zero-jet algebraic reconstruction passes the pure-dchi test", all(x == 0 for x in old_pure))
    exact("old and completed Euler objects are explicitly kept distinct", db != dt and any(x != 0 for x in old_pure))


# ---------------------------------------------------------------------------
# Two-sector independent-dual fermion family and action-derived currents.

Vector = tuple[F, F]
Matrix = tuple[tuple[F, F], tuple[F, F]]


def vadd(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def vscale(value, vector: Vector) -> Vector:
    return tuple(F(value) * item for item in vector)  # type: ignore[return-value]


def vdot(row: Vector, column: Vector) -> F:
    return sum((a * b for a, b in zip(row, column)), F(0))


def mv(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(sum((matrix[i][j] * vector[j] for j in range(2)), F(0)) for i in range(2))  # type: ignore[return-value]


def row_mv(row: Vector, matrix: Matrix) -> Vector:
    return tuple(sum((row[i] * matrix[i][j] for i in range(2)), F(0)) for j in range(2))  # type: ignore[return-value]


def outer(row: Vector, column: Vector) -> Matrix:
    return tuple(tuple(row[i] * column[j] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def matrix_pair(current: Matrix, variation: Matrix) -> F:
    return sum((current[i][j] * variation[i][j] for i in range(2) for j in range(2)), F(0))


def block_transform(block: Matrix, chi: Matrix) -> Matrix:
    return mcomm(chi, block)


def covariant(connection: Matrix, value: Vector, derivative: Vector) -> Vector:
    return vadd(derivative, mv(connection, value))


def fermion_residuals(state, coefficients, masses):
    zeta, nu, dzeta, dnu, a, b = state
    w, ell, r, s = coefficients
    mzz, mzn, mnz, mnn = masses
    db_zeta = covariant(b, zeta, dzeta)
    da_nu = covariant(a, nu, dnu)
    r_zeta = vadd(vadd(vscale(w, db_zeta), vscale(r, da_nu)), vadd(mv(mzz, zeta), mv(mzn, nu)))
    r_nu = vadd(vadd(vscale(s, db_zeta), vscale(ell, da_nu)), vadd(mv(mnz, zeta), mv(mnn, nu)))
    return r_zeta, r_nu


def fermion_action(state, duals, coefficients, masses, density=F(1)) -> F:
    bar_zeta, bar_nu = duals
    r_zeta, r_nu = fermion_residuals(state, coefficients, masses)
    return density * (vdot(bar_zeta, r_zeta) + vdot(bar_nu, r_nu))


def line_state(state, direction, parameter):
    zeta, nu, dzeta, dnu, a, b = state
    dz, dn, ddz, ddn, da, db = direction
    return (
        vadd(zeta, vscale(parameter, dz)),
        vadd(nu, vscale(parameter, dn)),
        vadd(dzeta, vscale(parameter, ddz)),
        vadd(dnu, vscale(parameter, ddn)),
        matrix_line(a, da, parameter),
        matrix_line(b, db, parameter),
    )


def line_duals(duals, direction, parameter):
    return tuple(vadd(item, vscale(parameter, delta)) for item, delta in zip(duals, direction))


def line_masses(masses, direction, parameter):
    return tuple(matrix_line(item, delta, parameter) for item, delta in zip(masses, direction))


def fermion_current_checks() -> None:
    M = G2["M"]
    zeta, nu = (F(1), F(2)), (F(-1), F(3))
    dzeta, dnu = (F(2), F(-2)), (F(1), F(1))
    a, b = M(1, 1, 0, -1), M(0, 1, -2, 1)
    state = (zeta, nu, dzeta, dnu, a, b)
    duals = ((F(2), F(-1)), (F(1), F(3)))
    coefficients = (F(2), F(-3, 4), F(1), F(1))
    masses = (M(1, 0, 0, -1), M(0, 1, 1, 0), M(2, -1, 0, 1), M(1, 2, -1, 0))

    direction = (
        (F(1), F(-1)), (F(2), F(0)), (F(-1), F(2)), (F(0), F(1)),
        M(0, 1, -1, 0), M(1, 0, 0, -1),
    )
    dual_direction = ((F(-1), F(2)), (F(2), F(1)))
    mass_direction = (M(0, 1, 0, 0), M(1, 0, -1, 0), M(0, 0, 1, 0), M(1, -1, 0, 1))
    density_direction = F(2, 5)
    finite = richardson(
        lambda parameter: fermion_action(
            line_state(state, direction, parameter),
            line_duals(duals, dual_direction, parameter),
            coefficients,
            line_masses(masses, mass_direction, parameter),
            F(7, 5) + parameter * density_direction,
        )
    )
    residual = fermion_residuals(state, coefficients, masses)
    delta_residual = richardson_tuple(
        lambda parameter: tuple(
            x
            for item in fermion_residuals(
                line_state(state, direction, parameter), coefficients, line_masses(masses, mass_direction, parameter)
            )
            for x in item
        )
    )
    analytic = density_direction * (vdot(duals[0], residual[0]) + vdot(duals[1], residual[1]))
    analytic += F(7, 5) * (
        vdot(dual_direction[0], residual[0])
        + vdot(dual_direction[1], residual[1])
        + vdot(duals[0], delta_residual[:2])
        + vdot(duals[1], delta_residual[2:])
    )
    exact("all-slot independent-dual fermion variation equals the exact directional derivative", finite == analytic)
    exact("barred variation emits both fermion residuals without another Krein factor", residual[0] != (0, 0) and residual[1] != (0, 0))

    w, ell, r, s = coefficients
    bar_zeta, bar_nu = duals
    j_a = outer(vadd(vscale(r, bar_zeta), vscale(ell, bar_nu)), nu)
    j_b = outer(vadd(vscale(w, bar_zeta), vscale(s, bar_nu)), zeta)
    h_a, h_b = direction[4], direction[5]
    connection_only = richardson(
        lambda parameter: fermion_action(
            line_state(state, ((0, 0), (0, 0), (0, 0), (0, 0), h_a, h_b), parameter),
            duals,
            coefficients,
            masses,
        )
    )
    exact("variation derives separate A and B adjoint Euler currents", connection_only == matrix_pair(j_a, h_a) + matrix_pair(j_b, h_b))

    # A tensorial zero-order block may be built from T=A-B.  Returning that
    # primitive dependence through the graph changes both connection owners.
    graph_masses = (masses[0], msub(a, b), masses[2], masses[3])
    j_t = outer(bar_zeta, nu)
    graph_connection_variation = richardson(
        lambda parameter: fermion_action(
            line_state(state, ((0, 0), (0, 0), (0, 0), (0, 0), h_a, h_b), parameter),
            duals,
            coefficients,
            (
                graph_masses[0],
                matrix_line(graph_masses[1], msub(h_a, h_b), parameter),
                graph_masses[2],
                graph_masses[3],
            ),
        )
    )
    exact(
        "T=A-B zero-order placement returns plus J_T to A and minus J_T to the reduction connection",
        graph_connection_variation
        == matrix_pair(madd(j_a, j_t), h_a) + matrix_pair(msub(j_b, j_t), h_b),
    )
    frozen_t_return = richardson(
        lambda parameter: fermion_action(
            line_state(state, ((0, 0), (0, 0), (0, 0), (0, 0), h_a, h_b), parameter),
            duals,
            coefficients,
            graph_masses,
        )
    )
    reject("freeze a T-built zero-order block during graph return", frozen_t_return == graph_connection_variation)
    reduction_direction = M(1, -1, 2, 0)
    reduction_return = matrix_pair(msub(j_b, j_t), reduction_direction)
    exact(
        "a supplied reduction direction pairs with the intermediate J_B-J_T covector before any owner transpose",
        reduction_return
        == richardson(
            lambda parameter: fermion_action(
                line_state(
                    state,
                    ((0, 0), (0, 0), (0, 0), (0, 0), mzero(), reduction_direction),
                    parameter,
                ),
                duals,
                coefficients,
                (
                    graph_masses[0],
                    matrix_line(graph_masses[1], mscale(-1, reduction_direction), parameter),
                    graph_masses[2],
                    graph_masses[3],
                ),
            )
        ),
    )

    source_coefficients = (F(2), F(0), F(1), F(1))
    w0, ell0, r0, s0 = source_coefficients
    source_current = madd(
        outer(vscale(r0, bar_zeta), nu),
        madd(outer(vscale(s0, bar_nu), zeta), outer(vscale(w0, bar_zeta), zeta)),
    )
    diagonal_current = madd(
        outer(vadd(vscale(r0, bar_zeta), vscale(ell0, bar_nu)), nu),
        outer(vadd(vscale(w0, bar_zeta), vscale(s0, bar_nu)), zeta),
    )
    exact("zero-southeast diagonal-connection comparator reproduces the draft's three bilinear monomial pattern", diagonal_current == source_current)
    repaired_current = madd(j_a, j_b)
    reject("a nonzero southeast derivative leaves the scalarized bilinear comparator unchanged", repaired_current == source_current)
    exact("the candidate extra comparator channel is exactly ell times bar-nu tensor nu", msub(repaired_current, source_current) == outer(vscale(ell, bar_nu), nu))

    # Full local first-jet ordinary gauge Ward identity.
    chi, dchi = M(0, 1, -1, 0), M(1, 0, 0, -1)
    delta_zeta, delta_nu = mv(chi, zeta), mv(chi, nu)
    delta_dzeta = vadd(mv(chi, dzeta), mv(dchi, zeta))
    delta_dnu = vadd(mv(chi, dnu), mv(dchi, nu))
    delta_a, delta_b = msub(mcomm(chi, a), dchi), msub(mcomm(chi, b), dchi)
    gauge_state = (delta_zeta, delta_nu, delta_dzeta, delta_dnu, delta_a, delta_b)
    gauge_duals = (vscale(-1, row_mv(bar_zeta, chi)), vscale(-1, row_mv(bar_nu, chi)))
    gauge_masses = tuple(block_transform(block, chi) for block in masses)
    ward = richardson(
        lambda parameter: fermion_action(
            line_state(state, gauge_state, parameter),
            line_duals(duals, gauge_duals, parameter),
            coefficients,
            line_masses(masses, gauge_masses, parameter),
        )
    )
    exact("fermion action closes the complete first-jet ordinary-gauge Ward identity", ward == 0)
    bad_derivative_state = (delta_zeta, delta_nu, mv(chi, dzeta), mv(chi, dnu), delta_a, delta_b)
    bad_ward = richardson(
        lambda parameter: fermion_action(
            line_state(state, bad_derivative_state, parameter),
            line_duals(duals, gauge_duals, parameter),
            coefficients,
            line_masses(masses, gauge_masses, parameter),
        )
    )
    reject("drop dchi from the matter first-jet transformation", bad_ward == 0)
    frozen_mass_ward = richardson(
        lambda parameter: fermion_action(
            line_state(state, gauge_state, parameter),
            line_duals(duals, gauge_duals, parameter),
            coefficients,
            masses,
        )
    )
    reject("freeze a noncentral zero-order completion in the Ward identity", frozen_mass_ward == 0)


def coefficient_and_real_pullback_checks() -> None:
    # Exact tied B2C5 stratum and its unresolved invariant.
    w_plus, w_minus, r = F(2), F(3), F(3, 2)
    ell_plus = -F(11) * r * r / (F(12) * w_minus)
    ell_minus = -F(11) * r * r / (F(12) * w_plus)
    p = w_plus * w_minus / (r * r)
    exact("tied nonzero-southeast family satisfies both exact 11/12 reciprocal equations", F(12) * w_plus * ell_minus + F(11) * r * r == 0 and F(12) * w_minus * ell_plus + F(11) * r * r == 0)
    exact("the surviving dimensionless family coordinate p is explicit and non-datum", p == F(8, 3))
    reject("replace the derived 11/12 coefficient by 10/12", F(12) * w_plus * (-F(10) * r * r / (F(12) * w_plus)) + F(11) * r * r == 0)
    type_level("strict zero corner, zero-principal corner with M00, and nonzero-principal southeast repair are separate strata")
    type_level("M0 has four typed blocks; Krein/reality pairs M10 with M01 rather than selecting either independently")
    type_level("overall source coupling and p remain construction parameters, not P1/P2/P3")

    # Moving indefinite lowerer: independent dual has no delta-K term; the
    # a future constrained-real pullback would require its active analogue.
    M = G2["M"]
    k0 = M(1, 0, 0, -1)
    n = M(0, 1, 0, 0)
    delta_k = madd(G2["mm"](transpose(n), k0), G2["mm"](k0, n))
    operator = M(1, 2, -1, 0)
    psi = (F(2), F(-1))
    delta_psi = (F(1), F(3))
    row = row_mv(psi, k0)
    constrained = vdot(row, mv(operator, psi))
    constrained_variation = (
        vdot(row_mv(delta_psi, k0), mv(operator, psi))
        + vdot(row_mv(psi, delta_k), mv(operator, psi))
        + vdot(row, mv(operator, delta_psi))
    )
    finite = richardson(
        lambda parameter: vdot(
            row_mv(vadd(psi, vscale(parameter, delta_psi)), matrix_line(k0, delta_k, parameter)),
            mv(operator, vadd(psi, vscale(parameter, delta_psi))),
        )
    )
    exact("finite same-field pullback control includes the moving generic indefinite lowerer exactly once", finite == constrained_variation and constrained != 0)
    reject(
        "freeze the generic indefinite lowerer in the same-field control",
        finite == constrained_variation - vdot(row_mv(psi, delta_k), mv(operator, psi)),
    )
    k0_inv = k0
    delta_inverse = mscale(-1, G2["mm"](G2["mm"](k0_inv, delta_k), k0_inv))
    inverse_identity_derivative = madd(G2["mm"](delta_inverse, k0), G2["mm"](k0_inv, delta_k))
    exact("the generic primalizer inverse carries the forced minus moving-lowerer response", matrix_zero(inverse_identity_derivative))
    type_level("C-plus reality is not treated as a second Riesz factor in the independent-dual action")


# ---------------------------------------------------------------------------
# Exact polynomial Green and total preboundary packet.

def poly_trim(poly):
    result = list(poly)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def poly_add(left, right):
    length = max(len(left), len(right))
    return poly_trim(tuple((left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0) for i in range(length)))


def poly_scale(value, poly):
    return tuple(F(value) * item for item in poly)


def poly_mul(left, right):
    result = [F(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return poly_trim(tuple(result))


def poly_derivative(poly):
    return (F(0),) if len(poly) == 1 else tuple(F(i) * poly[i] for i in range(1, len(poly)))


def poly_integral_01(poly):
    return sum((value / F(i + 1) for i, value in enumerate(poly)), F(0))


def endpoint(poly):
    return sum(poly, F(0)) - poly[0]


def preboundary_checks() -> None:
    # Fermion Green identity with a moving pairing k(x).
    bar, psi, k = (F(1), F(2), F(-1)), (F(2), F(-1), F(1)), (F(1), F(1))
    direct = poly_mul(poly_mul(bar, k), poly_derivative(psi))
    bulk = poly_scale(-1, poly_mul(poly_add(poly_mul(poly_derivative(bar), k), poly_mul(bar, poly_derivative(k))), psi))
    theta_f = poly_mul(poly_mul(bar, k), psi)
    fermion_boundary = endpoint(theta_f)
    exact("fermion Green identity retains the moving-pairing derivative and boundary flux", poly_integral_01(direct) == poly_integral_01(bulk) + fermion_boundary)
    frozen_bulk = poly_scale(-1, poly_mul(poly_mul(poly_derivative(bar), k), psi))
    reject("freeze the moving pairing inside the fermion Green identity", poly_integral_01(direct) == poly_integral_01(frozen_bulk) + fermion_boundary)
    exact("fermion preboundary contribution is nonzero", fermion_boundary != 0)

    # Reproduce a G3-shaped one-dimensional polynomial Green packet, then add
    # the unsymmetrized fermion comparator rather than jumping to a domain.
    b, t, h, metric = (F(1), F(2), F(-1)), (F(2), F(-1), F(1)), (F(1), F(1)), (F(3), F(-1))
    dbv, dtv = (F(-1), F(2)), (F(1), F(0), F(-2))
    b_prime, t_prime = poly_derivative(b), poly_derivative(t)
    core = poly_add(b_prime, poly_scale(F(1, 2), t_prime))
    direct_b = poly_add(
        poly_add(poly_mul(poly_mul(dtv, h), core), poly_mul(poly_mul(t, h), poly_add(poly_derivative(dbv), poly_scale(F(1, 2), poly_derivative(dtv))))),
        poly_scale(F(5, 3), poly_mul(poly_mul(metric, t), dtv)),
    )
    e_b = poly_scale(-1, poly_derivative(poly_mul(t, h)))
    e_t = poly_add(poly_mul(h, b_prime), poly_add(poly_scale(F(-1, 2), poly_mul(t, poly_derivative(h))), poly_scale(F(5, 3), poly_mul(metric, t))))
    bulk_b = poly_add(poly_mul(e_b, dbv), poly_mul(e_t, dtv))
    theta_b = poly_add(poly_mul(poly_mul(t, h), dbv), poly_scale(F(1, 2), poly_mul(poly_mul(t, h), dtv)))
    boson_boundary = endpoint(theta_b)
    exact("G3-shaped bosonic comparator retains its nonzero boundary flux", poly_integral_01(direct_b) == poly_integral_01(bulk_b) + boson_boundary and boson_boundary != 0)
    exact("additive G3-shaped plus unsymmetrized-fermion Green comparator closes", poly_integral_01(poly_add(direct_b, direct)) == poly_integral_01(poly_add(bulk_b, bulk)) + boson_boundary + fermion_boundary)
    exact("the unsymmetrized fermion fork changes the additive preboundary comparator", boson_boundary + fermion_boundary != boson_boundary)

    # A small exact field-space two-form check for theta_F=bar*k*delta psi.
    dbar1, dpsi1, dk1 = (F(1), F(-1)), (F(2), F(1)), (F(0), F(1))
    dbar2, dpsi2, dk2 = (F(-1), F(2)), (F(1), F(0), F(1)), (F(1),)
    def delta_theta(dbar, dk, test_psi):
        return poly_add(poly_mul(poly_mul(dbar, k), test_psi), poly_mul(poly_mul(bar, dk), test_psi))
    omega12 = endpoint(poly_add(delta_theta(dbar1, dk1, dpsi2), poly_scale(-1, delta_theta(dbar2, dk2, dpsi1))))
    omega21 = endpoint(poly_add(delta_theta(dbar2, dk2, dpsi1), poly_scale(-1, delta_theta(dbar1, dk1, dpsi2))))
    exact("fermion preboundary two-form is antisymmetric and nonzero", omega12 == -omega21 and omega12 != 0)
    type_level("a nonzero total preboundary form does not by itself choose a Green domain or polarization")


def main() -> int:
    source_checks()
    bosonic_first_jet_checks()
    fermion_current_checks()
    coefficient_and_real_pullback_checks()
    preboundary_checks()

    type_level("finite first-jet architecture is not the actual Y14 atlas or active Sp(32,32;H) closed domain")
    type_level("natural-equivariant completeness of M0 and the constrained Grassmann functional remain open")
    type_level("metric/epsilon returns require the actual trace-reversed DeWitt/Hodge/Krein derivatives")
    type_level("neither coupling architecture has yet selected the common Green-Lagrangian domain")
    type_level("no Poisson, prequantum, stationarity, Standard-Model, index, generation, or cosmology claim is made")
    type_level("no P1, P2, or P3 external datum is used to choose a coefficient, current, stress, or domain")

    print(
        f"SUMMARY: {EXACT} computational exact + {SOURCE_RECEIPTS} source receipts + "
        f"{TYPE_LEVEL} type-level + {PLANTED} planted = "
        f"{EXACT + SOURCE_RECEIPTS + TYPE_LEVEL + PLANTED}"
    )
    if FAILURES:
        print("FAILURES: " + "; ".join(FAILURES))
        return 1
    print("RESULT: finite full-first-jet bosonic Euler covariance and the scalarized source-corner bilinear alphabet close exactly")
    print("RESULT: the nonzero-southeast comparator predicts a candidate extra bilinear channel; active projection/nonvanishing is open")
    print("RESULT: a generic same-field moving-lowerer control differs from independent-dual variation by the lowerer response")
    print("RESULT: the additive unsymmetrized fermion plus G3-shaped Green comparator is nonzero but is not the selected B2C5 total form")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
