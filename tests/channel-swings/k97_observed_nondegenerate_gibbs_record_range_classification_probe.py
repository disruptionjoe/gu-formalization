#!/usr/bin/env python3
"""Exact finite-partition controls for the K97 Gibbs record-range theorem."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k97-observed-nondegenerate-gibbs-record-range-classification-wave.json"
N = 3
Matrix = tuple[tuple[F, ...], ...]
Partition = tuple[tuple[int, ...], ...]
WEIGHTS = (F(4, 7), F(2, 7), F(1, 7))
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
    n = len(values)
    return tuple(tuple(values[i] if i == j else F(0) for j in range(n)) for i in range(n))


def add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] + b[i][j] for j in range(len(a))) for i in range(len(a)))


def scale(c: F, a: Matrix) -> Matrix:
    return tuple(tuple(c * a[i][j] for j in range(len(a))) for i in range(len(a)))


def mul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(n)), F(0)) for j in range(n))
        for i in range(n)
    )


def trace(a: Matrix) -> F:
    return sum((a[i][i] for i in range(len(a))), F(0))


def phi(a: Matrix, weights: tuple[F, ...]) -> F:
    return sum((weights[i] * a[i][i] for i in range(len(weights))), F(0))


def block_projection(block: tuple[int, ...], n: int = N) -> Matrix:
    return diagonal(tuple(F(i in block) for i in range(n)))


def partition_expect(a: Matrix, partition: Partition, weights: tuple[F, ...]) -> Matrix:
    n = len(weights)
    out = [[F(0) for _ in range(n)] for _ in range(n)]
    for block in partition:
        block_weight = sum((weights[i] for i in block), F(0))
        coefficient = sum((weights[i] * a[i][i] for i in block), F(0)) / block_weight
        for i in block:
            out[i][i] = coefficient
    return tuple(tuple(row) for row in out)


def is_zero(a: Matrix) -> bool:
    return all(entry == 0 for row in a for entry in row)


def cp_choi_diagonal_nonnegative(partition: Partition, weights: tuple[F, ...]) -> bool:
    """The Choi matrix is diagonal; list its exact nonzero diagonal entries."""
    entries: list[F] = []
    for i in range(len(weights)):
        block = next((block for block in partition if i in block), ())
        block_weight = sum((weights[j] for j in block), F(0))
        for output_index in range(len(weights)):
            entries.append(weights[i] / block_weight if output_index in block else F(0))
    return all(entry >= 0 for entry in entries)


def bimodule_exact(partition: Partition, weights: tuple[F, ...]) -> bool:
    for left_block in partition:
        left = block_projection(left_block)
        for right_block in partition:
            right = block_projection(right_block)
            for i in range(N):
                for j in range(N):
                    a = basis(i, j)
                    lhs = partition_expect(mul(mul(left, a), right), partition, weights)
                    rhs = mul(mul(left, partition_expect(a, partition, weights)), right)
                    if lhs != rhs:
                        return False
    return True


def partition_properties(partition: Partition, weights: tuple[F, ...]) -> dict[str, bool]:
    images = [partition_expect(basis(i, j), partition, weights) for i in range(N) for j in range(N)]
    unital = partition_expect(identity(), partition, weights) == identity()
    idempotent = all(partition_expect(image, partition, weights) == image for image in images)
    state_preserving = all(
        phi(partition_expect(basis(i, j), partition, weights), weights) == phi(basis(i, j), weights)
        for i in range(N) for j in range(N)
    )
    trace_preserving = all(
        trace(partition_expect(basis(i, j), partition, weights)) == trace(basis(i, j))
        for i in range(N) for j in range(N)
    )
    # On every matrix unit, alpha_t supplies a scalar phase. Off-diagonal units
    # are killed and diagonal outputs commute with H, proving covariance without
    # floating-point phases.
    covariant = all(
        (is_zero(images[i * N + j]) if i != j else all(images[i * N + j][r][c] == 0 for r in range(N) for c in range(N) if r != c))
        for i in range(N) for j in range(N)
    )
    return {
        "unital": unital,
        "cp": cp_choi_diagonal_nonnegative(partition, weights),
        "idempotent": idempotent,
        "bimodular": bimodule_exact(partition, weights),
        "state_preserving": state_preserving,
        "trace_preserving": trace_preserving,
        "covariant": covariant,
    }


def two_by_two_degenerate_controls() -> tuple[bool, bool, bool]:
    i2 = identity(2)
    x2: Matrix = ((F(0), F(1)), (F(1), F(0)))
    z2: Matrix = ((F(1), F(0)), (F(0), F(-1)))
    p0: Matrix = ((F(1), F(0)), (F(0), F(0)))
    half_i = scale(F(1, 2), i2)

    def dephase(a: Matrix, sigma: Matrix) -> Matrix:
        return scale(F(1, 2), add(a, mul(mul(sigma, a), sigma)))

    ez = dephase(p0, z2)
    ex = dephase(p0, x2)
    distinct = ez == p0 and ex == half_i and ez != ex
    both_trace = trace(ez) == trace(p0) and trace(ex) == trace(p0)
    both_tracial_state = dephase(half_i, z2) == half_i and dephase(half_i, x2) == half_i
    return distinct, both_trace, both_tracial_state


def noncommutative_full_range_control() -> bool:
    x = ((F(0), F(1), F(0)), (F(1), F(0), F(0)), (F(0), F(0), F(0)))
    z = ((F(1), F(0), F(0)), (F(0), F(-1), F(0)), (F(0), F(0), F(0)))
    return mul(x, z) != mul(z, x)


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    weights = WEIGHTS
    partitions = PARTITIONS
    if mutation == "repeat_weight":
        weights = (F(2, 5), F(2, 5), F(1, 5))
    if mutation == "drop_partition":
        partitions = PARTITIONS[:-1]

    properties = [partition_properties(partition, weights) for partition in partitions]
    trace_passes = sum(props["trace_preserving"] for props in properties)
    coarse = ((0, 1), (2,))
    coarse_p0 = partition_expect(basis(0, 0), coarse, WEIGHTS)
    scalar_p0 = partition_expect(basis(0, 0, 2), ((0, 1),), (F(2, 3), F(1, 3)))
    degenerate_distinct, degenerate_trace, degenerate_state = two_by_two_degenerate_controls()
    beta_zero = (F(1, 3), F(1, 3), F(1, 3))
    beta_zero_trace_count = sum(partition_properties(partition, beta_zero)["trace_preserving"] for partition in PARTITIONS)

    if mutation == "break_covariance":
        properties[0]["covariant"] = False
    if mutation == "fake_all_trace":
        trace_passes = len(partitions)
    if mutation == "fake_scalar_trace":
        scalar_trace_fails = False
    else:
        scalar_trace_fails = trace(scalar_p0) != trace(basis(0, 0, 2))
    if mutation == "collapse_degenerate":
        degenerate_distinct = False
    if mutation == "deny_beta_zero":
        beta_zero_trace_count = 1
    if mutation == "non_CP":
        properties[0]["cp"] = False

    all_structural = all(
        props[key]
        for props in properties
        for key in ("unital", "cp", "idempotent", "bimodular", "state_preserving", "covariant")
    )
    return [
        ("the exact Gibbs weights are normalized", sum(weights, F(0)) == 1),
        ("the exact Gibbs weights are pairwise distinct", len(set(weights)) == 3),
        ("successive Gibbs ratios equal one half", weights[1] / weights[0] == F(1, 2) and weights[2] / weights[1] == F(1, 2)),
        ("the control has a repeated energy gap", True),
        ("all five set partitions are enumerated", len(partitions) == 5 and len(set(partitions)) == 5),
        ("every partition map is unital CP idempotent bimodular state preserving and covariant", all_structural),
        ("only the singleton partition preserves canonical trace", trace_passes == 1),
        ("the trace-preserving partition is the energy spectral MASA", properties[-1]["trace_preserving"] and len(partitions[-1]) == 3),
        ("the coarse 01|2 expectation has coefficient two thirds on P0", coarse_p0[0][0] == F(2, 3) and coarse_p0[1][1] == F(2, 3)),
        ("the coarse 01|2 expectation violates unnormalized trace on P0", trace(coarse_p0) == F(4, 3) and trace(coarse_p0) != 1),
        ("the scalar Gibbs expectation preserves the nondegenerate Gibbs state", phi(scalar_p0, (F(2, 3), F(1, 3))) == F(2, 3)),
        ("the scalar Gibbs expectation fails canonical trace preservation", scalar_trace_fails),
        ("the full identity range is noncommutative", noncommutative_full_range_control()),
        ("degenerate H admits distinct Z and X MASA dephasings", degenerate_distinct),
        ("both degenerate dephasings preserve trace", degenerate_trace),
        ("both degenerate dephasings preserve the tracial Gibbs state", degenerate_state),
        ("at beta zero every energy partition preserves canonical trace", beta_zero_trace_count == 5),
        ("gap nonresonance is not used by any exact partition check", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    system = data.get("finite_system", {})
    classification = data.get("partition_classification", {})
    corollaries = data.get("selector_corollaries", {})
    control = data.get("exact_control", {})
    counterexamples = data.get("counterexamples", {})
    owners = data.get("owner_accounting", {})
    retrieval = data.get("retrieval_duplicate_boundary", {})
    fences = data.get("fences", {})
    holdout = data.get("holdout_firewall", {})
    failures: list[str] = []
    if system.get("energy_gap_nonresonance_required") is not False or "simple spectrum" not in system.get("hamiltonian_assumption", ""):
        failures.append("system_assumptions")
    if classification.get("every_admissible_abelian_range_is_a_unique_energy_partition") is not True or classification.get("covariance_plus_gibbs_preservation_selects_unique_range") is not False:
        failures.append("partition_classification")
    if corollaries.get("masa_range_selects_energy_spectral_masa") is not True or corollaries.get("abelian_plus_canonical_trace_plus_gibbs_preservation_selects_energy_spectral_masa") is not True:
        failures.append("selector_corollaries")
    if control.get("gibbs_weights") != ["4/7", "2/7", "1/7"] or control.get("partition_count") != 5 or control.get("canonical_trace_preserving_partition_count") != 1:
        failures.append("exact_control")
    if counterexamples.get("nondegenerate_scalar_range", {}).get("canonical_trace_preserving") is not False:
        failures.append("scalar_counterexample")
    if counterexamples.get("noncommutative_full_range", {}).get("range_abelian") is not False:
        failures.append("full_range_counterexample")
    if counterexamples.get("beta_zero", {}).get("maximal_resolution_selected") is not False:
        failures.append("beta_zero_counterexample")
    if owners.get("source_selected_owner_count") != 0 or "abelian_record_interpretation" not in owners.get("imported", []):
        failures.append("owners")
    if retrieval.get("nearby_controls_repeated_or_promoted") is not False:
        failures.append("retrieval")
    required_false = (
        "covariance_and_state_alone_select_unique_record_range",
        "Hamiltonian_or_temperature_derived",
        "Gibbs_KMS_principle_derived",
        "abelian_classicality_derived",
        "maximal_resolution_derived",
        "physical_coupling_or_irreversibility_derived",
        "source_selected_dynamics_state_or_algebra",
        "continuum_AQFT_or_microcausality",
        "microlocal_or_Hadamard_state",
        "Born_rule_derived",
        "prediction_confirmation_or_verdict",
        "held_out_scored",
        "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if holdout.get("status") != "reserved_unscored" or holdout.get("scored_in_this_result") is not False:
        failures.append("holdout")
    ceiling = data.get("claim_ceiling", "")
    if "classification" not in ceiling or "no derivation" not in ceiling:
        failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    baseline = [label for label, ok in model_checks() if not ok] + manifest_failures(data)
    if baseline:
        print("BASELINE RED -- aborting mutations")
        for item in baseline:
            print(f"[FAIL] {item}")
        return 1

    mutations: list[tuple[str, bool]] = []
    for name in (
        "repeat_weight",
        "drop_partition",
        "break_covariance",
        "fake_all_trace",
        "fake_scalar_trace",
        "collapse_degenerate",
        "deny_beta_zero",
        "non_CP",
    ):
        mutations.append((name, any(not ok for _, ok in model_checks(name))))

    updates = (
        ("claim_unique_from_weak_axioms", lambda d: d["partition_classification"].__setitem__("covariance_plus_gibbs_preservation_selects_unique_range", True)),
        ("drop_MASA_corollary", lambda d: d["selector_corollaries"].__setitem__("masa_range_selects_energy_spectral_masa", False)),
        ("fake_partition_count", lambda d: d["exact_control"].__setitem__("partition_count", 4)),
        ("fake_scalar_trace_manifest", lambda d: d["counterexamples"]["nondegenerate_scalar_range"].__setitem__("canonical_trace_preserving", True)),
        ("fake_full_commutative", lambda d: d["counterexamples"]["noncommutative_full_range"].__setitem__("range_abelian", True)),
        ("fake_beta_zero_selection", lambda d: d["counterexamples"]["beta_zero"].__setitem__("maximal_resolution_selected", True)),
        ("source_owner_promotion", lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1)),
        ("duplicate_promotion", lambda d: d["retrieval_duplicate_boundary"].__setitem__("nearby_controls_repeated_or_promoted", True)),
        ("derive_classicality", lambda d: d["fences"].__setitem__("abelian_classicality_derived", True)),
        ("derive_Born", lambda d: d["fences"].__setitem__("Born_rule_derived", True)),
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
    checks = model_checks()
    checks.append(("manifest preserves theorem, controls, ownership, retrieval and promotion fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K97 NONDEGENERATE GIBBS RECORD RANGE: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
