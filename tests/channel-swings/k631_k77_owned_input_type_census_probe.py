#!/usr/bin/env python3
"""Independent controls and hostile mutations for K631."""

from __future__ import annotations

import copy
import json

from k631_k77_owned_input_type_census import build


def controls(p: dict) -> list[bool]:
    t = p["census_theorem"]
    o = p["ownership_reconciliation"]
    d = p["decision"]
    rows = p["candidates"]
    by_id = {row["id"]: row for row in rows}
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        p["candidate_count"] == 8,
        len(rows) == 8,
        len({row["id"] for row in rows}) == 8,
        all(row["first_failed_obligation"] for row in rows),
        all(row["reopener_matches"] == [] for row in rows),
        t["every_strong_current_candidate_typed"] is True,
        t["single_candidate_matching_ambient_gram"] is False,
        t["single_candidate_matching_source_domain_endomorphism"] is False,
        t["single_candidate_matching_stationary_odd_adapter"] is False,
        t["current_new_owned_input_dependency_is_not_a_retrieval_gap_at_single_object_level"] is True,
        t["composition_loophole_left_for_K632"] is True,
        o["H_Sigma_retracted"] is False,
        o["partial_stationary_Grams_retracted"] is False,
        o["K590_factorized_completion_retracted"] is False,
        o["K614_source_owned_injection_retracted"] is False,
        o["K617_corrected_descent_retracted"] is False,
        o["K629_K630_family_obstruction_retracted"] is False,
        o["source_or_action_rejected"] is False,
        d["single_current_object_reopens_K596_K598"] is False,
        p["source_and_ledger_effect"] == "none",
        p["required_reopener_signatures"]["ambient_gram"]["signature"].startswith("nondegenerate"),
        p["required_reopener_signatures"]["source_domain_endomorphism"]["signature"] == "V_128 -> V_128",
        p["required_reopener_signatures"]["stationary_odd_adapter"]["analytic"].startswith("K441-compatible"),
        "H_SIGMA" in by_id and by_id["H_SIGMA"]["source_or_action_owned"] is False,
    ]


def set_path(p: dict, path: tuple[object, ...], value: object) -> None:
    cursor = p
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value


def main() -> int:
    payload = build()
    assert all(controls(payload))
    mutations = [
        (("classification",), "SUPPORTED"),
        (("direction",), "native_to_observed"),
        (("target_claim",), "SC-ACT-01"),
        (("candidate_count",), 7),
        (("candidates", 0, "id"), "ZERO_FORM_SEED_J0"),
        (("candidates", 0, "first_failed_obligation"), ""),
        (("candidates", 0, "reopener_matches"), ["ambient_gram"]),
        (("census_theorem", "every_strong_current_candidate_typed"), False),
        (("census_theorem", "single_candidate_matching_ambient_gram"), True),
        (("census_theorem", "single_candidate_matching_source_domain_endomorphism"), True),
        (("census_theorem", "single_candidate_matching_stationary_odd_adapter"), True),
        (("census_theorem", "current_new_owned_input_dependency_is_not_a_retrieval_gap_at_single_object_level"), False),
        (("census_theorem", "composition_loophole_left_for_K632"), False),
        (("ownership_reconciliation", "H_Sigma_retracted"), True),
        (("ownership_reconciliation", "partial_stationary_Grams_retracted"), True),
        (("ownership_reconciliation", "K590_factorized_completion_retracted"), True),
        (("ownership_reconciliation", "K614_source_owned_injection_retracted"), True),
        (("ownership_reconciliation", "K617_corrected_descent_retracted"), True),
        (("ownership_reconciliation", "K629_K630_family_obstruction_retracted"), True),
        (("ownership_reconciliation", "source_or_action_rejected"), True),
        (("decision", "single_current_object_reopens_K596_K598"), True),
        (("source_and_ledger_effect",), "moved"),
        (("required_reopener_signatures", "source_domain_endomorphism", "signature"), "E_512 -> E_512"),
        (("candidates", 0, "source_or_action_owned"), True),
    ]
    caught = 0
    for path, value in mutations:
        case = copy.deepcopy(payload)
        set_path(case, path, value)
        caught += int(not all(controls(case)))
    assert caught == len(mutations)
    print(json.dumps({"controls_passed": len(controls(payload)), "hostile_mutations_rejected": caught}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
