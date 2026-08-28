#!/usr/bin/env python3
"""Durability audit for ledger v0.154 relative-boundary/P3 KO interface."""

import json
from pathlib import Path

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


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


ledger = load_unique(ROOT / "lab/process/conditional-physics-ledger-v0.154.json")
result = load_unique(ROOT / "lab/process/selected-k77-relative-boundary-p3-ko-interface.json")
report = (ROOT / "explorations/conditional-build/selected-k77-relative-boundary-p3-ko-interface-2026-08-10.md").read_text()
ledger_md = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.154.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-relative-boundary-p3-ko-interface-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-relative-boundary-p3-ko-interface-source-return-2026-08-10.md").read_text()
contract = load_unique(ROOT / "lab/methods/research-evidence-contract-v1.0.json")
contract_md = (ROOT / "lab/methods/research-evidence-contract-v1.0.md").read_text()
lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text()
next_steps = (ROOT / "NEXT-STEPS.md").read_text()
status = (ROOT / "RESEARCH-STATUS.md").read_text()
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
priorities = (ROOT / "lab/process/exploration-absorption-priorities-2026-08-10.md").read_text()
tests_readme = (ROOT / "tests/README.md").read_text()
gates_readme = (ROOT / "process_gates/README.md").read_text()
sources_readme = (ROOT / "lab/sources/README.md").read_text()

check("ledger version is v0.154", ledger["schema_version"] == "0.154")
check("predecessor is v0.153", ledger["predecessor"].endswith("v0.153.json"))
check("headline counts freeze", ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("residue freezes at 84", ledger["residue"]["continuous_real"] == 84)
check("five quotients remain", ledger["residue"]["quotients_ranked"] == 5)
check("frontier closes two", ledger["frontier_delta"]["conditions_closed"] == 2)
check("frontier opens one", ledger["frontier_delta"]["conditions_opened"] == 1)
check("two named conditions remain", ledger["frontier_delta"]["remaining_named_conditions"] == 2)

check("map starts at boundary winding", result["map_domain"] == "pi3(SL(2,C))=Z")
check("map retracts to SU2", result["compact_retract_target"] == "pi3(SU(2))=Z")
check("map lands in relative KO", result["relative_target"].startswith("KO^0(Ybar"))
check("map formula uses supplied collapse", result["map_formula"] == "n maps to nu^*([H_n]-[R4])")
check("c2 normalization exact", result["c2_formula"] == "c2(H_n)=n")
check("fundamental p1 normalization exact", result["p1_fundamental_formula"] == "p1(H_n)=-2n")
check("adjoint p1 normalization exact", result["p1_adjoint_formula"] == "p1(ad H_n)=-4n")
check("map is additive", result["map_additive"] is True)
check("map is injective", result["map_injective_on_integer_coordinate"] is True)
check("map is not parity-only", result["map_parity_only"] is False)
check("relative trivialization exists", result["relative_boundary_trivialization"] is True)

check("connection diagonal remains unbuilt", result["actual_tangent_normal_connection_diagonal_built"] is False)
check("class map does not need connection diagonal", result["connection_diagonal_required_for_integer_class_correlation"] is False)
check("source connection identity still needs diagonal", result["connection_diagonal_required_for_source_connection_identification"] is True)
check("real KO twist is K77 compatible", result["real_ko_twist_type_compatible_with_k77_real_bundle"] is True)
check("original comparator is K95", result["p3_original_comparator_carrier"].startswith("K95 quaternionic/right-H"))
check("K77 right-H port absent", result["k77_right_h_port_built"] is False)
check("two U32 halves do not supply H", result["two_u32_32_halves_supply_right_h"] is False)
check("K77 relative domain absent", result["k77_relative_closed_fredholm_domain_built"] is False)
check("relative index absent", result["relative_index_readout_built"] is False)
check("generation count absent", result["generation_count_readout_built"] is False)
check("same-object index bridge absent", result["full_same_object_index_bridge_built"] is False)

check("one external integer remains", result["external_integer_coordinates"] == 1)
check("one amplitude equation remains", result["independent_amplitude_constraints"] == 1)
check("no index count equation is booked", result["independent_index_count_constraints"] == 0)
check("strict surplus stays zero", result["strict_surplus"] == 0)
check("genuine future count equation would give plus one", result["conditional_surplus_if_genuine_index_count_readout"] == 1)

check("report contains ten specialist lenses", report.count("ACTUAL MATH,") == 10)
check("report separates input class and count", "input twist itself" in report and "physical interpretation of a realized index" in report)
check("report preserves U32 halves warning", "two `U(32,32)` Weyl halves" in report)
check("hostile review contains Layer-0", "**Layer-0 semantics:**" in review)
check("hostile review contains prior art", "**Prior art:**" in review)
check("hostile review contains analytic/index", "**Analytic/index:**" in review)
check("hostile review contains symplectic", "**Symplectic/BV--BFV:**" in review)
check("hostile review contains dissent", "## Dissent" in review)
check("source confirms arena", "SOURCE-CONFIRMS" in source and "Chern--Simons-like" in source)
check("source silence is explicit", "SOURCE-SILENT" in source)

check("current append-only ledger descends to v0.154", reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.154.json"
))
check("contract carries P3 KO directive", "p3_relative_ko_interface_directive" in contract["standing_ledger"])
check("human ledger records zero surplus", "Strict surplus remains" in ledger_md and "`1-1=0`" in ledger_md)
check("tests inventory names probe", "selected_k77_relative_boundary_p3_ko_interface_probe.py" in tests_readme)
check("process inventory names audit", "relative_boundary_p3_ko_interface_audit.py" in gates_readme)
check("source inventory names receipt", "selected-k77-relative-boundary-p3-ko-interface-source-return-2026-08-10.md" in sources_readme)

check("P1 P2 P3 unchanged", result["p1_p2_p3_assignment_change"] is False)
check("no residue movement", result["residue_change"] is False)
check("no canon movement", result["canon_verdict_change"] is False)
check("no public-posture movement", result["public_posture_change"] is False)
check("next gate returns to physical K77 carrier", result["next_gate"].startswith("RESUME_NONZERO_FERMION_SOURCE_OPERATOR_STATIONARITY"))

migrations = [m for m in ledger["migrations"] if m["to_version"] == "0.154"]
check("six v0.154 migrations", len(migrations) == 6)
check("all migrations preserve meaning", all(m["meaning_changed"] is False for m in migrations))
rows = {row["id"]: row for row in ledger["rows"]}
check(
    "migration grades match live rows",
    all((rows[m["row_id"]].get("frontier_grade") or rows[m["row_id"]]["mapping_grade"]) == m["new"][2] for m in migrations),
)

print(f"PASS {CHECKS}/{CHECKS}")
