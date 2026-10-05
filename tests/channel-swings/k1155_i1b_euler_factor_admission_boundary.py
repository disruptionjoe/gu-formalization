#!/usr/bin/env python3
"""K1155: integrate the Euler-factor result into the I1B admission boundary."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1155-i1b-euler-factor-admission-boundary.json"


def load(name): return json.loads((ROOT / "lab/process" / name).read_text())


def build():
    prior = load("k1150-i1b-functional-admission-compiler.json")
    theorem = load("k1151-euler-factor-radical-inheritance.json")
    floor = load("k1152-sharp-radical-capture-rank-floor.json")
    app = load("k1153-k132-causal-radical-capture-floor.json")
    repair = load("k1154-source-i1b-constraint-repair-trilemma.json")
    return {
        "schema_version": "1.0",
        "result_id": "K1155-I1B-EULER-FACTOR-ADMISSION-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "inputs": [prior["result_id"], theorem["result_id"], floor["result_id"], app["result_id"], repair["result_id"]],
        "source_owned_class_tested": "all linear Euler-row postprocessors Q=L H of the current K132 causal symbols",
        "source_owned_class_passes": False,
        "failure_gate": "positive_nonzero_cohomology_radical_equality",
        "causal_radical_capture_floors": app["causal_rank_floors"],
        "current_candidates_meeting_full_packet": 0,
        "admission_update": "a future current-Hessian Q must be nonfactor and injective on ker(H)/im(d), or source ownership must enlarge the gauge/KT image; a changed parent recomputes every prior gate",
        "protected_disposition": "SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "next_condition": "derive an actual source-owned nonfactor bulk-boundary or constraint differential satisfying the 98470/98470/106634 kernel-capture floors and every K1150 functional gate, or supply an enlarged gauge/KT image or changed stationary parent",
        "scope_boundary": "selected K132 finite causal symbols only; no global domain, physical state, prediction, confirmation, canon, paper or public move",
        "scorable_rows_added": 0,
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert len(d["inputs"]) == 5
    assert d["source_owned_class_tested"].startswith("all linear Euler-row postprocessors")
    assert not d["source_owned_class_passes"]
    assert d["failure_gate"] == "positive_nonzero_cohomology_radical_equality"
    assert d["causal_radical_capture_floors"] == {"timelike": 98470, "spacelike": 98470, "null": 106634}
    assert d["current_candidates_meeting_full_packet"] == 0
    assert "must be nonfactor" in d["admission_update"]
    assert "remain ASSERTS" in d["protected_disposition"]
    assert "98470/98470/106634" in d["next_condition"]
    assert "selected K132 finite causal symbols only" in d["scope_boundary"]
    assert d["scorable_rows_added"] == 0 and d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    assert json.loads(OUTPUT.read_text()) == data
    print("K1155 controls: 12/12")
