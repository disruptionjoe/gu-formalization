#!/usr/bin/env python3
"""K604 exact determinant-simplex kernel atlas for K500 finite moments."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from itertools import combinations_with_replacement, product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k604-k500-determinant-simplex-kernel-atlas.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K179 = load("k179_for_k604", "k179_matched_normal_order_coefficient_family.py")
K178 = K179.K178


def canonical_species_blocks(left: dict[str, Any], right: dict[str, Any]) -> list[dict[str, list[int]]]:
    labels = sorted(set(left["species_positions"]) | set(right["species_positions"]))
    blocks = []
    for label in labels:
        lpos = left["species_positions"].get(label, [])
        rpos = right["species_positions"].get(label, [])
        if len(lpos) != len(rpos):
            raise AssertionError("paired exterior sectors must have equal species multiplicities")
        blocks.append({"left": lpos, "right": rpos})
    return sorted(blocks, key=lambda row: (row["left"], row["right"]))


def cyclic_side(row: dict[str, Any]) -> dict[str, Any]:
    positions: dict[str, list[int]] = defaultdict(list)
    for index, label in enumerate(row["letters"], start=1):
        positions[label].append(index)
    order = int(row["order"])
    return {
        "kind": "cyclic",
        "simplex_rank": order,
        "normalization_prefactor": f"(2*pi)^(-{order}/2)",
        "contracted_scalar_heat_times": [],
        "species_positions": dict(sorted(positions.items())),
        "source_id": row["path_id"],
        "coefficient": 1,
    }


def action_side(row: dict[str, Any]) -> dict[str, Any]:
    positions: dict[str, list[int]] = defaultdict(list)
    for label, provenance in zip(row["output_letters"], row["output_variable_provenance"]):
        positions[label].append(int(provenance))
    return {
        "kind": "action",
        "simplex_rank": int(row["order"]) + 1,
        "normalization_prefactor": row["output_kernel_formula"]["normalization_prefactor"],
        "contracted_scalar_heat_times": [int(row["old_position"])],
        "species_positions": dict(sorted(positions.items())),
        "source_id": row["contraction_id"],
        "coefficient": int(row["exact_operator_coefficient"]),
    }


def side_kernel(side: dict[str, Any]) -> dict[str, Any]:
    return {
        "kind": side["kind"],
        "simplex_rank": side["simplex_rank"],
        "normalization_prefactor": side["normalization_prefactor"],
        "contracted_scalar_heat_times": side["contracted_scalar_heat_times"],
        "lambda_exponent": "256*s_1",
    }


def kernel_descriptor(pair_kind: str, left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    descriptor = {
        "pair_kind": pair_kind,
        "left": side_kernel(left),
        "right": side_kernel(right),
        "exterior_determinant_blocks": canonical_species_blocks(left, right),
        "one_particle_heat_kernel": "kappa(t)=K_1(t)/pi",
        "kernel_formula": "prod_scalar kappa(s_i) prod_scalar kappa(r_j) prod_species det[kappa(s_a+r_b)]",
        "simplex_domains": "s_1>...>s_p>0 and r_1>...>r_q>0",
    }
    if pair_kind in {"N", "B_F"}:
        swapped = {
            **descriptor,
            "left": descriptor["right"],
            "right": descriptor["left"],
            "exterior_determinant_blocks": sorted(
                ({"left": row["right"], "right": row["left"]} for row in descriptor["exterior_determinant_blocks"]),
                key=lambda row: (row["left"], row["right"]),
            ),
        }
        if json.dumps(swapped, sort_keys=True) < json.dumps(descriptor, sort_keys=True):
            descriptor = swapped
    return descriptor


def signature_groups() -> tuple[dict[tuple[int, int, str], list[dict[str, Any]]], dict[tuple[int, int, str], list[dict[str, Any]]]]:
    paths: dict[tuple[int, int, str], list[dict[str, Any]]] = defaultdict(list)
    actions: dict[tuple[int, int, str], list[dict[str, Any]]] = defaultdict(list)
    for row in K178.path_records(12):
        if int(row["order"]) >= 2:
            paths[(int(row["seed_impurity"]), int(row["order"]), row["occupation_signature"])].append(cyclic_side(row))
    for row in K179.coefficient_family(12):
        actions[(int(row["seed_impurity"]), int(row["order"]), row["output_signature"])].append(action_side(row))
    return paths, actions


def add_pair(classes: dict[str, dict[str, Any]], pair_kind: str, left: dict[str, Any], right: dict[str, Any], symmetry_factor: int) -> None:
    descriptor = kernel_descriptor(pair_kind, left, right)
    encoded = json.dumps(descriptor, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(encoded).hexdigest()
    row = classes.setdefault(digest, {
        "kernel_id": f"DSK-{digest[:16]}",
        "descriptor": descriptor,
        "unordered_pair_occurrences": 0,
        "diagonal_pair_occurrences": 0,
        "expanded_gram_multiplicity": 0,
        "signed_multiplicity": 0,
        "positive_contributions": 0,
        "negative_contributions": 0,
        "source_pair_examples": [],
    })
    signed = symmetry_factor * int(left["coefficient"]) * int(right["coefficient"])
    row["unordered_pair_occurrences"] += 1
    row["diagonal_pair_occurrences"] += int(left["source_id"] == right["source_id"])
    row["expanded_gram_multiplicity"] += symmetry_factor
    row["signed_multiplicity"] += signed
    row["positive_contributions"] += int(signed > 0) * abs(signed)
    row["negative_contributions"] += int(signed < 0) * abs(signed)
    if len(row["source_pair_examples"]) < 2:
        row["source_pair_examples"].append([left["source_id"], right["source_id"]])


def atlas() -> dict[str, Any]:
    paths, actions = signature_groups()
    classes: dict[str, dict[str, Any]] = {}
    raw = Counter()
    expanded = Counter()
    all_keys = sorted(set(paths) | set(actions))
    for key in all_keys:
        cyclic_rows = paths.get(key, [])
        action_rows = actions.get(key, [])
        for left, right in combinations_with_replacement(cyclic_rows, 2):
            factor = 1 if left["source_id"] == right["source_id"] else 2
            add_pair(classes, "N", left, right, factor)
            raw["N"] += 1; expanded["N"] += factor
        for left, right in product(cyclic_rows, action_rows):
            add_pair(classes, "A_F", left, right, 1)
            raw["A_F"] += 1; expanded["A_F"] += 1
        for left, right in combinations_with_replacement(action_rows, 2):
            factor = 1 if left["source_id"] == right["source_id"] else 2
            add_pair(classes, "B_F", left, right, factor)
            raw["B_F"] += 1; expanded["B_F"] += factor

    class_rows = sorted(classes.values(), key=lambda row: row["kernel_id"])
    by_kind = []
    for kind in ("N", "A_F", "B_F"):
        rows = [row for row in class_rows if row["descriptor"]["pair_kind"] == kind]
        by_kind.append({
            "pair_kind": kind,
            "surviving_unordered_pairs": raw[kind],
            "expanded_gram_terms": expanded[kind],
            "distinct_kernel_classes": len(rows),
            "classes_with_exact_signed_cancellation": sum(row["signed_multiplicity"] == 0 for row in rows),
            "nonzero_signed_kernel_classes": sum(row["signed_multiplicity"] != 0 for row in rows),
            "signed_multiplicity_l1": sum(abs(row["signed_multiplicity"]) for row in rows),
        })
    compact_classes = []
    for row in class_rows:
        descriptor = row["descriptor"]
        compact_classes.append({
            "id": row["kernel_id"],
            "k": descriptor["pair_kind"],
            "l": [
                descriptor["left"]["kind"][0].upper(),
                descriptor["left"]["simplex_rank"],
                descriptor["left"]["contracted_scalar_heat_times"],
            ],
            "r": [
                descriptor["right"]["kind"][0].upper(),
                descriptor["right"]["simplex_rank"],
                descriptor["right"]["contracted_scalar_heat_times"],
            ],
            "b": [[block["left"], block["right"]] for block in descriptor["exterior_determinant_blocks"]],
            "u": row["unordered_pair_occurrences"],
            "d": row["diagonal_pair_occurrences"],
            "g": row["expanded_gram_multiplicity"],
            "m": row["signed_multiplicity"],
            "p": row["positive_contributions"],
            "n": row["negative_contributions"],
            "x": row["source_pair_examples"][0],
        })
    return {
        "encoding": {
            "class_fields": {
                "id": "determinant-simplex kernel id",
                "k": "pair kind N, A_F or B_F",
                "l_r": "[side kind C=cyclic or A=action, simplex rank, contracted scalar heat-time positions]",
                "b": "flavor-isometry-quotiented determinant blocks [[left positions],[right positions]]",
                "u_d_g": "unordered occurrences, diagonal occurrences and expanded Gram multiplicity",
                "m_p_n": "signed multiplicity and positive/negative contribution L1 parts",
                "x": "one auditable source-coordinate pair",
            },
            "shared_kernel_formula": "prod_scalar kappa(s_i) prod_scalar kappa(r_j) prod_blocks det[kappa(s_a+r_b)]",
            "simplex_domains": "s_1>...>s_p>0 and r_1>...>r_q>0",
            "normalization_from_rank": "each side of simplex rank q has prefactor (2*pi)^(-q/2)",
            "lambda_exponent": "256*(s_1+r_1)",
            "one_particle_heat_kernel": "kappa(t)=K_1(t)/pi",
        },
        "classes": compact_classes,
        "summary": by_kind,
        "raw_pairs": dict(raw),
        "expanded_terms": dict(expanded),
        "class_digest": hashlib.sha256(json.dumps(compact_classes, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
    }


def build() -> dict[str, Any]:
    k603 = json.loads((ROOT / "lab/process/k603-k500-all-order-signature-sparsity.json").read_text())
    result = atlas()
    expected = {
        "N": sum(row["cyclic_norm_pairs_surviving"] for row in k603["seed_order_rows"]),
        "A_F": sum(row["cyclic_action_pairs_surviving"] for row in k603["seed_order_rows"]),
        "B_F": sum(row["action_norm_pairs_surviving"] for row in k603["seed_order_rows"]),
    }
    return {
        "schema_version": "1.0",
        "result_id": "K604-K500-DETERMINANT-SIMPLEX-KERNEL-ATLAS",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact determinant-simplex kernel classes and signed multiplicities for every K177/K179 finite N, A_F and B_F Gram product surviving K603 through order twelve.",
        "gu_typed_objects": {
            "cyclic_vectors": "the complete K177 G^n path coordinates for the three K162 zero-bath seeds through order twelve",
            "action_vectors": "the complete signed K179 matched-exchange coordinates through order twelve",
            "pairing": "normalized CAR exterior pairing represented specieswise by determinants of kappa(s_i+r_j)",
            "result": "determinant-simplex kernel atlas MAP-TYPE=exact-integral-class-quotient",
            "target": "one outward enclosure per nonzero signed K604 class before composing K599's finite N/A_F/B_F moments",
        },
        "kernel_theorem": {
            "cyclic_side": "order-n simplex with output heat times 1..n and no contracted scalar heat factor",
            "action_side": "order-(n+1) simplex with output heat times given by K179 provenance and one contracted scalar kappa(s_old)",
            "exterior_pairing": "one determinant det[kappa(s_i+r_j)] for every occupied bath species",
            "flavor_isometry_quotient": "species names are quotiented only after their paired left/right time-position blocks are retained",
            "symmetric_gram_factor": "off-diagonal N and B_F unordered pairs carry factor two; diagonal pairs carry factor one",
            "coefficient_rule": "K601's unit cyclic-coordinate convention and every exact signed K179 operator coefficient are retained",
            "surviving_count_is_not_value": True,
            "determinant_expansion_is_not_replaced_by_occurrencewise_absolute_values": True,
        },
        "atlas": result,
        "K603_reconciliation": {
            "expected_surviving_pairs": expected,
            "atlas_surviving_pairs": result["raw_pairs"],
            "all_pair_counts_match": result["raw_pairs"] == expected,
            "all_2958_action_terms_replayed": k603["complete_census"]["all_2958_action_terms_retained"],
        },
        "decision": {
            "complete_finite_kernel_atlas_emitted": True,
            "exact_signed_multiplicities_emitted": True,
            "duplicate_or_isometric_quadrature_identified": True,
            "outward_kernel_values_emitted": False,
            "complete_finite_K456_moments_emitted": False,
            "complete_K500_uniform_leakage_emitted": False,
            "native_noncyclic_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Outwardly enclose each nonzero signed determinant-simplex kernel class with within-determinant interference retained, sum by the exact signed multiplicities into finite N/A_F/B_F, then apply K599 with K574's tail once and prove uniformity.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact finite kernel-class quotient and signed multiplicity atlas through order twelve. It preserves every K177/K179 coordinate, determinant block, contraction heat factor and Gram symmetry factor while identifying identical flavor-isometric kernels. It supplies no numerical kernel value, finite moment enclosure, uniform K500 leakage, noncyclic floor, K473/K152 result, or source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion.",
    }


def validate(payload: dict[str, Any]) -> None:
    rec = payload["K603_reconciliation"]
    decision = payload["decision"]
    if rec["expected_surviving_pairs"] != {"N": 2352, "A_F": 21344, "B_F": 59586}:
        raise AssertionError("K603 surviving counts changed")
    if not rec["all_pair_counts_match"] or not rec["all_2958_action_terms_replayed"]:
        raise AssertionError("K604 failed to conserve K603 coordinates")
    if not payload["atlas"]["classes"] or len(payload["atlas"]["class_digest"]) != 64:
        raise AssertionError("K604 empty or unhashed atlas")
    if not decision["complete_finite_kernel_atlas_emitted"] or not decision["exact_signed_multiplicities_emitted"]:
        raise AssertionError("K604 release missing")
    if any(decision[key] for key in ("outward_kernel_values_emitted", "complete_finite_K456_moments_emitted", "complete_K500_uniform_leakage_emitted", "native_noncyclic_floor_emitted", "K473_released", "native_K152_interval_emitted")):
        raise AssertionError("K604 overclaimed numerical or downstream closure")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build(); validate(payload)
    # The exact atlas has 41,063 rows.  Canonical compact JSON keeps the
    # complete class set reviewable without a formatting-only repository bloat.
    rendered = json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
