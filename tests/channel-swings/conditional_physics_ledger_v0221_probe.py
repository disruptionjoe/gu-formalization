#!/usr/bin/env python3
"""Append-only and accounting checks for conditional physics ledger v0.221."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OLD_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.220.json"
NEW_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.221.json"


def no_duplicates(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


old = json.loads(OLD_PATH.read_text(), object_pairs_hook=no_duplicates)
new = json.loads(NEW_PATH.read_text(), object_pairs_hook=no_duplicates)
checks = []


def check(name, condition, planted=False):
    checks.append((name, bool(condition), planted))


check("schema", new["schema_version"] == "0.221")
check("predecessor", new["predecessor"].endswith("v0.220.json"))
check("status", new["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_221")
check("run_owner", new["updated_by"] == "RUN-20260812-205425-gu-i2b-trace-hq-contact-correction")
check("denominator_unchanged", new["denominator"] == old["denominator"])
check("verdict_counts_unchanged", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("coverage_unchanged", (new["progress"]["mapped"], new["progress"]["total"]) == (82, 82))
for key, expected in (("continuous_real", 84), ("function_valued_at_least", 19),
                      ("open_discrete_forks", 9), ("quotients_ranked", 5)):
    check(f"accounting_{key}", new["residue"][key] == old["residue"][key] == expected)

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
expected_rows = {"RA-E1", "RA-E3", "LT-SM6"}
changed = {row_id for row_id in old_rows if old_rows[row_id] != new_rows[row_id]}
check("row_ids_preserved", set(old_rows) == set(new_rows))
check("exact_changed_rows", changed == expected_rows)
check("verdicts_preserved", all(old_rows[row]["verdict"] == new_rows[row]["verdict"] for row in expected_rows))
check("reason_kinds_preserved", all(old_rows[row]["reason_kind"] == new_rows[row]["reason_kind"] for row in expected_rows))
check("current_evidence", all(new_rows[row]["evidence"] == "selected-k77-i2b-trace-hq-normal-contact-correction-2026-08-12.md" for row in expected_rows))

new_migrations = new["migration_history"][len(old["migration_history"]):]
check("three_migrations_appended", len(new_migrations) == 3)
check("migration_rows", {entry["row_id"] for entry in new_migrations} == expected_rows)
check("migration_versions", all((entry["from_version"], entry["to_version"]) == ("0.220", "0.221") for entry in new_migrations))

observer = new["residue"]["conditional_observer_time_reduction"]
check("rank120_of_160", "RANK120_OF_160" in observer["owned_contact"])
check("rank40_cokernel", "COKERNEL_RANK40" in observer["owned_contact"])
check("scalar_pointwise_realizable", "SCALAR_DESTROY_CREATE_POINTWISE_TRACE_HQ_SOURCE_REALIZABLE" in observer["contact_identifiability"])
check("on_shell_next", "DERIVE_COUPLED_EULER_NORMAL_PROLONGATION" in observer["open"])
check("source_return", "TRACE_HQ" in new["source_return"])
check("frontier", new["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3, "conditions_opened": 1, "remaining_named_conditions": 1})

check("no_120_parameter_booking", new["residue"]["continuous_real"] == 84, planted=True)
check("no_h_homonym", "HERMITIAN_HQ_EQUALS_GENERATION_HMINUS" not in json.dumps(new), planted=True)
check("no_dynamic_selection", "SCALAR_DYNAMICALLY_SELECTED" not in json.dumps(new), planted=True)
check("no_rank128_identity", "COKERNEL_IS_RANK128_FERMION_DEFECT" not in json.dumps(new), planted=True)

failed = [name for name, passed, _ in checks if not passed]
exact = sum(not planted for _, _, planted in checks)
planted = sum(planted for _, _, planted in checks)
print(f"CHECKS={exact} exact + {planted} planted; failures={len(failed)}")
if failed:
    print("FAILED=" + ",".join(failed))
    raise SystemExit(1)
print("RESULT=PASS")
