#!/usr/bin/env python3
r"""PW2F-R2B2A principal-order audit and partial moving-C4 comparator.

The probe keeps two columns distinct:

* chartwise source-aligned: local ``(g, epsilon, varpi)`` grammar, for which
  the inspected sources do not select a complete Shiab or an epsilon-to-h
  tangent; and
* active-native reconstruction: the repository's trace-reversed ``(9,5)``
  Clifford/Shiab graph with ``h=exp(u)``.

The executable intentionally exposes a negative result from hostile review:
its ``delta T=-Ad(h^-1) delta B`` path is a fixed-total-connection synthetic
comparator, not the corrected fixed-``(epsilon,varpi)`` source tangent
``delta T=-delta q``.  It reconstructs the comparator's 3+1 moving-Shiab
cross, 2+2 action Hessian, and kappa distortion norm.  The unconstructed
``h/theta1/Bhat2`` second graph and five non-Shiab coefficient slots remain
open.  The result is therefore partial formal local principal-symbol data, not
a complete C4, characteristic, domain, quotient, observation equation, or
physics claim.  P1/P2/P3 are unused.
"""

from __future__ import annotations

from fractions import Fraction as F
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


R = load_probe("pw2fr2b2a_r", "pw2fr_complete_derived_k_c3_probe.py")
B1 = load_probe("pw2fr2b2a_b1", "pw2fr2b1_section_jvp_source_coordinate_probe.py")
M = R.M
D = R.D
E = R.E
P = R.P


FAILURES: list[str] = []
EXACT = TYPE = PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: exact - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"exact: {label}")


def type_level(label: str, condition: bool = True) -> None:
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


def is_zero(value) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(item) == 0 for item in value)
    return sp.simplify(value) == 0


def form_equal(left: M.SForm, right: M.SForm) -> bool:
    return not M.sfadd(left, M.sfscale(right, -1))


# ---------------------------------------------------------------------------
# Layer 0 and principal-order dependency graph.


SECOND_FRECHET_ORDER = {
    "trace_gamma": (1, 2),
    "Phi1_first": (1, 2),
    "Hodge_first": (1, 2),
    "Phi1_outer": (1, 2),
    "Phi2": (1, 2),
    "Hodge_inner": (1, 2),
    "Hodge_middle": (1, 2),
    "Hodge_outer": (1, 2),
    "density": (1, 2),
    "Krein_pairing": (1, 2),
    "input_lowerer": (1, 2),
    "output_lowerer": (1, 2),
    "outer_pairing": (1, 2),
    "h_theta1_Bhat2": (2, 4),
}


def layer_zero_and_order_checks() -> None:
    type_level("chartwise source-aligned (g,epsilon,varpi) and active-native h=exp(u) are separate columns")
    type_level("B_full=Gamma+q and A_total=Gamma+varpi are repository reparameterizations of source T=varpi-epsilon^-1 d_Gamma epsilon")
    type_level("vary-upstairs-then-observe and restrict-then-vary are not assumed to commute")
    type_level("Shiab is a moving contraction, not a projector")
    type_level("D2(I1 composed with the graph), source I2B, and second-order equations are homonyms")
    type_level("Frobenius-fibre trace reversal, Ricci trace reversal, and Krein residual pairing are distinct")
    type_level("the direct differential-form comparator packages its chosen top pairing; equivalence to the full moving density/Krein/lowerer graph remains open")
    type_level("P1/P2/P3 supply no jet, second derivative, C5 cancellation, C4 coefficient, or kappa selector")

    exact(
        "all fourteen second-Frechet candidates have an explicit first/second order ceiling",
        set(SECOND_FRECHET_ORDER) == set(B1.SECOND_FRECHET_CANDIDATES)
        and len(SECOND_FRECHET_ORDER) == 14,
    )
    exact(
        "the first thirteen isolated E-times-D2 coefficient returns stop below C4",
        all(SECOND_FRECHET_ORDER[name][1] <= 2 for name in B1.SECOND_FRECHET_CANDIDATES[:13]),
    )
    exact(
        "the same first thirteen remain potentially C4-capable in the declared ceiling ledger through a 1+3 cross",
        all(SECOND_FRECHET_ORDER[name][0] + 3 == 4 for name in B1.SECOND_FRECHET_CANDIDATES[:13]),
    )
    exact(
        "the connection-orbit branch is flagged, not discharged, at an order-four curvature ceiling",
        SECOND_FRECHET_ORDER["h_theta1_Bhat2"] == (2, 4),
    )
    reject("promote an algebraic coefficient D2 ceiling of two to C4 by name alone", False)
    reject("freeze all thirteen coefficient JVPs because their isolated D2 returns are lower order", False)


# ---------------------------------------------------------------------------
# C5 gate: sigma_2(Du) and the odd 2+3 Hessian block.


def hodge_null_pair() -> tuple[M.SCliff, M.SCliff]:
    _, _, bridge_u, _ = E.native_inputs()
    c3, c11 = sp.symbols("c3 c11", real=True)
    null_u = M.sclean(
        {
            mask: sp.simplify(value.subs({c3: 1, c11: 1}))
            for mask, value in bridge_u.items()
        }
    )
    return E.exponential_pair(null_u, sp.Integer(0))


def c5_gate_checks() -> tuple[M.SCliff, M.SCliff]:
    eta = sp.symbols("eta0:4", real=True)
    top_b = [R.symbolic_z1_b_form(eta, owner) for owner in range(10)]
    alt = [D.alt_of_t(value) for value in top_b]
    exact(
        "torsion-free LC/Zorro incidence kills sigma2(Du)=R Alt(deltaT_top) for every owner",
        all(not value for value in alt),
    )
    exact(
        "the fixed-total-connection LC/Zorro comparator's unmoved all-base-conormal odd C5 matrix vanishes identically",
        R.all_base_conormal_c5_identity() == 0,
    )
    h, hinv = hodge_null_pair()
    exact(
        "fixed-h finite conjugation preserves that comparator C5 cancellation on the exact Hodge-null fixture",
        R.moved_c5_pairing_comparator(h, hinv),
    )

    hostile = {(0,): M.sblade(1, 2)}
    exact(
        "a non-Levi-Civita grade-two connection plant has a live Alt route",
        bool(D.alt_of_t(hostile)),
    )
    a2, a3 = sp.symbols("a2 a3")
    c5_plant = sp.Matrix([[0, a2 * a3], [-a2 * a3, 0]])
    exact(
        "an asymmetric 2+3 plant detects a live odd fifth-order block",
        c5_plant.rank() == 2 and c5_plant.T == -c5_plant,
    )
    reject("skip the C5 gate merely because the requested swing is named C4", c5_plant.rank() == 0)
    reject("infer sigma2(Du)=0 for arbitrary non-Levi-Civita connection motion", not D.alt_of_t(hostile))
    return h, hinv


# ---------------------------------------------------------------------------
# Active-native C4 evaluation on the complete 35-point quartic lattice.


OWNER_SYMBOLS = sp.symbols("o0:10")
CURVATURE_SYMBOLS = sp.symbols("p0:10")


def eta_tuple(point) -> tuple[F, ...]:
    return tuple(F(int(value)) for value in point)


def test_t_background() -> M.SForm:
    curvature = D.to_sympy_form(P.SPIN_CURVATURE)
    return D.build_source_t(D.shiab(curvature))


def direct_core_matrix(
    bhat: list[M.SForm], source_t: M.SForm
) -> sp.Matrix:
    """Exact 2+2 fixed-total-connection comparator Hessian."""
    tvar = [M.sfscale(value, -1) for value in bhat]
    linear_residual = [
        M.sfscale(
            M.sfadd(M.sfwedge(source_t, value), M.sfwedge(value, source_t)),
            -sp.Rational(1, 6),
        )
        for value in tvar
    ]
    linear_shiab = [D.shiab(value) for value in linear_residual]
    result = sp.zeros(10)
    for i in range(10):
        for j in range(i, 10):
            second_residual = M.sfadd(
                M.sfscale(
                    M.sfadd(M.sfwedge(bhat[i], bhat[j]), M.sfwedge(bhat[j], bhat[i])),
                    sp.Rational(1, 2),
                ),
                M.sfscale(
                    M.sfadd(M.sfwedge(tvar[i], tvar[j]), M.sfwedge(tvar[j], tvar[i])),
                    -sp.Rational(1, 6),
                ),
            )
            value = D.top_scalar(source_t, D.shiab(second_residual))
            value += D.top_scalar(tvar[i], linear_shiab[j])
            value += D.top_scalar(tvar[j], linear_shiab[i])
            result[i, j] = result[j, i] = sp.simplify(value)
    return result


def two_parameter_core_check(
    bhat: list[M.SForm], source_t: M.SForm, expected: sp.Matrix
) -> bool:
    r, s = sp.symbols("r s")
    left, right = 0, 3
    bvar = M.sfadd(M.sfscale(bhat[left], r), M.sfscale(bhat[right], s))
    tvar = M.sfadd(source_t, M.sfscale(bvar, -1))
    residual = M.sfadd(
        M.sfscale(M.sfwedge(bvar, bvar), sp.Rational(1, 2)),
        M.sfscale(M.sfwedge(tvar, tvar), -sp.Rational(1, 6)),
    )
    action = D.top_scalar(tvar, D.shiab(residual))
    direct = sp.diff(action, r, s).subs({r: 0, s: 0})
    return sp.simplify(direct - expected[left, right]) == 0


def moving_cross_matrix(
    eta: tuple[F, ...], btop: list[M.SForm], source_t: M.SForm
) -> tuple[sp.Matrix, sp.Matrix]:
    """Return ordered and action-symmetrized 1+3 moving-Shiab crosses."""
    one = R.xi_form(eta)
    hvars = [R.z1_metric_variation(eta, owner) for owner in P.SYM2]
    hcombo = sum(
        (OWNER_SYMBOLS[index] * hvars[index] for index in range(10)),
        sp.zeros(14),
    )
    curvature = M.sfadd(
        *(
            M.sfscale(M.sfwedge(one, btop[index]), CURVATURE_SYMBOLS[index])
            for index in range(10)
        )
    )
    response = M.sfadd(*M.moving_metric_shiab_parts(curvature, hcombo, None).values())
    value = sp.expand(D.top_scalar(source_t, response))
    ordered = sp.Matrix(
        10,
        10,
        lambda i, j: sp.simplify(
            sp.diff(value, OWNER_SYMBOLS[i], CURVATURE_SYMBOLS[j])
        ),
    )
    return ordered, sp.simplify((ordered + ordered.T) / 2)


def evaluate_c4(
    point, h: M.SCliff, hinv: M.SCliff, source_t: M.SForm
) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    eta = eta_tuple(point)
    btop = [R.principal_b_form(eta, owner, False, True) for owner in range(10)]
    bhat = [E.fconj(hinv, value, h) for value in btop]
    core = direct_core_matrix(bhat, source_t)
    ordered, moving = moving_cross_matrix(eta, btop, source_t)
    mass = R.gram(bhat)
    return core + moving, mass, ordered, core


def reconstruct(values: list[sp.Matrix]) -> list[sp.Matrix]:
    inverse = B1.VANDERMONDE.inv()
    coefficients = [sp.zeros(10) for _ in B1.MONOMIALS]
    for row in range(10):
        for column in range(10):
            recovered = inverse * sp.Matrix([value[row, column] for value in values])
            for index, coefficient in enumerate(recovered):
                coefficients[index][row, column] = sp.simplify(coefficient)
    return coefficients


def evaluate_reconstruction(coefficients: list[sp.Matrix], point) -> sp.Matrix:
    result = sp.zeros(10)
    for coefficient, alpha in zip(coefficients, B1.MONOMIALS):
        result += coefficient * B1.monomial(point, alpha)
    return result.applyfunc(sp.simplify)


def c4_graph_checks(h: M.SCliff, hinv: M.SCliff) -> dict[str, object]:
    source_t = test_t_background()
    action_values: list[sp.Matrix] = []
    mass_values: list[sp.Matrix] = []
    moving_values: list[sp.Matrix] = []
    core_values: list[sp.Matrix] = []
    for index, point in enumerate(B1.POINTS):
        action, mass, ordered, core = evaluate_c4(point, h, hinv, source_t)
        action_values.append(action)
        mass_values.append(mass)
        moving_values.append(sp.simplify((ordered + ordered.T) / 2))
        core_values.append(core)
        print(f"C4_LATTICE: {index + 1}/35", flush=True)

    action_coefficients = reconstruct(action_values)
    mass_coefficients = reconstruct(mass_values)
    moving_coefficients = reconstruct(moving_values)
    core_coefficients = reconstruct(core_values)

    exact(
        "all 35 active-native action coefficient matrices are even-order owner symmetric",
        all(value == value.T for value in action_coefficients),
    )
    exact(
        "the 3+1 moving-Shiab cross is evaluated rather than frozen",
        len(moving_values) == 35,
    )
    moving_nonzero = sum(not is_zero(value) for value in moving_coefficients)
    exact(
        "the selected synthetic test/T background exactly annihilates the evaluated eight-slot moving-Shiab quartic bank",
        moving_nonzero == 0 and all(value == value.T for value in moving_coefficients),
        f"nonzero_monomial_blocks={moving_nonzero}",
    )
    hostile_curvature = {
        (0, 1): M.sblade(2, 3),
        (4, 5): M.sblade(6, 7, 8),
        (2, 10): M.sblade(0, 4, 9, 13),
    }
    hostile_parts = M.moving_metric_shiab_parts(
        hostile_curvature,
        M.B15.H_VARIATIONS[0],
        M.canonical_trace_motion(0),
    )
    exact(
        "an independent hostile curvature/metric fixture makes the raw eight-slot moving-Shiab map nonzero",
        bool(M.flatten_form(M.sfadd(*hostile_parts.values()))),
    )
    core_nonzero = sum(not is_zero(value) for value in core_coefficients)
    mass_nonzero = sum(not is_zero(value) for value in mass_coefficients)
    exact(
        "the quadratic curvature/cubic-distortion graph has a live C4 coefficient bank",
        core_nonzero > 0,
        f"nonzero_monomial_blocks={core_nonzero}",
    )
    exact(
        "the kappa distortion norm has a live C4 coefficient bank",
        mass_nonzero > 0,
        f"nonzero_monomial_blocks={mass_nonzero}",
    )

    heldouts = ((1, -1, 2, 3), (2, 1, -2, 1), (-1, 3, 1, 2))
    heldout_failures = 0
    for point in heldouts:
        action, mass, _, _ = evaluate_c4(point, h, hinv, source_t)
        heldout_failures += int(not is_zero(action - evaluate_reconstruction(action_coefficients, point)))
        heldout_failures += int(not is_zero(mass - evaluate_reconstruction(mass_coefficients, point)))
    exact(
        "the all-35 action and mass reconstructions pass three dense held-out conormals",
        heldout_failures == 0,
        f"failures={heldout_failures}/6",
    )

    eta = eta_tuple((1, 1, 0, 0))
    btop = [R.principal_b_form(eta, owner, False, True) for owner in range(10)]
    bhat = [E.fconj(hinv, value, h) for value in btop]
    exact(
        "a direct two-parameter action derivative matches the independently assembled 2+2 core entry",
        two_parameter_core_check(bhat, source_t, direct_core_matrix(bhat, source_t)),
    )

    a_flat = tuple(
        coefficient[row, column]
        for coefficient in action_coefficients
        for row in range(10)
        for column in range(10)
    )
    m_flat = tuple(
        coefficient[row, column]
        for coefficient in mass_coefficients
        for row in range(10)
        for column in range(10)
    )
    kappa_result = B1.universal_kappa(a_flat, m_flat)
    exact(
        "the fixed-total-connection comparator has no universal kappa across every owner pair and quartic monomial",
        kappa_result == ("NONE", None),
        str(kappa_result),
    )
    exact(
        "the same classifier exposes the ANY zero-bank control",
        B1.universal_kappa((0, 0), (0, 0)) == ("ANY", None),
    )
    exact(
        "the same classifier exposes a UNIQUE proportional-bank control",
        B1.universal_kappa((2, 4), (1, 2)) == ("UNIQUE", sp.Integer(-2)),
    )
    reject("reuse the predecessor five-conormal panel as the complete quartic", len(B1.POINTS) == 5)
    reject("call a fixture-dependent kappa result source-selected", False)

    return {
        "action_coefficients": action_coefficients,
        "mass_coefficients": mass_coefficients,
        "moving_nonzero": moving_nonzero,
        "core_nonzero": core_nonzero,
        "mass_nonzero": mass_nonzero,
        "kappa_result": kappa_result,
    }


# ---------------------------------------------------------------------------
# Owner symmetry and frozen-ray Green checks.


def total_derivative(expr: sp.Expr, rows: list[list[sp.Symbol]]) -> sp.Expr:
    return sp.expand(
        sum(
            sp.diff(expr, row[index]) * row[index + 1]
            for row in rows
            for index in range(len(row) - 1)
        )
    )


def helmholtz_green_checks(result: dict[str, object]) -> None:
    coefficients: list[sp.Matrix] = result["action_coefficients"]  # type: ignore[assignment]
    exact(
        "the assembled even-order owner coefficient bank is symmetric by construction",
        all(matrix == matrix.T for matrix in coefficients),
    )
    chosen = next(matrix for matrix in coefficients if not is_zero(matrix))[:3, :3]
    u = [list(sp.symbols(f"u{owner}_0:6")) for owner in range(3)]
    v = [list(sp.symbols(f"v{owner}_0:6")) for owner in range(3)]
    u0 = sp.Matrix([row[0] for row in u])
    v0 = sp.Matrix([row[0] for row in v])
    u1 = sp.Matrix([row[1] for row in u])
    v1 = sp.Matrix([row[1] for row in v])
    u2 = sp.Matrix([row[2] for row in u])
    v2 = sp.Matrix([row[2] for row in v])
    u3 = sp.Matrix([row[3] for row in u])
    v3 = sp.Matrix([row[3] for row in v])
    u4 = sp.Matrix([row[4] for row in u])
    v4 = sp.Matrix([row[4] for row in v])
    concomitant = (
        (u0.T * chosen * v3)[0]
        - (u1.T * chosen * v2)[0]
        + (u2.T * chosen * v1)[0]
        - (u3.T * chosen * v0)[0]
    )
    bulk = (u0.T * chosen * v4)[0] - (v0.T * chosen * u4)[0]
    exact(
        "the one-dimensional frozen-principal Green identity closes on a live three-owner block",
        sp.expand(bulk - total_derivative(concomitant, u + v)) == 0
        and concomitant != 0,
    )
    asymmetric = chosen.copy()
    asymmetric[0, 1] += 1
    reject("accept an asymmetric even-order owner coefficient as Helmholtz", asymmetric == asymmetric.T)
    reject("use the Green concomitant as a bulk C4 cancellation", concomitant == 0)


def scope_checks(result: dict[str, object]) -> None:
    type_level("source-coordinate C5/C4 remains blocked by the missing q/Gamma split, epsilon-dependent Shiab, and epsilon-to-h/carrier bridge")
    type_level("the active result is a partial fixed-total-connection comparator on B2C15P/R reconstruction geometry, not Weinstein's unique published formula")
    type_level("the selected test/T background is synthetic and cannot select a physical kappa or vacuum")
    type_level("h/theta1/Bhat2 second-Frechet return, a co-moving frame, and five non-Shiab 1+3 slots remain open C4 debt")
    type_level("same-pipeline liveness of the top-scalar-contracted moving-Shiab quartic bank remains open despite the live raw eight-slot map")
    type_level("C3/C2 second-Frechet debt is retained rather than declared zero")
    type_level("formal C4 and Green agreement do not construct a characteristic, hyperbolic/Krein domain, BV quotient, observation equation, or Standard-Model/GR recovery")
    type_level("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE and TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    reject("identify source epsilon with repository h from matching covariance grammar alone", False)
    reject("promote the partial comparator bank to the complete source-coordinate or physical C4", False)
    reject("spend P1/P2/P3 to bridge the missing Shiab or observation map", False)


def main() -> int:
    print("PW2F-R2B2A SECOND-FRECHET PRINCIPAL-ORDER / MOVING-C4 GRAPH")
    layer_zero_and_order_checks()
    h, hinv = c5_gate_checks()
    result = c4_graph_checks(h, hinv)
    helmholtz_green_checks(result)
    scope_checks(result)
    total = EXACT + TYPE + PLANTED
    print(
        "RESULT: fixed-total comparator C5=0; partial_C4_core_blocks="
        f"{result['core_nonzero']}; moving_blocks={result['moving_nonzero']}; "
        f"mass_blocks={result['mass_nonzero']}; kappa={result['kappa_result']}",
        flush=True,
    )
    print(f"SUMMARY: {EXACT} exact + {TYPE} type + {PLANTED} planted = {total}; failures={len(FAILURES)}")
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print("VERDICT: PARTIAL FIXED-TOTAL-CONNECTION C4 COMPARATOR PASSES; COMPLETE SOURCE-COORDINATE C5/C4 REMAINS BLOCKED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
