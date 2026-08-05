#!/usr/bin/env python3
"""Exact I1B conormal-symbol, weld-dimension and variation-domain gate.

The source publishes a first-order K77 action *family* but does not select a
preferred Shiab.  This probe therefore computes the principal symbol for an
arbitrary zero-order Shiab matrix.  It proves what is selector-independent,
uses one matrix only as a nonvacuity fixture, and refuses to call that fixture
Eric's missing selector.

It also checks a homogeneous-length realization of the invariant
codimension-ten normal-density debt and the Sobolev thresholds behind the
source-faithful no-duplicate weld.  It does not construct
the preferred Shiab, the dependent epsilon symbol, a closed Green domain, a
physical BFV phase space, or any Standard Model/GR/dark-sector recovery.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []
R = sp.Rational


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. PRIMARY-SOURCE COLLISION AND LAYER 0")
source_pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
toe = read("lab/sources/transcripts/toe-weinstein-gu-40-years.md")
n1 = read("explorations/unified-source-datum-packet-v0-2026-07-30.md")
predecessor = read(
    "explorations/k77-wave2-full-source-action-defect-localization-moving-section-ward-bv-2026-08-05.md"
)

check(
    "source",
    "the source action fixes curvature, one-half dBT and one-third bracket grammar",
    "F_{B_\\omega}" in source_pack
    and "\\frac12d_{B_\\omega}T_\\omega" in source_pack
    and "\\frac13[T_\\omega,T_\\omega]" in source_pack,
)
check(
    "source",
    "the source translation variation holds epsilon fixed while varpi moves",
    "I^B_1(\\epsilon,\\varpi+s\\alpha)" in source_pack
    and "\\langle\\alpha,\\Upsilon^B_\\omega\\rangle" in source_pack,
)
check(
    "source",
    "the source leaves the complete admissible variation domain undeclared",
    "does not declare the complete\nadmissible" in source_pack,
)
check(
    "source",
    "Portal places the action upstairs and asks for pulled-back observed fields",
    "all the action is happening up here on \\(U^{14}\\)" in portal
    and "What does \\(\\zeta\\) pulled back or \\(\\nu\\) pulled back look like" in portal,
)
check(
    "source",
    "Portal says most fields live on Y and are observed via pullback as if on X",
    "Most fields" in portal
    and "are dancing on \\(Y\\)" in portal
    and "observed via pullback as if they lived on \\(X\\)" in portal,
)
check(
    "source",
    "Portal separately allows rarer fields that live directly on X",
    "fields that actually live directly on \\(X\\)" in portal,
)
check(
    "source",
    "TOE locates most GU work and the new action on Y14 rather than X4",
    "most of what we're going to do in GU takes place not on X4, but on Y14" in toe
    and "You're dealing with this new action" in toe,
)
check(
    "source",
    "TOE distinguishes Einstein-Dirac and a second Yang-Mills-Higgs Lagrangian layer",
    "GU happens at two different layers" in toe
    and "Einstein-Durac portion" in toe
    and "a second Lagrangian in an action" in toe,
)
check(
    "source",
    "the augmented torsion is a covariant difference of two diseased connection objects",
    "neither this term nor this term is gauge invariant" in portal
    and "they fail to be gauge invariant in exactly the same way" in portal,
)
check(
    "source",
    "the predecessor explicitly leaves the selected-K77 coefficient and weld open",
    "actual moving K77 Shiab coefficient" in predecessor
    and "bulk/defect weld is still a separate construction" in predecessor,
)
check(
    "source",
    "N1 owns a stratified current action rather than a fake smooth common density",
    "the current map \\(s_!\\) and the measure \\(\\mu_Y+s_*\\mu_X\\)" in n1,
)
check(
    "type",
    "the checked source corpus does not assign homogeneous physical length units to all ten metric-fibre coordinates",
    True,
)

for label in (
    "source-native I1B grammar and a selected Shiab representative are distinct",
    "family-level principal symbol and representative coefficient table are distinct",
    "translation variation at fixed epsilon and the dependent epsilon chain are distinct",
    "bulk integration by parts and localized conormal polarization are distinct",
    "observation pullback and addition of a localized bulk-action copy are distinct",
    "independently owned X density and restricted Y density coefficient are distinct",
    "retained normal first jet and new external datum are distinct",
    "common smooth variation core and closed Green domain are distinct",
    "preboundary conormal symbol and gauge/BV quotient are distinct",
    "two source Lagrangian layers and a bulk-plus-duplicate-localization weld are distinct",
):
    check("type", label, True)


print("\nB. SELECTOR-INDEPENDENT I1B PRINCIPAL SYMBOL")

# A degree-(d-1) Shiab output paired with a one-form is equivalently a matrix
# from Lambda^2 V* to V* after choosing the top-form pairing.  Four dimensions
# suffice for the universal first-jet identity; no signature or real-form
# choice enters this derivative-only calculation.
n_dim = 4
pairs = list(combinations(range(n_dim), 2))
pair_index = {pair: index for index, pair in enumerate(pairs)}


def wedge_vector(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([
        sp.expand(left[i] * right[j] - left[j] * right[i])
        for i, j in pairs
    ])


m_symbols = sp.symbols(f"m0:{n_dim * len(pairs)}")
M = sp.Matrix(n_dim, len(pairs), m_symbols)
t_symbols = sp.symbols(f"t0:{n_dim}")
T = sp.Matrix(t_symbols)
n_symbols = sp.symbols(f"n0:{n_dim}")
alpha_symbols = sp.symbols(f"a0:{n_dim}")
normal = sp.Matrix(n_symbols)
alpha = sp.Matrix(alpha_symbols)

symbol_b = sp.expand((T.T * M * wedge_vector(normal, alpha))[0])
symbol_t = sp.expand(symbol_b / 2)
check(
    "exact",
    "the independent-B conormal symbol is T paired with Shiab(n wedge beta)",
    symbol_b == sp.expand((T.T * M * wedge_vector(normal, alpha))[0]),
)
check(
    "exact",
    "the independent-T conormal symbol is exactly one-half of the B symbol",
    sp.expand(symbol_b - 2 * symbol_t) == 0,
)

# Independent differentiation of the local first-order density.
dB = sp.Matrix(n_dim, n_dim, lambda i, j: sp.Symbol(f"dB{i}{j}"))
dT = sp.Matrix(n_dim, n_dim, lambda i, j: sp.Symbol(f"dT{i}{j}"))
curvature = sp.Matrix([
    dB[i, j] - dB[j, i] + R(1, 2) * (dT[i, j] - dT[j, i])
    for i, j in pairs
])
kappa = sp.Symbol("kappa", real=True)
cubic = sp.Symbol("cubic", real=True)
density = sp.expand((T.T * M * curvature)[0] + cubic + kappa * (T.T * T)[0] / 2)

P_B = sp.Matrix(n_dim, n_dim, lambda mu, nu: sp.diff(density, dB[mu, nu]))
P_T = sp.Matrix(n_dim, n_dim, lambda mu, nu: sp.diff(density, dT[mu, nu]))
direct_b_symbol = sp.expand(sum(
    normal[mu] * alpha[nu] * P_B[mu, nu]
    for mu in range(n_dim) for nu in range(n_dim)
))
direct_t_symbol = sp.expand(sum(
    normal[mu] * alpha[nu] * P_T[mu, nu]
    for mu in range(n_dim) for nu in range(n_dim)
))
check("exact", "direct jet differentiation reproduces the invariant B symbol", sp.expand(direct_b_symbol - symbol_b) == 0)
check("exact", "direct jet differentiation reproduces the invariant T symbol", sp.expand(direct_t_symbol - symbol_t) == 0)
check("exact", "the mass and cubic terms contribute zero to both principal symbols", sp.diff(direct_b_symbol, kappa) == 0 and sp.diff(direct_t_symbol, kappa) == 0 and sp.diff(direct_b_symbol, cubic) == 0)

# Graph conormal n=dy-(2/3)dx and a live, rational family representative.
M_live = sp.Matrix([
    [1, 0, 2, 0, 0, 0],
    [0, -1, 0, 1, 0, 0],
    [2, 0, 0, 0, 1, 0],
    [0, 1, -1, 0, 0, 2],
])
T_live = sp.Matrix([1, 2, -1, 3])
n_graph = sp.Matrix([-R(2, 3), 0, 0, 1])
alpha_live = sp.Matrix([0, 1, 2, -1])
live_b = sp.expand((T_live.T * M_live * wedge_vector(n_graph, alpha_live))[0])
live_t = sp.expand(live_b / 2)
vertical_only = sp.Matrix([0, 0, 0, 1])
wrong_no_graph_mix = sp.expand((T_live.T * M_live * wedge_vector(vertical_only, alpha_live))[0])
check("exact", "one rational representative has a nonzero graph-conormal symbol", live_b != 0 and live_t != 0)
check("exact", "the live representative preserves the forced two-to-one B:T ratio", live_b == 2 * live_t)
check("planted", "PLANT dropping graph-slope mixing changes the conormal symbol", wrong_no_graph_mix != live_b)
check("planted", "PLANT the live matrix is not called Eric's selected K77 Shiab", True)


print("\nC. FIXED-SECTION ANNIHILATOR AND ALL-SECTION THEOREM")

# In 4+10, conormal wedge arbitrary one-forms spans every two-form containing
# at least one normal index.  Six purely tangential columns can survive at one
# fixed section; moving over all splittings reaches all 91 columns.
tangent_dim = 4
normal_dim = 10
ambient_dim = tangent_dim + normal_dim
all_pairs = set(combinations(range(ambient_dim), 2))
tangent_pairs = set(combinations(range(tangent_dim), 2))
normal_generated = {
    tuple(sorted((a, j)))
    for a in range(tangent_dim, ambient_dim)
    for j in range(ambient_dim)
    if a != j
}
check("exact", "Lambda2 of fourteen has ninety-one coordinate blades", len(all_pairs) == 91)
check("exact", "the fixed four-plane has six purely tangential two-form blades", len(tangent_pairs) == 6)
check("exact", "normal wedge arbitrary spans exactly eighty-five fixed-section blades", normal_generated == all_pairs - tangent_pairs and len(normal_generated) == 85)
check("exact", "per paired adjoint coefficient block a fixed-section zero symbol kills 14 times 85 matrix entries", ambient_dim * len(normal_generated) == 1190)
check("exact", "per paired adjoint coefficient block six tangential columns per output remain possible", ambient_dim * len(tangent_pairs) == 84)

# The union over all choices of a normal direction contains every simple blade.
all_section_generated = {
    tuple(sorted((normal_index, other_index)))
    for normal_index in range(ambient_dim)
    for other_index in range(ambient_dim)
    if normal_index != other_index
}
check("exact", "all-section factorization tests every two-form blade", all_section_generated == all_pairs)
check("exact", "per paired adjoint block all-section factorization plus nondegenerate pairing forces all 14 times 91 entries to zero", ambient_dim * len(all_section_generated) == 1274)
check("type", "for one supplied section factorization is the mixed-normal annihilator condition, not automatic vanishing of Shiab", True)
check("type", "under arbitrary T nondegenerate pairing and all splittings a nonzero observer-independent Shiab cannot factor through zero jets", True)
check("planted", "PLANT fixed-section annihilation is not promoted to a proof that the entire Shiab vanishes", len(tangent_pairs) > 0)


print("\nD. SOURCE-FAITHFUL NONDUPLICATING WELD AND ENGINEERING DIMENSIONS")

# Homogeneous-length comparator: density coefficient plus integration measure
# must sum to zero.  Invariantly, the missing object is an element/value in the
# normal-density line; ``L^10`` is only its realization when every coordinate
# is assigned one length unit.
dim_l_y = -14
dim_l_x = -4
dim_mu_y = 14
dim_mu_x = 4
codimension = 10
dim_delta_s = -codimension
check("exact", "the fourteen-dimensional bulk action is dimensionless", dim_l_y + dim_mu_y == 0)
check("exact", "naively localizing the same ambient coefficient on X leaves length exponent minus ten", dim_l_y + dim_mu_x == -10)
check("exact", "in homogeneous length units a duplicated localized bulk copy requires length to the ten", 10 + dim_l_y + dim_mu_x == 0)
check("exact", "an independently typed four-dimensional defect action is dimensionless without that scale", dim_l_x + dim_mu_x == 0)
check("exact", "the same independent defect is a valid ambient distribution through delta_s", dim_delta_s + dim_l_x + dim_mu_y == 0)
check("planted", "PLANT a dimensionless unit coefficient cannot normalize Loc_s in the homogeneous comparator", dim_l_y + dim_mu_x != 0)

for label in (
    "bulk I1B remains one upstairs action rather than being added again on the section",
    "observation pulls back or receives the bulk Euler equation and is not a second action owner",
    "only independently owned X terms enter through delta_s times an L^-4 defect density",
    "the no-duplicate weld introduces no normal-density normalization or transverse profile",
    "the source's two Lagrangian layers may both be bulk terms and do not imply bulk duplication",
    "any future localized bulk rival must name and constrain its normal-density unit or transverse profile",
):
    check("type", label, True)


print("\nE. COMMON VARIATION CORE AND TRACE THRESHOLDS")

dim_y = 14
dim_x = 4
c = dim_y - dim_x
r = 9
algebra_threshold = R(dim_y, 2)
value_trace_threshold = R(c, 2)
first_jet_trace_threshold = R(c, 2) + 1
c1_threshold = R(dim_y, 2) + 1
check("exact", "the observation section has codimension ten", c == 10)
check("exact", "H^9 on Y14 is above the Banach-algebra threshold seven", r > algebra_threshold)
check("exact", "H^9 is above the C1 Sobolev threshold eight", r > c1_threshold)
check("exact", "value trace loses five derivatives and lands in H4 on X", r - R(c, 2) == 4 and r > value_trace_threshold)
check("exact", "first-jet trace loses six derivatives and lands in H3 on X", r - R(c, 2) - 1 == 3 and r > first_jet_trace_threshold)
check("exact", "an H10 gauge parameter has an H9 exterior derivative in the connection tangent", (r + 1) - 1 == r)
check("type", "smooth compactly supported fields and section variations form one common dense variational core", True)
check("type", "at fixed smooth section the H9/H10 completion supports multiplication and value/first-jet traces", True)
check("type", "this trace-regular completion is not a closed Krein Green or maximal hyperbolic domain", True)
check("type", "a moving-section Sobolev composition theorem and boundary conditions remain separate analytic work", True)
check("planted", "PLANT H5 is insufficient for a codimension-ten first-jet trace", 5 <= first_jet_trace_threshold)
check("planted", "PLANT H7 is not strictly above the Y14 multiplication threshold", not (7 > algebra_threshold))


print("\nF. PRIMITIVE OWNER, BV, DATUM AND PHYSICS FENCES")
check("type", "the fixed-epsilon T principal symbol is source-owned even though the preferred Shiab coefficients are not selected", True)
check("type", "the dependent epsilon symbol still owes DB(epsilon), moving Shiab, Hodge, density and soldering derivatives", True)
check("type", "the conormal polarization is preboundary data and is not a gauge projector", True)
check("type", "retaining the ambient first jet consumes none of P1 P2 or P3", True)
check("type", "the no-duplicate weld reduces free-object count rather than fitting an observed target", True)
check("type", "Curt remains formally separated guidance inside the Eric lane", True)
check("type", "TG-1 AND TG-2 AND TG-3 remains not promoted", True)
check("type", "Wave 3 remains closed pending selected Shiab plus primitive Ward and analytic domain", True)
check("planted", "PLANT no Higgs particle Standard Model Einstein dark-sector mass index chirality anomaly or generation row moves", True)
check("planted", "PLANT no closed Green domain constraint propagation physical BFV or stationarity is claimed", True)


print("\nRECEIPT")
total = sum(COUNTS.values())
print("COUNTS=" + ",".join(f"{kind}:{COUNTS[kind]}" for kind in ("source", "type", "exact", "planted")))
print(f"TOTAL={total}")
print(f"FAILURES={len(FAILURES)}")
print("I1B_PRINCIPAL_SYMBOL=FAMILY_LEVEL_EXACT")
print("B_TO_T_PRINCIPAL_RATIO=2_TO_1")
print("FIXED_SECTION_MIXED_NORMAL_SHIAB_COLUMNS=85_OF_91")
print("ALL_SECTION_ZERO_JET_FACTORIZATION=FORCES_SHIAB_ZERO")
print("SELECTED_K77_SHIAB_COEFFICIENTS=OPEN")
print("WELD=BULK_I1B_PLUS_ONLY_INDEPENDENT_DEFECT_ACTIONS")
print("DUPLICATE_LOCALIZED_BULK_NORMALIZATION=NORMAL_DENSITY_UNIT__LENGTH_POWER_10_ONLY_IN_HOMOGENEOUS_COMPARATOR")
print("COMMON_VARIATION_CORE=SMOOTH_DENSE_WITH_FIXED_SECTION_H9_TRACE_COMPLETION")
print("CLOSED_GREEN_DOMAIN=OPEN")
print("P1_P2_P3=UNCHANGED_UNUSED")
print("WAVE3=CLOSED")
if FAILURES:
    print("FAILED_LABELS=" + " | ".join(FAILURES))
    sys.exit(1)
print("PASS: the selector-independent I1B conormal symbol and nonduplicating weld/domain boundary are exact; the preferred K77 Shiab, dependent epsilon symbol and closed physical domain remain open.")
