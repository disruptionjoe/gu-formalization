#!/usr/bin/env python3
"""K660: covariance of the Weyl denominator under bounded boundary translations."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k660-k500-boundary-translation-denominator-covariance.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K659 = load("k659_for_k660", "k659_k500_auxiliary_chart_floor_nonidentifiability.py")


def add(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(a + b for a, b in zip(left, right, strict=True))


def subtract(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(a - b for a, b in zip(left, right, strict=True))


def strings(values: tuple[Fraction, ...]) -> list[str]:
    return [str(value) for value in values]


def build() -> dict[str, Any]:
    k659 = K659.build()
    m = (Fraction(-1), Fraction(2))
    w = (Fraction(1, 2), Fraction(3))
    c = (Fraction(3, 2), Fraction(-2, 3))
    m_prime = add(m, c)
    w_prime = add(w, c)
    d = subtract(w, m)
    d_prime = subtract(w_prime, m_prime)
    e = (Fraction(1, 5), Fraction(-1, 7))
    d_n = add(d, e)
    w_n = add(w, e)
    w_n_prime = add(w_n, c)
    d_n_prime = subtract(w_n_prime, m_prime)
    return {
        "schema_version": "1.0",
        "result_id": "K660-K500-BOUNDARY-TRANSLATION-DENOMINATOR-COVARIANCE",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The exact invariant content of K657--K658 under bounded self-adjoint translations of one authenticated ordinary boundary triple on the complete spectator-Fock boundary space.",
        "gu_typed_objects": {
            "carrier": "one complete spectator-Fock boundary Hilbert space shared by the original and translated ordinary boundary triples",
            "form": "Gamma_0'=Gamma_0 and Gamma_1'=Gamma_1+C Gamma_0 for bounded self-adjoint C, with M'=M+C and W'=W+C",
            "domain": "the same target extension and unchanged reference extension ker(Gamma_0) represented in translated boundary coordinates",
            "target": "the invariant complete denominator D_W(-s)=W-M(-s), its order floor and K658 cofinal error",
            "result": "boundary-translation covariance MAP-TYPE=coordinate equivalence",
        },
        "translation_theorem": {
            "hypothesis": "C is bounded self-adjoint on the complete boundary Hilbert space",
            "boundary_maps": "Gamma_0'=Gamma_0; Gamma_1'=Gamma_1+C Gamma_0",
            "weyl_transform": "M'(z)=M(z)+C",
            "extension_transform": "W'=W+C",
            "denominator_identity": "D'_W(z)=W'-M'(z)=W-M(z)=D_W(z)",
            "reference_extension_unchanged": True,
            "reference_resolvent_level_unchanged": True,
            "friedrichs_status_preserved_if_previously_proved": True,
            "friedrichs_status_created_by_translation": False,
            "complete_denominator_order_unchanged": True,
            "same_coordinate_approximant_error_unchanged": True,
            "finite_impurity_translation_sufficient": False,
            "unbounded_translation_covered": False,
        },
        "exact_controls": {
            "M_diagonal": strings(m),
            "W_diagonal": strings(w),
            "C_diagonal": strings(c),
            "translated_M_diagonal": strings(m_prime),
            "translated_W_diagonal": strings(w_prime),
            "denominator_diagonal": strings(d),
            "translated_denominator_diagonal": strings(d_prime),
            "denominator_invariant": d == d_prime,
            "approximant_denominator_diagonal": strings(d_n),
            "translated_approximant_denominator_diagonal": strings(d_n_prime),
            "approximant_denominator_invariant": d_n == d_n_prime,
            "cofinal_error_diagonal": strings(e),
            "operator_norm_error": str(max(abs(x) for x in e)),
            "operator_norm_error_invariant": subtract(d_n_prime, d_prime) == e,
            "controls_are_synthetic": True,
        },
        "composition": {
            "K659_chart_floor_obstruction_consumed": k659["decision"]["K139_auxiliary_shift_rejected_as_native_s"],
            "K657_invariant_quantity": "complete D_W(-s) order, not W or M(-s) separately",
            "K658_invariant_quantity": "complete ||D_N(-s)-D(-s)|| and d_N in one jointly translated coordinate",
            "counterterm_coordinate_may_be_harmless_only_after_translation_law_is_proved": True,
            "K139_regulator_coordinates_already_authenticated_as_boundary_translation": False,
        },
        "decision": {
            "coordinate_dependent_W_rejected_as_floor_data": True,
            "complete_denominator_selected_as_invariant_packet": True,
            "native_translation_law_authenticated": False,
            "native_floor_supplied": False,
            "next_exact_input": "Construct K139's actual ordinary boundary maps on the complete spectator-Fock boundary space, prove the Gamma_0 reference is Friedrichs, and show any regulator/counterterm change is a bounded joint translation of M and W; then choose a separate real -s and prove the invariant D_N(-s), d_N and eta_N packet.",
        },
        "native_interface_status": {
            "actual_native_boundary_triple_serialized": False,
            "actual_native_translation_law_proved": False,
            "actual_native_s_identified": False,
            "actual_native_denominator_serialized": False,
            "actual_native_d_n_identified": False,
            "actual_native_eta_n_identified": False,
            "actual_native_base_floor_r0_identified": False,
            "actual_native_target_b_identified": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "Boundary-coordinate covariance is internal to the repository-supplied point-Fock extension calculus and supplies no source-selected action, physical quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K659 rejects the auxiliary chart parameter as a floor; the strongest follow-through is to identify which part of the boundary data is genuinely invariant under harmless coordinate changes.",
            "retrieval_collision_result": "K139 states compensated chart and regulator universality, while K159 and K657 fix W-M(z); no current artifact proves the joint ordinary-boundary-triple translation law or distinguishes invariant D from coordinate-dependent W and M.",
            "strongest_alternative": "A direct complete-form proof under K652 can bypass boundary-coordinate authentication.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating K168's finite W_ref or a renormalization counterterm coordinate by itself as the native real-level denominator or floor.",
            "strongest_contrary_construction": "The exact diagonal control changes both W and M while leaving D and the cofinal error byte-for-byte invariant.",
            "weakest_reproducibility_seam": "The native K139 boundary maps and the relation between its regulator/counterterm coordinates and an ordinary-boundary-triple translation remain unserialized.",
        },
        "claim_ceiling": "Exact boundary-coordinate covariance theorem. Under a bounded self-adjoint complete-space translation Gamma_0'=Gamma_0, Gamma_1'=Gamma_1+C Gamma_0, the reference extension is unchanged, M'=M+C and W'=W+C, so D'=W'-M'=D exactly; denominator order and K658's same-coordinate approximation error are invariant. Translation preserves a previously proved Friedrichs reference but cannot create that proof, and no finite impurity or unbounded translation is covered. K139's regulator coordinates are not thereby authenticated as such a translation. No native s, denominator, d_N, eta_N, r0, b, tail, m, alpha, delta, K473, K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is supplied.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["translation_theorem"]
    controls = payload["exact_controls"]
    native = payload["native_interface_status"]
    assert theorem["denominator_identity"] == "D'_W(z)=W'-M'(z)=W-M(z)=D_W(z)"
    assert controls["denominator_invariant"]
    assert controls["approximant_denominator_invariant"]
    assert controls["operator_norm_error_invariant"]
    assert not native["actual_native_translation_law_proved"]


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
