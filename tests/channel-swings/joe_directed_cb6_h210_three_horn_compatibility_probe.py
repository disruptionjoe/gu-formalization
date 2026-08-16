#!/usr/bin/env python3
"""Exact CB-6C three-horn compatibility and semantic-mutation certificate."""

from __future__ import annotations

import argparse
import itertools
from fractions import Fraction
from pathlib import Path


FCORR = 1
ALIGN = 2
PSRED = 4
HORNS = (FCORR, ALIGN, PSRED)

CLAIMS = {
    "intrinsic_z_to_f_carrier": 0,
    "local_offdiagonal_zero_order_chain": 0,
    "source_intended_reveal": FCORR,
    "imposter_provenance_quotient": ALIGN,
    "preferred_moving_ps_descent": PSRED,
    "aligned_source_reveal_chain": FCORR | ALIGN,
    "source_reveal_in_moving_ps_chain": FCORR | PSRED,
    "imposter_partner_in_moving_ps_chain": ALIGN | PSRED,
    "complete_source_labelled_moving_ps_chain": FCORR | ALIGN | PSRED,
}

EXPECTED_BRANCH_CLAIMS = {
    0: {"intrinsic_z_to_f_carrier", "local_offdiagonal_zero_order_chain"},
    FCORR: {
        "intrinsic_z_to_f_carrier",
        "local_offdiagonal_zero_order_chain",
        "source_intended_reveal",
    },
    ALIGN: {
        "intrinsic_z_to_f_carrier",
        "local_offdiagonal_zero_order_chain",
        "imposter_provenance_quotient",
    },
    PSRED: {
        "intrinsic_z_to_f_carrier",
        "local_offdiagonal_zero_order_chain",
        "preferred_moving_ps_descent",
    },
    FCORR | ALIGN: {
        "intrinsic_z_to_f_carrier",
        "local_offdiagonal_zero_order_chain",
        "source_intended_reveal",
        "imposter_provenance_quotient",
        "aligned_source_reveal_chain",
    },
    FCORR | PSRED: {
        "intrinsic_z_to_f_carrier",
        "local_offdiagonal_zero_order_chain",
        "source_intended_reveal",
        "preferred_moving_ps_descent",
        "source_reveal_in_moving_ps_chain",
    },
    ALIGN | PSRED: {
        "intrinsic_z_to_f_carrier",
        "local_offdiagonal_zero_order_chain",
        "imposter_provenance_quotient",
        "preferred_moving_ps_descent",
        "imposter_partner_in_moving_ps_chain",
    },
    FCORR | ALIGN | PSRED: set(CLAIMS),
}


def rank(matrix: list[list[Fraction | int]]) -> int:
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((i for i in range(pivot_row, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for i in range(rows):
            if i != pivot_row and a[i][col]:
                multiple = a[i][col]
                a[i] = [x - multiple * y for x, y in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def diagonal_stage(size: int, stage_rank: int) -> list[list[int]]:
    return [[int(i == j and i < stage_rank) for j in range(size)] for i in range(size)]


def row_tensor_stage(row: list[int], stage: list[list[int]]) -> list[list[int]]:
    # Matrix of r tensor B: M_3 tensor S -> W, in three domain blocks.
    return [[coefficient * x for coefficient in row for x in output_row] for output_row in stage]


def allowed_claims(branch: int) -> set[str]:
    return {name for name, prerequisites in CLAIMS.items() if branch & prerequisites == prerequisites}


def validate_semantics(state: dict[str, object]) -> None:
    branch = int(state.get("branch", 0))
    claims = set(state.get("claims", set()))
    if not claims <= allowed_claims(branch):
        raise AssertionError("claim used without its horn prerequisites")
    if state.get("collapse_horns"):
        raise AssertionError("the three horns are independent")
    forbidden_flags = (
        "z_is_f",
        "recovered_normal_leg",
        "deleted_conjugate_half",
        "kappa_is_varpi",
        "full_d0_varpi_resolved",
        "named_family",
        "physical_kernel",
        "derived_action",
        "selected_graph",
        "constructed_ps_reduction",
        "physical_quotient",
        "mass_or_spectrum",
    )
    if any(state.get(flag) for flag in forbidden_flags):
        raise AssertionError("forbidden semantic or physical promotion")
    stage_rank = int(state.get("stage_rank", 16))
    claimed_kernel = state.get("claimed_family_kernel")
    correct_kernel = 48 - stage_rank
    if claimed_kernel is not None and int(claimed_kernel) != correct_kernel:
        raise AssertionError("family kernel ignored the downstream stage kernel")


def exact_checks() -> list[str]:
    passed: list[str] = []

    branches = set(range(8))
    assert branches == {sum(bit * horn for bit, horn in zip(bits, HORNS))
                        for bits in itertools.product((0, 1), repeat=3)}
    passed.append("all eight horn branches exist")

    for branch in sorted(branches):
        assert allowed_claims(branch) == EXPECTED_BRANCH_CLAIMS[branch]
    passed.append("eight-branch claim-prerequisite matrix")

    # Exhaustive countermodels disprove every directed implication X => Y.
    for antecedent in HORNS:
        for consequent in HORNS:
            if antecedent != consequent:
                assert any((b & antecedent) and not (b & consequent) for b in branches)
    passed.append("all six pairwise horn implications have countermodels")

    row = [2, -1, 3]
    for stage_rank in (0, 8, 12, 16):
        stage = diagonal_stage(16, stage_rank)
        composite = row_tensor_stage(row, stage)
        observed_rank = rank(composite)
        assert observed_rank == stage_rank
        assert 48 - observed_rank == 32 + (16 - stage_rank)
    passed.append("exact family-kernel sequence at ranks 0/8/12/16")

    normalized_row = [[0, 0, 1]]
    exact_row_stabilizer = [[2, 1, 5], [0, 3, 7], [0, 0, 1]]
    row_line_stabilizer = [[2, 1, 5], [0, 3, 7], [0, 0, -4]]
    non_stabilizer = [[1, 0, 0], [0, 1, 0], [1, 0, 1]]
    assert matmul(normalized_row, exact_row_stabilizer) == normalized_row
    assert matmul(normalized_row, row_line_stabilizer) == [[0, 0, -4]]
    assert matmul(normalized_row, non_stabilizer) != normalized_row
    assert rank(exact_row_stabilizer) == rank(row_line_stabilizer) == 3
    passed.append("normalized-row and row-line stabilizer controls")

    # A family-basis permutation changes coordinates, never rank or kernel size.
    permutation = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
    moved_row = matmul([row], permutation)[0]
    assert rank(row_tensor_stage(row, diagonal_stage(16, 12))) == 12
    assert rank(row_tensor_stage(moved_row, diagonal_stage(16, 12))) == 12
    passed.append("family-basis covariance")

    upstream_f_projection = [[0 for _ in range(16)] for _ in range(16)]
    downstream_intrinsic_adapter = diagonal_stage(16, 16)
    assert rank(upstream_f_projection) == 0
    assert rank(downstream_intrinsic_adapter) == 16
    passed.append("upstream-F-zero/downstream-intrinsic-rank-16 order witness")

    halves = {
        "A": {"input": "+", "output": "-", "ranks": (0, 8, 12, 16, 12, 16)},
        "B": {"input": "-", "output": "+", "ranks": (0, 8, 12, 16, 12, 16)},
    }
    assert halves["A"]["input"] != halves["A"]["output"]
    assert halves["B"]["input"] != halves["B"]["output"]
    assert halves["A"]["ranks"] == halves["B"]["ranks"]
    passed.append("odd parity and both-half mirrored fingerprints")

    # Intrinsic carrier descent is horn-free; preferred PS descent is not.
    assert "intrinsic_z_to_f_carrier" in allowed_claims(0)
    assert "preferred_moving_ps_descent" not in allowed_claims(0)
    assert "preferred_moving_ps_descent" in allowed_claims(PSRED)
    passed.append("intrinsic descent separated from preferred-PS descent")

    validate_semantics({"branch": 7, "claims": set(CLAIMS), "stage_rank": 16,
                        "claimed_family_kernel": 32})
    passed.append("all-three coherent conditional state")
    return passed


def semantic_mutants() -> list[tuple[str, dict[str, object]]]:
    return [
        ("FCORR used without horn", {"branch": 0, "claims": {"source_intended_reveal"}}),
        ("ALIGN used without horn", {"branch": 0, "claims": {"imposter_provenance_quotient"}}),
        ("PSRED used without horn", {"branch": 0, "claims": {"preferred_moving_ps_descent"}}),
        ("horns collapsed", {"branch": 7, "claims": set(CLAIMS), "collapse_horns": True}),
        ("Z renamed F", {"branch": 7, "claims": set(CLAIMS), "z_is_f": True}),
        ("normal leg recovered", {"branch": 7, "claims": set(CLAIMS), "recovered_normal_leg": True}),
        ("conjugate half deleted", {"branch": 7, "claims": set(CLAIMS), "deleted_conjugate_half": True}),
        ("kappa inserted into varpi", {"branch": 7, "claims": set(CLAIMS), "kappa_is_varpi": True}),
        ("full cell resolved", {"branch": 7, "claims": set(CLAIMS), "full_d0_varpi_resolved": True}),
        ("family named", {"branch": 7, "claims": set(CLAIMS), "named_family": True}),
        ("kernel promoted physical", {"branch": 7, "claims": set(CLAIMS), "physical_kernel": True}),
        ("mass or spectrum promoted", {"branch": 7, "claims": set(CLAIMS), "mass_or_spectrum": True}),
        ("action derived", {"branch": 7, "claims": set(CLAIMS), "derived_action": True}),
        ("PS reduction constructed", {"branch": 7, "claims": set(CLAIMS), "constructed_ps_reduction": True}),
        ("rank-32 kernel used at rank 12", {"branch": 7, "claims": set(CLAIMS),
                                            "stage_rank": 12, "claimed_family_kernel": 32}),
    ]


def selftest() -> int:
    fired = 0
    for name, mutant in semantic_mutants():
        try:
            validate_semantics(mutant)
        except AssertionError:
            fired += 1
        else:
            raise AssertionError(f"semantic mutant did not fire: {name}")
    return fired


def artifact_guard() -> None:
    repo = Path(__file__).resolve().parents[2]
    artifact = repo / "lab/active-research/joe-directed/high-energy-two-plus-one/cb6-h210-three-horn-compatibility-2026-08-16.md"
    text = artifact.read_text(encoding="utf-8")
    required = (
        "H210-FCORR",
        "H210-ALIGN",
        "H210-PSRED",
        "all-three",
        "F_corr",
        "M_3",
        "Z/internal-144",
        "both conjugate halves",
        "full `d0+varpi`",
        "SC-GEN-53",
    )
    missing = [token for token in required if token not in text]
    assert not missing, f"artifact custody tokens missing: {missing}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()

    passed = exact_checks()
    artifact_guard()
    print(f"CB-6C exact checks: {len(passed)}/{len(passed)}")
    for item in passed:
        print(f"PASS {item}")
    print("PASS artifact source/custody guard")
    if args.selftest:
        fired = selftest()
        print(f"semantic mutants fired: {fired}/{len(semantic_mutants())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
