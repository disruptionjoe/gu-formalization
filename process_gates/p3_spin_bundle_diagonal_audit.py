#!/usr/bin/env python3
"""Durability audit for ledger v0.147 P3/chiral-spin bundle diagonal."""

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


ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.147.json").read_text())
result = json.loads((ROOT / "lab/process/selected-k77-p3-spin-bundle-diagonal.json").read_text())
report = (ROOT / "explorations/conditional-build/selected-k77-p3-spin-bundle-diagonal-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-p3-spin-bundle-diagonal-review.md").read_text()
contract = json.loads((ROOT / "lab/methods/research-evidence-contract-v1.0.json").read_text())
tests_readme = (ROOT / "tests/README.md").read_text()
gates_readme = (ROOT / "process_gates/README.md").read_text()

check("ledger version is v0.147", ledger["schema_version"] == "0.147")
check("headline counts freeze", ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("residue freezes at 84", ledger["residue"]["continuous_real"] == 84)
check("five quotients remain", ledger["residue"]["quotients_ranked"] == 5)
check("spin Chern pair is exact", result["spin_c2_pair"] == [1, -1])
check("positive P3 horn matches S plus", result["p3_matches"]["1"] == "S+")
check("negative P3 horn matches S minus", result["p3_matches"]["-1"] == "S-")
check("trivial P3 horn matches neither", result["p3_matches"]["0"] == "NONE")
check("arbitrary charge-one ASD orbit has five moduli", result["arbitrary_charge_one_asd_moduli_dim"] == 5)
check("homogeneous invariant deformation is zero", result["homogeneous_invariant_connection_deformations"] == 0)
check("report separates class from connection", "equal characteristic classes do not identify connections" in report)
check("report does not price gauge torsor as physical datum", "bundle isomorphisms form a\ngauge torsor" in report)
check("report stops before action", "It is not yet an action construction" in report)
check("hostile review preserves current-action kill", "v0.146 current-action kill: **survives**" in review)
check("hostile review scopes differential diagonal", "DIFFERENTIAL_DIAGONAL_REMAINS_CONDITIONAL" in review)
current_ledger_ref = contract["standing_ledger"]["ref"]
current_ledger_minor = int(current_ledger_ref.rsplit("v0.", 1)[1].split(".json", 1)[0])
check("contract ledger is not older than v0.147", current_ledger_minor >= 147)
check("contract carries diagonal directive", "p3_spin_bundle_diagonal_directive" in contract["standing_ledger"])
check("tests inventory names probe", "selected_k77_p3_spin_bundle_diagonal_probe.py" in tests_readme)
check("process inventory names audit", "p3_spin_bundle_diagonal_audit.py" in gates_readme)
check("P1 P2 P3 unchanged", result["p1_p2_p3_assignment_change"] is False)
check("no canon movement", result["canon_verdict_change"] is False)
check("no public-posture movement", result["public_posture_change"] is False)
check("source return is explicit", ledger["source_return"].startswith("SOURCE_SILENT_P3_SOURCE_CONNECTION_DIAGONAL"))
check("next gate is actual connection diagonal", "PROVE_SUPPLIED_BPST_EQUALS_SOURCE_CHIRAL_CONNECTION" in result["next_gate"])

print(f"PASS {CHECKS}/{CHECKS}")
