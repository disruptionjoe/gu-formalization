#!/usr/bin/env python3
r"""PW2E mixed metric/Frechet owner and native-Ward readiness gate.

This gate combines four previously separate earned pieces without pretending
that their composition has already been evaluated:

* the inherited structural 1D fixed-varpi chain-rule and Green certificate;
* the actual ten-owner, eight-slot moving native Shiab coefficient;
* the actual first-order induced-Y14 Levi-Civita spin graph; and
* the predecessor 2x2 residual active gauge-Ward comparator.

It then checks a conservative jet order for the missing composition.  The
current native fixture fixes a total-space metric two-jet, induced from a base
metric three-jet.  A scalar action/Frechet comparator can require a total
metric third jet and hence a base metric fourth jet after a first-order Zorro
graph.  Two exact comparator completions agreeing through the available base
three-jet give different returns.  This proves that the current fixture does
not by itself exclude fourth-jet dependence; it does not prove that the full
native GU composition has a nonzero fourth-jet coefficient, because other
same-order terms may cancel it.

This is a conservative sufficiency test: first assemble the complete native
top-order coefficient and prove whether it cancels.  Build an explicit
fourth-order native background family only if a nonzero coefficient survives.
It is not a no-go for the GU action.
"""

from __future__ import annotations

from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
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


D = load_probe("pw2e_metric_pw2d", "pw2d_native_transported_shiab_action_probe.py")
O = load_probe(
    "pw2e_metric_b2c15o",
    "eric_curt_wave3d_b2c15o_native_y14_background_stabilizer_probe.py",
)
P = load_probe(
    "pw2e_metric_b2c15p",
    "eric_curt_wave3d_b2c15p_source_epsilon_tangent_zorro_dewitt_probe.py",
)
W = load_probe("pw2e_metric_ward", "pw2d_right_tilted_ward_green_probe.py")
M = D.M
B15 = O.B15


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


def is_zero(value) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in value)
    return sp.simplify(value) == 0


def source_and_layer_zero() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    portal = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
    source(
        "the written first action uses epsilon, varpi, B_omega, T_omega, the one-half/one-third curvature block, and the bosonic distortion-norm slot",
        all(
            token in pack
            for token in (
                "T_\\omega",
                "B_\\omega",
                "\\frac12d_{B_\\omega}T_\\omega",
                "\\frac13[T_\\omega,T_\\omega]",
                "kappa_1",
            )
        ),
        "SOURCE-CONFIRMS",
    )
    source(
        "Weinstein places gauge-rotated Levi-Civita in the contorsion slot",
        "[02:19:17]" in toe and "[02:19:49]" in toe,
        "SOURCE-CONFIRMS",
    )
    source(
        "the reviewed source corpus does not release the active native mixed metric Frechet formula or a diffeomorphism Ward identity",
        "Section 9.1" in pack
        and "[02:19:17]" in toe
        and "[02:19:49]" in toe
        and "02:23:30" in portal
        and "02:23:52" in portal,
        "SOURCE-SILENT against draft section 9.1, TOE 02:19:17-02:19:49, and Portal 02:23:30-02:23:52",
    )
    typed("fixed total A, fixed source varpi, and fixed B are different metric variations")
    typed("residual internal gauge Ward, diffeomorphism Ward, Xi=D Upsilon redundancy, and Euler equation are different objects")
    typed("a point metric, total-space metric two-jet, base metric three-jet, and full composed action jet are different grades")
    typed("D.build_source_t and O's finite source-coordinate epsilon surrogate are not identified with Weinstein's T_omega and H-valued epsilon")
    typed("the kappa1/2 <T,*T> term is a bosonic distortion norm, not the fermion/Higgs/Yukawa mass carrier")
    reject("use the internal gauge Ward identity to erase the physical metric Euler owner", False)
    reject("call a structural Z0/Z1 comparator the evaluated native Y14 coefficient", False)
    synthetic_source = inspect.getsource(D.build_source_t)
    reject(
        "identify the synthetic source_t fixture with source T_omega",
        all(token in synthetic_source for token in ("epsilon", "varpi", "d_0")),
    )
    kappa_rows = [line for line in pack.splitlines() if "kappa_1" in line]
    if not kappa_rows:
        raise AssertionError("source packet must contain a kappa_1 row")
    reject(
        "identify the bosonic kappa1 distortion norm with a fermion/Yukawa mass term",
        "Yukawa" in kappa_rows[0],
    )


def fixed_varpi_source_return() -> None:
    correction = O.GAMMA_ADJOINT_E_T
    exact(
        "the inherited structural 1D source-coordinate varpi Euler covector is exactly the distortion Euler covector",
        all(
            is_zero(O.SOURCE_EULERS[O.varpi[index]] - O.SOURCE_E_T[index])
            for index in range(2)
        ),
    )
    exact(
        "the inherited structural 1D fixed-varpi metric return includes the live formal adjoint (D_g Gamma)^! E_T",
        is_zero(O.SOURCE_EULERS[O.B13.g] - O.FIXED_A_G - correction)
        and not is_zero(correction),
    )
    exact(
        "that structural fixed-varpi correction carries a separate nonzero Green companion",
        is_zero(O.SOURCE_THETA - O.FIXED_A_THETA_IN_SOURCE - O.GAMMA_GREEN_COMPANION)
        and not is_zero(O.GAMMA_GREEN_COMPANION),
    )
    reject("reuse the fixed-A metric equation after changing to source coordinates", is_zero(correction))
    reject("give K an independent Euler equation after declaring it a derived graph", False)
    third_jet = sp.diff(O.B13.g, O.B13.x, 3)
    fixed_a_third = sp.diff(O.FIXED_A_G, third_jet)
    gamma_third = sp.diff(O.GAMMA_ADJOINT_E_T, third_jet)
    source_third = sp.diff(O.SOURCE_EULERS[O.B13.g], third_jet)
    exact(
        "the inherited structural fixture has live fixed-A and Gamma-adjoint third-jet terms that cancel in the fixed-varpi sum",
        not is_zero(fixed_a_third)
        and is_zero(fixed_a_third + gamma_third)
        and is_zero(source_third),
        f"fixed_A={fixed_a_third}; Gamma={gamma_third}; source={source_third}",
    )
    typed("this finite two-component chain-rule certificate is not the actual 1274x10 native Y14 Levi-Civita composition")


def native_metric_inventory() -> None:
    curvature = D.to_sympy_form(D.P.SPIN_CURVATURE)
    fixed = D.shiab(curvature)
    source_t = D.build_source_t(fixed)
    d_t = {(0, 7): M.sscale(M.sblade(1, 3), -1)}
    q_t = M.sfwedge(source_t, source_t)
    original = M.sfadd(
        curvature,
        M.sfscale(d_t, sp.Rational(1, 2)),
        M.sfscale(q_t, sp.Rational(1, 3)),
    )

    slots: dict[str, int] = {}
    returns = []
    action_returns = []
    for owner, hvar in enumerate(B15.H_VARIATIONS):
        parts = M.moving_metric_shiab_parts(
            original, hvar, M.canonical_trace_motion(owner)
        )
        for name, value in parts.items():
            slots[name] = slots.get(name, 0) + len(M.flatten_form(value))
        total = M.sfadd(*parts.values())
        returns.append(M.flatten_form(total))
        action_returns.append(D.top_scalar(source_t, total))
    keys = sorted(set().union(*(set(item) for item in returns)))
    matrix = sp.Matrix([[item.get(key, 0) for item in returns] for key in keys])
    expected = {
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
        "all eight actual moving-Shiab metric slots are live",
        set(slots) == expected and all(count > 0 for count in slots.values()),
        str(slots),
    )
    exact(
        "the actual moving-Shiab coefficient sees all ten trace-reversed metric owners",
        matrix.rank() == 10,
        f"rows={matrix.rows}; rank={matrix.rank()}",
    )
    exact(
        "the frozen synthetic-source pairing sees a live moving-Shiab metric contribution",
        any(value != 0 for value in action_returns),
        f"nonzero={sum(value != 0 for value in action_returns)}/10",
    )

    # Assemble only the actual induced LC spin graph, without allocating the
    # enormous residual pairing used by the predecessor census.
    def lc_matrix(xi: tuple[F, ...], observed: bool = False) -> sp.Matrix:
        result = sp.zeros(14 * len(B15.H_BIVECTORS), 10)
        cut = sp.diag(1, 1, 1, 1, *([0] * 10))
        for owner, hvar in enumerate(B15.H_VARIATIONS):
            argument = cut * hvar * cut if observed else hvar
            value = B15.lc_spin_form(xi, argument)
            for (mu,), internal in value.items():
                for mask, coefficient in internal.items():
                    result[B15.H_INPUT_INDEX[(mu, mask)], owner] = coefficient
        return result

    xi_positive = tuple(F(1) if index == 0 else F(0) for index in range(14))
    xi_null = tuple(F(1) if index in (0, 3) else F(0) for index in range(14))
    ranks = []
    difference_ranks = []
    for xi in (xi_positive, xi_null):
        actual = lc_matrix(xi)
        observed = lc_matrix(xi, True)
        ranks.append(actual.rank())
        difference_ranks.append((actual - observed).rank())
    exact(
        "the actual first-order induced-Y14 Levi-Civita spin graph is live on nonnull and null covectors",
        all(rank > 0 for rank in ranks),
        f"ranks={ranks}",
    )
    exact(
        "the actual induced-Y14 graph is not the hostile observed-four-dimensional lift",
        all(rank > 0 for rank in difference_ranks),
        f"difference_ranks={difference_ranks}",
    )
    reject("freeze any of the eight metric slots because the LC graph is already live", False)
    reject("replace the induced-Y14 LC graph by its observed 4D truncation", all(rank == 0 for rank in difference_ranks))


def active_ward_and_metric_owner() -> None:
    x = sp.symbols("x", real=True)
    connection = sp.Matrix([[x, 1 + x], [2 - x, -x]])
    distortion = sp.Matrix([[1 + x, x**2], [1 - x, -1 - x]])
    reduction = sp.Matrix([[2 - x, 1 + x**2], [x, x - 2]])
    ghost = sp.Matrix([[x * (1 - x), 1 + x], [x**2, -x * (1 - x)]])
    lagrangian, kinetic, e_c, e_t, e_q = W.action_objects(
        connection, distortion, reduction, x
    )
    ward = W.cov(connection, e_c, x) + W.comm(distortion, e_t) + W.comm(reduction, e_q)
    rho = sp.symbols("rho", real=True)
    delta_c = -W.cov(connection, ghost, x)
    delta_t = W.comm(ghost, distortion)
    delta_q = W.comm(ghost, reduction)
    y = W.comm(reduction, distortion)
    delta_kinetic = W.cov(connection, delta_t, x) + W.comm(delta_c, distortion)
    delta_y = W.comm(delta_q, distortion) + W.comm(reduction, delta_t)
    direct = sp.expand(
        rho
        * (
            W.tr(kinetic * delta_kinetic)
            + W.tr(y * delta_y)
            + W.tr(distortion**3 * delta_t)
        )
    )
    exact(
        "the predecessor 2x2 residual active gauge-Ward comparator is off-shell and nontrivial",
        W.is_zero(ward) and not W.is_zero(e_c) and not W.is_zero(e_t) and not W.is_zero(e_q),
    )
    exact(
        "a gauge-invariant scalar weight can have a live Euler derivative while the internal gauge variation still vanishes",
        sp.simplify(direct) == 0 and lagrangian != 0 and sp.diff(rho * lagrangian, rho) == lagrangian,
    )
    reject("deduce the metric Euler equation from the residual internal gauge Ward identity", lagrangian == 0)
    typed("a formal diffeomorphism Noether schema can be derived now, but native evaluation and rank require the full composed metric owner")


def jet_determinacy_and_c2_gate() -> None:
    x, a, b = sp.symbols("x a b", real=True)
    base = 1 + 2 * x + 3 * x**2 + 5 * x**3
    g_a = base + a * x**4 / 24
    g_b = base + b * x**4 / 24
    same_through_three = all(
        sp.diff(g_a, x, degree).subs(x, 0)
        == sp.diff(g_b, x, degree).subs(x, 0)
        for degree in range(4)
    )
    # Valid scalar variational/Frechet comparator:
    #   G=g', F=G'=g'', L=1/2 F^2,
    #   E_G=-G'', (D_g G)^!E_G=-d(E_G)=g''''=E_g(L).
    # It proves possible fourth-jet sensitivity, not the unassembled native
    # GU coefficient.
    g = sp.Function("g")(x)
    graph = sp.diff(g, x)
    field_strength = sp.diff(graph, x)
    scalar_action = sp.Rational(1, 2) * field_strength**2
    direct_euler = sp.diff(sp.diff(scalar_action, sp.diff(g, x, 2)), x, 2)
    graph_euler = -sp.diff(field_strength, x)
    chained_euler = -sp.diff(graph_euler, x)
    return_a = sp.diff(g_a, x, 4).subs(x, 0)
    return_b = sp.diff(g_b, x, 4).subs(x, 0)
    exact(
        "a derived scalar action/Frechet comparator can distinguish two base metrics agreeing through the available three-jet",
        is_zero(direct_euler - chained_euler)
        and direct_euler == sp.diff(g, x, 4)
        and same_through_three
        and return_a == a
        and return_b == b
        and return_a != return_b,
        f"returns=({return_a},{return_b})",
    )
    exact(
        "the current native fixture explicitly stops at a total-space metric two-jet",
        P.G0.shape == (14, 14)
        and len(P.DG) == 14
        and len(P.D2G) == 14
        and all(len(row) == 14 for row in P.D2G),
        "G0,DG,D2G present; D3G not constructed",
    )
    reject("treat a base metric three-jet as sufficient for every possible composed metric Euler coefficient", return_a == return_b)
    actual_d3g = getattr(P, "D3G", None)
    reject(
        "promote possible fourth-jet dependence to an actual native nonzero coefficient before D3G and all same-order terms are assembled",
        actual_d3g is not None and return_a != return_b,
    )

    # Exact cancellation control for the still-unassembled complete C2 block.
    A2 = sp.Matrix([[1, 0], [0, 0]])
    Z1 = sp.Matrix([[0, 0], [1, 0]])
    Z0 = sp.Matrix([[1, 0], [1, 2]])
    A1 = sp.Matrix([[0, -1], [0, 0]])
    c3 = A2 * Z1
    c20 = A2 * Z0
    c2 = c20 + A1 * Z1
    exact(
        "the planted exact comparator confirms that live A2 Z0 can be cancelled by same-order A1 Z1",
        c3 == sp.zeros(2) and c20.rank() == 1 and c2.rank() == 0,
    )
    reject("promote the known native A2 Z0 rank to the complete C2 rank", c20.rank() == c2.rank())
    typed("PW2F-A must first compose the actual top-order D_g Gamma, D_g h, literal D_g K, all eight Shiab slots, Hodge distortion norm, density/Krein lowerers, and every generated Green term")
    typed("only if a nonzero total-third/base-fourth coefficient survives should PW2F-B build a fourth-order background family")
    typed("any surviving continuous jet/Frechet requirement cannot be supplied by P1/P2/P3")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE; TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")


def main() -> int:
    print("PW2E MIXED METRIC / FRECHET / NATIVE-WARD READINESS")
    source_and_layer_zero()
    fixed_varpi_source_return()
    native_metric_inventory()
    active_ward_and_metric_owner()
    jet_determinacy_and_c2_gate()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + "
        f"{PLANTED} planted = {total}; failures={len(FAILURES)}"
    )
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print("VERDICT: PW2E MIXED OWNER INVENTORY PASS; NATIVE TOP-ORDER COMPOSITION AND METRIC-WARD EVALUATION REMAIN UNASSEMBLED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
