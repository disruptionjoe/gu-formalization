#!/usr/bin/env python3
"""Append-only and accounting checks for conditional physics ledger v0.218."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OLD_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.217.json"
NEW_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.218.json"


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


check("schema", new["schema_version"] == "0.218")
check("predecessor", new["predecessor"].endswith("v0.217.json"))
check("status", new["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_218")
check("run_owner", new["updated_by"] == "historical-investigation")
check("denominator_unchanged", new["denominator"] == old["denominator"])
check("verdict_counts_unchanged", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("coverage_unchanged", (new["progress"]["mapped"], new["progress"]["total"]) == (82, 82))
check("continuous_residue_unchanged", new["residue"]["continuous_real"] == old["residue"]["continuous_real"] == 84)
check("function_residue_unchanged", new["residue"]["function_valued_at_least"] == old["residue"]["function_valued_at_least"] == 19)
check("forks_unchanged", new["residue"]["open_discrete_forks"] == old["residue"]["open_discrete_forks"] == 9)
check("quotients_unchanged", new["residue"]["quotients_ranked"] == old["residue"]["quotients_ranked"] == 5)

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
changed = {row_id for row_id in old_rows if old_rows[row_id] != new_rows[row_id]}
expected = {"RA-E1", "RA-E3", "LT-SM6"}
check("exact_changed_rows", changed == expected)
check("row_ids_preserved", set(old_rows) == set(new_rows))
check("changed_verdicts_preserved", all(new_rows[row]["verdict"] == old_rows[row]["verdict"] for row in expected))
check("changed_reasons_preserved", all(new_rows[row]["reason_kind"] == old_rows[row]["reason_kind"] for row in expected))
check("current_evidence", all(new_rows[row]["evidence"] == "selected-k77-i2b-constrained-observer-euler-ward-2026-08-12.md" for row in expected))

new_migrations = new["migration_history"][len(old["migration_history"]):]
check("three_append_only_migrations", len(new_migrations) == 3)
check("migration_rows", {entry["row_id"] for entry in new_migrations} == expected)
check("migration_versions", all((entry["from_version"], entry["to_version"]) == ("0.217", "0.218") for entry in new_migrations))
check("migration_meaning_visible", all(entry["meaning_changed"] for entry in new_migrations))

observer = new["residue"]["conditional_observer_time_reduction"]
check("observer_cost_scoped", observer["booking"].startswith("UNBOOKED__ZERO_CONTINUOUS_COST_ONLY_ON_A_POSITIVE"))
check("observer_tensor", observer["observer_euler_tensor"] == "C00_DIAG_MINUS8_I4_PLUS8_I12__C11_C22_C33_MINUS8_I16__MIXED_ZERO")
check("two_strata", "A_POSITIVE_SIMPLE_TIMELIKE_LINE" in observer["selection_strata"] and "A_ZERO_OBSERVER_FLAT" in observer["selection_strata"])
check("ward_exact", "EXACT_THREE_BOOSTS_X_EIGHT_LIVE_MASKS" in observer["comoving_ward"])
check("arrow_open", observer["time_arrow"] == "UNSELECTED__ACTION_EVEN_UNDER_U_TO_MINUS_U")
check("coupled_contact_next", "FULL_SC_ACT_04_MOVING_METRIC_HODGE_SHIAB_PROJECTOR_SECTION_CONTACT" in observer["open"])
check("source_return", new["source_return"].endswith("REPO_DERIVES_SCOPED_PRINCIPAL_LINE_EQUATION"))
check("frontier_delta", new["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3, "conditions_opened": 1, "remaining_named_conditions": 2})
check("rank_one_is_coupled", "full current SC-ACT-04" in new["next_work_queue"][0]["why"])

check("no_global_selector_inflation", "GLOBAL_COMMON_LINE_EXACT" not in json.dumps(new), planted=True)
check("no_arrow_inflation", "ARROW_SELECTED" not in json.dumps(new), planted=True)
check("no_residue_movement", new["residue"]["continuous_real"] == 84, planted=True)
check("a_zero_not_erased", "A_ZERO_OBSERVER_FLAT" in observer["selection_strata"], planted=True)

failed = [name for name, passed, _ in checks if not passed]
exact = sum(1 for _, _, planted in checks if not planted)
planted = sum(1 for _, _, is_planted in checks if is_planted)
print(f"CHECKS={exact} exact + {planted} planted; failures={len(failed)}")
if failed:
    print("FAILED=" + ",".join(failed))
    raise SystemExit(1)
print("RESULT=PASS")
