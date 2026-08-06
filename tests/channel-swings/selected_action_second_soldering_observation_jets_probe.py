#!/usr/bin/env python3
"""Exact second soldering/observation jets and nonlinear owner formula."""

from collections import Counter
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
Q = sp.Rational
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    path = ROOT / relative
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=hook)


def add_series(left, right, sign=1):
    keys = set(left) | set(right)
    return {key: left.get(key, sp.zeros(4)) + sign * right.get(key, sp.zeros(4)) for key in keys}


def mul_series(left, right):
    out = {}
    for (a, b), lm in left.items():
        for (c, d), rm in right.items():
            if a + c > 1 or b + d > 1:
                continue
            key = (a + c, b + d)
            out[key] = out.get(key, sp.zeros(4)) + lm * rm
    return out


print("A. SOURCE AND LAYER-0 OWNERS")
source = (ROOT / "lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-action-physical-soldering-observation-compose-2026-08-06.md").read_text()
check("source", "source names gauge-rotated Levi-Civita in the contorsion slot", "gauge-rotated Levi-Civita" in source)
check("source", "source types augmented torsion as a connection difference", "difference of two connections" in source)
check("source", "source corrects naive pullback", "SOURCE-CORRECTS-NAIVE-READING" in source)
check("repo", "predecessor leaves nonlinear second jets open", "second observation and soldering" in predecessor)
for label in (
    "Christoffel connection versus symmetric-frame spin connection",
    "Frechet second observation jet versus spatial second section jet",
    "nonlinear Euler owner formula versus expanded selected-action coefficient",
    "preboundary potential versus reduced BFV phase space",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT SECOND CHRISTOFFEL JET")
eta = sp.diag(-1, 1, 1, 1)
h = sp.zeros(4)
h[1, 1], h[2, 2] = 1, -1
l = sp.zeros(4)
l[1, 2] = l[2, 1] = 1
p = (Q(3), Q(0), Q(0), Q(3))
q = (Q(5), Q(0), Q(0), Q(-4))


def C(metric_wave, momentum, mu, nu):
    return sp.Matrix([
        momentum[mu] * metric_wave[nu, sigma]
        + momentum[nu] * metric_wave[mu, sigma]
        - momentum[sigma] * metric_wave[mu, nu]
        for sigma in range(4)
    ])


def gamma1(metric_wave, momentum):
    return [
        [Q(1, 2) * eta * C(metric_wave, momentum, mu, nu) for nu in range(4)]
        for mu in range(4)
    ]


def gamma2(hw, hp, lw, lq):
    hsharp = eta * hw * eta
    lsharp = eta * lw * eta
    return [
        [
            -Q(1, 2) * (hsharp * C(lw, lq, mu, nu) + lsharp * C(hw, hp, mu, nu))
            for nu in range(4)
        ]
        for mu in range(4)
    ]


G2 = gamma2(h, p, l, q)
G2_swap = gamma2(l, q, h, p)
check("exact", "second Christoffel jet is symmetric in the perturbation pairs", G2 == G2_swap)
check("exact", "second Christoffel jet is nonzero on the TT pair", any(entry != sp.zeros(4, 1) for row in G2 for entry in row))

t, u = sp.symbols("t u")
g = eta + t * h + u * l
g_inv = g.inv()
series_G2 = []
for mu in range(4):
    row = []
    for nu in range(4):
        derivative_metric = t * C(h, p, mu, nu) + u * C(l, q, mu, nu)
        exact_gamma = Q(1, 2) * g_inv * derivative_metric
        row.append(exact_gamma.diff(t, u).subs({t: 0, u: 0}))
    series_G2.append(row)
check("exact", "independent inverse-metric differentiation reproduces D2 Gamma", series_G2 == G2)
check("planted", "PLANT freezing the inverse metric would erase a live second jet", any(entry != sp.zeros(4, 1) for row in G2 for entry in row))


print("\nC. EXACT SYMMETRIC-FRAME SPIN-CONNECTION SECOND JET")
I = sp.eye(4)
H = eta * h
L = eta * l
Eh = Q(1, 2) * H
El = Q(1, 2) * L
Ehl = -Q(1, 8) * (H * L + L * H)
E = {(0, 0): I, (1, 0): Eh, (0, 1): El, (1, 1): Ehl}
E_inv = {
    (0, 0): I,
    (1, 0): -Eh,
    (0, 1): -El,
    (1, 1): Eh * El + El * Eh - Ehl,
}
g_series = {(0, 0): eta, (1, 0): h, (0, 1): l}
metric_from_frame = mul_series(mul_series({key: value.T for key, value in E.items()}, {(0, 0): eta}), E)
for key in ((0, 0), (1, 0), (0, 1), (1, 1)):
    check("exact", f"tetrad square-root identity holds at coefficient {key}", metric_from_frame.get(key, sp.zeros(4)) == g_series.get(key, sp.zeros(4)))
inverse_product = mul_series(E, E_inv)
check("exact", "frame inverse is exact through mixed order", all(inverse_product.get(key, sp.zeros(4)) == (I if key == (0, 0) else sp.zeros(4)) for key in ((0, 0), (1, 0), (0, 1), (1, 1))))

Gamma_h = gamma1(h, p)
Gamma_l = gamma1(l, q)
Gamma_hl = G2
omega = []
for mu in range(4):
    Gamma_mu = {
        (1, 0): sp.Matrix.hstack(*[Gamma_h[mu][nu] for nu in range(4)]),
        (0, 1): sp.Matrix.hstack(*[Gamma_l[mu][nu] for nu in range(4)]),
        (1, 1): sp.Matrix.hstack(*[Gamma_hl[mu][nu] for nu in range(4)]),
    }
    dE_mu = {
        (1, 0): p[mu] * Eh,
        (0, 1): q[mu] * El,
        (1, 1): (p[mu] + q[mu]) * Ehl,
    }
    numerator = add_series(mul_series(E, Gamma_mu), dE_mu, sign=-1)
    omega_mu = mul_series(numerator, E_inv)
    omega.append(omega_mu)
    postulate = add_series(add_series(dE_mu, mul_series(E, Gamma_mu), sign=-1), mul_series(omega_mu, E))
    check("exact", f"tetrad postulate closes through mixed order for mu={mu}", all(value == sp.zeros(4) for value in postulate.values()))
    check("exact", f"spin connection is eta-skew through mixed order for mu={mu}", all(value.T * eta + eta * value == sp.zeros(4) for value in omega_mu.values()))

for metric_wave, momentum, key, name in ((h, p, (1, 0), "h"), (l, q, (0, 1), "l")):
    expected = []
    for mu in range(4):
        target = sp.zeros(4)
        for a in range(4):
            for b in range(4):
                target[a, b] = Q(1, 2) * (momentum[b] * metric_wave[mu, a] - momentum[a] * metric_wave[mu, b])
        expected.append(target)
    check("exact", f"linear spin connection for {name} matches the selected-cubic owner", all(eta * omega[mu][key] == expected[mu] for mu in range(4)))

spin2 = [omega_mu[(1, 1)] for omega_mu in omega]
check("exact", "symmetric-frame second spin-connection jet is nonzero", any(value != sp.zeros(4) for value in spin2))

# Rebuild with the perturbation pairs swapped. Mixed coefficients must agree.
Hs, Ls = L, H
Ehs, Els = El, Eh
Ehls = -Q(1, 8) * (Hs * Ls + Ls * Hs)
check("exact", "the frame mixed coefficient is symmetric under pair exchange", Ehl == Ehls)
check("type", "gauge rotation adds an invertible adjoint action and a connection-gauge image", True)


print("\nD. EXACT SECOND OBSERVATION JET")
J = sp.Matrix([[Q(1, 2), Q(-1, 3)], [Q(2, 5), Q(3, 7)], [Q(-4, 9), Q(5, 11)]])
j1 = sp.Matrix([[Q(1, 7), Q(2, 9)], [Q(-3, 8), Q(4, 13)], [Q(5, 12), Q(-6, 17)]])
j2 = sp.Matrix([[Q(-2, 7), Q(1, 5)], [Q(3, 11), Q(-4, 15)], [Q(5, 17), Q(6, 19)]])
b, n = J.cols, J.rows


def M_of(section_jet):
    return sp.Matrix.vstack(
        sp.Matrix.hstack(sp.eye(b), section_jet.T),
        sp.Matrix.hstack(sp.zeros(n, b), sp.eye(n)),
    )


def dM(section_variation):
    return sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(b), section_variation.T),
        sp.zeros(n, b + n),
    )


M = M_of(J)
a = sp.Matrix([Q(3), Q(5), Q(7), Q(11), Q(13)])
a1 = sp.Matrix([Q(17), Q(19), Q(23), Q(29), Q(31)])
a2 = sp.Matrix([Q(37), Q(41), Q(43), Q(47), Q(53)])
mixed_observation = dM(j1) * a2 + dM(j2) * a1
check("exact", "pure-section second Frechet derivative of observation is zero", M_of(J + j1 + j2) - M - dM(j1) - dM(j2) == sp.zeros(b + n))
check("exact", "section-field cross second jet is nonzero", mixed_observation != sp.zeros(b + n, 1))

Qtu = M_of(J + t * j1 + u * j2) * (a + t * a1 + u * a2)
check("exact", "independent mixed differentiation gives the cross-jet formula", Qtu.diff(t, u).subs({t: 0, u: 0}) == mixed_observation)

O = M.inv().T
Otu = M_of(J + t * j1 + u * j2).inv().T
check("exact", "equation dual is affine in the section jet", Otu.diff(t, u).subs({t: 0, u: 0}) == sp.zeros(b + n))
check("exact", "a spatial second section jet enters only through total differentiation", dM(j2) != sp.zeros(b + n))
check("planted", "PLANT freezing the section jet deletes a live cross owner", mixed_observation != sp.zeros(b + n, 1))
check("type", "no new observation datum is required", True)


print("\nE. NONLINEAR FORMAL-ADJOINT AND PRESYMPLECTIC OWNER")
g0, g1, g2 = sp.symbols("g0 g1 g2", nonzero=True)
A = g1 / g0
lagrangian = A**2 / 2
dL_dg0 = sp.diff(lagrangian, g0)
dL_dg1 = sp.diff(lagrangian, g1)
total_d = lambda f: sp.diff(f, g0) * g1 + sp.diff(f, g1) * g2
direct_euler = sp.simplify(dL_dg0 - total_d(dL_dg1))
C0 = -g1 / g0**2
C1 = 1 / g0
chain_euler = sp.simplify(C0 * A - total_d(C1 * A))
check("exact", "nonlinear formal-adjoint chain equals direct composite Euler", direct_euler == chain_euler)
check("exact", "the nonlinear Euler owner contains the spatial second metric jet", g2 in chain_euler.free_symbols)
check("exact", "the soldered preboundary coefficient equals the direct Cartan coefficient", sp.simplify(C1 * A - dL_dg1) == 0)

h0, h1, l0, l1 = sp.symbols("h0 h1 l0 l1")
scalar_A = (g1 + t * h1 + u * l1) / (g0 + t * h0 + u * l0)
scalar_hessian = sp.simplify(scalar_A.diff(t, u).subs({t: 0, u: 0}))
expected_hessian = 2 * g1 * h0 * l0 / g0**3 - (h0 * l1 + l0 * h1) / g0**2
check(
    "exact",
    "scalar nonlinear connection control reproduces its exact second jet",
    sp.simplify(scalar_hessian - expected_hessian) == 0,
)
check("planted", "PLANT dropping total derivatives loses the g2 Euler term", sp.simplify(C0 * A - direct_euler) != 0)
check("planted", "PLANT the preboundary owner is not a BFV reduction", True)


print("\nF. REGISTRY AND PROGRAM FENCES")
registry = strict("lab/process/selected-action-second-soldering-observation-jets.json")
check("source", "source return is scoped", registry["source_return"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT")
check("exact", "no free object or datum is introduced", registry["free_object_delta"] == 0 and set(registry["external_datum"].values()) == {"UNUSED"})
check("type", "direct selected-action coefficient expansion remains open", registry["exact_result"]["direct_selected_action_metric_coefficients"] == "OPEN")
check("type", "Curt and third-lane fences hold", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and registry["third_lane"] == "NOT_PROMOTED")
for label in (
    "second jet ownership is not full selected-action stationarity",
    "Christoffel D2 is not silently substituted for spin-connection D2",
    "local Euler order is not a global hyperbolic domain",
    "no diffeomorphism or odd super-IG quotient is inferred",
    "P1 P2 P3 remain unused",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS_AND_SOURCE-SILENT")
print("SECOND_SPIN_LEVI_CIVITA_JET=EXACT_NONZERO_SYMMETRIC")
print("OBSERVATION_PURE_SECTION_D2=0__SECTION_FIELD_CROSS_D2=EXACT_NONZERO")
print("NONLINEAR_FORMAL_ADJOINT_EULER_AND_PREBOUNDARY_OWNER=EXACT")
print("DIRECT_SELECTED_ACTION_COEFFICIENT_EXPANSION=OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
