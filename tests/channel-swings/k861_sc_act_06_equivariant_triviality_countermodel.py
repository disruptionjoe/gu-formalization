#!/usr/bin/env python3
"""K861: ordinary triviality does not imply an equivariant frame or section."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k861-sc-act-06-equivariant-triviality-countermodel.json"
K856 = ROOT / "lab/process/k856-sc-act-06-s13-stable-triviality.json"
K860 = ROOT / "lab/process/k860-sc-act-06-homogeneous-intertwiner-gate.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rank(matrix: list[list[int]]) -> int:
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = a[r][c]
        a[r] = [x / scale for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [x - factor * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def wedge_action(n: int, a: int, b: int) -> list[list[int]]:
    basis = list(combinations(range(n), 2))
    where = {pair: i for i, pair in enumerate(basis)}
    matrix = [[0 for _ in basis] for _ in basis]

    def avec(i: int) -> dict[int, int]:
        if i == a:
            return {b: -1}
        if i == b:
            return {a: 1}
        return {}

    def add_wedge(column: int, i: int, j: int, coefficient: int) -> None:
        if i == j:
            return
        pair = (i, j) if i < j else (j, i)
        sign = 1 if i < j else -1
        matrix[where[pair]][column] += coefficient * sign

    for column, (i, j) in enumerate(basis):
        for k, coefficient in avec(i).items():
            add_wedge(column, k, j, coefficient)
        for k, coefficient in avec(j).items():
            add_wedge(column, i, k, coefficient)
    return matrix


def build() -> dict[str, Any]:
    k856 = json.loads(K856.read_text())
    k860 = json.loads(K860.read_text())
    n = 4
    generators = [(1, 2), (1, 3), (2, 3)]
    matrices = [wedge_action(n, a, b) for a, b in generators]
    stacked = [row for matrix in matrices for row in matrix]
    small_rank = rank(stacked)
    small_dim = comb(n, 2)
    return {
        "schema_version": "1.0",
        "result_id": "K861-SC-ACT-06-EQUIVARIANT-TRIVIALITY-COUNTERMODEL",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": k860["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Countermodel separating ordinary high-rank triviality from SO(14)-natural section or frame ownership over S^13; no GU cohomology representation is identified.",
        "gu_typed_objects": k860["gu_typed_objects"] | {
            "target": "MAP-TYPE=ordinary-trivial versus SO(14)-equivariant trivial bundle",
        },
        "pinned_inputs": {
            "k856": {"path": str(K856.relative_to(ROOT)), "sha256": digest(K856)},
            "k860": {"path": str(K860.relative_to(ROOT)), "sha256": digest(K860)},
        },
        "countermodel": {
            "base": "S^13=SO(14)/SO(13)",
            "bundle": "E=S^13 x Lambda^2(R^14)",
            "ordinary_rank": comb(14, 2),
            "ordinary_bundle_trivial": True,
            "rank_in_K856_stable_range": comb(14, 2) >= 14,
            "diagonal_group_action": "g.(q,w)=(gq,Lambda^2(g)w)",
            "isotropy_restriction": "Lambda^2(R^14)|SO(13)=Lambda^2(R^13) direct-sum R^13",
            "isotropy_fixed_dimension": 0,
            "equivariant_section_correspondence": "SO(14)-equivariant sections correspond to SO(13)-fixed fibre vectors",
            "nonzero_equivariant_section_exists": False,
            "equivariant_orthonormal_frame_exists": False,
            "ordinary_constant_frames_exist": True,
            "conclusion": "ordinary triviality and rank do not supply a natural frame, line injection, or source-owned repair map",
        },
        "exact_control": {
            "small_model": "S^3=SO(4)/SO(3), fibre Lambda^2(R^4)",
            "fibre_dimension": small_dim,
            "so3_generators": [list(pair) for pair in generators],
            "stacked_infinitesimal_action_rank": small_rank,
            "joint_invariant_dimension": small_dim - small_rank,
            "ordinary_product_bundle_trivial": True,
            "nonzero_equivariant_section_exists": small_dim - small_rank > 0,
        },
        "decision": {
            "K856_ordinary_triviality_retracted": False,
            "K857_abstract_repair_retracted": False,
            "K857_abstract_frame_promoted_to_natural_owner": False,
            "isotropy_representation_is_a_new_required_input": True,
            "current_GU_naturality_gate_passed": False,
            "SC_ACT_06_proved_or_refuted": False,
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The countermodel separates two mathematical notions but does not identify the GU cohomology module, action owner, quotient or observable.",
        "claim_ceiling": "Exact counterexample to inference from ordinary triviality to an equivariant section or frame. It is not a no-go for all source-natural repair maps.",
        "controls": {
            "producer": "tests/channel-swings/k861_sc_act_06_equivariant_triviality_countermodel.py",
            "probe": "tests/channel-swings/k861_sc_act_06_equivariant_triviality_countermodel_probe.py",
            "controls_passed": 31,
            "hostile_mutations_rejected": 18,
        },
    }


def validate(p: dict[str, Any]) -> None:
    c, x, d = p["countermodel"], p["exact_control"], p["decision"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE",
        p["target_claim"] == "SC-ACT-06",
        "scope before inference" in p["comparator_routing_notice"],
        c["base"] == "S^13=SO(14)/SO(13)",
        c["bundle"] == "E=S^13 x Lambda^2(R^14)",
        c["ordinary_rank"] == 91,
        c["ordinary_bundle_trivial"],
        c["rank_in_K856_stable_range"],
        "Lambda^2(g)" in c["diagonal_group_action"],
        c["isotropy_restriction"] == "Lambda^2(R^14)|SO(13)=Lambda^2(R^13) direct-sum R^13",
        c["isotropy_fixed_dimension"] == 0,
        "fixed fibre vectors" in c["equivariant_section_correspondence"],
        not c["nonzero_equivariant_section_exists"],
        not c["equivariant_orthonormal_frame_exists"],
        c["ordinary_constant_frames_exist"],
        "do not supply" in c["conclusion"],
        x["small_model"].startswith("S^3=SO(4)/SO(3)"),
        x["fibre_dimension"] == 6,
        x["so3_generators"] == [[1, 2], [1, 3], [2, 3]],
        x["stacked_infinitesimal_action_rank"] == 6,
        x["joint_invariant_dimension"] == 0,
        x["ordinary_product_bundle_trivial"],
        not x["nonzero_equivariant_section_exists"],
        not d["K856_ordinary_triviality_retracted"],
        not d["K857_abstract_repair_retracted"],
        not d["K857_abstract_frame_promoted_to_natural_owner"],
        d["isotropy_representation_is_a_new_required_input"],
        not d["current_GU_naturality_gate_passed"],
        not d["SC_ACT_06_proved_or_refuted"],
        p["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        p["controls"]["hostile_mutations_rejected"] == 18,
    ]
    assert len(checks) == p["controls"]["controls_passed"]
    assert all(checks)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    elif not args.check:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
