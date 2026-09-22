#!/usr/bin/env python3
"""Independent replay and hostile mutations for K295."""

from __future__ import annotations

import json
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k295-order-seven-exterior-integrability-boundary.json"


def valid(payload: dict) -> bool:
    audit = payload["pointwise_majorant_face_audit"]
    table = audit["one_gap_integrability"]
    release = payload["release_test"]
    return all(
        (
            len(table) == 5,
            [row["combined_face_power"] for row in table] == [1, 0, -1, -2, -3],
            [row["one_gap_integrable_at_zero"] for row in table] == [True, True, False, False, False],
            audit["first_nonintegrable_order"] == 2,
            audit["fourth_order_global_extension_legal"] is False,
            audit["true_integrand_divergence_proved"] is False,
            Decimal(payload["tube_bare_measure_upper"]["fraction_of_complete_bare_mass_upper"]) < Decimal("1e-20"),
            release["true_integrand_divergence_claimed"] is False,
            release["complete_base_action_column_evaluated"] is False,
        )
    )


def main() -> int:
    payload = json.loads(MANIFEST.read_text())
    if not valid(payload):
        raise AssertionError("K295 manifest failed independent replay")
    mutations = [
        ("powers", [1, 0, 0, -2, -3]),
        ("integrable", [True, True, True, False, False]),
        ("first", 3),
        ("global", True),
        ("true_divergence", True),
        ("share", "1"),
        ("release_divergence", True),
        ("action", True),
        ("rows", 4),
    ]
    rejected = 0
    for name, value in mutations:
        candidate = json.loads(json.dumps(payload))
        audit = candidate["pointwise_majorant_face_audit"]
        if name == "powers":
            for row, item in zip(audit["one_gap_integrability"], value): row["combined_face_power"] = item
        elif name == "integrable":
            for row, item in zip(audit["one_gap_integrability"], value): row["one_gap_integrable_at_zero"] = item
        elif name == "first": audit["first_nonintegrable_order"] = value
        elif name == "global": audit["fourth_order_global_extension_legal"] = value
        elif name == "true_divergence": audit["true_integrand_divergence_proved"] = value
        elif name == "share": candidate["tube_bare_measure_upper"]["fraction_of_complete_bare_mass_upper"] = value
        elif name == "release_divergence": candidate["release_test"]["true_integrand_divergence_claimed"] = value
        elif name == "action": candidate["release_test"]["complete_base_action_column_evaluated"] = value
        else: audit["one_gap_integrability"] = audit["one_gap_integrability"][:value]
        if not valid(candidate): rejected += 1
    if rejected != len(mutations):
        raise AssertionError("hostile mutation escaped K295 probe")
    print(f"K295 independent replay: 9/9 checks passed; hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
