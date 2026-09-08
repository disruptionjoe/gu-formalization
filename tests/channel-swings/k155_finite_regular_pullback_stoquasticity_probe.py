#!/usr/bin/env python3
"""Exact and hostile controls for the K155 finite pullback result."""

from __future__ import annotations

import copy
import json
import sys
from fractions import Fraction
from pathlib import Path

from k155_finite_regular_pullback import (
    CertificateError,
    add,
    charge_block,
    charge_components,
    demo,
    flavor_covariant,
    identity,
    induced_infinity_norm,
    matched_endpoint_counterterm,
    matmul,
    neumann_regular_tail_bound,
    regular_pullback,
    scale,
    state_label,
    stoquastic_gauge_certificate,
    transpose,
)


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k155-finite-regular-pullback-stoquasticity-obstruction-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k155-finite-regular-pullback-stoquasticity-obstruction-wave-2026-09-08.md"


def rejects(callable_) -> bool:
    try:
        callable_()
    except (CertificateError, AssertionError, KeyError, TypeError, ValueError):
        return True
    return False


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    fixed = data.get("fixed_control", {})
    pullback = data.get("finite_regular_pullback", {})
    tail = data.get("finite_neumann_certificate", {})
    count = data.get("charge_and_count_discriminator", {})
    bounds = data.get("boundaries", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("classification/direction")
    if fixed.get("representative_charges") != [[0, 0], [1, 0]] or fixed.get("flavor_partner") != [0, 1]:
        failures.append("charge scope")
    if fixed.get("auxiliary_chart_shift") != 256 or fixed.get("finite_regulator_only") is not True:
        failures.append("finite scope")
    required_pullback = (
        "boundary_halves_are_separated_as_C_and_Cstar",
        "pullback_identity_exact",
        "finite_counterterm_is_supplied_not_source_selected",
    )
    if any(pullback.get(key) is not True for key in required_pullback):
        failures.append("pullback contract")
    if pullback.get("coefficient_complete_native_R256_identified") is not False:
        failures.append("native R256 fence")
    required_tail = (
        "requires_one_norm_contraction",
        "requires_infinity_norm_contraction",
        "exact_error_is_checked_against_bound",
    )
    if any(tail.get(key) is not True for key in required_tail):
        failures.append("tail contract")
    if tail.get("finite_matrix_tail_is_common_carrier_graph_tail") is not False or tail.get("K139_graph_relative_limit_reproved") is not False:
        failures.append("graph-tail fence")
    if count.get("signed_flavor_swap_intertwines_R_q10_and_R_q01") is not True:
        failures.append("flavor covariance")
    for key in (
        "one_mode_q00_occupation_graph_connected",
        "one_mode_q10_occupation_graph_connected",
        "one_mode_representatives_admit_diagonal_sign_stoquastic_gauge",
        "two_mode_q00_occupation_graph_connected",
        "two_mode_q10_occupation_graph_connected",
    ):
        if count.get(key) is not True:
            failures.append(key)
    for key in (
        "two_mode_q00_admits_diagonal_sign_stoquastic_gauge",
        "two_mode_q10_admits_diagonal_sign_stoquastic_gauge",
        "standard_occupation_basis_Perron_Frobenius_route_certifies_native_ground_count",
        "another_non_diagonal_positivity_cone_excluded",
        "finite_ground_degeneracy_proved",
        "native_continuum_ground_degeneracy_proved",
        "native_ground_count_or_exterior_floor_certified",
    ):
        if count.get(key) is not False:
            failures.append(key)
    if count.get("q00_obstruction_cycle_length") != 6 or count.get("q00_obstruction_cycle_edge_signs") != [1, 1, 1, 1, 1, -1]:
        failures.append("frustrated cycle")
    if count.get("q00_cycle_sign_product") != -1 or count.get("q00_stoquastic_required_sign_product") != 1:
        failures.append("cycle parity")
    allowed_true = {"finite_exact_R_N_serialized"}
    for key, value in bounds.items():
        if key in allowed_true:
            if value is not True:
                failures.append(key)
        elif key in ("canon_verdict_change", "paper_release_or_public_posture_change"):
            if value != "none":
                failures.append(key)
        elif value is not False:
            failures.append(key)
    ceiling = data.get("claim_ceiling", "")
    if not all(
        phrase in ceiling
        for phrase in (
            "finite-regulator theorem",
            "does not prove degeneracy",
            "do not identify the common-carrier continuum R_256",
            "no native residual",
        )
    ):
        failures.append("claim ceiling")
    return failures


def checks(data: dict, text: str) -> list[tuple[str, bool]]:
    one = regular_pullback(["5/4"], [1], (0, 0), 256)
    one_tail_1 = neumann_regular_tail_bound(one, 1)
    one_tail_3 = neumann_regular_tail_bound(one, 3)
    states, free, c, cstar = charge_components(["5/4"], [1], (0, 0))
    endpoint = matched_endpoint_counterterm(states, ["5/4"], [1], 256)
    one_sign = stoquastic_gauge_certificate(add(c, cstar))
    _, _, c10, cs10 = charge_components(["5/4"], [1], (1, 0))
    one_sign_10 = stoquastic_gauge_certificate(add(c10, cs10))
    states2, _, c2, cs2 = charge_components(["5/4", "3/2"], [1, 1], (0, 0))
    _, k151_one = charge_block(["5/4"], [1], (0, 0))
    _, k151_two = charge_block(["5/4", "3/2"], [1, 1], (0, 0))
    _, free2, _, _ = charge_components(["5/4", "3/2"], [1, 1], (0, 0))
    two_sign = stoquastic_gauge_certificate(add(c2, cs2))
    states210, _, c210, cs210 = charge_components(["5/4", "3/2"], [1, 1], (1, 0))
    two_sign_10 = stoquastic_gauge_certificate(add(c210, cs210))
    output = demo()
    cycle_labels = [state_label(states2[vertex], 2) for vertex in two_sign["cycle"]]
    return [
        ("schema", data.get("schema_version") == "1.0"),
        ("manifest contract", not manifest_failures(data)),
        ("finite basis nonempty", bool(states)),
        ("free matrix diagonal", all(not free[i][j] for i in range(len(free)) for j in range(len(free)) if i != j)),
        ("boundary halves adjoint", cstar == transpose(c)),
        ("one mode reconstructs K151 H", add(free, c, cstar) == k151_one),
        ("two mode reconstructs K151 H", add(free2, c2, cs2) == k151_two),
        ("finite H symmetric", one["H"] == transpose(one["H"])),
        ("finite R symmetric", one["R"] == transpose(one["R"])),
        ("chart inverse left", matmul(one["U_inverse"], one["U"]) == identity(len(states))),
        ("chart inverse right", matmul(one["U"], one["U_inverse"]) == identity(len(states))),
        ("boundary generator identity", matmul(one["shifted_free"], one["G"]) == scale(Fraction(-1), one["Cstar"])),
        ("direct pullback identity", matmul(transpose(one["U"]), matmul(one["R"], one["U"])) == one["H"]),
        ("expanded pullback exact", one["R"] == add(one["shifted_free"], matmul(transpose(one["U_inverse"]), matmul(one["regular_core"], one["U_inverse"])))),
        ("endpoint diagonal", endpoint == transpose(endpoint)),
        ("vacuum endpoint twice leaf", endpoint[0][0] == 2 * endpoint[1][1]),
        ("one norm contraction", one_tail_1["one_norm_contraction"] < 1),
        ("infinity norm contraction", one_tail_1["infinity_norm_contraction"] < 1),
        ("order one tail valid", one_tail_1["regular_matrix_error_actual"] <= one_tail_1["regular_matrix_error_upper"]),
        ("order three tail valid", one_tail_3["regular_matrix_error_actual"] <= one_tail_3["regular_matrix_error_upper"]),
        ("higher order actual shrinks", one_tail_3["regular_matrix_error_actual"] < one_tail_1["regular_matrix_error_actual"]),
        ("higher order bound shrinks", one_tail_3["regular_matrix_error_upper"] < one_tail_1["regular_matrix_error_upper"]),
        ("flavor covariance", flavor_covariant(["5/4"], [1], (1, 0), 256)),
        ("demo flavor covariance", output["flavor_swap_intertwines_regular_pullback"] is True),
        ("one mode q00 connected", one_sign["components"] == 1),
        ("one mode q00 gauge", one_sign["stoquastic_diagonal_sign_gauge_exists"] is True),
        ("one mode q10 connected", one_sign_10["components"] == 1),
        ("one mode q10 gauge", one_sign_10["stoquastic_diagonal_sign_gauge_exists"] is True),
        ("two mode q00 connected", two_sign["components"] == 1),
        ("two mode q00 frustrated", two_sign["stoquastic_diagonal_sign_gauge_exists"] is False),
        ("two mode q10 connected", two_sign_10["components"] == 1),
        ("two mode q10 frustrated", two_sign_10["stoquastic_diagonal_sign_gauge_exists"] is False),
        ("q00 cycle length six", len(two_sign["cycle"]) == 6),
        ("q10 cycle length six", len(two_sign_10["cycle"]) == 6),
        ("q00 cycle sign obstruction", two_sign["cycle_sign_product"] == -1 and two_sign["stoquastic_required_sign_product"] == 1),
        ("q10 cycle sign obstruction", two_sign_10["cycle_sign_product"] == -1 and two_sign_10["stoquastic_required_sign_product"] == 1),
        ("demo cycle labels exact", output["frustrated_cycle_states"] == cycle_labels),
        ("demo finite only", output["continuum_R256_identified"] is False),
        ("demo count open", output["native_ground_count_certified"] is False),
        ("demo PF route closed", output["standard_occupation_basis_Perron_Frobenius_route_available"] is False),
        ("reject nonpositive energy", rejects(lambda: regular_pullback([0], [1], (0, 0), 256))),
        ("reject nonpositive shift", rejects(lambda: regular_pullback([1], [1], (0, 0), 0))),
        ("reject incompatible data", rejects(lambda: regular_pullback([1, 2], [1], (0, 0), 256))),
        ("reject negative word order", rejects(lambda: neumann_regular_tail_bound(one, -1))),
        ("artifact exact identity", "R_N=U_N^(-*) H_N U_N^-1" in text),
        ("artifact finite/native fence", "A finite exact matrix is neither the common-carrier K139" in text),
        ("artifact cycle parity", "Their product is `-1`, while (11)" in text),
        ("artifact no degeneracy overclaim", "does **not** prove a degenerate finite or" in text),
        ("artifact next route", "invariant non-diagonal positivity cone" in text),
        ("artifact source fence", "not selected by Weinstein's source or a GU action" in text),
    ]


def selftest(data: dict) -> int:
    updates = (
        ("native R256", lambda d: d["finite_regular_pullback"].__setitem__("coefficient_complete_native_R256_identified", True)),
        ("erase adjoint", lambda d: d["finite_regular_pullback"].__setitem__("boundary_halves_are_separated_as_C_and_Cstar", False)),
        ("erase pullback", lambda d: d["finite_regular_pullback"].__setitem__("pullback_identity_exact", False)),
        ("invent source counterterm", lambda d: d["finite_regular_pullback"].__setitem__("finite_counterterm_is_supplied_not_source_selected", False)),
        ("erase one norm", lambda d: d["finite_neumann_certificate"].__setitem__("requires_one_norm_contraction", False)),
        ("erase infinity norm", lambda d: d["finite_neumann_certificate"].__setitem__("requires_infinity_norm_contraction", False)),
        ("invent graph tail", lambda d: d["finite_neumann_certificate"].__setitem__("finite_matrix_tail_is_common_carrier_graph_tail", True)),
        ("invent K139 reproof", lambda d: d["finite_neumann_certificate"].__setitem__("K139_graph_relative_limit_reproved", True)),
        ("erase exact check", lambda d: d["finite_neumann_certificate"].__setitem__("exact_error_is_checked_against_bound", False)),
        ("erase flavor", lambda d: d["charge_and_count_discriminator"].__setitem__("signed_flavor_swap_intertwines_R_q10_and_R_q01", False)),
        ("invent q00 gauge", lambda d: d["charge_and_count_discriminator"].__setitem__("two_mode_q00_admits_diagonal_sign_stoquastic_gauge", True)),
        ("invent q10 gauge", lambda d: d["charge_and_count_discriminator"].__setitem__("two_mode_q10_admits_diagonal_sign_stoquastic_gauge", True)),
        ("invent PF count", lambda d: d["charge_and_count_discriminator"].__setitem__("standard_occupation_basis_Perron_Frobenius_route_certifies_native_ground_count", True)),
        ("exclude all cones", lambda d: d["charge_and_count_discriminator"].__setitem__("another_non_diagonal_positivity_cone_excluded", True)),
        ("invent finite degeneracy", lambda d: d["charge_and_count_discriminator"].__setitem__("finite_ground_degeneracy_proved", True)),
        ("invent continuum degeneracy", lambda d: d["charge_and_count_discriminator"].__setitem__("native_continuum_ground_degeneracy_proved", True)),
        ("invent count", lambda d: d["charge_and_count_discriminator"].__setitem__("native_ground_count_or_exterior_floor_certified", True)),
        ("change cycle length", lambda d: d["charge_and_count_discriminator"].__setitem__("q00_obstruction_cycle_length", 4)),
        ("change cycle signs", lambda d: d["charge_and_count_discriminator"].__setitem__("q00_obstruction_cycle_edge_signs", [1] * 6)),
        ("invent native limit", lambda d: d["boundaries"].__setitem__("native_coefficientwise_R256_limit_serialized", True)),
        ("invent residual", lambda d: d["boundaries"].__setitem__("native_total_residual_closing_bound_serialized", True)),
        ("invent gap", lambda d: d["boundaries"].__setitem__("native_next_distinct_spectrum_lower_bound_serialized", True)),
        ("invent interval", lambda d: d["boundaries"].__setitem__("native_energy_interval_emitted", True)),
        ("invent scattering", lambda d: d["boundaries"].__setitem__("native_full_Fock_Mourre_or_scattering", True)),
        ("invent source", lambda d: d["boundaries"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent Born", lambda d: d["boundaries"].__setitem__("Born_rule_derived", True)),
        ("score heldout", lambda d: d["boundaries"].__setitem__("held_out_scored", True)),
        ("invent prediction", lambda d: d["boundaries"].__setitem__("prediction_or_confirmation_credit", True)),
        ("promote canon", lambda d: d["boundaries"].__setitem__("canon_verdict_change", "changed")),
        ("erase ceiling", lambda d: d.__setitem__("claim_ceiling", "The unique GU Hamiltonian has a simple ground state.")),
    )
    results = []
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught = bool(manifest_failures(mutant))
        print(f"[{'PASS' if caught else 'FAIL'}] hostile mutation {name}")
        results.append(caught)
    print(f"HOSTILE SELFTEST: {sum(map(int, results))}/{len(results)} caught")
    return 0 if all(results) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    text = ARTIFACT.read_text(encoding="utf-8")
    results = checks(data, text)
    for name, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"K155 EXACT CONTROL: {sum(int(ok) for _, ok in results)}/{len(results)} pass")
    if not all(ok for _, ok in results):
        return 1
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
