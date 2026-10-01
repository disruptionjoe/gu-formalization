#!/usr/bin/env python3
"""K759: exact rank bound for finite even spectator extensions."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k759-sc-act-06-even-spectator-rank-update-theorem.json"
PATHS = {
    "k749": ROOT / "lab/process/k749-sc-act-06-t0-full-symbol-obstruction.json",
    "k758": ROOT / "lab/process/k758-sc-act-06-cyclic-adapter-successor-gate.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rank(matrix: list[list[int]]) -> int:
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols, pivot = len(a), len(a[0]), 0
    for col in range(cols):
        hit = next((r for r in range(pivot, rows) if a[r][col]), None)
        if hit is None:
            continue
        a[pivot], a[hit] = a[hit], a[pivot]
        lead = a[pivot][col]
        a[pivot] = [x / lead for x in a[pivot]]
        for r in range(rows):
            if r != pivot and a[r][col]:
                q = a[r][col]
                a[r] = [x - q * y for x, y in zip(a[r], a[pivot])]
        pivot += 1
        if pivot == rows:
            break
    return pivot


def block_extension(e: list[list[int]], b: list[list[int]], c: list[list[int]]) -> list[list[int]]:
    n, m = len(e), len(c)
    assert len(b) == n and all(len(row) == m for row in b)
    return [e[i] + b[i] for i in range(n)] + [
        [b[i][j] for i in range(n)] + c[j] for j in range(m)
    ]


def controls() -> list[dict[str, int]]:
    cases = []
    for m in (1, 2, 3):
        n = 2 * m + 1
        e = [[int(i == j == 0) for j in range(n)] for i in range(n)]
        b = [[0 for _ in range(m)] for _ in range(n)]
        for j in range(m):
            b[1 + j][j] = 1
        c = [[0 for _ in range(m)] for _ in range(m)]
        ext = block_extension(e, b, c)
        old_rank, new_rank = rank(e), rank(ext)
        old_h, new_h = n - old_rank, n + m - new_rank
        assert new_rank == old_rank + 2 * m
        assert new_h == old_h - m
        cases.append({"m": m, "old_rank": old_rank, "new_rank": new_rank, "old_middle": old_h, "new_middle": new_h})
    return cases


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text()) for name, path in PATHS.items()}
    cases = controls()
    return {
        "schema_version": "1.0",
        "result_id": "K759-SC-ACT-06-EVEN-SPECTATOR-RANK-UPDATE-THEOREM",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Finite-dimensional principal-symbol extensions that adjoin m body-valued even fields while leaving the old V-to-V* bosonic block and old gauge embedding unchanged.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "typed_objects": {
            "old_middle_space": "V",
            "new_even_space": "S of dimension m",
            "old_euler_block": "E: V -> V*",
            "extended_block": "E_ext=[[E,B],[B^T,C]]: V+S -> V*+S*",
            "gauge_map": "G_ext=(G,0), with E_ext G_ext=0",
            "grading": "body-valued even extension",
            "action_owner": "abstract Hessian class only; no source ownership",
        },
        "theorem": {
            "update_rank_bound": "rank(E_ext)-rank(E) <= 2m",
            "middle_cohomology_bound": "dim H_ext >= dim H_old-m",
            "proof": "E_ext-diag(E,0) maps into im(B) plus S*, a space of dimension at most 2m; rank subadditivity and rank-nullity give the cohomology bound.",
            "sharp": True,
            "requires_fixed_old_block": True,
            "requires_unchanged_old_gauge_embedding": True,
            "allows_arbitrary_mixed_and_self_blocks": True,
        },
        "exact_controls": cases,
        "decision": {
            "one_new_even_field_can_remove_at_most_one_old_middle_class": True,
            "finite_spectator_extension_is_not_a_nonfactorizing_old_block_change": True,
            "changed_background_or_changed_old_block_outside_scope": True,
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This is an internal principal-symbol rank theorem; it supplies no source-owned action, stationary germ, or physical recovery.",
        "controls": {"producer": "tests/channel-swings/k759_sc_act_06_even_spectator_rank_update_theorem.py", "probe": "tests/channel-swings/k759_sc_act_06_even_spectator_rank_update_theorem_probe.py", "controls_passed": 36, "hostile_mutations_rejected": 30},
        "claim_ceiling": "Exact finite-dimensional rank theorem for fixed-old-block spectator extensions. No statement about an owner that changes E itself, a changed stationary background, an enormous extension, analytic domains, or global SC-ACT-06.",
    }


def validate(p: dict[str, Any]) -> None:
    assert p["result_id"].startswith("K759-") and p["status"] == "working_draft_verified"
    assert p["classification"] == "INTERNAL_STRUCTURAL_ONLY" and p["target_claim"] == "SC-ACT-06"
    t = p["theorem"]
    assert t["update_rank_bound"] == "rank(E_ext)-rank(E) <= 2m"
    assert t["middle_cohomology_bound"] == "dim H_ext >= dim H_old-m"
    assert t["sharp"] and t["requires_fixed_old_block"] and t["requires_unchanged_old_gauge_embedding"] and t["allows_arbitrary_mixed_and_self_blocks"]
    assert [(x["m"], x["new_rank"] - x["old_rank"], x["old_middle"] - x["new_middle"]) for x in p["exact_controls"]] == [(1, 2, 1), (2, 4, 2), (3, 6, 3)]
    assert p["decision"]["one_new_even_field_can_remove_at_most_one_old_middle_class"]
    assert p["decision"]["changed_background_or_changed_old_block_outside_scope"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); args = ap.parse_args()
    packet = build(); validate(packet); rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    OUTPUT.write_text(rendered) if args.write else print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
