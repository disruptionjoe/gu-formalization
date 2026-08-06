#!/usr/bin/env python3
"""Fail-closed wiring audit for conditional-physics ledger v0.14."""

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


v13p = ROOT / "lab/process/conditional-physics-ledger-v0.13.json"
v13 = strict("lab/process/conditional-physics-ledger-v0.13.json")
v14 = strict("lab/process/conditional-physics-ledger-v0.14.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
registry = strict("lab/process/selected-branch-bv-tt-curvature-vev-flrw.json")
lanes = (ROOT / "LANES.yaml").read_text()
view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.14.md").read_text()
report = (ROOT / "explorations/conditional-build/selected-branch-bv-tt-and-curvature-vev-flrw-2026-08-05.md").read_text()
source = (ROOT / "lab/sources/selected-branch-bv-flrw-source-reinspection-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-selected-branch-bv-flrw-review.md").read_text()

rows13 = {row["id"]: row for row in v13["rows"]}
rows14 = {row["id"]: row for row in v14["rows"]}
active = [row for row in rows14.values() if row.get("row_status") != "SUPERSEDED"]
changed = {row_id for row_id in rows13 if rows13[row_id] != rows14[row_id]}
migrations = [item for item in v14["migrations"] if item.get("to_version") == "0.14"]
directive = contract["active_scientific_directives"][0]
expected = {"LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR2e", "LT-GR3", "LT-GR5", "LT-GR6"}

assert hashlib.sha256(v13p.read_bytes()).hexdigest() == "7e910115077e45d9b0d4e28f8237514bdb9792b65f684f1af4deac0c3af88677"
assert v14["schema_version"] == "0.14"
assert v14["predecessor"].endswith("conditional-physics-ledger-v0.13.json")
assert set(rows13) == set(rows14) and changed == expected
assert {item["row_id"] for item in migrations} == expected and len(migrations) == 8
assert len(active) == 82 and len(rows14) == 83
assert Counter(row["axis"] for row in active) == {
    "REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26
}
assert Counter(row["verdict"] for row in active) == {
    "SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6
}
assert v14["residue"]["continuous_real"] == 84
assert v14["residue"]["function_valued_at_least"] == 19
assert v14["residue"]["open_discrete_forks"] == 9
assert v14["residue"]["quotients_ranked"] == 3

assert "SOLDERING_MOD_GAUGE_EXACT" in rows14["LT-GR1"]["mapping_grade"]
assert "FINITE_TREE_KREIN_MAJORANT_POSITIVE" in rows14["LT-GR2b"]["mapping_grade"]
assert "LOCAL_SCALAR_CURVATURE_VEV_TWO_TO_ONE_EXACT" in rows14["LT-GR2c"]["mapping_grade"]
assert "SHIFT_SUSCEPTIBILITY_2_OVER_A_NONSCREENING" in rows14["LT-GR2d"]["mapping_grade"]
assert "SPATIAL_FLATNESS_HOMONYM_FENCED" in rows14["LT-GR2e"]["mapping_grade"]
assert "MASSIVE_EVEN_BV_TT_CLASSES_AT_LEAST_TWO" in rows14["LT-GR3"]["mapping_grade"]
assert "NONLINEAR_CHIMERIC_ODD_OPEN" in rows14["LT-GR6"]["mapping_grade"]

assert registry["source_return"] == "SOURCE-CONFIRMS"
assert registry["exact_results"]["metric_to_levi_civita_symbol_rank"] == 10
assert registry["exact_results"]["massive_partner_even_bv_tt_classes"] == 2
assert registry["exact_results"]["majorant_determinant"] == 1
assert registry["exact_results"]["curvature_shift_susceptibility"] == "2/a"
assert registry["boundaries"]["radiative_screening_local_horn"] == "FAILS"
assert registry["boundaries"]["ambient_global_nonlocal_cosmology_horn"] == "OPEN"

assert contract["standing_ledger"]["ref"].endswith("v0.14.json")
assert contract["standing_ledger"]["human_ref"].endswith("v0.14.md")
assert "conditional-physics-ledger-v0.14.json" in lanes
assert directive["source_return"] == "SOURCE-CONFIRMS"
assert directive["next_gate"] == registry["next_gate"]
assert directive["resolved_by"].endswith("selected-branch-bv-tt-and-curvature-vev-flrw-2026-08-05.md")
assert "Decisive return: `SOURCE-CONFIRMS`" in source
assert "dR/d rho_vac=2/a" in report and "rank ten" in report
assert "SUMMARY_OUTRUNS_ARTIFACT" in review
assert "DEFENDS_SUPERSEDED_OR_MISTYPED_OBJECT" in review
assert "PASS AFTER FIVE MATERIAL SCOPE CORRECTIONS" in review
assert "Ledger v0.14" in view and "33 SAME" in view and "9 open discrete forks" in view

print("PASS: v0.14 wires metric soldering modulo gauge, even-BV TT survival, finite Krein positivity, and local tracking-without-screening while retaining odd, UV and ambient/global fences")
