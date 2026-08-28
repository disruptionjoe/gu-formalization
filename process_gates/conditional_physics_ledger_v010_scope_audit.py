#!/usr/bin/env python3
"""Fail-closed wiring audit for conditional-physics ledger v0.10."""

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


v9p = ROOT / "lab/process/conditional-physics-ledger-v0.9.json"
v9 = strict("lab/process/conditional-physics-ledger-v0.9.json")
v10 = strict("lab/process/conditional-physics-ledger-v0.10.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
registry = strict("lab/process/observed-upback-stress-normal-constraint-vacuum.json")
view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.10.md").read_text()
report = (ROOT / "explorations/conditional-build/observed-upback-stress-normal-constraint-vacuum-2026-08-05.md").read_text()
source = (ROOT / "lab/sources/observed-upback-stress-source-reinspection-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-observed-upback-stress-normal-constraint-review.md").read_text()

rows9 = {row["id"]: row for row in v9["rows"]}
rows10 = {row["id"]: row for row in v10["rows"]}
active = [row for row in rows10.values() if row.get("row_status") != "SUPERSEDED"]
changed = {row_id for row_id in rows9 if rows9[row_id] != rows10[row_id]}
migrations = [m for m in v10["migrations"] if m.get("to_version") == "0.10"]

assert hashlib.sha256(v9p.read_bytes()).hexdigest() == "0ae17658c90f52895a76cd7bbba4079f3074ed40560a97f8efb682da6c0fdc66"
assert v10["schema_version"] == "0.10"
assert v10["predecessor"].endswith("conditional-physics-ledger-v0.9.json")
assert set(rows9) == set(rows10)
assert changed == {"LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR5", "LT-GR6"}
assert {m["row_id"] for m in migrations} == changed
assert len(active) == 82 and len(rows10) == 83
assert Counter(row["axis"] for row in active) == {
    "REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26
}
assert Counter(row["verdict"] for row in active) == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6
}
assert all(row["reason_kind"] in v10["taxonomy"]["verdict_kinds"][row["verdict"]]
           for row in active)
assert v10["residue"]["continuous_real"] == 84
assert v10["residue"]["function_valued_at_least"] == 19
assert v10["residue"]["open_discrete_forks"] == 10
assert v10["residue"]["quotients_ranked"] == 2

assert rows10["LT-GR2b"]["reason_kind"] == "DERIVED_PARTIAL"
assert "ZERO_INDEFINITE_ONLY" in rows10["LT-GR2b"]["mapping_grade"]
assert rows10["LT-GR2c"]["reason_kind"] == "MISSING_CONSTRUCTION"
assert "DOUBLE_POLE_NOT_EINSTEIN_SINGLE_POLE" in rows10["LT-GR2c"]["mapping_grade"]
assert rows10["LT-GR2d"]["reason_kind"] == "MISSING_CONSTRUCTION"
assert "FULL_NONLINEAR_T_CUBIC" in rows10["LT-GR2d"]["mapping_grade"]
assert next(m for m in migrations if m["row_id"] == "LT-GR2d")["meaning_changed"] is True
assert "GENERALIZED_DOUBLE_POLE_PARTNER_REMAINS" in rows10["LT-GR5"]["mapping_grade"]
assert "RADIAL_TRANSGRESSION_EXACT" in rows10["LT-GR6"]["mapping_grade"]

assert registry["stress"]["free_object_delta"] == 0
assert registry["stress"]["literal_VU_equals_stress"] is False
assert registry["observed_constraints"]["physical_quotient_dimension"] == 2
assert registry["propagator"]["pole_order"] == 2
assert registry["propagator"]["einstein_single_pole"] is False
assert registry["vacuum"]["stationary_hessian_inertia"] == [6, 4]
assert registry["vacuum"]["full_nonlinear_T_cubic"] == "OPEN"
assert registry["residue"]["P1_P2_P3"] == "UNCHANGED_UNUSED"

assert reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.10.json"
)
assert "02:03:07" in source and "SOURCE-CORRECTS" in source
assert "double pole" in report and "full nonlinear" in report
assert "SUMMARY_OUTRUNS_ARTIFACT" in review
assert "DEFENDS_SUPERSEDED_OR_MISTYPED_OBJECT" in review
assert "free_object_delta: 0" in review and "`T4` not earned" in review
assert "Ledger v0.10" in view and "82/82" in view

print("PASS: v0.10 wires zero-parameter Hilbert-stress transgression, exact 10-to-6-to-2 observed constraints, the adverse double-pole diagnosis and the scoped quadratic-vacuum correction without residue or posture inflation")
