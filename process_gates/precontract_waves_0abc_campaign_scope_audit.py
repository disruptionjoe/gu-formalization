#!/usr/bin/env python3
"""Fail-closed reconciliation gate for pre-contract Waves 0B, 0A and 0C."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def strict(path):
    def pairs(items):
        keys = [key for key, _ in items]
        if len(keys) != len(set(keys)):
            raise ValueError(f"duplicate key in {path}")
        return dict(items)
    return json.loads((ROOT / path).read_text(), object_pairs_hook=pairs)


campaign = strict("lab/process/precontract-waves-0abc-campaign.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.1.json")
wave0b = strict("lab/process/precontract-wave-0b-trace-reversal-robustness.json")
wave0c = strict("lab/process/precontract-wave-0c-typed-identity-theorem-scope.json")
synthesis = (ROOT / "explorations/precontract-waves-0abc-synthesis-2026-08-05.md").read_text()

assert campaign["status"] == "COMPLETE"
assert campaign["execution_order"] == ["0B", "0A", "0C"]
assert campaign["contract_ratified"] is False
assert all(wave["status"] == "COMPLETE" for wave in campaign["waves"].values())
assert wave0b["channel_primacy"] == "COMPOSE_PLUS_SOURCE_BEFORE_FURTHER_BUILD_ON_THIS_GATE"
assert wave0b["exact_results"]["ambient_to_observed_scalar_ratio"] == 26
assert wave0b["exact_results"]["ambient_to_observed_traceless_ricci_ratio"] == 6
assert wave0b["exact_results"]["scalar_adapter_exists"] is False
assert wave0c["spinor_identity"]["same_typed_object"] is True
assert wave0c["spinor_identity"]["full_sa_c2_same_object"] is False
assert wave0c["shiab_relation"]["trace_reversal_adapter_on_riemann"] is True
assert wave0c["shiab_relation"]["full_domain_adapter"] == "OPEN"

assert ledger["denominator"]["source_row_count"] == 86
assert ledger["denominator"]["canonical_target_count"] == 78
assert ledger["denominator"]["alias_count"] == 8
assert ledger["denominator"]["axes"] == {
    "REPRESENTATION": 35, "LAGRANGIAN": 17, "ANOMALY_CONSISTENCY": 26
}
assert "immutable" in ledger["denominator"]["freeze_rule"]
assert "Never overwrite" in ledger["denominator"]["migration_rule"]
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 18, "NEEDS": 22, "OVER_DETERMINED": 6
}
assert ledger["residue"]["continuous_real"] == 83
assert ledger["residue"]["function_valued_at_least"] >= 19
assert ledger["residue"]["quotients_ranked"] == 0
rows = {row["id"]: row for row in ledger["rows"]}
assert rows["LT-GR1b"]["reason_kind"] == "SCOPE_ERROR"
assert rows["LT-SM3b"]["reason_kind"] == "STALE_PREMISE"
assert rows["LT-SM3b"]["mapping_grade"] == "ADJUDICATED_STALE_PREMISE"
assert [entry["row_id"] for entry in ledger["over_determined_escalations"] if entry["status"].startswith("ADJUDICATED")] == ["LT-GR1b", "LT-SM3b"]

assert campaign["channel_primacy"]["immediate"] == "COMPOSE_PLUS_SOURCE"
assert campaign["channel_primacy"]["fixed_percentages"] is False
assert "FULL_DOMAIN_SHIAB_ACTION_ADAPTER_PLUS_OBSERVED_EQUATION_RECEIVER" in campaign["next_gates"]
assert "Every Build or Compose wave names its ledger rows" in synthesis
assert "The other four remain escalated" in synthesis
assert "not ratified in this Run" in synthesis
assert set(campaign["untouched"]) >= {"P1", "P2", "P3", "canon_status", "public_posture", "observed_physics"}

print("PASS: 0B/0A/0C campaign, ledger freshness, adapter scope, channel ordering and non-promotion fences retained")
