#!/usr/bin/env python3
"""Exact controls for the K98 reversible-jump fixed-point theorem."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k98-observed-detailed-balance-fixed-point-algebra-wave.json"
N = 3
KAPPA = F(3, 5)
WEIGHTS = (F(4, 7), F(2, 7), F(1, 7))
Matrix = tuple[tuple[F, ...], ...]
Partition = tuple[tuple[int, ...], ...]
PARTITIONS: tuple[Partition, ...] = (
    ((0, 1, 2),),
    ((0,), (1, 2)),
    ((1,), (0, 2)),
    ((2,), (0, 1)),
    ((0,), (1,), (2,)),
)


def zero(n: int = N) -> Matrix:
    return tuple(tuple(F(0) for _ in range(n)) for _ in range(n))


def identity(n: int = N) -> Matrix:
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))


def basis(i: int, j: int, n: int = N) -> Matrix:
    return tuple(tuple(F(row == i and col == j) for col in range(n)) for row in range(n))


def diagonal(values: tuple[F, ...]) -> Matrix:
    return tuple(
        tuple(values[i] if i == j else F(0) for j in range(len(values)))
        for i in range(len(values))
    )


def add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] + b[i][j] for j in range(len(a))) for i in range(len(a)))


def scale(c: F, a: Matrix) -> Matrix:
    return tuple(tuple(c * entry for entry in row) for row in a)


def mul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(n)), F(0)) for j in range(n))
        for i in range(n)
    )


def adjoint(a: Matrix) -> Matrix:
    return tuple(tuple(a[j][i] for j in range(len(a))) for i in range(len(a)))


def trace(a: Matrix) -> F:
    return sum((a[i][i] for i in range(len(a))), F(0))


def phi(a: Matrix, weights: tuple[F, ...] = WEIGHTS) -> F:
    return sum((weights[i] * a[i][i] for i in range(len(weights))), F(0))


def gns_inner(a: Matrix, b: Matrix, weights: tuple[F, ...] = WEIGHTS) -> F:
    return phi(mul(adjoint(a), b), weights)


def block_of(i: int, partition: Partition) -> tuple[int, ...]:
    return next((block for block in partition if i in block), ())


def rates(partition: Partition, weights: tuple[F, ...] = WEIGHTS) -> tuple[tuple[F, ...], ...]:
    return tuple(
        tuple(weights[j] if i != j and block_of(i, partition) == block_of(j, partition) else F(0) for j in range(N))
        for i in range(N)
    )


def dephase(a: Matrix, kappa: F = KAPPA) -> Matrix:
    return tuple(
        tuple(F(0) if i == j else -kappa * a[i][j] for j in range(N))
        for i in range(N)
    )


def dissipator(
    a: Matrix,
    partition: Partition,
    weights: tuple[F, ...] = WEIGHTS,
    kappa: F = KAPPA,
    rate_override: tuple[tuple[F, ...], ...] | None = None,
) -> Matrix:
    """Heisenberg Lindblad generator with L_ij=sqrt(k_ij)|j><i|."""
    rate = rate_override or rates(partition, weights)
    out = [list(row) for row in dephase(a, kappa)]
    for i in range(N):
        for j in range(N):
            kij = rate[i][j]
            if not kij:
                continue
            # L_ij^* A L_ij contributes k_ij A_jj P_i.
            out[i][i] += kij * a[j][j]
            # -1/2 {L_ij^*L_ij,A} = -k_ij/2 {P_i,A}.
            for col in range(N):
                out[i][col] -= kij * a[i][col] / 2
            for row in range(N):
                out[row][i] -= kij * a[row][i] / 2
    return tuple(tuple(row) for row in out)


def partition_expect(a: Matrix, partition: Partition, weights: tuple[F, ...] = WEIGHTS) -> Matrix:
    out = [[F(0) for _ in range(N)] for _ in range(N)]
    for block in partition:
        block_weight = sum((weights[i] for i in block), F(0))
        mean = sum((weights[i] * a[i][i] for i in block), F(0)) / block_weight
        for i in block:
            out[i][i] = mean
    return tuple(tuple(row) for row in out)


def block_projection(block: tuple[int, ...]) -> Matrix:
    return diagonal(tuple(F(i in block) for i in range(N)))


def flatten(a: Matrix) -> tuple[F, ...]:
    return tuple(entry for row in a for entry in row)


def rank(columns: list[tuple[F, ...]]) -> int:
    if not columns:
        return 0
    rows = [list(row) for row in zip(*columns)]
    row_count = len(rows)
    col_count = len(rows[0])
    pivot_row = 0
    for col in range(col_count):
        pivot = next((row for row in range(pivot_row, row_count) if rows[row][col]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][col]
        rows[pivot_row] = [value / pivot_value for value in rows[pivot_row]]
        for row in range(row_count):
            if row != pivot_row and rows[row][col]:
                multiple = rows[row][col]
                rows[row] = [rows[row][k] - multiple * rows[pivot_row][k] for k in range(col_count)]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def fixed_dimension(
    partition: Partition,
    weights: tuple[F, ...] = WEIGHTS,
    kappa: F = KAPPA,
    rate_override: tuple[tuple[F, ...], ...] | None = None,
) -> int:
    columns = [
        flatten(dissipator(basis(i, j), partition, weights, kappa, rate_override))
        for i in range(N)
        for j in range(N)
    ]
    return N * N - rank(columns)


def detailed_balance_exact(partition: Partition, rate_override: tuple[tuple[F, ...], ...] | None = None) -> bool:
    rate = rate_override or rates(partition)
    edge_balance = all(WEIGHTS[i] * rate[i][j] == WEIGHTS[j] * rate[j][i] for i in range(N) for j in range(N))
    basis_units = [basis(i, j) for i in range(N) for j in range(N)]
    gns_symmetry = all(
        gns_inner(a, dissipator(b, partition, rate_override=rate))
        == gns_inner(dissipator(a, partition, rate_override=rate), b)
        for a in basis_units
        for b in basis_units
    )
    return edge_balance and gns_symmetry


def covariance_exact(partition: Partition) -> bool:
    """Exact Bohr-block check; no floating phases or sampled times."""
    for i in range(N):
        for j in range(N):
            image = dissipator(basis(i, j), partition)
            if i == j:
                if any(image[row][col] for row in range(N) for col in range(N) if row != col):
                    return False
            else:
                if any(image[row][col] for row in range(N) for col in range(N) if (row, col) != (i, j)):
                    return False
    return True


def limit_certificate(partition: Partition, weights: tuple[F, ...] = WEIGHTS) -> bool:
    """Certify the exact spectral projection and all decaying complements."""
    units = [basis(i, j) for i in range(N) for j in range(N)]
    projection_ok = all(
        partition_expect(partition_expect(unit, partition, weights), partition, weights)
        == partition_expect(unit, partition, weights)
        for unit in units
    )
    annihilation_ok = all(
        dissipator(partition_expect(unit, partition, weights), partition, weights) == zero()
        and partition_expect(dissipator(unit, partition, weights), partition, weights) == zero()
        for unit in units
    )
    diagonal_decay_ok = True
    for block in partition:
        block_weight = sum((weights[i] for i in block), F(0))
        for i in block:
            residual = add(basis(i, i), scale(F(-1), partition_expect(basis(i, i), partition, weights)))
            if dissipator(residual, partition, weights) != scale(-block_weight, residual):
                diagonal_decay_ok = False
    offdiagonal_decay_ok = True
    rate = rates(partition, weights)
    for i in range(N):
        q_i = sum(rate[i], F(0))
        for j in range(N):
            if i == j:
                continue
            q_j = sum(rate[j], F(0))
            expected = -(KAPPA + (q_i + q_j) / 2)
            if expected >= 0 or dissipator(basis(i, j), partition, weights) != scale(expected, basis(i, j)):
                offdiagonal_decay_ok = False
    return projection_ok and annihilation_ok and diagonal_decay_ok and offdiagonal_decay_ok


def positive_controls(mutation: str | None = None) -> list[tuple[str, bool]]:
    partitions = PARTITIONS[:-1] if mutation == "drop_partition" else PARTITIONS
    kappa = F(0) if mutation == "zero_kappa" else KAPPA
    return [
        ("the exact Gibbs weights are positive and normalized", all(weight > 0 for weight in WEIGHTS) and sum(WEIGHTS, F(0)) == 1),
        ("the Gibbs weights are pairwise distinct with ratios one half", len(set(WEIGHTS)) == 3 and WEIGHTS[1] / WEIGHTS[0] == F(1, 2) and WEIGHTS[2] / WEIGHTS[1] == F(1, 2)),
        ("the pure energy-dephasing rate is strictly positive", kappa > 0),
        ("all five partitions of three labels are enumerated", len(partitions) == 5 and len(set(partitions)) == 5),
        ("the three possible conductances are exactly 8/49, 4/49 and 2/49", {WEIGHTS[i] * WEIGHTS[j] for i in range(N) for j in range(i + 1, N)} == {F(8, 49), F(4, 49), F(2, 49)}),
    ]


def result_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    rate_override = None
    kappa = KAPPA
    expected_dimensions = [1, 2, 2, 2, 3]
    if mutation in {"break_balance", "remove_reverse_edge"}:
        mutable = [list(row) for row in rates(PARTITIONS[0])]
        if mutation == "break_balance":
            mutable[0][1] += F(1, 7)
        else:
            mutable[1][0] = F(0)
        rate_override = tuple(tuple(row) for row in mutable)
    if mutation == "zero_kappa":
        kappa = F(0)
    if mutation == "fake_connected_dimension":
        expected_dimensions[0] = 2
    if mutation == "fake_noedge_dimension":
        expected_dimensions[-1] = 1

    dimensions = [fixed_dimension(partition, kappa=kappa) for partition in PARTITIONS]
    balance_results = [
        detailed_balance_exact(partition, rate_override if index == 0 else None)
        for index, partition in enumerate(PARTITIONS)
    ]
    covariance_results = [covariance_exact(partition) for partition in PARTITIONS]
    limit_results = [limit_certificate(partition) for partition in PARTITIONS]
    if mutation == "wrong_limit":
        limit_results[1] = False
    if mutation == "break_covariance":
        covariance_results[2] = False

    no_edges = PARTITIONS[-1]
    noedge_without_dephasing = fixed_dimension(no_edges, kappa=F(0))
    fixed_projections = all(
        dissipator(block_projection(block), partition) == zero()
        for partition in PARTITIONS
        for block in partition
    )
    invariance = all(
        phi(dissipator(basis(i, j), partition)) == 0
        for partition in PARTITIONS
        for i in range(N)
        for j in range(N)
    )
    scalar_limit = partition_expect(basis(0, 0), PARTITIONS[0])
    noedge_limit = partition_expect(basis(0, 1), PARTITIONS[-1])
    coarse_limit = partition_expect(basis(1, 1), ((0,), (1, 2)))
    return [
        ("Gibbs detailed balance and full GNS symmetry hold for every partition", all(balance_results)),
        ("the Lindblad generator is unital and preserves the Gibbs state", all(dissipator(identity(), partition) == zero() for partition in PARTITIONS) and invariance),
        ("continuous energy-dynamics covariance holds by exact Bohr-block preservation", all(covariance_results)),
        ("every component projection is fixed", fixed_projections),
        ("fixed-space dimensions follow the component counts 1,2,2,2,3", dimensions == expected_dimensions),
        ("the connected census fixes only scalar multiples of identity", dimensions[0] == 1 and len(PARTITIONS[0]) == 1),
        ("the three intermediate censuses have two-dimensional coarse fixed algebras", dimensions[1:4] == [2, 2, 2]),
        ("the no-edge census fixes the full energy diagonal algebra", dimensions[-1] == N and len(PARTITIONS[-1]) == N),
        ("pure dephasing is load-bearing at no edges", fixed_dimension(no_edges) == N and noedge_without_dephasing == N * N),
        ("the exact semigroup spectral projection is the K97 E_pi for all five partitions", all(limit_results)),
        ("the connected limit sends P0 to Gibbs weight 4/7 times identity", scalar_limit == scale(F(4, 7), identity())),
        ("the no-edge limit kills energy off-diagonal units", noedge_limit == zero()),
        ("the 0|12 coarse limit sends P1 to two thirds on its block", coarse_limit == diagonal((F(0), F(2, 3), F(2, 3)))),
        ("same H rho and kappa admit all scalar coarse and diagonal fixed algebras", len(set(dimensions)) == 3 and dimensions == [1, 2, 2, 2, 3]),
        ("the delayed-choice holdout is not evaluated", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    family = data.get("reversible_jump_family", {})
    theorem = data.get("fixed_point_theorem", {})
    balance = data.get("detailed_balance_and_covariance", {})
    limit = data.get("semigroup_limit", {})
    census = data.get("exact_three_level_census", {})
    owners = data.get("owner_accounting", {})
    retrieval = data.get("retrieval_duplicate_boundary", {})
    fences = data.get("fences", {})
    holdout = data.get("holdout_firewall", {})
    failures: list[str] = []
    if family.get("kappa_positive") is not True or family.get("jump_operator") != "L_ij=sqrt(k_ij)|j><i|":
        failures.append("family")
    if family.get("pure_dephasing_load_bearing_for_isolated_components") is not True:
        failures.append("dephasing")
    if theorem.get("fixed_algebra") != "N_pi" or theorem.get("connected_graph_fixed_algebra") != "C I" or theorem.get("no_edge_fixed_algebra") != "D_H":
        failures.append("fixed_theorem")
    if theorem.get("all_QDB_semigroups_classified") is not False:
        failures.append("classification_scope")
    if balance.get("GNS_detailed_balance") is not True or balance.get("continuous_energy_covariance") is not True:
        failures.append("balance_covariance")
    if limit.get("limit") != "E_pi from K97" or limit.get("pointwise_norm_limit") is not True:
        failures.append("limit")
    if census.get("gibbs_weights") != ["4/7", "2/7", "1/7"] or census.get("partition_count") != 5:
        failures.append("census")
    if census.get("fixed_dimensions") != [1, 2, 2, 2, 3] or census.get("conductances") != ["8/49", "4/49", "2/49"]:
        failures.append("census_values")
    required_imports = {"Hamiltonian", "Gibbs_state", "pure_energy_dephasing", "graph", "energy_basis", "classical_record_interpretation", "Born_state_pairing"}
    if owners.get("source_selected_owner_count") != 0 or not required_imports.issubset(set(owners.get("imported", []))):
        failures.append("owners")
    if retrieval.get("nearby_controls_repeated_or_promoted") is not False:
        failures.append("retrieval")
    required_false = (
        "all_QDB_semigroups_classified",
        "Hamiltonian_derived",
        "Gibbs_principle_derived",
        "dephasing_or_graph_derived",
        "energy_basis_or_classicality_derived",
        "Born_rule_derived",
        "physical_record_selection_derived",
        "source_selected_dynamics_state_or_algebra",
        "continuum_AQFT_or_microlocal_state",
        "prediction_confirmation_or_verdict",
        "held_out_scored",
        "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if holdout.get("status") != "reserved_unscored" or holdout.get("scored_in_this_result") is not False:
        failures.append("holdout")
    ceiling = data.get("claim_ceiling", "")
    if "explicit finite-dimensional" not in ceiling or "no classification of all" not in ceiling:
        failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    baseline = [label for label, ok in positive_controls() + result_checks() if not ok] + manifest_failures(data)
    if baseline:
        print("BASELINE RED -- aborting mutations")
        for item in baseline:
            print(f"[FAIL] {item}")
        return 1

    mutations: list[tuple[str, bool]] = []
    for name in (
        "drop_partition",
        "zero_kappa",
        "break_balance",
        "remove_reverse_edge",
        "fake_connected_dimension",
        "fake_noedge_dimension",
        "wrong_limit",
        "break_covariance",
    ):
        checks = positive_controls(name) + result_checks(name)
        mutations.append((name, any(not ok for _, ok in checks)))

    updates = (
        ("drop_dephasing_owner", lambda d: d["reversible_jump_family"].__setitem__("pure_dephasing_load_bearing_for_isolated_components", False)),
        ("promote_all_QDB", lambda d: d["fixed_point_theorem"].__setitem__("all_QDB_semigroups_classified", True)),
        ("break_GNS", lambda d: d["detailed_balance_and_covariance"].__setitem__("GNS_detailed_balance", False)),
        ("wrong_semigroup_limit", lambda d: d["semigroup_limit"].__setitem__("limit", "identity")),
        ("wrong_census", lambda d: d["exact_three_level_census"].__setitem__("fixed_dimensions", [1, 1, 1, 1, 3])),
        ("source_owner_promotion", lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1)),
        ("drop_graph_import", lambda d: d["owner_accounting"]["imported"].remove("graph")),
        ("duplicate_promotion", lambda d: d["retrieval_duplicate_boundary"].__setitem__("nearby_controls_repeated_or_promoted", True)),
        ("derive_graph", lambda d: d["fences"].__setitem__("dephasing_or_graph_derived", True)),
        ("derive_classicality", lambda d: d["fences"].__setitem__("energy_basis_or_classicality_derived", True)),
        ("derive_Born", lambda d: d["fences"].__setitem__("Born_rule_derived", True)),
        ("physical_selection", lambda d: d["fences"].__setitem__("physical_record_selection_derived", True)),
        ("score_holdout", lambda d: d["fences"].__setitem__("held_out_scored", True)),
        ("open_holdout", lambda d: d["holdout_firewall"].__setitem__("status", "scored")),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        mutations.append((name, bool(manifest_failures(mutant))))

    for name, caught in mutations:
        print(f"[{'PASS' if caught else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(caught for _, caught in mutations)}/{len(mutations)} caught")
    return 0 if all(caught for _, caught in mutations) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    if "--selftest" in sys.argv:
        return selftest(data)
    checks = positive_controls()
    print("POSITIVE CONTROLS")
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    results = result_checks()
    results.append(("manifest preserves theorem, ownership, retrieval and promotion fences", not manifest_failures(data)))
    print("RESULT CHECKS")
    for label, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    all_checks = checks + results
    passed = sum(ok for _, ok in all_checks)
    print(f"K98 DETAILED BALANCE FIXED POINT ALGEBRA: {passed}/{len(all_checks)} pass")
    return 0 if passed == len(all_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
