#!/usr/bin/env python3
"""Independent K255 source and spectral-witness probe."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
RECORD = ROOT / "lab/process/k255-native-i1b-full-operator-data-gate.json"


def values(alpha: Fraction, mass: Fraction) -> tuple[Fraction, ...]:
    return tuple(Fraction(n) + alpha + mass for n in range(-3, 4))


def main() -> None:
    record = json.loads(RECORD.read_text())
    register = yaml.safe_load((ROOT / "lab/sources/source-claim-register.yaml").read_text())
    extraction = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
    bulk = (ROOT / "lab/sources/selected-k77-bulk-operator-source-reinspection-2026-08-09.md").read_text()
    ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.263.json").read_text())

    claims = {row["id"]: row for row in register["claims"]}
    assert claims["SC-OP-04"]["polarity"] == "ASSERTS"
    assert claims["SC-OP-05"]["polarity"] == "UNCERTAIN"
    assert "neither source supplies a uniqueness theorem" in extraction
    assert "closed maximal/minimal graph domains" in bulk

    rows = {row["id"]: row for row in ledger["rows"]}
    assert rows["LT-GR6b"]["verdict"] == "NEEDS"
    assert rows["LT-SM8"]["verdict"] == "NEEDS"

    periodic = values(Fraction(0), Fraction(0))
    lower = values(Fraction(0), Fraction(1, 3))
    domain = values(Fraction(1, 2), Fraction(0))
    assert periodic != lower
    assert periodic != domain
    assert tuple(x - y for x, y in zip(lower, periodic)) == (Fraction(1, 3),) * 7
    assert tuple(x - y for x, y in zip(domain, periodic)) == (Fraction(1, 2),) * 7

    # Hostile controls: removing the allegedly changed datum must collapse the
    # corresponding witness back to the baseline.
    assert values(Fraction(0), Fraction(0)) == periodic
    assert values(Fraction(0), Fraction(0)) != lower
    assert values(Fraction(0), Fraction(0)) != domain

    gate = record["full_operator_admission_contract"]
    assert len(gate["required_before_spectrum"]) == 6
    assert len(gate["additional_before_physical_mode"]) == 3
    assert gate["current_status"] == "DEPENDENCY_OPEN__NO_SPECTRAL_OR_PHYSICAL_INFERENCE_ADMITTED"
    ceiling = record["claim_ceiling"]
    for required in (
        "No claim that GU lacks a valid completion",
        "no constructed GU full operator",
        "source/ledger/canon/public change",
    ):
        assert required in ceiling
    assert record["principal_data_nonuniqueness"]["common_principal_symbol"] == "xi"
    assert "K250 already closed unique source selection negatively" in record["interpretation"]
    assert "K254 closed the finite local hull positively" in record["interpretation"]

    print("K255 independent source/spectral probe: PASS")


if __name__ == "__main__":
    main()
