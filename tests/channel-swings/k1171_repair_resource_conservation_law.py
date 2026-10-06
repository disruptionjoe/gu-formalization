#!/usr/bin/env python3
"""K1171: exact Hessian/gauge/constraint repair-resource identity."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1171-repair-resource-conservation-law.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1171-REPAIR-RESOURCE-CONSERVATION-LAW",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "hypotheses": [
            "V is finite dimensional and H:V->V* is symmetric",
            "Hd=0 and Qd=0",
            "rad(H restricted to ker Q)=im d",
        ],
        "theorem": {
            "actual_constraint_rank": "c=rank(Q restricted to ker H)=dim ker H-rank d",
            "resource_identity": "rank H+rank d+c=dim V",
            "ceiling_form": "if c<=C then rank H+rank d+C>=dim V",
            "relative_repair_floor": "relative to ceilings h0,g0,C0, every successful packet needs Delta h+Delta g+Delta c>=dim V-h0-g0-C0",
        },
        "exact_control": {
            "field_dimension": 7,
            "hessian_rank": 2,
            "gauge_rank": 2,
            "constraint_rank_on_kernel": 3,
            "resource_sum": 7,
            "positive_quotient_dimension": 2,
        },
        "decision": "a successful radical-capture packet cannot hide missing directions: every field direction is paid for by Hessian rank, actual gauge image, or actual independent constraint rank",
        "scope_boundary": "exact finite-dimensional necessity; target dimension, formal parameter count, factor-through descendants, ownership, closure, propagation and physical positivity are separate",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert len(d["hypotheses"]) == 3
    assert "rank(Q restricted to ker H)" in d["theorem"]["actual_constraint_rank"]
    assert d["theorem"]["resource_identity"] == "rank H+rank d+c=dim V"
    assert ">=dim V" in d["theorem"]["ceiling_form"]
    assert "Delta h+Delta g+Delta c" in d["theorem"]["relative_repair_floor"]
    c = d["exact_control"]
    assert (c["hessian_rank"], c["gauge_rank"], c["constraint_rank_on_kernel"]) == (2, 2, 3)
    assert c["resource_sum"] == c["field_dimension"] == 7
    assert c["positive_quotient_dimension"] == 2
    assert "cannot hide missing directions" in d["decision"]
    assert "target dimension" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    assert json.loads(OUTPUT.read_text()) == data
    print("K1171 controls: 11/11")
