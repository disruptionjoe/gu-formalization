#!/usr/bin/env python3
"""Independent baseline and hostile controls for K644."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k644-k500-operator-block-lower-certificate.json"


def load_solver():
    path = Path(__file__).with_name("k644_k500_operator_block_lower_certificate.py")
    spec = importlib.util.spec_from_file_location("k644_probe_solver", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


SOLVER = load_solver()


def failures(data: dict) -> list[str]:
    bad: list[str] = []
    theorem = data.get("operator_block_theorem", {})
    composition = data.get("sector_to_global_composition", {})
    controls = data.get("exact_controls", {})
    native = data.get("native_interface_status", {})
    decision = data.get("decision", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        bad.append("routing")
    if theorem.get("sharp_comparison_floor") != "m_n>=lambda_min(C_n)" or "d_i,n" not in str(theorem.get("comparison_matrix", "")):
        bad.append("comparison")
    if "y^T C_n y" not in str(theorem.get("form_domination", "")) or "g_n" not in str(theorem.get("cheap_certificate", "")):
        bad.append("domination")
    for key in ("no_bounded_diagonal_operator_requirement", "off_diagonal_hilbert_bound_is_sufficient_not_necessary", "failed_row_sum_is_not_a_negative_spectrum_proof"):
        if theorem.get(key) is not True:
            bad.append(f"theorem:{key}")
    if composition.get("global_output") != "m=inf_n m_n, with a separately proved uniform tail beyond any finite prefix":
        bad.append("global")
    if composition.get("K642_base_floor") != "min(1/2,m-1/128)" or composition.get("K642_controlled_floor") != "min(1/2-alpha,m-delta-1/128)":
        bad.append("K642")
    if controls.get("all_controls_pass") is not True or controls.get("controls_are_synthetic_not_native") is not True:
        bad.append("controls")
    if not controls.get("rows") or any(row.get("all_test_slacks_nonnegative") is not True for row in controls["rows"]):
        bad.append("slacks")
    required_false = ("actual_K139_K168_common_domain_identity_proved", "actual_diagonal_sector_floors_identified", "actual_off_diagonal_sector_bounds_identified", "actual_uniform_tail_lower_identified", "native_global_m_identified", "native_remainder_alpha_delta_identified", "native_complete_sector_floor_emitted", "K473_released", "native_K152_interval_emitted")
    if any(native.get(key) is not False for key in required_false):
        bad.append("native_ceiling")
    if decision.get("K642_native_m_obligation_reduced_to_explicit_sector_block_data") is not True or decision.get("finite_synthetic_controls_are_native_inputs") is not False:
        bad.append("decision")
    if data.get("source_and_ledger_effect") != "none":
        bad.append("ledger")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("lambda_min", "uniform sector infimum", "remain missing", "no native complete-sector floor"):
        if token not in ceiling:
            bad.append(f"ceiling:{token}")
    return bad


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    fresh = SOLVER.build()
    theorem = data["operator_block_theorem"]
    composition = data["sector_to_global_composition"]
    controls = data["exact_controls"]
    native = data["native_interface_status"]
    rows = controls["rows"]
    return [
        ("fresh theorem matches", fresh["operator_block_theorem"] == theorem),
        ("fresh composition matches", fresh["sector_to_global_composition"] == composition),
        ("six sector channels", data["gu_typed_objects"]["sector_carrier"] == "H_b,n=direct_sum_(i=1)^6 H_n"),
        ("closed diagonal hypothesis", "closed" in theorem["hypotheses"]),
        ("comparison matrix", "d_i,n" in theorem["comparison_matrix"] and "-a_ij,n" in theorem["comparison_matrix"]),
        ("form domination", "y^T C_n y" in theorem["form_domination"]),
        ("least eigenvalue floor", theorem["sharp_comparison_floor"] == "m_n>=lambda_min(C_n)"),
        ("row floor", "g_n=min_i" in theorem["row_sum_floor"]),
        ("cheap certificate", theorem["cheap_certificate"] == "b_n>=g_n I on H_b,n"),
        ("closedness", "preserves closedness" in theorem["closedness"]),
        ("unbounded diagonals allowed", theorem["no_bounded_diagonal_operator_requirement"] is True),
        ("sufficient not necessary", theorem["off_diagonal_hilbert_bound_is_sufficient_not_necessary"] is True),
        ("failed row not negative proof", theorem["failed_row_sum_is_not_a_negative_spectrum_proof"] is True),
        ("sector inputs", "fifteen" in composition["sector_inputs"]),
        ("sector output", "lambda_min" in composition["sector_output"]),
        ("uniform global output", "uniform tail" in composition["global_output"]),
        ("K642 base composition", composition["K642_base_floor"] == "min(1/2,m-1/128)"),
        ("K642 remainder composition", composition["K642_controlled_floor"] == "min(1/2-alpha,m-delta-1/128)"),
        ("one sector falsifier", "reject" in composition["one_sector_falsifier"]),
        ("certificate failure scoped", "does not prove" in composition["certificate_failure_boundary"]),
        ("four controls", len(rows) == 4),
        ("all exact slacks", all(row["all_test_slacks_nonnegative"] for row in rows)),
        ("positive row positive", SOLVER.q(rows[0]["row_sum_lower"]) > 0),
        ("negative row retained", SOLVER.q(rows[1]["row_sum_lower"]) < 0),
        ("large coupling exposed", SOLVER.q(rows[2]["row_sum_lower"]) < 0),
        ("synthetic marked", controls["controls_are_synthetic_not_native"] is True),
        ("certificate constructed", native["six_channel_operator_certificate_constructed"] is True),
        ("native m withheld", native["native_global_m_identified"] is False),
        ("native floor withheld", native["native_complete_sector_floor_emitted"] is False),
        ("ledger unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    updates = (
        ("wrong comparison", lambda d: d["operator_block_theorem"].__setitem__("comparison_matrix", "identity")),
        ("wrong sharp floor", lambda d: d["operator_block_theorem"].__setitem__("sharp_comparison_floor", "m_n>=max diag")),
        ("erase domination", lambda d: d["operator_block_theorem"].__setitem__("form_domination", "unknown")),
        ("erase cheap certificate", lambda d: d["operator_block_theorem"].__setitem__("cheap_certificate", "unknown")),
        ("require bounded diagonal", lambda d: d["operator_block_theorem"].__setitem__("no_bounded_diagonal_operator_requirement", False)),
        ("claim necessity", lambda d: d["operator_block_theorem"].__setitem__("off_diagonal_hilbert_bound_is_sufficient_not_necessary", False)),
        ("claim negative spectrum", lambda d: d["operator_block_theorem"].__setitem__("failed_row_sum_is_not_a_negative_spectrum_proof", False)),
        ("erase uniform tail", lambda d: d["sector_to_global_composition"].__setitem__("global_output", "m=min prefix")),
        ("wrong base floor", lambda d: d["sector_to_global_composition"].__setitem__("K642_base_floor", "m")),
        ("wrong remainder floor", lambda d: d["sector_to_global_composition"].__setitem__("K642_controlled_floor", "m-delta")),
        ("fail controls", lambda d: d["exact_controls"].__setitem__("all_controls_pass", False)),
        ("claim native controls", lambda d: d["exact_controls"].__setitem__("controls_are_synthetic_not_native", False)),
        ("negative slack", lambda d: d["exact_controls"]["rows"][0].__setitem__("all_test_slacks_nonnegative", False)),
        ("invent identity", lambda d: d["native_interface_status"].__setitem__("actual_K139_K168_common_domain_identity_proved", True)),
        ("invent diagonals", lambda d: d["native_interface_status"].__setitem__("actual_diagonal_sector_floors_identified", True)),
        ("invent couplings", lambda d: d["native_interface_status"].__setitem__("actual_off_diagonal_sector_bounds_identified", True)),
        ("invent tail", lambda d: d["native_interface_status"].__setitem__("actual_uniform_tail_lower_identified", True)),
        ("invent m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("invent remainder", lambda d: d["native_interface_status"].__setitem__("native_remainder_alpha_delta_identified", True)),
        ("invent floor", lambda d: d["native_interface_status"].__setitem__("native_complete_sector_floor_emitted", True)),
        ("release K473", lambda d: d["native_interface_status"].__setitem__("K473_released", True)),
        ("release K152", lambda d: d["native_interface_status"].__setitem__("native_K152_interval_emitted", True)),
        ("deny reduction", lambda d: d["decision"].__setitem__("K642_native_m_obligation_reduced_to_explicit_sector_block_data", False)),
        ("promote controls", lambda d: d["decision"].__setitem__("finite_synthetic_controls_are_native_inputs", True)),
        ("move ledger", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    )
    caught = []
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(failures(mutant))))
    return caught


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    baseline = exact_checks(data)
    manifest_failures = failures(data)
    for name, ok in baseline:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    for failure in manifest_failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K644 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    if "--selftest" in sys.argv:
        hostile = hostile_checks(data)
        for name, ok in hostile:
            print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
        return 0 if all(ok for _, ok in baseline + hostile) and not manifest_failures else 1
    return 0 if all(ok for _, ok in baseline) and not manifest_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
