#!/usr/bin/env python3
"""Exact D7 one-root extension census and ambient-successor ownership gate."""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
import itertools
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
K81_PROBE = ROOT / "tests/channel-swings/selected_k81_rsap_a3_relative_placement_ownership_gate_probe.py"
K85_PROBE = ROOT / "tests/channel-swings/selected_k85_rsap_sustar4_a3_singular_transition_atlas_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k86-rsap-d7-first-deeper-stratum-ownership-gate-2026-08-15.md"
REGISTRY = ROOT / "lab/process/selected-k86-rsap-d7-first-deeper-stratum-ownership-gate.json"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k86-rsap-d7-first-deeper-stratum-ownership-gate-review.md"
K81_REGISTRY = ROOT / "lab/process/selected-k81-rsap-a3-relative-placement-ownership-gate.json"
A3_REGISTRIES = [
    ROOT / "lab/process/selected-k77-rsap-a3-two-wall-census-origin-attachment.json",
    ROOT / "lab/process/selected-k82-rsap-su22-a3-singular-transition-atlas.json",
    ROOT / "lab/process/selected-k83-rsap-su31-a3-singular-transition-atlas.json",
    ROOT / "lab/process/selected-k84-rsap-compact-su4-a3-semisimple-singular-transition-atlas.json",
    ROOT / "lab/process/selected-k85-rsap-sustar4-a3-singular-transition-atlas.json",
]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def root(i: int, j: int, sign_i: int = 1, sign_j: int = -1) -> tuple[int, ...]:
    value = [0] * 7
    value[i], value[j] = sign_i, sign_j
    return tuple(value)


def matrix_rank(rows: list[tuple[int, ...]]) -> int:
    matrix = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    columns = len(matrix[0]) if matrix else 0
    for column in range(columns):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        scale = matrix[rank][column]
        matrix[rank] = [value / scale for value in matrix[rank]]
        for i, row in enumerate(matrix):
            if i != rank and row[column]:
                factor = row[column]
                matrix[i] = [a - factor * b for a, b in zip(row, matrix[rank])]
        rank += 1
    return rank


def in_span(value: tuple[int, ...], basis: list[tuple[int, ...]]) -> bool:
    return matrix_rank(basis + [value]) == matrix_rank(basis)


print("A. PREDECESSORS AND DURABLE FILES")
for name, path, expected in (("k81", K81_PROBE, 46), ("k85", K85_PROBE, 75)):
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        prior = runpy.run_path(str(path))
    check("prior", f"the {name} predecessor replays {expected}/{expected}",
          f'"checks": {expected}' in capture.getvalue()
          and '"failures": []' in capture.getvalue()
          and not prior["FAILURES"])
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. FIXED ABSTRACT A3 INSIDE D7")
d7_roots = {
    root(i, j, sign_i, sign_j)
    for i, j in itertools.combinations(range(7), 2)
    for sign_i in (-1, 1)
    for sign_j in (-1, 1)
}
simple_a3 = [root(0, 1), root(1, 2), root(2, 3)]
a3_roots = {value for value in d7_roots if in_span(value, simple_a3)}
outside = d7_roots - a3_roots
check("root", "D7 has 84 roots", len(d7_roots) == 84)
check("root", "the fixed simple chain spans exactly twelve A3 roots", len(a3_roots) == 12)
check("root", "exactly 72 D7 roots lie outside the fixed A3", len(outside) == 72)
check("root", "the fixed A3 simple roots are linearly independent", matrix_rank(simple_a3) == 3)


print("\nC. COMPLETE ONE-ROOT EXTENSION CENSUS")
extension_root_counts: Counter[int] = Counter()
extension_rank_counts: Counter[int] = Counter()
for beta in outside:
    basis = simple_a3 + [beta]
    subsystem = {value for value in d7_roots if in_span(value, basis)}
    extension_root_counts[len(subsystem)] += 1
    extension_rank_counts[matrix_rank(basis)] += 1

check("census", "every outside root raises subsystem rank from three to four",
      extension_rank_counts == {4: 72})
check("census", "the exact root-count distribution is 14:12, 20:48, 24:12",
      extension_root_counts == {14: 12, 20: 48, 24: 12})
check("census", "fourteen roots identify A3+A1", 12 + 2 == 14)
check("census", "twenty roots identify A4", 4 * 5 == 20)
check("census", "twenty-four roots identify D4", 2 * 4 * 3 == 24)
check("census", "the three extension multiplicities exhaust all outside roots",
      sum(extension_root_counts.values()) == 72)

orthogonal_roots = {
    value for value in outside
    if all(sum(a * b for a, b in zip(value, alpha)) == 0 for alpha in simple_a3)
}
connecting_roots = {
    value for value in outside
    if any(value[i] for i in range(4)) and any(value[i] for i in range(4, 7))
}
internal_plus_roots = outside - orthogonal_roots - connecting_roots
check("census", "the twelve orthogonal roots give the A3+A1 extensions",
      len(orthogonal_roots) == 12)
check("census", "the forty-eight connecting roots give the A4 extensions",
      len(connecting_roots) == 48)
check("census", "the twelve internal plus-roots give the D4 extensions",
      len(internal_plus_roots) == 12)


print("\nD. CENTRALIZER AND POINTWISE RANK CEILINGS")
candidate_rows = {
    "A3+A1": {"roots": 14, "centralizer": 21, "target_rank": 70, "map_ceiling": 84},
    "A4": {"roots": 20, "centralizer": 27, "target_rank": 64, "map_ceiling": 81},
    "D4": {"roots": 24, "centralizer": 31, "target_rank": 60, "map_ceiling": 79},
}
for name, row in candidate_rows.items():
    check("rank", f"{name} centralizer dimension is rank(D7)+root count",
          row["centralizer"] == 7 + row["roots"])
    check("rank", f"{name} ambient orbit rank is 91-centralizer dimension",
          row["target_rank"] == 91 - row["centralizer"])
    check("rank", f"{name} map-rank ceiling obeys 2s <= 98+r",
          row["map_ceiling"] == (98 + row["target_rank"]) // 2)
check("rank", "the A3-origin row is target/map rank 72/85",
      85 == (98 + 72) // 2)
check("rank", "the forced losses below the A3-origin ceiling are 1, 4 and 6",
      [85 - candidate_rows[name]["map_ceiling"] for name in ("A3+A1", "A4", "D4")]
      == [1, 4, 6])
check("rank", "A3+A1 is nearest only by target-rank order",
      candidate_rows["A3+A1"]["target_rank"]
      > candidate_rows["A4"]["target_rank"]
      > candidate_rows["D4"]["target_rank"])


print("\nE. LOCAL A3 CARRIERS DO NOT OWN THE AMBIENT SUCCESSOR")
a3_registries = [load(path) for path in A3_REGISTRIES]
carriers = [
    registry.get("transitions", registry.get("three_wall_origin", {})).get("carrier", "")
    for registry in a3_registries
]
check("local", "all five completed local A3 models retain an abstract S72 factor",
      len(carriers) == 5 and all("S72" in carrier for carrier in carriers))
check("local", "all five completed local A3 models retain an unlabelled T*R4 complement",
      all("T*R4" in carrier for carrier in carriers))
check("local", "none of the five carrier strings selects an extra ambient D7 root",
      all("A3+A1" not in carrier and "A4" not in carrier and "D4" not in carrier
          for carrier in carriers))

k81 = load(K81_REGISTRY)
missing = k81["missing_joint_type"]
check("owner", "K81 provides no selected split support map",
      missing["selected_split_support_map"] == "NOT_PROVIDED")
check("owner", "K81 provides no selected SU22 support map",
      missing["selected_su22_support_map"] == "NOT_PROVIDED")
check("owner", "K81 records the selected relative orbit as type-missing",
      missing["selected_relative_orbit"] == "TYPE_MISSING")
check("owner", "the source owns no global symplectic realization",
      missing["source_owned_global_symplectic_realization"] is False)


print("\nF. K86 ROUTING AND CLAIM CEILING")
registry = load(REGISTRY)
classification = registry["classification"]
check("schema", "the registry records all 72 one-root extensions",
      classification["outside_root_count"] == 72)
check("schema", "the registry records the exact three-way multiplicity census",
      {row["type"]: row["extension_root_multiplicity"]
       for row in classification["one_root_extensions"]}
      == {"A3+A1": 12, "A4": 48, "D4": 12})
check("schema", "the registry labels A3+A1 as nearest but not selected",
      classification["nearest_by_target_rank"] == "A3+A1"
      and classification["selected_ambient_successor"] == "TYPE_MISSING")
check("schema", "candidate ceiling values are not promoted to achieved ranks",
      all(row["map_rank_status"] == "POINTWISE_CEILING_NOT_ACHIEVED_CONSTRUCTION"
          for row in registry["rank_schedule"]["candidate_rows"]))

ownership = registry["ownership"]
for key in ("selected_a3_ambient_embedding", "selected_extra_root",
            "ambient_degeneration_path", "successor_real_form"):
    check("owner", f"{key} is explicitly missing", ownership[key] == "NOT_PROVIDED")
check("owner", "the actual first deeper stratum remains type-missing",
      ownership["actual_first_deeper_ambient_stratum"] == "TYPE_MISSING")

conditional = registry["conditional_a3xa1_template"]
check("conditional", "the formal A3+A1 product has dimension 98",
      sum(conditional["dimension_terms"]) == 98)
check("conditional", "the formal joint-origin map-rank arithmetic is 84",
      sum(conditional["map_rank_terms"]) == 84)
check("conditional", "the formal product is neither constructed nor attached",
      conditional["status"] == "DIMENSIONAL_TEMPLATE_ONLY__NOT_CONSTRUCTED__NOT_ATTACHED")

scope = registry["scope"]
check("scope", "all completed local A3 atlases remain unchanged",
      scope["completed_local_a3_atlases"] == "UNCHANGED")
check("scope", "no ambient atlas edge is added", scope["ambient_successor_edge"] == "DO_NOT_ADD")
check("scope", "cross-real-form incidence remains type-missing",
      scope["cross_real_form_incidence"] == "TYPE_MISSING_NOT_REOPENED")
check("scope", "zero charge is the next independent local gate",
      scope["zero_charge_rank_at_most_49"] == "OPEN_NEXT_AS_AN_INDEPENDENT_LOCAL_GATE")
check("scope", "global RSAP remains open and the fallback remains 182D",
      scope["global_all_strata_rsap"] == "OPEN"
      and scope["all_charge_fallback_dimension"] == 182)
check("review", "hostile review preserves the type-missing ceiling",
      "PASS_WITH_EXACT_THREE_WAY_CENSUS_AND_TYPE_MISSING_SUCCESSOR_CEILING"
      in REVIEW.read_text(encoding="utf-8"))


print("\nSUMMARY")
print(json.dumps({
    "checks": sum(COUNTS.values()),
    "failures": FAILURES,
    "groups": dict(sorted(COUNTS.items())),
}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
