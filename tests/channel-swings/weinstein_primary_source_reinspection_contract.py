#!/usr/bin/env python3
"""Contract for the 2026-07-30 Weinstein primary-source reinspection.

This script checks the evidence/disposition ledger and the ordering of the
recommended construction swing.  It does not verify Weinstein's mathematics,
derive a source action, prove a Noether identity, or test a physical model.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_PACK = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
ANALYSIS = (
    ROOT
    / "explorations/weinstein-primary-source-reinspection-overlooked-answers-2026-07-30.md"
)
N1 = ROOT / "explorations/unified-source-datum-packet-v0-2026-07-30.md"
N3 = ROOT / "explorations/unified-source-datum-variational-emission-map-2026-07-30.md"


@dataclass(frozen=True)
class Source:
    source_id: str
    grade: str
    local_or_official_locator: str
    construction_bearing: bool


@dataclass(frozen=True)
class Finding:
    finding_id: str
    source_id: str
    locator: str
    disposition: str
    owner: str
    layer0: str
    current_blocker: str
    recommended: bool
    closes_blocker: bool = False
    count_claim: bool = False


@dataclass(frozen=True)
class Swing:
    order: int
    swing_id: str
    consumes: tuple[str, ...]
    emits: tuple[str, ...]
    depends_on: tuple[str, ...]


ALLOWED_DISPOSITIONS = {
    "SOURCE-EXPLICIT",
    "SOURCE-BOUND",
    "SOURCE-NEGATIVE",
    "ALREADY-ABSORBED",
    "NEW-CONSTRUCTION-PROMPT",
}

SOURCES = (
    Source(
        "WG-2021-DRAFT",
        "author-primary",
        "official PDF, 69 pages, prior repo checksum receipt",
        True,
    ),
    Source(
        "WG-2013-2020-PORTAL",
        "official-transcript",
        "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md",
        True,
    ),
    Source(
        "WG-2021-ITI-REVEALED",
        "official-editorial-transcript",
        "official Portal Group transcript",
        True,
    ),
    Source(
        "WG-2020-ITI-49",
        "automated-caption-discovery",
        "temporary caption extraction; no local transcript committed",
        False,
    ),
    Source(
        "WG-2020-DARKHORSE",
        "automated-caption-discovery",
        "temporary caption extraction; no local transcript committed",
        False,
    ),
    Source(
        "WG-2025-UCSD",
        "local-raw-transcript",
        "papers/drafts/Transcript into the impossible.md",
        True,
    ),
    Source(
        "WG-2025-TOE",
        "local-automated-transcript-already-mined",
        "lab/sources/transcripts/toe-weinstein-gu-40-years.md",
        True,
    ),
)

FINDINGS = (
    Finding(
        "F-ACTION",
        "WG-2021-DRAFT",
        "sec. 9.1, eqs. 9.1-9.7; sec. 12.4",
        "ALREADY-ABSORBED",
        "explorations/research-cycles/hourly-20260626-1003-cycle3-tau-source-locator-packet.md",
        "I1B and N1 packet are DIFFERENT-OBJECTS pending a map",
        "source-action functional class",
        False,
    ),
    Finding(
        "F-TOTAL-RESIDUAL",
        "WG-2021-DRAFT",
        "eqs. 9.18-9.20",
        "NEW-CONSTRUCTION-PROMPT",
        "current N1/N3 comparison; source formula owned by rendered DGU transcription",
        "UpsilonF_ad and J_D+J_F are SAME-ARENA-CANDIDATES only",
        "J_bridge disposition and full connection Euler covector",
        True,
    ),
    Finding(
        "F-QUADRATIC-EXACTNESS",
        "WG-2013-2020-PORTAL",
        "02:35:10 plus draft eq. 9.4",
        "NEW-CONSTRUCTION-PROMPT",
        "current N1/N3 exactness comparison; locator owned by Oxford frame receipts",
        "source eddy and N1 quadratic terms are not identified",
        "gauge exactness, Noether identity, and double counting",
        True,
    ),
    Finding(
        "F-REDUNDANCY",
        "WG-2021-DRAFT",
        "eqs. 9.5-9.6, Xi=D_omega Upsilon",
        "SOURCE-BOUND",
        "explorations/research-cycles/hourly-20260625-0502-cycle2-author-manuscript-dgu-vz-action-receipt-gate.md",
        "redundant Euler relation is not automatically an off-shell Noether identity",
        "gauge Noether identity and Euler-ideal factorization",
        False,
    ),
    Finding(
        "F-SPINLESS-VEV",
        "WG-2021-DRAFT",
        "sec. 12.9, eqs. 12.12-12.21",
        "NEW-CONSTRUCTION-PROMPT",
        "current full-20 placement comparison; coarse VEV claim owned by escape-corners",
        "R/4 toy, spinless gauge field, and full-20 mass map are not yet one typed map",
        "zero-order P0/rho/Y/reality placement and cosmological linkage",
        True,
    ),
    Finding(
        "F-EPSILON",
        "WG-2025-UCSD",
        "00:17:01-00:25:03 and draft secs. 6-7",
        "SOURCE-BOUND",
        "existing distortion-vacuum and tau source audits",
        "source gauge transformation epsilon may be a homonym of dynamical epsilon_IG",
        "full-Sp soldering orbit",
        False,
    ),
    Finding(
        "F-VEV-OPEN",
        "WG-2021-ITI-REVEALED",
        "01:41:43",
        "SOURCE-NEGATIVE",
        "this source packet",
        "source explicitly leaves VEV choice/location open",
        "vacuum/external-datum selection",
        False,
    ),
    Finding(
        "F-SHIAB-OPEN",
        "WG-2021-ITI-REVEALED",
        "01:41:43-01:42:50 and draft sec. 8.2",
        "SOURCE-NEGATIVE",
        "existing Shiab source receipts",
        "preferred projection is not supplied",
        "source-selected contraction",
        False,
    ),
    Finding(
        "F-DARKHORSE-HOMONYM",
        "WG-2020-DARKHORSE",
        "approximately 00:29, economics/social-choice discussion",
        "SOURCE-NEGATIVE",
        "this source packet",
        "extra piece of data is NOT a GU external datum",
        "none; planted Layer-0 control",
        False,
    ),
    Finding(
        "F-TOE-UNRELEASED",
        "WG-2025-TOE",
        "02:44:06-02:45:43",
        "ALREADY-ABSORBED",
        "lab/sources/claim-mining-toe-weinstein-2026-07-20.md",
        "unreleased cyclic complex is not a source-action or count receipt",
        "operator/domain and generation mechanism",
        False,
    ),
)

SWINGS = (
    Swing(
        1,
        "WSR-1-TOTAL-RESIDUAL-DICTIONARY",
        ("I1B", "UpsilonB", "UpsilonF", "N1", "N3"),
        (
            "native-real Layer-0 dictionary",
            "delta_A/U/epsilon of source-shaped rival",
            "J_bridge disposition",
        ),
        (),
    ),
    Swing(
        2,
        "WSR-2-QUADRATIC-EXACTNESS",
        ("source eddy coefficients", "WSR-1 dictionary", "gauge laws"),
        (
            "gauge contraction of full Euler covector",
            "wrong-coefficient controls",
            "first-order/square/double-count ledger",
        ),
        ("WSR-1-TOTAL-RESIDUAL-DICTIONARY",),
    ),
    Swing(
        3,
        "WSR-3-SPINLESS-VEV-PLACEMENT",
        ("stable T_omega/theta dictionary", "full-20 ledger", "five physics legs"),
        (
            "Pi_spin0 carrier map",
            "K/C zero-order placements",
            "shared mass/cosmology constraint-surplus verdict",
        ),
        (
            "WSR-1-TOTAL-RESIDUAL-DICTIONARY",
            "WSR-2-QUADRATIC-EXACTNESS",
        ),
    ),
)


def check(label: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"[PASS] {label}")


def finding_is_admissible(finding: Finding, sources: dict[str, Source]) -> bool:
    source = sources[finding.source_id]
    return (
        finding.disposition in ALLOWED_DISPOSITIONS
        and bool(finding.locator)
        and bool(finding.owner)
        and bool(finding.layer0)
        and not finding.closes_blocker
        and not finding.count_claim
        and not (
            finding.recommended
            and (
                not source.construction_bearing
                or finding.disposition == "SOURCE-NEGATIVE"
            )
        )
    )


def swings_are_topological(swings: tuple[Swing, ...]) -> bool:
    seen: set[str] = set()
    for expected_order, swing in enumerate(swings, start=1):
        if swing.order != expected_order:
            return False
        if not set(swing.depends_on).issubset(seen):
            return False
        seen.add(swing.swing_id)
    return True


def main() -> None:
    print("Weinstein primary-source reinspection contract")
    source_by_id = {source.source_id: source for source in SOURCES}

    required_sources = {
        "WG-2021-DRAFT",
        "WG-2013-2020-PORTAL",
        "WG-2021-ITI-REVEALED",
        "WG-2020-ITI-49",
        "WG-2020-DARKHORSE",
        "WG-2025-UCSD",
        "WG-2025-TOE",
    }
    check("all seven requested/core source surfaces are represented", set(source_by_id) == required_sources)
    check("source identifiers are unique", len(source_by_id) == len(SOURCES))
    check(
        "the author draft and Portal/Oxford transcript are construction-bearing",
        source_by_id["WG-2021-DRAFT"].construction_bearing
        and source_by_id["WG-2013-2020-PORTAL"].construction_bearing,
    )
    check(
        "DarkHorse and 2020 Into the Impossible captions are discovery-only",
        not source_by_id["WG-2020-DARKHORSE"].construction_bearing
        and not source_by_id["WG-2020-ITI-49"].construction_bearing,
    )

    check(
        "every finding has locator, owner, Layer-0 state, and honest disposition",
        all(finding_is_admissible(finding, source_by_id) for finding in FINDINGS),
    )
    check(
        "no source row is promoted to a closed N3 blocker",
        all(not finding.closes_blocker for finding in FINDINGS),
    )
    check(
        "no decomposition, cyclic complex, or source phrase is promoted to a count",
        all(not finding.count_claim for finding in FINDINGS),
    )

    recommended = {finding.finding_id for finding in FINDINGS if finding.recommended}
    check(
        "exactly the three construction-bearing comparisons are recommended",
        recommended
        == {
            "F-TOTAL-RESIDUAL",
            "F-QUADRATIC-EXACTNESS",
            "F-SPINLESS-VEV",
        },
    )
    check(
        "the first-order action is recorded as already owned, not rediscovered",
        next(f for f in FINDINGS if f.finding_id == "F-ACTION").disposition
        == "ALREADY-ABSORBED",
    )
    check(
        "the DarkHorse extra-data phrase is quarantined as a homonym",
        "NOT a GU external datum"
        in next(
            f for f in FINDINGS if f.finding_id == "F-DARKHORSE-HOMONYM"
        ).layer0,
    )
    check(
        "Xi=D Upsilon is not mislabeled as the Noether identity",
        "not automatically"
        in next(f for f in FINDINGS if f.finding_id == "F-REDUNDANCY").layer0,
    )

    check("recommended swings are ordered by their declared dependencies", swings_are_topological(SWINGS))
    check(
        "zero-order placement waits for the action dictionary and exactness pass",
        SWINGS[2].depends_on
        == (
            "WSR-1-TOTAL-RESIDUAL-DICTIONARY",
            "WSR-2-QUADRATIC-EXACTNESS",
        ),
    )

    source_text = SOURCE_PACK.read_text(encoding="utf-8")
    analysis_text = ANALYSIS.read_text(encoding="utf-8")
    n1_text = N1.read_text(encoding="utf-8")
    n3_text = N3.read_text(encoding="utf-8")
    for token in (
        "WGS-02",
        "WGS-03",
        "WGS-05",
        "Layer-0 dictionary",
        "SOURCE-NEGATIVE",
    ):
        check(f"source packet contains required token {token!r}", token in source_text)
    for token in (
        "Rival 1",
        "Rival 2",
        "Rival 3",
        "Constraint-surplus test",
        "Best next swing",
    ):
        check(f"analysis contains required token {token!r}", token in analysis_text)
    check(
        "comparison target still contains the explicit distortion bridge",
        "the W203 ultralocal bridge" in n1_text
        and "The source current is an action derivative" in n1_text,
    )
    check(
        "comparison target still names all eight missing maps",
        "The eight named missing maps are" in n3_text
        and "typed disposition of" in n3_text
        and "twisted subprincipal convention" in n3_text,
    )

    # Discriminating plants: each tempting shortcut must fail admission.
    darkhorse = next(f for f in FINDINGS if f.finding_id == "F-DARKHORSE-HOMONYM")
    planted_darkhorse_answer = replace(
        darkhorse,
        disposition="NEW-CONSTRUCTION-PROMPT",
        recommended=True,
    )
    check(
        "plant: discovery-grade DarkHorse homonym cannot become a recommended answer",
        not finding_is_admissible(planted_darkhorse_answer, source_by_id),
    )

    total_residual = next(f for f in FINDINGS if f.finding_id == "F-TOTAL-RESIDUAL")
    planted_closed = replace(total_residual, closes_blocker=True)
    check(
        "plant: a source formula cannot silently close the current/Riesz blocker",
        not finding_is_admissible(planted_closed, source_by_id),
    )

    planted_count = replace(
        next(f for f in FINDINGS if f.finding_id == "F-TOE-UNRELEASED"),
        count_claim=True,
    )
    check(
        "plant: the unreleased cyclic complex cannot become a generation count",
        not finding_is_admissible(planted_count, source_by_id),
    )

    planted_bad_order = (SWINGS[2], SWINGS[0], SWINGS[1])
    check(
        "plant: projecting the spinless VEV before the field dictionary is rejected",
        not swings_are_topological(planted_bad_order),
    )

    print(
        "\nVERDICT: contract passes. The source corpus emits three bounded "
        "construction comparisons and zero closed physical claims."
    )


if __name__ == "__main__":
    main()
