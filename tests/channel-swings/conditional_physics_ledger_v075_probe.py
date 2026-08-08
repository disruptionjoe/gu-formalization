#!/usr/bin/env python3
"""Integrity checks for conditional physics ledger v0.75."""

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


old = strict("lab/process/conditional-physics-ledger-v0.74.json")
new = strict("lab/process/conditional-physics-ledger-v0.75.json")
registry = strict("lab/process/selected-k77-action-contact-legendre-owner.json")

check("schema", "ledger advances once", old["schema_version"] == "0.74" and new["schema_version"] == "0.75")
check("schema", "predecessor is v0.74", new["predecessor"].endswith("v0.74.json"))
check("meter", "coverage remains 82 of 82", new["progress"]["mapped"] == new["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("meter", "residue remains frozen",
      new["residue"]["continuous_real"] == old["residue"]["continuous_real"] == 84
      and new["residue"]["function_valued_at_least"] == old["residue"]["function_valued_at_least"]
      and new["residue"]["open_discrete_forks"] == old["residue"]["open_discrete_forks"])
check("meter", "five scoped quotients remain", new["residue"]["quotients_ranked"] == old["residue"]["quotients_ranked"] == 5)
check("frontier", "frontier delta is 2 closed 1 opened 2 remaining",
      new["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 2,
                                "conditions_opened": 1, "remaining_named_conditions": 2})
check("source", "source return types confirmation silence and correction",
      all(marker in new["source_return"] for marker in ("SOURCE-CONFIRMS", "SOURCE-SILENT", "REPO-CORRECTS")))

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
expected = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}
check("rows", "row IDs remain immutable", set(old_rows) == set(new_rows))
check("rows", "exactly five named rows migrate",
      {rid for rid in old_rows if old_rows[rid] != new_rows[rid]} == expected)
for rid in sorted(expected):
    check("rows", f"{rid} verdict remains frozen", new_rows[rid]["verdict"] == old_rows[rid]["verdict"])
    check("rows", f"{rid} reason kind remains frozen", new_rows[rid]["reason_kind"] == old_rows[rid]["reason_kind"])
    check("rows", f"{rid} points to v0.75 evidence",
          new_rows[rid]["evidence"] == "selected-k77-action-contact-legendre-owner-2026-08-08.md")
    check("rows", f"{rid} preserves generic contact theorem", "GENERIC_CONTACT_WARD_THEOREM_EXACT" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} rejects p=KT action ownership", "P_EQUALS_KT_ACTION_OWNER_REJECTED" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} leaves actual K77 bank open", "ACTUAL_K77_LEGENDRE_GREEN" in new_rows[rid]["mapping_grade"] and "OPEN" in new_rows[rid]["mapping_grade"])

migrations = [item for item in new["migrations"]
              if item.get("from_version") == "0.74" and item.get("to_version") == "0.75"]
check("migration", "five append-only migration edges exist",
      len(migrations) == 5 and {item["row_id"] for item in migrations} == expected)
check("registry", "two indefinite K controls are inequivalent",
      registry["exact"]["indefinite_K_controls"] == 2 and registry["exact"]["different_KT_momenta"] is True)
check("registry", "selected action is cubically nonquadratic",
      registry["exact"]["selected_action_cubic_live"] is True)
check("registry", "E_B minus E_T is nonzero at T zero",
      registry["exact"]["E_B_minus_E_T_at_T_zero_nonzero"] is True)
check("registry", "fixed linear KT identity is rejected",
      registry["exact"]["fixed_linear_KT_global_identity"] is False
      and registry["corrected"]["p_equals_KT_selected_action_owner"] == "REJECTED")
check("registry", "one-point K fit is underconstrained",
      registry["exact"]["one_point_symmetric_K_parameters"] == 45
      and registry["exact"]["one_point_fit_constraint_rank"] == 9
      and registry["exact"]["one_point_fit_free_dimension"] == 36)
check("registry", "generic theorem and endpoint quotient survive",
      registry["preserved"]["two_connection_contact_map"] == "EXACT"
      and registry["preserved"]["direct_sum_local_quotient"] == "40_OF_40"
      and registry["preserved"]["single_holonomy_compression_no_go"] == "20_OF_40_ONLY")
check("queue", "rank one is actual all-ten action bank", "actual ten-direction" in new["next_work_queue"][0]["why"])
check("scope", "no constraint-accounting movement", set(registry["constraint_accounting"].values()) == {0})
check("scope", "P1 P2 P3 remain unused", set(registry["external_datum"].values()) == {"UNUSED"})
check("scope", "Curt and third-lane fences remain", registry["program_fences"]["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and registry["program_fences"]["third_lane"] == "NOT_PROMOTED")

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
