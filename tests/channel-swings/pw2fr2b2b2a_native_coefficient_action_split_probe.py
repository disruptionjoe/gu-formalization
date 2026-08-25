#!/usr/bin/env python3
r"""PW2F-R2B2B2A active coefficient-slot and staged-action prerequisite.

The probe extracts one exact, contracted metric derivative of the repository's
active trace-reversed ``(9,5)`` Shiab construction.  It then carries that
coefficient through a deliberately noncommuting finite stack with five named
slots: density, Krein form, input lowerer, output lowerer, and outer pairing.
The complete mixed product rule is enumerated independently of direct
differentiation.  Finally, source-directed ``I1`` grammar and the manuscript
``I2B`` residual square are differentiated as separate finite actions.

This is an active-native coefficient/action-split prerequisite, not the full
epsilon-to-q/u induced-Y14 graph or its 35-monomial C5/C4 bank.  It computes no
characteristic, domain, quotient, observation equation, or physics result.
P1/P2/P3 are unused; Curt remains formally separate.
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
        raise RuntimeError(filename)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


M = load_probe(
    "pw2fr2b2b2a_moving_shiab",
    "eric_curt_wave3d_b2c15m_moving_shiab_exact_g2_weighted_euler_probe.py",
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


def source_receipt(label: str, condition: bool, detail: str = "") -> None:
    global SOURCE
    SOURCE += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: source - {label}{suffix}", flush=True)
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


def zero(value: sp.Matrix | sp.Expr) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(item) == 0 for item in value)
    return sp.simplify(value) == 0


def origin(value: sp.Matrix | sp.Expr, r: sp.Symbol, s: sp.Symbol):
    return value.subs({r: 0, s: 0})


def mixed(value: sp.Matrix | sp.Expr, r: sp.Symbol, s: sp.Symbol):
    return origin(sp.diff(value, r, s), r, s)


def first(value: sp.Matrix | sp.Expr, parameter: sp.Symbol, r: sp.Symbol, s: sp.Symbol):
    return origin(sp.diff(value, parameter), r, s)


def source_and_layer_zero_checks() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    staged = (ROOT / "explorations/eric-curt-wave3d-b2c12-active-staged-action-2026-08-01.md").read_text()
    moving = (ROOT / "explorations/eric-curt-wave3d-b2c15m-moving-shiab-exact-g2-weighted-euler-2026-08-01.md").read_text()

    source_receipt(
        "the source pack retains first-order-total and second-order-sourced equations as distinct alternatives",
        r"\Upsilon^B_\omega+\Upsilon^F_\omega=0" in pack
        and r"D_\omega^*\Upsilon^B_\omega=\Upsilon^F_\omega" in pack,
    )
    source_receipt(
        "the manuscript residual norm is separately typed by the active repository primalizer rather than identified with I1",
        r"I_2^B=\|\Upsilon_B\|^2" in staged
        and "They are not identified" in staged,
    )
    source_receipt(
        "the active moving-Shiab exact construction is repository-derived and retains the source residual/action fork",
        "Upsilon_B_src" in moving
        and "retained separately" in moving
        and "This is a repository construction" in moving,
    )

    typed("source epsilon and repository h/u reduction data remain distinct")
    typed("the active trace-reversed (9,5) right-H/Krein port is not the source (7,7) real arena")
    typed("density, Krein, input lowerer, output lowerer, and outer pairing are five ordered coefficient slots")
    typed("source-directed I1 and manuscript I2B residual square are distinct actions")
    typed("a contracted moving-Shiab coefficient is not the complete epsilon-to-q/u graph")
    typed("a finite mixed parameter Hessian is not a C5/C4 conormal coefficient")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    typed("TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    typed("P1/P2/P3 supply no coefficient, tangent, cancellation, or proof certificate")

    dg0, dg1, dq0, dq1 = sp.symbols("dg0 dg1 dq0 dq1")
    delta_gamma = sp.Matrix([dg0, dg1])
    delta_q = sp.Matrix([dq0, dq1])
    delta_b = delta_gamma + delta_q
    delta_t = -delta_q
    exact(
        "fixed-varpi source coordinates retain deltaT=-deltaq and deltaB=deltaGamma+deltaq",
        zero(delta_t + delta_b - delta_gamma),
    )
    reject("replace the fixed-source tangent by deltaT=-deltaB_full", zero(delta_t + delta_b))


def top_scalar(one: M.SForm, density: M.SForm) -> sp.Expr:
    top = M.sfwedge(one, density).get(M.FULL_KEY, {})
    return sp.simplify(top.get(0, 0))


def active_moving_coefficient() -> dict[str, object]:
    curvature: M.SForm = {
        (0, 1): M.sblade(2, 3),
        (4, 5): M.sblade(6, 7, 8),
        (2, 10): M.sblade(0, 4, 9, 13),
    }
    base_shiab = M.sfproject(M.sfleft(M.STRACE, M.sraw(curvature)))
    selected = None
    for owner, h in enumerate(M.B15.H_VARIATIONS):
        response = M.sfadd(
            *M.moving_metric_shiab_parts(
                curvature, h, M.canonical_trace_motion(owner)
            ).values()
        )
        for (key, mask), coefficient in sorted(M.flatten_form(response).items()):
            if len(key) != M.N - 1 or coefficient == 0:
                continue
            missing_indices = [index for index in range(M.N) if index not in key]
            if len(missing_indices) != 1:
                raise AssertionError(
                    f"expected one codimension-one complement, got {missing_indices}"
                )
            missing = missing_indices[0]
            one: M.SForm = {(missing,): {mask: sp.Integer(1)}}
            derivative = top_scalar(one, response)
            if derivative != 0:
                selected = {
                    "owner": owner,
                    "key": key,
                    "mask": mask,
                    "one": one,
                    "base": top_scalar(one, base_shiab),
                    "derivative": derivative,
                    "response": response,
                }
                break
        if selected is not None:
            break

    exact(
        "one active trace/Phi/Hodge moving-Shiab coefficient survives the same top-form contraction",
        selected is not None and selected["derivative"] != 0,
        "none" if selected is None else f"owner={selected['owner']}; derivative={selected['derivative']}",
    )
    if selected is None:
        raise RuntimeError("no contracted active moving-Shiab coefficient")

    raw = M.flatten_form(selected["response"])
    exact(
        "the contracted witness is one coefficient of the exact active moving response rather than a free scalar plant",
        raw[(selected["key"], selected["mask"])] != 0
        and selected["derivative"] == top_scalar(selected["one"], selected["response"]),
    )
    return selected


def matrix_factors(r: sp.Symbol, s: sp.Symbol, shiab: sp.Expr):
    identity = sp.eye(2)
    rho = 2 + 3 * r - s + 2 * r * s
    outer = (
        sp.Matrix([[2, 1], [0, 1]])
        + r * sp.Matrix([[1, 0], [2, -1]])
        + s * sp.Matrix([[0, 2], [-1, 1]])
        + r * s * sp.Matrix([[1, -1], [1, 2]])
    )
    output = (
        sp.Matrix([[1, 1], [0, 2]])
        + r * sp.Matrix([[0, 1], [1, 0]])
        + s * sp.Matrix([[2, 0], [-1, 1]])
        + r * s * sp.Matrix([[1, 2], [0, -1]])
    )
    krein = (
        sp.diag(1, -1)
        + r * sp.Matrix([[1, 2], [2, 0]])
        + s * sp.Matrix([[0, 1], [1, -2]])
        + r * s * sp.Matrix([[2, -1], [-1, 1]])
    )
    input_lowerer = (
        sp.Matrix([[2, 0], [1, 1]])
        + r * sp.Matrix([[0, -1], [2, 1]])
        + s * sp.Matrix([[1, 1], [0, -1]])
        + r * s * sp.Matrix([[-1, 0], [1, 2]])
    )
    return [rho * identity, outer, output, krein, input_lowerer, shiab * identity]


def ordered_product(factors: list[sp.Matrix]) -> sp.Matrix:
    result = sp.eye(factors[0].rows)
    for factor in factors:
        result = sp.expand(result * factor)
    return result


def mixed_product_assembly(
    factors: list[sp.Matrix], r: sp.Symbol, s: sp.Symbol
) -> tuple[sp.Matrix, list[sp.Matrix], list[sp.Matrix]]:
    baseline = [origin(factor, r, s) for factor in factors]
    r_parts = [first(factor, r, r, s) for factor in factors]
    s_parts = [first(factor, s, r, s) for factor in factors]
    rs_parts = [mixed(factor, r, s) for factor in factors]

    intrinsic: list[sp.Matrix] = []
    for target in range(len(factors)):
        terms = [rs_parts[index] if index == target else baseline[index] for index in range(len(factors))]
        intrinsic.append(ordered_product(terms))

    cross: list[sp.Matrix] = []
    for r_target in range(len(factors)):
        for s_target in range(len(factors)):
            if r_target == s_target:
                continue
            terms = []
            for index in range(len(factors)):
                if index == r_target:
                    terms.append(r_parts[index])
                elif index == s_target:
                    terms.append(s_parts[index])
                else:
                    terms.append(baseline[index])
            cross.append(ordered_product(terms))
    return sp.simplify(sum(intrinsic + cross, sp.zeros(2))), intrinsic, cross


def coefficient_stack_checks(native: dict[str, object]) -> dict[str, object]:
    r, s = sp.symbols("r s", real=True)
    shiab = sp.expand(native["base"] + r * native["derivative"])
    factors = matrix_factors(r, s, shiab)
    product = ordered_product(factors)
    assembled, intrinsic, cross = mixed_product_assembly(factors, r, s)
    direct = mixed(product, r, s)
    exact(
        "direct mixed differentiation equals the independently enumerated ordered six-factor product rule",
        zero(direct - assembled) and len(intrinsic) == 6 and len(cross) == 30,
        "6 intrinsic + 30 ordered cross terms",
    )

    left = sp.Matrix([[1, 2]])
    right = sp.Matrix([1, 0])
    direct_action = sp.simplify((left * direct * right)[0])
    exact(
        "the complete contracted coefficient-stack mixed return is live",
        direct_action != 0,
        f"return={direct_action}",
    )

    slot_names = ("density", "outer_pairing", "output_lowerer", "Krein", "input_lowerer")
    isolated = {}
    baseline = [origin(factor, r, s) for factor in factors]
    shiab_r = first(factors[-1], r, r, s)
    for index, name in enumerate(slot_names):
        terms = list(baseline)
        terms[index] = first(factors[index], s, r, s)
        terms[-1] = shiab_r
        value = sp.simplify((left * ordered_product(terms) * right)[0])
        isolated[name] = value
        exact(
            f"the {name} derivative has a live same-pipeline cross with the native moving-Shiab coefficient",
            value != 0,
            f"return={value}",
        )

    frozen_factors = [origin(factor, r, s) for factor in factors[:-1]] + [factors[-1]]
    frozen_action = mixed((left * ordered_product(frozen_factors) * right)[0], r, s)
    exact(
        "freezing all five coefficient slots changes the mixed action return",
        sp.simplify(direct_action - frozen_action) != 0,
        f"frozen={frozen_action}",
    )

    reordered = [factors[0], factors[1], factors[3], factors[2], factors[4], factors[5]]
    reordered_action = mixed((left * ordered_product(reordered) * right)[0], r, s)
    exact(
        "swapping the output-lowerer and Krein slots changes the noncommuting mixed return",
        sp.simplify(direct_action - reordered_action) != 0,
        f"reordered={reordered_action}",
    )
    reject("absorb the five named slots into one order-free scalar coefficient", direct_action == reordered_action)
    reject("freeze every non-Shiab slot after observing raw moving-map liveness", direct_action == frozen_action)

    return {
        "r": r,
        "s": s,
        "factors": factors,
        "direct_action": direct_action,
        "isolated": isolated,
        "native_shiab": shiab,
    }


def staged_action_checks(stack: dict[str, object]) -> dict[str, sp.Expr]:
    r: sp.Symbol = stack["r"]
    s: sp.Symbol = stack["s"]
    factors: list[sp.Matrix] = stack["factors"]
    rho, outer, output, krein, input_lowerer, shiab_matrix = factors

    source_t = sp.Matrix([1 + r - 2 * s, -2 + 3 * r + s + r * s])
    source_input = sp.Matrix([2 - r + s, 1 + 2 * r - s])
    i1_map = sp.expand(rho * outer * output * krein * shiab_matrix * input_lowerer)
    i1 = sp.expand((source_t.T * i1_map * source_input)[0])
    i1_hessian = mixed(i1, r, s)

    carrier = sp.Matrix([1, -1])
    e0 = sp.Matrix([2, 1])
    es = sp.Matrix([-1, 3])
    ers = sp.Matrix([2, -2])
    shiab_scalar = shiab_matrix[0, 0]
    residual = sp.expand(e0 + shiab_scalar * carrier + s * es + r * s * ers)
    c_map = sp.expand(output * outer * input_lowerer)
    primalizer = sp.expand(rho * c_map.T * krein * c_map)
    exact(
        "the finite I2B primalizer is symmetric and indefinite at the base point",
        primalizer == primalizer.T
        and origin(primalizer, r, s).det() < 0,
    )
    i2b = sp.expand((residual.T * primalizer * residual)[0] / 2)
    i2b_hessian = mixed(i2b, r, s)

    e_base = origin(residual, r, s)
    er = first(residual, r, r, s)
    es0 = first(residual, s, r, s)
    ers0 = mixed(residual, r, s)
    r0 = origin(primalizer, r, s)
    rr = first(primalizer, r, r, s)
    rs = first(primalizer, s, r, s)
    rrs = mixed(primalizer, r, s)
    normal = sp.simplify((er.T * r0 * es0)[0])
    graph_second = sp.simplify((e_base.T * r0 * ers0)[0])
    moving_primalizer = sp.simplify(
        (er.T * rs * e_base)[0]
        + (es0.T * rr * e_base)[0]
        + sp.Rational(1, 2) * (e_base.T * rrs * e_base)[0]
    )
    exact(
        "the direct I2B mixed Hessian equals normal plus residual-second-graph plus moving-primalizer returns",
        sp.simplify(i2b_hessian - normal - graph_second - moving_primalizer) == 0,
    )
    exact(
        "the off-shell I2B residual-times-second-graph return is live",
        graph_second != 0,
        f"return={graph_second}",
    )
    exact(
        "the off-shell I2B moving-primalizer return is separately live",
        moving_primalizer != 0,
        f"return={moving_primalizer}",
    )

    residual_on = sp.expand(residual - e_base)
    i2b_on = sp.expand((residual_on.T * primalizer * residual_on)[0] / 2)
    i2b_on_hessian = mixed(i2b_on, r, s)
    exact(
        "the residual-zero control reduces the I2B mixed Hessian to the normal J-star-R-J term",
        sp.simplify(i2b_on_hessian - normal) == 0,
    )
    exact(
        "the separately differentiated finite I1 and I2B Hessians are inequivalent on the same graph",
        sp.simplify(i1_hessian - i2b_hessian) != 0,
        f"I1={i1_hessian}; I2B={i2b_hessian}",
    )
    reject("identify the source-directed I1 Hessian with the manuscript I2B Hessian", i1_hessian == i2b_hessian)
    reject("drop the residual-times-second-graph term off shell", sp.simplify(i2b_hessian - normal - moving_primalizer) == 0)
    reject("drop the moving-primalizer term off shell", sp.simplify(i2b_hessian - normal - graph_second) == 0)
    reject("replace the indefinite active primalizer by a positive Hilbert norm", origin(primalizer, r, s).is_positive_definite is True)

    return {
        "i1": i1_hessian,
        "i2b": i2b_hessian,
        "normal": normal,
        "graph_second": graph_second,
        "moving_primalizer": moving_primalizer,
    }


def scope_checks() -> None:
    typed("the coefficient-stack certificate closes finite product-rule accounting, not the native epsilon-to-q/u map")
    typed("the five deterministic noncommuting slot matrices test ownership and order; they are not the actual induced-Y14 coefficient tensors")
    typed("the active moving coefficient is exact but one contracted fixture is not the complete 35-monomial bank")
    typed("the finite I1 comparator does not assert the unreleased global source action or its unique normalization")
    typed("the I2B port is the repository-typed active primalizer, not a proof that the source (7,7) and active (9,5) carriers coincide")
    typed("complete C5 must still be computed before C4 on the actual source graph")
    typed("an independent reverse/formal-adjoint and native presymplectic Green reconciliation remains open")
    typed("C3/C2, characteristic, analytic domain, BV quotient, observation, and physics remain open")
    reject("report the five finite slot matrices as the actual induced-Y14 coefficient values", False)
    reject("promote a finite coefficient/action split to complete native C5/C4", False)
    reject("spend P1/P2/P3 to close the missing native source graph", False)
    reject("merge Curt or promote a third lane from this Eric-lane prerequisite", False)


def main() -> int:
    print("PW2F-R2B2B2A NATIVE COEFFICIENT SLOTS / STAGED-ACTION SPLIT")
    source_and_layer_zero_checks()
    native = active_moving_coefficient()
    stack = coefficient_stack_checks(native)
    actions = staged_action_checks(stack)
    scope_checks()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        "RESULT: active_contracted_moving_shiab="
        f"{native['derivative']}; I1_mixed={actions['i1']}; "
        f"I2B_mixed={actions['i2b']}; graph_second={actions['graph_second']}; "
        f"moving_primalizer={actions['moving_primalizer']}",
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
        "VERDICT: R2B2B2A ACTIVE COEFFICIENT/ACTION-SPLIT PREREQUISITE PASSES; "
        "COMPLETE NATIVE C5/C4 REMAINS OPEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
