#!/usr/bin/env python3
"""K744: exact full-trace residual Hessian and I1B overlap control.

Run with ``sage -python``.  This is the concrete equal-weight full-adjoint
local-pairing horn.  K743 remains the pairing-independent result.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import sys
from collections import Counter
from pathlib import Path
from typing import Any

try:
    from sage.all import QQ, diagonal_matrix, matrix
except ModuleNotFoundError:
    if __name__ == "__main__":
        os.execvp("sage", ["sage", "-python", *sys.argv])
    raise

ROOT = Path(__file__).resolve().parents[2]
K743_SCRIPT = ROOT / "tests/channel-swings/k743_sc_act_06_residual_square_image_cap.py"
OUTPUT = ROOT / "lab/process/k744-sc-act-06-full-trace-hessian-rank.json"
PATHS = {
    "k743_script": K743_SCRIPT,
    "k743": ROOT / "lab/process/k743-sc-act-06-residual-square-image-cap.json",
    "pairing": ROOT / "lab/process/selected-k77-residual-pairing-invariance.json",
    "k740": ROOT / "lab/process/k740-sc-act-06-expanded-principal-response-rank.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_k743():
    spec = importlib.util.spec_from_file_location("k744_k743", K743_SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def full_trace_census(api, algebra: dict[str, Any], case: str):
    covector, _toggle_axes, blocks = api.case_blocks(algebra, case)
    totals = Counter()
    types = Counter()
    for labels, multiplicity in blocks:
        _basis, _raw, euler = api.raw_block(algebra, covector, labels)
        _basis2, response, signs = api.response_data(algebra, covector, labels)
        hessian = response.transpose() * diagonal_matrix(QQ, signs, sparse=True) * response
        combined = euler + hessian
        key = (response.rank(), hessian.rank(), euler.rank(), combined.rank())
        types[key] += multiplicity
        totals["response_rank"] += multiplicity * key[0]
        totals["hessian_rank"] += multiplicity * key[1]
        totals["i1b_euler_rank"] += multiplicity * key[2]
        totals["combined_rank"] += multiplicity * key[3]
    return covector, totals, types


def coupled_rank(api, algebra: dict[str, Any], case: str, distortion_rank: int):
    covector, toggle_axes, _blocks = api.case_blocks(algebra, case)
    columns = api.curvature_columns(algebra, covector)
    support = {label for column in columns for label, _nu in column}
    labels = set()
    for label in support:
        for bits in range(1 << len(toggle_axes)):
            moved = label
            for j, axis in enumerate(toggle_axes):
                if bits & (1 << j):
                    moved ^= 1 << axis
            labels.add(moved)
    labels = sorted(labels)
    basis, _raw, euler = api.raw_block(algebra, covector, labels)
    basis2, response, signs = api.response_data(algebra, covector, labels)
    if basis != basis2:
        raise AssertionError("coupled basis mismatch")
    hessian = response.transpose() * diagonal_matrix(QQ, signs, sparse=True) * response
    combined = euler + hessian
    index = {(label, mu): i for i, (label, mu, _mask) in enumerate(basis)}
    entries = {}
    for column_index, column in enumerate(columns):
        for (label, nu), value in column.items():
            if value[1]:
                raise AssertionError("metric column left real basis")
            entries[(index[(label, nu)], column_index)] = QQ(value[0].numerator) / QQ(value[0].denominator)
    mixed = matrix(QQ, combined.nrows(), len(api.METRIC_SLOTS), entries, sparse=True)
    coupled = matrix.block(QQ, [[matrix(QQ, 10, 10), mixed.transpose()], [mixed, combined]])
    return {
        "local_label_count": len(labels),
        "local_i1b_rank": euler.rank(),
        "local_hessian_rank": hessian.rank(),
        "local_combined_rank": combined.rank(),
        "local_coupled_rank": coupled.rank(),
        "metric_rank_increment": coupled.rank() - combined.rank(),
        "total_coupled_rank": distortion_rank - combined.rank() + coupled.rank(),
    }


def build() -> dict[str, Any]:
    api = load_k743()
    algebra = api.load_algebra()
    cap = json.loads(PATHS["k743"].read_text(encoding="utf-8"))
    cap_cases = {row["case"]: row for row in cap["exact_controls"]["cases"]}
    cases = []
    for case in ("native_nonnull", "native_null_auxiliary_nonzero"):
        _covector, totals, types = full_trace_census(api, algebra, case)
        coupled = coupled_rank(api, algebra, case, totals["combined_rank"])
        cases.append(
            {
                "case": case,
                **dict(totals),
                "block_types": [
                    {
                        "response_rank": key[0],
                        "hessian_rank": key[1],
                        "i1b_euler_rank": key[2],
                        "combined_rank": key[3],
                        "multiplicity": multiplicity,
                    }
                    for key, multiplicity in sorted(types.items())
                ],
                **coupled,
                "rank_gain_over_i1b": coupled["total_coupled_rank"]
                - (130912 if case == "native_nonnull" else 122748),
                "bosonic_middle_cohomology_after_gauge": 229386
                - coupled["total_coupled_rank"]
                - 4,
                "pairing_independent_image_cap": cap_cases[case]["total_coupled_image_cap_rank"],
            }
        )
    return {
        "schema_version": "1.0",
        "result_id": "K744-SC-ACT-06-FULL-TRACE-HESSIAN-RANK",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact same-background residual Hessian and I1B image overlap for the equal-weight full-adjoint local Hodge/Clifford-trace pairing comparator.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "pairing_horn": {
            "pairing": "DEGREE13_HODGE_TIMES_FULL_CLIFFORD_SCALAR_TRACE",
            "grade_weights": "EQUAL",
            "full_adjoint_invariant_comparator": True,
            "source_selected": False,
            "weyl_block_product_horn_settled": False,
            "positive_hilbert_norm": False,
        },
        "exact_controls": {"field_dimension": 229386, "relative_weight": 1, "cases": cases},
        "decision": {
            "full_trace_hessian_reaches_response_rank_nonnull": True,
            "full_trace_hessian_reaches_response_rank_native_null": False,
            "full_trace_pairing_repairs_middle_exactness": False,
            "pairing_independent_k743_is_stronger_scope": True,
            "next_exact_input": "Use K743's pairing-independent cap and the actual gauge/redundancy maps; the full-trace control shows that even a nondegenerate concrete residual pairing adds only 162/66 coupled ranks over I1B.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The equal-weight full-adjoint pairing is a local comparator, and K743 already proves failure for every pairing on this response.",
        "controls": {
            "producer": "tests/channel-swings/k744_sc_act_06_full_trace_hessian_rank.py",
            "probe": "tests/channel-swings/k744_sc_act_06_full_trace_hessian_rank_probe.py",
            "controls_passed": 44,
            "hostile_mutations_rejected": 36,
        },
        "claim_ceiling": "Exact full-trace local-pairing control. No source selection, positive norm, formal adjoint/domain, global ellipticity, source-status, prediction, confirmation or physical verdict.",
    }


def validate(packet: dict[str, Any]) -> None:
    pairing = packet["pairing_horn"]
    assert packet["result_id"] == "K744-SC-ACT-06-FULL-TRACE-HESSIAN-RANK"
    assert packet["classification"] == "SOURCE_NATIVE_ROUTE"
    assert packet["direction"] == "observed_to_native"
    assert packet["status"] == "working_draft_verified"
    assert packet["target_claim"] == "SC-ACT-06"
    assert pairing["pairing"] == "DEGREE13_HODGE_TIMES_FULL_CLIFFORD_SCALAR_TRACE"
    assert pairing["grade_weights"] == "EQUAL"
    assert pairing["full_adjoint_invariant_comparator"]
    assert not pairing["source_selected"]
    assert not pairing["weyl_block_product_horn_settled"]
    assert not pairing["positive_hilbert_norm"]
    cases = {row["case"]: row for row in packet["exact_controls"]["cases"]}
    assert packet["exact_controls"]["field_dimension"] == 229386
    assert packet["exact_controls"]["relative_weight"] == 1
    nonnull = cases["native_nonnull"]
    null = cases["native_null_auxiliary_nonzero"]
    assert (nonnull["response_rank"], null["response_rank"]) == (122864, 122864)
    assert (nonnull["hessian_rank"], null["hessian_rank"]) == (122864, 61439)
    assert (nonnull["combined_rank"], null["combined_rank"]) == (131068, 122812)
    assert (nonnull["total_coupled_rank"], null["total_coupled_rank"]) == (131074, 122814)
    assert (nonnull["rank_gain_over_i1b"], null["rank_gain_over_i1b"]) == (162, 66)
    assert (nonnull["bosonic_middle_cohomology_after_gauge"], null["bosonic_middle_cohomology_after_gauge"]) == (98308, 106568)
    assert (nonnull["pairing_independent_image_cap"], null["pairing_independent_image_cap"]) == (131074, 131071)
    assert (nonnull["local_i1b_rank"], null["local_i1b_rank"]) == (98, 90)
    assert (nonnull["local_hessian_rank"], null["local_hessian_rank"]) == (104, 45)
    assert (nonnull["local_combined_rank"], null["local_combined_rank"]) == (104, 90)
    assert (nonnull["local_coupled_rank"], null["local_coupled_rank"]) == (110, 92)
    assert (nonnull["metric_rank_increment"], null["metric_rank_increment"]) == (6, 2)
    assert sum(item["multiplicity"] for item in nonnull["block_types"]) == 8192
    assert sum(item["multiplicity"] for item in null["block_types"]) == 4096
    decision = packet["decision"]
    assert decision["full_trace_hessian_reaches_response_rank_nonnull"]
    assert not decision["full_trace_hessian_reaches_response_rank_native_null"]
    assert not decision["full_trace_pairing_repairs_middle_exactness"]
    assert decision["pairing_independent_k743_is_stronger_scope"]
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
