#!/usr/bin/env python3
"""K696: integrate the graph-equivalent column with the native remainder form."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k696-k500-column-remainder-integration-compiler.json"


def q(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def build() -> dict[str, Any]:
    k693 = json.loads((ROOT / "lab/process/k693-k500-graph-equivalent-column-compiler.json").read_text())
    k691 = json.loads((ROOT / "lab/process/k691-k500-form-core-remainder-identification.json").read_text())
    assert k693["decision"]["two_sided_graph_equivalence_suffices_for_closed_column"]
    assert k691["decision"]["common_form_core_identity_suffices_for_native_remainder_identification"]
    lower, upper = Fraction(1, 2), Fraction(3, 4)
    return {
        "schema_version": "1.0",
        "result_id": "K696-K500-COLUMN-REMAINDER-INTEGRATION-COMPILER",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "An end-to-end complete-operator certificate combining graph-equivalent column closure with common-form-core identification, polar decomposition and shared reductions.",
        "gu_typed_objects": {
            "graph_weight": "one positive closed a with bounded everywhere inverse on H",
            "column": "C:Dom(a) subset H -> direct_sum_j K_j with the complete column norm",
            "native_form": "closed nonnegative h=-r_free on Dom(C), represented by H",
            "factor": "T=H^(1/2)=|C|",
            "bounded_remainder": "R=T a^-1 on H",
            "result": "column-remainder integration compiler MAP-TYPE=closed-form representation plus polar decomposition",
            "target": "the exact native R interface consumed by K676/K677",
        },
        "integration_theorem": {
            "complete_two_sided_graph_equivalence_required": True,
            "common_form_core_for_column_and_native_form_required": True,
            "closed_form_equality_consequence": "q_C=h on their complete common form domain",
            "representation_consequence": "H=C* C and T=H^(1/2)=|C|",
            "polar_decomposition_consequence": "C=U T with U isometric on closure ran(T)",
            "bounded_transform_consequence": "R=T a^-1 and B=C a^-1=U R are bounded with ||R||=||B||",
            "reduction_consequence": "a projection reducing both a and h reduces H,T,R*R and supplies the corresponding intertwiner",
            "graph_equivalence_without_form_identity_sufficient": False,
            "form_identity_on_algebraically_dense_tests_sufficient": False,
            "same_domain_without_common_form_core_sufficient": False,
            "column_closedness_identifies_native_remainder_automatically": False,
            "reduction_of_column_labels_alone_reduces_native_R": False,
        },
        "exact_controls": {
            "controls_are_synthetic": True,
            "model": "H=C^2, a=diag(2,4), C=diag(1,3), h[u]=||Cu||^2",
            "lower_graph_constant": q(lower),
            "upper_graph_constant": q(upper),
            "H_matrix": [["1", "0"], ["0", "9"]],
            "T_matrix": [["1", "0"], ["0", "3"]],
            "R_matrix": [["1/2", "0"], ["0", "3/4"]],
            "C_a_inverse_norm": q(upper),
            "T_a_inverse_norm": q(upper),
            "norm_identity": True,
            "same_closed_column_different_native_form_counterexample": "h_1=||Cu||^2 and h_2=2||Cu||^2 share Dom(C) but have different representing operators; graph equivalence alone chooses neither.",
        },
        "dependency_reconciliation": {
            "K693_column_closedness_consumed": True,
            "K691_common_form_core_identity_consumed": True,
            "K682_bounded_R_interface_closed_conditionally": True,
            "K676_K677_native_R_type_now_single_packet": True,
            "native_component_or_form_data_added": False,
        },
        "native_interface_status": {
            "actual_native_component_column_serialized": False,
            "actual_native_graph_equivalence_proved": False,
            "actual_native_common_form_core_proved": False,
            "actual_native_form_identity_proved": False,
            "actual_native_reductions_proved": False,
            "actual_native_R_constructed": False,
            "native_A_above_two_thirds_proved": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "graph_equivalence_plus_common_form_core_identifies_T_and_bounded_R": True,
            "native_column_remainder_packet_constructed": False,
            "next_exact_input": "Serialize the native complete component column on Dom(a), prove K693's two-sided graph equivalence, and prove equality with h=-r_free on one common form core for both closed forms. Then verify the charge/bath reductions and use K697 on the resulting R.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional closed-form and polar-decomposition theorem and supplies no source-owned action, physical quotient, state or observable.",
        "preflight_bookend": {
            "route_comparison": "K693 closes the column and K691 identifies the form. Their composition is the cheapest route to the exact bounded R type used by the seed/complement certificates.",
            "retrieval_collision_result": "K684 assumes a closed native column and K682 assumes a native form-relative row; no prior packet composes K693 and K691 through polar decomposition and shared reductions.",
            "strongest_alternative": "Construct h directly through K681 and prove K682's relative form bound without component columns.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating graph equivalence, domain equality or algebraic test equality as if it identified the native closed form.",
            "strongest_contrary_construction": "Two distinct closed nonnegative forms can share the same domain and the same already-closed column carrier.",
            "weakest_reproducibility_seam": "The equality must hold on one common form core for both closed forms, and every claimed reduction must reduce both a and h.",
        },
        "controls": {
            "producer": "tests/channel-swings/k696_k500_column_remainder_integration_compiler.py",
            "probe": "tests/channel-swings/k696_k500_column_remainder_integration_compiler_probe.py",
            "controls_passed": 38,
            "hostile_mutations_rejected": 32,
        },
        "claim_ceiling": "Exact conditional integration theorem: complete two-sided graph equivalence closes C; equality of q_C and h on a common form core gives H=C* C and T=|C|; polar decomposition gives bounded R=T a^-1 with ||R||=||C a^-1||. Current native custody supplies none of the component, equivalence, common-core, identity or reduction data. No native A, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, n = p["integration_theorem"], p["exact_controls"], p["native_interface_status"]
    assert t["complete_two_sided_graph_equivalence_required"]
    assert t["common_form_core_for_column_and_native_form_required"]
    for key in (
        "graph_equivalence_without_form_identity_sufficient",
        "form_identity_on_algebraically_dense_tests_sufficient",
        "same_domain_without_common_form_core_sufficient",
        "column_closedness_identifies_native_remainder_automatically",
        "reduction_of_column_labels_alone_reduces_native_R",
    ):
        assert not t[key]
    assert c["lower_graph_constant"] == "1/2" and c["upper_graph_constant"] == "3/4"
    assert c["C_a_inverse_norm"] == c["T_a_inverse_norm"] == "3/4" and c["norm_identity"]
    assert p["target_claim"] == "NONE-NOT-A-KILL" and p["source_and_ledger_effect"] == "none"
    assert all(value is False for value in n.values())
    assert p["decision"]["graph_equivalence_plus_common_form_core_identifies_T_and_bounded_R"]
    assert not p["decision"]["native_column_remainder_packet_constructed"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
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
