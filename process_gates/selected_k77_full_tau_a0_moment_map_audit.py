#!/usr/bin/env python3
"""Fail-closed process audit for conditional-physics ledger v0.102."""

from pathlib import Path
import json


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


ledger = load("lab/process/conditional-physics-ledger-v0.102.json")
registry = load("lab/process/selected-k77-full-tau-a0-moment-map.json")
contract = load("lab/process/functional-channel-operating-contract-v1.0.json")
report = read("explorations/conditional-build/selected-k77-full-tau-a0-moment-map-2026-08-08.md")
review = read("lab/process/hostile-reviews/2026-08-08-selected-k77-full-tau-a0-moment-map-review.md")

check("ledger schema", ledger["schema_version"] == "0.102")
check("ledger predecessor", ledger["predecessor"].endswith("v0.101.json"))
check("coverage", ledger["progress"]["mapped"] == 82 and ledger["progress"]["total"] == 82)
check("verdicts", ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
})
check("frontier", ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 4,
    "conditions_opened": 1, "remaining_named_conditions": 2
})
check("source return", "SOURCE-CONFIRMS_FULL_TILTED" in ledger["source_return"]
      and "SOURCE_SILENT_BOUNDARY_MOMENT_MAP" in ledger["source_return"])

required_layer0 = {
    "NONZERO_A0_DERIVATIVE_COCYCLE_Q_A0",
    "TILTED_GRAPH_TAU_A0",
    "LEFT_TILTED_CANONICAL_DISTORTION_THETA_A0",
    "RESIDUAL_RIGHT_ADJOINT_ACTION",
    "RAW_RESIDUAL_ADJOINT_MOMENT_MAP",
    "EDGE_DRESSED_CHARACTERISTIC_KERNEL",
    "GLOBAL_ALGEBRAIC_TAU_A0_DESCENT",
    "GLOBAL_FUNCTIONAL_BFV_COMPLETION_POLARIZATION_AND_CHARGE_ALGEBRA",
}
check("layer0", required_layer0 <= set(ledger["layer0_objects_compared"]))

check("residue", ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("queue", ledger["next_work_queue"][0]["rows"] == ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]
      and "global functional BFV" in ledger["next_work_queue"][0]["why"])

rows = {row["id"]: row for row in ledger["rows"] if row.get("row_status") != "SUPERSEDED"}
for row_id in ("LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"):
    check(f"{row_id} evidence", rows[row_id]["evidence"] == "selected-k77-full-tau-a0-moment-map-2026-08-08.md")
    check(f"{row_id} frontier", "FULL_NONZERO_A0_TAU_ALGEBRAIC_EDGE_DESCENT_EXACT" in rows[row_id]["frontier_grade"])

migrations = [m for m in ledger["migrations"] if m["from_version"] == "0.101" and m["to_version"] == "0.102"]
check("five migrations", [m["row_id"] for m in migrations] == ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"])
check("migration meanings", all(m["meaning_changed"] is False for m in migrations))

check("registry status", registry["status"].startswith("FULL_NONZERO_A0_TILTED"))
check("full cocycle", registry["full_tau_a0"]["graph_homomorphism"] is True
      and registry["full_tau_a0"]["zero_jet_shadow_rejected"] is True)
check("moment map", registry["moment_map"]["raw_action_charged"] is True
      and registry["moment_map"]["edge_kernel_equals_gauge_orbit"] is True
      and registry["moment_map"]["edge_kernel_dimension"] == 4)
check("horns", registry["boundary_horns"]["charged_boundary_symmetry"].startswith("LIVE_COMPARATOR")
      and registry["boundary_horns"]["physical_selection"].startswith("NOT_SELECTED"))
check("controls", registry["controls"]["main"] == "55/55 PASS"
      and registry["controls"]["independent_sage"] == "20/20 PASS")
check("data fence", registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
      and registry["constraint_fence"]["new_booked_quotients"] == 0)
check("parent sizes", registry["action_parent_fence"]["spin_native_selected_carrier"]["carrier_dimension_complex"] == 2107
      and registry["action_parent_fence"]["two_u32_32_halves"]["carrier_dimension_complex"] == 16382
      and registry["action_parent_fence"]["full_u64_64"]["carrier_dimension_complex"] == 16383)

check("report scope", "global algebraic associated-bundle** gate" in report
      and "parent from the source" in report)
check("review verdict", "FULL_TAU_A0_ALGEBRAIC_EDGE_DESCENT_SURVIVES" in review)
check("symplectic review", "Symplectic" in review and "residual orbit" in review)

current_refs = [
    "LANES.yaml", "NEXT-STEPS.md", "RESEARCH-STATUS.md", "explorations/README.md",
    "lab/process/README.md", "lab/process/agent-context-pack.md",
    "lab/process/functional-channel-operating-contract-v1.0.md",
]
for relative in current_refs:
    check(f"current pointer {relative}", "v0.102" in read(relative))
check("contract pointer", contract["standing_ledger"]["ref"].endswith("v0.102.json"))
check("contract next gate", contract["active_scientific_directives"][0]["next_gate"] == registry["next_gate"])

python_count = len(list((ROOT / "tests/channel-swings").glob("*.py")))
sage_count = len(list((ROOT / "tests/channel-swings").glob("*.sage")))
check("inventory counts", python_count == 475 and sage_count == 64)
check("inventory prose", "(475 Python + 64 Sage)" in read("tests/README.md"))

if FAILURES:
    raise SystemExit("FAIL selected K77 full tau_A0 moment-map audit: " + "; ".join(FAILURES))
print("PASS selected K77 full tau_A0 moment-map audit")
