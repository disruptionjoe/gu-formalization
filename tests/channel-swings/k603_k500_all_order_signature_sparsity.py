#!/usr/bin/env python3
"""K603 exact signature sparsity for K500 finite cyclic/action moments."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k603-k500-all-order-signature-sparsity.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K179 = load("k179_for_k603", "k179_matched_normal_order_coefficient_family.py")
K177 = K179.K177


def signature_text(word) -> str:
    impurity, counts = K177.signature(word)
    return f"d={impurity}|" + ",".join(f"{label}^{count}" for label, count in counts)


def order_seed_row(seed: int, order: int, terms: list[dict[str, Any]]) -> dict[str, Any]:
    cyclic = Counter(signature_text(word) for word in K177.words(seed, order))
    action = Counter(term["output_signature"] for term in terms if int(term["seed_impurity"]) == seed and int(term["order"]) == order)
    signatures = sorted(set(cyclic) | set(action))
    overlap_pairs = sum(cyclic[sig] * action[sig] for sig in signatures)
    cyclic_pairs = sum(count * (count + 1) // 2 for count in cyclic.values())
    action_pairs = sum(count * (count + 1) // 2 for count in action.values())
    total_overlap_pairs = sum(cyclic.values()) * sum(action.values())
    total_cyclic_pairs = sum(cyclic.values()) * (sum(cyclic.values()) + 1) // 2
    total_action_pairs = sum(action.values()) * (sum(action.values()) + 1) // 2
    return {
        "seed_impurity": seed,
        "charge": list(K177.charges(seed, ())),
        "order": order,
        "cyclic_paths": sum(cyclic.values()),
        "action_terms": sum(action.values()),
        "cyclic_signatures": len(cyclic),
        "action_signatures": len(action),
        "shared_signatures": sum(cyclic[sig] > 0 and action[sig] > 0 for sig in signatures),
        "cyclic_norm_pairs_surviving": cyclic_pairs,
        "cyclic_norm_pairs_total": total_cyclic_pairs,
        "cyclic_action_pairs_surviving": overlap_pairs,
        "cyclic_action_pairs_total": total_overlap_pairs,
        "action_norm_pairs_surviving": action_pairs,
        "action_norm_pairs_total": total_action_pairs,
        "cyclic_action_exact_zero_pairs": total_overlap_pairs - overlap_pairs,
        "signature_blocks": [
            {"signature": sig, "cyclic_multiplicity": cyclic[sig], "action_multiplicity": action[sig]}
            for sig in signatures if cyclic[sig] or action[sig]
        ],
    }


def build() -> dict[str, Any]:
    terms = K179.coefficient_family()
    rows = [order_seed_row(seed, order, terms) for order in range(2, 13) for seed in (0, 1, 2)]
    order_rows = []
    for order in range(2, 13):
        group = [row for row in rows if row["order"] == order]
        order_rows.append({
            "order": order,
            "cyclic_paths": sum(row["cyclic_paths"] for row in group),
            "action_terms": sum(row["action_terms"] for row in group),
            "cyclic_action_pairs_surviving": sum(row["cyclic_action_pairs_surviving"] for row in group),
            "cyclic_action_pairs_total": sum(row["cyclic_action_pairs_total"] for row in group),
            "cyclic_action_exact_zero_pairs": sum(row["cyclic_action_exact_zero_pairs"] for row in group),
            "action_norm_pairs_surviving": sum(row["action_norm_pairs_surviving"] for row in group),
        })
    total_possible = sum(row["cyclic_action_pairs_total"] for row in rows)
    total_surviving = sum(row["cyclic_action_pairs_surviving"] for row in rows)
    return {
        "schema_version": "1.0",
        "result_id": "K603-K500-ALL-ORDER-SIGNATURE-SPARSITY",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact impurity/exterior-signature sparsity of K177 cyclic vectors and K179 finite exchange action vectors for q00/q10/q01 through order twelve.",
        "gu_typed_objects": {
            "cyclic_vectors": "the K177 G^n path coordinates for the three K162 zero-bath seeds",
            "action_vectors": "the coefficient-complete K179 matched-exchange coordinates through order twelve",
            "pairing": "normalized CAR exterior pairing, orthogonal across unequal impurity or species multiplicity signatures",
            "result": "finite-moment sparsity atlas MAP-TYPE=orthogonal-sector-decomposition",
            "target": "the surviving N, A_F and B_F Gram blocks required by K599",
        },
        "theorem": {
            "zero_rule": "Different output impurity or exterior species-multiplicity signatures are exactly orthogonal.",
            "cyclic_norm_pairs": "sum_s c_s(c_s+1)/2",
            "cyclic_action_pairs": "sum_s c_s a_s",
            "action_norm_pairs": "sum_s a_s(a_s+1)/2",
            "surviving_pair_is_not_evaluated": True,
            "coefficient_signs_and_within_block_determinants_remain_required": True,
        },
        "order_summary": order_rows,
        "seed_order_rows": rows,
        "complete_census": {
            "orders": [2, 12],
            "seed_order_blocks": len(rows),
            "cyclic_paths": sum(row["cyclic_paths"] for row in rows),
            "action_terms": sum(row["action_terms"] for row in rows),
            "cyclic_action_pairs_total": total_possible,
            "cyclic_action_pairs_surviving": total_surviving,
            "cyclic_action_exact_zero_pairs": total_possible - total_surviving,
            "exact_zero_fraction": f"{total_possible-total_surviving}/{total_possible}",
            "all_2958_action_terms_retained": sum(row["action_terms"] for row in rows) == 2958,
        },
        "decision": {
            "order_two_through_twelve_signature_sparsity_complete": True,
            "exact_zero_cyclic_action_products_removed_before_quadrature": True,
            "surviving_higher_order_moments_numerically_evaluated": False,
            "complete_finite_K456_moments_emitted": False,
            "complete_K500_uniform_leakage_emitted": False,
            "native_noncyclic_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Group the surviving order-three-through-twelve cyclic/action pairs by their determinant-simplex kernel, outwardly enclose each distinct block with coefficient signs retained, and compose N/A_F/B_F before K599 and K574 are applied once.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact finite orthogonality and sparsity atlas through order twelve. It removes only products forced to zero by impurity/exterior signatures; it does not evaluate any surviving higher-order moment, control within-block interference, prove a uniform K500 bound, supply the noncyclic floor, release K473/K152, or move source, ledger, canon, paper, public, novelty or physical conclusions.",
    }


def validate(payload: dict[str, Any]) -> None:
    census = payload["complete_census"]
    assert census["seed_order_blocks"] == 33 and census["all_2958_action_terms_retained"]
    assert census["cyclic_action_pairs_total"] == census["cyclic_action_pairs_surviving"] + census["cyclic_action_exact_zero_pairs"]
    assert census["cyclic_action_exact_zero_pairs"] > 0
    order_two = [row for row in payload["seed_order_rows"] if row["order"] == 2]
    assert [row["cyclic_action_pairs_surviving"] for row in order_two] == [2, 1, 1]
    decision = payload["decision"]
    assert decision["order_two_through_twelve_signature_sparsity_complete"] and decision["exact_zero_cyclic_action_products_removed_before_quadrature"]
    assert not any(decision[key] for key in ("surviving_higher_order_moments_numerically_evaluated", "complete_finite_K456_moments_emitted", "complete_K500_uniform_leakage_emitted", "native_noncyclic_floor_emitted", "K473_released", "native_K152_interval_emitted"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
