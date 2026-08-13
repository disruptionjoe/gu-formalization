#!/usr/bin/env python3
"""Fail-closed audit for conditional ledger v0.165 and its coupled domain gate."""

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
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=reject)


ledger = strict("lab/process/conditional-physics-ledger-v0.165.json")
result = strict("lab/process/selected-k77-coupled-green-domain.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
rows = {row["id"]: row for row in ledger["rows"]}
expected_rows = {"RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"}

check("ledger schema is v0.165", ledger["schema_version"] == "0.165")
check("ledger predecessor is v0.164", ledger["predecessor"].endswith("v0.164.json"))
check("run id is exact", ledger["updated_by"] == result["run_id"] == "RUN-20260811-033947-gu-k77-coupled-green-domain")
check("headline is unchanged", ledger["frontier_delta"]["headline_delta"] == "NONE")
check("frontier closes two and opens one", ledger["frontier_delta"]["conditions_closed"] == 2 and ledger["frontier_delta"]["conditions_opened"] == 1)
check("coverage remains 82 of 82", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("verdict counts remain exact", ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("residue stays 84", ledger["residue"]["continuous_real"] == 84)
check("five scoped quotients remain", ledger["residue"]["quotients_ranked"] == 5)
check("six current wave dispositions", {item["row_id"] for item in ledger["wave_row_dispositions"]} == expected_rows)
check("all six rows cite the new evidence", all(row_id in rows and rows[row_id]["evidence"] == "selected-k77-coupled-green-domain-2026-08-11.md" for row_id in expected_rows))
check("result has 47 passing checks", result["checks"]["total"] == 47 and result["checks"]["failures"] == 0)
check("full boundary rank is 3860", result["boundary_dimensions"]["total"] == 3860)
check("Lagrangian rank is 1930", result["boundary_dimensions"]["lagrangian"] == 1930)
check("graph family lower bound is 120", result["domain_family"]["minimum_symmetric_multiplicity_coordinates"] == 120)
check("graph is not selected", result["domain_family"]["unique_selection"] is False)
check("naive moving reality is rejected", result["reality"]["naive_total_extension"] == "REJECTED_BY_MOVING_NORMAL_MIXED_TERMS")
check("actual K77 domain remains open", result["reality"]["physical_k77_antilinear_reality"] == "OPEN" and result["reality"]["calderon_or_maximal_dissipative_domain"] == "OPEN")
check("P1 P2 P3 unchanged", result["p1_p2_p3_change"] == "none")
check("no canon or public posture movement", result["canon_verdict_change"] == result["public_posture_change"] == "none")
check("contract points to v0.165", contract["standing_ledger"]["ref"].endswith("v0.165.json") and contract["standing_ledger"]["human_ref"].endswith("v0.165.md"))
check("contract carries the new domain directive", "NAIVE_MOVING_TOTAL_REALITY" in contract["standing_ledger"]["source_owned_hull_interface_directive"])
check("contract requires bounded postflight mailbox disposition", contract["postflight_mailbox"]["scope"] == "ONE_BOUNDED_GU_MAILBOX_DELTA_REVIEW" and contract["postflight_mailbox"]["unbounded_archaeology_forbidden"] is True)

if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS: {23} coupled Green/domain audit checks")
