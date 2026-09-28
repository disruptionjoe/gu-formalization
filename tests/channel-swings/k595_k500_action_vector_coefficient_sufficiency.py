#!/usr/bin/env python3
"""K595 coefficient-sufficiency boundary for K583 direct action vectors."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k595-k500-action-vector-coefficient-sufficiency.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None: raise RuntimeError(filename)
    module = importlib.util.module_from_spec(spec); sys.modules[name] = module; spec.loader.exec_module(module); return module


K177 = load("k177_for_k595", "k177_laplace_simplex_exchange_prefix.py")


def f(x) -> Fraction: return x if isinstance(x, Fraction) else Fraction(x)
def q(x: Fraction) -> str: return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def leakage(matrix, vector) -> Fraction:
    v = [f(x) for x in vector]
    wv = [sum(f(a) * v[j] for j, a in enumerate(row)) for row in matrix]
    n = sum(x*x for x in v)
    return sum(x*x for x in wv) / n - sum(x*y for x, y in zip(v, wv))**2 / n**2


def build() -> dict:
    k177_demo = K177.demo()
    k583 = json.loads((ROOT / "lab/process/k583-k500-all-level-tensor-pair-leakage.json").read_text())
    k593 = json.loads((ROOT / "lab/process/k593-k500-native-spectral-diameter-obstruction.json").read_text())
    rows = []
    for c in (Fraction(1), Fraction(2), Fraction(5)):
        matrix = [[Fraction(0), c, Fraction(0)], [c, Fraction(0), Fraction(1)], [Fraction(0), Fraction(1), Fraction(0)]]
        value = leakage(matrix, [Fraction(1), Fraction(0), Fraction(0)])
        rows.append({"exchange_scale": q(c), "exchange_support_count": 4, "leakage_square": q(value)})
    censuses = k177_demo["boundary_word_automaton"]["seed_census"]
    native = []
    for row in censuses[:2]:
        native.append({
            "seed": row["seed"], "charge": row["charge"],
            "resolved_prefix_coordinates_through_order_12": row["total_paths_orders_0_through_12"],
            "matched_exchange_coordinates_through_order_12": row["total_matched_contractions_orders_1_through_12"],
        })
    release = k177_demo["release_test"]
    assert release["coefficient_complete_base_action_column_evaluated"] is False
    assert k583["decision"]["actual_uniform_tensor_pair_upper_emitted"] is False
    assert k593["decision"]["finite_spectral_diameter_route_survives"] is False
    return {
        "schema_version": "1.0", "result_id": "K595-K500-ACTION-VECTOR-COEFFICIENT-SUFFICIENCY", "created": "2026-09-28",
        "status": "working_draft_verified", "classification": "INTERNAL_STRUCTURAL_ONLY", "direction": "observed_to_native", "target_claim": "NONE-NOT-A-KILL",
        "scope": "The exact data needed to execute K583's vector-specific K500 leakage certificate after K593 retired a spectral-diameter bound, with K177's higher-level matched exchange topology retained.",
        "gu_typed_objects": {
            "carrier": "one K162 q00 or q10 bath-number level with cyclic vector v_n",
            "pairing": "regular positive Hilbert pairing transported from M=S* S",
            "form": "self-adjoint native normal action W_n including diagonal and K177 matched exchange contributions",
            "result": "action-vector coefficient sufficiency boundary MAP-TYPE=vector-orbit-data",
            "target": "uniform K583 ratio ||W_n v_n tensor v_n-v_n tensor W_n v_n||^2/(2||v_n||^4)",
        },
        "native_K177_inventory": {
            "rows": native,
            "orders_resolved": [0, 12],
            "exchange_topology_and_CAR_signs_serialized": True,
            "laplace_simplex_integral_representation_serialized": True,
            "coefficient_complete_base_action_column_evaluated": release["coefficient_complete_base_action_column_evaluated"],
            "outward_numerical_prefix_integrals_evaluated": release["outward_numerical_prefix_integrals_evaluated"],
            "all_levels_beyond_order_12_serialized": False,
        },
        "theorem": {
            "minimum_sufficient_data": "For each supported n it is sufficient to serialize ||v_n||^2, <v_n,W_n v_n>, and ||W_n v_n||^2, or equivalently the coefficient-weighted vector W_n v_n; the full spectrum and full matrix of W_n are unnecessary.",
            "topology_is_insufficient": "Exchange-coordinate counts, support and CAR signs do not bound the coefficient-weighted action vector without amplitude estimates.",
            "fixed_support_scaling_family": "W_c=[[0,c,0],[c,0,1],[0,1,0]], v=e0 has the same four off-diagonal support entries for every nonzero c, but lambda(W_c,v)^2=c^2.",
            "spectral_diameter_not_required": True,
            "full_operator_matrix_not_required": True,
            "coefficient_weighted_action_vector_required": True,
        },
        "exact_controls": {
            "fixed_support_family": rows,
            "all_rows_same_exchange_support_count": len({r["exchange_support_count"] for r in rows}) == 1,
            "leakage_squares": [r["leakage_square"] for r in rows],
            "leakage_changes_with_amplitude": len({r["leakage_square"] for r in rows}) == len(rows),
            "expected_square_law": [r["leakage_square"] for r in rows] == ["1", "4", "25"],
        },
        "decision": {
            "K583_direct_vector_route_preserved": True,
            "K593_spectral_diameter_route_reopened": False,
            "K177_support_census_alone_bounds_leakage": False,
            "required_successor_narrowed_to_three_moments_or_action_vector": True,
            "complete_K500_uniform_leakage_emitted": False,
            "native_noncyclic_floor_emitted": False,
            "K473_released": False, "native_K152_interval_emitted": False,
            "next_exact_input": "Evaluate the coefficient-weighted K177 action column W_n v_n, with rigorous exchange-amplitude integrals and tail control, and bound its three normalized moments uniformly; do not construct the unused full W_n matrix or return to spectral diameter.",
        },
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "After K593, test whether K177 already contains the vector-specific amplitudes needed by K583 before launching an all-level operator enclosure.",
            "retrieval_collision_result": "K177 serializes exchange paths, signs and integral representations through order twelve, but explicitly leaves the coefficient-complete base action column unevaluated.",
            "strongest_alternative": "Bounding the full operator matrix or spectrum is stronger and more expensive than K583 requires; three moments of W_n v_n suffice.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating exchange counts as amplitude bounds, or calling a twelve-order topology census an all-level vector estimate.",
            "strongest_contrary_construction": "The fixed-support W_c family has identical support topology and arbitrarily different leakage, so coefficient amplitudes are load-bearing.",
            "weakest_reproducibility_seam": "The successor still needs rigorous continuum exchange integrals and an all-level tail; K595 narrows the data object but does not evaluate it.",
        },
        "claim_ceiling": "Exact data-sufficiency boundary for K583: the complete spectrum and full W_n matrix are unnecessary; the three moments ||v_n||^2, <v_n,W_n v_n> and ||W_n v_n||^2, equivalently W_n v_n, suffice. K177's support/sign/path census through order twelve does not serialize the coefficient-weighted action column, and identical exchange support can have leakage squares 1,4,25 under amplitude scaling. Thus the direct vector route remains live but no uniform K500 bound, noncyclic floor, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty or physical conclusion is emitted.",
    }


def validate(p: dict) -> None:
    n, t, c, d = p["native_K177_inventory"], p["theorem"], p["exact_controls"], p["decision"]
    assert n["exchange_topology_and_CAR_signs_serialized"] and n["laplace_simplex_integral_representation_serialized"]
    assert not n["coefficient_complete_base_action_column_evaluated"] and not n["outward_numerical_prefix_integrals_evaluated"] and not n["all_levels_beyond_order_12_serialized"]
    assert t["spectral_diameter_not_required"] and t["full_operator_matrix_not_required"] and t["coefficient_weighted_action_vector_required"]
    assert c["all_rows_same_exchange_support_count"] and c["leakage_changes_with_amplitude"] and c["expected_square_law"]
    assert d["K583_direct_vector_route_preserved"] and not d["K593_spectral_diameter_route_reopened"] and not d["K177_support_census_alone_bounds_leakage"]
    assert d["required_successor_narrowed_to_three_moments_or_action_vector"]
    assert not any(d[k] for k in ("complete_K500_uniform_leakage_emitted", "native_noncyclic_floor_emitted", "K473_released", "native_K152_interval_emitted"))


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true"); args = parser.parse_args()
    p = build(); validate(p); rendered = json.dumps(p, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
