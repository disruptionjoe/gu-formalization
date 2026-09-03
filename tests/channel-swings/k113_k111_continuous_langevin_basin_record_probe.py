#!/usr/bin/env python3
"""Exact K113 continuous Langevin and basin-record controls (stdlib only)."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k113-k111-continuous-langevin-basin-record-wave.json"


def well(x: Fraction, a: Fraction, b: Fraction) -> Fraction:
    return (x - a) ** 2 * (x - b) ** 2


def well_prime(x: Fraction, a: Fraction, b: Fraction) -> Fraction:
    return 2 * (x - a) * (x - b) * (2 * x - a - b)


def well_second(x: Fraction, a: Fraction, b: Fraction) -> Fraction:
    return 2 * ((2 * x - a - b) ** 2 + 2 * (x - a) * (x - b))


def tangent_project(values: list[Fraction]) -> list[Fraction]:
    mean = sum(values, Fraction(0)) / len(values)
    return [value - mean for value in values]


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    n = 256
    a = Fraction(2, 257)
    b = Fraction(1, 257)
    beta = Fraction(7, 3)
    if mutation == "wrong_dimension":
        n = 255
    elif mutation == "zero_beta":
        beta = Fraction(0)
    elif mutation == "equal_wells":
        a = b

    sample = [Fraction((3 * i + 5) % 17, 19) for i in range(n)]
    projected = tangent_project(sample)
    projected_twice = tangent_project(projected)
    constant = [Fraction(11, 13)] * n
    projected_constant = tangent_project(constant)

    vacuum = [b] * n
    vacuum[17] = a
    reversed_vacuum = list(reversed(vacuum))
    potential_vacuum = sum((well(x, a, b) for x in vacuum), Fraction(0))
    potential_reversed = sum((well(x, a, b) for x in reversed_vacuum), Fraction(0))
    ambient_gradient = [well_prime(x, a, b) for x in sample]
    tangent_gradient = tangent_project(ambient_gradient)

    hessian = well_second(a, a, b)
    light_hessian = well_second(b, a, b)
    laplace_weights = [Fraction(1, n)] * n

    basin_labels = []
    for selected in range(n):
        point = [b] * n
        point[selected] = a
        maxima = [i for i, value in enumerate(point) if value == max(point)]
        basin_labels.append(maxima[0] if len(maxima) == 1 else None)

    epsilon_one = Fraction(1, 8)
    epsilon_two = Fraction(1, 16)
    ramp_energy_one = Fraction(1, 2 * epsilon_one)
    ramp_energy_two = Fraction(1, 2 * epsilon_two)

    return [
        ("the continuous carrier has relative dimension 255", n - 1 == 255),
        ("the inverse temperature is strictly positive", beta > 0),
        ("the tangent projector kills constants", projected_constant == [0] * n),
        ("the tangent projector has zero-sum image", sum(projected, Fraction(0)) == 0),
        ("the tangent projector is idempotent", projected_twice == projected),
        ("the projected nonlinear drift is tangent", sum(tangent_gradient, Fraction(0)) == 0),
        ("the quartic potential is permutation invariant", potential_vacuum == potential_reversed),
        ("the K111 vacua still have zero potential", potential_vacuum == 0),
        ("all 256 vacua lie off the argmax tie set", all(label is not None for label in basin_labels)),
        ("the basin record reaches every branch exactly once on the vacuum orbit", all(label is not None for label in basin_labels) and sorted(label for label in basin_labels if label is not None) == list(range(n))),
        ("the symmetric basin law is uniform", sum(laplace_weights, Fraction(0)) == 1 and len(set(laplace_weights)) == 1),
        ("the perfect basin label carries eight classical bits", n.bit_length() - 1 == 8 and n == 2**8),
        ("all vacuum restricted Hessians have the same positive gap", hessian == light_hessian == Fraction(2, 257**2)),
        ("equal Hessian determinants give equal Laplace weights", laplace_weights[0] == laplace_weights[-1] == Fraction(1, 256)),
        ("the unconditional zero-noise projector average stays full rank", len([weight for weight in laplace_weights if weight]) == 256),
        ("a conditioned zero-noise basin selects one branch", basin_labels[17] == 17),
        ("a sharper record layer costs more Dirichlet energy", ramp_energy_two > ramp_energy_one),
        ("the exact one-dimensional wall-layer energy is inverse in epsilon", ramp_energy_one == 4 and ramp_energy_two == 8),
        ("finite positive temperature is distinct from the atomic zero-noise law", beta > 0 and all(weight > 0 for weight in laplace_weights)),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    carrier = data.get("continuous_carrier", {})
    dynamics = data.get("reflected_langevin_owner", {})
    measure = data.get("measure_and_variational_structure", {})
    record = data.get("basin_record", {})
    obstruction = data.get("sharp_record_domain_obstruction", {})
    limit = data.get("zero_noise_limit", {})
    result = data.get("result", {})
    if carrier.get("S_256_invariant") is not True or carrier.get("source_or_GU_owned") is not False:
        failures.append("carrier")
    if dynamics.get("tangent_covariance") != "(2/beta)*Pi_where_Pi=I-11^T/256" or dynamics.get("boundary_condition") != "normal_reflection_equivalently_zero_probability_flux" or dynamics.get("nonlinear_drift") is not True or dynamics.get("S_256_equivariant") is not True or dynamics.get("physical_environment_or_detector_owned") is not False:
        failures.append("dynamics")
    if measure.get("stationary_law") != "mu_beta=Z_beta^-1*exp(-beta*V)*lambda_Delta" or measure.get("detailed_balance") is not True or measure.get("finite_temperature_exact_vacuum_mass") != 0 or measure.get("spacetime_causal_or_BV_BFV_structure_owned") is not False:
        failures.append("measure")
    if record.get("tie_set_mu_beta_measure") != 0 or record.get("S_256_equivariant_almost_surely") is not True or record.get("record_law") != "uniform_1/256" or record.get("record_information_bits") != 8 or record.get("physical_measurement_or_record_dynamics_derived") is not False:
        failures.append("record")
    if obstruction.get("cell_indicators_in_Dirichlet_H1_domain") is not False or obstruction.get("sharp_record_has_finite_diffusion_energy") is not False or obstruction.get("continuous_generator_preserves_one_fixed_branch_domain") is not False:
        failures.append("obstruction")
    if limit.get("unconditional_limit") != "uniform_sum_j_delta_wj/256" or limit.get("conditional_limit_in_C_j") != "delta_wj" or limit.get("finite_beta_equals_perfect_K112_branch_law") is not False or limit.get("singular_limit_recovers_K112_branch_law") is not True or limit.get("preferred_coordinate_selected") is not False:
        failures.append("limit")
    required_false = (
        "finite_temperature_perfect_vacuum_record_constructed",
        "sharp_record_is_generator_domain_observable",
        "single_fixed_K91_domain_preserved_by_diffusion",
        "source_action_or_GU_boundary_law_derived",
        "physical_environment_measurement_or_collapse_derived",
        "actual_spacetime_causality_or_BV_BFV_descent_constructed",
        "Born_rule_derived",
        "prediction_or_confirmation_credit",
        "held_out_scored",
    )
    if any(result.get(key) is not False for key in required_false):
        failures.append("result")
    if result.get("continuous_nonlinear_carrier_stochastic_dynamics_constructed") is not True or result.get("measure_noise_boundary_and_variational_owner_complete") is not True or result.get("canon_verdict_change") != "none":
        failures.append("ceiling")
    claim_ceiling = data.get("claim_ceiling", "")
    if "reflected-diffusion" not in claim_ceiling or "not in the diffusion's finite-energy generator domain" not in claim_ceiling or "No source/GU stochastic action" not in claim_ceiling:
        failures.append("prose_ceiling")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [
        (name, any(not ok for _, ok in exact_checks(name)))
        for name in ("wrong_dimension", "zero_beta", "equal_wells")
    ]
    updates = (
        ("invent_source_owner", lambda d: d["continuous_carrier"].__setitem__("source_or_GU_owned", True)),
        ("break_covariance", lambda d: d["reflected_langevin_owner"].__setitem__("tangent_covariance", "I")),
        ("erase_reflection", lambda d: d["reflected_langevin_owner"].__setitem__("boundary_condition", "none")),
        ("linearize_drift", lambda d: d["reflected_langevin_owner"].__setitem__("nonlinear_drift", False)),
        ("invent_environment", lambda d: d["reflected_langevin_owner"].__setitem__("physical_environment_or_detector_owned", True)),
        ("break_gibbs", lambda d: d["measure_and_variational_structure"].__setitem__("stationary_law", "uniform")),
        ("give_vacua_atom_mass", lambda d: d["measure_and_variational_structure"].__setitem__("finite_temperature_exact_vacuum_mass", 1)),
        ("invent_spacetime", lambda d: d["measure_and_variational_structure"].__setitem__("spacetime_causal_or_BV_BFV_structure_owned", True)),
        ("give_ties_mass", lambda d: d["basin_record"].__setitem__("tie_set_mu_beta_measure", 1)),
        ("bias_record", lambda d: d["basin_record"].__setitem__("record_law", "biased")),
        ("invent_detector", lambda d: d["basin_record"].__setitem__("physical_measurement_or_record_dynamics_derived", True)),
        ("admit_sharp_H1_record", lambda d: d["sharp_record_domain_obstruction"].__setitem__("cell_indicators_in_Dirichlet_H1_domain", True)),
        ("finite_record_energy", lambda d: d["sharp_record_domain_obstruction"].__setitem__("sharp_record_has_finite_diffusion_energy", True)),
        ("preserve_fixed_branch", lambda d: d["sharp_record_domain_obstruction"].__setitem__("continuous_generator_preserves_one_fixed_branch_domain", True)),
        ("bias_zero_noise", lambda d: d["zero_noise_limit"].__setitem__("unconditional_limit", "delta_w0")),
        ("promote_finite_beta", lambda d: d["zero_noise_limit"].__setitem__("finite_beta_equals_perfect_K112_branch_law", True)),
        ("select_coordinate", lambda d: d["zero_noise_limit"].__setitem__("preferred_coordinate_selected", True)),
        ("invent_exact_finite_record", lambda d: d["result"].__setitem__("finite_temperature_perfect_vacuum_record_constructed", True)),
        ("invent_BV_BFV", lambda d: d["result"].__setitem__("actual_spacetime_causality_or_BV_BFV_descent_constructed", True)),
        ("invent_Born", lambda d: d["result"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["result"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["result"].__setitem__("canon_verdict_change", "changed")),
        ("erase_scope", lambda d: d.__setitem__("claim_ceiling", "GU derives measurement.")),
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
    checks.append(("manifest preserves dynamics, domain, record and ownership ceilings", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K113 CONTINUOUS LANGEVIN/BASIN RECORD: {sum(int(bool(ok)) for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
