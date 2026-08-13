#!/usr/bin/env python3
"""Durability audit for ledger v0.148 P3 normal/tangential support gate."""

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


ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.148.json").read_text())
result = json.loads((ROOT / "lab/process/selected-k77-p3-normal-tangential-support.json").read_text())
report = (ROOT / "explorations/conditional-build/selected-k77-p3-normal-tangential-support-obstruction-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-p3-normal-tangential-support-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-p3-normal-tangential-support-source-reinspection-2026-08-10.md").read_text()
contract = json.loads((ROOT / "lab/process/functional-channel-operating-contract-v1.0.json").read_text())
tests_readme = (ROOT / "tests/README.md").read_text()
gates_readme = (ROOT / "process_gates/README.md").read_text()

check("ledger version is v0.148", ledger["schema_version"] == "0.148")
check("headline counts freeze", ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("residue freezes at 84", ledger["residue"]["continuous_real"] == 84)
check("five quotients remain", ledger["residue"]["quotients_ranked"] == 5)
check("normal projection has rank zero", result["actual_base_maps"]["rank_d_pi_on_normal_cycle"] == 0)
check("horizontal projection has rank four", result["actual_base_maps"]["rank_d_pi_on_horizontal_four_plane"] == 4)
check("source class is trivial on normal cycle", result["source_c2_on_normal_cycle"] == 0)
check("P3 positive horn remains nontrivial", result["p3_c2_on_normal_cycle"]["1"] == 1)
check("only P3 zero horn matches", result["matching_p3_horns_on_normal_cycle"] == [0])
check("horizontal SD rank is three", result["form_slot_ranks"]["horizontal_selfdual"] == 3)
check("normal SD rank is three", result["form_slot_ranks"]["normal_selfdual"] == 3)
check("combined form-slot rank is six", result["form_slot_ranks"]["combined"] == 6)
check("internal gauge cannot repair slots", result["internal_gauge_repairs_slot_mismatch"] is False)
check("planted soldering repairs slots", result["planted_horizontal_normal_soldering_repairs_slots"] is True)
check("planted soldering changes observation split", result["planted_soldering_preserves_observation_split"] is False)
check("report preserves abstract S4 theorem", "Abstract `S4` class theorem: **survives**" in report)
check("report stops before action restriction", "Do not restrict or vary the action until one successor passes" in report)
check("hostile review scopes current support kill", "kills the present support identification, not all P3-like data" in review)
check("hostile review contains symplectic lens", "**Symplectic/BV:**" in review)
check("source return confirms tangent-normal separation", "SOURCE_CONFIRMS_HORIZONTAL_TANGENT_VERSUS_NORMAL_BUNDLE_SEPARATION" in source)
current_ledger_ref = contract["standing_ledger"]["ref"]
current_ledger_minor = int(current_ledger_ref.rsplit("v0.", 1)[1].split(".json", 1)[0])
check("contract ledger is not older than v0.148", current_ledger_minor >= 148)
check("contract carries actual-base directive", "p3_normal_tangential_support_directive" in contract["standing_ledger"])
check("tests inventory names probe", "selected_k77_p3_normal_tangential_support_probe.py" in tests_readme)
check("process inventory names audit", "p3_normal_tangential_support_audit.py" in gates_readme)
check("P1 P2 P3 unchanged", result["p1_p2_p3_assignment_change"] is False)
check("no canon movement", result["canon_verdict_change"] is False)
check("no public-posture movement", result["public_posture_change"] is False)
check("source return is explicit", ledger["source_return"].startswith("SOURCE_CONFIRMS_HORIZONTAL_TANGENT_VERSUS_NORMAL_BUNDLE_SEPARATION"))
check("next gate prices a replacement before action", "COUNT_SURPLUS_BEFORE_ACTION_RESTRICTION" in result["next_gate"])

print(f"PASS {CHECKS}/{CHECKS}")
