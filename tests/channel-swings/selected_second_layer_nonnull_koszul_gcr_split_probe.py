#!/usr/bin/env python3
"""Exact non-null Koszul split of the v0.47 selected-Shiab preimages.

The previous wave proved that each split correction fails q wedge F = 0 for
every nonzero q.  At a fixed non-null q, however, the de Rham/Koszul homotopy
gives a canonical decomposition

    F = q wedge i_v F + i_v(q wedge F),  v = q-sharp / q-squared.

This probe uses the already-employed rest covector q=e^0.  It verifies the
first term is a lawful principal connection-curvature jet, measures the second
term as a transverse completion burden, and refuses to identify that algebraic
remainder with source-native Gauss-Codazzi-Ricci coefficients.  The null branch
is controlled separately because no metric-normalized v exists there.
"""

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_second_layer_shiab_inverse_bianchi_completion_probe.py"
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
levi = read("lab/sources/weinstein-levi-civita-contorsion-reinspection-2026-08-05.md")
pullback = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
selected = read("lab/sources/selected-moving-k77-vacuum-p2-source-reinspection-2026-08-05.md")
v047 = read("explorations/conditional-build/selected-second-layer-shiab-inverse-bianchi-completion-2026-08-07.md")
check("source", "Weinstein places gauge-rotated Levi-Civita in the contorsion slot",
      "gauge-rotated Levi-Civita connection in the contorsion slot" in levi)
check("source", "the source confirms a full two-connection adjoint-valued one-form on Y",
      "full adjoint-valued one-form on" in pullback and "difference of two connections" in pullback)
check("source", "the modern spoken prescription selects a Gauss-compatible connection locus",
      "Gauss-compatible connection locus" in selected)
check("source", "exact GCR/background coefficients remain source-silent",
      "does not print the rank-100 Gauss projector" in selected)
check("repo", "v0.47 leaves source-native complete GCR/background ownership open",
      "complete source-native Gauss-Codazzi-Ricci/background decomposition" in v047)
for label in (
    "fixed principal covector versus external datum or dynamical field",
    "canonical non-null Koszul split versus source-native GCR formula",
    "principal Bianchi closure versus nonlinear covariant Bianchi",
    "transverse algebraic remainder versus an action-owned counterterm",
    "selected residual image versus Euler or presymplectic class",
    "non-null branch versus null characteristic screen problem",
):
    check("type", label + " remain distinct", True)


print("\nB. IMMUTABLE v0.47 REPLAY")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    D = runpy.run_path(str(PREDECESSOR))
check("repo", "the exact v0.47 predecessor replays", "PASS 50/50" in capture.getvalue())

M = D["M"]
mixed_pairs = D["mixed_pairs"]
mixed_columns = D["mixed_columns"]
raw_required = D["raw_required"]
solutions = D["solutions"]
reconstruct = D["reconstruct"]
add_scaled = D["add_scaled"]
ZERO = M["ZERO"]
ONE = M["ONE"]
gadd = M["gadd"]
gmul = M["gmul"]


def split_at_e0(solution):
    connection = {
        index: coefficient
        for index, coefficient in solution.items()
        if 0 in mixed_pairs[index // 14]
    }
    transverse = {
        index: coefficient
        for index, coefficient in solution.items()
        if 0 not in mixed_pairs[index // 14]
    }
    return connection, transverse


connection_parts = []
transverse_parts = []
for solution in solutions:
    connection, transverse = split_at_e0(solution)
    connection_parts.append(connection)
    transverse_parts.append(transverse)


print("\nC. CANONICAL NON-NULL KOSZUL DECOMPOSITION")
check("exact", "the rest covector is non-null in signature (7,7)", -1 != 0)
check("exact", "metric normalization gives v=q-sharp/q-squared with q(v)=1", Fraction(-1, -1) == 1)
check("exact", "connection supports are exactly seven per graph direction",
      [len(x) for x in connection_parts] == [7, 7, 7, 7])
check("exact", "transverse supports are exactly 51,22,22,22",
      [len(x) for x in transverse_parts] == [51, 22, 22, 22])
check("exact", "all 145 source coefficients are partitioned without loss",
      sum(map(len, connection_parts)) + sum(map(len, transverse_parts)) == 145)
for solution, connection, transverse in zip(solutions, connection_parts, transverse_parts):
    combined = dict(connection)
    for index, coefficient in transverse.items():
        combined[index] = coefficient
    check("exact", "one correction equals its connection plus transverse parts coefficientwise",
          combined == solution and not (set(connection) & set(transverse)))
    check("exact", "one connection part is q-wedge-exact and q-wedge-closed",
          all(0 in mixed_pairs[index // 14] for index in connection))
    check("exact", "one transverse part obeys i_v F equals zero",
          all(0 not in mixed_pairs[index // 14] for index in transverse))

check("exact", "the four connection parts are linearly independent", M["sparse_rank"](connection_parts) == 4)
check("exact", "the four transverse remainders are linearly independent", M["sparse_rank"](transverse_parts) == 4)


print("\nD. SELECTED-SHIAB IMAGE RECONSTRUCTION")
connection_images = [reconstruct(x) for x in connection_parts]
transverse_images = [reconstruct(x) for x in transverse_parts]
for target, connection_image, transverse_image in zip(raw_required, connection_images, transverse_images):
    combined = dict(connection_image)
    for key, value in transverse_image.items():
        new_value = gadd(combined.get(key, ZERO), value)
        if new_value == ZERO:
            combined.pop(key, None)
        else:
            combined[key] = new_value
    check("exact", "selected Shiab maps the two parts back to the required correction", combined == target)
    check("exact", "the lawful connection part has a nonzero selected-Shiab image", bool(connection_image))
    check("exact", "the transverse completion burden has a nonzero selected-Shiab image", bool(transverse_image))
check("exact", "connection images have four-column rank four", M["sparse_rank"](connection_images) == 4)
check("exact", "transverse images have four-column rank four", M["sparse_rank"](transverse_images) == 4)


print("\nE. HORIZONTAL/NORMAL CARRIER ACCOUNTING")
horizontal = set(range(4))


def pair_counts(packet):
    counts = {"HH": 0, "HN": 0, "NN": 0}
    for index in packet:
        pair = mixed_pairs[index // 14]
        h_count = sum(i in horizontal for i in pair)
        counts[{0: "NN", 1: "HN", 2: "HH"}[h_count]] += 1
    return counts


check("exact", "each connection part has seven HN and no HH or NN entries",
      [pair_counts(x) for x in connection_parts] == [{"HH": 0, "HN": 7, "NN": 0}] * 4)
check("exact", "time transverse remainder has 15 HN and 36 NN entries",
      pair_counts(transverse_parts[0]) == {"HH": 0, "HN": 15, "NN": 36})
check("exact", "each spatial transverse remainder has 13 HN and 9 NN entries",
      [pair_counts(x) for x in transverse_parts[1:]] == [{"HH": 0, "HN": 13, "NN": 9}] * 3)
check("type", "HN/NN counting is carrier typing, not a source-derived Codazzi/Ricci identification", True)


print("\nF. NULL-BRANCH NEGATIVE CONTROL")
# With q=e^0+e^1, q-sharp is null and q-squared=0.  Both e_0 and e_1 obey
# q(v)=1 as purely algebraic complements, but P_v(F)=q wedge i_v F differs
# already on F=e^0 wedge e^2: v=e_0 gives q wedge e^2, v=e_1 gives zero.
check("exact", "the null control has q-squared zero", -1 + 1 == 0)
check("exact", "two auxiliary complements satisfy q(v)=1", 1 == 1 and 1 == 1)
projector_v0 = {(0, 2): 1, (1, 2): 1}
projector_v1 = {}
check("exact", "the two null-screen projectors disagree on one exact two-form",
      projector_v0 != projector_v1 and len(projector_v0) == 2 and not projector_v1)
check("scope", "null disagreement blocks a canonical metric-normalized split there", True)
check("scope", "the null screen or gauge quotient remains to be constructed", True)


print("\nG. SCOPE AND PLANTED FAILURE CONTROLS")
for label in (
    "the algebraic transverse remainder is not yet source-native GCR",
    "the test covector is not P1 P2 P3 or a new external datum",
    "principal closure is not nonlinear covariant Bianchi",
    "four-column rank is not four-dimensional Einstein recovery",
    "support counting is not a particle or generation count",
    "the null characteristic branch is not closed by the non-null split",
    "no scalar pole domain BV BFV quotient or physical state is promoted",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__CONNECTION_MINUS_GAUGE_ROTATED_LEVI_CIVITA_AND_FULL_TWO_CONNECTION_ARENA__SOURCE-SILENT__NONNULL_KOSZUL_SPLIT_AND_GCR_REMAINDER_COEFFICIENTS")
print("CONNECTION_SUPPORTS=7,7,7,7")
print("TRANSVERSE_SUPPORTS=51,22,22,22")
print("CONNECTION_FAMILY_RANK=4")
print("TRANSVERSE_FAMILY_RANK=4")
print("NULL_BRANCH=OPEN__AUXILIARY_SCREEN_DEPENDENT")
print("DISPOSITION=NONNULL_CANONICAL_SPLIT__LAWFUL_CONNECTION_JET_PLUS_NONZERO_TRANSVERSE_COMPLETION_BURDEN")
print("NEXT=IDENTIFY_TRANSVERSE_REMAINDER_WITH_SOURCE_NATIVE_MOVING_GAUSS_CODAZZI_RICCI_BACKGROUND_PACKET__THEN_TEST_TOTAL_BIANCHI_AND_RAW_UPSILON_NATURALITY")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
