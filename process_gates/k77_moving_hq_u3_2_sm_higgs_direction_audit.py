#!/usr/bin/env python3
"""Fail-closed audit for moving H_q, U(3,2), SM and Higgs direction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.196.json"
REGISTRY = ROOT / "lab/process/selected-k77-moving-hq-u3_2-sm-higgs-direction-gate.json"
REPORT = ROOT / "explorations/conditional-build/selected-k77-moving-hq-u3_2-sm-higgs-direction-gate-2026-08-12.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-moving-hq-u3_2-sm-higgs-direction-review.md"
SOURCE = ROOT / "lab/sources/selected-k77-moving-hq-u3_2-sm-higgs-direction-source-return-2026-08-12.md"


def fail(message: str) -> None:
    raise SystemExit("FAIL: " + message)


ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
report = REPORT.read_text(encoding="utf-8")
review = REVIEW.read_text(encoding="utf-8")
source = SOURCE.read_text(encoding="utf-8")

if ledger["schema_version"] != "0.196" or ledger["predecessor"] != "lab/process/conditional-physics-ledger-v0.195.json":
    fail("ledger version/predecessor mismatch")
if ledger["progress"]["mapped"] != 82 or ledger["progress"]["verdict_counts"] != {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
}:
    fail("headline accounting changed")
if ledger["residue"]["continuous_real"] != 84 or ledger["residue"]["function_valued_at_least"] != 19:
    fail("booked residue changed")

result = registry["result"]
expected = {
    "checks": 57,
    "failures": 0,
    "u3_2_dimension": 25,
    "su3_2_dimension": 24,
    "orthogonal_J_family_dimension": 20,
    "pati_salam_intersect_u3_2_dimension": 13,
    "pati_salam_intersect_su3_2_dimension": 12,
    "actual_chiral_spin_hypercharge_states": 16,
    "post_higgs_stabilizer_dimension": 9,
    "post_higgs_derived_dimension": 8,
    "post_higgs_center_dimension": 1,
    "compact_q_orbit_dimension": 3,
    "radial_coefficients_needed": 1,
    "conditional_higgs_carrier_real_dimension": 4,
}
for key, value in expected.items():
    if result.get(key) != value:
        fail(f"registry {key} mismatch")
if result["selected_J"] != "OPEN" or result["radial_varpi_owner"] != "OPEN":
    fail("selection burden overpromoted")
if result["kinetic_potential_yukawa_stationarity"] != "OPEN":
    fail("Higgs action overpromoted")

for token in (
    "S(U(3)xU(2))",
    "positive-chiral 16",
    "post-Higgs",
    "20-dimensional family",
    "radial coefficient",
    "U(32,32)",
):
    if token not in report:
        fail(f"report missing {token}")
if "actual chiral spin representation" not in review or "Higgs-carrier" not in review:
    fail("hostile review missing material repair/fence")
for claim_id in ("SC-GRP-01", "SC-GRP-02", "SC-GRP-03", "SC-FER-03", "SC-GEO-58", "SC-META-57", "SC-SIG-52"):
    if claim_id not in source:
        fail(f"source return missing {claim_id}")

rows = {row["id"]: row for row in ledger["rows"]}
for row_id in registry["ledger_rows"]:
    if row_id not in rows or rows[row_id]["evidence"] != REPORT.name:
        fail(f"row {row_id} did not migrate to this evidence")
if len(ledger["migrations"]) != 141 or ledger["migration_history"] != ledger["migrations"]:
    fail("append-only migration history mismatch")

print("PASS: v0.196 constructs the exact U(3,2)/Pati-Salam Standard Model and its post-Higgs q stabilizer, while preserving J selection and radial-varpi action ownership as open burdens.")
