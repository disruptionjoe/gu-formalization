#!/usr/bin/env python3
"""Audit the Cycle 3 C_GW / BvN wall define-or-demote artifact.

This is a structural audit, not a proof of any operator-algebra statement. It
checks that the artifact names C_GW objects and morphisms, candidate L and R,
the BvN wall status, rollback conditions, and a machine-readable demotion
summary without claiming the underdefined wall has been proved.
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "cycle-gates-and-audits" / "cycle3-cgw-bvn-wall-define-or-demote-gate-2026-06-24.md"
)

EXPECTED_VERDICT = "DEMOTED_UNDERDEFINED_WITH_TRIVIAL_COMMUTATIVE_RESIDUE"

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Candidate `C_GW` Objects and Morphisms",
    "## 3. Candidate Functors `L`, `R` and Adjunction/Non-Adjunction Proposition",
    "## 4. Whether the BvN Wall Is Well-Typed, Trivial, or Underdefined",
    "## 5. First Exact Obstruction",
    "## 6. Impact for C_MPR/9-Tuple/Signed-Readout Claims",
    "## 7. Next Meaningful Proof or Demotion Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_TERMS = [
    "C_GW",
    "objects",
    "morphisms",
    "`L`",
    "`R`",
    "BvN wall",
    "anomaly-free",
    "well-typed",
    "trivial",
    "underdefined",
    "demoted",
    "rollback/falsification conditions",
]

REQUIRED_OBJECT_FIELDS = {
    "A_unital_star_or_lattice_Cstar_algebra",
    "H_Hilbert_or_lattice_spinor_module",
    "pi_faithful_representation",
    "D_GW_Dirac_operator",
    "Gamma_chirality_grading",
    "a_GW_scale",
    "Loc_locality_admissibility_data",
    "kappa_index_or_anomaly_class",
}

REQUIRED_MORPHISM_FIELDS = {
    "alpha_star_homomorphism",
    "U_intertwiner",
    "representation_compatibility",
    "chirality_compatibility",
    "Dirac_compatibility",
    "locality_compatibility",
    "anomaly_defect_zero",
}

REQUIRED_ROLLBACKS = {
    "repo_accepted_C_GW_objects",
    "repo_accepted_anomaly_free_C_GW_morphisms",
    "repo_accepted_C_ClassicalDistribLR_objects_and_morphisms",
    "functorial_R_to_distributive_classical_side_preserving_named_nontrivial_Dirac_GW_anomaly_content",
    "functorial_L_landing_in_nondegenerate_GW_subcategory",
    "nonadjunction_or_adjunction_proposition_without_smuggled_preservation_predicate",
}

FORBIDDEN_OVERCLAIMS = [
    r"\bthe BvN wall is proved\b",
    r"\bBvN wall proved\b",
    r"\bBvN wall theorem is proved\b",
    r"\bClassical-Value-Lattice Wall(?: theorem)? HOLDS rigorously\b",
    r'"bvn_wall_proved"\s*:\s*true',
    r"\bnon-adjunction wall is proved\b",
]


def read_artifact() -> str:
    try:
        return ARTIFACT.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing C_GW/BvN wall artifact: {ARTIFACT}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing fenced JSON summary after section 8")
    return json.loads(match.group(1))


class Cycle3CgwBvnWallDefineOrDemoteAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_artifact()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_required_terms_appear(self) -> None:
        for term in REQUIRED_TERMS:
            self.assertIn(term, self.text)

    def test_verdict_carries_required_status_words(self) -> None:
        self.assertEqual(self.summary["verdict"], EXPECTED_VERDICT)
        verdict_section = self.text.split("## 1. Verdict", 1)[1].split("## 2.", 1)[0].lower()
        for word in ["well-typed", "trivial", "underdefined", "demoted"]:
            self.assertIn(word, verdict_section)
            self.assertIn(word, self.summary["verdict_terms"])

    def test_cgw_objects_and_morphisms_are_machine_readable(self) -> None:
        candidate = self.summary["candidate_C_GW"]
        objects = set(candidate["objects"])
        morphisms = set(candidate["morphisms"])
        self.assertFalse(REQUIRED_OBJECT_FIELDS - objects)
        self.assertFalse(REQUIRED_MORPHISM_FIELDS - morphisms)
        self.assertIn("object_and_morphism_candidate", self.summary["strict_candidate_C_GW_status"])

    def test_candidate_L_and_R_are_present_and_nonpromotional(self) -> None:
        functors = self.summary["candidate_functors"]
        self.assertIn("L", functors)
        self.assertIn("R", functors)
        self.assertEqual(functors["L"]["L_comm"], "functorial_but_commutative_or_GW_trivial")
        self.assertIn("not_functorial", functors["L"]["L_freeGW"])
        self.assertIn("codomain_not_distributive", functors["R"]["R_proj"])
        self.assertIn("noncanonical", functors["R"]["R_ctx"])
        self.assertIn("not_full_GW", functors["R"]["R_SR"])

    def test_bvn_wall_is_demoted_not_proved(self) -> None:
        self.assertFalse(self.summary["bvn_wall_proved"])
        self.assertFalse(self.summary["current_statement_well_typed"])
        self.assertIn("underdefined", self.summary["bvn_wall_status"])
        self.assertIn("demoted", self.summary["bvn_wall_status"])
        self.assertIn("not_well_typed", self.summary["well_typed_assessment"]["current_repo_wall"])

        for pattern in FORBIDDEN_OVERCLAIMS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden overclaim present: {pattern}",
            )

    def test_first_obstruction_mentions_R_and_three_requirements(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertIn("R from C_GW", obstruction)
        self.assertIn("distributive", obstruction)
        self.assertIn("canonical", obstruction)
        self.assertIn("nontrivial Dirac/GW/anomaly content", obstruction)

    def test_impact_keeps_csr_and_bvn_status_separate(self) -> None:
        impact = self.summary["impact"]
        self.assertEqual(impact["C_SR_signed_readout"], "unchanged_rigorous_core")
        self.assertEqual(impact["C_MPR"], "schema_except_for_C_SR_reduct")
        self.assertEqual(impact["nine_tuple"], "classification_record_not_complete_invariant")
        self.assertIn("demote", impact["BvN_wall"])

    def test_rollback_conditions_and_json_summary_exist(self) -> None:
        self.assertIn("Rollback/falsification conditions", self.text)
        rollbacks = set(self.summary["rollback_conditions"])
        missing = REQUIRED_ROLLBACKS - rollbacks
        self.assertFalse(missing, f"missing rollback conditions: {sorted(missing)}")
        self.assertGreaterEqual(len(rollbacks), 6)
        self.assertIn("No BvN wall proof is claimed", self.summary["overclaim_guard"])


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(Cycle3CgwBvnWallDefineOrDemoteAudit)
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
