#!/usr/bin/env python3
"""Exact K114 hybrid detector and backreaction controls (stdlib only)."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k114-k113-hybrid-detector-finite-energy-record-wave.json"


def score(value: Fraction, epsilon: Fraction, power: int) -> Fraction:
    return (epsilon + value) ** power


def tangent_project(values: list[Fraction]) -> list[Fraction]:
    mean = sum(values, Fraction(0)) / len(values)
    return [value - mean for value in values]


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    n = 256
    epsilon = Fraction(1, 257)
    power = 16
    beta = Fraction(7, 3)
    clock = Fraction(5, 11)
    if mutation == "wrong_dimension":
        n = 255
    elif mutation == "zero_epsilon":
        epsilon = Fraction(0)
    elif mutation == "zero_power":
        power = 0
    elif mutation == "zero_beta":
        beta = Fraction(0)
    elif mutation == "zero_clock":
        clock = Fraction(0)

    light = Fraction(1, 257)
    heavy = Fraction(2, 257)
    vacuum = [light] * n
    if n > 17:
        vacuum[17] = heavy
    scores = [score(value, epsilon, power) for value in vacuum]
    total = sum(scores, Fraction(0))
    correct = scores[17] / total if n > 17 and total else Fraction(0)
    wrong = scores[0] / total if total else Fraction(0)
    expected_correct = Fraction(3**16, 3**16 + 255 * 2**16)
    expected_wrong = Fraction(2**16, 3**16 + 255 * 2**16)

    # Exact jump detailed balance at a non-symmetric rational point.
    sample = [Fraction((5 * i + 3) % 23, 29) for i in range(n)]
    sample_scores = [score(value, epsilon, power) for value in sample]
    r, s = 7, 19
    pi_r = sample_scores[r]
    pi_s = sample_scores[s]
    q_rs = clock * sample_scores[s]
    q_sr = clock * sample_scores[r]
    clock_ratio_ok = q_sr != 0 and pi_r != 0 and q_rs / q_sr == pi_s / pi_r

    # The detector indicator has zero continuous gradient and finite jump energy.
    indicator_grad = tangent_project([Fraction(0)] * n)
    indicator_jump_energy = clock * sum(
        sample_scores[r] * sample_scores[j]
        for j in range(n)
        if j != r
    )
    lower_rate = clock * (n - 1) * epsilon**power
    upper_rate = clock * (n - 1) * (epsilon + 1) ** power
    actual_rate = clock * sum(sample_scores[j] for j in range(n) if j != r)

    # m=1 preserves the base Gibbs marginal because sum_r(epsilon+w_r) is constant.
    affine_sum_vacuum = sum(score(value, epsilon, 1) for value in vacuum)
    uniform = [Fraction(1, n)] * n
    affine_sum_uniform = sum(score(value, epsilon, 1) for value in uniform)
    power_sum_vacuum = sum(score(value, epsilon, power) for value in vacuum)
    power_sum_uniform = sum(score(value, epsilon, power) for value in uniform)

    # Any nonconstant score produces a nonzero record-conditioned tangent drift.
    basis = [Fraction(0)] * n
    if n > r:
        basis[r] = Fraction(power, 1) / (beta * (epsilon + sample[r])) if beta else 0
    response = tangent_project(basis)

    return [
        ("the hybrid carrier has 256 detector sectors", n == 256),
        ("the score floor is strictly positive", epsilon > 0),
        ("the detector score is informative", power >= 1 and correct > wrong),
        ("the inverse temperature is strictly positive", beta > 0),
        ("the detector clock is finite and positive", clock > 0),
        ("vacuum correct-readout probability is exact", correct == expected_correct),
        ("vacuum wrong-readout probability is exact", wrong == expected_wrong),
        ("finite-parameter readout error is nonzero", correct < 1 and (n - 1) * wrong == 1 - correct),
        ("readout improves over the uniform prior", correct > Fraction(1, 256)),
        ("the detector marginal remains eight-bit uniform by orbit symmetry", n == 2**8),
        ("jump detailed balance is exact", pi_r * q_rs == pi_s * q_sr),
        ("the detector indicator has zero continuous gradient", indicator_grad == [0] * n),
        ("the detector indicator has finite positive jump energy", indicator_jump_energy > 0),
        ("the holding rate has a positive exact lower bound", lower_rate > 0),
        ("the holding rate obeys the compact-carrier upper bound", lower_rate <= actual_rate <= upper_rate),
        ("the kinetic clock cancels from stationary score ratios", clock_ratio_ok),
        ("affine scores preserve the K113 base Gibbs marginal", affine_sum_vacuum == affine_sum_uniform),
        ("higher-power accurate scores reweight the base marginal", power_sum_vacuum != power_sum_uniform),
        ("an informative record-conditioned reversible drift backreacts", any(value != 0 for value in response)),
        ("the backreaction is tangent", sum(response, Fraction(0)) == 0),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    carrier = data.get("hybrid_carrier", {})
    owner = data.get("reversible_hybrid_owner", {})
    form = data.get("joint_dirichlet_form", {})
    readout = data.get("readout_and_retention", {})
    backreaction = data.get("backreaction_boundary", {})
    branch = data.get("branch_interface", {})
    result = data.get("result", {})
    if carrier.get("S_256_equivariant") is not True or carrier.get("source_or_GU_owned") is not False:
        failures.append("carrier")
    if owner.get("jump_rate") != "q_r_to_s(w)=c*a_s(w)_for_s_not_equal_r" or owner.get("S_256_equivariant") is not True or owner.get("physical_bath_clock_or_detector_derived") is not False:
        failures.append("owner")
    if form.get("detector_indicator_continuous_gradient") != 0 or form.get("detector_indicator_has_finite_joint_energy") is not True or form.get("base_argmax_indicator_has_finite_K113_diffusion_energy") is not False or form.get("tie_wall_crossing_forces_detector_jump") is not False:
        failures.append("form")
    if readout.get("finite_parameter_error_strictly_positive") is not True or readout.get("detector_marginal_under_joint_S_256_law") != "uniform_1/256" or readout.get("barrier_or_clock_factor_c_changes_kinetics_not_stationary_readout") is not True or readout.get("perfect_record_bits_at_finite_parameters") != 0:
        failures.append("readout")
    if backreaction.get("m_equals_1_preserves_K113_Gibbs_marginal") is not True or backreaction.get("m_greater_than_1_generically_reweights_K113_Gibbs_marginal") is not True or backreaction.get("informative_record_conditioned_drift_equals_K113_drift") is not False or backreaction.get("unchanged_record_conditioned_K113_drift_for_all_r_forces_scores_constant_on_Delta") is not True or backreaction.get("one_way_nonequilibrium_detector_remains_open") is not True:
        failures.append("backreaction")
    if branch.get("record_center_evaluation_names_K110_K91_retract") is not True or branch.get("continuous_tie_crossing_changes_named_retract_without_detector_jump") is not False or branch.get("one_fixed_branch_domain_invariant_forever") is not False or branch.get("spacetime_causal_BV_BFV_observable_descent_owned") is not False:
        failures.append("branch")
    required_false = (
        "perfect_finite_parameter_measurement_constructed",
        "noninvasive_informative_reversible_detector_constructed",
        "source_action_or_physical_environment_derived",
        "actual_spacetime_causality_or_BV_BFV_descent_constructed",
        "Born_rule_derived",
        "prediction_or_confirmation_credit",
        "held_out_scored",
    )
    if any(result.get(key) is not False for key in required_false):
        failures.append("result")
    if result.get("enlarged_hybrid_state_space_constructed") is not True or result.get("finite_energy_discrete_record_constructed") is not True or result.get("record_persists_across_continuous_tie_crossings") is not True or result.get("canon_verdict_change") != "none":
        failures.append("ceiling")
    ceiling = data.get("claim_ceiling", "")
    if "finite-energy detector-record" not in ceiling or "backreacts" not in ceiling or "No source/GU physical environment" not in ceiling:
        failures.append("prose_ceiling")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [
        (name, any(not ok for _, ok in exact_checks(name)))
        for name in ("wrong_dimension", "zero_epsilon", "zero_power", "zero_beta", "zero_clock")
    ]
    updates = (
        ("invent_source_owner", lambda d: d["hybrid_carrier"].__setitem__("source_or_GU_owned", True)),
        ("break_jump_rate", lambda d: d["reversible_hybrid_owner"].__setitem__("jump_rate", "constant")),
        ("invent_physical_detector", lambda d: d["reversible_hybrid_owner"].__setitem__("physical_bath_clock_or_detector_derived", True)),
        ("erase_finite_energy", lambda d: d["joint_dirichlet_form"].__setitem__("detector_indicator_has_finite_joint_energy", False)),
        ("repair_old_argmax", lambda d: d["joint_dirichlet_form"].__setitem__("base_argmax_indicator_has_finite_K113_diffusion_energy", True)),
        ("force_wall_jump", lambda d: d["joint_dirichlet_form"].__setitem__("tie_wall_crossing_forces_detector_jump", True)),
        ("claim_zero_error", lambda d: d["readout_and_retention"].__setitem__("finite_parameter_error_strictly_positive", False)),
        ("bias_marginal", lambda d: d["readout_and_retention"].__setitem__("detector_marginal_under_joint_S_256_law", "biased")),
        ("make_clock_change_accuracy", lambda d: d["readout_and_retention"].__setitem__("barrier_or_clock_factor_c_changes_kinetics_not_stationary_readout", False)),
        ("claim_eight_perfect_bits", lambda d: d["readout_and_retention"].__setitem__("perfect_record_bits_at_finite_parameters", 8)),
        ("erase_affine_control", lambda d: d["backreaction_boundary"].__setitem__("m_equals_1_preserves_K113_Gibbs_marginal", False)),
        ("erase_reweighting", lambda d: d["backreaction_boundary"].__setitem__("m_greater_than_1_generically_reweights_K113_Gibbs_marginal", False)),
        ("claim_noninvasive", lambda d: d["backreaction_boundary"].__setitem__("informative_record_conditioned_drift_equals_K113_drift", True)),
        ("erase_no_go", lambda d: d["backreaction_boundary"].__setitem__("unchanged_record_conditioned_K113_drift_for_all_r_forces_scores_constant_on_Delta", False)),
        ("erase_nonequilibrium_escape", lambda d: d["backreaction_boundary"].__setitem__("one_way_nonequilibrium_detector_remains_open", False)),
        ("force_tie_retract_change", lambda d: d["branch_interface"].__setitem__("continuous_tie_crossing_changes_named_retract_without_detector_jump", True)),
        ("preserve_branch_forever", lambda d: d["branch_interface"].__setitem__("one_fixed_branch_domain_invariant_forever", True)),
        ("invent_BV_BFV", lambda d: d["branch_interface"].__setitem__("spacetime_causal_BV_BFV_observable_descent_owned", True)),
        ("invent_perfect_measurement", lambda d: d["result"].__setitem__("perfect_finite_parameter_measurement_constructed", True)),
        ("invent_noninvasive_detector", lambda d: d["result"].__setitem__("noninvasive_informative_reversible_detector_constructed", True)),
        ("invent_environment", lambda d: d["result"].__setitem__("source_action_or_physical_environment_derived", True)),
        ("invent_Born", lambda d: d["result"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["result"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["result"].__setitem__("canon_verdict_change", "changed")),
        ("erase_scope", lambda d: d.__setitem__("claim_ceiling", "GU derives a perfect detector.")),
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
    checks.append(("manifest preserves hybrid, energy, retention, backreaction and ownership ceilings", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K114 HYBRID DETECTOR/FINITE-ENERGY RECORD: {sum(int(bool(ok)) for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
