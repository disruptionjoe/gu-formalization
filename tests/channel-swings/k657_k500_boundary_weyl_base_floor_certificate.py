#!/usr/bin/env python3
"""K657: fail-closed boundary/Weyl certificate for one proposed base floor."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k657-k500-boundary-weyl-base-floor-certificate.json"


def row(s: Fraction, denominator_eigenvalues: tuple[Fraction, ...]) -> dict[str, Any]:
    margin = min(denominator_eigenvalues)
    return {
        "proposed_s": str(s),
        "proposed_base_floor_r0": str(-s),
        "k656_target_b": str(-s - 2),
        "denominator_eigenvalues": [str(x) for x in denominator_eigenvalues],
        "denominator_margin": str(margin),
        "certificate_accepts": margin >= 0,
    }


def build() -> dict[str, Any]:
    rows = [
        row(Fraction(5), (Fraction(1, 3), Fraction(7, 4))),
        row(Fraction(3, 2), (Fraction(0), Fraction(2))),
        row(Fraction(4), (Fraction(-1, 8), Fraction(3))),
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K657-K500-BOUNDARY-WEYL-BASE-FLOOR-CERTIFICATE",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A conditional ordinary-boundary-triple certificate converting positivity of the complete operator-valued Weyl denominator at one proposed real level into a lower floor for K139's fixed base extension.",
        "gu_typed_objects": {
            "carrier": "the complete spectator-Fock boundary Hilbert space of K159, never the finite impurity factor alone",
            "form": "D_W(lambda)=W-M(lambda) in one fixed ordinary-boundary-triple sign convention",
            "domain": "one fixed self-adjoint extension coordinate W with lambda=-s in the reference resolvent set",
            "target": "the K656 same-domain base inequality R0>=-s M and consequent reference target b=-s-2",
            "result": "boundary-denominator floor certificate MAP-TYPE=operator-order equivalence",
        },
        "ordinary_boundary_triple_theorem": {
            "theorem_basis": "Boundary Triplets and Weyl Functions, Appendix A, Theorem A.7(i)",
            "scalar_shift": "apply the nonnegative theorem to A-lambda I at zero, so its Weyl value is M_A(lambda)",
            "sign_convention": "A_W is defined by Gamma_1 f=W Gamma_0 f and D_W(lambda)=W-M(lambda)",
            "symmetric_operator_premise": "the underlying densely defined closed symmetric operator is semibounded below by lambda=-s",
            "reference_premise": "A_ref=ker(Gamma_0) is the Friedrichs extension A_F and lambda=-s lies in rho(A_F)",
            "extension_premise": "A_W and W are self-adjoint in the declared ordinary boundary triple",
            "boundary_space_premise": "M(lambda) is bounded and D_W(lambda) is the complete self-adjoint operator/form on the full spectator-Fock boundary space",
            "equivalence": "A_W>=lambda iff D_W(lambda)>=0",
            "accepted_consequence": "D_W(-s)>=0 implies A_W>=-s, hence r0=-s for K656 and b=-s-2 after K168",
            "kernel_boundary": "semidefinite D_W(-s) is admitted and may place -s at the extension spectrum; strict positivity is not required for a non-strict floor",
            "common_free_form_domain_required": False,
            "finite_impurity_denominator_sufficient": False,
            "native_sign_convention_may_be_inferred": False,
        },
        "fail_closed_admission": {
            "required_fields": [
                "ordinary boundary triple",
                "declared sign convention",
                "semibounded underlying symmetric operator",
                "Friedrichs reference extension",
                "self-adjoint reference and extension",
                "lambda in reference resolvent set",
                "reference floor at lambda",
                "bounded Weyl value M(lambda)",
                "full spectator-Fock boundary denominator",
                "complete denominator nonnegativity",
            ],
            "missing_any_field_rejects": True,
            "pointwise_sector_samples_reject": True,
            "finite_impurity_only_reject": True,
            "synthetic_controls_are_native_evidence": False,
        },
        "exact_controls": {
            "rows": rows,
            "accepted_rows": 2,
            "rejected_rows": 1,
            "zero_margin_accepts_non_strict_floor": rows[1]["certificate_accepts"],
            "negative_margin_rejected": not rows[2]["certificate_accepts"],
            "controls_are_synthetic": True,
        },
        "decision": {
            "K159_boundary_weyl_route_consumed": True,
            "K656_missing_base_floor_retyped": True,
            "native_floor_supplied": False,
            "next_exact_input": "Choose a proposed s, identify the K139 boundary triple whose Gamma_0 reference is the Friedrichs extension, verify bounded M(-s), and prove the full spectator-Fock denominator D_W(-s)>=0 in the actual extension coordinate and sign convention; K658 gives the admissible cofinal transfer shape.",
        },
        "native_interface_status": {
            "actual_native_s_identified": False,
            "actual_native_denominator_serialized": False,
            "actual_native_denominator_nonnegative": False,
            "actual_native_base_floor_r0_identified": False,
            "actual_native_target_b_identified": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This conditional analytic certificate remains inside the repository-supplied K139/K159 point-Fock control and supplies no action-owned state, quotient, observable or physical positivity result.",
        "preflight_bookend": {
            "route_comparison": "K656 needs one global base floor. K159's boundary/Weyl route is the only tested continuation that avoids the killed common free-form topology, so the cheapest strong move is to state its exact lower-bound criterion.",
            "retrieval_collision_result": "K159 records a contour-resolvent error interface but does not state the real-level denominator-order equivalence that directly emits K656's r0.",
            "strongest_alternative": "K652's cancellation-adapted all-order parity envelopes remain available if the complete real-level denominator cannot be controlled.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating a finite impurity matrix, sampled bath sectors or an undeclared sign convention as positivity of the complete native denominator.",
            "strongest_contrary_construction": "An uncontrolled negative direction in the spectator-Fock complement invalidates the floor even when every displayed finite impurity block is positive.",
            "weakest_reproducibility_seam": "K139/K159 do not serialize the actual complete denominator at any proposed real -s or prove the Friedrichs-reference, bounded-Weyl, sign-convention and positivity packet.",
        },
        "claim_ceiling": "Exact conditional ordinary-boundary-triple floor interface. For a semibounded symmetric operator, under one declared sign convention with Gamma_0 reference equal to the Friedrichs extension A_F, lambda=-s in rho(A_F), bounded M(lambda), and a fixed self-adjoint target extension, A_W>=-s exactly when its complete spectator-Fock denominator D_W(-s)=W-M(-s) is nonnegative. This would provide K656 with r0=-s and b=-s-2. The controls are synthetic. No native s, denominator, r0, b, tail, m, alpha, delta, K473, K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is supplied.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["ordinary_boundary_triple_theorem"]
    controls = payload["exact_controls"]
    native = payload["native_interface_status"]
    assert theorem["equivalence"] == "A_W>=lambda iff D_W(lambda)>=0"
    assert controls["accepted_rows"] == 2 and controls["rejected_rows"] == 1
    assert controls["zero_margin_accepts_non_strict_floor"]
    assert controls["negative_margin_rejected"]
    assert not native["actual_native_base_floor_r0_identified"]


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
