#!/usr/bin/env python3
"""Fail-closed wiring audit for conditional-physics ledger v0.11."""

from collections import Counter
import hashlib
import json
from pathlib import Path

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]


def strict(relative: str):
    path = ROOT / relative
    def pairs(items):
        keys = [key for key, _ in items]
        assert len(keys) == len(set(keys)), f"duplicate key in {path}"
        return dict(items)
    return json.loads(path.read_text(), object_pairs_hook=pairs)


v10p = ROOT / "lab/process/conditional-physics-ledger-v0.10.json"
v10 = strict("lab/process/conditional-physics-ledger-v0.10.json")
v11 = strict("lab/process/conditional-physics-ledger-v0.11.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
registry = strict("lab/process/full-norm-pole-split-nonlinear-t-vacuum.json")
view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.11.md").read_text()
report = (ROOT / "explorations/conditional-build/full-norm-pole-split-nonlinear-t-vacuum-2026-08-05.md").read_text()
source = (ROOT / "lab/sources/full-norm-gravity-source-reinspection-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-full-norm-pole-split-nonlinear-t-vacuum-review.md").read_text()

rows10 = {row["id"]: row for row in v10["rows"]}
rows11 = {row["id"]: row for row in v11["rows"]}
active = [row for row in rows11.values() if row.get("row_status") != "SUPERSEDED"]
changed = {row_id for row_id in rows10 if rows10[row_id] != rows11[row_id]}
migrations = [m for m in v11["migrations"] if m.get("to_version") == "0.11"]

assert hashlib.sha256(v10p.read_bytes()).hexdigest() == "e9fe118810f1ed5915d1cae37d27b0a4ce1cadf69542924f1667584790a29040"
assert v11["schema_version"] == "0.11"
assert v11["predecessor"].endswith("conditional-physics-ledger-v0.10.json")
expected = {"LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR3", "LT-GR5", "LT-GR6"}
assert set(rows10) == set(rows11) and changed == expected
assert {m["row_id"] for m in migrations} == expected
assert len(active) == 82 and len(rows11) == 83
assert Counter(row["axis"] for row in active) == {
    "REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26
}
assert Counter(row["verdict"] for row in active) == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6
}
assert all(row["reason_kind"] in v11["taxonomy"]["verdict_kinds"][row["verdict"]]
           for row in active)
assert v11["residue"]["continuous_real"] == 84
assert v11["residue"]["function_valued_at_least"] == 19
assert v11["residue"]["open_discrete_forks"] == 10
assert v11["residue"]["quotients_ranked"] == 2

assert "P2_ACTION_SELECTION_OPEN" in rows11["LT-GR1"]["mapping_grade"]
assert "MASSLESS_PLUS_MASSIVE_SIMPLE_POLES" in rows11["LT-GR2c"]["mapping_grade"]
assert "TWO_NONABELIAN_REAL_BRANCHES_BOTH_SADDLES" in rows11["LT-GR2d"]["mapping_grade"]
assert "DISTINCT_MASSIVE_POLE" in rows11["LT-GR3"]["mapping_grade"]
assert "SOURCE_TOTALIZATION_CURRENT_AND_DOMAIN_OPEN" in rows11["LT-GR6"]["mapping_grade"]

assert registry["source_return"] == "SOURCE-SILENT"
assert registry["gravity"]["pole_count"] == 2
assert registry["gravity"]["pole_multiplicity"] == [1, 1]
assert registry["gravity"]["plus_cross_retained"] is True
assert registry["nonlinear_vacuum_control"]["genuinely_nonlinear_real_branch_count"] == 2
assert registry["nonlinear_vacuum_control"]["stable_minimum_found"] is False
assert registry["nonlinear_vacuum_control"]["selected_moving_k77_frechet_adjoint_vacuum"] == "OPEN"
assert registry["residue"]["P1_P2_P3"] == "UNCHANGED_UNUSED"

assert reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.11.json"
)
assert "SOURCE-SILENT" in source and "one-pole-total" in source
assert "z(\\alpha_{II}\\kappa_1-z)" in report
assert "SUMMARY_OUTRUNS_ARTIFACT" in review
assert "DEFENDS_SUPERSEDED_OR_MISTYPED_OBJECT" in review
assert "PASS_WITH_MATERIAL_TARGET_AND_SCOPE_CORRECTIONS" in review
assert "Ledger v0.11" in view and "82/82" in view

print("PASS: v0.11 wires the corrected massless-plus-massive gravity target and nonlinear cyclic saddle branches without selecting P2, promoting the cyclic control, or changing residue/posture")
