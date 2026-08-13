#!/usr/bin/env python3
"""Fail-closed wiring audit for conditional-physics ledger v0.8."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def strict(relative: str):
    path = ROOT / relative

    def pairs(items):
        keys = [key for key, _ in items]
        assert len(keys) == len(set(keys)), f"duplicate key in {path}"
        return dict(items)

    return json.loads(path.read_text(), object_pairs_hook=pairs)


ledger = strict("lab/process/conditional-physics-ledger-v0.8.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
registry = strict("lab/process/k77-global-even-bv-null-green-domain.json")
lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text()
view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.8.md").read_text()
report = (ROOT / "explorations/conditional-build/k77-global-even-bv-null-green-domain-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-k77-global-even-bv-null-green-review.md").read_text()

rows = {row["id"]: row for row in ledger["rows"]}
active = [row for row in rows.values() if row.get("row_status") != "SUPERSEDED"]
directive = contract["active_scientific_directives"][0]

assert ledger["schema_version"] == "0.8"
assert ledger["predecessor"].endswith("conditional-physics-ledger-v0.7.json")
assert len(active) == 82 and len(rows) == 83
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6
}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["open_discrete_forks"] == 10
assert ledger["residue"]["open_fork_horn_product"] == 2304
assert ledger["residue"]["quotients_ranked"] == 2
assert rows["LT-GR2c"]["verdict"] == "NEEDS"
assert rows["LT-GR2c"]["reason_kind"] == "MISSING_CONSTRUCTION"
assert "FORMAL_MINIMAL_CME_COMPOSED" in rows["LT-GR2c"]["mapping_grade"]
assert "NULL_4_CONSTRAINT_4_GAUGE_2_PHYSICAL_EXACT" in rows["LT-GR2c"]["mapping_grade"]
assert "GLOBAL_Y14_DOMAIN_OBSERVATION_PHYSICS_OPEN" in rows["LT-GR2c"]["mapping_grade"]

assert contract["standing_ledger"]["ref"].endswith("v0.8.json")
assert contract["standing_ledger"]["human_ref"].endswith("v0.8.md")
assert "conditional-physics-ledger-v0.8.json" in lanes
assert directive["source_return"] == "SOURCE-SILENT"
assert directive["next_gate"] == registry["next_gate"]
assert registry["null_split"]["physical_quotient_dimension"] == 2
assert registry["green_domain"]["global_coupled_noncompact_y14_domain"] == "OPEN"
assert registry["normalization"]["prequotient_continuous_real_count"] == 84
assert registry["residue"]["P1_P2_P3"] == "UNCHANGED_UNUSED"

assert "SOURCE-SILENT" in report
assert "summary outruns the artifact" in review
assert "superseded or mistyped object" in review
assert "82/82" in view and "10 -> 6 -> 2" in view

print("PASS: v0.8 wires the formal homogeneous-gauge owner, exact null physical quotient, conditional flat-defect Green complex and 84-real prequotient count to the global Y14 observation/domain gate")
