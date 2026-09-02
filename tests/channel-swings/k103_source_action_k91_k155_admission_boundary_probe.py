#!/usr/bin/env python3
"""K103 typed source-action admission boundary against K91 and K155."""

from __future__ import annotations

from collections import Counter
from copy import deepcopy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/k103-source-action-k91-k155-admission-boundary-wave.json"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(path: Path) -> dict:
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=hook)


def valid(data: dict) -> bool:
    source = data.get("inputs", {}).get("source_corpus", {})
    k91 = data.get("k91_admission", {})
    k155 = data.get("k155_admission", {})
    result = data.get("result", {})
    if source.get("real_form") != "Cl(9,5)=M(64,H)" or source.get("action_status") != "no_coefficient_complete_action":
        return False
    if set(k91) != {
        "real_action_to_split_complex_map", "gauge_map_intertwining",
        "quotient_exactness_bridge", "closed_generator_domain_bridge",
        "invariant_core_bridge", "causal_green_boundary_bridge", "result",
    }:
        return False
    if any(k91[key] != "absent" for key in k91 if key != "result") or k91.get("result") != "not_admitted":
        return False
    if k155.get("fixture_recomputation_licensed") is not False:
        return False
    for key in (
        "real_form_action_bridge", "source_selected_shiab_coefficients",
        "same_order_action_owned_correction", "common_field_and_hessian_identification",
        "common_domain_and_green_identification",
    ):
        if k155.get(key) != "absent":
            return False
    if k155.get("result") != "not_admitted_before_fixture":
        return False
    return (
        data.get("inputs", {}).get("k155", {}).get("preserved_leakage_rank") == 1
        and result.get("k91_closed") is False
        and result.get("k155_tested_by_source_corpus") is False
        and result.get("k155_branch_verdict_changed") is False
    )


data = strict(REGISTRY)
k91 = strict(ROOT / "lab/process/k102-observed-k91-common-domain-instrument-descent-wave.json")
k155 = strict(ROOT / "lab/process/selected-k155-null-fivefold-third-lower.json")
custody = strict(ROOT / "lab/process/k103-absorbed-source-action-custody-qualification-wave.json")

print("A. POSITIVE CONTROLS")
check("positive", "custody packet has no coefficient-complete action", custody["result"]["qualified"] is False)
check(
    "positive",
    "K91 result owns common-domain reduced instrument descent",
    k91["status"] == "complete_repository_control"
    and k91["common_domain"]["domain_preserved"] is True
    and k91["descent"]["representative_independent"] is True,
)
check("positive", "K155 exact fixture has rank-one rotated leakage", k155["exact_result"]["rotated_metric_radical_leakage_rank"] == 1)
check("positive", "K155 flat control removes leakage", k155["exact_result"]["flat_control_rotated_radical_leakage_rank"] == 0)

print("\nB. TYPED ADMISSION")
check("typing", "source corpus and K155 real forms remain distinct", data["inputs"]["source_corpus"]["real_form"] != data["inputs"]["k155"]["real_form"])
check("typing", "K91 remains a repository functional control", data["inputs"]["k91"]["owner"] == "repository_functional_control")
for key, value in data["k91_admission"].items():
    if key != "result":
        check("k91", f"{key} is absent", value == "absent")
check("k91", "source corpus is not admitted to K91", data["k91_admission"]["result"] == "not_admitted")
for key in (
    "real_form_action_bridge", "source_selected_shiab_coefficients",
    "same_order_action_owned_correction", "common_field_and_hessian_identification",
    "common_domain_and_green_identification",
):
    check("k155", f"{key} is absent", data["k155_admission"][key] == "absent")
check("k155", "fixture recomputation is not licensed", data["k155_admission"]["fixture_recomputation_licensed"] is False)
check("k155", "K155 verdict remains unchanged", data["result"]["k155_branch_verdict_changed"] is False)
check("result", "complete invariant set passes", valid(data))

print("\nC. HOSTILE SELFTEST")
mutations = []
for section, key, value in (
    ("k91_admission", "real_action_to_split_complex_map", "qualified"),
    ("k91_admission", "gauge_map_intertwining", "qualified"),
    ("k91_admission", "quotient_exactness_bridge", "qualified"),
    ("k91_admission", "closed_generator_domain_bridge", "qualified"),
    ("k91_admission", "invariant_core_bridge", "qualified"),
    ("k91_admission", "causal_green_boundary_bridge", "qualified"),
    ("k91_admission", "result", "admitted"),
    ("k155_admission", "real_form_action_bridge", "qualified"),
    ("k155_admission", "source_selected_shiab_coefficients", "qualified"),
    ("k155_admission", "same_order_action_owned_correction", "qualified"),
    ("k155_admission", "common_field_and_hessian_identification", "qualified"),
    ("k155_admission", "common_domain_and_green_identification", "qualified"),
    ("k155_admission", "fixture_recomputation_licensed", True),
    ("result", "k91_closed", True),
    ("result", "k155_tested_by_source_corpus", True),
    ("result", "k155_branch_verdict_changed", True),
):
    bad = deepcopy(data)
    bad[section][key] = value
    mutations.append(bad)
bad = deepcopy(data)
bad["inputs"]["source_corpus"]["real_form"] = "Cl(7,7)"
mutations.append(bad)
bad = deepcopy(data)
bad["inputs"]["k155"]["preserved_leakage_rank"] = 0
mutations.append(bad)
for index, bad in enumerate(mutations, 1):
    check("hostile", f"mutation {index} is rejected", not valid(bad))

print(f"\nSUMMARY {sum(COUNTS.values()) - len(FAILURES)}/{sum(COUNTS.values())} passed; hostile {COUNTS['hostile']}/{COUNTS['hostile']} caught")
if FAILURES:
    raise SystemExit(1)
