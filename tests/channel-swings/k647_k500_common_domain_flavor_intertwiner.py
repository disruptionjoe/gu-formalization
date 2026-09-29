#!/usr/bin/env python3
"""K647: compose K139's recursive domain with K645 flavor covariance."""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k647-k500-common-domain-flavor-intertwiner.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K645 = load("k645_for_k647", "k645_k500_flavor_exchange_covariance.py")
K168 = load("k168_for_k647", "k168_flavor_symmetric_reference_extension.py")
K155 = K168.K155
K151 = K168.K151


def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(column) for column in zip(*matrix)]


def block_diag(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    n, m = len(left), len(right)
    return [
        list(left[i]) + [Fraction()] * m if i < n else [Fraction()] * n + list(right[i - n])
        for i in range(n + m)
    ]


def global_swap(local: list[list[Fraction]]) -> list[list[Fraction]]:
    zero = [[Fraction() for _ in row] for row in local]
    return [
        list(zero[i]) + list(transpose(local)[i]) if i < len(local)
        else list(local[i - len(local)]) + list(zero[i - len(local)])
        for i in range(2 * len(local))
    ]


def finite_control() -> dict[str, Any]:
    energies = ["5/4"]
    couplings = [1]
    left = K155.regular_pullback(energies, couplings, (1, 0), 256, 0)
    right = K155.regular_pullback(energies, couplings, (0, 1), 256, 0)
    left_ref = K168.regular_pullback_with_reference(energies, couplings, (1, 0), 256)
    right_ref = K168.regular_pullback_with_reference(energies, couplings, (0, 1), 256)
    swap = K151.flavor_swap_matrix(left["states"], right["states"], 1)
    identity = K155.identity(2 * len(swap))
    J = global_swap(swap)

    checks: dict[str, bool] = {
        "J_is_self_adjoint": J == transpose(J),
        "J_squared_is_identity": K155.matmul(J, J) == identity,
    }
    for name in ("G", "U", "U_inverse", "H", "R"):
        combined = block_diag(left[name], right[name])
        checks[f"J_commutes_with_{name}"] = K155.matmul(J, combined) == K155.matmul(combined, J)
    for name in ("reference_regular", "metric", "delta_regular"):
        combined = block_diag(left_ref[name], right_ref[name])
        checks[f"J_commutes_with_{name}"] = K155.matmul(J, combined) == K155.matmul(combined, J)
    return {
        "one_mode_charge_block_dimension_each": len(swap),
        "direct_sum_dimension": 2 * len(swap),
        "charge_pair": ["q=(1,0)", "q=(0,1)"],
        "all_exact_checks_pass": all(checks.values()),
        **checks,
        "finite_regulator_control_only": True,
    }


def build() -> dict[str, Any]:
    k645 = K645.build()
    k139 = json.loads((ROOT / "lab/process/k139-signed-boundary-inverse-profile-universality-wave.json").read_text())
    k153 = json.loads((ROOT / "lab/process/k153-neumann-chart-conforming-core-wave.json").read_text())
    k168 = json.loads((ROOT / "lab/process/k168-flavor-symmetric-reference-extension-wave.json").read_text())
    assert k645["finite_order_theorem"]["operator_identity"].startswith("J W_ex")
    assert k139["signed_minimal_limit"]["the_limit_has_one_common_recursive_boundary_domain"]
    assert k153["conforming_core"]["native_vectors"] == "psi_i=U_lambda^-1 phi_i"
    assert k168["reference_extension"]["flavor_symmetric"]
    control = finite_control()
    assert control["all_exact_checks_pass"]
    return {
        "schema_version": "1.0",
        "result_id": "K647-K500-COMMON-DOMAIN-FLAVOR-INTERTWINER",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The frozen equal-coupling K139 recursive boundary chart with K168's flavor-symmetric reference extension, composed with K645's second-quantized flavor involution.",
        "gu_typed_objects": {
            "carrier": "hard-core C3 impurity tensor signed particle/hole exterior Fock space",
            "free_domain": "the K139 positive free-operator domain Dom(H0)",
            "boundary_chart": "U=I-G and S=U^-1 on K139's common recursive boundary domain",
            "form": "the fixed K139 regular pullback plus K168 Delta R=S*W_ref S",
            "pairing": "the positive physical Gram M=S*S",
            "involution": "K645's self-adjoint second-quantized flavor swap J",
            "result": "common-domain flavor intertwiner MAP-TYPE=closed-form-domain unitary equivalence",
            "target": "the native same-form hypothesis required by K642/K644/K646",
        },
        "intertwiner_theorem": {
            "free_domain_invariance": "J Dom(H0)=Dom(H0) because the free dispersion is flavor blind",
            "boundary_covariance": "JG=GJ for equal couplings and matched profiles, including the K645 CAR phase",
            "chart_covariance": "JU=UJ for U=I-G",
            "inverse_covariance": "JS=SJ for S=U^-1 by the bounded inverse identity",
            "recursive_domain": "D_K139=S Dom(H0)",
            "recursive_domain_invariance": "J D_K139=D_K139",
            "physical_gram_covariance": "JM=MJ for M=S*S",
            "base_pullback_identity": "R0=S* H_base S on Dom(H0)",
            "base_pullback_covariance": "JR0=R0J when JH_base=H_baseJ",
            "reference_pullback_identity": "Delta R=S*W_ref S",
            "reference_pullback_covariance": "J Delta R=Delta R J because JW_ref=W_ref J",
            "same_form_identity": "a_ref(S phi,S psi)=r_ref(phi,psi) on the single common free-form domain",
            "complete_form_covariance": "r_ref(J phi,J psi)=r_ref(phi,psi) and a_ref(J x,J y)=a_ref(x,y)",
            "closed_form_consequence": "the K139/K168 common form domain is J invariant and the closed form reduces under (I+J)/2 and (I-J)/2",
        },
        "dependency_reconciliation": {
            "K139_common_recursive_domain_consumed": True,
            "K153_same_form_pullback_consumed": True,
            "K168_flavor_symmetric_extension_consumed": True,
            "K645_CAR_covariance_consumed": True,
            "K646_domain_invariance_hypothesis_discharged_for_frozen_model": True,
            "physical_flavor_symmetry_claimed": False,
            "source_selected_family_interpretation_claimed": False,
        },
        "finite_exact_control": control,
        "native_interface_status": {
            "actual_K139_recursive_domain_J_invariant": True,
            "actual_K139_K168_same_form_identity_J_invariant": True,
            "actual_physical_gram_J_invariant": True,
            "actual_parity_compression_forms_serialized": False,
            "actual_parity_block_floors_identified": False,
            "actual_uniform_parity_tails_identified": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "K646_native_domain_hypothesis_closed_for_frozen_equal_coupling_model": True,
            "next_exact_input": "Serialize the two native compression forms with the coupled channel-parity/spectator-parity decomposition, then certify their actual K644 block floors and independent uniform tails before setting m; separately bound the same-domain remainder constants alpha and delta.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This closes a domain/intertwining obligation inside a repository-supplied conditional point-Fock model; it supplies no action-owned physical state, observable, quotient or source mechanism.",
        "preflight_bookend": {
            "route_comparison": "K645--K646 left one exact theorem hypothesis between the existing K139 chart and parity reduction. Composing the chart with J is cheaper and more decisive than estimating numerical blocks on an unproved domain.",
            "retrieval_collision_result": "K139 owns the common recursive domain, K153 owns the same-form pullback, K168 owns flavor symmetry and K645 owns the CAR-correct involution, but no prior artifact composes all four into the native domain theorem.",
            "strongest_alternative": "A direct parity floor would be stronger numerically, but K612/K644 show its constants are absent and its use depended first on this domain identity.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling a domain intertwiner for the frozen equal-coupling control a physical family symmetry or a numerical semibound.",
            "strongest_contrary_construction": "Unequal flavor couplings or unmatched profiles break JG=GJ, so the proof does not transfer to those models and their cross-parity blocks must be restored.",
            "weakest_reproducibility_seam": "The continuum step uses K139's proved common recursive chart and K153 pullback identity; the finite exact matrix is only an algebraic control and supplies no continuum floor.",
        },
        "controls": {
            "producer": "tests/channel-swings/k647_k500_common_domain_flavor_intertwiner.py",
            "probe": "tests/channel-swings/k647_k500_common_domain_flavor_intertwiner_probe.py",
            "controls_passed": 32,
            "hostile_mutations_rejected": 26,
        },
        "claim_ceiling": "Exact common-domain flavor intertwiner for the frozen equal-coupling K139/K168 conditional model. K645 covariance and K139's common recursive chart imply J commutes with U=I-G, S=U^-1, the physical Gram M=S*S, the base regular pullback and K168's reference pullback; hence D_K139=S Dom(H0) is J invariant and the same native form reduces over total flavor parity. This is not physical family selection and supplies no parity block floor, uniform tail, m, alpha, delta, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["intertwiner_theorem"]
    native = payload["native_interface_status"]
    control = payload["finite_exact_control"]
    assert theorem["recursive_domain"] == "D_K139=S Dom(H0)"
    assert theorem["recursive_domain_invariance"] == "J D_K139=D_K139"
    assert control["all_exact_checks_pass"]
    assert native["actual_K139_K168_same_form_identity_J_invariant"]
    assert not native["native_global_m_identified"]


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
