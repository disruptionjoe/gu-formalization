#!/usr/bin/env python3
"""Executable skeleton for the K3 RS symbol-index contract.

This file is not a proof and not a verification of the GU RS index.  It only
checks arithmetic and decision-rule behavior for the contract in
explorations/generation-count-rs-symbol-index-contract-2026-06-24.md.

The tests that would require real Clifford matrices, gamma-trace projectors,
gauge fixing, a K-theory symbol class, or an Atiyah-Singer/APS index are
intentionally skipped until those data are supplied.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import argparse
import json
import sys
import unittest


class Status(str, Enum):
    OPEN_MISSING_SYMBOL_DATA = "OPEN_MISSING_SYMBOL_DATA"
    INVALID_CIRCULAR = "INVALID_CIRCULAR"
    NON_ELLIPTIC = "NON_ELLIPTIC"
    OPEN_BACKGROUND_DEPENDENT = "OPEN_BACKGROUND_DEPENDENT"
    COMPLEX_ONLY_H_STRUCTURE_MISSING = "COMPLEX_ONLY_H_STRUCTURE_MISSING"
    CANDIDATE_A = "CANDIDATE_A"
    CANDIDATE_B = "CANDIDATE_B"
    OTHER_INDEX = "OTHER_INDEX"


FORBIDDEN_INPUTS = {
    "assumed_ind_h_d_rs",
    "ind_h_d_rs_target",
    "rank_eff_target",
    "assumed_rank_eff_4",
    "target_total_index_24",
    "target_generation_count_3",
    "physical_dof_as_index",
}


@dataclass(frozen=True)
class K3Invariants:
    ahat: int = 2
    chi: int = 24
    sigma: int = -16
    p1: int = -48
    b0: int = 1
    b2_plus: int = 3
    b2_minus: int = 19
    b4: int = 1

    def validate(self) -> None:
        assert self.p1 == 3 * self.sigma
        assert self.ahat == -self.sigma // 8
        assert self.chi == self.b0 + self.b2_plus + self.b2_minus + self.b4
        assert self.sigma == self.b2_plus - self.b2_minus


@dataclass(frozen=True)
class Decision:
    status: Status
    reason: str
    index_h: int | None = None
    rank_eff: float | None = None
    total_index: int | None = None
    generation_count: float | None = None
    missing_data: tuple[str, ...] = field(default_factory=tuple)


def classify_symbol_index(
    *,
    index_h: int | None,
    elliptic: bool | None,
    h_structure_verified: bool,
    symbol_class_constructed: bool,
    depends_on_background: bool = False,
    forbidden_inputs_seen: set[str] | None = None,
    missing_data: tuple[str, ...] = (),
    ahat_k3: int = 2,
    spin_half_index_h: int = 16,
    h_lines_per_generation: int = 8,
) -> Decision:
    """Classify a completed or incomplete RS symbol-index attempt.

    This is contract logic only.  It assumes that any supplied index_h was
    computed elsewhere from a real symbol class and was not target-injected.
    """

    forbidden_inputs_seen = forbidden_inputs_seen or set()
    circular = FORBIDDEN_INPUTS.intersection(forbidden_inputs_seen)
    if circular:
        return Decision(
            status=Status.INVALID_CIRCULAR,
            reason=f"Forbidden target input(s) used: {sorted(circular)}",
        )

    if not symbol_class_constructed or index_h is None or elliptic is None or missing_data:
        return Decision(
            status=Status.OPEN_MISSING_SYMBOL_DATA,
            reason="Missing Clifford/projector/gauge/symbol/index data.",
            missing_data=missing_data,
        )

    if not h_structure_verified:
        return Decision(
            status=Status.COMPLEX_ONLY_H_STRUCTURE_MISSING,
            reason="Complex index may exist, but H-linear conversion is not verified.",
        )

    if elliptic is False:
        return Decision(
            status=Status.NON_ELLIPTIC,
            reason="Gauge-fixed symbol or elliptic complex is not elliptic.",
        )

    if depends_on_background:
        return Decision(
            status=Status.OPEN_BACKGROUND_DEPENDENT,
            reason="Index depends on an unspecified Chern/background class.",
            index_h=index_h,
        )

    rank_eff = index_h / ahat_k3
    total_index = spin_half_index_h + index_h
    generation_count = total_index / h_lines_per_generation

    if index_h == 8:
        return Decision(
            status=Status.CANDIDATE_A,
            reason="Independent index_H equals 8.",
            index_h=index_h,
            rank_eff=rank_eff,
            total_index=total_index,
            generation_count=generation_count,
        )
    if index_h == 16:
        return Decision(
            status=Status.CANDIDATE_B,
            reason="Independent index_H equals 16.",
            index_h=index_h,
            rank_eff=rank_eff,
            total_index=total_index,
            generation_count=generation_count,
        )

    return Decision(
        status=Status.OTHER_INDEX,
        reason="Independent index_H is neither 8 nor 16.",
        index_h=index_h,
        rank_eff=rank_eff,
        total_index=total_index,
        generation_count=generation_count,
    )


RAW_RANK_SANITY = {
    "full_14d_chiral_kernel_H_rank": 416,
    "pulled_back_4d_reducible_pre_gauge_H_rank": 96,
    "spin4_irreducible_refinement_H_rank": 24,
}


class ContractLogicTests(unittest.TestCase):
    def test_k3_invariants(self) -> None:
        K3Invariants().validate()

    def test_raw_ranks_are_not_candidate_outputs(self) -> None:
        self.assertEqual(RAW_RANK_SANITY["full_14d_chiral_kernel_H_rank"], 416)
        self.assertEqual(RAW_RANK_SANITY["pulled_back_4d_reducible_pre_gauge_H_rank"], 96)
        self.assertEqual(RAW_RANK_SANITY["spin4_irreducible_refinement_H_rank"], 24)
        self.assertNotIn(8, RAW_RANK_SANITY.values())
        self.assertNotIn(16, RAW_RANK_SANITY.values())

    def test_missing_data_keeps_gate_open(self) -> None:
        decision = classify_symbol_index(
            index_h=None,
            elliptic=None,
            h_structure_verified=False,
            symbol_class_constructed=False,
            missing_data=("clifford_matrices", "projectors", "gauge_fixing"),
        )
        self.assertEqual(decision.status, Status.OPEN_MISSING_SYMBOL_DATA)

    def test_circular_inputs_are_invalid(self) -> None:
        decision = classify_symbol_index(
            index_h=8,
            elliptic=True,
            h_structure_verified=True,
            symbol_class_constructed=True,
            forbidden_inputs_seen={"assumed_ind_h_d_rs"},
        )
        self.assertEqual(decision.status, Status.INVALID_CIRCULAR)

    def test_missing_h_structure_is_complex_only(self) -> None:
        decision = classify_symbol_index(
            index_h=8,
            elliptic=True,
            h_structure_verified=False,
            symbol_class_constructed=True,
        )
        self.assertEqual(decision.status, Status.COMPLEX_ONLY_H_STRUCTURE_MISSING)

    def test_non_elliptic_symbol_fails_aps_route(self) -> None:
        decision = classify_symbol_index(
            index_h=8,
            elliptic=False,
            h_structure_verified=True,
            symbol_class_constructed=True,
        )
        self.assertEqual(decision.status, Status.NON_ELLIPTIC)

    def test_background_dependent_index_stays_open(self) -> None:
        decision = classify_symbol_index(
            index_h=8,
            elliptic=True,
            h_structure_verified=True,
            symbol_class_constructed=True,
            depends_on_background=True,
        )
        self.assertEqual(decision.status, Status.OPEN_BACKGROUND_DEPENDENT)

    def test_candidate_a_rule(self) -> None:
        decision = classify_symbol_index(
            index_h=8,
            elliptic=True,
            h_structure_verified=True,
            symbol_class_constructed=True,
        )
        self.assertEqual(decision.status, Status.CANDIDATE_A)
        self.assertEqual(decision.rank_eff, 4)
        self.assertEqual(decision.total_index, 24)
        self.assertEqual(decision.generation_count, 3)

    def test_candidate_b_rule(self) -> None:
        decision = classify_symbol_index(
            index_h=16,
            elliptic=True,
            h_structure_verified=True,
            symbol_class_constructed=True,
        )
        self.assertEqual(decision.status, Status.CANDIDATE_B)
        self.assertEqual(decision.rank_eff, 8)
        self.assertEqual(decision.total_index, 32)
        self.assertEqual(decision.generation_count, 4)

    def test_other_index_rule(self) -> None:
        decision = classify_symbol_index(
            index_h=12,
            elliptic=True,
            h_structure_verified=True,
            symbol_class_constructed=True,
        )
        self.assertEqual(decision.status, Status.OTHER_INDEX)
        self.assertEqual(decision.total_index, 28)
        self.assertEqual(decision.generation_count, 3.5)

    @unittest.skip("Real Cl(4,0)/Cl(9,5) matrices are not supplied in this skeleton.")
    def test_explicit_clifford_relations(self) -> None:
        raise NotImplementedError

    @unittest.skip("Gamma-trace projectors P_+ and P_- are not supplied in this skeleton.")
    def test_gamma_trace_projector_identities(self) -> None:
        raise NotImplementedError

    @unittest.skip("Gauge-fixed RS symbol or elliptic complex is not supplied in this skeleton.")
    def test_gauge_fixed_symbol_ellipticity(self) -> None:
        raise NotImplementedError

    @unittest.skip("No K-theory symbol class or Atiyah-Singer/APS evaluation is supplied.")
    def test_rs_symbol_index_evaluation(self) -> None:
        raise NotImplementedError


def contract_summary() -> dict[str, object]:
    invariants = K3Invariants()
    invariants.validate()
    missing_real_data = [
        "explicit Cl(4,0) gamma matrices",
        "right-H structure J and conversion certificate",
        "gamma-trace maps G_+, G_-",
        "projectors P_+, P_-",
        "gauge-fixing or elliptic-complex data",
        "K-theory symbol class",
        "Atiyah-Singer/APS index evaluation",
    ]
    return {
        "not_verification": True,
        "k3_invariants": invariants.__dict__,
        "raw_rank_sanity": RAW_RANK_SANITY,
        "missing_real_data": missing_real_data,
        "candidate_a_requires_ind_h": 8,
        "candidate_b_requires_ind_h": 16,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run RS symbol-index contract skeleton checks. This is not a proof."
    )
    parser.add_argument("--json", action="store_true", help="Print the skeleton summary as JSON.")
    args, remaining = parser.parse_known_args(argv)

    summary = contract_summary()
    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print("RS symbol-index contract skeleton: NOT A VERIFICATION.")
        print("Real Clifford/projector/gauge/symbol/index tests are intentionally skipped.")
        print("Missing real data:")
        for item in summary["missing_real_data"]:
            print(f"  - {item}")
        print()

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ContractLogicTests)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

