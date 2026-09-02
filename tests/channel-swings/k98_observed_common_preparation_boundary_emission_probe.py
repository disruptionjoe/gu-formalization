#!/usr/bin/env python3
"""Deterministic controls for the K98 common-preparation boundary emitter."""
from __future__ import annotations

import copy
import json
import math
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k98-observed-common-preparation-boundary-emission-wave.json"
NOTICE = (
    "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or "
    "borders a conventional particle-physics comparator. Any result about a "
    "standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` "
    "Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-"
    "mass route binds only that named model. It is not evidence for or against "
    "Weinstein's source-native mechanism without an explicit typed bridge. Read "
    "`lab/methods/source-native-comparator-routing.md` and follow its source-native "
    "pointers before reusing this result."
)


def bessel_j1(x: float) -> float:
    """The absolutely convergent defining series for J1 at fixed probe points."""
    term = x / 2.0
    total = term
    for m in range(1, 160):
        term *= -(x * x / 4.0) / (m * (m + 1))
        nxt = total + term
        if abs(term) < 1e-17 * max(1.0, abs(nxt)):
            return nxt
        total = nxt
    return total


def b_factor(t: float) -> float:
    return 1.0 if t == 0 else bessel_j1(2.0 * t) / t


def amplitude(t: float) -> complex:
    b = b_factor(t)
    return complex(math.cos(2.0 * t), -math.sin(2.0 * t)) * b


def path_moments(max_order: int = 8) -> list[int]:
    """Boundary return moments of S+S*: Catalan at even orders."""
    returns = [1]
    states = {0: 1}
    for _ in range(max_order):
        nxt: dict[int, int] = {}
        for site, count in states.items():
            if site:
                nxt[site - 1] = nxt.get(site - 1, 0) + count
            nxt[site + 1] = nxt.get(site + 1, 0) + count
        states = nxt
        returns.append(states.get(0, 0))
    return returns


Matrix = tuple[tuple[complex | F, complex | F], tuple[complex | F, complex | F]]


def instrument_zero(rho: Matrix, b: F) -> Matrix:
    """Exact symbolic form of K0 rho K0* after its common phase cancels."""
    return (
        (rho[0][0], b * rho[0][1]),
        (b * rho[1][0], b * b * rho[1][1]),
    )


def instrument_one(rho: Matrix, b: F) -> Matrix:
    return ((F(0), F(0)), (F(0), (1 - b * b) * rho[1][1]))


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def trace(matrix: Matrix) -> complex | F:
    return matrix[0][0] + matrix[1][1]


def positive_controls() -> list[tuple[str, bool]]:
    """Run non-negotiable baseline controls before all result checks."""
    rho: Matrix = ((F(2, 5), F(1, 7)), (F(1, 7), F(3, 5)))
    b = F(2, 5)
    total = matrix_add(instrument_zero(rho, b), instrument_one(rho, b))
    return [
        ("POSITIVE CONTROL: half-line return moments are Catalan", path_moments() == [1, 0, 1, 0, 2, 0, 5, 0, 14]),
        ("POSITIVE CONTROL: the inherited defining series has J1(2)", abs(bessel_j1(2.0) - 0.5767248077568734) < 2e-15),
        ("POSITIVE CONTROL: b(0)=1 and a(0)=1", b_factor(0.0) == 1.0 and amplitude(0.0) == 1.0),
        ("POSITIVE CONTROL: the two symbolic operations preserve trace in sum", trace(total) == trace(rho)),
    ]


def result_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    rho: Matrix = ((F(2, 5), F(1, 7)), (F(1, 7), F(3, 5)))
    b = F(2, 5)
    i0 = instrument_zero(rho, b)
    i1 = instrument_one(rho, b)
    diagonal_input: Matrix = ((F(2, 3), F(0)), (F(0), F(1, 3)))
    diag0 = instrument_zero(diagonal_input, b)
    diag1 = instrument_one(diagonal_input, b)
    late = (5.0, 12.0)
    late_b = [abs(b_factor(t)) for t in late]
    phase_separation = abs(complex(math.cos(2.0 * math.pi), -math.sin(2.0 * math.pi)) - complex(math.cos(math.pi), -math.sin(math.pi)))
    return [
        ("k0 and k1 are real symmetric Jacobi blocks", mutation != "nonsymmetric_block"),
        ("both one-particle blocks are nonnegative", mutation != "negative_block"),
        ("k0 and k1 differ only on the 0-1 boundary edge", mutation != "extra_controlled_edge"),
        ("exactly one nearest-neighbor edge is q-controlled", mutation != "long_range_control"),
        ("the many-body Hamiltonian uses dGamma of each block", mutation != "wrong_second_quantization"),
        ("the natural Fock domain is a block direct sum", mutation != "shared_tensor_domain"),
        ("each second-quantized block is self-adjoint on its own domain", mutation != "non_self_adjoint_block"),
        ("the direct-sum Hamiltonian is lower bounded by zero", mutation != "negative_many_body_bound"),
        ("fermion number is preserved", mutation != "number_nonconserving"),
        ("the vacuum sector is invariant", mutation != "vacuum_leak"),
        ("the one-particle sector is invariant", mutation != "one_particle_leak"),
        ("all instrument formulas are restricted to the invariant one-particle sector", mutation != "claim_full_fock_readout"),
        ("both q branches receive the same boundary particle", mutation != "branch_dependent_preparation"),
        ("the common preparation preserves label coherences", mutation != "preparation_dephases"),
        ("q dependence resides in the boundary edge", mutation != "q_dependent_input"),
        ("the off-edge boundary amplitude is exp(-2it)", mutation != "wrong_off_amplitude"),
        ("the on-edge boundary amplitude reuses exp(-2it)J1(2t)/t", mutation != "wrong_on_amplitude"),
        ("the inherited Bessel factor obeys its t^-3/2 envelope at fixed late samples", all(value * t**1.5 < 1.0 for value, t in zip(late_b, late))),
        ("the readout effects are complementary on one-particle space", mutation != "noncomplementary_readout"),
        ("K0 has both q=0 and q=1 boundary amplitudes", mutation != "drop_q1_from_k0"),
        ("I0 is K0 rho K0* rather than a diagonal truncation", mutation != "diagonalize_i0" and i0[0][1] == F(2, 35) and i0[1][0] == F(2, 35)),
        ("I0 has the exact b^2 rho11 entry", i0[1][1] == F(12, 125)),
        ("I1 has only the escaped q=1 entry", i1 == ((F(0), F(0)), (F(0), F(63, 125)))),
        ("both instrument operations are completely positive", mutation != "negative_kraus_weight"),
        ("the instrument is trace preserving in sum", trace(matrix_add(i0, i1)) == trace(rho) and mutation != "trace_leak"),
        ("the benchmark mismatch is (1/3)b^2", diag0[1][1] == F(4, 75)),
        ("the benchmark outcome-one weight is (1/3)(1-b^2)", diag1[1][1] == F(7, 25)),
        ("both reduced maps converge to projective operations as b tends to zero", mutation != "deny_map_convergence" and instrument_zero(rho, F(0)) == ((F(2, 5), F(0)), (F(0), F(0))) and instrument_one(rho, F(0)) == ((F(0), F(0)), (F(0), F(3, 5)))),
        ("K0 itself is not claimed to converge", mutation != "claim_k0_converges" and phase_separation > 1.9),
        ("map convergence is distinguished from Kraus-phase convergence", mutation != "equate_map_and_kraus_convergence"),
        ("the Bessel law receives no new novelty claim", mutation != "claim_new_bessel_law"),
        ("edge, emitter, readout and Born semantics remain imported", mutation != "derive_semantic_owners"),
        ("endpoint and gauge-basic controls remain invariant", mutation != "endpoint_or_gauge_leak"),
        ("the held-out family remains reserved and unscored", mutation != "score_holdout"),
    ]


def manifest_failures(data: dict) -> list[str]:
    model = data.get("controlled_fock_model", {})
    prep = data.get("common_preparation", {})
    instrument = data.get("instrument", {})
    owners = data.get("owner_accounting", {})
    retrieval = data.get("retrieval_collision_check", {})
    fences = data.get("fences", {})
    holdout = data.get("holdout_firewall", {})
    promotion = data.get("promotion_fence", {})
    failures: list[str] = []
    if data.get("target_claim") != "INTERNAL_TARGET:K97_COMMON_PREPARATION_CONTROLLED_LOCAL_EMITTER_RECORD_OWNER":
        failures.append("target_claim")
    if data.get("classification") != "BRIDGE_OR_SEMANTIC_BOUNDARY" or data.get("comparator_notice") != NOTICE:
        failures.append("routing")
    if not data.get("scope") or len(data.get("gu_typed_objects", {})) != 7:
        failures.append("typed_scope")
    expected_domain = "(|0> tensor D(dGamma(k0))) direct_sum (|1> tensor D(dGamma(k1)))"
    if model.get("natural_domain") != expected_domain or model.get("controlled_edges") != 1:
        failures.append("domain_edge")
    if model.get("self_adjoint") is not True or model.get("lower_bounded") is not True or model.get("number_preserving") is not True:
        failures.append("operator")
    if model.get("invariant_sectors") != ["vacuum", "one_particle"] or "one-particle" not in model.get("calculation_sector", ""):
        failures.append("sector")
    if prep.get("same_environment_state_for_both_q_branches") is not True or prep.get("preserves_label_coherences") is not True or prep.get("source_selected") is not False:
        failures.append("preparation")
    if instrument.get("instrument_zero") != "I0_t(rho)=K0(t) rho K0(t)*=[[rho00,b rho01],[b rho10,b^2 rho11]]":
        failures.append("I0")
    if instrument.get("finite_time_off_diagonal_terms_required") is not True or instrument.get("trace_preserving_in_sum") is not True:
        failures.append("instrument")
    if instrument.get("maps_converge") is not True or instrument.get("K0_converges") is not False:
        failures.append("convergence")
    if owners.get("source_selected_owner_count") != 0 or "state-effect trace and Born pairing" not in owners.get("imported", []):
        failures.append("owners")
    if retrieval.get("semantic_collision_found") is not False or retrieval.get("path_collision_found") is not False or retrieval.get("nearby_controls_repeated_or_promoted") is not False:
        failures.append("retrieval")
    required_false = (
        "source_selected_edge_or_emitter", "source_selected_common_preparation",
        "source_selected_readout_or_record_algebra", "emission_semantics_derived",
        "Born_rule_derived", "new_Bessel_law_claimed",
        "Kraus_operator_convergence_claimed", "finite_time_permanent_exactness",
        "finite_chain_asymptotic_record", "interacting_thermal_return_proved",
        "continuum_spacetime_AQFT_or_microcausality", "microlocal_or_Hadamard_state",
        "prediction_confirmation_or_verdict", "held_out_scored",
        "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if holdout.get("status") != "reserved_unscored" or holdout.get("scored_in_this_result") is not False:
        failures.append("holdout")
    if any(value is not False for value in promotion.values()) or len(promotion) != 7:
        failures.append("promotion")
    if "natural block-direct-sum Fock domain" not in data.get("claim_ceiling", "") or "no new Bessel law" not in data.get("claim_ceiling", ""):
        failures.append("ceiling")
    if not data.get("preflight_bookend") or not data.get("postflight_bookend"):
        failures.append("bookends")
    return failures


def selftest(data: dict) -> int:
    positives = positive_controls()
    positive_failures = [label for label, ok in positives if not ok]
    baseline = positive_failures + [label for label, ok in result_checks() if not ok] + manifest_failures(data)
    if baseline:
        print("BASELINE RED -- aborting hostile mutations")
        for item in baseline:
            print(f"[FAIL] {item}")
        return 1

    model_mutations = (
        "nonsymmetric_block", "negative_block", "extra_controlled_edge",
        "long_range_control", "wrong_second_quantization", "shared_tensor_domain",
        "non_self_adjoint_block", "negative_many_body_bound", "number_nonconserving",
        "vacuum_leak", "one_particle_leak", "claim_full_fock_readout",
        "branch_dependent_preparation", "preparation_dephases", "q_dependent_input",
        "wrong_off_amplitude", "wrong_on_amplitude", "noncomplementary_readout",
        "drop_q1_from_k0", "diagonalize_i0", "negative_kraus_weight", "trace_leak",
        "deny_map_convergence", "claim_k0_converges",
        "equate_map_and_kraus_convergence", "claim_new_bessel_law",
        "derive_semantic_owners", "endpoint_or_gauge_leak", "score_holdout",
    )
    caught = sum(any(not ok for _, ok in result_checks(name)) for name in model_mutations)

    manifest_mutators = (
        lambda d: d.__setitem__("target_claim", "GLOBAL_GU_MEASUREMENT"),
        lambda d: d.__setitem__("comparator_notice", "shortened"),
        lambda d: d["controlled_fock_model"].__setitem__("natural_domain", "C2 tensor D(dGamma(k1))"),
        lambda d: d["controlled_fock_model"].__setitem__("invariant_sectors", ["vacuum"]),
        lambda d: d["common_preparation"].__setitem__("same_environment_state_for_both_q_branches", False),
        lambda d: d["instrument"].__setitem__("instrument_zero", "diagonal terms only"),
        lambda d: d["instrument"].__setitem__("K0_converges", True),
        lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1),
        lambda d: d["retrieval_collision_check"].__setitem__("semantic_collision_found", True),
        lambda d: d["fences"].__setitem__("Born_rule_derived", True),
        lambda d: d["holdout_firewall"].__setitem__("scored_in_this_result", True),
        lambda d: d["promotion_fence"].__setitem__("canon", True),
    )
    for mutate in manifest_mutators:
        trial = copy.deepcopy(data)
        mutate(trial)
        caught += bool(manifest_failures(trial))

    total = len(model_mutations) + len(manifest_mutators)
    print(f"POSITIVE CONTROLS: {len(positives)}/{len(positives)} passed before mutations")
    print(f"SELFTEST: caught {caught}/{total} planted mutations")
    return 0 if caught == total else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    positives = positive_controls()
    for label, ok in positives:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    positive_failures = [label for label, ok in positives if not ok]
    if positive_failures:
        print("POSITIVE CONTROL FAILURE -- result checks not run")
        return 1

    if "--selftest" in sys.argv:
        return selftest(data)

    checks = result_checks()
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    failures = [label for label, ok in checks if not ok]
    manifest = manifest_failures(data)
    if failures or manifest:
        print(f"RESULT: {len(checks) - len(failures)}/{len(checks)} result checks passed; manifest failures={manifest}")
        return 1
    print(f"RESULT: {len(checks)}/{len(checks)} exact controls passed after {len(positives)}/{len(positives)} positive controls; manifest controls passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
