#!/usr/bin/env python3
"""K772: total-complex audit for K771's summed comparator."""
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
K771_SCRIPT = ROOT / "tests/channel-swings/k771_sc_act_06_positive_curvature_i1b_composition.py"
OUTPUT = ROOT / "lab/process/k772-sc-act-06-positive-curvature-total-complex.json"
PATHS = {
    "k720": ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json",
    "k745": ROOT / "lab/process/k745-sc-act-06-gauge-redundancy-obstruction.json",
    "k768": ROOT / "lab/process/k768-sc-act-06-curvature-square-rank-boundary.json",
    "k771": ROOT / "lab/process/k771-sc-act-06-positive-curvature-i1b-composition.json",
}
ROUTING_NOTICE = "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result."


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def internal_gauge_matrix(basis, covector):
    masks = sorted({mask for _label, mu, mask in basis if covector[mu]})
    position = {mask: column for column, mask in enumerate(masks)}
    entries = {}
    for row, (_label, mu, mask) in enumerate(basis):
        if covector[mu]:
            entries[(row, position[mask])] = QQ(covector[mu])
    return masks, matrix(QQ, len(basis), len(masks), entries, sparse=True)


def gauge_census(K: dict[str, Any], H: dict[str, Any], M: dict[str, Any], case: str):
    covector, _toggle_axes, blocks = H["case_blocks"](M, case)
    totals = Counter()
    types = Counter()
    for labels, multiplicity in blocks:
        basis, _raw, i1b = H["raw_block"](M, covector, labels)
        curvature = K["positive_curvature_block"](basis, covector)
        combined = i1b + curvature
        masks, gauge = internal_gauge_matrix(basis, covector)
        gauge_rank = gauge.rank()
        i1b_on_gauge_rank = (i1b * gauge).rank()
        combined_on_gauge_rank = (combined * gauge).rank()
        candidate_kernel = gauge.ncols() - combined_on_gauge_rank
        key = (len(masks), gauge_rank, i1b_on_gauge_rank, combined_on_gauge_rank, candidate_kernel)
        types[key] += multiplicity
        totals["candidate_dimension"] += multiplicity * len(masks)
        totals["candidate_rank"] += multiplicity * gauge_rank
        totals["i1b_image_rank"] += multiplicity * i1b_on_gauge_rank
        totals["combined_image_rank"] += multiplicity * combined_on_gauge_rank
        totals["candidate_kernel_dimension"] += multiplicity * candidate_kernel
    return totals, types


def build() -> dict[str, Any]:
    K = runpy.run_path(str(K771_SCRIPT))
    H = K["load_helpers"]()
    M = H["load_algebra"]()
    k771 = json.loads(PATHS["k771"].read_text(encoding="utf-8"))
    k771_cases = {row["case"]: row for row in k771["exact_controls"]["cases"]}
    cases = []
    for case in ("native_nonnull", "native_null_auxiliary_nonzero"):
        totals, types = gauge_census(K, H, M, case)
        prior = k771_cases[case]
        actual_gauge_rank = prior["gauge_rank"]
        refined_middle = 229386 - prior["total_coupled_rank"] - actual_gauge_rank
        distortion_kernel = prior["distortion_dimension"] - prior["distortion_summed_operator_rank"]
        cases.append(
            {
                "case": case,
                "internal_candidate_dimension": totals["candidate_dimension"],
                "internal_candidate_rank": totals["candidate_rank"],
                "i1b_on_internal_candidate_rank": totals["i1b_image_rank"],
                "combined_on_internal_candidate_rank": totals["combined_image_rank"],
                "internal_candidate_kernel_dimension": totals["candidate_kernel_dimension"],
                "candidate_kernel_equals_distortion_kernel": totals["candidate_kernel_dimension"] == distortion_kernel,
                "internal_block_types": [
                    {
                        "coefficient_count": key[0],
                        "candidate_rank": key[1],
                        "i1b_on_candidate_rank": key[2],
                        "combined_on_candidate_rank": key[3],
                        "candidate_kernel_dimension": key[4],
                        "multiplicity": multiplicity,
                    }
                    for key, multiplicity in sorted(types.items())
                ],
                "metric_diffeomorphism_rank": prior["gauge_rank"],
                "total_actual_gauge_rank": actual_gauge_rank,
                "summed_euler_rank": prior["total_coupled_rank"],
                "euler_times_metric_gauge_rank": prior["euler_times_gauge_rank"],
                "metric_redundancy_times_euler_rank": prior["redundancy_times_euler_rank"],
                "refined_middle_cohomology_dimension": refined_middle,
                "middle_exact": refined_middle == 0,
            }
        )
    return {
        "schema_version": "1.0",
        "result_id": "K772-SC-ACT-06-POSITIVE-CURVATURE-TOTAL-COMPLEX",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "INTERNAL_COMPARATOR_ONLY",
        "gu_comparator_routing": ROUTING_NOTICE,
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact gauge/redundancy audit for K771's selected-I1B plus identity-Cartan curvature comparator on the two frozen covector strata.",
        "gu_typed_objects": {
            "carrier": "LAYER=source-print+toy BRIDGE=K720-plus-K768 frozen sum; S^2(T*X) direct-sum Omega1(Cl_14(C)); CHIRALITY=N/A",
            "pairing": "K717 native action form plus K714 identity Cartan comparator form; ON=coupled metric/distortion field",
            "real_structure": "K743 pinned real invariant blocks",
            "grading": "owned metric-diffeomorphism map -> coupled bosonic Euler map -> transpose redundancy",
            "action_owner": "source-action plus comparator; no combined source owner",
            "target": "middle cohomology of the summed tested-stratum complex; MAP-TYPE=not-a-map"
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "complex_theorem": {
            "curvature_only_internal_candidate": "lambda -> q lambda on each Clifford coefficient",
            "total_action_rule": "a curvature-only candidate direction is not quotiented merely because the selected I1B block also annihilates a subspace; the total theory must own that subspace as a gauge map",
            "metric_gauge": "the owned rank-four metric diffeomorphism map has zero connection component at the frozen T=0 germ",
            "metric_redundancy": "the transpose rank-four map annihilates the summed Euler block on both tested strata",
            "curvature_only_gauge_automatically_added": False,
            "accidental_candidate_kernel_promoted_to_gauge": False,
        },
        "exact_controls": {"field_dimension": 229386, "cases": cases},
        "decision": {
            "summed_comparator_middle_exact_on_both_tested_strata": all(row["middle_exact"] for row in cases),
            "complete_total_action_complex_constructed_for_tested_strata": True,
            "source_owned_total_action": False,
            "all_covector_exactness_proved": False,
            "global_SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Compose the exact bosonic nonexactness with the displayed fermion diagonal, then retire this positive-comparator repair without promoting it to a source action.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The complete tested-stratum complex remains a repository comparator with an unowned positive reduction.",
        "controls": {
            "producer": "tests/channel-swings/k772_sc_act_06_positive_curvature_total_complex.py",
            "probe": "tests/channel-swings/k772_sc_act_06_positive_curvature_total_complex_probe.py",
            "controls_passed": 28,
            "hostile_mutations_rejected": 16,
        },
        "claim_ceiling": "Exact total-complex and internal-gauge audit for one fixed positive-curvature/I1B comparator on two representative strata. No source ownership, all-covector theorem, global SC-ACT-06 conclusion, or physical conclusion.",
    }


def validate(packet: dict[str, Any]) -> None:
    assert packet["result_id"].startswith("K772-")
    assert packet["classification"] == "INTERNAL_COMPARATOR_ONLY"
    assert packet["target_claim"] == "SC-ACT-06"
    assert packet["exact_controls"]["field_dimension"] == 229386
    assert len(packet["exact_controls"]["cases"]) == 2
    assert packet["decision"]["complete_total_action_complex_constructed_for_tested_strata"]
    assert not packet["complex_theorem"]["curvature_only_gauge_automatically_added"]
    assert not packet["complex_theorem"]["accidental_candidate_kernel_promoted_to_gauge"]
    assert not packet["decision"]["source_owned_total_action"]
    assert not packet["decision"]["all_covector_exactness_proved"]
    assert not packet["decision"]["global_SC_ACT_06_proved_or_refuted"]
    rows = {row["case"]: row for row in packet["exact_controls"]["cases"]}
    nonnull = rows["native_nonnull"]
    null = rows["native_null_auxiliary_nonzero"]
    assert nonnull["internal_candidate_dimension"] == null["internal_candidate_dimension"] == 16384
    assert nonnull["internal_candidate_rank"] == null["internal_candidate_rank"] == 16384
    assert nonnull["combined_on_internal_candidate_rank"] == null["combined_on_internal_candidate_rank"] == 8191
    assert nonnull["internal_candidate_kernel_dimension"] == null["internal_candidate_kernel_dimension"] == 8193
    assert nonnull["candidate_kernel_equals_distortion_kernel"] and null["candidate_kernel_equals_distortion_kernel"]
    assert nonnull["total_actual_gauge_rank"] == null["total_actual_gauge_rank"] == 4
    assert (nonnull["summed_euler_rank"], null["summed_euler_rank"]) == (221189, 221186)
    assert (nonnull["refined_middle_cohomology_dimension"], null["refined_middle_cohomology_dimension"]) == (8193, 8196)
    assert nonnull["euler_times_metric_gauge_rank"] == null["euler_times_metric_gauge_rank"] == 0
    assert nonnull["metric_redundancy_times_euler_rank"] == null["metric_redundancy_times_euler_rank"] == 0
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
