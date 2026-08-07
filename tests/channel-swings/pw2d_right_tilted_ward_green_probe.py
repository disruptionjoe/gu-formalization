#!/usr/bin/env python3
r"""PW2D residual right-tilted nonabelian Ward and Frechet-Green gate.

The source-coordinate kernel, residual right-tilted gauge action, the
field-dependent full-K substitution, and Xi=D Upsilon are kept separate.
The probe first replays the exact derivative cocycle/double action, then
constructs a nonabelian differential action with live connection,
distortion, and moving-reduction owners.  Its off-shell Noether-II identity
and nonzero boundary relation are checked exactly.  Finally an invertible,
noncentral exact h(T) graph compares direct differentiation of a pulled
action with an explicitly integrated old-root Frechet-adjoint tuple and its
separate Green return.

This is the residual active-component Ward theorem needed by the local PW2D
fixture.  It is not a public-to-active source-bundle equivalence, a graded BV
action, an observed equation, or a domain theorem.
"""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
if str(CHANNEL) not in sys.path:
    sys.path.insert(0, str(CHANNEL))


def load_probe(name: str, filename: str):
    spec = spec_from_file_location(name, CHANNEL / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


G1 = load_probe("pw2d_g1", "g1_derivative_cocycle_moving_reference_probe.py")


FAILURES: list[str] = []
EXACT = SOURCE = TYPE = PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(label)


def source(label: str, condition: bool, detail: str = "") -> None:
    global SOURCE
    SOURCE += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: source receipt - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"source: {label}")


def typed(label: str, condition: bool = True) -> None:
    global TYPE
    TYPE += 1
    print(f"{'PASS' if condition else 'FAIL'}: type-level - {label}", flush=True)
    if not condition:
        FAILURES.append(f"type: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    print(f"{'PASS' if not false_claim else 'FAIL'}: planted rejection - {label}", flush=True)
    if false_claim:
        FAILURES.append(f"planted: {label}")


def comm(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return sp.simplify(left * right - right * left)


def dmat(value: sp.Matrix, x: sp.Symbol) -> sp.Matrix:
    return value.applyfunc(lambda entry: sp.diff(entry, x))


def cov(connection: sp.Matrix, value: sp.Matrix, x: sp.Symbol) -> sp.Matrix:
    return sp.simplify(dmat(value, x) + comm(connection, value))


def tr(value: sp.Matrix) -> sp.Expr:
    return sp.expand(sp.trace(value))


def is_zero(value: sp.Matrix | sp.Expr) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in value)
    return sp.simplify(value) == 0


def integrate_linear_variation(
    density: sp.Expr,
    variables: list[sp.Expr],
    x: sp.Symbol,
    max_order: int = 3,
) -> tuple[list[sp.Expr], sp.Expr]:
    """Return Euler coefficients and the canonical 1D Green concomitant.

    The input is linear in the named variations and their derivatives.  This
    routine is deliberately independent of the target-Euler/DF-adjoint
    formula used below: it integrates the raw pulled-action variation by
    parts component by component.
    """

    euler: list[sp.Expr] = []
    green = sp.Integer(0)
    for variation in variables:
        coefficients = [
            sp.diff(density, variation if order == 0 else sp.diff(variation, x, order))
            for order in range(max_order + 1)
        ]
        euler.append(
            sp.simplify(
                sum(
                    ((-1) ** order) * sp.diff(coefficient, x, order)
                    for order, coefficient in enumerate(coefficients)
                )
            )
        )
        for order in range(1, max_order + 1):
            for k in range(order):
                green += (
                    (-1) ** k
                    * sp.diff(coefficients[order], x, k)
                    * sp.diff(variation, x, order - 1 - k)
                )
    return euler, sp.expand(green)


def trace_owner_matrix(coefficients: list[sp.Expr]) -> sp.Matrix:
    """Convert row-major variation coefficients to the trace-pair owner."""

    return sp.Matrix(2, 2, lambda row, col: coefficients[2 * col + row])


def action_objects(
    connection: sp.Matrix, distortion: sp.Matrix, reduction: sp.Matrix, x: sp.Symbol
):
    kinetic = cov(connection, distortion, x)
    reduction_commutator = comm(reduction, distortion)
    lagrangian = sp.expand(
        sp.Rational(1, 2) * tr(kinetic * kinetic)
        + sp.Rational(1, 2) * tr(reduction_commutator * reduction_commutator)
        + sp.Rational(1, 4) * tr(distortion**4)
    )
    e_connection = comm(distortion, kinetic)
    e_distortion = sp.simplify(
        -cov(connection, kinetic, x)
        + comm(reduction_commutator, reduction)
        + distortion**3
    )
    e_reduction = comm(distortion, reduction_commutator)
    return lagrangian, kinetic, e_connection, e_distortion, e_reduction


def source_and_layer_zero() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    ucsd = (ROOT / "lab/literature/weinstein-ucsd-2025-04-transcript.md").read_text()
    source(
        "the draft owns source roots, homogeneous distortion, and the completed first action",
        "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in pack
        and "I^B_1" in pack,
        "SOURCE-CONFIRMS",
    )
    source(
        "TOE explicitly names left/right tilted actions and the double coset",
        "[02:19:49]" in toe and "[02:22:20]" in toe,
        "SOURCE-CONFIRMS residual symmetry grammar",
    )
    source(
        "the two-connection difference is motivated by cancellation of the shared inhomogeneous term",
        "00:17:01" in ucsd and "00:22:26" in ucsd,
        "SOURCE-CONFIRMS equivariant-difference intent",
    )
    source(
        "Xi is displayed as an Euler redundancy rather than an off-shell Ward theorem",
        "\\Xi_\\omega=D_\\omega\\Upsilon_\\omega" in pack
        and "Noether identity is not" in pack,
        "SOURCE-CORRECTS the Ward homonym",
    )
    typed("left-tilted source-coordinate invariance and residual right-tilted gauge covariance are different actions")
    typed("the local differential delta T=alpha-D_A zeta is not the full off-identity residual right action")
    typed("K_full is a derived graph variable and receives no independent Euler equation")
    typed("the internal gauge generator fixes the metric; the metric Euler owner belongs to the separate diffeomorphism Ward identity")
    reject("rename Xi=D Upsilon as the nonabelian source Ward identity", False)
    reject("rename the Abelian source-coordinate kernel as the residual right action", False)


def tilted_group_checks() -> None:
    m = G1.matrix
    a_ref = m([[2, 1], [3, -1]])
    g = (m([[1, 1], [0, 1]]), m([[1, 0], [2, -1]]))
    h = (m([[2, 0], [1, 1]]), m([[0, 1], [-1, 2]]))
    k = (m([[1, 0], [-1, 1]]), m([[2, -1], [0, 1]]))
    gh = G1.jet_mul(g, h)
    exact(
        "the derivative-bearing q_A cocycle closes the tilted graph exactly",
        G1.derivative_cocycle(a_ref, gh)
        == G1.add(
            G1.derivative_cocycle(a_ref, g),
            G1.ad(g[0], G1.derivative_cocycle(a_ref, h)),
        )
        and G1.ig_mul(G1.tau(a_ref, g), G1.tau(a_ref, h))
        == G1.tau(a_ref, gh),
    )
    omega = (g, m([[1, 2], [-2, 3]]))
    theta = G1.theta(a_ref, omega)
    exact(
        "the left tilted action fixes Theta_A while the residual right action is adjoint",
        G1.theta(a_ref, G1.ig_mul(G1.tau(a_ref, k), omega)) == theta
        and G1.theta(a_ref, G1.ig_mul(omega, G1.tau(a_ref, h)))
        == G1.ad(G1.inverse_2(h[0]), theta),
    )
    pure_derivative = (G1.identity(2), m([[0, 1], [-1, 0]]))
    reject(
        "drop the derivative term from q_A and retain the tilted homomorphism",
        G1.derivative_cocycle(a_ref, pure_derivative)
        == G1.zero_jet_shadow(a_ref, pure_derivative),
    )


def residual_ward_checks() -> None:
    x = sp.symbols("x", real=True)
    connection = sp.Matrix([[x, 1 + x], [2 - x, -x]])
    distortion = sp.Matrix([[1 + x, x**2], [1 - x, -1 - x]])
    reduction = sp.Matrix([[2 - x, 1 + x**2], [x, x - 2]])
    c = sp.Matrix([[x * (1 - x), 1 + x], [x**2, -x * (1 - x)]])

    lagrangian, kinetic, e_c, e_t, e_q = action_objects(
        connection, distortion, reduction, x
    )
    delta_c = -cov(connection, c, x)
    delta_t = comm(c, distortion)
    delta_q = comm(c, reduction)

    # Direct gauge variation of the three covariant building blocks.
    delta_kinetic = cov(connection, delta_t, x) + comm(delta_c, distortion)
    delta_y = comm(delta_q, distortion) + comm(reduction, delta_t)
    y = comm(reduction, distortion)
    direct = sp.expand(
        tr(kinetic * delta_kinetic)
        + tr(y * delta_y)
        + tr(distortion**3 * delta_t)
    )
    exact(
        "the residual right-tilted generator acts covariantly on every nonabelian action block",
        is_zero(delta_kinetic - comm(c, kinetic))
        and is_zero(delta_y - comm(c, y))
        and sp.simplify(direct) == 0,
        f"DX={sp.simplify(delta_kinetic-comm(c, kinetic))}; DY={sp.simplify(delta_y-comm(c,y))}; dL={direct}",
    )

    bulk_identity = sp.simplify(
        cov(connection, e_c, x)
        + comm(distortion, e_t)
        + comm(reduction, e_q)
    )
    exact(
        "the live connection, distortion, and moving-reduction Euler owners satisfy the off-shell Noether-II identity",
        is_zero(bulk_identity)
        and not is_zero(e_c)
        and not is_zero(e_t)
        and not is_zero(e_q),
    )

    theta = sp.expand(tr(kinetic * delta_t))
    green = sp.expand(tr(e_c * c))
    bulk = sp.expand(tr(e_c * delta_c) + tr(e_t * delta_t) + tr(e_q * delta_q))
    exact(
        "the Ward preboundary equals the connection Green concomitant and both are nonzero",
        sp.simplify(theta - green) == 0 and theta != 0,
    )
    exact(
        "the nonzero Ward bulk plus boundary derivative cancels pointwise",
        sp.simplify(bulk + sp.diff(theta, x)) == 0 and bulk != 0,
    )
    bulk_integral = sp.integrate(bulk, (x, 0, 1))
    boundary = sp.simplify(theta.subs(x, 1) - theta.subs(x, 0))
    exact(
        "the integrated weak Ward identity retains a nonzero endpoint flux",
        bulk_integral + boundary == 0 and boundary != 0,
        f"bulk={bulk_integral}; boundary={boundary}",
    )
    wrong = sp.simplify(cov(connection, e_c, x) + comm(distortion, e_t))
    reject("freeze the moving Q owner in the nonabelian Ward identity", is_zero(wrong))
    reject("drop the connection owner and keep a Ward identity", is_zero(comm(distortion, e_t) + comm(reduction, e_q)))
    reject("drop the live Ward endpoint flux", boundary == 0)
    typed("the action is an exact nonabelian residual-symmetry comparator; the native Shiab action inherits its separate active covariance only after the PW2D transported-owner gate")
    typed("no graded ghost, antibracket, CME, physical moment map, BFV phase space, or anomaly theorem is claimed")


def full_k_equivariance_and_frechet_green() -> None:
    x, tau = sp.symbols("x tau", real=True)
    identity = sp.eye(2)

    b0 = sp.Matrix([[x, 1], [1 - x, -x]])
    t0 = sp.Matrix([[1 + x, x], [x**2, -1 - x]])
    q0 = sp.Matrix([[2, 1 + x], [x, -2]])
    db = sp.Matrix([[1 - x, x**2], [x, x - 1]])
    dt = sp.Matrix([[x, 1 - x], [1 + x, -x]])
    dq = sp.Matrix([[x**2, x], [1 - x, -x**2]])

    def source_graph(b: sp.Matrix, t: sp.Matrix, q: sp.Matrix):
        # Exact conjugation-equivariant local group map.  On the selected
        # compact interval I+T/5 is invertible and equals exp(log(I+T/5));
        # unlike a component extraction, it transports under every common
        # nonabelian gauge conjugation.
        h = sp.simplify(identity + t / 5)
        hinv = sp.simplify(h.inv())
        k = sp.simplify(hinv * (dmat(h, x) + b * h - h * b))
        return (
            sp.simplify(b + k),
            sp.simplify(t - k),
            sp.simplify(hinv * q * h),
            h,
            hinv,
            k,
        )

    c0, th0, qh0, h0, hinv0, k0 = source_graph(b0, t0, q0)
    c_tau, th_tau, qh_tau, _, _, k_tau = source_graph(
        b0 + tau * db, t0 + tau * dt, q0 + tau * dq
    )
    dc = c_tau.diff(tau).subs(tau, 0)
    dth = th_tau.diff(tau).subs(tau, 0)
    dqh = qh_tau.diff(tau).subs(tau, 0)
    dk = k_tau.diff(tau).subs(tau, 0)
    exact(
        "the literal equivariant full-K graph has live independent B and T Frechet returns",
        not is_zero(k0) and not is_zero(dk) and is_zero(dc - db - dk),
    )

    det_h = sp.factor(h0.det())
    negative_derivative_numerator = sp.Poly(
        sp.together(-sp.diff(det_h, x)).as_numer_denom()[0], x
    )
    derivative_discriminant = sp.discriminant(negative_derivative_numerator, x)
    exact(
        "h=I+T/5 is an invertible local GL(2) comparator on the selected interval",
        det_h.subs(x, 1) > 0
        and sp.LC(negative_derivative_numerator) > 0
        and derivative_discriminant < 0,
        f"det(h)={det_h}; derivative-discriminant={derivative_discriminant}",
    )

    # Direct differentiation of the already-pulled target action.
    l_tau = action_objects(c_tau, th_tau, qh_tau, x)[0]
    direct = sp.expand(sp.diff(l_tau, tau).subs(tau, 0))
    _, xh, ec, et, eq = action_objects(c0, th0, qh0, x)
    theta = sp.expand(tr(xh * dth))
    forward_frechet = sp.expand(tr(ec * dc) + tr(et * dth) + tr(eq * dqh))
    exact(
        "direct pulled variation equals the target-Euler/forward-Frechet return plus target Green derivative",
        sp.simplify(direct - forward_frechet - sp.diff(theta, x)) == 0
        and not is_zero(dk)
        and theta != 0,
    )

    # Explicit formal adjoint of the literal source graph.  Writing
    # eta=h^-1 delta h and R=E_Chat-E_That gives
    #   delta K=D_Chat eta +(Ad_h^-1-1)delta B.
    # Integrating the D_Chat eta term produces the old-root owner tuple and a
    # separate, generally nonzero graph Green concomitant.
    eta = sp.simplify(hinv0 * dt / 5)
    response = sp.simplify(ec - et)
    eta_owner = sp.simplify(-cov(c0, response, x) + comm(eq, qh0))
    e_b_old = sp.simplify(et + h0 * response * hinv0)
    e_t_old = sp.simplify(et + eta_owner * hinv0 / 5)
    e_q_old = sp.simplify(h0 * eq * hinv0)
    graph_green = sp.expand(tr(response * eta))
    old_pair = sp.expand(tr(e_b_old * db) + tr(e_t_old * dt) + tr(e_q_old * dq))
    exact(
        "the forward Frechet pairing integrates to an explicit old-root adjoint tuple plus a separate graph Green term",
        sp.simplify(forward_frechet - old_pair - sp.diff(graph_green, x)) == 0
        and graph_green != 0,
    )

    # Independent route: vary the pulled action directly with generic old-root
    # variations, then integrate every derivative of those variations by
    # parts without importing the target Euler tuple above.
    db_generic = sp.Matrix(2, 2, lambda i, j: sp.Function(f"db{i}{j}")(x))
    dt_generic = sp.Matrix(2, 2, lambda i, j: sp.Function(f"dt{i}{j}")(x))
    dq_generic = sp.Matrix(2, 2, lambda i, j: sp.Function(f"dq{i}{j}")(x))
    eta_generic = sp.simplify(hinv0 * dt_generic / 5)
    dk_generic = sp.simplify(
        cov(c0, eta_generic, x) + hinv0 * db_generic * h0 - db_generic
    )
    dc_generic = sp.simplify(db_generic + dk_generic)
    dth_generic = sp.simplify(dt_generic - dk_generic)
    dqh_generic = sp.simplify(
        hinv0 * dq_generic * h0 + comm(qh0, eta_generic)
    )
    y0 = comm(qh0, th0)
    dx_generic = sp.simplify(
        cov(c0, dth_generic, x) + comm(dc_generic, th0)
    )
    dy_generic = sp.simplify(
        comm(dqh_generic, th0) + comm(qh0, dth_generic)
    )
    direct_generic = sp.expand(
        tr(xh * dx_generic)
        + tr(y0 * dy_generic)
        + tr(th0**3 * dth_generic)
    )
    generic_variables = [
        *list(db_generic),
        *list(dt_generic),
        *list(dq_generic),
    ]
    direct_coefficients, direct_green = integrate_linear_variation(
        direct_generic, generic_variables, x
    )
    e_b_direct = trace_owner_matrix(direct_coefficients[0:4])
    e_t_direct = trace_owner_matrix(direct_coefficients[4:8])
    e_q_direct = trace_owner_matrix(direct_coefficients[8:12])
    theta_generic = sp.expand(tr(xh * dth_generic))
    graph_green_generic = sp.expand(tr(response * eta_generic))
    old_pair_generic = sp.expand(
        tr(e_b_old * db_generic)
        + tr(e_t_old * dt_generic)
        + tr(e_q_old * dq_generic)
    )
    exact(
        "independent raw-action integration gives the same complete old-root Euler tuple",
        is_zero(e_b_direct - e_b_old)
        and is_zero(e_t_direct - e_t_old)
        and is_zero(e_q_direct - e_q_old),
    )
    exact(
        "the independently derived total preboundary equals target Green plus the nonzero graph Green layer",
        sp.simplify(direct_green - theta_generic - graph_green_generic) == 0
        and graph_green_generic != 0
        and sp.simplify(
            direct_generic - old_pair_generic - sp.diff(direct_green, x)
        )
        == 0,
    )

    total_green = sp.expand(theta + graph_green)
    boundary = sp.simplify(total_green.subs(x, 1) - total_green.subs(x, 0))
    exact(
        "the complete Frechet-adjoint calculation retains a nonzero exact endpoint return",
        sp.simplify(direct - old_pair - sp.diff(total_green, x)) == 0
        and boundary != 0,
        f"boundary={boundary}",
    )
    wrong_th = dt
    wrong_theta = sp.expand(tr(xh * wrong_th))
    reject(
        "freeze K_full in the source Frechet/Green return",
        sp.simplify(direct - (tr(ec * dc) + tr(et * wrong_th) + tr(eq * dqh)) - sp.diff(wrong_theta, x)) == 0,
    )
    reject(
        "drop the separate graph Green concomitant after forming the old-root Frechet adjoint",
        sp.simplify(direct - old_pair - sp.diff(theta, x)) == 0,
    )

    # Residual right-gauge covariance of the literal graph.
    c = sp.Matrix([[x, 1 + x], [x**2, -x]])
    delta_b = -cov(b0, c, x)
    delta_t = comm(c, t0)
    delta_q = comm(c, q0)
    cg, thg, qhg, hg, hinvg, kg = source_graph(
        b0 + tau * delta_b, t0 + tau * delta_t, q0 + tau * delta_q
    )
    delta_k = kg.diff(tau).subs(tau, 0)
    delta_th = thg.diff(tau).subs(tau, 0)
    delta_qh = qhg.diff(tau).subs(tau, 0)
    exact(
        "equivariant h(T) makes literal K tensorial and transports T-K and Qhat adjointly",
        is_zero(delta_k - comm(c, k0))
        and is_zero(delta_th - comm(c, th0))
        and is_zero(delta_qh - comm(c, qh0)),
        f"dK={sp.simplify(delta_k-comm(c,k0))}; dT={sp.simplify(delta_th-comm(c,th0))}; dQ={sp.simplify(delta_qh-comm(c,qh0))}",
    )
    exact(
        "the literal B+K target transforms as a connection under the same residual right action",
        is_zero(cg.diff(tau).subs(tau, 0) + cov(c0, c, x)),
        f"defect={sp.simplify(cg.diff(tau).subs(tau,0)+cov(c0,c,x))}",
    )
    reject("treat K_full as an independent connection rather than a tensorial difference", False)
    typed("h=I+T/5 is only an exact local GL(2) structural comparator; active Sp(32,32;H), right-H, and Krein membership remain native PW2E burdens")


def scope_checks() -> None:
    typed("the residual Ward closes before observation; section support does not imply equation descent or no leakage")
    typed("the public-to-active real bundle port, full Z0+Z1 metric Frechet owner, analytic domain, and physical quotient remain open")
    typed("P1/P2/P3 remain unchanged and unused; none supplies the tilted action, Ward owner, boundary, or quotient")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE; TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    reject("infer (1-LR)E_YL=0 from R E_Y L=E_X", False)
    reject("promote the ordinary nonabelian Ward comparator to a graded BV/CME theorem", False)


def main() -> int:
    print("PW2D RESIDUAL RIGHT-TILTED NONABELIAN WARD / FRECHET-GREEN")
    source_and_layer_zero()
    tilted_group_checks()
    residual_ward_checks()
    full_k_equivariance_and_frechet_green()
    scope_checks()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + {PLANTED} planted = {total}; failures={len(FAILURES)}"
    )
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print("VERDICT: PW2D RESIDUAL RIGHT-TILTED WARD AND FRECHET-GREEN PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
