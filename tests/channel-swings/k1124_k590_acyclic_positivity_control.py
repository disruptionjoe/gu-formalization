#!/usr/bin/env python3
"""K1124: acyclic finite KT exactness is a vacuous positivity control."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1124-k590-acyclic-positivity-control.json"


def build():
    k590 = json.loads((ROOT / "lab/process/k590-k77-corrected-carrier-completion-squares.json").read_text())
    homology = k590["factorized_completion"]["homology_dimensions"]
    return {
        "schema_version": "1.0",
        "result_id": "K1124-K590-ACYCLIC-POSITIVITY-CONTROL",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "control_input": "K590 factorized corrected-carrier complex",
        "degree_dimensions": k590["factorized_completion"]["degree_dimensions"],
        "homology_dimensions": homology,
        "acyclic": homology == [0, 0, 0],
        "positivity_on_zero_cohomology": "vacuously true for every descended form",
        "supplies_nontrivial_physical_state_space": False,
        "carrier_transfer_to_K128_K129": False,
        "reason": "K590 is a distinct K77 factorized finite homogeneous-orbit complex; zero cohomology carries no nonzero state, effect or observable",
        "scope_boundary": "typed independent control only; it neither solves nor obstructs every functional BV/BFV completion of I1B",
    }


def validate(d):
    assert d["control_input"] == "K590 factorized corrected-carrier complex"
    assert d["degree_dimensions"] == [10752, 46592, 35840]
    assert d["homology_dimensions"] == [0, 0, 0]
    assert d["acyclic"] is True
    assert d["positivity_on_zero_cohomology"] == "vacuously true for every descended form"
    assert d["supplies_nontrivial_physical_state_space"] is False
    assert d["carrier_transfer_to_K128_K129"] is False
    assert "no nonzero state" in d["reason"]
    assert "neither solves nor obstructs every" in d["scope_boundary"]


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1124 controls: 9/9")
