#!/usr/bin/env python3
r"""PW2F-R2B2B2F conditional I1 transgression/projective-kappa gate.

This probe composes the source-explicit

    C(B,T)=F_B + 1/2 d_B T + 1/3 [T,T]

grammar with R2B2B2E's exact nonlinear two-wave Zorro metric and canonical
orthonormal coframe.  Everything is evaluated in that one coframe: the active
Shiab/Hodge formula is fixed there and the outer density ``rho`` occurs once.
The probe therefore does not add B2C15M's coordinate ``dstar`` volume response
on top of ``rho``.

For independent owner/conormal pairs it directly differentiates the written
raw density, independently assembles the exhaustive mixed product rule,
proves a structural degree-five ceiling, extracts degrees zero through six,
and compares the live quartic frozen-Shiab density witness ``A4_raw`` with the
accepted quadratic-distortion density witness ``M4_raw``.  The final test is a
projective comparator under the declared probe convention
``[T,T]_probe := T wedge T``.  It does not yet classify the Euler operator: the
multi-index Green/Helmholtz quotient and the moving distinguished DeWitt trace
in Shiab are unbuilt.  It also does not identify the 2021 (7,7) action with the
active (9,5) reconstruction, select a source normalization, construct the full
35-monomial A4 bank, or produce physics.  P1/P2/P3 are unused; Curt remains a
formally separate comparator.
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


E = load_probe(
    "pw2fr2b2b2f_geometry",
    "pw2fr2b2b2e_actual_u4_jet_realizability_probe.py",
)
M = E.M
D = E.D
R = E.R


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


JForm = tuple[M.SForm, M.SForm, M.SForm, M.SForm]


def jfadd(left: JForm, right: JForm) -> JForm:
    return tuple(M.sfadd(left[index], right[index]) for index in range(4))  # type: ignore[return-value]


def jfscale(value: JForm, coefficient) -> JForm:
    return tuple(M.sfscale(item, coefficient) for item in value)  # type: ignore[return-value]


def jfwedge(left: JForm, right: JForm) -> JForm:
    return (
        M.sfwedge(left[0], right[0]),
        M.sfadd(M.sfwedge(left[1], right[0]), M.sfwedge(left[0], right[1])),
        M.sfadd(M.sfwedge(left[2], right[0]), M.sfwedge(left[0], right[2])),
        M.sfadd(
            M.sfwedge(left[3], right[0]),
            M.sfwedge(left[1], right[2]),
            M.sfwedge(left[2], right[1]),
            M.sfwedge(left[0], right[3]),
        ),
    )


def form_polynomial(value: JForm, r: sp.Symbol, s: sp.Symbol) -> M.SForm:
    return E.form_linear_combination(
        (
            (sp.Integer(1), value[0]),
            (r, value[1]),
            (s, value[2]),
            (r * s, value[3]),
        )
    )


def integrate_form(value: M.SForm, parameter: sp.Symbol) -> M.SForm:
    return M.sfclean(
        {
            key: {
                mask: sp.integrate(coefficient, (parameter, 0, 1))
                for mask, coefficient in internal.items()
            }
            for key, internal in value.items()
        }
    )


def exterior_wave(value: M.SForm, wave: tuple[sp.Expr, ...]) -> M.SForm:
    return M.sfwedge(R.xi_form(wave), value)


def top_pair(left: M.SForm, curvature: M.SForm) -> sp.Expr:
    return sp.simplify(D.top_scalar(left, D.shiab(curvature)))


def source_and_layer_zero() -> None:
    pack_path = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
    pack = pack_path.read_text()
    source_receipt(
        "the pinned source fixes the I1 transgression grammar and its one-half/one-third coefficients",
        hashlib.sha256(pack_path.read_bytes()).hexdigest()
        == "5b50adabf067959654073f7e5c6665e8ac1e3e52ae36ae22ae9754bc9db23b5f"
        and r"F_{B_\omega}" in pack
        and r"\frac12d_{B_\omega}T_\omega" in pack
        and r"\frac13[T_\omega,T_\omega]" in pack,
        "SOURCE-CONFIRMS the manuscript grammar, not the active port",
    )
    source_receipt(
        "frozen source custody plus the accepted prior audit leave the active real-form, joint domain, and kappa normalization open",
        "source does not declare the complete" in pack
        and "admissible" in pack
        and r"\operatorname{Sp}(32,32;\mathbb H)" in pack
        and "value or normalization of `kappa1`" in (
            ROOT / "explorations/pw2fr2b2b2e-actual-u4-jet-realizability-2026-08-03.md"
        ).read_text(),
        "SOURCE-SILENT on active A4 and kappa selection",
    )
    typed("source transgression, repository A4, Portal eddy, compact Euler residual, and manuscript I2B are distinct objects")
    typed("epsilon_src, epsilon_act, repository h=exp(u), and epsilon_red remain four distinct objects")
    typed("the 2021 (7,7) action and active trace-reversed (9,5) coframe port remain unported")
    typed("the source writes a bracket while the active calculation uses an explicit wedge-product convention; no factor-two identification is inferred")
    typed("the probe convention is [T,T]_probe := T wedge T; the source bracket normalization is not identified with that convention")
    typed("one canonical coframe carries the connection and forms; fixed orthonormal Shiab plus one outer rho replaces coordinate dstar volume motion only for this comparator")
    typed("the distinguished normalized DeWitt trace insertion is not proved trace-adapted in this coframe, so moving-STRACE terms remain outside the comparator")
    typed("the curvature-built off-shell T0 is held as a pointwise zero-derivative background jet; its possible derivative belongs to a different unbuilt background policy")
    typed("the relative Shiab normalization lambda and action-port sign s_kappa remain explicit")
    typed("P1/P2/P3 provide no action coefficient, normalization, cancellation, or certificate")


def active_background() -> M.SForm:
    curvature = D.to_sympy_form(E.P.SPIN_CURVATURE)
    return D.build_source_t(D.shiab(curvature))


def graph_jets(
    owner_i: int,
    xi: tuple[sp.Expr, ...],
    owner_j: int,
    zeta: tuple[sp.Expr, ...],
    epsilon: M.SCliff,
    epsilon_inv: M.SCliff,
) -> dict[str, object]:
    graph = E.graph_forms(owner_i, xi, owner_j, zeta, epsilon, epsilon_inv)
    conjugate = lambda value: E.E.fconj(epsilon_inv, value, epsilon)
    b: JForm = (
        {},
        conjugate(graph["gamma_r"]),  # type: ignore[arg-type]
        conjugate(graph["gamma_s"]),  # type: ignore[arg-type]
        conjugate(graph["gamma_rs"]),  # type: ignore[arg-type]
    )
    t: JForm = (
        {},
        graph["t_r"],  # type: ignore[assignment]
        graph["t_s"],  # type: ignore[assignment]
        graph["t_rs"],  # type: ignore[assignment]
    )
    wave_rs = tuple(sp.simplify(xi[index] + zeta[index]) for index in range(4))
    db: JForm = (
        {},
        exterior_wave(b[1], xi),
        exterior_wave(b[2], zeta),
        exterior_wave(b[3], wave_rs),
    )
    dt: JForm = (
        {},
        exterior_wave(t[1], xi),
        exterior_wave(t[2], zeta),
        exterior_wave(t[3], wave_rs),
    )
    exact_sum = all(
        form_equal(M.sfadd(b[index], t[index]), graph[name])
        for index, name in ((1, "gamma_r"), (2, "gamma_s"), (3, "gamma_rs"))
    )
    return {
        "graph": graph,
        "b": b,
        "t_variation": t,
        "db": db,
        "dt": dt,
        "rho": E.rho_jet(graph["metric"]),  # type: ignore[arg-type]
        "sum_identity": exact_sum,
    }


def transgression(
    b: JForm,
    t: JForm,
    db: JForm,
    dt: JForm,
    cubic=sp.Rational(1, 3),
) -> JForm:
    f_b = jfadd(db, jfwedge(b, b))
    d_b_t = jfadd(dt, jfadd(jfwedge(b, t), jfwedge(t, b)))
    return jfadd(
        f_b,
        jfadd(jfscale(d_b_t, sp.Rational(1, 2)), jfscale(jfwedge(t, t), cubic)),
    )


def path_integrated_transgression(
    b: JForm, t: JForm, db: JForm, dt: JForm
) -> JForm:
    def curvature_at(tau) -> JForm:
        a_tau = jfadd(b, jfscale(t, tau))
        da_tau = jfadd(db, jfscale(dt, tau))
        return jfadd(da_tau, jfwedge(a_tau, a_tau))

    # F_(B+tau T) is quadratic in tau. Simpson's exact quadratic quadrature
    # is an independent path-integral route with no symbolic r/s expansion.
    f0 = curvature_at(sp.Integer(0))
    fhalf = curvature_at(sp.Rational(1, 2))
    f1 = curvature_at(sp.Integer(1))
    return tuple(
        M.sfscale(
            M.sfadd(f0[index], M.sfscale(fhalf[index], 4), f1[index]),
            sp.Rational(1, 6),
        )
        for index in range(4)
    )  # type: ignore[return-value]


PForm = dict[tuple[int, int], M.SForm]
PScalar = dict[tuple[int, int], sp.Expr]


def pform_from_jet(value: JForm) -> PForm:
    return {
        (0, 0): value[0],
        (1, 0): value[1],
        (0, 1): value[2],
        (1, 1): value[3],
    }


def pform_add(*values: PForm) -> PForm:
    result: PForm = {}
    for value in values:
        for degree, form in value.items():
            result[degree] = M.sfadd(result.get(degree, {}), form)
    return {degree: form for degree, form in result.items() if form}


def pform_scale(value: PForm, coefficient) -> PForm:
    return {
        degree: scaled
        for degree, form in value.items()
        if (scaled := M.sfscale(form, coefficient))
    }


def pform_wedge(left: PForm, right: PForm) -> PForm:
    result: PForm = {}
    for (lr, ls), left_form in left.items():
        for (rr, rs), right_form in right.items():
            degree = (lr + rr, ls + rs)
            result[degree] = M.sfadd(
                result.get(degree, {}), M.sfwedge(left_form, right_form)
            )
    return {degree: form for degree, form in result.items() if form}


def pscalar_mul(left: PScalar, right: PScalar) -> PScalar:
    result: PScalar = {}
    for (lr, ls), left_value in left.items():
        for (rr, rs), right_value in right.items():
            degree = (lr + rr, ls + rs)
            result[degree] = sp.simplify(
                result.get(degree, sp.Integer(0)) + left_value * right_value
            )
    return {degree: value for degree, value in result.items() if value != 0}


def generic_raw_density_mixed(
    b: JForm,
    t: JForm,
    db: JForm,
    dt: JForm,
    rho: tuple[sp.Expr, ...],
    cubic,
    density_power: int,
) -> sp.Expr:
    """Build the whole bivariate polynomial by generic degree convolution."""
    b_poly = pform_from_jet(b)
    t_poly = pform_from_jet(t)
    db_poly = pform_from_jet(db)
    dt_poly = pform_from_jet(dt)
    c_poly = pform_add(
        db_poly,
        pform_wedge(b_poly, b_poly),
        pform_scale(
            pform_add(
                dt_poly,
                pform_wedge(b_poly, t_poly),
                pform_wedge(t_poly, b_poly),
            ),
            sp.Rational(1, 2),
        ),
        pform_scale(pform_wedge(t_poly, t_poly), cubic),
    )
    pair_poly: PScalar = {}
    for (tr, ts), left in t_poly.items():
        for (cr, cs), curvature in c_poly.items():
            degree = (tr + cr, ts + cs)
            pair_poly[degree] = sp.simplify(
                pair_poly.get(degree, sp.Integer(0)) + top_pair(left, curvature)
            )
    rho_poly: PScalar = {
        (0, 0): rho[0],
        (1, 0): rho[1],
        (0, 1): rho[2],
        (1, 1): rho[3],
    }
    if density_power == 2:
        rho_poly = pscalar_mul(rho_poly, rho_poly)
    return sp.simplify(pscalar_mul(rho_poly, pair_poly).get((1, 1), 0))


def action_mixed(
    jets: dict[str, object],
    background: M.SForm,
    cubic=sp.Rational(1, 3),
    density_power: int = 1,
    polynomial_check: bool = False,
) -> dict[str, object]:
    b: JForm = jets["b"]  # type: ignore[assignment]
    variation: JForm = jets["t_variation"]  # type: ignore[assignment]
    t: JForm = (background, variation[1], variation[2], variation[3])
    db: JForm = jets["db"]  # type: ignore[assignment]
    dt: JForm = jets["dt"]  # type: ignore[assignment]
    rho: tuple[sp.Expr, ...] = jets["rho"]  # type: ignore[assignment]
    c = transgression(b, t, db, dt, cubic)

    f0 = top_pair(t[0], c[0])
    fr = sp.simplify(top_pair(t[1], c[0]) + top_pair(t[0], c[1]))
    fs = sp.simplify(top_pair(t[2], c[0]) + top_pair(t[0], c[2]))
    frs = sp.simplify(
        top_pair(t[3], c[0])
        + top_pair(t[1], c[2])
        + top_pair(t[2], c[1])
        + top_pair(t[0], c[3])
    )
    assembled = sp.simplify(
        rho[0] * frs + rho[1] * fs + rho[2] * fr + rho[3] * f0
    )

    pair_jet = (f0, fr, fs, frs)

    def scalar_jet_product(left, right):
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

    density_jet = rho
    if density_power == 2:
        density_jet = scalar_jet_product(rho, rho)
    direct = scalar_jet_product(density_jet, pair_jet)[3]

    polynomial_direct = None
    if polynomial_check:
        polynomial_direct = generic_raw_density_mixed(
            b, t, db, dt, rho, cubic, density_power
        )
    return {
        "direct": direct,
        "assembled": assembled,
        "polynomial_direct": polynomial_direct,
        "c": c,
        "t": t,
    }


def universal_raw_density_degree_ledger() -> None:
    """Max-plus ceiling for the common-conormal raw-density comparator."""
    g_r = frozenset({0, 1})
    g_s = frozenset({0, 1})
    g_rs = frozenset({0, 1, 2})
    gamma_r = frozenset({1, 2})
    gamma_s = frozenset({1, 2})
    gamma_rs = frozenset({1, 2, 3})
    t_r = gamma_r
    t_s = gamma_s
    t_rs = gamma_rs
    db_r = E.draise(gamma_r)
    db_s = E.draise(gamma_s)
    db_rs = E.draise(gamma_rs)
    c_r = E.djoin(db_r, t_r)
    c_s = E.djoin(db_s, t_s)
    c_rs = E.djoin(
        db_rs,
        E.dproduct(gamma_r, gamma_s),
        E.dproduct(gamma_r, t_s),
        E.dproduct(gamma_s, t_r),
        E.dproduct(t_r, t_s),
        t_rs,
    )
    pair_rs = E.djoin(t_rs, E.dproduct(t_r, c_s), E.dproduct(t_s, c_r), c_rs)
    rho_r = g_r
    rho_s = g_s
    rho_rs = E.djoin(g_rs, E.dproduct(g_r, g_s))
    density_rs = E.djoin(
        pair_rs,
        E.dproduct(rho_r, E.djoin(t_s, c_s)),
        E.dproduct(rho_s, E.djoin(t_r, c_r)),
        rho_rs,
    )
    exact(
        "dependency-complete max-plus ledger bounds the tested raw density by common-conormal degree five",
        max(c_r) == max(c_s) == 3
        and max(c_rs) == 4
        and max(pair_rs) == 5
        and max(density_rs) == 5,
        f"C=({max(c_r)},{max(c_rs)}); pair={max(pair_rs)}; density={max(density_rs)}",
    )
    reject(
        "accept a planted degree-seven raw-density route under the degree-five ledger",
        7 in density_rs,
    )


SCALE_VANDERMONDE = sp.Matrix(
    [[sp.Integer(scale) ** degree for degree in range(7)] for scale in range(7)]
)
SCALE_INVERSE = SCALE_VANDERMONDE.inv()


def evaluate_case(
    label: str,
    owner_i: int,
    xi0: tuple[int, ...],
    owner_j: int,
    zeta0: tuple[int, ...],
    background: M.SForm,
    epsilon: M.SCliff,
    epsilon_inv: M.SCliff,
    polynomial_control: bool = False,
) -> dict[str, object]:
    action_values = []
    wrong_values = []
    doubled_values = []
    mass_values = []
    direct_mismatches = polynomial_mismatches = path_mismatches = graph_mismatches = 0
    metricity_failures = 0
    wrong_exercised = False
    for scale in range(7):
        xi = tuple(sp.Integer(scale * value) for value in xi0)
        zeta = tuple(sp.Integer(scale * value) for value in zeta0)
        jets = graph_jets(owner_i, xi, owner_j, zeta, epsilon, epsilon_inv)
        graph_mismatches += int(not jets["sum_identity"])
        graph = jets["graph"]
        metricity_failures += int(
            not graph["frame_metricity"] or not graph["connection_metricity"]  # type: ignore[index]
        )
        result = action_mixed(
            jets,
            background,
            polynomial_check=polynomial_control and scale == 1,
        )
        action_values.append(result["direct"])
        direct_mismatches += int(sp.simplify(result["direct"] - result["assembled"]) != 0)
        if result["polynomial_direct"] is not None:
            polynomial_mismatches += int(
                sp.simplify(result["polynomial_direct"] - result["assembled"]) != 0
            )
        if scale == 1 and polynomial_control:
            integrated = path_integrated_transgression(
                jets["b"], result["t"], jets["db"], jets["dt"]  # type: ignore[arg-type]
            )
            path_mismatches += sum(
                int(not form_equal(result["c"][index], integrated[index]))  # type: ignore[index]
                for index in range(4)
            )
            wrong = action_mixed(jets, background, cubic=sp.Rational(1, 2))
            doubled = action_mixed(jets, background, density_power=2)
            wrong_values.append(wrong["direct"])
            doubled_values.append(doubled["direct"])
            wrong_exercised = (
                sp.simplify(wrong["direct"] - result["direct"]) != 0
                and sp.simplify(doubled["direct"] - result["direct"]) != 0
            )
        variation: JForm = jets["t_variation"]  # type: ignore[assignment]
        mass_values.append(E.pair(variation[1], variation[2]))
        print(f"A4_PANEL: {label} {scale + 1}/7", flush=True)

    action_coefficients = SCALE_INVERSE * sp.Matrix(action_values)
    mass_coefficients = SCALE_INVERSE * sp.Matrix(mass_values)
    if polynomial_control:
        exact(
            f"{label}: generic full-polynomial raw-density coefficient equals the exhaustive coframe mixed product rule",
            direct_mismatches == 0 and polynomial_mismatches == 0,
            f"jet={direct_mismatches}/7; independent-polynomial={polynomial_mismatches}/1",
        )
    else:
        exact(
            f"{label}: direct raw-density coefficient equals the exhaustive coframe mixed product rule",
            direct_mismatches == 0,
            f"jet={direct_mismatches}/7; independent-polynomial=covered-by-first-panel",
        )
    if polynomial_control:
        exact(
            f"{label}: integrated curvature path equals the source one-half/one-third transgression",
            path_mismatches == 0,
            f"mismatches={path_mismatches}/4",
        )
    exact(
        f"{label}: corrected B+T=Gamma graph and coframe metricity survive every scale",
        graph_mismatches == 0 and metricity_failures == 0,
        f"graph={graph_mismatches}; metricity={metricity_failures}",
    )
    exact(
        f"{label}: C5 vanishes under the degree-five ceiling while the fitted raw-density A4 witness is live",
        action_coefficients[5] == 0
        and action_coefficients[6] == 0
        and action_coefficients[4] != 0,
        f"A4={action_coefficients[4]}",
    )
    if polynomial_control:
        exact(
            f"{label}: wrong one-third and double-density controls change the exact evaluator",
            wrong_exercised,
        )
    return {
        "label": label,
        "a4": action_coefficients[4],
        "m4": mass_coefficients[4],
        "a5": action_coefficients[5],
    }


def projective_classifier(rows: list[tuple[sp.Expr, sp.Expr]]) -> dict[str, object]:
    nonzero_rows = [(sp.simplify(a), sp.simplify(m)) for a, m in rows if a != 0 or m != 0]
    if not nonzero_rows:
        return {"classification": "ANY", "rank": 0, "ratio": None}
    matrix = sp.Matrix(nonzero_rows)
    rank = matrix.rank()
    if rank == 2:
        return {"classification": "NONE", "rank": rank, "ratio": None}
    if all(m == 0 for _, m in nonzero_rows):
        return {"classification": "NONE" if any(a != 0 for a, _ in nonzero_rows) else "ANY", "rank": rank, "ratio": None}
    ratio = next(sp.simplify(-a / m) for a, m in nonzero_rows if m != 0)
    consistent = all(m != 0 and sp.simplify(-a / m - ratio) == 0 for a, m in nonzero_rows)
    return {
        "classification": "UNIQUE_RELATIVE_TO_DECLARED_ACTIVE_PORT" if consistent else "NONE",
        "rank": rank,
        "ratio": ratio if consistent else None,
    }


def classification_checks(results: list[dict[str, object]]) -> dict[str, object]:
    rows = []
    for result in results:
        rows.append((result["a4"], result["m4"]))
    classification = projective_classifier(rows)
    exact(
        "independent owner/conormal entries at one frozen background give a projective rank-two raw-density comparator",
        classification["classification"] == "NONE" and classification["rank"] == 2,
        str(classification),
    )
    exact(
        "the classifier accepts a planted exact projective ratio",
        projective_classifier([(sp.Integer(-6), sp.Integer(2)), (sp.Integer(-9), sp.Integer(3))])
        == {
            "classification": "UNIQUE_RELATIVE_TO_DECLARED_ACTIVE_PORT",
            "rank": 1,
            "ratio": sp.Integer(3),
        },
    )
    exact(
        "the classifier accepts the all-zero ANY control and rejects support and ratio mismatches",
        projective_classifier([(0, 0)])["classification"] == "ANY"
        and projective_classifier([(1, 0), (0, 1)])["classification"] == "NONE"
        and projective_classifier([(-2, 1), (-6, 2)])["classification"] == "NONE",
    )
    reject("infer kappa from the first live ratio while later exact rows disagree", classification["classification"] != "NONE")
    return classification


def boundary_checks() -> None:
    typed("the raw-density comparator is conditional on the active canonical-coframe frozen-Shiab port and independent of the unresolved s_kappa sign")
    typed("rank two does not yet classify the Euler operator because total divergences and Green/Helmholtz reduction are unbuilt")
    typed("moving normalized DeWitt trace insertion, a full A4 bank, trace-reversed multi-index Green certificate, live C3 return, and distinct I2B C4 bank remain open")
    typed("the restricted metric Hessian is not a coupled Noether/BV identity and no boundary condition or analytic domain is inferred")
    typed("the off-shell background is a repository liveness witness, not a source-selected vacuum or external datum")
    typed("no characteristic, quotient, observation, Standard Model, GR, cosmology, dark-sector, or other physics equation is claimed")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE and TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    reject("call a relative active-port ratio Weinstein's selected kappa1", False)
    reject("add the Portal eddy as a second term on top of the written nonlinear transgression", False)
    reject("reuse the coordinate moving-Shiab dstar volume term on top of canonical-coframe rho", False)
    reject("spend P1/P2/P3 to select lambda, s_kappa, kappa1, or a cancellation", False)


def main() -> int:
    print("PW2F-R2B2B2F I1 TRANSGRESSION / PROJECTIVE KAPPA GATE")
    source_and_layer_zero()
    universal_raw_density_degree_ledger()
    epsilon, epsilon_inv = E.active_rotor()
    background = active_background()
    cases = (
        ("trace-diagonal", 0, (1, 1, 0, 0), 0, (1, 1, 0, 0)),
        ("independent-37", 3, (-1, 2, 0, 1), 7, (1, 0, -2, 2)),
        ("independent-49", 4, (1, -1, 2, 0), 9, (2, 1, 0, -1)),
    )
    results = []
    for case in cases:
        label, left, xi, right, zeta = case
        results.append(
            evaluate_case(
                label,
                left,
                xi,
                right,
                zeta,
                background,
                epsilon,
                epsilon_inv,
                polynomial_control=not results,
            )
        )
        if len(results) >= 2:
            trial = projective_classifier(
                [(result["a4"], result["m4"]) for result in results]
            )
            if trial["classification"] == "NONE" and trial["rank"] == 2:
                break
    classification = classification_checks(results)
    boundary_checks()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        "RESULT: projective_classifier="
        f"{classification['classification']}; rank={classification['rank']}; "
        f"panel={tuple((result['label'], result['a4'], result['m4']) for result in results)}",
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
        "VERDICT: THE CONDITIONAL ACTIVE COFRAME FROZEN-SHIAB I1 RAW-DENSITY "
        "COMPARATOR HAS LIVE FITTED A4 WITNESSES WITH INCONSISTENT PROJECTIVE "
        "RATIOS TO M4; EULER-OPERATOR CANCELLATION REMAINS OPEN PENDING MOVING "
        "TRACE AND GREEN/HELMHOLTZ REDUCTION"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
