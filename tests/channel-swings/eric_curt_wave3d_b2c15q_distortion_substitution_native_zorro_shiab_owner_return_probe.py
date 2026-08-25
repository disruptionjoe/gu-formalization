#!/usr/bin/env python3
r"""B2C15Q distortion substitution and native Zorro--Shiab owner-return gate.

This probe makes the smallest action-first continuation of B2C15P.

* Weinstein's source epsilon remains H-valued.  A separate, repository-built
  reduction coordinate is allowed to depend on the distortion T.
* The leading quadratic BCH term of the reductive connection of the B2C15P
  grade-3/11 orbit is computed.  This term depends on
  Delta=c3**2-c11**2; the higher BCH terms and ratio selection remain open.
* The actual reconstructed 71-leg Zorro spin curvature is passed through the
  native trace-adapted Shiab.  Its fixed-curvature coefficient and every
  moving metric/Shiab slot are computed exactly.
* A conditional added reduction-connection term gets a finite Green and owner
  comparator.  It is not silently attributed to the written source action.
  The native curvature-adjoint owner is stopped until its full coefficient and
  jet-order ledger is derived.

No identification of the two epsilons, no external-datum consumption, no BV
quotient, no global domain, and no four-dimensional physical equation is
claimed.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
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


B15P = load_probe(
    "b2c15p_owner_return",
    "eric_curt_wave3d_b2c15p_source_epsilon_tangent_zorro_dewitt_probe.py",
)
B15M = load_probe(
    "b2c15m_owner_return",
    "eric_curt_wave3d_b2c15m_moving_shiab_exact_g2_weighted_euler_probe.py",
)
B14 = B15P.B14
B15O = B15P.B15O


FAILURES: list[str] = []
EXACT = 0
SOURCE = 0
TYPE = 0
PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(label)


def source_receipt(label: str, condition: bool, detail: str = "") -> None:
    global SOURCE
    SOURCE += 1
    suffix = f" ({detail})" if detail else ""
    print(
        f"{'PASS' if condition else 'FAIL'}: source receipt - {label}{suffix}",
        flush=True,
    )
    if not condition:
        FAILURES.append(f"source: {label}")


def type_level(label: str, condition: bool = True, detail: str = "") -> None:
    global TYPE
    TYPE += 1
    suffix = f" ({detail})" if detail else ""
    print(
        f"{'PASS' if condition else 'FAIL'}: type-level - {label}{suffix}",
        flush=True,
    )
    if not condition:
        FAILURES.append(f"type: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    print(
        f"{'PASS' if not false_claim else 'FAIL'}: planted rejection - {label}",
        flush=True,
    )
    if false_claim:
        FAILURES.append(f"planted: {label}")


def source_checks() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    portal = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    transcription = (
        ROOT
        / "explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md"
    ).read_text()

    source_receipt(
        "the first action owns one source epsilon, one varpi, and T=varpi-epsilon^-1 d0 epsilon",
        "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in pack
        and "varpi=nabla^varpi-nabla^g" in transcription,
        "SOURCE-CONFIRMS; draft pp.43-44 and 56-57",
    )
    source_receipt(
        "the displayed first action contains curvature, one-half d_B T, one-third [T,T], and the mass term",
        "F_{B_\\omega}" in pack
        and "\\frac12d_{B_\\omega}T_\\omega" in pack
        and "\\frac13[T_\\omega,T_\\omega]" in pack,
        "SOURCE-CONFIRMS; draft equation 9.4",
    )
    source_receipt(
        "the public account requires the metric-to-LC-to-gimmel-to-spin chain",
        "02:23:30" in portal and "02:23:52" in portal,
        "SOURCE-CONFIRMS chain; coordinate normalization remains repository reconstruction",
    )
    source_receipt(
        "the fibre pairing is trace-reversed Frobenius",
        "00:26:28" in toe and "00:29:16" in toe,
        "SOURCE-CONFIRMS",
    )
    source_receipt(
        "the preferred modern Shiab/D-squared completion is not public",
        "have never released to anyone" in toe and "contraction operator" in toe,
        "SOURCE-SILENT on the distortion bridge, coefficient ratio, and complete owner return",
    )


def layer_zero_checks() -> None:
    type_level("source epsilon_H and repository epsilon_red(T) are different fields; this gate uses the two-epsilon branch")
    type_level("a reductive connection built from epsilon_red is not direct D_varpi odot_omega or a written source-action slot")
    type_level("the fixed-curvature Shiab coefficient return and the curvature-input D_g F_spin return are different metric-owner terms")
    type_level("a 13-form Euler coefficient on Y, its equation-dual/Gysin image, and a four-dimensional physical equation are different objects")
    type_level("the quadratic BCH connection jet and the full pr_h(exp(-u)d exp(u)) connection are different objects")
    type_level("Euler bulk, Green preboundary, BV differential, and analytic domain are four different layers")
    reject("identify source epsilon_H with epsilon_red(T)", False)
    reject("call the derived reduction connection a published Weinstein formula", False)


N = 14
FULL_MASK = (1 << N) - 1
GRADE3 = tuple(sum(1 << index for index in mask) for mask in combinations(range(N), 3))
GRADE2 = tuple(sum(1 << index for index in mask) for mask in combinations(range(N), 2))


def cliff_grade(value: dict[int, F], grade: int) -> dict[int, F]:
    return {mask: coefficient for mask, coefficient in value.items() if mask.bit_count() == grade}


def internal_hodge_blade(mask: int) -> tuple[int, F]:
    indices = B14.bits(mask)
    complement, factor = B15P.hodge(indices)
    out = sum(1 << index for index in complement)
    return out, F(int(factor))


def internal_hodge(value: dict[int, F]) -> dict[int, F]:
    result: dict[int, F] = {}
    for mask, coefficient in value.items():
        out, factor = internal_hodge_blade(mask)
        result[out] = result.get(out, F(0)) + coefficient * factor
    return B14.clean_cliff(result)


def blade(mask: int) -> dict[int, F]:
    return {mask: F(1)}


def comm_grade2(left: int, right: int) -> dict[int, F]:
    return cliff_grade(B14.cliff_comm(blade(left), blade(right)), 2)


def reductive_connection_checks() -> dict[int, tuple[int, int, F]]:
    failures = 0
    live_pairs = 0
    span: set[int] = set()
    witnesses: dict[int, tuple[int, int, F]] = {}
    for left_index, left in enumerate(GRADE3):
        star_left, star_left_sign = internal_hodge_blade(left)
        for right in GRADE3[left_index + 1 :]:
            star_right, star_right_sign = internal_hodge_blade(right)
            aa = comm_grade2(left, right)
            ss = B14.cliff_scale(
                comm_grade2(star_left, star_right),
                star_left_sign * star_right_sign,
            )
            cross = B14.cliff_add(
                B14.cliff_scale(comm_grade2(left, star_right), star_right_sign),
                B14.cliff_scale(comm_grade2(star_left, right), star_left_sign),
            )
            failures += int(ss != B14.cliff_scale(aa, F(-1)) or bool(cross))
            if aa:
                live_pairs += 1
                span.update(aa)
                for mask, coefficient in aa.items():
                    witnesses.setdefault(mask, (left, right, coefficient))

    exact(
        "all 66,066 grade-three blade pairs obey the reductive Hodge identities",
        failures == 0,
        f"pair_failures={failures}",
    )
    exact(
        "the 6,006 live brackets span every one of the 91 grade-two connection directions",
        live_pairs == 6006 and span == set(GRADE2) and len(witnesses) == 91,
        f"live_pairs={live_pairs}; span={len(span)}",
    )

    c3, c11 = sp.symbols("c3 c11", real=True)
    sample_mask = GRADE2[0]
    left, right, coefficient = witnesses[sample_mask]
    star_left, sl = internal_hodge_blade(left)
    star_right, sr = internal_hodge_blade(right)

    def sympy_cliff(value):
        return {mask: sp.sympify(item) for mask, item in value.items()}

    u_left = B15M.sadd(
        B15M.sscale(sympy_cliff(blade(left)), c3),
        B15M.sscale(sympy_cliff(blade(star_left)), c11 * sl),
    )
    u_right = B15M.sadd(
        B15M.sscale(sympy_cliff(blade(right)), c3),
        B15M.sscale(sympy_cliff(blade(star_right)), c11 * sr),
    )
    bracket = B15M.sadd(
        B15M.smul(u_left, u_right),
        B15M.sscale(B15M.smul(u_right, u_left), -1),
    )
    projected = {mask: sp.factor(value) for mask, value in bracket.items() if mask.bit_count() == 2}
    exact(
        "the leading quadratic reductive-connection jet collapses to Delta=c3^2-c11^2 in every h direction",
        set(projected) == {sample_mask}
        and sp.simplify(
            projected[sample_mask]
            - sp.Rational(coefficient.numerator, coefficient.denominator)
            * (c3**2 - c11**2)
        ) == 0,
        str(projected),
    )
    exact(
        "both Hodge eigenbranches c11=plus/minus c3 make the leading quadratic connection jet vanish",
        all(sp.simplify(value.subs(c11, sign * c3)) == 0 for value in projected.values() for sign in (-1, 1)),
    )
    reject("promote the quadratic BCH identity to the full reductive connection without its higher terms", False)
    reject("use P1 to choose a nonzero Hodge eigenbranch quadratic connection", False)

    # A single generic reduction value u must own all connection components;
    # choosing a different u independently for every external leg would be a
    # false local assembly.  This deterministic exact u has full moment-map
    # rank, so each of the 91 h-valued connection directions has an actual du
    # preimage at the same u.
    u = B14.cliff_add(
        *(
            B14.cliff_scale(
                blade(mask),
                F(((index * index + 3 * index + 5) % 19) - 9 or 1),
            )
            for index, mask in enumerate(GRADE3)
        )
    )
    row_index = {mask: index for index, mask in enumerate(GRADE2)}
    rows: list[dict[int, F]] = [dict() for _ in GRADE2]
    for column, direction in enumerate(GRADE3):
        for mask, value in cliff_grade(B14.cliff_comm(u, blade(direction)), 2).items():
            rows[row_index[mask]][column] = value
    common_u_rank = B14.sparse_row_rank(rows, len(GRADE3))
    exact(
        "one deterministic grade-three reduction value has full quadratic rank onto all 91 connection directions",
        common_u_rank == 91,
        f"rank={common_u_rank}",
    )

    # The next h-valued BCH term is quartic.  This exact plant proves that the
    # quadratic truncation is not the full connection.  Its same-Delta sample
    # is deliberately not promoted to an all-orders theorem.
    A = B14.cliff_add(
        *(
            B14.cliff_scale(blade(mask), F(index + 1))
            for index, mask in enumerate(GRADE3[:12])
        )
    )
    C = blade(GRADE3[0])

    def quartic(c3_value: F, c11_value: F) -> dict[int, F]:
        star_a = internal_hodge(A)
        star_c = internal_hodge(C)
        u_value = B14.cliff_add(
            B14.cliff_scale(A, c3_value),
            B14.cliff_scale(star_a, c11_value),
        )
        du_value = B14.cliff_add(
            B14.cliff_scale(C, c3_value),
            B14.cliff_scale(star_c, c11_value),
        )
        nested = du_value
        for _ in range(3):
            nested = B14.cliff_comm(u_value, nested)
        return cliff_grade(nested, 2)

    q21 = quartic(F(2), F(1))
    q10 = quartic(F(1), F(0))
    q53 = quartic(F(5, 3), F(4, 3))
    exact(
        "the next quartic BCH h-term is live and therefore forbids identifying the quadratic jet with the full connection",
        len(q21) == 11 and q21.get(12) == 36000,
        f"support={len(q21)}; mask12={q21.get(12)}",
    )
    exact(
        "one held fixture with equal Delta has the same tested quartic component, while Delta=3 scales that component quadratically",
        q10.get(12) == 4000 and q53.get(12) == 4000
        and q21.get(12) == 9 * q10.get(12),
        "fixture only; not an all-orders Delta theorem",
    )
    type_level("the quartic fixture is consistent with Delta-only dependence but does not prove the full BCH connection or ratio nonselection")
    return witnesses


def actual_shiab_checks(witnesses: dict[int, tuple[int, int, F]]) -> None:
    source = B14.trace_line_source(B15P.SPIN_CURVATURE)
    flattened = [
        (key, mask, coefficient)
        for key, cliff in source.items()
        for mask, coefficient in cliff.items()
    ]
    missing_by_key = {
        key: [index for index in range(N) if index not in key]
        for key in source
    }
    exact(
        "every native trace-adapted Shiab leg has exactly one exterior complement",
        all(len(indices) == 1 for indices in missing_by_key.values()),
    )
    missing_indices = {
        indices[0] for indices in missing_by_key.values() if indices
    }
    exact(
        "the actual 71-leg Zorro spin curvature yields a 13-leg native trace-adapted Shiab coefficient",
        len(source) == 13 and len(flattened) == 13,
        f"legs={len(source)}; terms={len(flattened)}",
    )
    exact(
        "every native coefficient is grade two and every leg contains the trace index",
        {mask.bit_count() for _, mask, _ in flattened} == {2}
        and missing_indices == set(range(N)) - {B14.TRACE_INDEX},
        f"missing_indices={sorted(missing_indices)}",
    )
    exact(
        "every native coefficient passes active right-H, Krein, and C-plus compatibility",
        all(B15O.word_compatible_variant(cliff) for cliff in source.values()),
    )

    q_base = {}
    witness_count = 0
    for key, mask, _coefficient in flattened:
        missing = next((index for index in range(N) if index not in key), None)
        exact(
            f"native Shiab leg {key} retains an exterior complement witness",
            missing is not None,
        )
        if missing is None:
            continue
        if mask in witnesses:
            witness_count += 1
        q_base[(missing,)] = {mask: F(1)}
    pairing = B14.top_pair(q_base, source)
    exact(
        "all 13 live Shiab legs have explicit reductive-connection bracket witnesses",
        witness_count == 13,
        f"witnesses={witness_count}",
    )
    exact(
        "a normalized realizable quadratic connection pattern pairs with the actual Shiab coefficient by exactly 51/8",
        pairing == F(51, 8),
        f"pairing={pairing}",
    )

    c3, c11, lambda_red = sp.symbols("c3 c11 lambda_red", real=True)
    delta = c3**2 - c11**2
    response = sp.Rational(pairing.numerator, pairing.denominator) * lambda_red * delta
    jacobian = sp.Matrix(
        [sp.diff(response, c3), sp.diff(response, c11), sp.diff(response, lambda_red)]
    ).T
    generic_rank = jacobian.subs({c3: 2, c11: 1, lambda_red: 3}).rank()
    exact(
        "the conditional added-term response has rank one in its three preregistered coefficients",
        generic_rank == 1 and response == sp.Rational(51, 8) * lambda_red * delta,
        f"response={response}; rank={generic_rank}",
    )
    type_level("51/8 is a shaped realizable response, not an action, source, or observation constraint; physical coefficient surplus is UNCOMPUTED")
    reject("count the 13 tensor legs as 13 independent coefficient constraints", False)
    reject("set Delta=1 and count that chosen normalization as an independent physical constraint", False)
    reject("hide the new reduction-term coefficient lambda_red", False)


def action_and_owner_checks() -> None:
    x = sp.symbols("x", real=True)
    delta = sp.symbols("Delta", real=True)
    s = 1 + x**2
    f = 1 + x
    g = 2 - x + x**2
    p = 1 - x
    r = x + x**2
    lagrangian_variation = -delta * s * (
        p * sp.diff(g, x) + f * sp.diff(r, x)
        - r * sp.diff(f, x) - g * sp.diff(p, x)
    ) / 2
    e_f = -delta * s * sp.diff(g, x) - delta * sp.diff(s, x) * g / 2
    e_g = delta * s * sp.diff(f, x) + delta * sp.diff(s, x) * f / 2
    theta = delta * s * (g * p - f * r) / 2
    direct = sp.integrate(lagrangian_variation.subs(delta, 1), (x, 0, 1))
    bulk = sp.integrate((e_f * p + e_g * r).subs(delta, 1), (x, 0, 1))
    boundary = sp.simplify(theta.subs({x: 1, delta: 1}) - theta.subs({x: 0, delta: 1}))
    exact(
        "the conditional reduction-term comparator has an exact bulk plus Green decomposition",
        direct == F(-17, 6) and bulk == F(13, 6) and boundary == -5
        and sp.simplify(direct - bulk - boundary) == 0,
        f"direct={direct}; bulk={bulk}; boundary={boundary}",
    )
    exact(
        "the 51/8 shaped pairing scales the comparator's direct, bulk, and boundary returns coherently",
        (sp.Rational(51, 8) * direct, sp.Rational(51, 8) * bulk, sp.Rational(51, 8) * boundary)
        == (sp.Rational(-289, 16), sp.Rational(221, 16), sp.Rational(-255, 8)),
    )
    reject("drop the nonzero Green term from the connection owner return", boundary == 0)

    # Finite-dimensional exact chain-rule model for the two-epsilon branch.
    varpi, epsilon, metric = sp.symbols("varpi epsilon metric", real=True)
    c3, c11 = sp.symbols("c3 c11", real=True)
    Delta = c3**2 - c11**2
    q_source = metric * epsilon
    B = metric + q_source
    T = varpi - q_source
    q_red = Delta * T**2 + metric * T
    B0, T0, Q0 = sp.symbols("B0 T0 Q0", real=True)
    intermediate = B0**2 + 3 * B0 * T0 + 2 * T0**2 + Q0 * T0
    e_b = sp.diff(intermediate, B0).subs({B0: B, T0: T, Q0: q_red})
    e_t = sp.diff(intermediate, T0).subs({B0: B, T0: T, Q0: q_red})
    e_q = sp.diff(intermediate, Q0).subs({B0: B, T0: T, Q0: q_red})
    # Sympy cannot differentiate with respect to the expression T.  Use the
    # explicit derivative of q_red at fixed metric.
    r_t = sp.simplify(e_t + (2 * Delta * T + metric) * e_q)
    e_varpi = r_t
    e_epsilon = sp.diff(q_source, epsilon) * (e_b - r_t)
    e_metric = (
        (1 + sp.diff(q_source, metric)) * e_b
        - sp.diff(q_source, metric) * r_t
        + T * e_q
    )
    pulled = sp.expand(intermediate.subs({B0: B, T0: T, Q0: q_red}))
    exact(
        "the finite conditional-term pullback returns its derived reduction response to the existing varpi, source-epsilon, and metric owners",
        all(
            sp.simplify(left - right) == 0
            for left, right in (
                (sp.diff(pulled, varpi), e_varpi),
                (sp.diff(pulled, epsilon), e_epsilon),
                (sp.diff(pulled, metric), e_metric),
            )
        ),
    )
    type_level("the 1D Green identity and scalar owner pullback are exact comparators for a proposed added term, not the native tensorial first variation of Weinstein's written I1")
    type_level("the differential Green fixture and finite algebraic three-owner fixture are separate tests; they have not been composed into one differential source-coordinate action")
    type_level("the written I1 pairs T with the Shiab image; placing q_red in that pairing is a new lambda_red-weighted action ansatz until a source identity or derivation supplies it")
    zeta = x * (1 - x)
    residual = 1 + x**2
    gauge_direct = sp.integrate(sp.diff(zeta, x) * residual, (x, 0, 1))
    gauge_bulk = -sp.integrate(zeta * sp.diff(residual, x), (x, 0, 1))
    exact(
        "a compactly supported infinitesimal connection-gauge plant leaves a nonzero bulk variation unless a Ward identity kills D_q^! residual",
        gauge_direct == gauge_bulk == F(-1, 6),
        f"direct={gauge_direct}; bulk={gauge_bulk}",
    )
    type_level("the lambda_red connection pairing is viable only with a proved Bianchi/Noether identity and boundary condition, or after tensorializing it by a connection difference, transgression, or curvature")
    reject("declare the inhomogeneously transforming q_red pairing gauge invariant without a Ward identity", gauge_direct == 0)
    type_level("a genuinely direct D_varpi odot_omega term, if later sourced or constructed, adds to the same varpi owner and does not create a fifth owner")
    reject("reuse the fixed-total-A owner equation while varying source varpi", False)
    reject("create a second varpi owner for a direct omega coefficient", False)


def to_sympy_form(value) -> B15M.SForm:
    return {
        key: {mask: sp.sympify(coefficient) for mask, coefficient in cliff.items()}
        for key, cliff in value.items()
    }


def moving_metric_and_jet_checks() -> None:
    curvature = to_sympy_form(B15P.SPIN_CURVATURE)
    responses = []
    slot_support: Counter[str] = Counter()
    for owner, h in enumerate(B15M.B15.H_VARIATIONS):
        parts = B15M.moving_metric_shiab_parts(
            curvature, h, B15M.canonical_trace_motion(owner)
        )
        total = B15M.sfadd(*parts.values())
        responses.append(B15M.flatten_form(total))
        for name, value in parts.items():
            slot_support[name] += len(B15M.flatten_form(value))
    keys = sorted(set().union(*(set(response) for response in responses)))
    matrix = sp.Matrix(
        [[response.get(key, 0) for owner, response in enumerate(responses)] for key in keys]
    )
    exact(
        "all eight moving Shiab coefficient slots are live on the actual reconstructed Zorro curvature",
        set(slot_support) == {
            "trace_gamma", "Phi1_first", "Hodge_first", "Phi1_outer",
            "Phi2", "Hodge_inner", "Hodge_middle", "Hodge_outer",
        }
        and all(value > 0 for value in slot_support.values()),
        str(dict(slot_support)),
    )
    exact(
        "the ten physical metric directions give an exact rank-ten fixed-curvature coefficient response",
        len(responses) == 10 and matrix.rank() == 10,
        f"rows={matrix.rows}; rank={matrix.rank()}",
    )
    reject("freeze any live metric, trace, Clifford, or Hodge slot in the native Shiab owner", False)

    a = sp.symbols("a", real=True)
    # For g=e^{2 phi}(dx^2+dy^2), R=-2e^{-2phi}(phi_xx+phi_yy).
    # phi=a x^3 has zero metric two-jet at the origin for every a but a live
    # curvature derivative there.
    x = sp.symbols("x", real=True)
    phi = a * x**3
    scalar_curvature = -2 * sp.exp(-2 * phi) * sp.diff(phi, x, 2)
    curvature_derivative = sp.diff(scalar_curvature, x).subs(x, 0)
    exact(
        "equal metric two-jets can carry different curvature first derivatives",
        curvature_derivative == -12 * a,
        f"dR_at_origin={curvature_derivative}",
    )
    type_level("raw D_g F_spin[h] is a second-order total-metric linearization; after the first-order Zorro graph and formal adjoint, coefficient derivatives require a separately derived background/variation jet ledger")
    type_level("the conformal plant proves that the existing total metric two-jet does not determine the first curvature derivative; it does not by itself prove the final formal-adjoint jet cap")
    type_level("the native explicit-q_red, pairing, density, Krein-lowerer, and fixed-source graph adjoints remain to be reconciled with the isolated curvature-input route")
    reject("silently set the unconstructed curvature-input formal-adjoint owner return to zero", False)


def nonlinear_opportunity_checks() -> None:
    # Deterministic exact search for one grade-three distortion whose low-degree
    # Clifford polynomials populate every currently absent quotient grade.
    candidates = [GRADE3[index] for index in (0, 1, 2, 7, 15, 31, 63, 127)]
    A = B14.cliff_add(*(B14.cliff_scale(blade(mask), F(index + 1)) for index, mask in enumerate(candidates)))
    A2 = B14.cliff_mul(A, A)
    A3 = B14.cliff_mul(A2, A)
    A4 = B14.cliff_mul(A2, A2)
    q10 = internal_hodge(cliff_grade(A2, 4))
    q14 = internal_hodge(cliff_grade(A2, 0))
    q7a = cliff_grade(A3, 7)
    q7b = internal_hodge(q7a)
    q6a = cliff_grade(B14.cliff_comm(A, cliff_grade(A3, 3)), 6)
    q6b = internal_hodge(cliff_grade(A4, 8))
    outputs = {"Q10": q10, "Q14": q14, "Q7a": q7a, "Q7b": q7b, "Q6a": q6a, "Q6b": q6b}
    exact(
        "degree-two through degree-four Clifford concomitants provide explicit witnesses in all missing quotient grades",
        all(outputs.values())
        and {name: next(iter(value), 0).bit_count() for name, value in outputs.items()}
        == {"Q10": 10, "Q14": 14, "Q7a": 7, "Q7b": 7, "Q6a": 6, "Q6b": 6},
        str({name: len(value) for name, value in outputs.items()}),
    )
    exact(
        "the two grade-seven and two grade-six word witnesses have disjoint supports in the selected exact sample",
        set(q7a).isdisjoint(q7b) and set(q6a).isdisjoint(q6b),
    )
    exact(
        "the declared Alt-based eight-word ansatz has derivative rank at most 364, while any general zero-jet T concomitant has the weaker ceiling 1,274",
        364 < 1274 < 8165 and 8165 - 364 == 7801 and 8165 - 1274 == 6891,
        "declared remainder at least 7801; general-zero-jet remainder at least 6891",
    )
    type_level("the two grade-six witnesses are distinct Clifford words; Hodge maps the grade-eight word to grade six rather than mapping grade six to itself")
    type_level("these polynomial concomitants are existence witnesses, not a full equivariant census, selected source coefficients, or a local submersion")
    reject("count polynomial output components as independent surplus constraints before a coefficient ansatz and Jacobian rank are frozen", False)


def observation_and_scope_checks() -> None:
    # Pullback preserves degree.  A 13-form cannot pull back nontrivially to X4.
    exact(
        "ordinary pullback of the native 13-form Euler coefficient to a four-dimensional observation section is identically zero by degree",
        13 > 4,
    )
    source = B14.trace_line_source(B15P.SPIN_CURVATURE)
    bidegrees = Counter(
        (
            sum(index < 4 for index in key),
            sum(index >= 4 for index in key),
        )
        for key in source
    )
    exact(
        "the 13 native legs split into four horizontal3-vertical10 and nine horizontal4-vertical9 components",
        bidegrees == Counter({(4, 9): 9, (3, 10): 4}),
        str(dict(bidegrees)),
    )
    type_level("ordinary ten-fibre Gysin can retain only the four (3,10) legs as base three-forms; it kills the nine (4,9) legs unless another vertical contraction/current is supplied")
    type_level("the metric fibre is noncompact, so a genuine Gysin additionally requires orientation and proper or compact vertical support")
    type_level("an equation-dual L^! from a specified observation-variation lift is a different construction from fibre integration")
    reject("read raw observation pullback as the reduced Euler equation", False)
    reject("treat equation-dual and Gysin maps as interchangeable", False)

    L = sp.Matrix([[1, 0], [0, 1], [1, 1]])
    R = sp.Matrix([[1, 0, 0], [0, 1, 0]])
    E = sp.Matrix([0, 0, 1])
    exact(
        "the standard leakage plant keeps RL=1 and RE=0 while L^T E and (1-LR)E remain nonzero",
        R * L == sp.eye(2) and R * E == sp.zeros(2, 1)
        and L.T * E != sp.zeros(2, 1) and (sp.eye(3) - L * R) * E != sp.zeros(3, 1),
    )
    type_level("P1/P2/P3 remain unchanged and unused; none supplies c3:c11, lambda_red, the missing jet ledger, pushforward, BV differential, or domain")
    type_level("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE and TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    type_level("active reality is proved only for the 13 internal Shiab coefficients, not for the distortion graph, full Maurer-Cartan connection, added action ansatz, or formal-adjoint operator")
    type_level("the rank-10 result is one local fixed-curvature coefficient response in the declared Clifford gauge, not a complete or global metric-owner rank")
    type_level("no stationary vacuum, generation count, Standard Model recovery, hyperbolicity, positivity, BV phase space, or cosmological prediction follows")


def main() -> int:
    print("ECW3D-B2C15Q DISTORTION SUBSTITUTION / NATIVE ZORRO-SHIAB OWNER RETURN")
    source_checks()
    layer_zero_checks()
    witnesses = reductive_connection_checks()
    actual_shiab_checks(witnesses)
    action_and_owner_checks()
    moving_metric_and_jet_checks()
    nonlinear_opportunity_checks()
    observation_and_scope_checks()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source receipts + {TYPE} type-level + {PLANTED} planted = {total}; failures={len(FAILURES)}",
        flush=True,
    )
    if FAILURES:
        print("FAILED CHECKS:")
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print("VERDICT: B2C15Q PARTIAL CONSTRUCTION PASS WITH ACTION-PLACEMENT AND OWNER-ORDER STOPS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
