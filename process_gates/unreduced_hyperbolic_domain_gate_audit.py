#!/usr/bin/env python3
"""Fail-closed audit for conditional ledger v0.168 domain obstruction."""

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
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=reject)


ledger = strict("lab/process/conditional-physics-ledger-v0.168.json")
result = strict("lab/process/selected-k77-unreduced-hyperbolic-domain-gate.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
rows = {row["id"]: row for row in ledger["rows"]}
expected_rows = {"RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"}
migrations = [item for item in ledger["migrations"] if item["to_version"] == "0.168"]

check("ledger schema is v0.168", ledger["schema_version"] == "0.168")
check("ledger predecessor is v0.167", ledger["predecessor"].endswith("v0.167.json"))
check("run id is exact", ledger["updated_by"] == result["run_id"] == "historical-investigation")
check("headline is unchanged", ledger["frontier_delta"]["headline_delta"] == "NONE")
check("frontier is one closed one opened three remaining", ledger["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 1, "conditions_opened": 1, "remaining_named_conditions": 3})
check("coverage remains 82 of 82", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("verdict counts remain exact", ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("residue stays 84", ledger["residue"]["continuous_real"] == 84)
check("five scoped quotients remain", ledger["residue"]["quotients_ranked"] == 5)
check("six current wave dispositions", {item["row_id"] for item in ledger["wave_row_dispositions"]} == expected_rows)
check("six append-only migrations", len(migrations) == 6 and {item["row_id"] for item in migrations} == expected_rows)
check("all six rows cite the new evidence", all(rows[row]["evidence"] == "selected-k77-unreduced-hyperbolic-domain-gate-2026-08-11.md" for row in expected_rows))
check("result has 52 passing checks", result["checks"] == {"total": 52, "failures": 0})
check("operator is the current source-shaped K77 object", result["operator"]["typed_owner"] == "REAL_K77_SOURCE_SHAPED_OMEGA1_PLUS_OMEGA0_FOUR_FIELD_PRINCIPAL_OPERATOR" and result["operator"]["dimension"] == 1920)
check("old W131 object is fenced", result["operator"]["not_isolated_W131"] is True)
check("same-object bridge is explicit", result["operator"]["same_object_bridge"] == "D_CURRENT=-P_D_PRIOR_MINUS_P")
check("all three directions are tested", result["observed_evolution"]["directions"] == ["x", "y", "z"])
check("Jordan remainder rank is 128", result["observed_evolution"]["jordan_remainder_rank_each"] == 128)
check("Jordan remainder is square zero", result["observed_evolution"]["jordan_remainder_square_zero"] is True)
check("positive symmetrizer cone is empty", result["observed_evolution"]["positive_simultaneous_symmetrizer_cone"] == "EMPTY")
check("strong hyperbolicity fails only unreduced", result["observed_evolution"]["strong_hyperbolicity"] == "FAIL_UNREDUCED")
check("standard one-time route is killed", result["domain"]["standard_one_time_maximal_dissipative_route"] == "KILLED_UNREDUCED")
check("every closed graph is not killed", result["domain"]["every_closed_graph_realization"] == "NOT_KILLED")
check("ambient route is ultrahyperbolic typed", result["domain"]["ambient_y14"].startswith("ULTRAHYPERBOLIC"))
check("source-derived reduction stays open", result["domain"]["source_derived_reduction"] == "OPEN")
check("characteristic quotient is not promoted", result["domain"]["conditional_characteristic_quotient"].startswith("NOT_PROMOTED"))
check("graph and P1 P2 P3 stay unselected", result["selection"] == {"graph_selected": False, "minimum_coordinates_transported": 120, "P1_P2_P3": "UNUSED"})
check("no canon residue quotient or posture movement", set(result["accounting"].values()) == {"none"})
check("current append-only ledger descends to v0.168", reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.168.json"
))
check("postflight mailbox disposition is recorded", ledger["collision_disposition"].endswith("POSTFLIGHT_MAILBOX_NO_NEWER_ITEM_OR_PRIORITY_CHANGE"))

if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: 30 unreduced hyperbolic-domain audit checks")
