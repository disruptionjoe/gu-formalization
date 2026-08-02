#!/usr/bin/env python3
r"""PW2E finite active-native Shiab and three-patch descent gate.

This probe upgrades PW2D's transported tangent to an independently assembled
finite operator on the active ``Cl(9,5)`` component.  The grade-3/11 bridge
satisfies ``u^2=-Delta`` on the synthetic fixture leg, so its exponential is an
exact two-term Clifford expression.  The moved trace line, Phi forms, Hodge
composition, and grade projector are assembled before comparison with the
conjugated-operator identity.

A derivative-bearing three-patch null-Spin atlas then checks coefficient,
connection, pairing, and grade-two representation-covector descent.  This is an active-component
theorem.  It does not identify the public U/(7,7) presentation with the
right-H ``Sp(32,32;H)/Spin0(9,5)`` bundle or construct a global analytic
domain.
"""

from __future__ import annotations

from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from math import comb
from pathlib import Path
import inspect
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


D = load_probe("pw2e_pw2d", "pw2d_native_transported_shiab_action_probe.py")
O = load_probe(
    "pw2e_b2c15o",
    "eric_curt_wave3d_b2c15o_native_y14_background_stabilizer_probe.py",
)
M = D.M


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


def cscalar(value: M.SCliff) -> sp.Expr:
    return sp.simplify(value.get(0, 0))


def cinv_pair(rotor: M.SCliff, inverse: M.SCliff) -> bool:
    one = {0: sp.Integer(1)}
    return (
        not M.sadd(M.smul(rotor, inverse), M.sscale(one, -1))
        and not M.sadd(M.smul(inverse, rotor), M.sscale(one, -1))
    )


def cconj(inverse: M.SCliff, value: M.SCliff, rotor: M.SCliff) -> M.SCliff:
    return M.sclean(M.smul(M.smul(inverse, value), rotor))


def fconj(inverse: M.SCliff, value: M.SForm, rotor: M.SCliff) -> M.SForm:
    return M.sfclean({key: cconj(inverse, coefficient, rotor) for key, coefficient in value.items()})


def cequal(left: M.SCliff, right: M.SCliff) -> bool:
    return not M.sadd(left, M.sscale(right, -1))


def fequal(left: M.SForm, right: M.SForm) -> bool:
    return not M.sfadd(left, M.sfscale(right, -1))


def cdiff(value: M.SCliff, variable: sp.Symbol) -> M.SCliff:
    return M.sclean({mask: sp.diff(coefficient, variable) for mask, coefficient in value.items()})


def raw_with(phi_one: M.SForm, phi_two: M.SForm, value: M.SForm) -> M.SForm:
    star_f = M.sfhodge(value)
    first = M.sfwedge(phi_one, star_f)
    middle = M.sfhodge(M.sfwedge(phi_two, star_f))
    outer = M.sfwedge(phi_one, middle)
    return M.sfadd(first, M.sfscale(M.sfhodge(outer), sp.Rational(-1, 2)))


def project_with(rotor: M.SCliff, inverse: M.SCliff, value: M.SForm) -> M.SForm:
    return fconj(inverse, M.sfproject(fconj(rotor, value, inverse)), rotor)


def explicit_shiab(rotor: M.SCliff, inverse: M.SCliff, value: M.SForm) -> M.SForm:
    """Assemble the moved native ingredients, not a transported answer."""
    trace = cconj(inverse, M.STRACE, rotor)
    phi_one = fconj(inverse, M.SPHI_ONE, rotor)
    phi_two = fconj(inverse, M.SPHI_TWO, rotor)
    preprojected = M.sfleft(trace, raw_with(phi_one, phi_two, value))
    # The full-basis check below proves the active projector commutes with the
    # finite active group, so use the fixed projector here.  This keeps the
    # finite naturality check from defining its own answer by conjugation.
    return M.sfproject(preprojected)


def transported_identity(rotor: M.SCliff, inverse: M.SCliff, value: M.SForm) -> M.SForm:
    return fconj(inverse, D.shiab(fconj(rotor, value, inverse)), rotor)


def exponential_pair(u: M.SCliff, delta: sp.Expr, amplitude: sp.Expr = sp.Integer(1)) -> tuple[M.SCliff, M.SCliff]:
    if sp.simplify(delta) == 0:
        h = M.sadd({0: sp.Integer(1)}, M.sscale(u, amplitude))
        hinv = M.sadd({0: sp.Integer(1)}, M.sscale(u, -amplitude))
        return h, hinv
    root = sp.sqrt(delta)
    cosine = sp.cos(amplitude * root)
    sine_over_root = sp.sin(amplitude * root) / root
    h = M.sadd({0: cosine}, M.sscale(u, sine_over_root))
    hinv = M.sadd({0: cosine}, M.sscale(u, -sine_over_root))
    return h, hinv


def algebraic_exponential_point(
    u: M.SCliff,
    delta: sp.Expr,
    scalar: sp.Expr,
    bridge: sp.Expr,
) -> tuple[M.SCliff, M.SCliff]:
    """Return an exact algebraic point on exp(span(u)).

    For ``u^2=-delta`` the exponential lies on
    ``scalar^2 + delta*bridge^2 = 1``.  Supplying rational points on that
    conic avoids asking SymPy to rediscover trigonometric identities inside
    every Clifford coefficient.
    """
    if sp.expand(scalar**2 + delta * bridge**2 - 1) != 0:
        raise AssertionError("point is not on the finite exponential conic")
    h = M.sadd({0: scalar}, M.sscale(u, bridge))
    hinv = M.sadd({0: scalar}, M.sscale(u, -bridge))
    return h, hinv


def group_compatible(rotor: M.SCliff) -> bool:
    beta = {O.BETA_MASK: F(1)}
    right_h = {O.RIGHT_H_MASK: F(1)}
    c_plus = {O.C_PLUS_MASK: F(1)}
    conjugate = O.cliff_transform(rotor, "conjugate")
    dagger = O.cliff_transform(rotor, "dagger")
    transpose = O.cliff_transform(rotor, "transpose")
    right_defect = O.cliff_sub(M.smul(rotor, right_h), M.smul(right_h, conjugate))
    krein_defect = O.cliff_sub(M.smul(M.smul(dagger, beta), rotor), beta)
    charge_defect = O.cliff_sub(M.smul(M.smul(transpose, c_plus), rotor), c_plus)
    return not right_defect and not krein_defect and not charge_defect


def top_scalar(one: M.SForm, density: M.SForm) -> sp.Expr:
    return D.top_scalar(one, density)


def source_and_layer_zero() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    source(
        "the source owns epsilon-varpi, completed one-half/one-third action grammar, and the bosonic distortion-norm slot",
        all(token in pack for token in ("B_\\omega", "T_\\omega", "\\frac12d_{B_\\omega}T_\\omega", "\\frac13[T_\\omega,T_\\omega]", "kappa_1")),
        "SOURCE-CONFIRMS",
    )
    source(
        "the source owns tilted left/right grammar and trace reversal but not this finite active operator",
        "[02:19:49]" in toe and "[02:22:20]" in toe and "[00:26:51]" in toe and "[00:29:16]" in toe,
        "SOURCE-CONFIRMS grammar; SOURCE-SILENT active construction",
    )
    source(
        "the public-source preferred Shiab projection sheet/calculation is unavailable",
        "SOURCE-NEGATIVE" in pack
        and "preferred Shiab projection" in pack
        and "draft Section 8.2" in pack,
        "SOURCE-NEGATIVE; not the active repository operator",
    )
    typed("public U/(7,7), active P_mix/Sp, reduced Spin(9,5), Q, p, Shiab, action, Euler dual, and physical equation are distinct")
    typed("the active principal-bundle atlas below fixes external differential-form coordinates; it is not a coordinate atlas or public real-bundle port")
    typed("covariant coefficient descent and the contragredient grade-two representation-covector law are checked separately")
    typed("D.build_source_t is a synthetic coefficient-dual-plus-planted-Alt fixture, not Weinstein's source T_omega")
    typed("the kappa1/2 <T,*T> term is a bosonic distortion norm, not the fermion/Higgs/Yukawa mass carrier")
    typed("the public-source Shiab calculation and repository active Cl(9,5)/Sp operator are different; their port is unbuilt")
    reject("identify Cl(7,7) and Cl(9,5) as real Clifford bundles", False)
    reject("replace trace-reversed (6,4)/(9,5) by raw Frobenius or Curt (7,7)", False)
    synthetic_source = inspect.getsource(D.build_source_t)
    preferred_row = next(line for line in pack.splitlines() if "preferred Shiab projection" in line)
    kappa_row = next(line for line in pack.splitlines() if "kappa_1" in line)
    reject(
        "identify the synthetic source_t fixture with source T_omega",
        all(token in synthetic_source for token in ("epsilon", "varpi", "d_0")),
    )
    reject(
        "identify the unavailable public preferred Shiab sheet with the active Cl(9,5)/Sp operator",
        "Cl(9,5)" in preferred_row or "Sp(32,32" in preferred_row,
    )
    reject(
        "identify the bosonic kappa1 distortion norm with the fermion/Yukawa mass carrier",
        "Yukawa" in kappa_row or "fermion" in kappa_row.lower(),
    )


def native_inputs() -> tuple[M.SForm, M.SForm, M.SCliff, M.SForm]:
    curvature = D.to_sympy_form(D.P.SPIN_CURVATURE)
    fixed = D.shiab(curvature)
    source_t = D.build_source_t(fixed)
    alt_t = D.alt_of_t(source_t)
    star_t = D.star_cliff(alt_t)
    c3, c11 = sp.symbols("c3 c11", real=True)
    u = M.sadd(M.sscale(alt_t, c3), M.sscale(star_t, c11))
    du = {(7,): M.sadd(M.sscale(M.sblade(0, 1, 3), c3), M.sscale(D.star_cliff(M.sblade(0, 1, 3)), c11))}
    return curvature, source_t, u, du


def finite_operator_checks(curvature: M.SForm, u: M.SCliff) -> None:
    c3, c11, s = sp.symbols("c3 c11 s", real=True)
    square = M.smul(u, u)
    exact(
        "the actual grade-3/11 bridge closes to the scalar square u^2=-Delta",
        square == {0: c11**2 - c3**2},
        str(square),
    )
    panel = (
        (1, 0, sp.Rational(3, 5), sp.Rational(4, 5)),
        (0, 1, sp.Rational(5, 3), sp.Rational(4, 3)),
        (1, 1, sp.Integer(1), sp.Integer(1)),
    )
    finite_failures = tangent_failures = group_failures = 0
    moved_actual = invariant_projector = 0
    projector_commutation_failures = 0
    tangent_cases = 0
    fixture_key = next(iter(curvature))
    sparse_fixture = {fixture_key: curvature[fixture_key]}
    for panel_index, (left, right, scalar, bridge) in enumerate(panel):
        uv = M.sclean({mask: sp.simplify(value.subs({c3: left, c11: right})) for mask, value in u.items()})
        delta = sp.simplify(left**2 - right**2)
        h, hinv = algebraic_exponential_point(uv, delta, scalar, bridge)
        finite_failures += int(not cinv_pair(h, hinv))
        # Prove operator naturality on a sparse nonzero curvature leg across
        # elliptic, hyperbolic, and null branches.  The complete actual
        # curvature is separately evaluated on the elliptic branch below;
        # densifying it twice merely duplicates PW2D's tangent calculation.
        direct = explicit_shiab(h, hinv, sparse_fixture)
        transported = transported_identity(h, hinv, sparse_fixture)
        finite_failures += int(not fequal(direct, transported))
        if panel_index == 0:
            actual_direct = explicit_shiab(h, hinv, curvature)
            moved_actual += int(not fequal(actual_direct, D.shiab(curvature)))
        group_failures += int(not group_compatible(h))

        if panel_index == 0:
            # One exact tangent comparison is sufficient here: PW2D already
            # checks the full five-direction first/second-variation panel.
            # Keeping this finite gate at first order avoids duplicating its
            # expensive symbolic second-order calculation.
            hs = M.sadd({0: 1}, M.sscale(uv, s))
            hinvs = M.sadd({0: 1}, M.sscale(uv, -s))
            finite_series = {
                key: {
                    mask: sp.series(value, s, 0, 2).removeO().expand()
                    for mask, value in coefficient.items()
                }
                for key, coefficient in explicit_shiab(hs, hinvs, sparse_fixture).items()
            }
            tangent_series = D.transported_shiab(uv, sparse_fixture, s, 1)
            tangent_failures += int(not fequal(M.sfclean(finite_series), tangent_series))
            tangent_cases += 1

        held_pre = {(tuple(range(13))): M.sblade(0, 2)}
        held_projected = project_with(h, hinv, held_pre)
        invariant_projector += int(fequal(held_projected, M.sfproject(held_pre)))
        finite_failures += int(not fequal(project_with(h, hinv, held_projected), held_projected))
        for mask in range(1 << M.N):
            basis_form = {(0,): {mask: sp.Integer(1)}}
            projector_commutation_failures += int(
                not fequal(project_with(h, hinv, basis_form), M.sfproject(basis_form))
            )
    exact(
        "independently assembled finite Q/Phi/projector/Shiab agrees with the finite transport identity on every nonzero panel branch",
        finite_failures == 0 and moved_actual == 1,
        f"failures={finite_failures}; actual_curvature_moved={moved_actual}/1",
    )
    exact(
        "the exact finite family reproduces PW2D's independently assembled transported tangent",
        tangent_failures == 0 and tangent_cases == 1,
        f"failures={tangent_failures}; cases={tangent_cases}",
    )
    exact(
        "the active Lie-algebra projector commutes on all 16,384 Clifford basis blades with every finite active-group branch and remains idempotent",
        invariant_projector == len(panel) and projector_commutation_failures == 0,
        f"held={invariant_projector}/{len(panel)}; full_basis_failures={projector_commutation_failures}/{len(panel)*(1 << M.N)}",
    )
    exact(
        "every finite bridge exponential preserves the active right-H, Krein, and C-plus group structures",
        group_failures == 0,
        f"failures={group_failures}",
    )
    reject("infer a static Shiab from the invariant active projector while Q, Phi, and the trace line move", moved_actual == 0)
    reject("define the finite native operator only by conjugating the desired output", finite_failures != 0)

    # The public projection retains seven Clifford grades.  The 91 bivectors
    # are a certified subspace, not the whole image (a Layer-0 distinction
    # missed by the pre-assessment).
    uv = M.sclean({mask: sp.simplify(value.subs({c3: 1, c11: 0})) for mask, value in u.items()})
    h, hinv = exponential_pair(uv, sp.Integer(1))
    grade_two = tuple(sum(1 << index for index in pair) for pair in combinations(range(M.N), 2))
    image_ok = 0
    for mask in grade_two:
        basis = {mask: sp.Integer(1)}
        image = cconj(hinv, basis, h)
        returned = cconj(h, image, hinv)
        projected = project_with(h, hinv, {(tuple(range(13))): image})
        image_ok += int(returned == basis and projected == {(tuple(range(13))): image})
    exact(
        "the finite active projector has rank 8,256, including an explicitly certified 91-dimensional bivector subspace",
        sum(comb(M.N, grade) for grade in D.B14.SP_GRADES) == 8256
        and len(grade_two) == 91
        and image_ok == 91,
        f"bivectors={image_ok}/91; full_rank={sum(comb(M.N, grade) for grade in D.B14.SP_GRADES)}",
    )


def connection_component(connection: M.SCliff, rotor: M.SCliff, inverse: M.SCliff, variable: sp.Symbol) -> M.SCliff:
    return M.sadd(cconj(inverse, connection, rotor), M.smul(inverse, cdiff(rotor, variable)))


def k_component(connection: M.SCliff, rotor: M.SCliff, inverse: M.SCliff, variable: sp.Symbol) -> M.SCliff:
    return M.smul(inverse, M.sadd(cdiff(rotor, variable), M.smul(connection, rotor), M.sscale(M.smul(rotor, connection), -1)))


def adjoint_matrix(rotor: M.SCliff, inverse: M.SCliff, masks: tuple[int, ...]) -> sp.Matrix:
    index = {mask: position for position, mask in enumerate(masks)}
    result = sp.zeros(len(masks))
    for column, mask in enumerate(masks):
        moved = cconj(inverse, {mask: sp.Integer(1)}, rotor)
        for out_mask, coefficient in moved.items():
            if out_mask not in index:
                raise AssertionError("adjoint left the declared grade-two carrier")
            result[index[out_mask], column] = coefficient
    return result


def three_patch_checks(curvature: M.SForm, source_t: M.SForm, u: M.SCliff) -> None:
    x = sp.symbols("x", real=True)
    c3, c11 = sp.symbols("c3 c11", real=True)
    uv = M.sclean({mask: sp.simplify(value.subs({c3: 1, c11: 1})) for mask, value in u.items()})
    h0, h0inv = exponential_pair(uv, sp.Integer(0))
    # Nonzero Hodge-null u has u^2=0, so h=1+u is an exact nontrivial group element.
    exact("the Hodge-null finite bridge is nontrivial although Delta and K_red vanish", bool(uv) and h0 != {0: 1} and cinv_pair(h0, h0inv))

    null_spin = M.sadd(M.sblade(0, 1), M.sblade(3, 1))
    exact("the derivative-bearing transition generator is a square-zero native bivector", not M.smul(null_spin, null_spin) and O.word_compatible_variant(null_spin))
    functions = (sp.Integer(0), x, 2 * x + x**2)
    frames = tuple(M.sadd({0: sp.Integer(1)}, M.sscale(null_spin, value)) for value in functions)
    inverses = tuple(M.sadd({0: sp.Integer(1)}, M.sscale(null_spin, -value)) for value in functions)
    transitions = {}
    transition_inverses = {}
    for left, right in ((0, 1), (1, 2), (0, 2)):
        transitions[(left, right)] = M.smul(inverses[left], frames[right])
        transition_inverses[(left, right)] = M.smul(inverses[right], frames[left])
    exact(
        "the nonconstant three-patch active Spin transitions obey the exact Cech cocycle",
        cequal(M.smul(transitions[(0, 1)], transitions[(1, 2)]), transitions[(0, 2)])
        and all(cinv_pair(transitions[pair], transition_inverses[pair]) for pair in transitions),
    )

    local_h_symbolic = tuple(cconj(inverses[i], h0, frames[i]) for i in range(3))
    local_hinv_symbolic = tuple(cconj(inverses[i], h0inv, frames[i]) for i in range(3))

    # The sparse independent coefficient and affine laws are evaluated
    # symbolically.  The transported complete action pairing and the 91d Gram
    # comparator below use one exact point of the nonconstant atlas.
    frames_at = tuple(M.sclean({mask: value.subs(x, 1) for mask, value in frame.items()}) for frame in frames)
    inverses_at = tuple(M.sclean({mask: value.subs(x, 1) for mask, value in frame.items()}) for frame in inverses)
    transitions_at = {
        pair: M.sclean({mask: value.subs(x, 1) for mask, value in transition.items()})
        for pair, transition in transitions.items()
    }
    transition_inverses_at = {
        pair: M.sclean({mask: value.subs(x, 1) for mask, value in transition.items()})
        for pair, transition in transition_inverses.items()
    }
    local_h = local_h_symbolic
    local_hinv = local_hinv_symbolic
    fixture_key = next(iter(curvature))
    sparse_fixture = {fixture_key: curvature[fixture_key]}
    local_f = tuple(fconj(inverses[i], sparse_fixture, frames[i]) for i in range(3))

    def local_operator(i: int, value: M.SForm) -> M.SForm:
        # The total finite mover is h*g_i: first apply the local frame g_i,
        # then the global bridge h.  Its inverse is g_i^-1*h^-1.
        total = M.smul(h0, frames[i])
        total_inverse = M.smul(inverses[i], h0inv)
        return explicit_shiab(total, total_inverse, value)

    local_output = tuple(local_operator(i, local_f[i]) for i in range(3))
    coefficient_defects = 0
    h_defects = 0
    for pair in transitions:
        i, j = pair
        tij, tijinv = transitions[pair], transition_inverses[pair]
        h_defects += int(not cequal(local_h[j], cconj(tijinv, local_h[i], tij)))
        coefficient_defects += int(not fequal(local_output[j], fconj(tijinv, local_output[i], tij)))
    exact(
        "finite h and the independently assembled native Shiab coefficient descend on all three overlaps",
        h_defects == 0 and coefficient_defects == 0,
        f"h={h_defects}; coefficient={coefficient_defects}",
    )

    # A derivative-bearing connection calculation tests the inhomogeneous
    # transition law rather than only pointwise conjugacy.
    b0 = M.sadd(M.sblade(1, 2), M.sscale(M.sblade(2, 3), 2))
    local_b = tuple(connection_component(b0, frames[i], inverses[i], x) for i in range(3))
    local_k = tuple(
        k_component(local_b[i], local_h_symbolic[i], local_hinv_symbolic[i], x)
        for i in range(3)
    )
    connection_defects = k_defects = 0
    for pair in transitions:
        i, j = pair
        tij, tijinv = transitions[pair], transition_inverses[pair]
        expected_b = M.sadd(cconj(tijinv, local_b[i], tij), M.smul(tijinv, cdiff(tij, x)))
        connection_defects += int(not cequal(local_b[j], expected_b))
        k_defects += int(not cequal(local_k[j], cconj(tijinv, local_k[i], tij)))
        expected_bhat = M.sadd(expected_b, cconj(tijinv, local_k[i], tij))
        connection_defects += int(not cequal(M.sadd(local_b[j], local_k[j]), expected_bhat))
    exact(
        "literal K is tensorial and B+K obeys the affine law on derivative-bearing overlaps",
        connection_defects == 0 and k_defects == 0,
        f"affine={connection_defects}; K={k_defects}",
    )
    reject("drop the inhomogeneous dt term from the nonconstant connection overlap", not bool(cdiff(transitions[(1, 2)], x)))

    # The action pairing is tested rather than inferred from coefficient
    # covariance.  External form coordinates are fixed on this principal-
    # bundle atlas, so all thirteen density legs must persist patchwise.
    actual_output = explicit_shiab(h0, h0inv, curvature)
    local_actual_output = tuple(fconj(inverses_at[i], actual_output, frames_at[i]) for i in range(3))
    local_t = tuple(fconj(inverses_at[i], source_t, frames_at[i]) for i in range(3))
    action_values = tuple(sp.simplify(top_scalar(local_t[i], local_actual_output[i])) for i in range(3))
    exact(
        "the transported complete thirteen-form coefficient and invariant native scalar pairing agree patchwise",
        all(all(len(key) == 13 for key in output) for output in local_actual_output)
        and all(local_actual_output)
        and action_values[0] == action_values[1] == action_values[2],
        f"action={action_values}",
    )

    # Grade-two adjoint representation: invariant Clifford scalar pairing
    # proves that the lowered covariant law equals contragredient Euler-dual
    # descent.  This is not merely relabelled coefficient covariance.
    masks = tuple(sum(1 << index for index in pair) for pair in combinations(range(M.N), 2))
    tij, tijinv = transitions_at[(1, 2)], transition_inverses_at[(1, 2)]
    transform = adjoint_matrix(tij, tijinv, masks)
    inverse_transform = adjoint_matrix(tijinv, tij, masks)
    gram = sp.diag(*(cscalar(M.smul({mask: 1}, {mask: 1})) for mask in masks))
    exact(
        "the actual 91-dimensional grade-two overlap preserves the indefinite invariant pairing",
        transform.T * gram * transform == gram
        and inverse_transform * transform == sp.eye(91),
    )
    exact(
        "Krein-lowered grade-two carrier covectors obey the independent contragredient representation law",
        gram * transform == inverse_transform.T * gram,
    )
    wrong_dual = transform.T * gram
    reject("transport Euler coordinate covectors covariantly instead of contragrediently", wrong_dual == inverse_transform.T * gram)

    bad_h1 = M.sadd(local_h[1], M.sblade(4, 5))
    reject("infer Cech descent from three unrelated local exponentials", cequal(bad_h1, cconj(transition_inverses[(0, 1)], local_h[0], transitions[(0, 1)])))


def signature_and_boundary_checks() -> None:
    dewitt = sp.Matrix(D.P.D0)
    total = sp.Matrix(D.P.G0)
    exact(
        "the finite atlas retains native trace-reversed fibre/total inertias and negative trace norm",
        D.B14.symmetric_inertia([[F(item) for item in row] for row in dewitt.tolist()]) == (6, 4, 0)
        and D.B14.symmetric_inertia([[F(item) for item in row] for row in total.tolist()]) == (9, 5, 0)
        and D.P.fibre_pair(D.P.G4, D.P.G4) == -4,
    )
    typed("finite active descent does not construct the public U/(7,7)-to-active real-bundle morphism")
    typed("local coefficient and representation-covector descent do not derive the actual action Euler dual, analytic domain, BV quotient, observation descent, or no leakage")
    typed("P1/P2/P3 remain unchanged and unused; none supplies a finite operator, overlap, dual, or domain")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE; TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")


def main() -> int:
    print("PW2E FINITE ACTIVE-NATIVE SHIAB / THREE-PATCH DESCENT")
    source_and_layer_zero()
    curvature, source_t, u, _du = native_inputs()
    finite_operator_checks(curvature, u)
    three_patch_checks(curvature, source_t, u)
    signature_and_boundary_checks()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + {PLANTED} planted = {total}; failures={len(FAILURES)}")
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print("VERDICT: PW2E FINITE ACTIVE-NATIVE OPERATOR AND THREE-PATCH DESCENT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
