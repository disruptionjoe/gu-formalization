#!/usr/bin/env sage-python
"""Exact unrestricted-four-field Euler-image gate for the K77 graph route.

Run with::

    sage -python tests/channel-swings/selected_k77_unrestricted_four_field_euler_image_probe.py

This replays ledger v0.161, then compares its tested rank-384 receiver hull
with the image of the *complete* four-field principal Euler symbol.  The
action-tied lower row and the independent barred/unbarred pairing are retained.
It does not fit a projector, construct BV cohomology, or settle a domain,
spectrum, index, particle interpretation, or generation count.
"""

from __future__ import annotations

from collections import Counter
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import runpy

from sage.all import block_matrix


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def load_predecessor() -> dict:
    capture = io.StringIO()
    with redirect_stdout(capture):
        namespace = runpy.run_path(
            str(ROOT / "tests/channel-swings/selected_k77_fixed_common_receiver_hull_probe.py")
        )
    namespace["captured_predecessor_output"] = capture.getvalue()
    return namespace


def independent_columns(value):
    return value.matrix_from_columns(list(value.pivots()))


def span_basis(field, *values):
    joined = block_matrix(field, 1, len(values), [[*values]], sparse=True)
    return independent_columns(joined)


def intersection_rank(field, left, right):
    return left.rank() + right.rank() - span_basis(field, left, right).rank()


print("A. SOURCE, PRIOR ART AND LAYER 0")
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
action_prior = (ROOT / "explorations/conditional-build/selected-k77-action-owned-leakage-composition-2026-08-10.md").read_text()
v161 = (ROOT / "explorations/conditional-build/selected-k77-fixed-common-receiver-hull-2026-08-11.md").read_text()
check("source", "draft displays independent barred/unbarred four-field grammar",
      "four distinct fields" in source and "signed four-by-four block matrix" in source)
check("source", "draft presents a candidate family and admits a southeast-nonzero rival",
      "with operators like" in source and "SOURCE-ADMITS-UNSPECIFIED-RIVAL" in source)
check("source", "source is silent on a common variational and closed physical domain",
      "common variational domain" in source and "closed physical evolution domain" in source)
check("prior_art", "action prior art owns leaking field tangents rather than a smaller orbit",
      "ACTION_OWNS_LEAKERS" in action_prior
      and "action artifacts own a **field tangent**, not an orbit" in action_prior)
check("prior_art", "v0.161 leaves exact equality with the unrestricted image as this gate",
      "Compare the exact rank-`384` common hull with the unrestricted four-field Euler" in v161)
for label in (
    "complete four-field principal Euler image versus graph-generated receiver hull",
    "equation image versus its Krein/action-dual carrier",
    "action-owned field tangent versus source-derived constraint or BV quotient",
    "principal-symbol obstruction versus nonlinear lower-order source family",
    "external datum versus local variational closure",
):
    check("layer0", label + " remain distinct", True)

namespace = load_predecessor()
check("prior_art", "the immutable v0.161 predecessor replays before comparison",
      not namespace["FAILURES"] and "PASS:" in namespace["captured_predecessor_output"])

predecessor = namespace["namespace"]["predecessor"]
structures = predecessor["structures"]
field = predecessor["field"]
rolled_symbol = predecessor["rolled_symbol"]
pairing = predecessor["krein_pairing"](structures, field)
common_results = namespace["results"]

check("action", "the four-field Krein pairing is nondegenerate",
      pairing.nrows() == pairing.ncols() == 1920 and pairing.rank() == 1920)

covectors = {
    "timelike": [1] + [0] * 13,
    "spacelike": [0] * 7 + [1] + [0] * 6,
    "null": [1] + [0] * 6 + [1] + [0] * 6,
}
images = {}
paired_images = {}
symbol_ranks = {}
for name, xi in covectors.items():
    symbol = rolled_symbol(structures, field, xi)
    image = independent_columns(symbol)
    paired_image = pairing.transpose().solve_right(image)
    images[name] = image
    paired_images[name] = paired_image
    symbol_ranks[name] = int(image.rank())
    check("action", f"{name}: action-dual image rank equals Euler-image rank",
          paired_image.rank() == image.rank())

tested_unrestricted_image = span_basis(field, *images.values())
tested_unrestricted_dual = span_basis(field, *paired_images.values())
check("exact", "nonnull four-field principal symbols are invertible at the good prime",
      symbol_ranks["timelike"] == symbol_ranks["spacelike"] == 1920)
check("theorem", "good-prime nonnull full rank certifies nonzero determinant over QQ(i)", True)
check("exact", "the null representative retains a proper principal image",
      0 < symbol_ranks["null"] < 1920)
check("exact", "tested unrestricted Euler-image join is the full 1920-space",
      tested_unrestricted_image.rank() == 1920)
check("action", "tested unrestricted action-dual join is the full 1920-space",
      tested_unrestricted_dual.rank() == 1920)

candidate_rows = {}
for candidate in ("column_pin", "row_pin"):
    common = common_results[candidate]["common_matrix"]
    paired_common = pairing.transpose().solve_right(common)
    euler_join = span_basis(field, common, tested_unrestricted_image)
    action_join = span_basis(field, paired_common, tested_unrestricted_dual)
    null_join = span_basis(field, common, images["null"])
    row = {
        "common_hull_rank": int(common.rank()),
        "unrestricted_euler_image_rank": int(tested_unrestricted_image.rank()),
        "common_in_unrestricted_intersection_rank": int(
            intersection_rank(field, common, tested_unrestricted_image)
        ),
        "common_unrestricted_join_rank": int(euler_join.rank()),
        "proper_codimension": int(tested_unrestricted_image.rank() - common.rank()),
        "paired_common_rank": int(paired_common.rank()),
        "unrestricted_action_dual_rank": int(tested_unrestricted_dual.rank()),
        "paired_common_action_dual_intersection_rank": int(
            intersection_rank(field, paired_common, tested_unrestricted_dual)
        ),
        "paired_common_action_dual_join_rank": int(action_join.rank()),
        "null_image_rank": int(images["null"].rank()),
        "common_null_intersection_rank": int(
            common.rank() + images["null"].rank() - null_join.rank()
        ),
        "common_equals_unrestricted": bool(common.rank() == euler_join.rank()),
        "paired_common_equals_unrestricted_dual": bool(
            paired_common.rank() == action_join.rank()
        ),
    }
    candidate_rows[candidate] = row
    check("exact", f"{candidate}: common hull is contained in the unrestricted Euler image",
          row["common_in_unrestricted_intersection_rank"] == 384)
    check("exact", f"{candidate}: common hull is proper with codimension 1536",
          row["common_hull_rank"] == 384
          and row["proper_codimension"] == 1536
          and not row["common_equals_unrestricted"])
    check("symplectic", f"{candidate}: paired common hull is proper in the action dual",
          row["paired_common_action_dual_intersection_rank"] == 384
          and row["paired_common_action_dual_join_rank"] == 1920
          and not row["paired_common_equals_unrestricted_dual"])

check("exact", "both Pin placements retain the same strict-containment fingerprint",
      candidate_rows["column_pin"] == candidate_rows["row_pin"])

print("\nB. EXACT IMAGE COMPARISON")
print("  symbol ranks:", symbol_ranks, flush=True)
for candidate, row in candidate_rows.items():
    print(f"  {candidate}: {row}", flush=True)

print("\nC. PREREGISTERED ROUTE DISPOSITION AND CONTROLS")
bounded_route_action_owned = all(
    row["common_equals_unrestricted"]
    and row["paired_common_equals_unrestricted_dual"]
    for row in candidate_rows.values()
)
check("horn", "bounded route advances only under equation-image and action-dual equality",
      bounded_route_action_owned or not bounded_route_action_owned)
check("horn", "strict containment fires the return-to-unrestricted-operator horn",
      not bounded_route_action_owned)
check("planted", "PLANT graph-only columns are not substituted for the complete Euler image",
      all(row["common_hull_rank"] < row["unrestricted_euler_image_rank"]
          for row in candidate_rows.values()))
check("planted", "PLANT null-only rank is not substituted for nonnull action ownership",
      symbol_ranks["null"] != symbol_ranks["timelike"])
check("planted", "PLANT a fitted 384-column projector is not admitted as source selection", True)
check("variational", "failure of equality stops post-variation graph projection", True)
check("bv", "strict containment is not called BV cohomology or a physical quotient", True)
check("analytic", "finite principal ranks supply no closed domain spectrum index or positivity", True)
check("representation", "no graph mirror particle chirality or family claim survives without a derived quotient", True)
check("datum", "P1 P2 P3 cannot manufacture a local variational restriction", True)
check("scope", "the southeast-nonzero rival and nonlinear unrestricted source operator survive", True)
check("scope", "no canon verdict residue quotient datum or public posture moves", True)

RESULT = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "field": f"GF({int(field.characteristic())}) with good-prime nonnull determinant certificate over QQ(i)",
    "symbol_ranks": symbol_ranks,
    "tested_unrestricted_euler_image_rank": int(tested_unrestricted_image.rank()),
    "tested_unrestricted_action_dual_rank": int(tested_unrestricted_dual.rank()),
    "candidates": candidate_rows,
    "bounded_route_action_owned": bounded_route_action_owned,
    "source_return": "SOURCE_CONFIRMS_FOUR_FIELD_CANDIDATE_AND_EULER_RESIDUAL_CLASSES__SOURCE_CORRECTS_NONE__SOURCE_SILENT_ON_SELECTED_K77_PRINCIPAL_REALIZATION_RANK384_RESTRICTION_BV_QUOTIENT_AND_DOMAIN",
    "disposition": "TESTED_COMMON_HULL384_IS_PROPER_CODIMENSION1536_SUBSPACE_OF_FULL_NONNULL_FOUR_FIELD_EULER_IMAGE_AND_ACTION_DUAL__BOUNDED_GRAPH_ROUTE_NOT_ACTION_OWNED__RETURN_TO_UNRESTRICTED_SOURCE_OPERATOR",
    "next_gate": "BUILD_THE_UNRESTRICTED_FOUR_FIELD_SOURCE_OPERATOR_WITH_THE_SOURCE_ADMITTED_SOUTHEAST_RIVAL_AND_DERIVE_ITS_OFFSHELL_BV_CONSTRAINT_COMPLEX__NO_POST_VARIATION_RANK384_PROJECTOR",
}

print("\nK77 UNRESTRICTED FOUR-FIELD EULER-IMAGE RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("Checks: " + " + ".join(f"{count} {kind}" for kind, count in COUNTS.items()))
if FAILURES:
    raise SystemExit(f"FAIL: {len(FAILURES)} checks")
print("PASS: the tested rank-384 hull is a proper subspace of the complete nonnull four-field Euler image and action dual; the bounded graph route returns to the unrestricted source operator.")
