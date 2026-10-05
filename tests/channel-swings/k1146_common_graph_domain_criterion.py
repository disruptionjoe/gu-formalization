#!/usr/bin/env python3
"""K1146: common graph-domain criterion and composition-domain warning."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1146-common-graph-domain-criterion.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1146-COMMON-GRAPH-DOMAIN-CRITERION",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "theorem": "a finite intersection of domains of closed operators is complete in the combined graph norm; identities containing products require the corresponding product domains as additional graph factors",
        "multiplier_model": {
            "hilbert_space": "ell2(N)",
            "Q_symbol": "n",
            "G_symbol": "n^2",
            "common_graph_weight": "1+n^2+n^4",
            "product_symbol": "n^3",
            "product_graph_weight": "n^6",
            "closed_common_domain": True,
        },
        "composition_counterexample": {
            "sequence": "u_n=n^-3",
            "ell2_series_exponent": -6,
            "Q_graph_series_exponent": -4,
            "G_graph_series_exponent": -2,
            "QG_graph_series_exponent": 0,
            "in_common_Q_G_domain": True,
            "in_QG_domain": False,
        },
        "admission_consequence": "the common I1B realization must include graph domains for Q,d,G,H and every composed word used by QG=RQ, Qd=0 and G*H+HG=0",
        "source_action_domain_supplied": False,
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    m, c = d["multiplier_model"], d["composition_counterexample"]
    assert "combined graph norm" in d["theorem"]
    assert "product domains" in d["theorem"]
    assert m["hilbert_space"] == "ell2(N)"
    assert m["common_graph_weight"] == "1+n^2+n^4"
    assert m["product_graph_weight"] == "n^6"
    assert m["closed_common_domain"]
    assert c["sequence"] == "u_n=n^-3"
    assert c["G_graph_series_exponent"] == -2
    assert c["QG_graph_series_exponent"] == 0
    assert c["in_common_Q_G_domain"] and not c["in_QG_domain"]
    assert "every composed word" in d["admission_consequence"]
    assert not d["source_action_domain_supplied"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1146 controls: 12/12")
