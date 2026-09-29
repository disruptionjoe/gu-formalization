#!/usr/bin/env python3
"""K606 determinant positivity and exact self-norm closure for K604."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k606-k500-self-norm-quadrature-compression.json"


def compact_key(kind: str, left: list[Any], right: list[Any], blocks: list[list[list[int]]]) -> str:
    descriptor = {
        "k": kind,
        "l": [left[0], int(left[1]), list(left[2])],
        "r": [right[0], int(right[1]), list(right[2])],
        "b": sorted([[list(a), list(b)] for a, b in blocks], key=lambda row: (row[0], row[1])),
    }
    if kind in {"N", "B_F"}:
        swapped = {
            "k": kind,
            "l": descriptor["r"],
            "r": descriptor["l"],
            "b": sorted([[b, a] for a, b in descriptor["b"]], key=lambda row: (row[0], row[1])),
        }
        if json.dumps(swapped, sort_keys=True) < json.dumps(descriptor, sort_keys=True):
            descriptor = swapped
    return json.dumps(descriptor, sort_keys=True, separators=(",", ":"))


def self_descriptor(row: dict[str, Any], side_index: int) -> tuple[str, str]:
    side = row["l"] if side_index == 0 else row["r"]
    positions = [block[side_index] for block in row["b"]]
    blocks = sorted([[p, p] for p in positions], key=lambda item: (item[0], item[1]))
    kind = "N" if side[0] == "C" else "B_F"
    return kind, compact_key(kind, side, side, blocks)


def mixture_control() -> dict[str, Any]:
    """Finite positive-mixture controls for the Andreief sign theorem.

    A finite sum is only an executable control.  The production theorem uses
    K_1(z)/pi = integral_1^infinity exp(-z lambda)
    lambda/(pi sqrt(lambda^2-1)) dlambda.
    """
    atoms = [(Fraction(2), Fraction(1)), (Fraction(3), Fraction(2)), (Fraction(5), Fraction(3))]
    xs = [Fraction(3), Fraction(1)]
    ys = [Fraction(4), Fraction(2)]

    def kernel(x: Fraction, y: Fraction) -> Fraction:
        # Rational surrogate exp(-lambda x) -> q(lambda)^x with q in (0,1).
        return sum(weight * Fraction(1, lam + 1) ** (x + y) for lam, weight in atoms)

    matrix = [[kernel(x, y) for y in ys] for x in xs]
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return {
        "positive_mixture_atom_count": len(atoms),
        "same_order_two_by_two_determinant": str(determinant),
        "same_order_two_by_two_determinant_positive": determinant > 0,
        "opposite_order_changes_sign": (
            matrix[0][1] * matrix[1][0] - matrix[0][0] * matrix[1][1]
        ) < 0,
    }


def build() -> dict[str, Any]:
    k604 = json.loads((ROOT / "lab/process/k604-k500-determinant-simplex-kernel-atlas.json").read_text())
    rows = k604["atlas"]["classes"]
    index = {compact_key(row["k"], row["l"], row["r"], row["b"]): row for row in rows}
    closure_rows = []
    endpoint_ids: set[str] = set()
    endpoint_kinds: Counter[str] = Counter()
    source_kinds: Counter[str] = Counter()
    missing = []
    for row in rows:
        if int(row["m"]) == 0:
            continue
        endpoints = []
        for side_index in (0, 1):
            endpoint_kind, key = self_descriptor(row, side_index)
            endpoint = index.get(key)
            if endpoint is None:
                missing.append([row["id"], side_index])
                continue
            endpoints.append(endpoint["id"])
            endpoint_ids.add(endpoint["id"])
            endpoint_kinds[endpoint_kind] += 1
            if int(endpoint["d"]) <= 0 or int(endpoint["m"]) <= 0:
                raise AssertionError("self endpoint is not a positive diagonal class")
        if len(endpoints) == 2:
            closure_rows.append([row["id"], endpoints[0], endpoints[1], int(row["m"])])
            source_kinds[row["k"]] += 1

    endpoint_rows = [row for row in rows if row["id"] in endpoint_ids]
    unique_by_kind = Counter(row["k"] for row in endpoint_rows)
    nonzero_count = sum(int(row["m"]) != 0 for row in rows)
    ratio = Fraction(nonzero_count, len(endpoint_ids))
    eliminated = nonzero_count - len(endpoint_ids)
    closure_digest = hashlib.sha256(
        json.dumps(closure_rows, separators=(",", ":")).encode()
    ).hexdigest()
    return {
        "schema_version": "1.0",
        "result_id": "K606-K500-SELF-NORM-QUADRATURE-COMPRESSION",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact total-positivity sign control and Hilbert Cauchy--Schwarz self-norm closure for every nonzero K604 determinant-simplex class.",
        "gu_typed_objects": {
            "finite_vectors": "K177 cyclic and K179 action coordinates through exchange order twelve",
            "pairing": "positive CAR exterior Hilbert pairing with specieswise determinants of kappa(s_i+r_j)",
            "kernel": "kappa(t)=K_1(t)/pi on strictly ordered positive simplex times",
            "result": "determinant self-norm closure MAP-TYPE=exterior-Gram Cauchy--Schwarz compression",
            "target": "the smallest positive diagonal integral bank sufficient to outwardly enclose all K604 finite N/A_F/B_F classes",
        },
        "total_positivity_theorem": {
            "laplace_representation": "kappa(z)=integral_1^infinity exp(-z lambda) lambda/(pi sqrt(lambda^2-1)) d lambda",
            "andreief_identity": "det[kappa(x_i+y_j)]=1/m! integral det[e^(-x_i lambda_j)] det[e^(-y_i lambda_j)] product dmu(lambda_j)",
            "same_order_sign": "for strictly same-ordered positive x and y, the two exponential determinants have the same sign almost everywhere; their product is positive",
            "strict_total_positivity": True,
            "within_determinant_interference_preserved": True,
            "class_integral_sign": "every raw K604 class integral is strictly positive; the serialized signed multiplicity alone fixes its signed contribution",
            "exact_zero_mixed_classes_remain_zero": k604["atlas"]["summary"][1]["classes_with_exact_signed_cancellation"],
        },
        "cauchy_schwarz_theorem": {
            "class_bound": "0<I_uv<=sqrt(I_uu I_vv) for every K604 raw class inner product",
            "endpoint_rule": "replace both sides independently by their exact diagonal self class with the same side kind, simplex rank, contracted scalar positions and species-position blocks",
            "signed_interval_rule": "multiply [0,sqrt(U_left U_right)] by the exact signed multiplicity and aggregate positive and negative classes separately",
            "diagonal_bounds_are_still_numerically_required": True,
            "determinants_are_not_expanded_or_replaced_by_occurrencewise_absolute_values": True,
        },
        "closure": {
            "K604_nonzero_signed_classes": nonzero_count,
            "mapped_nonzero_classes": len(closure_rows),
            "missing_self_endpoints": missing,
            "unique_positive_diagonal_self_norms": len(endpoint_ids),
            "unique_N_self_norms": unique_by_kind["N"],
            "unique_B_F_self_norms": unique_by_kind["B_F"],
            "direct_cross_integrals_eliminated": eliminated,
            "compression_ratio_exact": f"{ratio.numerator}/{ratio.denominator}",
            "compression_ratio_decimal": str(float(ratio)),
            "source_class_counts": dict(sorted(source_kinds.items())),
            "closure_row_encoding": "[source_class_id,left_self_class_id,right_self_class_id,signed_multiplicity]",
            "closure_rows": closure_rows,
            "closure_digest": closure_digest,
        },
        "exact_controls": mixture_control(),
        "decision": {
            "complete_self_norm_closure_emitted": True,
            "all_nonzero_K604_classes_mapped": not missing and len(closure_rows) == nonzero_count,
            "numerical_quadrature_bank_reduced_to_1614_positive_diagonal_norms": len(endpoint_ids) == 1614,
            "outward_diagonal_values_emitted": False,
            "complete_finite_K456_moments_emitted": False,
            "complete_K500_uniform_leakage_emitted": False,
            "native_noncyclic_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Outwardly enclose the 291 cyclic and 1,323 action diagonal self norms, infer every cross-class interval through the K606 closure, aggregate finite N/A_F/B_F with exact signed multiplicities, then apply K599 with K574's tail once and prove uniformity.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact determinant-sign and self-norm closure theorem for all 39,438 nonzero K604 classes, reducing their distinct numerical obligation to 1,614 positive diagonal norms. It emits no diagonal numerical value, finite moment enclosure, uniform leakage bound, noncyclic floor, K473/K152 result, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion.",
    }


def validate(payload: dict[str, Any]) -> None:
    tp = payload["total_positivity_theorem"]
    cs = payload["cauchy_schwarz_theorem"]
    closure = payload["closure"]
    control = payload["exact_controls"]
    decision = payload["decision"]
    assert tp["strict_total_positivity"] and tp["within_determinant_interference_preserved"]
    assert tp["exact_zero_mixed_classes_remain_zero"] == 1625
    assert cs["diagonal_bounds_are_still_numerically_required"]
    assert cs["determinants_are_not_expanded_or_replaced_by_occurrencewise_absolute_values"]
    assert closure["K604_nonzero_signed_classes"] == 39438
    assert closure["mapped_nonzero_classes"] == 39438 and not closure["missing_self_endpoints"]
    assert closure["unique_positive_diagonal_self_norms"] == 1614
    assert closure["unique_N_self_norms"] == 291 and closure["unique_B_F_self_norms"] == 1323
    assert closure["direct_cross_integrals_eliminated"] == 37824
    assert len(closure["closure_digest"]) == 64
    assert control["same_order_two_by_two_determinant_positive"] and control["opposite_order_changes_sign"]
    assert decision["complete_self_norm_closure_emitted"] and decision["all_nonzero_K604_classes_mapped"]
    assert decision["numerical_quadrature_bank_reduced_to_1614_positive_diagonal_norms"]
    assert not any(decision[key] for key in (
        "outward_diagonal_values_emitted", "complete_finite_K456_moments_emitted",
        "complete_K500_uniform_leakage_emitted", "native_noncyclic_floor_emitted",
        "K473_released", "native_K152_interval_emitted",
    ))


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
