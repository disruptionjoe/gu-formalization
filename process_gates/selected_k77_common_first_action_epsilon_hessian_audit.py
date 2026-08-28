#!/usr/bin/env python3
"""Fail-closed process audit for conditional-physics ledger v0.106."""

from pathlib import Path
import json

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]
FAILURES = []


def check(label, condition):
    if not condition:
        FAILURES.append(label)


def unique(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def load(relative):
    return json.loads(
        (ROOT / relative).read_text(encoding="utf-8"),
        object_pairs_hook=unique,
    )


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


ledger = load("lab/process/conditional-physics-ledger-v0.106.json")
registry = load("lab/process/selected-k77-common-first-action-epsilon-hessian.json")
contract = load("lab/methods/research-evidence-contract-v1.0.json")
report = read("explorations/conditional-build/selected-k77-common-first-action-epsilon-hessian-2026-08-08.md")
review = read("lab/process/hostile-reviews/2026-08-08-selected-k77-common-first-action-epsilon-hessian-review.md")

check("ledger schema", ledger["schema_version"] == "0.106")
check("ledger predecessor", ledger["predecessor"].endswith("v0.105.json"))
check("coverage", ledger["progress"]["mapped"] == 82 and ledger["progress"]["total"] == 82)
check("verdicts", ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
})
check("frontier", ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 5,
    "conditions_opened": 2, "remaining_named_conditions": 5,
})
check("source return", "SOURCE_CONFIRMS_NONLINEAR_FIRST_ACTION" in ledger["source_return"]
      and "SOURCE_SILENT" in ledger["source_return"])

required_layer0 = {
    "OLD_RAW_RESIDUAL_ZERO_BACKGROUND",
    "COMPLETE_LOW_GRADE_B_AND_T_FIRST_ACTION_EULER_COVECTORS",
    "NONTRIVIAL_COMMON_CONNECTION_CRITICAL_BRANCH",
    "DIRECT_TEN_COMPONENT_METRIC_EULER_COVECTOR",
    "LOWER_ORDER_MOVING_SHIAB_EPSILON_RESPONSE",
    "RANK91_EPSILON_BY_GRADE1_MIXED_FIRST_ACTION_HESSIAN",
    "RESTRICTED_FIELD125_VERSUS_MINIMAL_FIELD321_VERSUS_SOURCE_FIELD1571",
}
check("layer0", required_layer0 <= set(ledger["layer0_objects_compared"]))
check("residue", ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("quotients unbooked", "unbooked" in ledger["residue"]["meter"]
      and "220/220/32" in ledger["residue"]["meter"])
check("queue", ledger["next_work_queue"][0]["rows"]
      == ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]
      and "direct ten-component metric Euler" in ledger["next_work_queue"][0]["why"])

rows = {row["id"]: row for row in ledger["rows"]
        if row.get("row_status") != "SUPERSEDED"}
for row_id in ("LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"):
    check(f"{row_id} evidence", rows[row_id]["evidence"]
          == "selected-k77-common-first-action-epsilon-hessian-2026-08-08.md")
    check(f"{row_id} frontier", "COMMON_CONNECTION" in rows[row_id]["frontier_grade"]
          and "DIRECT_METRIC_EULER_OPEN" in rows[row_id]["frontier_grade"])

migrations = [m for m in ledger["migrations"]
              if m["from_version"] == "0.105" and m["to_version"] == "0.106"]
check("five migrations", [m["row_id"] for m in migrations]
      == ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"])
check("migration meanings", all(m["meaning_changed"] is False for m in migrations))

check("registry status", registry["status"].startswith("COMMON_CONNECTION_BRANCH_EXACT"))
branch = registry["common_connection_branch"]
check("old fixture", registry["old_fixture"]["E_B_support"] == 14
      and registry["old_fixture"]["E_B_nonzero_value"] == "1/312"
      and registry["old_fixture"]["critical_on_grade2_slice_only"] is True)
check("branch", branch["B_star"] == "(1/156)Phi1"
      and branch["T_star"] == "-(1/78)Phi1"
      and branch["E_B_zero_all_1470"] is True
      and branch["E_T_zero_all_1470"] is True
      and branch["raw_upsilon_zero"] is True)
check("metric fence", branch["direct_metric_euler"] == "OPEN")
cross = registry["moving_epsilon"]
check("epsilon cross", cross["moving_shiab_rank"] == 91
      and cross["mixed_cross_rank"] == 91
      and cross["mixed_cross_nonzero_entries"] == 182
      and cross["receiver_grade"] == 1)
check("tangent gate", registry["field_tangent_gate"] == {
    "current_restricted_dimension": 125,
    "minimal_known_completion_dimension": 321,
    "full_low_grade_source_candidate_dimension": 1571,
    "selection": "OPEN_ACTION_PARENT_AND_TRUNCATION_GATE",
})
check("parents", registry["action_parents"]["collapsed"] is False
      and set(registry["action_parents"]) >= {
          "selected_spin_native", "two_U32_32_halves", "full_U64_64"
      })
check("controls", registry["controls"]["primary"] == "61/61 PASS"
      and registry["controls"]["independent_sage"] == "29/29 PASS"
      and registry["controls"]["P1_P2_P3_unused"] is True)

check("report scope", "common connection-critical branch" in report
      and "not yet a full" in report and "direct metric Euler" in report)
check("review verdict", "CANDIDATE_SURVIVES_SCOPED__FULL_COMMON_HESSIAN_BLOCKED" in review)
for lens in ("layer0_semantics", "prior_art", "variational_bicomplex", "symplectic", "analytic", "source"):
    check(f"review lens {lens}", lens in review)

check("ledger ancestry", reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.106.json"))

if FAILURES:
    raise SystemExit("FAIL selected K77 common first-action audit: " + "; ".join(FAILURES))
print("PASS selected K77 common first-action epsilon Hessian audit")
