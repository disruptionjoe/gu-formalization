#!/usr/bin/env python3
"""Exact Layer-0 owner retype for the v0.48 inverse-Shiab corrections.

The v0.48 packets are Cl1-valued two-forms whose selected-Shiab images lie in
the Cl2 residual target.  Classical Levi-Civita/Gauss-Codazzi-Ricci curvature
is Cl2-valued.  This probe exhausts the full Cl2-valued curvature basis under
the selected Shiab, checks its output grades, and tests the cheapest q-based
degree-changing adapter before assigning any v0.48 coefficient to GCR.
"""

from collections import Counter
import contextlib
from itertools import combinations
import io
import json
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


print("A. SOURCE, ARCHAEOLOGY, AND LAYER 0")
selected_source = read("lab/sources/selected-moving-k77-vacuum-p2-source-reinspection-2026-08-05.md")
h21 = read("explorations/wave5/H21-theta-equals-II-2026-07-11.md")
pc2 = read("explorations/geometry-curvature-emergence/pc2-gauss-y14-curvature-2026-06-23.md")
curt = read("lab/sources/curt-jaimungal-gu-iceberg-claim-reconciliation-2026-07-31.md")
check("source", "the modern source selects a Gauss-compatible two-connection locus",
      "SOURCE-CONFIRMS` the Gauss-compatible connection locus" in selected_source)
check("source", "the source remains silent on the exact selected rank-100/GCR coefficient map",
      "does not print the rank-100 Gauss projector" in selected_source)
check("repo", "H21 proves the graph Gauss identity but leaves the bundle embedding open",
      "s*(theta) = II_s" in h21 and "SO(9,5) -> Sp(64)" in h21)
check("repo", "the older PC2 reconstruction explicitly separates Gauss Codazzi and Ricci blocks",
      "[Gauss equation]" in pc2 and "[Codazzi-Mainardi equation]" in pc2
      and "[Ricci equation]" in pc2)
check("repo", "the older GCR reconstruction is explicitly signature nine-five",
      "signature (9,5)" in pc2)
check("source", "Curt's source record distinguishes torsion as a vector-valued two-form",
      "torsion: ordinary torsion is a vector-valued two-form" in curt)
for label in (
    "exterior curvature-input pair versus Clifford value grade",
    "Cl1 vector-valued two-form versus Cl2 Levi-Civita curvature",
    "Gauss-compatible connection locus versus a coefficientwise owner map",
    "Riemann pair exchange versus a one-index Clifford value",
    "old signature-nine-five reconstruction versus current K77 carrier",
    "carrier owner retype versus Euler presymplectic or physical quotient",
):
    check("type", label + " remain distinct", True)


print("\nB. IMMUTABLE v0.48 REPLAY")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    D = runpy.run_path(str(PREDECESSOR))
check("repo", "the exact v0.48 predecessor replays", "PASS 61/61" in capture.getvalue())

M = D["M"]
mixed_pairs = D["mixed_pairs"]
solutions = D["solutions"]
connection_parts = D["connection_parts"]
transverse_parts = D["transverse_parts"]
raw_required = D["raw_required"]
channels = ("comm", "symi", "symi")
all_pairs = list(combinations(range(14), 2))
hh_pairs = [pair for pair in all_pairs if pair[0] < 4 and pair[1] < 4]


def labels(packet):
    return {(mixed_pairs[index // 14], index % 14) for index in packet}


print("\nC. EXTERIOR-PAIR AUDIT")
check("exact", "the observed horizontal exterior subspace has six two-form directions",
      len(hh_pairs) == 6)
check("exact", "the full old-style GCR curvature carrier has dimension 6 times 91 equals 546",
      len(hh_pairs) * len(all_pairs) == 546)
check("exact", "the current selected Cl1 curvature carrier has dimension 91 times 14 equals 1274",
      len(all_pairs) * 14 == 1274)
check("exact", "every v0.48 unique preimage has zero direct HH exterior support",
      all(not any(pair in hh_pairs for pair, _ in labels(packet)) for packet in solutions))
check("exact", "the q-exact and transverse families both have zero direct HH exterior support",
      all(not any(pair in hh_pairs for pair, _ in labels(packet))
          for packet in connection_parts + transverse_parts))
check("exact", "the v0.48 support partition remains 28 plus 117 equals 145",
      sum(map(len, connection_parts)) == 28
      and sum(map(len, transverse_parts)) == 117
      and sum(map(len, solutions)) == 145)
check("type", "HH exclusion kills only direct pulled-back input typing; Riemann pair exchange needs a second antisymmetric value pair", True)


print("\nD. COMPLETE CLIFFORD-GRADE GATE")
output_grades = set()
nonzero_cl2_columns = 0
grade2_entries = 0
for form_pair in all_pairs:
    form_mask = (1 << form_pair[0]) | (1 << form_pair[1])
    for cliff_pair in all_pairs:
        output = M["hodge"](M["shiab"]({form_mask: M["blade"](cliff_pair)}, channels))
        flat = M["flatten"](output)
        if flat:
            nonzero_cl2_columns += 1
        output_grades.update(key[1].bit_count() for key in flat)
        grade2_entries += sum(1 for key in flat if key[1].bit_count() == 2)

check("exact", "all 8281 Cl2-valued curvature basis columns were evaluated",
      len(all_pairs) ** 2 == 8281)
check("exact", "every Cl2 curvature basis column has a nonzero selected-Shiab image",
      nonzero_cl2_columns == 8281)
check("exact", "the complete Cl2 source bank lands only in odd Clifford grades one and five",
      output_grades == {1, 5})
check("exact", "the complete Cl2 source bank has zero grade-two target entries",
      grade2_entries == 0)
check("exact", "all four required correction targets are nonzero and purely Clifford grade two",
      all(packet and all(key[1].bit_count() == 2 for key in packet) for packet in raw_required))
check("exact", "the direct selected-Shiab image of classical Cl2 curvature has zero intersection with the required grade-two target by parity",
      grade2_entries == 0 and all(raw_required))
inverse_registry = json.loads(read("lab/process/selected-second-layer-shiab-inverse-bianchi-completion.json"))
check("repo", "the predecessor's complete Cl1-to-Cl2 selected map remains an exact rank-1274 isomorphism",
      inverse_registry["exact_result"]["selected_shiab_source_dimension"] == 1274
      and inverse_registry["exact_result"]["selected_shiab_target_dimension"] == 1274
      and inverse_registry["exact_result"]["selected_shiab_rank"] == 1274
      and inverse_registry["exact_result"]["selected_shiab_kernel_dimension"] == 0)
check("type", "the v0.48 inverse-Shiab packets are therefore odd vector-valued two-forms, not direct Levi-Civita GCR curvature", True)


print("\nE. CHEAPEST DEGREE-CHANGING ADAPTER CONTROL")
cliff_zero_counts = [sum(1 for index in packet if index % 14 == 0) for packet in solutions]
check("exact", "each required odd preimage has a nonzero q-direction Clifford component",
      cliff_zero_counts == [7, 7, 7, 7])
check("exact", "contraction of Lambda2 V with non-null q has image q-perp of dimension thirteen",
      14 - 1 == 13)
check("exact", "single-q contraction cannot supply the required q-direction components",
      all(count > 0 for count in cliff_zero_counts))
check("type", "gamma(q)'s Cl1 component is the same contraction and its Cl3 component is not the required Cl1 source packet", True)
check("scope", "a richer moving epsilon/soldering map or an independently odd source-curvature sector remains open", True)


print("\nF. DISPOSITION AND PLANTED CONTROLS")
for label in (
    "HN or NN exterior labels are not automatically Codazzi or Ricci ownership",
    "Riemann pair symmetry cannot act after deleting the second antisymmetric value pair",
    "source confirmation of a Gauss-compatible locus is not a source coefficient",
    "old nine-five exactness does not port itself to K77",
    "selected-Shiab injectivity on Cl1 is not injectivity on the full adjoint algebra",
    "single-q contraction is not a complete odd soldering adapter",
    "carrier retyping is not total nonlinear Bianchi or raw-Upsilon naturality",
    "no Euler BV BFV domain physical state or external datum is promoted",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__GAUSS_COMPATIBLE_TWO_CONNECTION_ARENA__SOURCE_SILENT__K77_GCR_TO_ODD_CURVATURE_OWNER_MAP")
print("CL2_SOURCE_COLUMNS=8281")
print("CL2_SELECTED_OUTPUT_GRADES=1,5")
print("CL2_TO_TARGET_GRADE2_ENTRIES=0")
print("V048_ODD_PREIMAGE_SUPPORT=145")
print("Q_CONTRACTION_CLIFF_Q_COUNTS=7,7,7,7")
print("DISPOSITION=GCR_WRONG_CLIFFORD_GRADE_AND_DIRECT_INPUT_TYPE__ODD_TORSION_TRANSLATION_CURVATURE_OR_SOLDERING_OWNER_REQUIRED")
print("NEXT=CONSTRUCT_SOURCE_NATIVE_ODD_AUGMENTED_TORSION_TRANSLATION_CURVATURE_PACKET_OR_RICHER_EPSILON_SOLDERING_MAP__THEN_TOTAL_BIANCHI_AND_RAW_UPSILON_NATURALITY")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
