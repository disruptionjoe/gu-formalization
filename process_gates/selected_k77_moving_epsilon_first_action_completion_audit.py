#!/usr/bin/env python3
"""Fail-closed audit for the selected K77 moving-epsilon completion wave."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]


def strict(path):
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=hook)


registry = strict(ROOT / "lab/process/selected-k77-moving-epsilon-first-action-completion.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.123.json")
contract = strict(ROOT / "lab/process/functional-channel-operating-contract-v1.0.json")
stationarity = strict(ROOT / "lab/process/selected-k77-source-tangent-branch-stationarity.json")
report = (ROOT / "explorations/conditional-build/selected-k77-moving-epsilon-first-action-completion-2026-08-09.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-09-selected-k77-moving-epsilon-first-action-completion-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-moving-epsilon-first-action-source-reinspection-2026-08-09.md").read_text()

checks = []


def require(condition, label):
    assert condition, label
    checks.append(label)


require(ledger["schema_version"] == "0.123", "ledger version")
require(ledger["predecessor"].endswith("v0.122.json"), "append-only predecessor")
require(registry["status"].startswith("SELECTED_SPIN_321_EPSILON_CLOSURE_KILLED"), "scoped status")
result = registry["exact_result"]
require(result["fixed_principal_ranks"] == {"full": 91, "horizontal": 6, "offslice": 88}, "fixed ranks")
require(result["lower_cartan_ranks"] == {"full": 0, "horizontal": 0, "offslice": 0}, "Cartan zero")
require(result["moving_shiab_ranks"] == {"full": 0, "horizontal": 0, "offslice": 0}, "moving Shiab zero")
require(result["total_ranks"] == {"full": 91, "horizontal": 6, "offslice": 88}, "total ranks")
require(result["coefficientwise_total_equals_fixed"] is True, "coefficientwise equality")
require(result["nonzero_counts"]["timelike"] == {"full": 403, "offslice": 385}, "timelike support")
require(result["nonzero_counts"]["spacelike"] == {"full": 403, "offslice": 385}, "spacelike support")
require(result["nonzero_counts"]["null"] == {"full": 806, "offslice": 770}, "null support")
require(registry["validation"]["primary_result"] == "399/399_PASS", "primary receipt")
require("695604" in registry["validation"]["independent_result"], "independent exact receipt")
require(registry["parent_fence"] == {
    "selected_spin77": "DECIDED_AS_STATED",
    "two_U32_32_halves": "NOT_PORTED",
    "full_U64_64": "NOT_PORTED",
}, "parent fence")
require(registry["accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED", "datum fence")
require(registry["accounting"]["new_quotients"] == 0, "no quotient promoted")
require(registry["claim_status_change"] == "none", "claim unchanged")
require(registry["canon_verdict_change"] == "none", "canon unchanged")
require(registry["public_posture_change"] == "none", "posture unchanged")
require(stationarity["exact_result"]["branch_pullback"]["observation"] == "ZERO_COVECTOR_TRANSPORTS_TO_ZERO", "stationary receiver transport")
process_gate = registry["mandatory_successor_process_gate"]
require(process_gate["priority"] == "BEFORE_NEXT_HEAVY_HESSIAN_EXTENSION", "process priority")
require(set(process_gate["requirements"]) == {
    "SOURCE_REVISION_HASH", "CONSTRUCTION_HASH", "STALE_CACHE_REJECTION",
    "BOUNDED_EQUIVALENCE_REPLAY", "NO_RECURSIVE_FULL_PREDECESSOR_REBUILD",
}, "process requirements")
require(contract["standing_ledger"]["ref"].endswith("v0.123.json"), "contract ledger wiring")
rank_one = ledger["next_work_queue"][0]
require(rank_one["rank"] == 1 and "durable versioned API" in rank_one["why"], "rank-one process dispatch")
require("SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source, "source return")
require("321-field selected-Spin truncation is therefore not Hessian-closed" in report, "report disposition")
require("does **not** automatically promote all 1,571" in report, "no 1571 promotion")
require("SURVIVES_WITH_PARENT_AND_QUOTIENT_FENCES" in review, "hostile verdict")
require("Symplectic" in review and "Analytic/Krein" in review, "mandatory reviews")
require(ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5,
}, "headline unchanged")
require(ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 3,
    "conditions_opened": 0,
    "remaining_named_conditions": 2,
}, "frontier delta")
require({row["id"] for row in ledger["rows"]
         if row.get("evidence") == "selected-k77-moving-epsilon-first-action-completion-2026-08-09.md"} == {
    "LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6",
}, "six row migrations")
require([entry["row_id"] for entry in ledger["migrations"][-6:]] == [
    "LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6",
], "migration order")

print(f"PASS selected K77 moving-epsilon first-action completion audit: {len(checks)}/{len(checks)}")
