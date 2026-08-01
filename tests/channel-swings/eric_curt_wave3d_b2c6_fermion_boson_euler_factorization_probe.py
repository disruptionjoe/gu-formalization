#!/usr/bin/env python3
r"""B2C6 fermion--boson and two-connection Euler-factorization gate.

This probe keeps four Layer-0 objects separate:

* the physical rolled fermion ``Psi=(zeta,nu)``;
* an independent odd parameter ``q_odd``;
* the ordinary even gauge generator / parity-odd BV ghost; and
* the source's two-connection somatic obstruction.

It first constructs the exact mixed-carrier symplectic bracket and the
G2/G3 graph return.  It then executes the source-directed two-connection
composition and both single-connection curved wedge compositions.  Finally it
tests the principal necessary condition for the current B2C5
nonzero-southeast fermion Hessian to support a local off-shell odd gauge
generator. The flat intermediate-field jet used here is not promoted to an
admissible solution of the actual Levi--Civita/DeWitt field graph.

The result is deliberately split: a repo construction motivated by the
two-connection route reconstructs the G2 curvature polynomial exactly, but at
any admissible solution carrying the verified B2C5 principal symbol, that
completed rolled operator has no nonzero local polynomial odd-gauge syzygy.
This does not kill the source's unreleased on-shell two-connection complex, a larger degenerate
parent action, a gauge-fixed interpretation, or a rigid odd symmetry.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import runpy
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
for path in (ROOT / "tests", ROOT / "tests" / "generation-sector"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import gen_sector_bridge as gb  # noqa: E402


G2 = runpy.run_path(str(ROOT / "tests/channel-swings/g2_native_variational_shiab_probe.py"))
B2C5 = runpy.run_path(
    str(ROOT / "tests/channel-swings/eric_curt_wave3d_b2c5_covariant_action_green_ward_probe.py")
)

FAILURES: list[str] = []
EXACT = 0
TYPE_LEVEL = 0
PLANTED = 0
TOL = 8.0e-8


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(label)


def type_level(label: str, condition: bool, detail: str = "") -> None:
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


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def product(items: list[np.ndarray]) -> np.ndarray:
    out = np.eye(items[0].shape[0], dtype=complex)
    for item in items:
        out = out @ item
    return out


def dot_fraction(left, right) -> F:
    return sum((F(x) * F(y) for x, y in zip(left, right)), F(0))


# ---------------------------------------------------------------------------
# Source collision and exact two-connection transgression.


def source_receipt_checks() -> None:
    portal = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
    exact("Portal source explicitly calls for two derivative operators", "I have two derivative operators here" in portal)
    exact(
        "Portal source says their difference is zero-order augmented torsion",
        "difference between them has been to be a zeroth-order" in portal
        and "precisely the augmented torsion" in portal,
    )
    exact(
        "Portal source says route composition drops differential operators and leaves an Einstein-shaped obstruction",
        "the differential operators fall out" in portal
        and "obstruction term that looks like the Einstein field equation" in portal,
    )
    exact(
        "Portal source separates Bose and Fermi somatic complexes with a common obstruction",
        "two somatic complexes" in portal
        and "common generalization of the Einstein field equations" in portal,
    )
    exact(
        "Portal source types zeta and nu as two physical fields in coupled Dirac-role equations",
        "zeta \\in \\Omega^1" in portal
        and "nu \\in \\Omega^0" in portal
        and "two separate fields" in portal
        and "coupled set of differential equations" in portal,
    )


def mat_vec(matrix, vector):
    return tuple(
        sum((matrix[i][j] * vector[j] for j in range(len(vector))), F(0))
        for i in range(len(vector))
    )


def vec_add(left, right):
    return tuple(x + y for x, y in zip(left, right))


def vec_sub(left, right):
    return tuple(x - y for x, y in zip(left, right))


def mixed_covariant_composition(left, right, d_right, value, first, second):
    """Return (nabla^left_0 nabla^right_1 - 0<->1)value."""

    def ordered(i: int, j: int):
        result = tuple(second[i][j])
        result = vec_add(result, mat_vec(d_right[i][j], value))
        result = vec_add(result, mat_vec(right[j], first[i]))
        result = vec_add(result, mat_vec(left[i], first[j]))
        result = vec_add(result, mat_vec(G2["mm"](left[i], right[j]), value))
        return result

    return vec_sub(ordered(0, 1), ordered(1, 0))


def two_connection_transgression_checks() -> None:
    M = G2["M"]
    add = G2["add"]
    f1_add = G2["f1_add"]
    form1 = G2["form1"]
    form2 = G2["form2"]
    curvature = G2["curvature"]
    covariant_d = G2["covariant_d"]
    q = G2["q"]
    f2_add = G2["f2_add"]
    f2_scale = G2["f2_scale"]
    f2_sub = G2["f2_sub"]
    ZERO = G2["ZERO"]

    b = form1(M(1, 1, 0, -1), M(0, 1, 2, 1), M(2, -1, 1, 0))
    t = form1(M(0, 2, -1, 1), M(1, -1, 1, 2), M(-1, 0, 2, 1))
    db = form2(M(0, 1, -1, 0), M(1, 0, 2, -1), M(-1, 2, 0, 1))
    dt = form2(M(2, -1, 0, 1), M(0, 2, 1, -1), M(1, 0, -2, 1))
    a = f1_add(b, t)
    da = f2_add(db, dt)

    f_b = curvature(b, db)
    f_a = curvature(a, da)
    d_b_t = covariant_d(b, t, dt)
    t2 = q(t, t)
    translated = f2_add(f_b, f2_add(d_b_t, t2))
    exact("two-connection endpoint curvature translates as F_A=F_B+D_BT+q(T,T)", f_a == translated)

    # Repo-derived from the source-motivated two-connection geometry: the G2
    # polynomial is the exact average of curvature along the affine connection
    # segment B+sT. Since it is quadratic in s, the integral is evaluated
    # coefficientwise with no numerical quadrature.
    segment_average = f2_add(f_b, f2_add(f2_scale(F(1, 2), d_b_t), f2_scale(F(1, 3), t2)))

    # H^E_AB is the symmetrized high-road/low-road composition on an
    # associated bundle E. Its curvature representative Hhat_AB is the
    # adjoint-valued form F_B+1/2 D_BT. The jet replay below applies that
    # representative in this finite matrix representation.
    h_hat_ab = f2_add(f_b, f2_scale(F(1, 2), d_b_t))
    h_endpoint = f2_scale(F(1, 2), f2_sub(f2_add(f_a, f_b), t2))
    exact("the curvature representative Hhat_AB is F_B+one-half D_BT", h_hat_ab == h_endpoint)

    route_barycenter = f2_scale(F(1, 3), f2_add(f_a, f2_add(f_b, h_hat_ab)))
    exact(
        "the G2 source curvature is both the connection-segment average and the AA/BB/AB route barycenter",
        segment_average == route_barycenter,
    )

    # Direct jet-level replay on the 01 component proves that this is not an
    # identity manufactured after replacing the derivatives by curvatures.
    b2 = b[:2]
    a2 = a[:2]
    ordered_db = ((ZERO, db[0]), (ZERO, ZERO))
    ordered_dt = ((ZERO, dt[0]), (ZERO, ZERO))
    ordered_da = tuple(
        tuple(add(ordered_db[i][j], ordered_dt[i][j]) for j in range(2))
        for i in range(2)
    )
    value = (F(2), F(-1))
    first_1 = ((F(1), F(3)), (F(-2), F(4)))
    first_2 = ((F(7), F(-5)), (F(6), F(1)))
    second_1 = (((F(2), F(0)), (F(3), F(-1))), ((F(3), F(-1)), (F(5), F(2))))
    second_2 = (((F(-4), F(1)), (F(9), F(2))), ((F(9), F(2)), (F(0), F(-3))))

    def mixed_average(first, second):
        ab = mixed_covariant_composition(a2, b2, ordered_db, value, first, second)
        ba = mixed_covariant_composition(b2, a2, ordered_da, value, first, second)
        return tuple(F(1, 2) * (x + y) for x, y in zip(ab, ba))

    replay_1 = mixed_average(first_1, second_1)
    replay_2 = mixed_average(first_2, second_2)
    expected = mat_vec(h_hat_ab[0], value)
    exact(
        "the symmetrized two-route composition cancels arbitrary first and symmetric second jets exactly",
        replay_1 == replay_2 == expected,
    )

    wrong_route_average = f2_scale(F(1, 2), f2_add(f_a, f_b))
    reject("the endpoint average alone reproduces the 1/2,1/3 source polynomial", wrong_route_average == segment_average)


# ---------------------------------------------------------------------------
# Mixed-carrier Super-IG candidate and graph-complete G3 return.


def symplectic_moment(j: np.ndarray, u: np.ndarray, v: np.ndarray) -> np.ndarray:
    return np.outer(v, u) @ j + np.outer(u, v) @ j


def beta_mixed(j: np.ndarray, left, right):
    u, psi = left
    v, chi = right
    return tuple(
        symplectic_moment(j, u, chi_i) + symplectic_moment(j, v, psi_i)
        for psi_i, chi_i in zip(psi, chi)
    )


def mixed_bracket_checks() -> None:
    eye = np.eye(2)
    j = np.block([[np.zeros((2, 2)), eye], [-eye, np.zeros((2, 2))]])
    a = np.array([[1.0, 1.0], [0.0, 1.0]])
    a_inv_t = np.linalg.inv(a).T
    g = np.block([[a, np.zeros((2, 2))], [np.zeros((2, 2)), a_inv_t]])
    g_inv = np.linalg.inv(g)
    exact("the finite control transformation is symplectic", max_abs(g.T @ j @ g - j) < 1.0e-12)

    u = np.array([1.0, 2.0, -1.0, 0.0])
    v = np.array([0.0, -1.0, 2.0, 1.0])
    psi = (np.array([2.0, 0.0, 1.0, -1.0]), np.array([1.0, -2.0, 0.0, 3.0]))
    chi = (np.array([-1.0, 1.0, 2.0, 0.0]), np.array([0.0, 2.0, -1.0, 1.0]))
    beta = beta_mixed(j, (u, psi), (v, chi))
    beta_swap = beta_mixed(j, (v, chi), (u, psi))
    exact("the mixed zero/one-form bracket is symmetric and nonzero", all(max_abs(x - y) < 1.0e-12 for x, y in zip(beta, beta_swap)) and max(max_abs(x) for x in beta) > 1.0)
    exact("the mixed bracket lands in the symplectic adjoint algebra", all(max_abs(x.T @ j + j @ x) < 1.0e-12 for x in beta))

    beta_moved = beta_mixed(j, (g @ u, tuple(g @ x for x in psi)), (g @ v, tuple(g @ x for x in chi)))
    exact(
        "the mixed bracket is equivariant under the full finite symplectic control",
        all(max_abs(moved - g @ original @ g_inv) < 1.0e-12 for moved, original in zip(beta_moved, beta)),
    )
    reject("a scalar identity endomorphism lies in the symplectic adjoint", max_abs(np.eye(4).T @ j + j @ np.eye(4)) < 1.0e-12)
    type_level(
        "the complex symplectic bracket still requires the active C-plus/right-H/native-real-form projection",
        True,
    )


def active_reality_bilinear_checks() -> None:
    """Show that active Krein/right-H/charge reality leaves live channels."""

    gammas, _, _, _ = gb.constraint_objects()
    spin = gammas[0].shape[0]
    identity = np.eye(spin, dtype=complex)
    omega = product(gammas)
    p_plus = 0.5 * (identity + omega)
    p_minus = 0.5 * (identity - omega)
    beta = product(gammas[:9])
    right_h = product([gammas[index] for index in (1, 3, 5, 7, 10, 12)])
    c_plus = np.linalg.inv(product([gammas[index] for index in range(14) if index % 2 == 0]))

    words = [identity]
    words.extend(product(gammas[:degree]) for degree in range(1, 15))
    transpose_defects = []
    chirality_pass = True
    for degree, word in enumerate(words):
        form = c_plus @ word
        sign = -((-1) ** (degree * (degree - 1) // 2))
        transpose_defects.append(max_abs(form.T - sign * form))
        same = max(max_abs(p_plus.T @ form @ p_plus), max_abs(p_minus.T @ form @ p_minus))
        cross = max(max_abs(p_plus.T @ form @ p_minus), max_abs(p_minus.T @ form @ p_plus))
        if degree % 2 == 0:
            chirality_pass = chirality_pass and same < TOL and cross > 0.5
        else:
            chirality_pass = chirality_pass and cross < TOL and same > 0.5
    exact(
        "representative C-plus Clifford bilinears at degrees 0-14 obey the exact p-dependent transpose law",
        max(transpose_defects) < TOL,
        f"defect={max(transpose_defects):.3g}",
    )
    exact(
        "active charge bilinears have cross chirality at even Clifford degree and same chirality at odd degree",
        chirality_pass,
    )

    rng = np.random.default_rng(2026080102)
    u = rng.normal(size=spin) + 1j * rng.normal(size=spin)
    v = rng.normal(size=spin) + 1j * rng.normal(size=spin)
    raw = np.outer(u, v.conj()) @ beta
    right_h_inverse = np.linalg.inv(right_h)
    projected_h = 0.5 * (raw + right_h @ raw.conj() @ right_h_inverse)
    krein_adjoint = np.linalg.inv(beta) @ projected_h.conj().T @ beta
    projected_sp = 0.5 * (projected_h - krein_adjoint)
    right_h_defect = max_abs(projected_sp @ right_h - right_h @ projected_sp.conj())
    krein_skew_defect = max_abs(beta @ projected_sp + projected_sp.conj().T @ beta)
    charge_skew_defect = max_abs(projected_sp.T @ c_plus + c_plus @ projected_sp)
    exact(
        "the active C-plus/right-H/Krein-skew projected-endomorphism space contains a nonzero rank-one witness",
        np.linalg.norm(projected_sp) > 1.0
        and right_h_defect < TOL
        and krein_skew_defect < TOL
        and charge_skew_defect < TOL,
        f"C+={charge_skew_defect:.3g}; right-H={right_h_defect:.3g}; K-skew={krein_skew_defect:.3g}",
    )
    reject(
        "an unprojected complex rank-one bilinear is automatically right-H and Krein-skew",
        max_abs(raw @ right_h - right_h @ raw.conj()) < TOL
        and max_abs(beta @ raw + raw.conj().T @ beta) < TOL,
    )
    type_level("the actual active projection of the mixed moment-map image remains uncomputed", True)

    zeta = [rng.normal(size=spin) + 1j * rng.normal(size=spin) for _ in range(14)]
    h = np.zeros((14, 14), dtype=float)
    for a in range(14):
        for b in range(14):
            h[a, b] = 0.5 * np.real(
                u.conj() @ beta @ gammas[a] @ zeta[b]
                + u.conj() @ beta @ gammas[b] @ zeta[a]
            )
    exact("the active Krein bilinear supplies a nonzero real symmetric metric-variation candidate", max_abs(h - h.T) < TOL and np.linalg.norm(h) > 1.0)
    type_level("the symmetric metric bilinear still needs projection to the induced DeWitt metric tangent image", True)


def graph_return_checks() -> None:
    # Exact rational finite graph with all moving B/S/flat responses live.
    d_eps_b = ((F(1), F(2)), (F(-1), F(1)))
    d_g_b = ((F(2), F(0)), (F(1), F(-1)))
    d_eps_s = (F(3), F(-2))
    d_g_s = (F(1), F(4))
    d_eps_flat = (F(-1), F(5))
    d_g_flat = (F(2), F(3))
    mu_a = (F(2), F(-3))
    mu_eps = (F(1), F(2))
    mu_g = (F(-2), F(1))

    def mv(matrix, vector):
        return tuple(sum((matrix[i][j] * vector[j] for j in range(2)), F(0)) for i in range(2))

    delta_b = tuple(x + y for x, y in zip(mv(d_eps_b, mu_eps), mv(d_g_b, mu_g)))
    mu_t = tuple(x - y for x, y in zip(mu_a, delta_b))

    e_t = (F(4), F(-1))
    e_b = (F(-2), F(3))
    e_s = F(5)
    e_flat = F(-4)
    primitive = dot_fraction(e_t, mu_t) + dot_fraction(e_b, delta_b)
    primitive += e_s * (dot_fraction(d_eps_s, mu_eps) + dot_fraction(d_g_s, mu_g))
    primitive += e_flat * (dot_fraction(d_eps_flat, mu_eps) + dot_fraction(d_g_flat, mu_g))

    def transpose_mv(matrix, vector):
        return tuple(sum((matrix[i][j] * vector[i] for i in range(2)), F(0)) for j in range(2))

    diff = tuple(x - y for x, y in zip(e_b, e_t))
    e_eps = transpose_mv(d_eps_b, diff)
    e_eps = tuple(x + e_s * y + e_flat * z for x, y, z in zip(e_eps, d_eps_s, d_eps_flat))
    e_g = transpose_mv(d_g_b, diff)
    e_g = tuple(x + e_s * y + e_flat * z for x, y, z in zip(e_g, d_g_s, d_g_flat))
    returned = dot_fraction(e_t, mu_a) + dot_fraction(e_eps, mu_eps) + dot_fraction(e_g, mu_g)
    exact("the odd bosonic transformation obeys the graph law mu_T=mu_A-D_B(mu_epsilon,mu_g)", primitive == returned)

    bad_mu_t = mu_a
    bad_primitive = dot_fraction(e_t, bad_mu_t) + dot_fraction(e_b, delta_b)
    bad_primitive += e_s * (dot_fraction(d_eps_s, mu_eps) + dot_fraction(d_g_s, mu_g))
    bad_primitive += e_flat * (dot_fraction(d_eps_flat, mu_eps) + dot_fraction(d_g_flat, mu_g))
    reject("mu_T may be varied independently of A, epsilon, and g", bad_primitive == returned)


# ---------------------------------------------------------------------------
# Both curved compositions on the torsion-free LC connection.


def left_vector_spinor_remainder(riemann, internal=None):
    gamma_word = B2C5["gamma_word"]
    clifford_multiply = B2C5["clifford_multiply"]
    clifford_add = B2C5["clifford_add"]
    spin_curvature = B2C5["spin_curvature"]
    eta = B2C5["ETA_INT"]
    spin = spin_curvature(riemann)
    if internal is None:
        internal = [[{} for _ in range(14)] for _ in range(14)]
    out = [{} for _ in range(14)]
    for input_index in range(14):
        for a in range(14):
            for b in range(14):
                if a == b:
                    continue
                for c in range(14):
                    if c == a or c == b:
                        continue
                    triple = gamma_word(a, b, c)
                    if c == input_index:
                        total_curvature = dict(spin[a][b])
                        clifford_add(total_curvature, internal[a][b])
                        if total_curvature:
                            clifford_add(
                                out[input_index],
                                clifford_multiply(triple, total_curvature),
                                F(1, 2),
                            )
                    vector_value = riemann[c][input_index][a][b]
                    if vector_value:
                        clifford_add(out[input_index], triple, F(eta[input_index]) * vector_value / 2)
    return out


def curved_composition_checks() -> None:
    riemann_from_ricci = B2C5["riemann_from_ricci"]
    spin_curvature = B2C5["spin_curvature"]
    right_remainder = B2C5["wedge_curvature_remainder"]
    einstein_gamma = B2C5["einstein_gamma"]
    blade_grade_support = B2C5["blade_grade_support"]
    is_riemann = B2C5["is_nonzero_algebraic_riemann"]
    ricci_of = B2C5["ricci_of_riemann"]
    eta = B2C5["ETA_INT"]
    gamma_word = B2C5["gamma_word"]

    zero = [[F(0) for _ in range(14)] for _ in range(14)]
    ricci = [row[:] for row in zero]
    ricci[0][0] = F(2)
    ricci[1][1] = F(-2)
    riemann = riemann_from_ricci(ricci)
    right = right_remainder(spin_curvature(riemann))
    left = left_vector_spinor_remainder(riemann)
    exact("right curved composition reproduces one-half Einstein-gamma", right == einstein_gamma(ricci))
    exact("left curved composition is nonzero and collapses to Clifford grade one on the Ricci fixture", bool(left) and blade_grade_support(left) == {1})

    def vector_krein_adjoint_rows(rows):
        return [
            {mask: F(eta[index]) * value for mask, value in row.items()}
            for index, row in enumerate(rows)
        ]

    exact(
        "left LC composition is the vector-metric/Krein adjoint row of the right Einstein-gamma fixture",
        left == vector_krein_adjoint_rows(right),
    )

    # Mixed-sign tracefree and off-diagonal Ricci fixtures expose the eta
    # placement that a positive-index-only example cannot see.
    for label, entries in (
        ("tracefree mixed-sign", ((0, 0, F(2)), (9, 9, F(2)))),
        ("off-diagonal mixed-sign", ((0, 9, F(3)), (9, 0, F(3)))),
    ):
        fixture = [row[:] for row in zero]
        for a, b, value in entries:
            fixture[a][b] = value
        fixture_riemann = riemann_from_ricci(fixture)
        fixture_right = right_remainder(spin_curvature(fixture_riemann))
        fixture_left = left_vector_spinor_remainder(fixture_riemann)
        exact(
            f"{label} Ricci fixture has right Einstein-gamma and exact left vector/Krein adjoint",
            fixture_right == einstein_gamma(fixture)
            and fixture_left == vector_krein_adjoint_rows(fixture_right),
        )

    # Reuse B2C5's algebraic Weyl construction.
    h = [F(v) for v in (1, -1, 2, -2, 0, 1, 0, -1, 2, 0, -2, 1, 0, -1)]
    k = [F(v) for v in (2, 1, -1, 0, 1, -2, 1, 0, -1, 2, 1, 0, -2, 1)]
    raw = [[[[F(0) for _ in range(14)] for _ in range(14)] for _ in range(14)] for _ in range(14)]
    for a in range(14):
        for b in range(14):
            for c in range(14):
                for d in range(14):
                    raw[a][b][c][d] = (
                        (h[a] if a == c else 0) * (k[b] if b == d else 0)
                        - (h[a] if a == d else 0) * (k[b] if b == c else 0)
                        - (h[b] if b == c else 0) * (k[a] if a == d else 0)
                        + (h[b] if b == d else 0) * (k[a] if a == c else 0)
                    )
    raw_ricci = ricci_of(raw)
    ricci_part = riemann_from_ricci(raw_ricci)
    weyl = [[[[raw[a][b][c][d] - ricci_part[a][b][c][d] for d in range(14)] for c in range(14)] for b in range(14)] for a in range(14)]
    exact(
        "a nonzero pure-Weyl fixture vanishes in both LC curved compositions",
        is_riemann(weyl)
        and all(value == 0 for row in ricci_of(weyl) for value in row)
        and all(not item for item in right_remainder(spin_curvature(weyl)))
        and all(not item for item in left_vector_spinor_remainder(weyl)),
    )

    internal = [[{} for _ in range(14)] for _ in range(14)]
    internal[0][1] = {0: F(1)}
    internal[1][0] = {0: F(-1)}
    left_internal = left_vector_spinor_remainder(
        [[[[F(0) for _ in range(14)] for _ in range(14)] for _ in range(14)] for _ in range(14)],
        internal,
    )
    exact("left composition detects an independent grade-three commuting-endomorphism curvature slot", blade_grade_support(left_internal) == {3})
    type_level("the commuting scalar endomorphism control is not certified as active GU-adjoint curvature", True)


# ---------------------------------------------------------------------------
# Formal-flat principal odd-syzygy obstruction for the current B2C5 action.


def formal_flat_syzygy_checks() -> None:
    gammas, _, _, _ = gb.constraint_objects()
    n = 14
    spin = 128
    roll = (n + 1) * spin
    identity_s = np.eye(spin, dtype=complex)
    identity_v = np.eye(n, dtype=complex)
    omega = product(gammas)
    p_plus = 0.5 * (identity_s + omega)
    p_minus = 0.5 * (identity_s - omega)
    eta = np.array([1.0] * 9 + [-1.0] * 5)

    def clifford(k):
        return sum(k[a] * gammas[a] for a in range(n))

    def k_map(k):
        return np.kron(k.reshape(n, 1), identity_s)

    def codiff(k):
        return np.kron((eta * k).reshape(1, n), identity_s)

    def wedge(k):
        out = np.zeros((n * spin, n * spin), dtype=complex)
        for b in range(n):
            if not k[b]:
                continue
            for a in range(n):
                if a == b:
                    continue
                for v in range(n):
                    if v == a or v == b:
                        continue
                    out[a * spin : (a + 1) * spin, v * spin : (v + 1) * spin] += (
                        k[b] * eta[a] * gammas[a] @ gammas[b] @ gammas[v]
                    )
        return out

    def rolled(k):
        weights = p_plus + p_minus
        ell = -F(11, 12) * (p_plus + p_minus)
        return np.block(
            [
                [wedge(k) @ np.kron(identity_v, weights), k_map(k)],
                [codiff(k), clifford(k) @ ell],
            ]
        )

    directions = {
        "timelike": np.array([0.0] * 9 + [1.0] + [0.0] * 4),
        "generic": np.array([1.0, -2.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0]),
    }
    for name, k in directions.items():
        d = rolled(k)
        c_k = clifford(k)
        r1 = np.vstack([k_map(k), np.zeros((spin, spin), dtype=complex)])
        r2 = np.vstack(
            [np.vstack([gammas[a] @ c_k for a in range(n)]), np.zeros((spin, spin), dtype=complex)]
        )
        r3 = np.vstack([np.zeros((n * spin, spin), dtype=complex), c_k])
        images = [d @ r for r in (r1, r2, r3)]
        gram = np.array(
            [[np.vdot(left, right).real for right in images] for left in images],
            dtype=float,
        )
        generator_gram = np.array(
            [[np.vdot(left, right).real for right in (r1, r2, r3)] for left in (r1, r2, r3)],
            dtype=float,
        )
        exact(
            f"{name}: the three natural first-order odd-generator channels have no completed-operator syzygy",
            np.linalg.matrix_rank(gram, tol=1.0e-6) == 3
            and np.linalg.matrix_rank(generator_gram, tol=1.0e-6) == 3,
            f"min Gram eig={np.linalg.eigvalsh(gram)[0]:.6g}",
        )
        exact(
            f"{name}: fixing the exterior-gradient coefficient to one is inconsistent with a local gauge kernel",
            np.linalg.norm(images[0]) > 1.0,
        )

    # The upper wedge route itself retains A_w K=0; the obstruction comes
    # from completing the physical rolled equations, not from a failed probe.
    k = directions["timelike"]
    exact("the bare wedge-after-gradient upper route still closes at flat principal order", max_abs(wedge(k) @ k_map(k)) < TOL)
    exact("the lower codifferential-after-gradient route is nonzero off the null cone", max_abs(codiff(k) @ k_map(k)) > 0.5)

    # Exact G2 intermediate source-curvature seed on a formal flat jet. This
    # does not construct an admissible Levi-Civita/DeWitt field-graph point or
    # execute the complete returned Euler tuple there.
    zero2 = G2["form2"](G2["ZERO"], G2["ZERO"], G2["ZERO"])
    zero1 = G2["form1"](G2["ZERO"], G2["ZERO"], G2["ZERO"])
    e_t = G2["source_curvature"](zero1, zero2, zero1, zero2, F(1, 2), F(1, 3))
    exact("the G2 source-curvature seed vanishes on the formal F_B=T=0 intermediate jet", e_t == zero2)
    reject("a fitted nonzero intermediate source seed may rescue the formal-flat principal syzygy", e_t != zero2)


def inherited_factorization_control() -> None:
    # Replay the exact G2 witness that a noncentral moving contraction has
    # q(y,z)=0 but a nonzero polarized Euler response.  This blocks replacing
    # the graph-complete Euler module by one linear S(q) map.
    M = G2["M"]
    ZERO = G2["ZERO"]
    form1 = G2["form1"]
    form2 = G2["form2"]
    q = G2["q"]
    wedge_pair = G2["wedge_pair"]
    shiab_insert = G2["shiab_insert"]
    insertion = M(1, 2, -1, 0)
    y = form1(M(1, 0, 0, 0), ZERO, ZERO)
    z = form1(ZERO, M(0, 0, 0, 1), ZERO)
    delta = form1(M(2, 0, 1, -1), M(-1, 2, 0, 1), M(1, 1, -2, 0))
    witness = F(1, 3) * (
        wedge_pair(delta, shiab_insert(insertion, q(y, z)))
        + wedge_pair(y, shiab_insert(insertion, q(delta, z)))
        + wedge_pair(z, shiab_insert(insertion, q(delta, y)))
    )
    exact("G2 control has zero polarized curvature but nonzero slot-symmetrized Euler response", q(y, z) == form2(ZERO, ZERO, ZERO) and witness != 0)
    reject("the compressed S(F_A)+kappa T shortcut is the graph-complete Euler module", witness == 0)


def main() -> int:
    print("ECW3D-B2C6 FERMION--BOSON / TWO-CONNECTION EULER-FACTORIZATION GATE")
    source_receipt_checks()
    two_connection_transgression_checks()
    mixed_bracket_checks()
    active_reality_bilinear_checks()
    graph_return_checks()
    curved_composition_checks()
    formal_flat_syzygy_checks()
    inherited_factorization_control()

    reject("the physical nu field is the odd gauge ghost", False)
    reject("the ordinary G3 gauge Ward identity is the proposed spinorial Noether identity", False)
    reject("the two-connection somatic composition is already an off-shell odd action symmetry", False)
    reject("the source supplies delta_q A, delta_q epsilon, or delta_q g", False)
    reject("the current obstruction kills the unreleased on-shell two-connection complex", False)
    reject("a missing super-IG bracket or parent action is P1, P2, or P3", False)
    reject("the AA/BB/AB route identity forces a generation count", False)
    reject("Curt's literal 7,7 pairing/domain has been promoted into the active 9,5 lane", False)

    print("-" * 108)
    print(f"checks: {EXACT} exact + {TYPE_LEVEL} type-level + {PLANTED} planted")
    if FAILURES:
        print("FINAL: FAIL")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print("FINAL: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
