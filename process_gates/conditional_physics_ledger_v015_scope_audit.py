#!/usr/bin/env python3
"""Fail-closed wiring audit for conditional-physics ledger v0.15."""

from collections import Counter
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def strict(relative):
    path = ROOT / relative
    def pairs(items):
        keys = [key for key, _ in items]
        assert len(keys) == len(set(keys)), f"duplicate key in {path}"
        return dict(items)
    return json.loads(path.read_text(), object_pairs_hook=pairs)


v14p = ROOT / "lab/process/conditional-physics-ledger-v0.14.json"
v14 = strict("lab/process/conditional-physics-ledger-v0.14.json")
v15 = strict("lab/process/conditional-physics-ledger-v0.15.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
registry = strict("lab/process/first-interaction-krein-global-zero-mode.json")
lanes = (ROOT / "LANES.yaml").read_text()
view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.15.md").read_text()
report = (ROOT / "explorations/conditional-build/first-interaction-krein-and-global-zero-mode-horn-2026-08-05.md").read_text()
source = (ROOT / "lab/sources/first-interaction-krein-global-zero-mode-source-reinspection-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-first-interaction-krein-global-zero-mode-review.md").read_text()

rows14 = {row["id"]: row for row in v14["rows"]}
rows15 = {row["id"]: row for row in v15["rows"]}
active = [row for row in rows15.values() if row.get("row_status") != "SUPERSEDED"]
changed = {row_id for row_id in rows14 if rows14[row_id] != rows15[row_id]}
migrations = [item for item in v15["migrations"] if item.get("to_version") == "0.15"]
directive = contract["active_scientific_directives"][0]
expected = {"LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR3", "LT-GR5", "LT-SM8"}

assert hashlib.sha256(v14p.read_bytes()).hexdigest() == "6bee3c8a18597f29ac7c2a202333bc7b2bfdae18d63ba839d3580ff695d84939"
assert v15["schema_version"] == "0.15"
assert v15["predecessor"].endswith("conditional-physics-ledger-v0.14.json")
assert set(rows14) == set(rows15) and changed == expected
assert {item["row_id"] for item in migrations} == expected and len(migrations) == 6
assert len(active) == 82 and len(rows15) == 83
assert Counter(row["axis"] for row in active) == {
    "REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26
}
assert Counter(row["verdict"] for row in active) == {
    "SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6
}
assert v15["residue"]["continuous_real"] == 84
assert v15["residue"]["function_valued_at_least"] == 19
assert v15["residue"]["open_discrete_forks"] == 9
assert v15["residue"]["quotients_ranked"] == 4

assert "SCALAR_SIGN_EXTENSION_FAILS_FIRST_CUBIC" in rows15["LT-GR2b"]["mapping_grade"]
assert "GLOBAL_PROJECTOR_SCREENS_CONDITIONALLY" in rows15["LT-GR2c"]["mapping_grade"]
assert "OPEN_NOT_P2" in rows15["LT-GR2d"]["mapping_grade"]
assert "FIRST_CUBIC_SCALAR_SIGN_EXTENSION_KILLED" in rows15["LT-GR3"]["mapping_grade"]
assert "SUPER_IG_REBASED_TO_ALGEBRAIC_GLOBAL_DESCENT_NOT_ODD_ACTION" in rows15["LT-SM8"]["mapping_grade"]

assert registry["source_return"] == "SOURCE-CORRECTS"
assert registry["result"]["interacting_c_operator"] == "OPEN"
assert registry["constraint_surplus"]["remaining_freedom_after_domain_measure_supplied"] == 0
assert registry["external_datum"]["P2"] == "UNUSED_NOT_IDENTIFIED"

assert contract["standing_ledger"]["ref"].endswith("v0.15.json")
assert contract["standing_ledger"]["human_ref"].endswith("v0.15.md")
assert "conditional-physics-ledger-v0.15.json" in lanes
assert directive["source_return"] == "SOURCE-CORRECTS"
assert directive["next_gate"] == registry["next_gate"]
assert directive["resolved_by"].endswith("first-interaction-krein-and-global-zero-mode-horn-2026-08-05.md")
assert "Decisive return: `SOURCE-CORRECTS`" in source
assert "No multiplicative sign" in report
assert "Where does the summary outrun the artifact?" in review
assert "Where is rigor defending a superseded object?" in review
assert "PASS_AFTER_SIX_MATERIAL_SCOPE_CORRECTIONS" in review
assert "Ledger v0.15" in view and "33 SAME" in view and "9 open discrete forks" in view

print("PASS: v0.15 wires first-interaction free-parity failure, local zero-mode closure, conditional global screening and super-IG source correction without consuming P2")
