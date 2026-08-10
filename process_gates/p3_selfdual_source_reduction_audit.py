#!/usr/bin/env python3
"""Durability audit for ledger v0.146 self-dual source-reduction kill."""

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


ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.146.json").read_text())
result = json.loads((ROOT / "lab/process/selected-k77-p3-selfdual-source-reduction.json").read_text())
report = (ROOT / "explorations/conditional-build/selected-k77-p3-selfdual-source-reduction-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-p3-selfdual-source-reduction-review.md").read_text()
contract = json.loads((ROOT / "lab/process/functional-channel-operating-contract-v1.0.json").read_text())
tests_readme = (ROOT / "tests/README.md").read_text()
gates_readme = (ROOT / "process_gates/README.md").read_text()

check("ledger version is v0.146", ledger["schema_version"] == "0.146")
check("headline counts freeze", ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("residue freezes at 84", ledger["residue"]["continuous_real"] == 84)
check("five quotients remain", ledger["residue"]["quotients_ranked"] == 5)
check("both factor ranks are three", result["factor_ranks"] == {"su2plus": 3, "su2minus": 3})
check("factor pairings are nonzero opposite", result["quadratic_pairings"] == {"su2plus": 12, "su2minus": -12, "full": 0})
check("current family intersects reduction only at zero", result["current_family_intersection"] == "t=0_ONLY")
check("split preservation does not select factor", result["split_preservation_selects_factor"] is False)
check("P3 source diagonal remains unbuilt", result["p3_source_diagonal"] == "UNBUILT")
check("restricted action is not promoted", result["restricted_action"] == "WELL_TYPED_GENERAL_CONSTRUCTION__GU_COEFFICIENTS_UNBUILT")
check("report distinguishes DBP from factor selection", "The first condition does not imply the second" in report)
check("report kills only current action", "current nonzero\nstationary family is not a connection" in report)
check("hostile review rejects post-solution projection", "projecting the old solution is not" in review)
check("hostile review preserves replacement", "PROJECTED_REPLACEMENT_REMAINS_NEW_CONSTRUCTION" in review)
current_ledger_ref = contract["standing_ledger"]["ref"]
current_ledger_minor = int(current_ledger_ref.rsplit("v0.", 1)[1].split(".json", 1)[0])
check("contract ledger is not older than v0.146", current_ledger_minor >= 146)
check("contract carries selfdual directive", "p3_selfdual_reduction_directive" in contract["standing_ledger"])
check("tests inventory names probe", "selected_k77_p3_selfdual_source_reduction_probe.py" in tests_readme)
check("process inventory names audit", "p3_selfdual_source_reduction_audit.py" in gates_readme)
check("P1 P2 P3 unchanged", result["p1_p2_p3"] == "UNCHANGED_AND_UNASSIGNED")
check("no canon movement", result["canon_verdict_change"] == "none")
check("source return is explicit", ledger["source_return"].startswith("SOURCE_SILENT_P3_SOURCE_DIAGONAL"))
check("next gate is restricted action", "RESTRICT_I1_BEFORE_VARIATION" in result["next_gate"])

print(f"PASS {CHECKS}/{CHECKS}")
