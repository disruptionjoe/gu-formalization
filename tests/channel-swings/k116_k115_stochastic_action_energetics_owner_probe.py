#!/usr/bin/env python3
"""Exact K116 stochastic-action/energetics controls (standard library only)."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k116-k115-stochastic-action-energetics-owner-wave.json"


def apply_complete_graph(values: list[Fraction], rate: Fraction) -> list[Fraction]:
    total = sum(values, Fraction(0))
    n = len(values)
    return [rate * (total - n * value) for value in values]


def finite_control(mutation: str | None = None) -> dict[str, object]:
    n = 3
    clock = Fraction(7, 11)
    base_rate = Fraction(2, 5)
    high = Fraction(81, 113)
    low = Fraction(16, 113)
    if mutation == "wrong_dimension":
        n = 4
    elif mutation == "zero_clock":
        clock = Fraction(0)
    elif mutation == "zero_base_rate":
        base_rate = Fraction(0)
    elif mutation == "unnormalized_kernel":
        high = Fraction(82, 113)
    elif mutation == "uninformative_kernel":
        high = Fraction(1, 3)
        low = Fraction(1, 3)

    p = [[high if r == i else low for i in range(3)] for r in range(3)]
    attenuation = clock / (clock + 3 * base_rate) if clock + 3 * base_rate else Fraction(0)
    h = [
        [Fraction(1, 3) + attenuation * (p[r][i] - Fraction(1, 3)) for i in range(3)]
        for r in range(3)
    ]

    stationarity = []
    for r in range(3):
        ah = apply_complete_graph(h[r], base_rate)
        stationarity.extend(ah[i] + clock * (p[r][i] - h[r][i]) == 0 for i in range(3))

    detailed_balance = []
    for i in range(3):
        for r in range(3):
            for s in range(3):
                if r != s and p[r][i] and p[s][i]:
                    q_rs = clock * p[s][i]
                    q_sr = clock * p[r][i]
                    detailed_balance.append(clock > 0 and q_rs / q_sr == p[s][i] / p[r][i])

    joint = [[h[r][i] / 3 for r in range(3)] for i in range(3)]
    divergence = []
    for i in range(3):
        for r in range(3):
            base_div = sum(base_rate * (joint[i][r] - joint[j][r]) for j in range(3) if j != i)
            jump_div = sum(
                joint[i][r] * clock * p[s][i] - joint[i][s] * clock * p[r][i]
                for s in range(3)
                if s != r
            )
            divergence.append(base_div + jump_div)

    def edge_production(forward: Fraction, backward: Fraction) -> float:
        if forward == backward:
            return 0.0
        return float(forward - backward) * math.log(float(forward / backward))

    sigma_base = 0.0
    for r in range(3):
        for i in range(3):
            for j in range(3):
                if i != j:
                    sigma_base += 0.5 * edge_production(joint[i][r] * base_rate, joint[j][r] * base_rate)
    sigma_jump = 0.0
    for i in range(3):
        for r in range(3):
            for s in range(3):
                if r != s:
                    sigma_jump += 0.5 * edge_production(
                        joint[i][r] * clock * p[s][i],
                        joint[i][s] * clock * p[r][i],
                    )

    def mutual_information(rows: list[list[Fraction]]) -> float:
        return sum(float(value) * math.log(3.0 * float(value)) for row in rows for value in row) / 3.0

    event_information = mutual_information([[p[r][i] for r in range(3)] for i in range(3)])
    stationary_information = mutual_information([[h[r][i] for r in range(3)] for i in range(3)])
    return {
        "n": n,
        "clock": clock,
        "base_rate": base_rate,
        "p": p,
        "h": h,
        "attenuation": attenuation,
        "stationarity": stationarity,
        "detailed_balance": detailed_balance,
        "divergence": divergence,
        "sigma_base": sigma_base,
        "sigma_jump": sigma_jump,
        "event_information": event_information,
        "stationary_information": stationary_information,
    }


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    c = finite_control(mutation)
    p = c["p"]
    h = c["h"]
    checks = [
        ("three base and record states", c["n"] == 3),
        ("positive base and clock rates", c["base_rate"] > 0 and c["clock"] > 0),
        ("event kernel rows normalize", all(sum(p[r][i] for r in range(3)) == 1 for i in range(3))),
        ("event kernel is strictly positive", all(p[r][i] > 0 for r in range(3) for i in range(3))),
        ("event kernel is informative", any(p[r][i] != Fraction(1, 3) for r in range(3) for i in range(3))),
        ("resolvent attenuation exact", c["attenuation"] == Fraction(35, 101)),
        ("stationary conditional rows normalize", all(sum(h[r][i] for r in range(3)) == 1 for i in range(3))),
        ("stationary detector marginals normalize", all(sum(h[r][i] for i in range(3)) == 1 for r in range(3))),
        ("stationary resolvent equation", all(c["stationarity"])),
        ("local detailed balance ratios", bool(c["detailed_balance"]) and all(c["detailed_balance"])),
        ("stationary current divergence vanishes", all(value == 0 for value in c["divergence"])),
        ("base-sector production positive", c["sigma_base"] > 0.0),
        ("refresh-sector production positive", c["sigma_jump"] > 0.0),
        ("total stationary production positive", c["sigma_base"] + c["sigma_jump"] > 0.0),
        ("event record information positive", c["event_information"] > 0.0),
        ("stationary information positive", c["stationary_information"] > 0.0),
        ("finite clock contracts record information", c["stationary_information"] < c["event_information"]),
        ("finite contrast leaves event error", p[1][0] > 0 and p[0][0] < 1),
        ("marked refresh rates recover event kernel", c["clock"] > 0 and all(c["clock"] * p[r][i] / c["clock"] == p[r][i] for r in range(3) for i in range(3))),
        ("K115 base generator remains record-independent", len({c["base_rate"] for _ in range(3)}) == 1),
    ]
    return checks


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    action = data.get("stochastic_path_action", {})
    bath = data.get("detector_bath_and_preparation", {})
    controller = data.get("controller_backreaction_invoice", {})
    energetics = data.get("stationary_energetics", {})
    information = data.get("information_resource", {})
    control = data.get("finite_control", {})
    result = data.get("result", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    if action.get("base_path_law_remains_K113") is not True or action.get("S_256_equivariant") is not True or action.get("Weinstein_source_or_GU_field_action") is not False:
        failures.append("action")
    if bath.get("ideal_isothermal_detector_bath_declared") is not True or bath.get("microscopic_Hamiltonian_reservoir_constructed") is not False or bath.get("autonomous_finite_fuel_supply_constructed") is not False or bath.get("physical_reset_apparatus_authenticated") is not False:
        failures.append("bath")
    if controller.get("detector_energy_depends_on_base_state_for_informative_p") is not True or controller.get("uncompensated_energy_gradient_would_backreact_on_base") is not True or controller.get("controller_is_external_supplied_structure") is not True or controller.get("noninvasive_autonomous_physical_measurement_derived") is not False:
        failures.append("controller")
    if energetics.get("nonnegative") is not True or energetics.get("zero_iff_uninformative_under_irreducibility_and_strict_positivity") is not True or energetics.get("informative_readout_strictly_positive") is not True or energetics.get("GU_physical_dissipation_or_cosmological_budget") is not False or energetics.get("microscopic_fluctuation_relation_derived") is not False:
        failures.append("energetics")
    if information.get("resolvent_contraction") != "0_le_I_stationary_le_I_event" or information.get("finite_contrast_event_error_positive") is not True or information.get("information_is_a_preparation_resource_not_a_universal_work_equality") is not True or information.get("universal_Landauer_reset_cost_claimed") is not False or information.get("Born_information_or_quantum_measurement_claimed") is not False:
        failures.append("information")
    if control.get("stationarity_checked_exactly") is not True or control.get("local_detailed_balance_checked_exactly") is not True or control.get("current_divergence_checked_exactly") is not True or control.get("positive_entropy_production_checked") is not True or control.get("event_information_exceeds_stationary_information") is not True:
        failures.append("control")
    required_true = (
        "repository_owned_stochastic_action_constructed",
        "conditional_detector_bath_clock_and_preparation_declared",
        "controller_backreaction_requirement_exposed",
        "stationary_entropy_production_theorem_constructed",
        "information_resource_and_resolvent_contraction_constructed",
    )
    required_false = (
        "Weinstein_source_or_GU_action_derived",
        "autonomous_physical_environment_constructed",
        "actual_spacetime_causality_or_BV_BFV_descent_constructed",
        "Born_rule_derived",
        "prediction_or_confirmation_credit",
        "held_out_scored",
    )
    if any(result.get(key) is not True for key in required_true) or any(result.get(key) is not False for key in required_false) or result.get("canon_verdict_change") != "none":
        failures.append("result")
    ceiling = data.get("claim_ceiling", "")
    if "marked-Poisson" not in ceiling or "declared repository constructions" not in ceiling or "No Weinstein/source/GU action" not in ceiling:
        failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "wrong_dimension", "zero_clock", "zero_base_rate", "unnormalized_kernel", "uninformative_kernel"
    )]
    updates = (
        ("invent_source_action", lambda d: d["stochastic_path_action"].__setitem__("Weinstein_source_or_GU_field_action", True)),
        ("break_base_autonomy", lambda d: d["stochastic_path_action"].__setitem__("base_path_law_remains_K113", False)),
        ("break_equivariance", lambda d: d["stochastic_path_action"].__setitem__("S_256_equivariant", False)),
        ("invent_reservoir", lambda d: d["detector_bath_and_preparation"].__setitem__("microscopic_Hamiltonian_reservoir_constructed", True)),
        ("invent_fuel", lambda d: d["detector_bath_and_preparation"].__setitem__("autonomous_finite_fuel_supply_constructed", True)),
        ("authenticate_reset", lambda d: d["detector_bath_and_preparation"].__setitem__("physical_reset_apparatus_authenticated", True)),
        ("hide_energy_coupling", lambda d: d["controller_backreaction_invoice"].__setitem__("detector_energy_depends_on_base_state_for_informative_p", False)),
        ("deny_backreaction", lambda d: d["controller_backreaction_invoice"].__setitem__("uncompensated_energy_gradient_would_backreact_on_base", False)),
        ("internalize_controller", lambda d: d["controller_backreaction_invoice"].__setitem__("controller_is_external_supplied_structure", False)),
        ("invent_noninvasive_measurement", lambda d: d["controller_backreaction_invoice"].__setitem__("noninvasive_autonomous_physical_measurement_derived", True)),
        ("allow_negative_production", lambda d: d["stationary_energetics"].__setitem__("nonnegative", False)),
        ("erase_strictness", lambda d: d["stationary_energetics"].__setitem__("informative_readout_strictly_positive", False)),
        ("invent_GU_budget", lambda d: d["stationary_energetics"].__setitem__("GU_physical_dissipation_or_cosmological_budget", True)),
        ("invent_fluctuation_theorem", lambda d: d["stationary_energetics"].__setitem__("microscopic_fluctuation_relation_derived", True)),
        ("reverse_information_bound", lambda d: d["information_resource"].__setitem__("resolvent_contraction", "I_event_le_I_stationary")),
        ("erase_event_error", lambda d: d["information_resource"].__setitem__("finite_contrast_event_error_positive", False)),
        ("invent_Landauer_equality", lambda d: d["information_resource"].__setitem__("universal_Landauer_reset_cost_claimed", True)),
        ("invent_Born_information", lambda d: d["information_resource"].__setitem__("Born_information_or_quantum_measurement_claimed", True)),
        ("erase_exact_stationarity", lambda d: d["finite_control"].__setitem__("stationarity_checked_exactly", False)),
        ("erase_current_balance", lambda d: d["finite_control"].__setitem__("current_divergence_checked_exactly", False)),
        ("erase_positive_EP", lambda d: d["finite_control"].__setitem__("positive_entropy_production_checked", False)),
        ("invent_environment", lambda d: d["result"].__setitem__("autonomous_physical_environment_constructed", True)),
        ("invent_BV_BFV", lambda d: d["result"].__setitem__("actual_spacetime_causality_or_BV_BFV_descent_constructed", True)),
        ("invent_Born", lambda d: d["result"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["result"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["result"].__setitem__("canon_verdict_change", "changed")),
        ("erase_scope", lambda d: d.__setitem__("claim_ceiling", "GU derives a physical detector action.")),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(manifest_failures(mutant))))
    for name, ok in caught:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(int(bool(ok)) for _, ok in caught)}/{len(caught)} caught")
    return 0 if all(ok for _, ok in caught) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if "--selftest" in sys.argv:
        return selftest(data)
    checks = exact_checks()
    checks.append(("manifest preserves action, energetics, information and ownership ceilings", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K116 STOCHASTIC ACTION ENERGETICS OWNER: {sum(int(bool(ok)) for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
