#!/usr/bin/env python3
"""Fail-closed audit for the K77 trace-H_q connection/internal-chain gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.195.json"
REGISTRY = ROOT / "lab/process/selected-k77-trace-hq-connection-internal-chain-gate.json"
REPORT = ROOT / "explorations/conditional-build/selected-k77-trace-hq-connection-internal-chain-gate-2026-08-12.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-trace-hq-connection-internal-chain-review.md"
SOURCE = ROOT / "lab/sources/selected-k77-trace-hq-connection-internal-chain-source-return-2026-08-12.md"


def fail(message: str) -> None:
    raise SystemExit("FAIL: " + message)


ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
report = REPORT.read_text(encoding="utf-8")
review = REVIEW.read_text(encoding="utf-8")
source = SOURCE.read_text(encoding="utf-8")

if ledger["schema_version"] != "0.195" or ledger["predecessor"] != "lab/process/conditional-physics-ledger-v0.194.json":
    fail("ledger version/predecessor mismatch")
if ledger["progress"]["mapped"] != 82 or ledger["progress"]["verdict_counts"] != {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
}:
    fail("headline accounting changed")
if ledger["residue"]["continuous_real"] != 84 or ledger["residue"]["function_valued_at_least"] != 19:
    fail("booked residue changed")
if ledger["residue"]["conditional_q_reduction"]["split_spin_compatibility"] != \
        "EXACT_SPIN1_3_X_SPIN6_3__DEFECT_RANK_9_AND_RECONSTRUCTIBLE":
    fail("split-spin H_q compatibility missing")

result = registry["result"]
expected = {
    "checks": 56,
    "failures": 0,
    "split_spin_dimension": 51,
    "compatible_base_dimension": 6,
    "compatible_normal_dimension": 36,
    "compatible_split_dimension": 42,
    "Hq_defect_rank": 9,
    "broken_normal_compact_dimension": 3,
    "broken_normal_noncompact_dimension": 6,
    "normal_q_maximal_compact_dimension": 18,
    "pati_salam_dimension": 21,
    "vPSB_stabilizer_dimension": 12,
    "trace_q_compact_stabilizer_dimension": 18,
    "joint_vPSB_trace_q_stabilizer_dimension": 9,
}
for key, value in expected.items():
    if result.get(key) != value:
        fail(f"registry {key} mismatch")
if not result["abstract_sm_algebra_contained"] or result["naive_fixed_q_sm_fermion_branching"]:
    fail("algebra-containment/representation fence collapsed")
if result["rank_nine_defect_is_higgs_doublet"]:
    fail("rank-nine connection defect relabeled as Higgs")
if result["operative_full_varpi_connection"] != "OPEN" or result["source_u3_2_intersection"] != "OPEN":
    fail("operative parent or source intersection overpromoted")

for token in ("rank(D H_q) = 9", "dim (Stab(v_PSB) ∩ Stab(q)) = 9", "SC-GRP-03", "nine-component connection defect is not a Higgs doublet"):
    if token not in report:
        fail(f"report missing {token}")
if "SURVIVES_AFTER_SCOPE_REPAIR" not in review or "needs-recheck" not in review:
    fail("hostile review missing scoped disposition")
for claim_id in ("SC-GRP-01", "SC-GRP-02", "SC-GRP-03", "SC-SIG-52", "SC-FER-03", "SC-GEO-58", "SC-META-57"):
    if claim_id not in source:
        fail(f"source return missing {claim_id}")

rows = {row["id"]: row for row in ledger["rows"]}
for row_id in registry["ledger_rows"]:
    if row_id not in rows or rows[row_id]["evidence"] != REPORT.name:
        fail(f"row {row_id} did not migrate to this evidence")
if len(ledger["migrations"]) != 135 or ledger["migration_history"] != ledger["migrations"]:
    fail("append-only migration history mismatch")

print("PASS: v0.195 constructs exact split-spin trace-H_q compatibility, rejects the frozen-q direct Pati-Salam/SM shortcut, and preserves the moving/full-unitary plus distinct-varpi route at honest grade.")
