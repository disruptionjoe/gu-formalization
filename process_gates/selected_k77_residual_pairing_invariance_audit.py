#!/usr/bin/env python3
"""Fail-closed audit for the conditional K77 residual pairing wave."""

from pathlib import Path
import ast
import json


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


registry = strict("lab/process/selected-k77-residual-pairing-invariance.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.92.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
source = (ROOT / "lab/sources/selected-k77-residual-pairing-source-reinspection-2026-08-08.md").read_text(encoding="utf-8")
review = (ROOT / registry["hostile_review"]).read_text(encoding="utf-8")
report = (ROOT / "explorations/conditional-build/selected-k77-residual-pairing-invariance-2026-08-08.md").read_text(encoding="utf-8")

assert registry["status"].endswith("ANALYTIC_DOMAIN_OPEN")
assert registry["local_pairing"]["full_carrier"]["dimension"] == 29498
assert registry["local_pairing"]["full_carrier"]["inertia"] == [14749, 14749, 0]
assert registry["local_pairing"]["response_gram"]["dimension"] == 1470
assert registry["local_pairing"]["response_gram"]["rank"] == 1470
assert registry["local_pairing"]["response_gram"]["inertia"] == [741, 729, 0]
assert registry["invariance_selection"]["spin77_only_grade_weight_dimension"] == 3
assert registry["invariance_selection"]["full_u6464_grade_weight_dimension"] == 1
assert registry["invariance_selection"]["weyl_block_u3232_product_grade_weight_dimension"] == "OPEN"
assert registry["invariance_selection"]["full_u6464_witness_parity"] == ["odd_grade_1", "odd_grade_5"]
assert registry["invariance_selection"]["weyl_block_transfer"].startswith("INVALID")
assert registry["constraint_accounting"]["new_continuous_parameters_on_full_u6464_comparator"] == 0
assert registry["constraint_accounting"]["operative_weyl_block_unbooked_relative_weights"].startswith("OPEN")
assert registry["constraint_accounting"]["residue_change"] == 0
assert all(value == "UNUSED" for value in registry["external_datum"].values())
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"

assert ledger["schema_version"] == "0.92"
assert ledger["predecessor"].endswith("v0.91.json")
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["quotients_ranked"] == 5
assert ledger["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 1, "conditions_opened": 1, "remaining_named_conditions": 3}
assert ledger["source_return"] == registry["source_return"]
assert sum(1 for item in ledger["migrations"] if item.get("to_version") == "0.92") == 5
assert {item["row_id"] for item in ledger["wave_row_dispositions"]} == set(registry["ledger_rows"])
assert "lower-order" in ledger["next_work_queue"][0]["why"]
assert "Weyl-block" in ledger["next_work_queue"][0]["why"]

assert contract["standing_ledger"]["ref"].endswith("v0.92.json")
assert contract["purpose_lanes_preserved"] == ["1", "2", "3", "A"]
assert "NO_LANE_COUNT_CHANGE" in contract["non_effects"]
directive = contract["active_scientific_directives"][0]
assert "K_LOC" in directive["latest_residual_pairing_evidence"]
assert "WEYL_BLOCK_U3232_PRODUCT" in directive["next_run_method"]["target"]

assert "SOURCE-SILENT" in source and "real K77 residual bilinear" in source
assert "two copies of `C^(32,32)`" in source and "odd and exchange" in source
for term in ("Symplectic geometry", "Krein operator theory", "Complex/path-integral analysis", "PASS AFTER TWO SCOPE REPAIRS"):
    assert term in review
for forbidden in ("positive Hilbert norm is constructed", "formal adjoint is constructed", "global invariant residual subbundle is constructed"):
    assert forbidden not in report
assert "inertia `(741,729,0)`" in report
assert "v0.85" in report and "principal augmented-torsion" in report
assert "Weyl-block" in report and "comparator" in report

for relative in registry["scripts"]:
    path = ROOT / relative
    assert path.exists()
    if path.suffix == ".py":
        ast.parse(path.read_text(encoding="utf-8"))

for relative in (
    "NEXT-STEPS.md",
    "RESEARCH-STATUS.md",
    "lab/process/README.md",
    "lab/process/agent-context-pack.md",
    "lab/process/functional-channel-operating-contract-v1.0.md",
    "explorations/README.md",
    "lab/sources/README.md",
    "process_gates/README.md",
    "tests/README.md",
):
    assert "v0.92" in (ROOT / relative).read_text(encoding="utf-8") or relative in {
        "lab/sources/README.md", "process_gates/README.md", "tests/README.md"
    }

print("PASS selected K77 residual-pairing invariance audit")
