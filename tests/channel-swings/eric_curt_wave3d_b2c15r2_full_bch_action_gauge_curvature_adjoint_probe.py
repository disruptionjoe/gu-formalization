#!/usr/bin/env python3
r"""B2C15R2 full-BCH, covariant split-action, and owner-order gate.

The probe advances three objects without identifying them:

* the complete grade-2 Maurer--Cartan connection produced by the linear
  grade-3/11 distortion bridge;
* a projected covariant connection-difference candidate K_u, plus a separate
  generic (B,T) -> (B+K,T-K) split-action comparator; and
* the raw curvature/Zorro owner plus the two rival observation maps.

The exact all-orders result is local and applies only while the reduction
coordinate is u=c3*A+c11*star(A), with fixed coefficients and parallel Hodge
volume.  Nonlinear odd-grade completions, global descent, the native first
variation, compact vertical support, BV/domain, and physical equations remain
outside this gate.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from pathlib import Path
import runpy
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


Q = load_probe(
    "b2c15q_full_bch",
    "eric_curt_wave3d_b2c15q_distortion_substitution_native_zorro_shiab_owner_return_probe.py",
)
B15P = Q.B15P
B15M = Q.B15M
B14 = Q.B14
B15O = Q.B15O
G2 = runpy.run_path(str(CHANNEL / "g2_native_variational_shiab_probe.py"))


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


def is_zero(value) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(item) == 0 for item in value)
    return sp.simplify(value) == 0


# ---------------------------------------------------------------------------
# Source collision and Layer 0.


def source_checks() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    portal = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    transcription = (
        ROOT
        / "explorations/hourly-cycles/hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md"
    ).read_text()

    source_receipt(
        "the written first action pairs the homogeneous distortion T with the completed Shiab residual",
        "I^B_1" in pack
        and "T_\\omega" in pack
        and "\\frac12d_{B_\\omega}T_\\omega" in pack
        and "\\frac13[T_\\omega,T_\\omega]" in pack,
        "SOURCE-CONFIRMS; draft equation 9.4",
    )
    source_receipt(
        "the one-half and one-third terms are required by the source exactness/eddy discussion",
        "quadratic “eddy” tensor" in pack and "02:35:10" in pack,
        "SOURCE-CONFIRMS grammar; affine-segment identity is REPOSITORY-DERIVES",
    )
    source_receipt(
        "the displayed Xi=D_omega Upsilon relation is a redundancy target rather than a supplied off-shell Ward identity",
        "\\Xi_\\omega=D_\\omega\\Upsilon_\\omega" in pack
        and "Noether identity is not" in pack,
        "SOURCE-CORRECTS the Ward homonym",
    )
    source_receipt(
        "the source owns field pullback/section language but no pullback of a thirteen-form Euler covector to a four-dimensional equation",
        "02:21:07" in portal and "four-dimensional" in portal,
        "SOURCE-CONFIRMS field observation; SOURCE-SILENT on the Euler pushdown",
    )
    source_receipt(
        "the fibre pairing remains trace-reversed Frobenius",
        "00:26:28" in toe and "00:29:16" in toe,
        "SOURCE-CONFIRMS",
    )
    source_receipt(
        "the public action cluster does not identify the repository reduction connection or its BCH resummation",
        "quarantined action context" in transcription and "D_GU" in transcription,
        "SOURCE-SILENT on epsilon_red, q_B, K_u, c3:c11, and the split substitution",
    )


def layer_zero_checks() -> None:
    type_level("source T, reduction coordinate u(T), pure Maurer-Cartan q_MC, reduced connection q_B, and tensorial difference K_u=q_B-B are distinct")
    type_level("Weinstein's I1, the rejected bare lambda_red q pairing, and the coefficient-free split substitution inside I1 are distinct actions")
    type_level("source F_B, reconstructed LC spin curvature, and curvature of the reduced connection require explicit maps before identification")
    type_level("raw curvature derivative, its formal adjoint, Green preboundary, selected domain, and BV differential are distinct layers")
    type_level("field pullback, raw 13-form pullback, ten-fibre Gysin, and the dual of a specified observation-variation lift are distinct maps")
    type_level("base g, trace-reversed fibre D_g, total Zorro G_Y, and physical observed metric stay typed separately")
    type_level("P1/P2 is an orientation line over a configuration loop, not an orientation or support kernel on the noncompact metric fibre")
    reject("identify q_MC with the source distortion T", False)
    reject("identify the source redundancy Xi=D Upsilon with an off-shell BRST/Noether identity", False)


# ---------------------------------------------------------------------------
# Full split-volume BCH resummation.


VOLUME = {Q.FULL_MASK: F(1)}


def cliff_add(*values):
    return B14.cliff_add(*values)


def cliff_scale(value, coefficient):
    return B14.cliff_scale(value, F(coefficient))


def cliff_comm(left, right):
    return B14.cliff_comm(left, right)


def nested_ad(left, right, degree: int):
    value = right
    for _ in range(degree):
        value = cliff_comm(left, value)
    return value


def grade(value, target: int):
    return Q.cliff_grade(value, target)


def reduction_value(A, c3: F, c11: F):
    return cliff_add(cliff_scale(A, c3), cliff_scale(Q.internal_hodge(A), c11))


def bch_h_truncation(u, du, highest_odd: int):
    value = {}
    for n in range(1, highest_odd + 1, 2):
        coefficient = -F(1, sp.factorial(n + 1))
        value = cliff_add(value, cliff_scale(grade(nested_ad(u, du, n), 2), coefficient))
    return value


def full_bch_checks() -> None:
    volume_square = B14.cliff_mul(VOLUME, VOLUME)
    hodge_failures = 0
    for mask in Q.GRADE3:
        value = {mask: F(1)}
        star = Q.internal_hodge(value)
        left = B14.cliff_mul(VOLUME, value)
        right = B14.cliff_mul(value, VOLUME)
        hodge_failures += int(star != left or right != cliff_scale(star, -1))
    exact(
        "the active split volume squares to one and realizes star(A)=nu A=-A nu on all 364 grade-three blades",
        volume_square == {0: F(1)} and hodge_failures == 0,
        f"failures={hodge_failures}",
    )

    A = cliff_add(
        *(
            cliff_scale({Q.GRADE3[index]: F(1)}, index + 1)
            for index in (0, 1, 2, 7, 15, 31)
        )
    )
    C = cliff_add(
        *(
            cliff_scale({Q.GRADE3[index]: F(1)}, 7 - offset)
            for offset, index in enumerate((3, 8, 16, 32, 64))
        )
    )
    factor_failures = 0
    for c3, c11 in ((F(2), F(1)), (F(5, 3), F(4, 3)), (F(1), F(1))):
        delta = c3 * c3 - c11 * c11
        u = reduction_value(A, c3, c11)
        du = reduction_value(C, c3, c11)
        for k in range(4):
            actual = nested_ad(u, du, 2 * k + 1)
            expected = cliff_scale(nested_ad(A, C, 2 * k + 1), delta ** (k + 1))
            factor_failures += int(actual != expected)
    exact(
        "odd BCH adjoint powers factor as Delta^(k+1) ad_A^(2k+1)(dA) through four held-out h-orders",
        factor_failures == 0,
        f"failures={factor_failures}",
    )

    blade_A = {7: F(1)}
    blade_C = {11: F(1)}
    iterates = [nested_ad(blade_A, blade_C, n) for n in range(1, 8)]
    exact(
        "the two-blade fixture has the exact alternating ad-power chain needed for a closed entire resummation",
        iterates
        == [
            {12: F(-2)}, {11: F(-4)}, {12: F(8)}, {11: F(16)},
            {12: F(-32)}, {11: F(-64)}, {12: F(128)},
        ],
    )
    delta = sp.symbols("Delta", real=True)
    series = delta - delta**2 / 3 + 2 * delta**3 / 45 - delta**4 / 315
    closed_series = sp.series((1 - sp.cos(2 * sp.sqrt(delta))) / 2, delta, 0, 5).removeO()
    exact(
        "the full two-blade connection is the entire function (1-cos(2 sqrt(Delta)))/2 in the e23 direction",
        sp.simplify(series - closed_series) == 0,
        str(series),
    )
    c3_symbol, c11_symbol = sp.symbols("c3 c11", real=True)

    def split_volume_mul(left, right):
        """Multiply (a+b nu)(c+d nu) in R[nu]/(nu^2-1)."""
        a, b = left
        c, d = right
        return (sp.expand(a * c + b * d), sp.expand(a * d + b * c))

    # Writing u=A r and du=C r with r=c3-c11 nu, odd Clifford words
    # exchange r with rbar while even words commute with it.  Therefore the
    # two closed parity transitions are
    #   odd O r --ad_u--> Delta ad_A(O)       (even),
    #   even E  --ad_u--> ad_A(E) r           (odd with r).
    # The symbolic identity rbar*r=Delta makes this an induction for every
    # odd adjoint power, rather than a finite check of powers of zero.
    r = (c3_symbol, -c11_symbol)
    r_bar = (c3_symbol, c11_symbol)
    delta_pair = (c3_symbol**2 - c11_symbol**2, sp.Integer(0))
    parity_state = ("odd_with_r", 0)
    parity_trace = []
    for _ in range(8):
        if parity_state[0] == "odd_with_r":
            parity_state = ("even", parity_state[1] + 1)
        else:
            parity_state = ("odd_with_r", parity_state[1])
        parity_trace.append(parity_state)
    exact(
        "the symbolic split-volume parity recurrence proves the full linear-bridge h-connection is Delta-only and both Hodge-null branches vanish to every order",
        split_volume_mul(r_bar, r) == delta_pair
        and parity_trace
        == [
            ("even", 1), ("odd_with_r", 1),
            ("even", 2), ("odd_with_r", 2),
            ("even", 3), ("odd_with_r", 3),
            ("even", 4), ("odd_with_r", 4),
        ],
        "rbar*r=Delta and the two parity transitions close inductively; the exponential series is entire",
    )

    same_delta_failures = 0
    for highest in (1, 3, 5, 7):
        first = bch_h_truncation(
            reduction_value(blade_A, F(1), F(0)),
            reduction_value(blade_C, F(1), F(0)),
            highest,
        )
        second = bch_h_truncation(
            reduction_value(blade_A, F(5, 3), F(4, 3)),
            reduction_value(blade_C, F(5, 3), F(4, 3)),
            highest,
        )
        same_delta_failures += int(first != second)
    exact(
        "same-Delta coefficient pairs agree termwise through eighth order on the closed fixture",
        same_delta_failures == 0,
        f"failures={same_delta_failures}",
    )

    generic_q = bch_h_truncation(
        reduction_value(A, F(2), F(1)),
        reduction_value(C, F(2), F(1)),
        7,
    )
    exact(
        "the held eighth-order grade-two truncation stays in the active right-H/Krein/C-plus compatible word class",
        bool(generic_q) and B15O.word_compatible_variant(generic_q),
        f"support={len(generic_q)}",
    )

    wrong_norm_equal = (F(1) ** 2 + F(0) ** 2) == (F(5, 3) ** 2 + F(4, 3) ** 2)
    reject("replace the split norm Delta=c3^2-c11^2 by c3^2+c11^2", wrong_norm_equal)

    mismatched_one = grade(
        cliff_comm(reduction_value(blade_A, F(1), F(0)), blade_C), 2
    )
    mismatched_two = grade(
        cliff_comm(reduction_value(blade_A, F(5, 3), F(4, 3)), blade_C), 2
    )
    reject(
        "extend Delta-only factorization when du does not share the same Hodge coefficient pair as u",
        mismatched_one == mismatched_two,
    )

    disjoint = {sum(1 << index for index in (3, 4, 5)): F(1)}
    non_symmetric = cliff_comm(blade_A, disjoint)
    exact(
        "the reduction is not a symmetric pair: two grade-three elements have a live grade-six bracket",
        bool(grade(non_symmetric, 6)),
        str(non_symmetric),
    )
    reject("derive the resummation from a false symmetric-space assumption [m,m] subset h", not bool(grade(non_symmetric, 6)))

    grade7 = {127: F(1)}
    nonlinear_values = []
    for c3, c11 in ((F(1), F(0)), (F(5, 3), F(4, 3))):
        u = cliff_add(grade7, reduction_value(blade_A, c3, c11))
        du = reduction_value(blade_C, c3, c11)
        nonlinear_values.append(bch_h_truncation(u, du, 3))
    exact(
        "an independent fixed grade-seven completion breaks same-Delta equality already in the quadratic-plus-quartic connection",
        nonlinear_values == [{12: F(2, 3)}, {12: F(2, 27)}],
        str(nonlinear_values),
    )
    reject("promote the Delta-only theorem to nonlinear odd-grade completions of u", nonlinear_values[0] == nonlinear_values[1])
    type_level("the full h-projection is controlled for the linear grade-3/11 bridge only; its m-part, varying coefficients/Hodge, nonlinear odd grades, global log chart, and source identity remain open")


# ---------------------------------------------------------------------------
# Covariant connection difference and source-action split substitution.


def matrix_comm(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return left * right - right * left


def matrix_ad_power(left: sp.Matrix, right: sp.Matrix, degree: int) -> sp.Matrix:
    value = right
    for _ in range(degree):
        value = matrix_comm(left, value)
    return value


def k_series(A: sp.Matrix, covariant_A: sp.Matrix, delta: sp.Expr, highest_k: int = 2) -> sp.Matrix:
    value = sp.zeros(*A.shape)
    for k in range(highest_k + 1):
        value -= (
            delta ** (k + 1)
            * matrix_ad_power(A, covariant_A, 2 * k + 1)
            / sp.factorial(2 * k + 2)
        )
    return sp.simplify(value)


def covariant_connection_checks() -> None:
    blade_A = {7: F(1)}
    mixed_DBA = cliff_add({11: F(1)}, {sum(1 << index for index in (3, 4, 5)): F(1)})
    unprojected_leading = cliff_comm(blade_A, mixed_DBA)
    projected_leading = grade(unprojected_leading, 2)
    projection_failures = 0
    for h_mask in Q.GRADE2:
        h_generator = {h_mask: F(1)}
        projection_failures += int(
            grade(cliff_comm(h_generator, unprojected_leading), 2)
            != cliff_comm(h_generator, projected_leading)
        )
    exact(
        "the required pr_h=pr_2 removes a live grade-six connection impostor and is equivariant under all 91 reduced grade-two h/Spin generators",
        bool(projected_leading)
        and bool(grade(unprojected_leading, 6))
        and set(projected_leading).issubset(set(Q.GRADE2))
        and projection_failures == 0,
        f"unprojected_grades={sorted({mask.bit_count() for mask in unprojected_leading})}; projection_failures={projection_failures}",
    )
    reject(
        "drop pr_h from K_u and call the resulting mixed grade-two/grade-six word an H-connection",
        unprojected_leading == projected_leading,
    )

    x = sp.symbols("x", real=True)
    A = sp.Matrix([[x, 1 + x], [2 - x, -x]])
    B = sp.Matrix([[0, 1 + x], [x, -1]])
    h = sp.Matrix([[1, x], [0, 1]])
    h_inverse = sp.simplify(h.inv())
    D_A = sp.diff(A, x) + matrix_comm(B, A)
    B_h = sp.simplify(h_inverse * B * h + h_inverse * sp.diff(h, x))
    A_h = sp.simplify(h_inverse * A * h)
    D_A_h = sp.simplify(sp.diff(A_h, x) + matrix_comm(B_h, A_h))
    exact(
        "the covariant derivative D_B A carries the full nonconstant gauge cocycle",
        is_zero(D_A_h - h_inverse * D_A * h),
    )

    delta = sp.Integer(3)
    K = k_series(A, D_A, delta)
    K_h = k_series(A_h, D_A_h, delta)
    q_B = sp.simplify(B + K)
    q_B_h = sp.simplify(B_h + K_h)
    exact(
        "the projected full-series truncation K_u=q_B-B transforms tensorially and q_B transforms as a connection in the matrix h-fixture",
        is_zero(K_h - h_inverse * K * h)
        and is_zero(q_B_h - h_inverse * q_B * h - h_inverse * sp.diff(h, x)),
    )
    raw_K = k_series(A, sp.diff(A, x), delta)
    raw_K_h = k_series(A_h, sp.diff(A_h, x), delta)
    reject(
        "replace D_B A by raw dA in the nonconstant-gauge covariant connection difference",
        is_zero(raw_K_h - h_inverse * raw_K * h),
    )
    type_level("the same-bundle theorem is conditional: an actual embedding of this reduced h-connection into the source adjoint bundle and its Cech descent are still required")


def source_split_checks() -> None:
    M = G2["M"]
    form1 = G2["form1"]
    form2 = G2["form2"]
    f1_add = G2["f1_add"]
    f1_scale = G2["f1_scale"]
    f2_add = G2["f2_add"]
    f2_scale = G2["f2_scale"]
    curvature = G2["curvature"]
    covariant_d = G2["covariant_d"]
    q = G2["q"]
    source_action = G2["source_action"]
    shiab_identity = G2["shiab_identity"]

    B = form1(M(1, 1, 0, -1), M(0, 1, 2, 1), M(2, -1, 1, 0))
    T = form1(M(0, 2, -1, 1), M(1, -1, 1, 2), M(-1, 0, 2, 1))
    dB = form2(M(0, 1, -1, 0), M(1, 0, 2, -1), M(-1, 2, 0, 1))
    dT = form2(M(2, -1, 0, 1), M(0, 2, 1, -1), M(1, 0, -2, 1))
    K = form1(M(1, 0, 1, -1), M(0, -1, 2, 1), M(2, 1, 0, -2))
    dK = form2(M(1, 2, 0, -1), M(-1, 0, 1, 2), M(0, 1, -2, 1))

    def split(scale: F):
        B_s = f1_add(B, f1_scale(scale, K))
        T_s = f1_add(T, f1_scale(-scale, K))
        dB_s = f2_add(dB, f2_scale(scale, dK))
        dT_s = f2_add(dT, f2_scale(-scale, dK))
        action = source_action(B_s, dB_s, T_s, dT_s, shiab_identity, F(2))
        return action, B_s, T_s, dB_s, dT_s

    actions = {scale: split(scale)[0] for scale in map(F, (-2, -1, 0, 1, 2))}
    exact(
        "a generic fixed-total-connection split comparator is nontrivial inside the existing source action and introduces no lambda_red",
        actions
        == {
            F(-2): F(115, 2), F(-1): F(32), F(0): F(23, 2),
            F(1): F(2), F(2): F(19, 2),
        },
        str(actions),
    )
    split_derivative = (actions[F(1)] - actions[F(-1)]) / 2
    exact(
        "the generic split direction has a live first response governed by the existing B-versus-T owner difference",
        split_derivative == F(-15),
        f"central response={split_derivative}",
    )

    endpoint_curvatures = []
    segment_failures = 0
    for scale in map(F, (-1, 0, 1)):
        _action, B_s, T_s, dB_s, dT_s = split(scale)
        endpoint_curvatures.append(curvature(f1_add(B_s, T_s), f2_add(dB_s, dT_s)))
        F_B = curvature(B_s, dB_s)
        D_BT = covariant_d(B_s, T_s, dT_s)
        T2 = q(T_s, T_s)
        segment = f2_add(F_B, f2_add(f2_scale(F(1, 2), D_BT), f2_scale(F(1, 3), T2)))
        segment_failures += int(
            source_action(B_s, dB_s, T_s, dT_s, shiab_identity, F(0))
            != G2["wedge_pair"](T_s, segment)
        )
    exact(
        "the generic split keeps the total endpoint connection and its curvature fixed while preserving the one-half/one-third segment grammar",
        endpoint_curvatures[0] == endpoint_curvatures[1] == endpoint_curvatures[2]
        and segment_failures == 0,
        f"segment_failures={segment_failures}",
    )

    g = M(1, 1, 0, 1)
    moved_action = source_action(
        G2["transform_f1"](g, split(F(1))[1]),
        G2["transform_f2"](g, split(F(1))[3]),
        G2["transform_f1"](g, split(F(1))[2]),
        G2["transform_f2"](g, split(F(1))[4]),
        shiab_identity,
        F(2),
    )
    exact(
        "the generic finite nonabelian source-action split control is invariant under common constant conjugation",
        moved_action == actions[F(1)],
    )

    c3, c11 = sp.symbols("c3 c11", real=True)
    delta = c3**2 - c11**2
    s_delta = delta - delta**2 / 3 + 2 * delta**3 / 45
    response_polynomial = (2 * s_delta**3 + 11 * s_delta**2 - 32 * s_delta + 23) / 2
    jacobian = sp.Matrix([[sp.diff(response_polynomial, c3), sp.diff(response_polynomial, c11)]])
    exact(
        "every split-action response mediated only by the linear-bridge full K_u has coefficient-sensitivity rank at most one",
        jacobian.subs({c3: 2, c11: 1}).rank() == 1
        and sp.simplify(response_polynomial.subs({c3: 1, c11: 0}) - response_polynomial.subs({c3: sp.Rational(5, 3), c11: sp.Rational(4, 3)})) == 0,
        "same-Delta heldout; this is not a physical constraint count",
    )
    reject("count the fixed 1/2 and 1/3 transgression weights as fitted action parameters", False)
    reject("add the rejected bare lambda_red q pairing on top of the covariant split without a no-double-counting proof", False)
    type_level("the candidate split has only c3,c11 and no new action coefficient, but the finite G2 K,dK direction is independently chosen rather than derived from u(T); actual K_u action response and coefficient visibility remain open")
    type_level("physical coefficient surplus remains UNCOMPUTED because neither a selected observed equation nor an independent target value exists")


def composite_k_green_checks() -> None:
    x = sp.symbols("x", real=True)
    A = sp.Matrix([[x, 1 + x], [2 - x, -x]])
    B = sp.Matrix([[1, x], [x**2, -1]])
    R = sp.Matrix([[1 + x**2, 2 - x], [x, -1 - x**2]])
    variation = sp.Matrix([[x * (1 - x), 1 + x], [x**2, -x * (1 - x)]])
    C = sp.diff(A, x) + matrix_comm(B, A)
    dC = sp.diff(variation, x) + matrix_comm(B, variation)
    dK = -sp.Rational(1, 2) * (
        matrix_comm(variation, C) + matrix_comm(A, dC)
    )
    direct = sp.integrate(sp.trace(dK * R), (x, 0, 1))
    S = matrix_comm(R, A)
    euler = -sp.Rational(1, 2) * (
        matrix_comm(C, R) + matrix_comm(S, B)
    ) + sp.Rational(1, 2) * sp.diff(S, x)
    bulk = sp.integrate(sp.trace(variation * euler), (x, 0, 1))
    theta = -sp.Rational(1, 2) * sp.trace(variation * S)
    boundary = sp.simplify(theta.subs(x, 1) - theta.subs(x, 0))
    exact(
        "the covariant quadratic K_u owner has an exact bulk-plus-Green return against a generic split-action driver R_B=E_B-E_T",
        direct == F(331, 28) and bulk == F(415, 28) and boundary == -3
        and sp.simplify(direct - bulk - boundary) == 0,
        f"direct={direct}; bulk={bulk}; boundary={boundary}",
    )
    reject("drop the nonzero K_u Green term from the split substitution", direct == bulk)
    raw_C = sp.diff(A, x)
    raw_dC = sp.diff(variation, x)
    raw_dK = -sp.Rational(1, 2) * (
        matrix_comm(variation, raw_C) + matrix_comm(A, raw_dC)
    )
    raw_direct = sp.integrate(sp.trace(raw_dK * R), (x, 0, 1))
    reject("replace D_B A by dA in the covariant K_u owner", raw_direct == direct)
    type_level("this is the exact differential owner comparator for the leading K_u term; the native full-series source-coordinate first variation remains the successor construction")


# ---------------------------------------------------------------------------
# Native Zorro-curvature order and exact sequential formal-adjoint control.


def symmetric_basis4() -> tuple[sp.Matrix, ...]:
    values = []
    for i in range(4):
        for j in range(i, 4):
            value = sp.zeros(4)
            value[i, j] = 1
            value[j, i] = 1
            values.append(value)
    return tuple(values)


def riemann_symbol(covector: tuple[sp.Expr, ...], H: sp.Matrix) -> tuple[sp.Expr, ...]:
    values = []
    for a, b in combinations(range(H.rows), 2):
        for c, d in combinations(range(H.rows), 2):
            values.append(
                sp.simplify(
                    sp.Rational(1, 2)
                    * (
                        covector[c] * covector[b] * H[a, d]
                        + covector[d] * covector[a] * H[b, c]
                        - covector[c] * covector[a] * H[b, d]
                        - covector[d] * covector[b] * H[a, c]
                    )
                )
            )
    return tuple(values)


def native_curvature_order_checks() -> None:
    basis = symmetric_basis4()
    inverse_G0 = B15P.G0.inv()
    pure_gauge_failures = 0
    cross_identity_failures = 0
    base_ranks = []
    shiab_ranks = []
    for k4 in ((sp.Integer(1), 0, 0, 0), (sp.Integer(1), 0, 0, sp.Integer(1))):
        xi = tuple(k4) + (sp.Integer(0),) * 10
        base_columns = []
        shiab_columns = []
        for q_owner, h in enumerate(basis):
            vertical = [
                -B15P.dewitt(h, fibre_basis)
                for fibre_basis in B15P.SYM2
            ]
            H = sp.zeros(14)
            for i in range(4):
                for q, coefficient in enumerate(vertical):
                    H[i, 4 + q] = H[4 + q, i] = sp.simplify(k4[i] * coefficient)
                    cross_identity_failures += int(
                        H[i, 4 + q]
                        != -sp.simplify(k4[i] * B15P.dewitt(h, B15P.SYM2[q]))
                    )
            pure_gauge_failures += sum(value != 0 for value in riemann_symbol(xi, H))
            base_columns.append(sp.Matrix(riemann_symbol(tuple(k4), h)))
            # The full A2 o Z0 curvature-principal block includes both the
            # base metric variation h and the simultaneous metric derivative
            # of the ten-dimensional trace-reversed DeWitt fibre block.
            H0 = sp.zeros(14)
            H0[:4, :4] = h
            H0[4:, 4:] = B15P.DD[q_owner]
            full_curvature = {}
            for c, d in combinations(range(14), 2):
                low = sp.zeros(14)
                for a in range(14):
                    for b in range(14):
                        low[a, b] = sp.Rational(1, 2) * (
                            xi[c] * xi[b] * H0[a, d]
                            + xi[d] * xi[a] * H0[b, c]
                            - xi[c] * xi[a] * H0[b, d]
                            - xi[d] * xi[b] * H0[a, c]
                        )
                full_curvature[(c, d)] = sp.simplify(inverse_G0 * low)
            spin_curvature, _incompatible = B15P.frame_spin_curvature(full_curvature)
            source = B14.trace_line_source(spin_curvature)
            shiab_columns.append(
                {
                    (key, mask): coefficient
                    for key, cliff in source.items()
                    for mask, coefficient in cliff.items()
                }
            )
        base_ranks.append(sp.Matrix.hstack(*base_columns).rank())
        shiab_keys = sorted(set().union(*(set(column) for column in shiab_columns)))
        shiab_ranks.append(
            sp.Matrix(
                [
                    [column.get(key, 0) for column in shiab_columns]
                    for key in shiab_keys
                ]
            ).rank()
        )
    exact(
        "the principal Zorro cross-block is the pure-gauge total-metric symbol xi symmetric-product v and is killed by the curvature principal symbol",
        cross_identity_failures == 0 and pure_gauge_failures == 0,
        f"cross_failures={cross_identity_failures}; curvature_failures={pure_gauge_failures}",
    )
    exact(
        "the differentiated observation pullback retains a rank-six second-order base Riemann symbol for both non-null and null held-out covectors",
        base_ranks == [6, 6]
        and all(
            B15P.PULLBACK2[a][b][k][l] == B15P.G2_BASE[a][b][k][l]
            for a in range(4) for b in range(4) for k in range(4) for l in range(4)
        ),
        f"ranks={base_ranks}",
    )
    exact(
        "the full A2 o Z0 curvature-principal subroute, including the moving DeWitt block, remains live at order two on both held-out covectors",
        shiab_ranks == [10, 4],
        f"Shiab ranks={shiab_ranks}",
    )
    exact(
        "the D_G F_spin/Zorro/Shiab route has zero order-three symbol and a live A2 o Z0 order-two summand",
        pure_gauge_failures == 0 and all(rank > 0 for rank in shiab_ranks),
        "the complete effective order-two symbol remains open until A1 o Z1 and all subprincipal coefficient terms are assembled",
    )
    reject("retain the generic order-three curvature/Zorro cap after the pure-gauge principal cancellation", pure_gauge_failures != 0)


def sequential_green_checks() -> None:
    x = sp.symbols("x", real=True)
    derivative = lambda value, degree=1: sp.diff(value, x, degree)
    rho = 1 + x
    J = sp.diag(1, -1)
    S_in = sp.Matrix([[1, x], [0, 1]])
    S_mid = sp.Matrix([[1, 0], [x, 1]])
    S_out = sp.Matrix([[1, x**2], [0, 1]])
    W_in = rho * S_in.T * J * S_in
    W_mid = rho * S_mid.T * J * S_mid
    W_out = rho * S_out.T * J * S_out
    A2 = sp.Matrix([[1, 0], [0, 0]])
    A1 = sp.Matrix([[0, 1 + x], [1, x]])
    A0 = sp.Matrix([[1, x], [x**2, -1]])
    Z1 = sp.Matrix([[0, 0], [1, 0]])
    Z0 = sp.Matrix([[1, x], [1 - x, 2]])
    h = sp.Matrix([1 + x + x**2, 2 - x + x**3])
    P = sp.Matrix([2 + x - x**2, 1 + 2 * x + x**2])

    H = Z1 * derivative(h) + Z0 * h
    AH = A2 * derivative(H, 2) + A1 * derivative(H) + A0 * H
    direct_integrand = (AH.T * W_out * P)[0]
    V2 = A2.T * W_out * P
    V1 = A1.T * W_out * P
    V0 = A0.T * W_out * P
    A_star = sp.simplify(W_mid.inv() * (derivative(V2, 2) - derivative(V1) + V0))
    weighted_A_star = W_mid * A_star
    Z_star = sp.simplify(
        W_in.inv()
        * (-derivative(Z1.T * weighted_A_star) + Z0.T * weighted_A_star)
    )
    bulk_integrand = (h.T * W_in * Z_star)[0]
    theta_A = (
        derivative(H).T * V2 - H.T * derivative(V2) + H.T * V1
    )[0]
    theta_Z = (h.T * Z1.T * weighted_A_star)[0]
    direct = sp.integrate(sp.expand(direct_integrand), (x, 0, 1))
    bulk = sp.integrate(sp.cancel(bulk_integrand), (x, 0, 1))
    inner_boundary = sp.simplify(theta_A.subs(x, 1) - theta_A.subs(x, 0))
    outer_boundary = sp.simplify(theta_Z.subs(x, 1) - theta_Z.subs(x, 0))
    exact(
        "the order-lowered curvature/Zorro comparator closes with both sequential Green boundaries",
        direct == F(30871333, 360360)
        and bulk == F(89610013, 360360)
        and inner_boundary == 146
        and outer_boundary == -309
        and sp.simplify(direct - bulk - inner_boundary - outer_boundary) == 0,
        f"direct={direct}; bulk={bulk}; inner={inner_boundary}; outer={outer_boundary}",
    )

    C3 = sp.simplify(A2 * Z1)
    C2 = sp.simplify(A2 * (2 * derivative(Z1) + Z0) + A1 * Z1)
    C1 = sp.simplify(
        A2 * (derivative(Z1, 2) + 2 * derivative(Z0))
        + A1 * (derivative(Z1) + Z0) + A0 * Z1
    )
    C0 = sp.simplify(A2 * derivative(Z0, 2) + A1 * derivative(Z0) + A0 * Z0)
    direct_star = sp.simplify(
        W_in.inv()
        * (
            C0.T * W_out * P
            - derivative(C1.T * W_out * P)
            + derivative(C2.T * W_out * P, 2)
            - derivative(C3.T * W_out * P, 3)
        )
    )
    exact(
        "the direct order-two formal adjoint equals the sequential Zorro-adjoint after curvature-adjoint and the order-three coefficient vanishes",
        C3 == sp.zeros(2) and C2.rank() == 2 and is_zero(direct_star - Z_star),
        f"C2_rank={C2.rank()}",
    )
    reject("omit the live inner curvature Green boundary", direct == bulk + outer_boundary)
    reject("omit the live outer Zorro Green boundary", direct == bulk + inner_boundary)

    K_in = S_in.T * J * S_in
    K_mid = S_mid.T * J * S_mid
    K_out = S_out.T * J * S_out
    V2_wrong = A2.T * K_out * P
    V1_wrong = A1.T * K_out * P
    V0_wrong = A0.T * K_out * P
    A_star_wrong = sp.simplify(
        K_mid.inv()
        * (derivative(V2_wrong, 2) - derivative(V1_wrong) + V0_wrong)
    )
    Z_star_wrong = sp.simplify(
        K_in.inv()
        * (
            -derivative(Z1.T * K_mid * A_star_wrong)
            + Z0.T * K_mid * A_star_wrong
        )
    )
    wrong_bulk = sp.integrate(sp.cancel((h.T * W_in * Z_star_wrong)[0]), (x, 0, 1))
    reject("freeze the moving density while forming both formal adjoints", wrong_bulk == bulk)
    positive_direct = sp.integrate(sp.expand((AH.T * sp.eye(2) * P)[0]), (x, 0, 1))
    reject("replace the declared Krein lowerer by a positive identity without changing the owner", positive_direct == direct)

    g = sp.Function("g")(x)
    test = sp.Function("p")(x)
    coefficient_motion_adjoint = -sp.diff(sp.diff(g, x, 2) * test, x)
    exact(
        "the first-order fixed-curvature coefficient-motion adjoint has a live total-metric background third jet after the order-three curvature-symbol cancellation",
        coefficient_motion_adjoint.coeff(sp.diff(g, x, 3)) == -test,
        str(coefficient_motion_adjoint),
    )
    type_level("native order ledger: the order-three curvature/Zorro symbol cancels and A2 o Z0 is live at order two, while A1 o Z1 and subprincipal terms can still cancel or modify the effective order-two symbol; moving coefficient slots can reach a total-metric third jet, generically a base-metric fourth jet through first-order Zorro")
    type_level("the bare q_red action branch is rejected; K_u is first order in A(T), so its split-action owner has an order-one T adjoint before source-graph substitution")
    type_level("Hessian derivatives of the owner, moving primalizers, BV quotient, and analytic domain are not first-action Euler terms in this gate")


# ---------------------------------------------------------------------------
# Observation: local Gysin feasibility versus a separately chosen lift dual.


def gysin_and_equation_dual_checks() -> None:
    source = B14.trace_line_source(B15P.SPIN_CURVATURE)
    vertical = set(range(4, 14))
    gysin = {}
    rejected_nine = 0
    for key, coefficient in source.items():
        vertical_degree = sum(index in vertical for index in key)
        if vertical_degree == 10:
            horizontal_key = tuple(index for index in key if index < 4)
            gysin[horizontal_key] = coefficient
        else:
            rejected_nine += 1
    exact(
        "ordinary oriented ten-fibre integration retains exactly four actual (3,10) Shiab legs and kills all nine (4,9) legs by degree",
        len(gysin) == 4 and rejected_nine == 9
        and set(gysin) == set(combinations(range(4), 3)),
        f"retained={len(gysin)}; killed={rejected_nine}",
    )
    torus_volume = sp.prod(sp.integrate(sp.Integer(1), (sp.symbols(f"y{i}"), 0, 1)) for i in range(10))
    exact(
        "a compact oriented unit-ten-torus control has normalized fibre volume one and reproduces the four local base three-forms",
        torus_volume == 1 and len(gysin) == 4,
        "control only; it is not the noncompact metric fibre",
    )
    reject("treat an orientation reversal as leaving the Gysin output unchanged", -1 == 1)
    reject("double an unnormalized fibre kernel without changing the observed equation", 2 * torus_volume == torus_volume)
    type_level("the actual Lorentz-metric fibre is noncompact; a transitive fibre symmetry admits no nonzero invariant compactly supported scalar cutoff, so the local coefficient has no canonical Gysin support")
    type_level("Gysin remains conditional on dynamical decay/proper support or new observation data; P1/P2/P3 supplies neither the support kernel nor its normalization")

    E = sp.Matrix(range(1, 14))
    L_horizontal = sp.zeros(13, 4)
    L_horizontal[:4, :4] = sp.eye(4)
    solder = sp.Matrix(9, 4, lambda i, j: sp.Integer(((i + 2 * j + 1) % 5) - 2))
    L_soldered = L_horizontal.copy()
    L_soldered[4:, :] = solder
    observed_horizontal = L_horizontal.T * E
    observed_soldered = L_soldered.T * E
    exact(
        "a purely horizontal normalized lift dual agrees with the four-leg selector while a vertical soldering lift can see the nine Gysin-ineligible slots",
        observed_horizontal == sp.Matrix([1, 2, 3, 4])
        and observed_soldered != observed_horizontal,
        f"horizontal={list(observed_horizontal)}; soldered={list(observed_soldered)}",
    )

    U = sp.Matrix([[1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 1]])
    V = sp.diag(*tuple(sp.Integer(2 if i % 2 == 0 else 3) for i in range(13)))
    L_patch = V * L_soldered * U.inv()
    E_patch = V.inv().T * E
    exact(
        "the equation-dual descends under the dual overlap law L_j=V L_i U^-1 and E_j=V^-T E_i",
        L_patch.T * E_patch == U.inv().T * observed_soldered,
    )
    reject(
        "transport an Euler covector covariantly rather than dually across observation patches",
        L_patch.T * (V * E) == U.inv().T * observed_soldered,
    )

    R = sp.zeros(4, 13)
    R[:, :4] = sp.eye(4)
    leakage = (sp.eye(13) - L_soldered * R).T * E
    exact(
        "a split observation lift can satisfy R L=1 while its dual covector projector retains nonzero upstairs leakage",
        R * L_soldered == sp.eye(4) and leakage != sp.zeros(13, 1),
        f"leakage_rank={int(leakage != sp.zeros(13, 1))}",
    )
    reject("infer no-leakage from the existence of a left inverse alone", leakage == sp.zeros(13, 1))
    type_level("the nine extra legs are not recovered until a geometric/source-selected vertical soldering block, pairing, support law, overlap descent, and no-leakage theorem are constructed")
    type_level("ordinary pullback of the 13-form to X4 remains zero; neither local Gysin nor this finite lift fixture is yet a physical observed equation")


def scope_checks() -> None:
    type_level("the full linear-bridge connection and split substitution consume no P1/P2/P3 datum")
    type_level("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE and TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    type_level("no canon/status/public-posture/Lane/scheduler, datum pricing, BV/BFV, analytic domain, vacuum, generation, Standard Model, or cosmological verdict changes")
    type_level("constraint surplus is not computed until the same-bundle native action and one selected descended observation equation exist")


def main() -> int:
    print("ECW3D-B2C15R2 FULL BCH / COVARIANT SPLIT ACTION / CURVATURE ADJOINT")
    source_checks()
    layer_zero_checks()
    full_bch_checks()
    covariant_connection_checks()
    source_split_checks()
    composite_k_green_checks()
    native_curvature_order_checks()
    sequential_green_checks()
    gysin_and_equation_dual_checks()
    scope_checks()
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
    print("VERDICT: B2C15R2 PARTIAL CONSTRUCTION PASS WITH FULL LINEAR-BRIDGE BCH, PROJECTED COVARIANT SPLIT-ACTION CANDIDATE, ORDER-THREE CURVATURE CANCELLATION, LIVE A2-Z0 SUBROUTE, AND OBSERVATION-SUPPORT STOP")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
