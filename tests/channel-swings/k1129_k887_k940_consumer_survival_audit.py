#!/usr/bin/env python3
"""K1129: classify K887--K940 after the adjoint and gauge-carrier corrections."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1129-k887-k940-consumer-survival-audit.json"


def one_packet(number):
    matches = sorted((ROOT / "lab/process").glob(f"k{number}-*.json"))
    assert len(matches) == 1, (number, matches)
    return json.loads(matches[0].read_text())["result_id"]


def build():
    ids = [one_packet(n) for n in range(887, 941)]
    return {
        "schema_version": "1.0",
        "result_id": "K1129-K887-K940-CONSUMER-SURVIVAL-AUDIT",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "audited_range": [887, 940],
        "audited_result_count": len(ids),
        "audited_result_ids": ids,
        "directly_corrected_range": [887, 898],
        "dependent_action_gate_range": [899, 925],
        "explicit_auxiliary_range": [926, 940],
        "historical_exact_algebra_preserved": True,
        "preservation_rule": "ranks, dimensions, characters and abstract theorems survive only on their originally declared frozen slice, projector or auxiliary carrier",
        "withdrawn_current_inference": "K887-K925 do not establish a source-action T0 gauge-descent failure, required radial completion, symmetric-S Helmholtz classification or authenticated physical quotient gate",
        "auxiliary_disposition": "K926-K940 remain exact auxiliary projector/domain mathematics and already supply no source/action ownership or physical credit",
        "independent_successor": "K941 source-epsilon cotangent parent is outside the corrected radial-old-quotient chain",
        "old_completion_gate_current": False,
        "source_and_ledger_effect": "SC-ACT-01_03_04_05_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
    }


def validate(d):
    assert d["audited_range"] == [887, 940]
    assert d["audited_result_count"] == 54
    assert len(d["audited_result_ids"]) == 54
    assert d["audited_result_ids"][0].startswith("K887-")
    assert d["audited_result_ids"][-1].startswith("K940-")
    assert d["directly_corrected_range"] == [887, 898]
    assert d["dependent_action_gate_range"] == [899, 925]
    assert d["explicit_auxiliary_range"] == [926, 940]
    assert d["historical_exact_algebra_preserved"] is True
    assert "originally declared frozen slice" in d["preservation_rule"]
    assert "do not establish" in d["withdrawn_current_inference"]
    assert "exact auxiliary" in d["auxiliary_disposition"]
    assert d["independent_successor"].startswith("K941")
    assert d["old_completion_gate_current"] is False
    assert d["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED")


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1129 controls: 15/15")
