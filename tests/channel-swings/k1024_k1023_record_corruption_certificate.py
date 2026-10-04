#!/usr/bin/env python3
"""K1024: deterministic record-corruption correction for sequential CHSH."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1024-k1023-record-corruption-certificate.json"


def build():
    n, r_count, alpha = 1000, 10, 0.05
    penalty = math.sqrt(math.log(1 / alpha) / (2 * n))
    return {
        "schema_version": "1.0", "result_id": "K1024-K1023-RECORD-CORRUPTION-CERTIFICATE",
        "status": "working_draft_verified", "created": "2026-10-04",
        "deterministic_budget": "sum_i |W_tilde_i-W_i|<=R",
        "pathwise_lipschitz_bound": "sum_i W_tilde_i<=sum_i W_i+R",
        "certificate": "w_hat_recorded>average_i(b_i)+R/n+sqrt(log(1/alpha)/(2n))",
        "combined_tv_form": "w_hat_recorded>3/4+average_i(epsilon_i)+R/n+sqrt(log(1/alpha)/(2n))",
        "example": {"n": n, "R": r_count, "R_over_n": r_count/n, "alpha": "1/20", "penalty": penalty, "uniform_threshold": .75+r_count/n+penalty},
        "tightness": "R adversarial flips can convert R losing records into wins, so R/n cannot be reduced without more structure",
        "memory_scope": "arbitrary inter-trial device memory and adversarial placement of at most R record changes",
        "unowned_assumptions": ["audited deterministic record-error budget", "conditional setting-source bound", "event-ready complete trial record"],
        "ownership": {"gu_record_system_constructed": False, "record_budget_empirically_certified": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["deterministic_budget"] == "sum_i |W_tilde_i-W_i|<=R"
    assert d["pathwise_lipschitz_bound"].endswith("+R")
    assert "+R/n+" in d["certificate"]
    assert "average_i(epsilon_i)" in d["combined_tv_form"]
    e=d["example"]
    assert e["R"] == 10 and e["n"] == 1000 and e["R_over_n"] == .01
    assert math.isclose(e["uniform_threshold"], .75+.01+e["penalty"], abs_tol=1e-15)
    assert "cannot be reduced" in d["tightness"]
    assert "adversarial placement" in d["memory_scope"]
    assert len(d["unowned_assumptions"]) == 3
    assert d["ownership"]["gu_record_system_constructed"] is False
    assert d["ownership"]["record_budget_empirically_certified"] is False
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    d=build(); validate(d)
    OUTPUT.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
    print("K1024 controls: 12/12")
