#!/usr/bin/env python3
"""Fail-closed audit for the K77 trace-q ownership / two-half gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.194.json"
REGISTRY = ROOT / "lab/process/selected-k77-tautological-trace-q-two-half-ownership-gate.json"
REPORT = ROOT / "explorations/conditional-build/selected-k77-tautological-trace-q-two-half-ownership-gate-2026-08-12.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-tautological-trace-q-two-half-ownership-review.md"
SOURCE = ROOT / "lab/sources/selected-k77-tautological-trace-q-two-half-ownership-source-return-2026-08-12.md"


def fail(message: str) -> None:
    raise SystemExit("FAIL: " + message)


ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
report = REPORT.read_text(encoding="utf-8")
review = REVIEW.read_text(encoding="utf-8")
source = SOURCE.read_text(encoding="utf-8")

if ledger["schema_version"] != "0.194" or ledger["predecessor"] != "lab/process/conditional-physics-ledger-v0.193.json":
    fail("ledger version/predecessor mismatch")
if ledger["progress"]["mapped"] != 82 or ledger["progress"]["verdict_counts"] != {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
}:
    fail("headline accounting changed")
if ledger["residue"]["continuous_real"] != 84 or ledger["residue"]["function_valued_at_least"] != 19:
    fail("booked residue changed")
q = ledger["residue"]["conditional_q_reduction"]
if q["fixed_q_orbit_dimension_before_gauge"] != 0 or not q["booking"].startswith("ZERO_COST"):
    fail("trace-q zero-cost ownership not recorded")
if q["P1_role"] != "NOT_USED__TAUTOLOGICAL_RADIAL_SIGN_IS_CANONICAL":
    fail("P1 was consumed or mistyped")

result = registry["result"]
expected = {
    "checks": 50,
    "failures": 0,
    "trace_g_dewitt_norm": -4,
    "trace_q_dewitt_norm": -1,
    "full_fixed_trace_q_stabilizer_dimension": 78,
    "base_stabilizer_dimension": 6,
    "normal_stabilizer_dimension": 36,
    "split_fixed_trace_q_stabilizer_dimension": 42,
    "q_new_datum_cost": 0,
    "P1_used": False,
}
for key, value in expected.items():
    if result.get(key) != value:
        fail(f"registry {key} mismatch")
if result["full_Hq_signature"] != [64, 64] or result["weyl_plus_Hq_signature"] != [32, 32] or result["weyl_minus_Hq_signature"] != [32, 32]:
    fail("Hermitian inertia mismatch")
if result["J4_Hq_relation"] != "ANTI_ISOMETRY" or result["J10_Hq_relation"] != "ANTI_ISOMETRY":
    fail("native complex relation was promoted or mistyped")
if result["operative_action_parent"] != "OPEN" or result["physical_block_identification"] != "OPEN":
    fail("action parent or physical block was overpromoted")

for token in ("q_g = g/2", "split stabilizer is `42`, not `48`", "`D_varpi H_q=0`", "P1 is not needed"):
    if token not in report:
        fail(f"report missing {token}")
if "SURVIVES_AFTER_MATERIAL_REPAIR" not in review or "needs-recheck" not in review:
    fail("hostile review missing scoped disposition")
if "SOURCE-SILENT" not in source or "D_varpi H_q=0" not in source:
    fail("source silence/action fence missing")

rows = {row["id"]: row for row in ledger["rows"]}
for row_id in registry["ledger_rows"]:
    if row_id not in rows or rows[row_id]["evidence"] != REPORT.name:
        fail(f"row {row_id} did not migrate to this evidence")
if len(ledger["migrations"]) != 129 or ledger["migration_history"] != ledger["migrations"]:
    fail("append-only migration history mismatch")

print("PASS: v0.194 trace-q ownership is exact, zero-cost and correctly scoped; normal-q stabilizer/action/Higgs burdens remain open.")
