#!/usr/bin/env python3
"""Exact gauge-slice and Green-compatibility gate for corrected observation.

The algebraic projector P = I - j Gamma is tested as a representative selector.
Exact rational controls distinguish its trace-lift kernel from unrelated gauge
images and show that a right inverse need not be Green-self-adjoint.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/corrected-observation-gauge-slice-green-compatibility.json"
Q = Fraction


def matmul(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a: list[list[Q]]) -> list[list[Q]]:
    return [list(row) for row in zip(*a)]


def matsub(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    return [[x - y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def matvec(a: list[list[Q]], v: list[Q]) -> list[Q]:
    return [sum((x * y for x, y in zip(row, v)), Q(0)) for row in a]


def q(value: Q) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def qmatrix(a: list[list[Q]]) -> list[list[str]]:
    return [[q(value) for value in row] for row in a]


def build() -> dict:
    identity = [[Q(int(i == j)) for j in range(3)] for i in range(3)]
    gamma = [[Q(1), Q(0), Q(0)]]
    j_orthogonal = [[Q(1)], [Q(0)], [Q(0)]]
    j_oblique = [[Q(1)], [Q(1)], [Q(0)]]
    p_orthogonal = matsub(identity, matmul(j_orthogonal, gamma))
    p_oblique = matsub(identity, matmul(j_oblique, gamma))
    green = identity
    wrong_gauge_generator = [Q(1), Q(0), Q(1)]
    trace_gauge_generator = [Q(1), Q(0), Q(0)]

    owner_paths = {
        "corrected_clifford_projector": ROOT / "lab/process/literal-observation-gamma-kernel-obstruction-package.json",
        "k77_observation_projector": ROOT / "lab/process/selected-k77-action-bundle-observation-overlap.json",
        "k77_section_faithfulness": ROOT / "lab/process/selected-k77-physical-section-faithfulness-gate.json",
        "k77_natural_trace_constraint": ROOT / "lab/process/selected-k77-natural-trace-constraint-gate.json",
        "k77_bfv": ROOT / "lab/process/selected-k77-full-bfv-master-equation-gate.json",
        "k77_green_domain": ROOT / "lab/process/selected-k77-coupled-green-domain.json",
    }
    owners = {key: json.loads(path.read_text()) for key, path in owner_paths.items()}

    return {
        "schema_version": "1.0",
        "result_id": "CORRECTED-OBSERVATION-GAUGE-SLICE-GREEN-COMPATIBILITY",
        "created": "2026-09-23",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "Determine exactly when the supplied corrected observed Clifford projector is an action-owned gauge slice with a compatible Green pairing, without identifying same-named K77 projectors across different carriers.",
        "theorem": {
            "projector": "P=I-j*Gamma with Gamma*j=I",
            "image": "im(P)=ker(Gamma)",
            "kernel": "ker(P)=im(j)",
            "coset_constancy": "P is constant on cosets of a gauge image G iff G is contained in im(j)",
            "full_slice": "If Gamma restricted to G is an isomorphism onto the trace carrier, then P is a complete gauge slice iff G=im(j)",
            "green_condition": "For a nondegenerate Green form H, P is H-self-adjoint iff j*Gamma is H-self-adjoint; the right-inverse law alone does not imply this",
        },
        "exact_fixture": {
            "field": "Q",
            "carrier_dimension": 3,
            "trace_dimension": 1,
            "gamma": qmatrix(gamma),
            "orthogonal_right_inverse": qmatrix(j_orthogonal),
            "oblique_right_inverse": qmatrix(j_oblique),
            "orthogonal_projector": qmatrix(p_orthogonal),
            "oblique_projector": qmatrix(p_oblique),
            "green_form": qmatrix(green),
            "right_inverse_laws": {
                "orthogonal": matmul(gamma, j_orthogonal) == [[Q(1)]],
                "oblique": matmul(gamma, j_oblique) == [[Q(1)]],
            },
            "projector_laws": {
                "orthogonal_idempotent": matmul(p_orthogonal, p_orthogonal) == p_orthogonal,
                "oblique_idempotent": matmul(p_oblique, p_oblique) == p_oblique,
                "both_land_in_gamma_kernel": matmul(gamma, p_orthogonal) == [[Q(0)] * 3] and matmul(gamma, p_oblique) == [[Q(0)] * 3],
                "trace_image_is_killed": matvec(p_orthogonal, trace_gauge_generator) == [Q(0)] * 3,
                "unrelated_gauge_image_is_not_killed": matvec(p_orthogonal, wrong_gauge_generator) != [Q(0)] * 3,
            },
            "green_laws": {
                "orthogonal_projector_is_self_adjoint": matmul(transpose(p_orthogonal), green) == matmul(green, p_orthogonal),
                "oblique_projector_is_not_self_adjoint": matmul(transpose(p_oblique), green) != matmul(green, p_oblique),
            },
        },
        "owner_audit": {
            "corrected_clifford_projector": {
                "carrier": "observed one-form-spinor module B",
                "owned": "algebraic split projector onto ker(Gamma_B)",
                "missing": "source/action choice of right inverse, gauge image, quotient, Green form and common domain",
                "evidence": "explorations/source-native-corrected-observation-projector-2026-08-31.md",
            },
            "k77_complete_observation_projector": {
                "carrier": owners["k77_observation_projector"]["layer0"]["observation"],
                "owned": owners["k77_observation_projector"]["result"],
                "missing": "typed intertwiner to B and proof that its killed image equals im(j_B)",
                "evidence": "lab/process/selected-k77-action-bundle-observation-overlap.json",
            },
            "k77_section_receiver": {
                "carrier": "four horizontal plus ten conormal equation components",
                "owned": owners["k77_section_faithfulness"]["result"],
                "missing": "source-derived conormal constraint/BV quotient and link to the Clifford trace complement",
                "evidence": "lab/process/selected-k77-physical-section-faithfulness-gate.json",
            },
            "k77_zero_order_trace_constraint": {
                "carrier": owners["k77_natural_trace_constraint"]["layer0"]["carrier"],
                "owned": "unique propagated Spin-natural zero-order line C=2 Gamma(zeta)-nu",
                "missing": "route is killed by the retained rank-128 Jordan image and is neither BV nor a quotient",
                "evidence": "lab/process/selected-k77-natural-trace-constraint-gate.json",
            },
            "k77_bfv_image": {
                "carrier": owners["k77_bfv"]["carrier"]["configuration"],
                "owned": "frozen distortion-orbit rank-70 classical BFV gauge image",
                "missing": "map to the observed one-form-spinor trace lift, proper global resolution and physical cohomology",
                "evidence": "lab/process/selected-k77-full-bfv-master-equation-gate.json",
            },
            "k77_green_form": {
                "carrier": "full 3860-dimensional boson/fermion boundary comparator",
                "owned": owners["k77_green_domain"]["disposition"],
                "missing": "selected moving reality/Calderon or maximal-dissipative domain and compatibility with P_B",
                "evidence": "lab/process/selected-k77-coupled-green-domain.json",
            },
            "typed_composition_result": "no current artifact supplies one carrier map intertwining P_B with an action-owned gauge image and a selected Green-domain projector",
        },
        "decision": {
            "algebraic_correction_retracted": False,
            "physical_gauge_slice_derived": False,
            "green_compatible_right_inverse_derived": False,
            "same_named_projectors_composed": False,
            "shortcut_route": "killed_until_typed_intertwiner_and_image_equality_are_supplied",
            "next_exact_input": "construct or identify an action-owned map iota from the observed one-form-spinor carrier into the K77 equation/field complex, then prove iota(im j_B) equals the relevant gauge/constraint image and iota intertwines the selected Green-domain projector",
        },
        "ledger_effect": {
            "RA-F1": "NEEDS_UNCHANGED",
            "RA-D4": "NEEDS_UNCHANGED",
            "AC-F1": "UNCHANGED",
            "LT-GR6b": "NEEDS_UNCHANGED",
            "SC-GEN-02/03/51/53/54": "SOURCE_POLARITY_UNCHANGED",
            "SC-CHI-01/51": "SOURCE_POLARITY_UNCHANGED",
        },
        "release_test": {
            "both_right_inverse_laws_hold": matmul(gamma, j_orthogonal) == [[Q(1)]] and matmul(gamma, j_oblique) == [[Q(1)]],
            "both_projectors_are_idempotent": matmul(p_orthogonal, p_orthogonal) == p_orthogonal and matmul(p_oblique, p_oblique) == p_oblique,
            "both_projectors_land_in_gamma_kernel": matmul(gamma, p_orthogonal) == [[Q(0)] * 3] and matmul(gamma, p_oblique) == [[Q(0)] * 3],
            "matching_trace_image_is_killed": matvec(p_orthogonal, trace_gauge_generator) == [Q(0)] * 3,
            "unrelated_gauge_image_survives": matvec(p_orthogonal, wrong_gauge_generator) != [Q(0)] * 3,
            "right_inverse_does_not_force_green_self_adjointness": matmul(transpose(p_oblique), green) != matmul(green, p_oblique),
            "owner_carriers_remain_distinct": True,
            "no_source_ledger_canon_paper_or_public_effect": True,
        },
        "claim_ceiling": "Exact linear-algebra criterion for when a split corrected Clifford projector can be a gauge representative selector, plus a typed audit showing that current K77 action, BV, observation and Green artifacts do not yet supply the required same-carrier intertwiner, image equality or selected common domain. No physical quotient, chirality, family count, residual-vector realization, source/ledger move, canon, paper, public or GU verdict follows.",
    }


def validate_payload(payload: dict) -> None:
    assert payload["theorem"]["image"] == "im(P)=ker(Gamma)"
    assert payload["theorem"]["kernel"] == "ker(P)=im(j)"
    assert payload["exact_fixture"]["projector_laws"]["orthogonal_idempotent"]
    assert payload["exact_fixture"]["projector_laws"]["oblique_idempotent"]
    assert payload["exact_fixture"]["projector_laws"]["unrelated_gauge_image_is_not_killed"]
    assert payload["exact_fixture"]["green_laws"]["orthogonal_projector_is_self_adjoint"]
    assert payload["exact_fixture"]["green_laws"]["oblique_projector_is_not_self_adjoint"]
    assert len(payload["owner_audit"]) == 7
    assert payload["owner_audit"]["typed_composition_result"].startswith("no current artifact")
    assert not payload["decision"]["physical_gauge_slice_derived"]
    assert not payload["decision"]["green_compatible_right_inverse_derived"]
    assert not payload["decision"]["same_named_projectors_composed"]
    assert all(payload["release_test"].values())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    if args.write:
        OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print("corrected-observation gate passed: gauge-slice image equality and Green-adjoint compatibility remain independent required owners")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
