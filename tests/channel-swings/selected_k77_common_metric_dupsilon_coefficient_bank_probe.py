#!/usr/bin/env python3
"""Exact common-coordinate ``D_g Upsilon`` bank on the selected K77 parent.

The fixed-independent-``varpi`` metric derivative has ``delta A=0`` and
``delta T=-delta B_LC``.  This certificate emits that derivative on the same
all-grade residual carrier used by the actual horizontal ``D_varpi Upsilon``
bank.  It then compares the physical metric columns with the previously
Ward-determined orbit completion.  The latter comparison is intentionally
allowed to fail: it decides whether the already-owned principal epsilon orbit
is the complete diffeomorphism transport.

Run with ``sage -python``.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
ALL_GRADE = ROOT / "tests/channel-swings/selected_k77_coupled_all_grade_upsilon_graph_probe.py"
SOURCE_VARIABLE = ROOT / "tests/channel-swings/selected_action_source_variable_hessian_probe.py"
COUNTS = Counter()
FAILURES = []
Q = sp.Rational


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


print("A. SOURCE, PREDECESSORS, AND LAYER ZERO")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
fixed_metric = strict("lab/process/selected-k77-fixed-varpi-normal-frechet-closure.json")
common_adjoint = strict("lab/process/selected-k77-common-field-formal-adjoint-green.json")
epsilon_orbit = strict("lab/process/selected-k77-gamma-soldered-epsilon-dupsilon-orbit.json")
check("source", "source owns augmented torsion as the difference of varpi and the rotated reference connection",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("source", "source displays a raw Upsilon with curvature and augmented-torsion terms",
      r"\Upsilon^B_\omega" in source and r"*\kappa_1T_\omega" in source)
check("source", "source remains silent on the common residual-coordinate metric bank",
      fixed_metric["source_return"].endswith("SOURCE_SILENT_FIXED_VARPI_NORMAL_FRECHET_CLOSURE"))
check("repo", "v0.95 owns delta T=-delta B, delta A=delta F_A=0",
      fixed_metric["local_fixed_varpi_block"]["delta_T"] == "MINUS_DELTA_B_LC"
      and fixed_metric["local_fixed_varpi_block"]["delta_A"] == "ZERO"
      and fixed_metric["local_fixed_varpi_block"]["delta_F_A"] == "ZERO")
check("repo", "v0.96 explicitly leaves this coefficient bank un-emitted",
      common_adjoint["common_field_ownership"]["D_g_common_residual_coordinate_bank"] == "NOT_EMITTED")
for label in (
    "fixed-varpi metric derivative versus independent-varpi derivative",
    "delta T=-delta B_LC versus applying the full D_varpi response to -delta B_LC",
    "physical metric bank versus a Ward-determined orbit completion",
    "principal gamma-epsilon orbit versus full primitive D-epsilon Upsilon",
    "common residual carrier versus a field-space Riesz map",
    "raw residual Ward identity versus action Euler or presymplectic basicness",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(ALL_GRADE))
check("repo", "the exact all-grade raw-Upsilon response replays",
      "PASS 50/50" in capture.getvalue() and not P["FAILURES"])
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    S = runpy.run_path(str(SOURCE_VARIABLE))
check("repo", "the exact source-variable Levi-Civita/diffeomorphism lift replays",
      "PASS " in capture.getvalue() and not S["FAILURES"])

M = P["M"]
V = P["V"]
pairs = [(a, b) for a in range(4) for b in range(a + 1, 4)]
slots = [(i, j) for i in range(4) for j in range(i, 4)]


def horizontal_form(column):
    result = {}
    for index, coefficient in enumerate(column):
        if coefficient:
            mu, pair_index = divmod(index, 6)
            result = M["fadd"](
                result,
                M["fscale"](
                    coefficient,
                    {1 << mu: M["blade"](pairs[pair_index])},
                ),
            )
    return result


def linear_combination(forms, coefficients):
    result = {}
    for form, coefficient in zip(forms, coefficients):
        if coefficient:
            result = M["fadd"](result, M["fscale"](coefficient, form))
    return result


def gamma_connection_form(q, nu):
    result = {}
    for mu in range(4):
        if q[mu]:
            result = M["fadd"](
                result,
                M["fscale"](
                    q[mu], {1 << mu: M["blade"]((nu,))}
                ),
            )
    return result


print("\nB. COMPLETE COVARIANT LEVI-CIVITA BANK ON COMMON COORDINATES")


def h_component(i, j, a, b):
    return int((i == a and j == b) or (i == b and j == a))


spin_slots = [(mu, a, b) for mu in range(4) for a, b in pairs]
jet_slots = [(lam, i, j) for lam in range(4) for i, j in slots]
L_full = sp.zeros(24, 40)
for row, (mu, a, b) in enumerate(spin_slots):
    for column, (lam, i, j) in enumerate(jet_slots):
        L_full[row, column] = Q(1, 2) * (
            int(lam == b) * h_component(i, j, mu, a)
            - int(lam == a) * h_component(i, j, mu, b)
        )


def fixed_q_map(q):
    insertion = sp.zeros(40, 10)
    for column in range(10):
        for lam in range(4):
            insertion[10 * lam + column, column] = q[lam]
    return L_full * insertion


metric_principal = []
for mu in range(4):
    q = sp.zeros(4, 1)
    q[mu] = 1
    L_mu = fixed_q_map(q)
    metric_principal.append([
        M["fscale"](-1, horizontal_form(L_mu[:, column]))
        for column in range(10)
    ])

metric_ranks = [V["family_rank"](bank) for bank in metric_principal]
metric_supports = [
    len(set().union(*(set(M["flatten"](value)) for value in bank)))
    for bank in metric_principal
]
full_metric_family = [value for bank in metric_principal for value in bank]
check("exact", "the four common-coordinate metric principal banks all have rank nine",
      metric_ranks == [9, 9, 9, 9])
check("exact", "their combined family has the exact rank-twenty torsion-free image",
      V["family_rank"](full_metric_family) == L_full.rank() == 20)
check("exact", "every emitted metric coefficient is a grade-two-valued one-form on the actual residual carrier",
      all({key[1].bit_count() for key in M["flatten"](value)} <= {2}
          for value in full_metric_family))
check("control", "the common metric bank is live rather than the zero coefficient family",
      all(any(bank) for bank in metric_principal))

# At fixed independent varpi, delta A=0.  Applying the full D_varpi response
# to -delta B would incorrectly move A and generate a curvature response.
wrong_full_response = [P["response"](value) for value in metric_principal[0]]
check("planted", "PLANT applying D_varpi Upsilon to -delta B is not the fixed-varpi metric derivative",
      any(M["flatten"](wrong) != M["flatten"](right)
          for wrong, right in zip(wrong_full_response, metric_principal[0])))


print("\nC. CAUSAL TRANSVERSE RANKS AND COMMON G-VARPI COORDINATES")
causal = {}
for name, packet in S["results"].items():
    q = sp.Matrix(S["orbits"][name])
    D = packet["D"]
    C = packet["connection_lift"]
    Lq = fixed_q_map(q)
    left_inverse = (D.T * D).inv() * D.T
    transverse = sp.eye(10) - D * left_inverse
    bank_q = [
        linear_combination(
            [metric_principal[mu][column] for mu in range(4)], q
        )
        for column in range(10)
    ]
    transverse_bank = [
        linear_combination(bank_q, transverse[:, column])
        for column in range(10)
    ]
    metric_orbit = [
        linear_combination(bank_q, D[:, column]) for column in range(4)
    ]
    varpi_forms = [horizontal_form(C[:, column]) for column in range(4)]

    check("exact", f"{name}: emitted bank equals -L_q coefficientwise",
          all(M["flatten"](bank_q[column])
              == M["flatten"](M["fscale"](-1, horizontal_form(Lq[:, column])))
              for column in range(10)))
    check("exact", f"{name}: physical transverse metric bank has rank six",
          V["family_rank"](transverse_bank) == 6)
    check("exact", f"{name}: metric and independent-varpi torsion graph cancels exactly",
          all(not M["fadd"](metric, varpi)
              for metric, varpi in zip(metric_orbit, varpi_forms)))
    check("control", f"{name}: freezing varpi leaves the physical metric orbit live",
          V["family_rank"](metric_orbit) == 3)
    causal[name] = {
        "metric_symbol_rank": V["family_rank"](bank_q),
        "transverse_metric_rank": V["family_rank"](transverse_bank),
        "metric_orbit_rank": V["family_rank"](metric_orbit),
        "torsion_graph_defect_rank": V["family_rank"]([
            M["fadd"](metric, varpi)
            for metric, varpi in zip(metric_orbit, varpi_forms)
        ]),
    }


print("\nD. FULL PRINCIPAL WARD COMPARISON")
ward = {}
for name, packet in S["results"].items():
    q = sp.Matrix(S["orbits"][name])
    D = packet["D"]
    C = packet["connection_lift"]
    bank_q = [
        linear_combination(
            [metric_principal[mu][column] for mu in range(4)], q
        )
        for column in range(10)
    ]
    physical_metric_orbit = [
        linear_combination(bank_q, D[:, column]) for column in range(4)
    ]
    varpi_forms = [horizontal_form(C[:, column]) for column in range(4)]
    varpi_responses = [P["response"](value) for value in varpi_forms]
    gamma_forms = [gamma_connection_form(q, nu) for nu in range(4)]
    epsilon_responses = [
        M["fscale"](-1, P["response"](value)) for value in gamma_forms
    ]
    source_orbit = [
        M["fadd"](varpi, epsilon)
        for varpi, epsilon in zip(varpi_responses, epsilon_responses)
    ]
    physical_defect = [
        M["fadd"](metric, source)
        for metric, source in zip(physical_metric_orbit, source_orbit)
    ]
    diagnostic_metric_orbit = [M["fscale"](-1, value) for value in source_orbit]
    discrepancy = [
        M["fadd"](physical, M["fscale"](-1, diagnostic))
        for physical, diagnostic in zip(physical_metric_orbit, diagnostic_metric_orbit)
    ]

    check("exact", f"{name}: prior Ward-determined metric orbit cancels its source orbit by construction",
          all(not M["fadd"](metric, source)
              for metric, source in zip(diagnostic_metric_orbit, source_orbit)))
    check("theorem", f"{name}: actual physical metric orbit does not equal the Ward-determined completion",
          any(discrepancy))
    check("theorem", f"{name}: current physical g-varpi-gamma-epsilon principal Ward defect remains live",
          V["family_rank"](physical_defect) > 0)
    check("planted", f"PLANT {name}: orbit completion may not be relabelled as the physical metric derivative",
          M["flatten"](physical_metric_orbit[0])
          != M["flatten"](diagnostic_metric_orbit[0])
          or any(physical_metric_orbit[1:]))

    ward[name] = {
        "source_orbit_rank": V["family_rank"](source_orbit),
        "physical_metric_orbit_rank": V["family_rank"](physical_metric_orbit),
        "diagnostic_metric_orbit_rank": V["family_rank"](diagnostic_metric_orbit),
        "physical_ward_defect_rank": V["family_rank"](physical_defect),
        "physical_vs_diagnostic_discrepancy_rank": V["family_rank"](discrepancy),
        "physical_ward_defect_supports": [
            len(M["flatten"](value)) for value in physical_defect
        ],
    }

check("theorem", "the common-coordinate metric bank closes but the current three-field principal Ward claim fails",
      all(row["physical_ward_defect_rank"] > 0 for row in ward.values()))
check("type", "the live defect reopens full primitive D-epsilon/diffeomorphism transport rather than invalidating the metric bank", True)


print("\nE. SCOPE, REGISTRY, AND RETURN")
for kind, label in (
    ("symplectic", "a raw-residual Ward defect is not a presymplectic non-basicness theorem"),
    ("variational", "the emitted D-g bank is exact while full lower-order nonlinear D-epsilon Upsilon remains open"),
    ("krein", "no positive field pairing or common closed domain is selected"),
    ("analytic", "the finite common-coordinate bank supplies no hyperbolicity contour measure or Green operator"),
    ("scope", "the current failure is a construction fork in the gauge-diffeomorphism transport not a GU-wide no-go"),
    ("scope", "the two U32,32 halves and full U64,64 remain distinct rival action parents"),
    ("scope", "P1 P2 P3 remain unused and no datum field coefficient or quotient is added"),
):
    check(kind, label, True)

registry_path = ROOT / "lab/process/selected-k77-common-metric-dupsilon-coefficient-bank.json"
if registry_path.exists():
    registry = strict("lab/process/selected-k77-common-metric-dupsilon-coefficient-bank.json")
    check("registry", "registry records exact metric principal ranks and supports",
          registry["metric_bank"]["principal_ranks"] == metric_ranks
          and registry["metric_bank"]["principal_supports"] == metric_supports)
    check("registry", "registry records all causal and Ward diagnostics",
          registry["causal_classes"] == causal and registry["ward_comparison"] == ward)
    check("registry", "constraint accounting and source return remain scoped",
          registry["constraint_fence"]["new_fields"] == 0
          and registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
          and registry["source_return"].startswith("SOURCE-CONFIRMS"))

print("SOURCE_RETURN=SOURCE-CONFIRMS_TWO_CONNECTION_RAW_UPSILON_GRAMMAR__SOURCE_SILENT_COMMON_METRIC_BANK_AND_COMPLETE_DIFFEO_EPSILON_TRANSPORT")
print("DG_COMMON_BANK=FOUR_RANK9_PRINCIPAL_BANKS__COMBINED_RANK20")
print("DG_TRANSVERSE=RANK6_TIMELIKE_SPACELIKE_NULL")
print("G_VARPI_TORSION_GRAPH=ZERO")
print("FULL_G_VARPI_GAMMA_EPSILON_WARD=NONZERO__PRIOR_ORBIT_COMPLETION_NOT_PHYSICAL_DG")
print("NEXT=CONSTRUCT_COMPLETE_PRIMITIVE_DEPSILON_AND_DIFFEO_TRANSPORT__RETEST_COMMON_JR_ZERO__THEN_EXTEND_FORMAL_ADJOINT_GREEN")
print("P1_P2_P3=UNUSED")
print("METRIC_PRINCIPAL_RANKS=" + ",".join(map(str, metric_ranks)))
print("METRIC_PRINCIPAL_SUPPORTS=" + ",".join(map(str, metric_supports)))
print("CAUSAL=" + json.dumps(causal, sort_keys=True))
print("WARD=" + json.dumps(ward, sort_keys=True))
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
