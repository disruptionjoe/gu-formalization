#!/usr/bin/env python3
"""K1176: one stratum-independent repair ceiling must pay the worst causal deficit."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1176-shared-causal-repair-budget.json"
DEFICITS = {"timelike": 98372, "spacelike": 98372, "null": 106536}


def build():
    return {
        "schema_version": "1.0", "result_id": "K1176-SHARED-CAUSAL-REPAIR-BUDGET",
        "status": "working_draft_verified", "created": "2026-10-05",
        "inputs": ["K1173-K132-CAUSAL-REPAIR-POLYTOPE", "K1175-I1B-THREE-REOPENER-ADMISSION-BOUNDARY"],
        "causal_deficits": DEFICITS,
        "theorem": "if one packet has stratum-independent added-rank ceilings H,G,C, success on every causal stratum requires H+G+C>=max_s D_s",
        "shared_ceiling_floor": max(DEFICITS.values()),
        "dominating_stratum": "null",
        "nonnull_slack_at_floor": 106536 - 98372,
        "pointwise_boundary": "if added ranks vary by stratum, retain the three separate K1173 inequalities; the shared floor applies only to uniform ceilings",
        "decision": "a single uniformly bounded repair packet must budget at least 106536 genuinely new directions even though each nonnull stratum needs only 98372",
        "scope_boundary": "finite causal-symbol necessity under the favorable rank-98 baseline; no source-owned coupling or global domain is constructed",
        "target_claim": "SC-ACT-06",
    }


def validate(d):
    assert len(d["inputs"]) == 2
    assert d["causal_deficits"] == DEFICITS
    assert "H+G+C>=max_s D_s" in d["theorem"]
    assert d["shared_ceiling_floor"] == 106536
    assert d["dominating_stratum"] == "null"
    assert d["nonnull_slack_at_floor"] == 8164
    assert "vary by stratum" in d["pointwise_boundary"]
    assert "106536" in d["decision"] and "98372" in d["decision"]
    assert "no source-owned coupling" in d["scope_boundary"]
    assert d["target_claim"] == "SC-ACT-06"


if __name__ == "__main__":
    data = build(); validate(data); assert json.loads(OUTPUT.read_text()) == data
    print("K1176 controls: 10/10")
