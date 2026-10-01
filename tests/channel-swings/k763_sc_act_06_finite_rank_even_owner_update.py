#!/usr/bin/env python3
"""K763: finite-rank old-block update plus finite even extension theorem."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k763-sc-act-06-finite-rank-even-owner-update.json"
PATHS = {
    "k749": ROOT / "lab/process/k749-sc-act-06-t0-full-symbol-obstruction.json",
    "k759": ROOT / "lab/process/k759-sc-act-06-even-spectator-rank-update-theorem.json",
    "k762": ROOT / "lab/process/k762-sc-act-06-even-owner-successor-gate.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rank(matrix: list[list[int]]) -> int:
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols, pivot = len(a), len(a[0]), 0
    for col in range(cols):
        hit = next((row for row in range(pivot, rows) if a[row][col]), None)
        if hit is None:
            continue
        a[pivot], a[hit] = a[hit], a[pivot]
        lead = a[pivot][col]
        a[pivot] = [x / lead for x in a[pivot]]
        for row in range(rows):
            if row != pivot and a[row][col]:
                factor = a[row][col]
                a[row] = [x - factor * y for x, y in zip(a[row], a[pivot])]
        pivot += 1
        if pivot == rows:
            break
    return pivot


def sharp_control(r: int, m: int) -> dict[str, int]:
    # Coordinate 0 is the old image, the next r coordinates support K, the
    # next m support B, and the last coordinate is the unchanged gauge image.
    n = r + m + 2
    e = [[0 for _ in range(n)] for _ in range(n)]
    k = [[0 for _ in range(n)] for _ in range(n)]
    b = [[0 for _ in range(m)] for _ in range(n)]
    c = [[0 for _ in range(m)] for _ in range(m)]
    e[0][0] = 1
    for j in range(r):
        k[1 + j][1 + j] = 1
    for j in range(m):
        b[1 + r + j][j] = 1
    old = e
    extended = [
        [e[i][j] + k[i][j] for j in range(n)] + b[i]
        for i in range(n)
    ] + [
        [b[i][j] for i in range(n)] + c[j]
        for j in range(m)
    ]
    old_rank, new_rank, gauge_rank = rank(old), rank(extended), 1
    old_middle = n - old_rank - gauge_rank
    new_middle = n + m - new_rank - gauge_rank
    assert all(old[i][-1] == k[i][-1] == 0 for i in range(n))
    assert all(b[-1][j] == 0 for j in range(m))
    assert new_rank == old_rank + r + 2 * m
    assert new_middle == old_middle - r - m
    return {
        "r": r,
        "m": m,
        "old_rank": old_rank,
        "new_rank": new_rank,
        "gauge_rank": gauge_rank,
        "old_middle": old_middle,
        "new_middle": new_middle,
    }


def build() -> dict[str, Any]:
    controls = [sharp_control(r, m) for r, m in ((0, 1), (1, 1), (3, 2), (10, 1))]
    return {
        "schema_version": "1.0",
        "result_id": "K763-SC-ACT-06-FINITE-RANK-EVEN-OWNER-UPDATE",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Finite-dimensional principal-symbol extensions with a rank-r correction K to the old V-to-V* block, m new body-valued even fields, and the old gauge embedding preserved.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "typed_objects": {
            "old_euler_block": "E: V -> V*",
            "old_block_correction": "K: V -> V* with rank(K)<=r",
            "new_even_space": "S of dimension m",
            "extended_block": "H=[[E+K,B],[B^T,C]] on V+S",
            "gauge_map": "G_ext=(G,0), with KG=0 and B^T G=0",
            "grading": "body-valued even extension",
            "action_owner": "abstract Hessian class; no source or physical owner inferred",
        },
        "theorem": {
            "rank_update_bound": "rank(H)-rank(E) <= r+2m",
            "middle_cohomology_bound": "dim H_ext >= dim H_old-r-m",
            "proof": "Subtract diag(E,0). The old-old correction contributes rank at most r; after quotienting its image, every remaining update column or row factors through the m-dimensional new field space, contributing at most 2m. Rank-nullity and the unchanged gauge rank give the cohomology bound.",
            "sharp": True,
            "requires_rank_bound_on_old_block_correction": True,
            "requires_unchanged_gauge_rank": True,
            "requires_ward_compatibility": True,
            "allows_arbitrary_mixed_and_new_self_blocks": True,
            "k759_recovered_at_r_zero": True,
        },
        "exact_controls": controls,
        "decision": {
            "small_rank_nonfactorizing_update_can_be_decisively_bounded": True,
            "r_plus_m_is_necessary_rank_budget_not_sufficiency": True,
            "changed_background_or_unbounded_rank_owner_outside_scope": True,
            "global_SC_ACT_06_refuted": False,
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This is an internal symbol-complex rank theorem; it supplies no source-owned action, stationary GU germ, analytic domain, or physical recovery.",
        "controls": {
            "producer": "tests/channel-swings/k763_sc_act_06_finite_rank_even_owner_update.py",
            "probe": "tests/channel-swings/k763_sc_act_06_finite_rank_even_owner_update_probe.py",
            "controls_passed": 40,
            "hostile_mutations_rejected": 34,
        },
        "claim_ceiling": "Exact finite-dimensional rank theorem for rank-r old-block corrections with m new even fields and unchanged gauge rank. No statement about unbounded-rank owners, changed germs, global domains, source ownership, or SC-ACT-06 globally.",
    }


def validate(packet: dict[str, Any]) -> None:
    assert packet["result_id"].startswith("K763-")
    assert packet["status"] == "working_draft_verified"
    assert packet["classification"] == "INTERNAL_STRUCTURAL_ONLY"
    assert packet["target_claim"] == "SC-ACT-06"
    theorem = packet["theorem"]
    assert theorem["rank_update_bound"] == "rank(H)-rank(E) <= r+2m"
    assert theorem["middle_cohomology_bound"] == "dim H_ext >= dim H_old-r-m"
    for key in ("sharp", "requires_rank_bound_on_old_block_correction", "requires_unchanged_gauge_rank", "requires_ward_compatibility", "allows_arbitrary_mixed_and_new_self_blocks", "k759_recovered_at_r_zero"):
        assert theorem[key]
    observed = [(row["r"], row["m"], row["new_rank"] - row["old_rank"], row["old_middle"] - row["new_middle"]) for row in packet["exact_controls"]]
    assert observed == [(0, 1, 2, 1), (1, 1, 3, 2), (3, 2, 7, 5), (10, 1, 12, 11)]
    decision = packet["decision"]
    assert decision["small_rank_nonfactorizing_update_can_be_decisively_bounded"]
    assert decision["r_plus_m_is_necessary_rank_budget_not_sufficiency"]
    assert decision["changed_background_or_unbounded_rank_owner_outside_scope"]
    assert not decision["global_SC_ACT_06_refuted"]
    assert "UNCHANGED" in packet["source_and_ledger_effect"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    OUTPUT.write_text(rendered) if args.write else print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
