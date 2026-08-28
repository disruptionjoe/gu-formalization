#!/usr/bin/env python3
"""Fail-closed wiring audit for conditional-physics ledger v0.9."""

import json
from pathlib import Path

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]


def strict(relative: str):
    path = ROOT / relative

    def pairs(items):
        keys = [key for key, _ in items]
        assert len(keys) == len(set(keys)), f"duplicate key in {path}"
        return dict(items)

    return json.loads(path.read_text(), object_pairs_hook=pairs)


ledger = strict("lab/process/conditional-physics-ledger-v0.9.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
registry = strict("lab/process/k77-moving-observation-y14-domain-obstruction.json")
view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.9.md").read_text()
report = (ROOT / "explorations/conditional-build/k77-moving-observation-y14-domain-obstruction-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-k77-moving-observation-y14-domain-review.md").read_text()

rows = {row["id"]: row for row in ledger["rows"]}
active = [row for row in rows.values() if row.get("row_status") != "SUPERSEDED"]

assert ledger["schema_version"] == "0.9"
assert ledger["predecessor"].endswith("conditional-physics-ledger-v0.8.json")
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
assert "FIRST_JET_GERM_NO_LEAKAGE_EXACT" in rows["LT-GR2c"]["mapping_grade"]
assert "PHYSICAL_STRESS_AND_CONSTRAINED_DOMAIN_OPEN" in rows["LT-GR2c"]["mapping_grade"]
assert "PHYSICAL_UP_AND_BACK_STRESS_OPEN" in rows["LT-GR6"]["mapping_grade"]

assert reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.9.json"
)
assert registry["observation"]["section_germ_no_leakage"] is True
assert registry["global_shell"]["finite_jet_faithful"] is False
assert registry["ambient_domain"]["standard_lorentzian_globally_hyperbolic_route"] == "SHARPLY_OBSTRUCTED"
assert registry["null_physics"]["predecessor_physical_quotient_dimension"] == 2
assert registry["observed_equations"]["up_and_back_stress_map"] == "OPEN_SOURCE_DIRECTED"
assert registry["residue"]["P1_P2_P3"] == "UNCHANGED_UNUSED"

assert "SOURCE-CORRECTS" in report
assert "summary outruns artifact" in review
assert "superseded or mistyped object" in review
assert "82/82" in view and "section-germ" in view

print("PASS: v0.9 wires exact first-jet section-germ observation, the sharp standard K77 ambient-Cauchy obstruction, conditional observed curvature/distortion equations, and the open constrained-domain/up-and-back-stress gate")
