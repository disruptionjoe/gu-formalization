#!/usr/bin/env python3
"""K507 native cancellation-free path lower bound for the K177 family."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K177_PATH = HERE / "k177_laplace_simplex_exchange_prefix.py"
OUTPUT = ROOT / "lab/process/k507-k500-native-car-path-positivity.json"


def load_k177():
    spec = importlib.util.spec_from_file_location("k177_for_k507", K177_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K177_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K177 = load_k177()


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def expected_signature_blocks(seed: int, order: int) -> int:
    if order == 0:
        return 1
    if seed == 0:
        return order // 2 + 1 if order % 2 == 0 else order + 1
    return (order + 1) // 2 if order % 2 == 1 else order


def census(maximum_order: int = 12) -> tuple[list[dict[str, Any]], int, int]:
    rows: list[dict[str, Any]] = []
    total_paths = 0
    total_blocks = 0
    for seed in (0, 1, 2):
        for order in range(maximum_order + 1):
            groups: dict[Any, list[int]] = defaultdict(list)
            for word in K177.words(seed, order):
                _, sign = K177.build_state(word, order + 1)
                groups[K177.signature(word)].append(sign)
            signs_constant = all(len(set(signs)) == 1 for signs in groups.values())
            expected_paths = K177.expected_path_count(seed, order)
            expected_blocks = expected_signature_blocks(seed, order)
            if len(K177.words(seed, order)) != expected_paths or len(groups) != expected_blocks:
                raise AssertionError("K507 closed path/signature census failed")
            if not signs_constant:
                raise AssertionError("K507 found a mixed CAR sign inside one native occupation block")
            row = {
                "seed_impurity": seed,
                "order": order,
                "path_count": expected_paths,
                "occupation_signature_blocks": len(groups),
                "expected_signature_blocks": expected_blocks,
                "maximum_paths_in_one_signature": max(len(group) for group in groups.values()),
                "all_paths_in_each_signature_have_one_CAR_sign": signs_constant,
            }
            rows.append(row)
            total_paths += expected_paths
            total_blocks += len(groups)
    return rows, total_paths, total_blocks


def cauchy_moment_control() -> dict[str, Any]:
    # K(s,r)=int_0^infty exp(-(s+r)x)dx=1/(s+r).
    s = [Fraction(3), Fraction(1)]
    r = [Fraction(4), Fraction(2)]
    matrix = [[1 / (left + right) for right in r] for left in s]
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    reversed_r = list(reversed(r))
    hostile = [[1 / (left + right) for right in reversed_r] for left in s]
    hostile_determinant = hostile[0][0] * hostile[1][1] - hostile[0][1] * hostile[1][0]
    return {
        "kernel": "K(s,r)=int_0^infinity exp(-(s+r)x) dx=1/(s+r)",
        "same_order_matrix": [[q(value) for value in row] for row in matrix],
        "same_order_determinant": q(determinant),
        "same_order_determinant_positive": determinant > 0,
        "one_order_reversed_determinant": q(hostile_determinant),
        "one_order_reversed_rejected": hostile_determinant < 0,
    }


def build() -> dict[str, Any]:
    rows, total_paths, total_blocks = census()
    control = cauchy_moment_control()
    return {
        "schema_version": "1.0",
        "result_id": "K507-K500-NATIVE-CAR-PATH-POSITIVITY",
        "created": "2026-09-25",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The exact K177 equal-coupling positive-Fock continuum path family for K139/K162 q00, q10 and flavor-related q01 seed orbits; arbitrary CAR decompositions and unequal or signed couplings are excluded.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_comparator_classification": "INTERNAL_ONLY__NO_SOURCE_NATIVE_OR_CONVENTIONAL_PARTICLE_VERDICT",
        "gu_typed_objects": {
            "carrier": "K177 hard-core C3 tensor fermionic Fock continuum path ranges",
            "pairing": "positive regular-coordinate Hilbert pairing transported from M=S* S",
            "form": "path Gram of K139 Neumann words before K500 normal-action leakage",
            "real_structure": "CAR adjoint on fixed q00/q10/q01 charge sectors",
            "grading": "bath number, output impurity and four bath-species occupation counts",
            "action_owner": "repository-supplied conditional equal-coupling operator; no source/GU action selection",
            "result": "native coherent-path lower reduction MAP-TYPE=positive-Gram-ray-bound",
            "target": "K506 word-norm lower-envelope input for K500",
        },
        "all_order_theorem": {
            "block_parity": "Every admitted K177 transition contains two odd CAR factors and has even fermion parity; a completed flavor cycle returns the impurity to zero and swapping completed cycles changes no CAR sign.",
            "signature_sign": "Paths with the same output impurity and bath-species occupation counts differ only by permutations of completed even cycles, so their global CAR sign is identical.",
            "orthogonal_blocks": "Different occupation signatures are orthogonal Fock sectors.",
            "heat_kernel": "kappa(t)=int_R exp(-t*sqrt(1+p^2)) dp/(2*pi)=K_1(t)/pi",
            "andreief_identity": "det[kappa(s_i+r_j)]=(1/m!)*int det[exp(-s_i E_k)] det[exp(-r_j E_k)] product_k dnu(E_k)",
            "moment_positivity": "When s and r use the same strict order, the two exponential determinants have the same fixed sign; their product is nonnegative and is positive off collision sets.",
            "native_cross_terms": "Positive Laplace weights, common CAR sign and specieswise moment determinants make every same-signature path cross inner product nonnegative.",
            "word_lower": "For v_n=sum_p x_(n,p), ||v_n||^2=sum_signature sum_(p,q)<x_p,x_q> >= sum_p ||x_p||^2 >= ||x_(n,p0)||^2 for every selected nonzero native path p0.",
            "K506_specialization": "The complete normalized-Gram eigenvalue is unnecessary for the actual all-ones native coefficient ray; entrywise positivity on that ray supplies the lower bound.",
        },
        "exact_controls": {
            "maximum_order": 12,
            "seed_order_rows": rows,
            "resolved_path_records": total_paths,
            "resolved_occupation_signature_blocks": total_blocks,
            "all_39_seed_order_blocks_match_closed_counts": len(rows) == 39 and all(row["occupation_signature_blocks"] == row["expected_signature_blocks"] for row in rows),
            "all_resolved_signature_blocks_have_one_CAR_sign": all(row["all_paths_in_each_signature_have_one_CAR_sign"] for row in rows),
            "cauchy_moment_control": control,
        },
        "decision": {
            "K505_generic_cancellation_control_retracted": False,
            "K505_generic_obstruction_applies_to_exact_K177_equal_coupling_paths": False,
            "native_path_cross_terms_nonnegative": True,
            "one_native_path_norm_is_a_valid_word_norm_lower_bound": True,
            "uniform_all_level_path_norm_rate_serialized": False,
            "complete_K500_uniform_leakage_emitted": False,
            "next_exact_input": "Choose one explicit nonzero continuum K177 path at every q00/q10 bath level, derive a refinement-uniform lower sequence for its norm, and compare that sequence directly with K175/K496's held absolute residual. No Gram-floor computation is required for the equal-coupling native ray.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "An all-order cancellation-free lower-norm theorem for the exact K177 equal-coupling positive-Fock path family, with exact CAR-sign and signature controls through order twelve. It removes K506's full normalized-Gram-floor obligation on the native all-ones coefficient ray, but supplies no quantitative all-level path-norm rate, uniform K500 leakage, noncyclic/cyclic floor, K473/K152 result, source, ledger, canon, paper, public, novelty or physical conclusion.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    controls = payload["exact_controls"]
    decision = payload["decision"]
    if len(controls["seed_order_rows"]) != 39 or controls["resolved_path_records"] <= controls["resolved_occupation_signature_blocks"]:
        raise AssertionError("K507 census changed")
    if not controls["all_39_seed_order_blocks_match_closed_counts"] or not controls["all_resolved_signature_blocks_have_one_CAR_sign"]:
        raise AssertionError("K507 native CAR controls failed")
    if not controls["cauchy_moment_control"]["same_order_determinant_positive"]:
        raise AssertionError("K507 moment positivity control failed")
    theorem = payload["all_order_theorem"]
    if "det[kappa(s_i+r_j)]" not in theorem["andreief_identity"] or "dnu(E_k)" not in theorem["andreief_identity"]:
        raise AssertionError("K507 Andreief identity lost")
    if "nonnegative" not in theorem["native_cross_terms"]:
        raise AssertionError("K507 native-cross theorem lost")
    if decision["K505_generic_cancellation_control_retracted"]:
        raise AssertionError("K507 may not retract K505's generic countercontrol")
    if not decision["native_path_cross_terms_nonnegative"] or not decision["one_native_path_norm_is_a_valid_word_norm_lower_bound"]:
        raise AssertionError("K507 route release lost")
    if decision["uniform_all_level_path_norm_rate_serialized"] or decision["complete_K500_uniform_leakage_emitted"]:
        raise AssertionError("K507 overclaimed quantitative closure")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
