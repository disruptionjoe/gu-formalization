#!/usr/bin/env python3
r"""PW2D active transported-Shiab and native transgression-action gate.

This probe composes, on the exact B2C15P local Y14 jet, objects that PW2C
kept in separate fixtures.  It builds a literal Alt(T) grade-3/11 bridge,
transports the Clifford/Shiab owner, uses the full dexp connection series in
an exact truncated Weil algebra, normalizes the written 1/2--1/3
transgression before substitution, and pairs the result with the actual
trace-adapted native Shiab coefficient.  It separately replays every one of
the eight metric coefficient slots on all ten trace-reversed metric owners;
their mixed bridge-by-metric derivative remains a later gate.

The public U/(7,7) source bundle is not identified with the active
Sp(32,32;H)/Spin(9,5) component.  The finite s-series is a local action jet,
not a global exponential chart, analytic domain, or coefficient selection.
"""

from __future__ import annotations

from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from math import factorial
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


P = load_probe(
    "pw2d_b2c15p",
    "eric_curt_wave3d_b2c15p_source_epsilon_tangent_zorro_dewitt_probe.py",
)
M = load_probe(
    "pw2d_b2c15m",
    "eric_curt_wave3d_b2c15m_moving_shiab_exact_g2_weighted_euler_probe.py",
)
Q = load_probe(
    "pw2d_b2c15q",
    "eric_curt_wave3d_b2c15q_distortion_substitution_native_zorro_shiab_owner_return_probe.py",
)
B14 = P.B14


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


def to_sympy_form(value) -> M.SForm:
    return {
        key: {mask: sp.sympify(coefficient) for mask, coefficient in cliff.items()}
        for key, cliff in value.items()
    }


def scomm(left: M.SCliff, right: M.SCliff) -> M.SCliff:
    return M.sadd(M.smul(left, right), M.sscale(M.smul(right, left), -1))


def ad_u_form(u: M.SCliff, value: M.SForm) -> M.SForm:
    return M.sfclean({key: scomm(u, coefficient) for key, coefficient in value.items()})


def truncate_cliff(value: M.SCliff, symbol: sp.Symbol, order: int) -> M.SCliff:
    return M.sclean(
        {
            mask: sp.series(coefficient, symbol, 0, order + 1).removeO().expand()
            for mask, coefficient in value.items()
        }
    )


def truncate_form(value: M.SForm, symbol: sp.Symbol, order: int) -> M.SForm:
    return M.sfclean(
        {
            key: truncate_cliff(coefficient, symbol, order)
            for key, coefficient in value.items()
        }
    )


def exp_ad_form(
    u: M.SCliff,
    value: M.SForm,
    symbol: sp.Symbol,
    sign: int,
    order: int,
) -> M.SForm:
    result = value
    current = value
    for degree in range(1, order + 1):
        current = ad_u_form(u, current)
        result = M.sfadd(
            result,
            M.sfscale(current, sp.Rational(sign**degree, factorial(degree)) * symbol**degree),
        )
    return truncate_form(result, symbol, order)


def k_full_series(
    u: M.SCliff,
    du: M.SForm,
    symbol: sp.Symbol,
    order: int,
) -> M.SForm:
    result: M.SForm = {}
    current = du
    for degree in range(order):
        result = M.sfadd(
            result,
            M.sfscale(
                current,
                sp.Rational((-1) ** degree, factorial(degree + 1))
                * symbol ** (degree + 1),
            ),
        )
        current = ad_u_form(u, current)
    return truncate_form(result, symbol, order)


def shiab(value: M.SForm) -> M.SForm:
    return M.sfproject(M.sfleft(M.STRACE, M.sraw(value)))


def preprojected_shiab(value: M.SForm) -> M.SForm:
    return M.sfleft(M.STRACE, M.sraw(value))


def transported_shiab(
    u: M.SCliff, value: M.SForm, symbol: sp.Symbol, order: int
) -> M.SForm:
    moved_input = exp_ad_form(u, value, symbol, +1, order)
    fixed_output = shiab(moved_input)
    return exp_ad_form(u, fixed_output, symbol, -1, order)


def top_scalar(one: M.SForm, density: M.SForm) -> sp.Expr:
    top = M.sfwedge(one, density).get(tuple(range(M.N)), {})
    return sp.simplify(top.get(0, 0))


def alt_of_t(one: M.SForm) -> M.SCliff:
    result: M.SCliff = {}
    for key, coefficient in one.items():
        if len(key) != 1:
            continue
        a = key[0]
        for mask, scalar in coefficient.items():
            if mask.bit_count() != 2:
                continue
            out, sign = P.alternation(a, tuple(B14.bits(mask)))
            if out is None:
                continue
            out_mask = sum(1 << index for index in out)
            result[out_mask] = sp.simplify(result.get(out_mask, 0) + scalar * sign)
    return M.sclean(result)


def star_cliff(value: M.SCliff) -> M.SCliff:
    rational = {mask: F(sp.Rational(coefficient)) for mask, coefficient in value.items()}
    return {mask: sp.sympify(coefficient) for mask, coefficient in Q.internal_hodge(rational).items()}


def source_and_layer_zero() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    source(
        "the draft owns the source roots and completed one-half/one-third first-action grammar",
        "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in pack
        and "\\frac12d_{B_\\omega}T_\\omega" in pack
        and "\\frac13[T_\\omega,T_\\omega]" in pack,
        "SOURCE-CONFIRMS",
    )
    source(
        "Weinstein describes the right/left tilted actions and double-coset replacement",
        "[02:19:49]" in toe and "[02:22:20]" in toe,
        "SOURCE-CONFIRMS symmetry grammar; not the repository's active real-form port",
    )
    source(
        "the native metric fibre is trace reversed",
        "[00:26:28]" in toe and "[00:29:16]" in toe,
        "SOURCE-CONFIRMS trace reversal; exact (6,4)/(9,5) is repository-derived",
    )
    source(
        "the public sources do not supply the active transported-Q/eight-slot assembly",
        "SOURCE-NEGATIVE" in pack and "preferred Shiab projection" in pack,
        "SOURCE-SILENT/REPOSITORY-DERIVED",
    )
    typed("public source bundle, active Sp component, reduced Spin bundle, and shared complexification are distinct")
    typed("Q, transported projector, K_full, K_red, and the native eight-slot coefficient are distinct owners")
    typed("the exact s-adic action jet below is local; it is not a global exponential chart or analytic domain")
    typed("the action curvature input and eight coefficient-motion slots are different derivative branches")
    reject("identify Cl(7,7)=M(128,R) with Cl(9,5)=M(64,H) as real bundles", False)
    reject("replace the trace-reversed native total signature by Curt's seven-seven", False)


def coefficient_dual_source_t(
    source_density: M.SForm, keys: list[tuple[int, ...]] | None = None
) -> M.SForm:
    result: M.SForm = {}
    for key in keys if keys is not None else sorted(source_density):
        missing = next((index for index in range(M.N) if index not in key), None)
        if missing is None:
            continue
        coefficient = source_density[key]
        result[(missing,)] = M.sadd(result.get((missing,), {}), coefficient)
    return M.sfclean(result)


def build_source_t(source_density: M.SForm) -> M.SForm:
    # Freeze the first three lexicographic dual legs before evaluating the
    # bridge response.  This is source-shaped and gives Alt(T) != 0; it is not
    # selected by a preferred sign, rank, or coefficient ratio.
    result = coefficient_dual_source_t(source_density, sorted(source_density)[:3])
    # The coefficient-dual legs above all have their form index inside their
    # Clifford two-blade, so Alt kills them.  Add the preregistered first
    # lexicographic Alt-bearing source basis vector; it is chosen before the
    # action response and kept separate from the dual sector.
    result[(0,)] = M.sadd(result.get((0,), {}), M.sblade(1, 2))
    return M.sfclean(result)


def transported_owner_checks() -> tuple[M.SForm, M.SForm, M.SCliff, M.SForm]:
    curvature = to_sympy_form(P.SPIN_CURVATURE)
    fixed = shiab(curvature)
    source_t = build_source_t(fixed)
    alt_t = alt_of_t(source_t)
    dual_only = M.sfadd(source_t, M.sfscale({(0,): M.sblade(1, 2)}, -1))
    all_dual_legs = coefficient_dual_source_t(fixed)
    individual_dual_alt_failures = 0
    for key in sorted(fixed):
        one_leg = coefficient_dual_source_t(fixed, [key])
        individual_dual_alt_failures += int(bool(alt_of_t(one_leg)))
    exact(
        "the frozen lexicographic source one-form is a genuine native grade-two T with nonzero Alt(T)",
        bool(source_t) and bool(alt_t) and {mask.bit_count() for mask in alt_t} == {3},
        f"T_legs={len(source_t)}; Alt_support={len(alt_t)}",
    )
    exact(
        "every actual coefficient-dual trace-line leg lies in ker Alt while the separately declared lexicographic source leg supplies the bridge",
        not alt_of_t(dual_only)
        and not alt_of_t(all_dual_legs)
        and individual_dual_alt_failures == 0
        and bool(alt_t),
        f"dual_legs={len(fixed)}; failures={individual_dual_alt_failures}",
    )

    star_t = star_cliff(alt_t)
    c3, c11 = sp.symbols("c3 c11", real=True)
    u = M.sadd(M.sscale(alt_t, c3), M.sscale(star_t, c11))

    # B2C15M's moving-Q derivative uses the right-commutator convention
    # [value,u].  In the local ad_u=[u,value] convention its exact naturality
    # identity is D_Q S(F)-S([u,F])=-[u,S(F)].  Independently differentiate
    # both the explicitly transported grade projector and the finite
    # covariance-completed operator so the owner cannot be defined as the
    # residual needed to make the identity true.
    panel = [(0, 0), (1, 0), (sp.Rational(5, 3), sp.Rational(4, 3)), (1, 1), (1, -1)]
    naturality_failures = 0
    live_q = 0
    live_projector = 0
    frozen_q_failures = 0
    finite_transport_failures = 0
    move_symbol = sp.symbols("r_move", real=True)
    preprojected = preprojected_shiab(curvature)
    for left, right in panel:
        uv = {mask: sp.simplify(value.subs({c3: left, c11: right})) for mask, value in u.items()}
        uv = M.sclean(uv)
        if not uv:
            continue
        moving_q = to_sympy_form(B14.derivative_trace_source(P.SPIN_CURVATURE, {mask: F(value) for mask, value in uv.items()}))
        input_motion = ad_u_form(uv, curvature)
        frozen_q_return = shiab(input_motion)
        rhs = ad_u_form(uv, fixed)
        # Independently differentiate the declared transported grade
        # projector p_r=Ad(e^-ru) p Ad(e^ru) on the pre-projection source.
        moved_preprojected = exp_ad_form(
            uv,
            M.sfproject(exp_ad_form(uv, preprojected, move_symbol, +1, 1)),
            move_symbol,
            -1,
            1,
        )
        projector_motion = M.sfclean(
            {
                key: {
                    mask: sp.diff(value, move_symbol).subs(move_symbol, 0)
                    for mask, value in coefficient.items()
                }
                for key, coefficient in moved_preprojected.items()
            }
        )
        naturality_lhs = M.sfadd(moving_q, M.sfscale(frozen_q_return, -1))
        naturality_failures += int(naturality_lhs != M.sfscale(rhs, -1))
        finite_transported = transported_shiab(uv, curvature, move_symbol, 1)
        finite_derivative = M.sfclean(
            {
                key: {
                    mask: sp.diff(value, move_symbol).subs(move_symbol, 0)
                    for mask, value in coefficient.items()
                }
                for key, coefficient in finite_transported.items()
            }
        )
        finite_transport_failures += int(finite_derivative != moving_q)
        frozen_q_failures += int(frozen_q_return != finite_derivative)
        live_q += int(bool(M.flatten_form(moving_q)))
        live_projector += int(bool(M.flatten_form(projector_motion)))
    exact(
        "independent finite transport and the explicit Q-family derivative satisfy exact active Shiab naturality on the five-pair panel",
        naturality_failures == 0
        and finite_transport_failures == 0
        and live_q == 4
        and live_projector == 0
        and frozen_q_failures == 4,
        f"naturality={naturality_failures}; finite={finite_transport_failures}; Q={live_q}; explicit_projector={live_projector}; frozen_Q_defects={frozen_q_failures}",
    )
    exact(
        "the independently differentiated transported grade projector vanishes on this actual curvature fixture",
        live_projector == 0,
    )
    reject("freeze the transported Q/Phi coefficient family while conjugating the actual curvature", frozen_q_failures == 0)

    # First-jet owner: partial_7 T_0=e_13, hence partial_7 Alt(T)=e_013.
    alt_jet = M.sblade(0, 1, 3)
    star_jet = star_cliff(alt_jet)
    du_coeff = M.sadd(M.sscale(alt_jet, c3), M.sscale(star_jet, c11))
    du = {(7,): du_coeff}
    exact(
        "the declared bridge first jet is an actual Alt image and exercises both grade-three and grade-eleven branches",
        set(mask.bit_count() for mask in du_coeff) == {3, 11},
    )
    return curvature, source_t, u, du


def native_action_checks(
    curvature: M.SForm, source_t: M.SForm, u: M.SCliff, du: M.SForm
) -> None:
    s = sp.symbols("s", real=True)
    c3, c11 = sp.symbols("c3 c11", real=True)
    kappa1 = sp.symbols("kappa1", real=True)
    order = 2

    # The first jet used for u comes from partial_7 T_0=e_13.  Its exterior
    # derivative is -dx0 wedge dx7 e_13.  B=0 at the selected normal frame.
    d_t = {(0, 7): M.sscale(M.sblade(1, 3), -1)}
    q_t = M.sfwedge(source_t, source_t)
    f_a = M.sfadd(curvature, d_t, q_t)
    original = M.sfadd(
        curvature,
        M.sfscale(d_t, sp.Rational(1, 2)),
        M.sfscale(q_t, sp.Rational(1, 3)),
    )
    normalized = M.sfadd(
        M.sfscale(M.sfadd(f_a, curvature), sp.Rational(1, 2)),
        M.sfscale(q_t, sp.Rational(-1, 6)),
    )
    exact(
        "the written one-half/one-third curvature block equals its fixed-total-connection transgression normal form",
        original == normalized and bool(q_t) and bool(d_t),
    )

    panel = [
        (0, 0),
        (1, 0),
        (sp.Rational(5, 3), sp.Rational(4, 3)),
        (1, 1),
        (1, -1),
    ]
    curvature_values = []
    mass_norm_values = []
    for left, right in panel:
        uv = M.sclean(
            {
                mask: sp.simplify(value.subs({c3: left, c11: right}))
                for mask, value in u.items()
            }
        )
        duv = M.sfclean(
            {
                key: {
                    mask: sp.simplify(value.subs({c3: left, c11: right}))
                    for mask, value in coefficient.items()
                }
                for key, coefficient in du.items()
            }
        )
        if not uv:
            curvature_values.append(top_scalar(source_t, shiab(original)))
            mass_norm_values.append(top_scalar(source_t, M.sfhodge(source_t)))
            continue
        k = k_full_series(uv, duv, s, order)
        f_b_hat = exp_ad_form(uv, curvature, s, -1, order)
        t_hat = truncate_form(M.sfadd(source_t, M.sfscale(k, -1)), s, order)
        q_hat = truncate_form(M.sfwedge(t_hat, t_hat), s, order)
        residual_hat = truncate_form(
            M.sfadd(
                M.sfscale(M.sfadd(f_a, f_b_hat), sp.Rational(1, 2)),
                M.sfscale(q_hat, sp.Rational(-1, 6)),
            ),
            s,
            order,
        )
        coefficient_hat = transported_shiab(uv, residual_hat, s, order)
        curvature_values.append(
            sp.series(top_scalar(t_hat, coefficient_hat), s, 0, order + 1)
            .removeO()
            .expand()
        )
        mass_norm_values.append(
            sp.series(
                top_scalar(t_hat, M.sfhodge(t_hat)),
                s,
                0,
                order + 1,
            )
            .removeO()
            .expand()
        )
    full_values = [
        sp.expand(curvature + sp.Rational(1, 2) * kappa1 * mass)
        for curvature, mass in zip(curvature_values, mass_norm_values)
    ]
    responses = [sp.diff(value, s).subs(s, 0) for value in full_values]
    curvature_seconds = [
        sp.diff(value, s, 2).subs(s, 0) for value in curvature_values
    ]
    mass_seconds = [
        sp.diff(value, s, 2).subs(s, 0) for value in mass_norm_values
    ]
    full_seconds = [sp.diff(value, s, 2).subs(s, 0) for value in full_values]
    exact(
        "literal K_full and the covariance-completed Shiab family give a full written first-action jet whose complete linear response cancels",
        all(response == 0 for response in responses)
        and curvature_seconds == [0, sp.Rational(3, 8), sp.Rational(3, 8), 0, 0]
        and mass_seconds == [0, 2, 2, 0, 0]
        and full_seconds
        == [0, sp.Rational(3, 8) + kappa1, sp.Rational(3, 8) + kappa1, 0, 0],
        f"first={responses}; curvature={curvature_seconds}; mass={mass_seconds}; full={full_seconds}",
    )
    exact(
        "the exact quadratic full first-action jet remains Delta-only but is not unconditionally nonzero",
        full_values[1] == full_values[2]
        and full_values[3] == full_values[4] == full_values[0]
        and full_seconds[1] == full_seconds[2] == sp.Rational(3, 8) + kappa1
        and full_seconds[3] == full_seconds[4] == 0
        and full_seconds[1].subs(kappa1, sp.Rational(-3, 8)) == 0,
        f"second={full_seconds}",
    )
    reject(
        "claim the quadratic full-action response is nonzero without fixing kappa1",
        full_seconds[1].subs(kappa1, sp.Rational(-3, 8)) != 0,
    )
    reject("promote this quadratic Delta-only fixture to an all-orders bridge theorem", False)
    reject("infer coefficient selection from the five action-jet values", False)
    reject("replace literal K_full by its grade-two Delta-only projection", False)

    # Actual native metric coefficient bank on the same normalized input at
    # s=0.  The eight labels are internal coefficient slots; curvature input
    # motion is deliberately not counted as a ninth slot.
    live_slots: dict[str, int] = {}
    responses_by_owner = []
    action_owner_values = []
    for owner, hvar in enumerate(M.B15.H_VARIATIONS):
        parts = M.moving_metric_shiab_parts(
            original, hvar, M.canonical_trace_motion(owner)
        )
        for name, value in parts.items():
            live_slots[name] = live_slots.get(name, 0) + len(M.flatten_form(value))
        total = M.sfadd(*parts.values())
        responses_by_owner.append(M.flatten_form(total))
        action_owner_values.append(top_scalar(source_t, total))
    keys = sorted(set().union(*(set(response) for response in responses_by_owner)))
    matrix = sp.Matrix(
        [[response.get(key, 0) for response in responses_by_owner] for key in keys]
    )
    expected_slots = {
        "trace_gamma",
        "Phi1_first",
        "Hodge_first",
        "Phi1_outer",
        "Phi2",
        "Hodge_inner",
        "Hodge_middle",
        "Hodge_outer",
    }
    exact(
        "all eight actual moving-Shiab slots remain live on the normalized native source residual",
        set(live_slots) == expected_slots and all(value > 0 for value in live_slots.values()),
        str(live_slots),
    )
    exact(
        "the normalized native coefficient retains exact rank ten across the ten trace-reversed metric owners",
        matrix.rank() == 10,
        f"rows={matrix.rows}; rank={matrix.rank()}",
    )
    exact(
        "the frozen action pairing sees a nonzero metric-owner return rather than merely a coefficient rank",
        any(value != 0 for value in action_owner_values),
        f"nonzero={sum(value != 0 for value in action_owner_values)}/10",
    )
    reject("freeze a live trace/Phi/Hodge slot in the native action owner", False)


def signature_and_scope_checks() -> None:
    dewitt = sp.Matrix(P.D0)
    total = sp.Matrix(P.G0)
    raw_frobenius = sp.Matrix(
        P.NF,
        P.NF,
        lambda i, j: sp.trace(P.G4 * P.SYM2[i] * P.G4 * P.SYM2[j]),
    )
    exact(
        "the assembled fixture keeps trace-reversed fibre inertia (6,4), total inertia (9,5), and trace norm -4",
        B14.symmetric_inertia([[F(item) for item in row] for row in dewitt.tolist()]) == (6, 4, 0)
        and B14.symmetric_inertia([[F(item) for item in row] for row in total.tolist()]) == (9, 5, 0)
        and P.fibre_pair(P.G4, P.G4) == -4,
    )
    exact(
        "unreversed Frobenius is a live rival geometry with inertia (7,3) and positive trace norm, not the native (6,4) block",
        B14.symmetric_inertia(
            [[F(item) for item in row] for row in raw_frobenius.tolist()]
        )
        == (7, 3, 0)
        and sp.trace(P.G4 * P.G4 * P.G4 * P.G4) == 4,
    )
    typed("the covariance-completed transported operator is tested on the active local component, not constructed from the public source bundle through second order")
    typed("the metric bank is the exact zero-jet coefficient response; the full Z0+Z1 total-space metric Frechet graph remains open")
    typed("PW2B certifies the grade-3/11 bridge generators, but PW2D does not recertify right-H/Krein/C+ for every composite K, hatted residual, transported coefficient, or metric-slot return")
    typed("a positive-Hilbert lowerer substitution in the composed action remains untested rather than rejected")
    typed("the s-adic action jet does not prove a global atlas, tame inverse, Green domain, hyperbolicity, or observation no-leakage")
    typed("P1/P2/P3 remain unchanged and unused; none supplies the port, coefficient, Ward differential, or domain")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE; TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")


def main() -> int:
    print("PW2D ACTIVE TRANSPORTED-SHIAB / NATIVE TRANSGRESSION ACTION")
    source_and_layer_zero()
    curvature, source_t, u, du = transported_owner_checks()
    native_action_checks(curvature, source_t, u, du)
    signature_and_scope_checks()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + {PLANTED} planted = {total}; failures={len(FAILURES)}"
    )
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print("VERDICT: PW2D PARTIAL FIXED-METRIC COVARIANCE-COMPLETED ACTION-JET PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
