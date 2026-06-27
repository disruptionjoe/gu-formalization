#!/usr/bin/env python3
"""Bounded checks for the Temporal-Issuance-as-GU-source-action steelmen.

This is not a GU source-action derivation. It encodes the finite distinctions the
steelman notes depend on:

* record/finality-only objects do not select a shiab family member;
* unique toy selection requires an explicit source-side family-coordinate carrier;
* boundary eta can move an index toy while staying blind to the shiab toy;
* signed readout can be non-monotone over monotone provenance;
* record finality without holonomy cannot supply a spectral section;
* cosmology bridges are killed if they are circularly defined from energy/expansion.
"""

from __future__ import annotations

import json
import math
import re
import unittest
from dataclasses import dataclass
from pathlib import Path
from typing import FrozenSet, Iterable, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]
CROSSWALK_DIR = ROOT / "explorations" / "time-as-finality-crosswalk"

OVERVIEW = CROSSWALK_DIR / "ti-as-gu-source-action-three-steelmen-2026-06-27.md"
V1 = CROSSWALK_DIR / "ti-as-gu-source-action-v1-formal-integration-steelman-2026-06-27.md"
V2 = CROSSWALK_DIR / "ti-as-gu-source-action-v2-wolfram-signed-readout-steelman-2026-06-27.md"
V3 = CROSSWALK_DIR / "ti-as-gu-source-action-v3-cosmological-steelman-2026-06-27.md"
README = CROSSWALK_DIR / "README.md"


FamilyCoord = Tuple[int, int, int, int]

CANON_SHIAB: FamilyCoord = (1, 0, 1, 0)
SHIAB_TOY_CANDIDATES: Tuple[FamilyCoord, ...] = (
    CANON_SHIAB,
    (0, 1, 0, 1),  # pure wedge on both chiral blocks
    (1, 1, 1, 1),  # mixed channel
    (1, 0, 0, 0),  # untied plus block
    (0, 0, 1, 0),  # untied minus block
    (1, 0, 0, 1),  # cross channel
    (0, 1, 1, 0),  # cross channel
    (1, -1, 1, -1),  # gamma-trace-style contrast toy
)


@dataclass(frozen=True)
class IssuanceRule:
    name: str
    effect_tags: FrozenSet[str]
    has_source_action: bool = False
    has_family_coordinate_function: bool = False
    selected_family_coord: Optional[FamilyCoord] = None
    has_boundary_holonomy: bool = False
    uses_existing_energy: bool = False
    defines_noncircular_accounting: bool = False
    has_theta_or_boundary_curvature_carrier: bool = False


def selected_family(rule: IssuanceRule) -> Tuple[FamilyCoord, ...]:
    """A toy selector: only Issue[S] plus a source family carrier can select."""
    can_select = (
        "Issue[S]" in rule.effect_tags
        and rule.has_source_action
        and rule.has_family_coordinate_function
        and rule.selected_family_coord is not None
    )
    if can_select:
        return (rule.selected_family_coord,)
    return SHIAB_TOY_CANDIDATES


def cot(x: float) -> float:
    return 1.0 / math.tan(x)


def signature_eta_lens_space(p: int, q: int) -> float:
    """Signature-eta style lens-space toy, enough to test nonzero boundary leverage."""
    if p <= 1:
        raise ValueError("p must be > 1")
    return -(1.0 / p) * sum(
        cot(math.pi * k / p) * cot(math.pi * q * k / p) for k in range(1, p)
    )


def eta_s3_shiab_toy(member: FamilyCoord) -> float:
    """Existing GU boundary toy behavior: S3 eta is zero and family-coordinate blind."""
    _ = member
    return 0.0


def regularized_index_toy(bulk_index: float, eta: float, h: float = 0.0) -> float:
    """APS-shaped toy: index = bulk - (eta + h)/2."""
    return bulk_index - 0.5 * (eta + h)


def provenance(events: Iterable[str], weights: dict[str, int]) -> Tuple[int, int]:
    plus = 0
    minus = 0
    for event in events:
        weight = weights[event]
        plus += max(weight, 0)
        minus += max(-weight, 0)
    return plus, minus


def readout(events: Iterable[str], weights: dict[str, int]) -> int:
    plus, minus = provenance(events, weights)
    return plus - minus


def classify_boundary_carrier(rule: IssuanceRule) -> str:
    if rule.has_boundary_holonomy:
        return "CARRIER_PRESENT"
    if "Finalize[R]" in rule.effect_tags and "Issue[S]" not in rule.effect_tags:
        return "FINALITY_ONLY_NO_CARRIER"
    return "NO_BOUNDARY_CARRIER"


def classify_cosmology_bridge(rule: IssuanceRule) -> str:
    if rule.uses_existing_energy:
        return "KILLED_CIRCULAR_ENERGY_ACCOUNTING"
    if not rule.has_source_action:
        return "BLOCKED_NO_SOURCE_ACTION"
    if not rule.defines_noncircular_accounting:
        return "PARKED_NO_NONCIRCULAR_ACCOUNTING"
    if not rule.has_theta_or_boundary_curvature_carrier:
        return "PARKED_NO_THETA_CARRIER"
    return "CANDIDATE_REQUIRES_FLRW_SIGN_CHECK"


def json_blocks(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    blocks = []
    for match in re.finditer(r"```json\n(.*?)\n```", text, re.DOTALL):
        blocks.append(json.loads(match.group(1)))
    return blocks


class TemporalIssuanceSourceActionToyChecks(unittest.TestCase):
    def test_record_finality_does_not_select_shiab(self) -> None:
        rule = IssuanceRule(
            name="record-only finality",
            effect_tags=frozenset({"Project[O]", "Finalize[R]", "Lose[K]"}),
        )
        selected = selected_family(rule)
        self.assertEqual(len(selected), len(SHIAB_TOY_CANDIDATES))
        self.assertIn(CANON_SHIAB, selected)

    def test_issue_tag_without_source_carrier_still_does_not_select(self) -> None:
        rule = IssuanceRule(
            name="issue tag no GU carrier",
            effect_tags=frozenset({"Issue[S]", "Finalize[R]"}),
        )
        selected = selected_family(rule)
        self.assertEqual(len(selected), len(SHIAB_TOY_CANDIDATES))

    def test_unique_selection_requires_source_family_coordinate_carrier(self) -> None:
        rule = IssuanceRule(
            name="source-family-coordinate toy",
            effect_tags=frozenset({"Issue[S]"}),
            has_source_action=True,
            has_family_coordinate_function=True,
            selected_family_coord=CANON_SHIAB,
        )
        selected = selected_family(rule)
        self.assertEqual(selected, (CANON_SHIAB,))
        self.assertTrue(rule.has_source_action)
        self.assertTrue(rule.has_family_coordinate_function)

    def test_boundary_eta_can_move_index_toy_but_not_shiab_toy(self) -> None:
        s3_values = [eta_s3_shiab_toy(member) for member in SHIAB_TOY_CANDIDATES]
        self.assertEqual(s3_values, [0.0] * len(SHIAB_TOY_CANDIDATES))

        eta_l31 = signature_eta_lens_space(3, 1)
        self.assertGreater(abs(eta_l31), 1e-6)
        self.assertNotEqual(
            regularized_index_toy(24.0, eta_l31),
            regularized_index_toy(24.0, 0.0),
        )

    def test_signed_readout_nonmonotone_over_monotone_provenance(self) -> None:
        weights = {"x_plus": 1, "x_minus": -1}
        before: tuple[str, ...] = ()
        after = ("x_minus",)

        self.assertEqual(provenance(before, weights), (0, 0))
        self.assertEqual(provenance(after, weights), (0, 1))
        self.assertGreaterEqual(provenance(after, weights)[1], provenance(before, weights)[1])
        self.assertLess(readout(after, weights), readout(before, weights))

    def test_record_finality_without_holonomy_is_not_boundary_carrier(self) -> None:
        record_only = IssuanceRule(
            name="record-only",
            effect_tags=frozenset({"Project[O]", "Finalize[R]", "Lose[K]"}),
        )
        carrier = IssuanceRule(
            name="source-boundary-carrier",
            effect_tags=frozenset({"Issue[S]", "Finalize[R]"}),
            has_source_action=True,
            has_boundary_holonomy=True,
        )
        self.assertEqual(classify_boundary_carrier(record_only), "FINALITY_ONLY_NO_CARRIER")
        self.assertEqual(classify_boundary_carrier(carrier), "CARRIER_PRESENT")

    def test_cosmology_bridge_kill_and_park_conditions(self) -> None:
        circular = IssuanceRule(
            name="defined from dark energy",
            effect_tags=frozenset({"Issue[S]"}),
            uses_existing_energy=True,
        )
        no_source = IssuanceRule(
            name="observer expansion readout",
            effect_tags=frozenset({"Project[O]", "Finalize[R]"}),
        )
        no_accounting = IssuanceRule(
            name="source tag no accounting",
            effect_tags=frozenset({"Issue[S]"}),
            has_source_action=True,
        )
        candidate = IssuanceRule(
            name="noncircular theta carrier",
            effect_tags=frozenset({"Issue[S]"}),
            has_source_action=True,
            defines_noncircular_accounting=True,
            has_theta_or_boundary_curvature_carrier=True,
        )

        self.assertEqual(classify_cosmology_bridge(circular), "KILLED_CIRCULAR_ENERGY_ACCOUNTING")
        self.assertEqual(classify_cosmology_bridge(no_source), "BLOCKED_NO_SOURCE_ACTION")
        self.assertEqual(classify_cosmology_bridge(no_accounting), "PARKED_NO_NONCIRCULAR_ACCOUNTING")
        self.assertEqual(classify_cosmology_bridge(candidate), "CANDIDATE_REQUIRES_FLRW_SIGN_CHECK")


class TemporalIssuanceSourceActionDocumentAudit(unittest.TestCase):
    def test_all_steelman_notes_exist_and_block_claim_promotion(self) -> None:
        for path in (OVERVIEW, V1, V2, V3):
            with self.subTest(path=path.name):
                self.assertTrue(path.exists())
                text = path.read_text(encoding="utf-8")
                self.assertRegex(text, r"NO_CLAIM_PROMOTION|claim_promotion")
                blocks = json_blocks(path)
                self.assertTrue(blocks, "expected machine-readable JSON block")
                for block in blocks:
                    self.assertFalse(block["claim_promotion"])

    def test_notes_preserve_version_specific_kill_criteria(self) -> None:
        checks = {
            V1: [
                "NO_UNIQUE_FAMILY_SELECTION_WITHOUT_SOURCE_CARRIER",
                "NO_BOUNDARY_HOLONOMY_CARRIER",
            ],
            V2: [
                "FIXED_RULE_OR_FIXED_LATENT_ABSORBS",
                "NO_HOLONOMY_ON_RECORD_GRAPH",
            ],
            V3: [
                "CIRCULAR_ENERGY_ACCOUNTING",
                "NO_NONCIRCULAR_ACCOUNTING_INVARIANT",
            ],
        }
        for path, phrases in checks.items():
            text = path.read_text(encoding="utf-8")
            for phrase in phrases:
                with self.subTest(path=path.name, phrase=phrase):
                    self.assertIn(phrase, text)

    def test_readme_links_packet(self) -> None:
        text = README.read_text(encoding="utf-8")
        for path in (OVERVIEW, V1, V2, V3):
            with self.subTest(path=path.name):
                self.assertIn(path.name, text)


if __name__ == "__main__":
    unittest.main()
