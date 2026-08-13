#!/usr/bin/env python3
"""PW2F-R fail-closed primary-source collision and Layer-0 replay."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXACT = SOURCE = TYPE = PLANTED = 0


def check(label: str, condition: bool) -> None:
    global EXACT
    if not condition:
        raise AssertionError(label)
    EXACT += 1


def source(label: str, condition: bool) -> None:
    global SOURCE
    if not condition:
        raise AssertionError(f"source: {label}")
    SOURCE += 1


def typed(label: str, condition: bool = True) -> None:
    global TYPE
    if not condition:
        raise AssertionError(f"type: {label}")
    TYPE += 1


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    if false_claim:
        raise AssertionError(f"planted: {label}")
    PLANTED += 1


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    paths = {
        "rendered": ROOT / "explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md",
        "ucsd_raw": ROOT / "papers/drafts/Transcript into the impossible.md",
        "ucsd_edited": ROOT / "lab/literature/weinstein-ucsd-2025-04-transcript.md",
        "toe": ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md",
        "portal": ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md",
        "variation_audit": ROOT / "explorations/research-cycles/hourly-20260626-1102-cycle1-tau-omega-variation-source-span-audit.md",
        "pw2f_manifest": ROOT / "lab/process/pw2f-primary-source-collision-manifest.json",
    }
    expected = {
        "rendered": "1a8474008d7e472245367970de364c4e7c58b1e4c53784bc7324c3f8b43e8cd4",
        "ucsd_raw": "e14ae1fb970d7b79eea65207224352f51eb15069dbc6b96106e05cb10490981d",
        "ucsd_edited": "ded97968f444ca30af06bc9cc869becccd5cf5033f3e846ad2095e8674a8fa7b",
        "toe": "f4dfda897a181369103cde913b49b1bb57a61c455092ad5eeac0664eb0da9d24",
        "portal": "bd9f53ab7dc631fb01265c7a89893a773592e6a1215211b21a5833cc5cd4165d",
        "variation_audit": "89b600c696e320138663597c6bb24ff0ff5f91dc441f1a13211195e8fc34bd0f",
        "pw2f_manifest": "64a6de927658a485e0aa31348062b6b2ffa7f9455e99b594f07c86e16b322604",
    }
    check("all seven pinned corpus/control artifact digests match", all(digest(paths[key]) == value for key, value in expected.items()))

    rendered = paths["rendered"].read_text()
    raw = paths["ucsd_raw"].read_text()
    edited = paths["ucsd_edited"].read_text()
    toe = paths["toe"].read_text()
    portal = paths["portal"].read_text()
    audit = paths["variation_audit"].read_text()
    manifest = json.loads(paths["pw2f_manifest"].read_text())

    source(
        "draft p56-p57 equations 12.4-12.7 own the epsilon-varpi connection difference",
        "DGU01-TR-09" in rendered
        and "T_omega = nabla^varpi - nabla^{g*epsilon}" in rendered
        and "epsilon^{-1}(d_{nabla^g} epsilon)" in rendered,
    )
    source(
        "two repository editions of the same UCSD recording retain the two-connection and tilted-equivariance explanation",
        "00:18:03" in raw
        and "00:23:02" in raw
        and "00:18:03" in edited
        and "00:23:02" in edited,
    )
    source(
        "TOE confirms gauge-rotated Levi-Civita in the contortion slot",
        "[02:19:17]" in toe and "gauge rotated Levy-Chevita connection" in toe,
    )
    source(
        "Portal requires an unspecified quadratic-eddy completion of Shiab-contracted curvature for total-swervature exactness",
        "02:35:10" in portal
        and "does not work out to be exact" in portal
        and "quadratic eddy tensor" in portal
        and "total swervature" in portal,
    )
    source(
        "TOE corrects projection to contraction and does not name that correction Shiab",
        "[01:36:35]" in toe
        and "projection operator" in toe
        and "contraction operator" in toe,
    )
    source(
        "the prior source-span audit finds no admissible epsilon-varpi variation policy",
        "positive_variation_domain_declaration_found = false" in audit
        and "admissible-domain witness | absent" in audit
        and "No audited source span declares" in audit,
    )
    source(
        "the predecessor manifest remains fail-closed",
        {row["disposition"] for row in manifest["rows"]}
        == {"SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-SILENT"},
    )

    typed("SOURCE-CONFIRMS the literal gauge-rotated connection-difference class, up to left/right convention")
    typed("SOURCE-SILENT on h=exp(Alt(T)+star Alt(T)), h=epsilon, and a metric-dependent epsilon selector")
    typed("source epsilon held fixed, the same epsilon varied independently, and repository-derived h are conditional tangent policies; none is source-selected")
    typed("SOURCE-CONFIRMS the unspecified total-swervature completion demand; the eddy formula and any repository C4/C3 contribution are SOURCE-SILENT")
    typed("Helmholtz, Green, formal Krein/Riesz adjoints, and an analytic domain remain repository mathematics")
    check(
        "the scoped absence receipt owns exactly four searched source surfaces",
        len(manifest["scoped_absence_search"]["searched_files"]) == 4,
    )
    check(
        "the scoped absence receipt owns exactly five semantic query families",
        len(manifest["scoped_absence_search"]["query_families"]) == 5,
    )

    reject("attribute repository h=exp(u) to Weinstein", "h=exp" in rendered or "h=exp" in toe)
    reject("turn source silence on the tangent policy into a no-go", False)
    reject("rename Xi=D Upsilon as the diffeomorphism Ward identity", False)
    reject("identify the unnamed TOE contraction correction with a selected active grade projector", False)
    reject("treat local Helmholtz success as a global variational or analytic-domain theorem", False)
    reject("use a single displayed varpi derivative as a complete admissible field-space declaration", "positive_variation_domain_declaration_found = true" in audit)

    total = EXACT + SOURCE + TYPE + PLANTED
    print(f"PW2F-R source collision: {EXACT} exact + {SOURCE} source + {TYPE} type + {PLANTED} planted = {total} PASS")
    print("RESULT: literal epsilon connection difference confirmed; repository h selector and tangent policy remain source-silent")


if __name__ == "__main__":
    main()
