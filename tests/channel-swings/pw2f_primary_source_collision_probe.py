#!/usr/bin/env python3
"""Fail-closed primary-source locator and Layer-0 manifest gate for PW2F."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/pw2f-primary-source-collision-manifest.json"

EXACT = TYPE = PLANTED = 0


def strict_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate key: {key}")
        result[key] = value
    return result


def check(label: str, condition: bool) -> None:
    global EXACT
    if not condition:
        raise AssertionError(label)
    EXACT += 1


def type_check(label: str, condition: bool) -> None:
    global TYPE
    if not condition:
        raise AssertionError(label)
    TYPE += 1


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    if false_claim:
        raise AssertionError(f"planted false claim passed: {label}")
    PLANTED += 1


def digest(value: bytes) -> str:
    return sha256(value).hexdigest()


def main() -> None:
    data = json.loads(MANIFEST.read_text(), object_pairs_hook=strict_object)
    rows = data["rows"]
    check("ten unique source collision rows are declared", len(rows) == 10 and len({row["id"] for row in rows}) == 10)
    check(
        "the disposition vocabulary is closed and all three outcomes are exercised",
        set(data["allowed_dispositions"])
        == {"SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-SILENT"}
        == {row["disposition"] for row in rows},
    )

    slices = {}
    for row in rows:
        path = ROOT / row["source_path"]
        raw = path.read_bytes()
        check(f"{row['id']} full-file hash matches", digest(raw) == row["file_sha256"])
        lines = raw.splitlines(keepends=True)
        selected = b"".join(lines[row["line_start"] - 1 : row["line_end"]])
        text = selected.decode("utf-8")
        slices[row["id"]] = text
        check(f"{row['id']} exact locator slice hash matches", digest(selected) == row["slice_sha256"])
        check(
            f"{row['id']} required tokens occur inside its declared slice",
            all(token in text for token in row["required_tokens"]),
        )
        check(
            f"{row['id']} carries typed source and repository objects",
            bool(row["layer_zero_source_object"])
            and bool(row["repository_object"])
            and bool(row["collision"]),
        )
        check(f"{row['id']} declares its evidence grade", bool(row["evidence_grade"]))

    custody = data["primary_draft_custody"]
    custody_path = ROOT / custody["render_receipt_path"]
    check(
        "the normalized draft rows are backed by the official author-PDF digest and rendered/manual receipt",
        custody["pdf_sha256"]
        == "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4"
        and digest(custody_path.read_bytes()) == custody["render_receipt_sha256"]
        and custody["grade"]
        == "AUTHOR_PRIMARY_PDF_WITH_RENDERED_MANUAL_TRANSCRIPTION_RECEIPT",
    )
    absence = data["scoped_absence_search"]
    check(
        "the source-silence receipt records exact searched files, semantic query families, and a non-global scope caveat",
        len(absence["searched_files"]) == 4
        and len(absence["query_families"]) == 5
        and "not a claim about all" in absence["scope_caveat"],
    )
    for item in absence["searched_files"]:
        check(
            f"absence-search corpus hash matches for {item['path']}",
            digest((ROOT / item["path"]).read_bytes()) == item["sha256"],
        )

    type_check(
        "projection/contraction, Xi/Ward, epsilon/h, and trace-reversed/raw forks remain distinct",
        set(data["anti_collapse"].values()) == {"DISTINCT", True},
    )
    type_check(
        "source silence closes no construction blocker",
        data["anti_collapse"]["source_silence_closes_no_blocker"] is True,
    )
    type_check(
        "the three silent rows separately own scoped active-metric/Ward absence, the odot fork, and variation/pairing ownership",
        {row["id"] for row in rows if row["disposition"] == "SOURCE-SILENT"}
        == {
            "PW2F-SRC-08-SCOPED-ACTIVE-METRIC-WARD-SILENCE",
            "PW2F-SRC-09-ODOT-EPSILON-OMEGA-FORK",
            "PW2F-SRC-10-VARIATION-AND-PAIRING-OWNERSHIP",
        },
    )

    projection = slices["PW2F-SRC-04-WGB06-CURVATURE-CONTRACTION"]
    xi = slices["PW2F-SRC-02-WGS04-XI"]
    trace = slices["PW2F-SRC-03-WGA05-TRACE-REVERSAL"]
    contortion = slices["PW2F-SRC-05-WGD01-CONTORTION-SLOT"]
    eddy = slices["PW2F-SRC-07-PORTAL-EDDY"]
    odot_fork = slices["PW2F-SRC-09-ODOT-EPSILON-OMEGA-FORK"]
    reject("swap projection/contraction locator with Xi locator", "contraction operator" in xi)
    reject("swap Xi locator with contortion locator", "Xi_\\omega" in contortion)
    reject("read the trace-reversal locator as support for raw 3,7", "3,7 metric on the fiber, which can't work" not in trace)
    reject("read source epsilon as the synthetic repository h=exp(u)", "h=exp(u)" in contortion)
    reject("attribute the name Shiab to the TOE contraction passage", "Shiab" in projection)
    reject("read the corrected contraction as a grade projector", "grade projector" in projection)
    reject("treat the positive eddy passage itself as an absence certificate", "SOURCE-SILENT" in eddy)
    reject("identify circledot_e with circledot_omega merely because both occur in the draft window", "definitionally identical" in odot_fork)

    total = EXACT + TYPE + PLANTED
    print(
        "PW2F PRIMARY-SOURCE COLLISION MANIFEST: "
        f"{EXACT} exact + {TYPE} type + {PLANTED} planted = {total} PASS"
    )


if __name__ == "__main__":
    main()
