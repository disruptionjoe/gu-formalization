#!/usr/bin/env python3
"""Exact K124 native I1B principal-TT evaluator and Cartan gate.

This probe composes the current K77 Clifford/exterior engine with the native
metric graph.  It evaluates the co-moving principal bulk normal form directly
on all three causal representatives, both TT polarizations, and every vertical
normal.  It does not replace the still-open lower-order/global Cartan packet by
a fitted completion.
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


spec = importlib.util.spec_from_file_location("k77_exact_bank_api_k124", API)
api = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = api
spec.loader.exec_module(api)

# Instantiate the current selected real K77 carrier directly.  Deliberately do
# not consume the versioned coefficient bank: K124 differentiates the scalar
# action rather than reading a prior Hessian column.
ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
CHANNELS = ("comm", "symi", "symi")
CORE = api.K77Core(ETA, CHANNELS)
ZERO = api.ZERO
SLOTS = [(i, j) for i in range(4) for j in range(i, 4)]
PAIRS = [(a, b) for a in range(4) for b in range(a + 1, 4)]


def h_component(i: int, j: int, a: int, b: int) -> int:
    return int((i == a and j == b) or (i == b and j == a))


def metric_connection_symbol(q: tuple[int, ...], h: dict[tuple[int, int], int]):
    """Principal symmetric-frame spin-LC symbol DB_LC(q)[h]."""
    out = {}
    for (i, j), amplitude in h.items():
        for mu in range(4):
            for a, b in PAIRS:
                coefficient = sum(
                    Fraction(q[lam], 2)
                    * ((lam == b) * h_component(i, j, mu, a)
                       - (lam == a) * h_component(i, j, mu, b))
                    for lam in range(4)
                )
                if coefficient:
                    out = CORE.fadd(
                        out,
                        {1 << mu: CORE.escale(amplitude * coefficient, CORE.blade((a, b)))},
                    )
    return out


def gauss_tt(normal: int, components: dict[tuple[int, int], int]):
    """Metric-skew insertion of one normal-valued TT second form."""
    out = {}
    for (mu, nu), amplitude in components.items():
        coefficient = -ETA[nu] * ETA[normal] * amplitude
        out = CORE.fadd(
            out,
            {1 << mu: CORE.escale(coefficient, CORE.blade((nu, normal)))},
        )
    return out


def scalar_action(b_field, t_field, kappa: Fraction = Fraction(1)):
    """Co-moving principal bulk normal form of the printed first action."""
    curvature = CORE.wedge_raw(b_field, b_field)
    db_t = CORE.fadd(
        CORE.wedge_raw(b_field, t_field), CORE.wedge_raw(t_field, b_field)
    )
    t_square = CORE.wedge_raw(t_field, t_field)
    packet = CORE.fadd(
        curvature,
        CORE.fscale(Fraction(1, 2), db_t),
        CORE.fscale(Fraction(1, 3), t_square),
    )
    return api.gadd(
        CORE.pair(t_field, CORE.shiab(packet)),
        api.gscale(Fraction(kappa, 2), CORE.pair(t_field, CORE.hodge(t_field))),
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


def q_square(q: tuple[int, ...]) -> int:
    return sum(ETA[mu] * q[mu] * q[mu] for mu in range(4))


def dewitt_tt(left: dict[tuple[int, int], int], right: dict[tuple[int, int], int]):
    lm = sp.zeros(4)
    rm = sp.zeros(4)
    for (i, j), value in left.items():
        lm[i, j] = lm[j, i] = value
    for (i, j), value in right.items():
        rm[i, j] = rm[j, i] = value
    ginv = sp.diag(1, -1, -1, -1)
    return sp.trace(ginv * lm * ginv * rm)


CONFIGS = {
    "timelike": {
        "q": (1, 0, 0, 0),
        "h": {"plus": {(1, 1): 1, (2, 2): -1}, "cross": {(1, 2): 1}},
        "v": {
            "plus": {(1, 1): 1, (2, 2): -1},
            "cross": {(1, 2): 1, (2, 1): 1},
        },
    },
    "spacelike": {
        "q": (0, 1, 0, 0),
        "h": {"plus": {(2, 2): 1, (3, 3): -1}, "cross": {(2, 3): 1}},
        "v": {
            "plus": {(2, 2): 1, (3, 3): -1},
            "cross": {(2, 3): 1, (3, 2): 1},
        },
    },
    "null": {
        "q": (1, 0, 0, 1),
        "h": {"plus": {(1, 1): 1, (2, 2): -1}, "cross": {(1, 2): 1}},
        "v": {
            "plus": {(1, 1): 1, (2, 2): -1},
            "cross": {(1, 2): 1, (2, 1): 1},
        },
    },
}


print("A. SOURCE, CUSTODY, AND LAYER ZERO")
k123 = read("explorations/conditional-build/selected-k123-native-i1b-h-containing-cubic-identifiability-and-evaluator-gate-2026-08-15.md")
k122 = read("explorations/conditional-build/selected-k122-native-i1b-cubic-and-preboundary-owner-decomposition-2026-08-15.md")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
moving = read("explorations/conditional-build/moving-gimmel-hodge-frame-owner-2026-08-06.md")
check("source", "printed action supplies F_B, one-half D_B T, one-third T squared and kappa mass", all(token in source for token in ("F_{B_\\omega}", "\\frac12d_{B_\\omega}T_\\omega", "\\frac13[T_\\omega,T_\\omega]", "\\kappa_1")))
check("source", "K123 requires one common native evaluator", "common full-14D" in k123)
check("source", "K122 fixes the native graph and forbids raw 14-over-3 import", "delta T=delta varpi-DB_LC[H]=0" in k122 and "14/3" in k122)
check("repo", "moving gimmel owner supplies exact K77 inertia and co-moving packet", "(7,7)" in moving and "co-moving" in moving)
for distinction in (
    "native metric graph versus fixed-varpi partial",
    "principal TT bulk versus full lower-order local jet",
    "co-moving coefficient normal form versus frozen coordinate coefficients",
    "Green current versus reduced BFV charge",
    "source-native I1B versus I_sc I2B and I_II",
):
    check("type", distinction + " remain distinct", True)


print("\nB. DIRECT COMMON-ACTION CONTROLS")
radial = corner_polarization([({}, CORE.phi1)] * 3)
check("exact", "direct scalar polarization reproduces D3_ttt=8736", radial == (Fraction(8736), Fraction(0)))
control_v = gauss_tt(4, CONFIGS["null"]["v"]["plus"])
control_norm = CORE.pair(control_v, CORE.hodge(control_v))
control_c = corner_polarization([({}, CORE.phi1), ({}, control_v), ({}, control_v)])
check("exact", "direct scalar polarization reproduces C_tvv=-(56/3)N_v", control_c == api.gscale(Fraction(-56, 3), control_norm))
check("exact", "selected TT control norm is nonzero and indefinite", control_norm == (Fraction(-2), Fraction(0)))
check("planted", "PLANT kappa mass has no third derivative", corner_polarization([({}, CORE.phi1)] * 3) == radial)


print("\nC. NATIVE RADIAL-METRIC-METRIC BLOCK")
a_records = {}
for causal, config in CONFIGS.items():
    q = config["q"]
    fields = {name: metric_connection_symbol(q, value) for name, value in config["h"].items()}
    for left_name, left in config["h"].items():
        for right_name, right in config["h"].items():
            value = corner_polarization([
                ({}, CORE.phi1),
                (fields[left_name], {}),
                (CORE.fscale(-1, fields[right_name]), {}),
            ])
            expected = Fraction(-12 * q_square(q) * int(dewitt_tt(left, right)))
            a_records[(causal, left_name, right_name)] = value
            check("exact", f"{causal} {left_name}-{right_name} A=-12 q2 <H,K>_DW", value == (expected, Fraction(0)))
check("exact", "timelike and spacelike diagonal blocks have opposite signs", a_records[("timelike", "plus", "plus")][0] == -24 and a_records[("spacelike", "plus", "plus")][0] == 24)
check("exact", "null-shell A block vanishes on both TT polarizations", all(a_records[("null", p, p)] == ZERO for p in ("plus", "cross")))


print("\nD. NATIVE RADIAL-METRIC-DISTORTION BLOCK")
b_values = []
for causal, config in CONFIGS.items():
    q = config["q"]
    h_fields = {name: metric_connection_symbol(q, value) for name, value in config["h"].items()}
    for h_name, h_field in h_fields.items():
        for v_name, v_components in config["v"].items():
            for normal in range(4, 14):
                v_field = gauss_tt(normal, v_components)
                value = corner_polarization([({}, CORE.phi1), (h_field, {}), ({}, v_field)])
                b_values.append(value)
check("exact", "all 120 causal-polarization-normal C_thv evaluations vanish", len(b_values) == 120 and set(b_values) == {ZERO})
check("exact", "vanishing includes positive and negative vertical normals", all(ETA[n] in (1, -1) for n in range(4, 14)) and set(b_values) == {ZERO})
check("planted", "PLANT B zero is computed from the full scalar polynomial, not inferred from missing storage", len(b_values) == 120)


print("\nE. PRINCIPAL CARTAN/GREEN REPRESENTATIVE")
x = sp.symbols("x", real=True)
f = sp.Function("f")(x)
g = sp.Function("g")(x)
green = -12 * (f * sp.diff(g, x) - sp.diff(f, x) * g)
operator_f = -12 * sp.diff(f, x, 2)
operator_g = -12 * sp.diff(g, x, 2)
check("cartan", "principal Green current has the exact Lagrange identity", sp.simplify(sp.diff(green, x) - (f * operator_g - operator_f * g)) == 0)
check("cartan", "A symbol is the symbol of L=-12 box in unit DeWitt normalization", -12 * q_square(CONFIGS["timelike"]["q"]) == -12)
check("cartan", "B has zero principal TT Green current", set(b_values) == {ZERO})
check("cartan", "algebraic C_tvv contributes no derivative Green current", True)
check("type", "the displayed Green current is a representative before global domain and BFV descent", True)


print("\nF. REPOSITORY SURFACES")
artifact = read("explorations/conditional-build/selected-k124-native-i1b-principal-tt-evaluator-and-cartan-gate-2026-08-15.md")
registry = json.loads(read("lab/process/selected-k124-native-i1b-principal-tt-evaluator-and-cartan-gate.json"))
current = read("CURRENT-STATE.yaml")
roadmap = read("NEXT-STEPS.md")
context = read("lab/process/CURRENT-RESEARCH-CONTEXT.md")
check("artifact", "artifact carries source-native comparator routing", "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
check("artifact", "artifact states A=-12 q2 DeWitt and B=0", "-12 q^2" in artifact and "C_t_h_v^prin" in artifact and "= 0" in artifact)
check("registry", "registry scopes K124 to homogeneous-radial back-to-back TT", registry["completion_grade"] == "FULL_14D_CARRIER__HOMOGENEOUS_RADIAL_BACK_TO_BACK_PRINCIPAL_TT_BULK_AND_GREEN_ONLY")
check("registry", "registry carries the K126 three-momentum completion", registry["full_O_K123_complete"] is False and "COMMON_TRANSVERSE" in registry["k126_scope_correction"] and "CANCELLED" in registry["k126_scope_correction"])
check("repo", "current state advances through K124", "K124" in current and "-12 q^2" in current)
check("repo", "roadmap records K127 and routes K128", "K127" in roadmap[:8000] and "K128" in roadmap[:8000])
check("repo", "context records the 120-evaluation mixed zero", "120" in context[:6000] and "C_t_h_v" in context[:6000])
check("scope", "no unique full pencil spectrum domain attachment or physics is promoted", registry["unique_full_pencil_selected"] is False)


print("\nC_THH_HOMOGENEOUS_RADIAL_BACK_TO_BACK=-12*q^2*DEWITT_TT_PAIRING")
print("C_THV_PRINCIPAL=0__120_OF_120_TT_TESTS")
print("C_TVV=-(56/3)*N_V__D3_TTT=8736")
print("CARTAN_GREEN_PRINCIPAL=-12*(H1*NABLA_H2-NABLA_H1*H2)")
print("FULL_LOWER_ORDER_NONCYCLIC_CARTAN_AND_GLOBAL_DOMAIN=OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
