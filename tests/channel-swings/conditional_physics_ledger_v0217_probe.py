#!/usr/bin/env python3
"""Append-only and accounting checks for conditional physics ledger v0.217."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OLD_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.216.json"
NEW_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.217.json"


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


check("schema", new["schema_version"] == "0.217")
check("predecessor", new["predecessor"].endswith("v0.216.json"))
check("status", new["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_217")
check("run_owner", new["updated_by"] == "historical-investigation")
check("denominator_unchanged", new["denominator"] == old["denominator"])
check("verdict_counts_unchanged", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("coverage_unchanged", (new["progress"]["mapped"], new["progress"]["total"]) == (82, 82))
check("rows_exactly_unchanged", new["rows"] == old["rows"])
check("migration_history_unchanged", new["migration_history"] == old["migration_history"])
check("continuous_residue_unchanged", new["residue"]["continuous_real"] == old["residue"]["continuous_real"] == 84)
check("function_residue_unchanged", new["residue"]["function_valued_at_least"] == old["residue"]["function_valued_at_least"] == 19)
check("forks_unchanged", new["residue"]["open_discrete_forks"] == old["residue"]["open_discrete_forks"] == 9)
check("quotients_unchanged", new["residue"]["quotients_ranked"] == old["residue"]["quotients_ranked"] == 5)

observer = new["residue"]["conditional_observer_time_reduction"]
check("observer_cost_still_unbooked", observer["booking"].startswith("UNBOOKED"))
check("diagonal_naturality_survives", "DIAGONAL_SPIN_NATURALITY_EXACT" in observer["observer_hu_result"])
check("coarse_nonselection_survives", observer["coarse_observation_result"].endswith("NO_FIXED_UNIT_TIME"))
check("inverse_adjoint_control_corrected", observer["vertical_basicness_result"] == "REFUTED_WITH_CORRECT_INVERSE_ADJOINT__FIXED_FIELD_BLOCKS_MINUS_328_OVER_9_PLUS_8_PLUS_8_PLUS_8")
check("rb4_prior_art_visible", "RB4_MOVING_U_SO3_BUILT" in observer["prior_art"])
check("rb5_prior_art_visible", "RB5_COARSE_FLAG_REFUTED" in observer["prior_art"])
check("current_action_gate", "CURRENT_SC_ACT_04_CONSTRAINED_U_EULER_WARD" in observer["open"])
check("source_return_present", "SOURCE_SILENT_INVERSE_ADJOINT_BLOCKS_AND_CURRENT_U_EULER" in new["source_return"])
check("frontier_delta", new["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 2, "conditions_opened": 0, "remaining_named_conditions": 2})
check("rank_one_retires_duplicate", "RB4 already built" in new["next_work_queue"][0]["why"])
check("rank_one_names_section_chain_rule", "section chain rule" in new["next_work_queue"][0]["why"])
check("all_wave_dispositions_are_corrections", all("ROW_MEANING_UNCHANGED" in entry["disposition"] for entry in new["wave_row_dispositions"]))

check("old_wrong_blocks_absent", "FIXED_FIELD_BOOST_CHANGES_8_TO_328_OVER_9" not in observer["vertical_basicness_result"], planted=True)
check("duplicate_so3_successor_absent", "CONSTRUCT_COMPLETE_EPSILON_IG_SO3_FLAG" not in observer["open"], planted=True)
check("no_silent_row_migration", new["rows"] == old["rows"], planted=True)

failed = [name for name, passed, _ in checks if not passed]
exact = sum(1 for _, _, planted in checks if not planted)
planted = sum(1 for _, _, is_planted in checks if is_planted)
print(f"CHECKS={exact} exact + {planted} planted; failures={len(failed)}")
if failed:
    print("FAILED=" + ",".join(failed))
    raise SystemExit(1)
print("RESULT=PASS")
