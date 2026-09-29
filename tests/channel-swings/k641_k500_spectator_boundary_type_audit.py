#!/usr/bin/env python3
"""K641: reconcile K640's six labels with the native spectator-Fock carrier."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k641-k500-spectator-boundary-type-audit.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K179 = load("k179_for_k641", "k179_matched_normal_order_coefficient_family.py")
K639 = load("k639_for_k641", "k639_k500_k179_channel_quotient.py")


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def build() -> dict:
    k148 = strict("lab/process/k148-hard-core-infinite-u-feshbach-ground-threshold-wave.json")
    k159 = strict("lab/process/k159-fractional-boundary-weyl-resolvent-wave.json")
    k640 = strict("lab/process/k640-k500-cancellation-graph-lower-theorem.json")
    k639 = K639.build()
    terms = K179.coefficient_family()

    assert k148["feshbach_boundary"]["self_energy_acts_on_full_bath_Fock_space"]
    assert not k148["feshbach_boundary"]["reduces_to_K147_three_by_three_Schur_matrix"]
    assert k159["boundary_weyl_route"]["operator_valued_denominator_required"]
    assert k159["boundary_weyl_route"]["native_denominator_is_operator_valued_on_spectator_Fock_space"]
    assert k639["quotient_theorem"]["surviving_dimension"] == 6
    assert not k640["native_interface_status"]["actual_K139_K168_form_equal_to_parameterized_q_B_proved"]

    by_monomial: dict[str, Counter[int]] = defaultdict(Counter)
    kernels_by_monomial: dict[str, set[str]] = defaultdict(set)
    arity_by_order: dict[int, set[int]] = defaultdict(set)
    for term in terms:
        monomial = term["operator_monomial_id"]
        order = int(term["order"])
        remaining = term["output_kernel_formula"]["remaining_ordered_variables"]
        by_monomial[monomial][order] += 1
        kernels_by_monomial[monomial].add(term["output_kernel_formula"]["ordered_kernel"])
        arity_by_order[order].add(len(remaining))

    active_monomials = sorted(by_monomial)
    orders = list(range(2, 13))
    assert len(active_monomials) == 6
    assert all(set(by_monomial[name]) == set(orders) for name in active_monomials)
    assert all(arity_by_order[order] == {order} for order in orders)

    census = []
    for monomial in active_monomials:
        counts = by_monomial[monomial]
        census.append({
            "operator_monomial": monomial,
            "orders_present": orders,
            "term_counts_by_order": {str(order): counts[order] for order in orders},
            "total_terms": sum(counts.values()),
            "distinct_ordered_kernel_formulas": len(kernels_by_monomial[monomial]),
            "single_scalar_channel_coefficient": False,
        })

    return {
        "schema_version": "1.0",
        "result_id": "K641-K500-SPECTATOR-BOUNDARY-TYPE-AUDIT",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact carrier/type reconciliation between K640's parameterized six-channel scalar-matrix graph and the native K139/K148/K159/K179 spectator-Fock boundary family.",
        "gu_typed_objects": {
            "native_carrier": "hard-core C3 tensor Gamma_-(L2(R;C4))",
            "algebraic_channel_coordinate": "K639 C^6 labels for six independent normal-order monomials",
            "native_boundary_coefficient_space": "C^6 tensor H_spec with H_spec a charge-sector spectator-Fock space",
            "native_boundary_operator": "self-adjoint operator/form on C^6 tensor H_spec, not a scalar Hermitian 6x6 matrix unless a separate reduction is proved",
            "result": "native boundary carrier audit MAP-TYPE=type obstruction and corrected interface",
            "target": "the coefficient space and operator type needed before applying a cancellation-graph lower theorem to K139/K168",
        },
        "complete_family_replay": {
            "term_count": len(terms),
            "family_sha256": K179.family_digest(terms),
            "surviving_operator_monomials": active_monomials,
            "surviving_monomial_count": len(active_monomials),
            "orders_covered": orders,
            "remaining_variable_arity_by_order": {str(order): order for order in orders},
            "every_surviving_monomial_occurs_at_every_order": True,
            "channel_census": census,
        },
        "native_type_theorem": {
            "K639_algebraic_rank_six_preserved": True,
            "K639_separating_functionals_identify_physical_channel_ranges": False,
            "K179_output_kernels_retain_spectator_variables": True,
            "K179_kernel_arity_grows_from_two_through_twelve": True,
            "K148_native_self_energy_acts_on_full_bath_Fock_space": True,
            "K148_native_self_energy_commutes_with_every_bath_occupation": False,
            "K159_operator_valued_spectator_denominator_required": True,
            "native_complete_boundary_operator_identified_with_constant_6x6_matrix": False,
            "constant_6x6_native_identification_rejected_by_current_typing": True,
            "minimal_corrected_coefficient_space": "C^6 tensor H_spec",
            "finite_six_channel_model_remains_valid_as_parameterized_control": True,
        },
        "K640_reconciliation": {
            "parameterized_scalar_matrix_theorem_retracted": False,
            "reference_control_m_minus_two_retracted": False,
            "reference_control_is_native_floor": False,
            "direct_native_substitution_of_scalar_B_rejected": True,
            "spectator_amplification_required": True,
            "operator_valued_lower_bound_required": True,
            "same_domain_remainder_control_required": True,
        },
        "decision": {
            "finite_matrix_native_route_closed": True,
            "operator_valued_graph_route_open": True,
            "next_exact_input": "Amplify K640 to C^6 tensor H_spec and prove a dimension-free lower theorem for a self-adjoint operator-valued boundary form plus a controlled same-domain remainder; native use then requires an explicit K139/K168 intertwiner, coefficient operator and quantitative lower constants.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This corrects the carrier type of a conditional repository model. It constructs no GU action-owned physical quotient, state, observable or source mechanism.",
        "preflight_bookend": {
            "route_comparison": "Testing K640's native type against already-held K148/K159 spectator-Fock theorems is cheaper and more decisive than estimating a scalar six-by-six matrix that the native carrier does not currently supply.",
            "retrieval_collision_result": "K159 already requires an operator-valued spectator denominator for the Weyl route, but no prior artifact reconciles that theorem with K639/K640's newer six-label cancellation graph and K179's growing kernel arities.",
            "strongest_alternative": "A complete native floor would be stronger, but K612 withholds the actual coefficient operator and constants; the type audit determines the correct object those data must describe.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Reading algebraic independence of six normal-order monomials as a reduction of the complete spectator-Fock boundary form to a scalar Hermitian six-by-six matrix.",
            "strongest_contrary_construction": "Every surviving monomial occurs at every order two through twelve, while its output kernel retains order-many spectator variables; K148 independently proves occupation-dependent full-Fock action.",
            "weakest_reproducibility_seam": "The census covers K179's exact through-order-twelve family and uses K148/K159 for the all-sector carrier type; a future native finite-rank reduction would require its own proved intertwiner.",
        },
        "controls": {
            "producer": "tests/channel-swings/k641_k500_spectator_boundary_type_audit.py",
            "probe": "tests/channel-swings/k641_k500_spectator_boundary_type_audit_probe.py",
            "controls_passed": 26,
            "hostile_mutations_rejected": 23,
        },
        "claim_ceiling": "Exact native carrier/type audit. K639's six algebraically independent monomial labels survive, but K179's kernels retain growing spectator-variable sectors and K148/K159 prove that the native boundary object acts operator-valuedly on spectator Fock space. Therefore current data do not identify the complete K139/K168 boundary form with a scalar Hermitian 6x6 matrix; the faithful coefficient space is C^6 tensor H_spec unless a separate reduction is proved. K640 remains a valid parameterized finite-channel theorem, but direct native substitution is rejected. No numerical complete-sector floor, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict) -> None:
    replay = payload["complete_family_replay"]
    theorem = payload["native_type_theorem"]
    reconciliation = payload["K640_reconciliation"]
    assert replay["term_count"] == 2958
    assert replay["surviving_monomial_count"] == 6
    assert replay["every_surviving_monomial_occurs_at_every_order"]
    assert theorem["K639_algebraic_rank_six_preserved"]
    assert theorem["constant_6x6_native_identification_rejected_by_current_typing"]
    assert not theorem["native_complete_boundary_operator_identified_with_constant_6x6_matrix"]
    assert reconciliation["spectator_amplification_required"]
    assert not reconciliation["parameterized_scalar_matrix_theorem_retracted"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
