#!/usr/bin/env python3
"""Durability audit for ledger v0.143 global-projector/amplitude separation."""

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


ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.143.json").read_text())
result = json.loads((ROOT / "lab/process/selected-k77-global-projector-amplitude-layer0.json").read_text())
report = (ROOT / "explorations/conditional-build/selected-k77-global-projector-amplitude-layer0-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-global-projector-amplitude-layer0-review.md").read_text()
contract = json.loads((ROOT / "lab/methods/research-evidence-contract-v1.0.json").read_text())
tests_readme = (ROOT / "tests/README.md").read_text()
gates_readme = (ROOT / "process_gates/README.md").read_text()

check("ledger version is v0.143", ledger["schema_version"] == "0.143")
check("headline counts freeze", ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("residue freezes at 84", ledger["residue"]["continuous_real"] == 84)
check("five quotients remain", ledger["residue"]["quotients_ranked"] == 5)
check("projector adds zero amplitude equations", result["result"]["amplitude_equations_added_by_Q"] == 0)
check("screened response retains rank three", result["result"]["screened_response_rank"] == 3)
check("projecting T forces zero", result["result"]["field_in_image_Q"] == "T_EQUALS_ZERO")
check("supplied c remains supplied", result["result"]["ell_T_equals_c"] == "T_EQUALS_SUPPLIED_C")
check("source silence explicit", result["source_return"].startswith("SOURCE_SILENT"))
check("report separates screening", "screening and amplitude selection are separate" in report)
check("report keeps amplitude-dependent route open", "amplitude-dependent global solvability" in report)
check("report keeps external route open", "typed external value" in report and "external-value horn" in report)
check("hostile review refuses global no-go", "No global functional can select the amplitude" in review)
check("hostile review preserves cosmology dissent", "screening result" in review)
check("contract points to v0.143", contract["standing_ledger"]["ref"].endswith("v0.143.json"))
check("contract carries projector directive", "global_projector_amplitude_directive" in contract["standing_ledger"])
check("tests inventory names probe", "selected_k77_global_projector_amplitude_layer0_probe.py" in tests_readme)
check("process inventory names audit", "global_projector_amplitude_layer0_audit.py" in gates_readme)
check("P1 P2 P3 unchanged", result["p1_p2_p3"] == "UNCHANGED_AND_UNASSIGNED")
check("no canon movement", result["canon_verdict_change"] == "none")

print(f"PASS {CHECKS}/{CHECKS}")
