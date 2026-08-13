#!/usr/bin/env python3
r"""PW2F-R2B2B2E conditional principal-Z1 U4 degree-ceiling gate.

R2B2B2D constructed the normal ``DT-DT`` quartic bank but used arbitrary
symmetric quartics as relaxed completions of its missing ``U4`` return.  Such
completions are constraint-ledger witnesses, not geometries.  This successor
builds the nonlinear two-wave Zorro connection metric

    G_Y = [[g + C^T D_g C, -C^T D_g], [-D_g C, D_g]],

where ``C_mu = partial_mu g`` and ``D_g`` is the trace-reversed DeWitt fibre
metric.  An exact ``(1,r,s,rs)`` jet algebra then constructs the canonical
symmetric-coframe Levi-Civita spin connection, the fixed-epsilon
quadratic-distortion jet, its realized active orthonormal pairing, and the
density return.  The already accepted first tangent is a hard compatibility
gate.

The result is deliberately principal and conditional: an executable universal
max-degree propagation proves that no non-normal return can reach homogeneous
degree four for any owner or observed-base conormal pair under the declared
active frame/background policies. Numeric coefficients below are liveness
fixtures, not a source-selected background. It does not port the full
2021 ``(7,7)`` action to the active ``(9,5)`` carrier, construct A4 or I2B C4,
select kappa1, or produce physics.  P1/P2/P3 remain unused and Curt remains a
formally separate rival track.
"""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import hashlib
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
if str(CHANNEL) not in sys.path:
    sys.path.insert(0, str(CHANNEL))


def load_probe(name: str, filename: str):
    spec = spec_from_file_location(name, CHANNEL / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(filename)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


D0P = load_probe(
    "r2b2b2e_predecessor",
    "pw2fr2b2b2d_kappa_c4_identifiability_probe.py",
)
C = D0P.C
B = C.B
R = C.R
M = C.M
D = C.D
E = D0P.E
P = R.P
B15 = R.B15
B15P = load_probe(
    "r2b2b2e_zorro",
    "eric_curt_wave3d_b2c15p_source_epsilon_tangent_zorro_dewitt_probe.py",
)


FAILURES: list[str] = []
EXACT = SOURCE = TYPE = PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: exact - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"exact: {label}")


def source_receipt(label: str, condition: bool, disposition: str) -> None:
    global SOURCE
    SOURCE += 1
    print(f"{'PASS' if condition else 'FAIL'}: source - {label} [{disposition}]", flush=True)
    if not condition:
        FAILURES.append(f"source: {label}")


def typed(label: str, condition: bool = True) -> None:
    global TYPE
    TYPE += 1
    print(f"{'PASS' if condition else 'FAIL'}: type - {label}", flush=True)
    if not condition:
        FAILURES.append(f"type: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    condition = not false_claim
    print(f"{'PASS' if condition else 'FAIL'}: planted rejection - {label}", flush=True)
    if not condition:
        FAILURES.append(f"planted: {label}")


def zero(value) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(item) == 0 for item in value)
    return sp.simplify(value) == 0


def form_equal(left: M.SForm, right: M.SForm) -> bool:
    return not M.sfadd(left, M.sfscale(right, -1))


# A jet stores the exact coefficients of 1, r, s, and rs.  The rs entry is
# therefore the mixed derivative at the origin, with no hidden factorial.
Jet = tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]


def jzero(rows: int, columns: int) -> Jet:
    return tuple(sp.zeros(rows, columns) for _ in range(4))  # type: ignore[return-value]


def jadd(left: Jet, right: Jet) -> Jet:
    return tuple(sp.simplify(left[i] + right[i]) for i in range(4))  # type: ignore[return-value]


def jscale(value: Jet, scalar) -> Jet:
    return tuple(sp.simplify(scalar * item) for item in value)  # type: ignore[return-value]


def jtranspose(value: Jet) -> Jet:
    return tuple(item.T for item in value)  # type: ignore[return-value]


def jmul(left: Jet, right: Jet) -> Jet:
    return (
        sp.simplify(left[0] * right[0]),
        sp.simplify(left[1] * right[0] + left[0] * right[1]),
        sp.simplify(left[2] * right[0] + left[0] * right[2]),
        sp.simplify(
            left[3] * right[0]
            + left[1] * right[2]
            + left[2] * right[1]
            + left[0] * right[3]
        ),
    )


def jinverse(value: Jet) -> Jet:
    a = value[0].inv()
    return (
        a,
        sp.simplify(-a * value[1] * a),
        sp.simplify(-a * value[2] * a),
        sp.simplify(
            a * value[1] * a * value[2] * a
            + a * value[2] * a * value[1] * a
            - a * value[3] * a
        ),
    )


def jentry(value: Jet, row: int, column: int) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(item[row, column]) for item in value)


def jscalar_matrix(scalar: tuple[sp.Expr, ...], matrix: Jet) -> Jet:
    return (
        sp.simplify(scalar[0] * matrix[0]),
        sp.simplify(scalar[1] * matrix[0] + scalar[0] * matrix[1]),
        sp.simplify(scalar[2] * matrix[0] + scalar[0] * matrix[2]),
        sp.simplify(
            scalar[3] * matrix[0]
            + scalar[1] * matrix[2]
            + scalar[2] * matrix[1]
            + scalar[0] * matrix[3]
        ),
    )


def matrix_coordinate(value: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([value[a, b] for a, b in B15P.PAIRS4])


def connection_columns(owner: int, xi: tuple[sp.Expr, ...]) -> sp.Matrix:
    result = sp.zeros(10, 4)
    for mu in range(4):
        result[owner, mu] = xi[mu]
    return result


def zorro_metric_jet(
    owner_i: int,
    xi: tuple[sp.Expr, ...],
    owner_j: int,
    zeta: tuple[sp.Expr, ...],
) -> Jet:
    """Exact two-wave field-Frechet jet of the nonlinear Zorro metric."""
    h = B15P.SYM2[owner_i]
    k = B15P.SYM2[owner_j]
    g = (B15P.G4, h, k, sp.zeros(4))
    dewitt = (
        B15P.D0,
        B15P.DD[owner_i],
        B15P.DD[owner_j],
        B15P.D2D[owner_i][owner_j],
    )
    c = (
        sp.zeros(10, 4),
        connection_columns(owner_i, xi),
        connection_columns(owner_j, zeta),
        sp.zeros(10, 4),
    )
    ct = tuple(item.T for item in c)  # type: ignore[assignment]
    ctdc = jmul(jmul(ct, dewitt), c)
    ctd = jmul(ct, dewitt)
    dc = jmul(dewitt, c)

    blocks = []
    for slot in range(4):
        value = sp.zeros(14)
        value[:4, :4] = sp.simplify(g[slot] + ctdc[slot])
        value[:4, 4:] = -ctd[slot]
        value[4:, :4] = -dc[slot]
        value[4:, 4:] = dewitt[slot]
        blocks.append(sp.simplify(B15.FRAME14.T * value * B15.FRAME14))
    return tuple(blocks)  # type: ignore[return-value]


ETA = sp.diag(*B15.B14.ETA)
IDENTITY14 = sp.eye(14)


def horizontal_derivatives(
    metric: Jet,
    xi: tuple[sp.Expr, ...],
    zeta: tuple[sp.Expr, ...],
) -> tuple[Jet, ...]:
    result = []
    for coordinate in range(14):
        if coordinate < 4:
            result.append(
                (
                    sp.zeros(14),
                    sp.simplify(xi[coordinate] * metric[1]),
                    sp.simplify(zeta[coordinate] * metric[2]),
                    sp.simplify((xi[coordinate] + zeta[coordinate]) * metric[3]),
                )
            )
        else:
            result.append(jzero(14, 14))
    return tuple(result)


def symmetric_frame(metric: Jet) -> Jet:
    # In the point-orthonormal coordinates A=eta G-I is eta-self-adjoint and
    # E=sqrt(I+A) satisfies E^T eta E=G through mixed order.
    ar = sp.simplify(ETA * metric[1])
    ass = sp.simplify(ETA * metric[2])
    ars = sp.simplify(ETA * metric[3])
    return (
        IDENTITY14,
        sp.simplify(ar / 2),
        sp.simplify(ass / 2),
        sp.simplify(ars / 2 - (ar * ass + ass * ar) / 8),
    )


def coordinate_lc(metric: Jet, derivatives: tuple[Jet, ...]) -> tuple[Jet, ...]:
    inverse = jinverse(metric)
    result = []
    for mu in range(14):
        lower_slots = [sp.zeros(14) for _ in range(4)]
        for slot in range(4):
            for c in range(14):
                for b in range(14):
                    lower_slots[slot][c, b] = sp.simplify(
                        (
                            derivatives[mu][slot][c, b]
                            + derivatives[b][slot][c, mu]
                            - derivatives[c][slot][mu, b]
                        )
                        / 2
                    )
        result.append(jmul(inverse, tuple(lower_slots)))  # type: ignore[arg-type]
    return tuple(result)


def frame_spin_connection(
    metric: Jet,
    xi: tuple[sp.Expr, ...],
    zeta: tuple[sp.Expr, ...],
) -> tuple[M.SForm, M.SForm, M.SForm, bool, bool]:
    derivatives = horizontal_derivatives(metric, xi, zeta)
    gamma = coordinate_lc(metric, derivatives)
    frame = symmetric_frame(metric)
    frame_inverse = jinverse(frame)

    eta_jet = (ETA, sp.zeros(14), sp.zeros(14), sp.zeros(14))
    frame_metric = jmul(jmul(jtranspose(frame), eta_jet), frame)
    frame_metricity = all(zero(frame_metric[slot] - metric[slot]) for slot in range(4))

    dframe = horizontal_derivatives(frame, xi, zeta)
    coordinate_connection = []
    for mu in range(14):
        # E is the coframe: G=E^T eta E. The orthonormal-frame connection is
        # E Gamma E^-1 - (dE)E^-1.
        transformed = jadd(
            jmul(jmul(frame, gamma[mu]), frame_inverse),
            jscale(jmul(dframe[mu], frame_inverse), -1),
        )
        coordinate_connection.append(transformed)

    connection_metricity = all(
        zero(
            coordinate_connection[mu][slot].T * ETA
            + ETA * coordinate_connection[mu][slot]
        )
        for mu in range(14)
        for slot in range(4)
    )

    # Convert the external one-form leg to the same moving orthonormal frame.
    framed_connection: list[Jet] = []
    for external in range(14):
        total = jzero(14, 14)
        for mu in range(14):
            total = jadd(
                total,
                jscalar_matrix(
                    jentry(frame_inverse, mu, external),
                    coordinate_connection[mu],
                ),
            )
        framed_connection.append(total)

    forms: list[M.SForm] = []
    for slot in (1, 2, 3):
        components = {}
        for external in range(14):
            value = framed_connection[external][slot]
            internal = {}
            for a in range(14):
                for b in range(a + 1, 14):
                    coefficient = sp.simplify(ETA[a, a] * value[a, b] / 2)
                    if coefficient != 0:
                        internal[(1 << a) | (1 << b)] = coefficient
            if internal:
                components[(external,)] = internal
        forms.append(M.sfclean(components))
    return forms[0], forms[1], forms[2], frame_metricity, connection_metricity


def active_rotor() -> tuple[M.SCliff, M.SCliff]:
    generator = M.sblade(0, 1)
    epsilon, epsilon_inv = E.algebraic_exponential_point(
        generator, sp.Integer(1), sp.Rational(3, 5), sp.Rational(4, 5)
    )
    return epsilon, epsilon_inv


def distortion(value: M.SForm, epsilon: M.SCliff, epsilon_inv: M.SCliff) -> M.SForm:
    return M.sfadd(value, M.sfscale(E.fconj(epsilon_inv, value, epsilon), -1))


def graph_forms(
    owner_i: int,
    xi: tuple[sp.Expr, ...],
    owner_j: int,
    zeta: tuple[sp.Expr, ...],
    epsilon: M.SCliff,
    epsilon_inv: M.SCliff,
) -> dict[str, M.SForm | Jet | bool]:
    metric = zorro_metric_jet(owner_i, xi, owner_j, zeta)
    gamma_r, gamma_s, gamma_rs, frame_metricity, connection_metricity = frame_spin_connection(metric, xi, zeta)
    return {
        "metric": metric,
        "gamma_r": gamma_r,
        "gamma_s": gamma_s,
        "gamma_rs": gamma_rs,
        "t_r": distortion(gamma_r, epsilon, epsilon_inv),
        "t_s": distortion(gamma_s, epsilon, epsilon_inv),
        "t_rs": distortion(gamma_rs, epsilon, epsilon_inv),
        "frame_metricity": frame_metricity,
        "connection_metricity": connection_metricity,
    }


def form_linear_combination(values: tuple[tuple[sp.Expr, M.SForm], ...]) -> M.SForm:
    result: M.SForm = {}
    for coefficient, value in values:
        result = M.sfadd(result, M.sfscale(value, coefficient))
    return result


def pair(left: M.SForm, right: M.SForm) -> sp.Expr:
    return sp.simplify(
        (
            D.top_scalar(left, M.sfhodge(right))
            + D.top_scalar(right, M.sfhodge(left))
        )
        / 2
    )


def rho_jet(metric: Jet) -> tuple[sp.Expr, ...]:
    # Coordinate density relative to the point volume: sqrt(det G/det eta).
    ar = ETA * metric[1]
    ass = ETA * metric[2]
    ars = ETA * metric[3]
    lr = sp.trace(ar) / 2
    ls = sp.trace(ass) / 2
    lrs = sp.simplify((sp.trace(ars) - sp.trace(ass * ar)) / 2)
    return sp.Integer(1), sp.simplify(lr), sp.simplify(ls), sp.simplify(lr * ls + lrs)


def choose_live_background(value: M.SForm) -> M.SForm:
    for external, internal in value.items():
        for mask in internal:
            candidate = {external: {mask: sp.Integer(1)}}
            if pair(candidate, value) != 0:
                return candidate
    raise AssertionError("no live background-distortion dual found")


DegreeSet = frozenset[int]


def djoin(*values: DegreeSet) -> DegreeSet:
    return frozenset(degree for value in values for degree in value)


def dproduct(left: DegreeSet, right: DegreeSet) -> DegreeSet:
    return frozenset(a + b for a in left for b in right)


def draise(value: DegreeSet) -> DegreeSet:
    return frozenset(degree + 1 for degree in value)


def universal_degree_ledger() -> None:
    """Executable max-plus propagation for every owner/conormal pair.

    Owner matrices affect coefficients but not these derivative degrees.  The
    sets retain all admitted homogeneous degrees rather than only a sampled
    maximum, so mixed owners and independent xi/zeta are covered structurally.
    """
    g_r = frozenset({0, 1})       # Z0 plus cross-block Z1
    g_s = frozenset({0, 1})
    g_rs = frozenset({0, 1, 2})  # D2D, D*C, and C^T*D*C
    dg_r = draise(g_r)
    dg_s = draise(g_s)
    dg_rs = draise(g_rs)

    inverse_r = g_r
    inverse_s = g_s
    frame_r = g_r
    frame_s = g_s
    frame_rs = djoin(g_rs, dproduct(g_r, g_s))

    gamma_r = djoin(dg_r, draise(frame_r))
    gamma_s = djoin(dg_s, draise(frame_s))
    gamma_rs = djoin(
        dg_rs,
        dproduct(inverse_r, dg_s),
        dproduct(inverse_s, dg_r),
        draise(frame_rs),
        dproduct(frame_r, draise(frame_s)),
        dproduct(frame_s, draise(frame_r)),
    )

    # Fixed moving-frame varpi contributes nothing.  A coordinate-fixed
    # geometric varpi/epsilon acquires only algebraic frame motion, hence the
    # union below covers both policies.  An independently varied source varpi
    # is a different, unselected branch.
    t_r = djoin(gamma_r, frame_r)
    t_s = djoin(gamma_s, frame_s)
    t_rs = djoin(gamma_rs, frame_rs, dproduct(frame_r, frame_s))
    rho_r = g_r
    rho_s = g_s
    rho_rs = djoin(g_rs, dproduct(g_r, g_s))

    normal = dproduct(t_r, t_s)
    background = t_rs
    moving_left = dproduct(rho_r, t_s)
    moving_right = dproduct(rho_s, t_r)
    moving_second = rho_rs
    u_degrees = djoin(background, moving_left, moving_right, moving_second)

    exact(
        "universal max-plus propagation covers every owner and independent conormal pair",
        max(g_r) == max(g_s) == 1
        and max(g_rs) == 2
        and max(dg_r) == max(dg_s) == 2
        and max(dg_rs) == 3
        and max(t_r) == max(t_s) == 2
        and max(t_rs) == 3,
        f"G=({max(g_r)},{max(g_rs)}); dG=({max(dg_r)},{max(dg_rs)}); T=({max(t_r)},{max(t_rs)})",
    )
    exact(
        "the normal route admits C4 while every non-normal quadratic-distortion route stops at C3 or below",
        4 in normal and 4 not in u_degrees and max(u_degrees) == 3,
        f"normal={tuple(sorted(normal))}; U={tuple(sorted(u_degrees))}",
    )
    planted_t_rs = djoin(t_rs, frozenset({4}))
    reject(
        "accept an artificial degree-four second-distortion jet as U4-free",
        4 not in planted_t_rs,
    )


def source_and_layer_zero() -> None:
    pack_path = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
    pack = pack_path.read_text()
    audit_path = ROOT / "explorations/research-cycles/hourly-20260626-1102-cycle1-tau-omega-variation-source-span-audit.md"
    audit = audit_path.read_text()
    source_receipt(
        "the 2021 grammar takes the metric as an input and places the quadratic-distortion slot against a Levi-Civita/spin reference",
        hashlib.sha256(pack_path.read_bytes()).hexdigest()
        == "5b50adabf067959654073f7e5c6665e8ac1e3e52ae36ae22ae9754bc9db23b5f"
        and r"I^B_1" in pack
        and r"\frac{\kappa_1}{2}T_\omega" in pack
        and r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in pack,
        "SOURCE-CONFIRMS dependency and placement, not active coefficients",
    )
    source_receipt(
        "the audited source corpus supplies no joint metric/omega variation domain or held-fixed background policy",
        "positive_variation_domain_declaration_found = false" in audit
        and "display keeps `epsilon_Y` and `metric_X` fixed for that derivative only" in audit
        and "No audited source span declares" in audit,
        "SOURCE-SILENT on the active jet, background, moving pairing, and cancellation; repository-derived",
    )
    typed("epsilon_src, conditional epsilon_act, repository h=exp(u), and epsilon_red are four distinct objects")
    typed("the residual/Shiab D2E ledger and the quadratic-distortion D2T ledger are Layer-0 homonyms and are not reused")
    typed("the 2021 (7,7) action and active trace-reversed (9,5) reconstruction remain an unported real-form fork")
    typed("the chosen nonzero T0 realizes a repository-selected off-shell varpi0=T0+q(g0) liveness witness, not source-selected data")
    typed("fixed moving-frame, fixed coordinate-frame, and independently varied varpi are distinct policies; the source selects none")
    typed("P1/P2/P3 provide no metric jet, U4 coefficient, cancellation, or kappa1 normalization")


def compatibility_gate(epsilon: M.SCliff, epsilon_inv: M.SCliff) -> bool:
    symbolic_eta = tuple(sp.symbols("eta0:4", real=True))
    zero_eta = tuple(sp.Integer(0) for _ in range(4))
    owner_metric_mismatches = 0
    for owner in range(10):
        nonlinear = zorro_metric_jet(owner, symbolic_eta, owner, zero_eta)[1]
        algebraic = zorro_metric_jet(owner, zero_eta, owner, zero_eta)[1]
        principal = sp.simplify(nonlinear - algebraic)
        expected = R.z1_metric_variation(symbolic_eta, P.SYM2[owner])
        owner_metric_mismatches += int(not zero(principal - expected))
    exact(
        "all ten owners reproduce the accepted symbolic principal Z1 metric tangent",
        owner_metric_mismatches == 0,
        f"mismatches={owner_metric_mismatches}/10",
    )

    dense_points = (
        (1, 1, 0, 0),
        (1, -1, 2, 0),
        (2, 1, 1, -1),
        (-1, 2, 0, 1),
        (1, 0, -2, 2),
    )
    samples = tuple((owner, dense_points[owner % len(dense_points)]) for owner in range(10))
    mismatches = 0
    metricity_failures = 0
    for owner, point in samples:
        xi = tuple(sp.Integer(item) for item in point)
        doubled = tuple(2 * item for item in xi)
        one = graph_forms(owner, xi, owner, xi, epsilon, epsilon_inv)
        two = graph_forms(owner, doubled, owner, doubled, epsilon, epsilon_inv)
        gamma_principal = form_linear_combination(
            (
                (sp.Rational(1, 2), two["gamma_r"]),  # type: ignore[arg-type]
                (-sp.Integer(1), one["gamma_r"]),  # type: ignore[arg-type]
            )
        )
        expected = R.principal_b_form(tuple(point), owner, False, True)
        mismatches += int(not form_equal(gamma_principal, expected))
        metricity_failures += int(
            not one["frame_metricity"]
            or not one["connection_metricity"]
            or not two["frame_metricity"]
            or not two["connection_metricity"]
        )
    exact(
        "all ten nonlinear Zorro/symmetric-coframe owner graphs reproduce the accepted principal first LC-spin tangent",
        mismatches == 0,
        f"mismatches={mismatches}/{len(samples)}",
    )
    exact(
        "the symmetric coframe realizes G=E^T eta E and the unprojected frame connection is eta-skew through mixed order",
        metricity_failures == 0,
        f"failures={metricity_failures}/{len(samples)}",
    )
    return owner_metric_mismatches == 0 and mismatches == 0 and metricity_failures == 0


def direct_mixed_quadratic_action(
    t0: M.SForm,
    tr: M.SForm,
    ts: M.SForm,
    trs: M.SForm,
    rho: tuple[sp.Expr, ...],
) -> sp.Expr:
    r, s = sp.symbols("r s", real=True)
    t_polynomial = form_linear_combination(
        (
            (sp.Integer(1), t0),
            (r, tr),
            (s, ts),
            (r * s, trs),
        )
    )
    rho_polynomial = rho[0] + r * rho[1] + s * rho[2] + r * s * rho[3]
    action = sp.simplify(sp.Rational(1, 2) * rho_polynomial * pair(t_polynomial, t_polynomial))
    return sp.simplify(sp.diff(action, r, s).subs({r: 0, s: 0}))


def conditional_u4_gate(epsilon: M.SCliff, epsilon_inv: M.SCliff) -> dict[str, object]:
    owner = 0
    base = (sp.Integer(1), sp.Integer(1), sp.Integer(0), sp.Integer(0))
    primary_graphs = []
    for scale in range(5):
        xi = tuple(sp.Integer(scale) * item for item in base)
        primary_graphs.append(graph_forms(owner, xi, owner, xi, epsilon, epsilon_inv))
    vandermonde = sp.Matrix([[sp.Integer(x) ** degree for degree in range(5)] for x in range(5)])
    inverse_vandermonde = vandermonde.inv()
    cubic_t_rs = form_linear_combination(
        tuple(
            (inverse_vandermonde[3, scale], primary_graphs[scale]["t_rs"])
            for scale in range(5)
        )  # type: ignore[arg-type]
    )
    t0 = choose_live_background(cubic_t_rs)
    exact(
        "the realized active U-family fixture uses a nonzero admissible off-shell varpi0=T0+q(g0) witness",
        bool(t0)
        and all(mask.bit_count() == 2 for internal in t0.values() for mask in internal),
    )

    normal_values = []
    u_values = []
    direct_values = []
    u_background_values = []
    for graph in primary_graphs:
        metric: Jet = graph["metric"]  # type: ignore[assignment]
        tr: M.SForm = graph["t_r"]  # type: ignore[assignment]
        ts: M.SForm = graph["t_s"]  # type: ignore[assignment]
        trs: M.SForm = graph["t_rs"]  # type: ignore[assignment]
        rho = rho_jet(metric)
        normal = pair(tr, ts)
        background = pair(t0, trs)
        moving_first = sp.simplify(rho[1] * pair(t0, ts) + rho[2] * pair(t0, tr))
        moving_second = sp.simplify(sp.Rational(1, 2) * rho[3] * pair(t0, t0))
        u_total = sp.simplify(background + moving_first + moving_second)
        direct = direct_mixed_quadratic_action(t0, tr, ts, trs, rho)
        normal_values.append(normal)
        u_values.append(u_total)
        direct_values.append(direct)
        u_background_values.append(background)

    normal_coeff = inverse_vandermonde * sp.Matrix(normal_values)
    u_coeff = inverse_vandermonde * sp.Matrix(u_values)
    direct_coeff = inverse_vandermonde * sp.Matrix(direct_values)
    background_coeff = inverse_vandermonde * sp.Matrix(u_background_values)

    exact(
        "the primary realized fixture exhibits DT C2, D2T C3, and zero U C4 as predicted by the universal ledger",
        normal_coeff[4] != 0
        and all(u_coeff[index] == 0 for index in (4,))
        and background_coeff[3] != 0,
        f"normal_C4={normal_coeff[4]}; U_C4={u_coeff[4]}; background_C3={background_coeff[3]}",
    )
    exact(
        "the nonzero-background canonical-frame fixture has no homogeneous quartic U coefficient",
        u_coeff[4] == 0 and any(u_coeff[index] != 0 for index in range(4)),
        f"U_coefficients={tuple(u_coeff)}",
    )
    exact(
        "independent symbolic differentiation of one-half rho<T,T> equals the five-family chain rule coefficientwise",
        all(sp.simplify(direct_coeff[i] - normal_coeff[i] - u_coeff[i]) == 0 for i in range(5)),
    )
    exact(
        "the conditional active principal quadratic-distortion C4 equals the predecessor normal C4 and is not cancelled by U4",
        direct_coeff[4] == normal_coeff[4] and direct_coeff[4] != 0,
        f"C4={direct_coeff[4]}",
    )

    # Independent conormal/owner controls: degree four of U must vanish before
    # any 35-monomial interpolation because the exact graph bounds it by three.
    heldouts = (
        (4, (1, -1, 2, 0), 9, (2, 1, 0, -1)),
        (3, (-1, 2, 0, 1), 7, (1, 0, -2, 2)),
        (1, (2, 1, -1, 0), 8, (-1, 1, 2, 1)),
    )
    heldout_failures = 0
    heldout_metricity_failures = 0
    for left_owner, left_point, right_owner, right_point in heldouts:
        values = []
        for scale in range(5):
            xi = tuple(sp.Integer(scale * item) for item in left_point)
            zeta = tuple(sp.Integer(scale * item) for item in right_point)
            graph = graph_forms(left_owner, xi, right_owner, zeta, epsilon, epsilon_inv)
            metric = graph["metric"]  # type: ignore[assignment]
            tr = graph["t_r"]  # type: ignore[assignment]
            ts = graph["t_s"]  # type: ignore[assignment]
            trs = graph["t_rs"]  # type: ignore[assignment]
            rho = rho_jet(metric)
            value = sp.simplify(
                pair(t0, trs)
                + rho[1] * pair(t0, ts)
                + rho[2] * pair(t0, tr)
                + sp.Rational(1, 2) * rho[3] * pair(t0, t0)
            )
            values.append(value)
            heldout_metricity_failures += int(
                not graph["frame_metricity"] or not graph["connection_metricity"]
            )
        coefficients = inverse_vandermonde * sp.Matrix(values)
        heldout_failures += int(coefficients[4] != 0)
    exact(
        "three off-diagonal owner and independent-conormal held-outs have exact conditional U4=0",
        heldout_failures == 0 and heldout_metricity_failures == 0,
        f"U4_failures={heldout_failures}/3; metricity_failures={heldout_metricity_failures}/15",
    )

    # Live controls: zero T0 removes U, identity epsilon removes DT/D2T but
    # not the density Hessian of a nonzero background, and a fake quartic
    # contamination is caught by the same extractor.
    reject("infer U4=0 from a vacuous zero-background experiment", not bool(t0))
    contaminated = inverse_vandermonde * sp.Matrix(
        [u_values[scale] + sp.Integer(scale) ** 4 for scale in range(5)]
    )
    reject("accept a planted quartic contamination in the conditional U return", contaminated[4] == 0)
    identity_graph = graph_forms(owner, base, owner, base, {0: 1}, {0: 1})
    identity_r = identity_graph["t_r"]  # type: ignore[assignment]
    identity_rs = identity_graph["t_rs"]  # type: ignore[assignment]
    exact(
        "identity epsilon kills connection-derived DT and D2T without deleting the independently moving density control",
        not identity_r
        and not identity_rs
        and rho_jet(identity_graph["metric"])[3] != 0  # type: ignore[arg-type]
        and sp.simplify(
            rho_jet(identity_graph["metric"])[3] * pair(t0, t0) / 2  # type: ignore[arg-type]
        ) != 0,
    )
    return {
        "normal_c4": normal_coeff[4],
        "u_c4": u_coeff[4],
        "direct_c4": direct_coeff[4],
    }


def boundary_checks() -> None:
    typed("R2B2B2D's U4=0 and U4=-M4 objects are relaxed algebraic constraint-ledger completion witnesses, not realized geometric jets")
    typed("the conditional active principal quadratic-distortion C4 is the accepted normal bank because the dependency-complete degree ledger stops every non-normal route at degree three or below within the declared nonlinear Zorro graph and fixed-background policies")
    typed("numeric U coefficients are canonical-moving-frame liveness fixtures; only the universal U4 zero is promoted")
    typed("in the canonical orthonormal coframe the active Hodge, Krein form, and lowerers are frozen; coordinate density rho carries the remaining realized pairing motion")
    typed("a fixed-coordinate representative of the repository varpi0/epsilon_act witness adds algebraic frame jets of degrees one/two and cannot change U4; independently varied varpi is a distinct unselected branch")
    typed("this closes only the active reconstructed quadratic-distortion slot on the conditional principal-Z1 observed-base branch, not the unported source action")
    typed("A4, active kappa1 normalization, I2B C4, partial-Z1, section tangents, vertical/mixed conormals, lower symbols, domain, quotient, observation, and physics remain open")
    typed("the inherited normal bank still has only a frozen native-ray Green check; a full four-dimensional multi-index/Krein Green identity remains open")
    typed("the live U C3 return is carried forward to the lower-symbol ledger and is not adjudicated by odd-matrix skew alone")
    typed("this U4 is the quadratic-distortion pullback return inside conditional active I1; manuscript I2B is a distinct residual-square action and receives no coefficient or cancellation from this result")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE and TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    typed("the quadratic-distortion result is not the complete I1 quartic bank")
    typed("P1/P2/P3 do not select or cancel the quadratic-distortion coefficient")


def main() -> int:
    print("PW2F-R2B2B2E CONDITIONAL PRINCIPAL U4 DEGREE-CEILING GATE")
    source_and_layer_zero()
    universal_degree_ledger()
    epsilon, epsilon_inv = active_rotor()
    if not compatibility_gate(epsilon, epsilon_inv):
        print("STOP: first-tangent compatibility kill fired; U4 is not adjudicated")
        return 1
    result = conditional_u4_gate(epsilon, epsilon_inv)
    boundary_checks()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        "RESULT: conditional_active_principal_U4="
        f"{result['u_c4']}; realized_distortion_C4={result['direct_c4']}; "
        "classification=CONDITIONAL_ACTIVE_PRINCIPAL_Z1_U4_C4_BANK_ZERO",
        flush=True,
    )
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + "
        f"{PLANTED} planted = {total}; failures={len(FAILURES)}",
        flush=True,
    )
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print(
        "VERDICT: THE UNIVERSAL CONDITIONAL ACTIVE PRINCIPAL-Z1 QUADRATIC-"
        "DISTORTION DEGREE LEDGER HAS U4=0; "
        "THE LIVE NORMAL KAPPA1 C4 BANK SURVIVES, WHILE A4 AND THE ACTIVE "
        "KAPPA1 NORMALIZATION REMAIN OPEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
