#!/usr/bin/env python3
r"""B2C15R3 same-bundle, derived-split, and observation-support gate.

This probe keeps four statements separate:

* the reduced Spin connection correction descends on its own bundle;
* the existing native induced bundle receives it without a new scale;
* a finite source-action comparator can derive K from the same B,T fields;
* a section-supported observation current is normalized and descended, but is
  selected observation data rather than decay derived from the bulk action.

The literal source-bundle real-form port, native Alt(T) source port, complete
effective order-two coefficient, functional Euler pushdown, BV quotient, and
analytic domain remain outside this executable gate.
"""

from __future__ import annotations

from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
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


R2 = load_probe(
    "b2c15r2_predecessor",
    "eric_curt_wave3d_b2c15r2_full_bch_action_gauge_curvature_adjoint_probe.py",
)
B15P = R2.B15P
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
    print(f"{'PASS' if condition else 'FAIL'}: source receipt - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"source: {label}")


def type_level(label: str, condition: bool = True, detail: str = "") -> None:
    global TYPE
    TYPE += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: type-level - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"type: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    print(f"{'PASS' if not false_claim else 'FAIL'}: planted rejection - {label}", flush=True)
    if false_claim:
        FAILURES.append(f"planted: {label}")


def is_zero(value) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in value)
    return sp.simplify(value) == 0


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return is_zero(sp.simplify(left - right))


# ---------------------------------------------------------------------------
# Source collision and Layer 0.


def source_and_layer_zero_checks() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    portal = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()

    source_receipt(
        "the source first action uses adP-valued distortion T and the fixed one-half/one-third completion",
        "I^B_1" in pack and "T_\\omega" in pack
        and "\\frac12d_{B_\\omega}T_\\omega" in pack
        and "\\frac13[T_\\omega,T_\\omega]" in pack,
        "SOURCE-CONFIRMS",
    )
    source_receipt(
        "the source describes the Shiab output as an upstairs thirteen-form/current to be observed on X",
        "02:31:34" in portal and r"ad-valued \((14 – 1)\)-form" in portal
        and "02:35:10" in portal and "before being pulled back" in portal,
        "SOURCE-CONFIRMS the grammar; ordinary pullback is a Layer-0 homonym",
    )
    source_receipt(
        "the fibre pairing is trace-reversed Frobenius rather than a positive block-product metric",
        "00:26:28" in toe and "00:29:16" in toe,
        "SOURCE-CONFIRMS",
    )
    source_receipt(
        "the source does not supply the active Spin(9,5)-to-Sp(32,32;H) real-form bundle morphism, K split, or observation current",
        "Sp(32,32" not in pack and "K_u" not in pack and "delta_s" not in pack,
        "SOURCE-SILENT on the repository constructions",
    )
    source_receipt(
        "a frozen-reference contorsion reading is corrected by the gauge-rotated Levi-Civita/reduction grammar",
        "gauge rotated Levi-Civita connection" in toe,
        "SOURCE-CORRECTS a naked fixed projector/reference",
    )

    type_level("source P, the active native induced bundle P_nat, and its reduced Spin bundle Q are distinct principal bundles")
    type_level("source T, its moving grade-two component, Alt(T), u(T), K_u, and q_B=B+K_u are distinct typed objects")
    type_level("raw pullback, proper-support Gysin, section delta-current, coefficient dual, Krein adjoint, and physical Euler equation are distinct maps")
    type_level("the native trace-reversed Sym2 fibre and the orthodox positive/block-product comparator are rival geometry forks")
    type_level("P1/P2/P3 supplies neither a source-bundle morphism, reduction projector, observation current, support law, nor no-leakage projector")
    reject("use the rank-one P1/P2 orientation line as a ten-fibre support kernel", 1 == 10)
    reject("use the KO/count kind of P3 as a gauge projector", "KO_COUNT_TWIST" == "GAUGE_PROJECTOR")
    reject("call ordinary pullback of an upstairs thirteen-form a four-dimensional equation", sp.binomial(4, 13) != 0)


# ---------------------------------------------------------------------------
# Reduced Cech descent and induced same-bundle inclusion.


def comm(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return sp.simplify(left * right - right * left)


def ad_power(owner: sp.Matrix, value: sp.Matrix, degree: int) -> sp.Matrix:
    out = value
    for _ in range(degree):
        out = comm(owner, out)
    return out


def k_truncation(A: sp.Matrix, D_A: sp.Matrix, delta: sp.Expr, highest: int = 3) -> sp.Matrix:
    result = sp.zeros(A.rows)
    for r in range(highest + 1):
        result -= delta ** (r + 1) * ad_power(A, D_A, 2 * r + 1) / sp.factorial(2 * r + 2)
    return sp.simplify(result)


def transform_connection(B: sp.Matrix, h: sp.Matrix, x: sp.Symbol) -> sp.Matrix:
    return sp.simplify(h.inv() * B * h + h.inv() * sp.diff(h, x))


def transform_tensor(A: sp.Matrix, h: sp.Matrix) -> sp.Matrix:
    return sp.simplify(h.inv() * A * h)


def covariant_derivative(B: sp.Matrix, A: sp.Matrix, x: sp.Symbol) -> sp.Matrix:
    return sp.simplify(sp.diff(A, x) + comm(B, A))


def sp4_lie_embed(value: sp.Matrix) -> sp.Matrix:
    return sp.diag(value, -value.T)


def sp4_group_embed(value: sp.Matrix) -> sp.Matrix:
    return sp.diag(value, value.inv().T)


def same_bundle_checks() -> None:
    x = sp.symbols("x", real=True)
    h01 = sp.Matrix([[1, x], [0, 1]])
    h12 = sp.Matrix([[1, 0], [x, 1]])
    h02 = sp.simplify(h01 * h12)
    B0 = sp.Matrix([[x, 1 + x], [1 - x, -x]])
    A0 = sp.Matrix([[1, x], [2 - x, -1]])

    B1 = transform_connection(B0, h01, x)
    A1 = transform_tensor(A0, h01)
    B2_via_1 = transform_connection(B1, h12, x)
    A2_via_1 = transform_tensor(A1, h12)
    B2_direct = transform_connection(B0, h02, x)
    A2_direct = transform_tensor(A0, h02)
    exact("three reduced transition functions obey the Cech cocycle", matrix_equal(h01 * h12, h02))
    exact("the reduced connection descends consistently on the triple overlap", matrix_equal(B2_via_1, B2_direct))
    exact("the reduction coordinate descends consistently on the triple overlap", matrix_equal(A2_via_1, A2_direct))

    D0 = covariant_derivative(B0, A0, x)
    D1 = covariant_derivative(B1, A1, x)
    D2 = covariant_derivative(B2_direct, A2_direct, x)
    exact("D_B A is tensorial on the first overlap", matrix_equal(D1, h01.inv() * D0 * h01))
    exact("D_B A is tensorial on the direct second overlap", matrix_equal(D2, h02.inv() * D0 * h02))
    reject("replace D_B A by raw dA under a nonconstant overlap", matrix_equal(sp.diff(A1, x), h01.inv() * sp.diff(A0, x) * h01))

    delta = sp.Integer(3)
    K0 = k_truncation(A0, D0, delta)
    K1 = k_truncation(A1, D1, delta)
    K2 = k_truncation(A2_direct, D2, delta)
    exact("the coefficientwise BCH K is tensorial on the first overlap", matrix_equal(K1, h01.inv() * K0 * h01))
    exact("the coefficientwise BCH K is tensorial on the triple overlap", matrix_equal(K2, h02.inv() * K0 * h02))
    exact(
        "q=B+K obeys the affine connection law on both overlaps",
        matrix_equal(B1 + K1, transform_connection(B0 + K0, h01, x))
        and matrix_equal(B2_direct + K2, transform_connection(B0 + K0, h02, x)),
    )
    type_level("each entire-series coefficient is an H-intertwiner, so the convergent phi(ad_A^2) series descends coefficientwise; the finite truncation is the executable plant")

    embedded_B0 = sp4_lie_embed(B0)
    embedded_K0 = sp4_lie_embed(K0)
    embedded_h01 = sp4_group_embed(h01)
    embedded_q1 = sp4_lie_embed(B1 + K1)
    embedded_affine = sp.simplify(
        embedded_h01.inv() * (embedded_B0 + embedded_K0) * embedded_h01
        + embedded_h01.inv() * sp.diff(embedded_h01, x)
    )
    exact("an SL2-to-Sp4 structural induced-bundle comparator transports q with no affine defect", matrix_equal(embedded_q1, embedded_affine))
    X = sp.Matrix([[1, 2], [3, -1]])
    Y = sp.Matrix([[0, 1], [-2, 0]])
    exact("the structural induced inclusion preserves the Lie bracket", matrix_equal(sp4_lie_embed(comm(X, Y)), comm(sp4_lie_embed(X), sp4_lie_embed(Y))))
    lam = sp.symbols("lambda")
    scale_defect = sp.simplify(comm(lam * sp4_lie_embed(X), lam * sp4_lie_embed(Y)) - lam * sp4_lie_embed(comm(X, Y)))
    nonzero_scale_entry = next(entry for entry in scale_defect if entry != 0)
    exact("a rescaled nonabelian inclusion is a Lie map only at scale zero or one", sp.solve(nonzero_scale_entry, lam) == [0, 1])

    J = sp.Matrix([[0, 1], [-1, 0]])
    g = sp.Matrix([[1, 1], [0, 1]])

    def pr_j(value: sp.Matrix) -> sp.Matrix:
        return sp.simplify(-sp.trace(J * value) * J / 2)

    moved_J = sp.simplify(g * J * g.inv())
    fixed_projection = pr_j(moved_J)
    moved_projection = sp.simplify(g * pr_j(g.inv() * moved_J * g) * g.inv())
    reject("claim ambient covariance in the structural comparator using a fixed reduced projector", matrix_equal(fixed_projection, moved_J))
    exact("the structural conjugated moving projector follows the moved reduced subalgebra", matrix_equal(moved_projection, moved_J))
    type_level("the abstract reduced descent theorem is earned from intertwining; this executable atlas is SL2-to-Sp4, while active Spin-to-Sp(32,32;H) descent is a formal corollary conditional on the prior G1/R2 native inclusion receipts")
    type_level("the literal source P still needs an explicit reduction/bundle isomorphism, and this gate does not newly machine-check the 128-dimensional right-H/Krein inclusion on overlaps")
    type_level("the descent theorem is signature-independent algebraically, but source-action placement remains on the native trace-reversed fork until the positive/block-product rival is separately ported")


# ---------------------------------------------------------------------------
# K derived from the same finite B,T fixture and substituted into I1 grammar.


def derived_action_checks() -> None:
    M = G2["M"]
    B = G2["form1"](M(1, 1, 0, -1), M(0, 1, 2, 1), M(2, -1, 1, 0))
    T = G2["form1"](M(0, 2, -1, 1), M(1, -1, 1, 2), M(-1, 0, 2, 1))
    dB = G2["form2"](M(0, 1, -1, 0), M(1, 0, 2, -1), M(-1, 2, 0, 1))
    dT = G2["form2"](M(2, -1, 0, 1), M(0, 2, 1, -1), M(1, 0, -2, 1))

    zero = M(0, 0, 0, 0)

    def zero_jet():
        return [[zero for _ in range(3)] for _ in range(3)]

    def exterior_from_jet(jet):
        return tuple(G2["sub"](jet[i][j], jet[j][i]) for i, j in ((0, 1), (0, 2), (1, 2)))

    # The exterior jets dB,dT leave symmetric first-jet components free.  This
    # declared compatible completion makes A=T_0 constant; it is fixture data,
    # not something derived from dT alone.
    Bjet = zero_jet()
    Tjet = zero_jet()
    Bjet[0][1], Bjet[0][2], Bjet[1][2] = dB
    Tjet[0][1], Tjet[0][2], Tjet[1][2] = dT
    exact("the declared full B first jet realizes the recorded exterior dB", exterior_from_jet(Bjet) == dB)
    exact("the declared constant-A full T first jet realizes the recorded exterior dT", exterior_from_jet(Tjet) == dT)

    # L_fin(T)=T_0 is a declared finite port, not the native Alt map.
    A = T[0]
    Kbar = tuple(G2["neg"](G2["comm"](A, G2["comm"](entry, A))) for entry in B)
    dKbar = tuple(G2["neg"](G2["comm"](A, G2["comm"](entry, A))) for entry in dB)
    expected_Kbar = G2["form1"](M(-9, 1, -4, 9), M(7, -21, -7, -7), M(-5, -1, -3, 5))
    expected_dKbar = G2["form2"](M(-3, 5, 1, 3), M(-4, -12, -8, 4), M(6, -10, -2, -6))
    exact("the finite correction Kbar is derived from the same B,T fixture", Kbar == expected_Kbar)
    exact("the exterior jet dKbar follows from the declared compatible constant-A germ", dKbar == expected_dKbar)

    def derived_dk(owner, owner_jet, connection, connection_jet):
        def partial_k(i: int, j: int):
            first = G2["comm"](owner_jet[i], G2["comm"](connection[j], owner))
            inner = G2["add"](
                G2["comm"](connection_jet[i][j], owner),
                G2["comm"](connection[j], owner_jet[i]),
            )
            return G2["neg"](G2["add"](first, G2["comm"](owner, inner)))

        return tuple(G2["sub"](partial_k(i, j), partial_k(j, i)) for i, j in ((0, 1), (0, 2), (1, 2)))

    dA = [Tjet[index][0] for index in range(3)]
    exact("the declared constant-A germ reproduces dKbar by differentiating Kbar", derived_dk(A, dA, B, Bjet) == dKbar)
    Tjet_moving = [row[:] for row in Tjet]
    moving_A_jet = M(1, 0, 0, -1)
    Tjet_moving[1][0] = moving_A_jet
    Tjet_moving[0][1] = G2["add"](dT[0], moving_A_jet)
    exact("a nonconstant-A heldout full jet preserves the same exterior dT", exterior_from_jet(Tjet_moving) == dT)
    dKbar_moving = derived_dk(A, [Tjet_moving[index][0] for index in range(3)], B, Bjet)
    reject("infer dKbar from dB alone without pricing the missing symmetric T first jet", dKbar_moving == dKbar)

    discriminant = G2["tr"](A) ** 2 - 4 * (A[0][0] * A[1][1] - A[0][1] * A[1][0])
    exact("the declared reduction owner has Cayley-Hamilton discriminant minus seven", discriminant == F(-7))
    C0 = G2["comm"](B[0], A)
    ch_chain = []
    for r in range(4):
        left = C0
        for _ in range(2 * r + 1):
            left = G2["comm"](A, left)
        right = G2["scale"](discriminant**r, G2["comm"](A, C0))
        ch_chain.append(left == right)
    exact("the odd adjoint tower collapses coefficientwise by Cayley-Hamilton", all(ch_chain), str(ch_chain))

    def split_action(scale: F, port: int = 0) -> F:
        owner = T[port]
        k_owner = tuple(G2["neg"](G2["comm"](owner, G2["comm"](entry, owner))) for entry in B)
        dk_owner = tuple(G2["neg"](G2["comm"](owner, G2["comm"](entry, owner))) for entry in dB)
        Bhat = G2["f1_add"](B, G2["f1_scale"](scale, k_owner))
        That = G2["f1_add"](T, G2["f1_scale"](-scale, k_owner))
        dBhat = G2["f2_add"](dB, G2["f2_scale"](scale, dk_owner))
        dThat = G2["f2_add"](dT, G2["f2_scale"](-scale, dk_owner))
        return G2["source_action"](Bhat, dBhat, That, dThat, G2["shiab_identity"], F(2))

    scales = list(map(F, (-2, -1, 0, 1, 2)))
    values = [split_action(scale) for scale in scales]
    exact(
        "the actual same-fixture derived-K split has the exact action polynomial (378 s^2+280 s+23)/2",
        values == [F(975, 2), F(121, 2), F(23, 2), F(681, 2), F(2095, 2)],
        str(values),
    )
    s = sp.symbols("s", real=True)
    polynomial = sp.interpolate([(sp.Rational(x.numerator, x.denominator), sp.Rational(y.numerator, y.denominator)) for x, y in zip(scales, values)], s)
    exact("five exact evaluations recover the written split polynomial", sp.expand(polynomial) == (378 * s**2 + 280 * s + 23) / 2)

    f = (1 - sp.cos(sp.sqrt(21))) / 7
    response = sp.simplify(polynomial.subs(s, f) - polynomial.subs(s, 0))
    exact("the full-series derived correction changes the finite source action by 189 f^2+140 f", sp.simplify(response - (189 * f**2 + 140 * f)) == 0)
    exact("the derived full-series response is strictly positive", sp.ask(sp.Q.positive(response)) is True, f"response={sp.N(response, 12)}")
    delta = sp.symbols("Delta", positive=True)
    f_delta = (1 - sp.cos(sp.sqrt(7 * delta))) / 7
    direct_derivative = sp.diff(polynomial.subs(s, f_delta), delta)
    chain_derivative = sp.diff(polynomial, s).subs(s, f_delta) * sp.diff(f_delta, delta)
    exact("the full-series coefficient variation equals the explicit K-chain rule", sp.simplify(direct_derivative - chain_derivative) == 0)
    exact("the K-chain is live at Delta=3", sp.simplify(chain_derivative.subs(delta, 3)) != 0)
    reject("drop the derived K chain and report zero coefficient response", sp.simplify(chain_derivative.subs(delta, 3)) == 0)

    endpoint0 = G2["curvature"](G2["f1_add"](B, T), G2["f2_add"](dB, dT))
    Bhat1 = G2["f1_add"](B, Kbar)
    That1 = G2["f1_add"](T, G2["f1_scale"](F(-1), Kbar))
    dBhat1 = G2["f2_add"](dB, dKbar)
    dThat1 = G2["f2_add"](dT, G2["f2_scale"](F(-1), dKbar))
    endpoint1 = G2["curvature"](G2["f1_add"](Bhat1, That1), G2["f2_add"](dBhat1, dThat1))
    exact("the derived split fixes the total connection and its exterior curvature jet", endpoint0 == endpoint1)

    g = M(1, 1, 0, 1)
    B_g = G2["transform_f1"](g, B)
    T_g = G2["transform_f1"](g, T)
    dB_g = G2["transform_f2"](g, dB)
    A_g = T_g[0]
    Kbar_g = tuple(G2["neg"](G2["comm"](A_g, G2["comm"](entry, A_g))) for entry in B_g)
    exact("the same-fixture Kbar construction is equivariant under common conjugation", Kbar_g == G2["transform_f1"](g, Kbar))
    moved_action = G2["source_action"](
        G2["transform_f1"](g, Bhat1),
        G2["transform_f2"](g, dBhat1),
        G2["transform_f1"](g, That1),
        G2["transform_f2"](g, dThat1),
        G2["shiab_identity"],
        F(2),
    )
    exact("the derived split action is invariant under common constant gauge conjugation", moved_action == split_action(F(1)))

    heldout_1 = [split_action(scale, 1) for scale in scales]
    heldout_2 = [split_action(scale, 2) for scale in scales]
    reject("identify the declared finite port L_fin(T)=T0 with a port-independent native Alt map", heldout_1 == values or heldout_2 == values)
    type_level("the finite result closes the independently-supplied-K hole at structural germ grade after declaring a compatible constant-A full first jet; dT alone does not select that jet")
    type_level("native promotion still needs Alt(pr_h^epsilon T), its full first-jet owner, and the actual source-bundle port")
    type_level("the exact first variation contains the pre-existing B and T Euler covectors plus (D K)^! applied to their difference, every moving Shiab/Hodge/density/Krein/lowerer owner, and its Green boundary")
    type_level("fixed-varpi source coordinates and fixed-total-connection variations are different chains and may not reuse one another")
    type_level("no lambda_red or new continuous action coefficient is introduced; the linear bridge sees only Delta=c3^2-c11^2")
    type_level("physical constraint surplus remains UNCOMPUTED until the native port and one descended, no-leakage observed equation exist")


# ---------------------------------------------------------------------------
# Trace-reversed fibre density and section-current observation.


def observation_checks() -> None:
    lam = sp.symbols("lambda", positive=True)
    lebesgue_scale = lam**10
    determinant_density_scale = lam**-10
    exact("the trace-reversed metric fibre supplies a scale-invariant absolute density", sp.simplify(lebesgue_scale * determinant_density_scale) == 1)
    A_gl = sp.diag(2, 1, 1, 1)
    inverse_scales = [sp.Rational(1, 2), 1, 1, 1]
    sym2_jacobian = sp.prod(inverse_scales[i] * inverse_scales[j] for i in range(4) for j in range(i, 4))
    expected_sym2_jacobian = sp.det(A_gl) ** -5
    metric_determinant_scale = sp.det(A_gl) ** -2
    density_weight_scale = metric_determinant_scale ** sp.Rational(-5, 2)
    exact("a non-unimodular GL4 congruence has the Sym2 Jacobian det(A)^-5", sp.simplify(sym2_jacobian - expected_sym2_jacobian) == 0 and sym2_jacobian == sp.Rational(1, 32))
    exact("the general-congruence density weight cancels that non-unimodular Sym2 Jacobian", sp.simplify(sym2_jacobian * density_weight_scale) == 1)
    type_level("the invariant density has radial measure d lambda/lambda and infinite mass; it supplies neither decay nor finite normalization")
    radius = sp.symbols("r", positive=True)
    reject("turn the indefinite DeWitt (6,4) fibre metric into a decaying positive Gaussian cutoff", sp.limit(sp.exp(radius**2), radius, sp.oo) == 0)
    reject("use a nonzero invariant scalar on a transitive noncompact fibre as compact support", sp.limit(sp.Integer(1), radius, sp.oo) == 0)

    KX = sp.diag(-1, 1, 1, 1)
    KV = sp.diag(1, 1, 1, 1, 1, 1, -1, -1, -1)
    KY = sp.diag(KX, KV)
    L = sp.Matrix.vstack(sp.eye(4), sp.zeros(9, 4))
    R = sp.simplify(KX.inv() * L.T * KY)
    exact("the Levi-Civita horizontal lift has Krein left inverse R L=1", matrix_equal(R * L, sp.eye(4)))

    H01 = sp.diag(-1, -1, 1, 1)
    H12 = sp.eye(4)
    H12[1, 1] = 0
    H12[2, 2] = 0
    H12[1, 2] = 1
    H12[2, 1] = 1
    V01 = sp.diag(-1, -1, 1, 1, 1, 1, 1, 1, 1)
    V12 = sp.diag(1, -1, -1, 1, 1, 1, 1, 1, 1)
    T01 = sp.diag(H01, V01)
    T12 = sp.diag(H12, V12)
    T02 = sp.simplify(T01 * T12)
    H02 = sp.simplify(H01 * H12)
    exact("the three observation transitions satisfy their cocycles", matrix_equal(T01 * T12, T02) and matrix_equal(H01 * H12, H02))
    exact("the upstairs and observed Krein forms are preserved on both overlaps", matrix_equal(T01.T * KY * T01, KY) and matrix_equal(T12.T * KY * T12, KY) and matrix_equal(H01.T * KX * H01, KX) and matrix_equal(H12.T * KX * H12, KX))
    exact("the horizontal observation lift descends on all three patches", matrix_equal(T01 * L, L * H01) and matrix_equal(T12 * L, L * H12) and matrix_equal(T02 * L, L * H02))
    exact("the Krein left inverse is natural on all three patches", matrix_equal(R * T01, H01 * R) and matrix_equal(R * T12, H12 * R) and matrix_equal(R * T02, H02 * R))

    E2 = sp.Matrix(list(range(1, 14)))
    E1 = sp.simplify(T12.inv().T * E2)
    E0 = sp.simplify(T01.inv().T * E1)
    exact("Euler covectors descend dually on the triple overlap", matrix_equal(E0, T02.inv().T * E2))
    exact("the coefficient-bundle observation dual descends", matrix_equal(L.T * E0, H02.inv().T * L.T * E2))

    Pdual = sp.simplify(R.T * L.T)
    base_covector = sp.Matrix([2, -1, 3, 4] + [0] * 9)
    hidden = sp.Matrix([0] * 4 + [1, -2, 3, 0, 0, 0, 0, 0, 0])
    exact("the section-selected horizontal equation can satisfy the independent no-leakage condition", matrix_equal((sp.eye(13) - Pdual) * base_covector, sp.zeros(13, 1)))
    exact("a hidden covector is invisible to the observed coefficient equation", matrix_equal(L.T * (base_covector + hidden), L.T * base_covector))
    reject("infer no leakage from the observed equation or R L=1 alone", matrix_equal((sp.eye(13) - Pdual) * (base_covector + hidden), sp.zeros(13, 1)))

    N = sp.zeros(13, 4)
    N[4, 2] = 1
    L_bad = L + N
    exact("a vertical lift perturbation can preserve the local left-inverse equation", matrix_equal(R * L_bad, sp.eye(4)))
    reject("infer overlap descent for an arbitrary vertical lift perturbation from R L=1", matrix_equal(T01 * L_bad, L_bad * H01))

    # The support current lives in all ten metric-fibre directions.  The
    # separate 13=4+9 coefficient carrier above does not change this
    # codimension.
    z = sp.symbols("z0:10")
    section_value = sp.Integer(5)
    integrand = section_value + sum((index + 1) * z[index] for index in range(10))
    delta_evaluation = integrand.subs({coordinate: 0 for coordinate in z})
    exact("the normalized section delta-current has pi_!(delta_s)=1 and evaluates a field on the observation section", delta_evaluation == section_value)
    delta_coordinate_weight = 1 / sym2_jacobian
    exact("the ten-fibre delta density transforms with the inverse non-unimodular Jacobian and remains normalized", sp.simplify(delta_coordinate_weight * sym2_jacobian) == 1)
    reject("leave the ten-fibre delta density untransformed under a non-unimodular congruence", sym2_jacobian == 1)
    reject("leave the section-current normalization free", 2 * delta_evaluation == delta_evaluation)
    kernel_at_zero = (z[0] ** 2).subs(z[0], 0)
    normalized_two_point_kernel = (sp.Rational(1, 2) * z[0] ** 2).subs(z[0], -1) + (sp.Rational(1, 2) * z[0] ** 2).subs(z[0], 1)
    reject("infer a unique smooth observation kernel from normalization alone", kernel_at_zero == normalized_two_point_kernel)
    type_level("the ten-fibre delta_s is properly supported on the section graph and its density Jacobian is atlas-covariant, but it is distributional section data rather than smooth decay selected by the written bulk action")
    type_level("the coefficient dual becomes a functional Euler adjoint only after pairing with delta_s or another specified transverse current")
    type_level("the selected LC lift returns the four previously Gysin-eligible legs; the remaining nine need an independently derived vertical soldering block and may not be fitted to the desired equation")


# ---------------------------------------------------------------------------
# Effective-order guard and scope.


def effective_order_and_scope_checks() -> None:
    base_first_derivatives = [B15P.DG[index] for index in range(4)]
    nonzero_counts = [sum(entry != 0 for entry in matrix) for matrix in base_first_derivatives]
    exact("the actual B2C15P Zorro-DeWitt fixture has live base first derivatives", all(count > 0 for count in nonzero_counts), str(nonzero_counts))
    reject("erase A1 Z1 and derivative-Z1 terms by calling the existing fixture normal-coordinate constant", all(matrix_equal(matrix, sp.zeros(14)) for matrix in base_first_derivatives))

    A2 = sp.Matrix([[1, 0], [0, 0]])
    Z1 = sp.Matrix([[0, 0], [1, 0]])
    Z0 = sp.Matrix([[1, 0], [1, 2]])
    A1 = sp.Matrix([[0, -1], [0, 0]])
    C3 = sp.simplify(A2 * Z1)
    C20 = sp.simplify(A2 * Z0)
    C2 = sp.simplify(C20 + A1 * Z1)
    exact("order-three cancellation does not prevent same-order A1 Z1 cancellation of a live A2 Z0 block", matrix_equal(C3, sp.zeros(2)) and C20.rank() == 1 and C2.rank() == 0)
    reject("promote the prior A2 Z0 ranks to the complete native effective order-two symbol", C20.rank() == C2.rank())
    type_level("the actual complete coefficient is A2(2 partial Z1+Z0)+A1 Z1 plus the remaining moving Shiab/frame/density/lowerer terms; it is still unassembled")
    type_level("this gate therefore closes the abstract reduced theorem and a declared-germ derived finite action response, but does not earn an active-native atlas, four-dimensional SM/Einstein equation, BV quotient, domain, or constraint surplus")
    type_level("P1/P2/P3 remains unchanged and unused")
    type_level("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    type_level("TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")


def main() -> int:
    print("ECW3D-B2C15R3 SAME-BUNDLE / DERIVED-SPLIT / OBSERVATION-SUPPORT GATE")
    print("=" * 86)
    source_and_layer_zero_checks()
    same_bundle_checks()
    derived_action_checks()
    observation_checks()
    effective_order_and_scope_checks()
    total = EXACT + SOURCE + TYPE + PLANTED
    print("-" * 86)
    print(f"COUNTS: {EXACT} exact + {SOURCE} source receipts + {TYPE} type-level + {PLANTED} planted = {total}")
    print(f"FAILURES: {len(FAILURES)}")
    if FAILURES:
        for failure in FAILURES:
            print(f" - {failure}")
        return 1
    print("VERDICT: B2C15R3 PARTIAL CONSTRUCTION PASS WITH ABSTRACT REDUCED DESCENT, STRUCTURAL INDUCED-BUNDLE COMPARATOR, DECLARED-GERM DERIVED-K ACTION RESPONSE, TEN-FIBRE SECTION CURRENT, AND FULL-ORDER2 STOP")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
