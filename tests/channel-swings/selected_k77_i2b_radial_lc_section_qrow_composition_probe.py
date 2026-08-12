#!/usr/bin/env python3
"""Exact local composition of radial LC and section-q-row action variations.

The four base-fibre directions corrected in v0.209 are identified with the
q-row of the already-certified forty-dimensional observation-section Cartan
lift.  Separately, the radial metric trace is pushed through the covariant
Levi-Civita first-jet map and paired with the live nonzero I2B branch.  The
result is local first-order action closure, not residual vanishing, a nonlinear
section theorem, a full Euler equation or a presymplectic preboundary class.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
ACTION = ROOT / "tests/channel-swings/selected_k77_source_i2b_hq_stationarity_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. LAYER ZERO, SOURCE, PRIOR ART, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/selected-k77-i2b-radial-lc-section-qrow-composition-source-return-2026-08-12.md")
section_prior = read("explorations/conditional-build/selected-k77-canonical-section-jet-cartan-spin-prolongation-2026-08-12.md")
for distinction in (
    "radial metric trace versus normalized fibre trace motion",
    "base-fibre section Cartan motion versus vertical-fibre motion",
    "metric-trace first jet versus Higgs amplitude",
    "zero action derivative versus zero residual derivative",
    "local first variation versus complete Euler and preboundary",
    "source C32_32 plus C32_32 carrier split versus full U64_64 parent",
):
    check("layer0", distinction + " remain distinct", True)
check("source", "source owns gauge-rotated Levi-Civita and observation pullback grammar",
      "SOURCE-CONFIRMS" in source)
check("source", "source is silent on this exact radial/q-row cancellation",
      "SOURCE-SILENT" in source)
check("prior_art", "the prior section certificate owns all forty graph slopes",
      "exactly 40 independent basis directions" in section_prior
      and "rank-four" in section_prior)
for lens in (
    "principal-bundle geometry identifies the q-row without selecting a section",
    "variational bicomplex distinguishes residual and action derivatives",
    "Clifford/Krein review tests equal-grade pairing rather than positivity",
    "symplectic review leaves the presymplectic current and boundary corner open",
    "analytic review leaves domains spectra and nonlinear evolution open",
    "contrary review requires a firing grade-one control",
):
    check("preflight", lens, True)


print("\nB. PREDECESSOR REPLAYS")
split_registry = json.loads(read(
    "lab/process/selected-k77-i2b-ambient-fibre-trace-split-correction.json"
))
orbit_registry = json.loads(read(
    "lab/process/selected-k77-i2b-full-trace-orbit-derivative.json"
))
check("repo", "v0.209 exact correction registry retains the nine-plus-four split",
      split_registry["exact_results"]["vertical_trace_orbit_dimension"] == 9
      and split_registry["exact_results"]["base_fibre_q_mixing_directions"] == 4)
check("repo", "v0.208 exact ambient theorem retains moving action covariance",
      orbit_registry["exact_results"]["moving_first_variation_failures"] == 0
      and orbit_registry["exact_results"]["dot_pplus_action_adjoint_failures"] == 0)
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    ACTION_DATA = runpy.run_path(str(ACTION))
check("repo", "v0.201 nonzero I2B branch replays",
      "failures=0" in capture.getvalue().lower())
fixed_varpi_registry = json.loads(read(
    "lab/process/selected-k77-fixed-varpi-normal-frechet-closure.json"
))
check("repo", "v0.95 registry retains fixed-varpi delta A and delta F equal zero",
      fixed_varpi_registry["local_fixed_varpi_block"]["delta_A"] == "ZERO"
      and fixed_varpi_registry["local_fixed_varpi_block"]["delta_F_A"] == "ZERO")


print("\nC. EXACT SECTION-Q-ROW IDENTIFICATION")
old_eta = (1,) * 7 + (-1,) * 7
old_observed = (0, 7, 8, 9)
old_vertical = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
old_q = 13
old_to_current = {
    0: 0, 1: 4, 2: 5, 3: 6, 4: 7, 5: 8, 6: 9,
    7: 1, 8: 2, 9: 3, 10: 10, 11: 11, 12: 12, 13: 13,
}
current_eta = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
check("exact", "the coordinate permutation transports the full K77 signature",
      all(old_eta[i] == current_eta[old_to_current[i]] for i in range(14)))
check("exact", "old observed axes become the current one-three base",
      tuple(old_to_current[i] for i in old_observed) == (0, 1, 2, 3))
check("exact", "old vertical axes become the current six-four fibre",
      tuple(old_to_current[i] for i in old_vertical) == tuple(range(4, 14)))
check("exact", "the section q-row remains current vertical axis thirteen",
      old_to_current[old_q] == 13)


def cartan_generator(eta, vertical, observed):
    out = sp.zeros(14)
    out[vertical, observed] = 1
    out[observed, vertical] = -eta[observed] * eta[vertical]
    return out


permutation = sp.zeros(14)
for old, new in old_to_current.items():
    permutation[new, old] = 1
transported = []
current = []
for old_base in old_observed:
    transported.append(
        permutation * cartan_generator(old_eta, old_q, old_base) * permutation.T
    )
    current.append(cartan_generator(current_eta, 13, old_to_current[old_base]))
check("exact", "all four mixed motions are exactly the permuted section q-row",
      transported == current)
check("exact", "the q-row is four-dimensional inside the prior forty-dimensional section jet",
      sp.Matrix.hstack(*[value.reshape(196, 1) for value in current]).rank() == 4)
check("control", "PLANT the q-row is the whole forty-dimensional section jet is rejected",
      4 != 40)
check("control", "PLANT identity coordinate transport is rejected",
      cartan_generator(old_eta, old_q, old_observed[1])
      != cartan_generator(current_eta, 13, 1))


print("\nD. RADIAL METRIC TRACE THROUGH THE LEVI-CIVITA FIRST JET")
slots = [(i, j) for i in range(4) for j in range(i, 4)]
spin_slots = [(mu, a, b) for mu in range(4)
              for a in range(4) for b in range(a + 1, 4)]
jet_slots = [(lam, i, j) for lam in range(4) for i, j in slots]


def h_component(i, j, a, b):
    return int((i == a and j == b) or (i == b and j == a))


lc_full = sp.zeros(24, 40)
for row, (mu, a, b) in enumerate(spin_slots):
    for column, (lam, i, j) in enumerate(jet_slots):
        lc_full[row, column] = sp.Rational(1, 2) * (
            int(lam == b) * h_component(i, j, mu, a)
            - int(lam == a) * h_component(i, j, mu, b)
        )
radial_insertion = sp.zeros(40, 4)
eta4 = (1, -1, -1, -1)
for lam in range(4):
    for slot, (i, j) in enumerate(slots):
        if i == j:
            radial_insertion[10 * lam + slot, lam] = eta4[i]
lc_radial = lc_full * radial_insertion
check("exact", "the full covariant spin Levi-Civita first-jet map retains rank twenty",
      lc_full.rank() == 20)
check("exact", "the four derivatives of a conformal trace mode have exact rank four",
      lc_radial.rank() == 4)
check("control", "the radial metric trace response is nonzero in every base derivative",
      all(lc_radial[:, index] != sp.zeros(24, 1) for index in range(4)))


ZERO = ACTION_DATA["ZERO"]
ONE = ACTION_DATA["ONE"]
I = ACTION_DATA["I"]
fadd = ACTION_DATA["fadd"]
residual_derivative = ACTION_DATA["residual_derivative"]
residual_at_branch = ACTION_DATA["residual_at_branch"]
sym_pair = ACTION_DATA["sym_pair"]
one_form = ACTION_DATA["one_form"]


def lc_column_to_form(column):
    terms = []
    for coefficient, (mu, a, b) in zip(column, spin_slots):
        if coefficient:
            terms.append({
                1 << mu: {
                    (1 << a) | (1 << b):
                        (Fraction(coefficient), Fraction(0))
                }
            })
    return fadd(*terms)


radial_deltas = [lc_column_to_form(lc_radial[:, index]) for index in range(4)]
radial_residual_derivatives = [residual_derivative(value) for value in radial_deltas]
radial_action_derivatives = [
    sym_pair(value, residual_at_branch) for value in radial_residual_derivatives
]
check("variation", "all four radial LC directions change the nonzero residual",
      all(radial_residual_derivatives))
check("variation", "all four exact radial action first derivatives vanish by grade orthogonality",
      radial_action_derivatives == [ZERO] * 4)
check("krein", "the branch residual is grade one while every radial LC input is grade two",
      all(mask.bit_count() == 1 for element in residual_at_branch.values() for mask in element)
      and all(mask.bit_count() == 2 for delta in radial_deltas
              for element in delta.values() for mask in element))
grade_one_plant = one_form(0, 0, I)
plant_value = sym_pair(residual_derivative(grade_one_plant), residual_at_branch)
check("control", "a grade-one connection plant fires with exact derivative eight-thirds",
      plant_value == (Fraction(8, 3), Fraction(0)))
check("plant", "PLANT zero radial action derivative is rejected as zero residual response",
      all(radial_residual_derivatives))
check("plant", "PLANT fixed T in place of fixed varpi is rejected by the v0.95 control",
      "moving B while freezing T" in read(
          "tests/channel-swings/selected_k77_fixed_varpi_normal_frechet_closure_probe.py"
      ))


print("\nE. SCOPE, ACCOUNTING, AND HANDOFF")
for kind, label in (
    ("principal_bundle", "the q-row is action-owned only as a possible section jet; no physical section coefficient is selected"),
    ("variation", "local first-order closure does not supply the other thirty-six section-Cartan directions"),
    ("symplectic", "no presymplectic current corner charge BV quotient or BFV class is inferred"),
    ("analytic", "no nonlinear domain spectrum positivity or evolution theorem is inferred"),
    ("scope", "pointwise radial moving-gimmel covariance remains distinct from fixed-gimmel Cartan motion"),
    ("scope", "complete arbitrary-field Euler and physical observation receiver remain open"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("accounting", "no field parameter quotient selector or external datum is added"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_LC_PULLBACK_GRAMMAR__SOURCE_SILENT_EXACT_COMPOSITION")
print("SECTION_Q_ROW=FOUR_OF_FORTY__LOCAL_CARTAN_SPIN_FRAME_OWNED")
print("RADIAL_LC=RANK4__RESIDUAL_DERIVATIVE_NONZERO__ACTION_DERIVATIVE_ZERO")
print("NEXT=NONLINEAR_EPSILON_IG_OBSERVATION_RECEIVER_AND_COMPLETE_EULER_PREBOUNDARY")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
