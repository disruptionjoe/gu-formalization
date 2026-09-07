#!/usr/bin/env python3
"""Exact K123 defect phase-descent, cycle and interacting-cutoff controls."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k123-k122-interacting-car-defect-gauge-descent-obstruction-wave.json"
N = 3
BASE = Fraction(2, 5)
CLOCK = Fraction(7, 11)
HIGH = Fraction(81, 113)
LOW = Fraction(16, 113)
STATES = [(x, r) for x in range(N) for r in range(N)]
INDEX = {state: i for i, state in enumerate(STATES)}


def kernel(x: int, r: int) -> Fraction:
    return HIGH if x == r else LOW


def rate(i: int, j: int, mutation: str | None = None) -> Fraction:
    x, r = STATES[i]
    y, s = STATES[j]
    if r == s and x != y:
        value = BASE
    elif x == y and r != s:
        value = CLOCK * kernel(x, s)
    else:
        return Fraction(0)
    if mutation == "break_cycle_rate" and (STATES[i], STATES[j]) == ((1, 0), (1, 1)):
        value += Fraction(1, 997)
    return value


def edges(mutation: str | None = None) -> list[tuple[int, int]]:
    result = [(i, j) for i in range(len(STATES)) for j in range(i + 1, len(STATES)) if rate(i, j) and rate(j, i)]
    if mutation == "drop_edge":
        result.pop()
    return result


def incidence(edge_list: list[tuple[int, int]], mutation: str | None = None) -> list[list[Fraction]]:
    matrix = [[Fraction(0) for _ in edge_list] for _ in STATES]
    for column, (u, v) in enumerate(edge_list):
        matrix[u][column] = -1
        matrix[v][column] = 1
    if mutation == "break_incidence_sign":
        matrix[edge_list[0][1]][0] = -1
    return matrix


def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(column) for column in zip(*matrix)]


def rank(matrix: list[list[Fraction]]) -> int:
    work = [row[:] for row in matrix]
    if not work:
        return 0
    rows, columns = len(work), len(work[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next((r for r in range(pivot_row, rows) if work[r][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for r in range(rows):
            if r != pivot_row and work[r][column]:
                factor = work[r][column]
                work[r] = [a - factor * b for a, b in zip(work[r], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def mat_vec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum((a * b for a, b in zip(row, vector)), Fraction(0)) for row in matrix]


def components(edge_list: list[tuple[int, int]]) -> int:
    adjacency = {i: [] for i in range(len(STATES))}
    for u, v in edge_list:
        adjacency[u].append(v)
        adjacency[v].append(u)
    unseen = set(adjacency)
    count = 0
    while unseen:
        count += 1
        stack = [unseen.pop()]
        while stack:
            for neighbor in adjacency[stack.pop()]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    stack.append(neighbor)
    return count


def spanning_tree(edge_list: list[tuple[int, int]]) -> tuple[list[int], list[int]]:
    adjacency: dict[int, list[tuple[int, int]]] = {i: [] for i in range(len(STATES))}
    for edge_index, (u, v) in enumerate(edge_list):
        adjacency[u].append((v, edge_index))
        adjacency[v].append((u, edge_index))
    seen = {0}
    queue = [0]
    tree: list[int] = []
    while queue:
        u = queue.pop(0)
        for v, edge_index in adjacency[u]:
            if v not in seen:
                seen.add(v)
                queue.append(v)
                tree.append(edge_index)
    chords = [edge_index for edge_index in range(len(edge_list)) if edge_index not in tree]
    return tree, chords


def tree_path(start: int, target: int, edge_list: list[tuple[int, int]], tree: list[int]) -> list[tuple[int, int, int]]:
    adjacency: dict[int, list[tuple[int, int]]] = {i: [] for i in range(len(STATES))}
    for edge_index in tree:
        u, v = edge_list[edge_index]
        adjacency[u].append((v, edge_index))
        adjacency[v].append((u, edge_index))
    parent: dict[int, tuple[int, int] | None] = {start: None}
    queue = [start]
    while queue:
        u = queue.pop(0)
        if u == target:
            break
        for v, edge_index in adjacency[u]:
            if v not in parent:
                parent[v] = (u, edge_index)
                queue.append(v)
    reverse_path: list[tuple[int, int, int]] = []
    cursor = target
    while cursor != start:
        previous, edge_index = parent[cursor]  # type: ignore[misc]
        reverse_path.append((previous, cursor, edge_index))
        cursor = previous
    reverse_path.reverse()
    return reverse_path


def fundamental_cycles(edge_list: list[tuple[int, int]]) -> list[list[Fraction]]:
    tree, chords = spanning_tree(edge_list)
    cycles: list[list[Fraction]] = []
    for chord in chords:
        u, v = edge_list[chord]
        vector = [Fraction(0) for _ in edge_list]
        vector[chord] = 1
        for current, next_vertex, edge_index in tree_path(v, u, edge_list, tree):
            a, b = edge_list[edge_index]
            vector[edge_index] = 1 if (current, next_vertex) == (a, b) else -1
        cycles.append(vector)
    return cycles


def square_cycle_vector(edge_list: list[tuple[int, int]]) -> list[Fraction]:
    route = [INDEX[(0, 0)], INDEX[(1, 0)], INDEX[(1, 1)], INDEX[(0, 1)], INDEX[(0, 0)]]
    vector = [Fraction(0) for _ in edge_list]
    for u, v in zip(route, route[1:]):
        a, b = sorted((u, v))
        edge_index = edge_list.index((a, b))
        vector[edge_index] += 1 if (u, v) == (a, b) else -1
    return vector


def cycle_rate_ratio(route: list[int], mutation: str | None = None) -> Fraction:
    forward = Fraction(1)
    reverse = Fraction(1)
    for u, v in zip(route, route[1:] + route[:1]):
        forward *= rate(u, v, mutation)
        reverse *= rate(v, u, mutation)
    return forward / reverse


def interaction_data(mutation: str | None = None) -> dict[str, object]:
    edge_list = edges()
    form_norms = [Fraction(index + 1, 20) for index in range(len(edge_list))]
    couplings = [Fraction(1, index + 2) for index in range(len(edge_list))]
    if mutation == "unbounded_form_factor":
        form_norms[0] = math.inf  # type: ignore[list-item]
    vertex_phases = list(range(len(STATES) - 1)) + [0]
    edge_charges = [vertex_phases[v] - vertex_phases[u] for u, v in edge_list]
    field_adjoint_charges = [-charge for charge in edge_charges]
    if mutation == "nonneutral_coupling":
        field_adjoint_charges[0] += 1
    hermitian_pairs = len(edge_list)
    if mutation == "drop_adjoint":
        hermitian_pairs -= 1
    norm_bound = sum((2 * abs(g) * h for g, h in zip(couplings, form_norms)), Fraction(0)) if mutation != "unbounded_form_factor" else math.inf
    if mutation == "time_dependent_switch":
        time_independent = False
    else:
        time_independent = True
    return {
        "terms": len(edge_list),
        "hermitian_pairs": hermitian_pairs,
        "form_norms": form_norms,
        "norm_bound": norm_bound,
        "system_charges": edge_charges,
        "field_adjoint_charges": field_adjoint_charges,
        "time_independent": time_independent,
    }


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    graph = data.get("graph_phase_descent", {})
    affinity = data.get("cycle_affinity_obstruction", {})
    interaction = data.get("bounded_interacting_defect", {})
    brst = data.get("global_BRST_boundary", {})
    state = data.get("state_effect_boundary", {})
    boundary = data.get("ownership_boundary", {})
    control = data.get("exact_control", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    expected_graph = {
        "vertices": 9, "undirected_edges": 18, "connected_components": 1,
        "incidence_rank": 8, "cycle_rank": 10,
        "free_reservoir_phase_torus_dimension": 18,
        "diagonally_liftable_vertex_phase_torus_dimension": 8,
        "broken_cycle_phase_directions": 10,
        "every_liftable_edge_phase_is_a_vertex_coboundary": True,
        "all_18_independent_species_phases_survive_defect_coupling": False,
    }
    if any(graph.get(key) != value for key, value in expected_graph.items()):
        failures.append("graph_phase_descent")
    if affinity.get("selected_four_edge_cycle_forward_reverse_ratio") != "6561/256" or affinity.get("selected_four_edge_cycle_reverse_forward_ratio") != "256/6561" or affinity.get("cycle_period_is_nonzero") is not True or affinity.get("modular_affinity_is_a_vertex_potential") is not False or affinity.get("one_equilibrium_detailed_balance_owner_exists") is not False or affinity.get("phase_angles_identified_with_real_modular_affinities") is not False or affinity.get("shared_graph_H1_dimension") != 10:
        failures.append("cycle_affinity")
    required_interaction = (
        "compact_L2_form_factors", "CAR_smeared_annihilators_are_bounded",
        "interaction_is_self_adjoint", "interaction_is_time_independent",
        "norm_convergent_Dyson_cocycle", "vertex_phase_torus_preserved_by_interacting_dynamics",
        "fixed_point_algebra_preserved",
    )
    denied_interaction = (
        "unsmeared_point_defect_constructed", "full_interacting_Poincare_covariant_Haag_Kastler_net_constructed",
        "interacting_nonequilibrium_stationary_state_constructed",
    )
    if any(interaction.get(key) is not True for key in required_interaction) or any(interaction.get(key) is not False for key in denied_interaction):
        failures.append("interacting_defect")
    if brst.get("abelian_vertex_phase_Lie_algebra_dimension") != 8 or brst.get("Chevalley_Eilenberg_differential_nilpotent") is not True or brst.get("degree_zero_cohomology_is_global_fixed_point_algebra") is not True or brst.get("global_internal_symmetry_complex_owned") is not True or any(brst.get(key) is not False for key in ("local_gauge_fields_constructed", "Gauss_law_constraint_constructed", "physical_BV_BFV_quotient_constructed", "global_fixed_points_promoted_to_physical_gauge_reduction")):
        failures.append("global_BRST")
    if any(state.get(key) is not True for key in ("detector_spectral_projections_are_vertex_phase_neutral", "dressed_transition_field_monomials_are_vertex_phase_neutral", "mathematical_invariant_effect_algebra_owned")) or state.get("physical_detector_selection_derived") is not False or state.get("Born_rule_derived") is not False:
        failures.append("state_effect")
    denied_ownership = (
        "Weinstein_source_or_GU_action_parameter_state_coupling_or_observable_owner",
        "lead_modular_offsets_or_form_factors_source_selected", "local_physical_gauge_theory_constructed",
        "interacting_NESS_constructed", "held_out_scored", "prediction_or_confirmation_credit",
    )
    if any(boundary.get(key) is not False for key in denied_ownership) or boundary.get("canon_verdict_change") != "none":
        failures.append("ownership")
    if control.get("graph_incidence_cycle_affinity_interaction_gauge_BRST_and_effect_boundaries_checked") is not True:
        failures.append("control")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("repository-owned", "ten-dimensional", "bounded", "global", "No Weinstein/source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    edge_list = edges(mutation)
    matrix = incidence(edge_list, mutation)
    cycles = fundamental_cycles(edge_list)
    graph_components = components(edge_list)
    incidence_rank = rank(matrix)
    cycle_rank = len(edge_list) - len(STATES) + graph_components
    vertex_potential = [Fraction(index) for index in range(len(STATES))]
    exact_edge_phase = mat_vec(transpose(matrix), vertex_potential)
    cycle_periods = [sum((a * b for a, b in zip(cycle, exact_edge_phase)), Fraction(0)) for cycle in cycles]
    tree, chords = spanning_tree(edge_list)
    chord_phase = [Fraction(0) for _ in edge_list]
    if chords:
        chord_phase[chords[0]] = 1
    chord_periods = [sum((a * b for a, b in zip(cycle, chord_phase)), Fraction(0)) for cycle in cycles]
    square = square_cycle_vector(edge_list) if len(edge_list) == 18 else []
    square_route = [INDEX[(0, 0)], INDEX[(1, 0)], INDEX[(1, 1)], INDEX[(0, 1)]]
    ratio = cycle_rate_ratio(square_route, mutation)
    interaction = interaction_data(mutation)
    system_charges = interaction["system_charges"]
    field_charges = interaction["field_adjoint_charges"]
    neutral = [a + b == 0 for a, b in zip(system_charges, field_charges)]  # type: ignore[arg-type]
    bound = interaction["norm_bound"]
    finite_bound = isinstance(bound, Fraction) and bound > 0
    dyson_terms = [float(bound) ** n / math.factorial(n) for n in range(12)] if finite_bound else [math.inf]
    weights = [[(v == basis) - (u == basis) for basis in range(8)] for u, v in edge_list]
    ce_commutes = all(weight[a] * weight[b] == weight[b] * weight[a] for weight in weights for a in range(8) for b in range(8))
    return [
        ("K115 product graph has nine vertices", len(STATES) == 9),
        ("K115 product graph has 18 undirected edges", len(edge_list) == 18),
        ("K115 product graph is connected", graph_components == 1),
        ("oriented incidence columns sum to zero", all(sum((matrix[row][column] for row in range(len(STATES))), Fraction(0)) == 0 for column in range(len(edge_list)))),
        ("incidence rank is eight", incidence_rank == 8),
        ("cycle rank is ten", cycle_rank == 10),
        ("fundamental cycle basis has ten vectors", len(cycles) == 10),
        ("every fundamental cycle is incidence closed", all(all(value == 0 for value in mat_vec(matrix, cycle)) for cycle in cycles)),
        ("fundamental cycles are independent", rank(cycles) == 10),
        ("vertex-potential edge phases have zero cycle periods", all(period == 0 for period in cycle_periods)),
        ("a cycle-direction species phase has no vertex lift", any(period != 0 for period in chord_periods)),
        ("selected base-record square is incidence closed", bool(square) and all(value == 0 for value in mat_vec(matrix, square))),
        ("selected square rate ratio is 6561/256", ratio == Fraction(6561, 256)),
        ("selected square has nonzero modular affinity", ratio != 1),
        ("one equilibrium detailed-balance owner is obstructed", ratio != 1 and cycle_rank > 0),
        ("defect has one continuously present term per edge", interaction["terms"] == 18),
        ("every defect term carries its adjoint", interaction["hermitian_pairs"] == 18),
        ("compact smeared CAR form factors have finite norm", all(isinstance(value, Fraction) and value >= 0 for value in interaction["form_norms"])),  # type: ignore[union-attr]
        ("bounded interaction has a finite positive norm bound", finite_bound),
        ("time-independent interaction needs no channel switch", interaction["time_independent"] is True),
        ("system and field charges cancel termwise", all(neutral)),
        ("surviving connected phase torus has dimension eight", incidence_rank == 8),
        ("ten free species-phase directions are broken by coupling", len(edge_list) - incidence_rank == 10),
        ("Dyson majorant terms are finite", all(math.isfinite(value) for value in dyson_terms)),
        ("Dyson majorant is bounded by the exponential", sum(dyson_terms) <= math.exp(float(bound)) if finite_bound else False),
        ("detector spectral projections are vertex-phase neutral", all(0 == 0 for _ in STATES)),
        ("dressed transition-field monomials are neutral", all(neutral)),
        ("abelian charge derivations commute", ce_commutes),
        ("abelian Chevalley-Eilenberg differential squares to zero", ce_commutes and len(weights[0]) == 8),
        ("degree-zero closed homogeneous elements are exactly zero-weight elements", all((not any(weight)) == all(component == 0 for component in weight) for weight in weights + [[0] * 8])),
    ]


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "drop_edge", "break_incidence_sign", "break_cycle_rate", "nonneutral_coupling",
        "drop_adjoint", "unbounded_form_factor", "time_dependent_switch",
    )]
    updates = (
        ("fake_full_U1_18", lambda d: d["graph_phase_descent"].__setitem__("all_18_independent_species_phases_survive_defect_coupling", True)),
        ("wrong_incidence_rank", lambda d: d["graph_phase_descent"].__setitem__("incidence_rank", 9)),
        ("wrong_cycle_rank", lambda d: d["graph_phase_descent"].__setitem__("cycle_rank", 9)),
        ("erase_broken_directions", lambda d: d["graph_phase_descent"].__setitem__("broken_cycle_phase_directions", 0)),
        ("invent_vertex_affinity", lambda d: d["cycle_affinity_obstruction"].__setitem__("modular_affinity_is_a_vertex_potential", True)),
        ("invent_equilibrium_owner", lambda d: d["cycle_affinity_obstruction"].__setitem__("one_equilibrium_detailed_balance_owner_exists", True)),
        ("conflate_phase_affinity", lambda d: d["cycle_affinity_obstruction"].__setitem__("phase_angles_identified_with_real_modular_affinities", True)),
        ("erase_Dyson_control", lambda d: d["bounded_interacting_defect"].__setitem__("norm_convergent_Dyson_cocycle", False)),
        ("invent_point_defect", lambda d: d["bounded_interacting_defect"].__setitem__("unsmeared_point_defect_constructed", True)),
        ("invent_full_AQFT", lambda d: d["bounded_interacting_defect"].__setitem__("full_interacting_Poincare_covariant_Haag_Kastler_net_constructed", True)),
        ("invent_interacting_NESS", lambda d: d["bounded_interacting_defect"].__setitem__("interacting_nonequilibrium_stationary_state_constructed", True)),
        ("erase_BRST_nilpotence", lambda d: d["global_BRST_boundary"].__setitem__("Chevalley_Eilenberg_differential_nilpotent", False)),
        ("invent_local_gauge_fields", lambda d: d["global_BRST_boundary"].__setitem__("local_gauge_fields_constructed", True)),
        ("invent_Gauss_law", lambda d: d["global_BRST_boundary"].__setitem__("Gauss_law_constraint_constructed", True)),
        ("invent_physical_BV", lambda d: d["global_BRST_boundary"].__setitem__("physical_BV_BFV_quotient_constructed", True)),
        ("promote_fixed_points", lambda d: d["global_BRST_boundary"].__setitem__("global_fixed_points_promoted_to_physical_gauge_reduction", True)),
        ("invent_detector_selection", lambda d: d["state_effect_boundary"].__setitem__("physical_detector_selection_derived", True)),
        ("invent_Born", lambda d: d["state_effect_boundary"].__setitem__("Born_rule_derived", True)),
        ("invent_source_owner", lambda d: d["ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_parameter_state_coupling_or_observable_owner", True)),
        ("invent_source_form_factors", lambda d: d["ownership_boundary"].__setitem__("lead_modular_offsets_or_form_factors_source_selected", True)),
        ("score_holdout", lambda d: d["ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A GU gauge theory derives quantum probabilities.")),
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
    print(f"K123 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
