#!/usr/bin/env python3
"""Exact/hostile checks for the K146 one-edge bidirectional BdG/IBC wave."""

from __future__ import annotations

import argparse
import copy
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k146-bidirectional-bdg-ibc-threshold-regularity-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k146-bidirectional-bdg-ibc-threshold-regularity-wave-2026-09-07.md"


def trapz(values: list[float], step: float) -> float:
    return step * (sum(values) - (values[0] + values[-1]) / 2)


def integral(fun, cutoff: float = 60.0, n: int = 120000) -> float:
    step = 2 * cutoff / n
    vals = [fun(-cutoff + j * step) for j in range(n + 1)]
    return trapz(vals, step) / (2 * math.pi)


def checks(data: dict, text: str) -> list[tuple[str, bool]]:
    eps = lambda p: math.sqrt(1 + p * p) + 0.25
    i2 = integral(lambda p: 1 / eps(p) ** 2)
    zeta = 1 / (1 + 2 * i2)
    gap_samples = [-1.1, -0.7, -0.2, 0.2, 0.7, 1.1]
    factors = [1 + 2 * integral(lambda p, z=z: 1 / (eps(p) ** 2 - z * z)) for z in gap_samples]
    nq = lambda q: max(1, min(abs(q), abs(q - 1)))
    b = data["bdg_ibc"]
    impl = data["implementability"]
    spec = data["fixed_charge_spectrum"]
    pauli = data["pauli_thresholds"]
    conj = data["physical_conjugate"]
    bounds = data["boundaries"]
    out = [
        ("schema", data["schema_version"] == "1.0"),
        ("classification", data["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", data["direction"] == "observed_to_native"),
        ("one edge", data["fixed_control"]["active_edges"] == 1),
        ("equal couplings", data["fixed_control"]["equal_real_couplings"] is True),
        ("not rook graph", data["fixed_control"]["complete_rook_graph"] is False),
        ("threshold", b["threshold"] == "5/4"),
        ("charge", b["conserved_charge"] == "q=n_d+N_plus-N_minus"),
        ("odd schur", b["schur_function"] == "F(z)=-z-[M(z)-M(-z)]"),
        ("positive gap factors", min(factors) > 1),
        ("zero simple", b["gap_point_spectrum"] == "{0}" and b["zero_mode_multiplicity"] == 1),
        ("no other gap", b["other_gap_eigenvalues"] is False),
        ("no embedded", b["embedded_eigenvalues"] is False),
        ("no sc", b["singular_continuous_spectrum"] is False),
        ("Z proper", 0 < zeta < 1),
        ("relative HS", impl["interacting_minus_free_negative_projection_is_Hilbert_Schmidt"] is True),
        ("relative implementable", impl["relative_Bogoliubov_transform_implementable"] is True),
        ("global flip not implementable", impl["global_hole_creation_annihilation_flip_implementable"] is False),
        ("nambu bookkeeping", impl["Nambu_notation_alone_changes_the_vacuum"] is False),
        ("q0 point", spec["point_spectrum_q0"] == "{E_B} simple"),
        ("q1 point", spec["point_spectrum_q1"] == "{E_B} simple"),
        ("other point empty", spec["point_spectrum_other_q"] == "empty"),
        ("q thresholds", [nq(q) for q in range(-3, 5)] == [3, 2, 1, 1, 1, 1, 2, 3]),
        ("q1 threshold", spec["q1_continuum_threshold"] == "E_B+5/4"),
        ("K144 fence", spec["K144_projected_levels_imported"] is False),
        ("four pauli charges", pauli["bound_residual_total_charges"] == [-1, 0, 1, 2]),
        ("even gamma", pauli["normalized_even_Gamma_tau"] == "[sqrt(Z)]"),
        ("branch gamma", pauli["two_branch_Gamma_tau"] == "[sqrt(Z/2),sqrt(Z/2)]"),
        ("D rank", pauli["D_tau"] == "[Z]" and pauli["rank"] == 1),
        ("odd kernel", pauli["odd_kinematic_kernel_dimension"] == 1),
        ("no dark impurity", pauli["dark_impurity_dimension"] == 0),
        ("vacuous compression", pauli["compressed_dark_denominator_dimension"] == 0),
        ("unit vacancy", pauli["continuum_Pauli_vacancy"] == 1),
        ("velocity", conj["velocity"] == "p/sqrt(1+p^2)"),
        ("nambu signs", conj["nambu_signs"] == [0, 1, -1]),
        ("commutator positive", conj["free_commutator"] == "diag(0,p^2/(1+p^2),p^2/(1+p^2))"),
        ("boundary commutators", conj["first_two_resolvent_dressed_boundary_commutators_in_L2"] is True),
        ("C11", conj["IBC_operator_C11"] is True and conj["implemented_quadratic_hamiltonian_C11"] is True),
        ("mourre", conj["strict_Mourre_away_from_zero_and_thresholds"] is True),
        ("lap", conj["weighted_LAP_s_greater_than_half"] is True),
        ("threshold nonuniform", conj["threshold_uniform_constant"] is False),
        ("rook nonuniform", conj["rook_cycle_uniformity"] is False),
        ("unequal fence", bounds["unequal_couplings_solved"] is False),
        ("offdiag W fence", bounds["off_diagonal_W_solved"] is False),
        ("cycle fence", bounds["two_edge_or_rook_cycle_extension_solved"] is False),
        ("scattering fence", bounds["many_body_asymptotic_completeness"] is False),
        ("NESS fence", bounds["NESS_or_current"] is False),
        ("source fence", bounds["Weinstein_source_or_GU_action_owner"] is False),
        ("Born fence", bounds["Born_rule_derived"] is False),
        ("prediction fence", bounds["prediction_or_confirmation_credit"] is False),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("scope global flip", "global hole-sea flip" in text),
        ("next two edge", "first two-edge" in text),
    ]
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    text = ARTIFACT.read_text()
    baseline = checks(data, text)
    failed = [name for name, ok in baseline if not ok]
    if failed:
        print(f"FAIL baseline: {failed}")
        return 1
    if not args.selftest:
        print(f"PASS {len(baseline)}/{len(baseline)} K146 exact controls")
        return 0
    mutations: list[tuple[str, callable]] = [
        ("global flip", lambda d: d["implementability"].__setitem__("global_hole_creation_annihilation_flip_implementable", True)),
        ("relative HS", lambda d: d["implementability"].__setitem__("interacting_minus_free_negative_projection_is_Hilbert_Schmidt", False)),
        ("zero multiplicity", lambda d: d["bdg_ibc"].__setitem__("zero_mode_multiplicity", 2)),
        ("q0 point", lambda d: d["fixed_charge_spectrum"].__setitem__("point_spectrum_q0", "empty")),
        ("q1 threshold", lambda d: d["fixed_charge_spectrum"].__setitem__("q1_continuum_threshold", "E_B+5/2")),
        ("pauli rank", lambda d: d["pauli_thresholds"].__setitem__("rank", 0)),
        ("dark", lambda d: d["pauli_thresholds"].__setitem__("dark_impurity_dimension", 1)),
        ("C11", lambda d: d["physical_conjugate"].__setitem__("IBC_operator_C11", False)),
        ("cycle", lambda d: d["boundaries"].__setitem__("two_edge_or_rook_cycle_extension_solved", True)),
        ("source", lambda d: d["boundaries"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
    ]
    caught = 0
    for _, mutate in mutations:
        trial = copy.deepcopy(data)
        mutate(trial)
        if any(not ok for _, ok in checks(trial, text)):
            caught += 1
    prose_mutations = [
        text.replace("GU-COMPARATOR-ROUTING", "ROUTING", 1),
        text.replace("Classification: INTERNAL_STRUCTURAL_ONLY.", "", 1),
        text.replace("```gu-typed-objects", "```text", 1),
        text.replace("global hole-sea flip", "global sea change"),
        text.replace("first two-edge", "later multi-edge", 1),
    ]
    for trial_text in prose_mutations:
        if any(not ok for _, ok in checks(data, trial_text)):
            caught += 1
    total = len(mutations) + len(prose_mutations)
    if caught != total:
        print(f"FAIL hostile selftest caught {caught}/{total}")
        return 1
    print(f"PASS hostile selftest caught {caught}/{total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
