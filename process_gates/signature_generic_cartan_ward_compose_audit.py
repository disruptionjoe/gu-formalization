#!/usr/bin/env python3
"""Fail-closed scope and wiring audit for Cartan/Ward composition."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            assert key not in out, f"duplicate key {key}: {path}"
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=hook)


ledger = strict("lab/process/conditional-physics-ledger-v0.90.json")
registry = strict("lab/process/signature-generic-cartan-ward-compose.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/signature-generic-cartan-ward-compose-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-signature-generic-cartan-ward-compose-review.md").read_text()
source = (ROOT / "lab/sources/signature-generic-cartan-ward-source-reinspection-2026-08-08.md").read_text()

assert ledger["schema_version"] == "0.90"
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["quotients_ranked"] == 5
assert registry["constraint_accounting"] == {
    "new_fields": 0,
    "new_coefficients": 0,
    "new_functions": 0,
    "new_quotients": 0,
    "external_datum_used": False,
    "residue_change": False,
    "headline_verdict_change": False,
}
assert "L_xi A = i_xi F_A + D_A(i_xi A)" in report
assert "selected-action Frechet coefficient bank" in report
assert "Mandatory symplectic geometry" in review
assert "Complex/path-integral" in review
assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert contract["standing_ledger"]["ref"].endswith("v0.90.json")
assert "CARTAN" in contract["standing_ledger"]["signature_branch_directive"]
assert registry["scope_boundary"]["selected_action_coefficientwise_JR_zero"] == "OPEN"
assert registry["external_datum"] == "P1_P2_P3_UNCHANGED_UNUSED"
print("PASS signature-generic Cartan/Ward composition scope audit")
