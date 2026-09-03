#!/usr/bin/env python3
"""Exact K115 feed-forward detector and nonequilibrium controls (stdlib only)."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k115-k114-feed-forward-nonequilibrium-detector-wave.json"


def apply_complete_graph(values: list[Fraction], rate: Fraction) -> list[Fraction]:
    total = sum(values, Fraction(0))
    n = len(values)
    return [rate * (total - n * value) for value in values]


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    detector_size = 256
    epsilon = Fraction(1, 257)
    power = 16
    clock = Fraction(7, 11)
    base_rate = Fraction(2, 5)
    if mutation == "wrong_dimension":
        detector_size = 255
    elif mutation == "zero_epsilon":
        epsilon = Fraction(0)
    elif mutation == "zero_power":
        power = 0
    elif mutation == "zero_clock":
        clock = Fraction(0)
    elif mutation == "zero_base_rate":
        base_rate = Fraction(0)

    light = Fraction(1, 257)
    heavy = Fraction(2, 257)
    high = (epsilon + heavy) ** power
    low = (epsilon + light) ** power
    score_total = high + (detector_size - 1) * low
    event_correct = high / score_total if score_total else Fraction(0)
    event_wrong = low / score_total if score_total else Fraction(0)
    expected_correct = Fraction(3**16, 3**16 + 255 * 2**16)

    # Exact three-state reversible-base control.  The centered modes of the
    # complete graph have eigenvalue -3*base_rate, so the stationary detector
    # density is the resolvent-smoothed event kernel.
    n = 3
    control_high = Fraction(3, 4) ** 4
    control_low = Fraction(1, 2) ** 4
    control_total = control_high + 2 * control_low
    p_correct = control_high / control_total
    p_wrong = control_low / control_total
    attenuation = clock / (clock + n * base_rate) if clock + n * base_rate else Fraction(0)
    h_correct = Fraction(1, n) + attenuation * (p_correct - Fraction(1, n))
    h_wrong = Fraction(1, n) + attenuation * (p_wrong - Fraction(1, n))
    p = [[p_correct if r == i else p_wrong for i in range(n)] for r in range(n)]
    h = [[h_correct if r == i else h_wrong for i in range(n)] for r in range(n)]

    stationary_equations = []
    for r in range(n):
        ah = apply_complete_graph(h[r], base_rate)
        stationary_equations.extend(ah[i] + clock * (p[r][i] - h[r][i]) for i in range(n))

    mu = Fraction(1, n)
    base_marginals = [sum(mu * h[r][i] for r in range(n)) for i in range(n)]
    record_marginals = [sum(mu * h[r][i] for i in range(n)) for r in range(n)]

    # Generator autonomy for a nonconstant base observable.
    base_observable = [Fraction(2), Fraction(-1), Fraction(4)]
    a_base = apply_complete_graph(base_observable, base_rate)
    generator_on_base = []
    for i in range(n):
        for _r in range(n):
            refresh = clock * (sum(p[s][i] * base_observable[i] for s in range(n)) - base_observable[i])
            generator_on_base.append(a_base[i] + refresh)

    # Informative stationary currents: diffusion current and refresh current
    # separately do not vanish, although their divergences balance.
    base_current = mu * base_rate * (h[0][0] - h[0][1])
    refresh_current = mu * clock * (h[0][0] * p[1][0] - h[1][0] * p[0][0])

    # The sharp record indicator has bounded generator image and carré du champ.
    gamma_values = []
    image_values = []
    for i in range(n):
        for r in range(n):
            image_values.append(clock * (p[0][i] - int(r == 0)))
            gamma_values.append(clock * Fraction(1, 2) * ((1 - p[0][i]) if r == 0 else p[0][i]))

    # Exact L2 resolvent-lag inequality on the three-state control.
    lag = sum(mu * (h[0][i] - p[0][i]) ** 2 for i in range(n))
    ap = apply_complete_graph(p[0], base_rate)
    form_energy = -sum(mu * p[0][i] * ap[i] for i in range(n))

    return [
        ("the detector alphabet has 256 labels", detector_size == 256),
        ("the score floor is strictly positive", epsilon > 0),
        ("the readout kernel is informative", power >= 1 and event_correct > event_wrong),
        ("the refresh clock is finite and positive", clock > 0),
        ("the K113 base control is irreducible", base_rate > 0),
        ("event-time vacuum readout is exact", event_correct == expected_correct),
        ("finite score contrast leaves nonzero error", event_correct < 1 and (detector_size - 1) * event_wrong == 1 - event_correct),
        ("the readout improves over the uniform prior", event_correct > Fraction(1, 256)),
        ("the readout kernel normalizes pointwise", all(sum(p[r][i] for r in range(n)) == 1 for i in range(n))),
        ("the stationary resolvent equation is exact", stationary_equations == [0] * (n * n)),
        ("the stationary conditional densities normalize", all(sum(h[r][i] for r in range(n)) == 1 for i in range(n))),
        ("the K113 base marginal is unchanged", base_marginals == [mu] * n),
        ("the detector marginal is uniform", record_marginals == [Fraction(1, n)] * n),
        ("the stationary detector remains informative", h_correct > h_wrong),
        ("finite clock rate smooths the event kernel", Fraction(0) < attenuation < 1 and p_correct > h_correct > Fraction(1, n)),
        ("base observables evolve with the base generator only", generator_on_base == [a_base[i] for i in range(n) for _r in range(n)]),
        ("informative feed-forward stationarity carries base current", base_current != 0),
        ("informative feed-forward stationarity carries refresh current", refresh_current != 0),
        ("the sharp record generator image is bounded", all(abs(value) <= clock for value in image_values)),
        ("the sharp record carré du champ is finite", all(Fraction(0) <= value <= clock / 2 for value in gamma_values)),
        ("the resolvent lag obeys the form-energy bound", lag <= form_energy / clock if clock else False),
        ("the stationary lag is strictly positive at finite rate", lag > 0),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    carrier = data.get("feed_forward_carrier", {})
    generator = data.get("generator", {})
    stationary = data.get("stationary_resolvent", {})
    record = data.get("finite_energy_record", {})
    noneq = data.get("nonequilibrium_boundary", {})
    readout = data.get("readout_and_lag", {})
    branch = data.get("branch_interface", {})
    result = data.get("result", {})
    if carrier.get("S_256_equivariant") is not True or carrier.get("source_or_GU_owned") is not False:
        failures.append("carrier")
    if generator.get("base_path_law_depends_on_detector") is not False or generator.get("record_changes_only_at_refresh_events") is not True or generator.get("absorbing_or_permanent_record") is not False or generator.get("physical_bath_clock_detector_or_preparation_derived") is not False:
        failures.append("generator")
    if stationary.get("base_marginal") != "mu_exactly" or stationary.get("normalization") != "sum_r_h_r=1" or stationary.get("detector_marginal") != "uniform_1/256" or stationary.get("uniqueness_under_K113_irreducibility_and_positive_refresh") is not True:
        failures.append("stationary")
    if record.get("continuous_gradient") != 0 or record.get("finite_joint_energy") is not True or record.get("tie_wall_crossing_forces_record_change") is not False:
        failures.append("record")
    if noneq.get("joint_reversibility_with_feed_forward_base_and_refresh_kernel") is not False or noneq.get("stationary_probability_currents_nonzero_for_informative_kernel") is not True or noneq.get("K114_record_conditioned_drift_backreaction_avoided") is not True or noneq.get("thermodynamic_dissipation_or_physical_entropy_production_derived") is not False:
        failures.append("nonequilibrium")
    if readout.get("finite_contrast_error_strictly_positive") is not True or readout.get("stationary_record_density_is_resolvent_smoothed") is not True or readout.get("clock_changes_response_lag_not_event_kernel") is not True or readout.get("Born_accuracy_or_information_optimality_derived") is not False:
        failures.append("readout")
    if branch.get("refresh_record_r_names_K110_K91_retract") is not True or branch.get("continuous_tie_crossing_changes_named_retract_without_refresh") is not False or branch.get("one_fixed_branch_domain_invariant_forever") is not False or branch.get("spacetime_causal_BV_BFV_observable_descent_owned") is not False:
        failures.append("branch")
    required_true = (
        "exact_feed_forward_nonequilibrium_detector_constructed",
        "K113_base_marginal_and_path_generator_preserved",
        "finite_energy_discrete_record_constructed",
        "reversible_record_conditioned_backreaction_avoided",
        "stationary_resolvent_and_lag_boundary_constructed",
    )
    required_false = (
        "source_action_or_physical_environment_derived",
        "actual_spacetime_causality_or_BV_BFV_descent_constructed",
        "Born_rule_derived",
        "prediction_or_confirmation_credit",
        "held_out_scored",
    )
    if any(result.get(key) is not True for key in required_true) or any(result.get(key) is not False for key in required_false) or result.get("canon_verdict_change") != "none":
        failures.append("result")
    ceiling = data.get("claim_ceiling", "")
    if "autonomous-base" not in ceiling or "stationary lag" not in ceiling or "No source/GU physical environment" not in ceiling:
        failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [
        (name, any(not ok for _, ok in exact_checks(name)))
        for name in ("wrong_dimension", "zero_epsilon", "zero_power", "zero_clock", "zero_base_rate")
    ]
    updates = (
        ("invent_source_owner", lambda d: d["feed_forward_carrier"].__setitem__("source_or_GU_owned", True)),
        ("break_equivariance", lambda d: d["feed_forward_carrier"].__setitem__("S_256_equivariant", False)),
        ("add_backreaction", lambda d: d["generator"].__setitem__("base_path_law_depends_on_detector", True)),
        ("force_continuous_record", lambda d: d["generator"].__setitem__("record_changes_only_at_refresh_events", False)),
        ("claim_absorption", lambda d: d["generator"].__setitem__("absorbing_or_permanent_record", True)),
        ("invent_physical_detector", lambda d: d["generator"].__setitem__("physical_bath_clock_detector_or_preparation_derived", True)),
        ("change_base_marginal", lambda d: d["stationary_resolvent"].__setitem__("base_marginal", "reweighted")),
        ("break_normalization", lambda d: d["stationary_resolvent"].__setitem__("normalization", "unknown")),
        ("bias_detector_marginal", lambda d: d["stationary_resolvent"].__setitem__("detector_marginal", "biased")),
        ("erase_uniqueness", lambda d: d["stationary_resolvent"].__setitem__("uniqueness_under_K113_irreducibility_and_positive_refresh", False)),
        ("erase_finite_energy", lambda d: d["finite_energy_record"].__setitem__("finite_joint_energy", False)),
        ("force_wall_refresh", lambda d: d["finite_energy_record"].__setitem__("tie_wall_crossing_forces_record_change", True)),
        ("claim_reversibility", lambda d: d["nonequilibrium_boundary"].__setitem__("joint_reversibility_with_feed_forward_base_and_refresh_kernel", True)),
        ("erase_currents", lambda d: d["nonequilibrium_boundary"].__setitem__("stationary_probability_currents_nonzero_for_informative_kernel", False)),
        ("erase_escape", lambda d: d["nonequilibrium_boundary"].__setitem__("K114_record_conditioned_drift_backreaction_avoided", False)),
        ("invent_thermodynamics", lambda d: d["nonequilibrium_boundary"].__setitem__("thermodynamic_dissipation_or_physical_entropy_production_derived", True)),
        ("claim_zero_error", lambda d: d["readout_and_lag"].__setitem__("finite_contrast_error_strictly_positive", False)),
        ("erase_lag", lambda d: d["readout_and_lag"].__setitem__("stationary_record_density_is_resolvent_smoothed", False)),
        ("make_clock_change_kernel", lambda d: d["readout_and_lag"].__setitem__("clock_changes_response_lag_not_event_kernel", False)),
        ("invent_Born_accuracy", lambda d: d["readout_and_lag"].__setitem__("Born_accuracy_or_information_optimality_derived", True)),
        ("force_tie_retract_change", lambda d: d["branch_interface"].__setitem__("continuous_tie_crossing_changes_named_retract_without_refresh", True)),
        ("preserve_branch_forever", lambda d: d["branch_interface"].__setitem__("one_fixed_branch_domain_invariant_forever", True)),
        ("invent_BV_BFV", lambda d: d["branch_interface"].__setitem__("spacetime_causal_BV_BFV_observable_descent_owned", True)),
        ("invent_environment", lambda d: d["result"].__setitem__("source_action_or_physical_environment_derived", True)),
        ("invent_Born", lambda d: d["result"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["result"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["result"].__setitem__("canon_verdict_change", "changed")),
        ("erase_scope", lambda d: d.__setitem__("claim_ceiling", "GU derives a physical detector.")),
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
    checks.append(("manifest preserves autonomy, resolvent, nonequilibrium, lag and ownership ceilings", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K115 FEED-FORWARD NONEQUILIBRIUM DETECTOR: {sum(int(bool(ok)) for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
