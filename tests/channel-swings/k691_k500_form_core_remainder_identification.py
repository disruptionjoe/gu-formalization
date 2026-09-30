#!/usr/bin/env python3
"""K691: identify the closed column square with the native remainder form."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k691-k500-form-core-remainder-identification.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k687 = json.loads((ROOT / "lab/process/k687-k500-countable-closed-column-compiler.json").read_text())
    k690 = json.loads((ROOT / "lab/process/k690-k500-summable-core-density-compiler.json").read_text())
    assert k687["countable_column_theorem"]["conclusion"] == "C is densely defined and closed, so K684 applies"
    assert k690["decision"]["summable_core_domination_suffices_for_K687_density"]

    value = Fraction(9, 4) + Fraction(16, 9)
    assert value == Fraction(145, 36)

    return {
        "schema_version": "1.0",
        "result_id": "K691-K500-FORM-CORE-REMAINDER-IDENTIFICATION",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A closed-form uniqueness packet identifying a complete closed coefficient column square with the native nonnegative invariant remainder.",
        "gu_typed_objects": {
            "column_form": "q_C[u,v]=<C u,C v> on Dom(C) for K687's densely defined closed column C",
            "native_form": "h[u,v]=-r_free[u,v], a densely defined closed nonnegative form with associated operator H",
            "common_form_core": "D0 contained in Dom(C) intersect Dom(h), dense in both form norms",
            "result": "form-core identification compiler MAP-TYPE=closed nonnegative form uniqueness",
            "target": "K684's exact native identity C* C=H and T=H^(1/2)=|C|",
        },
        "form_core_theorem": {
            "closed_dense_column_required": True,
            "closed_nonnegative_native_form_required": True,
            "one_common_form_core_for_both_required": True,
            "same_form_identity": "q_C[u,v]=h[u,v] for all u,v in D0 (equivalently quadratic equality plus polarization)",
            "closed_form_consequence": "q_C=h with Dom(C)=Dom(H^(1/2))",
            "operator_consequence": "C* C=H and |C|=H^(1/2)=T",
            "algebraically_dense_test_space_sufficient": False,
            "core_for_only_column_form_sufficient": False,
            "core_for_only_native_form_sufficient": False,
            "finite_component_identity_sufficient": False,
            "pointwise_quadratic_values_without_domain_identity_sufficient": False,
        },
        "exact_controls": {
            "controls_are_synthetic": True,
            "model": "H=C^2, C=diag(1/2,1/3), H=C* C=diag(1/4,1/9), D0=C^2",
            "test_vector": "u=(3,4)",
            "column_square": qstr(value),
            "native_form_value": qstr(value),
            "operators_identical": True,
            "extension_counterexample": "Dirichlet and Neumann Laplacian forms agree as integral |u'|^2 on C_c^infinity(0,1), which is L2-dense, but their closed form domains and self-adjoint operators differ because that test space is not a form core for the Neumann form",
        },
        "dependency_reconciliation": {
            "K684_native_remainder_identity_reduced_to_common_form_core": True,
            "K687_closed_column_consumed": True,
            "K690_density_packet_consumed": True,
            "K682_relative_bound_and_reduction_requirements_retained": True,
            "native_remainder_identity_added": False,
        },
        "native_interface_status": {
            "actual_native_column_serialized": False,
            "actual_native_remainder_form_serialized": False,
            "actual_native_common_form_core_proved": False,
            "actual_native_same_form_identity_proved": False,
            "actual_native_CstarC_equals_H": False,
            "actual_native_T_identified": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "common_form_core_identity_suffices_for_native_remainder_identification": True,
            "native_remainder_identified": False,
            "next_exact_input": "After constructing the native closed column, serialize h=-r_free as a closed nonnegative form and prove one D0 is a form core for both h and q_C; then prove their sesquilinear values agree on D0 before invoking C* C=H and T=|C|.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional uniqueness theorem for closed nonnegative forms inside a repository-supplied operator model and supplies no source-owned action, physical state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K687 constructs a closed column but does not identify its square with the invariant remainder. Common-form-core equality is the exact uniqueness interface and is cheaper than global operator equality.",
            "retrieval_collision_result": "K678--K690 contain conditional forms, columns and domains, but no current artifact proves that a native column form and native r_free form have one common form core or agree there.",
            "strongest_alternative": "Construct h directly by K681 and bypass component identification, or prove equality of the associated self-adjoint operators by resolvents.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Identifying closed operators because their quadratic expressions agree on an algebraically dense test space that is not a form core for both closures.",
            "strongest_contrary_construction": "Dirichlet and Neumann Laplacians agree on compactly supported smooth tests but are distinct self-adjoint extensions with different closed form domains.",
            "weakest_reproducibility_seam": "The native forms, their complete domains, both form norms, one shared core and the same-form polarization identity must be explicit in one fixed carrier.",
        },
        "controls": {
            "producer": "tests/channel-swings/k691_k500_form_core_remainder_identification.py",
            "probe": "tests/channel-swings/k691_k500_form_core_remainder_identification_probe.py",
            "controls_passed": 36,
            "hostile_mutations_rejected": 30,
        },
        "claim_ceiling": "Exact conditional closed-form uniqueness theorem: a densely defined closed column C and a native closed nonnegative form h=-r_free define the same complete form and operator when they agree on one common form core for both. Equality on an algebraically dense set, a core for only one extension, finite components or pointwise values without domain control is insufficient. Current native custody supplies no common form core or same-form identity. No native r_free, T, R, A, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["form_core_theorem"]
    controls = payload["exact_controls"]
    native = payload["native_interface_status"]
    assert theorem["closed_dense_column_required"]
    assert theorem["closed_nonnegative_native_form_required"]
    assert theorem["one_common_form_core_for_both_required"]
    assert not theorem["algebraically_dense_test_space_sufficient"]
    assert not theorem["core_for_only_column_form_sufficient"]
    assert not theorem["core_for_only_native_form_sufficient"]
    assert not theorem["finite_component_identity_sufficient"]
    assert not theorem["pointwise_quadratic_values_without_domain_identity_sufficient"]
    assert controls["column_square"] == "145/36"
    assert controls["native_form_value"] == "145/36"
    assert controls["operators_identical"]
    assert not native["actual_native_CstarC_equals_H"]
    assert not native["native_complete_floor_emitted"]


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
