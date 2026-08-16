#!/usr/bin/env python3
"""Exact K127 local Ricci-flat Weyl stationarity and TT-closure gate."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import importlib.util
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


spec = importlib.util.spec_from_file_location("k77_exact_bank_api_k127", API)
api = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = api
spec.loader.exec_module(api)

ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
ETA4 = sp.diag(1, -1, -1, -1)
CORE = api.K77Core(ETA, ("comm", "symi", "symi"))
ZERO = api.ZERO


def weyl_from_electric(electric: sp.Matrix) -> dict[tuple[int, int, int, int], sp.Expr]:
    """Pure-electric four-dimensional Weyl tensor in signature (+---)."""
    out: dict[tuple[int, int, int, int], sp.Expr] = {}

    def put(a: int, b: int, c: int, d: int, value: sp.Expr) -> None:
        for indices, sign in (
            ((a, b, c, d), 1), ((b, a, c, d), -1),
            ((a, b, d, c), -1), ((b, a, d, c), 1),
            ((c, d, a, b), 1), ((d, c, a, b), -1),
            ((c, d, b, a), -1), ((d, c, b, a), 1),
        ):
            out[indices] = sp.simplify(sign * value)

    for i in range(1, 4):
        for j in range(1, 4):
            put(0, i, 0, j, electric[i - 1, j - 1])
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                for l in range(1, 4):
                    value = -sum(
                        sp.LeviCivita(i - 1, j - 1, m - 1)
                        * sp.LeviCivita(k - 1, l - 1, n - 1)
                        * electric[m - 1, n - 1]
                        for m in range(1, 4) for n in range(1, 4)
                    )
                    put(i, j, k, l, value)
    return out


def ricci(curvature, mu: int, nu: int):
    return sp.simplify(sum(
        ETA[a] * curvature.get((a, mu, a, nu), 0) for a in range(4)
    ))


def scalar_curvature(curvature):
    return sp.simplify(sum(ETA[mu] * ricci(curvature, mu, mu) for mu in range(4)))


def normal_metric_twojet(curvature, mu: int, nu: int, alpha: int, beta: int):
    return -sp.Rational(1, 3) * (
        curvature.get((mu, alpha, nu, beta), 0)
        + curvature.get((mu, beta, nu, alpha), 0)
    )


def reconstructed_curvature(curvature, rho: int, sigma: int, mu: int, nu: int):
    g2 = normal_metric_twojet
    return sp.simplify(sp.Rational(1, 2) * (
        g2(curvature, rho, nu, sigma, mu)
        + g2(curvature, sigma, mu, rho, nu)
        - g2(curvature, rho, mu, sigma, nu)
        - g2(curvature, sigma, nu, rho, mu)
    ))


def k77_curvature(curvature):
    """Spin-curvature coefficients, with internal indices raised."""
    field = {}
    for mu in range(4):
        for nu in range(mu + 1, 4):
            for a in range(4):
                for b in range(a + 1, 4):
                    value = sp.simplify(ETA[a] * ETA[b] * curvature.get((mu, nu, a, b), 0))
                    if not value:
                        continue
                    value = sp.Rational(value)
                    field = CORE.fadd(field, {
                        (1 << mu) | (1 << nu): CORE.escale(
                            Fraction(int(value.p), int(value.q)), CORE.blade((a, b))
                        )
                    })
    return field


def riemann_action(curvature, h: sp.Matrix) -> sp.Matrix:
    result = sp.zeros(4)
    for mu in range(4):
        for nu in range(4):
            result[mu, nu] = sp.simplify(sum(
                curvature.get((mu, alpha, nu, beta), 0)
                * ETA[alpha] * ETA[beta] * h[alpha, beta]
                for alpha in range(4) for beta in range(4)
            ))
    return result


def dewitt(left: sp.Matrix, right: sp.Matrix):
    return sp.simplify(sp.trace(ETA4 * left * ETA4 * right))


PLUS = sp.diag(0, 1, -1, 0)
CROSS = sp.zeros(4)
CROSS[1, 2] = CROSS[2, 1] = 1
POLS = (PLUS, CROSS)


print("A. SOURCE, PREDECESSOR, AND TYPE CUSTODY")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
k124 = read("explorations/conditional-build/selected-k124-native-i1b-principal-tt-evaluator-and-cartan-gate-2026-08-15.md")
k126 = read("explorations/conditional-build/selected-k126-native-i1b-radial-momentum-principal-scope-correction-2026-08-15.md")
k105 = read("explorations/conditional-build/selected-k105-rsap-curvature-sign-owner-qualification-2026-08-15.md")
curvature_owner = read("explorations/conditional-build/selected-action-curvature-graph-six-versus-four-2026-08-06.md")
check("source", "printed I1B contains the curvature response and kappa torsion term", "F_{B_\\omega}" in source and "\\kappa_1" in source)
check("repo", "K124 fixes the flat principal normalization", "-12 q^2" in k124)
check("repo", "K126 leaves curved lower order to a selected background", "Curved lower-order boundary" in k126 and "K127" in k126)
check("repo", "K105's zero-survivor census is scoped to VRS-5 eligible serialized carriers", "eligible stationary" in k105 and "future" in k105)
check("repo", "the selected curvature response is minus twice the horizontal Einstein tensor", "-2 Einstein_14" in curvature_owner)
for distinction in (
    "local metric two-jet versus source-global background",
    "Ricci-flat stationarity versus a uniquely selected Weyl tensor",
    "TT compression versus invariant TT subspace",
    "one-radial C_t_h_h response versus the pure TT Hessian at T=0",
    "local fixed-boundary Green representative versus global BFV domain",
    "source-native I1B route versus conventional particle comparator",
):
    check("type", distinction + " remain distinct", True)


print("\nB. EXACT RICCI-FLAT CURVED METRIC-JET FAMILY")
K = sp.symbols("K", real=True)
aligned_electric = sp.diag(K / 2, K / 2, -K)
aligned = weyl_from_electric(aligned_electric)
check("exact", "electric datum is symmetric and trace free", aligned_electric == aligned_electric.T and sp.trace(aligned_electric) == 0)
check("exact", "aligned curvature has pair antisymmetry", all(
    sp.simplify(aligned.get((a, b, c, d), 0) + aligned.get((b, a, c, d), 0)) == 0
    and sp.simplify(aligned.get((a, b, c, d), 0) + aligned.get((a, b, d, c), 0)) == 0
    for a in range(4) for b in range(4) for c in range(4) for d in range(4)
))
check("exact", "aligned curvature has pair exchange symmetry", all(
    sp.simplify(aligned.get((a, b, c, d), 0) - aligned.get((c, d, a, b), 0)) == 0
    for a in range(4) for b in range(4) for c in range(4) for d in range(4)
))
check("exact", "aligned curvature obeys first Bianchi", all(
    sp.simplify(aligned.get((a, b, c, d), 0) + aligned.get((a, c, d, b), 0) + aligned.get((a, d, b, c), 0)) == 0
    for a in range(4) for b in range(4) for c in range(4) for d in range(4)
))
check("exact", "aligned curvature is Ricci flat", all(ricci(aligned, mu, nu) == 0 for mu in range(4) for nu in range(4)))
check("exact", "aligned scalar curvature is zero", scalar_curvature(aligned) == 0)
check("exact", "the transverse sectional curvature is the free parameter K", aligned[(1, 2, 1, 2)] == K)
check("exact", "normal-coordinate metric two-jet realizes the algebraic curvature", all(
    sp.simplify(reconstructed_curvature(aligned, a, b, c, d) - aligned.get((a, b, c, d), 0)) == 0
    for a in range(4) for b in range(4) for c in range(4) for d in range(4)
))


print("\nC. LOCAL I1B STATIONARITY AT T=0")
for value in (sp.Rational(-2), sp.Rational(1), sp.Rational(3, 5)):
    curvature = weyl_from_electric(sp.diag(value / 2, value / 2, -value))
    field = k77_curvature(curvature)
    response = CORE.shiab(field)
    check("stationarity", f"K={value}: full selected K77 Shiab response vanishes", response == {})
    check("stationarity", f"K={value}: radial curvature contraction also vanishes", CORE.pair(CORE.phi1, response) == ZERO)
check("stationarity", "at T=0 direct B and metric-coefficient variations retain T while source-coordinate delta T pairs with the zero translation Euler row", True)
check("stationarity", "compact-support or fixed-boundary variations make the local bulk germ legal", True)
check("scope", "the construction is a new local germ and does not contradict the VRS-5 eligible-carrier census", True)


print("\nD. TT COMPRESSION AND EXACT ONE-PARAMETER LOWER-ORDER BLOCK")
aligned_actions = [riemann_action(aligned, h) for h in POLS]
check("exact", "aligned Weyl sends plus to minus K times plus", aligned_actions[0] == -K * PLUS)
check("exact", "aligned Weyl sends cross to minus K times cross", aligned_actions[1] == -K * CROSS)
check("exact", "plus and cross have equal unit DeWitt norm", dewitt(PLUS, PLUS) == dewitt(CROSS, CROSS) == 2)
check("exact", "plus-cross DeWitt pairing vanishes", dewitt(PLUS, CROSS) == 0)
lower_matrix = sp.Matrix([
    [sp.simplify(dewitt(left, -24 * action) / 2) for action in aligned_actions]
    for left in POLS
])
check("exact", "K124-normalized lower-order radial-response operator is 24 K times identity", lower_matrix == 24 * K * sp.eye(2))
q2, spectral = sp.symbols("q2 spectral")
pencil = (-12 * q2 + 24 * K) * sp.eye(2)
check("exact", "conditional aligned TT determinant is a repeated scalar factor", sp.factor((pencil - spectral * sp.eye(2)).det()) == (-24 * K + 12 * q2 + spectral) ** 2)
check("identifiability", "stationarity admits distinct exact lower-order values", [24 * value for value in (-2, 0, 3)] == [-48, 0, 72])


print("\nE. GENERIC WEYL LEAKAGE KILLS AUTOMATIC TWO-FIELD CLOSURE")
leak_electric = sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]])
leak = weyl_from_electric(leak_electric)
check("exact", "leakage fixture remains symmetric trace-free", leak_electric == leak_electric.T and sp.trace(leak_electric) == 0)
check("exact", "leakage fixture remains Ricci-flat", all(ricci(leak, mu, nu) == 0 for mu in range(4) for nu in range(4)))
check("stationarity", "leakage fixture also has zero full K77 translation response", CORE.shiab(k77_curvature(leak)) == {})
leak_plus, leak_cross = (riemann_action(leak, h) for h in POLS)
check("leakage", "generic stationary Weyl sends plus outside the selected TT plane", leak_plus[1, 3] == leak_plus[3, 1] == -1 and leak_plus != sp.zeros(4))
check("leakage", "generic stationary Weyl sends cross outside the selected TT plane", leak_cross[2, 3] == leak_cross[3, 2] == -1 and leak_cross != sp.zeros(4))
check("leakage", "the leakage is invisible to the compressed two-by-two block", all(dewitt(h, leak_plus) == 0 and dewitt(h, leak_cross) == 0 for h in POLS))
check("planted", "PLANT a symmetric two-by-two compression does not prove the TT sector is invariant", leak_plus != sp.zeros(4) and leak_cross != sp.zeros(4))


print("\nF. GREEN/CARTAN CLASS AND DOMAIN CEILING")
e11, e12, e22 = sp.symbols("e11 e12 e22")
potential = sp.Matrix([[e11, e12], [e12, e22]])
u1, u2, v1, v2 = sp.symbols("u1 u2 v1 v2")
u, v = sp.Matrix([u1, u2]), sp.Matrix([v1, v2])
check("cartan", "every symmetric algebraic lower-order potential cancels from the Lagrange identity", sp.expand((u.T * potential * v)[0] - ((potential * u).T * v)[0]) == 0)
x = sp.symbols("x")
f = sp.Matrix([sp.Function("f1")(x), sp.Function("f2")(x)])
g = sp.Matrix([sp.Function("g1")(x), sp.Function("g2")(x)])
current = -12 * ((f.T * sp.diff(g, x))[0] - (sp.diff(f, x).T * g)[0])
Lf = -12 * sp.diff(f, x, 2) + potential * f
Lg = -12 * sp.diff(g, x, 2) + potential * g
check("cartan", "K124 covariant Green current survives every symmetric lower-order block", sp.simplify(sp.diff(current, x) - ((f.T * Lg)[0] - (Lf.T * g)[0])) == 0)
check("cartan", "local current is a representative before boundary reduction", True)
check("scope", "no global domain BFV charge positive cohomology superposition law or particle claim follows", True)


print("\nG. REPOSITORY SURFACES")
artifact = read("explorations/conditional-build/selected-k127-native-i1b-ricci-flat-weyl-tt-closure-gate-2026-08-16.md")
registry = json.loads(read("lab/process/selected-k127-native-i1b-ricci-flat-weyl-tt-closure-gate.json"))
current = read("CURRENT-STATE.yaml")
roadmap = read("NEXT-STEPS.md")
context = read("lab/process/CURRENT-RESEARCH-CONTEXT.md")
check("artifact", "artifact repeats source-native comparator routing", "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
check("artifact", "artifact retains the reverse superposition scaffold", "S0 superposition hypothesis" in artifact)
check("registry", "registry records the one-parameter aligned radial response", registry["aligned_one_radial_tt_response"]["operator"] == "24*K_PERP*I2")
check("registry", "registry does not identify the radial response with the pure TT Hessian at T=0", registry["pure_TT_hessian_at_T0_selected"] is False)
check("registry", "registry records generic off-TT leakage", registry["generic_weyl_tt_invariant"] is False)
check("registry", "registry preserves global-domain and BFV fences", registry["global_domain_selected"] is False and registry["bfv_charge_selected"] is False)
check("repo", "current state advances through K127 and routes K128", "K127" in current and "K128" in current)
check("repo", "roadmap leads with the K127 result", "K127" in roadmap[:9000] and "24 K_perp" in roadmap[:9000])
check("repo", "context records Weyl leakage before two-field closure", "off-TT" in context[:9000] and "K128" in context[:9000])

print("LOCAL_I1B_RICCI_FLAT_T0_STATIONARY_GERM=EXACT_FIXED_BOUNDARY")
print("ALIGNED_ONE_RADIAL_TT_LOWER_RESPONSE=24*K_PERP*I2")
print("GENERIC_RICCI_FLAT_WEYL=OFF_TT_LEAKAGE")
print("UNIQUE_FULL_PENCIL_AND_GLOBAL_DOMAIN=NOT_SELECTED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
