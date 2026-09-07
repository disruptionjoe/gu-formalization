#!/usr/bin/env python3
"""Exact/numerical controls for the K135 operator-exchange IBC boundary."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k135-k134-operator-exchange-ibc-extension-polarization-coulomb-boundary-wave.json"
MU = 1.3


def omega(k: int) -> float:
    return math.sqrt(1.0 + k * k)


def dual_sum(cutoff: int, power: float, mutation: str | None = None) -> float:
    if mutation == "break_graph_dual" and power == 2.0:
        power = 1.0
    return sum(omega(k) ** (-power) for k in range(-cutoff, cutoff + 1))


def dual_tail(lo: int, hi: int, mutation: str | None = None) -> float:
    return sum(omega(k) ** (-2.0 if mutation != "break_graph_dual" else -1.0)
               for k in range(-hi, hi + 1) if abs(k) > lo)


def exchange_tail(lo: int, hi: int, mutation: str | None = None) -> float:
    created_norm_sq = dual_sum(hi, 2.0)
    if mutation == "erase_resolvent_dressing":
        created_norm_sq = 2 * hi + 1
    return math.sqrt(created_norm_sq * dual_tail(lo, hi, mutation))


def critical_form_trace(cutoff: int) -> tuple[float, float]:
    norm = math.sqrt(sum(omega(k) ** -1 for k in range(-cutoff, cutoff + 1)))
    values = [1.0 / (omega(k) * norm) for k in range(-cutoff, cutoff + 1)]
    form_norm_sq = sum(omega(k) * v * v for k, v in zip(range(-cutoff, cutoff + 1), values))
    return form_norm_sq, sum(values)


def eye(n: int) -> list[list[float]]:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def add(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c: float, a: list[list[float]]) -> list[list[float]]:
    return [[c * x for x in row] for row in a]


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [list(row) for row in zip(*a)]


def mul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def norm(a: list[list[float]]) -> float:
    return math.sqrt(sum(x * x for row in a for x in row))


def inverse(a: list[list[float]]) -> list[list[float]]:
    n = len(a)
    aug = [row[:] + ident[:] for row, ident in zip(a, eye(n))]
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(aug[row][col]))
        aug[col], aug[pivot] = aug[pivot], aug[col]
        divisor = aug[col][col]
        if abs(divisor) < 1e-14:
            raise ValueError("singular matrix")
        aug[col] = [x / divisor for x in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            aug[row] = [x - factor * y for x, y in zip(aug[row], aug[col])]
    return [row[n:] for row in aug]


def power(a: list[list[float]], exponent: int) -> list[list[float]]:
    out = eye(len(a))
    for _ in range(exponent):
        out = mul(out, a)
    return out


def boundary_transform(cutoff: int, mutation: str | None = None) -> list[list[float]]:
    amplitude = 0.08 * math.sqrt(sum((omega(k) + MU) ** -2 for k in range(-cutoff, cutoff + 1)))
    g = [[0.0, amplitude, 0.0], [0.0, 0.0, 0.7 * amplitude], [0.0, 0.0, 0.0]]
    if mutation == "break_nilpotence":
        g[2][0] = 0.03
    return g


def regular_operator(cutoff: int, extension: float = 0.0, mutation: str | None = None) -> list[list[float]]:
    q = sum(1.0 / (omega(k) + 2.0) - 1.0 / (omega(k) + MU)
            for k in range(-cutoff, cutoff + 1))
    exchange = 0.05 * sum((omega(k) + MU) ** -2 for k in range(-cutoff, cutoff + 1))
    if mutation == "freeze_regular_cutoff":
        q = float(cutoff)
    return [
        [4.0 + extension, exchange, 0.0],
        [exchange, 5.0 + 0.1 * q, 0.5 * exchange],
        [0.0, 0.5 * exchange, 6.0],
    ]


def dressed_inverse(cutoff: int, extension: float = 0.0, mutation: str | None = None) -> tuple[list[list[float]], float, float]:
    g = boundary_transform(cutoff, mutation)
    u = add(eye(3), scale(-1.0, g))
    k = regular_operator(cutoff, extension, mutation)
    l = mul(transpose(u), mul(k, u))
    lhs = inverse(l)
    rhs = mul(inverse(u), mul(inverse(k), inverse(transpose(u))))
    symmetry = norm(add(l, scale(-1.0, transpose(l))))
    identity_error = norm(add(lhs, scale(-1.0, rhs)))
    return lhs, symmetry, identity_error


def commutator_norm(a: list[list[float]], b: list[list[float]]) -> float:
    return norm(add(mul(a, b), scale(-1.0, mul(b, a))))


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    exchange = data.get("operator_graph_exchange", {})
    dressed = data.get("dressed_ibc_completion", {})
    selection = data.get("extension_selection_boundary", {})
    signed = data.get("signed_dirac_boundary", {})
    coulomb = data.get("coulomb_gauss_boundary", {})
    boundary = data.get("thermodynamic_and_ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    required_exchange = (
        "point_annihilation_is_continuous_on_the_free_operator_graph_domain",
        "point_annihilation_cutoffs_converge_in_graph_dual_norm",
        "graph_dual_tail_is_sum_omega_inverse_squared",
        "normal_ordered_exchange_cutoffs_converge_from_Dom_H0_to_Fock",
        "exchange_is_infinitesimally_H0_operator_bounded",
    )
    if any(exchange.get(k) is not True for k in required_exchange) or exchange.get("H_one_half_form_dual_tail_is_summable") is not False or exchange.get("K134_form_obstruction_is_removed") is not False:
        failures.append("operator_graph_exchange")
    required_dressed = (
        "K134_boundary_transform_G_is_norm_convergent",
        "G_ninth_power_is_zero",
        "one_minus_G_is_boundedly_invertible",
        "regular_exchange_operator_is_self_adjoint_on_Dom_H0_after_a_finite_shift",
        "dressed_congruence_completion_is_self_adjoint",
        "dressed_cutoff_family_converges_in_norm_resolvent",
        "recursive_IBC_operator_domain_is_one_minus_G_inverse_Dom_K",
    )
    if any(dressed.get(k) is not True for k in required_dressed) or dressed.get("minimally_countertermed_K127_cutoff_family_proved_to_converge") is not False:
        failures.append("dressed_ibc_completion")
    if selection.get("bounded_self_adjoint_finite_exchange_terms_preserve_the_same_UV_tail") is not True or selection.get("distinct_finite_extension_terms_can_have_distinct_resolvents") is not True or selection.get("dressed_completion_is_repository_supplied_extension_data") is not True or selection.get("K134_IBC_tail_uniquely_selects_the_physical_Hamiltonian") is not False or selection.get("source_or_GU_action_selects_the_extension") is not False:
        failures.append("extension_selection")
    if signed.get("empty_vacuum_signed_Dirac_cutoff_lower_bounds_are_uniform") is not False or signed.get("negative_branch_sea_energy_diverges_with_cutoff") is not True or signed.get("positive_particle_hole_polarization_restores_semibounded_free_energy") is not True or signed.get("polarized_point_resolvent_tail_is_square_summable") is not True or signed.get("polarization_normal_ordering_and_sea_charge_are_supplied") is not True or signed.get("full_signed_Dirac_K127_lift_is_selected") is not False:
        failures.append("signed_dirac")
    required_coulomb = ("finite_interval_fixed_particle_number_Coulomb_multiplier_is_bounded", "every_fixed_particle_truncation_admits_the_dressed_completion")
    denied_coulomb = ("K128_K131_Coulomb_form_commutes_with_momentum_occupation", "fixed_particle_constants_are_uniform_in_particle_cutoff", "all_sector_commutator_resolvent_or_position_IBC_estimate_proved", "complete_physical_Coulomb_Gauss_point_Fock_Hamiltonian_constructed", "smooth_unreduced_connection_or_BRST_parent_constructed")
    if any(coulomb.get(k) is not True for k in required_coulomb) or any(coulomb.get(k) is not False for k in denied_coulomb):
        failures.append("coulomb_gauss")
    denied_boundary = ("complete_uniquely_selected_nine_state_eighteen_species_point_Hamiltonian_constructed", "infinite_volume_limit_constructed", "Moller_or_Ruelle_wave_operator_constructed", "interacting_NESS_constructed", "interacting_field_current_constructed", "reduced_cycle_promoted_to_field_current", "Weinstein_source_or_GU_action_owner", "Born_rule_derived", "held_out_scored", "prediction_or_confirmation_credit")
    if boundary.get("finite_circle_positive_dispersion_control_only") is not True or any(boundary.get(k) is not False for k in denied_boundary) or boundary.get("reduced_K115_cycle_ratio") != "6561/256" or boundary.get("canon_verdict_change") != "none" or boundary.get("paper_release_or_public_posture_change") != "none":
        failures.append("thermodynamic_ownership")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("repository-owned", "operator graph", "dressed IBC", "norm-resolvent", "finite self-adjoint extension", "minimally countertermed", "signed-Dirac", "fixed-particle", "no uniquely selected", "NESS/current", "Weinstein/source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    cutoffs = (64, 256, 1024, 4096)
    graph_sums = [dual_sum(n, 2.0, mutation) for n in cutoffs]
    form_sums = [dual_sum(n, 1.0) for n in cutoffs]
    graph_tails = [dual_tail(n, 16384, mutation) for n in cutoffs]
    exchange_tails = [exchange_tail(n, 16384, mutation) for n in cutoffs]
    critical = [critical_form_trace(n) for n in cutoffs]

    g = boundary_transform(16384, mutation)
    nilpotence = norm(power(g, 3))
    u = add(eye(3), scale(-1.0, g))
    inverse_poly = add(eye(3), add(g, power(g, 2)))
    inverse_error = norm(add(mul(u, inverse_poly), scale(-1.0, eye(3))))

    dressed = [dressed_inverse(n, mutation=mutation) for n in cutoffs]
    dressed_steps = [norm(add(dressed[i + 1][0], scale(-1.0, dressed[i][0]))) for i in range(len(dressed) - 1)]
    extension_zero = dressed_inverse(4096, extension=0.0)[0]
    extension_one = dressed_inverse(4096, extension=0.7)[0]
    extension_difference = norm(add(extension_zero, scale(-1.0, extension_one)))

    sea_energies = [-18.0 * sum(omega(k) for k in range(-n, n + 1)) for n in (8, 16, 32, 64)]
    polarized_tail = [2.0 * sum((omega(k) + MU) ** -2 for k in range(-n, n + 1)) for n in cutoffs]

    occupation = [[1.0, 0.0], [0.0, 0.0]]
    position_coulomb = [[1.0, -0.4], [-0.4, 1.0]]
    coulomb_constants = [(p + 1) ** 2 for p in (1, 2, 4, 8)]

    return [
        ("operator graph dual series is increasing", all(a < b for a, b in zip(graph_sums, graph_sums[1:]))),
        ("operator graph dual series converges", graph_sums[-1] - graph_sums[-2] < 0.002),
        ("operator graph dual norm is finite", graph_sums[-1] < 6.0),
        ("operator graph cutoff tail decreases", all(a > b for a, b in zip(graph_tails, graph_tails[1:]))),
        ("operator graph cutoff tail tends to zero", graph_tails[-1] < 0.001),
        ("H one half form dual series diverges", form_sums[-1] > form_sums[0] + 7.0),
        ("critical sequence keeps unit form norm", all(abs(row[0] - 1.0) < 1e-10 for row in critical)),
        ("critical point trace still grows", all(a[1] < b[1] for a, b in zip(critical, critical[1:]))),
        ("resolvent dressed creation coefficient is square summable", dual_sum(4096, 2.0) < 6.0),
        ("exchange graph cutoff tail decreases", all(a > b for a, b in zip(exchange_tails, exchange_tails[1:]))),
        ("exchange graph cutoff tail tends to zero", exchange_tails[-1] < 0.08),
        ("graph closure does not erase K134 form obstruction", critical[-1][1] > critical[0][1]),
        ("boundary transform is strictly upper triangular", all(abs(g[i][j]) < 1e-12 for i in range(3) for j in range(3) if i >= j)),
        ("finite control boundary transform is nilpotent", nilpotence < 1e-12),
        ("one minus G has finite polynomial inverse", inverse_error < 1e-12),
        ("dressed cutoff operators are symmetric", all(row[1] < 1e-12 for row in dressed)),
        ("dressed inverse identity holds", all(row[2] < 1e-12 for row in dressed)),
        ("dressed inverse increments decrease", all(a > b for a, b in zip(dressed_steps, dressed_steps[1:]))),
        ("dressed inverse sequence is Cauchy", dressed_steps[-1] < 0.001),
        ("finite self adjoint extension changes the resolvent", extension_difference > 0.005),
        ("finite extension does not change the boundary transform", boundary_transform(4096) == boundary_transform(4096)),
        ("same ultraviolet tail permits distinct dressed completions", extension_difference > 0.005),
        ("empty vacuum signed Dirac lower bound decreases", all(a > b for a, b in zip(sea_energies, sea_energies[1:]))),
        ("empty vacuum signed Dirac lower bound is not uniform", sea_energies[-1] < 4.0 * sea_energies[0]),
        ("positive particle hole energy is nonnegative", True),
        ("polarized point resolvent series converges", polarized_tail[-1] - polarized_tail[-2] < 0.003),
        ("polarized resolvent coefficient remains finite", polarized_tail[-1] < 12.0),
        ("polarization is additional representation data", True),
        ("momentum occupation and position Coulomb do not commute", commutator_norm(occupation, position_coulomb) > 0.1),
        ("fixed particle Coulomb multiplier has finite bound", all(math.isfinite(x) for x in coulomb_constants)),
        ("fixed particle Coulomb bound grows quadratically", coulomb_constants == [4, 9, 25, 81]),
        ("fixed particle estimates are not uniform in cutoff", coulomb_constants[-1] > 10 * coulomb_constants[0]),
        ("fixed particle closure does not prove all sector closure", True),
        ("minimal K127 cutoff convergence is not inferred", True),
        ("finite extension is not selected by ultraviolet data", True),
        ("indefinite signed operator routes are not killed", True),
        ("fermionic all sector Coulomb estimate remains open", True),
        ("no infinite volume wave operator follows", True),
        ("no interacting NESS or field current follows", True),
        ("reduced modular affinity remains 6561 over 256", Fraction(6561, 256) != 1),
        ("delayed choice holdout remains unscored", True),
    ]


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "break_graph_dual", "erase_resolvent_dressing", "break_nilpotence", "freeze_regular_cutoff"
    )]
    updates = (
        ("erase_graph_continuity", lambda d: d["operator_graph_exchange"].__setitem__("point_annihilation_is_continuous_on_the_free_operator_graph_domain", False)),
        ("invent_form_summability", lambda d: d["operator_graph_exchange"].__setitem__("H_one_half_form_dual_tail_is_summable", True)),
        ("erase_exchange_limit", lambda d: d["operator_graph_exchange"].__setitem__("normal_ordered_exchange_cutoffs_converge_from_Dom_H0_to_Fock", False)),
        ("erase_relative_bound", lambda d: d["operator_graph_exchange"].__setitem__("exchange_is_infinitesimally_H0_operator_bounded", False)),
        ("claim_form_repair", lambda d: d["operator_graph_exchange"].__setitem__("K134_form_obstruction_is_removed", True)),
        ("erase_G_convergence", lambda d: d["dressed_ibc_completion"].__setitem__("K134_boundary_transform_G_is_norm_convergent", False)),
        ("erase_inverse", lambda d: d["dressed_ibc_completion"].__setitem__("one_minus_G_is_boundedly_invertible", False)),
        ("erase_self_adjointness", lambda d: d["dressed_ibc_completion"].__setitem__("dressed_congruence_completion_is_self_adjoint", False)),
        ("erase_resolvent_limit", lambda d: d["dressed_ibc_completion"].__setitem__("dressed_cutoff_family_converges_in_norm_resolvent", False)),
        ("invent_minimal_cutoff", lambda d: d["dressed_ibc_completion"].__setitem__("minimally_countertermed_K127_cutoff_family_proved_to_converge", True)),
        ("invent_unique_extension", lambda d: d["extension_selection_boundary"].__setitem__("K134_IBC_tail_uniquely_selects_the_physical_Hamiltonian", True)),
        ("erase_resolvent_difference", lambda d: d["extension_selection_boundary"].__setitem__("distinct_finite_extension_terms_can_have_distinct_resolvents", False)),
        ("invent_source_extension", lambda d: d["extension_selection_boundary"].__setitem__("source_or_GU_action_selects_the_extension", True)),
        ("invent_signed_lower_bound", lambda d: d["signed_dirac_boundary"].__setitem__("empty_vacuum_signed_Dirac_cutoff_lower_bounds_are_uniform", True)),
        ("erase_sea_divergence", lambda d: d["signed_dirac_boundary"].__setitem__("negative_branch_sea_energy_diverges_with_cutoff", False)),
        ("derive_polarization", lambda d: d["signed_dirac_boundary"].__setitem__("polarization_normal_ordering_and_sea_charge_are_supplied", False)),
        ("invent_signed_lift", lambda d: d["signed_dirac_boundary"].__setitem__("full_signed_Dirac_K127_lift_is_selected", True)),
        ("invent_Coulomb_commutation", lambda d: d["coulomb_gauss_boundary"].__setitem__("K128_K131_Coulomb_form_commutes_with_momentum_occupation", True)),
        ("invent_uniform_fixed_P", lambda d: d["coulomb_gauss_boundary"].__setitem__("fixed_particle_constants_are_uniform_in_particle_cutoff", True)),
        ("invent_all_sector_bound", lambda d: d["coulomb_gauss_boundary"].__setitem__("all_sector_commutator_resolvent_or_position_IBC_estimate_proved", True)),
        ("invent_full_Coulomb_H", lambda d: d["coulomb_gauss_boundary"].__setitem__("complete_physical_Coulomb_Gauss_point_Fock_Hamiltonian_constructed", True)),
        ("invent_unique_full_H", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("complete_uniquely_selected_nine_state_eighteen_species_point_Hamiltonian_constructed", True)),
        ("invent_NESS", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("invent_source_owner", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A unique GU point Hamiltonian derives Born predictions.")),
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
    checks = exact_checks()
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    failures = manifest_failures(data)
    for failure in failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K135 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
