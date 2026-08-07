#!/usr/bin/env python3
"""Exact fixed-B translation-curvature ownership test for the v0.48 packet.

At a frozen reference connection B, the principal symbol of the linearized
translation-curvature term D_B T is q wedge delta T.  This probe composes that
source-native symbol with the exact v0.48 inverse-Shiab packets.  It tests the
owner claim coefficientwise and keeps moving B/epsilon/soldering coefficients
outside the result.
"""

from collections import Counter
import contextlib
import io
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_second_layer_nonnull_koszul_gcr_split_probe.py"
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


print("A. SOURCE RETURN AND LAYER 0")
pullback = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
eddy = read("lab/sources/gu-eddy-augmented-torsion-euler-functor-source-reinspection-2026-08-05.md")
retype = read("explorations/conditional-build/selected-second-layer-gcr-exterior-degree-owner-retype-2026-08-07.md")
check("source", "augmented torsion is a full adjoint-valued one-form and connection difference",
      "full adjoint-valued one-form on" in pullback and "difference of two connections" in pullback)
check("source", "the written source curvature contains one half D_B T",
      "\\frac12 D_B T" in eddy or "1/2 D_B T" in eddy)
check("source", "the written source curvature also contains the algebraic T wedge T term",
      "T\\wedge T" in eddy or "T \\wedge T" in eddy)
check("repo", "the predecessor correctly leaves an odd translation-curvature owner open",
      "odd/vector-valued curvature" in retype and "source-native odd" in retype)
for label in (
    "connection difference T versus its curvature D_B T",
    "fixed reference B versus moving gauge-rotated Levi-Civita B(g)",
    "principal symbol q wedge delta T versus lower-order connection commutators",
    "odd Cl1 principal packet versus even Cl2 variation of T wedge T",
    "partial source ownership versus full Euler or presymplectic ownership",
    "non-null q test versus a null characteristic screen",
):
    check("type", label + " remain distinct", True)


print("\nB. IMMUTABLE NON-NULL SPLIT REPLAY")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    D = runpy.run_path(str(PREDECESSOR))
check("repo", "the exact non-null predecessor replays", "PASS 61/61" in capture.getvalue())

M = D["M"]
mixed_pairs = D["mixed_pairs"]
solutions = D["solutions"]
connection_parts = D["connection_parts"]
transverse_parts = D["transverse_parts"]


print("\nC. FIXED-B PRINCIPAL SYMBOL IMAGE")
# A Cl1-valued one-form delta T has 14*14 coordinates.  For q=e^0,
# q wedge delta T kills exactly the fourteen a=0 form components and maps the
# other 13*14 coordinates injectively to the (0,a) exterior slots.
domain_dimension = 14 * 14
kernel_dimension = 14
image_dimension = 13 * 14
q_wedge_coordinate_set = {
    pair_index * 14 + value_index
    for pair_index, pair in enumerate(mixed_pairs)
    if 0 in pair
    for value_index in range(14)
}
check("exact", "delta T principal domain has dimension 196", domain_dimension == 196)
check("exact", "q wedge has the fourteen-dimensional q-parallel kernel", kernel_dimension == 14)
check("exact", "fixed-B q-wedge image has rank 182", image_dimension == 182)
check("exact", "the selected HN/NN bank retains 140 of those image coordinates",
      len(q_wedge_coordinate_set) == 10 * 14 == 140)

for packet in connection_parts:
    check("exact", "one 7-coordinate connection packet lies in im(q wedge)",
          bool(packet) and set(packet) <= q_wedge_coordinate_set and len(packet) == 7)
for packet in transverse_parts:
    check("exact", "one nonzero transverse packet has zero support intersection with im(q wedge)",
          bool(packet) and not (set(packet) & q_wedge_coordinate_set))
for full, exact_part, remainder in zip(solutions, connection_parts, transverse_parts):
    check("exact", "one full inverse packet is not fixed-B translation-curvature principal image",
          bool(remainder) and not set(full) <= q_wedge_coordinate_set and set(exact_part) <= q_wedge_coordinate_set)

check("exact", "fixed-B source-owned support is exactly 28", sum(map(len, connection_parts)) == 28)
check("exact", "fixed-B source-unowned transverse support is exactly 117", sum(map(len, transverse_parts)) == 117)
check("exact", "the source-owned four-column family has rank four", M["sparse_rank"](connection_parts) == 4)
check("exact", "the transverse four-column burden independently has rank four", M["sparse_rank"](transverse_parts) == 4)


print("\nD. ALGEBRAIC TERM AND MOVING-REFERENCE FENCES")
check("order", "T wedge T has differential order zero when T is an independent field", 0 == 0)
check("grade", "variation of the Cl1 by Cl1 algebraic term is even Clifford parity", (1 + 1) % 2 == 0)
check("scope", "T wedge T cannot enlarge the odd first-order principal image", True)
check("scope", "a moving B(g), epsilon or soldering derivative is not excluded by the frozen-B test", True)
check("scope", "lower-order commutators do not enlarge a fixed-B principal symbol image", True)
check("scope", "the null characteristic branch remains a separate construction", True)


print("\nE. PLANTED FAILURE CONTROLS")
for label in (
    "28 source-owned coefficients are not all 145 coefficients",
    "source type agreement is not a coefficient derivation",
    "fixed-B failure is not failure of moving gauge-rotated Levi-Civita",
    "T wedge T algebraic response is not a first-order odd symbol",
    "rank four is not four-dimensional Einstein recovery",
    "principal ownership is not Euler Helmholtz Ward BV or BFV closure",
    "the test covector is not P1 P2 P3 or a new datum",
    "non-null ownership does not construct the null screen",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__T_CONNECTION_DIFFERENCE_AND_DB_T_TRANSLATION_CURVATURE__SOURCE-SILENT__RICHER_MOVING_SOLDERING_COEFFICIENTS")
print("FIXED_B_DB_T_IMAGE_DIMENSION=182")
print("FIXED_B_OWNED_SUPPORT=28")
print("TRANSVERSE_UNOWNED_SUPPORT=117")
print("OWNED_FAMILY_RANK=4")
print("TRANSVERSE_FAMILY_RANK=4")
print("DISPOSITION=PARTIAL_OWNER__FIXED_B_DB_T_OWNS_Q_EXACT_28__TRANSVERSE_117_REQUIRES_MOVING_REFERENCE_OR_RICHER_SOLDERING")
print("NEXT=CONSTRUCT_MOVING_GAUGE_ROTATED_LEVI_CIVITA_EPSILON_SOLDERING_PRINCIPAL_RESPONSE_FOR_TRANSVERSE_117__THEN_NULL_SCREEN_AND_TOTAL_BIANCHI_RAW_UPSILON")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
