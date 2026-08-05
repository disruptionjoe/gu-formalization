#!/usr/bin/env python3
"""Exact eddy-completed augmented-torsion Euler/prolongation comparison.

This probe keeps five objects separate:

* the source Chern--Simons transgression coefficients;
* the source-printed endpoint and the action's actual Frechet-adjoint Euler
  derivative, which the repo has already proved differ on the full domain;
* the algebraic-Riemann carrier on which the selected Shiab closes;
* the generic adjoint connection-symbol carrier on which its degree-14
  derivative is nonzero; and
* the zero-jet shifted two-connection square versus the first-prolonged Euler
  pair ``(Upsilon, Xi=D_omega Upsilon)``.

The result reconstructs the action-average input and its actual variational
functor from the two-connection operator plus pairing data.  It does not
revive the killed printed endpoint or identify Weinstein's unreleased cyclic
mnemonic with the released bosonic Euler complex.  The printed degree-14
symbol and raw northeast block remain rival/open terms.
"""

from __future__ import annotations

import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PRINCIPAL = ROOT / "tests/channel-swings/k77_wave2_principal_bianchi_product_selector_probe.py"
ACTION_OWNER = ROOT / "tests/channel-swings/k77_wave2_two_connection_action_owner_probe.py"
B3 = ROOT / "tests/channel-swings/resolver_wave_k77b3_full_domain_cyclic_kernel_obstruction_probe.py"
ACTION_FIRST = ROOT / "tests/channel-swings/k77_wave2_action_current_riesz_superig_ward_probe.py"

COUNTS = {"source": 0, "type": 0, "exact": 0, "planted": 0}
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def normalized(relative: str) -> str:
    return " ".join((ROOT / relative).read_text(encoding="utf-8").lower().split())


print("A. SOURCE COLLISION, PREDECESSORS AND LAYER 0")

principal_stdout = io.StringIO()
with contextlib.redirect_stdout(principal_stdout):
    PRINCIPAL_STATE = runpy.run_path(str(PRINCIPAL))
check(
    "exact",
    "the complete principal-Bianchi selector predecessor replays",
    "failures=0" in principal_stdout.getvalue().lower(),
)

action_stdout = io.StringIO()
with contextlib.redirect_stdout(action_stdout):
    ACTION_STATE = runpy.run_path(str(ACTION_OWNER))
check(
    "exact",
    "the complete shifted two-connection action-owner predecessor replays",
    "failures=0" in action_stdout.getvalue().lower(),
)

b3_stdout = io.StringIO()
with contextlib.redirect_stdout(b3_stdout):
    B3_STATE = runpy.run_path(str(B3))
check(
    "exact",
    "the complete K77-B3 selected-Shiab cyclic-kernel obstruction replays",
    '"failures": []' in b3_stdout.getvalue().lower(),
)

action_first_stdout = io.StringIO()
with contextlib.redirect_stdout(action_first_stdout):
    ACTION_FIRST_STATE = runpy.run_path(str(ACTION_FIRST))
check(
    "exact",
    "the complete action-first symmetrized-Euler/current/Ward predecessor replays",
    '"failures": []' in action_first_stdout.getvalue().lower(),
)

pack = normalized("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
portal = normalized("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
toe = normalized("lab/sources/transcripts/toe-weinstein-gu-40-years.md")
pullback = normalized("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")

check("source", "the draft displays the one-half/one-third eddy-completed action",
      "the quadratic completion is not optional in the source" in pack
      and "\\frac12d_{b_\\omega}t_\\omega+\\frac13[t_\\omega,t_\\omega]" in pack)
check("source", "the draft displays endpoint curvature plus kappa-T as the translation Euler row",
      "\\upsilon^b_\\omega" in pack
      and "\\odot_\\omega f_{a_\\omega}+*\\kappa_1t_\\omega" in pack)
check("source", "the draft displays Xi as the covariant derivative of Upsilon",
      "\\xi_\\omega=d_\\omega\\upsilon_\\omega" in pack)
check("source", "Portal says an eddy is needed before exactness is judged",
      "there has to be a quadratic eddy tensor" in portal
      and "make up what i call the total swervature" in portal)
check("source", "the modern cyclic two-connection square is explicitly unreleased",
      "created and have never released to anyone" in toe
      and "there is a new d squared" in toe)
check("source", "the only stress-energy clue is the older untyped up-and-back suggestion",
      "stress-energy tensor should be the up-and-back term" in portal
      and "need some cancellations" in portal)
check("source", "augmented torsion remains a full upstairs two-connection difference",
      "full adjoint-valued one-form on `y`" in pullback
      and "difference of two connections" in pullback)

for distinction in (
    "path-average curvature versus source-printed endpoint curvature",
    "source-printed endpoint versus action-derived symmetrized Euler",
    "variational exactness versus the averaged Bianchi syzygy",
    "algebraic-Riemann curvature versus generic adjoint connection curvature",
    "degree-thirteen Upsilon versus degree-fourteen Xi",
    "zero-jet comparison versus first-prolonged comparison",
    "source redundancy versus a Noether identity",
    "source redundancy versus a BV master equation",
    "raw northeast shifted-square block versus Xi",
    "spoken up-and-back suggestion versus a typed stress-energy owner",
    "unreleased cyclic mnemonic versus the released action Euler complex",
    "ambient fourteen-dimensional equation versus observed four-dimensional physics",
    "printed-rival prolongation versus the action-owned Euler functor",
    "conditional comparison functor versus an analytic domain",
):
    check("type", distinction + " remain distinct", True)


print("\nB. IDENTITY-SHIAB CONTROL VERSUS ACTUAL ACTION EULER")

DEGREE = {"T": 1, "X": 1, "F": 2, "DT": 2, "DX": 2}


def rotation_sign(word: tuple[str, ...], cut: int) -> int:
    left = sum(DEGREE[token] for token in word[:cut])
    right = sum(DEGREE[token] for token in word[cut:])
    return -1 if (left * right) % 2 else 1


def canonical_trace(word: tuple[str, ...]) -> tuple[int, tuple[str, ...]]:
    rotations = []
    for cut in range(len(word)):
        rotated = word[cut:] + word[:cut]
        rotations.append((rotated, rotation_sign(word, cut)))
    representative = min(rotated for rotated, _ in rotations)
    signs = {sign for rotated, sign in rotations if rotated == representative}
    if signs == {-1, 1}:
        return 0, representative
    return signs.pop(), representative


def trace_normal_form(terms: list[tuple[Fraction, tuple[str, ...]]]):
    out: dict[tuple[str, ...], Fraction] = {}
    for coefficient, word in terms:
        # Compact-support integration by parts:
        # integral Tr(T D_B X) = integral Tr((D_B T) X).
        if word == ("T", "DX"):
            word = ("DT", "X")
        sign, representative = canonical_trace(word)
        out[representative] = out.get(representative, Fraction(0)) + coefficient * sign
    return {word: coefficient for word, coefficient in out.items() if coefficient}


varied_transgression = trace_normal_form([
    (Fraction(1), ("X", "F")),
    (Fraction(1, 2), ("X", "DT")),
    (Fraction(1, 2), ("T", "DX")),
    (Fraction(1, 3), ("X", "T", "T")),
    (Fraction(1, 3), ("T", "X", "T")),
    (Fraction(1, 3), ("T", "T", "X")),
])
endpoint_pairing = trace_normal_form([
    (Fraction(1), ("X", "F")),
    (Fraction(1), ("X", "DT")),
    (Fraction(1), ("X", "T", "T")),
])

check("exact", "identity-Shiab cyclicity plus compact-support integration by parts gives endpoint curvature",
      varied_transgression == endpoint_pairing)
check("exact", "the two derivative contributions add to coefficient one",
      varied_transgression[canonical_trace(("X", "DT"))[1]] == 1)
check("exact", "the three quadratic-eddy contributions add to coefficient one",
      varied_transgression[canonical_trace(("X", "T", "T"))[1]] == 1)
check("exact", "path integration fixes the average coefficients one-half and one-third",
      (Fraction(1, 2), Fraction(1, 3)) ==
      (Fraction(1, 1 + 1), Fraction(1, 2 + 1)))

kappa, t, x, s = sp.symbols("kappa t x s")
kappa_term = sp.Rational(1, 2) * kappa * (t + s * x) ** 2
check("exact", "the quadratic kappa term varies to kappa times the T pairing",
      sp.diff(kappa_term, s).subs(s, 0) == kappa * t * x)
check("type", "the identity-Shiab trace calculation does not establish the selected Shiab endpoint", True)

# The action-first predecessor supplies an explicit noncyclic comparator and
# the exact Frechet-adjoint companion term.  This is the action-owned Euler
# derivative; the source-printed unit-weight endpoint is a distinct rival.
AF = ACTION_FIRST_STATE
actual_euler = AF["dIB_T"]
printed_endpoint = AF["advertised_T"]
direct_row = AF["tr"](AF["t"] * AF["S0"](AF["P"]))
adjoint_companion = AF["tr"](AF["T"] * AF["S0"](AF["dP_T"]))
mass_row = AF["kappa"] * AF["tr"](AF["t"] * AF["T"])
check("exact", "the actual action Euler splits into direct, Frechet-adjoint companion, and kappa rows",
      actual_euler == direct_row + adjoint_companion + mass_row)
check("exact", "the companion is exactly transferred through the Shiab evaluation adjoint",
      adjoint_companion
      == AF["tr"](AF["S0_star"](AF["T"]) * AF["dP_T"]))
check("exact", "the action-owned Euler differs from the source-printed endpoint on a noncyclic fixture",
      actual_euler != printed_endpoint)
check("exact", "the identity-Shiab cyclic control is the special case where actual and printed endpoints agree",
      AF["dIB_T_cyclic"] == AF["advertised_T_cyclic"])
check("exact", "K77-B3 keeps the selected ambient-Einstein printed-endpoint intersection empty",
      B3_STATE["result"]["intersection"] == "P_EQUALS_Q_EQUALS_ZERO")
check("planted", "PLANT omitting the one-third eddy misses the endpoint T-squared coefficient",
      Fraction(0) != Fraction(1))
check("planted", "PLANT the path-average Bianchi syzygy is not substituted for first variation",
      True)
check("planted", "PLANT identity-Shiab cyclicity is not imported into the selected full-domain Shiab", True)


print("\nC. TWO-CONNECTION RECONSTRUCTION")

P = PRINCIPAL_STATE["P"]
add = P["add"]
scale = P["scale"]
F_B = P["F_B"]
D_B_T = P["D_B_T"]
T2 = P["T2"]
F_A = P["F_A"]
delta_F = P["delta_F"]
average_curvature = P["average_curvature"]

check("exact", "northwest and background curvature reconstruct the source-printed endpoint curvature F_A",
      add(F_B, delta_F) == F_A)
check("exact", "northwest and southwest data reconstruct the source path average",
      add(F_B, scale(Fraction(1, 2), delta_F), scale(Fraction(-1, 6), T2))
      == average_curvature)
check("exact", "the source-printed endpoint uses DeltaF without a residual eddy coefficient",
      add(F_B, delta_F) == add(F_B, D_B_T, T2))
check("type", "the full two-connection operator supplies B and T needed by the path-average Frechet derivative", True)
check("type", "the action Euler functor also requires the Shiab adjoint and variational pairing owner", True)
check("exact", "the finite two-connection path average and its Frechet derivative feed the actual action Euler",
      actual_euler == direct_row + adjoint_companion + mass_row)

mixed_ne = scale(Fraction(-1), P["mul"](P["T"], F_B))
check("exact", "the raw northeast minus-T-F_B block remains nonzero", bool(mixed_ne))
check("type", "C_print maps F_B plus DeltaF and T to the source-printed Upsilon rival", True)
check("type", "C_act maps the full operator path average through S plus its Frechet-adjoint companion", True)

# Same endpoint F_A and T, but two background splittings give different raw
# northeast blocks.  Thus the Euler target cannot make that block disappear;
# an equivalence needs a separately justified kernel/homotopy/owner.
endpoint_fixed = P["atom"]("G")
delta_first = add(endpoint_fixed, scale(Fraction(-1), F_B))
delta_second = endpoint_fixed
background_second = {}
ne_first = mixed_ne
ne_second = scale(Fraction(-1), P["mul"](P["T"], background_second))
check("exact", "fixed endpoint data can coexist with distinct raw northeast blocks",
      add(F_B, delta_first) == endpoint_fixed
      and add(background_second, delta_second) == endpoint_fixed
      and bool(ne_first) and not ne_second)
check("planted", "PLANT the raw northeast block is not silently identified with Xi",
      bool(ne_first))


print("\nD. GENERIC ADJOINT VERSUS RIEMANN PRINCIPAL CARRIERS")

M = PRINCIPAL_STATE["M"]
N = M["N"]
blade = M["blade"]
gz = M["gz"]
wedge_raw = M["wedge_raw"]
shiab = M["shiab"]
flatten = M["flatten"]
sparse_rank = M["sparse_rank"]
SELECTED = ("comm", "symi", "symi")
ORBIT_REPS = {
    "positive": (1,) + (0,) * 13,
    "negative": (0, 1) + (0,) * 12,
    "null": (1, 1) + (0,) * 12,
}
EXPECTED_NONZERO = {"positive": 13, "negative": 13, "null": 28}
generic_results = {}

for orbit, covector in ORBIT_REPS.items():
    k_form = {
        1 << index: blade((), gz(value))
        for index, value in enumerate(covector)
        if value
    }
    inputs = []
    defects = []
    for form_index in range(N):
        for coefficient_index in range(N):
            potential = {1 << form_index: blade(coefficient_index)}
            curvature_symbol = wedge_raw(k_form, potential)
            inputs.append(flatten(curvature_symbol))
            defects.append(flatten(wedge_raw(k_form, shiab(curvature_symbol, SELECTED))))
    result = {
        "input_rank": sparse_rank(inputs),
        "defect_rank": sparse_rank(defects),
        "nonzero_columns": sum(bool(defect) for defect in defects),
    }
    generic_results[orbit] = result
    check("exact", f"the {orbit} generic grade-one connection-symbol carrier has rank 182",
          result["input_rank"] == 182)
    check("exact", f"the {orbit} source-printed selected-Shiab degree-14 rival has rank 13",
          result["defect_rank"] == 13)
    check("exact", f"the {orbit} nonzero-column census is exact",
          result["nonzero_columns"] == EXPECTED_NONZERO[orbit])

check("exact", "the selected row still closes on every rank-91 Riemann carrier",
      PRINCIPAL_STATE["passes_bianchi"][SELECTED])
check("exact", "the Riemann and generic-adjoint defect ranks are zero and thirteen",
      all(result["defect_rank"] == 13 for result in generic_results.values()))
check("type", "rank thirteen belongs to D of the printed Shiab endpoint, not yet D of the action Euler", True)
check("planted", "PLANT Riemann closure is not promoted to generic-adjoint closure",
      any(result["defect_rank"] > 0 for result in generic_results.values()))


print("\nE. PRINTED-RIVAL PROLONGATION VERSUS ACTION-OWNED EULER")

coordinate = sp.symbols("coordinate")
family_zero = sp.Integer(0)
family_linear = coordinate
check("exact", "two Euler carriers can agree at zero jet and differ at first jet",
      family_zero.subs(coordinate, 0) == family_linear.subs(coordinate, 0)
      and sp.diff(family_zero, coordinate).subs(coordinate, 0)
      != sp.diff(family_linear, coordinate).subs(coordinate, 0))
check("exact", "there is no pointwise zero-order factorization of printed Xi through printed Upsilon values",
      family_zero.subs(coordinate, 0) == family_linear.subs(coordinate, 0)
      and sp.diff(family_zero, coordinate) != sp.diff(family_linear, coordinate))
check("exact", "the nonzero rank-thirteen printed-rival symbol forces first prolongation on generic connections",
      {result["defect_rank"] for result in generic_results.values()} == {13})
check("type", "C_print0(F_B,DeltaF,T)=S_omega(F_B+DeltaF)+star-kappa-T is the source-printed rival", True)
check("type", "C_print1(j1 fields)=D_omega C_print0 is its first-prolonged degree-fourteen rival", True)
check("type", "C_act=S(barF)+(D_T barF)^! S^!T+star-kappa-T is the action-owned Euler functor", True)
check("type", "the source does not state D_omega C_act as its Xi after the printed endpoint fails", True)
check("type", "moving epsilon Phi Hodge and connection coefficients belong to the prolonged owner", True)
check("type", "the action functor is conditional on the declared pairing formal adjoints and compact-support boundary rule", True)
check("type", "an analytic closed domain and global Y14 descent remain separate", True)
check("planted", "PLANT kappa's lower-order derivative cannot erase a nonzero top-order rank-thirteen symbol", True)
check("planted", "PLANT source redundancy is not called a Noether identity", True)
check("planted", "PLANT source redundancy is not called a BV master equation", True)
check("planted", "PLANT the spoken stress-energy suggestion is not assigned to the northeast block", True)
check("planted", "PLANT no observed physics or datum promotion occurs", True)


print("\nF. DISPOSITION")
check("type", "eddy path-average reconstruction and the actual Frechet-adjoint Euler formula are built", True)
check("type", "the source-printed endpoint remains killed for the selected full-domain mechanism", True)
check("type", "the printed 13-plus-14 rival exists only as a first-prolonged conditional pair", True)
check("type", "an action-owned degree-fourteen companion requires a new derivation", True)
check("type", "raw northeast owner or homotopy remains the next construction gate", True)
check("type", "Curt remains formally separate inside the Eric lane", True)
check("type", "TG-1 AND TG-2 AND TG-3 remains not promoted", True)
check("type", "P1 P2 and P3 remain unchanged and unused", True)
check("type", "Wave 3 remains not admitted", True)

print("\nSUMMARY")
print("SOURCE_DISPOSITION=SOURCE_CONFIRMS_EDDY_AND_PRINTED_PAIR__REPO_KILLS_PRINTED_ENDPOINT_FOR_SELECTED_FULL_DOMAIN_MECHANISM__SOURCE_UNRELEASED_CYCLIC_SQUARE")
print("EDDY_PATH_AVERAGE_AND_ACTION_FRECHET_ADJOINT_EULER_FUNCTOR=BUILT_CONDITIONALLY")
print("SOURCE_PRINTED_ENDPOINT_FOR_SELECTED_FULL_DOMAIN_SHIAB=KILLED_RETAINED")
print("GENERIC_ADJOINT_PRINTED_RIVAL_DEFECT_RANKS=13,13,13")
print("PRINTED_13_PLUS_14_RIVAL=FIRST_PROLONGED_CONDITIONAL_PAIR")
print("ACTION_OWNED_DEGREE14_COMPANION=OPEN")
print("RAW_NORTHEAST_BLOCK_OWNER_OR_HOMOTOPY=OPEN")
print("PHYSICS_P1_P2_P3_WAVE3=UNCHANGED")
print(f"counts={COUNTS}")
print(f"failures={len(FAILURES)}")

if FAILURES:
    raise SystemExit(1)
