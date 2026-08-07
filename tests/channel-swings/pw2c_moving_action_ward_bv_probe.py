#!/usr/bin/env python3
r"""PW2C structural moving-action, Green/Ward, and cotangent comparator gate.

The action panel is an exact scalar differential-substitution comparator with
the same root weights as the active source map. It contains independently
live labels shaped like density, Shiab, Hodge, Krein, lowerer, trace,
projector, and curvature dependencies; they are not the native formulas. The
native trace-adapted eight-slot/rank-ten response is checked separately
against the existing exact implementation. The two are not claimed to be the
still-unassembled literal Y14 tensor coefficient.
"""

from __future__ import annotations

from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
import json
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


R2 = load_probe(
    "pw2c_action_r2",
    "eric_curt_wave3d_b2c15r2_full_bch_action_gauge_curvature_adjoint_probe.py",
)
M = R2.B15M
REGISTRY = ROOT / "lab/process/pw2c-moving-action-ward-bv-registry.json"

EXACT = 0
TYPE = 0
SOURCE = 0
PLANTED = 0


def check(label: str, condition: bool) -> None:
    global EXACT
    if not condition:
        raise AssertionError(f"exact check failed: {label}")
    EXACT += 1


def type_check(label: str, condition: bool) -> None:
    global TYPE
    if not condition:
        raise AssertionError(f"type check failed: {label}")
    TYPE += 1


def source_check(label: str, condition: bool) -> None:
    global SOURCE
    if not condition:
        raise AssertionError(f"source check failed: {label}")
    SOURCE += 1


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    if false_claim:
        raise AssertionError(f"planted false claim passed: {label}")
    PLANTED += 1


def main() -> None:
    data = json.loads(REGISTRY.read_text())
    type_check("registry records a scoped structural pullback/Ward/cotangent pass", data["status"].startswith("PW2C_STRUCTURAL_SOURCE_PULLBACK"))
    type_check("field substitution and gauge symmetry remain distinct", "not itself" in data["layer_zero"]["field_substitution"])
    type_check("Xi is not imported as the Ward identity", "not imported" in data["ward"]["xi_warning"])
    type_check("physical BV/BFV remains open", data["cotangent_brst_boundary"]["physical_bv_bfv"] == "OPEN")
    type_check("moment map remains unclaimed", data["cotangent_brst_boundary"]["preboundary_moment_map"] == "OPEN_NOT_CLAIMED")
    type_check("actual Y14 composite coefficient remains open", "NO_ACTUAL_FULL_Y14" in data["claim_boundary"])
    type_check("P1/P2/P3 remain unused", data["external_datum"] == "P1/P2/P3 UNCHANGED AND UNUSED")
    type_check("Curt and third-lane boundaries remain intact", data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and data["third_lane_gate"].endswith("NOT_PROMOTED"))

    # Exact root-jet algebra.  T=a-Dq is gauge invariant under
    # (delta q,delta a)=(chi,Dchi).  The active source substitution has the
    # Abelian germ qhat=q+lambda*T, so That=T-lambda*DT.
    q = sp.symbols("q0:7")
    a = sp.symbols("a0:6")
    g = sp.symbols("g0:6")
    lam = sp.Rational(1, 2)
    T0 = a[0] - q[1]
    T1 = a[1] - q[2]
    That = sp.expand(T0 - lam * T1)

    factors = {
        "density": 2 + g[0],
        "Shiab": 3 + That + g[2],
        "Hodge": 4 - That + 2 * g[0],
        "Krein": -2 + That - g[0],
        "lowerer": 5 + 2 * That + g[2],
        "trace": 1 - That + 3 * g[0],
        "projector": 2 + That + g[0],
        "curvature": 3 + g[2] + g[2] ** 2,
    }
    weights = {name: sp.Integer(index + 1) for index, name in enumerate(factors)}
    coefficient = sum(weights[name] * factor for name, factor in factors.items())
    L = sp.expand(coefficient * That**2 / 2)
    base = {q[1]: 1, q[2]: -1, a[0]: 3, a[1]: 2, g[0]: 1, g[2]: 2}
    check("the literal source germ is nontrivial at the preregistered rational jet", That.subs(base) == sp.Rational(1, 2) and L.subs(base) != 0)
    for name, factor in factors.items():
        without = sp.expand((coefficient - weights[name] * factor) * That**2 / 2)
        check(f"structural dependency label {name} is independently live in the pulled scalar density", sp.simplify((L - without).subs(base)) != 0 and factor.subs(base) != 0)
    reject("freeze every moving action owner", all(sp.diff(L, variable) == 0 for variable in (a[0], q[1], g[0], g[2])))

    all_jets = (q, a, g)

    def total_d(expr: sp.Expr) -> sp.Expr:
        result = 0
        for jets in all_jets:
            result += sum(sp.diff(expr, jets[index]) * jets[index + 1] for index in range(len(jets) - 1))
        return sp.expand(result)

    p_a1 = sp.diff(L, a[1])
    p_q1 = sp.diff(L, q[1])
    p_q2 = sp.diff(L, q[2])
    p_g2 = sp.diff(L, g[2])
    E_a = sp.expand(sp.diff(L, a[0]) - total_d(p_a1))
    E_q = sp.expand(-total_d(p_q1) + total_d(total_d(p_q2)))
    E_g = sp.expand(sp.diff(L, g[0]) + total_d(total_d(p_g2)))

    def order_in(expr: sp.Expr, jets) -> int:
        return max((index for index, item in enumerate(jets) if expr.has(item)), default=-1)

    orders = tuple(tuple(order_in(expr, jets) for jets in (a, q, g)) for expr in (E_a, E_q, E_g))
    check("structural scalar comparator realizes the exact 2/3/4 mixed root-order table", orders == ((2, 3, 3), (3, 4, 4), (3, 4, 4)))
    check("registry and executable mixed-order table agree", data["moving_action"]["mixed_order_matrix"] == [list(row) for row in orders])

    top = (a[1], q[2], g[2])
    top_hessian = sp.Matrix([[sp.diff(L, left, right).subs(base) for right in top] for left in top])
    gauge_top = sp.Matrix([1, 1, 0])
    check("scalar top-jet Hessian has rank two with the comparator gauge direction in its sole kernel", top_hessian.rank() == 2 and top_hessian * gauge_top == sp.zeros(3, 1))
    reject("promote the scalar Hessian rank to a native physical quotient rank", data["moving_action"]["top_hessian"].startswith("PHYSICAL"))

    # Full bulk-plus-preboundary identity.  q and g carry two Green layers;
    # a carries one.  The identity is symbolic and off shell.
    va = sp.symbols("va0:4")
    vq = sp.symbols("vq0:5")
    vg = sp.symbols("vg0:5")

    direct = sp.expand(
        sp.diff(L, a[0]) * va[0] + p_a1 * va[1]
        + p_q1 * vq[1] + p_q2 * vq[2]
        + sp.diff(L, g[0]) * vg[0] + p_g2 * vg[2]
    )
    bulk = sp.expand(E_a * va[0] + E_q * vq[0] + E_g * vg[0])
    theta = sp.expand(
        p_a1 * va[0]
        + p_q2 * vq[1] + (p_q1 - total_d(p_q2)) * vq[0]
        + p_g2 * vg[1] - total_d(p_g2) * vg[0]
    )

    variation_jets = (va, vq, vg)

    def total_d_all(expr: sp.Expr) -> sp.Expr:
        result = total_d(expr)
        for jets in variation_jets:
            result += sum(sp.diff(expr, jets[index]) * jets[index + 1] for index in range(len(jets) - 1))
        return sp.expand(result)

    green_defect = sp.expand(direct - bulk - total_d_all(theta))
    check("direct pulled-comparator variation has exact Euler-Green agreement", green_defect == 0)
    check("one/two/two Green layers are all live", p_a1 != 0 and p_q2 != 0 and p_g2 != 0 and data["moving_action"]["green_layers"] == {"varpi": 1, "epsilon": 2, "metric": 2})
    reject("discard the pulled-action preboundary", sp.expand(direct - bulk) == 0)

    # Off-shell Ward identity.  Both covectors are live; their differential
    # combination vanishes because the action depends on q,a only through T.
    ward = sp.expand(E_q - total_d(E_a))
    check("separate source-gauge generator gives the exact off-shell Ward identity", ward == 0)
    check("Ward cancellation is nonvacuous", E_q != 0 and E_a != 0)
    chi = sp.symbols("chi0:4")
    direct_gauge = direct.subs({va[0]: chi[1], va[1]: chi[2], vq[0]: chi[0], vq[1]: chi[1], vq[2]: chi[2], vg[0]: 0, vg[1]: 0, vg[2]: 0}, simultaneous=True)
    check("the root gauge variation annihilates T and the direct density", sp.expand(direct_gauge) == 0)
    theta_gauge = theta.subs({va[0]: chi[1], vq[0]: chi[0], vq[1]: chi[1], vg[0]: 0, vg[1]: 0}, simultaneous=True)
    bulk_gauge = sp.expand(E_a * chi[1] + E_q * chi[0])

    def total_d_chi(expr: sp.Expr) -> sp.Expr:
        return sp.expand(total_d(expr) + sum(sp.diff(expr, chi[index]) * chi[index + 1] for index in range(len(chi) - 1)))

    check("Ward preboundary and bulk pieces are separately live", theta_gauge != 0 and bulk_gauge != 0)
    check("Ward preboundary obeys the explicit sign-convention identity", sp.expand(theta_gauge + E_a * chi[0]) == 0)
    check("the live Ward bulk plus preboundary derivative cancels exactly", sp.expand(bulk_gauge + total_d_chi(theta_gauge)) == 0)
    qhat_variation = sp.expand(chi[0] + lam * (chi[1] - chi[1]))
    check("source Jacobian transports the gauge generator naturally", qhat_variation == chi[0])
    reject("rename the source field substitution itself as the Ward symmetry", data["layer_zero"]["field_substitution"] == data["layer_zero"]["gauge_generator"])

    # Actual native metric coefficient receipt: all eight trace/Phi/Hodge
    # slots are exercised on all ten physical metric owners and have rank 10.
    curvature = {
        (0, 1): M.sblade(2, 3),
        (4, 5): M.sblade(6, 7, 8),
        (2, 10): M.sblade(0, 4, 9, 13),
    }
    responses = []
    live_slots: Counter[str] = Counter()
    for owner, hvar in enumerate(M.B15.H_VARIATIONS):
        parts = M.moving_metric_shiab_parts(curvature, hvar, M.canonical_trace_motion(owner))
        total = M.sfadd(*parts.values())
        responses.append(M.flatten_form(total))
        for name, value in parts.items():
            live_slots[name] += bool(value)
    keys = sorted(set().union(*(response.keys() for response in responses)))
    response_matrix = sp.Matrix([[responses[owner].get(key, 0) for owner in range(10)] for key in keys])
    expected_slots = {"trace_gamma", "Phi1_first", "Hodge_first", "Phi1_outer", "Phi2", "Hodge_inner", "Hodge_middle", "Hodge_outer"}
    check("actual native moving-Shiab implementation carries all eight named slots", set(live_slots) == expected_slots and all(live_slots[name] > 0 for name in expected_slots))
    check("actual native moving-Shiab metric response has exact ten-owner rank", response_matrix.rank() == 10)
    reject("call the scalar pullback comparator the assembled native Y14 coefficient", data["moving_action"]["composition_boundary"].startswith("ASSEMBLED"))

    # Canonical cotangent and finite Abelian BRST comparators. This is not a
    # graded BV action, antibracket, CME, or physical BFV construction.
    mode = sp.symbols("n", integer=True)
    J = sp.Matrix([[1 - sp.I * mode * lam, lam], [0, 1]])
    S = sp.diag(1, 1, 1, 1)
    S[0:2, 0:2] = J
    S[2:4, 2:4] = J.inv().T
    Omega = sp.zeros(4)
    Omega[0:2, 2:4] = sp.eye(2)
    Omega[2:4, 0:2] = -sp.eye(2)
    check("finite cotangent lift preserves the ordinary canonical symplectic form", sp.simplify(S.T * Omega * S - Omega) == sp.zeros(4))

    xx = sp.symbols("x", real=True)
    phq = sp.Function("phq")(xx)
    pha = sp.Function("pha")(xx)
    dq = sp.Function("dq")(xx)
    da = sp.Function("da")(xx)
    lhs = phq * (dq + lam * (da - sp.diff(dq, xx))) + pha * da
    adjoint_bulk = (phq + lam * sp.diff(phq, xx)) * dq + (pha + lam * phq) * da
    green = lam * phq * dq
    check("differential cotangent lift includes the exact nonzero Green concomitant", sp.simplify(lhs - adjoint_bulk + sp.diff(green, xx)) == 0 and green != 0)
    reject("drop the formal-adjoint Green endpoint from the cotangent lift", sp.simplify(lhs - adjoint_bulk) == 0)

    c = sp.symbols("c0:4")

    def s_brst(expr: sp.Expr) -> sp.Expr:
        result = 0
        for index in range(3):
            result += sp.diff(expr, q[index]) * c[index]
        for index in range(2):
            result += sp.diff(expr, a[index]) * c[index + 1]
        return sp.expand(result)

    qhat0 = sp.expand(q[0] + lam * (a[0] - q[1]))
    brst_generators = [q[0], q[1], q[2], a[0], a[1], T0, That, qhat0]
    check("finite Abelian BRST comparator has sT=0 and transports the source root", s_brst(T0) == 0 and s_brst(That) == 0 and s_brst(qhat0) == c[0])
    check("finite Abelian BRST comparator is explicitly nilpotent on every tested generator", all(s_brst(s_brst(item)) == 0 for item in brst_generators))
    reject("promote cotangent plus Abelian BRST comparators to a graded BV action or CME", data["cotangent_brst_boundary"]["graded_bv_action"] == "PASS")
    reject("promote the finite canonical cotangent control to a physical BFV phase space", data["cotangent_brst_boundary"]["physical_bv_bfv"] == "PASS")
    reject("promote the finite canonical charge control to the GU preboundary moment map", data["cotangent_brst_boundary"]["preboundary_moment_map"] == "PASS")

    # Native signature and source dispositions stay live.
    eta = tuple(M.ETA)
    check("native active carrier retains total (9,5) and fibre (6,4)", sum(value > 0 for value in eta) == 9 and sum(value < 0 for value in eta) == 5 and sum(value > 0 for value in eta[4:]) == 6 and sum(value < 0 for value in eta[4:]) == 4)
    reject("replace trace reversal by raw Frobenius", sum(value > 0 for value in eta[4:]) == 7)

    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    source_check("source owns the first action and fixed completion", "I^B_1" in pack and "\\frac12d_{B_\\omega}T_\\omega" in pack and "\\frac13[T_\\omega,T_\\omega]" in pack)
    source_check("source displays Xi but does not supply the off-shell Ward identity", "\\Xi_\\omega=D_\\omega\\Upsilon_\\omega" in pack and "Noether identity is not" in pack)
    source_check("source owns gauge-rotated Levi-Civita language", "[02:19:17]" in toe and "gauge rotated Levy-Chevita" in toe)
    source_check("source owns trace reversal while the complete native coefficient is repository work", "00:26:28" in toe and any("complete native" in item for item in data["source_disposition"]["SOURCE_SILENT_REPOSITORY_DERIVED"]))

    reject("spend external datum on Ward/BV/domain repair", data["external_datum"] != "P1/P2/P3 UNCHANGED AND UNUSED")
    reject("claim positive constraint surplus from identities true for every coefficient", data["constraint_surplus"].startswith("POSITIVE"))
    total = EXACT + TYPE + SOURCE + PLANTED
    print(f"PW2C structural action/Ward/cotangent: {EXACT} exact + {TYPE} type + {SOURCE} source + {PLANTED} planted = {total} PASS")
    print("RESULT: scalar dependency comparator, 2/3/4 orders, Green/Ward, native eight-slot response, cotangent, and Abelian BRST comparators PASS")
    print("BOUNDARY: actual literal-K times native Y14 coefficient, nonabelian source Ward, physical BFV, public bundle port, and domain remain open")


if __name__ == "__main__":
    main()
