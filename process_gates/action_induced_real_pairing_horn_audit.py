#!/usr/bin/env python3
"""Durability audit for ledger v0.153 selected real pairing and horn gate."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKS = 0


def check(label, condition):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)
    print(f"PASS {label}")


def load_unique(path):
    def pairs(items):
        keys = [key for key, _ in items]
        if len(keys) != len(set(keys)):
            raise ValueError(f"duplicate key in {path}")
        return dict(items)

    return json.loads(path.read_text(), object_pairs_hook=pairs)


ledger = load_unique(ROOT / "lab/process/conditional-physics-ledger-v0.153.json")
result = load_unique(ROOT / "lab/process/selected-k77-action-induced-real-pairing-horn.json")
report = (ROOT / "explorations/conditional-build/selected-k77-action-induced-real-pairing-horn-2026-08-10.md").read_text()
ledger_md = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.153.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-action-induced-real-pairing-horn-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-action-induced-real-pairing-horn-source-return-2026-08-10.md").read_text()
contract = load_unique(ROOT / "lab/process/functional-channel-operating-contract-v1.0.json")
contract_md = (ROOT / "lab/process/functional-channel-operating-contract-v1.0.md").read_text()
lanes = (ROOT / "LANES.yaml").read_text()
next_steps = (ROOT / "NEXT-STEPS.md").read_text()
status = (ROOT / "RESEARCH-STATUS.md").read_text()
context = (ROOT / "lab/process/agent-context-pack.md").read_text()
priorities = (ROOT / "lab/process/exploration-absorption-priorities-2026-08-10.md").read_text()
tests_readme = (ROOT / "tests/README.md").read_text()
gates_readme = (ROOT / "process_gates/README.md").read_text()
sources_readme = (ROOT / "lab/sources/README.md").read_text()

check("ledger version is v0.153", ledger["schema_version"] == "0.153")
check("predecessor is v0.152", ledger["predecessor"].endswith("v0.152.json"))
check("headline counts freeze", ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("residue freezes at 84", ledger["residue"]["continuous_real"] == 84)
check("five quotients remain", ledger["residue"]["quotients_ranked"] == 5)
check("frontier closes two", ledger["frontier_delta"]["conditions_closed"] == 2)
check("frontier opens none", ledger["frontier_delta"]["conditions_opened"] == 0)
check("one named condition remains", ledger["frontier_delta"]["remaining_named_conditions"] == 1)
check("pairing cone starts dimension two", result["pairing_cone_dimension_before_action_parent"] == 2)
check("selected scalar trace is B_Re", result["selected_scalar_trace_pairing"] == "B_Re")
check("alternative is B_Im", result["alternative_pairing"] == "B_Im")
check("alternative needs chirality insertion", result["alternative_requires_chirality_insertion"] is True)
check("realness alone does not select", result["real_valuedness_alone_selects_pairing"] is False)
check("conjugation line is B_Re", result["conjugation_invariant_line"] == "B_Re")
check("imposed parity line is B_Im", result["parity_invariant_line_if_imposed"] == "B_Im")
check("fixed orientation is not parity", result["fixed_orientation_imposes_parity_symmetry"] is False)
check("selected parent closes r", result["selected_parent_pairing_ratio_coordinates"] == 0)
check("selected parent closes horn cost", result["selected_parent_independent_horn_coordinates"] == 0)
check("one external integer remains", result["external_integer_coordinates"] == 1)
check("one independent fit constraint remains", result["independent_fit_constraints"] == 1)
check("strict surplus is zero", result["strict_surplus"] == 0)
check("BFV basicness is not double counted", result["small_gauge_basicness_counted_as_fit_constraint"] is False)
check("P3 bridge is absent", result["p3_bridge_built"] is False)
check("P3 bridge would give plus one", result["conditional_surplus_if_typed_p3_bridge"] == 1)
check("source does not select parent", result["action_parent_source_selected"] is False)
check("report contains ten specialist lenses", report.count("ACTUAL MATH,") == 10)
check("report separates realness and conjugation", "Reality by itself therefore does **not** choose" in report)
check("report separates orientation and parity", "orientation cannot silently be promoted" in report)
check("hostile review contains Layer-0 lens", "**Layer-0 semantics:**" in review)
check("hostile review contains prior-art lens", "**Prior art:**" in review)
check("hostile review contains analytic lens", "**Analytic/Krein:**" in review)
check("hostile review contains symplectic lens", "**Symplectic/BV--BFV:**" in review)
check("hostile review scopes source derivation", "GU derives the pairing" in review)
check("source confirms norm-square arena", "SOURCE-CONFIRMS" in source and "norm-squared" in source)
check("source silence is explicit", "SOURCE-SILENT" in source)
check("source fork is explicit", "SOURCE-FORK" in source)
check("contract points at v0.153", contract["standing_ledger"]["ref"].endswith("v0.153.json"))
check("contract carries pairing directive", "action_induced_real_pairing_horn_directive" in contract["standing_ledger"])
check("contract prose points at v0.153", "conditional-physics-ledger-v0.153.json" in contract_md)
check("lanes points at v0.153", "conditional-physics-ledger-v0.153.json" in lanes)
check("next steps leads with v0.153", "ACTION-INDUCED REAL-PAIRING/HORN GATE (ledger v0.153)" in next_steps)
check("research status leads with v0.153", "ledger v0.153" in status.split("predecessor to v0.153", 1)[0])
check("context pack leads with v0.153", "Current v0.153 selected real-pairing/horn fence" in context)
check("priorities lead with v0.153", "Ledger v0.153 closes" in priorities)
check("human ledger records exact zero surplus", "strict surplus is exactly `0`" in ledger_md)
check("tests inventory names probe", "selected_k77_action_induced_real_pairing_horn_probe.py" in tests_readme)
check("process inventory names audit", "action_induced_real_pairing_horn_audit.py" in gates_readme)
check("source inventory names receipt", "selected-k77-action-induced-real-pairing-horn-source-return-2026-08-10.md" in sources_readme)
check("P1 P2 P3 unchanged", result["p1_p2_p3_assignment_change"] is False)
check("no residue movement", result["residue_change"] is False)
check("no canon movement", result["canon_verdict_change"] is False)
check("no public-posture movement", result["public_posture_change"] is False)
check("next gate is typed P3 map", "RELATIVE_BOUNDARY_INDEX_TO_P3" in result["next_gate"])

migrations = [m for m in ledger["migrations"] if m["to_version"] == "0.153"]
check("six v0.153 migrations", len(migrations) == 6)
check("all migrations preserve meaning", all(m["meaning_changed"] is False for m in migrations))
rows = {row["id"]: row for row in ledger["rows"]}
check("migration frontier grades match live rows", all(rows[m["row_id"]]["frontier_grade"] == m["new"][2] for m in migrations))

print(f"PASS {CHECKS}/{CHECKS}")
