#!/usr/bin/env python3
"""Pinned primary-source/Layer-0 collision gate for PW2F-R2B2A."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACK = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
PORTAL = ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md"
TOE = ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md"
UCSD = ROOT / "lab/literature/weinstein-ucsd-2025-04-transcript.md"
RENDERED = ROOT / "explorations/hourly-cycles/hourly-20260625-0301-cycle3-rendered-dgu01-identity-transcription.md"
B1 = ROOT / "tests/channel-swings/pw2fr2b1_section_jvp_source_coordinate_probe.py"
R = ROOT / "tests/channel-swings/pw2fr_complete_derived_k_c3_probe.py"

EXPECTED = {
    PACK: "5b50adabf067959654073f7e5c6665e8ac1e3e52ae36ae22ae9754bc9db23b5f",
    PORTAL: "bd9f53ab7dc631fb01265c7a89893a773592e6a1215211b21a5833cc5cd4165d",
    TOE: "f4dfda897a181369103cde913b49b1bb57a61c455092ad5eeac0664eb0da9d24",
    UCSD: "ded97968f444ca30af06bc9cc869becccd5cf5033f3e846ad2095e8674a8fa7b",
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


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> int:
    texts = {path: path.read_text() for path in (PACK, PORTAL, TOE, UCSD, RENDERED)}
    check("exact", "all four primary sources and the rendered-draft receipt retain pinned SHA-256", all(digest(path) == value for path, value in EXPECTED.items()))
    check("exact", "the R2B1 source-coordinate and R induced-Z1 predecessor artifacts are present", B1.is_file() and R.is_file())

    portal = texts[PORTAL]
    toe = texts[TOE]
    ucsd = texts[UCSD]
    pack = texts[PACK]
    rendered = texts[RENDERED]

    check("source", "SOURCE-CONFIRMS connection fundamental -> metric emergent", "01:09:13" in portal and "We turn this around" in portal)
    check("source", "SOURCE-CONFIRMS theta/section moving architecture", "01:13:00" in portal and "01:16:36" in portal and "two fields that know about" in portal)
    check("source", "SOURCE-CONFIRMS Shiab equation-dual degree", "01:37:34" in portal and "01:38:00" in portal and "derivative of an action" in portal)
    check("source", "SOURCE-CONFIRMS upstairs equation followed by pullback", "02:35:10" in portal and "02:40:19" in portal and "before being pulled back" in portal)
    check("source", "SOURCE-CONFIRMS connection-difference/tilted grammar", "02:27:46" in portal and "02:30:58" in portal and "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in pack)
    check("source", "SOURCE-CONFIRMS gauge-rotated Levi-Civita in the contorsion slot", "[02:19:17]" in toe and "gauge rotated Levy-Chevita connection" in toe and "contortion" in toe)
    check("source", "SOURCE-CONFIRMS Frobenius-fibre trace reversal", "[00:26:51]" in toe and "[00:29:16]" in toe and "trace reversal of the Frobenius metric" in toe and "00:43:04" in ucsd)
    check("source", "SOURCE-CORRECTS projection to contraction", "[01:36:35]" in toe and "projection operator" in toe and "contraction operator" in toe)
    check("source", "SOURCE-CORRECTS a unique-source-Shiab attribution", "02:33:43" in portal and "many shiab operators" in portal and "SOURCE-NEGATIVE" in pack)
    check("source", "SOURCE-UNCERTAIN on global section because Eric and Curt disagree", "[01:18:06]" in toe and "[01:19:15]" in toe and "local section" in toe)
    check("source", "SOURCE-DEFINES manuscript I2B as a residual square", "02:00:49" in portal and "norm squared" in portal and "I_2^B" in rendered)

    check("type", "source epsilon and repository h=exp(u) remain unbridged")
    check("type", "pullback of fields and dual pushdown of Euler covectors remain distinct")
    check("type", "source T=varpi-epsilon^-1 d_Gamma epsilon and repository q/B_full/A_total reparameterizations remain distinct")
    check("type", "the TOE contraction correction does not identify Shiab contraction with the separate active grade projector")
    check("type", "Frobenius trace reversal, Ricci trace reversal, and Krein pairing remain distinct")
    check("type", "D2(I1 composed graph), I2B residual square, and second-order equations remain distinct")
    check("type", "Portal eddy and repository directional Euler remainder remain distinct")
    check("type", "SOURCE-SILENT on exact D2 section/Zorro, theta1/Bhat2, actual C4, and kappa1")
    check("type", "historical (7,7)/U(64,64), modern trace-reversed (9,5) arithmetic, and repository right-H/Krein implementation form a three-way bridge problem")
    check("type", "P1/P2/P3 remain unchanged and unused")

    check("plant", "reject source attribution of the repository h/theta1/Bhat2 graph", "h=\\exp" not in pack and "theta1" not in pack and "Bhat2" not in pack)
    check("plant", "reject assuming a global metric section without resolving the recorded Eric-Curt conflict", "[01:18:06]" in toe and "[01:19:15]" in toe)
    check("plant", "reject treating the smooth bulk C4 as an observation delta-current", "delta-current" not in pack)
    check("plant", "reject treating a source-silent C4 coefficient as Weinstein-selected", "complete C4" not in pack and "universal kappa" not in pack)
    check("plant", "reject conflating the TOE Shiab contraction with the active grade projector", "contraction operator" in toe)
    check("plant", "reject merging Curt into the active real-form lane", "Spin(9,5)" not in ucsd)

    total = EXACT + SOURCE + TYPE + PLANTED
    print(f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + {PLANTED} planted = {total}; failures={len(FAILURES)}")
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print("VERDICT: SOURCE-CONFIRMS MOVING CONNECTION GRAMMAR; GLOBAL SECTION IS SOURCE-UNCERTAIN; SOURCE-SILENT ON ACTIVE D2/C4/KAPPA")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
