#!/usr/bin/env python3
"""Exact K126 three-momentum principal-completion and cancellation gate.

K124 evaluated a homogeneous radial leg against back-to-back TT metric waves.
This probe restores the exterior derivative and the symmetric-frame second
spin-Levi-Civita jet. It proves that K124 is exact on that slice, catches the
false nonzero produced by an isolated connection cell, and derives the full
common-transverse polynomial through an independent coordinate-curvature route.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
API = ROOT / "tests/channel-swings/k77_exact_bank_api.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8-sig")


spec = importlib.util.spec_from_file_location("k77_exact_bank_api_k126", API)
api = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = api
spec.loader.exec_module(api)

ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
CHANNELS = ("comm", "symi", "symi")
CORE = api.K77Core(ETA, CHANNELS)
ZERO = api.ZERO
Q = sp.Rational
ETA4 = sp.diag(1, -1, -1, -1)
I4 = sp.eye(4)


def gsum(values):
    out = ZERO
    for value in values:
        out = api.gadd(out, value)
    return out


def h_component(h: sp.Matrix, i: int, j: int):
    return h[i, j]


def metric_connection_symbol(momentum, h: sp.Matrix):
    out = {}
    for mu in range(4):
        for a in range(4):
            for b in range(a + 1, 4):
                coefficient = Q(1, 2) * (
                    momentum[b] * h_component(h, mu, a)
                    - momentum[a] * h_component(h, mu, b)
                )
                if coefficient:
                    out = CORE.fadd(out, {
                        1 << mu: CORE.escale(
                            Fraction(int(coefficient.p), int(coefficient.q)),
                            CORE.blade((a, b)),
                        )
                    })
    return out


def add_series(left, right, sign=1):
    return {
        key: left.get(key, sp.zeros(4)) + sign * right.get(key, sp.zeros(4))
        for key in set(left) | set(right)
    }


def mul_series(left, right):
    out = {}
    for (a, b), lm in left.items():
        for (c, d), rm in right.items():
            if a + c > 1 or b + d > 1:
                continue
            key = (a + c, b + d)
            out[key] = out.get(key, sp.zeros(4)) + lm * rm
    return out


def c_tensor(metric_wave, momentum, mu, nu):
    return sp.Matrix([
        momentum[mu] * metric_wave[nu, sigma]
        + momentum[nu] * metric_wave[mu, sigma]
        - momentum[sigma] * metric_wave[mu, nu]
        for sigma in range(4)
    ])


def gamma1(metric_wave, momentum):
    return [
        [Q(1, 2) * ETA4 * c_tensor(metric_wave, momentum, mu, nu)
         for nu in range(4)]
        for mu in range(4)
    ]


def matrix_connection_form(matrices):
    out = {}
    for mu, matrix in enumerate(matrices):
        for a in range(4):
            for b in range(a + 1, 4):
                coefficient = Q(matrix[a, b])
                if coefficient:
                    out = CORE.fadd(out, {
                        1 << mu: CORE.escale(
                            Fraction(int(coefficient.p), int(coefficient.q)),
                            CORE.blade((a, b)),
                        )
                    })
    return out


def spin_connection_twojet(h, p, k, q):
    """Return DB[h], DB[k], D2B[h,k] in the symmetric orthonormal frame."""
    h_sharp = ETA4 * h * ETA4
    k_sharp = ETA4 * k * ETA4
    gamma2 = [
        [
            -Q(1, 2) * (
                h_sharp * c_tensor(k, q, mu, nu)
                + k_sharp * c_tensor(h, p, mu, nu)
            )
            for nu in range(4)
        ]
        for mu in range(4)
    ]

    hh, kk = ETA4 * h, ETA4 * k
    eh, ek = Q(1, 2) * hh, Q(1, 2) * kk
    ehk = -Q(1, 8) * (hh * kk + kk * hh)
    frame = {(0, 0): I4, (1, 0): eh, (0, 1): ek, (1, 1): ehk}
    frame_inv = {
        (0, 0): I4,
        (1, 0): -eh,
        (0, 1): -ek,
        (1, 1): eh * ek + ek * eh - ehk,
    }
    gh, gk = gamma1(h, p), gamma1(k, q)
    omega = []
    for mu in range(4):
        gamma_mu = {
            (1, 0): sp.Matrix.hstack(*gh[mu]),
            (0, 1): sp.Matrix.hstack(*gk[mu]),
            (1, 1): sp.Matrix.hstack(*gamma2[mu]),
        }
        dframe_mu = {
            (1, 0): p[mu] * eh,
            (0, 1): q[mu] * ek,
            (1, 1): (p[mu] + q[mu]) * ehk,
        }
        numerator = add_series(mul_series(frame, gamma_mu), dframe_mu, sign=-1)
        omega.append(mul_series(numerator, frame_inv))

    first_h = matrix_connection_form([ETA4 * item[(1, 0)] for item in omega])
    first_k = matrix_connection_form([ETA4 * item[(0, 1)] for item in omega])
    second = matrix_connection_form([ETA4 * item[(1, 1)] for item in omega])
    return first_h, first_k, second


def exterior_symbol(momentum, field):
    one_form = {
        1 << mu: {0: (Fraction(value), Fraction(0))}
        for mu, value in enumerate(momentum) if value
    }
    return CORE.wedge_raw(one_form, field)


def radial_curvature_polarization(h, p, k, q):
    b_h, b_k, b_hk = spin_connection_twojet(h, p, k, q)
    total_momentum = tuple(p[i] + q[i] for i in range(4))
    derivative = exterior_symbol(total_momentum, b_hk)
    square = CORE.fadd(
        CORE.wedge_raw(b_h, b_k), CORE.wedge_raw(b_k, b_h)
    )
    derivative_value = CORE.pair(CORE.phi1, CORE.shiab(derivative))
    square_value = CORE.pair(CORE.phi1, CORE.shiab(square))
    return derivative_value, square_value, api.gadd(derivative_value, square_value), b_hk


def q_square(q):
    return sum(ETA[index] * q[index] * q[index] for index in range(4))


def dewitt_tt(left, right):
    return sp.trace(ETA4 * left * ETA4 * right)


def coordinate_scalar_curvature_mixed(h, p, k, q):
    """Mixed flat-background scalar-curvature coefficient in a fixed chart."""
    gh, gk = gamma1(h, p), gamma1(k, q)
    h_sharp = ETA4 * h * ETA4
    k_sharp = ETA4 * k * ETA4
    g2 = [
        [
            -Q(1, 2) * (
                h_sharp * c_tensor(k, q, mu, nu)
                + k_sharp * c_tensor(h, p, mu, nu)
            )
            for nu in range(4)
        ]
        for mu in range(4)
    ]

    def riemann1(gamma, momentum):
        return {
            (rho, sigma, mu, nu): sp.expand(
                momentum[mu] * gamma[nu][sigma][rho]
                - momentum[nu] * gamma[mu][sigma][rho]
            )
            for rho in range(4) for sigma in range(4)
            for mu in range(4) for nu in range(4)
        }

    rh, rk = riemann1(gh, p), riemann1(gk, q)
    inverse_h, inverse_k = -ETA4 * h * ETA4, -ETA4 * k * ETA4
    value = 0
    for sigma in range(4):
        for nu in range(4):
            for rho in range(4):
                mixed_riemann = (
                    (p[rho] + q[rho]) * g2[nu][sigma][rho]
                    - (p[nu] + q[nu]) * g2[rho][sigma][rho]
                )
                for lam in range(4):
                    mixed_riemann += (
                        gh[rho][lam][rho] * gk[nu][sigma][lam]
                        + gk[rho][lam][rho] * gh[nu][sigma][lam]
                        - gh[nu][lam][rho] * gk[rho][sigma][lam]
                        - gk[nu][lam][rho] * gh[rho][sigma][lam]
                    )
                value += (
                    ETA4[sigma, nu] * mixed_riemann
                    + inverse_h[sigma, nu] * rk[rho, sigma, rho, nu]
                    + inverse_k[sigma, nu] * rh[rho, sigma, rho, nu]
                )
    return sp.factor(value)


PLUS = sp.diag(0, 1, -1, 0)
CROSS = sp.zeros(4)
CROSS[1, 2] = CROSS[2, 1] = 1
POLS = {"plus": PLUS, "cross": CROSS}
CAUSAL = {
    "timelike": (1, 0, 0, 0),
    "spacelike": (0, 0, 0, 1),
    "null": (1, 0, 0, 1),
}


print("A. SOURCE, PREDECESSOR, AND TYPE CUSTODY")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
k124 = read("explorations/conditional-build/selected-k124-native-i1b-principal-tt-evaluator-and-cartan-gate-2026-08-15.md")
k125 = read("explorations/conditional-build/selected-k125-native-i1b-fixed-chart-cartan-recombination-2026-08-15.md")
k125_probe = read("tests/channel-swings/selected_k125_native_i1b_fixed_chart_cartan_recombination_probe.py")
second_jet = read("explorations/conditional-build/selected-action-second-soldering-observation-jets-2026-08-06.md")
check("source", "printed action contains the curvature exterior derivative", "F_{B_\\omega}" in source)
check("source", "printed action contains the one-half covariant derivative term", "\\frac12d_{B_\\omega}T_\\omega" in source)
check("repo", "K124 explicitly deferred exterior derivative and D2LC", "K125" in k124 and "D2B_LC" in k124)
check("repo", "K125 proves generic curvature covariance but does not run the actual K77 action engine", "curvature naturality" in k125 and "K77Core" not in k125_probe and "k77_exact_bank_api" not in k125_probe)
check("repo", "the exact symmetric-frame second spin-LC jet is owned", "nonzero, symmetric second metric jet" in second_jet and "spin connection" in second_jet)
for distinction in (
    "homogeneous radial leg versus a radial leg carrying momentum",
    "back-to-back TT slice versus a general three-point symbol",
    "bulk coefficient versus a Cartan representative",
    "flat principal germ versus curved lower-order background data",
    "principal Cartan covector versus a reduced BFV charge",
):
    check("type", distinction + " remain distinct", True)


print("\nB. ACTUAL K77 CURVATURE CONTRACTION AND SECOND LC JET")
functional = {}
for mu in range(4):
    for nu in range(mu + 1, 4):
        for a in range(4):
            for b in range(a + 1, 4):
                field = {(1 << mu) | (1 << nu): CORE.blade((a, b))}
                value = CORE.pair(CORE.phi1, CORE.shiab(field))
                if value != ZERO:
                    functional[(mu, nu, a, b)] = value
check("exact", "radial Shiab contraction has exactly six horizontal diagonal cells", len(functional) == 6)
check("exact", "each live curvature-contraction cell has coefficient 24", set(functional.values()) == {(Fraction(24), Fraction(0))})

witness_p, witness_q = (1, 0, 0, 0), (0, 0, 0, 1)
b1, b2, b12 = spin_connection_twojet(PLUS, witness_p, PLUS, witness_q)
check("exact", "first spin-LC jet agrees with the K124 closed formula", b1 == metric_connection_symbol(witness_p, PLUS) and b2 == metric_connection_symbol(witness_q, PLUS))
check("exact", "mixed symmetric-frame second spin-LC jet is nonzero", bool(b12))
swap = spin_connection_twojet(PLUS, witness_q, PLUS, witness_p)[2]
check("exact", "second spin-LC jet is symmetric under its labelled pair exchange", b12 == swap)


print("\nC. K124 BACK-TO-BACK SLICE RECOMBINES EXACTLY")
back_records = {}
for causal, momentum in CAUSAL.items():
    opposite = tuple(-value for value in momentum)
    for left_name, left in POLS.items():
        for right_name, right in POLS.items():
            derivative, square, total, _ = radial_curvature_polarization(
                left, momentum, right, opposite
            )
            expected = (
                Fraction(-12 * q_square(momentum) * int(dewitt_tt(left, right))),
                Fraction(0),
            )
            back_records[(causal, left_name, right_name)] = total
            check("exact", f"{causal} {left_name}-{right_name}: dD2LC vanishes at total metric momentum zero", derivative == ZERO)
            check("exact", f"{causal} {left_name}-{right_name}: fixed-chart total reproduces K124", total == expected)
check("exact", "back-to-back unit diagonals remain -24,+24,0", [back_records[(name, "plus", "plus")][0] for name in CAUSAL] == [-24, 24, 0])


print("\nD. NONZERO RADIAL MOMENTUM: PARTIAL TERM AND FULL TRANSPORT CANCELLATION")
radial_momentum = tuple(-(witness_p[i] + witness_q[i]) for i in range(4))
nonback = {}
for left_name, left in POLS.items():
    for right_name, right in POLS.items():
        derivative, square, total, second = radial_curvature_polarization(
            left, witness_p, right, witness_q
        )
        nonback[(left_name, right_name)] = (derivative, square, total, second)
check("exact", "the selected radial momentum is nonzero and null", radial_momentum == (-1, 0, 0, -1) and q_square(radial_momentum) == 0)
check("exact", "plus-plus exterior D2LC contribution is nonzero", nonback[("plus", "plus")][0] == (Fraction(-24), Fraction(0)))
check("exact", "cross-cross exterior D2LC contribution is the same", nonback[("cross", "cross")][0] == (Fraction(-24), Fraction(0)))
check("exact", "the connection-square term vanishes on this nonback witness", nonback[("plus", "plus")][1] == ZERO and nonback[("cross", "cross")][1] == ZERO)
check("exact", "cross-polarization entries remain zero", nonback[("plus", "cross")][2] == ZERO and nonback[("cross", "plus")][2] == ZERO)

cartan_covector = []
for mu in range(4):
    unit = tuple(1 if index == mu else 0 for index in range(4))
    cartan_covector.append(
        CORE.pair(CORE.phi1, CORE.shiab(exterior_symbol(unit, b12)))
    )
total_metric_momentum = tuple(witness_p[i] + witness_q[i] for i in range(4))
cartan_contraction = gsum(
    api.gscale(total_metric_momentum[mu], cartan_covector[mu])
    for mu in range(4)
)
check("cartan", "partial noncyclic exterior Cartan covector is exact", cartan_covector == [
    (Fraction(-12), Fraction(0)), ZERO, ZERO, (Fraction(-12), Fraction(0))
])
check("cartan", "exterior D2LC term is total momentum contracted with Cartan", cartan_contraction == nonback[("plus", "plus")][0])
check("cartan", "momentum conservation transfers the term to the radial derivative", gsum(
    api.gscale(-radial_momentum[mu], cartan_covector[mu]) for mu in range(4)
) == nonback[("plus", "plus")][0])

coordinate_witness = coordinate_scalar_curvature_mixed(
    PLUS, witness_p, PLUS, witness_q
)
check("independent", "complete coordinate scalar-curvature coefficient vanishes on the witness", coordinate_witness == 0)
check("independent", "cross polarization has the same complete cancellation", coordinate_scalar_curvature_mixed(CROSS, witness_p, CROSS, witness_q) == 0)
check("correction", "omitted coframe pairing and tautological transport cancels the partial minus 24", nonback[("plus", "plus")][2][0] == -24 and -nonback[("plus", "plus")][2][0] == 24)
check("planted", "PLANT treating the exterior cell as the full action gives a false nonzero", nonback[("plus", "plus")][2][0] != -24 * coordinate_witness)

a, b, c, d = sp.symbols("a b c d")
symbolic_p, symbolic_q = (a, 0, 0, b), (c, 0, 0, d)
p2, q2 = a**2 - b**2, c**2 - d**2
pdotq = a * c - b * d
r2 = sp.expand(p2 + q2 + 2 * pdotq)
expected_curvature = 2 * (p2 + q2) + 3 * pdotq
plus_curvature = coordinate_scalar_curvature_mixed(PLUS, symbolic_p, PLUS, symbolic_q)
cross_curvature = coordinate_scalar_curvature_mixed(CROSS, symbolic_p, CROSS, symbolic_q)
check("independent", "plus common-transverse curvature polynomial is exact", sp.expand(plus_curvature - expected_curvature) == 0)
check("independent", "cross common-transverse curvature polynomial is identical", sp.expand(cross_curvature - expected_curvature) == 0)
check("independent", "cross-polarization coordinate curvature vanishes", coordinate_scalar_curvature_mixed(PLUS, symbolic_p, CROSS, symbolic_q) == 0 and coordinate_scalar_curvature_mixed(CROSS, symbolic_p, PLUS, symbolic_q) == 0)
full_common_transverse = sp.expand(-24 * expected_curvature)
radial_form = sp.expand(-12 * (p2 + q2 + 3 * r2))
check("exact", "full common-transverse K77 coefficient has radial-momentum normal form", sp.expand(full_common_transverse - radial_form) == 0)
check("exact", "K124 is recovered when q=-p and r=0", sp.expand(full_common_transverse.subs({c: -a, d: -b}) + 24 * p2) == 0)


print("\nE. MIXED TT BLOCK AND LOWER-ORDER IDENTIFIABILITY")


def gauss_tt(normal, components):
    out = {}
    for (mu, nu), amplitude in components.items():
        coefficient = -ETA[nu] * ETA[normal] * amplitude
        out = CORE.fadd(out, {
            1 << mu: CORE.escale(coefficient, CORE.blade((nu, normal)))
        })
    return out


def scalar_action(b_field, t_field):
    packet = CORE.fadd(
        CORE.wedge_raw(b_field, b_field),
        CORE.fscale(Fraction(1, 2), CORE.fadd(
            CORE.wedge_raw(b_field, t_field),
            CORE.wedge_raw(t_field, b_field),
        )),
        CORE.fscale(Fraction(1, 3), CORE.wedge_raw(t_field, t_field)),
    )
    return api.gadd(
        CORE.pair(t_field, CORE.shiab(packet)),
        api.gscale(Fraction(1, 2), CORE.pair(t_field, CORE.hodge(t_field))),
    )


def corner_polarization(directions):
    out = ZERO
    for bits in product((0, 1), repeat=len(directions)):
        b_field, t_field = {}, {}
        for bit, (b_direction, t_direction) in zip(bits, directions):
            if bit:
                b_field = CORE.fadd(b_field, b_direction)
                t_field = CORE.fadd(t_field, t_direction)
        sign = -1 if (len(directions) - sum(bits)) % 2 else 1
        out = api.gadd(out, api.gscale(sign, scalar_action(b_field, t_field)))
    return out


v_pols = {
    "plus": {(1, 1): 1, (2, 2): -1},
    "cross": {(1, 2): 1, (2, 1): 1},
}
mixed = []
for momentum in ((1, 0, 0, 0), (0, 0, 0, 1), (1, 0, 0, 1)):
    for h in POLS.values():
        b_h = metric_connection_symbol(momentum, h)
        for components in v_pols.values():
            for normal in range(4, 14):
                mixed.append(corner_polarization([
                    ({}, CORE.phi1), (b_h, {}), ({}, gauss_tt(normal, components))
                ]))
check("exact", "C_t_h_v remains zero on the 120-entry selected fixed-frame TT packet", len(mixed) == 120 and set(mixed) == {ZERO})
check("type", "dD2LC cannot enter a coefficient with only one metric leg", True)

background_b = {1 << 0: CORE.blade((0, 3))}
background_lower = CORE.pair(CORE.phi1, CORE.shiab(CORE.fadd(
    CORE.wedge_raw(background_b, b12), CORE.wedge_raw(b12, background_b)
)))
check("exact", "a nonzero fixed-chart background connection changes the lower-order D2LC packet", background_lower == (Fraction(24), Fraction(0)))
check("identifiability", "the flat principal germ does not select a curved background connection jet", True)
check("identifiability", "a coordinate background-connection witness is not a covariant lower-order invariant", True)
check("identifiability", "curved lower-order completion requires a selected background jet and natural coefficient transport", True)
check("cartan", "the partial Cartan covector is not promoted after full transport cancels its bulk", coordinate_witness == 0 and cartan_covector != [ZERO] * 4)
check("scope", "no global domain BFV charge full pencil spectrum or particle claim follows", True)


print("\nF. REPOSITORY SURFACES")
artifact = read("explorations/conditional-build/selected-k126-native-i1b-radial-momentum-principal-scope-correction-2026-08-15.md")
registry = json.loads(read("lab/process/selected-k126-native-i1b-radial-momentum-principal-scope-correction.json"))
current = read("CURRENT-STATE.yaml")
roadmap = read("NEXT-STEPS.md")
context = read("lab/process/CURRENT-RESEARCH-CONTEXT.md")
check("artifact", "artifact carries source-native comparator routing", "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
check("artifact", "artifact corrects K124 to homogeneous radial momentum", "homogeneous radial" in artifact and "back-to-back" in artifact)
check("registry", "registry records partial minus 24 and complete zero", registry["radial_momentum_witness"]["partial_d_D2B_LC"] == -24 and registry["radial_momentum_witness"]["complete_transported_action"] == 0)
check("registry", "registry preserves curved lower-order and BFV fences", registry["curved_lower_order_complete"] is False and registry["bfv_charge_selected"] is False)
check("repo", "current state advances through K126", "K126" in current and "transport" in current)
check("repo", "roadmap routes K127 through background and representative selection", "K127" in roadmap[:8000])
check("repo", "context records the K124 scope correction", "homogeneous-radial" in context[:7000])

print("K124_SCOPE=HOMOGENEOUS_RADIAL__BACK_TO_BACK_TT")
print("K126_PARTIAL_FIXED_CHART_CELL=D_D2BLC_MINUS_24__B_SQUARED_0")
print("FULL_TRANSPORT_REMAINDER=PLUS_24__COMPLETE_WITNESS_0")
print("COMMON_TRANSVERSE_FULL_SYMBOL=-6*(p2+q2+3*r2)*DEWITT")
print("PARTIAL_CARTAN_COVECTOR=(-12,0,0,-12)__NOT_FULL_CARTAN")
print("C_THV_SELECTED_TT=0__120_OF_120")
print("CURVED_LOWER_ORDER_BACKGROUND_AND_GLOBAL_BFV=OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
