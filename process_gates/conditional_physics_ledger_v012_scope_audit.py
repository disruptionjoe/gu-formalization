#!/usr/bin/env python3
"""Fail-closed wiring audit for conditional-physics ledger v0.12."""

from collections import Counter
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def strict(relative: str):
    path = ROOT / relative
    def pairs(items):
        keys = [key for key, _ in items]
        assert len(keys) == len(set(keys)), f"duplicate key in {path}"
        return dict(items)
    return json.loads(path.read_text(), object_pairs_hook=pairs)


v11p = ROOT / "lab/process/conditional-physics-ledger-v0.11.json"
v11 = strict("lab/process/conditional-physics-ledger-v0.11.json")
v12 = strict("lab/process/conditional-physics-ledger-v0.12.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
registry = strict("lab/process/selected-moving-k77-vacuum-p2-norm-placement.json")
lanes = (ROOT / "LANES.yaml").read_text()
view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.12.md").read_text()
report = (ROOT / "explorations/conditional-build/selected-moving-k77-vacuum-p2-norm-placement-2026-08-05.md").read_text()
source = (ROOT / "lab/sources/selected-moving-k77-vacuum-p2-source-reinspection-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-selected-moving-k77-vacuum-p2-norm-review.md").read_text()

rows11 = {row["id"]: row for row in v11["rows"]}
rows12 = {row["id"]: row for row in v12["rows"]}
active = [row for row in rows12.values() if row.get("row_status") != "SUPERSEDED"]
changed = {row_id for row_id in rows11 if rows11[row_id] != rows12[row_id]}
migrations = [m for m in v12["migrations"] if m.get("to_version") == "0.12"]
directive = contract["active_scientific_directives"][0]
expected = {"LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR3", "LT-GR5", "LT-GR6"}

assert hashlib.sha256(v11p.read_bytes()).hexdigest() == "9495e1279ef26dfb4360ad36ce4240ae44b804d91c42312a897be807486ce954"
assert v12["schema_version"] == "0.12"
assert v12["predecessor"].endswith("conditional-physics-ledger-v0.11.json")
assert set(rows11) == set(rows12) and changed == expected
assert {m["row_id"] for m in migrations} == expected
assert len(active) == 82 and len(rows12) == 83
assert Counter(row["axis"] for row in active) == {
    "REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26
}
assert Counter(row["verdict"] for row in active) == {
    "SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6
}
assert all(row["reason_kind"] in v12["taxonomy"]["verdict_kinds"][row["verdict"]]
           for row in active)
assert v12["residue"]["continuous_real"] == 84
assert v12["residue"]["function_valued_at_least"] == 19
assert v12["residue"]["open_discrete_forks"] == 9
assert v12["residue"]["open_fork_horn_product"] == 1152
assert v12["residue"]["quotients_ranked"] == 2

assert rows12["LT-GR1"]["verdict"] == "SAME"
assert rows12["LT-GR1"]["reason_kind"] == "DERIVED_CONDITIONAL"
assert "P2_NORM_FULL_II_DERIVED" in rows12["LT-GR1"]["mapping_grade"]
assert "SELECTED_NONCYCLIC_K77_NONZERO_ALGEBRAIC_STATIONARY_BRANCH_EXACT" in rows12["LT-GR2b"]["mapping_grade"]
assert "CANONICAL_GAUSS_FULL_II_NORM_SELECTED" in rows12["LT-GR2c"]["mapping_grade"]
assert "RADIAL_HESSIAN_MINUS_14_KAPPA_1" in rows12["LT-GR2d"]["mapping_grade"]
assert "SELECTS_DISTINCT_MASSIVE_POLE" in rows12["LT-GR3"]["mapping_grade"]
assert "SOURCE_TOTALIZATION_CURRENT_AND_DOMAIN_OPEN" in rows12["LT-GR6"]["mapping_grade"]

assert registry["source_return"] == "SOURCE-CONFIRMS_INGREDIENTS__REPO_DERIVES_COMPOSITION"
assert registry["gauss_norm"]["receiver_rank"] == 100
assert registry["gauss_norm"]["trace_first_quadratic_rank"] == 10
assert registry["selected_vacuum"]["selected_nonzero_branch"] == "t=-kappa_1/312"
assert registry["selected_vacuum"]["radial_hessian"] == "-14*kappa_1"
assert registry["selected_vacuum"]["stable_physical_vacuum"] == "OPEN"
assert registry["residue"]["external_P1_P2_P3"] == "UNCHANGED_UNUSED"

assert contract["standing_ledger"]["ref"].endswith("v0.12.json")
assert contract["standing_ledger"]["human_ref"].endswith("v0.12.md")
assert "conditional-physics-ledger-v0.12.json" in lanes
assert directive["source_return"] == "SOURCE-CONFIRMS"
assert registry["source_return"].startswith("SOURCE-CONFIRMS")
assert directive["next_gate"] == registry["next_gate"]
assert directive["resolved_by"].endswith("selected-moving-k77-vacuum-p2-norm-placement-2026-08-05.md")
assert "SOURCE-CONFIRMS" in source and "REPO-DERIVES-COMPOSITION" in source
assert "\\frac{\\kappa_1}{312}" in report and "-14\\kappa_1" in report
assert "summary_outruns_artifact" in review
assert "rigor_defends_superseded_or_mistyped_object" in review
assert "PASS_WITH_FOUR_MATERIAL_LAYER0_COEFFICIENT_AND_CONTROL_CORRECTIONS" in review
assert "Ledger v0.12" in view and "33 SAME" in view and "9 open discrete forks" in view

print("PASS: v0.12 derives P2_norm/full II on the canonical Gauss sector, records the selected K77 algebraic branch, retires one fork and keeps stability/totalization/domain and external P2_datum open")
