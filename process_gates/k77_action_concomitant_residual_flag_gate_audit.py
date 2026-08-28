#!/usr/bin/env python3
"""Fail-closed pointer and scope audit for ledger v0.190."""

from __future__ import annotations

import json
from pathlib import Path

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.190.json"
RESULT = ROOT / "lab/process/selected-k77-action-concomitant-residual-flag-gate.json"
PROBE = ROOT / "tests/channel-swings/selected_k77_action_concomitant_residual_flag_gate_probe.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


ledger = load(LEDGER)
result = load(RESULT)
assert ledger["schema_version"] == "0.190"
assert ledger["predecessor"].endswith("v0.189.json")
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32,
    "DIFFERS": 19,
    "NEEDS": 26,
    "OVER_DETERMINED": 5,
}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["function_valued_at_least"] == 19
assert ledger["residue"]["open_discrete_forks"] == 9
assert ledger["residue"]["quotients_ranked"] == 5
assert ledger["updated_by"] == result["run_id"]
assert ledger["frontier_delta"] == result["frontier_delta"]
assert ledger["source_return"] == result["source_return"]
assert result["target_claim"] == "NONE-NOT-A-KILL"
assert result["result"]["lorentz_commutant_dimension"] == 2
assert result["result"]["possible_gapped_projector_ranks"] == [0, 1, 9, 10]
assert result["result"]["rank_four_available"] is False
assert result["result"]["all_current_commutators_zero"] is True
assert result["result"]["nonhomogeneous_successor_open"] is True
assert "constant_section_totally_geodesic_shortcut_rejected" in result["controls"]
contract = load(ROOT / "lab/methods/research-evidence-contract-v1.0.json")
assert reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.190.json"
)

rows = {row["id"]: row for row in ledger["rows"]}
assert sum(edge.get("to_version") == "0.190" for edge in ledger["migrations"]) == 12
assert sum(edge.get("to_version") == "0.190" for edge in ledger["migration_history"]) == 12
for row_id in result["ledger_rows"]:
    assert row_id in rows
    evidence = " ".join(rows[row_id].get("evidence", [])) if isinstance(rows[row_id].get("evidence"), list) else str(rows[row_id].get("evidence", ""))
    assert "selected-k77-action-concomitant-residual-flag-gate-2026-08-12.md" in evidence

probe_text = PROBE.read_text(encoding="utf-8")
assert "target_claim: NONE-NOT-A-KILL" in probe_text
assert "not totally geodesic" in probe_text
assert "SOURCE_RETURN=SOURCE-CONFIRMS_GEOMETRIC_REDUCTION" in probe_text

print("PASS v0.190 action-concomitant residual-flag audit")
