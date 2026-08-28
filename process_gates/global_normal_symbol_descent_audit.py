#!/usr/bin/env python3
"""Fail-closed audit for conditional ledger v0.167 normal-symbol descent."""

from __future__ import annotations

import json
from pathlib import Path

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]
FAILURES: list[str] = []


def check(label: str, condition: object) -> None:
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative: str):
    path = ROOT / relative

    def reject(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result

    return json.loads(path.read_text(), object_pairs_hook=reject)


ledger = strict("lab/process/conditional-physics-ledger-v0.167.json")
result = strict("lab/process/selected-k77-global-normal-symbol-descent.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
rows = {row["id"]: row for row in ledger["rows"]}
expected_rows = {"RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"}
current_migrations = [item for item in ledger["migrations"] if item["to_version"] == "0.167"]

check("ledger schema is v0.167", ledger["schema_version"] == "0.167")
check("ledger predecessor is v0.166", ledger["predecessor"].endswith("v0.166.json"))
check("run id is exact", ledger["updated_by"] == result["run_id"] == "historical-investigation")
check("headline is unchanged", ledger["frontier_delta"]["headline_delta"] == "NONE")
check("frontier delta is 2 closed 1 opened 3 remaining", ledger["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 2, "conditions_opened": 1, "remaining_named_conditions": 3})
check("coverage remains 82 of 82", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("verdict counts remain exact", ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("residue stays 84", ledger["residue"]["continuous_real"] == 84)
check("five scoped quotients remain", ledger["residue"]["quotients_ranked"] == 5)
check("six current wave dispositions", {item["row_id"] for item in ledger["wave_row_dispositions"]} == expected_rows)
check("six append-only migrations", len(current_migrations) == 6 and {item["row_id"] for item in current_migrations} == expected_rows)
check("all six rows cite the new evidence", all(rows[row_id]["evidence"] == "selected-k77-global-normal-symbol-descent-2026-08-11.md" for row_id in expected_rows))
check("result has 46 passing checks", result["checks"] == {"total": 46, "failures": 0})
check("normal owner is the four-field fermion symbol", result["normal_symbol"]["typed_owner"] == "FIRST_ORDER_FOUR_FIELD_FERMION_PRINCIPAL_SYMBOL")
check("bosonic bank and scalar comparator are fenced", result["normal_symbol"]["not_bosonic_EB_minus_ET_bank"] is True and result["normal_symbol"]["not_v0165_scalar_comparator"] is True)
check("symbol is global morphism not automorphism", result["normal_symbol"]["global_associated_bundle_morphism"] is True and result["normal_symbol"]["global_automorphism"] is False)
check("actual causal ranks are exact", (result["normal_symbol"]["nonnull_rank"], result["normal_symbol"]["null_rank"], result["normal_symbol"]["null_kernel"]) == (1920, 1024, 896))
check("real Cl77 control is fenced", result["real_cl77_control"]["spin_dimension"] == 128 and result["real_cl77_control"]["not_substituted_for_full_symbol"] is True)
check("control reproduces causal degeneracy", result["real_cl77_control"]["nonnull_rank"] == 128 and result["real_cl77_control"]["null_rank"] == 64 and result["real_cl77_control"]["null_square_zero"] is True)
check("Darboux descent is complete on three patches", all(result["darboux_descent"][key] is True for key in ("complete_potential", "half_shear", "cotangent_overlap_shift", "three_patch_noncommuting_cocycle")))
check("Darboux descent is noncharacteristic only", result["darboux_descent"]["requires_noncharacteristic_normal"] is True)
check("graph remains unselected with 120 coordinates", result["selection"]["graph_selected"] is False and result["selection"]["minimum_coordinates_transported"] == 120)
check("P1 P2 P3 remain unused", result["selection"]["P1_P2_P3"] == "UNUSED")
check("nonnull successor is hyperbolic-domain typed", "MAXIMAL_DISSIPATIVE" in result["analytic_successor"]["nonnull"] and "CALDERON_ONLY_IF_ELLIPTIC" in result["analytic_successor"]["nonnull"])
check("null successor is a separate characteristic relation", result["analytic_successor"]["null"].startswith("SEPARATE_CHARACTERISTIC_RELATION"))
check("no canon residue quotient or posture movement", set(result["accounting"].values()) == {"none"})
check("current append-only ledger descends to v0.167", reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.167.json"
))
check("postflight mailbox disposition is recorded", ledger["collision_disposition"].endswith("POSTFLIGHT_MAILBOX_NO_NEWER_ITEM_OR_PRIORITY_CHANGE"))

if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: 28 global normal-symbol descent audit checks")
