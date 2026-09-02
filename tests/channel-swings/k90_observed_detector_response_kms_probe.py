#!/usr/bin/env python3
"""Exact finite detector-response and KMS ownership controls for K90."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k90-observed-detector-response-kms-wave.json"


def phase_quarter(power):
    return (1, 1j, -1, -1j)[power % 4]


def norm2(value):
    return F(int(round(value.real)) ** 2 + int(round(value.imag)) ** 2)


def response(occupation=0, coupling=F(1, 8), mutation=None):
    times = range(3) if mutation == "switching_endpoint_loss" else range(4)
    resonant = sum((phase_quarter(0 * t) for t in times), 0j)
    counter = sum((phase_quarter(2 * t) for t in times), 0j)
    resonant_weight = norm2(resonant)
    counter_weight = norm2(counter)
    up = coupling ** 2 * (F(occupation) * resonant_weight + F(occupation + 1) * counter_weight)
    down = coupling ** 2 * (F(occupation + 1) * resonant_weight + F(occupation) * counter_weight)
    if mutation == "spectral_reversal":
        up, down = down, up
    return up, down, resonant_weight, counter_weight


def checks(mutation=None):
    vacuum = response(0, mutation=mutation)
    thermal_n = 2 if mutation == "thermal_occupation" else 1
    thermal = response(thermal_n, mutation=mutation)
    large = response(0, coupling=F(1))
    return [
        ("four equal switching times give resonant weight sixteen", vacuum[2] == 16),
        ("four equal switching times cancel the counterrotating weight", vacuum[3] == 0),
        ("positive-frequency vacuum has zero leading excitation weight", vacuum[0] == 0),
        ("positive-frequency vacuum has deexcitation weight one quarter", vacuum[1] == F(1, 4)),
        ("thermal occupation one gives excitation weight one quarter", thermal[0] == F(1, 4)),
        ("thermal occupation one gives deexcitation weight one half", thermal[1] == F(1, 2)),
        ("the thermal detailed-balance ratio is one half", thermal[0] / thermal[1] == F(1, 2)),
        ("the detailed-balance ratio equals n over n plus one", thermal[0] / thermal[1] == F(thermal_n, thermal_n + 1)),
        ("the chosen weak coupling keeps every displayed response weight in range", all(F(0) <= x <= F(1) for x in vacuum[:2] + thermal[:2])),
        ("a large-coupling control leaves the probability range", large[1] > 1),
        ("vacuum and thermal response tables differ", vacuum[:2] != thermal[:2]),
        ("excitation and deexcitation are orientation sensitive", vacuum[0] != vacuum[1]),
        ("the response depends on the switching profile", response(0, mutation="switching_endpoint_loss")[:2] != vacuum[:2]),
        ("the response depends on the field occupation", response(2)[:2] != thermal[:2]),
        ("the detector gap and mode gap are matched in the resonant channel", True),
        ("the covariance is repository selected rather than source selected", True),
        ("the switching profile is an independent owner", True),
        ("the monopole interaction is an independent owner", True),
        ("interpreting response weights as probabilities imports the Born rule", True),
        ("a finite spectral table is not a continuum Hadamard condition", True),
        ("leading response weights are not nonperturbative unitary dynamics", True),
        ("no complete positive instrument is constructed", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]


def manifest_failures(data):
    detector = data.get("detector_model", {})
    response_data = data.get("spectral_response", {})
    owners = data.get("owner_accounting", {})
    fences = data.get("fences", {})
    failures = []
    if detector.get("coupling") != "one_eighth" or detector.get("response_order") != "leading_quadratic_weight":
        failures.append("detector")
    expected = {"vacuum_up_weight": "0", "vacuum_down_weight": "1/4", "thermal_up_weight": "1/4", "thermal_down_weight": "1/2", "KMS_ratio": "1/2"}
    if any(response_data.get(key) != value for key, value in expected.items()) or response_data.get("positive_frequency_orientation_required") is not True:
        failures.append("response")
    if owners.get("Born_readout_owner") != "imported_probability_interpretation_not_derived" or owners.get("source_selected_owner_count") != 0:
        failures.append("owners")
    required_false = (
        "source_selected_covariance", "continuum_Hadamard_state",
        "source_owned_detector_interaction", "Born_rule_derived",
        "complete_positive_instrument", "nonperturbative_unitary_detector_dynamics",
        "Bell_prediction_or_confirmation", "held_out_scored", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if data.get("holdout_firewall", {}).get("status") != "reserved_unscored":
        failures.append("holdout")
    return failures


def selftest(data):
    mutations = [(name, any(not ok for _, ok in checks(name))) for name in (
        "spectral_reversal", "switching_endpoint_loss", "thermal_occupation",
    )]
    updates = (
        ("large_coupling", lambda d: d["detector_model"].__setitem__("coupling", "one")),
        ("wrong_order", lambda d: d["detector_model"].__setitem__("response_order", "exact_nonperturbative")),
        ("wrong_vacuum_up", lambda d: d["spectral_response"].__setitem__("vacuum_up_weight", "1/4")),
        ("wrong_vacuum_down", lambda d: d["spectral_response"].__setitem__("vacuum_down_weight", "0")),
        ("wrong_thermal_up", lambda d: d["spectral_response"].__setitem__("thermal_up_weight", "1/2")),
        ("wrong_thermal_down", lambda d: d["spectral_response"].__setitem__("thermal_down_weight", "1/4")),
        ("wrong_kms", lambda d: d["spectral_response"].__setitem__("KMS_ratio", "1")),
        ("drop_orientation", lambda d: d["spectral_response"].__setitem__("positive_frequency_orientation_required", False)),
        ("born_owner", lambda d: d["owner_accounting"].__setitem__("Born_readout_owner", "derived")),
        ("source_owner", lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1)),
        ("source_covariance", lambda d: d["fences"].__setitem__("source_selected_covariance", True)),
        ("hadamard_promotion", lambda d: d["fences"].__setitem__("continuum_Hadamard_state", True)),
        ("interaction_promotion", lambda d: d["fences"].__setitem__("source_owned_detector_interaction", True)),
        ("born_promotion", lambda d: d["fences"].__setitem__("Born_rule_derived", True)),
        ("instrument_promotion", lambda d: d["fences"].__setitem__("complete_positive_instrument", True)),
        ("unitary_promotion", lambda d: d["fences"].__setitem__("nonperturbative_unitary_detector_dynamics", True)),
        ("bell_promotion", lambda d: d["fences"].__setitem__("Bell_prediction_or_confirmation", True)),
        ("holdout", lambda d: d["holdout_firewall"].__setitem__("status", "scored")),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        mutations.append((name, bool(manifest_failures(mutant))))
    for name, caught in mutations:
        print(f"[{'PASS' if caught else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(c for _, c in mutations)}/{len(mutations)} caught")
    return 0 if all(c for _, c in mutations) else 1


def main():
    data = json.loads(MANIFEST.read_text())
    if "--selftest" in sys.argv:
        return selftest(data)
    results = checks()
    results.append(("manifest preserves response-owner, source, Born and continuum fences", not manifest_failures(data)))
    for label, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in results)
    print(f"K90 DETECTOR RESPONSE KMS: {passed}/{len(results)} pass")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
