#!/usr/bin/env python3
"""Append-only and accounting checks for conditional physics ledger v0.216."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OLD_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.215.json"
NEW_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.216.json"


def no_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


old = json.loads(OLD_PATH.read_text(), object_pairs_hook=no_duplicates)
new = json.loads(NEW_PATH.read_text(), object_pairs_hook=no_duplicates)
checks: list[tuple[str, bool, bool]] = []


def check(name: str, condition: bool, planted: bool = False) -> None:
    checks.append((name, bool(condition), planted))


check("schema", new["schema_version"] == "0.216")
check("predecessor", new["predecessor"].endswith("v0.215.json"))
check("status", new["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_216")
check("run_owner", new["updated_by"] == "RUN-20260812-174351-gu-i2b-observer-associated-basicness")
check("denominator_unchanged", new["denominator"] == old["denominator"])
check("verdict_counts_unchanged", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("coverage_unchanged", (new["progress"]["mapped"], new["progress"]["total"]) == (82, 82))
check("continuous_residue_unchanged", new["residue"]["continuous_real"] == old["residue"]["continuous_real"] == 84)
check("function_residue_unchanged", new["residue"]["function_valued_at_least"] == old["residue"]["function_valued_at_least"] == 19)
check("forks_unchanged", new["residue"]["open_discrete_forks"] == old["residue"]["open_discrete_forks"] == 9)
check("quotients_unchanged", new["residue"]["quotients_ranked"] == old["residue"]["quotients_ranked"] == 5)
check("observer_cost_is_unbooked", new["residue"]["conditional_observer_time_reduction"]["booking"].startswith("UNBOOKED"))
check("trace_rank_zero_booked_as_result", new["residue"]["conditional_observer_time_reduction"]["geometry_trace_result"].endswith("RANK_0"))
check("observer_rank_four_booked_as_conditional", "RANK_4" in new["residue"]["conditional_observer_time_reduction"]["observer_hu_result"])
check("diagonal_naturality_exact", "DIAGONAL_SPIN_NATURALITY_EXACT" in new["residue"]["conditional_observer_time_reduction"]["observer_hu_result"])
check("coarse_observation_nonselection", new["residue"]["conditional_observer_time_reduction"]["coarse_observation_result"].endswith("NO_FIXED_UNIT_TIME"))
check("vertical_basicness_refuted", new["residue"]["conditional_observer_time_reduction"]["vertical_basicness_result"].startswith("REFUTED"))
check("source_return_present", "SOURCE_SILENT_UNIT_TIME_SELECTION" in new["source_return"])
check("layer0_naturality_vs_basicness", any("naturality" in value and "basicness" in value for value in new["layer0_objects_compared"]))
check("frontier_delta", new["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3, "conditions_opened": 1, "remaining_named_conditions": 3})

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
check("row_ids_immutable", old_rows.keys() == new_rows.keys())
changed_rows = {row_id for row_id in old_rows if old_rows[row_id] != new_rows[row_id]}
check("only_three_rows_migrated", changed_rows == {"RA-E1", "RA-E3", "LT-SM6"})
for row_id in sorted(changed_rows):
    check(f"{row_id}_verdict_unchanged", new_rows[row_id]["verdict"] == old_rows[row_id]["verdict"])
    check(f"{row_id}_reason_unchanged", new_rows[row_id]["reason_kind"] == old_rows[row_id]["reason_kind"])
    check(f"{row_id}_new_evidence", new_rows[row_id]["evidence"] == "selected-k77-i2b-observer-associated-basicness-2026-08-12.md")
    check(f"{row_id}_mentions_observer_hu", "OBSERVER_HU" in new_rows[row_id]["mapping_grade"])
    check(f"{row_id}_mentions_coarse_failure", "COARSE_OBSERVATION" in new_rows[row_id]["mapping_grade"])

new_migrations = [entry for entry in new["migration_history"] if entry.get("to_version") == "0.216"]
check("three_append_only_migrations", {entry["row_id"] for entry in new_migrations} == changed_rows)
check("all_migrations_scoped", all(entry.get("scope") and entry.get("evidence") for entry in new_migrations))
check("old_file_not_current", old["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_215", planted=True)
check("new_meter_not_old_version", "v0.215" not in new["progress"]["meter"], planted=True)
check("observer_not_silently_booked", new["residue"]["function_valued_at_least"] == 19, planted=True)

failed = [name for name, passed, _ in checks if not passed]
exact = sum(1 for _, _, planted in checks if not planted)
planted = sum(1 for _, _, is_planted in checks if is_planted)
print(f"CHECKS={exact} exact + {planted} planted; failures={len(failed)}")
if failed:
    print("FAILED=" + ",".join(failed))
    raise SystemExit(1)
print("RESULT=PASS")
