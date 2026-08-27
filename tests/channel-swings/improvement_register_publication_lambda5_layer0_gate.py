#!/usr/bin/env python3
"""Mutation-backed custody gate for P-H16, M-H2, and M-M28."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "wave_c": ROOT / "explorations/resolver-wave-c-rebased-q5-q6-mh7-2026-08-03.md",
    "register": ROOT / "lab/process/improvement-register-2026-08-03.md",
}
MANIFEST = ROOT / "lab/process/improvement-register-writeback-adjudication-v2.json"


def violations(texts: dict[str, str], manifest: dict[str, object]) -> list[str]:
    failures: list[str] = []
    required = {
        "register": [
            "10.5281/zenodo.21502234",
            "10.5281/zenodo.21502233",
            "2026-07-23",
            "10.5281/zenodo.21711582",
            "10.5281/zenodo.21711581",
            "2026-07-31",
            "unattended protected-surface audit rejected the edit",
            "| P-H16 | **VERIFIED LIVE (reconciled 2026-08-27 at the unattended-run boundary).**",
            "| M-H2 | **VERIFIED LIVE (reconciled 2026-08-27 at the exact representation ceiling).**",
            "| M-M28 | **EXECUTED (verified 2026-08-27 at the Layer-0 custody ceiling).**",
        ],
        "wave_c": [
            "252 + 840 + 720 + 180 + 10",
            "star^2=(-1)^(25+4)=-1",
            "(10bar,1,3)",
            "(10,1,3)",
            "raw K-self-adjoint",
            "nonzero source-owned VEV",
            "induced 4D mass/seesaw operator",
            "1664/128",
            "dimension of the proposed Y14 end link",
            "noncanonical `RP3 x S6` model",
            "S6 ---> L13=S(nu) ---> P(TX)",
        ],
    }
    for name, needles in required.items():
        for needle in needles:
            if needle not in texts[name]:
                failures.append(f"{name}: missing {needle!r}")
    rows = {row.get("id"): row for row in manifest.get("records", [])}
    expected = {"P-H16": "VERIFIED_LIVE", "M-H2": "VERIFIED_LIVE", "M-M28": "EXECUTED"}
    for row_id, disposition in expected.items():
        row = rows.get(row_id)
        if not row:
            failures.append(f"manifest: missing {row_id}")
        elif row.get("disposition") != disposition:
            failures.append(
                f"manifest: {row_id} is {row.get('disposition')!r}, expected {disposition!r}"
            )
    return failures


def main() -> None:
    texts = {name: path.read_text() for name, path in PATHS.items()}
    manifest = json.loads(MANIFEST.read_text())
    baseline = violations(texts, manifest)
    if baseline:
        raise SystemExit("\n".join(baseline))

    mutations: list[tuple[str, dict[str, str], dict[str, object]]] = []
    for label, name, old, new in [
        ("PP3 DOI loss", "register", "10.5281/zenodo.21502234", "10.5281/zenodo.MISSING"),
        ("protected-boundary loss", "register", "unattended protected-surface audit rejected the edit", "unrestricted edit path"),
        ("Lambda5 dimension drift", "wave_c", "252 + 840 + 720 + 180 + 10", "251 + 840 + 720 + 180 + 10"),
        ("Layer-0 map collapse", "wave_c", "dimension of the proposed Y14 end link", "constructed map to the proposed Y14 end link"),
        ("P-H16 disposition drift", "register", "| P-H16 | **VERIFIED LIVE", "| P-H16 | **EXECUTED"),
    ]:
        changed = dict(texts)
        changed[name] = changed[name].replace(old, new)
        mutations.append((label, changed, deepcopy(manifest)))

    changed_manifest = deepcopy(manifest)
    for row in changed_manifest["records"]:
        if row["id"] == "M-M28":
            row["disposition"] = "VERIFIED_LIVE"
    mutations.append(("M-M28 manifest drift", dict(texts), changed_manifest))

    caught = 0
    for label, changed_texts, changed_manifest in mutations:
        if violations(changed_texts, changed_manifest):
            caught += 1
        else:
            print(f"FAIL :: mutation escaped: {label}")

    check_count = 10 + 11 + 3
    print(
        "PUBLICATION/LAMBDA5/LAYER0 CUSTODY: "
        f"{check_count}/{check_count} checks pass; {caught}/{len(mutations)} mutations caught"
    )
    if caught != len(mutations):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
