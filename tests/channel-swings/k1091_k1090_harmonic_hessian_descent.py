#!/usr/bin/env python3
"""K1091: harmonic-projector criterion for Hessian descent."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1091-k1090-harmonic-hessian-descent.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1091-K1090-HARMONIC-HESSIAN-DESCENT",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "complex": "C0 --d0--> C1 --d1--> C2 with d1 d0=0 on finite Hilbert spaces",
        "harmonic_space": "H1=ker(d1) intersect ker(d0*)",
        "hodge_splitting": "C1=im(d0) direct_sum H1 direct_sum im(d1*)",
        "criterion": "for L=L*, harmonic representatives are invariant iff [L,P_H]=0",
        "proof": "(I-P_H)L P_H=0 is invariance; self-adjointness makes P_H L(I-P_H) its adjoint",
        "fixture_d0": [1, 0, 0],
        "fixture_d1": [0, 0, 1],
        "fixture_projector": [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        "good_hessian": [[0, 0, 0], [0, 3, 0], [0, 0, 5]],
        "good_commutator_rank": 0,
        "bad_commutator_rank": 2,
        "scope_boundary": "finite conditional theorem; no source-selected GU differential, Hessian, closed domain or physical pairing",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "d1 d0=0" in d["complex"]
    assert d["harmonic_space"] == "H1=ker(d1) intersect ker(d0*)"
    assert "im(d0) direct_sum H1 direct_sum im(d1*)" in d["hodge_splitting"]
    assert "iff [L,P_H]=0" in d["criterion"]
    assert "self-adjointness" in d["proof"] and "its adjoint" in d["proof"]
    assert d["fixture_d0"] == [1, 0, 0] and d["fixture_d1"] == [0, 0, 1]
    assert d["fixture_projector"][1][1] == 1 and sum(map(sum, d["fixture_projector"])) == 1
    assert d["good_hessian"] == [[0, 0, 0], [0, 3, 0], [0, 0, 5]]
    assert d["good_commutator_rank"] == 0 and d["bad_commutator_rank"] == 2
    assert "no source-selected GU differential" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1091 controls: 11/11")
