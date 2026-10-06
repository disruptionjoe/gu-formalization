#!/usr/bin/env python3
"""K1178: freeze optimistic ceilings for the strongest serialized native responses."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1178-native-response-ceiling-ledger.json"
DEFICITS = {"timelike": 98372, "spacelike": 98372, "null": 106536}


def candidate(cid, ceiling, kind, evidence):
    return {
        "candidate_id": cid, "optimistic_independent_rank_ceiling": ceiling,
        "ceiling_kind": kind, "evidence": evidence,
        "k132_transport": "unowned", "k132_kernel_complement_rank": "unmeasured",
        "residual_if_full_independent_transport": {s: max(0, d-ceiling) for s, d in DEFICITS.items()},
    }


def build():
    rows = [
        candidate("labelled-null-conormal-principal-symbol", 650, "measured principal-symbol rank", "selected-k77-observation-jet-euler-preboundary-sufficiency"),
        candidate("selected-spin-minimal-local-tangent", 915, "carrier-dimension ceiling", "conditional-physics-ledger-v0.263 nonnull_koszul_gcr_directive"),
        candidate("full-raw-upsilon-response", 1470, "measured response rank", "selected-k77-observation-jet-euler-preboundary-sufficiency"),
        candidate("source-native-y14-low-grade-tangent", 1571, "carrier-dimension ceiling", "conditional-physics-ledger-v0.263 moving source directives"),
    ]
    return {
        "schema_version": "1.0", "result_id": "K1178-NATIVE-RESPONSE-CEILING-LEDGER",
        "status": "working_draft_verified", "created": "2026-10-05",
        "inputs": ["K1176-SHARED-CAUSAL-REPAIR-BUDGET", "conditional-physics-ledger-v0.263"],
        "baseline_deficits": DEFICITS, "candidates": rows,
        "strongest_single_ceiling": 1571,
        "strongest_single_residual": {"timelike": 96801, "spacelike": 96801, "null": 104965},
        "decision": "even the strongest single serialized native ceiling misses the favorable K132 repair floor by at least 96801/96801/104965 directions",
        "ownership_firewall": "the optimistic grant is not a K132 coupling: target/carrier size is not actual rank on ker H, and actual complement rank may be smaller or zero",
        "protected_disposition": "SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "target_claim": "SC-ACT-06",
    }


def validate(d):
    assert len(d["inputs"]) == 2
    assert d["baseline_deficits"] == DEFICITS
    assert [x["optimistic_independent_rank_ceiling"] for x in d["candidates"]] == [650, 915, 1470, 1571]
    assert [x["ceiling_kind"] for x in d["candidates"]].count("measured response rank") == 1
    assert all(x["k132_transport"] == "unowned" for x in d["candidates"])
    assert all(x["k132_kernel_complement_rank"] == "unmeasured" for x in d["candidates"])
    assert d["candidates"][0]["residual_if_full_independent_transport"]["null"] == 105886
    assert d["strongest_single_ceiling"] == 1571
    assert d["strongest_single_residual"] == {"timelike": 96801, "spacelike": 96801, "null": 104965}
    assert "96801/96801/104965" in d["decision"]
    assert "not a K132 coupling" in d["ownership_firewall"]
    assert d["protected_disposition"].startswith("SC-ACT-01/02/06 remain ASSERTS")
    assert d["target_claim"] == "SC-ACT-06"


if __name__ == "__main__":
    data = build(); validate(data); assert json.loads(OUTPUT.read_text()) == data
    print("K1178 controls: 12/12")
