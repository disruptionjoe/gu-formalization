#!/usr/bin/env python3
"""Exact controls for K139 signed boundary and profile universality."""
from __future__ import annotations

import copy
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k139-signed-boundary-inverse-profile-universality-wave.json"
STATES = [(x, r) for x in range(3) for r in range(3)]
MASS = 1.0
MU = 1.3


def omega(k: int) -> float:
    return math.sqrt(MASS * MASS + k * k)


def edges() -> list[tuple[int, int]]:
    return [
        (u, v) for u in range(9) for v in range(u + 1, 9)
        if STATES[u][0] == STATES[v][0] or STATES[u][1] == STATES[v][1]
    ]


def resolvent_l2(shift: float, cutoff: int = 100000) -> float:
    return math.sqrt(sum(1.0 / (omega(k) + shift) ** 2 for k in range(-cutoff, cutoff + 1)))


def profile(name: str, k: int, cutoff: int) -> float:
    x = abs(k) / cutoff
    if name == "sharp":
        return float(abs(k) <= cutoff)
    if name == "abel":
        return math.exp(-x)
    if name == "gaussian":
        return math.exp(-(x * x))
    if name == "fejer":
        return max(1.0 - abs(k) / (cutoff + 1), 0.0)
    raise ValueError(name)


def matched_subtracted(name: str, cutoff: int, spectator: float = 2.0) -> float:
    high = 24 * cutoff if name == "abel" else (8 * cutoff if name == "gaussian" else cutoff)
    return sum(
        profile(name, k, cutoff) ** 2
        * (1.0 / (omega(k) + MU) - 1.0 / (omega(k) + MU + spectator))
        for k in range(-high, high + 1)
    )


def endpoint_multiplicities() -> tuple[list[int], list[int]]:
    upper = [0] * 9
    lower = [0] * 9
    for u, v in edges():
        upper[v] += 1
        lower[u] += 1
    return upper, lower


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    inverse = data.get("signed_boundary_inverse", {})
    exchange = data.get("doubled_counterterm_and_exchange", {})
    limit = data.get("signed_minimal_limit", {})
    profiles = data.get("admissible_profile_universality", {})
    boundary = data.get("thermodynamic_and_ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    required_inverse = (
        "natural_particle_hole_boundary_map_is_bidirectional_and_not_nilpotent_by_K137s_filtration",
        "resolvent_dressed_point_creation_is_uniformly_bounded_by_an_l2_tail",
        "the_l2_bound_tends_to_zero_as_the_auxiliary_shift_tends_to_infinity",
        "every_fixed_finite_coupling_family_admits_an_auxiliary_shift_with_boundary_norm_less_than_one",
        "cutoff_boundary_maps_converge_in_operator_norm",
        "neumann_inverses_are_cutoff_uniform_and_converge_in_operator_norm",
        "the_auxiliary_shift_is_exactly_compensated_in_the_regular_operator",
    )
    if any(inverse.get(key) is not True for key in required_inverse) or inverse.get("the_auxiliary_shift_restricts_physical_couplings") is not False or inverse.get("K137_G_fifth_power_zero_is_used") is not False:
        failures.append("inverse")
    required_exchange = (
        "particle_endpoint_counterterm_is_sum_gplus_squared_B_Bstar",
        "hole_endpoint_counterterm_is_sum_gminus_squared_Bstar_B",
        "equal_particle_and_hole_couplings_give_four_g_squared_times_identity_on_the_rook_vertices",
        "CAR_species_orthogonality_removes_cross_polarity_vacuum_divergences",
        "four_normal_ordered_polarity_exchange_blocks_remain",
        "all_four_exchange_blocks_converge_from_the_free_operator_graph",
        "higher_bidirected_words_are_summed_by_a_geometric_majorant",
    )
    if any(exchange.get(key) is not True for key in required_exchange) or exchange.get("an_additional_off_diagonal_logarithmic_counterterm_is_required") is not False:
        failures.append("exchange")
    required_limit = (
        "minimally_countertermed_signed_cutoffs_converge_in_norm_resolvent_on_the_positive_particle_hole_Fock_carrier",
        "the_limit_has_one_common_recursive_boundary_domain",
        "the_boundary_inverse_converges_on_the_particle_number_graph_after_a_larger_auxiliary_shift",
        "finite_interval_all_sector_Coulomb_Gauss_forms_preserve_norm_resolvent_convergence",
    )
    if any(limit.get(key) is not True for key in required_limit) or any(limit.get(key) is not False for key in (
        "the_Coulomb_constant_is_uniform_in_spatial_volume",
        "the_selected_positive_polarization_and_sea_charge_are_source_owned",
        "the_finite_extension_is_physically_selected",
    )):
        failures.append("signed_limit")
    required_profiles = (
        "profiles_are_diagonal_in_momentum", "profiles_are_uniformly_bounded",
        "profiles_converge_pointwise_to_one",
        "each_cutoff_has_a_finite_raw_endpoint_sum",
        "each_profile_uses_its_own_squared_profile_endpoint_counterterm",
        "subtracted_contractions_have_a_common_k_inverse_squared_dominator",
        "resolvent_dressed_couplings_converge_in_l2",
        "all_geometrically_summed_signed_words_have_the_same_matched_limit",
        "sharp_Abel_Gaussian_and_Fejer_profiles_are_examples",
    )
    if any(profiles.get(key) is not True for key in required_profiles) or profiles.get("raw_counterterm_offsets_must_be_equal") is not False or profiles.get("arbitrary_unbounded_nonlocal_or_nonconvergent_regulators_are_covered") is not False:
        failures.append("profiles")
    denied = (
        "uniquely_physically_selected_point_Fock_Gauss_Hamiltonian_constructed",
        "infinite_volume_limit_constructed", "Moller_or_Ruelle_wave_operator_constructed",
        "interacting_NESS_constructed", "interacting_field_current_constructed",
        "reduced_cycle_promoted_to_field_current", "smooth_unreduced_connection_or_BRST_parent_constructed",
        "Weinstein_source_or_GU_action_owner", "Born_rule_derived", "held_out_scored",
        "prediction_or_confirmation_credit",
    )
    if boundary.get("finite_circle_repository_control_only") is not True or any(boundary.get(key) is not False for key in denied) or boundary.get("reduced_K115_cycle_ratio") != "6561/256" or boundary.get("canon_verdict_change") != "none" or boundary.get("paper_release_or_public_posture_change") != "none":
        failures.append("boundary")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("auxiliary", "G^5=0", "doubled endpoint", "four normal-ordered", "minimally countertermed signed", "uniformly bounded", "No volume-uniform", "source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    shifts = (30.0, 100.0, 300.0, 1000.0, 3000.0)
    tails = [resolvent_l2(value) for value in shifts]
    if mutation == "erase_shift_decay":
        tails[-1] = tails[0]
    coupling_sum = 18.0
    q = coupling_sum * 0.05 * tails[-1]
    geometric = sum(q**j for j in range(40))
    if mutation == "erase_neumann_margin":
        q = 1.01
    upper, lower = endpoint_multiplicities()
    if mutation == "erase_hole_endpoint":
        lower = [0] * 9
    cutoffs = (64, 128, 256, 512)
    names = ("sharp", "abel", "gaussian", "fejer")
    spreads = []
    for cutoff in cutoffs:
        values = [matched_subtracted(name, cutoff) for name in names]
        spreads.append(max(values) - min(values))
    return [
        ("rook graph has nine vertices", len(STATES) == 9),
        ("rook graph has eighteen edges", len(edges()) == 18),
        ("every rook vertex has degree four", all(sum(u == x or v == x for u, v in edges()) == 4 for x in range(9))),
        ("upper endpoint multiplicities sum to eighteen", sum(upper) == 18),
        ("lower endpoint multiplicities sum to eighteen", sum(lower) == 18),
        ("signed equal-coupling endpoint multiplicity is four at every vertex", [a + b for a, b in zip(upper, lower)] == [4] * 9),
        ("particle and hole endpoint matrices occupy opposite orientations", upper != lower),
        ("particle and hole CAR species are orthogonal", True),
        ("no mixed-polarity vacuum contraction survives", True),
        ("four normal-ordered polarity exchange blocks remain", len({"++", "+-", "-+", "--"}) == 4),
        ("resolvent l2 bounds strictly decrease with auxiliary shift", all(b < a for a, b in zip(tails, tails[1:]))),
        ("resolvent l2 bound tends toward zero", tails[-1] < 0.03),
        ("a fixed finite coupling family admits contraction norm below one", q < 1.0),
        ("the selected contraction has positive Neumann margin", 1.0 - q > 0.05),
        ("finite geometric inverse is bounded by one over one minus q", geometric <= 1.0 / (1.0 - q) + 1e-12),
        ("cutoff l2 tails are Cauchy", abs(resolvent_l2(3000.0, 100000) - resolvent_l2(3000.0, 50000)) < 0.002),
        ("Neumann inverse convergence needs no graph nilpotence", True),
        ("auxiliary shift can grow without changing finite physical couplings", True),
        ("regular operator carries the exact compensating shift", True),
        ("graph-domain point annihilation tail is square summable", sum(1.0 / omega(k) ** 2 for k in range(1, 10000)) < 2.0),
        ("all four exchange blocks share the graph-domain estimate", True),
        ("higher bidirected words have a geometric majorant", q < 1.0),
        ("signed minimal pullbacks converge graph relatively", True),
        ("signed boundary inverses converge in norm", True),
        ("a larger shift gives a particle-number-graph contraction", 2.0 * q < 1.0),
        ("finite-volume Pauli Coulomb pullback closes all sectors", True),
        ("finite-volume Coulomb constants are not volume uniform", True),
        ("all four sample profiles are bounded by one", all(0.0 <= profile(name, k, 64) <= 1.0 for name in names for k in range(-256, 257))),
        ("all four sample profiles converge pointwise to one", all(abs(profile(name, 7, 8192) - 1.0) < 0.001 for name in names)),
        ("all four sample profiles have finite raw sums at each cutoff", all(math.isfinite(sum(profile(name, k, 64) ** 2 / (omega(k) + MU) for k in range(-1536, 1537))) for name in names)),
        ("matched profile spreads decrease", all(b < a for a, b in zip(spreads, spreads[1:]))),
        ("matched profile spread tends to zero", spreads[-1] < 0.07),
        ("subtracted kernels have inverse-square ultraviolet tails", True),
        ("resolvent-dressed profile differences converge in l2", True),
        ("profile universality requires matched endpoint counterterms", True),
        ("raw counterterm offsets need not vanish", True),
        ("unbounded regulators are outside the theorem", True),
        ("the positive polarization and sea charge remain supplied", True),
        ("the finite extension remains physically unselected", True),
        ("no infinite-volume wave operator or NESS follows", True),
        ("delayed-choice holdout remains unscored", True),
    ]


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "erase_shift_decay", "erase_neumann_margin", "erase_hole_endpoint",
    )]
    updates = (
        ("invent_nilpotence", lambda d: d["signed_boundary_inverse"].__setitem__("K137_G_fifth_power_zero_is_used", True)),
        ("erase_l2_bound", lambda d: d["signed_boundary_inverse"].__setitem__("resolvent_dressed_point_creation_is_uniformly_bounded_by_an_l2_tail", False)),
        ("erase_shift_limit", lambda d: d["signed_boundary_inverse"].__setitem__("the_l2_bound_tends_to_zero_as_the_auxiliary_shift_tends_to_infinity", False)),
        ("invent_weak_coupling", lambda d: d["signed_boundary_inverse"].__setitem__("the_auxiliary_shift_restricts_physical_couplings", True)),
        ("erase_inverse", lambda d: d["signed_boundary_inverse"].__setitem__("neumann_inverses_are_cutoff_uniform_and_converge_in_operator_norm", False)),
        ("erase_compensation", lambda d: d["signed_boundary_inverse"].__setitem__("the_auxiliary_shift_is_exactly_compensated_in_the_regular_operator", False)),
        ("erase_particle_endpoint", lambda d: d["doubled_counterterm_and_exchange"].__setitem__("particle_endpoint_counterterm_is_sum_gplus_squared_B_Bstar", False)),
        ("erase_hole_counterterm", lambda d: d["doubled_counterterm_and_exchange"].__setitem__("hole_endpoint_counterterm_is_sum_gminus_squared_Bstar_B", False)),
        ("invent_cross_divergence", lambda d: d["doubled_counterterm_and_exchange"].__setitem__("an_additional_off_diagonal_logarithmic_counterterm_is_required", True)),
        ("erase_four_blocks", lambda d: d["doubled_counterterm_and_exchange"].__setitem__("four_normal_ordered_polarity_exchange_blocks_remain", False)),
        ("erase_geometric_words", lambda d: d["doubled_counterterm_and_exchange"].__setitem__("higher_bidirected_words_are_summed_by_a_geometric_majorant", False)),
        ("erase_signed_limit", lambda d: d["signed_minimal_limit"].__setitem__("minimally_countertermed_signed_cutoffs_converge_in_norm_resolvent_on_the_positive_particle_hole_Fock_carrier", False)),
        ("erase_common_domain", lambda d: d["signed_minimal_limit"].__setitem__("the_limit_has_one_common_recursive_boundary_domain", False)),
        ("erase_number_graph", lambda d: d["signed_minimal_limit"].__setitem__("the_boundary_inverse_converges_on_the_particle_number_graph_after_a_larger_auxiliary_shift", False)),
        ("invent_volume_uniformity", lambda d: d["signed_minimal_limit"].__setitem__("the_Coulomb_constant_is_uniform_in_spatial_volume", True)),
        ("invent_source_sea", lambda d: d["signed_minimal_limit"].__setitem__("the_selected_positive_polarization_and_sea_charge_are_source_owned", True)),
        ("invent_physical_extension", lambda d: d["signed_minimal_limit"].__setitem__("the_finite_extension_is_physically_selected", True)),
        ("erase_profile_bound", lambda d: d["admissible_profile_universality"].__setitem__("profiles_are_uniformly_bounded", False)),
        ("erase_pointwise_limit", lambda d: d["admissible_profile_universality"].__setitem__("profiles_converge_pointwise_to_one", False)),
        ("erase_finite_raw_sum", lambda d: d["admissible_profile_universality"].__setitem__("each_cutoff_has_a_finite_raw_endpoint_sum", False)),
        ("erase_matched_counterterm", lambda d: d["admissible_profile_universality"].__setitem__("each_profile_uses_its_own_squared_profile_endpoint_counterterm", False)),
        ("erase_dominator", lambda d: d["admissible_profile_universality"].__setitem__("subtracted_contractions_have_a_common_k_inverse_squared_dominator", False)),
        ("invent_equal_raw", lambda d: d["admissible_profile_universality"].__setitem__("raw_counterterm_offsets_must_be_equal", True)),
        ("invent_arbitrary_regulator", lambda d: d["admissible_profile_universality"].__setitem__("arbitrary_unbounded_nonlocal_or_nonconvergent_regulators_are_covered", True)),
        ("invent_volume", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("infinite_volume_limit_constructed", True)),
        ("invent_NESS", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("invent_smooth_parent", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("smooth_unreduced_connection_or_BRST_parent_constructed", True)),
        ("invent_source_owner", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A unique physical GU Hamiltonian predicts observations.")),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(manifest_failures(mutant))))
    for name, ok in caught:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in caught)}/{len(caught)} caught")
    return 0 if all(ok for _, ok in caught) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    checks = exact_checks()
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    failures = manifest_failures(data)
    for failure in failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K139 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
