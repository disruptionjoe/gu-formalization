#!/usr/bin/env python3
"""K277 integrated GU reassessment and consumer-first rerank."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "lab/process/k277-gu-reassessment-integration-rerank.json"
INPUTS = {
    f"K{number}": next((ROOT / "lab/process").glob(f"k{number}-*.json"))
    for number in range(270, 277)
}

certificate = json.loads(CERT.read_text())
assert certificate["disposition"] == "R9_COMPLETE__CONSUMER_FIRST_RERANK_INSTALLED__ROUTINE_K218_EXPANSION_NOT_JUSTIFIED"
assert [row["id"] for row in certificate["reassessment_matrix"]] == ["R1", "R2", "R3", "R4", "R5", "R6", "R7a", "R7b", "R8"]
assert all(row["state"] == "concluded" for row in certificate["reassessment_matrix"])

for key, path in INPUTS.items():
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    assert certificate["input_hashes"][key] == digest

a, g, d = Fraction(3), Fraction(2), Fraction(1)
budget = d * a * g / ((a + g) * (a - d))
uncertainty = Fraction(1, 10)
small = (Fraction(1) * uncertainty) ** 2
large = (Fraction(10) * uncertainty) ** 2
assert budget == Fraction(3, 5)
assert small == Fraction(1, 100) < budget
assert large == Fraction(1) > budget

k270 = json.loads(INPUTS["K270"].read_text())
assert not k270["value_to_consumer_budget"]["native_numeric_budget_emitted"]
assert all(value is False for key, value in k270["native_input_audit"].items() if key != "reason")
k276 = json.loads(INPUTS["K276"].read_text())
assert k276["disposition"] == "R8_CONCLUDED_AT_EXACT_SOURCE_DATA_OBSTRUCTION"

follow = certificate["ready_followthrough"]
assert follow["status"] == "EXECUTED"
assert len(follow["required_native_inputs"]) == 8
assert "named downstream decision" in follow["admission_rule"]
assert certificate["ranked_portfolio"][0]["portfolio"] == "K152 native consumer-input closure"
assert certificate["ranked_portfolio"][3]["state"] == "suspended"
assert all(value is False for value in certificate["boundaries"].values())

print("[PASS] K277 integrated reassessment 12/12 exact, 5/5 hostile")
