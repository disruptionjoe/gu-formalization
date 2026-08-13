#!/usr/bin/env python3
"""Durability audit for ledger v0.144 characteristic-amplitude horn."""

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


ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.144.json").read_text())
result = json.loads((ROOT / "lab/process/selected-k77-p3-characteristic-amplitude-selector.json").read_text())
report = (ROOT / "explorations/conditional-build/selected-k77-p3-characteristic-amplitude-selector-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-p3-characteristic-amplitude-selector-review.md").read_text()
contract = json.loads((ROOT / "lab/methods/research-evidence-contract-v1.0.json").read_text())
tests_readme = (ROOT / "tests/README.md").read_text()
gates_readme = (ROOT / "process_gates/README.md").read_text()

check("ledger version is v0.144", ledger["schema_version"] == "0.144")
check("headline counts freeze", ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("residue freezes at 84", ledger["residue"]["continuous_real"] == 84)
check("five quotients remain", ledger["residue"]["quotients_ranked"] == 5)
check("conditional magnitude selector recorded", result["result"]["fixed_nonzero_pairing_continuous_dimension"] == 0)
check("current P3 adds no source equation", result["result"]["current_p3_source_equations_added"] == 0)
check("sign remains discrete", result["result"]["remaining_discrete_signs"] == 2)
check("free normalization relocation explicit", result["result"]["free_normalization"] == "RELOCATES_CONTINUOUS_FREEDOM")
check("P1 sign map stays open", result["result"]["p1_sign_map"] == "NOT_ESTABLISHED")
check("source silence explicit", result["source_return"].startswith("SOURCE_SILENT"))
check("report separates P3 and source connection", "does **not yet do this**" in report)
check("report states nonzero pairing kill", "pairing `C_B` vanishes" in report)
check("hostile review rejects present selection", "P3 selects the GU vacuum" in review)
check("hostile review demands surplus", "Without that positive" in review and "constraint surplus" in review)
check("contract points to v0.144", contract["standing_ledger"]["ref"].endswith("v0.144.json"))
check("contract carries topology directive", "characteristic_amplitude_directive" in contract["standing_ledger"])
check("tests inventory names probe", "selected_k77_p3_characteristic_amplitude_selector_probe.py" in tests_readme)
check("process inventory names audit", "p3_characteristic_amplitude_selector_audit.py" in gates_readme)
check("P1 P2 P3 unchanged", result["p1_p2_p3"] == "UNCHANGED_AND_UNASSIGNED")
check("no canon movement", result["canon_verdict_change"] == "none")

print(f"PASS {CHECKS}/{CHECKS}")
