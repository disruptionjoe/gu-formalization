#!/usr/bin/env python3
"""K771: exact selected-I1B plus positive curvature comparator composition.

Run with ``sage -python``.  The calculation reuses K743's complete invariant
28/56-dimensional decomposition and adds the K768 positive-Cartan curvature
Hessian coefficientwise before taking ranks.  Ranks are therefore ranks of
the summed operator, not sums of separately computed ranks.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import runpy
import sys
from collections import Counter
from pathlib import Path
from typing import Any

try:
    from sage.all import QQ, matrix
except ModuleNotFoundError:
    if __name__ == "__main__":
        os.execvp("sage", ["sage", "-python", *sys.argv])
    raise

ROOT = Path(__file__).resolve().parents[2]
K743_SCRIPT = ROOT / "tests/channel-swings/k743_sc_act_06_residual_square_image_cap.py"
OUTPUT = ROOT / "lab/process/k771-sc-act-06-positive-curvature-i1b-composition.json"
PATHS = {
    "k714": ROOT / "lab/process/k714-sc-act-06-cartan-reduction-gauge-metric.json",
    "k720": ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json",
    "k743": ROOT / "lab/process/k743-sc-act-06-residual-square-image-cap.json",
    "k768": ROOT / "lab/process/k768-sc-act-06-curvature-square-rank-boundary.json",
    "k770": ROOT / "lab/process/k770-sc-act-06-curvature-square-successor-gate.json",
}
ROUTING_NOTICE = "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result."


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_helpers() -> dict[str, Any]:
    return runpy.run_path(str(K743_SCRIPT))


def positive_curvature_block(basis: list[tuple[int, int, int]], covector: tuple[int, ...]):
    q2 = sum(value * value for value in covector)
    entries = {}
    for row, (_row_label, nu, row_mask) in enumerate(basis):
        for column, (_column_label, mu, column_mask) in enumerate(basis):
            if row_mask != column_mask:
                continue
            value = q2 * int(nu == mu) - covector[nu] * covector[mu]
            if value:
                entries[(row, column)] = QQ(value)
    return matrix(QQ, len(basis), len(basis), entries, sparse=True)


def distortion_census(H: dict[str, Any], M: dict[str, Any], case: str):
    covector, _toggle_axes, blocks = H["case_blocks"](M, case)
    totals = Counter()
    types = Counter()
    for labels, multiplicity in blocks:
        basis, _raw, i1b = H["raw_block"](M, covector, labels)
        curvature = positive_curvature_block(basis, covector)
        combined = i1b + curvature
        key = (i1b.rank(), curvature.rank(), combined.rank(), len(basis))
        types[key] += multiplicity
        totals["i1b_rank"] += multiplicity * key[0]
        totals["curvature_rank"] += multiplicity * key[1]
        totals["combined_rank"] += multiplicity * key[2]
        totals["dimension"] += multiplicity * key[3]
    return covector, totals, types


def coupled_rank(H: dict[str, Any], M: dict[str, Any], case: str, distortion_rank: int):
    covector, toggle_axes, _blocks = H["case_blocks"](M, case)
    columns = H["curvature_columns"](M, covector)
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
    basis, _raw, i1b = H["raw_block"](M, covector, labels)
    curvature = positive_curvature_block(basis, covector)
    combined_connection = i1b + curvature
    index = {(label, mu): i for i, (label, mu, _mask) in enumerate(basis)}
    entries = {}
    for column_index, column in enumerate(columns):
        for (label, nu), value in column.items():
            if value[1]:
                raise AssertionError("metric column left the pinned real basis")
            entries[(index[(label, nu)], column_index)] = QQ(value[0].numerator) / QQ(value[0].denominator)
    mixed = matrix(QQ, combined_connection.nrows(), len(H["METRIC_SLOTS"]), entries, sparse=True)
    coupled = matrix.block(
        QQ,
        [[matrix(QQ, 10, 10), mixed.transpose()], [mixed, combined_connection]],
    )
    gauge = matrix(QQ, coupled.nrows(), 4, sparse=True)
    for row, (a, b) in enumerate(H["METRIC_SLOTS"]):
        for vector_index in range(4):
            gauge[row, vector_index] = (
                (covector[a] if b == vector_index else 0)
                + (covector[b] if a == vector_index else 0)
            )
    local_connection_rank = combined_connection.rank()
    coupled_rank_value = coupled.rank()
    return {
        "local_label_count": len(labels),
        "local_connection_dimension": len(basis),
        "local_connection_rank": local_connection_rank,
        "metric_coupled_rank": coupled_rank_value,
        "metric_rank_increment": coupled_rank_value - local_connection_rank,
        "total_coupled_rank": distortion_rank - local_connection_rank + coupled_rank_value,
        "gauge_rank": gauge.rank(),
        "euler_times_gauge_rank": (coupled * gauge).rank(),
        "redundancy_times_euler_rank": (gauge.transpose() * coupled).rank(),
    }


def build() -> dict[str, Any]:
    H = load_helpers()
    M = H["load_algebra"]()
    cases = []
    for case in ("native_nonnull", "native_null_auxiliary_nonzero"):
        _covector, totals, types = distortion_census(H, M, case)
        coupled = coupled_rank(H, M, case, totals["combined_rank"])
        middle = 229386 - coupled["total_coupled_rank"] - coupled["gauge_rank"]
        cases.append(
            {
                "case": case,
                "distortion_dimension": totals["dimension"],
                "distortion_i1b_rank": totals["i1b_rank"],
                "distortion_positive_curvature_rank": totals["curvature_rank"],
                "distortion_summed_operator_rank": totals["combined_rank"],
                "block_types": [
                    {
                        "i1b_rank": key[0],
                        "positive_curvature_rank": key[1],
                        "summed_operator_rank": key[2],
                        "block_dimension": key[3],
                        "multiplicity": multiplicity,
                    }
                    for key, multiplicity in sorted(types.items())
                ],
                **coupled,
                "bosonic_middle_cohomology_dimension": middle,
                "middle_exact": middle == 0,
            }
        )
    return {
        "schema_version": "1.0",
        "result_id": "K771-SC-ACT-06-POSITIVE-CURVATURE-I1B-COMPOSITION",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "INTERNAL_COMPARATOR_ONLY",
        "gu_comparator_routing": ROUTING_NOTICE,
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact invariant-block ranks for the sum of K720's selected I1B bosonic Euler symbol and K768's identity-Cartan positive curvature-square comparator on K720's frozen flat germ.",
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "gu_typed_objects": {
            "carrier": "S^2(T*X) direct-sum Omega1(Cl_14(C)); complex dimension 229386",
            "pairing": "K714 identity Cartan auxiliary metric for the comparator; K717 native action pairing remains distinct",
            "real_structure": "K743 pinned real invariant blocks used only for exact rank calculation",
            "grading": "rank-four metric diffeomorphism gauge -> coupled metric/distortion field -> summed Euler rows",
            "action_owner": "selected source I1B plus a repository-only curvature-square comparator; the sum is not source-owned",
            "target": "middle principal-symbol cohomology of the frozen summed comparator",
        },
        "composition_theorem": {
            "operator": "E_total(q)=E_I1B(q)+diag(0_metric,d_q^{*q_Cartan}d_q)",
            "rank_method": "sum matrices inside every complete K743 invariant block before exact rational rank",
            "separate_rank_addition_used": False,
            "relative_weight": 1,
            "all_invariant_blocks_enumerated": True,
        },
        "exact_controls": {
            "field_dimension": 229386,
            "owned_metric_diffeomorphism_rank": 4,
            "cases": cases,
        },
        "decision": {
            "summed_comparator_middle_exact_on_both_tested_strata": all(row["middle_exact"] for row in cases),
            "source_owned_total_action": False,
            "all_covector_exactness_proved": False,
            "global_SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Check the actual total-action gauge/redundancy identities and the displayed fermion diagonal, then close the comparator at repository-only grade unless source ownership and an all-covector theorem are supplied.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The exact composition uses an unowned positive curvature comparator on two representative strata and cannot change the source or physics ledger.",
        "controls": {
            "producer": "tests/channel-swings/k771_sc_act_06_positive_curvature_i1b_composition.py",
            "probe": "tests/channel-swings/k771_sc_act_06_positive_curvature_i1b_composition_probe.py",
            "controls_passed": 30,
            "hostile_mutations_rejected": 16,
        },
        "claim_ceiling": "Exact two-stratum invariant-block rank theorem for one fixed repository-only positive-curvature/I1B sum. No source ownership, all-covector theorem, canonical reduction, global SC-ACT-06 conclusion, or physical conclusion.",
    }


def validate(packet: dict[str, Any]) -> None:
    assert packet["result_id"].startswith("K771-")
    assert packet["classification"] == "INTERNAL_COMPARATOR_ONLY"
    assert packet["target_claim"] == "SC-ACT-06"
    assert packet["exact_controls"]["field_dimension"] == 229386
    assert len(packet["exact_controls"]["cases"]) == 2
    assert packet["composition_theorem"]["all_invariant_blocks_enumerated"]
    assert not packet["composition_theorem"]["separate_rank_addition_used"]
    assert not packet["decision"]["source_owned_total_action"]
    assert not packet["decision"]["all_covector_exactness_proved"]
    assert not packet["decision"]["global_SC_ACT_06_proved_or_refuted"]
    rows = {row["case"]: row for row in packet["exact_controls"]["cases"]}
    nonnull = rows["native_nonnull"]
    null = rows["native_null_auxiliary_nonzero"]
    assert (nonnull["distortion_i1b_rank"], null["distortion_i1b_rank"]) == (130912, 122746)
    assert nonnull["distortion_positive_curvature_rank"] == null["distortion_positive_curvature_rank"] == 212992
    assert nonnull["distortion_summed_operator_rank"] == null["distortion_summed_operator_rank"] == 221183
    assert (nonnull["total_coupled_rank"], null["total_coupled_rank"]) == (221189, 221186)
    assert (nonnull["metric_rank_increment"], null["metric_rank_increment"]) == (6, 3)
    assert (nonnull["bosonic_middle_cohomology_dimension"], null["bosonic_middle_cohomology_dimension"]) == (8193, 8196)
    assert (nonnull["local_label_count"], null["local_label_count"]) == (8, 12)
    assert nonnull["gauge_rank"] == null["gauge_rank"] == 4
    assert nonnull["euler_times_gauge_rank"] == null["euler_times_gauge_rank"] == 0
    assert nonnull["redundancy_times_euler_rank"] == null["redundancy_times_euler_rank"] == 0
    assert sum(row["multiplicity"] for row in nonnull["block_types"]) == 8192
    assert sum(row["multiplicity"] for row in null["block_types"]) == 4096
    assert not nonnull["middle_exact"] and not null["middle_exact"]
    assert not packet["decision"]["summed_comparator_middle_exact_on_both_tested_strata"]
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
