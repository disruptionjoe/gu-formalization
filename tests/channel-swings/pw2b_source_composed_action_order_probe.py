#!/usr/bin/env python3
"""PW2B exact source-orbit transgression, Euler-order, and Green gate.

The compatible pointwise orbit jet is not an arbitrary
(B,T)->(B+K,T-K) displacement: the total connection stays fixed and the moved
reference curvature is conjugate to the old one. Consequently dK is derived
at this jet and must not be counted as an independent owner. The probe does
not construct the literal K=h(T)^-1 D_B h(T), moving Shiab coefficient, atlas,
or domain.
"""

from __future__ import annotations

from fractions import Fraction as F
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
G2 = runpy.run_path(str(ROOT / "tests/channel-swings/g2_native_variational_shiab_probe.py"))
REGISTRY = ROOT / "lab/process/pw2b-source-composed-action-order-registry.json"

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


def sym_add(left, right):
    return sp.simplify(left + right)


def sym_scale(value, coefficient):
    return sp.simplify(coefficient * value)


def sym_comm(left, right):
    return sp.simplify(left * right - right * left)


def s1_add(left, right):
    return tuple(sym_add(a, b) for a, b in zip(left, right))


def s1_scale(value, coefficient):
    return tuple(sym_scale(a, coefficient) for a in value)


def s2_add(left, right):
    return tuple(sym_add(a, b) for a, b in zip(left, right))


def s2_scale(value, coefficient):
    return tuple(sym_scale(a, coefficient) for a in value)


def sq(left, right):
    return (
        sp.simplify((sym_comm(left[0], right[1]) - sym_comm(left[1], right[0])) / 2),
        sp.simplify((sym_comm(left[0], right[2]) - sym_comm(left[2], right[0])) / 2),
        sp.simplify((sym_comm(left[1], right[2]) - sym_comm(left[2], right[1])) / 2),
    )


def scov(connection, value, exterior):
    return (
        sp.simplify(exterior[0] + sym_comm(connection[0], value[1]) - sym_comm(connection[1], value[0])),
        sp.simplify(exterior[1] + sym_comm(connection[0], value[2]) - sym_comm(connection[2], value[0])),
        sp.simplify(exterior[2] + sym_comm(connection[1], value[2]) - sym_comm(connection[2], value[1])),
    )


def scurvature(connection, exterior):
    return s2_add(exterior, sq(connection, connection))


def spair(one, two):
    return sp.expand(sp.trace(one[0] * two[2] - one[1] * two[1] + one[2] * two[0]))


def sinner(one, two):
    return sp.expand(sum(sp.trace(a * b) for a, b in zip(one, two)))


def saction(connection, d_connection, distortion, d_distortion, kappa=sp.Integer(2)):
    source_c = s2_add(
        scurvature(connection, d_connection),
        s2_add(s2_scale(scov(connection, distortion, d_distortion), sp.Rational(1, 2)), s2_scale(sq(distortion, distortion), sp.Rational(1, 3))),
    )
    return sp.expand(spair(distortion, source_c) + kappa * sinner(distortion, distortion) / 2)


def total_derivative(expr, jets):
    return sp.expand(sum(sp.diff(expr, jets[index]) * jets[index + 1] for index in range(len(jets) - 1)))


def main() -> None:
    data = json.loads(REGISTRY.read_text())
    type_check("registry status", data["status"].startswith("SOURCE_ORBIT_VARPI_ORDER2_ATTAINABLE"))
    type_check("repository endpoint stays separate from draft A_omega", "not identified" in data["endpoint_scope"])
    type_check("independent dK rejected only on the compatible pointwise orbit jet", data["independent_dK"] == "REJECTED_ON_COMPATIBLE_POINTWISE_CURVATURE_ORBIT_JET")
    type_check("varying-varpi fixed-epsilon/metric fixture has one Green layer", data["sector_orders"]["varying_varpi_fixed_epsilon_metric"]["green_layers"] == 1)
    type_check("literal derived-K/moving-Shiab coefficient stays open", data["sector_orders"]["varying_varpi_fixed_epsilon_metric"]["grade"].endswith("OPEN"))
    type_check("free-epsilon sector is separately graded", data["sector_orders"]["free_epsilon"]["grade"].startswith("ATTAINABLE"))
    type_check("metric Hessian remains open", data["sector_orders"]["metric"]["grade"].endswith("OPEN"))
    type_check("full root Ward remains open", data["ward_status"].endswith("FULL_ROOT_WARD_OPEN"))
    type_check("BV remains open", data["bv_status"] == "OPEN")
    type_check("domain remains open", data["domain_status"] == "OPEN")
    type_check("datum unchanged", data["external_datum"] == "P1/P2/P3 UNCHANGED AND UNUSED")
    type_check("Curt separate", data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE")

    # Exact noncommutative G2 convention check.  This fixes the sign that the
    # specialist pre-pass initially disagreed about.
    M, form1, form2 = G2["M"], G2["form1"], G2["form2"]
    B = form1(M(1, 1, 0, -1), M(0, 1, 2, 1), M(2, -1, 1, 0))
    T = form1(M(0, 2, -1, 1), M(1, -1, 1, 2), M(-1, 0, 2, 1))
    dB = form2(M(0, 1, -1, 0), M(1, 0, 2, -1), M(-1, 2, 0, 1))
    dT = form2(M(2, -1, 0, 1), M(0, 2, 1, -1), M(1, 0, -2, 1))
    A = G2["f1_add"](B, T)
    dA = G2["f2_add"](dB, dT)
    FB = G2["curvature"](B, dB)
    FA = G2["curvature"](A, dA)
    TT = G2["q"](T, T)
    C = G2["source_curvature"](B, dB, T, dT, F(1, 2), F(1, 3))
    normal = G2["f2_add"](G2["f2_scale"](F(1, 2), G2["f2_add"](FA, FB)), G2["f2_scale"](F(-1, 6), TT))
    wrong_plus = G2["f2_add"](G2["f2_scale"](F(1, 2), G2["f2_add"](FA, FB)), G2["f2_scale"](F(1, 6), TT))
    check("exact transgression normal form has minus one sixth q(T,T)", C == normal)
    check("quadratic control is live", TT != G2["form2"](G2["ZERO"], G2["ZERO"], G2["ZERO"]))
    reject("use plus one sixth under the repository q convention", C == wrong_plus)
    reject("replace one half by one in the mixed term", G2["source_curvature"](B, dB, T, dT, F(1), F(1, 3)) == C)

    # Compatible pointwise curvature-orbit jet at h=1. Curvature conjugacy fixes dK;
    # an arbitrary dK violates the reference-curvature orbit even though the
    # total endpoint connection is still held fixed.
    K = form1(M(1, 0, 1, -1), M(0, -1, 2, 1), M(2, 1, 0, -2))
    raw_dK = form2(M(1, 2, 0, -1), M(-1, 0, 1, 2), M(0, 1, -2, 1))
    Bhat = G2["f1_add"](B, K)
    That = G2["f1_add"](T, G2["f1_scale"](F(-1), K))
    legal_dK = G2["f2_add"](G2["q"](B, B), G2["f2_scale"](F(-1), G2["q"](Bhat, Bhat)))
    legal_dB = G2["f2_add"](dB, legal_dK)
    legal_dT = G2["f2_add"](dT, G2["f2_scale"](F(-1), legal_dK))
    raw_dB = G2["f2_add"](dB, raw_dK)
    raw_dT = G2["f2_add"](dT, G2["f2_scale"](F(-1), raw_dK))
    check("compatible orbit jet keeps the total connection", G2["f1_add"](Bhat, That) == A)
    check("compatible orbit jet keeps the total first jet", G2["f2_add"](legal_dB, legal_dT) == dA)
    check("curvature-constrained dK keeps F_B at the identity source point", G2["curvature"](Bhat, legal_dB) == FB)
    check("arbitrary independent dK leaves the source curvature orbit", G2["curvature"](Bhat, raw_dB) != FB)
    reject("treat raw dK as curvature-orbit compatible merely because A is fixed", G2["curvature"](Bhat, raw_dB) == FB)

    legal_action = G2["source_action"](Bhat, legal_dB, That, legal_dT, G2["shiab_identity"], F(2))
    g = M(1, 1, 0, 1)
    moved_action = G2["source_action"](
        G2["transform_f1"](g, Bhat), G2["transform_f2"](g, legal_dB),
        G2["transform_f1"](g, That), G2["transform_f2"](g, legal_dT),
        G2["shiab_identity"], F(2),
    )
    check("compatible orbit-jet action is invariant under common constant conjugation", moved_action == legal_action)

    # Symbolic varying-varpi, fixed-epsilon/metric order certificate in the same noncommutative
    # transgression grammar.  t0 is the field value, t1 its first jet, and t2
    # the next total derivative.  K is derived from t1; its exterior jet is
    # curvature-constrained rather than independently assigned.
    t0, t1, t2, t3, t4 = sp.symbols("t0 t1 t2 t3 t4")
    jets = (t0, t1, t2, t3, t4)
    sm = lambda a, b, c, d: sp.Matrix([[a, b], [c, d]])
    Bs = (sm(1, 1, 0, -1), sm(0, 1, 2, 1), sm(2, -1, 1, 0))
    dBs = (sm(0, 1, -1, 0), sm(1, 0, 2, -1), sm(-1, 2, 0, 1))
    T0 = (sm(0, 2, -1, 1), sm(1, -1, 1, 2), sm(-1, 0, 2, 1))
    DT0 = (sm(2, -1, 0, 1), sm(0, 2, 1, -1), sm(1, 0, -2, 1))
    K0 = (sm(1, 0, 1, -1), sm(0, -1, 2, 1), sm(2, 1, 0, -2))
    R0 = (sm(1, 2, 0, -1), sm(-1, 0, 1, 2), sm(0, 1, -2, 1))
    Ts, dTs, Ks = s1_scale(T0, t0), s2_scale(DT0, t1), s1_scale(K0, t1)
    Bhs, Ths = s1_add(Bs, Ks), s1_add(Ts, s1_scale(Ks, -1))
    dKraw = s2_scale(R0, t2)
    Lraw = saction(Bhs, s2_add(dBs, dKraw), Ths, s2_add(dTs, s2_scale(dKraw, -1)))
    dKlegal = s2_add(sq(Bs, Bs), s2_scale(sq(Bhs, Bhs), -1))
    L = saction(Bhs, s2_add(dBs, dKlegal), Ths, s2_add(dTs, s2_scale(dKlegal, -1)))
    check("raw split action has an independent second-jet owner", sp.diff(Lraw, t2) != 0)
    check("compatible orbit-jet action removes independent dK", not L.has(t2))
    check("compatible orbit-jet fixture retains a live first-jet response", sp.diff(L, t1) != 0)
    reject("read raw independent-dK order as source-composed order", sp.diff(Lraw, t2) == 0)

    euler_varpi = sp.expand(sp.diff(L, t0) - total_derivative(sp.diff(L, t1), jets))
    check("varying-varpi fixed-epsilon/metric Euler reaches exactly the second jet", euler_varpi.has(t2) and not euler_varpi.has(t3, t4))
    check("varying-varpi fixed-epsilon/metric principal coefficient is live", sp.diff(euler_varpi, t2) != 0)
    eta0, eta1 = sp.symbols("eta0 eta1")
    direct = sp.expand(sp.diff(L, t0) * eta0 + sp.diff(L, t1) * eta1)
    momentum = sp.diff(L, t1)
    Dmomentum = total_derivative(momentum, jets)
    green = sp.expand(momentum * eta0)
    Dgreen = sp.expand(Dmomentum * eta0 + momentum * eta1)
    check("one-layer Green identity closes exactly", sp.expand(direct - euler_varpi * eta0 - Dgreen) == 0)

    # If source epsilon owns one derivative already, t0=e1 and t1=e2.  The
    # nonzero t1 Hessian makes fourth order attainable and requires two Green
    # layers.  This is an exact jet-shift control, not the full native epsilon
    # coefficient after every moving Shiab/Hodge/density slot.
    hessian = sp.diff(L, t1, 2)
    check("free-epsilon highest-jet Hessian is nonzero", hessian != 0)
    euler_epsilon = sp.expand(-total_derivative(sp.diff(L, t0), jets) + total_derivative(total_derivative(sp.diff(L, t1), jets), jets))
    # Here t0=epsilon_1, t1=epsilon_2, t2=epsilon_3, and
    # t3=epsilon_4; t4 is the planted fifth-derivative control.
    check("free-epsilon shifted Euler reaches fourth order", euler_epsilon.has(t3) and sp.diff(euler_epsilon, t3) != 0 and not euler_epsilon.has(t4))
    eta2 = sp.symbols("eta2")
    direct2 = sp.expand(sp.diff(L, t0) * eta1 + sp.diff(L, t1) * eta2)
    p2 = sp.diff(L, t1)
    p1 = sp.expand(sp.diff(L, t0) - total_derivative(p2, jets))
    Dp1 = total_derivative(p1, jets)
    Dp2 = total_derivative(p2, jets)
    theta = sp.expand(p1 * eta0 + p2 * eta1)
    Dtheta = sp.expand(Dp1 * eta0 + p1 * eta1 + Dp2 * eta1 + p2 * eta2)
    check("two-layer free-epsilon Green identity closes exactly", sp.expand(direct2 - euler_epsilon * eta0 - Dtheta) == 0)
    reject("collapse free-epsilon and varying-varpi fixed-epsilon/metric into one jet grade", data["sector_orders"]["free_epsilon"]["euler"] == data["sector_orders"]["varying_varpi_fixed_epsilon_metric"]["attainable_euler_order"])

    # Gauge invariance is not silently promoted to the field-dependent root
    # Ward identity, and Xi is not used as a synonym for it.
    type_check("constant conjugation pass is not the full root Ward", "FIELD_DEPENDENT_CHAIN_NOT_A_NOETHER_IDENTITY" in data["ward_status"])
    reject("rename the source reparametrization chain as a Noether identity", data["ward_status"] == "FULL_ROOT_WARD_PASS")
    reject("rename Xi=D Upsilon as BV closure", data["bv_status"] == "PASS")

    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    source_check("draft action has one-half and one-third grammar", "\\frac12d_{B_\\omega}T_\\omega" in pack and "\\frac13[T_\\omega,T_\\omega]" in pack)
    source_check("source packet warns Xi is not a supplied Ward identity", "Noether identity is not" in pack)
    source_check("source is silent on the bridge action-order theorem", "c3:c11" not in pack)

    reject("spend external datum on the missing Ward operator", data["external_datum"] != "P1/P2/P3 UNCHANGED AND UNUSED")
    total = EXACT + TYPE + SOURCE + PLANTED
    print(f"PW2B source action: {EXACT} exact + {TYPE} type + {SOURCE} source + {PLANTED} planted = {total} PASS")
    print("RESULT: compatible orbit jet removes independent dK; varying-varpi fixed-epsilon/metric order two is attainable with one Green layer")
    print("BOUNDARY: literal derived-K/moving-Shiab coefficient, free-epsilon/metric packet, Ward/BV, covariant phase space, and domain remain open")


if __name__ == "__main__":
    main()
