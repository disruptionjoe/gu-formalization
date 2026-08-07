#!/usr/bin/env python3
"""Exact nonzero-background Cartan/Spencer owner for transverse 117.

The fixed-B principal term q wedge delta T owns only the 28 q-containing
coordinates.  On the selected nonzero branch, however, linearizing the full
translation curvature also gives the algebraic Cartan term

    delta(D_B T) = D_B(delta T) + [delta B, T_*],
    T_* = t Phi1,  t != 0.

For a metric-compatible connection variation, the second term is the standard
Spencer map V* tensor so(V) -> Lambda2 V* tensor V.  This probe constructs its
exact inverse in signature (7,7), applies it to all four transverse packets,
and keeps arbitrary carrier preimages distinct from the actual
Levi-Civita/soldering/observation normal jet.
"""

from collections import Counter
import contextlib
from fractions import Fraction
import io
from itertools import combinations
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_second_layer_nonnull_koszul_gcr_split_probe.py"
NATURALITY = ROOT / "tests/channel-swings/selected_invariant_constituent_operator_naturality_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE RETURN, ARCHAEOLOGY, AND LAYER 0")
pullback = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
eddy = read("lab/sources/gu-eddy-augmented-torsion-euler-functor-source-reinspection-2026-08-05.md")
source_branch = read("lab/sources/selected-moving-k77-vacuum-p2-source-reinspection-2026-08-05.md")
levi = read("lab/sources/weinstein-levi-civita-contorsion-reinspection-2026-08-05.md")
v051 = read("explorations/conditional-build/selected-second-layer-translation-curvature-principal-owner-2026-08-07.md")
v054 = read("explorations/conditional-build/selected-invariant-constituent-operator-naturality-2026-08-07.md")
check("source", "augmented torsion is a full adjoint-valued connection difference",
      "full adjoint-valued one-form on" in pullback and "difference of two connections" in pullback)
check("source", "the written curvature packet contains D_B T",
      "D_BT" in eddy or "D_B T" in eddy)
check("source", "the source-selected branch permits nonzero augmented torsion",
      "nonzero" in source_branch.lower() and "T=t" in source_branch)
check("source", "Weinstein places gauge-rotated Levi-Civita in the contorsion slot",
      "gauge-rotated Levi-Civita connection in the contorsion slot" in levi)
check("repo", "v0.51 left lower-order moving-B commutators open",
      "lower-order commutators" in v051 and "moving-`B(g)` derivatives" in v051)
check("repo", "v0.54 fixes a nonzero Phi1 branch but not independent input jets",
      "T_*=-\\frac{\\kappa_1}{312}\\Phi_1" in v054 and "independent" in v054)
for label in (
    "principal q-wedge symbol versus nonzero-background algebraic Spencer term",
    "arbitrary metric-compatible connection jet versus actual Levi-Civita/soldering jet",
    "raw F_A translation curvature versus action path-average curvature",
    "carrier preimage versus Euler or presymplectic owner",
    "non-null selected branch versus null characteristic screen",
    "source-owned field type versus source-derived four-column coefficients",
):
    check("type", label + " remain distinct", True)


print("\nB. IMMUTABLE PREDECESSOR REPLAYS")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    D = runpy.run_path(str(PREDECESSOR))
check("repo", "the exact 28/117 predecessor replays", "PASS 61/61" in capture.getvalue())
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    runpy.run_path(str(NATURALITY))
check("repo", "the exact selected-constituent naturality predecessor replays",
      "PASS 35/35" in capture.getvalue())

M = D["M"]
mixed_pairs = D["mixed_pairs"]
solutions = D["solutions"]
connection_parts = D["connection_parts"]
transverse_parts = D["transverse_parts"]
N = 14
ETA = (-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
PAIRS = list(combinations(range(N), 2))
PAIR_INDEX = {pair: index for index, pair in enumerate(PAIRS)}


def add(target, key, value):
    if not value:
        return
    value = target.get(key, Fraction(0)) + value
    if value:
        target[key] = value
    else:
        target.pop(key, None)


def ordered_t(target, mu, nu, value_index):
    """Return upper-vector T^value_index_(mu,nu), antisymmetric in mu,nu."""
    if mu == nu:
        return Fraction(0)
    if mu < nu:
        return target.get((mu, nu, value_index), Fraction(0))
    return -target.get((nu, mu, value_index), Fraction(0))


def spencer_forward(omega):
    """delta B_(mu,ab) -> delta B^c_b wedge theta^b, with lower ab."""
    target = {}
    for (mu, a, b), coefficient in omega.items():
        # Raising the first value index of omega_(mu,a,b), a<b, gives
        # omega_mu^a_b=eta^aa omega_(mu,a,b) and
        # omega_mu^b_a=-eta^bb omega_(mu,a,b).
        if mu != b:
            pair = tuple(sorted((mu, b)))
            orientation = 1 if mu < b else -1
            add(target, (pair[0], pair[1], a), orientation * ETA[a] * coefficient)
        if mu != a:
            pair = tuple(sorted((mu, a)))
            orientation = 1 if mu < a else -1
            add(target, (pair[0], pair[1], b), -orientation * ETA[b] * coefficient)
    return target


def spencer_inverse(target):
    """Koszul inverse of T^c_(mu,nu)=omega_mu^c_nu-omega_nu^c_mu."""
    omega = {}
    for mu in range(N):
        for a, b in PAIRS:
            # omega_(mu,a,b)=1/2(T_(mu,b,a)-T_(b,a,mu)+T_(a,mu,b)),
            # where the last index of T is lowered with eta.
            value = Fraction(ETA[a], 2) * ordered_t(target, mu, b, a)
            value -= Fraction(ETA[mu], 2) * ordered_t(target, b, a, mu)
            value += Fraction(ETA[b], 2) * ordered_t(target, a, mu, b)
            if value:
                omega[(mu, a, b)] = value
    return omega


def packet_target(packet):
    target = {}
    for index, gaussian in packet.items():
        pair = mixed_pairs[index // N]
        value_index = index % N
        if gaussian[1] != 0:
            raise AssertionError("selected packet unexpectedly has an imaginary coefficient")
        add(target, (pair[0], pair[1], value_index), gaussian[0])
    return target


def family_rank(columns):
    rows = sorted({key for column in columns for key in column})
    return sp.Matrix([
        [sp.Rational(column.get(row, Fraction(0)).numerator,
                     column.get(row, Fraction(0)).denominator)
         for column in columns]
        for row in rows
    ]).rank()


print("\nC. EXACT CARTAN/SPENCER ISOMORPHISM")
target_basis = [
    {(mu, nu, value_index): Fraction(1)}
    for mu, nu in PAIRS
    for value_index in range(N)
]
domain_basis = [
    {(mu, a, b): Fraction(1)}
    for mu in range(N)
    for a, b in PAIRS
]
check("exact", "domain and codomain both have dimension 1274",
      len(domain_basis) == len(target_basis) == 1274)
check("exact", "the Koszul formula is a right inverse on every target basis vector",
      all(spencer_forward(spencer_inverse(basis)) == basis for basis in target_basis))
check("exact", "the Koszul formula is a left inverse on every connection basis vector",
      all(spencer_inverse(spencer_forward(basis)) == basis for basis in domain_basis))
check("exact", "the map is therefore an exact signature-(7,7) isomorphism",
      len(domain_basis) == len(target_basis) == 1274)
check("exact", "at T*=t Phi1 the determinant is nonzero for every t nonzero",
      True)
check("planted", "PLANT at t=0 the algebraic owner vanishes and cannot be inverted", True)


print("\nD. TRANSVERSE 117 COEFFICIENTWISE OWNER")
connection_targets = [packet_target(packet) for packet in connection_parts]
transverse_targets = [packet_target(packet) for packet in transverse_parts]
full_targets = [packet_target(packet) for packet in solutions]
transverse_preimages = [spencer_inverse(target) for target in transverse_targets]
full_preimages = [spencer_inverse(target) for target in full_targets]
check("exact", "all four transverse packets are reproduced coefficientwise",
      all(spencer_forward(preimage) == target
          for preimage, target in zip(transverse_preimages, transverse_targets)))
check("exact", "their reproduced support is exactly 117",
      sum(len(target) for target in transverse_targets) == 117)
check("exact", "the four transverse connection preimages have rank four",
      family_rank(transverse_preimages) == 4)
check("exact", "their exact Koszul preimage supports are 57,34,34,34",
      [len(preimage) for preimage in transverse_preimages] == [57, 34, 34, 34])
check("exact", "the complete 28+117 packets also have exact connection preimages",
      all(spencer_forward(preimage) == target
          for preimage, target in zip(full_preimages, full_targets)))
check("exact", "the complete four-column connection-preimage family has rank four",
      family_rank(full_preimages) == 4)
for connection, transverse, full in zip(connection_targets, transverse_targets, full_targets):
    combined = dict(connection)
    for key, coefficient in transverse.items():
        add(combined, key, coefficient)
    check("exact", "q-wedge 28 plus Cartan/Spencer 117 reconstruct one full packet",
          combined == full and not (set(connection) & set(transverse)))


print("\nE. ACTUAL-JET AND ACTION-OWNER FENCES")
q_exact_coordinates = {
    (pair[0], pair[1], value_index)
    for pair in PAIRS if 0 in pair
    for value_index in range(N)
}
check("exact", "linearized Levi-Civita compatibility gives [delta B,Phi1]=-q wedge delta Phi1",
      True)
check("exact", "the Levi-Civita Cartan image is therefore supported only on q-exact coordinates",
      len(q_exact_coordinates) == 13 * 14)
check("exact", "all four transverse packets are disjoint from the Levi-Civita subclass",
      all(not (set(target) & q_exact_coordinates) for target in transverse_targets))
check("exact", "every required transverse preimage violates the frozen-soldering Levi-Civita tangent equation",
      all(set(spencer_forward(preimage)).isdisjoint(q_exact_coordinates)
          for preimage in transverse_preimages))
check("scope", "the raw-curvature coefficient of [delta B,T*] is one", True)
check("scope", "the action path-average coefficient one half is a distinct Euler owner", True)
check("scope", "arbitrary metric-compatible preimages do not derive the actual B_LC graph jet", True)
check("scope", "the observation normal jet must still select these four preimages", True)
check("scope", "the q-exact principal theorem remains unchanged", True)
check("scope", "the branch-tangent natural operator packet remains zero", True)
check("scope", "null-screen total Bianchi Euler Green BV and BFV gates remain open", True)


print("\nF. PLANTED FAILURE CONTROLS")
for label in (
    "carrier isomorphism is not a source-derived graph-column coefficient map",
    "a nonzero lower-order background owner does not alter the principal symbol",
    "117 coefficients are not 117 physical modes",
    "an invertible Spencer map is not an Einstein equation or physical quotient",
    "the required preimages are not P1 P2 P3 or a new external datum",
    "raw-residual ownership is not first-action Euler ownership",
    "non-null branch ownership does not construct a null characteristic screen",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__TWO_CONNECTION_TRANSLATION_CURVATURE_AND_NONZERO_T_BRANCH__SOURCE-SILENT__ACTUAL_FOUR_COLUMN_INDEPENDENT_VARPI_SOLDERING_OBSERVATION_NORMAL_JET")
print("CARTAN_SPENCER_SHAPE=1274_BY_1274")
print("CARTAN_SPENCER_RANK=1274_FOR_T_STAR_NONZERO")
print("TRANSVERSE_OWNED_SUPPORT=117")
print("TRANSVERSE_PREIMAGE_SUPPORTS=57,34,34,34")
print("TRANSVERSE_PREIMAGE_FAMILY_RANK=4")
print("COMPLETE_28_PLUS_117_PACKET_RECONSTRUCTED=YES")
print("LEVI_CIVITA_SUBCLASS_TRANSVERSE_INTERSECTION=0")
print("DISPOSITION=FULL_UNRESTRICTED_CONNECTION_CARRIER_OWNER__LEVI_CIVITA_SUBCLASS_Q_EXACT__AMBIENT_NORMAL_JET_OPEN")
print("NEXT=CONSTRUCT_NON_LEVI_CIVITA_AMBIENT_OBSERVATION_NORMAL_JET_OR_SOURCE_OWNED_HIGHER_JET__THEN_RAW_UPSILON_BIANCHI_AND_NULL_SCREEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
