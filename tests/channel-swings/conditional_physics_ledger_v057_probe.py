#!/usr/bin/env python3
"""Ledger v0.57 integrity and K77 signature-correction gate."""

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.57.json").read_text())
registry = json.loads((ROOT / "lab/process/selected-k77-cartan-spencer-signature-correction.json").read_text())

assert ledger["schema_version"] == "0.57"
assert ledger["predecessor"].endswith("conditional-physics-ledger-v0.56.json")
assert len(ledger["rows"]) == 84
active = [row for row in ledger["rows"] if row["id"] not in {"LT-GR2", "AC-G1"}]
assert len(active) == ledger["denominator"]["canonical_target_count"] == 82
assert Counter(row["verdict"] for row in active) == Counter({
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
})
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["function_valued_at_least"] == 19
assert ledger["residue"]["open_discrete_forks"] == 9
assert ledger["residue"]["quotients_ranked"] == 4
assert registry["signature_correction"]["old_executed_inertia"] == [9, 5]
assert registry["signature_correction"]["settled_k77_inertia"] == [7, 7]
assert registry["exact_result"]["transverse_total_support"] == 117
assert registry["exact_result"]["k77_koszul_supports"] == [57, 34, 34, 34]
assert registry["exact_result"]["k77_source_lift_family_rank"] == 4
assert registry["exact_result"]["pointwise_coefficient_freedom"] == 0
assert ledger["next_work_queue"][0]["rows"] == ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]
assert "corrected K77" in ledger["next_work_queue"][0]["why"]
assert all(item["change"] == "MIGRATED_MAPPING_GRADE_AND_EVIDENCE_ONLY" for item in ledger["wave_row_dispositions"])
rows_by_id = {row["id"]: row for row in ledger["rows"]}
target_rows = ("LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6")
assert all(row_id in rows_by_id for row_id in target_rows)
assert all("selected-k77-cartan-spencer-signature-correction" in rows_by_id[row_id]["evidence"]
           for row_id in target_rows)
assert all(value == "UNUSED" for value in registry["external_datum"].values())
print("PASS 21/21: v0.57 preserves the headline meter and corrects five rows to the exact K77 coefficient chain")
