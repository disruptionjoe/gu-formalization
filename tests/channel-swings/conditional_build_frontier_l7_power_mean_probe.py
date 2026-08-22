"""Exact propagation probe for the CBRS frontier rebuild and L7 Lean kernel."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/conditional-build-frontier-and-l7-power-mean.json"
RESULT = ROOT / "explorations/conditional-build/conditional-build-frontier-and-l7-power-mean-2026-08-22.md"
LEAN = ROOT / "Lean/GUFormalization/PowerMeanReduction.lean"

checks = 0


def check(condition: bool, label: str) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


data = json.loads(REGISTRY.read_text())
result = RESULT.read_text()
lean = LEAN.read_text()
root_lean = (ROOT / "Lean/GUFormalization.lean").read_text()
ledger = (ROOT / "lab/process/lean-verification-lane-LEDGER.md").read_text()
state = (ROOT / "CURRENT-STATE.yaml").read_text()
agenda = json.loads((ROOT / "lab/process/RESEARCH-AGENDA.json").read_text())

check(data["schema_version"] == "1.0", "schema")
check(data["admissible_candidate_count"] == 0, "empty admitted set")
check(len(data["admission_requirements"]) == 4, "four admission requirements")
check(len(data["candidate_census"]) == 7, "seven registered candidates")
check(all(not row["eligible"] for row in data["candidate_census"]), "no eligible candidate")
check(all(row["missing"] for row in data["candidate_census"]), "each candidate has exact missing owner")
check(data["cbrs1_state"] == "PARKED_UNTIL_COMPLETE_NEW_OWNER_PACKET", "CBRS-1 parked")
check("LOCAL_SOLUTION" in data["cbrs2_state"], "CBRS-2 dependency")

ids = {row["id"] for row in data["candidate_census"]}
for required in {
    "SECOND_SIGMA_FUNCTION",
    "INDEPENDENT_WODD_FIELD",
    "PROJECTED_T_TRACE_AXIAL_COMPONENT",
    "RESIDUAL_SQUARE_OR_SOURCE_XI_OMEGA",
    "CONTINUOUS_TOP_FORM_FLUX",
    "GRASSMANN_ODD_FERMION_SADDLE",
    "UNRELEASED_CYCLIC_TWO_CONNECTION",
}:
    check(required in ids, f"candidate {required}")

check("GU-COMPARATOR-ROUTING" in result, "routing notice")
check("GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY" in result, "routing class")
check("```gu-typed-objects" in result, "typed objects")
check("registry-relative" in result, "claim ceiling")
check("not a universal no-go" in result.lower(), "no universal no-go")
check("L8 chi-parity kernel" in result, "next gate")

for theorem in data["l7"]["theorems"]:
    check(f"theorem {theorem}" in lean, f"Lean theorem {theorem}")

check("sq_sum_le_card_mul_sum_sq" in lean, "mathlib inequality owner")
check("Fin 96" in lean, "96-cell specialization")
check("sorry" not in lean.lower(), "no sorry")
check("axiom" not in lean.lower(), "no axiom")
check("import GUFormalization.PowerMeanReduction" in root_lean, "default target import")
check("source document not located" not in ledger, "stale missing-source note removed")
check("LEAN-VERIFIED" in ledger and "L7 THEOREM D" in ledger, "ledger closure")
check(data["l7"]["source"] in result, "source path propagated")
check(data["l7"]["exact_companion"] in result, "companion path propagated")

check("admissible set is empty" in state, "current state frontier")
check("power-mean" in state.lower(), "current state L7")
items = {item["id"]: item for item in agenda["work_items"]}
check("PROOF-STABLE-KERNELS" in items, "proof agenda item")
check("L8" in items["PROOF-STABLE-KERNELS"]["next_swing"], "agenda advances to L8")
check("park" in items["CONDITIONAL-BUILD-REVERSE-SCAFFOLD"]["next_swing"].lower(), "agenda parks CBRS-1")

check(data["ledger_verdict_change"] == "none", "ledger unchanged")
check(data["source_ownership_change"] == "none", "source ownership unchanged")
check(data["canon_verdict_change"] == "none", "canon unchanged")
check(data["public_posture_change"] == "none", "public posture unchanged")

print(f"PASS {checks}/{checks}")
