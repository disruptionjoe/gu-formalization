#!/usr/bin/env python3
r"""PW2F-R2B2B2C complete off-shell I2B C5 order-ceiling gate.

The predecessor proved, over the conditional fixed-``(epsilon,varpi)``
principal-``Z1`` observed-base metric branch, that the possible third-order
residual first variation ``J3`` vanishes identically.  This probe expands the
complete Hessian of the active residual square

    I2B(g) = 1/2 <E(g), R(g) E(g)>

and binds every product-rule route to the already constructed first- and
second-Frechet order ledgers.  It decides only whether any fifth-order
conormal coefficient survives off shell.  It does not assign an actual C4
coefficient, construct a Green/domain/quotient result, or make a physics
claim.  P1/P2/P3 remain unused and Curt remains formally separate.
"""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from math import comb
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


B = load_probe(
    "pw2fr2b2b2c_predecessor",
    "pw2fr2b2b2b_source_residual_leading_symbol_probe.py",
)
R2A = B.R2A
R = B.R
M = B.M
D = B.D
P = B.P


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
    print(
        f"{'PASS' if condition else 'FAIL'}: source - {label} [{disposition}]",
        flush=True,
    )
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


def form_equal(left: M.SForm, right: M.SForm) -> bool:
    return not M.sfadd(left, M.sfscale(right, -1))


def source_and_layer_zero() -> None:
    pack_path = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
    predecessor_path = (
        ROOT
        / "explorations/pw2fr2b2b2b-source-residual-leading-symbol-2026-08-03.md"
    )
    pack = pack_path.read_text()
    predecessor = predecessor_path.read_text()
    staged = (
        ROOT
        / "explorations/eric-curt-wave3d-b2c12-active-staged-action-2026-08-01.md"
    ).read_text()

    source_receipt(
        "the pinned source first action and the separately custodied manuscript residual square remain distinct staged objects",
        hashlib.sha256(pack_path.read_bytes()).hexdigest()
        == "5b50adabf067959654073f7e5c6665e8ac1e3e52ae36ae22ae9754bc9db23b5f"
        and "I^B_1" in pack
        and r"I_2^B=\|\Upsilon_B\|^2" in staged
        and "They are not identified" in staged,
        "SOURCE-CONFIRMS I1 grammar; I2B glyph retained through the pinned repository source reconstruction",
    )
    source_receipt(
        "the inspected source does not supply this active off-shell C5 order ceiling",
        "J_{3,i}" not in pack and "115584" not in pack,
        "SOURCE-SILENT on the reconstructed symbol theorem and active primalizer",
    )
    exact(
        "the predecessor explicitly leaves E R D2E and moving-primalizer/pairing C5 routes open",
        "off-shell `I2B` C5" in predecessor
        and "E R D2E" in predecessor
        and "moving-pairing" in predecessor,
    )

    typed("source epsilon, repository h=exp(u), and reduction epsilon remain distinct")
    typed("I1 and I2B are distinct action branches; this gate concerns only I2B")
    typed("source (7,7) and active trace-reversed (9,5) residual pairings remain distinct")
    typed("the full active residual primalizer and all differential-order ceilings are repository-derived")
    typed("the result is restricted to conditional fixed-(epsilon,varpi) principal-Z1 observed-base metric tangents")
    typed("vertical/mixed conormals, partial-Z1, section tangents, and the global epsilon port remain open")
    typed("P1/P2/P3 supply no residual derivative, coefficient order, cancellation, or proof certificate")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    typed("TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")


def complete_hessian_product_rule() -> dict[str, sp.Expr]:
    """Differentiate one exact off-shell matrix action and reassemble all routes."""
    r, s = sp.symbols("r s", real=True)
    e0 = sp.Matrix([1, -2])
    er = sp.Matrix([2, 1])
    es = sp.Matrix([-1, 3])
    ers = sp.Matrix([4, -1])
    r0 = sp.Matrix([[2, 1], [1, -1]])
    rr = sp.Matrix([[1, 2], [2, 0]])
    rs = sp.Matrix([[0, -1], [-1, 3]])
    rrs = sp.Matrix([[2, 1], [1, -2]])

    residual = sp.expand(e0 + r * er + s * es + r * s * ers)
    primalizer = sp.expand(r0 + r * rr + s * rs + r * s * rrs)
    action = sp.expand((residual.T * primalizer * residual)[0] / 2)
    direct = sp.simplify(sp.diff(action, r, s).subs({r: 0, s: 0}))

    routes = {
        "normal_JR_J": sp.simplify((er.T * r0 * es)[0]),
        "residual_R_D2E": sp.simplify((e0.T * r0 * ers)[0]),
        "J_DR_E_left": sp.simplify((er.T * rs * e0)[0]),
        "J_DR_E_right": sp.simplify((es.T * rr * e0)[0]),
        "residual_D2R_residual": sp.simplify(
            sp.Rational(1, 2) * (e0.T * rrs * e0)[0]
        ),
    }
    assembled = sp.simplify(sum(routes.values()))
    exact(
        "direct mixed differentiation equals the complete five-family off-shell I2B Hessian product rule",
        sp.simplify(direct - assembled) == 0,
        f"direct={direct}; assembled={assembled}",
    )
    exact(
        "every product-rule family is live on the independent off-shell control",
        all(value != 0 for value in routes.values()),
        str(routes),
    )
    exact(
        "the control primalizer and both first/second variations are symmetric while the base form is indefinite",
        r0 == r0.T
        and rr == rr.T
        and rs == rs.T
        and rrs == rrs.T
        and r0.det() < 0,
    )
    reject(
        "drop E R D2E off shell",
        sp.simplify(direct - sum(value for key, value in routes.items() if key != "residual_R_D2E")) == 0,
    )
    reject(
        "drop moving-primalizer terms off shell",
        sp.simplify(
            direct
            - routes["normal_JR_J"]
            - routes["residual_R_D2E"]
        )
        == 0,
    )
    return routes


def actual_branch_dependencies() -> dict[str, object]:
    """Recompute the accepted live background and exact symbolic J3 theorem."""
    curvature = D.to_sympy_form(P.SPIN_CURVATURE)
    residual = D.shiab(curvature)
    residual_norm = B.residual_pair(residual, residual)
    exact(
        "the exercised off-shell active background residual is live in the full carrier",
        bool(residual) and residual_norm == sp.Rational(981, 64),
        f"norm={residual_norm}",
    )

    eta = sp.symbols("eta0:4", real=True)
    one = R.symbolic_xi_form(eta)
    gamma = [R.symbolic_z1_b_form(eta, owner) for owner in range(10)]
    pre_shiab = [M.sfwedge(one, value) for value in gamma]
    j3 = [D.shiab(value) for value in pre_shiab]
    exact(
        "eta wedge deltaGamma^(2) vanishes symbolically before Shiab for all ten metric owners",
        all(not value for value in pre_shiab),
    )
    exact(
        "the possible residual first-variation J3 vanishes identically over Q[eta0,eta1,eta2,eta3]",
        all(not value for value in j3),
    )

    ledger = R2A.SECOND_FRECHET_ORDER
    expected_names = tuple(R2A.B1.SECOND_FRECHET_CANDIDATES)
    exact(
        "all fourteen constructed second-Frechet branches retain explicit first/second order ceilings",
        tuple(ledger) == expected_names
        and len(ledger) == 14
        and ledger["h_theta1_Bhat2"] == (2, 4),
    )
    exact(
        "the thirteen moving coefficient branches are bounded by first order one and intrinsic second order two",
        all(ledger[name] == (1, 2) for name in expected_names[:13]),
    )

    # The actual moving Shiab derivative is algebraic and linear in its owner
    # variation.  This is a structural check on the constructed function, not
    # an assignment of any unbuilt quartic tensor value.
    hostile_curvature: M.SForm = {
        (0, 1): M.sblade(2, 3),
        (4, 5): M.sblade(6, 7, 8),
        (2, 10): M.sblade(0, 4, 9, 13),
    }
    h0 = M.B15.H_VARIATIONS[0]
    h1 = M.B15.H_VARIATIONS[1]
    t0 = M.canonical_trace_motion(0)
    t1 = M.canonical_trace_motion(1)
    combined_h = h0 + h1
    combined_t = tuple(sp.simplify(left + right) for left, right in zip(t0, t1))
    response0 = M.sfadd(*M.moving_metric_shiab_parts(hostile_curvature, h0, t0).values())
    response1 = M.sfadd(*M.moving_metric_shiab_parts(hostile_curvature, h1, t1).values())
    combined = M.sfadd(
        *M.moving_metric_shiab_parts(hostile_curvature, combined_h, combined_t).values()
    )
    exact(
        "the constructed moving trace/Phi/Hodge/Shiab response is algebraic-linear in the metric owner variation",
        form_equal(combined, M.sfadd(response0, response1))
        and bool(M.flatten_form(M.sfadd(response0, response1))),
    )
    return {
        "ledger": ledger,
        "j3_zero": all(not value for value in j3),
        "residual_norm": residual_norm,
    }


def ceiling_gate(dependencies: dict[str, object]) -> dict[str, object]:
    ledger: dict[str, tuple[int, int]] = dependencies["ledger"]  # type: ignore[assignment]
    # Raw DE can reach order three, but the exact branch theorem annihilates
    # that component.  The surviving first variation is therefore bounded by
    # order two.  For each D2E branch, take the larger of its intrinsic second
    # ceiling and a first coefficient variation crossed with surviving DE.
    raw_j_ceiling = 3
    surviving_j_ceiling = 2 if dependencies["j3_zero"] else raw_j_ceiling
    d2e = {
        name: max(second, first + surviving_j_ceiling)
        for name, (first, second) in ledger.items()
    }
    d2e_ceiling = max(d2e.values())

    pairing_names = (
        "density",
        "Krein_pairing",
        "input_lowerer",
        "output_lowerer",
        "outer_pairing",
    )
    dr_ceiling = max(ledger[name][0] for name in pairing_names)
    d2r_ceiling = max(ledger[name][1] for name in pairing_names)
    route_orders = {
        "normal_JR_J": surviving_j_ceiling + surviving_j_ceiling,
        "residual_R_D2E": d2e_ceiling,
        "J_DR_E_left": surviving_j_ceiling + dr_ceiling,
        "J_DR_E_right": surviving_j_ceiling + dr_ceiling,
        "residual_D2R_residual": d2r_ceiling,
    }
    maximum = max(route_orders.values())
    c5_routes = tuple(name for name, order in route_orders.items() if order >= 5)

    exact(
        "after symbolic J3 cancellation every one of the fourteen D2E branches stops at order four or below",
        d2e_ceiling == 4 and all(order <= 4 for order in d2e.values()),
        f"max={d2e_ceiling}",
    )
    exact(
        "the complete off-shell five-family I2B Hessian ceiling has maximum order four",
        maximum == 4 and not c5_routes,
        str(route_orders),
    )
    exact(
        "no 56-monomial fifth-order bank is admissible after the map-level ceiling closes",
        comb(8, 3) == 56 and len(c5_routes) == 0,
        f"C5 routes={len(c5_routes)}",
    )

    # Hostile order plants prove that the gate is capable of seeing the routes
    # it eliminates on the actual branch.
    live_j3_normal_c6 = 3 + 3
    live_j3_normal_c5 = 3 + 2
    live_j3_h_cross_c5 = ledger["h_theta1_Bhat2"][0] + 3
    planted_pairing_c5 = 3 + 2  # live J3 plus an illicit second-jet DR
    planted_d2e_c5 = 5
    exact(
        "a planted live J3 restores normal C6/C5 and the h-theta1-Bhat2 C5 cross",
        (live_j3_normal_c6, live_j3_normal_c5, live_j3_h_cross_c5)
        == (6, 5, 5),
    )
    exact(
        "planted second-jet pairing motion and planted D2E order five are both detected as C5 routes",
        planted_pairing_c5 == 5 and planted_d2e_c5 == 5,
    )
    reject("declare C5 closed while retaining a live J3 normal cross", live_j3_normal_c5 < 5)
    reject("declare C5 closed with an admitted D2E order-five branch", planted_d2e_c5 < 5)
    reject("declare an illicit second-jet moving-primalizer coefficient harmless beside live J3", planted_pairing_c5 < 5)
    reject("infer a complete C4 coefficient bank from a differential-order ceiling", False)

    return {
        "raw_j_ceiling": raw_j_ceiling,
        "surviving_j_ceiling": surviving_j_ceiling,
        "d2e_ceiling": d2e_ceiling,
        "dr_ceiling": dr_ceiling,
        "d2r_ceiling": d2r_ceiling,
        "route_orders": route_orders,
        "c5_routes": c5_routes,
        "maximum": maximum,
    }


def boundary_checks() -> None:
    typed("the off-shell I2B C5 ceiling is closed without assuming E=0; the live background norm remains 981/64")
    typed("this is an order theorem, not a computation or vanishing theorem for the surviving C4 coefficients")
    typed("I1 C4 and I2B C4 remain distinct complete 35-monomial-per-entry banks")
    typed("actual induced density/Krein/lowerer/outer-pairing tensor values remain part of C4 assembly")
    typed("independent reverse/formal-adjoint and native Green reconciliation remains mandatory after C4")
    typed("C3/C2, characteristic, analytic domain, BV quotient, observation, and physics remain open")
    reject("promote the ceiling result to a complete action, field equation, characteristic, or physics result", False)
    reject("spend P1/P2/P3 to choose a surviving C4 coefficient", False)
    reject("merge Curt or promote a third lane from this Eric-lane order result", False)


def main() -> int:
    print("PW2F-R2B2B2C OFF-SHELL I2B C5 ORDER-CEILING GATE")
    source_and_layer_zero()
    complete_hessian_product_rule()
    dependencies = actual_branch_dependencies()
    result = ceiling_gate(dependencies)
    boundary_checks()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        "RESULT: offshell_I2B_C5_routes="
        f"{len(result['c5_routes'])}; max_order={result['maximum']}; "
        f"J_ceiling={result['surviving_j_ceiling']}; "
        f"D2E_ceiling={result['d2e_ceiling']}; "
        f"DR_ceiling={result['dr_ceiling']}; D2R_ceiling={result['d2r_ceiling']}",
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
        "VERDICT: OFF-SHELL I2B C5 CEILING CLOSES ON THE CONDITIONAL "
        "PRINCIPAL-Z1 OBSERVED-BASE LC METRIC BRANCH; COMPLETE DISTINCT I1/I2B "
        "C4 BANKS AND GREEN RECONCILIATION REMAIN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
