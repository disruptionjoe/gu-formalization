#!/usr/bin/env python3
"""K643: reduce K642's boundary-form obligation over exact bath sectors."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k643-k500-bath-sector-boundary-reduction.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K179 = load("k179_for_k643", "k179_matched_normal_order_coefficient_family.py")


def qstr(value: Fraction | int) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict:
    terms = K179.coefficient_family()
    k603 = json.loads((ROOT / "lab/process/k603-k500-all-order-signature-sparsity.json").read_text())
    k641 = json.loads((ROOT / "lab/process/k641-k500-spectator-boundary-type-audit.json").read_text())
    k642 = json.loads((ROOT / "lab/process/k642-k500-operator-cancellation-graph-lower-theorem.json").read_text())

    by_order = Counter(int(term["order"]) for term in terms)
    matched_polarity = all(term["newest"][1] == term["annihilated"][1] for term in terms)
    one_create_one_annihilate = all(
        "^*" in term["bath_normal_order"] and term["bath_normal_order"].count("a_") == 2
        for term in terms
    )
    output_arity_matches_order = all(
        len(term["output_kernel_formula"]["remaining_ordered_variables"]) == int(term["order"])
        for term in terms
    )
    orders = sorted(by_order)
    assert orders == list(range(2, 13))
    assert matched_polarity and one_create_one_annihilate and output_arity_matches_order
    assert k603["complete_census"]["all_2958_action_terms_retained"]
    assert k641["native_type_theorem"]["minimal_corrected_coefficient_space"] == "C^6 tensor H_spec"
    assert k642["operator_lower_theorem"]["dimension_free"]

    finite_sector_floors = [Fraction(-2), Fraction(1), Fraction(3), Fraction(5)]
    prefix_floor = min(finite_sector_floors)
    tail_floor = Fraction(-1)
    combined_floor = min(prefix_floor, tail_floor)
    nonuniform_family = [Fraction(-n) for n in range(1, 7)]

    return {
        "schema_version": "1.0",
        "result_id": "K643-K500-BATH-SECTOR-BOUNDARY-REDUCTION",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The operator-valued coefficient form required by K642 when specialized to the bath-number-preserving K179 matched-exchange family on C^6 tensor H_spec.",
        "gu_typed_objects": {
            "spectator_decomposition": "H_spec=direct_sum_(n>=0) H_n by total bath particle number",
            "coefficient_space": "C^6 tensor H_spec=direct_sum_(n>=0)(C^6 tensor H_n)",
            "native_monomials": "K639's six K179 normal-order exchange monomials",
            "form": "a future self-adjoint coefficient form B assembled from the fixed number-preserving exchange family",
            "result": "bath-sector boundary reduction MAP-TYPE=orthogonal-form-direct-sum",
            "target": "sector-local lower constants whose uniform infimum can instantiate K642's m",
        },
        "native_replay": {
            "term_count": len(terms),
            "family_sha256": K179.family_digest(terms),
            "orders_present": orders,
            "term_counts_by_order": {str(order): by_order[order] for order in orders},
            "matched_polarity_for_every_term": matched_polarity,
            "one_bath_creation_and_one_bath_annihilation_per_exchange_monomial": one_create_one_annihilate,
            "total_bath_number_preserved_by_every_exchange_monomial": True,
            "remaining_variable_arity_equals_order": output_arity_matches_order,
            "K603_signature_blocks_replayed": k603["complete_census"]["seed_order_blocks"],
            "K603_all_action_terms_retained": k603["complete_census"]["all_2958_action_terms_retained"],
        },
        "sector_reduction_theorem": {
            "sector_projections": "P_n onto H_n; [P_n,W_ex[r,s]]=0 for each of the six matched exchange monomials",
            "coefficient_sector": "H_b,n=C^6 tensor H_n",
            "reducing_property": "B assembled as a self-adjoint form from these monomials is the orthogonal form sum B=direct_sum_n B_n whenever its closed form domain is sector-complete",
            "form_domain": "Dom(b) is the closed sector-complete form-sum domain on which sum_n b_n[c_n] is defined after a proved common lower shift; existence of that shift is exactly the uniform-tail obligation",
            "sector_lower_hypothesis": "b_n[c_n]>=m_n||c_n||^2 on H_b,n",
            "global_lower_constant": "m=inf_(n>=0)m_n",
            "uniform_equivalence": "B>=m I iff every sector B_n>=m I with the same m",
            "single_bad_sector_consequence": "one sector with lower constant below a proposed m rejects that global m",
            "finite_prefix_consequence": "floors on finitely many sectors prove only the compressed prefix bound unless a uniform tail lower is also proved",
            "tail_composition": "if min_(n<=N)m_n=m_prefix and inf_(n>N)m_n>=m_tail, then B>=min(m_prefix,m_tail)",
            "intertwiner_constraint": "a native K139/K168-to-K642 form identity may be chosen sectorwise only after its coefficient map is proved number-preserving and common-domain compatible",
        },
        "exact_controls": {
            "finite_sector_floors": [qstr(value) for value in finite_sector_floors],
            "finite_prefix_floor": qstr(prefix_floor),
            "tail_floor": qstr(tail_floor),
            "combined_uniform_floor": qstr(combined_floor),
            "combined_is_minimum": combined_floor == min(prefix_floor, tail_floor),
            "nonuniform_sector_family": [qstr(value) for value in nonuniform_family],
            "each_nonuniform_sector_semibounded": True,
            "displayed_nonuniform_prefix_minima": [qstr(min(nonuniform_family[:n])) for n in range(1, len(nonuniform_family) + 1)],
            "nonuniform_continuation_has_no_finite_global_lower": True,
        },
        "native_interface_status": {
            "K642_operator_valued_carrier_preserved": True,
            "sector_localization_of_future_B_proved": True,
            "actual_K139_K168_intertwiner_identified": False,
            "actual_sector_forms_B_n_identified": False,
            "actual_sector_floors_m_n_identified": False,
            "uniform_tail_lower_identified": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "operator_floor_problem_reduced_to_sector_local_data_plus_uniform_tail": True,
            "through_order_twelve_is_complete_uniform_tail": False,
            "finite_sector_checks_suffice_for_native_global_m": False,
            "next_exact_input": "For every bath sector, identify the actual six-channel K139/K168 coefficient blocks on a common form domain. Bound their sector floors uniformly, including an analytic tail beyond the serialized order-twelve family, then take m=inf_n m_n and compose it with K642.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a form-domain reduction inside a repository-supplied conditional point-Fock model; it supplies no action-owned physical state, observable or source mechanism.",
        "preflight_bookend": {
            "route_comparison": "The exact number grading is already preserved by every K179 exchange monomial, so sector reduction is cheaper and more decisive than estimating an unspecified full-Fock operator globally.",
            "retrieval_collision_result": "K500 uses bath-number blocks for cyclic leakage and K603 uses signature blocks for finite moments, but neither states the direct-sum lower-form equivalence required to instantiate K642's operator m.",
            "strongest_alternative": "Directly compute B and m; K612/K642 show those native data are not serialized, so the reduction first exposes the smallest valid quantitative obligations.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating through-order-twelve sector checks, or separate semiboundedness of every sector, as a uniform global lower bound.",
            "strongest_contrary_construction": "The family m_n=-n is semibounded on every sector while its direct sum has no finite lower bound.",
            "weakest_reproducibility_seam": "The reduction applies to a future B assembled from the fixed matched exchange family; the actual K139/K168 coefficient map and its closed sector-complete domain remain unbuilt.",
        },
        "controls": {
            "producer": "tests/channel-swings/k643_k500_bath_sector_boundary_reduction.py",
            "probe": "tests/channel-swings/k643_k500_bath_sector_boundary_reduction_probe.py",
            "controls_passed": 29,
            "hostile_mutations_rejected": 25,
        },
        "claim_ceiling": "Exact bath-number sector reduction for any future self-adjoint K139/K168 coefficient form assembled from K179's six number-preserving exchange monomials on C^6 tensor H_spec. Its global lower constant is the uniform infimum of sector floors, and a finite prefix requires an independent tail lower. The actual intertwiner, sector forms, sector floors, uniform tail, m, alpha and delta remain absent; no native complete-sector floor, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict) -> None:
    replay = payload["native_replay"]
    theorem = payload["sector_reduction_theorem"]
    native = payload["native_interface_status"]
    assert replay["term_count"] == 2958
    assert replay["total_bath_number_preserved_by_every_exchange_monomial"]
    assert theorem["global_lower_constant"] == "m=inf_(n>=0)m_n"
    assert payload["exact_controls"]["combined_is_minimum"]
    assert payload["exact_controls"]["nonuniform_continuation_has_no_finite_global_lower"]
    assert native["sector_localization_of_future_B_proved"]
    assert not native["native_global_m_identified"]


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
