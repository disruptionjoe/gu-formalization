#!/usr/bin/env python3
"""Fail-closed process audit for conditional-physics ledger v0.103."""

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


ledger = load("lab/process/conditional-physics-ledger-v0.103.json")
registry = load("lab/process/selected-k77-sobolev-edge-current-algebra.json")
contract = load("lab/methods/research-evidence-contract-v1.0.json")
report = read("explorations/conditional-build/selected-k77-sobolev-edge-current-algebra-2026-08-08.md")
review = read("lab/process/hostile-reviews/2026-08-08-selected-k77-sobolev-edge-current-algebra-review.md")

check("ledger schema", ledger["schema_version"] == "0.103")
check("ledger predecessor", ledger["predecessor"].endswith("v0.102.json"))
check("coverage", ledger["progress"]["mapped"] == 82 and ledger["progress"]["total"] == 82)
check("verdicts", ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
})
check("frontier", ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 4,
    "conditions_opened": 1, "remaining_named_conditions": 3
})
check("source return", "SOURCE_SILENT_SOBOLEV_COMPLETION" in ledger["source_return"])

required_layer0 = {
    "Y14_COMPACT_BOUNDARY_DIMENSION13",
    "OBSERVED_X4_BOUNDARY_DIMENSION3",
    "AUXILIARY_POSITIVE_SOBOLEV_TOPOLOGY",
    "PHYSICAL_K77_KREIN_PAIRING",
    "SAME_REGULARITY_H7_BY_H7_WEAK_FORM",
    "STRONG_COTANGENT_H7_BY_HMINUS7_FORM",
    "CONDITIONAL_NONEMPTY_EDGE_TORSOR_STRATUM",
    "ORDINARY_EVEN_STRONG_PRESYMPLECTIC_REDUCTION",
    "ODD_BFV_BRST_CHARGE_AND_CME",
    "CLASSICAL_CHARGED_CURRENT_ALGEBRA",
    "REAL_VERTICAL_COTANGENT_POLARIZATION",
}
check("layer0", required_layer0 <= set(ledger["layer0_objects_compared"]))

check("residue", ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("fifth quotient upgraded", "upgraded by v0.103" in ledger["residue"]["quotients_ranked_scope"])
check("queue", ledger["next_work_queue"][0]["rows"] == ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]
      and "common Green/Krein-domain" in ledger["next_work_queue"][0]["why"])

rows = {row["id"]: row for row in ledger["rows"] if row.get("row_status") != "SUPERSEDED"}
for row_id in ("LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"):
    check(f"{row_id} evidence", rows[row_id]["evidence"] == "selected-k77-sobolev-edge-current-algebra-2026-08-08.md")
    check(f"{row_id} frontier", "COMPACT_BOUNDARY_H7_HMINUS7_STRONG_EDGE_REDUCTION_CONDITIONAL" in rows[row_id]["frontier_grade"])

migrations = [m for m in ledger["migrations"] if m["from_version"] == "0.102" and m["to_version"] == "0.103"]
check("five migrations", [m["row_id"] for m in migrations] == ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"])
check("migration meanings", all(m["meaning_changed"] is False for m in migrations))

check("registry status", registry["status"].startswith("COMPACT_BOUNDARY_STRONG_SOBOLEV"))
check("orders", registry["sobolev_completion"]["boundary_dimension"] == 13
      and registry["sobolev_completion"]["gauge_and_edge_order"] == 8
      and registry["sobolev_completion"]["connection_and_distortion_order"] == 7
      and registry["sobolev_completion"]["momentum_order"] == -7)
check("weak/strong", registry["sobolev_completion"]["same_regularity_inverse"] == "UNBOUNDED"
      and registry["sobolev_completion"]["dual_regularity_form"] == "STRONG_CANONICAL_COTANGENT")
check("edge", registry["edge_reduction"]["dressing_is_split_submersion"] is True
      and registry["edge_reduction"]["kernel_equals_residual_gauge_orbit"] is True
      and registry["edge_reduction"]["global_torsor_nonemptiness"] == "OPEN")
check("charged", registry["charged_horn"]["classical_central_remainder"] == 0
      and registry["charged_horn"]["nonabelian"] is True)
check("polarization no selection", registry["polarization"]["selects_physical_horn"] is False)
check("odd BFV open", registry["analytic_fence"]["odd_bfv_brst_charge_cme"] == "OPEN")
check("controls", registry["controls"]["main"] == "59/59 PASS"
      and registry["controls"]["independent_sage"] == "22/22 PASS")
check("data fence", registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
      and registry["constraint_fence"]["new_booked_quotients"] == 0)
check("parent fence", "DIM2107" in registry["action_parent_fence"]["spin_native_selected_carrier"]
      and "DIM16382" in registry["action_parent_fence"]["two_u32_32_halves"]
      and "DIM16383" in registry["action_parent_fence"]["full_u64_64"])

check("report scope", "not yet full BFV" in report and "nonempty edge-torsor stratum" in report)
check("review verdict", "COMPACT_BOUNDARY_STRONG_SOBOLEV_REDUCTION_SURVIVES_CONDITIONALLY" in review)
check("symplectic review", "Symplectic geometry" in review and "only weak" in review)
check("analytic review", "Functional analysis" in review and "Noncompact" in review)

check("ledger ancestry", reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.103.json"))

if FAILURES:
    raise SystemExit("FAIL selected K77 Sobolev edge/current audit: " + "; ".join(FAILURES))
print("PASS selected K77 Sobolev edge/current audit")
