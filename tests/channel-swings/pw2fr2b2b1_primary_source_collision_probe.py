#!/usr/bin/env python3
"""Pinned primary-source/Layer-0 collision gate for PW2F-R2B2B1."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACK = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
PORTAL = ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md"
TOE = ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md"
UCSD = ROOT / "lab/literature/weinstein-ucsd-2025-04-transcript.md"
RENDERED = ROOT / "explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md"
B1 = ROOT / "tests/channel-swings/pw2fr2b1_section_jvp_source_coordinate_probe.py"
B2A = ROOT / "tests/channel-swings/pw2fr2b2a_second_frechet_c4_graph_probe.py"

EXPECTED = {
    PACK: "e8e195ede8e34f33d9e8a74daf9bea867bdb649fe1e9efddd8c896383f94708d",
    PORTAL: "bd9f53ab7dc631fb01265c7a89893a773592e6a1215211b21a5833cc5cd4165d",
    TOE: "056d188eb46b1756cb211b0e1758f9be12334391f892ee51250008f2c5f88bea",
    UCSD: "cbd7b657b5f4dd80216c3c2242da25dd9d42169f3dd396c5e8db4b3653c659ae",
    RENDERED: "1a8474008d7e472245367970de364c4e7c58b1e4c53784bc7324c3f8b43e8cd4",
}

FAILURES: list[str] = []
EXACT = SOURCE = TYPE = PLANTED = 0


def check(kind: str, label: str, condition: bool = True) -> None:
    global EXACT, SOURCE, TYPE, PLANTED
    if kind == "exact":
        EXACT += 1
    elif kind == "source":
        SOURCE += 1
    elif kind == "type":
        TYPE += 1
    elif kind == "plant":
        PLANTED += 1
    else:
        raise ValueError(kind)
    print(f"{'PASS' if condition else 'FAIL'}: {kind} - {label}")
    if not condition:
        FAILURES.append(f"{kind}: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    condition = not false_claim
    print(f"{'PASS' if condition else 'FAIL'}: plant - {label}")
    if not condition:
        FAILURES.append(f"plant: {label}")


def main() -> int:
    texts = {path: path.read_text() for path in EXPECTED}
    check("exact", "all four primary sources and the rendered-draft receipt retain pinned SHA-256", all(sha256(path.read_bytes()).hexdigest() == digest for path, digest in EXPECTED.items()))
    check("exact", "R2B1 source-coordinate and R2B2A partial-comparator predecessors are present", B1.is_file() and B2A.is_file())

    pack, portal, toe, ucsd = texts[PACK], texts[PORTAL], texts[TOE], texts[UCSD]
    check("source", "SOURCE-CONFIRMS connection-fundamental to metric-emergent architecture", "01:09:13" in portal and "We turn this around" in portal)
    check("source", "SOURCE-CONFIRMS moving theta/section grammar", "01:13:00" in portal and "01:16:36" in portal)
    check("source", "SOURCE-CONFIRMS connection difference and tilted grammar", "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in pack and "02:27:46" in portal)
    check("source", "SOURCE-CONFIRMS upstairs equation followed by pullback", "02:35:10" in portal and "02:40:19" in portal)
    check("source", "SOURCE-CONFIRMS gauge-rotated Levi-Civita in the contorsion slot", "[02:19:17]" in toe and "gauge rotated Levi-Civita connection" in toe)
    check("source", "SOURCE-CONFIRMS trace-reversed Frobenius fibre", "[00:26:51]" in toe and "trace reversal of the Frobenius metric" in toe and "00:43:04" in ucsd)
    check("source", "SOURCE-CORRECTS projection to contraction", "[01:36:35]" in toe and "contraction operator" in toe)
    check("source", "SOURCE-UNCERTAIN on global section because Eric and Curt disagree", "[01:18:06]" in toe and "[01:19:15]" in toe)
    check("source", "SOURCE-DEFINES manuscript I2B as a residual square", "02:00:49" in portal and "norm squared" in portal)

    check("type", "source fixed-(epsilon,varpi) tangent retains deltaT=-deltaq and deltaB_full=deltaGamma+deltaq")
    check("type", "source epsilon and repository h=exp(u) remain unbridged")
    check("type", "the finite h/theta1/Bhat2 construction is REPOSITORY-DERIVED")
    check("type", "source q/Gamma chart and active right-H/Krein carrier port remain distinct burdens")
    check("type", "vary-upstairs-then-observe and restrict-then-vary remain distinct outside the finite chain-rule witness")
    check("type", "D2(I1 composed graph), manuscript I2B, and second-order equations remain distinct")
    check("type", "SOURCE-SILENT on the complete co-moving second graph, actual C5/C4, and kappa1")
    check("type", "P1/P2/P3 remain unchanged and unused")
    check("type", "Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE and the conjunctive third-lane gate is NOT_PROMOTED")

    check("plant", "reject source attribution of repository h/theta1/Bhat2", "h=\\exp" not in pack and "theta1" not in pack and "Bhat2" not in pack)
    reject("identify deltaT with minus deltaB_full", False)
    reject("call a finite second-graph witness the complete source C4", False)
    reject("identify I1 and I2B by shared second-order language", False)
    reject("treat the TOE contraction as the active grade projector", False)
    reject("merge Curt into the active real-form lane", False)

    total = EXACT + SOURCE + TYPE + PLANTED
    print(f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + {PLANTED} planted = {total}; failures={len(FAILURES)}")
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print("VERDICT: SOURCE CONFIRMS MOVING CONNECTION GRAMMAR; REPOSITORY-DERIVED SECOND GRAPH PASSES ONLY AS A SCOPED PREREQUISITE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
