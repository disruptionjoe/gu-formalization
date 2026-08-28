#!/usr/bin/env python3
"""Protect the complete evidence-specific adjudication of register writebacks."""

from __future__ import annotations

import copy
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "lab/process/improvement-register-writeback-adjudication-v2.json"
REGISTER = ROOT / "lab/process/improvement-register-2026-08-03.md"

EXPECTED_IDS = {
    "P-C2", "P-H16", "P-H26", "P-H28", "P-H29", "P-M14", "P-L11", "P-L14", "P-L16",
    "M-C2", "M-H2", "M-H4", "M-H5", "M-H6", "M-H7", "M-H8", "M-H10",
    "M-H11", "M-H12", "M-H13", "M-H14", "M-H16", "M-M6", "M-M7", "M-M9",
    "M-M10", "M-M11", "M-M12", "M-M13", "M-M14", "M-M16", "M-M18", "M-M19", "M-M20",
    "M-M22", "M-M23", "M-M24", "M-M27", "M-L7", "M-H17", "M-M28", "M-M29",
    "M-M30", "M-S1", "M-S2", "M-S4", "M-S5",
}
ALLOWED = {"EXECUTED", "VERIFIED_LIVE", "PREMISE_SHIFTED", "PREMISE_CORRECTED", "RETIRED"}
ROW = re.compile(r"^\|\s*((?:P|M)-[A-Z]?\d+)\s*\|(.*)$", re.M)


def validate(data: dict, register_text: str) -> list[str]:
    errors: list[str] = []
    records = data.get("records", [])
    ids = [record.get("id") for record in records]
    if len(ids) != len(set(ids)):
        errors.append("duplicate record id")
    if set(ids) != EXPECTED_IDS:
        errors.append("candidate population mismatch")

    rows = {match.group(1): match.group(2) for match in ROW.finditer(register_text)}
    for record in records:
        rid = record.get("id")
        disposition = record.get("disposition")
        if disposition not in ALLOWED:
            errors.append(f"{rid}: invalid disposition")
        evidence = ROOT / str(record.get("evidence", ""))
        if not evidence.is_file():
            errors.append(f"{rid}: missing evidence")
        if len(str(record.get("basis", "")).split()) < 8:
            errors.append(f"{rid}: under-explained basis")
        display_disposition = str(disposition).replace("_", " ")
        if display_disposition not in rows.get(rid, ""):
            errors.append(f"{rid}: register marker missing")
    return errors


class ImprovementRegisterWritebackAdjudication(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(MANIFEST.read_text())
        cls.register_text = REGISTER.read_text()

    def test_live_manifest_and_register(self) -> None:
        self.assertEqual([], validate(self.data, self.register_text))

    def test_planted_missing_record_is_rejected(self) -> None:
        mutant = copy.deepcopy(self.data)
        mutant["records"].pop()
        self.assertIn("candidate population mismatch", validate(mutant, self.register_text))

    def test_planted_invalid_disposition_is_rejected(self) -> None:
        mutant = copy.deepcopy(self.data)
        mutant["records"][0]["disposition"] = "AUTO_CLOSED"
        self.assertTrue(any("invalid disposition" in item for item in validate(mutant, self.register_text)))

    def test_planted_missing_evidence_is_rejected(self) -> None:
        mutant = copy.deepcopy(self.data)
        mutant["records"][0]["evidence"] = "_local/does-not-exist"
        self.assertTrue(any("missing evidence" in item for item in validate(mutant, self.register_text)))

    def test_planted_unmarked_row_is_rejected(self) -> None:
        mutant_text = self.register_text.replace("**EXECUTED (writeback adjudicated 2026-08-26).**", "", 1)
        self.assertTrue(any("register marker missing" in item for item in validate(self.data, mutant_text)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
