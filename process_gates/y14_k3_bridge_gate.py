#!/usr/bin/env python3
"""Audit the Y14-to-K3 index bridge contract.

This is not a proof of the noncompact GU index.  It checks that the bridge note
keeps the noncompact Y^14 Fredholm problem, compact K3 control model, and
generation-count readout separated, and it exercises the decision logic for
when a K3 RS index may be promoted to a physical GU index.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import argparse
import json
from pathlib import Path
import re
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
BRIDGE_DOC = REPO_ROOT / "explorations" / "generation-sector" / "y14-k3-index-bridge-theorem-or-nogo-2026-06-24.md"


class BridgeDecision(str, Enum):
    BRIDGE_AVAILABLE = "BRIDGE_AVAILABLE"
    UNDERDEFINED = "UNDERDEFINED"
    NO_GO = "NO_GO"
    OPEN_BACKGROUND_DEPENDENT = "OPEN_BACKGROUND_DEPENDENT"
    COMPLEX_ONLY_H_STRUCTURE_MISSING = "COMPLEX_ONLY_H_STRUCTURE_MISSING"
    INVALID_CIRCULAR = "INVALID_CIRCULAR"


FORBIDDEN_INPUTS = {
    "ind_H(D_RS)=8",
    "ind_H(D_GU)=24",
    "rank_eff=4",
    "rank_eff=8",
    "three_generations",
    "physical_DOF_count_as_index",
}


@dataclass(frozen=True)
class BridgeInputs:
    physical_rs_complex: bool | None
    p_disc_nonempty: bool | None
    p_disc_bounded_weighted: bool | None
    weighted_fredholm_parametrix: bool | None
    k3_reduction_or_aps_map: bool | None
    symbol_class_matches: bool | None
    right_h_structure_verified: bool
    ch2_f_fixed: bool
    bounded_transform_family: bool | None
    aps_eta_spectral_flow_accounted: bool | None
    forbidden_inputs_seen: set[str] | None = None


def classify_bridge(inputs: BridgeInputs) -> BridgeDecision:
    """Classify whether a K3 RS index can be promoted to the Y14 physical index."""

    forbidden = FORBIDDEN_INPUTS.intersection(inputs.forbidden_inputs_seen or set())
    if forbidden:
        return BridgeDecision.INVALID_CIRCULAR

    no_go_fields = {
        "p_disc_nonempty": inputs.p_disc_nonempty,
        "p_disc_bounded_weighted": inputs.p_disc_bounded_weighted,
        "weighted_fredholm_parametrix": inputs.weighted_fredholm_parametrix,
        "k3_reduction_or_aps_map": inputs.k3_reduction_or_aps_map,
        "symbol_class_matches": inputs.symbol_class_matches,
        "bounded_transform_family": inputs.bounded_transform_family,
        "aps_eta_spectral_flow_accounted": inputs.aps_eta_spectral_flow_accounted,
    }
    if any(value is False for value in no_go_fields.values()):
        return BridgeDecision.NO_GO

    underdefined_fields = {
        "physical_rs_complex": inputs.physical_rs_complex,
        **no_go_fields,
    }
    if any(value is None for value in underdefined_fields.values()):
        return BridgeDecision.UNDERDEFINED

    if not inputs.right_h_structure_verified:
        return BridgeDecision.COMPLEX_ONLY_H_STRUCTURE_MISSING

    if not inputs.ch2_f_fixed:
        return BridgeDecision.OPEN_BACKGROUND_DEPENDENT

    return BridgeDecision.BRIDGE_AVAILABLE


def bridge_doc_text() -> str:
    return BRIDGE_DOC.read_text(encoding="utf-8")


def extract_ledger(text: str) -> dict[str, object]:
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if not match:
        raise AssertionError("Bridge condition ledger JSON block not found.")
    return json.loads(match.group(1))


class BridgeDocumentAuditTests(unittest.TestCase):
    def test_required_sections_are_present(self) -> None:
        text = bridge_doc_text()
        required = [
            "## 1. Verdict",
            "## 2. Physical `Y^14` Index Problem",
            "## 3. Compact K3 Model And What It Currently Proves",
            "## 4. Exact Bridge Conditions",
            "## 5. Failure Modes And Counterexamples",
            "## 6. What This Means For Generation-Count Claims",
            "## 7. Next Meaningful Proof Or Computation Step",
        ]
        for heading in required:
            self.assertIn(heading, text)

    def test_core_bridge_objects_are_named(self) -> None:
        text = bridge_doc_text()
        required_terms = [
            "D^Y_RS,delta,disc",
            "P_disc",
            "W^{1,2}_{H,delta,disc}",
            "APS",
            "eta(A_RS^phys)",
            "Fred_H(K_H)",
            "E_raw = (V + 1) tensor F",
            "ind_C(E_raw) = -38 n + 5 k",
            "ch_2(F)[K3]",
            "COMPLEX_ONLY_H_STRUCTURE_MISSING",
            "OPEN_BACKGROUND_DEPENDENT",
            "INVALID_CIRCULAR",
        ]
        for term in required_terms:
            self.assertIn(term, text)

    def test_ledger_declares_current_bridge_not_closed(self) -> None:
        ledger = extract_ledger(bridge_doc_text())
        self.assertEqual(ledger["verdict"], "CONDITIONAL_THEOREM_CURRENTLY_UNDERDEFINED")
        self.assertEqual(ledger["current_decision"], "OPEN_MISSING_BRIDGE_DATA")
        self.assertEqual(ledger["k3_raw_index_status"], "CONTROL_ONLY")
        self.assertEqual(ledger["y14_full_unprojected_status"], "NO_GO")

    def test_ledger_has_all_required_bridge_conditions(self) -> None:
        ledger = extract_ledger(bridge_doc_text())
        condition_ids = {entry["id"] for entry in ledger["required_bridge_conditions"]}
        expected = {
            "C1_PHYSICAL_RS_COMPLEX",
            "C2_TAU_DISCRETE_PROJECTION",
            "C3_WEIGHTED_FREDHOLM_PARAMETRIX",
            "C4_K3_REDUCTION_OR_APS_COMPACTIFICATION",
            "C5_SYMBOL_CLASS_MATCH",
            "C6_RIGHT_H_STRUCTURE",
            "C7_BACKGROUND_CH2_F",
            "C8_BOUNDED_TRANSFORM_FAMILY",
            "C9_BOUNDARY_ETA_AND_SPECTRAL_FLOW",
            "C10_NONCIRCULAR_GENERATION_READOUT",
        }
        self.assertEqual(condition_ids, expected)

    def test_forbidden_inputs_are_listed_in_ledger(self) -> None:
        ledger = extract_ledger(bridge_doc_text())
        self.assertEqual(set(ledger["forbidden_inputs"]), FORBIDDEN_INPUTS)


class BridgeDecisionTests(unittest.TestCase):
    def complete_inputs(self) -> BridgeInputs:
        return BridgeInputs(
            physical_rs_complex=True,
            p_disc_nonempty=True,
            p_disc_bounded_weighted=True,
            weighted_fredholm_parametrix=True,
            k3_reduction_or_aps_map=True,
            symbol_class_matches=True,
            right_h_structure_verified=True,
            ch2_f_fixed=True,
            bounded_transform_family=True,
            aps_eta_spectral_flow_accounted=True,
        )

    def test_bridge_available_only_when_every_gate_is_closed(self) -> None:
        self.assertEqual(classify_bridge(self.complete_inputs()), BridgeDecision.BRIDGE_AVAILABLE)

    def test_missing_physical_complex_is_underdefined(self) -> None:
        inputs = self.complete_inputs()
        changed = BridgeInputs(**{**inputs.__dict__, "physical_rs_complex": None})
        self.assertEqual(classify_bridge(changed), BridgeDecision.UNDERDEFINED)

    def test_empty_discrete_sector_is_no_go(self) -> None:
        inputs = self.complete_inputs()
        changed = BridgeInputs(**{**inputs.__dict__, "p_disc_nonempty": False})
        self.assertEqual(classify_bridge(changed), BridgeDecision.NO_GO)

    def test_unbounded_projection_is_no_go(self) -> None:
        inputs = self.complete_inputs()
        changed = BridgeInputs(**{**inputs.__dict__, "p_disc_bounded_weighted": False})
        self.assertEqual(classify_bridge(changed), BridgeDecision.NO_GO)

    def test_missing_h_structure_is_complex_only(self) -> None:
        inputs = self.complete_inputs()
        changed = BridgeInputs(**{**inputs.__dict__, "right_h_structure_verified": False})
        self.assertEqual(classify_bridge(changed), BridgeDecision.COMPLEX_ONLY_H_STRUCTURE_MISSING)

    def test_unfixed_ch2_is_background_dependent(self) -> None:
        inputs = self.complete_inputs()
        changed = BridgeInputs(**{**inputs.__dict__, "ch2_f_fixed": False})
        self.assertEqual(classify_bridge(changed), BridgeDecision.OPEN_BACKGROUND_DEPENDENT)

    def test_forbidden_generation_target_is_invalid(self) -> None:
        inputs = self.complete_inputs()
        changed = BridgeInputs(**{**inputs.__dict__, "forbidden_inputs_seen": {"ind_H(D_RS)=8"}})
        self.assertEqual(classify_bridge(changed), BridgeDecision.INVALID_CIRCULAR)


def summary() -> dict[str, object]:
    ledger = extract_ledger(bridge_doc_text())
    current = classify_bridge(
        BridgeInputs(
            physical_rs_complex=None,
            p_disc_nonempty=None,
            p_disc_bounded_weighted=None,
            weighted_fredholm_parametrix=None,
            k3_reduction_or_aps_map=None,
            symbol_class_matches=None,
            right_h_structure_verified=False,
            ch2_f_fixed=False,
            bounded_transform_family=None,
            aps_eta_spectral_flow_accounted=None,
        )
    )
    return {
        "not_a_proof": True,
        "document": str(BRIDGE_DOC.relative_to(REPO_ROOT)),
        "ledger_verdict": ledger["verdict"],
        "current_decision_logic": current.value,
        "required_conditions": [entry["id"] for entry in ledger["required_bridge_conditions"]],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit the Y14-to-K3 bridge contract.")
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(summary(), indent=2, sort_keys=True))
        return 0

    print("Y14-to-K3 bridge audit: contract and decision logic only, not a proof.")
    print()
    suite = unittest.defaultTestLoader.loadTestsFromNames(
        [
            "__main__.BridgeDocumentAuditTests",
            "__main__.BridgeDecisionTests",
        ]
    )
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
