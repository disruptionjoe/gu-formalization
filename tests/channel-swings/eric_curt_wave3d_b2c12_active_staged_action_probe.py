#!/usr/bin/env python3
r"""B2C12 active staged-action and moving residual-primalizer probe.

This probe constructs, rather than merely names, a local typed realization of
the norm in the manuscript's ``I_2^B=||Upsilon_B||^2``.  The bosonic residual
is treated as a 13-form/density-dual.  Consequently ``b_res`` lowers a primal
one-form residual and ``R_res=b_res^{-1}`` primalizes the repository-typed
density-dual Euler residual. The square is

    I_2^B = 1/2 <E, R_res E>,

not ``1/2 <E,b_res E>``.  Its moving-pairing return is checked in both forms,

    dI = <dE,u> + 1/2 <E,dR E>
       = <dE,u> - 1/2 <u,db u>,       u=R E.

The active coefficient slice uses the trace-reversed metric-on-metrics
geometry with inertia (3,1)+(6,4)=(9,5), and a nondegenerate (+,-) slice of
the invariant trace form on actual right-H/Krein/C-plus connection
generators.  A polynomial one-dimensional model then performs genuine
integration by parts and returns the Green endpoint term.  It is a local
finite-jet certificate, not the global Y^14 formal-adjoint/domain theorem.

The same run also varies the selected nonzero southeast fermion block in its
connection and fermion slots and carries its current through the local
reduction graph.  This derives one additional current contribution.  It does
not source-select every possible cyclic or compensating term, and it does not
identify the connection Euler covector with the observed four-dimensional
Yang--Mills current.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import runpy
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests/channel-swings"
if str(CHANNEL) not in sys.path:
    sys.path.insert(0, str(CHANNEL))

B2C10 = runpy.run_path(
    str(CHANNEL / "eric_curt_wave3d_b2c10_active_current_full_tuple_hessian_probe.py")
)

TOL = 2.0e-7
FAILURES: list[str] = []
COMPUTATIONAL = 0
SOURCE_RECEIPTS = 0
TYPE_LEVEL = 0
PLANTED = 0


def computational(label: str, condition: bool, detail: str = "") -> None:
    global COMPUTATIONAL
    COMPUTATIONAL += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(label)


def source_receipt(label: str, condition: bool, detail: str = "") -> None:
    global SOURCE_RECEIPTS
    SOURCE_RECEIPTS += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: source receipt - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"source receipt: {label}")


def type_level(label: str, condition: bool = True, detail: str = "") -> None:
    global TYPE_LEVEL
    TYPE_LEVEL += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: type-level - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"type-level: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    print(f"{'PASS' if not false_claim else 'FAIL'}: planted rejection - {label}", flush=True)
    if false_claim:
        FAILURES.append(f"planted: {label}")


def max_abs(value) -> float:
    return float(np.max(np.abs(value)))


def source_checks() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    paired = (
        ROOT / "lab/sources/paired-curt-eric-gu-axiom-and-argument-reconstruction-2026-07-31.md"
    ).read_text()
    tau = (
        ROOT / "explorations/hourly-cycles/hourly-20260626-1003-cycle3-tau-source-locator-packet.md"
    ).read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    b2c11 = (
        ROOT / "explorations/eric-curt-wave3d-b2c11-two-connection-current-ownership-2026-08-01.md"
    ).read_text()

    source_receipt(
        "the manuscript writes a bosonic residual norm but does not type the repository primalizer R_res",
        r"I_2^B=\|\Upsilon_\omega^B\|^2" in paired
        and "pairings `Q_B,Q_ED` are typed" in paired,
        "draft 9.11-9.15; Q_B/R_res is a repository realization of the norm glyph",
    )
    source_receipt(
        "the displayed derivative is only a partial varpi direction",
        "partial_varpi_directional_variation_present" in tau
        and "admissible_omega_variation_domain_declaration" in tau,
        "draft 9.7/9.12; epsilon, metric, graph, and domain returns remain open",
    )
    source_receipt(
        "the draft keeps first-order-total and second-order-sourced equations as alternatives",
        r"\Upsilon^B_\omega+\Upsilon^F_\omega=0" in pack
        and r"D_\omega^*\Upsilon^B_\omega=\Upsilon^F_\omega" in pack,
        "draft 9.18-9.20",
    )
    source_receipt(
        "the modern two-connection square/on-shell construction remains unreleased",
        "have never released" in toe and "on shell where the equations get satisfied" in toe,
        "TOE 02:44:06-02:45:13",
    )
    source_receipt(
        "the selected southeast current is a conditional repository construction, not a source-written 9.18 term",
        "minimal repository source-action role" in b2c11
        and "additional cyclic or compensating terms" in b2c11
        and "SOURCE-SILENT" in b2c11,
        "B2C11 source collision",
    )


# ---------------------------------------------------------------------------
# Active trace-reversed residual lowerer/primalizer.


def sym2_basis() -> list[np.ndarray]:
    basis = []
    for left in range(4):
        for right in range(left, 4):
            item = np.zeros((4, 4), dtype=float)
            item[left, right] = 1.0
            item[right, left] = 1.0
            basis.append(item)
    return basis


SYM2 = sym2_basis()


def dewitt_and_derivative(g: np.ndarray, h: np.ndarray | None = None):
    inverse = np.linalg.inv(g)
    d_inverse = None if h is None else -inverse @ h @ inverse

    def value(left, right):
        return float(
            np.trace(inverse @ left @ inverse @ right)
            - 0.5 * np.trace(inverse @ left) * np.trace(inverse @ right)
        )

    gram = np.array([[value(left, right) for right in SYM2] for left in SYM2])
    if h is None:
        return gram

    def derivative(left, right):
        return float(
            np.trace(d_inverse @ left @ inverse @ right)
            + np.trace(inverse @ left @ d_inverse @ right)
            - 0.5
            * (
                np.trace(d_inverse @ left) * np.trace(inverse @ right)
                + np.trace(inverse @ left) * np.trace(d_inverse @ right)
            )
        )

    d_gram = np.array(
        [[derivative(left, right) for right in SYM2] for left in SYM2]
    )
    return gram, d_gram


def gimmel_and_derivative(g: np.ndarray, h: np.ndarray | None = None):
    if h is None:
        fibre = dewitt_and_derivative(g)
        out = np.zeros((14, 14), dtype=float)
        out[:4, :4] = g
        out[4:, 4:] = fibre
        return out
    fibre, d_fibre = dewitt_and_derivative(g, h)
    out = np.zeros((14, 14), dtype=float)
    dout = np.zeros((14, 14), dtype=float)
    out[:4, :4] = g
    out[4:, 4:] = fibre
    dout[:4, :4] = h
    dout[4:, 4:] = d_fibre
    return out, dout


def active_adjoint_slice():
    gammas, _p_plus, _p_minus, beta, right_h, c_plus = B2C10["active_objects"]()
    negative = gammas[0] @ gammas[1]
    positive = gammas[0] @ gammas[9]
    generators = (negative, positive)
    kappa = np.array(
        [
            [float(np.real(np.trace(left @ right))) / 128.0 for right in generators]
            for left in generators
        ]
    )
    defects = [
        B2C10["active_generator_defects"](item, beta, right_h, c_plus)
        for item in generators
    ]
    return gammas, beta, right_h, c_plus, generators, kappa, defects


def residual_maps(g: np.ndarray, h: np.ndarray | None = None):
    _gammas, _beta, _right_h, _c_plus, _generators, kappa, _defects = active_adjoint_slice()
    if h is None:
        geometry = gimmel_and_derivative(g)
        inverse = np.linalg.inv(geometry)
        density = float(np.sqrt(abs(np.linalg.det(geometry))))
        lowerer = density * np.kron(inverse, kappa)
        primalizer = (1.0 / density) * np.kron(geometry, np.linalg.inv(kappa))
        return lowerer, primalizer

    geometry, d_geometry = gimmel_and_derivative(g, h)
    inverse = np.linalg.inv(geometry)
    density = float(np.sqrt(abs(np.linalg.det(geometry))))
    d_density = 0.5 * density * float(np.trace(inverse @ d_geometry))
    d_inverse = -inverse @ d_geometry @ inverse
    lowerer = density * np.kron(inverse, kappa)
    d_lowerer = d_density * np.kron(inverse, kappa) + density * np.kron(d_inverse, kappa)
    primalizer = (1.0 / density) * np.kron(geometry, np.linalg.inv(kappa))
    d_primalizer = (
        (1.0 / density) * np.kron(d_geometry, np.linalg.inv(kappa))
        - (d_density / density**2) * np.kron(geometry, np.linalg.inv(kappa))
    )
    return lowerer, primalizer, d_lowerer, d_primalizer


def trace_reverse(g: np.ndarray, tensor: np.ndarray) -> np.ndarray:
    return tensor - 0.5 * np.trace(np.linalg.inv(g) @ tensor) * g


def active_pairing_checks():
    g0 = np.diag([1.0, 1.0, 1.0, -1.0])
    h = np.diag([0.2, -0.1, 0.15, 0.05])
    geometry, d_geometry = gimmel_and_derivative(g0, h)
    fibre = geometry[4:, 4:]
    eig_fibre = np.linalg.eigvalsh(fibre)
    eig_total = np.linalg.eigvalsh(geometry)
    computational(
        "trace reversal gives fibre inertia (6,4) and total inertia (9,5)",
        (int(np.sum(eig_fibre > 1.0e-9)), int(np.sum(eig_fibre < -1.0e-9))) == (6, 4)
        and (int(np.sum(eig_total > 1.0e-9)), int(np.sum(eig_total < -1.0e-9))) == (9, 5),
    )

    gammas, beta, right_h, c_plus, generators, kappa, defects = active_adjoint_slice()
    computational(
        "the residual coefficient slice uses actual right-H/Krein/C-plus connection generators",
        max(max(item) for item in defects) < 1.0e-9
        and max_abs(kappa - np.diag([-1.0, 1.0])) < 1.0e-9,
        f"kappa={kappa.tolist()}",
    )
    computational(
        "the active spinor Krein form is balanced and right-H compatible",
        tuple(np.unique(np.round(np.linalg.eigvalsh(beta), 8), return_counts=True)[1]) == (64, 64)
        and max_abs(beta @ right_h - right_h @ beta.conj()) < 1.0e-9,
    )

    lowerer, primalizer, d_lowerer, d_primalizer = residual_maps(g0, h)
    identity = np.eye(lowerer.shape[0])
    eig_lowerer = np.linalg.eigvalsh(lowerer)
    computational(
        "b_res and R_res are inverse nondegenerate active residual maps with balanced (14,14) inertia",
        max_abs(primalizer @ lowerer - identity) < 1.0e-9
        and (int(np.sum(eig_lowerer > 1.0e-9)), int(np.sum(eig_lowerer < -1.0e-9))) == (14, 14),
    )
    computational(
        "the inverse variation obeys dR=-R(db)R",
        max_abs(d_primalizer + primalizer @ d_lowerer @ primalizer) < 2.0e-9,
    )
    eps = 2.0e-6
    lower_plus, primal_plus = residual_maps(g0 + eps * h)
    lower_minus, primal_minus = residual_maps(g0 - eps * h)
    computational(
        "the analytic moving Hodge/density/pseudo-musical derivatives match finite differences",
        max_abs((lower_plus - lower_minus) / (2.0 * eps) - d_lowerer) < 2.0e-6
        and max_abs((primal_plus - primal_minus) / (2.0 * eps) - d_primalizer) < 2.0e-6,
    )
    computational(
        "the active residual primalizer genuinely moves with the metric",
        np.linalg.norm(d_primalizer) > 1.0e-3 and np.linalg.norm(d_geometry) > 1.0e-3,
    )

    test_tensor = np.array(
        [[2.0, 1.0, 0.0, 0.0], [1.0, -1.0, 0.0, 0.0], [0.0, 0.0, 3.0, 0.0], [0.0, 0.0, 0.0, 4.0]]
    )
    computational(
        "four-dimensional trace reversal is an involution on Sym2",
        max_abs(trace_reverse(g0, trace_reverse(g0, test_tensor)) - test_tensor) < 1.0e-10,
    )
    computational(
        "the (9,5) one-form/thirteen-form Hodge parity is plus",
        (-1) ** (1 * 13 + 5) == 1 and (-1) ** (13 * 1 + 5) == 1,
    )

    rng = np.random.default_rng(2026080112)
    e = rng.integers(-3, 4, size=28).astype(float)
    de = rng.integers(-2, 3, size=28).astype(float)
    u = primalizer @ e
    direct_r = float(de @ u + 0.5 * e @ d_primalizer @ e)
    inverse_b = float(de @ u - 0.5 * u @ d_lowerer @ u)
    computational(
        "the moving residual square returns both DE and the inverse-pairing term with the required minus sign",
        abs(direct_r - inverse_b) < 1.0e-8
        and abs(0.5 * u @ d_lowerer @ u) > 1.0e-4,
        f"dI={direct_r:.10g}; moving-return={-0.5 * u @ d_lowerer @ u:.10g}",
    )
    eps_action = 1.0e-6
    _, rp = residual_maps(g0 + eps_action * h)
    _, rm = residual_maps(g0 - eps_action * h)
    ep = e + eps_action * de
    em = e - eps_action * de
    finite = (0.5 * ep @ rp @ ep - 0.5 * em @ rm @ em) / (2.0 * eps_action)
    computational(
        "the complete analytic variation matches direct finite differentiation of I2B",
        abs(finite - direct_r) < 2.0e-5,
        f"finite={finite:.10g}; analytic={direct_r:.10g}",
    )
    reject("freeze the active residual primalizer in the complete metric variation", abs(float(de @ u) - finite) < 1.0e-5)
    reject("use the lowerer b_res where the dual residual requires R_res", abs(float(e @ lowerer @ e) - float(e @ primalizer @ e)) < 1.0e-6)
    reject("change the inverse-pairing return to a plus sign", abs(direct_r - float(de @ u + 0.5 * u @ d_lowerer @ u)) < 1.0e-6)
    reject("a Euclidean positive form is the constructed active residual map", np.all(np.linalg.eigvalsh(lowerer) > 0.0))

    return g0, h


# ---------------------------------------------------------------------------
# Genuine one-dimensional integration by parts with the moving active R_res.


def polynomial_green_checks(g0: np.ndarray, h: np.ndarray) -> None:
    nodes, weights = np.polynomial.legendre.leggauss(24)
    xs = 0.5 * (nodes + 1.0)
    ws = 0.5 * weights
    carrier = np.zeros(28)
    carrier[0] = 1.0
    carrier[17] = 2.0
    coupling = 0.08

    def phi(x):
        return 1.0 + x - 0.5 * x * x

    def dphi(x):
        return 1.0 - x

    def ddphi(_x):
        return -1.0

    def variation(x):
        return 0.3 - 0.4 * x + 0.2 * x * x

    def dvariation(x):
        return -0.4 + 0.4 * x

    def a(x):
        return 1.0 + 0.25 * x

    def da(_x):
        return 0.25

    def c(x):
        return -0.2 + 0.3 * x

    def dc(_x):
        return 0.3

    def q_and_qphi(x):
        metric = g0 + coupling * phi(x) * h
        _b, r, _db, dr = residual_maps(metric, coupling * h)
        return float(carrier @ r @ carrier), float(carrier @ dr @ carrier)

    direct_values = []
    bulk_values = []
    frozen_values = []
    for x in xs:
        q, q_phi = q_and_qphi(float(x))
        residual = a(x) * dphi(x) + c(x) * phi(x)
        d_residual = a(x) * dvariation(x) + c(x) * variation(x)
        residual_prime = (
            da(x) * dphi(x) + a(x) * ddphi(x) + dc(x) * phi(x) + c(x) * dphi(x)
        )
        q_prime = q_phi * dphi(x)
        momentum_prime = (
            da(x) * q * residual
            + a(x) * q_prime * residual
            + a(x) * q * residual_prime
        )
        direct_values.append(d_residual * q * residual + 0.5 * residual**2 * q_phi * variation(x))
        bulk_values.append(
            variation(x)
            * (-momentum_prime + c(x) * q * residual + 0.5 * residual**2 * q_phi)
        )
        frozen_values.append(variation(x) * (-momentum_prime + c(x) * q * residual))

    direct = float(np.dot(ws, direct_values))
    bulk = float(np.dot(ws, bulk_values))
    frozen_bulk = float(np.dot(ws, frozen_values))

    def boundary_value(x):
        q, _q_phi = q_and_qphi(x)
        residual = a(x) * dphi(x) + c(x) * phi(x)
        return variation(x) * a(x) * q * residual

    boundary = boundary_value(1.0) - boundary_value(0.0)
    computational(
        "the differential moving-R model satisfies bulk formal-adjoint plus Green endpoint identity",
        abs(direct - (bulk + boundary)) < 2.0e-9 and abs(boundary) > 1.0e-4,
        f"direct={direct:.10g}; bulk={bulk:.10g}; boundary={boundary:.10g}",
    )
    reject("discard the nonzero Green endpoint term", abs(direct - bulk) < 1.0e-7)
    reject("omit the moving-primalizer return in the differential bulk equation", abs(direct - (frozen_bulk + boundary)) < 1.0e-7)

    eps = 2.0e-6

    def action(sign):
        values = []
        for x in xs:
            varied_phi = phi(x) + sign * eps * variation(x)
            varied_dphi = dphi(x) + sign * eps * dvariation(x)
            metric = g0 + coupling * varied_phi * h
            _b, r = residual_maps(metric)
            q = float(carrier @ r @ carrier)
            residual = a(x) * varied_dphi + c(x) * varied_phi
            values.append(0.5 * residual * q * residual)
        return float(np.dot(ws, values))

    finite = (action(1.0) - action(-1.0)) / (2.0 * eps)
    computational(
        "the bulk-plus-boundary result matches direct variation of the differential action",
        abs(finite - direct) < 2.0e-8,
        f"finite={finite:.10g}",
    )


# ---------------------------------------------------------------------------
# Active southeast fermion action, current, and graph return.


def southeast_action_checks() -> np.ndarray:
    gammas, p_plus, p_minus, beta, right_h, _c_plus = B2C10["active_objects"]()
    ell = (-11.0 / 16.0) * p_plus + (-33.0 / 32.0) * p_minus
    x_generator = gammas[0] @ gammas[1]
    observed = (0, 1, 2, 9)
    coefficients = np.array([0.7, -0.4, 0.9, 0.2])
    direction = np.array([-0.3, 0.8, 0.5, -0.6])
    rng = np.random.default_rng(2026080110)
    nu = rng.normal(size=128) + 1j * rng.normal(size=128)
    partner = right_h @ nu.conj()
    fields = (nu, partner)

    def action(coeffs, seed):
        fs = (seed, right_h @ seed.conj())
        total = 0.0
        for field in fs:
            for coefficient, index in zip(coeffs, observed):
                matrix = beta @ gammas[index] @ ell @ (coefficient * x_generator)
                total += float(np.real(field.conj() @ matrix @ field))
        return total

    current = np.array(
        [
            sum(
                float(np.real(field.conj() @ beta @ gammas[index] @ ell @ x_generator @ field))
                for field in fields
            )
            for index in observed
        ]
    )
    eps = 1.0e-6
    connection_finite = (action(coefficients + eps * direction, nu) - action(coefficients - eps * direction, nu)) / (2.0 * eps)
    computational(
        "the selected southeast fermion action emits its nonzero same-coefficient connection current",
        np.linalg.norm(current) > 1.0
        and abs(connection_finite - float(current @ direction)) < 2.0e-6,
        f"|J_SE|={np.linalg.norm(current):.9g}",
    )

    dnu = rng.normal(size=128) + 1j * rng.normal(size=128)
    fermion_finite = (action(coefficients, nu + eps * dnu) - action(coefficients, nu - eps * dnu)) / (2.0 * eps)
    expected = 0.0
    for field, dfield in ((nu, dnu), (partner, right_h @ dnu.conj())):
        for coefficient, index in zip(coefficients, observed):
            matrix = beta @ gammas[index] @ ell @ (coefficient * x_generator)
            expected += float(np.real(dfield.conj() @ matrix @ field + field.conj() @ matrix @ dfield))
    computational(
        "the constrained nu variation includes its direct term and induced right-H-partner contribution rather than a current-only amendment",
        abs(fermion_finite - expected) < 3.0e-5 and abs(expected) > 1.0,
    )

    # B_rot=u omega u^-1-u_i u^-1 at u=1,u_i=0.  This is the explicit local
    # graph owner used in B2C10, now paired with the action-derived current.
    rng_graph = np.random.default_rng(2026080111)
    metric_jets = rng_graph.normal(size=(4, 4, 4))
    metric_jets = 0.5 * (metric_jets + metric_jets.swapaxes(1, 2))
    omega = B2C10["lc_spin_lift"](metric_jets, gammas)
    current_rows = []
    for index in observed:
        coefficient = beta @ gammas[index] @ ell
        current_rows.append(
            sum(
                (coefficient.conj().T @ np.outer(field, field.conj()) for field in fields),
                np.zeros_like(beta),
            )
        )

    def connection_pair(items):
        return float(
            sum(
                np.real(np.trace(current_row.conj().T @ item))
                for current_row, item in zip(current_rows, items)
            )
        )

    delta_u = gammas[2] @ gammas[3]
    delta_ui = [(index + 1.0) * (gammas[4] @ gammas[5]) for index in range(4)]
    delta_b = [delta_u @ item - item @ delta_u - dui for item, dui in zip(omega, delta_ui)]
    direct_graph = connection_pair(delta_b)
    owner_u = sum(
        (
            (item @ row.conj().T - row.conj().T @ item).conj().T
            for item, row in zip(omega, current_rows)
        ),
        np.zeros_like(beta),
    )
    returned = float(np.real(np.trace(owner_u.conj().T @ delta_u)))
    returned += float(
        sum(
            np.real(np.trace((-row).conj().T @ dui))
            for row, dui in zip(current_rows, delta_ui)
        )
    )
    computational(
        "the action-derived current returns through the complete local B_rot reduction graph including d-epsilon",
        abs(direct_graph - returned) < 2.0e-8 and abs(returned) > 1.0,
        f"graph-return={returned:.9g}",
    )
    reject("append the southeast current while freezing its fermion slots", abs(fermion_finite) < 1.0e-7)
    reject("drop the B_rot graph owner return", abs(direct_graph) < 1.0e-7)
    return current


# ---------------------------------------------------------------------------
# Exact graph-owned staged comparator and current-completion rank audit.


Vector = tuple[F, ...]
Matrix = tuple[tuple[F, ...], ...]


def vadd(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right))


def vsub(left: Vector, right: Vector) -> Vector:
    return tuple(a - b for a, b in zip(left, right))


def vscale(value, vector: Vector) -> Vector:
    return tuple(F(value) * item for item in vector)


def vdot(left: Vector, right: Vector) -> F:
    return sum((a * b for a, b in zip(left, right)), F(0))


def mv(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum((matrix[i][j] * vector[j] for j in range(len(vector))), F(0))
        for i in range(len(matrix))
    )


def mtv(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum((matrix[i][j] * vector[i] for i in range(len(matrix))), F(0))
        for j in range(len(matrix[0]))
    )


def rational_owner_checks() -> None:
    hmat: Matrix = ((F(2), F(1)), (F(1), F(-1)))
    rmat: Matrix = ((F(0), F(1)), (F(2), F(0)))
    nmat: Matrix = ((F(1), F(0)), (F(0), F(2)))
    u0: Vector = (F(1), F(-1))
    v0: Vector = (F(0), F(1))
    a_field: Vector = (F(2), F(-1))
    b_rot: Vector = (F(1), F(1, 2))
    distortion = vsub(a_field, b_rot)
    residual = vadd(vadd(mv(hmat, distortion), mv(rmat, b_rot)), u0)
    direct_b = vadd(vadd(mtv(rmat, distortion), mv(nmat, b_rot)), v0)
    w_owner = vsub(direct_b, residual)
    r_res: Matrix = ((F(1), F(1, 2)), (F(1, 2), F(-3, 4)))
    d_r_res: Matrix = ((F(0), F(1)), (F(1), F(1)))
    primal = mv(r_res, residual)
    e_a = mtv(hmat, primal)
    e_epsilon = vdot(vscale(F(-1), mv(hmat, (F(1), F(0)))), primal)
    e_epsilon += vdot(mv(rmat, (F(1), F(0))), primal)
    e_g_without_dr = vdot(
        vadd(vscale(F(-1), mv(hmat, (F(0), F(1)))), mv(rmat, (F(0), F(1)))),
        primal,
    )
    e_g = e_g_without_dr + F(1, 2) * vdot(residual, mv(d_r_res, residual))
    computational(
        "the exact staged graph comparator returns independent A and graph-variable owners",
        e_a != (F(0), F(0)) and e_epsilon != 0 and e_g != 0 and w_owner != (F(0), F(0)),
        f"E_A={e_a}; E_epsilon={e_epsilon}; E_g={e_g}",
    )
    computational(
        "the exact graph-metric owner contains a nonzero one-half D R_res return",
        e_g - e_g_without_dr == F(1, 2) * vdot(residual, mv(d_r_res, residual))
        and e_g != e_g_without_dr,
    )

    def residual_at(a_value: Vector, epsilon: F, g_value: F) -> Vector:
        b_value = (epsilon, g_value)
        return vadd(
            vadd(mv(hmat, vsub(a_value, b_value)), mv(rmat, b_value)),
            u0,
        )

    def primalizer_at(g_value: F) -> Matrix:
        return tuple(
            tuple(r_res[i][j] + (g_value - F(1, 2)) * d_r_res[i][j] for j in range(2))
            for i in range(2)
        )

    def square_action(a_value: Vector, epsilon: F, g_value: F) -> F:
        e_value = residual_at(a_value, epsilon, g_value)
        return F(1, 2) * vdot(e_value, mv(primalizer_at(g_value), e_value))

    def shifted(direction_a: Vector, direction_epsilon: F, direction_g: F, scale: F):
        return (
            vadd(a_field, vscale(scale, direction_a)),
            b_rot[0] + scale * direction_epsilon,
            b_rot[1] + scale * direction_g,
        )

    def exact_cubic_direction(direction_a: Vector, direction_epsilon: F, direction_g: F) -> F:
        plus_1 = square_action(*shifted(direction_a, direction_epsilon, direction_g, F(1)))
        minus_1 = square_action(*shifted(direction_a, direction_epsilon, direction_g, F(-1)))
        plus_2 = square_action(*shifted(direction_a, direction_epsilon, direction_g, F(2)))
        minus_2 = square_action(*shifted(direction_a, direction_epsilon, direction_g, F(-2)))
        d1 = (plus_1 - minus_1) / F(2)
        d2 = (plus_2 - minus_2) / F(4)
        return (F(4) * d1 - d2) / F(3)

    arbitrary_a = (F(2, 3), F(-3, 5))
    arbitrary_epsilon = F(4, 7)
    arbitrary_g = F(-5, 6)
    expected_direction = (
        vdot(e_a, arbitrary_a)
        + e_epsilon * arbitrary_epsilon
        + e_g * arbitrary_g
    )
    computational(
        "direct exact differentiation of the composite residual-square action returns all A_tr, epsilon, and metric owners",
        exact_cubic_direction(arbitrary_a, arbitrary_epsilon, arbitrary_g)
        == expected_direction,
    )
    pure_r_direction_a = (F(-1, 3), F(2, 3))
    pure_r_derivative = exact_cubic_direction(pure_r_direction_a, F(0), F(1))
    pure_r_expected = F(1, 2) * vdot(residual, mv(d_r_res, residual))
    computational(
        "a pure moving-primalizer direction has D E_toy zero but a nonzero exact D R_res return",
        residual_at(
            vadd(a_field, pure_r_direction_a), b_rot[0], b_rot[1] + F(1)
        )
        == residual
        and pure_r_derivative == pure_r_expected
        and pure_r_expected != 0,
    )

    # A T-only term redistributes K but is in the kernel of diagonal/shared
    # pullback.  A true canceler must add the separate shared class L=-K.
    k: Vector = (F(2), F(-3), F(5))
    for transfer in (F(-1), F(0), F(1, 2), F(1), F(2)):
        j_a = vscale(transfer, k)
        j_b = vscale(F(1) - transfer, k)
        computational(
            f"T-only owner transfer q={transfer} preserves the shared southeast current",
            vadd(j_a, j_b) == k,
        )
    l = vscale(F(-1), k)
    computational(
        "shared cancellation requires a new diagonal class L=-K rather than a transfer coefficient",
        vadd(k, l) == (F(0), F(0), F(0)),
    )
    reject("q alone cancels the shared southeast current", any(vadd(vscale(q0, k), vscale(F(1) - q0, k)) == (F(0), F(0), F(0)) for q0 in (F(-1), F(0), F(1, 2), F(1), F(2))))


def completion_rank_checks(current: np.ndarray) -> None:
    normalized = current / np.linalg.norm(current)
    trial = np.eye(4)
    # Pick two artificial ambient-coordinate directions linearly independent
    # of K. They are deliberately not claimed to arise from an admissible
    # action.
    candidates = [normalized]
    for column in trial:
        if np.linalg.matrix_rank(np.column_stack(candidates + [column]), tol=1.0e-10) > len(candidates):
            candidates.append(column)
        if len(candidates) == 4:
            break
    design = np.column_stack(candidates[:3])
    held_out = candidates[3]
    computational(
        "the artificial ambient-coordinate rank fixture has three independent directions and a held-out fourth",
        np.linalg.matrix_rank(design, tol=1.0e-10) == 3
        and np.linalg.matrix_rank(np.column_stack([design, held_out]), tol=1.0e-10) == 4,
    )
    selected_action_constraint = np.array([[1.0, 0.0, 0.0]])
    type_level(
        "the hand-declared selected-action constraint has rank one in the artificial ambient-coordinate fixture",
        np.linalg.matrix_rank(selected_action_constraint) == 1
        and selected_action_constraint.shape[1] == 3,
        "no action-admissible compensator direction or coefficient is counted",
    )
    fitted = design @ np.linalg.lstsq(design, held_out, rcond=None)[0]
    reject("a permissive three-channel completion matcher fits the held-out fourth current", np.linalg.norm(fitted - held_out) < 1.0e-9)
    type_level(
        "global current-completion surplus is uncomputable at this gate",
        True,
        "the action fixes J_SE with zero new coefficient, but the complete admissible compensator alphabet is unknown",
    )


def scope_checks() -> None:
    type_level("I2B=||UpsilonB_src||^2 is manuscript-written; its density-dual R_res port is repository-typed and UpsilonB_src is not the selected G2 action's exact E_T_var")
    type_level("the scalar residual norm, spoken inter-layer DiracPair, and unreleased two-connection D-squared are three homonyms")
    type_level("A_tr, B_rot, and T=A_tr-B_rot replace unstable naked A/B source labels")
    type_level("J_9.18, the action-derived J_SE, and the observed four-dimensional Yang-Mills current are distinct")
    type_level("the staged I_ED followed by I2B packet is a conservative repository scaffold, not a source-displayed composite")
    type_level("the exact relative normalization between the reconstructed fermion action and I1B/I2B remains source-silent")
    type_level("the one-dimensional Green identity proves a local differential certificate, not a closed Y14 domain")
    type_level("the bosonic square raises Euler order and needs bosonic field plus conormal boundary data before mixed-domain replay")
    type_level("the active residual map is indefinite and supplies no coercivity, positive energy, unitarity, or global Cauchy theorem")
    type_level("the lower-right block and J_SE are conditional on the selected repository operator repair")
    type_level("no extra cyclic or compensating term is forced by this gate; completeness remains open")
    type_level("P1/P2/P3 supplies no residual map, current, action architecture, formal adjoint, owner, or domain")
    type_level("the active (9,5) right-H residual-map port is not the literal (7,7) U(64,64)-type manuscript arena; Curt remains formally separate and TG-1 AND TG-2 AND TG-3 remains false")


def main() -> int:
    print("ECW3D-B2C12 ACTIVE STAGED ACTION / MOVING RESIDUAL PRIMALIZER")
    source_checks()
    g0, h = active_pairing_checks()
    polynomial_green_checks(g0, h)
    current = southeast_action_checks()
    rational_owner_checks()
    completion_rank_checks(current)
    scope_checks()
    total = COMPUTATIONAL + SOURCE_RECEIPTS + TYPE_LEVEL + PLANTED
    print(
        f"SUMMARY: {COMPUTATIONAL} computational + {SOURCE_RECEIPTS} source receipts + "
        f"{TYPE_LEVEL} type-level + {PLANTED} planted = {total}",
        flush=True,
    )
    if FAILURES:
        print("FAILED: " + "; ".join(FAILURES), flush=True)
        return 1
    print("ALL B2C12 CHECKS PASS", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
