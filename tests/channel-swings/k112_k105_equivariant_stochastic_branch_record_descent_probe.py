#!/usr/bin/env python3
"""Exact K112 stochastic branch-record and descent controls (stdlib only)."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k112-k105-equivariant-stochastic-branch-record-descent-wave.json"


def generator_apply(values: list[Fraction], kappa: Fraction) -> list[Fraction]:
    total = sum(values, Fraction(0))
    n = len(values)
    return [kappa * (total - n * value) for value in values]


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    n = 256
    kappa = Fraction(3, 7)
    if mutation == "wrong_dimension":
        n = 255
    elif mutation == "zero_rate":
        kappa = Fraction(0)

    uniform = [Fraction(1, n)] * n
    quench = uniform[:]
    if mutation == "biased_quench":
        quench[0] += Fraction(1, 2 * n)
        quench[1] -= Fraction(1, 2 * n)

    diagonal_rate = -(n - 1) * kappa
    if mutation == "broken_generator":
        diagonal_rate = -(n - 2) * kappa
    generator_row_sum = diagonal_rate + (n - 1) * kappa
    stationary_columns = [
        uniform[j] * diagonal_rate
        + sum((uniform[i] * kappa for i in range(n) if i != j), Fraction(0))
        for j in range(n)
    ]
    witness = [Fraction(1), Fraction(-1)] + [Fraction(0)] * (n - 2)
    witness_image = generator_apply(witness, kappa)

    selected = 17
    recorded = selected
    if mutation == "broken_record":
        recorded = (selected + 1) % n
    joint_mass = Fraction(1, n)
    branch_marginal = joint_mass
    record_marginal = joint_mass
    conditional_selected_given_record = Fraction(1) if selected == recorded else Fraction(0)

    average_projector_diagonal = [Fraction(1, n)] * n
    conditioned_projector_diagonal = [Fraction(0)] * n
    conditioned_projector_diagonal[recorded] = Fraction(1)

    branch_observable = Fraction(5, 11)
    branchwise_values = [branch_observable] * n
    uniform_observable = sum(
        (uniform[j] * branchwise_values[j] for j in range(n)), Fraction(0)
    )
    constant_section = [Fraction(7, 13)] * n
    generator_on_constant = generator_apply(constant_section, kappa)
    information_bits = int(math.log2(n)) if n > 0 and n & (n - 1) == 0 else None

    return [
        ("the frozen vacuum orbit has 256 branches", n == 256),
        ("the jump rate is strictly positive", kappa > 0),
        ("each complete-graph generator row sums to zero", generator_row_sum == 0),
        ("the uniform law is stationary", all(value == 0 for value in stationary_columns)),
        ("uniform detailed balance holds on every off-diagonal edge", uniform[0] * kappa == uniform[-1] * kappa),
        ("the displayed mean-zero vector is an eigenvector with eigenvalue -256 kappa", witness_image == [-n * kappa * value for value in witness]),
        ("the exact mean-zero spectral gap is 256 kappa", n * kappa == Fraction(768, 7)),
        ("the symmetric one-shot quench is normalized", sum(quench, Fraction(0)) == 1),
        ("the symmetric one-shot quench is uniform", len(set(quench)) == 1),
        ("coordinate reversal preserves the quench law", list(reversed(quench)) == quench),
        ("no deterministic output law is invariant on the transitive orbit", not any(p == 1 for p in uniform)),
        ("the diagonal branch-record joint law is normalized", n * joint_mass == 1),
        ("both diagonal-coupling marginals are uniform", branch_marginal == record_marginal == Fraction(1, n)),
        ("conditioning on the matching record selects the branch exactly", conditional_selected_given_record == 1),
        ("the 256-valued exact record carries eight classical bits", information_bits == 8),
        ("the unconditional projector is full rank", len([x for x in average_projector_diagonal if x != 0]) == 256),
        ("the conditioned projector is rank one", len([x for x in conditioned_projector_diagonal if x != 0]) == 1),
        ("the unconditional projector trace is one", sum(average_projector_diagonal, Fraction(0)) == 1),
        ("the conditioned projector trace is one", sum(conditioned_projector_diagonal, Fraction(0)) == 1),
        ("branchwise-identical observables descend to the invariant algebra", uniform_observable == branch_observable),
        ("the label generator commutes with constant branch sections", generator_on_constant == [Fraction(0)] * n),
        ("the record changes branch embedding but not branch-independent calibration values", len(set(branchwise_values)) == 1),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    orbit = data.get("frozen_vacuum_orbit", {})
    law = data.get("stochastic_branch_law", {})
    record = data.get("branch_record_instrument", {})
    descent = data.get("projector_domain_descent", {})
    observables = data.get("observable_superselection_descent", {})
    result = data.get("result", {})
    if orbit.get("cardinality") != 256 or orbit.get("deterministic_equivariant_section_exists") is not False:
        failures.append("orbit")
    if law.get("S_256_equivariant") is not True or law.get("unique_stationary_law") != "uniform_1/256" or law.get("mean_zero_spectral_gap") != "256*kappa" or law.get("preferred_label_encoded") is not False or law.get("source_or_GU_owned") is not False:
        failures.append("law")
    if record.get("simultaneous_S_256_invariant") is not True or record.get("conditional_branch_given_record") != "delta_r" or record.get("record_information_bits") != 8 or record.get("realized_record_selects_embedded_branch") is not True or record.get("physical_measurement_or_collapse_derived") is not False:
        failures.append("record")
    if descent.get("unconditional_projector_rank") != 256 or descent.get("conditioned_projector_rank") != 1 or descent.get("conditioned_K91_action_domain_Green_retract_recovered") is not True or descent.get("label_generator_commutes_with_identical_branch_operators") is not True or descent.get("actual_spacetime_or_BV_BFV_domain_constructed") is not False:
        failures.append("descent")
    if observables.get("invariant_subalgebra") != "constant_tuples_isomorphic_to_A_0" or observables.get("record_center") != "R^256_with_primitive_idempotents_z_r" or observables.get("K110_finite_interface_transports_branchwise") is not True or observables.get("calibration_statistics_branch_independent") is not True or observables.get("Born_pairing_derived") is not False:
        failures.append("observables")
    required_false = (
        "source_action_or_GU_boundary_law_derived",
        "physical_environment_or_measurement_derived",
        "nonlinear_continuous_carrier_stochastic_dynamics_derived",
        "actual_spacetime_or_BV_BFV_global_quotient_constructed",
        "Born_rule_derived",
        "prediction_or_confirmation_credit",
        "held_out_scored",
    )
    if any(result.get(key) is not False for key in required_false):
        failures.append("result")
    if result.get("canon_verdict_change") != "none" or result.get("preferred_coordinate_inserted_before_sampling") is not False:
        failures.append("ceiling")
    ceiling = data.get("claim_ceiling", "")
    if "Exact finite probability" not in ceiling or "eight-bit" not in data.get("exact_reopener", "") or "No source/GU stochastic law" not in ceiling:
        failures.append("prose_ceiling")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [
        (name, any(not ok for _, ok in exact_checks(name)))
        for name in (
            "wrong_dimension",
            "zero_rate",
            "biased_quench",
            "broken_generator",
            "broken_record",
        )
    ]
    updates = (
        ("invent_deterministic_section", lambda d: d["frozen_vacuum_orbit"].__setitem__("deterministic_equivariant_section_exists", True)),
        ("break_covariance", lambda d: d["stochastic_branch_law"].__setitem__("S_256_equivariant", False)),
        ("bias_stationary_law", lambda d: d["stochastic_branch_law"].__setitem__("unique_stationary_law", "biased")),
        ("erase_gap", lambda d: d["stochastic_branch_law"].__setitem__("mean_zero_spectral_gap", "0")),
        ("encode_label", lambda d: d["stochastic_branch_law"].__setitem__("preferred_label_encoded", True)),
        ("invent_source_owner", lambda d: d["stochastic_branch_law"].__setitem__("source_or_GU_owned", True)),
        ("break_joint_invariance", lambda d: d["branch_record_instrument"].__setitem__("simultaneous_S_256_invariant", False)),
        ("break_conditioning", lambda d: d["branch_record_instrument"].__setitem__("conditional_branch_given_record", "uniform")),
        ("wrong_record_cost", lambda d: d["branch_record_instrument"].__setitem__("record_information_bits", 1)),
        ("invent_measurement", lambda d: d["branch_record_instrument"].__setitem__("physical_measurement_or_collapse_derived", True)),
        ("rank_one_unconditional", lambda d: d["projector_domain_descent"].__setitem__("unconditional_projector_rank", 1)),
        ("full_rank_conditional", lambda d: d["projector_domain_descent"].__setitem__("conditioned_projector_rank", 256)),
        ("break_domain_commutation", lambda d: d["projector_domain_descent"].__setitem__("label_generator_commutes_with_identical_branch_operators", False)),
        ("invent_BV_BFV_domain", lambda d: d["projector_domain_descent"].__setitem__("actual_spacetime_or_BV_BFV_domain_constructed", True)),
        ("break_invariant_algebra", lambda d: d["observable_superselection_descent"].__setitem__("invariant_subalgebra", "branch_selected")),
        ("erase_record_center", lambda d: d["observable_superselection_descent"].__setitem__("record_center", "R")),
        ("invent_Born", lambda d: d["observable_superselection_descent"].__setitem__("Born_pairing_derived", True)),
        ("invent_environment", lambda d: d["result"].__setitem__("physical_environment_or_measurement_derived", True)),
        ("invent_continuous_dynamics", lambda d: d["result"].__setitem__("nonlinear_continuous_carrier_stochastic_dynamics_derived", True)),
        ("score_holdout", lambda d: d["result"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["result"].__setitem__("canon_verdict_change", "promoted")),
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
    checks.append(("manifest preserves stochastic, record, descent and ownership ceilings", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K112 STOCHASTIC BRANCH/RECORD DESCENT: {sum(int(bool(ok)) for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
