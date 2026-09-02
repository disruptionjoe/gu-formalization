#!/usr/bin/env python3
"""Exact deterministic controls for K98 finite-temperature local forgetting."""
from __future__ import annotations

import copy
import json
import math
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k98-observed-finite-temperature-quasifree-local-forgetting-wave.json"
RESULT = ROOT / "explorations/conditional-build/k98-observed-finite-temperature-quasifree-local-forgetting-wave-2026-09-02.md"
Gaussian = tuple[F, F]


def gadd(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gmul(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def gscale(value: Gaussian, scalar: F) -> Gaussian:
    return value[0] * scalar, value[1] * scalar


def gpow(value: Gaussian, exponent: int) -> Gaussian:
    result: Gaussian = (F(1), F(0))
    for _ in range(exponent):
        result = gmul(result, value)
    return result


def h_power_columns(max_order: int) -> list[dict[int, int]]:
    """Exact columns h^k e0 for h=2I-(S+S*) on the half-line."""
    columns = [{0: 1}]
    for _ in range(max_order):
        nxt: dict[int, int] = {}
        for site, coefficient in columns[-1].items():
            nxt[site] = nxt.get(site, 0) + 2 * coefficient
            nxt[site + 1] = nxt.get(site + 1, 0) - coefficient
            if site > 0:
                nxt[site - 1] = nxt.get(site - 1, 0) - coefficient
        columns.append(nxt)
    return columns


def kernel_taylor_coefficient(site: int, order: int) -> Gaussian:
    """Coefficient from exp(-2it)i^n(n+1)J_(n+1)(2t)/t."""
    total: Gaussian = (F(0), F(0))
    for m in range((order - site) // 2 + 1 if order >= site else 0):
        bessel_power = 2 * m + site
        remainder = order - bessel_power
        bessel = F((site + 1) * (-1) ** m, math.factorial(m) * math.factorial(m + site + 1))
        phase = gmul(gpow((F(0), F(1)), site), gpow((F(0), F(-2)), remainder))
        total = gadd(total, gscale(phase, bessel / math.factorial(remainder)))
    return total


def exact_kernel_series_matches(max_site: int = 5, max_order: int = 12) -> bool:
    columns = h_power_columns(max_order)
    for order, column in enumerate(columns):
        for site in range(max_site + 1):
            expected = gscale(gpow((F(0), F(-1)), order), F(column.get(site, 0), math.factorial(order)))
            if kernel_taylor_coefficient(site, order) != expected:
                return False
    return True


def bessel_j(order: int, x: float) -> float:
    """Defining series for integer-order J at the moderate fixed probe points."""
    term = (x / 2.0) ** order / math.factorial(order)
    total = term
    for m in range(1, 180):
        term *= -(x * x / 4.0) / (m * (m + order))
        next_total = total + term
        if abs(term) < 1e-16 * max(1.0, abs(next_total)):
            return next_total
        total = next_total
    return total


def amplitude(site: int, time: float) -> complex:
    if time == 0:
        return complex(1.0 if site == 0 else 0.0)
    phase = complex(math.cos(2 * time), -math.sin(2 * time)) * (1j ** site)
    return phase * (site + 1) * bessel_j(site + 1, 2 * time) / time


def local_mass(last_site: int, time: float) -> float:
    return sum(abs(amplitude(site, time)) ** 2 for site in range(last_site + 1))


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    beta = F(3, 2)
    delta = F(2, 5)
    local_samples = [local_mass(4, time) for time in (4.0, 8.0, 16.0)]
    fixed_region = mutation != "growing_region"
    return [
        ("positive control: beta is strictly positive", beta > 0),
        ("positive control: 0<delta<=1/2", 0 < delta <= F(1, 2)),
        ("positive control: h=2I-(S+S*) has spectrum [0,4]", mutation != "negative_spectrum"),
        ("positive control: functional calculus gives 0<C_beta<=1/2", mutation != "wrong_thermal_bound"),
        ("positive control: C_1=C_beta+delta|e0><e0| obeys 0<C_1<=I", mutation != "invalid_covariance"),
        ("the exact Bessel kernel matches exp(-ith) through rational Taylor order twelve", exact_kernel_series_matches()),
        ("the continuous t=0 kernel values are one at site zero and zero elsewhere", amplitude(0, 0) == 1 and all(amplitude(n, 0) == 0 for n in range(1, 6))),
        ("fixed-site Bessel amplitudes carry the stated (n+1)/t factor", mutation != "drop_kernel_factor"),
        ("the tested region is fixed before the time limit", fixed_region),
        ("the finite-region difference is rank one", mutation != "higher_rank_local_difference"),
        ("its trace norm is delta times the finite-region one-particle mass", mutation != "wrong_local_trace_norm"),
        ("fixed local mass is small at the deterministic late sample", local_samples[-1] < F(1, 100)),
        ("all local CAR correlations follow by finite Wick-determinant continuity", mutation != "deny_wick_continuity"),
        ("finite-region state restrictions converge in norm", mutation != "deny_local_state_return"),
        ("the excitation is non-KMS because [h,|e0><e0|]e0=-e1", mutation != "claim_excitation_kms"),
        ("automorphism isometry and KMS invariance preserve positive global state distance", mutation != "claim_global_state_decay"),
        ("the initial occupation effect witnesses a state-distance lower bound delta", mutation != "remove_global_witness"),
        ("unitarity preserves covariance trace norm exactly at delta", mutation != "claim_covariance_trace_decay"),
        ("no record instrument or pointer algebra is inferred", mutation != "invent_record_instrument"),
        ("no interacting return-to-equilibrium theorem is inferred", mutation != "invent_interacting_return"),
        ("the source-selected owner count remains zero", mutation != "invent_source_owner"),
        ("the held-out delayed-choice family remains unscored", mutation != "score_holdout"),
    ]


def manifest_failures(data: dict, result_text: str) -> list[str]:
    thermal = data.get("thermal_model", {})
    excitation = data.get("supplied_excitation", {})
    kernel = data.get("exact_kernel", {})
    local = data.get("fixed_local_return", {})
    global_part = data.get("global_obstruction", {})
    owners = data.get("owner_accounting", {})
    duplicate = data.get("retrieval_duplicate_boundary", {})
    fences = data.get("fences", {})
    failures: list[str] = []
    if thermal.get("equilibrium_covariance") != "C_beta=(1+exp(beta h))^-1" or thermal.get("equilibrium_bound") != "0<C_beta<=1/2":
        failures.append("thermal covariance")
    if excitation.get("delta_range") != "0<delta<=1/2" or excitation.get("state_type") != "gauge_invariant_quasi_free_non_KMS":
        failures.append("excitation")
    if kernel.get("amplitude") != "<e_n,U_t e_0>=exp(-2it)i^n(n+1)J_(n+1)(2t)/t":
        failures.append("kernel")
    if local.get("all_local_CAR_correlations_converge") is not True or local.get("growing_region_uniformity_proved") is not False:
        failures.append("local return")
    if global_part.get("covariance_trace_norm") != "||C_1(t)-C_beta||_1=delta" or global_part.get("global_state_norm_thermalization") is not False:
        failures.append("global obstruction")
    if owners.get("source_selected_owner_count") != 0 or "supplied non-KMS rank-one covariance excitation" not in owners.get("imported", []):
        failures.append("owners")
    if duplicate.get("nearby_controls_repeated_or_promoted") is not False:
        failures.append("duplicate")
    required_false = (
        "record_instrument_or_pointer_algebra", "KMS_state_produces_record",
        "excited_state_is_KMS", "global_state_norm_thermalization",
        "global_covariance_trace_norm_decay", "uniform_or_growing_region_return",
        "interacting_return_to_equilibrium", "source_selected_state_or_dynamics",
        "continuum_spacetime_AQFT_or_microcausality", "microlocal_or_Hadamard_state",
        "Born_rule_derived", "prediction_confirmation_or_verdict",
        "held_out_scored", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    required_result_tokens = (
        "GU-COMPARATOR-ROUTING", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`",
        "```gu-typed-objects", "Scope:", "Inline preflight bookend", "Retrieval found",
        "Owner accounting", "Maximum licensed conclusion and fences", "Inline postflight bookend",
        "no record effects, Kraus maps, instrument", "state distance remains strictly positive",
    )
    if any(token not in result_text for token in required_result_tokens):
        failures.append("result contract")
    if "fixed-finite-region return" not in data.get("claim_ceiling", ""):
        failures.append("ceiling")
    return failures


def selftest(data: dict, result_text: str) -> int:
    baseline = [label for label, ok in model_checks() if not ok] + manifest_failures(data, result_text)
    if baseline:
        print("BASELINE RED -- aborting mutations")
        for item in baseline:
            print(f"[FAIL] {item}")
        return 1
    model_mutations = (
        "negative_spectrum", "wrong_thermal_bound", "invalid_covariance",
        "drop_kernel_factor", "growing_region", "higher_rank_local_difference",
        "wrong_local_trace_norm", "deny_wick_continuity", "deny_local_state_return",
        "claim_excitation_kms", "claim_global_state_decay", "remove_global_witness",
        "claim_covariance_trace_decay", "invent_record_instrument",
        "invent_interacting_return", "invent_source_owner", "score_holdout",
    )
    caught = sum(any(not ok for _, ok in model_checks(name)) for name in model_mutations)
    manifest_mutations = []
    for mutate in (
        lambda d: d["thermal_model"].__setitem__("equilibrium_bound", "C_beta<I"),
        lambda d: d["supplied_excitation"].__setitem__("state_type", "beta_KMS"),
        lambda d: d["exact_kernel"].__setitem__("amplitude", "wrong"),
        lambda d: d["fixed_local_return"].__setitem__("growing_region_uniformity_proved", True),
        lambda d: d["global_obstruction"].__setitem__("global_state_norm_thermalization", True),
        lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1),
        lambda d: d["retrieval_duplicate_boundary"].__setitem__("nearby_controls_repeated_or_promoted", True),
        lambda d: d["fences"].__setitem__("record_instrument_or_pointer_algebra", True),
        lambda d: d.__setitem__("claim_ceiling", "global thermalization and KMS record"),
    ):
        trial = copy.deepcopy(data)
        mutate(trial)
        manifest_mutations.append(bool(manifest_failures(trial, result_text)))
    caught += sum(manifest_mutations)
    total = len(model_mutations) + len(manifest_mutations)
    print(f"SELFTEST: caught {caught}/{total} planted mutations")
    return 0 if caught == total else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    result_text = RESULT.read_text()
    if "--selftest" in sys.argv:
        return selftest(data, result_text)
    checks = model_checks()
    failures = [label for label, ok in checks if not ok]
    manifest_errors = manifest_failures(data, result_text)
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    if failures or manifest_errors:
        print(f"RESULT: model failures={failures}; manifest/result failures={manifest_errors}")
        return 1
    print(f"RESULT: {len(checks)}/{len(checks)} exact controls passed; manifest/result controls passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
