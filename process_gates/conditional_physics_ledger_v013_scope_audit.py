#!/usr/bin/env python3
"""Fail-closed wiring audit for conditional-physics ledger v0.13."""

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


v12p = ROOT / "lab/process/conditional-physics-ledger-v0.12.json"
v12 = strict("lab/process/conditional-physics-ledger-v0.12.json")
v13 = strict("lab/process/conditional-physics-ledger-v0.13.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
registry = strict("lab/process/selected-branch-linearized-totalization-current-green-domain.json")
lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text()
view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.13.md").read_text()
report = (ROOT / "explorations/conditional-build/selected-branch-linearized-totalization-current-green-domain-2026-08-05.md").read_text()
source = (ROOT / "lab/sources/selected-branch-totalization-current-source-reinspection-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-selected-branch-totalization-domain-review.md").read_text()

rows12 = {row["id"]: row for row in v12["rows"]}
rows13 = {row["id"]: row for row in v13["rows"]}
active = [row for row in rows13.values() if row.get("row_status") != "SUPERSEDED"]
changed = {row_id for row_id in rows12 if rows12[row_id] != rows13[row_id]}
migrations = [item for item in v13["migrations"] if item.get("to_version") == "0.13"]
directive = contract["active_scientific_directives"][0]
expected = {"LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR3", "LT-GR5", "LT-GR6"}

assert hashlib.sha256(v12p.read_bytes()).hexdigest() == "5c21f4785415f94ce67c47b4570f4c5028124418c6083b414531194eea8ab7a3"
assert v13["schema_version"] == "0.13"
assert v13["predecessor"].endswith("conditional-physics-ledger-v0.12.json")
assert set(rows12) == set(rows13) and changed == expected
assert {item["row_id"] for item in migrations} == expected
assert len(active) == 82 and len(rows13) == 83
assert Counter(row["axis"] for row in active) == {
    "REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26
}
assert Counter(row["verdict"] for row in active) == {
    "SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6
}
assert v13["residue"]["continuous_real"] == 84
assert v13["residue"]["function_valued_at_least"] == 19
assert v13["residue"]["open_discrete_forks"] == 9
assert v13["residue"]["quotients_ranked"] == 2

assert "GAUSS_TRACE_AND_TRACELESS_HESSIANS_EXACT" in rows13["LT-GR2b"]["mapping_grade"]
assert "COMMON_DEFECT_KREIN_GREEN_DOMAIN" in rows13["LT-GR2c"]["mapping_grade"]
assert "TWO_FIELD_CURVATURE_VEV" in rows13["LT-GR2d"]["mapping_grade"]
assert "OPPOSITE_RESIDUES_EXACT" in rows13["LT-GR3"]["mapping_grade"]
assert "DIRECT_PLUS_SOLDERED_CURRENT_CHAIN_TYPED" in rows13["LT-GR6"]["mapping_grade"]

assert registry["source_return"] == "SOURCE-CORRECTS"
assert registry["exact_results"]["gauss_trace_coefficient"] == "100/117*kappa_1"
assert registry["exact_results"]["gauss_traceless_coefficient"] == "124/117*kappa_1"
assert registry["exact_results"]["tt_residues"] == ["1/alpha_II", "-1/alpha_II"]
assert registry["domain"]["ambient_y14_domain"] == "OPEN"
assert registry["domain"]["positive_physical_cohomology"] == "OPEN"

assert contract["standing_ledger"]["ref"].endswith("v0.13.json")
assert contract["standing_ledger"]["human_ref"].endswith("v0.13.md")
assert "conditional-physics-ledger-v0.13.json" in lanes
assert directive["source_return"] == "SOURCE-CORRECTS"
assert directive["next_gate"] == registry["next_gate"]
assert directive["resolved_by"].endswith("selected-branch-linearized-totalization-current-green-domain-2026-08-05.md")
assert "Decisive return: `SOURCE-CORRECTS`" in source
assert "{100\\over117}" in report and "{124\\over117}" in report
assert "SUMMARY_OUTRUNS_ARTIFACT" in review
assert "DEFENDS_SUPERSEDED_OR_MISTYPED_OBJECT" in review
assert "PASS AFTER FOUR MATERIAL SCOPE CORRECTIONS" in review
assert "Ledger v0.13" in view and "33 SAME" in view and "9 open discrete forks" in view

print("PASS: v0.13 separates radial and Gauss Hessians, closes the coupled defect Krein/Green domain, classifies opposite residues, and keeps physical cohomology plus two-field cosmology open")
