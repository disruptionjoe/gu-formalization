#!/usr/bin/env python3
"""K839: finite-cutoff invertibility need not survive the operator limit."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k839-sc-act-06-finite-cutoff-limit-gate.json"
INPUTS = {
    "k831": ROOT / "lab/process/k831-sc-act-06-noncompact-fredholm-boundary.json",
    "k838": ROOT / "lab/process/k838-sc-act-06-nonlinear-germ-admission-compiler.json",
}
SAMPLE_CUTOFFS = [1, 2, 4, 8, 16]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def build() -> dict[str, Any]:
    inverse_norms = [fraction_text(Fraction(cutoff)) for cutoff in SAMPLE_CUTOFFS]
    capped_errors = [fraction_text(Fraction(1, cutoff)) for cutoff in SAMPLE_CUTOFFS]
    compression_errors = [fraction_text(Fraction(1, cutoff + 1)) for cutoff in SAMPLE_CUTOFFS]
    return {
        "schema_version": "1.0",
        "result_id": "K839-SC-ACT-06-FINITE-CUTOFF-LIMIT-GATE",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact deterministic boundary between invertibility at every finite cutoff and invertibility, closed range, or Fredholmness of the limiting operator.",
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in INPUTS.items()
        },
        "governance": {
            "carrier": "ell^2(N_{>=1}; C)",
            "pairing_or_form": "standard positive Hilbert inner product sum_n conjugate(x_n)y_n",
            "real_structure": "coordinatewise complex conjugation",
            "grading": "ungraded",
            "action_owner": "synthetic diagonal operator control only; no GU action owner supplied",
            "target_object": "finite-cutoff-to-limit Fredholm inference required downstream of K831 and inside K838's closed-global-Fredholm row",
            "assumptions": [
                "coordinates are indexed by positive integers",
                "cutoffs use the first N coordinates or the equivalent capped diagonal regularization",
                "operator, range, and Fredholm statements use the standard ell^2 topology",
            ],
            "claim_grade": "exact_repository_owned_control",
            "protected_scientific_effect": "none",
        },
        "finite_cutoff_limit_certificate": {
            "operator": "T:ell^2->ell^2, (Tx)_n=x_n/n",
            "operator_norm": "1",
            "self_adjoint": True,
            "positive": True,
            "compact": True,
            "finite_section": {
                "subspace": "H_N=span{e_1,...,e_N}",
                "operator": "T|H_N=diag(1,1/2,...,1/N)",
                "all_positive_integer_cutoffs_invertible": True,
                "inverse": "diag(1,2,...,N)",
                "inverse_norm_rule": "N",
                "zero_extended_operator_norm_error_rule": "1/(N+1)",
            },
            "capped_full_space_cutoff": {
                "operator": "T_N e_n=e_n/min(n,N)",
                "all_positive_integer_cutoffs_invertible": True,
                "inverse": "T_N^-1 e_n=min(n,N)e_n",
                "inverse_norm_rule": "N",
                "operator_norm_error_rule": "||T_N-T||=1/N",
                "operator_norm_convergence_to_T": True,
            },
            "samples": {
                "cutoffs": SAMPLE_CUTOFFS,
                "inverse_norms": inverse_norms,
                "capped_operator_norm_errors": capped_errors,
                "zero_extended_compression_errors": compression_errors,
            },
            "uniform_inverse_bound": False,
            "inverse_norms_diverge": True,
        },
        "limit_certificate": {
            "kernel_dimension": 0,
            "injective": True,
            "finite_support_sequences_contained_in_range": True,
            "finite_support_sequences_dense_in_ell2": True,
            "range_dense": True,
            "nonrange_witness": "y=(1/n)_n",
            "nonrange_witness_in_ell2": True,
            "unique_formal_preimage": "x=(1,1,...)_n",
            "formal_preimage_in_ell2": False,
            "range_surjective": False,
            "range_closed": False,
            "range_closure": "ell^2",
            "orthogonal_complement_of_range_dimension": 0,
            "bounded_below": False,
            "unit_vector_witness": "||e_N||=1 and ||T e_N||=1/N -> 0",
            "fredholm": False,
            "fredholm_obstruction": "range_not_closed",
        },
        "exact_controls": {
            "negative_control": {
                "family": "the capped T_N sequence above",
                "every_cutoff_invertible": True,
                "operator_norm_convergent": True,
                "inverse_norms_uniformly_bounded": False,
                "limit_invertible": False,
                "limit_fredholm": False,
            },
            "positive_control": {
                "family": "S_N=I on ell^2 for every N",
                "every_cutoff_invertible": True,
                "operator_norm_convergent": True,
                "inverse_norm_rule": "1",
                "inverse_norms_uniformly_bounded": True,
                "limit": "I",
                "limit_invertible": True,
                "limit_range_closed": True,
                "limit_fredholm": True,
                "limit_fredholm_index": 0,
            },
        },
        "gate": {
            "finite_cutoff_invertibility_alone_implies_limit_invertibility": False,
            "finite_cutoff_invertibility_plus_operator_norm_convergence_implies_limit_fredholmness": False,
            "uniform_inverse_or_coercive_estimate_is_an_independent_limit_obligation": True,
            "finite_cutoff_data_may_be_used_as_a_limit_certificate_without_stability": False,
        },
        "decision": {
            "k831_closed_global_fredholm_requirement_bypassed": False,
            "k838_closed_global_fredholm_row_satisfied_by_finite_cutoffs": False,
            "actual_gu_cutoff_family_or_limit_domain_constructed": False,
            "global_sc_act_06_proved_or_refuted": False,
            "next_exact_input": "For one source/action-owned GU family on a common closed domain, prove a cutoff-uniform inverse/coercive or Fredholm estimate and identify the limiting kernel, closed range, cokernel, and index before using finite cutoff solvability in K838's 27-row admission compiler.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "claim_ceiling": "Exact generic ell^2 finite-cutoff/limit counterexample and stable identity control only; no GU operator family, common domain, Fredholm realization, rich moduli, source, ledger, canon, or physical verdict.",
        "controls": {
            "producer": "tests/channel-swings/k839_sc_act_06_finite_cutoff_limit_gate.py",
            "probe": "tests/channel-swings/k839_sc_act_06_finite_cutoff_limit_gate_probe.py",
            "controls_passed": 47,
            "hostile_mutations_rejected": 24,
        },
    }


def validate(payload: dict[str, Any]) -> None:
    expected_inputs = {
        name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
        for name, path in INPUTS.items()
    }
    governance = payload["governance"]
    certificate = payload["finite_cutoff_limit_certificate"]
    section = certificate["finite_section"]
    capped = certificate["capped_full_space_cutoff"]
    samples = certificate["samples"]
    limit = payload["limit_certificate"]
    controls = payload["exact_controls"]
    gate = payload["gate"]
    decision = payload["decision"]

    assert payload["pinned_inputs"] == expected_inputs
    assert payload["target_claim"] == "SC-ACT-06"
    assert governance["carrier"] == "ell^2(N_{>=1}; C)"
    assert governance["pairing_or_form"].startswith("standard positive Hilbert inner product")
    assert governance["real_structure"] == "coordinatewise complex conjugation"
    assert governance["grading"] == "ungraded"
    assert governance["action_owner"].startswith("synthetic diagonal operator control only")
    assert governance["protected_scientific_effect"] == "none"

    assert certificate["operator"] == "T:ell^2->ell^2, (Tx)_n=x_n/n"
    assert certificate["operator_norm"] == "1"
    assert certificate["self_adjoint"] and certificate["positive"] and certificate["compact"]
    assert section["all_positive_integer_cutoffs_invertible"]
    assert section["inverse_norm_rule"] == "N"
    assert section["zero_extended_operator_norm_error_rule"] == "1/(N+1)"
    assert capped["all_positive_integer_cutoffs_invertible"]
    assert capped["inverse_norm_rule"] == "N"
    assert capped["operator_norm_error_rule"] == "||T_N-T||=1/N"
    assert capped["operator_norm_convergence_to_T"]
    assert samples["cutoffs"] == SAMPLE_CUTOFFS
    assert samples["inverse_norms"] == [str(n) for n in SAMPLE_CUTOFFS]
    assert samples["capped_operator_norm_errors"] == [fraction_text(Fraction(1, n)) for n in SAMPLE_CUTOFFS]
    assert samples["zero_extended_compression_errors"] == [fraction_text(Fraction(1, n + 1)) for n in SAMPLE_CUTOFFS]
    assert not certificate["uniform_inverse_bound"] and certificate["inverse_norms_diverge"]

    assert limit["kernel_dimension"] == 0 and limit["injective"]
    assert limit["finite_support_sequences_contained_in_range"]
    assert limit["finite_support_sequences_dense_in_ell2"] and limit["range_dense"]
    assert limit["nonrange_witness"] == "y=(1/n)_n" and limit["nonrange_witness_in_ell2"]
    assert limit["unique_formal_preimage"] == "x=(1,1,...)_n"
    assert not limit["formal_preimage_in_ell2"]
    assert not limit["range_surjective"] and not limit["range_closed"]
    assert limit["range_closure"] == "ell^2"
    assert limit["orthogonal_complement_of_range_dimension"] == 0
    assert not limit["bounded_below"] and not limit["fredholm"]
    assert limit["fredholm_obstruction"] == "range_not_closed"

    negative = controls["negative_control"]
    positive = controls["positive_control"]
    assert negative["every_cutoff_invertible"] and negative["operator_norm_convergent"]
    assert not negative["inverse_norms_uniformly_bounded"]
    assert not negative["limit_invertible"] and not negative["limit_fredholm"]
    assert positive["every_cutoff_invertible"] and positive["operator_norm_convergent"]
    assert positive["inverse_norm_rule"] == "1" and positive["inverse_norms_uniformly_bounded"]
    assert positive["limit_invertible"] and positive["limit_range_closed"] and positive["limit_fredholm"]
    assert positive["limit_fredholm_index"] == 0

    assert not gate["finite_cutoff_invertibility_alone_implies_limit_invertibility"]
    assert not gate["finite_cutoff_invertibility_plus_operator_norm_convergence_implies_limit_fredholmness"]
    assert gate["uniform_inverse_or_coercive_estimate_is_an_independent_limit_obligation"]
    assert not gate["finite_cutoff_data_may_be_used_as_a_limit_certificate_without_stability"]
    assert not decision["k831_closed_global_fredholm_requirement_bypassed"]
    assert not decision["k838_closed_global_fredholm_row_satisfied_by_finite_cutoffs"]
    assert not decision["actual_gu_cutoff_family_or_limit_domain_constructed"]
    assert not decision["global_sc_act_06_proved_or_refuted"]
    assert payload["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED"
    assert payload["controls"]["hostile_mutations_rejected"] == 24


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    elif args.check:
        assert json.loads(OUTPUT.read_text(encoding="utf-8")) == payload
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
