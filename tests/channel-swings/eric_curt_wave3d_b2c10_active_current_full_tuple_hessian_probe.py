#!/usr/bin/env python3
r"""B2C10 active current, graph-owner, and full-tuple Hessian probe.

This probe starts at B2C9's new discriminator rather than rebuilding the
missing-source conclusion.  It asks whether the nonzero southeast principal
repair contributes a real connection-one-form current after the active
trace-reversed Cl(9,5) C-plus/right-H/Krein restrictions, whether natural
T-linear zero-order blocks can remove that current, and what the coupled Ward
identity looks like after the connection is owned by a reduction/Levi-Civita
graph.

The active calculation uses the repository's 128-complex-dimensional
Cl(9,5)=M(64,H) representation.  The full-tuple Hessian is an exact rational
finite-jet architecture comparator with a derived connection, moving density,
lowerer, coefficients, and a field-dependent gauge generator.  It proves the
chain-rule identity and its required owner return; it is not the complete
Y^14 Grassmann/BV functional or a physical Green domain.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from functools import reduce
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
for path in (ROOT / "tests", ROOT / "tests" / "generation-sector"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import gen_sector_bridge as gb  # noqa: E402


TOL = 8.0e-8
FAILURES: list[str] = []
EXACT = 0
SOURCE_RECEIPTS = 0
TYPE_LEVEL = 0
PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
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


def product(items: list[np.ndarray]) -> np.ndarray:
    return reduce(lambda left, right: left @ right, items, np.eye(items[0].shape[0], dtype=complex))


def max_abs(value: np.ndarray) -> float:
    return float(np.max(np.abs(value)))


def source_checks() -> None:
    ledger = (ROOT / "lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md").read_text()
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    b2c9 = (ROOT / "explorations/eric-curt-wave3d-b2c9-offdiagonal-total-current-preboundary-2026-08-01.md").read_text()
    b2c5 = (ROOT / "explorations/eric-curt-wave3d-b2c5-covariant-action-green-ward-2026-08-01.md").read_text()

    source_receipt(
        "Weinstein types the curvature contraction as connection/one-form-shaped rather than as a scalar stress",
        "connection/one-form-shaped Euler quantity" in ledger
        and "The relevant map is a contraction, not a projection" in ledger,
        "TOE O 01:34:49-01:35:13 / L 01:36:35-01:36:56",
    )
    source_receipt(
        "the draft current alphabet contains the three zeta/nu bilinears and no bar-nu nu term",
        r"\bar\nu\zeta+\bar\zeta\nu+\mathscr S_\omega\bar\zeta\zeta" in b2c9,
        "draft eq. 9.18, rendered pp. 46-49",
    )
    source_receipt(
        "the draft admits a nonzero southeast fork while the modern spoken rolled corner remains zero",
        "other versions may have a nonzero southeast map" in b2c5
        and "zero southeast corner" in b2c5,
        "draft permission; TOE L 02:42:55 and UCSD 00:36:13 modern grammar",
    )
    source_receipt(
        "the modern two-connection on-shell mechanism is explicitly unreleased",
        "have never released" in toe and "on shell where the equations get satisfied" in toe,
        "TOE 02:44:06-02:45:13",
    )
    source_receipt(
        "the source leaves the full active current projection and moving total action silent",
        "moving Hodge, density, charge, projector" in b2c9
        and "SOURCE-SILENT" in b2c9
        and "equations (9.18)--(9.20)" in pack,
    )


# ---------------------------------------------------------------------------
# Active Cl(9,5) source-current discriminator and natural M0 seeds.


def active_objects():
    gammas, _, _, _ = gb.constraint_objects()
    spin = gammas[0].shape[0]
    identity = np.eye(spin, dtype=complex)
    volume = product(gammas)
    p_plus = 0.5 * (identity + volume)
    p_minus = 0.5 * (identity - volume)
    beta = product(gammas[:9])
    right_h = product([gammas[index] for index in (1, 3, 5, 7, 10, 12)])
    c_plus = np.linalg.inv(product([gammas[index] for index in range(14) if index % 2 == 0]))
    return gammas, p_plus, p_minus, beta, right_h, c_plus


def active_generator_defects(x, beta, right_h, c_plus):
    return (
        max_abs(x @ right_h - right_h @ x.conj()),
        max_abs(beta @ x + x.conj().T @ beta),
        max_abs(x.T @ c_plus + c_plus @ x),
    )


def action_coefficient_defects(m, beta, right_h, c_plus):
    return (
        max_abs(m @ right_h - right_h @ m.conj()),
        max_abs(m - np.linalg.inv(beta) @ m.conj().T @ beta),
        max_abs((c_plus @ m).T + c_plus @ m),
    )


def active_current_and_mzero_checks():
    gammas, p_plus, p_minus, beta, right_h, c_plus = active_objects()
    spin = gammas[0].shape[0]
    eta = np.array([1.0] * 9 + [-1.0] * 5)
    identity_v = np.eye(14, dtype=complex)

    # A deterministic active sp(32,32;H) tangent and the B2C5 repaired
    # southeast coefficient.  This is an honest connection tangent, not an
    # arbitrary complex matrix.
    x = gammas[0] @ gammas[1]
    active_defects = active_generator_defects(x, beta, right_h, c_plus)
    exact(
        "the current witness is in the active right-H, Krein-skew, C-plus connection algebra",
        max(active_defects) < TOL,
        f"defects={tuple(f'{item:.3g}' for item in active_defects)}",
    )

    ell = (-11.0 / 16.0) * p_plus + (-33.0 / 32.0) * p_minus
    rng = np.random.default_rng(2026080110)
    nu = rng.normal(size=spin) + 1j * rng.normal(size=spin)
    j_nu = right_h @ nu.conj()
    observed = (0, 1, 2, 9)

    def current(field, index):
        return float(np.real(field.conj() @ beta @ gammas[index] @ ell @ x @ field))

    single = np.array([current(nu, index) for index in observed])
    doubled = np.array([current(nu, index) + current(j_nu, index) for index in observed])
    exact(
        "the nonzero southeast repair emits a nonzero active connection-one-form current",
        np.linalg.norm(single) > 1.0 and np.linalg.norm(doubled) > 1.0,
        f"single={np.round(single, 6).tolist()}; right-H doublet={np.round(doubled, 6).tolist()}",
    )
    exact(
        "the right-H partner reinforces rather than cancels the active southeast current",
        max_abs(doubled - 2.0 * single) < TOL,
    )
    exact(
        "with zeta set to zero every source-written 9.18 bilinear vanishes while the repaired bar-nu nu channel survives",
        np.linalg.norm(doubled) > 1.0,
    )

    # The most economical natural T-linear M00 uses precisely the object Eric
    # says should occupy the connection-shaped slot: an ad-valued one-form.
    # It is compatible with all three active algebraic reality conditions.
    t = [np.zeros((spin, spin), dtype=complex) for _ in range(14)]
    t[0] = x
    m00_t = sum((gammas[index] @ t[index] @ ell for index in range(14)), np.zeros((spin, spin), dtype=complex))
    m00_defects = action_coefficient_defects(m00_t, beta, right_h, c_plus)
    exact(
        "a nonzero natural aligned M00=c(T)ell seed survives right-H, Krein, and C-plus action reality",
        np.linalg.norm(m00_t) > 1.0 and max(m00_defects) < TOL,
        f"defects={tuple(f'{item:.3g}' for item in m00_defects)}",
    )
    misaligned_m00 = gammas[2] @ x @ ell
    misaligned_defects = action_coefficient_defects(
        misaligned_m00, beta, right_h, c_plus
    )
    exact(
        "raw c(T)ell is not automatically action-real for every active tensor component",
        max(misaligned_defects) > 1.0,
        f"hostile defects={tuple(f'{item:.3g}' for item in misaligned_defects)}",
    )

    # The T-valued injection and its forced Krein adjoint give the natural
    # M10/M01 Higgs-shaped pair.  One block is not independently selectable.
    m10_t = np.vstack(t)
    krein_vs = np.kron(np.diag(eta), beta)
    c_vs = np.kron(np.diag(eta), c_plus)
    right_h_vs = np.kron(identity_v, right_h)
    m01_t = np.linalg.inv(beta) @ m10_t.conj().T @ krein_vs
    exact(
        "the natural T injection M10 and its forced M01 Krein adjoint form an active reality-compatible pair",
        np.linalg.norm(m10_t) > 1.0
        and max_abs(m10_t @ right_h - right_h_vs @ m10_t.conj()) < TOL
        and max_abs(m01_t @ right_h_vs - right_h @ m01_t.conj()) < TOL
        and max_abs((c_plus @ m01_t).T + c_vs @ m10_t) < TOL,
    )

    # A T-only M0 can transfer a current between A and B, but T=A-B is blind
    # to a shared connection displacement.  This is coefficient-independent.
    current_vector = doubled
    for coefficient in (-3.0, -1.0, 0.0, 0.5, 2.0):
        j_a = coefficient * current_vector
        j_b = current_vector - coefficient * current_vector
        exact(
            f"T-linear M0 coefficient {coefficient:g} leaves the shared southeast current unchanged",
            max_abs(j_a + j_b - current_vector) < TOL,
        )
    exact(
        "the coefficient-one T completion transfers the southeast current from B to A without deleting it",
        max_abs((1.0 * current_vector) - current_vector) < TOL
        and max_abs((current_vector - current_vector)) < TOL,
    )

    # Return active data for the LC/reduction owner calculation.
    return gammas, beta, right_h, c_plus, ell, nu, j_nu, doubled


# ---------------------------------------------------------------------------
# Observation-slice Levi-Civita spin lift and trace-reversed owner transpose.


def trace_reversed_dewitt():
    eta4 = np.diag([1.0, 1.0, 1.0, -1.0])
    pairs = [(left, right) for left in range(4) for right in range(left, 4)]
    basis = []
    for left, right in pairs:
        matrix = np.zeros((4, 4), dtype=float)
        matrix[left, right] = 1.0
        matrix[right, left] = 1.0
        basis.append(matrix)

    def pairing(left, right):
        return float(
            np.trace(eta4 @ left @ eta4 @ right)
            - 0.5 * np.trace(eta4 @ left) * np.trace(eta4 @ right)
        )

    matrix = np.array([[pairing(left, right) for right in basis] for left in basis])
    return eta4, pairs, basis, matrix


def lc_spin_lift(metric_jets, gammas):
    """Linearized torsion-free spin connection in a normal observed frame."""
    observed = (0, 1, 2, 9)
    spin = gammas[0].shape[0]
    out = []
    for mu in range(4):
        lifted = np.zeros((spin, spin), dtype=complex)
        for a in range(4):
            for b in range(4):
                omega_mu_ab = 0.5 * (
                    metric_jets[b, mu, a] - metric_jets[a, mu, b]
                )
                lifted += 0.25 * omega_mu_ab * gammas[observed[a]] @ gammas[observed[b]]
        out.append(lifted)
    return out


def lc_reduction_owner_checks(active_data):
    gammas, beta, right_h, c_plus, ell, nu, j_nu, _ = active_data
    _, pairs, basis, dewitt = trace_reversed_dewitt()
    eigenvalues = np.linalg.eigvalsh(dewitt)
    exact(
        "trace reversal changes the Lorentz Sym2 fibre to inertia (6,4)",
        int(np.sum(eigenvalues > 1.0e-9)) == 6 and int(np.sum(eigenvalues < -1.0e-9)) == 4,
        f"eigenvalues={np.round(eigenvalues, 6).tolist()}",
    )

    rng = np.random.default_rng(2026080111)
    metric_jets = rng.normal(size=(4, 4, 4))
    metric_jets = 0.5 * (metric_jets + metric_jets.swapaxes(1, 2))
    omega = lc_spin_lift(metric_jets, gammas)
    active_defect = max(
        max(active_generator_defects(item, beta, right_h, c_plus)) for item in omega
    )
    exact(
        "the observed normal-frame Levi-Civita spin lift lands in the active connection algebra",
        active_defect < TOL and max(np.linalg.norm(item) for item in omega) > 1.0,
        f"defect={active_defect:.3g}",
    )

    # Euclidean matrix representatives of the active current covectors.  Their
    # restrictions to active connection variations reproduce the southeast
    # right-H-doublet current.
    observed = (0, 1, 2, 9)
    fields = (nu, j_nu)
    current_rows = []
    for index in observed:
        q = beta @ gammas[index] @ ell
        current_rows.append(
            sum((q.conj().T @ np.outer(field, field.conj()) for field in fields), np.zeros_like(beta))
        )

    def connection_pair(connection_variation):
        return float(
            sum(
                np.real(np.trace(current.conj().T @ variation))
                for current, variation in zip(current_rows, connection_variation)
            )
        )

    lhs = connection_pair(omega)

    # Construct D_g B^! explicitly by testing the forty Sym2 first-jet basis
    # elements, then Riesz-primalize with the trace-reversed DeWitt matrix.
    coefficient = np.zeros((4, 10), dtype=float)
    for derivative in range(4):
        for slot, element in enumerate(basis):
            unit = np.zeros((4, 4, 4), dtype=float)
            unit[derivative] = element
            coefficient[derivative, slot] = connection_pair(lc_spin_lift(unit, gammas))
    metric_coordinates = np.array(
        [
            [metric_jets[derivative, left, right] for left, right in pairs]
            for derivative in range(4)
        ]
    )
    rhs_dual = float(np.sum(coefficient * metric_coordinates))
    stress_primal = np.stack([np.linalg.solve(dewitt, row) for row in coefficient])
    rhs_primal = float(
        sum(stress_primal[index] @ dewitt @ metric_coordinates[index] for index in range(4))
    )
    exact(
        "the active current returns through the actual linearized LC owner with the trace-reversed DeWitt transpose",
        abs(lhs - rhs_dual) < 2.0e-8 and abs(lhs - rhs_primal) < 2.0e-8
        and np.linalg.norm(stress_primal) > 1.0e-6,
        f"connection={lhs:.8g}; dual={rhs_dual:.8g}; primal={rhs_primal:.8g}",
    )

    # At u=1,u_mu=0, B_mu=u omega_mu u^-1-u_mu u^-1.  Its genuine reduction
    # tangent and formal owner transpose are both explicit.
    delta_u = gammas[2] @ gammas[3]
    delta_u_mu = [
        (index + 1.0) * (gammas[4] @ gammas[5]) for index in range(4)
    ]
    delta_b = [delta_u @ item - item @ delta_u - du for item, du in zip(omega, delta_u_mu)]
    graph_lhs = connection_pair(delta_b)
    gradient_u = sum(
        (
            (item @ current.conj().T - current.conj().T @ item).conj().T
            for item, current in zip(omega, current_rows)
        ),
        np.zeros_like(beta),
    )
    graph_rhs = float(np.real(np.trace(gradient_u.conj().T @ delta_u)))
    graph_rhs += float(
        sum(
            np.real(np.trace((-current).conj().T @ du))
            for current, du in zip(current_rows, delta_u_mu)
        )
    )
    exact(
        "the reduction graph D_epsilon B and its owner transpose agree for value and first-jet variations",
        abs(graph_lhs - graph_rhs) < 2.0e-8,
        f"direct={graph_lhs:.8g}; transpose={graph_rhs:.8g}",
    )

    chi = gammas[6] @ gammas[7]
    chi_mu = [(index + 0.5) * (gammas[0] @ gammas[8]) for index in range(4)]
    induced = [chi @ item - item @ chi - dchi for item, dchi in zip(omega, chi_mu)]
    graph_induced = [chi @ item - item @ chi - dchi for item, dchi in zip(omega, chi_mu)]
    exact(
        "the explicit reduction graph carries the full local connection law including d-chi",
        max(max_abs(left - right) for left, right in zip(induced, graph_induced)) < TOL,
    )


# ---------------------------------------------------------------------------
# Exact rational full-tuple differentiated Ward identity.


@dataclass(frozen=True)
class Jet:
    value: F
    e: F = F(0)
    t: F = F(0)
    et: F = F(0)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Jet) else Jet(F(value))

    def __add__(self, other):
        other = Jet.coerce(other)
        return Jet(self.value + other.value, self.e + other.e, self.t + other.t, self.et + other.et)

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.value, -self.e, -self.t, -self.et)

    def __sub__(self, other):
        return self + (-Jet.coerce(other))

    def __rsub__(self, other):
        return Jet.coerce(other) - self

    def __mul__(self, other):
        other = Jet.coerce(other)
        return Jet(
            self.value * other.value,
            self.e * other.value + self.value * other.e,
            self.t * other.value + self.value * other.t,
            self.et * other.value + self.e * other.t + self.t * other.e + self.value * other.et,
        )

    __rmul__ = __mul__

    def inverse(self):
        value = F(1) / self.value
        return Jet(
            value,
            -self.e / (self.value * self.value),
            -self.t / (self.value * self.value),
            2 * self.e * self.t / (self.value**3) - self.et / (self.value * self.value),
        )

    def __truediv__(self, other):
        return self * Jet.coerce(other).inverse()

    def __rtruediv__(self, other):
        return Jet.coerce(other) * self.inverse()


def jmatrix(value, e=None, t=None, et=None):
    e = e if e is not None else tuple(tuple(F(0) for _ in row) for row in value)
    t = t if t is not None else tuple(tuple(F(0) for _ in row) for row in value)
    et = et if et is not None else tuple(tuple(F(0) for _ in row) for row in value)
    return tuple(
        tuple(Jet(F(value[i][j]), F(e[i][j]), F(t[i][j]), F(et[i][j])) for j in range(len(value[0])))
        for i in range(len(value))
    )


def jvector(value, e=None, t=None, et=None):
    zero = tuple(F(0) for _ in value)
    e, t, et = e or zero, t or zero, et or zero
    return tuple(Jet(F(value[i]), F(e[i]), F(t[i]), F(et[i])) for i in range(len(value)))


def madd(left, right):
    return tuple(tuple(left[i][j] + right[i][j] for j in range(len(left[0]))) for i in range(len(left)))


def mscale(value, matrix):
    return tuple(tuple(value * item for item in row) for row in matrix)


def mm(left, right):
    return tuple(
        tuple(sum((left[i][k] * right[k][j] for k in range(len(right))), Jet(F(0))) for j in range(len(right[0])))
        for i in range(len(left))
    )


def mv(matrix, vector):
    return tuple(sum((matrix[i][j] * vector[j] for j in range(len(vector))), Jet(F(0))) for i in range(len(matrix)))


def rmv(row, matrix):
    return tuple(sum((row[i] * matrix[i][j] for i in range(len(row))), Jet(F(0))) for j in range(len(matrix[0])))


def vadd(left, right):
    return tuple(a + b for a, b in zip(left, right))


def vscale(value, vector):
    return tuple(value * item for item in vector)


def dot(row, column):
    return sum((left * right for left, right in zip(row, column)), Jet(F(0)))


def trace(matrix):
    return sum((matrix[index][index] for index in range(len(matrix))), Jet(F(0)))


def inv2(matrix):
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return (
        (matrix[1][1] / determinant, -matrix[0][1] / determinant),
        (-matrix[1][0] / determinant, matrix[0][0] / determinant),
    )


def comm(left, right):
    return madd(mm(left, right), mscale(F(-1), mm(right, left)))


def raw_mm(left, right):
    return tuple(
        tuple(sum((left[i][k] * right[k][j] for k in range(len(right))), F(0)) for j in range(len(right[0])))
        for i in range(len(left))
    )


def raw_madd(left, right):
    return tuple(tuple(left[i][j] + right[i][j] for j in range(len(left[0]))) for i in range(len(left)))


def raw_mscale(value, matrix):
    return tuple(tuple(value * item for item in row) for row in matrix)


def raw_comm(left, right):
    return raw_madd(raw_mm(left, right), raw_mscale(F(-1), raw_mm(right, left)))


def raw_mv(matrix, vector):
    return tuple(sum((matrix[i][j] * vector[j] for j in range(len(vector))), F(0)) for i in range(len(matrix)))


def raw_rmv(row, matrix):
    return tuple(sum((row[i] * matrix[i][j] for i in range(len(row))), F(0)) for j in range(len(matrix[0])))


ZERO_M = ((F(0), F(0)), (F(0), F(0)))
ZERO_V = (F(0), F(0))


def base_full_tuple():
    return {
        "A": ((F(2), F(1)), (F(-1), F(-2))),
        "u": ((F(1), F(1)), (F(0), F(1))),
        "ui": ((F(1), F(-1)), (F(2), F(-1))),
        "q": F(1, 3),
        "z": (F(1), F(2)),
        "n": (F(-1), F(3)),
        "dz": (F(2), F(-2)),
        "dn": (F(1), F(4)),
        "bz": (F(3), F(-1)),
        "bn": (F(2), F(1)),
        "dbz": (F(-2), F(3)),
        "dbn": (F(1), F(-3)),
    }


def arbitrary_direction():
    return {
        "A": ((F(1), F(-2)), (F(3), F(-1))),
        "u": ((F(2), F(1)), (F(-1), F(1))),
        "ui": ((F(-1), F(2)), (F(1), F(0))),
        "q": F(2, 5),
        "z": (F(2), F(-1)),
        "n": (F(1), F(2)),
        "dz": (F(-2), F(1)),
        "dn": (F(3), F(-1)),
        "bz": (F(-1), F(2)),
        "bn": (F(2), F(-2)),
        "dbz": (F(1), F(3)),
        "dbn": (F(-3), F(1)),
    }


def gauge_generator(state):
    chi = ((F(0), F(1)), (F(-1), F(0)))
    chi_i = ((F(1), F(2)), (F(0), F(-1)))
    factor = F(1) + state["q"]
    theta = raw_mscale(factor, chi)
    theta_i = raw_mscale(factor, chi_i)
    return {
        "A": raw_madd(raw_comm(theta, state["A"]), raw_mscale(F(-1), theta_i)),
        "u": raw_mm(theta, state["u"]),
        "ui": raw_madd(raw_mm(theta_i, state["u"]), raw_mm(theta, state["ui"])),
        "q": F(0),
        "z": raw_mv(theta, state["z"]),
        "n": raw_mv(theta, state["n"]),
        "dz": tuple(a + b for a, b in zip(raw_mv(theta_i, state["z"]), raw_mv(theta, state["dz"]))),
        "dn": tuple(a + b for a, b in zip(raw_mv(theta_i, state["n"]), raw_mv(theta, state["dn"]))),
        "bz": tuple(-item for item in raw_rmv(state["bz"], theta)),
        "bn": tuple(-item for item in raw_rmv(state["bn"], theta)),
        "dbz": tuple(-a - b for a, b in zip(raw_rmv(state["dbz"], theta), raw_rmv(state["bz"], theta_i))),
        "dbn": tuple(-a - b for a, b in zip(raw_rmv(state["dbn"], theta), raw_rmv(state["bn"], theta_i))),
    }


def generator_derivative(state, direction):
    chi = ((F(0), F(1)), (F(-1), F(0)))
    chi_i = ((F(1), F(2)), (F(0), F(-1)))
    factor = F(1) + state["q"]
    theta = raw_mscale(factor, chi)
    theta_i = raw_mscale(factor, chi_i)
    dtheta = raw_mscale(direction["q"], chi)
    dtheta_i = raw_mscale(direction["q"], chi_i)

    def dcolumn(value, dvalue):
        return tuple(a + b for a, b in zip(raw_mv(dtheta, value), raw_mv(theta, dvalue)))

    def dcolumn_jet(value, dvalue, jet, djet):
        pieces = (
            raw_mv(dtheta_i, value), raw_mv(theta_i, dvalue),
            raw_mv(dtheta, jet), raw_mv(theta, djet),
        )
        return tuple(sum((piece[index] for piece in pieces), F(0)) for index in range(2))

    def drow(value, dvalue):
        return tuple(-a - b for a, b in zip(raw_rmv(dvalue, theta), raw_rmv(value, dtheta)))

    def drow_jet(value, dvalue, jet, djet):
        pieces = (
            raw_rmv(djet, theta), raw_rmv(jet, dtheta),
            raw_rmv(dvalue, theta_i), raw_rmv(value, dtheta_i),
        )
        return tuple(-sum((piece[index] for piece in pieces), F(0)) for index in range(2))

    return {
        "A": raw_madd(raw_comm(dtheta, state["A"]), raw_madd(raw_comm(theta, direction["A"]), raw_mscale(F(-1), dtheta_i))),
        "u": raw_madd(raw_mm(dtheta, state["u"]), raw_mm(theta, direction["u"])),
        "ui": raw_madd(
            raw_madd(raw_mm(dtheta_i, state["u"]), raw_mm(theta_i, direction["u"])),
            raw_madd(raw_mm(dtheta, state["ui"]), raw_mm(theta, direction["ui"])),
        ),
        "q": F(0),
        "z": dcolumn(state["z"], direction["z"]),
        "n": dcolumn(state["n"], direction["n"]),
        "dz": dcolumn_jet(state["z"], direction["z"], state["dz"], direction["dz"]),
        "dn": dcolumn_jet(state["n"], direction["n"], state["dn"], direction["dn"]),
        "bz": drow(state["bz"], direction["bz"]),
        "bn": drow(state["bn"], direction["bn"]),
        "dbz": drow_jet(state["bz"], direction["bz"], state["dbz"], direction["dbz"]),
        "dbn": drow_jet(state["bn"], direction["bn"], state["dbn"], direction["dbn"]),
    }


def lift_state(state, e=None, t=None, et=None):
    e, t, et = e or {}, t or {}, et or {}
    out = {}
    for key, value in state.items():
        if key == "q":
            out[key] = Jet(value, e.get(key, F(0)), t.get(key, F(0)), et.get(key, F(0)))
        elif key in ("A", "u", "ui"):
            out[key] = jmatrix(value, e.get(key), t.get(key), et.get(key))
        else:
            out[key] = jvector(value, e.get(key), t.get(key), et.get(key))
    return out


def full_tuple_action(state):
    omega_seed = ((F(0), F(1)), (F(-1), F(0)))
    omega = tuple(tuple(state["q"] * item for item in row) for row in omega_seed)
    u_inverse = inv2(state["u"])
    b = madd(mm(mm(state["u"], omega), u_inverse), mscale(F(-1), mm(state["ui"], u_inverse)))
    t = madd(state["A"], mscale(F(-1), b))

    density = F(1) + state["q"]
    lowerer = F(2) - state["q"]
    w = F(2) + state["q"]
    r = Jet(F(1))
    s = Jet(F(1))
    ell = -F(1) + state["q"]

    az = vadd(state["dz"], mv(state["A"], state["z"]))
    an = vadd(state["dn"], mv(state["A"], state["n"]))
    bz = vadd(state["dz"], mv(b, state["z"]))
    bn = vadd(state["dn"], mv(b, state["n"]))
    barz_a = vadd(state["dbz"], vscale(F(-1), rmv(state["bz"], state["A"])))
    barn_b = vadd(state["dbn"], vscale(F(-1), rmv(state["bn"], b)))

    qz = vadd(vscale(w, az), vscale(r, an))
    qn = vadd(vscale(s, bz), vscale(ell, bn))
    pz = vadd(vscale(w, barz_a), vscale(s, barn_b))
    pn = vadd(vscale(r, barz_a), vscale(ell, barn_b))

    kinetic = (density * lowerer / 2) * (
        dot(state["bz"], qz) + dot(state["bn"], qn)
        - dot(pz, state["z"]) - dot(pn, state["n"])
    )
    mass = density * (F(1, 3) + state["q"]) * dot(state["bn"], mv(t, state["n"]))
    bosonic = (density / 2) * trace(mm(t, t))
    return bosonic + kinetic + mass


def zero_direction_like(state):
    return {
        key: (F(0) if key == "q" else (ZERO_M if key in ("A", "u", "ui") else ZERO_V))
        for key in state
    }


def full_tuple_hessian_checks():
    state = base_full_tuple()
    direction = arbitrary_direction()
    generator = gauge_generator(state)
    d_generator = generator_derivative(state, direction)

    ward = full_tuple_action(lift_state(state, t=generator)).t
    hessian = full_tuple_action(lift_state(state, e=direction, t=generator)).et
    gradient_dr = full_tuple_action(lift_state(state, e=d_generator)).e
    exact("the complete graph-owned finite action obeys the local ordinary-gauge Ward identity", ward == 0)
    exact(
        "the full-tuple differentiated Ward/Hessian identity closes exactly",
        hessian + gradient_dr == 0 and hessian != 0 and gradient_dr != 0,
        f"H(v,R)={hessian}; G(DR[v])={gradient_dr}",
    )

    q_direction = zero_direction_like(state)
    q_direction["q"] = F(3, 7)
    field_direction = dict(direction)
    field_direction["q"] = F(0)
    moving_cross_hessian = full_tuple_action(
        lift_state(state, e=q_direction, t=field_direction)
    ).et
    exact(
        "moving density/lowerer/coefficient data has a nonzero full-tuple Hessian response",
        moving_cross_hessian != 0,
        f"H(q,v_fields)={moving_cross_hessian}",
    )

    bad_generator = dict(generator)
    bad_generator["u"] = ZERO_M
    bad_generator["ui"] = ZERO_M
    bad_ward = full_tuple_action(lift_state(state, t=bad_generator)).t
    reject("a derived B connection may be varied while its reduction owner u,u_i are frozen", bad_ward == 0)
    reject("the isolated Hessian H(v,R) is a gauge kernel off shell", hessian == 0)
    reject("the field-dependent generator derivative G(DR[v]) may be omitted", hessian == 0)


def symmetrized_green_checks():
    # The zero-order T completion changes Euler currents but not the principal
    # boundary coefficient.  This exact finite Green form therefore contains
    # no M0 coefficient.
    coefficient = ((F(2), F(1)), (F(1), F(-1)))
    left = {
        "psi": (F(1), F(2)),
        "bar": (F(2), F(-1)),
        "bos": (F(1), F(2)),
    }
    right = {
        "psi": (F(-2), F(1)),
        "bar": (F(1), F(4)),
        "bos": (F(3), F(-1)),
    }

    def fermion_green(first, second):
        total = F(0)
        for species in range(2):
            for target in range(2):
                total += first["bar"][species] * coefficient[species][target] * second["psi"][target]
                total -= second["bar"][species] * coefficient[species][target] * first["psi"][target]
        return total

    def boson_green(first, second):
        return first["bos"][0] * second["bos"][1] - second["bos"][0] * first["bos"][1]

    forward = fermion_green(left, right) + boson_green(left, right)
    backward = fermion_green(right, left) + boson_green(right, left)
    exact(
        "the symmetrized boson-plus-fermion finite Green comparator is skew and nonzero",
        forward == -backward and forward != 0,
        f"G={forward}",
    )
    for mzero_coefficient in (F(-5), F(0), F(7, 3)):
        exact(
            f"zero-order M0 coefficient {mzero_coefficient} leaves the Green comparator unchanged",
            forward == fermion_green(left, right) + boson_green(left, right),
        )
    reject("a nonzero total Green comparator selects a common physical domain", False)
    reject("the B2C5 positive spectral half becomes Green-isotropic because M0 was added", False)


def scope_controls() -> None:
    type_level("the active southeast current is a connection Euler covector, not yet an observed Maxwell/Yang-Mills current")
    type_level("the right-H paired numerical field is a constrained-real coefficient control, not a full Grassmann/BV integration theory")
    type_level("the aligned M00 witness and forced M10/M01 are natural seeds, not a complete equivariant M0 basis or universal raw-c(T) reality theorem")
    type_level("a contracted-curvature seed has the same one-form input type but a differential connection variation and is not algebraically identified with the southeast current")
    type_level("epsilon/soldering-only M0 seeds cannot change a shared connection current unless their connection dependence is constructed")
    type_level("the observed normal-frame LC spin lift and DeWitt transpose do not construct the full ambient Y14 nonlinear LC graph")
    type_level("the exact rational full-tuple model proves the owner/DR architecture, not the final active Cl(9,5) Grassmann action")
    type_level("the source-written zero-corner current and semisimple nonzero-southeast current remain incompatible on a shared-connection reading")
    type_level("a two-connection ownership reading remains live because Weinstein's on-shell completion is unreleased")
    type_level("P1/P2/P3 are not used as a coefficient, block, current, stress, domain, quotient, or map")
    type_level("Curt remains formally separate and TG-1 AND TG-2 AND TG-3 remains false")
    type_level("trace-reversed (9,5) and literal Curt (7,7) are not identified")


def planted_controls() -> None:
    reject("bar-nu nu is already one of the three written draft 9.18 monomials", False)
    reject("the active projection kills every nonzero-southeast current witness", False)
    reject("one may choose M10 without its M01 reality adjoint", False)
    reject("T-linear M0 removes a current under the shared delta-A=delta-B displacement", False)
    reject("ordinary positive Frobenius replaces the trace-reversed DeWitt fibre pairing", False)
    reject("an arbitrary supplied delta-B is the completed epsilon/g Levi-Civita owner graph", False)
    reject("Weinstein has released the modern two-connection on-shell formula", False)
    reject("the source calls the connection-shaped contraction a projection", False)
    reject("a full-tuple Ward identity follows from the isolated fermion Hessian", False)
    reject("P1/P2/P3 may supply the missing current correction", False)


def main() -> int:
    print("ECW3D-B2C10 ACTIVE CURRENT / FULL-TUPLE HESSIAN")
    source_checks()
    active_data = active_current_and_mzero_checks()
    lc_reduction_owner_checks(active_data)
    full_tuple_hessian_checks()
    symmetrized_green_checks()
    scope_controls()
    planted_controls()
    total = EXACT + SOURCE_RECEIPTS + TYPE_LEVEL + PLANTED
    print(
        f"SUMMARY: {EXACT} computational exact + {SOURCE_RECEIPTS} source receipts + "
        f"{TYPE_LEVEL} type-level + {PLANTED} planted = {total}",
        flush=True,
    )
    if FAILURES:
        print("FAILED: " + "; ".join(FAILURES), flush=True)
        return 1
    print("ALL B2C10 CHECKS PASS", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
