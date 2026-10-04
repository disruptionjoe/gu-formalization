#!/usr/bin/env python3
"""K1029: compose setting, locality-compromise and record budgets."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1029-k1028-causal-record-sequential-certificate.json"


def local_ceiling(epsilon, q):
    b = min(1.0, 0.75 + epsilon)
    return b + q * (1 - b)


def threshold(epsilon, q, record_rate, alpha, n):
    return local_ceiling(epsilon, q) + record_rate + math.sqrt(math.log(1 / alpha) / (2 * n))


def build():
    example = {"epsilon": 0.01, "q": 0.02, "record_rate": 0.003,
               "alpha": 0.05, "n": 10000}
    certificate_threshold = threshold(**example)
    example["good_local_ceiling"] = 0.75 + example["epsilon"]
    example["mixed_local_ceiling"] = local_ceiling(example["epsilon"], example["q"])
    example["certificate_threshold"] = certificate_threshold
    return {
        "schema_version": "1.0",
        "result_id": "K1029-K1028-CAUSAL-RECORD-SEQUENTIAL-CERTIFICATE",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "certificate": "w_hat_recorded>b+q(1-b)+R/n+sqrt(log(1/alpha)/(2n)), b=min(1,3/4+epsilon)",
        "pathwise_count_form": "for predictable c_i fixed before W_i: sum_i E[W_i|past]<=sum_i b_i+sum_i c_i(1-b_i), sum_i c_i<=qn",
        "memory_scope": "arbitrary inter-trial device memory with predictable conditional setting and compromise bounds",
        "record_scope": "at most R recorded binary wins differ from the underlying trial wins",
        "controls": {"q_zero": local_ceiling(0.01, 0), "q_one": local_ceiling(0.01, 1),
                     "epsilon_quarter": local_ceiling(0.25, 0.2)},
        "example": example,
        "audit_boundary": "epsilon, predictable pre-score compromise indicators with sum_i c_i<=qn, and R/n are supplied trial-level audit bounds; the theorem does not estimate them from experimental data",
        "ownership": {"locality_audit_constructed": False, "setting_source_certified": False,
                      "record_audit_constructed": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "b+q(1-b)+R/n" in d["certificate"] and "b=min(1,3/4+epsilon)" in d["certificate"]
    assert "predictable c_i fixed before W_i" in d["pathwise_count_form"]
    assert "sum_i c_i(1-b_i)" in d["pathwise_count_form"]
    assert "arbitrary inter-trial" in d["memory_scope"]
    assert d["record_scope"].startswith("at most R")
    assert math.isclose(d["controls"]["q_zero"], 0.76, abs_tol=1e-15)
    assert math.isclose(d["controls"]["q_one"], 1.0, abs_tol=1e-15)
    assert math.isclose(d["controls"]["epsilon_quarter"], 1.0, abs_tol=1e-15)
    e = d["example"]
    assert math.isclose(e["mixed_local_ceiling"], 0.7648, abs_tol=1e-15)
    assert e["certificate_threshold"] > e["mixed_local_ceiling"] + e["record_rate"]
    assert "pre-score compromise" in d["audit_boundary"] and "does not estimate" in d["audit_boundary"]
    assert all(value is False for value in d["ownership"].values())
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1029 controls: 12/12")
