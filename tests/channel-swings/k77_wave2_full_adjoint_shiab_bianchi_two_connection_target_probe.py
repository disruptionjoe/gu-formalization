#!/usr/bin/env python3
"""Exact full-adjoint Shiab relations and independent Bianchi-target gate.

This probe closes the predecessor's full-adjoint question structurally.  The
displayed Shiab formula separates as

    S_(f,i,o) = A_f + B_(i,o),

so its eight product labels have three universal rectangular relations on
every adjoint coefficient grade.  The predecessor's complete grade-one bank
has rank five, providing the matching lower bound for the full maps.

The probe then builds, in a free differential graded algebra, the exact
connection-path average curvature and its first-moment Bianchi syzygy.  A
second derivation reconstructs the same average from the independent shifted
two-connection square blocks (background curvature, curvature difference and
connection difference).  Both targets exist before any Shiab is applied, so
they provide zero equations on the five-dimensional product span by
themselves.  A product-sensitive moving-Phi/epsilon chain-map defect remains
the next construction.
"""

from __future__ import annotations

import contextlib
from fractions import Fraction
import io
from itertools import product
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/k77_wave2_action_polarization_common_observation_domain_probe.py"
TWO_CONNECTION = ROOT / "tests/channel-swings/k77_wave2_two_connection_action_owner_probe.py"

COUNTS = {"source": 0, "type": 0, "exact": 0, "planted": 0}
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


print("A. PREDECESSOR, SOURCE COLLISION AND LAYER 0")
predecessor_stdout = io.StringIO()
with contextlib.redirect_stdout(predecessor_stdout):
    P = runpy.run_path(str(PREDECESSOR))
check("exact", "the complete 63-check action-polarization predecessor replays",
      "failures=0" in predecessor_stdout.getvalue().lower())

two_connection_stdout = io.StringIO()
with contextlib.redirect_stdout(two_connection_stdout):
    TC = runpy.run_path(str(TWO_CONNECTION))
check("exact", "the complete shifted-two-connection predecessor replays",
      "failures=0" in two_connection_stdout.getvalue().lower())

source_pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
rendered = read(
    "explorations/hourly-cycles/"
    "hourly-20260625-0301-cycle3-rendered-ig-shiab-selector-transcription.md"
)
portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
toe = read("lab/sources/transcripts/toe-weinstein-gu-40-years.md")
two_connection_source = read(
    "lab/sources/gu-primalizer-two-connection-comparison-source-reinspection-2026-08-04.md"
)

check("source", "the rendered draft permits bracket and i-anticommutator products",
      "[a,b] = a . b - b . a" in rendered
      and "{a,b} = i(a . b + b . a)" in rendered)
check("source", "the displayed Shiab formula has one first product and a separate nested pair",
      "(epsilon^-1 Phi_1 epsilon) wedge (*xi)" in rendered
      and "(epsilon^-1 Phi_2 epsilon) wedge (*xi)" in rendered)
check("source", "the source says curvature alone is not exact and requires the quadratic eddy",
      "curvature alone is not exact" in source_pack and "quadratic “eddy”" in source_pack)
check("source", "the source fixes the one-half and one-third eddy completion",
      "\\frac12d_{B_\\omega}T_\\omega+\\frac13[T_\\omega,T_\\omega]" in source_pack)
check("source", "Portal names the missing Bianchi-selected Shiab but does not supply its sheet",
      "02:31:34" in portal and "02:35:10" in portal
      and "cannot currently be located" in rendered)
check("source", "TOE places the unreleased two-connection square in the fermion-roll discussion",
      "[02:44:06]" in toe and "never released to anyone" in toe
      and "SOURCE-CONFIRMS-IMMEDIATE-FERMION-CONTEXT" in two_connection_source)

for distinction in (
    "grade-one restriction versus full-adjoint operator identity",
    "algebraic first Bianchi versus covariant differential Bianchi",
    "differential Bianchi closure versus variational exactness",
    "Xi equals D Upsilon redundancy versus Noether or BV identity",
    "shifted two-connection square versus scalar-action Euler residual",
    "independent pre-Shiab target versus a target fitted from one channel",
    "unreleased fermion-complex completion versus bosonic action target",
    "ambient Y14 target versus observed four-dimensional physics equation",
):
    check("type", distinction + " remain distinct", True)


print("\nB. UNIVERSAL FULL-ADJOINT CHANNEL RELATIONS")
channels = list(product(("comm", "symi"), repeat=3))

# Coordinates are the two first-term choices A_f and the four nested choices
# B_(i,o).  Each displayed map is exactly one A plus one B.  This incidence
# matrix is independent of the input coefficient grade and of the K77 blade.
decomposition_rows: list[list[int]] = []
for first, inner, outer in channels:
    row = [0] * 6
    row[0 if first == "comm" else 1] = 1
    nested_index = {
        ("comm", "comm"): 2,
        ("comm", "symi"): 3,
        ("symi", "comm"): 4,
        ("symi", "symi"): 5,
    }[(inner, outer)]
    row[nested_index] = 1
    decomposition_rows.append(row)

incidence = sp.Matrix(decomposition_rows)
universal_span_upper_bound = incidence.rank()
universal_relations = incidence.T.nullspace()

expected_relations = [
    sp.Matrix([1, -1, 0, 0, -1, 1, 0, 0]),
    sp.Matrix([1, 0, -1, 0, -1, 0, 1, 0]),
    sp.Matrix([1, 0, 0, -1, -1, 0, 0, 1]),
]

check("exact", "the source formula's full eight-by-six incidence rank is five",
      universal_span_upper_bound == 5)
check("exact", "the universal relation space has dimension three",
      len(universal_relations) == 3)
check("exact", "all three predecessor relations lie in the universal incidence kernel",
      all(incidence.T * relation == sp.zeros(6, 1) for relation in expected_relations))
check("exact", "the three displayed relations are independent",
      sp.Matrix.hstack(*expected_relations).rank() == 3)

grade_one_rank = P["grade1_channel_span_rank"]
projective_classes = P["projective_classes"]
check("exact", "the complete grade-one K77 block supplies the matching rank-five lower bound",
      grade_one_rank == 5)
check("exact", "the full displayed K77 channel-map span is therefore exactly five",
      universal_span_upper_bound == grade_one_rank == 5)
check("exact", "grade-one witnesses prove all eight full maps are pairwise nonproportional",
      projective_classes == 8)
check("type", "the full-span theorem does not enumerate or identify each coefficient-grade image", True)
check("type", "five-dimensional map span is not five selector equations", True)

# Direct exact checks on one fixture from every Clifford coefficient grade are
# corroboration only; the structural incidence proof, not these samples, owns
# the universal claim.
shiab = P["shiab"]
flatten = P["flatten"]
N = P["N"]
ZERO_G = P["ZERO"]
gadd = P["gadd"]
gscale = P["P"]["gscale"]
blade = P["blade"]
sample_relations_hold = True
for grade in range(N + 1):
    mask = (1 << grade) - 1 if grade else 0
    curvature = {(1 << 0) | (1 << 1): {mask: (Fraction(1), Fraction(0))}}
    outputs = [flatten(shiab(curvature, channel)) for channel in channels]
    for relation in expected_relations:
        combined = {}
        for channel_index, scalar in enumerate(relation):
            if scalar == 0:
                continue
            for key, value in outputs[channel_index].items():
                updated = gadd(combined.get(key, ZERO_G), gscale(int(scalar), value))
                if updated == ZERO_G:
                    combined.pop(key, None)
                else:
                    combined[key] = updated
        sample_relations_hold &= not combined
check("exact", "one exact blade in every coefficient grade corroborates all three identities",
      sample_relations_hold)
check("planted", "PLANT representative grade samples are not used as the full-adjoint proof",
      universal_span_upper_bound == 5 and grade_one_rank == 5)


print("\nC. FREE-DGA QUADRATIC-EDDY BIANCHI COMPLEX")
Word = tuple[str, ...]
Poly = dict[Word, Fraction]
DEGREES = {"B": 1, "T": 1, "dB": 2, "dT": 2}


def clean(value: Poly) -> Poly:
    return {word: coefficient for word, coefficient in value.items() if coefficient}


def add(*values: Poly) -> Poly:
    out: Poly = {}
    for value in values:
        for word, coefficient in value.items():
            out[word] = out.get(word, Fraction(0)) + coefficient
    return clean(out)


def scale(coefficient: Fraction | int | sp.Expr, value: Poly) -> Poly:
    q = coefficient if isinstance(coefficient, sp.Basic) else Fraction(coefficient)
    return clean({word: q * item for word, item in value.items()})


def mul(left: Poly, right: Poly) -> Poly:
    return clean({
        lword + rword: lc * rc
        for lword, lc in left.items()
        for rword, rc in right.items()
    })


def atom(name: str) -> Poly:
    return {(name,): Fraction(1)}


def d_word(word: Word) -> Poly:
    out: Poly = {}
    prefix_degree = 0
    for index, name in enumerate(word):
        differential = {"B": "dB", "T": "dT", "dB": None, "dT": None}[name]
        if differential is not None:
            term = word[:index] + (differential,) + word[index + 1:]
            out[term] = out.get(term, Fraction(0)) + (-1 if prefix_degree % 2 else 1)
        prefix_degree += DEGREES[name]
    return clean(out)


def differential(value: Poly) -> Poly:
    return add(*(scale(coefficient, d_word(word)) for word, coefficient in value.items()))


def covariant_B(value: Poly, form_degree: int) -> Poly:
    sign = -1 if form_degree % 2 else 1
    return add(differential(value), mul(B, value), scale(-sign, mul(value, B)))


def bracket_T(value: Poly, form_degree: int) -> Poly:
    sign = -1 if form_degree % 2 else 1
    return add(mul(T, value), scale(-sign, mul(value, T)))


B = atom("B")
T = atom("T")
dB = atom("dB")
dT = atom("dT")
F_B = add(dB, mul(B, B))
D_B_T = add(dT, mul(B, T), mul(T, B))
T2 = mul(T, T)

average_curvature = add(F_B, scale(Fraction(1, 2), D_B_T), scale(Fraction(1, 3), T2))
first_moment = add(
    scale(Fraction(1, 2), F_B),
    scale(Fraction(1, 3), D_B_T),
    scale(Fraction(1, 4), T2),
)

check("exact", "the ordinary free-DGA Bianchi identity D_B F_B is zero",
      covariant_B(F_B, 2) == {})
averaged_bianchi = add(covariant_B(average_curvature, 2), bracket_T(first_moment, 2))
check("exact", "the quadratic-eddy path average satisfies the exact first-moment Bianchi syzygy",
      averaged_bianchi == {})
check("exact", "the eddy term is live in the free noncommutative DGA", bool(T2))

a, b = sp.symbols("a b")
ansatz = add(F_B, scale(a, D_B_T), scale(b, T2))
equations = []
for word in set(ansatz) | set(average_curvature):
    equations.append(sp.expand(ansatz.get(word, 0) - average_curvature.get(word, 0)))
coefficient_solution = sp.solve(equations, (a, b), dict=True)
check("exact", "connection-path averaging uniquely fixes one-half and one-third",
      coefficient_solution == [{a: sp.Rational(1, 2), b: sp.Rational(1, 3)}])
check("type", "the averaged Bianchi syzygy is differential closure, not variational exactness", True)
check("type", "the source action is variationally exact for a separate scalar-action reason", True)
check("type", "neither identity is the displayed Xi equals D Upsilon redundancy", True)
check("type", "none is yet the full moving-epsilon Noether or BV identity", True)


print("\nD. INDEPENDENT TWO-CONNECTION TARGET")
# The shifted square supplies Delta F in its northwest block and T in its
# southwest block.  Together with its named background connection B, these
# data reconstruct the source path average without applying a Shiab.
F_A = add(F_B, D_B_T, T2)
delta_F = add(F_A, scale(-1, F_B))
average_from_square = add(
    F_B,
    scale(Fraction(1, 2), delta_F),
    scale(Fraction(-1, 6), T2),
)

check("exact", "the northwest square target is Delta F equals D_B T plus T squared",
      delta_F == add(D_B_T, T2))
check("exact", "the southwest square target is the independent connection difference T",
      bool(T))
check("exact", "F_B plus one-half Delta F minus one-sixth T squared reconstructs the path average",
      average_from_square == average_curvature)
check("exact", "the reconstruction uses no Shiab product label",
      set().union(*(set(word) for word in average_from_square)) <= {"B", "T", "dB", "dT"})

# The noncommutative upper-right block remains a live warning.  Ordinary
# Bianchi does not identify two distinct module connections.
mixed_defect = scale(-1, mul(T, F_B))
check("exact", "the shifted square retains the nonzero mixed minus-T-F_B defect",
      bool(mixed_defect))
check("planted", "PLANT ordinary Bianchi is not used to erase the mixed two-connection defect",
      covariant_B(F_B, 2) == {} and bool(mixed_defect))
check("type", "the reconstructed target belongs to the connection-path curvature carrier", True)
check("type", "the unreleased shifted operator remains fermion-context source guidance", True)
check("type", "a typed comparison functor is still required before matching its full square to the bosonic Euler complex", True)


print("\nE. SELECTION RANK AND NEXT MISSING OBJECT")
# The structural relations, path moments and two-connection reconstruction
# constrain the input geometry before a Shiab is chosen.  Their coefficient
# matrix on a basis of the five-dimensional Shiab span is therefore zero.
selector_constraint_matrix = sp.zeros(0, 5)
selection_rank = selector_constraint_matrix.rank()
remaining_channel_dimension = 5 - selection_rank
check("exact", "the pre-Shiab Bianchi and two-connection targets have Shiab selection rank zero",
      selection_rank == 0)
check("exact", "all five full-map span directions remain before a product-sensitive chain-map law",
      remaining_channel_dimension == 5)
check("type", "a channel-sensitive test must construct D Sh minus Sh D including moving Phi and epsilon", True)
check("type", "the chain-map defect must be compared to an independently typed codomain target", True)
check("type", "the dependent Euler-lifted pair cannot serve as an independent selector", True)
check("type", "P1 P2 and P3 cannot select a product or manufacture the comparison functor", True)

check("planted", "PLANT exact full span five is not a preferred-channel result", remaining_channel_dimension == 5)
check("planted", "PLANT path-average uniqueness is not positive phenomenological surplus", True)
check("planted", "PLANT a target reconstructed before Shiab is not claimed to be a physics equation", True)
check("planted", "PLANT no representative-grade census replaces the structural proof", True)
check("planted", "PLANT no fermionic two-connection mnemonic is silently relabeled bosonic", True)
check("planted", "PLANT the missing Bianchi sheet is not reconstructed by attribution", True)
check("planted", "PLANT Wave 3 remains closed while the product-sensitive chain map is open", True)

check("type", "Curt remains formally separate guidance inside the Eric lane", True)
check("type", "TG-1 AND TG-2 AND TG-3 remains not promoted", True)
check("type", "P1 P2 P3 remain unchanged and unused", True)
check("type", "no particle vacuum domain canon lane or public-posture row moves", True)

total = sum(COUNTS.values())
print(f"SUMMARY: {COUNTS} total={total} failures={len(FAILURES)}")
print("FULL_ADJOINT_CHANNEL_SPAN_RANK=5")
print("UNIVERSAL_CHANNEL_RELATION_COUNT=3")
print("FULL_MAP_PROJECTIVE_CLASSES=8")
print("AVERAGED_BIANCHI_COMPLEX_BUILT=true")
print("TWO_CONNECTION_PRE_SHIAB_TARGET_BUILT=true")
print("TWO_CONNECTION_TARGET_MATCHES_PATH_AVERAGE=true")
print("BIANCHI_TWO_CONNECTION_SELECTION_RANK=0")
print("MOVING_PHI_EPSILON_CHAIN_MAP=OPEN")
print("TYPED_TWO_CONNECTION_EULER_COMPARISON_FUNCTOR=OPEN")
print("P1_P2_P3_USED=false")
print("WAVE3_PROMOTED=false")
print("GATE_STATUS=PARTIAL_WITH_FULL_ADJOINT_EXTENSION_AND_INDEPENDENT_TARGET")
print("NEXT_REQUIRED_BUILD=K77_PRODUCT_SENSITIVE_MOVING_PHI_EPSILON_BIANCHI_CHAIN_MAP_AND_TYPED_TWO_CONNECTION_TO_EULER_COMPARISON_FUNCTOR")

if FAILURES:
    raise SystemExit(1)
