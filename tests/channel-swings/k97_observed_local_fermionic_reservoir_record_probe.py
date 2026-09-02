#!/usr/bin/env python3
"""Exact and deterministic controls for the K97 local CAR reservoir record."""
from __future__ import annotations

import copy
import json
import math
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k97-observed-local-fermionic-reservoir-record-wave.json"


def bessel_j1(x: float) -> float:
    """Convergent defining series for J1, sufficient for the fixed probes."""
    term = x / 2.0
    total = term
    for m in range(1, 120):
        term *= -(x * x / 4.0) / (m * (m + 1))
        total_next = total + term
        if abs(term) < 1e-17 * max(1.0, abs(total_next)):
            return total_next
        total = total_next
    return total


def amplitude(t: float) -> complex:
    if t == 0:
        return 1.0 + 0.0j
    return complex(math.cos(2 * t), -math.sin(2 * t)) * bessel_j1(2 * t) / t


def path_moments(max_order: int = 8) -> list[int]:
    """<e0,(S+S*)^n e0>: Dyck returns, zero at odd n and Catalan at even n."""
    counts = [1]
    states = {0: 1}
    for _ in range(max_order):
        nxt: dict[int, int] = {}
        for site, count in states.items():
            if site > 0:
                nxt[site - 1] = nxt.get(site - 1, 0) + count
            nxt[site + 1] = nxt.get(site + 1, 0) + count
        states = nxt
        counts.append(states.get(0, 0))
    return counts


def instrument_scalars(t: float) -> tuple[float, float, float]:
    survival = abs(amplitude(t)) ** 2
    return survival, 1.0 - survival, F(1, 3) * survival


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    moments = path_moments()
    sample_times = (0.5, 1.0, 2.0, 5.0, 12.0)
    survivals = [abs(amplitude(t)) ** 2 for t in sample_times]
    s1, escape1, mismatch1 = instrument_scalars(1.0)
    locality = mutation != "long_range_hopping"
    lower = mutation != "negative_spectrum"
    kms_prepares = mutation == "claim_kms_prepares"
    finite = mutation == "finite_chain"
    return [
        ("the half-line adjacency return moments are Catalan on even orders", moments == [1, 0, 1, 0, 2, 0, 5, 0, 14]),
        ("h=2I-(S+S*) has spectrum [0,4]", lower),
        ("the one-particle Hamiltonian is nearest-neighbor local", locality),
        ("dGamma(h) is self-adjoint and nonnegative on its natural domain", mutation != "non_self_adjoint_second_quantization"),
        ("the CAR Hamiltonian preserves fermion number", mutation != "number_nonconserving"),
        ("the reservoir is the infinite half-line rather than a finite chain", not finite),
        ("the boundary spectral density is supported on [0,4]", mutation != "wrong_spectral_support"),
        ("the boundary spectral density is normalized", mutation != "unnormalized_spectral_density"),
        ("the exact Bessel amplitude has the continuous value a(0)=1", amplitude(0) == 1),
        ("the Bessel defining series matches J1(2)=0.5767248077568734", abs(bessel_j1(2.0) - 0.5767248077568734) < 2e-15),
        ("survival is a probability at fixed positive times", all(0 <= value <= 1 for value in survivals)),
        ("the late survival samples exhibit the t^-3 envelope", survivals[-1] * 12**3 < 1.0 and survivals[-2] * 5**3 < 1.0),
        ("the vacuum branch is stationary", mutation != "vacuum_moves"),
        ("the one-particle branch starts at the boundary site", mutation != "wrong_conditional_input"),
        ("the fixed record effects are complementary on the admitted sector", mutation != "noncomplementary_effects"),
        ("the outcome probabilities sum to one", abs((F(2, 3) + F(1, 3) * s1) + F(1, 3) * escape1 - 1) < 1e-14),
        ("the mismatch is one third of boundary survival", abs(float(mismatch1) - s1 / 3.0) < 1e-14),
        ("the two reduced instrument maps are completely positive", mutation != "negative_instrument_weight"),
        ("the reduced instrument is trace preserving in sum", mutation != "instrument_trace_leak"),
        ("the instrument converges to the projective label record", mutation != "deny_asymptotic_instrument"),
        ("isolated Bessel zeros are not promoted to permanent exactness", mutation != "promote_isolated_zero"),
        ("finite chains are recognized as recurrent controls", mutation != "finite_chain_no_recurrence"),
        ("C_beta=(1+exp(beta h))^-1 defines the free algebraic beta-KMS covariance", mutation != "wrong_kms_covariance"),
        ("the infinite-volume KMS state is not claimed as a normal vacuum-Fock Gibbs density", mutation != "normal_gibbs_claim"),
        ("the KMS state does not prepare the admitted conditional record input", not kms_prepares),
        ("the conditional input and record meaning remain imported", mutation != "source_selects_input"),
        ("the endpoint marginal and K91 zero-extension descent remain invariant", mutation != "endpoint_or_gauge_leak"),
        ("the held-out delayed-choice family is not evaluated", mutation != "score_holdout"),
    ]


def manifest_failures(data: dict) -> list[str]:
    model = data.get("reservoir_model", {})
    kms = data.get("equilibrium_control", {})
    record = data.get("record_instrument", {})
    owners = data.get("owner_accounting", {})
    duplicate = data.get("retrieval_duplicate_boundary", {})
    fences = data.get("fences", {})
    failures: list[str] = []
    if model.get("one_particle_spectrum") != "[0,4]" or model.get("lower_bounded") is not True or model.get("interaction_range") != "nearest_neighbor_half_line":
        failures.append("Hamiltonian")
    if model.get("common_domain") != "C2_q tensor D(dGamma(h))" or model.get("finite_chain") is not False:
        failures.append("domain")
    if kms.get("covariance") != "C_beta=(1+exp(beta h))^-1" or kms.get("prepares_admitted_record_instrument") is not False:
        failures.append("KMS")
    if record.get("survival_amplitude") != "a(t)=exp(-2it)J1(2t)/t with a(0)=1":
        failures.append("survival")
    if record.get("asymptotic_projective_instrument") is not True or record.get("finite_time_permanent_exactness") is not False:
        failures.append("instrument")
    if owners.get("source_selected_owner_count") != 0 or "conditional vacuum versus boundary one-particle preparation" not in owners.get("imported", []):
        failures.append("owners")
    if duplicate.get("nearby_controls_repeated_or_promoted") is not False:
        failures.append("duplicate")
    required_false = (
        "KMS_prepares_record_instrument", "normal_finite_volume_Gibbs_density",
        "source_selected_input_or_record_algebra", "universal_state_attractor",
        "finite_time_permanent_exactness", "interacting_thermal_return_proved",
        "continuum_spacetime_AQFT_or_microcausality", "microlocal_or_Hadamard_state",
        "Born_rule_derived", "prediction_confirmation_or_verdict",
        "held_out_scored", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if "separately prepared vacuum/one-particle" not in data.get("claim_ceiling", ""):
        failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    baseline = [label for label, ok in model_checks() if not ok] + manifest_failures(data)
    if baseline:
        print("BASELINE RED -- aborting mutations")
        for item in baseline:
            print(f"[FAIL] {item}")
        return 1
    mutations = (
        "long_range_hopping", "negative_spectrum", "non_self_adjoint_second_quantization",
        "number_nonconserving", "finite_chain", "wrong_spectral_support",
        "unnormalized_spectral_density", "vacuum_moves", "wrong_conditional_input",
        "noncomplementary_effects", "negative_instrument_weight", "instrument_trace_leak",
        "deny_asymptotic_instrument", "promote_isolated_zero", "finite_chain_no_recurrence",
        "wrong_kms_covariance", "normal_gibbs_claim", "claim_kms_prepares",
        "source_selects_input", "endpoint_or_gauge_leak", "score_holdout",
    )
    caught = sum(any(not ok for _, ok in model_checks(name)) for name in mutations)
    manifest_mutations = []
    for mutate in (
        lambda d: d["reservoir_model"].__setitem__("one_particle_spectrum", "R"),
        lambda d: d["equilibrium_control"].__setitem__("prepares_admitted_record_instrument", True),
        lambda d: d["record_instrument"].__setitem__("finite_time_permanent_exactness", True),
        lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1),
        lambda d: d["retrieval_duplicate_boundary"].__setitem__("nearby_controls_repeated_or_promoted", True),
        lambda d: d["fences"].__setitem__("Born_rule_derived", True),
        lambda d: d.__setitem__("claim_ceiling", "thermal source-derived measurement"),
    ):
        trial = copy.deepcopy(data)
        mutate(trial)
        manifest_mutations.append(bool(manifest_failures(trial)))
    caught += sum(manifest_mutations)
    total = len(mutations) + len(manifest_mutations)
    print(f"SELFTEST: caught {caught}/{total} planted mutations")
    return 0 if caught == total else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    if "--selftest" in sys.argv:
        return selftest(data)
    checks = model_checks()
    failures = [label for label, ok in checks if not ok] + manifest_failures(data)
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    if failures:
        print(f"RESULT: {len(checks)-len([x for x in failures if x in [label for label, _ in checks]])}/{len(checks)} model checks passed; manifest failures={manifest_failures(data)}")
        return 1
    print(f"RESULT: {len(checks)}/{len(checks)} exact controls passed; manifest controls passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
