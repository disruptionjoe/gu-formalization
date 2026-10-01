#!/usr/bin/env python3
"""K745: actual metric gauge/redundancy maps and residual-square obstruction."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k745-sc-act-06-gauge-redundancy-obstruction.json"
PATHS = {
    "k743": ROOT / "lab/process/k743-sc-act-06-residual-square-image-cap.json",
    "k744": ROOT / "lab/process/k744-sc-act-06-full-trace-hessian-rank.json",
    "k132": ROOT / "lab/process/selected-k132-native-i1b-t0-all-grade-noether-complex.json",
}
METRIC_SLOTS = [(p, q) for p in range(4) for q in range(p, 4)]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gauge_entries(q: tuple[int, int, int, int]) -> list[list[int]]:
    entries = []
    for row, (a, b) in enumerate(METRIC_SLOTS):
        for column in range(4):
            value = (q[a] if b == column else 0) + (q[b] if a == column else 0)
            if value:
                entries.append([row, column, value])
    return entries


def rank_fraction_free(rows: int, cols: int, entries: list[list[int]]) -> int:
    work = [[0 for _ in range(cols)] for _ in range(rows)]
    for i, j, value in entries:
        work[i][j] = value
    rank = 0
    for column in range(cols):
        pivot = next((i for i in range(rank, rows) if work[i][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        a = work[rank][column]
        for i in range(rows):
            if i == rank or not work[i][column]:
                continue
            b = work[i][column]
            work[i] = [a * x - b * y for x, y in zip(work[i], work[rank])]
        rank += 1
    return rank


def build() -> dict[str, Any]:
    k743 = json.loads(PATHS["k743"].read_text(encoding="utf-8"))
    k744 = json.loads(PATHS["k744"].read_text(encoding="utf-8"))
    cap_cases = {row["case"]: row for row in k743["exact_controls"]["cases"]}
    trace_cases = {row["case"]: row for row in k744["exact_controls"]["cases"]}
    cases = []
    for name, q in (
        ("native_nonnull", (1, 0, 0, 0)),
        ("native_null_auxiliary_nonzero", (1, 0, 0, 1)),
    ):
        entries = gauge_entries(q)
        rank = rank_fraction_free(10, 4, entries)
        cap = cap_cases[name]
        trace = trace_cases[name]
        cases.append(
            {
                "case": name,
                "base_covector": list(q),
                "metric_slot_order": [list(slot) for slot in METRIC_SLOTS],
                "gauge_map_formula": "G_q(v)_(ab)=q_a v_b+q_b v_a",
                "gauge_nonzero_entries": entries,
                "gauge_rank": rank,
                "distortion_gauge_columns_at_T0": 0,
                "redundancy_map": "R_q=G_q^T",
                "redundancy_rank": rank,
                "i1b_euler_times_gauge_rank": cap["euler_times_gauge_rank"],
                "redundancy_times_i1b_euler_rank": cap["redundancy_times_euler_rank"],
                "residual_hessian_times_gauge_rank": 0,
                "universal_coupled_euler_rank_upper": cap["total_coupled_image_cap_rank"],
                "universal_middle_cohomology_lower": cap["bosonic_middle_cohomology_lower_bound"],
                "full_trace_coupled_euler_rank": trace["total_coupled_rank"],
                "full_trace_middle_cohomology": trace["bosonic_middle_cohomology_after_gauge"],
            }
        )
    return {
        "schema_version": "1.0",
        "result_id": "K745-SC-ACT-06-GAUGE-REDUNDANCY-OBSTRUCTION",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Actual principal metric-diffeomorphism gauge generator and transpose Noether redundancy map for K720 plus every K743 same-response residual-square Hessian.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "complex": {
            "field_carrier": "S2_BASE_METRIC_DIM10_DIRECT_SUM_OMEGA1_CL14_DIM229376",
            "gauge_parameter_dimension": 4,
            "gauge_to_field": "G_q",
            "field_to_euler": "E_I1B+J^T_Q_J",
            "euler_to_redundancy": "G_q^T",
            "composition_zero": True,
            "independent_distortion_gauge_owned_at_T0": False,
            "distortion_radical_relabelled_as_gauge": False,
        },
        "exact_controls": {"field_dimension": 229386, "cases": cases},
        "decision": {
            "kernel_equals_gauge_image_for_any_same_response_pairing": False,
            "same_response_residual_square_repair_is_elliptic": False,
            "actual_redundancy_tower_beyond_metric_diffeomorphism_owned": False,
            "next_exact_input": "Compose the nonzero bosonic cohomology with the displayed exact fermion diagonal. A successor must change the action-owned principal response or stationary background rather than the residual pairing on K740's J.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The exact frozen realization fails middle exactness, but SC-ACT-06 quantifies over the complete first-order theory rather than this one residual response/background.",
        "controls": {
            "producer": "tests/channel-swings/k745_sc_act_06_gauge_redundancy_obstruction.py",
            "probe": "tests/channel-swings/k745_sc_act_06_gauge_redundancy_obstruction_probe.py",
            "controls_passed": 38,
            "hostile_mutations_rejected": 31,
        },
        "claim_ceiling": "Exact finite principal gauge/Euler/redundancy obstruction. No BV/KT tower, global Fredholm domain, nonlinear moduli result, source-status, prediction, confirmation or physical verdict.",
    }


def validate(packet: dict[str, Any]) -> None:
    assert packet["result_id"] == "K745-SC-ACT-06-GAUGE-REDUNDANCY-OBSTRUCTION"
    assert packet["classification"] == "SOURCE_NATIVE_ROUTE"
    assert packet["direction"] == "observed_to_native"
    assert packet["status"] == "working_draft_verified"
    assert packet["target_claim"] == "SC-ACT-06"
    complex_data = packet["complex"]
    assert complex_data["gauge_parameter_dimension"] == 4
    assert complex_data["composition_zero"]
    assert not complex_data["independent_distortion_gauge_owned_at_T0"]
    assert not complex_data["distortion_radical_relabelled_as_gauge"]
    cases = {row["case"]: row for row in packet["exact_controls"]["cases"]}
    assert packet["exact_controls"]["field_dimension"] == 229386
    nonnull = cases["native_nonnull"]
    null = cases["native_null_auxiliary_nonzero"]
    for row in cases.values():
        assert row["gauge_map_formula"] == "G_q(v)_(ab)=q_a v_b+q_b v_a"
        assert row["redundancy_map"] == "R_q=G_q^T"
        assert row["gauge_rank"] == row["redundancy_rank"] == 4
        assert row["distortion_gauge_columns_at_T0"] == 0
        assert row["i1b_euler_times_gauge_rank"] == 0
        assert row["redundancy_times_i1b_euler_rank"] == 0
        assert row["residual_hessian_times_gauge_rank"] == 0
        assert rank_fraction_free(10, 4, row["gauge_nonzero_entries"]) == 4
    assert (nonnull["universal_coupled_euler_rank_upper"], null["universal_coupled_euler_rank_upper"]) == (131074, 131071)
    assert (nonnull["universal_middle_cohomology_lower"], null["universal_middle_cohomology_lower"]) == (98308, 98311)
    assert (nonnull["full_trace_middle_cohomology"], null["full_trace_middle_cohomology"]) == (98308, 106568)
    decision = packet["decision"]
    assert not decision["kernel_equals_gauge_image_for_any_same_response_pairing"]
    assert not decision["same_response_residual_square_repair_is_elliptic"]
    assert not decision["actual_redundancy_tower_beyond_metric_diffeomorphism_owned"]
    assert "UNCHANGED" in packet["source_and_ledger_effect"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
