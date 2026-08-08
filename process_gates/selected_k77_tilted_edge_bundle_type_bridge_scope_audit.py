#!/usr/bin/env python3
"""Fail closed if the tilted edge-bundle result outruns its exact type gate."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-tilted-edge-bundle-type-bridge-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-tilted-edge-bundle-type-bridge-review.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-tilted-edge-bundle-type-bridge.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.71.json").read_text())

assert "TILTED_AFFINE_COCYCLE_EXACT__V70_EDGE_TYPE_MISMATCH__BRIDGE_OPEN" in report
assert "constant nonzero `xi`" in report
assert "Mandatory symplectic reading" in report
assert "SOURCE-CONFIRMS" in report and "SOURCE-SILENT" in report
assert "global quotient added: 0" in report
assert "P1/P2/P3 consumed: 0" in report
assert "Symplectic-geometry lens" in review
assert "summary outrun" in review
assert "superseded or mistyped object" in review
assert registry["exact_result"]["tilted_maurer_cartan_cocycle"] == "EXACT"
assert registry["exact_result"]["constant_xi_affine_shift"] == "ZERO"
assert registry["exact_result"]["constant_xi_edge_shift"] == "NONZERO"
assert registry["exact_result"]["direct_identity_bridge"] == "KILLED"
assert registry["exact_result"]["zero_order_glv_vstar_to_scalar_nullity"] == 0
assert registry["construction_disposition"]["typed_bridge_to_tau_a0_affine_field"] == "OPEN"
assert registry["construction_disposition"]["physical_bfv_phase_space"] == "OPEN"
assert registry["external_datum"]["free_object_delta"] == 0
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["quotients_ranked"] == 5
assert "group-valued boundary edge frame" in ledger["next_work_queue"][0]["why"]
print("PASS selected K77 tilted edge-bundle type bridge scope audit")
