#!/usr/bin/env python3
"""Durability audit for ledger v0.149 P3 replacement-surplus gate."""

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


ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.149.json").read_text())
result = json.loads((ROOT / "lab/process/selected-k77-p3-replacement-surplus.json").read_text())
report = (ROOT / "explorations/conditional-build/selected-k77-p3-replacement-surplus-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-p3-replacement-surplus-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-p3-replacement-surplus-source-reinspection-2026-08-10.md").read_text()
contract = json.loads((ROOT / "lab/process/functional-channel-operating-contract-v1.0.json").read_text())
tests_readme = (ROOT / "tests/README.md").read_text()
gates_readme = (ROOT / "process_gates/README.md").read_text()

check("ledger version is v0.149", ledger["schema_version"] == "0.149")
check("predecessor is v0.148", ledger["predecessor"].endswith("v0.148.json"))
check("headline counts freeze", ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("residue freezes at 84", ledger["residue"]["continuous_real"] == 84)
check("five quotients remain", ledger["residue"]["quotients_ranked"] == 5)
check("natural H-N map space is zero", result["natural_h_to_sym2_dimension"] == 0)
check("general H-N subspace costs 24 functions", result["hn_general_subspace_function_dimension"] == 24)
check("one-vector H-N ansatz costs three functions", result["hn_one_vector_function_dimension"] == 3)
check("timelike ansatz has Lorentz inertia", result["hn_one_vector_inertias"]["timelike"] == [1, 3, 0])
check("null ansatz is fully degenerate", result["hn_one_vector_inertias"]["null"] == [0, 0, 4])
check("Lorentzian star squares to minus one", result["hodge_star_square"]["lorentzian"] == -1)
check("real Lorentzian plus eigenspace is absent", result["lorentzian_real_plus_one_eigenspace_dimension"] == 0)
check("complex Lorentzian plus-i eigenspace has dimension three", result["lorentzian_complex_plus_i_eigenspace_dimension"] == 3)
check("S4 and T4 control c2 differs", set(result["background_c2_controls"].values()) == {0, 1})
check("tangential identity costs zero coordinates", result["tangential_identity_new_continuous_coordinates"] == 0)
check("tangential plus one is not universal", result["tangential_plus_one_is_universal"] is False)
check("report keeps action-derived H-N revival", "not a no-go against an action-owned `u`" in report)
check("report stops before action restriction", "do not restrict the action yet" in report)
check("hostile review contains Layer-0 lens", "**Layer-0 semantics:**" in review)
check("hostile review contains prior-art lens", "**Prior art:**" in review)
check("hostile review contains analytic lens", "**Analytic:**" in review)
check("hostile review contains symplectic lens", "**Symplectic/BV:**" in review)
check("source return is explicit", "SOURCE_CONFIRMS_LORENTZIAN_TANGENT_NORMAL_SPINOR_SPLIT" in source)
current_ref = contract["standing_ledger"]["ref"]
current_minor = int(current_ref.rsplit("v0.", 1)[1].split(".json", 1)[0])
check("contract ledger is not older than v0.149", current_minor >= 149)
check("contract carries replacement-surplus directive", "p3_replacement_surplus_directive" in contract["standing_ledger"])
check("tests inventory names probe", "selected_k77_p3_replacement_surplus_probe.py" in tests_readme)
check("process inventory names audit", "p3_replacement_surplus_audit.py" in gates_readme)
check("P1 P2 P3 unchanged", result["p1_p2_p3_assignment_change"] is False)
check("no canon movement", result["canon_verdict_change"] is False)
check("no public-posture movement", result["public_posture_change"] is False)
check("next gate tests actual Lorentzian background", "ACTUAL_LORENTZIAN_CHIRAL_BUNDLE_C2" in result["next_gate"])

migrations = [m for m in ledger["migrations"] if m["to_version"] == "0.149"]
check("five v0.149 migrations", len(migrations) == 5)
check("all migrations preserve meaning", all(m["meaning_changed"] is False for m in migrations))

print(f"PASS {CHECKS}/{CHECKS}")
