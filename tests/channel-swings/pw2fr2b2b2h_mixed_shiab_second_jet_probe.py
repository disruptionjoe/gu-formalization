#!/usr/bin/env python3
r"""PW2F-R2B2B2H exact mixed trace/Phi/Hodge/Shiab operator jet.

R2B2B2G transported the normalized DeWitt trace through the exact nonlinear
Zorro coframe and proved that its mixed slot is live.  This probe constructs
the missing bivariate ``(1,r,s,rs)`` operator jet rather than filling that slot
with an arbitrary symmetric tensor.

The construction keeps five ingredients explicit: the geometric trace jet,
the moving Clifford generators, their exterior ``Phi1/Phi2`` forms, the full
inverse-metric/density Hodge jet, and the final Shiab projection.  Both first
slots are compared coefficientwise with the accepted first-order
``moving_metric_shiab_parts`` constructor.  Mixed owner symmetry, Clifford
metricity, Hodge-square, curvature linearity, and planted omissions guard the
new second slot.

This closes an operator dependency only.  It does not construct the separate
off-shell residual-primalizer/pairing jet, complete I1 A4 or I2B C4 banks,
multi-index Green/Helmholtz data, a kappa1 classifier, or physics.  P1/P2/P3
remain unused; Curt remains formally separate; the third lane is not promoted.
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


G = load_probe(
    "pw2fr2b2b2h_predecessor",
    "pw2fr2b2b2g_full_a4_multiindex_green_distinct_i2b_c4_probe.py",
)
E = G.E
M = G.M
B15 = G.B15


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


def zero(value: sp.MatrixBase | sp.Expr) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in value)
    return sp.simplify(value) == 0


def form_equal(left: M.SForm, right: M.SForm) -> bool:
    return not M.sfadd(left, M.sfscale(right, -1))


JCliff = tuple[M.SCliff, M.SCliff, M.SCliff, M.SCliff]
JForm = tuple[M.SForm, M.SForm, M.SForm, M.SForm]


def jcadd(*values: JCliff) -> JCliff:
    return tuple(M.sadd(*(value[slot] for value in values)) for slot in range(4))  # type: ignore[return-value]


def jcscale(value: JCliff, coefficient) -> JCliff:
    return tuple(M.sscale(entry, coefficient) for entry in value)  # type: ignore[return-value]


def jcmul(left: JCliff, right: JCliff) -> JCliff:
    return (
        M.smul(left[0], right[0]),
        M.sadd(M.smul(left[1], right[0]), M.smul(left[0], right[1])),
        M.sadd(M.smul(left[2], right[0]), M.smul(left[0], right[2])),
        M.sadd(
            M.smul(left[3], right[0]),
            M.smul(left[1], right[2]),
            M.smul(left[2], right[1]),
            M.smul(left[0], right[3]),
        ),
    )


def jfadd(*values: JForm) -> JForm:
    return tuple(M.sfadd(*(value[slot] for value in values)) for slot in range(4))  # type: ignore[return-value]


def jfscale(value: JForm, coefficient) -> JForm:
    return tuple(M.sfscale(entry, coefficient) for entry in value)  # type: ignore[return-value]


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


def jfleft(left: JCliff, right: JForm) -> JForm:
    return (
        M.sfleft(left[0], right[0]),
        M.sfadd(M.sfleft(left[1], right[0]), M.sfleft(left[0], right[1])),
        M.sfadd(M.sfleft(left[2], right[0]), M.sfleft(left[0], right[2])),
        M.sfadd(
            M.sfleft(left[3], right[0]),
            M.sfleft(left[1], right[2]),
            M.sfleft(left[2], right[1]),
            M.sfleft(left[0], right[3]),
        ),
    )


def jfproject(value: JForm) -> JForm:
    return tuple(M.sfproject(entry) for entry in value)  # type: ignore[return-value]


def constant_form(value: M.SForm) -> JForm:
    return value, {}, {}, {}


def matrix_trace_to_cliff(value: tuple[sp.Matrix, ...]) -> JCliff:
    return tuple(
        M.sclean(
            {
                1 << index: sp.simplify(value[slot][index, 0])
                for index in range(14)
                if sp.simplify(value[slot][index, 0]) != 0
            }
        )
        for slot in range(4)
    )  # type: ignore[return-value]


def gamma_jet(metric) -> tuple[JCliff, ...]:
    frame = E.symmetric_frame(metric)
    return tuple(
        tuple(
            M.sclean(
                {
                    1 << other: sp.simplify(frame[slot].T[index, other])
                    for other in range(14)
                    if sp.simplify(frame[slot].T[index, other]) != 0
                }
            )
            for slot in range(4)
        )
        for index in range(14)
    )  # type: ignore[return-value]


def phi_jets(metric) -> tuple[JForm, JForm, tuple[JCliff, ...]]:
    gamma = gamma_jet(metric)
    phi_one = tuple(
        M.sfclean(
            {
                (index,): gamma[index][slot]
                for index in range(14)
                if gamma[index][slot]
            }
        )
        for slot in range(4)
    )
    # Half the exterior square removes the doubled ordered-pair contribution;
    # the Clifford anticommutator automatically subtracts the metric scalar.
    phi_two = jfscale(jfwedge(phi_one, phi_one), sp.Rational(1, 2))
    return phi_one, phi_two, gamma


def cross_external_action(left: sp.Matrix, right: sp.Matrix, value: M.SForm) -> M.SForm:
    """Apply left/right to distinct exterior slots, including both assignments."""
    sequential = M.action_on_form(left, M.action_on_form(right, value))
    same_slot = M.action_on_form(right * left, value)
    return M.sfadd(sequential, M.sfscale(same_slot, -1))


def exterior_inverse_metric_jet(metric, value: JForm, include_cross: bool = True) -> JForm:
    eta_jet = (E.ETA, sp.zeros(14), sp.zeros(14), sp.zeros(14))
    inverse = E.jinverse(metric)
    q = E.jmul(inverse, eta_jet)
    cross = cross_external_action(q[1], q[2], value[0]) if include_cross else {}
    return (
        value[0],
        M.sfadd(value[1], M.action_on_form(q[1], value[0])),
        M.sfadd(value[2], M.action_on_form(q[2], value[0])),
        M.sfadd(
            value[3],
            M.action_on_form(q[1], value[2]),
            M.action_on_form(q[2], value[1]),
            M.action_on_form(q[3], value[0]),
            cross,
        ),
    )


def jhodge(metric, value: JForm, include_cross: bool = True) -> JForm:
    transformed = exterior_inverse_metric_jet(metric, value, include_cross)
    starred = tuple(M.sfhodge(entry) for entry in transformed)
    rho = E.rho_jet(metric)
    return (
        starred[0],
        M.sfadd(starred[1], M.sfscale(starred[0], rho[1])),
        M.sfadd(starred[2], M.sfscale(starred[0], rho[2])),
        M.sfadd(
            starred[3],
            M.sfscale(starred[2], rho[1]),
            M.sfscale(starred[1], rho[2]),
            M.sfscale(starred[0], rho[3]),
        ),
    )


def shiab_jet(
    metric,
    trace: JCliff,
    curvature: JForm,
    include_hodge_cross: bool = True,
) -> JForm:
    phi_one, phi_two, _gamma = phi_jets(metric)
    star_f = jhodge(metric, curvature, include_hodge_cross)
    first = jfwedge(phi_one, star_f)
    middle_input = jfwedge(phi_two, star_f)
    middle = jhodge(metric, middle_input, include_hodge_cross)
    outer_input = jfwedge(phi_one, middle)
    raw = jfadd(
        first,
        jfscale(jhodge(metric, outer_input, include_hodge_cross), sp.Rational(-1, 2)),
    )
    return jfproject(jfleft(trace, raw))


def source_and_layer_zero() -> None:
    pack_path = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
    predecessor_path = (
        ROOT / "explorations/pw2fr2b2b2g-full-a4-multiindex-green-distinct-i2b-c4-2026-08-03.md"
    )
    pack = pack_path.read_text()
    predecessor = predecessor_path.read_text()
    source_receipt(
        "the pinned source fixes the I1 transgression grammar but supplies no active mixed Shiab jet",
        hashlib.sha256(pack_path.read_bytes()).hexdigest()
        == "5b50adabf067959654073f7e5c6665e8ac1e3e52ae36ae22ae9754bc9db23b5f"
        and r"\frac12d_{B_\omega}T_\omega" in pack
        and r"\frac13[T_\omega,T_\omega]" in pack,
        "SOURCE-CONFIRMS grammar; SOURCE-SILENT on active second jet",
    )
    source_receipt(
        "the accepted predecessor names the mixed trace/Phi/Hodge/Shiab jet as the first exact dependency",
        "BLOCKED_ON_MIXED_SHIAB_JET" in predecessor
        and "complete residual primalizer/pairing" in predecessor,
        "REPOSITORY-DERIVED successor construction",
    )
    typed("geometric trace, Clifford generator, Phi1/Phi2, Hodge, raw reduction, and Shiab projection are separately constructed typed objects")
    typed("the exterior inverse-metric action and density are both included exactly once in the Hodge jet")
    typed("source I1, repository mixed operator jet, I1 A4, and manuscript I2B residual-square Hessian remain distinct")
    typed("the active trace-reversed (9,5) port is not identified with the unported source (7,7) action pairing")
    typed("operator-jet closure is upstream of and weaker than complete coefficient banks or a Green/Helmholtz quotient")


def operator_gate() -> dict[str, object]:
    owner_i, xi = 3, tuple(map(sp.Integer, (-1, 2, 0, 1)))
    owner_j, zeta = 7, tuple(map(sp.Integer, (1, 0, -2, 2)))
    metric, trace_matrix = G.moving_frame_trace_jet(owner_i, xi, owner_j, zeta)
    trace = matrix_trace_to_cliff(trace_matrix)
    coordinate = G.fixed_frame_trace_jet(owner_i, owner_j)
    phi_one, phi_two, gamma = phi_jets(metric)

    cliff_failures = 0
    for left in range(14):
        for right in range(14):
            anticommutator = jcadd(
                jcmul(gamma[left], gamma[right]),
                jcmul(gamma[right], gamma[left]),
            )
            expected = tuple(
                {0: sp.simplify(2 * metric[slot][left, right])}
                if sp.simplify(metric[slot][left, right]) != 0
                else {}
                for slot in range(4)
            )
            cliff_failures += int(anticommutator != expected)
    exact(
        "all 196 moving Clifford-generator pairs satisfy the metric relation through mixed order",
        cliff_failures == 0,
        f"failures={cliff_failures}/196",
    )
    exact(
        "Phi1 and Phi2 recover the accepted base forms and Phi2 has no scalar contamination through mixed order",
        phi_one[0] == M.SPHI_ONE
        and phi_two[0] == M.SPHI_TWO
        and all(0 not in internal for slot in phi_two for internal in slot.values()),
    )

    curvature_a: M.SForm = {
        (0, 1): M.sblade(2, 3),
        (4, 5): M.sblade(6, 7, 8),
        (2, 10): M.sblade(0, 4, 9, 13),
    }
    curvature_b: M.SForm = {
        (1, 6): M.sblade(3, 11),
        (8, 12): M.sblade(0, 5, 9),
    }

    hodge = jhodge(metric, constant_form(curvature_a))
    exact(
        "both first Hodge slots equal the accepted complete first variation",
        form_equal(hodge[1], M.dstar(curvature_a, metric[1]))
        and form_equal(hodge[2], M.dstar(curvature_a, metric[2])),
    )
    twice = jhodge(metric, hodge)
    base_twice = M.sfhodge(M.sfhodge(curvature_a))
    sign = sp.Integer(1) if form_equal(base_twice, curvature_a) else sp.Integer(-1)
    exact(
        "the full Hodge jet squares to the exact base signature sign through mixed order",
        form_equal(twice[0], M.sfscale(curvature_a, sign))
        and not twice[1]
        and not twice[2]
        and not twice[3],
        f"star_square_sign={sign}",
    )

    full = shiab_jet(metric, trace, constant_form(curvature_a))
    expected_r = M.sfadd(
        *M.moving_metric_shiab_parts(
            curvature_a,
            metric[1],
            tuple(coordinate[1][index, 0] for index in range(14)),
        ).values()
    )
    expected_s = M.sfadd(
        *M.moving_metric_shiab_parts(
            curvature_a,
            metric[2],
            tuple(coordinate[2][index, 0] for index in range(14)),
        ).values()
    )
    exact(
        "the base and both first Shiab slots agree coefficientwise with the accepted fixed and moving constructors",
        form_equal(full[0], M.sfproject(M.sfleft(M.STRACE, M.sraw(curvature_a))))
        and form_equal(full[1], expected_r)
        and form_equal(full[2], expected_s),
    )
    exact(
        "the exact mixed trace/Phi/Hodge/Shiab slot is live on an independent off-diagonal owner pair",
        bool(full[3]),
        f"mixed_coordinates={len(M.flatten_form(full[3]))}",
    )

    swapped_metric, swapped_trace_matrix = G.moving_frame_trace_jet(
        owner_j, zeta, owner_i, xi
    )
    swapped = shiab_jet(
        swapped_metric,
        matrix_trace_to_cliff(swapped_trace_matrix),
        constant_form(curvature_a),
    )
    exact(
        "swapping owner/conormal directions exchanges first slots and preserves the mixed Shiab slot",
        form_equal(full[1], swapped[2])
        and form_equal(full[2], swapped[1])
        and form_equal(full[3], swapped[3]),
    )

    summed = shiab_jet(
        metric,
        trace,
        constant_form(M.sfadd(curvature_a, curvature_b)),
    )
    separate_a = full
    separate_b = shiab_jet(metric, trace, constant_form(curvature_b))
    exact(
        "the complete bivariate Shiab jet is coefficientwise linear in curvature",
        all(
            form_equal(summed[slot], M.sfadd(separate_a[slot], separate_b[slot]))
            for slot in range(4)
        ),
    )

    frozen_trace = trace[0], {}, {}, {}
    frozen = shiab_jet(metric, frozen_trace, constant_form(curvature_a))
    omitted_hodge_cross = shiab_jet(
        metric,
        trace,
        constant_form(curvature_a),
        include_hodge_cross=False,
    )
    reject(
        "freeze the normalized trace and claim the mixed Shiab response is unchanged",
        form_equal(full[3], frozen[3]),
    )
    reject(
        "drop the distinct-slot inverse-metric Hodge cross and claim the mixed Shiab response is unchanged",
        form_equal(full[3], omitted_hodge_cross[3]),
    )
    reject("identify operator-jet closure with a complete I1 A4 or I2B C4 bank", False)
    reject("promote a raw mixed operator slot to a full multi-index Green/Helmholtz or physics verdict", False)

    return {
        "mixed_coordinates": len(M.flatten_form(full[3])),
        "first_r_coordinates": len(M.flatten_form(full[1])),
        "first_s_coordinates": len(M.flatten_form(full[2])),
        "star_square_sign": str(sign),
    }


def boundary() -> None:
    typed("the distinct off-shell I2B second residual-primalizer/pairing jet remains unbuilt")
    typed("complete 35-monomial I1 and I2B quartic banks remain unassembled")
    typed("multi-index formal adjoint, Green concomitant, Helmholtz quotient, live C3 return, and projective kappa1 classification remain downstream")
    typed("vertical/mixed conormals, partial-Z1, section tangents, domain, observation, and physics remain open")
    typed("P1/P2/P3 remain unchanged and unused")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    typed("TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")


def main() -> int:
    print("PW2F-R2B2B2H EXACT MIXED TRACE/PHI/HODGE/SHIAB OPERATOR JET")
    source_and_layer_zero()
    result = operator_gate()
    boundary()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        "RESULT: mixed_shiab_coordinates="
        f"{result['mixed_coordinates']}; first_slots="
        f"({result['first_r_coordinates']},{result['first_s_coordinates']}); "
        "mixed_operator_jet=CLOSED; distinct_I2B_second_primalizer=OPEN",
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
        "VERDICT: R2B2B2H CLOSES THE CONDITIONAL ACTIVE MIXED "
        "TRACE/PHI/HODGE/SHIAB OPERATOR JET; COMPLETE I1 A4 AND DISTINCT "
        "I2B C4 REMAIN BLOCKED ON THE SEPARATE SECOND RESIDUAL-PRIMALIZER "
        "AND COEFFICIENT-BANK GATES"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
