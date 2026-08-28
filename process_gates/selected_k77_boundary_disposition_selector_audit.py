#!/usr/bin/env python3
"""Fail-closed process audit for conditional-physics ledger v0.101."""

from pathlib import Path
import json

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]
FAILURES = []


def check(label, condition):
    if not condition:
        FAILURES.append(label)


def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"), object_pairs_hook=unique)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


ledger = load("lab/process/conditional-physics-ledger-v0.101.json")
registry = load("lab/process/selected-k77-boundary-disposition-selector.json")
contract = load("lab/methods/research-evidence-contract-v1.0.json")
report = read("explorations/conditional-build/selected-k77-boundary-disposition-selector-2026-08-08.md")
review = read("lab/process/hostile-reviews/2026-08-08-selected-k77-boundary-disposition-selector-review.md")

check("ledger schema", ledger["schema_version"] == "0.101")
check("ledger predecessor", ledger["predecessor"].endswith("v0.100.json"))
check("coverage", ledger["progress"]["mapped"] == 82 and ledger["progress"]["total"] == 82)
check("verdicts", ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
})
check("frontier", ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 3,
    "conditions_opened": 1, "remaining_named_conditions": 2
})
check("source return", "SOURCE-SILENT_BOUNDARY_GAUGE_VS_PHYSICAL_SYMMETRY" in ledger["source_return"])

required_layer0 = {
    "BULK_TILTED_DOUBLE_COSET",
    "BOUNDARY_GAUGE_REDUNDANCY",
    "CHARGED_BOUNDARY_PHYSICAL_SYMMETRY",
    "FULL_BOUNDARY_GAUGE_PREDICATE",
    "GENERIC_NONZERO_ACTION_MOMENTUM_PREDICATE",
    "CONDITIONAL_MINIMAL_EDGE_HORN",
}
check("layer0", required_layer0 <= set(ledger["layer0_objects_compared"]))

check("residue", ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("queue", ledger["next_work_queue"][0]["rows"] == ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]
      and "actual K77 H/action trace" in ledger["next_work_queue"][0]["why"])

rows = {row["id"]: row for row in ledger["rows"] if row.get("row_status") != "SUPERSEDED"}
for row_id in ("LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"):
    check(f"{row_id} evidence", rows[row_id]["evidence"] == "selected-k77-boundary-disposition-selector-2026-08-08.md")
    check(f"{row_id} comparator", "CHARGED_SYMMETRY_COMPARATOR_LIVE" in rows[row_id]["frontier_grade"])

migrations = [m for m in ledger["migrations"] if m["from_version"] == "0.100" and m["to_version"] == "0.101"]
check("five migrations", [m["row_id"] for m in migrations] == ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"])
check("migration meanings", all(m["meaning_changed"] is False for m in migrations))

check("registry status", registry["status"].startswith("SOURCE_AND_LOCAL_ACTION_DO_NOT_SELECT"))
check("unique edge horn", registry["conditional_selector"]["unique_survivor"] == "MINIMAL_EDGE_COMPLETION")
check("selector conditional", registry["conditional_selector"]["source_derived"] is False
      and registry["conditional_selector"]["action_alone_derived"] is False)
check("charged comparator", registry["horns"]["CHARGED_BOUNDARY_SYMMETRY"]["status"] == "LIVE_COMPARATOR")
check("cost", registry["all_ten_cost"] == {
    "unextended_phase_dimension": 40,
    "extended_boundary_dimension": 60,
    "characteristic_kernel_dimension": 20,
    "reduced_symplectic_dimension": 40,
    "new_reduced_physical_dimensions": 0,
    "new_continuous_coefficients": 0
})
check("controls", registry["controls"]["main"] == "48/48 PASS"
      and registry["controls"]["independent_sage"] == "15/15 PASS")
check("data fence", registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
      and registry["constraint_fence"]["new_booked_quotients"] == 0)
check("parent fence", registry["action_parent_fence"] == {
    "spin_native_selected_carrier": "OPERATIVE_CONDITIONAL_PARENT",
    "weyl_block_product": "TWO_U32_32_HALVES_REMAIN_DISTINCT_RIVAL",
    "full_U64_64": "COMPARATOR_NOT_COLLAPSED"
})

check("report scope", "The first demand is not yet a source quotation or action theorem" in report)
check("review verdict", "CONDITIONAL_EDGE_SELECTOR_SURVIVES__SOURCE_AND_ACTION_SELECTION_CLAIM_REJECTED" in review)
check("symplectic review", "Symplectic geometry" in review and "charged physical symmetries" in review)

check("ledger ancestry", reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.101.json"))

if FAILURES:
    raise SystemExit("FAIL selected K77 boundary disposition selector audit: " + "; ".join(FAILURES))
print("PASS selected K77 boundary disposition selector audit")
