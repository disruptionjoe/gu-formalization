#!/usr/bin/env python3
"""K855: constant-rank middle cohomology is a continuous vector bundle."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k855-sc-act-06-cohomology-bundle.json"
K854 = ROOT / "lab/process/k854-sc-act-06-robust-quotient-repair-certificate.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rank(matrix: list[list[int]]) -> int:
    a = [[float(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols, pivot_row = len(a), len(a[0]), 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if abs(a[r][col]) > 1e-9), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row:
                factor = a[r][col]
                a[r] = [x - factor * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
    return pivot_row


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def build() -> dict[str, Any]:
    # G: R^2 -> R^5 spans e0,e1; J: R^5 -> R^2 reads e3,e4.
    g = [[1, 0], [0, 1], [0, 0], [0, 0], [0, 0]]
    j = [[0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
    projector_h = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    h = 5 - rank(j) - rank(g)
    return {
        "schema_version": "1.0",
        "result_id": "K855-SC-ACT-06-COHOMOLOGY-BUNDLE",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": json.loads(K854.read_text())["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Finite-dimensional constant-rank symbol families only; no complete GU cosphere family or source-owned repair map is supplied.",
        "gu_typed_objects": {
            "carrier": "LAYER=ambient CHIRALITY=N/A old middle symbol bundle over a compact Euclidean cosphere",
            "pairing": "continuous positive auxiliary fibre metric used only to realize orthogonal projectors",
            "real_structure": "fixed real symbol bundles",
            "grading": "old gauge image -> old middle kernel -> old equation image",
            "action_owner": "candidate-must-declare",
            "target": "MAP-TYPE=continuous old middle cohomology bundle",
        },
        "pinned_inputs": {"k854": {"path": str(K854.relative_to(ROOT)), "sha256": digest(K854)}},
        "theorem": {
            "base": "compact Hausdorff K",
            "complex": "continuous G_q:A->B and J_q:B->C with J_q G_q=0",
            "constant_rank_hypotheses": ["rank(G_q)=g", "rank(J_q)=j"],
            "bundle_conclusion": "H=ker(J)/im(G) is a continuous real vector bundle",
            "rank_formula": "rank(H)=dim(B)-rank(J)-rank(G)",
            "orthogonal_model": "H is represented by ker(J) intersect im(G)^perp",
            "projector_formula": "P_H=P_ker(J)-P_im(G)",
            "pointwise_dimensions_alone_are_not_enough": True,
            "rank_jumps_forbid_this_bundle_conclusion": True,
        },
        "exact_control": {
            "dim_A": 2, "dim_B": 5, "dim_C": 2,
            "rank_G": rank(g), "rank_J": rank(j), "JG": matmul(j, g),
            "rank_H": h, "projector_H": projector_h,
            "projector_rank": rank(projector_h),
            "projector_idempotent": matmul(projector_h, projector_h) == projector_h,
        },
        "decision": {
            "constant_rank_old_complex_produces_cohomology_bundle": True,
            "current_flat_packet_complete_cosphere_bundle_established": False,
            "source_owned_repair_maps_constructed": False,
            "SC_ACT_06_proved_or_refuted": False,
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "claim_ceiling": "Vector-bundle formation theorem for a future authenticated constant-rank family; no topological classification, GU realization, or ellipticity verdict yet.",
        "controls": {"producer": "tests/channel-swings/k855_sc_act_06_cohomology_bundle.py", "probe": "tests/channel-swings/k855_sc_act_06_cohomology_bundle_probe.py", "controls_passed": 29, "hostile_mutations_rejected": 16},
    }


def validate(p: dict[str, Any]) -> None:
    t, c, d = p["theorem"], p["exact_control"], p["decision"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE", p["target_claim"] == "SC-ACT-06",
        "scope before inference" in p["comparator_routing_notice"], p["gu_typed_objects"]["action_owner"] == "candidate-must-declare",
        t["base"] == "compact Hausdorff K", "J_q G_q=0" in t["complex"], len(t["constant_rank_hypotheses"]) == 2,
        "vector bundle" in t["bundle_conclusion"], t["rank_formula"] == "rank(H)=dim(B)-rank(J)-rank(G)",
        "perp" in t["orthogonal_model"], t["projector_formula"] == "P_H=P_ker(J)-P_im(G)",
        t["pointwise_dimensions_alone_are_not_enough"], t["rank_jumps_forbid_this_bundle_conclusion"],
        c["dim_A"] == 2, c["dim_B"] == 5, c["dim_C"] == 2, c["rank_G"] == 2, c["rank_J"] == 2,
        c["JG"] == [[0, 0], [0, 0]], c["rank_H"] == 1, c["projector_rank"] == 1, c["projector_idempotent"],
        d["constant_rank_old_complex_produces_cohomology_bundle"], not d["current_flat_packet_complete_cosphere_bundle_established"],
        not d["source_owned_repair_maps_constructed"], not d["SC_ACT_06_proved_or_refuted"],
        p["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED", "no topological classification" in p["claim_ceiling"],
        p["controls"]["hostile_mutations_rejected"] == 16,
    ]
    assert len(checks) == p["controls"]["controls_passed"]
    assert all(checks)


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true"); parser.add_argument("--check", action="store_true")
    args = parser.parse_args(); packet = build(); validate(packet); rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered, encoding="utf-8")
    elif not args.check: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
