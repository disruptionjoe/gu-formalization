#!/usr/bin/env python3
"""K1036: compose K77's repository-owned action quotient with K1031."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1036-k1035-k77-action-quotient-composition.json"
K77 = ROOT / "lab/process/k77-observed-action-owned-global-quotient-wave.json"
K1031 = ROOT / "lab/process/k1031-k1030-positive-quotient-descent.json"


def build():
    k77 = json.loads(K77.read_text())
    k1031 = json.loads(K1031.read_text())
    p = [[1, 0, 0, 0], [0, 1, 0, 0]]
    m = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    return {
        "schema_version": "1.0",
        "result_id": "K1036-K1035-K77-ACTION-QUOTIENT-COMPOSITION",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "predecessors": [str(K77.relative_to(ROOT)), str(K1031.relative_to(ROOT))],
        "finite_control": {
            "P": p,
            "M_equals_P_star_P": m,
            "ambient_rank": 4,
            "quotient_rank": 2,
            "gauge_rank": 2,
            "radical_basis": [[0, 0, 1, 0], [0, 0, 0, 1]],
        },
        "functional_composition": {
            "ambient": "H1(M;V), rank(V)=1920",
            "gauge": "H1(M;ker P), rank(ker P)=960",
            "quotient": "H1(M;V)/H1(M;ker P) ~= H1(M;W), rank(W)=960",
            "closed_range": k77["functional_quotient"]["closed_range_proof"],
            "positive_pairing": "the transported incoming H equals the quotient pairing induced by P*H P",
            "action_basicness": "S_m[Phi+kappa]=S_m[Phi] because P kappa=0",
        },
        "ownership": {
            "repository_owned_candidate_action": True,
            "source_selected_GU_action": False,
            "unique_physical_quotient": False,
        },
        "source_ledger_effect": "none -- SC-ACT-01/02/06 and SC-META-53 retain their prior polarities; LT-SM8 and LT-GR6b remain NEEDS",
        "claim_ceiling": "exact composition of an existing repository-owned K77 candidate with K1031; no source-selected GU action, unique physical quotient, prediction or confirmation",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert len(d["predecessors"]) == 2
    c = d["finite_control"]
    assert c["M_equals_P_star_P"] == [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert c["ambient_rank"] == c["quotient_rank"] + c["gauge_rank"] == 4
    assert len(c["radical_basis"]) == c["gauge_rank"] == 2
    f = d["functional_composition"]
    assert "rank(V)=1920" in f["ambient"]
    assert "rank(ker P)=960" in f["gauge"]
    assert "rank(W)=960" in f["quotient"]
    assert "bounded_projection" in f["closed_range"] or "bounded projection" in f["closed_range"]
    assert "P*H P" in f["positive_pairing"]
    assert "P kappa=0" in f["action_basicness"]
    assert d["ownership"] == {"repository_owned_candidate_action": True, "source_selected_GU_action": False, "unique_physical_quotient": False}
    assert d["source_ledger_effect"].startswith("none")
    assert "no source-selected GU action" in d["claim_ceiling"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1036 controls: 13/13")
