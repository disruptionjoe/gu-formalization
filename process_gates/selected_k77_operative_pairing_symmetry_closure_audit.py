#!/usr/bin/env python3
"""Fail-closed audit for the v0.93 operative pairing-symmetry closure."""

from pathlib import Path
import ast
import json

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]


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


registry = strict("lab/process/selected-k77-operative-pairing-symmetry-closure.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.93.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-operative-pairing-symmetry-closure-2026-08-08.md").read_text(encoding="utf-8")
review = (ROOT / registry["hostile_review"]).read_text(encoding="utf-8")
source = (ROOT / "lab/sources/selected-k77-residual-pairing-source-reinspection-2026-08-08.md").read_text(encoding="utf-8")

assert registry["status"].startswith("SELECTED_GRADE125_SPIN_NATIVE")
assert registry["closure"]["spin77"] == {
    "complex_dimension": 2107,
    "carrier": "Lambda1 plus Lambda2 plus Lambda5",
    "preserves_selected": True,
    "invariant_symmetric_pairing_dimension": 3,
}
assert registry["closure"]["weyl_block_u3232_product"]["complex_dimension"] == 16382
assert registry["closure"]["weyl_block_u3232_product"]["preserves_selected"] is False
assert registry["closure"]["weyl_block_u3232_product"]["invariant_symmetric_pairing_dimension"] == 3
assert registry["closure"]["weyl_block_plus_chirality_exchange"]["invariant_symmetric_pairing_dimension"] == 2
assert registry["closure"]["weyl_block_plus_chirality_exchange"]["exchange_source_status"] == "NOT_ESTABLISHED"
assert registry["closure"]["full_u6464"]["complex_dimension"] == 16383
assert registry["closure"]["full_u6464"]["preserves_selected"] is False
assert registry["closure"]["full_u6464"]["invariant_symmetric_pairing_dimension"] == 1
assert registry["closure"]["explicit_escape_grades"] == [3, 4, 7]

accounting = registry["constraint_accounting"]
assert accounting["booked_continuous_residue"] == 84
assert accounting["conditional_continuous_residue_by_parent"] == {
    "full_u6464_parent": 84,
    "weyl_block_plus_exchange_parent": 85,
    "weyl_block_or_spin_native_parent": 86,
}
assert accounting["residue_change"] == 0
assert all(value == "UNUSED" for value in registry["external_datum"].values())
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"

assert ledger["schema_version"] == "0.93"
assert ledger["predecessor"].endswith("v0.92.json")
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["continuous_real_range_by_action_parent"] == "84..86"
assert ledger["residue"]["conditional_pairing_weight_coordinates"]["weyl_block_or_spin_native_parent"] == 2
assert ledger["residue"]["quotients_ranked"] == 5
assert ledger["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 2, "conditions_opened": 1, "remaining_named_conditions": 2}
assert ledger["source_return"] == registry["source_return"]
assert sum(1 for item in ledger["migrations"] if item.get("to_version") == "0.93") == 5
assert {item["row_id"] for item in ledger["wave_row_dispositions"]} == set(registry["ledger_rows"])
assert "conditionall" not in ledger["next_work_queue"][0]["why"].lower()
assert "conditional Spin-native" in ledger["next_work_queue"][0]["why"]

assert reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.93.json"
)

assert "two copies of `C^(32,32)`" in source
assert "principal bundle has structure group" in source
for term in ("Symplectic geometry", "Representation theory", "Complex/path-integral", "PASS AFTER ACTION-PARENT"):
    assert term in review
for term in ("2,107", "16,382", "16,383", "two `C^(32,32)` Weyl halves", "full `U(64,64)`"):
    assert term in report
for forbidden in ("positive Hilbert space is constructed", "formal adjoint is constructed", "source selects the action parent"):
    assert forbidden not in report

for relative in registry["scripts"]:
    path = ROOT / relative
    assert path.exists()
    if path.suffix == ".py":
        ast.parse(path.read_text(encoding="utf-8"))

print("PASS selected K77 operative pairing-symmetry closure audit")
