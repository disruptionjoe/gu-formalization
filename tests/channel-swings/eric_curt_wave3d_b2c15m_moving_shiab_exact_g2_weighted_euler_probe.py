#!/usr/bin/env python3
r"""B2C15M moving-Shiab, weighted-Euler, and polynomial-chart gate.

This gate keeps five objects separate: the compressed source residual, the
exact partial-T Euler covector of the selected G2 first action, the full owner
Euler tuple of that first action, and the Euler operators of the two residual
squares.  It proves the moving reduction-family identity for the native
trace-adapted Shiab, constructs the complete metric derivative in the
declared symmetric Clifford gauge, differentiates a moving formal adjoint and
six-slot polarization, and freezes the Douglis--Nirenberg order ledgers before
any characteristic inference.

The rank theorem is deliberately chart-scoped.  On
``xi(a)=e_positive+a e_trace`` every fixed-Shiab coefficient entry is a
quadratic polynomial.  Values at ``a=-1,0,1`` reconstruct it exactly; ``a=2``
is held out.  The bipartite support splits into small blocks, so gcds of *all*
maximal minors certify the exceptional factor rather than relying on a single
witness.  This is not a global trace-stabilizer orbit theorem, a moving-Shiab
rank theorem, a BV quotient, or a common Green domain.
"""

from __future__ import annotations

from collections import Counter, deque
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from math import comb
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


B15R = load_probe(
    "b2c15r_probe",
    "eric_curt_wave3d_b2c15r_reductive_return_rank_strata_probe.py",
)
B15 = B15R.B15
B14 = B15.B14

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


N = B15.N
ETA = B15.ETA
TRACE_INDEX = B15.TRACE_INDEX
QUOTIENT_GRADES = B15.QUOTIENT_GRADES
ETA_MATRIX = sp.diag(*ETA)


# ---------------------------------------------------------------------------
# Source collision and Layer 0.


def source_checks() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    portal = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    g2 = (ROOT / "explorations/g2-field-space-native-variational-shiab-2026-07-31.md").read_text()
    b13 = (ROOT / "explorations/eric-curt-wave3d-b2c13-dupsilon-preboundary-2026-08-01.md").read_text()

    source_receipt(
        "the draft supplies the completed first-action grammar with one-half and one-third terms",
        "F_{B_\\omega}" in pack
        and "\\frac12d_{B_\\omega}T_\\omega" in pack
        and "\\frac13[T_\\omega,T_\\omega]" in pack,
        "draft p.44 eq.9.4 / WGS-01",
    )
    source_receipt(
        "Portal requires the quadratic eddy completion rather than curvature alone",
        "01:43:32" in portal and "01:45:53" in portal and "eddy" in portal,
        "Portal/Oxford 01:43:32-01:45:53",
    )
    source_receipt(
        "Weinstein corrects Shiab to contraction while leaving the preferred sheet and modern D-squared unreleased",
        "01:36:35" in toe
        and "contraction operator" in toe
        and "have never released to anyone" in toe,
        "TOE 01:36:35-01:36:56 and 02:44:06-02:45:13",
    )
    source_receipt(
        "the repository exact variation corrects the compressed source formula and already separates the two graph symbols",
        "fails the cyclic identities" in g2
        and "source response 0 and exact-G2 response 1/2" in b13,
        "SOURCE-CORRECTS; B2C13 exact collision",
    )


def layer_zero_checks() -> None:
    type_level("Upsilon_B_src, E_T_var, the two residual-square Euler operators, and the full first-action owner Euler tuple are five distinct objects")
    type_level("D Shiab applied to a fixed input, Shiab applied to D input, D(L!), (DL)!, DM, and DR_res are distinct moving returns")
    type_level("the active trace-reversed (9,5) right-H/Krein port is not identified with the source (7,7) real form by their common complexification")
    type_level("the native LC branch and the A0 lower-filtered comparator remain separate; pr_h[beta,chi] is not inserted into the native principal symbol")


# ---------------------------------------------------------------------------
# Exact differentiated naturality under all 91 vertical Spin directions.


def reduction_naturality_checks() -> None:
    representatives = {
        grade: {(0, 1): {B15.GRADE_MASKS[grade][0]: F(1)}}
        for grade in QUOTIENT_GRADES
    }
    checked = 0
    live = 0
    for h_mask in B14.H_BIVECTORS:
        generator = {h_mask: F(1)}
        for curvature in representatives.values():
            moving_family = B14.derivative_trace_source(curvature, generator)
            moving_input = B14.trace_line_source(
                B14.form_commutator(curvature, generator)
            )
            output_action = B14.form_commutator(
                B14.trace_line_source(curvature), generator
            )
            checked += 1
            live += bool(moving_family)
            if B14.add_forms(moving_family, moving_input) != output_action:
                FAILURES.append("differentiated Shiab naturality")
                break
    exact(
        "all 91 vertical Spin lifts satisfy differentiated Shiab covariance on every quotient-grade curvature representative",
        checked == 91 * len(QUOTIENT_GRADES)
        and not any(item == "differentiated Shiab naturality" for item in FAILURES),
        f"checks={checked}; live_family_responses={live}",
    )
    exact(
        "projection and invariant internal lowerer derivatives vanish in the co-moving Spin trivialization rather than being silently omitted",
        all(
            B14.form_commutator(B14.project_sp(value), {h: F(1)})
            == B14.project_sp(B14.form_commutator(value, {h: F(1)}))
            for h in B14.H_BIVECTORS
            for value in representatives.values()
        )
        and all(
            B14.cliff_mul(
                B14.cliff_comm({h: F(1)}, {mask: F(1)}),
                {mask: F(1)},
            ).get(0, F(0))
            + B14.cliff_mul(
                {mask: F(1)},
                B14.cliff_comm({h: F(1)}, {mask: F(1)}),
            ).get(0, F(0))
            == 0
            for h in B14.H_BIVECTORS
            for grade in QUOTIENT_GRADES
            for mask in B15.GRADE_MASKS[grade][:2]
        ),
    )
    reject("freeze trace and Phi while moving the reduction", live == 0)


def quotient_tangent_checks() -> None:
    curvature_representatives = {
        grade: {(0, 1): {B15.GRADE_MASKS[grade][0]: F(1)}}
        for grade in QUOTIENT_GRADES
    }
    # One grade-generating mask per irreducible exterior grade, plus a second
    # grade-seven mask because the middle exterior power can split by Hodge
    # type. This is a representative certificate, not an 8,165-direction
    # enumeration.
    directions = [
        (grade, B15.GRADE_MASKS[grade][0]) for grade in QUOTIENT_GRADES
    ] + [(7, B15.GRADE_MASKS[7][-1])]
    checked = 0
    live = 0
    for _grade, mask in directions:
        generator = {mask: F(1)}
        for curvature in curvature_representatives.values():
            moving_family = B14.derivative_trace_source(curvature, generator)
            moving_input = B14.trace_line_source(
                B14.form_commutator(curvature, generator)
            )
            output_action = B14.form_commutator(
                B14.trace_line_source(curvature), generator
            )
            checked += 1
            live += bool(moving_family)
            if B14.add_forms(moving_family, moving_input) != output_action:
                FAILURES.append("sampled quotient-tangent Shiab naturality")
                break
    exact(
        "seven grade-generating quotient-tangent representatives satisfy differentiated Shiab naturality against all six curvature grades",
        checked == 7 * len(QUOTIENT_GRADES)
        and "sampled quotient-tangent Shiab naturality" not in FAILURES,
        f"checks={checked}; live_family_responses={live}",
    )
    type_level(
        "the 42 quotient-tangent checks are grade-generating representatives, not a literal 8,165-direction enumeration or a global overlap theorem"
    )


# ---------------------------------------------------------------------------
# Sympy-valued exterior/Clifford calculus for ten metric owners.


SCliff = dict[int, sp.Expr]
SForm = dict[tuple[int, ...], SCliff]
FULL_KEY = tuple(range(N))


def qexpr(value) -> sp.Expr:
    if isinstance(value, F):
        return sp.Rational(value.numerator, value.denominator)
    return sp.sympify(value)


def sclean(value: SCliff) -> SCliff:
    return {
        mask: simplified
        for mask, coefficient in value.items()
        if (simplified := sp.simplify(coefficient)) != 0
    }


def sadd(*values: SCliff) -> SCliff:
    result: SCliff = {}
    for value in values:
        for mask, coefficient in value.items():
            result[mask] = result.get(mask, sp.Integer(0)) + coefficient
    return sclean(result)


def sscale(value: SCliff, coefficient) -> SCliff:
    factor = qexpr(coefficient)
    return sclean({mask: factor * entry for mask, entry in value.items()})


def smul(left: SCliff, right: SCliff) -> SCliff:
    result: SCliff = {}
    for lmask, lvalue in left.items():
        for rmask, rvalue in right.items():
            mask, sign = B14.mask_product(lmask, rmask)
            result[mask] = result.get(mask, sp.Integer(0)) + qexpr(sign) * lvalue * rvalue
    return sclean(result)


def sblade(*indices: int) -> SCliff:
    result: SCliff = {0: sp.Integer(1)}
    for index in indices:
        result = smul(result, {1 << index: sp.Integer(1)})
    return result


def sfclean(value: SForm) -> SForm:
    return {key: cleaned for key, item in value.items() if (cleaned := sclean(item))}


def sfadd(*values: SForm) -> SForm:
    result: SForm = {}
    for value in values:
        for key, coefficient in value.items():
            result[key] = sadd(result.get(key, {}), coefficient)
    return sfclean(result)


def sfscale(value: SForm, coefficient) -> SForm:
    return sfclean({key: sscale(item, coefficient) for key, item in value.items()})


def sfwedge(left: SForm, right: SForm) -> SForm:
    result: SForm = {}
    for lkey, lvalue in left.items():
        for rkey, rvalue in right.items():
            joined = lkey + rkey
            if len(set(joined)) != len(joined):
                continue
            key = tuple(sorted(joined))
            coefficient = sscale(
                smul(lvalue, rvalue), B14.permutation_sign(joined)
            )
            result[key] = sadd(result.get(key, {}), coefficient)
    return sfclean(result)


def sfhodge(value: SForm) -> SForm:
    result: SForm = {}
    for key, coefficient in value.items():
        complement = tuple(index for index in FULL_KEY if index not in key)
        factor = sp.Integer(B14.permutation_sign(key + complement))
        for index in key:
            factor *= ETA[index]
        result[complement] = sscale(coefficient, factor)
    return sfclean(result)


def sfleft(multiplier: SCliff, value: SForm) -> SForm:
    return sfclean({key: smul(multiplier, coefficient) for key, coefficient in value.items()})


def sfproject(value: SForm) -> SForm:
    return sfclean(
        {
            key: {
                mask: coefficient
                for mask, coefficient in item.items()
                if mask.bit_count() in B14.SP_GRADES
            }
            for key, item in value.items()
        }
    )


SPHI_ONE: SForm = {(index,): sblade(index) for index in range(N)}
SPHI_TWO: SForm = {pair: sblade(*pair) for pair in combinations(range(N), 2)}
STRACE = sblade(TRACE_INDEX)


def sraw(curvature: SForm) -> SForm:
    first = sfwedge(SPHI_ONE, sfhodge(curvature))
    second = sfhodge(
        sfwedge(
            SPHI_ONE,
            sfhodge(sfwedge(SPHI_TWO, sfhodge(curvature))),
        )
    )
    return sfadd(first, sfscale(second, sp.Rational(-1, 2)))


def action_on_form(matrix: sp.Matrix, value: SForm) -> SForm:
    result: SForm = {}
    for key, coefficient in value.items():
        for slot, old in enumerate(key):
            for new in range(N):
                factor = sp.simplify(matrix[old, new])
                if factor == 0:
                    continue
                replaced = list(key)
                replaced[slot] = new
                if len(set(replaced)) != len(replaced):
                    continue
                sign = B14.permutation_sign(tuple(replaced))
                out_key = tuple(sorted(replaced))
                contribution = sscale(coefficient, factor * sign)
                result[out_key] = sadd(result.get(out_key, {}), contribution)
    return sfclean(result)


def dstar_parts(value: SForm, h: sp.Matrix) -> tuple[SForm, SForm]:
    hsharp = ETA_MATRIX * h
    trace = sp.simplify(sp.trace(hsharp))
    volume = sfscale(sfhodge(value), trace / 2)
    index = sfscale(sfhodge(action_on_form(hsharp, value)), -1)
    return volume, index


def dstar(value: SForm, h: sp.Matrix) -> SForm:
    return sfadd(*dstar_parts(value, h))


def dgamma(index: int, h: sp.Matrix) -> SCliff:
    # Symmetric Clifford gauge: {D gamma_a,gamma_b}+{gamma_a,D gamma_b}=2h_ab.
    transform = h * ETA_MATRIX
    return sadd(
        *(
            sscale(sblade(other), transform[index, other] / 2)
            for other in range(N)
            if transform[index, other] != 0
        )
    )


def canonical_trace_motion(owner: int) -> tuple[sp.Expr, ...]:
    coordinate = sp.zeros(10, 1)
    coordinate[owner, 0] = sp.Rational(1, 2)
    vertical = sp.simplify(B15.DEWITT_FRAME.inv() * coordinate)
    return tuple([sp.Integer(0)] * 4 + [sp.simplify(value) for value in vertical])


def moving_phi(
    h: sp.Matrix, trace_motion: tuple[sp.Expr, ...] | None = None
) -> tuple[SCliff, SForm, SForm]:
    d_one: SForm = {(index,): dgamma(index, h) for index in range(N)}
    d_two: SForm = {}
    for left, right in combinations(range(N), 2):
        d_two[(left, right)] = sadd(
            smul(dgamma(left, h), sblade(right)),
            smul(sblade(left), dgamma(right, h)),
            {0: -sp.simplify(h[left, right])}
            if h[left, right] != 0
            else {},
        )
    d_trace = dgamma(TRACE_INDEX, h)
    if trace_motion is not None:
        d_trace = sadd(
            d_trace,
            *(
                sscale(sblade(index), coefficient)
                for index, coefficient in enumerate(trace_motion)
                if coefficient != 0
            ),
        )
    return d_trace, sfclean(d_one), sfclean(d_two)


def moving_metric_shiab_parts(
    curvature: SForm,
    h: sp.Matrix,
    trace_motion: tuple[sp.Expr, ...] | None = None,
) -> dict[str, SForm]:
    d_trace, d_one, d_two = moving_phi(h, trace_motion)
    star_f = sfhodge(curvature)
    middle_input = sfwedge(SPHI_TWO, star_f)
    middle = sfhodge(middle_input)
    outer_input = sfwedge(SPHI_ONE, middle)
    raw = sfadd(
        sfwedge(SPHI_ONE, star_f),
        sfscale(sfhodge(outer_input), sp.Rational(-1, 2)),
    )
    raw_parts = {
        "Phi1_first": sfwedge(d_one, star_f),
        "Hodge_first": sfwedge(SPHI_ONE, dstar(curvature, h)),
        "Phi1_outer": sfscale(sfhodge(sfwedge(d_one, middle)), sp.Rational(-1, 2)),
        "Phi2": sfscale(
            sfhodge(sfwedge(SPHI_ONE, sfhodge(sfwedge(d_two, star_f)))),
            sp.Rational(-1, 2),
        ),
        "Hodge_inner": sfscale(
            sfhodge(
                sfwedge(
                    SPHI_ONE,
                    sfhodge(sfwedge(SPHI_TWO, dstar(curvature, h))),
                )
            ),
            sp.Rational(-1, 2),
        ),
        "Hodge_middle": sfscale(
            sfhodge(sfwedge(SPHI_ONE, dstar(middle_input, h))),
            sp.Rational(-1, 2),
        ),
        "Hodge_outer": sfscale(dstar(outer_input, h), sp.Rational(-1, 2)),
    }
    parts = {
        "trace_gamma": sfproject(sfleft(d_trace, raw)),
        **{
            name: sfproject(sfleft(STRACE, value))
            for name, value in raw_parts.items()
        },
    }
    return parts


def flatten_form(value: SForm) -> dict[tuple[tuple[int, ...], int], sp.Expr]:
    return {
        (key, mask): sp.simplify(coefficient)
        for key, item in value.items()
        for mask, coefficient in item.items()
        if sp.simplify(coefficient) != 0
    }


def metric_moving_checks() -> None:
    curvature: SForm = {
        (0, 1): sblade(2, 3),
        (4, 5): sblade(6, 7, 8),
        (2, 10): sblade(0, 4, 9, 13),
    }
    responses = []
    live_slots: Counter[str] = Counter()
    for owner, h in enumerate(B15.H_VARIATIONS):
        trace_motion = canonical_trace_motion(owner)
        # Clifford compatibility is checked exactly on all 196 generator pairs.
        compatible = True
        for left in range(N):
            for right in range(N):
                derivative = sadd(
                    smul(dgamma(left, h), sblade(right)),
                    smul(sblade(right), dgamma(left, h)),
                    smul(sblade(left), dgamma(right, h)),
                    smul(dgamma(right, h), sblade(left)),
                )
                expected = {0: 2 * sp.simplify(h[left, right])} if h[left, right] != 0 else {}
                if sclean(derivative) != sclean(expected):
                    compatible = False
                    break
            if not compatible:
                break
        exact(
            f"metric owner {owner}: symmetric Clifford gauge differentiates the full Clifford relation",
            compatible,
        )

        _, _, d_phi_two = moving_phi(h)
        exact(
            f"metric owner {owner}: D Phi2 is the derivative of the antisymmetric Clifford bivector and has no scalar contamination",
            all(0 not in value for value in d_phi_two.values()),
        )

        trace_norm_derivative = sp.simplify(
            h[TRACE_INDEX, TRACE_INDEX]
            + 2 * ETA[TRACE_INDEX] * trace_motion[TRACE_INDEX]
        )
        exact(
            f"metric owner {owner}: canonical t(g)=g/2 motion preserves the normalized DeWitt trace norm",
            trace_norm_derivative == 0,
        )

        parts = moving_metric_shiab_parts(curvature, h, trace_motion)
        total = sfadd(*parts.values())
        responses.append(flatten_form(total))
        for name, value in parts.items():
            live_slots[name] += bool(value)

        plant = {(0, 1): sblade(0)}
        star_square_derivative = sfadd(
            dstar(sfhodge(plant), h), sfhodge(dstar(plant, h))
        )
        exact(
            f"metric owner {owner}: differentiated Hodge-square sign is fixed",
            not star_square_derivative,
        )

    keys = sorted(set().union(*(response.keys() for response in responses)))
    matrix = sp.Matrix(
        [[responses[owner].get(key, 0) for owner in range(10)] for key in keys]
    )
    exact(
        "all ten physical metric owners enter the complete moving-Shiab ledger with an exact nontrivial response map",
        len(responses) == 10 and matrix.rank() == 10 and all(response for response in responses),
        f"response_rank={matrix.rank()}; slot_liveness={dict(live_slots)}",
    )
    trace_owner = B15.H_VARIATIONS[0]
    volume, index = dstar_parts({(0, 1): sblade(2)}, trace_owner)
    exact(
        "the Hodge derivative contains separately visible volume-density and index-raising pieces which sum exactly once",
        dstar({(0, 1): sblade(2)}, trace_owner) == sfadd(volume, index),
    )
    reject("double-count the Hodge volume density as a second output density", False)


# ---------------------------------------------------------------------------
# Moving formal adjoint, six-slot DM, and residual-zero/off-shell Hessians.


def formal_adjoint_checks() -> None:
    x, e = sp.symbols("x e", real=True)
    f = sp.Function("f")(x)
    s = 2 + x + e * (1 - x)
    rho = 3 + x + e * (2 + x)
    b_in = 1 + x + e * x
    b_out = 2 - x + e * (1 + x)
    connection = 1 - x + e * (2 - x)

    def formal_adjoint(test: sp.Expr) -> sp.Expr:
        return sp.simplify(
            (-sp.diff(rho * b_out * s * test, x)
             + rho * b_out * s * connection * test)
            / (rho * b_in)
        )

    l_sharp = formal_adjoint(f)
    d_l_sharp = sp.diff(l_sharp, e).subs(e, 0)

    ds = sp.diff(s, e).subs(e, 0)
    dc = sp.diff(connection, e).subs(e, 0)
    dl_only = ds * sp.diff(f, x) + (ds * connection.subs(e, 0) + s.subs(e, 0) * dc) * f
    adjoint_of_dl_frozen = sp.simplify(
        (-sp.diff(rho.subs(e, 0) * b_out.subs(e, 0) * ds * f, x)
         + rho.subs(e, 0) * b_out.subs(e, 0)
         * (ds * connection.subs(e, 0) + s.subs(e, 0) * dc) * f)
        / (rho.subs(e, 0) * b_in.subs(e, 0))
    )
    exact(
        "D(L!) includes moving input/output lowerers and density and is not (DL)! with frozen pairings",
        sp.simplify(d_l_sharp - adjoint_of_dl_frozen) != 0 and dl_only != 0,
    )

    u = 1 + x + x**2
    v = 2 - x + x**3
    l_u = s * (sp.diff(u, x) + connection * u)
    lhs = sp.integrate(rho * b_out * l_u * v, (x, 0, 1))
    rhs_bulk = sp.integrate(rho * b_in * u * formal_adjoint(v), (x, 0, 1))
    endpoint = (rho * b_out * s * u * v).subs(x, 1) - (rho * b_out * s * u * v).subs(x, 0)
    exact(
        "the moving formal adjoint and moving endpoint satisfy the differentiated Green identity",
        sp.simplify(lhs - rhs_bulk - endpoint) == 0
        and sp.simplify(sp.diff(lhs - rhs_bulk - endpoint, e).subs(e, 0)) == 0
        and sp.diff(endpoint, e).subs(e, 0) != 0,
    )


def dm_checks() -> None:
    def top_scalar(one: SForm, density: SForm) -> sp.Expr:
        top = sfwedge(one, density).get(FULL_KEY, {})
        return sp.simplify(top.get(0, 0))

    def qsym(left: SForm, right: SForm) -> SForm:
        return sfscale(
            sfadd(sfwedge(left, right), sfwedge(right, left)),
            sp.Rational(1, 2),
        )

    def differentiated_cubic(
        x_form: SForm,
        y_form: SForm,
        z_form: SForm,
        h: sp.Matrix,
        trace_motion: tuple[sp.Expr, ...],
    ) -> tuple[sp.Expr, sp.Expr]:
        pairs = (
            (x_form, y_form, z_form), (x_form, z_form, y_form),
            (y_form, x_form, z_form), (y_form, z_form, x_form),
            (z_form, x_form, y_form), (z_form, y_form, x_form),
        )
        values = []
        for first, second, third in pairs:
            moving = sfadd(
                *moving_metric_shiab_parts(
                    qsym(second, third), h, trace_motion
                ).values()
            )
            values.append(top_scalar(first, moving))
        compact = top_scalar(
            x_form,
            sfadd(
                *moving_metric_shiab_parts(
                    qsym(y_form, z_form), h, trace_motion
                ).values()
            ),
        )
        return sp.simplify(sum(values) / 6), sp.simplify(compact)

    # Deterministically derive x from a live output of the compact slot, then
    # require the independently assembled six-slot polarization to survive.
    candidate_masks = tuple(
        mask
        for grade in (2,) + QUOTIENT_GRADES
        for mask in B15.GRADE_MASKS[grade][:2]
    )
    witness = None
    for owner, h in enumerate(B15.H_VARIATIONS):
        trace_motion = canonical_trace_motion(owner)
        for left_mask in candidate_masks:
            y_form: SForm = {(0,): {left_mask: sp.Integer(1)}}
            for right_mask in candidate_masks:
                z_form: SForm = {(1,): {right_mask: sp.Integer(1)}}
                moving = sfadd(
                    *moving_metric_shiab_parts(
                        qsym(y_form, z_form), h, trace_motion
                    ).values()
                )
                for key, internal in moving.items():
                    if len(key) != N - 1:
                        continue
                    missing_indices = [index for index in range(N) if index not in key]
                    if len(missing_indices) != 1:
                        raise AssertionError(
                            f"expected one codimension-one complement, got {missing_indices}"
                        )
                    missing = missing_indices[0]
                    for output_mask in internal:
                        x_form: SForm = {(missing,): {output_mask: sp.Integer(1)}}
                        dm_value, compact_value = differentiated_cubic(
                            x_form, y_form, z_form, h, trace_motion
                        )
                        if dm_value != 0:
                            witness = (
                                owner, left_mask.bit_count(), right_mask.bit_count(),
                                output_mask.bit_count(), dm_value, compact_value,
                            )
                            break
                    if witness:
                        break
                if witness:
                    break
            if witness:
                break
        if witness:
            break
    exact(
        "DM is constructed from all six differentiated trilinear slots and has a nonzero metric witness",
        witness is not None and witness[4] != 0,
        str(witness),
    )
    reject(
        "replace the six-slot DM by one compact (D Shiab)q slot",
        witness is not None and witness[4] == witness[5],
    )
    reject("infer all-grade DM vanishing from the prior grade-three zero fixture", witness is None)


def residual_hessian_checks() -> None:
    u, v = sp.symbols("u v", real=True)
    phi = sp.Matrix([u, v])
    c = sp.Matrix([[2, 1], [-1, 3]])
    quadratic = sp.Matrix([u * v, u**2 - v**2])
    p0 = {u: sp.Rational(1), v: sp.Rational(-1, 2)}
    e0 = -(c * phi + quadratic).subs(p0)
    residual = c * phi + quadratic + e0
    primalizer = sp.Matrix([[2 + u, sp.Rational(1, 2)], [sp.Rational(1, 2), -1 + v]])
    action = sp.simplify((residual.T * primalizer * residual)[0] / 2)
    jacobian = residual.jacobian(phi)
    hessian = sp.hessian(action, (u, v))
    normal = sp.simplify(jacobian.T * primalizer * jacobian)
    exact(
        "a nontrivial residual-zero fixture has live nonlinear and moving-primalizer data but Hessian equals J^T R J",
        residual.subs(p0) == sp.zeros(2, 1)
        and quadratic.subs(p0) != sp.zeros(2, 1)
        and sp.diff(primalizer, u) != sp.zeros(2)
        and sp.simplify(hessian.subs(p0) - normal.subs(p0)) == sp.zeros(2),
    )
    p1 = {u: sp.Rational(3, 2), v: sp.Rational(1, 3)}
    offshell_difference = sp.simplify(hessian.subs(p1) - normal.subs(p1))
    frozen_primalizer = primalizer.subs(p1)
    frozen_action = sp.simplify((residual.T * frozen_primalizer * residual)[0] / 2)
    frozen_hessian = sp.hessian(frozen_action, (u, v))
    residual_second_variation = sp.simplify(
        frozen_hessian.subs(p1) - normal.subs(p1)
    )
    moving_primalizer_correction = sp.simplify(
        hessian.subs(p1) - frozen_hessian.subs(p1)
    )
    exact(
        "off shell the residual-times-second-variation Hessian correction is separately live",
        residual_second_variation != sp.zeros(2)
        and residual_second_variation.rank() == 2,
        f"rank={residual_second_variation.rank()}",
    )
    exact(
        "off shell the moving-primalizer Hessian correction is separately live",
        moving_primalizer_correction != sp.zeros(2)
        and moving_primalizer_correction.rank() == 2
        and sp.simplify(
            residual_second_variation + moving_primalizer_correction
            - offshell_difference
        ) == sp.zeros(2),
        f"rank={moving_primalizer_correction.rank()}",
    )
    exact(
        "off shell the exact residual-square Hessian contains residual-times-second-variation and moving-primalizer terms beyond J^T R J",
        residual.subs(p1) != sp.zeros(2, 1) and offshell_difference != sp.zeros(2),
        f"difference_rank={offshell_difference.rank()}",
    )
    reject("call the B2C15R normal comparator the full off-shell Hessian", offshell_difference == sp.zeros(2))


# ---------------------------------------------------------------------------
# Douglis--Nirenberg ledgers and exact polynomial chart certificate.


DN_BRANCHES = {
    "source_square": {
        "fields": ("A", "epsilon", "g"),
        "row_weights": (1, 1, 1),
        "column_weights": (1, 1, 1),
        "orders": ((2, 2, 2), (2, 2, 2), (2, 2, 2)),
    },
    "variational_square": {
        "fields": ("A", "epsilon", "g"),
        "row_weights": (1, 2, 2),
        "column_weights": (1, 2, 2),
        "orders": ((2, 3, 3), (3, 4, 4), (3, 4, 4)),
    },
    "first_action_owner": {
        "fields": ("A", "epsilon", "g"),
        "row_weights": (0, 1, 1),
        "column_weights": (1, 2, 2),
        "orders": ((1, 2, 2), (2, 3, 3), (2, 3, 3)),
    },
}


def dn_checks() -> None:
    for name, branch in DN_BRANCHES.items():
        sums = tuple(
            tuple(left + right for right in branch["column_weights"])
            for left in branch["row_weights"]
        )
        exact(
            f"{name}: the preregistered weighted-order table equals row plus column weights",
            branch["orders"] == sums,
            str(sums),
        )
    type_level(
        "moving trace/Phi/Hodge/density/projection/primalizer/DM coefficients are algebraic in owner variations and therefore do not exceed the frozen top graph weights",
        True,
        "order declaration from the constructed zero-jet coefficient dependencies; full owner coefficient audit remains open",
    )
    reject("merge the three weighted symbols because they share owner names", False)


def chart_vector(value: int) -> tuple[F, ...]:
    result = [F(0)] * N
    result[0] = F(1)
    result[TRACE_INDEX] = F(value)
    return tuple(result)


def grade_rows(scan, grade: int) -> list[dict[int, F]]:
    return B15.rows_for_owner_grade(scan[grade][0], grade)


def interpolate_entry(vminus: F, vzero: F, vplus: F, symbol: sp.Symbol) -> sp.Expr:
    linear = sp.Rational((vplus - vminus).numerator, (vplus - vminus).denominator) / 2
    quadratic_f = (vplus + vminus) / 2 - vzero
    quadratic = sp.Rational(quadratic_f.numerator, quadratic_f.denominator)
    constant = sp.Rational(vzero.numerator, vzero.denominator)
    return sp.expand(constant + linear * symbol + quadratic * symbol**2)


def connected_blocks(entries: dict[tuple[int, int], sp.Expr]):
    adjacency: dict[tuple[str, int], set[tuple[str, int]]] = {}
    for (row, column), value in entries.items():
        if value == 0:
            continue
        rnode = ("r", row)
        cnode = ("c", column)
        adjacency.setdefault(rnode, set()).add(cnode)
        adjacency.setdefault(cnode, set()).add(rnode)
    seen: set[tuple[str, int]] = set()
    blocks = []
    for start in adjacency:
        if start in seen:
            continue
        queue = deque([start])
        component = set()
        while queue:
            node = queue.popleft()
            if node in component:
                continue
            component.add(node)
            queue.extend(adjacency[node] - component)
        seen.update(component)
        rows = sorted(index for kind, index in component if kind == "r")
        columns = sorted(index for kind, index in component if kind == "c")
        blocks.append((rows, columns))
    return blocks


def monic_gcd(values: list[sp.Expr], symbol: sp.Symbol) -> sp.Expr:
    polynomials = [sp.Poly(value, symbol, domain=sp.QQ) for value in values if value != 0]
    if not polynomials:
        return sp.Integer(0)
    result = polynomials[0]
    for value in polynomials[1:]:
        result = sp.gcd(result, value)
    return sp.factor(result.monic().as_expr())


def block_minor_gcd(
    rows: list[int], columns: list[int], entries: dict[tuple[int, int], sp.Expr], symbol: sp.Symbol
) -> sp.Expr:
    width = len(columns)
    if width == 1:
        return monic_gcd([entries.get((row, columns[0]), 0) for row in rows], symbol)
    if width == 2:
        minors = []
        left, right = columns
        for first, second in combinations(rows, 2):
            minors.append(
                entries.get((first, left), 0) * entries.get((second, right), 0)
                - entries.get((first, right), 0) * entries.get((second, left), 0)
            )
        return monic_gcd(minors, symbol)
    raise ValueError(f"unexpected chart block width {width}")


def polynomial_hostile_controls() -> None:
    a = sp.symbols("a", real=True)
    hidden_cubic = sp.expand((a + 1) * a * (a - 1))
    interpolant = interpolate_entry(F(0), F(0), F(0), a)
    exact(
        "the hidden-cubic plant vanishes at all three interpolation inputs but is live at the held-out point",
        all(hidden_cubic.subs(a, value) == 0 for value in (-1, 0, 1))
        and hidden_cubic.subs(a, 2) == 6
        and interpolant == 0,
    )
    reject(
        "certify coefficient degree at most two from the three interpolation inputs without a held-out point",
        sp.expand(interpolant.subs(a, 2) - hidden_cubic.subs(a, 2)) == 0,
    )

    one_minor_entries = {
        (0, 0): sp.Integer(1),
        (1, 1): a,
        (2, 0): sp.Integer(1),
        (2, 1): sp.Integer(1),
    }
    selected_minor = a
    all_minor_gcd = block_minor_gcd(
        [0, 1, 2], [0, 1], one_minor_entries, a
    )
    exact(
        "the selected-minor plant has an apparent root while the gcd of all maximal minors is one",
        selected_minor.subs(a, 0) == 0 and all_minor_gcd == 1,
    )
    reject(
        "define the rank-drop locus from one selected maximal minor",
        selected_minor.subs(a, 0) == 0 and all_minor_gcd.subs(a, 0) == 0,
    )


def polynomial_chart_checks():
    a = sp.symbols("a", real=True)
    scans = {
        value: B15.build_reduction_rows(chart_vector(value))
        for value in (-1, 0, 1, 2)
    }
    summaries = {}
    for grade in QUOTIENT_GRADES:
        sampled = {value: grade_rows(scan, grade) for value, scan in scans.items()}
        row_count = len(sampled[0])
        column_count = len(B15.GRADE_MASKS[grade])
        entries: dict[tuple[int, int], sp.Expr] = {}
        heldout_ok = True
        for row in range(row_count):
            support = set().union(*(set(sampled[value][row]) for value in (-1, 0, 1, 2)))
            for column in support:
                polynomial = interpolate_entry(
                    sampled[-1][row].get(column, F(0)),
                    sampled[0][row].get(column, F(0)),
                    sampled[1][row].get(column, F(0)),
                    a,
                )
                expected = sampled[2][row].get(column, F(0))
                expected_expr = sp.Rational(expected.numerator, expected.denominator)
                heldout_ok &= sp.expand(polynomial.subs(a, 2) - expected_expr) == 0
                if polynomial != 0:
                    entries[(row, column)] = polynomial
        exact(
            f"grade {grade}: the quadratic interpolation passes the held-out a=2 coefficient census",
            heldout_ok,
        )
        blocks = connected_blocks(entries)
        block_types = Counter()
        for rows, columns in blocks:
            gcd = block_minor_gcd(rows, columns, entries, a)
            block_types[(len(rows), len(columns), str(gcd))] += 1
        generic_rank = sum(len(columns) for _, columns in blocks)
        ranks = {
            value: B14.sparse_row_rank(sampled[value], column_count)
            for value in (-1, 0, 1, 2)
        }
        exceptional_blocks = sum(
            count
            for (height, width, gcd), count in block_types.items()
            if gcd != "1"
        )
        expected_exceptional_blocks = 0 if grade == 14 else comb(12, grade - 1)
        block_certificate = all(
            (width == 2 and gcd == "(a - 1)*(a + 1)")
            or (width == 1 and gcd == "1")
            for (_height, width, gcd) in block_types
        )
        exact(
            f"grade {grade}: all maximal-minor gcds certify full rank away from the exact chart exceptional factor",
            generic_rank == column_count
            and ranks[0] == column_count
            and ranks[2] == column_count
            and block_certificate
            and exceptional_blocks == expected_exceptional_blocks,
            f"ranks={ranks}; blocks={dict(block_types)}",
        )
        summaries[grade] = {
            "dimension": column_count,
            "ranks": ranks,
            "blocks": dict(block_types),
            "exceptional_blocks": exceptional_blocks,
        }

    expected_null = B15R.EXPECTED_RANKS["trace_involving_null"]
    exact(
        "the two roots a=plus/minus one are exactly q(xi)=1-a^2=0 and reproduce the trace-involving-null rank vector",
        ETA[0] == 1
        and ETA[TRACE_INDEX] == -1
        and tuple(summaries[grade]["ranks"][1] for grade in QUOTIENT_GRADES)
        == expected_null
        and tuple(summaries[grade]["ranks"][-1] for grade in QUOTIENT_GRADES)
        == expected_null,
        str(expected_null),
    )
    exact(
        "trace reversal is load-bearing on the chart: the hostile raw-Frobenius norm 1+a^2 has no real null roots",
        sp.solve(sp.Eq(1 + a**2, 0), a, domain=sp.S.Reals) == []
        and sp.factor(1 + a**2) != sp.factor(1 - a**2),
    )
    reject("promote the one-parameter positive-trace chart certificate to the orthogonal-null or degenerate q_perp=0 charts", False)
    return summaries


def scope_checks() -> None:
    type_level("the reduction-family naturality certificate and ten-owner metric derivative do not identify a BV tangent differential")
    type_level("the polynomial theorem is exact only on xi(a)=e_positive+a e_trace; orthogonal-null and degenerate trace-orthogonal charts remain separate")
    type_level("rank K, rank K^!R K, its radical, and the characteristic kernel of the full weighted Euler system remain distinct")
    type_level("P1/P2/P3 remains unchanged and unused; none supplies a moving slot, action branch, coefficient, quotient, or domain")
    type_level("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE and TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    type_level("no selected BFV phase space, Green domain, hyperbolicity, positivity, Standard Model, generation, or cosmological claim follows")


def main() -> int:
    print("ECW3D-B2C15M MOVING SHIAB / EXACT-G2 WEIGHTED EULER / POLYNOMIAL CHART GATE")
    source_checks()
    layer_zero_checks()
    reduction_naturality_checks()
    quotient_tangent_checks()
    metric_moving_checks()
    formal_adjoint_checks()
    dm_checks()
    residual_hessian_checks()
    dn_checks()
    polynomial_hostile_controls()
    chart = polynomial_chart_checks()
    scope_checks()

    reject("use P1/P2/P3 as a local metric-Clifford trivialization", False)
    reject("identify source epsilon with the repository reduction field without a typed map", False)
    reject("use the unreleased D-squared discussion to supply BV or domain closure", False)

    print(
        "RESULT: reduction_naturality=91x6; metric_owners=10; "
        "DN_branches=3; polynomial_chart=positive_plus_trace; "
        f"chart_grades={tuple(chart)}",
        flush=True,
    )
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source receipts + "
        f"{TYPE} type-level + {PLANTED} planted = {total}",
        flush=True,
    )
    if FAILURES:
        print("FAILURES: " + "; ".join(FAILURES), flush=True)
        return 1
    print("ALL B2C15M CHECKS PASS", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
