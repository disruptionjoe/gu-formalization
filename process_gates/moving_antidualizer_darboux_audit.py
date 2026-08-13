#!/usr/bin/env python3
"""Fail-closed audit for conditional ledger v0.166 and adaptive preflight."""

from __future__ import annotations

import json
from pathlib import Path


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


ledger = strict("lab/process/conditional-physics-ledger-v0.166.json")
result = strict("lab/process/selected-k77-moving-antidualizer-darboux.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
rows = {row["id"]: row for row in ledger["rows"]}
expected_rows = {"RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"}
current_migrations = [
    item for item in ledger["migrations"] if item["to_version"] == "0.166"
]

check("ledger schema is v0.166", ledger["schema_version"] == "0.166")
check("ledger predecessor is v0.165", ledger["predecessor"].endswith("v0.165.json"))
check("run id is exact", ledger["updated_by"] == result["run_id"] == "RUN-20260811-040603-gu-k77-moving-antidualizer-darboux")
check("headline is unchanged", ledger["frontier_delta"]["headline_delta"] == "NONE")
check("frontier closes one and opens one", ledger["frontier_delta"]["conditions_closed"] == 1 and ledger["frontier_delta"]["conditions_opened"] == 1)
check("coverage remains 82 of 82", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("verdict counts remain exact", ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("residue stays 84", ledger["residue"]["continuous_real"] == 84)
check("five scoped quotients remain", ledger["residue"]["quotients_ranked"] == 5)
check("six current wave dispositions", {item["row_id"] for item in ledger["wave_row_dispositions"]} == expected_rows)
check("six append-only migrations", len(current_migrations) == 6 and {item["row_id"] for item in current_migrations} == expected_rows)
check("all six rows cite the new evidence", all(rows[row_id]["evidence"] == "selected-k77-moving-antidualizer-darboux-2026-08-11.md" for row_id in expected_rows))
check("result has 46 passing checks", result["checks"]["total"] == 46 and result["checks"]["failures"] == 0)
check("potential identity is exact", result["darboux_completion"]["potential_identity"] is True)
check("half shear is forced", result["darboux_completion"]["shear_coefficient"] == "1/2__FORCED_IN_FIRST_JET_ANSATZ")
check("no square root or positive factorization", result["darboux_completion"]["square_root_or_positive_factorization"] == "NOT_USED")
check("moving map is involutive and anti-symplectic", result["moving_antidualizer"]["algebraic_involution"] is True and result["moving_antidualizer"]["anti_symplectic"] is True)
check("physical K77 reality stays open", result["moving_antidualizer"]["physical_k77_reality"].startswith("OPEN"))
check("graph family is transported not selected", result["selection"]["family_transported"] is True and result["selection"]["unique_graph_selected"] is False)
check("graph lower bound remains 120", result["selection"]["minimum_symmetric_multiplicity_coordinates"] == 120)
check("analytic domain remains open", set(result["analytic_domain"].values()) == {"OPEN"})
check("P1 P2 P3 unchanged", result["p1_p2_p3_change"] == "none")
check("no canon or posture movement", result["canon_verdict_change"] == result["public_posture_change"] == "none")
check("contract points to v0.166", contract["standing_ledger"]["ref"].endswith("v0.166.json") and contract["standing_ledger"]["human_ref"].endswith("v0.166.md"))
check("adaptive preflight has exactly three universal lenses", contract["preflight"]["universal_core"] == ["LAYER0_SEMANTICS", "PRIOR_ART_AND_SOURCE_COLLISION", "CONSTRUCTION_VERSUS_SELECTION"])
check("adaptive preflight records five routing fields", len(contract["preflight"]["required_lens_record"]) == 5)
router = contract["channels"]["VERIFY"]["efficient_specialist_routing"]
check("generic mandatory eight is retired", "mandatory_eight" not in router and router["superseded_generic_core"].startswith("MANDATORY_EIGHT_RETIRED"))
check("one contrary path is mandatory", router["contrary_path_lens_required"] is True)
check("contract requires bounded postflight mailbox disposition", contract["postflight_mailbox"]["scope"] == "ONE_BOUNDED_GU_MAILBOX_DELTA_REVIEW")

if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: 29 moving anti-dualizer/adaptive-preflight audit checks")
