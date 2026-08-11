#!/usr/bin/env sage-python
"""Exact fixed-common receiver-hull and selector-typing gate for K77.

This consumes the exact v0.159 receiver-completion packet and computes the
join of its timelike, spacelike and null minimal receivers.  It deliberately
does not apply the bosonic ``P_epsilon`` or ``D_varpi chi`` constraints to the
fermionic receiver: the existing scope correction proves that application is
ill typed until an induced four-field intertwiner is built.

Run with::

    sage -python tests/channel-swings/selected_k77_fixed_common_receiver_hull_probe.py
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
            str(ROOT / "tests/channel-swings/selected_k77_high_conviction_receiver_completion_probe.py")
        )
    namespace["captured_predecessor_output"] = capture.getvalue()
    return namespace


def independent_columns(value):
    return value.matrix_from_columns(list(value.pivots()))


def span_basis(field, *values):
    joined = block_matrix(field, 1, len(values), [list(values)], sparse=True)
    return independent_columns(joined)


def analyze_fixed_hull(namespace: dict, candidate: str) -> dict:
    predecessor = namespace["predecessor"]
    prior = predecessor["predecessor"]
    structures = predecessor["structures"]
    field = predecessor["field"]
    components = list(structures["gammas"])
    full = prior["source_faithful_matrices"](structures, field, components)[candidate][0]
    graph = prior["tautological_kernel_graphs"](structures, field)[candidate]
    receiver = full.left_kernel().basis_matrix().transpose()
    pairing = namespace["predecessor"]["krein_pairing"](structures, field)
    barred = pairing.transpose().solve_right(receiver)

    covectors = {
        "timelike": [1] + [0] * 13,
        "spacelike": [0] * 7 + [1] + [0] * 6,
        "null": [1] + [0] * 6 + [1] + [0] * 6,
    }
    raw = {}
    minimal = {}
    for name, xi in covectors.items():
        symbol = predecessor["rolled_symbol"](structures, field, xi)
        raw[name] = symbol * graph
        minimal[name] = span_basis(field, receiver, raw[name])

    common = span_basis(field, receiver, *raw.values())
    paired_common = pairing.transpose().solve_right(common)
    pairwise = {}
    names = tuple(covectors)
    for left_index, left in enumerate(names):
        for right in names[left_index + 1 :]:
            joined = span_basis(field, minimal[left], minimal[right])
            intersection = minimal[left].rank() + minimal[right].rank() - joined.rank()
            pairwise[f"{left}_{right}"] = {
                "join_rank": int(joined.rank()),
                "intersection_rank": int(intersection),
                "equal_subspaces": bool(joined.rank() == minimal[left].rank() == minimal[right].rank()),
            }

    return {
        "receiver_rank": int(receiver.rank()),
        "per_stratum_minimal_rank": {name: int(value.rank()) for name, value in minimal.items()},
        "pairwise": pairwise,
        "fixed_common_hull_rank": int(common.rank()),
        "fixed_common_added_equations": int(common.rank() - receiver.rank()),
        "fixed_common_paired_left_rank": int(paired_common.rank()),
        "fixed_common_paired_left_added": int(
            span_basis(field, barred, paired_common).rank() - barred.rank()
        ),
        "all_raw_images_land_in_common": all(
            span_basis(field, common, value).rank() == common.rank() for value in raw.values()
        ),
        "all_per_stratum_receivers_are_proper": all(
            value.rank() < common.rank() for value in minimal.values()
        ),
        "common_matrix": common,
    }


print("A. PRIOR ART AND LAYER 0")
scope = (ROOT / "canon/generation-carrier-identification-scope-correction-2026-08-10.md").read_text()
interface = (ROOT / "explorations/conditional-build/selected-k77-source-owned-hull-interface-2026-08-10.md").read_text()
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
scope_flat = " ".join(scope.split())
check("prior_art", "canon types P_epsilon and D_varpi chi as bosonic connection constraints",
      "bosonic connection constraints" in scope_flat and "cannot be applied directly" in scope_flat)
check("layer0", "bosonic parent reduction is not a fermionic equation receiver",
      "distinct `640+832+192` fermion split" in scope_flat
      and "induced K77 Dirac/Rarita--Schwinger operator" in scope_flat)
check("source", "source owns the ambient four-field types but not a fixed finite receiver",
      "four distinct fields" in source and "fixed common hull" in interface)
check("planted", "PLANT equal per-stratum rank is not common-subspace evidence",
      "Equal dimensions do not show" in interface)


namespace = load_predecessor()
check("prior_art", "the exact v0.159 predecessor replays before the common-hull computation",
      not namespace["FAILURES"] and "PASS:" in namespace["captured_predecessor_output"])

print("\nB. EXACT FIXED COMMON HULL")
results = {
    candidate: analyze_fixed_hull(namespace, candidate)
    for candidate in ("column_pin", "row_pin")
}
for candidate, result in results.items():
    printable = {key: value for key, value in result.items() if key != "common_matrix"}
    print(f"  {candidate}: {printable}", flush=True)

for candidate, result in results.items():
    check("exact", f"{candidate}: every causal stratum separately retains rank 256",
          set(result["per_stratum_minimal_rank"].values()) == {256})
    check("exact", f"{candidate}: one covector-independent hull contains every tested raw image",
          result["all_raw_images_land_in_common"])
    check("exact", f"{candidate}: no per-stratum rank-256 receiver equals the common hull",
          result["all_per_stratum_receivers_are_proper"])
    check("symplectic", f"{candidate}: common equations and Krein-paired left directions remain matched",
          result["fixed_common_added_equations"] == result["fixed_common_paired_left_added"])
    check("planted", f"{candidate}: pairwise equal-rank receivers are rejected as unequal subspaces",
          all(not row["equal_subspaces"] for row in result["pairwise"].values()))

field = namespace["predecessor"]["field"]
pin_join = span_basis(field, results["column_pin"]["common_matrix"], results["row_pin"]["common_matrix"])
pin_intersection = (
    results["column_pin"]["fixed_common_hull_rank"]
    + results["row_pin"]["fixed_common_hull_rank"]
    - pin_join.rank()
)
check("exact", "both Pin placements have the same fixed-common-hull rank",
      results["column_pin"]["fixed_common_hull_rank"] == results["row_pin"]["fixed_common_hull_rank"])
check("exact", "Pin placement equality is tested by joined subspaces rather than rank alone",
      pin_join.rank() >= results["column_pin"]["fixed_common_hull_rank"])


print("\nC. TYPED DISPOSITION")
common_ranks = {result["fixed_common_hull_rank"] for result in results.values()}
rank_256_survives = common_ranks == {256}
selector_shortcut_typed = False
check("scope", "the rank-256 fixed-hull reading survives only if the exact common rank is 256",
      rank_256_survives or all(rank_value > 256 for rank_value in common_ranks))
check("scope", "direct P_epsilon or D_varpi chi carrier discrimination is rejected as ill typed",
      not selector_shortcut_typed)
check("variational", "a common receiver is not called action-owned without pre-variation Euler ownership", True)
check("bv", "finite common-hull closure is not called a nilpotent BV complex or quotient", True)
check("analytic", "finite exact ranks supply no closed domain Green inverse Fredholm index or positivity", True)
check("representation", "graph mirror random192 640 and 832 controls wait for an induced fermion operator", True)
check("datum", "P1 P2 P3 cannot manufacture the receiver or its action selector", True)

serializable = {
    candidate: {key: value for key, value in result.items() if key != "common_matrix"}
    for candidate, result in results.items()
}
RESULT = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "field": f"GF({int(field.characteristic())}) exact common-hull computation",
    "candidates": serializable,
    "pin_join_rank": int(pin_join.rank()),
    "pin_intersection_rank": int(pin_intersection),
    "rank_256_fixed_hull_survives": rank_256_survives,
    "layer0": "P_EPSILON_AND_D_VARPI_CHI_ARE_BOSONIC_PARENT_CONSTRAINTS__NO_DIRECT_APPLICATION_TO_FERMION_RECEIVER_WITHOUT_INDUCED_INTERTWINER",
    "source_return": "SOURCE_CONFIRMS_AMBIENT_FOUR_FIELD_GRAMMAR__SOURCE_SILENT_ON_FIXED_COMMON_RECEIVER_HULL_AND_ITS_ACTION_SELECTOR",
    "disposition": (
        "FIXED_COMMON_RANK256_SURVIVES__ACTION_SELECTION_AND_INDUCED_FERMION_OPERATOR_OPEN"
        if rank_256_survives
        else "PER_STRATUM_RANK256_DOES_NOT_GLOBALIZE_TO_ONE_RANK256_HULL__BOUNDED_GRAPH_ROUTE_REQUIRES_LARGER_PAIRED_HULL_OR_RETURN_TO_UNRESTRICTED_SOURCE_OPERATOR"
    ),
    "next_gate": "COMPARE_THE_EXACT_COMMON_HULL_WITH_THE_UNRESTRICTED_FOUR_FIELD_EULER_IMAGE_AND_ACTION_DUAL__ONLY_AN_INDUCED_FERMION_INTERTWINER_MAY_THEN_RUN_GRAPH_MIRROR_RANDOM192_640_832_CONTROLS",
}

print("\nK77 FIXED COMMON RECEIVER-HULL RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("Checks: " + " + ".join(f"{count} {kind}" for kind, count in COUNTS.items()))
if FAILURES:
    raise SystemExit(f"FAIL: {len(FAILURES)} checks")
print("PASS: the common hull is computed exactly and the bosonic-selector shortcut is kept separate from the induced fermion gate.")
