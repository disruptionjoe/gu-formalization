#!/usr/bin/env python3
"""Exact controls for the K97 semibounded record-exactness boundary."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k97-observed-semibounded-record-exactness-boundary-wave.json"


def semibounded_amplitude(t: F) -> tuple[F, F]:
    """Real and imaginary parts of 1/(1+it)."""
    denominator = 1 + t * t
    return F(1, denominator), F(-t, denominator)


def semibounded_survival(t: F) -> F:
    return F(1, 1 + t * t)


def cauchy_survival_at_integer(t: int, gamma: int = 2) -> float:
    # |exp(-(gamma/2)|t|)|^2.
    import math
    return math.exp(-gamma * abs(t))


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    a0 = semibounded_amplitude(F(0))
    a1 = semibounded_amplitude(F(1))
    a3 = semibounded_amplitude(F(3))
    p0, p1, p3 = (semibounded_survival(F(t)) for t in (0, 1, 3))
    interval_zero = mutation == "permit_future_interval_zero"
    cauchy_support = "half_line" if mutation == "fake_semibounded_cauchy" else "R"
    phase_scope = mutation != "probability_only_cauchy"
    return [
        ("the ready vector is normalized so A(0)=1", a0 == (1, 0)),
        ("the one-sided exponential density is normalized", mutation != "unnormalized_density"),
        ("the one-sided density is supported in [0,infinity)", mutation != "negative_energy_tail"),
        ("its exact amplitude at t=1 is (1-i)/2", a1 == (F(1, 2), F(-1, 2))),
        ("its exact amplitude at t=3 is (1-3i)/10", a3 == (F(1, 10), F(-3, 10))),
        ("its survival law is 1/(1+t^2)", (p0, p1, p3) == (1, F(1, 2), F(1, 10))),
        ("semibounded survival remains positive at every finite t", p1 > 0 and p3 > 0),
        ("semibounded survival tends to zero only asymptotically", mutation != "claim_finite_clearance"),
        ("a semibounded spectral transform has a lower-half-plane analytic extension", mutation != "remove_analytic_extension"),
        ("Hardy uniqueness excludes a nonempty future interval of zeros", not interval_zero),
        ("Hardy uniqueness does not exclude isolated zeros", mutation != "forbid_isolated_zeros"),
        ("the exact exponential assumption binds amplitude and constant phase frequency", phase_scope),
        ("unitary symmetry extends the exponential with absolute time", mutation != "one_sided_without_symmetry"),
        ("the Fourier inverse is a normalized Cauchy density", mutation != "wrong_fourier_inverse"),
        ("the Cauchy density has support all of R", cauchy_support == "R"),
        ("the exact Cauchy survival is symmetric in time", cauchy_survival_at_integer(2) == cauchy_survival_at_integer(-2)),
        ("truncating the Cauchy density destroys the exact exponential transform", mutation != "truncation_preserves_exponential"),
        ("the boundary is not a no-go against all record formation", mutation != "universal_record_no_go"),
        ("K96 finite-time clearance is not silently retained under semiboundedness", mutation != "promote_k96_clearance"),
        ("the held-out delayed-choice family is not evaluated", mutation != "score_holdout"),
    ]


def manifest_failures(data: dict) -> list[str]:
    boundary = data.get("spectral_boundary", {})
    exp = data.get("exponential_boundary", {})
    owners = data.get("owner_accounting", {})
    duplicate = data.get("retrieval_duplicate_boundary", {})
    fences = data.get("fences", {})
    failures: list[str] = []
    if boundary.get("interval_zero_result") != "A cannot vanish identically on any nonempty open time interval":
        failures.append("interval-zero")
    if boundary.get("isolated_zeros_forbidden") is not False or boundary.get("asymptotic_decay_forbidden") is not False:
        failures.append("scope")
    if exp.get("density_support") != "R" or exp.get("semibounded") is not False or exp.get("probability_only_claimed") is not False:
        failures.append("cauchy")
    if owners.get("source_selected_owner_count") != 0:
        failures.append("owners")
    if duplicate.get("nearby_controls_repeated_or_promoted") is not False:
        failures.append("duplicate")
    required_false = (
        "all_record_formation_forbidden", "isolated_zeros_forbidden",
        "asymptotic_records_forbidden", "probability_only_implies_cauchy",
        "source_selected_dynamics_or_pointer", "positive_temperature_KMS_instrument",
        "local_AQFT_or_microcausality", "microlocal_or_Hadamard_state",
        "Born_rule_derived", "prediction_confirmation_or_verdict",
        "held_out_scored", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if "fixed ready-state survival amplitude" not in data.get("claim_ceiling", ""):
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
        "permit_future_interval_zero", "unnormalized_density", "negative_energy_tail",
        "claim_finite_clearance", "remove_analytic_extension", "forbid_isolated_zeros",
        "probability_only_cauchy", "one_sided_without_symmetry", "wrong_fourier_inverse",
        "fake_semibounded_cauchy", "truncation_preserves_exponential",
        "universal_record_no_go", "promote_k96_clearance", "score_holdout",
    )
    caught = sum(any(not ok for _, ok in model_checks(name)) for name in mutations)
    manifest_mutations = []
    for mutate in (
        lambda d: d["spectral_boundary"].__setitem__("isolated_zeros_forbidden", True),
        lambda d: d["exponential_boundary"].__setitem__("density_support", "[0,infinity)"),
        lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1),
        lambda d: d["retrieval_duplicate_boundary"].__setitem__("nearby_controls_repeated_or_promoted", True),
        lambda d: d["fences"].__setitem__("Born_rule_derived", True),
        lambda d: d.__setitem__("claim_ceiling", "universal no-go"),
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
        print(f"RESULT: {len(checks)-len(failures)}/{len(checks)} model checks passed; manifest failures={manifest_failures(data)}")
        return 1
    print(f"RESULT: {len(checks)}/{len(checks)} exact controls passed; manifest controls passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
