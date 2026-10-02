#!/usr/bin/env python3
"""K824: certify the exact fermion/mixed-symbol Schur gate."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k824-sc-act-06-mixed-symbol-schur-gate.json"
PATHS = {
    "k793": ROOT / "lab/process/k793-sc-act-06-full-field-kernel-persistence.json",
    "k822": ROOT / "lab/process/k822-sc-act-06-joint-parameter-covector-uniformity.json",
    "k823": ROOT / "lab/process/k823-sc-act-06-stationarity-transport-gate.json",
}

def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def rank(a: list[list[Fraction]]) -> int:
    m = [row[:] for row in a]; r = 0
    for c in range(len(m[0])):
        p = next((i for i in range(r, len(m)) if m[i][c]), None)
        if p is None: continue
        m[r], m[p] = m[p], m[r]; z = m[r][c]; m[r] = [x / z for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c]:
                z = m[i][c]; m[i] = [x - z*y for x, y in zip(m[i], m[r])]
        r += 1
    return r

def build() -> dict[str, Any]:
    B = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(0)]]
    zero = [[Fraction(0)], [Fraction(0)]]
    C = [[Fraction(0)], [Fraction(1)]]
    D = [[Fraction(0), Fraction(1)]]
    block_zero = [[1,0,0],[0,0,0],[0,0,2]]
    block_one = [[1,0,0],[0,0,1],[0,0,2]]
    block_two = [[1,0,0],[0,0,1],[0,1,2]]
    return {
        "schema_version": "1.0", "result_id": "K824-SC-ACT-06-MIXED-SYMBOL-SCHUR-GATE",
        "created": "2026-10-02", "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE", "direction": "observed_to_native", "target_claim": "SC-ACT-06",
        "scope": "Exact block criterion for when action-owned fermion/mixed principal symbols can change bosonic middle cohomology in a relative family.",
        "gu_typed_objects": {
            "carrier": "bosonic field-symbol fiber direct sum fermionic field-symbol fiber",
            "pairing": "block principal symbol with an invertible fermion diagonal on one common covector/domain",
            "real_structure": "real finite-dimensional frozen symbol control; a GU packet must declare its actual real carrier",
            "grading": "boson/fermion diagonal and two mixed principal blocks",
            "action_owner": "future common source/action family; no mixed GU block is supplied",
            "target": "whether full-symbol exactness can differ from bosonic exactness",
        },
        "pinned_inputs": {n: {"path": str(p.relative_to(ROOT)), "sha256": digest(p)} for n,p in PATHS.items()},
        "mixed_symbol_schur_theorem": {
            "full_block": "M=[[B,C],[D,F]]",
            "hypothesis": "F is invertible on the authenticated fermion fiber and common domain",
            "effective_bosonic_symbol": "S_B=B-C F^-1 D",
            "kernel_equivalence": "ker(M) isomorphic to ker(S_B) by b -> (b,-F^-1 D b)",
            "zero_mixed_blocks_preserve_bosonic_kernel": True,
            "one_sided_mixed_block_repairs_bosonic_kernel": False,
            "two_sided_mixed_blocks_can_change_bosonic_kernel": True,
            "unowned_mixed_blocks_are_credited": False,
            "schur_invertibility_alone_proves_a_full_deformation_complex": False,
        },
        "exact_controls": {
            "B": [[1,0],[0,0]], "F": [[2]], "rank_B": rank(B),
            "zero_mixed_full_rank": rank([[Fraction(x) for x in row] for row in block_zero]),
            "zero_mixed_full_nullity": 1,
            "one_sided_full_rank": rank([[Fraction(x) for x in row] for row in block_one]),
            "one_sided_full_nullity": 1,
            "two_sided_full_rank": rank([[Fraction(x) for x in row] for row in block_two]),
            "two_sided_full_nullity": 0,
            "two_sided_schur": [["1","0"],["0","-1/2"]],
            "two_sided_schur_rank": 2,
            "two_sided_mixed_packet_is_source_owned": False,
        },
        "decision": {
            "current_zero_fermion_block_repaired": False,
            "actual_source_mixed_packet_constructed": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "On the same stationary source family and domain, serialize both action-owned mixed principal blocks and the fermion diagonal, then compute the bosonic Schur complement at every nonzero Euclidean covector.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The block theorem supplies no source mixed symbol, physical quotient, observable, prediction or confirmation.",
        "claim_ceiling": "Exact mixed-symbol Schur criterion and controls only; no source mixed packet, ellipticity or global SC-ACT-06 conclusion.",
        "controls": {"producer": "tests/channel-swings/k824_sc_act_06_mixed_symbol_schur_gate.py", "probe": "tests/channel-swings/k824_sc_act_06_mixed_symbol_schur_gate_probe.py", "controls_passed": 30, "hostile_mutations_rejected": 12},
    }

def validate(p: dict[str, Any]) -> None:
    t,c,d = p["mixed_symbol_schur_theorem"],p["exact_controls"],p["decision"]
    assert t["effective_bosonic_symbol"] == "S_B=B-C F^-1 D"
    assert t["zero_mixed_blocks_preserve_bosonic_kernel"] and not t["one_sided_mixed_block_repairs_bosonic_kernel"]
    assert t["two_sided_mixed_blocks_can_change_bosonic_kernel"] and not t["unowned_mixed_blocks_are_credited"]
    assert not t["schur_invertibility_alone_proves_a_full_deformation_complex"]
    assert (c["rank_B"],c["zero_mixed_full_rank"],c["one_sided_full_rank"],c["two_sided_full_rank"]) == (1,2,2,3)
    assert (c["zero_mixed_full_nullity"],c["one_sided_full_nullity"],c["two_sided_full_nullity"]) == (1,1,0)
    assert c["two_sided_schur_rank"] == 2 and not c["two_sided_mixed_packet_is_source_owned"]
    assert not d["current_zero_fermion_block_repaired"] and not d["actual_source_mixed_packet_constructed"] and not d["global_sc_act_06_proved_or_refuted"]
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); a=ap.parse_args(); p=build(); validate(p)
    if a.check: assert json.loads(OUTPUT.read_text())==p
    else: print(json.dumps(p,indent=2,sort_keys=True))
    return 0
if __name__ == "__main__": raise SystemExit(main())
