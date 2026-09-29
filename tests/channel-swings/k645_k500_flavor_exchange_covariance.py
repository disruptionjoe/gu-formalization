#!/usr/bin/env python3
"""K645: exact flavor-exchange covariance of the equal-coupling K179 family."""

from __future__ import annotations

import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k645-k500-flavor-exchange-covariance.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K179 = load("k179_for_k645", "k179_matched_normal_order_coefficient_family.py")
K177 = K179.K177


def swap_impurity(value: int) -> int:
    return {0: 0, 1: 2, 2: 1}[int(value)]


def swap_letter(label: str) -> str:
    if len(label) != 2 or label[0] not in "12" or label[1] not in "+-":
        raise ValueError(f"invalid signed flavor label {label!r}")
    return ("2" if label[0] == "1" else "1") + label[1]


def swap_monomial(label: str) -> str:
    table = {
        "W_ex[p1,p1]": "W_ex[p2,p2]",
        "W_ex[p1,p2]": "W_ex[p2,p1]",
        "W_ex[p2,p1]": "W_ex[p1,p2]",
        "W_ex[p2,p2]": "W_ex[p1,p1]",
        "W_ex[h1,h1]": "W_ex[h2,h2]",
        "W_ex[h2,h2]": "W_ex[h1,h1]",
    }
    return table[label]


def partner_key(term: dict[str, Any]) -> tuple[Any, ...]:
    return (
        int(term["order"]),
        swap_impurity(term["seed_impurity"]),
        tuple(swap_letter(label) for label in term["input_letters"]),
        swap_letter(term["newest"]),
        int(term["old_position"]),
    )


def term_key(term: dict[str, Any]) -> tuple[Any, ...]:
    return (
        int(term["order"]),
        int(term["seed_impurity"]),
        tuple(term["input_letters"]),
        term["newest"],
        int(term["old_position"]),
    )


def swap_orbital(orbital: int, mode_count: int) -> int:
    if orbital < 2:
        return 1 - orbital
    shifted = orbital - 2
    species, mode = divmod(shifted, mode_count)
    flavor, polarity = divmod(species, 2)
    swapped_species = 2 * (1 - flavor) + polarity
    return 2 + swapped_species * mode_count + mode


def permutation_phase(bits: int, mode_count: int) -> int:
    occupied = [
        orbital
        for orbital in range(2 + 4 * mode_count)
        if (bits >> orbital) & 1
    ]
    permuted = [swap_orbital(orbital, mode_count) for orbital in occupied]
    inversions = sum(
        permuted[left] > permuted[right]
        for left in range(len(permuted))
        for right in range(left + 1, len(permuted))
    )
    return -1 if inversions % 2 else 1


def output_bits(term: dict[str, Any]) -> tuple[int, int]:
    order = int(term["order"])
    mode_count = order + 1
    impurity = int(term["output_impurity"])
    bits = 0 if impurity == 0 else 1 << (impurity - 1)
    removed = int(term["old_position"]) - 1
    for mode, label in enumerate(term["input_letters"]):
        if mode == removed:
            continue
        letter = (int(label[0]), label[1])
        bits |= 1 << K177.bath_orbital(letter, mode, mode_count)
    newest = (int(term["newest"][0]), term["newest"][1])
    bits |= 1 << K177.bath_orbital(newest, order, mode_count)
    return bits, mode_count


def kernel_body(term: dict[str, Any]) -> str:
    return term["output_kernel_formula"]["ordered_kernel"].split("*", 1)[1]


def verify_family(terms: list[dict[str, Any]]) -> dict[str, Any]:
    index = {term_key(term): position for position, term in enumerate(terms)}
    if len(index) != len(terms):
        raise AssertionError("K179 term identity is not unique")
    visited: set[int] = set()
    phase_counts: Counter[int] = Counter()
    orbit_counts: Counter[int] = Counter()
    monomial_orbits: Counter[tuple[str, str]] = Counter()
    for position, term in enumerate(terms):
        partner_position = index.get(partner_key(term))
        if partner_position is None:
            raise AssertionError("flavor-swapped K179 partner is absent")
        partner = terms[partner_position]
        if partner_key(partner) != term_key(term):
            raise AssertionError("flavor swap is not involutive")
        if partner_position == position:
            raise AssertionError("unexpected fixed K179 term")
        if swap_impurity(term["output_impurity"]) != int(partner["output_impurity"]):
            raise AssertionError("output impurity does not swap")
        if swap_monomial(term["operator_monomial_id"]) != partner["operator_monomial_id"]:
            raise AssertionError("operator monomial does not swap")
        if kernel_body(term) != kernel_body(partner):
            raise AssertionError("flavor-blind analytic kernel changed under swap")
        bits, mode_count = output_bits(term)
        phase = permutation_phase(bits, mode_count)
        phase_counts[phase] += 1
        expected = int(term["exact_operator_coefficient"]) * phase
        if int(partner["exact_operator_coefficient"]) != expected:
            raise AssertionError("CAR coefficient missed the output-wedge phase")
        if position not in visited:
            visited.update((position, partner_position))
            orbit_counts[int(term["order"])] += 1
            monomial_orbits[tuple(sorted((term["operator_monomial_id"], partner["operator_monomial_id"])))] += 1
    if len(visited) != len(terms):
        raise AssertionError("flavor orbits do not cover the family")
    return {
        "terms": len(terms),
        "two_element_orbits": len(terms) // 2,
        "fixed_terms": 0,
        "orbits_by_order": {str(order): orbit_counts[order] for order in sorted(orbit_counts)},
        "output_wedge_phase_counts": {str(phase): phase_counts[phase] for phase in (-1, 1)},
        "monomial_orbit_counts": {
            " <-> ".join(pair): count for pair, count in sorted(monomial_orbits.items())
        },
        "all_partners_present": True,
        "swap_is_involutive": True,
        "analytic_kernel_bodies_invariant": True,
        "CAR_coefficients_transform_by_output_wedge_phase": True,
    }


def build() -> dict[str, Any]:
    terms = K179.coefficient_family(12)
    replay = verify_family(terms)
    extended = verify_family(K179.coefficient_family(14))
    k139 = json.loads((ROOT / "lab/process/k139-signed-boundary-inverse-profile-universality-wave.json").read_text())
    k168 = json.loads((ROOT / "lab/process/k168-flavor-symmetric-reference-extension-wave.json").read_text())
    k643 = json.loads((ROOT / "lab/process/k643-k500-bath-sector-boundary-reduction.json").read_text())
    assert K179.family_digest(terms) == "ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686"
    assert k139["doubled_counterterm_and_exchange"]["equal_particle_and_hole_couplings_give_four_g_squared_times_identity_on_the_rook_vertices"]
    assert k168["reference_extension"]["flavor_symmetric"]
    assert k168["native_compatibility"]["signed_flavor_swap_intertwines"]
    assert k643["native_replay"]["total_bath_number_preserved_by_every_exchange_monomial"]
    return {
        "schema_version": "1.0",
        "result_id": "K645-K500-FLAVOR-EXCHANGE-COVARIANCE",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The frozen equal-coupling K139/K168/K179 conditional point-Fock family under interchange of flavor labels one and two, including the normalized fermionic exterior-basis phase.",
        "gu_typed_objects": {
            "carrier": "hard-core C3 impurity tensor Gamma_-(L2(R;C4)) with the two impurity and four signed bath species exchanged flavorwise",
            "form": "the equal-coupling K179 matched normal-order exchange family and flavor-symmetric K168 reference extension",
            "pairing": "the normalized CAR exterior Hilbert pairing in the fixed global orbital order",
            "involution": "the second-quantized unitary flavor permutation J with J^2=I",
            "result": "flavor-exchange covariance MAP-TYPE=unitary term-orbit intertwiner",
            "target": "a symmetry reduction of K643/K644's sector-local operator-valued lower problem",
        },
        "complete_family_replay": {
            **replay,
            "orders": [2, 12],
            "family_sha256": K179.family_digest(terms),
            "naive_sign_preservation_is_false": replay["output_wedge_phase_counts"]["-1"] > 0,
        },
        "finite_order_theorem": {
            "automaton_equivariance": "0<->i hard-core words and their matched older-letter contractions are carried bijectively by 1<->2 at every finite order",
            "kernel_equivariance": "the cumulative resolvent denominators and momentum-variable incidence are flavor blind at equal couplings",
            "fermionic_phase": "the canonical exterior basis acquires the sign of the induced permutation on occupied impurity and bath orbitals",
            "coefficient_identity": "c(swap(term))=epsilon_out(term)c(term), where epsilon_out is the exact output-wedge permutation phase",
            "operator_identity": "J W_ex^(<=N) J=W_ex^(<=N) for every finite N in the equal-coupling family",
            "bath_number_compatibility": "J commutes with total bath number, so the covariance restricts to every K643 sector",
            "monomial_orbits": [
                "W_ex[h1,h1]<->W_ex[h2,h2]",
                "W_ex[p1,p1]<->W_ex[p2,p2]",
                "W_ex[p1,p2]<->W_ex[p2,p1]",
            ],
        },
        "limit_interface": {
            "cutoff_rule": "equal flavor couplings, matched profiles, flavor-blind free energy and the doubled symmetric endpoint counterterm make every K139 cutoff commute with J",
            "norm_resolvent_rule": "a norm-resolvent limit of self-adjoint J-commuting cutoffs commutes with bounded J",
            "K168_rule": "diag(-2,1,1) commutes with interchange of impurity labels one and two",
            "conditional_complete_form_consequence": "the frozen equal-coupling K139/K168 reference form has a J-invariant closed domain and reduces over J parity, provided the native same-form identification required by K642/K644 is made on that domain",
            "physical_flavor_symmetry_claimed": False,
            "source_selected_family_interpretation_claimed": False,
        },
        "extended_controls": {
            "maximum_order": 14,
            "terms_checked": extended["terms"],
            "two_element_orbits": extended["two_element_orbits"],
            "all_controls_pass": all(extended[key] for key in ("all_partners_present", "swap_is_involutive", "analytic_kernel_bodies_invariant", "CAR_coefficients_transform_by_output_wedge_phase")),
            "control_extends_serialized_family_truth": False,
        },
        "native_interface_status": {
            "equal_coupling_coefficient_covariance_proved": True,
            "K643_sector_compatibility_proved": True,
            "full_native_K139_K168_to_K642_form_identity_proved": False,
            "native_parity_floors_identified": False,
            "native_uniform_tail_identified": False,
            "native_global_m_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "flavor_swap_is_exact_operator_symmetry_for_frozen_equal_coupling_family": True,
            "naive_term_sign_matching_rejected": True,
            "next_exact_input": "Use the J-invariant common domain to split each K643 bath sector into total flavor parity, identify the actual K139/K168 form on those compressions, and certify parity-local block floors and uniform tails before setting m=min(m_plus,m_minus).",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is an internal symmetry of a repository-supplied equal-coupling conditional model; it neither identifies physical families nor supplies an action-owned state or observable.",
        "preflight_bookend": {
            "route_comparison": "Before estimating twenty-one unknown K644 block constants, test the exact equal-coupling discrete symmetry already present in K179; a proved reducing involution removes cross-parity obligations without replacing the operator-valued spectator carrier.",
            "retrieval_collision_result": "K168 declares flavor symmetry and K179 serializes all coefficient signs, but no current artifact checks the fermionic permutation phase or proves covariance of the complete term family.",
            "strongest_alternative": "Direct numerical parity floors would be stronger, but K612/K644 show the same-form block data are not serialized; the symmetry test is the cheapest native reduction available now.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling conditional equal-coupling flavor covariance a physical family symmetry, a source-selected observation, or a numerical lower bound.",
            "strongest_contrary_construction": "Five hundred sixteen serialized terms change coefficient sign under the swap because the canonical exterior basis reorders; a label-only coefficient comparison gives the wrong covariance test.",
            "weakest_reproducibility_seam": "The exact replay covers the serialized orders two through twelve; the all-finite-order statement uses the unchanged automaton and equal-coupling kernel formula, while native use still needs the complete common-domain form identity.",
        },
        "controls": {
            "producer": "tests/channel-swings/k645_k500_flavor_exchange_covariance.py",
            "probe": "tests/channel-swings/k645_k500_flavor_exchange_covariance_probe.py",
            "controls_passed": 31,
            "hostile_mutations_rejected": 25,
        },
        "claim_ceiling": "Exact flavor-exchange covariance for the frozen equal-coupling K179 family. All 2,958 serialized terms form 1,479 two-element swap orbits; 516 terms require a negative output-wedge phase, so naive coefficient matching is false. The hard-core automaton and flavor-blind kernels give the same covariance at every finite order, and the symmetric K139 cutoff/K168 limit interface reduces over total flavor parity once the missing native same-form identity is supplied. This is not physical family selection and supplies no parity floor, uniform tail, m, alpha, delta, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion.",
    }


def validate(payload: dict[str, Any]) -> None:
    replay = payload["complete_family_replay"]
    assert replay["terms"] == 2958 and replay["two_element_orbits"] == 1479
    assert replay["output_wedge_phase_counts"] == {"-1": 516, "1": 2442}
    assert replay["CAR_coefficients_transform_by_output_wedge_phase"]
    assert payload["finite_order_theorem"]["operator_identity"].endswith("equal-coupling family")
    assert payload["limit_interface"]["physical_flavor_symmetry_claimed"] is False
    assert payload["native_interface_status"]["native_global_m_identified"] is False


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
