#!/usr/bin/env python3
"""Fail-closed audit for the K77 action/Frechet/Ward retype."""

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


registry = strict("lab/process/selected-k77-action-frechet-ward-object-separation.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.91.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")

assert registry["status"].endswith("ACTUAL_TRANSVERSE_J_AND_K_OPEN")
assert registry["exact_results"]["actual_full_coefficientwise_J_R_zero"].startswith("OPEN")
assert registry["frontier_delta"]["remaining_named_conditions"] == 2
assert registry["constraint_accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED"
assert registry["signature_condition"]["K77"]["real_dirac_dimension"] == 128
assert registry["signature_condition"]["K95"]["real_dirac_dimension"] == 256
assert registry["signature_condition"]["K77"]["complex_dirac_dimension"] == 128
assert registry["signature_condition"]["K95"]["complex_dirac_dimension"] == 128
assert registry["signature_condition"]["K95"]["symplectic_majorana_weyl_with_extra_doublet"] is True
assert ledger["predecessor"].endswith("v0.90.json")
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["quotients_ranked"] == 5
assert reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.91.json"
)

for relative in registry["scripts"].values():
    if not isinstance(relative, str) or not relative.endswith(".py"):
        continue
    ast.parse((ROOT / relative).read_text(encoding="utf-8"))

review = (ROOT / registry["hostile_review"]).read_text(encoding="utf-8")
assert "mandatory_symplectic_lens: completed" in review
assert "PASS_AFTER_SCOPE_REPAIR" in review
assert "summary-overrun charge" in review
assert "superseded-object charge" in review

print("PASS selected K77 action/Frechet/Ward object-separation audit")
