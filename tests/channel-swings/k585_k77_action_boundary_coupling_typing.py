#!/usr/bin/env python3
"""K585: reconstruct and type the actual first-action boundary-coupling candidate."""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import runpy
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_common_first_action_epsilon_hessian_probe.py"
OUTPUT = ROOT / "lab/process/k585-k77-action-boundary-coupling-typing.json"


def strict(relative: str) -> dict[str, Any]:
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def reconstruct():
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        packet = runpy.run_path(str(PREDECESSOR))
    if packet["FAILURES"] or "PASS 61/61" not in capture.getvalue():
        raise AssertionError("selected first-action predecessor failed")
    return packet["cross_matrix"], packet["direction_grades"]


def matrix_digest(matrix) -> str:
    entries = [
        [int(row), int(column), str(value)]
        for (row, column), value in sorted(matrix.todok().items())
    ]
    encoded = json.dumps(entries, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def build() -> dict[str, Any]:
    action = strict("lab/process/selected-k77-common-first-action-epsilon-hessian.json")
    tangent = strict("lab/process/selected-k77-first-action-tangent-closure.json")
    kt = strict("lab/process/k442-k77-corrected-boundary-kt-product.json")
    square = strict("lab/process/k444-k77-degree-changing-boundary-squares.json")
    matrix, grades = reconstruct()
    nonzero_rows = sorted({int(row) for row, _ in matrix.todok()})
    column_supports = [sum(1 for row in range(matrix.rows) if matrix[row, column] != 0) for column in range(matrix.cols)]
    grade_one_rows = [index for index, grade in enumerate(grades) if grade == 1]

    payload = {
        "schema_version": "1.0",
        "result_id": "K585-K77-ACTION-BOUNDARY-COUPLING-TYPING",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "scope": "Exact reconstruction and Layer-0 typing of the selected first-action moving-Shiab Hessian cross block against K442/K444's corrected-boundary homogeneous-orbit KT product. It identifies the actual source and receiver and tests direct arrow compatibility without inventing a reduction, tensor factorization or BV grading.",
        "gu_typed_objects": {
            "result": "actual action-coupling typing attempt MAP-TYPE=typed-interface-audit",
            "source": "91 primitive epsilon variations of the selected first action; LAYER=field-tangent variation; CHIRALITY=N/A",
            "target": "1470 connection Euler receiver directions split as Clifford grades 196 plus 1274; MAP-TYPE=Hessian-cross",
            "pairing": "selected first-action Shiab/Hodge pairing at the common stationary connection branch",
            "kt_product": "homogeneous-orbit base factors 21 to 91 to 70 tensored with the corrected rank-512 boundary carrier",
            "action_owner": "repository-selected source-shaped first transgression action; not a complete source-selected BV master action",
        },
        "source_and_ledger_context": {
            "source_claims": ["SC-ACT-01", "SC-ACT-02", "SC-ACT-06", "SC-META-53"],
            "source_polarity_effect": "none",
            "physics_rows": ["LT-SM8", "LT-GR6b", "RA-F1", "AC-F1"],
            "ledger": "lab/process/conditional-physics-ledger-v0.263.json",
            "ledger_effect": "none",
            "action_input": "lab/process/selected-k77-common-first-action-epsilon-hessian.json",
            "tangent_input": "lab/process/selected-k77-first-action-tangent-closure.json",
            "kt_input": "lab/process/k442-k77-corrected-boundary-kt-product.json",
            "typed_square_input": "lab/process/k444-k77-degree-changing-boundary-squares.json",
        },
        "preflight_bookend": {
            "route_comparison": "Reconstruct the only current coefficient-bearing action cross block before applying any abstract BV or boundary theorem.",
            "retrieval_collision_result": "K464/K475/K476/K479 provide admission, rank, support and nilpotence interfaces but explicitly serialize no native D2/D1 coefficients.",
            "strongest_alternative": "Tensoring or projecting an arbitrary control into K444 would create coefficients rather than test the selected action and was rejected.",
        },
        "actual_action_block": {
            "name": "moving-Shiab first-action Hessian cross",
            "shape": [matrix.rows, matrix.cols],
            "rank": int(matrix.rank()),
            "nonzero_entries": len(matrix.todok()),
            "nonzero_receiver_rows": len(nonzero_rows),
            "all_live_receivers_are_grade_one": all(grades[row] == 1 for row in nonzero_rows),
            "grade_one_receiver_dimension": len(grade_one_rows),
            "grade_two_receiver_dimension": grades.count(2),
            "column_support_set": sorted(set(column_supports)),
            "sparse_content_digest": matrix_digest(matrix),
            "predecessor_rank": action["moving_epsilon"]["mixed_cross_rank"],
            "tangent_grade_one_dimension": tangent["exact_result"][
                "grade1_grade1_first_action_hessian"
            ]["shape"][0],
        },
        "typed_map_attempt": {
            "kt_base_dimensions": kt["finite_product_complex"]["base_dimensions"],
            "corrected_boundary_rank": kt["finite_product_complex"]["corrected_carrier_rank"],
            "kt_product_dimensions": kt["finite_product_complex"]["product_dimensions"],
            "actual_source_matches_middle_base_dimension": matrix.cols == 91,
            "actual_receiver_matches_degree_zero_base_dimension": matrix.rows == 70,
            "actual_receiver_matches_degree_two_base_dimension": matrix.rows == 21,
            "actual_block_directly_types_as_K444_D1_or_D2": False,
            "tensor_with_identity_512_shape": [matrix.rows * 512, matrix.cols * 512],
            "tensor_with_identity_512_matches_D1": [matrix.rows * 512, matrix.cols * 512] == [35840, 46592],
            "tensor_with_identity_512_matches_D2": [matrix.rows * 512, matrix.cols * 512] == [46592, 10752],
            "dimension_coincidence_1470_equals_21_times_70": matrix.rows == 21 * 70,
            "dimension_coincidence_is_typed_factorization": False,
            "owner_authenticated_1470_to_70_reduction_present": False,
            "owner_authenticated_21_to_91_adjacent_block_present": False,
            "corrected_boundary_carrier_map_present": False,
        },
        "decision": {
            "actual_action_block_reconstructed": True,
            "actual_action_block_nontrivial": True,
            "actual_action_block_instantiates_K444": False,
            "absence_is_now_exactly_typed": True,
            "specified_completion_rejected": "direct identification or identity-512 tensor lift of the 1470-by-91 Hessian cross with either K444 arrow",
            "source_action_rejected": False,
            "next_exact_input": "Derive an action-owned rank-70 reduction L from the 1470 connection-Euler receiver to the orbit target, then derive an independent action-owned rank-21 adjacent block into ker(LB); separately identify the corrected rank-512 carrier action and test both K444 projector squares.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling the rank-91 Hessian cross a field/antifield differential merely because its source has dimension 91.",
            "strongest_contrary_construction": "The current block's receiver has dimension 1470 and its identity-512 lift has target dimension 752640, not K444's degree-zero or degree-one target.",
            "weakest_reproducibility_seam": "The exact matrix is rebuilt through the large predecessor probe rather than stored independently; its sparse digest and support/rank fingerprint bind that replay.",
        },
        "controls": {
            "producer": "tests/channel-swings/k585_k77_action_boundary_coupling_typing.py",
            "probe": "tests/channel-swings/k585_k77_action_boundary_coupling_typing_probe.py",
        },
        "claim_ceiling": "Exact reconstruction and typing of one selected first-action 1470-by-91 rank-91 Hessian cross. It proves that direct identification and the identity-512 tensor lift do not instantiate K444's corrected-boundary arrows. It does not prove that no action-owned reduction or BV/KT completion exists, serialize D2/D1, select a physical boundary, construct physical cohomology, or move source, ledger, canon, paper, public posture, novelty, prediction, confirmation or a physical GU verdict.",
    }
    validate(payload)
    return payload


def validate(payload: dict[str, Any]) -> None:
    block = payload["actual_action_block"]
    attempt = payload["typed_map_attempt"]
    decision = payload["decision"]
    if block["shape"] != [1470, 91] or block["rank"] != 91 or block["nonzero_entries"] != 182:
        raise AssertionError("actual action block fingerprint changed")
    if block["nonzero_receiver_rows"] != 182 or not block["all_live_receivers_are_grade_one"]:
        raise AssertionError("action receiver typing changed")
    if block["grade_one_receiver_dimension"] != 196 or block["grade_two_receiver_dimension"] != 1274:
        raise AssertionError("source tangent grading changed")
    if attempt["kt_base_dimensions"] != [21, 91, 70] or attempt["corrected_boundary_rank"] != 512:
        raise AssertionError("K442 carrier changed")
    if attempt["actual_block_directly_types_as_K444_D1_or_D2"] or attempt["tensor_with_identity_512_matches_D1"] or attempt["tensor_with_identity_512_matches_D2"]:
        raise AssertionError("mistyped action block as K444 arrow")
    if attempt["dimension_coincidence_is_typed_factorization"] or attempt["owner_authenticated_1470_to_70_reduction_present"]:
        raise AssertionError("invented action reduction")
    if not decision["actual_action_block_reconstructed"] or decision["actual_action_block_instantiates_K444"] or decision["source_action_rejected"]:
        raise AssertionError("K585 decision changed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
